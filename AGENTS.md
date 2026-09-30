# AGENTS.md — 003-Twitter

Social media content farm: XHS image-card articles (西汉风云 history/literature) for @DubaIGOHGOkTHOk.

## Hard rules

- **Never execute Twitter/X post commands** — prepare text, user sends manually
- `.png`/`.jpg`/`.jpeg` gitignored — never commit images
- **🚨 审核→存草稿流程（强制）**: 每次完成场景制作后，必须先**新建飞书文档**保存内容，**仅停留在飞书文档阶段**。待用户审核确认无误并明确说"存草稿"或"OK"后，**再执行**`opencli xiaohongshu publish --draft true`存小红书草稿。**严禁**在完成飞书文档后自动存草稿，必须等用户明确指示才可执行。**场景/游记通用此流程**。
- **每次写一个**：当前场景全部完成后，停止并等待用户审核指令。不要再自动推进到下一个场景。
- **langgraph 状态机与本 SOP 双轨**：结构化流水线在 `langgraph/`（见其 README），**默认演练模式**，`--real` 才真实执行；上条审核红线已由图的 `human_review` interrupt + `route_review` 边**强制**（未经 approve 不可达 publish 节点，`tests/test_redline.py` 守护）。图跑不通时回退下方手动 SOP，人工执行时红线原样生效。
- **每次修改（正文/配图）后必须新建飞书文档保存**，不能更新已有文档
- **飞书审核→确认无误→才存草稿**：先 `creator-profile` 验证 session，再 `publish --draft true`
- XHS 标题≤20 CJK字（含标点），正文≤950字纯文本，tags 用 `#话题` 附在正文末尾
- **`article.md` 第1行必须是独立标题行（≤20字），此即 XHS 标题**。若第1行是正文首句，`publish --title "$(head -1 article.md)"` 会报 "Title is NNN chars — must be ≤ 20"。177 曾因此失败，写入后即成功
- **写article.md前必须先确认标题≤20字**，避免-publish时失败重做
- **飞书文档ID必须立即记录**：`lark-cli docs +create`成功后立即提取document_id并写入.feishu_uploaded，**严禁使用占位符`_doc_id_`**
- **gen_one.py必须从上一成功案例copy**：每次新建文件夹后立即执行`cp image-cards/<上一个>/gen_one.py image-cards/<当前>/gen_one.py`，**gen_fixed.py（主用）与 gen_no_ref.py 同样要 copy**
- **插入图片前必须确认工作目录**：先`pwd`确认在正确文件夹，再用相对路径`./01-cover.png`
- All Python scripts with Chinese text need `# -*- coding: utf-8 -*-` (system Python 3.9)

## Setup

```bash
export PATH="/opt/homebrew/bin:$PATH"
set -a; source ~/.baoyu-skills/.env; set +a
```

- Agnes API: `apihub.agnes-ai.com` (NOT `api.agnesai.com`)
- 3 keys: `AGNES_API_KEY`, `AGNES_API_KEY2`, `AGNES_API_KEY3`
- lark-cli at `/opt/homebrew/bin/lark-cli`; auth: `cli_aadef45343f91cc3` on `qcnh2b60jsx1.feishu.cn` (user 何健)
- Feishu re-login: `lark-cli auth login --no-wait --json --domain all` → device code → `lark-cli auth login --device-code <code>`
- **飞书文档存放文件夹**：
  - `两汉风云`（folder_token: `JUBNfa8TyldTHsd9pzNcOTbynWf`，https://qcnh2b60jsx1.feishu.cn/drive/folder/JUBNfa8TyldTHsd9pzNcOTbynWf）— 场景文档
  - `游记`（folder_token: `L8MKfqrG6lNMJkdf79ZcrB8inJg`，https://qcnh2b60jsx1.feishu.cn/drive/folder/L8MKfqrG6lNMJkdf79ZcrB8inJg）— 游记文档
  - `科技`（folder_token: `LFpJf4lSRlMUKpdPi9fcWIjhnNZ`，https://qcnh2b60jsx1.feishu.cn/drive/folder/LFpJf4lSRlMUKpdPi9fcWIjhnNZ）— 科技类文档（2026-09-29 新建，科技帖 `--parent-token` 用此）

## Folder layout

- `image-cards/<topic>/` — 历史类 CURRENT pipeline（`topic-<N>` 目录）。Only create new topics here.
- `image-cards/<英文slug>/` — **科技类**目录（如 `ios27-official-release/`），**不建** `topic-<N>`，不占历史序号体系
- `*-xhs/` (~28 dirs, legacy remnant) — LEGACY SVG+Inkscape pipeline, do not touch
- `_gen_runner.py` / `batch_gen.py` — LEGACY, do not use（已不在仓库中）

## 世说新语 series

- Feishu drive folder「世说新语」 at root: `W729fRxeAlXePBdj1fMcWjoCnMb` (https://qcnh2b60jsx1.feishu.cn/drive/folder/W729fRxeAlXePBdj1fMcWjoCnMb)
- **All 世说新语 docs MUST be created inside this folder** (create doc with `--parent-token W729fRxeAlXePBdj1fMcWjoCnMb`, or `drive +move` afterwards — `docs +create` 只认 `--parent-token`)
- Local topic folders under `image-cards/shixi-xinyu/<topic>/`; Feishu title prefix = `世说N：{标题}`
- Sample content: 周处除三害（自新门，西晋）

## 游记系列

- Feishu drive folder「游记」 at root: `L8MKfqrG6lNMJkdf79ZcrB8inJg` (https://qcnh2b60jsx1.feishu.cn/drive/folder/L8MKfqrG6lNMJkdf79ZcrB8inJg)
- **All 游记 docs MUST be created inside this folder** (create doc with `--parent-token L8MKfqrG6lNMJkdf79ZcrB8inJg`, or `drive +move` afterwards)
- Local topic folders at repo root: `wohuling/`（卧虎岭，已用）、`youji/`（桃岔河，已用）; future topics: `<destination>/`
- XHS title prefix = `场景N：{标题}` or 直接标题（如「秦岭深处的阿勒泰」）
- 游记文章风格：**干货攻略型**，含导航地址、路线、用时、装备、最佳季节、轨迹链接
- 游记配图：用户自拍真实照片，无需AI生成；顺序：远景封面→核心景观→细节特写→收尾
- 游记含两步路轨迹链接：`https://www.2bulu.com/track/track_detail.htm?trackId={id}`（用户给了 trackId 才加）
- **XHS 单草稿最多 9 张图**（opencli 硬限制）：照片多时按「入口→上升→核心景观→高潮→收尾」叙事线精选
- 完整操作手册：`/Users/mac/ai_doc/macmin_游记类小红书创作与发布指南.md`（2026-09-29 成文，含排障表与 AGENTS 对照）

### 游记 workflow

1. 用户提供照片 + 目的地信息（海拔/难度/交通等）
2. 上网查证目的地资料（百度百科/抖音/8264等），确保信息准确
3. 写 `article.md` — 干货攻略风，**~650-800字**（计数含标题行与 tags），含阴阳割昏晓等文学引用（如适用）
4. 创建飞书文档（`--parent-token L8MKfqrG6lNMJkdf79ZcrB8inJg`）+ 逐张插入图片
5. 用户审核 → 说"存草稿" → `opencli xiaohongshu publish --draft true`

### 游记 gotchas

- `lark-cli drive +move --file-token <token> --type docx --folder-token <folder>` — **type参数是 `--type` 不是 `--file-type`**（2026-08-15 实测）
- `lark-cli drive +search --doc-types folder` 可搜索文件夹
- 游记文档创建时用 `--parent-token` 而非 `--folder-token`（与场景文档一致）
- **`lark-cli docs +media-insert` 必须用相对路径**：`--file ./x.jpg`；绝对路径报 `unsafe file path` 且不插入。第一轮就要 cd 到照片目录用相对路径（2026-09-05 实测）
- **插图成败以 `docs +fetch` 数 img 标签为准，勿凭自编 JSON 管道判定**：管道报错 ≠ 插入失败——桃岔河曾因管道报错误判"全失败"而重插，致 26 图翻倍；用 `+fetch --detail with-ids` 取 block id 后 `+update --command block_delete` 可删重复 block（2026-09-29 实操清 13 个）
- **lark-cli stderr 进度会干扰 JSON 解析**：命令先向 stderr 打 `Inserting/Block created`，直接 pipe 到 `json.load` 报错——先看原始输出或 `grep '^{'` 过滤（2026-09-05 实测）
- **路径方向双轨制**：飞书插图 `--file` 要**相对**路径；opencli `--images` 要**绝对**路径——记反必报错（2026-09-05 实测）
- **游记在 `.feishu_uploaded` 用 9001+ 独立编号段**（`9001|wohuling|…`、`9002|youji-taochahe|…`），勿复用场景号段防同号冲突（2026-09-29 实测，编号段规则待固化）
- **未提交的记录会被并行会话清掉**（2026-09-29 实测：本文件游记 gotchas、MEMORY.md、youji/article.md、.feishu_uploaded 追加行均被清除后重建）——关键记录写完尽快 `git commit`

## Article pipeline

### Writing style — must be engaging

Write like you're telling a friend a fascinating story. 情感真挚, avoid textbook tone. Use vivid details, concrete scenes, and narrative tension. The title should spark curiosity — a question, a contrast, or an unexpected angle. Aim for readers to think "I didn't know that" and want to share.

**科技类帖不适用上段**：用清单体——1️⃣2️⃣编号小标题+emoji+每条利益点短句+口语化点评+结尾互动问题（"你会升吗？评论区聊聊"），标题=关键词+痛点/数字/悬念，能短则短（详见「科技类帖速览」与《科技类指南》3.2）。

### Historical accuracy — must verify

Cite specific events, names, numbers, and years. **Verify any lesser-known claim** before writing — check against structured references (史记/后汉书/资治通鉴/三国志) and web sources. (本仓库未包含 `book/两汉风云.epub`，如需电子书请单独获取。) Don't invent or approximate. If unsure, omit rather than guess.

**Primary source hierarchy for verification** (must use when writing 东汉题材):
1. `后汉书` (范晔) — first stop for Eastern Han facts
2. `资治通鉴` (司马光) — most comprehensive narrative, cross-reference with 后汉书
3. `世说新语` — for biographical anecdotes (use with caution, not all are factual)
4. `东观汉记` (佚文) — when available, earliest Eastern Han source
5. 网路检索验证关键细节（人名/地名/年份/谥号/卒年等）

**Three Kingdoms (三国) topics**: verify against `三国志` (陈寿) first, cross-reference `资治通鉴`, use `后汉书` for late-Han events/careers (董卓/曹操/刘备 up to 曹丕篡汉). 演义 (《三国演义》) fictional scenes (锦囊、火烧博望坡、走马荐诸葛等) must be distinguished from 正史 — label as 演义加工.

**Common pitfalls from recent sessions (175–185)**:
- 181/183 岑彭、来歙之死：均被**公孙述刺客**所杀（资治通鉴卷42明确），原稿误作"隗嚣刺客"。来歙死在攻蜀前线（河池/下辨），不在陇右
- 181 浮桥：是**征蜀时荆门浮桥**（岑彭派鲁奇焚桥），非渭河浮桥
- 181 岑彭"年仅五十八"：后汉书未载，**删去**
- 181 "连克夷陵、江州"：江州田戎据守未下，**改为"长驱入江关"**
- 181 "关中饥荒班师"无据：刘秀班师主因是颍川变乱+军中乏粮
- 181 "天下豪杰归我"虚构台词：改为间接叙述
- 183 "揽衣痛哭"：通鉴原文是"省书揽涕"（擦泪）
- 183 刘秀"下令严查降兵""此后再无刺杀"：查无实据，**删去**，改写史实收尾
- 178 吴汉"退休送行"：吴汉实为病逝于征蜀后，**删去**
- 178 贾复"刘秀探病落泪"：无据，**删去**
- 178 "早一百多年杯酒释兵权"：应是"早九百多年"
- 185 岑彭"麦城破秦丰"：岑彭主要战场在荆楚（江关/武阳/彭亡），**删"麦城"**
- 185 "功多者人忌"引文归属：是**刘秀说的**，非韩信原话，引文需标注"刘秀评价"
- 184 标题超20字：「同样打蜀地：一个稳得吓人，一个冒进差点赔光」→ 21字，需删"地"字改为「同样打蜀：一个稳得吓人，一个差点输光」
- 187 冯异卒年46岁（后汉书明确），非48岁；"刘秀封冯异为大将军"玩笑无据，已删

**Rule**: 写任何正文前，先用 webfetch/grep 查证核心史实点（人名、时间、地点、事件），有疑处宁可删掉不写

### New topic workflow

> 📌 **详细版 SOP 见下方「完整作业流程（场景创作 SOP）」**，此处仅保留速览。

1. Write `article.md` — **5±2 paragraphs, 2–5 sentences each, ~800 chars total**. No 古文 quotes unless asked. 标题独立第1行 ≤20字，全中文无英文。
2. Write **3 English prompts** `prompts/01-cover.md` … `03-*.md` (was 6, changed from topic 150 onward) — 风格前缀以「水墨配图标准风格」定稿公式为准
3. Generate 3 images via **`gen_fixed.py`**（单模型，勿混跑 gen_one.py）
4. Upload to Feishu (see below) → user reviews images+正文 together at 飞书阶段 → XHS draft（近期 443–453 实际流程，无独立翻译审批步）

### 科技类帖速览（Tech，2026-09-29 新增；完整规范见 `/Users/mac/ai_doc/macmin_科技类小红书创作与发布指南.md`）

1. **选题**：无素材库，`websearch` 检索当日热点；查重只看已有成文（`grep`）+ 草稿箱，**不走** `正文提示词.md`
2. **正文**：清单体（1️⃣2️⃣编号+emoji+利益点短句+结尾互动问题），非讲故事；同硬性要求：标题≤20字全中文、全文750–900、零英文（`iOS`→「苹果新系统」、`Siri`→「语音助手」）；**例外——专有名词保留**：主角是英文名的产品（如 LangGraph/LangChain/Uber）正文可保留专有名词，**开写前先问用户**，标题仍全中文（5002 用户拍板）
3. **提示词**：扁平科技插画风 + **封面英文大字**（`Xiaohongshu social media cover, 3:4 vertical, clean flat tech illustration style` + `huge bold English headline text "XXX"`）——**中文大字必乱码，禁止中文大字**；逐张生成后 `read` 验字，不走 gen_fixed.py 盲出；大字拼写错两次就**换更短不易拼错的词**（PLUGINS→MODULAR），**别把逐字母拼写提示写进 prompt**（`M-O-D-U-L-A-R` 会被字面渲染出来）
4. **事实核查**：每条数据 websearch 查证，性能数据带「最高」口径，条件限定（首批语言/机型/地区）不能丢
5. **飞书**：`--parent-token LFpJf4lSRlMUKpdPi9fcWIjhnNZ`（**科技夹**，非两汉风云）
6. **序号**：科技帖独立段 **5001+**（5001 deepseek、5002 langgraph…），勿复用历史段号——393 曾与历史场景393 同号冲突；`.feishu_uploaded` 仍追加记录
7. **出图**：3 个 key 可 3 图**并行**（每图独立 key，约 1 分钟，用户已给 3 key 时用之），每张仍必须 `read` 验字；验字发现**内容与提示词完全对不上**（串图）→ 怀疑 API 返回错 URL，直连诊断（打印 `data[0].url` 另存对比），**不要盲目改 prompt 重试**（5002 实测连续 4 次串图，换词换 key 均无效，直连一次成功）；下载中断会产生 256KB 整数截断文件，生成后顺手查大小

### Article char count — critical

Target: **~800 chars** (after stripping spaces/newlines), approx 750–900 acceptable. No 古文 quotes unless asked. Do NOT waste time fine-tuning to an exact number — 800左右 is fine. No 后世影响/现代启示 sections.

```python
# Verify:
len(article.replace('\n','').replace(' ',''))
```

If <700 chars, expand the main narrative with more vivid scenes and details — **do NOT** add 后世影响/现代启示 sections (phased out).

### Historical enrichment (legacy — scripts no longer in repo)

Topics **1–100** were previously enriched and uploaded to Feishu (old 后世影响+现代启示 style). New topics from 144 onward must NOT use that structure. The `enrich_v2.py` / `enrich_v3_batch*.py` scripts have been removed; do not reference them.

### Feishu title format

`场景{num}：{title}` — e.g. `场景56：武帝双标——卜式与相如追星`

### Feishu upload

```bash
export PATH="/opt/homebrew/bin:$PATH"
# Create doc (passing content via stdin) — always use --parent-token:
# ⚠️ 按类型分流：历史/场景 → 两汉风云 JUBNfa8TyldTHsd9pzNcOTbynWf；科技 → 科技夹 LFpJf4lSRlMUKpdPi9fcWIjhnNZ（游记/世说见对应节）
echo "$article_text" | lark-cli docs +create --title "场景N：标题" --content - --doc-format markdown --as user --format json --parent-token JUBNfa8TyldTHsd9pzNcOTbynWf

# Insert images sequentially (parallel → 429):
lark-cli docs +media-insert --doc <token> --file ./01-cover.png --as user
lark-cli docs +media-insert --doc <token> --file ./02-cover.png --as user
lark-cli docs +media-insert --doc <token> --file ./03-cover.png --as user
# ... 3 total, sleep 3s between each
```

**Tracking**: `.feishu_uploaded` records `NNN|folder-name|doc-token` — always append, never deduplicate.

## Image generation (`gen_fixed.py` 主用；`gen_one.py` 为 legacy/备用)

> ⚠️ **当前主用 `gen_fixed.py`**（单模型 `agnes-image-2.1-flash` 三线程，见 SOP 第 3 步）——本节描述的是 `gen_one.py`（带参考图 + 2.1→2.0 降级）的 legacy 行为，仅在备用时参考；**禁止**用 gen_one/gen_no_ref 与 gen_fixed 混跑同一主题。

- Model: `agnes-image-2.1-flash` (falls back to `agnes-image-2.0-flash`)
- 3 parallel threads using `AGNES_API_KEY{i % 3}`
- Cover (`python3 gen_one.py 1`) has no reference image
- Subsequent images (`python3 gen_one.py 2 3`, `4 5`, `6`) use `01-cover.png` as ref
- 20 max retries per image; 503 / 000 empty responses are normal
- Prompt file: `prompts/{num:02d}-cover.md`; output: `{num:02d}-cover.png`
- Cover filename **must** be `01-cover.png` (ref step reads this exact name)

### Content policy — critical

- English prompt = **neutral scene description only**. Chinese subtitle carries meaning.
- NEVER: `corpse`/`blood`/`collapse`/`torture`/`starving`/`cannibalism`/`abyss`/`suffocating`/`harem`/`reclining`/`dark plot`/`scheming`
- Chinese prompts also trigger. Check for exact string `content_policy_violation` (not `content_policy`)
- Policy-violated prompts: rewrite immediately, don't retry
- 181-01 `辎重`/`浮桥` in Chinese prompt triggered policy — remove military logistics words even if seemingly neutral. Batch gen: only failed image need re-gen, others already saved

### Regeneration

User says "图X重画" → regenerate that image with ref → rebuild ENTIRE Feishu doc.
User says "不要第X张" → omit from `--images` list.

## XHS publish (draft only)

```bash
# 1. Probe session
opencli xiaohongshu creator-profile --site-session persistent --keep-tab true
# 2. Publish
export OPENCLI_BROWSER_COMMAND_TIMEOUT=180000
opencli xiaohongshu publish "$(cat article.md)" --title "$(head -1 article.md)" --images "/abs/path/01-cover.png,..." --window foreground --site-session persistent --draft true --format yaml
```

- Always `creator-profile` before `publish` (avoids 60s timeout)
- `--keep-tab true` prevents re-navigation
- **Prefer absolute paths** for `--images` (relative fails when workdir differs)
- Max 9 images per draft; `--draft true` accumulates drafts

## Performance notes

- 3-key parallel gen: ~30–60s per image (503 can double). Plan ~2 min/image
- Batch gen: Sweet spot is 2–3 per call. Never ≥4 (timeout risk). Never 1 (overhead)
- Feishu inserts: ~15s each, 6 sequential = 2 min min. Timeout 180s
- Each topic (article+prompts → pre-review → 3 images → Feishu → review → draft): ~8–12 min

## References

- `MEMORY.md.backup` — legacy gotcha collection（原 `MEMORY.md` 已改名，仓库内无独立 `MEMORY.md`）
- `正文提示词.md` — master document with topics 正文 + image prompts
- `.feishu_uploaded` — 统一飞书上传追踪：`NNN|folder-name|doc-token`（已合并原子目录分散记录）

## Style Preferences

- **同步约定（2026-09-29）**：本节及下方「水墨配图标准风格」「人物服饰规范」是**文字规范正本**；`langgraph/xhs_graph/prompts/style.py` 是其编译产物（创作节点只读 prompts/，不回读本文件）。**修改本节 → 必须同步 style.py**，防止双份漂移。

- 两汉内容（场景1-214）：写实历史画风格，精细描绘人物表情服饰，光线戏剧性，历史厚重感
- 三国内容（场景215起）：写实历史画风格，精细描绘人物表情服饰，光线戏剧性，历史厚重感

### 水墨配图标准风格（2026-09-28 确认，用户指定以霍去病篇为准，443–445、447、448、452 用户审核均通过，452 复核「这会儿风格很好」——此为**最终定稿公式**，不再改动）

- **用户不喜欢 `delicate pale colors peeking through` 淡彩版前缀**（442 审核反馈），要求参考 `image-cards/huoqubing*` 的风格
- **标准风格前缀（443–445 验证通过的最终版）**：
  ```
  Ink wash painting style, light rice paper texture, flowing ink strokes, subtle crimson and grey colors, sparse composition with negative space, misty atmosphere.
  ```
- **场景段写法（关键经验）**：风格段之后直接写生动场景 + 果断主色（如 `crimson battle robe`、`crimson sashes`），**不要**加 `strictly limited`、`faint`、`overcast`、`small in the lower third` 之类过度约束词——会把画面框死变平（442 教训）
- **光线统一**：三条 prompt 都用 `soft diffused daylight`（或夜景用 `soft light from paper window`），光线不统一会像三种画风
- **收尾约束**：
  ```
  Ancient Chinese people, period clothing. No heavy outlines. Ample whitespace. Unified series style, consistent brushwork and tone.
  ```
- **构图要求**：大留白，`wide empty sky above`，雾中远山 `fading into mist`
- **生成方式**：必须用 `gen_fixed.py`（单模型 `agnes-image-2.1-flash` 三线程并行，只换 key 不换模型）。**不要用 gen_one.py/gen_no_ref.py 混跑**——403 时切 2.0 模型会导致三张图风格漂移
- 霍去病原版 prompt 含中文书法标题（`Chinese title "..." in calligraphic brush style`）——**用户另有"图内无文字"要求，除非用户明确要标题，否则不加**
- **仅适用于历史/三国类**：新历史场景一律用此风格。**科技类不适用**——用扁平科技插画+玻璃拟态、封面必须英文大字（见「科技类帖速览」与《科技类指南》5.1）

### 历史画人物服饰规范（2026-08-17 新增）

- **所有汉代场景**人物必须穿汉代服饰（深衣/曲裾/直裾/宽袖长袍），禁止现代或错误朝代服装（西装、和服、明清服饰等）
- **年龄感准确**：如曹操假中风时约18-20岁青年，非孩童；段颎被毒死时须发花白老者
- **器物符合时代**：杯子用青铜卮/爵，不用玻璃杯；桌案用几榻，不用现代桌椅
- **背景建筑**：汉代庭院有柱廊、瓦当、夯土墙，避免唐宋及以后的建筑风格
- **「白衣」类词义防误画**：如「白衣渡江」= 换**平民商贾常服**伪装（素色交领民服、货担斗笠），**不是披麻戴孝**——prompt 写 plain commoner/merchant robes、carrying goods，禁 mourning clothes、white funeral headbands、垂髫丧巾意象（2026-09-29 场景453 图三教训，用户指出"白衣是普通人样貌非传白戴孝"）
- **Prompt中必须明确标注"汉代""深衣""宽袖长袍"** 等关键词确保AI不画错
- 图二、图三必须与图一有明显场景差异（不同地点/人物/活动），避免三张图雷同

### 完整作业流程（场景创作 SOP，2026-09-22 更新）

> ✅ **新工作流（2026-09-29）**：结构化执行走 `langgraph/`——`cd langgraph && uv run cli.py run --series history [--topic N]`，图会自动完成下方 0~6 步并在飞书文档后**停下等审核**（`--resume approve|rewrite|redraw|archive` 续跑），详见 `langgraph/README.md`。
> **langgraph 排障六条（2026-09-30 批量 470–495 实战，详本见 README「经验教训」节）**：
> 1. 飞书正文尾部多出代码块（字数统计元信息）→ 已修：`_strip_fences` 删全文任意位置围栏 + `verify_article` 硬检查打回；**清洗和验证两层都要管结构问题**
> 2. 重跑报"验证/生图重试超限"但 verify 明明 passed → 旧 thread checkpoint 残留 attempts 计数；CLI 已自动换新线程，**归档时若打印过"改用新线程"必须 `--thread <线程>-2`**
> 3. 重跑前先删残留 `image-cards/topic-N/`（否则 dedup 直接 skip）——**删前必查 `.feishu_uploaded` 和 git，已入台账的绝不能删**
> 4. fact_check 报错先看 report_error 里的 issues：模型偶发误判，同稿重跑即过，别急着改稿
> 5. **每条打回路由的原因都要进重试输入**（486：fact issues 未喂给重写 → 盲改二次失败，已修）；节点内重试耗尽 raise 会"静默崩图"（487），已改自动修补前缀+重试 4 轮——排障用 `graph.get_state(thread)` 看 `tasks[].error`
> 6. 归档线程号**照抄运行时打印的"改用新线程 XXX"**，换线程会累积（-2、-3…），别想当然
> **下方第 0~6 步保留为手动兜底/排障路径**：图跑不通、或需人工单步操作时按此执行；人工执行时 Hard rules 红线原样生效。
> 本流程适用于两汉风云/三国/后续所有 `image-cards/<topic>/` 场景创作。
> **必须严格按顺序执行，不得跳步。** 每步完成后自查，全部通过才进入下一步。

---

#### 第 0 步：查重 + 读取原始素材与确认序号

0. **先查重**（见下方「查重规则」节）：主题 N 若与近期主题/已有成文/草稿重复 → 直接跳过该号（序号照进不回填），N+1 继续，直到找到不重复的主题。
1. 打开 `正文提示词.md`，找到目标场景编号 N（如 431），读取：
   - 原始标题
   - 原始正文
   - 原始 3 条英文提示词
2. 确认当前最大已完成序号：**取 `.feishu_uploaded` 中行首数字的最大值**，N = 最大值 + 1。
   > ⚠️ **不能取最后一行**——该文件已混入其他系列条目（如 `393|ios27-official-release|…`，与历史场景 393 同号且追加在末尾），最后一行 ≠ 最大序号。示例：`awk -F'|' '$2 ~ /^topic-/ {if ($1+0>m) m=$1} END {print m}' .feishu_uploaded`
3. 在 `image-cards/` 下新建文件夹 `topic-<N>/`（若已有同名 topic 目录则复用）。
4. **立即 copy 生成脚本（gen_fixed.py 主用）**：
   ```bash
   cp image-cards/<上一个成功的>/gen_fixed.py image-cards/topic-<N>/
   cp image-cards/<上一个成功的>/gen_one.py image-cards/topic-<N>/
   cp image-cards/<上一个成功的>/gen_no_ref.py image-cards/topic-<N>/
   ```
   > 🚨 这一步不能忘，忘了会导致后续无法生成图片。

---

#### 第 1 步：写正文（article.md）

**格式硬性要求：**

| 项 | 要求 | 违反后果 |
|----|------|---------|
| 第 1 行 | 必须是独立标题行，≤20 个 CJK 字（含标点） | `publish --title` 报错 "Title is NNN chars" |
| 第 2 行 | 空行 | — |
| 第 3 行起 | 正文 | — |
| 正文字数 | 去掉空格换行后 750–900 字（目标 ~800） | <700 需扩写；>950 超出 XHS 限制 |
| 语言 | **全中文，绝不能有英文单词** | 用户标记为"极为严重的问题" |
| tags | `#话题` 格式附在正文末尾 | — |
| 古文引用 | 默认不加，除非用户要求 | — |
| 章节 | 无后世影响/现代启示（已废除） | — |

**写作流程：**

1. 先通读 `正文提示词.md` 中该场景的原始正文，理解核心事件。
2. 按"给朋友讲故事"的口吻重写：有细节、有场景、有情绪，避免教科书腔。
3. 写完后**逐字检查英文单词**：
   ```bash
   # 快速扫描正文中是否混入英文（标题行不含英文）
   tail -n +3 image-cards/topic-<N>/article.md | grep -nE '[a-zA-Z]{2,}'
   ```
   若有匹配行，必须改写为中文。特别注意人名/地名音译是否写成了英文。
4. 验证字数：
   ```bash
   python3 -c "print(len(open('image-cards/topic-<N>/article.md').read().replace('\n','').replace(' ','')))"
   ```
   注意：此数包含标题行，实际正文 ≈ 此数 - 标题字数。750–900 区间即可，不必精确抠数。
5. **验证标题字数 ≤20**：
   ```bash
   head -1 image-cards/topic-<N>/article.md | python3 -c "import sys; print(len(sys.stdin.read().strip()))"
   ```
6. 史实核查：人名、年份、地点、事件，不确定就删掉不写，或 webfetch 检索验证。

**article.md 模板：**
```
标题（≤20字，独立成行）

正文第一段……

正文第二段……

#话题 #话题2 #话题3
```

---

#### 第 2 步：写 3 条英文提示词（prompts/）

> ⚠️ 下列要素为**历史类**专用（朝代/服饰/故事性）。**科技类**要素不同：扁平插画前缀+英文大字+三图对应功能点，见「科技类帖速览」。

**目录结构：**
```
image-cards/topic-<N>/
├── article.md
├── gen_fixed.py（主用）/ gen_one.py / gen_no_ref.py
└── prompts/
    ├── 01-cover.md    ← 封面，无参考图
    ├── 02-cover.md    ← 用 01-cover.png 做参考图
    └── 03-cover.md    ← 用 01-cover.png 做参考图
```

**每条 prompt 必须包含的要素（缺一不可）：**

1. **风格前缀**（3 条完全一致，保证画面统一；⚠️ 以 Style Preferences「水墨配图标准风格」最终定稿公式为准，勿用旧淡彩版）：
   ```
   Ink wash painting style, light rice paper texture, flowing ink strokes, subtle crimson and grey colors, sparse composition with negative space, misty atmosphere.
   ```
2. **时代标注**：`late Eastern Han dynasty` / `Eastern Han dynasty` / `Three Kingdoms period`（按场景朝代）
3. **具体服饰**：写明 garment 类型，如 `dark robes with wide sleeves`、`iron lamellar armor`、`leather lamellar armor`
4. **人物形象**：
   - 武将 → `armor`、`military commander`（防画成文官）
   - 老年 → `white-haired`、`elderly`
   - 道士 → `Daoist priest` + `white beard`（禁止光头、禁止加道冠除非用户要求）
   - 面孔 → `handsome, elegant, slender, refined`（用户多次反馈拒绝"矮胖子"）
5. **动作/表情**：`staring intensely into eyes`、`leading troops through gates` 等，不能只写静态肖像
6. **环境细节**：`by lamplight`、`at night`、`torchlit scene`、`palace corridor`、`river` 等，让人看出"正在发生什么事"
7. **故事性**：每张图要对应正文中的某个具体情节，三张图场景明显不同（不同地点/人物/活动）

**绝对不能出现的词（content policy 高危）：**
`corpse`、`blood`、`collapse`、`torture`、`starving`、`cannibalism`、`abyss`、`suffocating`、`harem`、`reclining`、`dark plot`、`scheming`、以及中文 `辎重`、`浮桥` 等军事后勤词。
→ 一旦 API 返回 `content_policy_violation`，**立即重写 prompt，不要重试**。

**三图分工建议（避免雷同）：**

| 图 | 文件名 | 作用 | 参考图 |
|----|--------|------|--------|
| 图1 | `01-cover.png` | 封面/主视觉，最能概括全文 | 无 |
| 图2 | `02-cover.png` | 正文另一关键情节 | `01-cover.png` |
| 图3 | `03-cover.png` | 正文第三个关键情节/收尾意象 | `01-cover.png` |

---

#### 第 3 步：生成图片

**方式 A：gen_fixed.py（✅ 当前唯一推荐，三图并行，单模型防风格漂移）**
```bash
cd image-cards/topic-<N>
python3 gen_fixed.py            # 三线程并行，一键生成 01/02/03
```
- **固定单模型 `agnes-image-2.1-flash`，只轮换 3 个 key 不换模型**（gen_one.py 的 2.1→2.0 降级会导致三张图风格漂移，禁止混跑）
- 单图约 30–60s，503 正常会自动重试（最多 20 次）
- 输出：`01-cover.png` / `02-cover.png` / `03-cover.png`

**方式 B：curl 单图（单张重画时用）**
```bash
curl -s --max-time 120 -H "Content-Type: application/json" \
  -H "Authorization: Bearer <key>" \
  -d '{"model":"agnes-image-2.1-flash","prompt":"<prompt内容>","n":1,"size":"720x960"}' \
  "https://apihub.agnes-ai.com/v1/images/generations" \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['data'][0]['url'])" \
  | xargs -I {} curl -s -o 03-cover.png {}
```

**生成后自查（必须逐张打开看）：**

- [ ] 是水墨微彩风格，不是写实照片/油画？
- [ ] 画面里**没有文字/书法**？（用户明确要求图内不能有字）
- [ ] 人物穿的是**正确朝代**服饰（东汉末年 → 深衣/曲裾/铁札甲，不是西装/和服/明清官服）？
- [ ] 人物**有头发**（不是光头）、身材修长优雅（不是矮胖）？
- [ ] 武将穿铠甲、道士有道袍白须、老人白发？
- [ ] 画面有**环境和故事感**（不是纯人物肖像）？
- [ ] 三张图风格统一（水墨风格、色调、笔触一致）？
- [ ] 三张图场景各不相同？
- [ ] 图的内容**能对应到正文的某个情节**？
- [ ] 没有触发 content policy？

任何一项不过 → **改 prompt 重画该张**，不要带着问题往下走。

---

#### 第 4 步：创建飞书文档并插图

**硬性规则：每次修改（正文或配图）都必须新建文档，绝不能更新已有文档。**

```bash
export PATH="/opt/homebrew/bin:$PATH"
cd image-cards/topic-<N>

# 1. 创建文档（跳过 article.md 的第1行标题，因为标题单独传给 --title）
article=$(tail -n +3 article.md)
echo "$article" | lark-cli docs +create \
  --title "场景<N>：<标题>" \
  --content - --doc-format markdown --as user --format json \
  --parent-token JUBNfa8TyldTHsd9pzNcOTbynWf
# ↑ 历史类用两汉风云夹；科技帖改用 LFpJf4lSRlMUKpdPi9fcWIjhnNZ（科技夹），见「科技类帖速览」
# ↑ 立即从 JSON 输出中提取 document_id
```

```bash
# 2. 逐张插入图片（必须串行，间隔 3 秒，否则 429）
lark-cli docs +media-insert --doc <document_id> --file ./01-cover.png --as user
sleep 3
lark-cli docs +media-insert --doc <document_id> --file ./02-cover.png --as user
sleep 3
lark-cli docs +media-insert --doc <document_id> --file ./03-cover.png --as user
```

**插入前必须 `pwd` 确认在正确文件夹**，用相对路径 `./01-cover.png`。

```bash
# 3. 立即记录 document_id 到 .feishu_uploaded（严禁占位符）
echo "<N>|topic-<N>|<document_id>" >> .feishu_uploaded
```

**输出飞书链接给用户审核**——链接**单独成行，后面不加括号注释**（❌`https://…（科技夹）`，2026-09-29 用户指令），然后**停下来等待**。

---

#### 第 5 步：用户审核 → 存草稿

> 🚨 **绝对红线**：完成飞书文档后，**严禁自动存草稿**。必须等用户明确说"存草稿"或"OK"。

用户审核可能提出的问题及处理：

| 用户反馈 | 处理动作 |
|---------|---------|
| "图X重画" / "图X不行" | 改 prompt → 重生成该图 → **新建整个飞书文档**（含全部图）→ 重新走第4步 |
| "不要第X张" | 存草稿时 `--images` 列表里去掉该图 |
| "正文改成……" | 改 article.md → **新建飞书文档** → 重新走第4步 |
| 确认无误 | 进入存草稿 |

**存草稿命令（两步，缺一不可）：**

```bash
export PATH="/opt/homebrew/bin:$PATH"
# 1. 先探测 session（避免 publish 60s 超时）
opencli xiaohongshu creator-profile --site-session persistent --keep-tab true

# 2. 存草稿（注意：绝对路径！）
export OPENCLI_BROWSER_COMMAND_TIMEOUT=180000
opencli xiaohongshu publish "$(cat image-cards/topic-<N>/article.md)" \
  --title "$(head -1 image-cards/topic-<N>/article.md)" \
  --images "/abs/path/01-cover.png,/abs/path/02-cover.png,/abs/path/03-cover.png" \
  --window foreground --site-session persistent --draft true --format yaml
```

- `--images` **必须用绝对路径**，相对路径在 workdir 不同时会失败
- 最多 9 张图/草稿；`--draft true` 会累积多个草稿
- 存草稿成功后，**停止，等用户指示写下一场景**（"每次写一个"）

---

#### 第 6 步：进入下一场景

用户说"写下篇" → 回到第 0 步，序号 +1，重复全流程。

---

#### 查重规则（2026-09-28 用户指令：「重复的直接跳过」，447 起强制执行）

写任何新主题前**必须先查重**，判定重复就直接跳过该主题（序号照进，不回填、不写飞书、不存草稿），在回复中列一行跳过说明即可，**不要逐个追问用户**。

**三步查重法：**

1. **查近期主题**：比对 `正文提示词.md` 里最近 10–20 个主题——同人物、同事件、同战役弧线即算候选重复
2. **查已有正文**：`grep -E '关键词' image-cards/*/article.md`（人名/战役名/名场面），看该素材是否已成文
3. **查 XHS 草稿**：`grep 关键词 /tmp/xhs_drafts.txt`（`/tmp` 缓存可能过期或**被系统清空**，需准确列表时重新拉取：`opencli xiaohongshu drafts -f plain | tee /tmp/xhs_drafts.txt`）

⚠️ **科技类帖无素材库**：跳过第 1 步（不查 `正文提示词.md`），重点走第 2、3 步（产品/系统/热点名 grep 已有成文与草稿，如「iOS 27」「苹果新系统」），且选题本身要先 `websearch` 确认是当周热点。

⚠️ 旧系列文件夹（如 `guan-yu-history`、`water-flood-battles` 等英文slug目录）**很多不在 `.feishu_uploaded` 里**——查重不能只信该日志，必须同时看第 2、3 步。

**判定标准：**

| 情形 | 处理 |
|------|------|
| 主体人物/事件与已有成文或草稿相同（新文几乎全文都会是旧文换皮） | **直接跳过** |
| 仅次要提及重叠，但主体角度不同（人物深挖 vs 主题综述；单事件深挖 vs 通史类编译） | **保留写**：正文开头即换角度，**主动避开旧文已写过的段落**，飞书审核时标注重叠说明 |
| 原稿本身有大段整句重复（如 446 重复×3、448 重复×5） | 属于素材质量问题，不构成跳过理由——重写修正即可 |

**已执行记录（2026-09-28）：**

- 跳过：**446**（=442 刘渊洛阳）、**449**（=443 轲比能）、**450**（=444/445 袁氏投蹋顿）、**451**（=444/445 白狼山斩蹋顿）
- 保留改写区分：**448**（443 是"统一为何短命"主题文，448 换成"早成吉思汗一千年"人物深挖+制度对比框架，避开 443 已写的轲比能段）；**452**（425 已写"称王+封禅"，452 开篇即从五虎上将假名单切入，全文不写封禅梗）

#### 素材使用教训（2026-09-28）

- `正文提示词.md` 部分原稿有**整段/整句多次复制**（446、448、450 均是）——直接通读理解后重写，不要照抄
- **无把握的数字宁可删**：448 原稿战役兵力"各万骑"记不清出处，成文时删数字只留"三路大军""死者十七八/各带数十骑逃回"等有把握细节
- 演义台词必须与正史区分并标注（如"虎女焉肯嫁犬子"演义加工，正史只记"骂辱其使"——452 写法）
- 写前先 `grep` 旧文，**主动错开旧文已用的表述和段落**，即便判定"保留写"也要让读者看不出换皮

---

### 配图经验教训（2026-09-20 新增，2026-09-22 补充）

#### 核心原则
- **每张图必须紧密结合正文描述的具体场景**，不能只是通用的人物肖像
- **要体现"故事性"**，让读者一眼就能看出是正文中的哪个情节
- **图内绝对不能有文字/书法**（用户多次强调；**限历史类**——科技帖封面恰恰要英文大字，禁止的是中文大字，见科技类帖速览）

#### 人物形象规范
- **武将**：必须穿铠甲（铁札甲/皮甲），明确写 `armor`、`military commander`，否则画成文官
- **老年武将**：白发苍苍+铠甲，体现"七十多岁"的年龄感
- **道士**：必须有道袍、白须，不能是光头或普通人形象；不要擅自加道冠
- **将军**：必须有头发（短黑发），不能是光头
- **面孔/身材**：`handsome, elegant, slender, refined`，用户多次拒绝"矮胖子"
- **服饰**：必须符合东汉末年风格（深衣、曲裾、直裾、宽袖长袍）
- **朝代要匹配正文**：写三国就不要出现东汉卫兵装束的矛盾（除非剧情确为汉宫），写北魏不要画成汉代

#### 场景描写规范
- **不能只有人物**：要有环境、道具、动作，体现"场景感"
- **要有故事性**：如"率军夜袭宫门"要有士兵、城门、火把等元素
- **避免人物肖像画**：要体现"正在发生的事情"
- **场景不能太空**：用户反馈过"图2、图3太空了"——需补充人物群像、建筑、兵器、山水等环境元素

#### 提示词写法改进
- **描述要具体到"动作"和"表情"**：如 "staring intensely into eyes"、"leading troops through gates"
- **要包含"环境细节"**：如 "by lamplight"、"at night"、"torchlit scene"、"across a river"
- **避免模糊描述**：如 "wise physician" 要改为 "physician staring into patient eyes"
- **三图风格必须统一**：如果图2风格与图1、图3偏离，把图1的风格前缀原样复制到图2的 prompt 开头，再重画图2
- **分图叙事**：三张图分别对应正文三个不同情节，不要三张都画同一个场面

#### 常见问题与对策
| 问题 | 对策 |
|------|------|
| 超自然元素画错（飞头变断头） | 明确写 "head floating above body, alive, not severed" |
| 仙人画成道士/和尚 | 明确区分服饰特征 |
| 武将画成文官 | 强制写 armor + military commander |
| 人物光头 | 明确写 hair 描述 |
| 人物矮胖 | 写 slender/tall/elegant |
| 图内出现文字 | prompt 加 "no text, no calligraphy, no writing" |
| 三图雷同 | 每图指定不同地点/人物/动作 |
| 图与正文脱节 | 先回看正文对应段落，把那段的关键元素写进 prompt |
| content_policy_violation | 删敏感词重写，不要原样重试 |
| 503/空响应 | 正常，gen_one.py 会自动重试；单图 curl 需手动重试 |

#### 正文常见问题与对策（2026-09-22 补充）
| 问题 | 对策 |
|------|------|
| 正文混入英文单词（如 contemporaries） | 写完后 `grep -nE '[a-zA-Z]{2,}'` 全文扫描，发现即改中文 |
| 标题超 20 字 | 写 article.md 前先数标题字数，`head -1 \| python3 -c "print(len(...))"` |
| 字数不足 700 | 扩写主叙事细节，禁止加"后世影响/现代启示" |
| 史实错误 | 写前 webfetch/grep 查证，有疑则删 |

### 经验教训（2026-09-23 场景431）

- **403 "Model is blocked"（带参考图时）**：`gen_one.py` 带 `payload["image"]` 请求 2.1/2.0 模型可能触发 403 PermissionDeniedError（上游模型权限问题，与内容策略无关）。gen_one.py 会自动轮换 key/模型重试 20 次，若全部 blocked 则彻底失败，**不会自动降级到无参考图**。对策：按用户要求写 `gen_no_ref.py` 副本（删 `image` payload 逻辑），02/03 各开线程并行无参考图生成，首次命中 200。一致性靠统一风格前缀保证，审图时重点看三张风格是否统一
- **API key 位置**：`~/.baoyu-skills/.env`（3 行 `AGNES_API_KEY/KEY2/KEY3`），跑 gen 前 `set -a; source ~/.baoyu-skills/.env; set +a` 加载；若文件不存在由用户提供后重新写入
- **lark-cli 沙箱**：keychain token refresh 被 workspace-write 沙箱拒绝时，用 `sandbox_permissions: danger-full-access` 重试一次即可；若审批策略为 "never" 则会自动通过

### 经验教训（2026-09-28 数据丢失事故 — 正文提示词.md 被清零后恢复）

**事故**：批量修复提示词污染的脚本（`fix_469_484.py` 等）中 `c.find(f'## 主题 {n}')` 返回 -1 时，`c[:start] + nb + c[end:]` 拼接逻辑错误，导致 `正文提示词.md` 被写成 0 字节（10:51），491 个主题全部丢失。

**根因**：
1. 按 `find` 定位边界而非 `re.split(r'(?m)^## 主题 ', c)` 分块 — find 失败返回 -1 不报错，静默产出垃圾/空内容
2. 循环内重复对全局 `c` 做 find，前一轮结果污染后一轮定位
3. 修改前**没有备份**，直接对 1.4MB 唯一正本 `open(path,'w')` 覆盖写

**恢复路径（成功）**：
- opencode 快照：`~/.local/share/opencode/snapshot/<hash>/<hash>/objects/` 下 zlib 压缩 git blob，`zlib.decompress` 后 `split(b'\0',1)[1]` 取内容，按 `## 主题` 匹配筛出目标文件 blob
- ⚠️ **快照松散对象会被 git gc 极快回收**（本次发现到被清仅 ~30 分钟），找到后必须立即解出保存到 `/tmp/` 再慢慢分析
- 备份源优先级：快照 blob（含最新未提交修改）> git HEAD（仅到 419）> 会话 DB（`~/.local/share/opencode/opencode.db` 中的 write 记录/命令历史）
- 恢复后仍残留 33 处污染（452-484 提示词1），用安全版修复脚本（`re.split` 分块 + 逐行替换）补齐

**铁律（防复发）**：
1. **批量改文件前必备份**：`cp 正文提示词.md /tmp/正文提示词.bak.$(date +%H%M%S)`，写脚本第一步先做这步
2. **脚本写到 /tmp/ 再执行**，绝不内联 heredoc 跑写文件的 python（JSON 解析易炸）
3. **按主题分块用 `re.split`，禁用循环内 `c.find` 定位**；find 结果必须 `if start < 0: raise`
4. **写完立即验证**：行数（13551）、主题数（491）、污染串计数（0）、420-521 缺失检查 — 任一异常立即从备份回滚
5. **恢复成功后立即 git commit**（未提交的恢复成果没有第二道保险）
6. 修复脚本对同一文件**只跑一次**，跑完脚本即删/即标记，防止重复执行造成二次损坏

## Git & 部署

- **独立仓库**：本目录是独立 git repo，remote 为 `https://github.com/thehejian/xiaohongshu.git`（NOT 属于 `/Users/mac` 主仓库）
- **图片与生成物忽略**：`.gitignore` 忽略图片、`_payload_*.json`（含 base64 图）、`node_modules/`、`__pycache__/`、`*.mp4`、`*.log`、`.DS_Store`
- **定时推送（仅原 macOS 环境）**：`auto_push.sh` + launchd plist 不在本仓库内，部署在原机 `~/Library/LaunchAgents/`；日志 `/var/log/xiaohongshu_cron.log`
  - 无变更时自动跳过，不会产生空提交

### 经验教训（2026-09-20）

- **远程仓库已有内容时**：`git pull --rebase` 可能因数据量大导致 `early EOF` / `partial file` 错误，此时直接 `git push --force` 覆盖即可（用户确认过远程内容不需要保留）
- **crontab 在 opencode 环境阻塞**：`crontab -` 命令会超时卡死，改用 launchd plist 更可靠
- **launchd 加载**：先 `launchctl unload` 再 `launchctl load`，避免重复加载报错
- **验证推送一致性**：`git fetch origin && git diff --stat origin/main HEAD` 确认本地与远端完全同步
