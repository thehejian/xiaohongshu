import requests,sys,time,os
AGNES_KEY=os.environ.get("AGNES_KEY","sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL="https://apihub.agnes-ai.com/v1/images/generations";W=H=1024
C="zzsm-cover"
P="Catholic cathedral in small Chinese county town, Western-style church building, cross on spire, peaceful religious architecture, ink-wash painting style, serene spiritual atmosphere, ultra-detailed 8K"
def gen():
    for a in range(3):
        r=requests.post(AGNES_URL,headers={"Authorization":f"Bearer {AGNES_KEY}","Content-Type":"application/json"},json={"model":"agnes-image-2.1-flash","prompt":P,"n":1,"size":f"{W}x{H}"},timeout=120)
        if r.status_code==200:break
        time.sleep(5)
    else:raise RuntimeError("Failed cover")
    ir=requests.get(r.json()["data"][0]["url"],timeout=120)
    with open(f"{C}.png","wb") as fp:fp.write(ir.content);print(f"{C}.png saved",file=sys.stderr)
def main():
    gen()
    print("ALL DONE",file=sys.stderr)
if __name__=="__main__":main()