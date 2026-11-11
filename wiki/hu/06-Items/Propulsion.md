<!-- wiki-i18n source: fe17f46644fd6072 -->
<!-- wiki-i18n title: Hajtás -->
# Hajtás és sebesség {#propulsion-speed}

A hajtásrendszerek határozzák meg a hajód mozgási sebességét és manőverezőképességét.

## Egy percben {#in-one-minute}

- **A hajtóművek sebességet termelnek, a fúvókák beléjük kerülnek, és növelik azt.** Egy hajtómű egy–három fúvókát fogad (egy Engine I egyet, egy Engine II kettőt, egy Engine III hármat), az adaptív mag is (a szintje mondja meg, hányat).
- **Két család, mindkettő négy szintből áll.** Az Impulse Thrusterek adják a legtöbb fix sebességet. A Momentum Thrusterek kevesebb fix sebességet adnak, de jobban megszorozzák a sebességet. Mindkét családban minden szint jobb az alatta lévőnél, mindkét értékben.
- **Melyik hova.** Alapszabályként a teli Engine III-ba (három fúvóka) Momentum fúvókákat, az adaptív magba Impulse fúvókákat tegyél; a kisebb hajtóművekben a kettő az I. és II. szinten közel van egymáshoz, a III. szinttől pedig az Impulse vezet. [Az alábbi táblázatban](#which-thruster-where) ott vannak a számok. A leggyorsabb Engine III három Momentum Thruster IV-et tartalmaz, és 63,3-at ad.
- **Honnan szerezhetők.** Mindkét család I. szintje 20 000 kreditbe kerül. A II.–IV. szintet a Gyártásban készíted, mindegyiket az alatta lévőből, és egy fúvóka sosem vált családot.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Tárgyfa {#item-tree}

Amit a Gyártás elkészít, ahhoz előbb a technológiája kell; vidd az egeret egy tárgy fölé, hogy lásd, mennyi ideig tart a kutatása. A technológiafa, az üzemanyag és a boost: [Kutatás](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Engine I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 4000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 80 Ship Fragment, 4 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 80 Ship Fragment, 4 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 4000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 4000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I => Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Hajtóművek {#engines}

A hajtóművek a hajód fő tolóerő-forrásai. A **képességfoglalatba** tett hajtómű ehelyett a Különleges hatás oszlopban szereplő **Afterburner** képességet adja, tizenöt másodpercnyi sebességlöketet (több hajtóművel hosszabbat), és saját tolóerőt nem ad hozzá (lásd: [Képességek](/wiki/03-Mechanics/Abilities.md)).

| Név | Ritkaság | Alapsebesség | Sebességbónusz % | Pajzsbónusz % | Foglalatok | Különleges hatás | Ár |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Silány | +5 | +2% | -2% | 1 | Afterburner I | 20 000 kredit |
| **Engine II** | Gyakori | +10 | +3% | -8% | 2 | Afterburner II | Csak gyártható |
| **Engine III** | Ritka | +15 | +4% | -15% | 3 | Afterburner III | Csak gyártható |

Az **Engine II** a [Gyártásban](/wiki/06-Items/Overview.md#upgrading-modules) készül egy Engine I-ből, 2 000 Thuliummal, 60 Ship Fragmenttel, 1 Power Core-ral és 4 Velkonite Reinforced Plate-tel. Az **Engine III** ott készül egy Engine II-ből, 4 000 Thuliummal, 110 Ship Fragmenttel, 5 Power Core-ral, 1 Ancient Control Unittal és 4 Dark Matter Plate-tel ([Dark Matter és Dark Matter Plate-ek](/wiki/03-Mechanics/Dark-Matter.md)). Mindkettő megtartja az elhasznált hajtómű bűvölési fokozatát és bónuszait ([Modulfejlesztések a Gyártásban](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Előbb vedd le a hajóról az elhasználandó hajtóművet (és a fúvókáit is vedd ki belőle): az a hajtómű, amely fel van szerelve, vagy fúvókákat hordoz, nem használódik el.

A hajtóművek Pajzsbónusza benne van a tárgyadatokban, de a játék sosem alkalmazta: a hajtóművek nem gyengítik a pajzsaidat, és a tárgykártyák kihagyják.

---

## Fúvókák {#thrusters}

A fúvókák hajtóművekbe vagy adaptív magokba kerülnek, hogy növeljék azok sebességteljesítményét. Két család van, mindkettő négy szintből áll: az **Impulse** fúvókák adják a legtöbb fix sebességet, és egy kicsit megszorozzák annak a hajtóműnek a sebességét, amelybe be vannak építve; a **Momentum** fúvókák kevesebb fix sebességet adnak, de jobban megszorozzák. Mindkét családban minden szint jobb az alatta lévőnél, a fix sebességben és a szorzóban is. Egy fúvókákkal ellátott hajtómű (vagy adaptív mag) **a saját alapsebességét plusz a fúvókák fix sebességnövelését termeli, az egészet pedig megszorozza a fúvókák egymással összeszorzott sebességszorzóival** ([hogyan számolódik a sebesség](/wiki/03-Mechanics/Speed.md)): egy Engine III három Momentum Thruster IV-gyel (15 + 3 x 11,135) x 1,0935 x 1,0935 x 1,0935 = 63,3 sebességet termel, három Impulse Thruster IV-gyel (15 + 3 x 14,025) x 1,02975 x 1,02975 x 1,02975 = 62,3-öt, egy Adaptive Core II két Impulse Thruster IV-gyel pedig (0 + 2 x 14,025) x 1,02975 x 1,02975 = 29,7-et (két Momentum Thruster IV-gyel 26,6-at).

| Név | Ritkaság | Fix sebességnövelés | Sebességszorzó | Ár |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Silány | +4,25 | x1,017 | 20 000 kredit |
| **Impulse Thruster II** | Gyakori | +8,5 | x1,02125 | Csak gyártható |
| **Impulse Thruster III** | Ritka | +12,75 | x1,0255 | Csak gyártható |
| **Impulse Thruster IV** | Epikus | +14,025 | x1,02975 | Csak gyártható |
| **Momentum Thruster I** | Silány | +3,825 | x1,051 | 20 000 kredit |
| **Momentum Thruster II** | Gyakori | +7,65 | x1,0595 | Csak gyártható |
| **Momentum Thruster III** | Ritka | +10,625 | x1,0765 | Csak gyártható |
| **Momentum Thruster IV** | Epikus | +11,135 | x1,0935 | Csak gyártható |

### Melyik fúvóka hova {#which-thruster-where}

Az Impulse több fix sebességet ad, a Momentum jobban szoroz, ezért az dönt, melyik család a gyorsabb, hogy mennyit termel már a hajtómű magától. A fix sebesség ott számít a legtöbbet, ahol kevés a megszorozható sebesség: az adaptív magban (nincs saját sebessége) és az egy vagy két fúvókás hajtóműben. A szorzó a teli Engine III-ban számít a legtöbbet, ahol sok a megszorozható sebesség, és ott a Momentum fúvókák minden szinten győznek. Ennyi sebességet termel mindegyik IV. szintű fúvókákkal, minden foglalatban:

| Hol vannak a fúvókák | Impulse Thruster IV-gyel | Momentum Thruster IV-gyel | Gyorsabb |
| :--- | :---: | :---: | :--- |
| Engine I, 1 fúvóka | 19,6 | 17,6 | Impulse |
| Engine II, 2 fúvóka | 40,3 | 38,6 | Impulse |
| Engine III, 1 fúvóka | 29,9 | 28,6 | Impulse |
| Engine III, 2 fúvóka | 45,6 | 44,6 | Impulse |
| Engine III, 3 fúvóka | 62,3 | 63,3 | Momentum |
| Adaptive Core II, 2 fúvóka | 29,7 | 26,6 | Impulse |

- **Alacsonyabb szintek.** A III. szinttől az Impulse mindenhol vezet, a teli Engine III kivételével, 0,6 és 3,1 közötti különbséggel. Az I. és II. szinten a két család a teli Engine III-on kívül kevesebb mint egy ponttal tér el egymástól: az Impulse egy Engine I-ben és egy Adaptive Core I-ben vagy II-ben vezet, a Momentum egy- vagy kétfúvókás Engine III-ban és kétfúvókás Engine II-ben vezet vagy egyenlő. A kivétel a teli Engine III: ott a Momentum minden szinten vezet, 1,0 és 2,0 közötti különbséggel.
- **A leggyorsabb Engine III.** Három Momentum Thruster IV-et tartalmaz: 63,3, egy kicsit több, mint egy Impulse és két Momentum Thruster IV (63,2) vagy három Impulse (62,3).

A [Kovácsműhely](/wiki/06-Items/Forge.md) bónusza egy fúvóka sebességszorzóján az 1 feletti részt növeli (a +15% bónusz az x1,0935 szorzón x1,1075 értéket ad), az x1,05 vagy annál kisebb szorzóra pedig a Kovácsműhely nem sorsol bónuszt: egy Impulse Thruster x1,017–x1,02975 szorzóján 0,005-nál kevesebbet érne (a +15% az x1,02975 szorzón x1,034 értéket ad). Egy Impulse Thruster egy bónuszt bír (a fix sebességét), egy Momentum Thruster kettőt.

Az egyes családok I. szintjét 20 000 kreditért árulják. A II–IV. szintet a [Gyártásban](/wiki/06-Items/Overview.md#upgrading-modules) készíted el, mindegyiket az azonos család eggyel alacsonyabb szintű fúvókájából (egy Impulse Thruster II-t egy Impulse Thruster I-ből, a III-at a II-ből, a IV-et a III-ból), Thuliumból, zsákmányból és lemezekből: a II. vagy a III. szinthez 4 Velkonite Reinforced Plate a Skylabodból, a IV. szinthez 4 Dark Matter Plate és egy Ancient Control Unit. Egy fúvóka soha nem vált családot: az Impulse és a Momentum között az I. szint megvásárlásakor döntesz. Mindegyik megtartja az elhasznált fúvóka bűvölési fokozatát és bónuszait ([Modulfejlesztések a Gyártásban](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). A fúvókák nem illenek [képességfoglalatba](/wiki/03-Mechanics/Abilities.md); hajtóművekbe és adaptív magokba valók.

### Az idegenek lehagyása {#outrunning-aliens}

Az idegenek sebessége 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) és 230 (Crystalys). Egy Engine II-vel és két fúvókával felszerelt Ostirion (alapsebessége 220) 246,3-mal repül Impulse Thruster I-gyel, 255,6-tal II-vel, 265,1-gyel III-mal és 268,2-vel IV-gyel: minden szint lehagyja a Crystalyst, még a megvásárolható Impulse Thruster I is. A Momentum fúvókák ezen a hajón két ponton belül járnak ettől (246,7 egy Momentum Thruster I-gyel, aztán 255,9, 263,9 és 266,3 a II.–IV.-gyel): mindkét család minden szintje a Crystalys fölött van, legalább 16,3-mal.
