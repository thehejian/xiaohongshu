#!/usr/bin/env python3
"""小红书白色卡片风格 v3 - 简洁清爽"""
import subprocess, base64
from pathlib import Path

CARDS = [
    {"num": "01", "title": "Sora", "subtitle": "OpenAI · 文生视频天花板 · 1分钟长视频", "color": "#10B981", "logo_file": "openai.png"},
    {"num": "02", "title": "Runway", "subtitle": "Gen-3 · 老牌玩家 · 功能全面", "color": "#8B5CF6", "logo_file": "runway.png"},
    {"num": "03", "title": "Pika", "subtitle": "1.5 · 简单易用 · 免费额度友好", "color": "#06B6D4", "logo_file": "pika.png"},
    {"num": "04", "title": "可灵", "subtitle": "Kling · 国产之光 · 1080p · 免费可用", "color": "#EF4444", "logo_file": "kling.png"},
    {"num": "05", "title": "Vidu", "subtitle": "生数科技 · 国内首批 · 文生图+视频一体化", "color": "#F59E0B", "logo_file": "vidu.png"},
    {"num": "06", "title": "Kling", "subtitle": "商汤 · 画质细腻 · 中文prompt友好", "color": "#EC4899", "logo_file": "sensetime.png"},
]

W, H = 1024, 1024
CARD_X, CARD_Y = 60, 60
CARD_W, CARD_H = 904, 904
HEADER_H = 200
HEADER_C = CARD_Y + HEADER_H // 2  # 160
LOGO_DIR = Path(__file__).parent / "logos"

def load_logo_data_uri(logo_file):
    if not logo_file: return None
    logo_path = LOGO_DIR / logo_file
    if not logo_path.exists(): return None
    data = base64.b64encode(logo_path.read_bytes()).decode()
    return "data:image/png;base64," + data

def gen_svg(c, out):
    num = c["num"]
    title = c["title"]
    subtitle = c["subtitle"]
    color = c["color"]
    logo_uri = load_logo_data_uri(c["logo_file"])
    
    parts = []
    parts.append('<?xml version="1.0" encoding="UTF-8"?>')
    parts.append('<svg width="1024" height="1024" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">')
    
    # 浅灰背景
    parts.append('  <rect width="1024" height="1024" fill="#F5F5F5"/>')
    
    # 白色卡片
    parts.append('  <rect x="60" y="60" width="904" height="904" rx="24" fill="#FFFFFF" stroke="#E5E5E5" stroke-width="1"/>')
    
    # 顶部彩色条
    parts.append('  <rect x="60" y="60" width="904" height="200" rx="24" fill="{}"/>'.format(color))
    parts.append('  <rect x="60" y="60" width="904" height="24" fill="{}"/>'.format(color))
    
    # 数字编号
    parts.append('  <text x="130" y="{}" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="56" font-weight="900" fill="rgba(255,255,255,0.9)">{}</text>'.format(HEADER_C + 8, num))
    
    # 大标题
    parts.append('  <text x="512" y="{}" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="64" font-weight="800" fill="#FFFFFF">{}</text>'.format(HEADER_C - 20, title))
    
    # Logo
    if logo_uri:
        parts.append('  <image x="382" y="340" width="260" height="260" xlink:href="{}"/>'.format(logo_uri))
    
    # 副标题
    parts.append('  <text x="512" y="680" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="28" fill="#666666">{}</text>'.format(subtitle))
    
    # 装饰线
    parts.append('  <rect x="350" y="720" width="224" height="3" rx="1.5" fill="{}" opacity="0.3"/>'.format(color))
    
    # 底部文字
    parts.append('  <text x="512" y="820" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="22" fill="#999999">AI视频生成工具盘点</text>')
    
    parts.append('</svg>')
    
    out.write_text('\n'.join(parts), encoding="utf-8")

def to_png(svg_path, png_path):
    r = subprocess.run(["inkscape", str(svg_path), "--export-type=png", "--export-dpi=100", "--export-filename={}".format(png_path)], capture_output=True, text=True)
    return r.returncode == 0

def main():
    d = Path(__file__).parent
    print("🎨 生成白色卡片 v3（简洁风格）...")
    for i, c in enumerate(CARDS):
        svg_path = d / "card_v3_{:02d}.svg".format(i+1)
        png_path = d / "card_v3_{:02d}.png".format(i+1)
        print("  {}/{} {} [{}]" .format(i+1, len(CARDS), c["title"], c["logo_file"]))
        gen_svg(c, svg_path)
        if to_png(svg_path, png_path):
            print("    ✅ {}".format(png_path.name))
        else:
            print("    ❌ inkscape error")
        svg_path.unlink(missing_ok=True)
    print("\n✨ 完成！")

if __name__ == "__main__":
    main()
