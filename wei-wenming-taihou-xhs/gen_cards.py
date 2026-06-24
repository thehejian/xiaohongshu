#!/usr/bin/env python3
"""Generate 4 cards for 北魏文明太后 — focused on achievements."""
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
    "Ancient Chinese imperial palace, a powerful empress dowager in magnificent gold and purple silk robes seated on dragon throne, Northern Wei dynasty, regal beautiful woman in her 40s with commanding presence, traditional Chinese painting meets cinematic epic, golden light, Song dynasty aesthetic",
    "Ancient northern Chinese capital scene, an empress dowager reviewing tax records and land registers with Chinese scholar-officials, implementing fair governance, traditional Chinese painting, golden sunset light, scrolls on desks, Song dynasty aesthetic",
    "Ancient Chinese court scene, an empress dowager behind a screen holding court, ministers bowing before her, a young boy emperor beside her, political power dynamics, traditional Chinese painting, majestic atmosphere with deep shadows, Song dynasty aesthetic",
    "Ancient northern Chinese farmland, farmers receiving land deeds from officials, new boundary markers, prosperous countryside, equitable land distribution, traditional Chinese painting, peaceful rural scene, golden harvest light, Song dynasty aesthetic",
]

FILES = ["wenmingtaihou-cover", "wenmingtaihou-card-1", "wenmingtaihou-card-2", "wenmingtaihou-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="30%" stop-color="#000" stop-opacity="0.1"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.6"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="700" fill="#FFD700" letter-spacing="6" {STROKE}>北魏·女政治家</text>
<text x="512" y="370" text-anchor="middle" font-family="{FONT}" font-size="150" font-weight="900" fill="#FFFFFF" letter-spacing="4" {STROKE}>文明太后</text>
<rect x="312" y="415" width="400" height="3" rx="1.5" fill="#FFD700" opacity="0.7"/>
<text x="512" y="520" text-anchor="middle" font-family="{FONT}" font-size="44" font-weight="800" fill="#FFD700" letter-spacing="4" {STROKE}>奠定百年国基的改革家</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>三朝摄政 · 俸禄制 · 均田制 · 三长制</text>
<g transform="translate(262, 710)">
  <text x="0" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>北燕皇族冯氏</text>
  <text x="250" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="middle" {STROKE_S}>文成帝皇后</text>
  <text x="500" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="end" {STROKE_S}>442 - 490</text>
</g>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#北魏 #文明太后 #冯太后 #均田制 #太和改制</text>
''')

def make_card_1(bg_b64):
    items = [
        ("俸禄制", "官员领薪俸，贪腐者处死，吏治一清"),
        ("均田制", "按人口授田，老死还田，影响三百年"),
        ("三长制", "邻长—里长—党长，加强中央集权"),
        ("培养孝文帝", "为太和改制和汉化改革奠定基础"),
    ]
    items_svg = ""
    for i, (title, desc) in enumerate(items):
        y = 175 + i * 145
        items_svg += f'''
<g transform="translate(40, {y})">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#FFD700"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#FFD700" {STROKE}>{title}</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>{desc}</text>
</g>'''
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>四大功绩</text>
{items_svg}
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>俸禄制</text>

<g transform="translate(40, 160)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>改革前</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>北魏官员无固定俸禄</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>只能靠掠夺百姓维持生计</text>
</g>

<g transform="translate(40, 350)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>改革后</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>按品级发放固定俸禄</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>贪腐满一匹者处死</text>
</g>

<g transform="translate(40, 540)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>影响</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>吏治清明，百姓负担减轻</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>被隋唐继承并完善</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#北魏 #文明太后 #俸禄制 #吏治</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>均田制与三长制</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>均田制</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>无主土地分给农民，按人口授田</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>老死还田，循环利用</text>
</g>

<g transform="translate(40, 330)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>三长制</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>邻长—里长—党长三级行政体系</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>取代宗族酋长制，加强中央集权</text>
</g>

<g transform="translate(40, 510)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>历史意义</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>为孝文帝全面汉化改革铺平道路</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>被隋唐继承，影响中国数百年</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#北魏 #文明太后 #均田制 #三长制 #历史</text>
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
