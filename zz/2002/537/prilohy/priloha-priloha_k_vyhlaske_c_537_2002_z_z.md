Príloha k vyhláške č. 537/2002 Z. z.

- PODPISOVÉ SCHÉMY, ŠIFROVACIE ALGORITMY A ICH PARAMETRE

- Podpisové schémy

- Podpisová schéma | Asymetrický algoritmus | Minimálne parametre asymetrického algoritmu | Algoritmus na generovanie kľúčov | Metóda na doplnenie (padding) | Hašovacia funkcia

- 001 | RSA | MinModLen= 1020 | rsagen1 | emsa-pkcs-vl_5, 2_0, 2_1 | SHA1

- 002 | RSA | MinModLen= 1020 | rsagen1 | emsa-pss | SHA1

- 003 | RSA | MinModLen= 1020 | rsagen1 | emsa-pkcs-vl_5, 2_0, 2_1 | RIPEMD160

- 004 | RSA | MinModLen= 1020 | rsagen1 | emsa-pss | RIPEMD160

- 005 | DSA | pMinLen=1024 | dsagen1 | - | SHA1

- | | qMlnLen=160 | | |

- 006 | ECDSA-Fq | qMlnLen=160 rOMin= 10000 | ecgen1 | - | SHA1

- | | MinClass=200 | | |

- 007 | ECDSA-F2m | qMinLen=160 | ecgen1 | - | SHA1

- | | r0Min= 10000 | | |

- | | MinClass=200 | | |

- Algoritmy na generovanie kľúčov

Označenie generátora kľúčov | Používané označenie | Asymetrický algoritmus | Metóda generovania náhodných čísel | Parametre náhodného generátora

4.01 | rsagen1 | RSA | trueran | EntropyBits =128

4.02 | dsagen1 | DSA | trueran alebo pseuran (FIPS 186-2) | EntropyBits =128 alebo SeedLen =128

4.03 | ecgen1 | ECDSA-Fq alebo ECDSA-F2m | trueran alebo pseudoran | EntropyBits =128 alebo SeedLen =128

- Metódy generovania náhodných čísel

- Označenie náhodného generátora | Používané meno | Parametre náhodného generátora

- 5.01 | trueran | EntropyBits

- 5.02 | pseuran | SeedLen

- 5.03 | FIPS 186-2-31 | SeedLen

- 5.04 | FIPS 186-2-32 | SeedLen

- Hašovacie funkcie

- Označenie hašovacej funkcie | Používané meno

- 2.01 | SHA1

- 2.02 | RIPEMD160
