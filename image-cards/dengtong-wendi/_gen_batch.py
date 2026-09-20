import json, urllib.request, ssl, base64, os, sys, subprocess, time

workdir = os.path.dirname(os.path.abspath(__file__))
api_key = os.environ.get('AGNES_API_KEY', '')

with open(os.path.join(workdir, '01-cover.png'), 'rb') as f:
    b64 = base64.b64encode(f.read()).decode()

ctx = ssl._create_unverified_context()

def gen_one(num, use_ref=True):
    prompt_file = os.path.join(workdir, 'prompts', f'{num}-cover-en.md')
    with open(prompt_file) as f:
        prompt = f.read().strip()
    
    out_path = os.path.join(workdir, f'{num}-cover.png')
    print(f'=== Generating {num}-cover.png ===')
    
    payload = {
        'model': 'agnes-image-2.1-flash',
        'prompt': prompt,
        'n': 1,
        'size': '720x960'
    }
    if use_ref:
        payload['image'] = b64
    
    # Write payload to temp file to avoid "argument list too long"
    payload_str = json.dumps(payload)
    tmpfile = os.path.join(workdir, f'_payload_{num}.json')
    with open(tmpfile, 'w') as f:
        f.write(payload_str)
    
    r = subprocess.run(['curl', '-s', '--connect-timeout', '30', '--max-time', '120',
        '-H', f'Authorization: Bearer {api_key}',
        '-H', 'Content-Type: application/json',
        '-d', f'@{tmpfile}',
        'https://apihub.agnes-ai.com/v1/images/generations'],
        capture_output=True, text=True)
    
    try:
        data = json.loads(r.stdout)
        url = data['data'][0]['url']
        print(f'  URL: {url}')
        urllib.request.urlretrieve(url, out_path)
        sz = os.path.getsize(out_path)
        print(f'  DONE {num}-cover.png ({sz} bytes)')
        os.remove(tmpfile)
        return True
    except Exception as e:
        print(f'  FAIL: {e}')
        print(f'  STDERR: {r.stderr[:200]}')
        os.remove(tmpfile)
        return False

args = sys.argv[1:]
if not args:
    print('Usage: python3 _gen_batch.py <num1> [num2 ...]')
    sys.exit(1)

for num in args:
    ok = gen_one(num)
    if not ok:
        sys.exit(1)
    time.sleep(3)
