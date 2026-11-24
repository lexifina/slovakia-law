<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Monitorovanie: čo sa číta a čo z toho vyplynulo

[English](README.en.md)

Ako global-law monitoruje všetky krajiny: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). Táto stránka robí to isté len pre Slovensko: každé čítanie oficiálneho zdroja, kedy prebehlo a čo z neho vyplynulo (pridané, zmenené a zrušené predpisy). Strojovo čitateľná podoba je v [data/checks/](../data/checks/) (JSON Lines, schéma `lexifina-check/1`), v `git log` ako commity `Kind: check` a po mesiacoch v [checks/](checks/).

**Posledná kontrola:** 2026-11-24 15:15 UTC, Banská Bystrica: register všeobecne záväzných nariadení (VZN): prečítané adresy: 17; pridané 0, zmenené 0, zrušené 0; kontrola zlyhala; nezverejnené 152, z toho bez dôvodu 0. Príznaky: `publish-lag`.

## Zdroje

| Zdroj | Priečinky | Ako často | Posledná úspešná kontrola | Posledný výsledok | Stav |
| --- | --- | --- | --- | --- | --- |
| [Slov-Lex: Zbierka zákonov](https://www.slov-lex.sk/ezbierky/pravne-predpisy) | `zz/`, `zb/`, `constitution/ustava/`, `volebny-zakon/` | denne | 2026-11-23 16:36 UTC | kontrola zlyhala | sledovaný: Slov-Lex nemá otvorené dáta, RSS ani zoznam ELI; toto je zoznam, z ktorého čerpá jeho vlastné vyhľadávanie |
| [Slov-Lex: Register opatrení](https://www.slov-lex.sk/ezbierky/chronologicky-register-opatreni) | `ro/` | denne | 2026-11-24 05:51 UTC | bez zmeny | sledovaný |
| [Bratislava: register všeobecne záväzných nariadení (VZN)](https://bratislava.sk/vzn) | `local/bratislava/` | denne | 2026-11-24 05:52 UTC | našli sa zmeny | sledovaný |
| [Žilina: register všeobecne záväzných nariadení (VZN)](https://zilina.sk/mesto-zilina/sprava-mesta/legislativa/vseobecne-zavazne-nariadenia/) | `local/zilina/` | denne | 2026-11-24 05:55 UTC | našli sa zmeny | sledovaný |
| [Banská Bystrica: register všeobecne záväzných nariadení (VZN)](https://www.banskabystrica.sk/vzn/) | `local/banskabystrica/` | denne | 2026-11-23 17:18 UTC | kontrola zlyhala | sledovaný |
| [Nitra: register všeobecne záväzných nariadení (VZN)](https://nitra.sk/vzn/) | `local/nitra/` | denne | 2026-11-24 05:57 UTC | bez zmeny | sledovaný: zoznam neuvádza dni platnosti (mesto ich uvádza na stránke každého záznamu): vidno len zmenené a nové záznamy |

## Posledných 30 dní

| Začiatok (UTC) | Zdroj | Prečítané | Pridané | Zmenené | Zrušené | Nezverejnené (bez dôvodu) | Výsledok | Commity |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-24 15:15](checks/2026-11.md#sk-banskabystrica-vzn-20261124t151540z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-24 15:08](checks/2026-11.md#sk-slov-lex-zz-20261124t150840z) | slov-lex-zz | 383 | 0 | 0 | 0 | 97 (0) | kontrola zlyhala | — |
| [2026-11-24 14:25](checks/2026-11.md#sk-banskabystrica-vzn-20261124t142554z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-24 14:18](checks/2026-11.md#sk-slov-lex-zz-20261124t141849z) | slov-lex-zz | 383 | 0 | 0 | 0 | 97 (0) | kontrola zlyhala | — |
| [2026-11-24 13:13](checks/2026-11.md#sk-banskabystrica-vzn-20261124t131349z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-24 13:06](checks/2026-11.md#sk-slov-lex-zz-20261124t130653z) | slov-lex-zz | 383 | 0 | 0 | 0 | 97 (0) | kontrola zlyhala | — |
| [2026-11-24 12:46](checks/2026-11.md#sk-banskabystrica-vzn-20261124t124602z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-24 12:39](checks/2026-11.md#sk-slov-lex-zz-20261124t123906z) | slov-lex-zz | 383 | 0 | 0 | 0 | 97 (0) | kontrola zlyhala | — |
| [2026-11-24 11:20](checks/2026-11.md#sk-banskabystrica-vzn-20261124t112019z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-24 11:12](checks/2026-11.md#sk-slov-lex-zz-20261124t111253z) | slov-lex-zz | 383 | 0 | 0 | 0 | 97 (0) | kontrola zlyhala | — |
| [2026-11-24 10:16](checks/2026-11.md#sk-banskabystrica-vzn-20261124t101616z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-24 10:09](checks/2026-11.md#sk-slov-lex-zz-20261124t100920z) | slov-lex-zz | 383 | 0 | 0 | 0 | 97 (0) | kontrola zlyhala | — |
| [2026-11-24 09:14](checks/2026-11.md#sk-banskabystrica-vzn-20261124t091456z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-24 09:08](checks/2026-11.md#sk-slov-lex-zz-20261124t090803z) | slov-lex-zz | 383 | 0 | 0 | 0 | 97 (0) | kontrola zlyhala | — |
| [2026-11-24 08:14](checks/2026-11.md#sk-banskabystrica-vzn-20261124t081457z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-24 08:08](checks/2026-11.md#sk-slov-lex-zz-20261124t080803z) | slov-lex-zz | 383 | 0 | 0 | 0 | 97 (0) | kontrola zlyhala | — |
| [2026-11-24 05:55](checks/2026-11.md#sk-nitra-vzn-20261124t055540z) | nitra-vzn | 129 | 0 | 0 | 0 | 3 (0) | bez zmeny | — |
| [2026-11-24 05:55](checks/2026-11.md#sk-banskabystrica-vzn-20261124t055524z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-24 05:52](checks/2026-11.md#sk-zilina-vzn-20261124t055255z) | zilina-vzn | 91 | 0 | 0 | 0 | 165 (0) | našli sa zmeny `publish-lag` | [32](https://github.com/lexifina/slovakia-law/compare/b69b09f44513...0364327612ef) |
| [2026-11-24 05:51](checks/2026-11.md#sk-bratislava-vzn-20261124t055102z) | bratislava-vzn | 40 | 0 | 0 | 0 | 62 (0) | našli sa zmeny `publish-lag` | [20](https://github.com/lexifina/slovakia-law/compare/9b90557ab86e...b69b09f44513) |
| [2026-11-24 05:48](checks/2026-11.md#sk-slov-lex-op-20261124t054836z) | slov-lex-op | 141 | 0 | 0 | 0 | 3 (0) | bez zmeny `verify-differ` `audit-disagrees` | — |
| [2026-11-24 05:41](checks/2026-11.md#sk-slov-lex-zz-20261124t054134z) | slov-lex-zz | 383 | 0 | 0 | 0 | 97 (0) | kontrola zlyhala | — |
| [2026-11-23 17:18](checks/2026-11.md#sk-nitra-vzn-20261123t171837z) | nitra-vzn | 201 | 0 | 0 | 0 | 3 (0) | našli sa zmeny | [73](https://github.com/lexifina/slovakia-law/compare/e9a12fa57b2b...f41c2c81fb26) |
| [2026-11-23 17:17](checks/2026-11.md#sk-banskabystrica-vzn-20261123t171714z) | banskabystrica-vzn | 46 | 0 | 0 | 0 | 152 (0) | našli sa zmeny `publish-lag` | [6](https://github.com/lexifina/slovakia-law/compare/f580410761d2...e9a12fa57b2b) |
| [2026-11-23 17:10](checks/2026-11.md#sk-zilina-vzn-20261123t171014z) | zilina-vzn | 372 | 0 | 0 | 0 | 190 (0) | našli sa zmeny `publish-lag` | [177](https://github.com/lexifina/slovakia-law/compare/df51033789c7...f580410761d2) |
| [2026-11-23 17:07](checks/2026-11.md#sk-bratislava-vzn-20261123t170746z) | bratislava-vzn | 77 | 0 | 0 | 0 | 77 (0) | našli sa zmeny `publish-lag` | [67](https://github.com/lexifina/slovakia-law/compare/d2fbd4cab2ea...df51033789c7) |
| [2026-11-23 16:47](checks/2026-11.md#sk-slov-lex-op-20261123t164752z) | slov-lex-op | 1105 | 0 | 0 | 0 | 3 (0) | našli sa zmeny `audit-disagrees` | [294](https://github.com/lexifina/slovakia-law/compare/f104dadfe366...d2fbd4cab2ea) |
| [2026-11-23 16:35](checks/2026-11.md#sk-slov-lex-zz-20261123t163552z) | slov-lex-zz | 687 | 0 | 1 | 0 | 97 (0) | našli sa zmeny | — |
| [2026-11-23 01:09](checks/2026-11.md#sk-nitra-vzn-20261123t010929z) | nitra-vzn | 2 | 0 | 0 | 0 | 76 (0) | bez zmeny `publish-lag` | — |
| [2026-11-23 01:09](checks/2026-11.md#sk-banskabystrica-vzn-20261123t010925z) | banskabystrica-vzn | 3 | 0 | 0 | 0 | 158 (0) | bez zmeny `publish-lag` | — |
| [2026-11-23 01:09](checks/2026-11.md#sk-zilina-vzn-20261123t010918z) | zilina-vzn | 6 | 0 | 0 | 0 | 365 (0) | bez zmeny `publish-lag` | — |
| [2026-11-23 01:09](checks/2026-11.md#sk-bratislava-vzn-20261123t010914z) | bratislava-vzn | 4 | 0 | 0 | 0 | 139 (0) | bez zmeny `publish-lag` | — |
| [2026-11-23 01:09](checks/2026-11.md#sk-slov-lex-op-20261123t010912z) | slov-lex-op | 1 | 0 | 0 | 0 | 266 (0) | bez zmeny `publish-lag` | — |
| [2026-11-23 01:08](checks/2026-11.md#sk-slov-lex-zz-20261123t010838z) | slov-lex-zz | 27 | 0 | 0 | 0 | 176 (0) | bez zmeny `publish-lag` | — |

## Overte si to sami

```
python tools/checktrail.py                      # posledná kontrola každého zdroja
python tools/checktrail.py --day 2026-11-23     # všetky kontroly jedného dňa
python tools/checktrail.py --act <id>           # kedy bol predpis zaznamenaný a zverejnený
git log --grep='^Kind: check' --format='%ci %s'  # kontroly v histórii
```

Právnu silu má len oficiálne vydanie; texty tu sú kópie na čítanie a vyhľadávanie.
