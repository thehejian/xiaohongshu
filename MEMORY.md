# 003-Twitter 项目记忆

## ⚠️ 硬规则（不可违反）

- **Agent 不得执行任何 Twitter 发布命令**（包括 `opencli twitter post`、browser 手动操作）。只准备文案，通知用户，由用户手动发送。
- 小红书发布前必须先飞书预览审核，审核通过后再保存草稿。
- 推送到 GitHub 是最后一步，手动触发。

## 一、完整流水线

```
写文章 (article.md) → 生成卡片 (SVG → Inkscape → PNG) → 飞书预览
  → 用户审核 ← → 保存小红书/头条草稿 → 用户手动发布 → Git 推送（手动）
```

## 二、核心约束

### 小红书
| 约束 | 值 |
|------|------|
| 标题 | ≤ 20 字符（UTF-8 字符数，非字节） |
| 正文 | ≤ 950 字（XHS 硬上限 1000） |
| 正文首行 = 标题 | 用户偏好 |
| 正文不含时间/版本号 | 去掉日期、版本号 |
| 图片 | ≤ 9 张/帖 |
| 话题标签 | 正文末尾 `#话题`，**不传 `--topics`** |
| 正文格式 | 纯文本，无 Markdown |

### 今日头条
| 约束 | 值 |
|------|------|
| 标题 | ≤ 30 字 |
| 正文 | ≤ 2500 字 |
| 图片 | 封面 2.35:1 或 1:1，行内图 16:9 或 4:3 |

### Twitter/X
| 约束 | 值 |
|------|------|
| 字数 | ~140 字（CJK=2, ASCII=1, emoji=2） |
| 图片 | ≤ 4 张/推 |
| Thread | 用户已确认不发 Thread，只发单条推文 |

### 卡片尺寸
| 尺寸 | 用途 |
|------|------|
| 1024×1024 | 封面 + 内容卡 |
| 800×800 | 内容卡（旧标准，逐步淘汰） |
| 1792×1024 | 横幅（微博/头条） |

### 卡片配色
- **浅色（XHS 推荐）**：`#FAF7F2` 纯色底（非渐变），文字 `#1E293B`
- **深色（Twitter/英文）**：`#0B1027` 纯色底，文字 `#F8FAFC`
- 禁止：白色文字在浅底上、黑色/深灰文字在深底上、投影/阴影/滤镜
- 中文卡片必须用 SVG + Inkscape（PIL 渲染中文方块）
- 封面必须由 gen_cards.py 生成，`opencli gemini image` 不可靠

## 三、opencli 小红书发布

### 命令
```bash
opencli xiaohongshu publish "<正文>" \
  --title "<≤20字>" \
  --images "<相对路径,csv,≤9张>" \
  --draft true \
  --window foreground \
  --site-session persistent \
  -f yaml
```

### 关键点
- **不传 `--topics`**：niche 话题 attach 失败，正文用 `#话题` 替代
- **图片路径必须相对 CWD**：绝对路径报 `Image file not found`
- **必须 `--window foreground`**：后台无法上传图片
- **`--draft true` 每次新建草稿**：不覆盖旧草稿，草稿箱会堆积
- 三种返回状态：`✅ 发布成功` / `✅ 暂存成功` / `⚠️ 请在浏览器中确认`
- 标题字符数：`python3 -c "print(len('标题'))"`

### 已知 bug
- `upload` 命令 `markerAttr` 重复声明 → 改 `base-page.js` 中 `const`→`var`，重启 daemon

## 四、lark-cli 飞书文档

### 命令
```bash
# 创建文档（markdown 不含 H1）
lark-cli docs +create --title "标题" --markdown "$(cat README.md)" --as user

# 插入图片（一次一张，追加到末尾，--file 单数）
lark-cli docs +media-insert --doc <id> --file ./card.png --as user

# 覆盖全文（清空内容含 media blocks，需重插图片）
lark-cli docs +update --doc <id> --mode overwrite --markdown "..." --as user
```

### 关键点
- `--file` 是单数，路径必须相对 CWD
- `+update --mode overwrite` 清空文档含 media blocks
- `+media-insert` 只能追加到末尾
- `+fetch` 输出首行有 `[deprecated]` 警告，不是 JSON

## 五、SVG 生成踩坑

### 致命坑
- `height="{h}>` 缺闭合 `"` → Inkscape 静默输出空白 PNG
- `<rect width="100%">` 不被 Inkscape 支持 → 必须显式 `width="1024"`
- `&` 必须写 `&amp;`；`&middot;` `&rarr;` 不是 XML 标准实体 → 用 Unicode 字面量 `·` `→`
- CJK `letter-spacing` 与部分字符冲突 → 改用英文或去掉

### 文字重叠排查
```python
def text_extent(y, fontsize):
    top = y - fontsize * 0.25
    bottom = y + fontsize * 0.75
    return top, bottom
```
相邻元素 gap ≥ 10px 安全。X 轴分离优先于 Y 轴精细调整。

### PNG 验证
```python
from PIL import Image
import numpy as np
img = Image.open("card.png")
arr = np.array(img)
if len(np.unique(arr.reshape(-1, arr.shape[-1]), axis=0)) < 10:
    print("⚠️ 空白图片！")
```
1024×1024 正常 > 400KB，< 50KB 即空白。

## 六、内容创作

### 小红书爆款风格
- 短段落（1-2 行），emoji 分段
- 不用"首先/其次/最后/总之"（AI 味重）
- 不用营销词（"重磅""炸裂""神器"）
- 数据点用 `·` 分隔
- 开头：个人故事/情绪钩子
- 结构：先结论 → 分点 → 行动建议
- 语气：口语化，像朋友聊天
- 结尾：行动指令 + 4-6 个话题标签

### 标题公式
- 最佳 12-18 字，≤ 20 字
- 情绪式/悬念式/对比式/结论式
- 去掉空格/合并短词/砍 emoji 压缩

## 七、Twitter 发布（参考命令，Agent 不执行）

### 单条推文 + 4 图
```bash
opencli twitter post "<text>" --images "i1.png,i2.png,i3.png,i4.png" --window foreground -f yaml
```

### 已知坑
- `twitter reply` 对多行中文失败 → 用单行或 browser eval
- 连续 reply 需间隔 20-30 秒
- X.com 常被代理/CDN 阻断 → 用户网络问题
- `compose` 选择器：`[data-testid="tweetTextarea_0"]` + `tweetButtonInline`

## 八、GitHub 推送

- 仓库：`https://github.com/thehejian/xiaohongshu.git`
- 推送路径：项目根目录
- `Failed to connect to github.com port 443` → 网络抖动，重试

## 九、案例索引

每个案例文件夹包含：`article.md` + `README.md` + `gen_cards.py` + N 张 PNG/SVG

| # | 文件夹 | 主题 | 卡片风格 | 飞书文档 |
|---|--------|------|----------|----------|
| 8 | minimax-m3-xhs | M3 模型发布 | 深色·橙+紫 | 见原记录 |
| 10 | karpathy-skills-xhs | Karpathy Skills | 浅色 | 见原记录 |
| 11 | pua-xhs | PUA Skill | 深色·紫橙 | 见原记录 |
| 16 | lark-cli-xhs | 飞书 CLI | 浅色·蓝 | 见原记录 |
| 17 | opencli-xhs | OpenCLI | 深色·紫蓝 | 见原记录 |
| 18 | cli-anything-xhs | CLI-Anything | 深色·紫蓝 | 见原记录 |
| 19 | mo-xhs | OmO Agent | 深色·紫橙 | 见原记录 |
| 20 | cc-switch-xhs | CC Switch v3.16.1 | 浅色 | 见原记录 |
| 22 | anthropic-ban-reversal-xhs | Anthropic 封禁反转 | 浅色 | MOoUdJpMAoPKetx9ifqcZ6dgnqb |
| 23 | deepseek-api-apply-xhs | DeepSeek API | 浅色 | 见原记录 |
| 24 | opencut-xhs | OpenCut | 浅色 | 见原记录 |
| 25 | mcp-xhs | MCP 工具 | 浅色 | 见原记录 |
| 26 | openclaw-feishu-xhs | OpenClaw 飞书 | 浅色 | 见原记录 |
| 27 | ai-graveyard-xhs | AI 产品死亡名单 | 浅色 | 见原记录 |
| 31 | ai-interview-xhs | AI 面试模拟 | 浅色 | 见原记录 |
| 32 | video-elderly-quotes-xhs | AI 老人语录 | 浅色 | 见原记录 |
| 33 | adhd-ai-v2-xhs | ADHD AI 效应 | 浅色 | 见原记录 |
| 34 | ai-soul-interview-xhs | AI 灵魂拷问 | 双语言 | 见原记录 |
| 37 | ai-tool-stack-2026-xhs | AI 工具栈清单 | 浅色 | 见原记录 |
| 38 | grok-civilization-collapse | Grok 文明崩溃 | 深色 | 见原记录 |
| 39 | ai-rural-quotes-xhs | AI 农村语录 | 双语言 | 见原记录 |
| 40 | beiqi-lv-xhs | 北齐历史 Thread | 深色 | 见原记录 |
| 41 | 南北朝系列 | 南北朝历史 | 浅色 | 见原记录 |
| 42 | murongxi-xhs | 慕容熙 | 浅色 | 见原记录 |
| 44 | zhejiang-quxiao-zhongkao-xhs | 浙江取消中考 | 浅色 | 见原记录 |

**完整案例详情**：见 `MEMORY.md.backup`（已归档）。

## 十、历史案例关键教训

### minimax-m3-xhs (§8)
- 橙色+紫双色调深色卡，Banner 1792×1024 + Square 1024×1024 + 3 特性卡
- 标题压缩技巧：去掉"重磅"、改"跑赢"为"反超"、砍掉小数点

### karpathy-skills-xhs (§10)
- 浅色卡片配方：奶油底 + 4 原则 4 色 + 左侧 6px 色条 + 编号
- 标题：`Karpathy怒批AI写代码`（12 字符）

### PUA Skill (§11)
- 14 张大厂味道卡片，深色径向渐变 + 渐变标题
- 正文 912 字，需压缩到 950 以内

### cc-switch-xhs (§18)
- 版本更新公告卡片设计思路，红色 `v3.16.1` badge
- 飞书文档 `+update --mode overwrite` + 重插图片

### anthropic-ban-reversal-xhs (§22)
- 三层故事线：封杀中国→偷偷降智道歉→美国政府反杀
- 5 张浅色卡，标题 14 字，正文 432 字

### ai-soul-interview-xhs (§34)
- 双语言卡片设计模式：浅色中文 + 深色英文
- Twitter 只发主推文不发 Thread，`opencli gemini image` 4 次全部 no-images

### ai-rural-quotes-xhs (§39)
- 独深英文卡独立脚本模式：XHS 浅色中文 / Twitter 深色英文独立 gen_cards.py
- 英文文案策略：翻译中国特有概念，单位换算

### 批量发布 (§30)
- 37 个文件夹中 36 个已发布，`batch_post_twitter.py` / `post_remaining.sh` 脚本已大部分执行完毕

## 十一、2026世界杯系列（新技能 baoyu-xhs-images 流程）

### 技术栈切换
- 从 gen_cards.py (SVG+Inkscape) 切换到 **baoyu-xhs-images** skill + **agnes-image-2.1-flash** 生成图片
- SKILL.md 位于 `~/.agents/skills/baoyu-xhs-images/SKILL.md`
- 底层图片生成：`python3 ~/.agents/skills/agnes-image-gen/generate.py`
- 风格：`screen-print`（海报风、平涂色块、半调纹理、符号化叙事）
- 背景：奶油色 `#FAF7F2`，文字 `#1E293B`

### baoyu-xhs-images 工作流
```
Step 0: 创建 EXTEND.md（配置 preferred_image_backend, style 等）
Step 1: 分析内容 → analysis.md
Step 2: 确认方案（可跳过加 --yes）
Step 3: 写 outline.md → prompts/NN-xxx.md
Step 4: Image anchor chain → cover 先出图，其余以 cover 为 ref
Step 5: 飞书预览 → 小红书草稿
```

### Image Anchor Chain
- 图片1（封面）先单独生成，不用 ref
- 图片2+ 以图片1为 `--image` ref 参数，保持风格一致性
- 关键命令：`generate.py "<prompt>" --size 1024x1024 --output dir/ --prefix xx-name --image cover.png`

### 文字重叠规避
- prompt 中加入：`SMALLER text size` 减少字号30%、`Keep ample whitespace`
- 每点不超过6个字符

### 球员人种准确性（关键）
- 库拉索队：100%非裔黑人/非欧混血（克里奥尔人），prompt 中必须明确
- 佛得角球员：非裔克里奥尔人（葡萄牙+非洲混血）
- 沙特球员：阿拉伯人种
- 伊朗球员：波斯人种

### 本会话世界杯文章清单
| 主题 | 文件夹 | 卡片 | 飞书文档 | 状态 |
|------|--------|------|----------|------|
| 德国7-1库拉索（2026世界杯E组首轮） | curacao-xhs/ | 4张 | LwGWdGqdRoZgS4xM6qDc6jl1ncd | ✅ 草稿保存 |
| 佛得角介绍 | capeverde-xhs/ | 4张 | KCIGdCR0HooBPDxVshFcuwOwnD2 | ✅ 草稿保存 |
| 佛得角0-0西班牙 | capeverde-spain-xhs/ | 4张 | HdyUdpfceocBKxx9WhGcuBV2neb | ✅ 草稿保存 |
| 南美足球×百年孤独 | solitude-football-xhs/ | 8张 | FeXldT2QLomoSPxDrfQcM8bqn9f | ✅ 草稿保存 |
| 美加墨世界杯年轻身价预测 | worldcup-young-stars-xhs/ | 6张 | NS50dKe5koZmi8xArE3cHnZwn1f | ✅ 草稿保存 |
| 沙特1-1乌拉圭 | saudi-uruguay-xhs/ | 9张 | EJ1Vd2Py6oSuBZxGvZ9cQXVDnre | ✅ 草稿保存 |
| 伊朗vs新西兰预测 | iran-nz-prediction/ | 0张 | IPgKd5sHxoT8zWxW3L6cksSBnzd | 📋 预测完成，未发布 |
| 伊朗2-2新西兰 | iran-nz-xhs/ | 4张 | IZn8du21Oonl81xZcdycHPJjnHd | ✅ 草稿保存 |

### 本会话世界杯战绩（实时更新）
| 场次 | 比分 | 亚洲球队表现 |
|------|------|-------------|
| 德国 vs 库拉索 | 7-1 | 库拉索首秀 |
| 佛得角 vs 西班牙 | 0-0 | ✅ 亚洲不败（佛得角属非洲非亚，观察） |
| 沙特 vs 乌拉圭 | 1-1 | ✅ 亚洲不败 |
| 伊朗 vs 新西兰 | 2-2 | ✅ 亚洲不败（9场3胜6平0负） |

### 飞书文档审核规范
- 文档内容必须包含**完整正文（article.md）** + 所有图片
- 流程：`+create --markdown "$(cat article.md)"` → `+media-insert` 逐张插图片
- 如果此前只放了图片，用 `+update --mode overwrite --markdown "$(cat article.md)"` 补正文，再重插图片
- 预测/非发布内容也应有完整文本

### 世界杯话题标签规则
- 所有世界杯系列文章/推文必须包含话题标签 `#世界杯里看世界` 和 `#小众国家游记`
- 放在正文末尾的话题标签列表中

### 已知问题
- `baoyu-image-gen` 脚本（bun + main.ts）在 macOS 上超时 → 改用 `agnes-image-gen/generate.py` 直接调用
- Agnes API 单次返回1张图片，`--n` 参数不支持 >1
- 图片 URL 有效期1小时，须及时下载
- **Python SSL 故障**：Python 3.14 的 SSL 库与 Agnes API 服务器不兼容，`requests.post` 报 `SSL: UNEXPECTED_EOF_WHILE_READING`
  - `verify=False` 无效，错误来自底层 OpenSSL
  - 修复：用 `curl -s --max-time 300` 替代 Python requests
  - 带 ref 图时 payload 可达 2MB+ → 写 JSON 到临时文件，`curl -d @/tmp/payload.json`

### Agnes prompt 避坑

**禁止在 prompt 中使用色号代码**（如 `#FAF7F2` `#1E293B`）→ AI 会把色号当文字渲染到图片上。改为自然语言描述（如 `cream colored background` `dark navy text`）。

**中文文字**：prompt 中必须明确指定 `Chinese text labels` 或 `Chinese title "具体文字"`，否则 AI 默认出英文。

**人种对应**：prompt 中涉及人物时，必须明确指定该地区的人种/族群，否则 AI 默认出东亚面孔。
| 地区 | 真实人种 | prompt 关键词 |
|------|---------|--------------|
| 加勒比/库拉索 | 非裔加勒比人 | `Afro-Caribbean` |
| 中东/约旦 | 阿拉伯人 | `Arab Middle Eastern` |
| 北非/阿尔及利亚 | 阿拉伯人/柏柏尔人 | `North African Arab` |
| 非洲/佛得角 | 克里奥尔人（黑白混血） | `Cape Verdean Creole` / `African` |
| 阿根廷 | 白人（西班牙/意大利后裔） | `European-descended Argentinian` / `white Latin American` |
| 东亚 | 东亚人 | `East Asian` |
| 欧洲 | 白人 | `European` |
| 巴拿马/中美洲 | 混血人（印欧混血） | `Mestizo Latin American` |
| 南美一般 | 以混血和欧洲后裔为主 | 按具体国家：阿根廷white，秘鲁/玻利维亚indigenous |

**curl 大 payload 并行失败**：zsh 的 `$` 变量展开在 `-d @` 参数中可能出错（2MB+ 文件）。修复：使用硬编码路径 `/tmp/pXX.json`，或在一个 curl 完成后再进行下一个，避免并行竞争。

### 小红书帖子制作经验教训（此轮总结）

**流程**
- 完整链路：写 article.md → 写 6 个 prompt → 生成图片（cover 先，其余以 cover 为 ref）→ 飞书文档（创建+插入图片）→ 用户审核 → 小红书草稿
- 每个帖子约 30-40 分钟全流程
- image-cards 目录规范：`<folder>/image-cards/<slug>/prompts/` + 6 张 png

**Agnes AI 常见失败模式**
| 失败原因 | 表现 | 修复 |
|---------|------|------|
| 内容安全策略触发 | HTTP 400 `content_policy_violation` | 去掉敏感词（"colonial"/"slum"/"war"等），简化 prompt |
| SSL 握手失败 | Python requests 报 EOF | 改用 curl |
| 图片文字是英文 | 图上出现英文而非中文 | prompt 加 `Chinese text labels` + `Chinese title "..."` |
| 图片有无关文字（色号） | 图上出现 `#FAF7F2` 等 | 删除 hex code，用自然语言 |
| 人种不对 | 中东场景出现东亚面孔 | 显式指定人种关键词 |

**prompt 编写经验**
- 不要写 `screen-print` `halftone textures` `flat color blocks` —— 容易触发内容过滤，且风格控制不稳定
- 简短明确的 prompt 反而效果更好，如 `"Panama City modern buildings along coast, poster style, cream background"`
- Chinese title 指定要简洁，控制在 5-10 字
- 带 ref 图（img2img）一致性更好，但 payload 大容易出问题

**AI 图片中文文字渲染**
- Agnes API 生成的图片中 Chinese text 大概率乱码/方块，不要在 prompt 里要求渲染中文文字
- 正确做法：prompt 中写 `NO Chinese text anywhere`，AI 只出画面；再用 Pillow（PIL）叠干净中文文字到 AI 图上
- macOS 可用字体：`LiHei Pro`（路径 AssetData 下）、`PingFang`（PrivateFrameworks 下）
- `Pillow ImageFont.truetype()` 对 `.ttc` 文件兼容性差，优先用 `.ttf`
- `ImageDraw.rounded_rectangle()` 支持圆角矩形（用 Pillow ≥ 8.0），`rectangle(radius=...)` 不存在

**SSL/网络问题**
- `agnes-image-gen/generate.py` 的 Python requests 在 Python 3.14 上 SSL 频繁报 `UNEXPECTED_EOF_WHILE_READING`，尤其带 ref 图（payload 大时）
- 改用 curl：先写 JSON 到 `/tmp/payload.json`，再 `curl -s --max-time 300 -d @/tmp/payload.json`
- 多个 card 可以并行生成提升效率

**内容安全策略**：Agnes API 对某些词非常敏感，包括 `colonial`、`slum`、`poor`、`war`（但可用于足球/历史语境）、`refugee`、`conflict`。触发时简化到只剩景物描述。

**多轮修复原则**
- 用户只抱怨某一张卡时，只修那一张，不要顺手把没问题的卡也重新生成
- 每次改 prompt 后如果需要重新生成所有卡，先问用户确认
- 始终备份原始 prompt 到 `prompts/` 目录，便于回退

**AI底图+Pillow加字工作流（2026-06-17 新增）**
- 问题：AI直出图片中文文字乱码 + 人种错误
- 解决方案：两步法
  1. AI生成纯底图（prompt 明确要求 `absolutely NO text` + `NO letter forms` + `pure blank cream color only`）
  2. Python/Pillow 叠加清晰中文文字
- 关键：
  - prompt 中禁止色号代码（`#FAF7F2` → AI 会当成文字渲染），改用自然语言
  - 人种必须显式指定（混血=black African+white European features）
  - 底图可能残留模糊字母形状 → prompt 加 `NO typographic elements`
  - Pillow 字体优先 `.ttf`（macOS Arial Unicode），`.ttc` 兼容性差
  - 文字位置在 prompt 中预留：`Keep ample whitespace at top for title text`
- 示例脚本：`add_chinese_text.py`（Pillow 叠加中文，字体路径 fallback 链）
- 输出目录：`*-xhs/` 下的最终 PNG 文件

**飞书文档操作**
- `docs +create` 创建文档
- `docs +update --mode overwrite` 清空后重写（替换图片时必须先 overwrite 再重新 insert）
- `docs +media-insert --file ./xxx.png` 插入图片，一次只能 append 到末尾
- 不支持删除或替换已有图片 block，只能 overwrite 整个文档

### 图片生成两条路线 battle-tested（2026-06-17）
| 路线 | 适用场景 | 优点 | 缺点 |
|------|---------|------|------|
| **SVG + Inkscape** | 数据/排行榜/信息图 | 文字精准无乱码，可控性强，无内容安全策略 | 设计呆板，视觉冲击弱，用户反馈"不吸引人" |
| **AI photorealistic + Pillow 加字** | 旅行/比赛/人物 | 视觉震撼，真实感强 | 中文乱码需Pillow修正，内容安全策略随机触发，人种需显式指定 |

**决策原则**：
- 知识科普/数据类 → SVG + Inkscape（信息图）
- 旅行/赛事/人物 → AI photorealistic + Pillow（视觉优先）
- 用户不喜欢的风格直接切换，无需在原路线上硬磨

### Agnes API 故障模式排查（2026-06-17）
| 故障 | HTTP | 原因 | 修复 |
|------|------|------|------|
| `content_policy_violation` | 400 | 触发安全策略 | 简化 prompt，去掉敏感词（colonial/flag/drape/war等），只留景物 |
| `upstream error` | 500 | 服务端临时故障 | 重试 1-3 次，通常恢复 |
| 图片截断/损坏 | 200但无法打开 | 下载不完整 | 重新下载或重新生成 |
| `data` key missing | 200但无图 | 同上 | 检查 response JSON 再下载 |

### Pillow 叠加中文工作流细节（2026-06-17）
- 底图必须 AI 生成时写 `NO text or labels anywhere in the image`（不要写 `NO text` 也不够精确）
- Pillow 叠加时用 `STHeiti Medium.ttc`（macOS 系统字体，路径 `/System/Library/Fonts/STHeiti Medium.ttc`）
- 半透明黑底条：`rectangle([0, H-140, W, H], fill=(0, 0, 0, 160))`
- 文字阴影提高可读性：先画深色偏移字，再画白字
- 文字居中：`textbbox` 计算宽度后 `(W - tw) // 2`

### SVG 信息图设计教训（2026-06-17）
- 纯文字 + 横条的极简设计用户反馈"不吸引人"
- 需加视觉元素：奖杯图标、国旗、数字放大、对比色块
- 排行榜类卡片可用 8 个色条横向对比，比纯列表好
- 封面用大数字（48/22）+ 副标题，比纯文字有冲击力

### 本会话经验（messi-zidane-son-xhs，2026-06-17）

**新增案例**
| 文件夹 | 主题 | 卡片风格 | 飞书文档 | 状态 |
|--------|------|----------|----------|------|
| messi-zidane-son-xhs | 梅西爆锤齐达内之子 | AI底图+Pillow加字·screen-print | BNLAdVULhoZRPBxlSmGc7cz8nX2 | ✅ 草稿保存 |

**Pillow 叠加文字工作流成熟**
- 8张卡全部用 AI 生成纯底图（prompt 写 `NO text, NO Chinese characters, NO words, NO letters`）
- 再用 `overlay_text.py` 用 PingFang SC 字体叠加中文
- 确保 prompt 中禁止色号代码（`#FAF7F2` → 用 `cream colored background` 代替）
- 图层媒体区的文字位置：在 prompt 末尾加 `Keep ample whitespace` 预留空间

**overlay_text.py 路径设计**
- 脚本放在 `image-cards/<slug>/` 内
- `SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))` → SRC 目录
- `OUT = os.path.dirname(os.path.dirname(SCRIPT_DIR))` → `*-xhs/` 目录
- 最终输出 cover.png + card-N.png 到 `*-xhs/` 根目录

**飞书文档更新**
- `docs +update --mode overwrite --markdown "..."` 报错 `--command is required`
- 实际可行方案：直接新建文档 → 插全部图片
- 旧文档可保留不用删除

**话题标签稳定规则**
- 世界杯系列必须含 `#世界杯里看世界` + `#小众国家游记`
- 放在正文末尾话题标签列表的前两位

## 十、zhengxi-skill 项目经验教训

### 内容类型决定路线
结构化知识卡片（投资方法论/流程/对比）→ 直接走 Route A（SVG）。AI 生图+叠字在"文字即内容"的知识卡片上背景杂乱、文字不清，浪费一轮返工。

### SVG 在知识卡片上的优势
文字精确居中、对比度可控、零乱码、文件小、修改只需改 SVG 源码。AI 生图只适合纯视觉封面，不适合以文字为主要内容的知识卡片。

### cairosvg 的已知缺陷
- 小形状（<16px 的 polygon/path）渲染成模糊原点
- Unicode 符号渲染失真（①✗→ 等 dingbat 字符）
- 修复方案：SVG 里所有图形元素用大尺寸原生形状，Unicode 装饰字符替换为 `<circle>`+文字 或 `<path>` 绘制

### 全链路最小闭环测试
正式投产前先 1 张图完整走一遍：写 SVG → 转 PNG → 飞书上传 → 小红书发布。不要写满 6 张才发现转换环节有问题。每步的单点故障（cairosvg 渲染、飞书格式限制、opencli 扩展断连）都会卡住整条流水线。

## 十一、xiaomi-nas 项目经验教训

### 路线选择优先级（更新）
AI 直出中文文字路线有效，不再默认走 SVG。新产品发布/视觉类内容优先试 AI 生图（Agnes agnes-image-2.1-flash 可渲染中文），效果不好再降级到 SVG。

路线优先级：
1. **AI 直出中文**（Agnes agnes-image-2.1-flash）— 最快，视觉效果好，适合产品发布/封面
2. **SVG** — 文字精确可控，适合知识卡片/流程/对比
3. **AI 生图 + Pillow 叠字** — 最差，背景杂乱文字生硬，避免

### "AI 渲染中文必乱码"规则过时
agene-image-2.1-flash 模型可以直出中文文字。"No Chinese text in prompt" 规则可能适用于旧模型或特定 API，不再作为硬性规则。

### baoyu-xhs-images skill 流程不适用于快速出图
三步流程（分析→确认→生成）对文字卡片类内容过度设计。实际效果：prompt 文件写完后因现场调整作废，分析内容与最终成片无关。简单产品发布直接写 prompt 生成即可。

### 内容类型决定工具链（更新：2026-07-07）
- 产品发布/视觉封面 → AI 生图直出中文
- **知识卡片/流程/对比/数据 → SVG 或 AI notion 风格**
- 混合型 → AI 封面 + SVG 内容页

### 风格选择比工具链选择更重要（2026-07-07 新增）
同一套 Agnes API 不同 style 效果天差地别。选择不对等于白做一轮。

| 内容类型 | 有效的风格 | 无效的风格 |
|---------|-----------|-----------|
| 历史人物故事（商鞅变法逻辑链） | bold 红黑人物场景 | 抽象齿轮/链条（被要求重做） |
| 制度对比分析（郡县vs分封） | **notion** 白底手绘对比图 | bold 黑底人物场景（被要求重做） |

关键原则：
- **notion风格 = 知识卡片/制度对比的首选**：白底手绘线稿，左右对比/时间线结构清晰，视觉"聪明"，适合文字密集的制度分析
- **bold/screen-print风格 = 历史人物故事**：黑底红橙，戏剧冲突强，适合有人物有情节的叙事
- **抽象隐喻（齿轮/链条/箭头）在AI图里不好看**：用户明确要求"全部是古代人"——历史内容一定要有人物
- 匹配 baoyu-xhs-images 的 Auto-Selection 表的信号是对的：knowledge/concept → notion；editorial/cinematic → screen-print

### 一轮通过的预期不现实（2026-07-07 新增）
每篇配图平均需要 1-2 轮返工。用户在见到图之前无法准确表达风格偏好。预算好返工时间：
- 第一轮：按直觉选风格（通常是 bold/screen-print）
- 用户反馈后换风格（notion 或其他）
- 改 prompt + 重新生成 + 飞书新建文档

### screen-print 成为首选风格（2026-07-07 确认）
用户明确确认 screen-print（暖米白底 + 绛红/深蓝双色调，vintage 海报感）为后续首选风格。此前尝试的 notion 白底手绘被否决。结论：
- **历史制度分析 → screen-print**（暖米白底，vintage 海报，绛红/深蓝双色调）
- **所有新 topic 默认用 screen-print**，不主动推荐其他风格
- screen-print prompt 核心要素：warm cream paper background, dark navy and crimson duotone, halftone texture, bold condensed font, vintage poster feel

### screen-print + ref 超时问题
- 部分 prompt 带 `--ref` 时 Agnes API 响应极慢（>120s 甚至 >180s）
- 修复：不带 ref 重试即可成功（风格一致性靠 prompt 本身的详细描述保证，不是必须靠 ref）
- 如果 timeout：先不带 `--ref` 重试那张

### 超时规律观察（2026-07-07）
| 批次 | 风格 | ref | 结果 | 差异分析 |
|------|------|-----|------|---------|
| 户籍 02/05/06 | screen-print | 带 ref | 成功 | prompt 较简洁 |
| 户籍 03/04 | screen-print | 带 ref | 超时 >180s | prompt 有多个元素+复杂场景描述 |
| 户籍 03/04 重试 | screen-print | 无 ref | 成功 | 去掉 ref 后通过 |
| 军功爵 02-06 | screen-print | 带 ref | 全部一次过 | prompt 也复杂，但通过了 |

结论：超时不像是 prompt 复杂度的系统性问题，更可能是 Agnes API 服务端偶发负载导致。**不是每次带 ref 都会超时，同一批里有的过有的不过就是证据。** 策略：
1. 默认带 ref 生成
2. 超时后不带 ref 重试那张
3. 不要因为一次超时就不带 ref 重试整批

### notion 风格 prompt 要点
- 不要写 `#` 色号，用自然语言（"warm cream background"）
- 描述具体构图（"Split-screen comparison. Left side: ... Right side: ..."）
- 明确中文文字位置和内容（"Chinese title 'xxx' in clean sans-serif at top"）
- 保持 Minimalist/clean 关键词
- 手绘线稿风格比实景渲染更适合知识内容

## 六、古道项目复盘教训（2026-07-03）

### 环境检查
- 运行前先 `which lark-cli opencli` 确认 PATH，Homebrew 安装在 `/opt/homebrew/bin`，默认 PATH 不含
- 依赖检查：`pip3 install Pillow` 等要先装

### 图片生成 — Pillow 文字叠加字号
- 1024×1024 图：主标题 **110px** (`w*0.108`)，副标题 **60px** (`w*0.06`)，顶部半透明条 **256px** (`h*0.25`)
- 文字叠加在顶部比底部好，不被遮挡

### 飞书文档操作
- `lark-cli` 参数经常变：`--markdown` 已废弃→改用 `--content` + `--doc-format markdown`
- `--file` 路径必须用相对当前目录，不能用绝对路径
- `-f yaml` → `--format json`
- `+media-insert` 输出含进度信息，检查 `"ok": true` 需过滤最后一行 JSON

### 脚本防御
- 错误处理逻辑先小范围测试，再批量跑
- 标题用 `echo -n TITLE | wc -m` 自动校验 ≤20
- 不要用 `python3 -c "..."` 内联传中文，写单独脚本文件

### 流程控制
- 先做 1 条完整流程验证，再批量做剩下的
- 参考现有项目代码模式（如 `buendia-tree-xhs/overlay.py`），不走新路

## 七、头条号发布经验（wendi-four-sons 首次实战）

### 成功的工作流
1. 内容改编：从 XHS 版（~950 字，口语化）改为头条版（~1048 字，偏正式，无标签）
2. 图片处理：XHS 720×960 (3:4) → PIL resize_with_padding → 封面 1176×500 (2.35:1) + 行内 1280×720 (16:9)
3. 飞书预览：先建文档让用户审核（虽然这次用户跳过直接说 OK）
4. 浏览器自动化：`opencli browser session` 系列命令填充 + 发布

### opencli 操作要点
- `opencli bind` 不存在，改为 `opencli browser session bind`
- 页面元素定位：用 `state` 获取 DOM 快照，找 `data-opencli-ref` 编号，用编号 `click`/`fill`/`type`
- `type` 比 `fill` 更适合 contenteditable 编辑器（fill 对 textarea 有效，contenteditable 用 type）
- **导航离开发布页会丢失全部内容**（头条是 SPA，编辑器状态不持久）
- 封面上传：先选"单图"radio，再用 `upload "#upload-drag-input" <path>`，但 `#upload-drag-input` 可能消失（显示状态变化），此时改用 `upload "input[type=file]" --nth 1`
- 行内图上传：点击 toolbar 的 image 按钮（`.syl-toolbar-tool.image`）打开上传抽屉，上传后点 `[data-e2e="imageUploadConfirm-btn"]` 插入

### 发布流程关键点
1. fill title → type body → upload cover → click "预览并发布" → click "确认发布"
2. "预览并发布" 和 "确认发布" 是两步——先点预览进入确认页，再点确认真正发布
3. **SylEditor 工具栏按钮无 title/aria-label**，识别靠 `state` 快照中的 `syl-toolbar-tool image` class
4. 发布成功后会留在同一 URL（SPA），不跳转，需去 `/profile_v4/manage/content/all` 验证
5. 发布后文章显示"已发布"和"07-19 19:19"时间戳，可以从详情页拿到 item URL

### 图片生成经验
- Agnes API 全线 503（Service busy）——无法生图，备选方案是 PIL 处理已有图片
- 头条图片复用 XHS 图转制可行：PIL `resize_with_padding` 加米白底 `#FAF5EB` 填充空白
- 封面 2.35:1 用 1176×500，行内 16:9 用 1280×720——发布后显示正常
- 对比重新生成 6 张 Agnes 图（需 10-30min + 503 风险），PIL 转制只需 2s

### 踩坑记录
- ❌ 第一次点完"确认发布"后去检查 manage/content，返回时编辑器内容清空（SPA 导航丢失）
- ❌ `element.click()` (JS eval) 不如 `opencli browser click <ref>` 可靠——前者可能不触发 React 事件
- ❌ 封面 `#upload-drag-input` 在切换封面模式（单图→无封面→单图）后可能消失，需要重新获取 state
- ⚠️ 文章保存为草稿是自动的（"草稿保存中..."），但导航离开后草稿不会自动恢复为编辑器内容
- ⚠️ 标题字数显示"11/30"是 CJK 字符数，不是字节数，与 XHS 行为一致

### 改进建议
- **发布页导航后内容丢失无法恢复，建议一次性完成所有操作**
- 首次发布前先用 `opencli browser screenshot` 确认页面状态，避免盲操作
- 封面图先用 PIL 生成好（2s），不要依赖 Agnes 生图（503 不可控）
- 行内图可省略——头条文章纯文字也能通过审核，配图只是加分项

## 十二、行内图片插入经验（wendi-four-sons 第二次发布实战）

### 成功的工作流（已验证可插入行内图）
1. 首次发布的文章无行内图，需重新发布（不可编辑已有文章插入图片）
2. 正确流程：**先插行内图，再传封面**

### 行内图插入（图片抽屉）

**核心步骤：**
1. 打开图片抽屉：`[data-e2e=imageToolbar-btn]` 或 `.syl-toolbar-tool.image button`
2. 点击抽屉内的"本地上传"按钮
3. 用专用 selector `.upload-btn input[type=file]` 上传所有图片（一次性多选，利用 `multiple=true`）
4. 等待"已上传 N 张图片"出现
5. 点击"确定"按钮（`button` 文本含"确定"）插入到光标所在位置

**必须用 `.upload-btn input[type=file]` 而非 `input[type=file]`：**
- 后者页面中通常有 2 个匹配（封面 + 抽屉），导致上传双倍（6 张变 12 张编辑器元素）
- `.upload-btn input[type=file]` 只匹配 1 个，恰好是抽屉内的隐藏 input
- `matches_n: 2 → 12 张`，`matches_n: 1 → 6 张`（编辑器内 12 个 `<img>` 是正常现象——桌面端+移动端双渲染）

### 封面无法通过自动化上传
- 封面自定义上传的 `#upload-drag-input` 在发布页加载后可能不存在（需先点击覆盖上传图标激活）
- 即使激活，后续打开图片抽屉后文件 input 数量变化，selector 失效
- **替代方案：封面作为第一张行内图**（00-cover.jpg 以行内图形式上到正文最前面）
- 发布后封面区域显示空白（系统自动在正文中取一张作为封面），但正文第一张图就是封面图，效果可接受

### 编辑器内容验证
- 编辑器内 `<img>` 数量是实际图片数 × 2（桌面端 + 移动端双渲染）
- 发布后文章中图片以懒加载占位符展示（`data:image/gif;base64`，透明，676×380）
- 滚动到视口范围内后替换为真实 CDN URL（`p3-sign.toutiaoimg.com/tos-cn-i-*`，1280×720 自然分辨率）
- 因此用 `editor.querySelectorAll('img').length` 验证得到 12（6 张 × 2）是正常的

### 发布后的验证
- 发布成功后留在同一 SPA 页面，不跳转
- 去 `https://www.toutiao.com/article/<id>/` 确认，滚动到正文区域触发懒加载
- 真实图片 URL 模式：`p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/` 或 `tos-cn-i-axegupay5k/`
- 图片尺寸 676×380（显示） / 1280×720（自然），与上传的 16:9 匹配

### 踩坑记录
- ❌ `input[type=file] --nth 0` 匹配 2 个 input → 6 张图变 12 张编辑器元素
- ❌ `#upload-drag-input` 在封面未激活时不存在 → upload 报 selector_not_found
- ❌ 图片抽屉关闭后再打开不会清空之前上传的图片（SPA 状态保持）→ 第二次插入时会累积旧图片
- ⚠️ 标题支持最多 30 字，正文支持 ≤2500 字（本次正文 1048 字安全）
- ⚠️ 浏览器标签页状态累积：同一个 tab 内多次导航到发布页，图片抽屉状态不重置 → 需加载 cache-busting URL

### 可靠的操作顺序（已验证）
1. `open "https://mp.toutiao.com/profile_v4/graphic/publish?t=$(date +%s)"`（cache-busting）
2. `fill "textarea[placeholder*='文章标题']" "标题"`
3. `type "[contenteditable=true]" "正文"`
4. 打开图片抽屉 → 点击"本地上传" → 用 `.upload-btn input[type=file]` 传全部图片 → 点击"确定"
5. 封面：点击 cover 区域 [+] 图标（有时失败）→ 或干脆跳过，正文第一张图当封面
6. 点击"预览并发布"（`button` 文本含"预览并发布"）
7. 点击"确认发布"（`button` 文本含"确认发布"）
8. 去文章 URL 验证（懒加载，需滚动才显示真实图片）
