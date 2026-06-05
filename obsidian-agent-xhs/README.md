# Obsidian + AI Agent — 真有搞头还是炒作？

> 第二大脑终于装上了 AI 管家

---

## 背景

Obsidian 作为本地优先的笔记软件，长期是"第二大脑"的代名词。但它的本地属性也带来了一个问题：AI Agent 碰不到你的笔记。

你只能手动复制粘贴到 AI 对话窗口，然后 AI 在做回答时完全没有你的知识库上下文。

这个局面在 2026 年彻底被打破了。

---

## 转折点：Obsidian CLI

2026 年初，Obsidian 1.12 发布了官方 CLI。基准测试显示：

- **4,663 个文件、16GB vault**
- CLI 搜索：**0.26 秒**
- grep 搜索：**15.6 秒**
- **54 倍更快**

CEO Kepano 亲自展示了如何用 Claude Code 操作 Obsidian。这意味着 AI Agent 可以原生读写你的知识库了，不再需要任何中间人。

---

## 核心哲学：Agents Read, Humans Write

由 Greg Isenberg & InternetVin 推广的工作流，核心原则只有一句话：

> **AI 读取你的 vault 获取上下文，但从不替你写。**

Claude 的输出放在 `~/.claude/`，你的思考留在 Obsidian。自定义 slash 命令：
- `/my-world` — AI 读取你的 vault 了解你是谁
- `/today` — AI 拉取今日重点
- `/close` — 自动保存会话上下文
- `/trace` — 回溯思考链

---

## 技术架构：CLI + MCP 桥梁

```
你 (Obsidian)
   ↓ 写笔记
Obsidian CLI / MCP Server
   ↓ 语义搜索 / 上下文召回
AI Agent (Claude Code / Copilot)
   ↓ 理解你的知识
生成回答 + 联想
```

**关键组件：**
- **Obsidian CLI** — 直接操作 vault 文件，54x 快于 grep
- **MCP 服务器** — `obsidian-claude-code-mcp` 等插件，WebSocket 桥接
- **QMD (Quick Markdown Dump)** — Shopify CEO Tobi Lutke 的工具，自动导出 Claude 会话到 markdown，关闭即写回 vault
- **QMD 实测** — token 减少 60%+，处理时间降低超过一半

---

## 生态爆发

| 插件 | 角色 |
|------|------|
| **Copilot** (logancyang) | Chat 侧边栏，本地/远程 LLM |
| **Smart Connections** | 语义搜索 + 链接建议 |
| **Claudian** | Claude Code 作为侧边栏 |
| **Agent Client** | Claude Code + Codex + Gemini |
| **Claude Sidebar** | 嵌入式终端，自动启动 Claude Code |
| **Nexus AI Chat Importer** | 导入 5+ 平台 AI 对话 |

---

## 社区声音

> "传统的 copilot 体验在我的 vault 里感觉格格不入" — Obsidian Forum 用户

> "AI 应该安静地在后台工作。真正的语义搜索，而不是一个聊天框。" — gauthierae

> "QMD 把我的 token 使用和处理时间减少了 60% 以上" — Kevin Lee

> "Obsidian CLI 比 grep 快 54 倍 —— 现在 AI 可以原生使用 Obsidian 了" — @drrobcincotta

---

## 结论

**Obsidian + AI Agent 绝对有搞头。**

但正确的形式还在结晶中。社区已经明确拒绝了"聊天侧边栏"这种 AI 形态。赢家的模式是：

1. **无形后台 Agent** — 做语义搜索、链接建议、会话召回
2. **人写 AI 读** — 写作权永远在你手上
3. **基础设施就位** — CLI + MCP + QMD 三件套已可用

Obsidian 不是被 AI 替代，它是被 AI **激活**了。

---

## 相关资源

- [Obsidian CLI 官方公告](https://obsidian.md/blog/)
- [obsidian-claude-code-mcp](https://github.com/your/repo)
- [QMD — Quick Markdown Dump](https://github.com/tobi/qmd)
- [Obsidian Copilot 插件](https://github.com/logancyang/obsidian-copilot)
- [Smart Connections](https://github.com/brianpetro/obsidian-smart-connections)

## 文件清单

| 文件 | 尺寸 | 描述 |
|------|------|------|
| `oa-cover-zh.svg/png` | 1024×1024 | 中文封面 |
| `oa-card-1-zh.svg/png` | 800×800 | 中文痛点卡 |
| `oa-card-2-zh.svg/png` | 800×800 | 中文解决方案卡 |
| `oa-card-3-zh.svg/png` | 800×800 | 中文数据卡 |
| `oa-cover-en.svg/png` | 1024×1024 | 英文封面 |
| `oa-card-1-en.svg/png` | 800×800 | 英文哲学卡 |
| `oa-card-2-en.svg/png` | 800×800 | 英文架构卡 |
| `oa-card-3-en.svg/png` | 800×800 | 英文结论卡 |
| `article.md` | — | XHS 草稿 |
| `README.md` | — | 本文件 |
| `gen_cards.py` | — | SVG 生成脚本 |