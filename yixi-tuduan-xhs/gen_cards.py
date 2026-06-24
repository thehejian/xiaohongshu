import requests, sys, time, os

AGNES_KEY = os.environ.get("AGNES_KEY", "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL = "https://apihub.agnes-ai.com/v1/images/generations"
SRC_W, SRC_H = 1024, 1024

COVER = "yxtd-cover"
CARDS = ["yxtd-card1", "yxtd-card2", "yxtd-card3"]

PROMPTS = {
    "cover": (
        "Ancient Chinese government office, officials registering peasants in census records, "
        "scrolls and stamps everywhere, imperial decree being read, "
        "traditional ink-wash painting style, Song dynasty aesthetic, warm brown and gold palette, "
        "documentary-style composition, ultra-detailed, 8K"
    ),
    "card1": (
        "Ancient Chinese aristocratic manor, wealthy landlords counting coins, "
        "hidden peasants behind screens, contrast of rich and poor, "
        "traditional Chinese painting style, decadent gold and shadow tones, 8K"
    ),
    "card2": (
        "Ancient Chinese emperor in military armor reviewing census scrolls with generals, "
        "tax collection scene, soldiers standing guard, "
        "traditional ink-wash style, authoritative composition, deep red and gold, 8K"
    ),
    "card3": (
        "Ancient Chinese farmland with peasants working, "
        "government officials measuring land with ropes, rural landscape, "
        "traditional painting style, peaceful pastoral tones, warm amber and green, 8K"
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