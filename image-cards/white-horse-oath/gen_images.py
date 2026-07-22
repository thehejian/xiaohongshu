import json
import base64
import os
import sys
import time
import subprocess
import tempfile

API_KEY = os.environ.get("AGNES_API_KEY")
if not API_KEY:
    print("ERROR: AGNES_API_KEY not set")
    sys.exit(1)

API_URL = "https://apihub.agnes-ai.com/v1/images/generations"
MODEL = "agnes-image-2.1-flash"
SIZE = "720x960"
WORKDIR = os.path.dirname(os.path.abspath(__file__))

def b64_file(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def call_agnes(prompt, ref_b64=None, timeout=600):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "n": 1,
        "size": SIZE
    }
    if ref_b64:
        payload["image"] = f"data:image/png;base64,{ref_b64}"

    pf = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
    json.dump(payload, pf)
    pf.close()

    try:
        r = subprocess.run([
            'curl', '-s', '--request', 'POST', API_URL,
            '-H', f'Authorization: Bearer {API_KEY}',
            '-H', 'Content-Type: application/json',
            '-d', f'@{pf.name}',
            '--connect-timeout', '60', '--max-time', str(timeout)
        ], capture_output=True, text=True, timeout=timeout)
        os.unlink(pf.name)
        data = json.loads(r.stdout)
        url = data['data'][0]['url']
        if not url:
            return "CONTENT_POLICY_VIOLATION"
        return url
    except Exception as e:
        print(f"curl failed: {e}")
        return None

def download_image(url, path, timeout=600):
    try:
        subprocess.run(['curl', '-s', '-L', url, '-o', path, '--max-time', str(timeout)], check=True, timeout=timeout)
        return os.path.getsize(path) > 0
    except Exception as e:
        print(f"curl download error: {e}")
        return False

# Read prompts
prompts = {}
TOTAL = 9
for i in range(1, TOTAL + 1):
    fname = f"prompts/{i:02d}-cover.md"
    fpath = os.path.join(WORKDIR, fname)
    if os.path.exists(fpath):
        with open(fpath) as f:
            prompts[i] = f.read().strip()
    else:
        print(f"Missing: {fname}")
        sys.exit(1)

# Step 1: Generate 01 (no ref) if missing
f01 = os.path.join(WORKDIR, "01-cover.png")
if not os.path.exists(f01):
    print("=" * 50)
    print(f"Generating 01-cover.png (no ref)...")
    url = call_agnes(prompts[1])
    if url is None or url == "CONTENT_POLICY_VIOLATION":
        print(f"FAILED: 01-cover.png")
        sys.exit(1)
    ok = download_image(url, f01)
    if not ok:
        print("FAILED: download 01-cover.png")
        sys.exit(1)
    print(f"OK: 01-cover.png ({os.path.getsize(f01)} bytes)")
    print()
else:
    print(f"01-cover.png already exists, skipping")

# Step 2: Generate 02-09 with ref
ref_b64 = b64_file(f01)
for i in range(2, TOTAL + 1):
    fname = f"{i:02d}-cover.png"
    fpath = os.path.join(WORKDIR, fname)
    if os.path.exists(fpath):
        print(f"{fname} already exists, skipping")
        continue
    print("=" * 50)
    print(f"Generating {fname} (with ref)...")
    url = call_agnes(prompts[i], ref_b64=ref_b64)
    if url is None:
        print(f"FAILED: {fname}")
        sys.exit(1)
    if url == "CONTENT_POLICY_VIOLATION":
        print(f"FAILED: content policy violation for {fname}")
        sys.exit(1)
    ok = download_image(url, fpath)
    if not ok:
        print(f"FAILED: download {fname}")
        sys.exit(1)
    print(f"OK: {fname} ({os.path.getsize(fpath)} bytes)")
    print()
    time.sleep(1)

print("=" * 50)
print("ALL DONE!")
