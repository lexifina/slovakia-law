"""Qatar (Arabic), in a copy of global-law's vulnerabilities/scripts (once, after the kit's other patches and patch_ar.py;
every change carries a "patch_qa" marker that later edits keep):
- ingest/textscan.py, time limits: a period "ending on" a date was not read: "لمدة سنتين تنتهي في 30/10/2000" (for two
  years ending on 30/10/2000), "تبدأ من أول مايو 2008 وتنتهي في 31 ديسمبر 2009", "تنتهي في يوم 30 يونيه عام 2004".
  تنتهي/ينتهي (it ends), with "و" (and) before and "في" (on) after, now count as "until" before a date, as "expires on"
  does in English. Like patch_ar's words, they cannot occur in another script.
- detectors/currency_scan.py: the Gulf rupee (روبية), Qatar's currency until 1966, is dead in Qatar only. Qatari texts
  write it after the amount in words or in brackets ("خمسة آلاف روبية", "50 ألف روبية", "(20) روبية"), so the word is read
  on its own, in a corpus whose code is QA (the riyal, "ريال", is current).

    python -X utf8 patch_qa.py <scripts dir>      (after the kit's patches; apply_patches.py runs it last)
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
ENDING = ('# patch_qa: "ending on" a date: "لمدة سنتين تنتهي في 30/10/2000", "وتنتهي في 31 ديسمبر 2009", "تنتهي في يوم 30 يونيه"\n'
          'UNTIL = r"و?(?:تنتهي|ينتهي)(?:\\s+في)?|" + UNTIL\n')

RET = '    return rf"{NUM}\\s*{cur}|{cur}\\s*{NUM}"\n'
RUPEE = ('    if (c.get("code") or "").upper() == "QA":  # patch_qa: the Gulf rupee, Qatar\'s currency until 1966, after the\n'
         '        # amount in words or in brackets ("خمسة آلاف روبية", "50 ألف روبية", "(20) روبية"), read as a word of its own\n'
         '        return rf"{NUM}\\s*{cur}|{cur}\\s*{NUM}" + r"|(?:^|\\s|\\()(?:ال|ب)?روبي(?:ة|ات)(?=$|\\s|[.,:)]|،|؛)"\n'
         + RET)

patch("ingest/textscan.py", [
    ("qa: 'ending on' a date", LIMIT_LINE, ENDING + LIMIT_LINE, '# patch_qa: "ending on"'),
])
patch("detectors/currency_scan.py", [
    ("qa: the Gulf rupee", RET, RUPEE, "# patch_qa: the Gulf rupee"),
])
