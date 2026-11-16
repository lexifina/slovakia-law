"""Mexican blind spot, in a copy of global-law's vulnerabilities/scripts (idempotent):
- detectors/notes_scan.py: the Cámara de Diputados marks a slip in the published text with "(sic DOF 03-02-1983)", the
  DOF issue that carried it, sometimes with the right word first ("(funcionario, sic DOF 20-01-1975)"). The scan read
  only "(sic)" and "[sic]", so it found 6 of these notes and missed 49 (41 files). The two forms are now read in every
  corpus: elsewhere "sic DOF" does not occur.

    python -X utf8 patch_mx.py <scripts dir>
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


patch("detectors/notes_scan.py", [
    ("publisher notes: the Cámara's (sic DOF dd-mm-yyyy)",
     'r"\\[sic\\]", r"\\(sic\\)",',
     'r"\\[sic\\]", r"\\(sic\\)", r"\\bsic DOF [0-9]",  # mexico-law: "(sic DOF 03-02-1983)", "(funcionario, sic DOF 20-01-1975)"',
     'r"\\bsic DOF [0-9]"'),
])
