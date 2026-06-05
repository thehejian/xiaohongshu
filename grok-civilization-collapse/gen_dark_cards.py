#!/usr/bin/env python3
"""Generate dark mode social cards with clear text using PIL."""

from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/grok-civilization-collapse/output"

# Dark mode colors
BG_COLOR = (11, 16, 39)       # #0B1027
TEXT_COLOR = (248, 250, 252)  # #F8FAFC
ACCENT_COLOR = (56, 189, 248) # #38BDF8

# Card dimensions (3:4 ratio, 1080x1440)
WIDTH = 1080
HEIGHT = 1440

# Cards to generate
CARDS = [
    {
        "title": "Grok AI\nCivilization\nCollapse",
        "subtitle": "What happens next?",
        "filename": "en-dark-01.png"
    },
    {
        "title": "Collapse\nIs\nInevitable",
        "subtitle": "Not an accident",
        "filename": "en-dark-02.png"
    },
    {
        "title": "Tech Boom\n=\nFaster Death",
        "subtitle": "The paradox",
        "filename": "en-dark-03.png"
    },
    {
        "title": "Flat Societies\nSurvive\n3x Longer",
        "subtitle": "But can't handle crises",
        "filename": "en-dark-04.png"
    },
]

def get_font(size):
    """Try to get a good font, fallback to default."""
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSMono.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except:
                continue
    return ImageFont.load_default()

def create_card(card, output_path):
    """Create a dark mode card with centered text."""
    # Create dark background
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Try to load fonts
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 100)
        subtitle_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
    except:
        try:
            title_font = ImageFont.truetype("/System/Library/Fonts/SFNSMono.ttf", 100)
            subtitle_font = ImageFont.truetype("/System/Library/Fonts/SFNSMono.ttf", 48)
        except:
            title_font = get_font(100)
            subtitle_font = get_font(48)
    
    # Draw accent bar
    bar_width = 120
    bar_height = 4
    bar_x = (WIDTH - bar_width) // 2
    bar_y = HEIGHT // 2 + 180
    draw.rectangle([bar_x, bar_y, bar_x + bar_width, bar_y + bar_height], fill=ACCENT_COLOR)
    
    # Draw title (multi-line, centered)
    lines = card["title"].split("\n")
    total_height = len(lines) * 110
    start_y = (HEIGHT // 2 - total_height // 2) - 60
    
    for i, line in enumerate(lines):
        # Get text bounding box
        bbox = draw.textbbox((0, 0), line, font=title_font)
        text_width = bbox[2] - bbox[0]
        x = (WIDTH - text_width) // 2
        y = start_y + i * 110
        draw.text((x, y), line, fill=TEXT_COLOR, font=title_font)
    
    # Draw subtitle
    subtitle = card["subtitle"]
    bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    text_width = bbox[2] - bbox[0]
    x = (WIDTH - text_width) // 2
    y = bar_y + 40
    draw.text((x, y), subtitle, fill=TEXT_COLOR, font=subtitle_font)
    
    # Save
    img.save(output_path, "PNG", quality=95)
    print(f"Created: {output_path}")

def main():
    for card in CARDS:
        output_path = os.path.join(OUTPUT_DIR, card["filename"])
        create_card(card, output_path)
    print("\nAll 4 dark cards generated successfully!")

if __name__ == "__main__":
    main()
