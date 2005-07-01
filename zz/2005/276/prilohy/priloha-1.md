Príloha č. 1 k vyhláške č. 276/2005 Z. z.

- OPIS ROZHRANIA NA POSKYTOVANIE ÚDAJOV A VÝMENU ÚDAJOV O VYDANÝCH LEKÁRSKYCH PREDPISOCH MEDZI ZDRAVOTNÝMI POISŤOVŇAMI

  - Typ dávky: XXX

  - Predkladá: zdravotná poisťovňa, ktorá vydala tlačivá lekárskych predpisov zmluvným lekárom a zdravotníckym zariadeniam iných zdravotných poisťovní

  - Obsah dávky: záhlavie dávky

  - veta tela dávky

- Záhlavie dávky | | |

- 1. charakter dávky | p | char | 1

- 2. typ dávky | P | int | 3-3

- 3. IČO odosielateľa | p | int | 8

- 4. dátum odoslania dávky | P | date | RRRRMMDD

- 5. za obdobie | P | int | RRRRMM

- 6. počet dokladov v dávke | P | int | 6

  - Charakter dávky: N – nová, O – opravná (veľké písmeno O), A – aditívna

  - Typ dávky: číslený kód je špecifikovaný pri opise štruktúry každej dávky

  - Počet dokladov: obsahuje súčet dokladov (viet) tela dávky

- Veta tela dávky | | |

- 1. typ tlačiva | P | int | 3

- 2. kód lekára, zdravotníckeho zariadenia alebo lekárne, ktorej boli vydané tlačivá | P | char | 13

- 3. deň vydania tlačív | P | date | RRRRMMDD

- 4. počet vydaných tlačív | P | int | 6

- 5. počiatočný identifikačný kód tlačiva | p | char | 12

- 6. koncový identifikačný kód tlačiva | P | char | 12

  - Typ tlačiva: 001 - lekársky predpis, 002 - lekársky poukaz, ...

  - Kód lekára, ktorému boli vydané tlačivá: podľa metodiky VšZP

  - Počiatočný identifikačný kód tlačiva: XXNNNNNNNNNN

  - Koncový identifikačný kód tlačiva: XXNNNNNNNNNN
