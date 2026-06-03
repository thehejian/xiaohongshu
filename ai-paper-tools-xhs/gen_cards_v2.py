#!/usr/bin/env python3
"""Generate Xiaohongshu-style card images v2 - more eye-catching design."""

import subprocess
import os

WIDTH = 1024
HEIGHT = 1024

# More vibrant XHS-style palette
ACCENTS = {
    "paperpal": {
        "primary": "#6366F1",
        "gradient_start": "#818CF8",
        "gradient_end": "#6366F1",
        "bg": "#EEF2FF"
    },
    "scite": {
        "primary": "#10B981",
        "gradient_start": "#34D399",
        "gradient_end": "#10B981",
        "bg": "#ECFDF5"
    },
    "elicit": {
        "primary": "#F59E0B",
        "gradient_start": "#FBBF24",
        "gradient_end": "#F59E0B",
        "bg": "#FFFBEB"
    },
    "connected_papers": {
        "primary": "#EF4444",
        "gradient_start": "#F87171",
        "gradient_end": "#EF4444",
        "bg": "#FEF2F2"
    },
    "jenni": {
        "primary": "#8B5CF6",
        "gradient_start": "#A78BFA",
        "gradient_end": "#8B5CF6",
        "bg": "#FAF5FF"
    }
}

TOOLS = [
    {
        "name": "Paperpal",
        "tagline": "论文润色",
        "number": "01",
        "icon": "✏️",
        "desc": "语法纠错 · 学术表达",
        "color_key": "paperpal"
    },
    {
        "name": "Scite",
        "tagline": "智能引用",
        "number": "02",
        "icon": "🔗",
        "desc": "看论文被如何引用",
        "color_key": "scite"
    },
    {
        "name": "Elicit",
        "tagline": "文献检索",
        "number": "03",
        "icon": "🔍",
        "desc": "关键词秒出论文",
        "color_key": "elicit"
    },
    {
        "name": "Connected Papers",
        "tagline": "关联图谱",
        "number": "04",
        "icon": "🕸️",
        "desc": "可视化引用关系",
        "color_key": "connected_papers"
    },
    {
        "name": "Jenni",
        "tagline": "AI写作",
        "number": "05",
        "icon": "🤖",
        "desc": "边写边补全",
        "color_key": "jenni"
    }
]

def generate_svg(tool, output_path):
    """Generate SVG for a tool card - XHS style."""
    colors = ACCENTS[tool["color_key"]]
    primary = colors["primary"]
    grad_start = colors["gradient_start"]
    grad_end = colors["gradient_end"]
    bg = colors["bg"]
    
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Gradient for top bar -->
    <linearGradient id="gradTop" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:{grad_start}"/>
      <stop offset="100%" style="stop-color:{grad_end}"/>
    </linearGradient>
    <!-- Gradient for card shadow -->
    <linearGradient id="gradCard" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#FFFFFF"/>
      <stop offset="100%" style="stop-color:#F9FAFB"/>
    </linearGradient>
    <!-- Drop shadow -->
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="8" stdDeviation="20" flood-color="{primary}" flood-opacity="0.15"/>
    </filter>
  </defs>
  
  <!-- Background with subtle pattern -->
  <rect width="{WIDTH}" height="{HEIGHT}" fill="{bg}"/>
  
  <!-- Decorative circles -->
  <circle cx="100" cy="100" r="60" fill="{primary}" opacity="0.05"/>
  <circle cx="924" cy="100" r="80" fill="{primary}" opacity="0.05"/>
  <circle cx="100" cy="924" r="70" fill="{primary}" opacity="0.05"/>
  <circle cx="924" cy="924" r="50" fill="{primary}" opacity="0.05"/>
  
  <!-- Top accent bar -->
  <rect x="0" y="0" width="{WIDTH}" height="16" fill="url(#gradTop)"/>
  
  <!-- Main card with shadow -->
  <rect x="80" y="80" width="864" height="864" rx="40" fill="url(#gradCard)" filter="url(#shadow)"/>
  
  <!-- Number badge -->
  <circle cx="160" cy="160" r="48" fill="url(#gradTop)"/>
  <text x="160" y="178" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-size="32" font-weight="bold" fill="#FFFFFF">{tool["number"]}</text>
  
  <!-- Icon in circle -->
  <circle cx="512" cy="320" r="120" fill="{primary}" opacity="0.1"/>
  <text x="512" y="380" text-anchor="middle" font-size="100">{tool["icon"]}</text>
  
  <!-- Tool name - BIG -->
  <text x="512" y="520" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-size="72" font-weight="900" fill="#1F2937">{tool["name"]}</text>
  
  <!-- Tagline with accent -->
  <text x="512" y="600" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-size="36" font-weight="600" fill="{primary}">{tool["tagline"]}</text>
  
  <!-- Divider line -->
  <line x1="312" y1="640" x2="712" y2="640" stroke="{primary}" stroke-width="3" stroke-linecap="round" opacity="0.3"/>
  
  <!-- Description -->
  <text x="512" y="700" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-size="28" fill="#6B7280">{tool["desc"]}</text>
  
  <!-- Bottom accent bar -->
  <rect x="80" y="880" width="864" height="64" rx="32" fill="url(#gradTop)" opacity="0.1"/>
  
  <!-- Small decorative dots -->
  <circle cx="200" cy="810" r="8" fill="{primary}" opacity="0.2"/>
  <circle cx="230" cy="810" r="8" fill="{primary}" opacity="0.2"/>
  <circle cx="260" cy="810" r="8" fill="{primary}" opacity="0.2"/>
  <circle cx="764" cy="810" r="8" fill="{primary}" opacity="0.2"/>
  <circle cx="794" cy="810" r="8" fill="{primary}" opacity="0.2"/>
  <circle cx="824" cy="810" r="8" fill="{primary}" opacity="0.2"/>
</svg>'''
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg)

def main():
    output_dir = os.path.dirname(os.path.abspath(__file__))
    
    for tool in TOOLS:
        svg_path = os.path.join(output_dir, f"{tool['name'].lower().replace(' ', '_')}_v2.svg")
        png_path = os.path.join(output_dir, f"{tool['name'].lower().replace(' ', '_')}_v2.png")
        
        print(f"Generating {tool['name']} v2...")
        
        # Generate SVG
        generate_svg(tool, svg_path)
        
        # Convert to PNG with Inkscape
        try:
            result = subprocess.run(
                ["inkscape", svg_path, "--export-type=png", f"--export-width={WIDTH}", f"--export-height={HEIGHT}", f"--export-filename={png_path}"],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode != 0:
                print(f"  Inkscape error: {result.stderr}")
            else:
                print(f"  ✓ Created {png_path}")
        except FileNotFoundError:
            print(f"  ⚠ Inkscape not found, SVG saved at {svg_path}")
        except subprocess.TimeoutExpired:
            print(f"  ⚠ Inkscape timed out")
    
    print("\nDone! Generated 5 v2 SVG files.")

if __name__ == "__main__":
    main()
