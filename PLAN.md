# The plan: every source a Slovak lawyer or citizen needs

This is the plan for this repository, part by part, with what is published so far. It is regenerated with each documentation commit, so the gap can be followed over time.

**15.3%** of the plan is published, weighted by how binding each source is and how often it is used. The Collection of Laws (Zbierka zákonov) lists 25,891 items since 1918; 5,817 of them are on `main`. Updated 2026-11-13 02:10 UTC.

| Part | Will be in | Weight | Progress | How | Status |
| --- | --- | ---: | --- | --- | --- |
| **Primary legislation** | | | | | |
| Constitution and constitutional acts | constitution/ustava/, volebny-zakon/; constitutional acts in zz/ and zb/ | 8.0% | 64 of 154 acts · 41.6% | the consolidated text of every version, credited to the amending act | collecting |
| Laws, legislative measures and decrees (in force and repealed) | zz/<year>/<number>/ (from 1993), zb/<year>/<number>/ (1918-1992) | 25.0% | 1,641 of 6,471 acts · 25.4% | Slov-Lex: every dated version of each act, then its repeal | collecting |
| Every consolidated version of each act | one commit per version, in the act's folder | 12.0% | 5,864 versions; target: Slov-Lex version lists being read (5,953 of 25,891) | each version credited to the act Slov-Lex names for it; earlier versions of the acts held as their current version follow | collecting |
| **Secondary legislation** | | | | | |
| Government regulations (nariadenia vlády) | zz/, zb/ | 7.0% | 809 of 3,683 acts · 22.0% | as the laws | collecting |
| Ministerial and authority regulations in the Collection (vyhlášky, výnosy, opatrenia, NBS) | zz/, zb/ | 10.5% | 3,303 of 8,468 regulations · 39.0% | as the laws | collecting |
| Ministerial bulletins and regulations outside the Collection (rezortné zbierky, Vestník NBS, regulators) | vestnik/<issuer>/ | 4.0% | target unknown | the issuers' own bulletins (Slov-Lex rezortné zbierky, NBS, ÚRSO) | planned |
| **Local acts** | | | | | |
| Bratislava: city council (VZN) | local/bratislava/ | 2.0% | target unknown | the city's own register of generally binding regulations (všeobecne záväzné nariadenia) | planned |
| Košice: city council (VZN) | local/kosice/ | 1.0% | target unknown | the city's own register of VZN | planned |
| Self-governing regions (8 VÚC) | local/kraj/<region>/ | 1.5% | 0 of 8 regions · 0.0% | each region's register of VZN | planned |
| Regional cities (Trnava, Trenčín, Nitra, Žilina, Banská Bystrica, Prešov) and Bratislava/Košice boroughs | local/<city>/ | 1.0% | 0 of 6 cities · 0.0% | each council's register of VZN | planned |
| Other municipalities (obce a mestá) | local/<district>/<municipality>/ | 2.5% | 0 of 2,890 municipalities · 0.0% | each council's official board or register, where it publishes in a machine-readable form | planned |
| **Case law** | | | | | |
| Constitutional Court findings published in the Collection (nálezy) | zz/, zb/ | 2.0% | 0 of 205 findings · 0.0% | the text published in the Collection of Laws | planned |
| Constitutional Court decisions (Ústavný súd SR) | judikatura/ustavny-sud/ | 5.0% | target unknown | the Court's own database; texts as the Court anonymises them | planned |
| Supreme Court and Supreme Administrative Court | judikatura/ns/, judikatura/nss/ | 4.0% | target unknown | the courts' own published decisions, as they anonymise them | planned |
| Other courts (anonymised decisions) | data/sudy/ (metadata and links) | 1.5% | target unknown | the Ministry of Justice's court-decision register: metadata and links | planned |
| **Parliament, President and elections** | | | | | |
| Resolutions and decisions in the Collection (amnesties, elections, parliament) | zz/, zb/ | 1.5% | 0 of 839 items · 0.0% | the text published in the Collection of Laws | planned |
| Parliament bills (NR SR parlamentné tlače) | data/navrhy/<term>.csv | 3.0% | target unknown | the National Council's own records of each bill, labelled not law | planned |
| Draft acts in public consultation (legislatívny proces) | navrh/<year>/ | 1.5% | target unknown | Slov-Lex's legislative process: drafts and explanatory reports, labelled not law | planned |
| **EU and international** | | | | | |
| Notices in the Collection (treaties, announced measures) | zz/, zb/ | 4.0% | 0 of 5,800 notices · 0.0% | the notices as published in the Collection (the Ministry of Foreign Affairs announces each treaty there) | planned |
| EU transposition links | data/eu-transpozicia.csv | 2.5% | target unknown | Slov-Lex's EU law register and the transposition clauses in the acts | planned |
| **Publications** | | | | | |
| Corrections and republished full texts in the Collection | zz/, zb/ | 0.5% | 0 of 271 items · 0.0% | as published in the Collection of Laws | planned |
| **Out of scope** | | | | | |
| Technical standards (STN), doctrine, commentaries | none | 0.0% | out of scope | standard numbers cited only (the texts are copyright) | not planned: copyright |

Progress counts what is on `main`; targets are the official counts where they exist (Slov-Lex's own year indexes and version lists, the courts' and councils' registers), otherwise "target unknown". Folders not on `main` yet will appear as the parts are published. Every text is copied from the official publisher named in its commit; nothing is written, summarised or translated.
