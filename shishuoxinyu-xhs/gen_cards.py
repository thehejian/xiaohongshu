#!/usr/bin/env python3
"""Generate 4 cards for 世说新语."""
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
    "Ancient Chinese literati scene, a group of elegant scholars in flowing robes gathered in a bamboo grove, discussing philosophy and poetry, traditional Chinese ink wash painting, Song dynasty aesthetic, jade green and warm gold tones, refined and intellectual atmosphere, classical Chinese landscape",
    "Ancient Chinese scene of a scholar compiling a book in a library, surrounded by scrolls and manuscripts, candlelight, traditional Chinese ink wash painting, warm amber tones, scholarly atmosphere, Song dynasty aesthetic",
    "Ancient Chinese winter night scene, a scholar in a small boat on a snowy river, traveling to visit a friend, traditional Chinese ink wash painting, monochrome blue-gray tones, poetic and minimalist atmosphere, Song dynasty aesthetic",
    "Ancient Chinese scene of a scholar playing围棋 (weiqi) while receiving urgent battle news, remaining completely composed, pavilion setting with autumn colors, traditional Chinese ink wash painting, warm gold and green tones, graceful atmosphere",
]

FILES = ["sxy-cover", "sxy-card-1", "sxy-card-2", "sxy-card-3"]

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
<text x="512" y="170" text-anchor="middle" font-family="{FONT}" font-size="28" font-weight="700" fill="#22C55E" letter-spacing="6" {STROKE}>六朝文学巅峰</text>
<text x="512" y="340" text-anchor="middle" font-family="{FONT}" font-size="80" font-weight="900" fill="#FFFFFF" letter-spacing="8" {STROKE}>世说新语</text>
<rect x="312" y="380" width="400" height="3" rx="1.5" fill="#22C55E" opacity="0.6"/>
<text x="512" y="500" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#22C55E" letter-spacing="4" {STROKE}>名士风流三百年</text>
<text x="512" y="620" text-anchor="middle" font-family="{FONT}" font-size="24" fill="#E2E8F0" {STROKE_S}>东汉末 → 东晋 · 36门 · 一千五百年的审美天花板</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#世说新语 #魏晋风度 #刘义庆 #名士风流</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="800" fill="#22C55E" letter-spacing="3" {STROKE}>一部书定义一个时代</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#22C55E"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#22C55E" {STROKE}>刘义庆</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>南朝宋宗室，召集门客精选数百种典籍编成</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#22C55E"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#22C55E" {STROKE}>三百年名人轶事</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>从东汉末到东晋末，一部魏晋真人秀</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#22C55E"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#22C55E" {STROKE}>36门人格体系</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>德行·言语·政事·文学·方正·雅量·容止·品藻</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#22C55E" {STROKE}>每个名士都被放进一个"门"里打分</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#世说新语 #刘义庆 #文学 #魏晋</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="800" fill="#38BDF8" letter-spacing="3" {STROKE}>顶流名场面</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#38BDF8"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#38BDF8" {STROKE}>雪夜访戴</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>王子猷大雪乘舟访友，到了门口转身就走</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#38BDF8"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#38BDF8" {STROKE}>东床坦腹</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>王羲之露着肚子吃东西，被选为最佳女婿</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#38BDF8"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#38BDF8" {STROKE}>小儿辈大破贼</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>淝水大捷，谢安淡定下棋："小儿辈遂已破贼"</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#38BDF8" {STROKE}>乘兴而行，兴尽而返——何必见戴</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#雪夜访戴 #王羲之 #东床坦腹 #谢安 #淝水之战</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="800" fill="#E2E8F0" letter-spacing="3" {STROKE}>千年回响</text>

<g transform="translate(40, 180)">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#22C55E"/>
  <text x="30" y="42" font-family="{FONT}" font-size="26" font-weight="700" fill="#22C55E" {STROKE}>中国文人的"圣经"</text>
  <text x="30" y="82" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>一千五百年来，没有哪本书比世说新语</text>
  <text x="30" y="110" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>更能代表中国文人的精神世界</text>
</g>

<g transform="translate(40, 340)">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#38BDF8"/>
  <text x="30" y="42" font-family="{FONT}" font-size="26" font-weight="700" fill="#38BDF8" {STROKE}>文学影响</text>
  <text x="30" y="82" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>后世诗词、小说、戏曲无不引用它的典故</text>
  <text x="30" y="110" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>"雪夜访戴""东床坦腹"已成汉语成语</text>
</g>

<g transform="translate(40, 500)">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#22C55E"/>
  <text x="30" y="42" font-family="{FONT}" font-size="26" font-weight="700" fill="#22C55E" {STROKE}>人格审美</text>
  <text x="30" y="82" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>"雅量""容止""品藻"——定义了中国人</text>
  <text x="30" y="110" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>对风度与气质的终极想象</text>
</g>

<text x="512" y="760" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#22C55E" {STROKE}>一部书，定义了魏晋三百年的风流</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#世说新语 #魏晋风度 #文学 #经典</text>
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
