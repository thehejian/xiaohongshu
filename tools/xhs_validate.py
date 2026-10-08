# -*- coding: utf-8 -*-
"""XHS article.md 校验器 — 对应指南第三章「格式硬性要求」三条命令的固化。

用法:
    python3 tools/xhs_validate.py image-cards/topic-453/article.md
    python3 tools/xhs_validate.py --json image-cards/topic-453/article.md
    cat article.md | python3 tools/xhs_validate.py -   # stdin

退出码: 0 = 无 error（warning 可接受）; 1 = 存在 error

导入用法（供后续 LangGraph 节点调用）:
    from xhs_validate import validate
    result = validate(open('article.md').read())
    result['errors'] / result['warnings'] / result['ok']
"""
import json
import re
import sys

BOUNDED_SECTIONS = ['后世影响', '现代启示']


def _title_check(lines):
    errors, warnings = [], []
    if not lines:
        return ['文章为空'], warnings
    title = lines[0].strip()
    if not title:
        errors.append('第1行为空 — 必须是独立标题行')
        return errors, warnings
    if len(title) > 20:
        errors.append('标题 %d 字 > 20 字上限: %s' % (len(title), title))
    if len(title) < 4:
        warnings.append('标题过短 (%d 字): %s' % (len(title), title))
    if re.search(r'[a-zA-Z0-9]', title):
        errors.append('标题含英文/数字（须全中文）: %s' % title)
    return errors, warnings


def _format_check(lines):
    errors, warnings = [], []
    if len(lines) >= 2 and lines[1].strip() != '':
        warnings.append('第2行不是空行（建议标题后空一行）')
    return errors, warnings


def _char_count(text):
    return len(text.replace('\n', '').replace(' ', ''))


def _count_check(text):
    n = _char_count(text)
    if n < 700:
        return ['全文 %d 字 < 700 — 必须扩写主叙事' % n], [], n
    if n < 750:
        return [], ['全文 %d 字，低于目标区间 750–900' % n], n
    if n <= 900:
        return [], [], n
    if n <= 950:
        return [], ['全文 %d 字，超出目标区间 750–900（XHS 上限 950 内，可发）' % n], n
    return ['全文 %d 字 > 950 — 超出 XHS 上限' % n], [], n


def _english_check(lines):
    errors = []
    for i, line in enumerate(lines[2:], start=3):
        for m in re.finditer(r'[a-zA-Z]{2,}', line):
            errors.append('第%d行混入英文 "%s": %s' % (i, m.group(), line[:40]))
    return errors


def _structure_check(lines):
    warnings = []
    body = '\n'.join(lines[2:])
    paras = [p for p in re.split(r'\n\s*\n', body) if p.strip()]
    if len(paras) < 3 or len(paras) > 7:
        warnings.append('正文段落数 %d（要求 5±2 段）' % len(paras))
    return warnings, len(paras)


def _section_check(text):
    return ['正文含已废除章节: %s' % s for s in BOUNDED_SECTIONS if s in text]


def _tag_check(lines):
    last = ''
    for line in reversed(lines):
        if line.strip():
            last = line.strip()
            break
    if not last.startswith('#'):
        return ['末行不是 #话题 tags（当前末行: %s）' % last[:30]]
    return []


def validate(text):
    lines = text.split('\n')
    errors, warnings = [], []

    e, w = _title_check(lines); errors += e; warnings += w
    e, w = _format_check(lines); errors += e; warnings += w
    e, w, n_chars = _count_check(text); errors += e; warnings += w
    errors += _english_check(lines)
    errors += _section_check(text)
    para_warnings, n_paras = _structure_check(lines)
    warnings += para_warnings
    errors += _tag_check(lines)

    return {
        'ok': not errors,
        'errors': errors,
        'warnings': warnings,
        'title': lines[0].strip() if lines else '',
        'title_len': len(lines[0].strip()) if lines else 0,
        'char_count': n_chars,
        'paragraphs': n_paras,
    }


def _report(r, path):
    print('== %s ==' % path)
    print('标题: %s（%d 字）' % (r['title'], r['title_len']))
    print('字数: %d  段落: %d' % (r['char_count'], r['paragraphs']))
    for e in r['errors']:
        print('  [ERROR] %s' % e)
    for w in r['warnings']:
        print('  [WARN]  %s' % w)
    print('结果: %s' % ('PASS ✓' if r['ok'] else 'FAIL ✗ (%d errors)' % len(r['errors'])))


def main(argv):
    as_json = '--json' in argv
    args = [a for a in argv if a != '--json']
    if not args:
        print('用法: xhs_validate.py [--json] <article.md | ->')
        return 2
    path = args[0]
    if path == '-':
        text = sys.stdin.read()
        path = '<stdin>'
    else:
        with open(path, encoding='utf-8') as f:
            text = f.read()
    r = validate(text)
    if as_json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        _report(r, path)
    return 0 if r['ok'] else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
