#!/usr/bin/env python3
"""Generate 6 Agnes images for 傥骆道 + overlay text."""
import subprocess, os, json, sys, time, base64

ROOT = os.path.dirname(os.path.abspath(__file__))
API_KEY = "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect"
API_URL = "https://apihub.agnes-ai.com/v1/images/generations"

def call_agnes(prompt, ref_b64=None, retries=3):
    payload = {"model": "agnes-image-2.1-flash", "prompt": prompt, "size": "1024x1024", "n": 1}
    if ref_b64:
        payload["image"] = ref_b64
    fp = os.path.join(ROOT, "tmp_payload.json")
    with open(fp, "w") as f:
        json.dump(payload, f)
    hdr = ["-H", "Authorization: Bearer " + API_KEY, "-H", "Content-Type: application/json"]
    for attempt in range(retries):
        try:
            r = subprocess.run(["curl", "-s", "--max-time", "300"] + hdr + ["-d", "@" + fp, API_URL], capture_output=True, text=True, timeout=300)
            resp = json.loads(r.stdout)
            if "data" in resp and len(resp["data"]) > 0:
                url = resp["data"][0]["url"]
                dl = subprocess.run(["curl", "-sL", "--max-time", "60", url, "-o", os.path.join(ROOT, "tmp_dl.png")], capture_output=True, timeout=60)
                if os.path.exists(os.path.join(ROOT, "tmp_dl.png")) and os.path.getsize(os.path.join(ROOT, "tmp_dl.png")) > 10000:
                    with open(os.path.join(ROOT, "tmp_dl.png"), "rb") as f:
                        return base64.b64encode(f.read()).decode()
        except Exception as e:
            print(f"  Attempt {attempt+1} failed: {e}")
        if attempt < retries - 1:
            time.sleep(5)
    return None

PROMPTS = [
    "Aerial dramatic view of ancient Chinese mountain pass road cutting through the center of Qinling mountains, highest elevation pass in the range, snow-capped peaks, misty valleys, traditional Chinese landscape painting style, epic scale, golden hour, NO text",
    "Ancient Chinese imperial postal relay station in a high mountain valley, Tang dynasty architecture, snow-covered surroundings, mountain pass at over 2000 meters elevation, traditional Chinese painting style, NO text",
    "Tang dynasty emperor fleeing through treacherous mountain pass in heavy snow, imperial procession emergency escape, dramatic cold atmosphere, traditional Chinese imperial robes, cinematic composition, NO text",
    "Extreme high altitude mountain pass in ancient China, snow and ice year-round, narrow trail on steep cliff, dramatic windswept scene, photorealistic, NO text",
    "Ancient Chinese mountain road with stone-paved sections winding through deep valley, Tang dynasty postal stations visible along the route, lush green mountains, traditional Chinese landscape, NO text",
    "Dramatic mountain landscape showing the highest Qinling pass with snow and clouds, treacherous narrow path carved into mountainside, ancient Chinese setting, cinematic lighting, NO text",
]

TITLES = ["傥骆道", "路线", "海拔最高", "唐代皇帝逃难", "终年积雪", "紧急专用"]
SUBTITLES = ["长安到汉中最快的命悬一线", "北起周至 → 南到洋县", "骆谷口超2000米", "玄宗德宗僖宗三次走此道", "即使夏天山顶也积雪", "唐代17个驿站的皇家专线"]

if __name__ == "__main__":
    print("Generating 6 images for 傥骆道...")
    ref_b64 = call_agnes(PROMPTS[0])
    if not ref_b64:
        print("FAILED to generate cover"); sys.exit(1)
    with open(os.path.join(ROOT, "01-cover.png"), "wb") as f:
        f.write(base64.b64decode(ref_b64))
    for i in range(1, 6):
        print(f"[{i+1}/6] Generating...")
        result = call_agnes(PROMPTS[i], ref_b64=ref_b64)
        if result:
            path = os.path.join(ROOT, f"0{i+1}-card{i}.png")
            with open(path, "wb") as f:
                f.write(base64.b64decode(result))
            print(f"  Saved: {os.path.getsize(path)} bytes")
    print("Done! Run overlay_text.py to add text.")
