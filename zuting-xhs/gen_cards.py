import requests, sys, time, os
AGNES_KEY = os.environ.get("AGNES_KEY","sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL="https://apihub.agnes-ai.com/v1/images/generations"; SRC_W=SRC_H=1024
COVER="zt-cover"; CARDS=["zt-card1","zt-card2","zt-card3"]
P={"cover":("Ancient Chinese blind scholar-official in court robes, sitting at a desk, eyes closed but sharp expression, scrolls around him, traditional ink-wash painting, dark red and gold palette, mysterious intellectual atmosphere, ultra-detailed 8K"),
"card1":("Ancient Chinese marketplace, a man getting caught stealing a golden cup, crowd watching, chaotic scene, traditional painting style, satirical tone, 8K"),
"card2":("Ancient Chinese court, blind minister dictating documents to scribes, confident expression, political power scene, traditional ink-wash style, 8K"),
"card3":("Ancient Chinese prison cell, elderly blind minister in chains, regretful expression, tragic end, traditional painting style, dark melancholic tones, 8K")}
def g(k):
    p=P[k];f={"cover":COVER,"card1":CARDS[0],"card2":CARDS[1],"card3":CARDS[2]}[k]
    for a in range(3):
        r=requests.post(AGNES_URL,headers={"Authorization":f"Bearer {AGNES_KEY}","Content-Type":"application/json"},json={"model":"agnes-image-2.1-flash","prompt":p,"n":1,"size":f"{SRC_W}x{SRC_H}"},timeout=120)
        if r.status_code==200:break
        print(f"Attempt {a+1} failed: {r.status_code}",file=sys.stderr);time.sleep(5)
    else:raise RuntimeError(f"Failed {k}")
    ir=requests.get(r.json()["data"][0]["url"],timeout=120)
    with open(f"{f}.png","wb") as fp:fp.write(ir.content);print(f"{f}.png saved",file=sys.stderr)
def main():
    g("cover")
    for k in["card1","card2","card3"]:g(k)
    print("ALL DONE",file=sys.stderr)
if __name__=="__main__":main()