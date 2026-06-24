import requests,sys,time,os
AGNES_KEY=os.environ.get("AGNES_KEY","sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL="https://apihub.agnes-ai.com/v1/images/generations";W=H=1024
C="btw-cover";D=["btw-card1","btw-card2","btw-card3"]
P={"cover":"Tang dynasty black horse with white hooves, first warhorse of Emperor Taizong, galloping across a battlefield at sunrise, ink-wash painting style, youthful energetic atmosphere, ultra-detailed 8K",
"card1":"Tang dynasty stone horse relief carving at Zhaoling mausoleum, classical Chinese art, black horse with white hooves, traditional sculpture style, ink-wash aesthetic, 8K",
"card2":"Young Li Shimin at age 19 on his first campaign, leading troops, youthful emperor on a black horse, traditional ink-wash painting, 8K",
"card3":"Tang dynasty mausoleum grounds, six horse reliefs displayed together, cultural heritage site, misty morning, ink-wash style, 8K"}
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