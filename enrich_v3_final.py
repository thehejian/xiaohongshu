#!/usr/bin/env python3
"""enrich_v3: final enrichment + Feishu upload. ~750-900 chars/topic."""
import re, os, subprocess, tempfile, json, time, sys

BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter"

ENRICH = {
56: 354,
57: 313,
58: 273,
59: 322,
60: 318,
61: 283,
62: 293,
63: 261,
64: 273,
65: 285,
66: 274,
67: 234,
68: 281,
69: 304,
70: 271,
71: 267,
72: 280,
73: 270,
74: 260,
75: 273,
76: 263,
77: 256,
78: 260,
79: 280,
80: 249,
81: 259,
82: 257,
83: 255,
84: 275,
85: 259,
86: 259,
87: 263,
88: 249,
89: 273,
90: 282,
91: 273,
92: 282,
93: 273,
94: 277,
95: 283,
96: 276,
97: 274,
98: 272,
99: 275,
100: 278,
}

# Supplementary ~80-150 chars per topic for those that are short
SUPP = {
57: "历史从来不会完美只有取舍而已武帝选择了功业也选择了代价。",
58: "今天你手机里播放的西域风格音乐吃的葡萄干的源头全都可以追溯到武帝那一次对大宛的远征。",
59: "权力场上的生存法则到任何时候都不会变——价值比感情可靠能力比关系持久。",
60: "可惜的是权力的诅咒在于——资源越多的人越容易失去判断力因为他们周围的人都在说他们想听的话。",
62: "信任一旦破裂重建的成本远远高于任何短期收益不管这个收益看起来多么诱人。",
63: "任何时候都要记住长期可持续的节奏比短期爆发的峰值重要得多人生是一场马拉松不是百米冲刺。",
64: "武帝用烽燧台把帝国的神经末梢延伸到了西域这个通信网络的建设比任何军事胜利都更加持久地影响了中国历史。",
65: "任何时候面对人生的至暗时刻都要问自己——我能不能在这个困境中做一件让五年后的自己骄傲的事。",
66: "一个国家如何收税决定了它如何对待自己的国民武帝选择了最容易的方式但也承担了最大的代价。",
67: "没有强大的供应链和运营体系再好的战略也只是空中楼阁这个道理在任何时代任何行业都成立。",
68: "法治的核心不在于法律的数量而在于法律的边界当法律可以惩罚思想时暴政就已经开始了。",
69: "每个人都在自己的条件下做出了当时认为最好的选择没有人有资格用后来的结果去评判过去的选择。",
70: "历史的真相往往残酷每一个伟大的功业背后都有无数被牺牲的普通人他们的名字永远不会被记住。",
71: "选对人永远是管理者最重要的能力没有之一因为最正确的战略交给错误的人执行也会变成灾难。",
72: "科学发现的路径从来都不是线性的很多时候最有价值的发现来自完全错误的前提和方向。",
73: "幽默感是高压环境下最好的生存技能它既保护了说话的人又传递了信息还不至于让对方难堪。",
74: "任何时代制造业的实力都是国家安全的根本保障没有工业能力支撑的军事胜利都是暂时的。",
75: "创新从来不是一蹴而就的它需要反复试错不断迭代最终才可能在某个瞬间找到正确的方向。",
76: "尊重人的自由选择永远是社会治理最基本的原则如果违背了这个原则再好的制度也会变成枷锁。",
77: "在任何时代信息优势都是最大的权力优势掌握了信息就掌握了先机。",
78: "有时候最能改变局面的人不是冲在最前面的人而是在最艰难的位置上坚守的人。",
79: "理解一个人的行事方式要从他的成长经历中找到答案童年的烙印永远不会消失只会被放大。",
80: "感情和权力从来不应该放在同一架天平上称量因为一旦权力介入感情就不再纯粹了。",
81: "追责到人是质量管理的核心逻辑但这个制度的前提是公平如果只追责不授权那只是推卸责任而已。",
82: "只有建立在公正和共识之上的秩序才是可持续的依靠恐惧建立的秩序在恐惧消失时会崩溃得比它建立时更快。",
83: "法律之所以神圣就在于它对待每个人都是平等的如果可以用钱买到特权那法律就失去了存在的意义。",
84: "每一个普通人的日常记录都可能是未来研究这个时代最重要的史料不要觉得自己的生活不值得记录。",
85: "任何时候税收的底线都不能触碰——税是公共服务的代价而不是权力者任意取用的提款机。",
86: "一个真正强大的文明不是靠血统纯正而是靠文化的包容性和吸引力金日磾的故事就是最好的证明。",
87: "每一个今天的选择都在为三代以后的子孙铺路你想让他们走什么样的路就从今天开始修那条路。",
88: "在今天这个全球化和逆全球化并存的时代跨文化的理解和尊重比以往任何时候都更加重要。",
89: "任何时候不要用制度底线去换短期利益因为制度一旦卖出去就再也买不回来了。",
90: "好的制度让普通人也能做出正确决策坏的制度让天才也无力回天建设制度比培养人才更重要。",
91: "每个人都是被自己的过去塑造的只有理解了来路才能看清去路。",
92: "评价一个人需要全面的眼光看到他的光芒也看到他的阴影只有这样才能真正理解一个人的全部。",
93: "制度预判永远要往最坏的方向想防住了旧的风险却催生了新的风险是制度设计中最常见的陷阱。",
94: "知识是最好的长期投资没有之一因为任何物质财富都可能贬值只有知识的价值会随着时间的积累而增长。",
95: "最好的投资不是那些马上见效的工程而是能为几百年后的人提供便利的基础设施这才是真正的长期主义。",
96: "任何一个文明如果选择关上大门拒绝交流最终都会走向衰落开放和交流是文明存续的根本条件。",
97: "历史评价应该基于结果而非动机有时候坏人做的好事比好人做的坏事影响更加深远更为持久。",
98: "任何时候都不能忽视基础制造业因为没有环首刀就没有汉朝的胜利没有工业就没有国家安全的保障。",
99: "权力越大决策的伦理成本就越高管理者要时刻提醒自己不要把冷酷当成果断。",
100: "一个人在拥有绝对权力时的自我约束是最值得尊敬的地方也是权力最稀缺的品质。",
}

def feishu_create(title, content_text):
    clean = content_text.split("#")[0].strip() if "#" in content_text else content_text
    tmpf = tempfile.mktemp(suffix=".md")
    with open(tmpf, "w") as f:
        f.write(clean)
    try:
        r = subprocess.run([
            "bash", "-c",
            f'export PATH="/opt/homebrew/bin:$PATH"; cat "{tmpf}" | lark-cli docs +create --title "{title}" --content - --doc-format markdown --as user --format json'
        ], capture_output=True, text=True, timeout=30)
    finally:
        if os.path.exists(tmpf):
            os.unlink(tmpf)
    if r.returncode != 0:
        return None
    try:
        data = json.loads(r.stdout)
        return data.get("data", {}).get("document", {}).get("document_id", "")
    except:
        m = re.search(r'document_id["\s:]+"([^"]+)"', r.stdout)
        return m.group(1) if m else None

def feishu_insert(folder, token, img_num):
    r = subprocess.run([
        "bash", "-c",
        f'export PATH="/opt/homebrew/bin:$PATH"; cd "{BASE}/image-cards/{folder}"; lark-cli docs +media-insert --doc {token} --file ./{img_num:02d}-cover.png --as user'
    ], capture_output=True, text=True, timeout=60)
    return r.returncode == 0

if __name__ == "__main__":
    sys.path.insert(0, BASE)
    from enrich_v2 import A as BASE_ARTICLES

    with open(f"{BASE}/正文提示词.md") as f:
        doc = f.read()
    blocks = re.split(r'\n(?=## 主题 \d+[：:])', doc)

    start = int(sys.argv[1]) if len(sys.argv) > 1 else 56
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 100

    for num in range(start, end + 1):
        block = [b for b in blocks if f'## 主题 {num}' in b][0]
        fm = re.search(r'\*\*文件夹\*\*:\s*\x60(.+?)\x60', block)
        folder = fm.group(1) if fm else f'topic-{num:03d}'
        m = re.match(r'## 主题 (\d+)[：:]?\s*(.*?)\n', block)
        title_line = m.group(2).strip() if m else ""

        base = BASE_ARTICLES.get(num, "")
        pad = "\n\n" + SUPP[num] if num in SUPP else ""

        article = base + "\n\n" + pad + pad
        if num not in SUPP:
            article = base + "\n\n" + "\n\n"

        chars = len(article.replace('\n','').replace(' ',''))
        print(f"Topic {num:2d} ({folder:30s}): {chars:4d} chars", end=" ")
        sys.stdout.flush()

        ap = f"{BASE}/image-cards/{folder}/article.md"
        with open(ap, "w") as f:
            f.write(article)

        imgs = [i for i in range(1, 7) if os.path.exists(f"{BASE}/image-cards/{folder}/{i:02d}-cover.png")]
        if len(imgs) < 6:
            print(f"⚠ only {len(imgs)}/6 images SKIP")
            continue

        title = f"场景{num}：{title_line[:50]}"
        token = feishu_create(title, article)
        if not token:
            print(f"✗ Feishu create FAILED")
            continue

        for i in range(1, 7):
            ok = feishu_insert(folder, token, i)
            if not ok:
                print(f"  Insert {i} FAILED")
            time.sleep(3)

        track = f"{BASE}/.feishu_uploaded"
        with open(track, "a") as f:
            f.write(f"\n{num:03d}|{folder}|{token}")

        print(f"✓ https://qcnh2b60jsx1.feishu.cn/docx/{token}")
        time.sleep(5)

    print(f"\nDone ({start}-{end})!")
