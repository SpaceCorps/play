<!-- wiki-i18n source: 0ed9858d316d7ddd -->
<!-- wiki-i18n title: Seeker-raj -->
# Seeker-raj {#seeker-swarm}

A Seeker-raj a [rajok](/wiki/05-Swarms/Swarms.md) legkisebbike: egy **Boss Seeker** és a **Seeker Slave-ek**, amelyek őrzik és gyógyítják. Azokban a szektorokban él, ahol az új pilóták repülni kezdenek, ezért ez az első raj, amellyel a legtöbben találkoznak. A Boss Seeker soha nem kezd harcot, de ha rálősz, sokkal veszélyesebb, mint a [Seeker](/wiki/04-Aliens/Seeker.md), amelyre épül.

## Röviden {#at-a-glance}

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Hol**: Minden vállalat `x-1` és `x-2` szektora
- **Hány**: Egy-egy az ilyen szektorokban, világonként 6
- **Megjelenik**: A szezon 4. napjától a wipe-ig
- **Vezér**: Boss Seeker
- **Kísérők**: Legfeljebb 4 × Seeker Slave, mindig 10 mp múlva egy újabb
- **A kísérők közel maradnak**: legfeljebb 500 egységre a vezértől
- **Gyógyítás**: Minden Seeker Slave, amely a vezértől 600 egységen belül van, gyógyítja a hajótestét, Alphában másodpercenként 50 HP-t
- **A vezér megsemmisül**: A kísérők a vezér megsemmisülése után 30 mp múlva eltűnnek, kivéve ha éppen támadnak
- **Visszatér**: 2 perc azután, hogy a vezér megsemmisült, ugyanabban a szektorban
- **Értesítés**: A szektor pilótái értesülnek arról, mikor jelenik meg a vezér, és mikor semmisül meg. Ezek rendszersorok: a chat **Rendszer** lapján jelennek meg, olvasatlan sorok számlálójával, és nem a **Globális** vagy a **Helyi** lapon. A kill feed megnevezi a pilótát, akinek a kilövést jóváírják.

<!-- seeker-glance:end -->

## A tagok {#the-members}

- **Boss Seeker**: egy sokkal nagyobb Seeker, a raj színezésében és a nevével fölötte, egy Seeker hajótestének, pajzsának és sebzésének sokszorosával (az értékek lent vannak). Passzív: kóborol, amíg egy pilóta el nem találja, aztán megáll ott, ahol van, és arra a pilótára tüzel, és a raj közeli hajói beszállnak a harcba. A fegyverének hatótávja és a sebessége egy Seekeréé, a hajótestét pedig soha nem javítja meg magától.
- **Seeker Slave**: egy közönséges Seeker a raj színezésében. A Slave-ek a boss közelében maradnak, beszállnak a harcba, ha egy közeli rajhajót eltalálnak, és mindegyik, amelyik a boss közelében van, gyógyítja a hajótestét. A Slave egy kis pihenő után megjavítja a saját hajótestét, ahogy egy Seeker is.

## A harc menete {#how-the-fight-goes}

- **Hagyd békén, amíg a hajód nem bírja el.** A Boss Seeker keményebben üt, mint amit egy pilóta első hajója elbír: az új pilóta pajzs nélküli Protosát másodpercek alatt megsemmisítik, amint a boss és a Slave-jei rákerülnek.
- **Maradj hatótávon kívül.** A boss és a Slave-ek lassabbak egy Protosnál, a fegyvereik pedig kevésbé hatnak el messzire, mint egy Quantum Laser 2 (lásd [Lézerek és lőszer](/wiki/06-Items/Lasers.md)): aki ilyen lézerekkel repül, és a hatótávjukon kívül marad, nem szenved sebzést, miközben tüzelnek. A Quantum Laser 1-es pilóta nem tud hatótávon kívül maradni.
- **A Slave-ek gyorsabban gyógyítanak, mint ahogy egy magányos új pilóta sebez.** Együtt többet gyógyítanak, mint amennyit egy pilóta lézerei okoznak x1 lőszerrel, ezért vigyél társat és x2 lőszert. Két Quantum Laser 2-es pilóta, aki tartja a távolságot, nagyjából egy perc alatt leteríti a bosst Alphában, x2 lőszerrel pedig sokkal gyorsabban.
- **A boss visszatér** a *Röviden* lista szerinti idő múlva, teljes erővel, ugyanabban a szektorban, a Slave-ei pedig egymás után érkeznek.

## Jutalmak és zsákmány {#rewards-and-drops}

A Boss Seeker **pontosan tíz Seekert** fizet: egy Seeker kreditjének, Thuliumának, XP-jének és becsületének tízszeresét, a sebzés szerint elosztva a vele harcoló pilóták között ([hogyan fizet egy boss megölése](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). A ládája tíz Seeker zsákmányát tartalmazza, ezen felül pedig az Epikus alatti lőszert és rakétákat, annak a pilótának, aki a legtöbb sebzést okozta. A Slave-ek keveset fizetnek, és nem ejtenek semmit; a kilövésük nem farmolás, mert a bossal együtt visszatérnek.

## A számok {#the-numbers}

A raj hajóinak értékei mindhárom világban ([Világok](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker

Alapja: Seeker, hajótestének, pajzsának és sebzésének 400%-a; a sebessége és a hatótávja a mintahajóé.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | 3 200 | 4 800 | 6 400 |
| Pajzs | 3 200 | 4 800 | 6 400 |
| Lézersebzés (másodpercenként egy sorozat) | 720 | 1 080 | 1 440 |
| Sebesség | 120 | 120 | 120 |
| Lézer hatótávja | 600 | 600 | 600 |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Kredit | 10 000 | 20 000 | 30 000 |
| Thulium | 40 | 80 | 120 |
| Tapasztalat (XP) | 1 000 | 2 000 | 3 000 |
| Becsület | 20 | 40 | 60 |
| PvE-pont kilövésenként | 5 | 5 | 5 |

**Zsákmány**: egy láda, annak a pilótának, aki a legtöbb sebzést okozta.

| Tárgy | Esély | Mennyiség |
| :--- | ---: | ---: |
| Ship Fragment | 20% mind a 10 dobásnál | 1 |
| Daraxium | 50% mind a 10 dobásnál | 1–2 |
| Standard Battery | 100% | 200–400 |
| Advanced Plasma | 100% | 10–20 |
| Ultra Core | 100% | 2–4 |
| Egy a kreditért vásárolható 8 [rakéta](/wiki/06-Items/Rockets.md) közül, véletlenszerűen | 100% | 2–3 |

### Seeker Slave

Alapja: Seeker, hajótestének, pajzsának és sebzésének 100%-a; a sebessége és a hatótávja a mintahajóé.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | 800 | 1 200 | 1 600 |
| Pajzs | 800 | 1 200 | 1 600 |
| Lézersebzés (másodpercenként egy sorozat) | 180 | 270 | 360 |
| Sebesség | 120 | 120 | 120 |
| Lézer hatótávja | 600 | 600 | 600 |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Gyógyítja a vezért, egyenként, másodpercenként (csak hajótest) | 50 | 75 | 100 |
| Kredit | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Tapasztalat (XP) | 12 | 24 | 36 |
| Becsület | 1 | 2 | 3 |
| PvE-pont kilövésenként | 1 | 1 | 1 |

**Zsákmány**: nincs. A kilövés csak a kreditjét, Thuliumát, XP-jét és becsületét fizeti.

<!-- seeker-members:end -->
