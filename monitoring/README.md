<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Monitorovanie: čo sa číta a čo z toho vyplynulo

[English](README.en.md)

Ako global-law monitoruje všetky krajiny: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). Táto stránka robí to isté len pre Slovensko: každé čítanie oficiálneho zdroja, kedy prebehlo a čo z neho vyplynulo (pridané, zmenené a zrušené predpisy). Strojovo čitateľná podoba je v [data/checks/](../data/checks/) (JSON Lines, schéma `lexifina-check/1`), v `git log` ako commity `Kind: check` a po mesiacoch v [checks/](checks/).

**Posledná kontrola:** 2026-11-27 15:15 UTC, Banská Bystrica: register všeobecne záväzných nariadení (VZN): prečítané adresy: 17; pridané 0, zmenené 0, zrušené 0; kontrola zlyhala; nezverejnené 152, z toho bez dôvodu 0. Príznaky: `publish-lag`.

## Zdroje

| Zdroj | Priečinky | Ako často | Posledná úspešná kontrola | Posledný výsledok | Stav |
| --- | --- | --- | --- | --- | --- |
| [Slov-Lex: Zbierka zákonov](https://www.slov-lex.sk/ezbierky/pravne-predpisy) | `zz/`, `zb/`, `constitution/ustava/`, `volebny-zakon/` | denne | 2026-11-23 16:36 UTC | kontrola zlyhala | sledovaný: Slov-Lex nemá otvorené dáta, RSS ani zoznam ELI; toto je zoznam, z ktorého čerpá jeho vlastné vyhľadávanie |
| [Slov-Lex: Register opatrení](https://www.slov-lex.sk/ezbierky/chronologicky-register-opatreni) | `ro/` | denne | 2026-11-27 05:30 UTC | bez zmeny | sledovaný |
| [Bratislava: register všeobecne záväzných nariadení (VZN)](https://bratislava.sk/vzn) | `local/bratislava/` | denne | 2026-11-27 05:31 UTC | bez zmeny | sledovaný |
| [Žilina: register všeobecne záväzných nariadení (VZN)](https://zilina.sk/mesto-zilina/sprava-mesta/legislativa/vseobecne-zavazne-nariadenia/) | `local/zilina/` | denne | 2026-11-25 05:34 UTC | kontrola zlyhala | sledovaný |
| [Banská Bystrica: register všeobecne záväzných nariadení (VZN)](https://www.banskabystrica.sk/vzn/) | `local/banskabystrica/` | denne | 2026-11-23 17:18 UTC | kontrola zlyhala | sledovaný |
| [Nitra: register všeobecne záväzných nariadení (VZN)](https://nitra.sk/vzn/) | `local/nitra/` | denne | 2026-11-27 05:35 UTC | bez zmeny | sledovaný: zoznam neuvádza dni platnosti (mesto ich uvádza na stránke každého záznamu): vidno len zmenené a nové záznamy |

## Posledných 30 dní

| Začiatok (UTC) | Zdroj | Prečítané | Pridané | Zmenené | Zrušené | Nezverejnené (bez dôvodu) | Výsledok | Commity |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-27 15:14](checks/2026-11.md#sk-banskabystrica-vzn-20261127t151431z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-27 15:13](checks/2026-11.md#sk-zilina-vzn-20261127t151319z) | zilina-vzn | 57 | 0 | 0 | 0 | 154 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-27 15:04](checks/2026-11.md#sk-slov-lex-zz-20261127t150444z) | slov-lex-zz | 387 | 0 | 0 | 0 | 106 (0) | kontrola zlyhala | — |
| [2026-11-27 14:13](checks/2026-11.md#sk-banskabystrica-vzn-20261127t141319z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-27 14:12](checks/2026-11.md#sk-zilina-vzn-20261127t141210z) | zilina-vzn | 57 | 0 | 0 | 0 | 154 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-27 14:04](checks/2026-11.md#sk-slov-lex-zz-20261127t140438z) | slov-lex-zz | 387 | 0 | 0 | 0 | 106 (0) | kontrola zlyhala | — |
| [2026-11-27 13:13](checks/2026-11.md#sk-banskabystrica-vzn-20261127t131312z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-27 13:12](checks/2026-11.md#sk-zilina-vzn-20261127t131207z) | zilina-vzn | 57 | 0 | 0 | 0 | 154 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-27 13:04](checks/2026-11.md#sk-slov-lex-zz-20261127t130453z) | slov-lex-zz | 387 | 0 | 0 | 0 | 106 (0) | kontrola zlyhala | — |
| [2026-11-27 12:12](checks/2026-11.md#sk-banskabystrica-vzn-20261127t121245z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-27 12:11](checks/2026-11.md#sk-zilina-vzn-20261127t121141z) | zilina-vzn | 57 | 0 | 0 | 0 | 154 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-27 12:04](checks/2026-11.md#sk-slov-lex-zz-20261127t120436z) | slov-lex-zz | 387 | 0 | 0 | 0 | 106 (0) | kontrola zlyhala | — |
| [2026-11-27 11:12](checks/2026-11.md#sk-banskabystrica-vzn-20261127t111245z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-27 11:11](checks/2026-11.md#sk-zilina-vzn-20261127t111140z) | zilina-vzn | 57 | 0 | 0 | 0 | 154 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-27 11:04](checks/2026-11.md#sk-slov-lex-zz-20261127t110435z) | slov-lex-zz | 387 | 0 | 0 | 0 | 106 (0) | kontrola zlyhala | — |
| [2026-11-27 10:12](checks/2026-11.md#sk-banskabystrica-vzn-20261127t101255z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-27 10:11](checks/2026-11.md#sk-zilina-vzn-20261127t101149z) | zilina-vzn | 57 | 0 | 0 | 0 | 154 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-27 10:04](checks/2026-11.md#sk-slov-lex-zz-20261127t100435z) | slov-lex-zz | 387 | 0 | 1 | 0 | 106 (0) | kontrola zlyhala | — |
| [2026-11-27 09:12](checks/2026-11.md#sk-banskabystrica-vzn-20261127t091237z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-27 09:11](checks/2026-11.md#sk-zilina-vzn-20261127t091130z) | zilina-vzn | 57 | 0 | 0 | 0 | 154 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-27 09:04](checks/2026-11.md#sk-slov-lex-zz-20261127t090435z) | slov-lex-zz | 387 | 0 | 4 | 0 | 106 (0) | kontrola zlyhala | — |
| [2026-11-27 08:13](checks/2026-11.md#sk-banskabystrica-vzn-20261127t081302z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-27 08:11](checks/2026-11.md#sk-zilina-vzn-20261127t081150z) | zilina-vzn | 57 | 0 | 0 | 0 | 154 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-27 08:04](checks/2026-11.md#sk-slov-lex-zz-20261127t080438z) | slov-lex-zz | 387 | 0 | 0 | 0 | 106 (0) | kontrola zlyhala | — |
| [2026-11-27 05:33](checks/2026-11.md#sk-nitra-vzn-20261127t053343z) | nitra-vzn | 128 | 0 | 0 | 0 | 3 (0) | bez zmeny | — |
| [2026-11-27 05:33](checks/2026-11.md#sk-banskabystrica-vzn-20261127t053326z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-27 05:31](checks/2026-11.md#sk-zilina-vzn-20261127t053111z) | zilina-vzn | 57 | 0 | 0 | 0 | 154 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-27 05:30](checks/2026-11.md#sk-bratislava-vzn-20261127t053039z) | bratislava-vzn | 21 | 0 | 0 | 0 | 37 (0) | bez zmeny `publish-lag` | — |
| [2026-11-27 05:28](checks/2026-11.md#sk-slov-lex-op-20261127t052806z) | slov-lex-op | 141 | 0 | 0 | 0 | 4 (0) | bez zmeny | — |
| [2026-11-27 05:20](checks/2026-11.md#sk-slov-lex-zz-20261127t052055z) | slov-lex-zz | 387 | 7 | 0 | 0 | 106 (0) | kontrola zlyhala | — |
| [2026-11-26 15:25](checks/2026-11.md#sk-banskabystrica-vzn-20261126t152513z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-26 15:24](checks/2026-11.md#sk-zilina-vzn-20261126t152407z) | zilina-vzn | 57 | 0 | 0 | 0 | 154 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-26 15:14](checks/2026-11.md#sk-slov-lex-zz-20261126t151404z) | slov-lex-zz | 387 | 0 | 0 | 0 | 99 (0) | kontrola zlyhala | — |
| [2026-11-26 14:13](checks/2026-11.md#sk-banskabystrica-vzn-20261126t141332z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-26 14:12](checks/2026-11.md#sk-zilina-vzn-20261126t141228z) | zilina-vzn | 57 | 0 | 0 | 0 | 154 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-26 14:04](checks/2026-11.md#sk-slov-lex-zz-20261126t140447z) | slov-lex-zz | 387 | 0 | 0 | 0 | 99 (0) | kontrola zlyhala | — |
| [2026-11-26 13:12](checks/2026-11.md#sk-banskabystrica-vzn-20261126t131254z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-26 13:11](checks/2026-11.md#sk-zilina-vzn-20261126t131149z) | zilina-vzn | 57 | 0 | 0 | 0 | 154 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-26 13:04](checks/2026-11.md#sk-slov-lex-zz-20261126t130439z) | slov-lex-zz | 387 | 0 | 0 | 0 | 99 (0) | kontrola zlyhala | — |
| [2026-11-26 12:12](checks/2026-11.md#sk-banskabystrica-vzn-20261126t121249z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-26 12:11](checks/2026-11.md#sk-zilina-vzn-20261126t121142z) | zilina-vzn | 57 | 0 | 0 | 0 | 154 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-26 12:04](checks/2026-11.md#sk-slov-lex-zz-20261126t120432z) | slov-lex-zz | 387 | 0 | 0 | 0 | 99 (0) | kontrola zlyhala | — |
| [2026-11-26 11:13](checks/2026-11.md#sk-banskabystrica-vzn-20261126t111316z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-26 11:12](checks/2026-11.md#sk-zilina-vzn-20261126t111209z) | zilina-vzn | 57 | 0 | 0 | 0 | 154 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-26 11:04](checks/2026-11.md#sk-slov-lex-zz-20261126t110453z) | slov-lex-zz | 387 | 0 | 0 | 0 | 99 (0) | kontrola zlyhala | — |
| [2026-11-26 10:14](checks/2026-11.md#sk-banskabystrica-vzn-20261126t101416z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-26 10:13](checks/2026-11.md#sk-zilina-vzn-20261126t101301z) | zilina-vzn | 57 | 0 | 0 | 0 | 154 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-26 10:05](checks/2026-11.md#sk-slov-lex-zz-20261126t100513z) | slov-lex-zz | 387 | 0 | 0 | 0 | 99 (0) | kontrola zlyhala | — |
| [2026-11-26 09:29](checks/2026-11.md#sk-banskabystrica-vzn-20261126t092913z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-26 09:28](checks/2026-11.md#sk-zilina-vzn-20261126t092808z) | zilina-vzn | 57 | 0 | 0 | 0 | 154 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-26 09:20](checks/2026-11.md#sk-slov-lex-zz-20261126t092054z) | slov-lex-zz | 387 | 0 | 0 | 0 | 99 (0) | kontrola zlyhala | — |
| [2026-11-26 05:33](checks/2026-11.md#sk-nitra-vzn-20261126t053304z) | nitra-vzn | 128 | 0 | 0 | 0 | 3 (0) | bez zmeny | — |
| [2026-11-26 05:32](checks/2026-11.md#sk-banskabystrica-vzn-20261126t053238z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-26 05:30](checks/2026-11.md#sk-zilina-vzn-20261126t053055z) | zilina-vzn | 57 | 0 | 0 | 0 | 154 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-26 05:30](checks/2026-11.md#sk-bratislava-vzn-20261126t053022z) | bratislava-vzn | 21 | 0 | 0 | 0 | 37 (0) | bez zmeny `publish-lag` | — |
| [2026-11-26 05:27](checks/2026-11.md#sk-slov-lex-op-20261126t052751z) | slov-lex-op | 141 | 0 | 0 | 0 | 4 (0) | bez zmeny | — |
| [2026-11-26 05:20](checks/2026-11.md#sk-slov-lex-zz-20261126t052047z) | slov-lex-zz | 387 | 0 | 0 | 0 | 99 (0) | kontrola zlyhala | — |
| [2026-11-25 15:11](checks/2026-11.md#sk-banskabystrica-vzn-20261125t151141z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-25 15:04](checks/2026-11.md#sk-slov-lex-zz-20261125t150433z) | slov-lex-zz | 387 | 0 | 0 | 0 | 99 (0) | kontrola zlyhala | — |
| [2026-11-25 14:11](checks/2026-11.md#sk-banskabystrica-vzn-20261125t141146z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-25 14:04](checks/2026-11.md#sk-slov-lex-zz-20261125t140440z) | slov-lex-zz | 387 | 0 | 0 | 0 | 99 (0) | kontrola zlyhala | — |
| [2026-11-25 13:11](checks/2026-11.md#sk-banskabystrica-vzn-20261125t131144z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-25 13:04](checks/2026-11.md#sk-slov-lex-zz-20261125t130437z) | slov-lex-zz | 387 | 0 | 0 | 0 | 99 (0) | kontrola zlyhala | — |
| [2026-11-25 12:11](checks/2026-11.md#sk-banskabystrica-vzn-20261125t121136z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-25 12:04](checks/2026-11.md#sk-slov-lex-zz-20261125t120435z) | slov-lex-zz | 387 | 0 | 0 | 0 | 99 (0) | kontrola zlyhala | — |
| [2026-11-25 11:11](checks/2026-11.md#sk-banskabystrica-vzn-20261125t111133z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-25 11:04](checks/2026-11.md#sk-slov-lex-zz-20261125t110435z) | slov-lex-zz | 387 | 0 | 0 | 0 | 99 (0) | kontrola zlyhala | — |
| [2026-11-25 10:26](checks/2026-11.md#sk-banskabystrica-vzn-20261125t102629z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-25 10:19](checks/2026-11.md#sk-slov-lex-zz-20261125t101921z) | slov-lex-zz | 387 | 0 | 0 | 0 | 99 (0) | kontrola zlyhala | — |
| [2026-11-25 09:11](checks/2026-11.md#sk-banskabystrica-vzn-20261125t091128z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-25 09:04](checks/2026-11.md#sk-slov-lex-zz-20261125t090433z) | slov-lex-zz | 387 | 0 | 0 | 0 | 99 (0) | kontrola zlyhala | — |
| [2026-11-25 05:35](checks/2026-11.md#sk-nitra-vzn-20261125t053513z) | nitra-vzn | 128 | 0 | 0 | 0 | 3 (0) | bez zmeny | — |
| [2026-11-25 05:34](checks/2026-11.md#sk-banskabystrica-vzn-20261125t053457z) | banskabystrica-vzn | 17 | 0 | 0 | 0 | 152 (0) | kontrola zlyhala `publish-lag` | — |
| [2026-11-25 05:31](checks/2026-11.md#sk-zilina-vzn-20261125t053117z) | zilina-vzn | 80 | 0 | 0 | 0 | 146 (0) | našli sa zmeny `publish-lag` | [26](https://github.com/lexifina/slovakia-law/compare/43e98bfe350e...300810473461) |
| [2026-11-25 05:29](checks/2026-11.md#sk-bratislava-vzn-20261125t052928z) | bratislava-vzn | 42 | 0 | 0 | 0 | 36 (0) | našli sa zmeny `publish-lag` | [26](https://github.com/lexifina/slovakia-law/compare/4ac9db488bb2...43e98bfe350e) |
| [2026-11-25 05:26](checks/2026-11.md#sk-slov-lex-op-20261125t052652z) | slov-lex-op | 144 | 1 | 0 | 0 | 4 (0) | našli sa zmeny | — |
| [2026-11-25 05:19](checks/2026-11.md#sk-slov-lex-zz-20261125t051953z) | slov-lex-zz | 387 | 2 | 0 | 0 | 99 (0) | kontrola zlyhala | — |
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
