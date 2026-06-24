#!/usr/bin/env python3
"""Generate 4 cards for 萧衍."""
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
    "Ancient Chinese emperor in magnificent golden and vermilion dragon robes, seated on a grand throne, founding emperor of the Liang dynasty at the peak of his power, traditional Chinese ink wash painting, Song dynasty aesthetic, gold and vermilion palette, majestic",
    "Ancient Chinese prosperous capital city of Jiankang during the Liang dynasty, flourishing culture, scholars gathering, golden age of literature, traditional Chinese ink wash painting, Song dynasty aesthetic, warm golden tones, peaceful",
    "Ancient Chinese Buddhist emperor in monk's robes with imperial ornaments, numerous temples in background, devout and majestic, traditional Chinese ink wash painting, Song dynasty aesthetic, gold and white palette, serene but grand",
    "Ancient Chinese palace in chaos, an elderly emperor trapped and starving in his own palace, rebel forces surrounding, tragic and desolate, traditional Chinese ink wash painting, Song dynasty aesthetic, dark gray and crimson tones, dramatic",
]

FILES = ["xiaoyan-cover", "xiaoyan-card-1", "xiaoyan-card-2", "xiaoyan-card-3"]

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
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#FFD700" letter-spacing="6" {STROKE}>南朝·梁武帝</text>
<text x="512" y="360" text-anchor="middle" font-family="{FONT}" font-size="140" font-weight="900" fill="#FFFFFF" letter-spacing="10" {STROKE}>萧衍</text>
<rect x="262" y="405" width="500" height="3" rx="1.5" fill="#FFD700" opacity="0.7"/>
<text x="512" y="510" text-anchor="middle" font-family="{FONT}" font-size="42" font-weight="800" fill="#FFD700" letter-spacing="6" {STROKE}>时来天地皆同力</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="24" fill="#E2E8F0" {STROKE_S}>48年皇帝 · 菩萨天子 · 饿死台城</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#萧衍 #梁武帝 #南朝 #菩萨皇帝 #侯景 #南北朝</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>时来天地皆同力</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>前三十年盛世</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>勤于政事，任用贤能，南朝太平天子</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>文化黄金时代</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>梁朝是南朝文学最繁荣的时期</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>在位48年</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>南朝在位最长的皇帝</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>前半生，他配得上"英明神武"四个字</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#萧衍 #梁武帝 #梁朝 #南朝 #太平盛世</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>菩萨天子</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>四次出家</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>四次当和尚，每次朝廷花几亿钱"赎"回</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>四百八十寺</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>杜牧——"南朝四百八十寺，多少楼台烟雨中"</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>信佛的代价</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>不杀生、不死刑，对叛徒心慈手软</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>最虔诚的皇帝佛教徒，也是最糊涂的</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#萧衍 #菩萨皇帝 #佛教 #南朝四百八十寺 #杜牧</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#DC2626" letter-spacing="3" {STROKE}>运去英雄不自由</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#DC2626"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>548年侯景之乱</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>收留的降将侯景，反过来毁灭了他</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#DC2626"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>儿子冷眼旁观</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>诸王各怀鬼胎，无人救驾</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#DC2626"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>86岁饿死台城</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>当了48年皇帝，最后连口饭都吃不上</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>时来天地皆同力，运去英雄不自由</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#萧衍 #梁武帝 #侯景之乱 #台城 #罗隐</text>
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
