import requests, sys, time, os

AGNES_KEY = os.environ.get("AGNES_KEY", "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL = "https://apihub.agnes-ai.com/v1/images/generations"
SRC_W, SRC_H = 1024, 1024

COVER = "bjs-cover"
CARDS = ["bjs-card1", "bjs-card2", "bjs-card3"]

PROMPTS = {
    "cover": (
        "Ancient Korean and Chinese ships meeting on the Yellow Sea, envoys exchanging gifts, "
        "traditional Korean Baekje and Silla ships alongside Chinese junks, "
        "traditional ink-wash painting style with Korean influence, sea and sky palette, "
        "peaceful diplomatic scene, epic panoramic view, ultra-detailed, 8K"
    ),
    "card1": (
        "Ancient Korean royal court, king receiving Chinese envoys, "
        "traditional Korean architecture, silk and gold gifts on display, "
        "traditional Korean painting style, warm ceremonial tones, 8K"
    ),
    "card2": (
        "Ancient Chinese Buddhist temple, Korean monks studying scriptures with Chinese masters, "
        "scrolls and statues, peaceful scholarly atmosphere, "
        "traditional painting style, warm gold and amber tones, 8K"
    ),
    "card3": (
        "Ancient Chinese Nanjing harbor, Korean embassy ships docking, "
        "city walls and pagodas visible, merchants unloading cargo, "
        "traditional painting style, bustling port scene, 8K"
    ),
}

def gen(prompt_key):
    prompt = PROMPTS[prompt_key]
    fname = {"cover": COVER, "card1": CARDS[0], "card2": CARDS[1], "card3": CARDS[2]}[prompt_key]
    for attempt in range(3):
        r = requests.post(AGNES_URL, headers={"Authorization": f"Bearer {AGNES_KEY}", "Content-Type": "application/json"}, json={"model": "agnes-image-2.1-flash", "prompt": prompt, "n": 1, "size": f"{SRC_W}x{SRC_H}"}, timeout=120)
        if r.status_code == 200:
            break
        print(f"Attempt {attempt+1} failed: {r.status_code}", file=sys.stderr)
        time.sleep(5)
    else:
        raise RuntimeError(f"Failed for {prompt_key}")
    url = r.json()["data"][0]["url"]
    ir = requests.get(url, timeout=120)
    out = f"{fname}.png"
    with open(out, "wb") as f:
        f.write(ir.content)
    print(f"{out} saved", file=sys.stderr)

def main():
    gen("cover")
    for k in ["card1", "card2", "card3"]:
        gen(k)
    print("ALL DONE", file=sys.stderr)

if __name__ == "__main__":
    main()