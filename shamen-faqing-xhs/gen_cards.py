import requests, sys, time, os

AGNES_KEY = os.environ.get("AGNES_KEY", "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL = "https://apihub.agnes-ai.com/v1/images/generations"
SRC_W, SRC_H = 1024, 1024

COVER = "smfq-cover"
CARDS = ["smfq-card1", "smfq-card2", "smfq-card3"]

PROMPTS = {
    "cover": (
        "Ancient Chinese Buddhist monk leading a rebel army, burning temple in background, "
        "yellow-robed followers with weapons, chaotic battlefield, "
        "traditional ink-wash painting style, dark crimson and smoke gray palette, "
        "epic dramatic composition, ultra-detailed, 8K"
    ),
    "card1": (
        "Ancient Chinese Buddhist monastery on fire, monks fleeing, "
        "scriptures burning, smoke rising to heaven, "
        "traditional Chinese painting style, apocalyptic atmosphere, 8K"
    ),
    "card2": (
        "Ancient Chinese battlefield, Buddhist rebel army charging imperial forces, "
        "yellow banners with '大乘' characters, chaotic melee, "
        "traditional ink-wash style, dramatic action scene, 8K"
    ),
    "card3": (
        "Ancient Chinese imperial court, officials debating religious policy, "
        "emperor looking troubled, scrolls of Buddhist law on table, "
        "traditional painting style, tense political atmosphere, 8K"
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