# 小红书草稿 - 飞书 CLI

> 一个命令行管飞书全部 API

---

## 📋 标题

```
灭霸来了，飞书CLI接管一切
```

---

## 📋 正文（直接复制，小红书自动分段）

```
天天用飞书的打工人请举手 🙋‍♂️

来，对号入座 👇

名场面一：
查今天几点开会 → 打开网页 → 密码忘了 → 重置 → 登上了 → 会已经开完了 😅

名场面二：
同事说「文件发群里了」→ 切到 App → 翻 2000 条消息 → 找不到 → 问「发了吗」→ 他说「早发了啊」

名场面三：
老板说「改一下多维表格」→ 打开网页 → 手动改 50 行 → 心想「能不能批量」→ 打开 API 文档 → 研究一下午 → 下班了

每次内心 OS：能不能一条命令解决？？🙏

能。飞书 CLI —— 一个命令行管飞书全部 API ✨

不用开网页、不用切 App，终端敲一行完事：

📅 日历：+agenda 秒看今日安排，+create 建会议
💬 消息：发通知搜聊天管群成员上传文件
📝 文档：+create 创建 +media-insert 插图
📊 表格：建表设字段写数据配公式配视图
📧 邮件：起草发送收件箱过滤标签管理
👥 通讯录：搜员工查组织架构找 open_id
🎥 会议：查已结束会议拿总结待办逐字稿
✅ 审批 + 考勤：一条命令查询不折腾

三个让我离不开的理由：

① 原生 API 封装 —— 免签名免 token 刷新
lark-cli api GET/POST 直接调任意飞书接口
开箱即用，不用折腾认证

② 双身份切换 —— --as user 日常干活
--as bot 跑自动化脚本，一行命令切换
底层 API 一样，身份不同权限不同

③ 20+ AI Agent Skill ——
npx skills add larksuite/cli -s lark-calendar
装一个 skill，AI 自动学会那个领域的操作流程

实用小功能：
--jq <表达式> 过滤 JSON 结果
--page-all 自动翻页不限量
--dry-run 预览请求不执行

安装就一行：
npm install -g @larksuiteo/cli
macOS 也能 brew install lark-cli

飞书用得越深越离不开它
省下的时间摸鱼不香吗 😂

👇 你平时用飞书最烦哪个操作？评论区聊聊
```

---

## 🖼️ 图片

| 顺序 | 文件 |
|------|------|
| 1 | `lark-cli-square.png` |
| 2 | `lark-cli-card-1.png` |
| 3 | `lark-cli-card-2.png` |
| 4 | `lark-cli-banner.png` |

---

## 🎯 发布命令

```bash
opencli xiaohongshu publish "<body>" \
  --title "灭霸来了，飞书CLI接管一切" \
  --images "lark-cli-square.png,lark-cli-card-1.png,lark-cli-card-2.png,lark-cli-banner.png" \
  --topics "飞书,开发者工具,CLI,效率工具,自动化,Lark,开源" \
  --draft true \
  --window foreground \
  --site-session persistent \
  -f yaml
```
