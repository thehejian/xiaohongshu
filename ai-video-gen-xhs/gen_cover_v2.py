#!/usr/bin/env python3
"""小红书爆款封面 v2"""
import subprocess
from pathlib import Path

W, H = 1024, 1024

def gen_svg(out):
    parts = []
    parts.append('<?xml version="1.0" encoding="UTF-8"?>')
    parts.append('<svg width="1024" height="1024" xmlns="http://www.w3.org/2000/svg">')
    
    # 紫粉渐变
    parts.append('  <defs>')
    parts.append('    <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">')
    parts.append('      <stop offset="0%" stop-color="#6366F1"/>')
    parts.append('      <stop offset="50%" stop-color="#8B5CF6"/>')
    parts.append('      <stop offset="100%" stop-color="#EC4899"/>')
    parts.append('    </linearGradient>')
    parts.append('    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">')
    parts.append('      <feGaussianBlur stdDeviation="10" result="blur"/>')
    parts.append('      <feComposite in="SourceGraphic" in2="blur" operator="over"/>')
    parts.append('    </filter>')
    parts.append('    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">')
    parts.append('      <feDropShadow dx="4" dy="8" stdDeviation="20" flood-color="#000" flood-opacity="0.3"/>')
    parts.append('    </filter>')
    parts.append('  </defs>')
    
    # 背景
    parts.append('  <rect width="1024" height="1024" fill="url(#g)"/>')
    
    # 装饰圆
    parts.append('  <circle cx="150" cy="150" r="200" fill="rgba(255,255,255,0.08)"/>')
    parts.append('  <circle cx="874" cy="874" r="200" fill="rgba(255,255,255,0.06)"/>')
    parts.append('  <circle cx="874" cy="150" r="150" fill="rgba(255,255,255,0.05)"/>')
    parts.append('  <circle cx="150" cy="874" r="100" fill="rgba(255,255,255,0.04)"/>')
    
    # 主标题
    parts.append('  <text x="512" y="280" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="110" font-weight="900" fill="#FFFFFF" filter="url(#glow)">AI视频生成</text>')
    parts.append('  <text x="512" y="400" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="80" font-weight="900" fill="#FFFFFF" filter="url(#glow)">6款神器对比</text>')
    
    # 副标题
    parts.append('  <text x="512" y="500" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="32" fill="rgba(255,255,255,0.8)">Sora · Runway · Pika · 可灵 · Vidu · Kling</text>')
    
    # 数字编号装饰
    parts.append('  <circle cx="200" cy="650" r="50" fill="rgba(255,255,255,0.15)"/>')
    parts.append('  <text x="200" y="668" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="32" font-weight="bold" fill="#FFFFFF">01</text>')
    parts.append('  <circle cx="350" cy="650" r="50" fill="rgba(255,255,255,0.1)"/>')
    parts.append('  <text x="350" y="668" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="32" font-weight="bold" fill="#FFFFFF">02</text>')
    parts.append('  <circle cx="500" cy="650" r="50" fill="rgba(255,255,255,0.1)"/>')
    parts.append('  <text x="500" y="668" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="32" font-weight="bold" fill="#FFFFFF">03</text>')
    parts.append('  <circle cx="650" cy="650" r="50" fill="rgba(255,255,255,0.1)"/>')
    parts.append('  <text x="650" y="668" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="32" font-weight="bold" fill="#FFFFFF">04</text>')
    parts.append('  <circle cx="800" cy="650" r="50" fill="rgba(255,255,255,0.1)"/>')
    parts.append('  <text x="800" y="668" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="32" font-weight="bold" fill="#FFFFFF">05</text>')
    parts.append('  <circle cx="900" cy="650" r="50" fill="rgba(255,255,255,0.1)"/>')
    parts.append('  <text x="900" y="668" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="32" font-weight="bold" fill="#FFFFFF">06</text>')
    
    # 底部装饰线
    parts.append('  <rect x="300" y="780" width="424" height="6" rx="3" fill="rgba(255,255,255,0.4)"/>')
    
    # 底部文字
    parts.append('  <text x="512" y="850" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="28" fill="rgba(255,255,255,0.7)">AI视频生成工具盘点</text>')
    
    # 标签
    parts.append('  <rect x="720" y="880" width="220" height="50" rx="25" fill="rgba(255,255,255,0.2)"/>')
    parts.append('  <text x="830" y="912" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="22" fill="#FFFFFF">🔥 爆款推荐</text>')
    
    parts.append('</svg>')
    
    out.write_text('\n'.join(parts), encoding="utf-8")

d = Path(__file__).parent
svg_path = d / "card_cover_v2.svg"
png_path = d / "card_cover_v2.png"
gen_svg(svg_path)
r = subprocess.run(["inkscape", str(svg_path), "--export-type=png", "--export-dpi=100", "--export-filename={}".format(png_path)], capture_output=True, text=True)
if r.returncode == 0:
    print("✅ card_cover_v2.png")
else:
    print("❌ inkscape error")
svg_path.unlink(missing_ok=True)
