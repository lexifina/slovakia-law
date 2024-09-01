Príloha k vyhláške č. 224/2024 Z. z.

- TVAR POSKYTOVANÝCH IDENTIFIKAČNÝCH ÚDAJOV A LOKALIZAČNÝCH ÚDAJOV

  - ČASŤ A Tvar telefónneho čísla volajúceho a medzinárodné označenie mobilného koncového zariadenia

    - 1. Tvar telefónneho čísla volajúceho pri národnom volaní

    - SS7/ISUP parameter Calling Party Number

    - Address signals = národný cieľový kód (NDC) + účastnícke číslo (SN)

    - Nature of Address indicator = national (significant) number

    - Screening indicator = user provided, verified and passed / network provided

    - alebo

    - Address signals = kód krajiny (CC = 421) + národný cieľový kód (NDC) + účastnícke číslo (SN)

    - Nature of Address indicator = international number

    - Screening indicator = user provided, verified and passed / network provided

    - 2. Tvar telefónneho čísla volajúceho pri tiesňovom volaní podľa § 1 ods. 1 písm. d)

    - SS7/ISUP parameter Calling Party Number

    - Address signals = kód krajiny (CC) + národný cieľový kód (NDC) + účastnícke číslo (SN)

    - Nature of Address indicator = international number

    - Screening indicator = user provided, verified and passed / network provided

    - 3. Medzinárodné označenie volajúceho pri tiesňovom volaní podľa § 1 ods. 1 písm. b)

    - SS7/ISUP parameter Calling Party Number

    - Address signals = IMEI

    - Nature of Address indicator = national (significant) number / unknown / international number

    - Screening indicator = user provided, not verified

    - Číslice IMEI sa prenášajú ako binárne kódované dekadické číslice v poradí pridelený kód typu (TAC), sériové číslo (SNR), rezervná číslica (SD). Číslica kódu TAC s najvyššou váhou sa prenáša v 4-bitovom poli na pozícii 1<sup>st</sup> address signal. Nasledujúce číslice sa prenášajú postupne v po sebe idúcich 4-bitových poliach. Rezervná číslica SD sa prenáša na pozícii 15<sup>th</sup> address signal, pozícia

    - 16<sup>th</sup>address signal obsahuje výplň.<sup>13</sup>)

  - ČASŤ B Tvar identifikátora sektora základňovej stanice

    - 1. Mobilné siete druhej generácie a tretej generácie

      - Ako identifikátor sektora základňovej stanice sa používa Cell Global Identification (CGI),<sup>14</sup>) ktorý sa skladá z týchto častí:

        - a) Mobilný kód krajiny (MCC) identifikuje krajinu, v ktorej sa nachádza verejná pozemná mobilná sieť (PLMN). Mobilný kód krajiny pridelený Slovenskej republike je 231.

        - b) Kód mobilnej siete (MNC) je kód identifikujúci verejnú pozemnú mobilnú sieť (PLMN) v danej krajine. V Slovenskej republike je kód mobilnej siete dvojmiestny.

        - c) Kód lokalizačnej oblasti (LAC) je kód pevnej dĺžky (2 oktety) identifikujúci lokalizačnú oblasť v rámci verejnej pozemnej mobilnej siete (PLMN). Na vyjadrenie úplného rozsahu hodnôt uvedeného parametra v dekadickom formáte je potrebných 5 dekadických číslic.

        - d) Identita bunky (CI) je kód pevnej dĺžky (2 oktety) identifikujúci bunku v rámci lokalizačnej oblasti. Identita bunky musí byť jedinečná v rámci lokalizačnej oblasti. Na vyjadrenie úplného rozsahu hodnôt uvedeného parametra v dekadickom formáte je potrebných 5 dekadických číslic.

      - Dĺžka CGI je 15 dekadických číslic. Ak ide o prenos CGI podľa § 4 ods. 3 písm. a) sa jeho hodnoty prenášajú v dekadickom formáte.

    - 2. Mobilné siete štvrtej generácie a piatej generácie

      - Ako identifikátor sektora základňovej stanice sa používa E-UTRAN Cell Global Identification (ECGI),<sup>15</sup>) ktorý je vytvorený spojením

        - a) identifikátora verejnej pozemnej mobilnej siete PLMN (PLMN-Id) tvoreného mobilným kódom krajiny (MCC) a kódom mobilnej siete (MNC) a

        - b) identity bunky E-UTRAN (ECI), ktorá má pevnú dĺžku 28 bitov. ECI pozostáva z dvoch častí: eNodeB ID a Physical Cell ID. eNodeB ID predstavuje jedinečné identifikačné číslo pridelené každej eNodeB (základňovej stanici) v sieti. Physical Cell ID označuje identifikátor fyzickej vrstvy konkrétnej bunky v rámci eNodeB. Na vyjadrenie úplného rozsahu hodnôt ECI v dekadickom formáte je potrebných 9 dekadických číslic.

      - Keďže kód mobilnej siete (MNC) v Slovenskej republike je dvojmiestne číslo, dĺžka ECGI je 14 dekadických číslic. V prípade prenosu ECGI podľa § 4 ods. 3 písm. a) sa jeho hodnoty prenášajú v dekadickom formáte.

    - ČASŤ C Formát telefónneho čísla volaného

      - 1. Volania na čísla tiesňových volaní 112 a 155

        - SS7/ISUP parameter Called Party Number

        - Address signals = národný cieľový kód (NDC) + číslo tiesňového volania + sieťové smerovacie číslo (NRN)

        - Nature of Address indicator = national (significant) number

      - 2. Volania na čísla tiesňových volaní 150 a 158

        - SS7/ISUP parameter Called Party Number

        - Address signals = národný cieľový kód (NDC) + číslo tiesňového volania + číslo atrakčného obvodu v tvare XY podľa zoznamu určeného ministerstvom a zverejneného na webovom sídle ministerstva + sieťové smerovacie číslo (NRN)

        - Nature of Address indicator = national (significant) number

      - ČASŤ D Pravidlá smerovania tiesňových volaní na základe signalizácie koncového zariadenia mobilnej siete

        - 1. Mobilné siete druhej generácie a tretej generácie

          - Na základe obsahu oktetu 3 informačného elementu Service Category generovaného koncovým zariadením mobilnej siete v rámci protokolu CC (Call Control)<sup>16</sup>) sa tiesňové volania smerujú takto:

          - Oktet 3 informačného elementu Service Category – Emergency Service Category Value |

          - Hodnota bitov | Smerovanie

          - Bit 1 (Police) = 1, ostatné bity = 0 | NDC+158+číslo atrakčného obvodu+NRN

          - Bit 2 (Ambulance) = 1, ostatné bity = 0 | NDC+155+NRN​

          - Bit 3 (Fire Brigade) = 1, ostatné bity = 0 | NDC+150+číslo atrakčného obvodu+NRN

          - Bit 4 (Marine Guard) = 1, ostatné bity = 0 | NDC+112+NRN

          - Bit 5 (Mountain Rescue) = 1, ostatné bity = 0 | NDC+112+NRN

          - Bit 6 (Manually Initiated eCall) = 1, ostatné bity = 0 | NDC+11202+NRN

          - Bit 7 (Automatically Initiated eCall) = 1, ostatné bity = 0 | NDC+11201+NRN

          - Bit 8 (Spare) = 1, ostatné bity = 0 | NDC+112+NRN

          - Všetky bity nastavené na hodnotu 0 | NDC+112+NRN

          - Dva a viac bitov nastavených na hodnotu 1, vrátane situácie, keď sú naraz nastavené bity 6 aj 7 na hodnotu 1 | NDC+112+NRN

        - 2. Mobilné siete štvrtej generácie a piatej generácie

          - Na základe obsahu Request-URI prenášaného v počiatočnom riadku signalizačnej správy INVITE signalizačného protokolu SIP generovaného koncovým zariadením mobilnej siete<sup>17</sup>) sa tiesňové volania smerujú takto:

          - Request-URI obsahujúci identitu tiesňovej služby |

          - Jednotný názov zdroja (URN) | Smerovanie

          - urn:service:sos | NDC+112+NRN

          - urn:service:sos.fire | NDC+150+číslo atrakčného obvodu+NRN

          - urn:service:sos.ambulance | NDC+155+NRN

          - urn:service:sos.police | NDC+158+číslo atrakčného obvodu+NRN

          - urn:service:sos.* (* znamená akýkoľvek iný reťazec, vrátane marine a mountain) | NDC+112+NRN
