"""English blind spots found on nauru-law, in a copy of global-law's vulnerabilities/scripts (run after the other
patches; each change carries a marker, NR_HISTORY_NOTE / NR_REPEALED_ADJ / NR_ORDINAL_DATE, and is skipped where the marker is already there):
- ingest/refscan.py refs(): a history note that RONLAW's reprints print under a provision ("[s 18 (formerly section 15)
  renum No 25 of 1967 s 5 and Sch 3, opn 29 Dec 1967]", "[s 50 omitted by the Law Revision Commission under powers
  authorised by Act 10 of 2019]") was read for references, so a section's own former number counted as a reference to
  the section that now has that number; a line that is only such a note (in square brackets, ending with the operative
  day "opn <day> <month> <year>", or naming the Law Revision Commission) is no longer read for references. This also
  serves dead_fine.py and the reference scan, which use the same refs();
- detectors/placeholder_ref.py GONE: "repealed" after "a", "any" or "the" ("A reference to the Administrator or Registrar
  under a repealed Act ... shall be deemed to be a reference to the Registrar") describes another law, not the mark of a
  repealed provision;
- ingest/textscan.py DATE (NR_ORDINAL_DATE): an English day with an ordinal suffix and a comma before the year ("until
  1st January 1978", "until 31st October, 1963") was not read as a date, so five "until" limits in current law text were
  never seen; a day may now end in st/nd/rd/th, and a comma may stand between the month and the year.

    python -X utf8 patch_en_nr.py <scripts dir>
"""
import sys
from pathlib import Path


def patch(rel, pairs):
    p = Path(sys.argv[1]) / rel
    s = p.read_text(encoding="utf-8")
    for marker, a, b in pairs:
        if marker in s:
            print("in place:", marker)
        elif a in s:
            s = s.replace(a, b, 1)
            print("patched:", marker)
        else:
            raise SystemExit(f"not found: {marker}")
    p.write_text(s, encoding="utf-8", newline="\n")


patch("ingest/refscan.py", [
    ("NR_HISTORY_NOTE",
     """    body = "\\n".join(l for l in body.splitlines() if "|" not in l)  # tables list other laws' articles\n""",
     """    body = "\\n".join(l for l in body.splitlines() if "|" not in l)  # tables list other laws' articles\n"""
     """    # NR_HISTORY_NOTE: a line that is only a reprint's history note ("[s 18 (formerly section 15) renum No 25 of 1967 s 5\n"""
     """    # and Sch 3, opn 29 Dec 1967]", "[s 50 omitted by the Law Revision Commission ...]") cites no provision of this act\n"""
     """    body = "\\n".join(l for l in body.splitlines()\n"""
     """                     if not re.match(r"^\\s*\\[[^\\[\\]]*(?:\\bopn\\s+\\d{1,2}\\s+[A-Za-z]{3,9}\\.?\\s+\\d{4}|\\bLaw Revision Commission\\b[^\\[\\]]*)\\]\\s*$", l))\n"""),
])
patch("detectors/placeholder_ref.py", [
    ("NR_REPEALED_ADJ",
     r"|repealed|(?<!shall be )deleted|omitted|",
     r"|(?<!\ba )(?<!\bany )(?<!\bthe )repealed|(?<!shall be )deleted|omitted|"),
])
# the marker for the second change lives in a comment next to GONE, so a later edit to the pattern keeps it findable
p = Path(sys.argv[1]) / "detectors/placeholder_ref.py"
s = p.read_text(encoding="utf-8")
if "# NR_REPEALED_ADJ" not in s:
    s = s.replace("GONE = re.compile(", "# NR_REPEALED_ADJ: 'a/any/the repealed Act' describes another law, not a repealed provision\nGONE = re.compile(", 1)
    p.write_text(s, encoding="utf-8", newline="\n")
patch("ingest/textscan.py", [
    ("NR_ORDINAL_DATE",
     'LIMIT = re.compile(rf"(?i)',
     '# NR_ORDINAL_DATE: English days with an ordinal ("until 1st January 1978") and a comma before the year ("31st October, 1963")\n'
     r'DATE = DATE.replace(r"(?P<d1>\d{1,2})(?:[oº°]\.?)?", r"(?P<d1>\d{1,2})(?:[oº°]\.?|(?<=\d)(?:st|nd|rd|th)\b)?", 1)'
     r'.replace(r"(?P<y1>\d{4})", r"(?:,\s*)?(?P<y1>\d{4})", 1)' '\n'
     'LIMIT = re.compile(rf"(?i)'),
])
