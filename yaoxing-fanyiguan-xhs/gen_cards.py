import requests, sys, time, os
AGNES_KEY = os.environ.get("AGNES_KEY", "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL = "https://apihub.agnes-ai.com/v1/images/generations"
SRC_W, SRC_H = 1024, 1024
COVER = "yxfg-cover"
CARDS = ["yxfg-card1", "yxfg-card2", "yxfg-card3"]
PROMPTS = {
    "cover": ("Ancient Chinese emperor and a Buddhist monk sitting together translating scrolls, large translation team around them, library setting, traditional ink-wash painting style, warm gold and amber palette, scholarly atmosphere, ultra-detailed 8K"),
    "card1": ("Ancient Chinese battlefield, general Yao Chang capturing a fleeing enemy king, dramatic capture scene, traditional Chinese painting style, epic battle composition, 8K"),
    "card2": ("Ancient Chinese translation bureau, eight hundred monks debating a Sanskrit text, scrolls everywhere, traditional ink-wash style, intellectual atmosphere, 8K"),
    "card3": ("Ancient Chinese Buddhist temple, monks chanting sutras, golden statues, peaceful spiritual scene, traditional painting style, warm sacred tones, 8K"),
}
def gen(k):
    p = PROMPTS[k]; f = {"cover": COVER, "card1": CARDS[0], "card2": CARDS[1], "card3": CARDS[2]}[k]
    for a in range(3):
        r = requests.post(AGNES_URL, headers={"Authorization": f"Bearer {AGNES_KEY}", "Content-Type": "application/json"}, json={"model": "agnes-image-2.1-flash", "prompt": p, "n": 1, "size": f"{SRC_W}x{SRC_H}"}, timeout=120)
        if r.status_code == 200: break
        print(f"Attempt {a+1} failed: {r.status_code}", file=sys.stderr); time.sleep(5)
    else: raise RuntimeError(f"Failed {k}")
    ir = requests.get(r.json()["data"][0]["url"], timeout=120)
    with open(f"{f}.png","wb") as fp: fp.write(ir.content)
    print(f"{f}.png saved", file=sys.stderr)
def main():
    gen("cover")
    for k in ["card1","card2","card3"]: gen(k)
    print("ALL DONE", file=sys.stderr)
if __name__ == "__main__": main()