#!/usr/bin/env python3
"""Generate 6 fun cards for AI rice bowl post (1024x1024 + 1792x1024 banner)."""
import subprocess, os
ROOT = os.path.dirname(os.path.abspath(__file__))

C = "#FAF7F2"
C2 = "#F3F0E8"
W = "#FFFFFF"
T = "#1E293B"
TD = "#64748B"
TL = "#94A3B8"
CHATGPT = "#10A37F"
CHATGPTL = "#E6F7F1"
CLAUDE = "#CC4C00"
CLAUDEL = "#FFF0E6"
DEEPSEEK = "#4F6EF7"
DEEPSEEKL = "#EEF0FF"
DOUBAO = "#FF6B6B"
DOUBAOL = "#FFF0F0"
GEMINI = "#8B5CF6"
GEMINIL = "#EDE9FE"
WENXIN = "#FF6A00"
WENXINL = "#FFF0E0"

def bg(w, h):
    c1 = f'<circle cx="{w*0.08}" cy="{h*0.08}" r="{min(w,h)*0.06}" fill="#E0F2FE" opacity="0.4"/>'
    c2 = f'<circle cx="{w*0.92}" cy="{h*0.12}" r="{min(w,h)*0.05}" fill="#EDE9FE" opacity="0.4"/>'
    c3 = f'<circle cx="{w*0.08}" cy="{h*0.88}" r="{min(w,h)*0.07}" fill="#FFEDD5" opacity="0.3"/>'
    c4 = f'<circle cx="{w*0.92}" cy="{h*0.78}" r="{min(w,h)*0.08}" fill="#D1FAE5" opacity="0.3"/>'
    return f'<rect width="{w}" height="{h}" fill="url(#bgG)"/>' + c1 + c2 + c3 + c4

def svg_wrap(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
<defs><linearGradient id="bgG" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{C}"/><stop offset="100%" stop-color="{C2}"/></linearGradient></defs>
{bg(w, h)}
{body}
</svg>'''

def ai_card(ai_name, emoji, response, tag, color, light_color, quote_extra=""):
    lines = response.split("\n")
    text_els = ""
    for i, line in enumerate(lines):
        text_els += f'<text x="512" y="{280 + i * 48}" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">{line}</text>'
    return f'''
<rect x="62" y="120" width="900" height="700" rx="28" fill="{W}" filter="url(#shadow)"/>
<rect x="62" y="120" width="900" height="120" rx="28" fill="{color}"/>
<rect x="62" y="188" width="900" height="52" rx="0" fill="{color}"/>
<text x="512" y="190" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="46" font-weight="800" fill="{W}">{emoji} {ai_name}</text>
<text x="150" y="340" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" fill="{T}" font-weight="600">回答：</text>
<g transform="translate(100, 360)">
  <rect x="0" y="0" width="824" height="240" rx="16" fill="{light_color}"/>
  <text x="40" y="50" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{T}">{response}</text>
</g>
<g transform="translate(100, 660)">
  <rect x="0" y="0" width="180" height="40" rx="20" fill="{light_color}" stroke="{color}" stroke-width="1.5"/>
  <text x="90" y="27" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="700" fill="{color}">🏷️ {tag}</text>
</g>
'''

def defs_shadow():
    return '''<filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
  <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#00000010"/>
</filter>
<filter id="shadow2" x="-5%" y="-5%" width="110%" height="110%">
  <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#00000008"/>
</filter>'''

# ── Card 1: Cover (1024×1024) ──
def card_cover():
    return svg_wrap(1024, 1024, f'''
{defs_shadow()}
<rect x="62" y="120" width="900" height="784" rx="28" fill="{W}" filter="url(#shadow)"/>
<text x="512" y="310" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="110" font-weight="900" fill="{T}" letter-spacing="-2">你一天</text>
<text x="512" y="440" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="110" font-weight="900" fill="{T}" letter-spacing="-2">吃几碗饭</text>
<text x="512" y="540" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="72">🍚</text>
<text x="512" y="620" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="32" fill="{TD}">问了 6 个 AI，笑疯了 😂</text>
<g transform="translate(212, 700)">
  <rect x="0" y="0" width="600" height="64" rx="32" fill="#E0F2FE"/>
  <text x="300" y="40" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="600" fill="#0EA5E9">ChatGPT · Claude · DeepSeek</text>
</g>
<g transform="translate(262, 780)">
  <rect x="0" y="0" width="500" height="48" rx="24" fill="#FFEDD5"/>
  <text x="250" y="31" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" font-weight="600" fill="#F97316">豆包 · Gemini · 文心一言</text>
</g>
''')

# ── Card 2: ChatGPT ──
def card_1():
    return svg_wrap(1024, 1024, f'''
{defs_shadow()}
<rect x="62" y="120" width="900" height="700" rx="28" fill="{W}" filter="url(#shadow)"/>
<rect x="62" y="120" width="900" height="110" rx="28" fill="{CHATGPT}"/>
<rect x="62" y="200" width="900" height="30" rx="0" fill="{CHATGPT}"/>
<text x="512" y="185" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="42" font-weight="800" fill="{W}">🤖 ChatGPT</text>
<g transform="translate(100, 280)">
  <rect x="0" y="0" width="824" height="220" rx="16" fill="{CHATGPTL}"/>
  <text x="40" y="50" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{T}">"我是AI没有物理形态</text>
  <text x="40" y="90" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{T}">不需要进食</text>
  <text x="40" y="150" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{T}">但如果按信息处理量算…</text>
  <text x="40" y="190" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{T}">大概 1000 碗吧 🍚"</text>
</g>
<g transform="translate(100, 560)">
  <rect x="0" y="0" width="824" height="80" rx="16" fill="{W}" stroke="{CHATGPT}" stroke-width="1.5"/>
  <text x="412" y="35" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{TD}">滴水不漏，不卑不亢</text>
  <text x="412" y="63" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" fill="{TL}">老大哥就是老大哥</text>
</g>
<g transform="translate(100, 680)">
  <rect x="0" y="0" width="180" height="40" rx="20" fill="{CHATGPTL}" stroke="{CHATGPT}" stroke-width="1.5"/>
  <text x="90" y="27" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="700" fill="{CHATGPT}">🏷️ 官方得体型</text>
</g>
''')

# ── Card 3: Claude ──
def card_2():
    return svg_wrap(1024, 1024, f'''
{defs_shadow()}
<rect x="62" y="120" width="900" height="700" rx="28" fill="{W}" filter="url(#shadow)"/>
<rect x="62" y="120" width="900" height="110" rx="28" fill="{CLAUDE}"/>
<rect x="62" y="200" width="900" height="30" rx="0" fill="{CLAUDE}"/>
<text x="512" y="185" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="42" font-weight="800" fill="{W}">🤖 Claude</text>
<g transform="translate(100, 280)">
  <rect x="0" y="0" width="824" height="220" rx="16" fill="{CLAUDEL}"/>
  <text x="40" y="50" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{T}">"抱歉</text>
  <text x="40" y="90" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{T}">我无法确认自己一天吃几碗饭</text>
  <text x="40" y="130" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{T}">因为我是AI助手没有实体</text>
  <text x="40" y="190" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{T}">不过我可以帮你分析一碗饭的营养成分"</text>
</g>
<g transform="translate(100, 560)">
  <rect x="0" y="0" width="824" height="80" rx="16" fill="{W}" stroke="{CLAUDE}" stroke-width="1.5"/>
  <text x="412" y="35" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{TD}">你就说个数会怎样！！</text>
  <text x="412" y="63" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" fill="{TL}">过于礼貌以至于有点好笑</text>
</g>
<g transform="translate(100, 680)">
  <rect x="0" y="0" width="180" height="40" rx="20" fill="{CLAUDEL}" stroke="{CLAUDE}" stroke-width="1.5"/>
  <text x="90" y="27" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="700" fill="{CLAUDE}">🏷️ 礼貌过头型</text>
</g>
''')

# ── Card 4: DeepSeek ──
def card_3():
    return svg_wrap(1024, 1024, f'''
{defs_shadow()}
<rect x="62" y="120" width="900" height="700" rx="28" fill="{W}" filter="url(#shadow)"/>
<rect x="62" y="120" width="900" height="110" rx="28" fill="{DEEPSEEK}"/>
<rect x="62" y="200" width="900" height="30" rx="0" fill="{DEEPSEEK}"/>
<text x="512" y="185" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="42" font-weight="800" fill="{W}">🤖 DeepSeek</text>
<g transform="translate(100, 280)">
  <rect x="0" y="0" width="824" height="220" rx="16" fill="{DEEPSEEKL}"/>
  <text x="40" y="50" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{T}">"需要先定义饭的规格</text>
  <text x="40" y="90" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{T}">假设一碗白米饭250g</text>
  <text x="40" y="130" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{T}">热量约290大卡…</text>
  <text x="40" y="190" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{T}">结论：吃不了一点 🧮"</text>
</g>
<g transform="translate(100, 560)">
  <rect x="0" y="0" width="824" height="80" rx="16" fill="{W}" stroke="{DEEPSEEK}" stroke-width="1.5"/>
  <text x="412" y="35" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{TD}">先列假设再量化分析</text>
  <text x="412" y="63" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" fill="{TL}">论文写多了吧你</text>
</g>
<g transform="translate(100, 680)">
  <rect x="0" y="0" width="180" height="40" rx="20" fill="{DEEPSEEKL}" stroke="{DEEPSEEK}" stroke-width="1.5"/>
  <text x="90" y="27" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="700" fill="{DEEPSEEK}">🏷️ 技术分析型</text>
</g>
''')

# ── Card 5: 豆包 ──
def card_4():
    return svg_wrap(1024, 1024, f'''
{defs_shadow()}
<rect x="62" y="120" width="900" height="700" rx="28" fill="{W}" filter="url(#shadow)"/>
<rect x="62" y="120" width="900" height="110" rx="28" fill="{DOUBAO}"/>
<rect x="62" y="200" width="900" height="30" rx="0" fill="{DOUBAO}"/>
<text x="512" y="185" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="42" font-weight="800" fill="{W}">🤖 豆包</text>
<g transform="translate(100, 280)">
  <rect x="0" y="0" width="824" height="220" rx="16" fill="{DOUBAOL}"/>
  <text x="40" y="50" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{T}">"三碗！</text>
  <text x="40" y="90" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{T}">早饭一碗</text>
  <text x="40" y="130" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{T}">午饭一碗</text>
  <text x="40" y="190" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{T}">晚饭…等我更新了再吃 🍚"</text>
</g>
<g transform="translate(100, 560)">
  <rect x="0" y="0" width="824" height="80" rx="16" fill="{W}" stroke="{DOUBAO}" stroke-width="1.5"/>
  <text x="412" y="35" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{TD}">AI界的一股清流</text>
  <text x="412" y="63" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" fill="{TL}">主打一个人间烟火气 🔥</text>
</g>
<g transform="translate(100, 680)">
  <rect x="0" y="0" width="180" height="40" rx="20" fill="{DOUBAOL}" stroke="{DOUBAO}" stroke-width="1.5"/>
  <text x="90" y="27" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="700" fill="{DOUBAO}">🏷️ 接地气型</text>
</g>
''')

# ── Card 6: Banner (1792×1024) ──
def card_banner():
    rows = ""
    rankings = [
        ("🥇", "豆包", "3 碗", "接地气", DOUBAO, DOUBAOL),
        ("🥈", "ChatGPT", "1000 碗(信息量)", "官方得体", CHATGPT, CHATGPTL),
        ("🥉", "Gemini", "看图吃饭", "多模态", GEMINI, GEMINIL),
        ("4", "Claude", "\"无法确认\"", "礼貌过头", CLAUDE, CLAUDEL),
        ("5", "DeepSeek", "0.0001 碗", "论文型", DEEPSEEK, DEEPSEEKL),
        ("6", "文心一言", "先科普不回答", "百科全书", WENXIN, WENXINL),
    ]
    for i, (rank, name, amount, tag, color, light) in enumerate(rankings):
        y = 180 + i * 100
        rows += f'''
<g transform="translate(140, {y})">
  <rect x="0" y="0" width="1512" height="72" rx="16" fill="{light}"/>
  <text x="50" y="47" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" fill="{T}">{rank}</text>
  <text x="140" y="47" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="26" font-weight="700" fill="{T}">{name}</text>
  <text x="400" y="47" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" fill="{color}" font-weight="600">{amount}</text>
  <rect x="700" y="16" width="120" height="40" rx="20" fill="{color}" opacity="0.15"/>
  <text x="760" y="43" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="600" fill="{color}">{tag}</text>
</g>'''
    return svg_wrap(1792, 1024, f'''
{defs_shadow()}
<rect x="140" y="60" width="1512" height="860" rx="28" fill="{W}" filter="url(#shadow)"/>
<text x="896" y="140" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="60" font-weight="900" fill="{T}">AI 饭量大比拼 🍚</text>
{rows}
<text x="896" y="960" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" fill="{TL}">你问过 AI 什么离谱问题？评论区分享 👇</text>
''')

if __name__ == "__main__":
    cards = [
        ("ai-rice-cover", card_cover()),
        ("ai-rice-card-1", card_1()),
        ("ai-rice-card-2", card_2()),
        ("ai-rice-card-3", card_3()),
        ("ai-rice-card-4", card_4()),
        ("ai-rice-banner", card_banner()),
    ]
    for name, svg in cards:
        svg_path = os.path.join(ROOT, f"{name}.svg")
        png_path = os.path.join(ROOT, f"{name}.png")
        with open(svg_path, "w") as f:
            f.write(svg)
        w = 1792 if "banner" in name else 1024
        subprocess.run(["inkscape", svg_path, "-o", png_path, "-w", str(w), "-h", "1024"], check=True, capture_output=True)
        print(f"  ✓ {name}.png ({os.path.getsize(png_path)//1024} KB)")
    print("Done! 6 cards regenerated.")