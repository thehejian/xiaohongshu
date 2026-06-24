import requests, sys, time, os

AGNES_KEY = os.environ.get("AGNES_KEY", "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL = "https://apihub.agnes-ai.com/v1/images/generations"
SRC_W, SRC_H = 1024, 1024

COVER = "hlbb-cover"
CARDS = ["hlbb-card1", "hlbb-card2", "hlbb-card3"]

PROMPTS = {
    "cover": (
        "Ancient Chinese fortress city in desert, massive white walls gleaming under the sun, "
        "Hunnic/Xiongnu architecture, watchtowers and battlements, "
        "traditional ink-wash painting style, desert sand and white stone palette, "
        "epic panoramic view, ultra-detailed, 8K"
    ),
    "card1": (
        "Ancient Chinese construction scene, thousands of workers building a city wall, "
        "iron cauldrons steaming sticky rice mortar, overseers with whips, "
        "traditional Chinese painting style, harsh labor atmosphere, 8K"
    ),
    "card2": (
        "Ancient Chinese king testing a wall with an iron awl, executed workers lying nearby, "
        "ruthless expression, brutal construction site, "
        "traditional ink-wash style, dark and menacing composition, 8K"
    ),
    "card3": (
        "Modern aerial view of an ancient fortress in the Gobi Desert, "
        "well-preserved white walls still standing, archaeological wonder, "
        "documentary photography style, golden hour lighting, 8K"
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