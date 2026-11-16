"""Eighteenth round (found by the Germany run), in a copy of global-law's vulnerabilities/scripts, after patch_de.py and
patch_sv.py (apply_patches.py runs it last but one):
- detectors/currency_scan.py: the Austrian schilling (and "S" after an amount) was added for every German-language corpus,
  so "S" after a number in German federal law gave 54 false flags: it now counts for Austria only (pins.json code AT);
- detectors/currency_scan.py: in German, "Franken" is the Swiss franc (current) or the wine region, never a dead currency:
  "frank(en)" is left out for German-language corpora (Belgian Dutch "frank" still counts).

    python -X utf8 patch_r18.py <scripts dir>        (idempotent)
"""
import sys
from pathlib import Path

p = Path(sys.argv[1]) / "detectors" / "currency_scan.py"
s = p.read_text(encoding="utf-8")
SCH = r'"de": r"|(?:(?:millionen|milliarden)\s+)?schilling\b|(?-i:S)\b(?![.,]?\s*\d)"'
done = []
if "EXTRA_CURRENCY = {" + SCH + "}" in s and '"AT": r"|(?:(?:millionen' not in s:
    s = s.replace("EXTRA_CURRENCY = {" + SCH + "}", "EXTRA_CURRENCY = {}  # by language; the schilling is by code (AT), below")
    s = s.replace('EXTRA_CURRENCY_CODE = {"SV": r"|colones\\b|¢"}',
                  'EXTRA_CURRENCY_CODE = {"SV": r"|colones\\b|¢", ' + SCH.replace('"de"', '"AT"') + '}')
    if '"AT": r"|(?:(?:millionen' not in s:
        raise SystemExit("not found: EXTRA_CURRENCY_CODE (run patch_sv.py first)")
    done.append("schilling for AT only")
FR = r"frank(en)?\b(?!\s+(suisses?|CHF|švýcar))|"
if '"de": (r"' + FR not in s:
    if 'NOT_CURRENCY = {' not in s:
        raise SystemExit("not found: NOT_CURRENCY")
    s = s.replace('NOT_CURRENCY = {', 'NOT_CURRENCY = {"de": (r"' + FR + '",), ', 1)
    done.append("Franken not a dead currency in German")
p.write_bytes(s.encode("utf-8"))
print("patched:" if done else "in place:", ", ".join(done) or "schilling for AT only; Franken")
