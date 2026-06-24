import requests,sys,time,os
AGNES_KEY=os.environ.get("AGNES_KEY","sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL="https://apihub.agnes-ai.com/v1/images/generations";W=H=1024
C="lb-cover";D=["lb-card1","lb-card2","lb-card3"]
P={"cover":"Ancient Chinese hermit poet in a mountain hut made of oak leaves, writing poetry on a leaf, misty mountain forest, traditional ink-wash painting, deep green and mist white palette, ultra-detailed 8K",
"card1":"Ancient Chinese deep mountain scene, hermit clearing land with a hoe, planting vegetables, simple rustic life, traditional Chinese painting, warm sunlit tones, 8K",
"card2":"Ancient Chinese poet sitting on a mountain peak, enjoying clouds and white mist, scrolls scattered around, traditional ink-wash landscape, ethereal atmosphere, 8K",
"card3":"Ancient Chinese thatched hut in autumn mountain forest, fallen oak leaves covering the ground, a simple grave nearby, melancholic scene, traditional painting, 8K"}
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