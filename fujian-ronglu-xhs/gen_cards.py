import requests, sys, time, os
AGNES_KEY = os.environ.get("AGNES_KEY", "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL = "https://apihub.agnes-ai.com/v1/images/generations"
SRC_W, SRC_H = 1024, 1024
COVER = "fjrl-cover"
CARDS = ["fjrl-card1", "fjrl-card2", "fjrl-card3"]
PROMPTS = {
    "cover": ("Ancient Chinese emperor in dragon robe sitting on throne surrounded by officials of different ethnicities, Xianbei, Han, Qiang, Jie all together, traditional ink-wash painting style, warm gold and diverse palette, epic harmonious scene, ultra-detailed 8K"),
    "card1": ("Ancient Chinese battlefield on the Fei River, massive army crossing a river, banners and flags everywhere, epic scale battle scene, traditional Chinese painting style, misty river landscape, 8K"),
    "card2": ("Ancient Chinese court, loyal minister Wang Meng on his deathbed warning the emperor, emperor looking conflicted, tragic atmosphere, traditional ink-wash style, 8K"),
    "card3": ("Ancient Chinese emperor in captivity, former vassals rebelling, broken crown on ground, sad lonely figure, traditional painting style, melancholic tones, 8K"),
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