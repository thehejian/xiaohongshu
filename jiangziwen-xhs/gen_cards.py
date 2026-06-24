#!/usr/bin/env python3
"""Generate 4 cards for 蒋子文: 不敬苍天敬鬼神."""
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
    "Ancient Chinese supernatural scene, a ghostly official in white robes riding a white horse on a misty mountain, eerie atmosphere, traditional Chinese ink wash painting with ghost story aesthetic, dark purple and gray tones, Six Dynasties style, haunting and majestic",
    "Ancient Chinese scene of a city suffering from plagues and disasters, locusts and floods, dark clouds, panicked people, traditional Chinese ink wash painting, Song dynasty aesthetic, dark red and gray tones, apocalyptic atmosphere",
    "Ancient Chinese imperial court scene, a Wu kingdom emperor discussing with ministers, deciding to officially deify a local ghost, traditional Chinese ink wash painting, solemn and dramatic, dark gold and black tones",
    "Ancient Chinese underworld scene, a majestic deity with ghost soldiers in the mist, ruling over the spirit world, traditional Chinese ink wash painting, dark fantasy aesthetic, deep purple and red tones, epic and supernatural",
]

FILES = ["jiang-cover", "jiang-card-1", "jiang-card-2", "jiang-card-3"]

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
<text x="512" y="160" text-anchor="middle" font-family="{FONT}" font-size="28" font-weight="700" fill="#A78BFA" letter-spacing="6" {STROKE}>六朝鬼神志</text>
<text x="512" y="330" text-anchor="middle" font-family="{FONT}" font-size="80" font-weight="900" fill="#FFFFFF" letter-spacing="8" {STROKE}>蒋子文</text>
<rect x="312" y="370" width="400" height="3" rx="1.5" fill="#A78BFA" opacity="0.6"/>
<text x="512" y="500" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#A78BFA" letter-spacing="6" {STROKE}>不敬苍天敬鬼神</text>
<text x="512" y="600" text-anchor="middle" font-family="{FONT}" font-size="24" fill="#E2E8F0" {STROKE_S}>殉职小吏 → 孙权封神 → 六朝第一阴神</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#蒋子文 #六朝 #阴神 #孙权 #魏晋南北朝 #民间信仰</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="800" fill="#A78BFA" letter-spacing="3" {STROKE}>谁是蒋子文</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#A78BFA"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#A78BFA" {STROKE}>东汉末年的小官</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>秣陵县尉（相当于南京公安局局长）</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#A78BFA"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#A78BFA" {STROKE}>殉职钟山</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>追捕盗贼时被击中额头而死</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#A78BFA"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#A78BFA" {STROKE}>死而作祟</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>几十年后自称土地神，要求立庙祭祀</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#A78BFA" {STROKE}>生前没人知道，死后成了时代的精神图腾</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#蒋子文 #六朝 #民间信仰 #志怪</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="800" fill="#F59E0B" letter-spacing="3" {STROKE}>孙权封神</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#F59E0B"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#F59E0B" {STROKE}>瘟疫降临</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>没人给蒋子文立庙，虫灾水火灾接踵而至</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#F59E0B"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#F59E0B" {STROKE}>朝廷争议</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>大臣说妖言惑众，孙权的态度却很务实</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#F59E0B"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#F59E0B" {STROKE}>封侯建庙</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>追封中都侯，钟山改名蒋山大修庙宇</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#F59E0B" {STROKE}>他信的不是蒋子文，而是不信的代价他不敢承担</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#孙权 #蒋子文 #东吴 #六朝 #蒋山</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="800" fill="#EF4444" letter-spacing="3" {STROKE}>六朝第一阴神</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EF4444"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>历代祭祀</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>东晋、宋、齐、梁、陈——每个王朝都继续拜</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EF4444"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>从山神到冥帝</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>从地方土地神升级为掌管阴间的大帝</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EF4444"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>淝水阴兵</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>传说他带数万阴兵助阵东晋击败前秦</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>一个小官，硬是被恐惧和迷信塑造成了神</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#蒋子文 #六朝 #阴神 #淝水之战 #魏晋南北朝 #志怪</text>
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
