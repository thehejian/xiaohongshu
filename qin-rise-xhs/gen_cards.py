#!/usr/bin/env python3
"""秦人六世一统天下 — 卡片生成（黑色描边+大字）"""
import base64, subprocess
from pathlib import Path

IMG_DIR = Path(__file__).parent / "image-cards" / "qin-unification"
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
      <stop offset="0%" stop-color="#F59E0B" stop-opacity="0"/>
      <stop offset="50%" stop-color="#F59E0B" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#F59E0B" stop-opacity="0"/>
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
    t1=tx("秦人六世一统天下", y=470, size=84, weight="900", family=F),
    t2=tx("一个马夫部落的逆袭之路", y=550, size=36, fill="#FCD34D", weight="600"),
    t3=tx("非子养马→嬴政称帝 · 六百年奋斗史", y=660, size=28, fill="#E5E7EB"),
    t4=tx("# 秦朝  # 统一六国  # 历史冷知识", y=760, size=24, fill="#D1D5DB", stroke=STROKE_L),
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
    t1=tx("① 从养马到建国", y=440, size=56, weight="900", family=F),
    t2=tx("始祖非子给周孝王养马", y=560, size=36),
    t3=tx("养得好，封在秦地（今甘肃天水）", y=620, size=34),
    t4=tx("西周灭亡时勤王有功", y=690, size=36),
    t5=tx("周平王正式封秦为诸侯", y=760, size=34, fill="#FCD34D", weight="600"),
    t6=tx("秦国诞生——从马夫到国君", y=840, size=28, fill="#9CA3AF", stroke=STROKE_L),
))

def gen_card3():
    return card_svg("03-card20_0.png", '''
  <rect x="0" y="370" width="1024" height="654" fill="url(#fade)"/>
  {t1}
  <rect x="312" y="490" width="400" height="3" rx="1.5" fill="url(#accent)"/>
  {t2}
  {t3}
  {t4}
  {t5}
  {t6}
'''.format(
    t1=tx("② 九迁定鼎", y=440, size=56, weight="900", family=F),
    t2=tx("西陲→秦邑→汧渭之会→平阳", y=560, size=34),
    t3=tx("雍城→泾阳→栎阳→咸阳", y=620, size=34),
    t4=tx("每一迁都向东推进", y=700, size=38, fill="#FCD34D", weight="600"),
    t5=tx("从西陲边陲到关中核心", y=760, size=34),
    t6=tx("战略眼光拉满", y=830, size=28, fill="#9CA3AF", stroke=STROKE_L),
))

def gen_card4():
    return card_svg("04-card30_0.png", '''
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
    t1=tx("③ 变法图强：商鞅来了", y=420, size=52, weight="900", family=F),
    t2=tx("秦孝公任用商鞅变法", y=540, size=36),
    t3=tx("废井田 · 开阡陌 · 军功爵", y=600, size=34, fill="#FCD34D", weight="600"),
    t4=tx('从"蛮夷"变成"战争机器"', y=680, size=36),
    t5=tx("六国开始真正害怕秦国", y=750, size=34),
    t6=tx("商君虽死，秦法犹存", y=820, size=28, fill="#9CA3AF", stroke=STROKE_L),
    t7=tx("——法治传统奠定秦的强大", y=860, size=24, fill="#D1D5DB", stroke=STROKE_L),
))

def gen_card5():
    return card_svg("05-card40_0.png", '''
  <rect x="0" y="350" width="1024" height="674" fill="url(#fade)"/>
  {t1}
  <rect x="312" y="470" width="400" height="3" rx="1.5" fill="url(#accent)"/>
  {t2}
  {t3}
  {t4}
  {t5}
  {t6}
'''.format(
    t1=tx("④ 奋六世之余烈", y=440, size=56, weight="900", family=F),
    t2=tx("孝公→惠文王→武王→昭襄王", y=560, size=34),
    t3=tx("孝文王→庄襄王→嬴政", y=620, size=34),
    t4=tx("连续六代明君强主", y=700, size=38, fill="#FCD34D", weight="600"),
    t5=tx("中国历史上唯一的六世连珠", y=760, size=34),
    t6=tx("没有一位昏君，这概率比中彩票还低", y=840, size=26, fill="#9CA3AF", stroke=STROKE_L),
))

def gen_card6():
    return card_svg("06-card50_0.png", '''
  <rect x="0" y="350" width="1024" height="674" fill="url(#fade)"/>
  <rect x="312" y="480" width="400" height="3" rx="1.5" fill="url(#accent)"/>
  {t1}
  {t2}
  {t3}
  {t4}
  {t5}
  {t6}
  {t7}
'''.format(
    t1=tx("⑤ 十年灭六国 🏆", y=450, size=60, weight="900", family=F),
    t2=tx("230-221 BC 横扫六合", y=550, size=38, fill="#FCD34D", weight="600"),
    t3=tx("韩→赵→魏→楚→燕→齐", y=610, size=36),
    t4=tx("书同文 · 车同轨 · 行同伦", y=690, size=34),
    t5=tx("中国历史上第一个大一统王朝", y=760, size=36),
    t6=tx("——", y=820, size=28, fill="#9CA3AF"),
    t7=tx("你觉得秦能统一，最关键的一步是什么？👇", y=870, size=30, fill="#FCD34D", weight="bold"),
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
        ("qin-cover", gen_cover),
        ("qin-card-1", gen_card2),
        ("qin-card-2", gen_card3),
        ("qin-card-3", gen_card4),
        ("qin-card-4", gen_card5),
        ("qin-card-5", gen_card6),
    ]
    print("生成秦人六世一统天下卡片...")
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
