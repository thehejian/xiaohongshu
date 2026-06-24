#!/usr/bin/env python3
"""Overlay Chinese text onto generated images at 2x resolution for clarity."""

from PIL import Image, ImageDraw, ImageFont
import os

BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/zhushenhunxuan-xhs/image-cards/zhushenhunxuan"

FONT_PATH = "/System/Library/Fonts/Heiti SC.ttf"

def get_font(size):
    try:
        return ImageFont.truetype(FONT_PATH, size)
    except:
        return ImageFont.load_default()

def overlay_cover(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    # Scale up 2x
    w, h = img.size
    img = img.resize((w*2, h*2), Image.LANCZOS)
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Title at top 15%
    font_title = get_font(int(h * 0.07 * 2))
    title = "诸神黄昏"
    bbox = draw.textbbox((0, 0), title, font=font_title)
    tw = bbox[2] - bbox[0]
    tx = (img.size[0] - tw) // 2
    ty = int(img.size[1] * 0.12)
    draw.text((tx, ty), title, font=font_title, fill="#FFFFFF")
    
    # Subtitle at 25%
    font_sub = get_font(int(h * 0.035 * 2))
    sub = "这可能是他们最后一次同台了"
    bbox = draw.textbbox((0, 0), sub, font=font_sub)
    sw = bbox[2] - bbox[0]
    sx = (img.size[0] - sw) // 2
    sy = int(img.size[1] * 0.25)
    draw.text((sx, sy), sub, font=font_sub, fill="#F0E6E6")
    
    # Tag at 33%
    font_tag = get_font(int(h * 0.028 * 2))
    tag = "梅西 · C罗 · 莫德里奇"
    bbox = draw.textbbox((0, 0), tag, font=font_tag)
    tag_w = bbox[2] - bbox[0]
    tag_x = (img.size[0] - tag_w) // 2
    tag_y = int(img.size[1] * 0.34)
    draw.text((tag_x, tag_y), tag, font=font_tag, fill="#CCCCCC")
    
    # Bottom tag
    font_bottom = get_font(int(h * 0.025 * 2))
    bottom_text = "#世界杯里看世界 #小众国家游记"
    bbox = draw.textbbox((0, 0), bottom_text, font=font_bottom)
    bw = bbox[2] - bbox[0]
    bx = (img.size[0] - bw) // 2
    by = int(img.size[1] * 0.88)
    draw.text((bx, by), bottom_text, font=font_bottom, fill="#999999")
    
    result = Image.alpha_composite(img, overlay)
    result.convert("RGB").save(out_path, "JPEG", quality=95)
    print(f"Cover saved: {out_path} ({result.size})")

def overlay_card2(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    w, h = img.size
    img = img.resize((w*2, h*2), Image.LANCZOS)
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_title = get_font(int(h * 0.05 * 2))
    font_body = get_font(int(h * 0.032 * 2))
    
    title = "2006 德国世界杯 — 开始"
    bbox = draw.textbbox((0, 0), title, font=font_title)
    tw = bbox[2] - bbox[0]
    tx = int(img.size[0] * 0.08)
    draw.text((tx, int(img.size[1] * 0.06)), title, font=font_title, fill="#FFFFFF")
    
    points = [
        "梅西 18岁，青涩少年",
        "C罗 21岁，曼联7号",
        "莫德里奇 21岁，热刺新人",
        "那时谁也不知道——"
    ]
    y = int(img.size[1] * 0.18)
    for pt in points:
        draw.text((tx, y), f"▸ {pt}", font=font_body, fill="#F0E6E6")
        y += int(img.size[1] * 0.07)
    
    font_bottom = get_font(int(h * 0.025 * 2))
    bottom_text = "#世界杯里看世界 #小众国家游记"
    bbox = draw.textbbox((0, 0), bottom_text, font=font_bottom)
    bw = bbox[2] - bbox[0]
    bx = (img.size[0] - bw) // 2
    by = int(img.size[1] * 0.88)
    draw.text((bx, by), bottom_text, font=font_bottom, fill="#999999")
    
    result = Image.alpha_composite(img, overlay)
    result.convert("RGB").save(out_path, "JPEG", quality=95)
    print(f"Card 2 saved: {out_path} ({result.size})")

def overlay_card3(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    w, h = img.size
    img = img.resize((w*2, h*2), Image.LANCZOS)
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_title = get_font(int(h * 0.05 * 2))
    font_body = get_font(int(h * 0.028 * 2))
    
    title = "十年·五届世界杯 — 命运交织"
    bbox = draw.textbbox((0, 0), title, font=font_title)
    tw = bbox[2] - bbox[0]
    tx = int(img.size[0] * 0.08)
    draw.text((tx, int(img.size[1] * 0.06)), title, font=font_title, fill="#FFFFFF")
    
    points = [
        "2010 梅西第一次接近大力神杯",
        "2014 C罗本土悲情，梅西亚军",
        "2018 莫德里奇MVP，克罗地亚亚军",
        "2022 梅西加冕，C罗落泪"
    ]
    y = int(img.size[1] * 0.18)
    for pt in points:
        draw.text((tx, y), f"▸ {pt}", font=font_body, fill="#F0E6E6")
        y += int(img.size[1] * 0.10)
    
    font_bottom = get_font(int(h * 0.025 * 2))
    bottom_text = "#世界杯里看世界 #小众国家游记"
    bbox = draw.textbbox((0, 0), bottom_text, font=font_bottom)
    bw = bbox[2] - bbox[0]
    bx = (img.size[0] - bw) // 2
    by = int(img.size[1] * 0.88)
    draw.text((bx, by), bottom_text, font=font_bottom, fill="#999999")
    
    result = Image.alpha_composite(img, overlay)
    result.convert("RGB").save(out_path, "JPEG", quality=95)
    print(f"Card 3 saved: {out_path} ({result.size})")

def overlay_card4(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    w, h = img.size
    img = img.resize((w*2, h*2), Image.LANCZOS)
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_title = get_font(int(h * 0.05 * 2))
    font_sub = get_font(int(h * 0.035 * 2))
    font_body = get_font(int(h * 0.032 * 2))
    
    title = "2026 — 最后一次"
    bbox = draw.textbbox((0, 0), title, font=font_title)
    tw = bbox[2] - bbox[0]
    tx = int(img.size[0] * 0.08)
    draw.text((tx, int(img.size[1] * 0.06)), title, font=font_title, fill="#FFFFFF")
    
    sub = "39岁 · 41岁 · 40岁"
    bbox = draw.textbbox((0, 0), sub, font=font_sub)
    sw = bbox[2] - bbox[0]
    sx = (img.size[0] - sw) // 2
    draw.text((sx, int(img.size[1] * 0.16)), sub, font=font_sub, fill="#FFCCCC")
    
    points = [
        "同一个球场",
        "三双不同的球鞋",
        "二十年的光阴"
    ]
    y = int(img.size[1] * 0.25)
    for pt in points:
        bbox = draw.textbbox((0, 0), pt, font=font_body)
        pw = bbox[2] - bbox[0]
        px = (img.size[0] - pw) // 2
        draw.text((px, y), pt, font=font_body, fill="#F0E6E6")
        y += int(img.size[1] * 0.08)
    
    font_bottom = get_font(int(h * 0.025 * 2))
    bottom_text = "#世界杯里看世界 #小众国家游记"
    bbox = draw.textbbox((0, 0), bottom_text, font=font_bottom)
    bw = bbox[2] - bbox[0]
    bx = (img.size[0] - bw) // 2
    by = int(img.size[1] * 0.88)
    draw.text((bx, by), bottom_text, font=font_bottom, fill="#999999")
    
    result = Image.alpha_composite(img, overlay)
    result.convert("RGB").save(out_path, "JPEG", quality=95)
    print(f"Card 4 saved: {out_path} ({result.size})")

def overlay_ending(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    w, h = img.size
    img = img.resize((w*2, h*2), Image.LANCZOS)
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_title = get_font(int(h * 0.055 * 2))
    font_sub = get_font(int(h * 0.035 * 2))
    font_cta = get_font(int(h * 0.03 * 2))
    font_bottom = get_font(int(h * 0.025 * 2))
    
    title = "青春不过几届世界杯"
    bbox = draw.textbbox((0, 0), title, font=font_title)
    tw = bbox[2] - bbox[0]
    tx = (img.size[0] - tw) // 2
    draw.text((tx, int(img.size[1] * 0.2)), title, font=font_title, fill="#FFFFFF")
    
    sub = "谢谢你们，陪伴的那些年"
    bbox = draw.textbbox((0, 0), sub, font=font_sub)
    sw = bbox[2] - bbox[0]
    sx = (img.size[0] - sw) // 2
    draw.text((sx, int(img.size[1] * 0.35)), sub, font=font_sub, fill="#F0E6E6")
    
    cta = "你最早看他们踢球是哪一年？"
    bbox = draw.textbbox((0, 0), cta, font=font_cta)
    cw = bbox[2] - bbox[0]
    cx = (img.size[0] - cw) // 2
    draw.text((cx, int(img.size[1] * 0.55)), cta, font=font_cta, fill="#FFCCCC")
    
    bottom_text = "#世界杯里看世界 #小众国家游记"
    bbox = draw.textbbox((0, 0), bottom_text, font=font_bottom)
    bw = bbox[2] - bbox[0]
    bx = (img.size[0] - bw) // 2
    by = int(img.size[1] * 0.88)
    draw.text((bx, by), bottom_text, font=font_bottom, fill="#999999")
    
    result = Image.alpha_composite(img, overlay)
    result.convert("RGB").save(out_path, "JPEG", quality=95)
    print(f"Ending saved: {out_path} ({result.size})")

if __name__ == "__main__":
    print("Processing images at 2x resolution...")
    overlay_cover(f"{BASE}/01-cover0_0.png", f"{BASE}/01-cover.png")
    overlay_card2(f"{BASE}/02-content0_0.png", f"{BASE}/02-content.png")
    overlay_card3(f"{BASE}/03-content0_0.png", f"{BASE}/03-content.png")
    overlay_card4(f"{BASE}/04-content0_0.png", f"{BASE}/04-content.png")
    overlay_ending(f"{BASE}/05-ending0_0.png", f"{BASE}/05-ending.png")
    print("Done!")
