# AI助手接入飞书绝了 🔥

> 小红书风格文章 · 2026-06-03
> OpenClaw: https://openclaw.ai
> 飞书官方插件: https://github.com/larksuite/openclaw-lark
> OpenClaw 飞书文档: https://docs.openclaw.ai/zh-CN/channels/feishu
> 飞书预览: https://www.feishu.cn/docx/QNEWdBRmboIuVmxMtzcceAYNn3b

## 📖 文章正文

打工人的终极理想出现了 👇

把 AI 直接装进飞书会怎样？不用切 App、不用开网页，在群里 @ 一下就能干活。

**OpenClaw** — 一个开源自托管的 AI 个人助手，由 PSPDFKit 创始人 Peter Steinberger 创建。支持 Claude、GPT 以及本地模型共 30+ 平台，但对 **飞书生态的支持** 是最大的亮点。

---

### 🚀 安装：两步搞定

```bash
# 第一步：安装 OpenClaw
npm i -g openclaw

# 第二步：飞书登录
openclaw channels login --channel feishu

# 重启网关
openclaw gateway restart
```

配置完成后，直接在飞书里 @ 机器人就能对话。**WebSocket 直连**，不需要公网服务器。

### 📦 飞书官方插件

字节跳动飞书团队还维护了官方插件 `@larksuite/openclaw-lark`：

```bash
npm i @larksuite/openclaw-lark
```

覆盖领域：

| 领域 | 能力 |
|------|------|
| **消息** 💬 | 读写私聊/群聊、回复线程、搜索消息、下载文件 |
| **文档** 📄 | 创建、更新、读取飞书文档 |
| **多维表格** 📊 | 管理 Base、表、字段、记录、视图 |
| **电子表格** 📈 | 创建、编辑、查看 |
| **日历** 📅 | 管理日程、参会人、忙闲查询 |
| **任务** ✅ | 创建/查询/更新/完成任务、子任务、评论 |
| **交互式卡片** 🃏 | 实时状态更新 + 确认按钮 |

---

### 💎 三大亮点

**1️⃣ 流式卡片输出 🌊**

AI 一边思考一边在飞书卡片上实时输出文本，不用盯着转圈圈等结果。

**2️⃣ 交互式确认按钮 🔘**

敏感操作前显示「确认/取消」按钮，防止手滑。AI 做了不该做的事？你自己点的确认 😂

**3️⃣ 灵活的权限策略 🔒**

- `dmPolicy`: 私聊策略（配对/白名单/全开/禁用）
- `groupPolicy`: 群聊策略（全开/白名单/禁用）
- `requireMention`: 是否需要 @ 才响应

私聊随便调，群里只响应 @，不会被刷屏。

---

### ⚙️ 核心配置

| 参数 | 说明 |
|------|------|
| `streaming: true` | 流式卡片输出（默认开启） |
| `requireMention: true` | 群聊需 @ 才响应 |
| 多账号支持 | 同时接入多个飞书账号 |
| ACP 会话 | Agent 间协作会话 |
| 多 Agent 路由 | 按场景路由到不同 Agent |

支持 DM 和群聊两种模式，`user` / `bot` 双身份，灵活可控。

---

<callout emoji="💡" background-color="light-blue" border-color="blue">

**飞书用户 + AI 玩家必试。** 这套组合拳够丝滑 😎

</callout>

**你现在用飞书做啥？评论区聊聊 👇**

`#OpenClaw` `#飞书` `#AI助手` `#效率工具` `#开源` `#自动化` `#Feishu` `#Lark`

---

## 📂 文件清单

| 文件 | 说明 |
|------|------|
| `README.md` | 本文(文章 + 描述) |
| `article.md` | 小红书草稿 |
| `gen_cards.py` | SVG 卡片生成器 |
| `openclaw-square.png` | 方版封面 (1024×1024) |
| `openclaw-card-1.png` | 功能卡片1 (1024×1024) |
| `openclaw-card-2.png` | 功能卡片2 (1024×1024) |
| `openclaw-banner.png` | 横版配图 (1792×1024) |

## 🔗 相关链接

- OpenClaw 官网: https://openclaw.ai
- GitHub: https://github.com/openclaw/openclaw
- 中文站: https://openclaw.cc
- 飞书官方插件: https://github.com/larksuite/openclaw-lark
- OpenClaw 飞书文档: https://docs.openclaw.ai/zh-CN/channels/feishu
- 安装: `npm i -g openclaw`