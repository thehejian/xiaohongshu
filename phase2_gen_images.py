#!/usr/bin/env python3
"""Phase 2: Generate 6 images per topic using 3 Agnes tokens in parallel."""
import subprocess, json, sys, os, time, tempfile, threading, base64, re

BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter"

# ── Load env ──
for k in ["AGNES_API_KEY", "AGNES_API_KEY2", "AGNES_API_KEY3"]:
    if k not in os.environ:
        val = subprocess.run(f"source ~/.baoyu-skills/.env 2>/dev/null; echo ${k}", shell=True, capture_output=True, text=True).stdout.strip()
        if val:
            os.environ[k] = val

API_KEYS = [os.environ.get(k, "") for k in ["AGNES_API_KEY", "AGNES_API_KEY2", "AGNES_API_KEY3"]]
MODELS = ["agnes-image-2.0-flash", "agnes-image-2.1-flash"]

if not all(API_KEYS):
    print("ERROR: API keys not set")
    sys.exit(1)

# ── Parse topics ──
with open(f"{BASE}/正文提示词.md") as f:
    doc = f.read()

blocks = re.split(r'\n(?=## 主题 \d+[：:])', doc)
topics = []
for block in blocks:
    m = re.match(r'## 主题 (\d+)[：:]?\s*(.*?)\n', block)
    if not m:
        continue
    num = int(m.group(1))
    if num < 43 or num > 100:
        continue
    fm = re.search(r'\*\*文件夹\*\*:\s*\x60(.+?)\x60', block)
    folder = fm.group(1) if fm else f'topic-{num:03d}'
    topics.append((num, folder))

print(f"Loaded {len(topics)} topics for image generation")

# ── Image gen ──
def gen_image(folder, num, prompt, start_key, has_ref=True):
    """Generate one image. Returns True on success."""
    workdir = f"{BASE}/image-cards/{folder}"
    outfile = f"{workdir}/{num:02d}-cover.png"
    
    ref_b64 = None
    if has_ref:
        ref_path = f"{workdir}/01-cover.png"
        if os.path.exists(ref_path):
            with open(ref_path, "rb") as f:
                ref_b64 = base64.b64encode(f.read()).decode()

    mi = 0
    ki = start_key % len(API_KEYS)
    fails_on_current = 0
    retries_no_ref = 0

    for attempt in range(15):
        model = MODELS[mi]
        key = API_KEYS[ki]
        use_ref_now = has_ref and retries_no_ref == 0

        payload = {"model": model, "prompt": prompt, "n": 1, "size": "720x960"}
        if use_ref_now and ref_b64:
            payload["image"] = f"data:image/png;base64,{ref_b64}"

        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".json") as f:
            json.dump(payload, f)
            tmpfile = f.name

        try:
            r = subprocess.run([
                "curl", "-s", "--max-time", "120", "--insecure",
                "-H", "Content-Type: application/json",
                "-H", f"Authorization: Bearer {key}",
                "-d", f"@{tmpfile}",
                "-w", "\nHTTP_CODE:%{http_code}",
                "https://apihub.agnes-ai.com/v1/images/generations"
            ], capture_output=True, text=True, timeout=130)
        except subprocess.TimeoutExpired:
            print(f"  [{num:02d} T{ki+1}] Timeout a{attempt+1}")
            ki = (ki + 1) % len(API_KEYS)
            time.sleep(3)
            if os.path.exists(tmpfile):
                os.unlink(tmpfile)
            continue
        finally:
            if os.path.exists(tmpfile):
                os.unlink(tmpfile)

        lines = r.stdout.strip().split("\n")
        http_code = next((l.split(":")[-1].strip() for l in lines if "HTTP_CODE:" in l), "000")
        body = "\n".join(lines[:-1]) if "HTTP_CODE:" in r.stdout else r.stdout

        if "content_policy_violation" in body.lower():
            print(f"  [{num:02d} T{ki+1}] CONTENT POLICY - simplifying prompt")
            prompt = re.sub(r'题字「.*?」以书法笔意置于画面上方。', '', prompt)
            prompt = re.sub(r'人物为古代中国人形象，勿用抽象隐喻。画面留白充足，勿堆满。', '', prompt)
            prompt = re.sub(r'[，。！？、]', ' ', prompt)[:200]
            retries_no_ref = 1
            time.sleep(5)
            continue

        if http_code == "200":
            try:
                data = json.loads(body)
                url = data.get("data", [{}])[0].get("url")
                if url:
                    subprocess.run(["curl", "-s", "--max-time", "60", url, "-o", outfile], timeout=70)
                    sz = os.path.getsize(outfile)
                    if sz > 1000:
                        print(f"  [{num:02d} T{ki+1}] OK ({sz} bytes)")
                        return True
                    else:
                        print(f"  [{num:02d} T{ki+1}] Too small: {sz} bytes")
            except Exception as e:
                print(f"  [{num:02d} T{ki+1}] Parse: {e}")

        fails_on_current += 1
        if fails_on_current >= 2:
            mi = (mi + 1) % len(MODELS)
            fails_on_current = 0
        ki = (ki + 1) % len(API_KEYS)

        if use_ref_now and http_code in ("000", "503") and attempt >= 2:
            retries_no_ref = 1
            print(f"  [{num:02d} T{ki+1}] -> no ref")

        time.sleep(5)
    
    print(f"  [{num:02d}] FAILED after 15 attempts")
    return False


def process_topic(topic_num, folder):
    """Generate 6 images for one topic."""
    print(f"\n--- TOPIC {topic_num}: {folder} ---")
    workdir = f"{BASE}/image-cards/{folder}"
    
    # Check existing
    existing = [i for i in range(1, 7) if os.path.exists(f"{workdir}/{i:02d}-cover.png")]
    if len(existing) == 6:
        print(f"  All 6 images exist, skipping")
        return True

    # Read prompts
    prompts = {}
    for i in range(1, 7):
        pf = f"{workdir}/prompts/{i:02d}-cover.md"
        if os.path.exists(pf):
            with open(pf) as f:
                prompts[i] = f.read().strip()
    
    if len(prompts) < 6:
        print(f"  ERROR: Only {len(prompts)} prompt files found")
        return False

    # Batch 1: 01 (no ref), 02, 03 (ref=01)
    print(f"  Batch 1: 01 (no ref), 02, 03...")
    results = {}
    threads = []
    
    # 01: no ref
    t1 = threading.Thread(target=lambda: results.update({1: gen_image(folder, 1, prompts[1], 0, has_ref=False)}))
    t1.start()
    threads.append(t1)
    
    # 02, 03: need 01 done first or ref skip
    # Actually gen_image handles ref not found gracefully
    for img in [2, 3]:
        t = threading.Thread(target=lambda i=img: results.update({i: gen_image(folder, i, prompts[i], (i-1) % 3)}))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    if not results.get(1):
        print(f"  COVER FAILED, cannot continue")
        return False

    # Batch 2: 04, 05, 06 (ref=01)
    print(f"  Batch 2: 04, 05, 06...")
    threads = []
    for img in [4, 5, 6]:
        t = threading.Thread(target=lambda i=img: results.update({i: gen_image(folder, i, prompts[i], (i-1) % 3)}))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    success = all(results.get(i, False) for i in range(1, 7))
    # Verify files
    final = [i for i in range(1, 7) if os.path.exists(f"{workdir}/{i:02d}-cover.png")]
    print(f"  Result: {len(final)}/6 images generated")
    return len(final) == 6


# ── Main ──
if len(sys.argv) > 1:
    args = [a for a in sys.argv[1:] if a.isdigit()]
    if len(args) == 1:
        # Single topic mode
        num = int(args[0])
        folder = [f for n, f in topics if n == num]
        if folder:
            process_topic(num, folder[0])
        else:
            print(f"Topic {num} not found")
    elif len(args) == 2:
        # Range mode: start end
        start_n = int(args[0])
        end_n = int(args[1])
        for num, folder in topics:
            if num < start_n or num > end_n:
                continue
            success = process_topic(num, folder)
            if not success:
                print(f"  TOPIC {num} IMAGES FAILED, continuing anyway")
            time.sleep(5)
    else:
        print("Usage: phase2_gen_images.py [start] [end]")
else:
    # Batch mode - process all
    for num, folder in topics:
        success = process_topic(num, folder)
        if not success:
            print(f"  TOPIC {num} IMAGES FAILED, continuing anyway")
        time.sleep(5)

print("\n=== ALL DONE ===")
