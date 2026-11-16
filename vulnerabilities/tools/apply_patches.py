"""Applies the kit's detector patches to a copy of global-law's vulnerabilities/scripts, each ONCE, in a fixed order.

    python -X utf8 apply_patches.py <scripts dir>

The patches were written one after another, and later ones edit text earlier ones inserted, so a patch's own "is it in
place?" check can fail on a second run. Each patch is therefore run once on a copy and recorded in
<scripts dir>/.kit_patches.json (name -> sha1 of the patch file when applied); a recorded patch is skipped. A patch whose
file changed since it was applied is reported, not re-run (re-running it on edited text is what breaks). A patch that
fails is reported and not recorded; the run goes on with the next one.
"""
import hashlib, json, os, subprocess, sys

K = os.path.dirname(os.path.abspath(__file__))
S = sys.argv[1]
ORDER = ["patch_detectors.py", "patch_detectors_vi.py", "patch_es.py", "patch_ca.py", "patch_en.py", "patch_de.py",
         "patch_en_et.py", "patch_co.py", "patch_sv.py", "patch_pt.py", "patch_ru.py", "patch_r18.py", "patch_xk.py", "patch_mo.py", "patch_lu.py", "patch_li.py", "patch_mx.py", "patch_mn.py", "patch_mt.py", "patch_np.py", "patch_en_nr.py", "patch_dv.py", "patch_az.py", "patch_ar.py", "patch_en_nz.py", "patch_nb.py", "patch_mk.py", "patch_pa.py", "patch_py.py", "patch_pe.py", "patch_en_ph.py", "patch_qa.py", "patch_nl.py", "patch_it.py", "patch_pl.py", "patch_ru_fz.py", "patch_sk.py"]
REC = os.path.join(S, ".kit_patches.json")
rec = json.load(open(REC, encoding="utf-8")) if os.path.exists(REC) else {}
sha = lambda f: hashlib.sha1(open(os.path.join(K, f), "rb").read()).hexdigest()
for f in ORDER:
    h = sha(f)
    if f in rec:
        if rec[f] != h:
            print(f"{f}: changed since it was applied here; not re-run (apply its new part by hand if needed)")
        continue
    r = subprocess.run([sys.executable, "-X", "utf8", os.path.join(K, f), S], capture_output=True, text=True, encoding="utf-8")
    if r.returncode:
        print(f"{f}: FAILED, not recorded: {(r.stdout + r.stderr).strip().splitlines()[-1:]}")
        continue
    rec[f] = h
    print(f"{f}: applied")
json.dump(rec, open(REC, "w", encoding="utf-8"), indent=1)
