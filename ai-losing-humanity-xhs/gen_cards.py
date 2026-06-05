import subprocess, pathlib

HERE = pathlib.Path(__file__).parent

FG = "#1E293B"
RED = "#DC2626"
GREEN = "#059669"
BLUE = "#2563EB"
PURPLE = "#7C3AED"

BG_LIGHT = """<linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#FAF7F2"/><stop offset="100%" stop-color="#F5F0E8"/>
</linearGradient>"""

BG_DARK = """<radialGradient id="bg" cx="50%" cy="50%" r="70%">
    <stop offset="0%" stop-color="#141C3A"/><stop offset="100%" stop-color="#0B1027"/>
</radialGradient>"""

PINGFANG = "PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif"
MONO = "SF Mono, JetBrains Mono, IBM Plex Mono, Menlo, Consolas, monospace"

LIGHT_ACCENT_RED = """<linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#DC2626"/><stop offset="100%" stop-color="#EA580C"/>
</linearGradient>"""

LIGHT_ACCENT_GREEN = """<linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#059669"/><stop offset="100%" stop-color="#10B981"/>
</linearGradient>"""

LIGHT_ACCENT_BLUE = """<linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#2563EB"/><stop offset="100%" stop-color="#3B82F6"/>
</linearGradient>"""

LIGHT_ACCENT_PURPLE = """<linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#7C3AED"/><stop offset="100%" stop-color="#8B5CF6"/>
</linearGradient>"""

DARK_ACCENT_BLUE = """<linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#93C5FD"/><stop offset="100%" stop-color="#60A5FA"/>
</linearGradient>"""

DARK_ACCENT_GREEN = """<linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#6EE7B7"/><stop offset="100%" stop-color="#34D399"/>
</linearGradient>"""

DARK_ACCENT_PURPLE = """<linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#C4B5FD"/><stop offset="100%" stop-color="#A78BFA"/>
</linearGradient>"""

DARK_ACCENT_RED = """<linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#FCA5A5"/><stop offset="100%" stop-color="#F87171"/>
</linearGradient>"""

def svg_head(bg_def, extra_defs=""):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>{bg_def}{extra_defs}</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>"""

def card_cn_cover():
    return svg_head(BG_LIGHT, LIGHT_ACCENT_RED) + f"""
<text x="80" y="300" font-family="{PINGFANG}" font-size="140" font-weight="900" fill="{FG}" letter-spacing="-4">AI正在偷走</text>
<text x="80" y="480" font-family="{PINGFANG}" font-size="140" font-weight="900" fill="url(#accent)" letter-spacing="-4">你的人性</text>
<rect x="80" y="540" width="80" height="4" rx="2" fill="{RED}" opacity=".5"/>
<text x="80" y="610" font-family="{PINGFANG}" font-size="36" font-weight="700" fill="{FG}">前Meta产品经理 深度反思</text>
<text x="80" y="670" font-family="{PINGFANG}" font-size="28" font-weight="500" fill="{FG}">情绪扁平化 · AI支配作息 · 多线程耗竭</text>
</svg>"""

def card_cn_flatten():
    return svg_head(BG_LIGHT, LIGHT_ACCENT_BLUE) + f"""
<text x="80" y="280" font-family="{PINGFANG}" font-size="120" font-weight="900" fill="url(#accent)" letter-spacing="-3">情绪</text>
<text x="80" y="440" font-family="{PINGFANG}" font-size="120" font-weight="900" fill="url(#accent)" letter-spacing="-3">扁平化</text>
<rect x="80" y="500" width="80" height="4" rx="2" fill="{BLUE}" opacity=".5"/>
<text x="80" y="580" font-family="{PINGFANG}" font-size="34" font-weight="700" fill="{FG}">你正在模仿AI的冷漠理性</text>
<text x="80" y="650" font-family="{PINGFANG}" font-size="26" font-weight="500" fill="{FG}">不再愤怒 · 不再激动 · 不再难过</text>
<text x="80" y="720" font-family="{PINGFANG}" font-size="28" font-weight="900" fill="{RED}">是AI把你的情绪抹平了</text>
</svg>"""

def card_cn_schedule():
    return svg_head(BG_LIGHT, LIGHT_ACCENT_GREEN) + f"""
<text x="80" y="280" font-family="{PINGFANG}" font-size="120" font-weight="900" fill="url(#accent)" letter-spacing="-3">AI支配</text>
<text x="80" y="430" font-family="{PINGFANG}" font-size="120" font-weight="900" fill="url(#accent)" letter-spacing="-3">你的作息</text>
<rect x="80" y="490" width="80" height="4" rx="2" fill="{GREEN}" opacity=".5"/>
<text x="80" y="570" font-family="{PINGFANG}" font-size="34" font-weight="700" fill="{FG}">凌晨2点的日报不是自由</text>
<text x="80" y="650" font-family="{PINGFANG}" font-size="44" font-weight="900" fill="{RED}">是牢笼</text>
<text x="80" y="720" font-family="{PINGFANG}" font-size="26" font-weight="500" fill="{FG}">AI排任务 · AI催回复 · AI追进度</text>
</svg>"""

def card_cn_exhaust():
    return svg_head(BG_LIGHT, LIGHT_ACCENT_PURPLE) + f"""
<text x="80" y="280" font-family="{PINGFANG}" font-size="100" font-weight="900" fill="url(#accent)" letter-spacing="-3">多线程</text>
<text x="80" y="440" font-family="{PINGFANG}" font-size="120" font-weight="900" fill="url(#accent)" letter-spacing="-3">认知耗竭</text>
<rect x="80" y="500" width="80" height="4" rx="2" fill="{PURPLE}" opacity=".5"/>
<text x="80" y="580" font-family="{PINGFANG}" font-size="32" font-weight="700" fill="{FG}">更快的处理器</text>
<text x="80" y="640" font-family="{PINGFANG}" font-size="32" font-weight="700" fill="{FG}">不是更强的人</text>
<text x="80" y="720" font-family="{PINGFANG}" font-size="26" font-weight="500" fill="{FG}">多线程切换 永远无法深度思考</text>
</svg>"""

def card_en_cover():
    return svg_head(BG_DARK, DARK_ACCENT_RED) + f"""
<text x="80" y="280" font-family="{MONO}" font-size="90" font-weight="900" fill="url(#accent)" letter-spacing="-2">AI IS STEALING</text>
<text x="80" y="400" font-family="{MONO}" font-size="100" font-weight="900" fill="url(#accent)" letter-spacing="-2">YOUR HUMANITY</text>
<rect x="80" y="460" width="80" height="3" rx="1.5" fill="#F87171" opacity=".5"/>
<text x="80" y="540" font-family="{MONO}" font-size="26" font-weight="400" fill="#FFFFFF">Ex-Meta PM Xiaoyin Qu's Reflection</text>
<text x="80" y="600" font-family="{MONO}" font-size="22" font-weight="400" fill="#FCA5A5">Emotional Flattening  ·  Lost Autonomy  ·  Burnout</text>
</svg>"""

def card_en_flatten():
    return svg_head(BG_DARK, DARK_ACCENT_BLUE) + f"""
<text x="80" y="280" font-family="{MONO}" font-size="90" font-weight="900" fill="url(#accent)" letter-spacing="-2">EMOTIONAL</text>
<text x="80" y="400" font-family="{MONO}" font-size="90" font-weight="900" fill="url(#accent)" letter-spacing="-2">FLATTENING</text>
<rect x="80" y="460" width="80" height="3" rx="1.5" fill="#60A5FA" opacity=".5"/>
<text x="80" y="540" font-family="{MONO}" font-size="28" font-weight="400" fill="#FFFFFF">You mimic AI's cold rationality</text>
<text x="80" y="600" font-family="{MONO}" font-size="22" font-weight="400" fill="#93C5FD">No anger  ·  No outrage  ·  No sadness</text>
<text x="80" y="670" font-family="{MONO}" font-size="22" font-weight="400" fill="#FFFFFF">Not maturity — neural atrophy</text>
</svg>"""

def card_en_schedule():
    return svg_head(BG_DARK, DARK_ACCENT_GREEN) + f"""
<text x="80" y="260" font-family="{MONO}" font-size="80" font-weight="900" fill="url(#accent)" letter-spacing="-1">AI CONTROLS</text>
<text x="80" y="370" font-family="{MONO}" font-size="96" font-weight="900" fill="url(#accent)" letter-spacing="-1">YOUR SCHEDULE</text>
<rect x="80" y="430" width="80" height="3" rx="1.5" fill="#34D399" opacity=".5"/>
<text x="80" y="520" font-family="{MONO}" font-size="26" font-weight="400" fill="#FFFFFF">2AM summaries · 8AM task lists</text>
<text x="80" y="580" font-family="{MONO}" font-size="22" font-weight="400" fill="#6EE7B7">Lunch pings · Evening progress · Weekend flags</text>
<text x="80" y="660" font-family="{MONO}" font-size="24" font-weight="700" fill="#FFFFFF">The tool became the master</text>
</svg>"""

def card_en_exhaust():
    return svg_head(BG_DARK, DARK_ACCENT_PURPLE) + f"""
<text x="80" y="280" font-family="{MONO}" font-size="82" font-weight="900" fill="url(#accent)" letter-spacing="-2">COGNITIVE</text>
<text x="80" y="400" font-family="{MONO}" font-size="90" font-weight="900" fill="url(#accent)" letter-spacing="-2">EXHAUSTION</text>
<rect x="80" y="460" width="80" height="3" rx="1.5" fill="#A78BFA" opacity=".5"/>
<text x="80" y="540" font-family="{MONO}" font-size="28" font-weight="400" fill="#FFFFFF">A faster processor</text>
<text x="80" y="600" font-family="{MONO}" font-size="28" font-weight="400" fill="#C4B5FD">not a stronger person</text>
<text x="80" y="670" font-family="{MONO}" font-size="22" font-weight="400" fill="#93C5FD">Infinite switching  ·  Zero depth</text>
</svg>"""

CARDS = [
    ("card-1.svg", card_cn_cover()),
    ("card-2.svg", card_cn_flatten()),
    ("card-3.svg", card_cn_schedule()),
    ("card-4.svg", card_cn_exhaust()),
    ("card-5.svg", card_en_cover()),
    ("card-6.svg", card_en_flatten()),
    ("card-7.svg", card_en_schedule()),
    ("card-8.svg", card_en_exhaust()),
]

def main():
    for name, svg in CARDS:
        svg_path = HERE / name
        png_path = svg_path.with_suffix(".png")
        svg_path.write_text(svg, encoding="utf-8")
        print(f"  SVG  {name}")
        result = subprocess.run(
            ["inkscape", str(svg_path), "--export-filename", str(png_path), "--export-dpi", "192"],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0:
            size = png_path.stat().st_size
            print(f"  PNG  {png_path.name}  ({size//1024} KB)")
        else:
            print(f"  FAIL {name}: {result.stderr[:200]}")

if __name__ == "__main__":
    main()