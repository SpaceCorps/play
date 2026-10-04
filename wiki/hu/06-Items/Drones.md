<!-- wiki-i18n source: 0dfda8fd6d9be79d -->
<!-- wiki-i18n title: Drónok -->
# Drónok {#drones}

A drónok megvásárolható vagy legyártható támogató egységek. Egyszerre legfeljebb **8 drón** lehet aktív nálad, a Slave Drone-okat és a Master Drone-okat együtt számítva.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Tárgyfa {#item-tree}

Amit a Gyártás elkészít, ahhoz előbb a technológiája kell; vidd az egeret egy tárgy fölé, hogy lásd, mennyi ideig tart a kutatása. A technológiafa, az üzemanyag és a boost: [Kutatás](/wiki/03-Mechanics/Research.md).

```tree
Slave Drone | drone, common | buy 100000 Credits | /wiki/06-Items/Drones.md#available-drones
Master Drone | drone, rare | craft 40000 Thulium, 60 s | research 36000 s, 36000 science | 1 Slave Drone, 100 Ship Fragment | /wiki/06-Items/Drones.md#available-drones

Slave Drone => Master Drone
```
<!-- item-tree:end -->

## Elérhető drónok {#available-drones}

| Név | Ritkaság | Foglalatok | Leírás | Ár |
| :--------------- | :----- | :---- | :------------------------------------------------------------------------------------------- | :------------------------------- |
| **Slave Drone** | Gyakori | 1 | Alap drón egyetlen felszerelési foglalattal. Az idegenek megsemmisítésével 8 szinten át fejlődik. | 100 000 kredittől (lásd lent) |
| **Master Drone** | Ritka | 2 | A Gyártásban továbbfejlesztett Slave Drone. Aranyszínben repül, megtartja a sorszámát és amit hordoz, második felszerelési foglalatot kap, és újra az 1. szintről indul. | Egy Slave Drone fejlesztése: 40 000 Thulium és 100 Ship Fragment |

A Slave Drone kis gömbként indul, és a 8. szinten páncélozott rohamhajóvá nő. Minden birtokodban lévő drón ugyanannyi tapasztalatot szerez, valahányszor megsemmisítesz egy idegent, a magasabb szint pedig egy kicsit növeli a foglalatában lévő lézer sebzését (a 8. szinten legfeljebb +7%). A szintekről és arról, hogy mindegyikhez mennyi kell, a Drónmechanika oldalon (a Játékmechanika alatt) olvashatsz. Egy Master Drone legyártása nem használ el drónt: a kiválasztott Slave Drone-t fejleszti helyben, és **a szintje és a tapasztalata 0-ra áll vissza**, amikor a fejlesztés befejeződik (a Gyártás ezt kiírja, és megerősítést kér). Cserébe a drónnak **két felszerelési foglalata** van egy helyett: amit hordozott, az az első foglalatban marad, a második üres. A drónjaid a szintjükkel és a tapasztalatukkal együtt megmaradnak a szezon wipe-ján át.

## A Slave Drone árai {#slave-drone-prices}

Minden megvásárolt Slave Drone drágább az előzőnél. Az ár attól függ, hány drónod van vásárláskor (egy Master Drone egynek számít), és a Bolt mindig a következő drónod árát mutatja. Az első három csak kreditbe kerül; a negyediktől Thulium is jár hozzá.

| Drón | Kredit | Thulium |
| :---- | :--------- | :------ |
| 1. | 100 000 | – |
| 2. | 200 000 | – |
| 3. | 400 000 | – |
| 4. | 800 000 | 10 000 |
| 5. | 1 600 000 | 20 000 |
| 6. | 3 200 000 | 30 000 |
| 7. | 6 400 000 | 40 000 |
| 8. | 12 800 000 | 50 000 |

Mind a nyolc együtt 25 500 000 kreditbe és 150 000 Thuliumba kerül. A drónjaid megmaradnak a szezon wipe-ján át, ezért az ár onnan folytatódik, ahány drónod van: három drónnál a következő mindig a 4., nyolcnál pedig már nincs mit venni.

## Használat {#usage}

1. **Vásárolj** Slave Drone-okat a Boltban. **Fejlessz** egyet Master Drone-ná a Gyártásban, ha az aranyszínűt szeretnéd (a szintje és az XP-je újraindul).
2. **Szereld fel** őket a hangárban, a „Drónok” lapon.
3. **Szerelj beléjük** lézereket vagy pajzsokat, hogy erősebb legyél: egy Slave Drone-nak egy foglalata van, egy Master Drone-nak kettő. A lézer a hajóddal együtt tüzel; a pajzs úgy számít, mint a magfoglalatban lévő, az összes értékével.
4. **Léptesd szintre** őket idegenek megsemmisítésével: a hangár megmutatja minden drón szintjét, és hogy a következőhöz mennyi tapasztalat kell.
