# AI视频生成小红书卡片 — 经验教训

## 📋 项目概述

- **任务**：制作AI视频生成工具盘点小红书图文（Sora, Runway, Pika, 可灵, Vidu, Kling）
- **输出**：7张卡片图 + 小红书正文 + 飞书文档
- **最终方案**：白色卡片风格 v3（简洁清爽）

---

## 🔧 踩坑记录

### 1. SVG 文字溢出问题

**问题**：标题在色块中上下溢出，文字被裁剪

**原因**：SVG `<text>` 的 `y` 属性是**基线（baseline）**，不是文字中心。大字号时基线偏下，视觉上文字整体偏下

**解决**：
- 单行标题：基线向上偏移 ~15px（y = centre - 15）
- 双行标题：两行整体居中，第一行 centre-35，第二行 centre+25

---

### 2. Logo 图片显示错误

**问题**：卡片中 logo 区域空白

**原因**：SVG 中 `<image href="openai.png">` 引用相对路径文件，但 SVG 生成后立即删除，Inkscape 渲染时找不到文件

**错误尝试**：
- ❌ 下载官网 logo（返回 HTML 或 404）
- ❌ GitHub simple-icons（404）
- ❌ clearbit logo API（超时）
- ❌ Wikimedia Commons（无对应 logo）

**解决**：**base64 data URI 内嵌**

```xml
<image xlink:href="data:image/png;base64,iVBORw0KGgo..." />
```

Logo 直接编码进 SVG，不再依赖外部文件，Inkscape 渲染稳定。

---

### 3. Inkscape 尺寸问题

**问题**：`--export-dpi` 未正确生效，输出尺寸不对

**解决**：
- 使用 `--export-dpi=100` + `--export-type=png`
- SVG 本身定义 1024×1024，确保输出一致

---

### 4. 小红书发布限制

**限制**：
- 标题 ≤ 20 字
- 正文 ≤ 950 字
- 图片 ≤ 9 张
- 话题标签无 `#` 前缀

**注意**：正文第一行即为标题（小红书自动提取），不要重复写标题

---

### 5. 设计风格迭代

| 版本 | 风格 | 问题 |
|------|------|------|
| v1 | 深色渐变 + 白色卡片 | 文字看不清 |
| v2 | 对角线渐变 + 大数字 | 太花哨，不符合小红书风格 |
| v3 | 白色卡片 + 顶部色条 | ✅ 简洁清爽，最终版 |

---

## ✅ 最佳实践

### SVG 卡片设计

```python
# 1. 白色卡片背景
<rect x="60" y="60" width="904" height="904" rx="24" fill="#FFFFFF" stroke="#E5E5E5"/>

# 2. 顶部彩色条（品牌色）
<rect x="60" y="60" width="904" height="200" rx="24" fill="#10B981"/>

# 3. Logo 内嵌（base64）
<image x="382" y="340" width="260" height="260" xlink:href="data:image/png;base64,..."/>

# 4. 文字全部白色（色条上）/ 灰色（卡片上）
<text fill="#FFFFFF">标题</text>
<text fill="#666666">副标题</text>
```

### 小红书发布

```bash
opencli xiaohongshu publish "$(cat content.txt)" \
  --title "标题≤20字" \
  --images "img1.png,img2.png,..." \
  --topics "标签1,标签2,..." \
  --draft true
```

### 飞书文档

```bash
# 创建文档
lark-cli docs +create --title "标题" --markdown - <<'MD'
内容...
MD

# 插入图片
lark-cli docs +media-insert --doc "$DOC_ID" --file ./card.png --align center
```

---

## 📁 项目文件结构

```
ai-video-gen-xhs/
├── gen_cards_v3.py        # 卡片生成脚本（v3 简洁白色风格）
├── gen_cover_v3.py        # 封面生成脚本
├── card_cover_v3.png      # 封面图
├── card_v3_01.png ~ 06.png # 6张产品卡片
├── logos/                 # Logo 源文件（base64 内嵌）
│   ├── openai.png         # OpenAI 六边形
│   ├── runway.png         # RUNWAY 文字
│   ├── pika.png           # PIKA 文字
│   ├── kling.png          # 可灵 中文
│   ├── vidu.png           # VIDU 文字
│   └── sensetime.png      # KLING 文字
├── xhs_content.txt        # 小红书正文（886字）
├── article.md             # 完整文章
├── README.md              # 项目说明
└── LESSONS.md             # 本文
```

---

## 🎯 关键决策

| 决策 | 选择 | 原因 |
|------|------|------|
| Logo 方案 | base64 内嵌 | 外部链接不稳定，内嵌最可靠 |
| 设计风格 | 白色卡片 | 小红书爆款风格，简洁清爽 |
| 发布方式 | 草稿模式 | 先预览再手动发布，更安全 |
| 飞书文档 | 分步插入 | 先创建文档，再逐张插入图片 |

---

*最后更新：2026-06-03*
