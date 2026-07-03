#!/usr/bin/env python3
import subprocess, os
ROOT = os.path.dirname(os.path.abspath(__file__))

C = "#FAF7F2"
C2 = "#F3F0E8"
W = "#FFFFFF"
T = "#1E293B"
TD = "#64748B"
TL = "#94A3B8"
RED = "#EF4444"
REDL = "#FEE2E2"
ORANGE = "#F97316"
ORANGEL = "#FFEDD5"
BLUE = "#3B82F6"
BLUEL = "#DBEAFE"
GREEN = "#10B981"
GREENL = "#D1FAE5"
PURPLE = "#8B5CF6"
PURPLEL = "#EDE9FE"
YELLOW = "#F59E0B"
YELLOWL = "#FEF3C7"

def bg(w, h):
    return f'<rect width="{w}" height="{h}" fill="url(#bgG)"/><circle cx="{w*0.08}" cy="{h*0.08}" r="60" fill="{REDL}" opacity="0.5"/><circle cx="{w*0.92}" cy="{h*0.12}" r="50" fill="{BLUEL}" opacity="0.5"/><circle cx="{w*0.08}" cy="{h*0.88}" r="70" fill="{ORANGEL}" opacity="0.4"/><circle cx="{w*0.92}" cy="{h*0.78}" r="80" fill="{PURPLEL}" opacity="0.4"/>'

def svg_wrap(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
<defs><linearGradient id="bgG" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{C}"/><stop offset="100%" stop-color="{C2}"/></linearGradient></defs>
{bg(w, h)}
{body}
</svg>'''

def cover():
    return svg_wrap(1024, 1024, f'''
<text x="512" y="260" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="100" font-weight="900" fill="{T}" letter-spacing="-4">阿里全面禁用</text>
<text x="512" y="400" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="120" font-weight="900" fill="{RED}" letter-spacing="-5">Claude Code</text>

<g transform="translate(262, 480)">
<rect x="0" y="0" width="500" height="70" rx="35" fill="{REDL}" stroke="{RED}" stroke-width="2"/>
<text x="250" y="44" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="30" font-weight="800" fill="{RED}">列入高风险软件名单</text>
</g>

<text x="512" y="620" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="26" font-weight="700" fill="{T}">7月10日起 · 全员卸载</text>
<text x="512" y="665" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">原因：Claude Code 被曝存在植入后门风险</text>

<g transform="translate(120, 740)">
<rect x="0" y="0" width="200" height="44" rx="22" fill="{REDL}"/><text x="100" y="29" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="600" fill="{RED}">Sonnet 禁</text>
<rect x="220" y="0" width="200" height="44" rx="22" fill="{ORANGEL}"/><text x="320" y="29" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="600" fill="{ORANGE}">Opus 禁</text>
<rect x="440" y="0" width="200" height="44" rx="22" fill="{YELLOWL}"/><text x="540" y="29" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="600" fill="{YELLOW}">Fable 禁</text>
<rect x="660" y="0" width="200" height="44" rx="22" fill="{BLUEL}"/><text x="760" y="29" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="600" fill="{BLUE}">全线禁</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TL}">#阿里 #ClaudeCode #AI安全 #程序员</text>
''')

def card_1():
    items = ""
    events = [
        (RED, REDL, "事件", "2026.07.03", "阿里内部通知，全体员工卸载 Claude Code"),
        (ORANGE, ORANGEL, "原因", "植入后门风险", "被曝存在代码级安全漏洞，列入高风险名单"),
        (YELLOW, YELLOWL, "范围", "Anthropic 全线产品", "Sonnet / Opus / Fable / Claude Code 全部禁用"),
        (BLUE, BLUEL, "替代", "Qoder", "阿里云自研编程助手，承接内部流量"),
    ]
    for i, (color, light, tag, title, sub) in enumerate(events):
        y = 170 + i * 150
        items += f'''
<g transform="translate(62, {y})">
<rect x="0" y="0" width="900" height="120" rx="14" fill="{W}" stroke="{color}" stroke-width="1.5"/>
<rect x="0" y="0" width="5" height="120" rx="2.5" fill="{color}"/>
<text x="30" y="35" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" font-weight="700" fill="{color}">{tag}</text>
<text x="100" y="35" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{T}">{title}</text>
<text x="30" y="70" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" fill="{TD}">{sub}</text>
<circle cx="30" cy="95" r="5" fill="{color}" opacity="0.3"/>
</g>'''
    return svg_wrap(1024, 1024, f'''
<text x="512" y="85" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="38" font-weight="800" fill="{T}">事件全貌</text>
<text x="512" y="125" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">来源：科创板日报 · 阿里内部人士确认</text>
{items}
<text x="512" y="960" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TL}">7月10日起正式生效</text>
''')

def card_2():
    points = [
        (RED, REDL, "代码级后门", "Claude Code 直接接触企业私有代码，一旦植入后门等于给攻击者开了内网权限"),
        (ORANGE, ORANGEL, "供应链攻击", "AI 模型下发恶意指令 → 本地 Agent 执行 → 传统杀毒无法拦截"),
        (YELLOW, YELLOWL, "数据泄露风险", "代码助手读取全部项目文件，核心算法/密钥/配置面临泄密"),
        (BLUE, BLUEL, "行业连锁反应", "阿里打响第一枪，其他大厂大概率跟进 AI 工具安全审查"),
    ]
    items = ""
    for i, (color, light, title, desc) in enumerate(points):
        y = 160 + i * 170
        items += f'''
<g transform="translate(62, {y})">
<rect x="0" y="0" width="900" height="140" rx="16" fill="{W}" stroke="{color}" stroke-width="1.5"/>
<rect x="20" y="20" width="40" height="40" rx="20" fill="{color}"/>
<text x="40" y="45" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="800" fill="{W}">{i+1}</text>
<text x="80" y="40" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{T}">{title}</text>
<text x="25" y="80" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">{desc}</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
<text x="512" y="80" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="38" font-weight="800" fill="{T}">为什么是红线？</text>
<text x="512" y="120" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">AI 编程工具的安全风险拆解</text>
{items}
<text x="512" y="960" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TL}">企业级 AI 工具安全审查从加分项变成必选项</text>
''')

def card_3():
    return svg_wrap(1024, 1024, f'''
<text x="512" y="80" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="38" font-weight="800" fill="{T}">影响与启示</text>
<text x="512" y="120" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">不止是一家公司的决策</text>

<g transform="translate(62, 170)">
<rect x="0" y="0" width="430" height="200" rx="16" fill="{W}" stroke="{RED}" stroke-width="1.5"/>
<text x="215" y="50" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="25" font-weight="700" fill="{RED}">Qoder 接盘</text>
<text x="215" y="90" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">阿里云编程助手</text>
<text x="215" y="125" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">承接全部内部流量</text>
<text x="215" y="160" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">国产替代再下一城</text>
</g>

<g transform="translate(532, 170)">
<rect x="0" y="0" width="430" height="200" rx="16" fill="{W}" stroke="{BLUE}" stroke-width="1.5"/>
<text x="215" y="50" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="25" font-weight="700" fill="{BLUE}">行业连锁反应</text>
<text x="215" y="90" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">其他大厂跟进审查</text>
<text x="215" y="125" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">AI 工具安全标准</text>
<text x="215" y="160" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">可能加速出台</text>
</g>

<g transform="translate(62, 400)">
<rect x="0" y="0" width="430" height="200" rx="16" fill="{W}" stroke="{ORANGE}" stroke-width="1.5"/>
<text x="215" y="50" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="25" font-weight="700" fill="{ORANGE}">开发者影响</text>
<text x="215" y="90" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">阿里系员工立即切换</text>
<text x="215" y="125" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">外部用户评估风险</text>
<text x="215" y="160" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">多云工具链成趋势</text>
</g>

<g transform="translate(532, 400)">
<rect x="0" y="0" width="430" height="200" rx="16" fill="{W}" stroke="{PURPLE}" stroke-width="1.5"/>
<text x="215" y="50" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="25" font-weight="700" fill="{PURPLE}">长远趋势</text>
<text x="215" y="90" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">AI 工具安全审查</text>
<text x="215" y="125" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">从加分项变必选项</text>
<text x="215" y="160" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">安全大于效率</text>
</g>

<g transform="translate(62, 660)">
<rect x="0" y="0" width="900" height="70" rx="35" fill="{REDL}" stroke="{RED}" stroke-width="1"/>
<text x="450" y="44" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{RED}">AI 工具好用重要，安全更重要</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TL}">#阿里 #ClaudeCode #AI安全 #Qoder</text>
''')

if __name__ == "__main__":
    cards = [
        ("cover", cover(), 1024, 1024),
        ("card-1", card_1(), 1024, 1024),
        ("card-2", card_2(), 1024, 1024),
        ("card-3", card_3(), 1024, 1024),
    ]
    for name, svg, w, h in cards:
        svg_path = os.path.join(ROOT, f"{name}.svg")
        png_path = os.path.join(ROOT, f"{name}.png")
        with open(svg_path, "w") as f:
            f.write(svg)
        subprocess.run(["inkscape", svg_path, "-o", png_path, "-w", str(w), "-h", str(h)], check=True, capture_output=True)
        sz = os.path.getsize(png_path) // 1024
        print(f"  {name}.png ({sz} KB)")
    print("Done!")