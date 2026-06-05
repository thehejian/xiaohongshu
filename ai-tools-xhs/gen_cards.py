#!/usr/bin/env python3
w, h = 1024, 1024
brand = "#E85D04"
dark_text = "#1E293B"
bg_dark = "#0B1027"

light_cards = [
    {"items": ["Leonardo.ai — 每日150积分", "Playground AI — 每天500张", "SeaArt AI — 国产免费"]},
    {"items": ["ElevenLabs — 免费10分钟克隆", "Murf AI — 商用配音首选", "Coqui — 开源完全免费"]},
    {"items": ["Runway — 免费85秒生成", "Pika Labs — 免费无限生成", "CapCut — 免费AI视频"]},
    {"items": ["Gamma — AI一键PPT", "ChatGPT/Claude — 免费3.5", "Cursor — 免费AI编程"]},
]

dark_cards = [
    {"items": ["Leonardo.ai — 150 credits", "Playground AI — 500/day", "SeaArt AI — Free"]},
    {"items": ["ElevenLabs — 10 min clone", "Murf AI — Commercial use", "Coqui — Open source"]},
    {"items": ["Runway — 85 sec free", "Pika Labs — Unlimited", "CapCut — Free AI video"]},
    {"items": ["Gamma — AI PPT", "ChatGPT/Claude — Free", "Cursor — AI coding"]},
]

def make_light_card(items, page, total):
    ys = [250, 420, 590]
    html = ""
    for i, item in enumerate(items):
        html += f'''<text x="{w//2}" y="{ys[i]}" font-family="Noto Sans SC, PingFang SC, Microsoft YaHei, sans-serif" font-size="36" font-weight="bold" fill="{dark_text}" text-anchor="middle">{item}</text>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs><linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" style="stop-color:#FAF7F2"/><stop offset="100%" style="stop-color:#F5F0E8"/></linearGradient></defs>
<rect width="{w}" height="{h}" fill="url(#bg)"/>
<rect x="40" y="30" width="944" height="100" rx="20" fill="{brand}"/>
<text x="512" y="85" font-family="Noto Sans SC, PingFang SC, Microsoft YaHei, sans-serif" font-size="36" font-weight="bold" fill="#FFFFFF" text-anchor="middle">30个免费AI神器</text>
<text x="512" y="115" font-family="Noto Sans SC, PingFang SC, Microsoft YaHei, sans-serif" font-size="18" fill="#FFFFFF" text-anchor="middle">Page {page}/{total}</text>
<text x="512" y="170" font-family="Noto Sans SC, PingFang SC, Microsoft YaHei, sans-serif" font-size="28" font-weight="bold" fill="{dark_text}" text-anchor="middle">— 免费 · 无需付费 —</text>
{html}</svg>'''

def make_dark_card(items, page, total):
    ys = [250, 420, 590]
    html = ""
    for i, item in enumerate(items):
        html += f'''<text x="{w//2}" y="{ys[i]}" font-family="Arial, sans-serif" font-size="32" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{item}</text>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<rect width="{w}" height="{h}" fill="{bg_dark}"/>
<rect x="40" y="30" width="944" height="100" rx="20" fill="{brand}"/>
<text x="512" y="85" font-family="Arial, sans-serif" font-size="32" font-weight="bold" fill="#FFFFFF" text-anchor="middle">30 FREE AI TOOLS</text>
<text x="512" y="115" font-family="Arial, sans-serif" font-size="18" fill="#FFFFFF" text-anchor="middle">Page {page}/{total}</text>
<text x="512" y="170" font-family="Arial, sans-serif" font-size="26" fill="#FFD700" text-anchor="middle">— Free & Open —</text>
{html}</svg>'''

for i, card in enumerate(light_cards, 1):
    open(f"ai-tools-xhs/card-light-{i}.svg","w",encoding="utf-8").write(make_light_card(card["items"], i, 4))
    print(f"light {i}")

for i, card in enumerate(dark_cards, 1):
    open(f"ai-tools-xhs/card-dark-{i}.svg","w",encoding="utf-8").write(make_dark_card(card["items"], i, 4))
    print(f"dark {i}")

print("Done")