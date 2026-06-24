#!/usr/bin/env python3
"""李光弼到底有没有反心 — 卡片生成 v2（黑色描边+大字）"""
import base64, subprocess
from pathlib import Path

IMG_DIR = Path(__file__).parent / "image-cards" / "liguangbi-loyalty"
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
    <linearGradient id="fade" x1="0%" y1="55%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#000" stop-opacity="0"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0.85"/>
    </linearGradient>
    <linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F59E0B" stop-opacity="0"/>
      <stop offset="50%" stop-color="#F59E0B" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#F59E0B" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <image width="1024" height="1024" href="data:image/png;base64,__B64__"/>
  __EXTRA__
</svg>'''
    tmpl = tmpl.replace('__B64__', image_b64).replace('__EXTRA__', extra)
    return tmpl

F = 'system-ui,-apple-system,sans-serif'
SF = 'system-ui,sans-serif'

def gen_cover():
    return card_svg("01-cover-liguangbi-loyalty.png", '''
  <rect x="0" y="350" width="1024" height="674" fill="url(#fade)"/>
  <rect x="312" y="560" width="400" height="3" rx="1.5" fill="url(#accent)"/>
  {t1}
  {t2}
  {t3}
  {t4}
'''.format(
    t1=tx("李光弼到底有没有反心", y=490, size=84, weight="900", family=F),
    t2=tx("安史之乱功臣的忠诚之谜", y=550, size=34, fill="#FCD34D", weight="600"),
    t3=tx("一段被误解的历史 · 一个将军的困境", y=660, size=28, fill="#E5E7EB"),
    t4=tx("# 历史真相  # 唐朝名将", y=760, size=24, fill="#D1D5DB", stroke=STROKE_L),
))

def gen_card2():
    return card_svg("02-content-liguangbi-loyalty.png", '''
  <rect x="0" y="380" width="1024" height="644" fill="url(#fade)"/>
  {t1}
  <rect x="312" y="500" width="400" height="3" rx="1.5" fill="url(#accent)"/>
  {t2}
  {t3}
  {t4}
  {t5}
  {t6}
'''.format(
    t1=tx('战功赫赫的"反贼"？', y=460, size=60, weight="900", family=F),
    t2=tx("与郭子仪并称「李郭」", y=570, size=36),
    t3=tx("太原之战以少胜多", y=630, size=36),
    t4=tx("河阳之战扭转战局", y=690, size=36),
    t5=tx("同样的战功，不同的结局", y=770, size=28, fill="#9CA3AF", stroke=STROKE_L),
    t6=tx("郭子仪善终 · 李光弼郁郁而终", y=820, size=30, fill="#FCD34D", weight="600"),
))

def gen_card3():
    return card_svg("03-content-liguangbi-loyalty.png", '''
  <rect x="0" y="340" width="1024" height="684" fill="url(#fade)"/>
  {t1}
  <rect x="312" y="460" width="400" height="3" rx="1.5" fill="url(#accent)"/>
  {t2}
  {t3}
  {t4}
  {t5}
  {t6}
  {t7}
'''.format(
    t1=tx("走到半路的徐州事件", y=420, size=56, weight="900", family=F),
    t2=tx("763年，朝廷召李光弼入朝", y=530, size=34),
    t3=tx("走到半路听说有人进谗言", y=590, size=34, fill="#FCA5A5"),
    t4=tx("说他密谋造反", y=640, size=34, fill="#FCA5A5"),
    t5=tx("他立刻退回徐州", y=710, size=34),
    t6=tx("再不敢踏进长安一步", y=760, size=34),
    t7=tx("来瑱被冤杀 · 仆固怀恩被逼反 · 人人自危", y=850, size=28, fill="#9CA3AF", stroke=STROKE_L),
))

def gen_card4():
    return card_svg("04-ending-liguangbi-loyalty.png", '''
  <rect x="0" y="360" width="1024" height="664" fill="url(#fade)"/>
  {t1}
  <rect x="312" y="480" width="400" height="3" rx="1.5" fill="url(#accent)"/>
  {t2}
  {t3}
  {t4}
  {t5}
  {t6}
  {t7}
'''.format(
    t1=tx("至死都在自责的人", y=440, size=60, weight="900", family=F),
    t2=tx('「吾在军中，不敢避死」', y=560, size=38, fill="#FCD34D", weight="600"),
    t3=tx('「但恐死不足塞责耳」', y=620, size=38, fill="#FCD34D", weight="600"),
    t4=tx("至死都在怕自己做得不够好", y=710, size=32),
    t5=tx("这样的人，真的会反吗？", y=760, size=32),
    t6=tx("——", y=810, size=28, fill="#9CA3AF"),
    t7=tx("你觉得呢？评论区说说 👇", y=860, size=30, fill="#FCD34D", weight="bold"),
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
        ("liguangbi-cover", gen_cover),
        ("liguangbi-card-1", gen_card2),
        ("liguangbi-card-2", gen_card3),
        ("liguangbi-card-3", gen_card4),
    ]
    print("生成李光弼卡片 v2（黑色描边+大字）...")
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
