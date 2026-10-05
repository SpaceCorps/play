<!-- wiki-i18n source: 969bfa836749a15e -->
<!-- wiki-i18n title: Hajtás -->
# Hajtás és sebesség {#propulsion-speed}

A hajtásrendszerek határozzák meg a hajód mozgási sebességét és manőverezőképességét.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Tárgyfa {#item-tree}

Amit a Gyártás elkészít, ahhoz előbb a technológiája kell; vidd az egeret egy tárgy fölé, hogy lásd, mennyi ideig tart a kutatása. A technológiafa, az üzemanyag és a boost: [Kutatás](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | buy 2000 Thulium | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I -> Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Hajtóművek {#engines}

A hajtóművek a hajód fő tolóerő-forrásai. A **képességfoglalatba** tett hajtómű ehelyett a Különleges hatás oszlopban szereplő **Afterburner** képességet adja, tíz másodpercnyi sebességlöketet (több hajtóművel hosszabbat), és saját tolóerőt nem ad hozzá (lásd: [Képességek](/wiki/03-Mechanics/Abilities.md)).

| Név | Ritkaság | Alapsebesség | Sebességbónusz % | Pajzsbónusz % | Foglalatok | Különleges hatás | Ár |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Silány | +2 | +2% | -2% | 1 | Afterburner I | 20 000 kredit |
| **Engine II** | Gyakori | +4 | +4% | -8% | 2 | Afterburner II | 2 000 Thulium |
| **Engine III** | Ritka | +6 | +5% | -15% | 3 | Afterburner III | Csak gyártható |

Az **Engine III** a [Gyártásban](/wiki/06-Items/Overview.md#upgrading-modules) készül egy Engine II-ből, 2 000 Thuliummal, 60 Ship Fragmenttel, 3 Power Core-ral és a Skylabodból származó 6 Velkonite Reinforced Plate-tel. Megtartja az elhasznált hajtómű bűvölési fokozatát, a bónuszai pedig újra kisorsolódnak ([Modulfejlesztések a Gyártásban](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Előbb vedd le az Engine II-t a hajóról (és a fúvókáit is vedd ki belőle): az a hajtómű, amely fel van szerelve, vagy fúvókákat hordoz, nem használódik el.

A hajtóművek Pajzsbónusza benne van a tárgyadatokban, de a játék sosem alkalmazta: a hajtóművek nem gyengítik a pajzsaidat, és a tárgykártyák kihagyják.

---

## Fúvókák {#thrusters}

A fúvókák hajtóművekbe vagy adaptív magokba kerülnek, hogy növeljék azok sebességteljesítményét. Két család van, mindkettő négy szintből áll: az **Impulse** fúvókák adják a legtöbb fix sebességet, és egy kicsit megszorozzák annak a hajtóműnek a sebességét, amelybe be vannak építve; a **Momentum** fúvókák kevesebb fix sebességet adnak, de jobban megszorozzák. Egy fúvókákkal ellátott hajtómű (vagy adaptív mag) **a saját alapsebességét plusz a fúvókák fix sebességnövelését termeli, az egészet pedig megszorozza a fúvókák egymással összeszorzott sebességszorzóival** ([hogyan számolódik a sebesség](/wiki/03-Mechanics/Speed.md)): egy Engine III három Momentum Thruster IV-gyel (6 + 3 x 12) x 1,11 x 1,11 x 1,11 = 57,4 sebességet termel, három Impulse Thruster IV-gyel (6 + 3 x 17) x 1,02 x 1,02 x 1,02 = 60,5-öt, egy Adaptive Core II két Impulse Thruster IV-gyel pedig (0 + 2 x 17) x 1,02 x 1,02 = 35,4-et (két Momentum Thruster IV-gyel 29,6-et).

| Név | Ritkaság | Fix sebességnövelés | Sebességszorzó | Ár |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Silány | +5 | x1,02 | 20 000 kredit |
| **Impulse Thruster II** | Gyakori | +10 | x1,02 | Csak gyártható |
| **Impulse Thruster III** | Ritka | +15 | x1,03 | Csak gyártható |
| **Impulse Thruster IV** | Epikus | +17 | x1,02 | Csak gyártható |
| **Momentum Thruster I** | Silány | +4 | x1,06 | 20 000 kredit |
| **Momentum Thruster II** | Gyakori | +8 | x1,07 | Csak gyártható |
| **Momentum Thruster III** | Ritka | +11 | x1,09 | Csak gyártható |
| **Momentum Thruster IV** | Epikus | +12 | x1,11 | Csak gyártható |

Minden szinten az Impulse Thruster többet termel, mint az azonos szintű Momentum Thruster, adaptív magban és egy, két vagy három fúvókás hajtóműben egyaránt (60,5 a 57,4 ellen három IV. szintű fúvókával egy Engine III-ban, és három Impulse Thruster IV a legjobb, amilyen egy Engine III lehet). Amiben a Momentum Thruster többet ad, az egy második bónusz (lent).

A [Kovácsműhely](/wiki/06-Items/Forge.md) bónusza egy fúvóka sebességszorzóján az 1 feletti részt növeli (a +15% bónusz az x1,11 szorzón x1,1265 értéket ad), az x1,05 vagy annál kisebb szorzóra pedig a Kovácsműhely nem sorsol bónuszt: egy Impulse Thruster x1,02 vagy x1,03 szorzóján ezredrésznyit érne. Egy Impulse Thruster egy bónuszt bír (a fix sebességét), egy Momentum Thruster kettőt.

Az egyes családok I. szintjét 20 000 kreditért árulják. A II–IV. szintet a [Gyártásban](/wiki/06-Items/Overview.md#upgrading-modules) készíted el, mindegyiket az azonos család eggyel alacsonyabb szintű fúvókájából (egy Impulse Thruster II-t egy Impulse Thruster I-ből, a III-at a II-ből, a IV-et a III-ból), Thuliumból, zsákmányból és a Skylabodból származó Velkonite Reinforced Plate-ekből (2, 4 és 6 lemez). Egy fúvóka soha nem vált családot: az Impulse és a Momentum között az I. szint megvásárlásakor döntesz. Mindegyik megtartja az elhasznált fúvóka bűvölési fokozatát, a bónuszaik pedig újra kisorsolódnak ([Modulfejlesztések a Gyártásban](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). A fúvókák nem illenek [képességfoglalatba](/wiki/03-Mechanics/Abilities.md); hajtóművekbe és adaptív magokba valók.

### Az idegenek lehagyása {#outrunning-aliens}

Az idegenek sebessége 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) és 230 (Crystalys). Egy Engine II-vel és két fúvókával felszerelt Ostirion 223,1-gyel repül Impulse Thruster I-gyel: ez még a Crystalys alatt van, ezért egy a Gyártásban készült fúvóka kell hozzá, hogy lehagyd (234,0 Impulse Thruster II-vel, 245,5 III-mal, 249,1 IV-gyel). A Momentum fúvókák ezen a hajón kicsit alacsonyabban repülnek (222,0 egy Momentum Thruster I-gyel; 231,8, 240,1 és 243,9 a II.–IV.-gyel): mindkét család I. szintje a Crystalys alatt marad, a Gyártásban készült szintek mind fölé kerülnek.
