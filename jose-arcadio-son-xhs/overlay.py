#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os
BASE="/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/jose-arcadio-son-xhs"
FONT = "/System/Library/Fonts/STHeiti Medium.ttc"
cards = {
    "01-cover": {"title": "何塞·阿尔卡蒂奥", "subtitle": "被家族期望毁掉的长孙"},
    "02-rome": {"title": "去罗马当教皇？", "subtitle": "他在欧洲学会了赌博和挥霍"},
    "03-return": {"title": "灰溜溜回马孔多", "subtitle": "布恩迪亚家已经彻底破败"},
    "04-gold": {"title": "挖出三袋金币", "subtitle": "乌尔苏拉藏了一辈子的家底"},
    "05-death": {"title": "被孩子溺死在浴池", "subtitle": "一群邻居小孩抢走了金币"},
    "06-epitaph": {"title": "布恩迪亚家的最后一点钱", "subtitle": "被这个不成器的长孙彻底断送"},
}
for name, info in cards.items():
    path = os.path.join(BASE, f"{name}.png")
    img = Image.open(path).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    w, h = img.size
    bar_h = int(h * 0.18)
    draw.rectangle([0, 0, w, bar_h], fill=(0, 0, 0, 100))
    title_size = int(w * 0.05)
    title_font = ImageFont.truetype(FONT, title_size)
    bbox = draw.textbbox((0, 0), info["title"], font=title_font)
    tx = (w - (bbox[2] - bbox[0])) // 2
    ty = int(h * 0.025)
    draw.text((tx, ty), info["title"], fill=(255, 255, 255), font=title_font)
    sub_size = int(w * 0.028)
    sub_font = ImageFont.truetype(FONT, sub_size)
    bbox = draw.textbbox((0, 0), info["subtitle"], font=sub_font)
    sx = (w - (bbox[2] - bbox[0])) // 2
    sy = ty + title_size + int(h * 0.015)
    draw.text((sx, sy), info["subtitle"], fill=(220, 220, 220), font=sub_font)
    result = Image.alpha_composite(img, overlay).convert("RGB")
    result.save(path, "PNG")
    sz = os.path.getsize(path) // 1024
    print(f"{name} OK {sz} KB")
