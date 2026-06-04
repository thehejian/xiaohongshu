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

### 故障处理 fallback
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

## 十、参考文献
- `小红书生产流水线大纲.md` — XHS 完整流水线（含卡片设计语言、爆款写作）
- `MEMORY.md` #28-#30 — Twitter 发布详细踩坑记录
- `batch_post_twitter.py` — 批量发布脚本（37 topic）
- `post_remaining.sh` — 剩余 topic shell 发布脚本
- `twitter/twitter-publish-workflow.md` — 原始 Twitter 发布工作流
- `twitter-ai-top50.md` — 热榜选题参考
