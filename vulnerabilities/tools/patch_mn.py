r"""Mongolian blind spots, in a copy of global-law's vulnerabilities/scripts (idempotent; every pair has a marker that
survives later edits of the same text):
- ingest/textscan.py: Mongolian writes the year first, the month as an ordinal number and "until" after the date:
  "2020 оны 12 дугаар сарын 31-ний өдрийг хүртэл", "... 31-ний өдөр хүртэлх хугацаанд", "... 31-ний өдрийг дуустал"
  (= until it ends), "2000 он дуусталх" (until the year 2000 ends); no time limit was read (0 of 191 such dates in the
  current text). Read only for a corpus whose language is "mn". "2030 он хүртэл" (year only, "until 2030") is left out:
  it does not say whether the year itself is included.
- ingest/refscan.py: articles are files zuil-21.md (zuil-19-1.md: article 19¹) and had no key, so placeholder_ref,
  dead_fine and the history scan saw no provision; "энэ хуулийн 7 дугаар зүйл" (article 7 of this law) was not read as a
  reference (only "хуулийн 7.1-д" was); and a reference to another law ("Эрүүгийн хуулийн 131.1-д",
  "Банкны тухай хуулийн 3 дугаар зүйл") was read as one to the act's own article: for "mn", only "энэ хуулийн/журмын/
  дүрмийн ..." (this law, these rules) is the act's own.
- detectors/placeholder_ref.py: a repealed article's file holds "128 дугаар зүйл./Энэ зүйлийг 1993 оны 6 дугаар сарын
  7-ны өдрийн хуулиар хүчингүй болсонд тооцсон./"; "хүчингүй болсонд тооцсон" (deemed repealed) was not a repeal
  marker, and the article label at the start of the same line pushed the marker past the 70 characters it may start in.

    python -X utf8 patch_mn.py <scripts dir>
"""
import sys
from pathlib import Path


def patch(rel, pairs):
    p = Path(sys.argv[1]) / rel
    s = p.read_text(encoding="utf-8")
    for name, a, b, marker in pairs:
        if b in s or marker in s:  # the marker: in place even if another patch edited the same text since
            print("in place:", name)
        elif a in s:
            s = s.replace(a, b, 1)
            print("patched:", name)
        else:
            raise SystemExit(f"not found: {name}")
    p.write_text(s, encoding="utf-8", newline="\n")


patch("ingest/textscan.py", [
    ("LIMIT_MN",
     '\nCUR = (r"',
     '\n# patch_mn: Mongolian puts "until" after the date: "2020 оны 12 дугаар сарын 31-ний өдрийг хүртэл", "... 31-ний өдөр\n'
     '# хүртэлх хугацаанд", "... 31-ний өдрийг дуустал" (until it ends), "2000 он дуусталх" (until the year 2000 ends)\n'
     'LIMIT_MN = re.compile(r"(?i)(?<!\\d)(?P<y10>\\d{4})\\s+(?:оны\\s+(?P<m10>\\d{1,2})\\s*(?:-?р|дугаар|дүгээр)\\s+сарын\\s+(?P<d10>\\d{1,2})"\n'
     '                      r"(?:\\s*-\\s*[а-яёөү]+)?(?:\\s+өдр[а-яёөү]*|\\s+өдөр)?\\s+(?:хүртэл|дуустал)|он\\s+дуустал)")\n'
     'CUR = (r"',
     "LIMIT_MN = re.compile("),
    ("limits: read LIMIT_MN for mn",
     "    post = list(LIMIT_POST.finditer(text)) if _POST_WORDS.search(text) else []\n",
     "    post = list(LIMIT_POST.finditer(text)) if _POST_WORDS.search(text) else []\n"
     "    if _LANG[\"v\"] == \"mn\":  # patch_mn\n"
     "        post += list(LIMIT_MN.finditer(text))\n",
     "post += list(LIMIT_MN.finditer(text))"),
    ("limits: a Mongolian date",
     '            if g.get("y6") or g.get("y7"):\n',
     '            if g.get("y10"):  # patch_mn: "2020 оны 12 дугаар сарын 31", or the year\'s end ("2000 он дуустал")\n'
     '                y, mo, d = int(g["y10"]), int(g.get("m10") or 12), int(g.get("d10") or 31)\n'
     '            elif g.get("y6") or g.get("y7"):\n',
     'if g.get("y10"):  # patch_mn'),
])
patch("ingest/refscan.py", [
    ("MONGOL: N дугаар зүйл",
     'MONGOL = re.compile(r"(?:хуулийн|журмын|дүрмийн)\\s+(\\d{1,4})(?:\\.\\d{1,3})*(?:\\s*-?\\s*(?:т|д|ыг|ийн|д заасан|т заасан))")\n',
     '# patch_mn: also "хуулийн 7 дугаар зүйл" (article 7 of the law), not only "хуулийн 7.1-д"\n'
     'MONGOL = re.compile(r"(?:хуулийн|журмын|дүрмийн)\\s+(\\d{1,4})(?:(?:\\.\\d{1,3})*(?:\\s*-?\\s*(?:т|д|ыг|ийн|д заасан|т заасан))"\n'
     '                    r"|\\s+(?:дугаар|дүгээр)\\s+зүйл)")\n',
     'patch_mn: also "хуулийн 7 дугаар зүйл"'),
    ("path_key: zuil-NN",
     '    m = re.match(r"(?i)^(?:(?:ugovor|naredba)',
     '    z = re.match(r"^zuil-0*(\\d{1,4})(?:-(\\d{1,3}))?$", base)  # patch_mn: zuil-21.md is article 21, zuil-19-1.md article 19¹\n'
     '    if z:\n'
     '        return f"{int(z.group(1))}-{z.group(2)}" if z.group(2) else str(int(z.group(1)))\n'
     '    m = re.match(r"(?i)^(?:(?:ugovor|naredba)',
     "patch_mn: zuil-21.md is article 21"),
    ("refs: only энэ хуулийн is the act's own (mn)",
     "            if is_external(before, tail):\n                continue\n",
     "            if is_external(before, tail):\n                continue\n"
     "            if rx is MONGOL and _LANG[\"v\"] == \"mn\" and not re.search(r\"(?i)(?<!\\w)энэ\\s*$\", before):\n"
     "                continue  # patch_mn: only \"энэ хуулийн\" (this law) is the act's own; \"Эрүүгийн хуулийн 131.1\" is another act\n",
     "patch_mn: only \"энэ хуулийн\""),
])
patch("detectors/placeholder_ref.py", [
    ("GONE: хүчингүй болсонд тооцсон",
     r'r"sin efecto|sans objet|',
     r'r"sin efecto|sans objet|хүчингүй болсонд тооцсон|',
     "|хүчингүй болсонд тооцсон|"),
    ("is_placeholder: drop the Mongolian article label",
     "\n\ndef is_placeholder(text: str) -> bool:\n",
     "\n\n# patch_mn: \"128 дугаар зүйл./Энэ зүйлийг ... хүчингүй болсонд тооцсон./\" has the label on the marker's line\n"
     "MN_LABEL = re.compile(r\"^\\d{1,4}(?:-\\d{1,3})?\\s+(?:дугаар|дүгээр)\\s+зүйл\\s*\\.?\")\n\n\n"
     "def is_placeholder(text: str) -> bool:\n",
     "MN_LABEL = re.compile("),
    ("is_placeholder: use MN_LABEL",
     "    lines = [l.strip() for l in text.splitlines() if l.strip()]\n    head = ",
     "    lines = [l.strip() for l in text.splitlines() if l.strip()]\n"
     "    lines = [MN_LABEL.sub(\"\", l, count=1).strip() or l for l in lines]  # patch_mn\n    head = ",
     "MN_LABEL.sub(\"\", l, count=1)"),
])
