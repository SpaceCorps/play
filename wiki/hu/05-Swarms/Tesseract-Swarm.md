<!-- wiki-i18n source: 98e91b2bd1dede81 -->
<!-- wiki-i18n title: Tesseract-raj -->
# Tesseract-raj {#tesseract-swarm}

A Tesseract-raj egyetlen hatalmas anyahajó, a **Tesseract**, és a **Facetek**, amelyeket addig bocsát ki, amíg találatot kap. A Tesseract a [veszélyes szektor](/wiki/01-General/Danger-Sectors.md) `DS-4` egy rögzített pontján él, nincs saját fegyvere, és soha nem hagyja el a szektorát. A legerősebb pilóták nagyon nagy csoportjának készült: hajóteste és pajzsa messze felülmúlja a Crystalysét, és amint békén hagyják, magától javítja magát. A veszélyes szektorok PvP-szektorok, ezért a harc a Faceteken kívül rivális pilótákat is odacsalhat.

## Röviden {#at-a-glance}

<!-- tesseract-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Hol**: A veszélyes szektor: `DS-4`
- **Hány**: Világonként egy
- **Megjelenik**: A szezon 4. napjától a wipe-ig (Betában és Gammában: a szezon 1. napjától)
- **Vezér**: Tesseract
- **Otthon**: A szektortérkép 25 900, 11 900 pontjától legfeljebb 2 500 egységre
- **Regeneráció**: Alphában másodpercenként 125 000 HP, előbb a hajótest, aztán a pajzs, miután 5 mp telt el sebzés nélkül
- **Kísérők**: Legfeljebb 100 × Facet, 5 mp múlva 20 újabb, amíg a vezért találatok érik
- **A kísérők érkezése**: Csak amíg a vezért az elmúlt 5 mp alatt találat érte, tőle legfeljebb 400 egységre
- **Vadászok**: Minden Facet saját szakaszokat repül a vezér körül, tőle legfeljebb 3 600 egységre, és senkit sem üldöz. Arra a legközelebbi pilótára tüzel, aki eltalálta a vezért, ha az a hatótávjában van. Ha nincs kire lőnie, tovább repked a vezér körül, és az utolsó találat után 20 mp múlva elmegy
- **A vezér megsemmisül**: A kísérők a vezér megsemmisülése után 1 perc múlva eltűnnek, akkor is, ha éppen támadnak
- **Visszatér**: {{guide:vitals.respawn@Tesseract#1;Tesseract#2;Tesseract#3}} azután, hogy a vezér megsemmisült, ugyanabban a szektorban
- **Értesítés**: A szektor pilótái értesülnek arról, mikor jelenik meg a vezér, és mikor semmisül meg. Ezek rendszersorok: a chat **Rendszer** lapján jelennek meg, olvasatlan sorok számlálójával, és nem a **Globális** vagy a **Helyi** lapon. A kill feed megnevezi a pilótát, akinek a kilövést jóváírják.

<!-- tesseract-glance:end -->

## A tagok {#the-members}

- **Tesseract**: egy kocka alakú anyahajó, többszöröse egy Crystalys méretének, sötét kovácsolt vasból, izzó parázsvarratokkal és a nevével a feje fölött. Az elülső falában egy öböl kinyílik, amíg találatok érik, a tetején pedig egy izzó kocka forog egy ketrecben. Passzív: amíg senki sem sebzi, lassan sodródik a saját területén belül, és amint egy pilóta eltalálja, megáll, és tartja a helyét. Nem lő semmire, és senkit sem üldöz; a védelme a mérete, a javulása és a Facetek, amelyeket kibocsát.
- **Facet**: egy kicsi, gyors hajó ugyanabból a sötét vasból, izzó élekkel, világító lencsével az orrában és két lebegő szárnylemezzel. Csak addig létezik, amíg a Tesseractot találatok érik. Senkit sem üldöz: a Tesseract mellett marad, rövid, saját szakaszokat repül véletlenszerű helyekre körülötte, és arra a legközelebbi pilótára tüzel, aki eltalálta a Tesseractot, amint egy is a hatótávjába kerül. Elmegy, amikor a Tesseractot békén hagyják. Gyorsabb bármelyik hajónál, ezért a rajtól menekülni nem segít, de aki messze marad a Tesseracttól, arra soha nem lőnek.

## A harc menete {#how-the-fight-goes}

- **Hozz egy nagyon nagy csoportot, és csapjatok le együtt.** A Tesseract hajótestét és pajzsát milliós pontkészlet adja, ezért a harc még erős hajók nagy csoportjának is sokáig tart, a fizetést pedig a sebzés szerint osztják el: minden jelen lévő pilóta számít.
- **Soha ne hagyd békén.** Ha senki sem sebezte a *Röviden* listában megadott ideig, előbb a hajótestét, majd a pajzsát javítja ezzel a sebességgel, így néhány másodperces szünet egy hosszú perc munkáját semmisítheti meg. A teljesen kijavult Tesseract elfelejti, ki sebezte: a fizetés és a zsákmány a megölő harc sebzése szerint alakul.
- **Minden találat hívja a Faceteket.** Amíg a Tesseractot találatok érik, néhány másodpercenként egy csapat Facet érkezik a közelébe, a *Röviden* listában megadott felső határig. Amíg senki sem találja el, egy sem jön, a már ott lévők pedig várnak, majd elmennek.
- **A Facetek a Tesseract körül repkednek, és arra lőnek, aki a hatótávjukba kerül.** Nem a legtöbb sebzést okozó pilótára és nem is egyetlen pilótára vadásznak: minden Facet saját rövid szakaszokat repül a Tesseract körüli széles gyűrű véletlenszerű helyeire, minden irányban, és amint egy olyan pilóta kerül a hatótávjába, aki eltalálta a Tesseractot, a legközelebbire tüzel. Az együtt maradó csoport egyszerre kevesebb Facet hatótávjába esik, és megosztja a tüzüket, szemben a Tesseract körül szétszóródott csoporttal. Egy Facetnek kevés a hajótestje és a pajzsa, és ha lelősz egyet, annyit fizet, mint egy [Phantasm](/wiki/04-Aliens/Phantasm.md), de egy sorozatot levesz a közelében lévő pilótákról. Aki nem találta el a Tesseractot, az nem a célpontjuk.
- **Aki elég messze marad, azt békén hagyják.** A Facetek soha nem távolodnak el a Tesseracttól jobban, mint a *Röviden* listában megadott távolság; aki ezen a távolságon és egy Facet lézerének hatótávján túl marad, azt nem lövik, akármennyi sebzést okozott is. Az a Facet, amelynek nincs kire lőnie, tovább repked a Tesseract körül, és elmegy, amikor a Tesseractot békén hagyják.
- **A Beta és a Gamma keményebb.** Ezeknek a világoknak a rajai erősebbek ([Világok](/wiki/05-Swarms/Swarms.md#the-worlds)), és ugyanígy a Tesseract javulása és minden Facet sorozata is.
- **A veszélyes szektorok PvP-szektorok.** Egy rivális a harc közepén megtámadhatja a csoportot. A roncsnál nincs láda, amelyre várhatna: a zsákmány minden pilótának, akit a megölés kifizet, egy [privát láda](/wiki/03-Mechanics/Cargo.md#private-boxes), amelyet csak az a pilóta lát és vehet fel. Ne egyedül menj.
- **A Tesseract visszatér** a *Röviden* listában megadott idő múlva, teljes erővel, a helyén.

## A vezér három lépése {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

A harcának három lépése van ([hogyan működnek](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); mindegyik egyszer történik meg, és elölről kezdődnek, amint teljesen meggyógyult.

- **Kétharmad alatt**: 20 további hajó érkezik egyszerre a szokásos számuk fölött: Facets.

<!-- mob-ladder:end -->

## Jutalmak és zsákmány {#rewards-and-drops}

A Tesseract azt fizeti, amit a harc megér: annyit, mint sok Crystalys együtt, és a felvett sebzéshez képest többet, mint egy Crystalys, a legjobban fizető idegen. A fizetést a sebzés szerint osztják el a vele harcoló pilóták között ([hogyan fizet egy boss megölése](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). A legtöbb sebzést okozó pilótának nincs külön láda. Minden pilóta, akit a megölés kifizet, saját [privát ládát](/wiki/03-Mechanics/Cargo.md#private-boxes) kap, amelyet csak ő lát és vehet fel, 10 percig. A ládában Reinforced Hull Plate, Velkonite Reinforced Plate, Orvium Reinforced Plate, Power Core, Ancient Control Unit és Dark Matter van. A sebzésből rá eső részre dobják, mint egy [Clan Warden](/wiki/03-Mechanics/Clans.md#warden-pay-and-loot) zsákmányát: aki a sebzés ötödét okozta, a táblázatbeli mennyiségek nagyjából ötödét kapja, csoportban pedig mindenki a csoport részéből kapja a magáét, ahogy a fizetést is elosztják. A Dark Matterre pilótánként felső határ vonatkozik: egy megölésből legfeljebb 5-öt kap, bármekkora is a részesedése (csoportban előbb mindenki része válik le, és a határ mindenkire külön vonatkozik), és ami a határ fölé esik, elvész, nem kapják meg a többiek. Egy Facet ugyanazt a Kreditet, Thuliumot, XP-t és Becsületet fizeti, mint egy [Phantasm](/wiki/04-Aliens/Phantasm.md); a megölése megölésnek számít (a statisztikádban, az eredményeknél és a drónjaid meg P.E.T.-jeid tapasztalatánál), de nem ejt semmit, és nem ad PvE-pontot.

## A számok {#the-numbers}

A raj hajóinak értékei mindhárom világban ([Világok](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- tesseract-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Tesseract

Alapja: Crystalys, hajótestének 625%-a; nincs fegyvere, a pajzsa és a sebessége saját.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | {{guide:vitals.hull@Tesseract#1}} | {{guide:vitals.hull@Tesseract#2}} | {{guide:vitals.hull@Tesseract#3}} |
| Pajzs | {{guide:vitals.shield@Tesseract#1}} | {{guide:vitals.shield@Tesseract#2}} | {{guide:vitals.shield@Tesseract#3}} |
| Lézersebzés (másodpercenként egy sorozat) | nincs | nincs | nincs |
| Sebesség | {{guide:vitals.speed@Tesseract#1}} | {{guide:vitals.speed@Tesseract#2}} | {{guide:vitals.speed@Tesseract#3}} |
| Lézer hatótávja | – | – | – |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Javít, másodpercenként, 5 mp sebzés nélküli idő után (előbb hajótest, aztán pajzs) | 125 000 | 187 500 | 250 000 |
| Kredit | {{guide:spoils.pay.credits@Tesseract#1}} | {{guide:spoils.pay.credits@Tesseract#2}} | {{guide:spoils.pay.credits@Tesseract#3}} |
| Thulium | {{guide:spoils.pay.thulium@Tesseract#1}} | {{guide:spoils.pay.thulium@Tesseract#2}} | {{guide:spoils.pay.thulium@Tesseract#3}} |
| Tapasztalat (XP) | {{guide:spoils.pay.experience@Tesseract#1}} | {{guide:spoils.pay.experience@Tesseract#2}} | {{guide:spoils.pay.experience@Tesseract#3}} |
| Becsület | {{guide:spoils.pay.honor@Tesseract#1}} | {{guide:spoils.pay.honor@Tesseract#2}} | {{guide:spoils.pay.honor@Tesseract#3}} |
| PvE-pont kilövésenként | 42 | 42 | 42 |

**Zsákmány minden pilótának, akit a megölés kifizet**: egy láda mindegyiküknek, csak neki, a mennyiségek rá eső részével.

| Tárgy |
| :--- |
| {{guide:spoils.box@Tesseract#1;Tesseract#2;Tesseract#3}} |

### Facet

Alapja: Seeker, hajótestének 2 500%-a és lézersebzésének 463%-a; a pajzsa, a sebessége és a hatótávja saját.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | {{guide:vitals.hull@Facet#1}} | {{guide:vitals.hull@Facet#2}} | {{guide:vitals.hull@Facet#3}} |
| Pajzs | {{guide:vitals.shield@Facet#1}} | {{guide:vitals.shield@Facet#2}} | {{guide:vitals.shield@Facet#3}} |
| Lézersebzés (másodpercenként egy sorozat) | {{guide:vitals.dps@Facet#1}} | {{guide:vitals.dps@Facet#2}} | {{guide:vitals.dps@Facet#3}} |
| Sebesség | {{guide:vitals.speed@Facet#1}} | {{guide:vitals.speed@Facet#2}} | {{guide:vitals.speed@Facet#3}} |
| Lézer hatótávja | 600 | 600 | 600 |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Kredit | {{guide:spoils.pay.credits@Facet#1}} | {{guide:spoils.pay.credits@Facet#2}} | {{guide:spoils.pay.credits@Facet#3}} |
| Thulium | {{guide:spoils.pay.thulium@Facet#1}} | {{guide:spoils.pay.thulium@Facet#2}} | {{guide:spoils.pay.thulium@Facet#3}} |
| Tapasztalat (XP) | {{guide:spoils.pay.experience@Facet#1}} | {{guide:spoils.pay.experience@Facet#2}} | {{guide:spoils.pay.experience@Facet#3}} |
| Becsület | {{guide:spoils.pay.honor@Facet#1}} | {{guide:spoils.pay.honor@Facet#2}} | {{guide:spoils.pay.honor@Facet#3}} |
| PvE-pont kilövésenként | 0 | 0 | 0 |

**Zsákmány**: nincs. A kilövés csak a kreditjét, Thuliumát, XP-jét és becsületét fizeti.

<!-- tesseract-members:end -->
