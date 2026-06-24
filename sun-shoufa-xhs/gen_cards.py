import requests,sys,time,os
AGNES_KEY=os.environ.get("AGNES_KEY","sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL="https://apihub.agnes-ai.com/v1/images/generations";W=H=1024
C="ssf-cover";D=["ssf-card1","ssf-card2","ssf-card3"]
P={"cover":"Ancient Chinese warrior general wielding an iron whip on horseback, leading a charge against Qing army, epic battlefield, traditional ink-wash painting, deep crimson and iron gray palette, ultra-detailed 8K",
"card1":"Ancient Chinese mountain fortress on a cliff, rebels defending the stronghold, Qing troops besieging below, dramatic mountain terrain, traditional Chinese painting, 8K",
"card2":"Ancient Chinese night raid scene, rebels sneaking down from mountain to attack enemy camp, moonlight ambush, traditional ink-wash style, 8K",
"card3":"Ancient Chinese riverbank battle, general fighting to his last arrow, surrounded by enemy troops, tragic last stand, traditional painting, dramatic twilight tones, 8K"}
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