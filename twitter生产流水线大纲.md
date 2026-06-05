# 003-Twitter Twitter/X 内容生产流水线

## 一、项目定位
- 将 XHS `-xhs/` 文件夹内容适配后发布到 X/Twitter（账号 `@DubaIGOHGOkTHOk`）
- 选题来源：XHS 内容二转 / `twitter-ai-top50.md` 热榜追踪 / 独立原创
- 两种输出形式：**单条推文 + 图片** 和 **Thread 推文串**
- 卡片复用 XHS 生成的 PNG，或独立制作 Twitter 风格卡（深色/英文居多）
- 仓库：`https://github.com/thehejian/xiaohongshu.git`

## 二、核心工具链

| 工具 | 用途 | 关键约束 |
|------|------|----------|
| **opencli** | 浏览器自动化发推 | `twitter post`/`reply`，必须 `--window foreground` |
| **Python 3** | 批量发布脚本、字符计数 | `batch_post_twitter.py`、`check_char_count()` |
| **Playwright/Puppeteer** | HTML→PNG 卡片渲染（非 Inkscape 方案） | 需本地 Chrome，`npm install` |
| **PIL/Pillow** (按需) | 纯 Python 生成 PNG 卡片 | `generate_cards.py`，无 Inkscape 依赖 |
| **Inkscape 1.4+** | SVG→PNG 栅格化（XHS 复用） | 与 XHS 共享 |
| **浏览器桥接扩展** | opencli 控制真实 Chrome | 每次会话前确认扩展已连接 |

## 三、完整生产流水线

```
待办.txt / twitter-ai-top50.md 选题
    ↓
① 内容适配（XHS → Twitter）
   ├── XHS body ~950字 → ≤280 加权字符（约 140 汉字）
   ├── 提取 2-4 张最佳卡片（square/cover + 内容卡）
   ├── 删除"姐妹们""评论区聊聊"等 XHS 口语
   ├── 改用 Twitter 短句 + 换行呼吸感
   └── 末尾 2-4 个 #Tag
    ↓
② 卡片准备
   ├── 复用 XHS 目录已有 PNG（img1.png, img2.png...）
   ├── 路径相对 CWD，最多 4 张
   └── 缺失时用 Playwright/Inkscape 独立生成
    ↓
③ 发布
   ├── 单条: opencli twitter post --images "..."
   ├── Thread: 首条 post → 逐条 reply
   └── 批量: batch_post_twitter.py / post_remaining.sh（2min 间隔）
    ↓
④ 验证
   └── opencli twitter timeline / thread 确认发布成功
```

### 批量发布脚本

**Python 版**（`batch_post_twitter.py`）：
```bash
python3 batch_post_twitter.py
```
- 37 个 topic 的推文 + 图片预配置
- 自动校验加权字符数 ≤ 280，超限中止
- `START_INDEX` 变量支持断点续发
- 每帖间隔 120s

**Bash 版**（`post_remaining.sh`）：
```bash
bash post_remaining.sh
```
- 手动维护 11 个 topic
- 每帖 `sleep 120` 间隔

## 四、字符计数规则（Twitter 加权字符）

| 类型 | 权重 | 上限 |
|------|------|------|
| CJK 中文字符 | 2 | ~140 汉字 |
| ASCII（字母/数字/空格） | 1 | 280 |
| Emoji | 2 | — |

```python
def check_char_count(text):
    count = 0
    for c in text:
        if ord(c) > 0x2E80:  # CJK range
            count += 2
        else:
            count += 1
    return count
```

快速估算：`中文字符数 × 2 + ASCII 字符数 ≤ 280`

## 五、XHS → Twitter 适配规则

| 维度 | XHS | Twitter |
|------|-----|---------|
| 字数 | ≤950 字 | ≤140 汉字 / ≤280 加权 |
| 图片 | ≤9 张 | ≤4 张 |
| 风格 | 口语化、emoji 丰富、姐妹向 | 简洁短句、信息密度高、认知输出 |
| 话题 | 正文 `#标签` / `--topics` | 正文尾部 `#Tag` |
| 结构 | 痛点→干货→CTA | Hook→展开→反问/金句 |

策略：
- 保留核心亮点最多 3 个，每条一句话
- 选 1 张封面 + 2-3 张内容卡
- 删 XHS 引导语（"评论区聊聊""宝子们""亲测"）
- **SVG 中禁止 HTML entity**（如 `&middot;`）— 改用 Unicode 字面量
- 用 `\n` 换行营造呼吸感

## 六、发布命令

### 单条推文
```bash
opencli twitter post "<text>" \
  --images "img1.png,img2.png,img3.png,img4.png" \
  --window foreground \
  --site-session persistent \
  -f yaml
```
- `\n` 在 text 中直接支持换行，无需特殊处理
- 图片路径相对 CWD，最多 4 张

### Thread 推文串
```bash
# 首条
opencli twitter post "首条推文" --images "..." --window foreground -f yaml
# → 返回 url: https://x.com/.../status/<id>

# 续推文（逐条回复）
opencli twitter reply "<url>" "回复内容" --window foreground -f yaml
```

线程建议：首条 ≤140 汉字带图，每条回复 1-2 观点，总条数 ≤10（超长被折叠）。

### 命令一览

| 命令 | 功能 | 策略 | 可用性 |
|------|------|------|--------|
| `twitter post` | 发推文 | UI | ✅ 必须 `--window foreground` |
| `twitter reply` | 回复/续 thread | UI | ✅ 同上 |
| `twitter quote` | 引用转推 | UI | ✅ |
| `twitter delete` | 删推文 | UI | ❌ buggy，找不到菜单选择器 |
| `twitter thread` | 读取 thread | COOKIE | ✅ 只读 |
| `twitter timeline` | 读取时间线 | COOKIE | ✅ |
| `twitter search` | 搜索推文 | COOKIE | ✅ |

## 七、写作规范

### 调性要求
- **观点输出**：不是描述产品，是输出认知（"这不是省钱的故事，这是认知差的故事"）
- **认知颠覆**：打破读者固有认知
- **犀利精炼**：每句话有信息量，不废话

### 结构模板（Hook → 展开 → 收尾）
```
主推文（≤140字，第一句 1 秒抓眼球）
   ↓
对比/冲突/反常识开头
  "考公面试班8000块，AI面试模拟49块。我选了后者。"
   ↓
展开（2-3 句核心观点）
  "这不是省钱的故事。这是认知差的故事。"
  "真人老师会累，会敷衍。AI不会。"
   ↓
反问/金句收尾
  "考公面试班8000块，AI面试模拟49块。你选哪个？"
```

### 格式
- 多用换行留白，每段 1-2 行
- 尾部 2-4 个 `#Tag`
- 不用"首先/其次/最后/总之"
- 不用营销词（"重磅""炸裂""神器"）

## 八、卡片生成方案

Twitter 发布复用 XHS 生成的卡片，但部分场景需要独立生成：

| 方案 | 工具 | 适用场景 | 示例 |
|------|------|----------|------|
| **复用 XHS PNG** | XHS gen_cards.py | 标准 XHS→Twitter 二转 | 37 个批量发布 topic |
| **Python SVG + Inkscape** | Python f-string + Inkscape | 独立 Twitter 内容 | `openrouter-top10/` 9 张 800×800 |
| **HTML + Playwright** | Node.js + Chromium | 多页图文、双语言 | `grok-civilization-collapse/` 8 张 1080×1440 |
| **PIL 直接渲染** | Python PIL/Pillow | 简单文字卡片 | `codex-plugin-deep-dive/` 8 张 1080×1080 |

### Twitter 专用卡片规格
- 尺寸：800×800、1024×1024、1080×1080、1792×1024（banner）
- 风格偏好：深色底（`#0B1027`/`#0F0F23`）+ 英文标题 + 品牌色强调
- 引用和 filter 规则与 XHS SVG 一致（`&` → `&amp;`，无 `100%` 尺寸）

## 九、已知坑点

### 发布限制
- `--window background` 不可用 → 必须 foreground
- 文本超 280 加权字符 → `Tweet button is disabled`
- `--images` 超过 4 张 → 适配器报错

### 适配器问题
- `twitter delete` 找不到菜单选择器 → 手动 eval 替代
- React 重新渲染后 ref 编号变化 → 用 CSS 选择器代替 ref

### 首次发布故障处理（2026-06-05 验证）

**场景：** `twitter post` 一直返回 `This operation was aborted`

**根因：** 没有绑定浏览器 session，adapter 无法定位已登录 tab

**修复流程：**
```bash
# 1. 绑定已有登录态 tab
opencli browser <session> bind

# 2. 导航到发帖页
opencli browser <session> open "https://x.com/compose/post"

# 3. 正常发布
opencli twitter post "<text>" --images "..." -f yaml
```
- 绑定后**不要**传 `--window foreground`（与绑定 session 冲突）

**场景：** `twitter reply` 返回 `Could not verify reply text in the composer after typing`

**根因：** compose 页面已关闭或 textarea 选择器不匹配

**替代方案（eval fallback）：**
```bash
# 导航到 tweet 页
opencli browser <session> open "https://x.com/.../status/<id>"

# 用 eval 找到并点击回复按钮
opencli browser <session> eval 'document.querySelector(\'[data-testid="reply"]\').click()'

# 等待输入框出现，插入文本
opencli browser <session> eval '
  const tb = document.querySelector(\'[data-testid="tweetTextarea_0"]\');
  if (tb) { tb.focus(); document.execCommand("insertText", false, "回复内容"); }
'

# 点击发布
opencli browser <session> click '[data-testid="tweetButton"]'
```

### Thread 回复踩坑（2026-06-05 obsidian-agent-xhs 验证）

**1. 多行中文回复失败**
- `twitter reply` 对多行中文文本（含换行符）经常失败
- 错误信息：`Could not verify reply text in the composer after typing`
- 解决方案：使用单行英文/短中文句，避免换行
- 实测成功率：英文单行 100% > 中文单行 80% > 多行中文 0%

**2. Emoji 导致 reply 验证失败（2026-06-04 codex-plugin-deep-dive 验证）**
- `1/4 🏗` 等 emoji 字符可能导致 verification 失败
- 解决方案：用 ASCII 符号替代（`->` 代替 `→`，去掉 emoji）

**3. 需要 inter-tweet 延时**
- 主推文发布后不能立即 reply
- 首条 reply 至少等 3 秒（实测 `sleep 3` 足够，不一定要 60s）
- 不足时返回 `Could not verify reply text in the composer after typing`
- 推荐：`sleep 3` 后重试即成功

**4. Thread 暂未完整发布时的处理**
- 当 thread 中途被打断（如主推文已发但 reply 未完成），下次会话可继续：
  ```bash
  opencli twitter reply "<已有主推文url>" "<下一条内容>" --window foreground -f yaml
  ```
- 无需重新发主推文

**3. 推荐 Thread 发布节奏**
```
主推文 post（带图）
  → sleep 60s
  → reply #2（英文单行）
  → sleep 30s  
  → reply #3（英文/中文单行）
  → sleep 20s
  → reply #4（英文单行）
```
- 每条保持独立完整的观点
- 有换行/中文长句的场景用 browser eval fallback

### 卡片样式规范（2026-06-05 新增）
- 深色卡片（英文，Twitter 用）：底色 `#0A0A14`，亮色文字（`#F5F5F7`/`#C4B5FD`/`#67E8F9`/`#FCD34D`/`#F472B6`）
- 禁止黑色/深灰色/暗色文字，必须用高亮浅色系
- 绝对居中、无阴影、无标题栏、无底部文字
- 与 XHS 浅色卡片共用 `gen_cards.py`（light + dark 两组函数）

**合集型内容卡片密度规范（2026-06-05 ai-tool-stack-2026-xhs 验证）：**
- 每张卡片必须有具体条目（工具名 + 简短点评），不能只有大标题
- 每张卡片 4-7 个具体条目，使用垂直列表或 2×2 网格布局
- 条目太多时拆分为多张卡片（每张 3-6 条），共 4 张
- 浅色/深色语言规则不可混用：浅色=中文/小红书，深色=英文/Twitter

### 单条推文 + 4 图发布模式（2026-06-05 验证）
- **适用场景**：合集型/清单型内容，信息密度高，无需 thread
- **推文内容**：控制在 60-80 中文字符（120-160 加权），远低于 280 上限
- **图片数量**：4 张深色英文卡片（800×800）
- **发布命令**：
  ```bash
  opencli twitter post "<text>" \
    --images "card-0.png,card-1.png,card-2.png,card-3.png" \
    --window foreground \
    --site-session persistent \
    -f yaml
  ```
- **优势**：无需 thread 发布，无需延时，一次成功率高
- **推文示例**：
  ```
  2026 AI 工具清单｜只会 ChatGPT 不够了

  🧵 7 大分类，15+ 工具，选对效率翻倍
  ```
  （29 中文字符 + 空格/emoji ≈ 76 加权字符）

### 故障处理 fallback

#### Twitter 发布按钮不可用（2026-06-05 grok-civilization-collapse 验证）
- **症状**：`Tweet button is disabled or not found`
- **根因**：浏览器未登录 Twitter / 页面未完全加载 / session stale
- **排查步骤**：
  1. `opencli doctor` 确认 Extension connected
  2. `opencli browser <session> open "https://x.com"` 手动检查登录态
  3. 如未登录，在浏览器中手动登录
  4. 重试 `opencli twitter post`
- **备选方案**：手动发布（复制文案 + 上传图片）

#### 深色卡片文字渲染（2026-06-05 grok-civilization-collapse 验证）
- **AI 生成图片（Kolors 等）文字经常模糊或缺失** — 不可靠用于文字卡片
- **推荐方案**：PIL (Pillow) 直接渲染文字，确保 100% 清晰
- **生成脚本**：`gen_dark_cards.py` — Python PIL 生成深色卡片
- **配色**：背景 `#0B1027`，文字 `#F8FAFC`，强调条 `#38BDF8`
- **字体**：Helvetica/Noto Sans SC，标题 100px，副标题 48px
- **尺寸**：1080×1440 (3:4)

#### 超时处理
- `twitter/post` 内部超时 60s，不支持 `--timeout` 参数
- 重试方法：`--window foreground --site-session persistent --keep-tab true` + 多次重试
- 也可用 `OPENCLI_BROWSER_COMMAND_TIMEOUT=180` 环境变量（但偶现 `aborted` 错误）
- **先确认登录状态**：`opencli twitter profile` 验证后再发帖

#### 备用发帖方案
当 `twitter post/reply` 验证失败时，直接用 browser eval 操作：
```javascript
const tb = document.querySelector('[data-testid=tweetTextarea_0]');
tb.focus();
tb.textContent = '';
document.execCommand('insertText', false, '🔥 推文内容');
tb.dispatchEvent(new Event('input', {bubbles: true}));
const btn = document.querySelector('[data-testid=tweetButton]');
if (btn && !btn.disabled) btn.click();
```

### compose button CSS 选择器
| 选择器 | 位置 |
|--------|------|
| `[data-testid=SideNav_NewTweet_Button]` | 侧边栏"发帖" |
| `[data-testid=tweetButton]` | 对话框内"发帖" |
| `[data-testid=tweetButtonInline]` | 时间线内嵌"发帖" |

### 网络问题
- GitHub push 失败（`Failed to connect` / `HTTP2 framing error`）→ retry 即可

### compose 页面 IPv6 屏蔽（2026-06-04 修复）
- `https://x.com/compose/post` 被 X.com CDN/IP 检测屏蔽 → 返回 `<pre>IPv6</pre>` 空白页
- **修复方案**：导航到 `https://x.com` 首页 → 点击 `[data-testid="SideNav_NewTweet_Button"]` → 用模态对话框发帖
- submit 检测适配：模态关闭后 composer 从 DOM 移除，检查 `boxes.length > 0`（可见性）而非仅检查文本内容
- 此修复已验证通过

### Twitter 无草稿模式
- `opencli twitter post` 没有 `--draft` 参数，发布即公开
- 用户要求"暂存为草稿"时无法满足

### browser session 管理
- `--site-session persistent` 的 session 容易 stale（多次失败后），需 `opencli daemon restart` 恢复
- `--site-session ephemeral` 可能触发 IPv6 检测
- 推荐策略：ephemeral foreground 测试通过后，用 persistent 保持
- 执行发布前必须 `opencli doctor` 确认 Extension connected

## 八、参考文献
- `小红书生产流水线大纲.md` — XHS 完整流水线（含卡片设计语言、爆款写作）
- `MEMORY.md` #32 — AI老人语录红利项目经验（Twitter 单条发布验证）
- `batch_post_twitter.py` — 批量发布脚本（37 topic）
- `post_remaining.sh` — 剩余 topic shell 发布脚本
- `twitter/twitter-publish-workflow.md` — 原始 Twitter 发布工作流
- `twitter-ai-top50.md` — 热榜选题参考
