"""Peruvian blind spots, in a copy of global-law's vulnerabilities/scripts (idempotent; every pair has a marker that
survives later edits of the same text):
- detectors/placeholder_ref.py: "sin efecto" (deprived of effect) counts as a repeal marker, but the Código Procesal
  Civil names its own articles "Apelación sin efecto suspensivo" (appeal without suspensive effect): Article 757,
  "Trámite de la apelación sin efecto suspensivo", was read as a repealed placeholder, and the three provisions citing
  it (Arts. 783, 799 and 810) as references to a repealed provision. "sin efecto" followed by "suspensivo" is now
  ordinary text.
- detectors/ref_detectors.py: a reference that ends its line was taken for a heading and dropped, so item 4 of
  Article 549 of the Código Civil ("4.- Por cesar la incapacidad del padre o de la madre en el caso del artículo
  580.") was not read. It is now kept when a word and a lower-case "artículo(s)" come before it in the sentence
  (refscan already drops the headings at a line's start): dangling references went from 16 to 17.
- detectors/currency_scan.py: the sol de oro, Peru's currency until the inti replaced it in 1985, is dead in Peru only
  ("soles de oro", "soles oro"; today's sol is live); the inti was already read.

    python -X utf8 patch_pe.py <scripts dir>
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
    ("placeholder: 'sin efecto suspensivo' is not a repeal marker",
     'r"sin efecto|sans objet|',
     'r"sin efecto(?!\\s+suspensiv)(?#PE_SUSPENSIVO)|sans objet|',
     "(?#PE_SUSPENSIVO)"),
])
patch("detectors/ref_detectors.py", [
    ("dangling: a reference that ends its line is not a heading",
     "not regexp_matches(tail, '^\\s*(\\.º|º|\\.|\\))?\\s*\\n')   -- a heading, not a reference",
     "(not regexp_matches(tail, '^\\s*(\\.º|º|\\.|\\))?\\s*\\n')   -- a heading, not a reference\n"
     "               -- PE_REF_LINE_END: unless a word and a lower-case 'artículo(s)' come before it in the sentence: "
     "'4.- Por cesar ... en el caso del artículo 580.' ends its line (refscan already drops the headings at a line's start)\n"
     "               or regexp_matches(left(context, greatest(strpos(context, left(regexp_replace(tail, '[[:space:]]+', ' ', 'g'), 40)) - 1, 0)),\n"
     "                                 '[a-záéíóúñ,;][[:space:]]+art[íi]culos?[[:space:]]+([0-9][0-9A-Za-z°º-]*[[:space:]]*(,|y|e|o|al)?[[:space:]]*)*$'))",
     "PE_REF_LINE_END"),
])
patch("detectors/currency_scan.py", [
    ("currency: the sol de oro, dead in Peru only",
     'EXTRA_CURRENCY_CODE = {',
     'EXTRA_CURRENCY_CODE = {"PE": r"|soles?\\s+(?:de\\s+)?oro\\b(?#PE_SOLES_DE_ORO)", ',
     "(?#PE_SOLES_DE_ORO)"),
])
