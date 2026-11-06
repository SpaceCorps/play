<!-- wiki-i18n source: 7859e3f6a7efac1e -->
<!-- wiki-i18n title: Goombah-raj -->
# Goombah-raj {#goombah-swarm}

A Goombah-raj egy **Boss Goombah** és a **Goombah Guardjai**: egy óriási [Goombah](/wiki/04-Aliens/Goombah.md), amely soha nem kezd harcot, és kisebbek, amelyek a közelében maradnak, és gyógyítják. Ugyanazokban a szektorokban él, mint a [Phantasm-raj](/wiki/05-Swarms/Phantasm-Swarm.md), az `x-3` és az `x-4` szektorban, és a vállalati szektorok legerősebb pilótái csoportjának való harc.

## Röviden {#at-a-glance}

<!-- goombah-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Hol**: Minden vállalat `x-3` és `x-4` szektora
- **Hány**: Egy-egy az ilyen szektorokban, világonként 6
- **Megjelenik**: A szezon 4. napjától a wipe-ig (Betában és Gammában: a szezon 1. napjától)
- **Vezér**: Boss Goombah
- **Kísérők**: Legfeljebb 4 × Goombah Guard, mindig 10 mp múlva egy újabb
- **A kísérők közel maradnak**: legfeljebb 500 egységre a vezértől
- **Gyógyítás**: Minden Goombah Guard, amely a vezértől 600 egységen belül van, gyógyítja a hajótestét, Alphában másodpercenként 110 HP-t
- **A vezér megsemmisül**: A kísérők a vezér megsemmisülése után 30 mp múlva eltűnnek, kivéve ha éppen támadnak
- **Visszatér**: 5 perc azután, hogy a vezér megsemmisült, ugyanabban a szektorban
- **Értesítés**: A szektor pilótái értesülnek arról, mikor jelenik meg a vezér, és mikor semmisül meg. Ezek rendszersorok: a chat **Rendszer** lapján jelennek meg, olvasatlan sorok számlálójával, és nem a **Globális** vagy a **Helyi** lapon. A kill feed megnevezi a pilótát, akinek a kilövést jóváírják.

<!-- goombah-glance:end -->

## A tagok {#the-members}

- **Boss Goombah**: egy nagyobb Goombah, a raj színezésében és a nevével fölötte, saját hajótesttel, pajzzsal és lézersortűzzel (az értékek lent vannak). Passzív: kóborol, amíg egy pilóta el nem találja, aztán arra a pilótára támad és tüzel, és a raj közeli hajói beszállnak a harcba. A fegyverének hatótávja és a sebessége egy Goombahé, a hajótestét pedig soha nem javítja meg magától.
- **Goombah Guard**: egy kisebb Goombah a raj színezésében. A Guardok a boss közelében maradnak, beszállnak a harcba, ha egy közeli rajhajót eltalálnak, és mindegyik, amelyik a boss közelében van, gyógyítja a hajótestét. A Guard egy kis pihenő után megjavítja a saját hajótestét, ahogy egy Goombah is.

## A harc menete {#how-the-fight-goes}

- **Vigyél csoportot a legerősebb hajókból.** Három 8. szintű pilóta x2 lőszerrel Alphában nagyjából 75 másodperc alatt megsemmisíti, legfeljebb egy hajót veszítve; közülük kettőnek x4 lőszer kell, az alacsonyabb szintű pilóták pedig nem okoznak elég sebzést a győzelemhez.
- **A bossra lőj, ne a Guardokra.** Egy Guard másodpercek alatt elesik, de a *Röviden* lista szerinti gyakorisággal új érkezik, és amit a Guardok gyógyítanak, az csak kis része annak, amit egy csoport okoz: ha békén hagyod őket, az kis időbe kerül, ha üldözöd őket, többe.
- **A Beta és a Gamma keményebb.** Ezeknek a világoknak a rajai erősebbek ([Világok](/wiki/05-Swarms/Swarms.md#the-worlds)), ezért több pilóta vagy jobb lőszer kell.
- **Figyeld a szektort.** Az `x-4` Alphában PvP-szektor, az `x-3` és az `x-4` pedig Betában és Gammában az ([Világok](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): egy rivális beléphet a harcba, vagy megvárhatja a ládát. Hagyj egy hajót a csoportból őrségben.
- **A boss visszatér** a *Röviden* lista szerinti idő múlva, teljes erővel, ugyanabban a szektorban, a Guardjai pedig egymás után érkeznek.

## Jutalmak és zsákmány {#rewards-and-drops}

A Boss Goombah annyit fizet, amennyi a harc, amit jelent: egy perc harc vele többet fizet, mint egy perc harc egy Goombah ellen, ezeknek a szektoroknak a legjobban fizető idegenje ellen. A fizetést a sebzés szerint osztják el a vele harcoló pilóták között ([hogyan fizet egy boss megölése](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). A ládája annak a pilótának jár, aki a legtöbb sebzést okozta, és egy Goombah saját zsákmányát tartalmazza többszörösen (Cataclysite, Quorvium, Power Core, Reinforced Hull Plate és Ship Fragment), lőszerrel és rakétákkal. A Guardok keveset fizetnek, és nem ejtenek semmit; a kilövésük nem farmolás, mert a bossal együtt visszatérnek.

## A számok {#the-numbers}

A raj hajóinak értékei mindhárom világban ([Világok](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- goombah-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Goombah

Alapja: Goombah, hajótestének 400%-a és lézersebzésének 100%-a; a sebessége és a hatótávja a mintahajóé.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | 128 000 | 192 000 | 256 000 |
| Pajzs | 192 000 | 288 000 | 384 000 |
| Lézersebzés (másodpercenként egy sorozat) | 3 000 | 4 500 | 6 000 |
| Sebesség | 180 | 180 | 180 |
| Lézer hatótávja | 800 | 800 | 800 |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Kredit | 120 000 | 240 000 | 360 000 |
| Thulium | 600 | 1 200 | 1 800 |
| Tapasztalat (XP) | 24 000 | 48 000 | 72 000 |
| Becsület | 192 | 384 | 576 |
| PvE-pont kilövésenként | 14 | 14 | 14 |

**Zsákmány**: egy láda, annak a pilótának, aki a legtöbb sebzést okozta.

| Tárgy | Esély | Mennyiség |
| :--- | ---: | ---: |
| Ship Fragment | 100% mind a 8 dobásnál | 3 |
| Reinforced Hull Plate | 60% mind a 8 dobásnál | 1 |
| Power Core | 25% mind a 8 dobásnál | 1 |
| Cataclysite | 100% mind a 8 dobásnál | 4 |
| Quorvium | 100% mind a 8 dobásnál | 2–4 |
| Advanced Plasma | 100% | 100–200 |
| Ultra Core | 100% | 100–200 |
| Egy a kreditért vásárolható 8 [rakéta](/wiki/06-Items/Rockets.md) közül, véletlenszerűen | 100% | 6–10 |

### Goombah Guard

Alapja: Goombah, hajótestének, pajzsának és sebzésének 20%-a; a sebessége és a hatótávja a mintahajóé.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | 6 400 | 9 600 | 12 800 |
| Pajzs | 9 600 | 14 400 | 19 200 |
| Lézersebzés (másodpercenként egy sorozat) | 600 | 900 | 1 200 |
| Sebesség | 180 | 180 | 180 |
| Lézer hatótávja | 800 | 800 | 800 |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Gyógyítja a vezért, egyenként, másodpercenként (csak hajótest) | 110 | 165 | 220 |
| Kredit | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Tapasztalat (XP) | 12 | 24 | 36 |
| Becsület | 1 | 2 | 3 |
| PvE-pont kilövésenként | 3 | 3 | 3 |

**Zsákmány**: nincs. A kilövés csak a kreditjét, Thuliumát, XP-jét és becsületét fizeti.

<!-- goombah-members:end -->
