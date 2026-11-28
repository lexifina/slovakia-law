<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Watching the sources: what is watched for Slovakia

[Slovenčina](WATCHING.md)

How global-law watches every country's sources: [global-law WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md). This page is the same for Slovakia only: every official source this repository takes text from, what is read on it, how often and when it was last read. Every read and what came of it: [monitoring/](monitoring/README.en.md).

| Source | What is read | Folders | How often | Last read | State |
| --- | --- | --- | --- | --- | --- |
| [Slov-Lex: Collection of Laws (Zbierka zákonov)](https://www.slov-lex.sk/ezbierky/pravne-predpisy) | the list of every item of the Collection from Slov-Lex's search service (1,000 a request): its number, title, day of announcement and the version in force today, or its last version and the day it ended; the version pages (static.slov-lex.sk) of each new or changed item; a seventh of the held acts' versions in force each day; a few versions' PDFs | `zz/`, `zb/`, `constitution/ustava/`, `volebny-zakon/` | daily | 2026-11-28 05:20 UTC | watched: Slov-Lex has no open-data feed, RSS or ELI list; this is the list behind its own search |
| [Slov-Lex: Register of measures (Register opatrení)](https://www.slov-lex.sk/ezbierky/chronologicky-register-opatreni) | the list of every measure of the register (one request): its number, title and the version in force today; the version pages of each new or changed measure; a seventh of the held ones each day; a few versions' PDFs | `ro/` | daily | 2026-11-28 05:27 UTC | watched |
| [Bratislava: register of generally binding regulations (VZN)](https://bratislava.sk/vzn) | the city's register (its public GraphQL service, 100 records a request): number, day in force, repeal, document and the day each record last changed; the documents of the VZN not here yet; a thirtieth of the held documents each day | `local/bratislava/` | daily | 2026-11-28 05:29 UTC | watched |
| [Žilina: register of generally binding regulations (VZN)](https://zilina.sk/mesto-zilina/sprava-mesta/legislativa/vseobecne-zavazne-nariadenia/) | the city's register (its site's public REST list, 100 records a request): number, validity, documents and the day each record last changed; the documents of the VZN not here yet; a thirtieth of the held documents each day | `local/zilina/` | daily | 2026-11-28 05:30 UTC | watched |
| [Banská Bystrica: register of generally binding regulations (VZN)](https://www.banskabystrica.sk/vzn/) | the city's register (its site's public REST list, 100 records a request): number, validity, documents and the day each record last changed; the documents of the VZN not here yet; a thirtieth of the held documents each day | `local/banskabystrica/` | daily | 2026-11-28 05:31 UTC | watched |
| [Nitra: register of generally binding regulations (VZN)](https://nitra.sk/vzn/) | the city's register (its site's public REST list, 100 records a request): title with the number, and the day each record last changed; each record's page and the documents of the VZN not here yet; a thirtieth of the held documents each day | `local/nitra/` | daily | 2026-11-28 05:31 UTC | watched: the list gives no validity days (the city puts them on each record's page): only changed and new records are seen |

Sources are read within their robots.txt and terms, with pauses between requests.
