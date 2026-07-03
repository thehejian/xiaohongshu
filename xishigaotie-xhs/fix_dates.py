#!/usr/bin/env python3
"""Regenerate 05-progress and 06-ending with corrected date."""
import json, os, subprocess, base64, re
from pathlib import Path

BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/xishigaotie-xhs"
api_key = ""
for m in re.findall(r'api_key:\s*(.+)', (Path.home()/".hermes"/"config.yaml").read_text()):
    m = m.strip().strip("'").strip('"')
    if m.startswith("sk-") and len(m) > 30: api_key = m; break

ref_b64 = base64.b64encode(open(f"{BASE}/01-cover.png", "rb").read()).decode()

for name in ["05-progress", "06-ending"]:
    prompt = open(f"{BASE}/prompts/{name}.md").read().strip()
    payload = {"model":"agnes-image-2.1-flash","prompt":prompt,"size":"1024x1024","n":1,"steps":25,"guidance":8.0,"image":f"data:image/png;base64,{ref_b64}"}
    with open(f"/tmp/ag_{name}.json","w") as f: json.dump(payload, f, ensure_ascii=False)
    print(f"{name}...", end=" ", flush=True)
    r = subprocess.run(["curl","-s","--max-time","300","-H",f"Authorization: Bearer {api_key}","-H","Content-Type: application/json","-d",f"@/tmp/ag_{name}.json","https://apihub.agnes-ai.com/v1/images/generations"], capture_output=True, text=True, timeout=300)
    d = json.loads(r.stdout)
    subprocess.run(["curl","-sL",d["data"][0]["url"],"-o",f"{BASE}/{name}.png"], timeout=120)
    print(f"{os.path.getsize(f'{BASE}/{name}.png')//1024}KB")

print("Done!")