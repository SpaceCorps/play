<!-- wiki-i18n source: f06b4c7b561b1789 -->
<!-- wiki-i18n title: Pirate-raj -->
# Pirate-raj {#pirate-swarm}

A Pirate-raj egy **Pirate Boss** a **Pirate Scoutjaival**: egy hatalmas, lassú hajó, amely senkit sem támad meg, és rakétákkal válaszol, meg egy gyorsabb hajókból álló csapat, amely őrzi és gyógyítja. Egy vállalat bázisa és határa közötti szektorokban él, ahol a játék középső szintjeit játsszák, és hosszú harc egy pilótacsoportnak, nem gyors kilövés.

## Röviden {#at-a-glance}

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Hol**: Minden vállalat `x-2` és `x-3` szektora
- **Hány**: Egy-egy az ilyen szektorokban, világonként 6
- **Megjelenik**: A szezon 4. napjától a wipe-ig
- **Vezér**: Pirate Boss
- **Kísérők**: Legfeljebb 5 × Pirate Scout, mindig 10 mp múlva egy újabb
- **A kísérők közel maradnak**: legfeljebb 900 egységre a vezértől
- **Gyógyítás**: Minden Pirate Scout, amely a vezértől 600 egységen belül van, gyógyítja a hajótestét, Alphában másodpercenként 40 HP-t
- **A vezér megsemmisül**: A kísérők a vezér megsemmisülése után 1 perc múlva eltűnnek, kivéve ha éppen támadnak
- **Visszatér**: 2 perc azután, hogy a vezér megsemmisült, ugyanabban a szektorban
- **Értesítés**: A szektor pilótái értesülnek arról, mikor jelenik meg a vezér, és mikor semmisül meg. Ezek rendszersorok: a chat **Rendszer** lapján jelennek meg, olvasatlan sorok számlálójával, és nem a **Globális** vagy a **Helyi** lapon. A kill feed megnevezi a pilótát, akinek a kilövést jóváírják.

<!-- pirate-glance:end -->

## A tagok {#the-members}

- **Pirate Boss**: az Ironcladre épülő hajó, annak erejének egy részével (az értékek lent vannak). Passzív, és **nem lő lézerekkel**: az egyetlen fegyvere egy **egyenes rakéta** ([Rakéták](/wiki/06-Items/Rockets.md); hogy melyik, az a szektortól függ, lásd a táblázatot) arra a pilótára, aki megtámadta, és lövés közben tovább kóborol. A hajótestét soha nem javítja meg magától.
- **Pirate Scout**: a Kitefinre épülő hajó, annak erejének egy részével. A Scoutok megtámadnak minden pilótát, aki a közelükbe ér, a boss közelében maradnak, és mindegyik, amelyik a boss közelében van, gyógyítja a hajótestét.

## A harc menete {#how-the-fight-goes}

- **A bosst lődd, ne a Scoutokat.** A Scoutok gyógyítják a bosst, de a gyógyítás kicsi a boss hajótestéhez képest, és új Scout olyan gyakran érkezik, ahogy a *Röviden* lista mondja: az a csoport, amelyik előbb a Scoutokat lövi, sosem kerül előnybe velük szemben, és csak egy nagyon nagy csoport tudja kitakarítani őket, mégis tovább tart neki a boss befejezése, mint annak, amelyik békén hagyta őket. A Scoutok időt vesznek el tőled, a harcot nem ők döntik el.
- **Vezesd el a Scoutokat.** A Scout csak addig gyógyít, amíg a boss hatótávján belül van, így az a Scout, amelyik a hatótávon kívülre követ téged, semmit sem gyógyít, és az Ostirion gyorsabb a Scoutnál.
- **Mozogj folyamatosan.** A boss rakétája egyenes és nem önirányító: a folyamatosan mozgó hajó kitér előle, az álló hajót eltalálja.
- **Hozz csoportot.** Három Ostirion-pilóta x2 lőszerrel nagyjából öt perc alatt leterítheti Alphában; egy Ostirion egyedül nem, egy Paragon egyedül igen. A boss az első pilótának válaszol, aki eltalálta, ezért a legellenállóbb hajó kezdje, és használd a képességeidet (Emergency Repair, Shield Surge: [Képességek](/wiki/03-Mechanics/Abilities.md)) egy ilyen hosszú harcban. A még 2. vagy 3. szintű pilóták túl gyengék hozzá, még ott is, ahol repülnek: maradj távol, amíg erősebb nem leszel.
- **A boss visszatér** a *Röviden* lista szerinti idő múlva, ugyanabban a szektorban.

## Jutalmak és zsákmány {#rewards-and-drops}

A Pirate Boss a harc értékéhez mérten fizet: egy perc harc vele többet fizet, mint egy perc harc egy Goombah ellen. A fizetést a sebzés szerint osztják el a vele harcoló pilóták között ([hogyan fizet egy boss megölése](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). A ládája annak a pilótának jár, aki a legtöbb sebzést okozta, és tartalmazhat **Reinforced Hull Plate**-et, rakétákat és lőszert. A Scoutok keveset fizetnek, és nem ejtenek semmit.

## A számok {#the-numbers}

A raj hajóinak értékei mindhárom világban ([Világok](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss {#pirate-boss}

Alapja: Ironclad, hajótestének, pajzsának és sebzésének 50%-a; a sebessége és a hatótávja a mintahajóé. 5 mp alatt egy egyenes rakétát lő ki: [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets): `x-2`, [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets): `x-3`.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | 300 000 | 450 000 | 600 000 |
| Pajzs | 50 100 | 75 150 | 100 200 |
| Lézersebzés (másodpercenként egy sorozat) | nincs | nincs | nincs |
| Sebesség | 92 | 92 | 92 |
| Lézer hatótávja | – | – | – |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Rakétasebzés, legfeljebb | 2 500 (Rivet I) / 5 000 (Rivet II) | 3 750 (Rivet I) / 7 500 (Rivet II) | 5 000 (Rivet I) / 10 000 (Rivet II) |
| Kredit | 145 000 | 290 000 | 435 000 |
| Thulium | 725 | 1 450 | 2 175 |
| Tapasztalat (XP) | 29 000 | 58 000 | 87 000 |
| Becsület | 232 | 464 | 696 |
| PvE-pont kilövésenként | 10 | 10 | 10 |

**Zsákmány**: egy láda, annak a pilótának, aki a legtöbb sebzést okozta.

| Tárgy | Esély | Mennyiség |
| :--- | ---: | ---: |
| Reinforced Hull Plate | 50% | 1 |
| Egy a kreditért vásárolható 8 [rakéta](/wiki/06-Items/Rockets.md) közül, véletlenszerűen | 100% | 5–10 |
| Egy a következők közül: Advanced Plasma és Siphon Battery, véletlenszerűen | 100% | 500–1 000 |

### Pirate Scout {#pirate-scout}

Alapja: Kitefin, hajótestének, pajzsának és sebzésének 50%-a; a sebessége és a hatótávja a mintahajóé.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | 12 000 | 18 000 | 24 000 |
| Pajzs | 9 818 | 14 727 | 19 636 |
| Lézersebzés (másodpercenként egy sorozat) | 98 | 147 | 196 |
| Sebesség | 175 | 175 | 175 |
| Lézer hatótávja | 700 | 700 | 700 |
| Aggrósugár | 700 | 700 | 700 |
| Gyógyítja a vezért, egyenként, másodpercenként (csak hajótest) | 40 | 60 | 80 |
| Kredit | 1 000 | 2 000 | 3 000 |
| Thulium | 4 | 8 | 12 |
| Tapasztalat (XP) | 100 | 200 | 300 |
| Becsület | 2 | 4 | 6 |
| PvE-pont kilövésenként | 1 | 1 | 1 |

**Zsákmány**: nincs. A kilövés csak a kreditjét, Thuliumát, XP-jét és becsületét fizeti.

<!-- pirate-members:end -->
