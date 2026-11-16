"""Dutch blind spots, in a copy of global-law's vulnerabilities/scripts (idempotent; found by the Netherlands run):
- ingest/textscan.py: a date written with hyphens was read as month-day-year ("12-01-2020" as 1 December), the US order.
  Dutch writes day-month-year ("t/m 31-12-2025", "tot 1-1-2026"), so a day above 12 was dropped and the rest were read
  with day and month swapped (328 such time limits in netherlands-law, nearly all in ministerial regulations). For a
  Dutch-language corpus (pins.json language "nl") the two are now swapped back. And "tot" after "terug" is retroactive
  effect, not a time limit ("Artikel I werkt terug tot en met 1 januari 2013", "met terugwerkende kracht tot 1 januari
  2011"): for "nl" such a date is no longer read as a lapsed "until".
- detectors/currency_scan.py: the Dutch guilder, replaced by the euro on 1 January 2002, was not read at all. Dutch texts
  write it "100 gulden", "ƒ 1.000", "f 26,50" (a plain "f" and a space before the amount), "fl. 200,-", "Hfl. 500" or
  "NLG 50.000". These are added for the Netherlands only (pins.json code NL). The guilders and florins of the Caribbean
  parts of the Kingdom are left out: "(Nederlands-)Antilliaanse gulden", "Caribische gulden", "Arubaanse florin",
  "NAf." and "Afl." (the letters before "f"/"fl." keep these from matching), and the Surinamese guilder; so are "f"
  without a space ("f1", a factor in formulas or an item "f1."), "f" inside a word or an identifier, and "f 2°" (an item).
  In Dutch "kroon" is a crown (a dental crown, the crown on a decoration), not the Estonian kroon: left out for "nl".
- ingest/refscan.py (used by the reference, placeholder and dead-fine detectors): Dutch names another act after the
  reference ("artikel 15, eerste lid, van de Wet minimumloon", "artikel 9 van de wet" in an order in council, "artikel 12
  van Verordening (EU) 2023/2405"), which was read as a reference to the citing act's own article; and "artikel 3.3" or
  "artikel 7:670" (chapter or book, then article) was read as article 3 or 7. For "nl" the first is now another act, and
  the second is left out (the file names, art-03-003.md, give no key to match it to). A second round, after the hand
  check: "2.134" was read as the number 2134 (the Brazilian thousands form), a list of numbers and subunits longer than
  the 70 characters read after a reference ("de artikelen 43, tweede lid, 53, tweede lid, tweede volzin en 55b, tweede
  lid, van de Woningwet") hid the act named at its end, and "van de kaderrichtlijn afvalstoffen" names an EU directive.
- detectors/placeholder_ref.py: an article whose text withdraws another act or sets the act's own end ("De Wet
  personenvervoer wordt ingetrokken.", "Deze regeling vervalt met ingang van 1 augustus 2027.") was read as a provision
  that now reads only "vervallen", as the English, French, Spanish, Portuguese and German forms already were not.
  A fourth round, after reading a sample: Dutch uses "vervalt" (lapses) and "vervallen" in ordinary text ("Het
  auteursrecht vervalt door verloop van 70 jaren", art. 37 Auteurswet), and such an article of 400 characters or less was
  read as a placeholder. A placeholder is now the word alone ("[Vervallen]", "Vervallen.", "[Vervallen door
  vernummering.]"); "(Vervallen per 1-1-2005)" was already one.
- detectors/currency_scan.py, third round (after the hand check): two ministerial regulations for Curaçao and Sint
  Maarten (tariffs under the Schepenwet and for fishing vessels, 2010) write their amounts "f 305,-", which there is the
  Antillean guilder, not the Dutch one (99 flags). For NL, a guilder form in an act whose README title names Curaçao, Sint
  Maarten, Aruba, the Antilles, the Caribbean Netherlands, Bonaire, Sint Eustatius or Saba is left out.

    python -X utf8 patch_nl.py <scripts dir>
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


patch("ingest/textscan.py", [
    ("Dutch day-month-year with hyphens (nl)",
     '                y, mo, d = int(g["y5"]), int(g["m5"]), int(g["d5"])\n',
     '                y, mo, d = int(g["y5"]), int(g["m5"]), int(g["d5"])\n'
     '                if _LANG["v"] == "nl":  # patch_nl: Dutch writes day-month-year ("t/m 31-12-2025")\n'
     '                    mo, d = d, mo\n',
     "# patch_nl: Dutch writes day-month-year"),
    ("Dutch: retroactive effect is not a time limit (nl)",
     '        if _LANG["v"] == "pt" and re.match(r"(?i)do\\b", m.group(0)):\n',
     '        if _LANG["v"] == "nl" and re.search(r"(?i)\\bterug(?:werkende\\s+kracht)?\\s*$", text[max(0, m.start() - 40):m.start()]):\n'
     '            continue  # patch_nl: "werkt terug tot en met 1 januari 2013", "terugwerkende kracht tot": back to a date, not until it\n'
     '        if _LANG["v"] == "pt" and re.match(r"(?i)do\\b", m.group(0)):\n',
     "# patch_nl: \"werkt terug tot en met"),
])
patch("ingest/refscan.py", [
    ("Dutch: another act named after the reference (nl)",
     '    if _LANG["v"] == "ru" and EXT_AFTER_RU.match(tail):\n        return True\n',
     '    if _LANG["v"] == "ru" and EXT_AFTER_RU.match(tail):\n        return True\n'
     '    if _LANG["v"] == "nl" and EXT_AFTER_NL.match(tail):  # patch_nl: "artikel 15, eerste lid, van de Wet minimumloon"\n'
     '        return True\n',
     'and EXT_AFTER_NL.match(tail):  # patch_nl'),
    ("Dutch: the pattern for another act named after the reference (nl)",
     'def is_external_de(tail: str) -> bool:\n',
     '# patch_nl: Dutch names another act after the reference and its subunits: "artikel 15, eerste lid, van de Wet minimumloon",\n'
     '# "artikel 9, onderdeel a, van de Handelsregisterwet 2007", "de artikelen 14 en 22 van het Wetboek van Strafrecht BES",\n'
     '# "artikel 9 van de wet" (in an order in council: its parent act), "artikel 12 van Verordening (EU) 2023/2405",\n'
     '# "artikel 5 van die wet"; "van deze wet", "van dit besluit" and "van toepassing" are not another act\n'
     'NL_TOK = r"(?:\\w+(?:de|ste)|lid|leden|onder(?:deel|delen)?|aanhef|sub|punt|en|of|tot|met|juncto|[a-z]|\\d+[°º]?\\.?|[a-z]°|[IVX]+)"\n'
     'EXT_AFTER_NL = re.compile(rf"^(?:[\\s,]+{NL_TOK}(?!\\w))*[\\s,]+van\\s+(?:(?:de|het)\\s+)?(?:[A-Z]|wet\\b|(?:eerst|laatst)?genoemde\\b|bedoelde\\b|"\n'
     '                          r"(?:die|dat)\\s+(?:wet|besluit|regeling|verordening|richtlijn|verdrag|wetboek)\\b|"\n'
     '                          r"(?:richtlijn|verordening|beschikking|kaderbesluit|besluit)\\s*(?:\\(|nr|no|\\d))")\n\n\n'
     'def is_external_de(tail: str) -> bool:\n',
     'EXT_AFTER_NL = re.compile('),
    ("Dutch: chapter-numbered articles (nl)",
     '            tail = body[m.end():m.end() + 70]\n',
     '            tail = body[m.end():m.end() + 70]\n'
     '            if _LANG["v"] == "nl" and re.match(r"[.:]\\d", tail):\n'
     '                continue  # patch_nl: "artikel 3.3", "artikel 7:670" (chapter or book and article), not article 3 or 7\n',
     '# patch_nl: "artikel 3.3"'),
    # second round (after the hand check): longer lists of subunits and numbers, and EU directives in lower case
    ("Dutch: subunit words (nl, round 2)",
     '|en|of|tot|met|juncto|[a-z]|\\d+[°º]?\\.?|[a-z]°|[IVX]+)"\n',
     '|en|of|tot|met|juncto|volzin|volzinnen|zin|slot|[a-z]|\\d+[a-z]{0,2}[°º]?\\.?|[a-z]°|[IVX]+)"  # patch_nl2\n',
     '# patch_nl2'),
    ("Dutch: EU directives and regulations in lower case (nl, round 2)",
     '                          r"(?:richtlijn|verordening|beschikking|kaderbesluit|besluit)\\s*(?:\\(|nr|no|\\d))")\n',
     '                          r"(?:richtlijn|verordening|beschikking|kaderbesluit|besluit)\\s*(?:\\(|nr|no|\\d)|"\n'
     '                          r"(?:[\\w-]*richtlijn|(?:EU|EG|EEG)-verordening)\\b)")  # patch_nl2: "van de kaderrichtlijn afvalstoffen"\n',
     '# patch_nl2: "van de kaderrichtlijn'),
    ("Dutch: chapter-numbered articles read as thousands, and a long list before the act (nl, round 2)",
     '            if _LANG["v"] == "nl" and re.match(r"[.:]\\d", tail):\n',
     '            if _LANG["v"] == "nl" and (re.match(r"[.:]\\d", tail) or re.search(r"\\d[.:]\\d", m.group(0))\n'
     '                                       or EXT_AFTER_NL.match(body[m.end():m.end() + 400])):  # patch_nl2: "2.134", a list\n',
     '# patch_nl2: "2.134", a list'),
])
patch("detectors/placeholder_ref.py", [
    ("Dutch: an article that withdraws another act is not a placeholder (nl)",
     'werden aufgehoben",\n',
     'werden aufgehoben|(?:wordt|worden)\\s+(?:hierbij\\s+)?ingetrokken|\\bvervalt\\s+(?:met ingang van|op|per|na)\\s",  # patch_nl\n',
     'ingetrokken|\\bvervalt\\s+(?:met ingang van|op|per|na)\\s"'),
])
patch("detectors/placeholder_ref.py", [
    # fourth round (after reading a sample): Dutch writes "vervalt" (lapses) and "vervallen" in ordinary text ("Het
    # auteursrecht vervalt door verloop van 70 jaren", art. 37 Auteurswet; "Verval van recht op pensioen"); a repealed
    # article reads only "[Vervallen]", "Vervallen.", "(Vervallen per 1-1-2005)" or "[Vervallen door vernummering.]"
    ("Dutch: a placeholder is the word alone, not a provision that uses it (nl, round 4)",
     '    m = GONE.search(substantive)  # not substantive[:70]: the cut can fall inside a word\n',
     '    m = GONE.search(substantive)  # not substantive[:70]: the cut can fall inside a word\n'
     '    if m and m.group(0).lower() in ("vervallen", "vervalt", "ingetrokken") and not re.fullmatch(\n'
     '            r"(?i)\\W*(?:vervallen|ingetrokken)\\b[^.\\])]{0,40}[.\\])]*\\W*", substantive):  # patch_nl4\n'
     '        return False\n',
     '# patch_nl4'),
])
patch("detectors/currency_scan.py", [
    ("Dutch guilder (NL)", 'EXTRA_CURRENCY_CODE = {',
     'EXTRA_CURRENCY_CODE = {"NL": r"|(?<!antilliaanse )(?<!caribische )(?<!surinaamse )(?<!arubaanse )guldens?\\b'
     r'|(?<![\w.\-/])(?:(?-i:ƒ|fl\.|NLG)|(?-i:[Hh]fl)\.?)(?=\s?[0-9])|(?<![\w.\-/])(?-i:f)(?=\s[0-9])(?!\s[0-9]+\s?[°º])", ',
     '"NL": r"|(?<!antilliaanse )'),
    ("Dutch kroon = crown (nl)", 'NOT_CURRENCY = {', 'NOT_CURRENCY = {"nl": (r"kroon|",), ', '"nl": (r"kroon|",)'),  # any first entry (patch_az puts "az" first)
    # third round (after the hand check): a regulation for Curaçao and Sint Maarten (or Aruba, the former Netherlands
    # Antilles, the Caribbean Netherlands) writes its Antillean guilders or Aruban florins as "f 305,-", the same sign as the
    # Dutch guilder; its title names the island, so an NL act whose README title names one is left out of the guilder forms
    ("Caribbean guilders in an act for the islands (NL, round 3)",
     '        out.append({"corpus": c["path"], "repo": c["repo"], "path": path, "line": int(ln), "text": text[:700]})\n    return out\n',
     '        out.append({"corpus": c["path"], "repo": c["repo"], "path": path, "line": int(ln), "text": text[:700]})\n'
     '    if (c.get("code") or "").upper() == "NL":  # patch_nl3: "f 305,-" in an act for Curaçao and Sint Maarten is the Antillean guilder\n'
     '        import re as _re3\n'
     '        isl = _re3.compile(r"(?i)cura[cç]a|sint maarten|aruba|antill|caribisch|bonaire|eustatius|\\bsaba\\b|\\bBES\\b")\n'
     '        nl_g = _re3.compile(r"(?i)(?<!antilliaanse )(?<!caribische )(?<!surinaamse )(?<!arubaanse )guldens?\\b|(?<![\\w.\\-/])(?:(?-i:\\u0192|fl\\.|NLG)|(?-i:[Hh]fl)\\.?)(?=\\s?[0-9])|(?<![\\w.\\-/])(?-i:f)(?=\\s[0-9])")\n'
     '        other = _re3.compile(pat_for({k: v for k, v in c.items() if k != "code"}), _re3.I)\n'
     '        titles = {}\n'
     '        def _title(folder):\n'
     '            if folder not in titles:\n'
     '                r = subprocess.run(["git", "-C", str(repo), "show", f"{c[\'sha\']}:{folder}/README.md"], capture_output=True, creationflags=FLAGS)\n'
     '                titles[folder] = (r.stdout.decode("utf-8", "replace").splitlines() or [""])[0]\n'
     '            return titles[folder]\n'
     '        out = [o for o in out if not (isl.search(_title(o["path"].rsplit("/", 1)[0])) and nl_g.search(o["text"]) and not other.search(o["text"]))]\n'
     '    return out\n',
     '# patch_nl3: "f 305,-" in an act for'),
])
