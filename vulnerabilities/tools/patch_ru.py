r"""Russian (as written in Kyrgyz law) blind spots, in a copy of global-law's vulnerabilities/scripts (idempotent):
- ingest/textscan.py: the deadline "не позднее 1 июля 2022 года" (= not later than) was not read as a time limit
  ("до ..." and "по ... включительно" and the genitive months "января ... декабря" already were);
- ingest/refscan.py: article files named statya-NNN.md (and statya-NNN-N.md for an inserted article) had no key, so
  placeholder_ref and dead_fine saw no provision at all; "статья 131-1" (an article inserted after 131) was read as article
  131; the other cases of "статья" ("статье", "статьей", "статьями", "статей" ...) were not read as references; and
  "статьи 5 Закона ...", "статьей 12 Налогового кодекса" (another act named after the number) were read as references to
  the act's own articles ("настоящего Закона/Кодекса" stays the act's own);
- detectors/placeholder_ref.py: "исключ[её]н\w*" (excluded, a repeal marker) also matched "за исключением" (= except)
  and "исключения" (exclusion): six of seven first flags were articles that merely say "except"; now only
  "исключен", "исключена", "исключено", "исключены" (and with ё).

    python -X utf8 patch_ru.py <scripts dir>
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
    ("UNTIL: не позднее", r'|не по-късно от|изтича на|', r'|не по-късно от|не позднее|изтича на|'),
])
patch("ingest/refscan.py", [
    ("UNIT: Russian cases", r"|статья|статьи|", r"|статья|статьи|стать[еёю]й?|статьями|статьям|статьях|статей|", "стать[еёю]й?|"),
    ("path_key: statya-NNN", r"|clanek|clanak|clan|neni)?", r"|clanek|clanak|clan|neni|statya)?", "|neni|statya)?"),
    ("path_key: statya-NNN-N",
     '    if SERIES_PATH.search("/" + base):\n        return None\n    m = re.match(',
     '    if SERIES_PATH.search("/" + base):\n        return None\n'
     '    r = re.match(r"^statya-0*(\\d{1,4})-(\\d{1,3})$", base)  # an inserted article (statya-131-1.md: article 131-1)\n'
     '    if r:\n        return f"{int(r.group(1))}-{r.group(2)}"\n    m = re.match(',
     "an inserted article (statya-131-1.md"),
    ("heading_key: Статья 131-1",
     "    return _mkey(m) if m.re is HEAD else key(m.group(1), m.group(2))\n",
     "    if m.re is HEAD and _LANG[\"v\"] == \"ru\":  # \"Статья 131-1.\": article 131-1, inserted after 131\n"
     "        r = re.match(r\"-(\\d{1,3})(?!\\d)\", m.string[m.end():])\n"
     "        if r and not m.group(2) and not m.group(3):\n"
     "            return f\"{_mkey(m)}-{r.group(1)}\"\n"
     "    return _mkey(m) if m.re is HEAD else key(m.group(1), m.group(2))\n",
     "\"Статья 131-1.\": article 131-1"),
    ("refs: статьи 131-1",
     "                if sub:  # Belgian numbering",
     "                if sub is None and _LANG[\"v\"] == \"ru\" and not m.group(2) and not m.group(3):  # \"статьи 131-1\": article 131-1;\n"
     "                    sub = re.match(r\"-(\\d{1,3})(?!\\d)(?![.,]\\d)\", body[m.end():m.end() + 7])  # \"статьями 56-59\" stays a range\n"
     "                    if sub and int(sub.group(1)) > int(m.group(1)):\n"
     "                        sub = None\n"
     "                if sub:  # Belgian numbering",
     "\"статьи 131-1\": article 131-1"),
    # anchored on patch_de.py's early return (the shared return line is edited by patch_pt.py and others)
    ("is_external: another act named after the number (ru)",
     "    if is_external_de(tail):\n        return True\n",
     "    if is_external_de(tail):\n        return True\n"
     "    if _LANG[\"v\"] == \"ru\" and EXT_AFTER_RU.match(tail):\n        return True\n",
     "_LANG[\"v\"] == \"ru\" and EXT_AFTER_RU.match(tail)"),
    ("EXT_AFTER_RU", "\n\ndef is_external_de(tail: str) -> bool:\n",
     "\n\n# Russian: \"статьи 5 Закона ...\", \"статьей 12 Налогового кодекса\" name another act; \"настоящего Закона\" is this one\n"
     "EXT_AFTER_RU = re.compile(r\"(?i)^[\\s,]*(?:(?!настоящ|данн|этого|этой)[а-яё\\-]+\\s+){0,3}(?:закон\\w*|кодекс\\w*|конституци\\w*|\"\n"
     "                          r\"указ\\w*|постановлени\\w*|положени\\w*|конвенци\\w*|соглашени\\w*|договор\\w*|регламент\\w*|устав\\w*|\"\n"
     "                          r\"правил\\b|правила\\b|протокол\\w*|декрет\\w*)\\b\")\n\n\ndef is_external_de(tail: str) -> bool:\n",
     "EXT_AFTER_RU = re.compile("),
])
patch("detectors/placeholder_ref.py", [
    ("GONE: исключен, not за исключением", r"|исключ[её]н\w*|", r"|исключ[её]н[аоы]?\b|", r"|исключ[её]н[аоы]?"),
])
