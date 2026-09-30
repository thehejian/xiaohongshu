# langgraph — 小红书创作发布流水线（LangGraph 状态机）

把 `AGENTS.md` 的 0~6 步 SOP 固化成状态机：**每步产物落 state、断点可续、发布必过人工闸门**。
P0 = 图骨架 + 读类节点真实执行 + 全链路演练（已完成）；LLM/飞书/发布的真实分支是显式 `NotImplementedError`，P1 再接。

## 用法

```bash
export PATH="$HOME/.local/bin:/opt/homebrew/bin:$PATH"
uv sync                       # 首次

# 演练（默认，就是 --dry-run）：选题→查重→正文→验证→生图→飞书桩→⏸审核闸门
uv run cli.py run --series history --topic 454

# 审核续跑（闸门只吃这四个词；空线程/未到闸门会友好报错 exit 2，不再 KeyError）
uv run cli.py run --series history --topic 454 --resume approve   # → 存草稿 → 记台账
uv run cli.py run --series history --topic 454 --resume rewrite   # → 回写正文
uv run cli.py run --series history --topic 454 --resume redraw    # → 回重新生图
uv run cli.py run --series history --topic 454 --resume archive   # → 只归档不发布

# 批量一键：到闸门自动 archive（仅记台账+commit+push，绝不存草稿），一条命令跑完一题
uv run cli.py run --series history --topic 517 --real --auto-archive
for n in $(seq 517 525); do uv run cli.py run --series history --topic $n --real --auto-archive || true; done

# 单节点续跑（节点 raise 后不整题重跑，保住已通过的上游产物）
uv run cli.py run --series history --topic 516 --real --thread history-516-2 --jump-to write_prompts

uv run pytest -q             # 红线测试：未经 approve 不可达 publish
```

- **`--real` 才真实执行**；P0 阶段所有花钱/触达外部的节点会 `NotImplementedError` 快速失败，不会半途产生副作用。
- 断点存 `langgraph/.state/graph.db`（SQLite，gitignore）；同一 `--thread`（默认 `<series>-<topic>`）才能续跑。
- 演练产物写 `langgraph/.state/dryrun/topic-<N>/`，**不碰共享的 `image-cards/` 与台账**。

## 图结构

```
resolve_topic → dedup ─skip→ report_skip → END
      ↓ continue
 write_article → verify_article ─3次不过→ report_error → END
      ↓ pass                                ↓ pass
 fact_check → write_prompts → gen_images → verify_images → create_feishu
      ↓ travel 无图直连                    ↑____重试____↓
                                  human_review ⏸ interrupt（唯一闸门）
   approve → publish_draft → record → END
   rewrite → write_article   redraw → gen_images   archive → record
   非法输入 → 再次 interrupt
```

## 红线怎么落实（对应 AGENTS.md Hard rules）

| 红线 | 机制 |
|------|------|
| 审核确认才能存草稿 | `human_review` 是唯一 `interrupt`；`route_review` 只认 approve 才连 `publish_draft`；节点内部再验一次 decision（双保险，见 `nodes.publish_draft`） |
| 每次只写一个、写完停下 | 图跑到 `create_feishu` 后必然中断，无自动续跑 |
| 不占位符 doc_id | `record` 在非演练下校验 `ledger_line` 后才追加台账 |
| gen_fixed.py copy | `gen_images` 真实分支实现时强制从上一成功案例 copy（P1） |

## 与 AGENTS.md 的关系（唯一事实源）

- **流程步骤以本图为准**；`AGENTS.md` 的「完整作业流程」保留为手动兜底/排障路径。
- **写作风格正本在 `AGENTS.md` 的 Style Preferences 节**；`xhs_graph/prompts/style.py` 是它的编译产物 —— **改那边必须同步这边**。
- 三系列参数集中在 `xhs_graph/profiles.py`（飞书 folder_token、字数区间、生图张数、串行验图等）。

## P1 完成清单（2026-09-30 实测通过）

1. ✅ `write_article` → Agnes LLM（`agnes-2.5-flash`，重试 ≤3 轮，失败反馈含具体 problems）
2. ✅ `dedup` LLM 判重（确定性 grep 命中后调 `agnes-3.0-flash` 判定）
3. ✅ `fact_check` → Agnes 史实核查（LLM JSON 解析失败降级 pass + 记 notes）
4. ✅ `write_prompts` → LLM 生成 3 条水墨风格提示词（含禁词校验 + 光线统一校验 + 2 轮重试）
5. ✅ `gen_images` → copy gen_fixed.py（红线）+ 真实调用 Agnes 生图（幂等：已有图不重生成）
6. ✅ `verify_images` → 结构检查（PNG 魔数 + 宽高比≈3:4 + 大小≥50KB）；视觉 10 项自查留给人审
7. ✅ `create_feishu` → lark-cli docs +create + 串行 media-insert（sleep 3）
8. ✅ `publish_draft` → creator-profile + publish --draft true（仅 approve 后可达）
9. ✅ `record` → 追加台账 + git add/commit + **`git push origin HEAD` 自动推送 GitHub**（push 失败/超时不致命：本地已提交，record_note 会带 ⚠ 提示，稍后手动 `git push` 补推）
10. ✅ 默认 dry-run，`--real` 才真实执行；红线由 interrupt + route_review 双保险守护

## 经验教训（2026-09-30 批量 470–485 实战）

### 1. LLM 在文末塞代码块元信息（475 事故，用户发现"正文下面多了代码块"）

- **现象**：飞书文档正文尾部多出 `<pre><code>` 块，内容是 `---` + `**字数统计**：全文约782字…` 这类 LLM 自评元信息
- **根因**：`_strip_fences` 只在**整篇**以 ``` 开头时才剥围栏，正文中/文末的代码块漏网；`verify_article` 也不检查
- **修复**：
  - `_strip_fences` → `re.sub(r"```[a-zA-Z]*\s*[\s\S]*?```", ...)` 删全文任意位置代码块 + 循环剥文末孤立 `---`/`字数统计` 行
  - `verify_article` 新增硬检查：含 ``` 或行首 `字数统计` → 记 problem → 图路由打回重写（实测拦下一稿 5867 字带围栏废稿）
- **教训**：**只剥首尾围栏是不够的**，LLM 会把元信息包在任意位置的代码块里；结构类问题要同时进"清洗"和"验证"两层

### 2. 旧 checkpoint 残留 attempts → 幽灵报错"重试超限"（474/476/483）

- **现象**：第一次重跑就报 `验证/生图重试超限`，但明明 verify passed、甚至只跑了一轮
- **根因**：非 `--resume` 重跑复用同一 thread（`history-<N>`），LangGraph 从旧 checkpoint 继承 `attempts` 计数（上次已耗尽 3 次）→ `_n()` +1 即触发 `>= 3` 路由到 `report_error`
- **修复**：`cli.py` 全新启动时检测 `graph.get_state().values` 非空 → 自动换新线程 `<thread>-2/-3…` 并打印 `⚠ 旧线程 …改用新线程`
- **连锁坑**：**归档时必须用跑出成果的那个线程** — 若运行时自动换了线程，`--resume archive` 要带 `--thread history-<N>-2`，默认旧线程拿到的是失败态（曾把 483 归档到旧错误态上）
- **教训**：stateful 图的"全新启动"≠ 旧状态无害；断点库不清就必须换线程

### 3. dedup 见 article.md 即 skip —— 重跑前必须清理残留目录

- 上一轮失败/调试残留的 `image-cards/topic-N/article.md` 会让重跑直接 `dedup skip`（474/475/476 均踩到）
- 重跑前：`rm -rf image-cards/topic-N`——**但先查 `.feishu_uploaded`，已入台账的目录绝不能删**（本次曾用宽模式 `topic-47[0-9]` 误删已提交的 470–473，靠 `git checkout --` 恢复）
- 删目录的正确顺序：查台账无记录 → 查 git 是否已提交 → 再删

### 4. fact_check 偶发误判（483）

- `agnes-2.5-flash` 偶尔对没问题的稿返回 `passed:false`；同一稿手动重跑 fact_check 两次全过
- `report_error` 现已附带 `fact_check` 与 `attempts` 内容——先看它报的具体 issues，是真史实问题才改稿，解析/模型抽风直接重跑即可

### 5. 本批工具链备忘

- 批量归档：`for n in …; do uv run cli.py run --series history --topic $n --real --resume archive; done`
- 换过线程的主题归档要显式 `--thread <原线程>-2`
- 失败主题重跑 = 查台账 → 删残留目录 → `--real` 重跑 → 闸门后 archive

### 6. 第二批（486–495）新增教训

- **fact_check 打回必须把 issues 喂给重写**（486）：原实现只把 `verify.problems` 反馈进 `write_article`，fact 打回的稿重写时拿不到原因 → 盲改必然二次失败 → report_error。已修：`state["fact_check"].issues` 拼进 feedback（`史实问题（必须修正）：…`）。**教训：每一条打回路由都要检查它的"原因"是否进了下一次重试的输入**
- **节点内重试耗尽直接 raise 会把整图打崩**（487）：`write_prompts` 两轮校验不过就 `RuntimeError`，进程只在流里打一行异常，`grep` 关键字过滤时完全看不见 → 表现为"跑了一半静默停止"。已修：前缀/收尾缺失改为**自动修补**（固定公式直接补齐再验，禁词/条数仍靠重试）+ 重试 2→4 轮。排障手段：`graph.get_state({"configurable":{"thread_id":...}})` 看 `tasks[].error` 和 `next` 定位断点
- **换线程号是累积的，以实际打印为准**：487 先后出现 `-2`（中间探查跑出残留）、最终 `-3`；归档时照抄运行时打印的"改用新线程 XXX"，不要想当然用 `-2`
- **LLM 查重首次实战拦截**（494）：与 480「东吴开发江南」主体事件相同被判 skip，序号照进不回填——查重三步法的 LLM 判定层有效
- **verify 拦截类型本批全出现**：英文 `vs`/`tags`、标题 20 字、1410 字超长、563 字不足——反馈重写一轮即过，说明 verify→feedback 通路健康
- **fact_check 拦下真史实错误**（486 原稿"公元223年"vs 夷陵之战 222 年）——史实核查不是摆设，报 issues 时先核实再改稿

### 7. 第三批（496–505）新增教训

- **空稿静默重试是浪费**（499/503 中招）：`_strip_fences` 把纯元信息输出剥空后原实现 `continue` 盲试 6 轮，最后写入空文件白耗一次图 attempts。已修：空输出也**带反馈**重试（明确要求输出"标题+空行+正文+tags"结构）
- **report_error 先重跑再改稿**：498/499 三轮 attempts 耗尽后，`rm article.md` + 重跑（自动新线程）**一次全过**——多为 LLM 单轮方差（英文词混入、标题超长、空输出轮替出现），不是内容本身有问题。判定标准：重跑一次还栽在**同类**问题上才人工介入
- **push 不致命机制实战验证**：496 归档时撞 `Connection reset by peer`，record_note 带 ⚠ 继续；下一次归档的 push 自动把 496 的提交一起带上去——无需人工补推
- **verify 元信息检查实战**：497 首轮"正文含「字数统计」元信息行"被拦（475 修复的第二道防线生效）；英文 `think/already/anth`、24 字标题、1195 字超长均一轮反馈重修即过
- 归档带 `⚠ push 失败` 时**不用管**，看下一条 record_note 是否"已推送 GitHub"即可确认补齐

### 8. 第四批（499/504 修订实战）新增教训

- **单图重生成仍可能撞风格漂移**（499 图三）：即便带 `ref=01-cover.png` + 固定 `agnes-image-2.1-flash`，首轮生成的图仍然是"清透线描+平涂"而非"水墨晕染"（与 01/02 的笔触/底色不一致）。必须在 prompt 末尾追加**正向风格锚点 + 反向禁词**：
  - 正向：`Traditional Chinese ink-and-wash figure painting, wet brush washes with soft bleeding edges, visible watercolor gradients and paper grain, muted desaturated earth tones, hand-painted loose brushwork`
  - 反向：`No clean digital outlines, no flat cel shading, no cartoon style, no glossy digital rendering`
  - 结论：**参考图能纠色调，但画风锁定还得靠 prompt 文字**；遇到风格漂移先加风格关键词而不是换 key/模型
- **lark-cli 在非交互 shell 里需要显式 PATH**（两处缺失都踩过）：
  - `~/.npm-global/bin/lark-cli` 需要 node，node 在 `/opt/homebrew/bin/node`，但非交互 shell 不含该目录 → `env: node: No such file or directory`
  - 必须 `export PATH="$HOME/.npm-global/bin:/opt/homebrew/bin:$PATH"` 才能跑 `lark-cli docs +create` / `+media-insert`
- **GitHub HTTP 500 是瞬态错误，重试即成**（2026-09-30 首次 push 遇 Internal Server Error 被拒，sleep 5 后重试成功 `45cb19b..91f02a0`）。日志里 `gh: command not found` 只是 credential helper 提示，不影响推送结果
- **修订后必须新建飞书文档（硬规则不变）**：499 重写图三、504 改标题都走了 `docs +create` 新建路径，旧文档 `BRwtdTAN…/VgykdOeb…` 留在飞书但不更新。台账 append 新 token 行（格式 `NNN|topic-NNN|新token`）供追溯，原 token 仍保留在上一条
- **图片文件 gitignore，修订提交只含元数据**：`*.png` 被 `.gitignore` 排除，`git add -f` 也不生效（被 ignore 拦截不报错但实际不 add）。因此修订类 commit 只 `git add` 台账 + `prompts/*.md` + `article.md`，图片本身靠飞书文档承载新版本

### 9. 第五批（506–515）新增教训

- **fact_check 拦截的具体数字问题需要改标题而非正文**（514）：原稿 `一场暴雨击溃三十万魏军` 的 `三十万` 属素材未提供的具体数字，节点内 2 轮重写后 fact_check 仍报同一问题。正确修法：**把具体数字从标题里去掉**（改为 `数十万`），正文保持素材原文不碰；教训：fact_check 报 "标题使用具体数字而素材未提供" 时，改标题比改正文更干净
- **事实核查打回不等于节点内重试有效**（508/514）：两道题都是 fact_check 打回后 retry → 同一 issue 再次出现 → `report_error`。**判定标准**：fact_check 报的是 **LLM 对素材解读**（如"赵云亲自烧毁栈道"与素材措辞偏差），可以人工改稿绕过；报的是 **数字/日期/人名等硬事实**（如"三十万"素材说"数十万"），必须改标题或重写，不能靠 retry 蒙混
- **topic 目录被误删后 prompt 需要手补**（508/514 事故）：执行 `rm -rf image-cards/topic-508 /image-cards/topic-514` 时误删了整批 topic 目录（含 gen_fixed.py + prompts + 已生成图），只能靠 515 的目录 copy + 手写 prompt 恢复。**教训**：删目录前先 `ls` 确认范围，用 `find -maxdepth 1 -type d -name "topic-50[89]"` 更稳；恢复时用 `cp -r topic-515/* topic-508/` 后只覆盖 `prompts/*.md` + `article.md`
- **topic 目录缺失时的恢复路径**（实战验证）：① 从同批次相邻 topic copy 完整目录（含 gen_fixed.py） ② 手写 3 个 `prompts/{01,02,03}-cover.md`（按本次正文内容改写，保留统一水墨风格后缀）③ `python3 gen_fixed.py` 一次生成全部 3 图 ④ `lark-cli docs +create` 建新文档 + 串行 media-insert + 台账 append。全流程约 20 分钟，不算太慢
- **批量 10 题中有 2 题撞 fact_check 不丢人**：506/507/509/510/511/512/513/515 共 8 题一次过闸归档（通过率 80%）；508/514 因 fact_check 打回需人工介入，修正后一次重新生成。说明 pipeline 对常规题稳定，特殊事实细节仍靠人工兜底
- **流水号连续推进不受影响**：ledger max=515，508/514 虽有修复但序号照进，不影响后续扩展


### 10. 第六批（508/509/513/514/515 修复轮）新增教训

- **图片重复的根因 = 并行工具调用里跑了两遍 media-insert 循环**（508/514 各 6 图）：修复时同时发了两个 bash 调用，两边都执行了同一插图循环，全部 `ok:true` 无任何告警。**红线：media-insert 只允许一个串行执行点**——批量插图必须收在单条命令的 for 循环里，绝不允许并行工具调用各插一遍
- **插图后必须 fetch 验图数**：`lark-cli docs +fetch --doc <tid>` 返回的 content 含 `<img name="01-cover.png" ... src="file_token"/>`，正则计数应 =3 且 src 去重后仍 =3。**以后每次重建文档，插入完成后必跑这一步**（本次靠它定位 508/514=6 图、077=2 图）
- **台账同序号多 token 扫描法**：`awk -F'|' '{print $1}' .feishu_uploaded | sort | uniq -d` 列出所有重建过的序号（本次 33 个），逐个取**最后**一条 token fetch 验图。注意 435/436 的 token 带 ` #draft-saved` 后缀，解析要 `split()[0]`
- **跨文档搬图补缺失**（077 案例）：本地 topic 目录已删时，从旧版文档 fetch 拿 `<img src="file_token">` → `lark-cli docs +media-download --token <file_token> --output x.png`（**没有 `--doc` 参数，加了报 unknown flag**）→ `media-insert` 插入目标文档
- **重生成单图要同时验"风格"和"主体"**（509）：带 ref=同 topic 图三 + 风格锚点后画风达标，但两张**主体画反**（01 画成授印场景、02 画成上奏朝堂）。ref 场景元素会干扰主体。修复：对调两张文件名，让顺序匹配正文叙事（比再赌一轮重生成稳）
- **标题"我没想到…"句式被用户连续打回**（509/513 同款）：本批两篇标题都以"我没想到"开头，用户判不好。改写方向：**从正文提炼具体动作/对比**——`斩马谡贬自己：诸葛亮的赏罚组合拳`、`没打一场硬仗，诸葛亮白捡两郡`、`曹真病死，司马懿从没被雪藏`。规则：标题要具体、有反差、能一眼看出讲什么，忌空悬的惊叹句式
- **旧重复文档的处置**：旧 508/514 文档（6 图）已于 2026-09-30 经用户确认删除（`lark-cli drive +delete --file-token <tok> --type docx --yes --as user`）；台账最新行指向新文档。历史其他重建文档先不动

### 11. 流程加固（2026-09-30，把 499–515 的教训固化进代码）

以上教训不只记文档，已直接改 `xhs_graph`（改动均有红线测试守护，`uv run pytest tests/ -q` 8/8 过）：

| 教训来源 | 代码改动 | 位置 |
|---------|---------|------|
| 509/513 标题"我没想到"连遭打回 | ① 文风提示词改为"具体动作/对比/反差"并明令禁句式 ② 写正文硬性要求同步 ③ `verify_article` 新增硬校验：标题含「我没想到」直接打回重写 | `prompts/style.py` #文风、`nodes.py` write_article 要求3、`nodes.py` verify_article |
| 499/509 画风漂移（线描平涂） | `INKWASH_CLOSING` 追加正反双面风格锚点（ink-and-wash + No clean digital outlines…），LLM 输出与自动修补都会带上 | `nodes.py` INKWASH_CLOSING |
| 514 数字类 fact 打回重试无效 | fact issues 喂给重写时追加修法提示：**只用素材原文说法或删掉数字，严禁自造精确数字** | `nodes.py` write_article fact feedback |
| 508/514 双循环插图 6 图无告警 | `create_feishu` 插完必 `docs +fetch` 验图：数量=预期、src 去重；缺图自动补插 2 轮，验不过 raise；重复图直接 raise 要求删文档重建。`_insert` 收成唯一执行点并加红线注释 | `nodes.py` create_feishu |
| 509 目录里有 `*.bak.png` | 兜底 glob 从 `*.png` 收紧为 `0\d-cover\.png`，备份文件不会被误插 | `nodes.py` create_feishu |
| （潜伏 bug）`_strip_fences` 用到 `json` 却未 import | 补 `import json`（此前 LLM 输出 JSON 包裹时会 NameError） | `nodes.py` 头部 |

配套红线测试：`test_verify_rejects_cliche_title` / `test_verify_accepts_concrete_title` / `test_inkwash_closing_has_style_anchor`（`tests/test_redline.py`）。

### 12. 通用操作细节十条（2026-09-30 追加，对应 AGENTS.md 第 14–23 条）

1. **lark-cli 非交互 PATH**：`export PATH="$HOME/.npm-global/bin:/opt/homebrew/bin:$PATH"` 后再 `+create/+media-insert`；图内 `_tool_env()` 已内置双目录
2. **验图/搬图**：`docs +fetch --format json` → `data.document.content` 数 `<img name=`、src 去重=3；缺图 `docs +media-download --token <src>`（无 `--doc` 参数）→ 原位 insert
3. **台账读法**：`awk -F'|' '{print $1}' | sort | uniq -d` 列重建序号，取**最后一条** token 为最新；` #draft-saved` 后缀 `split()[0]`
4. **修订 commit 只含元数据**：png 被 gitignore 且 `add -f` 无效，图片版本靠飞书承载
5. **push 瞬态错误**：HTTP 500 / Connection reset → sleep 5 重试；`gh: command not found` 无害
6. **建文档 body = `tail -n +3 article.md`**（跳标题行+空行），标题单独传 `--title`；`document_id` 取不到即 raise，严禁占位符
7. **改流程先 `--dry-run`**：占位稿 + `DRYRUN-DOC` 走通全链路（verify/gen/create/闸门）再上真实题
8. **机器验结构、人审验视觉**：`verify_images` 只查 PNG 魔数/3:4/≥50KB，画风漂移和主体画反必须人在闸门里看文档
9. **两层重试分工**：节点内 6 轮只修空输出/字数（不耗 attempts）；围栏/英文/标题问题由 verify 打回走图路由 3 轮——排障先看谁在报错
10. **删飞书文档需用户点名确认**：`drive +delete --file-token <tok> --type docx --yes --as user`；删前核对是旧重复版（非台账最新行），历史文档不动
