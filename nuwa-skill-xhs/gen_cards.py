#!/usr/bin/env python3
"""Generate 6 SVG cards for nuwa-skill (Xiaohongshu style).

Layout:
  - nuwa-banner.png   1792 x 1024  (horizontal cover, used for Weibo/header)
  - nuwa-square.png   1024 x 1024  (square cover, XHS thumbnail)
  - nuwa-card-1.png   1024 x 1024  (6-agent parallel research)
  - nuwa-card-2.png   1024 x 1024  (5-layer mental model extraction)
  - nuwa-card-3.png   1024 x 1024  (13 distilled personas grid)
  - nuwa-card-4.png   1024 x 1024  (one-line install + 50+ runtimes)
"""

import os
import subprocess

OUT = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/nuwa-skill-xhs"
os.makedirs(OUT, exist_ok=True)

# ---------- palette ----------
BG       = "#0A0A14"
BG_PANEL = "#15151F"
BG_DEEP  = "#050509"
INK      = "#F5F5F7"
INK_DIM  = "#A1A1AA"
INK_MUTE = "#71717A"
LINE     = "#27272A"
RED      = "#DC2626"
RED_D    = "#EF4444"
PURPLE   = "#A855F7"
PURPLE_D = "#C084FC"
GOLD     = "#F59E0B"
CYAN     = "#06B6D4"
GREEN    = "#10B981"

FONT_SANS = "PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif"
FONT_MONO = "SF Mono, JetBrains Mono, IBM Plex Mono, Menlo, Consolas, monospace"


# ---------- shared defs ----------
def make_defs(extra=""):
    return (
        '<defs>\n'
        f'  <linearGradient id="redGrad" x1="0%" y1="0%" x2="100%" y2="0%">\n'
        f'    <stop offset="0%" stop-color="{RED}"/>\n'
        f'    <stop offset="100%" stop-color="{RED_D}"/>\n'
        '  </linearGradient>\n'
        f'  <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">\n'
        f'    <stop offset="0%" stop-color="{PURPLE}"/>\n'
        f'    <stop offset="100%" stop-color="{RED}"/>\n'
        '  </linearGradient>\n'
        f'  <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">\n'
        f'    <stop offset="0%" stop-color="{GOLD}"/>\n'
        f'    <stop offset="100%" stop-color="{RED}"/>\n'
        '  </linearGradient>\n'
        f'  <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">\n'
        f'    <stop offset="0%" stop-color="{BG_PANEL}"/>\n'
        f'    <stop offset="100%" stop-color="{BG_DEEP}"/>\n'
        '  </linearGradient>\n'
        '  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">\n'
        '    <feGaussianBlur stdDeviation="4" result="blur"/>\n'
        '    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>\n'
        '  </filter>\n'
        '  <filter id="shadow" x="-10%" y="-10%" width="130%" height="130%">\n'
        '    <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#000" flood-opacity=".5"/>\n'
        '  </filter>\n'
        '  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">\n'
        f'    <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{LINE}" stroke-width="0.5" opacity="0.4"/>\n'
        '  </pattern>\n'
        f'  {extra}\n'
        '</defs>'
    )


def make_base_bg(w, h):
    return (
        f'<rect width="{w}" height="{h}" fill="{BG}"/>\n'
        f'<rect width="{w}" height="{h}" fill="url(#grid)" opacity="0.3"/>\n'
        f'<circle cx="0" cy="0" r="300" fill="{RED}" opacity="0.08"/>\n'
        f'<circle cx="{w}" cy="{h}" r="400" fill="{PURPLE}" opacity="0.08"/>'
    )


def make_header(x=64, y=64):
    return (
        f'<g transform="translate({x},{y})">\n'
        f'  <rect x="0" y="0" width="6" height="36" fill="{RED}"/>\n'
        f'  <text x="20" y="20" font-family="{FONT_SANS}" font-size="14" font-weight="700" letter-spacing="3" fill="{RED}">NUWA · SKILL 造人术</text>\n'
        f'  <text x="20" y="34" font-family="{FONT_MONO}" font-size="11" letter-spacing="2" fill="{INK_MUTE}">2026.06 · 22K STARS · MIT</text>\n'
        '</g>'
    )


def make_footer(w, h, idx=None, total=4):
    page = f"CARD {idx:02d}/{total:02d}" if idx else ""
    return (
        f'<g transform="translate(64,{h-40})">\n'
        f'  <text x="0" y="0" font-family="{FONT_MONO}" font-size="11" letter-spacing="2" fill="{INK_MUTE}">SOURCE · github.com/alchaincyf/nuwa-skill</text>\n'
        f'  <text x="{w-128}" y="0" text-anchor="end" font-family="{FONT_MONO}" font-size="11" letter-spacing="2" fill="{INK_MUTE}">{page}</text>\n'
        '</g>'
    )


def make_chip(x, y, label, color, dark_text=False):
    text_color = BG if dark_text else color
    w = len(label) * 13 + 30
    return (
        f'<g transform="translate({x},{y})">\n'
        f'  <rect x="0" y="0" width="{w}" height="28" rx="14" fill="{color}" opacity="0.18"/>\n'
        f'  <rect x="0" y="0" width="{w}" height="28" rx="14" fill="none" stroke="{color}" stroke-width="1" opacity="0.6"/>\n'
        f'  <text x="{w/2}" y="18" text-anchor="middle" font-family="{FONT_SANS}" font-size="12" font-weight="600" fill="{text_color}">{label}</text>\n'
        '</g>'
    )


# ================================================================
# CARD: banner  (1792 x 1024) — horizontal cover
# ================================================================
def make_banner():
    W, H = 1792, 1024

    # Left column
    left = f'''
<!-- Eyebrow -->
<g transform="translate(96, 80)">
  <rect x="0" y="0" width="8" height="48" fill="{RED}"/>
  <text x="28" y="22" font-family="{FONT_SANS}" font-size="18" font-weight="700" letter-spacing="4" fill="{RED}">NUWA · SKILL 造人术</text>
  <text x="28" y="42" font-family="{FONT_MONO}" font-size="13" letter-spacing="2" fill="{INK_MUTE}">22K STARS · MIT · 50+ RUNTIMES</text>
</g>

<!-- Hero title -->
<g transform="translate(96, 300)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="220" font-weight="900" fill="url(#redGrad)" letter-spacing="-6">女娲</text>
  <text x="0" y="100" font-family="{FONT_SANS}" font-size="48" font-weight="500" fill="{INK}">蒸馏任何人的思维方式</text>
</g>

<!-- Tagline -->
<g transform="translate(96, 580)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="28" font-weight="400" fill="{INK_DIM}">输入一个名字 · 6 路 Agent 并行调研 · 三重验证提炼</text>
  <text x="0" y="40" font-family="{FONT_SANS}" font-size="28" font-weight="400" fill="{INK_DIM}">乔布斯 / 马斯克 / 芒格 / 费曼 / 纳瓦尔 / 塔勒布 ... 给你打工</text>
</g>

<!-- Chip row -->
<g transform="translate(96, 720)">
  {make_chip(0,    0, "心智模型", RED)}
  {make_chip(150,  0, "决策启发式", PURPLE)}
  {make_chip(330,  0, "表达 DNA", GOLD)}
  {make_chip(490,  0, "诚实边界", CYAN)}
  {make_chip(640,  0, "13 位已蒸馏", GREEN)}
</g>

<!-- Install -->
<g transform="translate(96, 820)">
  <rect x="0" y="0" width="700" height="64" rx="8" fill="{BG_PANEL}" filter="url(#shadow)"/>
  <rect x="0" y="0" width="700" height="64" rx="8" fill="none" stroke="{LINE}" stroke-width="1"/>
  <text x="24" y="40" font-family="{FONT_MONO}" font-size="22" font-weight="600" fill="{GREEN}">$</text>
  <text x="60" y="40" font-family="{FONT_MONO}" font-size="22" font-weight="500" fill="{INK}">npx skills add alchaincyf/nuwa-skill</text>
</g>

<!-- Bottom -->
<g transform="translate(96, 940)">
  <text x="0" y="0" font-family="{FONT_MONO}" font-size="14" letter-spacing="2" fill="{INK_MUTE}">▶ DISTILL HOW ANYONE THINKS</text>
</g>'''

    # Right column: 13 personas showcase
    personas = [
        ("Paul Graham", RED),
        ("张一鸣", PURPLE),
        ("Karpathy", GOLD),
        ("Ilya", CYAN),
        ("MrBeast", GREEN),
        ("特朗普", RED_D),
        ("乔布斯", PURPLE_D),
        ("马斯克", GOLD),
        ("芒格", CYAN),
        ("费曼", GREEN),
        ("纳瓦尔", RED),
        ("塔勒布", PURPLE),
        ("× 主题", INK_MUTE),
    ]
    cards_parts = []
    grid_x, grid_y = 1100, 100
    cell_w, cell_h = 220, 80
    gap = 10
    for i, (name, color) in enumerate(personas):
        col = i % 3
        row = i // 3
        x = grid_x + col * (cell_w + gap)
        y = grid_y + row * (cell_h + gap)
        cards_parts.append(
            f'<g transform="translate({x},{y})">\n'
            f'  <rect x="0" y="0" width="{cell_w}" height="{cell_h}" rx="12" fill="{BG_PANEL}" filter="url(#shadow)"/>\n'
            f'  <rect x="0" y="0" width="{cell_w}" height="{cell_h}" rx="12" fill="none" stroke="{color}" stroke-width="1.5" opacity="0.7"/>\n'
            f'  <circle cx="22" cy="40" r="6" fill="{color}"/>\n'
            f'  <text x="42" y="46" font-family="{FONT_SANS}" font-size="20" font-weight="700" fill="{INK}">{name}</text>\n'
            '</g>'
        )
    cards_xml = "\n".join(cards_parts)

    right = f'''
<!-- Right panel: personas grid -->
<g transform="translate(0, 0)">
  <text x="1100" y="62" font-family="{FONT_SANS}" font-size="14" font-weight="700" letter-spacing="3" fill="{RED}">已蒸馏 · 13 位 + 1 主题</text>
  {cards_xml}
</g>

<!-- Footer: 50+ runtimes -->
<g transform="translate(1100, 880)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="14" font-weight="700" letter-spacing="3" fill="{PURPLE}">跨 50+ RUNTIME</text>
  <text x="0" y="32" font-family="{FONT_MONO}" font-size="14" fill="{INK_DIM}">Claude Code · Codex · Cursor · OpenClaw</text>
  <text x="0" y="58" font-family="{FONT_MONO}" font-size="14" fill="{INK_DIM}">Hermes · Gemini CLI · OpenCode · ...</text>
</g>'''

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
        f'{make_defs()}\n'
        f'{make_base_bg(W, H)}\n'
        f'{left}\n'
        f'{right}\n'
        '</svg>'
    )


# ================================================================
# CARD: square  (1024 x 1024) — XHS cover
# ================================================================
def make_square():
    W, H = 1024, 1024

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
        f'{make_defs()}\n'
        f'{make_base_bg(W, H)}\n'
        f'''
<!-- Eyebrow -->
<g transform="translate(64, 80)">
  <rect x="0" y="0" width="6" height="36" fill="{RED}"/>
  <text x="22" y="18" font-family="{FONT_SANS}" font-size="14" font-weight="700" letter-spacing="3" fill="{RED}">NUWA · SKILL 造人术</text>
  <text x="22" y="34" font-family="{FONT_MONO}" font-size="11" letter-spacing="2" fill="{INK_MUTE}">22K STARS · MIT</text>
</g>

<!-- Hero -->
<g transform="translate(64, 200)">
  <text x="0" y="180" font-family="{FONT_SANS}" font-size="240" font-weight="900" fill="url(#redGrad)" letter-spacing="-8">女娲</text>
  <text x="0" y="240" font-family="{FONT_SANS}" font-size="32" font-weight="500" fill="{INK}">蒸馏任何人的思维方式</text>
</g>

<!-- Focal panel: stats -->
<g transform="translate(64, 540)">
  <rect x="0" y="0" width="896" height="220" rx="16" fill="{BG_PANEL}" filter="url(#shadow)"/>
  <rect x="0" y="0" width="896" height="220" rx="8" fill="none" stroke="{LINE}" stroke-width="1"/>

  <g transform="translate(40, 30)">
    <text x="0" y="20" font-family="{FONT_SANS}" font-size="14" font-weight="700" letter-spacing="2" fill="{RED}">6 路并行</text>
    <text x="0" y="130" font-family="{FONT_SANS}" font-size="80" font-weight="900" fill="url(#redGrad)" letter-spacing="-3">6</text>
    <text x="100" y="160" font-family="{FONT_SANS}" font-size="16" font-weight="400" fill="{INK_DIM}">Agent 调研</text>
  </g>

  <line x1="300" y1="30" x2="300" y2="190" stroke="{LINE}" stroke-width="1"/>

  <g transform="translate(320, 30)">
    <text x="0" y="20" font-family="{FONT_SANS}" font-size="14" font-weight="700" letter-spacing="2" fill="{PURPLE}">三重验证</text>
    <text x="0" y="130" font-family="{FONT_SANS}" font-size="80" font-weight="900" fill="{PURPLE}" letter-spacing="-3">3</text>
    <text x="100" y="160" font-family="{FONT_SANS}" font-size="16" font-weight="400" fill="{INK_DIM}">提炼心智模型</text>
  </g>

  <line x1="600" y1="30" x2="600" y2="190" stroke="{LINE}" stroke-width="1"/>

  <g transform="translate(620, 30)">
    <text x="0" y="20" font-family="{FONT_SANS}" font-size="14" font-weight="700" letter-spacing="2" fill="{GOLD}">13 + 1</text>
    <text x="0" y="130" font-family="{FONT_SANS}" font-size="80" font-weight="900" fill="url(#goldGrad)" letter-spacing="-3">已蒸馏</text>
    <text x="0" y="170" font-family="{FONT_SANS}" font-size="14" font-weight="400" fill="{INK_DIM}">牛人 + 主题</text>
  </g>
</g>

<!-- Install -->
<g transform="translate(64, 800)">
  <rect x="0" y="0" width="896" height="60" rx="8" fill="{BG_PANEL}" filter="url(#shadow)"/>
  <rect x="0" y="0" width="896" height="60" rx="8" fill="none" stroke="{GREEN}" stroke-width="1.5" opacity="0.6"/>
  <text x="24" y="40" font-family="{FONT_MONO}" font-size="20" font-weight="600" fill="{GREEN}">$</text>
  <text x="56" y="40" font-family="{FONT_MONO}" font-size="20" font-weight="500" fill="{INK}">npx skills add alchaincyf/nuwa-skill</text>
</g>

<!-- Bottom -->
<g transform="translate(64, 900)">
  {make_chip(0,    0, "Claude Code", RED)}
  {make_chip(160,  0, "Codex", PURPLE)}
  {make_chip(260,  0, "Cursor", GOLD)}
  {make_chip(360,  0, "OpenClaw", CYAN)}
  {make_chip(490,  0, "Hermes", GREEN)}
  {make_chip(610,  0, "50+ runtime", RED_D)}
</g>

<g transform="translate(64, 980)">
  <text x="0" y="0" font-family="{FONT_MONO}" font-size="12" letter-spacing="2" fill="{INK_MUTE}">▶ 同事.skill 之后,下一个员工何必是同事</text>
</g>
'''
        '</svg>'
    )


# ================================================================
# CARD 1: 6-agent parallel research
# ================================================================
def make_card1():
    W, H = 1024, 1024
    agents = [
        ("01", "著作", "所有书、文章、论文", RED),
        ("02", "播客访谈", "公开演讲、长访谈", PURPLE),
        ("03", "社交媒体", "推文、博客、动态", GOLD),
        ("04", "批评者视角", "他者视角与反驳", CYAN),
        ("05", "决策记录", "关键转折点", GREEN),
        ("06", "人生时间线", "成长与转折", RED_D),
    ]
    parts = []
    for i, (num, title, desc, color) in enumerate(agents):
        col = i % 2
        row = i // 2
        x = col * 448
        y = row * 168
        parts.append(
            f'<g transform="translate({x},{y})">\n'
            f'  <rect x="0" y="0" width="432" height="152" rx="12" fill="{BG_PANEL}" filter="url(#shadow)"/>\n'
            f'  <rect x="0" y="0" width="432" height="152" rx="12" fill="none" stroke="{color}" stroke-width="1.5" opacity="0.7"/>\n'
            f'  <text x="20" y="36" font-family="{FONT_MONO}" font-size="14" font-weight="700" letter-spacing="3" fill="{color}">AGENT {num}</text>\n'
            f'  <text x="20" y="80" font-family="{FONT_SANS}" font-size="32" font-weight="700" fill="{INK}">{title}</text>\n'
            f'  <text x="20" y="120" font-family="{FONT_SANS}" font-size="16" font-weight="400" fill="{INK_DIM}">{desc}</text>\n'
            '</g>'
        )
    agents_xml = "\n".join(parts)

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
        f'{make_defs()}\n'
        f'<rect width="{W}" height="{H}" fill="{BG}"/>\n'
        f'<rect width="{W}" height="{H}" fill="url(#grid)" opacity="0.3"/>\n'
        f'{make_header()}\n'
        f'''
<!-- Title -->
<g transform="translate(64, 180)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="20" font-weight="700" letter-spacing="3" fill="{RED}">CARD 01 · 调研流水线</text>
  <text x="0" y="60" font-family="{FONT_SANS}" font-size="48" font-weight="900" fill="{INK}" letter-spacing="-2">6 路 Agent 并行</text>
  <text x="0" y="110" font-family="{FONT_SANS}" font-size="28" font-weight="400" fill="{INK_DIM}">一个名字,六条信息源同时拉</text>
</g>

<!-- 6 agents grid -->
<g transform="translate(64, 360)">
  {agents_xml}
</g>

<!-- Bottom note -->
<g transform="translate(64, 940)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="16" font-weight="500" fill="{RED}">▶ 6 个 Agent 各自存档,跑完统一进提炼</text>
</g>

{make_footer(W, H, idx=1, total=4)}
'''
        '</svg>'
    )


# ================================================================
# CARD 2: 5-layer mental model extraction
# ================================================================
def make_card2():
    W, H = 1024, 1024
    layers = [
        ("L1", "怎么说话", "表达 DNA —— 语气、节奏、用词偏好", RED),
        ("L2", "怎么想",   "心智模型 · 认知框架", PURPLE),
        ("L3", "怎么判断", "决策启发式 · 直觉规则", GOLD),
        ("L4", "绝不做什么", "反模式 · 价值观底线", CYAN),
        ("L5", "知道局限", "诚实边界 · 做不到什么", GREEN),
    ]
    parts = []
    for i, (num, title, desc, color) in enumerate(layers):
        y = i * 100
        parts.append(
            f'<g transform="translate(0,{y})">\n'
            f'  <rect x="0" y="0" width="896" height="84" rx="10" fill="{BG_PANEL}" filter="url(#shadow)"/>\n'
            f'  <rect x="0" y="0" width="6" height="84" fill="{color}"/>\n'
            f'  <text x="30" y="36" font-family="{FONT_MONO}" font-size="14" font-weight="700" letter-spacing="3" fill="{color}">{num}</text>\n'
            f'  <text x="100" y="40" font-family="{FONT_SANS}" font-size="26" font-weight="700" fill="{INK}">{title}</text>\n'
            f'  <text x="100" y="68" font-family="{FONT_SANS}" font-size="16" font-weight="400" fill="{INK_DIM}">{desc}</text>\n'
            '</g>'
        )
    layers_xml = "\n".join(parts)

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
        f'{make_defs()}\n'
        f'<rect width="{W}" height="{H}" fill="{BG}"/>\n'
        f'<rect width="{W}" height="{H}" fill="url(#grid)" opacity="0.3"/>\n'
        f'{make_header()}\n'
        f'''
<!-- Title -->
<g transform="translate(64, 180)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="20" font-weight="700" letter-spacing="3" fill="{RED}">CARD 02 · 提炼方法论</text>
  <text x="0" y="60" font-family="{FONT_SANS}" font-size="48" font-weight="900" fill="{INK}" letter-spacing="-2">5 层心智模型提取</text>
  <text x="0" y="110" font-family="{FONT_SANS}" font-size="28" font-weight="400" fill="{INK_DIM}">不是语录合集,是认知操作系统</text>
</g>

<!-- 5 layers list -->
<g transform="translate(64, 360)">
  {layers_xml}
</g>

<!-- Bottom note -->
<g transform="translate(64, 920)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="16" font-weight="500" fill="{PURPLE}">▶ 3-7 个心智模型 + 5-10 条决策启发式,装进 SKILL.md</text>
  <text x="0" y="28" font-family="{FONT_SANS}" font-size="14" font-weight="400" fill="{INK_DIM}">女娲不是复制人,提取认知操作系统</text>
</g>

{make_footer(W, H, idx=2, total=4)}
'''
        '</svg>'
    )


# ================================================================
# CARD 3: 13 distilled personas
# ================================================================
def make_card3():
    W, H = 1024, 1024
    personas = [
        ("Paul Graham", "创业/写作", RED),
        ("张一鸣",      "产品/组织", PURPLE),
        ("Karpathy",    "AI/工程",   GOLD),
        ("Ilya",        "AI 安全",   CYAN),
        ("MrBeast",     "YouTube",   GREEN),
        ("特朗普",      "谈判/传播", RED_D),
        ("乔布斯",      "产品/设计", PURPLE_D),
        ("马斯克",      "工程/成本", GOLD),
        ("芒格",        "投资",     CYAN),
        ("费曼",        "学习/教学", GREEN),
        ("纳瓦尔",      "财富/杠杆", RED),
        ("塔勒布",      "反脆弱",   PURPLE),
    ]
    parts = []
    for i, (name, domain, color) in enumerate(personas):
        col = i % 3
        row = i // 3
        x = col * 296
        y = row * 110
        parts.append(
            f'<g transform="translate({x},{y})">\n'
            f'  <rect x="0" y="0" width="284" height="96" rx="10" fill="{BG_PANEL}" filter="url(#shadow)"/>\n'
            f'  <rect x="0" y="0" width="4" height="96" fill="{color}"/>\n'
            f'  <circle cx="36" cy="48" r="18" fill="{color}" opacity="0.2"/>\n'
            f'  <text x="36" y="55" text-anchor="middle" font-family="{FONT_SANS}" font-size="16" font-weight="900" fill="{color}">{name[0]}</text>\n'
            f'  <text x="72" y="42" font-family="{FONT_SANS}" font-size="20" font-weight="700" fill="{INK}">{name}</text>\n'
            f'  <text x="72" y="68" font-family="{FONT_SANS}" font-size="13" font-weight="400" fill="{INK_DIM}">{domain}</text>\n'
            '</g>'
        )
    personas_xml = "\n".join(parts)

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
        f'{make_defs()}\n'
        f'<rect width="{W}" height="{H}" fill="{BG}"/>\n'
        f'<rect width="{W}" height="{H}" fill="url(#grid)" opacity="0.3"/>\n'
        f'{make_header()}\n'
        f'''
<!-- Title -->
<g transform="translate(64, 180)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="20" font-weight="700" letter-spacing="3" fill="{RED}">CARD 03 · 已蒸馏牛人</text>
  <text x="0" y="60" font-family="{FONT_SANS}" font-size="48" font-weight="900" fill="{INK}" letter-spacing="-2">13 位 + 1 主题</text>
  <text x="0" y="110" font-family="{FONT_SANS}" font-size="28" font-weight="400" fill="{INK_DIM}">一键安装,装完就能直接调用</text>
</g>

<!-- Personas grid -->
<g transform="translate(64, 360)">
  {personas_xml}
</g>

<!-- Bottom note -->
<g transform="translate(64, 940)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="16" font-weight="500" fill="{GOLD}">▶ 想蒸不在列表里的人?对 Agent 说「蒸馏一个 XXX」即可</text>
</g>

{make_footer(W, H, idx=3, total=4)}
'''
        '</svg>'
    )


# ================================================================
# CARD 4: one-line install + 50+ runtimes
# ================================================================
def make_card4():
    W, H = 1024, 1024

    runtimes = [
        ("Claude Code", RED),
        ("Codex",       PURPLE),
        ("Cursor",      GOLD),
        ("OpenClaw",    CYAN),
        ("Hermes",      GREEN),
        ("CodeBuddy",   RED_D),
        ("Gemini CLI",  PURPLE_D),
        ("OpenCode",    GOLD),
    ]
    parts = []
    for i, (name, color) in enumerate(runtimes):
        col = i % 4
        row = i // 4
        x = col * 220
        y = row * 88
        parts.append(
            f'<g transform="translate({x},{y})">\n'
            f'  <rect x="0" y="0" width="208" height="76" rx="10" fill="{BG_PANEL}" filter="url(#shadow)"/>\n'
            f'  <rect x="0" y="0" width="208" height="76" rx="10" fill="none" stroke="{color}" stroke-width="1.5" opacity="0.7"/>\n'
            f'  <circle cx="22" cy="38" r="5" fill="{color}"/>\n'
            f'  <text x="40" y="44" font-family="{FONT_SANS}" font-size="18" font-weight="700" fill="{INK}">{name}</text>\n'
            '</g>'
        )
    runtimes_xml = "\n".join(parts)

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
        f'{make_defs()}\n'
        f'<rect width="{W}" height="{H}" fill="{BG}"/>\n'
        f'<rect width="{W}" height="{H}" fill="url(#grid)" opacity="0.3"/>\n'
        f'{make_header()}\n'
        f'''
<!-- Title -->
<g transform="translate(64, 180)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="20" font-weight="700" letter-spacing="3" fill="{RED}">CARD 04 · 一键安装</text>
  <text x="0" y="60" font-family="{FONT_SANS}" font-size="48" font-weight="900" fill="{INK}" letter-spacing="-2">一行命令,跨 50+ runtime</text>
  <text x="0" y="110" font-family="{FONT_SANS}" font-size="28" font-weight="400" fill="{INK_DIM}">自动识别你用的 Agent,放到正确目录</text>
</g>

<!-- Install command box -->
<g transform="translate(64, 360)">
  <rect x="0" y="0" width="896" height="100" rx="12" fill="{BG_PANEL}" filter="url(#shadow)"/>
  <rect x="0" y="0" width="896" height="100" rx="12" fill="none" stroke="{GREEN}" stroke-width="2" opacity="0.7"/>
  <text x="24" y="38" font-family="{FONT_MONO}" font-size="14" font-weight="700" letter-spacing="3" fill="{INK_MUTE}">INSTALL</text>
  <text x="24" y="78" font-family="{FONT_MONO}" font-size="32" font-weight="600" fill="{GREEN}">$</text>
  <text x="68" y="78" font-family="{FONT_MONO}" font-size="28" font-weight="500" fill="{INK}">npx skills add alchaincyf/nuwa-skill</text>
</g>

<!-- Or say -->
<g transform="translate(64, 500)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="16" font-weight="600" fill="{PURPLE}">或者,直接告诉你的 Agent:</text>
  <rect x="0" y="20" width="896" height="80" rx="10" fill="{BG_PANEL}" stroke="{PURPLE}" stroke-width="1" opacity="0.8"/>
  <text x="24" y="68" font-family="{FONT_MONO}" font-size="22" font-weight="500" fill="{PURPLE}">"帮我安装这个 skill: https://github.com/alchaincyf/nuwa-skill"</text>
</g>

<!-- Runtimes grid -->
<g transform="translate(64, 640)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="14" font-weight="700" letter-spacing="3" fill="{GOLD}">支持的 RUNTIME</text>
  <g transform="translate(0, 24)">
    {runtimes_xml}
  </g>
  <text x="0" y="200" font-family="{FONT_SANS}" font-size="14" font-weight="400" fill="{INK_DIM}">...以及 40+ 其他 skills-compatible runtime</text>
</g>

<!-- Bottom note -->
<g transform="translate(64, 940)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="16" font-weight="500" fill="{RED}">▶ 装完说「蒸馏一个 XXX」/「用芒格视角分析...」就能直接用</text>
</g>

{make_footer(W, H, idx=4, total=4)}
'''
        '</svg>'
    )


# ================================================================
# MAIN
# ================================================================
def save_svg(name, svg):
    svg_path = os.path.join(OUT, f"{name}.svg")
    png_path = os.path.join(OUT, f"{name}.png")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    subprocess.run(
        ["inkscape", svg_path, "--export-type=png", f"--export-filename={png_path}"],
        check=True, capture_output=True,
    )
    print(f"  -> {png_path}")


if __name__ == "__main__":
    print("Generating nuwa-skill XHS cards...")
    cards = [
        ("nuwa-banner", make_banner()),
        ("nuwa-square", make_square()),
        ("nuwa-card-1", make_card1()),
        ("nuwa-card-2", make_card2()),
        ("nuwa-card-3", make_card3()),
        ("nuwa-card-4", make_card4()),
    ]
    for name, svg in cards:
        save_svg(name, svg)
    print(f"Done! {len(cards)} cards saved to {OUT}")
