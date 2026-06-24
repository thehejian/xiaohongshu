import requests, sys, time, os

AGNES_KEY = os.environ.get("AGNES_KEY", "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL = "https://apihub.agnes-ai.com/v1/images/generations"
SRC_W, SRC_H = 1024, 1024

COVER = "lz-cover"
CARDS = ["lz-card1", "lz-card2", "lz-card3"]

PROMPTS = {
    "cover": (
        "Ancient Chinese oasis city on the Silk Road, Dunhuang, Buddhist cave temples, "
        "caravans of camels entering a bustling market town, desert mountains in background, "
        "traditional ink-wash painting style, warm sand and jade green palette, "
        "epic panoramic composition, ultra-detailed, 8K"
    ),
    "card1": (
        "Ancient Chinese library in Dunhuang, scholars copying scrolls, "
        "Confucian classics piled on desks, traditional study scene, "
        "traditional painting style, warm amber and parchment tones, 8K"
    ),
    "card2": (
        "Ancient Silk Road market scene, merchants from Central Asia trading spices and silk, "
        "multilingual bustling bazaar, traditional painting style, "
        "vibrant earth tones, cultural fusion atmosphere, 8K"
    ),
    "card3": (
        "Ancient Chinese court musicians playing pipa and flute, "
        "Liangzhou music performance, traditional instruments, "
        "ink-wash painting style, warm gold tones, cultural elegance, 8K"
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