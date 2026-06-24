import subprocess, json, sys, math, time, base64, requests, os

# ---------- config ----------
AGNES_KEY = os.environ.get("AGNES_KEY", "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL = "https://apihub.agnes-ai.com/v1/images/generations"
INKSCAPE = "/Applications/Inkscape.app/Contents/MacOS/inkscape"

CARD_W = 1024
CARD_H = 1024
SRC_W = 1280
SRC_H = 1280
FONT = "Source Han Serif SC"

COVER = "yxr-cover"
CARDS = ["yxr-card-1", "yxr-card-2", "yxr-card-3"]

# ---------- Agnes prompt ----------
PROMPTS = {
    "cover": (
        "Ancient Chinese empress in elaborate phoenix crown and vermillion court robes, "
        "standing in a misty palace corridor, dramatic lighting, half in shadow, "
        "traditional ink-wash painting style, Song dynasty aesthetic, muted red and gold palette, "
        "empty throne visible behind her, atmospheric haze, ultra-detailed, 8K"
    ),
    "card1": (
        "Ancient Chinese palace scene, imperial edict being torn, a woman in queen robes kneeling, "
        "fallen crown beside her, court officials bowing in fear, traditional Chinese painting style, "
        "somber mood, muted crimson and gray tones, cinematic composition, 8K"
    ),
    "card2": (
        "Ancient Chinese battlefield at dusk, a woman in damaged imperial robes standing beside "
        "a Xiongnu chieftain on horseback, burning palace in background, epic scale, "
        "traditional ink-wash meets classical realism, dramatic orange and purple sky, 8K"
    ),
    "card3": (
        "Ancient Chinese palace interior, elderly empress sitting on throne with dignity, "
        "three young princes beside her, ornate architecture, warm candlelight, "
        "traditional Chinese court painting style, gold and crimson palette, peaceful yet melancholic, 8K"
    ),
}

# ---------- Agnes ----------
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

# ---------- SVG ----------
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

def text_extent(y, sz):
    """Return list of (line_y, remaining_lines) for a given y start position."""
    return y

def make_svg(bg_file, lines, title, out_svg, palette, is_cover=False):
    h, w = CARD_H, CARD_W
    svg = SVG_TPL.format(w=w, h=h, bg=bg_file)

    # Title line
    title_sz = 58 if is_cover else 48
    title_y = 140 if is_cover else 120
    svg += f'<text x="60" y="{title_y}" fill="{palette[0]}" font-family="{FONT}" font-size="{title_sz}" font-weight="700" filter="url(#stroke)">{title}</text>'

    # Separator
    sep_y = title_y + 40
    svg += f'<line x1="60" y1="{sep_y}" x2="{w-60}" y2="{sep_y}" stroke="{palette[0]}" stroke-opacity="0.4" stroke-width="1.5"/>'

    # Body lines
    y = sep_y + 30
    for line in lines:
        svg += f'<text x="60" y="{y}" fill="{palette[1]}" font-family="{FONT}" font-size="32" font-weight="400" filter="url(#stroke)">{line}</text>'
        y += 46

    # Page marker
    page = os.path.splitext(os.path.basename(out_svg))[0].split("-")[-1]
    svg += f'<text x="{w-80}" y="{h-40}" fill="{palette[1]}" font-family="{FONT}" font-size="18" font-weight="300" text-anchor="end" opacity="0.5">{page}</text>'

    with open(out_svg, "w") as f:
        f.write(svg)
    print(f"{out_svg} written", file=sys.stderr)

def make_cover_svg(bg_file, out_svg):
    svg = SVG_TPL.format(w=CARD_W, h=CARD_H, bg=bg_file)
    svg += f'<text x="512" y="280" fill="#E8D5B7" font-family="{FONT}" font-size="72" font-weight="700" text-anchor="middle" filter="url(#stroke)">羊献容</text>'
    svg += f'<text x="512" y="350" fill="#D4AF87" font-family="{FONT}" font-size="36" font-weight="400" text-anchor="middle" filter="url(#stroke)">五废六立·传奇皇后</text>'
    svg += f'<line x1="312" y1="380" x2="712" y2="380" stroke="#D4AF87" stroke-opacity="0.5" stroke-width="1.5"/>'
    svg += f'<text x="512" y="700" fill="#C9A97A" font-family="{FONT}" font-size="24" font-weight="300" text-anchor="middle" opacity="0.7">晋末乱世 · 从晋后到赵后</text>'
    svg += f'<text x="512" y="740" fill="#C9A97A" font-family="{FONT}" font-size="20" font-weight="300" text-anchor="middle" opacity="0.5">从被废五次到异国为后</text>'
    with open(out_svg, "w") as f:
        f.write(svg)
    print(f"{out_svg} written", file=sys.stderr)

# ---------- Main ----------
def main():
    raw = agnes("cover")
    make_cover_svg(raw, f"{COVER}.svg")
    subprocess.run([INKSCAPE, f"{COVER}.svg", "-o", f"{COVER}.png"], capture_output=True)
    print(f"{COVER}.png done", file=sys.stderr)

    card_info = [
        ("card1", ["她曾是西晋皇后",
                    "被成都王司马颖废为庶人",
                    "八王之乱中沦为政治棋子",
                    "五次被废，五次复位",
                    "每一次都是权臣博弈的结果"]),
        ("card2", ["洛阳城破，被匈奴刘曜俘虏",
                    "从晋朝皇后变成敌国妻妾",
                    "刘曜问她:我和司马家比如何",
                    "她答:他连你一根头发都比不上",
                    "在敌国却找到了真正的尊严"]),
        ("card3", ["晚年贵为前赵皇后",
                    "为刘曜生下三子",
                    "参与政事，深受宠爱",
                    "谥号献文，终得善终",
                    "五废六立，千年传奇"]),
    ]

    palettes = [
        ["#E8D5B7", "#D4AF87"],
        ["#E8D5B7", "#C9A97A"],
        ["#E8D5B7", "#BFA075"],
    ]

    for i, ((key, lines), pal) in enumerate(zip(card_info, palettes)):
        raw = agnes(key)
        title = ["身不由己", "异国为后", "传奇落幕"][i]
        out = f"yxr-{key}.svg"
        make_svg(raw, lines, title, out, pal)
        subprocess.run([INKSCAPE, out, "-o", out.replace(".svg", ".png")], capture_output=True)
        print(f"{out.replace('.svg', '.png')} done", file=sys.stderr)

    print("ALL DONE", file=sys.stderr)

if __name__ == "__main__":
    main()
