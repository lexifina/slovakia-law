"""Arabic (Oman), in a copy of global-law's vulnerabilities/scripts (once, after the kit's other patches; every change
carries a "patch_ar" marker that later edits keep).
- ingest/textscan.py, time limits: no Arabic "until" was read. "حتى ١ / ١١ / ١٩٩٦م" (until 1/11/1996), "لغاية 31 ديسمبر
  2020", "حتى تاريخ ..." and "قبل نهاية سنة ٢٠٢٤م" (before the end of 2024) are now read: حتى, وحتى, لغاية, ولغاية and
  "إلى غاية" before a date, "قبل" only before "نهاية" (the end of a year), "تاريخ"/"يوم" between them, and the Gregorian
  month names (يناير ... ديسمبر, with the spellings ابريل/إبريل, يونيه, يوليه, اغسطس, اكتوبر, and the Levantine كانون الثاني
  ... كانون الأول), with "من شهر" before the month and "سنة"/"عام" before the year. Arabic-Indic digits (٠-٩) need nothing:
  Python's \\d and int() read them. Hijri dates ("١٤٤٢هـ") are not read. The Arabic words cannot occur in another script,
  so the "until" words and month names apply to every corpus;
- ingest/textscan.py, amounts: amounts in rials and baisas were not read; the number (often in brackets, in either digit
  set) is followed by the amount in words and then the currency ("(٥٠٠) خمسمائة ريال عماني", "(١٠) عشرة ريالات عمانية").
  They are now read, as "rial" and "baisa", in a corpus whose language is "ar", for the search for stale amounts; the
  rule that drops a four-digit number starting 19 or 20 (a year) does not apply there, as the currency follows.

    python -X utf8 patch_ar.py <scripts dir>      (after the kit's patches; apply_patches.py runs it last)
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


LIMIT_LINE = 'LIMIT = re.compile(rf"(?i)\\b(?:{UNTIL})'
DATES = '''# patch_ar: Arabic "until" before the date ("حتى ١ / ١١ / ١٩٩٦م", "لغاية 31 ديسمبر 2020", "حتى تاريخ ..."), "قبل نهاية
# سنة ٢٠٢٤م" (before the end of 2024), and the Gregorian months; Arabic-Indic digits are \\d already. Hijri dates are not read.
AR_MONTHS = ("يناير كانون_الثاني", "فبراير شباط", "مارس آذار", "أبريل ابريل إبريل نيسان", "مايو أيار", "يونيو يونيه حزيران",
             "يوليو يوليه تموز", "أغسطس اغسطس آب", "سبتمبر أيلول", "أكتوبر اكتوبر تشرين_الأول", "نوفمبر تشرين_الثاني",
             "ديسمبر كانون_الأول")
for _n, _ms in enumerate(AR_MONTHS, 1):
    for _m in _ms.split():
        MI[_m.replace("_", " ")] = _n
AR_MON = "|".join(sorted((m.replace("_", " ") for ms in AR_MONTHS for m in ms.split()), key=len, reverse=True))
DATE = DATE.replace("(?P<mon>", "(?:من\\\\s+)?(?:شهر\\\\s+)?(?P<mon>" + AR_MON + "|", 1)
DATE = DATE.replace("(?:del?\\\\s+(?:año\\\\s+)?|", "(?:(?:سنة|عام)\\\\s+|del?\\\\s+(?:año\\\\s+)?|", 1)
DATE = DATE.replace("(?:kraja\\\\s+|", "(?:نهاية\\\\s+(?:سنة|عام|العام)\\\\s+|kraja\\\\s+|", 1)
UNTIL = r"وحتى|حتى|ولغاية|لغاية|إلى\\s+غاية|الى\\s+غاية|قبل(?=\\s+نهاية\\s)|" + UNTIL
DEADLINE = r"قبل(?=\\s+نهاية\\s)|" + DEADLINE
FILL = FILL.replace("(?:", "(?:تاريخ|يوم|", 1)
'''
AMT_DEFS = '''

# patch_ar: rials and baisas, "(٥٠٠) خمسمائة ريال عماني", "(١٠) عشرة ريالات عمانية", read only in a corpus whose language is "ar"
AR_DIGITS_TX = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
AR_AMT = re.compile(rf"(?<![\\d.,])\\(?(?P<arn>{NUM})\\)?\\s*(?:[\\u0621-\\u064A]+\\s+){{0,5}}?(?P<arc>ريال|بيس)")


def norm_num(s: str) -> str:'''

patch("ingest/textscan.py", [
    ("ar: until words, months, fillers", LIMIT_LINE, DATES + LIMIT_LINE, "# patch_ar: Arabic \"until\""),
    ("ar: amount pattern", "\n\ndef norm_num(s: str) -> str:", AMT_DEFS, "# patch_ar: rials and baisas"),
    ("ar: amounts in rials and baisas",
     '        out.add((v, "%" if pct else c.rstrip(".")))\n',
     '        out.add((v, "%" if pct else c.rstrip(".")))\n'
     '    if _LANG["v"] == "ar":  # patch_ar: rials and baisas (a year never comes before the currency)\n'
     '        for m in AR_AMT.finditer(text):\n'
     '            v = norm_num(m.group("arn").translate(AR_DIGITS_TX))\n'
     '            if v != "0" and len(v.split(".")[0]) >= 2:\n'
     '                out.add((v, "rial" if m.group("arc") == "ريال" else "baisa"))\n',
     "# patch_ar: rials and baisas (a year"),
])
