# 小红书草稿 - Codex++

> Codex App 外部增强启动器 · Rust + Tauri · 不修改原文件

---

## 📋 标题

```
聊聊 Codex++：Codex App 终于能删会话了✨
```

---

## 📋 正文（直接复制，小红书会自动 emoji + 段落）

```
聊聊 Codex++：Codex App 终于能删会话了 ✨

用 Codex App 的朋友 👋
这两个痛点一定折磨过你

🤯 痛点 1：API Key 登录后
插件入口直接灰掉
点啥都提示"需要登录 ChatGPT"

🗑️ 痛点 2：会话只能归档不能删
旧会话越积越多
本地数据库越塞越大，半年几 G

Codex++ 一把梭 ✅

它是 Codex App 的外部增强启动器
Rust + Tauri 写的
不修改 Codex 原始安装文件
通过 CDP 注入增强脚本，升级也不影响

🔓 核心能力
· 插件入口强制解锁 · 会话悬停秒删
· Markdown 导出 · 项目移动 · Timeline
· 用户脚本注入 · Upstream worktree
· Zed Remote 远程打开

🔌 中转注入
绑了官方登录但想走第三方 API？
Codex++ 自动写 model_provider
多中转配置热切换，一键回官方

🖥️ Windows NSIS / macOS x64+arm64 双 DMG

⚠️ macOS 报"已损坏"？
终端执行：
sudo xattr -rd com.apple.quarantine /Applications/Codex++\ 管理工具.app
sudo xattr -rd com.apple.quarantine /Applications/Codex++.app

📦 GitHub: BigPizzaV3/CodexPlusPlus
交流：QQ 群 1103050832 · Telegram

你在用 Codex 吗？评论区聊聊 👇

#CodeX #AI编程 #开发工具 #CodexPlusPlus #开源 #AIAgent #程序员 #VibeCoding
```

---

## 🖼️ 图片（按 001 → 002 → ... 顺序）

| 顺序 | 文件 |
|------|------|
| 1 | `codex-card-1-cover.png` |
| 2 | `codex-card-2-pain.png` |
| 3 | `codex-card-3-features.png` |
| 4 | `codex-card-4-relay.png` |
| 5 | `codex-card-5-platforms.png` |
| 6 | `codex-card-6-start.png` |

---

## 🎯 操作步骤

1. 创建飞书文档：lark-cli docs +create --title "聊聊 Codex++：Codex App 终于能删会话了"
2. overwrite 文档内容：lark-cli docs +update --doc <id> --mode overwrite --markdown "$(cat README.md)"
3. 逐张插入图片：lark-cli docs +media-insert --doc <id> --file <path>
