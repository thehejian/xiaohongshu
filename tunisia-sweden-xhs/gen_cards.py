#!/usr/bin/env python3
"""Redesigned gen_cards.py for Tunisia 1-5 Sweden — professional light-mode cards"""
import subprocess, os

OUT = "output"
os.makedirs(OUT, exist_ok=True)

# ── Light Palette ──
CREAM = "#FAF7F2"
CREAM2 = "#F5F0E8"
WHITE = "#FFFFFF"
TEXT = "#1E293B"
TEXT_DIM = "#64748B"
TEXT_LIGHT = "#94A3B8"
RED = "#DC2626"
RED_LIGHT = "#FEE2E2"
GOLD = "#F59E0B"
GOLD_LIGHT = "#FEF3C7"
GREEN = "#10B981"
GREEN_LIGHT = "#D1FAE5"
GRAY = "#94A3B8"
GRAY_LIGHT = "#F1F5F9"

def save_svg(name, svg):
    svg_path = os.path.join(OUT, f"{name}.svg")
    png_path = os.path.join(OUT, f"{name}.png")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    subprocess.run(
        ["inkscape", svg_path, "--export-type=png", f"--export-filename={png_path}",
         "-w", "1024", "-h", "1024"],
        check=True, capture_output=True,
    )

def shadow():
    return ('<filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">'
            '<feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="#1E293B" flood-opacity="0.08"/>'
            '</filter>')

def bg_circles():
    return f'''<circle cx="80" cy="80" r="140" fill="{RED_LIGHT}" opacity="0.15"/>
<circle cx="924" cy="924" r="180" fill="{GOLD_LIGHT}" opacity="0.12"/>
<circle cx="80" cy="924" r="80" fill="{GREEN_LIGHT}" opacity="0.1"/>
<circle cx="924" cy="80" r="60" fill="{RED_LIGHT}" opacity="0.08"/>'''

def page_footer(y=960, hashtag=""):
    return f'''<line x1="80" y1="{y}" x2="944" y2="{y}" stroke="#E2E8F0" stroke-width="1"/>
<text x="512" y="{y+30}" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_LIGHT}">{hashtag}</text>'''

# ── CARD 1: Cover ──
def card_cover():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>
  <radialGradient id="bg" cx="50%" cy="40%" r="70%">
    <stop offset="0%" stop-color="{CREAM}"/>
    <stop offset="100%" stop-color="{CREAM2}"/>
  </radialGradient>
  <linearGradient id="titleG" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#DC2626"/>
    <stop offset="50%" stop-color="#EF4444"/>
    <stop offset="100%" stop-color="#DC2626"/>
  </linearGradient>
  {shadow()}
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>
{bg_circles()}
<rect x="62" y="40" width="900" height="80" rx="40" fill="{WHITE}" filter="url(#shadow)"/>
<text x="512" y="90" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="24" font-weight="700" fill="{RED}">⚽ 2026世界杯 · F组首轮</text>

<text x="512" y="240" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="100" font-weight="900" fill="url(#titleG)">5-1</text>
<text x="512" y="310" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="28" font-weight="600" fill="{TEXT_DIM}">瑞典 vs 突尼斯</text>

<rect x="262" y="350" width="500" height="60" rx="30" fill="{RED_LIGHT}" stroke="{RED}" stroke-width="1.5"/>
<text x="512" y="389" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="28" font-weight="800" fill="{RED}">主教练拉穆希 · 一场下课</text>

<text x="512" y="460" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" fill="{TEXT_DIM}">世界杯史上第4位赛中遭解雇的主帅</text>
<text x="512" y="500" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" fill="{TEXT_LIGHT}">前面3位都在1998年 · 拉老师一把拉回2026</text>

<rect x="312" y="560" width="400" height="50" rx="25" fill="{RED}"/>
<text x="512" y="593" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="#FFF">下翻 → 到底有多惨</text>

<rect x="62" y="680" width="900" height="200" rx="24" fill="{WHITE}" filter="url(#shadow)"/>
<g transform="translate(82, 700)">
  <rect x="0" y="0" width="860" height="60" rx="12" fill="{RED_LIGHT}"/>
  <text x="430" y="38" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="{RED}">赛前热身：比利时 5-0 突尼斯</text>
  <text x="430" y="80" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">正赛：瑞典 5-1 突尼斯 → 两场丢10球</text>
  <text x="430" y="116" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">前5场执教：1胜4负，唯一赢的是海地</text>
  <text x="430" y="152" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="16" fill="{TEXT_LIGHT}">拉穆希（赛前）：没事，热热身而已 → 赛后：（沉默）</text>
</g>
{page_footer(960, "#突尼斯 #世界杯 #2026世界杯 #足球 #瑞典 #足坛趣闻 #教练下课")}
</svg>'''

# ── CARD 2: Stats Timeline ──
def card_stats():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>
  <radialGradient id="bg" cx="50%" cy="40%" r="70%">
    <stop offset="0%" stop-color="{CREAM}"/>
    <stop offset="100%" stop-color="{CREAM2}"/>
  </radialGradient>
  {shadow()}
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>
<circle cx="80" cy="80" r="90" fill="{RED_LIGHT}" opacity="0.2"/>
<circle cx="924" cy="924" r="100" fill="{GOLD_LIGHT}" opacity="0.15"/>

<rect x="62" y="30" width="900" height="80" rx="35" fill="{WHITE}" filter="url(#shadow)"/>
<text x="512" y="80" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="30" font-weight="800" fill="{TEXT}">📊 崩溃时间线 · 数字不会骗人</text>

<g transform="translate(62, 140)">
  <rect x="0" y="0" width="900" height="130" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="{TEXT_LIGHT}"/>
  <text x="30" y="45" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" font-weight="600" fill="{TEXT_LIGHT}">热身赛 · 赛前10天</text>
  <text x="30" y="85" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="40" font-weight="900" fill="{TEXT_DIM}">比利时 5-0 突尼斯</text>
  <text x="30" y="115" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">拉穆希：没事没事，热身而已，战术还在磨合</text>
</g>

<g transform="translate(62, 300)">
  <rect x="0" y="0" width="900" height="130" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="{RED}"/>
  <text x="30" y="45" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" font-weight="600" fill="{RED}">正赛 · 2026世界杯F组首轮</text>
  <text x="30" y="85" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="40" font-weight="900" fill="{RED}">瑞典 5-1 突尼斯</text>
  <text x="30" y="115" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">拉穆希：……（说都不会话了）</text>
</g>

<rect x="62" y="470" width="900" height="80" rx="20" fill="{RED_LIGHT}" stroke="{RED}" stroke-width="1.5" stroke-dasharray="6,3"/>
<text x="512" y="505" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="24" font-weight="800" fill="{RED}">两场统计：10球丢失  1次下课</text>
<text x="512" y="535" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">效率之高，令人叹为观止</text>

<g transform="translate(62, 580)">
  <rect x="0" y="0" width="900" height="200" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="30" y="40" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">世界杯历史上赛中解雇的主帅</text>
  <text x="30" y="80" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">1998 · 沙特 · 佩雷拉（2场后）</text>
  <text x="30" y="115" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">1998 · 韩国 · 车范根（2场后）</text>
  <text x="30" y="150" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">1998 · 突尼斯 · 卡斯佩尔恰克（2场后）</text>
  <text x="30" y="185" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" font-weight="700" fill="{RED}">2026 · 突尼斯 · 拉穆希（1场后）← 新纪录</text>
</g>
{page_footer(960, "#世界杯历史 #下课纪录 #突尼斯 #瑞典 #足坛趣闻")}
</svg>'''

# ── CARD 3: Son Drama ──
def card_son():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>
  <radialGradient id="bg" cx="50%" cy="40%" r="70%">
    <stop offset="0%" stop-color="{CREAM}"/>
    <stop offset="100%" stop-color="{CREAM2}"/>
  </radialGradient>
  {shadow()}
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>
<circle cx="80" cy="80" r="80" fill="{GOLD_LIGHT}" opacity="0.2"/>
<circle cx="924" cy="924" r="120" fill="{RED_LIGHT}" opacity="0.15"/>

<rect x="62" y="30" width="900" height="80" rx="35" fill="{WHITE}" filter="url(#shadow)"/>
<text x="512" y="80" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="30" font-weight="800" fill="{TEXT}">🎭 赛后发布会 · 年度迷惑剧情</text>

<!-- Reporter Q -->
<g transform="translate(62, 150)">
  <rect x="0" y="0" width="520" height="65" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="30" y="28" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" font-weight="600" fill="{TEXT_DIM}">📰 记者</text>
  <text x="30" y="52" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" fill="{TEXT}">为什么你儿子在酒店跟球迷打架？</text>
</g>

<!-- Lamouchi A -->
<g transform="translate(420, 245)">
  <rect x="0" y="0" width="542" height="65" rx="16" fill="{RED_LIGHT}" stroke="{RED}" stroke-width="1"/>
  <text x="512" y="28" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" font-weight="600" fill="{RED}">🎙️ 拉穆希</text>
  <text x="512" y="52" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="600" fill="{RED}">他是在写毕业论文！跟球队无关！</text>
</g>

<!-- Reporter Q2 -->
<g transform="translate(62, 340)">
  <rect x="0" y="0" width="450" height="65" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="30" y="28" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" font-weight="600" fill="{TEXT_DIM}">📰 记者</text>
  <text x="30" y="52" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" fill="{TEXT}">论文写完了吗？他在队里什么职务？</text>
</g>

<!-- Lamouchi A2 -->
<g transform="translate(320, 435)">
  <rect x="0" y="0" width="642" height="65" rx="16" fill="{RED_LIGHT}" stroke="{RED}" stroke-width="1"/>
  <text x="622" y="28" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" font-weight="600" fill="{RED}">🎙️ 拉穆希</text>
  <text x="622" y="52" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="600" fill="{RED}">没有职务！不参与选拔！关你啥事！！！</text>
</g>

<!-- Reporter Q3 -->
<g transform="translate(62, 530)">
  <rect x="0" y="0" width="380" height="65" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="30" y="28" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" font-weight="600" fill="{TEXT_DIM}">📰 记者</text>
  <text x="30" y="52" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" fill="{TEXT}">为什么打人？</text>
</g>

<!-- Lamouchi A3 - big anger -->
<g transform="translate(260, 625)">
  <rect x="0" y="0" width="702" height="80" rx="16" fill="{RED}" filter="url(#shadow)"/>
  <text x="682" y="35" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" font-weight="800" fill="#FFF">🎙️ 拉穆希</text>
  <text x="682" y="65" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" font-weight="700" fill="#FFF">关 你 啥 事 ！ ！ ！</text>
</g>

<rect x="62" y="750" width="900" height="70" rx="20" fill="{GOLD_LIGHT}" stroke="{GOLD}" stroke-width="1.5"/>
<text x="512" y="785" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" font-weight="800" fill="{GOLD}">论文还没交，爹的工作先交了 💀</text>
<text x="512" y="815" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">世界杯年度最离谱剧情，没有之一</text>

<rect x="312" y="870" width="400" height="50" rx="25" fill="{RED}"/>
<text x="512" y="903" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="#FFF">下翻 → 后面怎么走</text>
{page_footer(960, "#突尼斯 #世界杯迷惑行为 #足球段子 #教练下课")}
</svg>'''

# ── CARD 4: End ──
def card_end():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>
  <radialGradient id="bg" cx="50%" cy="40%" r="70%">
    <stop offset="0%" stop-color="{CREAM}"/>
    <stop offset="100%" stop-color="{CREAM2}"/>
  </radialGradient>
  {shadow()}
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>
<circle cx="80" cy="80" r="100" fill="{RED_LIGHT}" opacity="0.15"/>
<circle cx="924" cy="924" r="130" fill="{GOLD_LIGHT}" opacity="0.12"/>

<rect x="62" y="30" width="900" height="80" rx="35" fill="{WHITE}" filter="url(#shadow)"/>
<text x="512" y="80" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="30" font-weight="800" fill="{TEXT}">🚨 F组死亡之榜 · 出线形势</text>

<rect x="62" y="140" width="900" height="350" rx="24" fill="{WHITE}" filter="url(#shadow)"/>

<g transform="translate(82, 160)">
  <rect x="0" y="0" width="860" height="55" rx="12" fill="{GRAY_LIGHT}"/>
  <text x="20" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">排名</text>
  <text x="200" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">球队</text>
  <text x="500" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">赛果</text>
  <text x="740" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">状态</text>
</g>

<g transform="translate(82, 230)">
  <text x="20" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" font-weight="800" fill="{GREEN}">1</text>
  <text x="200" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" font-weight="700" fill="{TEXT}">瑞典</text>
  <text x="500" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" fill="{TEXT_DIM}">5-1 胜突尼斯</text>
  <rect x="720" y="10" width="80" height="28" rx="14" fill="{GREEN_LIGHT}"/>
  <text x="760" y="30" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="16" font-weight="700" fill="{GREEN}">出线在望</text>
</g>

<g transform="translate(82, 290)">
  <text x="20" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" font-weight="800" fill="{GOLD}">2</text>
  <text x="200" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" font-weight="700" fill="{TEXT}">日本</text>
  <text x="500" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" fill="{TEXT_DIM}">2-2 平荷兰</text>
  <rect x="720" y="10" width="80" height="28" rx="14" fill="{GOLD_LIGHT}"/>
  <text x="760" y="30" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="16" font-weight="700" fill="{GOLD}">还有机会</text>
</g>

<g transform="translate(82, 350)">
  <text x="20" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" font-weight="800" fill="{GOLD}">3</text>
  <text x="200" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" font-weight="700" fill="{TEXT}">荷兰</text>
  <text x="500" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" fill="{TEXT_DIM}">2-2 平日本</text>
  <rect x="720" y="10" width="80" height="28" rx="14" fill="{GOLD_LIGHT}"/>
  <text x="760" y="30" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="16" font-weight="700" fill="{GOLD}">还有机会</text>
</g>

<g transform="translate(82, 410)">
  <text x="20" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" font-weight="800" fill="{RED}">4</text>
  <text x="200" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" font-weight="700" fill="{TEXT}">突尼斯</text>
  <text x="500" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" fill="{TEXT_DIM}">1-5 负瑞典</text>
  <rect x="720" y="10" width="100" height="28" rx="14" fill="{RED_LIGHT}"/>
  <text x="770" y="30" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="16" font-weight="700" fill="{RED}">基本告别</text>
</g>

<!-- Next matches -->
<g transform="translate(62, 530)">
  <rect x="0" y="0" width="900" height="100" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="30" y="40" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">剩余赛程</text>
  <text x="30" y="75" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">第2场：日本 vs 突尼斯（⚔️ 背水一战）</text>
  <text x="560" y="75" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">第3场：荷兰 vs 突尼斯（💀 凶多吉少）</text>
</g>

<rect x="62" y="670" width="900" height="70" rx="20" fill="{RED_LIGHT}" stroke="{RED}" stroke-width="1.5" stroke-dasharray="6,3"/>
<text x="512" y="705" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="26" font-weight="800" fill="{RED}">晋级希望：一行白鹭上青天</text>
<text x="512" y="735" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">——远走高飞，明年再来 🛫</text>

<rect x="312" y="800" width="400" height="50" rx="25" fill="{RED}"/>
<text x="512" y="833" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="#FFF">关注我 · 看更多世界杯名场面</text>

<text x="512" y="920" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" fill="{TEXT_DIM}">❤️ 点赞  ⭐ 收藏  🔄 转发</text>
{page_footer(960, "#突尼斯 #世界杯 #2026世界杯 #死亡之组 #足球段子")}
</svg>'''

if __name__ == "__main__":
    print("Generating v3 cards (professional light mode)...")
    for name, fn in [
        ("01-cover", card_cover),
        ("02-stats", card_stats),
        ("03-son", card_son),
        ("04-end", card_end),
    ]:
        svg = fn()
        save_svg(name, svg)
        print(f"  ✓ {name}")
    print("Done! 4 cards in output/")
