#!/usr/bin/env python3
"""Generate v3.16.1 update announcement cards for CC Switch (1024x1024 + 1792x1024 banner)."""
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
RED = "#EF4444"
REDL = "#FEE2E2"

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
<text x="512" y="200" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="120" font-weight="900" fill="{T}" letter-spacing="-4">CC</text>
<text x="512" y="340" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="140" font-weight="900" fill="{TEAL}" letter-spacing="-5">Switch</text>

<g transform="translate(162, 420)">
  <rect x="0" y="0" width="700" height="80" rx="40" fill="{REDL}" stroke="{RED}" stroke-width="2"/>
  <text x="350" y="50" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="32" font-weight="800" fill="{RED}">v3.16.1 史诗级更新</text>
</g>

<text x="512" y="580" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" font-weight="700" fill="{T}">Codex OAuth 保留 🔑</text>
<text x="512" y="620" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">第三方 API + 官方登录同时用</text>

<g transform="translate(120, 700)">
  <rect x="0" y="0" width="200" height="44" rx="22" fill="{TEALL}"/><text x="100" y="29" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="600" fill="{TEAL}">Chat 路由修复</text>
  <rect x="220" y="0" width="200" height="44" rx="22" fill="{BLUEL}"/><text x="320" y="29" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="600" fill="{BLUE}">模型目录加固</text>
  <rect x="440" y="0" width="200" height="44" rx="22" fill="{PURPLEL}"/><text x="540" y="29" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="600" fill="{PURPLE}">热切换稳定</text>
  <rect x="660" y="0" width="200" height="44" rx="22" fill="{GREENL}"/><text x="760" y="29" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" font-weight="600" fill="{GREEN}">23 commits</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="ui-monospace,monospace" font-size="16" fill="{TL}">brew install --cask cc-switch</text>'''
    return svg_wrap(1024, 1024, b)

# ── Card 2: Codex OAuth Preservation (1024x1024) ──
def card_1():
    return svg_wrap(1024, 1024, f'''
<text x="512" y="90" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="38" font-weight="800" fill="{T}">🔑 Codex OAuth 保留</text>
<text x="512" y="130" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">切换供应商不掉登录</text>

<g transform="translate(62, 180)">
  <rect x="0" y="0" width="900" height="60" rx="14" fill="{REDL}"/>
  <text x="450" y="36" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="700" fill="{RED}">以前：第三方 Key 写入 auth.json → 覆盖官方 OAuth</text>
</g>

<g transform="translate(62, 270)">
  <rect x="0" y="0" width="900" height="280" rx="18" fill="{W}" stroke="{TEAL}" stroke-width="2"/>
  <text x="450" y="50" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" font-weight="700" fill="{TEAL}">v3.16.1 改进</text>
  
  <g transform="translate(40, 90)">
    <circle cx="14" cy="14" r="10" fill="{GREEN}"/>
    <text x="40" y="20" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{T}">第三方 token → config.toml</text>
  </g>
  <g transform="translate(40, 135)">
    <circle cx="14" cy="14" r="10" fill="{GREEN}"/>
    <text x="40" y="20" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{T}">官方 OAuth 继续留在 auth.json</text>
  </g>
  <g transform="translate(40, 180)">
    <circle cx="14" cy="14" r="10" fill="{GREEN}"/>
    <text x="40" y="20" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{T}">远程操作 / 官方插件不受影响</text>
  </g>
  <g transform="translate(40, 225)">
    <circle cx="14" cy="14" r="10" fill="{GREEN}"/>
    <text x="40" y="20" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{T}">默认关闭，兼容旧行为</text>
  </g>
</g>

<g transform="translate(62, 580)">
  <rect x="0" y="0" width="900" height="60" rx="14" fill="{TEALL}"/>
  <text x="450" y="36" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{TEAL}">设置 → Codex 应用增强 → 开启官方认证保留</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">同时保留官方订阅权益 + 第三方供应商价格优势</text>
<text x="512" y="900" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TL}">支持 Claude Code / Claude Desktop / Codex / Gemini CLI / OpenCode / OpenClaw / Hermes</text>
<text x="512" y="960" text-anchor="middle" font-family="ui-monospace,monospace" font-size="16" fill="{TL}">github.com/farion1231/cc-switch</text>
''')

# ── Card 3: Bug Fixes & Stability (1024x1024) ──
def card_2():
    fixes = [
        (TEAL, TEALL, "Codex 模型目录", "不再被静默清空\n以数据库为真相来源，live 回填/切换/恢复不丢"),
        (BLUE, BLUEL, "Chat 工具/插件路由", "tool_search / 自定义工具完整恢复\n流式输出原生事件"),
        (PURPLE, PURPLEL, "热切换更稳", "串行锁定 + PROXY_MANAGED 占位符\n防止配置被覆盖"),
        (GREEN, GREENL, "Claude Desktop 修复", "官方供应商添加不再报错"),
    ]
    items = ""
    for i, (color, light, title, desc) in enumerate(fixes):
        y = 180 + i * 150
        items += f'''
<g transform="translate(62, {y})">
  <rect x="0" y="0" width="900" height="130" rx="16" fill="{W}" stroke="{color}" stroke-width="1.5"/>
  <text x="30" y="40" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{color}">{title}</text>
  <text x="30" y="80" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{TD}">{desc.replace(chr(10), " · ")}</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
<text x="512" y="90" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="38" font-weight="800" fill="{T}">修复与稳定性</text>
<text x="512" y="130" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">23 commits · 62 files · 尽在 v3.16.1</text>
{items}
''')

# ── Card 4: Additional Fixes (1024x1024) ──
def card_3():
    extras = [
        ("Kimi / Moonshot 工具思考历史", "正确重放 reasoning 与 tool-call 上下文", ORANGE, ORANGEL),
        ("Windows 版本探测修复", '乱码与误判修复，不再显示"已安装但无法运行"', PURPLE, PURPLEL),
        ("余额 / Coding Plan 查询", "按 app 解析凭据，不再跨应用错用", TEAL, TEALL),
        ("Codex CLI 发现与模板兜底", "多平台安装位置 + GPT-5.5 模型兜底", BLUE, BLUEL),
        ("诊断错误更完整", "返回含 provider/model/endpoint/错误码的 JSON", GREEN, GREENL),
    ]
    items = ""
    for i, (title, desc, color, light) in enumerate(extras):
        y = 160 + i * 120
        items += f'''
<g transform="translate(62, {y})">
  <rect x="0" y="0" width="900" height="90" rx="14" fill="{light}"/>
  <text x="30" y="36" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="600" fill="{T}">{title}</text>
  <text x="30" y="66" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" fill="{TD}">{desc}</text>
  <rect x="850" y="28" width="28" height="32" rx="6" fill="{color}" opacity="0.2"/>
</g>'''
    return svg_wrap(1024, 1024, f'''
<text x="512" y="80" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="38" font-weight="800" fill="{T}">更多修复 & 支持</text>
{items}
<text x="512" y="960" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TL}">7 个工具统一管理 · MIT 开源 · brew install --cask cc-switch</text>
''')

# ── Card 5: Banner (1792x1024) ──
def card_banner():
    return svg_wrap(1792, 1024, f'''
<text x="896" y="220" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="160" font-weight="900" fill="{T}" letter-spacing="-6">CC</text>
<text x="896" y="400" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="180" font-weight="900" fill="{TEAL}" letter-spacing="-6">Switch</text>

<g transform="translate(396, 480)">
  <rect x="0" y="0" width="1000" height="80" rx="40" fill="{REDL}" stroke="{RED}" stroke-width="2"/>
  <text x="500" y="50" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="34" font-weight="800" fill="{RED}">v3.16.1 史诗级更新</text>
</g>

<text x="896" y="640" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" fill="{TD}">Codex OAuth 保留 · Chat 路由修复 · 模型目录加固 · 23 commits</text>

<g transform="translate(200, 730)">
  <rect x="0" y="0" width="240" height="48" rx="24" fill="{TEALL}"/><text x="120" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" font-weight="600" fill="{TEAL}">🔑 OAuth 保留</text>
  <rect x="280" y="0" width="240" height="48" rx="24" fill="{BLUEL}"/><text x="400" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" font-weight="600" fill="{BLUE}">🛠️ Chat 路由</text>
  <rect x="560" y="0" width="240" height="48" rx="24" fill="{PURPLEL}"/><text x="680" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" font-weight="600" fill="{PURPLE}">📂 模型目录</text>
  <rect x="840" y="0" width="240" height="48" rx="24" fill="{ORANGEL}"/><text x="960" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" font-weight="600" fill="{ORANGE}">🔄 热切换</text>
  <rect x="1120" y="0" width="240" height="48" rx="24" fill="{GREENL}"/><text x="1240" y="32" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" font-weight="600" fill="{GREEN}">🐛 修复</text>
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
