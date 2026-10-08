# -*- coding: utf-8 -*-
"""XHS 三步查重法固化 — 对应指南第四章。

用法:
    python3 tools/xhs_dedup.py 454                # 按素材库主题号查（自动取该主题标题作关键词）
    python3 tools/xhs_dedup.py 关羽 水淹七军       # 直接给关键词查

三步:
    1. 正文提示词.md 近期主题 + 关键词命中（主体重叠候选）
    2. grep image-cards/*/article.md 已有成文
    3. grep /tmp/xhs_drafts.txt 草稿箱缓存（缺失时提示重拉命令）

退出码: 0 = 无重复; 1 = 发现重复/候选; 2 = 用法错误/主题号不存在
"""
import glob
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPTS_FILE = os.path.join(REPO, '正文提示词.md')
DRAFTS_CACHE = '/tmp/xhs_drafts.txt'
DRAFTS_REFRESH = 'opencli xiaohongshu drafts -f plain --site-session persistent --keep-tab true | tee /tmp/xhs_drafts.txt'

RECENT_WINDOW = 15  # 步骤1：比对最近 N 个主题


def load_topics():
    """返回 {topic_num: raw_block}。按 re.split 分块（铁律：禁止 find 定位）。"""
    with open(PROMPTS_FILE, encoding='utf-8') as f:
        content = f.read()
    parts = re.split(r'(?m)^## 主题 ', content)
    topics = {}
    for p in parts[1:]:
        m = re.match(r'(\d+)', p)
        if m:
            topics[int(m.group(1))] = p
    return topics


def terms_from_topic(topics, num):
    if num not in topics:
        return None, None
    block = topics[num]
    first_lines = [l.strip() for l in block.split('\n')[:5] if l.strip()]
    title = ''
    for l in first_lines:
        if l.startswith('#') or l.startswith('**') or l.startswith('###'):
            continue
        title = l
        break
    raw = [t for t in re.split(r'[：:——、，,。.·\s「」\[\]【】()（）]+', title) if len(t) >= 2]
    # 丢弃纯数字（如编号本身）与超长分句（grep 无区分度），其余作关键词
    terms = [t for t in raw if not t.isdigit() and len(t) <= 8 and t != str(num)]
    return title, terms


def recent_topics(topics, num, window=RECENT_WINDOW):
    nums = sorted(topics)
    idx = nums.index(num) if num in nums else len(nums) - 1
    return nums[max(0, idx - window):idx]


def grep_articles(terms, topn=8, rare_thresh=3):
    """按区分度打分：命中词数多、或命中稀缺词 → 强候选。

    返回 (strong_hits, weak_summary, term_counts)
      strong: [(folder, [term,...], snippet), ...] 按分数降序
      weak_summary: {term: article_count} 仅低区分度词命中的统计
    """
    per_article = {}   # folder -> (set(terms), snippet)
    term_articles = {t: set() for t in terms}
    for path in sorted(glob.glob(os.path.join(REPO, 'image-cards', '*', 'article.md'))):
        try:
            with open(path, encoding='utf-8') as f:
                lines = f.read().split('\n')
        except Exception:
            continue
        matched, snippet = set(), ''
        for line in lines:
            for t in terms:
                if t in line and t not in matched:
                    matched.add(t)
                    if not snippet:
                        snippet = line.strip()[:50]
        if matched:
            rel = os.path.relpath(os.path.dirname(path), REPO)
            per_article[rel] = (matched, snippet)
            for t in matched:
                term_articles[t].add(rel)

    term_counts = {t: len(s) for t, s in term_articles.items()}
    strong, weak_terms = [], set()
    for rel, (matched, snippet) in per_article.items():
        rare = [t for t in matched if term_counts[t] <= rare_thresh]
        if len(matched) >= 2 or rare:
            strong.append((rel, sorted(matched), snippet))
        else:
            weak_terms.update(matched)
    strong.sort(key=lambda x: (-len(x[1]), x[0]))
    weak_summary = {t: term_counts[t] for t in sorted(weak_terms)}
    return strong[:topn], weak_summary, term_counts


def grep_prompts(topics, terms, exclude_num):
    """返回 (strong_hits, old_weak_count)。

    strong = 命中 ≥2 个词，或命中稀缺词（该词在素材库 ≤10 个主题中出现）。
    远期主题的单个常见词命中不报（如"洛阳"遍布百个主题）。
    """
    term_topic_counts = {t: 0 for t in terms}
    for block in topics.values():
        for t in terms:
            if t in block:
                term_topic_counts[t] += 1
    strong, old_weak = [], 0
    for num, block in topics.items():
        if num == exclude_num:
            continue
        found = [t for t in terms if t in block]
        if not found:
            continue
        rare = [t for t in found if term_topic_counts[t] <= 10]
        if len(found) >= 2 or rare:
            strong.append((num, found))
        else:
            old_weak += 1
    return strong, old_weak


def grep_drafts(terms):
    if not os.path.exists(DRAFTS_CACHE):
        return None
    hits = []
    with open(DRAFTS_CACHE, encoding='utf-8', errors='replace') as f:
        for line in f:
            matched = [t for t in terms if t in line]
            if matched:
                hits.append((matched, line.strip()[:60]))
    return hits


def main(argv):
    if not argv:
        print(__doc__)
        return 2

    topics = load_topics()
    exclude_num = None
    extra = [a for a in argv if not a.isdigit()]
    digits = [a for a in argv if a.isdigit()]
    if digits:
        exclude_num = int(digits[0])
        title, terms = terms_from_topic(topics, exclude_num)
        if terms is None:
            print('素材库中不存在主题 %s（检查 正文提示词.md 编号）' % digits[0])
            return 2
        terms += [a for a in extra if len(a) >= 2]
        print('主题 %d 原题: %s' % (exclude_num, title))
        print('关键词: %s' % (' / '.join(terms) or '（无有效关键词，建议追加）'))
        if not terms:
            return 2
    else:
        terms = [a for a in argv if len(a) >= 2]
        if not terms:
            print('关键词至少 2 个字符')
            return 2

    dup = False

    # 步骤 1：素材库近期主题 + 关键词命中
    if exclude_num is not None:
        recents = set(recent_topics(topics, exclude_num))
        print('\n[1/3] 素材库近期主题: %s' % ', '.join(str(n) for n in sorted(recents)))
    else:
        recents = set()
    strong_all, old_weak = grep_prompts(topics, terms, exclude_num)
    recent_hit = [(n, f) for n, f in sorted(strong_all) if n in recents]
    old_hit = [(n, f) for n, f in sorted(strong_all) if n not in recents]
    if recent_hit:
        dup = True
        print('[1/3] ⚠ 近期主题命中（同人物/事件即候选）:')
        for n, found in recent_hit[:10]:
            print('        主题 %d ← %s' % (n, '/'.join(found)))
    elif old_hit:
        print('[1/3] 近期主题无命中 ✓（远期素材库强命中 %d 个，仅参考: %s）'
              % (len(old_hit), ', '.join(str(n) for n, _ in old_hit[:8])))
    else:
        print('[1/3] 素材库无强命中 ✓%s'
              % ('（弱命中 %d 个主题略）' % old_weak if old_weak else ''))

    # 步骤 2：已有成文（按区分度分级）
    strong, weak_summary, term_counts = grep_articles(terms)
    if strong:
        dup = True
        print('[2/3] ⚠ 已有成文强候选（多词命中或稀缺词命中）:')
        for rel, matched, snippet in strong:
            print('        %s/article.md  ← %s' % (rel, '/'.join(matched)))
            print('            %s' % snippet)
    else:
        print('[2/3] 无强候选 ✓')
    if weak_summary:
        parts = ['%s(%d篇)' % (t, c) for t, c in weak_summary.items()]
        print('        低区分度词命中（参考）: %s' % ' '.join(parts))

    # 步骤 3：草稿箱缓存
    draft_hits = grep_drafts(terms)
    if draft_hits is None:
        print('[3/3] 草稿缓存缺失（/tmp 可能被清空），需要时重拉:')
        print('        %s' % DRAFTS_REFRESH)
    elif draft_hits:
        dup = True
        print('[3/3] ⚠ 草稿箱命中:')
        for matched, line in draft_hits[:10]:
            print('        [%s] %s' % ('/'.join(matched), line))
    else:
        print('[3/3] 草稿箱无命中 ✓')

    print('\n结论: %s' % ('发现重复候选 → 按指南4.2判定，可能需跳过该号' if dup else '未发现重复 ✓'))
    return 1 if dup else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
