<!-- wiki-i18n source: da8af0d25d34a2c4 -->
<!-- wiki-i18n title: Leltár -->
# Leltár és felszerelés {#inventory-equipment}

A hangár a hajóid és a felszerelésed kezelésére szolgál. A tárgyak hatékony felszerelése kulcs a túléléshez és az uralomhoz. Megteheted az állomáson, repülés közben pedig biztonságos zónán belülről: lásd: [A hangár repülés közben](/wiki/03-Mechanics/Hangar.md).

![The Hangar's inventory: the category chips are one glyph each (the name is the tooltip) with the count of what you hold](../../img/wiki-img/shots/inventory-chips.jpg)
![Dragging a rectangle over the empty space of the inventory: every tile it touches is selected and the title row counts them](../../img/wiki-img/shots/inventory-marquee.jpg)

## Felszerelési foglalatok és értékhatékonyság {#equipment-slots-stat-efficiencies}

A hagyományos űrjátékokkal ellentétben a SpaceCorpsban dinamikusan sávokra osztott felszerelési foglalatok vannak, amelyek a beszerelt modulok hatékonyságát skálázzák.

- **Lézerfoglalatok**: támadó fegyvereknek (lézerek). Ezek mindig **100%-os sebzéssel és hatótávval** működnek.
- **Generátorfoglalatok**: közös foglalatok pajzsoknak, hajtóműveknek és adaptív magoknak. Három hatékonysági sávra oszlanak, és a sáv dönti el, hogy egy tárgy alapértékeiből mennyi számít. A hangárban minden sáv neve mellett van egy (i), amely elmagyarázza:
  - **Magfoglalatok**: az ide helyezett tárgyak az alapértékeik **100%-át** kapják. Minden hajónak van belőlük: a legerősebb pajzsaidat és hajtóműveidet ide tedd.
  - **Támogató foglalatok**: az ide helyezett tárgyak az alapértékeik **75%-át** kapják (pl. a sebesség vagy a pajzskapacitás 75%-át). Minden hajónak van belőlük.
  - **Segédfoglalatok**: az ide helyezett tárgyak az alapértékeik **50%-át** kapják. Csak néhány hajónak van belőlük (Nomad: 1, Paragon és Storm: 2, Ironclad: 3, Wraith: 4; Protos, Kitefin és Ostirion: nincs). A legjobbak extra, gyengébb pajzsokhoz és hajtóművekhez valók, míg a legerősebbek a magfoglalatokba kerülnek.
  - **Drónfoglalatok**: a drónjaid egyikén lévő pajzs úgy számít, mint a magfoglalatban lévő: az alapértékeinek **100%-át** kapja (lásd: [Drónmechanika](/wiki/03-Mechanics/Drones.md)).
  - **Besorolatlan/régi foglalatok**: az ide helyezett tárgyak nem járulnak hozzá az értékekhez.
  - **A halmozás is csökken**: a pajzsokat és a hajtóműveket a legerősebbtől kezdve rangsorolják (aszerint, hogy mi számít belőlük a foglalatuk részesedése után), és a sáv részesedését megszorozzák a rangjukéval: az 1.–4. teljes értékkel számít, az 5.–7. 85%-kal, 70%-kal és 55%-kal, a 8.-tól kezdve a pajzsok 50%-kal, a hajtóművek 25%-kal. Lásd: [Pajzsok](/wiki/03-Mechanics/Shields.md) és [Sebesség](/wiki/03-Mechanics/Speed.md).
- **Extrafoglalatok**: speciális segédtárgyaknak, például Repair Drone-oknak. A Protoson, a Kitefinen, az Ostirionon és a Nomadon kettő van; a Paragonon, az Ironcladen, a Wraithen és a Stormon, amelyeket gyártasz, három. Az Extra Slots CPU-k ([Extrák](/wiki/06-Items/Extras.md#extra-slots-cpus)) 3, 5 vagy 7 foglalattal többet adnak.
- **Páncélzatfoglalatok**: [hajótest-páncélzatnak](/wiki/06-Items/Hull-Plating.md#hull-plate-slots), amely hajótestet ad hozzá. Csak a négy hajónak vannak, amelyet gyártasz (a Paragonnak 5, a Stormnak 7, az Ironcladnek 15 és a Wraithnek 9), mindegyik zárolva, amíg a Skylabben ki nem kutatod, és a két konfigurációban egyformák.

## Leltárrend {#inventory-order}

A leltár a tárgyaidat ugyanabban a sorrendben listázza, mint a Bolt, függetlenül attól, milyen sorrendben vetted, gyártottad vagy találtad őket. Az összetartozó fajták együtt vannak: lézerek, lézererősítők és lézerlőszerek; pajzsok és pajzscellák; hajtóművek és fúvókák; adaptív magok; extrák (Repair Drone-ok); drónok és drónformációk; végül a nyersanyagok. Egy fajtán belül a legolcsóbb az első (előbb a kreditben, aztán a Thuliumban fizetős), utána az, aminek nincs ára: a csak gyártható felszerelés és a zsákmány, a leggyengébb ritkasággal kezdve (az azonos ritkaságú lézerek közül a leggyengébb sebzésűvel). A lézerlőszer x1-től x4-ig követi egymást, utána a Siphon Battery. A rakéták fajta szerint következnek (előbb az egy célpontú, aztán a területi robbanású, előbb az irányított, aztán az egyenes), majd fokozat szerint, így az Epikus rakéta, amely Thuliumba kerül, a fajtájában az utolsó. Egy tárgy példányai a bűvölési fokozatuk szerint sorakoznak. A rács fölött minden fajtához egy szűrőgomb tartozik, ugyanebben a sorrendben, mindegyik azzal a számmal, ahány tárgyat a keresés talál benne. Mindegyik szűrőgomb külön kapcsolható be vagy ki, így elrejtheted a lőszert és a Repair Drone-okat, amíg lézereken, pajzsokon és hajtóműveken dolgozol: kattints egy szűrőgombra a fajtája megjelenítéséhez vagy elrejtéséhez, Shift-kattintással (vagy dupla kattintással) csak azt a fajtát hagyod bekapcsolva, és kattints rá újra, hogy a többi visszajöjjön. A **Mind** minden fajtát megmutat, az **Egyik sem** mindet elrejti, hogy csak azokat kapcsold be, amelyeket szeretnél. Az áthúzott szűrőgomb ki van kapcsolva, a pipával jelölt be. A keresés a bekapcsolt fajtákon dolgozik, és a választásodat a pilótáddal együtt megjegyzi a játék. Ha minden el van rejtve, a rács ezt kiírja, és felajánlja a **Minden kategória megjelenítése** gombot.

## Eladható tárgyak {#marketable-items}

A megszerzett tárgyak (zsákmány, küldetésjutalmak, és amit a Gyártás és a Kovácsműhely előállít) csempéjén kis **Eladható** címke látszik, a tárgykártya pedig azt írja: „Eladható”, vagy egy olyan köteg esetén, amelynek csak egy része adható el, „Eladható (3 / 5)”. A kategóriachipek melletti **Csak eladható** chip csak ezeket a tárgyakat mutatja. A címkézett tárgy szemetese mellett megjelenő **kalapács** megnyitja az [Aukció](/wiki/03-Mechanics/Auction.md) eladólapját (repülés közben nem látszik: az eladás az állomás egyik oldala). Amit vásároltál, nyertél vagy ajándékba kaptál, nem kap címkét, és nem adható el újra.

## Több tárgy kijelölése {#select-several-items}

Nyomj az eltárolt tárgyak egy üres részére (a csempék melletti szélre, két csempe közti résre vagy az utolsó sor alatti helyre), és húzd: egy áttetsző téglalap követi a mutatót, és minden csempe, amelyet érint, kijelölődik, amíg húzod. Ha elengeded, a kijelölés megmarad; a címsor megszámolja („3 kijelölve”). Húzás közben tartsd lenyomva a **Shift**, a **Ctrl** vagy a **Cmd** billentyűt, hogy hozzáadj a kijelöléshez: a már kijelölt csempék, amelyeket a téglalap érint, ilyenkor kikerülnek belőle. A sima húzás új kijelölést kezd. Az **Esc**, egy kattintás az üres helyen vagy a címsorban a szemetes melletti gomb megszünteti a kijelölést; az **Esc** húzás közben megszakítja a húzást. Egy hosszú leltár felső vagy alsó szélénél a lista magától görget. A csempére nyomás továbbra is a csempéé: kattintás a felszereléshez, húzás egy foglalatra. A címsor szemetese kérdés után törli a kijelölt tárgyakat, amely fel is sorolja őket (az azonos Extrák kötege egészben megy); amíg a repülés közbeni Hangár zárolva van, nem érhető el. A Skylabba szerelt tárgy nem jelölhető ki, és csak az jelölhető ki, amit a keresés és a kategóriachipek a rácson hagynak. Halk kattanás hallatszik, amikor a téglalap egy újabb csempét vesz fel (a beállításokban a „Gombhangok” kapcsolót követi).

**A teljes kijelölés felszerelése.** Húzd az egyik kijelölt csempét, és a teljes kijelölés vele tart: csempék kötege a mutató előtt egy számmal (a nem kijelölt csempe egyedül húzódik, a kijelölt csempére kattintás pedig továbbra is csak azt a tárgyat szereli fel). Ha egy foglalaton vagy egy kártyán engeded el, a mutató alatti tárgy oda kerül, ha belefér, az összes többi pedig a legjobb foglalatába; ha a hajó üres részein engeded el, minden tárgy a legjobb foglalatába kerül; máshol nem történik semmi, az **Esc** pedig elengedi a húzást. A szemetes melletti nyíl gomb a címsorban (ha rámutatsz, azt írja, hogy a kijelölt tárgyakat a legjobb foglalataikba szereli) ugyanezt teszi húzás nélkül; a P.E.T.-nézetben és amíg a repülés közbeni Hangár zárolva van, nem érhető el. A legjobb foglalat az, ahová egy kattintás tenné a tárgyat, tárgyról tárgyra kiszámítva: először a lézerek, a legerősebbek elöl, aztán a pajzsok, a hajtóművek és az adaptív magok, az extrák, a Repair Dronek (szabad képességfoglalatba, ha az extrák megteltek), a páncélzatok, és utoljára az erősítők, cellák és fúvókák, amelyekhez már fel kell szerelve lennie a lézereknek, pajzsoknak és hajtóműveknek. Ami nem fért el, kijelölve marad, és egy üzenet megmondja, hányat sikerült felszerelni („Felszerelve: 7 / 9.”), és a többit miért nem. Az egész lerakásra egyetlen halk hang szól.

## Tárgy a tárgyba szerelés (alfoglalatok) {#item-to-item-equipping-sub-sockets-}

Egyes elsődleges tárgyak „felszerelhetnek” másodlagos támogató tárgyakat (ezt nevezzük alfoglalatba szerelésnek), hogy erősítsék a paramétereiket. Az alfoglalatba szereléshez húzd a támogató tárgyat közvetlenül az elsődleges tárgyra a hangár leltárában.

### Kompatibilitási táblázat {#compatibility-table}

| Elsődleges tárgy | Elfogadott alfoglalat-tárgyak | Eredmény |
| :--- | :--- | :--- |
| **Lézer** | Lézererősítő (Amp) | Növeli az alapsebzést és a kritikus találat értékeit, vagy pontokat von le a célpont elnyeléséből (Penetration Amp) |
| **Pajzs** | Pajzscella | Növeli a pajzskapacitást és a töltődési sebességet |
| **Hajtómű** | Fúvóka | Növeli a hajtómű sebességét és szorzóit |
| **Hibridgenerátor** | Pajzscella VAGY fúvóka | Növeli a pajzskapacitást, a töltődési sebességet vagy a sebességet |
| **Drón** | Lézer vagy pajzs a drón mindegyik foglalatába (egy Master Drone-nak kettő van) | A lézer hozzáadja a sebzését a sortüzedhez; a pajzs úgy számít, mint a magfoglalatban lévő (az alapértékeinek 100%-a) |

---

## Lőszerkezelés {#ammo-management}

A lézerlőszer fogyóeszköz.
- A lőszer halmozódik a leltáradban.
- Az aktív lézerlőszert a HUD gyorssávján válthatod.
- A jobb minőségű lőszer sebzésszorzót ad (pl. Standard Battery x1, Advanced Plasma x2, Ultra Core x3, Experimental Fusion Core x4). A Siphon Battery x1 sebzést okoz kizárólag a pajzsoknak, és a sebzést a te pajzsodnak adja.
