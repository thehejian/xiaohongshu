#!/usr/bin/env python3
"""Generate 8 social cards with strict centering and correct font colors."""

from PIL import Image, ImageDraw, ImageFont
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
W, H = 1024, 1024

FONT_HEITI = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_ARIAL = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_COURIER = "/System/Library/Fonts/Supplemental/Courier New.ttf"

def fnt(path, size):
    return ImageFont.truetype(path, size)

def center_x(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return (W - (bbox[2] - bbox[0])) // 2

def save(img, name):
    img.save(os.path.join(OUT_DIR, name), "PNG")
    print(f"✓ {name}")

# ============================================================
# LIGHT CARDS (Chinese, cream bg, deep text)
# ============================================================

def make_light_bg():
    """Cream gradient background."""
    img = Image.new("RGB", (W, H))
    for y in range(H):
        t = y / H
        r = int(250 + (245-250)*t)
        g = int(247 + (240-247)*t)
        b = int(242 + (232-242)*t)
        draw_line(img, 0, y, W, y, (r, g, b))
    return img

def draw_line(img, x1, y1, x2, y2, color):
    """Draw a horizontal line by setting pixels."""
    for x in range(x1, min(x2, W-1)+1):
        img.putpixel((x, y1), color)

# Card CN-01: Cover — "7项第一！Cosmos 3 凭什么封神？"
img = make_light_bg()
d = ImageDraw.Draw(img)

# Accent bar at top
d.rectangle([0, 0, W, 6], fill="#002FA7")

f_kicker = fnt(FONT_COURIER, 16)
f_title = fnt(FONT_HEITI, 92)
f_footer = fnt(FONT_HEITI, 18)
f_mono = fnt(FONT_COURIER, 13)

# Kicker — top
d.text((center_x(d, "NVIDIA COSMOS 3  ·  RELEASE", f_kicker), 120),
       "NVIDIA COSMOS 3  ·  RELEASE", font=f_kicker, fill="#737373")

# Main title — vertically centered
title_lines = ["7项第一", "Cosmos 3", "凭什么封神？"]
line_height = 110
total_h = len(title_lines) * line_height
start_y = (H - total_h) // 2

for i, line in enumerate(title_lines):
    if "Cosmos" in line:
        d.text((center_x(d, line, f_title), start_y + i * line_height),
               line, font=f_title, fill="#002FA7")
    else:
        d.text((center_x(d, line, f_title), start_y + i * line_height),
               line, font=f_title, fill="#0A0A0A")

# Footer
d.line([(64, H-80), (960, H-80)], fill="#D4D4D2", width=1)
d.text((64, H-55), "PHYSICAL AI  ·  OPEN MODEL", font=f_mono, fill="#737373")
d.text((960, H-55), "机器人 / 自动驾驶 / 视觉 AI", font=f_footer, fill="#737373", anchor="ra")

save(img, "card-cn-01.png")

# Card CN-02: Core Capability — "先推理，再行动"
img = make_light_bg()
d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 6], fill="#002FA7")

f_large = fnt(FONT_HEITI, 84)
f_body = fnt(FONT_HEITI, 26)

d.text((center_x(d, "CORE CAPABILITY", f_kicker), 120),
       "CORE CAPABILITY", font=f_kicker, fill="#737373")

# Centered Chinese text
zh_lines = ["先", "推理", "，再", "行动"]
line_h = 100
total = len(zh_lines) * line_h
sy = (H - total) // 2

for i, line in enumerate(zh_lines):
    color = "#002FA7" if line in ("推理", "行动") else "#0A0A0A"
    d.text((center_x(d, line, f_large), sy + i * line_h),
           line, font=f_large, fill=color)

# Accent divider
d.rectangle([480, sy + len(zh_lines)*line_h + 20, 544, sy + len(zh_lines)*line_h + 24], fill="#002FA7")

# Subtitle
d.text((center_x(d, "原生推理 + 世界生成 + 动作生成", f_body), sy + len(zh_lines)*line_h + 50),
       "原生推理 + 世界生成 + 动作生成", font=f_body, fill="#5F6D78")

# Footer
d.line([(64, H-80), (960, H-80)], fill="#D4D4D2", width=1)
d.text((64, H-55), "MIXTURE OF TRANSFORMERS", font=f_mono, fill="#737373")
d.text((960, H-55), "Think before it acts", font=f_footer, fill="#737373", anchor="ra")

save(img, "card-cn-02.png")

# Card CN-03: Benchmark — "7 项榜单第一"
img = make_light_bg()
d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 6], fill="#002FA7")

f_num = fnt(FONT_ARIAL, 150)
f_med = fnt(FONT_HEITI, 52)
f_mono16 = fnt(FONT_COURIER, 15)
f_mono14 = fnt(FONT_COURIER, 14)

d.text((center_x(d, "BENCHMARK DOMINANCE", f_kicker), 100),
       "BENCHMARK DOMINANCE", font=f_kicker, fill="#737373")

# Big number
d.text((center_x(d, "7", f_num), 280), "7", font=f_num, fill="#002FA7")
d.text((center_x(d, "项榜单第一", f_med), 380), "项榜单第一", font=f_med, fill="#0A0A0A")

# Benchmark badges — centered grid
benchmarks = ["VANTAGE-Bench", "TAR", "Artificial Analysis", "Physics-IQ", "R-Bench", "PAI-Bench"]
badge_w = 150
badge_h = 34
gap = 14
row_w = 3 * badge_w + 2 * gap
start_x = (W - row_w) // 2

for i, name in enumerate(benchmarks):
    row = i // 3
    col = i % 3
    x = start_x + col * (badge_w + gap)
    y = 460 + row * (badge_h + gap)
    d.rounded_rectangle([x, y, x + badge_w, y + badge_h], radius=4, fill="#002FA7")
    d.text((x + badge_w//2, y + badge_h//2), name, font=f_mono16, fill="#FFFFFF", anchor="mm")

# +1 more
more_w = 100
x_more = start_x + 3 * (badge_w + gap) - gap + (badge_w - more_w) // 2
y_more = 460 + 2 * (badge_h + gap)
d.rounded_rectangle([x_more, y_more, x_more + more_w, y_more + badge_h], radius=4, outline="#D4D4D2", width=1)
d.text((x_more + more_w//2, y_more + badge_h//2), "+ 1 more", font=f_mono14, fill="#737373", anchor="mm")

# Footer
d.line([(64, H-80), (960, H-80)], fill="#D4D4D2", width=1)
d.text((64, H-55), "OPEN WEIGHTS LEADERBOARD", font=f_mono, fill="#737373")
d.text((960, H-55), "这不是刷榜，是碾压", font=f_footer, fill="#737373", anchor="ra")

save(img, "card-cn-03.png")

# Card CN-04: Ecosystem — "生态已起来 开源可用"
img = make_light_bg()
d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 6], fill="#002FA7")

f_big = fnt(FONT_HEITI, 68)
f_partner = fnt(FONT_HEITI, 18)
f_quote = fnt(FONT_HEITI, 26)

d.text((center_x(d, "ECOSYSTEM  ·  OPEN SOURCE", f_kicker), 100),
       "ECOSYSTEM  ·  OPEN SOURCE", font=f_kicker, fill="#737373")

# Title
d.text((center_x(d, "生态已起来", f_big), 260), "生态已起来", font=f_big, fill="#0A0A0A")
d.text((center_x(d, "开源可用", f_big), 350), "开源可用", font=f_big, fill="#002FA7")

# Partners grid
partners = [
    ("Agile Robots", 120), ("1X Technologies", 300), ("Figure AI", 480),
    ("General Motors", 660), ("Uber", 120), ("Toyota Research", 300),
]
pw = [160, 160, 160, 180, 100, 180]
ph = 40
for i, (name, x) in enumerate(partners):
    y = 460 + (i // 3) * (ph + 12)
    w = pw[i]
    d.rounded_rectangle([x, y, x + w, y + ph], radius=6, fill="#F0F0EE", outline="#E5E5E3")
    d.text((x + w//2, y + ph//2), name, font=f_partner, fill="#5F6D78", anchor="mm")

# Quote
d.text((center_x(d, "「当别人还在收集数据时，", f_quote), 680),
       "「当别人还在收集数据时，", font=f_quote, fill="#002FA7")
d.text((center_x(d, "它已经在生成世界。」", f_quote), 720),
       "它已经在生成世界。」", font=f_quote, fill="#002FA7")

# Footer
d.line([(64, H-80), (960, H-80)], fill="#D4D4D2", width=1)
d.text((64, H-55), "HUGGING FACE  ·  OPENMDW 1.1", font=f_mono, fill="#737373")
d.text((960, H-55), "立即体验 → build.nvidia.com", font=f_footer, fill="#737373", anchor="ra")

save(img, "card-cn-04.png")

# ============================================================
# DARK CARDS (English, dark bg, light text)
# ============================================================

def make_dark_bg():
    """Radial gradient dark background."""
    img = Image.new("RGB", (W, H))
    for y in range(H):
        for x in range(W):
            dx = (x - W//2) / (W//2)
            dy = (y - H//2) / (H//2)
            dist = (dx*dx + dy*dy) ** 0.5
            t = min(dist / 1.2, 1.0)
            r = int(26*(1-t) + 6*t)
            g = int(31*(1-t) + 8*t)
            b = int(46*(1-t) + 20*t)
            img.putpixel((x, y), (r, g, b))
    return img

def draw_dark_line(img, x1, y1, x2, y2, color):
    for x in range(x1, min(x2, W-1)+1):
        img.putpixel((x, y1), color)

# Card EN-01: "COSMOS 3"
img = make_dark_bg()
d = ImageDraw.Draw(img)

# Accent dot
d.ellipse([958, 50, 970, 62], fill="#00D4FF")

f_kicker = fnt(FONT_COURIER, 15)
f_en_huge = fnt(FONT_ARIAL, 110)
f_en_footer = fnt(FONT_ARIAL, 17)
f_mono = fnt(FONT_COURIER, 13)

d.text((center_x(d, "NVIDIA  ·  COMPUTEX 2026", f_kicker), 160),
       "NVIDIA  ·  COMPUTEX 2026", font=f_kicker, fill="#5F6D78")

# COSMOS 3 — split colors
text1 = "COSMOS "
text2 = "3"
bbox1 = d.textbbox((0,0), text1, font=f_en_huge)
bbox2 = d.textbbox((0,0), text2, font=f_en_huge)
tw1 = bbox1[2] - bbox1[0]
tw2 = bbox2[2] - bbox2[0]
total_w = tw1 + tw2
sx = (W - total_w) // 2

d.text((sx, 400), text1, font=f_en_huge, fill="#F5F0E8")
d.text((sx + tw1, 400), text2, font=f_en_huge, fill="#00D4FF")

# Footer
draw_dark_line(img, 64, H-80, 960, H-80, (95, 109, 120))
d.text((64, H-55), "OPEN PHYSICAL AI MODEL", font=f_mono, fill="#5F6D78")
d.text((960, H-55), "The world foundation model", font=f_en_footer, fill="#5F6D78", anchor="ra")

save(img, "card-en-01.png")

# Card EN-02: "7 LEADERBOARDS. #1."
img = make_dark_bg()
d = ImageDraw.Draw(img)
d.ellipse([958, 50, 970, 62], fill="#00D4FF")

f_en_med = fnt(FONT_ARIAL, 44)
f_mono14 = fnt(FONT_COURIER, 14)
f_en_footer = fnt(FONT_ARIAL, 17)

d.text((center_x(d, "LEADERBOARD DOMINANCE", f_kicker), 100),
       "LEADERBOARD DOMINANCE", font=f_kicker, fill="#5F6D78")

d.text((center_x(d, "7", f_num), 280), "7", font=f_num, fill="#00D4FF")
d.text((center_x(d, "LEADERBOARDS.", f_en_med), 400), "LEADERBOARDS.", font=f_en_med, fill="#F5F0E8")
d.text((center_x(d, "#1.", f_en_med), 460), "#1.", font=f_en_med, fill="#F5F0E8")

# Benchmarks
benchmarks = ["VANTAGE", "TAR", "Artificial Analysis", "Physics-IQ", "R-Bench", "PAI-Bench"]
bw = [120, 70, 160, 110, 90, 90]
bh = 30
gap = 12
row_w = 3 * max(bw) + 2 * gap
start_x = (W - row_w) // 2

for i, name in enumerate(benchmarks):
    row = i // 3
    col = i % 3
    x = start_x + col * (max(bw) + gap) + (max(bw) - bw[i]) // 2
    y = 540 + row * (bh + gap)
    d.rounded_rectangle([x, y, x + bw[i], y + bh], radius=4, fill="#00D4FF")
    d.text((x + bw[i]//2, y + bh//2), name, font=f_mono14, fill="#060814", anchor="mm")

# +1 more
more_x = start_x + 2 * (max(bw) + gap) + (max(bw) - 90) // 2
more_y = 540 + 2 * (bh + gap)
d.rounded_rectangle([more_x, more_y, more_x + 90, more_y + bh], radius=4, outline=(50, 60, 70), width=1)
d.text((more_x + 45, more_y + bh//2), "+ 1 more", font=f_mono14, fill="#8899AA", anchor="mm")

# Footer
draw_dark_line(img, 64, H-80, 960, H-80, (95, 109, 120))
d.text((64, H-55), "OPEN WEIGHTS  ·  HUGGING FACE", font=f_mono, fill="#5F6D78")
d.text((960, H-55), "Not ranking. Domination.", font=f_en_footer, fill="#5F6D78", anchor="ra")

save(img, "card-en-02.png")

# Card EN-03: "THINK BEFORE IT ACTS"
img = make_dark_bg()
d = ImageDraw.Draw(img)
d.ellipse([958, 50, 970, 62], fill="#00D4FF")

f_en_large = fnt(FONT_ARIAL, 80)
f_en_body = fnt(FONT_ARIAL, 22)

d.text((center_x(d, "CORE PHILOSOPHY", f_kicker), 160),
       "CORE PHILOSOPHY", font=f_kicker, fill="#5F6D78")

d.text((center_x(d, "THINK BEFORE", f_en_large), 360),
       "THINK BEFORE", font=f_en_large, fill="#F5F0E8")
d.text((center_x(d, "IT ACTS", f_en_large), 460),
       "IT ACTS", font=f_en_large, fill="#00D4FF")

# Accent line
d.rectangle([488, 530, 536, 533], fill="#00D4FF")

d.text((center_x(d, "Reason first. Generate second.", f_en_body), 580),
       "Reason first. Generate second.", font=f_en_body, fill="#8899AA")
d.text((center_x(d, "The first omni-model with native action generation.", f_en_body), 615),
       "The first omni-model with native action generation.", font=f_en_body, fill="#8899AA")

# Footer
draw_dark_line(img, 64, H-80, 960, H-80, (95, 109, 120))
d.text((64, H-55), "MIXTURE OF TRANSFORMERS", font=f_mono, fill="#5F6D78")
d.text((960, H-55), "Robotics  ·  AV  ·  Vision AI", font=f_en_footer, fill="#5F6D78", anchor="ra")

save(img, "card-en-03.png")

# Card EN-04: "THE PHYSICAL AI OS"
img = make_dark_bg()
d = ImageDraw.Draw(img)
d.ellipse([958, 50, 970, 62], fill="#00D4FF")

f_en_big = fnt(FONT_ARIAL, 64)
f_partner = fnt(FONT_ARIAL, 17)
f_quote = fnt(FONT_ARIAL, 24)

d.text((center_x(d, "ECOSYSTEM  ·  OPEN SOURCE", f_kicker), 100),
       "ECOSYSTEM  ·  OPEN SOURCE", font=f_kicker, fill="#5F6D78")

d.text((center_x(d, "THE PHYSICAL", f_en_big), 280),
       "THE PHYSICAL", font=f_en_big, fill="#F5F0E8")
d.text((center_x(d, "AI OS", f_en_big), 370),
       "AI OS", font=f_en_big, fill="#00D4FF")

# Partners
partners_en = [
    ("Agile Robots", 120, 460, 140),
    ("1X Technologies", 280, 460, 140),
    ("Figure AI", 440, 460, 120),
    ("General Motors", 600, 460, 140),
    ("Uber", 120, 516, 90),
    ("Toyota Research", 230, 516, 160),
]
for name, x, y, w in partners_en:
    d.rounded_rectangle([x, y, x + w, y + 38], radius=6, fill=(20, 25, 35), outline=(136, 153, 170))
    d.text((x + w//2, y + 19), name, font=f_partner, fill="#8899AA", anchor="mm")

# Quote
d.text((center_x(d, '"While others collect data,', f_quote), 640),
       '"While others collect data,', font=f_quote, fill="#00D4FF")
d.text((center_x(d, 'it generates the world."', f_quote), 675),
       'it generates the world."', font=f_quote, fill="#00D4FF")

# Footer
draw_dark_line(img, 64, H-80, 960, H-80, (95, 109, 120))
d.text((64, H-55), "HUGGING FACE  ·  OPENMDW 1.1", font=f_mono, fill="#5F6D78")
d.text((960, H-55), "build.nvidia.com  →", font=f_en_footer, fill="#5F6D78", anchor="ra")

save(img, "card-en-04.png")

print(f"\n✅ All 8 cards rendered to {OUT_DIR}")
