#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/tangkluo-road-xhs"
FONT = "/System/Library/Fonts/STHeiti Medium.ttc"

cards = {
    "01-cover": {"title": "傥骆道", "subtitle": "唐代皇帝的逃命专线"},
    "02-card1": {"title": "路线", "subtitle": "北起周至 → 南到洋县，400公里"},
    "03-card2": {"title": "海拔最高", "subtitle": "骆谷口超2000米"},
    "04-card3": {"title": "唐代皇帝逃难", "subtitle": "玄宗德宗僖宗三次走此道"},
    "05-card4": {"title": "终年积雪", "subtitle": "即使夏天山顶也积雪"},
    "06-card5": {"title": "紧急专用", "subtitle": "唐代17个驿站的皇家专线"},
}

for name, info in cards.items():
    path = os.path.join(BASE, f"{name}.png")
    if not os.path.exists(path):
        print(f"SKIP {name}"); continue
    img = Image.open(path).convert("RGBA")
    overlay_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay_layer)
    w, h = img.size
    bar_h = int(h * 0.25)
    draw.rectangle([0, 0, w, bar_h], fill=(0, 0, 0, 100))
    title_size = int(w * 0.108)
    title_font = ImageFont.truetype(FONT, title_size)
    bbox = draw.textbbox((0, 0), info["title"], font=title_font)
    tw = bbox[2] - bbox[0]
    tx = (w - tw) // 2
    ty = int(h * 0.04)
    draw.text((tx, ty), info["title"], fill=(255, 255, 255), font=title_font)
    sub_size = int(w * 0.06)
    sub_font = ImageFont.truetype(FONT, sub_size)
    bbox = draw.textbbox((0, 0), info["subtitle"], font=sub_font)
    sw = bbox[2] - bbox[0]
    sx = (w - sw) // 2
    sy = ty + title_size + int(h * 0.025)
    draw.text((sx, sy), info["subtitle"], fill=(200, 200, 200), font=sub_font)
    result = Image.alpha_composite(img, overlay_layer)
    result = result.convert("RGB")
    result.save(path, "PNG")
    sz = os.path.getsize(path) // 1024
    print(f"{name} overlay OK {sz} KB")
