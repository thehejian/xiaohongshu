#!/usr/bin/env python3
"""Generate dark-style cards for opencli (1024x1024 + 1792x1024 banner)."""
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

def card_square():
    return svg_wrap(1024, 1024, f'''
<rect x="62" y="80" width="900" height="864" rx="32" fill="{BG_P}" filter="url(#shadow)" stroke="{LINE}" stroke-width="1"/>

<text x="512" y="160" text-anchor="middle" font-family="{FONT}" font-size="36" fill="{INK_D}" letter-spacing="3" font-weight="300">OPEN</text>
<text x="512" y="380" text-anchor="middle" font-family="{FONT}" font-size="160" font-weight="900" fill="url(#accentG)" letter-spacing="-4" filter="url(#glow)">CLI</text>
<text x="512" y="460" text-anchor="middle" font-family="{FONT}" font-size="26" fill="{INK_D}" letter-spacing="1">让每个网站都拥有 CLI</text>

<rect x="200" y="500" width="624" height="60" rx="30" fill="none" stroke="url(#accentG2)" stroke-width="2"/>
<text x="512" y="537" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="600" fill="{PURPLE_L}">npm install -g opencli</text>

<g transform="translate(120, 620)">
  <rect x="0" y="0" width="180" height="42" rx="21" fill="{PURPLE}" opacity="0.15"/><text x="90" y="27" text-anchor="middle" font-family="{FONT}" font-size="16" font-weight="600" fill="{PURPLE_L}">148+ 适配器</text>
  <rect x="200" y="0" width="180" height="42" rx="21" fill="{BLUE}" opacity="0.15"/><text x="290" y="27" text-anchor="middle" font-family="{FONT}" font-size="16" font-weight="600" fill="{CYAN}">Browser Bridge</text>
  <rect x="400" y="0" width="180" height="42" rx="21" fill="{TEAL}" opacity="0.15"/><text x="490" y="27" text-anchor="middle" font-family="{FONT}" font-size="16" font-weight="600" fill="{TEAL}">AI Agent</text>
  <rect x="600" y="0" width="180" height="42" rx="21" fill="{ORANGE}" opacity="0.15"/><text x="690" y="27" text-anchor="middle" font-family="{FONT}" font-size="16" font-weight="600" fill="{ORANGE}">外部 CLI</text>
</g>

<text x="512" y="870" text-anchor="middle" font-family="{FMONO}" font-size="15" fill="{INK_M}">github.com/jackwener/opencli</text>
''')

def card_1():
    sites = [
        ("小红书", "xiaohongshu", PURPLE),
        ("知乎", "zhihu", BLUE),
        ("B站", "bilibili", CYAN),
        ("微博", "weibo", TEAL),
        ("推特", "twitter", BLUE),
        ("豆瓣", "douban", GREEN),
        ("ChatGPT", "chatgpt", PURPLE),
        ("GitHub", "github", INK),
        ("Docker", "docker", BLUE),
        ("飞书CLI", "lark-cli", CYAN),
    ]
    chips = ""
    for i, (name, cmd, color) in enumerate(sites):
        x = 90 + (i % 5) * 180
        y = 240 + (i // 5) * 90
        chips += f'''
<g transform="translate({x}, {y})">
  <rect x="0" y="0" width="160" height="70" rx="14" fill="{BG}" stroke="{color}" stroke-width="1" stroke-opacity="0.4"/>
  <text x="80" y="30" text-anchor="middle" font-family="{FONT}" font-size="18" font-weight="700" fill="{color}">{name}</text>
  <text x="80" y="54" text-anchor="middle" font-family="{FMONO}" font-size="13" fill="{INK_M}">{cmd}</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
<rect x="62" y="60" width="900" height="904" rx="32" fill="{BG_P}" filter="url(#shadow)" stroke="{LINE}" stroke-width="1"/>
<text x="512" y="130" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="800" fill="{INK}">148+ 网站适配器</text>
<text x="512" y="170" text-anchor="middle" font-family="{FONT}" font-size="18" fill="{INK_D}">覆盖日常 90% 的网站操作</text>
{chips}
<text x="512" y="880" text-anchor="middle" font-family="{FONT}" font-size="16" fill="{INK_M}">+ Claude · Gemini · Obsidian · Notion · 企业微信 · 掘金 · 更多</text>
''')

def card_2():
    return svg_wrap(1024, 1024, f'''
<rect x="62" y="60" width="900" height="904" rx="32" fill="{BG_P}" filter="url(#shadow)" stroke="{LINE}" stroke-width="1"/>

<text x="512" y="130" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="800" fill="{INK}">核心能力</text>

<g transform="translate(90, 200)">
  <rect x="0" y="0" width="400" height="200" rx="20" fill="{BG}" stroke="{PURPLE}" stroke-width="1" stroke-opacity="0.4"/>
  <text x="30" y="45" font-family="{FONT}" font-size="22" font-weight="700" fill="{PURPLE_L}">Browser Bridge</text>
  <text x="30" y="80" font-family="{FONT}" font-size="16" fill="{INK_D}">真实 Chrome 驱动网页</text>
  <text x="30" y="110" font-family="{FONT}" font-size="16" fill="{INK_D}">登录态长期复用</text>
  <text x="30" y="140" font-family="{FONT}" font-size="16" fill="{INK_D}">查 Feed · 看笔记 · 搜内容</text>
  <text x="30" y="170" font-family="{FONT}" font-size="16" fill="{INK_D}">取评论 · 发帖子 · 全终端</text>

  <rect x="430" y="0" width="400" height="200" rx="20" fill="{BG}" stroke="{BLUE}" stroke-width="1" stroke-opacity="0.4"/>
  <text x="460" y="45" font-family="{FONT}" font-size="22" font-weight="700" fill="{CYAN}">AI Agent 原生</text>
  <text x="460" y="80" font-family="{FONT}" font-size="16" fill="{INK_D}">所有命令 --format yaml/json</text>
  <text x="460" y="110" font-family="{FONT}" font-size="16" fill="{INK_D}">结构化数据直接给 Agent</text>
  <text x="460" y="140" font-family="{FONT}" font-size="16" fill="{INK_D}">自动决策自动执行</text>
  <text x="460" y="170" font-family="{FONT}" font-size="16" fill="{INK_D}">20+ lark skill 用它跑</text>
</g>

<g transform="translate(90, 450)">
  <rect x="0" y="0" width="400" height="200" rx="20" fill="{BG}" stroke="{TEAL}" stroke-width="1" stroke-opacity="0.4"/>
  <text x="30" y="45" font-family="{FONT}" font-size="22" font-weight="700" fill="{TEAL}">外部 CLI 聚合</text>
  <text x="30" y="80" font-family="{FONT}" font-size="16" fill="{INK_D}">lark-cli · gh · vercel</text>
  <text x="30" y="110" font-family="{FONT}" font-size="16" fill="{INK_D}">wrangler · obsidian · tg</text>
  <text x="30" y="140" font-family="{FONT}" font-size="16" fill="{INK_D}">一个 opencli 管所有</text>
  <text x="30" y="170" font-family="{FONT}" font-size="16" fill="{INK_D}">浏览器 + 终端无缝衔接</text>

  <rect x="430" y="0" width="400" height="200" rx="20" fill="{BG}" stroke="{ORANGE}" stroke-width="1" stroke-opacity="0.4"/>
  <text x="460" y="45" font-family="{FONT}" font-size="22" font-weight="700" fill="{ORANGE}">零配置上手</text>
  <text x="460" y="80" font-family="{FONT}" font-size="16" fill="{INK_D}">安装即用，无需配置</text>
  <text x="460" y="110" font-family="{FONT}" font-size="16" fill="{INK_D}">148+ 适配器随时调用</text>
  <text x="460" y="140" font-family="{FONT}" font-size="16" fill="{INK_D}">--help 查看全部命令</text>
  <text x="460" y="170" font-family="{FONT}" font-size="16" fill="{INK_D}">Browser Bridge 扩展即连</text>
</g>

<g transform="translate(90, 700)">
  <rect x="0" y="0" width="844" height="60" rx="14" fill="{PURPLE}" opacity="0.1"/>
  <text x="422" y="36" text-anchor="middle" font-family="{FMONO}" font-size="19" font-weight="600" fill="{PURPLE_L}">npm install -g opencli</text>
</g>

<text x="512" y="880" text-anchor="middle" font-family="{FONT}" font-size="15" fill="{INK_M}">让每个网站都拥有 CLI</text>
''')

def card_banner():
    return svg_wrap(1792, 1024, f'''
<text x="896" y="260" text-anchor="middle" font-family="{FONT}" font-size="52" font-weight="300" fill="{INK_D}" letter-spacing="4">OPEN</text>
<text x="896" y="430" text-anchor="middle" font-family="{FONT}" font-size="200" font-weight="900" fill="url(#accentG)" letter-spacing="-6" filter="url(#glow)">CLI</text>
<text x="896" y="520" text-anchor="middle" font-family="{FONT}" font-size="30" fill="{INK_D}" letter-spacing="1">让每个网站都拥有 CLI</text>

<rect x="396" y="590" width="1000" height="70" rx="35" fill="none" stroke="url(#accentG2)" stroke-width="2"/>
<text x="896" y="633" text-anchor="middle" font-family="{FMONO}" font-size="26" font-weight="600" fill="{PURPLE_L}">npm install -g opencli</text>

<g transform="translate(200, 730)">
  <rect x="0" y="0" width="200" height="48" rx="24" fill="{PURPLE}" opacity="0.15"/><text x="100" y="32" text-anchor="middle" font-family="{FONT}" font-size="18" font-weight="600" fill="{PURPLE_L}">148+ 适配器</text>
  <rect x="230" y="0" width="200" height="48" rx="24" fill="{BLUE}" opacity="0.15"/><text x="330" y="32" text-anchor="middle" font-family="{FONT}" font-size="18" font-weight="600" fill="{CYAN}">Browser Bridge</text>
  <rect x="460" y="0" width="200" height="48" rx="24" fill="{TEAL}" opacity="0.15"/><text x="560" y="32" text-anchor="middle" font-family="{FONT}" font-size="18" font-weight="600" fill="{TEAL}">AI 原生</text>
  <rect x="690" y="0" width="200" height="48" rx="24" fill="{ORANGE}" opacity="0.15"/><text x="790" y="32" text-anchor="middle" font-family="{FONT}" font-size="18" font-weight="600" fill="{ORANGE}">外部 CLI</text>
  <rect x="920" y="0" width="200" height="48" rx="24" fill="{GREEN}" opacity="0.15"/><text x="1020" y="32" text-anchor="middle" font-family="{FONT}" font-size="18" font-weight="600" fill="{GREEN}">零配置</text>
  <rect x="1150" y="0" width="200" height="48" rx="24" fill="{PURPLE}" opacity="0.15"/><text x="1250" y="32" text-anchor="middle" font-family="{FONT}" font-size="18" font-weight="600" fill="{PURPLE_L}">开源免费</text>
</g>

<text x="896" y="920" text-anchor="middle" font-family="{FMONO}" font-size="17" fill="{INK_M}">github.com/jackwener/opencli</text>
''')

if __name__ == "__main__":
    cards = [
        ("opencli-square", card_square()),
        ("opencli-card-1", card_1()),
        ("opencli-card-2", card_2()),
        ("opencli-banner", card_banner()),
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