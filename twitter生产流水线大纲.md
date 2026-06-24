# Twitter (X) 生产流水线大纲

> ⚠️ **硬规则**：Agent 不得执行 Twitter 发布命令（见 AGENTS.md）。本文档所有 `opencli twitter` 命令仅为**参考命令**，发布由用户手动执行。

## 一、项目定位

- 社交媒体系列：Markdown 文章 + PNG 卡片
- 小红书投放：浅色中文卡
- Twitter 投放：深色英文卡（独立 gen_cards.py）
- 账号：@DubaIGOHGOkTHOk

## 二、核心约束

| 约束 | 值 |
|------|------|
| 字数 | ~140 字（CJK=2, ASCII=1, emoji=2） |
| 图片 | ≤ 4 张/推 |
| Thread | 用户已确认**不发 Thread**，只发单条推文 |

## 三、卡片规范

### 深色英文卡
- 底色：`#0B1027`（纯色，无渐变）
- 文字：`#F8FAFC`（主色）+ 强调色 `#7C3AED`/`#38BDF8`/`#F59E0B`/`#F472B6`
- 字体：Helvetica/Noto Sans SC
- 标题：100px，副标题：48px
- 布局：Flex 居中，文字绝对水平和垂直居中
- 尺寸：1080×1440 (3:4)，与小红书卡片一致

### XHS vs Twitter 卡片关系
- **通常不同**：XHS 浅色中文，Twitter 深色英文
- 一套 gen_cards.py 可同时包含 light + dark 两组函数
- 内容对应但不完全相同：中文走痛点→方案→数据线，英文走 why→how→结论线
- 适用场景："信息差/红利"类中国本土话题的 Twitter 出海适配

### 生成方式
- 封面和中文卡：SVG + Inkscape（中文卡片必须用 SVG）
- 英文卡：PIL (Pillow) 直接渲染（文字清晰度高）
- `opencli gemini image` 不可靠，封面必须由 gen_cards.py 生成

## 四、发布命令（参考）

### 单条推文 + 4 图
```bash
opencli twitter post "<text>" --images "i1.png,i2.png,i3.png,i4.png" --window foreground -f yaml
```

### Browser eval 方案（100% 可靠）
```bash
# 步骤：
# 1. goto compose page
# 2. fill tweetTextarea_0
# 3. click tweetButtonInline
opencli browser <session> type "<ref>" "<text>" --target tweetTextarea_0
opencli browser <session> click "<ref>" --target tweetButtonInline
```

### 首次发布绑定
```bash
opencli twitter bind --window foreground
# 绑定后不要传 --window foreground（与绑定 session 冲突）
```

## 五、已知坑点

### compose 选择器
| 场景 | 选择器 |
|------|--------|
| 推文编辑器 | `[data-testid="tweetTextarea_0"]` |
| 发布按钮 | `button[data-testid="tweetButtonInline"]` |
| 新建推文按钮 | `[data-testid="SideNav_NewTweet_Button"]` |

### 发布按钮不可用
- X.com 常被代理/CDN 阻断 → `ERR_PROXY_CONNECTION_FAILED`
- 用户网络问题，非 Agent 问题

### compose 页面 IPv6 屏蔽
- 某些网络环境下 IPv6 被屏蔽 → 编辑框空白
- 修复：`opencli browser <session> eval "document.querySelector('[data-testid=tweetTextarea_0]').style.display='block'"`

### 超时处理
- 默认 60s 超时
- 可设 `OPENCLI_BROWSER_COMMAND_TIMEOUT=120000`

### Session 管理
- `--site-session persistent`：跨命令复用登录态
- Binding 模式：首次绑定后不传 `--window foreground`

### 适配器问题
- `twitter delete`：❌ buggy，找不到菜单选择器
- `twitter reply`：多行中文失败 → 用单行或 browser eval

### 批量发布脚本
- `batch_post_twitter.py`：已执行 36/37 个 topic
- `post_remaining.sh`：仅剩 1 个 topic 未发布

## 六、参考文献

- `AGENTS.md` — 硬规则入口
- `MEMORY.md` — 案例记录 + 踩坑沉淀
- `小红书生产流水线大纲.md` — XHS 核心规范
