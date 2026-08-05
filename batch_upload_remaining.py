#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Upload remaining 16 topics to Feishu (15 SKIP + 85 fix)."""

import os, sys, subprocess, tempfile, json, time, re

BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter"
track_file = f"{BASE}/.feishu_uploaded"

with open(f"{BASE}/正文提示词.md") as f:
    doc = f.read()
blocks = re.split(r'\n(?=## 主题 \d+[：:])', doc)
folder_map, title_map = {}, {}
for num in range(43, 101):
    for b in blocks:
        if f"## 主题 {num}" in b:
            fm = re.search(r'\*\*文件夹\*\*:\s*\x60(.+?)\x60', b)
            if fm: folder_map[num] = fm.group(1)
            tm = re.match(r'## 主题 (\d+)[：:]?\s*(.*?)\n', b)
            if tm: title_map[num] = tm.group(2).strip()

retry_upload = [59, 63, 66, 70, 71, 77, 81, 82, 86, 89, 90, 91, 97, 98, 100, 85]
print(f"Topics to upload: {retry_upload}")

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
        os.unlink(tmpf)
    if r.returncode != 0:
        print(f"  Create FAILED: {r.stderr[:200]}")
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

ok = 0
fail = []

for num in retry_upload:
    folder = folder_map.get(num)
    if not folder:
        print(f"[{num:3d}] No folder mapping, SKIP")
        fail.append(num)
        continue
    
    article_path = f"{BASE}/image-cards/{folder}/article.md"
    if not os.path.exists(article_path):
        print(f"[{num:3d}] article.md not found, SKIP")
        fail.append(num)
        continue
    
    imgs = [i for i in range(1,7) if os.path.exists(f"{BASE}/image-cards/{folder}/{i:02d}-cover.png")]
    if len(imgs) < 6:
        print(f"[{num:3d}] Only {len(imgs)}/6 images, SKIP")
        fail.append(num)
        continue
    
    with open(article_path) as f:
        article = f.read()
    
    title_line = title_map.get(num, f"主题{num}")
    title = f"场景{num}：{title_line[:50]}"
    
    print(f"[{num:3d}/{folder:30s}] Creating doc...", end=" ", flush=True)
    token = feishu_create(title, article)
    if not token:
        print("✗ CREATE FAILED")
        fail.append(num)
        time.sleep(5)
        continue
    print(f"token={token}", end=" ", flush=True)
    
    all_ok = True
    for i in range(1, 7):
        ok_ins = feishu_insert(folder, token, i)
        if not ok_ins:
            print(f"insert-{i} FAILED", end=" ", flush=True)
            all_ok = False
        else:
            print(f"✓{i}", end=" ", flush=True)
        time.sleep(3)
    
    if all_ok:
        ok += 1
        with open(track_file, "a") as f:
            f.write(f"\n{num:03d}|{folder}|{token}")
        print(f" ✓ https://qcnh2b60jsx1.feishu.cn/docx/{token}")
    else:
        fail.append(num)
        print(f" ⚠ partial failure")
    
    time.sleep(5)

print(f"\nDone: {ok} uploaded, {len(fail)} failed")
if fail:
    print(f"Failed: {fail}")
