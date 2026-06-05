#!/usr/bin/env python3
"""Generate 8 cards: 4 light (Chinese) + 4 dark (English). Flat, centered, no shadows. SOLUTIONS are the hero."""
import subprocess, os
ROOT = os.path.dirname(os.path.abspath(__file__))

FONT = "PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif"
FONT_EN = "Helvetica Neue, Helvetica, Arial, sans-serif"

# Light palette
LIGHT_BG = "#FAF7F2"
LIGHT_DEEP = "#1E293B"
LIGHT_BRAND = "#E63E6B"
LIGHT_BRAND2 = "#0D9488"
LIGHT_BRAND3 = "#F59E0B"
LIGHT_BRAND4 = "#8B5CF6"

# Dark palette
DARK_BG = "#0A0A14"
DARK_DEEP = "#F5F5F7"
DARK_BRAND = "#C4B5FD"
DARK_BRAND2 = "#67E8F9"
DARK_BRAND3 = "#FCD34D"
DARK_BRAND4 = "#F472B6"

def svg_wrap(w, h, body, bg):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
<rect width="{w}" height="{h}" fill="{bg}"/>
{body}
</svg>'''

# ─── Light Cards (Chinese) ───
# Card 1: Cover — the problem statement
def light_cover():
    return svg_wrap(1024, 1024, f'''
<text x="512" y="400" text-anchor="middle" dominant-baseline="middle" font-family="{FONT}" font-size="96" font-weight="900" fill="{LIGHT_DEEP}" letter-spacing="-2">与AI共事 =</text>
<text x="512" y="540" text-anchor="middle" dominant-baseline="middle" font-family="{FONT}" font-size="110" font-weight="900" fill="{LIGHT_BRAND}" letter-spacing="-3">ADHD</text>
''', LIGHT_BG)

# Card 2: The consequence
def light_card_1():
    return svg_wrap(800, 800, f'''
<text x="400" y="350" text-anchor="middle" dominant-baseline="middle" font-family="{FONT}" font-size="68" font-weight="900" fill="{LIGHT_DEEP}">越用AI</text>
<text x="400" y="460" text-anchor="middle" dominant-baseline="middle" font-family="{FONT}" font-size="68" font-weight="900" fill="{LIGHT_BRAND2}">越像机器</text>
''', LIGHT_BG)

# Card 3: THE SOLUTIONS (hero card) — 3 antidotes
def light_card_2():
    return svg_wrap(800, 800, f'''
<text x="400" y="200" text-anchor="middle" dominant-baseline="middle" font-family="{FONT}" font-size="40" font-weight="600" fill="{LIGHT_DEEP}" letter-spacing="4">解</text>
<text x="400" y="260" text-anchor="middle" dominant-baseline="middle" font-family="{FONT}" font-size="40" font-weight="600" fill="{LIGHT_DEEP}" letter-spacing="4">药</text>
<text x="400" y="380" text-anchor="middle" dominant-baseline="middle" font-family="{FONT}" font-size="96" font-weight="900" fill="{LIGHT_BRAND3}" letter-spacing="-2">3个</text>
<text x="400" y="500" text-anchor="middle" dominant-baseline="middle" font-family="{FONT}" font-size="48" font-weight="700" fill="{LIGHT_DEEP}">减少AI切换频率</text>
''', LIGHT_BG)

# Card 4: Action call
def light_card_3():
    return svg_wrap(800, 800, f'''
<text x="400" y="350" text-anchor="middle" dominant-baseline="middle" font-family="{FONT}" font-size="68" font-weight="900" fill="{LIGHT_DEEP}">AI应该</text>
<text x="400" y="460" text-anchor="middle" dominant-baseline="middle" font-family="{FONT}" font-size="68" font-weight="900" fill="{LIGHT_BRAND4}">解放你</text>
''', LIGHT_BG)

# ─── Dark Cards (English) ───
def dark_cover():
    return svg_wrap(1024, 1024, f'''
<text x="512" y="400" text-anchor="middle" dominant-baseline="middle" font-family="{FONT_EN}" font-size="96" font-weight="900" fill="{DARK_DEEP}" letter-spacing="-2">Working with AI =</text>
<text x="512" y="540" text-anchor="middle" dominant-baseline="middle" font-family="{FONT_EN}" font-size="110" font-weight="900" fill="{DARK_BRAND}" letter-spacing="-3">ADHD</text>
''', DARK_BG)

def dark_card_1():
    return svg_wrap(800, 800, f'''
<text x="400" y="350" text-anchor="middle" dominant-baseline="middle" font-family="{FONT_EN}" font-size="68" font-weight="900" fill="{DARK_DEEP}">The More You</text>
<text x="400" y="460" text-anchor="middle" dominant-baseline="middle" font-family="{FONT_EN}" font-size="68" font-weight="900" fill="{DARK_BRAND2}">Use, The More Machine</text>
''', DARK_BG)

def dark_card_2():
    return svg_wrap(800, 800, f'''
<text x="400" y="200" text-anchor="middle" dominant-baseline="middle" font-family="{FONT_EN}" font-size="36" font-weight="600" fill="{DARK_DEEP}" letter-spacing="6">A N T I D O T E S</text>
<text x="400" y="380" text-anchor="middle" dominant-baseline="middle" font-family="{FONT_EN}" font-size="96" font-weight="900" fill="{DARK_BRAND3}" letter-spacing="-2">3</text>
<text x="400" y="500" text-anchor="middle" dominant-baseline="middle" font-family="{FONT_EN}" font-size="44" font-weight="700" fill="{DARK_DEEP}">Reduce AI Switching</text>
''', DARK_BG)

def dark_card_3():
    return svg_wrap(800, 800, f'''
<text x="400" y="350" text-anchor="middle" dominant-baseline="middle" font-family="{FONT_EN}" font-size="68" font-weight="900" fill="{DARK_DEEP}">AI Should</text>
<text x="400" y="460" text-anchor="middle" dominant-baseline="middle" font-family="{FONT_EN}" font-size="68" font-weight="900" fill="{DARK_BRAND4}">Liberate You</text>
''', DARK_BG)

if __name__ == "__main__":
    cards = [
        ("adhd-cover-light", light_cover(), 1024, 1024),
        ("adhd-card-1-light", light_card_1(), 800, 800),
        ("adhd-card-2-light", light_card_2(), 800, 800),
        ("adhd-banner-light", light_card_3(), 800, 800),
        ("adhd-cover-dark", dark_cover(), 1024, 1024),
        ("adhd-card-1-dark", dark_card_1(), 800, 800),
        ("adhd-card-2-dark", dark_card_2(), 800, 800),
        ("adhd-banner-dark", dark_card_3(), 800, 800),
    ]
    for name, svg, w, h in cards:
        svg_path = os.path.join(ROOT, f"{name}.svg")
        png_path = os.path.join(ROOT, f"{name}.png")
        with open(svg_path, "w") as f:
            f.write(svg)
        subprocess.run(["inkscape", svg_path, "-o", png_path, "-w", str(w), "-h", str(h)], check=True, capture_output=True)
        sz = os.path.getsize(png_path) // 1024
        print(f"  {name}.png ({sz} KB)")
    print("Done! 8 cards generated (4 light + 4 dark).")