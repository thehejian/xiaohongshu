import subprocess, os

OUT = "output"
os.makedirs(OUT, exist_ok=True)

CREAM = "#FAF7F2"
CREAM2 = "#F5F0E8"
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
  <circle cx="512" cy="380" r="220" fill="none" stroke="{BLUE}" stroke-width="6" opacity="0.15"/>
  <circle cx="512" cy="380" r="180" fill="none" stroke="{BLUE}" stroke-width="3" opacity="0.1"/>
  <text x="512" y="320" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="160" fill="{DEEP}" font-weight="bold">48</text>
  <text x="512" y="440" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="28" fill="{GRAY}">支球队 · 前所未有的世界杯</text>
  <line x1="300" y1="480" x2="724" y2="480" stroke="{GOLD}" stroke-width="3"/>
  <text x="512" y="530" font-family="PingFang SC, Heiti SC, sans-serif" font-size="36" fill="{DEEP}" font-weight="bold" text-anchor="middle">1分钟看懂全新赛制</text>
  <text x="512" y="580" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{GRAY}" text-anchor="middle">2026 美加墨世界杯</text>
  <rect x="362" y="640" width="300" height="50" rx="25" fill="{BLUE}"/>
  <text x="512" y="673" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{WHITE}" font-weight="bold">滑动查看全部内容</text>
</svg>'''

def groups_card():
    groups_svg = ""
    colors = [BLUE, GREEN, RED, GOLD]
    positions = []
    for row in range(4):
        for col in range(3):
            x = 120 + col * 300
            y = 200 + row * 150
            c = colors[row % 4]
            groups_svg += f'''<rect x="{x}" y="{y}" width="80" height="80" rx="8" fill="{c}" opacity="0.15"/>
<text x="{x+40}" y="{y+48}" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{c}" font-weight="bold">组{chr(65+row*3+col)}</text>
'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024">
  <rect width="1024" height="1024" fill="{CREAM}"/>
  <text x="512" y="100" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="32" fill="{DEEP}" font-weight="bold">小组赛：12组 × 4队</text>
  <line x1="200" y1="120" x2="824" y2="120" stroke="{GOLD}" stroke-width="2"/>
  {groups_svg}
  <rect x="150" y="780" width="724" height="56" rx="10" fill="{BLUE}" opacity="0.08"/>
  <text x="512" y="816" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="22" fill="{BLUE}" font-weight="bold">每组前2名 → 直接晋级（24队）</text>
</svg>'''

def qualify_card():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024">
  <rect width="1024" height="1024" fill="{CREAM}"/>
  <text x="512" y="90" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="32" fill="{DEEP}" font-weight="bold">晋级规则</text>
  <line x1="300" y1="110" x2="724" y2="110" stroke="{GOLD}" stroke-width="2"/>

  <text x="512" y="200" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="26" fill="{GREEN}" font-weight="bold">12个小组前两名</text>
  <text x="512" y="235" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="60" fill="{GREEN}" font-weight="bold">24 队</text>
  <line x1="462" y1="270" x2="562" y2="310" stroke="{DEEP}" stroke-width="3"/>

  <text x="512" y="360" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="26" fill="{BLUE}" font-weight="bold">+ 8个成绩最好的小组第三</text>
  <text x="512" y="395" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="60" fill="{BLUE}" font-weight="bold">8 队</text>
  <line x1="462" y1="430" x2="562" y2="470" stroke="{DEEP}" stroke-width="3"/>

  <rect x="312" y="480" width="400" height="80" rx="15" fill="{GOLD}"/>
  <text x="512" y="525" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="36" fill="{WHITE}" font-weight="bold">32 强淘汰赛</text>

  <text x="512" y="680" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{GRAY}">小组第三之间比积分、净胜球、进球数</text>
  <text x="512" y="715" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{GRAY}">取前8名进入淘汰赛</text>
</svg>'''

def bracket_card():
    lines = ""
    for i in range(4):
        y = 140 + i * 200
        lines += f'''<rect x="80" y="{y}" width="200" height="36" rx="6" fill="{DEEP}" opacity="0.05"/>
<rect x="80" y="{y+50}" width="200" height="36" rx="6" fill="{DEEP}" opacity="0.05"/>
<line x1="280" y1="{y+18}" x2="340" y2="{y+68}" stroke="{GRAY}" stroke-width="2"/>
<line x1="280" y1="{y+68}" x2="340" y2="{y+18}" stroke="{GRAY}" stroke-width="2"/>
<line x1="340" y1="{y+43}" x2="400" y2="{y+43}" stroke="{GRAY}" stroke-width="2"/>
'''
    for i in range(2):
        y = 240 + i * 400
        lines += f'''<line x1="400" y1="{y-57}" x2="460" y2="{y-7}" stroke="{GRAY}" stroke-width="2"/>
<line x1="400" y1="{y+143}" x2="460" y2="{y-7}" stroke="{GRAY}" stroke-width="2"/>
<line x1="460" y1="{y-7}" x2="520" y2="{y-7}" stroke="{GRAY}" stroke-width="2"/>
'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024">
  <rect width="1024" height="1024" fill="{CREAM}"/>
  <text x="512" y="80" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="32" fill="{DEEP}" font-weight="bold">32强淘汰赛对阵</text>
  <line x1="300" y1="100" x2="724" y2="100" stroke="{GOLD}" stroke-width="2"/>
  {lines}
  <text x="670" y="500" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{DEEP}" font-weight="bold">决赛</text>
  <text x="670" y="530" font-family="PingFang SC, Heiti SC, sans-serif" font-size="14" fill="{GRAY}">一场定生死</text>
  <circle cx="650" cy="560" r="40" fill="{GOLD}" opacity="0.2"/>
  <text x="650" y="570" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="28" fill="{GOLD}" font-weight="bold">🏆</text>
</svg>'''

def proscons_card():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024">
  <rect width="1024" height="1024" fill="{CREAM}"/>
  <text x="512" y="80" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="32" fill="{DEEP}" font-weight="bold">扩军48队：好与坏</text>
  <line x1="300" y1="100" x2="724" y2="100" stroke="{GOLD}" stroke-width="2"/>

  <rect x="80" y="160" width="400" height="50" rx="10" fill="{GREEN}" opacity="0.15"/>
  <text x="280" y="193" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="22" fill="{GREEN}" font-weight="bold">✅ 好处</text>
  <rect x="544" y="160" width="400" height="50" rx="10" fill="{RED}" opacity="0.15"/>
  <text x="744" y="193" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="22" fill="{RED}" font-weight="bold">❌ 坏处</text>

  <text x="280" y="260" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{DEEP}">更多国家参与</text>
  <text x="280" y="295" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{DEEP}">小国圆梦世界杯</text>
  <text x="280" y="330" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{DEEP}">佛得角、库拉索的故事</text>
  <text x="280" y="365" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{DEEP}">亚洲8.5名额，国足机会大</text>

  <text x="744" y="260" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{DEEP}">强弱悬殊极大</text>
  <text x="744" y="295" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{DEEP}">7:1惨案变多</text>
  <text x="744" y="330" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{DEEP}">小组第三能出线</text>
  <text x="744" y="365" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{DEEP}">强队小组赛可能摸鱼</text>

  <line x1="512" y1="420" x2="512" y2="780" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="5,5"/>

  <text x="512" y="500" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{DEEP}">比赛变多了</text>
  <text x="512" y="540" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{DEEP}">冷门变少了</text>
  <text x="512" y="580" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{DEEP}">世界杯更热闹了</text>
</svg>'''

def summary_card():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024">
  <rect width="1024" height="1024" fill="{CREAM}"/>
  <text x="512" y="100" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="32" fill="{DEEP}" font-weight="bold">关键数字</text>
  <line x1="350" y1="120" x2="674" y2="120" stroke="{GOLD}" stroke-width="2"/>

  <text x="256" y="250" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="60" fill="{BLUE}" font-weight="bold">48</text>
  <text x="256" y="290" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{GRAY}">参赛球队</text>

  <text x="512" y="250" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="60" fill="{GREEN}" font-weight="bold">12</text>
  <text x="512" y="290" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{GRAY}">小组数量</text>

  <text x="768" y="250" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="60" fill="{GOLD}" font-weight="bold">104</text>
  <text x="768" y="290" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{GRAY}">总比赛场次</text>

  <line x1="100" y1="330" x2="924" y2="330" stroke="#E2E8F0" stroke-width="1"/>

  <text x="256" y="430" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="60" fill="{RED}" font-weight="bold">32</text>
  <text x="256" y="470" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{GRAY}">淘汰赛队伍</text>

  <text x="512" y="430" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="60" fill="{DEEP}" font-weight="bold">8.5</text>
  <text x="512" y="470" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{GRAY}">亚洲名额</text>

  <text x="768" y="430" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="60" fill="{RED}" font-weight="bold">+40</text>
  <text x="768" y="470" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{GRAY}">比2022年多</text>

  <rect x="150" y="580" width="724" height="80" rx="15" fill="{DEEP}" opacity="0.05"/>
  <text x="512" y="618" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="22" fill="{DEEP}" font-weight="bold">中国球迷：8.5个名额都救不了国足</text>
  <text x="512" y="650" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="16" fill="{GRAY}">印尼都进了，国足还没进</text>
</svg>'''

if __name__ == "__main__":
    print("Generating SVG cards...")
    for name, fn in [
        ("01-cover", cover_card),
        ("02-groups", groups_card),
        ("03-qualify", qualify_card),
        ("04-bracket", bracket_card),
        ("05-proscons", proscons_card),
        ("06-summary", summary_card),
    ]:
        svg = fn()
        save_svg(name, svg)
        print(f"  {name}.svg + {name}.png")
    print("Done! 6 cards in output/")