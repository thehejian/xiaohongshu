#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pipeline for topics 101-149: setup, gen images, Feishu upload.
Usage:
  python3 pipeline_101_149.py setup          # create dirs/articles/prompts
  python3 pipeline_101_149.py gen [s] [e]    # gen images in 3-topic batches
  python3 pipeline_101_149.py upload [s] [e] # Feishu upload
  python3 pipeline_101_149.py all            # setup + gen + upload
"""
import os, sys, subprocess, tempfile, json, time, threading, re

BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter"
GEN_SCRIPT = f"{BASE}/image-cards/war-tech/gen_one.py"
TRACK_FILE = f"{BASE}/.feishu_uploaded"

# ── Load data ──
sys.path.insert(0, BASE)
import topics_101_149_data as D

def setup_phase(start, end):
    for num in range(start, end + 1):
        if num not in D.TOPICS:
            continue
        data = D.TOPICS[num]
        folder = data["folder"]
        path = f"{BASE}/image-cards/{folder}"
        os.makedirs(path, exist_ok=True)
        os.makedirs(f"{path}/prompts", exist_ok=True)
        with open(f"{path}/article.md", "w", encoding="utf-8") as f:
            f.write(data["article"])
        for i, prompt in enumerate(data["prompts"], 1):
            with open(f"{path}/prompts/{i:02d}-cover.md", "w", encoding="utf-8") as f:
                f.write(prompt)
        gen_dst = f"{path}/gen_one.py"
        if not os.path.exists(gen_dst):
            os.symlink(GEN_SCRIPT, gen_dst)
        print(f"  Setup {num:3d}: {folder}")

def gen_topic(num):
    data = D.TOPICS[num]
    path = f"{BASE}/image-cards/{data['folder']}"
    r = subprocess.run(["python3", "gen_one.py", "1", "2", "3"],
        cwd=path, capture_output=True, text=True, timeout=900)
    sys.stdout.write(r.stdout)
    if r.returncode != 0:
        sys.stdout.write(f"  [{num}] GEN FAILED\n")
        if r.stderr:
            sys.stdout.write(f"  [{num}] stderr: {r.stderr[:200]}\n")
        return False
    return True

def gen_phase(start, end):
    nums = sorted(k for k in D.TOPICS if start <= k <= end)
    for i in range(0, len(nums), 3):
        batch = nums[i:i+3]
        threads = []
        for num in batch:
            t = threading.Thread(target=lambda n=num: gen_topic(n))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        print(f"  Batch {i//3 + 1}/{(len(nums)+2)//3} done: topics {batch}")

def feishu_create(title, content_text):
    title_escaped = title.replace("'", "\\'").replace('"', '\\"').replace("`", "\\`")
    clean = content_text.split("#")[0].strip() if "#" in content_text else content_text
    tmpf = tempfile.mktemp(suffix=".md")
    with open(tmpf, "w", encoding="utf-8") as f:
        f.write(clean)
    try:
        r = subprocess.run(["bash", "-c",
            f'export PATH="/opt/homebrew/bin:$PATH"; cat "{tmpf}" | lark-cli docs +create --title "{title_escaped}" --content - --doc-format markdown --as user --format json'
        ], capture_output=True, text=True, timeout=30)
    finally:
        if os.path.exists(tmpf):
            os.unlink(tmpf)
    if r.returncode != 0:
        return None
    try:
        data = json.loads(r.stdout)
        return data.get("data", {}).get("document", {}).get("document_id", "")
    except:
        m = re.search(r'document_id["\s:]+"([^"]+)"', r.stdout)
        return m.group(1) if m else None

def feishu_insert(folder, token, img_num):
    r = subprocess.run(["bash", "-c",
        f'export PATH="/opt/homebrew/bin:$PATH"; cd "{BASE}/image-cards/{folder}"; lark-cli docs +media-insert --doc {token} --file ./{img_num:02d}-cover.png --as user'
    ], capture_output=True, text=True, timeout=60)
    return r.returncode == 0

def upload_phase(start, end):
    for num in sorted(k for k in D.TOPICS if start <= k <= end):
        data = D.TOPICS[num]
        folder = data["folder"]
        imgs = [i for i in range(1, 4) if os.path.exists(f"{BASE}/image-cards/{folder}/{i:02d}-cover.png")]
        if len(imgs) < 3:
            print(f"  [{num}] SKIP: only {len(imgs)}/3 images")
            continue
        title = data["article"].split("\n")[0].strip()
        ftitle = f"场景{num}：{title}"
        token = feishu_create(ftitle, data["article"])
        if not token:
            print(f"  [{num}] Feishu create FAILED")
            continue
        for i in range(1, 4):
            ok = feishu_insert(folder, token, i)
            if not ok:
                print(f"  [{num}] Insert {i} FAILED")
            time.sleep(3)
        with open(TRACK_FILE, "a") as f:
            f.write(f"\n{num:03d}|{folder}|{token}")
        print(f"  [{num}] OK https://qcnh2b60jsx1.feishu.cn/docx/{token}")
        time.sleep(5)

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    s = int(sys.argv[2]) if len(sys.argv) > 2 else 101
    e = int(sys.argv[3]) if len(sys.argv) > 3 else 149
    os.environ["PATH"] = f"/opt/homebrew/bin:{os.environ.get('PATH', '')}"
    if cmd in ("all", "setup"):
        print("=== Setup phase ===")
        setup_phase(s, e)
    if cmd in ("all", "gen"):
        print("=== Gen phase ===")
        gen_phase(s, e)
    if cmd in ("all", "upload"):
        print("=== Upload phase ===")
        upload_phase(s, e)
    print("Done!")
