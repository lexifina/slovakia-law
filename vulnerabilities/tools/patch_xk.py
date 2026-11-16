"""Kosovo fixes for the copy of global-law's scripts (ingest/textscan.py, the time-limit search):
 1. "deri me" (no diacritic), "deri mé" and "deri m€" (the Gazette's text layer prints "ë" as "é" or "€") and "deri" right
    before a date ("deri 31 dhjetor 2014");
 2. the word "datë" before the date in those prints and without its diacritic ("deri me daté 10 shtator 2021", "datén",
    "daten"), and its abbreviation "dt.".
    python -X utf8 patch_xk.py <scripts dir>        (a fix already in place is skipped)"""
import os, sys

S = sys.argv[1]
p = os.path.join(S, "ingest", "textscan.py")
s = open(p, encoding="utf-8").read()
FIXES = [
    ("deri me / deri mé / deri m€ / deri <date>", 'r"deri më|deri në|', 'r"deri më|deri në|deri m[eé€](?!\\w)|deri|', "deri m[eé€](?!\\w)|"),
    ("daté / datén / daten / dt. before the date", "datën|datës|datë|date|", "datën|datës|datë|date|datén|datés|daté|daten|dt\\.|",
     "datén|datés|daté|daten|dt\\.|"),
]
for name, old, new, mark in FIXES:
    if mark in s:
        print("already in place:", name)
        continue
    assert s.count(old) == 1, f"not found: {name}"
    s = s.replace(old, new, 1)
    print("patched:", name)
open(p, "w", encoding="utf-8", newline="\n").write(s)
