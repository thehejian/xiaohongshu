# 小红书草稿 - CC Switch v3.16.1

> Codex OAuth 保留 + Chat 工具路由 + 稳定性大修

---

## 📋 标题

```
CC Switch 史诗级更新
```

---

## 📋 正文（直接复制，小红书自动分段）

```
CC Switch 史诗级更新

最大的亮点：Codex 官方 OAuth 保留 🔑

以前用第三方 API 会覆盖官方登录态
现在可以同时保留 OAuth，切供应商不丢登录
远程操作、官方插件继续用，流量走第三方

Codex 模型目录不再被静默清空
Chat 工具/插件路由完整恢复
本地代理接管更稳，热切换不丢配置

新版还修复了：
· Claude Desktop 官方供应商添加报错
· Kimi/Moonshot 工具思考历史规范化
· Windows 版本探测乱码问题
· 余额查询跨应用凭据错用

开源免费，brew install --cask cc-switch

现在支持 7 个 AI 编程 CLI 了
你用几个？评论区聊聊 👇

#开源工具 #CCSwitch #ClaudeCode #AI编程 #Codex #GeminiCLI #开发者工具 #AIAgent
```

---

## 🖼️ 图片

| 顺序 | 文件 |
|------|------|
| 1 | `cc-switch-square.png` |
| 2 | `cc-switch-card-1.png` |
| 3 | `cc-switch-card-2.png` |
| 4 | `cc-switch-card-3.png` |

---

## 🎯 发布命令

```bash
opencli xiaohongshu publish "<body>" \
  --title "CC Switch 史诗级更新" \
  --images "cc-switch-square.png,cc-switch-card-1.png,cc-switch-card-2.png,cc-switch-card-3.png" \
  --topics "开源工具,CCSwitch,ClaudeCode,AI编程,Codex,GeminiCLI,开发者工具,AIAgent" \
  --window foreground \
  --site-session persistent \
  -f yaml
```