import requests, sys, time, os

AGNES_KEY = os.environ.get("AGNES_KEY", "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL = "https://apihub.agnes-ai.com/v1/images/generations"
SRC_W, SRC_H = 1024, 1024

COVER = "ycsw-cover"
CARDS = ["ycsw-card1", "ycsw-card2", "ycsw-card3"]

PROMPTS = {
    "cover": (
        "Ancient Chinese underground water system beneath a city wall, intricate brick tunnels "
        "with flowing water, torchlight illuminating engineering, "
        "traditional ink-wash painting style, dark blue and stone gray palette, "
        "archaeological cross-section view, ultra-detailed, 8K"
    ),
    "card1": (
        "Ancient Chinese city Ye, massive walls with water moats and floodgate system, "
        "water cascading from city gates, misty landscape, "
        "traditional Chinese painting style, panoramic view, amber and gray tones, 8K"
    ),
    "card2": (
        "Ancient Chinese underground passageway, secret escape tunnel with candlelight, "
        "brick arches and stone steps, hidden door mechanism, "
        "traditional painting style, dark warm tones, mysterious atmosphere, 8K"
    ),
    "card3": (
        "Modern archaeological excavation of ancient Ye city underground water system, "
        "revealing brick tunnels and ceramic pipes, "
        "documentary photography style mixed with traditional aesthetic, 8K"
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