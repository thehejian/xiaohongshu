import requests, sys, time, os

AGNES_KEY = os.environ.get("AGNES_KEY", "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL = "https://apihub.agnes-ai.com/v1/images/generations"
SRC_W, SRC_H = 1024, 1024

COVER = "tdj-cover"
CARDS = ["tdj-card1", "tdj-card2", "tdj-card3"]

PROMPTS = {
    "cover": (
        "Ancient Chinese general on a battlefield at night, pouring grain from a sack onto a sand pile, "
        "soldiers carrying sandbags in background, torchlight illumination, "
        "traditional ink-wash painting style, Song dynasty aesthetic, dark blue and amber palette, "
        "epic cinematic composition, ultra-detailed, 8K"
    ),
    "card1": (
        "Ancient Chinese military camp at night, soldiers carrying sand under starlight, "
        "general standing on a hill watching, moonlit landscape, "
        "traditional Chinese painting style, misty atmosphere, muted earth tones, 8K"
    ),
    "card2": (
        "Ancient Chinese palace scene, general being arrested by imperial guards, "
        "angry expression tearing off his headdress, tragic atmosphere, "
        "traditional ink-wash style, crimson and dark gray tones, cinematic composition, 8K"
    ),
    "card3": (
        "Ancient Chinese battlefield map with troop movements, "
        "quote '走为上计' in ancient calligraphy style on a scroll, "
        "traditional painting style, warm parchment and ink tones, 8K"
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