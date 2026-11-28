<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Sledovanie zdrojov: čo sa sleduje pre Slovensko

[English](WATCHING.en.md)

Ako global-law sleduje zdroje všetkých krajín: [global-law WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md). Táto stránka robí to isté len pre Slovensko: každý oficiálny zdroj, z ktorého tento repozitár berie text, čo sa na ňom číta, ako často a kedy bol naposledy prečítaný. Každé čítanie a čo z neho vyplynulo: [monitoring/](monitoring/README.md).

| Zdroj | Čo sa číta | Priečinky | Ako často | Naposledy prečítané | Stav |
| --- | --- | --- | --- | --- | --- |
| [Slov-Lex: Zbierka zákonov](https://www.slov-lex.sk/ezbierky/pravne-predpisy) | zoznam všetkých predpisov Zbierky z vyhľadávacej služby Slov-Lexu (1 000 na požiadavku): číslo, názov, deň vyhlásenia a znenie účinné dnes, alebo posledné znenie a deň, keď skončilo; stránky časových verzií (static.slov-lex.sk) každého nového alebo zmeneného predpisu; každý deň siedmu časť účinných znení predpisov v repozitári; PDF niekoľkých verzií | `zz/`, `zb/`, `constitution/ustava/`, `volebny-zakon/` | denne | 2026-11-28 05:20 UTC | sledovaný: Slov-Lex nemá otvorené dáta, RSS ani zoznam ELI; toto je zoznam, z ktorého čerpá jeho vlastné vyhľadávanie |
| [Slov-Lex: Register opatrení](https://www.slov-lex.sk/ezbierky/chronologicky-register-opatreni) | zoznam všetkých opatrení registra (jedna požiadavka): číslo, názov a znenie účinné dnes; stránky časových verzií každého nového alebo zmeneného opatrenia; každý deň siedmu časť opatrení v repozitári; PDF niekoľkých verzií | `ro/` | denne | 2026-11-28 05:27 UTC | sledovaný |
| [Bratislava: register všeobecne záväzných nariadení (VZN)](https://bratislava.sk/vzn) | register mesta (jeho verejná služba GraphQL, 100 záznamov na požiadavku): číslo, účinnosť, zrušenie, dokument a deň poslednej zmeny záznamu; dokumenty VZN, ktoré tu ešte nie sú; každý deň tridsiatu časť dokumentov v repozitári | `local/bratislava/` | denne | 2026-11-28 05:29 UTC | sledovaný |
| [Žilina: register všeobecne záväzných nariadení (VZN)](https://zilina.sk/mesto-zilina/sprava-mesta/legislativa/vseobecne-zavazne-nariadenia/) | register mesta (verejný zoznam REST jeho webu, 100 záznamov na požiadavku): číslo, platnosť, dokumenty a deň poslednej zmeny záznamu; dokumenty VZN, ktoré tu ešte nie sú; každý deň tridsiatu časť dokumentov v repozitári | `local/zilina/` | denne | 2026-11-28 05:30 UTC | sledovaný |
| [Banská Bystrica: register všeobecne záväzných nariadení (VZN)](https://www.banskabystrica.sk/vzn/) | register mesta (verejný zoznam REST jeho webu, 100 záznamov na požiadavku): číslo, platnosť, dokumenty a deň poslednej zmeny záznamu; dokumenty VZN, ktoré tu ešte nie sú; každý deň tridsiatu časť dokumentov v repozitári | `local/banskabystrica/` | denne | 2026-11-28 05:31 UTC | sledovaný |
| [Nitra: register všeobecne záväzných nariadení (VZN)](https://nitra.sk/vzn/) | register mesta (verejný zoznam REST jeho webu, 100 záznamov na požiadavku): názov s číslom a deň poslednej zmeny záznamu; stránku každého záznamu a dokumenty VZN, ktoré tu ešte nie sú; každý deň tridsiatu časť dokumentov v repozitári | `local/nitra/` | denne | 2026-11-28 05:31 UTC | sledovaný: zoznam neuvádza dni platnosti (mesto ich uvádza na stránke každého záznamu): vidno len zmenené a nové záznamy |

Zdroje sa čítajú v medziach ich robots.txt a podmienok používania, s prestávkami medzi požiadavkami.
