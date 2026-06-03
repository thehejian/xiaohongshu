#!/usr/bin/env python3
"""
AI音乐生成 Suno 5 vs Udio 卡片 — 浅色风格 v2（更抓眼球）
"""
import subprocess
from pathlib import Path

CARDS = [
    {
        "title": "AI写歌",
        "title2": "谁才是真神？",
        "subtitle": "Suno 5 vs Udio 实测",
        "bg": "#6366F1",
        "accent": "#F472B6",
        "icon": "🔥",
        "file": "suno-udio-cover",
        "bottom": "结果意外了",
    },
    {
        "title": "Suno 5",
        "title2": "小白神器",
        "subtitle": "一键出歌 · 中文自然 · 免费够用",
        "bg": "#3B82F6",
        "accent": "#8B5CF6",
        "icon": "⚡",
        "file": "suno-udio-card-suno",
        "bottom": "适合不想动脑的人",
    },
    {
        "title": "Udio",
        "title2": "音质天花板",
        "subtitle": "呼吸声都听得见 · 和声像真人 · 人声逼真",
        "bg": "#EC4899",
        "accent": "#F59E0B",
        "icon": "🎧",
        "file": "suno-udio-card-udio",
        "bottom": "适合追求成品质量",
    },
    {
        "title": "实测对比",
        "title2": "",
        "subtitle": "中文歌词 · 音质 · 速度 · 曲风 四维度PK",
        "bg": "#10B981",
        "accent": "#06B6D4",
        "icon": "🔍",
        "file": "suno-udio-card-compare",
        "bottom": "别光看，去试试",
    },
]

W, H = 1024, 1024
CARD_X, CARD_Y = 60, 80
CARD_W, CARD_H = 904, 864
HEADER_H = 260
HEADER_Y = CARD_Y
HEADER_C = HEADER_Y + HEADER_H // 2

def gen_svg(c, out):
    has_title2 = bool(c["title2"])
    
    if has_title2:
        # 双行标题：78px + 44px，整体在色块中垂直居中
        # 78px: ascent≈60, descent≈18; 44px: ascent≈34, descent≈10; gap≈15
        # 总视觉高度 ≈ 163px, 色块中心 y=210 → 第一行基线 ≈ 188
        t1_y = 188
        t2_y = t1_y + 93  # 78 + 15 gap
        t1 = '<text x="512" y="{}" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="78" font-weight="bold" fill="#FFFFFF">{}</text>'.format(t1_y, c["title"])
        t2 = '<text x="512" y="{}" text-anchor="middle" font-family="system-ui,sans-serif" font-size="44" fill="#E0E7FF">{}</text>'.format(t2_y, c["title2"])
    else:
        # 单行标题：78px，视觉中心在色块中心 y=210
        # 基线 = center + (height/2 - ascent) = 210 + (39 - 60) = 231
        t1_y = 231
        t1 = '<text x="512" y="{}" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="78" font-weight="bold" fill="#FFFFFF">{}</text>'.format(t1_y, c["title"])
        t2 = ""
    
    sub = '<text x="512" y="580" text-anchor="middle" font-family="system-ui,sans-serif" font-size="28" fill="#64748B">{}</text>'.format(c["subtitle"])
    bottom = '<text x="512" y="860" text-anchor="middle" font-family="system-ui,sans-serif" font-size="22" fill="#94A3B8">{}</text>'.format(c["bottom"])
    
    # 浅色风格：米白背景 + 白色卡片 + 彩色顶部色块
    svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="1024" height="1024" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F1F5F9"/>
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="12" stdDeviation="24" flood-color="#000" flood-opacity="0.08"/>
    </filter>
  </defs>
  
  <!-- 浅色背景 -->
  <rect width="1024" height="1024" fill="url(#bg)"/>
  
  <!-- 装饰圆（浅色柔和） -->
  <circle cx="850" cy="150" r="120" fill="{BG}" opacity="0.08"/>
  <circle cx="180" cy="850" r="160" fill="{BG}" opacity="0.06"/>
  
  <!-- 白色卡片 -->
  <rect x="60" y="80" width="904" height="864" rx="36" fill="#ffffff" filter="url(#shadow)"/>
  
  <!-- 顶部色块（只圆上角） -->
  <rect x="60" y="80" width="904" height="{HH}" fill="{BG}"/>
  <rect x="60" y="80" width="904" height="36" rx="36" fill="{BG}"/>
  
  <!-- 标题 -->
  {T1}
  {T2}
  
  <!-- 图标 -->
  <text x="512" y="460" text-anchor="middle" font-size="96">{IC}</text>
  
  <!-- 副标题 -->
  {SUB}
  
  <!-- 装饰线 -->
  <rect x="350" y="680" width="324" height="4" rx="2" fill="{AC}" opacity="0.4"/>
  
  <!-- 底部文字 -->
  {BTM}
</svg>'''.format(HH=HEADER_H, BG=c["bg"], T1=t1, T2=t2, IC=c["icon"], SUB=sub, AC=c["accent"], BTM=bottom)
    
    out.write_text(svg, encoding="utf-8")

def to_png(svg_path, png_path):
    r = subprocess.run(["inkscape", str(svg_path), "--export-type=png", "--export-dpi=100", "--export-filename={}".format(png_path)], capture_output=True, text=True)
    return r.returncode == 0

def main():
    d = Path(__file__).parent
    print("🎨 生成抓眼球卡片 v2...")
    for i, c in enumerate(CARDS):
        svg_path = d / "{}.svg".format(c["file"])
        png_path = d / "{}.png".format(c["file"])
        print("  {}/{} {}".format(i+1, len(CARDS), c["title"]))
        gen_svg(c, svg_path)
        if to_png(svg_path, png_path):
            print("    ✅ {}".format(png_path.name))
        else:
            print("    ❌ inkscape error")
        svg_path.unlink(missing_ok=True)
    print("\n✨ 完成！")

if __name__ == "__main__":
    main()
