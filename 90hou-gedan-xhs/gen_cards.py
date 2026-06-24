#!/usr/bin/env python3
"""90后怀旧歌单74首 — 卡片生成 v3（大字+小红书风格）"""
import subprocess
from pathlib import Path

def gen_svg_cover():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="1024" height="1024" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF7ED"/>
      <stop offset="50%" stop-color="#FFEDD5"/>
      <stop offset="100%" stop-color="#FED7AA"/>
    </linearGradient>
    <linearGradient id="circle1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F97316" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#EA580C" stop-opacity="0.06"/>
    </linearGradient>
    <linearGradient id="circle2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F59E0B" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#D97706" stop-opacity="0.04"/>
    </linearGradient>
  </defs>

  <rect width="1024" height="1024" fill="url(#bg)"/>

  <!-- 装饰大圆 -->
  <circle cx="512" cy="512" r="420" fill="url(#circle1)"/>
  <circle cx="512" cy="512" r="300" fill="url(#circle2)"/>

  <!-- 小装饰圆 -->
  <circle cx="180" cy="180" r="60" fill="#F97316" opacity="0.06"/>
  <circle cx="840" cy="840" r="80" fill="#EA580C" opacity="0.05"/>

  <!-- 大数字74（视觉焦点） -->
  <text x="512" y="440" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="200" font-weight="900" fill="#1C1917" opacity="0.08">74</text>

  <!-- 标题 -->
  <text x="512" y="370" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="96" font-weight="900" fill="#1C1917">90后怀旧歌单</text>
  <text x="512" y="470" text-anchor="middle" font-family="system-ui,sans-serif" font-size="40" font-weight="600" fill="#C2410C">74首刻进DNA的歌</text>

  <!-- 分隔线 -->
  <rect x="312" y="530" width="400" height="4" rx="2" fill="#EA580C" opacity="0.25"/>

  <!-- 底部 -->
  <text x="512" y="640" text-anchor="middle" font-family="system-ui,sans-serif" font-size="28" fill="#9A3412" opacity="0.6">致我们逝去的青春</text>

  <!-- 音符 -->
  <text x="180" y="780" font-family="system-ui,sans-serif" font-size="48" fill="#EA580C" opacity="0.12">♪</text>
  <text x="800" y="300" font-family="system-ui,sans-serif" font-size="56" fill="#F97316" opacity="0.1">♫</text>
  <text x="300" y="300" font-family="system-ui,sans-serif" font-size="40" fill="#EA580C" opacity="0.08">♪</text>
  <text x="740" y="760" font-family="system-ui,sans-serif" font-size="44" fill="#F97316" opacity="0.1">♫</text>
</svg>'''

def gen_svg_jay():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="1024" height="1024" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F8FAFC"/>
    </linearGradient>
  </defs>

  <rect width="1024" height="1024" fill="url(#bg)"/>

  <!-- 顶部蓝色色块 -->
  <rect x="0" y="0" width="1024" height="280" fill="#1E40AF"/>
  <rect x="0" y="280" width="1024" height="12" fill="#3B82F6"/>

  <text x="512" y="140" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="88" font-weight="900" fill="#FFFFFF">周杰伦专场</text>
  <text x="512" y="210" text-anchor="middle" font-family="system-ui,sans-serif" font-size="34" fill="#BFDBFE">一人独占 20+ 首 · 华语乐坛天花板</text>

  <!-- 歌曲 - 大字号两列 -->
  <g font-family="system-ui,sans-serif" font-size="40" fill="#1E293B">
    <text x="100" y="390" font-weight="600">晴天</text>
    <text x="564" y="390" font-weight="600">七里香</text>
    <text x="100" y="480" font-weight="600">夜曲</text>
    <text x="564" y="480" font-weight="600">青花瓷</text>
    <text x="100" y="570" font-weight="600">稻香</text>
    <text x="564" y="570" font-weight="600">简单爱</text>
    <text x="100" y="660" font-weight="600">告白气球</text>
    <text x="564" y="660" font-weight="600">双截棍</text>
    <text x="100" y="750" font-weight="600">东风破</text>
    <text x="564" y="750" font-weight="600">千里之外</text>
    <text x="100" y="840" font-weight="600">说好的幸福呢</text>
    <text x="564" y="840" font-weight="600">不能说的秘密</text>
  </g>

  <!-- 小字补充 -->
  <text x="512" y="940" text-anchor="middle" font-family="system-ui,sans-serif" font-size="26" fill="#94A3B8">发如雪 · 菊花台 · 听妈妈的话 · 本草纲目 · 明明就 · 安静 · 迷迭香 · 红模仿 · 珊瑚海</text>
</svg>'''

def gen_svg_legend():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="1024" height="1024" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#FAF5FF"/>
    </linearGradient>
  </defs>

  <rect width="1024" height="1024" fill="url(#bg)"/>

  <!-- 顶部紫色色块 -->
  <rect x="0" y="0" width="1024" height="280" fill="#6D28D9"/>
  <rect x="0" y="280" width="1024" height="12" fill="#8B5CF6"/>

  <text x="512" y="140" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="80" font-weight="900" fill="#FFFFFF">神仙打架的年代</text>
  <text x="512" y="210" text-anchor="middle" font-family="system-ui,sans-serif" font-size="34" fill="#DDD6FE">每一首都是经典</text>

  <!-- 歌手+歌曲 - 左对齐 -->
  <g font-family="system-ui,sans-serif" fill="#334155">
    <text x="80" y="370" font-size="34" font-weight="bold" fill="#6D28D9">林俊杰</text>
    <text x="80" y="420" font-size="34" fill="#64748B">江南 · 小酒窝 · 醉赤壁</text>

    <text x="80" y="510" font-size="34" font-weight="bold" fill="#6D28D9">陈奕迅</text>
    <text x="80" y="560" font-size="34" fill="#64748B">十年 · 富士山下</text>

    <text x="80" y="650" font-size="34" font-weight="bold" fill="#6D28D9">五月天</text>
    <text x="80" y="700" font-size="34" fill="#64748B">倔强 · 知足 · 天使</text>

    <text x="540" y="370" font-size="34" font-weight="bold" fill="#6D28D9">胡歌</text>
    <text x="540" y="420" font-size="34" fill="#64748B">逍遥叹 · 忘记时间 · 六月的雨</text>

    <text x="540" y="510" font-size="34" font-weight="bold" fill="#6D28D9">张敬轩</text>
    <text x="540" y="560" font-size="34" fill="#64748B">断点 · 吻得太逼真</text>

    <text x="540" y="650" font-size="34" font-weight="bold" fill="#6D28D9">Beyond / 伍佰</text>
    <text x="540" y="700" font-size="34" fill="#64748B">光辉岁月 / 挪威的森林·突然的自我</text>
  </g>

  <text x="512" y="900" text-anchor="middle" font-family="system-ui,sans-serif" font-size="28" fill="#94A3B8">王力宏/谭维维 · 许巍 · 赵雷 · 薛之谦 · 许嵩 · 阿桑 · 李克勤 · 水木年华 ……</text>
</svg>'''

def gen_svg_memory():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="1024" height="1024" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#FFF1F2"/>
    </linearGradient>
  </defs>

  <rect width="1024" height="1024" fill="url(#bg)"/>

  <!-- 顶部红色色块 -->
  <rect x="0" y="0" width="1024" height="280" fill="#B91C1C"/>
  <rect x="0" y="280" width="1024" height="12" fill="#EF4444"/>

  <text x="512" y="140" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="80" font-weight="900" fill="#FFFFFF">你的青春是哪首？</text>
  <text x="512" y="210" text-anchor="middle" font-family="system-ui,sans-serif" font-size="34" fill="#FECACA">74首 · 全是回忆</text>

  <!-- 歌曲列表（居中） -->
  <g font-family="system-ui,sans-serif" font-size="40" fill="#1E293B">
    <text x="512" y="390" text-anchor="middle" font-weight="600">薛之谦 — 认真的雪</text>
    <text x="512" y="480" text-anchor="middle" font-weight="600">许嵩 — 城府</text>
    <text x="512" y="570" text-anchor="middle" font-weight="600">阿桑 — 一直很安静</text>
    <text x="512" y="660" text-anchor="middle" font-weight="600">李克勤 — 红日</text>
    <text x="512" y="750" text-anchor="middle" font-weight="600">许巍 — 蓝莲花</text>
    <text x="512" y="840" text-anchor="middle" font-weight="600">赵雷 — 成都</text>
  </g>

  <!-- CTA按钮 -->
  <rect x="262" y="920" width="500" height="64" rx="32" fill="#FEE2E2"/>
  <text x="512" y="961" text-anchor="middle" font-family="system-ui,sans-serif" font-size="30" font-weight="bold" fill="#B91C1C">评论区说说你心中的 TOP1 👇</text>
</svg>'''

def gen_svg(c):
    f = c["file"]
    if f == "90hou-cover": return gen_svg_cover()
    elif f == "90hou-card-jay": return gen_svg_jay()
    elif f == "90hou-card-legend": return gen_svg_legend()
    elif f == "90hou-card-memory": return gen_svg_memory()

def to_png(svg_path, png_path):
    r = subprocess.run(
        ["inkscape", str(svg_path), "--export-type=png",
         "--export-dpi=100", "--export-filename={}".format(png_path)],
        capture_output=True, text=True
    )
    return r.returncode == 0

def main():
    d = Path(__file__).parent
    files = ["90hou-cover", "90hou-card-jay", "90hou-card-legend", "90hou-card-memory"]
    titles = ["封面", "周杰伦专场", "神仙打架", "青春记忆"]
    print("生成卡片 v3...")
    for i, f in enumerate(files):
        svg = d / "{}.svg".format(f)
        png = d / "{}.png".format(f)
        c = {"file": f}
        print("  {}/4 {}".format(i+1, titles[i]))
        svg.write_text(gen_svg(c), encoding="utf-8")
        if to_png(svg, png):
            print("    OK")
        else:
            print("    FAIL")
        svg.unlink(missing_ok=True)
    print("完成！")

if __name__ == "__main__":
    main()
