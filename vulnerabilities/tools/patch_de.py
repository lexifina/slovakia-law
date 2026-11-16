"""Austrian (German-language) blind spots, in a copy of global-law's vulnerabilities/scripts (idempotent):
- ingest/textscan.py: dates the time-limit search missed: the Austrian month names "Jänner" (January) and "Feber"
  (February), and "bis zum Ablauf des 31. Dezember 2020" / "bis einschließlich 31. Dezember 2020" (words between
  "bis (zum)" and the date);
- ingest/refscan.py, for a German-language corpus only (pins.json "language": "de"): a reference to another act named
  after the number was read as a reference to the citing act's own provision. Now external: a mixed-case or hyphenated
  abbreviation ("§ 221 Abs. 1 Z 2 UGB", "§ 70 ZaDiG 2018", "Art. 10 B-VG", "Art. 11 EuSchMaVO"), with "Z", "lit." and
  "Abs." in between; an act's name ending in -gesetz, -ordnung, -vertrag and the like ("§ 26 Verwaltungsstrafgesetz
  1991", "Artikel 73 der Wechselordnung", "§ 18 Z 4 Maß- und Eichgesetz"), but not "dieses Bundesgesetzes"; and an act
  named after a list or range ("§§ 10, 17 und 18 VStG", "§§ 67 und 70 bis 75 Notariatsordnung"). "§§ 70 bis 75" is
  a range, not § 70bis (the Latin suffix). RIS's notes ("(Anm.: aus BGBl. Nr. 475/1990, zu den §§ 96, ...)") name the
  provisions an amending act changed and are skipped like other amendment notes. "S. 28" after an Official Journal
  citation is a page (Seite), not a section.

    python -X utf8 patch_de.py <scripts dir>
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


patch("ingest/textscan.py", [
    ("months: Jänner, Feber", 'MI["setiembre"] = 9\n', 'MI["setiembre"] = 9\nMI["jänner"] = 1; MI["feber"] = 2  # Austrian German\n'),
    ("FILL: Ablauf des, einschließlich", r'FILL = r"(?:the|le|el|d[íi]a|o|il|den|dem|',
     r'FILL = r"(?:the|le|el|d[íi]a|o|il|den|dem|ablauf|des|einschlie(?:ß|ss)lich|'),
])

DE = r'''
# German (Austria): another act named after the number, after "Abs.", "Z", "lit." and the like: a mixed-case or hyphenated
# abbreviation ("UGB", "ZaDiG 2018", "B-VG", "EuSchMaVO") or an act's name ("Verwaltungsstrafgesetz 1991", "der
# Wechselordnung", "Maß- und Eichgesetz"), never "dieses Bundesgesetzes"
EXT_AFTER_DE = re.compile(
    r"^\s*,?\s*(?:ff\.\s*)?(?:(?:Abs\.|Absatz|Satz|Unterabs\.|UAbs\.|Z|Ziffer|Ziff\.|lit\.|Nr\.|Pkt\.|Punkt)\s*[\w.]+\s*,?\s*"
    r"(?:(?:und|oder|bis|sowie)\s+[\w.]+\s*,?\s*)*)*(?:(?:des|der|dem|im|zum)\s+)?"
    r"(?:[A-ZÄÖÜ][A-Za-zÄÖÜäöüß]*[A-ZÄÖÜ][A-Za-zÄÖÜäöüß]*(?:-[A-ZÄÖÜ][A-Za-zÄÖÜäöüß]*)*\b(?![.:])|[A-ZÄÖÜ]-[A-ZÄÖÜ][A-Za-zÄÖÜ]*\b"
    r"|(?:Vertrag|Vertrages|Vertrags|Gesetzes|Abkommens|Übereinkommens)\b"
    r"|(?:[A-ZÄÖÜ][\wäöüß]*-\s+und\s+)?[A-ZÄÖÜ][\wäöüß\-]*"
    r"(?:gesetz|gesetzes|gesetzbuch|gesetzbuches|ordnung|vertrag|vertrages|vertrags|konvention|statut|statuts|richtlinie|"
    r"abkommen|abkommens|übereinkommen|übereinkommens|verfassung)\b)")
DE_NOTE = re.compile(r"\(Anm\.:")


def is_external_de(tail: str) -> bool:
    return _LANG["v"] == "de" and bool(EXT_AFTER_DE.match(tail))
'''

patch("ingest/refscan.py", [
    ("EXT_AFTER_DE", '\n\ndef is_external(before: str, tail: str) -> bool:',
     DE.rstrip("\n") + '\n\n\ndef is_external(before: str, tail: str) -> bool:'),
    # an early return, so that round 7's line ("... or EXT_AFTER_VI.match(tail))") stays as patch_detectors_vi.py checks it
    ("is_external: German (undo the first version, which edited round 7's line)",
     " or EXT_AFTER_VI.match(tail) or is_external_de(tail))", " or EXT_AFTER_VI.match(tail))", "is_external_de(tail):\n        return True"),
    ("is_external: German", "    return bool(EXT_BEFORE.search(before[-60:]) or EXT_AFTER.match(tail) or EXT_AFTER_VI.match(tail))",
     "    if is_external_de(tail):\n        return True\n"
     "    return bool(EXT_BEFORE.search(before[-60:]) or EXT_AFTER.match(tail) or EXT_AFTER_VI.match(tail))"),
    ("RIS notes", "            if NOTE.search(line) or (REPEAL_NOTE",
     "            if (_LANG[\"v\"] == \"de\" and DE_NOTE.search(line)) or NOTE.search(line) or (REPEAL_NOTE"),
    ("German 'bis' is a range", '    body = "\\n".join(l for l in body.splitlines() if "|" not in l)  # tables list other laws\' articles\n',
     '    body = "\\n".join(l for l in body.splitlines() if "|" not in l)  # tables list other laws\' articles\n'
     '    if _LANG["v"] == "de":  # "§§ 70 bis 75" is a range, not § 70bis\n'
     '        body = re.sub(r"(?<=\\d) bis (?=(?:§\\s*)?\\d)", " – ", body)\n'),
    ("German 'S.' is a page", "            if is_external(before, tail):\n                continue\n",
     "            if _LANG[\"v\"] == \"de\" and re.match(r\"(?i)s\\.\", m.group(0).lstrip()):\n"
     "                continue  # \"ABl. Nr. L 76 vom 19.03.2018 S. 28\": in German, S. is a page (Seite) or a sentence (Satz)\n"
     "            if is_external(before, tail):\n                continue\n"),
    ("list or range then an act","                    ks, end = _expand(body, m, first)\n",
     "                    ks, end = _expand(body, m, first)\n"
     "                    if len(ks) > 1 and is_external_de(body[end:end + 70]):\n"
     "                        seen_spans.append((m.start(), end))\n"
     "                        continue  # \"§§ 10, 17 und 18 VStG\": the act is named after the list\n"),
])

patch("detectors/notes_scan.py", [
    ("RIS's '(Anm.: richtig ...)'", '    r"\\[sic\\]", r"\\(sic\\)",\n',
     '    r"\\[sic\\]", r"\\(sic\\)", r"\\(Anm\\.: richtig",  # the RIS\'s own [sic]: "Genugthung (Anm.: richtig: Genugthuung)", "(Anm.: richtig wäre Z 15b)"\n'),
])

patch("detectors/currency_scan.py", [
    ("Schilling (de)", 'NOT_CURRENCY = {',
     '# a currency only one language writes: the Austrian schilling, by name or as "S" after an amount ("1 000 S", not the\n'
     '# page in "ABl. Nr. L 66 S 7")\n'
     r'EXTRA_CURRENCY = {"de": r"|(?:(?:millionen|milliarden)\s+)?schilling\b|(?-i:S)\b(?![.,]?\s*\d)"}' '\n'
     'NOT_CURRENCY = {', "\nEXTRA_CURRENCY = {"),  # marker: patch_ca.py edits the NOT_CURRENCY line (before or after)
    ("pat_for: extra currencies", r'    return rf"{NUM}\s*{cur}|{cur}\s*{NUM}"',
     '    cur = cur[:-1] + EXTRA_CURRENCY.get((c.get("language") or "").lower(), "") + ")"\n'
     r'    return rf"{NUM}\s*{cur}|{cur}\s*{NUM}"',
     'EXTRA_CURRENCY.get((c.get("language")'),  # patch_sv.py extends this line
])
