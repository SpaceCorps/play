<!-- wiki-i18n source: 38ffa8ba7cbf5000 -->
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
- **Visszatér**: {{guide:vitals.respawn@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} azután, hogy a vezér megsemmisült, ugyanabban a szektorban
- **Értesítés**: A szektor pilótái értesülnek arról, mikor jelenik meg a vezér, és mikor semmisül meg. Ezek rendszersorok: a chat **Rendszer** lapján jelennek meg, olvasatlan sorok számlálójával, és nem a **Globális** vagy a **Helyi** lapon. A kill feed megnevezi a pilótát, akinek a kilövést jóváírják.

<!-- goombah-glance:end -->

## A tagok {#the-members}

- **Boss Goombah**: egy nagyobb Goombah, a raj színezésében és a nevével fölötte, saját hajótesttel, pajzzsal és lézersortűzzel (az értékek lent vannak). Passzív: kóborol, amíg egy pilóta el nem találja, aztán arra a pilótára támad és tüzel, és a raj közeli hajói beszállnak a harcba. A fegyverének hatótávja és a sebessége egy Goombahé, a hajótestét pedig soha nem javítja meg magától. A [három lépése](#the-leaders-three-steps) és egy [különleges képesség](/wiki/03-Mechanics/Special-Abilities.md) változtathat ezen.
- **Goombah Guard**: egy kisebb Goombah a raj színezésében. A Guardok a boss közelében maradnak, beszállnak a harcba, ha egy közeli rajhajót eltalálnak, és mindegyik, amelyik a boss közelében van, gyógyítja a hajótestét. A Guard egy kis pihenő után megjavítja a saját hajótestét, ahogy egy Goombah is.

## A harc menete {#how-the-fight-goes}

- **Vigyél csoportot a legerősebb hajókból.** Három 8. szintű pilóta x2 lőszerrel Alphában nagyjából 75 másodperc alatt megsemmisíti, legfeljebb egy hajót veszítve; közülük kettőnek x4 lőszer kell, az alacsonyabb szintű pilóták pedig nem okoznak elég sebzést a győzelemhez.
- **A bossra lőj, ne a Guardokra.** Egy Guard másodpercek alatt elesik, de a *Röviden* lista szerinti gyakorisággal új érkezik, és amit a Guardok gyógyítanak, az csak kis része annak, amit egy csoport okoz: ha békén hagyod őket, az kis időbe kerül, ha üldözöd őket, többe.
- **A Beta és a Gamma keményebb.** Ezeknek a világoknak a rajai erősebbek ([Világok](/wiki/05-Swarms/Swarms.md#the-worlds)), ezért több pilóta vagy jobb lőszer kell.
- **Figyeld a szektort.** Az `x-4` Alphában PvP-szektor, az `x-3` és az `x-4` pedig Betában és Gammában az ([Világok](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): egy rivális beléphet a harcba, vagy megvárhatja a ládát. Hagyj egy hajót a csoportból őrségben.
- **A boss visszatér** a *Röviden* lista szerinti idő múlva, teljes erővel, ugyanabban a szektorban, a Guardjai pedig egymás után érkeznek.

## A vezér három lépése {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

A harcának három lépése van ([hogyan működnek](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); mindegyik egyszer történik meg.

- **Az elején**: 6 mp ideig minden találatnak csak 50% részét veszi fel.
- **Kétharmad alatt**: 10 mp ideig a sebzésének szorzója ×1,5, a sebességének szorzója ×1,25.
- **Egyharmad alatt**: Meggyógyítja a hajótestének és pajzsának 25% részét (egy sebzéslöket megszakítja), és közben a Goombah Guards gyorsabban gyógyítják: a szorzó ×2.

<!-- mob-ladder:end -->

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
| Hajótest | {{guide:vitals.hull@Boss Goombah#1}} | {{guide:vitals.hull@Boss Goombah#2}} | {{guide:vitals.hull@Boss Goombah#3}} |
| Pajzs | {{guide:vitals.shield@Boss Goombah#1}} | {{guide:vitals.shield@Boss Goombah#2}} | {{guide:vitals.shield@Boss Goombah#3}} |
| Lézersebzés (másodpercenként egy sorozat) | {{guide:vitals.dps@Boss Goombah#1}} | {{guide:vitals.dps@Boss Goombah#2}} | {{guide:vitals.dps@Boss Goombah#3}} |
| Sebesség | {{guide:vitals.speed@Boss Goombah#1}} | {{guide:vitals.speed@Boss Goombah#2}} | {{guide:vitals.speed@Boss Goombah#3}} |
| Lézer hatótávja | 800 | 800 | 800 |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Kredit | {{guide:spoils.pay.credits@Boss Goombah#1}} | {{guide:spoils.pay.credits@Boss Goombah#2}} | {{guide:spoils.pay.credits@Boss Goombah#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Goombah#1}} | {{guide:spoils.pay.thulium@Boss Goombah#2}} | {{guide:spoils.pay.thulium@Boss Goombah#3}} |
| Tapasztalat (XP) | {{guide:spoils.pay.experience@Boss Goombah#1}} | {{guide:spoils.pay.experience@Boss Goombah#2}} | {{guide:spoils.pay.experience@Boss Goombah#3}} |
| Becsület | {{guide:spoils.pay.honor@Boss Goombah#1}} | {{guide:spoils.pay.honor@Boss Goombah#2}} | {{guide:spoils.pay.honor@Boss Goombah#3}} |
| PvE-pont kilövésenként | 14 | 14 | 14 |

**Zsákmány**: egy láda, annak a pilótának, aki a legtöbb sebzést okozta.

| Tárgy |
| :--- |
| {{guide:spoils.box@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} |

### Goombah Guard

Alapja: Goombah, hajótestének, pajzsának és sebzésének 20%-a; a sebessége és a hatótávja a mintahajóé.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | {{guide:vitals.hull@Goombah Guard#1}} | {{guide:vitals.hull@Goombah Guard#2}} | {{guide:vitals.hull@Goombah Guard#3}} |
| Pajzs | {{guide:vitals.shield@Goombah Guard#1}} | {{guide:vitals.shield@Goombah Guard#2}} | {{guide:vitals.shield@Goombah Guard#3}} |
| Lézersebzés (másodpercenként egy sorozat) | {{guide:vitals.dps@Goombah Guard#1}} | {{guide:vitals.dps@Goombah Guard#2}} | {{guide:vitals.dps@Goombah Guard#3}} |
| Sebesség | {{guide:vitals.speed@Goombah Guard#1}} | {{guide:vitals.speed@Goombah Guard#2}} | {{guide:vitals.speed@Goombah Guard#3}} |
| Lézer hatótávja | 800 | 800 | 800 |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Gyógyítja a vezért, egyenként, másodpercenként (csak hajótest) | 110 | 165 | 220 |
| Kredit | {{guide:spoils.pay.credits@Goombah Guard#1}} | {{guide:spoils.pay.credits@Goombah Guard#2}} | {{guide:spoils.pay.credits@Goombah Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Goombah Guard#1}} | {{guide:spoils.pay.thulium@Goombah Guard#2}} | {{guide:spoils.pay.thulium@Goombah Guard#3}} |
| Tapasztalat (XP) | {{guide:spoils.pay.experience@Goombah Guard#1}} | {{guide:spoils.pay.experience@Goombah Guard#2}} | {{guide:spoils.pay.experience@Goombah Guard#3}} |
| Becsület | {{guide:spoils.pay.honor@Goombah Guard#1}} | {{guide:spoils.pay.honor@Goombah Guard#2}} | {{guide:spoils.pay.honor@Goombah Guard#3}} |
| PvE-pont kilövésenként | 3 | 3 | 3 |

**Zsákmány**: nincs. A kilövés csak a kreditjét, Thuliumát, XP-jét és becsületét fizeti.

<!-- goombah-members:end -->
