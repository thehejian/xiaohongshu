#!/usr/bin/env python3
"""Overlay Chinese text on pure AI-generated images using Pillow."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC = SCRIPT_DIR
OUT = os.path.dirname(os.path.dirname(SCRIPT_DIR))

def find_font():
    candidates = [
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/86ba2c91f017a3749571a82f2c6d890ac7ffb2fb.asset/AssetData/PingFang.ttc",
        "/System/Library/Fonts/PingFang.ttc",
    ]
    for p in candidates:
        if os.path.exists(p):
            return p
    return candidates[0]

FONT_PATH = find_font()
WHITE = (255, 255, 255)
NAVY = (30, 41, 59)
GREEN = (0, 98, 51)
GOLD = (212, 168, 67)
RED = (211, 47, 47)
GRAY = (100, 116, 139)

def add_text_with_bg(img, text, font_size, y_pos, text_color=WHITE, bg_color=(0, 0, 0, 160), pad_x=20, pad_y=8):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_PATH, font_size)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    W = img.width
    x = (W - tw) // 2
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    o_draw = ImageDraw.Draw(overlay)
    o_draw.rounded_rectangle(
        [x - pad_x, y_pos - pad_y, x + tw + pad_x, y_pos + th + pad_y + 4],
        radius=8, fill=bg_color
    )
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)
    draw.text((x, y_pos), text, fill=text_color, font=font)
    return img

def add_text_simple(img, text, font_size, position, color=WHITE, anchor="center"):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_PATH, font_size)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    W = img.width
    if anchor == "center":
        x = (W - tw) // 2
    elif anchor == "left":
        x = 40
    elif anchor == "right":
        x = W - tw - 40
    else:
        x = position[0]
    draw.text((x, position[1]), text, fill=color, font=font)
    return img

def process_card(src_name, out_name):
    src_path = os.path.join(SRC, src_name)
    out_path = os.path.join(OUT, out_name)
    img = Image.open(src_path).convert("RGBA").resize((1024, 1024), Image.LANCZOS)
    return img, out_path

def main():
    w = 1024
    cards = []

    # Card 0: Cover - Messi celebration
    cards.append(("01-cover.png", "cover.png", [
        ("梅西帽子戏法！", 56, (w//2, 85, WHITE, (0, 0, 0, 170))),
        ("阿根廷 3-0 阿尔及利亚", 32, (w//2, 145, WHITE, (0, 0, 0, 150))),
        ("2026世界杯·39岁最后一舞", 24, (w//2, 965, WHITE, (0, 0, 0, 140))),
    ]))

    # Card 1: Three goals
    cards.append(("02-card.png", "card-1.png", [
        ("帽子戏法", 52, (w//2, 85, WHITE, (0, 0, 0, 170))),
        ("任意球 · 低射 · 单刀", 30, (w//2, 145, WHITE, (0, 0, 0, 150))),
        ("三种方式，同一个梅西", 24, (w//2, 960, WHITE, (0, 0, 0, 140))),
    ]))

    # Card 2: Algeria team
    cards.append(("03-card.png", "card-2.png", [
        ("阿尔及利亚", 52, (w//2, 85, WHITE, (0, 0, 0, 170))),
        ("北非之狐，第二次世界杯之旅", 28, (w//2, 145, WHITE, (0, 0, 0, 150))),
        ("#小众国家游记", 22, (w//2, 960, WHITE, (0, 0, 0, 140))),
    ]))

    # Card 3: Post-match respect
    cards.append(("04-card.png", "card-3.png", [
        ("赛后一幕", 52, (w//2, 85, WHITE, (0, 0, 0, 170))),
        ("梅西弯下腰，拍了拍他的头", 30, (w//2, 145, WHITE, (0, 0, 0, 150))),
        ("没有人知道梅西说了什么", 24, (w//2, 960, WHITE, (0, 0, 0, 140))),
    ]))

    # Card 4: Algeria culture
    cards.append(("05-card.png", "card-4.png", [
        ("撒哈拉沙漠中的足球梦", 48, (w//2, 85, WHITE, (0, 0, 0, 170))),
        ("阿尔及利亚，面积238万km²的足球国度", 26, (w//2, 140, WHITE, (0, 0, 0, 150))),
        ("沙漠之狐的骄傲", 24, (w//2, 960, WHITE, (0, 0, 0, 140))),
    ]))

    # Card 5: Final frame
    cards.append(("06-card.png", "card-5.png", [
        ("Messi es la patria", 50, (w//2, 85, WHITE, (0, 0, 0, 170))),
        ("梅西就是祖国", 36, (w//2, 150, WHITE, (0, 0, 0, 150))),
        ("#世界杯里看世界", 22, (w//2, 960, WHITE, (0, 0, 0, 140))),
    ]))

    for src, out, items in cards:
        img, out_path = process_card(src, out)
        for text, size, pos_data in items:
            x, y, color, bg = pos_data
            img = add_text_with_bg(img, text, size, y, text_color=color, bg_color=bg)
        img.save(out_path)
        print(f"  Saved: {out_path}")

    print("\nAll 6 cards with text overlay complete!")

if __name__ == "__main__":
    main()
