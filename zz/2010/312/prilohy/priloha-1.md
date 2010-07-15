Príloha č. 1 k výnosu č. MF/016332/2010-132

- Štandardy prístupnosti webových stránok

  - Pravidlo 1. Poskytovanie ekvivalentných alternatív k zvukovému a vizuálnemu obsahu.

  - Poskytovanie obsahu, ktorý má používateľovi prezentovať tú istú funkciu alebo účel ako sluchovo alebo zrakovo vnímaný obsah.

    - 1.1 Ku všetkým „netextovým“ prvkom sa poskytuje textový ekvivalent. „Netextové“ prvky sú najmä obrázky, grafické náhrady textu vrátane symbolov, oblasti klikateľnej mapy, animácie, ako animované GIF-súbory a podobne, aplety a programové objekty, ASCII obrázky, rámy (frames), skripty, obrázky používané ako list bullets, tabulátory, grafické tlačidlá, zvuky prehrávané so zásahom alebo bez zásahu používateľa, samostatné zvukové súbory, zvukové stopy videa a video.

    - 1.1.1 V prvkoch ‹img›, ‹input› a ‹applet› sa používa atribút „alt“ alebo sa poskytuje textový ekvivalent pomocou obsahu prvkov ‹object› a ‹applet›.

    - 1.1.2 Pre komplexný obsah ako grafy a podobne, kde „alt“ text neposkytuje kompletný textový ekvivalent, sa poskytuje doplňujúci popis s použitím „longdesc“ a podobne v prvkoch ‹img› alebo ‹frame› odkaz v rámci prvku ‹object› alebo odkaz na popis.

    - 1.1.3 Pre klikateľné mapy sa v prvku ‹area› používajú atribúty „alt“ aj „title“ alebo sa pri prvku ‹map› použijú prvky ‹a› a ďalší text ako obsah.

    - 1.1.4 Ak obrázok neobsahuje žiadnu významovú informáciu a je použitý iba ako dekorácia, atribút „alt“ obsahuje prázdnu hodnotu. Ak však slúži na ovládanie webovej stránky a podobne, obsahuje zmysluplný obsah.

    - 1.1.5 Ak je obrázok použitý na odlíšenie, či webovú stránku ovláda človek, alebo počítač, používateľovi sú k dispozícii i také metódy, ktoré umožňujú toto odlíšenie uskutočniť napriek neschopnosti používateľa získať požadovanú grafickú informáciu z obrázka, napríklad zvukový výstup, doplňovanie bežného textu a podobne. Na odlíšenie človeka a počítača sa používa plne automatizovaný verejný Turingov test na rozlíšenie počítačov od ľudí, ktorým je metóda CAPTCHA a podobne.

    - 1.2 Pre každú aktívnu oblasť klikateľnej mapy na strane servera sa poskytujú doplnkové textové odkazy.

    - 1.2.1 Ak je použitie mapy nevyhnutné, nepoužívajú sa „server-side“ mapy, ale najmä „client-side“ mapy uvedené v bode 9.1.

    - 1.2.2 Aktívne časti na strane servera sa rovnako ako v bode 1.1 vhodne označujú.

    - 1.3 Ak dokáže agent používateľa automaticky čítať nahlas textový ekvivalent vizuálneho záznamu, poskytuje sa zvukový popis dôležitých informácií vizuálneho záznamu multimediálnej prezentácie.

    - Zvukový popis sa so zvukovou stopou synchronizuje v súlade s bodom 1.4.

    - 1.3.1 Ak webová stránka poskytuje informácie prostredníctvom multimediálneho prvku, ktorým môže byť vizuálny alebo zvukový záznam, a tento nie je iba alternatívou k existujúcemu textovému obsahu, je doplnený titulkami v textovej forme alebo iným textovým zápisom.

    - 1.4 Alternatívy ekvivalentné s multimediálnou prezentáciou, ako titulky alebo zvukové popisy vizuálneho záznamu, založenou na čase, napríklad film alebo animácia, sa s ňou synchronizujú.

    - 1.5 Ak agent používateľa interpretuje textové ekvivalenty pre odkazy klikateľných máp na strane klienta, poskytujú sa ďalšie textové odkazy pre všetky aktívne oblasti klikateľnej mapy na strane klienta.

    - 1.5.1 Používa sa v súlade s bodmi 1.2 a 9.1.

    - 1.6 Predpisy určujúce typ písma obsahujú aj bežný font písma.

    - 1.6.1 Definícia typu písma, ktorým je napríklad atribút „font-family“ v kaskádových štýloch CSS a podobne, obsahuje aj uvedenie bežného fontu. V rámci výpočtu jednotlivých typov písma sa bežný font uvádza na poslednom mieste.

    - 1.6.2 Bežné fonty pre serifové (pätkové) písmo, ktorým je napríklad Times New Roman, je „serif“, pre bezserifové (bezpätkové) písmo, ktorými sú napríklad Arial alebo Verdana, je „sans-serif“ a pre neproporcionálne písmo, ktorým je napríklad Courier, je „monospace“.

  - Pravidlo 2. Nespoliehanie sa len na farbu.

  - Texty a grafika si zachovávajú zrozumiteľnosť, aj keď sa zobrazia bez použitia farby.

    - 2.1 Zabezpečuje sa, aby boli všetky informácie prezentované pomocou farieb prístupné a zrozumiteľné aj bez farieb, a to z kontextu alebo pomocou zvýraznenia a podobne.

    - 2.1.1 Všetky informácie na webovej stránke sú rovnako prístupné i pri zapnutí inej farebnej schémy operačného systému, akú má štandardné nastavenie.

    - 2.2 Zabezpečuje sa, aby farebné kombinácie pozadia a popredia poskytovali dostatočný kontrast.

    - 2.2.1 Kombinácie farby popredia (písma a podobne) a farby alebo vzoru pozadia majú dostatočný vzájomný kontrast a na pozadí sa nevyskytuje vzorka, ktorá znižuje čitateľnosť.

  - Pravidlo 3. Používanie zvýrazňovania a štýlov a ich správne používanie.

  - Dokumenty sa zvýrazňujú pomocou vhodných štrukturálnych prvkov. Prezentácia sa ovláda najmä pomocou štýlov ako pomocou prezentačných prvkov a atribútov.

    - 3.1 Na prezentovanie informácií sa namiesto obrázkov uprednostňuje vhodný značkovací skript, ak existuje.

    - 3.1.1 Na zvýraznenie matematických rovníc sa používa MathML.

    - 3.1.2 Na formátovanie a rozloženie textu sa používajú štýly (style sheets), napríklad kaskádové štýly (CSS).

    - 3.1.3 Je nevhodné používať obrázky ako náhrady textu; používa sa text a štýly.

    - 3.2 Dokumenty sa vytvárajú v súlade s oficiálnou formálnou úpravou a gramatikou. Kód webových stránok zodpovedá niektorej zverejnenej finálnej špecifikácii jazyka HTML alebo XHTML a neobsahuje syntaktické chyby, ktoré je technický prevádzkovateľ alebo správca obsahu schopný odstrániť.

    - 3.2.1 Popis typu dokumentu webovej stránky sa zahrnie do úvodu dokumentu alebo inej časti, ktorý sa vzťahuje na uverejnené definície typov dokumentov, napríklad striktný HTML 4.01 Strict DTD, HTML 4.01 Transitional, XHTML 1.0 Strict.

    - 3.2.2 Validáciu s konkrétnymi špecifikáciami je vhodné uviesť na vstupnej webovej stránke aj vizuálne pomocou na to určených symbolov, ktoré sa dajú získať po ukončení validácie na adrese http://validator.w3.org/ alebo na inej adrese.

    - 3.3 Na riadenie vizuálneho rozloženia obsahu a prezentácie sa používajú štýly.

    - 3.3.1 Na riadenie štýlov písma sa v HTML namiesto prvku font> používajú možnosti fontu v CSS.

    - 3.4 Pri uvádzaní hodnôt atribútov v značkovacom jazyku alebo vo vlastnostiach štýlov sa namiesto absolútnych jednotiek používajú relatívne jednotky. Veľkosť textu možno zväčšovať a zmenšovať prostredníctvom štandardných funkcií prehliadača.

    - 3.4.1 Veľkosť písma sa na webových stránkach definuje len pomocou kľúčových slov CSS, ktorými sú xx-small, x-small, small, medium, large, x-large a xx-large alebo pomocou percent, hodnôt smaller, larger a jednotiek em a ex. Toto sa týka aj tabuliek.

    - 3.4.2 Veľkosť písma sa nedefinuje prostredníctvom jednotiek pt, pc, in, cm, mm a px.

    - 3.5 Na vyjadrenie štruktúry dokumentu sa používajú prvky hlavičky a používajú sa vhodne podľa ich špecifikácie.

    - 3.5.1 Nadpisy sa definujú pomocou značiek , ‹h2›... ‹h6›. Nie je vhodné definovanie nadpisov pomocou značky ‹font› alebo definovaním vlastnej triedy pre danú úroveň nadpisu. Pri použití značiek pre nadpisy sa dbá aj na správnu hierarchiu nadpisov.

    - 3.5.2 Sémantické značky ‹h1›, ‹h2›... ‹h6› sa v zdrojovom kóde nepoužívajú pre obsah, ktorý nezodpovedá ich významu. Znamená to, že prvky, ktoré netvoria nadpisy, sa takto neoznačujú.

    - 3.6 Zoznamy a ich jednotlivé položky sa označujú správne.

    - 3.6.1 V HTML sa na vyznačenie jednotlivých položiek zoznamu pri nečíslovanom zozname ‹li› používa značka ‹ul›, pri číslovanom zozname značka ‹ol›, a ak má zoznam definičný význam značka ‹dl›.

    - 3.6.2 Text, ktorý je vo svojej podstate zoznamom, sa označí ako zoznam.

    - 3.6.3 Prvky, ktoré netvoria zoznamy, sa v zdrojovom kóde takto neoznačujú.

    - 3.7 Citácie sa zvýrazňujú. Úvodzovky a ďalšie označenia určené na zvýraznenie citácie sa nepoužívajú na formátovací efekt, akým je odsadenie a podobne.

    - 3.7.1 V HTML sa na zvýraznenie krátkych a dlhších citácií používajú prvky ‹q› a ‹blockquote›.

    - 3.7.2

  - Pravidlo 4. Objasňovanie použitia pôvodného jazyka.

  - Označenie pôvodného jazyka prípadne jeho zmien uľahčuje výslovnosť alebo interpretáciu skratiek či cudzieho textu najmä pre pomocné technológie. Zároveň však zjednodušuje vyhľadávanie a identifikáciu dokumentov v požadovanom jazyku pomocou automatov a zlepšuje čitateľnosť obsahu pre všetkých používateľov.

    - 4.1 Zmeny pôvodného jazyka textu sa v dokumente a vo všetkých textových ekvivalentoch, ako sú titulky a podobne, zreteľne označujú.

    - 4.1.1 V HTML sa používa atribút „lang“.

    - 4.1.2 V XML sa používa atribút „xml:lang“.

    - 4.2 Celý význam každej skratky sa uvádza na mieste jej prvého použitia.

      - Vysvetlenie:

      - Uvedenie celého významu skratiek v tele dokumentu napomáha použiteľnosť dokumentu a zabraňuje nemožnosti správne interpretovať skratky pomocnými technológiami.

    - 4.2.1 V HTML sa v prvkoch ‹abbr› a ‹acronym› používa atribút „title“.

    - 4.3 Identifikuje sa pôvodný primárny jazyk webovej stránky. V zdrojovom kóde sa definuje hlavný jazyk obsahu webovej stránky.

    - 4.3.1 V jazyku HTML sa v prvku ‹html› používa atribút „lang“.

    - 4.3.2 V XML sa používa atribút „xml:lang“.

    - 4.3.3 Systémy sa nastavia tak, aby sa využila výhoda výmenného mechanizmu obsahu HTTP (internetová špecifikácia RFC2616, článok 14.12) a klienti mohli automaticky získať dokumenty v preferovanom jazyku.

    - 4.4 V metadátach sa uvádza použitá znaková sada.

    - 4.4.1 V HTML sa v prvku ‹head› používa atribút „content-type“.

    - 4.4.2 V XML sa používa atribút „encoding“.

  - Pravidlo 5. Tvorenie tabuliek, ktoré sa ľahko transformujú.

  - Preverí sa, či tabuľky sú dostatočne zvýraznené na účel ich transformácie pomocou prístupných prehliadačov alebo iných agentov používateľa.

    - 5.1 V dátových tabuľkách sa identifikujú hlavičky riadkov a stĺpcov. Obsahy buniek sa štrukturálne zhodujú s významom.

    - 5.1.1 V HTML sa na identifikovanie dátových buniek používa prvok ‹td› a na identifikovanie hlavičiek prvok ‹th›. Na rýchlejšiu identifikáciu tabuliek na webovej stránke možno využiť accessibility toolbary.

    - 5.1.2 Všetky tabuľky dávajú zmysel pri čítaní zľava doprava.

    - 5.1.3 Obsah, ktorý významovo patrí do jednej bunky, sa nachádza iba v jednej bunke. Ak významovo patrí do viacerých buniek, nachádza sa vo viacerých bunkách.

    - 5.2 Pre dátové tabuľky, ktoré majú dve alebo viac logických úrovní hlavičiek riadkov alebo stĺpcov, sa používa zvýraznenie vzťahov medzi dátovými bunkami a bunkami hlavičky.

    - 5.2.1 V HTML sa na zoskupenie hlavičiek riadkov používajú prvky ‹thead›, ‹tfoot› a ‹tbody› a na zoskupenie hlavičiek stĺpcov prvky ‹col› a ‹colgroup›.

    - 5.2.2 K popisu komplexnejších vzťahov medzi dátami sa používajú atribúty „axis“, „scope“ a „headers“.

    - 5.3 Tabuľka sa nepoužíva na vytvorenie vizuálneho rozloženia obsahu, ak nedáva zmysel v linearizovanej podobe. Ak tabuľka nedáva zmysel a nemožno sa jej vyhnúť, poskytuje sa alternatívny ekvivalent, ktorým môže byť aj linearizovaná verzia.

    - 5.3.1 Ak agent používateľa podporuje nastavenie pomocou štýlov, tabuľky sa na vizuálne rozloženie nepoužívajú.

    - 5.4 Ak sa tabuľka použije iba na vizuálne rozloženie obsahu, nepoužívajú sa žiadne štrukturálne označenia s cieľom vizuálneho formátovania.

    - 5.4.1 V HTML sa prvok ‹th› nepoužíva na to, aby bol obsah bunky zobrazený centrovane a napísaný tučným písmom a podobne.

    - 5.4.2 Zbytočne sa nedefinujú prvky na označenie hlavičky, päty a podobne, v HTML sú to napríklad prvky ‹tfoot› a ‹caption›.

    - 5.5 Vo všetkých tabuľkách sa uvádzajú zhrnutia.

    - 5.5.1 V HTML sa v prvku ‹table› používa atribút „summary“.

    - 5.6 Menovkám hlavičiek sa uvádzajú skratky.

    - 5.6.1 V HTML sa v prvku ‹th› používa atribút „abbr“.

  - Pravidlo 6. Zabezpečenie, aby sa webové stránky využívajúce nové technológie ľahko transformovali.

  - Zabezpečenie, aby boli webové stránky prístupné, aj keď nie sú novšie technológie podporované alebo sú vypnuté.

    - 6.1 Webové stránky sa organizujú tak, aby sa dali čítať aj bez použitia štýlov.

    - 6.1.1 Dokument v HTML možno prečítať, aj keď je interpretovaný bez asociovaného štýlu.

    - 6.1.2 Obsah je logicky zorganizovaný tak, aby bola jeho interpretácia zmysluplná, aj keď budú štýly vypnuté alebo nebudú podporované.

    - 6.2 V prípade zmeny dynamického obsahu sa zabezpečí aj aktualizácia ekvivalentov tohto obsahu.

    - 6.3 Zabezpečuje sa, aby sa webové stránky dali použiť, aj keď sú aktívne prvky, ktorými sú skripty, aplety a iné programové objekty, vypnuté alebo nie sú podporované. Ak to nie je možné, poskytujú sa ekvivalentné informácie na alternatívnej prístupnej webovej stránke.

    - 6.3.1 Zabezpečenie, aby napríklad odkazy, ktoré spúšťajú skripty, pracovali, aj keď sú tieto skripty vypnuté alebo nie sú podporované. JavaScript sa nepoužíva ako cieľ odkazu a podobne.

    - 6.3.2 Ak nemožno vytvoriť webovú stránku použiteľnú bez skriptov, poskytuje sa buď text ekvivalentný s prvkom ‹noscript›, alebo sa použije skript na strane servera namiesto skriptu na strane klienta, prípadne sa poskytne alternatívna prístupová webová stránka, ako je uvedené v bode 11.4.

    - 6.4 Zabezpečuje sa, aby boli obslužné programy skriptov a apletov nezávislé od vstupných zariadení.

    - 6.5 Zabezpečuje sa prístupnosť dynamického obsahu, prípadne sa poskytuje alternatívna prezentácia alebo webová stránka.

    - 6.5.1 V HTML sa napríklad na konci každého súboru rámov (frameset) použije prvok ‹noframes›. Skripty na strane servera môžu byť pri niektorých aplikáciách prístupnejšie ako skripty na strane klienta.

  - Pravidlo 7. Zabezpečenie riadenia zmien časovo citlivého obsahu používateľom.

  - Zabezpečenie toho, aby mohli byť pohyblivé, blikajúce, rolujúce či samoobnovovacie objekty alebo webové stránky zastavené alebo vypnuté.

    - 7.1 Ak agent používateľa neumožňuje používateľovi kontrolu nastavení kmitania, vyhýba sa použitiu kmitania.

    - 7.1.1 Prvky ‹blink› a ‹marquee› nie sú definované v žiadnej W3C HTML špecifikácii, a preto sa nepoužívajú.

    - 7.1.2 Prípadné použitie animácie alebo dynamicky sa meniacich prvkov sa trvale mení najviac s frekvenciou 1 Hz. To znamená, že jedna fáza dynamicky sa meniaceho obsahu sa zobrazuje aspoň 1 sekundu.

    - 7.2 Ak používateľom ich agent neumožňuje kontrolu blikania obsahu, zabráni sa tomu, aby obsah webovej stránky blikal. Prezentácia sa mení v pravidelných intervaloch, vypína sa, zapína sa a podobne.

    - 7.3 Ak agent používateľa neumožňuje používateľom „zamraziť“ multimediálny obsah, na webových stránkach sa vyhýba „pohybu“, akými sú flashové animácie, automaticky prehrávaný zvuk a podobne.

    - 7.3.1 Ak webová stránka obsahuje pohyblivý obsah, poskytuje sa v rámci skriptu alebo appletu mechanizmus, ktorý umožní používateľom „zamraziť“ pohyb a aktualizácie.

    - 7.3.2 Vytvorenie pohyblivých prvkov na webovej stránke pomocou použitia štýlov so skriptovaním umožňuje používateľom ľahšie vypnúť, či zrušiť tento efekt.

    - 7.3.3 Animácie sa nepoužívajú pri texte, ktorý slúži na zobrazenie dôležitých informácií.

    - 7.3.4 Ak sa audio na webovej stránke prehráva dlhšie ako tri sekundy, je k dispozícii prístupný a nezávislý mechanizmus, ktorý umožní audio dočasne alebo úplne zastaviť.

    - 7.4 Ak agent používateľa neposkytuje možnosť zastaviť obnovovanie, nie je vhodné vytvárať webové stránky, ktoré sa pravidelne samy obnovujú. Obsah sa mení len vtedy, ak používateľ aktivuje nejaký prvok.

    - 7.4.1 V HTML nie je vhodné vytvárať webové stránky tak, aby sa samy obnovovali pomocou metadátového prvku „HTTP-EQUIV=refresh“, ak agent používateľa neumožňuje používateľom tento prvok vypnúť.

    - 7.4.2 Pri pohybe na webovej stránke nemá pri bežnom nastavení nastať zmena určitej časti webovej stránky.

    - 7.5 Ak agent používateľa neposkytuje možnosť zastaviť automatické presmerovanie, nepoužíva sa nastavenie na automatické presmerovanie webovej stránky. Na vykonávanie presmerovania sa konfiguruje server.

  - Pravidlo 8. Zabezpečenie priamej prístupnosti vsadených rozhraní používateľa.

  - Zabezpečenie toho, aby používateľské rozhrania spĺňali princípy dizajnu prístupnosti – prístup k funkčnosti nezávislý od zariadenia, použiteľnosť klávesnice, hlasový výstup a podobne.

    - 8.1 Programové prvky, ako sú skripty a applety, sa robia priamo prístupné alebo kompatibilné s pomocnými technológiami. Nie je vhodné, aby obsah ani kód webovej stránky predpokladal, prípadne vyžadoval konkrétny spôsob použitia ani konkrétne vstupné alebo výstupné zariadenie. Ak to nie je možné, poskytuje sa prístupné alternatívne riešenie.

    - 8.1.1 Kód ani obsah webovej stránky nepredpokladá alebo nevyžaduje, aby mal používateľ konkrétny operačný systém, konkrétny prehliadač, aktívny zvukový výstup a podobne.

    - 8.1.2 Kód ani obsah nepredpokladá, že určité tlačidlá klávesnice alebo myši existujú a majú priradenú určitú funkciu, ako napríklad F5 na obnovenie webovej stránky, F1 na nápovedu a podobne.

    - 8.2.1 Všetky funkcie obsahu, ako aj všetky položky a aktívne prvky na webovej stránke možno obsluhovať a riadiť prostredníctvom klávesnice.

    - 8.2.2 Ak je presun na určitý prvok vykonateľný prostredníctvom klávesnice, je vykonateľný aj presun z daného prvku. Ak sú na tento presun potrebné iné klávesy, ako tabulátor s nezmenenou funkciou, šípky a podobne, je používateľ poučený o spôsobe presunu aktívneho zamerania mimo daného prvku.

    - 8.3.1 Pre každé používateľské rozhranie ovládané z klávesnice sa poskytuje viditeľné zameranie kurzora, a to najmä na identifikáciu aktívneho zamerania navigačných prvkov.

  - Pravidlo 9. Dizajnovanie nezávisle od zariadení.

  - Používanie vlastností, ktoré povoľujú aktiváciu prvkov webovej stránky pre čo možno najväčšie množstvo vstupných zariadení. Znamená to, že používateľ môže komunikovať so svojím agentom alebo dokumentom pomocou rôznych zariadení, ako sú myš, klávesnica, hlas a podobne. Textové ekvivalenty k obrázkom umožňujú interakciu bez použitia zariadenia na ukazovanie (myš) a zároveň webové stránky, ktoré povoľujú interakciu pomocou klávesnice, umožňujú prístupnosť aj cez hlasové ovládanie alebo pomocou príkazového rozhrania.

    - 9.1 Namiesto klikateľných máp na strane servera sa poskytujú klikateľné mapy na strane klienta okrem prípadov, keď sa oblasti nedajú definovať pomocou dostupného geometrického tvaru.

    - 9.2 Zabezpečí sa, aby každý prvok, ktorý má svoje vlastné rozhranie, mohol byť použitý spôsobom nezávislým od zariadení.

    - 9.3 Pri skriptoch sa uprednostňuje špecifikácia logických správcov udalostí pred správcami udalostí závislých od zariadení.

    - 9.4 Vytvára sa logické príkazové navádzanie pomocou odkazov, ovládačov formátu a objektov.

    - 9.4.1 V HTML sa logické zoradenie špecifikuje pomocou atribútu „tabindex“ alebo sa zabezpečí logický dizajn webovej stránky.

    - 9.5 K dôležitým odkazom vrátane tých, ktoré sa nachádzajú v klikateľných mapách na strane klienta, k ovládačom formátu a k skupinám ovládačov formátov sa poskytujú klávesové skratky.

    - 9.5.1 V HTML sa skratky špecifikujú pomocou atribútu „accesskey“ a podobne.

    - 9.5.2 Klávesové skratky sa nedefinujú pre každý odkaz, definujú sa len pre tie najdôležitejšie odkazy, inak si ich používatelia nezapamätajú.

    - 9.5.3 Pri definovaní klávesových skratiek sa vyhýba kolíziám s preddefinovanými klávesovými skratkami operačného systému alebo aplikácie. Takým je napríklad „D“, ktoré v Internet Exploreri v kombinácii ALT+D znamená vstup pre riadok Adresa.

  - Pravidlo 10. Používanie „dočasného“ riešenia.

  - Používanie dočasných riešení prístupnosti tak, aby mohli technológie a staršie prehliadače fungovať správne.

    - 10.1 Ak agent používateľa nedovoľuje používateľovi vypnúť vytváranie podradených okien, nepoužíva sa zjavovanie „pop-up“ či iných podobných okien a aktuálne otvorené okno sa nevymieňa bez toho, aby bol používateľ o tom informovaný.

    - 10.1.1 V HTML je potrebné vyhnúť sa použitiu rámu a podobných funkcií, ktorých cieľom je otvorenie nového okna.

    - 10.1.2 Textový popis odkazu je doplnený o upozornenie, že odkaz otvára nové okno.

    - 10.2 Ak agent používateľa nepodporuje jasné, explicitné priradenie menoviek a prvkov formulára, pre všetky prvky formulára s implicitne, priamo priradenými menovkami sa zabezpečí, aby bola každá menovka správne umiestnená.

      - Menovka predchádza priamo svojmu prvku v rovnakom riadku, čo umožňuje použiť viac ako jeden prvok a menovku na riadok, alebo sa nachádza v predchádzajúcom riadku, čo umožňuje použiť iba jednu menovku a jeden prvok na riadok.

    - 10.2.1 Prvkami formuláru sú editovateľné políčka, začiarkavacie políčka, prepínače, rozbaľovacie zoznamy alebo tlačidlá a podobne.

    - 10.3 Ak agent používateľa vrátane pomocných technológií neinterpretuje susediace texty správne, na aktuálnej alebo inej webovej stránke sa pre všetky tabuľky, ktoré zobrazujú text v paralelných stĺpcoch so zalamovaním slov, poskytuje alternatíva s jednoduchým lineárnym textom.

    - 10.4 Ak agent používateľa nedokáže správne spracúvať prázdne ovládacie prvky, v editovateľných políčkach a textových oblastiach sa uvádzajú prednastavené znaky, ktoré vymedzujú miesto.

    - 10.4.1 V HTML to platí pre prvky ‹textarea› a ‹input›.

    - 10.4.2 Znaky ako medzera a podobne, prekladače väčšinou ignorujú, a preto sa nepovažujú za také, ktoré vymedzujú miesto.

    - 10.5 Ak agent používateľa vrátane pomocných technológií nedokáže zreteľne odlíšiť susediace odkazy, medzi susediace odkazy sa uvádzajú neodkazové, vytlačiteľné znaky ohraničené medzerami.

    - 10.5.1 V HTML sa medzi prvkami ‹a› používajú bežné spojovacie slová, respektíve znaky abecedy a podobne.

  - Pravidlo 11. Používanie technológií a smerníc W3C.

  - Vhodné používanie W3C technológií a dodržiavanie smerníc prístupnosti je dôležitým základom prístupnosti. Tam, kde nemožno použiť technológiu W3C alebo jej použitie môže mať za následok netransformovateľný materiál, poskytuje sa alternatívna verzia príslušného obsahu.

    - 11.1 Ak sú dostupné a vhodné na určitú úlohu, používajú sa W3C technológie, a to ich čo možno najnovšie verzie.

    - 11.2 Vyhýba sa neschváleným vlastnostiam W3C technológií.

    - 11.2.1 V HTML sa nepoužíva neschválený prvok ‹font›. Namiesto toho sa používajú štýly, ako napríklad fontové vlastnosti CSS.

    - 11.3 Informácie sa poskytujú tak, aby používatelia mohli prijímať dokumenty podľa ich vlastných preferencií, akými sú napríklad jazyk a typ obsahu.

    - 11.3.1 Tam, kde je to možné, sa používa výmenný mechanizmus obsahu.

    - 11.4 Ak nemožno vytvoriť webovú stránku, ktorá je prístupná podľa týchto pravidiel, poskytuje sa odkaz na alternatívnu webovú stránku, ktorá je prístupná, má ekvivalentné informácie alebo funkčnosť a je aktualizovaná tak často ako pôvodná neprístupná webová stránka. To isté platí v prípade celého webového sídla.

    - 11.4.1 Poskytnutie webovej stránky alebo webového sídla iba v jednoduchej textovej podobe a podobne.

    - 11.4.2 Odkaz na alternatívnu webovú stránku sa sprístupňuje z každej pôvodnej neprístupnej webovej stránky a je viditeľne odlíšený od ostatného obsahu.

  - Pravidlo 12. Poskytovanie kontextových a orientačných informácií.

  - Poskytnutie kontextových a orientačných informácií tak, aby pomohli používateľom pochopiť komplexné webové stránky a jej prvky.

    - 12.1 Na umožnenie identifikácie rámov a ľahšej navigácie sa pre každý rám používa nadpis.

    - 12.1.1 Pre každý rám sa vhodne a zrozumiteľne zvolí názov, a to pomocou atribútu „name“, a jeho popisný titulok pomocou atribútu „title“. Popis vystihuje účel rámu a jeho vzťah k ďalšiemu rámu, prípadne ďalším rámom.

    - 12.2 Ak to nie je zrejmé z nadpisov jednotlivých rámov, uvádza sa účel rámov a ich vzájomných vzťahov.

    - 12.2.1 V HTML sa používa atribút „longdesc“, prvok ‹noframes› alebo odkaz na popis. Prvok ‹noframes› možno pre ostatných používateľov skryť pomocou kaskádových štýlov.

    - 12.3 Tam, kde je to prirodzené a vhodné, sa veľké bloky informácií rozdeľujú do viacerých, lepšie ovládateľných skupín.

    - 12.3.1 V HTML sa používa ‹optgroup› na zlúčenie prvkov ‹option› v rámci prvku ‹select›. Ovládače formátu sa zoskupujú pomocou prvkov ‹fieldset› a ‹legend›. Tam, kde je to vhodné, sa používajú vnorené zoznamy a na štruktúrovanie dokumentov sa používajú hlavičky a podobne.

    - 12.4 Menovky sa jasne spájajú s ovládačmi. Každý formulárový prvok má priradený výstižný názov.

    - 12.4.1 Prvkami formulára sú editovateľné políčka, začiarkavacie políčka, prepínače, rozbaľovacie zoznamy alebo tlačidlá a podobne.

    - 12.4.2 Aby každý používateľ vedel, čo má v danom prvku vyplniť alebo zvoliť, má každý použitý prvok svoj popis, v ktorom je jednoznačne uvedené, ako má používateľ s prvkom zaobchádzať.

    - 12.4.3 Pri definovaní jednotlivých prvkov formulára je ich popisný text zrozumiteľný a jednoznačne priradený, zviazaný pomocou prvku ‹label› a atribútov „for“ pre prvok ‹label› a „id“ pre formulárový prvok.

    - 12.4.4 Vizuálne umiestnenie popisného textu vedľa prvku formulára nie je dostačujúce.

    - 12.5.1 Ak je pri zadávaní textu alebo iného obsahu do príslušného vypĺňateľného prvku automaticky zistená chyba, chybná položka sa zreteľne označí a chyba je používateľovi popísaná vo forme textu.

  - Pravidlo 13. Poskytovanie prehľadného mechanizmu navigácie.

  - Poskytnutie prehľadného a úplného mechanizmu navigácie (orientačné informácie, navigačné panely, mapa webového sídla a podobne) je zamerané najmä na zvýšenie pravdepodobnosti, že každý na danom webovom sídle nájde to, čo tam hľadal.

    - 13.1.1 Text odkazu je dostatočne zmysluplný, aby dával zmysel aj pri čítaní odkazu mimo kontextu, či už samostatne, alebo ako časť skupiny odkazov. Pre odkazy v plynulom texte postačuje zmysluplnosť z kontextu použitia v danom texte. Text odkazu je stručný a výstižný.

    - 13.1.2 V HTML sa píšu významovo výstižné informácie, napríklad „Informácia o verzii 4.3“ a nie „kliknite sem“. Pri odkaze s prázdnym textom sa cieľ odkazu bližšie špecifikuje pomocou informatívneho titulku odkazu, v HTML napríklad pomocou atribútu „title“.

    - 13.1.3 Označením odkazu sa rozumie kombinácia samotného textu odkazu, napríklad textu umiestneného medzi párové prvky ‹a›, a atribútu „title“ týchto prvkov.

    - 13.1.4 Na odlíšenie textu odkazu sa nepoužíva iba farba, ale aj napríklad podčiarknutie alebo iné zvýraznenie, a to najmä, ak je súčasťou ďalšieho textu.

    - 13.1.5 Účel každého odkazu možno určiť iba z textového označenia alebo z textových označení v kombinácii s jeho programovo určeným kontextom. Výnimku tvorí prípad, keď je účel odkazu nejednoznačný pre všetkých používateľov.

    - 13.2 Poskytujú sa metadáta, pomocou ktorých sa webovým sídlam a ich jednotlivým webovým stránkam pridávajú významové (sémantické) informácie.

    - 13.2.1 Na identifikáciu autora dokumentu, typu obsahu a podobne sa používa RDF.

    - 13.2.2 Niektorí HTML agenti používateľa dokážu vytvoriť navigačné nástroje zo vzťahov dokumentu popísaných pomocou prvku ‹link› a atribútov „rel“ alebo „rev“, a to napríklad rel=„next“, rel=„previous“, rel=„index“.

    - 13.3.1 Ak webové sídlo obsahuje viac ako 50 uverejnených informačných webových stránok, poskytuje sa mapa webového sídla a podobne.

    - 13.3.2 Odporúča sa, aby bola mapa webového sídla alebo obsah prístupný z každej webovej stránky webového sídla.

      - b) Pri popisovaní rozloženia webovej stránky sa zvýrazňujú a vysvetľujú dostupné funkcie prístupnosti. Navigačné a obsahové informácie sú zreteľne oddelené.

    - 13.3.3 Webová stránka alebo webové sídlo sa vytvára tak, aby bol používateľ schopný rozpoznať, ktoré informácie slúžia na navigáciu a ktoré patria k obsahu. Navigačné informácie, ako napríklad odkazy na iné webové stránky, sa správne umiestňujú v samostatnom oddelenom bloku. Odkazy v plynulom texte sa viditeľne odlišujú od ostatného textu; ich oddelenie od ostatného textu sa nevyžaduje.

    - 13.4 Navigačné mechanizmy sú zrozumiteľné a používajú sa konzistentným spôsobom. Rovnako označené odkazy majú rovnaký cieľ.

    - 13.4.1 Navigácia je vytvorená jednoduchým a intuitívnym spôsobom, navigačné odkazy nie sú príliš dlhé.

    - 13.4.2 Pri výskyte viacerých navigačných informácií, ako napríklad dva druhy navigácie na dvoch miestach, má toto rozdelenie opodstatnenie a jasný význam.

    - 13.5 Na zvýraznenie a sprístupnenie navigačného mechanizmu sa poskytujú navigačné panely.

    - 13.6 Príbuzné odkazy sa spájajú do skupín a tieto skupiny sa pre agentov používateľa identifikujú. Ak to agenti používateľa umožňujú, uvedie sa aj spôsob, akým sa dá daná skupina preskočiť. Bloky obsahu, ktoré sa opakujú na viacerých webových stránkach, možno preskočiť.

    - 13.6.1 V úvode každej webovej stránky sa v prípade rozsiahlejšej webovej prezentácie alebo dlhého obsahu uvádza odkaz (prípadne odkazy s viacerými alternatívami prechodu), ktorý umožňuje preskočiť odkazy a bloky obsahu, a to pomocou hlavnej navigácie, menu a podobne. Rovnaký postup sa používa aj pre opakujúce sa obsahy na viacerých webových stránkach. Ide predovšetkým o odkazy, ako „prejsť na obsah“, „preskočiť navigáciu“, „skočiť na podmenu“ a podobne. V HTML sa v prvku ‹a› používa atribút „id“ a podobne.

    - 13.6.2 Uvedené odkazy môže tvorca webových stránok ukryť pred bežným vizuálnym zobrazovaním prostredníctvom kaskádových štýlov (CSS) a podobne. Na skrývanie týchto odkazov sa však nepoužíva predpis „display:none“ a „visibility:hidden“, pretože takto skrytý text pomocná technológia nemusí byť schopná interpretovať.

    - 13.7 Ak sú prítomné funkcie vyhľadávania, pre rôzne úrovne zručnosti a pre rôzne záujmy sa umožňujú rôzne druhy vyhľadávaní.

    - 13.7.1 Používa sa nielen jednoduché vyhľadávanie, ale aj možnosti nastavenia podrobnejšieho vyhľadávania podľa zadaných kritérií alebo filtrov.

    - 13.8 Na začiatku odsekov, kapitol, strán, zoznamov, samotnej webovej stránky a podobne sa umiestňujú zrozumiteľné informácie o kontexte obsahu.

    - 13.9 Poskytujú sa informácie o súvisiacich dokumentoch.

    - 13.9.1 Súvisiacimi dokumentmi sa rozumejú vnorené externé dokumenty, ako CSS a podobne, alebo dokumenty s rovnakým obsahom, ktorý je rozdelený na viac webových stránok, obvykle niekoľko webových stránok aktualít a podobne.

    - 13.9.2 Súvisiace dokumenty sa v HTML špecifikujú pomocou prvku ‹link› a atribútov „rel“ a „rev“ a podobne alebo sa poskytuje kolekcia všetkých dokumentov pomocou formátov na kompresiu súborov typu ZIP, TAR a GZIP s cieľom umožniť čítanie off-line.

    - 13.9.3 Pri formátoch na kompresiu súborov sa poskytuje informácia o ich obsahu.

    - 13.10 Poskytujú sa prostriedky umožňujúce preskočiť viacriadkové ASCII obrázky. ASCII obrázky, skratky a špecifické symbolické skratky sa sprístupňujú aj zrakovo postihnutým.

    - 13.10.1 V HTML sa pre nevýznamné ASCII obrázky používa najmä preskočenie ako v bode 13.6 alebo sa poskytne náhrada pomocou prvku ‹acronym› alebo ‹abbr› s atribútmi „title“ a podobne.

    - 13.10.2 Pri komplexnom ASCII umení sa preveruje adekvátnosť textového ekvivalentu.

    - 13.11.1 V HTML sa najmä pomocu atribútu „title“ prvku ‹a› uvádza informácia o type cieľového súboru (PDF, RTF a podobne) a o jeho veľkosti.

    - 13.12 Obsah ani kód webovej stránky nepredpokladá, že používateľ navštívil inú webovú stránku.

    - 13.12.1 Každá webová stránka funguje samostatne. V obsahu sa nevyskytuje kontext v zmysle „Ako ste videli na predchádzajúcej stránke“ alebo „Vyplňte číslo, ktoré ste si prečítali na titulnej stránke“.

    - 13.13 Ak webové sídlo obsahuje viac ako dve vnorenia v hierarchii, čo znamená, že najmenej jedna kategória má aspoň jednu podkategóriu, každá webová stránka obsahuje odkaz na vyššiu úroveň v hierarchii webového sídla a odkaz na úvodnú webovú stránku.

    - 13.14 Webová stránka vo všeobecnosti nemanipuluje používateľským prostredím bez priameho príkazu používateľa.

    - 13.14.1 Vnútro samotného obsahu webovej stránky sa považuje za používateľské prostredie.

    - 13.14.2 Webová stránka neotvára bez príkazu nové okná, nemení svoju veľkosť a pozíciu okien, žiadnym spôsobom nemení ovládacie prvky prehliadača, nezakazuje alebo neobmedzuje posúvače (scrollbar), a to ani v rámoch, neobmedzuje použitie kontextových ponúk, histórie, navigačných tlačidiel ako Späť/Dopredu, nemení obsah obľúbených položiek, nenastavuje sa ako domovská webová stránka a podobne.

    - 13.14.3 Používateľ má vždy možnosť zobrazený obsah posúvať podľa potreby a dostať sa tak k časti obsahu, ktorá mu je skrytá.

    - 13.14.4 Zmena nastavenia určitej položky v používateľskom rozhraní nevyvoláva automatickú zmenu kontextu webovej stránky bez upozornenia používateľa.

    - 13.14.5 Zmena aktívneho zamerania kurzora nespôsobuje zmenu kontextu.

    - 13.15.1 V HTML obsahuje prvok ‹title› v časti ‹head› výstižný názov konkrétnej webovej stránky, ktorý popisuje jeho obsah, zmysel alebo funkcionalitu, a to aj v súlade s celým webovým sídlom.

  - Pravidlo 14. Ubezpečenie sa, že dokumenty sú jasné a zrozumiteľné.

  - Zabezpečenie tohto pravidla je zamerané na ľahké pochopenie elektronických dokumentov a informácií (obsahu) v elektronickej podobe pre každého čitateľa.

    - 14.1 Webové stránky prezentujú informácie jednoduchým jazykom a zrozumiteľnou formou. Používa sa čo možno najjasnejší a najjednoduchší jazyk zodpovedajúci obsahu webovej stránky.

    - 14.1.1 Popisy odkazov a nadpisov dávajú zmysel aj vytrhnuté z kontextu. Použitie informatívnych nadpisov zrýchľuje prehľad o obsahu webovej stránky.

    - 14.1.2 Ucelená myšlienka sa uvádza tak, aby sa nachádzala v jednom obsahovom bloku.

    - 14.1.3 Používajú sa bežné slová, ako napríklad „začať“, ktoré je vhodnejšie ako „pristúpiť“. Použitie výrazov závisí aj od cieľovej skupiny čitateľov, teda od tých, ktorým je webová stránka určená.

    - 14.1.4 Vyhýba sa príliš komplikovaným a ťažko pochopiteľným skladbám vety.

    - 14.1.5 Je vhodné vyhýbať sa slangu, žargónu a špecializovanému významu slov, ak nie je v obsahu uvedené vysvetlenie.

    - 14.2 Text sa dopĺňa grafickými a zvukovými prezentáciami tam, kde uľahčia pochopenie webovej stránky.

    - 14.3 Štýl prezentácie sa vytvára tak, aby bol zhodný pre všetky webové stránky daného webového sídla.

    - 14.3.1 Minimalizuje sa množstvo použitých štýlov.

    - 14.3.2 Uprednostňuje sa použitie prepojených štýlov pred vnorenými štýlmi.

    - 14.3.3 Vo všetkých štýloch sa pre rovnaký koncept používa rovnaké meno triedy (atribút „class“).

    - 14.4 Úvodná webová stránka jednoznačne popisuje zmysel a účel webového sídla.

    - 14.4.1 Z úvodnej webovej stránky je zrejmé,

    - 14.4.1.1 o aký typ webovej prezentácie ide, čo je jej cieľom a uvádza sa jej názov, čo môže byť splnené aj uvedením názvu správcu obsahu, ak je to dostatočne výstižné,

    - 14.4.1.2 kto je jej technickým prevádzkovateľom; z úvodnej webovej stránky je rozpoznateľné, ktorej organizácii alebo inštitúcii webové sídlo patrí, teda, kto je jej správcom obsahu.
