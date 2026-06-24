import requests,sys,time,os
AGNES_KEY = os.environ.get("AGNES_KEY","sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL = "https://apihub.agnes-ai.com/v1/images/generations"
W=1024;H=1024
C="lyg14-cover"
D=["lyg14-card1","lyg14-card2","lyg14-card3"]
P=["Tang dynasty general Chai Shao, imperial son-in-law and warrior husband of Princess Pingyang, traditional ink-wash painting, ultra-detailed 8K","Tang dynasty battlefield scene, heroic general leading troops, epic cavalry charge, traditional ink-wash painting, dramatic composition, 8K","Tang dynasty imperial court, officials in audience with Emperor Taizong, grand ceremony, traditional Chinese painting, warm gold tones, 8K","Tang dynasty Zhaoling mausoleum, classical Chinese stone carvings, solemn memorial atmosphere, ink-wash aesthetic, 8K"]
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
