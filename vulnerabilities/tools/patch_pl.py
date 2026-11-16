"""Poland fixes for the copy of global-law's scripts:
 1. ingest/textscan.py: "nie później niż" (not later than) marks a deadline, as "najpóźniej" does, so "nie później niż
    do dnia 30 czerwca 2025 r." is not read as a time limit that lapses;
 2. ingest/textscan.py: "do końca 2035 r." and "do końca roku 1922" (until the end of the year) are 31 December of that year;
 3. ingest/refscan.py: in a Polish ("pl") article file ("# Art. 154.") "§ 2" is a paragraph of that article, not § 2 of the
    act (codes number their paragraphs §; regulations number their units §, and their files are par-*.md); and Polish
    never writes "7 §" or "7. §" (the Nordic and Hungarian forms), so "§ 2 i 3. § 7" is not § 3, and "s. 69" is a page;
 4. ingest/refscan.py: Polish inserted articles, "art. 4¹" and "art. 1153¹⁵ᵃ", are article 4-1 and 1153-15a (headings,
    references, list items such as "art. 14 i art. 15¹", and the files art-004-1.md, art-1153-15a.md), not article 4
    and 1153;
 5. ingest/refscan.py: a reference followed by another act's name ("art. 7 ust. 2 ustawy z dnia ...", "art. 8 Kodeksu
    cywilnego", "art. 51 ust. 1 unijnego kodeksu celnego", "art. 64 lub art. 65 Kodeksu karnego", "art. 10 i 11 k.c.")
    is to that act, also at the end of a list longer than the 70 characters the scan otherwise reads after a reference;
    "niniejszej ustawy" (this act) stays this act's; and "art. 47o" is article 47o, not article 47 with an ordinal "o";
 6. ingest/refscan.py: a heading line "(zawierający art. 62-70 - uchylony)" (a chapter whose articles were repealed) is a
    repeal note, as "(weggefallen)" is, so the articles it names are not references;
 7. detectors/placeholder_ref.py: in Polish a placeholder is a whole provision that reads only "(uchylony)" ("# Art. 23.
    (uchylony)"), not an article with one repealed point ("1. Ustawa określa:" then "- 1) (uchylony)"), and an article
    inside a span ("art. 759-774") is not cited on its own; "(pominięty)", an amending article a consolidated text
    leaves out, is not a repeal;
 8. detectors/text_detectors.py: "najpóźniej" and "nie później niż" mark a lapsed limit as a deadline (column `deadline`, and
    a lower score), as "nejpozději" does;
 9. detectors/dup_labels.py: "§ 2¹", a paragraph inserted after § 2, is not a second "§ 2";
10. detectors/currency_scan.py: pre-1995 złoty amounts written "złotych starych" or "starych złotych" (the kit had only
    the spelling without "ł").
    python -X utf8 patch_pl.py <scripts dir>        (a fix already in place is skipped)"""
import os, sys

S = sys.argv[1]
FIXES = {
    os.path.join(S, "ingest", "textscan.py"): [
        ("nie później niż", "najpóźniej|nejpozději|", "najpóźniej|nie później niż|nejpozději|", "nie później niż|"),
        ("do końca <year>", 'DATE = (r"(?:kraja\\s+|konce\\s+roku\\s+|',
         'DATE = (r"(?:kraja\\s+|konce\\s+roku\\s+|końca\\s+(?:roku\\s+)?|', "końca\\s+(?:roku\\s+)?|"),
    ],
    os.path.join(S, "ingest", "refscan.py"): [
        ("superscript map (pl)",
         "THAI_DIGITS = str.maketrans(",
         "# patch_pl: Polish inserted articles are numbered with superscripts (\"art. 4¹\", \"art. 1153¹⁵ᵃ\")\n"
         "PL_SUP = re.compile(\"[⁰¹²³⁴⁵⁶⁷⁸⁹]+[ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻ]?\")\n"
         "PL_SUP_TX = str.maketrans(\"⁰¹²³⁴⁵⁶⁷⁸⁹ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻ\", \"0123456789abcdefghijklmnoprstuvwxyz\")\n"
         "# patch_pl: another act named after the reference (\"art. 7 ust. 2 ustawy z dnia ...\", \"art. 8 Kodeksu cywilnego\",\n"
         "# \"art. 10 i 11 k.c.\"); \"niniejszej ustawy\" is this act\n"
         r'''EXT_AFTER_PL = re.compile(r"(?i)^[⁰¹²³⁴⁵⁶⁷⁸⁹ᵃ-ᶻ]*(?:(?:\s*,)?\s*(?:(?:i|oraz|lub|albo|a|do)\s+|[-–]\s*)?"
                          r"(?:art\.\s*\d{1,4}[a-z]{0,2}[⁰¹²³⁴⁵⁶⁷⁸⁹ᵃ-ᶻ]*(?!\w)|§\s*\d+\w*(?!\w)|ust\.\s*\d+\w*(?!\w)|pkt\s*\d+\w*(?!\w)|zdani[eau]\s+\w+|zd\.\s*\w+|tiret\s+\w+|akapit\w*\s+\w+|"
                          r"(?:dział|rozdział)\w*\s+(?:(?-i:[IVXLC]+[a-z]?)|\d+[a-z]?)(?:\s*(?:,|i|oraz)\s*(?:(?-i:[IVXLC]+[a-z]?)|\d+[a-z]?))*(?!\w)|"
                          r"lit\.\s*[a-z]+(?!\w)(?:\s*(?:,|i|oraz|lub|albo|-|–)\s*[a-z](?![\w.]))*|\d{1,4}[a-z]{0,2}[⁰¹²³⁴⁵⁶⁷⁸⁹ᵃ-ᶻ]*(?!\w)))*"
                          r"\s*,?\s*(?:(?!niniejsz|do\b|w\b|z\b|na\b|od\b|dla\b|i\b|oraz\b|lub\b|albo\b)[^\W\d]+\s+)?"
                          r"(?:ustaw\w*|kodeks\w*|konstytucj\w*|ordynacj\w*|rozporządze\w*|dekret\w*|konwencj\w*|umow\w*|traktat\w*|"
                          r"protok[oó]ł\w*|statut\w*|porozumie\w*|układu|uchwał\w*|zarządze\w*|regulamin\w*|dyrektyw\w*|prawa\s+\w+|"
                          r"k\.\s?[a-z]{1,2}\.(?:\s?[a-z]{1,2}\.)*)(?!\w)")
'''
         "THAI_DIGITS = str.maketrans(",
         "PL_SUP = re.compile("),
        ("Polish articles 47o, 20o (pl)",
         '    if s == "º" or (s == "o" and _LANG["v"] != "en"):',
         '    if s == "º" or (s == "o" and _LANG["v"] not in ("en", "pl")):  # patch_pl: article 47o is not 47',
         "# patch_pl: article 47o is not 47"),
        ("the act named after a long list (pl)",
         "            if is_external(before, tail):\n",
         "            if is_external(before, body[m.end():m.end() + 300] if _LANG[\"v\"] == \"pl\" else tail):  # patch_pl: a long list\n",
         "# patch_pl: a long list"),
        ("other act named after (pl)",
         "    if _LANG[\"v\"] == \"ru\" and EXT_AFTER_RU.match(tail):\n        return True\n",
         "    if _LANG[\"v\"] == \"ru\" and EXT_AFTER_RU.match(tail):\n        return True\n"
         "    if _LANG[\"v\"] == \"pl\" and EXT_AFTER_PL.match(tail):  # patch_pl\n        return True\n",
         "EXT_AFTER_PL.match(tail):  # patch_pl"),
        ("§ in an article file is a paragraph (pl)",
         "            if rx is NORDIC and _LANG[\"v\"] in NB_LANGS:\n",
         r'''            if _LANG["v"] == "pl" and (rx is NORDIC or (rx is PRE and m.group(0).rstrip().endswith("§")) or (rx is REF and re.match(r"(?i)s\.", m.group(0).lstrip()))):
                continue  # patch_pl: Polish writes "§ 7", never "7 §" or "7. §"; "s. 69" is a page (strona)
'''
         "            if _pl_art and rx is REF and m.group(0).lstrip().startswith(\"§\"):\n"
         "                continue  # patch_pl: in a Polish article (\"# Art. 154.\") \"§ 2\" is a paragraph of that article\n"
         "            if rx is NORDIC and _LANG[\"v\"] in NB_LANGS:\n",
         "# patch_pl: in a Polish article"),
        ("superscript in a list (pl)",
         "        if l and l.group(1):\n            keys.append(",
         r'''        _s = PL_SUP.match(body, l.end()) if l and l.group(1) and _LANG["v"] == "pl" else None
        if _s:  # patch_pl: "art. 14 i art. 15¹": article 15-1
            keys.append(f"{key(l.group(1), l.group(2), l.group(3))}-{_s.group(0).translate(PL_SUP_TX)}"); prev, pos = int(l.group(1).replace(".", "")), _s.end(); continue
'''
         "        if l and l.group(1):\n            keys.append(",
         "# patch_pl: \"art. 14 i art. 15¹\""),
        ("_pl_art flag",
         "    seen_spans = []\n    for rx in (REF,",
         "    seen_spans = []\n"
         "    _pl_art = _LANG[\"v\"] == \"pl\" and bool(re.search(r\"(?m)^#\\s*Art\\.\", text))  # patch_pl\n"
         "    for rx in (REF,",
         "_pl_art = _LANG[\"v\"] == \"pl\""),
        ("superscript reference (pl)",
         "                if nbx:  # patch_nb",
         "                plsup = PL_SUP.match(body, m.end()) if _LANG[\"v\"] == \"pl\" and not m.group(2) and not m.group(3) else None\n"
         "                if plsup:  # patch_pl: \"art. 4¹\" is article 4-1 (the list after it is not read)\n"
         "                    first = f\"{first}-{plsup.group(0).translate(PL_SUP_TX)}\"\n"
         "                    ks, end = [first], plsup.end()\n"
         "                elif nbx:  # patch_nb",
         "# patch_pl: \"art. 4¹\" is article 4-1"),
        ("superscript heading (pl)",
         "    if m.re is HEAD and _LANG[\"v\"] == \"ru\":",
         "    if m.re is HEAD and _LANG[\"v\"] == \"pl\" and not m.group(2) and not m.group(3):  # patch_pl: \"# Art. 4¹.\"\n"
         "        r = PL_SUP.match(m.string, m.end())\n"
         "        if r:\n"
         "            return f\"{_mkey(m)}-{r.group(0).translate(PL_SUP_TX)}\"\n"
         "    if m.re is HEAD and _LANG[\"v\"] == \"ru\":",
         "# patch_pl: \"# Art. 4¹.\""),
        ("superscript file names (pl)",
         "    r = re.match(r\"^statya-0*(\\d{1,4})-(\\d{1,3})$\", base)",
         "    if _LANG[\"v\"] == \"pl\":  # patch_pl: art-004-1.md is art. 4¹, art-1153-15a.md art. 1153¹⁵ᵃ\n"
         "        r = re.match(r\"^(?:art|par)-0*(\\d{1,4})-0*(\\d{1,3}[a-z]?)$\", base)\n"
         "        if r:\n"
         "            return f\"{int(r.group(1))}-{r.group(2)}\"\n"
         "    r = re.match(r\"^statya-0*(\\d{1,4})-(\\d{1,3})$\", base)",
         "# patch_pl: art-004-1.md"),
        ("uchylony in a repeal note (pl)", 'r"ուժը կորցրած|ძალადაკარგ|revogad|καταργ")',
         'r"ուժը կորցրած|ძალადაკარგ|revogad|καταργ|uchylon|pominięt")', "|uchylon|pominięt"),
    ],
    os.path.join(S, "detectors", "placeholder_ref.py"): [
        ("refscan's language (pl)",
         "from refscan import refs, path_key, act_of, is_external, before_ref\n",
         "from refscan import refs, path_key, act_of, is_external, before_ref\nimport refscan as _RS  # patch_pl\n",
         "import refscan as _RS  # patch_pl"),
        ("a placeholder is the whole provision (pl)",
         '''    head = " ".join(l.lstrip("# ") for l in lines if l.startswith("#"))
''',
         r'''    head = " ".join(l.lstrip("# ") for l in lines if l.startswith("#"))
    if _RS._LANG["v"] == "pl":  # patch_pl: "# Art. 4. (uchylony)" is a placeholder; an article with a repealed point
        # ("1. Ustawa określa:" then "- 1) (uchylony)") or paragraph is not
        rest = " ".join(l for l in lines if not l.startswith("#"))
        if rest:
            return bool(re.fullmatch(r"(?i)\W*(?:uchylon[aey]|skreślon[aey])\W*", rest))
        return bool(re.search(r"(?i)\((?:uchylon|skreślon)\w*\)\W*$", head))
''', "# patch_pl: \"# Art. 4. (uchylony)\" is a placeholder"),
        ("pl_in_range",
         "def is_placeholder(text: str) -> bool:",
         r'''def pl_in_range(k: str, ctx: str) -> bool:
    """patch_pl: k lies strictly inside a span of the context ("art. 759-774", "§ 23-34")"""
    km = re.match(r"(\d+)$", k)
    return bool(km) and any(int(r.group(1)) < int(km.group(1)) < int(r.group(2))
                            for r in re.finditer(r"(?<![\d.])(\d{1,4})[a-z]?\s*[-–]\s*(\d{1,4})(?![\d])", ctx))


def is_placeholder(text: str) -> bool:''', "def pl_in_range("),
        ("a span is not a reference to each article in it (pl)",
         '''                continue  # NZ_EN_SKIP
''',
         '''                continue  # NZ_EN_SKIP
            if (c.get("language") or "").lower() == "pl" and pl_in_range(k, ctx):
                continue  # patch_pl: "art. 759-774" names a span, not article 772 on its own
''', "# patch_pl: \"art. 759-774\" names a span"),
    ],
    os.path.join(S, "detectors", "text_detectors.py"): [
        ("Polish deadlines marked as deadlines (pl)",
         "jo më vonë|chậm nhất|trước ngày)') as deadline,",
         "jo më vonë|chậm nhất|trước ngày|najpóźniej|nie później niż)') as deadline,",
         "najpóźniej|nie później niż)') as deadline,"),
        ("Polish deadlines in the lapsed-limit score (pl)",
         "jo më vonë|chậm nhất|trước ngày|report|",
         "jo më vonë|chậm nhất|trước ngày|najpóźniej|nie później niż|report|",
         "najpóźniej|nie później niż|report|"),
    ],
    os.path.join(S, "detectors", "dup_labels.py"): [
        ("superscript paragraphs (pl)",
         'NB_INSTRUCTION = re.compile(',
         r'''# patch_pl: a Polish paragraph inserted later carries a superscript ("§ 2¹" after "§ 2"): another label
LAB_PL = re.compile(LAB.pattern.replace(r"(§+\s*\d+[º°o]?", r"(§+\s*\d+[⁰¹²³⁴⁵⁶⁷⁸⁹ᵃ-ᶻ]*[º°o]?", 1), re.I)
NB_INSTRUCTION = re.compile(''', "LAB_PL = re.compile("),
        ("use LAB_PL (pl)",
         "            m = (LAB_NB if nb else LAB).match(line)\n",
         "            m = (LAB_NB if nb else LAB_PL if (c.get(\"language\") or \"\").lower() == \"pl\" else LAB).match(line)  # patch_pl\n",
         "else LAB_PL if"),
    ],
    os.path.join(S, "detectors", "currency_scan.py"): [
        ("złotych starych", "lei vechi|zlotych starych|",
         "lei vechi|zlotych starych|z(?:ł|l)otych starych|starych z(?:ł|l)otych|", "starych z(?:ł|l)otych|"),
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
