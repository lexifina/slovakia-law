Príloha č. 1 k vyhláške č. 135/2009 Z. z.

- PODPISOVÉ SCHÉMY

  - Podpisová schéma je tvorená postupnosťou označení uvedených v tejto prílohe, oddelených bodkočiarkou, kde ako prvé sa uvádza označenie podpisového algoritmu.<sup>4</sup>)

  - Hašovacie funkcie

- Označenie hašovacejfunkcie | Používané meno | Doba platnosti

- 1.01 | sha1 | Do 31. 12. 2010

- 1.02 | ripemd160 | Do 31. 12. 2010

- 1.03 | sha224 | neurčená

- 1.04 | sha256 | neurčená

- 1.05 | whirlpool | neurčená

- 1.06 | sha384 | neurčená

- 1.07 | sha512 | neurčená

  - Podpisové algoritmy

- Označenie podpisového algoritmu | Podpisový algoritmus | Algoritmy generovania kľúčov | Podpisový algoritmus podľa minimálnej veľkosti parametrov a doba jeho použitia

- 2.01 | rsa | rsagen1 | MinModLen=1024, ErrProb= 2<sup>-80</sup>, SeedEntropy/EntropyBits=80 – do 31. 12. 2010 MinModLen=2048, ErrProb= 2<sup>-100</sup>, SeedEntropy/EntropyBits=100

- 2.02 | dsa | dsagen1 | pMinLen=1024, qMinLen= 160, ErrProb=2<sup>-80</sup>, SeedEntropy/EntropyBits=80 – do 31. 12. 2010 pMinLen=2048, qMinLen=224, ErrProb=2<sup>-100</sup>, SeedEntropy/EntropyBits=100

- 2.03 | ecdsa-Fp | ecgen1 | pMinLen=-, qMinLen=160, r0Min=104, MinClass=200, ErrProb=2<sup>-80</sup>, SeedEntropy/EntropyBits=80 – do 31. 12. 2010 pMinLen=-, qMinLen=224, r0Min=104, MinClass=200, ErrProb=2<sup>-100</sup>, SeedEntropy/EntropyBits=100

- 2.04 | ecdsa-F2m | ecgen2 | mMin=-, qMinLen=160, r0Min=104, MinClass=200, ErrProb=2<sup>-80</sup>, SeedEntropy/EntropyBits=80 – do 31. 12. 2010 mMin=-, qMinLen=224, r0Min=104, MinClass=200, ErrProb=2<sup>-100</sup>, SeedEntropy/EntropyBits=100

- 2.05 | ecgdsa-Fp | ecgen1 | pMinLen=-, qMinLen=160, r0Min=104, MinClass=200, ErrProb=2<sup>-80</sup>, SeedEntropy/EntropyBits=80 – do 31. 12. 2010 pMinLen=-, qMinLen=224, r0Min=104, MinClass=200, ErrProb=2<sup>-100</sup>, SeedEntropy/EntropyBits=100

- 2.06 | ecgdsa-F2m | ecgen2 | mMin=-, qMinLen=160, r0Min=104, MinClass=200, ErrProb=2<sup>-80</sup>, SeedEntropy/EntropyBits=80 – do 31. 12. 2010 mMin=-, qMinLen=224, r0Min=104, MinClass=200, ErrProb=2<sup>-100</sup>, SeedEntropy/EntropyBits=100

  - Algoritmy na generovanie kľúčových párov

- Označenie generátora kľúčov | Používané označenie | Podpisový algoritmus | Metóda generovania náhodných čísel | Parametre náhodného generátora

- 3.01 | rsagen1 | rsa | trueran | EntropyBits

- 3.02 | dsagen1 | dsa | trueran alebo pseuran | EntropyBits alebo SeedEntropy

- 3.03 | ecgen1 | ecdsa-Fp, ecgdsa-Fp | trueran alebo pseuran | EntropyBits alebo SeedEntropy

- 3.04 | ecgen2 | ecdsa-F2m, ecgdsa-F2m | trueran alebo pseuran | EntropyBits alebo SeedEntropy

  - Metódy na doplnenie (padding)

- Označenie metódy na doplnenie | Používané označenie | Metóda generovania náhodných čísel | Parametre náhodného generátora

- 4.01 | emsa-pkcs1-v1.5 | – | –

- 4.02 | emsa-pkcs1-v2.1 | – | –

- 4.03 | emsa-pss | trueran/pseuran | MinSaltEntropy

- 4.04 | iso9796ds2 | trueran/pseuran | MinSaltEntropy

- 4.05 | iso9796-din-rn | trueran/pseuran | MinSaltEntropy

- 4.06 | iso9796ds3 | – | –

  - Metódy generovania náhodných čísel

- Označenie metódy generovania | Používané označenie | Parametre náhodného generátora

- 5.01 | trueran | EntropyBits

- 5.02 | pseuran | SeedEntropy
