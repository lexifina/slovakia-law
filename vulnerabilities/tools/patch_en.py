"""English blind spots in detectors/placeholder_ref.py, found on bhutan-law, in a copy of global-law's
vulnerabilities/scripts (idempotent):
- "vacat" (meant for "[Vacated]") also matched "Upon vacation of seat" and "wishes to vacate", and "void" matched "null
  and void", so a short section using those words was taken for a repealed placeholder: now "vacated" only, and "void" not
  after "null and";
- an amending Act's own section that repeals a section of the Act it amends ("9. In the Code, Section 14.1 is repealed.")
  was taken for a placeholder of a repealed section: a text that says a section is repealed is now, like "repeals the ...",
  the repealing provision, not a placeholder.

    python -X utf8 patch_en.py <scripts dir>
"""
import sys
from pathlib import Path


def patch(rel, pairs):
    p = Path(sys.argv[1]) / rel
    s = p.read_text(encoding="utf-8")
    for name, a, b, *marker in pairs:
        if b in s or (marker and marker[0] in s):  # a marker: in place even if a later patch (patch_en_et.py) edited the text
            print("in place:", name)
        elif a in s:
            s = s.replace(a, b, 1)
            print("patched:", name)
        else:
            raise SystemExit(f"not found: {name}")
    p.write_text(s, encoding="utf-8", newline="\n")


patch("detectors/placeholder_ref.py", [
    ("GONE: vacated only", r"|expired|vacat|", r"|expired|vacated\b|"),
    ("GONE: not null and void", r"|sans objet|void|", r"|sans objet|(?<!null and )void|"),
    ("repealing provision", r'repeals? (?:the|all|any)|sont abrog',
     r'repeals? (?:the|all|any)|\b(?:section|article|chapter|part|schedule)s?\s+[\w.() ,]{1,30}?\s+(?:is|are|shall be|stands?)\s+(?:hereby\s+)?repealed|sont abrog',
     r'\b(?:section|article|chapter|part|schedule)s?\s+[\w.() ,]{1,30}?\s+(?:is|are|shall be|stands?)'),
])
