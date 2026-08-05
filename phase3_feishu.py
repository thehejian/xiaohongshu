#!/usr/bin/env python3
"""Phase 3: Upload topics to Feishu docs + insert images."""
import subprocess, json, os, sys, time, re

BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter"

def feishu_create(title, content_text):
    """Create Feishu doc, return token."""
    clean = content_text.split("#")[0].strip() if "#" in content_text else content_text
    # Write to temp file to avoid shell escaping hell
    import tempfile
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
        print(f"  Feishu create fail: {r.stderr[:200]}")
        return None
    try:
        data = json.loads(r.stdout)
        return data.get("data", {}).get("document", {}).get("document_id") or data.get("token", "")
    except:
        m = re.search(r'document_id["\s:]+"([^"]+)"', r.stdout)
        if m:
            return m.group(1)
        print(f"  Feishu parse: {r.stdout[:200]}")
        return None

def feishu_insert_image(folder, token, img_num):
    """Insert one image into Feishu doc."""
    workdir = f"{BASE}/image-cards/{folder}"
    img_path = f"{workdir}/{img_num:02d}-cover.png"
    if not os.path.exists(img_path):
        print(f"  Image {img_num:02d} missing")
        return False
    r = subprocess.run([
        "bash", "-c",
        f'export PATH="/opt/homebrew/bin:$PATH"; cd "{workdir}"; lark-cli docs +media-insert --doc {token} --file ./{img_num:02d}-cover.png --as user'
    ], capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        print(f"  Insert {img_num:02d}: {r.stderr[:100]}")
        return False
    print(f"  Insert {img_num:02d}: OK")
    return True

def process_topic(num, folder):
    """Create Feishu doc + insert 6 images for one topic."""
    workdir = f"{BASE}/image-cards/{folder}"
    article_path = f"{workdir}/article.md"
    if not os.path.exists(article_path):
        print(f"  Article missing for {folder}")
        return None
    
    with open(article_path) as f:
        content = f.read()
    
    title = content.split("\n")[0].strip()[:50]
    
    # Check images
    images = [i for i in range(1, 7) if os.path.exists(f"{workdir}/{i:02d}-cover.png")]
    if len(images) < 6:
        print(f"  Only {len(images)}/6 images for {folder}, skipping Feishu")
        return None
    
    print(f"  Creating Feishu doc: {title}")
    token = feishu_create(title, content)
    if not token:
        print(f"  Failed to create doc for {folder}")
        return None
    print(f"  Token: {token}")
    
    # Insert images sequentially
    for i in range(1, 7):
        feishu_insert_image(folder, token, i)
        time.sleep(3)
    
    url = f"https://qcnh2b60jsx1.feishu.cn/docx/{token}"
    print(f"  URL: {url}")
    return token

# ── Parse topics list from doc ──
with open(f"{BASE}/正文提示词.md") as f:
    doc = f.read()
blocks = re.split(r'\n(?=## 主题 \d+[：:])', doc)

topics = []
for block in blocks:
    m = re.match(r'## 主题 (\d+)[：:]?\s*(.*?)\n', block)
    if not m:
        continue
    num = int(m.group(1))
    if num < 43 or num > 100:
        continue
    fm = re.search(r'\*\*文件夹\*\*:\s*\x60(.+?)\x60', block)
    folder = fm.group(1) if fm else f'topic-{num:03d}'
    topics.append((num, folder))

print(f"Loaded {len(topics)} topics for Feishu upload")

# ── Process ──
if len(sys.argv) > 1:
    args = [a for a in sys.argv[1:] if a.isdigit()]
    if len(args) == 1:
        num = int(args[0])
        folder = [f for n, f in topics if n == num][0]
        process_topic(num, folder)
    elif len(args) == 2:
        start_n, end_n = int(args[0]), int(args[1])
        for num, folder in topics:
            if num < start_n or num > end_n:
                continue
            tok = process_topic(num, folder)
            if tok:
                time.sleep(5)
            else:
                print(f"  TOPIC {num} Feishu FAILED, continuing")
else:
    for num, folder in topics:
        tok = process_topic(num, folder)
        if tok:
            time.sleep(5)

print("\n=== ALL FEISHU DONE ===")
