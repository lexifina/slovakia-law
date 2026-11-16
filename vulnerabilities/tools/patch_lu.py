"""Luxembourg blind spots, in a copy of global-law's vulnerabilities/scripts (idempotent):
- detectors/currency_scan.py: the Luxembourg franc, replaced by the euro in 1999/2002, is read when written out
  ("500 francs"), but Luxembourg's laws also write it "fr.", "frs" or "LUF" ("1200 fr. par an", "11,475 frs.",
  "250.000.000 LUF"), which the scan did not read. These are added for Luxembourg only (pins.json code LU): elsewhere
  "fr." is not a currency.
- ingest/common.py (git()), detectors/currency_scan.py, detectors/notes_scan.py: git quotes a path with non-ASCII
  characters in `ls-tree` and `grep` output ("loi/.../art_12_rubrique_administration_g\\303\\251n\\303\\251rale.md",
  with the quotes), while the history (`log -z`) has it as written. The text and reference scans therefore saw such a
  file under another act ('"loi/...'), so references to its article read as references to a deleted provision, and the
  flags carried the quoted path. git now runs with core.quotepath=false; a path is quoted only for control characters,
  quotes and backslashes.

    python -X utf8 patch_lu.py <scripts dir>
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
    ("Luxembourg franc abbreviations (LU only)",
     'EXTRA_CURRENCY_CODE = {"SV": r"|colones\\b|¢"',
     'EXTRA_CURRENCY_CODE = {"LU": r"|(?-i:\\bLUF\\b)|(?<![./@])\\bfrs?\\b\\.?", "SV": r"|colones\\b|¢"',
     '"LU": r"|(?-i:\\bLUF\\b)'),
    ("currency scan: unquoted non-ASCII paths",
     'subprocess.run(["git", "-C", str(repo), "grep"',
     'subprocess.run(["git", "-c", "core.quotepath=false", "-C", str(repo), "grep"',
     '"core.quotepath=false"'),
])
patch("detectors/notes_scan.py", [
    ("notes scan: unquoted non-ASCII paths",
     'subprocess.run(["git", "-C", str(repo), "grep"',
     'subprocess.run(["git", "-c", "core.quotepath=false", "-C", str(repo), "grep"',
     '"core.quotepath=false"'),
])
patch("ingest/common.py", [
    ("git(): unquoted non-ASCII paths",
     'p = subprocess.run(["git", *args], cwd=cwd',
     'p = subprocess.run(["git", "-c", "core.quotepath=false", *args], cwd=cwd',
     '"core.quotepath=false"'),
])
