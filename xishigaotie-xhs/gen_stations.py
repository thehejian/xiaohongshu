#!/usr/bin/env python3
"""Generate station cards with curl."""
import json, os, subprocess, sys, base64, re
from pathlib import Path

BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/xishigaotie-xhs"
config = Path.home() / ".hermes" / "config.yaml"

api_key = ""
for m in re.findall(r'api_key:\s*(.+)', config.read_text()):
    m = m.strip().strip("'").strip('"')
    if m.startswith("sk-") and len(m) > 30: api_key = m; break

ref_b64 = base64.b64encode(open(f"{BASE}/01-cover.png", "rb").read()).decode()

stations = {"xian": "11-xian", "shangluo": "12-shangluo", "manchuanguan": "13-manchuanguan", "shiyan": "14-shiyan", "wuhan": "15-wuhan"}

for name, fname in stations.items():
    prompt = open(f"{BASE}/prompts/{fname}.md").read().strip()
    payload = {
        "model": "agnes-image-2.1-flash",
        "prompt": prompt, "size": "1024x1024", "n": 1,
        "steps": 25, "guidance": 8.0,
        "image": f"data:image/png;base64,{ref_b64}",
    }
    with open(f"/tmp/ag_{name}.json", "w") as f:
        json.dump(payload, f, ensure_ascii=False)

    print(f"{name}...", end=" ", flush=True)
    r = subprocess.run(
        ["curl", "-s", "--max-time", "300",
         "-H", f"Authorization: Bearer {api_key}",
         "-H", "Content-Type: application/json",
         "-d", f"@/tmp/ag_{name}.json",
         "https://apihub.agnes-ai.com/v1/images/generations"],
        capture_output=True, text=True, timeout=300)
    try:
        data = json.loads(r.stdout)
        url = data["data"][0]["url"]
        subprocess.run(["curl", "-sL", url, "-o", f"{BASE}/{name}.png"], timeout=120)
        sz = os.path.getsize(f"{BASE}/{name}.png") // 1024
        print(f"{sz}KB")
    except Exception as e:
        print(f"FAIL: {e}")

print("Done!")
