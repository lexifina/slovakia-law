"""Writes data/verzie.json and REPRODUCE.md into the Slovak law repository, from the facts of the build that made it.
Called by build.py; kept apart so the record of how the repository was made reads as one document.

The results of the checks (check_repo.py, test_repo.py and the rebuild that compares hashes) are read from
verification.json next to this file, which check_repo.py, `test_repo.py --record` and `build.py --verify-rebuild` write.
They describe the build before the one that writes this file, from the same data; a rebuild with the same data and the
same verification.json gives the same hashes."""
from __future__ import annotations

import datetime as dt
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent


def write_manifest(repo: Path, built: list[dict], today: str):
    """Every source page the text comes from, with its sha256, so a rebuild can show it read the same bytes."""
    out = {'built': today, 'source': 'https://static.slov-lex.sk', 'acts': [{
        'id': b['act']['id'], 'label': b['label'], 'slug': b['act']['slug'], 'title': b['title'],
        'versions': [{'from': v['from'], 'to': v['to'], 'acts': [b['laws'][l]['label'] for l in v['laws']],
                      'html': v['url'], 'sha256': v['sha256']} for v in b['versions']],
    } for b in built]}
    (repo / 'data').mkdir(exist_ok=True)
    (repo / 'data' / 'verzie.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8',
                                               newline='\n')


def write_reproduce(repo: Path, built: list[dict], log: list[dict], tags: dict, requests: list[dict], today: str):
    blob = subprocess.run(['git', 'hash-object', str(HERE / 'build.py')], capture_output=True, text=True).stdout.strip()
    pyv = subprocess.run(['python', '--version'], capture_output=True, text=True).stdout.strip()
    gitv = subprocess.run(['git', '--version'], capture_output=True, text=True).stdout.strip()
    try:
        import lxml.etree
        lxmlv = '.'.join(str(x) for x in lxml.etree.LXML_VERSION[:3])
    except Exception:
        lxmlv = '?'
    ver = json.loads((HERE / 'verification.json').read_text(encoding='utf-8')) if (HERE / 'verification.json').exists() else {}
    files = {r['file'] for r in requests if r['file'].exists()}
    days = sorted({dt.date.fromtimestamp(f.stat().st_mtime).isoformat() for f in files})
    urls = {r['url'] for r in requests}
    n_lists = sum(1 for u in urls if u.endswith('/'))
    n_versions = sum(1 for u in urls if u.endswith('.portal') and 'vyhlasene_znenie' not in u)
    n_acts = sum(1 for u in urls if u.endswith('vyhlasene_znenie.portal'))
    n_law = sum(1 for c in log if c['kind'] == 'law')
    n_empty = sum(1 for c in log if c['kind'] == 'law' and not c['units'])
    n_cand = sum(1 for c in log if c['kind'] == 'candidates')
    n_unexp = sum(1 for c in log if c['kind'] == 'unexplained')
    n_start = sum(1 for c in log if c['kind'] == 'start')
    n_clamped = sum(1 for c in log if c['clamped'])
    why: dict[str, int] = {}
    listed: dict[str, list[str]] = {}
    for b in built:
        for ch in b['changes']:
            for k, w in ch['why'].items():
                w2 = 'headings moved' if w.startswith('headings moved') else w
                why[w2] = why.get(w2, 0) + 1
                if w2 != 'mark' and w2 != 'commencement clause of the act itself':
                    lab = (ch['cur']['units'].get(k) or ch['prev']['units'][k])['label']
                    listed.setdefault(w2, []).append(f'{b["act"]["short"]} {ch["from"]}: {lab}')
    n_changes = sum(why.values())
    rows = '\n'.join(
        f'| {b["label"]} | {b["title"]} | `{b["act"]["slug"]}/` | {len(b["versions"])} | '
        f'{b["versions"][0]["from"]} to {b["versions"][-1]["from"]} | {len(b["versions"][-1]["units"])} |' for b in built)
    retrieved = ', '.join(days) if days else today
    chk = ver.get('check', {})
    det = ver.get('rebuild', {})
    smoke = ver.get('smoke', {})
    check_line = (f'`{chk["versions"]} versions checked ({chk["files"]} files), {chk["mismatches"]} mismatches; '
                  f'{chk["wordcheck"]} versions word for word ({chk["words"]} words) against the whole official text, '
                  f'{chk["word_mismatches"]} mismatches`' if chk else '(not yet run)')
    rebuild_line = (f'A second build from the same cache into an empty folder gave the same history: the last law commit '
                    f'was `{det["history_tip"]}` in both, and every one of the {det["commits"]} law commits and {det["tags"]} '
                    f'tags had the same hash.' if det.get('identical') else '(not yet run)')
    smoke_lines = ('\n'.join(f'   - {"pass" if r["ok"] else "FAIL"}: {r["test"]}: {r["detail"]}' for r in smoke['results'])
                   if smoke else '   (not yet run)')
    smoke_head = f'{smoke["passed"]} of {smoke["total"]} passed' if smoke else 'not yet run'

    def items(w):
        return '\n'.join(f'- {x}' for x in listed.get(w, [])) or '- none'

    text = f"""# How this history was made, and how to make it again

This file records exactly how the repository was built: the sources, the commands, the software, the decisions made
by hand, and what an AI model did and did not do. The build writes it, so it describes the build that made this
commit.

## Short version

```sh
git clone https://github.com/lexifina/slovakia-law && cd slovakia-law
pip install lxml
python -X utf8 tools/build.py --repo ../rebuilt --today {today}
git -C ../rebuilt rev-parse main        # the same hash as this repository's main
python -X utf8 tools/check_repo.py --repo ../rebuilt
python -X utf8 tools/test_repo.py --repo ../rebuilt
```

`tools/build.py` needs Python 3.12 or later with `lxml`, and git. It reads Slov-Lex (or its own cache, `.cache/` next
to the script) and writes this repository into `--repo`. With the same Slov-Lex data and the same `--today` it gives
the same commits with the same hashes. `data/verzie.json` lists every version page it read with the sha256 of the
HTML, so a rebuild can show it read the same bytes; Slov-Lex may change its pages, and then the hashes change too.

## Sources

All legal text and all information about versions and amending acts come from **Slov-Lex** (www.slov-lex.sk), the
legal information system of the Ministry of Justice of the Slovak Republic, through its static mirror
(static.slov-lex.sk). Nothing was typed in, summarised or rewritten. The build read {n_lists} version lists,
{n_versions} versions and the published text of {n_acts} acts:

| What | Where |
| --- | --- |
| Each act's dated versions ("časové verzie"), with the days each applies from and to, and the acts Slov-Lex names for each version ("Novela") | `https://static.slov-lex.sk/static/SK/ZZ/<year>/<number>/` |
| The text of each version, with Slov-Lex's mark (class `modified`) on each element the version changed | `https://static.slov-lex.sk/static/SK/ZZ/<year>/<number>/<yyyymmdd>.portal`, listed with sha256 in `data/verzie.json` |
| Each amending act's title, kind, issuer, and the days it was passed and published | `https://static.slov-lex.sk/static/SK/ZZ/<year>/<number>/vyhlasene_znenie.portal`, its information table |

| Act | Title | Folder | Versions | In force from | Files today |
| --- | --- | --- | ---: | --- | ---: |
{rows}

The data was retrieved on {retrieved}, at most four requests at a time and a request started at most every 0.5
seconds, with the user agent `lexifina-watch/1.0 (+https://lexifina.com/watch; corpus@lexifina.com)`. The static mirror
has no robots.txt (the address answers 404) and needs no login. The `.portal` address of a version is the page's
content without the site's frame; it was found in the Slovak fetcher of legalize-dev (below).

## The build, step by step

1. `python -X utf8 scripts/slovakia-law/build.py --today {today}` in Lexifina's own repository fetched the data into
   its cache and wrote this repository. `tools/build.py` here is the same file as `scripts/slovakia-law/build.py`
   there (git blob `{blob}`), with `tools/reproduce.py`, which writes this file, `tools/check_repo.py` and
   `tools/test_repo.py`. Every later build ran with `--offline`, from the cache.
2. `python -X utf8 scripts/slovakia-law/check_repo.py` read every version of each act back from this repository with
   `tools/ku_dnu.py`, on the day it took effect, and compared it file by file with the official text parsed afresh
   from the cached HTML; then it compared the whole act, word for word, with all the words of the official page (the
   act, its annexes and its footnotes), read without the build's parser. Result: {check_line}.
3. `python -X utf8 scripts/slovakia-law/test_repo.py --record` ran the functional smoke test against this repository
   ({smoke_head}):
{smoke_lines}
4. `python -X utf8 scripts/slovakia-law/build.py --offline --verify-rebuild` built the repository a second time from
   the same cache into a temporary folder and compared the hashes. {rebuild_line}
5. The build was run once more to write these results into this file, and the final `main` was rebuilt again in a
   temporary folder and compared hash for hash before it was pushed.
6. `git push -f origin main --tags` published it to the private GitHub repository `lexifina/slovakia-law`.

It ran with {pyv}, lxml {lxmlv} and {gitv} on Windows 11. No network service other than Slov-Lex is involved.

## How the text and the commits are derived

Everything below is done by `tools/build.py`, deterministically.

- **Text.** Each act is a folder. Each article or section is one file named after Slov-Lex's element identifier:
  `ustavnyclanok-7` is `ustava/cl-007.md`, `paragraf-14a` is `volebny-zakon/par-014a.md`, and an article of an act
  that holds no sections (Čl. II to Čl. VI of Act 180/2014, which amend other acts or set its commencement) is
  `clanok-2.md`. The headings of the parts (hlava, časť, oddiel, the groups of sections and Čl. I) that begin with a
  provision are `##` lines at the top of its file; the provision's designation and heading are the `#` line; each
  paragraph (odsek) is one line beginning with its number, and each letter (písmeno) and point (bod) is a list item,
  one level deeper for each level of nesting. Quoted text, line breaks and blocks inside a paragraph start new lines.
  Tables are one line per row, cells separated by ` | `. `uvod.md` holds the number, title, date and preamble or
  enacting words; `zaver.md` the signatures; `prilohy/priloha-<n>.md` each annex; `poznamky.md` the footnotes, one
  line each.
- **Normalised.** Only white space: runs of spaces, line breaks inside a line of the HTML, tabs and no-break spaces
  become one space. Every other character is kept, including footnote numbers ("predpisu,1)").
- **Changes.** Consecutive versions are compared file by file. {n_changes} changes of a file were found.
- **Cause.** Slov-Lex names the act or acts behind each version, and its HTML marks each element that the version
  changed with the class `modified`. Tried in this order:
  1. the file holds an element Slov-Lex marks as changed, and the version has one act: that act
     ({why.get('mark', 0)} file changes);
  2. the version names no act, and the act's own commencement provision names that day ("Tento zákon nadobúda účinnosť
     1. júla 2014 okrem čl. I a II, ktoré nadobúdajú účinnosť 1. júla 2015, a čl. V, ktorý nadobúda účinnosť
     1. januára 2016."): the act itself, quoting that provision in the commit
     ({why.get('commencement clause of the act itself', 0)});
  3. the change only removes text, which leaves nothing to mark, and the version has one act: that act, by date only
     ({why.get('date-only removal', 0)});
  4. a whole new provision with no mark, and the version has one act: that act, by date only
     ({why.get('date-only insertion', 0)});
  5. part headings that only moved to or from a provision an act of the same version changed: that act
     ({why.get('headings moved', 0)});
  6. a marked, removed or new provision in a version with two acts: neither; committed by the publisher naming both
     ({why.get('two acts took effect that day', 0)});
  7. otherwise: no act; committed by the publisher and labelled
     ({why.get('Slov-Lex marks no element of it as changed', 0) + why.get('Slov-Lex names no amending act for this version', 0)}).
- **Date.** The day the version applies from in Slov-Lex (`data-ucinnostod`), which for the version an act produced
  is the day the act took effect.
- **Commits.** One commit per act of the record, per day and per amending act ({n_law} law commits, of which
  {n_empty} change no words of that act), one for the first version of each act ({n_start}), {n_cand} for changes
  where two acts took effect the same day, and {n_unexp} for changes nothing explains, in the order they took effect,
  then one for this documentation.
  - The author is the amending act, `255/2025 Z. z.` (`460/1992 Zb.` before 1993), at an address ending
    `@slov-lex.invalid` (`zz-2025-255@slov-lex.invalid`). Findings of the Constitutional Court (nálezy) published in
    the Collection are authors in the same way. The first version of each act is credited to the act itself: Slov-Lex
    names no amending act for it.
  - Changes with two candidate acts are by `Slov-Lex (Ministerstvo spravodlivosti SR)`, say "dva predpisy v jeden deň"
    in the subject and name both acts in `Candidate:` trailers.
  - Author and committer dates are noon in Bratislava on the day the change took effect: UTC+1, or UTC+2 in summer
    time (from the last Sunday in March to the last Sunday in October; September until 1995), written into the code
    because the build machine has no time-zone database. The committer is `Lexifina <slovakia-law@lexifina.com>`.
    {n_clamped} commits are before 1970 (git cannot store such dates; they would be dated 1970-01-01, seconds apart,
    with the real day in `In-force:`, which `tools/ku_dnu.py` reads).
  - The message has the act's full title, the provisions it inserted, amended or removed (Vložené, Zmenené, Vypustené),
    and the trailers `Evidence:`, `Kind:`, `Issuer:`, `Enacted:` (passed by the National Council), `Published:` (in the
    Collection, with its issue, čiastka), `In-force:`, `Affecting:`, `Source:` (the act on Slov-Lex) and
    `Consolidated:` (the exact version page the text came from).
  - Tags: each act's days (`ustava/2025-11-01`) and each amending act (`zz/2025-255`; an act that took effect on
    several days has one tag per day, `zz/2020-422/2021-01-01`); {len(tags)} in all.
- **Documentation commit.** Dated {today}, the day the data was retrieved, not the day of the run, so a later rebuild
  of the same data gives the same hash.

Changes credited by date only (removal):

{items('date-only removal')}

Changes credited by date only (insertion):

{items('date-only insertion')}

Headings moved with a provision:

{items('headings moved')}

Changes with two candidate acts (credited to neither):

{items('two acts took effect that day')}

Changes nothing explains:

{items('Slov-Lex marks no element of it as changed')}

## Decisions made by hand

These choices were made when the tool was written, after looking at the data. They are in the code.

1. **The acts.** The Constitution (460/1992 Zb.), the act readers ask about first, with all 28 dated versions since
   1 October 1992; and Act 180/2014 Z. z. on the conditions for exercising the right to vote, because it is amended
   often (some twenty acts, including Constitutional Court findings), is deeply structured (parts, sections,
   paragraphs, letters, points, annexes, footnotes), and exercises every rule above: a deferred commencement, two acts
   on one day, removals and insertions without a mark.
2. **Slov-Lex's mark is the evidence.** Slov-Lex's consolidated text has no notes naming the amending act of each
   provision; it lists the acts per version and marks the changed elements. A change is credited to an act only on
   that evidence, or by date only where text was removed or a provision inserted (labelled in each commit).
3. **Two acts on one day are not separated.** Where a version names two acts (Constitution 2023-01-01: 422/2020 Z. z.
   and 378/2022 Z. z.; Act 180/2014 2017-05-31: two Constitutional Court findings, 130/2017 and 131/2017 Z. z.;
   2019-01-01: 344/2018 and 177/2018 Z. z.), the amending acts' own texts were not parsed to divide the changes. The
   changes are committed by the publisher, naming both. Their law commits are empty, so each act still has a commit
   and a tag on that day.
4. **The act's own commencement.** Slov-Lex shows only the parts of an act in force: Act 180/2014's sections (Čl. I)
   appear on 1 July 2015 and its Čl. V on 1 January 2016, versions for which Slov-Lex names no amending act. The act's
   own Čl. VI names those days; the build checks that it does and quotes it.
5. **Slov-Lex's version days are the in-force days.** The acts' own commencement clauses were not parsed otherwise.
6. **The record starts with the first dated version.** Slov-Lex also publishes each act as published
   ("vyhlásené znenie"); the record starts with the first version in force, which Slov-Lex credits to no amendment.
7. **Slovak only**, the official language.

## What an AI model did

This repository was built on {today} in **Claude Code**, Anthropic's coding tool, by the model **Claude Opus 5.5**
(model id `claude-opus-5-5`), working from a brief by the user at Lexifina: a private "git for law" repository for
Slovakia to the same standard as Lexifina's other corpora.

The model:

- **Researched the source:** Slov-Lex's static mirror, the shape of its HTML and its change marks, its notice, the
  Copyright Act, and the Slovak fetcher of legalize-dev (below).
- **Wrote all the code and text in this repository:** `tools/build.py`, `tools/reproduce.py`, `tools/check_repo.py`,
  `tools/test_repo.py`, `tools/ku_dnu.py`, the README, this file and the licence, and chose the design described in
  them.
- **Ran the commands above** and checked the results.

The model did **not**:

- **Write or edit any legal text.** Every word of every provision, every date and every act's title is copied by the
  script from Slov-Lex.
- **Take part in building the history.** No AI model is called when the history is built or checked.

The user decided what was in scope and decides whether the repository is ever made public. The work was not reviewed
line by line by a lawyer. Slov-Lex itself says that the content shown is for information and that the legally binding
content is the PDF version of the Collection of Laws.

## Prior art

- [legalize-dev/legalize-pipeline](https://github.com/legalize-dev/legalize-pipeline), `src/legalize/fetcher/sk/`:
  a Slov-Lex fetcher. From it we took one fact about the site, checked against it: that each version's text is served
  without the page frame at `<yyyymmdd>.portal`. No code was copied.
- [legalize-dev/legalize-sk](https://github.com/legalize-dev/legalize-sk): Slovak acts in Markdown, one commit per
  version ("každá novela je commit"). This repository instead credits each change to the act Slov-Lex marks for it,
  one file per provision, and keeps changes it cannot attribute apart.
- Lexifina's other corpora, whose rules this one follows (Estonia, Liechtenstein, Luxembourg, Swiss federal law, the
  Grundgesetz, UK legislation and the US Code).
"""
    (repo / 'REPRODUCE.md').write_text(text, encoding='utf-8', newline='\n')
