"""Colombian blind spots, in a copy of global-law's vulnerabilities/scripts (idempotent):
- ingest/textscan.py: dates the time-limit search missed: a day written as an ordinal ("1o de enero", "1o. de enero",
  "1º de enero"), a day or a year written in words with the figure in brackets ("hasta el treinta y uno (31) de diciembre
  de dos mil cinco (2005)", "hasta el primero (1o) de abril de 2017"), and the deadline "a más tardar el 31 de diciembre de
  2020" (read as "no later than" is in English; the empty-period search still leaves deadlines out).

    python -X utf8 patch_co.py <scripts dir>
"""
import sys
from pathlib import Path


def patch(rel, pairs):
    p = Path(sys.argv[1]) / rel
    s = p.read_text(encoding="utf-8")
    for name, a, b in pairs:
        if b in s:
            print("in place:", name)
        elif a in s:
            s = s.replace(a, b, 1)
            print("patched:", name)
        else:
            raise SystemExit(f"not found: {name}")
    p.write_text(s, encoding="utf-8", newline="\n")


W = r"(?:[a-záéíóúñ]+\s+)"
patch("ingest/textscan.py", [
    ("DATE: day and year in words, ordinal day",
     r'rf"(?P<d1>\d{{1,2}})(?:η|ή|ης|ής|-?го|-?ти)?\.?\s*(?:de\s+|d[' + "'" + r'’]\s*)?(?P<mon>{MON})\s*(?:del?\s+(?:año\s+)?)?(?P<y1>\d{{4}})"',
     r'rf"(?:' + W + r'{{1,3}}\()?(?P<d1>\d{{1,2}})(?:[oº°]\.?)?\)?(?:η|ή|ης|ής|-?го|-?ти)?\.?\s*(?:de\s+|d[' + "'" + r'’]\s*)?(?P<mon>{MON})\s*(?:del?\s+(?:año\s+)?)?(?:' + W + r'{{1,5}}\()?(?P<y1>\d{{4}})"'),
    ("UNTIL: a más tardar", r'r"hasta el|hasta|', r'r"hasta el|hasta|a más tardar|'),
])
