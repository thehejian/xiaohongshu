#!/usr/bin/env python3
"""Generate Zidane-Algeria social cards: 1x cover (1024x1024) + 3x content (800x800)."""
import subprocess, os
ROOT = os.path.dirname(os.path.abspath(__file__))

C = "#FAF7F2"
C2 = "#F5F0E8"
W = "#FFFFFF"
T = "#1E293B"
TD = "#64748B"
TL = "#94A3B8"

GREEN = "#006233"
GREENL = "#D1FAE5"
GREENM = "#059669"
RED = "#D32F2F"
REDL = "#FEE2E2"
WHITE = "#FFFFFF"
GOLD = "#D4A843"
GOLDL = "#FEF3C7"

def bg(w, h):
    return f'<rect width="{w}" height="{h}" fill="url(#bgG)"/><circle cx="{w*0.08}" cy="{h*0.08}" r="60" fill="{GREENL}" opacity="0.3"/><circle cx="{w*0.92}" cy="{h*0.12}" r="50" fill="{GOLDL}" opacity="0.3"/><circle cx="{w*0.08}" cy="{h*0.88}" r="70" fill="{REDL}" opacity="0.2"/><circle cx="{w*0.92}" cy="{h*0.78}" r="80" fill="{GREENL}" opacity="0.2"/>'

def svg_wrap(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
<defs><linearGradient id="bgG" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{C}"/><stop offset="100%" stop-color="{C2}"/></linearGradient></defs>
{bg(w, h)}
{body}
</svg>'''

def card_cover():
    return svg_wrap(1024, 1024, f'''
<rect x="0" y="0" width="1024" height="200" fill="{GREEN}"/>
<rect x="0" y="200" width="1024" height="12" fill="{RED}"/>

<text x="512" y="125" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="80" font-weight="900" fill="{WHITE}" letter-spacing="8">ZIDANE</text>
<text x="512" y="165" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" fill="{WHITE}" opacity="0.85">ALGERIA · 2026 WORLD CUP</text>

<text x="512" y="310" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="60" font-weight="900" fill="{T}">齐达内之子</text>
<text x="512" y="380" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="56" font-weight="700" fill="{GREEN}">卢卡·齐达内</text>
<text x="512" y="430" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" fill="{TD}">Luca Zinedine Zidane</text>

<g transform="translate(262, 490)">
  <rect x="0" y="0" width="500" height="90" rx="16" fill="{W}" stroke="{GREEN}" stroke-width="2"/>
  <text x="250" y="38" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" font-weight="700" fill="{GREEN}">门将 · 28岁 · 183cm</text>
  <text x="250" y="72" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">🇩🇿 阿尔及利亚国家队 · 格拉纳达</text>
</g>

<g transform="translate(112, 620)">
  <rect x="0" y="0" width="260" height="70" rx="35" fill="{GREENL}"/>
  <text x="130" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{GREENM}">皇马青训出身</text>
  <text x="130" y="55" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{GREENM}">15年西班牙历练</text>
</g>
<g transform="translate(400, 620)">
  <rect x="0" y="0" width="240" height="70" rx="35" fill="{GOLDL}"/>
  <text x="120" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{GOLD}">2025年转籍</text>
  <text x="120" y="55" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{GOLD}">代表父亲祖国</text>
</g>
<g transform="translate(668, 620)">
  <rect x="0" y="0" width="240" height="70" rx="35" fill="{REDL}"/>
  <text x="120" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{RED}">非洲杯3场零封</text>
  <text x="120" y="55" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{RED}">一战成名</text>
</g>

<text x="512" y="790" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" font-weight="700" fill="{T}">时隔20年，Zidane重返世界杯</text>
<text x="512" y="840" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">姓氏相同，球衣不同</text>

<text x="512" y="970" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TL}">齐达内之子 · 阿尔及利亚门将 · 世界杯2026</text>
''')

def card_1():
    return svg_wrap(800, 800, f'''
<text x="400" y="65" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="34" font-weight="800" fill="{T}">从皇马青训到国门</text>
<text x="400" y="105" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">Luca Zidane 足球生涯时间线</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="720" height="130" rx="16" fill="{W}" stroke="{GREEN}" stroke-width="1.5"/>
  <text x="30" y="40" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{GREEN}">2004 - 2018</text>
  <text x="30" y="72" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{T}">皇马青训营</text>
  <text x="30" y="100" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TD}">6岁加入，从卡斯蒂利亚到一线队</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="720" height="130" rx="16" fill="{W}" stroke="{GOLD}" stroke-width="1.5"/>
  <text x="30" y="40" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{GOLD}">2019 - 2024</text>
  <text x="30" y="72" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{T}">西班牙二级联赛历练</text>
  <text x="30" y="100" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TD}">桑坦德 · 巴列卡诺 · 埃瓦尔 · 格拉纳达</text>
</g>

<g transform="translate(40, 450)">
  <rect x="0" y="0" width="720" height="130" rx="16" fill="{W}" stroke="{RED}" stroke-width="1.5"/>
  <text x="30" y="40" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{RED}">2025.9</text>
  <text x="30" y="72" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{T}">转籍阿尔及利亚</text>
  <text x="30" y="100" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TD}">FIFA批准 · 首次入选国家队集训名单</text>
</g>

<g transform="translate(40, 600)">
  <rect x="0" y="0" width="720" height="130" rx="16" fill="{W}" stroke="{GREEN}" stroke-width="1.5"/>
  <text x="30" y="40" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{GREEN}">2026.5.31</text>
  <text x="30" y="72" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{T}">入选世界杯大名单</text>
  <text x="30" y="100" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TD}">时隔12年，阿尔及利亚重返世界杯</text>
</g>
''')

def card_2():
    return svg_wrap(800, 800, f'''
<text x="400" y="65" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="34" font-weight="800" fill="{T}">父与子</text>
<text x="400" y="105" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">Zinedine vs Luca · 传奇与传承</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="340" height="280" rx="18" fill="{W}" stroke="{GREEN}" stroke-width="2"/>
  <text x="170" y="45" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" font-weight="900" fill="{GREEN}">齐达内</text>
  <line x1="30" y1="65" x2="310" y2="65" stroke="{GREENL}" stroke-width="2"/>
  <text x="170" y="100" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" font-weight="600" fill="{T}">法国传奇中场</text>
  <text x="170" y="135" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TD}">1998世界杯冠军</text>
  <text x="170" y="165" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TD}">2000欧洲杯冠军</text>
  <text x="170" y="195" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TD}">2002欧冠天外飞仙</text>
  <text x="170" y="225" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TD}">皇马主帅三连欧冠</text>
  <text x="170" y="260" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="14" fill="{TL}">🇫🇷 法国 · 中场 · 10号</text>
</g>

<g transform="translate(420, 150)">
  <rect x="0" y="0" width="340" height="280" rx="18" fill="{W}" stroke="{GOLD}" stroke-width="2"/>
  <text x="170" y="45" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" font-weight="900" fill="{GOLD}">卢卡</text>
  <line x1="30" y1="65" x2="310" y2="65" stroke="{GOLDL}" stroke-width="2"/>
  <text x="170" y="100" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" font-weight="600" fill="{T}">阿尔及利亚门将</text>
  <text x="170" y="135" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TD}">2025转籍阿尔及利亚</text>
  <text x="170" y="165" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TD}">2026非洲杯3零封</text>
  <text x="170" y="195" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TD}">2026世界杯大名单</text>
  <text x="170" y="225" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TD}">格拉纳达俱乐部</text>
  <text x="170" y="260" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="14" fill="{TL}">🇩🇿 阿尔及利亚 · 门将 · 23号</text>
</g>

<text x="400" y="500" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{T}">"他的旅程是他的，我有我的旅程"</text>
<text x="400" y="540" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">—— Luca Zidane</text>

<g transform="translate(100, 590)">
  <rect x="0" y="0" width="600" height="70" rx="35" fill="{GREENL}"/>
  <text x="300" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="700" fill="{GREENM}">同一个姓氏，不同的传奇之路</text>
  <text x="300" y="56" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="15" fill="{GREENM}">法国10号 → 阿尔及利亚23号</text>
</g>

<text x="400" y="740" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TL}">传承 · 选择 · 走自己的路</text>
''')

def card_3():
    return svg_wrap(800, 800, f'''
<text x="400" y="65" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="34" font-weight="800" fill="{T}">世界杯2026 · J组</text>
<text x="400" y="105" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">阿尔及利亚时隔12年重返世界杯</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="720" height="60" rx="12" fill="{GREEN}"/>
  <text x="100" y="38" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{WHITE}">🇩🇿 阿尔及利亚</text>
  <text x="260" y="38" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" fill="{WHITE}">FIFA排名</text>
  <text x="400" y="38" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="700" fill="{WHITE}">—</text>
  <text x="550" y="38" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" fill="{WHITE}">非洲杯八强</text>
</g>

<g transform="translate(40, 230)">
  <rect x="0" y="0" width="720" height="50" rx="12" fill="{REDL}"/>
  <text x="80" y="33" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{RED}">🇦🇷 阿根廷</text>
  <text x="250" y="33" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">卫冕冠军 · 梅西领衔</text>
</g>

<g transform="translate(40, 290)">
  <rect x="0" y="0" width="720" height="50" rx="12" fill="{GOLDL}"/>
  <text x="80" y="33" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{GOLD}">🇯🇴 约旦</text>
  <text x="250" y="33" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">亚洲黑马</text>
</g>

<g transform="translate(40, 350)">
  <rect x="0" y="0" width="720" height="50" rx="12" fill="{GREENL}"/>
  <text x="80" y="33" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{GREENM}">🇦🇹 奥地利</text>
  <text x="250" y="33" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">欧洲劲旅</text>
</g>

<text x="400" y="470" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{T}">齐达内这个名字回来了</text>

<g transform="translate(40, 510)">
  <rect x="0" y="0" width="720" height="130" rx="16" fill="{W}" stroke="{GREEN}" stroke-width="2"/>
  <text x="360" y="38" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="700" fill="{GREEN}">时隔20年 Zidane 重返世界杯</text>
  <line x1="40" y1="55" x2="680" y2="55" stroke="{GREENL}" stroke-width="1.5"/>
  <text x="40" y="85" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" fill="{T}">2006年 齐达内头顶马特拉齐</text>
  <text x="40" y="112" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" fill="{T}">2026年 卢卡·齐达内镇守龙门</text>
</g>

<text x="400" y="720" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{T}">一个传奇谢幕，另一个传奇开始</text>

<text x="400" y="770" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TL}">阿尔及利亚世界杯2026 · J组</text>
''')

CARDS = [
    ("01-cover", 1024, 1024, card_cover()),
    ("02-journey", 800, 800, card_1()),
    ("03-father-son", 800, 800, card_2()),
    ("04-worldcup", 800, 800, card_3()),
]

def main():
    for name, w, h, svg in CARDS:
        svg_path = os.path.join(ROOT, f"{name}.svg")
        png_path = os.path.join(ROOT, f"{name}.png")
        with open(svg_path, "w") as f:
            f.write(svg)
        subprocess.run([
            "inkscape", svg_path,
            "--export-filename=" + png_path,
            f"--export-width={w}",
            f"--export-height={h}",
        ], check=True)
        print(f"Generated {png_path}")

if __name__ == "__main__":
    main()
