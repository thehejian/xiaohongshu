#!/usr/bin/env python3
"""Generate 4 cards for 鸠摩罗什."""
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
    "Ancient Buddhist monk with a golden halo, serene and wise, sitting in meditation, surrounded by sacred Buddhist texts, traditional Chinese ink wash painting, Tang dynasty aesthetic, gold and red palette, divine atmosphere",
    "Ancient Central Asian kingdom of Kucha, a young prodigy monk in a grand Buddhist monastery,丝绸之路 oasis, traditional Chinese ink wash painting, Tang dynasty aesthetic, warm golden and green tones",
    "Ancient Chinese scene of a Buddhist monk being escorted by soldiers across desert landscapes, a captive scholar crossing the Gobi, traditional Chinese ink wash painting, Tang dynasty aesthetic, brown and gray tones, dramatic journey",
    "Ancient Chinese translation hall in Chang'an, an elderly Buddhist monk surrounded by Chinese scholars translating Sanskrit scrolls into Chinese, a grand scriptorium, traditional Chinese ink wash painting, Tang dynasty aesthetic, gold and warm brown tones, scholarly",
]

FILES = ["jiumoluoshi-cover", "jiumoluoshi-card-1", "jiumoluoshi-card-2", "jiumoluoshi-card-3"]

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
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="28" font-weight="700" fill="#EAB308" letter-spacing="6" {STROKE}>十六国·译经大师</text>
<text x="512" y="360" text-anchor="middle" font-family="{FONT}" font-size="120" font-weight="900" fill="#FFFFFF" letter-spacing="8" {STROKE}>鸠摩罗什</text>
<rect x="262" y="405" width="500" height="3" rx="1.5" fill="#EAB308" opacity="0.6"/>
<text x="512" y="510" text-anchor="middle" font-family="{FONT}" font-size="42" font-weight="800" fill="#EAB308" letter-spacing="6" {STROKE}>战火走来的译经大师</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="24" fill="#E2E8F0" {STROKE_S}>龟兹神童 · 苻坚发兵 · 译经三百卷</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#鸠摩罗什 #译经 #佛经 #金刚经 #法华经 #苻坚</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EAB308" letter-spacing="3" {STROKE}>龟兹神童</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>出身西域</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>生于龟兹（今新疆库车），父印度贵族，母公主</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>七岁出家</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>日诵千偈，少年名震西域</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>声名远播</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>名声传到中原——苻坚不惜为他发兵西域</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>一个僧人的名声，值得一场战争</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#鸠摩罗什 #龟兹 #西域 #佛教 #苻坚</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EAB308" letter-spacing="3" {STROKE}>苻坚西征</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>382年吕光西征</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>苻坚派大将吕光攻龟兹——目的之一：抢人</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>被扣凉州十七年</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>吕光在凉州自立，鸠摩罗什被扣留无法离开</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>半生蹉跎</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>从壮年到暮年，最好的年华被虚掷在凉州</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>一场战争改变了他的一生</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#鸠摩罗什 #苻坚 #吕光 #凉州 #西域</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EAB308" letter-spacing="3" {STROKE}>长安译场</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>401年入长安</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>后秦姚兴迎入长安——此时已年近六十</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>译经三百卷</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>《金刚经》《法华经》《心经》……皆为经典译本</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>不坏之舌</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>圆寂前说：译经无误，火化后舌头不坏——果然</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>今天中国人念的佛经，多半出自他手</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#鸠摩罗什 #译经 #金刚经 #法华经 #中国佛教</text>
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
