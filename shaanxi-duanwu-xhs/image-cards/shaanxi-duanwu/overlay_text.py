#!/usr/bin/env python3
"""Overlay Chinese text on pre-generated AI images using Pillow."""
import os
from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC = SCRIPT_DIR
OUT = os.path.dirname(os.path.dirname(SCRIPT_DIR))

FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"

WHITE = (255, 255, 255)
NAVY = (30, 41, 59)
GOLD = (212, 168, 67)
BG_BAR = (0, 0, 0, 160)

def process_card(src_name, out_name, texts, font_sizes, positions):
    src_path = os.path.join(SRC, src_name)
    out_path = os.path.join(OUT, out_name)
    img = Image.open(src_path).convert("RGBA").resize((1024, 1024), Image.LANCZOS)
    W, H = img.size

    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    for text, size, pos in zip(texts, font_sizes, positions):
        font = ImageFont.truetype(FONT_PATH, size)
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]

        if len(pos) == 4:
            x, y, color, bg = pos
        elif len(pos) == 3:
            x, y, color = pos
            bg = None
        else:
            x, y = pos
            color = WHITE
            bg = None

        if bg:
            pad = 12
            draw.rectangle(
                [x - tw // 2 - pad, y - pad, x + tw // 2 + pad, y + th + pad],
                fill=bg
            )

        draw.text((x - tw // 2, y), text, fill=color, font=font)

    img = Image.alpha_composite(img, overlay)
    img.save(out_path)
    print(f"  Saved: {out_path}")

def main():
    W = 1024
    FONT_XL = 48
    FONT_LG = 34
    FONT_MD = 26
    FONT_SM = 22

    cards = [
        ("01-cover.png", "cover.png", [
            ("老陕端午", FONT_XL, (W//2, 820, WHITE, BG_BAR)),
            ("把政敌做成馍", FONT_LG, (W//2, 878, WHITE, BG_BAR)),
        ]),
        ("02-qulianmo.png", "card-1.png", [
            ("曲连馍", FONT_XL, (W//2, 820, WHITE, BG_BAR)),
            ("比脸还大的端午C位", FONT_LG, (W//2, 878, WHITE, BG_BAR)),
        ]),
        ("03-process.png", "card-2.png", [
            ("油曲轮", FONT_XL, (W//2, 820, WHITE, BG_BAR)),
            ("新麦收割·老面发酵·焦黄酥脆", FONT_LG, (W//2, 878, WHITE, BG_BAR)),
        ]),
        ("04-kid.png", "card-3.png", [
            ("兵马俑预备役", FONT_XL, (W//2, 820, WHITE, BG_BAR)),
            ("五彩绳一串，往脖子上一挂", FONT_LG, (W//2, 878, WHITE, BG_BAR)),
        ]),
        ("05-basket.png", "card-4.png", [
            ("粽子？那是小甜点", FONT_XL, (W//2, 820, WHITE, BG_BAR)),
            ("真正C位只有一个——曲连馍", FONT_LG, (W//2, 878, GOLD, BG_BAR)),
        ]),
        ("06-scene.png", "card-5.png", [
            ("端午快乐！", FONT_XL, (W//2, 820, WHITE, BG_BAR)),
            ("政敌没了·麦子丰收·普天同庆", FONT_LG, (W//2, 878, WHITE, BG_BAR)),
        ]),
    ]

    for src, out, items in cards:
        texts = [i[0] for i in items]
        sizes = [i[1] for i in items]
        positions = [tuple(i[2]) for i in items]
        process_card(src, out, texts, sizes, positions)

    print("\nAll cards with text overlay complete!")

if __name__ == "__main__":
    main()
