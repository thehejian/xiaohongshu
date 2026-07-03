#!/usr/bin/env python3
import json, subprocess, base64, re, os
from pathlib import Path

BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/germany-out-xhs"

api_key = ""
config_path = Path.home() / ".hermes" / "config.yaml"
if config_path.exists():
    for m in re.findall(r'api_key:\s*(.+)', config_path.read_text()):
        m = m.strip().strip("'").strip('"')
        if m.startswith('sk-') and len(m) > 30:
            api_key = m
            break

if not api_key:
    print("FAIL: No Agnes API key found")
    exit(1)

def generate(prompt, output_path, ref_b64=None):
    payload = {
        "model": "agnes-image-2.1-flash",
        "prompt": prompt,
        "size": "1024x1024",
        "n": 1,
        "steps": 25,
        "guidance": 8.0,
    }
    if ref_b64:
        payload["image"] = "data:image/png;base64," + ref_b64

    tmpfile = f"/tmp/germany_{Path(output_path).stem}.json"
    with open(tmpfile, "w") as f:
        json.dump(payload, f)

    r = subprocess.run(
        ["curl", "-s", "--max-time", "300",
         "-H", f"Authorization: Bearer {api_key}",
         "-H", "Content-Type: application/json",
         "-d", f"@{tmpfile}",
         "https://apihub.agnes-ai.com/v1/images/generations"],
        capture_output=True, text=True, timeout=300
    )

    d = json.loads(r.stdout)
    if 'data' in d:
        subprocess.run(["curl", "-sL", d['data'][0]['url'], "-o", output_path], timeout=120)
        size_kb = os.path.getsize(output_path) // 1024
        print(f"{Path(output_path).name} OK {size_kb} KB")
        return True
    else:
        print(f"{Path(output_path).name} FAIL: {r.stdout[:300]}")
        return False

os.makedirs(BASE, exist_ok=True)

# Step 1: Generate cover (image 1) — no ref
print("=== Generating cover (image 1) ===")
prompts_dir = Path(BASE) / "prompts"
cover_prompt = (prompts_dir / "01-cover.md").read_text().strip()
cover_path = os.path.join(BASE, "01-cover.png")
if generate(cover_prompt, cover_path):
    ref_b64 = base64.b64encode(open(cover_path, "rb").read()).decode()

    # Step 2: Generate images 2–6 using cover as reference
    for name, prompt_file in [
        ("02-enciso", "02-enciso.md"),
        ("03-havertz", "03-havertz.md"),
        ("04-penalty", "04-penalty.md"),
        ("05-decline", "05-decline.md"),
        ("06-ending", "06-ending.md"),
    ]:
        prompt = (prompts_dir / prompt_file).read_text().strip()
        out_path = os.path.join(BASE, f"{name}.png")
        print(f"=== Generating {name} ===")
        generate(prompt, out_path, ref_b64)
else:
    print("FAIL: Cover generation failed, aborting")

print("\nDone!")
