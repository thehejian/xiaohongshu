# 小红书草稿 - OpenCLI

> 让每个网站都拥有 CLI

---

## 📋 标题

```
OpenCLI 万物皆可 CLI
```

---

## 📋 正文（直接复制，小红书自动分段）

```
OpenCLI 万物皆可 CLI 🤯

用过就回不去了 👇

以前你的一天：

查知乎热榜 → 打开网页 → 广告弹窗 → 关掉 → 找到热榜
搜 GitHub 项目 → 打开网页 → 搜关键词 → 翻 README → 半小时
发小红书 → 打开网页 → 登录 → 传图 → 写文案 → 选话题 → 发布

每干一件事就得打开网页、等加载、找功能、点半天。

现在呢？终端敲一行：

opencli zhihu search AI Agent
opencli github search opencli
opencli xiaohongshu publish --title '标题' --images 'xxx.png'

148 个网站适配器，全部一行搞定。

四大核心

① 148+ 适配器 · 覆盖日常 90% 网站
小红书、知乎、B站、微博、豆瓣、推特
ChatGPT、Claude、GitHub、Docker、飞书CLI
还在持续增加

② Browser Bridge · 真浏览器自动化
Chrome 驱动操作网页，登录态长期复用
查 Feed、看笔记、搜内容、发帖子，全在终端完成

③ AI Agent 原生友好
所有命令 --format yaml/json 输出
Agent 拿到结构化数据，自动执行

④ 13 个外部 CLI 一键聚合
lark-cli · gh · vercel · wrangler · obsidian
一个 opencli 管所有

安装就一行：
npm install -g opencli

148 个适配器还在加
一个终端，管所有 👇
```

---

## 🖼️ 图片

| 顺序 | 文件 |
|------|------|
| 1 | `opencli-square.png` |
| 2 | `opencli-card-1.png` |
| 3 | `opencli-card-2.png` |
| 4 | `opencli-banner.png` |

---

## 🎯 发布命令

```bash
opencli xiaohongshu publish "<body>" \
  --title "OpenCLI 万物皆可 CLI" \
  --images "opencli-square.png,opencli-card-1.png,opencli-card-2.png,opencli-banner.png" \
  --topics "OpenCLI,开发者工具,CLI,效率工具,自动化,开源" \
  --draft true \
  --window foreground \
  --site-session persistent \
  -f yaml
```
