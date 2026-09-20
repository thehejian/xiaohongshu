#!/usr/bin/env python3
"""Overlay Chinese text on pure AI-generated images using Pillow."""
import os
from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC = SCRIPT_DIR
OUT = os.path.dirname(os.path.dirname(SCRIPT_DIR))

FONT_PATH = "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/86ba2c91f017a3749571a82f2c6d890ac7ffb2fb.asset/AssetData/PingFang.ttc"

WHITE = (255, 255, 255)
NAVY = (30, 41, 59)
GREEN = (0, 98, 51)
GREEN_LIGHT = (209, 250, 229)
GOLD = (212, 168, 67)
RED = (211, 47, 47)
GRAY = (100, 116, 139)
GRAY_LIGHT = (148, 163, 184)

def draw_text_bg(draw, x, y, text, font, bg_color, pad=8, radius=12):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.rounded_rectangle(
        [x - tw//2 - pad, y - pad, x + tw//2 + pad, y + th + pad],
        radius=radius, fill=bg_color
    )
    draw.text((x - tw//2, y), text, fill=WHITE, font=font)

def add_text(img, texts, font_sizes, positions):
    draw = ImageDraw.Draw(img)
    for text, size, pos in zip(texts, font_sizes, positions):
        font = ImageFont.truetype(FONT_PATH, size)
        if len(pos) == 3:
            x, y, align = pos
            bbox = draw.textbbox((0, 0), text, font=font)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
            if align == "center":
                px = x - tw // 2
            elif align == "right":
                px = x - tw
            else:
                px = x
            draw.text((px, y - th // 2), text, fill=NAVY, font=font)
        else:
            x, y, color = pos
            bbox = draw.textbbox((0, 0), text, font=font)
            tw = bbox[2] - bbox[0]
            draw.text((x - tw // 2, y), text, fill=color, font=font)
    return img

def process_card(src_name, out_name, texts, font_sizes, positions):
    src_path = os.path.join(SRC, src_name)
    out_path = os.path.join(OUT, out_name)
    img = Image.open(src_path).convert("RGBA").resize((1024, 1024), Image.LANCZOS)
    img = add_text(img, texts, font_sizes, positions)
    img.save(out_path)
    print(f"  Saved: {out_path}")

def main():
    w = 1024
    FONT_LG = 56
    FONT_MD = 36
    FONT_SM = 26
    FONT_XS = 20
    FONT_TAG = 18

    cards = [
        ("01-cover0_0.png", "cover.png", [
            ("梅西 vs 齐达内之子", FONT_LG, (w//2, 88, "center")),
            ("阿根廷 3 : 0 阿尔及利亚", FONT_MD, (w//2, 140, "center")),
            ("2026世界杯·小组赛", FONT_XS, (w//2, 960, "center")),
        ]),
        ("02-three-goals0_0.png", "card-1.png", [
            ("帽子戏法", FONT_LG, (w//2, 80, "center")),
            ("任意球 · 低射 · 单刀", FONT_MD, (w//2, 135, "center")),
            ("卢卡·齐达内三次从球门捡球", FONT_SM, (w//2, 960, "center")),
        ]),
        ("03-postmatch-respect0_0.png", "card-2.png", [
            ("赛后一幕", FONT_LG, (w//2, 75, "center")),
            ("梅西走过去，弯下腰，拍了拍他的头", FONT_MD, (w//2, 135, "center")),
            ("没有人知道梅西说了什么", FONT_SM, (w//2, 965, "center")),
        ]),
        ("04-2006-20260_0.png", "card-3.png", [
            ("2006", FONT_LG, (w//4, 85, "center")),
            ("齐达内头顶马特拉齐", FONT_MD, (w//4, 145, "center")),
            ("2026", FONT_LG, (w*3//4, 85, "center")),
            ("卢卡·齐达内镇守龙门", FONT_MD, (w*3//4, 145, "center")),
            ("18年，两代人的世界杯", FONT_SM, (w//2, 960, "center")),
        ]),
        ("05-zidane-quote0_0.png", "card-4.png", [
            ("梅西是一个外星人", FONT_LG, (w//2, 80, "center")),
            ("但他属于巴萨，我恨这一点", FONT_MD, (w//2, 140, "center")),
            ("——齐达内", FONT_SM, (w//2, 965, "center")),
        ]),
        ("06-algeria-roots0_0.png", "card-5.png", [
            ("阿尔及利亚之根", FONT_LG, (w//2, 80, "center")),
            ("齐达内的父亲是阿尔及利亚人", FONT_MD, (w//2, 140, "center")),
            ("卢卡选择代表父亲的祖国", FONT_SM, (w//2, 960, "center")),
        ]),
        ("07-argentina-celebration0_0.png", "card-6.png", [
            ("阿根廷 3-0 大胜", FONT_LG, (w//2, 80, "center")),
            ("卫冕冠军小组赛开门红", FONT_MD, (w//2, 140, "center")),
            ("梅西：39岁，最后一舞", FONT_SM, (w//2, 960, "center")),
        ]),
        ("08-final-frame0_0.png", "card-7.png", [
            ("有人在封神", FONT_LG, (w//2, 85, "center")),
            ("有人在长大", FONT_LG, (w//2, 155, "center")),
            ("这就是世界杯", FONT_MD, (w//2, 960, "center")),
        ]),
    ]

    for src, out, items in cards:
        texts = [i[0] for i in items]
        sizes = [i[1] for i in items]
        positions = [i[2] for i in items]
        process_card(src, out, texts, sizes, positions)

    print("\nAll cards with text overlay complete!")

if __name__ == "__main__":
    main()