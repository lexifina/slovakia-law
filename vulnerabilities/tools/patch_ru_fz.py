r"""Russian federal law (russia-law) blind spots, in a copy of global-law's vulnerabilities/scripts (idempotent; run after
patch_ru.py):
- ingest/refscan.py: an inserted article is written "статья 12<sup>1</sup>" (the portal's superscript) or "статья 12.1";
  both were read as article 12, so a reference to the live article 12.1 counted as one to a repealed article 12, and
  "статьей 19.5 Кодекса ... об административных правонарушениях" escaped the "another act named after the number" test
  (the ".5" stood between the number and the act's name). Both forms, and "9¹", are now article 12.1 / 19.5 / 9.1; a
  heading at the start of a line ("Статья 12.1. ...") is not a reference; the five acts of 1994-1999 kept in one file per
  article (9-1.md, for "Статья 9¹") have keys.
- detectors/placeholder_ref.py: the acts kept as one file (fz/<year>/<number>/text.md, 1,752 of them) were never split
  into articles, so a reference to "Статья 6. (Статья утратила силу - ...)" in the same act could not be seen; for Russian,
  such a file is now read article by article ("Статья N." headings at the start of a line). An article titled "О признании
  утратившими силу ..." (it repeals other acts) is not itself a repeal placeholder. An amending article ("Внести в
  Федеральный закон ... следующие изменения: 1) в статье 5 ...", "изложить в следующей редакции", "следующего содержания")
  cites the amended act's articles, and "настоящего Федерального закона" in the wording it sets out is that act too, so
  its references are not read as the amending act's own.
- detectors/dup_labels.py: "§ 4<sup>1</sup>" (a paragraph inserted after § 4) was read as a second "§ 4".

    python -X utf8 patch_ru_fz.py <scripts dir>
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


patch("ingest/refscan.py", [
    ("RU_SUP: normalise 12<sup>1</sup> and 9¹ to 12.1",
     '    if _LANG["v"] == "de":  # "§§ 70 bis 75" is a range, not § 70bis\n',
     '    if _LANG["v"] == "ru":  # RU_SUP: "статья 12<sup>1</sup>", "статья 9¹" are article 12.1 and 9.1, as "статья 12.1" is\n'
     '        body = re.sub(r"(?<=\\d)<sup>(\\d{1,3})</sup>", r".\\1", body)\n'
     '        body = re.sub(r"(?<=\\d)([¹²³⁴⁵⁶⁷⁸⁹])", lambda x: "." + str("¹²³⁴⁵⁶⁷⁸⁹".index(x.group(1)) + 1), body)\n'
     '    if _LANG["v"] == "de":  # "§§ 70 bis 75" is a range, not § 70bis\n',
     "# RU_SUP:"),
    ("RU_DOT: статьи 12.1 is article 12.1",
     '                if sub is None and _LANG["v"] == "ru" and not m.group(2) and not m.group(3):  # "статьи 131-1": article 131-1;\n',
     '                _ru_dot = False\n'
     '                if sub is None and _LANG["v"] == "ru" and not m.group(2) and not m.group(3):  # RU_DOT: "статьи 12.1": article 12.1\n'
     '                    sub = re.match(r"\\.(\\d{1,3})(?!\\d|[.,]\\d)", body[m.end():m.end() + 8])\n'
     '                    if sub and not before.strip(" -*#>\\t\\"«") and re.match(r"\\s*(?:\\.\\s|\\.$|\\.?\\s*[-–—:(])", body[m.end() + sub.end():m.end() + sub.end() + 4] or "."):\n'
     '                        seen_spans.append((m.start(), m.end() + sub.end()))\n'
     '                        continue  # the heading "Статья 12.1. ..." at the start of a line, not a reference\n'
     '                    if sub and EXT_AFTER_RU.match(body[m.end() + sub.end():m.end() + sub.end() + 70]):\n'
     '                        seen_spans.append((m.start(), m.end() + sub.end()))\n'
     '                        continue  # "статьей 19.5 Кодекса ... об административных правонарушениях": another act\n'
     '                    _ru_dot = bool(sub)\n'
     '                if sub is None and _LANG["v"] == "ru" and not m.group(2) and not m.group(3):  # "статьи 131-1": article 131-1;\n',
     "# RU_DOT:"),
    ("RU_DOT: key with a dot",
     '                    first, ks, end = f"{first}-{sub.group(1)}", [f"{first}-{sub.group(1)}"], m.end() + sub.end()\n',
     '                    _sep = "." if _ru_dot else "-"  # RU_DOT_KEY\n'
     '                    first, ks, end = f"{first}{_sep}{sub.group(1)}", [f"{first}{_sep}{sub.group(1)}"], m.end() + sub.end()\n',
     "# RU_DOT_KEY"),
    ("RU_LIST_DOT: статьями 11, 19.1 and 22",
     '            keys.append(key(l.group(1), l.group(2), l.group(3))); prev, pos = int(l.group(1).replace(".", "")), l.end(); continue\n',
     '            _d = re.match(r"\\.(\\d{1,3})(?!\\d|[.,]\\d)", body[l.end():l.end() + 6]) if _LANG["v"] == "ru" and not l.group(2) and not l.group(3) else None\n'
     '            if _d:  # RU_LIST_DOT: "статьями 11, 13 - 16, 19.1, 22": 19.1 is one article, not 19\n'
     '                keys.append(f"{key(l.group(1), None)}.{_d.group(1)}"); prev, pos = int(l.group(1)), l.end() + _d.end(); continue\n'
     '            keys.append(key(l.group(1), l.group(2), l.group(3))); prev, pos = int(l.group(1).replace(".", "")), l.end(); continue\n',
     "# RU_LIST_DOT:"),
    ("RU_CLAUSE: the act named after a list",
     "            if is_external(before, ",   # patch_pl rewrites the rest of this line, so anchor on its start
     "            if _LANG[\"v\"] == \"ru\" and ru_other_act(body, m.end()):  # RU_CLAUSE\n                continue\n"
     "            if is_external(before, ",
     "# RU_CLAUSE\n"),
    ("RU_CLAUSE: helper",
     "\n\ndef is_external_de(tail: str) -> bool:\n",
     "\n\n# RU_CLAUSE_FN: Russian names the act once, after the whole list (\"статью 21, пункт 1 статьи 25 и статью 29 Федерального\n"
     "# закона от 8 мая 2010 года ...\"); the first act named after the number, within its clause, is the act cited\n"
     "RU_ACT_WORD = re.compile(r\"(?i)\\b(?:настоящ\\w+|закон(?:а|у|ом|е|ы|ов|ами|ах)?|кодекс(?:а|у|ом|е|ы|ов|ами|ах)?|конституци(?:я|и|ей|ю)|\"\n"
     "                         r\"указ(?:а|у|ом|е|ы|ов)?|постановлени(?:е|я|ю|ем|и|й)|договор(?:а|у|ом|е|ы|ов)?|соглашени(?:е|я|ю|ем|и|й)|\"\n"
     "                         r\"конвенци(?:я|и|ей|ю)|регламент(?:а|у|ом|е)?|устав(?:а|у|ом|е)?|протокол(?:а|у|ом|е)?)\\b\")\n\n\n"
     "def ru_other_act(body: str, pos: int) -> bool:\n"
     "    seg = re.split(r\"[;\\n]|\\.\\s+[А-ЯЁ]\", body[pos:pos + 400], maxsplit=1)[0]\n"
     "    a = RU_ACT_WORD.search(seg)\n"
     "    return bool(a) and not a.group(0).lower().startswith(\"настоящ\")\n"
     "\n\ndef is_external_de(tail: str) -> bool:\n",
     "# RU_CLAUSE_FN:"),
    ("RU_PATH: 9-1.md and text.md#12.1",
     '    base = path.rsplit("/", 1)[-1].rsplit(".", 1)[0]\n    if SERIES_PATH.search("/" + base):\n        return None\n',
     '    if "#" in path:  # RU_PATH: placeholder_ref\'s article of a one-file act (fz/2010/1/text.md#12.1)\n'
     '        return path.rsplit("#", 1)[1]\n'
     '    base = path.rsplit("/", 1)[-1].rsplit(".", 1)[0]\n    if SERIES_PATH.search("/" + base):\n        return None\n'
     '    if _LANG["v"] == "ru" and re.match(r"^\\d{1,4}-\\d{1,3}$", base):  # RU_PATH: 9-1.md holds "Статья 9¹" (article 9.1)\n'
     '        return base.replace("-", ".")\n',
     "# RU_PATH:"),
])
patch("detectors/placeholder_ref.py", [
    ("RU_SPLIT: helper",
     "\n\ndef is_placeholder(text: str) -> bool:\n",
     "\n\n# RU_SPLIT: russia-law keeps most acts as one file (text.md) with \"Статья N.\" headings; read it article by article\n"
     "RU_ART = re.compile(r\"(?m)^Статья\\s+(\\d{1,4})((?:<sup>\\d{1,3}</sup>|\\.\\d{1,3}(?=[.\\s(]))?)\\.?(?=[\\s(]|$)\")\n\n\n"
     "def ru_split(text: dict) -> dict:\n"
     "    out = {}\n"
     "    for path, t in text.items():\n"
     "        if path_key(path) or not path.endswith(\"/text.md\"):\n"
     "            out[path] = t\n"
     "            continue\n"
     "        hs = list(RU_ART.finditer(t))\n"
     "        parts, k, prev = {}, None, None\n"
     "        for i, h in enumerate(hs):\n"
     "            chunk = t[h.start():hs[i + 1].start() if i + 1 < len(hs) else len(t)]\n"
     "            n = int(h.group(1))\n"
     "            # the act's own articles run on in order; past repealed chapters the portal leaves out (311-FZ: 149, then 321)\n"
     "            # they may jump ahead, but not inside an amending article, which sets out another act's articles\n"
     "            if k is None or prev <= n <= prev + 5 or (n > prev and not RU_AMENDING.search(parts.get(k, \"\"))):\n"
     "                k, prev = h.group(1) + (\".\" + re.sub(r\"\\D\", \"\", h.group(2)) if h.group(2) else \"\"), n\n"
     "            # else: a heading out of sequence (\"Статья 189.61.\" set out by an amending article) continues the article\n"
     "            parts[k] = parts.get(k, \"\") + chunk  # a number met twice: the later text continues the first article\n"
     "        for k, chunk in parts.items():\n"
     "            out[f\"{path}#{k}\"] = chunk\n"
     "    return out\n\n\n"
     "def is_placeholder(text: str) -> bool:\n",
     "# RU_SPLIT: russia-law"),
    ("RU_SPLIT: call",
     "    holders = {}\n",
     "    if (c.get(\"language\") or \"\").lower() == \"ru\":  # RU_SPLIT\n"
     "        text = ru_split(text)\n"
     "    holders = {}\n",
     "        text = ru_split(text)\n"),
    ("RU_SPLIT: report the file, not the article",
     '            out.append({"corpus": c["path"], "repo": c["repo"], "path": path, "ref": k,',
     '            out.append({"corpus": c["path"], "repo": c["repo"], "path": path.split("#")[0], "ref": k,  # RU_SPLIT_PATH\n                        "from": path_key(path) if "#" in path else None,',
     "# RU_SPLIT_PATH"),
    ("RU_AMENDING: an amending article cites the amended act's articles",
     "        if a not in acts or (a, path_key(path)) in holders:\n            continue\n        for k, ctx, tail in refs(t):\n",
     "        if a not in acts or (a, path_key(path)) in holders:\n            continue\n"
     "        if \"#\" in path and RU_AMENDING.search(t):  # RU_AMENDING: \"Внести в Федеральный закон ... следующие изменения: 1) в статье 5 ...\"\n"
     "            continue  # its articles, and \"настоящего Федерального закона\" in the new wording it quotes, are the amended act's\n"
     "        for k, ctx, tail in refs(t):\n",
     "# RU_AMENDING: \"Внести"),
    ("RU_AMENDING: pattern",
     "\n\ndef ru_split(text: dict) -> dict:\n",
     "\nRU_AMENDING = re.compile(r\"(?i)внести\\s+в\\s+[^:]{0,800}?изменени|изложить\\s+(?:\\w+\\s+){0,2}в\\s+(?:следующей|новой)\\s+редакции|\"\n"
     "                         r\"следующего\\s+содержания|заменить\\s+(?:словами|словом|цифрами)|дополнить\\s+(?:словами|словом|предложением)\")  # RU_AMENDING_RX\n\n\ndef ru_split(text: dict) -> dict:\n",
     "# RU_AMENDING_RX"),
    ("RU_REPEALS_OTHERS: an article that repeals other acts is not a placeholder",
     '    if re.search(r"(?i)re-?enacted|\\brepeal of\\b|',
     '    if re.search(r"(?i)призна\\w*\\s+утративш", substantive):  # RU_REPEALS_OTHERS: "О признании утратившими силу ..."\n'
     '        return False\n'
     '    if re.search(r"(?i)re-?enacted|\\brepeal of\\b|',
     "# RU_REPEALS_OTHERS"),
])
patch("detectors/dup_labels.py", [
    ("RU_SUP_LABEL: § 4<sup>1</sup> is not § 4",
     r'(§+\s*\d+[º°o]?(?:\s?[-‑][A-Z]{1,2}\b',
     r'(§+\s*\d+[º°o]?(?:<sup>\d{1,3}</sup>)?(?:\s?[-‑][A-Z]{1,2}\b',
     r'(?:<sup>\d{1,3}</sup>)?(?:\s?[-‑]'),
])
