"""Liechtenstein (Swiss-style German) blind spots, in a copy of global-law's vulnerabilities/scripts (idempotent):
- detectors/currency_scan.py, for a German-language corpus only (pins.json "language": "de"):
  - "Franken" was read as a dead franc ("1'000 Franken" flagged as a currency no longer in use), but in German "Franken"
    is the Swiss franc, legal tender in Switzerland and Liechtenstein. A German text now flags only a franc named as
    Belgian, French or Luxembourg ("100 belgische Franken"); "CHF" and "Fr." were never flagged.
  - patch_de.py's Austrian schilling as "S" after an amount also took codes and symbols ("NO88S", "S00S", "12S",
    "BISD 27S/24", "S-300", "S.E."), and "Schilling" the end of a longer word ("Jagdpachtschilling", a hunting lease).
    "S" now needs a space after the amount and no "-", "/" or ".X" after it; "Schilling" must be a word of its own.
- ingest/refscan.py (read by the reference scan, and again by the detectors of references to repealed placeholders and of
  fines without an offence), for a German-language corpus only:
  - "Bst." (Buchstabe), which Liechtenstein and Swiss law write where Austria writes "lit.", may stand between the number
    and another act ("Art. 2 Abs. 2 Bst. d des Grundverkehrsgesetzes", "Art. 6 Abs. 1 Bst. e des Gesetzes");
  - an EU regulation or directive named after the number is another act ("Art. 4 Abs. 1 Ziff. 21 der Richtlinie
    2014/65/EU", "Art. 6 Bst. a der Delegierten Verordnung (EU) 2017/1943");
  - an ordinance's enabling clause ("Aufgrund von Art. 2 Abs. 1, Art. 25 Abs. 3 ... des Asylgesetzes ... verordnet die
    Regierung:") cites the act it rests on, not the ordinance itself, and is skipped.

    python -X utf8 patch_li.py <scripts dir>
"""
import sys
from pathlib import Path


def patch(rel, pairs):
    p = Path(sys.argv[1]) / rel
    s = p.read_text(encoding="utf-8")
    for name, a, b, *marker in pairs:
        if b in s or (marker and marker[0] in s):  # a marker: in place even if the text was edited since
            print("in place:", name)
        elif a in s:
            s = s.replace(a, b, 1)
            print("patched:", name)
        else:
            raise SystemExit(f"not found: {name}")
    p.write_text(s, encoding="utf-8", newline="\n")


FRANKEN_DE = r'''

# FRANKEN_DE: in German, "Franken" is the Swiss franc, legal tender in Switzerland and Liechtenstein ("1'000 Franken");
# a German text flags only a franc named as Belgian, French or Luxembourg ("100 belgische Franken")
import re as _re
_frank = _re.search(r"(?:\(\?<![^)]*\))*frank\(en\)\?\\b\(\?!\\s\+\([^)]*\)\)\|", CUR)
if _frank:
    NOT_CURRENCY["de"] = tuple(NOT_CURRENCY.get("de", ())) + (_frank.group(0),)
EXTRA_CURRENCY["de"] = EXTRA_CURRENCY.get("de", "") + r"|(?:belgisch|französisch|luxemburgisch)e[nrs]?\s+franken?\b"
'''

SCHILLING_DE = r'''
# SCHILLING_S_DE: the schilling as "S" only after an amount and a space ("689 000 S."), not a code or symbol ("NO88S",
# "S00S", "12S", "BISD 27S/24", "S-300", "S.E."), and "Schilling" only as a word of its own, not the rent in
# "Jagdpachtschilling"
EXTRA_CURRENCY["de"] = (EXTRA_CURRENCY.get("de", "")
    .replace(r"(?:(?:millionen|milliarden)\s+)?schilling\b", r"(?:(?:millionen|milliarden)\s+)?(?<![a-zäöüß])schilling\b")
    .replace(r"(?-i:S)\b(?![.,]?\s*\d)", r"(?<=\d[ \xa0])(?-i:S)\b(?![.,]?\s*\d|[-/]|\.\w)"))
'''

patch("ingest/refscan.py", [
    # LI_BST: Liechtenstein (and Swiss) law writes "Bst." (Buchstabe) where Austria writes "lit.": "Art. 2 Abs. 2 Bst. d des
    # Grundverkehrsgesetzes (GVG)", "Art. 6 Abs. 1 Bst. e des Gesetzes" name another act after the letter
    ("'Bst.' between the number and another act (de)", r"Pkt\.|Punkt)\s*[\w.]+", r"Pkt\.|Punkt|Bst\.|Buchstabe)\s*[\w.]+",
     r"Punkt|Bst\.|Buchstabe)"),
    # LI_EU_ACT: an EU act named after the number: "Art. 4 Abs. 1 Ziff. 21 der Richtlinie 2014/65/EU", "Art. 6 Bst. a der
    # Delegierten Verordnung (EU) 2017/1943", "Art. 27 der Verordnung (EU) Nr. 181/2011"
    ("EU regulation or directive after the number (de)", r'|(?:Vertrag|Vertrages|Vertrags|Gesetzes|Abkommens|Übereinkommens)\b"',
     r'|(?:Vertrag|Vertrages|Vertrags|Gesetzes|Abkommens|Übereinkommens)\b"' '\n'
     r'    r"|(?:Delegierten\s+|Durchführungs)?(?:[Vv]erordnung|[Rr]ichtlinie)\s+(?:\((?:EU|EG|EWG|Euratom)\)|\d)"  # LI_EU_ACT',
     "# LI_EU_ACT"),
    # LI_ENABLING: an ordinance's enabling clause cites the articles of the act it rests on ("Aufgrund von Art. 2 Abs. 1,
    # Art. 25 Abs. 3, ... des Asylgesetzes (AsylG) ... verordnet die Regierung:"), not its own
    ("enabling clause (de)", '        body = re.sub(r"(?<=\\d) bis (?=(?:§\\s*)?\\d)", " – ", body)\n',
     '        body = re.sub(r"(?<=\\d) bis (?=(?:§\\s*)?\\d)", " – ", body)\n'
     '    if _LANG["v"] == "de":  # LI_ENABLING: "Aufgrund von Art. 6 Abs. 5, ... des Gesetzes ... verordnet die Regierung:" cites the enabling act\n'
     '        body = re.sub(r"(?:Aufgrund|Auf Grund|Gestützt auf)\\b[^:]{0,2000}?\\b(?:verordnet|erlässt|beschliesst|beschließt|verfügt)\\b[^:\\n]{0,60}:", " ", body)\n',
     "# LI_ENABLING"),
])

patch("detectors/currency_scan.py", [
    ("Franken (de) is the Swiss franc", "\n\ndef pat_for(c):", FRANKEN_DE.rstrip("\n") + "\n\n\ndef pat_for(c):", "# FRANKEN_DE:"),
    ("Schilling 'S' (de) after an amount and a space", "\n\n\ndef pat_for(c):", SCHILLING_DE.rstrip("\n") + "\n\n\ndef pat_for(c):",
     "# SCHILLING_S_DE:"),
])
