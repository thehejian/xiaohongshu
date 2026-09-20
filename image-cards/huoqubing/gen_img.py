import subprocess, json, sys, os, time, re

workdir = os.path.dirname(os.path.abspath(__file__))

prompt = open(f"{workdir}/prompts/01-cover.md").read().strip()
models = ["agnes-image-2.0-flash", "agnes-image-2.1-flash"]

api_key = os.environ.get("AGNES_API_KEY", "")

for i in range(6):
    model = models[i % 2]
    print(f"Attempt {i+1} with {model}...")
    
    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "n": 1,
        "size": "720x960"
    })
    
    r = subprocess.run([
        "curl", "-s", "--max-time", "120",
        "-H", "Content-Type: application/json",
        "-H", f"Authorization: Bearer {api_key}",
        "-d", payload,
        "-w", "\nHTTP_CODE:%{http_code}",
        "https://apihub.agnes-ai.com/v1/images/generations"
    ], capture_output=True, text=True)
    
    output = r.stdout
    lines = output.strip().split('\n')
    http_code_line = [l for l in lines if 'HTTP_CODE:' in l]
    http_code = http_code_line[-1].split(':')[-1] if http_code_line else '000'
    body = '\n'.join(lines[:-1]) if http_code_line else output
    
    print(f"HTTP_CODE: {http_code}")
    
    if 'content_policy' in body.lower():
        print("Content policy violation - stopping")
        sys.exit(1)
    
    if http_code == '200':
        try:
            data = json.loads(body)
            url = data['data'][0]['url']
            if url:
                subprocess.run(["curl", "-s", url, "-o", f"{workdir}/01-cover.png"])
                size = os.path.getsize(f"{workdir}/01-cover.png")
                print(f"Saved 01-cover.png ({size} bytes)")
                sys.exit(0)
        except:
            pass
    
    wait = (i + 1) * 5
    print(f"Retrying in {wait}s...")
    time.sleep(wait)

print("All attempts failed")
sys.exit(1)
