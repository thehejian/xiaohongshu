# CC Switch v3.16.1 史诗级更新 🔥 Codex OAuth 保留 + Chat 路由大修

> 小红书风格文章 · 2026-06-02
> 项目地址: https://github.com/farion1231/cc-switch
> 官网: https://ccswitch.io
> 飞书预览: https://www.feishu.cn/docx/GTjsdLrAwolK6TxUNiscUmDsn4d

---

## 📖 文章正文

> 2026-06-02 · github.com/farion1231/cc-switch/releases/tag/v3.16.1

CC Switch 迎来 v3.16.1 重大更新 🚀

**最大的亮点：Codex 官方 OAuth 保留 🔑**

以前用第三方 API 会覆盖官方登录态。现在可以同时保留 OAuth，切供应商不丢登录。远程操作、官方插件继续用，流量走第三方。

---

### 🎯 v3.16.1 核心变化

**1️⃣ Codex OAuth 保留 🔑**
新增可选设置，第三方供应商 token 写入 `config.toml`，官方 ChatGPT / Codex OAuth 登录继续留在 `auth.json`。开启后即使频繁切换供应商，官方登录也不会掉。

**2️⃣ Codex 模型目录不再被静默清空 📂**
`modelCatalog` 以数据库为真相来源，live 回填、供应商切换、接管关闭恢复、编辑弹窗都会避免用丢失投影的 live 配置覆盖数据库。

**3️⃣ Chat 工具/插件路由完整恢复 🛠️**
Chat Completions 上游返回的 `tool_search`、已加载命名空间工具、自定义工具会重新映射回 Codex Responses 形态。流式自定义工具现在发出原生 `response.custom_tool_call_input.*` 事件。

**4️⃣ 本地路由接管与热切换更稳 🔄**
供应商切换和接管开关按 app 串行，热切换会刷新 Codex live 中的供应商显示信息，但 endpoint 仍保持指向本地代理。

---

### 🔧 其他修复

- Claude Desktop 官方供应商添加报错
- Kimi / Moonshot 工具思考历史规范化
- Windows 版本探测修复乱码与误判
- 余额查询跨 app 错用凭据

---

### 🛒 安装

`brew install --cask cc-switch`(macOS) · Win/Linux 去 [Releases](https://github.com/farion1231/cc-switch/releases) 下载

---

<callout emoji="💡" background-color="light-blue" border-color="blue">

**23 commits · 62 files changed · 开源免费。** 现在支持 7 个 AI 编程 CLI 工具了！

</callout>

**你用几个 AI 编程工具？评论区聊聊 👇**

`#开源工具` `#CCSwitch` `#ClaudeCode` `#AI编程` `#Codex` `#GeminiCLI` `#开发者工具` `#AIAgent`

---

## 📂 文件清单

| 文件 | 说明 |
|------|------|
| `README.md` | 本文(文章 + 描述) |
| `cc-switch-square.png` | 方版配图 (1024×1024), 小红书封面 |
| `cc-switch-banner.png` | 横版配图 (1792×1024), 微博/头图 |

## 🔗 相关链接

- GitHub 仓库: https://github.com/farion1231/cc-switch
- 官网: https://ccswitch.io
- v3.16.1 发布说明: https://github.com/farion1231/cc-switch/releases/tag/v3.16.1