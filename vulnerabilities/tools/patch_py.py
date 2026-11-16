"""Paraguayan (Spanish) blind spots, in a copy of global-law's vulnerabilities/scripts (idempotent; every pair has a marker
that stays in place if a later patch edits the same text):
- detectors/currency_scan.py: in Spanish, "marco" is a framework ("8. marco penal:", Código Penal art. 14; "Estrategia
  ... 2017, marco político", "directiva marco 84/532/CEE" in spain-law), not the Deutsche Mark. For Spanish only, the
  mark is now read as "marcos" after an amount ("424.394.963 marcos", which spain-law holds) or "marco(s) alemán/alemanes".
- detectors/notes_scan.py: "no pudo realizarse" / "no ha podido realizarse" is ordinary law text in Spanish ("Si ésta no
  pudo realizarse, se estará a su valor", Código Civil art. 982; "si la entrega no ha podido realizarse" in spain-law's
  treaties; "no pudo realizarse el pago" in colombia-law): every hit of the realizar/ejecutar forms in five Spanish
  repositories was law text. Those forms now need a modification as their subject ("la modificación no pudo
  realizarse"); "no ha podido ser incorporada" is read as before.
- detectors/notes_scan.py (all languages): patch_mx.py's comment ran on into the Austrian RIS pattern r"\\(Anm\\.: richtig"
  that an earlier patch had put on the same line, so that pattern was commented out. It is put back on a line of its
  own (no effect on Paraguay; skipped if the line is no longer there).

    python -X utf8 patch_py.py <scripts dir>
"""
import sys
from pathlib import Path


def patch(rel, pairs):
    p = Path(sys.argv[1]) / rel
    s = p.read_text(encoding="utf-8")
    for name, a, b, marker, optional in pairs:
        if b in s or marker in s:  # the marker: in place even if another patch edited the same text since
            print("in place:", name)
        elif a in s:
            s = s.replace(a, b, 1)
            print("patched:", name)
        elif optional:
            print("not there, skipped:", name)
        else:
            raise SystemExit(f"not found: {name}")
    p.write_text(s, encoding="utf-8", newline="\n")


patch("detectors/currency_scan.py", [
    ("currency: Spanish 'marco' is a framework",
     "def pat_for(c):\n    cur = CUR\n",
     "def pat_for(c):\n    cur = CUR\n"
     "    if (c.get(\"language\") or \"\").lower() == \"es\":  # patch_py: Spanish \"marco\" = framework (\"8. marco penal\")\n"
     "        cur = cur.replace(r\"(?<![Dd]ecisión )(?-i:marcos?)\\b\", r\"(?<![Dd]ecisión )(?:(?-i:marcos)\\b(?!\\s*[0-9])|(?-i:marcos?)\\s+alem[aá]n)\")\n",
     "# patch_py: Spanish \"marco\" = framework",
     False),
])

patch("detectors/notes_scan.py", [
    ("publisher notes: Spanish 'no pudo realizarse' is law text",
     'r"no (pudo|ha podido) (ser )?(incorporad|realizar|ejecutar)", ',
     'r"no (pudo|ha podido) (ser )?incorporad",\n'
     '    # patch_py: "no pudo realizarse" alone is law text in Spanish (Código Civil del Paraguay, art. 982)\n'
     '    r"(modificaci[oó]n|reforma|redacci[oó]n) no (pudo|ha podido) (ser )?(realizar|ejecutar)", ',
     '# patch_py: "no pudo realizarse" alone',
     False),
    ("publisher notes: the RIS pattern commented out by patch_mx's comment",
     '"(funcionario, sic DOF 20-01-1975)" r"\\(Anm\\.: richtig",',
     '"(funcionario, sic DOF 20-01-1975)"\n    r"\\(Anm\\.: richtig",  # patch_py: back on a line of its own',
     '# patch_py: back on a line of its own',
     True),
])
