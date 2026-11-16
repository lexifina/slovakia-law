"""Japanese support for global-law's vulnerability detectors (found on japan-law), in a copy of vulnerabilities/scripts.

    python -X utf8 patch_ja.py <scripts dir>        (idempotent: a fix already in place is skipped)

1. Dates (ingest/textscan.py, used by lapsed_limit and late_extension): Japanese law text writes dates in era years and
   kanji numerals and puts "until" after the date, so nothing was read. Now read: 令和二年三月三十一日まで / までの間 /
   限り (the rule ends that day); 令和五年度まで / 年度末まで (a fiscal year: 31 March of the next year); 三月末日まで
   (the last day of the month); 元年 = 1; numerals with 十/百/千, positional ones (一七 = 17) and Arabic or full-width
   digits. Eras: 明治 1868, 大正 1912, 昭和 1926, 平成 1989, 令和 2019. "までに" (by) is a deadline: deadlines=False skips
   it, and detectors/text_detectors.py ranks it as one.
2. Amounts (ingest/textscan.py, used by stale_amount): yen in kanji numerals (五十万円, 三百万円, 一億円; 万/億/兆).
3. References (ingest/refscan.py, used by dangling_ref and placeholder_ref):
   - 第十六条の二 is article 16-2 (key "16-2"), not article 16; file art-016-2.md is "16-2";
   - a reference after another law's name or number (地方自治法第二条, 法第十条, 施行令第三条, 同法第五条,
     ...（昭和二十二年法律第六十七号）第二条) is to another act; 本法 stays internal;
   - 附則第三条 is a supplementary provision, not article 3.
4. Placeholders (detectors/placeholder_ref.py): "第十条　削除" (deleted, number kept) is a repeal placeholder.
5. retroactive_date (detectors/trailer_only.py): the Promulgated: trailer counts as the day a law was made.
"""
import sys
from pathlib import Path

S = Path(sys.argv[1])
done, skipped = [], []


def patch(rel, pairs):
    p = S / rel
    s = p.read_text(encoding="utf-8")
    for name, a, b, *marker in pairs:
        if b in s or (marker and marker[0] in s):  # marker: a later round rewrote what this one inserted
            skipped.append(f"{rel}: {name}")
            continue
        if s.count(a) == 0:  # superseded by a later round already applied
            skipped.append(f"{rel}: {name} (superseded)")
            continue
        if s.count(a) != 1:
            raise SystemExit(f"{rel}: {name}: anchor found {s.count(a)} times")
        s = s.replace(a, b)
        done.append(f"{rel}: {name}")
    p.write_bytes(s.encode("utf-8"))


JA = r'''# Japanese: era dates in kanji numerals, "until" after the date (令和二年三月三十一日まで, 平成三十一年三月三十一日までの間,
# 昭和六十年九月三十日限り, 令和五年度末まで, 令和五年三月末日まで); までに (by) is a deadline
JP_ERA = {"明治": 1867, "大正": 1911, "昭和": 1925, "平成": 1988, "令和": 2018}
JP_DIG = {c: i for i, c in enumerate("〇一二三四五六七八九")}
JP_DIG.update({"零": 0, **{c: i for i, c in enumerate("０１２３４５６７８９")}, **{str(i): i for i in range(10)}})
JNUM = r"[元〇零一二三四五六七八九十百千0-9０-９]{1,6}"
JP_LIMIT = re.compile(rf"(?P<era>明治|大正|昭和|平成|令和)(?P<y>{JNUM})年(?:(?P<fy>度)末?|(?P<m>{JNUM})月(?:(?P<d>{JNUM})日|(?P<me>末日?)))"
                      r"(?P<w>までに|まで|限り)")
JP_AMT = re.compile(r"(?<![〇一二三四五六七八九十百千万億兆0-9０-９])([〇一二三四五六七八九十百千万億兆0-9０-９][〇一二三四五六七八九十百千万億兆0-9０-９,，]*)円")


def jnum(s: str) -> int:
    """kanji or digit numeral: 三十一, 一七 (positional), 千二百, 五十万, 元 (= 1)."""
    s = s.replace(",", "").replace("，", "")
    if s == "元":
        return 1
    total = section = cur = 0
    for ch in s:
        if ch in JP_DIG:
            cur = cur * 10 + JP_DIG[ch]
        elif ch in "十百千":
            section += (cur or 1) * {"十": 10, "百": 100, "千": 1000}[ch]; cur = 0
        elif ch in "万億兆":
            total += ((section + cur) or 1) * {"万": 10**4, "億": 10**8, "兆": 10**12}[ch]; section = cur = 0
        else:
            raise ValueError(s)
    return total + section + cur


def jp_limits(text: str, deadlines: bool = True):
    import calendar
    for m in JP_LIMIT.finditer(text):
        if not deadlines and m.group("w") == "までに":
            continue
        try:
            y = JP_ERA[m.group("era")] + jnum(m.group("y"))
            if m.group("fy"):
                y, mo, d = y + 1, 3, 31
            else:
                mo = jnum(m.group("m"))
                d = calendar.monthrange(y, mo)[1] if m.group("me") else jnum(m.group("d"))
        except (KeyError, ValueError, calendar.IllegalMonthError):
            continue
        if 1800 <= y <= 2100 and 1 <= mo <= 12 and 1 <= d <= 31:
            s, e = max(0, m.start() - 200), min(len(text), m.end() + 100)
            yield f"{y:04d}-{mo:02d}-{d:02d}", text[s:e].replace("\n", " ")


def limits(text: str, deadlines: bool = True):
    """(iso date, context) for every 'until <date>' in the text; deadlines=False drops 'not later than <date>' deadlines."""
    if "年" in text and ("まで" in text or "限り" in text):
        yield from jp_limits(text, deadlines)
    yield from _limits(text, deadlines)


def _limits(text: str, deadlines: bool = True):'''

patch("ingest/textscan.py", [
    ("Japanese dates",
     'def limits(text: str, deadlines: bool = True):\n',
     JA + "\n"),
    ("Japanese yen amounts",
     '        out.add((v, "%" if pct else c.rstrip(".")))\n    return out\n',
     '        out.add((v, "%" if pct else c.rstrip(".")))\n'
     '    if "円" in text:  # Japanese: 五十万円, 三百万円 (kanji numerals)\n'
     '        for m in JP_AMT.finditer(text):\n'
     '            try:\n'
     '                v = str(jnum(m.group(1)))\n'
     '            except ValueError:\n'
     '                continue\n'
     '            if len(v) >= 2 and not (len(v) == 4 and v.startswith(("19", "20"))):\n'
     '                out.add((v, "円"))\n'
     '    return out\n'),
])
# JP_AMT / jnum are defined after amounts() in the module; they are looked up at call time, so the order is fine.

patch("detectors/text_detectors.py", [
    ("Japanese deadline (までに), flag",
     "jo më vonë)') as deadline,",
     "jo më vonë)') or regexp_matches(d.context, '(日|年度|末)までに') as deadline,"),
    ("Japanese deadline (までに), score",
     "jo më vonë|report|submit|bericht|informe)') then 0 else 0.3 end)",
     "jo më vonë|report|submit|bericht|informe)') or regexp_matches(d.context, '(日|年度|末)までに') then 0 else 0.3 end)"),
])

patch("ingest/refscan.py", [
    ("Japanese branch articles (第十六条の二)",
     'CJK = re.compile(r"第\\s*([\\d一二三四五六七八九十百千〇零]{1,8})\\s*[條条](?:\\s*之\\s*(\\d{1,3}))?")',
     'CJK = re.compile(r"第\\s*([\\d一二三四五六七八九十百千〇零]{1,8})\\s*[條条](?:\\s*之\\s*(\\d{1,3}))?((?:の[一二三四五六七八九十百〇\\d]{1,6})*)")'),
    ("Japanese branch articles: key",
     '                first = str(kanji_int(m.group(1)))\n',
     '                first = str(kanji_int(m.group(1))) + "".join("-" + str(kanji_int(x)) for x in re.findall(r"の([^の]+)", m.group(3) or ""))\n'),
    ("Japanese: another act named before the reference",
     '    return bool(EXT_BEFORE.search(before[-60:]) or EXT_AFTER.match(tail))',
     '    return bool(EXT_BEFORE.search(before[-60:]) or EXT_AFTER.match(tail) or JP_EXT.search(before[-20:]))\n\n\n'
     '# Japanese: 地方自治法第二条, 法第十条, 施行令第三条, 同法第五条, （昭和二十二年法律第六十七号）第二条 (本法 is this act)\n'
     'JP_EXT = re.compile(r"(?:(?<!本)法|令|規則|規程|条例|条約|協定|）)\\s*$")'),
    ("Japanese: 附則 (supplementary provisions) is its own series",
     'r"schluss\\w*|annex|anhang|anlage|schedule|annexe|anexo|supplementary|additional)\\s*$")',
     'r"schluss\\w*|annex|anhang|anlage|schedule|annexe|anexo|supplementary|additional|附則)\\s*$")'),
    ("Japanese file names art-016-2 (article 16-2)",
     '    m = re.match(r"(?i)^(?:(?:ugovor|naredba)[-_])?(?:art|madde',
     '    j = re.match(r"^art-0*(\\d{1,4})((?:-\\d{1,3})+)$", base) if _LANG["v"] == "ja" else None\n'
     '    if j:  # Japanese 第十六条の二 is art-016-2.md\n'
     '        return str(int(j.group(1))) + "".join("-" + str(int(x)) for x in j.group(2).split("-")[1:])\n'
     '    m = re.match(r"(?i)^(?:(?:ugovor|naredba)[-_])?(?:art|madde'),
    ("language from pins.json for importers (placeholder_ref)",
     '_LANG = {"v": ""}\n',   # appended after the kit's line, which patch_detectors.py looks for
     '_LANG = {"v": ""}\n'
     'try:  # one() sets it per corpus; importers (placeholder_ref) get the one pinned corpus\'s language\n'
     '    _LANG = {"v": (lambda cs: (cs[0].get("language") or "").lower() if len(cs) == 1 else "")(pins()["corpora"])}\n'
     'except Exception:\n'
     '    pass\n'),
])

patch("detectors/placeholder_ref.py", [
    ("Japanese placeholder 第十条　削除",
     '    if not substantive:\n        return bool(GONE.search(head)',
     '    if re.fullmatch(r"第\\S{1,12}条(?:の\\S{1,8})?[\\s　]+削除", substantive.strip()):  # Japanese: deleted, number kept\n'
     '        return True\n'
     '    if not substantive:\n        return bool(GONE.search(head)'),
])

patch("detectors/trailer_only.py", [
    ("Promulgated: trailer",
     "      try_cast(regexp_extract(json_extract_string(trailers, '$.Issued[0]'), '\\\\d{4}-\\\\d{2}-\\\\d{2}') as date)) as made,",
     "      try_cast(regexp_extract(json_extract_string(trailers, '$.Issued[0]'), '\\\\d{4}-\\\\d{2}-\\\\d{2}') as date),\n"
     "      try_cast(regexp_extract(json_extract_string(trailers, '$.Promulgated[0]'), '\\\\d{4}-\\\\d{2}-\\\\d{2}') as date)) as made,"),
    ("Promulgated: field name",
     "         else 'Issued' end as made_field,",
     "         when json_extract_string(trailers, '$.Issued[0]') is not null then 'Issued'\n"
     "         else 'Promulgated' end as made_field,"),
])

# ---------------------------------------------------------------- round 2 (after the first run's dangling references)
patch("ingest/refscan.py", [
    ("Japanese: a list of references continues the act named before it",
     '    return bool(EXT_BEFORE.search(before[-60:]) or EXT_AFTER.match(tail) or JP_EXT.search(before[-20:]))',
     '    return bool(EXT_BEFORE.search(before[-60:]) or EXT_AFTER.match(tail) or jp_external(before))'),
    ("Japanese: list continuation, abbreviations ending in 基準",
     'JP_EXT = re.compile(r"(?:(?<!本)法|令|規則|規程|条例|条約|協定|）)\\s*$")',
     'JP_EXT = re.compile(r"(?:(?<!本)法|令|規則|規程|条例|条約|協定|基準|）|附則)\\s*$")\n'
     '# one link of a Japanese list of references: 第十条, 第二項, 第三十四条の二, （…を除く。）, 、 及び 並びに 若しくは 又は から まで ―\n'
     'JP_LINK = re.compile(r"(?:第[〇一二三四五六七八九十百千\\d]+(?:条|項|号|章|節|款|目|編)(?:の[〇一二三四五六七八九十百千\\d]+)*|"\n'
     '                     r"（[^（）]{0,80}）|[、，・\\s]|及び|並びに|若しくは|又は|から|まで|―|－|ただし書|前段|後段|本文|各号)$")\n\n\n'
     'def jp_external(before: str) -> bool:\n'
     '    """the reference is one of a list that began with another act (地方自治法第二条、第十条及び第十一条) or 附則."""\n'
     '    s = before[-400:]\n'
     '    if not s or not ("\\u3000" <= s[-1] <= "\\u9fff" or s[-1] in "\\uff08\\uff09\\uff0c\\uff1a"):\n'
     '        return False\n'
     '    for _ in range(200):\n'
     '        m = JP_LINK.search(s[-90:])\n'
     '        if not m or not m.group(0):\n'
     '            break\n'
     '        s = s[:len(s) - len(m.group(0))]\n'
     '    return bool(JP_EXT.search(s[-20:]))'),
    ("Japanese range files art-029-to-031 (articles 29 to 31) hold their numbers",
     '        for k in {heading_key(text), path_key(path)} - {None}:\n            now.add((act_of(path), k))',
     '        for k in ({heading_key(text), path_key(path)} | set(range_keys(path))) - {None}:\n            now.add((act_of(path), k))'),
    ("range_keys",
     'def act_of(path: str) -> str:',
     'def range_keys(path: str) -> list[str]:\n'
     '    """Japanese: art-029-to-031.md holds articles 29 to 31 (usually 削除)."""\n'
     '    m = re.match(r"^art-0*(\\d{1,4})-to-0*(\\d{1,4})$", path.rsplit("/", 1)[-1].rsplit(".", 1)[0]) if _LANG["v"] == "ja" else None\n'
     '    return [str(k) for k in range(int(m.group(1)), int(m.group(2)) + 1)] if m and int(m.group(2)) - int(m.group(1)) < 500 else []\n\n\n'
     'def act_of(path: str) -> str:', "def range_keys("),
])
patch("detectors/placeholder_ref.py", [
    ("Japanese placeholder ranges 第二十九条から第三十一条まで　削除",
     '    if re.fullmatch(r"第\\S{1,12}条(?:の\\S{1,8})?[\\s　]+削除", substantive.strip()):  # Japanese: deleted, number kept',
     '    if re.fullmatch(r"第[^\\s条]{1,12}条(?:の[^\\s条]{1,8})*(?:(?:から|及び|、)第[^\\s条]{1,12}条(?:の[^\\s条]{1,8})*(?:まで)?)*[\\s　]+削除",\n'
     '                    substantive.strip()):  # Japanese: deleted, number kept'),
    ("Japanese range files hold every number in the range",
     '    holders = {}\n    for path, t in text.items():\n        k = path_key(path)\n        if not k:\n            continue\n'
     '        if is_placeholder(t):\n            holders[(act_of(path), k)] = (path, re.sub(r"\\s+", " ", t)[:200])',
     '    holders = {}\n    for path, t in text.items():\n        if range_keys(path) and is_placeholder(t):  # Japanese: art-029-to-031.md, 削除\n'
     '            for k in range_keys(path):\n                holders[(act_of(path), k)] = (path, re.sub(r"\\s+", " ", t)[:200])\n'
     '        k = path_key(path)\n        if not k:\n            continue\n'
     '        if is_placeholder(t):\n            holders[(act_of(path), k)] = (path, re.sub(r"\\s+", " ", t)[:200])'),
    ("import range_keys",
     'from refscan import refs, path_key, act_of, is_external, before_ref',
     'from refscan import refs, path_key, act_of, is_external, before_ref, range_keys'),
])

# ---------------------------------------------------------------- round 3 (after the second run's samples)
patch("ingest/refscan.py", [
    ("Japanese: 法律 ends an act's name; quoted wording (「…」) is another text's",
     'JP_EXT = re.compile(r"(?:(?<!本)法|令|規則|規程|条例|条約|協定|基準|）|附則)\\s*$")',
     'JP_EXT = re.compile(r"(?:(?<!本)法|法律|令|規則|規程|条例|条約|協定|基準|）|附則)\\s*$")', "|基本法|"),
    ("Japanese: a reference inside 「…」 quotes another text",
     '    s = before[-400:]\n    if not s or not',
     '    if before.count("「") > before.count("」"):  # inside a quotation (読替え: 「第十七条」とあるのは)\n'
     '        return True\n'
     '    s = before[-400:]\n    if not s or not'),
    ("Japanese range files with branch numbers (art-020-2-to-020-4, art-024-to-027-3)",
     '    m = re.match(r"^art-0*(\\d{1,4})-to-0*(\\d{1,4})$", path.rsplit("/", 1)[-1].rsplit(".", 1)[0]) if _LANG["v"] == "ja" else None\n'
     '    return [str(k) for k in range(int(m.group(1)), int(m.group(2)) + 1)] if m and int(m.group(2)) - int(m.group(1)) < 500 else []',
     '    m = re.match(r"^art-0*(\\d{1,4})((?:-\\d{1,3})*)-to-0*(\\d{1,4})((?:-\\d{1,3})*)$", path.rsplit("/", 1)[-1].rsplit(".", 1)[0]) if _LANG["v"] == "ja" else None\n'
     '    if not m or int(m.group(3)) - int(m.group(1)) >= 500:\n'
     '        return []\n'
     '    a, b = int(m.group(1)), int(m.group(3))\n'
     '    ks = [str(k) for k in range(a, b + 1)]\n'
     '    lo = int(m.group(2).split("-")[1]) if m.group(2) else 1\n'
     '    hi = int(m.group(4).split("-")[1]) if m.group(4) else 1\n'
     '    if a == b:  # art-020-2-to-020-4: 20-2 ... 20-4\n'
     '        return [str(a) if k == 1 else f"{a}-{k}" for k in range(lo, hi + 1)]\n'
     '    return ks + [f"{a}-{k}" for k in range(max(lo, 2), 11)] + [f"{b}-{k}" for k in range(2, hi + 1)]'),
    ("own range is the file's own label; tables of contents are not references",
     '        seen = {heading_key(text), path_key(path)}\n        for k, ctx, tail in refs(text):',
     '        seen = {heading_key(text), path_key(path)} | set(range_keys(path))\n'
     '        if _LANG["v"] == "ja" and path.endswith("/toc.md"):  # 目次: chapter spans, not references\n'
     '            continue\n'
     '        for k, ctx, tail in refs(text):'),
])
patch("detectors/placeholder_ref.py", [
    ("Japanese: tables of contents and a range file's own numbers",
     '        if a not in acts or (a, path_key(path)) in holders:\n            continue',
     '        if a not in acts or (a, path_key(path)) in holders:\n            continue\n'
     '        if path.endswith("/toc.md") and refscan_lang() == "ja":  # 目次: chapter spans, not references\n'
     '            continue'),
    ("refscan language",
     'from refscan import refs, path_key, act_of, is_external, before_ref, range_keys',
     'from refscan import refs, path_key, act_of, is_external, before_ref, range_keys, _LANG as _REFLANG\n\n\n'
     'def refscan_lang() -> str:\n    return _REFLANG["v"]'),
])

# ---------------------------------------------------------------- round 4: 基本法 (災害対策基本法第四十八条) is another act
patch("ingest/refscan.py", [
    ("Japanese: 基本法 ends an act's name (本法 alone is this act)",
     'JP_EXT = re.compile(r"(?:(?<!本)法|法律|令|規則|規程|条例|条約|協定|基準|）|附則)\\s*$")',
     'JP_EXT = re.compile(r"(?:(?<!本)法|基本法|法律|令|規則|規程|条例|条約|協定|基準|）|附則)\\s*$")'),
])

print("done:", *done, sep="\n  ")
print("already there:", len(skipped))
