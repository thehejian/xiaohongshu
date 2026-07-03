#!/usr/bin/env python3
import json, subprocess, base64, re, os
from pathlib import Path
BASE="/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/comfyui-xhs"
api_key=''
for m in re.findall(r'api_key:\s*(.+)',(Path.home()/'.hermes'/'config.yaml').read_text()):
    m=m.strip().strip("'").strip('"')
    if m.startswith('sk-') and len(m)>30: api_key=m; break

os.rename(BASE+"/c010_0.png",BASE+"/01-cover.png")
ref_b64=base64.b64encode(open(BASE+"/01-cover.png","rb").read()).decode()

for name in ["02-compare","03-workflow","04-advantages","05-learning","06-ending"]:
    p=open(f"{BASE}/prompts/{name}.md").read().strip()
    payload={"model":"agnes-image-2.1-flash","prompt":p,"size":"1024x1024","n":1,"steps":25,"guidance":8.0,"image":"data:image/png;base64,"+ref_b64}
    with open(f"/tmp/cf_{name}.json","w") as f: json.dump(payload,f)
    r=subprocess.run(["curl","-s","--max-time","300","-H","Authorization: Bearer "+api_key,"-H","Content-Type: application/json","-d",f"@/tmp/cf_{name}.json","https://apihub.agnes-ai.com/v1/images/generations"],capture_output=True,text=True,timeout=300)
    d=json.loads(r.stdout)
    if 'data' in d:
        subprocess.run(["curl","-sL",d['data'][0]['url'],"-o",f"{BASE}/{name}.png"],timeout=120)
        print(name,"OK",os.path.getsize(f"{BASE}/{name}.png")//1024,"KB")
    else:
        print(name,"FAIL:",r.stdout[:200])
print("Done!")