# 小红书草稿 — Hermes 🤝 飞书：AI管家接管飞书后台

> 飞书文档：https://www.feishu.cn/docx/FZWbdvIlxoGnagxIl1icr0klnTf

---

## 📋 标题

```
Hermes对接飞书，7个场景看傻
```

---

## 📋 正文（直接复制）

```
Hermes对接飞书，7个场景看傻 🤯

最近一直在找能长期跑在后台的 AI 助手
试了一圈终于找到绝配组合

Hermes Agent + 飞书 = 王炸 💥

简单说：
Hermes 是你服务器上的 AI 管家
飞书是你团队的工作台
管家帮你管工作台，不用你动手

👇 7 个场景，个个实用

① 先说清楚它不干什么
不是聊天机器人，不是代码助手
它是一个自主 Agent
你跟它说需求，它自己去干
像请了个远程实习生，分配完任务就不用管了

② 飞书日程，一句话安排
「明天下午2点跟市场部开会」
Hermes 自动查日历、找空闲、发邀请
不用打开飞书网页，全自动

③ 飞书消息，它帮你盯
监控指定群聊，自动回复常见问题
关键词触发，通知转发到 Telegram
7×24 在线，不摸鱼不请假

④ Bitable，自动录数据
爬到的信息自动写入多维表格
定时同步外部数据库
一条指令批量修改 500 行
告别手动复制粘贴

⑤ 文档草稿，自动生成
给个主题，Hermes 帮你写
自动排版、插图片、生成目录
技术方案、周报、会议纪要全包

⑥ 审批流程，不用盯
报销自动审批，请假智能判断
异常单据自动标记
规则灵活，不漏单不卡单

⑦ 双内核：飞书+Telegram 同时管
OpenClaw 管飞书，Hermes 管 Telegram
两个 Agent 共享技能库
圈里叫「养虾又养马」
虾是 QClaw，马是 Hermes

安装就一行：
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

飞书这边靠 OpenClaw 打通
两个都有，你就能实现 AI 全自动办公

现在 GitHub 175K+ Star，生态在长
方向对了，早用早享受 👇

#Hermes #飞书 #AI #开源 #效率工具 #自动化 #Agent
```

---

## 🖼️ 图片

| 顺序 | 文件 |
|------|------|
| 1 | `hermes-feishu-cover.png` |
| 2 | `hermes-feishu-card-1.png` |
| 3 | `hermes-feishu-card-2.png` |
| 4 | `hermes-feishu-card-3.png` |
| 5 | `hermes-feishu-card-4.png` |
| 6 | `hermes-feishu-card-5.png` |
| 7 | `hermes-feishu-card-6.png` |
| 8 | `hermes-feishu-card-7.png` |

---

## 🎯 发布命令

```bash
opencli xiaohongshu publish "<body>" \
  --title "Hermes对接飞书，7个场景看傻" \
  --images "hermes-feishu-cover.png,hermes-feishu-card-1.png,hermes-feishu-card-2.png,hermes-feishu-card-3.png,hermes-feishu-card-4.png,hermes-feishu-card-5.png,hermes-feishu-card-6.png,hermes-feishu-card-7.png" \
  --topics "Hermes,飞书,AI,开源,效率工具,自动化,Agent" \
  --draft true \
  --window foreground \
  --site-session persistent \
  -f yaml
```