Príloha č. 3 k výnosu č. MF/016332/2010-132

- Štandard pre elektronické formuláre

  - 1. Definícia základných pojmov pre elektronické formuláre

  - 1.1 Formulár

  - 1.1.1 Formulárom sa označujú tlačivá v listinnej podobe alebo neštruktúrované elektronické dokumenty vo formátoch PDF, RTF, ODF a podobne, reprezentujúce tieto tlačivá. Formulár má predpísanú formu a náležitosti, ktoré definuje osobitný predpis alebo gestor služby, ktorá ho používa.

  - 1.1.2 Formulár je:

    - a) tlačivo v listinnej podobe,

    - b) textový súbor podľa § 19, ktorý umožňuje zverejnenie písomného tlačiva v elektronickej forme a jeho následné vytlačenie,

    - c) taký štruktúrovaný elektronický dokument, ktorý nespĺňa všetky vlastnosti pre elektronický formulár podľa bodu 1.2.

  - 1.1.3 Formulár podľa bodu 1.1.2 písmena a) sa používa najmä na poskytovanie a výmenu informácií medzi používateľom služby a gestorom služby. Formulár podľa bodu 1.1.2 písm. b) a c) sa používa najmä na jednosmernú elektronickú komunikáciu medzi používateľom služby a gestorom služby.

  - 1.1.4 Formulár podľa bodu 1.1.2 písm. b) a c) dodržiava príslušné požiadavky podľa § 18 až 24.

  - 1.2 Elektronický formulár

  - 1.2.1 Elektronický formulár slúži na obojsmernú výmenu informácií v elektronickej forme medzi používateľom služby a gestorom služby v predpísanej forme.

  - 1.2.2 Základ elektronického formulára tvorí XML štruktúra, reprezentujúca informačný obsah elektronického formulára. Elektronický formulár umožňuje vyplnenie údajov prostredníctvom elektronických prostriedkov, ich uchovanie v štruktúrovanej elektronickej forme, zobrazovanie a ich automatizované spracovanie v informačných systémoch.

  - 1.2.3 Elektronický formulár je možné:

    - a) vytlačiť ako predlohu na manuálne vyplnenie (perom, písacím strojom a podobne),

    - b) elektronicky vyplniť, vykonať elektronickým formulárom definované kontroly a následne vyplnený elektronický formulár vytlačiť,

    - c) elektronicky vyplniť, vykonať elektronickým formulárom definované kontroly, elektronicky podpísať, elektronicky odoslať a ďalej následne spracovať v ňom uchované údaje.

  - 1.3 Podanie

  - 1.3.1 Podanie je proces komunikácie používateľa služby s gestorom služby. Predmetom podania je používateľom vyplnený formulár alebo elektronický formulár a ďalšie s ním súvisiace procesné náležitosti a prílohy definované osobitnými predpismi.

  - 1.4 Elektronické podanie

  - 1.4.1 Elektronickým podaním je elektronický spôsob realizácie podania, pričom všetky kroky podania vykonané používateľom služby sa musia uskutočniť elektronickými prostriedkami. Elektronické podanie sa realizuje prostredníctvom elektronického formulára.

  - 2. Náležitosti elektronického formulára

  - 2.1 Základné požiadavky

  - 2.1.1 Náležitosti elektronického formulára spĺňajú požiadavky podľa bodov 2.2 až 2.9. Pre všetky náležitosti elektronického formulára existuje úplná dokumentácia, zverejnená spolu s príslušným elektronickým formulárom, ktorá umožní splnenie požiadaviek podľa § 6 ods.1 zákona.

  - 2.2 Identifikačné údaje elektronického formulára

  - 2.2.1 Identifikačné údaje elektronického formulára vymedzujú základné informácie o elektronickom formulári a jeho použití. Sú to tieto údaje:

    - a) názov,

    - b) identifikátor elektronického formulára, ktorý je jedinečný v rámci elektronickej verejnej správy v Slovenskej republike,

    - c) krátky popis účelu elektronického formulára,

    - d) gestor služby,

    - e) verzia,

    - f) platnosť, ktorá obsahuje dátum stanovujúci začiatok platnosti, a ak ide o elektronické formuláre so skončenou platnosťou aj dátum skončenia platnosti.

  - 2.3 Dátová štruktúra

  - 2.3.1 Dátová štruktúra elektronického formulára predstavuje predlohu elektronického formulára bez vyplneného dátového obsahu (ďalej len „prázdny formulár“), a to na základe popisu dátových polí. Vyplnením jednotlivých dátových polí vzniká vyplnený elektronický formulár (ďalej len „vyplnený formulár“), ktorý je možné ďalej elektronicky spracovávať.

  - 2.3.2 Dátová štruktúra je definovaná prostredníctvom XML Schema Definition Language (XSD) a určuje vlastnú dátovú štruktúru elektronického formulára, povolené typy a hodnoty jednotlivých dátových polí a ich informačný význam.

  - 2.4 Dátový obsah

  - 2.4.1 Dátový obsah definuje požadovaný informačný obsah elektronického formulára, ktorý sa viaže ku konkrétnemu úkonu. Dátový obsah elektronického formulára je založený na príslušnej dátovej štruktúre dátových prvkov podľa § 43.

  - 2.5 Prílohy

  - 2.5.1 Súčasťou dátového obsahu môže byť aj zoznam príloh, ktoré sú vyžadované podľa dátovej štruktúry elektronického formulára. Vlastná dátová štruktúra danej prílohy elektronického formulára však nie je súčasťou dátovej štruktúry elektronického formulára.

  - 2.5.2 Prílohy dodržiavajú príslušné požiadavky podľa § 18 až 24.

  - 2.6 Kontroly dátového obsahu

  - 2.6.1 Dátový obsah elektronického formulára môže obsahovať dodatočné kontroly okrem rámca kontrol zabezpečovaných prostredníctvom XSD. Dodatočné kontroly zabezpečujú overovanie požadovanej integrity údajov, vzájomné väzby v jednotlivých dátových poliach a podobne.

  - 2.6.2 Dodatočné kontroly sa môžu týkať iba vzájomných vzťahov a dátových polí daného elektronického formulára. Nie je možné definovať kontroly, vyžadujúce údaje z externých registrov, databáz a iných dátových zdrojov, nachádzajúcich sa mimo vlastnej dátovej štruktúry elektronického formulára.

  - 2.6.3 Pre všetky kontroly sa zverejňuje aj ich úplná dokumentácia.

  - 2.7 Prezentácia

  - 2.7.1 Prezentácia elektronického formulára predstavuje formálny predpis, ktorým je možné dátovú štruktúru a dátový obsah elektronického formulára transformovať do vizualizácie alebo inej požadovanej formy prezentácie, prístupnej aj zdravotne postihnutým používateľom služby.

  - 2.7.2 Prezentácia elektronického formulára je definovaná prezentačnou schémou.

  - 2.7.3 Prezentačná schéma popisuje presný spôsob transformácie dátovej štruktúry a dátového obsahu elektronického formulára do predpísanej prezentačnej formy pomocou štandardných formulárových blokov, ktoré jednoznačne definujú umiestnenie informácií v elektronickom formulári najmä informácie o fyzickej osobe ako používateľovi služby, informácie o gestorovi služby a podobne. Prezentačná schéma stanovuje spôsob zobrazenia jednotlivých dátových polí, ako aj identifikačných údajov. Prezentačná schéma tiež určuje navigáciu používateľa služby pri vypĺňaní jednotlivých dátových polí elektronického formulára.

  - 2.7.4 Z hľadiska prezentácie možno elektronický formulár zobrazovať ako prázdny formulár alebo ako vyplnený formulár.

  - 2.7.5 Pre konkrétny elektronický formulár je možné definovať viac povolených prezentačných schém. Tie určujú predpísaný spôsob prezentovania formulára pre rôzne technologické prostredia, ktoré sa používajú na prácu s elektronickými formulármi, pričom je možné použiť aj špecializovaný prostriedok podporujúci konkrétny typ prezentačnej schémy.

  - 2.7.6 Ak elektronická služba verejnej správy počas ďalšieho spracovania vyžaduje podpísanie elektronického formulára zaručeným elektronickým podpisom, prezentačná schéma, použitá pri podpisovaní sa uvádza vo vytvorenom elektronickom podpise.

  - 2.7.7 Pre každú schválenú prezentačnú schému sa zverejňuje aj úplná dokumentácia prezentačnej schémy.

  - 2.7.8 Prezentačná schéma dodržiava príslušné požiadavky podľa § 14 a § 19 až 24 a pri použití elektronického podpisu aj podľa osobitného predpisu.<sup>4</sup>)

  - 2.8 Kód elektronického formulára

  - 2.8.1 Každý vyplnený elektronický formulár obsahuje kód, ktorý umožňuje jednoznačnú identifikáciu dátového obsahu konkrétneho vyplneného elektronického formulára. Kód elektronického formulára je súčasťou vytlačenej podoby elektronického formulára.

  - 2.9 Doplňujúce informácie

  - 2.9.1 Doplňujúce informácie sú informácie, ktoré nie sú nutné pre správnu definíciu alebo prezentáciu príslušného elektronického formulára, ale môžu napomôcť pri pochopení významu jednotlivých častí elektronického formulára, spôsobu jeho použitia a spracovania. Medzi doplňujúce informácie patrí najmä nápoveda, legenda, vzory a príklady.

  - 3. Organizačné zabezpečenie

  - 3.1 Tvorbu elektronických formulárov a zabezpečenie ich správnosti zaisťuje gestor služby.

  - 3.2 Tvorbu a určenie štruktúry identifikátorov elektronických formulárov a určenie štruktúry kódov elektronických formulárov zabezpečuje ministerstvo.
