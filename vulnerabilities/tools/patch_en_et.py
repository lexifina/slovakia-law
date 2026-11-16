"""More English blind spots in detectors/placeholder_ref.py, found on ethiopia-law, in a copy of global-law's
vulnerabilities/scripts (idempotent; run after patch_en.py):
- a repeal article that repeals a whole earlier law ("1/ The Public Enterprises Proclamation No. 25/1992 is hereby
  repealed.", "... is here by repealed.") was taken for a placeholder of a repealed article: patch_en.py's repealing-provision
  test knew only "Section/Article ... is repealed"; it now also knows a named proclamation, act, law, code, decree,
  regulation or directive, with its number, and "here by";
- "shall be deleted" ("The information registered shall be deleted by line on it") is a rule about deleting something, not
  the mark of a deleted provision: "deleted" no longer counts after "shall be".

    python -X utf8 patch_en_et.py <scripts dir>
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


patch("detectors/placeholder_ref.py", [
    ("GONE: not 'shall be deleted'", r"|repealed|deleted|omitted|", r"|repealed|(?<!shall be )deleted|omitted|"),
    ("repealing provision: a named law",
     r'(?:is|are|shall be|stands?)\s+(?:hereby\s+)?repealed|sont abrog',
     r'(?:is|are|shall be|stands?)\s+(?:hereby\s+)?repealed|\b(?:proclamation|act|law|code|decree|regulation|directive)s?\b[^;:]{0,40}?\s+(?:is|are|shall be)\s+(?:here\s?by\s+)?repealed|sont abrog'),
])
