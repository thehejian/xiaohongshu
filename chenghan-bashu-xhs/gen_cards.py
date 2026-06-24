#!/usr/bin/env python3
"""Generate 4 cards for 成汉."""
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
    "Ancient Chinese mountain fortress in Sichuan, a Di tribe leader rallying refugees, founding of the Cheng-Han kingdom, misty Sichuan landscape, traditional Chinese ink wash painting, Song dynasty aesthetic, deep green and earthy tones",
    "Ancient Chinese refugee camp in Sichuan, starving people being fed by a tribal leader, compassion and rebellion brewing, traditional Chinese ink wash painting, Song dynasty aesthetic, warm brown and green tones, human drama",
    "Ancient Chinese capital city of Chengdu during the Cheng-Han kingdom, peaceful prosperous Sichuan basin, mountains surrounding, traditional Chinese ink wash painting, Song dynasty aesthetic, lush green and gold tones, peaceful",
    "Ancient Chinese battle scene, a Jin dynasty general leading a small elite army into Chengdu, conquering the Cheng-Han kingdom, dramatic river battle on the Yangtze, traditional Chinese ink wash painting, Song dynasty aesthetic, blue and crimson tones",
]

FILES = ["chenghan-cover", "chenghan-card-1", "chenghan-card-2", "chenghan-card-3"]

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
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#16A34A" letter-spacing="6" {STROKE}>十六国·巴氐</text>
<text x="512" y="360" text-anchor="middle" font-family="{FONT}" font-size="140" font-weight="900" fill="#FFFFFF" letter-spacing="10" {STROKE}>成汉</text>
<rect x="262" y="405" width="500" height="3" rx="1.5" fill="#16A34A" opacity="0.6"/>
<text x="512" y="510" text-anchor="middle" font-family="{FONT}" font-size="48" font-weight="800" fill="#16A34A" letter-spacing="6" {STROKE}>巴氐立国巴蜀</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="24" fill="#E2E8F0" {STROKE_S}>304-347 · 李雄治蜀 · 桓温西征</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#成汉 #李雄 #十六国 #巴氐 #四川 #桓温</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#16A34A" letter-spacing="3" {STROKE}>李特流民起义</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#16A34A"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>氐人流民</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>关中大饥荒，氐人首领李特率流民入蜀</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#16A34A"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>开仓济民</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>李特深得人心，朝廷下令驱逐时被迫起兵</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#16A34A"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>战死托孤</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>李特战死，儿子李雄继承大业</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>一场难民起义，开启了一个王国</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#成汉 #李特 #流民起义 #氐族 #四川</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#16A34A" letter-spacing="3" {STROKE}>李雄治蜀</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#16A34A"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>304年称帝</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>攻占成都，国号"成"（后改"汉"）</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#16A34A"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>三十载太平</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>轻徭薄赋，刑法宽松，蜀中乐土</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#16A34A"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>十六国中的异类</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>不争霸中原，专心经营蜀地</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>乱世中的一片乐土</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#成汉 #李雄 #成都 #巴蜀 #十六国</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#DC2626" letter-spacing="3" {STROKE}>桓温灭成汉</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#DC2626"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>李雄死后崩坏</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>子李期残暴，侄李寿夺位后也挥霍无度</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#DC2626"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>347年西征</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>桓温一万人逆长江而上，成都城外大破敌军</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#DC2626"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>43年而终</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>成汉灭亡，四川重回东晋版图</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>桓温的成名之战，也是成汉的终章</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#成汉 #桓温 #东晋 #四川 #十六国 #李势</text>
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
