import requests, sys, time, os

AGNES_KEY = os.environ.get("AGNES_KEY", "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect")
AGNES_URL = "https://apihub.agnes-ai.com/v1/images/generations"
W = H = 1024

prefix = "cc"
cover_name = f"{prefix}-cover"
cards = [f"{prefix}-card1", f"{prefix}-card2", f"{prefix}-card3"]

prompts = {
    "cover": "A small Caribbean island nation map on vintage world map background, Curacao flag waving, tiny island with turquoise waters, football at the center, cream background #FAF7F2 with deep text #1E293B, elegant infographic style, ultra-detailed 8K",
    "card1": "Map of Curacao island in Caribbean Sea, close to Venezuela coast, showing its small size with only 150,000 population, vintage nautical map style with blue turquoise sea, cream background, ultra-detailed 8K",
    "card2": "Curacao national football team in blue jerseys playing on a Caribbean beach stadium, players of Dutch descent with strong homeland passion, sunset over turquoise Caribbean waters, ultra-detailed 8K",
    "card3": "Football with FIFA flag replacing national flag, a small island team waiting for recognition, emotional sports moment, cream background with deep text labels, ultra-detailed 8K",
}

def generate(key):
    prompt = prompts[key]
    names = {"cover": cover_name, "card1": cards[0], "card2": cards[1], "card3": cards[2]}[key]

    for attempt in range(3):
        r = requests.post(
            AGNES_URL,
            headers={"Authorization": f"Bearer {AGNES_KEY}", "Content-Type": "application/json"},
            json={"model": "agnes-image-2.1-flash", "prompt": prompt, "n": 1, "size": f"{W}x{H}"},
            timeout=120
        )
        if r.status_code == 200:
            break
        time.sleep(5)
    else:
        raise RuntimeError(f"Failed to generate {key}")

    url = r.json()["data"][0]["url"]
    img = requests.get(url, timeout=120)
    filepath = f"{names}.png"
    with open(filepath, "wb") as f:
        f.write(img.content)
    print(f"{filepath} saved", file=sys.stderr)

def main():
    generate("cover")
    for k in ["card1", "card2", "card3"]:
        generate(k)
    print("ALL DONE", file=sys.stderr)

if __name__ == "__main__":
    main()
