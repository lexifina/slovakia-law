"""Slovak fixes for the copy of global-law's vulnerabilities/scripts (each pair has a marker, so it stays in place if a later
patch edits the same text):
 1. ingest/textscan.py: "do konca roka 2012" / "do konca roku 2012" (until the end of the year) is 31 December of that
    year, as the Czech "do konce roku" already was;
 2. ingest/textscan.py: in a Slovak ("sk") corpus, amounts in the Slovak koruna ("5 000 Sk", "100 000 slovenských korún")
    and the Czechoslovak koruna ("2 000 Kčs") are amounts (units "sk" and "kčs"), so a law that changed one of them
    can leave the old figure standing elsewhere (stale_amount); "Sk" and "Kčs" only with that capitalisation;
 3. detectors/currency_scan.py: for Slovakia (pins.json code SK) the Slovak koruna, replaced by the euro,
    and the Czechoslovak koruna are dead currencies: "5 000 Sk", "2 000 Kčs",
    "100 000 slovenských korún", "500 korún"; written byte-safe (git grep -P may not read the pattern as UTF-8);
 4. detectors/ref_detectors.py: a Slovak amending sentence ("V § 4 tretia veta znie", "sa vkladá", "sa nahrádza",
    "sa vypúšťa", "sa dopĺňa", "strácajú účinnosť") quotes another act's provisions, as the Czech ones already in the
    list do; a reference followed by another act's name in Slovak ("Občianskeho zákonníka", "nariadenia vlády",
    "Trestného poriadku", "Ústavy", "dohovoru", "smernice") is to that act; "tohto zákona" (this act) stays this act's;
 5. detectors/placeholder_ref.py: in a Slovak ("sk") corpus a placeholder is a provision whose body reads only
    "Zrušený.", "(zrušené včítane nadpisov)", "– zrušený", "vypustený" and the like (or, with no body, a heading ending
    in it), not any provision with "zrušen-" in its first 70 characters ("Rozhodnutie o zrušení akreditácie",
    "okamžitým zrušením"), and not one whose list items ("- a) ...") the general rule skips as notes;
 6. ingest/refscan.py: in a Slovak ("sk") corpus a reference followed by another act's name, after any list of units
    ("§ 7 ods. 1 zákona č. 1/1991 Zb.", "§ 93, 94 Tr. zák.", "§ 49 a 50 správního řádu", "§ 270a Zákonníka práce",
    "§ 3, 16, 19, 20 a 21 vládneho nariadenia"), is to that act, read up to 300 characters on as patch_pl does;
    "tohto zákona" (this act) stays this act's.

    python -X utf8 patch_sk.py <scripts dir>
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


SK_AMT = (
    '# patch_sk: the Slovak koruna ("5 000 Sk", "100 000 slovenských korún", "500 korún") and the Czechoslovak koruna\n'
    '# ("2 000 Kčs"), read only in a corpus whose language is "sk"; "Sk" and "Kčs" only with that capitalisation\n'
    'SK_AMT = re.compile(rf"(?<![\\d.,])(?P<skn>{NUM})\\s?(?:(?P<skc>Kčs)|Sk|(?i:(?:slovensk\\w+\\s+)?kor[uú]n(?:a|y|e|u|ou|ám|ách|ami)?))(?!\\w)")\n'
    '\n\n'
    'def norm_num(s: str) -> str:'
)
SK_USE = (
    '    if _LANG["v"] == "sk":  # patch_sk: Slovak and Czechoslovak koruna\n'
    '        for m in SK_AMT.finditer(text):\n'
    '            v = norm_num(m.group("skn"))\n'
    '            if v != "0" and len(v.split(".")[0]) >= 2 and not (len(v) == 4 and v.startswith(("19", "20"))):\n'
    '                out.add((v, "kčs" if m.group("skc") else "sk"))\n'
    '    if _LANG["v"] == "ar":  # patch_ar: rials and baisas (a year never comes before the currency)'
)

patch("ingest/textscan.py", [
    ("do konca roka", r'konce\s+roku\s+|', r'konce\s+roku\s+|konca\s+(?:roka|roku)\s+|', r'konca\s+(?:roka|roku)'),
    ("SK_AMT", "\n\ndef norm_num(s: str) -> str:", "\n" + SK_AMT, "SK_AMT = re.compile("),
    ("SK_AMT use", '    if _LANG["v"] == "ar":  # patch_ar: rials and baisas (a year never comes before the currency)', SK_USE,
     "# patch_sk: Slovak and Czechoslovak koruna"),
])

patch("detectors/currency_scan.py", [
    ("Slovak koruna (SK)", 'EXTRA_CURRENCY_CODE = {',
     'EXTRA_CURRENCY_CODE = {"SK": r"|(?-i:(?<![A-Za-z])Sk)\\b|(?-i:Kčs)|(?:slovensk\\S*\\s+|československ\\S*\\s+)?kor(?:u|ú)n(?#SK_KORUNA)", ',
     "(?#SK_KORUNA)"),
])

SK_PH = (
    '    if _RS._LANG["v"] == "sk":  # patch_sk: "Zrušený.", "(zrušené včítane nadpisov)" as the whole body\n'
    '        rest = " ".join(l for l in lines if not l.startswith("#"))\n'
    '        if rest:\n'
    '            return bool(SK_GONE.fullmatch(rest))\n'
    '        return bool(re.search(r"(?i)\\b(?:zrušen(?:ý|á|é|o|a|i)?|vypusten(?:ý|á|é))\\W*$", head))\n'
    '    body = [l for l in lines if not l.startswith("#")]\n'
    '    labels = '
)
SK_GONE = (
    '# patch_sk: a Slovak placeholder body ("Zrušený.", "– zrušený", "(zrušené včítane nadpisov)", "zrušený od 1. 1. 2005")\n'
    'SK_GONE = re.compile(r"(?i)\\W*(?:zrušen(?:ý|á|é|o|a|i)?|vypusten(?:ý|á|é))\\b(?:\\s+(?:včítane|vrátane)\\s+nadpis\\w*)?"\n'
    '                     r"(?:\\s+(?:od|dňom|s\\s+účinnosťou\\s+od)\\s+[\\d.\\s]+(?:[a-zá-ž]+\\s+\\d{4})?)?\\W*")\n'
    '\n\n'
    'def is_placeholder(text: str) -> bool:'
)

patch("detectors/placeholder_ref.py", [
    ("SK_GONE", "\n\ndef is_placeholder(text: str) -> bool:", "\n" + SK_GONE, "SK_GONE = re.compile("),
    ("Slovak placeholder", '    body = [l for l in lines if not l.startswith("#")]\n    labels = ', SK_PH, '# patch_sk: "Zrušený.", "(zrušené'),
])

EXT_SK = (
    '# patch_sk: Slovak (and Czech, in the Czechoslovak acts) references to another act, named after the reference and any\n'
    '# list that follows it: "§ 7 ods. 1 zákona č. 1/1991 Zb.", "§ 93, 94 Tr. zák.", "§ 49 a 50 správního řádu",\n'
    '# "§ 270a Zákonníka práce", "§ 3, 16, 19, 20 a 21 vládneho nariadenia č. 17/1954 Zb."; never "tohto zákona" (this act)\n'
    'EXT_AFTER_SK = re.compile(r"(?i)^(?:(?:\\s*,)?\\s*(?:(?:a|alebo|až|aj|i|nebo|-|–)\\s+)?"\n'
    '                          r"(?:§§?\\s*\\d{1,4}[a-z]{0,2}(?!\\w)|(?:ods|odst|odsek|odseku|odseky|písm|bod|bodu|body|čl|bodov)\\.?\\s*\\w{1,4}\\)?(?!\\w)|"\n'
    '                          r"\\d{1,4}[a-z]{0,2}\\)?(?!\\w)|(?:prv|druh|tret|štvrt|piat|posledn)\\w*\\s+(?:vet|bod|čas)\\w*))*"\n'
    '                          r"\\s*,?\\s*(?:(?!tohto\\b|tejto\\b|tohoto\\b|této\\b|toho\\b|na\\b|v\\b|vo\\b|a\\b|sa\\b|podľa\\b)[^\\W\\d]+\\s+)?"\n'
    '                          r"(?:zákon\\w*|zák\\.|vyhlášk\\w*|vyhl\\.|nariaden\\w*|nařízení|ústavn\\w*|(?-i:Ústav[ayeou])|dohovor\\w*|zmluv\\w*|smernic\\w*|"\n'
    '                          r"poriad\\w*|řádu|zákonník\\w*|zákoník\\w*|výnos\\w*|dekrét\\w*|dekret\\w*|protokol\\w*|štatút\\w*|Tr\\.\\s?(?:zák|por|ř)|"\n'
    '                          r"Obč\\.\\s?zák|Obch\\.\\s?zák|O\\.\\s?s\\.\\s?[př])(?!\\w)")\n'
    'THAI_DIGITS = str.maketrans('
)

patch("ingest/refscan.py", [
    ("EXT_AFTER_SK", "THAI_DIGITS = str.maketrans(", EXT_SK, "EXT_AFTER_SK = re.compile("),
    ("EXT_AFTER_SK use", '    if _LANG["v"] == "pl" and EXT_AFTER_PL.match(tail):  # patch_pl\n        return True\n',
     '    if _LANG["v"] == "pl" and EXT_AFTER_PL.match(tail):  # patch_pl\n        return True\n'
     '    if _LANG["v"] == "sk" and EXT_AFTER_SK.match(tail):  # patch_sk\n        return True\n', "EXT_AFTER_SK.match(tail):  # patch_sk"),
    ("Slovak long list", 'if _LANG["v"] == "pl" else tail):  # patch_pl: a long list',
     'if _LANG["v"] in ("pl", "sk") else tail):  # patch_pl: a long list (patch_sk too)', 'in ("pl", "sk") else tail'),
])

patch("detectors/ref_detectors.py", [
    ("Slovak amending sentences", "se vkládají|se nahrazuj|", "se vkládají|se nahrazuj|sa vklad|sa nahrádza|sa vypúšťa|sa dopĺňa|sa mení|sa pripája|znie:|znejú:|strácajú účinnosť|stráca účinnosť|",
     "sa vypúšťa|"),
    ("Slovak other acts", "zákona|vyhlášky|nařízení|", "zákona|vyhlášky|nařízení|zákonníka|nariadenia|poriadku|ústavy|dohovoru|smernice|", "zákonníka|nariadenia|poriadku|"),
    ("Slovak this act", "|presente|bu kanun|", "|presente|tohto|tejto|bu kanun|", "|tohto|tejto|"),
])
