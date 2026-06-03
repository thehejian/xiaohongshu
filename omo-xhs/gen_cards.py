#!/usr/bin/env python3
"""Generate dark-style cards for oh-my-openagent (1024x1024 + 1792x1024 banner)."""
import subprocess, os
ROOT = os.path.dirname(os.path.abspath(__file__))

BG = "#0A0A14"
BG_P = "#15151F"
INK = "#F5F5F7"
INK_D = "#A1A1AA"
INK_M = "#71717A"
PURPLE = "#8B5CF6"
PURPLE_L = "#C4B5FD"
BLUE = "#3B82F6"
CYAN = "#06B6D4"
TEAL = "#14B8A6"
ORANGE = "#F97316"
GREEN = "#10B981"
RED = "#EF4444"
GOLD = "#FBBF24"
LINE = "#27272A"

FONT = "PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif"
FMONO = "SF Mono, JetBrains Mono, IBM Plex Mono, Menlo, Consolas, monospace"

def defs_block():
    return f'''<defs>
<linearGradient id="bgG" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#0D0D1A"/>
  <stop offset="100%" stop-color="{BG}"/>
</linearGradient>
<linearGradient id="accentG" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="{PURPLE}"/>
  <stop offset="100%" stop-color="{ORANGE}"/>
</linearGradient>
<linearGradient id="accentG2" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="{PURPLE}"/>
  <stop offset="100%" stop-color="{CYAN}"/>
</linearGradient>
<filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
  <feGaussianBlur stdDeviation="8" result="blur"/>
  <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
<filter id="shadow">
  <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#000" flood-opacity="0.4"/>
</filter>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
  <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1A1A2E" stroke-width="0.5"/>
</pattern>
</defs>'''

def bg_rects(w, h):
    return f'<rect width="{w}" height="{h}" fill="url(#bgG)"/><rect width="{w}" height="{h}" fill="url(#grid)"/><circle cx="{w*0.05}" cy="{h*0.05}" r="{w*0.12}" fill="{PURPLE}" opacity="0.08"/><circle cx="{w*0.95}" cy="{h*0.95}" r="{w*0.15}" fill="{ORANGE}" opacity="0.06"/>'

def svg_wrap(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
{defs_block()}
{bg_rects(w, h)}
{body}
</svg>'''

def chip(text, x, y, color):
    return f'<rect x="{x}" y="{y}" width="150" height="36" rx="18" fill="{color}" opacity="0.15"/><text x="{x+75}" y="{y+24}" text-anchor="middle" font-family="{FONT}" font-size="14" font-weight="600" fill="{color}">{text}</text>'

def card_square():
    return svg_wrap(1024, 1024, f'''
<rect x="62" y="80" width="900" height="864" rx="32" fill="{BG_P}" filter="url(#shadow)" stroke="{LINE}" stroke-width="1"/>

<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="28" fill="{INK_D}" letter-spacing="3" font-weight="300">OH MY</text>
<text x="512" y="340" text-anchor="middle" font-family="{FONT}" font-size="150" font-weight="900" fill="url(#accentG)" letter-spacing="-5" filter="url(#glow)">OmO</text>
<text x="512" y="420" text-anchor="middle" font-family="{FONT}" font-size="22" fill="{INK_D}">一个命令拉起 AI 团队</text>

<rect x="250" y="490" width="524" height="55" rx="28" fill="none" stroke="url(#accentG2)" stroke-width="2"/>
<text x="512" y="525" text-anchor="middle" font-family="{FMONO}" font-size="18" font-weight="600" fill="{PURPLE_L}">bunx oh-my-openagent install</text>

<text x="512" y="620" text-anchor="middle" font-family="{FONT}" font-size="20" fill="{INK_D}">然后输入  ultrawork</text>
<text x="512" y="660" text-anchor="middle" font-family="{FONT}" font-size="16" fill="{INK_M}">11 个 Agent · Team Mode · 54+ Hooks</text>

{chip("Cursor 退订", 160, 720, ORANGE)}
{chip("Claude Code 替代", 340, 720, PURPLE)}
{chip("一夜重构 SaaS", 520, 720, CYAN)}
{chip("开源免费", 700, 720, GREEN)}

<text x="512" y="870" text-anchor="middle" font-family="{FMONO}" font-size="15" fill="{INK_M}">github.com/code-yeongyu/oh-my-openagent</text>
''')

def card_1():
    agents = [
        ("Sisyphus", "总指挥 · 规划+委派+驱动", "Opus/Kimi/GLM", PURPLE),
        ("Hephaestus", "深度执行 · 自主探索+执行", "GPT-5.5", ORANGE),
        ("Prometheus", "策略规划 · 访谈式需求分析", "Opus/Kimi/GLM", BLUE),
        ("Oracle", "策略分析 · 架构决策", "GPT-5.5 xhigh", CYAN),
        ("Librarian", "知识管理 · 上下文维护", "Claude/GPT", TEAL),
        ("Explore", "调研探索 · 代码库扫描", "Claude/GPT", GREEN),
    ]
    items = ""
    for i, (name, role, model, color) in enumerate(agents):
        y = 170 + i * 95
        items += f'''
<g transform="translate(62, {y})">
  <rect x="0" y="0" width="900" height="80" rx="14" fill="{BG}" stroke="{color}" stroke-width="1" stroke-opacity="0.3"/>
  <text x="25" y="33" font-family="{FMONO}" font-size="17" font-weight="700" fill="{color}">{name}</text>
  <text x="25" y="62" font-family="{FONT}" font-size="16" fill="{INK_D}">{role}</text>
  <text x="750" y="47" font-family="{FMONO}" font-size="15" fill="{INK_M}">{model}</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
<rect x="62" y="50" width="900" height="924" rx="32" fill="{BG_P}" filter="url(#shadow)" stroke="{LINE}" stroke-width="1"/>
<text x="512" y="110" text-anchor="middle" font-family="{FONT}" font-size="32" font-weight="800" fill="{INK}">11 个专业 Agent</text>
<text x="512" y="140" text-anchor="middle" font-family="{FONT}" font-size="18" fill="{INK_D}">各配最优模型 · 自动编排</text>
{items}
<text x="512" y="860" text-anchor="middle" font-family="{FONT}" font-size="15" fill="{INK_M}">Anthropic 因为 OmO 封了 OpenCode</text>
''')

def card_2():
    return svg_wrap(1024, 1024, f'''
<rect x="62" y="50" width="900" height="924" rx="32" fill="{BG_P}" filter="url(#shadow)" stroke="{LINE}" stroke-width="1"/>
<text x="512" y="110" text-anchor="middle" font-family="{FONT}" font-size="32" font-weight="800" fill="{INK}">核心能力</text>

<g transform="translate(90, 170)">
  <rect x="0" y="0" width="400" height="180" rx="18" fill="{BG}" stroke="{PURPLE}" stroke-width="1" stroke-opacity="0.4"/>
  <text x="25" y="40" font-family="{FONT}" font-size="22" font-weight="700" fill="{PURPLE_L}">Team Mode</text>
  <text x="25" y="72" font-family="{FONT}" font-size="16" fill="{INK_D}">1 主控 + 8 并行成员</text>
  <text x="25" y="100" font-family="{FONT}" font-size="16" fill="{INK_D}">hyperplan：5 批评家</text>
  <text x="25" y="128" font-family="{FONT}" font-size="16" fill="{INK_D}">security-research</text>
  <text x="25" y="156" font-family="{FONT}" font-size="16" fill="{INK_D}">3 猎人 + 2 PoC 并行</text>

  <rect x="430" y="0" width="400" height="180" rx="18" fill="{BG}" stroke="{ORANGE}" stroke-width="1" stroke-opacity="0.4"/>
  <text x="455" y="40" font-family="{FONT}" font-size="22" font-weight="700" fill="{ORANGE}">ultrawork</text>
  <text x="455" y="72" font-family="{FONT}" font-size="16" fill="{INK_D}">输入 ultrawork / ulw</text>
  <text x="455" y="100" font-family="{FONT}" font-size="16" fill="{INK_D}">所有 Agent 激活</text>
  <text x="455" y="128" font-family="{FONT}" font-size="16" fill="{INK_D}">不达目标不停止</text>
  <text x="455" y="156" font-family="{FONT}" font-size="16" fill="{INK_D}">Ralph 自动循环</text>
</g>

<g transform="translate(90, 390)">
  <rect x="0" y="0" width="400" height="180" rx="18" fill="{BG}" stroke="{CYAN}" stroke-width="1" stroke-opacity="0.4"/>
  <text x="25" y="40" font-family="{FONT}" font-size="22" font-weight="700" fill="{CYAN}">精准编辑</text>
  <text x="25" y="72" font-family="{FONT}" font-size="16" fill="{INK_D}">LINE#ID 哈希锚定</text>
  <text x="25" y="100" font-family="{FONT}" font-size="16" fill="{INK_D}">LSP 集成 · AST-Grep</text>
  <text x="25" y="128" font-family="{FONT}" font-size="16" fill="{INK_D}">25 种语言模式搜索</text>
  <text x="25" y="156" font-family="{FONT}" font-size="16" fill="{INK_D}">IDE 级精度</text>

  <rect x="430" y="0" width="400" height="180" rx="18" fill="{BG}" stroke="{GREEN}" stroke-width="1" stroke-opacity="0.4"/>
  <text x="455" y="40" font-family="{FONT}" font-size="22" font-weight="700" fill="{GREEN}">生态兼容</text>
  <text x="455" y="72" font-family="{FONT}" font-size="16" fill="{INK_D}">Claude Code 全插件兼容</text>
  <text x="455" y="100" font-family="{FONT}" font-size="16" fill="{INK_D}">54+ Lifecycle Hooks</text>
  <text x="455" y="128" font-family="{FONT}" font-size="16" fill="{INK_D}">内置 MCP 开箱即用</text>
  <text x="455" y="156" font-family="{FONT}" font-size="16" fill="{INK_D}">规则注入 AGENTS.md</text>
</g>

<g transform="translate(90, 620)">
  <rect x="0" y="0" width="844" height="60" rx="14" fill="{PURPLE}" opacity="0.1"/>
  <text x="422" y="36" text-anchor="middle" font-family="{FMONO}" font-size="18" font-weight="600" fill="{PURPLE_L}">bunx oh-my-openagent install → ultrawork</text>
</g>

<text x="512" y="870" text-anchor="middle" font-family="{FONT}" font-size="15" fill="{INK_M}">开源免费 · SUL-1.0 协议</text>
''')

def card_banner():
    return svg_wrap(1792, 1024, f'''
<text x="896" y="220" text-anchor="middle" font-family="{FONT}" font-size="40" font-weight="300" fill="{INK_D}" letter-spacing="3">OH MY</text>
<text x="896" y="400" text-anchor="middle" font-family="{FONT}" font-size="200" font-weight="900" fill="url(#accentG)" letter-spacing="-6" filter="url(#glow)">OmO</text>
<text x="896" y="490" text-anchor="middle" font-family="{FONT}" font-size="28" fill="{INK_D}">一个命令拉起 AI 团队</text>

<rect x="496" y="550" width="800" height="60" rx="30" fill="none" stroke="url(#accentG2)" stroke-width="2"/>
<text x="896" y="587" text-anchor="middle" font-family="{FMONO}" font-size="22" font-weight="600" fill="{PURPLE_L}">bunx oh-my-openagent install</text>

<g transform="translate(280, 670)">
  <rect x="0" y="0" width="200" height="46" rx="23" fill="{PURPLE}" opacity="0.15"/><text x="100" y="30" text-anchor="middle" font-family="{FONT}" font-size="17" font-weight="600" fill="{PURPLE_L}">11 个 Agent</text>
  <rect x="230" y="0" width="200" height="46" rx="23" fill="{ORANGE}" opacity="0.15"/><text x="330" y="30" text-anchor="middle" font-family="{FONT}" font-size="17" font-weight="600" fill="{ORANGE}">Team Mode</text>
  <rect x="460" y="0" width="200" height="46" rx="23" fill="{CYAN}" opacity="0.15"/><text x="560" y="30" text-anchor="middle" font-family="{FONT}" font-size="17" font-weight="600" fill="{CYAN}">ultrawork</text>
  <rect x="690" y="0" width="200" height="46" rx="23" fill="{TEAL}" opacity="0.15"/><text x="790" y="30" text-anchor="middle" font-family="{FONT}" font-size="17" font-weight="600" fill="{TEAL}">Hash 编辑</text>
  <rect x="920" y="0" width="200" height="46" rx="23" fill="{GREEN}" opacity="0.15"/><text x="1020" y="30" text-anchor="middle" font-family="{FONT}" font-size="17" font-weight="600" fill="{GREEN}">LSP 集成</text>
  <rect x="1150" y="0" width="200" height="46" rx="23" fill="{PURPLE}" opacity="0.15"/><text x="1250" y="30" text-anchor="middle" font-family="{FONT}" font-size="17" font-weight="600" fill="{PURPLE_L}">开源免费</text>
</g>

<g transform="translate(200, 770)">
  <text x="0" y="0" font-family="{FONT}" font-size="18" fill="{INK_D}">Anthropic 因为它封了 OpenCode · 开源免费 · Claude Code 全插件兼容</text>
</g>

<text x="896" y="900" text-anchor="middle" font-family="{FMONO}" font-size="16" fill="{INK_M}">github.com/code-yeongyu/oh-my-openagent</text>
''')

if __name__ == "__main__":
    cards = [
        ("omo-square", card_square()),
        ("omo-card-1", card_1()),
        ("omo-card-2", card_2()),
        ("omo-banner", card_banner()),
    ]
    for name, svg in cards:
        svg_path = os.path.join(ROOT, f"{name}.svg")
        png_path = os.path.join(ROOT, f"{name}.png")
        with open(svg_path, "w") as f:
            f.write(svg)
        w = 1792 if "banner" in name else 1024
        subprocess.run(["inkscape", svg_path, "-o", png_path, "-w", str(w), "-h", "1024"], check=True, capture_output=True)
        sz = os.path.getsize(png_path) // 1024
        print(f"  {name}.png ({sz} KB)")
    print("Done! 4 cards regenerated.")