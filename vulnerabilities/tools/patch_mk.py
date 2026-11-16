"""North Macedonia fixes for the copy of global-law's scripts:
 1. ingest/textscan.py: the Macedonian month names ("јануари", "мај", "јуни", "јули"; the other eight are spelled as in
    Bulgarian and already read), so "до 30 јуни 2020 година" is a time limit;
 2. ingest/textscan.py: "до крајот на 2020 година" (until the end of 2020) is 31 December of that year;
 3. ingest/textscan.py: "заклучно со" (up to and including) before a date is a time limit, and "најдоцна" (at the
    latest) marks a deadline, as "najkasnije" does; and in a Macedonian ("mk") text "по" before a date is "after"
    ("по 1 јануари 2009"), not the Russian "up to", so it starts no time limit;
 4. ingest/refscan.py: "clen-007.md" (the Constitution's and the data protection law's files) is article 7;
 5. detectors/currency_scan.py: for Macedonian ("mk") texts, amounts in Yugoslav dinars ("динари") and Deutsche Marks
    ("германски марки") written in Cyrillic are dead currencies (the denar, "денар", is not touched).
    python -X utf8 patch_mk.py <scripts dir>        (a fix already in place is skipped)"""
import os, sys

S = sys.argv[1]
FIXES = {
    os.path.join(S, "ingest", "textscan.py"): [
        ("Macedonian months",
         '"януари февруари март април май юни юли август септември октомври ноември декември "\n',
         '"януари февруари март април май юни юли август септември октомври ноември декември "\n'
         '          "јануари февруари март април мај јуни јули август септември октомври ноември декември "  # patch_mk\n',
         '"јануари февруари март април мај јуни јули'),
        ("до крајот на <year>", r'края\s+на\s+|', r'края\s+на\s+|крајот\s+на\s+|', r'крајот\s+на\s+|'),
        ("заклучно со", r'zaključno sa|zaključno s|', r'zaključno sa|zaključno s|заклучно со|', "заклучно со|"),
        ("најдоцна", r'najkasnije|', r'najkasnije|најдоцна|', "најдоцна|"),
        ("по <date> is after, not until (mk)",
         '            continue  # patch_mo: Portuguese "do" is "of the" ("a partir do dia 1 de Julho"), not the Slavic "until"\n',
         '            continue  # patch_mo: Portuguese "do" is "of the" ("a partir do dia 1 de Julho"), not the Slavic "until"\n'
         '        if _LANG["v"] == "mk" and re.match(r"(?i)по\\b", m.group(0)):\n'
         '            continue  # patch_mk: Macedonian "по 1 јануари 2009" is "after 1 January 2009", not the Russian "until"\n',
         '# patch_mk: Macedonian "по 1 јануари 2009"'),
    ],
    os.path.join(S, "ingest", "refscan.py"): [
        ("clen-N file names", "clanek|clanak|clan|", "clanek|clanak|clan|clen|", "clanak|clan|clen|"),
    ],
    os.path.join(S, "detectors", "currency_scan.py"): [
        ("Cyrillic dinars and Deutsche Marks (mk)",
         "EXTRA_CURRENCY = {}  # by language; the schilling is by code (AT), below\n",
         "EXTRA_CURRENCY = {}  # by language; the schilling is by code (AT), below\n"
         "# patch_mk: Macedonian texts write the Yugoslav dinar (replaced by the denar in 1992) and the Deutsche Mark in\n"
         "# Cyrillic; the denar (\"денар\") is current. Spelled out in each case, as git grep -P may not fold Cyrillic case.\n"
         'EXTRA_CURRENCY["mk"] = r"|динар|Динар|ДИНАР|германски марк|германски Марк|Германски марк"\n',
         'EXTRA_CURRENCY["mk"]'),
    ],
}
for p, fixes in FIXES.items():
    s = open(p, encoding="utf-8").read()
    for name, old, new, mark in fixes:
        if mark in s:
            print("already in place:", name)
            continue
        assert s.count(old) == 1, f"not found: {name}"
        s = s.replace(old, new, 1)
        print("patched:", name)
    open(p, "w", encoding="utf-8", newline="\n").write(s)
