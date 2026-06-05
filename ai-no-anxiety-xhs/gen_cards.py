#!/usr/bin/env python3
import os, shutil, subprocess, sys

W, H = 1024, 1024
cream_start = "#FAF7F2"
cream_end = "#F5F0E8"
dark = "#1E293B"
brand = "#E85D04"
accent = "#D97706"
muted = "#64748B"

def bg():
    return f'''<defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{cream_start}"/>
      <stop offset="100%" style="stop-color:{cream_end}"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>'''

def top_accent():
    return f'<rect x="0" y="0" width="{W}" height="8" fill="{brand}"/>'

def bottom_accent():
    return f'<rect x="0" y="{H-8}" width="{W}" height="8" fill="{brand}"/>'

def page_num(n, total):
    return f'<text x="{W-60}" y="{H-50}" font-family="Noto Sans SC, sans-serif" font-size="22" fill="{muted}" text-anchor="end">{n}/{total}</text>'

def dot(x, y, color=brand):
    return f'<circle cx="{x}" cy="{y}" r="8" fill="{color}"/>'

CARDS = []

CARDS.append(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  {bg()}
  {top_accent()}
  {bottom_accent()}
  <text x="{W//2}" y="360" font-family="Noto Sans SC, sans-serif" font-size="72" font-weight="bold" fill="{dark}" text-anchor="middle">只要学得够慢</text>
  <text x="{W//2}" y="460" font-family="Noto Sans SC, sans-serif" font-size="72" font-weight="bold" fill="{brand}" text-anchor="middle">完全不用学</text>
  <line x1="300" y1="510" x2="{W-300}" y2="510" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>
  <text x="{W//2}" y="600" font-family="Noto Sans SC, sans-serif" font-size="32" fill="{muted}" text-anchor="middle">AI时代反焦虑指南</text>
  <text x="{W//2}" y="780" font-family="Noto Sans SC, sans-serif" font-size="24" fill="{muted}" text-anchor="middle">慢即是快 · 少即是多</text>
  {page_num(1, 4)}
</svg>''')

CARDS.append(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  {bg()}
  {top_accent()}
  {bottom_accent()}
  <text x="80" y="140" font-family="Noto Sans SC, sans-serif" font-size="28" fill="{muted}">01</text>
  <text x="80" y="200" font-family="Noto Sans SC, sans-serif" font-size="56" font-weight="bold" fill="{dark}">AI焦虑的真相</text>
  <line x1="80" y1="240" x2="400" y2="240" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>
  <text x="80" y="340" font-family="Noto Sans SC, sans-serif" font-size="32" fill="{dark}">每天刷100篇AI资讯</text>
  <text x="80" y="400" font-family="Noto Sans SC, sans-serif" font-size="32" fill="{dark}">收藏50个工具</text>
  <text x="80" y="460" font-family="Noto Sans SC, sans-serif" font-size="32" fill="{dark}">买3门课</text>
  <text x="80" y="540" font-family="Noto Sans SC, sans-serif" font-size="32" font-weight="bold" fill="{brand}">然后更焦虑了</text>
  <line x1="80" y1="620" x2="{W-80}" y2="620" stroke="#E2E8F0" stroke-width="2"/>
  <text x="80" y="700" font-family="Noto Sans SC, sans-serif" font-size="28" fill="{muted}">90%的AI新闻 三个月后毫无意义</text>
  <text x="80" y="760" font-family="Noto Sans SC, sans-serif" font-size="28" fill="{muted}">焦虑本身比AI更消耗你</text>
  {page_num(2, 4)}
</svg>''')

CARDS.append(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  {bg()}
  {top_accent()}
  {bottom_accent()}
  <text x="80" y="140" font-family="Noto Sans SC, sans-serif" font-size="28" fill="{muted}">02</text>
  <text x="80" y="200" font-family="Noto Sans SC, sans-serif" font-size="56" font-weight="bold" fill="{dark}">慢的三大优势</text>
  <line x1="80" y1="240" x2="400" y2="240" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>
  <rect x="80" y="300" width="864" height="120" rx="16" fill="#FFF" opacity="0.5"/>
  <circle cx="120" cy="360" r="10" fill="{brand}"/>
  <text x="150" y="340" font-family="Noto Sans SC, sans-serif" font-size="36" font-weight="bold" fill="{dark}">噪音过滤器</text>
  <text x="150" y="390" font-family="Noto Sans SC, sans-serif" font-size="26" fill="{muted}">自动避开90%的泡沫信息</text>
  <rect x="80" y="440" width="864" height="120" rx="16" fill="#FFF" opacity="0.5"/>
  <circle cx="120" cy="500" r="10" fill="{brand}"/>
  <text x="150" y="480" font-family="Noto Sans SC, sans-serif" font-size="36" font-weight="bold" fill="{dark}">深度壁垒</text>
  <text x="150" y="530" font-family="Noto Sans SC, sans-serif" font-size="26" fill="{muted}">一个工具跑出10个作品 > 蜻蜓点水20个工具</text>
  <rect x="80" y="580" width="864" height="120" rx="16" fill="#FFF" opacity="0.5"/>
  <circle cx="120" cy="640" r="10" fill="{brand}"/>
  <text x="150" y="620" font-family="Noto Sans SC, sans-serif" font-size="36" font-weight="bold" fill="{dark}">底层能力</text>
  <text x="150" y="670" font-family="Noto Sans SC, sans-serif" font-size="26" fill="{muted}">Prompt工程·数据思维·问题拆解</text>
  <text x="80" y="830" font-family="Noto Sans SC, sans-serif" font-size="28" fill="{accent}">快的人在追热点，慢的人在看本质</text>
  {page_num(3, 4)}
</svg>''')

CARDS.append(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  {bg()}
  {top_accent()}
  <rect x="60" y="280" width="904" height="420" rx="24" fill="#FFF" opacity="0.4"/>
  <text x="{W//2}" y="400" font-family="Noto Sans SC, sans-serif" font-size="36" fill="{brand}" text-anchor="middle">✦</text>
  <text x="{W//2}" y="490" font-family="Noto Sans SC, sans-serif" font-size="44" font-weight="bold" fill="{dark}" text-anchor="middle">AI不会淘汰</text>
  <text x="{W//2}" y="555" font-family="Noto Sans SC, sans-serif" font-size="44" font-weight="bold" fill="{brand}" text-anchor="middle">"学得慢的人"</text>
  <text x="{W//2}" y="630" font-family="Noto Sans SC, sans-serif" font-size="32" fill="{muted}" text-anchor="middle">只会淘汰</text>
  <text x="{W//2}" y="680" font-family="Noto Sans SC, sans-serif" font-size="32" fill="{dark}" text-anchor="middle">"只收藏不行动的人"</text>
  <line x1="360" y1="730" x2="{W-360}" y2="730" stroke="{accent}" stroke-width="3" stroke-linecap="round"/>
  <text x="{W//2}" y="830" font-family="Noto Sans SC, sans-serif" font-size="26" fill="{muted}" text-anchor="middle">点赞收藏，去行动吧</text>
  {page_num(4, 4)}
</svg>''')

os.chdir(os.path.dirname(os.path.abspath(__file__)))

for i, svg in enumerate(CARDS, 1):
    svg_path = f"card-{i}.svg"
    png_path = f"card-{i}.png"
    with open(svg_path, "w") as f:
        f.write(svg)
    print(f"Generated {svg_path}")

    if sys.platform == "darwin":
        for candidate in [
            "/Applications/Inkscape.app/Contents/Resources/bin/inkscape",
            "/opt/homebrew/bin/inkscape",
            "/usr/local/bin/inkscape",
        ]:
            if os.path.exists(candidate):
                inkscape = candidate
                break
        else:
            inkscape = shutil.which("inkscape") or "inkscape"
        subprocess.run([inkscape, svg_path, "--export-filename", png_path, f"--export-width={W}", f"--export-height={H}"], check=True)
        print(f"Converted to {png_path}")
    else:
        subprocess.run(["inkscape", svg_path, "--export-filename", png_path], check=True)
        print(f"Converted to {png_path}")

print("Done!")