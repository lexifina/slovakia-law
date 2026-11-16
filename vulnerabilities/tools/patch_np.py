"""English fix found by the Nepal run, in a copy of global-law's vulnerabilities/scripts (idempotent):
- detectors/placeholder_ref.py (and dead_fine.py, which uses the same test): "expired" counted as the mark of a
  repealed section, so a short section that forbids selling a drug "which is date expired" (section 30 of the Drugs Act,
  2035) was read as repealed, and section 34, which punishes selling a date-expired drug "contrary to section 30", as a
  reference to it and a fine with nothing to punish. "expired" right after "date" or "date-" no longer counts.

    python -X utf8 patch_np.py <scripts dir>
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


patch("detectors/placeholder_ref.py", [
    ("date expired (NP)", r"|spent|lapsed|expired|", r"|spent|lapsed|(?<!date )(?<!date-)expired|", "(?<!date-)expired"),
])
