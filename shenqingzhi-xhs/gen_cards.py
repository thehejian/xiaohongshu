import subprocess, json, sys, math, time, base64, requests, os

AGNES_KEY = os.environ.get("AGNES_KEY", "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL = "https://apihub.agnes-ai.com/v1/images/generations"
INKSCAPE = "/Applications/Inkscape.app/Contents/MacOS/inkscape"

CARD_W = 1024
CARD_H = 1024
SRC_W = 1280
SRC_H = 1280
FONT = "Source Han Serif SC"

COVER = "sqz-cover"
CARDS = ["sqz-card-1", "sqz-card-2", "sqz-card-3"]

PROMPTS = {
    "cover": (
        "Ancient Chinese elderly general in full armor standing on a battlefield at dawn, "
        "holding a spear, gray beard flowing in wind, weathered face with sharp eyes, "
        "traditional ink-wash painting style, Song dynasty aesthetic, steel gray and deep blue palette, "
        "mountain fortress behind, epic cinematic composition, ultra-detailed, 8K"
    ),
    "card1": (
        "Ancient Chinese army camp at night, elderly general studying a map by torchlight, "
        "soldiers standing guard in background, traditional Chinese painting style, "
        "dark blue and amber tones, dramatic chiaroscuro, cinematic composition, 8K"
    ),
    "card2": (
        "Ancient Chinese besieged city walls with fire and smoke, elderly general directing "
        "catapult assault, burning towers, chaotic battlefield, traditional ink-wash style, "
        "crimson and dark gray palette, epic scale, ultra-detailed, 8K"
    ),
    "card3": (
        "Ancient Chinese palace courtyard at dusk, elderly general kneeling before a young emperor, "
        "imperial guards surrounding them, tragic atmosphere, traditional painting style, "
        "muted gold and gray tones, cinematic composition, 8K"
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
    svg += f'<text x="512" y="280" fill="#C8D6E5" font-family="{FONT}" font-size="72" font-weight="700" text-anchor="middle" filter="url(#stroke)">沈庆之</text>'
    svg += f'<text x="512" y="350" fill="#A0B4C8" font-family="{FONT}" font-size="36" font-weight="400" text-anchor="middle" filter="url(#stroke)">八十岁战死的军神</text>'
    svg += f'<line x1="362" y1="380" x2="662" y2="380" stroke="#A0B4C8" stroke-opacity="0.5" stroke-width="1.5"/>'
    svg += f'<text x="512" y="700" fill="#8899AA" font-family="{FONT}" font-size="24" font-weight="300" text-anchor="middle" opacity="0.7">从庄稼汉到三公之位</text>'
    svg += f'<text x="512" y="740" fill="#8899AA" font-family="{FONT}" font-size="20" font-weight="300" text-anchor="middle" opacity="0.5">刘宋五朝元老·一代军神</text>'
    with open(out_svg, "w") as f:
        f.write(svg)
    print(f"{out_svg} written", file=sys.stderr)

def main():
    raw = agnes("cover")
    make_cover_svg(raw, f"{COVER}.svg")
    subprocess.run([INKSCAPE, f"{COVER}.svg", "-o", f"{COVER}.png"], capture_output=True)
    print(f"{COVER}.png done", file=sys.stderr)

    card_info = [
        ("card1", ["出身寒门，种地出身",
                    "三十岁投军，白手起家",
                    "发明连营围剿法",
                    "专打各种叛军蛮族",
                    "从无名小卒杀成大将"]),
        ("card2", ["七十高龄仍亲自督战",
                    "火攻破广陵城",
                    "以少胜多，以弱胜强",
                    "历经五朝屹立不倒",
                    "深知功高震主从不争功"]),
        ("card3", ["前废帝猜忌四朝元老",
                    "称病不出仍被赐死",
                    "八十岁被逼饮鸩而亡",
                    "预见了自己的结局",
                    "刘宋一代军神落幕"]),
    ]

    palettes = [
        ["#C8D6E5", "#A0B4C8"],
        ["#B8C9D8", "#95A9BD"],
        ["#A8BACB", "#8A9EB2"],
    ]

    for i, ((key, lines), pal) in enumerate(zip(card_info, palettes)):
        raw = agnes(key)
        title = ["白手起家", "百战百胜", "英雄末路"][i]
        out = f"sqz-{key}.svg"
        make_svg(raw, lines, title, out, pal)
        subprocess.run([INKSCAPE, out, "-o", out.replace(".svg", ".png")], capture_output=True)
        print(f"{out.replace('.svg', '.png')} done", file=sys.stderr)

    print("ALL DONE", file=sys.stderr)

if __name__ == "__main__":
    main()
