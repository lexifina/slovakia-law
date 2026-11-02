"""Check the acts appended as their current version (data/ucinne-predpisy.csv) against the repository itself.

    python -X utf8 tools/check_wave3.py [--repo .]

Needs only git and Python; reads no network. For every act in the table: its folder holds the listed number of law
files; every image and annex PDF linked from its files is in its assets/ folder, named by the sha256 of its bytes,
and listed in data/assets.tsv; the images and PDFs the table counts are each linked or marked "[Image omitted: ...]";
no file holds an unresolved link. For every commit that added an act: Kind is law or baseline, it carries In-force,
In-force-basis, Text-as-of and Text-source, and its committer date is its author date. Prints one line per failure
and a summary; exits 1 on any failure.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
import subprocess
import sys
from pathlib import Path

LINK = re.compile(r'\]\(((?:\.\./)*)assets/([0-9a-f]{64})\.([a-z0-9]+)\)')


def git(repo: Path, *args: str) -> bytes:
    return subprocess.run(['git', *args], cwd=repo, capture_output=True, check=True).stdout


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default='.')
    repo = Path(ap.parse_args().repo)
    rows = list(csv.DictReader(io.StringIO(git(repo, 'show', 'HEAD:data/ucinne-predpisy.csv').decode('utf-8'))))
    tree: dict[str, str] = {}
    for rec in git(repo, 'ls-tree', '-r', '-z', 'HEAD').split(b'\0'):
        if rec:
            meta, path = rec.decode('utf-8').split('\t', 1)
            tree[path] = meta.split()[2]
    listed = {}
    try:
        for r in csv.DictReader(io.StringIO(git(repo, 'show', 'HEAD:data/assets.tsv').decode('utf-8')), delimiter='\t'):
            listed[r['path']] = r
    except subprocess.CalledProcessError:
        pass
    fails = []
    for r in rows:
        act = r['priecinok']
        law = [p for p in tree if p.startswith(act + '/') and '/assets/' not in p]
        if str(len(law)) != r['subory']:
            fails.append(f'{act}: {len(law)} law files, the table says {r["subory"]}')
        links = notices = 0
        for p in law:
            text = git(repo, 'cat-file', 'blob', tree[p]).decode('utf-8')
            if '⟦' in text:
                fails.append(f'{p}: unresolved asset token')
            notices += text.count('[Image omitted: ')
            for up, sha, ext in LINK.findall(text):
                links += 1
                if len(up) // 3 != p.count('/') - 1:
                    fails.append(f'{p}: asset link {up}assets/{sha}.{ext} does not resolve from this folder')
                a = f'{act}/assets/{sha}.{ext}'
                if a not in tree:
                    fails.append(f'{p}: links {a}, which is not in the tree')
                    continue
                if hashlib.sha256(git(repo, 'cat-file', 'blob', tree[a])).hexdigest() != sha:
                    fails.append(f'{a}: bytes do not match the sha256 in its name')
                if a not in listed:
                    fails.append(f'{a}: not in data/assets.tsv')
        want = int(r.get('obrazky') or 0) + int(r.get('prilohy_pdf') or 0)
        if r.get('obrazky', '') != '' and links + notices != want:
            fails.append(f'{act}: {want} images/PDFs counted, {links} linked and {notices} marked omitted')
    fmt = '%H%x09%(trailers:key=Kind,valueonly,separator=)%x09%(trailers:key=In-force,valueonly,separator=)%x09' \
          '%(trailers:key=In-force-basis,valueonly,separator=)%x09%(trailers:key=Text-as-of,valueonly,separator=)%x09' \
          '%(trailers:key=Text-source,valueonly,separator=)%x09%ad%x09%cd'
    sources = {r['zdroj'] for r in rows}
    seen = 0
    for line in git(repo, 'log', f'--format={fmt}', '--date=iso-strict', 'HEAD').decode('utf-8').splitlines():
        f = line.split('\t')
        if f[5] not in sources or not f[5]:
            continue
        seen += 1
        if f[1] not in ('law', 'baseline'):
            fails.append(f'{f[0][:10]}: Kind {f[1]!r}, not law or baseline')
        if not (f[2] and f[3] and f[4]):
            fails.append(f'{f[0][:10]}: missing In-force, In-force-basis or Text-as-of')
        if f[6] != f[7]:
            fails.append(f'{f[0][:10]}: committer date {f[7]} is not the author date {f[6]}')
    if seen < len(rows):
        fails.append(f'{len(rows) - seen} listed acts have no commit with their Text-source')
    for line in fails:
        print('FAIL', line)
    print(f'{len(rows)} acts, {len(listed)} assets listed, {seen} commits checked, {len(fails)} failures')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
