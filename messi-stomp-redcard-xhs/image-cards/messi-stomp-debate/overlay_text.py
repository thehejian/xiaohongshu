#!/usr/bin/env python3
"""Overlay Chinese text onto textless images using Pillow."""

from PIL import Image, ImageDraw, ImageFont
import os

BASE = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/86ba2c91f017a3749571a82f2c6d890ac7ffb2fb.asset/AssetData/PingFang.ttc"

def get_font(size, weight="Semibold"):
    return ImageFont.truetype(FONT_PATH, size, index=0 if weight == "Regular" else 5)

def draw_text(draw, text, x, y, font, color="white", stroke_width=0, stroke_color="black", anchor=None):
    draw.text((x, y), text, fill=color, font=font, stroke_width=stroke_width, stroke_fill=stroke_color, anchor=anchor)

def text_size(text, font):
    bbox = font.getbbox(text)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]

def card_01_cover(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    W, H = img.size

    # Top gradient bar
    for i in range(180):
        alpha = int(180 * (1 - i / 180))
        draw.rectangle([0, i, W, i + 1], fill=(0, 0, 0, alpha))

    # Bottom gradient bar
    for i in range(160):
        alpha = int(180 * (1 - i / 160))
        draw.rectangle([0, H - 160 + i, W, H - 160 + i + 1], fill=(0, 0, 0, alpha))

    # Main title
    title = "梅西踩小腿"
    subtitle = "红牌争议"
    f1 = get_font(72)
    tw, th = text_size(title, f1)
    draw_text(draw, title, (W - tw) // 2, 30, f1, "#FF4444", stroke_width=3, stroke_color="#000000")

    f2 = get_font(64)
    sw, sh = text_size(subtitle, f2)
    draw_text(draw, subtitle, (W - sw) // 2, 30 + th + 8, f2, "#FFFFFF", stroke_width=3, stroke_color="#000000")

    # Bottom info line
    f3 = get_font(32)
    info = "世界杯第32分钟 · 引爆热搜第一"
    iw, ih = text_size(info, f3)
    draw_text(draw, info, (W - iw) // 2, H - 130, f3, "#FFD700", stroke_width=2, stroke_color="#000000")

    # Weibo tag
    tag = "#微博热搜 No.1"
    f4 = get_font(28)
    tag_w, tag_h = text_size(tag, f4)
    draw_text(draw, tag, (W - tag_w) // 2, H - 80, f4, "#FF6B6B", stroke_width=1, stroke_color="#000000")

    result = Image.alpha_composite(img, overlay).convert("RGB")
    result.save(out_path, quality=95)
    print(f"  Saved: {out_path}")


def card_02_debate(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    W, H = img.size

    # Top gradient bar
    for i in range(120):
        alpha = int(160 * (1 - i / 120))
        draw.rectangle([0, i, W, i + 1], fill=(0, 0, 0, alpha))

    # Bottom bar
    for i in range(100):
        alpha = int(160 * (1 - i / 100))
        draw.rectangle([0, H - 100 + i, W, H - 100 + i + 1], fill=(0, 0, 0, alpha))

    # Title
    title = "观点大对决"
    f1 = get_font(56)
    tw, th = text_size(title, f1)
    draw_text(draw, title, (W - tw) // 2, 25, f1, "#FFFFFF", stroke_width=3, stroke_color="#000000")

    # Left side: ESPN
    f2 = get_font(44)
    left_label = "ESPN:"
    right_label = "亨利:"

    lw, lh = text_size(left_label, f2)
    draw_text(draw, left_label, W // 4 - lw // 2, 100, f2, "#FF4444", stroke_width=2, stroke_color="#000000")

    f3 = get_font(38)
    left_text = "100% 红牌！"
    lw2, lh2 = text_size(left_text, f3)
    draw_text(draw, left_text, W // 4 - lw2 // 2, 100 + lh + 5, f3, "#FF8888", stroke_width=2, stroke_color="#000000")

    # Right side: Henry
    rw, rh = text_size(right_label, f2)
    draw_text(draw, right_label, 3 * W // 4 - rw // 2, 100, f2, "#66BBFF", stroke_width=2, stroke_color="#000000")

    rw2, rh2 = text_size(left_text, f3)
    right_text = "看意图，非故意"
    rw3, rh3 = text_size(right_text, f3)
    draw_text(draw, right_text, 3 * W // 4 - rw3 // 2, 100 + rh + 5, f3, "#99CCFF", stroke_width=2, stroke_color="#000000")

    # Bottom vs divider label
    vs = "⚽ 你站哪边？"
    f4 = get_font(32)
    vw, vh = text_size(vs, f4)
    draw_text(draw, vs, (W - vw) // 2, H - 80, f4, "#FFD700", stroke_width=2, stroke_color="#000000")

    result = Image.alpha_composite(img, overlay).convert("RGB")
    result.save(out_path, quality=95)
    print(f"  Saved: {out_path}")


def card_03_rules(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    W, H = img.size

    # Top gradient bar
    for i in range(100):
        alpha = int(160 * (1 - i / 100))
        draw.rectangle([0, i, W, i + 1], fill=(0, 0, 0, alpha))

    # Bottom gradient bar
    for i in range(100):
        alpha = int(160 * (1 - i / 100))
        draw.rectangle([0, H - 100 + i, W, H - 100 + i + 1], fill=(0, 0, 0, alpha))

    # Title
    title = "按规则，三条全占"
    f1 = get_font(52)
    tw, th = text_size(title, f1)
    draw_text(draw, title, (W - tw) // 2, 20, f1, "#FFD700", stroke_width=3, stroke_color="#000000")

    # Three rule items evenly spaced
    items = [
        ("① 亮鞋钉", "#FF6666"),
        ("② 踩小腿", "#FFAA44"),
        ("③ 从背后", "#FF4444"),
    ]
    f2 = get_font(48)
    item_y = 120
    gap = 115

    for i, (item, color) in enumerate(items):
        iw, ih = text_size(item, f2)
        draw_text(draw, item, (W - iw) // 2, item_y + i * gap, f2, color, stroke_width=3, stroke_color="#000000")

        # Checkmark for each
        f_check = get_font(32)
        check = "✓"
        cw, ch = text_size(check, f_check)
        draw_text(draw, check, (W - iw) // 2 + iw + 15, item_y + i * gap + 5, f_check, "#44FF44", stroke_width=2, stroke_color="#000000")

    # Bottom verdict
    verdict = "裁判结果：仅判犯规 · 未给牌"
    f3 = get_font(32)
    vw, vh = text_size(verdict, f3)
    draw_text(draw, verdict, (W - vw) // 2, H - 80, f3, "#FFFFFF", stroke_width=2, stroke_color="#000000")

    result = Image.alpha_composite(img, overlay).convert("RGB")
    result.save(out_path, quality=95)
    print(f"  Saved: {out_path}")


def card_04_ending(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    W, H = img.size

    # Bottom gradient bar (stronger)
    for i in range(200):
        alpha = int(220 * (1 - i / 200))
        draw.rectangle([0, H - 200 + i, W, H - 200 + i + 1], fill=(0, 0, 0, alpha))

    # Main question
    question = "不给牌"
    f1 = get_font(80)
    qw, qh = text_size(question, f1)
    draw_text(draw, question, (W - qw) // 2, H - 190, f1, "#FFFFFF", stroke_width=4, stroke_color="#000000")

    question2 = "合理吗？"
    f2 = get_font(72)
    qw2, qh2 = text_size(question2, f2)
    draw_text(draw, question2, (W - qw2) // 2, H - 190 + qh + 5, f2, "#FFD700", stroke_width=4, stroke_color="#000000")

    # Subtext
    sub = "世界杯最后一舞 vs 规则公平性"
    f3 = get_font(30)
    sw, sh = text_size(sub, f3)
    draw_text(draw, sub, (W - sw) // 2, H - 190 + qh + qh2 + 20, f3, "#CCCCCC", stroke_width=1, stroke_color="#000000")

    # Hashtags
    tags = "#梅西 #世界杯 #红牌争议"
    f4 = get_font(26)
    tw, th = text_size(tags, f4)
    draw_text(draw, tags, (W - tw) // 2, H - 45, f4, "#90CAF9", stroke_width=1, stroke_color="#000000")

    result = Image.alpha_composite(img, overlay).convert("RGB")
    result.save(out_path, quality=95)
    print(f"  Saved: {out_path}")


if __name__ == "__main__":
    out_dir = os.path.join(BASE, "output")
    os.makedirs(out_dir, exist_ok=True)

    C = lambda name: os.path.join(BASE, f"{name}0_0.png")

    print("Card 1: Cover")
    card_01_cover(C("01-cover"), os.path.join(out_dir, "01-cover-overlay.png"))

    print("Card 2: Debate")
    card_02_debate(C("02-debate"), os.path.join(out_dir, "02-debate-overlay.png"))

    print("Card 3: Rules")
    card_03_rules(C("03-rules"), os.path.join(out_dir, "03-rules-overlay.png"))

    print("Card 4: Ending")
    card_04_ending(C("04-ending"), os.path.join(out_dir, "04-ending-overlay.png"))

    print("\nAll done!")