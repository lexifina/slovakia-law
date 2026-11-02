# Slovak law, change by change

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Slovakia's national law, which global-law reads at `slovakia/national/acts/`.

Slovak law as a git repository. Two acts are traced version by version: the Constitution (Ústava Slovenskej
republiky, 460/1992 Zb.) and the Act on the Conditions for Exercising the Right to Vote (zákon č. 180/2014 Z. z. o
podmienkach výkonu volebného práva); 664 other acts in force, chosen as "The acts in force" below says, are
held as their current version. In the two traced acts each amending act is one commit, credited to that act and dated the day it took effect, at noon in Bratislava.
The text is the consolidated text published by the Ministry of Justice in [Slov-Lex](https://www.slov-lex.sk).

*Slovensky: [nižšie](#slovensky).*

## The questions, as git commands

| Question | Command |
| --- | --- |
| What did čl. 7 of the Constitution say on 1 January 2020? | `python tools/ku_dnu.py 2020-01-01 ustava 7` |
| The whole Constitution as it stood in 2000 | `python tools/ku_dnu.py 2000-01-01 ustava` |
| § 4 of the election act on 1 January 2017 | `python tools/ku_dnu.py 2017-01-01 volebny-zakon 4` |
| Which act wrote each paragraph of čl. 7? | `git blame ustava/cl-007.md` |
| Every change to čl. 7, with the act and the day | `git log --follow ustava/cl-007.md` |
| Everything one act changed | `git show --stat zz/2025-255` |
| What changed in the election act on one day | `git show --stat volebny-zakon/2022-01-01` |
| The amending acts with all their dates | [`predpisy.csv`](predpisy.csv) |
| Changes where two acts took effect the same day | `git log --grep="dva predpisy v jeden deň"` |
| Changes credited to the act's own deferred commencement | `git log --grep="Evidence: commencement"` |
| Changes credited by date only (no change mark) | `git log --grep="Evidence: date only"` |
| Acts amending the election act in 2022 | `git log --format="%an %s" --author="/2022 Z. z." -- volebny-zakon` |

## The dates, and which one we use

A Slovak act has the day the National Council passed it (`Enacted:`), the day it was published in the Collection of
Laws (`Published:`), and the day it took effect (`In-force:`). **Commits are dated the day the change took effect**, at
noon in Bratislava (CET, or CEST in summer time): that is the day that decides which text applies. It is the day
Slov-Lex gives as the start of the version the act produced. All three dates are in every commit message of the two
traced acts; the acts appended as their current version carry `In-force:` (with `In-force-basis:` and
`Text-as-of:`) but not `Enacted:` or `Published:`. No date in these two acts is before 1970.

## What "author" means

The author of a commit is the act that made the change: `255/2025 Z. z.` (with an address ending
`@slov-lex.invalid`, which cannot exist), so `git blame` names the act. Constitutional Court findings (nálezy) published
in the Collection are authors too. Slov-Lex lists, for each version, the acts that produced it, and marks each element
of the text that the version changed. A change is credited to the version's act when Slov-Lex marks an element of that
provision as changed. Three further rules, each labelled in the commit: text removed or a provision inserted without a
mark goes to the one act of that day ("date only"); part headings that moved with a provision go with the act that
changed it; and a version for which Slov-Lex names no act is credited to the act itself when its own commencement
provision names that day (Act 180/2014 took effect in three steps).

Where two acts took effect on the same day, Slov-Lex does not say which changed what: such changes are committed by
`Slov-Lex (Ministerstvo spravodlivosti SR)`, labelled "dva predpisy v jeden deň", and name both acts in `Candidate:`
trailers. They are never credited to either. The committer is always `Lexifina`.

## How it is checked

For the two traced acts, `tools/check_repo.py` (it needs `build.py`, kept with the build notes) reads every version of
each act back from git on the day it took effect and compares it with the
official text: file by file with the text parsed from Slov-Lex's page, and word for word with all the words of the page,
read independently of the parser. `tools/test_repo.py` checks that the commands above work. The results are in
[`REPRODUCE.md`](REPRODUCE.md).

## Files

Each act is a folder (`ustava/`, `volebny-zakon/`). Each article (článok) or section (paragraf) is one file named after
Slov-Lex's identifier: `ustava/cl-007.md` is `ustavnyclanok-7`, `volebny-zakon/par-014a.md` is `paragraf-14a`, and
`volebny-zakon/clanok-2.md` is Čl. II of Act 180/2014 (an article that amends another act). The headings of the parts
that begin with a provision are `##` lines at the top of its file; the provision's number and heading are the `#` line;
each paragraph (odsek) is one line, and each letter (písmeno) and point (bod) is a list item. `uvod.md` is the title and
preamble or enacting words, `zaver.md` the signatures, `prilohy/` the annexes and `poznamky.md` the footnotes. A
repealed provision is removed, as Slov-Lex removes it from the consolidated text.

## What it does not show

- Versions Slov-Lex does not publish: the Constitution's text is recorded from 1 October 1992, its first dated version.
- Which of two acts of the same day made a change (above).
- The earlier versions of the acts held as their current version, and the amending acts behind them (not yet traced).

The consolidated text is for information: Slov-Lex says that the legally binding content is the PDF version of the
Collection of Laws.

## How it is built

The two traced acts were written by a build script (`build.py`) kept with the build notes, not in this repository;
the acts appended after them by a second private script. Every step, the sources, the decisions made by hand and
what an AI model did are in [`REPRODUCE.md`](REPRODUCE.md). `tools/ku_dnu.py` reads any act on any day, in the
order the source gives its provisions; `tools/check_wave3.py` checks the appended acts.
[`corpus.json`](corpus.json) describes the corpus for tools that read several of Lexifina's law repositories.

## Licence

The text of a legal regulation is not a subject of copyright in Slovakia (§ 5 písm. b) of the Copyright Act,
185/2015 Z. z.). Source: Slov-Lex, www.slov-lex.sk, Ministerstvo spravodlivosti Slovenskej republiky. The history,
commit messages, tables and tools are released under [CC0 1.0](LICENSE).

---

## Slovensky

Slovenské právo ako repozitár git. Verziu po verzii sú zaznamenané dva predpisy, Ústava Slovenskej republiky
(460/1992 Zb.) a zákon č. 180/2014 Z. z. o podmienkach výkonu volebného práva; ďalších 664 účinných predpisov
(výber opisuje „Účinné predpisy, aktuálne znenie“) je v aktuálnom znení, všetko v konsolidovanom znení zo Slov-Lexu.

- **V dvoch predpisoch zaznamenaných verziu po verzii je každý commit jeden novelizujúci predpis**, zapísaný ako autor (`255/2025 Z. z.`), takže `git blame` ukazuje, ktorý
  predpis napísal ktorý odsek. Predpis určuje zoznam časových verzií v Slov-Lexe a jeho označenie zmenených prvkov.
- **Každý commit nesie deň účinnosti**, poludnie v Bratislave. Pri týchto dvoch predpisoch je v správe aj deň schválenia a deň vyhlásenia; pri ostatných `In-force-basis` a
  `Text-as-of`.
- **Každý článok a paragraf je súbor**, každý odsek riadok.
- **Zmeny dvoch predpisov v jeden deň sa nepripisujú nijakému z nich**; commit je od Slov-Lexu a uvádza oba predpisy.

Konsolidované znenie má informatívny charakter; právne záväzný obsah sa nachádza v pdf verzii Zbierky zákonov.

## Účinné predpisy, aktuálne znenie

Okrem Ústavy a zákona č. 180/2014 Z. z., zaznamenaných verziu po verzii, obsahuje záznam 2801 predpisov účinných podľa Slov-Lexu, každý v jednom commite: časová verzia účinná ku dňu získania údajov, datovaná dňom svojej účinnosti. Ak je to pôvodné znenie, je pripísaná predpisu samému; inak ju zapisuje Slov-Lex bez pripísania novele. Staršie verzie pribudnú za nimi bez prepisovania histórie. Zoznam: `data/ucinne-predpisy.csv`. Priečinok predpisu je `zz-<rok>-<číslo>` (od 1993) alebo `zb-<rok>-<číslo>`.

Besides the two acts traced version by version, the record holds 2801 acts in force at Slov-Lex, one commit each: the version in force when the data was read, dated by its own day of effect; credited to the act when it is the act as enacted (`Kind: law`), otherwise committed by Slov-Lex as a `Kind: baseline` and credited to no act. Earlier versions will be added behind them without rewriting history. Notices, decisions, rulings and acts that only amend others are left out.

Images and annexes Slov-Lex gives only as PDF are kept as published, byte for byte, in each act's `assets/` folder and linked where they stand (`data/assets.tsv` lists them); one that could not be kept is marked `[Image omitted: ...]` at its place (columns `obrazky`, `prilohy_pdf`, `vynechane` of the table). Check the record with `python -X utf8 tools/check_wave3.py`.
