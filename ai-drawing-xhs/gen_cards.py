#!/usr/bin/env python3
"""Generate comparison cards: Midjourney vs DALL-E vs SD vs Leonardo vs 即梦."""
import subprocess, os
ROOT = os.path.dirname(os.path.abspath(__file__))

C = "#FAF7F2"
C2 = "#F3F0E8"
W = "#FFFFFF"
T = "#1E293B"
TD = "#64748B"
TL = "#94A3B8"

MJ = "#9B59B6"
MJL = "#F3E8FF"
DE = "#10B981"
DEL = "#D1FAE5"
SD = "#3B82F6"
SDL = "#DBEAFE"
LE = "#06B6D4"
LEL = "#CFFAFE"
JM = "#F97316"
JML = "#FFEDD5"

RED = "#EF4444"
REDL = "#FEE2E2"
ORANGE = "#F97316"
GREEN = "#10B981"

def bg(w, h):
    return (f'<rect width="{w}" height="{h}" fill="url(#bgG)"/>'
            f'<circle cx="{w*0.06}" cy="{h*0.06}" r="60" fill="{MJL}" opacity="0.5"/>'
            f'<circle cx="{w*0.94}" cy="{h*0.10}" r="50" fill="{DEL}" opacity="0.4"/>'
            f'<circle cx="{w*0.06}" cy="{h*0.90}" r="70" fill="{SDL}" opacity="0.4"/>'
            f'<circle cx="{w*0.94}" cy="{h*0.85}" r="80" fill="{JML}" opacity="0.4"/>')

def svg_wrap(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
<defs><linearGradient id="bgG" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{C}"/><stop offset="100%" stop-color="{C2}"/></linearGradient></defs>
{bg(w, h)}
{body}
</svg>'''

TOOLS = [
    ("Midjourney", MJ, MJL),
    ("DALL-E 3", DE, DEL),
    ("Stable Diffusion", SD, SDL),
    ("Leonardo.ai", LE, LEL),
    ("即梦", JM, JML),
]

def card_square():
    chips = ""
    for i, (name, color, light) in enumerate(TOOLS):
        y = 300 + i * 115
        chips += f'''
<g transform="translate(62, {y})">
  <rect x="0" y="0" width="900" height="90" rx="18" fill="{W}" stroke="{color}" stroke-width="2" filter="url(#s)"/>
  <text x="450" y="55" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="36" font-weight="800" fill="{color}">{name}</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
<defs><filter id="s" x="-5%" y="-5%" width="110%" height="110%"><feDropShadow dx="0" dy="3" stdDeviation="6" flood-color="#000" flood-opacity="0.08"/></filter></defs>
<text x="512" y="130" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="56" font-weight="900" fill="{T}" letter-spacing="-2">AI 画图工具横评</text>
<text x="512" y="195" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="26" fill="{TD}">2026 主流 AI 绘画工具全对比</text>
{chips}
<text x="512" y="990" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TL}">从入门到专业，一张图看懂怎么选</text>
''')

def card_1():
    headers = ["工具", "价格", "画质", "速度", "上手难度"]
    rows = [
        ("Midjourney", "10-60$/月", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐"),
        ("DALL-E 3", "20$/月含ChatGPT", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
        ("Stable Diffusion", "免费(需GPU)", "⭐⭐⭐⭐⭐", "⭐⭐⭐", "⭐⭐"),
        ("Leonardo.ai", "免费~30$/月", "⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐"),
        ("即梦", "免费+积分", "⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
    ]
    cx = [80, 270, 455, 605, 790]
    y0 = 170
    items = ""
    for ri, row in enumerate(rows):
        y = y0 + ri * 90
        color = [MJ, DE, SD, LE, JM][ri]
        items += f'''
<g transform="translate(62, {y})">
  <rect x="0" y="0" width="900" height="75" rx="12" fill="{W}" stroke="{color}" stroke-width="2" stroke-opacity="0.4"/>
  <text x="{cx[0]}" y="46" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="800" fill="{color}">{row[0]}</text>
  <text x="{cx[1]}" y="46" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{T}">{row[1]}</text>
  <text x="{cx[2]}" y="46" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{T}">{row[2]}</text>
  <text x="{cx[3]}" y="46" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{T}">{row[3]}</text>
  <text x="{cx[4]}" y="46" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{T}">{row[4]}</text>
</g>'''
    hdr_y = y0 - 45
    return svg_wrap(1024, 1024, f'''
<text x="512" y="70" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="42" font-weight="900" fill="{T}" letter-spacing="-1">横向对比</text>
<text x="512" y="110" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">价格 · 画质 · 速度 · 上手难度 全维度对比</text>
<g transform="translate(62, {hdr_y})">
  {''.join(f'<text x="{x}" y="28" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" font-weight="800" fill="{TD}">{h}</text>' for h, x in zip(headers, cx))}
</g>
{items}
<text x="512" y="990" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="14" fill="{TL}">价格以 USD 为单位 · 速度受硬件和网络影响 · 2026/06</text>
''')

def card_2():
    descs = [
        (MJ, MJL, "Midjourney", "艺术质感天花板，人像/概念设计最强", "光影氛围无敌 · 风格统一性好 · 社区生态丰富"),
        (DE, DEL, "DALL-E 3", "提示词理解最准，文字渲染最强", "和 ChatGPT 深度集成 · 英文文字正确率高 · 上手零门槛"),
        (SD, SDL, "Stable Diffusion", "完全开源，可本地部署，可定制", "ControlNet/LoRA 生态 · 模型自由度高 · 需要一定技术"),
        (LE, LEL, "Leonardo.ai", "游戏资产生成利器，Web 端好用", "画风一致性高 · 内置多种模型 · 免费额度充足"),
        (JM, JML, "即梦", "中文理解最好，免费，不需要魔法", "提示词支持中文 · 人像/国风出色 · 小红书爆款利器"),
    ]
    items = ""
    for i, (color, light, name, tagline, detail) in enumerate(descs):
        y = 140 + i * 160
        items += f'''
<g transform="translate(62, {y})">
  <rect x="0" y="0" width="900" height="140" rx="14" fill="{W}" stroke="{color}" stroke-width="1.5"/>
  <rect x="0" y="0" width="8" height="140" rx="4" fill="{color}"/>
  <text x="30" y="38" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{color}">{name}</text>
  <text x="30" y="72" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" font-weight="600" fill="{T}">{tagline}</text>
  <text x="30" y="106" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" fill="{TD}">{detail}</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
<text x="512" y="70" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="34" font-weight="800" fill="{T}">各工具核心优势</text>
{items}
''')

def card_3():
    scores = [
        (MJ, MJL, "Midjourney", "专业设计师首选", "画质顶尖但最贵，适合商业出图"),
        (DE, DEL, "DALL-E 3", "新手友好全能王", "ChatGPT 用户无脑入，日常够用"),
        (SD, SDL, "Stable Diffusion", "技术玩家进阶之选", "免费但需折腾，上限极高"),
        (LE, LEL, "Leonardo.ai", "游戏/素材生产力", "Web 端体验好，免费额度够用"),
        (JM, JML, "即梦", "国内用户首选", "免费中文友好，小红书出图神器"),
    ]
    items = ""
    for i, (color, light, name, role, note) in enumerate(scores):
        y = 145 + i * 155
        stars = "⭐" * (5 - i)
        items += f'''
<g transform="translate(62, {y})">
  <rect x="0" y="0" width="900" height="135" rx="14" fill="{W}" stroke="{color}" stroke-width="1" stroke-opacity="0.3"/>
  <rect x="0" y="0" width="4" height="135" rx="2" fill="{color}"/>
  <text x="24" y="46" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="30" font-weight="800" fill="{color}">#{i+1} {name}</text>
  <text x="24" y="82" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{T}">{role}</text>
  <text x="24" y="114" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" fill="{TD}">{note}</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
<text x="512" y="70" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="34" font-weight="800" fill="{T}">综合推荐排名</text>
{items}
<text x="512" y="990" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="14" fill="{TL}">排名仅供参考，实际选择取决于使用场景和预算</text>
''')

def card_banner():
    w_c = 320
    gap = 36
    x0 = int((1792 - (w_c * 5 + gap * 4)) / 2)
    cards_html = ""
    for i, (name, color, light, abbrev, tag, price, desc) in enumerate([
        (MJ, MJL, "Midjourney", "MJ", "画质天花板", "10-60$/月", "专业级出图"),
        (DE, DEL, "DALL-E 3", "DE3", "新手友好", "20$/月", "提示词理解最强"),
        (SD, SDL, "Stable Diffusion", "SD", "开源生态", "免费(需GPU)", "可定制性最高"),
        (LE, LEL, "Leonardo.ai", "Leo", "游戏素材", "0-30$/月", "Web端好用"),
        (JM, JML, "即梦", "即梦", "中文首选", "免费+积分", "小红书画图神器"),
    ]):
        x = x0 + i * (w_c + gap)
        cards_html += f'''
<g transform="translate({x}, 350)">
  <rect x="0" y="0" width="{w_c}" height="250" rx="18" fill="{W}" stroke="{color}" stroke-width="3"/>
  <text x="{w_c//2}" y="60" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="36" font-weight="900" fill="{color}">{abbrev}</text>
  <text x="{w_c//2}" y="110" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="26" font-weight="700" fill="{T}">{tag}</text>
  <text x="{w_c//2}" y="155" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">{price}</text>
  <text x="{w_c//2}" y="200" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">{desc}</text>
</g>'''
    return svg_wrap(1792, 1024, f'''
<text x="896" y="180" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="90" font-weight="900" fill="{T}" letter-spacing="-3">AI 画图工具横评</text>
<text x="896" y="260" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="30" fill="{TD}">Midjourney · DALL-E 3 · Stable Diffusion · Leonardo · 即梦</text>
{cards_html}
<text x="896" y="700" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="26" fill="{T}" font-weight="700">没有最好的工具，只有最适合你的工具</text>
<g transform="translate(296, 760)">
  <rect x="0" y="0" width="1200" height="80" rx="40" fill="{MJL}" stroke="{MJ}" stroke-width="2" stroke-opacity="0.6"/>
  <text x="600" y="50" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="30" font-weight="800" fill="{MJ}">预算够 → MJ  ·  新手 → DALL-E  ·  懂技术 → SD  ·  国内 → 即梦</text>
</g>
<text x="896" y="970" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TL}">2026/06 · 建议都试用一遍再决定</text>
''')

if __name__ == "__main__":
    cards = [
        ("ai-drawing-square", card_square()),
        ("ai-drawing-card-1", card_1()),
        ("ai-drawing-card-2", card_2()),
        ("ai-drawing-card-3", card_3()),
        ("ai-drawing-banner", card_banner()),
    ]
    for name, svg in cards:
        svg_path = os.path.join(ROOT, f"{name}.svg")
        png_path = os.path.join(ROOT, f"{name}.png")
        with open(svg_path, "w") as f:
            f.write(svg)
        subprocess.run(["inkscape", svg_path, "-o", png_path, "-w", str(1792 if "banner" in name else 1024), "-h", "1024"], check=True, capture_output=True)
        print(f"  ✓ {name}.png ({os.path.getsize(png_path)//1024} KB)")
    print("Done! 5 cards regenerated.")
