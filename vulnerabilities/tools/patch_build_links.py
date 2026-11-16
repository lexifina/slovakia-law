"""Links each retroactive-date flag to the commit that made that act's version on that day, read from the detectors' own
history table (index/root.parquet: law, in_force -> corpus_commit), instead of the first commit by an author of the same name
(several acts can share a title, and some histories name the act in a Law: trailer, not the author).

    python -X utf8 patch_build_links.py <build_vulns.py> [...]        (idempotent)
"""
import re, sys

LOOKUP = '''# retroactive-date links: the commit that made this act's version on this day, from the detectors' history table
ROOT_COMMIT = {}
for _law, _inf, _c in duckdb.sql(f"""select law, in_force, corpus_commit from '{os.path.join(SCR, "index", "root.parquet").replace(chr(92), "/")}'
                                   where corpus = '{json.load(open(os.path.join(SCR, "pins.json"), encoding="utf-8"))["corpora"][0]["path"]}'
                                   and kind = 'law' order by in_force""").fetchall():
    ROOT_COMMIT.setdefault((_law, str(_inf)), _c)
'''
for f in sys.argv[1:]:
    s = open(f, encoding="utf-8").read()
    if "ROOT_COMMIT = {}" in s:
        print(f, "already"); continue
    i = s.index("AUTHOR_COMMIT = {}")
    s = s[:i] + LOOKUP + s[i:]
    pat = re.compile(r'^(\s*)first = AUTHOR_COMMIT\.get\((.*)\)\s*$', re.M)
    m = pat.search(s)
    if not m:
        raise SystemExit(f"{f}: no 'first = AUTHOR_COMMIT.get(...)' line")
    ind = m.group(1)
    new = f'{ind}first = ROOT_COMMIT.get((d["law"], str(d["in_force"])), "") or AUTHOR_COMMIT.get({m.group(2)})'
    s = s[:m.start()] + new + s[m.end():]
    open(f, "w", encoding="utf-8", newline="\n").write(s)
    print(f, "patched")
