#!/usr/bin/env python3
"""Generate 8 social cards for Codex Plugin Deep Dive."""

from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Card dimensions
WIDTH, HEIGHT = 1080, 1080

# Light mode colors (Chinese cards)
LIGHT_PAPER = "#FAF7F2"
LIGHT_INK = "#1E293B"
LIGHT_ACCENT = "#002FA7"

# Dark mode colors (English cards)
DARK_PAPER = "#0B1027"
DARK_INK = "#F8FAFC"
DARK_ACCENT = "#C5E803"


def get_font(size, bold=False):
    font_paths = [
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except:
                continue
    return ImageFont.load_default()


def create_light_card(text_lines, accent_color=LIGHT_ACCENT, output_path=None):
    """Create a light mode card with centered text."""
    img = Image.new("RGB", (WIDTH, HEIGHT), LIGHT_PAPER)
    draw = ImageDraw.Draw(img)
    
    # Draw accent bar at top
    bar_width = 120
    bar_height = 6
    bar_x = (WIDTH - bar_width) // 2
    bar_y = HEIGHT // 2 - 200
    draw.rectangle([bar_x, bar_y, bar_x + bar_width, bar_y + bar_height], fill=accent_color)
    
    # Calculate text positioning for multi-line text
    y_start = HEIGHT // 2 - 80
    line_height = 120
    
    # Use large font for main text
    font_large = get_font(100)
    
    for i, line in enumerate(text_lines):
        # Get text bbox to center it
        bbox = draw.textbbox((0, 0), line, font=font_large)
        text_width = bbox[2] - bbox[0]
        x = (WIDTH - text_width) // 2
        y = y_start + i * line_height
        draw.text((x, y), line, fill=LIGHT_INK, font=font_large)
    
    if output_path:
        img.save(output_path, "PNG", quality=95)
        print(f"✓ Saved: {output_path}")
    return img


def create_dark_card(text_lines, accent_color=DARK_ACCENT, output_path=None):
    """Create a dark mode card with centered text."""
    img = Image.new("RGB", (WIDTH, HEIGHT), DARK_PAPER)
    draw = ImageDraw.Draw(img)
    
    # Draw accent bar at top
    bar_width = 120
    bar_height = 6
    bar_x = (WIDTH - bar_width) // 2
    bar_y = HEIGHT // 2 - 200
    draw.rectangle([bar_x, bar_y, bar_x + bar_width, bar_y + bar_height], fill=accent_color)
    
    # Calculate text positioning for multi-line text
    y_start = HEIGHT // 2 - 80
    line_height = 120
    
    # Use large font for main text
    font_large = get_font(100)
    
    for i, line in enumerate(text_lines):
        # Get text bbox to center it
        bbox = draw.textbbox((0, 0), line, font=font_large)
        text_width = bbox[2] - bbox[0]
        x = (WIDTH - text_width) // 2
        y = y_start + i * line_height
        draw.text((x, y), line, fill=DARK_INK, font=font_large)
    
    if output_path:
        img.save(output_path, "PNG", quality=95)
        print(f"✓ Saved: {output_path}")
    return img


def main():
    """Generate all 8 cards."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Chinese Light Cards (4 cards)
    cn_cards = [
        ("card-cn-01-cover.png", ["Codex插件", "深度解析"]),
        ("card-cn-02-architect.png", ["架构师", "系统级设计"]),
        ("card-cn-03-reviewer.png", ["代码审查员", "Bug猎手"]),
        ("card-cn-04-docwriter.png", ["文档撰写员", "注释自动生成"]),
    ]
    
    print("🇨🇳 Generating Chinese Light Cards...")
    for filename, text_lines in cn_cards:
        create_light_card(text_lines, output_path=os.path.join(OUTPUT_DIR, filename))
    
    # English Dark Cards (4 cards)
    en_cards = [
        ("card-en-01-cover.png", ["Codex Plugin", "Deep Dive"]),
        ("card-en-02-architect.png", ["ARCHITECT", "System Design"]),
        ("card-en-03-reviewer.png", ["CODE REVIEWER", "Bug Hunter"]),
        ("card-en-04-docwriter.png", ["DOC WRITER", "Auto Comments"]),
    ]
    
    print("\n🇬🇧 Generating English Dark Cards...")
    for filename, text_lines in en_cards:
        create_dark_card(text_lines, output_path=os.path.join(OUTPUT_DIR, filename))
    
    print("\n✅ All 8 cards generated successfully!")


if __name__ == "__main__":
    main()
