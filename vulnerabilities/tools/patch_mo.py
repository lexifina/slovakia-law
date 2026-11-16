"""Portuguese as written in Macau (European Portuguese), in a copy of global-law's vulnerabilities/scripts (once, after
patch_pt.py; every change carries a "patch_mo" marker that later edits keep):
- ingest/textscan.py: "até ao dia 30 de Junho de 2027" was not read (no "ao" between "até" and "dia"), and the Slavic
  "do" (until) read the Portuguese "do" (of the): "produz efeitos a partir do dia 1 de Janeiro de 2021" and "Do dia 1 de
  Julho de 2026 até ..." were read as rules that end on that day. In a Portuguese corpus a match that opens with "do" is
  now skipped;
- ingest/refscan.py: "artigo 5.º" (the ordinal sign after a full stop) left ".º" in the tail, so "artigos 7.º a 9.º"
  was read as article 7 alone, "artigo 3.º-A" lost its letter, and "artigo 26.º do Código Civil" was read as the act's own
  article 26;
- detectors/dup_labels.py: a line that begins with a reference ("artigo 71.º da Lei Básica ...", where the text wraps)
  was read as a heading; a heading never starts with a lower-case letter.

    python -X utf8 patch_mo.py <scripts dir>      (after the kit's patches; apply_patches.py runs it last)
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


patch("ingest/textscan.py", [
    ("FILL: até ao dia", "\nLIMIT = re.compile(",
     '\nFILL = FILL.replace("(?:", "(?:ao|", 1)  # patch_mo: European Portuguese "até ao dia 30 de Junho de 2027"\nLIMIT = re.compile(',
     "# patch_mo: European Portuguese"),
    ("pt: do is not until", "        g = m.groupdict()\n",
     "        g = m.groupdict()\n"
     "        if _LANG[\"v\"] == \"pt\" and re.match(r\"(?i)do\\b\", m.group(0)):\n"
     "            continue  # patch_mo: Portuguese \"do\" is \"of the\" (\"a partir do dia 1 de Julho\"), not the Slavic \"until\"\n",
     "# patch_mo: Portuguese \"do\""),
])
patch("ingest/refscan.py", [
    ("NUM: 5.º", "|\\d{{1,4}})(?:[\\s\\-‑]?({LATIN})",
     "|\\d{{1,4}})(?:\\.[º°])?(?:[\\s\\-‑]?({LATIN})",
     "|\\d{{1,4}})(?:\\.[º°])?"),
    ("EXT_AFTER_PT: 9.º do Código", '\nTHAI = re.compile(r"',
     '\n# patch_mo: Macau writes the ordinal after a full stop ("artigos 7.º a 9.º do Código Civil")\n'
     'EXT_AFTER_PT = re.compile(EXT_AFTER_PT.pattern.replace(r"\\d+[º°]?", r"\\d+\\.?[º°]?"))\n'
     '\nTHAI = re.compile(r"',
     "# patch_mo: Macau writes"),
])
patch("detectors/dup_labels.py", [
    ("a wrapped reference is not a heading", "            if m and not REVOKED.search(line[:160])",
     "            if m and line.lstrip(\" #*-\")[:1].islower():  # patch_mo: \"artigo 71.º da Lei ...\" (wrapped text) is a reference\n"
     "                continue\n"
     "            if m and not REVOKED.search(line[:160])",
     "# patch_mo: \"artigo 71.º"),
])
