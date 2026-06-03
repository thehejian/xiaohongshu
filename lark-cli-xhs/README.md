# 灭霸来了，飞书CLI接管一切 🔥

> 小红书风格文章 · 2026-06-02
> 项目地址: https://github.com/larksuite/cli
> 文档: https://open.feishu.cn/document/
> 飞书预览: https://www.feishu.cn/docx/K7kHdqAjto4IfqxP9iUcBG9fnCh

## 📖 文章正文

> 2026-06-02 · github.com/larksuite/cli

用飞书开发的朋友 🙋‍♂️

查个日历要开网页、发个消息要切 App，想批量操作多维表格还得写脚本……

**飞书 CLI** —— 一个命令行工具覆盖飞书全部 API ✨

---

### 🚀 核心能力

一个命令覆盖全部飞书场景：

| 领域 | 能力 |
|------|------|
| **日历会议** 📅 | `+agenda` 日程概览、`+create` 创建会议、`+freebusy` 查忙闲 |
| **即时通讯** 💬 | 发消息、搜记录、管理群聊、上传文件 |
| **云文档** 📝 | 创建/更新文档、插入图片、搜索云空间 |
| **多维表格** 📊 | 建表建字段、批量读写、公式计算、视图配置 |
| **邮箱** 📧 | 起草、发送、收件箱、标签管理 |
| **通讯录** 👥 | 搜员工、查组织架构、找联系方式 |
| **视频会议** 🎥 | 查已结束会议、取纪要总结逐字稿 |
| **审批** ✅ | 审批实例、审批任务管理 |
| **考勤** ⏰ | 查询打卡记录 |

支持 `user` / `bot` 双身份切换，自动翻页，JSON / Table / CSV / Pretty 四种输出格式。

---

### 💎 三大亮点

**1️⃣ 原生 API 封装，零额外依赖**

基于飞书 OpenAPI 官方规范，`lark-cli api GET/POST` 可直接发任意接口。无需手动拼签名、不用操心 token 刷新。

**2️⃣ AI Agent Skills 生态**

```bash
npx skills add larksuite/cli -s lark-calendar -y
npx skills add larksuite/cli -s lark-im -y
npx skills add larksuite/cli -s lark-doc -y
```

每个 skill 封装一个领域的完整工作流，AI Agent 自动学会怎么用飞书。目前 20+ 领域 skill，覆盖从日历到审批的全场景。

**3️⃣ 开发者友好设计**

- `--jq <expr>` 直接过滤 JSON 结果
- `--page-all` 自动翻页（不限量）
- `--dry-run` 预览请求不执行
- `--output <path>` 二进制文件导出
- `--format pretty` 人类可读输出

---

### 🛒 安装

```bash
npm install -g @larksuiteo/cli
```

macOS 也可以用 Homebrew: `brew install lark-cli`

首次使用:
```bash
lark-cli config init       # 配置应用
lark-cli auth login        # 登录授权
lark-cli doctor            # 健康检查
```

---

<callout emoji="💡" background-color="light-blue" border-color="blue">

**飞书用户 + 命令行党必装。** 省下的时间够摸鱼一下午 😂

</callout>

**你用飞书做啥？评论区聊聊 👇**

`#飞书` `#开发者工具` `#CLI` `#效率工具` `#自动化` `#Lark` `#开源`

---

## 📂 文件清单

| 文件 | 说明 |
|------|------|
| `README.md` | 本文(文章 + 描述) |
| `lark-cli-square.png` | 方版封面 (1024×1024)，白色风格 |
| `lark-cli-banner.png` | 横版配图 (1792×1024)，白色风格 |

## 🔗 相关链接

- GitHub 仓库: https://github.com/larksuite/cli
- 飞书开放平台文档: https://open.feishu.cn/document/
- AI Agent Skills: https://github.com/larksuite/cli#agent-skills
