import requests, sys, time, os
AGNES_KEY = os.environ.get("AGNES_KEY","sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL="https://apihub.agnes-ai.com/v1/images/generations"; SRC_W=SRC_H=1024
COVER="fth-cover"; CARDS=["fth-card1","fth-card2","fth-card3"]
P={"cover":("Ancient Chinese empress dowager in splendid robes sitting behind a young emperor, powerful and dignified, court scene, traditional ink-wash painting, deep purple and gold palette, authoritative atmosphere, ultra-detailed 8K"),
"card1":("Ancient Chinese palace, a noble woman conspiring with eunuchs, secret political plotting, traditional painting style, dark intrigue atmosphere, 8K"),
"card2":("Ancient Chinese emperor as a child studying with his grandmother, scrolls and Confucian texts, warm educational scene, traditional ink-wash style, 8K"),
"card3":("Ancient Chinese farmland, peasants receiving land titles from officials, land reform scene, traditional painting style, hopeful pastoral atmosphere, 8K")}
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