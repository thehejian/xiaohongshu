import requests,sys,time,os
AGNES_KEY=os.environ.get("AGNES_KEY","sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL="https://apihub.agnes-ai.com/v1/images/generations";W=H=1024
C="tlb-cover";D=["tlb-card2","tlb-card3"]
P={"cover":"Tang dynasty yellow-white warhorse, sturdy and reliable, on the Qianshuiyuan battlefield, grassy plains, ink-wash painting style, warm earth tones, heroic atmosphere, ultra-detailed 8K",
"card2":"Tang dynasty army crossing a swampy battlefield, difficult terrain, soldiers pushing forward, epic campaign scene, traditional ink-wash painting, 8K",
"card3":"Turkic steppe landscape, nomads and horses, grasslands of Inner Asia, traditional Chinese painting style, 8K"}
def g(k):
    p=P[k];f={"cover":C,"card2":D[0],"card3":D[1]}[k]
    for a in range(3):
        r=requests.post(AGNES_URL,headers={"Authorization":f"Bearer {AGNES_KEY}","Content-Type":"application/json"},json={"model":"agnes-image-2.1-flash","prompt":p,"n":1,"size":f"{W}x{H}"},timeout=120)
        if r.status_code==200:break
        time.sleep(5)
    else:raise RuntimeError(f"Failed {k}")
    ir=requests.get(r.json()["data"][0]["url"],timeout=120)
    with open(f"{f}.png","wb") as fp:fp.write(ir.content);print(f"{f}.png saved",file=sys.stderr)
def main():
    g("cover")
    for k in["card2","card3"]:g(k)
    print("ALL DONE",file=sys.stderr)
if __name__=="__main__":main()