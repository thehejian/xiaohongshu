#!/usr/bin/env python3
"""Generate 4 cards for 法显."""
import subprocess, os, requests, time, base64
ROOT = os.path.dirname(os.path.abspath(__file__))

API_KEY = "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect"
API_URL = "https://apihub.agnes-ai.com/v1/images/generations"

STROKE = 'paint-order="stroke fill" stroke="#000" stroke-width="5" stroke-linejoin="round"'
STROKE_S = 'paint-order="stroke fill" stroke="#000" stroke-width="3" stroke-linejoin="round"'
FONT = 'Noto Sans SC,PingFang SC,Microsoft YaHei,sans-serif'

def agnes_image(prompt, size="1024x1024", retries=3):
    for attempt in range(retries):
        try:
            r = requests.post(API_URL, headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }, json={"model": "agnes-image-2.1-flash", "prompt": prompt, "size": size, "n": 1}, timeout=120)
            r.raise_for_status()
            url = r.json()["data"][0]["url"]
            img = requests.get(url, timeout=60)
            return img.content
        except Exception as e:
            print(f"  Agnes attempt {attempt+1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(5)
    raise RuntimeError(f"Failed after {retries} attempts")

PROMPTS = [
    "Ancient Chinese Buddhist monk in simple robes walking alone across a vast desert landscape, the Gobi Desert, elderly monk on a pilgrimage, traditional Chinese ink wash painting, Tang dynasty aesthetic, warm ochre and sandy tones, epic journey",
    "Ancient Chinese Buddhist monk crossing high snowy mountains with a staff, the Pamir Mountains, perilous mountain pass, traditional Chinese ink wash painting, Tang dynasty aesthetic, white and gray tones, dramatic landscape",
    "Ancient Indian Buddhist monastery, an elderly Chinese monk studying Sanskrit scrolls under a Bodhi tree, learning and copying scriptures, traditional Chinese ink wash painting, Tang dynasty aesthetic, warm green and gold tones, serene",
    "Ancient Chinese monk on a sailing ship crossing stormy seas, returning from Sri Lanka to China by sea, dramatic waves, traditional Chinese ink wash painting, Tang dynasty aesthetic, deep blue and white tones, adventurous",
]

FILES = ["faxian-cover", "faxian-card-1", "faxian-card-2", "faxian-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="30%" stop-color="#000" stop-opacity="0.15"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.65"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#D97706" letter-spacing="6" {STROKE}>东晋·西行高僧</text>
<text x="512" y="360" text-anchor="middle" font-family="{FONT}" font-size="140" font-weight="900" fill="#FFFFFF" letter-spacing="10" {STROKE}>法显</text>
<rect x="262" y="405" width="500" height="3" rx="1.5" fill="#D97706" opacity="0.6"/>
<text x="512" y="510" text-anchor="middle" font-family="{FONT}" font-size="48" font-weight="800" fill="#D97706" letter-spacing="6" {STROKE}>六十西行佛国记</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="24" fill="#E2E8F0" {STROKE_S}>比玄奘早两百年 · 戈壁高山 · 海路归来</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#法显 #佛国记 #西行取经 #东晋 #佛教 #丝绸之路</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#D97706" letter-spacing="3" {STROKE}>花甲西行</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#D97706"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#D97706" {STROKE}>399年出发</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>六十二岁，从长安孤身西行</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#D97706"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#D97706" {STROKE}>穿越戈壁</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>"热风恶鬼，遇者皆死"——九死一生</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#D97706"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#D97706" {STROKE}>翻越葱岭</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>过帕米尔高原，同行十人死散殆尽</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#D97706" {STROKE}>六十岁出发，十四年不归路</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#法显 #西行 #戈壁 #丝绸之路 #僧人</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#D97706" letter-spacing="3" {STROKE}>天竺取经</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#D97706"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#D97706" {STROKE}>印度十年</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>学梵文、抄原典，在菩提树下哭泣</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#D97706"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#D97706" {STROKE}>佛国记</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>记录西域和印度各国风土——珍贵史料</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#D97706"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#D97706" {STROKE}>早于玄奘两百余年</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>中国最早的西行取经记录</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#D97706" {STROKE}>比玄奘早，比玄奘苦，比玄奘传奇</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#法显 #佛国记 #天竺 #玄奘 #佛教</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#D97706" letter-spacing="3" {STROKE}>海路归来</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#D97706"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#D97706" {STROKE}>不走回头路</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>从斯里兰卡坐商船，走海路回国</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#D97706"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#D97706" {STROKE}>风暴漂流</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>遇风暴漂流九十天，在崂山（青岛）登陆</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#D97706"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#D97706" {STROKE}>一生译经</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>带回梵本，直到圆寂</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#D97706" {STROKE}>一个老人，带回了文明的火种</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#法显 #佛国记 #海上丝绸之路 #青岛 #佛教</text>
''')

if __name__ == "__main__":
    os.makedirs(ROOT, exist_ok=True)
    makers = [make_cover, make_card_1, make_card_2, make_card_3]
    for i, prompt in enumerate(PROMPTS):
        name = FILES[i]
        print(f"  Generating Agnes image for {name}...")
        img_data = agnes_image(prompt)
        bg_b64 = base64.b64encode(img_data).decode()
        svg = makers[i](bg_b64)
        svg_path = os.path.join(ROOT, f"{name}.svg")
        png_path = os.path.join(ROOT, f"{name}.png")
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(svg)
        subprocess.run(
            ["inkscape", svg_path, "-o", png_path, "-w", "1024", "-h", "1024"],
            check=True, capture_output=True
        )
        sz = os.path.getsize(png_path) // 1024
        print(f"  {name}.png ({sz} KB)")
    print("Done! 4 cards generated.")
