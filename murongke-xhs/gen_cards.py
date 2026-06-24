import requests, sys, time, os

AGNES_KEY = os.environ.get("AGNES_KEY", "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL = "https://apihub.agnes-ai.com/v1/images/generations"
SRC_W, SRC_H = 1024, 1024

COVER = "mrk-cover"
CARDS = ["mrk-card1", "mrk-card2", "mrk-card3"]

PROMPTS = {
    "cover": (
        "Ancient Chinese general in shining armor on horseback leading a cavalry charge, "
        "horses chained together with iron links, massive army behind, battlefield epic, "
        "traditional ink-wash painting style, Song dynasty aesthetic, steel blue and gold palette, "
        "epic cinematic composition, ultra-detailed, 8K"
    ),
    "card1": (
        "Ancient Chinese battlefield, two armies clashing, chained cavalry formation breaking enemy lines, "
        "general with white banner directing troops, "
        "traditional Chinese painting style, dramatic battle scene, 8K"
    ),
    "card2": (
        "Ancient Chinese palace, young general kneeling before the throne, "
        "prince offering the crown, refusal gesture, loyal minister scene, "
        "traditional ink-wash style, warm amber and gold tones, 8K"
    ),
    "card3": (
        "Ancient Chinese funeral scene for a great general, entire army mourning, "
        "white flags and banners, somber atmosphere, "
        "traditional painting style, muted gray and blue tones, melancholic composition, 8K"
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