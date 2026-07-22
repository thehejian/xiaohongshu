import subprocess, json, sys, os, time, base64, tempfile

workdir = os.path.dirname(os.path.abspath(__file__))
api_key = os.environ.get("AGNES_API_KEY", "")

def b64img(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

ref_img = b64img(f"{workdir}/01-cover.png")
models = ["agnes-image-2.0-flash", "agnes-image-2.1-flash"]

# Usage: python3 gen_batch.py [num1] [num2] ...
# e.g. python3 gen_batch.py 2 3  or  python3 gen_batch.py 4 5  or  python3 gen_batch.py 6
nums = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [2, 3]

for num in nums:
    prompt = open(f"{workdir}/prompts/{num:02d}-cover.md").read().strip()
    outfile = f"{workdir}/{num:02d}-cover.png"

    for attempt in range(10):
        model = models[attempt % 2]
        print(f"Generating {num:02d}-cover (attempt {attempt+1}, {model})...")

        payload = {
            "model": model,
            "prompt": prompt,
            "n": 1,
            "size": "720x960",
            "image": f"data:image/png;base64,{ref_img}"
        }

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            json.dump(payload, f)
            tmpfile = f.name

        r = subprocess.run([
            "curl", "-s", "--max-time", "120",
            "-H", "Content-Type: application/json",
            "-H", f"Authorization: Bearer {api_key}",
            "-d", f"@{tmpfile}",
            "-w", "\nHTTP_CODE:%{http_code}",
            "https://apihub.agnes-ai.com/v1/images/generations"
        ], capture_output=True, text=True)
        os.unlink(tmpfile)

        output = r.stdout
        lines = output.strip().split('\n')
        http_code_line = [l for l in lines if 'HTTP_CODE:' in l]
        http_code = http_code_line[-1].split(':')[-1] if http_code_line else '000'
        body = '\n'.join(lines[:-1]) if http_code_line else output

        print(f"  HTTP_CODE: {http_code}")

        # Check real content_policy_violation (not any 400)
        if 'content_policy_violation' in body.lower():
            print("  Content policy violation detected in response!")
            print(f"  Body: {body[:300]}")
            sys.exit(1)

        if http_code == '200':
            try:
                data = json.loads(body)
                url = data.get('data', [{}])[0].get('url')
                if url:
                    subprocess.run(["curl", "-s", url, "-o", outfile])
                    size = os.path.getsize(outfile)
                    print(f"  Saved {num:02d}-cover.png ({size} bytes)")
                    break
            except Exception as e:
                print(f"  Parse error: {e}")
        else:
            if body.strip():
                print(f"  Body: {body[:200]}")
            wait = 10
            print(f"  Retrying in {wait}s...")
            time.sleep(wait)
    else:
        print(f"Failed {num:02d}-cover after all attempts")
        sys.exit(1)

print(f"Done: {', '.join(f'{n:02d}' for n in nums)}")
