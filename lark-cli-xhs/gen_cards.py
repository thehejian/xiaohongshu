#!/usr/bin/env python3
"""Generate light-style cards for lark-cli (1024x1024 + 1792x1024 banner)."""
import subprocess, os
ROOT = os.path.dirname(os.path.abspath(__file__))

C = "#FAF7F2"
C2 = "#F3F0E8"
W = "#FFFFFF"
T = "#1E293B"
TD = "#64748B"
TL = "#94A3B8"
BLUE = "#3370FF"
BLUEL = "#E8EEFF"
TEAL = "#0EA5E9"
TEALL = "#E0F2FE"
PURPLE = "#8B5CF6"
PURPLEL = "#EDE9FE"
ORANGE = "#F97316"
ORANGEL = "#FFEDD5"
GREEN = "#10B981"
GREENL = "#D1FAE5"

def bg(w, h):
    return f'<rect width="{w}" height="{h}" fill="url(#bgG)"/><circle cx="{w*0.08}" cy="{h*0.08}" r="60" fill="{BLUEL}" opacity="0.5"/><circle cx="{w*0.92}" cy="{h*0.12}" r="50" fill="{PURPLEL}" opacity="0.4"/><circle cx="{w*0.08}" cy="{h*0.88}" r="70" fill="{TEALL}" opacity="0.3"/><circle cx="{w*0.92}" cy="{h*0.78}" r="80" fill="{ORANGEL}" opacity="0.3"/>'

def svg_wrap(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
<defs><linearGradient id="bgG" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{C}"/><stop offset="100%" stop-color="{C2}"/></linearGradient></defs>
{bg(w, h)}
{body}
</svg>'''

def card_square():
    domains = [
        ("日历", BLUE, BLUEL),
        ("消息", TEAL, TEALL),
        ("文档", PURPLE, PURPLEL),
        ("表格", ORANGE, ORANGEL),
        ("邮箱", GREEN, GREENL),
        ("通讯录", BLUE, BLUEL),
    ]
    chips = ""
    for i, (name, color, light) in enumerate(domains):
        x = 162 + i * 120
        chips += f'<rect x="{x}" y="720" width="100" height="40" rx="20" fill="{light}"/><text x="{x+50}" y="746" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" font-weight="600" fill="{color}">{name}</text>'
    return svg_wrap(1024, 1024, f'''
<text x="512" y="260" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="48" font-weight="400" fill="{TD}" letter-spacing="2">飞书</text>
<text x="512" y="390" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="160" font-weight="900" fill="{BLUE}" letter-spacing="-5">CLI</text>
<text x="512" y="470" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" fill="{TD}">一行命令管所有 · 开发者效率神器</text>
<g transform="translate(162, 560)">
  <rect x="0" y="0" width="700" height="80" rx="40" fill="{W}" stroke="{BLUE}" stroke-width="2"/>
  <text x="350" y="50" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" font-weight="700" fill="{BLUE}">npm i -g @larksuiteo/cli</text>
</g>
{chips}
<text x="512" y="850" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" fill="{TL}">日历 · 消息 · 文档 · 表格 · 邮箱 · 通讯录 · 审批 · 考勤</text>
<text x="512" y="960" text-anchor="middle" font-family="ui-monospace,monospace" font-size="16" fill="{TL}">github.com/larksuite/cli</text>''')

def card_1():
    services = [
        ("calendar", "日历会议", "+agenda / +create / +freebusy", BLUE, BLUEL),
        ("im", "即时通讯", "发消息 + 搜记录 + 群管理", TEAL, TEALL),
        ("docs", "云文档", "创建 / 更新 / 插入图片", PURPLE, PURPLEL),
        ("base", "多维表格", "建表 / 读写 / 公式配置", ORANGE, ORANGEL),
        ("mail", "邮箱", "起草 / 发送 / 收件箱", GREEN, GREENL),
        ("contact", "通讯录", "搜员工 / 查组织架构", BLUE, BLUEL),
    ]
    items = ""
    for i, (service, name, desc, color, light) in enumerate(services):
        y = 175 + i * 100
        items += f'''
<g transform="translate(62, {y})">
  <rect x="0" y="0" width="900" height="80" rx="14" fill="{light}"/>
  <text x="30" y="36" font-family="ui-monospace,monospace" font-size="20" font-weight="600" fill="{color}">{service}</text>
  <text x="30" y="62" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" font-weight="600" fill="{T}">{name}</text>
  <text x="480" y="48" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" fill="{TD}">{desc}</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
<text x="512" y="90" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="38" font-weight="800" fill="{T}">一行命令 · 全部场景</text>
<text x="512" y="130" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">lark-cli 覆盖飞书 8 大领域 API</text>
{items}
<text x="512" y="840" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TL}">+ 审批 · 考勤 · 妙记 · 任务 · 画板 · 知识库 · OKR</text>
<g transform="translate(262, 880)">
  <rect x="0" y="0" width="500" height="50" rx="25" fill="{BLUE}" opacity="0.1"/>
  <text x="250" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" font-weight="600" fill="{BLUE}">user / bot 双身份切换 · 自动翻页</text>
</g>
''')

def card_2():
    return svg_wrap(1024, 1024, f'''
<text x="512" y="90" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="38" font-weight="800" fill="{T}">开发者体验</text>
<text x="512" y="130" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">原生 API 封装 · AI Agent 友好</text>

<g transform="translate(62, 200)">
  <rect x="0" y="0" width="900" height="160" rx="18" fill="{W}" stroke="{BLUE}" stroke-width="2"/>
  <text x="30" y="45" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{BLUE}">通用 API 调用</text>
  <text x="30" y="80" font-family="ui-monospace,monospace" font-size="17" fill="{T}">lark-cli api GET /open-apis/calendar/v4/calendars</text>
  <text x="30" y="112" font-family="ui-monospace,monospace" font-size="17" fill="{T}">lark-cli api POST /open-apis/im/v1/messages</text>
  <text x="30" y="144" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TD}">免签名 · 免 token 刷新 · 匹配官方 OpenAPI 文档</text>
</g>

<g transform="translate(62, 400)">
  <rect x="0" y="0" width="900" height="160" rx="18" fill="{W}" stroke="{PURPLE}" stroke-width="2"/>
  <text x="30" y="45" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{PURPLE}">AI Agent Skills</text>
  <text x="30" y="80" font-family="ui-monospace,monospace" font-size="17" fill="{T}">npx skills add larksuite/cli -s lark-calendar -y</text>
  <text x="30" y="112" font-family="ui-monospace,monospace" font-size="17" fill="{T}">npx skills add larksuite/cli -s lark-im -y</text>
  <text x="30" y="144" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TD}">每个 skill 封装领域工作流 · AI 自动学会用飞书</text>
</g>

<g transform="translate(62, 600)">
  <rect x="0" y="0" width="900" height="120" rx="18" fill="{W}" stroke="{TEAL}" stroke-width="2"/>
  <text x="30" y="40" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{TEAL}">实用小功能</text>
  <text x="30" y="75" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{T}">--page-all 自动翻页 · --jq JSON 过滤 · --dry-run 预览</text>
  <text x="30" y="102" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{T}">--format pretty / table / csv · --as bot / user 身份切换</text>
</g>

<g transform="translate(62, 800)">
  <rect x="0" y="0" width="900" height="60" rx="14" fill="{BLUEL}"/>
  <text x="28" y="36" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{BLUE}">npm install -g @larksuiteo/cli</text>
  <text x="700" y="36" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">一行安装 · 开箱即用</text>
</g>
''')

def card_banner():
    return svg_wrap(1792, 1024, f'''
<text x="896" y="280" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="60" font-weight="400" fill="{TD}" letter-spacing="3">飞书</text>
<text x="896" y="460" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="200" font-weight="900" fill="{BLUE}" letter-spacing="-6">CLI</text>
<text x="896" y="560" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="34" fill="{TD}">一行命令管理全部飞书 API · 开发者效率神器</text>

<g transform="translate(396, 640)">
  <rect x="0" y="0" width="1000" height="80" rx="40" fill="{W}" stroke="{BLUE}" stroke-width="2"/>
  <text x="500" y="50" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="30" font-weight="700" fill="{BLUE}">npm i -g @larksuiteo/cli · 开箱即用</text>
</g>

<g transform="translate(200, 780)">
  <rect x="0" y="0" width="200" height="48" rx="24" fill="{BLUEL}"/><text x="100" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" font-weight="600" fill="{BLUE}">日历会议</text>
  <rect x="230" y="0" width="200" height="48" rx="24" fill="{TEALL}"/><text x="330" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" font-weight="600" fill="{TEAL}">即时通讯</text>
  <rect x="460" y="0" width="200" height="48" rx="24" fill="{PURPLEL}"/><text x="560" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" font-weight="600" fill="{PURPLE}">云文档</text>
  <rect x="690" y="0" width="200" height="48" rx="24" fill="{ORANGEL}"/><text x="790" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" font-weight="600" fill="{ORANGE}">多维表格</text>
  <rect x="920" y="0" width="200" height="48" rx="24" fill="{GREENL}"/><text x="1020" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" font-weight="600" fill="{GREEN}">邮箱</text>
  <rect x="1150" y="0" width="200" height="48" rx="24" fill="{BLUEL}"/><text x="1250" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" font-weight="600" fill="{BLUE}">通讯录</text>
  <rect x="1380" y="0" width="200" height="48" rx="24" fill="{TEALL}"/><text x="1480" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" font-weight="600" fill="{TEAL}">审批考勤</text>
</g>

<text x="896" y="960" text-anchor="middle" font-family="ui-monospace,monospace" font-size="18" fill="{TL}">github.com/larksuite/cli · Apache-2.0 开源 · 20+ Agent Skills</text>
''')

if __name__ == "__main__":
    cards = [
        ("lark-cli-square", card_square()),
        ("lark-cli-card-1", card_1()),
        ("lark-cli-card-2", card_2()),
        ("lark-cli-banner", card_banner()),
    ]
    for name, svg in cards:
        svg_path = os.path.join(ROOT, f"{name}.svg")
        png_path = os.path.join(ROOT, f"{name}.png")
        with open(svg_path, "w") as f:
            f.write(svg)
        w = 1792 if "banner" in name else 1024
        subprocess.run(["inkscape", svg_path, "-o", png_path, "-w", str(w), "-h", "1024"], check=True, capture_output=True)
        sz = os.path.getsize(png_path) // 1024
        print(f"  ✓ {name}.png ({sz} KB)")
    print("Done! 4 cards regenerated.")
