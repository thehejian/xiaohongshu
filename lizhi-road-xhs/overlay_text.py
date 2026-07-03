from PIL import Image, ImageDraw, ImageFont
import os
BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/lizhi-road-xhs"
FONT = "/System/Library/Fonts/STHeiti Medium.ttc"
cards = {
    "01-cover": {"title": "荔枝道", "subtitle": "杨贵妃的快递专线"},
    "02-card1": {"title": "路线", "subtitle": "涪陵 → 达州 → 长安，1200公里"},
    "03-card2": {"title": "一骑红尘", "subtitle": "妃子笑，无人知是荔枝来"},
    "04-card3": {"title": "玄宗与贵妃", "subtitle": "奢侈的鲜果快递"},
    "05-card4": {"title": "杜牧名句", "subtitle": "一骑红尘妃子笑"},
    "06-card5": {"title": "帝国快递", "subtitle": "唐代最快驿站系统"},
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
