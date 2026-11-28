<!-- wiki-i18n source: 33448f95d2520b3a -->
<!-- wiki-i18n title: Pirate-raj -->
# Pirate-raj {#pirate-swarm}

A Pirate-raj egy **Pirate Boss** a **Pirate Scoutjaival**: egy hatalmas, lassú hajó, amely senkit sem támad meg, és rakétákkal válaszol, meg egy gyorsabb hajókból álló csapat, amely őrzi és gyógyítja. Egy vállalat bázisa és határa közötti szektorokban él, ahol a játék középső szintjeit játsszák, és hosszú harc egy pilótacsoportnak, nem gyors kilövés.

## Röviden {#at-a-glance}

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Hol**: Minden vállalat `x-2` és `x-3` szektora
- **Hány**: Egy-egy az ilyen szektorokban, világonként 6
- **Megjelenik**: A szezon 4. napjától a wipe-ig (Betában és Gammában: a szezon 1. napjától)
- **Vezér**: Pirate Boss
- **Kísérők**: Legfeljebb 5 × Pirate Scout, mindig 10 mp múlva egy újabb
- **A kísérők közel maradnak**: legfeljebb 900 egységre a vezértől
- **Gyógyítás**: Minden Pirate Scout, amely a vezértől 600 egységen belül van, gyógyítja a hajótestét, Alphában másodpercenként 40 HP-t
- **A vezér megsemmisül**: A kísérők a vezér megsemmisülése után 1 perc múlva eltűnnek, kivéve ha éppen támadnak
- **Visszatér**: {{guide:vitals.respawn@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} azután, hogy a vezér megsemmisült, ugyanabban a szektorban
- **Értesítés**: A szektor pilótái értesülnek arról, mikor jelenik meg a vezér, és mikor semmisül meg. Ezek rendszersorok: a chat **Rendszer** lapján jelennek meg, olvasatlan sorok számlálójával, és nem a **Globális** vagy a **Helyi** lapon. A kill feed megnevezi a pilótát, akinek a kilövést jóváírják.

<!-- pirate-glance:end -->

## A tagok {#the-members}

- **Pirate Boss**: az Ironcladre épülő hajó, annak erejének egy részével (az értékek lent vannak). Passzív, és **nem lő lézerekkel**: az egyetlen fegyvere egy **egyenes rakéta** ([Rakéták](/wiki/06-Items/Rockets.md); hogy melyik, az a szektortól függ, lásd a táblázatot) arra a pilótára, aki megtámadta, és lövés közben tovább kóborol. A hajótestét soha nem javítja meg magától. A [három lépése](#the-leaders-three-steps) és egy [különleges képesség](/wiki/03-Mechanics/Special-Abilities.md) változtathat ezen.
- **Pirate Scout**: a Kitefinre épülő hajó, annak erejének egy részével. A Scoutok megtámadnak minden pilótát, aki a közelükbe ér, a boss közelében maradnak, és mindegyik, amelyik a boss közelében van, gyógyítja a hajótestét.

## A harc menete {#how-the-fight-goes}

- **A bosst lődd, ne a Scoutokat.** A Scoutok gyógyítják a bosst, de a gyógyítás kicsi a boss hajótestéhez képest, és új Scout olyan gyakran érkezik, ahogy a *Röviden* lista mondja: az a csoport, amelyik előbb a Scoutokat lövi, sosem kerül előnybe velük szemben, és csak egy nagyon nagy csoport tudja kitakarítani őket, mégis tovább tart neki a boss befejezése, mint annak, amelyik békén hagyta őket. A Scoutok időt vesznek el tőled, a harcot nem ők döntik el.
- **Vezesd el a Scoutokat.** A Scout csak addig gyógyít, amíg a boss hatótávján belül van, így az a Scout, amelyik a hatótávon kívülre követ téged, semmit sem gyógyít, és az Ostirion gyorsabb a Scoutnál.
- **Mozogj folyamatosan.** A boss rakétája egyenes és nem önirányító: a folyamatosan mozgó hajó kitér előle, az álló hajót eltalálja.
- **Hozz csoportot.** Három Ostirion-pilóta x2 lőszerrel az `x-2` szektoron egyetlen hajó elvesztése nélkül leteríti, bár csak éppen hogy, az `x-3` szektoron viszont elpusztul, még amíg a találatok szétoszlanak; négyen nagyjából három perc alatt leterítik Alphában. x4 lőszerrel az `x-3` szektoron három pilóta nagyjából két perc alatt leteríti. Öten nagyjából két és fél perc alatt leterítik, ha a találatok szétoszlanak, és nagyjából három perc alatt, ha egy pilóta kapja az összes tüzet, de akkor két hajót elveszítenek: az a csoport, amelynél egy pilóta kapja az összes tüzet, öt főt kíván. Betában öt, Gammában hét pilóta kell, szétoszló találatokkal (ott nagyobb a boss, és a Scoutjai többet gyógyítanak). Alphában az `x-3` szektoron x2 lőszerrel egy Ostirion egyedül nem tudja leteríteni, egy Paragon egyedül sem teríti le, két Paragon pedig biztonságosan leteríti. Betában és Gammában az `x-3` szektoron egy Paragon egyedül x2 és x4 lőszerrel is elpusztul. A boss az első pilótának válaszol, aki eltalálta, ezért a legellenállóbb hajó kezdje, és használd a képességeidet (Emergency Repair, Shield Surge: [Képességek](/wiki/03-Mechanics/Abilities.md)) egy ilyen hosszú harcban. A még 2. vagy 3. szintű pilóták túl gyengék hozzá, még ott is, ahol repülnek: maradj távol, amíg erősebb nem leszel.
- **A boss visszatér** a *Röviden* lista szerinti idő múlva, ugyanabban a szektorban.

## A vezér három lépése {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

A harcának három lépése van ([hogyan működnek](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); mindegyik egyszer történik meg.

- **Az elején**: 3 rakétából álló legyezőt lő, 12 fokos közökkel, az első pilótára, aki eltalálta.
- **Kétharmad alatt**: Egyszerre 5 újabb hajót hív: Pirate Scouts; legfeljebb 10 él egyszerre. Nem fizetnek, és 45 mp múlva távoznak.
- **Egyharmad alatt**: 10 mp ideig a legközelebbi kapu felé repül, a sebességének szorzója ×1,8, aztán a pilóták ellen fordul.

<!-- mob-ladder:end -->

## Jutalmak és zsákmány {#rewards-and-drops}

A Pirate Boss a harc értékéhez mérten fizet: egy perc harc vele többet fizet, mint egy perc harc egy Goombah ellen. A fizetést a sebzés szerint osztják el a vele harcoló pilóták között ([hogyan fizet egy boss megölése](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). A ládája annak a pilótának jár, aki a legtöbb sebzést okozta, és tartalmazhat **Reinforced Hull Plate**-et, rakétákat és lőszert. A ládája valamivel kevesebb mint a felét éri annak, amit maga a megölés fizet. A Scoutok keveset fizetnek, és nem ejtenek semmit.

## A számok {#the-numbers}

A raj hajóinak értékei mindhárom világban ([Világok](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss

Alapja: Ironclad, hajótestének, pajzsának és sebzésének 50%-a; a sebessége és a hatótávja a mintahajóé. 5 mp alatt egy egyenes rakétát lő ki: [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets): `x-2`, [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets): `x-3`.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | {{guide:vitals.hull@Pirate Boss#1}} | {{guide:vitals.hull@Pirate Boss#2}} | {{guide:vitals.hull@Pirate Boss#3}} |
| Pajzs | {{guide:vitals.shield@Pirate Boss#1}} | {{guide:vitals.shield@Pirate Boss#2}} | {{guide:vitals.shield@Pirate Boss#3}} |
| Lézersebzés (másodpercenként egy sorozat) | nincs | nincs | nincs |
| Sebesség | {{guide:vitals.speed@Pirate Boss#1}} | {{guide:vitals.speed@Pirate Boss#2}} | {{guide:vitals.speed@Pirate Boss#3}} |
| Lézer hatótávja | – | – | – |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Rakétasebzés, legfeljebb | {{guide:behaviour.ability:rocket.damage@Pirate Boss#1}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#2}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#3}} |
| Kredit | {{guide:spoils.pay.credits@Pirate Boss#1}} | {{guide:spoils.pay.credits@Pirate Boss#2}} | {{guide:spoils.pay.credits@Pirate Boss#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Boss#1}} | {{guide:spoils.pay.thulium@Pirate Boss#2}} | {{guide:spoils.pay.thulium@Pirate Boss#3}} |
| Tapasztalat (XP) | {{guide:spoils.pay.experience@Pirate Boss#1}} | {{guide:spoils.pay.experience@Pirate Boss#2}} | {{guide:spoils.pay.experience@Pirate Boss#3}} |
| Becsület | {{guide:spoils.pay.honor@Pirate Boss#1}} | {{guide:spoils.pay.honor@Pirate Boss#2}} | {{guide:spoils.pay.honor@Pirate Boss#3}} |
| PvE-pont kilövésenként | 15 | 15 | 15 |

**Zsákmány**: egy láda, annak a pilótának, aki a legtöbb sebzést okozta.

| Tárgy |
| :--- |
| {{guide:spoils.box@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} |

### Pirate Scout

Alapja: Kitefin, hajótestének 50%-a és lézersebzésének 113%-a; a sebessége és a hatótávja a mintahajóé.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | {{guide:vitals.hull@Pirate Scout#1}} | {{guide:vitals.hull@Pirate Scout#2}} | {{guide:vitals.hull@Pirate Scout#3}} |
| Pajzs | {{guide:vitals.shield@Pirate Scout#1}} | {{guide:vitals.shield@Pirate Scout#2}} | {{guide:vitals.shield@Pirate Scout#3}} |
| Lézersebzés (másodpercenként egy sorozat) | {{guide:vitals.dps@Pirate Scout#1}} | {{guide:vitals.dps@Pirate Scout#2}} | {{guide:vitals.dps@Pirate Scout#3}} |
| Sebesség | {{guide:vitals.speed@Pirate Scout#1}} | {{guide:vitals.speed@Pirate Scout#2}} | {{guide:vitals.speed@Pirate Scout#3}} |
| Lézer hatótávja | 700 | 700 | 700 |
| Aggrósugár | {{guide:vitals.aggro@Pirate Scout#1}} | {{guide:vitals.aggro@Pirate Scout#2}} | {{guide:vitals.aggro@Pirate Scout#3}} |
| Gyógyítja a vezért, egyenként, másodpercenként (csak hajótest) | 40 | 60 | 80 |
| Kredit | {{guide:spoils.pay.credits@Pirate Scout#1}} | {{guide:spoils.pay.credits@Pirate Scout#2}} | {{guide:spoils.pay.credits@Pirate Scout#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Scout#1}} | {{guide:spoils.pay.thulium@Pirate Scout#2}} | {{guide:spoils.pay.thulium@Pirate Scout#3}} |
| Tapasztalat (XP) | {{guide:spoils.pay.experience@Pirate Scout#1}} | {{guide:spoils.pay.experience@Pirate Scout#2}} | {{guide:spoils.pay.experience@Pirate Scout#3}} |
| Becsület | {{guide:spoils.pay.honor@Pirate Scout#1}} | {{guide:spoils.pay.honor@Pirate Scout#2}} | {{guide:spoils.pay.honor@Pirate Scout#3}} |
| PvE-pont kilövésenként | 4 | 4 | 4 |

**Zsákmány**: nincs. A kilövés csak a kreditjét, Thuliumát, XP-jét és becsületét fizeti.

<!-- pirate-members:end -->
