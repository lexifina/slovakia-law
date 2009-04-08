Príloha č. 1 k vyhláške č. 135/2009 Z. z.

- PODPISOVÉ SCHÉMY, ŠIFROVACIE ALGORITMY A ICH PARAMETRE

  - Podpisové schémy

- Podpisová schéma | Asymetrický algoritmus | Minimálne parametre asymetrického algoritmu | Algoritmus na generovanie kľúčov | Metóda na doplnenie (padding) | Hašovacia funkcia

- 001 | RSA | MinModLen=1 020 | rsagen1 | emsa-pkcs- v1_5, 2_0, 2_1 | SHA1

- 002 | RSA | MinModLen=1 020 | rsagen1 | emsa-pss | SHA1

- 003 | RSA | MinModLen=1 020 | rsagen1 | emsa-pkcs- v1_5, 2_0, 2_1 | RIPEMD160

- 004 | RSA | MinModLen=1 020 | rsagen1 | emsa-pss | RIPEMD160

- 005 | DSA | pMinLen=1 024 qMinLen=160 | dsagen1 | – | SHA1

- 006 | ECDSA-Fp | qMinLen=160 r0Min=10 000 MinClass=200 | ecgen1 | – | SHA1

- 007 | ECDSA-F2m | qMinLen=160 r0Min=10 000 MinClass=200 | ecgen2 | – | SHA1

- 008 | ECGDSA-Fp | qMinLen=160 r0Min=10 000 MinClass=200 | ecgen1 | – | SHA1

- 009 | ECGDSA-F2m | qMinLen=160 r0Min=10 000 MinClass=200 | ecgen2 | – | SHA1

  - Algoritmy na generovanie kľúčov

- Označenie generátora kľúčov | Používané označenie | Asymetrický algoritmus | Metóda generovanie náhodných čísel | Parametre náhodného generátora

- 4.01 | rsagen1 | RSA | trueran | EntropyBits = 128

- 4.02 | dsagen1 | DSA | trueran alebo pseuran (FIPS 186-2) | EntropyBits = 128 alebo SeedLen = 128

- 4.03 | ecgen1 | ECDSA-Fp alebo ECGDSA-Fp | trueran alebo pseuran | EntropyBits = 128 alebo SeedLen = 128

- 4.04 | ecgen2 | ECDSA-F2m alebo ECGDSA-F2m | trueran alebo pseuran | EntropyBits = 128 alebo SeedLen = 128

  - Metódy generovania náhodných čísel

- Označenie náhodného generátora | Používané meno | Parametre náhodného generátora

- 5.01 | Trueran | EntropyBits

- 5.02 | Pseuran | SeedLen

- 5.03 | FIPS 186-2-31 | SeedLen

- 5.04 | FIPS 186-2-32 | SeedLen

  - Hašovacie funkcie

- Označenie hašovacej funkcie | Používané meno | Doba platnosti

- 2.01 | SHA1 | Do 31. 12. 2009

- 2.02 | RIPEMD160 | Do 31. 12. 2014

- 2.03 | SHA-224 | -

- 2.04 | SHA-256 | -

- 2.05 | SHA-384 | -

- 2.06 | SHA-512 | -

- 2.07 | Whirlpool | Do 31. 12. 2014
