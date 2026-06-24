import requests,sys,time,os
AGNES_KEY=os.environ.get("AGNES_KEY","sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL="https://apihub.agnes-ai.com/v1/images/generations";W=H=1024
C="whz-cover";D=["whz-card1","whz-card2","whz-card3"]
P={"cover":"Ancient Chinese scholar in Ming robes at a mountain study beneath Hua Mountain, writing books, pine trees and steep cliffs in background, traditional ink-wash painting, deep blue and stone gray palette, ultra-detailed 8K",
"card1":"Ancient Chinese mountain villa library filled with scrolls, scholar organizing books, warm study atmosphere, traditional Chinese painting style, 8K",
"card2":"Ancient Chinese capital city street, scholar walking reluctantly with officials, being pressured to join examination, tense mood, traditional ink-wash, 8K",
"card3":"Ancient Chinese mountain tomb with simple epitaph reading 'Ming person Wang', Hua Mountain in background, solemn memorial, traditional painting, 8K"}
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