#!/usr/bin/env python3
"""AI视频生成工具卡片 - 白色文字 + base64内嵌产品Logo"""
import subprocess, base64
from pathlib import Path

CARDS = [
    {"title": "AI视频生成", "title2": "6款神器对比", "subtitle": "Sora · Runway · Pika · 可灵 · Vidu · Kling", "bg": "#6366F1", "accent": "#F472B6", "logo_file": None, "file": "card_cover"},
    {"title": "Sora", "title2": "", "subtitle": "OpenAI · 文生视频天花板 · 1分钟长视频", "bg": "#10B981", "accent": "#F59E0B", "logo_file": "openai.png", "file": "card_1"},
    {"title": "Runway", "title2": "Gen-3", "subtitle": "老牌玩家 · 功能全面 · 多模态输入", "bg": "#8B5CF6", "accent": "#EC4899", "logo_file": "runway.png", "file": "card_2"},
    {"title": "Pika", "title2": "1.5", "subtitle": "简单易用 · 免费额度友好 · 动画风格出色", "bg": "#06B6D4", "accent": "#F97316", "logo_file": "pika.png", "file": "card_3"},
    {"title": "可灵", "title2": "Kling", "subtitle": "国产之光！中文理解强 · 1080p · 免费可用", "bg": "#EF4444", "accent": "#FBBF24", "logo_file": "kling.png", "file": "card_4"},
    {"title": "Vidu", "title2": "", "subtitle": "生数科技 · 国内首批 · 文生图+视频一体化", "bg": "#F59E0B", "accent": "#10B981", "logo_file": "vidu.png", "file": "card_5"},
    {"title": "Kling", "title2": "商汤", "subtitle": "商汤技术加持 · 画质细腻 · 中文prompt友好", "bg": "#EC4899", "accent": "#8B5CF6", "logo_file": "sensetime.png", "file": "card_6"},
]

W, H = 1024, 1024
HEADER_H = 260
HEADER_C = 100 + HEADER_H // 2
LOGO_DIR = Path(__file__).parent / "logos"

def load_logo_data_uri(logo_file):
    """加载Logo并返回data URI"""
    if not logo_file:
        return None
    logo_path = LOGO_DIR / logo_file
    if not logo_path.exists():
        return None
    data = base64.b64encode(logo_path.read_bytes()).decode()
    return "data:image/png;base64," + data

def gen_svg(c, out):
    has_title2 = bool(c["title2"])
    
    # 标题
    if has_title2:
        t1 = '<text x="512" y="{}" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="72" font-weight="bold" fill="#FFFFFF">{}</text>'.format(HEADER_C - 35, c["title"])
        t2 = '<text x="512" y="{}" text-anchor="middle" font-family="system-ui,sans-serif" font-size="48" fill="#FFFFFF">{}</text>'.format(HEADER_C + 25, c["title2"])
    else:
        t1 = '<text x="512" y="{}" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="72" font-weight="bold" fill="#FFFFFF">{}</text>'.format(HEADER_C - 15, c["title"])
        t2 = ""
    
    # 副标题 - 白色
    sub = '<text x="512" y="560" text-anchor="middle" font-family="system-ui,sans-serif" font-size="30" fill="#FFFFFF">{}</text>'.format(c["subtitle"])
    
    # Logo - 使用base64 data URI内嵌
    logo_uri = load_logo_data_uri(c["logo_file"])
    if logo_uri:
        if c["logo_file"] == "openai.png":
            # OpenAI六边形图标，居中放大
            logo_svg = '    <image x="382" y="320" width="260" height="260" xlink:href="{}"/>'.format(logo_uri)
        else:
            # 其他文字Logo，水平居中
            logo_svg = '    <image x="{}" y="390" width="{}" height="63" xlink:href="{}"/>'.format(
                512 - 125, 250, logo_uri)
    else:
        # 封面用文字徽章
        logo_svg = '''    <rect x="432" y="392" width="160" height="56" rx="28" fill="rgba(255,255,255,0.10)"/>
    <rect x="433" y="393" width="158" height="54" rx="27" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <text x="512" y="428" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="28" font-weight="800" fill="#FFFFFF" letter-spacing="8">AI</text>'''
    
    parts = []
    parts.append('<?xml version="1.0" encoding="UTF-8"?>')
    parts.append('<svg width="1024" height="1024" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">')
    parts.append('  <defs>')
    parts.append('    <radialGradient id="bg" cx="35%" cy="35%" r="65%">')
    parts.append('      <stop offset="0%" stop-color="{}"/>'.format(c["bg"]))
    parts.append('      <stop offset="100%" stop-color="#0f172a"/>')
    parts.append('    </radialGradient>')
    parts.append('    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">')
    parts.append('      <feDropShadow dx="0" dy="10" stdDeviation="20" flood-color="#000" flood-opacity="0.2"/>')
    parts.append('    </filter>')
    parts.append('  </defs>')
    parts.append('')
    parts.append('  <rect width="1024" height="1024" fill="url(#bg)"/>')
    parts.append('')
    parts.append('  <circle cx="850" cy="150" r="120" fill="{}" opacity="0.06"/>'.format(c["accent"]))
    parts.append('  <circle cx="180" cy="850" r="160" fill="{}" opacity="0.05"/>'.format(c["accent"]))
    parts.append('')
    parts.append('  <rect x="60" y="80" width="904" height="864" rx="36" fill="#ffffff" filter="url(#shadow)"/>')
    parts.append('')
    parts.append('  <rect x="60" y="80" width="904" height="{}" fill="{}"/>'.format(HEADER_H, c["bg"]))
    parts.append('  <rect x="60" y="80" width="904" height="36" rx="36" fill="{}"/>'.format(c["bg"]))
    parts.append('')
    parts.append('  {}'.format(t1))
    parts.append('  {}'.format(t2))
    parts.append('')
    parts.append(logo_svg)
    parts.append('')
    parts.append('  {}'.format(sub))
    parts.append('')
    parts.append('  <rect x="350" y="660" width="324" height="4" rx="2" fill="#FFFFFF" opacity="0.3"/>')
    parts.append('')
    parts.append('  <text x="512" y="880" text-anchor="middle" font-family="system-ui,sans-serif" font-size="24" fill="#FFFFFF">AI视频生成工具盘点</text>')
    parts.append('</svg>')
    
    out.write_text('\n'.join(parts), encoding="utf-8")

def to_png(svg_path, png_path):
    r = subprocess.run(["inkscape", str(svg_path), "--export-type=png", "--export-dpi=100", "--export-filename={}".format(png_path)], capture_output=True, text=True)
    return r.returncode == 0

def main():
    d = Path(__file__).parent
    print("🎨 生成卡片（base64内嵌Logo）...")
    for i, c in enumerate(CARDS):
        svg_path = d / "{}.svg".format(c["file"])
        png_path = d / "{}.png".format(c["file"])
        logo_info = c["logo_file"] if c["logo_file"] else "AI文字徽章"
        print("  {}/{} {} [logo: {}]" .format(i+1, len(CARDS), c["title"], logo_info))
        gen_svg(c, svg_path)
        if to_png(svg_path, png_path):
            print("    ✅ {}".format(png_path.name))
        else:
            print("    ❌ inkscape error")
        svg_path.unlink(missing_ok=True)
    print("\n✨ 完成！")

if __name__ == "__main__":
    main()
