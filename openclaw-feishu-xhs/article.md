# 小红书草稿 - OpenClaw 对接飞书

> AI 个人助手接入飞书，一个命令搞定

---

## 📋 标题

```
AI助手接入飞书绝了
```

---

## 📋 正文（直接复制，小红书自动分段，标题在首行）

```
AI助手接入飞书绝了

打工人的终极理想出现了 👇

把 AI 直接装进飞书会怎样？
不用切 App、不用开网页
在群里 @一下就能干活

来说说 OpenClaw + 飞书 🔥

一个开源的 AI 个人助手
30+ 平台都支持（Claude/GPT/本地模型）
但最绝的是对飞书生态的支持 😎

它能干什么？
直接看图 👇

💬 消息：在群里 @ 它，自动回私聊/群聊
📄 文档：让 AI 帮你写飞书文档
📊 多维表格：跟 AI 说一声就建好
📅 日历：查日程建会议一条龙
✅ 任务：安排待办自动跟踪

安装就两步：

第一步，装 OpenClaw
npm i -g openclaw

第二步，飞书登录
openclaw channels login --channel feishu

完事。WebSocket 直连，不需要公网服务器 🚀

另外飞书官方还出了插件
npm i @larksuite/openclaw-lark
字节飞书团队自己维护的
文档/表格/日历/任务全覆盖

三个让我觉得离谱的点：

① 流式卡片输出 ——
AI 一边思考一边显示
不是傻等转圈圈

② 交互式确认按钮 ——
操作前问你是不是确定
手滑 AI 帮你按撤回？

③ DM 和群聊权限分离 ——
私聊随便调，群里只响应 @
不会被刷屏

飞书用户 + AI 玩家
这套组合拳值得一试 👊

👇 你现在用飞书做啥？评论区聊聊
```

---

## 🖼️ 图片

| 顺序 | 文件 |
|------|------|
| 1 | `openclaw-square.png` |
| 2 | `openclaw-card-1.png` |
| 3 | `openclaw-card-2.png` |
| 4 | `openclaw-banner.png` |

---

## 🎯 发布命令

```bash
BODY='AI助手接入飞书绝了

打工人的终极理想出现了 👇

把 AI 直接装进飞书会怎样？
不用切 App、不用开网页
在群里 @一下就能干活

来说说 OpenClaw + 飞书 🔥

一个开源的 AI 个人助手
30+ 平台都支持（Claude/GPT/本地模型）
但最绝的是对飞书生态的支持 😎

它能干什么？
直接看图 👇

💬 消息：在群里 @ 它，自动回私聊/群聊
📄 文档：让 AI 帮你写飞书文档
📊 多维表格：跟 AI 说一声就建好
📅 日历：查日程建会议一条龙
✅ 任务：安排待办自动跟踪

安装就两步：

第一步，装 OpenClaw
npm i -g openclaw

第二步，飞书登录
openclaw channels login --channel feishu

完事。WebSocket 直连，不需要公网服务器 🚀

另外飞书官方还出了插件
npm i @larksuite/openclaw-lark
字节飞书团队自己维护的
文档/表格/日历/任务全覆盖

三个让我觉得离谱的点：

① 流式卡片输出 ——
AI 一边思考一边显示
不是傻等转圈圈

② 交互式确认按钮 ——
操作前问你是不是确定
手滑 AI 帮你按撤回？

③ DM 和群聊权限分离 ——
私聊随便调，群里只响应 @
不会被刷屏

飞书用户 + AI 玩家
这套组合拳值得一试 👊

👇 你现在用飞书做啥？评论区聊聊'

opencli xiaohongshu publish "$BODY" \
  --title "" \
  --images "openclaw-square.png,openclaw-card-1.png,openclaw-card-2.png,openclaw-banner.png" \
  --topics "OpenClaw,飞书,AI助手,效率工具,开源,自动化,Feishu" \
  --draft true \
  --window foreground \
  --site-session persistent \
  -f yaml
```