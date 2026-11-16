"""Panamanian blind spots, in a copy of global-law's vulnerabilities/scripts (idempotent; each pair carries a marker that
survives later edits):
- detectors/dup_labels.py: the treaties that Panama's approving laws reproduce break lines before a citation, so a line
  can open with a reference ("Artículo 2 de este Acuerdo y la ruta ...", "Artículo 14, apartado 2 del mencionado
  Tratado", "Artículo 4.2)b), dicho domicilio;", "Artículo 26 no incluye ...", "Artículo 12 (Seguridad Aérea) y el
  Artículo 13 ...") that the search took for a second heading with that number. In a Spanish text, a line whose label is
  followed by a comma, a paragraph number with a bracket (".2)"), or "de", "del", "y", "o", "no" (directly or after a
  bracketed title) is now read as a reference, not a heading: 108 flags became 90 on panama-law. A heading followed by
  its title or a full stop ("Artículo 2. Esta Ley ...", "ARTÍCULO 17 Jurisdicción competente", "Artículo 17
  (transitorio). ...") is read as before.
- detectors/currency_scan.py: "francos?" was read in any case, so the name Franco before a number ("Victoriano Franco
  67 soluciones habitacionales", a peasant settlement in Veraguas and its 67 dwellings in Law 50 of 2001, Art. 2)
  counted as an amount in francs. The Spanish word for the currency is now read in lower case or in capitals only
  ("francos", "FRANCOS"), as currencies are written in Spanish; "Franco" with a capital, a name, is left out: dead
  currencies went from 2 to 1 on panama-law.

    python -X utf8 patch_pa.py <scripts dir>
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


patch("detectors/dup_labels.py", [
    ("duplicate numbering: a Spanish line that opens with a citation is not a heading",
     '            if m and line.lstrip(" #*-")[:1].islower():',
     '            if m and (c.get("language") or "").lower() == "es" and re.match(r"(?:\\s*\\([^)]{1,60}\\))?(?:,|\\.\\d+\\)|\\s+(?:de|del|y|o|no)\\s)", line[m.end():]):  # patch_pa: "Artículo 2 de este Acuerdo", "Artículo 14, apartado 2" (a wrapped citation)\n'
     '                continue\n'
     '            if m and line.lstrip(" #*-")[:1].islower():',
     '# patch_pa: "Artículo 2 de este Acuerdo"'),
])

patch("detectors/currency_scan.py", [
    ("dead currencies: the Spanish franc in lower case or capitals only, not the surname Franco",
     r'francos?\b(?!\s+suizos?)|',
     r'(?-i:francos?|FRANCOS?)\b(?!\s+suizos?)|',  # patch_pa: not "Victoriano Franco 67"
     r'(?-i:francos?|FRANCOS?)'),
])
