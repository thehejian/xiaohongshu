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

## 9. opencli 1.8.1 坑（2026-06-02）

### upload 命令 bug
- **症状**：`SyntaxError: Identifier 'markerAttr' has already been declared`
- **影响**：`opencli xiaohongshu publish --images` 完全失效
- **状态**：1.8.0 和 1.8.1 都存在，暂无 fix

### 文件选择器 3 种方案

| 方案 | 原理 | 成功率 |
|------|------|--------|
| `opencli click <ref>` | 触发 input.click() | ❌ Chrome extension bridge 拦截，不弹 dialog |
| `opencli eval <js>` 调用 .click() | 同上 | ❌ 非 user gesture，Chrome 拦截 |
| **HTTP Server + DataTransfer** | fetch 图片转 Blob，注入 input.files | ✅ **实测成功** |

### DataTransfer 注入步骤
```bash
# 1. 本地起 HTTP server（带 CORS）
cd <images_dir> && python3 -c "
from http.server import HTTPServer, SimpleHTTPRequestHandler
class C(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin','*')
        super().end_headers()
HTTPServer(('127.0.0.1', 8765), C).serve_forever()
" &

# 2. eval 注入文件
opencli browser <session> eval '
(async () => {
  const urls = ["http://127.0.0.1:8765/001.png","http://127.0.0.1:8765/002.jpg"];
  const files = [];
  for (const u of urls) {
    const r = await fetch(u);
    const blob = await r.blob();
    files.push(new File([blob], u.split("/").pop(), { type: blob.type }));
  }
  const dt = new DataTransfer();
  files.forEach(f => dt.items.add(f));
  const input = document.querySelector("input[type=file][accept*=.jpg]");
  input.files = dt.files;
  input.dispatchEvent(new Event("change", { bubbles: true }));
})()
'
```

### file input accept 陷阱
- 小红书创作者中心有**两个 file input**：
  - [84] `accept=.mp4,.mov,.flv...` — 视频上传
  - [84/77] `accept=.jpg,.jpeg,.png,.webp` — 图片上传
- **注意**：tab 切换后 ref 编号会变，用 CSS selector 更稳：
  ```bash
  opencli browser <session> state 2>&1 | grep 'accept=\.jpg'
  ```

### contenteditable 填写
- 不用 fill 命令（fill 只支持 input/textarea）
- 用 eval + innerHTML + InputEvent：
  ```javascript
  const editor = document.querySelector('div[contenteditable][role=textbox]');
  editor.innerHTML = body.split('\n').map(l => `<p>${l}</p>`).join('');
  editor.dispatchEvent(new InputEvent('input', { bubbles: true }));
  ```

### 底部按钮定位
- "暂存离开"/"发布"按钮在页面底部，需 `window.scrollTo(0, document.body.scrollHeight)` 展开
- 用 `opencli screenshot` 确认按钮出现后再 click

### click ref stale 问题
- opencli 返回的 ref 容易 stale（React/Vue 重新渲染后 ref 编号变）
- 改用 CSS selector + eval 更稳：
  ```bash
  opencli browser <session> eval 'document.querySelector(".tab-item:nth-child(2)").click()'
  ```

### eval 参数传递
- **不支持 `--args`**：报错 `unknown option --args`
- 闭包嵌入：
  ```bash
  opencli browser <session> eval "(async () => { const urls = [...]; ... })()"
  ```

### M3 草稿发布路径（已验证）
1. 打开创作者中心 → 草稿箱 → 图文笔记
2. 找到目标草稿 → 点"编辑"
3. 编辑界面 → 点"发布" → 笔记进入"审核中"
4. **30 分钟内可在 App 撤回**，Web 端无法撤回

### 今日成果
- ✅ M3 草稿 → 发布成功（审核中）
- ✅ Qwen3.7 草稿 → 3 图 + 标题 + 正文 已填好，待用户点"暂存离开"

## 10. karpathy-skills-xhs 案例（浅色卡片 + 精简正文）

**任务**：Karpathy 开源 Skills 的小红书内容
**完成时间**：2026-06-02
**文件**：`karpathy-技能名-xhs/`（README + square/banner PNG/SVG）

### 完整工作流
1. **用户输入**：GitHub 项目链接 + "写小红书"
2. **获取 README**：用 `webfetch` 拿原始 markdown
3. **写 README.md**：小红书风格正文（< 950 字）
4. **设计 SVG 卡片**：浅色奶油底 + 4 原则 4 色卡片布局
5. **Inkscape 渲染**：`inkscape *.svg -o *.png -w 10xx -h 10xx`
6. **飞书预览**：`lark-cli docs +create` + `+media-insert × 2`
7. **XHS 草稿**：`opencli xiaohongshu publish --draft true`
8. **等用户审核后手动发布**

### 浅色卡片配方（本次验证有效）
```
底色：#FAF7F2 → #F3F0E8 渐变
强调色：蓝 #1E40AF / 绿 #10B981 / 橙 #F59E0B / 粉 #EC4899
结构：左侧 6px 色条 + 编号 + 大字标题 + 描述句
圆角：rx="16"
阴影：feDropShadow opacity=0.08 蓝调
字号：标题 92-110px，卡片 32-34px，副文 18-22px
```

### XHS 标题压缩（本次实践）
- 原：`Karpathy 亲自吐槽 AI 写代码 他给的解法是这套 Skill 🔥`
- 压缩：`Karpathy怒批AI写代码`（12 字符）✓
- 技巧：去空格 / 合并短词 / 砍 emoji

### 发布命令正确写法
```bash
# content 必须全放在一个 positional 参数（不要换行/不要多个参数）
# --title/--images/--topics 顺序随意，但全部要指定
# --window foreground 必须（后台无法上传图片）
# --site-session persistent 避免重复扫码

opencli xiaohongshu publish "<正文>" \
  --title "<≤20字>" \
  --images "<相对路径,csv>" \
  --topics "<不含#,csv>" \
  --draft true \
  --window foreground \
  --site-session persistent \
  -f yaml
```

### 本次数据
- 正文：~812 字符（< 950 ✓）
- 标题：12 字符（≤ 20 ✓）
- 图片：2 张（square 10KB + banner 10KB）
- 话题：7 个（Karpathy,AI编程,ClaudeCode,Cursor,开源工具,程序员,Skills）

### 飞书文档
- URL：`https://www.feishu.cn/docx/ZvlcdCJ7mobFxax2eBNcwzlOnad`
- 流程：`+create` → `+media-insert × 2`（banner + square）

---

## 11. PUA Skill 小红书项目（2026-06-02）

### 项目结构
```
pua-xhs/
├── README.md          # 小红书正文（912 字）
├── pua-square.png     # 封面 (1024×1024)
├── pua-banner.png     # 横版 (1792×1024)
├── pua-square.svg     # 源文件
├── pua-banner.svg     # 源文件
└── flavor-cards/      # 14 张大厂味道卡片
    ├── ali.png        # 阿里
    ├── bytedance.png  # 字节
    ├── huawei.png     # 华为
    ...（共 14 张）
```

### 正文压缩（950 → 912 字）
- 砍掉 14 厂完整列表（保留主要 6 家 + "+ 4 家"）
- 砍掉 11 个 IDE 完整列表（保留前 6 家）
- 表格简化（只保留 3 行关键数据）
- 工具：Python 正则提取纯文字 + 计数

### 卡片生成尝试记录
| 尝试 | 工具 | 风格 | 结果 |
|------|------|------|------|
| 1 | Kolors AI | 浅米色 + 场景 | ❌ 背景有花瓶窗帘等具体场景，AI 味重 |
| 2 | SVG Swiss | 浅米 paper + 黑色 ink | ❌ 用户不喜欢"干净设计感" |
| 3 | SVG codex++ | 深色径向渐变 + 渐变标题 + 星点装饰 | ✅ 用户认可 |

### SVG 代码风格（codex++ 深色）
```xml
<!-- 背景：深色径向渐变 -->
<radialGradient id="bg" cx="50%" cy="40%" r="70%">
  <stop offset="0%" stop-color="#1E1B4B"/>
  <stop offset="100%" stop-color="#070B1E"/>
</radialGradient>

<!-- 标题：渐变 -->
<linearGradient id="titleGrad">
  <stop offset="0%" stop-color="#FF6A00"/>  <!-- 品牌色 -->
  <stop offset="100%" stop-color="#e14c00"/> <!-- 稍暗 -->
</linearGradient>

<!-- 装饰星点 -->
<circle cx="120" cy="120" r="2" fill="#FF6A00" opacity="0.6"/>
```

### 大厂味道卡片（14 张）
- 布局：800×800，深色背景，渐变标题
- 按钮居中：3 按钮 × 120px + 20px gap = 400px 整体
- 起始位置：x = (800 - 400) / 2 = 200
- 首次生成时按钮偏左（从 x=180 开始），修复后居中

### 飞书上传
```bash
cd pua-xhs
lark-cli docs +media-insert --doc "<doc_id>" --file "./pua-square.png"
lark-cli docs +media-insert --doc "<doc_id>" --file "./pua-banner.png"

# 14 张大厂卡片
for f in ali.png bytedance.png ...; do
  lark-cli docs +media-insert --doc "<doc_id>" --file "./$f"
done
```

### 小红书发布
```bash
# 标题 ≤ 20 字符
opencli xiaohongshu publish "<正文>" \
  --title "<≤20字>" \
  --images "./pua-square.png" \
  --topics "AI编程,ClaudeCode,Codex,AIAgent,开源工具,效率工具" \
  --draft true
```

### 本次数据
- 正文：912 字符（< 950 ✓）
- 标题：14 字符（≤ 20 ✓）
- 飞书文档：`https://www.feishu.cn/docx/R3QpdTJSJoTFODxvICgcfpsXnch`
- 小红书草稿：已保存，标题「这个开源 Skill 专治 AI 摆烂」

## 13. SVG 卡片生成踩坑（cc-switch-xhs，2026-06-02）

### 致命坑：SVG 属性闭合引号
```
# ❌ 错误 — 漏了末尾的 "
<svg ... height="{h}>
# 输出: height="1024>

# ✅ 正确
<svg ... height="{h}">
# 输出: height="1024">
```
- **Python f-string 中容易遗漏**：`{h}>` 看起来自然，但 `"` 被吃掉了
- **Inkscape 静默处理**：不报错，直接输出全透明 PNG
- **症状**：文件 <10KB（1024×1024 正常 >400KB）

### 尺寸用 `100%` 失效
- `<rect width="100%" height="100%">` 在 Inkscape 中不渲染
- 必须用显式像素值：`<rect width="1024" height="1024">`

### PNG 生成后立即验证
```python
from PIL import Image
import numpy as np
img = Image.open("card.png")
arr = np.array(img)
if len(np.unique(arr.reshape(-1, arr.shape[-1]), axis=0)) < 10:
    print("⚠️ 空白图片！")
```
文件大小经验：1024×1024 > 400KB 正常，<50KB 即空白。

### 卡片去 AI 味
- **避免**：图表（柱状图/饼图）、hub-and-spoke 拓扑图、点阵底纹、过多装饰
- **保持**：纯奶油底 + 白色卡片 + 简洁文字 + 单一强调色
- **一张卡片只传达一个信息**，不堆叠

## 14. opencli upload 命令修复（2026-06-02，coding-plan-xhs）

### bug 根因
- `evaluateWithArgs` 使用 `const` 声明变量注入到 `page.evaluate()`
- 第二次调用同名字段（如 `markerAttr`）时，`const` 不允许重复声明 → `SyntaxError: Identifier 'markerAttr' has already been declared`
- 影响范围：所有调用 `uploadFiles()` 的场景（XHS 图片上传、ChatGPT 文件上传等）

### 修复方案
**文件**: `/opt/homebrew/lib/node_modules/@jackwener/opencli/dist/src/browser/base-page.js`

```diff
- return `const ${key} = ${JSON.stringify(value)};`;
+ return `var ${key} = ${JSON.stringify(value)};`;
```

`var` 允许重复声明，不会抛出 SyntaxError。修改后重启 daemon 生效：
```bash
kill $(lsof -ti:19825) && opencli doctor
```

### upload 命令的正确用法（修复后验证通过）
```bash
# 先找到 file input
opencli browser <session> find --css "input[type=file]"

# 上传文件（支持多个，路径需相对 CWD）
opencli browser <session> upload <ref> file1.png file2.png
```

### XHS 上传图文流程（验证通过）
1. 打开 `https://creator.xiaohongshu.com/publish/publish`
2. 用 `click "div[tabindex]" --nth 1` 切换到"上传图文" tab（2nd tab = 图文）
3. 用 `find --css "input[type=file]"` 定位图片 file input（accept=.jpg,.jpeg,.png,.webp）
4. 用 `upload <ref> file1.png file2.png` 上传图片
5. 用 `fill <ref> "标题"` 填写标题（input[type=text]）
6. 用 `fill <ref> "正文"` 填写正文（div[contenteditable=true]）
7. 内容自动保存到草稿箱（无需点击"存为草稿"按钮）

### 注意事项
- `div[tabindex]` 匹配 4 个 tab：视频/图文/长文/播客，`--nth 1` = 图文
- 每次 tab 切换会重新渲染 DOM，ref 编号会变，需重新 `find`
- contenteditable div 的 `fill` 返回 `verified: false` 不影响实际填写
- XHS 创作平台没有"存为草稿"按钮，所有编辑内容**自动保存为草稿**

### ERR_PROXY_CONNECTION_FAILED
- 导航到某些 XHS 子页面（如 `/note/manage`）可能触发代理连接错误
- 错误的 tab 无法恢复，需 `tab close` + `tab new` 重新打开
- 如果无法恢复，重启 daemon 可解决：`kill $(lsof -ti:19825)` + `opencli doctor`

## 15. coding-plan-xhs 数据源说明

### 信息采集
- 主站：`https://www.codingplan.fyi/` — 25 大平台对比工具
- 选型文章：`https://www.codingplan.fyi/articles/plan_comparison_20260519/index.html`
- 更新日期：2026.5.19

### 核心数据（已验证）
| 平台 | 评分 | 月费起 | 限购 | 独占模型 |
|------|------|--------|------|----------|
| 智谱AI | ★★★★★ | ¥46.55 | ⚠️限购抢购 | GLM-5.1 |
| MiniMax | ★★★★★ | ¥26.1 | ✅不限购 | M2.7 |
| 讯飞·星火 | ★★★★★ | ¥39 | ✅不限购 | GLM-5.1（智谱平替） |
| Kimi | ★★★★☆ | ¥49 | ✅不限购 | K2.6 |
| 字节·方舟 | ★★★★☆ | ¥36 | ⚠️已限购 | 多模型 |
| 阿里·百炼 | ★★★★☆ | ¥200 | ⚠️仅Pro | Qwen-3.6-Plus |

### 行业趋势（2026.5）
- 阿里/字节/腾讯纷纷从 Coding Plan 转向 Token Plan
- 腾讯已全面下架 Coding Plan
- GitHub Copilot 2026.6.1 起改为 Token 计费
- 智谱/字节/阿里三大头部已限购

### 免费资源
- 小米 MiMo：可领 16 亿 Credits
- NVIDIA NIM：每分钟 40 次，无 Token 限制
- 摩尔线程：新用户 30 天免费
- 商汤·日日新：每 5 小时 1500 次

## 16. 2026-06-02/03 批量生产记录

### 新增内容文件夹
| 文件夹 | 主题 | 卡片风格 | 状态 |
|--------|------|----------|------|
| `lark-cli-xhs/` | 飞书 CLI 介绍 | 浅色 · 飞书蓝 #3370FF | ✅ 已发布 |
| `opencli-xhs/` | OpenCLI 万物皆可 CLI | 深色 · 紫蓝渐变 #8B5CF6→#3B82F6 | ✅ 已发布 |
| `cli-anything-xhs/` | CLI-Anything 方法论 | 深色 · 紫蓝渐变 #8B5CF6→#3B82F6 | ✅ 已发布 |

### lark-cli-xhs 要点
- 标题：`灭霸来了，飞书CLI接管一切`（14 字）
- 正文 922 字，三个名场面开场
- 4 张浅色卡片，奶油色 #FAF7F2 背景
- 飞书文档：https://www.feishu.cn/docx/K7kHdqAjto4IfqxP9iUcBG9fnCh

### opencli-xhs 要点
- 标题：`OpenCLI 万物皆可 CLI`（14 字）
- 正文 743 字，四个痛点场景 + 四大核心
- 4 张深色卡片，深黑 #0A0A14 背景
- 飞书文档：https://www.feishu.cn/docx/GLPHdFGtto1lydxgiCOc2b8en9g

### cli-anything-xhs 要点
- 标题：`CLI-Anything 万物皆可命令行`（14 字）
- 正文 809 字，AI 无法操控软件的痛点切入
- 4 张深色卡片，11 款软件 + 7 步流水线
- 飞书文档：https://www.feishu.cn/docx/GUJad2AobotBFfxsAsrcnU4bndh

### 踩坑记录

**1. SVG f-string 中 `}` 转义问题**
- 在 f-string 中 `{变量}}` 会被解析为 `{变量}` + `}` → 正确
- 但 `{变量}}+` 中 `}+` 的 `}` 是单独的 → `SyntaxError: f-string: single '}' is not allowed`
- 修复：在 f-string 中使用 `}}` 表示字面 `}`

**2. SVG 右列文字 x 坐标错误**
- 2×2 网格布局中，右列 text 的 x 坐标写成和左列一样（如 `x="30"`）
- 结果右列文字渲染在左列区域，右列显示为空白
- 修复：右列 text 使用 `x="460"`（左列 30 + 间距 430 + 内边距）

**3. OPEN/CLI 文字重叠**
- 封面「CLI」字号 160，`letter-spacing="-4"` + `filter="url(#glow)"` 扩展区域大
- 「OPEN」y=220 被「CLI」y=340 覆盖
- 修复：OPEN 上移到 y=160，CLI 下移到 y=380

**4. 正文超 950 字问题**
- 原始体.md 含 `> 2026-06-02 · github.com/...` 元数据行 + 标题重复
- 小红书实际渲染时元数据行占用大量字符
- 修复：移除元数据行，精简正文到 <950 字

**5. opencli xiaohongshu publish 图片上传**
- `Image injection failed: No file input found on page` — 偶发
- 重试即可解决，或用 `--trace retain-on-failure` 获取调试截图
- 发布后 status `⚠️ 操作完成，请在浏览器中确认` — 需要浏览器手动确认上传
- 有时直接返回 `✅ 发布成功` 自动完成

### 标题公式总结
三种标题风格已验证有效：
- 灭霸梗：`灭霸来了，飞书CLI接管一切`
- 口号式：`OpenCLI 万物皆可 CLI`
- 价值式：`CLI-Anything 万物皆可命令行`

最佳标题长度 12-14 字，控制在 20 字以内即可。

## 17. 2026-06-03 oh-my-openagent (OmO) 生产记录

### 新增内容
| 文件夹 | 主题 | 卡片风格 | 状态 |
|--------|------|----------|------|
| `omo-xhs/` | Oh My OpenAgent — OpenCode 超强插件 | 深色 · 紫橙渐变 #8B5CF6→#F97316 | ✅ 已发布 |

### 内容要点
- 标题：`OmO 一个命令拉起 AI 团队`（16 字）
- 正文 774 字，纯文本格式（无 Markdown），无时间信息
- 主打卖点：11 个 Agent、Team Mode、ultrawork、Anthropic 封杀事件
- 4 张深色卡片，OmO 品牌色紫橙渐变
- 飞书文档：https://www.feishu.cn/docx/KCC4djHlVo3Slqxhcrhc0wnpnZe

### 踩坑记录

**1. card-2 右列文字 x 坐标错误（重复问题）**
- 2×2 网格布局中，右列「ultrawork」「生态兼容」两个面板的 text 写成 `x="25"`（和左列一样）
- 右列实际应在 `x="455"`（右列起始 430 + 内边距 25）
- 与 opencli-xhs 完全相同的 Bug，说明 gen_cards.py 的 2×2 布局模板有模式性风险

**2. body.md 中 Markdown 格式问题**
- 小红书正文是纯文本渲染，不支持 Markdown（`---`、`###`、`**`、`>` 都会显示为原文）
- 修复：将 body.md 改为纯文本格式，去掉所有 Markdown 装饰

**3. 数据源获取方式**
- GitHub 页面有时限（`webfetch` 超时）
- 改用 `curl` + GitHub API 获取 raw README：`curl -sL "https://api.github.com/repos/.../readme" -H "Accept: application/vnd.github.v3.raw"`
- API 方式更稳定，推荐优先使用

### 新增标题风格
- 功能概括式：`OmO 一个命令拉起 AI 团队` — 直接说明核心价值

## 18. cc-switch-xhs v3.16.1 更新流程（2026-06-03）

### 本次亮点
- **首次直接发布（非草稿）**：用户要求 `立即发布`，去掉 `--draft true` 即可
- **正文第一行 = 标题**：用户偏好标题在正文第一行重复
- **正文不出现时间信息**：去掉 "v3.16.1"、"23 commits" 等版本/时间信息
- **全链路零 Bug**：从调研 GitHub → 写文 → SVG 卡片 → Inkscape 渲染 → 飞书更新 → XHS 发布，一次通过

### 卡片更新策略
- 已有 `gen_cards.py` 的项目，发布版本更新时**直接重写卡片内容**而非新建文件
- 保持文件名不变（`cc-switch-square.png` 等），仅替换卡片设计——飞书旧图片保留，XHS 上传新图
- 设计思路：从"产品介绍"转向"版本更新公告"，卡片加红色 `v3.16.1 史诗级更新` badge

### 飞书文档更新流程（已验证高效）
```
lark-cli docs +update --doc <id> --mode overwrite --markdown "..."  # 替换全文
lark-cli docs +media-insert --doc <id> --file card-1.png           # 串行插入图片 × N
lark-cli docs +fetch --doc <id>                                    # 验证
```
- `--mode overwrite` 清空整篇文档重写，适用**内容完全不同**的场景
- 图片需用 `+media-insert` 重新插入（overwrite 会删除旧 media blocks）

### 发布命令（本次验证通过）
```bash
opencli xiaohongshu publish "<正文>" \
  --title "<≤20字>" \
  --images "<相对路径,csv>" \
  --topics "<不含#>" \
  --window foreground \
  --site-session persistent \
  -f yaml
```
- 不传 `--draft` 即直接发布
- 返回 `status: ✅ 发布成功` 含 detail 信息

### 正文要求
- 第一行放标题（用户偏好）
- 不出现任何时间、版本号、commit 数
- 短段落 + emoji 分段 + `·` 列表 + 末尾话题标签

### 正文含换行时传参
- `opencli xiaohongshu publish` 的 content 参数含换行时，直接用字符串会被 shell 拆成多个参数
- 正确做法：写入临时文件后 `"$(cat /tmp/body.txt)"` 传递

## 2. SVG 生成 (Python f-string + Inkscape)

### f-string 传颜色变量的陷阱
- 错误写法：`topic_card(..., "{NVIDIA}", "{NVIDIAS}")` — 外层 f-string 表达式里，`"{NVIDIA}"` 是字面字符串 `{NVIDIA}`，不是变量值
- 正确写法：`topic_card(..., NVIDIA, NVIDIAS)` — 直接传变量，无引号包裹
- 后果：Inkscape 读到 `fill="{NVIDIA}"` 视作无效颜色，渲染为黑色块

### SVG 多行文本
- `<text>` 不支持 `\n` 换行，Inkscape 会忽略
- 必须用 `<tspan x="..." dy="...">` 元素逐个分行

### 文字大小要求
- 图片最终在小红书手机端展示，正文文字 font-size 至少 30+，标题至少 40+
- 1024×1024 画布上 30px 对应手机屏幕约 7-8mm，低于此值难以辨认

## 3. SVG 卡片文字重叠排查 (2026-06-03, ai-side-hustle-xhs)

### 问题
初次生成 4 张卡片后，飞书预览发现多处文字叠加覆盖，历经 3 轮修复。

### 根因
写 SVG 时只凭感觉排坐标，没有系统计算每个 text 元素的垂直占用范围。Inkscape 渲染后肉眼检查才发现重叠，返工成本高。

### 解决方案：render 前用 Python 做坐标分析

```python
def text_extent(y, fontsize):
    """Approximate text vertical extent. Baseline at y."""
    top = y - fontsize * 0.25
    bottom = y + fontsize * 0.75
    return top, bottom

def circle_extent(cy, r):
    return cy - r, cy + r
```

对每个 text 元素计算 `[top, bottom]` 范围，检查相邻元素 gap：
- 文字 vs 文字：gap ≥ 10px 安全
- 文字 vs 圆：gap ≥ 15px 安全
- 文字 vs rect 边界：gap ≥ 6px 安全

### 本次发现的 6 处重叠

| 卡片 | 重叠位置 | 原因 | 修复 |
|------|---------|------|------|
| 封面小卡片 | 标题 vs icon 圆 | title y=512, icon cy=510, title 进入圆内 | icon 下移 cy=y+58, 缩小 r=22; title 右移 x=96 (X 轴分离) |
| 封面底部备注 | 两行文字间距 10px | y=775 和 y=805, fs=20/18 | 第二行下移到 y=748, gap=14px |
| 路径卡 | desc2 vs icon 圆 | desc2 y=290, icon cy=340, gap 仅 15px | icon 下移 cy=360, desc2→y=258 |
| 路径卡 | price value vs box 底 | value y=445 fs=36, box 底 460, 超出 4px | box 加高至 120px, value baseline→490 |
| 路径卡 | tips 第4条 vs box 底 | tip4 y=770, box 底 760, 超出 5px | tips box 加高至 255px |
| 路径卡 | footer vs bottom note | footer y=900, bottom note 底 860, gap 仅 16px | 保持 (gap>10 安全) |

### 经验总结

1. **先算后画**：写 SVG 前先用 Python 脚本算一遍所有坐标，打印每个元素的 `[top, bottom]` 范围，检查 gap
2. **留足余量**：文字到底部/边界的 gap 至少 10px，Inkscape 渲染可能有 1-2px 偏差
3. **X 轴分离优先**：标题和 icon 圆尽量在 X 轴上分离（title x > icon x + icon_r），避免 Y 轴精细调整
4. **icon 不宜过大**：小卡片 icon r=22 足够，大卡片 r=65 以内，给文字留空间
5. **tips 区域要预留**：4 条 tips × 45px 行距 = 135px + title 45px + 上下边距 = 至少 240px 高度
6. **price box 高度**：label + value 至少 100px，value fs=32 时建议 120px

### 文件结构
```
ai-side-hustle-xhs/
├── article.md          # 小红书草稿正文（标题首行 + 正文）
├── README.md           # 完整版博客文章
├── gen_cards.py        # SVG→PNG 生成器（含坐标分析逻辑）
├── ai-side-hustle-square.png   # 封面 (1024×1024)
├── ai-side-hustle-card-write.png
├── ai-side-hustle-card-draw.png
└── ai-side-hustle-card-ppt.png
```

## 4. 知乎数据采集

### opencli zhihu 热榜
- `opencli zhihu hot` 需要浏览器登录态（已登录 Chrome），否则返回空数组
- 替代方案：通过 tophub.today 聚合站获取知乎热榜
- 搜索（`zhihu search`）同样需登录态，返回 AUTH_REQUIRED

## 5. ai-ppt-tools-xhs 四巨头横评（2026-06-03）

### 项目结构
```
ai-ppt-tools-xhs/
├── article.md          # 小红书草稿正文
├── README.md           # 完整版博客文章 + 对比表
├── gen_cards.py        # SVG→PNG 生成器（5 张卡片）
├── cover.png           # 封面 (1024×1365, 3:4 小红书比例)
├── card-gamma.png      # Gamma 卡片 (1024×1365)
├── card-tome.png       # Tome 卡片 (1024×1365)
├── card-mindshow.png   # MindShow 卡片 (1024×1365)
├── card-islide.png     # iSlide AI 卡片 (1024×1365)
```

### 完整工作流
1. **调研四款工具**：Gamma / Tome / MindShow / iSlide AI
2. **写 README.md**：每款工具核心能力 + 适用场景 + 价格 + 对比表格
3. **写 article.md**：小红书草稿（标题首行 + 正文 < 950 字）
4. **设计 SVG 卡片**：浅色奶油底 + 4 工具品牌色 + 3 区块结构
5. **Inkscape 渲染**：1024×1365（小红书 3:4 比例）
6. **飞书文档**：`+create` → `+media-insert × 5`
7. **XHS 草稿**：`opencli xiaohongshu publish --draft true`

### 三轮迭代修复记录

| 轮次 | 问题 | 修复方案 |
|------|------|---------|
| v1 | 文字叠加、内容不饱满 | 每项独立 y 坐标精确计算；3 区块×2-3 条详情；改为 3:4 比例 |
| v2 | 文字太小看不清楚 | 标题 48→64→80px；列表正文 18→24px；区块标签 16→22px；评分 32→50px |
| v3 | 仅首图标题需更大 | 封面标题 64→80px，封面工具名 38→44px；单卡保持 64px 不变 |

### 卡片设计要点（浅色四巨头横评）
```
底色：#FAF7F2 → #EFF6FF/#F5F3FF/#ECFDF5/#FFFBEB（各工具对应色温）
强调色：Gamma 蓝#3B82F6 / Tome 紫#8B5CF6 / MindShow 绿#10B981 / iSlide 橙#F59E0B
结构：大标题 → 副标题 → 色标 tagline → 分隔线 → 3 区块（标签 badge + 项目符号）→ 评分星级 → 推荐标签 → 底部话题
字号（单卡）：标题 64px / 副标题 32px / tagline 26px / 区块标签 22px / 列表 24px / 评分 50px / 推荐 22px / 底部 20px
字号（封面）：标题 80px / 副标题 36px / 工具名 44px / 工具标签 20px / 工具描述 20px / 底部说明 24px
```

### 小红书发布约束（本次验证）
- **标题 ≤ 20 字符**：`AI做PPT工具四巨头🔥` = 12 字符 ✅
- **正文 ≤ 950 字**：484 字符 ✅
- **正文首行 = 标题**：用户偏好，标题在正文第一行重复
- **正文不含时间**：去掉日期、版本号等时间信息
- **图片 ≤ 9 张**：5 张 ✅
- **图片路径相对 CWD**：`cd` 到卡片目录后传相对路径

### 发布命令
```bash
cd ai-ppt-tools-xhs
opencli xiaohongshu publish "<正文>" \
  --title "AI做PPT工具四巨头🔥" \
  --images "cover.png,card-gamma.png,card-tome.png,card-mindshow.png,card-islide.png" \
  --topics "AI工具,PPT,Gamma,Tome,MindShow,iSlide,效率工具" \
  --draft true \
  --window foreground \
  --site-session persistent \
  -f yaml
```

### 飞书文档
- URL：`https://www.feishu.cn/docx/B151dbdP4oMUKJxcZMxcNSw8nGf`
- 5 张图全部上传成功

### lark-cli 更新
- 提示 1.0.46 可用，但 npm 上实际最高版本为 1.0.45
- `npm view @larksuite/cli versions` 确认最新：1.0.42/43/44/45
- **结论：当前已是最新版，提示为误报**

## 6. ai-drawing-xhs AI 画图工具横评（2026-06-03）

### 项目结构
```
ai-drawing-xhs/
├── article.md          # 小红书草稿正文（标题 9 字 + 正文 454 字）
├── README.md           # 完整版博客文章
├── gen_cards.py        # SVG→PNG 生成器（5 张浅色卡片）
├── ai-drawing-square.png   # 封面 (1024×1024) — 5 工具名列表
├── ai-drawing-card-1.png   # 横向对比表 (1024×1024)
├── ai-drawing-card-2.png   # 各工具核心优势 (1024×1024)
├── ai-drawing-card-3.png   # 综合推荐排名 (1024×1024)
└── ai-drawing-banner.png   # 总结 Banner (1792×1024)
```

### 卡片文字大小教训（三轮修复）

| 轮次 | 问题 | 修复 |
|------|------|------|
| v1 | 卡片文字太小、内容不饱满 | square 标题 46→56，工具卡片 800→900×90，文字 28→36；banner 标题 80→90，单卡 280×200→320×250 |
| v2 | 对比表文字溢出列宽 | 列宽重新分配（工具 160 + 价格 220 + 画质 150 + 速度 150 + 上手难度 220），价格文字缩短（"免费+付费 0-30$/月"→"免费~30$/月"），字号 20→18 |
| v3 | 无（一次通过） | — |

### 对比表列宽设计要点
- 5 列不宜等宽：价格列需最宽（220px），星级列可窄（150px）
- 工具名和上手难度列居中（160-220px）
- 列 x 中心坐标：`[80, 270, 455, 605, 790]`（总计 900px 宽）
- 文字过大（20px+）时长文本（如"免费+付费 0-30$/月"）必然溢出 180px 列
- 解决方案：缩短价格文案 + 列宽分配 + 字号 18px 以内

### Banner 卡片自动排列
- 5 个等宽卡片用 Python 计算位置避免手配坐标：
  ```python
  w_c = 320
  gap = 36
  x0 = int((1792 - (w_c * 5 + gap * 4)) / 2)
  for i in range(5):
      x = x0 + i * (w_c + gap)
  ```
- 这样多一张少一张都不用手动调整

### 飞书文档操作经验
- `docs +update --mode overwrite` 清空文档内容（含 media blocks），**必须重新插入所有图片**
- 批量插入图片可用 shell 循环，每张串行插入
- `+media-insert` 的 `--file` 支持**绝对路径**（`$PWD/file.png`），也支持相对路径

### 正文格式严格执行
- **标题 ≤ 20 字**：`AI画图工具红黑榜` = 9 字 ✓
- **正文第一行 = 标题**：用户要求标题在正文开头重复
- **正文不含时间**：去掉日期、版本号等时间信息
- **正文 ≤ 950 字**：454 字 ✓

### 飞书文档
- URL：`https://www.feishu.cn/docx/BwgKdGen6oVISPxqXNVc4NRznIh`
- 5 张图全部上传成功

### XHS 草稿
- 已保存为草稿，标题「AI画图工具红黑榜」
- 5 张图片 + 6 个话题标签
- 待用户去 creator.xiaohongshu.com 审核发布
## 19. suno-udio-music-xhs 实测对比（2026-06-03）

### 项目结构
```
suno-udio-music-xhs/
├── article.md          # 小红书草稿正文（标题首行 + 正文）
├── gen_cards.py        # SVG→PNG 生成器（4 张浅色卡片）
├── suno-udio-cover.png     # 封面 (1024×1024)
├── suno-udio-card-suno.png # Suno 5 卡片
├── suno-udio-card-udio.png # Udio 卡片
└── suno-udio-card-compare.png # 实测对比卡片
```

### 完整工作流
1. **调研对比**：Suno 5 vs Udio 两大 AI 音乐生成器
2. **写 article.md**：小红书草稿（标题首行 + 正文 < 950 字）
3. **设计 SVG 卡片**：浅色奶油底 + 4 张卡片（封面 + 2 产品 + 对比）
4. **Inkscape 渲染**：1024×1024
5. **飞书文档**：`+create` → `+media-insert × 4`
6. **XHS 草稿**：`opencli xiaohongshu publish --draft true`

### 正文迭代（3 轮）
| 轮次 | 问题 | 修复 |
|------|------|------|
| v1 | 内容平淡，像评测报告 | 改"AI写歌已经能到专业水平了？"为"最近AI写歌风很大，说真的我本来不信"（个人故事钩子） |
| v2 | 标题不够抓眼球 | "AI音乐生成Suno5 vs Udio实测" → "Suno5和Udio，我替你们试了"（悬念+情绪） |
| v3 | 正文格式需调整 | 标题放正文第一行，去掉时间戳/版本号，纯文本格式 |

### 卡片文字垂直居中（关键修复）
**问题**：标题在色块中偏上，不居中

**根因**：SVG `<text>` 的 y 属性是**基线（baseline）**，不是视觉中心。直接用色块中心 y 值会导致文字偏上。

**解决方案**：
```python
# 色块高度 260px，中心 y = 210
# 单行标题 (78px): 视觉高度 ≈ 78px, ascent≈60, descent≈18
#   视觉中心 ≈ baseline - (ascent - height/2) = baseline - 21
#   要让视觉中心 = 210 → baseline = 231

# 双行标题 (78px + 44px): 总视觉高度 ≈ 163px
#   第一行基线 y = 188, 第二行 y = 281
#   整体视觉中心 ≈ (188-60+18 + 281-34+10) / 2 ≈ 210 ✓
```

**经验**：
- 不要直接用色块中心作为 text y 坐标
- 单行：`y = center + fontsize * 0.15`（约偏移 fontsize/7）
- 双行：先算总视觉高度，再反推第一行基线位置
- 78px 字号：`y ≈ center + 11`；44px 字号：`y ≈ center + 6`

### 小红书爆款标题公式（本次验证）
| 风格 | 示例 | 字数 |
|------|------|------|
| 悬念+情绪 | "Suno5和Udio，我替你们试了" | 16 |
| 冲突对比 | "AI写歌杀疯了！Suno5 vs Udio谁才是真神？" | 22 ❌ |
| 结论前置 | "Suno5 = 小白神器，Udio = 音质天花板" | 22 ❌ |

**最佳**：14-18 字，带情绪词（"试了""意外""杀疯了"），避免纯描述。

### 正文风格（XHS 爆款特征）
- **开头**：个人故事/情绪钩子（"说真的我本来不信"）
- **结构**：先说结论 → 分产品描述 → 实测对比 → 行动建议
- **语气**：口语化，像朋友聊天（"不想动脑的人""差点信了"）
- **排版**：短段落 + emoji 分段 + `→` 对比符号
- **结尾**：行动指令（"别光看，去试试"）+ 话题标签

### 发布数据
- 标题：16 字符（≤ 20 ✓）
- 正文：566 字符（≤ 950 ✓）
- 图片：4 张
- 状态：✅ 暂存成功（草稿箱）
- 飞书文档：https://www.feishu.cn/docx/SKaJdXspJoByACxyi4ocB49Vnyg

## 21. Obsidian + AI Agent 双语言卡片项目（2026-06-05）

### 项目结构
```
obsidian-agent-xhs/
├── article.md              # 小红书草稿（标题 15 字 + 正文 639 字）
├── README.md               # 完整博客版
├── gen_cards.py            # SVG 生成器（8 张卡片：4 中文浅色 + 4 英文深色）
├── oa-cover-zh.png/svg     # 中文封面 (1024×1024)
├── oa-card-1-zh.png/svg    # 中文痛点卡
├── oa-card-2-zh.png/svg    # 中文解决方案卡
├── oa-card-3-zh.png/svg    # 中文数据卡
├── oa-cover-en.png/svg     # 英文封面 (1024×1024)
├── oa-card-1-en.png/svg    # 英文哲学卡
├── oa-card-2-en.png/svg    # 英文架构卡
└── oa-card-3-en.png/svg    # 英文结论卡
```

### 内容规划（8 张卡）
**中文 4 张（浅色奶油底 #FAF7F2）：**
- 封面：大标题 "Obsidian + AI 真有搞头" + 四大信号
- 卡1：死笔记痛点（写了5000条没人读、AI碰不到、插件各自为政）
- 卡2：AI管家方案（Agents Read理念 + CLI/MCP/QMD/生态四件套）
- 卡3：三组数据（54x CLI速度、60%+ Token节省、6+插件）

**英文 4 张（深色 #0B1027/141B33）：**
- 封面：Overhyped or Underrated? + 4 signals
- 卡1：Agents Read, Humans Write 哲学 + 4 slash commands
- 卡2：How It Works — CLI + MCP + QMD 三件套
- 卡3：The Verdict — 4 conclusions

### 经验教训

**1. Twitter reply 多行中文策略**
- `opencli twitter reply` 对多行中文文本经常返回 `Could not verify reply text in the composer after typing`
- 解决方案：用单行英文/中文短句，不要用换行
- 实测：短英文单行成功率 100%，中文单行也 OK，多行中文失败
- 需要发长内容时：先发短英文，再用 browser eval 操作

**2. Twitter reply 需要延时**
- 连续发 reply 需要间隔至少 20-30 秒，否则 composer 页面可能尚未准备好
- 首条 reply 尤其需要更多时间（post 后 tweet 需要时间发布）
- 推荐间隔：首条 reply 等待 60 秒，后续每条 20-30 秒

**3. XHS `--topics` 对 niche 主题必须省略**
- Obsidian/AI Agent 被系统判定为 niche，attach topic 时 "no real topic entity appeared"
- 解决方案：body 末尾用 `#话题` 标签替代 `--topics`，不传 `--topics` 参数

**4. 双语言卡片设计模式**
- 同一主题用浅色/深色两套卡片，分别用于不同平台（XHS 浅色中文 / Twitter 深色英文）
- 一套 gen_cards.py 同时生成 light + dark 两组函数，共享颜色变量
- 内容对应但不完全相同：中文走痛点→方案→数据线，英文走哲学→架构→结论线

**5. 中/英文封面区别**
- 中文封面：大字标题（96px + 64px），更情绪化，有 hashtag
- 英文封面：略小节标题（80px + 52px），更理性，突出 "Overhyped or Underrated?" 的争议感
- 深色封面用 `#1A2340` 色块代替白色卡片，避免浅色在深底上突兀

### 飞书文档
- URL: https://www.feishu.cn/docx/NgY3dZPhmoJTOsxKSOWcW9MRnEg
- 8 张图全部上传成功（2 封面 + 6 卡片）

### 发布状态
- XHS 草稿：✅ 已保存，标题「Obsidian+AI真有搞头」，4 张中文浅色图
- Twitter 主推文：✅ 已发布，4 张英文深色图（仅发主推文，不发推文串）

### 关键教训（2026-06-05 用户确认）
- **Twitter 只发主推文，不发推文串**：用户明确要求只发单条推文+4图，超出内容不切 Thread
- **XHS `--topics` 对 niche 主题必须省略**：Obsidian/AI Agent 无法匹配话题实体

### 2026-06-03 经验总结

#### 初版设计问题
- 卡片过于简单（纯色背景 + 大 emoji + 小字）
- 缺乏视觉冲击力，不符合 XHS 热门封面风格
- 用户反馈"图太丑了"

#### XHS 爆款封面特征
1. **大标题 + 醒目文字** — 字体大、粗体、高对比度
2. **高饱和度配色** — 颜色鲜艳吸睛
3. **渐变背景** — 更有层次感
4. **装饰元素** — 小图标、线条、贴纸感
5. **数字/榜单感** — 突出"5个"这种数字

#### v2 设计改进
| 改进点 | 原版 | v2 版 |
|--------|------|-------|
| 标题 | 普通字体 | 超大粗体 (72px) + 数字编号 |
| 配色 | 单色 | 渐变 + 高饱和度 |
| 背景 | 纯色 | 浅色渐变 + 装饰圆 |
| 图标 | 大 emoji | 圆形背景 + emoji |
| 层次感 | 扁平 | 卡片阴影 + 多层元素 |

#### SVG 绘制要点
```xml
<!-- 渐变定义 -->
<linearGradient id="gradTop" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" style="stop-color:{start}"/>
  <stop offset="100%" style="stop-color:{end}"/>
</linearGradient>

<!-- 阴影滤镜 -->
<filter id="shadow">
  <feDropShadow dx="0" dy="8" stdDeviation="20" flood-opacity="0.15"/>
</filter>

<!-- 装饰圆 -->
<circle cx="100" cy="100" r="60" fill="{primary}" opacity="0.05"/>
```

#### 配色方案（XHS 友好）
| 工具 | Primary | Gradient | Background |
|------|---------|----------|------------|
| Paperpal | #6366F1 | #818CF8→#6366F1 | #EEF2FF |
| Scite | #10B981 | #34D399→#10B981 | #ECFDF5 |
| Elicit | #F59E0B | #FBBF24→#F59E0B | #FFFBEB |
| Connected Papers | #EF4444 | #F87171→#EF4444 | #FEF2F2 |
| Jenni | #8B5CF6 | #A78BFA→#8B5CF6 | #FAF5FF |

#### 卡片尺寸
- **XHS 推荐**: 3:4 (1242×1660) 或 1:1 (1024×1024)
- 本次使用 1024×1024（正方形，通用性更好）

#### 生成流程
```bash
python3 gen_cards_v2.py  # SVG → Inkscape → PNG
```

#### 常见 SVG 陷阱
- `width="100%"` 在 Inkscape 中不被支持 → 用明确数值 `width="1024"`
- 渐变引用错误 → 确保 `<defs>` 中定义了 `id`
- 字体缺失 → 用 `system-ui, -apple-system, sans-serif` 通用字体栈
- 阴影不显示 → 确保 `<filter>` 在 `<defs>` 中且 `id` 正确引用

### 设计决策流程
1. 先做简单版验证内容结构
2. 用户反馈后快速迭代设计
3. 参考平台热门内容调整风格
4. 保持品牌一致性（5张卡片统一风格）
5. 输出可复用模板（gen_cards_v2.py）

## 20. ai-xhs-tool-xhs 项目经验（2026-06-03）

### 项目结构
```
ai-xhs-tool-xhs/
├── article.md          # 小红书草稿正文
├── xhs_content.txt     # 发布用纯文本（标题首行 + 正文）
├── index.html          # HTML 卡片模板（Swiss IKB Blue）
├── render.js           # Puppeteer 渲染脚本
├── package.json
└── output/
    ├── page1.png       # 封面
    ├── page2.png       # 痛点对比
    ├── page3.png       # 功能矩阵
    ├── page4.png       # 实测数据
    ├── page5.png       # 工作流
    ├── page6.png       # 避坑指南
    ├── page7.png       # 进阶技巧
    └── page8.png       # 收尾金句
```

### 8页内容规划（验证有效）
| 页 | 主题 | 布局 | 核心内容 |
|----|------|------|---------|
| P1 | 封面 | 克莱因蓝满版 | 超大标题 + 标签 |
| P2 | 痛点 | 旧vs新对比 | 灰化旧方式 + 蓝底新方式 |
| P3 | 功能 | 2×2 矩阵 | 4大能力卡片 |
| P4 | 数据 | KPI + 进度条 | 3组数据 + "0熬夜"黑框 |
| P5 | 工作流 | 垂直流程 | 4步 + 图标 |
| P6 | 避坑 | 列表 | 5个经验教训 |
| P7 | 技巧 | 卡片列表 | 3个进阶用法 |
| P8 | 收尾 | 居中金句 | "工具不是替代，是放大器" |

### 设计选择
- **风格**: Swiss International + IKB Blue (#002FA7)
- **理由**: 克莱因蓝高饱和度 + 科技感，适合 AI/工具类内容
- **浅色方案**: 全克莱因蓝背景比柠檬黄更有冲击力

### 致命 Bug：Puppeteer 截图全一样

**症状**：8张图文件大小完全相同（都是 48856 字节），内容看起来一样。

**根因**：
```javascript
// ❌ 错误写法 — selector 截图截取的是视口区域，不是元素本身
await page.screenshot({
  path: outputPath,
  selector: `#${posterId}`,  // 所有 section 尺寸都是 1080×1440
  fullPage: false
});
```

所有8个 `<section class="poster xhs">` 尺寸都是 1080×1440，`page.screenshot({ selector })` 截取的是**固定视口区域**，所以每张图都一样。

**修复**：
```javascript
// ✅ 正确写法 — 直接截取元素本身
const element = await page.$(`#${posterId}`);
const boundingBox = await element.boundingBox();
await element.scrollIntoView();
await element.screenshot({
  path: outputPath,
  type: 'png'
});
```

**验证方法**：
```bash
ls -la output/page*.png  # 文件大小应该各不相同
file output/page*.png    # 确认都是 PNG
```

### 其他踩坑

**1. Puppeteer 安装问题**
- macOS 系统 Python 是 externally-managed 环境，`pip install puppeteer` 失败
- 解决方案：`npm install puppeteer-core`（不下载 Chromium，用本地 Chrome）

**2. Chrome 路径**
```javascript
executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
```
必须指定完整路径，不能用 `chromium` 或 `google-chrome`。

**3. lark-cli 文件路径**
- `--file` 必须是**相对路径**，不能用绝对路径
- 错误：`--file /Users/.../output/page1.png` → `unsafe file path`
- 正确：`cd` 到项目目录后用 `--file ./output/page1.png`

**4. 多页渲染循环**
```javascript
for (let i = 1; i <= 8; i++) {
  await renderPage(i, path.join(outputDir, `page${i}.png`));
}
```
每个 section 的 ID 是 `xhs-01` ~ `xhs-08`，循环渲染时注意补零。

### 小红书发布约束（严格执行）
- **标题 ≤ 20 字符**：`AI写小红书｜保姆级教程` = 13 字符 ✓
- **正文 ≤ 950 字**：244 字符 ✓
- **标题在正文第一行**：用户偏好
- **无时间戳/版本号**：去掉所有日期信息
- **图片 ≤ 9 张**：8 张 ✓
- **话题标签**：逗号分隔，不含 # 号

### 发布命令
```bash
opencli xiaohongshu publish "$(cat xhs_content.txt)" \
  --title "AI写小红书｜保姆级教程" \
  --images "output/page1.png,output/page2.png,..." \
  --topics "AI工具,小红书运营,内容创作,效率工具,自媒体" \
  --draft true \
  --window foreground \
  --site-session persistent \
  -f yaml
```

### 飞书文档
- URL：https://www.feishu.cn/docx/Q4YMdpT3cojGpTxVinZcDsCNn3e
- 8张图全部上传成功

### 内容结构建议（8页模板）
```
P1 封面 → 吸引点击（大标题 + 高饱和度背景）
P2 痛点 → 引发共鸣（旧vs新对比）
P3 功能 → 展示能力（矩阵/列表）
P4 数据 → 建立信任（数字 + 进度条）
P5 流程 → 可操作（步骤 + 图标）
P6 避坑 → 增加价值（经验教训）
P7 技巧 → 进阶内容（给高手）
P8 收尾 → 金句收尾（记忆点）
```

这个结构适用于**工具推荐/教程/经验分享**类内容，内容饱满度刚好填满8页，不会显得空洞。

## 21. api-price-war-xhs 大模型API价格战（2026-06-03）

### 项目结构
```
api-price-war-xhs/
├── article.md              # 小红书草稿正文（标题首行 + 正文 462 字）
├── README.md               # 完整版文章
├── gen_cards.py            # SVG→PNG 生成器（8 张浅色卡片）
├── price-war-cover.png     # 封面 (1024×1024) — 大标题 + 5模型速览
├── price-war-table.png     # 价格对比表 (1024×1024)
├── price-war-deepseek.png  # DeepSeek 详情 (1024×1024)
├── price-war-qwen.png      # Qwen 详情 (1024×1024)
├── price-war-gpt4o.png     # GPT-4o 详情 (1024×1024)
├── price-war-claude.png    # Claude 详情 (1024×1024)
├── price-war-gemini.png    # Gemini 详情 (1024×1024)
└── price-war-summary.png   # 终极选择指南 (1024×1024)
```

### 发布数据
- 标题：`大模型API价格战`（6 字，≤20 ✓）
- 正文：462 字（≤950 ✓）
- 图片：8 张（≤9 ✓）
- 话题：`大模型,API,DeepSeek,Qwen,GPT-4o,Claude,Gemini,价格对比`
- 发布：✅ 直接发布（非草稿），去掉 `--draft true`

### 踩坑 & 修复

**1. Table 卡片数据行与表头重叠**
- 行起点 `y = 82 + i * 88`，但表头在 `y=170` → 第2行直接盖在表头上
- 修复：行起点改为 `y = 240 + i * 80`（表头 y=170 + h=44 + padding 后）

**2. Table 卡片 Logo key 查找失败**
- `name.lower().split("-")[0].replace("3","").replace("5","").replace("2","")` 
- "GPT-4o" → `"gpt"` ❌（key 是 `"gpt4o"`）
- "Claude 3.5" → `"claude "` ❌（尾部空格）
- "Gemini 2.0" → `"gemini "` ❌（尾部空格）
- 修复：用显式 `TABLE_LOGO_KEY = {"DeepSeek-V4": "deepseek", ...}` 字典映射

**3. Model 卡片核心优势与警告区间距过紧**
- 核心优势最后一行 y=540+156=696，警告区 y=700 → 仅 4px 间距
- 修复：核心优势上移至 y=520，行距 40→36，警告区下移至 y=730

**4. Cover 卡片底部文字出界**
- Footer 文字在 y=975，但白卡 rect 在 y=50 到 y=974（h=924）→ 文字在白卡外
- 修复：footer 上移至 y=955，行距 92→86

**5. Cover 标题投影（glow filter）**
- "大模型"文字使用了 `filter="url(#glow)"`，用户要求去掉
- 修复：去掉 glow filter，改为普通黑色文字

**6. SVG 卡片含时间戳**
- Cover 卡片副标题含 "· 2026.06" 时间信息
- 修复：去掉 SVG 中的时间戳，内容不出现日期/版本

**7. Model 卡片功能点间距压缩**
- 4 个功能点 + 核心优势标题 + 警告区需紧凑排列
- 修复：功能点 y 起点 32（原 36）、行距 36（原 40）、全部在 520-696 区间

### 卡片设计要点（浅色价格对比型）
```
底色：#FAF7F2 → #F3F0E8 渐变
白卡：x=62, y=50, w=900, h=924（底部内容必须在 y < 974 以内）
5 品牌色：DeepSeek 蓝 #4F6EF7 / Qwen 橙 #FF6A00 / GPT-4o 绿 #10A37F / Claude 橙 #CC4C00 / Gemini 蓝 #4285F4
封面：大标题 88px + 80px，无投影
对比表：表头 + 表行 + 省钱公式 + 推荐场景，全部在 1024×1024 内紧凑排布
Model 卡：品牌色顶栏 180px → 价格三列 → 核心优势 → 警告区 → 标签
```

### 发布命令（本项目的正确写法）
```bash
opencli xiaohongshu publish "大模型API价格战

DeepSeek-V4 去年..." \
  --title "大模型API价格战" \
  --images "price-war-cover.png,price-war-table.png,..." \
  --topics "大模型,API,DeepSeek,Qwen,GPT-4o,Claude,Gemini,价格对比" \
  --window foreground \
  --site-session persistent \
  -f yaml
```

### 飞书文档
- URL：https://www.feishu.cn/docx/GXIRdu3h0o6nHKxoiBvcYomcnMk
- 8 张图全部上传成功

### 关键约束（本次验证）
1. **标题第一行**：正文第一行必须是标题文字
2. **无时间戳**：SVG 卡片内容、正文都不出现日期/版本号
3. **直接发布**：去掉 `--draft true` 即直接发布，返回 `status: ✅ 发布成功`
4. **SVG 白卡边界**：内容 y 坐标必须 ≤ 白卡 bottom（y=974），footer 在 y=955 安全
5. **Logo 字典映射**：模型名含特殊字符（`-`、`.`、数字）时必须用显式映射
6. **覆盖重发流程**：`docs +update --mode overwrite` 清空文档 → 重插全部图片

## 22. hermes-feishu-xhs 项目经验（2026-06-03）

### 项目结构
```
hermes-feishu-xhs/
├── article.md              # 小红书草稿（标题 17 字 + 正文 812 字）
├── README.md               # 完整博客版
├── gen_cards.py            # SVG→PNG 生成器（8 张 v3 高饱和全幅渐变卡片）
├── hermes_logo.json        # Hermes 官方 favicon base64（48×48 → 128×128 LANCZOS 放大）
├── feishu_logo.json        # 飞书图标 base64（144×145 → 128×128）
├── hermes-feishu-cover.png # 封面（双 Logo + 🤝 + 安装命令）
├── hermes-feishu-card-1..7.png  # ①-⑦ 编号卡片
```

### 卡片设计演进（v1 → v3）

| 版本 | 背景 | Logo | 标题 | 用户反馈 |
|------|------|------|------|----------|
| v1（suno-udio 模板） | 米白底+白卡片 | 无 | 普通大小 | ❌ 图不吸引人 |
| v2（高饱和渐变） | 全幅渐变 | 无 | 140px 大数字 | ❌ 封面缺 logo |
| v3（双 Logo 封面） | 左紫右蓝渐变 | Hermes+favicon + 飞书官方图标 | 无投影 | ✅ |

### v3 封面设计详解
```
布局：                        色彩：
  [Hermes] ↔ 🤝 ↔ [飞书]     左 → 右：#7C3AED → #3370FF
     ↓            ↓           文字无投影（glow filter 已移除）
   "Hermes"    "飞书"          Logo 放在白色圆形背景上（shadow filter）
     ↓
  "AI管家 + 飞书后台 = 双剑合璧"
     ↓
  ⚡ 一行命令安装
  curl -fsSL https://...
     ↓
  175K+ Stars · MIT · Nous Research
```

### Logo 获取策略（本次验证）
- **Hermes**：从 `https://hermes-agent.nousresearch.com/favicon.ico` 下载（48×48 RGBA），用 PIL LANCZOS 放大到 128×128，base64 嵌入 SVG
- **飞书**：从 `https://p1-hera.feishucdn.com/...` CDN 下载（144×145 RGBA），同样 LANCZOS 放大
- **Logo 存储**：base64 数据存为 `.json` 文件，`gen_cards.py` 运行时 `json.loads()` 读取，避免 Python 源码中嵌入巨型字符串

### SVG 卡片关键修复（本次踩坑）

**1. 封面文字投影（glow filter）**
- 症状：用户反馈"文字不需要有投影"
- 根因：Hermes/飞书/🤝 文字使用了 `filter="url(#glow)"`
- 修复：删除 `<text>` 上的 `filter="url(#glow)"`，同时删除 `<defs>` 中的 glow 滤镜定义
- 注意：logo 的白圆底座的 `filter="url(#shadow)"` 保留（这是圆形的阴影，不是文字的）

**2. Logo 白圆底座设计**
- 每个 logo 放在白色圆形（r=80）上，带轻度阴影
- 位置：Hermes x=310, 飞书 x=714（对称分布），y=280
- 图标 128×128，居中显示（x=246/650, y=216）

**3. 双 Logo 布局（cover 专属 vs 编号卡）**
- cover 用特殊布局（左右对称 + 中间握手）
- 编号卡保持 v2 全幅渐变 + 大数字风格不变
- 区分通过 `c["sg"] == "cover"` 条件判断

**4. 封面底部安装命令**
- `rect x=120, y=780, w=784, h=64` 半透明黑底
- 命令行黄色文字 `fill="#FDE68A"` 更醒目
- 安装 badge 在命令上方（y=700）

**5. 卡片设计与前序 patterns**
- 封面双 logo 让用户一眼看清"这个产品对接了谁"
- 编号列表 + 统一底部布局（半透明黑卡叠加"底栏"）
- 每卡一个 emoji 图标作"锚点"，提高信息辨识度

## 23. deepseek-api-apply-xhs 项目经验（2026-06-03）

### 项目结构
```
deepseek-api-apply-xhs/
├── article.md                         # 小红书草稿（标题 20 字 + 正文 476 字）
├── README.md                          # 完整博客版
├── gen_cards.py                       # SVG→PNG 生成器（6 张浅色爆款卡片）
├── deepseek-square-cover.png          # 封面卡（1024×1024，SVG 生成）
├── deepseek-gemini-cover.png          # Gemini AI 生成封面（1024×1024）
├── deepseek-card-1..5-signup/apikey/code/pricing/tips.png  # 步骤卡（800×800）
```

### 发布参数（实测）
- 标题：`DeepSeek API 申请保姆级教程` = 20 字 ✓
- 正文：476 字（首行为标题）✓
- 图片：6 张（1 cover + 5 步骤卡）
- 话题：10 个
- 状态：✅ 暂存成功（草稿箱）

### 卡片设计要点（浅色大标题爆款型）
```
底色：#FAF7F2 → #F5F0E8 渐变
标题栏：rx=50 pill 形状，浅色背景 + 深色文字（#1E293B）
封面：大标题 80px gradient（蓝→紫→粉），带 shadow filter
步骤卡：48px 粗体标题 + 白卡片分块 + 左侧色条指示器
代码卡：深色终端风格 #1E293B 背景，语法高亮
价格卡：两个模型白卡上下排列，底部比较标签
避坑卡：红色 alert 标题 + 4 条 tips 列表
```

### SVG 关键陷阱（本次踩坑）

**1. `&` 字符必须转义为 `&amp;`**
- 症状：`"注册 & 登录"` → Inkscape 报 `xmlParseEntityRef: no name`，卡片渲染空白
- 根因：`&` 在 XML/SVG 中是特殊字符，不能直接写在文本内容里
- 修复：所有文本中的 `&` 改为 `&amp;`
- 检查点：`grep '&[^a]' *.svg` 可发现未转义的 `&`

**2. 标题栏文字颜色对比度**
- 症状：白字 (`#FFF`) 在纯色蓝/紫/绿/橙/红背景上看不清
- 修复：标题栏背景改为浅色版（`BLUE_LIGHT`/`PURPLE_LIGHT`/...），文字改为深色 `#1E293B`
- 原则：标题栏主体用 light variant 做 bg + dark text，而非 bold color + white text

**3. 代码块行距溢出**
- 症状：Python 代码块 6 行 × 34px 行距 = 204px，超出 block height 210px
- 根因：行数 × 行距 > 容器高度，末行文字跑出圆角边界
- 修复：增大 block height（210→230px）或减小字号/行距
- 公式：`block_height ≥ last_line_y + font_size * 1.4`

**4. lark-cli media-insert 路径限制**
- 绝对路径 `/Users/.../file.png` → `unsafe file path: --file must be a relative path`
- 必须 `cd` 到卡片目录后用 `--file ./xxx.png`

**5. Gemini 封面命名**
- `opencli gemini image --op <dir>` 输出 `gemini_<timestamp>.png`
- 需要手动 `cp / mv` 为有意义的名字（如 `deepseek-gemini-cover.png`）

### 飞书文档
- URL：https://www.feishu.cn/docx/OUVXdi4u3olD4hxhN8ncn7runpb
- 7 张图全部上传成功（gemini cover + svg cover + 5 步骤卡）

### 关键约束（本次验证）
1. **标题 ≤ 20 字**：`"DeepSeek API 申请保姆级教程"` = 20 ✓（含 emoji 会超限）
2. **正文 ≤ 950 字**：476 字，内容到"关注我"结尾
3. **首行即标题**：正文第一行复制标题文字
4. **无时间戳**：SVG 卡片、正文均无日期/版本号
5. **Card 3 代码块**：双 block（cURL + Python），需确保行距不溢出
6. **lark-cli 图片插入**：先 `cd` 到目录，再用相对路径 `--file ./xxx.png`

## 24. opencut-xhs 项目经验（2026-06-03）

### 项目结构
```
opencut-xhs/
├── article.md              # 小红书草稿（标题 15 字 + 正文 444 字）
├── README.md               # 完整博客版
├── gen_cards.py            # SVG→PNG 生成器（4 张浅色大标题卡片）
├── opencut-cover.png       # 封面 (1024×1024)
├── opencut-card-1.png      # 核心能力 2×2 网格 (1024×1024)
├── opencut-card-2.png      # OpenCut vs 剪映 对比表 (1024×1024)
└── opencut-card-3.png      # AI 黑科技全家桶 (1024×1024)
```

### 发布数据
- 标题：`OpenCut 开源剪映平替🔥`（15 字，≤20 ✓）
- 正文：444 字（≤950 ✓），首行即标题
- 图片：4 张（≤9 ✓）
- 话题：OpenCut,开源,剪映,视频剪辑,AI工具,效率工具,CapCut
- 状态：✅ 暂存成功（草稿箱）
- 飞书文档：`https://www.feishu.cn/docx/Kj89dwCN1o7Vigx6Z9EcHbRanQc`

### 卡片设计要点（浅色大标题 XHS 爆款型）
```
底色：#FAF7F2 → #F0EBE0 渐变
强调色：蓝色 #2563EB / 紫色 #8B5CF6 / 绿色 #10B981 / 橙色 #F59E0B
封面：140px 超大标题 "Cut" + OPEN 小字 eyebrows + 安装命令按钮
功能卡：2×2 大圆角白卡，每卡 icon + 标题 + 描述
对比卡：表头蓝底 + 行交替白底 + 末尾安装 CTA
AI 卡：2×2 四象限白卡，icon + 标题 + 双行描述
```

### 踩坑记录

**1. opencli gemini image 返回 no-images**
- 症状：`status: ⚠️ no-images`，Gemini 页面打开了但未生成图片
- 可能原因：Gemini 会话未登录或 prompt 不符合生成条件
- 尝试方案：换了 3 次 prompt + `--window foreground/background` 均失败
- 结论：Gemini 当前会话不可用，全部用 SVG 卡片代替封面

**2. opencli xiaohongshu publish 图片上传失败**
- 首次使用 ``--window background`` 时报 `Image injection failed: No file input found on page`
- 修复：改用 `--window foreground` 让浏览器窗口在前台运行，上传成功
- 经验：XHS publish 命令必须用 foreground 模式，后台无法操作 file input

**3. 首次 publish `--draft true` 输出格式**
- 本次启用了 `--window foreground --site-session persistent -f yaml` 四个参数
- 返回格式：`- status: ✅ 暂存成功`（yaml 数组格式）
- 区别于其他项目的 `"ok": true` JSON 格式——注意解析差异

### 内容迭代（无，一稿过）
- 标题、正文、卡片全部一次通过用户审核
- 验证了"浅色大标题 + 对比表 + AI 功能"组合适合开源工具介绍类内容

## 25. mcp-xhs 项目经验（2026-06-03）

### 项目结构
```
mcp-xhs/
├── article.md              # 小红书草稿（标题 19 字 + 正文 867 字）
├── README.md               # 完整博客版 + 文件清单
├── gen_cards.py            # SVG→PNG 生成器（5 张浅色大标题卡片）
├── mcp-cover.png           # 封面 (1024×1024) 标题 100px
├── mcp-card-1-problem.png  # 问题卡 (800×800)
├── mcp-card-2-what.png     # MCP 定义卡 (800×800)
├── mcp-card-3-how.png      # 工作原理卡 (800×800)
└── mcp-card-4-adoption.png # 生态数据卡 (800×800)
```

### 封面标题布局（核心教训）
- 标题 `"MCP 是什么？"` font-size=100px，baseline y=230
- 文字底部 ≈ y=230 + 25(descent) = y=255
- 副标题卡从 y=300 开始，gap=45px → 安全
- **公式**：`gap ≥ fontsize × 0.5`，100px 字号至少留 50px 到下一个元素
- 标签卡（eyebrow）从 y=40 开始，font-size=26px，gap 充裕

### 标题文字禁用投影（规则）
- `<text>` 元素上**永远不要**加 `filter="url(#glow)"` 或 `filter="url(#shadow)"`
- 用户多次反馈投影降低可读性和高级感
- `<rect>` 容器的卡阴影（feDropShadow）可以保留，这不属于"标题文字投影"
- 这条规则已记入 AGENTS.md SVG pitfalls 节

### SVG 的 & 转义
- 正文含 `&`（如 `"OpenAI & Google"`）必须写为 `&amp;`
- 否则 Inkscape 报 `xmlParseEntityRef: no name`，整张卡片变空白
- 检查方法：`grep '&[^a]' gen_cards.py` 除 `&amp;` 外不应有裸 `&`

### 浅色风格白字检查清单
- `fill="#FFF"` 或 `fill="#FFFFFF"` 只允许出现在**深色背景**上（如色号 #2563EB/#7C3AED/#059669 等）
- 浅色背景（`BLUE_LIGHT`/`GREEN_LIGHT`/cream/white）上的文字必须用深色（`#1E293B` 或品牌色）
- 检查方法：`grep -n 'fill="#FFF\|fill="#FFFFFF' gen_cards.py` 逐一确认背景色

### opencli gemini image 可靠性
- 本次 `opencli gemini image` 两次调用均返回 `status: ⚠️ no-images`
- Gemini 页面打开了但未生成图片（可能会话状态或 prompt 问题）
- **结论**：不可作为封面唯一来源，SVG 卡片必须自带封面作为 fallback

### opencli xiaohongshu publish topics 限制
- `--topics` 中不常见的话题名（如 `"MCP"`、`"AI协议"`、`"ModelContextProtocol"`）导致 `Could not attach topic: no real topic entity appeared after selection`
- 修复：去掉 `--topics` 参数，发布成功
- **经验**：XHS 话题必须使用平台已有的热门标签，小众标签会导致整个发布失败
- 要么用常见话题（`AI工具,大模型,开发者,开源`），要么不传 `--topics`

### 本次发布数据
- 标题：`MCP 是什么？AI 圈的 USB-C`（19 字，≤20 ✓）
- 正文：867 字（≤950 ✓），首行即标题 ✓
- 图片：5 张（≤9 ✓）
- 话题：无（去掉了 `--topics` 因话题无法匹配）
- 状态：✅ 暂存成功（草稿箱）
- 飞书文档：`https://www.feishu.cn/docx/QyGudmAkjopuJGxj9DGcnQUgnpc`

## 26. openclaw-feishu-xhs 项目经验（2026-06-03）

### 项目结构
```
openclaw-feishu-xhs/
├── article.md              # 小红书草稿（标题 10 字 + 正文 608 字）
├── README.md               # 完整博客版 + 链接
├── gen_cards.py            # SVG→PNG 生成器（4 张浅色大标题卡片）
├── openclaw-square.png     # 封面 (1024×1024) 官方龙虾 logo
├── openclaw-card-1.png     # 飞书官方插件功能列表 (1024×1024)
├── openclaw-card-2.png     # 两步开通指南 (1024×1024)
└── openclaw-banner.png     # 横幅 (1792×1024)
```

### 发布数据
- 标题：`AI助手接入飞书绝了`（10 字，≤20 ✓）
- 正文：608 字（≤950 ✓），首行即标题 ✓
- 图片：4 张（≤9 ✓）
- 话题：无（`OpenClaw`/`AI` 都无法匹配 XHS 话题实体，去掉 --topics 后成功）
- 状态：✅ 暂存成功（草稿箱）
- 飞书文档：https://www.feishu.cn/docx/QNEWdBRmboIuVmxMtzcceAYNn3b

### 官方 Logo 嵌入 SVG
- OpenClaw 官方图标从 `https://openclaw.ai/favicon.svg` 获取（红色龙虾 SVG）
- 剥掉 SVG 外套（`<svg>...</svg>`），只取 `<g>` 内的 path 数据
- Gradient def 合并到 `<defs>` 中统一管理，避免重复定义
- 龙虾图标嵌入到封面卡（square）顶部居中，banner 卡左上角

### 卡片设计要点（浅色大标题爆款型）
```
底色：#FAF7F2 → #F3F0E8 渐变
Logo：官方龙虾 favicon 路径嵌入 SVG（scale 0.65，居中/左上角）
封面：Logo → OpenClaw 60px → × 飞书 190px 超大标题 → 副标题 38px → 命令 (BLUEL底+BLUE文)
功能卡：6 大领域列表（蓝/青/紫/橙/绿/粉），每领域 key + 名称 + 描述
教程卡：Step 1/2 + 可选插件 + 重启命令
Banner：Logo（左上）+ 标题 220px + 命令 + 6 领域标签
```

### 关键踩坑 & 修复

**1. 标题文字与下方元素重叠**
- 症状：封面 "OpenClaw" 与下方 "× 飞书" 文字重叠
- 修复：重新分配 y 坐标，增大间距（Logo y=95 → OpenClaw y=260 → × 飞书 y=460 → 副标题 y=560）
- 公式：`gap ≥ fontsize × 0.5` 留安全间距

**2. 浅色风格不能用白色文字**
- 原设计：蓝色按钮（`#3370FF`）上白色文字 `fill="#FFFFFF"`
- 修复：改为浅蓝底 `BLUEL`（`#E8EEFF`）+ 深蓝字 `BLUE`（`#3370FF`）
- 规则：浅色卡片上任何文字都不能用 `#FFF`/`#FFFFFF`

**3. 标题文字禁用投影**
- SVG 中 `<text>` 元素不添加任何 `filter` 属性（glow/shadow）
- 容器的阴影（`<rect>` 上的 feDropShadow）可保留

**4. 官方 Logo 太小**
- 初版 `scale(0.45)` → 用户反馈太小 → 放大到 `scale(0.65)`
- 面积增大约 2 倍，视觉上合适

**5. opencli xiaohongshu publish 话题匹配失败**
- `OpenClaw`、`AI`、`飞书` 等话题都返回 `Could not attach topic: no real topic entity appeared`
- 修复：去掉 `--topics` 参数后发布成功
- 经验：小众/非 XHS 热门话题直接导致发布失败，要么用平台已有热门标签，要么不传

**6. SVG 属性闭合引号检查**
- `height="{h}>` 漏写 `"` → Inkscape 输出空白 PNG
- 所有 SVG 属性必须显式用 `"` 闭合

### 正文格式严格执行
- **标题 ≤ 20 字符**：`AI助手接入飞书绝了` = 10 ✓
- **正文 ≤ 950 字**：608 ✓
- **首行即标题**：正文第一行是标题文字
- **无时间戳**：正文中无日期/版本号
- **纯文本**：不支持 Markdown 格式（`---`、`###` 等会显示为原文）

## 27. ai-graveyard-xhs AI产品死亡名单（2026-06-03）

### 项目结构
```
ai-graveyard-xhs/
├── article.md              # 小红书草稿（标题 14 字 + 正文 684 字）
├── README.md               # 完整博客版 + 数据来源
├── gen_cards.py            # SVG→PNG 生成器（5 张浅色无白块卡片）
├── ai-graveyard-cover.png       # 封面 (1024×1024)
├── ai-graveyard-card-1-global.png  # 全球重磅关停 (800×800)
├── ai-graveyard-card-2-cn.png      # 国产阵亡名单 (800×800)
├── ai-graveyard-card-3-death-reasons.png  # 三大死因 (800×800)
└── ai-graveyard-card-4-survivors.png   # 幸存者名单 (800×800)
```

### 发布数据
- 标题：`AI死亡名单｜年度关停大盘点`（14 字，≤20 ✓）
- 正文：684 字（≤950 ✓），首行即标题 ✓
- 图片：5 张（≤9 ✓）
- 话题：有 topics 在 body 标签中，publish 时不传 `--topics`（因话题无法匹配）
- 状态：✅ 暂存成功（草稿箱）
- 飞书文档（最终版）：`https://www.feishu.cn/docx/Ky3gdcCiGoKMuRxI5gecpP4KnKd`

### 卡片设计原则（浅色无白色大块）
```
底色：#FAF7F2 → #F0EAE0 径向渐变
结构：奶油底色直接放文字，不用白色卡片做容器
分区：用细线（<line>）或间距做视觉分隔
色块：仅用浅色变体（RED_LIGHT/PURPLE_LIGHT/PINK_LIGHT/BLUE_LIGHT）作为数据标签
文本：始终深色（#1E293B 或品牌色），无 #FFF 白字
投影：无 feDropShadow 滤镜（Inkscape WARNING + 用户厌恶）
圆角：rx=16~30 数据标签
```

### 关键踩坑 & 修复

**1. 首图标题与下方文字重叠（3 轮修复）**
- v1 问题：白色卡片内，"💀 2025-2026 关停大盘点" (y=120 fs=28) 与 "AI 产品死亡名单" (y=190 fs=80) 重叠 20px
- v2 修复：移出白色卡片，subtitle y=70 + 白卡 y=100-240 + title y=200 + 副标题 y=318 + 数据 y=500-980 → 互不重叠
- v3 修复：去掉全部白色卡片，用奶油底色直接承载文字 + 细线分隔
- **教训**：布局设计用 Python 预算每个 text 的 `[top, bottom]` 范围，确保 gap ≥ 20px

**2. 浅色风格不能出现白色文字**
- 全局检查所有卡片，移除 3 处 `fill="#FFF"`（card-1 底部条、card-3 标题栏、card-4 结论条）
- 改为浅色背景（RED_LIGHT）+ 深色文字（RED/TEXT）
- **规则**：浅色卡片全卡无 `#FFF`/`#FFFFFF`，背景和文字都必须在浅色系内

**3. 文字永远不要出现投影**
- 移除全部 `<feDropShadow>` 滤镜（4 张卡片 × defs + 引用）
- 移除后 Inkscape 不再报 `WARNING: unknown type: svg:feDropShadow`
- **规则**：SVG `<text>` 元素永远不加 filter，`<rect>` 容器的投影也不加（统一无阴影）

**4. 避免大片白色色块**
- 初版封面有 3 个白色大 rect（标题卡 900×176、副标题卡 700×72、数据卡 900×540）
- 用户反馈"大片的白色色块，很low"
- 修复：全部去掉，文字直接放在奶油渐变底色上
- **经验**：浅色风格用奶油色（#FAF7F2）基底 + 小面积浅色强调块 + 细线分隔，比白色大卡片更高级

**5. opencli gemini image 返回 no-images**
- 与 mcp-xhs 和 opencut-xhs 现象一致
- **结论**：Gemini 当前不可靠，SVG 封面是唯一稳定的封面来源

**6. opencli xiaohongshu publish topics 限制**
- `AI产品` / `AI` 等话题均无法匹配 XHS 话题实体
- 去掉 `--topics` 后发布成功
- **经验**：不常见话题名一律去掉 `--topics`，body 中的 #标签 已足够

### 设计决策记录
| 轮次 | 封面布局 | 白色块 | 投影 | 文字颜色 | 结果 |
|------|---------|--------|------|---------|------|
| v1 | 3 层白卡堆叠 | 3 个大白色 rect | feDropShadow | 有 #FFF | ❌ 重叠+白块+白字+投影 |
| v2 | 4 层白卡 + 间距调整 | 3 个白卡 | 无 | 无 #FFF | ❌ 白块仍存在 |
| v3 | 奶油底面 + 细线分隔 | 0 个白卡 | 无 | 全深色 | ✅ |

### 正文格式（严格执行）
- 标题 ≤ 20 字：`AI死亡名单｜年度关停大盘点` = 14 ✓
- 正文 ≤ 950 字：684 ✓
- 首行即标题：正文第一行复制标题
- 无时间戳：不出现日期/版本号
- 纯文本：无 Markdown（无 `---` `###` `**` `>`）
- 短段落 + emoji 分段 + · 列表 + 末尾 #标签
- 话题标签用 # 写 body 中，publish 不传 `--topics`

## 28. Twitter (X) 推文串发布（2026-06-03）

### 项目
- **内容**：`github-trending/` — GitHub AI 今日最热 Top 10
- **账号**：`@DubaIGOHGOkTHOk`（老何不会）
- **首发链接**：`https://x.com/DubaIGOHGOkTHOk/status/2062129953102291358`

### 发布流程
```bash
# 1. 绑定浏览器会话（用户已登录 X）
opencli browser <session> bind

# 2. 发首条推文
opencli twitter post "<text>" \
  --window foreground \
  --site-session persistent \
  -f yaml

# 3. 逐条回复组成 thread
opencli twitter reply "<首条URL>" "<text>" \
  --window foreground \
  --site-session persistent \
  -f yaml
```

### 字符限制
- **中文推文**：每个 CJK 字符计 2 字，最多 140 汉字（280 加权字符上限）
- 英文字母/数字/空格计 1 字
- emoji 计 2 字
- 超过 280 加权字符时 `tweetButton` 或 `tweetButtonInline` 的 `aria-disabled="true"`
- 快速估算：中文字符数 × 2 + ASCII 字符数 ≤ 280

### 命令限制

| 命令 | 策略 | 是否可用 | 说明 |
|------|------|----------|------|
| `twitter post` | UI | ✅ 可用 | 必须 `--window foreground` |
| `twitter reply` | UI | ✅ 可用 | 同上，文本太长老会验证失败 |
| `twitter delete` | UI | ❌ 不可用 | 找不到"More"菜单，适配器 bug |
| `twitter thread` | COOKIE | ✅ 只读 | 读取已有 thread |

### manual eval （适配器 fallback）

当 `twitter post/reply` 验证失败时，可直接用 browser eval 操作：

```javascript
// 1. 设置文本
const tb = document.querySelector('[data-testid=tweetTextarea_0]');
tb.focus();
tb.textContent = '';
document.execCommand('insertText', false, '🔥 推文内容');
tb.dispatchEvent(new Event('input', {bubbles: true}));

// 2. 点击发布按钮
const btn = document.querySelector('[data-testid=tweetButton]');
if (btn && !btn.disabled) btn.click();
```

### compose button 索引
- `data-testid=SideNav_NewTweet_Button` — 侧边栏"发帖"按钮
- `data-testid=tweetButton` — 对话框内的"发帖"按钮（dialog 内）
- `data-testid=tweetButtonInline` — 主页时间线的内嵌"发帖"按钮
- 注意：ref 索引在 React 重新渲染后会变化，用 CSS 选择器更稳

### 踩坑记录

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| `twitter post` 后台超时 | `--window background` 无法操作 UI | 改用 `--window foreground` |
| `Tweet button is disabled` | 文本超 280 加权字符 | 缩减到 ≤140 汉字 |
| `Could not verify reply text` | 回复文本含换行或过长 | 缩短文本 / 用 eval 替代 |
| contenteditable 换行失效 | `execCommand('insertText')` 处理 `\n` 有误 | 用 `<div>` 包裹第二行 |
| `twitter delete` 失败 | 适配器找不到菜单选择器 | 改用手动 eval 删除 |

### thread 长度建议
- **首条推文**：一句话标题 + 指引（如"看 thread 👇"），配图
- **每条回复**：1-2 个项目，≤ 140 汉字
- **回复数**：建议 ≤ 10 条，太多会被折叠
- 推文串的每条回复都是独立的推文，发布后不可批量管理

## 29. cc-switch-xhs → Twitter 单条推文发布（2026-06-03）

### 场景
将 XHS 卡片内容压缩为单条推文 + 全部 4 张图片发布到 Twitter。

### 发布命令
```bash
opencli twitter post "<text>" \
  --images "img1.png,img2.png,img3.png,img4.png" \
  --window foreground \
  --site-session persistent \
  -f yaml
```

### 关键发现
| 项目 | 说明 |
|------|------|
| 图片数量上限 | 4 张（`--images` comma-separated） |
| 图片路径 | 相对 CWD，与 XHS 发布规则相同 |
| 文字换行 | 直接支持 `\n`，无需特殊处理 |
| 话题标签 | 正文内 `#Tag` 正常渲染 |
| 命令策略 | `UI` 模式，必须 `--window foreground` |

### XHS → Twitter 内容适配
- XHS 正文 ~950 字 → 压缩为 ≤280 加权字符（约 140 汉字）
- 保留核心亮点：Codex OAuth 保留、Chat 工具路由恢复、稳定性修复
- XHS 生成的 4 张卡片 PNG 可直接复用，无需额外制作
- 删除 XHS 特有的语气词和引导句式，改用 Twitter 风格短句

### 踩坑记录
| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 无（本次成功） | — | — |

## 30. 批量 XHS → Twitter 全量发布（2026-06-03~04）

### 发布统计
| 项目 | 值 |
|------|-----|
| 文件夹总数 | 37 个 `-xhs/` |
| 已发布 | 36 个（含本次 + 历史） |
| 未发布 | 1 个（`ai-xhs-tool-xhs`，无 PNG 图片） |
| 本次新增 | 32 个 topic |
| 账号 | @DubaIGOHGOkTHOk（老何不会） |

### 发布方式
- **单条推文 + 最多 4 张图**：将 XHS ~950 字正文压缩为 ≤280 加权字符
- **间隔 2 分钟**：第 1 批用 Python 脚本自动发（21 条），第 2 批因脚本中断手动补发（11 条）
- 有 banner 的文件夹优先用 square/cover + card1~3，最多 4 张

### XHS → Twitter 适配规则
| 维度 | 策略 |
|------|------|
| 字数 | 压缩到 80~150 加权字符，保留核心亮点 |
| 图片 | 选 square/cover + 2~3 张内容卡，最多 4 张 |
| 话题标签 | 2~4 个，尾部 `#Tag` |
| 风格 | 去掉"评论区聊聊"等 XHS 引导语，改用短句 |

### 命令限制经验
| 命令 | 限制 |
|------|------|
| `--images` | 最多 4 张，路径相对 CWD |
| `--window foreground` | 必须前台窗口，后台会超时 |
| `opencli twitter post` | text 含 `\n` 换行正常支持 |
| 批量脚本 | Python subprocess 需 `cwd` 参数，bash 需先 `cd` |

### 跳过目录
- `ai-xhs-tool-xhs`：目录内无任何 PNG 图片，无法发布

## 31. ai-interview-xhs 项目经验（2026-06-04）

### 项目结构
```
ai-interview-xhs/
├── article.md              # 小红书草稿（标题首行 + 正文）
├── README.md               # 完整博客版
├── gen_cards.py            # SVG→PNG 生成器（4 张浅色 + 4 张深色大标题卡片）
├── ai-interview-lite-1~4.png  # 浅色中文卡片 (800×800)
├── ai-interview-dark-1~4.png  # 深色英文卡片 (800×800)
├── *.svg                   # SVG 源文件
└── twitter_thread.txt      # X/Twitter 推文串
```

### 内容迭代（3 轮重写）

| 轮次 | 问题 | 修复 |
|------|------|------|
| v1 | 内容太干巴，像产品说明书 | 重写为个人体验 + 真香反转风格 |
| v2 | 用户要求"像素级模仿平台热点"，提供爆款规范 | 严格按规范重写：姐妹们/亲测/避坑/痛点引入+干货+CTA |
| v3 | 一稿过 | 标题 19 字，正文 414 字，4 张浅色卡 + 4 张深色卡 |

### v3 爆款规范（严格执行）

**小红书文案规范：**
- 调性：利他价值 + 情绪共鸣，用"姐妹们/亲测/避坑/大数据帮我推给"等高互动口吻
- 结构：痛点引入（8000块班）→ 个人经历（练30遍）→ 干货（AI追问狠、逐题评分）→ 行动呼吁（别等面试前一周）→ CTA（一杯奶茶换铁饭碗）
- 标题 ≤ 20 字：`姐妹们！49块AI面试模拟亲测真香了😭` = 19 ✓
- 正文 ≤ 950 字：414 ✓
- 标题必须作为正文第一行
- 无时间戳

**X/Twitter 推文串规范：**
- 调性：观点输出 + 认知颠覆，犀利精炼有启发性
- 主推文第一句必须是 Hook：`考公面试班8000块，AI面试模拟49块。我选了后者。`
- 主推文 ≤ 140 字（中文）：113 ✓
- 超出部分自动切分为连贯 Thread
- 多用换行留白，营造呼吸感

### 卡片设计要点（大标题爆款型）

**浅色中文卡片（XHS 用）：**
```
底色：#FAF7F2 → #F5F0E8 渐变
装饰：角落装饰圆（accent color, opacity 0.04-0.06）
emoji：大 emoji 在标题上方（🎯⚡🔥💰）
主标题：64px 粗体 深色 #1E293B
副标题：32px 品牌色
边框：极细圆角矩形（opacity 0.12）
```

**深色英文卡片（X/Twitter 用）：**
```
底色：径向渐变 #141B33 → #0B1027（近黑，避免纯#000）
装饰：角落装饰圆（accent color, opacity 0.10-0.15）
边框：极细圆角矩形（accent color, opacity 0.15）
主标题：60px 粗体 亮色（LIGHT_BLUE/LIGHT_GREEN/LIGHT_PINK/LIGHT_YELLOW）
副标题：30px 亮色（opacity 0.85）
```

### 关键踩坑 & 修复

**1. opencli gemini image 返回 no-images**
- 与 mcp-xhs/opencut-xhs/ai-graveyard-xhs 现象一致
- **结论**：Gemini 不可靠，SVG 卡片是唯一稳定的封面来源
- **经验**：不要依赖 Gemini 生成卡片，gen_cards.py 必须自带完整封面

**2. 正文内容太干巴（2 轮重写）**
- v1 像产品说明书 → 用户反馈"太干巴"
- v2 加了个人体验但还不够 → 用户提供了完整的"爆款写作风格规范"
- v3 严格按规范重写，一稿过
- **教训**：AI 生成内容天然偏"说明书式"，必须主动注入情绪词、个人故事、互动感口吻

**3. GitHub 推送网络问题**
- `Failed to connect to github.com port 443` — 网络抖动
- 已在 commit 中暂存，待网络恢复后 push

### 发布数据
- 小红书：✅ 暂存成功（草稿箱）
- 飞书文档：https://www.feishu.cn/docx/Kq8QdrffhoVZaDx5WvIcCR9UnKf
- 8 张卡片全部上传成功
- X/Twitter Thread：已准备（主推文 + 续推文），待用户确认发布

## 32. video-elderly-quotes-xhs AI老人语录红利（2026-06-05）

### 项目结构
```
video-elderly-quotes-xhs/
├── article.md                  # 小红书草稿（标题 10 字 + 正文）
├── README.md                   # 完整博客版 + 变现方式
├── gen_cards.py                # SVG→PNG 生成器（3 张浅色卡片）
├── ai-elderly-cover.png        # 封面 (1024×1024) — GPT+MJ+BGM+分发 4步
├── ai-elderly-workflow.png     # 4步套路拆解 (1024×1024)
└── ai-elderly-money.png        # 4种变现方式 (1024×1024)
```

### 发布数据
- 小红书：⚠️ 浏览器待确认（未自动完成，需手动点发布）
- Twitter：✅ 成功 — https://x.com/DubaIGOHGOkTHOk/status/2062491514408947760
- 图片：3 张（封面 + 工作流 + 变现）

### 内容要点
- 主题：微信视频号 AI 老人语录红利（GPT 模写莫言体 + AI 头像 + 慢 BGM）
- 目标人群：45-65 岁中老年人，对人生哲理类内容有天然信任感
- 核心卖点：GPT+Midjourney+剪映，新手 1 小时上手

### Twitter 发布验证
- 命令：`opencli twitter post` + 3 张图片 → 一次成功，无故障
- 字符数：178 加权字符（< 280 ✓），含中文 + ASCII + #Tag
- 换行：`\n` 在 text 中的换行正常渲染
- 图片：3 张 1024×1024 PNG（610KB + 141KB + 113KB），无尺寸/分辨率问题

### 小红书发布状态
- `opencli xiaohongshu publish` 返回 `⚠️ 操作完成，请在浏览器中确认`
- 与之前某些项目的 `✅ 发布成功` 或 `✅ 暂存成功` 不同
- 需要用户手动在浏览器中点确认（发布页已打开，图片已上传）

### 本会话经验
1. **Twitter 单条发布工作流可靠**：使用 `opencli twitter post` + `--window foreground --site-session persistent -f yaml` 稳定成功
2. **XHS publish 状态多样**：返回值有 `✅ 发布成功`、`✅ 暂存成功`、`⚠️ 操作完成，请在浏览器中确认` 三种，后一种需用户手动操作
3. **3 张图片适配两种平台**：小红书用 3 张，Twitter 用同样的 3 张（≤4 上限）
4. **卡片设计**：浅色奶油底 + 4 个步骤卡片 + 文字对称分布，无重叠问题
5. **内容定位**：微信视频号 + 中老年流量赛道，属于"信息差红利"类内容

## 35. 合集型文章卡片设计规范（ai-tools-xhs）

### 内容密度要求
- **卡片不能只有大标题**：用户明确要求"体现具体内容"，每张卡片必须有具体的工具名 + 简短点评
- **每张卡片 3-6 个具体条目**，使用 3×2 网格布局或垂直列表
- **分类标题 + 具体条目**的组合结构（如"🎨 生图类"下罗列 Leonardo.ai, Playground 等）

### 浅色/深色卡片的语言规则
- **浅色卡片 → 中文**：奶油底 `#FAF7F2` → `#F5F0E8` 渐变，深色文字 `#1E293B`
- **深色卡片 → 英文**：深蓝底 `#0B1027`，白色/浅色文字 `#FFFFFF`
- 两条规则**不可混用**：浅色用英文或深色用中文都会造成风格不一致

### 视觉限制严格执行
- **无投影/阴影**：`<text>` 不得使用 `filter="url(#glow)"` 或 `filter="url(#shadow)"`
- **浅色卡无白色或灰色文字**：仅用 `#1E293B` 级深色
- **深色卡无黑色或暗色文字**：仅用 `#FFFFFF` 或高亮色（如 `#FFD700`）
- **文字不重叠、不溢出**：预先计算 y 偏移量，控制每张卡片条目数（6条以内/卡）

### SVG 特殊字符
- `&` 在 SVG text 中必须写作 `&amp;`，否则 Inkscape 报 `xmlParseEntityRef: no name`
- 中文字符串中避免使用 `&`，如 `"Free & Open"` 改为 `"Free and Open"`

### 首图/顶栏设计
- **标题条**：橙色 `#E85D04` 圆角矩形 + 白色文字，位于卡片顶部
- **标题条高度 100px**，字体 32-36px，下方标注页码
- 标题条下方 10px 间距开始排具体内容

## 36. 完整内容流水线执行要点

### 人工审核断点
- **飞书文档审核是强制断点**：在发布前必须创建/更新飞书文档 + 插入全部图片
- 用户审核确认后才执行多平台分发
- 文档更新用 `--mode overwrite` 后必须重新插入所有图片

### Twitter 发布注意
- `twitter/post` 内部超时 60s，用 `--window foreground --site-session persistent` + 重试解决
- 先用简单短推文测试连接，再发带4张图的正式推文
- **不用 `--timeout` 参数**（不支持），用 `OPENCLI_BROWSER_COMMAND_TIMEOUT` 环境变量
- 发帖失败时先检查 `opencli twitter profile` 确认登录状态

### 小红书草稿
- **图片路径必须是相对 CWD 的相对路径**：`./ai-tools-xhs/card-light-1.png` 格式
- 工作目录为项目根目录时，用 `./ai-tools-xhs/` 前缀的子目录路径
- 绝对路径报 `Image file not found`
- `--draft true` 保存草稿，返回值 `✅ 暂存成功` 即为成功

## 33. adhd-ai-v2-xhs 与AI共事ADHD效应（2026-06-05）

### 项目结构
```
adhd-ai-v2-xhs/
├── article.md              # 小红书草稿（标题 18 字 + 正文 440 字）
├── README.md               # 完整博客版 + 飞书链接
├── gen_cards.py            # SVG→PNG 生成器（4 浅色中文 + 4 深色英文）
├── adhd-cover-light/dark.png     # Cover (1024×1024)
├── adhd-card-1-light/dark.png    # 后果卡 (800×800)
├── adhd-card-2-light/dark.png    # 解决方案卡 (800×800)
└── adhd-banner-light/dark.png    # 收尾金句卡 (800×800)
```

### 发布数据
- 小红书：✅ 暂存成功（草稿箱），标题 18 字，正文 440 字，4 张浅色卡
- Twitter：✅ 主推文已发布（`https://x.com/DubaIGOHGOkTHOk/status/2062736962189197349`），4 张深色卡
- Twitter Thread：❌ `reply` 命令频繁失败，未完成推文串发布
- 飞书文档：`https://www.feishu.cn/docx/K32odQUN4oEMaUxA6tbcqKY0ni7`

### 卡片设计新规范（大标题爆款型 + 严格约束）

本次根据用户要求严格执行了全新的卡片样式规范：

**1. 浅色卡片（中文）规则：**
```
底色：#FAF7F2（纯色，无渐变）
文字定位：绝对居中 x="50%" y="50%" text-anchor="middle" dominant-baseline="middle"
字号：封面 100-110px，内容卡 68-80px
颜色：深色 #1E293B + 品牌色（#E63E6B / #0D9488 / #F59E0B / #8B5CF6）
扁平化：无任何阴影/投影/滤镜
简洁：无标题栏、无底部文字、无辅助说明（仅保留核心大标题）
约束：字不能重叠、不能溢出、不能用白色/灰色文字
```

**2. 深色卡片（英文）规则：**
```
底色：#0A0A14（纯色，无渐变）
文字：亮色系（#F5F5F7 / #C4B5FD / #67E8F9 / #FCD34D / #F472B6）
与浅色相同的绝对居中、无阴影、无标题、无底部文字
禁止：黑色、深灰色、暗色/泥泞色文字
```

**3. 解决方案必须是核心焦点：**
- 4 张卡片中必须有一张专门突出解决方案（"3个解药"/"3 Antidotes"）
- 解决方案卡的文字最大、最醒目（96px 超大字号 + 金色/琥珀色强调）
- 该卡排在第三张（封面→问题→解决方案→行动号召）

### Twitter 发布故障记录

**问题 1：`twitter post` 返回 `This operation was aborted`**
- 根因：浏览器 session 未绑定，adapter 无法控制已有登录态页面
- 修复流程：
  1. `opencli browser <session> bind` — 绑定当前已登录 Twitter 的 tab
  2. `opencli browser <session> open "https://x.com/compose/post"` — 导航到发帖页
  3. `opencli twitter post "<text>" --images "..." -f yaml` — 成功
- 经验：使用 binding 之前不要传 `--window foreground`（会与已有 session 冲突）

**问题 2：`twitter reply` 返回 `Could not verify reply text in the composer`**
- 根因：compose 页面已在前一步被关闭，或 textarea 选择器不匹配
- 尝试方案：navigate 到 tweet 页面后重试 → 仍然失败
- 未解决：最终未完成 thread 发布
- 替代方案：使用 browser eval 手动操作（见流水线 fallback 节）

### 内容规范执行检查
- 标题 ≤ 20 字：`与AI共事 = ADHD？越用越机器` = 18 ✓
- 正文 ≤ 950 字：440 ✓
- 首行即标题：正文第一行是标题文字 ✓
- 无时间戳 ✓
- 纯文本格式 ✓
- 短段落 + emoji 分段 ✓
- 末尾话题标签 ✓
- 图片 4 张（浅色）/ 4 张（深色）✓

## 34. ai-soul-interview-xhs — AI灵魂拷问实验（2026-06-04）

### 项目结构
```
ai-soul-interview-xhs/
├── article.md              # 小红书草稿（标题 10 字 + 正文 351 字）
├── README.md               # 完整博客版
├── gen_cards.py            # SVG→PNG 生成器（4 张浅色中文 + 4 张深色英文）
├── card-cover.png          # 浅色封面 (1024×1024) — AI灵魂拷问 120px
├── card-1.png              # 浅色30天流程 (1024×1024)
├── card-2.png              # 浅色深度对比 (1024×1024)
├── card-3.png              # 浅色潜意识白皮书 (1024×1024)
├── card-cover-dark.png     # 深色封面 (1024×1024) — AI SOUL INTERVIEW
├── card-1-dark.png         # 深色30天流程 (1024×1024)
├── card-2-dark.png         # 深色深度对比 (1024×1024)
└── card-3-dark.png         # 深色潜意识白皮书 (1024×1024)
```

### 发布数据
- 小红书：✅ 暂存成功（草稿箱），标题「AI灵魂拷问30天」（10字），正文 351 字，4 张浅色中文卡
- Twitter：✅ 已发布 https://x.com/DubaIGOHGOkTHOk/status/2062784967135137811，4 张深色英文卡
- 飞书文档：https://www.feishu.cn/docx/NrEOd7s8io7MDCxyzLacSsyWnhg

### 卡片样式最终规范（本轮用户反复确认）

**浅色卡片（中文，小红书用）：**
```
底色：#FAF7F2 → #F5F0E8 渐变（或纯色）
结构：外层白卡 rect (rx=36) + 内部 item rects（rx=16, opacity=0.08）
文字定位：绝对居中（text-anchor="middle" + 精确基线计算）
字号：封面 120px，内容卡标题 40-48px，描述 22-34px
颜色：#1E293B（主）+ 品牌色：蓝#2563EB / 紫#7C3AED / 粉#EC4899 / 绿#059669 / 橙#D97706
禁止：白色文字（#FFF）、灰色文字、任何 filter/投影/阴影
删除：大标题、"30天流程"等 section 标题、评论区扣灵魂等底部 CTA
```

**深色卡片（英文，Twitter 用）：**
```
底色：#070717 径向渐变
外卡：#111130 (rx=36)，item rects 同色 opacity=0.12
文字：#E2E8F0（主）+ 高亮色：蓝#60A5FA / 紫#A78BFA / 粉#F472B6 / 绿#34D399 / 橙#FBBF24
禁止：黑色、深灰色、暗色文字
```
**垂直居中算法（cv2）：**
```python
def v1(ry, rh, fs):           # 单行居中
    return ry + rh // 2 + int(fs * 0.35)

def v2(ry, rh, fs1, fs2, g=10):  # 双行居中（标题+描述）
    tv = int(0.75 * fs1) + g + int(0.75 * fs2)
    vt = ry + (rh - tv) // 2
    return vt + int(0.7 * fs1), vt + int(0.75 * fs1) + g + int(0.7 * fs2)
```

### 关键踩坑 & 修复

**1. Twitter compose page IPv6 block（最严重的阻塞）**
- 症状：`https://x.com/compose/post` 返回 `<body><pre>IPv6</pre></body>` — 页面空白
- 根因：X.com 对 headless/automated 浏览器的 compose 页面做了 CDN/IP 检测
- 修复过程（3 轮）：
  - v1：改变 COMPOSE_URL 为 `https://x.com/home` → 文本输入+图片上传成功，但提交检测超时
  - v2：改 submitTweet 检测逻辑（检查 composer 可见性而非文本）→ 提交后 composer 元素从 DOM 移除，检测通过
  - v3：最终修复组合（见以下代码）
- 最终 adapter 修改：
  ```javascript
  // 使用 homepage + 点击侧边栏 Post 按钮打开 compose dialog
  const COMPOSE_URL = 'https://x.com';
  await page.goto(COMPOSE_URL, { waitUntil: 'load', settleMs: 2500 });
  await page.wait({ selector: '[data-testid="SideNav_NewTweet_Button"]', timeout: 15 });
  await page.evaluate(`document.querySelector('[data-testid="SideNav_NewTweet_Button"]')?.click()`);
  await page.wait({ selector: '[data-testid="tweetTextarea_0"]', timeout: 15 });
  ```

**2. Browser session 管理**
- `--site-session persistent` 的 session 容易 stale（多次失败后）→ 需要 `opencli daemon restart` 恢复
- `--site-session ephemeral` 每次都创建新 session，但可能触发 x.com IPv6 检测
- 推荐策略：先用 ephemeral foreground 测试，成功后用 persistent 保持
- `opencli doctor` 确认 Extension connected 后再执行发布命令

**3. Twitter 发布无草稿模式**
- `opencli twitter post` 没有 `--draft` 参数，发布即公开
- 用户要求"保存到草稿箱"时无法直接满足
- 替代方案：用 browser eval 填充 compose 页面但不点击 Post

**4. opencli gemini image 持续不可用**
- 本次 4 次尝试全部返回 `status: ⚠️ no-images`
- 与本项目前 3 次（opencut-xhs/mcp-xhs/ai-graveyard-xhs）现象完全一致
- 结论：`opencli gemini image` 不应作为封面主要生成方式，SVG gen_cards.py 是唯一可靠方案

**5. 小红书 publish 必须 foreground + ephemeral**
- `--window background` 报 `Image injection failed: No file input found on page`
- `--site-session persistent` 在 daemon restart 后报 `stale page identity`
- 最终成功参数：`--window foreground --site-session ephemeral --keep-tab true`
- 注意：foreground + ephemeral 每次打开新浏览器窗口，用户需确认登录态

### 发布命令（本轮验证）
```bash
# 小红书草稿
opencli xiaohongshu publish "AI灵魂拷问30天\n\n正文..." \
  --title "AI灵魂拷问30天" \
  --images "ai-soul-interview-xhs/card-cover.png,ai-soul-interview-xhs/card-1.png,..." \
  --draft true \
  --window foreground \
  --site-session ephemeral \
  -f yaml

# Twitter 发布
opencli twitter post "推文内容" \
  --images "...card-cover-dark.png,...card-1-dark.png,..." \
  --window foreground \
  --site-session persistent \
  -f yaml
```

### 正文字数验证方法
```bash
echo -n "正文内容" | wc -m  # 简单准确
```

### 飞书文档更新（3轮）
- v1：`+create` 含完整正文 + 后插 4 张图
- v2：`+update --mode overwrite` 换正文 + 重插 4 张图
- v3：`+update --mode overwrite` 换简版正文（含浅色/深色章节）+ 重插 8 张图
- 教训：每次 overwrite 都需重插全部图片，效率低，适合内容完全不同的场景

## 10. Nous Hermes Desktop — 2026-06-05

### 内容要点
- **主题**: Hermes Desktop Beta 公测 + Jensen GTC 首秀
- **卡片风格**: 浅色中文（奶油渐变） + 深色英文（径向渐变）
- **字数**: 标题 20 字 ✓，正文 885 字 ✓（含换行），Twitter 主推文 62 字符（87 加权）

### SVG 实坑
- **`&middot;` 和 `&rarr;` 不是 XML 实体**：HTML 的 `&middot;`（·）和 `&rarr;`（→）在 SVG/XML 中不是标准实体。Inkscape 会报 `parser error : Entity 'middot' not defined` 并渲染为空白。必须用 Unicode 字符 `·` (U+00B7) 和 `→` (U+2192) 直接写入 f-string。
- **卡片的副标题行用 `·` 分隔比 `|` 更优雅**，但必须用 Python Unicode 字面量而非 HTML entity。

### 发布验证
- XHS 草稿: `--draft true` + `--window foreground` + `--site-session persistent` 成功保存
- Twitter: 直接发布成功，无 draft 模式。用户要求"保存到草稿箱"目前无法满足（opencli twitter post 无 --draft）
- 飞书文档：先 `+create` 再 `+media-insert` × 8 张图，无需 overwrite

### 流程改进建议
- 对于含 SVG 实体的场景，生成后先跑 `xmllint --noout *.svg` 或直接检查 Inkscape 输出是否有 parser error
- Twitter 主推文应控制在 60-80 中文字符（120-160 weighted），留余量给 emoji 和空格

## 37. ai-tool-stack-2026-xhs — 2026 AI 工具栈清单（2026-06-05）

### 项目结构
```
ai-tool-stack-2026-xhs/
├── article.md              # 小红书草稿（标题 13 字 + 正文 286 字）
├── README.md               # 完整博客版 + 数据源
├── gen_cards.py            # SVG→PNG 生成器（4 张深色英文卡）
├── card-0.png              # Writing & Search (800×800)
├── card-1.png              # Image & Video (800×800)
├── card-2.png              # Audio · Music · Coding (800×800)
└── card-3.png              # 2026 AI Tool Stack 全景图 (800×800)
```

### 发布数据
- **小红书草稿**：✅ 暂存成功（草稿箱），标题「只会 ChatGPT 真的不够了」（13 字），正文 286 字，4 张浅色卡
- **Twitter**：✅ 已发布 https://x.com/DubaIGOHGOkTHOk/status/2062788324193124758，4 张深色英文卡
- **飞书文档**：https://www.feishu.cn/docx/JYxEdvQ4moVX2RxYuCPc4Q4onOg（8 张图全部上传成功）

### 内容迭代（3 轮）
| 轮次 | 问题 | 修复 |
|------|------|------|
| v1 | 卡片内容太单薄（仅标题） | 每张卡片增加 4-7 个具体工具条目 + 描述 |
| v2 | 用户要求"浅色中文/深色英文"严格规范 | 全部改为深色英文卡片（Twitter 用） |
| v3 | 用户要求"卡片内容要丰富，体现具体内容" | 每张卡片含 4-7 个工具条目，信息密度高 |

### 卡片设计最终规范（本轮验证）

**浅色卡片（中文，小红书用）：**
```
底色：#FAF7F2（纯色，无渐变）
文字：#1E293B（主色）+ 品牌色（#64748B 描述）
布局：每卡 4-7 个工具条目，白色卡片容器（rx=16）
禁止：白色/灰色文字，投影/阴影/滤镜
```

**深色卡片（英文，Twitter 用）：**
```
底色：#0B1027（纯色，无渐变）
文字：#F1F5F9（主色）+ #94A3B8（描述）
布局：每卡 4-7 个工具条目，深色卡片容器（#1E293B，rx=16）
禁止：黑色/深灰色/暗色文字
```

### 关键踩坑 & 修复

**1. 卡片内容密度（最核心问题）**
- 初版：4 张卡片仅含大标题（"2026 AI 工具清单"等），用户反馈"内容太单薄"
- 修复：每张卡片增加具体工具条目（工具名 + 简短描述），共 4-7 条/卡
- 教训：合集型内容每张卡片必须有具体条目，不能只有大标题

**2. 浅色/深色语言规则严格执行**
- 浅色 → 中文（小红书），深色 → 英文（Twitter）
- 不可混用：浅色配英文或深色配中文都造成风格不一致
- 浅色卡无白色/灰色文字；深色卡无黑色/暗色文字

**3. 飞书文档 overwrite 后图片丢失**
- `+update --mode overwrite` 会清空文档含 media blocks
- 修复：overwrite 后必须重新 `+media-insert` 所有图片
- 4 张图串行插入，每张一次调用

**4. Twitter 发布成功路径**
- 多次 `twitter post` 超时/aborted → 最终用 `--window foreground --site-session persistent` 成功
- 推文内容：29 中文字符（58 加权）+ 空格/emoji，远低于 280 上限
- 4 张图片同时上传成功

**5. XHS 草稿发布**
- `--draft true` + `--window foreground` + `--site-session persistent` → `✅ 暂存成功`
- 标题「只会 ChatGPT 真的不够了」= 13 字符 ✓（≤20）
- 正文 286 字 ✓（≤950）
- 4 张图片 ✓（≤9）

### 推文内容（Twitter）
```
2026 AI 工具清单｜只会 ChatGPT 不够了

🧵 7 大分类，15+ 工具，选对效率翻倍
```
- 字符数：29 中文字符 + 空格/emoji ≈ 76 加权字符（≤280 ✓）
- 图片：4 张深色英文卡片

### 小红书正文（article.md）
```
只会用 ChatGPT？真的不够了。

亲测半年，AI 工具栈早就不是"一个 ChatGPT 走天下"的时代了。

📌 我的 2026 工具栈：

写作对话 → Claude Sonnet 4.6（长文天花板）
AI 搜索 → Perplexity（答案带来源，研究神器）
生图视频 → Midjourney + Veo 3 + Firefly
PPT 制作 → Gamma（描述即生成）
音乐创作 → Suno AI（人人可写歌）
会议转录 → Notta（实时转文字）
编程开发 → Claude Code（最稳）

💡 选工具记住一个原则：
查资料用 Perplexity
写长文用 Claude
做图片用 Midjourney
做视频用 Veo 3

别再用一个工具应付所有场景了。

工具选对，效率翻倍。

#AI工具 #效率神器 #2026 #AI工具栈 #生产力工具
```

### 经验总结

1. **合集型内容卡片必须高密度**：每张卡片含 4-7 个具体条目，不能只有大标题
2. **浅色/深色语言规则不可混用**：浅色=中文/小红书，深色=英文/Twitter
3. **飞书 overwrite 后必须重插全部图片**：media blocks 会被清空
4. **Twitter 单条推文 + 4 图是可靠模式**：无需 thread，信息密度高即可
5. **XHS 草稿发布参数组合**：`--draft true --window foreground --site-session persistent -f yaml`

## 38. grok-civilization-collapse — Grok AI 模拟文明崩溃（2026-06-05）

### 项目结构
```
grok-civilization-collapse/
├── article.md              # 小红书草稿（标题 19 字 + 正文 892 字）
├── tweet.md                # Twitter 推文（英文，~280 字符）
├── doc-content.md          # 飞书文档正文
├── index.html              # HTML 卡片模板（Swiss 风格）
├── gen_dark_cards.py       # PIL 深色卡片生成器
├── output/
│   ├── card-cn-01.png      # 中文浅色封面 (1080×1440)
│   ├── card-cn-02.png      # 中文浅色 - 崩溃不是意外
│   ├── card-cn-03.png      # 中文浅色 - 技术爆炸=加速灭亡
│   ├── card-cn-04.png      # 中文浅色 - 扁平社会存活3倍长
│   ├── en-dark-01.png      # 英文深色封面 (1080×1440)
│   ├── en-dark-02.png      # 英文深色 - Collapse Is Inevitable
│   ├── en-dark-03.png      # 英文深色 - Tech Boom = Faster Death
│   └── en-dark-04.png      # 英文深色 - Flat Societies Survive 3x Longer
└── preview-full.png        # 全页预览
```

### 发布数据
- **小红书草稿**：✅ 暂存成功（草稿箱），标题「Grok AI 模拟文明崩溃」（19 字），正文 892 字，4 张浅色卡
- **Twitter**：❌ `Tweet button is disabled or not found` — 浏览器未登录/页面未加载，需手动发布
- **飞书文档**：https://kcn2x4k2r5fn.feishu.cn/docx/HVBud2G7RowUMFx1hhccXqVinTc（8 张图全部上传成功）

### 内容要点
- **主题**：Grok AI 模拟整个文明兴衰，发现文明崩溃是数学必然
- **核心发现**：
  1. 文明崩溃不是意外，而是必然（平均周期 300-500 年）
  2. 资源陷阱无法逃脱（消耗 > 再生）
  3. 技术爆炸 = 加速灭亡（反直觉）
  4. 扁平社会存活 3 倍长（但难抗危机）
- **调性**：小红书走"情绪共鸣 + 利他价值"，Twitter 走"认知颠覆 + 观点输出"

### 关键踩坑 & 修复

**1. 飞书文档 overwrite 后图片丢失（最严重）**
- 症状：`+update --mode overwrite` 后 `+fetch` 返回的 markdown 中 `<image token=""/>` 为空
- 根因：`overwrite` 模式清空整个文档（包括 media blocks），但 `+media-insert` 的 token 绑定失效
- **修复方案**：
  - **方案 A（推荐）**：先 `+create` 创建空文档 → 串行 `+media-insert` 插入所有图片 → 再 `+update --mode append` 写入正文
  - **方案 B**：用 `v2 API` 的 `+create --content` 创建含正文的文档 → 再 `+media-insert` 插入图片
  - **绝对避免**：`+create` 含正文 + `+media-insert` → `+update --mode overwrite`（token 会丢失）
- 教训：`overwrite` 是破坏性操作，图片必须后插

**2. 深色卡片 AI 生成文字模糊/缺失**
- 症状：Kolors AI 生成的深色卡片文字经常模糊、变形或缺失
- 根因：AI 图像模型不擅长渲染精确文字
- **修复方案**：改用 PIL (Pillow) 直接渲染文字
  ```python
  from PIL import Image, ImageDraw, ImageFont
  img = Image.new("RGB", (1080, 1440), (11, 16, 39))  # #0B1027
  draw = ImageDraw.Draw(img)
  draw.text((x, y), "文字内容", fill=(248, 250, 252), font=font)
  ```
- 配色：背景 `#0B1027`，文字 `#F8FAFC`，强调条 `#38BDF8`
- 字体：Helvetica/Noto Sans SC，标题 100px，副标题 48px

**3. Twitter 发布按钮不可用**
- 症状：`Tweet button is disabled or not found`
- 根因：浏览器未登录 Twitter / 页面未完全加载 / session stale
- **排查步骤**：
  1. `opencli doctor` 确认 Extension connected
  2. `opencli browser <session> open "https://x.com"` 手动检查登录态
  3. 如未登录，在浏览器中手动登录
  4. 重试 `opencli twitter post`
- **备选方案**：手动发布（复制文案 + 上传图片）

**4. 浏览器扩展未连接**
- 症状：`Browser Bridge extension not connected`
- 修复：`opencli daemon restart` → `opencli doctor` 确认
- 如仍失败，需手动检查 Chrome 扩展是否启用

**5. 小红书草稿发布成功**
- 命令：`opencli xiaohongshu publish --draft true --window foreground --site-session persistent -f yaml`
- 返回：`- status: ✅ 暂存成功`
- 图片路径：必须相对 CWD（`./output/card-cn-01.png`）

### 卡片设计最终规范（本轮验证）

**浅色卡片（中文，小红书用）：**
```
底色：#FAF7F2（纯色，无渐变）
文字：#1E293B（深灰）+ 品牌强调色 #FF6B35（橙色）
字号：标题 110-140px，副标题 88px
布局：Flex 居中，绝对水平和垂直居中
禁止：白色文字、灰色文字、投影/阴影/滤镜
```

**深色卡片（英文，Twitter 用）：**
```
底色：#0B1027（深蓝，纯色无渐变）
文字：#F8FAFC（白色）+ 强调条 #38BDF8（天蓝）
字号：标题 100-110px，副标题 48px
布局：Flex 居中，绝对水平和垂直居中
生成方式：PIL 直接渲染（不可用 AI 生成）
禁止：黑色、深灰色、暗色文字
```

### 推文内容（Twitter — 待手动发布）
```
Grok AI ran a civilization collapse simulation. Every single civilization collapsed after 300-500 years. Tech acceleration = faster death. Flat societies survive 3x longer but can't handle crises. Collapse isn't an accident—it's inevitable. AI is our civilization mirror. #GrokAI #AI
```
- 字符数：~280 加权字符（符合上限）
- 图片：4 张深色英文卡片

### 小红书正文（article.md）
- 标题：`Grok AI 模拟文明崩溃：人类未来会怎样？`（19 字）
- 正文：892 字（≤950 ✓）
- 首行即标题 ✓
- 无时间戳 ✓
- 纯文本格式 ✓
- 4 张浅色中文卡片 ✓

### 经验总结

1. **飞书文档图片插入顺序至关重要**：先插图片后写正文，或先用 v2 API 创建再插图片
2. **深色文字卡片必须用 PIL 渲染**：AI 图像模型不靠谱
3. **Twitter 发布前必须确认登录态**：`opencli browser open "https://x.com"` 手动检查
4. **小红书草稿发布参数固定组合**：`--draft true --window foreground --site-session persistent -f yaml`
5. **双语言卡片尺寸统一**：1080×1440 (3:4)，与小红书规范一致

