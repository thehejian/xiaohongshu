#!/usr/bin/env python3
"""Generate 6 Agnes images for 子午道 + Pillow overlay Chinese text."""
import subprocess, os, json, sys, time, base64

ROOT = os.path.dirname(os.path.abspath(__file__))
API_KEY = os.environ.get("AGNES_API_KEY", "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
API_URL = "https://apihub.agnes-ai.com/v1/images/generations"

def call_agnes(prompt, size="1024x1024", ref_b64=None, retries=3):
    payload = {
        "model": "agnes-image-2.1-flash",
        "prompt": prompt,
        "size": size,
        "n": 1
    }
    if ref_b64:
        payload["image"] = ref_b64
    fp = os.path.join(ROOT, "tmp_payload.json")
    with open(fp, "w") as f:
        json.dump(payload, f)
    hdr = ["-H", "Authorization: Bearer " + API_KEY, "-H", "Content-Type: application/json"]
    for attempt in range(retries):
        try:
            r = subprocess.run(
                ["curl", "-s", "--max-time", "300"] + hdr + ["-d", "@" + fp, API_URL],
                capture_output=True, text=True, timeout=300
            )
            resp = json.loads(r.stdout)
            if "data" in resp and len(resp["data"]) > 0:
                url = resp["data"][0]["url"]
                dl = subprocess.run(
                    ["curl", "-sL", "--max-time", "60", url, "-o", os.path.join(ROOT, "tmp_download.png")],
                    capture_output=True, timeout=60
                )
                if os.path.exists(os.path.join(ROOT, "tmp_download.png")):
                    sz = os.path.getsize(os.path.join(ROOT, "tmp_download.png"))
                    if sz > 10000:
                        with open(os.path.join(ROOT, "tmp_download.png"), "rb") as f:
                            return base64.b64encode(f.read()).decode()
            print(f"  API response: {json.dumps(resp)[:200]}")
        except Exception as e:
            print(f"  Attempt {attempt+1} failed: {e}")
        if attempt < retries - 1:
            time.sleep(5)
    return None

def overlay_text(png_path, title, subtitle, tag_line=None):
    """Overlay Chinese text on generated image using Pillow."""
    script_dir = os.path.dirname(os.path.abspath(png_path))
    cmd = [
        "python3", "-c",
        f"""
import sys
from PIL import Image, ImageDraw, ImageFont
img = Image.open("{png_path}").convert("RGBA")
W, H = img.size
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)
font_title = ImageFont.truetype("/System/Library/Fonts/STHeiti Medium.ttc", 52)
font_sub = ImageFont.truetype("/System/Library/Fonts/STHeiti Medium.ttc", 30)
# Semi-transparent dark bar at bottom
bar = Image.new("RGBA", (W, 180), (0, 0, 0, 140))
img = Image.alpha_composite(img, bar)
draw = ImageDraw.Draw(img)
# Title centered
tw, th = draw.textbbox((0, 0), "{title}", font=font_title)[2:4]
tw2 = tw - 0
draw.text(((W - tw2) // 2, H - 160), "{title}", font=font_title, fill=(255, 255, 255))
# Subtitle
sw, sh = draw.textbbox((0, 0), "{subtitle}", font=font_sub)[2:4]
draw.text(((W - sw) // 2, H - 115), "{subtitle}", font=font_sub, fill=(230, 230, 230))
img.save("{png_path}")
"""
    ]
    subprocess.run(cmd, shell=False)

PROMPTS = [
    # 01 Cover - Epic Qinling mountain pass aerial view
    "Aerial dramatic view of ancient Chinese Qinling mountain pass road carved into steep cliffs, misty mountains, traditional Chinese landscape painting style, epic scale, golden hour lighting, NO text",
    
    # 02 Route map style - North to south path
    "Ancient Chinese map illustration showing a mountain trail route from Xi'an south through Qinling mountains to Hanzhong, topographic style with elevation contours, sepia tones, NO text",
    
    # 03 Three Kingdoms scene - military expedition
    "Ancient Chinese military expedition crossing a treacherous mountain pass in Qinling, Three Kingdoms period soldiers with supplies navigating steep cliff paths, dramatic lighting, cinematic composition, NO text",
    
    # 04 Steep mountain terrain - dangerous path
    "Extreme steep mountain trail carved into sheer cliff face in ancient China, narrow path with wooden planks, deep valley below, dramatic perspective looking down, photorealistic, NO text",
    
    # 05 Snow-covered mountain pass
    "Snow-covered ancient mountain pass in Qinling mountains, winter scene with heavy snow, narrow trail barely visible, dramatic cold atmosphere, photorealistic, NO text",
    
    # 06 Tang dynasty emperor fleeing
    "Tang dynasty imperial procession fleeing through snowy mountain pass, Emperor Xuanzong escaping to Sichuan during rebellion, dramatic emergency escape scene, traditional Chinese clothing, cinematic, NO text",
]

TAG_LINES = [
    None,  # cover has no tag line
    "北口：西安子午峪 → 南口：石泉县",
    "全长约250公里，直穿秦岭",
    "诸葛亮北伐 · 钟会灭蜀 · 唐代皇帝逃难",
    "海拔落差超1500米，最险古道",
    "夏天山顶也可能下雪",
]

SUBTITLES = [
    None,
    "最短的秦岭古道",
    "不绕弯的直穿路线",
    "命悬一线的奇兵之道",
    "秦岭核心区的险峻",
    "唐玄宗逃难走过的路",
]

TITLES = [
    "子午道",
    "路线",
    "最短最直",
    "三国名场面",
    "地形极险",
    "紧急专用",
]

if __name__ == "__main__":
    print("Generating 6 images for 子午道...")
    
    # Generate cover first (no ref)
    print("\n[1/6] Generating cover...")
    ref_b64 = call_agnes(PROMPTS[0])
    if ref_b64:
        cover_path = os.path.join(ROOT, "01-cover.png")
        with open(cover_path, "wb") as f:
            f.write(base64.b64decode(ref_b64))
        print(f"  Cover saved: {os.path.getsize(cover_path)} bytes")
    else:
        print("  FAILED to generate cover")
        sys.exit(1)
    
    # Generate remaining 5 with cover as ref
    for i in range(1, 6):
        print(f"\n[{i+1}/6] Generating card {i}...")
        ref_with_cover = ref_b64  # use cover as style anchor
        result = call_agnes(PROMPTS[i], ref_b64=ref_with_cover)
        if result:
            card_path = os.path.join(ROOT, f"0{i+1}-card{i}.png")
            with open(card_path, "wb") as f:
                f.write(base64.b64decode(result))
            print(f"  Saved: {os.path.getsize(card_path)} bytes")
            
            # Overlay text
            title = TITLES[i]
            subtitle = SUBTITLES[i]
            if subtitle:
                overlay_text(card_path, title, subtitle)
                print(f"  Text overlaid: '{title}' + '{subtitle}'")
        else:
            print(f"  FAILED to generate card {i}")
    
    print("\nDone!")
