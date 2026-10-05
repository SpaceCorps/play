<!-- wiki-i18n source: 3d97a6f4bd324d8d -->
<!-- wiki-i18n title: Lézerek -->
# Lézerek és lőszer {#lasers-ammo}

A fegyverek a SpaceCorps elsődleges eszközei a sebzés okozására.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Tárgyfa {#item-tree}

Amit a Gyártás elkészít, ahhoz előbb a technológiája kell; vidd az egeret egy tárgy fölé, hogy lásd, mennyi ideig tart a kutatása. A technológiafa, az üzemanyag és a boost: [Kutatás](/wiki/03-Mechanics/Research.md).

```tree
Quantum Laser 1 | laser, shoddy | buy 8000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser 2 | laser, common | buy 80000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser 3 | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-3 | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser 3, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-3, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp 1 | laser-amp, shoddy | buy 10000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp 1 | laser-amp, shoddy | buy 15000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Arc Amp | laser-amp, uncommon | buy 60000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Focus Amp | laser-amp, uncommon | buy 60000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Pulse Amp | laser-amp, rare | buy 1500 Thulium | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Prism Amp | laser-amp, rare | buy 1500 Thulium | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Nova Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Pulse Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Apex Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Prism Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Standard Battery | ammo, common | buy 10 Credits | /wiki/06-Items/Lasers.md#laser-ammunition
Siphon Battery | ammo, rare | buy 0.25 Thulium | /wiki/06-Items/Lasers.md#siphon-battery
Advanced Plasma | ammo, rare | buy 0.5 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Ultra Core | ammo, rare | buy 1 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Experimental Fusion Core | ammo, epic | buy 2.2 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition

Quantum Laser 1 -> Quantum Laser 2 -> Quantum Laser 3 => Starfire-3 => Helios Beam
Damage Amp 1 -> Arc Amp -> Pulse Amp => Nova Amp
Crit Amp 1 -> Focus Amp -> Prism Amp => Apex Amp
Standard Battery -> Advanced Plasma -> Ultra Core -> Experimental Fusion Core
```
<!-- item-tree:end -->

## Lézerek {#lasers}

Szerelj lézereket közvetlenül a hajó lézerfoglalataiba vagy drónokba, hogy növeld a támadóerődet.

| Név | Ritkaság | Alapsebzés | Kritikus esély | Hatótáv | Erősítőfoglalatok | Ár |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Quantum Laser 1** | Silány | 55 | – | 600 | 1 | 8 000 kredit |
| **Quantum Laser 2** | Gyakori | 65 | – | 700 | 2 | 80 000 kredit |
| **Quantum Laser 3** | Ritka | 80 | 10% | 800 | 3 | Csak gyártható |
| **Starfire-3** | Mitikus | 135 | 15% | 850 | 3 | Csak gyártható |
| **Helios Beam** | Mitikus | 185 | 25% | 900 | 3 | Csak gyártható |

A Hatótáv oszlop az egyes lézerek saját értéke. **A hajód a lézerei hatótávjának átlagával tüzel** (a drónokban lévő lézerek is számítanak), a legközelebbi egységre kerekítve, és minden lézer akkor tüzel, amint a célpont ezen a távolságon belülre kerül. Egy Starfire-3 két Quantum Laser 2 mellett 750-es hajóhatótávot ad, nem 850-et; három Starfire-3 megtartja a 850-et, az egyforma lézerek pedig semmin sem változtatnak. Egy Kovácsműhely-hatótávbónusz a saját lézerén számít, mielőtt az átlagot kiszámolják. Lézer nélkül a hangár nem mutat hatótávot (egy gondolatjelet), és a lézerek nem tudnak tüzelni, de a rakétáid igen, mindegyik a saját hatótávjával (lásd: [Rakéták](/wiki/06-Items/Rockets.md)). A hangárban a csempe „Átl. hatótáv” feliratot kap, ha a lézereid eltérnek, és ha fölé viszed az egeret, felsorolja az egyes lézerek hatótávját.

A Quantum Laser 1-nek és a Quantum Laser 2-nek nincs saját kritikus esélye („–”): a foglalataikba tett Damage Amp vagy Crit Amp adja meg. A kritikus találatok más színnel jelennek meg a lebegő sebzésszámokban (jégkék, nagyobb, „!” jellel).

### A legfelső három lézer elkészítése {#making-the-top-three-lasers}

A **Quantum Laser 3**, a **Starfire-3** és a **Helios Beam** csak a **Gyártásban** készül. A Quantum Laser 3-at már nem árulják a Boltban; aki már birtokol egyet, megtartja. Mindegyik recept a [Skylab](/wiki/03-Mechanics/Skylab.md) kovácsműhelyéből származó lemezeket kér:

| Lézer | Gyártási idő | Ez kell hozzá |
| :--- | :---: | :--- |
| Quantum Laser 3 | 1 perc | 10 Ship Fragment, 2 Velkonite Reinforced Plate, 1 500 Thulium |
| Starfire-3 | 1 perc | 1 Quantum Laser 3, 15 Ship Fragment, 8 Velkonite Reinforced Plate, 1 Reinforced Hull Plate, 1 500 Thulium, 100 000 kredit |
| Helios Beam | 3 perc | 1 Starfire-3, 50 Cataclysite, 2 Power Core, 18 Orvium Reinforced Plate, 4 Reinforced Hull Plate, 2 000 Thulium |

A Gyártás oldal megmutatja, mid van meg ahhoz képest, amit egy recept kér, az Elkészítés gomb pedig megmondja, mi hiányzik. Ha egy recept képére vagy nevére, esetleg valamelyik alapanyagára mutatsz, megjelenik a tárgy teljes leírása és az értékei.

**A Starfire-3 egy Quantum Laser 3-ból készül.** Előbb elkészíted a Quantum Laser 3-at, a Starfire-3 pedig elhasználja. Amit a Quantum Laser 3 már elvett, azt nem kéri újra, így a kettő együtt pontosan azt kéri, amit egy Starfire-3 önmagában kért: 3 000 Thuliumot, 100 000 kreditet, 25 Ship Fragmentet, 10 Velkonite Reinforced Plate-et, 1 Reinforced Hull Plate-et és 2 percet. Ha már van Quantum Laser 3-ad, csak a Starfire-3 saját részét fizeted. A szabályok a Helios Beaméi, lent: a Starfire-3 megtartja az elhasznált Quantum Laser 3 bűvölési fokozatát (egy Isteni Quantum Laser 3-ból Isteni Starfire-3 lesz), a bónuszai pedig újra kisorsolódnak; te döntöd el, melyik Quantum Laser 3 megy el, a kártya megkérdezi, mielőtt a Normálnál magasabbat használna fel, és a Quantum Laser 3-nak szabadnak kell lennie: **előbb vedd le a hajódról** (az erősítői visszakerülnek a leltárba), és vedd ki a tranzittárolóból is. Ha a hajón van, az Elkészítés gomb ezt írja: „Előbb vedd le: Quantum Laser 3”.

**A Helios Beam egy Starfire-3-ból készül.** Előbb elkészíted a Starfire-3-at (3 000 Thulium és 100 000 kredit a hozzá tartozó Quantum Laser 3-mal együtt), a Helios Beam pedig elhasználja, ahogyan a [Master Drone](/wiki/06-Items/Drones.md) elhasznál egy Slave Drone-t. Amit a Starfire-3 már elvett, azt nem kéri újra, így a kettő együtt azt kéri, amit a Helios Beam önmagában kért: az 5 000 Thuliumot, a Cataclysite-ot, a Power Core-okat és a Reinforced Hull Plate-eket, valamint 18 Orvium lemezt 20 helyett (a Starfire-3 tíz Velkonite lemeze pótolja a hiányzó kettőt); ezenkívül a Starfire-3-hoz tartozó 100 000 kreditet és 25 Ship Fragmentet fizeted. A szabály ugyanaz, mint a [modulfejlesztéseknél](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly): a Helios Beam megtartja az elhasznált Starfire-3 bűvölési fokozatát (egy Isteni Starfire-3-ból Isteni Helios Beam lesz), a bónuszai pedig újra kisorsolódnak; te döntöd el, melyik Starfire-3 megy el, ha több is van nálad, és a kártya megkérdezi, mielőtt a Normálnál magasabbat használna fel. A Starfire-3-nak szabadnak kell lennie: **előbb vedd le a hajódról** (a belé szerelt erősítők visszakerülnek a leltárba), és vedd ki a tranzittárolóból is. Ha a hajón van, az Elkészítés gomb ezt írja: „Előbb vedd le: Starfire-3”.

Honnan jönnek a lemezek:

- A **Velkonite Reinforced Plate**-eket (Quantum Laser 3 és Starfire-3) Velkonite-ércből kovácsolják, a kovácsműhely 1. szintjén lemezenként 40 érc. Az **Orvium Reinforced Plate**-eket (Helios Beam) Orvium-ércből kovácsolják, lemezenként 80 érc.
- Az ércet csak a Skylabod gyűjtői adják. Egy 5. szintű Velkonite-gyűjtő óránként 18 Velkonite-ot bányászik, így egy Quantum Laser 3 lemezei körülbelül 4 óra bányászatba kerülnek, egy Starfire-3 tíz lemeze (kettő a hozzá szükséges Quantum Laser 3-ban, nyolc a saját lépésében) körülbelül 22-be. A Helios Beam a hosszú: a 18 lemezéhez 1 440 Orvium kell, ami egy 5. szintű Orvium-gyűjtőtől körülbelül 4 nap.
- Az erőforrás-raktár az 1. szinten ércenként 240-et tárol: 6 Velkonite-lemezt vagy 3 Orvium-lemezt a Kovácsműhely 1. szintjén. Ezért menet közben kovácsolj (a Kovácsműhely adagja az 1. szinten legfeljebb 10 lemez), vagy fejleszd a raktárat.
- A kovácsolt lemezek a kovácsműhelyben várnak, amíg leszállt hajóval be nem gyűjtöd őket, és közönséges tárgyakként a leltáradba kerülnek.

A Ship Fragmenteket, a Cataclysite-ot, a Power Core-okat és a Reinforced Hull Plate-eket az idegenek dobják; minden nyersanyag minden forrását és felhasználását az [Erőforrások](/wiki/06-Items/Resources.md) oldal tartalmazza; hogy mennyit, azt a [Bulwark](/wiki/04-Aliens/Bulwark.md) és a [Goombah](/wiki/04-Aliens/Goombah.md) oldalának zsákmánylistái mutatják.

---

## Lézererősítők (Amp-ek) {#laser-amplifiers-amps-}

Ezeket közvetlenül a lézer foglalatába szereld, hogy növeld a jellemzőit. Két vonal van, mindegyikben négy lépcsőfok: a **sebzésvonal** fix mennyiségű sebzést ad, a **kritikus vonal** pedig kritikus esélyt és fix kritikus sebzést.

| Név | Ritkaság | Alapsebzés-növelés | Kritikus esély növelése | Fix kritikus sebzés | Ár |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Damage Amp 1** | Silány | +10 | +5% | +5 | 10 000 kredit |
| **Arc Amp** | Szokatlan | +16 | +5% | +8 | 60 000 kredit |
| **Pulse Amp** | Ritka | +26 | +6% | +13 | 1 500 Thulium |
| **Nova Amp** | Epikus | +38 | +7% | +20 | Csak gyártható |
| **Crit Amp 1** | Silány | +0 | +15% | +0 | 15 000 kredit |
| **Focus Amp** | Szokatlan | +0 | +20% | +14 | 60 000 kredit |
| **Prism Amp** | Ritka | +0 | +25% | +24 | 1 500 Thulium |
| **Apex Amp** | Epikus | +0 | +25% | +44 | Csak gyártható |

A Nova Amp és az Apex Amp a [Gyártásban](/wiki/06-Items/Overview.md#upgrading-modules) készül egy Pulse Ampből, illetve egy Prism Ampből, Thuliumból, zsákmányból és a Skylabodból származó 3-3 Velkonite Reinforced Plate felhasználásával. Megtartják az elhasznált erősítő bűvölési fokozatát, a bónuszaik pedig újra kisorsolódnak ([Modulfejlesztések a Gyártásban](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)).

### Melyik erősítő hova való {#which-amp-goes-where}

A sebzéserősítő bármelyik lézerhez ugyanannyi sebzést ad, ezért a **Quantum lézereken** ér a legtöbbet. A kritikus erősítő megsokszorozza azt, amit a lézer már tud, ezért annál többet ér, minél erősebben üt a lézer: a **Starfire-3**-on egyenlő a sebzésvonallal, a **Helios Beamen** pedig körülbelül 3,5%-kal előzi meg azt. A lézer kritikus esélye 100%-nál megáll: három Prism Amp vagy Apex Amp pontosan ennyire viszi a Helios Beamet.

Ugyanazzal az erősítővel feltöltve egy lézer mindig erősebb, mint az alatta lévő, így egy jobb erősítő sosem pótol egy jobb lézert: egy Quantum Laser 3 három Nova Amppal kevesebbet sebez, mint egy Helios Beam három Damage Amp 1-gyel (azonos bűvölési fokozatú darabokkal: egy Isteni vagy jobb fokozatra kovácsolt Quantum Laser 3 és Nova Ampek a legjobb kisorsolt bónuszokkal megelőzhetnek egy sima, Damage Amp 1-es Helios Beamet, Isteninél egy hajszállal).

---

## Lézerlőszer {#laser-ammunition}

Elhasználódó elemek, amelyek megsokszorozzák a lézersortüzeid sebzését:

| Név | Ritkaság | Sebzésszorzó | Pajzsáthatolás | Ár darabonként |
| :--- | :--- | :---: | :---: | :--- |
| **Standard Battery** | Gyakori | x1,0 | – | 10 kredit |
| **Advanced Plasma** | Ritka | x2,0 | – | 0,5 Thulium |
| **Ultra Core** | Ritka | x3,0 | 5% | 1,0 Thulium |
| **Experimental Fusion Core** | Epikus | x4,0 | 10% | 2,2 Thulium |
| **Siphon Battery** | Ritka | x1,0, csak pajzsra | – | 0,25 Thulium |

A **pajzsáthatolást** a sortüzeid minden találatánál levonják a célpont elnyeléséből: a pajzsok a célpont elnyelésének és az áthatolásnak a különbségét fogják fel (lásd: [Pajzsmechanika](/wiki/03-Mechanics/Shields.md#shield-penetration)). Egy 80%-os hajóval szemben (a legjobb pajzs a legjobb cellákkal) az x4 lőszer 10%-os áthatolása mellett a pajzsok a találat 70%-át fogják fel, a hajótest 30%-át kapja. A legtöbbet azoknál a hajóknál számít, amelyeknek kicsi a hajótestük a pajzsukhoz képest; egy nagyon nagy, 80%-os hajó így is, úgy is ugyanannyit bír ki. Az idegeneknek nincs említésre méltó elnyelés-értékük (a pajzsuk a találat 80%-át fogja fel), és az áthatolás ebből is levonódik.

### Siphon Battery

A Siphon Battery pajzslopásra való lőszer, a hajótestek összetörése helyett. **x1 sebzést okoz közvetlenül a célpont pajzsán**, és ugyanennyit ad hozzá a **saját pajzsodhoz**, a maximumodig. A gyorssáv lőszermenüjében választhatod ki, mint bármelyik másik lőszert (ez a kékeszöld örvényes csempe). Nem lő sugarat: egy vékony, halvány kékeszöld szonda indul a célpont felé, a célpont pajzsa kékeszöldben felvillan, ahol az becsapódik, a kiszívott pajzs pedig láthatóan visszaáramlik a hajódra izzó kékeszöld csomagokként (három–tíz, nagyobb szívásnál több), egymás után, körülbelül fél másodperc alatt. Minden megérkező csomag megpulzáltatja a pajzsodat. Ugyanezt látod minden látótérben lévő Siphon Battery esetében is, akárkit szív le: idegeneket, más pilótákat és vállalati pilóták hajóit.

- **Csak pajzs**: a hajótestet sosem éri, a célpont elnyelése nem osztja meg a sebzést, és a Siphon Battery sosem tud semmit megsemmisíteni. A sebzését az korlátozza, amennyit a célpont pajzsa még tart.
- **Nincs mit elvenni**: ha a célpontnak már nincs pajzsa, nem szív le semmit, és nem ad semmit. A sortűz így is elfogy, lézerenként egy elem, mint minden lőszernél. Csak a szondát látod és egy tompa villódzást a hajótesten, csomagokat nem.
- **Nyereség**: a pajzsod sosem megy a maximuma fölé, és a pajzs felvétele nem késlelteti a saját pajzsregenerációdat.
- Az **idegeneknek és a pilótáknak** egyaránt van lecsapolható pajzsuk. Az a szívás, amely egy idegentől vesz el pajzsot, találatnak számít az [első találat szerinti foglalásnál](/wiki/03-Mechanics/Combat.md); amelyik nem talál pajzsot, az nem. A Seekert vagy a Goombah-ot is felébreszti, amelyek csak visszavágnak, ahogy bármelyik másik találat.
- A **kritikus találatok** számítanak: egy kritikus sortűz másfélszer annyit szív le, és a száma kritikus találatként jelenik meg. A csomagjai nagyobbak és fényesebbek, a célpont pajzsa pedig erősebben felvillan.
- A [vállalati pilóták](/wiki/03-Mechanics/Company-Pilots.md) szabványos x1 lőszerrel tüzelnek.
