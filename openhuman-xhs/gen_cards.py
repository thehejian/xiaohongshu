#!/usr/bin/env python3
"""Generate 8 SVG cards for OpenHuman (4 light Chinese + 4 dark English).

Light cards (Chinese): cream bg #FAF7F2-#F5E8E0, deep text #1E293B
Dark cards (English):  #0B1027 radial bg, light text
"""

import os
import subprocess

OUT = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/openhuman-xhs"
os.makedirs(OUT, exist_ok=True)

# ---------- Palettes ----------
# Light
LBG1   = "#FAF7F2"
LBG2   = "#F5F0E8"
LINK   = "#1E293B"
LDIM   = "#475569"
LMUTE  = "#94A3B8"
LACCENT = "#3B82F6"
LRED   = "#DC2626"
LGREEN = "#059669"
LPURPLE = "#7C3AED"

# Dark
DBG   = "#0B1027"
DINK  = "#F1F5F9"
DDIM  = "#94A3B8"
DMUTE = "#64748B"
DRED  = "#EF4444"
DGREEN = "#22C55E"
DPURPLE = "#A855F7"
DCYAN = "#22D3EE"
DGOLD = "#F59E0B"

FONT_SANS = "PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif"
FONT_EN  = "Inter, SF Pro, Helvetica Neue, Arial, sans-serif"
FONT_MONO = "SF Mono, JetBrains Mono, IBM Plex Mono, Menlo, Consolas, monospace"


# ---------- Helpers ----------
def light_grad():
    return (
        '<linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">\n'
        f'  <stop offset="0%" stop-color="{LBG1}"/>\n'
        f'  <stop offset="100%" stop-color="{LBG2}"/>\n'
        '</linearGradient>'
    )

def dark_grad():
    return (
        '<radialGradient id="bgGrad" cx="50%" cy="50%" r="70%">\n'
        f'  <stop offset="0%" stop-color="#141B3D"/>\n'
        f'  <stop offset="100%" stop-color="{DBG}"/>\n'
        '</radialGradient>'
    )

def light_defs():
    return (
        '<defs>\n'
        f'{light_grad()}\n'
        f'<linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="100%">\n'
        f'  <stop offset="0%" stop-color="{LACCENT}"/>\n'
        f'  <stop offset="100%" stop-color="#2563EB"/>\n'
        '</linearGradient>\n'
        f'<linearGradient id="redGrad" x1="0%" y1="0%" x2="100%" y2="0%">\n'
        f'  <stop offset="0%" stop-color="{LRED}"/>\n'
        f'  <stop offset="100%" stop-color="#F87171"/>\n'
        '</linearGradient>\n'
        '</defs>'
    )

def dark_defs():
    return (
        '<defs>\n'
        f'{dark_grad()}\n'
        f'<linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="100%">\n'
        f'  <stop offset="0%" stop-color="{DPURPLE}"/>\n'
        f'  <stop offset="100%" stop-color="{DCYAN}"/>\n'
        '</linearGradient>\n'
        f'<linearGradient id="redGrad" x1="0%" y1="0%" x2="100%" y2="0%">\n'
        f'  <stop offset="0%" stop-color="{DRED}"/>\n'
        f'  <stop offset="100%" stop-color="#FCA5A5"/>\n'
        '</linearGradient>\n'
        '<filter id="glow">\n'
        '  <feGaussianBlur stdDeviation="3" result="blur"/>\n'
        '  <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>\n'
        '</filter>\n'
        '</defs>'
    )


# ================================================================
# LIGHT CARDS (Chinese)
# ================================================================

def light_base(w=1024, h=1024):
    return (
        f'<rect width="{w}" height="{h}" fill="url(#bgGrad)"/>\n'
        f'<circle cx="0" cy="0" r="300" fill="{LACCENT}" opacity="0.04"/>\n'
        f'<circle cx="{w}" cy="{h}" r="400" fill="{LRED}" opacity="0.03"/>'
    )

def light_footer(w, h, label):
    return (
        f'<g transform="translate(64,{h-40})">\n'
        f'  <text x="0" y="0" font-family="{FONT_MONO}" font-size="11" fill="{LMUTE}">{label}</text>\n'
        f'  <text x="{w-64}" y="0" text-anchor="end" font-family="{FONT_MONO}" font-size="11" fill="{LMUTE}">openhuman.ai</text>\n'
        '</g>'
    )

# --- Light Cover (Chinese) ---
def make_light_cover():
    W, H = 1024, 1024
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
        f'{light_defs()}\n'
        f'{light_base(W, H)}\n'
        f'''
<g transform="translate(64, 80)">
  <rect x="0" y="0" width="6" height="32" fill="{LACCENT}"/>
  <text x="20" y="18" font-family="{FONT_EN}" font-size="13" font-weight="700" letter-spacing="3" fill="{LACCENT}">OPENHUMAN</text>
  <text x="20" y="32" font-family="{FONT_MONO}" font-size="10" fill="{LMUTE}">WEBGL 2.0 DIGITAL HUMAN ENGINE</text>
</g>

<g transform="translate(64, 260)">
  <text x="0" y="0" font-family="{FONT_EN}" font-size="120" font-weight="900" fill="{LINK}" letter-spacing="-6">Open</text>
  <text x="0" y="130" font-family="{FONT_EN}" font-size="120" font-weight="900" fill="url(#accentGrad)" letter-spacing="-6">Human</text>
</g>

<g transform="translate(64, 580)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="40" font-weight="700" fill="{LINK}" letter-spacing="-1">纯 WebGL 2.0</text>
  <text x="0" y="52" font-family="{FONT_SANS}" font-size="32" font-weight="500" fill="{LDIM}">数字人渲染引擎</text>
</g>

<g transform="translate(64, 720)">
  <rect x="0" y="0" width="896" height="80" rx="12" fill="white" opacity="0.55"/>
  <rect x="0" y="0" width="896" height="80" rx="12" fill="none" stroke="{LACCENT}" stroke-width="1.5" opacity="0.4"/>
  <g transform="translate(40, 24)">
    <text x="0" y="0" font-family="{FONT_SANS}" font-size="14" font-weight="700" fill="{LACCENT}">零依赖</text>
    <text x="0" y="22" font-family="{FONT_SANS}" font-size="13" fill="{LDIM}">不套 Three.js / Babylon.js</text>
  </g>
  <g transform="translate(260, 24)">
    <text x="0" y="0" font-family="{FONT_SANS}" font-size="14" font-weight="700" fill="{LRED}">200KB</text>
    <text x="0" y="22" font-family="{FONT_SANS}" font-size="13" fill="{LDIM}">打包体积</text>
  </g>
  <g transform="translate(480, 24)">
    <text x="0" y="0" font-family="{FONT_SANS}" font-size="14" font-weight="700" fill="{LGREEN}">52 FACS</text>
    <text x="0" y="22" font-family="{FONT_SANS}" font-size="13" fill="{LDIM}">面部表情控制</text>
  </g>
  <g transform="translate(680, 24)">
    <text x="0" y="0" font-family="{FONT_SANS}" font-size="14" font-weight="700" fill="{LPURPLE}">WebSocket</text>
    <text x="0" y="22" font-family="{FONT_SANS}" font-size="13" fill="{LDIM}">流式动画驱动</text>
  </g>
</g>

<g transform="translate(64, 840)">
  <rect x="0" y="0" width="420" height="48" rx="8" fill="white" opacity="0.6" stroke="{LMUTE}" stroke-width="1"/>
  <text x="20" y="30" font-family="{FONT_MONO}" font-size="16" fill="{LDIM}">$ npm install @openhuman/sdk</text>
</g>

{light_footer(W, H, "CARD 01/04")}
'''
        '</svg>'
    )

# --- Light Card 1 (Chinese): 零依赖 · 200KB ---
def make_light_card1():
    W, H = 1024, 1024
    stats = [
        ("0", "运行时依赖", "纯 WebGL 2.0, 无框架锁定", LACCENT),
        ("200KB", "gzipped", "全引擎打包体积", LRED),
        ("52", "FACS 形变", "面部表情精准控制", LGREEN),
        ("60", "fps", "目标帧率, 手机 30fps", LPURPLE),
    ]
    parts = []
    for i, (val, unit, desc, color) in enumerate(stats):
        x = 64 + i * 240
        parts.append(
            f'<g transform="translate({x},380)">\n'
            f'  <rect x="0" y="0" width="208" height="220" rx="12" fill="white" opacity="0.5"/>\n'
            f'  <rect x="0" y="0" width="208" height="220" rx="12" fill="none" stroke="{color}" stroke-width="2" opacity="0.5"/>\n'
            f'  <text x="104" y="80" text-anchor="middle" font-family="{FONT_EN}" font-size="60" font-weight="900" fill="{color}">{val}</text>\n'
            f'  <text x="104" y="120" text-anchor="middle" font-family="{FONT_SANS}" font-size="18" font-weight="700" fill="{LINK}">{unit}</text>\n'
            f'  <text x="104" y="160" text-anchor="middle" font-family="{FONT_SANS}" font-size="14" fill="{LDIM}">{desc}</text>\n'
            '</g>'
        )
    stats_xml = "\n".join(parts)

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
        f'{light_defs()}\n'
        f'{light_base(W, H)}\n'
        f'''
<g transform="translate(64, 80)">
  <rect x="0" y="0" width="6" height="32" fill="{LACCENT}"/>
  <text x="20" y="18" font-family="{FONT_EN}" font-size="13" font-weight="700" letter-spacing="3" fill="{LACCENT}">OPENHUMAN</text>
  <text x="20" y="32" font-family="{FONT_MONO}" font-size="10" fill="{LMUTE}">PERFORMANCE</text>
</g>

<g transform="translate(64, 180)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="48" font-weight="900" fill="{LINK}" letter-spacing="-2">零依赖 · 极轻量</text>
  <text x="0" y="50" font-family="{FONT_SANS}" font-size="22" fill="{LDIM}">不套 Three.js, 不自建渲染管线——拿来即用</text>
</g>

<g transform="translate(64, 680)">
  <text x="0" y="0" font-family="{FONT_MONO}" font-size="14" font-weight="700" fill="{LACCENT}">支持浏览器</text>
  <g transform="translate(0, 24)">
    <rect x="0" y="0" width="896" height="60" rx="8" fill="white" opacity="0.5"/>
    <text x="20" y="38" font-family="{FONT_SANS}" font-size="16" fill="{LINK}">Chrome 60+  ·  Firefox 55+  ·  Edge 79+  ·  Safari 15+  ·  Mobile</text>
  </g>
</g>

<g transform="translate(64, 820)">
  <rect x="0" y="0" width="200" height="40" rx="20" fill="{LACCENT}" opacity="0.12"/>
  <text x="100" y="26" text-anchor="middle" font-family="{FONT_SANS}" font-size="14" font-weight="700" fill="{LACCENT}">Shadow Map</text>
  <rect x="220" y="0" width="140" height="40" rx="20" fill="{LRED}" opacity="0.12"/>
  <text x="290" y="26" text-anchor="middle" font-family="{FONT_SANS}" font-size="14" font-weight="700" fill="{LRED}">SSS 皮肤</text>
  <rect x="380" y="0" width="140" height="40" rx="20" fill="{LGREEN}" opacity="0.12"/>
  <text x="450" y="26" text-anchor="middle" font-family="{FONT_SANS}" font-size="14" font-weight="700" fill="{LGREEN}">Bloom</text>
  <rect x="540" y="0" width="120" height="40" rx="20" fill="{LPURPLE}" opacity="0.12"/>
  <text x="600" y="26" text-anchor="middle" font-family="{FONT_SANS}" font-size="14" font-weight="700" fill="{LPURPLE}">ACES</text>
</g>

{stats_xml}

{light_footer(W, H, "CARD 02/04")}
'''
        '</svg>'
    )

# --- Light Card 2 (Chinese): 一行标签嵌入 ---
def make_light_card2():
    W, H = 1024, 1024
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
        f'{light_defs()}\n'
        f'{light_base(W, H)}\n'
        f'''
<g transform="translate(64, 80)">
  <rect x="0" y="0" width="6" height="32" fill="{LACCENT}"/>
  <text x="20" y="18" font-family="{FONT_EN}" font-size="13" font-weight="700" letter-spacing="3" fill="{LACCENT}">OPENHUMAN</text>
  <text x="20" y="32" font-family="{FONT_MONO}" font-size="10" fill="{LMUTE}">WEB COMPONENT</text>
</g>

<g transform="translate(64, 180)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="48" font-weight="900" fill="{LINK}" letter-spacing="-2">一行标签嵌入</text>
  <text x="0" y="50" font-family="{FONT_SANS}" font-size="22" fill="{LDIM}">任何页面, 一个自定义元素搞定</text>
</g>

<g transform="translate(64, 360)">
  <text x="0" y="0" font-family="{FONT_EN}" font-size="14" font-weight="700" fill="{LACCENT}">EMBED</text>
  <rect x="0" y="20" width="896" height="100" rx="10" fill="white" opacity="0.5"/>
  <rect x="0" y="20" width="896" height="100" rx="10" fill="none" stroke="{LACCENT}" stroke-width="1.5" opacity="0.4"/>
  <text x="24" y="60" font-family="{FONT_MONO}" font-size="15" fill="{LINK}">&lt;script type="module" src="https://cdn.openhuman.io/sdk/latest/embed.js"&gt;&lt;/script&gt;</text>
  <text x="24" y="95" font-family="{FONT_MONO}" font-size="15" fill="{LINK}">&lt;open-human src="./char.ohb" animation="idle"&gt;&lt;/open-human&gt;</text>
</g>

<g transform="translate(64, 560)">
  <text x="0" y="0" font-family="{FONT_EN}" font-size="14" font-weight="700" fill="{LRED}">SDK</text>
  <rect x="0" y="20" width="896" height="100" rx="10" fill="white" opacity="0.5"/>
  <rect x="0" y="20" width="896" height="100" rx="10" fill="none" stroke="{LRED}" stroke-width="1.5" opacity="0.4"/>
  <text x="24" y="60" font-family="{FONT_MONO}" font-size="15" fill="{LINK}">import {{ OpenHuman }} from "@openhuman/sdk"</text>
  <text x="24" y="95" font-family="{FONT_MONO}" font-size="15" fill="{LINK}">const human = new OpenHuman({{ canvas, quality: "high" }})</text>
</g>

<g transform="translate(64, 760)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="18" font-weight="700" fill="{LGREEN}">支持属性</text>
  <g transform="translate(0, 20)">
    <rect x="0" y="0" width="280" height="36" rx="6" fill="white" opacity="0.5"/>
    <text x="16" y="24" font-family="{FONT_MONO}" font-size="13" fill="{LDIM}">src</text>
    <text x="80" y="24" font-family="{FONT_SANS}" font-size="13" fill="{LINK}">字符模型路径</text>
  </g>
  <g transform="translate(300, 20)">
    <rect x="0" y="0" width="180" height="36" rx="6" fill="white" opacity="0.5"/>
    <text x="16" y="24" font-family="{FONT_MONO}" font-size="13" fill="{LDIM}">animation</text>
    <text x="90" y="24" font-family="{FONT_SANS}" font-size="13" fill="{LINK}">初始动画</text>
  </g>
  <g transform="translate(500, 20)">
    <rect x="0" y="0" width="160" height="36" rx="6" fill="white" opacity="0.5"/>
    <text x="16" y="24" font-family="{FONT_MONO}" font-size="13" fill="{LDIM}">quality</text>
    <text x="72" y="24" font-family="{FONT_SANS}" font-size="13" fill="{LINK}">渲染质量</text>
  </g>
</g>

{light_footer(W, H, "CARD 03/04")}
'''
        '</svg>'
    )

# --- Light Card 3 (Chinese): 流式动画驱动 ---
def make_light_card3():
    W, H = 1024, 1024
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
        f'{light_defs()}\n'
        f'{light_base(W, H)}\n'
        f'''
<g transform="translate(64, 80)">
  <rect x="0" y="0" width="6" height="32" fill="{LACCENT}"/>
  <text x="20" y="18" font-family="{FONT_EN}" font-size="13" font-weight="700" letter-spacing="3" fill="{LACCENT}">OPENHUMAN</text>
  <text x="20" y="32" font-family="{FONT_MONO}" font-size="10" fill="{LMUTE}">STREAMING</text>
</g>

<g transform="translate(64, 180)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="48" font-weight="900" fill="{LINK}" letter-spacing="-2">流式动画驱动</text>
  <text x="0" y="50" font-family="{FONT_SANS}" font-size="22" fill="{LDIM}">WebSocket 实时推流, 端到端延迟 &lt;50ms</text>
</g>

<g transform="translate(64, 360)">
  <text x="0" y="0" font-family="{FONT_EN}" font-size="14" font-weight="700" fill="{LACCENT}">TTS LIP SYNC</text>
  <rect x="0" y="20" width="896" height="100" rx="10" fill="white" opacity="0.5"/>
  <rect x="0" y="20" width="896" height="100" rx="10" fill="none" stroke="{LACCENT}" stroke-width="1.5" opacity="0.4"/>
  <text x="24" y="55" font-family="{FONT_SANS}" font-size="18" font-weight="700" fill="{LINK}">TTS 文本转语音 → 自动生成唇形动画</text>
  <text x="24" y="90" font-family="{FONT_SANS}" font-size="15" fill="{LDIM}">52 FACS blendshape 实时驱动, 口型自然</text>
</g>

<g transform="translate(64, 520)">
  <rect x="0" y="20" width="896" height="100" rx="10" fill="white" opacity="0.5"/>
  <rect x="0" y="20" width="896" height="100" rx="10" fill="none" stroke="{LRED}" stroke-width="1.5" opacity="0.4"/>
  <text x="24" y="55" font-family="{FONT_SANS}" font-size="18" font-weight="700" fill="{LINK}">动作捕捉实时推流</text>
  <text x="24" y="90" font-family="{FONT_SANS}" font-size="15" fill="{LDIM}">16-bit 量化关节数据, 带宽节省 50%</text>
</g>

<g transform="translate(64, 680)">
  <text x="0" y="0" font-family="{FONT_EN}" font-size="14" font-weight="700" fill="{LPURPLE}">ANIMATION GRAPH</text>
  <rect x="0" y="20" width="896" height="80" rx="10" fill="white" opacity="0.5"/>
  <rect x="0" y="20" width="896" height="80" rx="10" fill="none" stroke="{LPURPLE}" stroke-width="1.5" opacity="0.4"/>
  <g transform="translate(24, 30)">
    <text x="0" y="0" font-family="{FONT_SANS}" font-size="16" fill="{LINK}">idle  ⇄  talk  ⇄  gesture  状态机无缝切换</text>
    <text x="0" y="30" font-family="{FONT_SANS}" font-size="14" fill="{LDIM}">自动过渡, 无需开发者管理动画状态</text>
  </g>
</g>

<g transform="translate(64, 840)">
  <rect x="0" y="0" width="896" height="72" rx="10" fill="white" opacity="0.65"/>
  <rect x="0" y="0" width="896" height="72" rx="10" fill="none" stroke="{LGREEN}" stroke-width="2" opacity="0.6"/>
  <text x="24" y="30" font-family="{FONT_MONO}" font-size="13" fill="{LMUTE}">STREAMING CLIENT</text>
  <text x="24" y="58" font-family="{FONT_MONO}" font-size="18" font-weight="600" fill="{LGREEN}">new StreamingClient({{ url: "wss://..." }})</text>
</g>

{light_footer(W, H, "CARD 04/04")}
'''
        '</svg>'
    )


# ================================================================
# DARK CARDS (English)
# ================================================================

def dark_base(w=1024, h=1024):
    return (
        f'<rect width="{w}" height="{h}" fill="url(#bgGrad)"/>\n'
        f'<circle cx="0" cy="0" r="250" fill="{DPURPLE}" opacity="0.08"/>\n'
        f'<circle cx="{w}" cy="{h}" r="350" fill="{DCYAN}" opacity="0.06"/>'
    )

def dark_footer(w, h, label):
    return (
        f'<g transform="translate(64,{h-40})">\n'
        f'  <text x="0" y="0" font-family="{FONT_MONO}" font-size="11" fill="{DMUTE}">{label}</text>\n'
        f'  <text x="{w-64}" y="0" text-anchor="end" font-family="{FONT_MONO}" font-size="11" fill="{DMUTE}">openhuman.ai</text>\n'
        '</g>'
    )

# --- Dark Cover (English) ---
def make_dark_cover():
    W, H = 1024, 1024
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
        f'{dark_defs()}\n'
        f'{dark_base(W, H)}\n'
        f'''
<g transform="translate(64, 80)">
  <rect x="0" y="0" width="6" height="32" fill="{DCYAN}"/>
  <text x="20" y="18" font-family="{FONT_EN}" font-size="13" font-weight="700" letter-spacing="3" fill="{DCYAN}">OPENHUMAN</text>
  <text x="20" y="32" font-family="{FONT_MONO}" font-size="10" fill="{DMUTE}">PURE WEBGL 2.0</text>
</g>

<g transform="translate(64, 260)">
  <text x="0" y="0" font-family="{FONT_EN}" font-size="120" font-weight="900" fill="{DINK}" letter-spacing="-6">Open</text>
  <text x="0" y="130" font-family="{FONT_EN}" font-size="120" font-weight="900" fill="url(#accentGrad)" letter-spacing="-6">Human</text>
</g>

<g transform="translate(64, 580)">
  <text x="0" y="0" font-family="{FONT_EN}" font-size="36" font-weight="700" fill="{DINK}">Pure WebGL 2.0</text>
  <text x="0" y="46" font-family="{FONT_EN}" font-size="24" font-weight="400" fill="{DDIM}">Digital Human Render Engine</text>
</g>

<g transform="translate(64, 720)">
  <rect x="0" y="0" width="896" height="80" rx="12" fill="#1E2952" opacity="0.6"/>
  <rect x="0" y="0" width="896" height="80" rx="12" fill="none" stroke="{DCYAN}" stroke-width="1" opacity="0.4"/>
  <g transform="translate(40, 24)">
    <text x="0" y="0" font-family="{FONT_EN}" font-size="13" font-weight="700" fill="{DCYAN}">Zero Deps</text>
    <text x="0" y="20" font-family="{FONT_EN}" font-size="12" fill="{DDIM}">No Three.js / Babylon.js</text>
  </g>
  <g transform="translate(260, 24)">
    <text x="0" y="0" font-family="{FONT_EN}" font-size="13" font-weight="700" fill="{DRED}">200KB</text>
    <text x="0" y="20" font-family="{FONT_EN}" font-size="12" fill="{DDIM}">Gzipped bundle</text>
  </g>
  <g transform="translate(480, 24)">
    <text x="0" y="0" font-family="{FONT_EN}" font-size="13" font-weight="700" fill="{DGREEN}">52 FACS</text>
    <text x="0" y="20" font-family="{FONT_EN}" font-size="12" fill="{DDIM}">Facial blendshapes</text>
  </g>
  <g transform="translate(680, 24)">
    <text x="0" y="0" font-family="{FONT_EN}" font-size="13" font-weight="700" fill="{DPURPLE}">Streaming</text>
    <text x="0" y="20" font-family="{FONT_EN}" font-size="12" fill="{DDIM}">WebSocket animation</text>
  </g>
</g>

<g transform="translate(64, 840)">
  <rect x="0" y="0" width="420" height="48" rx="8" fill="#1E2952" opacity="0.7" stroke="{DMUTE}" stroke-width="1"/>
  <text x="20" y="30" font-family="{FONT_MONO}" font-size="15" fill="{DGREEN}">$ npm install @openhuman/sdk</text>
</g>

{dark_footer(W, H, "CARD 01/04")}
'''
        '</svg>'
    )

# --- Dark Card 1 (English): Zero Runtime Dependencies ---
def make_dark_card1():
    W, H = 1024, 1024
    items = [
        ("ZERO", "Runtime Dependencies", "Pure WebGL 2.0, no framework lock-in", DCYAN),
        ("200KB", "Bundle Size", "Full engine gzipped", DRED),
        ("52", "FACS Morph Targets", "Precise facial expression control", DGREEN),
        ("60fps", "Target Frame Rate", "30fps+ on mobile", DPURPLE),
    ]
    parts = []
    for i, (val, title, desc, color) in enumerate(items):
        x = 64 + i * 240
        parts.append(
            f'<g transform="translate({x},380)">\n'
            f'  <rect x="0" y="0" width="208" height="220" rx="12" fill="#1E2952" opacity="0.5"/>\n'
            f'  <rect x="0" y="0" width="208" height="220" rx="12" fill="none" stroke="{color}" stroke-width="1.5" opacity="0.6"/>\n'
            f'  <text x="104" y="80" text-anchor="middle" font-family="{FONT_EN}" font-size="52" font-weight="900" fill="{color}">{val}</text>\n'
            f'  <text x="104" y="120" text-anchor="middle" font-family="{FONT_EN}" font-size="16" font-weight="700" fill="{DINK}">{title}</text>\n'
            f'  <text x="104" y="160" text-anchor="middle" font-family="{FONT_EN}" font-size="13" fill="{DDIM}">{desc}</text>\n'
            '</g>'
        )
    items_xml = "\n".join(parts)

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
        f'{dark_defs()}\n'
        f'{dark_base(W, H)}\n'
        f'''
<g transform="translate(64, 80)">
  <rect x="0" y="0" width="6" height="32" fill="{DCYAN}"/>
  <text x="20" y="18" font-family="{FONT_EN}" font-size="13" font-weight="700" letter-spacing="3" fill="{DCYAN}">OPENHUMAN</text>
  <text x="20" y="32" font-family="{FONT_MONO}" font-size="10" fill="{DMUTE}">PERFORMANCE</text>
</g>

<g transform="translate(64, 180)">
  <text x="0" y="0" font-family="{FONT_EN}" font-size="44" font-weight="900" fill="{DINK}" letter-spacing="-2">Zero Runtime Deps</text>
  <text x="0" y="48" font-family="{FONT_EN}" font-size="22" fill="{DDIM}">Everything in one &le;200KB package</text>
</g>

<g transform="translate(64, 680)">
  <text x="0" y="0" font-family="{FONT_EN}" font-size="14" font-weight="700" fill="{DCYAN}">Browser Support</text>
  <g transform="translate(0, 24)">
    <rect x="0" y="0" width="896" height="60" rx="8" fill="#1E2952" opacity="0.6"/>
    <text x="20" y="38" font-family="{FONT_EN}" font-size="15" fill="{DINK}">Chrome 60+ · Firefox 55+ · Edge 79+ · Safari 15+ · Mobile</text>
  </g>
</g>

<g transform="translate(64, 820)">
  <rect x="0" y="0" width="180" height="40" rx="20" fill="{DCYAN}" opacity="0.15"/>
  <text x="90" y="26" text-anchor="middle" font-family="{FONT_EN}" font-size="13" font-weight="700" fill="{DCYAN}">Shadow Map</text>
  <rect x="200" y="0" width="180" height="40" rx="20" fill="{DRED}" opacity="0.15"/>
  <text x="290" y="26" text-anchor="middle" font-family="{FONT_EN}" font-size="13" font-weight="700" fill="{DRED}">SSS Skin</text>
  <rect x="400" y="0" width="140" height="40" rx="20" fill="{DGREEN}" opacity="0.15"/>
  <text x="470" y="26" text-anchor="middle" font-family="{FONT_EN}" font-size="13" font-weight="700" fill="{DGREEN}">Bloom</text>
  <rect x="560" y="0" width="120" height="40" rx="20" fill="{DPURPLE}" opacity="0.15"/>
  <text x="620" y="26" text-anchor="middle" font-family="{FONT_EN}" font-size="13" font-weight="700" fill="{DPURPLE}">ACES</text>
</g>

{items_xml}

{dark_footer(W, H, "CARD 02/04")}
'''
        '</svg>'
    )

# --- Dark Card 2 (English): Web Component Ready ---
def make_dark_card2():
    W, H = 1024, 1024
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
        f'{dark_defs()}\n'
        f'{dark_base(W, H)}\n'
        f'''
<g transform="translate(64, 80)">
  <rect x="0" y="0" width="6" height="32" fill="{DCYAN}"/>
  <text x="20" y="18" font-family="{FONT_EN}" font-size="13" font-weight="700" letter-spacing="3" fill="{DCYAN}">OPENHUMAN</text>
  <text x="20" y="32" font-family="{FONT_MONO}" font-size="10" fill="{DMUTE}">WEB COMPONENT</text>
</g>

<g transform="translate(64, 180)">
  <text x="0" y="0" font-family="{FONT_EN}" font-size="44" font-weight="900" fill="{DINK}" letter-spacing="-2">Web Component Ready</text>
  <text x="0" y="48" font-family="{FONT_EN}" font-size="22" fill="{DDIM}">One HTML tag to embed a digital human</text>
</g>

<g transform="translate(64, 360)">
  <text x="0" y="0" font-family="{FONT_EN}" font-size="14" font-weight="700" fill="{DCYAN}">EMBED</text>
  <rect x="0" y="20" width="896" height="100" rx="10" fill="#1E2952" opacity="0.6"/>
  <rect x="0" y="20" width="896" height="100" rx="10" fill="none" stroke="{DCYAN}" stroke-width="1" opacity="0.5"/>
  <text x="24" y="60" font-family="{FONT_MONO}" font-size="14" fill="{DGREEN}">&lt;script type="module" src="https://cdn.openhuman.io/sdk/latest/embed.js"&gt;&lt;/script&gt;</text>
  <text x="24" y="95" font-family="{FONT_MONO}" font-size="14" fill="{DGREEN}">&lt;open-human src="./char.ohb" animation="idle"&gt;&lt;/open-human&gt;</text>
</g>

<g transform="translate(64, 540)">
  <text x="0" y="0" font-family="{FONT_EN}" font-size="14" font-weight="700" fill="{DRED}">SDK</text>
  <rect x="0" y="20" width="896" height="100" rx="10" fill="#1E2952" opacity="0.6"/>
  <rect x="0" y="20" width="896" height="100" rx="10" fill="none" stroke="{DRED}" stroke-width="1" opacity="0.5"/>
  <text x="24" y="60" font-family="{FONT_MONO}" font-size="14" fill="{DINK}">import {{ OpenHuman }} from "@openhuman/sdk"</text>
  <text x="24" y="95" font-family="{FONT_MONO}" font-size="14" fill="{DINK}">const human = new OpenHuman({{ canvas, quality: "high" }})</text>
</g>

<g transform="translate(64, 720)">
  <text x="0" y="0" font-family="{FONT_EN}" font-size="14" font-weight="700" fill="{DGREEN}">Attributes</text>
  <g transform="translate(0, 24)">
    <rect x="0" y="0" width="200" height="36" rx="6" fill="#1E2952" opacity="0.6"/>
    <text x="16" y="24" font-family="{FONT_MONO}" font-size="13" fill="{DCYAN}">src</text>
    <text x="80" y="24" font-family="{FONT_EN}" font-size="13" fill="{DDIM}">Character path</text>
  </g>
  <g transform="translate(220, 24)">
    <rect x="0" y="0" width="200" height="36" rx="6" fill="#1E2952" opacity="0.6"/>
    <text x="16" y="24" font-family="{FONT_MONO}" font-size="13" fill="{DPURPLE}">animation</text>
    <text x="100" y="24" font-family="{FONT_EN}" font-size="13" fill="{DDIM}">Initial anim</text>
  </g>
  <g transform="translate(440, 24)">
    <rect x="0" y="0" width="160" height="36" rx="6" fill="#1E2952" opacity="0.6"/>
    <text x="16" y="24" font-family="{FONT_MONO}" font-size="13" fill="{DGOLD}">quality</text>
    <text x="80" y="24" font-family="{FONT_EN}" font-size="13" fill="{DDIM}">Quality preset</text>
  </g>
</g>

{dark_footer(W, H, "CARD 03/04")}
'''
        '</svg>'
    )

# --- Dark Card 3 (English): Real-time Streaming ---
def make_dark_card3():
    W, H = 1024, 1024
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
        f'{dark_defs()}\n'
        f'{dark_base(W, H)}\n'
        f'''
<g transform="translate(64, 80)">
  <rect x="0" y="0" width="6" height="32" fill="{DCYAN}"/>
  <text x="20" y="18" font-family="{FONT_EN}" font-size="13" font-weight="700" letter-spacing="3" fill="{DCYAN}">OPENHUMAN</text>
  <text x="20" y="32" font-family="{FONT_MONO}" font-size="10" fill="{DMUTE}">STREAMING</text>
</g>

<g transform="translate(64, 180)">
  <text x="0" y="0" font-family="{FONT_EN}" font-size="44" font-weight="900" fill="{DINK}" letter-spacing="-2">Real-time Streaming</text>
  <text x="0" y="48" font-family="{FONT_EN}" font-size="22" fill="{DDIM}">WebSocket-driven animation, &lt;50ms latency</text>
</g>

<g transform="translate(64, 360)">
  <text x="0" y="0" font-family="{FONT_EN}" font-size="14" font-weight="700" fill="{DCYAN}">TTS LIP SYNC</text>
  <rect x="0" y="20" width="896" height="100" rx="10" fill="#1E2952" opacity="0.6"/>
  <rect x="0" y="20" width="896" height="100" rx="10" fill="none" stroke="{DCYAN}" stroke-width="1" opacity="0.5"/>
  <text x="24" y="55" font-family="{FONT_EN}" font-size="18" font-weight="700" fill="{DINK}">AI TTS → Automatic Lip Sync</text>
  <text x="24" y="90" font-family="{FONT_EN}" font-size="15" fill="{DDIM}">52 FACS blendshapes driven in real time</text>
</g>

<g transform="translate(64, 520)">
  <text x="0" y="0" font-family="{FONT_EN}" font-size="14" font-weight="700" fill="{DRED}">MOCAP</text>
  <rect x="0" y="20" width="896" height="100" rx="10" fill="#1E2952" opacity="0.6"/>
  <rect x="0" y="20" width="896" height="100" rx="10" fill="none" stroke="{DRED}" stroke-width="1" opacity="0.5"/>
  <text x="24" y="55" font-family="{FONT_EN}" font-size="18" font-weight="700" fill="{DINK}">MoCap Streaming</text>
  <text x="24" y="90" font-family="{FONT_EN}" font-size="15" fill="{DDIM}">16-bit quantized joint data, 50% bandwidth saving</text>
</g>

<g transform="translate(64, 680)">
  <text x="0" y="0" font-family="{FONT_EN}" font-size="14" font-weight="700" fill="{DPURPLE}">ANIMATION GRAPH</text>
  <rect x="0" y="20" width="896" height="80" rx="10" fill="#1E2952" opacity="0.6"/>
  <rect x="0" y="20" width="896" height="80" rx="10" fill="none" stroke="{DPURPLE}" stroke-width="1" opacity="0.5"/>
  <g transform="translate(24, 30)">
    <text x="0" y="0" font-family="{FONT_EN}" font-size="16" fill="{DINK}">idle  ⇄  talk  ⇄  gesture  state machine</text>
    <text x="0" y="30" font-family="{FONT_EN}" font-size="14" fill="{DDIM}">Seamless transitions, no manual state management</text>
  </g>
</g>

<g transform="translate(64, 840)">
  <rect x="0" y="0" width="896" height="72" rx="10" fill="#1E2952" opacity="0.7"/>
  <rect x="0" y="0" width="896" height="72" rx="10" fill="none" stroke="{DGREEN}" stroke-width="1.5" opacity="0.6"/>
  <text x="24" y="30" font-family="{FONT_MONO}" font-size="13" fill="{DMUTE}">STREAMING CLIENT</text>
  <text x="24" y="58" font-family="{FONT_MONO}" font-size="18" font-weight="600" fill="{DGREEN}">new StreamingClient({{ url: "wss://..." }})</text>
</g>

{dark_footer(W, H, "CARD 04/04")}
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
    print("Generating OpenHuman cards...")
    cards = [
        ("oh-cover-zh", make_light_cover()),
        ("oh-card-1-zh", make_light_card1()),
        ("oh-card-2-zh", make_light_card2()),
        ("oh-card-3-zh", make_light_card3()),
        ("oh-cover-en", make_dark_cover()),
        ("oh-card-1-en", make_dark_card1()),
        ("oh-card-2-en", make_dark_card2()),
        ("oh-card-3-en", make_dark_card3()),
    ]
    for name, svg in cards:
        save_svg(name, svg)
    print(f"Done! {len(cards)} cards saved to {OUT}")