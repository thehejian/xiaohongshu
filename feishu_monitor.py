#!/usr/bin/env python3
"""Monitor + auto-uploade Feishu for completed topics. Runs in background."""
import subprocess, json, os, sys, time, re, tempfile

BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter"
PROGRESS_FILE = f"{BASE}/feishu_upload.log"
UPLOADED_FILE = f"{BASE}/.feishu_uploaded"

# Load already uploaded topics
uploaded = set()
if os.path.exists(UPLOADED_FILE):
    with open(UPLOADED_FILE) as f:
        uploaded = set(line.strip() for line in f if line.strip())

def log(msg):
    ts = time.strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(PROGRESS_FILE, "a") as f:
        f.write(line + "\n")

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
    workdir = f"{BASE}/image-cards/{folder}"
    r = subprocess.run([
        "bash", "-c",
        f'export PATH="/opt/homebrew/bin:$PATH"; cd "{workdir}"; lark-cli docs +media-insert --doc {token} --file ./{img_num:02d}-cover.png --as user'
    ], capture_output=True, text=True, timeout=60)
    return r.returncode == 0

def upload_topic(num, folder):
    workdir = f"{BASE}/image-cards/{folder}"
    article_path = f"{workdir}/article.md"
    if not os.path.exists(article_path):
        log(f"  No article for {folder}")
        return False
    
    with open(article_path) as f:
        content = f.read()
    title = content.split("\n")[0].strip()[:50]
    
    images = [i for i in range(1, 7) if os.path.exists(f"{workdir}/{i:02d}-cover.png")]
    if len(images) < 6:
        return False
    
    log(f"  Uploading {folder} ({title[:30]}...)")
    token = feishu_create(title, content)
    if not token:
        log(f"  Feishu create FAILED for {folder}")
        return False
    
    for i in range(1, 7):
        ok = feishu_insert(folder, token, i)
        if not ok:
            log(f"  Insert {i} FAILED for {folder}")
        time.sleep(3)
    
    url = f"https://qcnh2b60jsx1.feishu.cn/docx/{token}"
    log(f"  DONE: {url}")
    
    # Mark as uploaded
    marker = f"{num:03d}|{folder}|{token}"
    with open(UPLOADED_FILE, "a") as f:
        f.write(marker + "\n")
    uploaded.add(marker)
    return True

# Parse topics
with open(f"{BASE}/正文提示词.md") as f:
    doc = f.read()

blocks = re.split(r'\n(?=## 主题 \d+[：:])', doc)
topic_list = []
for block in blocks:
    m = re.match(r'## 主题 (\d+)[：:]?\s*(.*?)\n', block)
    if not m:
        continue
    num = int(m.group(1))
    if num < 43 or num > 100:
        continue
    fm = re.search(r'\*\*文件夹\*\*:\s*\x60(.+?)\x60', block)
    folder = fm.group(1) if fm else f'topic-{num:03d}'
    topic_list.append((num, folder))

log(f"Monitor started. {len(topic_list)} topics to watch")
log(f"Already uploaded: {len(uploaded)}")

# Main loop
while True:
    all_done = True
    for num, folder in topic_list:
        marker = f"{num:03d}|{folder}"
        if any(marker in u for u in uploaded):
            continue
        
        workdir = f"{BASE}/image-cards/{folder}"
        images = [i for i in range(1, 7) if os.path.exists(f"{workdir}/{i:02d}-cover.png")]
        
        if len(images) == 6:
            log(f"Topic {num} ({folder}): all 6 images ready, uploading...")
            upload_topic(num, folder)
            time.sleep(5)
            all_done = False
        else:
            all_done = False
    
    if all_done:
        log("All topics processed! Monitor exiting.")
        break
    
    pending_count = sum(1 for n, f in topic_list if f'{n:03d}|{f}' not in str(uploaded))
    log(f"Pending: {pending_count}")
    time.sleep(120)  # Check every 2 minutes
