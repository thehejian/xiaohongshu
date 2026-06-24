#!/usr/bin/env python3
"""Generate 4 cards for Shi Hu / Later Zhao tyrant using Agnes AI backgrounds."""
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
    "Dark cinematic portrait of a cruel ancient Chinese tyrant king with blood-red armor and a dark crown, sitting on a skull throne, burning palace in background, dramatic lightning, stormy sky, red and black tones, traditional Chinese ink wash meets dark fantasy, terrifying imperial presence, Song dynasty aesthetic",
    "Dark ancient Chinese palace scene, a tyrannical king ordering executions, soldiers dragging prisoners, blood on marble floors, dramatic dark lighting, traditional Chinese painting style, red candles casting shadows, terrifying atmosphere, imperial cruelty",
    "Ancient Chinese Buddhist temple contrasting with a dark palace in background, a tyrant king praying before a golden Buddha while soldiers kill outside, dramatic contrast between peace and violence, traditional ink wash painting, ironic juxtaposition, dark spiritual atmosphere",
    "Ancient Chinese capital city in flames at night, burning palaces and collapsing walls, dark smoke against red sky, fleeing civilians and soldiers, apocalyptic scene, traditional Chinese painting meets dark disaster epic, tragic historical moment, massive destruction",
]

FILES = ["shihu-cover", "shihu-card-1", "shihu-card-2", "shihu-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="40%" stop-color="#000" stop-opacity="0.2"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.7"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="40" font-weight="700" fill="#FF4444" letter-spacing="8" {STROKE}>五胡十六国</text>
<text x="512" y="400" text-anchor="middle" font-family="{FONT}" font-size="170" font-weight="900" fill="#FFFFFF" letter-spacing="4" {STROKE}>石虎</text>
<rect x="312" y="445" width="400" height="3" rx="1.5" fill="#FF4444" opacity="0.7"/>
<text x="512" y="550" text-anchor="middle" font-family="{FONT}" font-size="56" font-weight="800" fill="#FF4444" letter-spacing="5" {STROKE}>十六国第一暴君</text>
<text x="512" y="630" text-anchor="middle" font-family="{FONT}" font-size="28" fill="#E2E8F0" {STROKE_S}>拜佛也杀人</text>
<g transform="translate(262, 710)">
  <text x="0" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>石勒养子</text>
  <text x="250" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="middle" {STROKE_S}>后赵第三帝</text>
  <text x="500" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="end" {STROKE_S}>334 - 349</text>
</g>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#石虎 #后赵 #十六国 #暴君</text>
''')

def make_card_1(bg_b64):
    items = [
        ("篡位夺权", "石勒死后杀光其子孙，自登帝位"),
        ("征发百万", "强征数百万民夫修宫殿、筑长城"),
        ("杀人如麻", "动辄灭门，太子妻儿亦不放过"),
        ("骨肉相残", "太子石宣被活活烧死，三百余人连坐"),
    ]
    items_svg = ""
    for i, (title, desc) in enumerate(items):
        y = 175 + i * 145
        items_svg += f'''
<g transform="translate(40, {y})">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#FF4444"/>
  <text x="30" y="48" font-family="{FONT}" font-size="30" font-weight="700" fill="#FF4444" {STROKE}>{title}</text>
  <text x="30" y="88" font-family="{FONT}" font-size="24" fill="#FFFFFF" {STROKE_S}>{desc}</text>
</g>'''
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FF4444" letter-spacing="3" {STROKE}>暴行录</text>
{items_svg}
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FF4444" letter-spacing="3" {STROKE}>信佛的暴君</text>

<g transform="translate(40, 160)">
  <rect x="0" y="0" width="944" height="170" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="170" rx="3" fill="#FF4444"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#FF4444" {STROKE}>国教佛教</text>
  <text x="30" y="98" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>中国第一位立佛教为国教的皇帝</text>
  <text x="30" y="135" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>拜高僧佛图澄为国师</text>
</g>

<g transform="translate(40, 370)">
  <rect x="0" y="0" width="944" height="170" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="170" rx="3" fill="#CBD5E1" opacity="0.5"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#E2E8F0" {STROKE}>佛图澄的劝诫</text>
  <text x="30" y="98" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>高僧多次劝其戒杀，石虎表面听从</text>
  <text x="30" y="135" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>一边拜佛一边杀人，杀比拜多</text>
</g>

<g transform="translate(40, 580)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#FF4444"/>
  <text x="30" y="44" font-family="{FONT}" font-size="28" font-weight="700" fill="#FF4444" {STROKE}>讽刺</text>
  <text x="30" y="90" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>中国历史上最虔诚的佛教皇帝之一</text>
  <text x="30" y="118" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>也是中国历史上最残暴的皇帝之一</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#石虎 #佛图澄 #佛教 #十六国</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FF4444" letter-spacing="3" {STROKE}>王朝崩塌</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#FF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FF4444" {STROKE}>石虎死后</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>诸子争位，自相残杀</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>养孙冉闵趁机崛起</text>
</g>

<g transform="translate(40, 340)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#CBD5E1" opacity="0.5"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#E2E8F0" {STROKE}>杀胡令</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>冉闵下令屠杀胡人</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>一夜之间二十万胡人被杀</text>
</g>

<g transform="translate(40, 530)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#FF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FF4444" {STROKE}>后赵覆灭</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>石虎建立的王朝在血腥中终结</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>比之前的任何一个政权都惨烈</text>
</g>

<text x="512" y="820" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#FF4444" {STROKE}>权力落在疯子手里，就是灾难</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#石虎 #后赵 #冉闵 #杀胡令 #历史</text>
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
