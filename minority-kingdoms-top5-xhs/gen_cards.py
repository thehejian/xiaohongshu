import requests, sys, time, os
AGNES_KEY = os.environ.get("AGNES_KEY","sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL="https://apihub.agnes-ai.com/v1/images/generations"; SRC_W=SRC_H=1024
COVER="mk-cover"; CARDS=["mk-card1","mk-card2","mk-card3","mk-card4","mk-card5"]
PROMPTS={"cover":("Ancient Chinese frontier map showing territories of 5 minority kingdoms, traditional ink-wash style, parchment background, epic historical panoramic view, ultra-detailed 8K"),
"card1":("Ancient Khitan/Liao dynasty palace, Khitan warriors on horseback, traditional grassland empire scene, ink-wash painting style, deep blue and gold palette, 8K"),
"card2":("Ancient Tibetan plateau, Potala Palace, Tibetan warriors and Buddhist monks, snow mountains background, traditional Tibetan painting style, warm sand and red tones, 8K"),
"card3":("Ancient Manchu/ Qing dynasty Forbidden City, imperial court scene, Manchu nobles in court dress, traditional Chinese painting style, imperial gold and crimson, 8K"),
"card4":("Ancient Dali kingdom in Yunnan, Buddhist pagodas, tropical mountain landscape, Bai ethnic architecture, traditional Chinese painting style, jade green and gold, 8K"),
"card5":("Ancient Goguryeo mountain fortress, Korean-style watchtower, warriors on fortress walls, northeast Asian landscape, traditional ink-wash painting, misty mountain palette, 8K")}
def g(k):
    p=PROMPTS[k];f={"cover":COVER,"card1":CARDS[0],"card2":CARDS[1],"card3":CARDS[2],"card4":CARDS[3],"card5":CARDS[4]}[k]
    for a in range(3):
        r=requests.post(AGNES_URL,headers={"Authorization":f"Bearer {AGNES_KEY}","Content-Type":"application/json"},json={"model":"agnes-image-2.1-flash","prompt":p,"n":1,"size":f"{SRC_W}x{SRC_H}"},timeout=120)
        if r.status_code==200:break
        time.sleep(5)
    else:raise RuntimeError(f"Failed {k}")
    ir=requests.get(r.json()["data"][0]["url"],timeout=120)
    with open(f"{f}.png","wb") as fp:fp.write(ir.content);print(f"{f}.png saved",file=sys.stderr)
def main():
    g("cover")
    for k in["card1","card2","card3","card4","card5"]:g(k)
    print("ALL DONE",file=sys.stderr)
if __name__=="__main__":main()