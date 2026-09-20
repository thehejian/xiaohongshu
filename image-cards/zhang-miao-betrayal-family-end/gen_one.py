import subprocess, json, sys, os, time, tempfile, threading, base64

os.chdir(os.path.dirname(os.path.abspath(__file__)))
api_keys = [
    os.environ.get("AGNES_API_KEY", ""),
    os.environ.get("AGNES_API_KEY2", ""),
    os.environ.get("AGNES_API_KEY3", "")
]
models = ["agnes-image-2.1-flash", "agnes-image-2.0-flash"]

nums = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [1]
has_ref = nums[0] > 1
ref_b64 = None

if has_ref:
    with open("01-cover.png", "rb") as f:
        ref_b64 = base64.b64encode(f.read()).decode()

lock = threading.Lock()
errors = []

def gen_one(num, start_key):
    prompt = open(f"prompts/{num:02d}-cover.md").read().strip()
    outfile = f"{num:02d}-cover.png"

    mi = 0
    ki = start_key
    fails_on_current = 0
    retries_without_ref = 0

    for attempt in range(20):
        model = models[mi]
        key = api_keys[ki]
        use_ref = has_ref and retries_without_ref == 0

        with lock:
            print(f"Generating {num:02d} (attempt {attempt+1}, {model}, key#{ki+1}, ref={use_ref})...")

        payload = {"model": model, "prompt": prompt, "n": 1, "size": "720x960"}
        if use_ref:
            payload["image"] = f"data:image/png;base64,{ref_b64}"

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
            errors.append(num)
            return

        if http_code == "200":
            try:
                url = json.loads(body)["data"][0].get("url")
                if url:
                    subprocess.run(["curl", "-s", url, "-o", outfile])
                    sz = os.path.getsize(outfile)
                    with lock:
                        print(f"  [{num:02d}] Saved {outfile} ({sz} bytes)")
                    return
            except Exception as e:
                with lock:
                    print(f"  [{num:02d}] Parse: {e}")

        fails_on_current += 1
        if fails_on_current >= 2:
            mi = (mi + 1) % len(models)
            fails_on_current = 0
            with lock:
                print(f"  [{num:02d}] -> Switching to {models[mi]}")
        ki = (ki + 1) % len(api_keys)

        if use_ref and http_code in ("000", "503") and attempt >= 3:
            retries_without_ref = 1
            with lock:
                print(f"  [{num:02d}] -> Ref seems stuck, retrying without ref")

        if body.strip():
            with lock:
                print(f"  [{num:02d}] Body: {body[:150]}")
        time.sleep(5)
    else:
        with lock:
            print(f"  [{num:02d}] Failed after 20 attempts")
        errors.append(num)

threads = []
for i, num in enumerate(nums):
    t = threading.Thread(target=gen_one, args=(num, i % 3))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

if errors:
    print(f"Errors on images: {errors}")
    sys.exit(1)
print("Done")
