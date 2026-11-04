<!-- wiki-i18n source: 62896aebea81e95a -->
<!-- wiki-i18n title: Crystalys-raj -->
# Crystalys-raj {#crystalys-swarm}

A Crystalys-raj egy **Boss Crystalys** és a **Crystalys Guardjai**: a legszívósabb idegen, a [Crystalys](/wiki/04-Aliens/Crystalys.md) megnagyobbítva, őrökkel, amelyek a közelében maradnak, és gyógyítják. A [veszélyes szektorok](/wiki/01-General/Danger-Sectors.md) közül a `DS-1`, `DS-2` és `DS-3` szektorban él, mindegyikben egy, és soha nem hagyja el a szektorát. A veszélyes szektorok PvP-szektorok, ezért a harc a legerősebb pilóták nagy csoportjának való, és a boss nem az egyetlen veszély ott.

## Röviden {#at-a-glance}

<!-- crystalys-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Hol**: A veszélyes szektorok: `DS-1`, `DS-2`, `DS-3`
- **Hány**: Egy-egy az ilyen szektorokban, világonként 3
- **Megjelenik**: A szezon 4. napjától a wipe-ig
- **Vezér**: Boss Crystalys
- **Kísérők**: Legfeljebb 3 × Crystalys Guard, mindig 10 mp múlva egy újabb
- **A kísérők közel maradnak**: legfeljebb 500 egységre a vezértől
- **Gyógyítás**: Minden Crystalys Guard, amely a vezértől 600 egységen belül van, gyógyítja a hajótestét, Alphában másodpercenként 250 HP-t
- **A vezér megsemmisül**: A kísérők a vezér megsemmisülése után 30 mp múlva eltűnnek, kivéve ha éppen támadnak
- **Visszatér**: 30 perc azután, hogy a vezér megsemmisült, ugyanabban a szektorban
- **Értesítés**: A szektor pilótái értesülnek arról, mikor jelenik meg a vezér, és mikor semmisül meg. Ezek rendszersorok: a chat **Rendszer** lapján jelennek meg, olvasatlan sorok számlálójával, és nem a **Globális** vagy a **Helyi** lapon. A kill feed megnevezi a pilótát, akinek a kilövést jóváírják.

<!-- crystalys-glance:end -->

## A tagok {#the-members}

- **Boss Crystalys**: egy nagyobb Crystalys, a raj színezésében és a nevével fölötte, saját hajótesttel, pajzzsal és lézersortűzzel (az értékek lent vannak). Passzív: kóborol, amíg egy pilóta el nem találja, aztán arra a pilótára támad és tüzel, és a raj közeli hajói beszállnak a harcba. A fegyverének hatótávja és a sebessége egy Crystalysé, a hajótestét pedig soha nem javítja meg magától.
- **Crystalys Guard**: egy kisebb Crystalys a raj színezésében. A Guardok a boss közelében maradnak, beszállnak a harcba, ha egy közeli rajhajót eltalálnak, és mindegyik, amelyik a boss közelében van, gyógyítja a hajótestét. A Guard egy kis pihenő után megjavítja a saját hajótestét, ahogy egy Crystalys is.

## A harc menete {#how-the-fight-goes}

- **Vigyél nagy csoportot.** Nyolc 8. szintű pilóta Paragonokban x2 lőszerrel Alphában nagyjából egy perc alatt megsemmisíti, legfeljebb egy hajót veszítve; négynek x4 lőszer kell, egy pilótát egyedül megsemmisítenek.
- **A bossra lőj, ne a Guardokra.** Egy Guard másodpercek alatt elesik, de a *Röviden* lista szerinti gyakorisággal új érkezik, és amit a Guardok gyógyítanak, az csak kis része annak, amit egy csoport okoz: ha békén hagyod őket, az kis időbe kerül, ha üldözöd őket, többe.
- **A Beta és a Gamma keményebb.** Ezeknek a világoknak a rajai erősebbek ([Világok](/wiki/05-Swarms/Swarms.md#the-worlds)), ezért több pilóta vagy jobb lőszer kell.
- **A veszélyes szektorok PvP-szektorok.** Egy rivális a harc közepén megtámadhatja a csoportot, és megvárhatja a ládát: az 30 másodpercig a legtöbb sebzést okozó pilótáé (és a klánjáé), utána bárkié ([Rakomány](/wiki/03-Mechanics/Cargo.md)). Ne egyedül menj.
- **A boss visszatér** a *Röviden* lista szerinti idő múlva, teljes erővel, ugyanabban a szektorban, a Guardjai pedig egymás után érkeznek.

## Jutalmak és zsákmány {#rewards-and-drops}

A Boss Crystalys annyit fizet, amennyi a harc, amit jelent: egy perc harc vele többet fizet, mint egy perc harc egy Crystalys ellen, a legjobban fizető idegen ellen. A fizetést a sebzés szerint osztják el a vele harcoló pilóták között ([hogyan fizet egy boss megölése](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). A ládája annak a pilótának jár, aki a legtöbb sebzést okozta, és Cataclysite-ot és Quorviumot tartalmaz, időnként egy Power Core-t, egy Ancient Control Unitot vagy Dark Mattert, x3 és x4 lőszert és Epikus rakétákat. A Guardok keveset fizetnek, és nem ejtenek semmit; a kilövésük nem farmolás, mert a bossal együtt visszatérnek.

## A számok {#the-numbers}

A raj hajóinak értékei mindhárom világban ([Világok](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- crystalys-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Crystalys

Alapja: Crystalys, hajótestének 175%-a és lézersebzésének 50%-a; a sebessége és a hatótávja a mintahajóé.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | 448 000 | 672 000 | 896 000 |
| Pajzs | 280 000 | 420 000 | 560 000 |
| Lézersebzés (másodpercenként egy sorozat) | 5 000 | 7 500 | 10 000 |
| Sebesség | 230 | 230 | 230 |
| Lézer hatótávja | 900 | 900 | 900 |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Kredit | 393 750 | 787 500 | 1 181 250 |
| Thulium | 1 050 | 2 100 | 3 150 |
| Tapasztalat (XP) | 63 000 | 126 000 | 189 000 |
| Becsület | 273 | 546 | 819 |
| PvE-pont kilövésenként | 21 | 21 | 21 |

**Zsákmány**: egy láda, annak a pilótának, aki a legtöbb sebzést okozta.

| Tárgy | Esély | Mennyiség |
| :--- | ---: | ---: |
| Cataclysite | 100% mind a 2 dobásnál | 8 |
| Quorvium | 100% mind a 2 dobásnál | 6–10 |
| Power Core | 30% | 1 |
| Ancient Control Unit | 15% | 1 |
| Dark Matter | 4% | 1 |
| Ultra Core és Experimental Fusion Core, egyenlően elosztva | 100% | összesen 600–1 000 |
| Egy a 4 Epikus [rakéta](/wiki/06-Items/Rockets.md) közül, véletlenszerűen | 100% | 8–15 |

### Crystalys Guard

Alapja: Crystalys, hajótestének, pajzsának és sebzésének 15%-a; a sebessége és a hatótávja a mintahajóé.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | 38 400 | 57 600 | 76 800 |
| Pajzs | 24 000 | 36 000 | 48 000 |
| Lézersebzés (másodpercenként egy sorozat) | 1 500 | 2 250 | 3 000 |
| Sebesség | 230 | 230 | 230 |
| Lézer hatótávja | 900 | 900 | 900 |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Gyógyítja a vezért, egyenként, másodpercenként (csak hajótest) | 250 | 375 | 500 |
| Kredit | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Tapasztalat (XP) | 12 | 24 | 36 |
| Becsület | 1 | 2 | 3 |
| PvE-pont kilövésenként | 6 | 6 | 6 |

**Zsákmány**: nincs. A kilövés csak a kreditjét, Thuliumát, XP-jét és becsületét fizeti.

<!-- crystalys-members:end -->
