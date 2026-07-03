from PIL import Image, ImageDraw, ImageFont
import os
BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/sanguan-road-xhs"
FONT = "/System/Library/Fonts/STHeiti Medium.ttc"
cards = {
    "01-cover": {"title": "散关道", "subtitle": "铁马秋风大散关"},
    "02-card1": {"title": "路线", "subtitle": "宝鸡 → 大散关 → 汉中，300公里"},
    "03-card2": {"title": "岳飞抗金", "subtitle": "宋金战争最前线"},
    "04-card3": {"title": "陆游名句", "subtitle": "铁马秋风大散关"},
    "05-card4": {"title": "多重防线", "subtitle": "最坚固的关隘"},
    "06-card5": {"title": "兵家必争", "subtitle": "战国到明清"},
}
for name, info in cards.items():
    path = os.path.join(BASE, f"{name}.png")
    if not os.path.exists(path): continue
    img = Image.open(path).convert("RGBA")
    ol = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(ol)
    w, h = img.size
    draw.rectangle([0, 0, w, int(h*0.25)], fill=(0, 0, 0, 100))
    tf = ImageFont.truetype(FONT, int(w*0.108))
    bbox = draw.textbbox((0, 0), info["title"], font=tf)
    tx = (w - (bbox[2]-bbox[0])) // 2
    draw.text((tx, int(h*0.04)), info["title"], fill=(255, 255, 255), font=tf)
    sf = ImageFont.truetype(FONT, int(w*0.06))
    bbox = draw.textbbox((0, 0), info["subtitle"], font=sf)
    sx = (w - (bbox[2]-bbox[0])) // 2
    draw.text((sx, int(h*0.04)+int(w*0.108)+int(h*0.025)), info["subtitle"], fill=(200, 200, 200), font=sf)
    r = Image.alpha_composite(img, ol).convert("RGB")
    r.save(path, "PNG")
    print(f"{name} OK")
