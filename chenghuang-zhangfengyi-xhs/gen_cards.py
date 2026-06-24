import requests,sys,time,os
AGNES_KEY=os.environ.get("AGNES_KEY","sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL="https://apihub.agnes-ai.com/v1/images/generations";W=H=1024
C="zfy-cover";D=["zfy-card1","zfy-card2","zfy-card3"]
P=["Qing dynasty magistrate Zhang Fengyi reviewing legal cases, honest official scene, traditional Chinese folk painting, ink-wash","Ancient Chinese city god temple interior, incense and offerings, traditional folk belief scene, ink-wash painting style, 8K","Ancient Shaanxi folk temple fair, traditional stage performance, worshippers gathering, festive atmosphere, ink-wash painting, 8K","Ancient Chinese city god statue in temple, majestic figure in official robes, traditional folk art, ink-wash style, 8K"]
def g(i):
    for a in range(3):
        r=requests.post(AGNES_URL,headers={"Authorization":f"Bearer {AGNES_KEY}","Content-Type":"application/json"},json={"model":"agnes-image-2.1-flash","prompt":P[i],"n":1,"size":f"{W}x{H}"},timeout=120)
        if r.status_code==200:break
        time.sleep(5)
    else:raise RuntimeError(f"Failed {i}")
    ir=requests.get(r.json()["data"][0]["url"],timeout=120)
    fn=[C]+D
    with open(f"{fn[i]}.png","wb") as fp:fp.write(ir.content);print(f"{fn[i]}.png saved",file=sys.stderr)
def main():
    for i in range(4):g(i)
    print("ALL DONE",file=sys.stderr)
if __name__=="__main__":main()
