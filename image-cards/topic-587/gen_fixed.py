import subprocess, json, sys, os, time, tempfile, threading

os.chdir(os.path.dirname(os.path.abspath(__file__)))
api_keys = [
    os.environ.get("AGNES_API_KEY", ""),
    os.environ.get("AGNES_API_KEY2", ""),
    os.environ.get("AGNES_API_KEY3", "")
]
MODEL = "agnes-image-2.1-flash"  # 固定单一模型，风格统一

lock = threading.Lock()

def gen_one(num, key_idx):
    prompt = open(f"prompts/{num:02d}-cover.md").read().strip()
    outfile = f"{num:02d}-cover.png"
    key = api_keys[key_idx]

    for attempt in range(20):
        with lock:
            print(f"Generating {num:02d} (attempt {attempt+1}, {MODEL}, key#{key_idx+1})...")

        payload = {"model": MODEL, "prompt": prompt, "n": 1, "size": "720x960"}
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".json") as f:
            json.dump(payload, f)
            tmpfile = f.name

        r = subprocess.run([
            "curl", "-s", "--max-time", "120",
            "-H", "Content-Type: application/json",
            "-H", f"Authorization: Bearer {key}",
            "-d", f"@{tmpfile}",
            "-w", "\nHTTP_CODE:%{http_code}",
            "https://apihub.agnes-ai.com/v1/images/generations"
        ], capture_output=True, text=True)
        os.unlink(tmpfile)

        lines = r.stdout.strip().split("\n")
        http_code = next((l.split(":")[-1] for l in lines if "HTTP_CODE:" in l), "000")
        body = "\n".join(lines[:-1]) if "HTTP_CODE:" in r.stdout else r.stdout

        with lock:
            print(f"  [{num:02d}] HTTP_CODE: {http_code}")

        if "content_policy_violation" in body.lower():
            with lock:
                print(f"  [{num:02d}] Content policy! {body[:200]}")
            return False

        if http_code == "200":
            try:
                url = json.loads(body)["data"][0].get("url")
                if url:
                    subprocess.run(["curl", "-s", url, "-o", outfile])
                    sz = os.path.getsize(outfile)
                    with lock:
                        print(f"  [{num:02d}] Saved {outfile} ({sz} bytes)")
                    return True
            except Exception as e:
                with lock:
                    print(f"  [{num:02d}] Parse error: {e}")

        # 只换key重试，绝不换模型
        if http_code in ("503", "000", "429"):
            time.sleep(3)
        key_idx = (key_idx + 1) % 3

    with lock:
        print(f"  [{num:02d}] Failed after 20 attempts")
    return False

results = {}
threads = []
for i, num in enumerate([1, 2, 3]):
    t = threading.Thread(target=lambda n=num, k=i: results.update({n: gen_one(n, k)}), daemon=True)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

for num, ok in sorted(results.items()):
    if not ok:
        print(f"ERROR: {num:02d} failed")
        sys.exit(1)
print("Done")
