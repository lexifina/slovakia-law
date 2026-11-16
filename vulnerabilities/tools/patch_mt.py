"""Maltese blind spot, in a copy of global-law's vulnerabilities/scripts (idempotent):
- detectors/currency_scan.py: the Maltese lira, replaced by the euro on 1 January 2008, was read only as "lira" next to an
  amount. Maltese texts write it "Lm15", "Lm 1,000" or "100 liri": "Lm" right before an amount (capital L, small m, not
  inside a word) and "liri" are added for Malta only (pins.json code MT). "Lm" after a number is left out: in the
  measuring-instruments regulations it is a length ("not less than 0,02 Lm"); so is "Lm" before a figure with one decimal
  place, the minimum landing size in the fisheries management plans ("Lm 11.1 cm", "Lm 16.0").
- detectors/currency_scan.py, every language: "Cabernet Franc" (the grape, in the wine regulations) and "Dinaric" (the
  Dinaric dolomite pine forests, a habitat type) were read as the franc and the dinar.

    python -X utf8 patch_mt.py <scripts dir>
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


patch("detectors/currency_scan.py", [
    ("Maltese lira (MT)", 'EXTRA_CURRENCY_CODE = {',
     'EXTRA_CURRENCY_CODE = {"MT": r"|liri\\b|(?-i:(?<![A-Za-z])Lm)(?=\\s?[0-9])(?!\\s?[0-9]+\\.[0-9](?![0-9]))", ', '"MT": r"|liri'),
    ("Cabernet Franc", r"francs?\b(?!\s+(suisses?|CFA|", r"(?<!cabernet )francs?\b(?!\s+(suisses?|CFA|", "(?<!cabernet )francs?"),
    ("Dinaric", r"leva? stari|dinara?)", r"leva? stari|dinara?(?!ic))", "dinara?(?!ic)"),
])
