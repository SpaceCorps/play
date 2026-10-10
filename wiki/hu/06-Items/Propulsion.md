<!-- wiki-i18n source: 1433a0058afe39fa -->
<!-- wiki-i18n title: Hajtás -->
# Hajtás és sebesség {#propulsion-speed}

A hajtásrendszerek határozzák meg a hajód mozgási sebességét és manőverezőképességét.

## Egy percben {#in-one-minute}

- **A hajtóművek sebességet termelnek, a fúvókák beléjük kerülnek, és növelik azt.** Egy hajtómű egy–három fúvókát fogad (egy Engine I egyet, egy Engine II kettőt, egy Engine III hármat), az adaptív mag is (a szintje mondja meg, hányat).
- **Két család, mindkettő négy szintből áll.** Az Impulse Thrusterek adják a legtöbb fix sebességet. A Momentum Thrusterek kevesebb fix sebességet adnak, de jobban megszorozzák a sebességet. Mindkét családban minden szint jobb az alatta lévőnél, mindkét értékben.
- **Melyik hova.** Alapszabályként az Impulse család fúvókáit tedd mindenhová: csak a teli Engine III-ban (három fúvóka) vezetnek az I. és II. szintű Momentum fúvókák. [Az alábbi táblázatban](#which-thruster-where) ott vannak a számok. A leggyorsabb Engine III három Impulse Thruster IV-et tartalmaz, és 52,5-öt ad.
- **Honnan szerezhetők.** Mindkét család I. szintje 20 000 kreditbe kerül. A II.–IV. szintet a Gyártásban készíted, mindegyiket az alatta lévőből, és egy fúvóka sosem vált családot.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Tárgyfa {#item-tree}

Amit a Gyártás elkészít, ahhoz előbb a technológiája kell; vidd az egeret egy tárgy fölé, hogy lásd, mennyi ideig tart a kutatása. A technológiafa, az üzemanyag és a boost: [Kutatás](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Engine I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I => Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Hajtóművek {#engines}

A hajtóművek a hajód fő tolóerő-forrásai. A **képességfoglalatba** tett hajtómű ehelyett a Különleges hatás oszlopban szereplő **Afterburner** képességet adja, tíz másodpercnyi sebességlöketet (több hajtóművel hosszabbat), és saját tolóerőt nem ad hozzá (lásd: [Képességek](/wiki/03-Mechanics/Abilities.md)).

| Név | Ritkaság | Alapsebesség | Sebességbónusz % | Pajzsbónusz % | Foglalatok | Különleges hatás | Ár |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Silány | +2 | +2% | -2% | 1 | Afterburner I | 20 000 kredit |
| **Engine II** | Gyakori | +4 | +4% | -8% | 2 | Afterburner II | Csak gyártható |
| **Engine III** | Ritka | +6 | +5% | -15% | 3 | Afterburner III | Csak gyártható |

Az **Engine II** a [Gyártásban](/wiki/06-Items/Overview.md#upgrading-modules) készül egy Engine I-ből, 1 000 Thuliummal, 10 Ship Fragmenttel, 1 Power Core-ral és 2 Velkonite Reinforced Plate-tel. Az **Engine III** ott készül egy Engine II-ből, 2 000 Thuliummal, 60 Ship Fragmenttel, 3 Power Core-ral és 3 Dark Matter Plate-tel ([Dark Matter és Dark Matter Plate-ek](/wiki/03-Mechanics/Dark-Matter.md)). Mindkettő megtartja az elhasznált hajtómű bűvölési fokozatát, a bónuszai pedig újra kisorsolódnak ([Modulfejlesztések a Gyártásban](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Előbb vedd le a hajóról az elhasználandó hajtóművet (és a fúvókáit is vedd ki belőle): az a hajtómű, amely fel van szerelve, vagy fúvókákat hordoz, nem használódik el.

A hajtóművek Pajzsbónusza benne van a tárgyadatokban, de a játék sosem alkalmazta: a hajtóművek nem gyengítik a pajzsaidat, és a tárgykártyák kihagyják.

---

## Fúvókák {#thrusters}

A fúvókák hajtóművekbe vagy adaptív magokba kerülnek, hogy növeljék azok sebességteljesítményét. Két család van, mindkettő négy szintből áll: az **Impulse** fúvókák adják a legtöbb fix sebességet, és egy kicsit megszorozzák annak a hajtóműnek a sebességét, amelybe be vannak építve; a **Momentum** fúvókák kevesebb fix sebességet adnak, de jobban megszorozzák. Mindkét családban minden szint jobb az alatta lévőnél, a fix sebességben és a szorzóban is. Egy fúvókákkal ellátott hajtómű (vagy adaptív mag) **a saját alapsebességét plusz a fúvókák fix sebességnövelését termeli, az egészet pedig megszorozza a fúvókák egymással összeszorzott sebességszorzóival** ([hogyan számolódik a sebesség](/wiki/03-Mechanics/Speed.md)): egy Engine III három Momentum Thruster IV-gyel (6 + 3 x 11,135) x 1,0935 x 1,0935 x 1,0935 = 51,5 sebességet termel, három Impulse Thruster IV-gyel (6 + 3 x 14,025) x 1,02975 x 1,02975 x 1,02975 = 52,5-öt, egy Adaptive Core II két Impulse Thruster IV-gyel pedig (0 + 2 x 14,025) x 1,02975 x 1,02975 = 29,7-et (két Momentum Thruster IV-gyel 26,6-at).

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

Az Impulse több fix sebességet ad, a Momentum jobban szoroz, ezért az dönt, melyik család a gyorsabb, hogy mennyit termel már a hajtómű magától. A fix sebesség ott számít a legtöbbet, ahol kevés a megszorozható sebesség: az adaptív magban (nincs saját sebessége) és az egy vagy két fúvókás hajtóműben. A szorzó a teli Engine III-ban számít a legtöbbet, ahol sok a megszorozható sebesség, de ott csak az I. és II. szintű Momentum fúvókák győznek. Ennyi sebességet termel mindegyik IV. szintű fúvókákkal, minden foglalatban:

| Hol vannak a fúvókák | Impulse Thruster IV-gyel | Momentum Thruster IV-gyel | Gyorsabb |
| :--- | :---: | :---: | :--- |
| Engine I, 1 fúvóka | 16,5 | 14,4 | Impulse |
| Engine II, 2 fúvóka | 34,0 | 31,4 | Impulse |
| Engine III, 1 fúvóka | 20,6 | 18,7 | Impulse |
| Engine III, 2 fúvóka | 36,1 | 33,8 | Impulse |
| Engine III, 3 fúvóka | 52,5 | 51,5 | Impulse |
| Adaptive Core II, 2 fúvóka | 29,7 | 26,6 | Impulse |

- **Alacsonyabb szintek.** Az alacsonyabb szintek ugyanígy mennek, két szoros esettel és egy kivétellel: két fúvókával egy Engine II-ben a családok az I. és II. szinten egyenlők (az Impulse 0,06-tal, illetve 0,24-gyel vezet), két fúvókával egy Engine III-ban is (0,1-en belül). A III. szinttől mindkettőben az Impulse vezet, 1,5–2,6-tal. A kivétel a teli Engine III: ott a Momentum az I. és II. szinten vezet, 0,6-tal és 0,9-cel, az Impulse pedig a III. és IV. szinten, 0,5-tel és 1,0-val.
- **A leggyorsabb Engine III.** Három Impulse Thruster IV-et tartalmaz: 52,5, egy kicsit több, mint egy Impulse és két Momentum Thruster IV (52,1) vagy három Momentum (51,5).

A [Kovácsműhely](/wiki/06-Items/Forge.md) bónusza egy fúvóka sebességszorzóján az 1 feletti részt növeli (a +15% bónusz az x1,0935 szorzón x1,1075 értéket ad), az x1,05 vagy annál kisebb szorzóra pedig a Kovácsműhely nem sorsol bónuszt: egy Impulse Thruster x1,017–x1,02975 szorzóján 0,005-nál kevesebbet érne (a +15% az x1,02975 szorzón x1,034 értéket ad). Egy Impulse Thruster egy bónuszt bír (a fix sebességét), egy Momentum Thruster kettőt.

Az egyes családok I. szintjét 20 000 kreditért árulják. A II–IV. szintet a [Gyártásban](/wiki/06-Items/Overview.md#upgrading-modules) készíted el, mindegyiket az azonos család eggyel alacsonyabb szintű fúvókájából (egy Impulse Thruster II-t egy Impulse Thruster I-ből, a III-at a II-ből, a IV-et a III-ból), Thuliumból, zsákmányból és lemezekből: a II. vagy a III. szinthez 2 vagy 4 Velkonite Reinforced Plate a Skylabodból, a IV. szinthez 3 Dark Matter Plate. Egy fúvóka soha nem vált családot: az Impulse és a Momentum között az I. szint megvásárlásakor döntesz. Mindegyik megtartja az elhasznált fúvóka bűvölési fokozatát, a bónuszaik pedig újra kisorsolódnak ([Modulfejlesztések a Gyártásban](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). A fúvókák nem illenek [képességfoglalatba](/wiki/03-Mechanics/Abilities.md); hajtóművekbe és adaptív magokba valók.

### Az idegenek lehagyása {#outrunning-aliens}

Az idegenek sebessége 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) és 230 (Crystalys). Egy Engine II-vel és két fúvókával felszerelt Ostirion 221,4-gyel repül Impulse Thruster I-gyel: ez még a Crystalys alatt van, ezért egy a Gyártásban készült fúvóka kell hozzá, hogy lehagyd (230,8 Impulse Thruster II-vel, 240,3 III-mal, 243,3 IV-gyel). A Momentum fúvókák ezen a hajón ugyanolyan gyorsan vagy kicsit alacsonyabban repülnek (221,4 egy Momentum Thruster I-gyel, aztán 230,5, 238,4 és 240,7 a II.–IV.-gyel): mindkét család I. szintje a Crystalys alatt marad, a Gyártásban készült szintek mind fölé kerülnek, a II. szint csak 0,8-cal, illetve 0,5-tel.
