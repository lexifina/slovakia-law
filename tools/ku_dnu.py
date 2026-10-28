"""Prints an act, or one provision of it, as it stood on a given day, from this repository's history.

    python tools/ku_dnu.py 2010-01-01 ustava 7             # čl. 7 of the Constitution on 1 January 2010
    python tools/ku_dnu.py 2020-01-01 ustava               # the whole Constitution on 1 January 2020
    python tools/ku_dnu.py 2018-01-01 volebny-zakon 4      # § 4 of Act 180/2014 on 1 January 2018
    python tools/ku_dnu.py 2018-01-01 volebny-zakon poznamky

Each commit carries the day its change took effect in an `In-force:` trailer (git cannot store dates before 1970, so
the trailer, not the commit date, is the source of truth). The text in force on a day is the last commit on or before
it. Changes published but not yet in force would be on the branch "buduce"; a date after today reads from there.
Standard library only.
"""
import datetime as dt
import re
import subprocess
import sys


def git(*args: str) -> str:
    return subprocess.run(['git', *args], capture_output=True, text=True, encoding='utf-8', check=True).stdout


def order(path: str) -> tuple:
    """The order of the act's files: opening, articles or sections by number, articles of the act, closing words,
    annexes, footnotes."""
    name = path.split('/', 1)[1][:-3]
    if name == 'uvod':
        return (0, 0, '', '')
    m = re.fullmatch(r'(cl|par)-(\d+)([a-z]*)(.*)', name)
    if m:
        return (1, int(m.group(2)), f'{len(m.group(3)):02d}{m.group(3)}', m.group(4))
    m = re.fullmatch(r'clanok-(\d+)([a-z]*)(.*)', name)
    if m:
        return (2, int(m.group(1)), f'{len(m.group(2)):02d}{m.group(2)}', m.group(3))
    if name == 'zaver':
        return (3, 0, '', '')
    m = re.fullmatch(r'prilohy/priloha-(\d+)([a-z]*)', name)
    if m:
        return (4, int(m.group(1)), m.group(2), '')
    if name.startswith('prilohy/'):
        return (4, 999, name, '')
    return (5, 0, name, '')


def file_for(act: str, key: str) -> str:
    """'7' -> cl-007.md in the Constitution, par-007.md in an act; anything else is a file name."""
    m = re.fullmatch(r'(\d+)([a-z]*)', key)
    if m:
        return f'{"cl" if act == "ustava" else "par"}-{int(m.group(1)):03d}{m.group(2)}.md'
    return key if key.endswith('.md') else f'{key}.md'


def commit_on(day: str, act: str) -> str:
    branch = 'buduce' if day > dt.date.today().isoformat() and git('branch', '--list', 'buduce').strip() else 'main'
    out = git('log', '--format=%H%x09%(trailers:key=In-force,valueonly,separator=)', branch, '--', act)
    for line in out.splitlines():
        h, _, d = line.partition('\t')
        if d.strip() and d.strip() <= day:
            return h
    return ''


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    day, act = sys.argv[1], sys.argv[2]
    dt.date.fromisoformat(day)
    commit = commit_on(day, act)
    if not commit:
        sys.exit(f'{act} is not in the record on {day}.')
    if len(sys.argv) > 3:
        name = file_for(act, sys.argv[3])
        try:
            sys.stdout.write(git('show', f'{commit}:{act}/{name}'))
        except subprocess.CalledProcessError:
            sys.exit(f'{act}/{name} was not in the text on {day}.')
        return
    files = [f for f in git('ls-tree', '-r', '--name-only', commit, f'{act}/').split('\n')
             if f.endswith('.md') and not f.endswith('/README.md')]
    for f in sorted(files, key=order):
        sys.stdout.write(git('show', f'{commit}:{f}') + '\n')


if __name__ == '__main__':
    main()
