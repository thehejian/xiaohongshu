#!/usr/bin/env python3
"""Generate 4 cards for 谢安谢玄."""
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
    "Two elegant ancient Chinese scholars and generals standing side by side on a mountain overlooking a vast river, one holding a chess piece, one holding a military banner, refined and heroic, traditional Chinese ink wash painting, Song dynasty aesthetic, purple and jade green palette",
    "Ancient Chinese noble scholar playing chess in a pavilion, reading a battle report with a calm smile, serene expression despite momentous news, elegant surroundings, traditional Chinese ink wash painting, Song dynasty aesthetic",
    "Ancient Chinese general inspecting elite troops, soldiers with determined faces and northern refugee backgrounds, military camp at dawn, new army formation, traditional Chinese ink wash painting, Song dynasty aesthetic, steel blue tones",
    "Ancient Chinese battle scene at a wide river, massive army on one side in chaos, smaller disciplined force charging on the other side, panic and triumph, traditional Chinese ink wash painting, Song dynasty aesthetic, dramatic composition",
]

FILES = ["xiean-xiexuan-cover", "xiean-card-1", "xiexuan-card-2", "xiean-xiexuan-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="30%" stop-color="#000" stop-opacity="0.12"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.6"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#7C3AED" letter-spacing="6" {STROKE}>东晋·淝水之战</text>
<text x="512" y="330" text-anchor="middle" font-family="{FONT}" font-size="110" font-weight="900" fill="#FFFFFF" letter-spacing="6" {STROKE}>谢安·谢玄</text>
<rect x="262" y="380" width="500" height="3" rx="1.5" fill="#7C3AED" opacity="0.7"/>
<text x="512" y="490" text-anchor="middle" font-family="{FONT}" font-size="46" font-weight="800" fill="#7C3AED" letter-spacing="6" {STROKE}>淝水定乾坤</text>
<text x="512" y="590" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>八万破百万 · 叔侄双雄 · 东山再起</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#谢安 #谢玄 #淝水之战 #东山再起 #草木皆兵 #东晋</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#7C3AED" letter-spacing="3" {STROKE}>谢安 · 东山再起的名士</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#7C3AED"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#7C3AED" {STROKE}>隐居东山</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>年轻时隐居不出，朝廷征召不理</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#7C3AED"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#7C3AED" {STROKE}>东山再起</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>40多岁才出山，位至宰相</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#7C3AED"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#7C3AED" {STROKE}>淝水捷报</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>继续下棋："小儿辈遂已破贼"</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#7C3AED" {STROKE}>中国历史上最从容的宰相</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#谢安 #东山再起 #淝水之战 #风流名士</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#059669" letter-spacing="3" {STROKE}>谢玄 · 北府兵</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#059669"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#059669" {STROKE}>谢安举荐</text>
  <text x="30" y="84" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>叔父谢安力排众议提拔他为统帅</text>
</g>

<g transform="translate(40, 310)">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#059669"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#059669" {STROKE}>招募北府兵</text>
  <text x="30" y="84" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>招募北方流民，组建精锐部队</text>
</g>

<g transform="translate(40, 470)">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#059669"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#059669" {STROKE}>八万破百万</text>
  <text x="30" y="84" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>淝水之战的实际军事指挥官</text>
</g>

<text x="512" y="760" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#059669" {STROKE}>北府兵——南北朝最强军队</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#谢玄 #北府兵 #淝水之战 #东晋</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EF4444" letter-spacing="3" {STROKE}>淝水之战 & 王谢风流</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="100" rx="12" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="100" rx="3" fill="#EF4444"/>
  <text x="30" y="38" font-family="{FONT}" font-size="24" font-weight="700" fill="#EF4444" {STROKE}>草木皆兵</text>
  <text x="30" y="72" font-family="{FONT}" font-size="20" fill="#E2E8F0" {STROKE_S}>苻坚看草木都像是晋军——出自此战</text>
</g>

<g transform="translate(40, 275)">
  <rect x="0" y="0" width="944" height="100" rx="12" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="100" rx="3" fill="#EF4444"/>
  <text x="30" y="38" font-family="{FONT}" font-size="24" font-weight="700" fill="#EF4444" {STROKE}>风声鹤唳</text>
  <text x="30" y="72" font-family="{FONT}" font-size="20" fill="#E2E8F0" {STROKE_S}>秦军溃逃时听到风声鹤叫都以为是追兵</text>
</g>

<g transform="translate(40, 400)">
  <rect x="0" y="0" width="944" height="100" rx="12" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="100" rx="3" fill="#EF4444"/>
  <text x="30" y="38" font-family="{FONT}" font-size="24" font-weight="700" fill="#EF4444" {STROKE}>前秦崩溃</text>
  <text x="30" y="72" font-family="{FONT}" font-size="20" fill="#E2E8F0" {STROKE_S}>苻坚两年后被杀，北方重新分裂</text>
</g>

<g transform="translate(40, 525)">
  <rect x="0" y="0" width="944" height="100" rx="12" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="100" rx="3" fill="#7C3AED"/>
  <text x="30" y="38" font-family="{FONT}" font-size="24" font-weight="700" fill="#7C3AED" {STROKE}>旧时王谢堂前燕</text>
  <text x="30" y="72" font-family="{FONT}" font-size="20" fill="#E2E8F0" {STROKE_S}>陈郡谢氏与琅琊王氏并列</text>
</g>

<text x="512" y="760" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#7C3AED" {STROKE}>一战诞生两个成语，挽大厦于将倾</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#淝水之战 #谢安谢玄 #草木皆兵 #风声鹤唳</text>
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
