<!-- wiki-i18n source: 2bd1925e336e25b6 -->
<!-- wiki-i18n title: Hajótest-páncélzat -->
# Hajótest-páncélzat {#hull-plating}

<!-- wiki-search: hull plate; hull plate slot; hull plate slots; plate slot; plate; armour; armor; hpl; páncélzat; páncélzatfoglalat; páncélozás -->

A Dormant raj tanulmányozása előrelépést mutatott a páncélzat technológiájában. Ezzel a technológiával a hajók javíthatják a hajótestüket: a **hajótest-páncélzat** olyan páncélzat, amely egy legyártott hajó hajótestlemez-foglalatába illeszkedik, és hajótestpontokat ad hozzá. Ez nem a Hull Plating **Booster**, amelyről a [Boosterek](/wiki/06-Items/Boosters.md) oldal szól: az egy időleges bónusz.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Tárgyfa {#item-tree}

Amit a Gyártás elkészít, ahhoz előbb a technológiája kell; vidd az egeret egy tárgy fölé, hogy lásd, mennyi ideig tart a kutatása. A technológiafa, az üzemanyag és a boost: [Kutatás](/wiki/03-Mechanics/Research.md).

```tree
Hull Plating I | hull-plating, uncommon | buy 5000 Thulium | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating II | hull-plating, rare | craft 2500 Thulium, 300 s | research 86400 s, 86400 science, 25 Dark Matter | 1 Hull Plating I, 150 Ship Fragment, 20 Reinforced Hull Plate, 6 Power Core, 5 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating III | hull-plating, epic | craft 4000 Thulium, 600 s | research 172800 s, 172800 science, 40 Dark Matter | 1 Hull Plating II, 300 Ship Fragment, 40 Reinforced Hull Plate, 12 Power Core, 1 Ancient Control Unit, 8 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings

Hull Plating I => Hull Plating II => Hull Plating III
```
<!-- item-tree:end -->

## A három páncélzat {#the-three-platings}

| Tárgy | Hozzáadott hajótest | Honnan származik |
| :--- | ---: | :--- |
| **Hull Plating I** | 5 000 | Bolt, 5 000 Thulium |
| **Hull Plating II** | 10 000 | Gyártás, Hull Plating I-ből |
| **Hull Plating III** | 15 000 | Gyártás, Hull Plating II-ből |

A Hull Plating I-et megveszik. **A II és a III fejlesztés**: a Gyártás elhasznál egy eggyel alacsonyabb szintű páncélzatot (a leltáradban szabadon), és Thuliumot, nyersanyagot és **Dark Matter Plate-et** kér, a II-höz 5-öt, a III-hoz 8-at, miközben bármely más felszerelés utolsó szintje 3-at kér. Mindegyikhez előbb a technológiája kell, a [Kutatás](/wiki/03-Mechanics/Research.md#tree-hull-plating) oldal Hull Plating fájában: a II-höz 1 nap és 25 Dark Matter, a III-hoz 2 nap és 40, magának a Dark Matter Plate-nek a technológiáján felül. A fenti fa mutatja az árakat, az anyagokat és az időket.

A [Kovácsműhely](/wiki/06-Items/Forge.md) minden páncélzatot elfogad, a fejlesztés megtartja az elhasznált páncélzat kovácsolási fokozatát, és újra sorsolja a bónuszát. A páncélzatnak egyetlen értéke van, a hajóteste, ezért egyetlen bónuszt hordoz, fokozattól függően +2%-tól +15%-ig: egy Örök fokozatú Hull Plating III legfeljebb 17 250-et ad. Az [Aukció](/wiki/03-Mechanics/Auction.md) a Hull Plating II-t és III-at listázza, a Hull Plating I-et soha, mert azt a Bolt árulja.

## Páncélzatfoglalatok {#hull-plate-slots}

A hajótest-páncélzat csak **páncélzatfoglalatba** illik, egy önálló foglalattípusba, amely a négy hajónak, amelyet a Gyártásban készítesz, megvan a lézer-, generátor-, extra-, képesség- és drónfoglalatai mellett:

| Hajó | Páncélzatfoglalatok | Egy teljes Hull Plating III készlet hozzáad |
| :--- | ---: | ---: |
| **Paragon** | 5 | 75 000 |
| **Storm** | 7 | 105 000 |
| **Ironclad** | 15 | 225 000 |
| **Wraith** | 9 | 135 000 |

- **Kezdetben mind zárolva.** Egy foglalat akkor nyílik meg, ha a Skylabben kikutatod: foglalatonként egy technológia, 1 óra és 10 Dark Matter, az elsőtől kezdve sorban. A [Kutatás](/wiki/03-Mechanics/Research.md#ship-technologies) nézet egy hajó foglalatait egyetlen kártyaként mutatja, foglalatonként egy ponttal.
- **Hajófajta, nem egy hajó.** A foglalatok, amelyeket a Paragonhoz kinyitottál, a Paragon minden dizájnján is nyitva vannak ([Hajódizájnok](/wiki/03-Mechanics/Ship-Designs.md)). A technológia örökre a tiéd: a wipe megtartja.
- **A két konfiguráció osztozik rajtuk.** A páncélzatok a hajóhoz tartoznak: a konfigurációváltás rajta hagyja őket, és a hangár mindkettőben ugyanazokat mutatja.
- **Bármilyen keverék.** A foglalat bármilyen hajótest-páncélzatot elfogad, és két egyforma is rendben van.
- **A hajótested aránya megmarad.** Egy páncélzat felszerelése vagy leszerelése megtartja a hajótested arányát, így a páncélzat soha nem gyógyít és soha nem árt.
- **Mint minden felszerelést**, a páncélzatot a hangárban szereled fel és le, vagy annak ablakában biztonságos zónából, soha nem a nyílt űrben. A foglalat, amelyet nem kutattál ki, visszautasítja a páncélzatot.

A hangárban a **Hajótest-páncélzat** kártya mutatja a foglalatokat. A nyitottba húzással teszel páncélzatot, mint bármelyik foglalatba; a zárolt lakatot mutat, és egy kattintás megnyitja a Skylab kutatását. A többi érték mellett egy csempe összeadja, mit adnak a felszerelt páncélzatok.

## Hogyan adódik össze a hajótest {#how-the-hull-adds-up}

A páncélzat a hajó saját hajótestéhez adja a magáét, és a hangár meg a hajóablak a nagyobb számot mutatja. A hajó hajóteste plusz a páncélzatai ezután ugyanazokon a szorzókon megy át, mint mindig: egy [Hull Plating Booster](/wiki/06-Items/Boosters.md)-en és a viselt [drónformáción](/wiki/03-Mechanics/Formations.md). A dizájn, amely a hajótestet módosítja (a BUCKY-é 25%-kal több), a hajó saját hajótestét változtatja, és a páncélzatok ennek tetejére jönnek.

## Hull Plating vagy Hull Plating Booster? {#hull-plating-or-booster}

Két dolog osztozik a néven. A **hajótest-páncélzat** (ez az oldal) páncél: egy lemez, amely egy legyártott hajó páncélzatfoglalatában ül, és addig adja a hajótestét, amíg fel van szerelve. A **Hull Plating Booster** a [Boosterek](/wiki/06-Items/Boosters.md) oldal időre szóló bónusza, +10% maximális hajótest-pont 10 órára arra a hajóra, amelyet éppen repülsz, és nincs mit felszerelni hozzá. Összeadódnak: a páncélzatok jönnek először, és a Booster 10%-át az összegből veszik.
