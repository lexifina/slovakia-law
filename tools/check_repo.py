"""Checks the git repository against the official text: every version of every act in Slov-Lex, read back from git with
tools/ku_dnu.py on the day it took effect, must equal that version's consolidated text.

    python -X utf8 scripts/slovakia-law/check_repo.py [--repo ../slovakia-law] [--no-record]

Two checks per version, from the cached Slov-Lex HTML (no network):
1. File by file: the act's files in git on that day are exactly the files the build's parser makes from that version's
   HTML (same set of files, same bytes).
2. Word for word: the whole act printed by ku_dnu.py, with its markdown marks removed, has the same words in the same
   order as the whole official text, read independently of the parser (every text node of the act, its annexes and its
   footnotes on the page).
The result is written to verification.json next to this script (unless --no-record), for REPRODUCE.md.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

from lxml import html as lhtml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build  # noqa: E402

TOKEN = re.compile(r'\w+|[^\w\s]')


def official_words(raw: bytes) -> list[str]:
    """All words of the act on the page: the act (#predpis), its annexes (#prilohy) and its footnotes (#poznamky)."""
    doc = lhtml.fromstring(raw.decode('utf-8'))
    parts = []

    def text(e) -> str:
        # Inline elements (a footnote number in <sup>, a link) join the words around them as the page shows them;
        # block elements, line breaks and table cells separate words.
        if not isinstance(e.tag, str):
            return e.tail or ''
        gap = ' ' if e.tag in ('div', 'br', 'p', 'td', 'th', 'tr', 'table') else ''
        return gap + (e.text or '') + ''.join(text(c) for c in e) + gap + (e.tail or '')
    for ident in ('predpis', 'prilohy', 'poznamky'):
        try:
            e = doc.get_element_by_id(ident)
        except KeyError:
            continue
        e.tail = None
        parts.append(text(e))
    return TOKEN.findall(' '.join(parts).replace('\u00a0', ' '))


def repo_words(text: str) -> list[str]:
    lines = []
    for l in text.split('\n'):
        l = re.sub(r'^\s*(#+ |- )', '', l)
        lines.append(l.replace(' | ', ' '))   # the separator between the cells of a table row
    return TOKEN.findall(' '.join(lines))


def tool(repo: str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, 'tools/ku_dnu.py', *args], cwd=repo, capture_output=True, text=True,
                          encoding='utf-8')


def files_at(repo: str, commit: str, slug: str) -> dict[str, str]:
    """The act's files at a commit, read with one ls-tree and one cat-file --batch (not one git show per file)."""
    out = subprocess.run(['git', 'ls-tree', '-r', commit, f'{slug}/'], cwd=repo, capture_output=True,
                         text=True, encoding='utf-8').stdout.split('\n')
    blobs = []
    for line in out:
        if not line:
            continue
        info, f = line.split('\t', 1)
        if f.endswith('.md') and not f.endswith('/README.md'):
            blobs.append((f[len(slug) + 1:], info.split()[2]))
    if not blobs:
        return {}
    data = subprocess.run(['git', 'cat-file', '--batch'], cwd=repo, input=''.join(f'{sha}\n' for _, sha in blobs).encode(),
                          capture_output=True).stdout
    res, pos = {}, 0
    for name, _ in blobs:
        nl = data.index(b'\n', pos)
        size = int(data[pos:nl].split()[2])
        res[name] = data[nl + 1:nl + 1 + size].decode('utf-8')
        pos = nl + 1 + size + 1
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=str(build.ROOT.parent / 'slovakia-law'))
    ap.add_argument('--no-record', action='store_true')
    args = ap.parse_args()
    versions = files = bad = words = wbad = 0
    nwords = 0
    per_act = {}
    for act in build.ACTS:
        for v in build.history(act, offline=True):
            raw = build.fetch(v['url'], offline=True)
            parsed = build.read_version(raw)
            expected = {build.file_name(k): u['text'] for k, u in parsed['units'].items()}
            commit = subprocess.run([sys.executable, '-c', 'import sys; sys.path.insert(0, "tools"); import ku_dnu; '
                                     f'print(ku_dnu.commit_on("{v["from"]}", "{act["slug"]}"))'],
                                    cwd=args.repo, capture_output=True, text=True).stdout.strip()
            got = files_at(args.repo, commit, act['slug']) if commit else {}
            versions += 1
            per_act[act['slug']] = per_act.get(act['slug'], 0) + 1
            files += len(expected)
            if got != expected:
                bad += 1
                diff = sorted(set(got) ^ set(expected)) or [k for k in expected if got.get(k) != expected[k]]
                print(f'MISMATCH {act["slug"]} {v["from"]}: {diff[:5]}')
            whole = tool(args.repo, v['from'], act['slug'])
            words += 1
            ow, rw = official_words(raw), repo_words(whole.stdout)
            nwords += len(ow)
            if whole.returncode or ow != rw:
                wbad += 1
                i = next((i for i, (a, b) in enumerate(zip(ow, rw)) if a != b), min(len(ow), len(rw)))
                print(f'WORDS {act["slug"]} {v["from"]}: official {len(ow)} vs repo {len(rw)} words; first difference at '
                      f'{i}: {" ".join(ow[max(0, i - 5):i + 5])!r} / {" ".join(rw[max(0, i - 5):i + 5])!r}')
    print(f'{versions} versions checked ({files} files), {bad} mismatches; {words} versions word for word '
          f'({nwords} words), {wbad} mismatches')
    print('per act:', per_act)
    if not args.no_record:
        p = HERE / 'verification.json'
        rec = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
        rec['check'] = {'versions': versions, 'files': files, 'mismatches': bad, 'wordcheck': words,
                        'words': nwords, 'word_mismatches': wbad, 'per_act': per_act}
        p.write_text(json.dumps(rec, indent=1, sort_keys=True) + '\n', encoding='utf-8', newline='\n')
    raise SystemExit(1 if bad or wbad else 0)


if __name__ == '__main__':
    main()
