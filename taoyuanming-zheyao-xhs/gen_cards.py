#!/usr/bin/env python3
"""Generate 4 cards for 陶渊明."""
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
    "Ancient Chinese poet in simple robes standing in a chrysanthemum garden, holding a wine cup, looking at distant mountains, serene and elegant, traditional Chinese ink wash painting, Song dynasty aesthetic, green and earthy tones, pastoral",
    "Ancient Chinese magistrate in a modest government office, taking off his official robe, quitting his post with dignity, traditional Chinese ink wash painting, Song dynasty aesthetic, muted brown and green tones",
    "Ancient Chinese paradise landscape, a hidden valley with peach blossoms in full bloom, a small fishing boat entering a cave, the Peach Blossom Spring, traditional Chinese ink wash painting, Song dynasty aesthetic, pink and green tones, dreamy",
    "Ancient Chinese poet sitting under a chrysanthemum hedge by a fence, drinking wine, facing the South Mountain, peaceful rural life, traditional Chinese ink wash painting, Song dynasty aesthetic, warm golden and green tones, serene",
]

FILES = ["taoyuanming-cover", "taoyuanming-card-1", "taoyuanming-card-2", "taoyuanming-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="30%" stop-color="#000" stop-opacity="0.1"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.55"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#16A34A" letter-spacing="6" {STROKE}>东晋·隐逸诗人</text>
<text x="512" y="360" text-anchor="middle" font-family="{FONT}" font-size="140" font-weight="900" fill="#FFFFFF" letter-spacing="10" {STROKE}>陶渊明</text>
<rect x="262" y="405" width="500" height="3" rx="1.5" fill="#16A34A" opacity="0.6"/>
<text x="512" y="510" text-anchor="middle" font-family="{FONT}" font-size="48" font-weight="800" fill="#16A34A" letter-spacing="6" {STROKE}>不为五斗米折腰</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="24" fill="#E2E8F0" {STROKE_S}>83天县令 · 桃花源记 · 采菊东篱下</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#陶渊明 #不为五斗米折腰 #桃花源记 #东晋 #隐士</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#16A34A" letter-spacing="3" {STROKE}>不为五斗米折腰</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#16A34A"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>彭泽县令</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>为了养家，当了彭泽县县令</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#16A34A"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>83天辞职</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>不为五斗米折腰，当天辞官回家种地</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#16A34A"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>归园田居</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>"少无适俗韵，性本爱丘山"</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>中国文人气节的最高表达</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#陶渊明 #归园田居 #五斗米 #隐逸 #魏晋风骨</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#16A34A" letter-spacing="3" {STROKE}>桃花源记</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#16A34A"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>武陵渔人</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>偶然发现一个与世隔绝的世外桃源</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#16A34A"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>理想国</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>没有战争，没有赋税，不知秦汉魏晋</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#16A34A"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>中国精神家园</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>每个失意的中国文人心里都有一座桃花源</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>阡陌交通，鸡犬相闻——永恒的乌托邦</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#陶渊明 #桃花源记 #世外桃源 #乌托邦</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#16A34A" letter-spacing="3" {STROKE}>采菊东篱下</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#16A34A"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>田园诗开创者</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>种田、饮酒、写诗——平淡中有至味</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#16A34A"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>苏轼评价</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>"质而实绮，癯而实腴"——朴素却华丽</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#16A34A"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>身后名</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>生前无人问津，死后被推上神坛</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>采菊东篱下，悠然见南山</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#陶渊明 #田园诗 #苏轼 #采菊东篱下 #中国文学</text>
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
