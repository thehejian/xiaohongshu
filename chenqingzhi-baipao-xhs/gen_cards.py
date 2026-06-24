#!/usr/bin/env python3
"""Generate 4 cards for 陈庆之."""
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
    "Ancient Chinese general in magnificent white robes leading an army, legendary 'White Robe General' of the Liang dynasty, heroic and elegant, thousands of troops, traditional Chinese ink wash painting, Song dynasty aesthetic, white and silver palette with deep blue accents, epic",
    "Ancient Chinese palace scene, a scholarly figure playing chess with an emperor, a bookish young man who would become a legendary general, traditional Chinese ink wash painting, Song dynasty aesthetic, warm gold and jade tones",
    "Ancient Chinese battlefield with 7000 white-robed soldiers charging against a massive army, dramatic victory against overwhelming odds, the Battle of Xingyang, traditional Chinese ink wash painting, Song dynasty aesthetic, white and crimson tones, epic action",
    "Ancient Chinese general in white robes entering the gates of Luoyang triumphant, citizens watching in awe, a southern army reaching the northern capital, traditional Chinese ink wash painting, Song dynasty aesthetic, grand and majestic with golden light",
]

FILES = ["chenqingzhi-cover", "chenqingzhi-card-1", "chenqingzhi-card-2", "chenqingzhi-card-3"]

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
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#FFFFFF" letter-spacing="6" {STROKE}>梁朝·白袍将军</text>
<text x="512" y="360" text-anchor="middle" font-family="{FONT}" font-size="140" font-weight="900" fill="#FFFFFF" letter-spacing="10" {STROKE}>陈庆之</text>
<rect x="262" y="405" width="500" height="3" rx="1.5" fill="#FFFFFF" opacity="0.5"/>
<text x="512" y="510" text-anchor="middle" font-family="{FONT}" font-size="42" font-weight="800" fill="#FFFFFF" letter-spacing="6" {STROKE}>千兵万马避白袍</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="24" fill="#E2E8F0" {STROKE_S}>书生将军 · 七千破三十万 · 攻入洛阳</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#陈庆之 #白袍将军 #千兵万马避白袍 #梁朝 #北伐</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFFFFF" letter-spacing="3" {STROKE}>书生将军</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFFFFF"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFFFFF" {STROKE}>棋童出身</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>梁武帝萧衍的棋童，因陪下棋被发掘</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFFFFF"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFFFFF" {STROKE}>不会武艺</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>拉不开弓，骑不了马——纯粹的战术天才</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFFFFF"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFFFFF" {STROKE}>被嘲笑</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>北魏将领笑他"书呆子带兵"——很快笑不出了</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFFFFF" {STROKE}>打仗靠脑子，不靠蛮力</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#陈庆之 #梁武帝 #萧衍 #书生将军</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFFFFF" letter-spacing="3" {STROKE}>七千白袍北伐</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFFFFF"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFFFFF" {STROKE}>527年起兵</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>带七千白袍军北伐，全部穿白色战袍</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFFFFF"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFFFFF" {STROKE}>荥阳之战</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>七千人大破三十万北魏军——史诗级逆袭</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFFFFF"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFFFFF" {STROKE}>连下三十二城</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>短短几个月，从边境打到洛阳</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFFFFF" {STROKE}>名师大将莫自牢，千兵万马避白袍</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#陈庆之 #白袍军 #荥阳 #北伐 #梁朝</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFFFFF" letter-spacing="3" {STROKE}>入洛·孤军·结局</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFFFFF"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFFFFF" {STROKE}>攻入洛阳</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>扶元颢为帝，北魏朝廷震惊逃窜</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFFFFF"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFFFFF" {STROKE}>孤军无援</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>萧衍不派援军，北魏反扑后全军覆没</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFFFFF"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFFFFF" {STROKE}>令人神往</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>毛泽东批语——"陈庆之令人神往"</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFFFFF" {STROKE}>虽败犹荣，千古白袍</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#陈庆之 #白袍将军 #毛泽东 #令人神往 #南北朝</text>
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
