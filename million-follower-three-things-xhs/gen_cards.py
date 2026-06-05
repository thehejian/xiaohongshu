#!/usr/bin/env python3
"""Generate 8 cards: 4 light (Chinese) + 4 dark (English).
Flat design, centered text, no shadows, no white/gray on light, no dark on dark."""
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent

# --- Light palette ---
LTEXT = "#1E293B"
LBLUE = "#2563EB"
LBLUE_BG = "#DBEAF4"
LPURPLE = "#7C3AED"
LPURPLE_BG = "#EDE9FE"
LGREEN = "#059669"
LGREEN_BG = "#D1FAE5"
LPINK_BG = "#FCE7F3"
LINDIGO_BG = "#E0E7FF"

# --- Dark palette ---
DWHITE = "#FFFFFF"
DLIGHT = "#E2E8F0"
DBLUE = "#93C5FD"
DBLUE_BG = "#1E3A5F"
DPURPLE = "#C4B5FD"
DPURPLE_BG = "#2D1B69"
DGREEN = "#86EFAC"
DGREEN_BG = "#064E3B"
DPINK = "#F9A8D4"
DINDIGO = "#A5B4FC"

CARDS = []

# ========== LIGHT CHINESE ==========

def light_cover():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F0EAE0"/>
    </radialGradient>
    <linearGradient id="titleG" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2563EB"/>
      <stop offset="50%" stop-color="#7C3AED"/>
      <stop offset="100%" stop-color="#EC4899"/>
    </linearGradient>
  </defs>
  <rect width="1024" height="1024" fill="url(#bg)"/>
  <circle cx="80" cy="80" r="120" fill="{LBLUE_BG}" opacity="0.35"/>
  <circle cx="944" cy="120" r="90" fill="{LPURPLE_BG}" opacity="0.35"/>
  <circle cx="120" cy="944" r="100" fill="{LPINK_BG}" opacity="0.25"/>
  <circle cx="924" cy="900" r="80" fill="{LINDIGO_BG}" opacity="0.25"/>
  <text x="512" y="420" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="130" font-weight="900" fill="url(#titleG)">普通人</text>
  <text x="512" y="560" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="130" font-weight="900" fill="url(#titleG)">逆袭三件套</text>
  <text x="512" y="650" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="36" font-weight="700" fill="{LTEXT}">自媒体 \u00b7 AI \u00b7 投资</text>
  <rect x="42" y="730" width="290" height="200" rx="24" fill="{LBLUE_BG}"/>
  <text x="187" y="805" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="44" font-weight="900" fill="{LBLUE}">01</text>
  <text x="187" y="860" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="34" font-weight="800" fill="{LTEXT}">自媒体</text>
  <text x="187" y="895" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="22" fill="{LBLUE}">最低成本杠杆</text>
  <rect x="367" y="730" width="290" height="200" rx="24" fill="{LPURPLE_BG}"/>
  <text x="512" y="805" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="44" font-weight="900" fill="{LPURPLE}">02</text>
  <text x="512" y="860" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="34" font-weight="800" fill="{LTEXT}">AI</text>
  <text x="512" y="895" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="22" fill="{LPURPLE}">一个人就是团队</text>
  <rect x="692" y="730" width="290" height="200" rx="24" fill="{LGREEN_BG}"/>
  <text x="837" y="805" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="44" font-weight="900" fill="{LGREEN}">03</text>
  <text x="837" y="860" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="34" font-weight="800" fill="{LTEXT}">投资</text>
  <text x="837" y="895" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="22" fill="{LGREEN}">复利 + 资产意识</text>
  <text x="512" y="1000" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="26" font-weight="700" fill="{LBLUE}">内容天然有传播结构</text>
</svg>'''
    (ROOT / "cover.svg").write_text(svg)
    CARDS.append(("cover.svg", 1024))


def light_card1():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="65%">
      <stop offset="0%" stop-color="#E8F4FD"/>
      <stop offset="100%" stop-color="#DBEAF4"/>
    </radialGradient>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <circle cx="100" cy="100" r="120" fill="#C7E2F5" opacity="0.3"/>
  <circle cx="700" cy="700" r="100" fill="#C7E2F5" opacity="0.25"/>
  <text x="400" y="400" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="96" font-weight="900" fill="{LBLUE}">自媒体</text>
  <text x="400" y="480" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="42" font-weight="800" fill="{LTEXT}">最低成本的杠杆</text>
</svg>'''
    (ROOT / "card-1.svg").write_text(svg)
    CARDS.append(("card-1.svg", 800))


def light_card2():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="65%">
      <stop offset="0%" stop-color="#F2EDFE"/>
      <stop offset="100%" stop-color="#EDE9FE"/>
    </radialGradient>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <circle cx="100" cy="100" r="120" fill="#DDD6FE" opacity="0.3"/>
  <circle cx="700" cy="700" r="100" fill="#DDD6FE" opacity="0.25"/>
  <text x="400" y="400" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="96" font-weight="900" fill="{LPURPLE}">AI</text>
  <text x="400" y="480" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="42" font-weight="800" fill="{LTEXT}">一个人就是一个团队</text>
</svg>'''
    (ROOT / "card-2.svg").write_text(svg)
    CARDS.append(("card-2.svg", 800))


def light_card3():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="65%">
      <stop offset="0%" stop-color="#DCFCE7"/>
      <stop offset="100%" stop-color="#D1FAE5"/>
    </radialGradient>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <circle cx="100" cy="100" r="120" fill="#A7F3D0" opacity="0.3"/>
  <circle cx="700" cy="700" r="100" fill="#A7F3D0" opacity="0.25"/>
  <text x="400" y="400" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="96" font-weight="900" fill="{LGREEN}">投资</text>
  <text x="400" y="480" text-anchor="middle" font-family="ui-sans-serif, PingFang SC, -apple-system, sans-serif" font-size="42" font-weight="800" fill="{LTEXT}">复利 + 资产意识</text>
</svg>'''
    (ROOT / "card-3.svg").write_text(svg)
    CARDS.append(("card-3.svg", 800))


# ========== DARK ENGLISH ==========

def dark_cover():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#141A3A"/>
      <stop offset="100%" stop-color="#0B1027"/>
    </radialGradient>
    <linearGradient id="titleG" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#93C5FD"/>
      <stop offset="50%" stop-color="#C4B5FD"/>
      <stop offset="100%" stop-color="#F9A8D4"/>
    </linearGradient>
  </defs>
  <rect width="1024" height="1024" fill="url(#bg)"/>
  <circle cx="80" cy="80" r="120" fill="{DBLUE_BG}" opacity="0.5"/>
  <circle cx="944" cy="120" r="90" fill="{DPURPLE_BG}" opacity="0.5"/>
  <circle cx="120" cy="944" r="100" fill="{DGREEN_BG}" opacity="0.4"/>
  <circle cx="924" cy="900" r="80" fill="{DBLUE_BG}" opacity="0.4"/>

  <text x="512" y="350" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="90" font-weight="900" fill="url(#titleG)">ORDINARY PEOPLE</text>
  <text x="512" y="470" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="90" font-weight="900" fill="url(#titleG)">NEED JUST</text>
  <text x="512" y="590" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="90" font-weight="900" fill="url(#titleG)">THREE THINGS</text>

  <text x="512" y="680" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="32" font-weight="600" fill="{DLIGHT}">Content Creation \u00b7 AI \u00b7 Investment</text>

  <rect x="42" y="740" width="290" height="190" rx="24" fill="{DBLUE_BG}" opacity="0.6"/>
  <text x="187" y="810" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="36" font-weight="900" fill="{DBLUE}">01</text>
  <text x="187" y="860" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="{DWHITE}">Content</text>
  <text x="187" y="895" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="{DWHITE}">Creation</text>

  <rect x="367" y="740" width="290" height="190" rx="24" fill="{DPURPLE_BG}" opacity="0.6"/>
  <text x="512" y="810" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="36" font-weight="900" fill="{DPURPLE}">02</text>
  <text x="512" y="860" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="{DWHITE}">AI</text>
  <text x="512" y="895" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="{DWHITE}">Force Multiplier</text>

  <rect x="692" y="740" width="290" height="190" rx="24" fill="{DGREEN_BG}" opacity="0.6"/>
  <text x="837" y="810" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="36" font-weight="900" fill="{DGREEN}">03</text>
  <text x="837" y="860" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="{DWHITE}">Investment</text>
  <text x="837" y="895" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="{DWHITE}">Compounding</text>

  <text x="512" y="1005" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="600" fill="{DBLUE}">Content that spreads itself</text>
</svg>'''
    (ROOT / "cover-dark.svg").write_text(svg)
    CARDS.append(("cover-dark.svg", 1024))


def dark_card1():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="65%">
      <stop offset="0%" stop-color="#1E3A5F"/>
      <stop offset="100%" stop-color="#162D4A"/>
    </radialGradient>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <circle cx="100" cy="100" r="120" fill="{DBLUE_BG}" opacity="0.4"/>
  <circle cx="700" cy="700" r="100" fill="{DBLUE_BG}" opacity="0.3"/>
  <text x="400" y="390" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="96" font-weight="900" fill="{DBLUE}">Content</text>
  <text x="400" y="490" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="42" font-weight="800" fill="{DWHITE}">The Cheapest Leverage</text>
</svg>'''
    (ROOT / "card-1-dark.svg").write_text(svg)
    CARDS.append(("card-1-dark.svg", 800))


def dark_card2():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="65%">
      <stop offset="0%" stop-color="#2D1B69"/>
      <stop offset="100%" stop-color="#1F1250"/>
    </radialGradient>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <circle cx="100" cy="100" r="120" fill="{DPURPLE_BG}" opacity="0.4"/>
  <circle cx="700" cy="700" r="100" fill="{DPURPLE_BG}" opacity="0.3"/>
  <text x="400" y="390" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="120" font-weight="900" fill="{DPURPLE}">AI</text>
  <text x="400" y="490" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="42" font-weight="800" fill="{DWHITE}">You Are a Team of One</text>
</svg>'''
    (ROOT / "card-2-dark.svg").write_text(svg)
    CARDS.append(("card-2-dark.svg", 800))


def dark_card3():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="65%">
      <stop offset="0%" stop-color="#064E3B"/>
      <stop offset="100%" stop-color="#043A2C"/>
    </radialGradient>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <circle cx="100" cy="100" r="120" fill="{DGREEN_BG}" opacity="0.4"/>
  <circle cx="700" cy="700" r="100" fill="{DGREEN_BG}" opacity="0.3"/>
  <text x="400" y="390" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="96" font-weight="900" fill="{DGREEN}">Invest</text>
  <text x="400" y="490" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="42" font-weight="800" fill="{DWHITE}">Build Asset Awareness</text>
</svg>'''
    (ROOT / "card-3-dark.svg").write_text(svg)
    CARDS.append(("card-3-dark.svg", 800))


def main():
    light_cover()
    light_card1()
    light_card2()
    light_card3()
    dark_cover()
    dark_card1()
    dark_card2()
    dark_card3()

    print(f"Generated {len(CARDS)} SVGs")
    for name, size in CARDS:
        png = name.replace(".svg", ".png")
        subprocess.run([
            "inkscape", str(ROOT / name),
            "-o", str(ROOT / png),
            "-w", str(size), "-h", str(size)
        ], check=True)
        print(f"  \u2713 {png}")


if __name__ == "__main__":
    main()