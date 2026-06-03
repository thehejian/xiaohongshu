#!/usr/bin/env python3
"""小红书爆款风格卡片 v2 - 渐变 + 大标题 + 数字编号 + 真实Logo"""
import subprocess, base64
from pathlib import Path

CARDS = [
    {"num": "01", "title": "Sora", "subtitle": "OpenAI · 文生视频天花板", "bg_top": "#10B981", "bg_bot": "#059669", "accent": "#F59E0B", "logo_file": "openai.png"},
    {"num": "02", "title": "Runway", "subtitle": "Gen-3 · 老牌视频AI", "bg_top": "#8B5CF6", "bg_bot": "#7C3AED", "accent": "#EC4899", "logo_file": "runway.png"},
    {"num": "03", "title": "Pika", "subtitle": "1.5 · 免费动画神器", "bg_top": "#06B6D4", "bg_bot": "#0891B2", "accent": "#F97316", "logo_file": "pika.png"},
    {"num": "04", "title": "可灵", "subtitle": "Kling · 国产之光🔥", "bg_top": "#EF4444", "bg_bot": "#DC2626", "accent": "#FBBF24", "logo_file": "kling.png"},
    {"num": "05", "title": "Vidu", "subtitle": "生数科技 · 首批上线", "bg_top": "#F59E0B", "bg_bot": "#D97706", "accent": "#10B981", "logo_file": "vidu.png"},
    {"num": "06", "title": "Kling", "subtitle": "商汤 · 画质细腻", "bg_top": "#EC4899", "bg_bot": "#DB2777", "accent": "#8B5CF6", "logo_file": "sensetime.png"},
]

W, H = 1024, 1024
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
    bg_top = c["bg_top"]
    bg_bot = c["bg_bot"]
    accent = c["accent"]
    logo_uri = load_logo_data_uri(c["logo_file"])
    
    parts = []
    parts.append('<?xml version="1.0" encoding="UTF-8"?>')
    parts.append('<svg width="1024" height="1024" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">')
    
    # 渐变定义
    parts.append('  <defs>')
    parts.append('    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">')
    parts.append('      <stop offset="0%" stop-color="{}"/>'.format(bg_top))
    parts.append('      <stop offset="100%" stop-color="{}"/>'.format(bg_bot))
    parts.append('    </linearGradient>')
    parts.append('    <linearGradient id="grad2" x1="0%" y1="100%" x2="0%" y2="0%">')
    parts.append('      <stop offset="0%" stop-color="{}"/>'.format(bg_bot))
    parts.append('      <stop offset="100%" stop-color="{}"/>'.format(bg_top))
    parts.append('    </linearGradient>')
    parts.append('    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">')
    parts.append('      <feGaussianBlur stdDeviation="8" result="blur"/>')
    parts.append('      <feComposite in="SourceGraphic" in2="blur" operator="over"/>')
    parts.append('    </filter>')
    parts.append('    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">')
    parts.append('      <feDropShadow dx="4" dy="8" stdDeviation="16" flood-color="#000" flood-opacity="0.3"/>')
    parts.append('    </filter>')
    parts.append('  </defs>')
    
    # 背景渐变
    parts.append('  <rect width="1024" height="1024" fill="url(#grad)"/>')
    
    # 装饰圆
    parts.append('  <circle cx="150" cy="150" r="200" fill="rgba(255,255,255,0.08)"/>')
    parts.append('  <circle cx="874" cy="874" r="150" fill="rgba(255,255,255,0.06)"/>')
    parts.append('  <circle cx="874" cy="150" r="100" fill="rgba(255,255,255,0.05)"/>')
    
    # 左侧数字编号大圆
    parts.append('  <circle cx="160" cy="200" r="100" fill="rgba(255,255,255,0.15)" filter="url(#glow)"/>')
    parts.append('  <circle cx="160" cy="200" r="90" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="3"/>')
    parts.append('  <text x="160" y="230" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="72" font-weight="900" fill="#FFFFFF">{}</text>'.format(num))
    
    # 大标题
    parts.append('  <text x="512" y="260" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="100" font-weight="900" fill="#FFFFFF" filter="url(#glow)">{}</text>'.format(title))
    
    # 副标题
    parts.append('  <text x="512" y="330" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="36" fill="rgba(255,255,255,0.85)">{}</text>'.format(subtitle))
    
    # Logo
    if logo_uri:
        parts.append('  <image x="382" y="400" width="260" height="260" xlink:href="{}" filter="url(#shadow)"/>'.format(logo_uri))
    else:
        parts.append('  <rect x="412" y="432" width="200" height="56" rx="28" fill="rgba(255,255,255,0.2)"/>')
        parts.append('  <text x="512" y="470" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="24" font-weight="700" fill="#FFFFFF">{}</text>'.format(title.upper()))
    
    # 底部装饰线
    parts.append('  <rect x="300" y="720" width="424" height="6" rx="3" fill="rgba(255,255,255,0.4)"/>')
    
    # 底部文字
    parts.append('  <text x="512" y="800" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="28" fill="rgba(255,255,255,0.7)">AI视频生成工具盘点</text>')
    
    # 右下角排名标签
    if num == "04":
        parts.append('  <rect x="750" y="750" width="200" height="60" rx="30" fill="#FBBF24"/>')
        parts.append('  <text x="850" y="790" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="28" font-weight="bold" fill="#0f172a">🥇 国产之光</text>')
    elif num == "01":
        parts.append('  <rect x="750" y="750" width="200" height="60" rx="30" fill="rgba(255,255,255,0.2)"/>')
        parts.append('  <text x="850" y="790" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="24" font-weight="bold" fill="#FFFFFF">潜力满分</text>')
    
    parts.append('</svg>')
    
    out.write_text('\n'.join(parts), encoding="utf-8")

def to_png(svg_path, png_path):
    r = subprocess.run(["inkscape", str(svg_path), "--export-type=png", "--export-dpi=100", "--export-filename={}".format(png_path)], capture_output=True, text=True)
    return r.returncode == 0

def main():
    d = Path(__file__).parent
    print("🎨 生成爆款风格卡片 v2...")
    for i, c in enumerate(CARDS):
        svg_path = d / "card_v2_{:02d}.svg".format(i+1)
        png_path = d / "card_v2_{:02d}.png".format(i+1)
        print("  {}/{} {} [{}]" .format(i+1, len(CARDS), c["title"], c["logo_file"]))
        gen_svg(c, svg_path)
        if to_png(svg_path, png_path):
            print("    ✅ {}".format(png_path.name))
        else:
            print("    ❌ inkscape error: {}".format(r.stderr[:200] if 'r' in dir() else "unknown"))
        svg_path.unlink(missing_ok=True)
    print("\n✨ 完成！")

if __name__ == "__main__":
    main()
