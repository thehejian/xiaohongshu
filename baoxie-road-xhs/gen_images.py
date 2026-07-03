#!/usr/bin/env python3
import subprocess, os, json, sys, time, base64
ROOT = os.path.dirname(os.path.abspath(__file__))
API_KEY = "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect"
API_URL = "https://apihub.agnes-ai.com/v1/images/generations"
def call_agnes(prompt, ref_b64=None, retries=3):
    payload = {"model": "agnes-image-2.1-flash", "prompt": prompt, "size": "1024x1024", "n": 1}
    if ref_b64: payload["image"] = ref_b64
    fp = os.path.join(ROOT, "tmp_payload.json")
    with open(fp, "w") as f: json.dump(payload, f)
    hdr = ["-H", "Authorization: Bearer " + API_KEY, "-H", "Content-Type: application/json"]
    for attempt in range(retries):
        try:
            r = subprocess.run(["curl", "-s", "--max-time", "300"] + hdr + ["-d", "@" + fp, API_URL], capture_output=True, text=True, timeout=300)
            resp = json.loads(r.stdout)
            if "data" in resp and len(resp["data"]) > 0:
                url = resp["data"][0]["url"]
                dl = subprocess.run(["curl", "-sL", "--max-time", "60", url, "-o", os.path.join(ROOT, "tmp_dl.png")], capture_output=True, timeout=60)
                if os.path.exists(os.path.join(ROOT, "tmp_dl.png")) and os.path.getsize(os.path.join(ROOT, "tmp_dl.png")) > 10000:
                    with open(os.path.join(ROOT, "tmp_dl.png"), "rb") as f: return base64.b64encode(f.read()).decode()
        except: pass
        if attempt < retries - 1: time.sleep(5)
    return None
PROMPTS = [
    "Ancient Chinese plank road carved into sheer cliff face along a river valley, Baoxie Road Qinling mountains, wooden walkways extending from mountainside, dramatic perspective, traditional Chinese landscape painting style, golden light, NO text",
    "Ancient Chinese stone tunnel carved through mountain rock, Stone Gate tunnel Baoxie Road, Han dynasty engineering marvel, dramatic interior lighting, traditional Chinese style, NO text",
    "Zhuge Liang ancient Chinese military commander leading troops repairing plank roads on cliff face, Three Kingdoms period, Northern Expedition, dramatic mountain setting, NO text",
    "Cao Cao ancient Chinese warlord contemplating in mountain camp, chicken rib metaphor scene, traditional Chinese military camp with banners, dramatic lighting, NO text",
    "Stone Gate stele inscription Han dynasty calligraphy masterpiece, ancient Chinese rock carving on cliff face, Baoxie Road cultural heritage, traditional Chinese aesthetic, NO text",
    "Ancient Chinese merchant caravan transporting salt and tea along plank road, Baoxie Road commercial highway, Tang dynasty traders, dramatic mountain valley, NO text",
]
if __name__ == "__main__":
    print("Generating 6 images for 褒斜道...")
    ref_b64 = call_agnes(PROMPTS[0])
    if not ref_b64: print("FAIL"); sys.exit(1)
    with open(os.path.join(ROOT, "01-cover.png"), "wb") as f: f.write(base64.b64decode(ref_b64))
    for i in range(1, 6):
        print(f"[{i+1}/6]...")
        result = call_agnes(PROMPTS[i], ref_b64=ref_b64)
        if result:
            path = os.path.join(ROOT, f"0{i+1}-card{i}.png")
            with open(path, "wb") as f: f.write(base64.b64decode(result))
            print(f"  Saved: {os.path.getsize(path)} bytes")
    print("Done!")
