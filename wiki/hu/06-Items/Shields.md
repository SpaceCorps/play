<!-- wiki-i18n source: 1adce749be3cd1f3 -->
<!-- wiki-i18n title: Pajzsok -->
# Pajzsok és védelem {#shields-defense}

A védelmi modulok pajzskapacitást adnak, elnyelik a sebzést, és újratöltik a védelmedet.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Tárgyfa {#item-tree}

Amit a Gyártás elkészít, ahhoz előbb a technológiája kell; vidd az egeret egy tárgy fölé, hogy lásd, mennyi ideig tart a kutatása. A technológiafa, az üzemanyag és a boost: [Kutatás](/wiki/03-Mechanics/Research.md).

```tree
Light Shield Core | shield, shoddy | buy 20000 Credits | /wiki/06-Items/Shields.md#shield-cores
Basic Shield Core | shield, common | buy 2000 Thulium | /wiki/06-Items/Shields.md#shield-cores
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cores
Adaptive Core I | hybrid-generator, shoddy | buy 100000 Credits | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core II | hybrid-generator, common | buy 4000 Thulium | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core III | hybrid-generator, rare | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Absorption Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells

Light Shield Core -> Basic Shield Core => Heavy Shield Core
Adaptive Core I -> Adaptive Core II -> Adaptive Core III
Absorption Shield Cell I => Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell I => Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```
<!-- item-tree:end -->

## Pajzsmagok {#shield-cores}

Szereld fel a pajzsmagokat aktív védőgátak létrehozásához, a hajód generátorfoglalataiba vagy a [drónjaidra](/wiki/03-Mechanics/Drones.md) (a drón foglalata magfoglalatnak számít). Vedd figyelembe, hogy a nehéz pajzsok lassítják a hajódat. A **képességfoglalatba** tett pajzsmag ehelyett a Különleges hatás oszlopban szereplő **Shield Surge** képességet adja, tíz másodperc alatt lezajló pajzsjavítást, és saját pajzsot nem ad hozzá (lásd: [Képességek](/wiki/03-Mechanics/Abilities.md)).

| Név | Ritkaság | Kapacitás | Töltődési sebesség | Elnyelés | Pajzs % | Sebesség % | Cellafoglalatok | Különleges hatás | Ár |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Light Shield Core** | Silány | 10 000 | 333/mp | 45% | +5% | -1% | 1 | Shield Surge I | 20 000 kredit |
| **Basic Shield Core** | Gyakori | 15 000 | 500/mp | 48% | +10% | -3% | 2 | Shield Surge II | 2 000 Thulium |
| **Heavy Shield Core** | Ritka | 25 000 | 833/mp | 50% | +20% | -5% | 3 | Shield Surge III | Csak gyártható |

A **Heavy Shield Core** a [Gyártásban](/wiki/06-Items/Overview.md#upgrading-modules) készül egy Basic Shield Core-ból, 2 000 Thuliummal, 20 Cataclysite-tal, 8 Reinforced Hull Plate-tel és a Skylabodból származó 6 Velkonite Reinforced Plate-tel. Megtartja az elhasznált mag bűvölési fokozatát, a bónuszai pedig újra kisorsolódnak ([Modulfejlesztések a Gyártásban](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Előbb vedd le a Basic Shield Core-t a hajóról (és a celláit is vedd ki belőle): az a mag, amely fel van szerelve, vagy cellákat hordoz, nem használódik el.

Az **elnyelés** a találatoknak az a része, amelyet a pajzsaid felfognak; a többit a hajótest kapja. Egy pajzs önmagában **45–50%**, a többit a cellái adják: a legjobb pajzs a legjobb cellákkal (egy Heavy Shield Core három Absorption Shield Cell IV-gyel) **80%**, ennyi a legtöbb, amit egy hajó külön boostok nélkül elér. Ezt két állandó boost növeli tovább: a Szezonbolt Shield Absorbance Boost buffja (szintenként +0,1 pont, 100 szint, szintenként 25 wipe-pont) és a Kovácsműhely elnyelési bónuszai. A wipe-pontok mai forrásai (a felső határukon összesen 855, és a wipe-okon át megmaradnak; további források tervben vannak) a 100 szintből 34-et vesznek meg (+3,4 pont), ami egy teljesen kikovácsolt Örök fokozatú összeállítással körülbelül **95%**. A jellemzőnek azonban nincs 100%-nál felső határa: a támadó *pajzsáthatolását* levonják belőle, ezért ami egy hajónál 100% fölött van, az a tartaléka az áthatolással szemben. Lásd: [Pajzsmechanika](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-).

---

## Hibridgenerátorok (adaptív magok) {#hybrid-generators-adaptive-cores-}

Az adaptív magok hibridgenerátorként működnek, a pajzs és a sebesség képességeit egyesítik. Foglalataikba fúvókákat és pajzscellákat is fogadnak (foglalatonként egy modul, bármelyik fajtából). A Pajzsbónuszuk és a Sebességbónuszuk úgy számít, mint egy pajzsé vagy egy hajtóműé (a négy legjobb, a foglalat arányával szorozva). Nincs elnyelésük: nem változtatják a hajód elnyelését, és a bennük lévő cellák csak kapacitást és töltődést adnak. A találatokból csak a pajzsok fognak fel részt, ezért az adaptív magban lévő celláknak a hajón pajzs is kell.

| Név | Ritkaság | Pajzsbónusz % | Sebességbónusz % | Foglalatok | Különleges hatás | Ár |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **Adaptive Core I** | Silány | +5% | +3% | 1 | — | 100 000 kredit |
| **Adaptive Core II** | Gyakori | +8% | +4% | 2 | — | 4 000 Thulium |
| **Adaptive Core III** | Ritka | +15% | +5% | 3 | — | Csak gyártható |

---

## Pajzscellák {#shield-cells}

A pajzscellákat pajzsmagokba vagy adaptív magokba szereled (annyit, ahány foglalata a magnak van), hogy erősítsék az adott magot. Egy pajzsmagban az elnyelését is növelik, pontokban, és vele azt a részt, amelyet a pajzsaid fognak fel minden találatból. Két család van, mindkettő négy szintből áll: a **Capacity** cellák adják a legtöbb pajzsot és töltődést, az **Absorption** cellák a legtöbb elnyelést (minden szinten kétszer annyi elnyelést és feleannyi pajzsot és töltődést, mint az azonos szintű Capacity). A Capacity azoknak a hajóknak segít, amelyeknél a pajzs dönti el a harcot, az Absorption azoknak, amelyeknél a hajótest. Egy mag, amelynek minden foglalatát ugyanolyan cella tölti ki: egy Light Shield Core (1 foglalat) 47–55%, egy Basic Shield Core (2 foglalat) 52–68%, egy Heavy Shield Core (3 foglalat) 56–80%, az I. szintű Capacity celláktól a IV. szintű Absorption cellákig. Ha leszereled a magot, vagy a [Kovácsműhely](/wiki/06-Items/Forge.md) összevonásánál donorként elhasználod, a cellái visszakerülnek a leltárba.

| Név | Ritkaság | Kapacitásnövelés | Töltődésnövelés | Elnyelésnövelés | Ár |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Capacity Shield Cell I** | Silány | +3 000 | +250/mp | +2% | 30 000 kredit |
| **Capacity Shield Cell II** | Gyakori | +6 000 | +500/mp | +3% | Csak gyártható |
| **Capacity Shield Cell III** | Ritka | +9 000 | +750/mp | +4% | Csak gyártható |
| **Capacity Shield Cell IV** | Epikus | +12 000 | +1 000/mp | +5% | Csak gyártható |
| **Absorption Shield Cell I** | Silány | +1 500 | +125/mp | +4% | 30 000 kredit |
| **Absorption Shield Cell II** | Gyakori | +3 000 | +250/mp | +6% | Csak gyártható |
| **Absorption Shield Cell III** | Ritka | +4 500 | +375/mp | +8% | Csak gyártható |
| **Absorption Shield Cell IV** | Epikus | +6 000 | +500/mp | +10% | Csak gyártható |

Az egyes családok I. szintjét 30 000 kreditért árulják. A II–IV. szintet a [Gyártásban](/wiki/06-Items/Overview.md#upgrading-modules) készíted el, mindegyiket az azonos család eggyel alacsonyabb szintű cellájából (egy Capacity Shield Cell II-t egy Capacity Shield Cell I-ből, a III-at a II-ből, a IV-et a III-ból), Thuliumból, zsákmányból és a Skylabodból származó Velkonite Reinforced Plate-ekből (2, 4 és 6 lemez). Egy cella soha nem vált családot: a Capacity és az Absorption között az I. szint megvásárlásakor döntesz. Az új cella megtartja az elhasznált cella bűvölési fokozatát, a bónuszai pedig újra kisorsolódnak ([Modulfejlesztések a Gyártásban](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). A cellák nem illenek [képességfoglalatba](/wiki/03-Mechanics/Abilities.md); pajzsokba és adaptív magokba valók.
