#!/usr/bin/env python3
"""Generate Xiaohongshu-style card images for AI paper tools."""

import subprocess
import os

WIDTH = 1024
HEIGHT = 1024

# Light palette (XHS-friendly)
BG = "#FAF7F2"
WHITE = "#FFFFFF"
ACCENTS = {
    "paperpal": "#6366F1",   # Indigo
    "scite": "#10B981",      # Emerald
    "elicit": "#F59E0B",     # Amber
    "connected_papers": "#EF4444",  # Red
    "jenni": "#8B5CF6",      # Violet
}

TOOLS = [
    {
        "name": "Paperpal",
        "tagline": "论文润色专家",
        "color": ACCENTS["paperpal"],
        "icon": "✏️",
        "desc": "语法纠错 + 学术表达优化"
    },
    {
        "name": "Scite",
        "tagline": "智能引用分析",
        "color": ACCENTS["scite"],
        "icon": "🔗",
        "desc": "告诉你论文被如何引用"
    },
    {
        "name": "Elicit",
        "tagline": "文献检索助手",
        "color": ACCENTS["elicit"],
        "icon": "🔍",
        "desc": "输入关键词秒出相关论文"
    },
    {
        "name": "Connected Papers",
        "tagline": "文献关联图谱",
        "color": ACCENTS["connected_papers"],
        "icon": "🕸️",
        "desc": "可视化展示论文引用关系"
    },
    {
        "name": "Jenni",
        "tagline": "AI写作助手",
        "color": ACCENTS["jenni"],
        "icon": "🤖",
        "desc": "边写边补全，像有导师指导"
    }
]

def generate_svg(tool, output_path):
    """Generate SVG for a tool card."""
    color = tool["color"]
    
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="{WIDTH}" height="{HEIGHT}" fill="{BG}"/>
  
  <!-- Center card -->
  <rect x="112" y="180" width="800" height="664" rx="32" fill="{WHITE}" stroke="{color}" stroke-width="4"/>
  
  <!-- Top accent bar -->
  <rect x="112" y="180" width="800" height="12" rx="32" fill="{color}"/>
  <rect x="112" y="284" width="800" height="12" rx="6" fill="{color}"/>
  
  <!-- Icon -->
  <text x="512" y="380" text-anchor="middle" font-size="120">{tool["icon"]}</text>
  
  <!-- Tool name -->
  <text x="512" y="500" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-size="56" font-weight="bold" fill="#1F2937">{tool["name"]}</text>
  
  <!-- Tagline -->
  <text x="512" y="580" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-size="32" fill="{color}">{tool["tagline"]}</text>
  
  <!-- Description -->
  <text x="512" y="660" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-size="28" fill="#6B7280">{tool["desc"]}</text>
  
  <!-- Bottom decoration -->
  <circle cx="200" cy="880" r="20" fill="{color}" opacity="0.1"/>
  <circle cx="824" cy="880" r="20" fill="{color}" opacity="0.1"/>
  <circle cx="512" cy="900" r="8" fill="{color}" opacity="0.2"/>
  
  <!-- Bottom accent -->
  <rect x="112" y="844" width="800" height="12" rx="6" fill="{color}" opacity="0.1"/>
</svg>'''
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg)

def main():
    output_dir = os.path.dirname(os.path.abspath(__file__))
    
    for tool in TOOLS:
        svg_path = os.path.join(output_dir, f"{tool['name'].lower().replace(' ', '_')}.svg")
        png_path = os.path.join(output_dir, f"{tool['name'].lower().replace(' ', '_')}.png")
        
        print(f"Generating {tool['name']}...")
        
        # Generate SVG
        generate_svg(tool, svg_path)
        
        # Convert to PNG with Inkscape
        try:
            result = subprocess.run(
                ["inkscape", svg_path, f"--export-type=png", f"--export-width={WIDTH}", f"--export-height={HEIGHT}", f"--export-filename={png_path}"],
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
    
    print("\nDone! Generated 5 SVG files.")

if __name__ == "__main__":
    main()
