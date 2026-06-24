#!/usr/bin/env python3
"""Generate 4 cards for 大野渊和普六茹坚."""
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
    "Two ancient Chinese founding emperors side by side, one labeled with a funny name, a playful and humorous depiction of Sui and Tang dynasty founders with name plaques, traditional Chinese ink wash painting, Tang dynasty aesthetic, gold and vermilion palette, whimsical",
    "Ancient Chinese court scene, a Northern Zhou nobleman granting names to generals, a ceremony of bestowing Xianbei surnames, traditional Chinese ink wash painting, Tang dynasty aesthetic, warm gold and brown tones, ceremonial atmosphere",
    "Ancient Chinese imaginary scene, a Tang dynasty prince named Daye Shimin riding a horse, a hilarious anachronistic hypothetical, traditional Chinese ink wash painting, playful style, blue and gold tones, humorous",
    "Two imperial seals showing name changes, old Xianbei names being replaced with Han Chinese names, the restoration of original surnames, traditional Chinese ink wash painting, Tang dynasty aesthetic, warm gold and red tones, triumphant",
]

FILES = ["daye-cover", "daye-card-1", "daye-card-2", "daye-card-3"]

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
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#EAB308" letter-spacing="4" {STROKE}>南北朝冷知识</text>
<text x="512" y="320" text-anchor="middle" font-family="{FONT}" font-size="90" font-weight="900" fill="#FFFFFF" letter-spacing="6" {STROKE}>大野渊</text>
<text x="512" y="430" text-anchor="middle" font-family="{FONT}" font-size="50" font-weight="700" fill="#DC2626" letter-spacing="4" {STROKE}>VS</text>
<text x="512" y="530" text-anchor="middle" font-family="{FONT}" font-size="90" font-weight="900" fill="#FFFFFF" letter-spacing="6" {STROKE}>普六茹坚</text>
<rect x="262" y="560" width="500" height="3" rx="1.5" fill="#EAB308" opacity="0.6"/>
<text x="512" y="650" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="800" fill="#EAB308" letter-spacing="6" {STROKE}>开国皇帝黑历史</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#大野渊 #普六茹坚 #隋文帝 #唐高祖 #宇文泰 #鲜卑姓氏</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="800" fill="#EAB308" letter-spacing="3" {STROKE}>宇文泰的赐姓运动</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>拉拢汉人将领</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>大量赐予鲜卑姓——入籍荣誉</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>杨忠 → 普六茹氏</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>杨坚的曾用名：普六茹坚</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>李虎 → 大野氏</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>李渊的曾用名：大野渊</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>隋唐开国皇帝都有鲜卑曾用名</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#宇文泰 #关陇集团 #鲜卑 #赐姓 #大野 #普六茹</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="800" fill="#DC2626" letter-spacing="3" {STROKE}>如果没改回来……</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#DC2626"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>大野世民</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>"大野世民发动玄武门之变"</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#DC2626"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>普六茹广</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>"普六茹广征讨高句丽"</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#DC2626"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>大野唐</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>大野唐 vs 普六茹隋，感觉像部落内战</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>历史岔路口，差点就有大野世民</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#大野世民 #历史脑洞 #唐朝 #隋朝 #突厥</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="800" fill="#16A34A" letter-spacing="3" {STROKE}>改回来了</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#16A34A"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>普六茹坚 → 杨坚</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>581年登基第一件事：恢复汉姓杨</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#16A34A"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>大野渊 → 李渊</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>617年起兵当天扔掉大野，变回李</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#16A34A"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>全国改回汉姓</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>普六茹、大野这些鲜卑姓从此消失</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#16A34A" {STROKE}>历史正常了，但少了很多乐子</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#大野渊 #普六茹坚 #隋文帝 #唐高祖 #历史冷知识</text>
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
