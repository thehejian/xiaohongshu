#!/usr/bin/env python3
import json, subprocess, base64, re, os
from pathlib import Path
BASE=os.path.dirname(os.path.abspath(__file__))
FOLDER=os.path.basename(BASE).replace('-xhs','')
api_key=''
for m in re.findall(r'api_key:\s*(.+)',(Path.home()/'.hermes'/'config.yaml').read_text()):
    m=m.strip().strip("'").strip('"')
    if m.startswith('sk-') and len(m)>30: api_key=m; break
hdr=["-H","Authorization: Bearer "+api_key,"-H","Content-Type: application/json"]
prompts=sorted(os.listdir(BASE+"/prompts"))
skip_cover=True
for name in prompts:
    p=open(f"{BASE}/prompts/{name}").read().strip()
    is_cover=name.startswith("01-")
    payload={"model":"agnes-image-2.1-flash","prompt":p,"size":"1024x1024","n":1,"steps":25,"guidance":8.0}
    if not is_cover and skip_cover:
        ref_b64=base64.b64encode(open(BASE+"/01-cover.png","rb").read()).decode()
        payload["image"]="data:image/png;base64,"+ref_b64
        skip_cover=False
    fp=f"/tmp/{FOLDER}-{name.replace('.md','')}.json"
    with open(fp,"w") as f: json.dump(payload,f)
    r=subprocess.run(["curl","-s","--max-time","300"]+hdr+["-d",f"@{fp}","https://apihub.agnes-ai.com/v1/images/generations"],capture_output=True,text=True,timeout=300)
    d=json.loads(r.stdout)
    if 'data' in d:
        outname=name.replace('.md','.png')
        subprocess.run(["curl","-sL",d['data'][0]['url'],"-o",f"{BASE}/{outname}"],timeout=120)
        sz=os.path.getsize(f"{BASE}/{outname})//1024
        print(FOLDER,name.replace('.md',''),"OK",sz,"KB")
    else:
        print(FOLDER,name.replace('.md',''),"FAIL:",r.stdout[:200])
print(FOLDER,"Done!")
