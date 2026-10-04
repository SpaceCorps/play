<!-- wiki-i18n source: 55131889617bd886 -->
<!-- wiki-i18n title: Kutatás -->
# Kutatás {#research}

A **Kutatóközpont** a [Skylabod](/wiki/03-Mechanics/Skylab.md) laboratóriuma. Nyersanyagokkal táplálod, ő **tudománnyá** alakítja őket, a tudomány pedig **technológiákat** kutat. A [Gyártás](/wiki/06-Items/Overview.md#upgrading-modules) minden elkészítéséhez előbb a technológiája kell: hajót, lézert, fúvókát vagy CPU-t addig nem lehet legyártani, amíg ki nem kutatták.

Ez az oldal tartalmazza a teljes technológiafát az egyes technológiák idejével, azt, hogy az egyes nyersanyagok mennyi tudományt adnak, a Thulium-boostot, a Dark Matter szabályát és az új CPU-kat. A számokat a játék saját adataiból olvassuk, ezért mindig azok szerepelnek itt, amelyek a játékban.

## A Kutatóközpont {#the-research-centre}

<!-- research-centre:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **A Mag 10. szintjétől.** A Kutatóközpont a [Skylabod](/wiki/03-Mechanics/Skylab.md) egy modulja, a többihez hasonlóan építed: 25 Ship Fragment a leltáradból (leszállt hajóval), 25 000 kredit és 500 Thulium. A képernyője a Skylab-oldal **Kutatás** nézete.
- **1–10. szint.** A magasabb szint nagyobb tartályt ad, és több energiát fogyaszt. A kutatást nem teszi gyorsabbá: egy technológia minden szinten ugyanannyi ideig tart.
- **A tartály.** A Kutatóközpont a tudományát egy tartályban tartja, amely az 1. szinten 12 óra kutatásnyit tárol, és minden szinttel 25%-kal többet (lásd a lenti táblázatot).
- **Az üzemanyagból tudomány lesz.** A betáplált nyersanyag azonnal tudománnyá válik, ahogy az üzemanyag-táblázat mutatja. Egy kutatás a kutatási idejének minden másodpercében 1 tudományt éget el; üres tartálynál várakozik, és folytatódik, amint újra táplálod a Kutatóközpontot.
- **Ingyenes első óra.** Az új Kutatóközpont 3 600 tudománnyal indul a tartályában, ami 1 óra kutatás.
- **Egyszerre egy.** A Kutatóközpont egyszerre csak egy technológiát kutat. Nincs sor.
- **Amíg távol vagy.** A kutatás a szerver órája szerint fut, ezért kijelentkezés után is megy tovább, amíg el nem készül vagy ki nem ürül a tartály. Az energiahiány vagy a Kutatóközpont fejlesztése nem állítja meg.
- **Energia.** A Kutatóközpont az 1. szinten 25 energiát fogyaszt, és minden szinttel 15%-kal többet, és nem kapcsolható ki.
- **A wipe mindent megtart:** a technológiáidat, a tartály tudományát, a belehelyezett Dark Mattert, a folyamatban lévő kutatást és a boostot.
- **Ami a tiéd, az a tiéd marad.** Amikor a kutatás megjelent a játékban, minden pilóta megkapta minden már birtokolt tárgyának technológiáját, és azokat a technológiákat, amelyekre ezeknek szükségük volt. Az a tárgy, amely később jut hozzád (ajándék, kód, jutalom), nem nyitja meg a technológiáját.
- **A Mag 10. szintje alatt** nem kutathatsz, így a Gyártásban még semmi újat nem készíthetsz el. Az állomásküldetések végigvezetnek a Mag szintjein.

<!-- research-centre:end -->

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

A Kutatóközpontot nyersanyagokkal táplálod, és minden egység azonnal tudománnyá válik. Minél több munkába kerül egy egység megszerzése, annál több tudományt ad: az értékek azt követik, mennyire nehéz megszerezni, nem a ritkasági címkét, ezért egy Power Core (Szokatlan) többet ad, mint egy Orvium (Ritka). Az ércek a [Skylabod](/wiki/03-Mechanics/Skylab.md#resource-storage) Erőforrás-raktárából jönnek; minden más nyersanyag a leltáradból, és a hajódnak leszállva kell lennie. Nem égethető el: Velkonite Reinforced Plate, Orvium Reinforced Plate, Dark Matter Plate, Dark Matter, kredit és Thulium; a Reinforced Hull Plate igen.

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
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | Szokatlan | Erőforrás-raktár | 40 | 90 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | Ritka | Erőforrás-raktár | 80 | 45 |
| [Power Core](/wiki/06-Items/Resources.md#power-core) | Szokatlan | A leltárad | 100 | 36 |
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

## Dark Matter {#dark-matter}

A fa csúcsán lévő technológiákhoz Dark Matter is kell. A [feketelyukból](/wiki/03-Mechanics/Black-Hole.md#dark-matter) származik, ahol egy N.I.K.E. rakéta, amely eléri, hagy valamennyit, és időnként a [Dormant-raj](/wiki/05-Swarms/Dormant-Swarm.md) egy Dormant Pulse-ától.

<!-- research-dark-matter:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **10 Dark Matter** az alábbi táblázat 15 technológiájának mindegyikéhez, a tudományon felül: a kutatás indulása előtt helyezd be a Kutatóközpontba (a leltáradból, leszállt hajóval), és a kutatás induláskor elveszi.
- **A szabály:** egy Epikus vagy magasabb ritkaságú tárgy, amelynek kutatása 10 óra vagy tovább tart. Az N.I.K.E.-nek, amely a Dark Matter forrása, soha nincs rá szüksége.
- **Ha megszakítasz egy kutatást,** a hozzá belehelyezett Dark Matter visszakerül a Kutatóközpontba. A haladás és az addig elégetett tudomány nem.
- Együtt 150 Dark Mattert kérnek.

| Technológia | Ritkaság | Kutatási idő | Dark Matter |
| :--- | :--- | :--- | ---: |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | Epikus | 10 óra | 10 |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | Epikus | 10 óra | 10 |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | Epikus | 10 óra | 10 |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | Epikus | 10 óra | 10 |
| [Starfire-3](/wiki/06-Items/Lasers.md#lasers) | Mitikus | 1 nap | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | Mitikus | 1 nap | 10 |
| [Nova Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Epikus | 10 óra | 10 |
| [Apex Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Epikus | 10 óra | 10 |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | Epikus | 1 nap | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | Epikus | 1 nap | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | Mitikus | 2 nap | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | Mitikus | 1 nap | 10 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | Legendás | 1 nap | 10 |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | Epikus | 1 nap | 10 |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | Epikus | 1 nap | 10 |

<!-- research-dark-matter:end -->

## A technológiafa {#the-technology-tree}

Minden doboz egy technológia: az a tárgy, amelynek legyártását lehetővé teszi, a neve alatt a kutatási idővel (az óra), és ahol Dark Matter kell, a Dark Matter-jelvénnyel. A nyíl az egyik technológiától arra vezet, amelynek szüksége van rá, és amelyet előbb kutatsz ki; nyíl nélküli doboz azonnal kikutatható. Vidd az egeret egy doboz fölé, hogy lásd a kutatási időt, az elégetett tudományt és azt, amit a Gyártás utána kér a tárgyért, és kattints rá a tárgy oldalának megnyitásához. A fákat a játék saját adataiból rajzoljuk.

<!-- research-tree:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

### Hajtás és sebesség {#tree-propulsion}

```tree research
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines

Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```

### Pajzsok és védelem {#tree-shields}

```tree research
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cores

Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```

### Lézerek és lőszer {#tree-lasers}

```tree research
Quantum Laser 3 | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-3 | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser 3, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-3, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Nova Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Pulse Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Apex Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Prism Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-

Quantum Laser 3 => Starfire-3 => Helios Beam
```

### Boosterek {#tree-boosters}

```tree research
Damage Amp II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
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
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 20 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 8 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu

Extra Slots CPU I => Extra Slots CPU II => Extra Slots CPU III
Base CPU I => Base CPU II => Jump CPU
```


<!-- research-tree:end -->

## Az összes technológia {#all-the-technologies}

<!-- research-technologies:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Technológia | Előbb kell hozzá | Osztály | Kutatási idő | Tudomány | Dark Matter |
| :--- | :--- | :--- | ---: | ---: | ---: |
| [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 perc | 1 800 | – |
| [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 óra | 10 800 | – |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 óra | 36 000 | 10 |
| [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 perc | 1 800 | – |
| [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 óra | 10 800 | – |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 óra | 36 000 | 10 |
| [Engine III](/wiki/06-Items/Propulsion.md#engines) | – | B | 3 óra | 10 800 | – |
| [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 perc | 1 800 | – |
| [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 óra | 10 800 | – |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | C | 10 óra | 36 000 | 10 |
| [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 perc | 1 800 | – |
| [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 óra | 10 800 | – |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | C | 10 óra | 36 000 | 10 |
| [Heavy Shield Core](/wiki/06-Items/Shields.md#shield-cores) | – | B | 3 óra | 10 800 | – |
| [Quantum Laser 3](/wiki/06-Items/Lasers.md#lasers) | – | B | 3 óra | 10 800 | – |
| [Starfire-3](/wiki/06-Items/Lasers.md#lasers) | [Quantum Laser 3](/wiki/06-Items/Lasers.md#lasers) | D | 1 nap | 86 400 | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | [Starfire-3](/wiki/06-Items/Lasers.md#lasers) | D | 1 nap | 86 400 | 10 |
| [Nova Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | C | 10 óra | 36 000 | 10 |
| [Apex Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | C | 10 óra | 36 000 | 10 |
| [Damage Amp II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 óra | 10 800 | – |
| [Shield Wall II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 óra | 10 800 | – |
| [Hull Plating II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 óra | 10 800 | – |
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
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | D | 1 nap | 86 400 | 10 |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | – | B | 3 óra | 10 800 | – |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | C | 10 óra | 36 000 | – |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | D | 1 nap | 86 400 | 10 |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | – | B | 6 óra | 21 600 | – |

Az osztályok kutatási idő szerint:

| Osztály | Kutatási idő | Technológiák | Egymás után | Tudomány | Dark Matter |
| :--- | :--- | ---: | ---: | ---: | ---: |
| A | 30 perc | 5 | 2 óra 30 perc | 9 000 | 0 |
| B | 3 óra–6 óra | 14 | 2 nap | 172 800 | 0 |
| C | 10 óra | 9 | 3 nap 18 óra | 324 000 | 60 |
| D | 1 nap–2 nap | 9 | 10 nap | 864 000 | 90 |
| Összesen |  | 37 | 15 nap 20 óra 30 perc | 1 369 800 | 150 |

Egymás után kutatva a teljes fa 15 nap 20 óra 30 perc alatt készül el. Ha a boost végig be van kapcsolva, 7 nap 22 óra 15 perc alatt, ami 8 boost és 40 000 Thulium; a tudomány ugyanannyi.

<!-- research-technologies:end -->

## A CPU-k {#the-cpus}

Az új CPU-kat is itt kutatod ki, majd a Gyártásban készíted el. Ugyanez a táblázat és ugyanezek a megjegyzések az [Extrák](/wiki/06-Items/Extras.md#research-cpus) oldalon is megvannak.

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | Kutatási idő | Előbb kell hozzá | Thulium a gyártáshoz | Gyártási idő |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 perc | – | 12 000 | 5 perc |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10 óra | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 000 | 10 perc |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1 nap | [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75 000 | 15 perc |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3 óra | – | 8 000 | 5 perc |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10 óra | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 20 000 | 10 perc |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1 nap | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40 000 | 15 perc |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6 óra | – | 15 000 | 10 perc |

Egyik sem kapható a Boltban: kutasd ki a technológiát, majd készítsd el a CPU-t a Gyártásban. Vidd az egeret egy CPU fölé a fáján, hogy lásd, mit kér érte a Gyártás.

### Extra Slots CPUs {#extra-slots-cpus}

- **Mit tudnak.** Az Extra Slots CPU I, II és III minden hajónak 3, 5 és 7 további extrafoglalatot ad, vagyis összesen 6, 8 és 10 foglalatot az eleve meglévő 3 mellé. A magasabb CPU lecseréli az előzőt: a II nem adódik hozzá az I-hez.
- **Telepítve, nem hordva.** Az Extra Slots CPU nem tárgy: ha a Gyártásban átveszed, magától települ a Skylabodba, minden hajóra mindkét konfigurációban, és nem foglal el foglalatot. A wipe után is megmarad.
- **Sorrendben.** Egymás után gyárts: a II csak akkor, ha az I telepítve van, a III csak akkor, ha a II telepítve van; addig a Gyártás megmondja, melyiket telepítsd előbb. A három együtt 117 000 Thuliumba kerül: 12 000, 30 000 és 75 000.

### Jump CPU {#jump-cpu}

- **Mit tud.** A hajódat a világod bármelyik vállalati szektorába ugrasztja, a saját vállalatodéba és a többiekébe is, a bázisszektorokat is beleértve (`M`, `T` és `G`, 1–4. szektor), ugrásonként **500 Thuliumért**. A használatok száma nem korlátozott: csak a Thuliumot fizeted. Veszélyes szektorba (`DS`) és semleges szektorba (`N`) sosem visz.
- **Az ugrás.** Nyomd meg a JMP helyet, válaszd ki a szektort a Csillagrendszer térképén, és erősítsd meg: a hajó 5 másodpercig töltődik, majd megérkezik a szektor egyik kapujához, védve, mint bármelyik kapuugrás után. Érkezés után a CPU 30 másodpercig hűl.
- **Nem harcban.** Nem indítható lövés vagy találat után 10 másodpercen belül, és a töltés közbeni lövés vagy találat megszakítja az ugrást; ilyenkor nem kell fizetni. Álcázva nem ugorhatsz.
- **Semleges szektorból nem:** a semleges szektorban lévő vagy vállalat nélküli pilóta nem használhatja.
- Veszélyes szektorból elhagyható, ha nem vagy harcban.

### Base CPUs {#base-cpus}

- **Mit tudnak.** A hajódat a vállalatod bázisára teleportálják, az állomás körüli biztonságos zónába (`M-1`, `T-1` vagy `G-1`, a Mission Control szektora), Thulium nélkül. A gyorssáv BSE helyéről indítod őket.
- **Nem harcban.** 10 másodperces töltés, mindkettőnél ugyanaz. Nem indítható lövés vagy találat után 10 másodpercen belül, álcázva vagy ha már a bázisod biztonságos zónájában vagy, és a töltés közbeni lövés vagy találat megszakítja.

| CPU | Használat | Hűlési idő |
| :--- | ---: | ---: |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 10 | 10 perc |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 25 | 5 perc |

- **Elfogy, nem töltődik újra.** Minden használat elvesz egyet a CPU használataiból, és a használat nélkül maradt CPU eltűnik: készíts újat. Ha mindkettő fel van szerelve, előbb a jobbik (II) fogy.

### Auto-Repair CPU {#auto-repair-cpu}

- **Mit tud.** Magától kiküldi az extrafoglalataidban lévő Repair Dronet, valahányszor kézzel is kiküldhetted volna: a hajótested nincs tele, a drón nincs kint, és az utolsó találat óta eltelt 10 másodperc. Nincs beállítandó hajótest-szint.
- Saját extrafoglalatot foglal el, és nem csinál semmit Repair Drone nélkül ugyanannak a konfigurációnak egy extrafoglalatában. Képességfoglalatban lévő Repair Dronet sosem küld ki (az az Emergency Repair gomb).
- **Ha kézzel megállítod a drónt,** a CPU nem nyúl hozzá, amíg a hajótested újra tele nem lesz, vagy amíg te magad ki nem küldöd a drónt.


<!-- research-cpus:end -->
