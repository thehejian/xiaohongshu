import requests,sys,time,os
AGNES_KEY=os.environ.get("AGNES_KEY","sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL="https://apihub.agnes-ai.com/v1/images/generations";W=H=1024
C="leq-cover";D=["leq-card1","leq-card2","leq-card3"]
P={"cover":"Ancient Chinese Confucian scholar in Ming dynasty robes, refusing an imperial edict, coffin beside him, traditional ink-wash painting style, Song dynasty aesthetic, solemn atmosphere, deep indigo and gold palette, ultra-detailed 8K",
"card1":"Ancient Chinese thatched cottage study, scholar reading by candlelight, his mother weaving cloth, poor but determined atmosphere, traditional Chinese painting, warm amber tones, 8K",
"card2":"Ancient Chinese palace scene, emperor's messenger delivering edict, scholar kneeling with head bowed in refusal, tension between power and integrity, traditional ink-wash, 8K",
"card3":"Ancient Chinese mountain path, elderly scholar walking away from the capital, carrying books, autumn leaves falling, traditional painting, melancholic yet dignified, 8K"}
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