"""Italian fixes (san-marino-law) for the copy of global-law's scripts:
 1. ingest/textscan.py: in an Italian ("it") text, deadlines "entro il 30 giugno 2021", "entro e non oltre il ...",
    "non oltre il ...", and "fino alla data del ...", "sino alle ore 05.00 del ...", an extension's new end ("prorogato al
    31 marzo 2015", "differito al ...") and the end of a period ("dal 1 luglio 2023 al 30 settembre 2023") are time
    limits; "fino al" and "sino al" were read already. "entro" and "non oltre" mark a deadline, as "no later than" does,
    so the empty-period search leaves them out;
 2. detectors/text_detectors.py: "entro il", "entro e non oltre" and "non oltre il" count as deadline wording in the
    score of a lapsed time limit, as "not later than" does;
 3. detectors/placeholder_ref.py: an Italian repeal clause ("È abrogato il Regolamento 15 aprile 2016 n.8", "Sono
    abrogati: ...", "Sono abrogate tutte le norme in contrasto con la presente legge", "Il secondo comma dell'articolo 97
    della Legge 70/2004 è abrogato") is the repealing provision, not a repeal placeholder, as "sont abrogés" and
    "quedan derogados" already were;
 4. ingest/refscan.py: in an Italian text, "articolo 14, comma 1 della Legge 16 dicembre 2013 n.166" (a paragraph,
    letter or number, then another act) cites another act, not this act's article 14;
 5. detectors/currency_scan.py: in an Italian text, lire written "L.5.000.000" or "L. 10.000", in words ("lire
    sessantamila", "lire cento") and as "20 milioni di lire" are dead currency (only "5.000 lire" and "lire 50" were read);
 6. detectors/notes_scan.py (every language): the English publisher's note "So in original" only as words of its own,
    not inside the Italian "trasmesso in originale" or "sia esso in originale".
    python -X utf8 patch_it.py <scripts dir>        (each change carries a patch_it marker; one already in place is skipped)"""
import os, sys

S = sys.argv[1]
FIXES = {
    os.path.join(S, "ingest", "textscan.py"): [
        ("Italian deadlines, extensions and period ends (definition)",
         'LIMIT = re.compile(rf"(?i)\\b(?:{UNTIL})\\s*(?:{FILL}){{0,2}}(?:{DATE})")\n',
         'LIMIT = re.compile(rf"(?i)\\b(?:{UNTIL})\\s*(?:{FILL}){{0,2}}(?:{DATE})")\n'
         '# patch_it: Italian deadlines ("entro il 30 giugno 2021", "entro e non oltre il", "non oltre il"), "fino alla data del",\n'
         '# "sino alle ore 05.00 del", an extension\'s new end ("prorogato al 31 marzo 2015") and a period\'s end ("dal 1 luglio\n'
         '# 2023 al 30 settembre 2023"); "fino al" and "sino al" are in UNTIL. Read only in an Italian ("it") text.\n'
         'IT_UNTIL = (r"entro\\s+e\\s+non\\s+oltre|non\\s+oltre|entro|(?:fino|sino)\\s+alla\\s+data\\s+del|(?:fino|sino)\\s+alle\\s+ore\\s+\\d{1,2}[.:]\\d{2}\\s+del|"\n'
         '            r"(?:prorogat|differit|posticipat|rinviat)[oaie]\\s+(?:al|all[\'’])")\n'
         'LIMIT_IT = re.compile(rf"(?i)(?:\\b(?:{IT_UNTIL})|(?<=\\d{{4}}\\s)(?:al|all[\'’]))\\s*(?:{FILL}){{0,2}}(?:{DATE})")\n',
         "LIMIT_IT = re.compile("),
        ("Italian deadlines, extensions and period ends (read)",
         '    if _LANG["v"] == "mn":  # patch_mn\n        post += list(LIMIT_MN.finditer(text))\n',
         '    if _LANG["v"] == "mn":  # patch_mn\n        post += list(LIMIT_MN.finditer(text))\n'
         '    if _LANG["v"] == "it":  # patch_it\n        post += list(LIMIT_IT.finditer(text))\n',
         "post += list(LIMIT_IT.finditer(text))"),
        ("entro / non oltre mark a deadline",
         "        if not deadlines and m.re is LIMIT_AZ and re.search(r\"(?i)gec\\s+olma\", m.group(0)):\n            continue\n",
         "        if not deadlines and m.re is LIMIT_AZ and re.search(r\"(?i)gec\\s+olma\", m.group(0)):\n            continue\n"
         "        if not deadlines and m.re is LIMIT_IT and re.match(r\"(?i)(?:entro|non\\s+oltre)\\b\", m.group(0)):\n"
         "            continue  # patch_it: \"entro il\", \"non oltre il\" give a deadline\n",
         "m.re is LIMIT_IT and re.match"),
    ],
    os.path.join(S, "detectors", "text_detectors.py"): [
        ("Italian deadline wording in the score",
         "'(not later than|no later than|spätestens",
         "'(entro il|entro e non oltre|non oltre il|not later than|no later than|spätestens",
         "'(entro il|entro e non oltre|non oltre il|"),
    ],
    os.path.join(S, "detectors", "placeholder_ref.py"): [
        ("Italian repeal clauses are not placeholders",
         "|sont abrog|quedan derogad|",
         "|sont abrog|quedan derogad|(?#patch_it)\\b(?:è|e['’]|sono|viene|vengono)\\s+(?:(?:altresì|espressamente|definitivamente|inoltre|pertanto|in particolare)\\s+)?abrogat|"
         "\\bs['’]intende\\s+(?:comunque\\s+)?abrogat|\\babrogat[oaie]\\s*:|in\\s+contrasto\\s+con\\s+la\\s+presente|"
         "\\b(?:legge|decreto|regolamento|articol[oi]|comm[ai]|titolo|capo|disposizion\\w*|norm\\w*)\\b[^;:]{0,80}?\\s(?:è|e['’]|sono)\\s+abrogat|",
         "(?#patch_it)"),
    ],
    os.path.join(S, "ingest", "refscan.py"): [
        ("Italian: a paragraph, letter or number of another act",
         '    return bool((_LANG["v"] == "pt" and EXT_AFTER_PT.match(tail))',
         '    if _LANG["v"] == "it" and EXT_AFTER_IT.match(tail):  # patch_it\n        return True\n'
         '    return bool((_LANG["v"] == "pt" and EXT_AFTER_PT.match(tail))',
         "EXT_AFTER_IT.match(tail):  # patch_it"),
        ("Italian: a paragraph, letter or number of another act (pattern)",
         'EXT_AFTER_PT = re.compile(EXT_AFTER_PT.pattern.replace(r"\\d+[º°]?", r"\\d+\\.?[º°]?"))\n',
         'EXT_AFTER_PT = re.compile(EXT_AFTER_PT.pattern.replace(r"\\d+[º°]?", r"\\d+\\.?[º°]?"))\n\n\n'
         '# patch_it: "articolo 14, comma 1 della Legge 16 dicembre 2013 n.166", "art. 5, primo comma, lettera b) del Decreto ..."\n'
         '# name another act; "del presente decreto" and "della medesima legge" are this one\n'
         '_IT_SUF = r"(?:[\\s-]*(?:bis|ter|quater|quinquies|sexies|septies|octies|novies|decies))?"\n'
         'EXT_AFTER_IT = re.compile(rf"(?i)^{_IT_SUF}(?:\\s*(?:,|e|ed)\\s*\\d+{_IT_SUF})*\\s*(?:(?:,\\s*|\\s+)(?:(?:primo|secondo|terzo|quarto|quinto|sesto|settimo|ottavo|nono|decimo|ultimo)\\s+comma|"\n'
         '                          rf"comm[ai]\\s+\\d+{_IT_SUF}|letter[ae]\\s+[a-z]{{1,2}}\\)?|lett\\.\\s*[a-z]{{1,2}}\\)?|numer[oi]\\s+\\d+\\)?|n\\.\\s*\\d+\\)?|punto\\s+\\d+[.)]?)"\n'
         '                          rf"(?:\\s*(?:,|e|ed)\\s*(?:\\d+{_IT_SUF}|[a-z]{{1,2}}\\)))*)*\\s*,?\\s*(?:del|della|dello|dei|degli|delle|al|alla|allo|ai|agli|alle|nel|nella)\\s+"\n'
         '                          r"(?!presente|medesim|stess)(?:Legge|Decreto|Regolamento|Codice|Costituzione|Dichiarazione|Delibera|Statuto|Convenzione|"\n'
         '                          r"Trattato|Accordo|Direttiva|Testo\\s+Unico|D\\.\\s?D\\.|D\\.\\s?L\\.|L\\.)")\n',
         "EXT_AFTER_IT = re.compile("),
    ],
    os.path.join(S, "detectors", "notes_scan.py"): [
        ("'So in original' as words, not inside 'esso in originale'",
         'r"[Ss]o in original", ',
         'r"(^|[^A-Za-z])[Ss]o in original([^A-Za-z]|$)", ',
         'r"(^|[^A-Za-z])[Ss]o in original'),
    ],
    os.path.join(S, "detectors", "currency_scan.py"): [
        ("Italian lire as L.<amount>, in words and in millions",
         '    return rf"{NUM}\\s*{cur}|{cur}\\s*{NUM}"\n',
         '    if (c.get("language") or "").lower() == "it":  # patch_it: "L.5.000.000", "lire sessantamila", "20 milioni di lire"\n'
         '        cur = cur[:-1] + r"|(?-i:(?<![A-Za-z])L\\.)(?=\\s?[0-9]{1,3}(?:\\.[0-9]{3})+))"\n'
         '        return (rf"{NUM}\\s*{cur}|{cur}\\s*{NUM}|\\blire\\s+[a-zà]*(?:mila|mille|cento|milion[ei]|miliard[oi])[a-zà]*\\b"\n'
         '                r"|\\b[0-9][0-9.,]*\\s+(?:milion[ei]|miliard[oi])\\s+di\\s+lire\\b")\n'
         '    return rf"{NUM}\\s*{cur}|{cur}\\s*{NUM}"\n',
         "# patch_it: \"L.5.000.000\""),
    ],
}
for p, fixes in FIXES.items():
    s = open(p, encoding="utf-8").read()
    for name, old, new, mark in fixes:
        if mark in s:
            print("already in place:", name)
            continue
        if old not in s:
            raise SystemExit(f"not found: {name}")
        n = s.count(old)
        s = s.replace(old, new)
        print("patched:", name, f"({n} places)" if n > 1 else "")
    open(p, "w", encoding="utf-8", newline="\n").write(s)
