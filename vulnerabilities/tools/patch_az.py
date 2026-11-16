"""Azerbaijani blind spots, in a copy of global-law's vulnerabilities/scripts (idempotent: a second run changes nothing):
- ingest/textscan.py: Azerbaijani dates and time limits, none of which the time-limit search read:
  "2020-ci il dekabrın 31-dək", "1997-ci il dekabrın 31-nə qədər", "2019-cu il avqust ayının 18-dək",
  "31 dekabr 2020-ci il tarixinədək" (also "tarixədək", "tarixinə qədər"), "2020-ci il 1 yanvar tarixinədək",
  "2020-ci ilin sonunadək" / "maliyyə ilinin sonunadək" (31 December), and the deadlines "ən geci" and
  "...-dən gec olmayaraq" / "gec olmamaq" (read as deadlines, as the other languages' "not later than");
  e-qanun's notes at the end of each file ("[^1]: ... Qanunu ilə ...", which quote earlier wording after "əvvəlki
  redaksiyada deyilirdi:") are not read as the provision's text; "100 manatadək", "manatdan" are manat amounts.
- ingest/refscan.py: "Bu Qanunun 12.3-cü maddəsi" and "10-1.2-ci maddə" (article and part numbered with a dot) are
  references to article 12 and 10; "... Məcəlləsinin 5-ci maddəsi", "... Qanununun 7-ci maddəsi" name another act;
  "Qanunvericilik Toplusu, 2004-cü il, № 3, maddə 123" is a gazette entry, not article 123; e-qanun's notes are skipped.
- ingest/textscan.py amounts: "lari" read the plural ending "-ları" after a number ("2625-ları") as the Georgian lari
  (Python's case-insensitive match takes the dotless ı for i): a unit with a dotless ı is not a currency.
- detectors/currency_scan.py: in Azerbaijani, "lira" is the Turkish lira (in use), "inti" is inside "tikinti"
  (construction), and the dinars named are in use: none is a dead currency.
- detectors/placeholder_ref.py: sets refscan's language before calling refs(), which it never did, so the two refscan
  fixes above (notes, gazette entries) apply to the search for references to repealed placeholders too.
Every fix carries a marker (a piece of its own text that later patches leave alone), so a second run, also after other
patches have edited the lines around a fix, changes nothing; run it after the kit's other patches (apply_patches.py).
"2010-cu ilədək" ("until 2010") is left unread: it does not say which day of the year.

    python -X utf8 patch_az.py <scripts dir>
"""
import sys
from pathlib import Path


def patch(rel, pairs):
    """each pair: (name, anchor, replacement, marker). The marker is a piece of the replacement that later patches leave
    alone, so a fix already in place is found even when other patches have since edited the lines around it. An anchor
    may be a tuple of alternatives (the first found is used); the replacement may then be a function of that anchor."""
    p = Path(sys.argv[1]) / rel
    s = p.read_text(encoding="utf-8")
    for name, a, b, marker in pairs:
        if marker in s:
            print("in place:", name)
            continue
        a = next((x for x in (a if isinstance(a, tuple) else (a,)) if x in s), None)
        if a is None:
            raise SystemExit(f"not found: {name}")
        s = s.replace(a, b(a) if callable(b) else b, 1)
        print("patched:", name)
    p.write_text(s, encoding="utf-8", newline="\n")


AZ_BLOCK = r'''# Azerbaijani (patch_az.py): the date comes first and the "until" is a suffix: "2020-ci il dekabrın 31-dək",
# "31 dekabr 2020-ci il tarixinədək", "2020-ci il 1 yanvar tarixinədək", "2020-ci ilin sonunadək"
AZ_MONTHS = "yanvar fevral mart aprel may iyun iyul avqust sentyabr oktyabr noyabr dekabr".split()
_AZM = "(?:" + "|".join(AZ_MONTHS) + ")"
_AZY = r"\s?-?\s?c[iıuü]\s+il(?:in)?"
_AZ_TILL = r"(?:tarix(?:in)?ədək|tarix(?:in)?ə\s+(?:qədər|kimi)|tarix(?:in)?dən\s+gec\s+olma(?:yaraq|maq))"
LIMIT_AZ = re.compile(
    rf"(?i)(?<!\d)(?P<azy1>\d{{4}}){_AZY}\s+(?P<azm1>{_AZM})(?:ın|in|un|ün)?(?:\s+ayının)?\s+(?P<azd1>\d{{1,2}})"
    rf"\s?-\s?(?:[a-zəıöüçşğ]{{0,3}}\s?(?:dək|qədər)\b|d[əa]n\s+gec\s+olma(?:yaraq|maq))"
    rf"|(?<!\d)(?P<azd2>\d{{1,2}})\s+(?P<azm2>{_AZM})\s+(?P<azy2>\d{{4}}){_AZY}\s+{_AZ_TILL}"
    rf"|(?<!\d)(?P<azy3>\d{{4}}){_AZY}\s+(?P<azd3>\d{{1,2}})\s+(?P<azm3>{_AZM})\s+{_AZ_TILL}"
    rf"|(?<!\d)(?P<azy5>\d{{4}}){_AZY}\s+(?:(?:maliyyə|təqvim|büdcə)\s+ilinin\s+)?(?:sonunadək|sonuna\s+qədər|sonuna\s+kimi|"
    rf"axırınadək|axırına\s+qədər|sonundan\s+gec\s+olma(?:yaraq|maq))")
_AZ_WORDS = re.compile(r"(?i)dək\b|qədər|kimi\b|gec\s+olma")
AZ_NOTES = re.compile(r"(?m)^\[\^\d+\]:")


def az_body(text: str) -> str:
    """the provision without e-qanun's notes (and the earlier wording they quote) at the end of the file"""
    m = AZ_NOTES.search(text)
    return text[:m.start()] if m else text


def _az_ymd(g):
    for i in ("1", "2", "3"):
        if g.get("azy" + i):
            mon = g["azm" + i].lower().replace("i̇", "i").replace("İ", "i")
            return int(g["azy" + i]), next(n for n, s in enumerate(AZ_MONTHS, 1) if mon.startswith(s)), int(g["azd" + i])
    if g.get("azy5"):
        return int(g["azy5"]), 12, 31
    return None


AZ_MANAT = re.compile(r"(?i)\bmanat[a-zəıöüçşğ]+")
ROMAN = {r: i for i, r in'''

patch("ingest/textscan.py", [
    ("az: LIMIT_AZ block", "ROMAN = {r: i for i, r in", AZ_BLOCK, "LIMIT_AZ = re.compile("),
    ("az: DEADLINE ən geci", 'DEADLINE = (r"', 'DEADLINE = (r"ən geci|ən gec|', 'r"ən geci|'),
    ("az: limits() reads LIMIT_AZ",
     "    post = list(LIMIT_POST.finditer(text)) if _POST_WORDS.search(text) else []\n",
     "    post = list(LIMIT_POST.finditer(text)) if _POST_WORDS.search(text) else []\n"
     "    if _LANG[\"v\"] == \"az\":  # patch_az.py\n"
     "        text = az_body(text)\n"
     "        post = [m for m in post if m.end() <= len(text)] + (list(LIMIT_AZ.finditer(text)) if _AZ_WORDS.search(text) else [])\n",
     "list(LIMIT_AZ.finditer(text))"),
    ("az: deadline suffix", "        g = m.groupdict()\n",
     "        g = m.groupdict()\n"
     "        if not deadlines and m.re is LIMIT_AZ and re.search(r\"(?i)gec\\s+olma\", m.group(0)):\n"
     "            continue\n",
     "m.re is LIMIT_AZ"),
    # the first branch of the date chain: global-law's, or patch_mn.py's Mongolian one put before it
    ("az: date from LIMIT_AZ", ('            if g.get("y10"):', '            if g.get("y6") or g.get("y7"):'),
     lambda a: '            if _az_ymd(g):\n                y, mo, d = _az_ymd(g)\n            el' + a.lstrip(" "),
     "if _az_ymd(g):"),
    ("az: manat with a suffix", "def amounts(text: str) -> set[tuple[str, str]]:\n    out = set()\n",
     "def amounts(text: str) -> set[tuple[str, str]]:\n    out = set()\n"
     "    if _LANG[\"v\"] == \"az\":  # patch_az.py: '100 manatadək', 'manatdan'\n"
     "        text = AZ_MANAT.sub(\"manat\", text)\n",
     "AZ_MANAT.sub("),
    ("az: current text without notes", "        if len(text) > 2_000_000:\n            continue\n        for u, ctx in limits(text):",
     "        if len(text) > 2_000_000:\n            continue\n        if _LANG[\"v\"] == \"az\":\n            text = az_body(text)\n"
     "        for u, ctx in limits(text):",
     "            text = az_body(text)\n        for u, ctx in limits(text):"),
    ("az: amendments without notes", "        a, b = next(texts)[1], next(texts)[1]\n",
     "        a, b = next(texts)[1], next(texts)[1]\n        if _LANG[\"v\"] == \"az\":\n            a, b = az_body(a), az_body(b)\n",
     "a, b = az_body(a), az_body(b)"),
])
patch("ingest/textscan.py", [
    ("az: no unit with a dotless i", "        c = (m.group(\"c1\") or m.group(\"c2\") or \"\").lower()\n",
     "        c = (m.group(\"c1\") or m.group(\"c2\") or \"\").lower()\n"
     "        if \"ı\" in c:  # patch_az.py: the plural '-ları' after a number ('2625-ları') is not the Georgian lari\n"
     "            continue\n",
     "patch_az.py: the plural '-ları'"),
])
patch("detectors/currency_scan.py", [
    ("az: not currencies in Azerbaijani", r'NOT_CURRENCY = {',
     r'NOT_CURRENCY = {"az": (r"\blira(?!glutid)\w{0,6}|", r"intis?\b|", r"|dinara?"), ', r'"az": ('),
])
# limits() is defined after the block, and LIMIT_POST's matches beyond the cut notes are dropped before LIMIT's are
# re-read on the cut text; LIMIT itself runs on `text`, which is now the cut text, since the sort line reads it after.
patch("ingest/refscan.py", [
    ("az: 12.3-cü maddəsi", r'r"(?:-\d{1,3})?[-\s]?(?:ci|cı|cu|cü|nci', r'r"(?:[-.]\d{1,3}){0,4}[-\s]?(?:ci|cı|cu|cü|nci',
     r'(?:[-.]\d{1,3}){0,4}[-\s]?(?:ci|'),
    ("az: another act named before", 'EXT_BEFORE = re.compile(r"(?i)(?:',
     'EXT_BEFORE = re.compile(r"(?i)(?:(?:Qanununun|Məcəlləsinin|Konstitusiyasının|Konvensiyasının|Sazişinin|Sazişin|'
     'Müqaviləsinin|Protokolunun|Əsasnaməsinin|Nizamnaməsinin|Qaydalarının|Fərmanının|Qərarının|Aktının|Qanunu|Məcəlləsi)[”\\"»]?|',
     "(?:(?:Qanununun|Məcəlləsinin|Konstitusiyasının|"),
    ("az: notes skipped",
     '    """(key, context, tail) for every reference to a numbered provision in the body of a provision file."""\n',
     '    """(key, context, tail) for every reference to a numbered provision in the body of a provision file."""\n'
     '    if _LANG["v"] == "az":  # patch_az.py: e-qanun\'s notes (and the earlier wording they quote) end the file\n'
     '        n = re.search(r"(?m)^\\[\\^\\d+\\]:", text)\n'
     '        text = text[:n.start()] if n else text\n',
     "patch_az.py: e-qanun's notes"),
    ("az: gazette entry", "            if is_external(before, tail):\n",
     "            if _LANG[\"v\"] == \"az\" and re.search(r\"№\\s*\\d+\\s*,?\\s*$\", before):\n"
     "                continue  # patch_az.py: 'Qanunvericilik Toplusu, 2004-cü il, № 3, maddə 123' is a gazette entry\n"
     "            if is_external(before, tail):\n",
     "is a gazette entry"),
])
# placeholder_ref.py calls refscan's refs() without setting refscan's language, so there refs() skipped no e-qanun note
# and no gazette entry ("Qanunvericilik Toplusu, 2004-cü il, № 10, maddə 761" was read as a reference to article 761)
patch("detectors/placeholder_ref.py", [
    ("az: refs() knows the language", "def one(c):\n    lower_priority()\n",
     "def one(c):\n    lower_priority()\n"
     "    sys.modules[\"refscan\"]._LANG[\"v\"] = (c.get(\"language\") or \"\").lower()  # patch_az.py: refs() reads the language\n",
     "sys.modules[\"refscan\"]._LANG[\"v\"]"),
])
