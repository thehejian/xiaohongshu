#!/usr/bin/env python3
import json, subprocess, base64, re, os
from pathlib import Path
BASE=os.path.dirname(os.path.abspath(__file__))
api_key=''
for m in re.findall(r'api_key:\s*(.+)',(Path.home()/'.hermes'/'config.yaml').read_text()):
    m=m.strip().strip("'").strip('"')
    if m.startswith('sk-') and len(m)>30: api_key=m; break
hdr=["-H","Authorization: Bearer "+api_key,"-H","Content-Type: application/json"]
def gen(name):
    p=open(f"{BASE}/prompts/{name}.md").read().strip()
    payload={"model":"agnes-image-2.1-flash","prompt":p,"size":"1024x1024","n":1,"steps":25,"guidance":8.0}
    fp=f"/tmp/yy-{name}.json"
    with open(fp,"w") as f: json.dump(payload,f)
    r=subprocess.run(["curl","-s","--max-time","300"]+hdr+["-d",f"@{fp}","https://apihub.agnes-ai.com/v1/images/generations"],capture_output=True,text=True,timeout=300)
    d=json.loads(r.stdout)
    if 'data' in d:
        subprocess.run(["curl","-sL",d['data'][0]['url'],"-o",f"{BASE}/{name}.png"],timeout=120)
        sz=os.path.getsize(f"{BASE}/{name}.png")//1024
        print("yy",name,"OK",sz,"KB")
        return d['data'][0]['url']
    else:
        print("yy",name,"FAIL:",r.stdout[:200])
        return None
gen("01-cover")
ref_b64=base64.b64encode(open(BASE+"/01-cover.png","rb").read()).decode()
for name in ["02-suspicion","03-khitan","04-humiliation","05-betrayal","06-legacy"]:
    p=open(f"{BASE}/prompts/{name}.md").read().strip()
    payload={"model":"agnes-image-2.1-flash","prompt":p,"size":"1024x1024","n":1,"steps":25,"guidance":8.0,"image":"data:image/png;base64,"+ref_b64}
    fp=f"/tmp/yy-{name}.json"
    with open(fp,"w") as f: json.dump(payload,f)
    r=subprocess.run(["curl","-s","--max-time","300"]+hdr+["-d",f"@{fp}","https://apihub.agnes-ai.com/v1/images/generations"],capture_output=True,text=True,timeout=300)
    d=json.loads(r.stdout)
    if 'data' in d:
        subprocess.run(["curl","-sL",d['data'][0]['url'],"-o",f"{BASE}/{name}.png"],timeout=120)
        sz=os.path.getsize(f"{BASE}/{name}.png")//1024
        print("yy",name,"OK",sz,"KB")
    else: print("yy",name,"FAIL:",r.stdout[:200])
print("yy Done!")
