#!/usr/bin/env python3
"""Generate beautiful cards for Murong Chui using Agnes AI backgrounds with big readable text."""
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
    "Epic cinematic portrait of an ancient Chinese warrior general in magnificent red and black armor, standing on a misty mountain peak at golden sunrise, traditional ink wash painting style meets epic fantasy, dramatic clouds, red war banners flying, majestic composition, Song dynasty aesthetic, golden light, highly detailed",
    "Ancient Chinese historical scroll painting style, a winding timeline of war banners and marching armies across a vast landscape, misty mountains, traditional ink wash, red seals and calligraphy elements, panoramic epic scene, aged parchment texture, Song dynasty battlefield panorama",
    "Epic ancient Chinese cavalry battle scene at dawn, thousands of warriors with red banners charging across a misty plain, dramatic storm clouds, dust and smoke, traditional ink wash painting meets cinematic epic, Song dynasty aesthetic, dynamic composition, rich red and gold tones, highly detailed dramatic battle",
    "A solitary ancient Chinese general in armor on a mountain cliff overlooking a vast river valley at sunset, contemplative mood, golden hour light through mist, traditional Chinese ink wash painting, poetic atmosphere, fading light, cranes flying in distance, philosophical Chinese landscape, masterpiece quality",
]

FILES = ["murong-cover", "murong-card-1", "murong-card-2", "murong-card-3"]

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
<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="42" font-weight="700" fill="#FFD700" letter-spacing="8" {STROKE}>五胡十六国</text>
<text x="512" y="400" text-anchor="middle" font-family="{FONT}" font-size="170" font-weight="900" fill="#FFFFFF" letter-spacing="4" {STROKE}>慕容垂</text>
<rect x="312" y="445" width="400" height="3" rx="1.5" fill="#FFD700" opacity="0.7"/>
<text x="512" y="545" text-anchor="middle" font-family="{FONT}" font-size="55" font-weight="800" fill="#FFD700" letter-spacing="5" {STROKE}>十六国第一战神</text>
<text x="512" y="630" text-anchor="middle" font-family="{FONT}" font-size="30" fill="#FFFFFF" {STROKE_S}>从亡命客到复国者的悲壮一生</text>
<rect x="262" y="680" width="500" height="1" rx="0.5" fill="#FFFFFF" opacity="0.3"/>
<g transform="translate(262, 710)">
  <text x="0" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>后燕建立者</text>
  <text x="250" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="middle" {STROKE_S}>慕容皝第五子</text>
  <text x="500" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="end" {STROKE_S}>327 - 396</text>
</g>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#五胡十六国 #慕容垂 #后燕 #历史</text>
''')

def make_card_1(bg_b64):
    events = [
        ("327", "生于前燕皇族", "慕容皝第五子，鲜卑慕容部"),
        ("340", "13岁随父出征", "勇冠三军，初露锋芒"),
        ("369", "投奔前秦苻坚", "功高震主遭猜忌，被迫出逃"),
        ("383", "淝水之战", "率3万军完整撤退，护送苻坚"),
        ("384", "称燕王复国", "河北重建燕国（后燕）"),
        ("386", "后燕极盛", "灭翟魏、西燕，统一慕容故地"),
        ("395", "参合陂之役", "70岁亲征，目睹儿败吐血而亡"),
    ]
    items = ""
    for i, (year, title, desc) in enumerate(events):
        y = 165 + i * 100
        items += f'''
<g transform="translate(40, {y})">
  <rect x="0" y="0" width="944" height="82" rx="12" fill="#0F172A" opacity="0.8"/>
  <rect x="0" y="0" width="5" height="82" rx="2" fill="#FFD700"/>
  <text x="30" y="38" font-family="{FONT}" font-size="22" font-weight="800" fill="#FFD700" {STROKE_S}>{year}</text>
  <text x="130" y="38" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFFFFF" {STROKE_S}>{title}</text>
  <text x="130" y="66" font-family="{FONT}" font-size="20" fill="#CBD5E1" {STROKE_S}>{desc}</text>
</g>'''
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>慕容垂生平大事记</text>
{items}
<text x="512" y="970" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#64748B" {STROKE_S}>327 — 396 · 七十年波澜壮阔</text>
''')

def make_card_2(bg_b64):
    battles = [
        ("淝水之战", "383", "苻坚87万大军惨败，慕容垂3万军队完整撤退，以忠义护送苻坚"),
        ("邺城之战", "384", "慕容垂以少胜多平定河北，奠定后燕立国根基"),
        ("滑台之战", "385", "智取翟魏收复河南，展现慕容垂老辣军事智慧"),
    ]
    items = ""
    for i, (name, year, desc) in enumerate(battles):
        y = 180 + i * 250
        items += f'''
<g transform="translate(40, {y})">
  <rect x="0" y="0" width="944" height="220" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="220" rx="3" fill="#FFD700"/>
  <text x="30" y="55" font-family="{FONT}" font-size="40" font-weight="800" fill="#FFD700" {STROKE}>{name}</text>
  <text x="230" y="55" font-family="{FONT}" font-size="24" fill="#CBD5E1" {STROKE_S}>{year}</text>
  <line x1="30" y1="78" x2="930" y2="78" stroke="#334155" stroke-width="1"/>
  <text x="30" y="128" font-family="{FONT}" font-size="24" fill="#FFFFFF" {STROKE_S}>{desc}</text>
</g>'''
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>经典战役</text>
{items}
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>历史评价</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="220" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="220" rx="3" fill="#FFD700"/>
  <text x="472" y="50" text-anchor="middle" font-family="{FONT}" font-size="24" font-weight="700" fill="#FFD700" {STROKE_S}>《晋书》评价</text>
  <text x="512" y="120" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="700" fill="#FFFFFF" letter-spacing="2" {STROKE}>"慕容垂者，霸王之器也"</text>
  <text x="512" y="170" text-anchor="middle" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>—— 兼具霸主的器量与仁德</text>
</g>

<g transform="translate(40, 410)">
  <rect x="0" y="0" width="944" height="170" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="170" rx="3" fill="#94A3B8" opacity="0.5"/>
  <text x="472" y="42" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="700" fill="#E2E8F0" {STROKE_S}>与项羽并论</text>
  <text x="35" y="90" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>同样力拔山兮气盖世，同样因内部问题功败垂成</text>
  <text x="35" y="130" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>不同的是，慕容垂在流亡中隐忍二十年</text>
  <text x="35" y="165" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>暮年才完成复国大业，比项羽更坚韧</text>
</g>

<g transform="translate(40, 620)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#94A3B8" opacity="0.5"/>
  <text x="472" y="40" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="700" fill="#E2E8F0" {STROKE_S}>军事天才</text>
  <text x="35" y="82" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>一生未尝败绩，从无到有重建后燕</text>
  <text x="35" y="118" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>却在最惨痛的失败中落幕——那是儿子的失败，不是他的</text>
</g>

<text x="512" y="840" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>战神落幕，气节长存</text>
<text x="512" y="970" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#慕容垂 #后燕 #十六国 #五胡十六国</text>
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
    print("Done! 4 cards regenerated.")
