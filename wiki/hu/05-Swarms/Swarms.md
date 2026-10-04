<!-- wiki-i18n source: bbd76eb145ce6188 -->
<!-- wiki-i18n title: Rajok -->
# Rajok {#swarms}

A **raj** idegenek csoportja, amely egy **vezér** alatt járja a galaxis egy részét: a vezér egy boss, sokkal erősebb bármelyik környező idegennél, és **kísérői** őrzik, két rajban pedig gyógyítják is. Három van, mindegyiknek saját cikke:

- [Seeker-raj](/wiki/05-Swarms/Seeker-Swarm.md): a Boss Seeker és a Seeker Slave-jei, a legkisebb raj, azokban a szektorokban, ahol az új pilóták repülnek.
- [Pirate-raj](/wiki/05-Swarms/Pirate-Swarm.md): a Pirate Boss és a Pirate Scoutjai, hosszú harc egy csoportnak.
- [Dormant-raj](/wiki/05-Swarms/Dormant-Swarm.md): a Dormant Force és a Dormant Pulse-jai, a legerősebb raj, a leggazdagabb zsákmánnyal.

A hajóik **saját fajú idegenek**: saját nevük és saját kilövésszámlálójuk van, és egyik sem számít Seekernek, Phantasmnak vagy más idegennek. A rajhajó alakja a hajóé, amelyre épül, saját színezéssel és fölötte a nevével; a Boss Seeker egy sokkal nagyobb Seeker.

## A három raj {#the-three-swarms}

<!-- swarms-list:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Raj | Hol | Hány | Vezér | Kísérők | Visszatér |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**Pirate-raj**](/wiki/05-Swarms/Pirate-Swarm.md) | Minden vállalat `x-2` és `x-3` szektora | Egy-egy az ilyen szektorokban, világonként 6 | **Pirate Boss** | Legfeljebb 5 × Pirate Scout, mindig 10 mp múlva egy újabb | 2 perc azután, hogy a vezér megsemmisült, ugyanabban a szektorban |
| [**Dormant-raj**](/wiki/05-Swarms/Dormant-Swarm.md) | A veszélyes szektorok: `DS-1`, `DS-2`, `DS-3`, `DS-4`; az egyikből a másikba repül | Világonként egy | **Dormant Force** | 2 × Dormant Pulse, a vezérrel együtt repülnek | 1 óra azután, hogy az egész raj megsemmisült, egy véletlenszerű veszélyes szektorban |
| [**Seeker-raj**](/wiki/05-Swarms/Seeker-Swarm.md) | Minden vállalat `x-1` és `x-2` szektora | Egy-egy az ilyen szektorokban, világonként 6 | **Boss Seeker** | Legfeljebb 4 × Seeker Slave, mindig 10 mp múlva egy újabb | 2 perc azután, hogy a vezér megsemmisült, ugyanabban a szektorban |

<!-- swarms-list:end -->

## Mikor és hol {#when-and-where}

A rajok az **Első kapcsolattal** kezdenek megjelenni, és a wipe-ig maradnak (lásd a [Wipe-idővonalat](/wiki/03-Mechanics/Wipe-Timeline.md); a napot az alábbi szabályok első sora adja meg). **Minden világnak megvannak a saját rajai** ugyanazokon a helyeken, így az Alpha Pirate Bossa és a Beta Pirate Bossa két különböző hajó, és az a raj, amelyet a saját világodban megsemmisítesz, egy másikban nem semmisül meg. A megsemmisített raj a fenti táblázatban szereplő idő múlva tér vissza.

## Minden raj szabályai {#the-rules-of-every-swarm}

<!-- swarms-rules:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- A rajok a szezon 4. napjától a wipe-ig jelennek meg.
- Ha egy rajhajót eltalálnak, a rajának 1 500 egységen belüli hajói beszállnak a harcba az első pilóta ellen, aki eltalálta.
- A vezér legalább 2 500 egység távolságra jelenik meg minden állomás- és kapugyűrű szélétől.
- Az a pilóta, aki egy bossnak okozott sebzés legalább 5% részét leadta, fizetést kap a kilövéséért.

<!-- swarms-rules:end -->

## A világok {#the-worlds}

A világ úgy skálázza a rajt, ahogy minden idegent ([Világok](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): a rajhajók hajóteste, pajzsa, pajzstöltődése, lézersebzése, rakétasebzése és gyógyítása az Alpha értékeinek és az alábbi erősségnek a szorzata, a kilövés pedig az alábbi fizetést adja. A sebesség, a hatótáv és a zsákmány minden világban ugyanaz. A cikkek minden hajó értékeit megadják mindhárom világban.

<!-- swarms-world:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Világ | Erősség | Fizetés |
| :--- | ---: | ---: |
| **Alpha** | ×1 | ×1 |
| **Beta** | ×1,5 | ×2 |
| **Gamma** | ×2 | ×3 |

<!-- swarms-world:end -->

## Mit tudnak meg a pilóták {#what-the-pilots-are-told}

A Seeker- és a Pirate-raj értesíti a saját szektorának pilótáit, amikor egy boss megjelenik, és amikor megsemmisül. A Dormant-raj az egész világát értesíti, és a veszélyes szektorok térképén és a galaxistérképen jelölve van, hogy a pilóták megtalálhassák. Ezek rendszersorok: a chat **Rendszer** lapján jelennek meg, olvasatlan sorok számlálójával, és nem a **Globális** vagy a **Helyi** lapon. A boss kilövése a kill feedben is kap egy sort, amely megnevezi a pilótát, akinek jóváírják. Az egyes cikkek *Röviden* listája megmondja, kit értesítenek.

## Harc egy rajjal {#fighting-a-swarm}

- **A vezérek soha nem kezdenek harcot.** A vezér kóborol, amíg egy pilóta el nem találja, aztán visszavág, és a raj hozzá közeli hajói beszállnak a harcba az első pilóta ellen, aki eltalálta (a távolságot a fenti szabályok adják meg). A Pirate Scoutok kivételek: megtámadnak minden pilótát, aki a közelükbe ér. A vezér a hajótestét soha nem javítja meg magától, így a sebzés, amelyet okoztál, rajta marad, hacsak a kísérői meg nem gyógyítják; a pajzsa úgy töltődik újra, mint bármely idegené.
- **A rajhajók csak pilótákkal harcolnak.** Nem lőnek idegenekre, az idegenek sem lőnek rájuk, a [vállalati pilóták](/wiki/03-Mechanics/Company-Pilots.md) pedig figyelmen kívül hagyják őket: nem vadásznak rajhajóra, és nem sietnek a segítségedre ellene.
- **Rakéták.** A Pirate Boss, valamint a Dormant Force és a Pulse-ok **egyenes** rakétákat, [Rivet-rakétákat](/wiki/06-Items/Rockets.md) lőnek arra a pilótára, aki megtámadta őket. A folyamatosan mozgó hajó kitér előlük, az álló hajót eltalálják.
- **A harcok mérete.** A Seeker-raj két pilótának való, a Pirate-raj egy kis csoportnak, a Dormant-raj a legerősebb hajók nagy csoportjának; a magasabb világokhoz több pilóta kell, mint minden idegennél.

## Mit vigyél magaddal {#what-to-bring}

- **Egy csoportot.** Repülj [csoportban](/wiki/03-Mechanics/Groups.md): a rajok csoportokra vannak kiegyensúlyozva, az egyedül repülő alacsony szintű pilótát gyorsan megsemmisítik, és csak a legerősebb hajók győzhetnek le egyedül egy Pirate Bosst. A Dormant-rajat senki sem győzi le egyedül. A raj azt a pilótát támadja, aki először eltalálta ([Kit támad az idegen](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)), ezért a csoport legellenállóbb hajója kezdje.
- **Jobb lőszert.** Vigyél x2 vagy jobb lőszert (lásd [Lézerek és lőszer](/wiki/06-Items/Lasers.md)). A raj kísérőinek gyógyítása több lehet annál, amennyit egy kis csoport x1 lőszerrel okoz.
- **Pajzsot és javítást** egy hosszú harchoz: a hajód képességei ([Képességek](/wiki/03-Mechanics/Abilities.md)) a kalózok elleni harcban számítanak a legtöbbet, mert az percekig tart.
- **Mozgásteret.** Maradj olyan fegyver hatótávján kívül, amelynél nagyobb a hatótávod, és mozogj folyamatosan a rakéta ellen.

## Hogyan fizet egy boss megölése {#how-a-boss-kill-pays}

A közönséges idegen annak a pilótának fizet, aki először eltalálta ([Harc](/wiki/03-Mechanics/Combat.md#kill-rewards-first-hit-claims)). A raj vezére és minden Dormant Pulse ehelyett **a leadott sebzés szerint** fizet:

- **A fizetést a sebzés szerint osztják el.** Minden pilóta, aki legalább a fenti szabályokban megadott részt okozta, fizetést kap, a leadott sebzéssel arányosan: a kilövés kreditjét, Thuliumát, XP-jét és becsületét elosztják köztük. Aki a rész alatt marad, semmit sem kap.
- **A rakományláda annak a pilótának jár, aki a legtöbb sebzést okozta.** Az övé (és a klánjáé) 30 másodpercig, mint minden idegennél, utána bárki elviheti ([Rakomány](/wiki/03-Mechanics/Cargo.md)). Minden Dormant-hajónak saját sebzésszámlálója és saját ládája van.
- **A kísérők a megszokott módon fizetnek**: a Pirate Scoutok és a Seeker Slave-ek annak a pilótának fizetnek, aki először eltalálta őket, és a fizetésük kicsi egy boss fizetéséhez képest.
- **Egy boss fizetése úgy van megszabva, hogy felülmúlja a körülötte lévő idegeneket.** Egy perc harc egy Pirate Bossszal többet fizet, mint egy perc harc egy Goombah ellen, a Dormant-raj pedig még többet; a Boss Seeker pontosan tíz Seekert fizet.

Minden kilövést a hajó saját neve alatt számolnak a kilövési statisztikádban, és PvE-pontokat ad a rangsorodhoz:

<!-- swarms-points:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Rajhajó | Raj | PvE-pont kilövésenként |
| :--- | :--- | ---: |
| **Pirate Boss** | Pirate-raj | 10 |
| **Pirate Scout** | Pirate-raj | 1 |
| **Dormant Force** | Dormant-raj | 25 |
| **Dormant Pulse** | Dormant-raj | 10 |
| **Boss Seeker** | Seeker-raj | 5 |
| **Seeker Slave** | Seeker-raj | 1 |

<!-- swarms-points:end -->

A rajkilövés nem számít más idegen kilövésének: a Boss Seeker vagy a Seeker Slave nem Seeker annak a küldetésnek, amely Seekereket kér, a wipe-pontok mérföldkövei ([Wipe-idővonal](/wiki/03-Mechanics/Wipe-Timeline.md#earning-wipe-points)) pedig csak az öt idegenéi.
