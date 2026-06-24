import subprocess, json, sys, math, time, base64, requests, os

AGNES_KEY = os.environ.get("AGNES_KEY", "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL = "https://apihub.agnes-ai.com/v1/images/generations"
INKSCAPE = "/Applications/Inkscape.app/Contents/MacOS/inkscape"

CARD_W = 1024
CARD_H = 1024
SRC_W = 1280
SRC_H = 1280
FONT = "Source Han Serif SC"

COVER = "zcz-cover"
CARDS = ["zcz-card-1", "zcz-card-2", "zcz-card-3"]

PROMPTS = {
    "cover": (
        "Ancient Chinese astronomer-mathematician studying a celestial globe and geometric diagrams, "
        "scrolls covered in numbers and star charts, traditional studio setting, "
        "ink-wash painting style with blue and white palette, Song dynasty aesthetic, "
        "scholarly atmosphere with compass and abacus visible, ultra-detailed, 8K"
    ),
    "card1": (
        "Ancient Chinese scholar drawing circles and polygons on paper, "
        "intricate geometric patterns covering the desk, focused expression, "
        "traditional ink-wash painting style, blue jade and white palette, "
        "mathematical precision atmosphere, ultra-detailed, 8K"
    ),
    "card2": (
        "Ancient Chinese observatory at night, scholar studying star positions, "
        "bronze astronomical instruments, moon and stars visible, "
        "traditional Chinese painting style, deep blue and silver palette, "
        "scientific atmosphere, ultra-detailed, 8K"
    ),
    "card3": (
        "Ancient Chinese workshop with mechanical devices, a wooden model of a south-pointing chariot, "
        "water-powered mill mechanism, scholar examining gears, "
        "traditional ink-wash style with warm wood tones, invention workshop atmosphere, 8K"
    ),
}

def agnes(prompt_key):
    prompt = PROMPTS[prompt_key]
    fname = {"cover": COVER, "card1": CARDS[0], "card2": CARDS[1], "card3": CARDS[2]}[prompt_key]
    for attempt in range(3):
        r = requests.post(AGNES_URL, headers={"Authorization": f"Bearer {AGNES_KEY}", "Content-Type": "application/json"}, json={"model": "agnes-image-2.1-flash", "prompt": prompt, "n": 1, "size": f"{SRC_W}x{SRC_H}"}, timeout=120)
        if r.status_code == 200:
            data = r.json()
            break
        print(f"Agnes {prompt_key} attempt {attempt+1} failed: {r.status_code} {r.text[:200]}", file=sys.stderr)
        time.sleep(5)
    else:
        raise RuntimeError(f"Agnes failed for {prompt_key}")
    url = data["data"][0]["url"]
    ir = requests.get(url, timeout=120)
    with open(f"{fname}_raw.png", "wb") as f:
        f.write(ir.content)
    print(f"{fname}_raw.png generated", file=sys.stderr)
    return f"{fname}_raw.png"

SVG_TPL = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <linearGradient id="overlay" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#000" stop-opacity="0"/>
      <stop offset="30%" stop-color="#000" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0.65"/>
    </linearGradient>
    <filter id="stroke">
      <feMorphology operator="dilate" radius="3" in="SourceAlpha" result="expanded"/>
      <feFlood flood-color="#000" flood-opacity="1" result="colored"/>
      <feComposite operator="in" in="colored" in2="expanded" result="stroked"/>
      <feMerge><feMergeNode in="stroked"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <image href="{bg}" x="0" y="0" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice"/>
  <rect x="0" y="0" width="{w}" height="{h}" fill="url(#overlay)"/>
</svg>"""

def make_svg(bg_file, lines, title, out_svg, palette, is_cover=False):
    h, w = CARD_H, CARD_W
    svg = SVG_TPL.format(w=w, h=h, bg=bg_file)
    title_sz = 58 if is_cover else 48
    title_y = 140 if is_cover else 120
    svg += f'<text x="60" y="{title_y}" fill="{palette[0]}" font-family="{FONT}" font-size="{title_sz}" font-weight="700" filter="url(#stroke)">{title}</text>'
    sep_y = title_y + 40
    svg += f'<line x1="60" y1="{sep_y}" x2="{w-60}" y2="{sep_y}" stroke="{palette[0]}" stroke-opacity="0.4" stroke-width="1.5"/>'
    y = sep_y + 30
    for line in lines:
        svg += f'<text x="60" y="{y}" fill="{palette[1]}" font-family="{FONT}" font-size="32" font-weight="400" filter="url(#stroke)">{line}</text>'
        y += 46
    page = os.path.splitext(os.path.basename(out_svg))[0].split("-")[-1]
    svg += f'<text x="{w-80}" y="{h-40}" fill="{palette[1]}" font-family="{FONT}" font-size="18" font-weight="300" text-anchor="end" opacity="0.5">{page}</text>'
    with open(out_svg, "w") as f:
        f.write(svg)
    print(f"{out_svg} written", file=sys.stderr)

def make_cover_svg(bg_file, out_svg):
    svg = SVG_TPL.format(w=CARD_W, h=CARD_H, bg=bg_file)
    svg += f'<text x="512" y="280" fill="#B8D4E3" font-family="{FONT}" font-size="72" font-weight="700" text-anchor="middle" filter="url(#stroke)">祖冲之</text>'
    svg += f'<text x="512" y="350" fill="#8BB8D0" font-family="{FONT}" font-size="36" font-weight="400" text-anchor="middle" filter="url(#stroke)">领先世界千年的天才</text>'
    svg += f'<line x1="312" y1="380" x2="712" y2="380" stroke="#8BB8D0" stroke-opacity="0.5" stroke-width="1.5"/>'
    svg += f'<text x="512" y="700" fill="#6FA0BA" font-family="{FONT}" font-size="24" font-weight="300" text-anchor="middle" opacity="0.7">π=3.1415926…·大明历·指南车</text>'
    svg += f'<text x="512" y="740" fill="#6FA0BA" font-family="{FONT}" font-size="20" font-weight="300" text-anchor="middle" opacity="0.5">南朝的科学丰碑</text>'
    with open(out_svg, "w") as f:
        f.write(svg)
    print(f"{out_svg} written", file=sys.stderr)

def main():
    raw = agnes("cover")
    make_cover_svg(raw, f"{COVER}.svg")
    subprocess.run([INKSCAPE, f"{COVER}.svg", "-o", f"{COVER}.png"], capture_output=True)
    print(f"{COVER}.png done", file=sys.stderr)

    card_info = [
        ("card1", ["圆周率精确到小数点后七位",
                    "3.1415926到3.1415927之间",
                    "这个纪录保持近千年",
                    "直到十五世纪才被打破",
                    "领先世界千年的精度"]),
        ("card2", ["编制大明历引入岁差概念",
                    "算出回归年365.2428148天",
                    "与现代实测仅差46秒",
                    "与守旧派激烈论战",
                    "死后十年才得以推行"]),
        ("card3", ["复原失传的指南车",
                    "造千里船日行百里",
                    "发明水碓磨水力舂米",
                    "理论数学与工程全才",
                    "千年一遇的科学大师"]),
    ]

    palettes = [
        ["#B8D4E3", "#8BB8D0"],
        ["#A8C9D8", "#7DABC5"],
        ["#98BECD", "#6FA0BA"],
    ]

    for i, ((key, lines), pal) in enumerate(zip(card_info, palettes)):
        raw = agnes(key)
        title = ["圆周率", "大明历", "工程天才"][i]
        out = f"zcz-{key}.svg"
        make_svg(raw, lines, title, out, pal)
        subprocess.run([INKSCAPE, out, "-o", out.replace(".svg", ".png")], capture_output=True)
        print(f"{out.replace('.svg', '.png')} done", file=sys.stderr)

    print("ALL DONE", file=sys.stderr)

if __name__ == "__main__":
    main()
