import requests, sys, time, os
AGNES_KEY = os.environ.get("AGNES_KEY", "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL = "https://apihub.agnes-ai.com/v1/images/generations"
SRC_W, SRC_H = 1024, 1024
COVER = "zg-cover"
CARDS = ["zg-card1", "zg-card2", "zg-card3"]
PROMPTS = {
    "cover": ("Ancient Chinese frontier city on the Silk Road, scholars and students in a library, camel caravans passing by outside, traditional ink-wash painting style, warm desert and jade palette, peaceful cultural oasis atmosphere, ultra-detailed 8K"),
    "card1": ("Ancient Chinese governor building schools in a frontier town, Confucian scholars teaching students, traditional Chinese painting style, scholarly prosperity, 8K"),
    "card2": ("Ancient Chinese oasis market town on the Silk Road, merchants from different cultures trading, bustling harmonious scene, traditional ink-wash style, 8K"),
    "card3": ("Ancient Chinese court musicians playing traditional instruments, elegant performance, cultural heritage scene, traditional painting style, gold and amber tones, 8K"),
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