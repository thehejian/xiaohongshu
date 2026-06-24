import requests,sys,time,os
AGNES_KEY=os.environ.get("AGNES_KEY","sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL="https://apihub.agnes-ai.com/v1/images/generations";W=H=1024
C="sfc-cover";D=["sfc-card2","sfc-card3"]
P={"cover":"Tang dynasty red warhorse from the Western Regions, Ferghana horse, muscular and powerful, on ancient battlefield, ink-wash painting style, deep crimson and gold palette, ultra-detailed 8K",
"card2":"Central Asian Ferghana valley, wild horses running free, the original homeland of blood-sweating horses, traditional Chinese painting, 8K",
"card3":"Tang dynasty cavalry returning in triumph, red flags and banners, victory celebration, traditional ink-wash painting, 8K"}
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