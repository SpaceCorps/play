<!-- wiki-i18n source: 2eff9c368449da99 -->
<!-- wiki-i18n title: Phantasm-raj -->
# Phantasm-raj {#phantasm-swarm}

A Phantasm-raj egy **Boss Phantasm** és a **Phantasm Guardjai**: egy hatalmas [Phantasm](/wiki/04-Aliens/Phantasm.md), amely soha nem kezd harcot, és kisebbek, amelyek a közelében maradnak, és gyógyítják. A vállalatok külső szektoraiban él, az `x-3` és az `x-4` szektorban, és közepes szintű pilóták csoportjának való harc.

## Röviden {#at-a-glance}

<!-- phantasm-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Hol**: Minden vállalat `x-3` és `x-4` szektora
- **Hány**: Egy-egy az ilyen szektorokban, világonként 6
- **Megjelenik**: A szezon 4. napjától a wipe-ig (Betában és Gammában: a szezon 1. napjától)
- **Vezér**: Boss Phantasm
- **Kísérők**: Legfeljebb 4 × Phantasm Guard, mindig 10 mp múlva egy újabb
- **A kísérők közel maradnak**: legfeljebb 500 egységre a vezértől
- **Gyógyítás**: Minden Phantasm Guard, amely a vezértől 600 egységen belül van, gyógyítja a hajótestét, Alphában másodpercenként 30 HP-t
- **A vezér megsemmisül**: A kísérők a vezér megsemmisülése után 30 mp múlva eltűnnek, kivéve ha éppen támadnak
- **Visszatér**: {{guide:vitals.respawn@Boss Phantasm#1;Boss Phantasm#2;Boss Phantasm#3}} azután, hogy a vezér megsemmisült, ugyanabban a szektorban
- **Értesítés**: A szektor pilótái értesülnek arról, mikor jelenik meg a vezér, és mikor semmisül meg. Ezek rendszersorok: a chat **Rendszer** lapján jelennek meg, olvasatlan sorok számlálójával, és nem a **Globális** vagy a **Helyi** lapon. A kill feed megnevezi a pilótát, akinek a kilövést jóváírják.

<!-- phantasm-glance:end -->

## A tagok {#the-members}

- **Boss Phantasm**: egy nagyobb Phantasm, a raj színezésében és a nevével fölötte, saját hajótesttel, pajzzsal és lézersortűzzel (az értékek lent vannak). Passzív: kóborol, amíg egy pilóta el nem találja, aztán arra a pilótára támad és tüzel, és a raj közeli hajói beszállnak a harcba. A fegyverének hatótávja és a sebessége egy Phantasmé, a hajótestét pedig soha nem javítja meg magától. A [három lépése](#the-leaders-three-steps) és egy [különleges képesség](/wiki/03-Mechanics/Special-Abilities.md) változtathat ezen.
- **Phantasm Guard**: egy kisebb Phantasm a raj színezésében. A Guardok a boss közelében maradnak, beszállnak a harcba, ha egy közeli rajhajót eltalálnak, és mindegyik, amelyik a boss közelében van, gyógyítja a hajótestét. A Guard egy kis pihenő után megjavítja a saját hajótestét, ahogy egy Phantasm is.

## A harc menete {#how-the-fight-goes}

- **Vigyél csoportot.** Három 4–5. szintű pilóta x2 lőszerrel Alphában körülbelül másfél perc alatt megsemmisíti, legfeljebb egy hajót veszítve; egy ilyen szintű pilótát egyedül megsemmisítenek, kettő pedig csak éppen hogy nyer, és csak akkor, ha a találatok szétoszlanak. Jobb hajók és x4 lőszer sokkal gyorsabbá teszik.
- **A bossra lőj, ne a Guardokra.** Egy Guard másodpercek alatt elesik, de a *Röviden* lista szerinti gyakorisággal új érkezik, és amit a Guardok gyógyítanak, az csak kis része annak, amit egy csoport okoz: ha békén hagyod őket, az kis időbe kerül, ha üldözöd őket, többe.
- **A Beta és a Gamma keményebb.** Ezeknek a világoknak a rajai erősebbek ([Világok](/wiki/05-Swarms/Swarms.md#the-worlds)), ezért több pilóta vagy jobb lőszer kell.
- **Figyeld a szektort.** Az `x-4` Alphában PvP-szektor, az `x-3` és az `x-4` pedig Betában és Gammában az ([Világok](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): egy rivális beléphet a harcba, vagy megvárhatja a ládát. Hagyj egy hajót a csoportból őrségben.
- **A boss visszatér** a *Röviden* lista szerinti idő múlva, teljes erővel, ugyanabban a szektorban, a Guardjai pedig egymás után érkeznek.

## A vezér három lépése {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

A harcának három lépése van ([hogyan működnek](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); mindegyik egyszer történik meg.

- **Az elején**: A Phantasm Guards mindegyike a saját hajótestének 10% részét kitevő pajzsréteget emel.
- **Kétharmad alatt**: 3 másolata jelenik meg, és a valódin gyűrű van.
- **Egyharmad alatt**: Körülbelül 2 500 egységre ugrik a pilótáktól, és a Phantasm Guards sértetlenül térnek vissza körülötte.

<!-- mob-ladder:end -->

## Jutalmak és zsákmány {#rewards-and-drops}

A Boss Phantasm annyit fizet, amennyi a harc, amit jelent: egy perc harc vele többet fizet, mint egy perc harc egy Goombah ellen, ezeknek a szektoroknak a legjobban fizető idegenje ellen. A fizetést a sebzés szerint osztják el a vele harcoló pilóták között ([hogyan fizet egy boss megölése](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). A ládája annak a pilótának jár, aki a legtöbb sebzést okozta, és egy Phantasm saját zsákmányát tartalmazza sokszorosan (Ship Fragment, Daraxium és Nyxite), lőszerrel és rakétákkal. A Guardok keveset fizetnek, és nem ejtenek semmit; a kilövésük nem farmolás, mert a bossal együtt visszatérnek.

## A számok {#the-numbers}

A raj hajóinak értékei mindhárom világban ([Világok](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- phantasm-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Phantasm

Alapja: Phantasm, hajótestének 2 000%-a és lézersebzésének 300%-a; a sebessége és a hatótávja a mintahajóé.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | {{guide:vitals.hull@Boss Phantasm#1}} | {{guide:vitals.hull@Boss Phantasm#2}} | {{guide:vitals.hull@Boss Phantasm#3}} |
| Pajzs | {{guide:vitals.shield@Boss Phantasm#1}} | {{guide:vitals.shield@Boss Phantasm#2}} | {{guide:vitals.shield@Boss Phantasm#3}} |
| Lézersebzés (másodpercenként egy sorozat) | {{guide:vitals.dps@Boss Phantasm#1}} | {{guide:vitals.dps@Boss Phantasm#2}} | {{guide:vitals.dps@Boss Phantasm#3}} |
| Sebesség | {{guide:vitals.speed@Boss Phantasm#1}} | {{guide:vitals.speed@Boss Phantasm#2}} | {{guide:vitals.speed@Boss Phantasm#3}} |
| Lézer hatótávja | 700 | 700 | 700 |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Kredit | {{guide:spoils.pay.credits@Boss Phantasm#1}} | {{guide:spoils.pay.credits@Boss Phantasm#2}} | {{guide:spoils.pay.credits@Boss Phantasm#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Phantasm#1}} | {{guide:spoils.pay.thulium@Boss Phantasm#2}} | {{guide:spoils.pay.thulium@Boss Phantasm#3}} |
| Tapasztalat (XP) | {{guide:spoils.pay.experience@Boss Phantasm#1}} | {{guide:spoils.pay.experience@Boss Phantasm#2}} | {{guide:spoils.pay.experience@Boss Phantasm#3}} |
| Becsület | {{guide:spoils.pay.honor@Boss Phantasm#1}} | {{guide:spoils.pay.honor@Boss Phantasm#2}} | {{guide:spoils.pay.honor@Boss Phantasm#3}} |
| PvE-pont kilövésenként | 8 | 8 | 8 |

**Zsákmány**: egy láda, annak a pilótának, aki a legtöbb sebzést okozta.

| Tárgy |
| :--- |
| {{guide:spoils.box@Boss Phantasm#1;Boss Phantasm#2;Boss Phantasm#3}} |

### Phantasm Guard

Alapja: Phantasm, hajótestének, pajzsának és sebzésének 50%-a; a sebessége és a hatótávja a mintahajóé.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | {{guide:vitals.hull@Phantasm Guard#1}} | {{guide:vitals.hull@Phantasm Guard#2}} | {{guide:vitals.hull@Phantasm Guard#3}} |
| Pajzs | {{guide:vitals.shield@Phantasm Guard#1}} | {{guide:vitals.shield@Phantasm Guard#2}} | {{guide:vitals.shield@Phantasm Guard#3}} |
| Lézersebzés (másodpercenként egy sorozat) | {{guide:vitals.dps@Phantasm Guard#1}} | {{guide:vitals.dps@Phantasm Guard#2}} | {{guide:vitals.dps@Phantasm Guard#3}} |
| Sebesség | {{guide:vitals.speed@Phantasm Guard#1}} | {{guide:vitals.speed@Phantasm Guard#2}} | {{guide:vitals.speed@Phantasm Guard#3}} |
| Lézer hatótávja | 700 | 700 | 700 |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Gyógyítja a vezért, egyenként, másodpercenként (csak hajótest) | 30 | 45 | 60 |
| Kredit | {{guide:spoils.pay.credits@Phantasm Guard#1}} | {{guide:spoils.pay.credits@Phantasm Guard#2}} | {{guide:spoils.pay.credits@Phantasm Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Phantasm Guard#1}} | {{guide:spoils.pay.thulium@Phantasm Guard#2}} | {{guide:spoils.pay.thulium@Phantasm Guard#3}} |
| Tapasztalat (XP) | {{guide:spoils.pay.experience@Phantasm Guard#1}} | {{guide:spoils.pay.experience@Phantasm Guard#2}} | {{guide:spoils.pay.experience@Phantasm Guard#3}} |
| Becsület | {{guide:spoils.pay.honor@Phantasm Guard#1}} | {{guide:spoils.pay.honor@Phantasm Guard#2}} | {{guide:spoils.pay.honor@Phantasm Guard#3}} |
| PvE-pont kilövésenként | 1 | 1 | 1 |

**Zsákmány**: nincs. A kilövés csak a kreditjét, Thuliumát, XP-jét és becsületét fizeti.

<!-- phantasm-members:end -->
