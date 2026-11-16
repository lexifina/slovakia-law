"""Philippine blind spots in detectors/placeholder_ref.py (whose is_placeholder() dead_fine.py also uses), found on
philippines-law, in a copy of global-law's vulnerabilities/scripts (idempotent; each pair carries a marker that survives
later edits):
- PH_DELETED: an amending Act's own section that deletes a section of the Act it amends ("SEC. 10. Section 15 of Republic
  Act No. 9160 is hereby deleted.", "SEC. 24. Sections 10, 11 and 12 of the same Act are hereby deleted.") was taken for
  a placeholder of a deleted section, so the amending Act's references to sections of the Act it amends, or to sections of
  a third Act, with the same numbers ("Section 10 of the same Act is hereby amended to read as follows: \"SEC. 10. ...")
  read as references to a repealed placeholder: a text that says a section "is hereby deleted" or "are hereby deleted" is
  now, like one that says it "is hereby repealed" (patch_en.py), the deleting provision, not a placeholder;
- PH_ADVERB: "Section 22. Revival of Law Impliedly Repealed. - When a law which impliedly repeals a prior law is itself
  repealed, ..." (Administrative Code of 1987) was taken for a placeholder because "Repealed" opens its text: a marker
  word after an adverb ("impliedly repealed", "expressly repealed") and followed by more than 60 characters of text
  names a kind of repeal, not the provision's own.

    python -X utf8 patch_en_ph.py <scripts dir>
"""
import sys
from pathlib import Path


def patch(rel, pairs):
    p = Path(sys.argv[1]) / rel
    s = p.read_text(encoding="utf-8")
    for name, a, b, marker in pairs:
        if marker in s:
            print("in place:", name)
        elif a in s:
            s = s.replace(a, b, 1)
            print("patched:", name)
        else:
            raise SystemExit(f"not found: {name}")
    p.write_text(s, encoding="utf-8", newline="\n")


patch("detectors/placeholder_ref.py", [
    ("PH_DELETED",
     "    if not substantive:\n        return bool(GONE.search(head)",
     "    # PH_DELETED: an amending Act's own section that deletes a section of the Act it amends (\"SEC. 10. Section 15 of\n"
     "    # Republic Act No. 9160 is hereby deleted.\") is the deleting provision, not a placeholder\n"
     "    if re.search(r\"(?i)\\b(?:section|article|chapter|part|schedule)s?\\s+[\\w.() ,]{1,40}?\\s+(?:is|are)\\s+hereby\\s+deleted\\b\", substantive):\n"
     "        return False\n"
     "    if not substantive:\n        return bool(GONE.search(head)",
     "PH_DELETED"),
    ("PH_ADVERB",
     "    m = GONE.search(substantive)  # not substantive[:70]: the cut can fall inside a word\n",
     "    m = GONE.search(substantive)  # not substantive[:70]: the cut can fall inside a word\n"
     "    if m and re.search(r\"(?i)\\b\\w{3,}ly\\s+$\", substantive[:m.start()]) and len(substantive) - m.end() > 60:\n"
     "        return False  # PH_ADVERB: \"Revival of Law Impliedly Repealed. - When a law ...\" names a kind of repeal\n",
     "PH_ADVERB"),
])
