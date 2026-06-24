#!/usr/bin/env python3
"""Generate 4 cards for Tuoba Gui / Northern Wei using Agnes AI backgrounds."""
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
    "Epic cinematic portrait of a young Xianbei warrior king in magnificent armor on a ridge at sunrise, vast northern steppe in background, fur cloak and iron helmet, traditional Chinese ink wash meets epic fantasy, powerful young emperor, golden dawn light, Song dynasty aesthetic",
    "Massive ancient battlefield scene at dawn, Xianbei cavalry ambushing a larger army in a mountain valley, chaos and dust, dramatic morning mist, traditional Chinese ink wash painting meets cinematic epic, ambush battle, thousands of soldiers, Song dynasty aesthetic",
    "Ancient northern Chinese frontier, Xianbei nomads settling into farming villages, people plowing fields, a young king overseeing the transformation, blend of steppe and Chinese culture, traditional Chinese painting, civilizational transition, epic historical scroll style",
    "Dark ancient palace interior at night, a paranoid emperor on throne surrounded by shadows, empty hall with flickering candles, a lone assassin figure approaching from behind, tragic atmosphere, traditional Chinese painting style, dark cinematic lighting, psychological tension",
]

FILES = ["tuobagui-cover", "tuobagui-card-1", "tuobagui-card-2", "tuobagui-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="40%" stop-color="#000" stop-opacity="0.15"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.65"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="40" font-weight="700" fill="#3B82F6" letter-spacing="8" {STROKE}>五胡十六国</text>
<text x="512" y="400" text-anchor="middle" font-family="{FONT}" font-size="170" font-weight="900" fill="#FFFFFF" letter-spacing="4" {STROKE}>拓跋珪</text>
<rect x="312" y="445" width="400" height="3" rx="1.5" fill="#3B82F6" opacity="0.7"/>
<text x="512" y="550" text-anchor="middle" font-family="{FONT}" font-size="52" font-weight="800" fill="#3B82F6" letter-spacing="4" {STROKE}>北魏开国雄主</text>
<text x="512" y="630" text-anchor="middle" font-family="{FONT}" font-size="28" fill="#E2E8F0" {STROKE_S}>十六国的终结者，南北朝的开端</text>
<g transform="translate(262, 710)">
  <text x="0" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>鲜卑拓跋部</text>
  <text x="250" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="middle" {STROKE_S}>北魏道武帝</text>
  <text x="500" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="end" {STROKE_S}>386 - 409</text>
</g>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#拓跋珪 #北魏 #参合陂 #鲜卑 #南北朝</text>
''')

def make_card_1(bg_b64):
    items = [
        ("代国后裔", "淝水战后趁乱重建代国，改称北魏"),
        ("16岁称帝", "386年即代王位，改国号为魏"),
        ("参合陂之战", "395年诱歼后燕大军，一战定北方"),
        ("终结十六国", "为北魏统一北方奠定了基础"),
    ]
    items_svg = ""
    for i, (title, desc) in enumerate(items):
        y = 175 + i * 145
        items_svg += f'''
<g transform="translate(40, {y})">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#3B82F6"/>
  <text x="30" y="48" font-family="{FONT}" font-size="30" font-weight="700" fill="#3B82F6" {STROKE}>{title}</text>
  <text x="30" y="88" font-family="{FONT}" font-size="24" fill="#FFFFFF" {STROKE_S}>{desc}</text>
</g>'''
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#3B82F6" letter-spacing="3" {STROKE}>崛起之路</text>
{items_svg}
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#3B82F6" letter-spacing="3" {STROKE}>参合陂之战</text>

<g transform="translate(40, 160)">
  <rect x="0" y="0" width="944" height="170" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="170" rx="3" fill="#3B82F6"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#3B82F6" {STROKE}>背景</text>
  <text x="30" y="98" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>后燕慕容垂派太子慕容宝率军攻魏</text>
  <text x="30" y="135" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>拓跋珪诱敌深入，退兵千里</text>
</g>

<g transform="translate(40, 370)">
  <rect x="0" y="0" width="944" height="170" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="170" rx="3" fill="#CBD5E1" opacity="0.5"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#E2E8F0" {STROKE}>突袭</text>
  <text x="30" y="98" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>参合陂夜袭，后燕军猝不及防</text>
  <text x="30" y="135" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>数万大军几乎全军覆没</text>
</g>

<g transform="translate(40, 580)">
  <rect x="0" y="0" width="944" height="170" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="170" rx="3" fill="#3B82F6"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#3B82F6" {STROKE}>后果</text>
  <text x="30" y="98" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>慕容垂次年亲征，见尸骨如山吐血而亡</text>
  <text x="30" y="135" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>北魏一举成为北方最强势力</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#拓跋珪 #参合陂 #慕容垂 #后燕</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#3B82F6" letter-spacing="3" {STROKE}>功过与结局</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#3B82F6"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#3B82F6" {STROKE}>治国功绩</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>离散部落，定居农耕</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>重用汉人士族，建立官僚制度</text>
</g>

<g transform="translate(40, 340)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#CBD5E1" opacity="0.5"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#E2E8F0" {STROKE}>晚年昏暴</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>沉迷丹药，多疑暴虐，动辄杀人</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>众叛亲离，人人自危</text>
</g>

<g transform="translate(40, 530)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#3B82F6"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#3B82F6" {STROKE}>被刺身亡</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>409年被儿子拓跋绍刺杀</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>年仅39岁，令人唏嘘</text>
</g>

<text x="512" y="820" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#3B82F6" {STROKE}>开国雄主，死于亲子之手</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#拓跋珪 #北魏 #历史</text>
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
