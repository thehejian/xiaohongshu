#!/usr/bin/env python3
"""Overlay Chinese text on generated images using Pillow. Pattern from buendia-tree-xhs."""
from PIL import Image, ImageDraw, ImageFont
import os, sys

BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/ziwu-road-xhs"
FONT = "/System/Library/Fonts/STHeiti Medium.ttc"

cards = {
    "01-cover": {
        "title": "子午道",
        "subtitle": "长安到汉中最快的命悬一线",
    },
    "02-card1": {
        "title": "路线",
        "subtitle": "北口子午峪 → 南口石泉县，250公里",
    },
    "03-card2": {
        "title": "最短最直",
        "subtitle": "直穿秦岭不绕弯",
    },
    "04-card3": {
        "title": "三国名场面",
        "subtitle": "诸葛亮北伐 · 钟会灭蜀",
    },
    "05-card4": {
        "title": "地形极险",
        "subtitle": "海拔落差超1500米",
    },
    "06-card5": {
        "title": "紧急专用",
        "subtitle": "唐代皇帝逃难走过的路",
    },
}

for name, info in cards.items():
    path = os.path.join(BASE, f"{name}.png")
    if not os.path.exists(path):
        print(f"SKIP {name}: {path} not found")
        continue
    img = Image.open(path).convert("RGBA")
    overlay_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay_layer)
    w, h = img.size

    # semi-transparent bar at top
    bar_h = int(h * 0.25)
    draw.rectangle([0, 0, w, bar_h], fill=(0, 0, 0, 100))

    # title (double size: 110px on 1024)
    title_size = int(w * 0.108)
    title_font = ImageFont.truetype(FONT, title_size)
    bbox = draw.textbbox((0, 0), info["title"], font=title_font)
    tw = bbox[2] - bbox[0]
    tx = (w - tw) // 2
    ty = int(h * 0.04)
    draw.text((tx, ty), info["title"], fill=(255, 255, 255), font=title_font)

    # subtitle (double size: 60px on 1024)
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
