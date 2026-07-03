#!/usr/bin/env python3
import json, subprocess, base64, re, os, sys, time
from pathlib import Path
WORKSPACE="/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter"
api_key=''
for m in re.findall(r'api_key:\s*(.+)',(Path.home()/'.hermes'/'config.yaml').read_text()):
    m=m.strip().strip("'").strip('"')
    if m.startswith('sk-') and len(m)>30: api_key=m; break
hdr=["-H","Authorization: Bearer "+api_key,"-H","Content-Type: application/json"]

folders=[f.replace('-xhs','') for f in sys.argv[1:]] if len(sys.argv)>1 else []
if not folders:
    print("Usage: python3 batch_gen.py zhuxin likeyong ...")
    sys.exit(1)

for fold in folders:
    BASE=f"{WORKSPACE}/{fold}-xhs"
    if not os.path.isdir(BASE):
        print(f"SKIP {fold}: no folder")
        continue
    tag=fold
    prompts=sorted(os.listdir(f"{BASE}/prompts"))
    print(f"\n=== {fold} ({len(prompts)} prompts) ===")
    ref_b64=None
    for name in prompts:
        p=open(f"{BASE}/prompts/{name}").read().strip()
        payload={"model":"agnes-image-2.1-flash","prompt":p,"size":"1024x1024","n":1,"steps":25,"guidance":8.0}
        if name.startswith("01-"):
            pass
        elif ref_b64:
            payload["image"]="data:image/png;base64,"+ref_b64
        else:
            ref_b64=base64.b64encode(open(f"{BASE}/01-cover.png","rb").read()).decode()
            payload["image"]="data:image/png;base64,"+ref_b64
        fp=f"/tmp/{tag}-{name.replace('.md','')}.json"
        with open(fp,"w") as f: json.dump(payload,f)
        r=subprocess.run(["curl","-s","--max-time","300"]+hdr+["-d",f"@{fp}","https://apihub.agnes-ai.com/v1/images/generations"],capture_output=True,text=True,timeout=300)
        d=json.loads(r.stdout)
        if 'data' in d:
            outname=name.replace('.md','.png')
            subprocess.run(["curl","-sL",d['data'][0]['url'],"-o",f"{BASE}/{outname}"],timeout=120)
            sz=os.path.getsize(f"{BASE}/{outname}")//1024
            print(f"  {tag} {name.replace('.md','')} OK {sz}KB")
            if name.startswith("01-"):
                ref_b64=base64.b64encode(open(f"{BASE}/01-cover.png","rb").read()).decode()
        else:
            print(f"  {tag} {name.replace('.md','')} FAIL:",r.stdout[:200])
print("\nAll done!")
