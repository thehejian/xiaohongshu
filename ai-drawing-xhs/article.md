# 小红书草稿 - AI 画图工具横评

> 5 大主流 AI 绘画工具深度对比

---

## 📋 标题

```
AI画图工具红黑榜
```

---

## 📋 正文（直接复制）

```
AI画图工具红黑榜

AI绘图工具太多不知道怎么选？

这期把5个主流工具全测了一遍 👇

🎨 Midjourney — 画质天花板
优点：光影氛围无敌，出图一眼惊艳
缺点：贵（10-60$/月），上手有门槛
适合：专业设计师、商业出图

🎨 DALL-E 3 — 新手友好全能王
优点：提示词理解最强，文字渲染准
缺点：画质略逊MJ，风格选择少
适合：ChatGPT用户、日常需求

🎨 Stable Diffusion — 技术玩家
优点：完全免费开源，LoRA/ControlNet
缺点：需要好显卡，配置麻烦
适合：愿意折腾的进阶玩家

🎨 Leonardo.ai — 网页端神器
优点：免费额度足，内置多种模型
缺点：高级功能需付费
适合：游戏素材、快速出图

🎨 即梦 — 国内用户首选
优点：免费，支持中文提示词
缺点：精细控制不如MJ/SD
适合：小红书配图、国风创作

总结：没有最好的，只有最适合的
预算够选MJ，新手选DALL-E
爱折腾选SD，在国内选即梦

都去试试免费版再决定 👍
```

---

## 🖼️ 图片

| 顺序 | 文件 |
|------|------|
| 1 | `ai-drawing-square.png` |
| 2 | `ai-drawing-card-1.png` |
| 3 | `ai-drawing-card-2.png` |
| 4 | `ai-drawing-card-3.png` |
| 5 | `ai-drawing-banner.png` |

---

## 🎯 发布命令

```bash
opencli xiaohongshu publish "<body>" \
  --title "AI画图工具红黑榜" \
  --images "ai-drawing-square.png,ai-drawing-card-1.png,ai-drawing-card-2.png,ai-drawing-card-3.png,ai-drawing-banner.png" \
  --topics "AI绘画,Midjourney,StableDiffusion,DALLE,即梦,AI工具" \
  --draft true \
  --window foreground \
  --site-session persistent \
  -f yaml
```