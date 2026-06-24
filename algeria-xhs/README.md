# 阿尔及利亚 · 足球与沙漠之国

**小红书帖子** | 2026年6月

---

## 内容类型
- 国家旅行 + 足球趣闻

## 正文 (article.md)
- 标题：阿尔及利亚，足球与沙漠之国
- 字数：519 字符（≤950 ✅）
- 话题标签：阿尔及利亚、北非旅行、撒哈拉沙漠、阿尔及利亚足球、马赫雷斯、小众旅行地、世界杯、非洲旅行

## 卡片 (4张)

| 卡片 | 内容 |
|------|------|
| 01-cover | 封面 · 阿尔及利亚总览（足球+沙漠+地中海） |
| 02-football | 足球篇 · 2014世界杯、2019非洲杯、马赫雷斯、齐达内 |
| 03-travel | 旅行篇 · 阿尔及尔、卡斯巴、古罗马遗址、美食 |
| 04-sahara | 撒哈拉篇 · 塔西利恩阿耶、沙漠奇观、此生必去 |

## 发布命令

```bash
opencli xiaohongshu publish "$(cat article.md)" \
  --title "阿尔及利亚，足球与沙漠之国" \
  --images "output/01-cover.png,output/02-football.png,output/03-travel.png,output/04-sahara.png" \
  --window foreground \
  --site-session persistent \
  -f yaml
```
