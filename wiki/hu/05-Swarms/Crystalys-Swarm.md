<!-- wiki-i18n source: 2b3edf7bcb1d9673 -->
<!-- wiki-i18n title: Crystalys-raj -->
# Crystalys-raj {#crystalys-swarm}

A Crystalys-raj egy **Boss Crystalys** és a **Crystalys Guardjai**: a legszívósabb idegen, a [Crystalys](/wiki/04-Aliens/Crystalys.md) megnagyobbítva, őrökkel, amelyek a közelében maradnak, és gyógyítják. A [veszélyes szektorok](/wiki/01-General/Danger-Sectors.md) közül a `DS-1`, `DS-2` és `DS-3` szektorban él, mindegyikben egy, és soha nem hagyja el a szektorát. A veszélyes szektorok PvP-szektorok, ezért a harc a legerősebb pilóták nagy csoportjának való, és a boss nem az egyetlen veszély ott.

## Röviden {#at-a-glance}

<!-- crystalys-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Hol**: A veszélyes szektorok: `DS-1`, `DS-2`, `DS-3`
- **Hány**: Egy-egy az ilyen szektorokban, világonként 3
- **Megjelenik**: A szezon 4. napjától a wipe-ig (Betában és Gammában: a szezon 1. napjától)
- **Vezér**: Boss Crystalys
- **Kísérők**: Legfeljebb 3 × Crystalys Guard, mindig 10 mp múlva egy újabb
- **A kísérők közel maradnak**: legfeljebb 500 egységre a vezértől
- **Gyógyítás**: Minden Crystalys Guard, amely a vezértől 600 egységen belül van, gyógyítja a hajótestét, Alphában másodpercenként 250 HP-t
- **A vezér megsemmisül**: A kísérők a vezér megsemmisülése után 30 mp múlva eltűnnek, kivéve ha éppen támadnak
- **Visszatér**: {{guide:vitals.respawn@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} azután, hogy a vezér megsemmisült, ugyanabban a szektorban
- **Értesítés**: A szektor pilótái értesülnek arról, mikor jelenik meg a vezér, és mikor semmisül meg. Ezek rendszersorok: a chat **Rendszer** lapján jelennek meg, olvasatlan sorok számlálójával, és nem a **Globális** vagy a **Helyi** lapon. A kill feed megnevezi a pilótát, akinek a kilövést jóváírják.

<!-- crystalys-glance:end -->

## A tagok {#the-members}

- **Boss Crystalys**: egy nagyobb Crystalys, a raj színezésében és a nevével fölötte, saját hajótesttel, pajzzsal és lézersortűzzel (az értékek lent vannak). Passzív: kóborol, amíg egy pilóta el nem találja, aztán arra a pilótára támad és tüzel, és a raj közeli hajói beszállnak a harcba. A fegyverének hatótávja és a sebessége egy Crystalysé, a hajótestét pedig soha nem javítja meg magától. A [három lépése](#the-leaders-three-steps) és egy [különleges képesség](/wiki/03-Mechanics/Special-Abilities.md) változtathat ezen.
- **Crystalys Guard**: egy kisebb Crystalys a raj színezésében. A Guardok a boss közelében maradnak, beszállnak a harcba, ha egy közeli rajhajót eltalálnak, és mindegyik, amelyik a boss közelében van, gyógyítja a hajótestét. A Guard egy kis pihenő után megjavítja a saját hajótestét, ahogy egy Crystalys is.

## A harc menete {#how-the-fight-goes}

- **Vigyél nagy csoportot.** Alphában hat 8. szintű pilóta Paragonokban x2 lőszerrel elég, ha a tüze megoszlik köztük, kilenc, ha mind egyetlen pilótára megy; x4 lőszerrel öt, illetve hat. Minél többen vannak, annál hamarabb ér véget a harc és annál kevesebb hajó vész el, egy pilótát egyedül megsemmisítenek.
- **A bossra lőj, ne a Guardokra.** Egy Guard másodpercek alatt elesik, de a *Röviden* lista szerinti gyakorisággal új érkezik, és amit a Guardok gyógyítanak, az csak kis része annak, amit egy csoport okoz: ha békén hagyod őket, az kis időbe kerül, ha üldözöd őket, többe.
- **A Beta és a Gamma keményebb.** Ezeknek a világoknak a rajai erősebbek ([Világok](/wiki/05-Swarms/Swarms.md#the-worlds)), ezért több pilóta vagy jobb lőszer kell.
- **A veszélyes szektorok PvP-szektorok.** Egy rivális a harc közepén megtámadhatja a csoportot, és megvárhatja a ládát: az 30 másodpercig a legtöbb sebzést okozó pilótáé (és a klánjáé), utána bárkié ([Rakomány](/wiki/03-Mechanics/Cargo.md)). Ne egyedül menj.
- **A boss visszatér** a *Röviden* lista szerinti idő múlva, teljes erővel, ugyanabban a szektorban, a Guardjai pedig egymás után érkeznek.

## A vezér három lépése {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

A harcának három lépése van ([hogyan működnek](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); mindegyik egyszer történik meg.

- **Az elején**: 8 mp ideig minden találatnak csak 50% részét veszi fel.
- **Kétharmad alatt**: Egy 700 egység sugarú gyűrű minden benne lévő hajót eltalál a sortüzének 4 adagjával, és 4 rakétát lő.
- **Egyharmad alatt**: Meggyógyítja a hajótestének és pajzsának 20% részét (egy sebzéslöket megszakítja), és 3 újabb hajó jön: Crystalys Guards; legfeljebb 6 él egyszerre.

<!-- mob-ladder:end -->

## Jutalmak és zsákmány {#rewards-and-drops}

A Boss Crystalys annyit fizet, amennyi a harc, amit jelent: egy perc harc vele többet fizet, mint egy perc harc egy Crystalys ellen, a legjobban fizető idegen ellen. A fizetést a sebzés szerint osztják el a vele harcoló pilóták között ([hogyan fizet egy boss megölése](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). A ládája annak a pilótának jár, aki a legtöbb sebzést okozta, és Cataclysite-ot és Quorviumot tartalmaz, időnként egy Power Core-t, egy Ancient Control Unitot vagy Dark Mattert, x3 és x4 lőszert és Epikus rakétákat. A Guardok keveset fizetnek, és nem ejtenek semmit; a kilövésük nem farmolás, mert a bossal együtt visszatérnek.

## A számok {#the-numbers}

A raj hajóinak értékei mindhárom világban ([Világok](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- crystalys-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Crystalys

Alapja: Crystalys, hajótestének 350%-a és lézersebzésének 100%-a; a sebessége és a hatótávja a mintahajóé.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | {{guide:vitals.hull@Boss Crystalys#1}} | {{guide:vitals.hull@Boss Crystalys#2}} | {{guide:vitals.hull@Boss Crystalys#3}} |
| Pajzs | {{guide:vitals.shield@Boss Crystalys#1}} | {{guide:vitals.shield@Boss Crystalys#2}} | {{guide:vitals.shield@Boss Crystalys#3}} |
| Lézersebzés (másodpercenként egy sorozat) | {{guide:vitals.dps@Boss Crystalys#1}} | {{guide:vitals.dps@Boss Crystalys#2}} | {{guide:vitals.dps@Boss Crystalys#3}} |
| Sebesség | {{guide:vitals.speed@Boss Crystalys#1}} | {{guide:vitals.speed@Boss Crystalys#2}} | {{guide:vitals.speed@Boss Crystalys#3}} |
| Lézer hatótávja | 900 | 900 | 900 |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Kredit | {{guide:spoils.pay.credits@Boss Crystalys#1}} | {{guide:spoils.pay.credits@Boss Crystalys#2}} | {{guide:spoils.pay.credits@Boss Crystalys#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Crystalys#1}} | {{guide:spoils.pay.thulium@Boss Crystalys#2}} | {{guide:spoils.pay.thulium@Boss Crystalys#3}} |
| Tapasztalat (XP) | {{guide:spoils.pay.experience@Boss Crystalys#1}} | {{guide:spoils.pay.experience@Boss Crystalys#2}} | {{guide:spoils.pay.experience@Boss Crystalys#3}} |
| Becsület | {{guide:spoils.pay.honor@Boss Crystalys#1}} | {{guide:spoils.pay.honor@Boss Crystalys#2}} | {{guide:spoils.pay.honor@Boss Crystalys#3}} |
| PvE-pont kilövésenként | 30 | 30 | 30 |

**Zsákmány**: egy láda, annak a pilótának, aki a legtöbb sebzést okozta.

| Tárgy |
| :--- |
| {{guide:spoils.box@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} |

### Crystalys Guard

Alapja: Crystalys, hajótestének, pajzsának és sebzésének 15%-a; a sebessége és a hatótávja a mintahajóé.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | {{guide:vitals.hull@Crystalys Guard#1}} | {{guide:vitals.hull@Crystalys Guard#2}} | {{guide:vitals.hull@Crystalys Guard#3}} |
| Pajzs | {{guide:vitals.shield@Crystalys Guard#1}} | {{guide:vitals.shield@Crystalys Guard#2}} | {{guide:vitals.shield@Crystalys Guard#3}} |
| Lézersebzés (másodpercenként egy sorozat) | {{guide:vitals.dps@Crystalys Guard#1}} | {{guide:vitals.dps@Crystalys Guard#2}} | {{guide:vitals.dps@Crystalys Guard#3}} |
| Sebesség | {{guide:vitals.speed@Crystalys Guard#1}} | {{guide:vitals.speed@Crystalys Guard#2}} | {{guide:vitals.speed@Crystalys Guard#3}} |
| Lézer hatótávja | 900 | 900 | 900 |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Gyógyítja a vezért, egyenként, másodpercenként (csak hajótest) | 250 | 375 | 500 |
| Kredit | {{guide:spoils.pay.credits@Crystalys Guard#1}} | {{guide:spoils.pay.credits@Crystalys Guard#2}} | {{guide:spoils.pay.credits@Crystalys Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Crystalys Guard#1}} | {{guide:spoils.pay.thulium@Crystalys Guard#2}} | {{guide:spoils.pay.thulium@Crystalys Guard#3}} |
| Tapasztalat (XP) | {{guide:spoils.pay.experience@Crystalys Guard#1}} | {{guide:spoils.pay.experience@Crystalys Guard#2}} | {{guide:spoils.pay.experience@Crystalys Guard#3}} |
| Becsület | {{guide:spoils.pay.honor@Crystalys Guard#1}} | {{guide:spoils.pay.honor@Crystalys Guard#2}} | {{guide:spoils.pay.honor@Crystalys Guard#3}} |
| PvE-pont kilövésenként | 6 | 6 | 6 |

**Zsákmány**: nincs. A kilövés csak a kreditjét, Thuliumát, XP-jét és becsületét fizeti.

<!-- crystalys-members:end -->
