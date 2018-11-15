Príloha č. 1 k výnosu č. 55/2014 Z. z.

- Doplňujúce štandardy prístupnosti webových stránok

  - 1. Predpisy určujúce typ písma obsahujú aj niektorý z generických fontov písma.

    - 1.1. Definícia typu písma, ktorým je napríklad atribút „font-family“ v kaskádových štýloch CSS, obsahuje aj uvedenie generického fontu. V rámci výpočtu jednotlivých typov písma sa generický font uvádza na poslednom mieste.

    - 1.2. Generickým fontom serifového (pätkového) písma, ktorým je napríklad Times New Roman, je „serif“, bezserifového (bezpätkového) písma, ktorými sú napríklad Arial alebo Verdana, je „sans-serif“ a neproporcionálneho písma, ktorým je napríklad Courier, je „monospace“.

  - 2. Pri uvádzaní hodnôt atribútov v značkovacom jazyku alebo vo vlastnostiach štýlov sa namiesto absolútnych jednotiek používajú relatívne jednotky. Veľkosť textu je možné zväčšovať a zmenšovať prostredníctvom štandardných funkcií prehliadača.

    - 2.1. Veľkosť písma sa na webových stránkach definuje len pomocou kľúčových slov CSS, ktorými sú xx-small, x-small, small, medium, large, x-large a xx-large alebo pomocou percent, hodnôt smaller, larger a jednotiek em a ex. Toto sa týka aj tabuliek.

    - 2.2. Veľkosť písma sa nedefinuje prostredníctvom jednotiek pt, pc, in, cm, mm a px.

    - 2.3. Umožňuje sa zväčšenie veľkosti textu do hodnoty 200 % bez straty obsahu alebo funkcionality, a to bez použitia asistenčných technológií; to sa nevzťahuje na titulky alebo text vo forme obrázku.

  - 3. Aktívne prvky, ktorými sú skripty, aplety a iné programové objekty sa poskytujú prístupne alebo sa zabezpečuje, že sú webové stránky použiteľné, aj keď sú aktívne prvky vypnuté alebo nie sú podporované. Ak to nie je možné, poskytujú sa ekvivalentné informácie na alternatívnej prístupnej webovej stránke.

    - 3.1. Skripty na webovej stránke sa poskytujú v súlade s platnými technikami prístupného použitia Javaskriptu podľa prílohy č. 10.

    - 3.2. Ak nie je možné vzhľadom na povahu poskytovaného obsahu, napríklad pri interaktívnych mapách, vytvoriť webovú stránku použiteľnú bez skriptov, použije sa prvok <noscript> s ekvivalentným textovým opisom alebo sa použije skript na strane servera namiesto skriptu na strane klienta alebo sa poskytne alternatívna prístupná webová stránka podľa bodu 11.4. Ak nie je možné z povahy poskytovaného obsahu vytvoriť úplný ekvivalentný textový opis, poskytuje sa prístupne čo najväčší rozsah poskytovaného obsahu, pričom na začiatku obsahu webovej stránky textové oznámenie, napríklad v znení „Pre správne fungovanie stránky povoľte Javascript vo Vašom prehliadači.“. Dôvodom na tento postup nesmie byť ozdobné grafické spracovanie a animácie textu a ovládacích prvkov.

    - 3.3. V HTML 5 sa aktívne prvky dopĺňajú o opatrenia, ktoré sú v súlade so špecifikáciou WAI-ARIA 1.0.

  - 4. Aktuálne otvorené okno sa nesmie vymeniť bez informovania používateľa.

    - 4.1. Textový opis odkazu je spravidla doplnený o upozornenie, že odkaz otvára nové okno.

  - 5. Cieľ každého odkazu sa jasne identifikuje. Označenie každého odkazu výstižne popisuje jeho cieľ nezávisle od okolitého kontextu. Odkazy sú jasne odlíšené od ostatného textu.

    - 5.1. Text odkazu je dostatočne zmysluplný a to tak, že dáva zmysel aj pri čítaní odkazu mimo kontext, či už samostatne alebo ako časť skupiny odkazov. Pre odkazy v plynulom texte postačuje zmysluplnosť z kontextu použitia v danom texte. Text odkazu je stručný a výstižný.

    - 5.2. V HTML sa píšu významovo výstižné informácie, napríklad „Informácia o verzii 4.3“ a nie „kliknite sem“. Pri odkaze s prázdnym textom sa cieľ odkazu bližšie špecifikuje pomocou informatívneho titulku odkazu, v HTML napríklad pomocou atribútu „title“.

    - 5.3. Označením odkazu sa rozumie kombinácia samotného textu odkazu, napríklad textu umiestneného medzi párové prvky <a> a atribútu „title“ týchto prvkov.

    - 5.4. Na odlíšenie textu odkazu sa nepoužíva len farba, ale aj napríklad podčiarknutie alebo iné zvýraznenie, a to najmä, ak je súčasťou ďalšieho textu.

    - 5.5. Účel každého odkazu je určiteľný len z textového označenia alebo z textových označení v kombinácii s jeho programovo určeným kontextom. Výnimkou je, ak nie je odkazu jednoznačný pre všetkých používateľov.

  - 6. Poskytujú sa informácie o celkovom rozložení webovej stránky. Pri opise rozloženia webovej stránky sa zvýrazňujú a vysvetľujú dostupné funkcie prístupnosti. Navigačné a obsahové informácie sú zreteľne oddelené.

    - 6.1. Ak webové sídlo obsahuje viac ako 50 uverejnených informačných webových stránok, poskytuje sa mapa webového sídla alebo jej ekvivalent.

    - 6.2. Mapa webového sídla alebo jej ekvivalent je dostupná z každej webovej stránky webového sídla.

    - 6.3. Webová stránka alebo webové sídlo sa vytvára tak, že je používateľ schopný rozpoznať, ktoré informácie slúžia k navigácii a ktoré patria k obsahu. Navigačné informácie, ako napríklad odkazy na iné webové stránky, sa správne umiestňujú v samostatnom oddelenom bloku. Odkazy v plynulom texte sa viditeľne odlišujú od ostatného textu; ich oddelenie od plynulého textu sa vyžaduje.

  - 7. Používateľ je vopred upozornený na odkaz, ktorý smeruje na obsah iného typu ako je webová stránka. Takýto odkaz je doplnený informáciou o type a veľkosti cieľového súboru.

    - 7.1. V HTML sa najmä pomocou atribútu „title“ prvku <a> alebo v bezprostrednej blízkosti prvku <a> v obsahu príslušnej webovej stránky uvádza informácia o type cieľového súboru (PDF, RTF) a o jeho veľkosti.
