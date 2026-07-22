#!/usr/bin/env python3
import json, os, sys, time, subprocess, tempfile, base64

API_KEY = os.environ.get("AGNES_API_KEY")
if not API_KEY:
    print("ERROR: AGNES_API_KEY not set")
    sys.exit(1)

API_URL = "https://apihub.agnes-ai.com/v1/images/generations"
MODEL = "agnes-image-2.1-flash"
SIZE = "1024x1024"
WORKDIR = os.path.dirname(os.path.abspath(__file__))
PROMPT_DIR = os.path.join(WORKDIR, "prompts-toutiao")
OUT_DIR = os.path.join(WORKDIR, "toutiao-images")
os.makedirs(OUT_DIR, exist_ok=True)

prompt_files = sorted(os.listdir(PROMPT_DIR))
prompts = {}
for pf in prompt_files:
    if pf.endswith(".md"):
        idx = int(pf.split("-")[0])
        with open(os.path.join(PROMPT_DIR, pf)) as f:
            prompts[idx] = f.read().strip()

def call(prompt, ref=None, timeout=300):
    payload = {"model": MODEL, "prompt": prompt, "n": 1, "size": SIZE}
    if ref:
        payload["image"] = ref
    pf = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
    json.dump(payload, pf)
    pf.close()
    for attempt in range(3):
        try:
            r = subprocess.run(['curl', '-s', '--request', 'POST', API_URL,
                '-H', f'Authorization: Bearer {API_KEY}',
                '-H', 'Content-Type: application/json',
                '-d', f'@{pf.name}',
                '--connect-timeout', '30', '--max-time', str(timeout)],
                capture_output=True, text=True, timeout=timeout)
            data = json.loads(r.stdout)
            if 'data' in data and len(data['data']) > 0 and 'url' in data['data'][0]:
                url = data['data'][0]['url']
                if url:
                    os.unlink(pf.name)
                    return url
            print(f"Attempt {attempt+1}: empty response, retrying...")
            time.sleep(3)
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(3)
    os.unlink(pf.name)
    return None

def download(url, path, timeout=120):
    r = subprocess.run(['curl', '-s', '-L', url, '-o', path, '--max-time', str(timeout)],
        capture_output=True, timeout=timeout)
    return os.path.getsize(path) > 0 if os.path.exists(path) else False

# Generate 01 (no ref)
for i in sorted(prompts.keys()):
    oname = f"{i:02d}-cover.png"
    opath = os.path.join(OUT_DIR, oname)
    if os.path.exists(opath):
        print(f"{oname} exists, skip")
        continue
    print(f"--- Generating {oname} ---")
    ref_b64 = None
    f01 = os.path.join(OUT_DIR, "01-cover.png")
    if i > 1 and os.path.exists(f01):
        with open(f01, "rb") as f:
            ref_b64 = f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"
    url = call(prompts[i], ref=ref_b64, timeout=300)
    if not url:
        print(f"FAILED: {oname}")
        continue
    ok = download(url, opath)
    if ok:
        print(f"OK: {oname} ({os.path.getsize(opath)} bytes)")
    else:
        print(f"FAILED download: {oname}")
    time.sleep(2)

print("DONE")
