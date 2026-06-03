#!/usr/bin/env python3
"""Generate light-style cards for OpenClaw × Feishu (1024x1024 + 1792x1024 banner)."""
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
ROSE = "#F43F5E"
ROSEL = "#FFE4E6"
LOGO = '''<g transform="translate(36,0) scale(0.65)">
  <path d="M60 10 C30 10 15 35 15 55 C15 75 30 95 45 100 L45 110 L55 110 L55 100 C55 100 60 102 65 100 L65 110 L75 110 L75 100 C90 95 105 75 105 55 C105 35 90 10 60 10Z" fill="url(#lobsterG)"/>
  <path d="M20 45 C5 40 0 50 5 60 C10 70 20 65 25 55 C28 48 25 45 20 45Z" fill="url(#lobsterG)"/>
  <path d="M100 45 C115 40 120 50 115 60 C110 70 100 65 95 55 C92 48 95 45 100 45Z" fill="url(#lobsterG)"/>
  <path d="M45 15 Q35 5 30 8" stroke="#ff4d4d" stroke-width="3" stroke-linecap="round"/>
  <path d="M75 15 Q85 5 90 8" stroke="#ff4d4d" stroke-width="3" stroke-linecap="round"/>
  <circle cx="45" cy="35" r="6" fill="#050810"/><circle cx="75" cy="35" r="6" fill="#050810"/>
  <circle cx="46" cy="34" r="2.5" fill="#00e5cc"/><circle cx="76" cy="34" r="2.5" fill="#00e5cc"/>
</g>'''

LOGO_SMALL = '''<g transform="translate(18,0) scale(0.25)">
  <path d="M60 10 C30 10 15 35 15 55 C15 75 30 95 45 100 L45 110 L55 110 L55 100 C55 100 60 102 65 100 L65 110 L75 110 L75 100 C90 95 105 75 105 55 C105 35 90 10 60 10Z" fill="url(#lobsterG)"/>
  <path d="M20 45 C5 40 0 50 5 60 C10 70 20 65 25 55 C28 48 25 45 20 45Z" fill="url(#lobsterG)"/>
  <path d="M100 45 C115 40 120 50 115 60 C110 70 100 65 95 55 C92 48 95 45 100 45Z" fill="url(#lobsterG)"/>
  <path d="M45 15 Q35 5 30 8" stroke="#ff4d4d" stroke-width="3" stroke-linecap="round"/>
  <path d="M75 15 Q85 5 90 8" stroke="#ff4d4d" stroke-width="3" stroke-linecap="round"/>
  <circle cx="45" cy="35" r="6" fill="#050810"/><circle cx="75" cy="35" r="6" fill="#050810"/>
  <circle cx="46" cy="34" r="2.5" fill="#00e5cc"/><circle cx="76" cy="34" r="2.5" fill="#00e5cc"/>
</g>'''

def bg(w, h):
    return f'<rect width="{w}" height="{h}" fill="url(#bgG)"/><circle cx="{w*0.08}" cy="{h*0.08}" r="60" fill="{BLUEL}" opacity="0.5"/><circle cx="{w*0.92}" cy="{h*0.12}" r="50" fill="{PURPLEL}" opacity="0.4"/><circle cx="{w*0.08}" cy="{h*0.88}" r="70" fill="{TEALL}" opacity="0.3"/><circle cx="{w*0.92}" cy="{h*0.78}" r="80" fill="{ORANGEL}" opacity="0.3"/>'

def svg_wrap(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
<defs><linearGradient id="bgG" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{C}"/><stop offset="100%" stop-color="{C2}"/></linearGradient>
<linearGradient id="lobsterG" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#ff4d4d"/><stop offset="100%" stop-color="#cc2222"/></linearGradient></defs>
{bg(w, h)}
{body}
</svg>'''

def card_square():
    return svg_wrap(1024, 1024, f'''
<rect x="62" y="60" width="900" height="900" rx="40" fill="{W}" opacity="0.7"/>
<g transform="translate(452, 95)">{LOGO}</g>
<text x="512" y="260" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="60" font-weight="400" fill="{TD}" letter-spacing="2">OpenClaw</text>
<text x="512" y="460" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="190" font-weight="900" fill="{BLUE}" letter-spacing="-6">× 飞书</text>
<text x="512" y="560" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="38" fill="{TD}">AI 个人助手 · 直接接入飞书</text>
<g transform="translate(142, 650)">
  <rect x="0" y="0" width="740" height="70" rx="35" fill="{BLUEL}"/>
  <text x="370" y="44" text-anchor="middle" font-family="ui-monospace,monospace" font-size="26" font-weight="700" fill="{BLUE}">openclaw channels login --channel feishu</text>
</g>
<rect x="162" y="750" width="700" height="50" rx="25" fill="{BLUEL}"/>
<text x="512" y="782" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{BLUE}">npm i -g openclaw · 两步开通 · 开源免费</text>
<text x="512" y="860" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TL}">消息 · 文档 · 多维表格 · 日历 · 任务 · 流式输出</text>
<text x="512" y="930" text-anchor="middle" font-family="ui-monospace,monospace" font-size="17" fill="{TL}">openclaw.ai · MIT License</text>''')

def card_1():
    features = [
        ("messages", "消息 💬", "读写私聊/群聊 · 回复线程 · 搜索 · 文件下载", BLUE, BLUEL),
        ("docs", "文档 📄", "创建 · 更新 · 读取飞书文档", TEAL, TEALL),
        ("base", "多维表格 📊", "管理 Base · 表 · 字段 · 记录 · 视图", PURPLE, PURPLEL),
        ("sheets", "电子表格 📈", "创建 · 编辑 · 查看 · 公式配置", ORANGE, ORANGEL),
        ("calendar", "日历 📅", "日程管理 · 参会人 · 忙闲查询", GREEN, GREENL),
        ("tasks", "任务 ✅", "创建/查询/更新 · 子任务 · 评论", ROSE, ROSEL),
    ]
    items = ""
    for i, (key, name, desc, color, light) in enumerate(features):
        y = 165 + i * 108
        items += f'''
<g transform="translate(62, {y})">
  <rect x="0" y="0" width="900" height="88" rx="16" fill="{light}"/>
  <text x="30" y="40" font-family="ui-monospace,monospace" font-size="20" font-weight="600" fill="{color}">{key}</text>
  <text x="30" y="70" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{T}">{name}</text>
  <text x="380" y="52" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" fill="{TD}">{desc}</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
<text x="512" y="90" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="42" font-weight="800" fill="{T}">飞书官方插件</text>
<text x="512" y="132" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">@larksuite/openclaw-lark · 字节飞书团队维护</text>
{items}
<text x="512" y="850" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TL}">+ 交互式卡片 · 流式输出 · 权限策略 · 多账号</text>
<g transform="translate(162, 890)">
  <rect x="0" y="0" width="700" height="50" rx="25" fill="{BLUE}" opacity="0.1"/>
  <text x="350" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" font-weight="600" fill="{BLUE}">DM / 群聊双模式 · streaming · requireMention</text>
</g>
''')

def card_2():
    return svg_wrap(1024, 1024, f'''
<text x="512" y="90" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="42" font-weight="800" fill="{T}">两步开通</text>
<text x="512" y="132" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">WebSocket 直连 · 无需公网服务器</text>

<g transform="translate(62, 200)">
  <rect x="0" y="0" width="900" height="160" rx="20" fill="{W}" stroke="{BLUE}" stroke-width="2"/>
  <text x="30" y="45" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{BLUE}">Step 1 · 安装 OpenClaw</text>
  <text x="30" y="85" font-family="ui-monospace,monospace" font-size="20" fill="{T}">npm install -g openclaw</text>
  <text x="30" y="120" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">支持 macOS / Windows / Linux</text>
  <text x="30" y="146" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">或一键脚本 curl -fsSL https://openclaw.ai/install.sh | bash</text>
</g>

<g transform="translate(62, 410)">
  <rect x="0" y="0" width="900" height="160" rx="20" fill="{W}" stroke="{PURPLE}" stroke-width="2"/>
  <text x="30" y="45" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{PURPLE}">Step 2 · 飞书登录</text>
  <text x="30" y="85" font-family="ui-monospace,monospace" font-size="20" fill="{T}">openclaw channels login --channel feishu</text>
  <text x="30" y="120" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">OAuth 授权 · 扫码绑定</text>
  <text x="30" y="146" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">浏览器登录后自动配置完成</text>
</g>

<g transform="translate(62, 620)">
  <rect x="0" y="0" width="900" height="120" rx="20" fill="{W}" stroke="{TEAL}" stroke-width="2"/>
  <text x="30" y="40" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{TEAL}">可选 · 飞书官方插件</text>
  <text x="30" y="80" font-family="ui-monospace,monospace" font-size="20" fill="{T}">npm install @larksuite/openclaw-lark</text>
  <text x="30" y="108" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">更多 API 支持 · 文档 / 多维表格 / 日历 / 任务</text>
</g>

<g transform="translate(62, 810)">
  <rect x="0" y="0" width="900" height="70" rx="16" fill="{BLUEL}"/>
  <text x="30" y="44" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="600" fill="{BLUE}">openclaw gateway restart  →  立即生效 🚀</text>
</g>
''')

def card_banner():
    return svg_wrap(1792, 1024, f'''
<g transform="translate(30, 30)">{LOGO_SMALL}</g>
<text x="896" y="250" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="56" font-weight="400" fill="{TD}" letter-spacing="3">OpenClaw</text>
<text x="896" y="460" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="220" font-weight="900" fill="{BLUE}" letter-spacing="-7">× 飞书</text>
<text x="896" y="560" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="40" fill="{TD}">AI 个人助手 · 直接接入飞书 · 两步开通</text>

<g transform="translate(296, 650)">
  <rect x="0" y="0" width="1200" height="80" rx="40" fill="{BLUEL}"/>
  <text x="600" y="52" text-anchor="middle" font-family="ui-monospace,monospace" font-size="32" font-weight="700" fill="{BLUE}">openclaw channels login --channel feishu</text>
</g>

<g transform="translate(100, 800)">
  <rect x="0" y="0" width="220" height="50" rx="25" fill="{BLUEL}"/><text x="110" y="34" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{BLUE}">消息</text>
  <rect x="250" y="0" width="220" height="50" rx="25" fill="{TEALL}"/><text x="360" y="34" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{TEAL}">文档</text>
  <rect x="500" y="0" width="220" height="50" rx="25" fill="{PURPLEL}"/><text x="610" y="34" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{PURPLE}">多维表格</text>
  <rect x="750" y="0" width="220" height="50" rx="25" fill="{ORANGEL}"/><text x="860" y="34" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{ORANGE}">日历</text>
  <rect x="1000" y="0" width="220" height="50" rx="25" fill="{GREENL}"/><text x="1110" y="34" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{GREEN}">任务</text>
  <rect x="1250" y="0" width="220" height="50" rx="25" fill="{ROSEL}"/><text x="1360" y="34" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{ROSE}">流式输出</text>
</g>

<text x="896" y="960" text-anchor="middle" font-family="ui-monospace,monospace" font-size="22" fill="{TL}">openclaw.ai · npm i -g openclaw · MIT License · 30+ 模型平台</text>
''')

if __name__ == "__main__":
    cards = [
        ("openclaw-square", card_square()),
        ("openclaw-card-1", card_1()),
        ("openclaw-card-2", card_2()),
        ("openclaw-banner", card_banner()),
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