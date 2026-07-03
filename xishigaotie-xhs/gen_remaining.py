#!/usr/bin/env python3
"""Generate remaining cards via curl to bypass SSL issues."""
import json, os, subprocess, sys, base64
from pathlib import Path

BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/xishigaotie-xhs"

# Get API key
config = Path.home() / ".hermes" / "config.yaml"
content = config.read_text()
import re
api_key = ""
for m in re.findall(r'api_key:\s*(.+)', content):
    m = m.strip().strip("'").strip('"')
    if m.startswith("sk-") and len(m) > 30:
        api_key = m
        break

ref_img_path = f"{BASE}/01-cover.png"
ref_b64 = base64.b64encode(open(ref_img_path, "rb").read()).decode()

cards = [
    ("04-stations", "prompts/04-stations.md"),
    ("05-progress", "prompts/05-progress.md"),
    ("06-ending", "prompts/06-ending.md"),
]

for name, prompt_path in cards:
    prompt = open(f"{BASE}/{prompt_path}").read().strip()
    payload = {
        "model": "agnes-image-2.1-flash",
        "prompt": prompt,
        "size": "1024x1024",
        "n": 1,
        "steps": 25,
        "guidance": 8.0,
        "image": f"data:image/png;base64,{ref_b64}",
    }
    tmp = f"/tmp/agnes_{name}.json"
    with open(tmp, "w") as f:
        json.dump(payload, f, ensure_ascii=False)

    print(f"Generating {name}...")
    result = subprocess.run(
        ["curl", "-s", "--max-time", "300",
         "-H", f"Authorization: Bearer {api_key}",
         "-H", "Content-Type: application/json",
         "-d", f"@{tmp}",
         "https://apihub.agnes-ai.com/v1/images/generations"],
        capture_output=True, text=True, timeout=300
    )
    try:
        data = json.loads(result.stdout)
        if "data" in data and len(data["data"]) > 0:
            url = data["data"][0]["url"]
            print(f"  Downloading {url[:60]}...")
            subprocess.run(["curl", "-sL", url, "-o", f"{BASE}/{name}.png"], timeout=120)
            size = os.path.getsize(f"{BASE}/{name}.png")
            print(f"  Saved: {name}.png ({size//1024}KB)")
        else:
            print(f"  Error: {json.dumps(data, indent=2)[:300]}")
    except json.JSONDecodeError:
        print(f"  JSON parse failed: {result.stdout[:200]}")

print("\nDone!")