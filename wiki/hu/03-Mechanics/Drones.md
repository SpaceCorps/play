<!-- wiki-i18n source: e65164e763773d17 -->
<!-- wiki-i18n title: Drónok -->
# Drónmechanika {#drone-mechanics}

A drónok önálló támogató egységek, amelyek a hajód mellett repülnek. További felszerelési foglalatokat adnak, és közvetlenül hozzájárulnak a hajód harci teljesítményéhez. A Slave Drone fejlődik is: minden alkalommal tapasztalatot szerez, amikor megsemmisítesz egy idegent, és **nyolc szinten** halad végig, a kis páncélozott gömbtől a félhold alakú szárnyú rohamhajóig. A Gyártásban egy Slave Drone **Master Drone**-ná fejleszthető, amelynek a szintjei újrakezdődnek (lásd lent: Master Drone). A drónok azt is lehetővé teszik, hogy **drónformációt** viselj: csak akkor működik, ha legalább egy drón van a flottádban (lásd: [Drónformációk](/wiki/03-Mechanics/Formations.md)).

![Emergency Repair: repair drones beam the hull](../../img/wiki-img/shots/emergency-repair.jpg)

## Drónok beszerzése {#getting-drones}

Minden drón, amelyet birtokolsz, akár **Slave Drone**, akár Master Drone, megnyitja a saját drónfoglalatait (a Slave Drone egyet, a Master Drone kettőt), legfeljebb **8** drónig. A Bolt Slave Drone-okat árul kreditért, a negyediktől kezdve Thuliumért is. Mindegyik többe kerül az előzőnél: az árak a [Drónok](/wiki/06-Items/Drones.md) oldalon vannak.

## Repülési elrendezés és mozgás {#formation-movement}

A drónok egy szokásos **„Wingman” elrendezésben (2–2–4)** repülnek:

- **2 drón** a hajó mellett, egy-egy a két oldalán.
- **2 drón** mellette és kicsit mögötte.
- **4 drón** mögötte, a nyomában.

Sima követési algoritmust használnak, amely a hajód sebessége és elfordulása alapján igazítja a helyzetüket, éles manőverek közben összeszorítva az elrendezést. Senki sem repül előtted.

A drónok kicsik, és közel maradnak: egy 8. szintű drón körülbelül 19,5 egység átmérőjű (egy Protos 50), egy 1. szintű drón pedig egy körülbelül 8 egység átmérőjű gömb, így az egész elrendezés nagyjából 135 egységen belül elfér a hajódtól. Az a drón, amelyet először vettél, rendelkezik a legtöbb tapasztalattal, és a bal oldaladon repül, a második a jobbon, a legújabbak pedig hátul követnek.

Ez az elrendezés csak a drónok megjelenése, és ugyanaz, bármelyik [drónformációt](/wiki/03-Mechanics/Formations.md) viseled. A drónformáció bónuszok és árak összessége, nem a repülésnek egy másik módja.

## Felszerelés és értékek {#equipment-stats}

A drónok a hajód bővítő felszerelésállványaiként működnek.

- Egy Slave Drone-nak **1 foglalata** van, egy Master Drone-nak **2**, legfeljebb **8 drónig**.
- Ezekbe a foglalatokba **lézereket** és **pajzsokat** szerelhetsz, egy Master Drone mindkét foglalatába is. Más nem fér be: se hajtómű, se adaptív mag.
- **A lézerek teljes értékkel számítanak.** A drónon lévő lézer akkor tüzel, amikor te tüzelsz, hozzáadja a sebzését a sortűzedhez, és lőszert használ, mint bármelyik másik lézer (minden lézer sortűzenként egy töltet lőszert éget el). Egy Master Drone két lézere két lézernek számít.
- **A pajzsok is teljes értékkel számítanak.** A drónon lévő pajzs úgy számít, mint a magfoglalatban lévő, bármelyik foglalatban: a kapacitása és a töltődése a celláival együtt, az elnyelése a hajód átlagában, a pajzsbónusza és a lassulása. A hajód saját pajzsaival együtt aszerint sorolják be, hogy mi számít belőle a foglalat részesedése után (a drón foglalata 100%-ot számít; a négy legjobb teljes értékkel számít, az ötödik és a további kevesebbel, lásd: [Pajzsmechanika](/wiki/03-Mechanics/Shields.md)), és a Kovácsműhely buffjai, a Szezonbolt buffjai és a támadó pajzsáthatolása úgy hat rá, mint bármelyik pajzsra. A drón szintje csak a lézerét növeli, a pajzsát sosem. Amíg egy drónt fejlesztenek, a foglalatai offline vannak, a pajzs éppúgy, mint a lézer. A 0.4.7-es verzió előtt a drónon lévő pajzs semmit sem adott.
- **Lézer vagy pajzs?** Egy foglalatba az egyik vagy a másik fér: a lézer egy lézert ad a sortűzedhez, a pajzs a pajzspontjait adja. Egy kis hajón, jó pajzsokkal a plusz pontok keveset adnak, mert előbb elfogy a hajótest; nagy hajótesten viszont sokkal többet bírsz ki velük.
- **A formációnak drón kell, nem foglalat.** A [drónformáció](/wiki/03-Mechanics/Formations.md) addig működik, amíg van legalább egy drónod. Nem foglal el drónfoglalatot, és a drónok száma, a szintjük és az, hogy mit hordoznak, nem változtat rajta.

## Szintek {#levels}

Minden Slave Drone az 1. szinten indul, és tapasztalatot (XP) szerez, valahányszor megsemmisítesz egy idegent. A Master Drone is az 1. szinten indul, XP nélkül, és ugyanúgy szintet lép. Minden szint többet kér az előzőnél, és a külseje is változik vele, így látod, meddig jutott egy drón. A táblázat minden szintnél megadja, mennyi XP kell az előző szintről idáig feljutni, és hogy ez hány kilövést jelent egyetlen idegenfajtából önmagában (az Alpha világban; a Beta világban nagyjából feleannyi, a Gammában nagyjából harmadannyi kell):

<!-- drones:begin -->
<!-- Generated from server/Resources/drone-levels.json by scripts/drones-wiki.sh: don't edit by hand. -->

- **1. szint, Mag:** egy kis páncélozott gömb egyetlen ciánkék lencsével.
- **2. szint, Halo:** a gömb egy lebegő gyűrűben.
- **3. szint, Korong:** egy lapos korong egy üvegkupola alatt.
- **4. szint, Csészealj:** egy csészealj páncéllemezekkel és légbeömlőkkel.
- **5. szint, Rohamhajó:** a csészealjhoz egy orr és két ágyú csatlakozik.
- **6. szint, Szárnyrügyek:** ágyúk és rövid szárnylapátok tartóoszlopokon.
- **7. szint, Félszárnyak:** hosszabb szárnylapátok arany hegyekkel.
- **8. szint, Félhold:** a kész rohamhajó: teljes félholdszárnyak ciánkék fénycsíkokkal.

| Szint | Elérendő XP | XP a szinthez | Lézersebzés | Seeker kilövés | Bulwark kilövés | Goombah kilövés |
| --: | --: | --: | --: | --: | --: | --: |
| 1 | 0 | – | – | – | – | – |
| 2 | 350 | 350 | – | 350 | 44 | 15 |
| 3 | 900 | 550 | +1% | 550 | 69 | 23 |
| 4 | 2 000 | 1 100 | +2% | 1 100 | 138 | 46 |
| 5 | 3 700 | 1 700 | +3% | 1 700 | 213 | 71 |
| 6 | 6 000 | 2 300 | +4% | 2 300 | 288 | 96 |
| 7 | 9 500 | 3 500 | +5% | 3 500 | 438 | 146 |
| 8 | 14 000 | 4 500 | +7% | 4 500 | 563 | 188 |

| Idegen | XP drónonként |
| :--- | --: |
| Seeker | 1 |
| Phantasm | 2 |
| Bulwark | 8 |
| Goombah | 24 |
| Crystalys | 72 |

<!-- drones:end -->

### Hogyan szereznek XP-t a drónok {#how-drones-earn-xp}

- **Minden birtokodban lévő drón ugyanannyi XP-t szerez** minden olyan idegenkilövésért, amelyért jutalmat kapsz: az első 8 drón, akár hordoz lézert, akár nem. Az a drón, amelyet később veszel, az 1. szinten indul, XP nélkül, ezért az első drónjaid mindig a legmagasabb szintűek.
- **A keményebb idegenek többet érnek.** Az idegenek által adott XP a fenti második táblázatban van (egy Crystalys 72 Seekert ér). Minden más idegen 1-et ad.
- **A világok többet fizetnek.** A Beta megduplázza az XP-t, a Gamma megháromszorozza (az ottani idegeneknek több életerejük is van). A boosterek és a Prémium nem változtatnak rajta.
- **A kilövés akkor számít, ha fizet neked.** Az az idegen, amelyet úgy lősz ki, hogy egy másik pilóta tartja a foglalását, semmit sem fizet a drónjaidnak, ahogy neked sem. A pilótakilövések, a küldetések és a vállalati pilóták saját kilövései nem adnak drón-XP-t.
- **A 8. szint az utolsó.** Az XP ezután is számolódik.

### Mit ad egy szint {#what-a-level-gives}

A **drón foglalatába szerelt lézer** több alapsebzést okoz, ahogy a drón szintet lép: az 1. és a 2. szinten semmivel, aztán a 3. szinten +1%-kal, és egészen **+7%-kal a 8. szinten**. A bónusz a lézer saját sebzését szorozza (a bűvölési fokozatának hatása után); a beleszerelt erősítők ráadásként hozzáadódnak, és nincsenek megszorozva. A hangár megmutatja minden drón szintjét, az XP-sávját és azt, hogy a következő szinthez hány kilövés kell, a mutatott sebzésértékek pedig már tartalmazzák a bónuszt. Ha egy drón szintet lép, a Játéknapló jelzi („2. drón szintet lépett: 4. szint.”), és a drón egy fénygyűrűvel felvillan.

### Mennyi ideig tart {#how-long-it-takes}

A görbe úgy van beállítva, hogy egy új drón nagyjából egy óra normál játékkal (Bulwark és Goombah idegenek vadászatával) éri el a 2. szintet, a 8. szintet pedig nagyjából 27 játékórával. Ezek az órák arra a pilótára vonatkoznak, aki az első drónt nagyjából a 7. szintű küldetéseknél veszi meg; gyengébb felszereléssel tovább tart (a 2. szinthez legfeljebb nagyjából 4 óra, a 8. szinthez nagyjából 150). Ha egyetlen idegenfajtára vadászol, az legfeljebb nagyjából másfélszer olyan gyors, mint egy normál keverék. A drónok a szintjükkel és a tapasztalatukkal együtt megmaradnak a szezon wipe-ja után, így ezeket az órákat csak egyszer kell ledolgozni, annyi szezonon át, amennyi kell: aki napi fél órát játszik, pár szezon alatt eljut odáig.

### Master Drone

Egy Slave Drone **Master Drone**-ná válik, ha a Gyártásban továbbfejleszted, miután a Master Drone technológiáját kikutattad ([Kutatás](/wiki/03-Mechanics/Research.md)). A recept ára 40 000 Thulium és 100 Ship Fragment, 60 másodpercig tart, és nem használ el drónt: **te választod ki, melyik Slave Drone legyen** (a választó mutatja mindegyik szintjét és XP-jét), és ugyanaz a drón a sorszámával, a drónfoglalatával és mindennel, ami beleszerelve van, Master Drone-ná alakul, amikor a munka véget ér, egy második, üres foglalattal. A leltáradba nem kerül semmi, és nincs mit átvenni: a Játéknapló jelzi, ha elkészült, akkor is, ha a fejlesztés olyankor fejeződött be, amikor nem voltál ott.

**A szintje és az XP-je 0-ra áll vissza, amikor a fejlesztés véget ér.** A Master Drone újra az 1. szinten indul, XP nélkül, és úgy lép szintet, ahogy a Slave Drone (lásd a fenti táblázatot); az addigi szintjével járó lézerbónusz is elvész. A Gyártás indítás előtt szól erről, és megerősítést kér, megnevezve a drónt, ha van XP-je. Az alapértelmezett választás a legkevesebb XP-vel rendelkező drón.

Amíg a fejlesztés tart, a drón zárolva van: nem fejlesztheted újra, és nem törölheted, a foglalata pedig **offline**, ezért a benne lévő lézer nem tüzel, amíg a munka véget nem ér (addig még egy egyfoglalatos Slave Drone). A többi munkád mögé kerül a sorban, mint bármely gyártás.

A Master Drone is a legfeljebb 8 drónod egyike: beleszámít a drónlimitbe és a következő Slave Drone árába, így a fejlesztés egyiket sem változtatja, és a szintjével és az XP-jével együtt megmarad a szezon wipe-ja után. Repülés közben ő a kész rohamhajó, aranyban. Egy Master Drone-nak **két felszerelési foglalata** van ott, ahol egy Slave Drone-nak egy: mindkettőbe lézer vagy pajzs kerülhet, és a szintbónusz bármelyikben lévő lézerre vonatkozik. Egyébként Slave Drone: ugyanaz a nyolc szint és ugyanaz a lézerbónusz. Azok a Master Drone-ok, amelyeket még a második foglalat előtt készítettél, most megkapták, és amit addig hordoztak, az ott marad, ahol volt. Azok a Master Drone-ok, amelyeket a helyben történő fejlesztés bevezetése előtt gyártottak, hétköznapi tárgyak a leltáradban, és nem repülnek.

## Harci viselkedés {#combat-behavior}

- **Lézerek**: a drónok a felszerelt lézereikkel a célba vett célpontodra tüzelnek.
- **Sebzés**: a drónok sérülhetnek (ha külön entitáslogika létezik; jelenleg többnyire a hajó közös készletén osztoznak, de vizuálisan különállóak). _Megjegyzés: jelenleg a drónok a hajó elpusztíthatatlan kiterjesztései._
- **Repair Drone-ok**: a Repair Drone tárgyak (I–IV) [extrák](/wiki/06-Items/Extras.md#repair-drones), nem a flottád drónjai. Amíg az egyik javítja a hajótestedet, kis javítódrónok repülnek ki a hajóból, körbeszállják és sugárral érik, és a közelben lévő pilóták látják őket.
