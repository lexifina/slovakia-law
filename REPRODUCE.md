# How this history was made, and how to make it again

This file records exactly how the repository was built: the sources, the commands, the software, the decisions made
by hand, and what an AI model did and did not do. The build writes it, so it describes the build that made this
commit.

## Short version

```sh
git clone https://github.com/lexifina/slovakia-law && cd slovakia-law
pip install lxml
python -X utf8 tools/build.py --repo ../rebuilt --today 2026-10-28
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
(static.slov-lex.sk). Nothing was typed in, summarised or rewritten. The build read 2 version lists,
49 versions and the published text of 45 acts:

| What | Where |
| --- | --- |
| Each act's dated versions ("časové verzie"), with the days each applies from and to, and the acts Slov-Lex names for each version ("Novela") | `https://static.slov-lex.sk/static/SK/ZZ/<year>/<number>/` |
| The text of each version, with Slov-Lex's mark (class `modified`) on each element the version changed | `https://static.slov-lex.sk/static/SK/ZZ/<year>/<number>/<yyyymmdd>.portal`, listed with sha256 in `data/verzie.json` |
| Each amending act's title, kind, issuer, and the days it was passed and published | `https://static.slov-lex.sk/static/SK/ZZ/<year>/<number>/vyhlasene_znenie.portal`, its information table |

| Act | Title | Folder | Versions | In force from | Files today |
| --- | --- | --- | ---: | --- | ---: |
| 460/1992 Zb. | Ústava Slovenskej republiky | `ustava/` | 28 | 1992-10-01 to 2025-11-01 | 179 |
| 180/2014 Z. z. | Zákon o podmienkach výkonu volebného práva a o zmene a doplnení niektorých zákonov | `volebny-zakon/` | 21 | 2014-07-01 to 2026-06-01 | 239 |

The data was retrieved on 2026-10-28, at most four requests at a time and a request started at most every 0.5
seconds, with the user agent `lexifina-watch/1.0 (+https://lexifina.com/watch; corpus@lexifina.com)`. The static mirror
has no robots.txt (the address answers 404) and needs no login. The `.portal` address of a version is the page's
content without the site's frame; it was found in the Slovak fetcher of legalize-dev (below).

## The build, step by step

1. `python -X utf8 scripts/slovakia-law/build.py --today 2026-10-28` in Lexifina's own repository fetched the data into
   its cache and wrote this repository. `tools/build.py` here is the same file as `scripts/slovakia-law/build.py`
   there (git blob `262b57ba9c4c33124017d116db45cc63028a1a0a`), with `tools/reproduce.py`, which writes this file, `tools/check_repo.py` and
   `tools/test_repo.py`. Every later build ran with `--offline`, from the cache.
2. `python -X utf8 scripts/slovakia-law/check_repo.py` read every version of each act back from this repository with
   `tools/ku_dnu.py`, on the day it took effect, and compared it file by file with the official text parsed afresh
   from the cached HTML; then it compared the whole act, word for word, with all the words of the official page (the
   act, its annexes and its footnotes), read without the build's parser. Result: `49 versions checked (9202 files), 0 mismatches; 49 versions word for word (1378404 words) against the whole official text, 0 mismatches`.
3. `python -X utf8 scripts/slovakia-law/test_repo.py --record` ran the functional smoke test against this repository
   (6 of 6 passed):
   - pass: blame names an act: ustava/cl-007.md lines by 255/2025 Z. z., 460/1992 Zb., 90/2001 Z. z.
   - pass: text before and after an amendment: ustava/cl-007.md 2025-10-31 != 2025-11-01; volebny-zakon/par-004.md 2017-05-30 != 2017-05-31
   - pass: log --follow in date order: ustava/cl-007.md 3 commits; volebny-zakon/par-004.md 3 commits; volebny-zakon/par-050.md 5 commits
   - pass: tags resolve, In-force on every law commit: 101 tags resolve; 55 law commits carry In-force
   - pass: only the documentation commit is by Lexifina: only the documentation commit 12e1f192b3 is by Lexifina; 46 distinct authors
   - pass: README commands run: 11 README commands ran and printed output
4. `python -X utf8 scripts/slovakia-law/build.py --offline --verify-rebuild` built the repository a second time from
   the same cache into a temporary folder and compared the hashes. A second build from the same cache into an empty folder gave the same history: the last law commit was `fac61a2ca5217b49e0faa8b3c6b6ef1bbb1e0f4a` in both, and every one of the 55 law commits and 101 tags had the same hash.
5. The build was run once more to write these results into this file, and the final `main` was rebuilt again in a
   temporary folder and compared hash for hash before it was pushed.
6. `git push -f origin main --tags` published it to the private GitHub repository `lexifina/slovakia-law`.

It ran with Python 3.12.10, lxml 6.1.3 and git version 2.46.0.windows.1 on Windows 11. No network service other than Slov-Lex is involved.

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
- **Changes.** Consecutive versions are compared file by file. 676 changes of a file were found.
- **Cause.** Slov-Lex names the act or acts behind each version, and its HTML marks each element that the version
  changed with the class `modified`. Tried in this order:
  1. the file holds an element Slov-Lex marks as changed, and the version has one act: that act
     (403 file changes);
  2. the version names no act, and the act's own commencement provision names that day ("Tento zákon nadobúda účinnosť
     1. júla 2014 okrem čl. I a II, ktoré nadobúdajú účinnosť 1. júla 2015, a čl. V, ktorý nadobúda účinnosť
     1. januára 2016."): the act itself, quoting that provision in the commit
     (224);
  3. the change only removes text, which leaves nothing to mark, and the version has one act: that act, by date only
     (17);
  4. a whole new provision with no mark, and the version has one act: that act, by date only
     (3);
  5. part headings that only moved to or from a provision an act of the same version changed: that act
     (1);
  6. a marked, removed or new provision in a version with two acts: neither; committed by the publisher naming both
     (28);
  7. otherwise: no act; committed by the publisher and labelled
     (0).
- **Date.** The day the version applies from in Slov-Lex (`data-ucinnostod`), which for the version an act produced
  is the day the act took effect.
- **Commits.** One commit per act of the record, per day and per amending act (50 law commits, of which
  6 change no words of that act), one for the first version of each act (2), 3 for changes
  where two acts took effect the same day, and 0 for changes nothing explains, in the order they took effect,
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
    0 commits are before 1970 (git cannot store such dates; they would be dated 1970-01-01, seconds apart,
    with the real day in `In-force:`, which `tools/ku_dnu.py` reads).
  - The message has the act's full title, the provisions it inserted, amended or removed (Vložené, Zmenené, Vypustené),
    and the trailers `Evidence:`, `Kind:`, `Issuer:`, `Enacted:` (passed by the National Council), `Published:` (in the
    Collection, with its issue, čiastka), `In-force:`, `Affecting:`, `Source:` (the act on Slov-Lex) and
    `Consolidated:` (the exact version page the text came from).
  - Tags: each act's days (`ustava/2025-11-01`) and each amending act (`zz/2025-255`; an act that took effect on
    several days has one tag per day, `zz/2020-422/2021-01-01`); 101 in all.
- **Documentation commit.** Dated 2026-10-28, the day the data was retrieved, not the day of the run, so a later rebuild
  of the same data gives the same hash.

Changes credited by date only (removal):

- Ústava 2001-07-01: Čl. 11
- Ústava 2001-07-01: Čl. 127
- Ústava 2001-07-01: Čl. 132
- Ústava 2019-02-23: Čl. 154d
- Zákon 180/2014 2014-09-17: Čl. III
- Zákon 180/2014 2014-09-17: Čl. IV
- Zákon 180/2014 2017-03-31: § 162
- Zákon 180/2014 2023-03-01: § 11
- Zákon 180/2014 2023-03-01: § 45
- Zákon 180/2014 2023-03-01: § 46
- Zákon 180/2014 2023-03-01: § 76
- Zákon 180/2014 2023-03-01: § 99
- Zákon 180/2014 2023-03-01: § 117
- Zákon 180/2014 2023-03-01: § 197
- Zákon 180/2014 2023-03-01: § 198
- Zákon 180/2014 2024-06-01: § 172
- Zákon 180/2014 2024-06-01: § 177

Changes credited by date only (insertion):

- Zákon 180/2014 2021-01-01: § 195b
- Zákon 180/2014 2021-01-01: § 195c
- Zákon 180/2014 2021-01-01: § 195d

Headings moved with a provision:

- Ústava 2001-07-01: Čl. 12

Changes with two candidate acts (credited to neither):

- Ústava 2023-01-01: Čl. 39
- Ústava 2023-01-01: Čl. 151a
- Zákon 180/2014 2017-05-31: § 4
- Zákon 180/2014 2017-05-31: § 165
- Zákon 180/2014 2017-05-31: § 176
- Zákon 180/2014 2017-05-31: § 177
- Zákon 180/2014 2019-01-01: § 8
- Zákon 180/2014 2019-01-01: § 12
- Zákon 180/2014 2019-01-01: § 13
- Zákon 180/2014 2019-01-01: § 16
- Zákon 180/2014 2019-01-01: § 19
- Zákon 180/2014 2019-01-01: § 22
- Zákon 180/2014 2019-01-01: § 45
- Zákon 180/2014 2019-01-01: § 49
- Zákon 180/2014 2019-01-01: § 50
- Zákon 180/2014 2019-01-01: § 52
- Zákon 180/2014 2019-01-01: § 59
- Zákon 180/2014 2019-01-01: § 73
- Zákon 180/2014 2019-01-01: § 80
- Zákon 180/2014 2019-01-01: § 81
- Zákon 180/2014 2019-01-01: § 82
- Zákon 180/2014 2019-01-01: § 103
- Zákon 180/2014 2019-01-01: § 178
- Zákon 180/2014 2019-01-01: § 197
- Zákon 180/2014 2019-01-01: § 201
- Zákon 180/2014 2019-01-01: § 207
- Zákon 180/2014 2019-01-01: § 219b
- Zákon 180/2014 2019-01-01: Poznámky pod čiarou

Changes nothing explains:

- none

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

This repository was built on 2026-10-28 in **Claude Code**, Anthropic's coding tool, by the model **Claude Opus 5.5**
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
