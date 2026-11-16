"""Dhivehi (the Maldives), in a copy of global-law's vulnerabilities/scripts (once, after the kit's other patches; every
change carries a "patch_dv" marker that later edits keep). Dhivehi puts "until" after the date, in Thaana:
- ingest/textscan.py, time limits: "31 ޑިސެންބަރު 2024 ގެ ނިޔަލަށް" (until 31 December 2024) and "17 ނޮވެންބަރު 2018
  ނިޔަލަށް" were not read: no Dhivehi month name, and "until" (ނިޔަލަށް, sentence-final ނިޔަލަށެވެ) comes after the date.
  A day, a Dhivehi month (in every spelling the texts use: ޑިސެމްބަރ, ޑިސެމްބަރު, ޑިސެންބަރު; އެޕްރީލް, އޭޕްރިލް ...) and a
  four-digit year, then "ގެ ނިޔަލަށް" or "ނިޔަލަށް", are now read in a corpus whose language is "dv". Dates given only as a
  year ("2030 ވަނަ އަހަރުގެ ނިޔަލަށް", until the year 2030) are left out, as other languages leave out "until 2030";
- ingest/textscan.py, amounts: rufiyaa and US dollars were not read: the number is followed by the amount in words in
  brackets and then the currency, with Dhivehi case endings attached ("10,000 (ދިހަހާސް) ރުފިޔާއާ", "250000 (ދެލައްކަ
  ފަންސާސްހާސް) ޑޮލަރާ", "500 (ފަސްސަތޭކަ) އެމެރިކާ ޑޮލަރު"). They are now read as "mvr" and "usd" amounts in a "dv" corpus.

    python -X utf8 patch_dv.py <scripts dir>      (after the kit's patches; apply_patches.py runs it last)
"""
import sys
from pathlib import Path


def patch(rel, pairs):
    p = Path(sys.argv[1]) / rel
    s = p.read_text(encoding="utf-8")
    for name, a, b, marker in pairs:
        if marker in s:
            print("in place:", name)
        elif s.count(a) == 1:
            s = s.replace(a, b, 1)
            print("patched:", name)
        else:
            raise SystemExit(f"not found once: {name}")
    p.write_text(s, encoding="utf-8", newline="\n")


DEFS = '''

# patch_dv: Dhivehi (Thaana) dates and amounts, read only in a corpus whose language is "dv"
DV_MI = {}
for _n, _ms in enumerate(("ޖަނަވަރީ ޖެނުއަރީ", "ފެބުރުވަރީ ފެބްރުއަރީ ފެބުރުއަރީ", "މާރިޗު މާޗް މާޗު", "އެޕްރީލް އޭޕްރިލް އޭޕްރީލް އެޕްރިލް",
                          "މޭ މެއި", "ޖޫން", "ޖުލައި", "އޯގަސްޓް އޯގަސްޓު އޮގަސްޓް އޮގަސްޓު", "ސެޕްޓެމްބަރު ސެޕްޓެމްބަރ ސެޕްޓެންބަރު ސެޕްޓެންބަރ",
                          "އޮކްޓޫބަރު އޮކްޓޫބަރ އޮކްޓޯބަރު އޮކްޓޯބަރ", "ނޮވެމްބަރު ނޮވެމްބަރ ނޮވެންބަރު ނޮވެންބަރ",
                          "ޑިސެމްބަރު ޑިސެމްބަރ ޑިސެންބަރު ޑިސެންބަރ"), 1):
    for _m in _ms.split():
        DV_MI[_m] = _n
DV_MON = "|".join(sorted(DV_MI, key=len, reverse=True))
# "31 ޑިސެންބަރު 2024 ގެ ނިޔަލަށް" (until 31 December 2024), "... ގެ ނިޔަލަށެވެ." at the end of a sentence; RLM marks may precede digits
DV_LIMIT = re.compile(rf"[\\u200e\\u200f]?(?P<dvd>\\d{{1,2}})\\s*(?P<dvm>{DV_MON})\\s*(?:މަހުގެ\\s*)?[\\u200e\\u200f]?(?P<dvy>\\d{{4}})(?!\\d)"
                      r"\\s*(?:ގެ\\s*)?ނިޔަލަށ(?:ް|ެވެ)")
# "10,000 (ދިހަހާސް) ރުފިޔާއާ", "-/5,000 (ފަސްހާސް) ރުފިޔާ", "500 (ފަސްސަތޭކަ) އެމެރިކާ ޑޮލަރު", "250000 (...) ޑޮލަރާ"
DV_AMT = re.compile(rf"(?<![\\d,.])(?:-/)?(?P<dvn>{NUM})(?:/-)?\\s*(?:\\([^()\\n]{{1,60}}\\)\\s*)?(?:އެމެރިކާ\\s*)?(?P<dvc>ރުފިޔާ|ޑޮލަރ)")


def norm_num(s: str) -> str:'''

patch("ingest/textscan.py", [
    ("dv: months, limit and amount patterns", "\n\ndef norm_num(s: str) -> str:", DEFS, "# patch_dv: Dhivehi (Thaana) dates"),
    ("dv: amounts in rufiyaa and dollars",
     '        out.add((v, "%" if pct else c.rstrip(".")))\n    return out\n',
     '        out.add((v, "%" if pct else c.rstrip(".")))\n'
     '    if _LANG["v"] == "dv":  # patch_dv: rufiyaa and US dollars\n'
     '        for m in DV_AMT.finditer(text):\n'
     '            v = norm_num(m.group("dvn"))\n'
     '            if v != "0" and len(v.split(".")[0]) >= 2 and not (len(v) == 4 and v.startswith(("19", "20"))):\n'
     '                out.add((v, "mvr" if m.group("dvc") == "ރުފިޔާ" else "usd"))\n'
     '    return out\n',
     "# patch_dv: rufiyaa"),
    ("dv: until after the date",
     "    post = list(LIMIT_POST.finditer(text)) if _POST_WORDS.search(text) else []\n",
     "    post = list(LIMIT_POST.finditer(text)) if _POST_WORDS.search(text) else []\n"
     "    if _LANG[\"v\"] == \"dv\":\n"
     "        post += list(DV_LIMIT.finditer(text))  # patch_dv: \"31 ޑިސެންބަރު 2024 ގެ ނިޔަލަށް\"\n",
     "# patch_dv: \"31"),
    ("dv: parse the Dhivehi date",  # anchored on the branch's body, which patch_mn (it makes the "if" an "elif") leaves alone
     '                y, mo, d = int(g.get("y6") or g.get("y7")), 12, 31\n',
     '                y, mo, d = int(g.get("y6") or g.get("y7")), 12, 31\n'
     '            elif g.get("dvy"):  # patch_dv: day, Dhivehi month, year\n'
     '                y, mo, d = int(g["dvy"]), DV_MI[g["dvm"]], int(g["dvd"])\n',
     "# patch_dv: day, Dhivehi"),
])
