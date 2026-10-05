<!-- wiki-i18n source: ad9b37b491751af9 -->
<!-- wiki-i18n title: Leltár -->
# Leltár és felszerelés {#inventory-equipment}

A hangár a hajóid és a felszerelésed kezelésére szolgál. A tárgyak hatékony felszerelése kulcs a túléléshez és az uralomhoz. Megteheted az állomáson, repülés közben pedig biztonságos zónán belülről: lásd: [A hangár repülés közben](/wiki/03-Mechanics/Hangar.md).

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

## Leltárrend {#inventory-order}

A leltár a tárgyaidat ugyanabban a sorrendben listázza, mint a Bolt, függetlenül attól, milyen sorrendben vetted, gyártottad vagy találtad őket. Az összetartozó fajták együtt vannak: lézerek, lézererősítők és lézerlőszerek; pajzsok és pajzscellák; hajtóművek és fúvókák; adaptív magok; extrák (Repair Drone-ok); drónok és drónformációk; végül a nyersanyagok. Egy fajtán belül a legolcsóbb az első (előbb a kreditben, aztán a Thuliumban fizetős), utána az, aminek nincs ára: a csak gyártható felszerelés és a zsákmány, a leggyengébb ritkasággal kezdve (az azonos ritkaságú lézerek közül a leggyengébb sebzésűvel). A lézerlőszer x1-től x4-ig követi egymást, utána a Siphon Battery. A rakéták fajta szerint következnek (előbb az egy célpontú, aztán a területi robbanású, előbb az irányított, aztán az egyenes), majd fokozat szerint, így az Epikus rakéta, amely Thuliumba kerül, a fajtájában az utolsó. Egy tárgy példányai a bűvölési fokozatuk szerint sorakoznak. A rács fölött minden fajtához egy szűrőgomb tartozik, ugyanebben a sorrendben, mindegyik azzal a számmal, ahány tárgyat a keresés talál benne. Mindegyik szűrőgomb külön kapcsolható be vagy ki, így elrejtheted a lőszert és a Repair Drone-okat, amíg lézereken, pajzsokon és hajtóműveken dolgozol: kattints egy szűrőgombra a fajtája megjelenítéséhez vagy elrejtéséhez, Shift-kattintással (vagy dupla kattintással) csak azt a fajtát hagyod bekapcsolva, és kattints rá újra, hogy a többi visszajöjjön. A **Mind** minden fajtát megmutat, az **Egyik sem** mindet elrejti, hogy csak azokat kapcsold be, amelyeket szeretnél. Az áthúzott szűrőgomb ki van kapcsolva, a pipával jelölt be. A keresés a bekapcsolt fajtákon dolgozik, és a választásodat a pilótáddal együtt megjegyzi a játék. Ha minden el van rejtve, a rács ezt kiírja, és felajánlja a **Minden kategória megjelenítése** gombot.

## Tárgy a tárgyba szerelés (alfoglalatok) {#item-to-item-equipping-sub-sockets-}

Egyes elsődleges tárgyak „felszerelhetnek” másodlagos támogató tárgyakat (ezt nevezzük alfoglalatba szerelésnek), hogy erősítsék a paramétereiket. Az alfoglalatba szereléshez húzd a támogató tárgyat közvetlenül az elsődleges tárgyra a hangár leltárában.

### Kompatibilitási táblázat {#compatibility-table}

| Elsődleges tárgy | Elfogadott alfoglalat-tárgyak | Eredmény |
| :--- | :--- | :--- |
| **Lézer** | Lézererősítő (Amp) | Növeli az alapsebzést és a kritikus találat értékeit |
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
