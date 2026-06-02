#!/usr/bin/env python3
"""Generate 5 cleaner white-style cards for CC Switch (1024x1024 + 1792x1024 banner)."""
import subprocess, os
ROOT = os.path.dirname(os.path.abspath(__file__))

C = "#FAF7F2"
C2 = "#F3F0E8"
W = "#FFFFFF"
T = "#1E293B"
TD = "#64748B"
TL = "#94A3B8"
TEAL = "#0EA5E9"
TEALL = "#E0F2FE"
BLUE = "#3B82F6"
BLUEL = "#DBEAFE"
PURPLE = "#8B5CF6"
PURPLEL = "#EDE9FE"
ORANGE = "#F97316"
ORANGEL = "#FFEDD5"
GREEN = "#10B981"
GREENL = "#D1FAE5"

def bg(w, h):
    return f'<rect width="{w}" height="{h}" fill="url(#bgG)"/><circle cx="{w*0.08}" cy="{h*0.08}" r="60" fill="{TEALL}" opacity="0.4"/><circle cx="{w*0.92}" cy="{h*0.12}" r="50" fill="{PURPLEL}" opacity="0.4"/><circle cx="{w*0.08}" cy="{h*0.88}" r="70" fill="{BLUEL}" opacity="0.3"/><circle cx="{w*0.92}" cy="{h*0.78}" r="80" fill="{ORANGEL}" opacity="0.3"/>'

def svg_wrap(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
<defs><linearGradient id="bgG" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{C}"/><stop offset="100%" stop-color="{C2}"/></linearGradient></defs>
{bg(w, h)}
{body}
</svg>'''

# ── Card 1: Square Cover (1024x1024) ──
def card_square():
    b = f'''
<text x="512" y="240" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="140" font-weight="900" fill="{T}" letter-spacing="-4">CC</text>
<text x="512" y="380" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="160" font-weight="900" fill="{TEAL}" letter-spacing="-5">Switch</text>
<text x="512" y="460" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" fill="{TD}">5 个 AI 编程 CLI · 一个 App 统一管理</text>

<g transform="translate(162, 560)">
  <rect x="0" y="0" width="700" height="80" rx="40" fill="{W}" stroke="{TEAL}" stroke-width="2"/>
  <text x="350" y="50" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" font-weight="700" fill="{TEAL}">告别手改 JSON · 托盘秒切</text>
</g>

<g transform="translate(120, 700)">
  <rect x="0" y="0" width="160" height="44" rx="22" fill="{TEALL}"/><text x="80" y="29" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="600" fill="{TEAL}">Claude Code</text>
  <rect x="180" y="0" width="120" height="44" rx="22" fill="{BLUEL}"/><text x="240" y="29" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="600" fill="{BLUE}">Codex</text>
  <rect x="320" y="0" width="140" height="44" rx="22" fill="{PURPLEL}"/><text x="390" y="29" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="600" fill="{PURPLE}">Gemini CLI</text>
  <rect x="480" y="0" width="130" height="44" rx="22" fill="{ORANGEL}"/><text x="545" y="29" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="600" fill="{ORANGE}">OpenCode</text>
  <rect x="630" y="0" width="130" height="44" rx="22" fill="{GREENL}"/><text x="695" y="29" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="600" fill="{GREEN}">OpenClaw</text>
</g>

<text x="512" y="850" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TL}">50+ 供应商预设 · MCP / Skills 统一管理 · 云同步</text>
<text x="512" y="960" text-anchor="middle" font-family="ui-monospace,monospace" font-size="16" fill="{TL}">github.com/farion1231/cc-switch</text>'''
    return svg_wrap(1024, 1024, b)

# ── Card 2: Pain Point (1024x1024) ──
def card_1():
    tools = [
        ("Claude Code",  "#JSON", BLUE, BLUEL),
        ("Codex",        "config.toml", TEAL, TEALL),
        ("Gemini CLI",   "auth.json", PURPLE, PURPLEL),
        ("OpenCode",     "settings.yaml", ORANGE, ORANGEL),
        ("OpenClaw",     "config.toml", GREEN, GREENL),
    ]
    rows = ""
    for i, (name, conf, color, light) in enumerate(tools):
        y = 210 + i * 80
        rows += f'''
<g transform="translate(62, {y})">
  <rect x="0" y="0" width="900" height="60" rx="14" fill="{light}"/>
  <text x="30" y="36" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{T}">{name}</text>
  <rect x="240" y="15" width="28" height="30" rx="6" fill="{color}" opacity="0.2"/>
  <text x="300" y="36" font-family="ui-monospace,monospace" font-size="19" fill="{color}" font-weight="600">{conf}</text>
  <text x="780" y="36" text-anchor="end" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" fill="{TD}">格式各不同</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
<text x="512" y="90" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="38" font-weight="800" fill="{T}">5 个 CLI · 5 套配置</text>
<text x="512" y="130" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">每次换工具都要手改配置，半天找不到</text>
{rows}
<g transform="translate(62, 630)">
  <rect x="0" y="0" width="900" height="80" rx="18" fill="{W}" stroke="{TEAL}" stroke-width="2"/>
  <text x="450" y="35" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{TEAL}">CC Switch：一次配置，5 个工具通用</text>
  <text x="450" y="62" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">50+ 供应商预设 · 复制 Key 就能用</text>
</g>
''')

# ── Card 3: Features (1024x1024) ──
def card_2():
    feats = [
        ("01", "50+ 供应商预设", "AWS Bedrock · NVIDIA NIM · 各家中转\n复制 Key 就能用", TEAL),
        ("02", "托盘秒切换", "系统托盘一键切换供应商\nClaude Code 支持热切换不重启", BLUE),
        ("03", "用量成本追踪", "跨供应商统计支出 Token\n趋势图表 · 详细请求日志 · 心中有数", PURPLE),
        ("04", "MCP / Skills 统一", "所有工具的 MCP 服务 + Prompts\n一个界面管理，不用到处找", ORANGE),
    ]
    items = ""
    for i, (num, title, desc, color) in enumerate(feats):
        y = 180 + i * 160
        items += f'''
<g transform="translate(62, {y})">
  <circle cx="30" cy="30" r="26" fill="none" stroke="{color}" stroke-width="3"/>
  <text x="30" y="37" text-anchor="middle" font-family="ui-monospace,monospace" font-size="22" font-weight="800" fill="{color}">{num}</text>
  <text x="80" y="30" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="26" font-weight="700" fill="{T}">{title}</text>
  <text x="80" y="70" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">{desc.replace(chr(10), " · ")}</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
<text x="512" y="90" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="38" font-weight="800" fill="{T}">核心能力</text>
{items}
<text x="512" y="960" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TL}">所有功能开源免费 · Tauri 原生 · 跨平台</text>
''')

# ── Card 4: Open Source + Cross Platform (1024x1024) ──
def card_3():
    return svg_wrap(1024, 1024, f'''
<text x="512" y="90" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="38" font-weight="800" fill="{T}">开源免费 · 原生体验</text>
<text x="512" y="130" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">Tauri 2 + Rust · 低内存 · 跨平台</text>

<g transform="translate(62, 200)">
  <rect x="0" y="0" width="430" height="200" rx="18" fill="{W}" stroke="{TEAL}" stroke-width="2"/>
  <text x="215" y="60" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" font-weight="700" fill="{TEAL}">MIT 开源协议</text>
  <text x="215" y="105" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" fill="{T}">永久免费 · 可商用</text>
  <text x="215" y="140" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">社区贡献 · 持续迭代</text>
  <text x="215" y="175" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">SQLite 原子写入</text>

  <rect x="470" y="0" width="430" height="200" rx="18" fill="{W}" stroke="{PURPLE}" stroke-width="2"/>
  <text x="685" y="60" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" font-weight="700" fill="{PURPLE}">云同步</text>
  <text x="685" y="105" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" fill="{T}">Dropbox / iCloud</text>
  <text x="685" y="140" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">坚果云 / WebDAV</text>
  <text x="685" y="175" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">换电脑无感迁移</text>
</g>

<g transform="translate(62, 460)">
  <text x="0" y="0" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="700" fill="{T}">全平台支持</text>
  <g transform="translate(0, 30)">
    <rect x="0" y="0" width="286" height="100" rx="16" fill="{W}" stroke="{BLUE}" stroke-width="1.5"/>
    <text x="143" y="44" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{T}">macOS</text>
    <text x="143" y="72" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TD}">brew install cc-switch</text>
    <rect x="307" y="0" width="286" height="100" rx="16" fill="{W}" stroke="{ORANGE}" stroke-width="1.5"/>
    <text x="450" y="44" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{T}">Windows</text>
    <text x="450" y="72" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TD}">.msi / 便携版</text>
    <rect x="614" y="0" width="286" height="100" rx="16" fill="{W}" stroke="{GREEN}" stroke-width="1.5"/>
    <text x="757" y="44" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{T}">Linux</text>
    <text x="757" y="72" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TD}">.deb / .rpm / AppImage</text>
  </g>
</g>

<g transform="translate(62, 640)">
  <rect x="0" y="0" width="900" height="60" rx="14" fill="{TEALL}"/>
  <text x="28" y="36" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{TEAL}">brew install --cask cc-switch</text>
  <text x="700" y="36" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">开箱即用</text>
</g>
''')

# ── Card 5: Banner (1792x1024) ──
def card_banner():
    return svg_wrap(1792, 1024, f'''
<text x="896" y="260" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="180" font-weight="900" fill="{T}" letter-spacing="-6">CC</text>
<text x="896" y="440" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="200" font-weight="900" fill="{TEAL}" letter-spacing="-6">Switch</text>
<text x="896" y="540" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="34" fill="{TD}">5 个 AI 编程 CLI · 一个 App 统一管理</text>

<g transform="translate(396, 640)">
  <rect x="0" y="0" width="1000" height="80" rx="40" fill="{W}" stroke="{TEAL}" stroke-width="2"/>
  <text x="500" y="50" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="30" font-weight="700" fill="{TEAL}">告别手改 JSON · 托盘秒切 · 开源免费</text>
</g>

<g transform="translate(200, 780)">
  <rect x="0" y="0" width="190" height="48" rx="24" fill="{TEALL}"/><text x="95" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" font-weight="600" fill="{TEAL}">50+ 预设</text>
  <rect x="220" y="0" width="190" height="48" rx="24" fill="{BLUEL}"/><text x="315" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" font-weight="600" fill="{BLUE}">托盘秒切</text>
  <rect x="440" y="0" width="230" height="48" rx="24" fill="{PURPLEL}"/><text x="555" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" font-weight="600" fill="{PURPLE}">MCP / Skills</text>
  <rect x="700" y="0" width="170" height="48" rx="24" fill="{ORANGEL}"/><text x="785" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" font-weight="600" fill="{ORANGE}">云同步</text>
  <rect x="900" y="0" width="190" height="48" rx="24" fill="{GREENL}"/><text x="995" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" font-weight="600" fill="{GREEN}">开源免费</text>
</g>

<text x="896" y="960" text-anchor="middle" font-family="ui-monospace,monospace" font-size="18" fill="{TL}">github.com/farion1231/cc-switch · brew install --cask cc-switch</text>
''')

if __name__ == "__main__":
    cards = [
        ("cc-switch-square", card_square()),
        ("cc-switch-card-1", card_1()),
        ("cc-switch-card-2", card_2()),
        ("cc-switch-card-3", card_3()),
        ("cc-switch-banner", card_banner()),
    ]
    for name, svg in cards:
        svg_path = os.path.join(ROOT, f"{name}.svg")
        png_path = os.path.join(ROOT, f"{name}.png")
        with open(svg_path, "w") as f:
            f.write(svg)
        subprocess.run(["inkscape", svg_path, "-o", png_path, "-w", str(1792 if "banner" in name else 1024), "-h", "1024"], check=True, capture_output=True)
        print(f"  ✓ {name}.png ({os.path.getsize(png_path)//1024} KB)")
    print("Done! 5 cards regenerated.")
