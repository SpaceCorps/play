<!-- wiki-i18n source: 6c44f12b3eb7ef7a -->
<!-- wiki-i18n title: Kutatás -->
# Kutatás {#research}

A **Kutatóközpont** a [Skylabod](/wiki/03-Mechanics/Skylab.md) laboratóriuma. Nyersanyagokkal táplálod, ő **tudománnyá** alakítja őket, a tudomány pedig **technológiákat** kutat. A [Gyártás](/wiki/06-Items/Overview.md#upgrading-modules) minden elkészítéséhez előbb a technológiája kell: hajót, lézert, fúvókát vagy CPU-t addig nem lehet legyártani, amíg ki nem kutatták.

Ez az oldal tartalmazza a teljes technológiafát az egyes technológiák idejével, azt, hogy az egyes nyersanyagok mennyi tudományt adnak, a Thulium-boostot, a Dark Matter szabályát és az új CPU-kat. A számokat a játék saját adataiból olvassuk, ezért mindig azok szerepelnek itt, amelyek a játékban.

![The Research view with a technology that needs Dark Matter picked: its Dark Matter row, the Add and Take back buttons, where Dark Matter comes from and the Wiki button](../../img/wiki-img/shots/research-dark-matter.jpg)
![The Research view filtered to the Defence tree: the shield and hull formations, each a technology with its Dark Matter](../../img/wiki-img/shots/research-formations.jpg)
![The Research view of the Skylab with the pointer on Impulse Thruster III: its kind and tier, what it does, its numbers, the four tiers of its family and what Assembly asks to craft it](../../img/wiki-img/shots/research-hover.jpg)

## A Kutatóközpont {#the-research-centre}

<!-- research-centre:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **A Mag 10. szintjétől.** A Kutatóközpont a [Skylabod](/wiki/03-Mechanics/Skylab.md) egy modulja, a többihez hasonlóan építed: 25 Ship Fragment a leltáradból (leszállt hajóval), 25 000 kredit és 500 Thulium. A képernyője a Skylab-oldal **Kutatás** nézete.
- **1–10. szint.** A magasabb szint nagyobb tartályt ad, és több energiát fogyaszt. A kutatást nem teszi gyorsabbá: egy technológia minden szinten ugyanannyi ideig tart.
- **A tartály.** A Kutatóközpont a tudományát egy tartályban tartja, amely az 1. szinten 12 óra kutatásnyit tárol, és minden szinttel 25%-kal többet (lásd a lenti táblázatot).
- **Az üzemanyagból tudomány lesz.** A betáplált nyersanyag azonnal tudománnyá válik, ahogy az üzemanyag-táblázat mutatja. Egy kutatás a kutatási idejének minden másodpercében 1 tudományt éget el; üres tartálynál várakozik, és folytatódik, amint újra táplálod a Kutatóközpontot.
- **Ingyenes első óra.** Az új Kutatóközpont 3 600 tudománnyal indul a tartályában, ami 1 óra kutatás.
- **Egyszerre egy.** A Kutatóközpont egyszerre csak egy technológiát kutat, de a Sorba gombbal akár 5 továbbit beállíthatsz mögé. Mindegyik magától indul, amint az előtte lévő kész, akkor is, ha nem vagy ott. A sorba állítás ingyen van: a technológia az indulásakor veszi el a Dark Matter-t, a sorban álló pedig ingyen kivehető.
- **Amíg távol vagy.** A kutatás a szerver órája szerint fut, ezért kijelentkezés után is megy tovább, amíg el nem készül vagy ki nem ürül a tartály. Az energiahiány vagy a Kutatóközpont fejlesztése nem állítja meg.
- **Energia.** A Kutatóközpont az 1. szinten 25 energiát fogyaszt, és minden szinttel 15%-kal többet, és nem kapcsolható ki.
- **A wipe mindent megtart:** a technológiáidat, a tartály tudományát, a belehelyezett Dark Mattert, a folyamatban lévő kutatást és a boostot.
- **Ami a tiéd, az a tiéd marad.** Amikor a kutatás megjelent a játékban, minden pilóta megkapta minden már birtokolt tárgyának technológiáját, és azokat a technológiákat, amelyekre ezeknek szükségük volt. Az a tárgy, amely később jut hozzád (ajándék, kód, jutalom), nem nyitja meg a technológiáját.
- **A Mag 10. szintje alatt** nem kutathatsz, így a Gyártásban még semmi újat nem készíthetsz el. Az állomásküldetések végigvezetnek a Mag szintjein.

<!-- research-centre:end -->

**A lézererősítők és az utolsó szint.** A II–IV. szintű Damage, Crit és Penetration Amp-eket úgy kell kikutatni, mint minden mást, ami gyártható. Azok a pilóták, akik az erősítővonalak érkezésekor erősítőt birtokoltak vagy sorba állítottak, megkapták mindegyik technológiáját és az alatta lévő szintekét. Tizenkét technológiához másik fa technológiája kell, a Dark Matter Plate-é, az Erőforrások fáról, mert minden fejlesztési lánc utolsó szintje három plate-et kér. Ezek: a IV. szintű Damage, Crit és Penetration Amp, a IV. szintű Absorption és Capacity Shield Cell, a IV. szintű Impulse és Momentum Thruster, a Heavy Shield Core, az Engine III, a Helios Beam, az Extra Slots CPU III és a Base CPU II. Aki korábban kikutatta valamelyiket, az megtartja, de a plate-jeinek elkészítéséhez szüksége van a plate technológiájára. Az alábbi fa nem rajzol hozzá nyilat, de a táblázat felsorolja, a játékbeli kártya pedig megnevezi ([Dark Matter és Dark Matter Plate-ek](/wiki/03-Mechanics/Dark-Matter.md)).

A Skylabod **Kutatás** nézetében egy technológia többet mond el, mint az alábbi fák egy doboza. Vidd az egeret egy technológia fölé, és megnyílik egy kártya a kutatási idővel és az elégetett tudománnyal, alatta pedig azzal, hogy a tárgy **micsoda és mit tud**: a fajtája és a fokozata a családjában (például a négy Impulse Thruster harmadik), a leírása, az értékei úgy, ahogy a Hangár és a Bolt mutatja őket (egy lézer sebzése, kritikus esélye és hatótávja, egy pajzs kapacitása, töltődési sebessége és elnyelése, egy fúvóka sebességnövelése és sebességszorzója, egy rakéta sebzése, robbanási sugara és hatótávja, mit ad egy drónformáció és mibe kerül neked), a családja fokozatainak kis táblázata, és az, amit a Gyártás utána kér az elkészítéséhez: az idő, a kredit és a Thulium, valamint az anyagok. Így láthatod, mit ad egy fokozat, mielőtt kikutatnád. Kattints egy technológiára a kiválasztásához: a fa melletti kártya ugyanezt teljes egészében mutatja, a **Kutatás indítása** gomb alatt. Amíg egy kutatás fut, a **Sorba** gomb lép az indítás helyére: a sorba állított technológia a fán mutatja a sorszámát, a futó kutatás alatti sorkártya pedig mindet felsorolja, mindegyik mellett egy kereszttel a kivételhez. Ha a következő nem tud elindulni (a hozzá kellő Dark Matter nincs a Kutatóközpontban, vagy üres a tartály), a sor vár, és megmondja az okát, amíg ki nem javítod, és meg nem nyomod a **Sor indítása** gombot.

### A tartály minden szinten {#the-tank-at-every-level}

<!-- research-tank:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Szint | Tartály (tudomány) | Ennyi kutatásra elég | … boosttal | Energia |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 43 200 | 12 óra | 6 óra | 25 |
| 2 | 54 000 | 15 óra | 7,5 óra | 28,7 |
| 3 | 67 500 | 18,8 óra | 9,4 óra | 33,1 |
| 4 | 84 375 | 23,4 óra | 11,7 óra | 38 |
| 5 | 105 469 | 29,3 óra | 14,6 óra | 43,7 |
| 6 | 131 836 | 36,6 óra | 18,3 óra | 50,3 |
| 7 | 164 795 | 45,8 óra | 22,9 óra | 57,8 |
| 8 | 205 994 | 57,2 óra | 28,6 óra | 66,5 |
| 9 | 257 492 | 71,5 óra | 35,8 óra | 76,5 |
| 10 | 321 865 | 89,4 óra | 44,7 óra | 87,9 |

<!-- research-tank:end -->

## Üzemanyag {#fuel}

A Kutatóközpontot nyersanyagokkal táplálod, és minden egység azonnal tudománnyá válik. Minél több munkába kerül egy egység megszerzése, annál több tudományt ad: az értékek azt követik, mennyire nehéz megszerezni, nem a ritkasági címkét. Az ércek kivételek: egy egység több tudományt ad, mint ahány másodperc alatt egy gyűjtő kitermeli, így egy a szintjei közepén járó gyűjtő egy óra érce nagyjából két óra kutatást táplál. Az ércek a [Skylabod](/wiki/03-Mechanics/Skylab.md#resource-storage) Erőforrás-raktárából jönnek, minden más nyersanyag a készletedből, és a hajódnak le kell szállnia. A Velkonite Reinforced Plate, az Orvium Reinforced Plate, a Dark Matter Plate, a Dark Matter, a kredit és a Thulium nem égethető el; a Reinforced Hull Plate igen.

<!-- research-fuel:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Nyersanyag | Ritkaság | Innen veszi | Tudomány egységenként | Egységek 1 órára |
| :--- | :--- | :--- | ---: | ---: |
| [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) | Gyakori | A leltárad | 5 | 720 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | Gyakori | A leltárad | 5 | 720 |
| [Daraxium](/wiki/06-Items/Resources.md#daraxium) | Gyakori | A leltárad | 7 | 515 |
| [Nyxite](/wiki/06-Items/Resources.md#nyxite) | Gyakori | A leltárad | 7 | 515 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | Gyakori | A leltárad | 8 | 450 |
| [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) | Gyakori | A leltárad | 33 | 110 |
| [Power Core](/wiki/06-Items/Resources.md#power-core) | Szokatlan | A leltárad | 100 | 36 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | Szokatlan | Erőforrás-raktár | 210 | 18 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | Ritka | Erőforrás-raktár | 321 | 12 |
| [Ancient Control Unit](/wiki/06-Items/Resources.md#ancient-control-unit) | Ritka | A leltárad | 650 | 6 |

Az utolsó oszlop azt mutatja, hány egység fedez egy óra kutatást boost nélkül, felfelé kerekítve; boosttal ennek 2-szerese kell.

<!-- research-fuel:end -->

## A Thulium-boost {#the-thulium-boost}

<!-- research-boost:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **5 000 Thulium** egy boostot vesz: a Kutatóközpont **24 órán át 2-szer gyorsabban** kutat.
- A tudományt is **2-szer gyorsabban égeti el**, ezért a boost időt vesz, soha nem üzemanyagot: egy technológia ugyanannyi tudományt éget el, boosttal vagy anélkül.
- A boost abban a pillanatban elindul, amikor megveszed, és az óra szerint fut, akár van üzemanyag a tartályban, akár nincs, ezért futó kutatás közben vedd meg. A Kutatóközpont visszautasítja, ha éppen semmit sem kutat.
- A boostok összeadódnak: ha egyet vásárolsz, miközben egy másik fut, az 24 órával megtoldja a végét, legfeljebb 72 órával előre. A boost a Kutatóközponthoz tartozik, nem egy kutatáshoz.

Mit tesz a boost egy kutatás idejével, ha az elejétől fogva működik:

| Kutatási idő | Boosttal | Boostok az egészre | Thulium |
| :--- | :--- | ---: | ---: |
| 30 perc | 15 perc | 1 | 5 000 |
| 3 óra | 1 óra 30 perc | 1 | 5 000 |
| 6 óra | 3 óra | 1 | 5 000 |
| 10 óra | 5 óra | 1 | 5 000 |
| 1 nap | 12 óra | 1 | 5 000 |
| 2 nap | 1 nap | 1 | 5 000 |

<!-- research-boost:end -->

## Dark Matter

A fa csúcsán lévő technológiákhoz Dark Matter is kell. A [feketelyukból](/wiki/03-Mechanics/Black-Hole.md#dark-matter) származik, ahol egy N.I.K.E. rakéta, amely eléri, hagy valamennyit, és időnként a [Dormant-raj](/wiki/05-Swarms/Dormant-Swarm.md) egy Dormant Pulse-ától.

<!-- research-dark-matter:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **10 Dark Matter** az alábbi táblázat 16 technológiájának mindegyikéhez, a tudományon felül: a kutatás indulása előtt helyezd be a Kutatóközpontba (a leltáradból, leszállt hajóval), és a kutatás induláskor elveszi.
- **A szabály:** egy Epikus vagy magasabb ritkaságú tárgy, amelynek kutatása 10 óra vagy tovább tart. Az N.I.K.E.-nek, amely a Dark Matter forrása, soha nincs rá szüksége.
- **A drónformációk** kívül esnek a szabályon: minden formációkutatás Dark Mattert kér, erősségtől függően 5, 13 vagy 20 darabot, ahogy a táblázat mutatja.
- **A hajótest-páncélzat** szintén kívül esik a szabályon: két kutatása többet kér, egy napnyi kutatásért 25, két napért 40 Dark Mattert, ahogy a táblázat mutatja.
- **Ha megszakítasz egy kutatást,** a hozzá belehelyezett Dark Matter visszakerül a Kutatóközpontba. A haladás és az addig elégetett tudomány nem.
- Együtt 414 Dark Mattert kérnek.

| Technológia | Ritkaság | Kutatási idő | Dark Matter |
| :--- | :--- | :--- | ---: |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | Epikus | 10 óra | 10 |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | Epikus | 10 óra | 10 |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | Epikus | 10 óra | 10 |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | Epikus | 10 óra | 10 |
| [Starfire-III](/wiki/06-Items/Lasers.md#lasers) | Mitikus | 1 nap | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | Mitikus | 1 nap | 10 |
| [Damage Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Epikus | 10 óra | 10 |
| [Crit Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Epikus | 10 óra | 10 |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | Epikus | 1 nap | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | Epikus | 1 nap | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | Mitikus | 2 nap | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | Mitikus | 1 nap | 10 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | Legendás | 1 nap | 10 |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | Epikus | 1 nap | 10 |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | Epikus | 1 nap | 10 |
| [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epikus | 10 óra | 5 |
| [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epikus | 1 nap | 13 |
| [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epikus | 10 óra | 5 |
| [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Mitikus | 2 nap | 20 |
| [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epikus | 10 óra | 5 |
| [Ballista Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epikus | 1 nap | 13 |
| [Stiletto Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Mitikus | 2 nap | 20 |
| [Rampart Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Mitikus | 2 nap | 20 |
| [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epikus | 1 nap | 13 |
| [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epikus | 10 óra | 5 |
| [Culler Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epikus | 1 nap | 13 |
| [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epikus | 1 nap | 13 |
| [Auger Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epikus | 1 nap | 13 |
| [Cordon Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epikus | 1 nap | 13 |
| [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epikus | 10 óra | 5 |
| [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epikus | 1 nap | 13 |
| [Penetration Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Epikus | 10 óra | 10 |
| [Hull Plating II](/wiki/06-Items/Hull-Plating.md#the-three-platings) | Ritka | 1 nap | 25 |
| [Hull Plating III](/wiki/06-Items/Hull-Plating.md#the-three-platings) | Epikus | 2 nap | 40 |

<!-- research-dark-matter:end -->

## A technológiafa {#the-technology-tree}

Minden doboz egy technológia: az a tárgy, amelynek legyártását lehetővé teszi, a neve alatt a kutatási idővel (az óra), és ahol Dark Matter kell, a Dark Matter-jelvénnyel. A nyíl az egyik technológiától arra vezet, amelynek szüksége van rá, és amelyet előbb kutatsz ki; nyíl nélküli doboz azonnal kikutatható. Vidd az egeret egy doboz fölé, hogy lásd a kutatási időt, az elégetett tudományt és azt, amit a Gyártás utána kér a tárgyért, és kattints rá a tárgy oldalának megnyitásához. A fákat a játék saját adataiból rajzoljuk. Két fa, a **Védelem** és a **Támadás és mozgékonyság** tartalmazza a tizenhat [drónformációt](/wiki/03-Mechanics/Formations.md).

<!-- research-tree:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

### Hajtás és sebesség {#tree-propulsion}

```tree research
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines

Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```

### Pajzsok és védelem {#tree-shields}

```tree research
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cores

Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```

### Lézerek és lőszer {#tree-lasers}

```tree research
Quantum Laser III | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Quantum Laser II, 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-III | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser III, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-III, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Damage Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Crit Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Damage Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Damage Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Crit Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Crit Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Penetration Amp I, 20 Daraxium, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Penetration Amp II, 1 Power Core, 30 Nyxite, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp IV | laser-amp, epic | craft 1200 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Penetration Amp III, 1 Power Core, 30 Cataclysite, 40 Quorvium, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-

Quantum Laser III => Starfire-III => Helios Beam
Damage Amp II => Damage Amp III => Damage Amp IV
Crit Amp II => Crit Amp III => Crit Amp IV
Penetration Amp II => Penetration Amp III => Penetration Amp IV
```

### Boosterek {#tree-boosters}

```tree research
Laser Damage Booster II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
```

### Drónok {#tree-drones}

```tree research
Master Drone | drone, rare | craft 40000 Thulium, 60 s | research 36000 s, 36000 science | 1 Slave Drone, 100 Ship Fragment | /wiki/06-Items/Drones.md#available-drones
```

### Hajók {#tree-ships}

```tree research
Paragon | ship, rare | craft 1500 Thulium, 900 s | research 21600 s, 21600 science | 120 Ship Fragment, 20 Reinforced Hull Plate, 5 Power Core | /wiki/02-Ships/Paragon.md
Ironclad | ship, epic | craft 10500 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit | /wiki/02-Ships/Ironclad.md
Storm | ship, epic | craft 15000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit | /wiki/02-Ships/Storm.md
Wraith | ship, mythical | craft 20000 Thulium, 900 s | research 172800 s, 172800 science, 10 Dark Matter | 300 Ship Fragment, 50 Reinforced Hull Plate, 15 Power Core, 3 Ancient Control Unit | /wiki/02-Ships/Wraith.md
```

### Erőforrások {#tree-resources}

```tree research
Dark Matter Plate | resource, mythical | craft 250 Thulium, 120 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Velkonite Reinforced Plate, 1 Orvium Reinforced Plate, 5 Dark Matter | /wiki/06-Items/Resources.md#dark-matter-plate
```

### Rakéták {#tree-rockets}

```tree research
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
```

### CPU-k {#tree-cpus}

```tree research
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 6 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 2 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Extras.md#base-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu

Extra Slots CPU I => Extra Slots CPU II => Extra Slots CPU III
Base CPU I => Base CPU II => Jump CPU
```

### Védelem {#tree-defence}

```tree research
Testudo Formation | formation, epic | craft 7500 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Adamant Formation | formation, epic | craft 9000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Rampart Formation | formation, mythical | craft 38500 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Sanctum Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Redoubt Formation | formation, epic | craft 21000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Cordon Formation | formation, epic | craft 21500 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations

Testudo Formation => Sanctum Formation => Rampart Formation
Adamant Formation => Redoubt Formation => Cordon Formation
```

### Támadás és mozgékonyság {#tree-strike-mobility}

```tree research
Bodkin Formation | formation, epic | craft 21000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Asterism Formation | formation, epic | craft 7000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Gemini Formation | formation, mythical | craft 38000 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Ballista Formation | formation, epic | craft 24000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Stiletto Formation | formation, mythical | craft 46000 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Shrike Formation | formation, epic | craft 8500 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Culler Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Auger Formation | formation, epic | craft 20500 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Centurion Formation | formation, epic | craft 8000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Gyre Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations

Asterism Formation => Bodkin Formation => Ballista Formation
Gemini Formation => Stiletto Formation
Centurion Formation => Shrike Formation => Culler Formation
Gyre Formation => Auger Formation
```

### Hajótest-páncélzat {#tree-hull-plating}

```tree research
Hull Plating II | hull-plating, rare | craft 2500 Thulium, 300 s | research 86400 s, 86400 science, 25 Dark Matter | 1 Hull Plating I, 150 Ship Fragment, 20 Reinforced Hull Plate, 6 Power Core, 5 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating III | hull-plating, epic | craft 4000 Thulium, 600 s | research 172800 s, 172800 science, 40 Dark Matter | 1 Hull Plating II, 300 Ship Fragment, 40 Reinforced Hull Plate, 12 Power Core, 1 Ancient Control Unit, 8 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings

Hull Plating II => Hull Plating III
```


<!-- research-tree:end -->

## Hajódizájnok és páncélzatfoglalatok {#ship-technologies}

A Skylab kutatási nézetének Hajók családjában kétféle technológia van, amely nem gyártás. A fenti fa kihagyja őket, mert amit megnyitnak, az egy foglalat vagy egy átalakítás, nem tárgy.

- **Páncélzatfoglalatok.** Egy technológia a négy hajó, amelyet készítesz, minden [páncélzatfoglalatához](/wiki/06-Items/Hull-Plating.md#hull-plate-slots). Mindegyik az előző után jön, az első a hajó saját technológiája után. A játékban egy hajó foglalatai egyetlen kártya, foglalatonként egy ponttal.
- **Hajódizájnok.** Egy technológia minden [dizájnhoz](/wiki/03-Mechanics/Ship-Designs.md). Mindegyikhez kell a hajója technológiája meg a Dark Matter Plate-é.

Az idejük, a Dark Matterük és az összegek a [Hajódizájnok](/wiki/03-Mechanics/Ship-Designs.md#the-technologies) oldalon vannak.

## Az összes technológia {#all-the-technologies}

<!-- research-technologies:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Technológia | Előbb kell hozzá | Osztály | Kutatási idő | Tudomány | Dark Matter |
| :--- | :--- | :--- | ---: | ---: | ---: |
| [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 perc | 1 800 | – |
| [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 óra | 10 800 | – |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 óra | 36 000 | 10 |
| [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 perc | 1 800 | – |
| [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 óra | 10 800 | – |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 óra | 36 000 | 10 |
| [Engine III](/wiki/06-Items/Propulsion.md#engines) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | B | 3 óra | 10 800 | – |
| [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 perc | 1 800 | – |
| [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 óra | 10 800 | – |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10 óra | 36 000 | 10 |
| [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 perc | 1 800 | – |
| [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 óra | 10 800 | – |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10 óra | 36 000 | 10 |
| [Heavy Shield Core](/wiki/06-Items/Shields.md#shield-cores) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | B | 3 óra | 10 800 | – |
| [Quantum Laser III](/wiki/06-Items/Lasers.md#lasers) | – | B | 3 óra | 10 800 | – |
| [Starfire-III](/wiki/06-Items/Lasers.md#lasers) | [Quantum Laser III](/wiki/06-Items/Lasers.md#lasers) | D | 1 nap | 86 400 | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Starfire-III](/wiki/06-Items/Lasers.md#lasers) | D | 1 nap | 86 400 | 10 |
| [Damage Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Damage Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10 óra | 36 000 | 10 |
| [Crit Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Crit Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10 óra | 36 000 | 10 |
| [Laser Damage Booster II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 óra | 10 800 | – |
| [Shield Wall Booster II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 óra | 10 800 | – |
| [Hull Plating Booster II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 óra | 10 800 | – |
| [Master Drone](/wiki/06-Items/Drones.md#available-drones) | – | C | 10 óra | 36 000 | – |
| [Paragon](/wiki/02-Ships/Paragon.md) | – | B | 6 óra | 21 600 | – |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | – | D | 1 nap | 86 400 | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | – | D | 1 nap | 86 400 | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | – | D | 2 nap | 172 800 | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | – | D | 1 nap | 86 400 | 10 |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | B | 3 óra | 10 800 | – |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | D | 1 nap | 86 400 | 10 |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | – | A | 30 perc | 1 800 | – |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | C | 10 óra | 36 000 | – |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | D | 1 nap | 86 400 | 10 |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | – | B | 3 óra | 10 800 | – |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10 óra | 36 000 | – |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | D | 1 nap | 86 400 | 10 |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | – | B | 6 óra | 21 600 | – |
| [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 óra | 36 000 | 5 |
| [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 nap | 86 400 | 13 |
| [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 óra | 36 000 | 5 |
| [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | D | 2 nap | 172 800 | 20 |
| [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 óra | 36 000 | 5 |
| [Ballista Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 nap | 86 400 | 13 |
| [Stiletto Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 2 nap | 172 800 | 20 |
| [Rampart Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 2 nap | 172 800 | 20 |
| [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 nap | 86 400 | 13 |
| [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | C | 10 óra | 36 000 | 5 |
| [Culler Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 nap | 86 400 | 13 |
| [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 nap | 86 400 | 13 |
| [Auger Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 nap | 86 400 | 13 |
| [Cordon Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 nap | 86 400 | 13 |
| [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 óra | 36 000 | 5 |
| [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | D | 1 nap | 86 400 | 13 |
| [Damage Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30 perc | 1 800 | – |
| [Damage Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Damage Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3 óra | 10 800 | – |
| [Crit Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30 perc | 1 800 | – |
| [Crit Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Crit Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3 óra | 10 800 | – |
| [Penetration Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30 perc | 1 800 | – |
| [Penetration Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Penetration Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3 óra | 10 800 | – |
| [Penetration Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Penetration Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10 óra | 36 000 | 10 |
| [Hull Plating II](/wiki/06-Items/Hull-Plating.md#the-three-platings) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | D | 1 nap | 86 400 | 25 |
| [Hull Plating III](/wiki/06-Items/Hull-Plating.md#the-three-platings) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Hull Plating II](/wiki/06-Items/Hull-Plating.md#the-three-platings) | D | 2 nap | 172 800 | 40 |

Az osztályok kutatási idő szerint:

| Osztály | Kutatási idő | Technológiák | Egymás után | Tudomány | Dark Matter |
| :--- | :--- | ---: | ---: | ---: | ---: |
| A | 30 perc | 8 | 4 óra | 14 400 | 0 |
| B | 3 óra–6 óra | 17 | 2 nap 9 óra | 205 200 | 0 |
| C | 10 óra | 15 | 6 nap 6 óra | 540 000 | 95 |
| D | 1 nap–2 nap | 22 | 27 nap | 2 332 800 | 319 |
| Összesen |  | 62 | 35 nap 19 óra | 3 092 400 | 414 |

Egymás után kutatva a teljes fa 35 nap 19 óra alatt készül el. Ha a boost végig be van kapcsolva, 17 nap 21 óra 30 perc alatt, ami 18 boost és 90 000 Thulium; a tudomány ugyanannyi.

<!-- research-technologies:end -->

## A CPU-k {#the-cpus}

Az új CPU-kat is itt kutatod ki, majd a Gyártásban készíted el. Ugyanez a táblázat és ugyanezek a megjegyzések az [Extrák](/wiki/06-Items/Extras.md#research-cpus) oldalon is megvannak.

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | Kutatási idő | Előbb kell hozzá | Thulium a gyártáshoz | Gyártási idő |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 perc | – | 12 000 | 5 perc |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10 óra | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 000 | 10 perc |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1 nap | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75 000 | 15 perc |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3 óra | – | 8 000 | 5 perc |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10 óra | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | 20 000 | 10 perc |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1 nap | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40 000 | 15 perc |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6 óra | – | 15 000 | 10 perc |

Egyik sem kapható a Boltban: kutasd ki a technológiát, majd készítsd el a CPU-t a Gyártásban. Vidd az egeret egy CPU fölé a fáján, hogy lásd, mit kér érte a Gyártás.

### Extra Slots CPUs

- **Mit tudnak.** Az Extra Slots CPU I, II és III minden hajónak 3, 5 és 7 további extrafoglalatot ad, vagyis összesen 6, 8 és 10 foglalatot egy olyan hajón, amelynek eleve 3 van, és 5, 7 és 9 foglalatot egy olyan hajón, amelynek eleve 2 van. A magasabb CPU lecseréli az előzőt: a II nem adódik hozzá az I-hez.
- **Telepítve, nem hordva.** Az Extra Slots CPU nem tárgy: ha a Gyártásban átveszed, magától települ a Skylabodba, minden hajóra mindkét konfigurációban, és nem foglal el foglalatot. A wipe után is megmarad.
- **Sorrendben.** Egymás után gyárts: a II csak akkor, ha az I telepítve van, a III csak akkor, ha a II telepítve van; addig a Gyártás megmondja, melyiket telepítsd előbb. A három együtt 117 000 Thuliumba kerül: 12 000, 30 000 és 75 000.

### Jump CPU

- **Mit tud.** A hajódat a világod bármelyik vállalati szektorába ugrasztja, a saját vállalatodéba és a többiekébe is, a bázisszektorokat is beleértve (`M`, `T` és `G`, 1–4. szektor), ugrásonként **500 Thuliumért**. A használatok száma nem korlátozott: csak a Thuliumot fizeted. Veszélyes szektorba (`DS`) és semleges szektorba (`N`) sosem visz.
- **Az ugrás.** Nyomd meg a JMP helyet, válaszd ki a szektort a Csillagrendszer térképén, és erősítsd meg: a hajó 5 másodpercig töltődik, majd megérkezik a szektor egyik kapujához, védve, mint bármelyik kapuugrás után. Érkezés után a CPU 30 másodpercig hűl.
- **Nem harcban.** Nem indítható lövés vagy találat után 10 másodpercen belül, és a töltés közbeni lövés vagy találat megszakítja az ugrást; ilyenkor nem kell fizetni. Álcázva nem ugorhatsz.
- **Semleges szektorból nem:** a semleges szektorban lévő vagy vállalat nélküli pilóta nem használhatja.
- Veszélyes szektorból elhagyható, ha nem vagy harcban.

### Base CPUs

- **Mit tudnak.** A hajódat a vállalatod bázisára teleportálják, az állomás körüli biztonságos zónába (`M-1`, `T-1` vagy `G-1`, a Mission Control szektora), Thulium nélkül. A gyorssáv BSE helyéről indítod őket.
- **Nem harcban.** 10 másodperces töltés, mindkettőnél ugyanaz. Nem indítható lövés vagy találat után 10 másodpercen belül, álcázva vagy ha már a bázisod biztonságos zónájában vagy, és a töltés közbeni lövés vagy találat megszakítja.

| CPU | Használat | Hűlési idő |
| :--- | ---: | ---: |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 10 | 10 perc |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 25 | 5 perc |

- **Elfogy, nem töltődik újra.** Minden használat elvesz egyet a CPU használataiból, és a használat nélkül maradt CPU eltűnik: készíts újat. Ha mindkettő fel van szerelve, előbb a jobbik (II) fogy.

### Auto-Repair CPU

- **Mit tud.** Magától kiküldi az extrafoglalataidban lévő Repair Dronet, valahányszor kézzel is kiküldhetted volna: a hajótested nincs tele, a drón nincs kint, és az utolsó találat óta eltelt 10 másodperc. Nincs beállítandó hajótest-szint.
- Saját extrafoglalatot foglal el, és nem csinál semmit Repair Drone nélkül ugyanannak a konfigurációnak egy extrafoglalatában. Képességfoglalatban lévő Repair Dronet sosem küld ki (az az Emergency Repair gomb).
- **Ha kézzel megállítod a drónt,** a CPU nem nyúl hozzá, amíg a hajótested újra tele nem lesz, vagy amíg te magad ki nem küldöd a drónt.


<!-- research-cpus:end -->
