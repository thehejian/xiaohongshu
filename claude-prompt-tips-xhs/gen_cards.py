import subprocess, pathlib

HERE = pathlib.Path(__file__).parent

# === LIGHT (Chinese) ===
LIGHT_BG = "#FAF7F2"
LIGHT_TEXT = "#1E293B"
LIGHT_SUB = "#475569"
LIGHT_ACCENT = "#D97706"
LIGHT_BLUE = "#2563EB"
LIGHT_GREEN = "#059669"
LIGHT_ORANGE = "#EA580C"
LIGHT_PINK = "#DB2777"

# === DARK (English) ===
DARK_BG = "#0B1027"
DARK_TEXT = "#F8FAFC"
DARK_SUB = "#94A3B8"
DARK_ACCENT = "#F59E0B"
DARK_BLUE = "#3B82F6"
DARK_GREEN = "#10B981"
DARK_ORANGE = "#F97316"
DARK_PINK = "#EC4899"

def light_cover():
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
<rect width="1024" height="1024" fill="{LIGHT_BG}"/>
<g transform="translate(512,512)">
<text x="0" y="-50" font-family="PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif" font-size="72" font-weight="900" fill="{LIGHT_TEXT}" text-anchor="middle" dominant-baseline="middle" letter-spacing="-1">Claude 高阶</text>
<text x="0" y="50" font-family="PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif" font-size="72" font-weight="900" fill="{LIGHT_ACCENT}" text-anchor="middle" dominant-baseline="middle" letter-spacing="-1">提示词 8 招</text>
</g>
</svg>"""

def light_tips1():
    tips = [
        ("01", "结构标签法", "用 XML 标签划边界", LIGHT_BLUE),
        ("02", "反向追问法", "先澄清再回答", LIGHT_GREEN),
        ("03", "思考链法", "逐步推理标注依据", LIGHT_ORANGE),
        ("04", "角色锚定法", "越具体越强大", LIGHT_PINK),
    ]
    cards = ""
    for i, (num, title, sub, color) in enumerate(tips):
        col = i % 2
        row = i // 2
        x = 122 + col * 380
        y = 332 + row * 320
        cards += f"""
<g transform="translate({x},{y})">
<rect x="0" y="0" width="340" height="280" rx="20" fill="#FFFFFF"/>
<rect x="0" y="0" width="6" height="280" rx="3" fill="{color}"/>
<text x="36" y="70" font-family="PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif" font-size="14" font-weight="700" letter-spacing="2" fill="{color}">{num}</text>
<text x="36" y="120" font-family="PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif" font-size="30" font-weight="800" fill="{LIGHT_TEXT}">{title}</text>
<text x="36" y="165" font-family="PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif" font-size="18" font-weight="500" fill="{LIGHT_SUB}">{sub}</text>
</g>"""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
<rect width="1024" height="1024" fill="{LIGHT_BG}"/>
{cards}
</svg>"""

def light_tips2():
    tips = [
        ("05", "示例驱动法", "Few-Shot 最稳", LIGHT_BLUE),
        ("06", "输出锁定法", "JSON 一步到位", LIGHT_GREEN),
        ("07", "对抗审查法", "主动让 AI 挑刺", LIGHT_ORANGE),
        ("08", "知识边界法", "不知道就说不知道", LIGHT_PINK),
    ]
    cards = ""
    for i, (num, title, sub, color) in enumerate(tips):
        col = i % 2
        row = i // 2
        x = 122 + col * 380
        y = 332 + row * 320
        cards += f"""
<g transform="translate({x},{y})">
<rect x="0" y="0" width="340" height="280" rx="20" fill="#FFFFFF"/>
<rect x="0" y="0" width="6" height="280" rx="3" fill="{color}"/>
<text x="36" y="70" font-family="PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif" font-size="14" font-weight="700" letter-spacing="2" fill="{color}">{num}</text>
<text x="36" y="120" font-family="PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif" font-size="30" font-weight="800" fill="{LIGHT_TEXT}">{title}</text>
<text x="36" y="165" font-family="PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif" font-size="18" font-weight="500" fill="{LIGHT_SUB}">{sub}</text>
</g>"""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
<rect width="1024" height="1024" fill="{LIGHT_BG}"/>
{cards}
</svg>"""

def light_summary():
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
<rect width="1024" height="1024" fill="{LIGHT_BG}"/>
<g transform="translate(512,512)">
<text x="0" y="-50" font-family="PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif" font-size="44" font-weight="900" fill="{LIGHT_TEXT}" text-anchor="middle" dominant-baseline="middle" letter-spacing="-0.5">和 Claude 交流</text>
<text x="0" y="50" font-family="PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif" font-size="44" font-weight="900" fill="{LIGHT_ACCENT}" text-anchor="middle" dominant-baseline="middle" letter-spacing="-0.5">就像和一流顾问合作</text>
<text x="0" y="150" font-family="PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif" font-size="22" font-weight="500" fill="{LIGHT_SUB}" text-anchor="middle" dominant-baseline="middle">交付质量 ≈ 输入的上下文质量</text>
<text x="0" y="200" font-family="PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif" font-size="22" font-weight="500" fill="{LIGHT_SUB}" text-anchor="middle" dominant-baseline="middle">越具体的框架 → 越精准的输出</text>
<text x="0" y="250" font-family="PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif" font-size="22" font-weight="500" fill="{LIGHT_SUB}" text-anchor="middle" dominant-baseline="middle">越明确的约束 → 越少的意外</text>
</g>
</svg>"""

def dark_cover():
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
<rect width="1024" height="1024" fill="{DARK_BG}"/>
<g transform="translate(512,512)">
<text x="0" y="-50" font-family="Inter, Helvetica, Arial, sans-serif" font-size="72" font-weight="900" fill="{DARK_TEXT}" text-anchor="middle" dominant-baseline="middle" letter-spacing="-1">Claude</text>
<text x="0" y="50" font-family="Inter, Helvetica, Arial, sans-serif" font-size="72" font-weight="900" fill="{DARK_ACCENT}" text-anchor="middle" dominant-baseline="middle" letter-spacing="-1">Prompt 8 Tips</text>
</g>
</svg>"""

def dark_tips1():
    tips = [
        ("01", "XML Tags", "Structure the prompt", DARK_BLUE),
        ("02", "Ask First", "Clarify before answering", DARK_GREEN),
        ("03", "Chain of Thought", "Show your reasoning", DARK_ORANGE),
        ("04", "Role Anchor", "Be specific about identity", DARK_PINK),
    ]
    cards = ""
    for i, (num, title, sub, color) in enumerate(tips):
        col = i % 2
        row = i // 2
        x = 122 + col * 380
        y = 332 + row * 320
        cards += f"""
<g transform="translate({x},{y})">
<rect x="0" y="0" width="340" height="280" rx="20" fill="#151B3A"/>
<rect x="0" y="0" width="6" height="280" rx="3" fill="{color}"/>
<text x="36" y="70" font-family="Inter, Helvetica, Arial, sans-serif" font-size="14" font-weight="700" letter-spacing="2" fill="{color}">{num}</text>
<text x="36" y="120" font-family="Inter, Helvetica, Arial, sans-serif" font-size="28" font-weight="800" fill="{DARK_TEXT}">{title}</text>
<text x="36" y="165" font-family="Inter, Helvetica, Arial, sans-serif" font-size="16" font-weight="500" fill="{DARK_SUB}">{sub}</text>
</g>"""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
<rect width="1024" height="1024" fill="{DARK_BG}"/>
{cards}
</svg>"""

def dark_tips2():
    tips = [
        ("05", "Few-Shot", "Give examples first", DARK_BLUE),
        ("06", "JSON Lock", "Lock output format", DARK_GREEN),
        ("07", "Adversarial", "Let AI critique you", DARK_ORANGE),
        ("08", "Know Limits", "Say I don't know", DARK_PINK),
    ]
    cards = ""
    for i, (num, title, sub, color) in enumerate(tips):
        col = i % 2
        row = i // 2
        x = 122 + col * 380
        y = 332 + row * 320
        cards += f"""
<g transform="translate({x},{y})">
<rect x="0" y="0" width="340" height="280" rx="20" fill="#151B3A"/>
<rect x="0" y="0" width="6" height="280" rx="3" fill="{color}"/>
<text x="36" y="70" font-family="Inter, Helvetica, Arial, sans-serif" font-size="14" font-weight="700" letter-spacing="2" fill="{color}">{num}</text>
<text x="36" y="120" font-family="Inter, Helvetica, Arial, sans-serif" font-size="28" font-weight="800" fill="{DARK_TEXT}">{title}</text>
<text x="36" y="165" font-family="Inter, Helvetica, Arial, sans-serif" font-size="16" font-weight="500" fill="{DARK_SUB}">{sub}</text>
</g>"""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
<rect width="1024" height="1024" fill="{DARK_BG}"/>
{cards}
</svg>"""

def dark_summary():
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
<rect width="1024" height="1024" fill="{DARK_BG}"/>
<g transform="translate(512,512)">
<text x="0" y="-50" font-family="Inter, Helvetica, Arial, sans-serif" font-size="44" font-weight="700" fill="{DARK_TEXT}" text-anchor="middle" dominant-baseline="middle" letter-spacing="-0.5">Talk to Claude</text>
<text x="0" y="50" font-family="Inter, Helvetica, Arial, sans-serif" font-size="44" font-weight="700" fill="{DARK_ACCENT}" text-anchor="middle" dominant-baseline="middle" letter-spacing="-0.5">like a top consultant</text>
<text x="0" y="150" font-family="Inter, Helvetica, Arial, sans-serif" font-size="22" font-weight="500" fill="{DARK_SUB}" text-anchor="middle" dominant-baseline="middle">Output quality ≈ Context quality</text>
<text x="0" y="200" font-family="Inter, Helvetica, Arial, sans-serif" font-size="22" font-weight="500" fill="{DARK_SUB}" text-anchor="middle" dominant-baseline="middle">Specific framework → Precise output</text>
<text x="0" y="250" font-family="Inter, Helvetica, Arial, sans-serif" font-size="22" font-weight="500" fill="{DARK_SUB}" text-anchor="middle" dominant-baseline="middle">Clear constraints → Fewer surprises</text>
</g>
</svg>"""

CARDS = [
    ("card-1-light.svg", light_cover()),
    ("card-2-light.svg", light_tips1()),
    ("card-3-light.svg", light_tips2()),
    ("card-4-light.svg", light_summary()),
    ("card-1-dark.svg", dark_cover()),
    ("card-2-dark.svg", dark_tips1()),
    ("card-3-dark.svg", dark_tips2()),
    ("card-4-dark.svg", dark_summary()),
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
