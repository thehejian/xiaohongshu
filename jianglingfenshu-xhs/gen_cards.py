import requests, sys, time, os

AGNES_KEY = os.environ.get("AGNES_KEY", "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL = "https://apihub.agnes-ai.com/v1/images/generations"
SRC_W, SRC_H = 1024, 1024

COVER = "jlf-cover"
CARDS = ["jlf-card1", "jlf-card2", "jlf-card3"]

PROMPTS = {
    "cover": (
        "Ancient Chinese palace library in flames, a man in imperial robes watching books burn, "
        "scrolls turning to ash, smoke rising, tragic atmosphere, "
        "traditional ink-wash painting style, Song dynasty aesthetic, dark red and gray palette, "
        "epic cinematic composition, ultra-detailed, 8K"
    ),
    "card1": (
        "Ancient Chinese scholar-emperor writing poetry in a grand library, "
        "thousands of scrolls on shelves behind him, candlelight, "
        "traditional Chinese painting style, warm amber and gold tones, 8K"
    ),
    "card2": (
        "Ancient Chinese city under siege, soldiers breaking through gates, "
        "fire and smoke rising, desperate defenders, epic battle scene, "
        "traditional ink-wash style, crimson and dark tones, cinematic composition, 8K"
    ),
    "card3": (
        "Ancient Chinese palace after destruction, charred scroll fragments scattered, "
        "an empty throne in darkness, ashes floating in air, "
        "traditional painting style, muted gray and brown tones, melancholic atmosphere, 8K"
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