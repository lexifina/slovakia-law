Príloha č. 2 k výnosu 312/2010 Z. z.

- Katalóg dátových prvkov

  - 1. Dátové prvky na popis osoby

    - D.1 Údaje o osobe (PersonData)

  - Základné atribúty | Hodnota

  - Dátový prvok | Údaje o osobe

  - Je súčasťou | Hlavný koreňový prvok (root element)

  - Má súčasti | Fyzická osoba Právnická osoba Identifikátor Fyzická adresa Telefónna adresa Internetová adresa

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | MF SR

  - Popisné atribúty | Hodnota

  - Názov | Údaje o osobe

  - Definícia | Zložený dátový prvok na rôzne informácie o osobe

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je PersonData

  - Hodnoty | Neobsahuje

    - Skrátená forma popisu súčastí dátového prvku Údaje o osobe (PersonData)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Fyzická osoba (D.1.1) | PhysicalPerson | Zložený dátový prvok na popis fyzickej osoby.

  - Právnická osoba (D.1.2) | CorporateBody | Zložený dátový prvok na popis právnickej osoby alebo subjektu, ktorý nie je právnickou osobou ani fyzickou osobou v zmysle právneho poriadku Slovenskej republiky. [Poznámky: Ak má fyzická osoba aj právnu formu, ktorou je najmä podnikateľ, možno využiť tento prvok na výmenu údajov, ktoré prvok Fyzická osoba neobsahuje (Právna forma a podobne). Vzhľadom na množstvo rôznych zahraničných organizácií nemožno ich vždy jednoznačne označiť ako právnické osoby. Tento prvok je určený aj na prenos takých údajov.]

  - Fyzická adresa (D.1.3) | PhysicalAddress | Zložený dátový prvok pre poštový kontakt. Atribúty: type

  - | type | Bližší popis kategórie adresy ako bydlisko, sídlo, ústredie. [Hodnoty: type=postOfficeBoxAddress Označuje, že adresa je P. O. BOX. type=streetAddress Označuje, že ide o bežnú fyzickú adresu príjemcu, ktorou nie je P. O. BOX. type=militaryAddress Označuje, že adresa sa riadi vojenským zaradením. type=undefined Označuje neznámy/neuvedený typ, rovnaký význam má úplné neuvedenie atribútu type.] [Poznámky: Uvádza sa kvôli rozlíšeniu typu adresy, tento atribút však nie je povinný.]

  - Telefónna adresa (D.1.4) | TelephoneAddress | Zložený dátový prvok pre telefonický kontakt. [Poznámky: Možno použiť viackrát. Prvá adresa v poradí je prioritná.]

  - Internetová adresa (D.1.5) | InternetAddress | Zložený dátový prvok pre elektronický kontakt. [Poznámky: Možno použiť viackrát. Prvá adresa v poradí je prioritná.]

  - Identifikátor (D.1.6) | ID | Zložený dátový prvok pre rôzne identifikátory.

    - D.1.1 Fyzická osoba (PhysicalPerson)

  - Základné atribúty | Hodnota

  - Dátový prvok | Fyzická osoba

  - Je súčasťou | Údaje o osobe, Príbuzná osoba

  - Má súčasti | Meno osoby Alternatívne meno Stav Pohlavie Narodenie Úmrtie Štátna príslušnosť Náboženstvo Povolanie Príbuzná osoba Bankové spojenie

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | MF SR

  - Popisné atribúty | Hodnota

  - Názov | Fyzická osoba

  - Definícia | Zložený dátový prvok pre rôzne informácie o fyzickej osobe

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je PhysicalPerson

  - Hodnoty | Neobsahuje

    - Skrátená forma popisu súčastí dátového prvku Fyzická osoba (PhysicalPerson)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Meno osoby (D.1.1.1) | PersonName | Zložený dátový prvok pre rôzne súčasti mena.

  - Alternatívne meno (D.1.1.2) 1.0 Povinný MF SR | AlternativeName | Popisuje meno, ktoré osoba používa, a zároveň to nie je ani jedno zo súčasných oficiálnych mien alebo priezvísk. [Hodnoty: Uvádza sa predchádzajúce meno, umelecké meno, meno z prvého manželstva, prezývka a podobne. Obsah je obmedzený iba formou reprezentácie.] [Poznámky: Môže byť použité viackrát.]

  - Stav (D.1.1.3) 1.0 Povinný MV SR | MaritalStatus | Zložený dátový prvok pre číselník obsahujúci údaje o rodinnom stave osoby. [Formát reprezentácie: V podradených prvkoch sa uvádza textová informácia podľa použitého atribútu číselníka.] [Hodnoty: Podradené prvky sa vypĺňajú v súlade s číselníkom Štatistického úradu Slovenskej republiky č. 4002 Rodinný stav. Vypĺňa sa adekvátny tvar podľa pohlavia. Stav „5“, t. j. „registrované partnerstvo“, sa uvádza iba tam, kde to umožňuje účel použitia v zmysle platnej legislatívy, inak sa v tomto prípade uvádza stav „0“ t. j. „nezistené“.]

  - Pohlavie (D.1.1.4) 1.0 Povinný MV SR | Sex | Zložený dátový prvok pre číselník obsahujúci údaje o pohlaví osoby. [Formát reprezentácie: V podradených prvkoch sa uvádza textová informácia podľa použitého atribútu číselníka.] [Hodnoty: Podradené prvky sa vypĺňajú v súlade s číselníkom Štatistického úradu Slovenskej republiky č. 3003 Pohlavie.]

  - Narodenie (D.1.1.5) | Birth | Zložený dátový prvok obsahujúci údaje o narodení.

  - Úmrtie (D.1.1.6) | Death | Zložený dátový prvok obsahujúci údaje o aktuálnom existenčnom stave osoby. [Poznámky: Podradené prvky sa vypĺňajú, iba ak má atribút „status“ inú hodnotu ako „1“ t. j. „živý“.] Atribúty: status.

  - | Status | [Hodnoty: Vypĺňa sa v súlade s číselníkom Štatistického úradu Slovenskej republiky č. 4003 Existenčný stav. Uvádza sa atribút KODPOL.]

  - Štátna príslušnosť (D.1.1.7) | Nationality | Zložený dátový prvok pre číselník obsahujúci údaje o štátnej príslušnosti. [Formát reprezentácie: V podradených prvkoch sa uvádza textová informácia podľa použitého atribútu číselníka.] [Hodnoty: Podradené prvky sa vypĺňajú v súlade s číselníkom Štatistického úradu Slovenskej republiky č. 0086 Krajiny OSN.] [Založené na: ISO 3166-1] [Poznámky: Tento prvok je obsahovo totožný s prvkom Štát (D.1.3.2). Pri použití znakového kódu sa odporúča používať dvojznakovú podobu (atribút POZN).]

  - Náboženstvo (D.1.1.8) 1.0 Povinný ŠÚ SR | Confession | Informácia o náboženskom vyznaní. [Formát reprezentácie: Textový reťazec.] [Hodnoty: Prázdna množina.] [Poznámky: V podmienkach Slovenskej republiky nepoužívať alebo používať iba s prázdnym obsahom. Zavádza sa iba kvôli kompatibilite so zahraničím.]

  - Povolanie (D.1.1.9) 1.0 Povinný ŠÚ SR | Occupation | Názov povolania, ktoré osoba vykonáva. [Formát reprezentácie: Textový reťazec.] [Hodnoty: Nemá predpísaný obsah. Odporúča sa vypĺňať v súlade s číselníkom Štatistického úradu Slovenskej republiky č. 5598 Skupiny Klasifikácie zamestnaní rozšírenej (KZAMR3), atribút NAZPLS.] [Poznámky: Tento prvok nie je zložený dátový prvok pre číselník.]

  - Príbuzná osoba (D.1.1.10) | RelatedPerson | Zložený dátový prvok obsahujúci údaje o príbuzných. [Poznámky: Môže byť použitý viackrát.]

  - Bankové spojenie (D.1.1.11) | BankConnection | Zložený dátový prvok obsahujúci údaje o bankovom spojení. [Poznámky: Môže byť použitý viackrát.]

    - D.1.1.1 Meno osoby (PersonName)

  - Základné atribúty | Hodnota

  - Dátový prvok | Meno osoby

  - Je súčasťou | Fyzická osoba Majiteľ

  - Má súčasti | Formátované meno Právne meno Meno Preferované meno Ďalšie meno Priezvisko Rodné priezvisko Affix

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | MF SR

  - Popisné atribúty | Hodnota

  - Názov | Fyzická osoba

  - Definícia | Zložený dátový prvok pre rôzne súčasti mena osoby

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je PersonName

  - Hodnoty | Neobsahuje

    - Skrátená forma popisu súčastí dátového prvku Meno osoby (PersonName)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Formátované meno (D.1.1.1.1) 1.0 Povinný MV SR | FormattedName | Formátované meno vrátane predpony a prípony. [Formát reprezentácie: Obsahuje celé meno v jednom reťazci so všetkými časťami v správnom poradí, čo znamená na správnom mieste. Oddelenie častí sa uvádza pomocou prázdneho znaku.] [Hodnoty: Nemá predpísaný obsah.] [Poznámky: Vhodné predovšetkým pre mená z iných jazykových oblastí. Taká forma mena nedokáže byť jednoducho parsovaná.]

  - Právne meno (D.1.1.1.2) 1.0 Povinný MV SR | LegalName | Používa sa na právne účely v niektorých štátoch. [Formát reprezentácie: Obsah je rovnaký ako pri FormattedName.] [Poznámky: V podmienkach Slovenskej republiky nepoužívať.]

  - Meno (D.1.1.1.3) 1.0 Povinný MV SR | GivenName | Obsahuje rodné meno, ktorým je nededená časť mena osoby. Známe aj ako prvé meno osoby alebo v užšom význame krstné meno osoby. [Formát reprezentácie: Textový reťazec. Každé meno sa uzatvára do vlastnej značky.] [Hodnoty: Nemá predpísaný obsah.] [Založené na: Zákon č. 300/1993 Z. z. o mene a priezvisku v znení neskorších predpisov.] [Poznámky: Možno použiť viackrát, v takom prípade je poradie použitia určujúce.]

  - Preferované meno (D.1.1.1.4) 1.0 Povinný MV SR | PreferredGivenName | Meno, ktoré osoba uprednostňuje pri svojom oslovení v prípade viacerých rodných mien. [Formát reprezentácie: Textový reťazec.] [Pravidlo použitia: Nemá predpísaný obsah.] [Hodnoty: Toto meno môže byť obľúbené meno z rodných mien. Ak by to mala byť prezývka, používa sa prvok Alternatívne meno (D.1.1.2).] [Poznámky: V Slovenskej republike nie je zvykom mať viac rodných mien, ale v zahraničí, najmä v španielsky hovoriacich krajinách, je to úplne bežné.]

  - Ďalšie meno (D.1.1.1.5) 1.0 Povinný MV SR | OtherName | Obsahuje stredné meno osoby alebo iniciály. [Formát reprezentácie: Textový reťazec.] [Pravidlo použitia: Nemá predpísaný obsah.] [Založené na: Zákon č. 300/1993 Z. z. o mene a priezvisku v znení neskorších predpisov.] [Poznámky: V podmienkach Slovenskej republiky nepoužívať. Originálne použitie najmä v Spojených štátoch amerických.]

  - Priezvisko (D.1.1.1.6) 1.0 Povinný MV SR | FamilyName | Obsahuje priezvisko. [Formát reprezentácie: Textový reťazec. Každé priezvisko sa uzavrie do vlastnej značky, a to aj vtedy, ak ide iba o prázdny znak.] [Hodnoty: Nemá predpísaný obsah.] [Založené na: Zákon č. 300/1993 Z. z. o mene a priezvisku v znení neskorších predpisov.] [Poznámky: Možno použiť viackrát, v takom prípade je poradie použitia určujúce.] Atribúty: primary, prefix.

  - | primary | [Hodnoty: primary=”true” Znamená, že tento výskyt priezviska je primárny. Odporúča sa uvádzať ako prvé v poradí použitých priezvisk. primary=”false” Znamená, že tento výskyt sa nepovažuje za primárny. Odporúča sa uvádzať až po primárnom výskyte priezviska. Poradie priezvisk s atribútom „false“ je určujúce. primary=”undefined” Znamená, že sa nepoužívajú viaceré priezviská; prípadne pri ich viacnásobnom použití s týmto atribútom je určujúce iba ich poradie použitia.] [Poznámky: Používa sa iba v prípade viacerých priezvisk. Pri použití viacerých priezvisk je poradie určujúce.]

  - | prefix | Môže obsahovať šľachtický alebo ekvivalentný titul. Ak existuje v priezvisku, vždy sa uvádza. [Hodnoty: Príklady použitia: de (ako v „de Witt“), la (ako v „la Salle“); van (ako v „van der Voss“).]

  - Rodné priezvisko (D.1.1.1.7) 1.0 Povinný MV SR | GivenFamilyName | Obsahuje rodné priezvisko. [Formát reprezentácie: Textový reťazec. Každé rodné priezvisko sa uzavrie do vlastnej značky, a to aj ak ide iba o prázdny znak.] [Hodnoty: Nemá predpísaný obsah.] [Založené na: Zákon Národnej rady Slovenskej republiky č. 300/1993 Z. z. o mene a priezvisku v znení neskorších predpisov] [Poznámky: Je možné použiť viackrát, v takom prípade je poradie použitia určujúce. Používa sa rovnako ako prvok Priezvisko.] Atribúty: primary, prefix

  - | primary | [Hodnoty: primary=”true” Znamená, že tento výskyt rodného priezviska je primárny. Odporúča sa uvádzať ako prvé v poradí použitých rodných priezvisk. primary=”false” Znamená, že tento výskyt sa nepovažuje za primárny. Odporúča sa uvádzať až po primárnom výskyte rodného priezviska. Poradie rodných priezvisk s atribútom „false“ je určujúce. primary=”undefined” Znamená, že sa nepoužívajú viaceré rodné priezviská, prípadne v ich viacnásobnom použití s týmto atribútom je určujúce iba ich poradie použitia.] [Poznámky: Používa sa iba v prípade viacerých rodných priezvisk. Pri použití viacerých rodných priezvisk je poradie určujúce.]

  - | prefix | Môže obsahovať šľachtický alebo ekvivalentný titul. Ak existuje v rodnom priezvisku, vždy sa uvádza. [Hodnoty: Príklady použitia: de (ako v „de Witt“), la (ako v „la Salle“); van (ako v „van der Voss“).]

  - Affix (D.1.1.1.8) 1.0 Povinný MV SR | Affix | Obsahuje ostatné časti mena osoby (predponu alebo príponu), tak ako ju definujú jednotlivé typy atribútov. [Formát reprezentácie: Textový reťazec uvádzaný v tvare, ako ho predpisuje atribút type.] [Hodnoty: Nemá predpísaný obsah.] [Poznámky: Je možné použiť viackrát (ani použitie rovnakého typu nie je obmedzené), v takom prípade je poradie použitia určujúce.] Atribúty: type, position

  - | type | Definuje kontext predpony alebo prípony. [Hodnoty: type=aristocraticTitle Uvádza sa, ak hodnota Affix obsahuje šľachtický titul. Príklady použitia: Barón, Graf, Earl, Vojvoda a podobne. type=formOfAddress Uvádza sa, ak hodnota Affix obsahuje oslovenie. Príklady použitia: Pán, Pani, Hon., Dr., Major a podobne. type=generation Uvádza sa, ak hodnota Affix obsahuje generačný titul. Príklady použitia: Sr., Jr., III (tretí) a podobne. type=qualification Uvádza sa, ak hodnota Affix obsahuje písmená, ktoré sa používajú na popis akademického titulu alebo iného typu kvalifikácie, ktoré osobe prináležia. Príklady použitia: PhD, MD, CPA, MCSD, Ing., Mgr. a podobne. [Hodnoty: V prípade uvádzania slovenských akademických titulov sa používa atribút NAZPLS číselníka Štatistického úradu Slovenskej republiky č. 0062 Titul pred menom a číselníka Štatistického úradu Slovenskej republiky č. 0063 Titul za menom.]

  - | position | Určuje pozíciu ostatnej časti mena. [Hodnoty: position=prefix Predpona – titul alebo oslovenie sa uvádza pred menom osoby. position=postfix Prípona – titul alebo oslovenie sa uvádza za menom osoby.]

    - D.1.1.5 Narodenie (Birth)

  - Základné atribúty | Hodnota

  - Dátový prvok | Narodenie

  - Je súčasťou | Fyzická osoba

  - Má súčasti | Dátum narodenia Miesto narodenia Štát

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | MV SR

  - Popisné atribúty | Hodnota

  - Názov | Narodenie

  - Definícia | Kontajner pre spresňujúce informácie ohľadne narodenia fyzickej osoby

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je Birth

    - Skrátená forma popisu súčastí dátového prvku Narodenie (Birth)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Dátum narodenia (D.1.1.5.1) 1.0 Povinný MV SR | DateOfBirth | Obsahuje dátum narodenia fyzickej osoby. [Formát reprezentácie: Štandardný XML formát Date. Deň a/alebo mesiac možno vynechať, najmä pre prípad, že nie je známy. Dátum nie je väčší, ako je aktuálny, a zároveň nie je väčší ako dátum úmrtia osoby, ak sú známe obidva dátumy.] [Hodnoty: Podľa formátu Date.] [Založené na: Zákon Národnej rady Slovenskej republiky č. 154/1994 Z. z. o matrikách v znení neskorších predpisov. Vyhláška Ministerstva vnútra Slovenskej republiky č. 302/1994 Z. z., ktorou sa vykonávajú niektoré ustanovenia zákona Národnej rady Slovenskej republiky o matrikách v znení vyhlášky č. 159/2006 Z. z.]

  - Miesto narodenia (D.1.1.5.2) 1.0 Povinný MV SR | PlaceOfBirth | Uvádza sa miesto narodenia v súlade s informáciou zapísanou na matrike pri narodení. Je to zložený dátový prvok pre číselník obsahujúci údaje o mieste narodenia. [Formát reprezentácie: V podradených prvkoch sa uvádza textová informácia podľa použitého atribútu číselníka.] [Hodnoty: Podradené prvky sa vypĺňajú v súlade s použitým prvkom Okres, Obec alebo Časť obce.] [Založené na: Zákon Národnej rady Slovenskej republiky č. 154/1994 Z. z. o matrikách v znení neskorších predpisov. Vyhláška Ministerstva vnútra Slovenskej republiky č. 302/1994 Z. z., ktorou sa vykonávajú niektoré ustanovenia zákona Národnej rady Slovenskej republiky o matrikách v znení vyhlášky č. 159/2006 Z. z.] [Poznámky: Poradie podradených prvkov je určujúce podľa vymenovania v atribúte Hodnoty.]

  - Štát (D.1.3.2) | Country | Zložený dátový prvok pre číselník obsahujúci údaje o štáte narodenia fyzickej osoby.

    - D.1.1.6 Úmrtie (Death)

  - Základné atribúty | Hodnota

  - Dátový prvok | Úmrtie

  - Je súčasťou | Fyzická osoba

  - Má súčasti | Dátum úmrtia Miesto úmrtia

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | MV SR

  - Popisné atribúty | Hodnota

  - Názov | Úmrtie

  - Definícia | Kontajner obsahujúci údaje o aktuálnom existenčnom stave fyzickej osoby a spresňujúce informácie ohľadne jej úmrtia

  - Formát reprezentácie | Obsahuje atribút „status“

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je Death

  - Hodnoty | Neobsahuje. Atribút „status“ sa vypĺňa v súlade s číselníkom Štatistického úradu Slovenskej republiky č. 4003 Existenčný stav. Uvádza sa atribút KODPOL.

  - Poznámky | Podprvky sa vypĺňajú, iba ak je hodnota atribútu „status“ iná ako „živý“.

  - Skrátená forma popisu súčastí dátového prvku Úmrtie (Death)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Dátum úmrtia (D.1.1.6.1) 1.0 Povinný MV SR | DateOfDeath | Ak nastala smrť fyzickej osoby, uvádza sa dátum jej úmrtia. [Formát reprezentácie: Štandardný XML formát Date. Deň a/alebo mesiac možno vynechať, najmä pre prípad, že nie je známy. Dátum nie je väčší, ako je aktuálny, a zároveň nie je menší ako dátum narodenia osoby, ak sú známe obidva dátumy.] [Hodnoty: Podľa formátu Date.] [Založené na: Zákon Národnej rady Slovenskej republiky č. 154/1994 Z. z. o matrikách v znení neskorších predpisov. Vyhláška Ministerstva vnútra Slovenskej republiky č. 302/1994 Z. z., ktorou sa vykonávajú niektoré ustanovenia zákona Národnej rady Slovenskej republiky o matrikách v znení vyhlášky č. 159/2006 Z. z.] [Poznámky: Vypĺňa sa, iba ak je hodnota atribútu „status“ prvku Úmrtie iná ako „živý“.]

  - Miesto úmrtia (D.1.1.6.2) 1.0 Povinný MV SR | PlaceOfDeath | Ak nastala smrť fyzickej osoby, uvádza sa v súlade s informáciou zapísanou na matrike miesto úmrtia. Je to zložený dátový prvok pre číselník obsahujúci údaje o mieste úmrtia. [Formát reprezentácie: V podradených prvkoch sa uvádza textová informácia podľa použitého atribútu číselníka.] [Hodnoty: Podradené prvky sa vypĺňajú v súlade s použitým prvkom Okres, Obec alebo Časť obce.] [Založené na: Zákon Národnej rady Slovenskej republiky č. 154/1994 Z. z. o matrikách v znení neskorších predpisov. Vyhláška Ministerstva vnútra Slovenskej republiky č. 302/1994 Z. z., ktorou sa vykonávajú niektoré ustanovenia zákona Národnej rady Slovenskej republiky o matrikách v znení vyhlášky č. 159/2006 Z. z.] [Poznámky: Vypĺňa sa, iba ak je hodnota atribútu „status“ prvku Úmrtie iná ako „živý“. Poradie podradených prvkov je určujúce podľa vymenovania v atribúte Hodnoty.]

    - D.1.1.10 Príbuzná osoba (RelatedPerson)

  - Základné atribúty | Hodnota

  - Dátový prvok | Príbuzná osoba

  - Je súčasťou | Fyzická osoba

  - Má súčasti | Druh príbuzenstva Fyzická osoba

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | MF SR

  - Popisné atribúty | Hodnota

  - Názov | Príbuzná osoba

  - Definícia | Zložený dátový prvok pre popis stupňa príbuznosti a osoby

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je RelatedPerson

  - Hodnoty | Neobsahuje

  - Poznámky | V tomto prípade je vhodné obmedziť vnorenie ďalších podprvkov Príbuzná osoba vzhľadom na prvok Fyzická osoba na vhodnú úroveň, prípadne úplne eliminovať.

    - Skrátená forma popisu súčastí dátového prvku Príbuzná osoba (RelatedPerson)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Druh príbuzenstva (D.1.1.10.1) 1.0 Povinný ŠÚ SR | TypeOfRelation | Zložený dátový prvok pre číselník obsahujúci údaje o príbuzenskom vzťahu pre príbuznú osobu. [Formát reprezentácie: V podradených prvkoch sa uvádza textová informácia podľa použitého atribútu číselníka.] [Hodnoty: Podradené prvky sa vypĺňajú v súlade s číselníkom Štatistického úradu Slovenskej republiky č. 4004 Príbuzenský stav.]

  - Fyzická osoba (D.1.1) | PhysicalPerson | Zložený dátový prvok pre popis fyzickej osoby. [Poznámky: V tomto prípade je vhodné obmedziť vnorenie ďalších podprvkov Príbuzná osoba na potrebnú úroveň, prípadne úplne eliminovať.]

    - D.1.1.11 Bankové spojenie (BankConnection)

  - Základné atribúty | Hodnota

  - Dátový prvok | Bankové spojenie

  - Je súčasťou | Fyzická osoba, Právnická osoba

  - Má súčasti | Majiteľ Názov banky Tuzemské bankové spojenie Medzinárodné bankové spojenie

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | NBS

  - Popisné atribúty | Hodnota

  - Názov | Bankové spojenie

  - Definícia | Kontajner pre informácie o bankovom účte a ďalších sprievodných údajoch pre bankové spojenie

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je BankConnection

  - Hodnoty | Neobsahuje

    - Skrátená forma popisu súčastí dátového prvku Bankové spojenie (BankConnection)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Majiteľ (D.1.1.11.1) | Holder | Zložený dátový prvok pre údaje o mene majiteľa (vlastníka) účtu.

  - Názov banky (D.1.1.11.2) 1.0 Povinný NBS | BankName | Obsahuje celé meno banky. [Formát reprezentácie: Obsahuje celé meno v jednom reťazci so všetkými časťami v správnom poradí, čo znamená na správnom mieste.] [Hodnoty: Pre tuzemské banky sa vypĺňa v súlade s aktuálnym Prevodníkom identifikačných kódov pre tuzemský platobný styk, ktorý zverejňuje Národná banka Slovenska, stĺpec Názov.]

  - Tuzemské bankové spojenie (D.1.1.11.3) | DomesticBankConnection | Zložený dátový prvok popisujúci tuzemské číslo účtu a kód banky.

  - Medzinárodné bankové spojenie (D.1.1.11.4) | InternationalBankConnection | Zložený dátový prvok popisujúci medzinárodné číslo účtu a kód banky.

    - D.1.1.11.1 Majiteľ (Holder)

  - Základné atribúty | Hodnota

  - Dátový prvok | Majiteľ

  - Je súčasťou | Bankové spojenie

  - Má súčasti | Meno osoby Plné meno právnickej osoby

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | NBS

  - Popisné atribúty | Hodnota

  - Názov | Majiteľ

  - Definícia | Kontajner pre údaje o mene majiteľa účtu

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je Holder

  - Hodnoty | Neobsahuje

    - Skrátená forma popisu súčastí dátového prvku Majiteľ (Holder)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Meno osoby (D.1.1.1) | PersonName | Zložený dátový prvok pre rôzne súčasti mena.

  - Plné meno právnickej osoby (D.1.2.1) | CorporateBodyFullName | Uvádza sa plný názov právnickej osoby. [Poznámky: Ak je držiteľom účtu fyzická osoba, ktorá má aj právnu formu, ktorou je najmä podnikateľ, je možné využiť obe súčasti dátového prvku Majiteľ.]

    - D.1.1.11.3 Tuzemské bankové spojenie (DomesticBankConnection)

  - Základné atribúty | Hodnota

  - Dátový prvok | Tuzemské bankové spojenie

  - Je súčasťou | Bankové spojenie

  - Má súčasti | Formátované spojenie Predčíslie účtu Základné číslo účtu Kód banky

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | NBS

  - Popisné atribúty | Hodnota

  - Názov | Tuzemské bankové spojenie

  - Definícia | Zložený dátový prvok pre údaje o bankovom spojení tuzemskej banky

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je DomesticBankConnection

  - Hodnoty | Neobsahuje

  - Poznámky | Na účely tohto materiálu sa za tuzemské bankové spojenie považuje úplné číslo účtu a kód banky.

    - Skrátená forma popisu súčastí dátového prvku Tuzemské bankové spojenie (NationalBankConnection)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Formátované spojenie (D.1.1.11.3.1) 1.0 Povinný NBS | FormattedDomesticBankConnection | Spojené celé tuzemské číslo účtu (vrátane predčíslia) a kód banky. [Formát reprezentácie: Textový reťazec. Predčíslie sa oddeľuje pomlčkou. Kód banky sa oddeľuje lomkou. Uvádza sa v súlade s opatrením Národnej banky Slovenska č. 7/2003, ktorým sa ustanovuje štruktúra bankového spojenia na účely tuzemských prevodov, štruktúra medzinárodného bankového čísla účtu na účely cezhraničných prevodov a podrobnosti o vydávaní prevodníka identifikačných kódov.] [Hodnoty: Príklady použitia: 123456-0123456789/1111.] [Poznámky: V prípade dekompozície na Predčíslie účtu, Číslo účtu a Kód banky sa nepoužíva.]

  - Predčíslie účtu (D.1.1.11.3.2) 1.0 Povinný NBS | AccountNumberPrefix | Uvádza sa číslo pred samotným číslom účtu. [Formát reprezentácie: Predčíslie účtu sa uvádza ako číslo v súlade s opatrením Národnej banky Slovenska č. 7/2003, ktorým sa ustanovuje štruktúra bankového spojenia na účely tuzemských prevodov, štruktúra medzinárodného bankového čísla účtu na účely cezhraničných prevodov a podrobnosti o vydávaní prevodníka identifikačných kódov.] [Hodnoty: Uvádza sa, iba ak existuje, nakoľko jeho existencia nie je povinná.]

  - Základné číslo účtu (D.1.1.11.3.3) 1.0 Povinný NBS | AccountNumber | Samotné číslo účtu pridelené osobe. [Formát reprezentácie: Číslo účtu sa uvádza ako číslo v súlade s opatrením Národnej banky Slovenska č. 7/2003, ktorým sa ustanovuje štruktúra bankového spojenia na účely tuzemských prevodov, štruktúra medzinárodného bankového čísla účtu na účely cezhraničných prevodov a podrobnosti o vydávaní prevodníka identifikačných kódov.] [Hodnoty: Hodnoty nie sú predpísané, závisia od hodnôt, ktoré prideľuje konkrétna banka.]

  - Kód banky (D.1.1.11.3.4) 1.0 Povinný NBS | BankCode | Uvádza sa kód, ktorý má konkrétna banka – každá banka má pridelené unikátne číslo. [Formát reprezentácie: Kód banky sa uvádza ako číslo.] [Hodnoty: Vypĺňa sa v súlade s aktuálnym Prevodníkom identifikačných kódov pre tuzemský platobný styk, ktorý zverejňuje Národná banka Slovenska.]

    - D.1.1.11.4 Medzinárodné bankové spojenie (InternationalBankConnection)

  - Základné atribúty | Hodnota

  - Dátový prvok | Medzinárodné bankové spojenie

  - Je súčasťou | Bankové spojenie

  - Má súčasti | IBAN BIC

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | NBS

  - Popisné atribúty | Hodnota

  - Názov | Tuzemské bankové spojenie

  - Definícia | Zložený dátový prvok pre údaje o bankovom spojení medzinárodnej banky

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je InternationalBankConnection

  - Hodnoty | Neobsahuje

  - Poznámky | Na účely výnosu sa za medzinárodné bankové spojenie považuje číslo účtu a kód banky.

    - Skrátená forma popisu súčastí dátového prvku Medzinárodné bankové spojenie (InternationalBankConnection)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - IBAN (D.1.1.11.4.1) 1.0 Povinný NBS | IBAN | Číslo IBAN (International Bank Account Number) je celoeurópske jednoznačné číslo účtu. [Forma reprezentácie: Textový reťazec. Vypĺňa sa v súlade s opatrením Národnej banky Slovenska č. 7/2003, ktorým sa ustanovuje štruktúra bankového spojenia na účely tuzemských prevodov, štruktúra medzinárodného bankového čísla účtu na účely cezhraničných prevodov a podrobnosti o vydávaní prevodníka identifikačných kódov.] [Hodnoty: Hodnoty nie sú predpísané, závisia od hodnôt, ktoré prideľuje konkrétna banka.] [Založené na: Norma ISO 13616.]

  - BIC (D.1.1.11.4.2) 1.0 Povinný NBS | BIC | BIC (Bank Identifier Code) znamená medzinárodný kód banky (tzv. SWIFT). [Formát reprezentácie: Textový reťazec.] [Hodnoty: Vypĺňa sa v súlade s normou ISO 9362.] [Založené na: Norma ISO 9362]

    - D.1.2 Právnická osoba (CorporateBody)

  - Základné atribúty | Hodnota

  - Dátový prvok | Právnická osoba

  - Je súčasťou | Údaje o osobe

  - Má súčasti | Plné meno právnickej osoby Alternatívne meno právnickej osoby Právna forma Organizačná jednotka Vznik Zánik Bankové spojenie Predmet činnosti Iné právne skutočnosti Základné imanie Zainteresovaná osoba

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | MF SR

  - Popisné atribúty | Hodnota

  - Názov | Právnická osoba

  - Definícia | Zložený dátový prvok pre popis právnickej osoby alebo subjektu, ktorý nie je právnickou osobou ani fyzickou osobou v zmysle právneho poriadku Slovenskej republiky.

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je CorporateBody

  - Hodnoty | Neobsahuje

  - Poznámky | Ak má fyzická osoba aj právnu formu, ktorou je najmä podnikateľ, je možné využiť tento prvok na výmenu údajov, ktoré prvok Fyzická osoba neobsahuje (Právna forma a podobne). Vzhľadom na množstvo rôznych zahraničných organizácií nie je vždy možné ich jednoznačné označenie ako právnickej osoby. Tento prvok je určený aj na prenos takýchto údajov.

    - Skrátená forma popisu súčastí dátového prvku Právnická osoba (CorporateBody)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Plné meno právnickej osoby (D.1.2.1) 1.0 Povinný MS SR | CorporateBodyFullName | Uvádza sa plný názov právnickej osoby. [Formát reprezentácie: Obsahuje celé meno v jednom reťazci so všetkými časťami v správnom poradí, čo znamená na správnom mieste. Oddelenie častí sa uvádza pomocou prázdneho znaku.] [Hodnoty: Nemá predpísaný obsah.] [Poznámky: Uvádza sa vrátane typových označení organizácie ako „a. s.“.]

  - Alternatívne meno právnickej osoby (D.1.2.2) 1.0 Povinný MV SR | CorporateBodyAlternativeName | Môže obsahovať alternatívy k plným názvom, ako sú zaužívané synonymá, skratky a podobne. [Formát reprezentácie: Textový reťazec.] [Hodnoty: Nemá predpísaný obsah.] [Poznámky: Môže byť použité viacnásobne.]

  - Právna forma (D.1.2.3) 1.0 Povinný MS SR, MV SR, MF SR, MK SR | LegalForm | Zložený dátový prvok pre číselník obsahujúci údaje o type právnickej osoby, ako je akciová spoločnosť a podobne. [Formát reprezentácie: V podradených prvkoch sa uvádza textová informácia podľa použitého atribútu číselníka.] [Hodnoty: Podradené prvky sa vypĺňajú v súlade s číselníkom Štatistického úradu Slovenskej republiky č. 0056 Právna forma organizácie.] [Poznámky: Používa sa na spresnenie typu alebo triedy právnickej osoby. Pre rôzne typy právnických osôb existujú rôzni gestori.]

  - Organizačná jednotka (D.1.2.4) 1.0 Povinný MF SR | OrganizationUnit | Obsahuje nižší útvar danej organizácie v prípade jej členenia. [Formát reprezentácie: Textový reťazec.] [Hodnoty: Nemá predpísaný obsah.] [Poznámky: Je možné použiť viackrát, v takom prípade je použitie určujúce. V poradí sa uvádza najprv hierarchicky najvyššia organizačná jednotka, ďalšie nasledujú podľa toho istého princípu.] Príklady použitia: Sekcia informatizácie spoločnosti, Odbor legislatívy, metodiky, štandardov a bezpečnosti informačných systémov.]

  - Vznik (D.1.2.5) 1.0 Povinný MF SR | Establishment | Uvádza sa dátum zriadenia právnickej osoby. [Formát reprezentácie: Štandardný XML formát Date. Deň a/alebo mesiac možno vynechať, najmä ak nie je známy. Dátum nie je väčší, ako je aktuálny, a zároveň nie je väčší ako dátum zániku, ak sú známe obidva dátumy.] [Hodnoty: Podľa formátu Date.]

  - Zánik (D.1.2.6) 1.0 Povinný MF SR | Termination | Uvádza sa dátum zániku alebo ukončenia činnosti právnickej osoby. [Formát reprezentácie: Štandardný XML formát Date. Deň a/alebo mesiac možno vynechať, najmä ak nie je známy. Dátum nie je väčší, ako je aktuálny, a zároveň nie je väčší ako dátum zániku, ak sú známe obidva dátumy.] [Hodnoty: Podľa formátu Date.]

  - Bankové spojenie (D.1.1.11) | BankConnection | Zložený dátový prvok obsahujúci údaje o bankovom spojení.

  - Predmet činnosti (D.1.2.7) 1.0 Povinný MS SR | Activities | Uvádza sa predmet činnosti právnickej osoby. [Formát reprezentácie: Textový reťazec.] [Hodnoty: Nemá predpísaný obsah.] [Poznámky: Je možné použiť viackrát. Odporúča sa vhodne rozdeliť podľa rozdielnych činností, takisto aj v prípade príliš dlhého reťazca pre jednu činnosť.]

  - Iné právne skutočnosti (D.1.2.8) 1.0 Povinný MS SR | OtherLegalFacts | Uvádza sa doplňujúca informácia v súvislosti s právnymi činnosťami týkajúcimi sa danej právnickej osoby.] [Formát reprezentácie: Textový reťazec.] [Hodnoty: Nemá predpísaný obsah.] [Poznámky: Je možné použiť viackrát. Obsahuje informáciu týkajúcu sa konkurzu, vyrovnania, likvidácie, nútenej správy, právneho dôvodu výmazu a podobne.]

  - Základné imanie (D.1.2.9) 1.0 Povinný MS SR | Equity | Zložený dátový prvok obsahujúci údaje o základnom imaní osoby.

  - Zainteresovaná osoba (D.1.2.10) 1.0 Povinný MS SR | Stakeholder | Zložený dátový prvok obsahujúci údaje o zainteresovanej osobe.

    - D.1.2.9 Základné imanie (Equity)

  - Základné atribúty | Hodnota

  - Dátový prvok | Základné imanie

  - Je súčasťou | Právnická osoba

  - Má súčasti | Mena Výška základného imania Výška splateného základného imania Schválená výška základného imania

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | MS SR

  - Popisné atribúty | Hodnota

  - Názov | Základné imanie

  - Definícia | Zložený dátový prvok obsahujúci údaje o imaní osoby.

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je Equity

  - Hodnoty | Neobsahuje

    - Skrátená forma popisu súčastí dátového prvku Základné imanie (Equity)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Mena (D.1.2.9.1) 1.0 Povinný MF SR | Currency | Uvádza sa, v akej mene je imanie vedené. [Formát reprezentácie: Zaužívaná skratka meny.] [Hodnoty: Nemá predpísaný obsah. Odporúča sa použitie atribútu skratka (alphabetic code) normy ISO 4217 currency names and code elements.] [Poznámky: Nepoužíva sa bez použitia dátového prvku Výška imania alebo Výška splateného imania.]

  - Výška základného imania (D.1.2.9.2) 1.0 Povinný MS SR | EquityValue | Obsahuje výšku imania osoby. [Formát reprezentácie: Číselná hodnota.] [Hodnoty: Nemá predpísaný obsah.] [Poznámky: Nepoužíva sa bez použitia dátového prvku Mena.]

  - Výška splateného základného imania (D.1.2.9.3) 1.0 Povinný MS SR | EquityValuePaid | Obsahuje výšku splateného imania osoby. [Formát reprezentácie: Číselná hodnota.] [Hodnoty: Nemá predpísaný obsah.] [Poznámky: Nepoužíva sa bez použitia dátového prvku Mena.]

  - Schválená výška základného imania (D.1.2.9.4) 1.0 Povinný MS SR | EquityValueApproved | Obsahuje výšku schváleného imania osoby [Formát reprezentácie: Číselná hodnota.] [Hodnoty: Nemá predpísaný obsah.] [Poznámky: Nepoužíva sa bez použitia dátového prvku Mena.]

    - D.1.2.10 Zainteresovaná osoba (Stakeholder)

  - Základné atribúty | Hodnota

  - Dátový prvok | Zainteresovaná osoba

  - Je súčasťou | Právnická osoba

  - Má súčasti | Typ zainteresovanej osoby Fyzická osoba Právnická osoba

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | MS SR

  - Popisné atribúty | Hodnota

  - Názov | Zainteresovaná osoba

  - Definícia | Zložený dátový prvok obsahujúci údaje o zainteresovanej osobe vo vzťahu k právnickej osobe.

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je Stakeholder

  - Hodnoty | Neobsahuje

  - Skrátená forma popisu súčastí dátového prvku Zainteresovaná osoba (Stakeholder)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Typ zainteresovanej osoby (D.1.2.10.1) 1.0 Povinný MS SR | StakeholderType | Obsahuje určenie typu zainteresovanej osoby. [Formát reprezentácie: Textový reťazec.] [Hodnoty: Nemá predpísaný obsah.] [Poznámky: Príklady použitia: konateľ, spoločník, komanditista.]

  - Fyzická osoba (D.1.1) | PhysicalPerson | Zložený dátový prvok pre popis fyzickej osoby. [Poznámky: Neuvádza sa v prípade, ak je uvedená právnická osoba.]

  - Právnická osoba (D.1.2) | CorporateBody | Zložený dátový prvok pre popis osôb, ktoré nie sú fyzickými osobami. [Poznámky: V prípade uvedenia Fyzickej osoby sa neuvádza a nemôže ani nastať ďalšie podradenie. Cyklické podradenie Právnickej osoby cez prvok Zainteresovaná osoba sa uvádza, až pokiaľ nie je vyplnená v podradení Fyzická osoba.]

    - D.1.3 Fyzická adresa (PhysicalAddress)

  - Základné atribúty | Hodnota

  - Dátový prvok | Fyzická adresa

  - Je súčasťou | Údaje o osobe

  - Má súčasti | Formátovaná adresa Štát Región Okres Obec Časť obce Ulica Orientačné číslo Súpisné číslo Časť budovy Záznam v registri adries Adresný bod Index domu Doručovacia adresa

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | MF SR

  - Popisné atribúty | Hodnota

  - Názov | Fyzická adresa

  - Definícia | Zložený dátový prvok pre poštovú adresu

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je PhysicalAddress

  - Hodnoty | Neobsahuje

    - Skrátená forma popisu súčastí dátového prvku Fyzická adresa (PhysicalAddress)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Formátovaná adresa (D.1.3.1) 1.0 Povinný MV SR | AddressLine | Formátovaná informácia, ktorá jednoznačne určuje adresu (katastrálne územie, názov hospodárskej usadlosti a podobne). [Formát reprezentácie: Obsahuje celú adresu v jednom reťazci so všetkými časťami v správnom poradí, resp. na správnom mieste. Oddelenie častí sa uvádza pomocou prázdneho znaku.] [Hodnoty: Nemá predpísaný obsah, neobsahuje však meno príjemcu, na to je určený podprvok Príjemca. Obsahuje ľubovoľné podprvky prvku Fyzická adresa.] [Poznámky: Takáto forma adresy nedokáže byť jednoducho parsovaná. V prípade dekompozície na jednotlivé podradené prvky Fyzickej adresy sa tento dátový prvok nepoužíva. Z príslušných číselníkov, podľa ktorých sa vypĺňajú jednotlivé podradené prvky Fyzickej adresy, obsahuje len textovú informáciu, a nie kódové označenie a podobne. Prvok sa používa najmä na potreby jednoduchej tlače. V podmienkach Slovenskej republiky sa odporúča nepoužívať.]

  - Štát (D.1.3.2) 1.0 Povinný ŠÚ SR | Country | Zložený dátový prvok pre číselník obsahujúci údaje o štáte. [Formát reprezentácie: V podradených prvkoch sa uvádza textová informácia podľa použitého atribútu číselníka.] [Hodnoty: Podradené prvky sa vypĺňajú v súlade s číselníkom Štatistického úradu Slovenskej republiky č. 0086 Krajiny OSN.] [Založené na: ISO 3166-1] [Poznámky: Pri použití znakového kódu sa odporúča používať dvojznakovú podobu (atribút POZN).]

  - Región (D.1.3.3) 1.0 Povinný MV SR | Region | Predstavuje federatívny štát, provinciu a/alebo šľachtické členenie území. [Formát reprezentácie: Textový reťazec.] [Hodnoty: Nemá predpísaný obsah.] [Poznámky: Je možné použiť viackrát, v takom prípade je poradie použitia určujúce. Vojenské adresy sa ukladajú viacnásobne (hierarchicky od najvyššieho po najnižší región) – 1. región = armádny / letecký / námorný poštový úrad, 2. región (dvojznakové označenie časti sveta ako AE = Európa, AA = obe Ameriky a podobne). V Slovenskej republike sa takéto členenie nerozoznáva, v zahraničí je však bežne používané.]

  - Okres (D.1.3.4) 1.0 Povinný MV SR | County | Zložený dátový prvok pre číselník obsahujúci údaje o okrese ako územnosprávnom členení. [Formát reprezentácie: V podradených prvkoch sa uvádza textová informácia podľa použitého atribútu číselníka.] [Hodnoty: V prípade Slovenskej republiky sa podradené prvky vypĺňajú v súlade s číselníkom Štatistického úradu Slovenskej republiky č. 0024 Lokálne štatistické územné jednotky 1 – okresy.] [Poznámky: V Slovenskej republike sa takéto členenie nezvykne pri zasielaní poštou používať, v zahraničí je to však bežné.]

  - Obec (D.1.3.5) 1.0 Povinný MV SR | Municipality | Zložený dátový prvok pre číselník obsahujúci údaje o obci. Obcou je územnosprávna jednotka charakterizovaná súvislým domovým osídlením a vlastným názvom. Obcou je aj mesto. [Formát reprezentácie: V podradených prvkoch sa uvádza textová informácia podľa použitého atribútu číselníka.] [Hodnoty: Podradené prvky sa vypĺňajú v súlade s číselníkom Štatistického úradu Slovenskej republiky č. 0025 Lokálne štatistické územné jednotky 2 – obce.]

  - Časť obce (D.1.3.6) 1.0 Povinný MV SR | District | Uvádza sa časť obce. [Formát reprezentácie: Textová informácia.] [Formát reprezentácie: Nemá predpísaný tvar. Neuvádza sa, ak je časť obce zároveň aj obcou (časti obcí Bratislava a Košice a podobne).]

  - Ulica (D.1.3.7) 1.0 Povinný MV SR | StreetName | Obsahuje názov ulice. Ak osada nemá názov ulice, udáva sa tu názov osady. [Formát reprezentácie: Textový reťazec.] [Hodnoty: Ak má obec definovaný vlastný register, zoznam alebo číselník ulíc, vypĺňa sa v súlade s ním, ak nemá, obsah sa nepredpisuje. Ak sa má udávať názov osady, vypĺňa sa v súlade s číselníkom Štatistického úradu Slovenskej republiky č. 0025 Lokálne štatistické územné jednotky 2 – obce. Uvádza sa položka NAZSKS.] [Založené na: Vyhláška Ministerstva vnútra Slovenskej republiky č. 31/2003 Z. z., ktorou sa ustanovujú podrobnosti o označovaní ulíc a iných verejných priestranstiev a o číslovaní stavieb.] [Poznámky: Údaje sa zadávajú z dôvodu porovnateľnosti v neskrátenej podobe. Mnohé ulice sú v zahraničí označované číselne – toto sa nepovažuje za číselný údaj za ulicou, tak ako sa udáva v Slovenskej republike. Tento prvok nie je zložený dátový prvok pre číselník. Príklady použitia: Lachova, Námestie P. O. Hviezdoslava, Nad humnom, 5223 W High Road.]

  - Orientačné číslo (D.1.3.8) 1.0 Povinný MV SR | BuildingNumber | Obsahuje názov budovy alebo číslo domu. [Formát reprezentácie: Textový reťazec.] [Hodnoty: Nemá predpísaný obsah.] [Poznámky: Môže obsahovať aj nečíselné znaky, preto je definované ako reťazec. Príklady použitia: 10, 23A, 18/III, Berlaymont.]

  - Súpisné číslo (D.1.3.9) 1.0 Povinný MV SR | PropertyRegistrationNumber | Obsahuje súpisné číslo budovy. [Formát reprezentácie: Obsahuje číslo.] [Hodnoty: Nemá predpísaný obsah.] [Poznámky: Používa sa najmä pre obce, kde neexistujú ulice. Nakoľko budova má súpisné číslo, ale zároveň môže mať aj orientačné číslo, nie sú tieto dva údaje totožné.]

  - Časť budovy (D.1.3.10) 1.0 Povinný MV SR | Unit | Tento prvok je určený na bližšie určenie miesta v rámci budovy, ak je to potrebné. [Formát reprezentácie: Textový reťazec.] [Hodnoty: Nemá predpísaný obsah, používa sa však iba raz, a preto obsahuje celú informáciu, t. j. aj prípadné viacnásobné členenie.] [Poznámky: Príklady použitia: Blok D, dielňa, 4. poschodie vpravo, byt 41.]

  - Záznam v registri adries (D.1.3.11) 1.0 Povinný ÚGKK SR | AddressRegisterEntry | Zložený dátový prvok obsahujúci údaje podľa registra adries. [Pravidlo použitia: V súčasnosti sa nevypĺňa.]

  - Adresný bod (D.1.3.12) | AddressPoint | Zložený dátový prvok, ktorý je priamym priestorovým identifikátorom adresy v súradniciach záväzných súradnicových systémov. [Poznámky: Používa sa najmä pre potrebu GPS navigácie. Používa rovinné súradnice x, y v systéme JTSK a nadmorskú výšku h v systéme Bpv a priestorové súradnice BLH v súradnicovom systéme ETRS 89. Na vzájomný prevod súradníc sa používa jednotný transformačný kľúč zverejnený v Spravodajcovi ÚRGG SR.]

  - Index domu (D.1.3.13) 1.0 Povinný MV SR | BuildingIndex | Tento prvok je identifikátorom adresy v informačnom systéme registra obyvateľov. [Formát reprezentácie: Číselný reťazec s maximálne desiatimi ciframi.] [Hodnoty: Nemá predpísaný obsah.]

  - Doručovacia adresa (D.1.3.14) | DeliveryAddress | Zložený dátový prvok presnejšie určujúci adresu.

    - D.1.3.12 Adresný bod (AddressPoint)

  - Základné atribúty | Hodnota

  - Dátový prvok | Adresný bod

  - Je súčasťou | Fyzická adresa

  - Má súčasti | XYZ BLH Určenie bodu

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | ÚGKK SR

  - Popisné atribúty | Hodnota

  - Názov | Adresný bod

  - Definícia | Zložený dátový prvok, ktorý je priamym priestorovým identifikátorom adresy v súradniciach záväzných súradnicových systémov.

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je AddressPoint

  - Hodnoty | Neobsahuje

  - Poznámky | Používa sa najmä pre potrebu GPS navigácie. Používa rovinné súradnice x, y v systéme JTSK a nadmorskú výšku h v systéme Bpv a priestorové súradnice BLH v súradnicovom systéme ETRS 89. Na vzájomný prevod súradníc sa používa jednotný transformačný kľúč zverejnený v Spravodajcovi ÚRGG SR.

  - Skrátená forma popisu súčastí dátového prvku Adresný bod (AddressPoint)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - xyh (D.1.3.12.1) 1.0 Povinný ÚGKK SR | xyh | Zložený dátový prvok pre súradnicu v tvare x,y,h. [Založené na: Súradnicový systém S-JTSK, výškový systém Bpv.] [Poznámky: Principiálne určuje bežné použitie v súradnicovom systéme jednotnej trigonometrickej siete katastrálnej a baltskom výškovom systéme.]

  - BLH (D.1.3.12.2) 1.0 Povinný ÚGKK SR | BLH | Zložený dátový prvok pre súradnicu v tvare B,L,H. [Založené na: Európsky terestrický referenčný systém 1989.]

  - Určenie bodu (D.1.3.12.3) 1.0 Povinný ÚGKK SR | AddressPointID | Prvok určujúci presné umiestnenie objektu, odvodzuje sa od vchodu. [Formát reprezentácie: Textový reťazec zložený z dvanástich cifier.] [Hodnoty: Prvých šesť cifier určuje katastrálne územie, ostatných šesť tvorí poradové pozície.]

    - D.1.3.12.1 XYZ (XYZ)

  - Základné atribúty | Hodnota

  - Dátový prvok | xyh

  - Je súčasťou | Adresný bod

  - Má súčasti | x y h

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | ÚGKK SR

  - Popisné atribúty | Hodnota

  - Názov | xyh

  - Definícia | Obsahuje súradnicu v tvare x,y,h.

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je xyh

  - Hodnoty | Neobsahuje

  - Založené na | Súradnicový systém S-JTSK, výškový systém Bpv.

  - Poznámky | Principiálne určuje bežné použitie v súradnicovom systéme jednotnej trigonometrickej siete katastrálnej a baltskom výškovom systéme.]

  - Skrátená forma popisu súčastí dátového prvku XYZ (XYZ)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - x (D.1.3.12.1.1) 1.0 Povinný ÚGKK SR | AxisX | Obsahuje X-ovú súradnicu. [Formát reprezentácie: Číslo.] [Hodnoty: Nemá predpísaný obsah.] [Založené na: Norma S-JTSK.] [Poznámky: Príklad použitia: 1279338,64]

  - y (D.1.3.12.1.2) 1.0 Povinný ÚGKK SR | AxisY | Obsahuje Y-ovú súradnicu. [Formát reprezentácie: Číslo.] [Hodnoty: Nemá predpísaný obsah.] [Založené na: Norma S-JTSK.] [Poznámky: Príklad použitia: 566986,96]

  - h (D.1.3.12.1.3) 1.0 Povinný ÚGKK SR | HeightH | Obsahuje nadmorskú výšku h. [Formát reprezentácie: Číslo.] [Hodnoty: Nemá predpísaný obsah.] [Založené na: Bpv.] [Poznámky: Príklad použitia: 123,96]

    - D.1.3.12.2 BLH (BLH)

  - Základné atribúty | Hodnota

  - Dátový prvok | BLH

  - Je súčasťou | Adresný bod

  - Má súčasti | B L H

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | ÚGKK SR

  - Popisné atribúty | Hodnota

  - Názov | BLH

  - Definícia | Obsahuje súradnicu v tvare B,L,H.

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je BLH

  - Hodnoty | Neobsahuje

  - Založené na | Európsky terestrický referenčný systém 1989.

  - Skrátená forma popisu súčastí dátového prvku XYZ (XYZ)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - B (D.1.3.12.2.1) 1.0 Povinný ÚGKK SR | AxisB | Obsahuje B-ovú súradnicu. [Formát reprezentácie: Číslo.] [Hodnoty: Nemá predpísaný obsah.] [Založené na: ETRS-89.] [Poznámky: Príklad použitia: 48,123456]

  - L (D.1.3.12.2.2) 1.0 Povinný ÚGKK SR | AxisL | Obsahuje L-ovú súradnicu. [Formát reprezentácie: Číslo.] [Hodnoty: Nemá predpísaný obsah.] [Založené na: ETRS-89.] [Poznámky: Príklad použitia: 18,123456]

  - H (D.1.3.12.2.3) 1.0 Povinný ÚGKK SR | AxisH | Obsahuje H-ovú súradnicu. [Formát reprezentácie: Číslo.] [Hodnoty: Nemá predpísaný obsah.] [Založené na: ETRS-89.] [Poznámky: Príklad použitia: 365,12.]

    - D.1.3.14 Doručovacia adresa (DeliveryAddress)

  - Základné atribúty | Hodnota

  - Dátový prvok | Doručovacia adresa

  - Je súčasťou | Fyzická adresa

  - Má súčasti | Poštové smerové číslo P.O.BOX Príjemca

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | MF SR

  - Popisné atribúty | Hodnota

  - Názov | Doručovacia adresa

  - Definícia | Zložený dátový prvok presnejšie určujúci adresu

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je DeliveryAddress

  - Hodnoty | Neobsahuje

    - Skrátená forma popisu súčastí dátového prvku Doručovania adresa (DeliveryAddress)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Poštové smerové číslo (D.1.3.14.1) 1.0 Povinný Poštový úrad SR | PostalCode | Obsahuje kód, ktorý ustanovili poštové autority na účely doručovania pošty. [Formát reprezentácie: Textový reťazec.] [Hodnoty: Pre slovenské adresy sa uvádza podľa platného zoznamu Slovenskej pošty.] [Poznámky: Zahraničné poštové smerové čísla majú častokrát nečíselný charakter. Reťazec sa vždy uvádza spolu, čo znamená, že sa neoddeľuje medzerou.]

  - P.O.BOX (D.1.3.14.2) 1.0 Povinný Poštový úrad SR | PostOfficeBox | Poštový priečinok. [Formát reprezentácie: Textový reťazec začínajúci definovanou hodnotou a končiaci číslom.] [Hodnoty: Vždy sa uvádza aj text „P.O.BOX“.] [Poznámky: Príklady použitia: P.O.BOX 32, P.O.BOX 311.]

  - Príjemca (D.1.3.14.3) | Recipient | Zložený dátový prvok na identifikáciu príjemcu.

    - D.1.3.14.3 Príjemca (Recipient)

  - Základné atribúty | Hodnota

  - Dátový prvok | Príjemca

  - Je súčasťou | Doručovacia adresa

  - Má súčasti | Meno osoby Ďalší text Organizačná jednotka Názov organizácie

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | MDPT SR

  - Popisné atribúty | Hodnota

  - Názov | Príjemca

  - Definícia | Zložený dátový prvok na identifikáciu príjemcu

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je Recipient

  - Hodnoty | Neobsahuje

  - Skrátená forma popisu súčastí dátového prvku Príjemca (Recipient)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Meno osoby (D.1.1.1) | PersonName | Zložený dátový prvok pre meno fyzickej osoby. [Poznámky: Nevypĺňa sa, ak je táto informácia vyplnená v prvku Fyzická osoba a tá je zároveň aj príjemcom (inak nastáva zbytočná duplicita).]

  - Ďalší text (D.1.3.14.3.1) 1.0 Povinný Poštový úrad SR | AdditionalText | Môže obsahovať ďalšie smerovacie informácie príjemcu. Zvyčajne udáva ďalšiu navigáciu po doručení poštovou službou. [Formát reprezentácie: Textový reťazec.] [Hodnoty: Nemá predpísaný obsah.] [Poznámky : Je možné použiť viackrát. Príklady použitia: anketa, daňové priznanie.]

  - Organizačná jednotka (D.1.2.4) | OrganizationUnit | Obsahuje nižší útvar danej organizácie v prípade jej členenia.

  - Plné meno právnickej osoby (D.1.2.1) | CorporateBodyFullName | Uvádza sa plný názov právnickej osoby. [Poznámky: Nevypĺňa sa, ak je táto informácia vyplnená v prvku Právnická osoba a tá je zároveň aj príjemcom (inak nastáva zbytočná duplicita).]

    - TABULKA_58

    - D.1.4 Telefónna adresa (TelephoneAddress)

  - Základné atribúty | Hodnota

  - Dátový prvok | Telefónna adresa

  - Je súčasťou | Údaje o osobe

  - Má súčasti | Typ telefónu Číslo

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | Telekomunikačný úrad SR

  - Popisné atribúty | Hodnota

  - Názov | Telefónna adresa

  - Definícia | Zložený dátový prvok pre rôzne druhy telefónnych čísel

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je TelephoneAddress

  - Hodnoty | Neobsahuje

    - Skrátená forma popisu súčastí dátového prvku Telefónna adresa (TelephoneAddress)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Typ telefónu (D.1.4.1) 1.0 Povinný TÚ SR | TelephoneType | Zložený dátový prvok pre číselník, obsahujúci údaje o type alebo kategórii telekomunikačného zariadenia. [Formát reprezentácie: V podradených prvkoch sa uvádza textová informácia podľa použitého atribútu číselníka.] [Hodnoty: Podradené prvky sa vypĺňajú v súlade s číselníkom Štatistického úradu Slovenskej republiky č. 4005 Typ telefónneho čísla.]

  - Číslo (D.1.4.2) | Number | Zložený dátový prvok pre štruktúrované telefónne číslo.

    - D.1.4.2 Číslo (Number)

  - Základné atribúty | Hodnota

  - Dátový prvok | Číslo

  - Je súčasťou | Telefónna adresa

  - Má súčasti | Formátované číslo Medzinárodné smerové číslo Národné číslo Smerové číslo Účastnícke číslo Sublinka

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | Telekomunikačný úrad SR

  - Popisné atribúty | Hodnota

  - Názov | Číslo

  - Definícia | Zložený dátový prvok pre štruktúrované telefónne číslo

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je Number

  - Hodnoty | Neobsahuje

    - Skrátená forma popisu súčastí dátového prvku Číslo (Number)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Formátované číslo (D.1.4.2.1) 1.0 Povinný TÚ SR | FormattedNumber | Obsahuje reprezentáciu telekomunikačného číselného reťazca. [Formát reprezentácie: Textový reťazec, tvorený tromi skupinami znakov, pričom prvá skupina začína znakom „+“ alebo znakmi „00“.] [Hodnoty: Vypĺňa sa v súlade s aktuálnym číslovacím plánom, ktorý zverejňuje Telekomunikačný úrad.] [Založené na: Opatrenie Telekomunikačného úradu Slovenskej republiky z 1. februára 2007 č. O – 14/2007 o číslovacom pláne.] [Poznámky: Takáto podoba sa ťažko parsuje. Ak je použité formátované číslo, nepoužíva sa neformátovaná podoba. Príklad použitia: +421 48 4324134.]

  - Medzinárodné smerové číslo (D.1.4.2.2) 1.0 Povinný TÚ SR | InternationalCountryCode | Kód krajiny podľa ITU, ktorý identifikuje špecifickú krajinu, krajiny v integrovanom číselnom pláne alebo špecifickú geografickú oblasť. [Formát reprezentácie: Textový reťazec, ktorý začína znakom „+“ alebo znakmi „00“.] [Hodnoty: Vypĺňa sa v súlade s číslovacím plánom, ktorý svojím opatrením vydáva Telekomunikačný úrad.] [Založené na: Opatrenie Telekomunikačného úradu Slovenskej republiky z 1. februára 2007 č. O – 14/2007 o číslovacom pláne.]

  - Národné číslo (D.1.4.2.3) 1.0 Povinný TÚ SR | NationalNumber | Niektoré oblasti majú dve predvoľby – vnútroštátne a zahraničné medzimestské predvoľby, tento prvok obsahuje vnútroštátnu predvoľbu. [Formát reprezentácie: Textový reťazec.] [Hodnoty: Nemá predpísaný obsah.] [Poznámky: V Slovenskej republike sa nepoužíva.]

  - Smerové číslo (D.1.4.2.4) 1.0 Povinný TÚ SR | AreaCityCode | Definuje buď číslovanie v rámci jednej krajiny (alebo skupiny krajín či geografickej oblasti), alebo sieť – službu. V Slovenskej republike je to ekvivalent národného cieľového kódu. [Formát reprezentácie: Textový reťazec.] [Hodnoty: Vypĺňa sa v súlade s číslovacím plánom, ktorý svojím opatrením vydáva Telekomunikačný úrad.] [Založené na: Opatrenie Telekomunikačného úradu Slovenskej republiky z 1. februára 2007 č. O – 14/2007 o číslovacom pláne.]

  - Účastnícke číslo (D.1.4.2.5) 1.0 Povinný TÚ SR | SubscriberNumber | Číslo, ktoré identifikuje užívateľa siete alebo číslovacej oblasti. [Formát reprezentácie: Textový reťazec.] [Hodnoty: Pre čísla slovenských operátorov sa vypĺňa v súlade s číslovacím plánom, ktorý svojím opatrením vydáva Telekomunikačný úrad. Obsahuje aspoň jednu číslicu.] [Založené na: Opatrenie Telekomunikačného úradu Slovenskej republiky z 1. februára 2007 č. O – 14/2007 o číslovacom pláne.] [Poznámky: Okrem číslic môže najmä v údajoch zo zahraničia obsahovať medzery, spojovacie znamienka alebo periódy.]

  - Sublinka (D.1.4.2.6) 1.0 Povinný TÚ SR | Extension | Môže obsahovať PBX linku, PIN pagera, faxovú podadresu alebo ďalšie doplňujúce adresné informácie. [Formát reprezentácie: Textový reťazec.] [Hodnoty: Nemá predpísaný obsah.]

    - D.1.5 Internetová adresa (InternetAddress)

  - Základné atribúty | Hodnota

  - Dátový prvok | Internetová adresa

  - Je súčasťou | Údaje o osobe

  - Má súčasti | Adresa dsig:KeyInfo

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | MF SR

  - Popisné atribúty | Hodnota

  - Názov | Internetová adresa

  - Definícia | Zložený dátový prvok pre elektronický kontakt

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je InternetAddress

  - Hodnoty | Neobsahuje

  - Poznámky | Používa sa pre rôzne súčasti internetovej adresy ako e-mail alebo webová adresa.

    - Skrátená forma popisu súčastí dátového prvku Internetová adresa (InternetAddress)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Adresa (D.1.5.1) 1.0 Povinný MF SR | Address | Uvádza sa kontakt pre rôzne typy elektronických adries. [Formát reprezentácie: Uvádza sa v tvare URI ako „typ: adresa“. Adresa je v tvare textových reťazcov oddelených bodkami. Vo väčšine prípadov hneď za znakom „:“ nasleduje zdvojený znak „//“. V prípade emailovej adresy sa namiesto prvej bodky uvádza znak „@“.] [Hodnoty: Rozoznávajú sa typy ako mailto (mailová adresa), http (webová adresa), ftp, ldap a podobne. Časť adresy vo väčšine prípadov dodržiava radenie textových reťazcov podľa podradenia doménových mien.]

  - dsig:KeyInfo (D.1.5.2) 1.0 Povinný NBÚ SR | Dsig:KeyInfo | Medzinárodný štandard pre digitálne podpisy podľa W3C-XMLDSig. [Formát reprezentácie: V súlade s definíciami k W3C-XMLD Sig.] [Hodnoty: V súlade s definíciami k W3C-XMLD Sig.] [Založené na: Odporúčania W3C XML-Signature Syntax and Processing.]

    - D.1.6 Identifikátor (ID)

  - Základné atribúty | Hodnota

  - Dátový prvok | Identifikátor

  - Je súčasťou | Údaje o osobe

  - Má súčasti | Typ identifikátora Hodnota identifikátora

  - Verzia | 1.0

  - Stav | Povinný

  - Gestor | MF SR

  - Popisné atribúty | Hodnota

  - Názov | Identifikátor

  - Definícia | Zložený dátový prvok pre rôzne identifikátory

  - Typ prvku | Dátový typ

  - XML schéma | XML názov prvku je ID

  - Hodnoty | Neobsahuje

    - Skrátená forma popisu súčastí dátového prvku Identifikátor (ID)

  - Slovensky Verzia Stav Gestor | Anglicky XML | Poznámka

  - Typ identifikátora (D.1.6.1) 1.0 Povinný MV SR | IdentifierType | Zložený dátový prvok pre číselník, obsahujúci údaje o type použitého identifikátora. [Formát reprezentácie: V podradených prvkoch sa uvádza textová informácia podľa použitého atribútu číselníka.] [Hodnoty: Podradené prvky sa vypĺňajú v súlade s číselníkom Štatistického úradu Slovenskej republiky č. 4001 Identifikátor.] [Poznámky: Uvádza sa vo dvojici s Hodnotou identifikátora. Je možné viacnásobné použitie, pričom každý typ je možné použiť práve raz.]

  - Hodnota identifikátora (D.1.6.2) 1.0 Povinný MV SR | IdentifierValue | Obsahuje samotnú hodnotu použitého identifikátora. [Formát reprezentácie: V závislosti od typu identifikátora vo všeobecnosti je to reťazec znakov.] [Poznámky: Uvádza sa vo dvojici s Typom identifikátora. Je možné viacnásobné použitie, pričom pre každý typ identifikátora sa môže použiť práve raz.]
