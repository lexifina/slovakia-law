Príloha č. 3 k vyhláške č. 91/2008 Z. z. [Príloha 03](../assets/da742d1df89e483c9f4bac09f7b457b8faf10c21db25476308fb2357ce70006f.pdf)

- Metodika poskytovania informácie Ddf (DIT) 07-98

- 1. V informácii sa uvádzajú všetky transakcie s majetkom v dôchodkovom fonde uskutočnené za príslušný pracovný deň. Ak sa informácia zmení alebo stornuje, zašle sa opravná informácia s vykonanými zmenami ako vyššia verzia informácie. Ak opravná informácia má vplyv aj na údaje v ďalšej informácii, opraví sa aj ďalšia informácia a zašle sa ako vyššia verzia.

- 2. Na ocenenie transakcií sa vzťahuje vyhláška Ministerstva financií Slovenskej republiky č. 48/2005 Z. z. o metódach a postupoch stanovenia hodnoty majetku v dôchodkovom fonde a o spôsobe určenia hodnoty cenných papierov v majetku v dôchodkovom fonde (ďalej len „vyhláška“).

- 3. Ak v príslušný pracovný deň nie je vykonaná žiadna transakcia s majetkom v dôchodkovom fonde, predkladá sa prázdna informácia.

- 4. V záhlaví v ľavom rohu v časti „Názov dôchodkového fondu“ sa uvádza názov dôchodkového fondu podľa platného povolenia na výkon činnosti.

- 5. V záhlaví v pravom rohu v časti „Identifikačný kód“ sa uvádza príslušný číselný kód, ktorý sa nachádza v APS STATUS DFT časť C. Číselníky/C.1 Subjekty.

- 6. V záhlaví v pravom rohu v časti „Stav ku dňu“ sa uvádza dátum, ku ktorému bola informácia vykázaná.

- 7. Pri prepočte súm z cudzej meny na slovenskú menu sa používa kurz NBS platný pre príslušnú menu v deň uskutočnenia transakcie.

- 8. Pri transakciách na bežnom účte alebo termínovanom vklade sa uvádza každé nakladanie s vkladom v príslušný pracovný deň. Transakcie sa vykazujú jednotlivo, vzájomne sa nespočítavajú ani nezapočítavajú.

- 9. Číselné údaje sa vykazujú ako skutočné obchodné a stavové údaje v podobe reálneho čísla, pričom sa vykazujú najviac na štrnásť desatinných miest.

- 10. V časti s názvom „Bežný účet“

  - a) v stĺpci „Typ“ sa uvádza „VKL“ pre vklad alebo „VYB“ pre výber,

  - b) v stĺpci „Mena“ sa uvádza kód meny podľa medzinárodných štandardov ISO 4217, kód príslušnej meny sa vyberá zo zoznamu prípustných kódov číselníka MENA, ktorý sa nachádza v APS STATUS DFT/C. Číselníky/C.7 Číselníky kódov,

  - c) v stĺpci „Objem v CM“ sa uvádza objem transakcie v cudzej mene; ak ide o výber, uvádza sa hodnota so záporným znamienkom; ak ide o transakciu v slovenskej mene, uvádza sa „0“,

  - d) v stĺpci „Objem v Sk“ sa uvádza objem transakcie v slovenskej mene alebo protihodnota v slovenskej mene; ak ide o výber, uvádza sa hodnota so záporným znamienkom.

- 11. V časti s názvom „Termínovaný vklad“

  - a) v stĺpci „ID obchodu“ sa uvádza identifikácia obchodu vnútorným alfanumerickým kódom,

  - b) v stĺpci „Typ TV“ sa uvádza „FIX“ pre fixný alebo „VAR“ pre variabilný typ vkladu,

  - c) v stĺpci „Mena“ sa uvádza kód meny podľa medzinárodných štandardov ISO 4217, kód príslušnej meny sa vyberá zo zoznamu prípustných kódov číselníka MENA, ktorý sa nachádza v APS STATUS DFT/C. Číselníky/C.7 Číselníky kódov,

  - d) v stĺpci „Objem v CM“ sa uvádza objem transakcie v cudzej mene; ak ide o transakciu v slovenskej mene, uvádza sa „0“,

  - e) v stĺpci „Objem v Sk“ sa uvádza objem transakcie v slovenskej mene alebo protihodnota v slovenskej mene,

  - f) v stĺpci „Dátum – začiatok trvania TV“ sa uvádza začiatok doby platnosti termínovaného vkladu v tvare d.m.rrrr,

  - g) v stĺpci „Dátum – koniec trvania TV“ sa uvádza koniec doby platnosti termínovaného vkladu v tvare d.m.rrrr,

  - h) v stĺpci „Sadzba v %“ sa uvádza úroková sadzba dohodnutá v deň uzatvorenia termínovaného vkladu, pri termínovanom vklade s variabilnou sadzbou sa uvádza hodnota úrokovej sadzby, ktorá je súčtom hodnoty variabilnej sadzby platnej pre príslušné obdobie a bázických bodov (pipsov),

  - i) v stĺpci „Protistrana“ sa uvádza názov protistrany, s ktorou bol vykonaný termínovaný vklad; názov protistrany sa uvádza vo forme SWIFT kódu; ak protistrana nemá SWIFT kód, uvádza sa obchodné meno a sídlo,

  - j) v stĺpci „Báza úročenia“ sa uvádza jedna z možností: Act/360, Act/365, 30/360, 30E/360 alebo Act/Act, pričom čitateľ je počet úročených dní a menovateľ je počet dní v roku,

  - k) v stĺpci „Splátka istiny“ sa uvádza frekvencia splácania istiny takto: týždenná „W“, dvojtýždňová „2W“, mesačná „M“, dvojmesačná „2M“, štvrťročná „Q“, polročná „S“, ročná „Y“, jednorazové splatenie istiny na konci „F“, nepravidelné splatenie istiny „I“,

  - l) v stĺpci „Splátka úroku“ sa uvádza frekvencia splácania úroku takto: týždenná „W“, dvojtýždňová „2W“, mesačná „M“, dvojmesačná „2M“, štvrťročná „Q“, polročná „S“, ročná „Y“, jednorazové splatenie úroku na konci „F“, nepravidelné splatenie úroku „I“,

  - m) v stĺpci „Variabilná sadzba“ sa uvádza napríklad „2W BRIBOR“, „3M BRIBOR“, „1M PRIBOR“,

  - n) v stĺpci „Bázické body (pips) k variabilnej sadzbe“ sa uvádza reálne číslo, napríklad ak úroková sadzba je stanovená „3M LIBOR-35“, uvádza sa „-35“,

  - o) v stĺpci „Dátum splácania istiny“ sa uvádza dátum, od ktorého sa začína počítať splácanie istiny; vypĺňa sa, ak sa dátum splácania líši od položky „Dátum – začiatok trvania TV“, uvádza sa v tvare d.m.rrrr,

  - p) v stĺpci „Dátum splácania úroku“ sa uvádza dátum, od ktorého sa začína počítať splácanie úroku; vypĺňa sa, ak sa dátum splácania líši od položky „Dátum – začiatok trvania TV“, uvádza sa v tvare d.m.rrrr,

  - Ak sa v spôsobe splátky istiny alebo splátky úroku uvádza nepravidelné splatenie istiny „I“ alebo nepravidelné splatenie úroku „I“, vypĺňa sa aj časť informácie „Termínovaný vklad s nepravidelnými splátkami istiny“ s doplňujúcimi údajmi, kde sa uvádza splátka istiny v jednotlivých dátumoch.

- 12. V časti s názvom „Termínovaný vklad s nepravidelnými splátkami istiny“

  - a) v stĺpci „ID obchodu“ sa uvádza identifikácia obchodu vnútorným alfanumerickým kódom,

  - b) v stĺpci „Dátum“ sa uvádza dátum, na ktorý sa viaže aktuálna splátka istiny termínovaného vkladu; uvádza sa v tvare d.m.rrrr,

  - c) v stĺpci „Splátka istiny“ sa uvádza aktuálna splátka nominálnej hodnoty termínovaného vkladu,

  - d) v stĺpci „Mena“ sa uvádza kód meny podľa medzinárodných štandardov ISO 4217, kód príslušnej meny sa vyberá zo zoznamu prípustných kódov číselníka MENA, ktorý sa nachádza v APS STATUS DFT/C. Číselníky/C.7 Číselníky kódov,

  - e) v stĺpci „Splátka úroku“ sa uvádza „ÁNO“, ak sa spolu so splátkou istiny platí aj úrok; v opačnom prípade sa uvádza „NIE“.

- 13. V časti s názvom „FX transakcie“

  - a) v stĺpci „ID obchodu“ sa uvádza identifikácia obchodu vnútorným alfanumerickým kódom,

  - b) v stĺpci „Typ“ sa uvádza „SP“ pre FX spot alebo „F“ pre FX forward,

  - c) v stĺpci „Mena 1“ sa uvádza hlavná mena v menovom páre podľa medzinárodných štandardov ISO 4217, kód príslušnej meny sa vyberá zo zoznamu prípustných kódov číselníka MENA, ktorý sa nachádza v APS STATUS DFT/C. Číselníky/C.7 Číselníky kódov,

  - d) v stĺpci „Objem – mena 1“ sa uvádza objem transakcie v hlavnej mene; ak ide o predaj meny, uvádza sa hodnota so záporným znamienkom; ak bola uskutočnená transakcia v slovenskej mene, uvádza sa „0“,

  - e) v stĺpci „Objem – mena 1 v Sk“ sa uvádza objem transakcie v slovenskej mene alebo protihodnota v slovenskej mene; ak ide o predaj meny, uvádza sa hodnota so záporným znamienkom,

  - f) v stĺpci „Mena 2“ sa uvádza vedľajšia mena v menovom páre podľa medzinárodných štandardov ISO 4217, kód príslušnej meny sa vyberá zo zoznamu prípustných kódov číselníka MENA, ktorý sa nachádza v APS STATUS DFT/C. Číselníky/C.7 Číselníky kódov,

  - g) v stĺpci „Objem – mena 2“ sa uvádza objem transakcie vo vedľajšej mene; ak ide o predaj meny, uvádza sa hodnota so záporným znamienkom; ak bola uskutočnená transakcia v slovenskej mene, uvádza sa „0“,

  - h) v stĺpci „Objem – mena 2 v Sk“ sa uvádza objem transakcie v slovenskej mene alebo protihodnota v slovenskej mene; ak ide o predaj meny, uvádza sa hodnota so záporným znamienkom,

  - i) v stĺpci „Kurz“ sa uvádza dohodnutý spotový alebo forwardový kurz,

  - j) v stĺpci „Dátum – valuta“ sa uvádza dátum vyrovnania obchodu v tvare d.m.rrrr,

  - k) v stĺpci „Protistrana“ sa uvádza názov protistrany, s ktorou bola vykonaná FX spotová alebo forwardová transakcia, názov protistrany sa uvádza vo forme SWIFT kódu; ak protistrana nemá SWIFT kód, uvádza sa obchodné meno a sídlo.

- 14. V časti s názvom „FX swapy“

  - a) v stĺpci „ID obchodu“ sa uvádza identifikácia obchodu vnútorným alfanumerickým kódom,

  - b) v stĺpci „Typ“ sa uvádza „SP“ pre FX spot alebo „F“ pre FX forward,

  - c) v stĺpci „Mena 1“ sa uvádza hlavná mena v menovom páre podľa medzinárodných štandardov ISO 4217, kód príslušnej meny sa vyberá zo zoznamu prípustných kódov číselníka MENA, ktorý sa nachádza v APS STATUS DFT/C. Číselníky/C.7 Číselníky kódov,

  - d) v stĺpci „Objem – mena 1“ sa uvádza objem transakcie v hlavnej mene; ak ide o predaj meny, uvádza sa hodnota so záporným znamienkom; ak bola transakcia uskutočnená v slovenskej mene, uvádza sa „0“,

  - e) v stĺpci „Objem – mena 1 v Sk“ sa uvádza objem transakcie v slovenskej mene alebo protihodnota v slovenskej mene; ak ide o predaj meny, uvádza sa hodnota so záporným znamienkom,

  - f) v stĺpci „Mena 2“ sa uvádza vedľajšia mena v menovom páre podľa medzinárodných štandardov ISO 4217, kód príslušnej meny sa vyberá zo zoznamu prípustných kódov číselníka MENA, ktorý sa nachádza v APS STATUS DFT/C. Číselníky/C.7 Číselníky kódov,

  - g) v stĺpci „Objem – mena 2“ sa uvádza objem transakcie vo vedľajšej mene; ak ide o predaj meny, uvádza sa hodnota so záporným znamienkom; ak bola uskutočnená transakcia v slovenskej mene, uvádza sa „0“,

  - h) v stĺpci „Objem – mena 2 v Sk“ sa uvádza objem transakcie v slovenskej mene alebo protihodnota v slovenskej mene; ak ide o predaj meny, uvádza sa hodnota so záporným znamienkom,

  - i) v stĺpci „Kurz“ sa uvádza dohodnutý spotový alebo forwardový kurz,

  - j) v stĺpci „Dátum – valuta“ sa uvádza dátum vyrovnania obchodu v tvare d.m.rrrr,

  - k) v stĺpci „Protistrana“ sa uvádza názov protistrany, s ktorou bola vykonaná FX spotová alebo forwardová transakcia, názov protistrany sa uvádza vo forme SWIFT kódu; ak protistrana nemá SWIFT kód, uvádza sa obchodné meno a sídlo.

  - Vo výkaze sa pre každý FX swap vykazujú dva riadky, jeden pre spotovú časť a jeden pre forwardovú časť.

- 15. V časti s názvom „Opcie“

  - a) v stĺpci „ID obchodu“ sa uvádza identifikácia obchodu vnútorným alfanumerickým kódom,

  - b) v stĺpci „Typ opcie“ sa uvádza „CO“ pre call opciu alebo „PO“ pre put opciu,

  - c) v stĺpci „Nákup/predaj“ sa uvádza „N“ pre nákup alebo „P“ pre predaj,

  - d) pod názvom stĺpca „Mena 1“ sa uvádza hlavná mena v menovom páre podľa medzinárodných štandardov ISO 4217, kód príslušnej meny sa vyberá zo zoznamu prípustných kódov číselníka MENA, ktorý sa nachádza v APS STATUS DFT/C. Číselníky/C.7 Číselníky kódov,

  - e) v stĺpci „Objem – mena 1“ sa uvádza objem transakcie v hlavnej mene; ak ide o predaj meny, uvádza sa hodnota so záporným znamienkom; ak bola uskutočnená transakcia v slovenskej mene, uvádza sa „0“,

  - f) v stĺpci „Objem – mena 1 v Sk“ sa uvádza objem transakcie v slovenskej mene alebo protihodnota v slovenskej mene; ak ide o predaj meny, uvádza sa hodnota so záporným znamienkom,

  - g) v stĺpci „Mena 2“ sa uvádza vedľajšia mena v menovom páre podľa medzinárodných štandardov ISO 4217, kód príslušnej meny sa vyberá zo zoznamu prípustných kódov číselníka MENA, ktorý sa nachádza v APS STATUS DFT/C. Číselníky/C.7 Číselníky kódov,

  - h) v stĺpci „Objem – mena 2“ sa uvádza objem transakcie vo vedľajšej mene; ak ide o predaj meny, uvádza sa hodnota so záporným znamienkom; ak bola uskutočnená transakcia v slovenskej mene, uvádza sa „0“,

  - i) v stĺpci „Objem – mena 2 v Sk“ sa uvádza objem transakcie v slovenskej mene alebo protihodnota v slovenskej mene; ak ide o predaj meny, uvádza sa hodnota so záporným znamienkom,

  - j) v stĺpci „Realizačný kurz opcie“ sa uvádza vopred dohodnutý realizačný menový kurz (strike price),

  - k) v stĺpci „Dátum – valuta – expirácia opcie“ sa uvádza dátum expirácie opcie v tvare d.m.rrrr,

  - l) v stĺpci „Mena prémie“ sa uvádza kód meny podľa medzinárodných štandardov ISO 4217, kód príslušnej meny sa vyberá zo zoznamu prípustných kódov číselníka MENA, ktorý sa nachádza v APS STATUS DFT/C. Číselníky/C.7 Číselníky kódov,

  - m) v stĺpci „Opčná prémia v CM“ sa uvádza objem opčnej prémie v príslušnej cudzej mene; ak ide o transakciu v slovenskej mene, uvádza sa „0“,

  - n) v stĺpci „Opčná prémia v Sk“ sa uvádza objem opčnej prémie v slovenskej mene alebo protihodnota v slovenskej mene,

  - o) v stĺpci „Dátum – valuta – prémia“ sa uvádza dátum vyrovnania prémie v tvare d.m.rrrr,

  - p) v stĺpci „Protistrana“ sa uvádza názov protistrany, s ktorou bola vykonaná FX opcia európskeho typu, názov protistrany sa uvádza vo forme SWIFT kódu; ak protistrana nemá SWIFT kód, uvádza sa obchodné meno a sídlo.

- 16. V časti s názvom „Akcie a Podielové listy“

  - a) v stĺpci „ID obchodu“ sa uvádza identifikácia obchodu vnútorným alfanumerickým kódom,

  - b) v stĺpci „Nákup/predaj“ sa uvádza „N“ pre nákup alebo „P“ pre predaj,

  - c) v stĺpci „ISIN“ sa uvádza číselný kód emisie cenného papiera,

  - d) v stĺpci „Emitent“ sa uvádza názov subjektu, ktorý vydal cenný papier; ak ide o podielové listy, uvádza sa názov správcu podielového fondu,

  - e) v stĺpci „Počet kusov“ sa uvádza počet kusov cenných papierov, ktoré boli kúpené do majetku fondu alebo predané z majetku fondu,

  - f) v stĺpci „Mena“ sa uvádza kód meny podľa medzinárodných štandardov ISO 4217, kód príslušnej meny sa vyberá zo zoznamu prípustných kódov číselníka MENA, ktorý sa nachádza v APS STATUS DFT/C. Číselníky/C.7 Číselníky kódov,

  - g) v stĺpci „Cena/ks v CM “ sa uvádza nákupná alebo predajná cena za jeden kus akcie alebo podielového listu v cudzej mene; ak bola uskutočnená transakcia v slovenskej mene, uvádza sa „0“,

  - h) v stĺpci „Cena/ks v Sk“ sa uvádza nákupná alebo predajná cena za jeden kus akcie alebo podielového listu v slovenskej mene,

  - i) v stĺpci „Objem obchodu spolu v CM“ sa uvádza celkový objem transakcie v cudzej mene; ak bola uskutočnená transakcia v slovenskej mene, uvádza sa „0“,

  - j) v stĺpci „Objem obchodu spolu v Sk“ sa uvádza celkový objem transakcie v slovenskej mene alebo protihodnota v slovenskej mene,

  - k) v stĺpci „Dátum – valuta“ sa uvádza dátum vyrovnania obchodu v tvare d.m.rrrr,

  - l) v stĺpci „Bloomberg ticker/Reuters RIC“ sa uvádza kód akcie alebo podielového listu zo systému Bloomberg alebo Reuters,

  - m) v stĺpci „Protistrana“ sa uvádza názov protistrany, s ktorou bol vykonaný nákup alebo predaj akcie alebo podielového listu; názov protistrany sa uvádza vo forme SWIFT kódu, ak protistrana nemá SWIFT kód, uvádza sa obchodné meno a sídlo.

- 17. V časti s názvom „Dlhopisy“

  - a) v stĺpci „ID obchodu“ sa uvádza identifikácia obchodu vnútorným alfanumerickým kódom,

  - b) v stĺpci „Typ“ sa uvádza kód príslušného typu dlhopisu, ktorý sa vyberá zo zoznamu prípustných kódov číselníka s názvom DRUH CENNÉHO PAPIERA, ktorý sa nachádza v APS STATUS DFT/C. Číselníky/C.7 Číselníky kódov,

  - c) v stĺpci „Nákup/predaj“ sa uvádza „N“ pre nákup alebo „P“ pre predaj,

  - d) v stĺpci „ISIN“ sa uvádza číselný kód emisie cenného papiera,

  - e) v stĺpci „Emitent“ sa uvádza názov subjektu, ktorý vydal cenný papier,

  - f) v stĺpci „Počet kusov“ sa uvádza počet kusov cenných papierov, ktoré boli kúpené do majetku dôchodkového fondu alebo predané z majetku dôchodkového fondu,

  - g) v stĺpci „Mena“ sa uvádza kód meny podľa medzinárodných štandardov ISO 4217, kód príslušnej meny sa vyberá zo zoznamu prípustných kódov číselníka MENA, ktorý sa nachádza v APS STATUS DFT/C. Číselníky/C.7 Číselníky kódov,

  - h) v stĺpci „Cena/ks v CM “ sa uvádza nákupná alebo predajná cena za jeden kus dlhopisu v cudzej mene; ak bola uskutočnená transakcia v slovenskej mene, uvádza sa „0“,

  - i) v stĺpci „Cena/ks v Sk“ sa uvádza nákupná alebo predajná cena za jeden kus dlhopisu v slovenskej mene alebo protihodnota v slovenskej mene,

  - j) v stĺpci „Objem obchodu spolu v CM“ sa uvádza celkový objem transakcie v cudzej mene; ak bola uskutočnená transakcia v slovenskej mene, uvádza sa „0“,

  - k) v stĺpci „Objem obchodu spolu v Sk“ sa uvádza celkový objem transakcie v slovenskej mene alebo protihodnota v slovenskej mene,

  - l) v stĺpci „Sadzba v %“ sa uvádza úroková sadzba, na ktorú dlhopis znie; pri variabilnej úrokovej sadzbe sa uvádza hodnota úrokovej sadzby, ktorá je súčtom jej fixnej a variabilnej zložky platnej pre príslušné obdobie,

  - m) v stĺpci „Dátum splatnosti“ sa uvádza dátum splatnosti dlhopisu v tvare d.m.rrrr,

  - n) v stĺpci „Dátum – valuta“ sa uvádza dátum vyrovnania obchodu v tvare d.m.rrrr,

  - o) v stĺpci „Protistrana“ sa uvádza názov protistrany, s ktorou bol vykonaný nákup alebo predaj dlhopisu; názov protistrany sa uvádza vo forme SWIFT kódu, ak protistrana nemá SWIFT kód, uvádza sa obchodné meno a sídlo.

- 18. V časti s názvom „Ostatné cenné papiere“

  - a) v stĺpci „ID obchodu“ sa uvádza identifikácia obchodu vnútorným alfanumerickým kódom,

  - b) v stĺpci „Typ“ sa uvádza kód príslušného typu cenného papiera, ktorý sa vyberá zo zoznamu prípustných kódov číselníka s názvom DRUH CENNÉHO PAPIERA, ktorý sa nachádza v APS STATUS DFT/C. Číselníky/C.7 Číselníky kódov,

  - c) v stĺpci „Nákup/predaj“ sa uvádza „N“ pre nákup alebo „P“ pre predaj,

  - d) v stĺpci „ISIN“ sa uvádza číselný kód emisie cenného papiera,

  - e) v stĺpci „Emitent“ sa uvádza názov subjektu, ktorý vydal cenný papier,

  - f) v stĺpci „Počet kusov“ sa uvádza počet kusov cenných papierov, ktoré boli kúpené do majetku fondu alebo predané z majetku fondu,

  - g) v stĺpci „Mena“ sa uvádza kód meny podľa medzinárodných štandardov ISO 4217, kód príslušnej meny sa vyberá zo zoznamu prípustných kódov číselníka MENA, ktorý sa nachádza v APS STATUS DFT/C. Číselníky/C.7 Číselníky kódov,

  - h) v stĺpci „Cena/ks v CM “ sa uvádza nákupná alebo predajná cena za jeden kus cenného papiera v cudzej mene; ak bola uskutočnená transakcia v slovenskej mene, uvádza sa „0“,

  - i) v stĺpci „Cena/ks v Sk“ sa uvádza nákupná alebo predajná cena za jeden kus cenného papiera v slovenskej mene alebo protihodnota v slovenskej mene,

  - j) v stĺpci „Objem obchodu spolu v CM“ sa uvádza celkový objem transakcie v cudzej mene; ak bola uskutočnená transakcia v slovenskej mene, uvádza sa „0“,

  - k) v stĺpci „Objem obchodu spolu v Sk“ sa uvádza celkový objem transakcie v slovenskej mene alebo protihodnota v slovenskej mene,

  - l) v stĺpci „Sadzba v %“ sa uvádza úroková sadzba, na ktorú cenný papier znie; pri variabilnej úrokovej sadzbe sa uvádza hodnota úrokovej sadzby, ktorá je súčtom jej fixnej a variabilnej zložky platnej pre príslušné obdobie,

  - m) v stĺpci „Dátum splatnosti“ sa uvádza dátum splatnosti cenného papiera v tvare d.m.rrrr,

  - n) v stĺpci „Dátum – valuta“ sa uvádza dátum vyrovnania obchodu v tvare d.m.rrrr,

  - o) v stĺpci „Bloomberg ticker/Reuters RIC“ sa uvádza kód cenného papiera zo systému Bloomberg alebo Reuters,

  - p) v stĺpci „Protistrana“ sa uvádza názov protistrany, s ktorou bol vykonaný nákup alebo predaj cenného papiera; názov protistrany sa uvádza vo forme SWIFT kódu, ak protistrana nemá SWIFT kód, uvádza sa obchodné meno a sídlo.

Použité skratky |

skratka | opis

Čís. r. | číslo riadka

Sk | slovenské koruny

CM | cudzia mena

TV | termínovaný vklad

ks | kus

NBS | Národná banka Slovenska

APS | Aplikačný programový systém

ISIN | číselný kód emisie cenného papiera

ID | identifikačný kód
