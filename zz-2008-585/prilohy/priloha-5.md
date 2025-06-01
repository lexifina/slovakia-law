Príloha č. 5 k vyhláške č. 585/2008 Z. z. HLÁSENIE ÚDAJOV O VÝKONE OČKOVANIA

Predkladá: Lekár, ktorý vykonáva povinné pravidelné očkovanie osôb, ktoré dosiahli určený vek

Frekvencia: Jedenkrát mesačne do 15. dňa nasledujúceho mesiaca

Štruktúra: Jeden záznam pre každý plánovaný výkon očkovania v kalendárnom mesiaci podľa platného

očkovacieho kalendára

Identifikačná časť: PZS – poskytovateľ zdravotnej starostlivosti (lekár)

Položka | Typ int*, char** | Opis | Poznámka

Mesiac hlásenia | int (2) | Kalendárny mesiac, za ktorý sa hlásia údaje |

Dátum odoslania | ddmmrrrr | Dátum odoslania súboru |

Počet záznamov | int (5) | Počet záznamov v súbore |

Kód PZS | char (12) | Kód poskytovateľa zdravotnej starostlivosti |

Názov PZS | char (40) | |

Ulica PZS | char (20) | |

Orientačné číslo PZS | char (6) / int (6) | |

Obec PZS | char (30) | Kód obce |

Email PZS | char (40) | |

Kód lekára | char (9) | Kód lekára |

Meno lekára | char (20) | |

Priezvisko lekára | char (30) | |

* int = číslo (v zátvorke je uvedený počet možných číslic)

** char = písmeno (v zátvorke je uvedený počet možných písmen)

Údajová časť: Očkovaná osoba

Položka | Typ int*, char** | Opis | Poznámka

Číslo záznamu | int (5) | Poradové číslo záznamu v súbore |

Meno | char (15) | |

Priezvisko | char (20) | |

Rodné číslo | char (10) | |

Dátum narodenia | ddmmrrrr | |

Zdravotná poisťovňa | int (4) | Kód zdravotnej poisťovne | Zdravotná poisťovňa platná k dátumu očkovania

Ulica | char (20) | |

Orientačné číslo | char (6)/int (6) | |

Obec | char (30) | Kód obce |

Zaočkovaný | int (1) | 0 – nie, 1 – áno |

Dátum pozvania | ddmmrrrr | Dátum pozvania na očkovanie | Deň, na ktorý je pacient objednaný

Dátum očkovania | ddmmrrrr | Dátum výkonu očkovania |

Dávka | int (1) | 1 (1. dávka), 2 (2. dávka), 3 (3. dávka), 4 (preočkovanie), 5 (iné očkovanie ako povinné) |

Druh očkovacej látky | int (3) | Číselník | Názov očkovacej látky

Šarža očkovacej látky | char (15) | V definovanej štruktúre |

Vedľajšie účinky | int (1) | 0 – nie, 1 – áno | Pri zaočkovaní

Kontraindikácie | int (1) | 1 – dočasné, 2 – trvalé | Pri nezaočkovaní

* int = číslo (v zátvorke je uvedený počet možných číslic)

** char = písmeno (v zátvorke je uvedený počet možných písmen)
