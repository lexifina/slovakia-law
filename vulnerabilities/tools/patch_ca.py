"""Catalan blind spots, in a copy of global-law's vulnerabilities/scripts (idempotent):
- ingest/textscan.py: Catalan dates and time limits, none of which the time-limit search read: the month names
  (gener ... desembre), "d'agost" / "d'octubre" / "d'abril" (d' before the month), "fins al 31 de desembre de 2020",
  "fins a l'1 de gener de 2021", "fins el ...", and the deadlines "abans del", "no més tard del", "com a màxim",
  "com a molt tard" (read as deadlines, as the other languages' "not later than");
- detectors/currency_scan.py: the Catalan peseta ("pessetes", "pesseta") was not read as a currency, and "sucre"
  (sugar, as in a customs tariff's "Sucre 1%") was read as the Ecuadorian sucre.

    python -X utf8 patch_ca.py <scripts dir>
"""
import sys
from pathlib import Path


def patch(rel, pairs):
    p = Path(sys.argv[1]) / rel
    s = p.read_text(encoding="utf-8")
    for name, a, b, *marker in pairs:
        if b in s or (marker and marker[0] in s):  # a marker: in place even if another patch edited the same text since
            print("in place:", name)
        elif a in s:
            s = s.replace(a, b, 1)
            print("patched:", name)
        else:
            raise SystemExit(f"not found: {name}")
    p.write_text(s, encoding="utf-8", newline="\n")


patch("ingest/textscan.py", [
    ("MONTHS: Catalan", 'MONTHS = ("january february',
     'MONTHS = ("gener febrer març abril maig juny juliol agost setembre octubre novembre desembre "\n          "january february'),
    ("DATE: d' before the month", r"\.?\s*(?:de\s+)?(?P<mon>{MON})", r"\.?\s*(?:de\s+|d['’]\s*)?(?P<mon>{MON})"),
    ("DEADLINE: Catalan", r'DEADLINE = (r"not later than|',
     r'DEADLINE = (r"no més tard del?|no més tard de l[' + "'" + r'’]|com a màxim|com a molt tard|abans del?|abans de l[' + "'" + r'’]|not later than|'),
    ("UNTIL: Catalan", r'UNTIL = (r"until the end of|',
     r'UNTIL = (r"fins al|fins a l[' + "'" + r'’]|fins el|fins a|abans del|abans de l[' + "'" + r'’]|no més tard del|no més tard de l[' + "'" + r'’]|'
     r'com a màxim fins al|com a màxim el|com a molt tard el|until the end of|'),
])
patch("detectors/currency_scan.py", [
    ("pessetes", r"|pesetas?|", r"|pesetas?|pessetes|pesseta\b|"),
    ("sucre: not in Catalan", r'NOT_CURRENCY = {"fr": (',
     r'NOT_CURRENCY = {"ca": (r"(?-i:sucres?)\b|",), "fr": (', r'NOT_CURRENCY = {"ca": ('),  # round 17 rewrites the sucre text
])
