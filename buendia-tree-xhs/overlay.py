#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

BASE="/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/buendia-tree-xhs"
FONT = "/System/Library/Fonts/STHeiti Medium.ttc"

cards = {
    "01-cover": {
        "title": "布恩迪亚家族七代人",
        "subtitle": "名字重复率高，一张图理清"
    },
    "02-gen1-2": {
        "title": "第一、二代",
        "subtitle": "开创者与开拓者"
    },
    "03-gen3": {
        "title": "第三代",
        "subtitle": "全是私生子，全部死于非命"
    },
    "04-gen4": {
        "title": "第四代",
        "subtitle": "走向分化的一代"
    },
    "05-gen5": {
        "title": "第五代",
        "subtitle": "现代冲突的一代"
    },
    "06-gen6-7": {
        "title": "第六、七代",
        "subtitle": "破译预言，走向终结"
    }
}

for name, info in cards.items():
    path = os.path.join(BASE, f"{name}.png")
    img = Image.open(path).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    w, h = img.size

    # semi-transparent bar at top
    bar_h = int(h * 0.18)
    draw.rectangle([0, 0, w, bar_h], fill=(0, 0, 0, 100))

    # title
    title_size = int(w * 0.055)
    title_font = ImageFont.truetype(FONT, title_size)
    bbox = draw.textbbox((0, 0), info["title"], font=title_font)
    tw = bbox[2] - bbox[0]
    tx = (w - tw) // 2
    ty = int(h * 0.025)
    draw.text((tx, ty), info["title"], fill=(255, 255, 255), font=title_font)

    # subtitle
    sub_size = int(w * 0.03)
    sub_font = ImageFont.truetype(FONT, sub_size)
    bbox = draw.textbbox((0, 0), info["subtitle"], font=sub_font)
    sw = bbox[2] - bbox[0]
    sx = (w - sw) // 2
    sy = ty + title_size + int(h * 0.015)
    draw.text((sx, sy), info["subtitle"], fill=(200, 200, 200), font=sub_font)

    # bottom bar with generation labels
    bot_bar_h = int(h * 0.06)
    draw.rectangle([0, h - bot_bar_h, w, h], fill=(0, 0, 0, 80))
    bbox = draw.textbbox((0, 0), info["subtitle"], font=sub_font)
    gen_label = name.split("-")[-1].upper() if "-" in name else name
    gen_label = f"GEN {gen_label}"
    bbox = draw.textbbox((0, 0), gen_label, font=sub_font)
    gw = bbox[2] - bbox[0]
    gx = (w - gw) // 2
    gy = h - bot_bar_h + int((bot_bar_h - sub_size) / 2)
    draw.text((gx, gy), gen_label, fill=(180, 180, 180), font=sub_font)

    result = Image.alpha_composite(img, overlay)
    result = result.convert("RGB")
    result.save(path, "PNG")
    sz = os.path.getsize(path) // 1024
    print(f"{name} overlay OK {sz} KB")
