#!/usr/bin/env python3
"""Generate 8 cards: 4 Chinese light + 4 English dark for nuwa-skill post."""
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent

# Light palette (Chinese)
CREAM = "#FAF7F2"
CREAM2 = "#F5F0E8"
WHITE = "#FFFFFF"
TEXT = "#1E293B"
TEXT_DIM = "#64748B"
TEXT_LIGHT = "#94A3B8"
RED_L = "#DC2626"
RED_LIGHT = "#FEE2E2"
PURPLE_L = "#7C3AED"
PURPLE_LIGHT = "#EDE9FE"
GOLD_L = "#F59E0B"
GOLD_LIGHT = "#FEF3C7"
CYAN_L = "#06B6D4"
CYAN_LIGHT = "#CFFAFE"
GREEN_L = "#10B981"
GREEN_LIGHT = "#D1FAE5"
BLUE_L = "#2563EB"
BLUE_LIGHT = "#DBEAFE"
ORANGE_L = "#EA580C"
ORANGE_LIGHT = "#FFEDD5"

# Dark palette (English)
DARK_BG = "#0B1027"
DARK_CARD = "#141B33"
DARK_TEXT = "#E2E8F0"
DARK_DIM = "#8892B0"
DARK_ACCENT = "#60A5FA"

CARDS = []


# ================================================================
# CHINESE CARD 1: Cover
# ================================================================
def zh_cover():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>
  <radialGradient id="bg" cx="50%" cy="40%" r="70%">
    <stop offset="0%" stop-color="#FAF7F2"/>
    <stop offset="100%" stop-color="#F0EAE0"/>
  </radialGradient>
  <linearGradient id="titleG" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#DC2626"/>
    <stop offset="50%" stop-color="#7C3AED"/>
    <stop offset="100%" stop-color="#F59E0B"/>
  </linearGradient>
  <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
    <feDropShadow dx="0" dy="6" stdDeviation="16" flood-color="#1E293B" flood-opacity="0.10"/>
  </filter>
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>
<circle cx="80" cy="80" r="120" fill="{RED_LIGHT}" opacity="0.08"/>
<circle cx="924" cy="924" r="150" fill="{PURPLE_LIGHT}" opacity="0.08"/>
<circle cx="80" cy="924" r="80" fill="{GOLD_LIGHT}" opacity="0.06"/>
<rect x="62" y="30" width="900" height="100" rx="30" fill="{WHITE}" filter="url(#shadow)"/>
<text x="512" y="90" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="700" fill="{RED_L}">让牛人的思维给你打工</text>
<text x="512" y="240" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="120" font-weight="900" fill="url(#titleG)">女娲</text>
<text x="512" y="350" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="800" fill="{TEXT}">一键蒸馏大师方法论</text>
<text x="512" y="410" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="500" fill="{TEXT_DIM}">输入名字 → 6 路 Agent 调研 → 5 层认知操作系统</text>
<g transform="translate(112, 470)">
  <rect x="0" y="0" width="800" height="430" rx="24" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="400" y="50" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{TEXT_DIM}">核心能力</text>
  <line x1="40" y1="70" x2="760" y2="70" stroke="#E2E8F0" stroke-width="1"/>
  <g transform="translate(30, 95)">
    <rect x="0" y="0" width="355" height="60" rx="12" fill="{RED_LIGHT}"/>
    <text x="177" y="38" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{RED_L}">6 路 Agent 并行调研</text>
  </g>
  <g transform="translate(415, 95)">
    <rect x="0" y="0" width="355" height="60" rx="12" fill="{PURPLE_LIGHT}"/>
    <text x="177" y="38" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{PURPLE_L}">三重验证筛选</text>
  </g>
  <g transform="translate(30, 180)">
    <rect x="0" y="0" width="355" height="60" rx="12" fill="{GOLD_LIGHT}"/>
    <text x="177" y="38" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{GOLD_L}">5 层认知操作系统</text>
  </g>
  <g transform="translate(415, 180)">
    <rect x="0" y="0" width="355" height="60" rx="12" fill="{GREEN_LIGHT}"/>
    <text x="177" y="38" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{GREEN_L}">13 位已蒸馏牛人</text>
  </g>
  <g transform="translate(30, 265)">
    <rect x="0" y="0" width="355" height="60" rx="12" fill="{BLUE_LIGHT}"/>
    <text x="177" y="38" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{BLUE_L}">50+ Runtime 兼容</text>
  </g>
  <g transform="translate(415, 265)">
    <rect x="0" y="0" width="355" height="60" rx="12" fill="{ORANGE_LIGHT}"/>
    <text x="177" y="38" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{ORANGE_L}">一键安装即用</text>
  </g>
  <rect x="200" y="350" width="400" height="52" rx="26" fill="{RED_LIGHT}" stroke="{RED_L}" stroke-width="1.5"/>
  <text x="400" y="384" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{RED_L}">22K Star · MIT 开源</text>
</g>
<text x="512" y="990" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{TEXT_DIM}">#女娲skill #AI工具 #认知升级 #Agent</text>
</svg>'''
    (ROOT / "nuwa-cover-zh.svg").write_text(svg)
    CARDS.append(("nuwa-cover-zh.svg", 1024))


# ================================================================
# CHINESE CARD 2: 6-Agent Pipeline
# ================================================================
def zh_card_1():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>
  <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#FAF7F2"/>
    <stop offset="100%" stop-color="#F5F0E8"/>
  </linearGradient>
  <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
    <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#1E293B" flood-opacity="0.08"/>
  </filter>
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>
<circle cx="100" cy="100" r="80" fill="{RED_LIGHT}" opacity="0.3"/>
<circle cx="924" cy="924" r="70" fill="{PURPLE_LIGHT}" opacity="0.3"/>
<rect x="40" y="30" width="944" height="100" rx="40" fill="{WHITE}" filter="url(#shadow)"/>
<text x="512" y="95" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="40" font-weight="900" fill="{TEXT}">输入一个名字，6 路同时开工</text>
<g transform="translate(40, 170)">
  <g transform="translate(0, 0)">
    <rect x="0" y="0" width="452" height="120" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="8" height="120" rx="4" fill="{RED_L}"/>
    <text x="30" y="50" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{RED_L}">01 · 著作</text>
    <text x="30" y="88" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" fill="{TEXT_DIM}">读遍他写的所有书和长文</text>
  </g>
  <g transform="translate(480, 0)">
    <rect x="0" y="0" width="452" height="120" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="8" height="120" rx="4" fill="{PURPLE_L}"/>
    <text x="30" y="50" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{PURPLE_L}">02 · 播客访谈</text>
    <text x="30" y="88" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" fill="{TEXT_DIM}">扒他所有公开演讲和深度对话</text>
  </g>
  <g transform="translate(0, 150)">
    <rect x="0" y="0" width="452" height="120" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="8" height="120" rx="4" fill="{GOLD_L}"/>
    <text x="30" y="50" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{GOLD_L}">03 · 社交媒体</text>
    <text x="30" y="88" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" fill="{TEXT_DIM}">翻他所有推文、微博、博客动态</text>
  </g>
  <g transform="translate(480, 150)">
    <rect x="0" y="0" width="452" height="120" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="8" height="120" rx="4" fill="{CYAN_L}"/>
    <text x="30" y="50" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{CYAN_L}">04 · 他者视角</text>
    <text x="30" y="88" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" fill="{TEXT_DIM}">找批评者是怎么评价他的</text>
  </g>
  <g transform="translate(0, 300)">
    <rect x="0" y="0" width="452" height="120" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="8" height="120" rx="4" fill="{GREEN_L}"/>
    <text x="30" y="50" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{GREEN_L}">05 · 决策记录</text>
    <text x="30" y="88" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" fill="{TEXT_DIM}">扒他做过哪些关键决策</text>
  </g>
  <g transform="translate(480, 300)">
    <rect x="0" y="0" width="452" height="120" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="8" height="120" rx="4" fill="{ORANGE_L}"/>
    <text x="30" y="50" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{ORANGE_L}">06 · 时间线</text>
    <text x="30" y="88" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" fill="{TEXT_DIM}">拉一条完整人生时间线</text>
  </g>
</g>
<g transform="translate(40, 910)">
  <rect x="0" y="0" width="944" height="60" rx="30" fill="{RED_LIGHT}" stroke="{RED_L}" stroke-width="1.5"/>
  <text x="472" y="39" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{RED_L}">6 路并进，每路存档，跑完统一进提炼</text>
</g>
<text x="512" y="1000" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="500" fill="{TEXT_LIGHT}">github.com/alchaincyf/nuwa-skill</text>
</svg>'''
    (ROOT / "nuwa-card-1-zh.svg").write_text(svg)
    CARDS.append(("nuwa-card-1-zh.svg", 1024))


# ================================================================
# CHINESE CARD 3: Triple Verification + 5-Layer OS
# ================================================================
def zh_card_2():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>
  <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#FAF7F2"/>
    <stop offset="100%" stop-color="#F5F0E8"/>
  </linearGradient>
  <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
    <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#1E293B" flood-opacity="0.08"/>
  </filter>
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>
<circle cx="80" cy="80" r="90" fill="{GREEN_LIGHT}" opacity="0.3"/>
<circle cx="924" cy="924" r="80" fill="{BLUE_LIGHT}" opacity="0.3"/>
<rect x="40" y="30" width="944" height="90" rx="35" fill="{WHITE}" filter="url(#shadow)"/>
<text x="512" y="85" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="36" font-weight="900" fill="{TEXT}">三重验证 + 五层认知操作系统</text>

<!-- Triple verification -->
<g transform="translate(40, 150)">
  <text x="0" y="0" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{RED_L}">三重验证筛选器</text>
  <g transform="translate(0, 20)">
    <rect x="0" y="0" width="280" height="70" rx="14" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="140" y="30" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="{GREEN_L}">✅ 跨 2+ 领域出现</text>
    <text x="140" y="56" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{TEXT_DIM}">不是随口一说</text>
  </g>
  <g transform="translate(310, 20)">
    <rect x="0" y="0" width="280" height="70" rx="14" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="140" y="30" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="{GREEN_L}">✅ 能预判新问题</text>
    <text x="140" y="56" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{TEXT_DIM}">有预测力</text>
  </g>
  <g transform="translate(620, 20)">
    <rect x="0" y="0" width="280" height="70" rx="14" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="140" y="30" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="{GREEN_L}">✅ 只有他这么想</text>
    <text x="140" y="56" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{TEXT_DIM}">有排他性</text>
  </g>
</g>

<!-- 3 filters result -->
<g transform="translate(40, 260)">
  <g transform="translate(0, 0)">
    <rect x="0" y="0" width="290" height="44" rx="22" fill="{GREEN_LIGHT}"/>
    <text x="145" y="29" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="{GREEN_L}">3/3 → 心智模型 ✓</text>
  </g>
  <g transform="translate(320, 0)">
    <rect x="0" y="0" width="290" height="44" rx="22" fill="{GOLD_LIGHT}"/>
    <text x="145" y="29" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="{GOLD_L}">2/3 → 观察分类</text>
  </g>
  <g transform="translate(640, 0)">
    <rect x="0" y="0" width="290" height="44" rx="22" fill="{ORANGE_LIGHT}"/>
    <text x="145" y="29" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="{ORANGE_L}">1/3 → 不入库</text>
  </g>
</g>

<!-- 5-layer OS -->
<g transform="translate(40, 340)">
  <text x="0" y="0" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{PURPLE_L}">提取为五层认知操作系统</text>
  <g transform="translate(0, 20)">
    <rect x="0" y="0" width="944" height="60" rx="12" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="10" height="60" rx="5" fill="{RED_L}"/>
    <text x="30" y="26" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">表达 DNA</text>
    <text x="30" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{TEXT_DIM}">语气、节奏、用词偏好 — 他怎么表达自己</text>
  </g>
  <g transform="translate(0, 95)">
    <rect x="0" y="0" width="944" height="60" rx="12" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="10" height="60" rx="5" fill="{PURPLE_L}"/>
    <text x="30" y="26" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">心智模型</text>
    <text x="30" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{TEXT_DIM}">3-7 个核心认知框架 — 他怎么理解世界</text>
  </g>
  <g transform="translate(0, 170)">
    <rect x="0" y="0" width="944" height="60" rx="12" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="10" height="60" rx="5" fill="{GOLD_L}"/>
    <text x="30" y="26" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">决策启发式</text>
    <text x="30" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{TEXT_DIM}">5-10 条直觉规则 — 他怎么做判断</text>
  </g>
  <g transform="translate(0, 245)">
    <rect x="0" y="0" width="457" height="60" rx="12" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="10" height="60" rx="5" fill="{CYAN_L}"/>
    <text x="30" y="26" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">反模式</text>
    <text x="30" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{TEXT_DIM}">他绝对不会做什么</text>
  </g>
  <g transform="translate(487, 245)">
    <rect x="0" y="0" width="457" height="60" rx="12" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="10" height="60" rx="5" fill="{GREEN_L}"/>
    <text x="30" y="26" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">诚实边界</text>
    <text x="30" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{TEXT_DIM}">他知道自己做不到什么</text>
  </g>
</g>

<g transform="translate(40, 700)">
  <rect x="0" y="0" width="944" height="200" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="472" y="45" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{RED_L}">不是语录合集，是可调用的认知操作系统</text>
  <line x1="40" y1="65" x2="904" y2="65" stroke="#E2E8F0" stroke-width="1"/>
  <g transform="translate(30, 85)">
    <rect x="0" y="0" width="270" height="40" rx="20" fill="{RED_LIGHT}"/>
    <text x="135" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="{RED_L}">用芒格视角看这笔投资</text>
  </g>
  <g transform="translate(320, 85)">
    <rect x="0" y="0" width="300" height="40" rx="20" fill="{PURPLE_LIGHT}"/>
    <text x="150" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="{PURPLE_L}">费曼怎么解释量子计算</text>
  </g>
  <g transform="translate(640, 85)">
    <rect x="0" y="0" width="275" height="40" rx="20" fill="{GOLD_LIGHT}"/>
    <text x="137" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="{GOLD_L}">切到纳瓦尔帮我决策</text>
  </g>
  <text x="472" y="168" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="600" fill="{TEXT_DIM}">它会以那个人的思维方式跟你聊</text>
</g>
<text x="512" y="1000" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="500" fill="{TEXT_LIGHT}">github.com/alchaincyf/nuwa-skill · 22K Star</text>
</svg>'''
    (ROOT / "nuwa-card-2-zh.svg").write_text(svg)
    CARDS.append(("nuwa-card-2-zh.svg", 1024))


# ================================================================
# CHINESE CARD 4: 13 Personas + Install
# ================================================================
def zh_card_3():
    personas = [
        ("Paul Graham", RED_L), ("张一鸣", PURPLE_L), ("Karpathy", GOLD_L),
        ("Ilya", CYAN_L), ("MrBeast", GREEN_L), ("特朗普", ORANGE_L),
        ("乔布斯", RED_L), ("马斯克", PURPLE_L), ("芒格", GOLD_L),
        ("费曼", CYAN_L), ("纳瓦尔", GREEN_L), ("塔勒布", ORANGE_L),
    ]
    parts = []
    for i, (name, color) in enumerate(personas):
        col = i % 4
        row = i // 4
        x = col * 216
        y = row * 65
        parts.append(
            f'<g transform="translate({x},{y})">\n'
            f'  <rect x="0" y="0" width="204" height="52" rx="10" fill="{WHITE}" filter="url(#shadow)"/>\n'
            f'  <rect x="0" y="0" width="4" height="52" fill="{color}"/>\n'
            f'  <circle cx="20" cy="26" r="6" fill="{color}"/>\n'
            f'  <text x="38" y="33" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="700" fill="{TEXT}">{name}</text>\n'
            f'</g>'
        )
    grid = "\n".join(parts)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>
  <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#FAF7F2"/>
    <stop offset="100%" stop-color="#F5F0E8"/>
  </linearGradient>
  <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
    <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#1E293B" flood-opacity="0.08"/>
  </filter>
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>
<circle cx="80" cy="80" r="100" fill="{GOLD_LIGHT}" opacity="0.3"/>
<circle cx="924" cy="924" r="90" fill="{BLUE_LIGHT}" opacity="0.3"/>
<rect x="40" y="30" width="944" height="90" rx="30" fill="{WHITE}" filter="url(#shadow)"/>
<text x="512" y="85" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="36" font-weight="900" fill="{TEXT}">12 位牛人 + 1 主题已蒸馏</text>
<g transform="translate(40, 150)">
  {grid}
</g>
<g transform="translate(40, 445)">
  <text x="0" y="0" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="600" fill="{TEXT_DIM}">不在列表里？直接对 Agent 说「蒸馏一个 XXX」全自动完成</text>
</g>

<g transform="translate(40, 500)">
  <rect x="0" y="0" width="944" height="380" rx="24" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="472" y="45" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="{GREEN_L}">一行命令，开箱即用</text>
  <line x1="40" y1="65" x2="904" y2="65" stroke="#E2E8F0" stroke-width="1"/>

  <g transform="translate(30, 85)">
    <rect x="0" y="0" width="884" height="80" rx="12" fill="{GREEN_LIGHT}"/>
    <text x="30" y="32" font-family="ui-monospace, SF Mono, monospace" font-size="18" font-weight="600" fill="{GREEN_L}">$ npx skills add alchaincyf/nuwa-skill</text>
    <text x="30" y="62" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{TEXT_DIM}">自动识别你用的 Agent，放到正确目录</text>
  </g>

  <g transform="translate(30, 185)">
    <rect x="0" y="0" width="210" height="40" rx="8" fill="{RED_LIGHT}"/>
    <text x="105" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="14" font-weight="700" fill="{RED_L}">Claude Code</text>
  </g>
  <g transform="translate(250, 185)">
    <rect x="0" y="0" width="150" height="40" rx="8" fill="{PURPLE_LIGHT}"/>
    <text x="75" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="14" font-weight="700" fill="{PURPLE_L}">Codex</text>
  </g>
  <g transform="translate(420, 185)">
    <rect x="0" y="0" width="150" height="40" rx="8" fill="{GOLD_LIGHT}"/>
    <text x="75" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="14" font-weight="700" fill="{GOLD_L}">Cursor</text>
  </g>
  <g transform="translate(590, 185)">
    <rect x="0" y="0" width="170" height="40" rx="8" fill="{CYAN_LIGHT}"/>
    <text x="85" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="14" font-weight="700" fill="{CYAN_L}">OpenClaw</text>
  </g>
  <g transform="translate(30, 240)">
    <rect x="0" y="0" width="150" height="40" rx="8" fill="{GREEN_LIGHT}"/>
    <text x="75" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="14" font-weight="700" fill="{GREEN_L}">Hermes</text>
  </g>
  <g transform="translate(200, 240)">
    <rect x="0" y="0" width="170" height="40" rx="8" fill="{BLUE_LIGHT}"/>
    <text x="85" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="14" font-weight="700" fill="{BLUE_L}">Gemini CLI</text>
  </g>
  <g transform="translate(390, 240)">
    <rect x="0" y="0" width="170" height="40" rx="8" fill="{ORANGE_LIGHT}"/>
    <text x="85" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="14" font-weight="700" fill="{ORANGE_L}">OpenCode</text>
  </g>
  <g transform="translate(580, 240)">
    <rect x="0" y="0" width="200" height="40" rx="8" fill="{PURPLE_LIGHT}"/>
    <text x="100" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="14" font-weight="700" fill="{PURPLE_L}">50+ runtime</text>
  </g>

  <g transform="translate(30, 310)">
    <rect x="0" y="0" width="884" height="44" rx="22" fill="{RED_LIGHT}" stroke="{RED_L}" stroke-width="1.5"/>
    <text x="442" y="29" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="{RED_L}">22K Star · MIT 开源 · 即装即用</text>
  </g>
</g>
<text x="512" y="1000" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="500" fill="{TEXT_LIGHT}">github.com/alchaincyf/nuwa-skill</text>
</svg>'''
    (ROOT / "nuwa-card-3-zh.svg").write_text(svg)
    CARDS.append(("nuwa-card-3-zh.svg", 1024))


# ================================================================
# ENGLISH CARD 1: Cover
# ================================================================
def en_cover():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>
  <radialGradient id="bg" cx="50%" cy="40%" r="75%">
    <stop offset="0%" stop-color="#141B33"/>
    <stop offset="100%" stop-color="#0B1027"/>
  </radialGradient>
  <linearGradient id="titleG" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#DC2626"/>
    <stop offset="50%" stop-color="#A855F7"/>
    <stop offset="100%" stop-color="#F59E0B"/>
  </linearGradient>
  <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
    <feDropShadow dx="0" dy="6" stdDeviation="16" flood-color="#000" flood-opacity="0.30"/>
  </filter>
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>
<circle cx="120" cy="120" r="140" fill="#1E3A5F" opacity="0.3"/>
<circle cx="880" cy="180" r="100" fill="#3B1F6E" opacity="0.3"/>
<circle cx="160" cy="880" r="110" fill="#5F1E4A" opacity="0.2"/>
<circle cx="900" cy="850" r="90" fill="#1E3A5F" opacity="0.2"/>
<rect x="62" y="40" width="900" height="100" rx="30" fill="#1A2340" filter="url(#shadow)"/>
<text x="512" y="95" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{DARK_ACCENT}">Make Any Great Mind Your AI Advisor</text>
<text x="512" y="250" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="120" font-weight="900" fill="url(#titleG)">NUWA</text>
<text x="512" y="360" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="800" fill="{DARK_TEXT}">Skill Distillery</text>
<text x="512" y="420" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="500" fill="{DARK_DIM}">One name in → 6-Agent research → Cognitive OS out</text>
<g transform="translate(112, 480)">
  <rect x="0" y="0" width="800" height="400" rx="24" fill="#1A2340" filter="url(#shadow)"/>
  <text x="400" y="45" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{DARK_DIM}">Core Capabilities</text>
  <line x1="40" y1="65" x2="760" y2="65" stroke="#2A3A5F" stroke-width="1"/>
  <g transform="translate(30, 85)">
    <rect x="0" y="0" width="355" height="55" rx="12" fill="#1E3A5F"/>
    <text x="177" y="35" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{DARK_ACCENT}">6-Agent Parallel Research</text>
  </g>
  <g transform="translate(415, 85)">
    <rect x="0" y="0" width="355" height="55" rx="12" fill="#3B1F6E"/>
    <text x="177" y="35" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="#A78BFA">Triple Verification</text>
  </g>
  <g transform="translate(30, 165)">
    <rect x="0" y="0" width="355" height="55" rx="12" fill="#1E4A3A"/>
    <text x="177" y="35" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="#34D399">5-Layer Cognitive OS</text>
  </g>
  <g transform="translate(415, 165)">
    <rect x="0" y="0" width="355" height="55" rx="12" fill="#5F1E4A"/>
    <text x="177" y="35" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="#F472B6">13 Distilled Minds</text>
  </g>
  <g transform="translate(30, 245)">
    <rect x="0" y="0" width="355" height="55" rx="12" fill="#1E3A5F"/>
    <text x="177" y="35" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{DARK_ACCENT}">50+ Runtime Compatible</text>
  </g>
  <g transform="translate(415, 245)">
    <rect x="0" y="0" width="355" height="55" rx="12" fill="#3B1F6E"/>
    <text x="177" y="35" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="#A78BFA">One-Line Install</text>
  </g>
  <rect x="200" y="330" width="400" height="48" rx="24" fill="#5F1E4A" stroke="#EC4899" stroke-width="1.5"/>
  <text x="400" y="361" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#EC4899">22K Stars · MIT Open Source</text>
</g>
<text x="512" y="990" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{DARK_DIM}">#NUWA #AIAgent #CognitiveOS #OpenSource</text>
</svg>'''
    (ROOT / "nuwa-cover-en.svg").write_text(svg)
    CARDS.append(("nuwa-cover-en.svg", 1024))


# ================================================================
# ENGLISH CARD 2: 6-Agent Pipeline
# ================================================================
def en_card_1():
    agents = [
        ("01", "Writings", "All books, essays, papers", "#DC2626", "#1E3A5F"),
        ("02", "Conversations", "Podcasts, interviews, talks", "#A855F7", "#3B1F6E"),
        ("03", "Social Media", "Tweets, blogs, short-form", "#F59E0B", "#1E4A3A"),
        ("04", "Outside Views", "Critics, reviews, observers", "#06B6D4", "#1E4A5F"),
        ("05", "Decisions", "Key choices &amp; turning points", "#10B981", "#1E4A3A"),
        ("06", "Timeline", "Life milestones &amp; evolution", "#F97316", "#5F1E4A"),
    ]
    parts = []
    for i, (num, title, desc, color, _) in enumerate(agents):
        col = i % 2
        row = i // 2
        x = col * 450
        y = row * 160
        parts.append(
            f'<g transform="translate({x},{y})">\n'
            f'  <rect x="0" y="0" width="434" height="140" rx="16" fill="#1A2340" filter="url(#shadow)"/>\n'
            f'  <rect x="0" y="0" width="8" height="140" rx="4" fill="{color}"/>\n'
            f'  <text x="30" y="40" font-family="ui-monospace, SF Mono, monospace" font-size="16" font-weight="700" fill="{color}">AGENT {num}</text>\n'
            f'  <text x="30" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="700" fill="{DARK_TEXT}">{title}</text>\n'
            f'  <text x="30" y="115" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{DARK_DIM}">{desc}</text>\n'
            f'</g>'
        )
    grid = "\n".join(parts)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>
  <radialGradient id="bg" cx="50%" cy="40%" r="75%">
    <stop offset="0%" stop-color="#141B33"/>
    <stop offset="100%" stop-color="#0B1027"/>
  </radialGradient>
  <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
    <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#000" flood-opacity="0.30"/>
  </filter>
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>
<circle cx="80" cy="80" r="100" fill="#1E3A5F" opacity="0.3"/>
<circle cx="924" cy="924" r="90" fill="#3B1F6E" opacity="0.3"/>
<rect x="40" y="30" width="944" height="90" rx="30" fill="#1A2340" filter="url(#shadow)"/>
<text x="512" y="85" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="36" font-weight="900" fill="{DARK_TEXT}">Input a Name, 6 Agents Go to Work</text>
<g transform="translate(40, 155)">
  {grid}
</g>
<g transform="translate(40, 660)">
  <rect x="0" y="0" width="944" height="60" rx="30" fill="#1E3A5F" stroke="{DARK_ACCENT}" stroke-width="1.5"/>
  <text x="472" y="39" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{DARK_ACCENT}">6 streams, each archived — then unified refinement</text>
</g>
<g transform="translate(40, 750)">
  <rect x="0" y="0" width="944" height="160" rx="20" fill="#1A2340" filter="url(#shadow)"/>
  <text x="472" y="40" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{DARK_DIM}">Then triple verification filters every insight</text>
  <line x1="40" y1="60" x2="904" y2="60" stroke="#2A3A5F" stroke-width="1"/>
  <g transform="translate(30, 80)">
    <rect x="0" y="0" width="270" height="35" rx="17" fill="#1E4A3A"/>
    <text x="135" y="24" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" font-weight="700" fill="#34D399">3/3 = Mental Model</text>
  </g>
  <g transform="translate(330, 80)">
    <rect x="0" y="0" width="270" height="35" rx="17" fill="#3B1F6E"/>
    <text x="135" y="24" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" font-weight="700" fill="#A78BFA">2/3 = Observation</text>
  </g>
  <g transform="translate(630, 80)">
    <rect x="0" y="0" width="270" height="35" rx="17" fill="#5F1E4A"/>
    <text x="135" y="24" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" font-weight="700" fill="#F472B6">1/3 = Discard</text>
  </g>
</g>
<text x="512" y="1000" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="500" fill="{DARK_DIM}">github.com/alchaincyf/nuwa-skill</text>
</svg>'''
    (ROOT / "nuwa-card-1-en.svg").write_text(svg)
    CARDS.append(("nuwa-card-1-en.svg", 1024))


# ================================================================
# ENGLISH CARD 3: Cognitive OS layers
# ================================================================
def en_card_2():
    layers = [
        ("Expression DNA", "Tone, rhythm, vocabulary preferences", "#DC2626"),
        ("Mental Models", "3-7 core cognitive frameworks", "#A855F7"),
        ("Decision Heuristics", "5-10 intuitive rules of thumb", "#F59E0B"),
        ("Anti-Patterns", "What they would never do", "#06B6D4"),
        ("Honesty Boundaries", "What they can't do", "#10B981"),
    ]
    parts = []
    for i, (title, desc, color) in enumerate(layers):
        y = i * 85
        parts.append(
            f'<g transform="translate(0,{y})">\n'
            f'  <rect x="0" y="0" width="944" height="70" rx="12" fill="#1A2340" filter="url(#shadow)"/>\n'
            f'  <rect x="0" y="0" width="10" height="70" rx="5" fill="{color}"/>\n'
            f'  <text x="30" y="30" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{DARK_TEXT}">{title}</text>\n'
            f'  <text x="30" y="56" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{DARK_DIM}">{desc}</text>\n'
            f'</g>'
        )
    grid = "\n".join(parts)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>
  <radialGradient id="bg" cx="50%" cy="40%" r="75%">
    <stop offset="0%" stop-color="#141B33"/>
    <stop offset="100%" stop-color="#0B1027"/>
  </radialGradient>
  <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
    <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#000" flood-opacity="0.30"/>
  </filter>
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>
<circle cx="80" cy="80" r="100" fill="#1E3A5F" opacity="0.3"/>
<circle cx="924" cy="924" r="90" fill="#3B1F6E" opacity="0.3"/>
<rect x="40" y="30" width="944" height="90" rx="30" fill="#1A2340" filter="url(#shadow)"/>
<text x="512" y="85" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="36" font-weight="900" fill="{DARK_TEXT}">Extract a 5-Layer Cognitive OS</text>
<g transform="translate(40, 155)">
<text x="0" y="0" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="600" fill="{DARK_DIM}">Not a quote collection — a runnable operating system</text>
  <g transform="translate(0, 30)">
    {grid}
  </g>
</g>
<g transform="translate(40, 635)">
  <rect x="0" y="0" width="944" height="280" rx="20" fill="#1A2340" filter="url(#shadow)"/>
  <text x="472" y="40" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{DARK_ACCENT}">Works with any AI Agent</text>
  <line x1="40" y1="65" x2="904" y2="65" stroke="#2A3A5F" stroke-width="1"/>
  <g transform="translate(30, 85)">
    <rect x="0" y="0" width="200" height="40" rx="8" fill="#1E3A5F"/>
    <text x="100" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="{DARK_ACCENT}">Claude Code</text>
  </g>
  <g transform="translate(250, 85)">
    <rect x="0" y="0" width="140" height="40" rx="8" fill="#3B1F6E"/>
    <text x="70" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#A78BFA">Codex</text>
  </g>
  <g transform="translate(410, 85)">
    <rect x="0" y="0" width="140" height="40" rx="8" fill="#1E4A3A"/>
    <text x="70" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#34D399">Cursor</text>
  </g>
  <g transform="translate(570, 85)">
    <rect x="0" y="0" width="170" height="40" rx="8" fill="#3B1F6E"/>
    <text x="85" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#A78BFA">OpenClaw</text>
  </g>
  <g transform="translate(30, 140)">
    <rect x="0" y="0" width="140" height="40" rx="8" fill="#5F1E4A"/>
    <text x="70" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#F472B6">Hermes</text>
  </g>
  <g transform="translate(190, 140)">
    <rect x="0" y="0" width="160" height="40" rx="8" fill="#1E3A5F"/>
    <text x="80" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="{DARK_ACCENT}">Gemini CLI</text>
  </g>
  <g transform="translate(370, 140)">
    <rect x="0" y="0" width="160" height="40" rx="8" fill="#3B1F6E"/>
    <text x="80" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#A78BFA">OpenCode</text>
  </g>
  <g transform="translate(550, 140)">
    <rect x="0" y="0" width="180" height="40" rx="8" fill="#1E4A3A"/>
    <text x="90" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#34D399">40+ more</text>
  </g>
  <rect x="200" y="210" width="544" height="44" rx="22" fill="#5F1E4A" stroke="#EC4899" stroke-width="1.5"/>
  <text x="472" y="239" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="#EC4899">One Install. 50+ Runtimes. Any Great Mind.</text>
</g>
<text x="512" y="1000" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="500" fill="{DARK_DIM}">github.com/alchaincyf/nuwa-skill</text>
</svg>'''
    (ROOT / "nuwa-card-2-en.svg").write_text(svg)
    CARDS.append(("nuwa-card-2-en.svg", 1024))


# ================================================================
# ENGLISH CARD 4: Personas + Install
# ================================================================
def en_card_3():
    personas = [
        ("Paul Graham", "#DC2626"), ("Zhang Yiming", "#A855F7"),
        ("Karpathy", "#F59E0B"), ("Ilya Sutskever", "#06B6D4"),
        ("MrBeast", "#10B981"), ("Donald Trump", "#F97316"),
        ("Steve Jobs", "#DC2626"), ("Elon Musk", "#A855F7"),
        ("Charlie Munger", "#F59E0B"), ("Richard Feynman", "#06B6D4"),
        ("Naval Ravikant", "#10B981"), ("Nassim Taleb", "#F97316"),
    ]
    parts = []
    for i, (name, color) in enumerate(personas):
        col = i % 4
        row = i // 4
        x = col * 216
        y = row * 65
        parts.append(
            f'<g transform="translate({x},{y})">\n'
            f'  <rect x="0" y="0" width="204" height="52" rx="10" fill="#1A2340" filter="url(#shadow)"/>\n'
            f'  <rect x="0" y="0" width="4" height="52" fill="{color}"/>\n'
            f'  <circle cx="20" cy="26" r="6" fill="{color}"/>\n'
            f'  <text x="38" y="33" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="{DARK_TEXT}">{name}</text>\n'
            f'</g>'
        )
    grid = "\n".join(parts)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>
  <radialGradient id="bg" cx="50%" cy="40%" r="75%">
    <stop offset="0%" stop-color="#141B33"/>
    <stop offset="100%" stop-color="#0B1027"/>
  </radialGradient>
  <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
    <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#000" flood-opacity="0.30"/>
  </filter>
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>
<circle cx="80" cy="80" r="100" fill="#1E3A5F" opacity="0.3"/>
<circle cx="924" cy="924" r="90" fill="#3B1F6E" opacity="0.3"/>
<rect x="40" y="30" width="944" height="90" rx="30" fill="#1A2340" filter="url(#shadow)"/>
<text x="512" y="85" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="36" font-weight="900" fill="{DARK_TEXT}">12 Minds + 1 Theme Ready</text>
<g transform="translate(40, 150)">
  {grid}
</g>
<g transform="translate(40, 425)">
  <text x="0" y="0" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{DARK_DIM}">Not on the list? Tell your Agent "distill someone" — it just works.</text>
</g>

<g transform="translate(40, 470)">
  <rect x="0" y="0" width="944" height="420" rx="24" fill="#1A2340" filter="url(#shadow)"/>
  <text x="472" y="45" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="#34D399">One-Line Install, Zero Config</text>
  <line x1="40" y1="65" x2="904" y2="65" stroke="#2A3A5F" stroke-width="1"/>

  <g transform="translate(30, 85)">
    <rect x="0" y="0" width="884" height="80" rx="12" fill="#1E4A3A"/>
    <text x="30" y="34" font-family="ui-monospace, SF Mono, monospace" font-size="20" font-weight="600" fill="#34D399">$ npx skills add alchaincyf/nuwa-skill</text>
    <text x="30" y="64" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{DARK_DIM}">Auto-detects your Agent, saves to the right directory</text>
  </g>

  <g transform="translate(30, 185)">
    <text x="0" y="0" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="700" fill="{DARK_DIM}">Just ask your Agent:</text>
  </g>
  <g transform="translate(30, 215)">
    <rect x="0" y="0" width="450" height="40" rx="10" fill="#1E3A5F"/>
    <text x="225" y="28" text-anchor="middle" font-family="ui-monospace, SF Mono, monospace" font-size="16" font-weight="500" fill="{DARK_ACCENT}">"install alchaincyf/nuwa-skill"</text>
  </g>
  <g transform="translate(500, 215)">
    <rect x="0" y="0" width="414" height="40" rx="10" fill="#3B1F6E"/>
    <text x="207" y="28" text-anchor="middle" font-family="ui-monospace, SF Mono, monospace" font-size="16" font-weight="500" fill="#A78BFA">"distill Steve Jobs"</text>
  </g>

  <g transform="translate(30, 275)">
    <rect x="0" y="0" width="884" height="50" rx="25" fill="#5F1E4A" stroke="#EC4899" stroke-width="1.5"/>
    <text x="442" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="#EC4899">Ask it questions in any great mind's voice</text>
  </g>

  <g transform="translate(30, 345)">
    <text x="0" y="0" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{DARK_DIM}">">Use Munger's lens on this investment"</text>
    <text x="0" y="35" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{DARK_DIM}">">How would Feynman explain quantum computing?"</text>
    <text x="0" y="70" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{DARK_DIM}">">Switch to Naval, I'm torn between 3 choices"</text>
  </g>
</g>

<text x="512" y="1000" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="500" fill="{DARK_DIM}">22K Stars · MIT · github.com/alchaincyf/nuwa-skill</text>
</svg>'''
    (ROOT / "nuwa-card-3-en.svg").write_text(svg)
    CARDS.append(("nuwa-card-3-en.svg", 1024))


# ================================================================
# MAIN
# ================================================================
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
