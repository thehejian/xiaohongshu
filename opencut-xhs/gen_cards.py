#!/usr/bin/env python3
"""Generate OpenCut social card images — light theme, big title, XHS viral style."""

import os, subprocess

OUT = os.path.dirname(os.path.abspath(__file__))

BG = "#FAF7F2"
BG2 = "#F0EBE0"
WHITE = "#FFFFFF"
INK = "#0F172A"
INK2 = "#64748B"
INK3 = "#94A3B8"
BLUE = "#2563EB"
BLUE_L = "#DBEAFE"
GREEN = "#10B981"
GREEN_L = "#D1FAE5"
PURPLE = "#8B5CF6"
PURPLE_L = "#EDE9FE"
ORANGE = "#F59E0B"
ORANGE_L = "#FEF3C7"
FONT = "PingFang SC, Microsoft YaHei, sans-serif"


def svg(w, h, parts):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
  {" ".join(parts)}
</svg>'''


def cover():
    w, h = 1024, 1024
    parts = [
        f'<defs><linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="{BG}"/><stop offset="100%" stop-color="{BG2}"/></linearGradient><linearGradient id="ab" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="{BLUE}"/><stop offset="100%" stop-color="{BLUE}" stop-opacity="0.5"/></linearGradient><filter id="sh" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="0" dy="6" stdDeviation="14" flood-color="#000" flood-opacity="0.1"/></filter></defs>',
        f'<rect width="{w}" height="{h}" fill="url(#bg)"/>',
        f'<circle cx="900" cy="120" r="220" fill="{BLUE}" opacity="0.06"/>',
        f'<circle cx="120" cy="900" r="180" fill="{PURPLE}" opacity="0.05"/>',
        f'<rect width="{w}" height="8" fill="url(#ab)"/>',
        f'<text x="512" y="100" text-anchor="middle" font-size="40" fill="{BLUE}" font-family="{FONT}" font-weight="700" letter-spacing="4">OPEN</text>',
        f'<text x="512" y="280" text-anchor="middle" font-size="140" fill="{INK}" font-family="{FONT}" font-weight="900" letter-spacing="-4">Cut</text>',
        f'<text x="512" y="350" text-anchor="middle" font-size="28" fill="{INK2}" font-family="{FONT}" font-weight="500">开源剪映 · 隐私优先 · 跨平台</text>',
        f'<line x1="312" y1="390" x2="712" y2="390" stroke="{BLUE}" stroke-width="4" stroke-linecap="round" opacity="0.3"/>',
        f'<rect x="212" y="440" width="600" height="200" rx="24" fill="{WHITE}" filter="url(#sh)"/>',
        f'<g transform="translate(240, 470)">',
        f'<text x="0" y="0" font-size="22" fill="{INK}" font-family="{FONT}" font-weight="700">🎬 视频剪辑全套</text>',
        f'<text x="0" y="35" font-size="18" fill="{INK2}" font-family="{FONT}">多轨时间轴 · 裁剪 · 字幕 · 滤镜 · 转场 · 4K</text>',
        f'<text x="0" y="70" font-size="22" fill="{INK}" font-family="{FONT}" font-weight="700">🤖 AI 黑科技</text>',
        f'<text x="0" y="105" font-size="18" fill="{INK2}" font-family="{FONT}">声音克隆 · 视频翻译 · AI去水印 · 人声分离</text>',
        f'<text x="0" y="140" font-size="22" fill="{INK}" font-family="{FONT}" font-weight="700">🖼️ 图片处理</text>',
        f'<text x="0" y="175" font-size="18" fill="{INK2}" font-family="{FONT}">AI抠图 · 超清修复 · 动漫化 · 图片翻译</text>',
        f'</g>',
        f'<rect x="262" y="690" width="500" height="60" rx="30" fill="{BLUE}" opacity="0.1"/>',
        f'<text x="512" y="727" text-anchor="middle" font-size="22" fill="{BLUE}" font-family="{FONT}" font-weight="600">⭐ 40K+ GitHub Stars</text>',
        f'<rect x="312" y="780" width="400" height="54" rx="27" fill="{BLUE}"/>',
        f'<text x="512" y="814" text-anchor="middle" font-size="20" fill="white" font-family="{FONT}" font-weight="600">npm install -g opencut</text>',
        f'<text x="512" y="920" text-anchor="middle" font-size="18" fill="{INK3}" font-family="{FONT}">github.com/OpenCut-app/OpenCut</text>',
        f'<text x="512" y="960" text-anchor="middle" font-size="16" fill="{INK3}" font-family="{FONT}">#OpenCut #开源 #剪映平替 #视频剪辑</text>',
    ]
    return svg(w, h, parts)


def card_features():
    w, h = 1024, 1024
    features = [
        ("🎬", "视频剪辑", "多轨时间轴 · 裁剪分割\n字幕添加 · 变速 · 转场\n滤镜 · 关键帧 · 4K导出", BLUE),
        ("🤖", "AI 功能", "声音克隆 · 视频翻译\n人声分离 · 智能去水印\nAI 动漫化 · 智能抠图", PURPLE),
        ("🖼️", "图片处理", "AI 抠图 · 一键去背景\n超清修复 · 老照片变4K\n图片翻译 · 不损原图", GREEN),
        ("🔒", "隐私优先", "完全不采集用户数据\n不上传隐私到云端\n本地处理 · 代码开源", ORANGE),
    ]
    parts = [
        f'<defs><linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="{BG}"/><stop offset="100%" stop-color="{BG2}"/></linearGradient><linearGradient id="ab" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="{BLUE}"/><stop offset="100%" stop-color="{BLUE}" stop-opacity="0.5"/></linearGradient><filter id="sh" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#000" flood-opacity="0.08"/></filter></defs>',
        f'<rect width="{w}" height="{h}" fill="url(#bg)"/>',
        f'<rect width="{w}" height="8" fill="url(#ab)"/>',
        f'<text x="512" y="100" text-anchor="middle" font-size="52" fill="{INK}" font-family="{FONT}" font-weight="800">OpenCut 核心能力</text>',
        f'<text x="512" y="145" text-anchor="middle" font-size="24" fill="{INK2}" font-family="{FONT}" font-weight="500">一个工具，视频+AI+图片全搞定</text>',
        f'<line x1="312" y1="170" x2="712" y2="170" stroke="{BLUE}" stroke-width="3" stroke-linecap="round" opacity="0.25"/>',
    ]
    for i, (icon, name, desc, color) in enumerate(features):
        col = i % 2
        row = i // 2
        cx = 60 + col * 500
        cy = 210 + row * 320
        lines = desc.split("\n")
        text_y = cy + 85
        parts.append(f'<rect x="{cx}" y="{cy}" width="440" height="280" rx="24" fill="{WHITE}" filter="url(#sh)"/>')
        parts.append(f'<rect x="{cx}" y="{cy}" width="440" height="6" rx="24" fill="{color}"/>')
        parts.append(f'<text x="{cx + 30}" y="{cy + 60}" font-size="42" font-family="sans-serif">{icon}</text>')
        parts.append(f'<text x="{cx + 85}" y="{cy + 60}" font-size="30" fill="{color}" font-family="{FONT}" font-weight="800">{name}</text>')
        for li, line in enumerate(lines):
            parts.append(f'<text x="{cx + 30}" y="{text_y + li * 40}" font-size="20" fill="{INK2}" font-family="{FONT}" font-weight="500">{line}</text>')
    parts.append(f'<text x="512" y="960" text-anchor="middle" font-size="16" fill="{INK3}" font-family="{FONT}">github.com/OpenCut-app/OpenCut</text>')
    return svg(w, h, parts)


def card_compare():
    w, h = 1024, 1024
    rows = [
        ("开源", "✅ MIT", "❌ 闭源", BLUE),
        ("隐私保护", "✅ 不上传", "❌ 采集数据", GREEN),
        ("跨平台", "✅ 全平台", "✅ 有", PURPLE),
        ("AI 功能", "✅ 丰富", "✅ 丰富", BLUE),
        ("轻量度", "✅ 轻量快速", "❌ 臃肿", ORANGE),
        ("GitHub Star", "⭐ 40K+", "N/A", GREEN),
    ]
    parts = [
        f'<defs><linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="{BG}"/><stop offset="100%" stop-color="{BG2}"/></linearGradient><linearGradient id="ab" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="{BLUE}"/><stop offset="100%" stop-color="{BLUE}" stop-opacity="0.5"/></linearGradient><filter id="sh" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#000" flood-opacity="0.08"/></filter></defs>',
        f'<rect width="{w}" height="{h}" fill="url(#bg)"/>',
        f'<rect width="{w}" height="8" fill="url(#ab)"/>',
        f'<text x="512" y="100" text-anchor="middle" font-size="52" fill="{INK}" font-family="{FONT}" font-weight="800">OpenCut vs 剪映</text>',
        f'<text x="512" y="145" text-anchor="middle" font-size="24" fill="{INK2}" font-family="{FONT}" font-weight="500">为什么推荐迁移到开源方案</text>',
        f'<line x1="312" y1="170" x2="712" y2="170" stroke="{BLUE}" stroke-width="3" stroke-linecap="round" opacity="0.25"/>',
        f'<rect x="120" y="200" width="784" height="54" rx="12" fill="{BLUE}" opacity="0.08"/>',
        f'<text x="260" y="235" text-anchor="middle" font-size="22" fill="{BLUE}" font-family="{FONT}" font-weight="700">对比项</text>',
        f'<text x="500" y="235" text-anchor="middle" font-size="22" fill="{BLUE}" font-family="{FONT}" font-weight="700">OpenCut</text>',
        f'<text x="740" y="235" text-anchor="middle" font-size="22" fill="{BLUE}" font-family="{FONT}" font-weight="700">剪映</text>',
    ]
    for i, (item, left, right, color) in enumerate(rows):
        y = 278 + i * 100
        bg_alt = WHITE if i % 2 == 0 else "transparent"
        if bg_alt != "transparent":
            parts.append(f'<rect x="120" y="{y}" width="784" height="80" rx="10" fill="{bg_alt}" opacity="0.6"/>')
        parts.append(f'<text x="260" y="{y + 48}" text-anchor="middle" font-size="20" fill="{INK}" font-family="{FONT}" font-weight="600">{item}</text>')
        parts.append(f'<text x="500" y="{y + 48}" text-anchor="middle" font-size="20" fill="{color}" font-family="{FONT}" font-weight="600">{left}</text>')
        parts.append(f'<text x="740" y="{y + 48}" text-anchor="middle" font-size="20" fill="{INK3}" font-family="{FONT}" font-weight="500">{right}</text>')
    parts.append(f'<rect x="262" y="920" width="500" height="54" rx="27" fill="{BLUE}"/>')
    parts.append(f'<text x="512" y="952" text-anchor="middle" font-size="20" fill="white" font-family="{FONT}" font-weight="600">npm install -g opencut</text>')
    parts.append(f'<text x="512" y="992" text-anchor="middle" font-size="16" fill="{INK3}" font-family="{FONT}">github.com/OpenCut-app/OpenCut  #OpenCut #开源</text>')
    return svg(w, h, parts)


def card_ai():
    w, h = 1024, 1024
    items = [
        ("🎤", "声音克隆", "复制你的声音\n相似度达 99%", "#8B5CF6"),
        ("🌍", "视频翻译", "一键翻译多语言\n短剧出海利器", "#2563EB"),
        ("🔊", "人声分离", "清空背景噪音\n提取纯净人声", "#10B981"),
        ("🧹", "AI 去水印", "消除 LOGO 物体\n智能擦除不留痕", "#F59E0B"),
    ]
    parts = [
        f'<defs><linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="{BG}"/><stop offset="100%" stop-color="{BG2}"/></linearGradient><linearGradient id="ab" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="{BLUE}"/><stop offset="100%" stop-color="{BLUE}" stop-opacity="0.5"/></linearGradient><filter id="sh" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#000" flood-opacity="0.08"/></filter></defs>',
        f'<rect width="{w}" height="{h}" fill="url(#bg)"/>',
        f'<rect width="{w}" height="8" fill="url(#ab)"/>',
        f'<text x="512" y="100" text-anchor="middle" font-size="52" fill="{INK}" font-family="{FONT}" font-weight="800">AI 黑科技全家桶</text>',
        f'<text x="512" y="145" text-anchor="middle" font-size="24" fill="{INK2}" font-family="{FONT}" font-weight="500">四个功能，覆盖 90% 创作场景</text>',
        f'<line x1="312" y1="170" x2="712" y2="170" stroke="{BLUE}" stroke-width="3" stroke-linecap="round" opacity="0.25"/>',
    ]
    for i, (icon, name, desc, color) in enumerate(items):
        col = i % 2
        row = i // 2
        cx = 60 + col * 490
        cy = 210 + row * 330
        lines = desc.split("\n")
        parts.append(f'<rect x="{cx}" y="{cy}" width="430" height="280" rx="24" fill="{WHITE}" filter="url(#sh)"/>')
        parts.append(f'<rect x="{cx}" y="{cy}" width="430" height="6" rx="24" fill="{color}"/>')
        parts.append(f'<text x="{cx + 30}" y="{cy + 65}" font-size="48" font-family="sans-serif">{icon}</text>')
        parts.append(f'<text x="{cx + 95}" y="{cy + 65}" font-size="32" fill="{color}" font-family="{FONT}" font-weight="800">{name}</text>')
        for li, line in enumerate(lines):
            parts.append(f'<text x="{cx + 30}" y="{cy + 120 + li * 45}" font-size="22" fill="{INK2}" font-family="{FONT}" font-weight="500">{line}</text>')
    parts.append(f'<text x="512" y="960" text-anchor="middle" font-size="16" fill="{INK3}" font-family="{FONT}">github.com/OpenCut-app/OpenCut</text>')
    return svg(w, h, parts)


def main():
    cards = [
        ("opencut-cover", cover()),
        ("opencut-card-1", card_features()),
        ("opencut-card-2", card_compare()),
        ("opencut-card-3", card_ai()),
    ]
    for name, svg_content in cards:
        svg_path = os.path.join(OUT, f"{name}.svg")
        png_path = os.path.join(OUT, f"{name}.png")
        with open(svg_path, "w") as f:
            f.write(svg_content)
        subprocess.run(["inkscape", svg_path, "-o", png_path, "-w", "1024", "-h", "1024"], check=True, capture_output=True, timeout=30)
        sz = os.path.getsize(png_path) // 1024
        print(f"  {name}.png ({sz} KB)")
    print("Done! 4 cards generated.")


if __name__ == "__main__":
    main()