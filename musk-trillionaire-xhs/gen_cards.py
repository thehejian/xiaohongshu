#!/usr/bin/env python3
"""Generate Musk trillionaire social cards (1024x1024 cover + 3x 800x800 content cards)."""
import subprocess, os
ROOT = os.path.dirname(os.path.abspath(__file__))

C = "#FAF7F2"
W = "#FFFFFF"
C2 = "#F5F0E8"
T = "#1E293B"
TD = "#64748B"
TL = "#94A3B8"
TEAL = "#0EA5E9"
TEALL = "#E0F2FE"
BLUE = "#3B82F6"
BLUEL = "#DBEAFE"
PURPLE = "#8B5CF6"
PURPLEL = "#EDE9FE"
ORANGE = "#F97316"
ORANGEL = "#FFEDD5"
GREEN = "#10B981"
GREENL = "#D1FAE5"
RED = "#EF4444"
REDL = "#FEE2E2"
GOLD = "#F59E0B"
GOLDL = "#FEF3C7"

def bg(w, h):
    return f'<rect width="{w}" height="{h}" fill="url(#bgG)"/><circle cx="{w*0.08}" cy="{h*0.08}" r="60" fill="{TEALL}" opacity="0.4"/><circle cx="{w*0.92}" cy="{h*0.12}" r="50" fill="{PURPLEL}" opacity="0.4"/><circle cx="{w*0.08}" cy="{h*0.88}" r="70" fill="{BLUEL}" opacity="0.3"/><circle cx="{w*0.92}" cy="{h*0.78}" r="80" fill="{ORANGEL}" opacity="0.3"/>'

def svg_wrap(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
<defs><linearGradient id="bgG" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{C}"/><stop offset="100%" stop-color="{C2}"/></linearGradient></defs>
{bg(w, h)}
{body}
</svg>'''

def card_cover():
    return svg_wrap(1024, 1024, f'''
<text x="512" y="180" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="120" font-weight="900" fill="{T}" letter-spacing="-3">1.1</text>
<text x="512" y="310" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="100" font-weight="900" fill="{GOLD}" letter-spacing="-2">万亿</text>
<text x="512" y="400" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" fill="{TD}">美元 · 人类首位万亿富豪</text>

<g transform="translate(162, 470)">
  <rect x="0" y="0" width="700" height="80" rx="40" fill="{REDL}" stroke="{RED}" stroke-width="2"/>
  <text x="350" y="50" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="32" font-weight="800" fill="{RED}">月薪2万要赚 3325万年</text>
</g>

<text x="512" y="630" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="26" font-weight="700" fill="{T}">从恐龙时代打工到现在</text>
<text x="512" y="670" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">不吃不喝不扣税 · 才能攒够</text>

<g transform="translate(120, 750)">
  <rect x="0" y="0" width="220" height="44" rx="22" fill="{TEALL}"/><text x="110" y="29" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="600" fill="{TEAL}">7.98万亿人民币</text>
  <rect x="240" y="0" width="220" height="44" rx="22" fill="{ORANGEL}"/><text x="350" y="29" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="600" fill="{ORANGE}">每天花2.18亿</text>
  <rect x="480" y="0" width="220" height="44" rx="22" fill="{PURPLEL}"/><text x="590" y="29" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="600" fill="{PURPLE}">SpaceX上市</text>
  <rect x="720" y="0" width="180" height="44" rx="22" fill="{GREENL}"/><text x="810" y="29" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="600" fill="{GREEN}">股票代码SPCX</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28">🤯</text>
''')

def card_1():
    return svg_wrap(800, 800, f'''
<text x="400" y="80" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="34" font-weight="800" fill="{T}">数字对比 · 万亿有多离谱</text>

<g transform="translate(40, 130)">
  <rect x="0" y="0" width="720" height="160" rx="18" fill="{W}" stroke="{TEAL}" stroke-width="2"/>
  <text x="360" y="40" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="26" font-weight="700" fill="{TEAL}">打工人 vs 马斯克</text>
  <line x1="60" y1="60" x2="660" y2="60" stroke="{TEALL}" stroke-width="2"/>
  <text x="40" y="100" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="600" fill="{T}">月薪2万</text>
  <text x="40" y="135" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="600" fill="{T}">年薪24万</text>
  <text x="500" y="100" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">×</text>
  <text x="520" y="135" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" font-weight="900" fill="{RED}">3325万年</text>
</g>

<g transform="translate(40, 320)">
  <rect x="0" y="0" width="720" height="140" rx="18" fill="{W}" stroke="{GOLD}" stroke-width="2"/>
  <text x="360" y="38" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{GOLD}">横向对比</text>
  <line x1="60" y1="50" x2="660" y2="50" stroke="{GOLDL}" stroke-width="2"/>
  <text x="40" y="85" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">北京猿人</text>
  <text x="200" y="85" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{T}">约50万年前</text>
  <circle cx="180" cy="78" r="4" fill="{GOLD}"/>
  <text x="40" y="120" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">恐龙灭绝</text>
  <text x="200" y="120" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{T}">约6600万年前</text>
  <circle cx="180" cy="113" r="4" fill="{GOLD}"/>
</g>

<text x="400" y="540" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{T}">你需要从恐龙灭绝后的</text>
<text x="400" y="580" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="36" font-weight="900" fill="{RED}">第3000万年开始打工</text>
<text x="400" y="630" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">不吃不喝加班到现在</text>

<text x="400" y="720" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TL}">一图看懂万亿有多夸张</text>
''')

def card_2():
    return svg_wrap(800, 800, f'''
<text x="400" y="80" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="34" font-weight="800" fill="{T}">荒诞花钱指南</text>
<text x="400" y="120" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" fill="{TD}">限定100年花完 · 每天2.18亿</text>

<g transform="translate(40, 170)">
  <rect x="0" y="0" width="720" height="100" rx="16" fill="{W}" stroke="{BLUE}" stroke-width="1.5"/>
  <text x="30" y="38" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{BLUE}">终极买房 🏠</text>
  <text x="30" y="75" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">每天买2套1亿豪宅 · 连买100年</text>
  <text x="660" y="38" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{BLUE}">×2</text>
</g>

<g transform="translate(40, 290)">
  <rect x="0" y="0" width="720" height="100" rx="16" fill="{W}" stroke="{PURPLE}" stroke-width="1.5"/>
  <text x="30" y="38" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{PURPLE}">全员红包 🧧</text>
  <text x="30" y="75" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">给全中国14亿人每人发5700块</text>
  <text x="660" y="38" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{PURPLE}">14亿</text>
</g>

<g transform="translate(40, 410)">
  <rect x="0" y="0" width="720" height="100" rx="16" fill="{W}" stroke="{ORANGE}" stroke-width="1.5"/>
  <text x="30" y="38" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{ORANGE}">疯狂购物 🛒</text>
  <text x="30" y="75" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">每秒必须花2500元 · 呼吸停顿就失败</text>
  <text x="660" y="38" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{ORANGE}">⚡</text>
</g>

<g transform="translate(40, 530)">
  <rect x="0" y="0" width="720" height="100" rx="16" fill="{W}" stroke="{GREEN}" stroke-width="1.5"/>
  <text x="30" y="38" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{GREEN}">超级尾款人 💳</text>
  <text x="30" y="75" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">24小时不停地刷卡 · 每秒刷25次</text>
  <text x="660" y="38" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{GREEN}">💸</text>
</g>

<text x="400" y="720" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TL}">富豪的快乐 我们根本想象不到</text>
''')

def card_3():
    return svg_wrap(800, 800, f'''
<text x="400" y="100" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="40" font-weight="900" fill="{T}">🤔 灵魂拷问</text>

<text x="400" y="220" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="26" font-weight="700" fill="{T}">给你 2.18亿 单日额度</text>
<text x="400" y="270" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="26" font-weight="700" fill="{T}">第一天你怎么花？</text>

<g transform="translate(80, 340)">
  <rect x="0" y="0" width="640" height="60" rx="30" fill="{TEALL}"/>
  <text x="320" y="38" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{TEAL}">评论区写出你的方案</text>
</g>

<g transform="translate(80, 440)">
  <rect x="0" y="0" width="640" height="60" rx="30" fill="{ORANGEL}"/>
  <text x="320" y="38" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{ORANGE}">点赞最高的送虚拟豪宅🏠</text>
</g>

<g transform="translate(80, 540)">
  <rect x="0" y="0" width="640" height="60" rx="30" fill="{PURPLEL}"/>
  <text x="320" y="38" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{PURPLE}">转发到闺蜜群一起做梦</text>
</g>

<text x="400" y="700" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="36">💰💭✨</text>

<text x="400" y="770" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TL}">收藏 = 今晚就暴富 ✓</text>
''')

if __name__ == "__main__":
    cards = [
        ("cover", card_cover()),
        ("card-1", card_1()),
        ("card-2", card_2()),
        ("card-3", card_3()),
    ]
    for name, svg in cards:
        svg_path = os.path.join(ROOT, f"{name}.svg")
        png_path = os.path.join(ROOT, f"{name}.png")
        with open(svg_path, "w") as f:
            f.write(svg)
        w = 1024 if name == "cover" else 800
        h = 1024 if name == "cover" else 800
        subprocess.run(["inkscape", svg_path, "-o", png_path, "-w", str(w), "-h", str(h)], check=True, capture_output=True)
        print(f"  ✓ {name}.png ({os.path.getsize(png_path)//1024} KB)")
    print("Done! 4 cards regenerated.")