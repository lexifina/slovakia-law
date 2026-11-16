"""English blind spots found on new-zealand-law, in a copy of global-law's vulnerabilities/scripts (run after the other
patches, last in apply_patches.py's ORDER; each change carries a marker and is skipped where the marker is already there):
- ingest/refscan.py key() (NZ_O_SUFFIX): a trailing "o" was dropped as an ordinal mark ("4o.", Spanish and Portuguese),
  so New Zealand's section 312O was keyed as section 312 and section 216O as 216; in English text "o" is a letter suffix;
- ingest/refscan.py refs() (NZ_LINE_BREAK): in English text a unit word at the end of one line and a number at the start
  of the next ("... performance requirement regulation" / "17 Purpose of ...", a schedule's table of contents) was read
  as one reference; a reference no longer spans a line break;
- ingest/refscan.py refs() (NZ_AMENDED_ENACTMENT): a schedule of consequential amendments or of enactments repealed
  lists other enactments under a heading line that ends with their year and number ("Animal Products Act 1999 (1999
  No 93)", "(SR 2003/123)", "(LI 2021/249)"); from the first such line on, the file cites those enactments, not its own Act;
- ingest/refscan.py refs() (NZ_OF_ACT): in English text, a reference followed by subsections or a list and then "of the
  <Name> Act/Regulations/Rules/Order/Code/Convention ..." or "of that Act" ("sections 9(2), 10, and 11 of the Family
  Violence Act 2018") cites another enactment; only "of the X Act" straight after the number was recognised;
- ingest/refscan.py refs() (NZ_ACT_BEFORE): in English text, a reference straight after an enactment's name and year and a
  comma or colon ("Piracy Act 1850: section 6", "Chemical Weapons (Prohibition) Act 1996, section 6") cites that enactment;
- ingest/textscan.py amounts() (NZ_MILLION): in English text "$10 million" was read as $10, so an amendment that rewrote
  "$10,000,000" as "$10 million" looked like a cut from $10,000,000 to $10 (stale amounts); a dollar amount followed by
  "million" or "billion" is now multiplied out;
- detectors/placeholder_ref.py (NZ_DUP_LIVE): new-zealand-law keeps a repealed section and a later section with the same
  number side by side ("sec-057g.md" "[Repealed]", "sec-057g-2.md" the new section 57G); a number that a live "-N" file
  also holds is not only a placeholder;
- detectors/placeholder_ref.py (NZ_EN_SKIP, English corpora only): an amendment direction names the provision it repeals
  or amends ("repeal section 169AA", "In section 5(2), replace ...", "Section 365(2): insert ..."); a section inside a
  range ("sections 117 to 119A") is not cited for itself; "Article 9" of a convention set out in a schedule is not
  section 9 of the Act;
- detectors/dead_fine.py (NZ_DF_DUP_LIVE, NZ_DF_EN_SKIP, NZ_DF_IMPORT): the same two rules for dead fines: a live "-N" file
  keeps its number alive ("competition study (as defined in section 48)", Commerce Act s 100, where sec-048-2.md is the
  new section 48), and in English corpora a section inside a range or named by an amendment direction is not relied on.

    python -X utf8 patch_en_nz.py <scripts dir>
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
    ("NZ_O_SUFFIX",
     '    if s in ("o", "º"):          # ordinal marker ("4o.", "1º"), not a suffix\n',
     '    if s == "º" or (s == "o" and _LANG["v"] != "en"):  # ordinal marker ("4o.", "1º"), not a suffix\n'
     '        # NZ_O_SUFFIX: in English "o" is a letter suffix (New Zealand\'s section 312O, 216O)\n'),
    ("NZ_AMENDED_ENACTMENT",
     '    if _LANG["v"] == "de":  # "§§ 70 bis 75" is a range, not § 70bis\n',
     '    if _LANG["v"] == "en":  # NZ_AMENDED_ENACTMENT: from a heading line "Animal Products Act 1999 (1999 No 93)" on, a\n'
     '        # schedule of consequential amendments or of enactments repealed cites those enactments, not its own Act\n'
     '        _h = re.search(r"(?m)^[A-Z][^\\n]{2,200}\\((?:\\d{4} No \\d+|SR \\d{4}/\\d+|LI \\d{4}/\\d+)\\)\\s*$", body)\n'
     '        if _h:\n'
     '            body = body[:_h.start()]\n'
     '    if _LANG["v"] == "de":  # "§§ 70 bis 75" is a range, not § 70bis\n'),
    ("NZ_LINE_BREAK",
     '            tail = body[m.end():m.end() + 70]\n',
     '            tail = body[m.end():m.end() + 70]\n'
     '            if rx is REF and _LANG["v"] == "en" and "\\n" in m.group(0):\n'
     '                continue  # NZ_LINE_BREAK: "regulation" ending one line, "17 Purpose of ..." opening the next\n'),
    ("NZ_ACT_BEFORE",
     '            if is_external(before, tail):\n',
     '            if _LANG["v"] == "en" and re.search(r"\\b(?:Act|Regulations|Rules|Order|Code)\\s+\\d{4}(?:\\s+\\([^)]*\\))?\\s*[,:]\\s*(?:\\S+\\s+){0,3}$", before):\n'
     '                continue  # NZ_ACT_BEFORE: "Piracy Act 1850: section 6", "Chemical Weapons (Prohibition) Act 1996, section 6"\n'
     '            if is_external(before, tail):\n'),
    ("NZ_OF_ACT",
     '                    ks, end = _expand(body, m, first)\n',
     '                    ks, end = _expand(body, m, first)\n'
     '                    if _LANG["v"] == "en" and EN_OF_ACT.match(body, end):  # NZ_OF_ACT\n'
     '                        seen_spans.append((m.start(), end))\n'
     '                        continue  # "sections 9(2), 10, and 11 of the Family Violence Act 2018"\n'),
    ("NZ_OF_ACT_RX",
     'def before_ref(ctx: str, tail: str) -> str:\n',
     '# NZ_OF_ACT_RX: subsections, a list or a range, then "of the <Name> Act ..." or "of that Act": another enactment\n'
     'EN_OF_ACT = re.compile(r"(?:\\s*\\([0-9A-Za-z]{1,6}\\))*(?:\\s*(?:,\\s*(?:and\\b|or\\b)?|\\band\\b|\\bor\\b|\\bto\\b)\\s*(?:(?:sections?|ss?)\\s+)?\\d{1,4}[A-Z]{0,3}"\n'
     '                       r"(?:\\s*\\([0-9A-Za-z]{1,6}\\))*)*\\s*,?\\s+of\\s+(?:that\\s+Act\\b|the\\s+(?:former|principal|repealed|\\d{4})\\s+Act\\b|"\n'
     '                       r"(?:the\\s+)?[A-Z][\\w\'’\\-]*(?:\\s+(?:of|and|for|to|on|in|the|[A-Z][\\w\'’()\\-]*|\\(\\w[^)]{0,30}\\)))*?\\s+"\n'
     '                       r"(?:Act|Regulations|Rules|Order|Code|Convention|Treaty|Agreement|Protocol)\\b)")\n\n\n'
     'def before_ref(ctx: str, tail: str) -> str:\n'),
])

patch("ingest/textscan.py", [
    ("NZ_MILLION",
     '        v = norm_num(n)\n',
     '        v = norm_num(n)\n'
     '        if _LANG["v"] == "en" and m.group("c1"):  # NZ_MILLION: "$10 million" is 10000000, not 10\n'
     '            mm = re.match(r"\\s+(million|billion)\\b", text[m.end():m.end() + 12], re.I)\n'
     '            if mm:\n'
     '                v = str(round(float(v) * (10 ** 6 if mm.group(1).lower() == "million" else 10 ** 9)))\n'),
])

patch("detectors/placeholder_ref.py", [
    ("NZ_DUP_LIVE",
     "    if not holders:\n        return []\n",
     "    # NZ_DUP_LIVE: a number that a live provision also holds (new-zealand-law keeps the repealed section 57G as\n"
     "    # sec-057g.md and the new section 57G as sec-057g-2.md) is not only a placeholder\n"
     "    for path, t in text.items():\n"
     "        mm = re.match(r\"^(.*)-\\d\\.md$\", path)\n"
     "        if mm and not path_key(path) and not is_placeholder(t):\n"
     "            k2 = path_key(mm.group(1) + \".md\")\n"
     "            if k2:\n"
     "                holders.pop((act_of(path), k2), None)\n"
     "    if not holders:\n        return []\n"),
    ("NZ_EN_SKIP",
     "            if not h or h[0] == path or EXTERNAL.match(tail) or is_external(before_ref(ctx, tail), tail):\n                continue\n",
     "            if not h or h[0] == path or EXTERNAL.match(tail) or is_external(before_ref(ctx, tail), tail):\n                continue\n"
     "            if (c.get(\"language\") or \"\").lower() == \"en\" and en_skip(k, ctx, tail, h[0]):\n"
     "                continue  # NZ_EN_SKIP\n"),
    ("NZ_EN_SKIP_FN",
     "def is_placeholder(text: str) -> bool:\n",
     "def en_skip(k: str, ctx: str, tail: str, target: str) -> bool:\n"
     "    \"\"\"NZ_EN_SKIP_FN: English references that name a repealed provision without relying on it\"\"\"\n"
     "    b = before_ref(ctx, tail)\n"
     "    if re.search(r\"(?i)\\b(?:repeal|revoke|replace|omit|amend|substitute)\\s+(?:sections?|subsections?|ss?\\.?)\\s*$\", b):\n"
     "        return True  # an amendment direction: \"repeal section 169AA\"\n"
     "    if re.match(r\"(?i)^(?:\\s*\\([0-9A-Za-z]{1,6}\\))*\\s*[,:]\\s*(?:replace|delete|insert|repeal|omit|add|revoke|substitute)\\b\", tail):\n"
     "        return True  # \"In section 5(2), replace ...\", \"Section 365(2): insert ...\", \"After section 7, insert\"\n"
     "    if re.search(r\"(?i)\\barticles?\\s*$\", b) and target.rsplit(\"/\", 1)[-1].startswith(\"sec-\"):\n"
     "        return True  # \"Article 9\" of a convention set out in a schedule is not section 9\n"
     "    km = re.match(r\"(\\d+)([a-z]*)$\", k)\n"
     "    if km:\n"
     "        kk = (int(km.group(1)), km.group(2))\n"
     "        for r in re.finditer(r\"(?i)(?:\\b(?:sections?|ss)\\s+|,\\s*(?:and\\s+)?|\\band\\s+)(\\d{1,4})([A-Z]{0,3})\\s*(?:to|–|-)\\s*(?:section\\s+)?(\\d{1,4})([A-Z]{0,3})\\b\", ctx):\n"
     "            if (int(r.group(1)), r.group(2).lower()) < kk < (int(r.group(3)), r.group(4).lower()):\n"
     "                return True  # inside a range (\"sections 117 to 119A\"): not cited for itself\n"
     "    return False\n\n\n"
     "def is_placeholder(text: str) -> bool:\n"),
])

patch("detectors/dead_fine.py", [
    ("NZ_DF_DUP_LIVE",
     '            status[k] = ("placeholder", p) if is_placeholder(t) else ("live", p)\n',
     '            status[k] = ("placeholder", p) if is_placeholder(t) else ("live", p)\n'
     '    for p, t in files.items():  # NZ_DF_DUP_LIVE: "sec-048-2.md" holds a live section 48 beside the repealed one\n'
     '        mm = re.match(r"^(.*)-\\d\\.md$", p)\n'
     '        if mm and not path_key(p) and not is_placeholder(t):\n'
     '            k2 = path_key(mm.group(1) + ".md")\n'
     '            if k2:\n'
     '                status[k2] = ("live", p)\n'),
    ("NZ_DF_EN_SKIP",
     '            if st and st[0] == "placeholder":\n',
     '            if st and st[0] == "placeholder" and _REFLANG["v"] == "en" and en_skip(k, ctx, tail, st[1]):\n'
     '                continue  # NZ_DF_EN_SKIP: amendment directions, sections inside a range, a convention\'s articles\n'
     '            if st and st[0] == "placeholder":\n'),
    ("NZ_DF_IMPORT",
     "from placeholder_ref import is_placeholder, EXTERNAL\n",
     "from placeholder_ref import is_placeholder, EXTERNAL\n"
     "from placeholder_ref import en_skip  # NZ_DF_IMPORT\n"
     "from refscan import _LANG as _REFLANG\n"),
])
