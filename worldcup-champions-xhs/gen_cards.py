import subprocess, os

OUT = "output"
os.makedirs(OUT, exist_ok=True)

CREAM = "#FAF7F2"
DEEP = "#1E293B"
GOLD = "#B8860B"
BLUE = "#2563EB"
GREEN = "#059669"
RED = "#DC2626"
GRAY = "#94A3B8"
WHITE = "#FFFFFF"

def save_svg(name, svg):
    svg_path = os.path.join(OUT, f"{name}.svg")
    png_path = os.path.join(OUT, f"{name}.png")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    subprocess.run(
        ["inkscape", svg_path, "--export-type=png", f"--export-filename={png_path}",
         "-w", "1024", "-h", "1024"],
        check=True, capture_output=True,
    )

def cover_card():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024">
  <rect width="1024" height="1024" fill="{CREAM}"/>
  <text x="512" y="200" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="24" fill="{GRAY}">FIFA World Cup</text>
  <text x="512" y="260" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="48" fill="{DEEP}" font-weight="bold">世界杯冠军排名</text>
  <text x="512" y="310" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{GRAY}">22届比赛 · 8个冠军国家</text>
  <line x1="300" y1="340" x2="724" y2="340" stroke="{GOLD}" stroke-width="3"/>
  <text x="512" y="420" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="160" fill="{GOLD}" font-weight="bold">22</text>
  <text x="512" y="490" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="22" fill="{GRAY}">届世界杯 · 1930-2022</text>
  <text x="512" y="580" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="22" fill="{DEEP}">下拉查看完整排名</text>
  <rect x="362" y="620" width="300" height="50" rx="25" fill="{BLUE}"/>
  <text x="512" y="653" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{WHITE}" font-weight="bold">滑动查看</text>
</svg>'''

def ranking_card():
    countries = [
        ("巴西", 5, GREEN),
        ("德国", 4, DEEP),
        ("意大利", 4, GREEN),
        ("阿根廷", 3, BLUE),
        ("法国", 2, RED),
        ("乌拉圭", 2, GOLD),
        ("英格兰", 1, RED),
        ("西班牙", 1, GOLD),
    ]
    bars = ""
    y = 190
    for name, cnt, color in countries:
        w = 60 + cnt * 100
        bars += f'''<text x="160" y="{y+10}" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{DEEP}">{name}</text>
<rect x="280" y="{y-15}" width="{w}" height="30" rx="6" fill="{color}" opacity="0.85"/>
<text x="{290+w}" y="{y+8}" font-family="PingFang SC, Heiti SC, sans-serif" font-size="22" fill="{DEEP}" font-weight="bold">{cnt}</text>
'''
        y += 55
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024">
  <rect width="1024" height="1024" fill="{CREAM}"/>
  <text x="512" y="80" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="32" fill="{DEEP}" font-weight="bold">冠军次数排行榜</text>
  <line x1="250" y1="100" x2="774" y2="100" stroke="{GOLD}" stroke-width="2"/>
  {bars}
  <text x="512" y="820" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="16" fill="{GRAY}">截至2026年，共22届世界杯</text>
</svg>'''

def brazil_card():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024">
  <rect width="1024" height="1024" fill="{CREAM}"/>
  <text x="512" y="100" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="40" fill="{DEEP}" font-weight="bold">巴西</text>
  <text x="512" y="150" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="100" fill="{GREEN}" font-weight="bold">5</text>
  <text x="512" y="200" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{GRAY}">次冠军 · 历史第一</text>
  <text x="512" y="280" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="22" fill="{DEEP}" font-weight="bold">1958 1962 1970 1994 2002</text>
  <text x="512" y="350" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{DEEP}">球王贝利 · 3次夺冠（历史唯一）</text>
  <text x="512" y="390" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{DEEP}">唯一参加过全部22届世界杯的国家</text>
  <line x1="200" y1="450" x2="824" y2="450" stroke="#E2E8F0" stroke-width="1"/>
  <text x="512" y="510" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{GRAY}">2002年决赛 2:0 德国</text>
  <text x="512" y="550" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{GRAY}">2014年半决赛 1:7 德国（史上最惨）</text>
  <text x="512" y="590" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{GRAY}">2026年等待第6冠</text>
</svg>'''

def gerita_card():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024">
  <rect width="1024" height="1024" fill="{CREAM}"/>
  <text x="512" y="90" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="32" fill="{DEEP}" font-weight="bold">并列第二：德国 &amp; 意大利</text>
  <line x1="200" y1="110" x2="824" y2="110" stroke="{GOLD}" stroke-width="2"/>
  <text x="280" y="200" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="80" fill="{DEEP}" font-weight="bold">4</text>
  <text x="280" y="230" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{GRAY}">德国</text>
  <text x="744" y="200" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="80" fill="{GREEN}" font-weight="bold">4</text>
  <text x="744" y="230" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{GRAY}">意大利</text>
  <text x="280" y="300" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{DEEP}">1954 1974 1990 2014</text>
  <text x="744" y="300" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{DEEP}">1934 1938 1982 2006</text>
  <text x="512" y="370" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="16" fill="{GRAY}">---</text>
  <text x="512" y="430" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{DEEP}">德国：2014年7:1巴西</text>
  <text x="512" y="540" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{DEEP}">意大利：4次冠军但2018/2022缺席</text>
</svg>'''

def rest_card():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024">
  <rect width="1024" height="1024" fill="{CREAM}"/>
  <text x="512" y="80" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="32" fill="{DEEP}" font-weight="bold">其他冠军国家</text>
  <line x1="250" y1="100" x2="774" y2="100" stroke="{GOLD}" stroke-width="2"/>
  <text x="512" y="190" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="60" fill="{BLUE}" font-weight="bold">3</text>
  <text x="512" y="230" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="22" fill="{DEEP}">阿根廷</text>
  <text x="512" y="270" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{GRAY}">1978 1986马拉多纳 2022梅西</text>
  <line x1="200" y1="310" x2="824" y2="310" stroke="#E2E8F0" stroke-width="1"/>
  <text x="280" y="390" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="60" fill="{RED}" font-weight="bold">2</text>
  <text x="280" y="430" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{DEEP}">法国</text>
  <text x="280" y="460" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="16" fill="{GRAY}">1998齐达内 2018姆巴佩</text>
  <text x="744" y="390" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="60" fill="{GOLD}" font-weight="bold">2</text>
  <text x="744" y="430" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{DEEP}">乌拉圭</text>
  <text x="744" y="460" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="16" fill="{GRAY}">1930首届 1950</text>
  <line x1="200" y1="510" x2="824" y2="510" stroke="#E2E8F0" stroke-width="1"/>
  <text x="280" y="590" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="60" fill="{RED}" font-weight="bold">1</text>
  <text x="280" y="630" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{DEEP}">英格兰</text>
  <text x="280" y="660" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="16" fill="{GRAY}">1966 唯一一次</text>
  <text x="744" y="590" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="60" fill="{GOLD}" font-weight="bold">1</text>
  <text x="744" y="630" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{DEEP}">西班牙</text>
  <text x="744" y="660" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="16" fill="{GRAY}">2010传控王朝</text>
</svg>'''

def funfacts_card():
    items = ""
    facts = [
        ("最多冠军", "巴西  5次"),
        ("最多决赛", "德国  8次进决赛"),
        ("最多亚军", "荷兰  3次亚军0冠军"),
        ("还没进过", "中国  仅2002年进过一次"),
        ("扩军48队", "2026年更多国家圆梦"),
    ]
    y = 170
    for label, value in facts:
        items += f'''<rect x="120" y="{y}" width="784" height="60" rx="10" fill="{DEEP}" opacity="0.04"/>
<text x="160" y="{y+38}" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{DEEP}" font-weight="bold">{label}</text>
<text x="864" y="{y+38}" text-anchor="end" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{GRAY}">{value}</text>
'''
        y += 80
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024">
  <rect width="1024" height="1024" fill="{CREAM}"/>
  <text x="512" y="80" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="32" fill="{DEEP}" font-weight="bold">世界杯冷知识</text>
  <line x1="300" y1="100" x2="724" y2="100" stroke="{GOLD}" stroke-width="2"/>
  {items}
  <text x="512" y="740" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="22" fill="{BLUE}" font-weight="bold">2026年 第23届世界杯</text>
  <text x="512" y="780" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{GRAY}">48支队 美加墨联合主办</text>
</svg>'''

if __name__ == "__main__":
    print("Generating SVG cards...")
    for name, fn in [
        ("01-cover", cover_card),
        ("02-ranking", ranking_card),
        ("03-brazil", brazil_card),
        ("04-gerita", gerita_card),
        ("05-rest", rest_card),
        ("06-funfacts", funfacts_card),
    ]:
        svg = fn()
        save_svg(name, svg)
        print(f"  {name}.svg + {name}.png")
    print("Done! 6 cards in output/")
