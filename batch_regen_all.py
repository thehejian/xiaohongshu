#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量重新生成图片 + 上传飞书（58个主题 43–100）"""

import os, sys, subprocess, tempfile, json, time, re, threading

BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter"

# ── 加载主题映射 ──
with open(f"{BASE}/正文提示词.md") as f:
    doc = f.read()
blocks = re.split(r'\n(?=## 主题 \d+[：:])', doc)
folder_map, title_map = {}, {}
for num in range(43, 101):
    for b in blocks:
        if f"## 主题 {num}" in b:
            fm = re.search(r'\*\*文件夹\*\*:\s*\x60(.+?)\x60', b)
            if fm:
                folder_map[num] = fm.group(1)
            tm = re.match(r'## 主题 (\d+)[：:]?\s*(.*?)\n', b)
            if tm:
                title_map[num] = tm.group(2).strip()

topics = sorted(folder_map.keys())
print(f"Total topics: {len(topics)} ({min(topics)}–{max(topics)})")

# ── Step 1: 复制 gen_one.py ──
gen_src = f"{BASE}/image-cards/wudi-sanjiquan/gen_one.py"
gen_missing = []
for num in topics:
    folder = folder_map[num]
    dst = f"{BASE}/image-cards/{folder}/gen_one.py"
    if not os.path.exists(dst):
        with open(gen_src) as f:
            content = f.read()
        with open(dst, 'w') as f:
            f.write(content)
        gen_missing.append(num)
        print(f"  Copied gen_one.py -> {folder}")
print(f"gen_one.py copied to {len(gen_missing)} folders")

# ── Step 2: 图片生成 ──
BATCH_SIZE = 2  # 同时运行2个主题
gen_log = f"{BASE}/batch_regen_images.log"

def gen_topic(num):
    folder = folder_map[num]
    workdir = f"{BASE}/image-cards/{folder}"
    existing = [i for i in range(1, 7) if os.path.exists(f"{workdir}/{i:02d}-cover.png")]
    print(f"[{num:3d}/{folder:30s}] Existing images: {len(existing)}/6")
    
    # 4 calls: gen_one.py 1 → 2 3 → 4 5 → 6
    calls = [
        (["python3", "gen_one.py", "1"], os.path.join(workdir, "01-cover.png")),
        (["python3", "gen_one.py", "2", "3"], os.path.join(workdir, "02-cover.png")),
        (["python3", "gen_one.py", "4", "5"], os.path.join(workdir, "04-cover.png")),
        (["python3", "gen_one.py", "6"], os.path.join(workdir, "06-cover.png")),
    ]
    for cmd, check_file in calls:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300, cwd=workdir)
        if r.returncode != 0:
            print(f"  [{num:3d}] gen cmd {' '.join(cmd)} FAILED: {r.stderr[:200]}")
            return False
        if not os.path.exists(check_file):
            print(f"  [{num:3d}] Output not found: {check_file}")
            # wait a bit and check again
            time.sleep(5)
            if not os.path.exists(check_file):
                print(f"  [{num:3d}] Output STILL missing: {check_file}")
                return False
    
    # verify all 6
    final = [i for i in range(1, 7) if os.path.exists(f"{workdir}/{i:02d}-cover.png")]
    sizes = [os.path.getsize(f"{workdir}/{i:02d}-cover.png") for i in range(1, 7)]
    print(f"  [{num:3d}/{folder:30s}] Generated: {len(final)}/6 images, sizes: {sizes}")
    return len(final) == 6

# Run in batches
queue = list(topics)
results = {}
start_time = time.time()

while queue:
    batch = queue[:BATCH_SIZE]
    queue = queue[BATCH_SIZE:]
    threads = []
    for num in batch:
        t = threading.Thread(target=lambda n=num: results.update({n: gen_topic(n)}))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    elapsed = time.time() - start_time
    done = sum(1 for v in results.values() if v)
    print(f"\n=== Progress: {done}/{len(topics)} topics done ({elapsed/60:.1f} min) ===\n")

ok = sum(1 for v in results.values() if v)
fail = [n for n, v in results.items() if not v]
print(f"\n{'='*60}")
print(f"Image gen complete: {ok}/{len(topics)} OK, {len(fail)} failed")
if fail:
    print(f"Failed topics: {fail}")

# ── Step 3: 飞书上传（新建文档） ──
print(f"\n{'='*60}")
print(f"Starting Feishu upload for {ok} topics...\n")

upload_log = f"{BASE}/batch_regen_upload.log"
track_file = f"{BASE}/.feishu_uploaded"

def feishu_create(title, content_text):
    clean = content_text.split("#")[0].strip() if "#" in content_text else content_text
    tmpf = tempfile.mktemp(suffix=".md")
    with open(tmpf, "w") as f:
        f.write(clean)
    try:
        r = subprocess.run([
            "bash", "-c",
            f'export PATH="/opt/homebrew/bin:$PATH"; cat "{tmpf}" | lark-cli docs +create --title "{title}" --content - --doc-format markdown --as user --format json'
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
    r = subprocess.run([
        "bash", "-c",
        f'export PATH="/opt/homebrew/bin:$PATH"; cd "{BASE}/image-cards/{folder}"; lark-cli docs +media-insert --doc {token} --file ./{img_num:02d}-cover.png --as user'
    ], capture_output=True, text=True, timeout=60)
    return r.returncode == 0

upload_ok = 0
upload_fail = []

for num in topics:
    if results.get(num) is not True:
        print(f"  Topic {num}: SKIP (image gen failed)")
        continue
    
    folder = folder_map[num]
    article_path = f"{BASE}/image-cards/{folder}/article.md"
    if not os.path.exists(article_path):
        print(f"  Topic {num}: article.md not found, SKIP")
        continue
    
    with open(article_path) as f:
        article = f.read()
    
    title_line = title_map.get(num, f"主题{num}")
    title = f"场景{num}：{title_line[:50]}"
    
    print(f"  [{num:3d}/{folder:30s}] Creating doc...", end=" ", flush=True)
    token = feishu_create(title, article)
    if not token:
        print(f"✗ CREATE FAILED")
        upload_fail.append(num)
        time.sleep(5)
        continue
    print(f"token={token}", end=" ", flush=True)
    
    all_ok = True
    for i in range(1, 7):
        ok = feishu_insert(folder, token, i)
        if not ok:
            print(f"insert-{i} FAILED", end=" ", flush=True)
            all_ok = False
        else:
            print(f"✓{i}", end=" ", flush=True)
        time.sleep(3)
    
    if all_ok:
        upload_ok += 1
        with open(track_file, "a") as f:
            f.write(f"\n{num:03d}|{folder}|{token}")
        print(f"✓ https://qcnh2b60jsx1.feishu.cn/docx/{token}")
    else:
        upload_fail.append(num)
        print(f"⚠ partial failure")
    
    time.sleep(5)

total_elapsed = time.time() - start_time
print(f"\n{'='*60}")
print(f"Upload complete: {upload_ok} docs created, {len(upload_fail)} failed")
if upload_fail:
    print(f"Failed uploads: {upload_fail}")
print(f"Total time: {total_elapsed/60:.1f} min")
