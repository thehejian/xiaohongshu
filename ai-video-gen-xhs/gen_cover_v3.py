#!/usr/bin/env python3
"""小红书白色卡片封面 v3 - 简洁清爽"""
import subprocess
from pathlib import Path

W, H = 1024, 1024

def gen_svg(out):
    parts = []
    parts.append('<?xml version="1.0" encoding="UTF-8"?>')
    parts.append('<svg width="1024" height="1024" xmlns="http://www.w3.org/2000/svg">')
    
    # 浅灰背景
    parts.append('  <rect width="1024" height="1024" fill="#F5F5F5"/>')
    
    # 白色卡片
    parts.append('  <rect x="60" y="60" width="904" height="904" rx="24" fill="#FFFFFF" stroke="#E5E5E5" stroke-width="1"/>')
    
    # 顶部渐变条
    parts.append('  <defs>')
    parts.append('    <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="0%">')
    parts.append('      <stop offset="0%" stop-color="#6366F1"/>')
    parts.append('      <stop offset="100%" stop-color="#EC4899"/>')
    parts.append('    </linearGradient>')
    parts.append('  </defs>')
    parts.append('  <rect x="60" y="60" width="904" height="200" rx="24" fill="url(#g)"/>')
    parts.append('  <rect x="60" y="60" width="904" height="24" fill="url(#g)"/>')
    
    # 主标题
    parts.append('  <text x="512" y="140" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="64" font-weight="800" fill="#FFFFFF">AI视频生成</text>')
    parts.append('  <text x="512" y="210" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="56" font-weight="800" fill="#FFFFFF">6款神器对比</text>')
    
    # 副标题
    parts.append('  <text x="512" y="320" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="28" fill="#666666">Sora · Runway · Pika · 可灵 · Vidu · Kling</text>')
    
    # 数字编号
    for i, x in enumerate([160, 300, 440, 580, 720, 860]):
        parts.append('  <rect x="{}" y="400" width="80" height="80" rx="40" fill="#6366F1"/>'.format(x - 40))
        parts.append('  <text x="{}" y="452" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="28" font-weight="bold" fill="#FFFFFF">{}</text>'.format(x, i+1))
    
    # 装饰线
    parts.append('  <rect x="350" y="540" width="224" height="3" rx="1.5" fill="#6366F1" opacity="0.3"/>')
    
    # 底部文字
    parts.append('  <text x="512" y="620" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="22" fill="#999999">AI视频生成工具盘点</text>')
    
    parts.append('</svg>')
    
    out.write_text('\n'.join(parts), encoding="utf-8")

d = Path(__file__).parent
svg_path = d / "card_cover_v3.svg"
png_path = d / "card_cover_v3.png"
gen_svg(svg_path)
r = subprocess.run(["inkscape", str(svg_path), "--export-type=png", "--export-dpi=100", "--export-filename={}".format(png_path)], capture_output=True, text=True)
if r.returncode == 0:
    print("✅ card_cover_v3.png")
else:
    print("❌ inkscape error")
svg_path.unlink(missing_ok=True)
