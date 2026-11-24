<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Monitoring: what is read and what came of it

[Slovenčina](README.md)

How global-law monitors every country: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). This page is the same for Slovakia only: every time an official source is read, when, and what came of it (acts added, changed and removed). The machine-readable form is [data/checks/](../data/checks/) (JSON Lines, schema `lexifina-check/1`), in `git log` as `Kind: check` commits, and month by month in [checks/](checks/).

**Last check:** 2026-11-24 15:15 UTC, Banská Bystrica: register of generally binding regulations (VZN): 17 addresses read; 0 added, 0 changed, 0 removed; the check failed; 152 not published, 0 of them with no reason. Flags: `publish-lag`.

## Sources

| Source | Folders | How often | Last successful check | Last result | State |
| --- | --- | --- | --- | --- | --- |
| [Slov-Lex: Collection of Laws (Zbierka zákonov)](https://www.slov-lex.sk/ezbierky/pravne-predpisy) | `zz/`, `zb/`, `constitution/ustava/`, `volebny-zakon/` | daily | 2026-11-23 16:36 UTC | the check failed | watched: Slov-Lex has no open-data feed, RSS or ELI list; this is the list behind its own search |
| [Slov-Lex: Register of measures (Register opatrení)](https://www.slov-lex.sk/ezbierky/chronologicky-register-opatreni) | `ro/` | daily | 2026-11-24 05:51 UTC | no change | watched |
| [Bratislava: register of generally binding regulations (VZN)](https://bratislava.sk/vzn) | `local/bratislava/` | daily | 2026-11-24 05:52 UTC | changes found | watched |
| [Žilina: register of generally binding regulations (VZN)](https://zilina.sk/mesto-zilina/sprava-mesta/legislativa/vseobecne-zavazne-nariadenia/) | `local/zilina/` | daily | 2026-11-24 05:55 UTC | changes found | watched |
| [Banská Bystrica: register of generally binding regulations (VZN)](https://www.banskabystrica.sk/vzn/) | `local/banskabystrica/` | daily | 2026-11-23 17:18 UTC | the check failed | watched |
| [Nitra: register of generally binding regulations (VZN)](https://nitra.sk/vzn/) | `local/nitra/` | daily | 2026-11-24 05:57 UTC | no change | watched: the list gives no validity days (the city puts them on each record's page): only changed and new records are seen |

## The last 30 days

| Started (UTC) | Source | Read | Added | Changed | Removed | Not published (no reason) | Result | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-24 15:15](checks/2026-11.md#sk-banskabystrica-vzn-20261124t151540z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | the check failed `publish-lag` | — |
| [2026-11-24 15:08](checks/2026-11.md#sk-slov-lex-zz-20261124t150840z) | slov-lex-zz | 383 | 0 | 0 | 0 | 97 (0) | the check failed | — |
| [2026-11-24 14:25](checks/2026-11.md#sk-banskabystrica-vzn-20261124t142554z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | the check failed `publish-lag` | — |
| [2026-11-24 14:18](checks/2026-11.md#sk-slov-lex-zz-20261124t141849z) | slov-lex-zz | 383 | 0 | 0 | 0 | 97 (0) | the check failed | — |
| [2026-11-24 13:13](checks/2026-11.md#sk-banskabystrica-vzn-20261124t131349z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | the check failed `publish-lag` | — |
| [2026-11-24 13:06](checks/2026-11.md#sk-slov-lex-zz-20261124t130653z) | slov-lex-zz | 383 | 0 | 0 | 0 | 97 (0) | the check failed | — |
| [2026-11-24 12:46](checks/2026-11.md#sk-banskabystrica-vzn-20261124t124602z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | the check failed `publish-lag` | — |
| [2026-11-24 12:39](checks/2026-11.md#sk-slov-lex-zz-20261124t123906z) | slov-lex-zz | 383 | 0 | 0 | 0 | 97 (0) | the check failed | — |
| [2026-11-24 11:20](checks/2026-11.md#sk-banskabystrica-vzn-20261124t112019z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | the check failed `publish-lag` | — |
| [2026-11-24 11:12](checks/2026-11.md#sk-slov-lex-zz-20261124t111253z) | slov-lex-zz | 383 | 0 | 0 | 0 | 97 (0) | the check failed | — |
| [2026-11-24 10:16](checks/2026-11.md#sk-banskabystrica-vzn-20261124t101616z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | the check failed `publish-lag` | — |
| [2026-11-24 10:09](checks/2026-11.md#sk-slov-lex-zz-20261124t100920z) | slov-lex-zz | 383 | 0 | 0 | 0 | 97 (0) | the check failed | — |
| [2026-11-24 09:14](checks/2026-11.md#sk-banskabystrica-vzn-20261124t091456z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | the check failed `publish-lag` | — |
| [2026-11-24 09:08](checks/2026-11.md#sk-slov-lex-zz-20261124t090803z) | slov-lex-zz | 383 | 0 | 0 | 0 | 97 (0) | the check failed | — |
| [2026-11-24 08:14](checks/2026-11.md#sk-banskabystrica-vzn-20261124t081457z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | the check failed `publish-lag` | — |
| [2026-11-24 08:08](checks/2026-11.md#sk-slov-lex-zz-20261124t080803z) | slov-lex-zz | 383 | 0 | 0 | 0 | 97 (0) | the check failed | — |
| [2026-11-24 05:55](checks/2026-11.md#sk-nitra-vzn-20261124t055540z) | nitra-vzn | 129 | 0 | 0 | 0 | 3 (0) | no change | — |
| [2026-11-24 05:55](checks/2026-11.md#sk-banskabystrica-vzn-20261124t055524z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | the check failed `publish-lag` | — |
| [2026-11-24 05:52](checks/2026-11.md#sk-zilina-vzn-20261124t055255z) | zilina-vzn | 91 | 0 | 0 | 0 | 165 (0) | changes found `publish-lag` | [32](https://github.com/lexifina/slovakia-law/compare/b69b09f44513...0364327612ef) |
| [2026-11-24 05:51](checks/2026-11.md#sk-bratislava-vzn-20261124t055102z) | bratislava-vzn | 40 | 0 | 0 | 0 | 62 (0) | changes found `publish-lag` | [20](https://github.com/lexifina/slovakia-law/compare/9b90557ab86e...b69b09f44513) |
| [2026-11-24 05:48](checks/2026-11.md#sk-slov-lex-op-20261124t054836z) | slov-lex-op | 141 | 0 | 0 | 0 | 3 (0) | no change `verify-differ` `audit-disagrees` | — |
| [2026-11-24 05:41](checks/2026-11.md#sk-slov-lex-zz-20261124t054134z) | slov-lex-zz | 383 | 0 | 0 | 0 | 97 (0) | the check failed | — |
| [2026-11-23 17:18](checks/2026-11.md#sk-nitra-vzn-20261123t171837z) | nitra-vzn | 201 | 0 | 0 | 0 | 3 (0) | changes found | [73](https://github.com/lexifina/slovakia-law/compare/e9a12fa57b2b...f41c2c81fb26) |
| [2026-11-23 17:17](checks/2026-11.md#sk-banskabystrica-vzn-20261123t171714z) | banskabystrica-vzn | 46 | 0 | 0 | 0 | 152 (0) | changes found `publish-lag` | [6](https://github.com/lexifina/slovakia-law/compare/f580410761d2...e9a12fa57b2b) |
| [2026-11-23 17:10](checks/2026-11.md#sk-zilina-vzn-20261123t171014z) | zilina-vzn | 372 | 0 | 0 | 0 | 190 (0) | changes found `publish-lag` | [177](https://github.com/lexifina/slovakia-law/compare/df51033789c7...f580410761d2) |
| [2026-11-23 17:07](checks/2026-11.md#sk-bratislava-vzn-20261123t170746z) | bratislava-vzn | 77 | 0 | 0 | 0 | 77 (0) | changes found `publish-lag` | [67](https://github.com/lexifina/slovakia-law/compare/d2fbd4cab2ea...df51033789c7) |
| [2026-11-23 16:47](checks/2026-11.md#sk-slov-lex-op-20261123t164752z) | slov-lex-op | 1105 | 0 | 0 | 0 | 3 (0) | changes found `audit-disagrees` | [294](https://github.com/lexifina/slovakia-law/compare/f104dadfe366...d2fbd4cab2ea) |
| [2026-11-23 16:35](checks/2026-11.md#sk-slov-lex-zz-20261123t163552z) | slov-lex-zz | 687 | 0 | 1 | 0 | 97 (0) | changes found | — |
| [2026-11-23 01:09](checks/2026-11.md#sk-nitra-vzn-20261123t010929z) | nitra-vzn | 2 | 0 | 0 | 0 | 76 (0) | no change `publish-lag` | — |
| [2026-11-23 01:09](checks/2026-11.md#sk-banskabystrica-vzn-20261123t010925z) | banskabystrica-vzn | 3 | 0 | 0 | 0 | 158 (0) | no change `publish-lag` | — |
| [2026-11-23 01:09](checks/2026-11.md#sk-zilina-vzn-20261123t010918z) | zilina-vzn | 6 | 0 | 0 | 0 | 365 (0) | no change `publish-lag` | — |
| [2026-11-23 01:09](checks/2026-11.md#sk-bratislava-vzn-20261123t010914z) | bratislava-vzn | 4 | 0 | 0 | 0 | 139 (0) | no change `publish-lag` | — |
| [2026-11-23 01:09](checks/2026-11.md#sk-slov-lex-op-20261123t010912z) | slov-lex-op | 1 | 0 | 0 | 0 | 266 (0) | no change `publish-lag` | — |
| [2026-11-23 01:08](checks/2026-11.md#sk-slov-lex-zz-20261123t010838z) | slov-lex-zz | 27 | 0 | 0 | 0 | 176 (0) | no change `publish-lag` | — |

## Check it yourself

```
python tools/checktrail.py                      # the latest check of every source
python tools/checktrail.py --day 2026-11-23     # every check of a day
python tools/checktrail.py --act <id>           # when an act was seen and published
git log --grep='^Kind: check' --format='%ci %s'  # the checks in the history
```

Only the official publication has legal force; the texts here are copies for reading and searching.
