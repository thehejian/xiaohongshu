#!/usr/bin/env python3
"""Light-style cards for Zhihu AI Hot 5 post (1024x1024 + 1792x1024 banner)."""
import subprocess, os
ROOT = os.path.dirname(os.path.abspath(__file__))

C  = "#FAF7F2"
C2 = "#F3F0E8"
W  = "#FFFFFF"
T  = "#1E293B"
TD = "#64748B"
TL = "#94A3B8"

NVIDIA     = "#76B900"
NVIDIAS    = "#E8F5D8"
UNITREE    = "#FF6B35"
UNITREES   = "#FFE8DC"
ANTHROPIC  = "#CC4C00"
ANTHROPICS = "#FFE4CC"
DEEPSEEK   = "#4F6EF7"
DEEPSEEKS  = "#DEE3FF"
BYTEDANCE  = "#FF6B6B"
BYTEDANCES = "#FFE0E0"
ZHIHU      = "#0066FF"
GOLD       = "#D4A017"

FONT = 'font-family="ui-sans-serif,-apple-system,sans-serif"'

def bg(w, h):
    c1 = f'<circle cx="{w*0.08}" cy="{h*0.08}" r="{min(w,h)*0.06}" fill="#E0F2FE" opacity="0.4"/>'
    c2 = f'<circle cx="{w*0.92}" cy="{h*0.12}" r="{min(w,h)*0.05}" fill="#EDE9FE" opacity="0.4"/>'
    c3 = f'<circle cx="{w*0.08}" cy="{h*0.88}" r="{min(w,h)*0.07}" fill="#FFEDD5" opacity="0.3"/>'
    c4 = f'<circle cx="{w*0.92}" cy="{h*0.78}" r="{min(w,h)*0.08}" fill="#D1FAE5" opacity="0.3"/>'
    return c1 + c2 + c3 + c4

def svg_wrap(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
<defs><linearGradient id="bgG" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{C}"/><stop offset="100%" stop-color="{C2}"/></linearGradient></defs>
<rect width="{w}" height="{h}" fill="url(#bgG)"/>
{bg(w, h)}
{body}
</svg>'''

SHADOW = '''<filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
  <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#00000010"/>
</filter>'''

SHADOW2 = '''<filter id="shadow2" x="-5%" y="-5%" width="110%" height="110%">
  <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#00000008"/>
</filter>'''

def logo_svg(name):
    logos = {
        "nvidia":     f'<rect x="0" y="0" width="52" height="52" rx="12" fill="{NVIDIA}"/><text x="26" y="34" text-anchor="middle" {FONT} font-size="22" font-weight="900" fill="#FFF">N</text>',
        "unitree":    f'<rect x="0" y="0" width="52" height="52" rx="12" fill="{UNITREE}"/><text x="26" y="35" text-anchor="middle" {FONT} font-size="14" font-weight="900" fill="#FFF">宇树</text>',
        "anthropic":  f'<rect x="0" y="0" width="52" height="52" rx="12" fill="{ANTHROPIC}"/><text x="26" y="34" text-anchor="middle" {FONT} font-size="26" font-weight="900" fill="#FFF">A</text>',
        "deepseek":   f'<rect x="0" y="0" width="52" height="52" rx="12" fill="{DEEPSEEK}"/><text x="26" y="35" text-anchor="middle" {FONT} font-size="15" font-weight="900" fill="#FFF">DS</text>',
        "bytedance":  f'<rect x="0" y="0" width="52" height="52" rx="12" fill="{BYTEDANCE}"/><text x="26" y="34" text-anchor="middle" {FONT} font-size="20" font-weight="900" fill="#FFF">B</text>',
        "zhihu":      f'<rect x="0" y="0" width="52" height="52" rx="12" fill="{ZHIHU}"/><text x="26" y="34" text-anchor="middle" {FONT} font-size="20" font-weight="900" fill="#FFF">知</text>',
    }
    return logos.get(name, "")

def fmt_desc(text):
    lines = text.split("\\n")
    els = ""
    for i, line in enumerate(lines):
        els += f'<tspan x="40" dy="{28 if i > 0 else 0}">{line}</tspan>'
    return els

def topic_card(rank, emoji, title, desc, tag, heat, color, light_color, logokey):
    desc_ts = fmt_desc(desc)
    return f'''
<rect x="62" y="100" width="900" height="740" rx="28" fill="{W}" filter="url(#shadow)"/>
<rect x="62" y="100" width="900" height="110" rx="28" fill="{color}"/>
<rect x="62" y="180" width="900" height="30" rx="0" fill="{color}"/>
<g transform="translate(100, 120)">{logo_svg(logokey)}</g>
<text x="512" y="168" text-anchor="middle" {FONT} font-size="38" font-weight="800" fill="#FFF">{emoji} {rank}</text>
<g transform="translate(100, 260)">
  <rect x="0" y="0" width="824" height="240" rx="16" fill="{light_color}"/>
  <text x="40" y="45" {FONT} font-size="30" font-weight="700" fill="{T}">{title}</text>
  <text x="40" y="90" {FONT} font-size="20" fill="{TD}">{desc_ts}</text>
  <text x="40" y="195" {FONT} font-size="19" fill="{color}" font-weight="600">🔥 {heat}</text>
</g>
<g transform="translate(100, 560)">
  <rect x="0" y="0" width="824" height="80" rx="16" fill="{C}" stroke="#E2E8F0" stroke-width="1"/>
  <text x="412" y="35" text-anchor="middle" {FONT} font-size="20" font-weight="600" fill="{TD}">来自知乎热榜 · 2026年6月3日</text>
  <text x="412" y="63" text-anchor="middle" {FONT} font-size="17" fill="{TL}">数据来源：知乎 & opencli</text>
</g>
<g transform="translate(100, 680)">
  <rect x="0" y="0" width="180" height="40" rx="20" fill="{light_color}" stroke="{color}" stroke-width="1.5"/>
  <text x="90" y="27" text-anchor="middle" {FONT} font-size="17" font-weight="700" fill="{color}">🏷️ {tag}</text>
</g>
'''

def cover():
    items = [
        ("🥇", "NVIDIA RTX Spark",     "124万热度", NVIDIA),
        ("🥈", "宇树科技IPO过会",      "75万热度", UNITREE),
        ("🥉", "Anthropic抢跑IPO",     "AI圈热议", ANTHROPIC),
        ("🏅", "DeepSeek-V4降价97.5%", "大模型价格战", DEEPSEEK),
        ("🏅", "字节AI大地震",         "豆包付费/大将离职", BYTEDANCE),
    ]
    rows = ""
    for i, (emoji, name, heat, color) in enumerate(items):
        y = 360 + i * 72
        rows += f'''
<g transform="translate(120, {y})">
  <rect x="0" y="0" width="784" height="56" rx="14" fill="{W}" filter="url(#shadow2)"/>
  <text x="35" y="37" {FONT} font-size="24">{emoji}</text>
  <text x="120" y="37" {FONT} font-size="20" font-weight="600" fill="{T}">{name}</text>
  <text x="680" y="37" text-anchor="end" {FONT} font-size="16" fill="{color}" font-weight="600">{heat}</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
{SHADOW}
{SHADOW2}
<rect x="62" y="80" width="900" height="864" rx="28" fill="{W}" filter="url(#shadow)"/>
<g transform="translate(475, 110)">{logo_svg("zhihu")}</g>
<text x="512" y="200" text-anchor="middle" {FONT} font-size="64" font-weight="900" fill="{T}">知乎AI热榜</text>
<text x="512" y="260" text-anchor="middle" {FONT} font-size="30" fill="{TD}">今日热门 TOP 5 🔥</text>
<text x="512" y="300" text-anchor="middle" {FONT} font-size="20" fill="{TL}">2026.06.03</text>
{rows}
<text x="512" y="870" text-anchor="middle" {FONT} font-size="16" fill="{TL}">数据 via opencli zhihu + tophub.today</text>
''')

def card(rank, emoji, title, desc, tag, heat, color, light, lk):
    return svg_wrap(1024, 1024, f'''
{SHADOW}
{topic_card(rank, emoji, title, desc, tag, heat, color, light, lk)}
''')

def card_1():
    return card("TOP 1", "🥇",
        "NVIDIA RTX Spark",
        "英伟达发布全新AI PC芯片\\nWindows迎来真AI PC时代\\n知乎热榜第13名·124万热度",
        "英伟达", "124万热度 · 知乎热榜#13",
        NVIDIA, NVIDIAS, "nvidia")

def card_2():
    return card("TOP 2", "🥈",
        "宇树科技IPO过会",
        "人形机器人第一股来了\\n王兴兴身家或超140亿\\n具身智能赛道大爆发",
        "机器人", "75万热度 · 知乎热榜#20",
        UNITREE, UNITREES, "unitree")

def card_3():
    return card("TOP 3", "🥉",
        "Anthropic 抢跑IPO",
        "估值近万亿美元\\n秘密申请IPO冲击AI史上最大IPO\\n奥特曼：竞争核心是技术",
        "AI资本", "AI圈热议 · 36kr热榜#2",
        ANTHROPIC, ANTHROPICS, "anthropic")

def card_4():
    return card("TOP 4", "🏅",
        "DeepSeek-V4 降价97.5%",
        "腾讯云宣布最高降价97.5%\\n全面对齐官方出厂价\\n大模型价格战杀疯了",
        "降价", "AI圈热议 · 媒体刷屏",
        DEEPSEEK, DEEPSEEKS, "deepseek")

def card_5():
    return card("TOP 5", "🏅",
        "字节AI大地震",
        "AI大将顾全全离职\\n豆包6月下旬正式付费\\n字节AI面临内外变局",
        "字节跳动", "AI圈热议 · 36kr独家",
        BYTEDANCE, BYTEDANCES, "bytedance")

def banner():
    topics = [
        ("🥇", "NVIDIA RTX Spark",     "124万热度",     "AI PC芯片",   NVIDIA,    NVIDIAS,    "nvidia"),
        ("🥈", "宇树科技IPO过会",      "75万热度",      "人形机器人",  UNITREE,   UNITREES,   "unitree"),
        ("🥉", "Anthropic抢跑IPO",     "AI圈热议",      "估值万亿美元",ANTHROPIC, ANTHROPICS, "anthropic"),
        ("🏅", "DeepSeek-V4降价97.5%", "媒体刷屏",      "大模型价格战",DEEPSEEK,  DEEPSEEKS,  "deepseek"),
        ("🏅", "字节AI大地震",         "36kr独家",      "豆包付费",   BYTEDANCE, BYTEDANCES, "bytedance"),
    ]
    rows = ""
    for i, (emoji, name, heat, tag, color, light, lk) in enumerate(topics):
        y = 230 + i * 115
        rows += f'''
<g transform="translate(100, {y})">
  <rect x="0" y="0" width="1592" height="88" rx="16" fill="{W}" filter="url(#shadow2)"/>
  <g transform="translate(20, 18)">{logo_svg(lk)}</g>
  <text x="90" y="55" {FONT} font-size="30">{emoji}</text>
  <text x="170" y="55" {FONT} font-size="26" font-weight="700" fill="{T}">{name}</text>
  <text x="620" y="55" {FONT} font-size="21" fill="{color}" font-weight="600">{heat}</text>
  <rect x="780" y="24" width="160" height="40" rx="20" fill="{light}" stroke="{color}" stroke-width="1"/>
  <text x="860" y="51" text-anchor="middle" {FONT} font-size="16" font-weight="600" fill="{color}">{tag}</text>
</g>'''
    return svg_wrap(1792, 1024, f'''
{SHADOW}
{SHADOW2}
<rect x="100" y="50" width="1592" height="888" rx="28" fill="{W}" filter="url(#shadow)"/>
<g transform="translate(870, 55)">{logo_svg("zhihu")}</g>
<text x="896" y="160" text-anchor="middle" {FONT} font-size="52" font-weight="900" fill="{T}">知乎AI热榜 TOP5 🔥</text>
<text x="896" y="200" text-anchor="middle" {FONT} font-size="20" fill="{TD}">2026.06.03</text>
{rows}
<text x="896" y="920" text-anchor="middle" {FONT} font-size="18" fill="{TL}">数据 via opencli zhihu + tophub.today | 你还刷到了什么？评论区说说 👇</text>
''')

if __name__ == "__main__":
    cards = [
        ("zhihu-ai-hot5-cover", cover()),
        ("zhihu-ai-hot5-card-1", card_1()),
        ("zhihu-ai-hot5-card-2", card_2()),
        ("zhihu-ai-hot5-card-3", card_3()),
        ("zhihu-ai-hot5-card-4", card_4()),
        ("zhihu-ai-hot5-card-5", card_5()),
        ("zhihu-ai-hot5-banner", banner()),
    ]
    for name, svg in cards:
        svg_path = os.path.join(ROOT, f"{name}.svg")
        png_path = os.path.join(ROOT, f"{name}.png")
        with open(svg_path, "w") as f:
            f.write(svg)
        w = 1792 if "banner" in name else 1024
        subprocess.run(["inkscape", svg_path, "-o", png_path, "-w", str(w), "-h", "1024"], check=True, capture_output=True)
        print(f"  ✓ {name}.png ({os.path.getsize(png_path)//1024} KB)")
    print("Done! 7 cards regenerated.")