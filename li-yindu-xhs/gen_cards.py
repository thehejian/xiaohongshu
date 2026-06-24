import requests,sys,time,os
AGNES_KEY=os.environ.get("AGNES_KEY","sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL="https://apihub.agnes-ai.com/v1/images/generations";W=H=1024
C="lyd-cover";D=["lyd-card1","lyd-card2","lyd-card3"]
P={"cover":"Ancient Chinese scholar in simple Ming robes teaching children in a rustic classroom, farm tools beside the desk, half-farming half-studying lifestyle, traditional ink-wash painting, warm earth tones, ultra-detailed 8K",
"card1":"Ancient Chinese imperial examination hall, scholar writing poetry reluctantly, surrounded by officials, tense atmosphere, traditional Chinese painting style, 8K",
"card2":"Ancient Chinese road, scholar traveling on foot with a staff, vast landscape, determined expression heading home, traditional ink-wash, 8K",
"card3":"Ancient Chinese village scene, elderly scholar refusing to meet Qing officials at his door, rural setting with willows, traditional painting style, resolute dignity, 8K"}
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