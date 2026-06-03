#!/usr/bin/env python3
"""Generate dark-style cards for CLI-Anything (1024x1024 + 1792x1024 banner)."""
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
  <stop offset="100%" stop-color="{BLUE}"/>
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
    return f'<rect width="{w}" height="{h}" fill="url(#bgG)"/><rect width="{w}" height="{h}" fill="url(#grid)"/><circle cx="{w*0.05}" cy="{h*0.05}" r="{w*0.12}" fill="{PURPLE}" opacity="0.08"/><circle cx="{w*0.95}" cy="{h*0.95}" r="{w*0.15}" fill="{BLUE}" opacity="0.06"/>'

def svg_wrap(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
{defs_block()}
{bg_rects(w, h)}
{body}
</svg>'''

def chip(text, x, y, color):
    return f'<rect x="{x}" y="{y}" width="160" height="40" rx="20" fill="{color}" opacity="0.15"/><text x="{x+80}" y="{y+26}" text-anchor="middle" font-family="{FONT}" font-size="16" font-weight="600" fill="{color}">{text}</text>'

def card_square():
    return svg_wrap(1024, 1024, f'''
<rect x="62" y="80" width="900" height="864" rx="32" fill="{BG_P}" filter="url(#shadow)" stroke="{LINE}" stroke-width="1"/>

<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="32" fill="{INK_D}" letter-spacing="2" font-weight="300">CLI-ANYTHING</text>
<text x="512" y="380" text-anchor="middle" font-family="{FONT}" font-size="130" font-weight="900" fill="url(#accentG)" letter-spacing="-4" filter="url(#glow)">万物皆可 CLI</text>
<text x="512" y="460" text-anchor="middle" font-family="{FONT}" font-size="26" fill="{INK_D}">让 AI 操控任何软件</text>

<rect x="200" y="520" width="624" height="60" rx="30" fill="none" stroke="url(#accentG2)" stroke-width="2"/>
<text x="512" y="557" text-anchor="middle" font-family="{FMONO}" font-size="20" font-weight="600" fill="{PURPLE_L}">11 款软件 · 1628 项测试</text>

{chip("GIMP", 120, 620, PURPLE)}
{chip("Blender", 300, 620, BLUE)}
{chip("Inkscape", 480, 620, CYAN)}
{chip("LibreOffice", 660, 620, TEAL)}
{chip("OBS Studio", 120, 680, ORANGE)}
{chip("Kdenlive", 300, 680, GREEN)}
{chip("Shotcut", 480, 680, PURPLE)}
{chip("Sketch", 660, 680, BLUE)}
{chip("OpenScreen", 120, 740, CYAN)}
{chip("Draw.io", 300, 740, TEAL)}
{chip("Audacity", 480, 740, ORANGE)}
{chip("Zoom", 660, 740, GREEN)}

<text x="512" y="870" text-anchor="middle" font-family="{FMONO}" font-size="15" fill="{INK_M}">github.com/CLI-Anything</text>
''')

def card_1():
    feats = [
        ("01", "真实操控，不是模拟", "直接调用软件后端 API\n无降级无截屏，AI 真实操控软件", PURPLE),
        ("02", "结构化输出", "所有命令支持 --json\nAgent 拿到数据直接读取", BLUE),
        ("03", "7 步构建流水线", "分析 → 设计 → 实现 → 测试\n→ 文档 → 发布，快速封装", CYAN),
        ("04", "零妥协验证", "后端缺失时测试直接失败\n魔术字节 · 像素分析 · 音频检测", TEAL),
    ]
    items = ""
    for i, (num, title, desc, color) in enumerate(feats):
        y = 180 + i * 160
        items += f'''
<g transform="translate(62, {y})">
  <circle cx="30" cy="30" r="26" fill="none" stroke="{color}" stroke-width="3"/>
  <text x="30" y="37" text-anchor="middle" font-family="{FMONO}" font-size="22" font-weight="800" fill="{color}">{num}</text>
  <text x="80" y="30" font-family="{FONT}" font-size="24" font-weight="700" fill="{INK}">{title}</text>
  <text x="80" y="65" font-family="{FONT}" font-size="17" fill="{INK_D}">{desc.replace(chr(10), " · ")}</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
<rect x="62" y="60" width="900" height="904" rx="32" fill="{BG_P}" filter="url(#shadow)" stroke="{LINE}" stroke-width="1"/>
<text x="512" y="130" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="800" fill="{INK}">为什么推荐？</text>
{items}
<text x="512" y="880" text-anchor="middle" font-family="{FONT}" font-size="16" fill="{INK_M}">100% 测试通过率 · 开源 · 可扩展</text>
''')

def card_2():
    return svg_wrap(1024, 1024, f'''
<rect x="62" y="60" width="900" height="904" rx="32" fill="{BG_P}" filter="url(#shadow)" stroke="{LINE}" stroke-width="1"/>
<text x="512" y="130" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="800" fill="{INK}">7 步构建流水线</text>

<g transform="translate(90, 190)">
  <rect x="0" y="0" width="260" height="100" rx="16" fill="{BG}" stroke="{PURPLE}" stroke-width="1" stroke-opacity="0.4"/>
  <text x="130" y="38" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="700" fill="{PURPLE_L}">Step 1</text>
  <text x="130" y="70" text-anchor="middle" font-family="{FONT}" font-size="18" fill="{INK_D}">分析源码结构</text>

  <rect x="290" y="0" width="260" height="100" rx="16" fill="{BG}" stroke="{BLUE}" stroke-width="1" stroke-opacity="0.4"/>
  <text x="420" y="38" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="700" fill="{CYAN}">Step 2</text>
  <text x="420" y="70" text-anchor="middle" font-family="{FONT}" font-size="18" fill="{INK_D}">规划命令分组</text>

  <rect x="580" y="0" width="260" height="100" rx="16" fill="{BG}" stroke="{CYAN}" stroke-width="1" stroke-opacity="0.4"/>
  <text x="710" y="38" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="700" fill="{TEAL}">Step 3</text>
  <text x="710" y="70" text-anchor="middle" font-family="{FONT}" font-size="18" fill="{INK_D}">构建 Click CLI</text>
</g>

<g transform="translate(90, 330)">
  <rect x="0" y="0" width="260" height="100" rx="16" fill="{BG}" stroke="{TEAL}" stroke-width="1" stroke-opacity="0.4"/>
  <text x="130" y="38" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="700" fill="{TEAL}">Step 4</text>
  <text x="130" y="70" text-anchor="middle" font-family="{FONT}" font-size="18" fill="{INK_D}">生成测试计划</text>

  <rect x="290" y="0" width="260" height="100" rx="16" fill="{BG}" stroke="{ORANGE}" stroke-width="1" stroke-opacity="0.4"/>
  <text x="420" y="38" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="700" fill="{ORANGE}">Step 5</text>
  <text x="420" y="70" text-anchor="middle" font-family="{FONT}" font-size="18" fill="{INK_D}">编写测试套件</text>

  <rect x="580" y="0" width="260" height="100" rx="16" fill="{BG}" stroke="{GREEN}" stroke-width="1" stroke-opacity="0.4"/>
  <text x="710" y="38" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="700" fill="{GREEN}">Step 6</text>
  <text x="710" y="70" text-anchor="middle" font-family="{FONT}" font-size="18" fill="{INK_D}">生成文档</text>
</g>

<g transform="translate(90, 470)">
  <rect x="0" y="0" width="260" height="100" rx="16" fill="{BG}" stroke="{PURPLE}" stroke-width="1" stroke-opacity="0.4"/>
  <text x="130" y="38" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="700" fill="{PURPLE_L}">Step 7</text>
  <text x="130" y="70" text-anchor="middle" font-family="{FONT}" font-size="18" fill="{INK_D}">安装到 PATH</text>

  <rect x="290" y="0" width="550" height="100" rx="16" fill="{BG}" stroke="{BLUE}" stroke-width="1" stroke-opacity="0.4"/>
  <text x="565" y="38" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="700" fill="{CYAN}">pip install -e . → 开箱即用</text>
  <text x="565" y="70" text-anchor="middle" font-family="{FONT}" font-size="18" fill="{INK_D}">11 款软件已武装 · 新软件 7 步搞定</text>
</g>

<g transform="translate(90, 650)">
  <rect x="0" y="0" width="844" height="70" rx="14" fill="{PURPLE}" opacity="0.1"/>
  <text x="422" y="30" text-anchor="middle" font-family="{FONT}" font-size="18" fill="{INK_D}">AI Agent 原生调用 @cli-anything build</text>
  <text x="422" y="55" text-anchor="middle" font-family="{FONT}" font-size="16" fill="{INK_M}">在飞书直接触发 · 自动封装</text>
</g>

<text x="512" y="830" text-anchor="middle" font-family="{FONT}" font-size="15" fill="{INK_M}">让 AI 操控任何软件</text>
''')

def card_banner():
    return svg_wrap(1792, 1024, f'''
<text x="896" y="240" text-anchor="middle" font-family="{FONT}" font-size="48" font-weight="300" fill="{INK_D}" letter-spacing="3">CLI-ANYTHING</text>
<text x="896" y="430" text-anchor="middle" font-family="{FONT}" font-size="180" font-weight="900" fill="url(#accentG)" letter-spacing="-6" filter="url(#glow)">万物皆可 CLI</text>
<text x="896" y="520" text-anchor="middle" font-family="{FONT}" font-size="30" fill="{INK_D}">让 AI 操控任何软件 · 11 款已武装</text>

<rect x="496" y="580" width="800" height="70" rx="35" fill="none" stroke="url(#accentG2)" stroke-width="2"/>
<text x="896" y="623" text-anchor="middle" font-family="{FMONO}" font-size="24" font-weight="600" fill="{PURPLE_L}">github.com/CLI-Anything</text>

<g transform="translate(200, 720)">
  {chip("GIMP", 0, 0, PURPLE)}
  {chip("Blender", 180, 0, BLUE)}
  {chip("Inkscape", 360, 0, CYAN)}
  {chip("LibreOffice", 540, 0, TEAL)}
  {chip("OBS", 720, 0, ORANGE)}
  {chip("Kdenlive", 900, 0, GREEN)}
  {chip("Shotcut", 1080, 0, PURPLE)}
  {chip("Sketch", 1260, 0, BLUE)}
</g>

<g transform="translate(460, 780)">
  {chip("OpenScreen", 0, 0, CYAN)}
  {chip("Draw.io", 180, 0, TEAL)}
  {chip("Audacity", 360, 0, ORANGE)}
  {chip("Zoom", 540, 0, GREEN)}
</g>

<text x="896" y="920" text-anchor="middle" font-family="{FONT}" font-size="17" fill="{INK_M}">1628 项测试 · 100% 通过率 · 7 步构建流水线</text>
''')

if __name__ == "__main__":
    cards = [
        ("cli-anything-square", card_square()),
        ("cli-anything-card-1", card_1()),
        ("cli-anything-card-2", card_2()),
        ("cli-anything-banner", card_banner()),
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