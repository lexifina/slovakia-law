Príloha č. 6 k vyhláške č. 78/2020 Z. z.

- Štandard architektúry cloud computingu

  - 1. Delenie funkcionálnych vrstiev

    - 1.1 Architektúra cloud computingu sa skladá z funkcionálnych vrstiev, ktorými sú vrstva dopytu, vrstva poskytovania cloudových služieb a vrstva dodávania zdrojov.

      - 1.1.1 Vrstva dopytu riadi katalóg opisujúci cloudové služby dostupné pre odberateľov cloudových služieb a zabezpečuje validitu ich vzájomného mapovania podľa dohody o poskytovanej úrovni cloudových služieb.

      - 1.1.2 Vrstva poskytovania cloudových služieb riadi cloudové služby a ich kompozície na základe požiadaviek vrstvy dopytu a dostupnosti vrstvy dodávania cloudových služieb s cieľom zabezpečiť súlad s dohodou o poskytovanej úrovni cloudových služieb.

      - 1.1.3 Vrstva dodávania zdrojov poskytuje jednotné rozhranie pre ľubovoľné hardvérové zdroje, zabezpečuje riadenie zdrojov, optimalizuje a monitoruje využitie prostriedkov z dispozičných zdrojov.

    - 1.2 Vrstva poskytovania cloudových služieb a vrstva dodávania zdrojov sa môže v architektúre cloud computingu nachádzať aj viackrát.

  - 2. Vrstva dopytu

    - 2.1 Vrstva dopytu sa skladá najmä z modulu prístupu ku cloudovým službám, modulu manažmentu používateľov a prístupových práv, modulu pre dodržiavanie definovanej úrovne služieb, modulu manažmentu objednávok a modulu katalógu cloudových služieb.

      - 2.1.1 Modul prístupu ku cloudových službám je unifikovaným webovým používateľským rozhraním, poskytujúcim prezentačnú funkciu najmä katalógu cloudových služieb podľa jednotlivých rolí používateľov tohto modulu.

      - 2.1.2 Modul manažmentu používateľov a prístupových práv

        - a) zabezpečuje riadenie prístupu jednotlivých používateľov, vrátane administrátorov, a to najmä ich identifikáciu, autentifikáciu a autorizáciu,

        - b) spravuje riadenie životného cyklu používateľských účtov, najmä ich vytváranie, modifikovanie a zrušenie.

      - 2.1.3 Modul pre dodržiavanie definovanej úrovne služieb zabezpečuje správu požiadaviek pre vytváranie dohody o poskytovaní cloudových služieb.

      - 2.1.4 Modul manažmentu objednávok

        - a) prijíma objednávky na operácie spojené s cloudovými službami,

        - b) potvrdzuje správnosť objednávky v súlade s dohodou o poskytovanej úrovni cloudových služieb,

        - c) rozkladá objednávku do adekvátnych služieb a ich atribútov na základe katalógu cloudových služieb,

        - d) rozhoduje, ktoré cloudové služby sú poskytované tou-ktorou konkrétnou vrstvou, ak existujú viaceré vrstvy poskytovania cloudových služieb,

        - e) preposiela požiadavky na služby do vrstvy poskytovania cloudových služieb,

        - f) poskytuje informácie o stave objednávky a iniciuje nápravu v prípade zlyhania realizácie objednávky,

        - g) využíva katalóg cloudových služieb pre rozhodnutia, ktoré cloudové služby môžu byť ponúkané jednotlivému používateľovi.

      - 2.1.5 Modul katalógu cloudových služieb

        - a) spravuje katalóg cloudových služieb, ktorý obsahuje informácie najmä o ponúkaných cloudových službách a ich možných kompozíciách, o dohodnutých podmienkach ako napríklad cene, špecifických atribútoch cloudových služieb, ktoré zabezpečujú dohodnuté podmienky, o mapovaní oprávnení používateľov k objednávaniu konkrétnych cloudových služieb a o objednaných cloudových službách,

        - b) priraďuje konkrétne charakteristiky z dohody o poskytovanej úrovni cloudových služieb ku konkrétnym cloudovým službám a obsahuje opis objednávkových a eskalačných procedúr, podmienok technickej podpory, špecifických zvýhodnení a podobne.

    - 2.2 Vrstva dopytu môže byť rozšírená o ďalšie logické moduly, napríklad o modul manažmentu ponuky cloudových služieb, modul modelovania dopytu, modul vytvárania správ o využívaní cloudových služieb, modul fakturácie a vyhodnocovania a modul kvalitatívnych referencií využívaných cloudových služieb.

  - 3. Vrstva poskytovania cloudových služieb

    - 3.1 Vrstva poskytovania cloudových služieb sa skladá najmä z modulu spracovania požiadaviek a aktivácie a deaktivácie cloudových služieb, modulu repozitára modelu cloudových služieb, modulu modelovania a návrhu cloudových služieb, modulu realizácie cloudových služieb, modulu monitorovania cloudových služieb, modulu manažmentu stavu cloudových služieb a modulu využívania cloudových služieb.

      - 3.1.1 Modul spracovania požiadaviek a aktivácie a deaktivácie cloudových služieb

        - a) spracováva požiadavky z modulu manažmentu objednávok na základe dohody o poskytovanej úrovni cloudových služieb, dostupnosti zdrojov a konfiguračného modelu cloudových služieb,

        - b) vytvára požiadavky pre vrstvu dodávania zdrojov ohľadom aktivácie a deaktivácie cloudových služieb,

        - c) rozhoduje na základe príslušných politík o zvolení adekvátnej vrstvy, ak viaceré vrstvy dodávania zdrojov spĺňajú kritériá na vybavenie požiadavky,

        - d) riadi aktiváciu a deaktiváciu cloudových služieb na základe príslušných pracovných postupov, ktoré synchronizujú nasadzovanie všetkých komponentov cloudovej služby s transakčnou konzistenciou,

        - e) zapisuje stav cloudovej služby do modulu repozitára modelu cloudových služieb,

        - f) iniciuje nápravné kompenzácie pri zlyhaní spracovania požiadaviek.

      - 3.1.2 Modul repozitára modelu cloudových služieb

        - a) definuje konfiguračné šablóny a atribúty cloudovej služby, pracovné postupy pre aktiváciu a deaktiváciu cloudovej služby,

        - b) definuje hierarchiu cloudových služieb, zachytáva stavy cloudových služieb v reálnom čase a zabezpečuje mapovanie medzi cloudovými službami a potrebnými zdrojmi.

      - 3.1.3 Modul modelovania a návrhu cloudových služieb

        - a) špecifikuje cloudové služby z pohľadu implementačných detailov a definuje informácie potrebné pre modul repozitár modelu cloudových služieb,

        - b) navrhuje vhodné šablóny cloudových služieb a pracovných postupov s cieľom automatizácie riadenia životného cyklu cloudových služieb.

      - 3.1.4 Modul realizácie cloudových služieb

        - a) konfiguruje virtuálnu infraštruktúru pre realizáciu cloudovej služby na základe informácií z modulu repozitára modelu cloudových služieb,

        - b) realizuje cloudovú službu,

        - c) implementuje možnosť zmeny realizácie cloudovej služby bez nutnosti jej opätovnej aktivácie,

        - d) komunikuje s vrstvou dodávania zdrojov s cieľom využitia špecifických atribútov zdrojov pri realizácii cloudovej služby,

        - e) overuje a pripravuje všetky parametre aktivácie a realizuje cloudovú službu.

      - 3.1.5 Modul monitorovania cloudových služieb

        - a) konfiguruje monitorovanie cloudových služieb, ktoré nasledujú po aktivácii cloudovej služby,

        - b) zhromažďuje udalosti a informácie o výkone v reálnom čase pre modul manažmentu stavu cloudových služieb.

      - 3.1.6 Modul manažmentu stavu cloudových služieb

        - a) spravuje monitorovanie cloudových služieb a prezentuje jeho výstupy vo forme prehľadov o stave cloudovej služby,

        - b) ukladá a koreluje udalosti na úrovni cloudových služieb a podľa potreby ich eskaluje do obslužných procesov.

      - 3.1.7 Modul využívania cloudových služieb zbiera informácie o využívaní a meraní realizácie cloudovej služby a spracováva ich dávkovo alebo v reálnom čase pre každého odberateľa cloudovej služby.

    - 3.2 Vrstva poskytovania cloudových služieb môže byť rozšírená o ďalšie logické moduly, napríklad o modul modelovania kapacít.

  - 4. Vrstva dodávania zdrojov

    - 4.1 Vrstva dodávania zdrojov sa skladá najmä z modulu katalógu zdrojov, modulu manažmentu životného cyklu zdrojov, modulu modelovania kapacít zdrojov, modulu návrhu šablón zdrojov, modulu realizácie prideľovania zdrojov, modulu monitorovania využívania zdrojov, modulu stavu zdrojov a modulu adaptéra zdrojov a kontroly.

      - 4.1.1 Modul katalógu zdrojov

        - a) poskytuje unifikované informácie o zdrojoch, obsahujúce typy ich kompozícií,

        - b) v reálnom čase poskytuje informácie zachytené modulmi pre modelovanie kapacít a stavov zdrojov,

        - c) v reálnom čase riadi vyváženie zaťaženia zdrojov na základe stavu zdrojov,

        - d) zabezpečuje mapovanie modelov poskytovania služieb na zdroje,

        - e) poskytuje funkciu riadenia životného cyklu využívaných softvérových licencií.

      - 4.1.2 Modul manažmentu životného cyklu zdrojov

        - a) prijíma požiadavky z vrstvy poskytovania cloudových služieb a alokuje potrebné zdroje,

        - b) prijíma požiadavky na kapacity a výkon z modulu modelovania kapacít zdrojov a modulu návrhu šablón zdrojov,

        - c) prijíma informácie dostupnosti nových zdrojov a odosiela ich do vrstvy poskytovania cloudových služieb,

        - d) určuje potrebný počet a typy zdrojov na základe požiadavky na kapacitu cloudovej služby,

        - e) riadi spotrebu zdrojov a modul monitorovania využívania zdrojov,

        - f) riadi zdroje s ohľadom na záťaž cloudovej služby a manažuje rozdeľovanie záťaže v reálnom čase s preddefinovanou logikou.

      - 4.1.3 Modul modelovania kapacít zdrojov

        - a) slúži na prognózovanie využívania zdrojov a poskytuje informácie o kapacitách a výkonnosti zdrojov, a to v reálnom čase a v historickom spracovaní,

        - b) zabezpečuje koordináciu modulov vrstvy dodávania zdrojov s ohľadom na prideľovanie zdrojov, manažment záťaže a monitorovanie pre modelovanie požiadaviek na dodávku,

        - c) zabezpečuje priraďovanie požiadaviek na zdroje s dostupnými zdrojmi v module katalógu zdrojov a podľa potreby vytvára informácie pre obstarávanie dodatočných prostriedkov.

      - 4.1.4 Modul návrhu šablón zdrojov

        - a) je zodpovedný za návrh zdrojov infraštruktúry a modifikácie špecifických typov zdrojov na základe využívaných cloudových služieb,

        - b) je zodpovedný za návrh pracovných postupov pre modul manažmentu životného cyklu zdrojov, vrátane návrhu konfigurácie zdrojov, ich nasadzovania, manažmentu zaťaženia a automatizácie špecifických alebo všeobecných cloudových služieb,

        - c) poskytuje návrhy pre modul katalóg zdrojov,

        - d) navrhuje metriky pre modul manažmentu životného cyklu zdrojov na monitorovanie stavu prostriedkov.

      - 4.1.5 Modul realizácie prideľovania zdrojov

        - a) prijíma informácie o kapacitných konfiguráciách zdrojov z modulu manažmentu životného cyklu prostriedkov,

        - b) zabezpečuje mapovanie informácií o konfiguráciách zdrojov pre modul katalógu zdrojov,

        - c) riadi alokáciu a konfiguráciu zdrojov pomocou modulu adaptéra zdrojov a kontroly.

      - 4.1.6 Modul monitorovania využívania zdrojov

        - a) monitoruje zmeny spotreby a využívania zdrojov, špecifických pre konkrétnu službu alebo odberateľa cloudových služieb, s využitím modulu manažmentu životného cyklu zdrojov,

        - b) monitoruje dostupnosť a úroveň využívania zdrojov a informuje modul manažmentu životného cyklu zdrojov o ich skutočnom alebo predpokladanom preťažení.

      - 4.1.7 Modul stavu zdrojov

        - a) poskytuje modulu manažmentu stavu cloudových služieb informácie o zlyhaniach a chybách zdrojov, ktoré môžu potenciálne ovplyvniť kvalitu poskytovania cloudových služieb,

        - b) sleduje a spracováva chybové stavy zdrojov a pri výskyte chyby iniciuje proces nápravy,

        - c) udržuje v reálnom čase dostupné agregované správy riadenia udalostí ohľadom dostupnosti zdrojov a ich zlyhaní.

      - 4.1.8 Modul adaptéra zdrojov a kontroly

        - a) poskytuje funkciu inteligentného virtualizačného prostredia, ktoré na základe typu hardvéru prekladá abstraktné výkonné operácie do konkrétnych inštrukcií, ktoré daný hardvér dokáže spracovať,

        - b) transformuje požiadavky na pridelenie zdrojov na skutočné zdroje,

        - c) v reálnom čase poskytuje aktualizovaný stav a informácie o využívaní konkrétneho hardvéru a softvéru pre modul katalógu zdrojov, modul monitorovania využívania zdrojov a modul stavu zdrojov.

    - 4.2 Vrstva dodávania zdrojov môže byť rozšírená o ďalšie logické moduly.
