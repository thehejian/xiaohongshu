#!/usr/bin/env python3
"""Generate rich social cards for Codex Plugin Deep Dive using SVG + Inkscape."""

import subprocess, os, shutil

OUT = os.path.dirname(os.path.abspath(__file__))

W, H = 1080, 1080

def svg_tag():
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'

def make_bg_gradient():
    return (
        '<defs>'
        '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0%" stop-color="#FAF7F2"/>'
        '<stop offset="100%" stop-color="#F5F0E8"/>'
        '</linearGradient>'
        '<linearGradient id="bg-dark" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0%" stop-color="#0B1027"/>'
        '<stop offset="100%" stop-color="#151B3D"/>'
        '</linearGradient>'
        '</defs>'
    )

# ── Chinese Light Cards ──────────────────────────────────────────

def card_cn_cover():
    return f'''{svg_tag()}
{make_bg_gradient()}
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<!-- Top accent stripe -->
<rect x="0" y="0" width="{W}" height="8" fill="#002FA7"/>
<!-- Decorative circles -->
<circle cx="920" cy="160" r="180" fill="none" stroke="#002FA7" stroke-width="1.5" opacity="0.12"/>
<circle cx="920" cy="160" r="220" fill="none" stroke="#002FA7" stroke-width="0.8" opacity="0.08"/>
<circle cx="160" cy="920" r="120" fill="none" stroke="#002FA7" stroke-width="1.5" opacity="0.10"/>
<!-- Accent square top-right -->
<rect x="780" y="60" width="240" height="4" fill="#002FA7" opacity="0.3"/>
<!-- Main title -->
<text x="540" y="400" text-anchor="middle" font-family="STHeitiTC-Medium,STHeitiTC,Heiti TC,PingFang SC,sans-serif" font-size="164" font-weight="700" fill="#1E293B">Codex插件</text>
<text x="540" y="560" text-anchor="middle" font-family="STHeitiTC-Medium,STHeitiTC,Heiti TC,PingFang SC,sans-serif" font-size="164" font-weight="700" fill="#002FA7">深度解析</text>
<!-- Accent bar under title -->
<rect x="360" y="620" width="360" height="4" fill="#002FA7"/>
<!-- Subtitle -->
<text x="540" y="720" text-anchor="middle" font-family="STHeitiTC-Medium,STHeitiTC,Heiti TC,PingFang SC,sans-serif" font-size="40" fill="#64748B" letter-spacing="4">每个角色的具体用法</text>
<!-- Bottom decoration -->
<rect x="0" y="H-80" width="280" height="80" fill="#002FA7" opacity="0.06"/>
<rect x="440" y="H-3" width="200" height="3" fill="#002FA7" opacity="0.3"/>
<!-- Tag -->
<text x="800" y="H-40" text-anchor="end" font-family="STHeitiTC-Medium,STHeitiTC,Heiti TC,PingFang SC,sans-serif" font-size="28" fill="#94A3B8">AI · 效率 · 开发</text>
</svg>'''

def card_cn_architect():
    return f'''{svg_tag()}
{make_bg_gradient()}
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<rect x="0" y="0" width="{W}" height="8" fill="#002FA7"/>
<!-- Decorative grid dots -->
<g opacity="0.05">
<circle cx="100" cy="100" r="3" fill="#1E293B"/><circle cx="200" cy="100" r="3" fill="#1E293B"/>
<circle cx="300" cy="100" r="3" fill="#1E293B"/><circle cx="400" cy="100" r="3" fill="#1E293B"/>
<circle cx="100" cy="200" r="3" fill="#1E293B"/><circle cx="200" cy="200" r="3" fill="#1E293B"/>
<circle cx="300" cy="200" r="3" fill="#1E293B"/><circle cx="400" cy="200" r="3" fill="#1E293B"/>
</g>
<!-- Role badge -->
<rect x="420" y="120" width="240" height="48" rx="24" fill="#002FA7" opacity="0.10"/>
<text x="540" y="152" text-anchor="middle" font-family="STHeitiTC-Medium,sans-serif" font-size="26" fill="#002FA7" letter-spacing="4">ROLE 01</text>
<!-- Main title -->
<text x="540" y="400" text-anchor="middle" font-family="STHeitiTC-Medium,Heiti TC,PingFang SC,sans-serif" font-size="148" font-weight="700" fill="#1E293B">架构师</text>
<text x="540" y="540" text-anchor="middle" font-family="STHeitiTC-Medium,Heiti TC,PingFang SC,sans-serif" font-size="100" font-weight="500" fill="#002FA7">系统级设计</text>
<rect x="340" y="590" width="400" height="3" fill="#002FA7" opacity="0.25"/>
<!-- Description -->
<text x="540" y="680" text-anchor="middle" font-family="STHeitiTC-Medium,Heiti TC,PingFang SC,sans-serif" font-size="36" fill="#64748B">大项目重构 · 全局架构规划</text>
<text x="540" y="730" text-anchor="middle" font-family="STHeitiTC-Medium,Heiti TC,PingFang SC,sans-serif" font-size="30" fill="#94A3B8">适合从 0 到 1 的系统搭建</text>
<!-- Bottom icon bars -->
<rect x="200" y="H-6" width="160" height="6" fill="#002FA7" opacity="0.3"/>
<rect x="400" y="H-6" width="160" height="6" fill="#002FA7" opacity="0.15"/>
<rect x="600" y="H-6" width="160" height="6" fill="#002FA7" opacity="0.08"/>
</svg>'''

def card_cn_reviewer():
    return f'''{svg_tag()}
{make_bg_gradient()}
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<rect x="0" y="0" width="{W}" height="8" fill="#002FA7"/>
<!-- Decorative code-like lines -->
<g opacity="0.06" stroke="#1E293B" stroke-width="2">
<line x1="100" y1="120" x2="280" y2="120"/><line x1="100" y1="150" x2="340" y2="150"/><line x1="100" y1="180" x2="200" y2="180"/>
<line x1="800" y1="840" x2="980" y2="840"/><line x1="800" y1="870" x2="920" y2="870"/><line x1="800" y1="900" x2="960" y2="900"/>
</g>
<circle cx="150" cy="150" r="60" fill="none" stroke="#002FA7" stroke-width="1" opacity="0.08"/>
<circle cx="930" cy="930" r="80" fill="none" stroke="#002FA7" stroke-width="1" opacity="0.08"/>
<!-- Role badge -->
<rect x="420" y="120" width="240" height="48" rx="24" fill="#002FA7" opacity="0.10"/>
<text x="540" y="152" text-anchor="middle" font-family="STHeitiTC-Medium,sans-serif" font-size="26" fill="#002FA7" letter-spacing="4">ROLE 02</text>
<!-- Main title -->
<text x="540" y="400" text-anchor="middle" font-family="STHeitiTC-Medium,Heiti TC,PingFang SC,sans-serif" font-size="120" font-weight="700" fill="#1E293B">代码审查员</text>
<text x="540" y="540" text-anchor="middle" font-family="STHeitiTC-Medium,Heiti TC,PingFang SC,sans-serif" font-size="120" font-weight="500" fill="#002FA7">Bug 猎手</text>
<rect x="340" y="590" width="400" height="3" fill="#002FA7" opacity="0.25"/>
<!-- Description -->
<text x="540" y="680" text-anchor="middle" font-family="STHeitiTC-Medium,Heiti TC,PingFang SC,sans-serif" font-size="36" fill="#64748B">揪出隐藏 Bug · 提升代码质量</text>
<text x="540" y="730" text-anchor="middle" font-family="STHeitiTC-Medium,Heiti TC,PingFang SC,sans-serif" font-size="30" fill="#94A3B8">代码审查效率提升 300%</text>
</svg>'''

def card_cn_docwriter():
    return f'''{svg_tag()}
{make_bg_gradient()}
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<rect x="0" y="0" width="{W}" height="8" fill="#002FA7"/>
<!-- Decorative horizontal lines -->
<g opacity="0.05">
<rect x="120" y="100" width="300" height="2" fill="#1E293B"/><rect x="120" y="130" width="240" height="2" fill="#1E293B"/>
<rect x="120" y="160" width="200" height="2" fill="#1E293B"/>
<rect x="660" y="840" width="300" height="2" fill="#1E293B"/><rect x="660" y="870" width="240" height="2" fill="#1E293B"/>
<rect x="660" y="900" width="200" height="2" fill="#1E293B"/>
</g>
<rect x="760" y="80" width="260" height="4" fill="#002FA7" opacity="0.2"/>
<!-- Role badge -->
<rect x="420" y="120" width="240" height="48" rx="24" fill="#002FA7" opacity="0.10"/>
<text x="540" y="152" text-anchor="middle" font-family="STHeitiTC-Medium,sans-serif" font-size="26" fill="#002FA7" letter-spacing="4">ROLE 03</text>
<!-- Main title -->
<text x="540" y="400" text-anchor="middle" font-family="STHeitiTC-Medium,Heiti TC,PingFang SC,sans-serif" font-size="120" font-weight="700" fill="#1E293B">文档撰写员</text>
<text x="540" y="540" text-anchor="middle" font-family="STHeitiTC-Medium,Heiti TC,PingFang SC,sans-serif" font-size="100" font-weight="500" fill="#002FA7">注释自动生成</text>
<rect x="340" y="590" width="400" height="3" fill="#002FA7" opacity="0.25"/>
<!-- Description -->
<text x="540" y="680" text-anchor="middle" font-family="STHeitiTC-Medium,Heiti TC,PingFang SC,sans-serif" font-size="36" fill="#64748B">自动生成注释 · 告别写文档</text>
<text x="540" y="730" text-anchor="middle" font-family="STHeitiTC-Medium,Heiti TC,PingFang SC,sans-serif" font-size="30" fill="#94A3B8">API 文档覆盖率自动 100%</text>
</svg>'''

# ── English Dark Cards ───────────────────────────────────────────

def card_en_cover():
    return f'''{svg_tag()}
{make_bg_gradient()}
<rect width="{W}" height="{H}" fill="url(#bg-dark)"/>
<rect x="0" y="0" width="{W}" height="8" fill="#C5E803"/>
<circle cx="160" cy="920" r="160" fill="none" stroke="#C5E803" stroke-width="1.5" opacity="0.10"/>
<circle cx="160" cy="920" r="200" fill="none" stroke="#C5E803" stroke-width="0.8" opacity="0.06"/>
<circle cx="920" cy="160" r="100" fill="none" stroke="#C5E803" stroke-width="1" opacity="0.08"/>
<rect x="60" y="60" width="200" height="4" fill="#C5E803" opacity="0.3"/>
<text x="540" y="380" text-anchor="middle" font-family="Inter,Helvetica Neue,sans-serif" font-size="136" font-weight="200" fill="#F8FAFC" letter-spacing="-2">Codex</text>
<text x="540" y="520" text-anchor="middle" font-family="Inter,Helvetica Neue,sans-serif" font-size="136" font-weight="200" fill="#C5E803" letter-spacing="-2">Plugin</text>
<text x="540" y="570" text-anchor="middle" font-family="Inter,Helvetica Neue,sans-serif" font-size="60" font-weight="300" fill="#CBD5E1" letter-spacing="6" text-transform="uppercase">DEEP DIVE</text>
<rect x="360" y="620" width="360" height="3" fill="#C5E803" opacity="0.4"/>
<text x="540" y="720" text-anchor="middle" font-family="Inter,Helvetica Neue,sans-serif" font-size="32" font-weight="300" fill="#64748B">Every Role, Explained</text>
<text x="540" y="H-60" text-anchor="middle" font-family="Inter,monospace" font-size="18" fill="#475569" letter-spacing="4" text-transform="uppercase">DEV EFFICIENCY · AI</text>
</svg>'''

def card_en_architect():
    return f'''{svg_tag()}
{make_bg_gradient()}
<rect width="{W}" height="{H}" fill="url(#bg-dark)"/>
<rect x="0" y="0" width="{W}" height="8" fill="#C5E803"/>
<g opacity="0.04" stroke="#F8FAFC" stroke-width="1">
<rect x="100" y="100" width="200" height="200" fill="none"/><rect x="110" y="110" width="180" height="180" fill="none"/>
<rect x="780" y="780" width="200" height="200" fill="none"/><rect x="790" y="790" width="180" height="180" fill="none"/>
</g>
<rect x="420" y="120" width="240" height="48" rx="24" fill="#C5E803" opacity="0.15"/>
<text x="540" y="152" text-anchor="middle" font-family="Inter,monospace,sans-serif" font-size="22" fill="#C5E803" letter-spacing="4">ROLE 01</text>
<text x="540" y="400" text-anchor="middle" font-family="Inter,Helvetica Neue,sans-serif" font-size="148" font-weight="200" fill="#F8FAFC" letter-spacing="-2">Architect</text>
<text x="540" y="540" text-anchor="middle" font-family="Inter,Helvetica Neue,sans-serif" font-size="80" font-weight="300" fill="#C5E803">System Design</text>
<rect x="340" y="590" width="400" height="3" fill="#C5E803" opacity="0.25"/>
<text x="540" y="680" text-anchor="middle" font-family="Inter,Helvetica Neue,sans-serif" font-size="32" font-weight="300" fill="#94A3B8">Greenfield · Large Refactor</text>
<text x="540" y="730" text-anchor="middle" font-family="Inter,Helvetica Neue,sans-serif" font-size="26" font-weight="300" fill="#475569">From zero to production-ready</text>
</svg>'''

def card_en_reviewer():
    return f'''{svg_tag()}
{make_bg_gradient()}
<rect width="{W}" height="{H}" fill="url(#bg-dark)"/>
<rect x="0" y="0" width="{W}" height="8" fill="#C5E803"/>
<!-- Code-like brackets -->
<g opacity="0.04" fill="none" stroke="#F8FAFC" stroke-width="2">
<text x="140" y="200" font-family="monospace" font-size="60" fill="#F8FAFC">&lt;/&gt;</text>
<text x="800" y="900" font-family="monospace" font-size="40" fill="#F8FAFC">{'{}'}</text>
</g>
<rect x="420" y="120" width="240" height="48" rx="24" fill="#C5E803" opacity="0.15"/>
<text x="540" y="152" text-anchor="middle" font-family="Inter,monospace,sans-serif" font-size="22" fill="#C5E803" letter-spacing="4">ROLE 02</text>
<text x="540" y="400" text-anchor="middle" font-family="Inter,Helvetica Neue,sans-serif" font-size="120" font-weight="200" fill="#F8FAFC" letter-spacing="-2">Code Reviewer</text>
<text x="540" y="540" text-anchor="middle" font-family="Inter,Helvetica Neue,sans-serif" font-size="100" font-weight="200" fill="#C5E803">Bug Hunter</text>
<rect x="340" y="590" width="400" height="3" fill="#C5E803" opacity="0.25"/>
<text x="540" y="680" text-anchor="middle" font-family="Inter,Helvetica Neue,sans-serif" font-size="32" font-weight="300" fill="#94A3B8">Catch bugs. Ship quality.</text>
<text x="540" y="730" text-anchor="middle" font-family="Inter,Helvetica Neue,sans-serif" font-size="26" font-weight="300" fill="#475569">3x faster code review cycles</text>
</svg>'''

def card_en_docwriter():
    return f'''{svg_tag()}
{make_bg_gradient()}
<rect width="{W}" height="{H}" fill="url(#bg-dark)"/>
<rect x="0" y="0" width="{W}" height="8" fill="#C5E803"/>
<!-- Document lines -->
<g opacity="0.04">
<rect x="120" y="90" width="280" height="3" fill="#F8FAFC"/><rect x="120" y="110" width="220" height="3" fill="#F8FAFC"/>
<rect x="120" y="130" width="250" height="3" fill="#F8FAFC"/>
<rect x="680" y="850" width="280" height="3" fill="#F8FAFC"/><rect x="680" y="870" width="220" height="3" fill="#F8FAFC"/>
</g>
<rect x="420" y="120" width="240" height="48" rx="24" fill="#C5E803" opacity="0.15"/>
<text x="540" y="152" text-anchor="middle" font-family="Inter,monospace,sans-serif" font-size="22" fill="#C5E803" letter-spacing="4">ROLE 03</text>
<text x="540" y="400" text-anchor="middle" font-family="Inter,Helvetica Neue,sans-serif" font-size="120" font-weight="200" fill="#F8FAFC" letter-spacing="-2">Doc Writer</text>
<text x="540" y="540" text-anchor="middle" font-family="Inter,Helvetica Neue,sans-serif" font-size="80" font-weight="300" fill="#C5E803">Auto Comments</text>
<rect x="340" y="590" width="400" height="3" fill="#C5E803" opacity="0.25"/>
<text x="540" y="680" text-anchor="middle" font-family="Inter,Helvetica Neue,sans-serif" font-size="32" font-weight="300" fill="#94A3B8">Generate docs. Ship confidence.</text>
<text x="540" y="730" text-anchor="middle" font-family="Inter,Helvetica Neue,sans-serif" font-size="26" font-weight="300" fill="#475569">100% API doc coverage</text>
</svg>'''

# ── Render ───────────────────────────────────────────────────────

CARDS = [
    ("card-cn-01-cover.svg",     card_cn_cover()),
    ("card-cn-02-architect.svg", card_cn_architect()),
    ("card-cn-03-reviewer.svg",  card_cn_reviewer()),
    ("card-cn-04-docwriter.svg", card_cn_docwriter()),
    ("card-en-01-cover.svg",     card_en_cover()),
    ("card-en-02-architect.svg", card_en_architect()),
    ("card-en-03-reviewer.svg",  card_en_reviewer()),
    ("card-en-04-docwriter.svg", card_en_docwriter()),
]

for name, svg in CARDS:
    svg_path = os.path.join(OUT, name)
    png_path = svg_path.replace(".svg", ".png")
    with open(svg_path, "w") as f:
        f.write(svg)
    subprocess.run(["inkscape", svg_path, "--export-filename", png_path,
                    "--export-width", str(W), "--export-height", str(H)],
                   capture_output=True)
    size = os.path.getsize(png_path)
    print(f"  {name} -> {png_path} ({size/1024:.0f} KB)")

print("\nDone! 8 cards generated.")
