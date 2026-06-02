# 003-Twitter 项目记忆

跨会话沉淀的技术经验和踩坑记录。

## 1. opencli (Xiaohongshu 发布)

### 完整发布流程
```
写文章 (article.md)
  ↓
生成卡片 (SVG → Inkscape → PNG, 800×800)
  ↓
上传飞书 (lark-cli docs +update --mode overwrite + +media-insert × N)
  ↓
推送 GitHub (git add + commit + push)
  ↓
保存草稿 (opencli xiaohongshu publish --draft true)
  ↓
用户审核 (XHS 创作者中心 → 草稿箱)
  ↓
用户手动发布
```

### 发布命令
```bash
opencli xiaohongshu publish "<content>" \
  --title "<max20字>" \
  --images "<csv, max9, 相对路径>" \
  --topics "<csv, 不含#>" \
  --draft true \
  --window foreground \
  --site-session persistent \
  -f yaml
```

### 关键约束
- **图片路径必须相对当前工作目录**（绝对路径会报 `Image file not found`，因为 opencli 会拼上 CWD）
- **必须 `--window foreground`**：后台窗口拿不到文件选择器，图片上传失败
- **标题 ≤ 20 字符**（中英混合按 UTF-8 字符数算）：超出直接报 `Title is N chars — must be ≤ 20`
- **每帖 ≤ 9 张图**
- **每次 `--draft true` 都创建新草稿**——多次发布会堆积草稿，需手动清理

### 标题字符数算法（实测）
- `len(str) in Python 3` = Unicode 字符数，不是字节
- 1 个汉字 = 1 字符，1 个 ASCII = 1 字符，1 个空格 = 1 字符
- emoji 多数 = 1 字符（少数 = 2 字符，如带 ZWJ 组合的）
- 标点全角 = 1 字符，半角 = 1 字符
- 快速判断：`echo -n "标题" | wc -m` 或 `python3 -c "print(len('标题'))"`
- 常见错误：`"minimax M3 反超 Opus 4.7"` = 22 ❌，`"minimax M3 反超 Opus 4"` = 20 ✓

### 前置条件
- **Browser Bridge 扩展必须已连接**（chrome://extensions → 开发者模式 → 加载已解压扩展）
- 否则 `opencli` 无法控制 creator.xiaohongshu.com 页面
- 每次会话首次使用前确认扩展状态

### 调试选项
- `--trace on`：实时显示所有浏览器操作日志
- `--trace retain-on-failure`：失败时保留 trace artifact，便于排查
- `--keep-tab true`：命令结束后保留浏览器 tab（适合连续操作）
- `--site-session persistent`：跨命令复用登录态，避免重复扫码

### 正文字数
- XHS 硬上限 1000 字
- 用户常要求更紧（本次 950）—— `wc -m` 不带换行可作为字数预估
- 一条 emoji 按 1+ 字符算，超出后 XHS 会截断
- 用户指定字数限制时：`wc -m` 不带换行的数字 = 实际显示字数

### 草稿管理
- 每次 `--draft true` 都新建一个草稿，不会覆盖旧的
- 同一文章多次调整 → 草稿箱里会有多个版本
- 用户审核时需手动选一个发布、删掉其他
- 优化方案：发布前确认草稿箱状态，避免堆积

### 内容质量
- **不要在命令里带 `2>&1 | grep ok` 等过滤**：用户偏好清爽输出（详见 待办.txt）
- 检查 `ok: true` 直接看 yaml 输出即可

## 2. lark-cli (飞书云文档)

### 关键命令
```bash
# 创建新文档 (带 markdown 内容)
lark-cli docs +create --title "标题" --markdown "$(cat body.md)" --as user

# 验证文档内容
lark-cli docs +fetch --doc <id> --as user

# 插入图片（一次一张，--file 单数）—— 追加到文档末尾
lark-cli docs +media-insert --doc <id> --file <relative_path> \
  --align center --caption "图 1 · 描述" --as user

# 覆盖整篇文档
lark-cli docs +update --doc <id> --mode overwrite --markdown "$(cat file.md)"

# 旧接口: +media-insert 只能用 --file（不是 --files）
# 旧接口: --mode overwrite 是 +update 的参数，不是 +media-insert 的
```

### 完整创建流程（图文混排）
1. **准备 markdown 正文**：从 README 提取正文，**去掉 H1 标题**（title 已是文档标题）+ 去掉图片引用
2. **`+create` 创建文档**：传 title + markdown，返回 `doc_id` + `doc_url`
3. **`+media-insert` 串行插入 N 张图**：每张图一次调用，按需加 `--caption`，全部追加到文档末尾
4. **`+fetch` 验证**：检查返回的 markdown 中 `<image token="..."/>` 数量 == 实际插入数

### 踩坑
- **`--file` 是单数**，且**路径必须是当前目录下的相对路径**——`unsafe file path` 报错时要 `cd` 到目标目录或用 `./xxx`
- **`+update --mode overwrite`** 会清空文档内容（包括 media blocks）——完美用于重新生成
- **`+create` 的 markdown 中禁止 H1 标题**（与 title 重复），飞书自动生成 TOC，无需手动添加
- **`+media-insert` 只能追加到末尾**，不能在文档中间插入图片——需要穿插时改为末尾"图集"章节
- 串行调用 9 次 `+media-insert` 单图成功率约 89%（1 张可能限流），失败那张直接重试即可
- 默认 `--as user`；若用 `--as bot` 创建会返回 `permission_grant.status` 说明是否自动授权

### JSON 解析坑
- `+fetch` 输出首行是 `[deprecated] ...` 警告文字，不是 JSON
- 用 `2>&1 | tail -n +1` 或 `2>&1 | python3 -c "import json; ..."` 时需先剥离 stderr
- 简单做法：`... | tail -100` 拿到 JSON 块后再 `python3 -c '...'`

## 3. SVG → PNG 卡片生成

### 工具链
```bash
# SVG 转 PNG (中文/复杂排版必须用 Inkscape，不能用 cairosvg)
# 推荐 Inkscape 1.4+ 写法（带完整 filename 参数）
inkscape input.svg --export-type=png --export-filename=output.png

# 也可指定 width/height
inkscape input.svg --export-type=png --export-filename=output.png -w 800 -h 800

# 图片缩放
sips -Z 128 input.png --out output.png  # 长边缩到 128
```

### cairosvg vs Inkscape 对比（macOS）
- **cairosvg** 渲染中文失败 → 字符变方块（fallback 字体无 CJK 字形）
- **Inkscape 1.4+** 渲染中文正常（自带 fontconfig + macOS 字体）
- **结论：本地卡片生成统一用 Inkscape**，cairosvg 只用于无中文场景

### Inkscape 中文踩坑
- **字间距 (letter-spacing) 与部分中文字符冲突** → 显示成方块
- 出现场景：font-size=11 / letter-spacing=2 + 字符如"评测"、"发布"
- 解决：把"评测"改"AGENT BENCHMARK"、把"发布"改"MODEL DROP"，或去掉 letter-spacing
- 经验：含中文的小字标签 **优先用英文**，避免 letter-spacing 渲染异常

### 卡片设计原则（小红书爆款款）
- **浅色底优先**（深色显廉价）：`#FAF7F2` (cream) → `#F3F0E8` 渐变
- **大字号 + 留白**：标题 120px，描述 24-28px
- **真实产品 logo 优于文字头像**：从官网/GitHub 下载，PNG 128×128 最佳
- **每 app 一个品牌色**作为强调色（左侧色条 + 圆点装饰）
- **底部"适合谁用"小框**让用户对号入座，提高收藏率
- **页脚统一话题标签**（灰色小字），符合 XHS 视觉规范
- **深色卡片（科技/对比型）**：避免用纯黑（`#000`），用近黑 `#0A0A14` + 网格底纹 + 角落色块辐射

### 深色卡片大字标题布局（minimax-m3-xhs 验证）
- 大字 (font-size 160-200) baseline y 位置下移 ≥ 280，给 eyebrow (y 80-130) 留 100+ px 间距
- 数字焦点 (font-size 200+) 单独占一行，**不要同时画 label 和数字** —— label 放在数字上方 80-100 px
- 右侧对比卡 (576×720 嵌在 banner 中)：label 80px → 数字 200px → 分割线 → 4 行对比 → 底部高亮 bar

### Logo 嵌入到 SVG
- PNG → base64 data URI：`<image href="data:image/png;base64,..." x= y= w= h= />`
- SVG → 剥掉 `<?xml ?>` 声明和 width/height，嵌套在 `<svg viewBox="0 0 24 24">` 里

### Logo 获取策略
- 官方 favicon (32×32) 用 sips 放大到 128
- 闭源/fork 项目可用上游 logo：Roo Code 用 Cline 图标（Roo 是 Cline fork，原项目已停维护）
- 通用品牌用母公司 logo：Codex → OpenAI blossom SVG

## 4. 内容创作

### 小红书标题公式
- 模板：`聊聊/来了/啊 <主题> <数量/后缀>` (2 字前缀 + 主题 + 描述)
- 例：`聊聊 Hermes Agent`、`Coding Agent 月榜 TOP10`
- 避免：标题党词（绝绝子/yyds）、技术黑话堆叠
- 总长 14-18 字最佳

### 正文风格
- 短段落（1-2 行为宜），密集 emoji 分段
- 不用 `首先/其次/最后/总之`（AI 味重）
- 不用营销词（`重磅`、`炸裂`、`神器`）
- 数据点用 `·` 分隔：`跨会话记忆 · 40+ 工具 · 子 Agent 并行`
- 末尾 4-6 个话题标签：英文 + 中文混搭

### 排行榜内容结构
- 介绍（前 2 名点名、整体趋势）
- 列表（1️⃣-🔟 编号 + token 数据 + 一句描述）
- 观察（4-5 个 emoji 引导的洞察）
- 话题标签

## 5. GitHub 推送

### 仓库
- https://github.com/thehejian/xiaohongshu.git
- 推送路径：`/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter`

### 常见问题
- `Failed to connect to github.com port 443` — 网络抖动，等几秒重试
- `Error in the HTTP2 framing layer` — HTTP/2 协议层错误，重试即可
- 两种错误都不需要改 config，retry 就好

## 6. 数据源注意事项

- **OpenRouter Apps 页是 Next.js 客户端渲染**，无法直接 scrape
- 排行榜数据要交叉验证（daily/weekly/monthly 数字差异巨大）：web search 多关键词 + task agent 横向校对
- 本次以"月度 Token 消耗"为口径统一所有数字

## 7. 卡片配色风格（白/黑两种）

项目里**同时存在**两种卡片配色体系，按内容文件夹分布：

| 文件夹 | 风格 | 主色 | 尺寸 | 用途 |
|--------|------|------|------|------|
| `hermes-xhs/` | **DARK** 深色 | `#7C3AED` 紫 | 800×800 | 单项目深聊 |
| `github-skills-top10-xhs/` | **DARK** 深色 | 渐变 | 1792×1024 banner | 排行榜横幅 |
| `github-trending/` | **DARK** 深色 | 渐变 | 1024×1024 | 榜单卡片 |
| `weibo-top10-xhs/` | **LIGHT** 浅色 | 品牌色 | 1792×1024 banner | 排行榜横幅 |
| `openrouter-top10/` | **LIGHT** 浅色 | 品牌色 | 800×800 | 排行榜卡片 |
| `minimax-m3-xhs/` | **DARK** 深色 | 橙 `#FF6B35` + 紫 `#8B5CF6` | 1792×1024 + 1024×1024 | 模型发布对比 |

### 何时选深色
- **品牌色本身就是深色**（紫色 Hermes 紫、深蓝 GitHub 黑）
- **科技/技术深度内容**，需要"严肃感"
- **单项目深聊**类（一篇文章只讲一个产品）

### 何时选浅色
- **小红书爆款款**：XHS 主流卡片就是浅色/奶油色（cream `#FAF7F2`）
- **多 app 对比**：每 app 一个品牌色作为强调色，浅底更突出
- **排行榜/TOP10 类**：需要清晰分隔多个 entry
- **面向 C 端用户**，降低视觉压迫感

### 决策建议
- **新内容先选浅色**——XHS 用户审美偏好浅色，浅色点击率普遍更高
- **深色用于：产品本身就是深色品牌**（如 Hermes 紫） 或**专题深聊**
- 同一篇文章的所有卡片必须统一风格，不要混搭
- 卡片文件命名带主题前缀方便识别：`hermes-card-*.png` / `or-card-*.png` / `weibo-*.png`

## 8. minimax-m3-xhs 案例（参考样例）

**任务**：minimax M3 模型发布的小红书内容
**完成时间**：2026-06-02
**文件**：`minimax-m3-xhs/` （5 PNG + 5 SVG + 1 README + 1 gen_cards.py）

### 完整工作流（已验证）
1. **用户原始输入**：模型发布链接 + "先整理思路"
2. **思路整理**：列出内容定位、标题候选、配图方案、调性
3. **用户选择**：对比型标题 / 5 张全套图 / 专业震撼调性
4. **创建目录 + 写 README.md**（小红书风格正文）
5. **写 `gen_cards.py` 用 Python 生成 SVG**（banner + square + 3 特性卡）
6. **Inkscape 串行转 PNG**（替代 cairosvg，解决中文渲染）
7. **修复渲染问题**：banner 标题重叠 / 字号过大 / "评测/发布"显示方块
8. **git commit** 12 文件
9. **发布飞书文档**：`lark-cli docs +create` + 5 次 `+media-insert`
10. **保存 XHS 草稿**：`opencli xiaohongshu publish --draft true`

### 信息源采集策略
- 用户给一个 URL（minimaxi.com/models/text/m3）→ 用 `webfetch` 一次性拿全页面 markdown
- 提取关键数据：3 个核心卖点 + 3 个 demo + 4 种接入
- 数字亮点优先入卡片：BrowseComp 83.5 / PostTrainBench 37.1 / 9.4× 加速 / 147 次迭代

### 卡片配色（橙+紫双色调）
```python
ORANGE   = "#FF6B35"   # minimax 品牌主色
ORANGE_D = "#F97316"
PURPLE   = "#8B5CF6"   # 辅色（次要数据/对比）
CYAN     = "#06B6D4"   # 第三个能力
GREEN    = "#10B981"   # 第四个能力 / 成功
GOLD     = "#FBBF24"   # 渐变终止色
BG       = "#0A0A14"   # 近黑（避免纯 #000）
BG_PANEL = "#15151F"
```

### 5 张图清单（minimax-m3-xhs）
- `m3-banner.png` 1792×1024 — 横版：左侧大字标题 + 右侧 BrowseComp 焦点对比
- `m3-square.png` 1024×1024 — 小红书封面：标题 + 数字对比 + 4 个 chip
- `m3-card-1.png` 1024×1024 — BrowseComp 83.5 vs Opus 4.7 大数字 + 4 行条形图
- `m3-card-2.png` 1024×1024 — 12h ICLR 论文复现：3 数据卡 + 4 段时间线
- `m3-card-3.png` 1024×1024 — CUDA 9.4× 加速：起点/终点进度条对比 + 3 数据卡

### XHS 标题压缩
- 原："重磅!minimax M3 发布 · BrowseComp 83.5 跑赢 Opus 4.7" (46 字符)
- 压缩："minimax M3 反超 Opus 4" (20 字符) ✓
- 技巧：去掉"重磅"等营销词 / 改"跑赢"为"反超" / 砍掉小数点后

### 飞书文档 URL（成功案例）
- `https://www.feishu.cn/docx/AuX8d8FlooBMYOxHxaycnyKwnpf`
- 5 张图全部上传成功（image token 数 == 5）

### lark-cli 与 XHS 草稿顺序
- **先 git commit**（让本地有完整备份）→ 再飞书 → 再 XHS 草稿
- 这样中途失败可以从 git 恢复

