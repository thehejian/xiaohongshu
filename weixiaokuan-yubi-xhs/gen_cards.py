#!/usr/bin/env python3
"""Generate 4 cards for 韦孝宽."""
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
    "Ancient Chinese general in iron armor standing on a fortress wall overlooking a besieging army, determined defender of a crucial fortress, traditional Chinese ink wash painting, Song dynasty aesthetic, iron gray and deep blue palette, epic defensive scene",
    "Ancient Chinese fortress under siege, siege towers, battering rams, tunnels, various attack methods against a fortified city wall, intense battle scene, traditional Chinese ink wash painting, Song dynasty aesthetic, dark and dramatic tones",
    "Ancient Chinese warlord sick on a battlefield, depressed after a failed siege, a meteor falling in the night sky, defeat and despair, traditional Chinese ink wash painting, Song dynasty aesthetic, muted gray and dark red tones",
    "Ancient Chinese strategist and general in old age writing a unification strategy document, planning to reunite the divided land, traditional Chinese ink wash painting, Song dynasty aesthetic, warm gray and gold tones, scholarly dignity",
]

FILES = ["weixiaokuan-cover", "weixiaokuan-card-1", "weixiaokuan-card-2", "weixiaokuan-card-3"]

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
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#475569" letter-spacing="6" {STROKE}>西魏·北周名将</text>
<text x="512" y="360" text-anchor="middle" font-family="{FONT}" font-size="140" font-weight="900" fill="#FFFFFF" letter-spacing="10" {STROKE}>韦孝宽</text>
<rect x="262" y="405" width="500" height="3" rx="1.5" fill="#475569" opacity="0.6"/>
<text x="512" y="510" text-anchor="middle" font-family="{FONT}" font-size="48" font-weight="800" fill="#475569" letter-spacing="6" {STROKE}>玉壁之战定乾坤</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="24" fill="#E2E8F0" {STROKE_S}>孤城抗高欢 · 50天对决 · 一战崩北齐</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#韦孝宽 #玉壁之战 #高欢 #北周 #北齐 #守城名将</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#475569" letter-spacing="3" {STROKE}>玉壁攻防神战</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#475569"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>546年高欢亲征</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>高欢倾全国之力进攻玉壁，志在必得</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#475569"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>见招拆招</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>堆土山？加城墙。挖地道？横沟截击。</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#475569"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>纹丝不动</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>打了50天，高欢用尽所有方法，玉壁不动</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>南北朝最经典的守城战</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#韦孝宽 #玉壁之战 #攻城战 #古代兵法</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#DC2626" letter-spacing="3" {STROKE}>气死高欢</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#DC2626"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>死伤七万</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>高欢军队损失惨重，锐气尽丧</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#DC2626"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>陨星坠营</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>一夜陨星坠入大营，高欢撤军</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#DC2626"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>含恨而终</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>回去没多久就病死了，一代枭雄就此终结</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>一座城，打垮了一个时代</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#韦孝宽 #高欢 #玉壁之战 #北齐 #北周</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#475569" letter-spacing="3" {STROKE}>平汉策·身后局</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#475569"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>平汉策</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>上书统一蓝图的战略规划</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#475569"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>北周东扩</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>玉壁之胜奠定西魏/北周东向扩张的基础</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#475569"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>580年去世</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>死后一年杨坚建隋，九年后天下统一</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>他奠基的胜利，后人摘了果实</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#韦孝宽 #平汉策 #北周 #隋 #统一</text>
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
