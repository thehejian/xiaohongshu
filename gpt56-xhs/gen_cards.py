#!/usr/bin/env python3
"""GPT-5.6炸裂更新 — 卡片生成"""
import base64, subprocess
from pathlib import Path

IMG_DIR = Path(__file__).parent / "image-cards" / "gpt56"
OUT_DIR = Path(__file__).parent
CX = 512
STROKE = 'stroke="#000000" stroke-width="5" stroke-linejoin="round" paint-order="stroke fill"'
STROKE_L = 'stroke="#000000" stroke-width="3" stroke-linejoin="round" paint-order="stroke fill"'

def b64img(name):
    return base64.b64encode((IMG_DIR / name).read_bytes()).decode()

def tx(text, x=CX, y=0, size=32, fill="#FFFFFF", weight="normal", family="system-ui,sans-serif", stroke=None):
    s = stroke or STROKE
    return '<text x="{}" y="{}" text-anchor="middle" font-family="{}" font-size="{}" font-weight="{}" fill="{}" {}>{}</text>'.format(
        x, y, family, size, weight, fill, s, text)

def card_svg(bg_file, extra):
    image_b64 = b64img(bg_file)
    tmpl = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="1024" height="1024" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="fade" x1="0%" y1="50%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#000" stop-opacity="0"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0.88"/>
    </linearGradient>
    <linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3B82F6" stop-opacity="0"/>
      <stop offset="50%" stop-color="#3B82F6" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#3B82F6" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <image width="1024" height="1024" href="data:image/png;base64,__B64__"/>
  __EXTRA__
</svg>'''
    tmpl = tmpl.replace('__B64__', image_b64).replace('__EXTRA__', extra)
    return tmpl

F = 'system-ui,-apple-system,sans-serif'

def gen_cover():
    return card_svg("01-cover0_0.png", '''
  <rect x="0" y="340" width="1024" height="684" fill="url(#fade)"/>
  <rect x="312" y="530" width="400" height="3" rx="1.5" fill="url(#accent)"/>
  {t1}
  {t2}
  {t3}
  {t4}
'''.format(
    t1=tx("GPT-5.6炸裂更新", y=470, size=84, weight="900", family=F),
    t2=tx("1.5M上下文 · 编程飞跃 · 降价", y=550, size=36, fill="#60A5FA", weight="600"),
    t3=tx("OpenAI再次出手，这次太狠了", y=660, size=28, fill="#E5E7EB"),
    t4=tx("# AI  # GPT  # 科技前线", y=760, size=24, fill="#D1D5DB", stroke=STROKE_L),
))

def gen_card2():
    return card_svg("02-card10_0.png", '''
  <rect x="0" y="370" width="1024" height="654" fill="url(#fade)"/>
  {t1}
  <rect x="312" y="490" width="400" height="3" rx="1.5" fill="url(#accent)"/>
  {t2}
  {t3}
  {t4}
  {t5}
  {t6}
'''.format(
    t1=tx("1.5M上下文窗口", y=450, size=56, weight="900", family=F),
    t2=tx("一次塞进三本《三体》", y=570, size=38),
    t3=tx("超长文档直接丢进去就能聊", y=640, size=36),
    t4=tx("整库代码分析也不在话下", y=720, size=34),
    t5=tx("GPT-5.5的1M → 1.5M", y=810, size=28, fill="#60A5FA", weight="600"),
    t6=tx("40%的提升", y=850, size=26, fill="#9CA3AF", stroke=STROKE_L),
))

def gen_card3():
    return card_svg("03-card20_0.png", '''
  <rect x="0" y="350" width="1024" height="674" fill="url(#fade)"/>
  {t1}
  <rect x="312" y="470" width="400" height="3" rx="1.5" fill="url(#accent)"/>
  {t2}
  {t3}
  {t4}
  {t5}
  {t6}
  {t7}
'''.format(
    t1=tx("Agentic Coding 飞跃", y=440, size=56, weight="900", family=F),
    t2=tx("自动debug · 自动规划 · 多步执行", y=560, size=36),
    t3=tx("代码写一半它自动帮你纠错", y=630, size=34),
    t4=tx("Codex UltraFast 模式", y=700, size=38, fill="#60A5FA", weight="600"),
    t5=tx("推理速度提升2-5倍", y=770, size=34),
    t6=tx("编程基准测试全面领先", y=840, size=28, fill="#E5E7EB"),
    t7=tx("开发者狂喜", y=880, size=26, fill="#9CA3AF", stroke=STROKE_L),
))

def gen_card4():
    return card_svg("04-card30_0.png", '''
  <rect x="0" y="370" width="1024" height="654" fill="url(#fade)"/>
  {t1}
  <rect x="312" y="490" width="400" height="3" rx="1.5" fill="url(#accent)"/>
  {t2}
  {t3}
  {t4}
  {t5}
  {t6}
'''.format(
    t1=tx("推理升级 · 幻觉降60%", y=440, size=54, weight="900", family=F),
    t2=tx("医学·法律·金融接近专家水平", y=570, size=36),
    t3=tx("幻觉率相较GPT-5.5再降60%", y=640, size=34),
    t4=tx("复杂推理大幅提升", y=720, size=38, fill="#60A5FA", weight="600"),
    t5=tx("对标Claude Opus 4.8", y=790, size=34),
    t6=tx("甚至正面硬刚Fable 5", y=850, size=28, fill="#E5E7EB", stroke=STROKE_L),
))

def gen_card5():
    return card_svg("05-card40_0.png", '''
  <rect x="0" y="360" width="1024" height="664" fill="url(#fade)"/>
  <rect x="312" y="480" width="400" height="3" rx="1.5" fill="url(#accent)"/>
  {t1}
  {t2}
  {t3}
  {t4}
  {t5}
  {t6}
  {t7}
'''.format(
    t1=tx("降价 + 6月发布", y=460, size=60, weight="900", family=F),
    t2=tx("调用成本比GPT-5.5更低", y=570, size=36),
    t3=tx("OpenAI用规模效应狠卷价格", y=630, size=34),
    t4=tx("预计6月25日前后上线", y=710, size=38, fill="#60A5FA", weight="600"),
    t5=tx("Plus/Pro先用 → API随后", y=780, size=34),
    t6=tx("——", y=840, size=28, fill="#9CA3AF"),
    t7=tx("你觉得能打过Claude Fable 5吗？对此你打几分？👇", y=880, size=30, fill="#60A5FA", weight="bold"),
))

def to_png(svg_path, png_path):
    r = subprocess.run(
        ["inkscape", str(svg_path), "--export-type=png",
         "--export-dpi=100", "--export-filename={}".format(png_path)],
        capture_output=True, text=True
    )
    return r.returncode == 0

def main():
    cards = [
        ("gpt56-cover", gen_cover),
        ("gpt56-card-1", gen_card2),
        ("gpt56-card-2", gen_card3),
        ("gpt56-card-3", gen_card4),
        ("gpt56-card-4", gen_card5),
    ]
    print("生成GPT-5.6卡片...")
    for name, fn in cards:
        svg = OUT_DIR / "{}.svg".format(name)
        png = OUT_DIR / "{}.png".format(name)
        svg.write_text(fn(), encoding="utf-8")
        print("  {} ".format(name), end="")
        if to_png(svg, png):
            print("OK")
        else:
            print("FAIL")
        svg.unlink(missing_ok=True)
    print("完成！")

if __name__ == "__main__":
    main()
