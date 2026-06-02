# 聊聊 Codex++：Codex App 终于能删会话了 ✨

> 小红书风格文章 · 2026-06-02
> Codex App 外部增强启动器 · Rust + Tauri · 不修改原文件

![banner](codex-card-1-cover.png)

---

## 📖 文章正文

用 Codex App 的朋友，下面这两个问题你大概率都遇到过 👇

### 🤯 痛点一：插件入口是"装饰品"

API Key 模式登录后，Codex 插件页直接灰掉，点啥都提示「需要登录 ChatGPT」。明明是个能本地安装的工具，偏偏被官方硬切回云端登录态。

### 🗑️ 痛点二：会话只能"归档"不能"删"

原生界面只有一个归档按钮（`Archive`），没有真正的 Delete。旧会话越积越多，本地数据库 `~/.codex/state_5.sqlite` 越塞越大。半年下来几个 G 都不稀奇。

---

## ✅ Codex++ 是什么？

它是 **Codex App 的外部增强启动器**，用 **Rust + Tauri** 写的桌面工具。

**关键设计**：不修改 Codex 原始安装文件。Codex++ 启动 Codex App 后，通过 **Chromium DevTools Protocol** 注入增强脚本（`renderer-inject.js`），所有功能都在外部层叠加 —— Codex 升级也不会失效。

GitHub：[BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus)

---

## 🔓 核心能力一览

| 模块 | 说明 |
|------|------|
| 插件入口解锁 | API Key 模式下也能用 Codex 插件 |
| 会话删除 | 列表悬停显示「删除」按钮，真删本地 DB |
| Markdown 导出 | 一键导出 session 为 `.md` |
| 项目移动 | 在 UI 内调整项目归属 |
| Timeline 视图 | 按时间线浏览所有会话 |
| 用户脚本 | 启动时注入自定义 JS 脚本 |
| Upstream worktree | 从 `upstream/<base>` 创建新 worktree，自动 fetch 远端 |
| Zed 远程打开 | 识别 SSH 上下文后从 Codex 直接打开对应文件到 Zed Remote |
| 自动更新 | 静默启动器 + 管理工具都检测 GitHub Release |

---

## 🔌 中转注入（杀手锏）

如果你已经完成 ChatGPT 官方登录、但模型想走自己的中转 API，Codex++ 的中转注入模式就是为你准备的。

**操作步骤**：
1. 打开 Codex++ 管理工具 → 中转注入
2. 确认已检测到 ChatGPT 登录状态
3. 添加中转配置：Base URL + Key
4. 选择当前配置 → 应用中转注入
5. 启动 Codex++

Codex++ 会自动在 `~/.codex/config.toml` 写入：

```toml
model_provider = "CodexPlusPlus"

[model_providers.CodexPlusPlus]
name = "CodexPlusPlus"
wire_api = "responses"
requires_openai_auth = true
base_url = "https://example.com/v1"
experimental_bearer_token = "sk-..."
```

需要切回官方登录态？点「清除 API 模式」就完事。

**支持的 API 中转**（项目 README 提到的）：JOJO Code、AIGoCode、PackyCode、APIKEY.FUN、RunAPI、0029 云桥、RawChat、VisionCoder、AIHub2API、优云智算、Cubence、MaoLao API。

---

## 🖥️ 全平台覆盖

| 平台 | 安装包 |
|------|--------|
| Windows x64 | `CodexPlusPlus-*-windows-x64-setup.exe` (NSIS) |
| macOS Intel | `CodexPlusPlus-*-macos-x64.dmg` |
| macOS Apple Silicon | `CodexPlusPlus-*-macos-arm64.dmg` |

Windows 安装包会创建桌面和开始菜单快捷方式。macOS DMG 会装 `/Applications/Codex++.app` 和 `/Applications/Codex++ 管理工具.app` 两个 App。

### ⚠️ macOS 报「已损坏」？

当前安装包未签名/未公证，Gatekeeper 可能拦截。终端执行：

```bash
sudo xattr -rd com.apple.quarantine /Applications/Codex++\ 管理工具.app
sudo xattr -rd com.apple.quarantine /Applications/Codex++.app
```

---

## 🧱 技术架构

```
apps/
  codex-plus-launcher/          静默启动入口
  codex-plus-manager/           Tauri 管理工具 (React)
assets/inject/
  renderer-inject.js            注入到 Codex 渲染端的增强脚本
crates/
  codex-plus-core/              启动、注入、配置、更新、安装、桥接
  codex-plus-data/              会话数据、导出、Provider 同步
scripts/installer/
  windows/CodexPlusPlus.nsi     Windows NSIS 安装包
  macos/package-dmg.sh          macOS DMG 打包
```

- **Rust 1.85+** 后端，启动不依赖额外运行时
- **Tauri 2.x** + React 前端，支持深色/浅色切换
- **CDP 注入**：不打包 `app.asar`，不向 Codex 安装目录写 DLL
- **Provider 同步**：启动前同步本地会话 metadata，切换供应商后旧会话仍可见
- **Windows 单实例 / 无黑框启动** + 管理员权限清单
- **macOS x64/arm64** 分架构 DMG，静默入口隐藏 Dock 图标

---

## 📂 数据位置

- Codex 配置：`~/.codex/config.toml`
- Codex 登录状态：`~/.codex/auth.json`
- Codex 本地数据库：`~/.codex/state_5.sqlite`
- Codex++ 状态与日志：`~/.codex-session-delete/`
- Provider 同步备份：`~/.codex/backups_state/provider-sync`

---

## 🤝 交流

- GitHub：https://github.com/BigPizzaV3/CodexPlusPlus
- QQ 群：1103050832
- Telegram：https://t.me/CodexPlusPlus

---

**你在用 Codex 吗？最想要什么增强功能？评论区聊聊 👇**

`#Codex` `#AI编程` `#开发工具` `#CodexPlusPlus` `#开源` `#AIAgent` `#程序员` `#开发者` `#VibeCoding` `#ClaudeCode`

---

## 📂 文件清单

| 文件 | 说明 |
|------|------|
| `article.md` | 小红书发布草稿（标题 + 正文 + 发布命令） |
| `README.md` | 本文（文章正文 + 架构说明） |
| `codex-logo-256.png` | Codex++ 官方 logo（256×256） |
| `codex-card-1-cover.png` | 封面卡（800×800） |
| `codex-card-2-pain.png` | 痛点对比卡 |
| `codex-card-3-features.png` | 功能一览卡 |
| `codex-card-4-relay.png` | 中转注入卡 |
| `codex-card-5-platforms.png` | 多平台卡 |
| `codex-card-6-start.png` | 三步上手卡 |
| `gen_cards.py` | SVG → PNG 卡片生成脚本 |
| `*.svg` | 卡片源文件 |

## 📝 信息来源

- [Codex++ GitHub README](https://github.com/BigPizzaV3/CodexPlusPlus)
- [GitHub Releases](https://github.com/BigPizzaV3/CodexPlusPlus/releases)
- 项目图标：`docs/images/codex-plus-plus.png`
