<!-- wiki-i18n source: 7c6bc3eaf70223f5 -->
<!-- wiki-i18n title: Seeker-raj -->
# Seeker-raj {#seeker-swarm}

A Seeker-raj a [rajok](/wiki/05-Swarms/Swarms.md) legkisebbike: egy **Boss Seeker** és a **Seeker Slave-ek**, amelyek őrzik és gyógyítják. Azokban a szektorokban él, ahol az új pilóták repülni kezdenek, ezért ez az első raj, amellyel a legtöbben találkoznak. A Boss Seeker soha nem kezd harcot, de ha rálősz, sokkal veszélyesebb, mint a [Seeker](/wiki/04-Aliens/Seeker.md), amelyre épül.

## Röviden {#at-a-glance}

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Hol**: Minden vállalat `x-1` és `x-2` szektora
- **Hány**: Egy-egy az ilyen szektorokban, világonként 6
- **Megjelenik**: A szezon 4. napjától a wipe-ig (Betában és Gammában: a szezon 1. napjától)
- **Vezér**: Boss Seeker
- **Kísérők**: Legfeljebb 4 × Seeker Slave, mindig 10 mp múlva egy újabb
- **A kísérők közel maradnak**: legfeljebb 500 egységre a vezértől
- **Gyógyítás**: Minden Seeker Slave, amely a vezértől 600 egységen belül van, gyógyítja a hajótestét, Alphában másodpercenként 50 HP-t
- **A vezér megsemmisül**: A kísérők a vezér megsemmisülése után 30 mp múlva eltűnnek, kivéve ha éppen támadnak
- **Visszatér**: {{guide:vitals.respawn@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} azután, hogy a vezér megsemmisült, ugyanabban a szektorban
- **Értesítés**: A szektor pilótái értesülnek arról, mikor jelenik meg a vezér, és mikor semmisül meg. Ezek rendszersorok: a chat **Rendszer** lapján jelennek meg, olvasatlan sorok számlálójával, és nem a **Globális** vagy a **Helyi** lapon. A kill feed megnevezi a pilótát, akinek a kilövést jóváírják.

<!-- seeker-glance:end -->

## A tagok {#the-members}

- **Boss Seeker**: egy sokkal nagyobb Seeker, a raj színezésében és a nevével fölötte, egy Seeker hajótestének, pajzsának és sebzésének sokszorosával (az értékek lent vannak). Passzív: kóborol, amíg egy pilóta el nem találja, aztán megáll ott, ahol van, és arra a pilótára tüzel, és a raj közeli hajói beszállnak a harcba. A fegyverének hatótávja és a sebessége egy Seekeréé, a hajótestét pedig soha nem javítja meg magától. A [három lépése](#the-leaders-three-steps) és egy [különleges képesség](/wiki/03-Mechanics/Special-Abilities.md) változtathat ezen.
- **Seeker Slave**: egy közönséges Seeker a raj színezésében. A Slave-ek a boss közelében maradnak, beszállnak a harcba, ha egy közeli rajhajót eltalálnak, és mindegyik, amelyik a boss közelében van, gyógyítja a hajótestét. A Slave egy kis pihenő után megjavítja a saját hajótestét, ahogy egy Seeker is.

## A harc menete {#how-the-fight-goes}

- **Hagyd békén, amíg a hajód nem bírja el.** A Boss Seeker keményebben üt, mint amit egy pilóta első hajója elbír: az új pilóta pajzs nélküli Protosát másodpercek alatt megsemmisítik, amint a boss és a Slave-jei rákerülnek.
- **Maradj hatótávon kívül.** A boss és a Slave-ek lassabbak egy Protosnál, a fegyvereik pedig kevésbé hatnak el messzire, mint egy Quantum Laser II (lásd [Lézerek és lőszer](/wiki/06-Items/Lasers.md)): aki ilyen lézerekkel repül, és a hatótávjukon kívül marad, nem szenved sebzést, miközben tüzelnek. A Quantum Laser I-es pilóta nem tud hatótávon kívül maradni.
- **A Slave-ek gyorsabban gyógyítanak, mint ahogy egy magányos új pilóta sebez.** Együtt többet gyógyítanak, mint amennyit egy pilóta lézerei okoznak x1 lőszerrel, ezért vigyél társat és x2 lőszert. Két Quantum Laser II-es pilóta, aki tartja a távolságot, nagyjából egy perc alatt leteríti a bosst Alphában, x2 lőszerrel pedig sokkal gyorsabban.
- **A boss visszatér** a *Röviden* lista szerinti idő múlva, teljes erővel, ugyanabban a szektorban, a Slave-ei pedig egymás után érkeznek.

## A vezér három lépése {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

A harcának három lépése van ([hogyan működnek](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); mindegyik egyszer történik meg.

- **Az elején**: A Seeker Slaves 8 mp ideig gyorsabban gyógyítják: a gyógyítás szorzója ×2.
- **Kétharmad alatt**: 2 másolata jelenik meg, és a valódin gyűrű van.
- **Egyharmad alatt**: 4 mp ideig menekül a pilóták elől, aztán visszafordul.

<!-- mob-ladder:end -->

## Jutalmak és zsákmány {#rewards-and-drops}

A Boss Seeker **pontosan tíz Seekert** fizet: egy Seeker kreditjének, Thuliumának, XP-jének és becsületének tízszeresét, a sebzés szerint elosztva a vele harcoló pilóták között ([hogyan fizet egy boss megölése](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). A ládája tíz Seeker zsákmányát tartalmazza, ezen felül pedig az Epikus alatti lőszert és rakétákat, annak a pilótának, aki a legtöbb sebzést okozta. A Slave-ek keveset fizetnek, és nem ejtenek semmit; a kilövésük nem farmolás, mert a bossal együtt visszatérnek.

## A számok {#the-numbers}

A raj hajóinak értékei mindhárom világban ([Világok](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker

Alapja: Seeker, hajótestének, pajzsának és sebzésének 400%-a; a sebessége és a hatótávja a mintahajóé.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | {{guide:vitals.hull@Boss Seeker#1}} | {{guide:vitals.hull@Boss Seeker#2}} | {{guide:vitals.hull@Boss Seeker#3}} |
| Pajzs | {{guide:vitals.shield@Boss Seeker#1}} | {{guide:vitals.shield@Boss Seeker#2}} | {{guide:vitals.shield@Boss Seeker#3}} |
| Lézersebzés (másodpercenként egy sorozat) | {{guide:vitals.dps@Boss Seeker#1}} | {{guide:vitals.dps@Boss Seeker#2}} | {{guide:vitals.dps@Boss Seeker#3}} |
| Sebesség | {{guide:vitals.speed@Boss Seeker#1}} | {{guide:vitals.speed@Boss Seeker#2}} | {{guide:vitals.speed@Boss Seeker#3}} |
| Lézer hatótávja | 600 | 600 | 600 |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Kredit | {{guide:spoils.pay.credits@Boss Seeker#1}} | {{guide:spoils.pay.credits@Boss Seeker#2}} | {{guide:spoils.pay.credits@Boss Seeker#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Seeker#1}} | {{guide:spoils.pay.thulium@Boss Seeker#2}} | {{guide:spoils.pay.thulium@Boss Seeker#3}} |
| Tapasztalat (XP) | {{guide:spoils.pay.experience@Boss Seeker#1}} | {{guide:spoils.pay.experience@Boss Seeker#2}} | {{guide:spoils.pay.experience@Boss Seeker#3}} |
| Becsület | {{guide:spoils.pay.honor@Boss Seeker#1}} | {{guide:spoils.pay.honor@Boss Seeker#2}} | {{guide:spoils.pay.honor@Boss Seeker#3}} |
| PvE-pont kilövésenként | 5 | 5 | 5 |

**Zsákmány**: egy láda, annak a pilótának, aki a legtöbb sebzést okozta.

| Tárgy |
| :--- |
| {{guide:spoils.box@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} |

### Seeker Slave

Alapja: Seeker, hajótestének, pajzsának és sebzésének 100%-a; a sebessége és a hatótávja a mintahajóé.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | {{guide:vitals.hull@Seeker Slave#1}} | {{guide:vitals.hull@Seeker Slave#2}} | {{guide:vitals.hull@Seeker Slave#3}} |
| Pajzs | {{guide:vitals.shield@Seeker Slave#1}} | {{guide:vitals.shield@Seeker Slave#2}} | {{guide:vitals.shield@Seeker Slave#3}} |
| Lézersebzés (másodpercenként egy sorozat) | {{guide:vitals.dps@Seeker Slave#1}} | {{guide:vitals.dps@Seeker Slave#2}} | {{guide:vitals.dps@Seeker Slave#3}} |
| Sebesség | {{guide:vitals.speed@Seeker Slave#1}} | {{guide:vitals.speed@Seeker Slave#2}} | {{guide:vitals.speed@Seeker Slave#3}} |
| Lézer hatótávja | 600 | 600 | 600 |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Gyógyítja a vezért, egyenként, másodpercenként (csak hajótest) | 50 | 75 | 100 |
| Kredit | {{guide:spoils.pay.credits@Seeker Slave#1}} | {{guide:spoils.pay.credits@Seeker Slave#2}} | {{guide:spoils.pay.credits@Seeker Slave#3}} |
| Thulium | {{guide:spoils.pay.thulium@Seeker Slave#1}} | {{guide:spoils.pay.thulium@Seeker Slave#2}} | {{guide:spoils.pay.thulium@Seeker Slave#3}} |
| Tapasztalat (XP) | {{guide:spoils.pay.experience@Seeker Slave#1}} | {{guide:spoils.pay.experience@Seeker Slave#2}} | {{guide:spoils.pay.experience@Seeker Slave#3}} |
| Becsület | {{guide:spoils.pay.honor@Seeker Slave#1}} | {{guide:spoils.pay.honor@Seeker Slave#2}} | {{guide:spoils.pay.honor@Seeker Slave#3}} |
| PvE-pont kilövésenként | 1 | 1 | 1 |

**Zsákmány**: nincs. A kilövés csak a kreditjét, Thuliumát, XP-jét és becsületét fizeti.

<!-- seeker-members:end -->
