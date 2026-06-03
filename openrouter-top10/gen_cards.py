#!/usr/bin/env python3
"""Generate 9 SVG cards for OpenRouter Coding Agents TOP10 (Xiaohongshu style)."""

import os

OUT = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/openrouter-top10"
os.makedirs(OUT, exist_ok=True)

W, H = 800, 800
FONT = "system-ui,-apple-system,sans-serif"

# --- app data ---
apps = [
    ("Hermes Agent", "629B", "#7C3AED", "H", "Nous Research 出品，开源自主 Agent。跨会话记忆 + 子 Agent 并行 + 40+ 内置工具。"),
    ("OpenClaw",      "154B", "#0891B2", "O", "飞书生态 + 50+ 消息平台接入。ClawHub 4.4 万技能库，370K GitHub Star。"),
    ("Kilo Code",     "136B", "#059669", "K", "VS Code/JetBrains/CLI 三端通吃。Orchestrator 模式，150万用户，800万美金种子轮。"),
    ("Claude Code",   "56.7B","#D97706", "C", "Anthropic 官方出品。读全库、跨文件改、跑测试、迭代修复。最稳编码 Agent。"),
    ("pi",            "37.5B","#DC2626", "π",  "自带 API Key，CLI 原生，主打个性化和隐私。你的专属编码 Agent。"),
    ("Roo Code",      "20B",  "#7C3AED", "R", "VS Code 插件，给你一支专业 Agent 团队。架构师/编码/调试/审查各司其职。"),
    ("Cline",         "19.1B","#2563EB", "C", "IDE 里的自主 Agent。翻代码库、改文件、跑终端、浏览器自动化。"),
    ("Lemonade",      "12.9B","#F59E0B", "L", "专做 Roblox 游戏的 AI 工具。很垂直的方向。"),
    ("Codex",         "7.37B","#059669", "C", "OpenAI 官方编码 Agent。新加浏览器控制，还在起步阶段。"),
    ("Zed Editor",    "4.86B","#6366F1", "Z", "Rust 高性能编辑器，Atom 原班人马。AI 辅助编码 + 低延迟协作。"),
]

def bg(w, h, tint="0F0F23"):
    return f'<rect width="{w}" height="{h}" fill="#{tint}" rx="24"/>'

def defs_block():
    return f'''<defs>
  <linearGradient id="g1" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#7C3AED" stop-opacity=".15"/>
    <stop offset="50%" stop-color="#0891B2" stop-opacity=".08"/>
    <stop offset="100%" stop-color="#6366F1" stop-opacity=".15"/>
  </linearGradient>
  <linearGradient id="g2" x1="0%" y1="100%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#7C3AED" stop-opacity=".1"/>
    <stop offset="100%" stop-color="#2563EB" stop-opacity=".05"/>
  </linearGradient>
  <linearGradient id="accentBar" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#7C3AED"/>
    <stop offset="50%" stop-color="#0891B2"/>
    <stop offset="100%" stop-color="#6366F1"/>
  </linearGradient>
  <linearGradient id="accentGold" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#F59E0B"/>
    <stop offset="100%" stop-color="#D97706"/>
  </linearGradient>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="6" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="shadow" x="-10%" y="-10%" width="130%" height="130%">
    <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#000" flood-opacity=".3"/>
  </filter>
</defs>'''

def logo_circle(cx, cy, r, color, letter, font_size=20):
    return f'''<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" filter="url(#shadow)"/>
<text x="{cx}" y="{cy+font_size*0.35}" text-anchor="middle" fill="white" font-size="{font_size}" font-weight="700" font-family="{FONT}">{letter}</text>'''

def stat_card(x, y, w, h, rank, name, tokens, color):
    return f'''<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{color}" opacity=".12"/>
<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="none" stroke="{color}" stroke-width="1.5" opacity=".3"/>
<text x="{x+16}" y="{y+30}" fill="{color}" font-size="22" font-weight="700" font-family="{FONT}">{rank}</text>
<text x="{x+46}" y="{y+28}" fill="#E2E8F0" font-size="13" font-weight="600" font-family="{FONT}">{name}</text>
<text x="{x+46}" y="{y+48}" fill="{color}" font-size="16" font-weight="700" font-family="{FONT}">{tokens}</text>'''

def entry_block(x, y, w, h, rank, name, tokens, color, letter, desc, font_size=20):
    lines = []
    ly = y + 20
    # rank badge
    lines.append(f'''<rect x="{x+8}" y="{y+12}" width="28" height="20" rx="6" fill="{color}" opacity=".2"/>
<text x="{x+22}" y="{y+26}" text-anchor="middle" fill="{color}" font-size="12" font-weight="700" font-family="{FONT}">{rank}</text>''')
    # logo circle
    lines.append(logo_circle(x + 44, y + 22, 18, color, letter, font_size))
    # name + tokens
    lines.append(f'<text x="{x+74}" y="{y+20}" fill="#F1F5F9" font-size="15" font-weight="700" font-family="{FONT}">{name}</text>')
    lines.append(f'<text x="{x+74}" y="{y+38}" fill="{color}" font-size="12" font-weight="600" font-family="{FONT}">{tokens} tokens</text>')
    # description
    lines.append(f'<text x="{x+12}" y="{y+60}" fill="#94A3B8" font-size="11" font-family="{FONT}">{desc}</text>')
    # separator
    lines.append(f'<line x1="{x+12}" y1="{y+88}" x2="{x+w-12}" y2="{y+88}" stroke="#1E293B" stroke-width="1"/>')
    return '\n'.join(lines)

def save_svg(num, svg):
    path = os.path.join(OUT, f"or-card-{num}.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"  -> {path}")

def card_svg(content):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
{defs_block()}
{bg(W, H)}
<rect width="{W}" height="{H}" fill="url(#g1)"/>
{content}
</svg>'''

# ================================================================
# CARD 1: Cover
# ================================================================
def make_card1():
    c = f'''<text x="400" y="120" text-anchor="middle" fill="white" font-size="42" font-weight="800" font-family="{FONT}" letter-spacing="1">OpenRouter</text>
<text x="400" y="170" text-anchor="middle" fill="url(#accentBar)" font-size="36" font-weight="800" font-family="{FONT}" letter-spacing="2">Coding Agents TOP10</text>
<text x="400" y="210" text-anchor="middle" fill="#64748B" font-size="14" font-family="{FONT}">月度 Token 消耗排行 · {apps[0][1]} ~ {apps[9][1]}</text>
<line x1="260" y1="235" x2="540" y2="235" stroke="url(#accentBar)" stroke-width="2" opacity=".5"/>
<text x="400" y="275" text-anchor="middle" fill="#94A3B8" font-size="13" font-family="{FONT}">🔥 开源 Agent 霸榜 90% · IDE 插件 vs 通用 Agent</text>'''
    # 5 mini stat cards
    top5 = apps[:5]
    card_w = 140
    card_h = 65
    gap = 16
    total_w = 5 * card_w + 4 * gap
    start_x = (W - total_w) // 2
    colors = ["#7C3AED", "#0891B2", "#059669", "#D97706", "#DC2626"]
    for i, (name, tokens, color, letter, desc) in enumerate(top5):
        cx = start_x + i * (card_w + gap)
        cy = 310
        c += stat_card(cx, cy, card_w, card_h, f"{i+1}", name, tokens, colors[i])

    # bottom decorative
    c += f'''<text x="400" y="460" text-anchor="middle" fill="#334155" font-size="11" font-family="{FONT}">Powered by OpenRouter Leaderboard</text>
<rect x="300" y="490" width="200" height="40" rx="20" fill="none" stroke="#7C3AED" stroke-width="1.5" opacity=".4"/>
<text x="400" y="516" text-anchor="middle" fill="#7C3AED" font-size="13" font-weight="600" font-family="{FONT}">&#9654; 滑动查看排名</text>'''
    # decoration circles
    c += '''<circle cx="80" cy="700" r="120" fill="#7C3AED" opacity=".04"/>
<circle cx="720" cy="100" r="100" fill="#0891B2" opacity=".04"/>
<circle cx="650" cy="650" r="80" fill="#6366F1" opacity=".04"/>'''
    return card_svg(c)

# ================================================================
# CARD 2: #1 + #2
# ================================================================
def make_card2():
    a1, a2 = apps[0], apps[1]
    c = f'''<rect x="30" y="20" width="740" height="40" rx="20" fill="url(#accentBar)" opacity=".15"/>
<text x="400" y="46" text-anchor="middle" fill="url(#accentBar)" font-size="16" font-weight="800" font-family="{FONT}">OpenRouter Coding Agents TOP10</text>'''
    for i, (name, tokens, color, letter, desc) in enumerate([a1, a2]):
        y = 90 + i * 160
        # card bg
        c += f'''<rect x="40" y="{y}" width="720" height="140" rx="16" fill="#1E1E3A" opacity=".4" filter="url(#shadow)"/>
<rect x="40" y="{y}" width="720" height="140" rx="16" fill="none" stroke="{color}" stroke-width="1" opacity=".2"/>'''
        c += entry_block(40, y, 720, 140, f"{i+1}", name, tokens, color, letter, desc, 22)
    # extra info for Hermes
    c += f'''<text x="60" y="416" fill="#94A3B8" font-size="11" font-family="{FONT}">&#127775; 跨会话记忆 + 子 Agent 并行 + 40+ 内置工具</text>
<text x="60" y="440" fill="#64748B" font-size="11" font-family="{FONT}">&#127775; Nous Research 出品，开源自主 Agent</text>'''
    # extra info for OpenClaw
    c += f'''<text x="60" y="580" fill="#94A3B8" font-size="11" font-family="{FONT}">&#127775; 飞书生态 + 50+ 消息平台接入</text>
<text x="60" y="604" fill="#64748B" font-size="11" font-family="{FONT}">&#127775; ClawHub 4.4 万技能库 · 370K GitHub Star</text>'''
    c += '''<circle cx="700" cy="650" r="100" fill="#7C3AED" opacity=".04"/>
<circle cx="100" cy="700" r="80" fill="#0891B2" opacity=".04"/>'''
    return card_svg(c)

# ================================================================
# CARD 3: #3 #4 #5
# ================================================================
def make_card3():
    c = f'''<rect x="30" y="20" width="740" height="40" rx="20" fill="url(#accentBar)" opacity=".15"/>
<text x="400" y="46" text-anchor="middle" fill="url(#accentBar)" font-size="16" font-weight="800" font-family="{FONT}">OpenRouter Coding Agents TOP10</text>'''
    for i, (name, tokens, color, letter, desc) in enumerate(apps[2:5]):
        y = 85 + i * 140
        c += f'''<rect x="40" y="{y}" width="720" height="125" rx="16" fill="#1E1E3A" opacity=".4" filter="url(#shadow)"/>
<rect x="40" y="{y}" width="720" height="125" rx="16" fill="none" stroke="{color}" stroke-width="1" opacity=".2"/>'''
        c += entry_block(40, y, 720, 125, f"{i+3}", name, tokens, color, letter, desc, 20)
    c += '''<circle cx="700" cy="700" r="90" fill="#059669" opacity=".04"/>
<circle cx="100" cy="100" r="70" fill="#D97706" opacity=".04"/>'''
    return card_svg(c)

# ================================================================
# CARD 4: #6 #7 #8
# ================================================================
def make_card4():
    c = f'''<rect x="30" y="20" width="740" height="40" rx="20" fill="url(#accentBar)" opacity=".15"/>
<text x="400" y="46" text-anchor="middle" fill="url(#accentBar)" font-size="16" font-weight="800" font-family="{FONT}">OpenRouter Coding Agents TOP10</text>'''
    for i, (name, tokens, color, letter, desc) in enumerate(apps[5:8]):
        y = 85 + i * 140
        c += f'''<rect x="40" y="{y}" width="720" height="125" rx="16" fill="#1E1E3A" opacity=".4" filter="url(#shadow)"/>
<rect x="40" y="{y}" width="720" height="125" rx="16" fill="none" stroke="{color}" stroke-width="1" opacity=".2"/>'''
        c += entry_block(40, y, 720, 125, f"{i+6}", name, tokens, color, letter, desc, 20)
    c += '''<circle cx="700" cy="80" r="90" fill="#7C3AED" opacity=".04"/>
<circle cx="100" cy="700" r="80" fill="#F59E0B" opacity=".04"/>'''
    return card_svg(c)

# ================================================================
# CARD 5: #9 #10 + Summary
# ================================================================
def make_card5():
    a9, a10 = apps[8], apps[9]
    c = f'''<rect x="30" y="20" width="740" height="40" rx="20" fill="url(#accentBar)" opacity=".15"/>
<text x="400" y="46" text-anchor="middle" fill="url(#accentBar)" font-size="16" font-weight="800" font-family="{FONT}">OpenRouter Coding Agents TOP10</text>'''
    for i, (name, tokens, color, letter, desc) in enumerate([a9, a10]):
        y = 85 + i * 140
        c += f'''<rect x="40" y="{y}" width="720" height="125" rx="16" fill="#1E1E3A" opacity=".4" filter="url(#shadow)"/>
<rect x="40" y="{y}" width="720" height="125" rx="16" fill="none" stroke="{color}" stroke-width="1" opacity=".2"/>'''
        c += entry_block(40, y, 720, 125, f"{i+9}", name, tokens, color, letter, desc, 20)

    # summary
    y = 390
    c += f'''<rect x="40" y="{y}" width="720" height="160" rx="16" fill="#1E1E3A" opacity=".5" filter="url(#shadow)"/>
<rect x="40" y="{y}" width="720" height="160" rx="16" fill="none" stroke="url(#accentBar)" stroke-width="1.5" opacity=".3"/>'''
    c += f'''<text x="400" y="{y+32}" text-anchor="middle" fill="url(#accentGold)" font-size="18" font-weight="800" font-family="{FONT}">&#128202; 排名速览</text>'''
    stats = [
        ("1", "Hermes Agent", "629B", "#7C3AED"),
        ("2", "OpenClaw", "154B", "#0891B2"),
        ("3", "Kilo Code", "136B", "#059669"),
        ("4", "Claude Code", "56.7B", "#D97706"),
        ("5", "pi", "37.5B", "#DC2626"),
    ]
    for i, (r, n, t, col) in enumerate(stats):
        row_x = 60 + (i % 3) * 240
        row_y = y + 60 + (i // 3) * 40
        c += f'<text x="{row_x}" y="{row_y}" fill="{col}" font-size="14" font-weight="700" font-family="{FONT}">#{r}</text>'
        c += f'<text x="{row_x+30}" y="{row_y}" fill="#E2E8F0" font-size="13" font-family="{FONT}">{n}</text>'
        c += f'<text x="{row_x+170}" y="{row_y}" fill="{col}" font-size="13" font-weight="600" font-family="{FONT}">{t}</text>'
    c += '''<circle cx="720" cy="700" r="90" fill="#6366F1" opacity=".04"/>
<circle cx="80" cy="80" r="70" fill="#059669" opacity=".04"/>'''
    return card_svg(c)

# ================================================================
# CARD 6: Insight "开源 90% 碾压闭源"
# ================================================================
def make_card6():
    c = f'''<text x="400" y="80" text-anchor="middle" fill="url(#accentBar)" font-size="16" font-weight="800" font-family="{FONT}">&#128300; 深度观察</text>
<text x="400" y="180" text-anchor="middle" fill="white" font-size="48" font-weight="800" font-family="{FONT}">开源 &#128200; 碾压闭源</text>
<text x="400" y="230" text-anchor="middle" fill="#94A3B8" font-size="18" font-family="{FONT}">前 10 里 9 个开源，只有 Claude Code 是闭源</text>
<line x1="200" y1="260" x2="600" y2="260" stroke="url(#accentBar)" stroke-width="2" opacity=".4"/>'''
    # bar chart visual
    bar_y = 310
    c += f'''<rect x="120" y="{bar_y}" width="560" height="40" rx="8" fill="#1E293B"/>
<rect x="120" y="{bar_y}" width="504" height="40" rx="8" fill="#7C3AED" opacity=".8"/>
<text x="400" y="{bar_y+26}" text-anchor="middle" fill="white" font-size="15" font-weight="700" font-family="{FONT}">开源 90% (9/10)</text>'''
    bar_y += 60
    c += f'''<rect x="120" y="{bar_y}" width="560" height="40" rx="8" fill="#1E293B"/>
<rect x="120" y="{bar_y}" width="56" height="40" rx="8" fill="#D97706" opacity=".8"/>
<text x="400" y="{bar_y+26}" text-anchor="middle" fill="#94A3B8" font-size="15" font-weight="600" font-family="{FONT}">闭源 10% (1/10)</text>'''
    # annotation
    c += f'''<text x="400" y="480" text-anchor="middle" fill="#64748B" font-size="13" font-family="{FONT}">Claude Code (Anthropic) 是唯一闭源选手</text>
<text x="400" y="510" text-anchor="middle" fill="#64748B" font-size="13" font-family="{FONT}">Hermes Agent、OpenClaw、Kilo Code 领跑开源阵营</text>'''
    # bottom insight
    y = 570
    c += f'''<rect x="60" y="{y}" width="680" height="120" rx="16" fill="#1E1E3A" opacity=".5" filter="url(#shadow)"/>
<rect x="60" y="{y}" width="680" height="120" rx="16" fill="none" stroke="#7C3AED" stroke-width="1" opacity=".3"/>
<text x="400" y="{y+40}" text-anchor="middle" fill="#E2E8F0" font-size="15" font-weight="600" font-family="{FONT}">&#128161; 开源生态正在重塑编码 Agent 市场</text>
<text x="400" y="{y+65}" text-anchor="middle" fill="#94A3B8" font-size="12" font-family="{FONT}">社区驱动创新 + 快速迭代 = 碾压式领先</text>
<text x="400" y="{y+85}" text-anchor="middle" fill="#94A3B8" font-size="12" font-family="{FONT}">闭源方案只有在生态壁垒够高时才有一战之力</text>'''
    c += '''<circle cx="80" cy="700" r="100" fill="#7C3AED" opacity=".04"/>
<circle cx="720" cy="80" r="80" fill="#D97706" opacity=".04"/>'''
    return card_svg(c)

# ================================================================
# CARD 7: Insight "IDE 三兄弟 fork 链"
# ================================================================
def make_card7():
    c = f'''<text x="400" y="60" text-anchor="middle" fill="url(#accentBar)" font-size="16" font-weight="800" font-family="{FONT}">&#128300; 深度观察</text>
<text x="400" y="130" text-anchor="middle" fill="white" font-size="42" font-weight="800" font-family="{FONT}">IDE 三兄弟 fork 链</text>
<text x="400" y="170" text-anchor="middle" fill="#94A3B8" font-size="16" font-family="{FONT}">Kilo Code &#8594; Roo Code &#8594; Cline 同源进化</text>
<line x1="220" y1="195" x2="580" y2="195" stroke="url(#accentBar)" stroke-width="2" opacity=".4"/>'''
    # fork tree visual
    # Cline at top center
    cx, cy = 400, 250
    c += logo_circle(cx, cy, 24, "#2563EB", "C", 22)
    c += f'<text x="{cx}" y="{cy+40}" text-anchor="middle" fill="#E2E8F0" font-size="14" font-weight="700" font-family="{FONT}">Cline (19.1B)</text>'
    c += f'<text x="{cx}" y="{cy+58}" text-anchor="middle" fill="#64748B" font-size="11" font-family="{FONT}">&#127919; IDE 自主 Agent 始祖</text>'
    # fork lines
    lx = 200
    rx = 600
    fy = 340
    # left branch
    c += f'''<line x1="{cx}" y1="{cy+30}" x2="{lx}" y2="{fy}" stroke="#64748B" stroke-width="1.5" stroke-dasharray="4,3" opacity=".6"/>
<line x1="{lx}" y1="290" x2="{lx}" y2="{fy}" stroke="#64748B" stroke-width="1.5" opacity=".6"/>'''
    # right branch
    c += f'''<line x1="{cx}" y1="{cy+30}" x2="{rx}" y2="{fy}" stroke="#64748B" stroke-width="1.5" stroke-dasharray="4,3" opacity=".6"/>
<line x1="{rx}" y1="290" x2="{rx}" y2="{fy}" stroke="#64748B" stroke-width="1.5" opacity=".6"/>'''
    # Kilo Code (left)
    c += logo_circle(lx, fy, 24, "#059669", "K", 22)
    c += f'<text x="{lx}" y="{fy+40}" text-anchor="middle" fill="#E2E8F0" font-size="14" font-weight="700" font-family="{FONT}">Kilo Code (136B)</text>'
    c += f'<text x="{lx}" y="{fy+58}" text-anchor="middle" fill="#64748B" font-size="11" font-family="{FONT}">&#128640; 三端通吃 + Orchestrator</text>'
    c += f'<text x="{lx}" y="{fy+74}" text-anchor="middle" fill="#64748B" font-size="11" font-family="{FONT}">150万用户 · 800万美金种子轮</text>'
    # Roo Code (right)
    c += logo_circle(rx, fy, 24, "#7C3AED", "R", 22)
    c += f'<text x="{rx}" y="{fy+40}" text-anchor="middle" fill="#E2E8F0" font-size="14" font-weight="700" font-family="{FONT}">Roo Code (20B)</text>'
    c += f'<text x="{rx}" y="{fy+58}" text-anchor="middle" fill="#64748B" font-size="11" font-family="{FONT}">&#128101; Agent 团队模式</text>'
    c += f'<text x="{rx}" y="{fy+74}" text-anchor="middle" fill="#64748B" font-size="11" font-family="{FONT}">架构/编码/调试/审查</text>'
    # bottom insight
    y = 460
    c += f'''<rect x="60" y="{y}" width="680" height="230" rx="16" fill="#1E1E3A" opacity=".5" filter="url(#shadow)"/>
<rect x="60" y="{y}" width="680" height="230" rx="16" fill="none" stroke="url(#accentBar)" stroke-width="1.5" opacity=".3"/>'''
    c += f'''<text x="400" y="{y+35}" text-anchor="middle" fill="url(#accentGold)" font-size="16" font-weight="800" font-family="{FONT}">&#128161; fork 链背后的格局</text>'''
    insights = [
        "Cline 是始祖，Kilo Code 和 Roo Code 都 fork 自它",
        "Kilo Code 走商业化路线，三端通吃 + 融资扩张",
        "Roo Code 专注 IDE 插件内的 Agent 团队协作",
        "三个项目底层共享大量 DNA，但方向各不相同",
        "这是开源生态最典型的进化模式：fork + 差异化",
    ]
    for i, ins in enumerate(insights):
        iy = y + 65 + i * 32
        c += f'''<circle cx="80" cy="{iy-8}" r="4" fill="#7C3AED" opacity=".8"/>
<text x="95" y="{iy}" fill="#94A3B8" font-size="12" font-family="{FONT}">{ins}</text>'''
    c += '''<circle cx="720" cy="700" r="90" fill="#2563EB" opacity=".04"/>
<circle cx="80" cy="80" r="70" fill="#059669" opacity=".04"/>'''
    return card_svg(c)

# ================================================================
# CARD 8: Insight "Agent 走出编辑器"
# ================================================================
def make_card8():
    c = f'''<text x="400" y="60" text-anchor="middle" fill="url(#accentBar)" font-size="16" font-weight="800" font-family="{FONT}">&#128300; 深度观察</text>
<text x="400" y="140" text-anchor="middle" fill="white" font-size="42" font-weight="800" font-family="{FONT}">Agent 走出编辑器</text>
<text x="400" y="185" text-anchor="middle" fill="#94A3B8" font-size="16" font-family="{FONT}">前 5 名里 4 个是通用 Agent（不绑 IDE）</text>
<line x1="200" y1="215" x2="600" y2="215" stroke="url(#accentBar)" stroke-width="2" opacity=".4"/>'''
    # visual: IDE plugin vs General Agent
    y = 260
    # left: IDE plugin
    c += f'''<rect x="60" y="{y}" width="320" height="200" rx="16" fill="#1E1E3A" opacity=".5" filter="url(#shadow)"/>
<rect x="60" y="{y}" width="320" height="200" rx="16" fill="none" stroke="#D97706" stroke-width="1.5" opacity=".4"/>
<text x="220" y="{y+35}" text-anchor="middle" fill="#D97706" font-size="15" font-weight="700" font-family="{FONT}">&#128187; IDE 插件型</text>
<text x="220" y="{y+55}" text-anchor="middle" fill="#94A3B8" font-size="12" font-family="{FONT}">Kilo Code · Roo Code · Cline</text>'''
    plugins = ["绑定 VS Code/JetBrains", "依赖编辑器生态", "深度文件系统集成", "1 个上榜 (Kilo Code)"]
    for i, p in enumerate(plugins):
        py = y + 85 + i * 28
        c += f'<circle cx="80" cy="{py-6}" r="3" fill="#D97706"/><text x="95" y="{py}" fill="#64748B" font-size="11" font-family="{FONT}">{p}</text>'
    # right: General Agent
    c += f'''<rect x="420" y="{y}" width="320" height="200" rx="16" fill="#1E1E3A" opacity=".5" filter="url(#shadow)"/>
<rect x="420" y="{y}" width="320" height="200" rx="16" fill="none" stroke="#7C3AED" stroke-width="1.5" opacity=".4"/>
<text x="580" y="{y+35}" text-anchor="middle" fill="#7C3AED" font-size="15" font-weight="700" font-family="{FONT}">&#127758; 通用 Agent</text>
<text x="580" y="{y+55}" text-anchor="middle" fill="#94A3B8" font-size="12" font-family="{FONT}">Hermes · OpenClaw · Claude Code · pi</text>'''
    generals = ["跨平台/跨 IDE", "CLI/API 原生", "可集成到任意工作流", "4 个上榜 (前 5 占 4)"]
    for i, g in enumerate(generals):
        gy = y + 85 + i * 28
        c += f'<circle cx="440" cy="{gy-6}" r="3" fill="#7C3AED"/><text x="455" y="{gy}" fill="#64748B" font-size="11" font-family="{FONT}">{g}</text>'
    # bottom insight
    y2 = 500
    c += f'''<rect x="60" y="{y2}" width="680" height="180" rx="16" fill="#1E1E3A" opacity=".5" filter="url(#shadow)"/>
<rect x="60" y="{y2}" width="680" height="180" rx="16" fill="none" stroke="url(#accentBar)" stroke-width="1" opacity=".3"/>
<text x="400" y="{y2+35}" text-anchor="middle" fill="url(#accentGold)" font-size="16" font-weight="800" font-family="{FONT}">&#128161; 趋势解读</text>'''
    trends = [
        "编码 Agent 的终极形态不是 IDE 插件，而是通用助手",
        "CLI 原生 + API 优先 = 可嵌入任何开发环境",
        "Hermes Agent 和 OpenClaw 代表了两种生态路径",
        "IDE 插件型 Agent 仍有价值，但天花板更低",
    ]
    for i, t in enumerate(trends):
        ty = y2 + 65 + i * 28
        c += f'''<circle cx="80" cy="{ty-6}" r="4" fill="#0891B2" opacity=".8"/>
<text x="95" y="{ty}" fill="#94A3B8" font-size="12" font-family="{FONT}">{t}</text>'''
    c += '''<circle cx="720" cy="80" r="90" fill="#7C3AED" opacity=".04"/>
<circle cx="80" cy="700" r="80" fill="#0891B2" opacity=".04"/>'''
    return card_svg(c)

# ================================================================
# CARD 9: Closing
# ================================================================
def make_card9():
    c = f'''<text x="400" y="160" text-anchor="middle" fill="white" font-size="36" font-weight="800" font-family="{FONT}">OpenRouter</text>
<text x="400" y="210" text-anchor="middle" fill="url(#accentBar)" font-size="30" font-weight="800" font-family="{FONT}">Coding Agents TOP10</text>
<line x1="260" y1="240" x2="540" y2="240" stroke="url(#accentBar)" stroke-width="2" opacity=".5"/>
<text x="400" y="290" text-anchor="middle" fill="#94A3B8" font-size="16" font-family="{FONT}">数据来源：OpenRouter Leaderboard</text>
<text x="400" y="320" text-anchor="middle" fill="#64748B" font-size="13" font-family="{FONT}">月度 Token 消耗排行 · 实时更新</text>'''
    # 3 key takeaways
    takes = [
        ("&#128200;", "开源 90% 碾压闭源", "9/10 开源，社区驱动创新", "#7C3AED"),
        ("&#128279;", "fork 链进化", "Cline → Kilo Code / Roo Code", "#0891B2"),
        ("&#127758;", "Agent 走出编辑器", "通用 Agent 占前 5 中 4 席", "#059669"),
    ]
    for i, (emoji, title, desc, col) in enumerate(takes):
        bx = 60 + i * 240
        by = 380
        c += f'''<rect x="{bx}" y="{by}" width="220" height="140" rx="16" fill="#1E1E3A" opacity=".5" filter="url(#shadow)"/>
<rect x="{bx}" y="{by}" width="220" height="140" rx="16" fill="none" stroke="{col}" stroke-width="1.5" opacity=".3"/>
<text x="{bx+110}" y="{by+35}" text-anchor="middle" fill="white" font-size="24" font-family="{FONT}">{emoji}</text>
<text x="{bx+110}" y="{by+70}" text-anchor="middle" fill="{col}" font-size="14" font-weight="700" font-family="{FONT}">{title}</text>
<text x="{bx+110}" y="{by+95}" text-anchor="middle" fill="#94A3B8" font-size="11" font-family="{FONT}">{desc}</text>'''
    # CTA
    c += f'''<rect x="240" y="580" width="320" height="48" rx="24" fill="#7C3AED" opacity=".15"/>
<rect x="240" y="580" width="320" height="48" rx="24" fill="none" stroke="#7C3AED" stroke-width="1.5" opacity=".5"/>
<text x="400" y="610" text-anchor="middle" fill="#7C3AED" font-size="15" font-weight="700" font-family="{FONT}">&#9829; 点赞 + 收藏 ★ 持续更新</text>'''
    c += f'''<text x="400" y="670" text-anchor="middle" fill="#334155" font-size="11" font-family="{FONT}">#OpenRouter #CodingAgents #AI #开源 #HermesAgent #OpenClaw</text>'''
    c += '''<circle cx="80" cy="700" r="120" fill="#7C3AED" opacity=".04"/>
<circle cx="720" cy="80" r="100" fill="#0891B2" opacity=".04"/>
<circle cx="650" cy="650" r="80" fill="#6366F1" opacity=".04"/>'''
    return card_svg(c)

# ================================================================
# MAIN
# ================================================================
if __name__ == "__main__":
    print("Generating OpenRouter TOP10 cards...")
    cards = [make_card1, make_card2, make_card3, make_card4, make_card5, make_card6, make_card7, make_card8, make_card9]
    for idx, fn in enumerate(cards, 1):
        svg = fn()
        save_svg(idx, svg)
    print(f"Done! {len(cards)} cards saved to {OUT}")
