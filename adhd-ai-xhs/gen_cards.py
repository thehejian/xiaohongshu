#!/usr/bin/env python3
"""Light-mode cards: Chinese text, absolute center, flat, no shadows, no titles, no bottom text."""
import subprocess, os
ROOT = os.path.dirname(os.path.abspath(__file__))

BG = "#FAF7F2"
BRAND = "#E63E6B"
BRAND2 = "#0D9488"
BRAND3 = "#F59E0B"
BRAND4 = "#8B5CF6"
DEEP = "#1E293B"

FONT = "PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif"

def svg_wrap(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
<rect width="{w}" height="{h}" fill="{BG}"/>
{body}
</svg>'''

def cover():
    """1024x1024 — 与AI共事 = ADHD"""
    return svg_wrap(1024, 1024, f'''
<text x="512" y="512" text-anchor="middle" dominant-baseline="middle" font-family="{FONT}" font-size="110" font-weight="900" fill="{BRAND}" letter-spacing="-2">与AI共事 = ADHD</text>
''')

def card_1():
    """800x800 — 多线程切换耗尽精力"""
    return svg_wrap(800, 800, f'''
<text x="400" y="360" text-anchor="middle" dominant-baseline="middle" font-family="{FONT}" font-size="72" font-weight="900" fill="{DEEP}">多线程切换</text>
<text x="400" y="460" text-anchor="middle" dominant-baseline="middle" font-family="{FONT}" font-size="72" font-weight="900" fill="{BRAND2}">耗尽精力</text>
''')

def card_2():
    """800x800 — 3个解药"""
    return svg_wrap(800, 800, f'''
<text x="400" y="350" text-anchor="middle" dominant-baseline="middle" font-family="{FONT}" font-size="84" font-weight="900" fill="{BRAND3}">3个解药</text>
<text x="400" y="460" text-anchor="middle" dominant-baseline="middle" font-family="{FONT}" font-size="36" font-weight="600" fill="{DEEP}">减少AI切换频率</text>
''')

def card_3():
    """800x800 — AI应该解放你"""
    return svg_wrap(800, 800, f'''
<text x="400" y="350" text-anchor="middle" dominant-baseline="middle" font-family="{FONT}" font-size="72" font-weight="900" fill="{DEEP}">AI应该</text>
<text x="400" y="460" text-anchor="middle" dominant-baseline="middle" font-family="{FONT}" font-size="72" font-weight="900" fill="{BRAND4}">解放你</text>
''')

if __name__ == "__main__":
    cards = [
        ("adhd-cover", cover(), 1024, 1024),
        ("adhd-card-1", card_1(), 800, 800),
        ("adhd-card-2", card_2(), 800, 800),
        ("adhd-banner", card_3(), 800, 800),
    ]
    for name, svg, w, h in cards:
        svg_path = os.path.join(ROOT, f"{name}.svg")
        png_path = os.path.join(ROOT, f"{name}.png")
        with open(svg_path, "w") as f:
            f.write(svg)
        subprocess.run(["inkscape", svg_path, "-o", png_path, "-w", str(w), "-h", str(h)], check=True, capture_output=True)
        sz = os.path.getsize(png_path) // 1024
        print(f"  {name}.png ({sz} KB)")
    print("Done!")