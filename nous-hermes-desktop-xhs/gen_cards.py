#!/usr/bin/env python3
"""Generate 8 cards: 4 light Chinese + 4 dark English for Hermes Desktop Beta."""
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent

CREAM = "#FAF7F2"
CREAM2 = "#F5F0E8"
TEXT = "#1E293B"
TEXT_DIM = "#64748B"
BLUE = "#2563EB"
PURPLE = "#7C3AED"
GREEN = "#059669"
ORANGE = "#D97706"

DARK_BG = "#0B1027"
DARK_CARD = "#141B33"
DARK_TEXT = "#E2E8F0"
DARK_DIM = "#8892B0"
DARK_BLUE = "#60A5FA"
DARK_PURPLE = "#A78BFA"
DARK_GREEN = "#34D399"
DARK_PINK = "#F472B6"

CARDS = []


def zh_cover():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{CREAM}"/>
      <stop offset="100%" stop-color="{CREAM2}"/>
    </linearGradient>
    <linearGradient id="titleG" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{BLUE}"/>
      <stop offset="50%" stop-color="{PURPLE}"/>
      <stop offset="100%" stop-color="{ORANGE}"/>
    </linearGradient>
  </defs>
  <rect width="1024" height="1024" fill="url(#bg)"/>
  <text x="512" y="400" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="72" font-weight="900" fill="{TEXT}">英伟达GTC首秀</text>
  <text x="512" y="520" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="88" font-weight="900" fill="url(#titleG)">开源桌面Agent</text>
   <text x="512" y="640" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="36" font-weight="600" fill="{TEXT_DIM}">Hermes Desktop Beta · MIT</text>
  <text x="512" y="950" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{BLUE}">一行命令安装 → curl -fsSL hermes-agent.nousresearch.com/install.sh | bash</text>
</svg>'''
    (ROOT / "nhd-cover-zh.svg").write_text(svg)
    CARDS.append(("nhd-cover-zh.svg", 1024))


def zh_card_1():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{CREAM}"/>
      <stop offset="100%" stop-color="{CREAM2}"/>
    </linearGradient>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <text x="400" y="360" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="60" font-weight="900" fill="{TEXT}">这不是网页AI</text>
  <text x="400" y="460" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="60" font-weight="900" fill="{BLUE}">是跑在桌面的Agent</text>
  <text x="400" y="560" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" font-weight="500" fill="{TEXT_DIM}">7x24后台运行 · 跨会话记忆 · 自主执行</text>
</svg>'''
    (ROOT / "nhd-card-1-zh.svg").write_text(svg)
    CARDS.append(("nhd-card-1-zh.svg", 800))


def zh_card_2():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{CREAM}"/>
      <stop offset="100%" stop-color="{CREAM2}"/>
    </linearGradient>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <text x="400" y="340" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="56" font-weight="900" fill="{TEXT}">7x24</text>
  <text x="400" y="440" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="56" font-weight="900" fill="{PURPLE}">后台沉默运行</text>
  <text x="400" y="540" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" font-weight="500" fill="{TEXT_DIM}">你说需求 → 它自己干 → 不用你盯着</text>
</svg>'''
    (ROOT / "nhd-card-2-zh.svg").write_text(svg)
    CARDS.append(("nhd-card-2-zh.svg", 800))


def zh_card_3():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{CREAM}"/>
      <stop offset="100%" stop-color="{CREAM2}"/>
    </linearGradient>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <text x="400" y="340" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="56" font-weight="900" fill="{TEXT}">一行命令安装</text>
  <text x="400" y="440" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="56" font-weight="900" fill="{GREEN}">MIT 开源</text>
  <text x="400" y="560" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{BLUE}">curl -fsSL hermes-agent.nousresearch.com/install.sh | bash</text>
</svg>'''
    (ROOT / "nhd-card-3-zh.svg").write_text(svg)
    CARDS.append(("nhd-card-3-zh.svg", 800))


def en_cover():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="75%">
      <stop offset="0%" stop-color="#141B33"/>
      <stop offset="100%" stop-color="{DARK_BG}"/>
    </radialGradient>
    <linearGradient id="titleG" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{DARK_BLUE}"/>
      <stop offset="50%" stop-color="{DARK_PURPLE}"/>
      <stop offset="100%" stop-color="{DARK_PINK}"/>
    </linearGradient>
  </defs>
  <rect width="1024" height="1024" fill="url(#bg)"/>
  <circle cx="120" cy="120" r="140" fill="#1E3A5F" opacity="0.3"/>
  <circle cx="880" cy="180" r="100" fill="#3B1F6E" opacity="0.3"/>
  <text x="512" y="380" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="72" font-weight="900" fill="{DARK_TEXT}">Hermes Desktop</text>
  <text x="512" y="500" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="96" font-weight="900" fill="url(#titleG)">Beta</text>
  <text x="512" y="640" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="32" font-weight="500" fill="{DARK_DIM}">The Agent That Grows With You</text>
  <text x="512" y="950" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{DARK_BLUE}">curl -fsSL hermes-agent.nousresearch.com/install.sh | bash</text>
</svg>'''
    (ROOT / "nhd-cover-en.svg").write_text(svg)
    CARDS.append(("nhd-cover-en.svg", 1024))


def en_card_1():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="75%">
      <stop offset="0%" stop-color="#141B33"/>
      <stop offset="100%" stop-color="{DARK_BG}"/>
    </radialGradient>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <circle cx="700" cy="80" r="60" fill="#3B1F6E" opacity="0.4"/>
  <circle cx="80" cy="720" r="50" fill="#1E3A5F" opacity="0.4"/>
  <text x="400" y="340" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="56" font-weight="900" fill="{DARK_TEXT}">Jensen's</text>
  <text x="400" y="440" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="64" font-weight="900" fill="{DARK_BLUE}">GTC Debut</text>
  <text x="400" y="560" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="26" font-weight="500" fill="{DARK_DIM}">Live on stage · 20s demo · Shipped</text>
</svg>'''
    (ROOT / "nhd-card-1-en.svg").write_text(svg)
    CARDS.append(("nhd-card-1-en.svg", 800))


def en_card_2():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="75%">
      <stop offset="0%" stop-color="#141B33"/>
      <stop offset="100%" stop-color="{DARK_BG}"/>
    </radialGradient>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <circle cx="80" cy="80" r="60" fill="#1E3A5F" opacity="0.4"/>
  <circle cx="720" cy="720" r="50" fill="#3B1F6E" opacity="0.4"/>
  <text x="400" y="340" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="56" font-weight="900" fill="{DARK_TEXT}">Open Source</text>
  <text x="400" y="440" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="64" font-weight="900" fill="{DARK_GREEN}">MIT License</text>
  <text x="400" y="560" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="26" font-weight="500" fill="{DARK_DIM}">No signup · No credit card · Just run</text>
</svg>'''
    (ROOT / "nhd-card-2-en.svg").write_text(svg)
    CARDS.append(("nhd-card-2-en.svg", 800))


def en_card_3():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="75%">
      <stop offset="0%" stop-color="#141B33"/>
      <stop offset="100%" stop-color="{DARK_BG}"/>
    </radialGradient>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <circle cx="700" cy="80" r="60" fill="#1E3A5F" opacity="0.4"/>
  <circle cx="80" cy="720" r="50" fill="#3B1F6E" opacity="0.4"/>
  <text x="400" y="330" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="52" font-weight="900" fill="{DARK_TEXT}">13+ Platforms</text>
  <text x="400" y="440" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="64" font-weight="900" fill="{DARK_PINK}">One Agent</text>
  <text x="400" y="560" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="26" font-weight="500" fill="{DARK_DIM}">Telegram · Slack · Discord · Email · CLI</text>
</svg>'''
    (ROOT / "nhd-card-3-en.svg").write_text(svg)
    CARDS.append(("nhd-card-3-en.svg", 800))


def main():
    zh_cover()
    zh_card_1()
    zh_card_2()
    zh_card_3()
    en_cover()
    en_card_1()
    en_card_2()
    en_card_3()

    print(f"Generated {len(CARDS)} SVGs")
    for name, size in CARDS:
        png = name.replace(".svg", ".png")
        subprocess.run([
            "inkscape", str(ROOT / name),
            "-o", str(ROOT / png),
            "-w", str(size), "-h", str(size)
        ], check=True)
        print(f"  OK {png}")


if __name__ == "__main__":
    main()