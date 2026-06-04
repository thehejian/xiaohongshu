#!/usr/bin/env python3
"""8 big-title cards: 4 Chinese light + 4 English dark. More visual pop, flat design, no text shadows."""
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent

CREAM = "#FAF7F2"
CREAM2 = "#F5F0E8"
TEXT = "#1E293B"
BLUE = "#2563EB"
GREEN = "#059669"
PURPLE = "#7C3AED"
ORANGE = "#D97706"
RED = "#DC2626"
PINK = "#EC4899"
TEAL = "#0D9488"
VIOLET = "#6D28D9"
DARK_BG = "#0B1027"
DARK_CARD = "#141B33"
LIGHT_BLUE = "#60A5FA"
LIGHT_GREEN = "#34D399"
LIGHT_PINK = "#F472B6"
LIGHT_YELLOW = "#FBBF24"
LIGHT_ORANGE = "#FB923C"
LIGHT_TEAL = "#2DD4BF"
LIGHT_VIOLET = "#A78BFA"

CARDS = []

# Light card color pairs (background accent, decorative)
LIGHT_STYLES = [
    (BLUE, "#DBEAFE", "🎯"),
    (GREEN, "#D1FAE5", "⚡"),
    (PURPLE, "#EDE9FE", "🔥"),
    (ORANGE, "#FEF3C7", "💰"),
]

# Dark card color pairs (text color, decorative circle color)
DARK_STYLES = [
    (LIGHT_BLUE, "#1E3A5F"),
    (LIGHT_GREEN, "#064E3B"),
    (LIGHT_PINK, "#5B1E3A"),
    (LIGHT_YELLOW, "#5C4A00"),
]


def light_card(filename, main_text, sub_text, accent, accent_bg, emoji):
    w, h = 800, 800
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{CREAM}"/>
      <stop offset="100%" stop-color="{CREAM2}"/>
    </linearGradient>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#bg)"/>
  <circle cx="100" cy="80" r="120" fill="{accent}" opacity="0.04"/>
  <circle cx="720" cy="700" r="140" fill="{accent_bg}" opacity="0.4"/>
  <circle cx="80" cy="720" r="60" fill="{accent}" opacity="0.06"/>
  <rect x="60" y="60" width="680" height="680" rx="30" fill="none" stroke="{accent}" stroke-width="1.5" opacity="0.12"/>
  <text x="{w//2}" y="300" text-anchor="middle"
        font-family="ui-sans-serif,-apple-system,sans-serif" font-size="80" font-weight="900" fill="{accent}">{emoji}</text>
  <text x="{w//2}" y="420" text-anchor="middle" dominant-baseline="central"
        font-family="ui-sans-serif,-apple-system,sans-serif" font-size="64" font-weight="900" fill="{TEXT}">{main_text}</text>
  <text x="{w//2}" y="520" text-anchor="middle" dominant-baseline="central"
        font-family="ui-sans-serif,-apple-system,sans-serif" font-size="32" font-weight="700" fill="{accent}">{sub_text}</text>
</svg>'''
    (ROOT / f"{filename}.svg").write_text(svg)
    CARDS.append(f"{filename}.svg")


def dark_card(filename, main_text, sub_text, accent, deco_color):
    w, h = 800, 800
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#141B33"/>
      <stop offset="100%" stop-color="{DARK_BG}"/>
    </radialGradient>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#bg)"/>
  <circle cx="120" cy="100" r="130" fill="{deco_color}" opacity="0.15"/>
  <circle cx="700" cy="720" r="100" fill="{deco_color}" opacity="0.1"/>
  <rect x="60" y="60" width="680" height="680" rx="30" fill="none" stroke="{accent}" stroke-width="1.5" opacity="0.15"/>
  <text x="{w//2}" y="320" text-anchor="middle" dominant-baseline="central"
        font-family="ui-sans-serif,-apple-system,sans-serif" font-size="60" font-weight="900" fill="{accent}">{main_text}</text>
  <text x="{w//2}" y="440" text-anchor="middle" dominant-baseline="central"
        font-family="ui-sans-serif,-apple-system,sans-serif" font-size="30" font-weight="700" fill="{accent}" opacity="0.85">{sub_text}</text>
</svg>'''
    (ROOT / f"{filename}.svg").write_text(svg)
    CARDS.append(f"{filename}.svg")


def main():
    # ── 4 Light Chinese cards ──
    light_card("ai-interview-lite-1", "才49块", "AI面试模拟随便练", *LIGHT_STYLES[0])
    light_card("ai-interview-lite-2", "考公考研", "结构化面试稳了", *LIGHT_STYLES[1])
    light_card("ai-interview-lite-3", "AI追问", "专挖逻辑漏洞", *LIGHT_STYLES[2])
    light_card("ai-interview-lite-4", "一杯奶茶", "换个铁饭碗", *LIGHT_STYLES[3])

    # ── 4 Dark English cards ──
    dark_card("ai-interview-dark-1", "¥49 ONLY", "AI Mock Interview", *DARK_STYLES[0])
    dark_card("ai-interview-dark-2", "CRACK IT", "Civil Service Interview", *DARK_STYLES[1])
    dark_card("ai-interview-dark-3", "AUTO-GRILL", "AI Chases Your Logic", *DARK_STYLES[2])
    dark_card("ai-interview-dark-4", "CHEAP BET", "Bubble Tea vs Career", *DARK_STYLES[3])

    print(f"Generated {len(CARDS)} SVGs")
    for name in CARDS:
        png = name.replace(".svg", ".png")
        try:
            subprocess.run([
                "inkscape", str(ROOT / name),
                "-o", str(ROOT / png),
                "-w", "800", "-h", "800"
            ], check=True, capture_output=True, timeout=60)
            print(f"  ✓ {png}")
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f"  ✗ {png} — {e}")


if __name__ == "__main__":
    main()
