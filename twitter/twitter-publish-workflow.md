# Twitter (X) 发布工作流

## 前置条件

- 浏览器已登录 X.com（账号：@DubaIGOHGOkTHOk）
- Browser Bridge 扩展已连接
- `opencli` 可用

## 发布单条推文（带图片）

```bash
# text: 推文正文（≤140 汉字 / ≤280 加权字符）
# --images: 最多 4 张，逗号分隔，路径相对 CWD
# --window foreground: 必须前台窗口
# --site-session persistent: 复用登录态

opencli twitter post "推文内容" \
  --images "img1.png,img2.png,img3.png,img4.png" \
  --window foreground \
  --site-session persistent \
  -f yaml
```

成功返回示例：
```yaml
- status: success
  message: Tweet posted successfully.
  text: "..."
  id: '2062136855613862169'
  url: https://x.com/account/status/2062136855613862169
```

## 发布 Thread（多条推文）

```bash
# 1. 发首条推文
opencli twitter post "标题推文" \
  --images "..." \
  --window foreground \
  --site-session persistent \
  -f yaml

# 2. 用首条 URL 逐条回复
opencli twitter reply "<首条URL>" "回复内容" \
  --window foreground \
  --site-session persistent \
  -f yaml
```

## 字符限制

| 类型 | 限制 |
|------|------|
| 中文（CJK） | 每个字计 2 字符，最多 ~140 汉字 |
| 英文/数字/空格 | 每个计 1 字符 |
| Emoji | 每个计 2 字符 |
| 总上限 | 280 加权字符 |

快速估算：`中文字符 × 2 + ASCII 字符数 ≤ 280`

## XHS 内容 → Twitter 适配

| 维度 | XHS | Twitter |
|------|-----|---------|
| 字数 | ≤950 字 | ≤140 汉字 |
| 图片 | ≤9 张 | ≤4 张 |
| 风格 | 口语化、emoji 丰富 | 简洁短句、信息密度高 |
| 话题 | `#话题` 标签 | `#Tag` 标签 |

适配策略：
- 提取核心亮点（最多 3 个），每条一句话
- 保留最吸引人的 1 张封面 + 3 张内容卡
- 末尾加安装命令 + 话题标签
- 删除 XHS 特有的"评论区聊聊""宝子们"等引导语

## 可用命令一览

| 命令 | 功能 | 策略 |
|------|------|------|
| `twitter post` | 发推文/thread | UI |
| `twitter reply` | 回复推文 | UI |
| `twitter quote` | 引用转推 | UI |
| `twitter delete` | 删推文（❌ buggy） | UI |
| `twitter thread` | 读取 thread | COOKIE |
| `twitter timeline` | 读取时间线 | COOKIE |
| `twitter search` | 搜索推文 | COOKIE |

## 故障处理

### `Tweet button is disabled`
原因：文本超 280 加权字符
解决：缩短文本

### `--window background` 超时
原因：后台窗口无法操作 UI
解决：改用 `--window foreground`

### 适配器验证失败 fallback
```javascript
// 手动填充并发布
const tb = document.querySelector('[data-testid=tweetTextarea_0]');
tb.focus();
tb.textContent = '';
document.execCommand('insertText', false, '🔥 推文内容');
tb.dispatchEvent(new Event('input', {bubbles: true}));
const btn = document.querySelector('[data-testid=tweetButton]');
if (btn && !btn.disabled) btn.click();
```

## compose button 选择器

| 选择器 | 位置 |
|--------|------|
| `[data-testid=SideNav_NewTweet_Button]` | 侧边栏"发帖"按钮 |
| `[data-testid=tweetButton]` | 对话框内的"发帖"按钮 |
| `[data-testid=tweetButtonInline]` | 主页时间线内嵌"发帖"按钮 |
