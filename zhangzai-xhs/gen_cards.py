import requests,sys,time,os
AGNES_KEY=os.environ.get("AGNES_KEY","sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL="https://apihub.agnes-ai.com/v1/images/generations";W=H=1024
C="zz-cover";D=["zz-card1","zz-card2","zz-card3"]
P={"cover":"Ancient Chinese philosopher in Song dynasty scholar robes, writing calligraphy with brush, four monumental phrases floating in air behind him, traditional ink-wash painting style, majestic atmosphere, deep black and gold palette, ultra-detailed 8K",
"card1":"Ancient Chinese scholar studying in a mountain studio, Fan Zhongyan visiting him, scrolls of Confucian classics on desk, traditional Chinese painting, warm scholarly tones, 8K",
"card2":"Ancient Chinese lecture hall, scholar teaching students beneath a pavilion, village setting with farmland, traditional ink-wash style, pastoral scholarly atmosphere, 8K",
"card3":"Ancient Chinese tombstone with engraved epitaph, misty mountain landscape, pine trees, memorial atmosphere, traditional painting, melancholic reverence, 8K"}
def g(k):
    p=P[k];f={"cover":C,"card1":D[0],"card2":D[1],"card3":D[2]}[k]
    for a in range(3):
        r=requests.post(AGNES_URL,headers={"Authorization":f"Bearer {AGNES_KEY}","Content-Type":"application/json"},json={"model":"agnes-image-2.1-flash","prompt":p,"n":1,"size":f"{W}x{H}"},timeout=120)
        if r.status_code==200:break
        time.sleep(5)
    else:raise RuntimeError(f"Failed {k}")
    ir=requests.get(r.json()["data"][0]["url"],timeout=120)
    with open(f"{f}.png","wb") as fp:fp.write(ir.content);print(f"{f}.png saved",file=sys.stderr)
def main():
    g("cover")
    for k in["card1","card2","card3"]:g(k)
    print("ALL DONE",file=sys.stderr)
if __name__=="__main__":main()