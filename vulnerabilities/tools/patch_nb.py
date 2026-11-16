r"""Norwegian blind spots, in a copy of global-law's vulnerabilities/scripts (idempotent; every pair has a marker that
survives later edits of the same text). Everything here is read only for a corpus whose language is "nb", "nn" or "no".
- ingest/textscan.py: only "frem til" and "til og med" were read as "until"; Norwegian also writes "til 31. desember
  2020", "inntil 1. mars 2018", "fram til 31. desember 2012" (the nynorsk and older form) and the year's end, "frem til
  utgangen av 2027". "innen" (by) and "senest" (at the latest) are deadlines and stay unread, as for the other languages.
- ingest/refscan.py: Norwegian acts number their sections by chapter ("§ 14-9", "§ 1a-1", "§ 4-1 a") and write an
  inserted section with a space ("§ 6 a"). A reference "§ 14-9" was read as § 14, a heading "§ 4-1 a." gave the key 4,
  and the files (paragraf-14-009.md, paragraf-01-a-001.md, paragraf-04-001-a.md) gave none, so a repealed § 14-12 was
  never missed while § 14-1 stood. The key is now "14-9", "1a-1", "4-1a", "6a", in references (with lists: "§§ 22-6 og
  22-7"), headings and file names; "§§ 291-296" (two section marks) also gives §§ 291 to 296, which only a plainly numbered act has. "62 §" (Swedish order) is not read: in "lov ... nr. 62 § 7" it is no section.
  Another act named before the reference ("barnelova § 3", "lov 17. juni 2005 nr. 62
  § 3", "byggesaksforskriften § 5") or after it ("§ 3 første ledd i lov om ...", "§ 5 i folketrygdloven") is not the
  act's own.
- detectors/dup_labels.py: "§ 3-1" and "§ 3-2" at the start of two lines were read as two units labelled "§ 3", and an
  amending act's instructions ("§ 10 annet ledd skal lyde:", "§ 10 fjerde ledd skal lyde:") as two units "§ 10".

    python -X utf8 patch_nb.py <scripts dir>
"""
import sys
from pathlib import Path


def patch(rel, pairs):
    p = Path(sys.argv[1]) / rel
    s = p.read_text(encoding="utf-8")
    for name, a, b, marker in pairs:
        if b in s or marker in s:  # the marker: in place even if another patch edited the same text since
            print("in place:", name)
        elif a in s:
            s = s.replace(a, b, 1)
            print("patched:", name)
        else:
            raise SystemExit(f"not found: {name}")
    p.write_text(s, encoding="utf-8", newline="\n")


patch("ingest/textscan.py", [
    ("NB_LIMIT",
     'LIMIT = re.compile(rf"(?i)\\b(?:{UNTIL})\\s*(?:{FILL}){{0,2}}(?:{DATE})")\n',
     'LIMIT = re.compile(rf"(?i)\\b(?:{UNTIL})\\s*(?:{FILL}){{0,2}}(?:{DATE})")\n'
     '# patch_nb: Norwegian "til 31. desember 2020", "inntil 1. mars 2018", "fram til 31. desember 2012", and the year\'s end\n'
     '# "frem til utgangen av 2027" (only "frem til" and "til og med" were read); read only for nb, nn and no\n'
     'NB_LANGS = ("nb", "nn", "no")\n'
     'NB_LIMIT = re.compile(rf"(?i)\\b(?:(?:fram|frem)\\s+til|inntil|til)\\s+(?:(?:utgangen|utløpet)\\s+av\\s+)?(?:{DATE})")\n'
     'NB_YEAR_END = re.compile(r"(?i)\\b(?:(?:fram|frem)\\s+til|inntil|til)\\s+(?:utgangen|utløpet)\\s+av\\s+(?P<ynb>\\d{4})(?![\\d.\\-/])")\n',
     "patch_nb: Norwegian \"til 31. desember 2020\""),
    ("limits: read NB_LIMIT for nb",
     "    post = list(LIMIT_POST.finditer(text)) if _POST_WORDS.search(text) else []\n",
     "    post = list(LIMIT_POST.finditer(text)) if _POST_WORDS.search(text) else []\n"
     "    if _LANG[\"v\"] in NB_LANGS:  # patch_nb: \"frem til\" is read by LIMIT already; the same match once\n"
     "        _ends = {m.end() for m in LIMIT.finditer(text)}\n"
     "        post += [m for m in list(NB_LIMIT.finditer(text)) + list(NB_YEAR_END.finditer(text)) if m.end() not in _ends]\n",
     "# patch_nb: \"frem til\" is read by LIMIT already"),
    ("limits: the year's end (nb)",
     '            elif g.get("y6") or g.get("y7"):\n                y, mo, d = int(g.get("y6") or g.get("y7")), 12, 31\n',
     '            elif g.get("y6") or g.get("y7") or g.get("ynb"):  # patch_nb: "til utgangen av 2027"\n'
     '                y, mo, d = int(g.get("y6") or g.get("y7") or g.get("ynb")), 12, 31\n',
     'patch_nb: "til utgangen av 2027"'),
])
patch("ingest/refscan.py", [
    ("NB helpers",
     "\ndef key(num: str, suf: str | None, suf2: str | None = None) -> str:\n",
     "\n# patch_nb: Norwegian sections by chapter (\"§ 14-9\", \"§ 1a-1\", \"§ 4-1 a\") and inserted sections (\"§ 6 a\"); another act\n"
     "# named before (\"barnelova § 3\", \"lov 17. juni 2005 nr. 62 § 3\") or after (\"§ 3 første ledd i lov om ...\")\n"
     "NB_LANGS = (\"nb\", \"nn\", \"no\")\n"
     "NB_TAIL = re.compile(r\"(?:[\\-‑](\\d{1,3})(?!\\d)(?![.,]\\d))?(?:\\s?([a-h])(?![\\wæøåÆØÅ]))?\")\n"
     "NB_LIST = re.compile(r\"\\s*(?:,|\\bog\\b|\\beller\\b)\\s*(?:§\\s*)?(\\d{1,4})([a-z])?(?![\\d\\wæøå])\")\n"
     "EXT_BEFORE_NB = re.compile(r\"(?i)(?:\\b(?:lov|lova|loven|forskrift|forskrifta|forskriften)\\s+(?:av\\s+)?\\d{1,2}\\.?\\s+[a-zæøå]+\\.?\\s+\\d{4}\"\n"
     "                           r\"(?:\\s+nr\\.?\\s*\\d+)?|\\w+(?:lova|lovas)|\\w+(?:forskriften|forskrifta|forskriftens))\\s*(?:\\([\\w\\s]+\\)\\s*)?,?\\s*$\")\n"
     "EXT_AFTER_NB = re.compile(r\"(?i)^[\\s,]*(?:(?:første|annet|andre|tredje|fjerde|femte|sjette|sjuende|syvende|åttende|niende|tiende|siste)\\s+\"\n"
     "                          r\"(?:ledd|punktum)[\\s,]*|(?:bokstav|nr\\.?|nummer)\\s+\\w+[\\s,]*|(?:og|eller|til)\\s+[\\w\\-]+[\\s,]*)*i\\s+\"\n"
     "                          r\"(?:lov(?:a|en)?\\s+(?:av\\s+)?\\d|lov(?:a|en)?\\s+om\\b|forskrift(?:a|en)?\\s+(?:av\\s+)?\\d|forskrift(?:a|en)?\\s+om\\b|\"\n"
     "                          r\"[\\wæøå\\-]+(?:loven|lova|lovens|forskriften|forskrifta|avtalen|konvensjonen|traktaten|direktivet|forordningen)\\b)\")\n"
     "\n\n"
     "def _nb_tail(s: str, pos: int, k: str):\n"
     "    \"\"\"patch_nb: the rest of a Norwegian section number after the § number: \\\"-9\\\" (§ 14-9), \\\" a\\\" (§ 6 a), \\\"-1 a\\\" (§ 4-1 a).\"\"\"\n"
     "    t = NB_TAIL.match(s, pos)\n"
     "    if not t or not t.group(0):\n"
     "        return k, pos\n"
     "    if t.group(1):\n"
     "        return f\"{k}-{int(t.group(1))}{t.group(2) or ''}\", t.end()\n"
     "    if t.group(2) and not k[-1:].isalpha():\n"
     "        return k + t.group(2), t.end()\n"
     "    return k, pos\n"
     "\n\n"
     "def _nb_refs(body: str, m, first: str):\n"
     "    \"\"\"patch_nb: the keys of \\\"§ 14-9\\\", \\\"§§ 22-6 og 22-7\\\", \\\"§ 6 a\\\"; None for a plain \\\"§ 6\\\" (read as before).\"\"\"\n"
     "    k, pos = _nb_tail(body, m.end(), first)\n"
     "    if pos == m.end():\n"
     "        return None\n"
     "    ks = [k]\n"
     "    while True:\n"
     "        l = NB_LIST.match(body, pos)\n"
     "        if not l:\n"
     "            break\n"
     "        k2, pos = _nb_tail(body, l.end(), key(l.group(1), l.group(2)))\n"
     "        ks.append(k2)\n"
     "    return ks, pos\n"
     "\n\n"
     "def key(num: str, suf: str | None, suf2: str | None = None) -> str:\n",
     "def _nb_refs(body: str, m, first: str):"),
    ("_nb_refs: a range in a plainly numbered act (nb)",
     "    ks = [k]\n    while True:\n        l = NB_LIST.match(body, pos)\n",
     "    ks = [k]\n"
     "    r = re.fullmatch(r\"(\\d+)-(\\d+)\", k)  # patch_nb: a range \"§§ 291-296\" (only after §§) where sections are not numbered by chapter\n"
     "    if r and m.group(0).lstrip().startswith(\"§§\") and int(r.group(1)) < int(r.group(2)) <= int(r.group(1)) + 30:\n"
     "        ks += [str(x) for x in range(int(r.group(1)), int(r.group(2)) + 1)]\n"
     "    while True:\n        l = NB_LIST.match(body, pos)\n",
     "# patch_nb: a range \"§§ 291-296\""),
    ("heading_key: § 14-9 (nb)",
     "    return _mkey(m) if m.re is HEAD else key(m.group(1), m.group(2))\n",
     "    if m.re is HEAD and _LANG[\"v\"] in NB_LANGS and m.group(0).lstrip(\"# \").startswith(\"§\"):  # patch_nb: \"§ 14-9.\", \"§ 4-1 a.\"\n"
     "        return _nb_tail(m.string, m.end(), _mkey(m))[0]\n"
     "    return _mkey(m) if m.re is HEAD else key(m.group(1), m.group(2))\n",
     "# patch_nb: \"§ 14-9.\", \"§ 4-1 a.\""),
    ("refs: § 14-9 (nb)",
     "                if sub:  # Belgian numbering: article 259bis-9 is its own article, not 259bis\n",
     "                nbx = _nb_refs(body, m, first) if sub is None and _LANG[\"v\"] in NB_LANGS and m.group(0).lstrip().startswith(\"§\") else None\n"
     "                if nbx:  # patch_nb: \"§ 14-9\", \"§§ 22-6 og 22-7\", \"§ 6 a\"\n"
     "                    first, ks, end = nbx[0][0], nbx[0], nbx[1]\n"
     "                elif sub:  # Belgian numbering: article 259bis-9 is its own article, not 259bis\n",
     "# patch_nb: \"§ 14-9\", \"§§ 22-6 og 22-7\""),
    ("refs: no \"7 §\" in Norwegian (nb)",
     "            if any(a <= m.start() < b for a, b in seen_spans):\n                continue\n",
     "            if any(a <= m.start() < b for a, b in seen_spans):\n                continue\n"
     "            if rx is NORDIC and _LANG[\"v\"] in NB_LANGS:\n"
     "                continue  # patch_nb: Norwegian writes \"§ 7\", never \"7 §\"; \"nr. 62 § 7\" is not § 62\n",
     "# patch_nb: Norwegian writes \"§ 7\", never \"7 §\""),
    ("is_external: another act (nb)",
     "    if is_external_de(tail):\n        return True\n",
     "    if is_external_de(tail):\n        return True\n"
     "    if _LANG[\"v\"] in NB_LANGS and (EXT_BEFORE_NB.search(before[-80:]) or EXT_AFTER_NB.match(tail)):  # patch_nb\n"
     "        return True\n",
     "EXT_AFTER_NB.match(tail)):  # patch_nb"),
    ("path_key: paragraf-14-009 (nb)",
     '    m = re.match(r"(?i)^(?:(?:ugovor|naredba)',
     '    n = re.match(r"^paragraf-0*(\\d{1,4})(?:-([a-z]))?(?:-0*(\\d{1,4}))?(?:-([a-z]))?$", base) if _LANG["v"] in NB_LANGS else None\n'
     '    if n:  # patch_nb: paragraf-14-009.md is § 14-9, paragraf-01-a-001.md § 1a-1, paragraf-04-001-a.md § 4-1 a\n'
     '        return f"{int(n.group(1))}{n.group(2) or \'\'}" + (f"-{int(n.group(3))}{n.group(4) or \'\'}" if n.group(3) else "")\n'
     '    m = re.match(r"(?i)^(?:(?:ugovor|naredba)',
     "# patch_nb: paragraf-14-009.md is § 14-9"),
])
patch("detectors/dup_labels.py", [
    ("LAB_NB: § 3-1 and § 3-2 are two labels (nb)",
     "\n\ndef one(c):\n",
     "\n# patch_nb: Norwegian sections by chapter: \"§ 3-1\" and \"§ 3-2\" are two labels, not two \"§ 3\"; and an amending act's\n"
     "# instructions (\"§ 10 annet ledd skal lyde:\", \"§ 10 tredje ledd oppheves.\") are not units of the text\n"
     "LAB_NB = re.compile(LAB.pattern.replace(r\"(§+\\s*\\d+[º°o]?\", r\"(§+\\s*\\d+[a-z]?(?:[-‑]\\d+)?[º°o]?\", 1), re.I)\n"
     "NB_INSTRUCTION = re.compile(r\"(?i)\\bskal lyde\\b|\\boppheves\\b|\\bblir\\b|\\bnytt?\\b.{0,60}\\bskal\\b\")\n"
     "\n\ndef one(c):\n",
     "LAB_NB = re.compile("),
    ("one: LAB_NB for nb",
     "        for i, line in enumerate(body.splitlines()):\n            m = LAB.match(line)\n",
     "        nb = (c.get(\"language\") or \"\").lower() in (\"nb\", \"nn\", \"no\")  # patch_nb\n"
     "        for i, line in enumerate(body.splitlines()):\n"
     "            m = (LAB_NB if nb else LAB).match(line)\n"
     "            if m and nb and NB_INSTRUCTION.search(line):\n"
     "                continue  # patch_nb: an amending act's instruction\n",
     "# patch_nb: an amending act's instruction"),
])
