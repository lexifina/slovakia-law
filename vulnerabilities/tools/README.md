# Tools

The scripts behind this Slovakia-only run of global-law's vulnerability detectors. They run inside a copy of
[global-law/vulnerabilities/scripts](https://github.com/lexifina/global-law/tree/main/vulnerabilities/scripts) (Python 3.11+,
`pip install duckdb pyarrow`), with a bare clone of this repository at `sources/corpus/slovakia-law.git`, a blobless bare clone
of global-law at `sources/global-law.git`, and a `pins.json` that names only slovakia-law and its commit (language `sk`).
`build_vulns.py`, `flags_chart.py`, `late_ext_select.py`, `late_ext_rebut.py` and `config.json` sit two folders above the
scripts.

| Script | What it does |
| --- | --- |
| `run.sh` | Indexes the history and texts, maps paths to each act's folder (`map_moved.py`), adds this repository's history rows, and runs the detectors (`bash run.sh <shards>`) |
| `map_moved.py` | Rewrites the paths in the history table to each act's folder since the move of 10 November 2026 (`data/paths.json`, `zz-2001-311/` to `zz/2001/311/`), so that an act's history is not split in two at the move; here it rewrote 325,928 paths of 5,928 folders |
| `add_root.py` | Builds the history rows from this repository's own commits (global-law replays it only up to an earlier commit), so the history detectors read every change; changed for this repository (below) |
| `run_triage.sh` | The model review: the 40 strongest flags per category, the 40 strongest lapsed time limits in law texts, and the empty periods |
| `late_ext_select.py` | Chooses the empty periods for global-law's review of that category: those whose old and new date stand in one sentence, then the shortest gaps |
| `late_ext_rebut.py` | Adds the second, arguing-against pass to the empty-period review, as `triage.py` does for the other categories |
| `build_vulns.py` | Builds `data/flags.csv`, `data/reviewed.csv` and `data/by_category.csv` from the findings and the model review; changed for this repository (below) |
| `flags_chart.py` | Draws the chart at the top of the READMEs, in Slovak and English, light and dark |
| `config.json` | The repository, the Slovak category names and chart labels, and what is not law: `data/`, `tools/`, `vulnerabilities/` and the root files (`README`, `REPRODUCE.md`, `PLAN.md`, `LICENSE`, `predpisy.csv`, `corpus.json`); every other top-level folder (`constitution/`, `volebny-zakon/`, `zz/`, `zb/`, `ro/`, `local/`) holds law |
| `apply_patches.py` | Applies the patches below to a copy of the scripts, each once, in a fixed order, and records them in `.kit_patches.json` (`python -X utf8 apply_patches.py <scripts dir>`); later patches edit text earlier ones inserted, so a patch is never run twice on the same copy. `patch_sk.py` is last in its order |
| `patch_detectors.py` | Fixes blind spots found in runs on several country repositories in the copy of global-law's scripts |
| `patch_detectors_vi.py`, `patch_es.py`, `patch_ca.py`, `patch_en.py`, `patch_de.py`, `patch_en_et.py`, `patch_co.py`, `patch_sv.py`, `patch_pt.py`, `patch_ru.py`, `patch_r18.py`, `patch_xk.py`, `patch_mo.py`, `patch_lu.py`, `patch_li.py`, `patch_mx.py`, `patch_mn.py`, `patch_mt.py`, `patch_np.py`, `patch_en_nr.py`, `patch_dv.py`, `patch_az.py`, `patch_ar.py`, `patch_en_nz.py`, `patch_nb.py`, `patch_mk.py`, `patch_pa.py`, `patch_py.py`, `patch_pe.py`, `patch_en_ph.py`, `patch_qa.py`, `patch_nl.py`, `patch_it.py`, `patch_pl.py`, `patch_ru_fz.py` | The same for the dates, references and currency names of other languages and jurisdictions; they change nothing in Slovak text (`patch_ru_fz.py`, Russian only, was applied after this run) |
| `patch_ja.py` | Japanese fixes, kept with the kit but not in `apply_patches.py`'s order; not applied here |
| `patch_sk.py` | The Slovak fixes made for this repository, in the same form (`python -X utf8 patch_sk.py <scripts dir>`; a fix already in place is skipped; see below) |
| `patch_build_r7.py`, `patch_build_links.py` | Bring a country's `build_vulns.py` up to date (lapsed-limit reviews matched on 400 characters of context, links to files deleted before a folder move); already applied to the `build_vulns.py` here |
| `redo.py` | Runs `apply_patches.py`, then again only the scans and detectors the fixes change, the model review of lapsed time limits, references to deleted provisions and empty periods, and the build (`python -X utf8 redo.py <run folder> [--keep-reviews] [--full]`); not used here: the scans and the reference review were re-run by hand (below) |

The model review needs `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL` and `LLM_AUTH` set for an OpenAI-compatible Responses API.
It was run as `bash run_triage.sh '^(data|tools|vulnerabilities)/|^(README|REPRODUCE|PLAN|LICENSE|predpisy|corpus)'`.

Changes made for this repository:

- `add_root.py` counts as law, besides commits with no `Kind:` trailer and `Kind: law`, the `Kind` values this repository
  gives real changes: `unexplained` (a version for which Slov-Lex names no amending act) and `candidates` (several acts
  took effect that day and Slov-Lex does not say which changed what), the kinds of amending act the Constitution's and the
  election act's changes carry (`zákon`, `ústavný zákon`, `nález`, `uznesenie`), and `local` (the cities' VZN). 32,782
  commits count as law; `baseline`, `documentation` and the court record keep their own kind.
- `patch_sk.py`, Slovak dates, amounts and references, made after testing the scans on this repository's text:
  - `ingest/textscan.py`: "do konca roka 2012" and "do konca roku 2012" (until the end of the year) are 31 December. The
    Slovak month names ("31. decembra 2020"), the dates with dots and spaces ("31. 12. 2020") and "najneskôr" (at the
    latest) were already read. Amounts in Slovak korunas ("5 000 Sk", "100 000 slovenských korún", "500 korún") and
    Czechoslovak korunas ("2 000 Kčs") are read as amounts, with units `sk` and `kčs`, so a change of one can leave a
    stale amount; "Sk" and "Kčs" only with that capitalisation.
  - `detectors/currency_scan.py`: for Slovakia (code `SK`) the Slovak koruna (replaced by the euro) and
    the Czechoslovak koruna are dead currencies; before, none of the 9,697 amounts was found.
  - `detectors/placeholder_ref.py`: in Slovak, a placeholder is a section whose body reads only "Zrušený.", "– zrušený",
    "(zrušené včítane nadpisov)" and the like, or a heading ending in it, not any section with "zrušen-" in its first
    70 characters ("Rozhodnutie o zrušení akreditácie", "okamžitým zrušením"): 120 references to repealed placeholders
    became 42.
  - `ingest/refscan.py`: a reference followed, after any list of units, by another act's name ("§ 7 ods. 1 zákona
    č. 1/1991 Zb.", "§ 93, 94 Tr. zák.", "§ 49 a 50 správního řádu", "§ 270a Zákonníka práce", "§ 3, 16, 19, 20 a 21
    vládneho nariadenia") is to that act, read up to 300 characters on as for Polish; "tohto zákona" (this act) stays
    this act's. With it the references to repealed placeholders became 8.
  - `detectors/ref_detectors.py`: Slovak amending sentences ("sa vkladá", "sa nahrádza", "sa vypúšťa", "sa dopĺňa",
    "znie:", "strácajú účinnosť") quote another act's provisions, as the Czech ones already listed do; "zákonníka",
    "nariadenia", "poriadku", "Ústavy", "dohovoru" and "smernice" after a reference name another act; "tohto" and "tejto"
    (this) keep it this act's. With both reference fixes the references to deleted provisions went from 377 to 225.
- `build_vulns.py` drops exact duplicate rows (marked `EXACT_DUP_ROWS`): this repository writes the history of 1,432 act
  folders twice, so the empty-period detector found 23 extensions twice.
- The first run's text scan (`ingest/textscan.py`) wrote nothing and printed nothing, so the lapsed time limits and
  stale amounts were missing (`text_detectors.py` then failed on the empty `index/dates/`); run alone it worked, and the
  scans and detectors were run again from the text scan onward with `patch_sk.py` in place. The reference scan and the
  reference detectors were run once more after the reference fixes, and the references to deleted provisions were
  sent to the model again (the 40 earlier reviews of that category were set aside).
