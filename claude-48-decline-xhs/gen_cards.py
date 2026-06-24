import subprocess, os
ROOT = os.path.dirname(os.path.abspath(__file__))

# Dark palette
BG = "#0B1027"
CARD_BG = "#151B3A"
TEXT = "#F8FAFC"
SUB = "#94A3B8"
PURPLE = "#7C3AED"
PURPLE_L = "#2D1B69"
ORANGE = "#F97316"
ORANGE_L = "#3D2A10"
RED = "#EF4444"
GREEN = "#10B981"
BLUE = "#3B82F6"
YELLOW = "#F59E0B"

FONT = "PingFang SC,Heiti SC,STHeiti,Hiragino Sans GB,Microsoft YaHei,sans-serif"
FONT_EN = "Inter,Helvetica,Arial,sans-serif"

def svg_wrap(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
<defs>
<radialGradient id="bgG" cx="50%" cy="50%" r="70%">
<stop offset="0%" stop-color="#151B3A"/>
<stop offset="100%" stop-color="{BG}"/>
</radialGradient>
</defs>
<rect width="{w}" height="{h}" fill="url(#bgG)"/>
{body}
</svg>'''

def cover():
    return svg_wrap(1024, 1024, f'''
<circle cx="512" cy="512" r="320" fill="none" stroke="{PURPLE}" stroke-width="1" opacity="0.15"/>
<circle cx="512" cy="512" r="220" fill="none" stroke="{PURPLE}" stroke-width="0.5" opacity="0.1" stroke-dasharray="6,6"/>
<text x="512" y="380" text-anchor="middle" font-family="{FONT}" font-size="100" font-weight="900" fill="{TEXT}" letter-spacing="-3">Claude 4.8</text>
<text x="512" y="500" text-anchor="middle" font-family="{FONT}" font-size="100" font-weight="900" fill="{ORANGE}" letter-spacing="-3">降智争议</text>
<rect x="320" y="550" width="384" height="3" rx="1.5" fill="{PURPLE}" opacity="0.6"/>
<text x="512" y="600" text-anchor="middle" font-family="{FONT}" font-size="32" font-weight="600" fill="{SUB}">用户集体吐槽质量下降</text>
<text x="512" y="650" text-anchor="middle" font-family="{FONT}" font-size="28" font-weight="500" fill="{SUB}">GPT-5 已全面反超</text>
<g transform="translate(512, 750)">
<rect x="-120" y="-28" width="240" height="56" rx="28" fill="{PURPLE}" opacity="0.2" stroke="{PURPLE}" stroke-width="1"/>
<text x="0" y="6" text-anchor="middle" font-family="{FONT_EN}" font-size="18" font-weight="700" fill="{PURPLE}">SWE-bench ▼ 5.5%</text>
</g>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{SUB}" opacity="0.5">#Claude #GPT5 #AI竞争</text>
''')

def card_1():
    cards = [
        ("代码生成退化", "500行→反复修正3轮", RED, "#3D1A1A"),
        ("逻辑推理变弱", "多步任务自相矛盾", ORANGE, ORANGE_L),
        ("长篇偏离主题", ">2000 token 开始胡言", YELLOW, "#3D2F10"),
    ]
    items = ""
    for i, (title, sub, color, bgc) in enumerate(cards):
        y = 180 + i * 240
        items += f'''
<g transform="translate(62, {y})">
<rect x="0" y="0" width="900" height="200" rx="18" fill="{bgc}" stroke="{color}" stroke-width="1" opacity="0.9"/>
<rect x="0" y="0" width="6" height="200" rx="3" fill="{color}"/>
<text x="40" y="60" font-family="{FONT}" font-size="36" font-weight="800" fill="{TEXT}">{title}</text>
<text x="40" y="110" font-family="{FONT}" font-size="24" font-weight="500" fill="{SUB}">{sub}</text>
<text x="40" y="160" font-family="{FONT}" font-size="16" fill="{color}" opacity="0.7">用户 AB 测试：4.7 明显优于 4.8</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
<text x="512" y="80" text-anchor="middle" font-family="{FONT}" font-size="40" font-weight="900" fill="{TEXT}">用户体感崩塌</text>
<text x="512" y="120" text-anchor="middle" font-family="{FONT}" font-size="22" fill="{SUB}">Reddit / Twitter 用户集体吐槽</text>
{items}
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{SUB}" opacity="0.5">来源: Reddit r/ClaudeAI, Twitter #ClaudeDecline</text>
''')

def card_2():
    return svg_wrap(1024, 1024, f'''
<text x="512" y="80" text-anchor="middle" font-family="{FONT}" font-size="40" font-weight="900" fill="{TEXT}">GPT-5 反超</text>
<text x="512" y="120" text-anchor="middle" font-family="{FONT}" font-size="22" fill="{SUB}">关键编程基准对比</text>

<g transform="translate(62, 180)">
<rect x="0" y="0" width="900" height="60" rx="10" fill="{PURPLE_L}"/>
<text x="40" y="38" font-family="{FONT}" font-size="20" font-weight="700" fill="{SUB}">基准测试</text>
<text x="330" y="38" font-family="{FONT}" font-size="20" font-weight="700" fill="{ORANGE}">Claude 4.8</text>
<text x="530" y="38" font-family="{FONT}" font-size="20" font-weight="700" fill="{GREEN}">GPT-5</text>
<text x="750" y="38" font-family="{FONT}" font-size="20" font-weight="700" fill="{SUB}">差距</text>
</g>

<g transform="translate(62, 260)">
<rect x="0" y="0" width="900" height="70" rx="10" fill="#1A183A"/>
<text x="40" y="44" font-family="{FONT}" font-size="22" font-weight="600" fill="{TEXT}">SWE-bench Verified</text>
<text x="330" y="44" font-family="{FONT}" font-size="22" font-weight="700" fill="{ORANGE}">58.2%</text>
<text x="530" y="44" font-family="{FONT}" font-size="22" font-weight="700" fill="{GREEN}">63.7%</text>
<text x="740" y="44" font-family="{FONT}" font-size="22" font-weight="700" fill="{RED}">-5.5%</text>
</g>

<g transform="translate(62, 350)">
<rect x="0" y="0" width="900" height="70" rx="10" fill="#1A183A"/>
<text x="40" y="44" font-family="{FONT}" font-size="22" font-weight="600" fill="{TEXT}">HumanEval+</text>
<text x="330" y="44" font-family="{FONT}" font-size="22" font-weight="700" fill="{ORANGE}">86.4%</text>
<text x="530" y="44" font-family="{FONT}" font-size="22" font-weight="700" fill="{GREEN}">91.2%</text>
<text x="740" y="44" font-family="{FONT}" font-size="22" font-weight="700" fill="{RED}">-4.8%</text>
</g>

<g transform="translate(62, 440)">
<rect x="0" y="0" width="900" height="70" rx="10" fill="#1A183A"/>
<text x="40" y="44" font-family="{FONT}" font-size="22" font-weight="600" fill="{TEXT}">LiveCodeBench v3</text>
<text x="330" y="44" font-family="{FONT}" font-size="22" font-weight="700" fill="{ORANGE}">54.1%</text>
<text x="530" y="44" font-family="{FONT}" font-size="22" font-weight="700" fill="{GREEN}">61.8%</text>
<text x="740" y="44" font-family="{FONT}" font-size="22" font-weight="700" fill="{RED}">-7.7%</text>
</g>

<g transform="translate(62, 580)">
<rect x="0" y="0" width="900" height="140" rx="16" fill="{ORANGE_L}" stroke="{ORANGE}" stroke-width="1"/>
<text x="30" y="40" font-family="{FONT}" font-size="22" font-weight="700" fill="{ORANGE}">💡 半年前 Claude 还是编程王者</text>
<text x="30" y="80" font-family="{FONT}" font-size="19" font-weight="500" fill="{SUB}">Claude 3.5 Sonnet 曾连续 6 个月霸榜</text>
<text x="30" y="115" font-family="{FONT}" font-size="19" font-weight="500" fill="{SUB}">如今 GPT-5 在所有编程基准上完成反超</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{SUB}" opacity="0.5">数据来源: SWE-bench, HumanEval, LiveCodeBench 2026-06</text>
''')

def card_3():
    items = ""
    causes = [
        ("01", "成本优化", "小模型路由替代主力模型", "降低推理成本牺牲质量", PURPLE, PURPLE_L),
        ("02", "量化压缩", "过度量化损失模型精度", "响应快了但智商降了", ORANGE, ORANGE_L),
        ("03", "Safety 过激", "新安全机制误杀正常输出", "生成内容被过度过滤", RED, "#3D1A1A"),
    ]
    for i, (num, title, sub, detail, color, bgc) in enumerate(causes):
        y = 170 + i * 220
        items += f'''
<g transform="translate(62, {y})">
<rect x="0" y="0" width="900" height="190" rx="16" fill="{bgc}" stroke="{color}" stroke-width="1"/>
<circle cx="55" cy="50" r="22" fill="{color}" opacity="0.3"/>
<text x="55" y="57" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="800" fill="{color}">{num}</text>
<text x="100" y="55" font-family="{FONT}" font-size="28" font-weight="800" fill="{TEXT}">{title}</text>
<text x="40" y="100" font-family="{FONT}" font-size="22" font-weight="500" fill="{SUB}">{sub}</text>
<text x="40" y="145" font-family="{FONT}" font-size="20" fill="{color}" opacity="0.8">{detail}</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
<text x="512" y="80" text-anchor="middle" font-family="{FONT}" font-size="40" font-weight="900" fill="{TEXT}">三大可能原因</text>
<text x="512" y="120" text-anchor="middle" font-family="{FONT}" font-size="22" fill="{SUB}">社区分析 + 行业推测</text>
{items}
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{SUB}" opacity="0.5">Anthropic 尚未正面回应</text>
''')

def card_4():
    return svg_wrap(1024, 1024, f'''
<text x="512" y="120" text-anchor="middle" font-family="{FONT}" font-size="44" font-weight="900" fill="{TEXT}">意味着什么？</text>

<g transform="translate(62, 200)">
<rect x="0" y="0" width="900" height="140" rx="16" fill="#1A183A" stroke="{PURPLE}" stroke-width="1"/>
<circle cx="40" cy="45" r="18" fill="{PURPLE}" opacity="0.3"/>
<text x="40" y="52" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="800" fill="{PURPLE}">1</text>
<text x="75" y="50" font-family="{FONT}" font-size="26" font-weight="700" fill="{TEXT}">用户开始回流 GPT-5</text>
<text x="40" y="95" font-family="{FONT}" font-size="20" font-weight="500" fill="{SUB}">重度编程用户迁移，Claude Pro 订阅可能下滑</text>
</g>

<g transform="translate(62, 370)">
<rect x="0" y="0" width="900" height="140" rx="16" fill="#1A183A" stroke="{ORANGE}" stroke-width="1"/>
<circle cx="40" cy="45" r="18" fill="{ORANGE}" opacity="0.3"/>
<text x="40" y="52" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="800" fill="{ORANGE}">2</text>
<text x="75" y="50" font-family="{FONT}" font-size="26" font-weight="700" fill="{TEXT}">Anthropic 信任度下降</text>
<text x="40" y="95" font-family="{FONT}" font-size="20" font-weight="500" fill="{SUB}">不透明的降质操作引发开发者信任危机</text>
</g>

<g transform="translate(62, 540)">
<rect x="0" y="0" width="900" height="140" rx="16" fill="#1A183A" stroke="{GREEN}" stroke-width="1"/>
<circle cx="40" cy="45" r="18" fill="{GREEN}" opacity="0.3"/>
<text x="40" y="52" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="800" fill="{GREEN}">3</text>
<text x="75" y="50" font-family="{FONT}" font-size="26" font-weight="700" fill="{TEXT}">AI 没有永远的王者</text>
<text x="40" y="95" font-family="{FONT}" font-size="20" font-weight="500" fill="{SUB}">赛道竞争激烈，今天领先明天可能被反超</text>
</g>

<g transform="translate(120, 760)">
<rect x="0" y="0" width="784" height="80" rx="40" fill="none" stroke="{PURPLE}" stroke-width="1.5" stroke-dasharray="8,4"/>
<text x="392" y="46" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="600" fill="{PURPLE}" opacity="0.8">永远不要对任何一个模型产生依赖</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{SUB}" opacity="0.5">#Claude #GPT5 #AI竞争</text>
''')

if __name__ == "__main__":
    cards = [
        ("cover", cover(), 1024, 1024),
        ("card-1", card_1(), 1024, 1024),
        ("card-2", card_2(), 1024, 1024),
        ("card-3", card_3(), 1024, 1024),
        ("card-4", card_4(), 1024, 1024),
    ]
    for name, svg, w, h in cards:
        svg_path = os.path.join(ROOT, f"{name}.svg")
        png_path = os.path.join(ROOT, f"{name}.png")
        with open(svg_path, "w") as f:
            f.write(svg)
        subprocess.run(["inkscape", svg_path, "-o", png_path, "-w", str(w), "-h", str(h)], check=True, capture_output=True)
        sz = os.path.getsize(png_path) // 1024
        print(f"  {name}.png ({sz} KB)")
    print("Done! 5 cards regenerated.")