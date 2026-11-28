<!-- wiki-i18n source: 3c07d568f3af3aab -->
<!-- wiki-i18n title: Dormant Swamp -->
# Dormant Swamp

<!-- wiki-search: swamp; dormant swamp; base; turret; turrets; nike turret; laser turret; inert mass; unwakened; the unwakened; slumbering void; void; dormant lance; ds-4; mocsár; lövegtorony; lövegtornyok; löveg -->

Réges-rég egy fejlett civilizáció élt a galaxis közepén. Lilásfekete kristályból épített, világító ibolya erekkel, és ismeretlen okból összeomlott. A **Dormant Swamp** az előőrse, a `DS-4` bal felső sarkában. A szezon 11. napjától megmozdul: a középen lévő lövegek minden hajóra tüzelnek, amit látnak, az **Inert Massek** őrzik, és a legközepén alszik **az Unwakened**. Álca alatt eljuthatsz az Unwakenedig. Mióta megnyílt a [Deep Void](/wiki/03-Mechanics/Deep-Void.md), a lövegek és az Unwakened elpusztíthatók, és az Unwakened szezonbeli első leölése minden világban megnyitja annak a világnak a Thresholdját. Magába a bázisba nem lehet belépni, nem lehet megrohamozni, és kereskedni sem lehet vele.

A mocsárnál jelenik meg a 11. naptól a [Dormant-raj](/wiki/05-Swarms/Dormant-Swarm.md) is, és **Slumbering Voidok** járőröznek körülötte. Ugyanezek a Voidok hullámokban jönnek az [óriás kotrógépekhez](/wiki/03-Mechanics/Giant-Excavator.md#the-slumbering-voids). A szektorok itt vannak: [Veszélyes szektorok](/wiki/01-General/Danger-Sectors.md).

![Flying in towards the Dormant Swamp: the amber notice ring and, inside it, the red ring of the zone the guns reach](../../img/wiki-img/shots/swamp-rings.jpg)

## Dióhéjban {#at-a-glance}

<!-- swamp-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Hol**: A(z) `DS-4` bal felső sarka: a közepe itt van: 5 000 / 5 000
- **Megjelenik**: A szezon 11. napjától a wipe-ig
- **A zóna**: 4 300 egység a közép körül: ameddig a lövegek legfeljebb elérnek
- **A figyelmeztetés**: Az a hajó, amely átlépi a középtől 4 800 egységre lévő gyűrűt, rendszersort kap
- **Álca**: Egyetlen löveg sem lát soha álcázott hajót, sem EMP-ablakban lévőt
- **Az idegenek**: 5 Inert Mass marad a középtől 2 400 egységen belül. Az Unwakened a közepén alszik. 2 Slumbering Void járőrözik a középtől 4 600 és 6 500 egység között.
- **A Dormant-raj**: Itt jelenik meg: 9 417 / 6 606, a középtől 4 700 egységre, a zónán kívül
- **Sziklák**: Egyetlen aszteroida sem fekszik a középtől 4 900 egységen belül

<!-- swamp-glance:end -->

## A lövegek {#the-guns}

A mocsár lövegtornyai a **legközelebbi hajóra tüzelnek, amelyet látnak**, a hatótávolságukon belül, és semmilyen másikra: a zóna az a kör, amelyet a legtávolabbra érő közülük elér. Nem hajók, de amióta megnyílt a Deep Void, mindegyiknek van életereje: kattints egy lövegtoronyra, hogy a lézereiddel tüzelj rá, és a közelében szétrobbanó rakéta is sebzi. Egy elpusztított lövegtorony addig marad lent, amíg az Unwakened vissza nem tér. A lövéseik valódiak, és a világ úgy skálázza a sebzésüket, ahogy bármely idegen fegyverét.

<!-- swamp-guns:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Egy lövés sebzése, minden világban:

| Löveg | Hely | Tüzel | Hatótáv (egység) | Alpha | Beta | Gamma |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets)-lövegtorony | 5 000 / 4 400 | 2 mp | 3 640 | 75 000 | 112 500 | 150 000 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets)-lövegtorony | 5 000 / 4 400 | 5 mp | 1 080 | 50 000 | 75 000 | 100 000 |
| Lézertorony × 2 | 3 600 / 5 200; 6 400 / 5 200 | 1 mp | 2 500 | 45 000–55 000 | 67 500–82 500 | 90 000–110 000 |

- A rakétát annak a hatótávnak a 82% részénél lövik ki, amellyel ugyanez a rakéta a pilóták kezében rendelkezik, hogy odaérjen; a lézertorony másodpercenként egyszer tüzel, a sebzése a megadott tartományban dobódik.
- Egy N.I.K.E. pajzsáthatolása 35%, amelyet levonnak a pajzs elnyeléséből.
- A lövegtorony N.I.K.E. rakétája gyorsabb a tiédnél (25%), és messzebbre repül (2×): másodpercenként 1 250 egységet, összesen 8 910 egységet tesz meg, így a menekülő hajót hosszan üldözi.
- Egy N.U.K.E. 1 013 egység sugarú körben robban, középen a legerősebben.
- A lövegtorony N.U.K.E. rakétája gyorsabb a tiédnél (25%), és messzebbre repül (2×): másodpercenként 375 egységet, összesen 2 640 egységet tesz meg, így a menekülő hajót hosszan üldözi.

<!-- swamp-guns:end -->

- **A zónán kívülről semmi sem lő,** és benne egy hajó másodpercek alatt megsemmisül: minél közelebb ér a középhez, annál több löveg kapcsolódik be, és még a legjobban védett Wraith sem bírja. A már a levegőben lévő rakéta viszont tovább repül, és a lövegtorony rakétái gyorsabbak és messzebbre jutnak, mint a tieid: ha egyenesen elmenekülsz előlük, nem rázod le őket.
- **Az álca bejuttat.** Egyetlen lövegtorony sem lát soha álcázott hajót, sem EMP-ablakban lévőt, semmilyen távolságból. Egy látható hajóra célzott robbanás, amely egy álcázott hajó mellett robban, azt mégis megsebzi, és megszünteti az álcáját.
- **Csak pilótákra lőnek,** soha idegenekre, vállalati pilótákra vagy a rajra, és az éppen megsemmisülésből visszatért hajó védelme velük szemben is érvényes.
- **A figyelmeztető gyűrű.** A zónán kívüli gyűrűt átlépő hajó rendszersort kap: a lövegtornyok minden hajóra tüzelnek, amit látnak, és a közepén valami alszik. Újra csak akkor értesül, ha elhagyta a gyűrűt, és visszatért.
- **Kijutás.** Ha ott semmisülsz meg, nem térhetsz vissza helyben (a veszélyes szektor csak a bázist és a legközelebbi portált kínálja), és ha a zónában jelentkezel be, kívülre tesznek. Az általad kattintott útvonalat a játék a zóna köré hajlítja, és egy értesítés figyelmeztet, ha a kattintott hely beleesik.

## Az idegenek {#the-aliens}

Az elveszett civilizáció három idegene él itt, mindegyiknek megvannak a saját számai. Úgy fizetnek, mint egy raj főellensége: **az okozott sebzés szerint**, minden pilótának, aki legalább a [Rajok](/wiki/05-Swarms/Swarms.md#the-rules-of-every-swarm) oldalán megadott részt elérte, a láda pedig a legtöbb sebzést okozó pilótáé. A kilövéseik a PvE rangpontjaidat gyarapítják, mint egy rajhajóé, a fizetésükkel arányosan ([Rangok](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points)). Mindegyikük pajzsa egy találat {{guide:vitals.absorbance@Slumbering Void;Inert Mass;The Unwakened}}-át elnyeli, amíg tart ([Pajzsok](/wiki/03-Mechanics/Shields.md)).

- **Slumbering Void.** A karcsú vadász, a játék leggyorsabb idegene (gyorsabb, mint egy Storm Afterburner III-mal). Néhány mindig a mocsár környékét járőrözi, mások hullámokban érkeznek a kotrógépekhez. Agresszív, a legközelebbi pilótára vadászik, akit lát, és soha nem lát álcázott hajót.
- **Inert Mass.** Egy holt roncsóriás ibolya repedésekkel, egy kis állomás méretű. Állandó távolságon belül maradnak a mocsár közepétől, és egyelőre nem hagyják el. **Dormant Lance-eket** lő: nagyon nagy hatótávú, irányított rakétákat, amelyek követik a hajót, amíg az nem álcázza magát, nem nyit EMP-ablakot, nem lép biztonsági gyűrűbe, nem ugrik, vagy meg nem hal. Minden hajónál gyorsabb, ezért csak ezek a megszakítások segítenek. Egy aszteroida a Dormant Lance útjában megállítja azt, a Lance pedig a saját sebzésével rongálja az aszteroidát (ezért senki nem kap fizetséget), így egy szikla csak néhány találatig véd egy Inert Mass ellen.
- **Az Unwakened.** Egy monolit, amely a mocsár közepén alszik, a legnagyobb dolog bármely térképen, olyan lassú, hogy soha nem ér utol hajót. Semmit nem lő, de minden hajó, amely az aurájában van, elég, **álcázva vagy sem**. Amióta megnyílt a [Deep Void](/wiki/03-Mechanics/Deep-Void.md), elpusztítható: az okozott sebzés szerint fizet, egy nappal a halála után tér vissza, és minden világban a szezon első leölése megnyitja annak a világnak a Thresholdját. A pilóta **Sugárzástechnikája** csökkenti az égetést, a 100. szinten annak 0,40-szeresére.

<!-- swamp-members:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

### Slumbering Void

2 Slumbering Void járőrözik a mocsár közepétől 4 600 és 6 500 egység között; amelyik megsemmisül, {{guide:vitals.respawn@Slumbering Void}} múlva visszatér. A kotrógép hullámai ugyanebből az idegenből hoznak többet.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | {{guide:vitals.hull@Slumbering Void}} | {{guide:vitals.hull*1.5@Slumbering Void}} | {{guide:vitals.hull*2@Slumbering Void}} |
| Pajzs | {{guide:vitals.shield@Slumbering Void}} | {{guide:vitals.shield*1.5@Slumbering Void}} | {{guide:vitals.shield*2@Slumbering Void}} |
| Pajzs elnyelése | {{guide:vitals.absorbance@Slumbering Void}} | {{guide:vitals.absorbance@Slumbering Void}} | {{guide:vitals.absorbance@Slumbering Void}} |
| Lézersebzés (másodpercenként egy sorozat) | {{guide:vitals.dps@Slumbering Void}} | {{guide:vitals.dps*1.5@Slumbering Void}} | {{guide:vitals.dps*2@Slumbering Void}} |
| Sebesség | {{guide:vitals.speed@Slumbering Void}} | {{guide:vitals.speed@Slumbering Void}} | {{guide:vitals.speed@Slumbering Void}} |
| Lézer hatótávja | 800 | 800 | 800 |
| Aggrósugár | {{guide:vitals.aggro@Slumbering Void}} | {{guide:vitals.aggro@Slumbering Void}} | {{guide:vitals.aggro@Slumbering Void}} |
| Kredit | {{guide:spoils.pay.credits@Slumbering Void}} | {{guide:spoils.pay.credits*2@Slumbering Void}} | {{guide:spoils.pay.credits*3@Slumbering Void}} |
| Thulium | {{guide:spoils.pay.thulium@Slumbering Void}} | {{guide:spoils.pay.thulium*2@Slumbering Void}} | {{guide:spoils.pay.thulium*3@Slumbering Void}} |
| Tapasztalat (XP) | {{guide:spoils.pay.experience@Slumbering Void}} | {{guide:spoils.pay.experience*2@Slumbering Void}} | {{guide:spoils.pay.experience*3@Slumbering Void}} |
| Becsület | {{guide:spoils.pay.honor@Slumbering Void}} | {{guide:spoils.pay.honor*2@Slumbering Void}} | {{guide:spoils.pay.honor*3@Slumbering Void}} |
| PvE-pont kilövésenként | 10 | 10 | 10 |

**Zsákmány**: egy láda, annak a pilótának, aki a legtöbb sebzést okozta.

| Tárgy |
| :--- |
| {{guide:spoils.box@Slumbering Void}} |

### Inert Mass

5 Inert Mass áll a középtől 2 400 egységen belül; amelyik megsemmisül, {{guide:vitals.respawn@Inert Mass}} múlva visszatér. 6 mp időnként irányított [Dormant Lance](/wiki/06-Items/Rockets.md#the-craft-only-rockets)-et lő a legközelebbi hajóra, amelyet lát: sebesség 750, 5 250 egységnyi repülés, 40% áthatolás.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | {{guide:vitals.hull@Inert Mass}} | {{guide:vitals.hull*1.5@Inert Mass}} | {{guide:vitals.hull*2@Inert Mass}} |
| Pajzs | {{guide:vitals.shield@Inert Mass}} | {{guide:vitals.shield*1.5@Inert Mass}} | {{guide:vitals.shield*2@Inert Mass}} |
| Pajzs elnyelése | {{guide:vitals.absorbance@Inert Mass}} | {{guide:vitals.absorbance@Inert Mass}} | {{guide:vitals.absorbance@Inert Mass}} |
| Egy Dormant Lance sebzése | {{guide:behaviour.ability:rocket.damageMin@Inert Mass}}–{{guide:behaviour.ability:rocket.damage@Inert Mass}} | {{guide:behaviour.ability:rocket.damageMin*1.5@Inert Mass}}–{{guide:behaviour.ability:rocket.damage*1.5@Inert Mass}} | {{guide:behaviour.ability:rocket.damageMin*2@Inert Mass}}–{{guide:behaviour.ability:rocket.damage*2@Inert Mass}} |
| Sebesség | {{guide:vitals.speed@Inert Mass}} | {{guide:vitals.speed@Inert Mass}} | {{guide:vitals.speed@Inert Mass}} |
| Rakéta hatótávja | 5 000 | 5 000 | 5 000 |
| Aggrósugár | {{guide:vitals.aggro@Inert Mass}} | {{guide:vitals.aggro@Inert Mass}} | {{guide:vitals.aggro@Inert Mass}} |
| Kredit | {{guide:spoils.pay.credits@Inert Mass}} | {{guide:spoils.pay.credits*2@Inert Mass}} | {{guide:spoils.pay.credits*3@Inert Mass}} |
| Thulium | {{guide:spoils.pay.thulium@Inert Mass}} | {{guide:spoils.pay.thulium*2@Inert Mass}} | {{guide:spoils.pay.thulium*3@Inert Mass}} |
| Tapasztalat (XP) | {{guide:spoils.pay.experience@Inert Mass}} | {{guide:spoils.pay.experience*2@Inert Mass}} | {{guide:spoils.pay.experience*3@Inert Mass}} |
| Becsület | {{guide:spoils.pay.honor@Inert Mass}} | {{guide:spoils.pay.honor*2@Inert Mass}} | {{guide:spoils.pay.honor*3@Inert Mass}} |
| PvE-pont kilövésenként | 15 | 15 | 15 |

**Zsákmány**: egy láda, annak a pilótának, aki a legtöbb sebzést okozta.

| Tárgy |
| :--- |
| {{guide:spoils.box@Inert Mass}} |

### The Unwakened

Egy van belőle, a mocsár közepén és sehol máshol; megsemmisítése után {{guide:vitals.respawn@The Unwakened}} múlva visszatér. Amióta megnyílt a Deep Void, elpusztítható, és a többi itteni idegenhez hasonlóan az okozott sebzés szerint fizet.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | {{guide:vitals.hull@The Unwakened}} | {{guide:vitals.hull*1.5@The Unwakened}} | {{guide:vitals.hull*2@The Unwakened}} |
| Pajzs | {{guide:vitals.shield@The Unwakened}} | {{guide:vitals.shield*1.5@The Unwakened}} | {{guide:vitals.shield*2@The Unwakened}} |
| Pajzs elnyelése | {{guide:vitals.absorbance@The Unwakened}} | {{guide:vitals.absorbance@The Unwakened}} | {{guide:vitals.absorbance@The Unwakened}} |
| Aurasebzés másodpercenként minden bent lévő hajónak | {{guide:behaviour.ability:aura.damagePerSecond@The Unwakened}} | {{guide:behaviour.ability:aura.damagePerSecond*1.5@The Unwakened}} | {{guide:behaviour.ability:aura.damagePerSecond*2@The Unwakened}} |
| Aura sugara | 700 | 700 | 700 |
| Sebesség | {{guide:vitals.speed@The Unwakened}} | {{guide:vitals.speed@The Unwakened}} | {{guide:vitals.speed@The Unwakened}} |
| Aggrósugár | {{guide:vitals.aggro@The Unwakened}} | {{guide:vitals.aggro@The Unwakened}} | {{guide:vitals.aggro@The Unwakened}} |
| Kredit | {{guide:spoils.pay.credits@The Unwakened}} | {{guide:spoils.pay.credits*2@The Unwakened}} | {{guide:spoils.pay.credits*3@The Unwakened}} |
| Thulium | {{guide:spoils.pay.thulium@The Unwakened}} | {{guide:spoils.pay.thulium*2@The Unwakened}} | {{guide:spoils.pay.thulium*3@The Unwakened}} |
| Tapasztalat (XP) | {{guide:spoils.pay.experience@The Unwakened}} | {{guide:spoils.pay.experience*2@The Unwakened}} | {{guide:spoils.pay.experience*3@The Unwakened}} |
| Becsület | {{guide:spoils.pay.honor@The Unwakened}} | {{guide:spoils.pay.honor*2@The Unwakened}} | {{guide:spoils.pay.honor*3@The Unwakened}} |
| PvE-pont kilövésenként | 112 | 112 | 112 |

**Zsákmány**: egy láda, annak a pilótának, aki a legtöbb sebzést okozta.

| Tárgy |
| :--- |
| {{guide:spoils.box@The Unwakened}} |

<!-- swamp-members:end -->

## A Deep Voiddal {#with-the-deep-void}

Amit a Deep Void itt megváltoztatott, röviden:

- **Az Unwakened elpusztítható.** Már nem sebezhetetlen: a többi itteni idegenhez hasonlóan az okozott sebzés szerint fizet, és egy nappal a halála után tér vissza.
- **A lövegek elpusztíthatók.** A három löveg (a rakétatorony, amely a N.I.K.E.-t és a N.U.K.E.-t is kilövi, és a két lézertorony) mindegyikének most már van életereje, és a lézerek és a rakéták sebzik őket. Egy elpusztított löveg addig marad lent, amíg az Unwakened vissza nem tér.
- **Az első leölés megnyitja a Thresholdot.** Minden világban az Unwakened szezonbeli első leölése megnyitja annak a világnak a Thresholdját a `DS-4` átellenes sarkában, ahol a [Deep Void](/wiki/03-Mechanics/Deep-Void.md) kezdődik.

## Mit csinálj itt {#what-to-do-here}

- **Az első leölés megnyitja az utat.** Az Unwakened szezonbeli első leölése megnyitja a világának Thresholdját, és vele az utat a [Deep Void](/wiki/03-Mechanics/Deep-Void.md) felé; a zónán belül a lövegek másodpercek alatt elpusztítanak egy hajót. A zónán kívül a zóna körül gyűrűben járőröző Voidok a mocsár első vonala, és az a hely, ahol egy csoport a lövegek nélkül harcolhat.
- **A Voidokkal áthatolással harcolj.** A Void nagy pajzsa egy találat {{guide:vitals.absorbance@Slumbering Void;Inert Mass;The Unwakened}}-át elnyeli, és szinte mellékes: a mögötte lévő hajótest kicsi. Minél több pajzsáthatolása van a lézereidnek, annál előbb esik el ([Lézerek és lőszer](/wiki/06-Items/Lasers.md)).
- **Maradj távol a Lance-ektől.** Egy Inert Mass messzire lát, és egy Lance elől nem lehet elfutni: törd meg a tapadását álcával, EMP-vel, biztonsági gyűrűvel vagy ugrással, vagy hagyd el a hatótávját. Egy Mass hosszú harc még a legerősebb hajók nagy csoportjának is.
- **A Dormant-raj** mostantól közvetlenül a zónán kívül jelenik meg, így egy csoport a lövegek nélkül várhatja. Lásd: [Dormant-raj](/wiki/05-Swarms/Dormant-Swarm.md).

## Hol olvass tovább {#where-to-read-more}

- [Veszélyes szektorok](/wiki/01-General/Danger-Sectors.md): mi változott a 11. napon.
- [Óriás kotrógép](/wiki/03-Mechanics/Giant-Excavator.md): a Slumbering Voidok hullámai és amit védenek.
- [Rajok](/wiki/05-Swarms/Swarms.md) és [Dormant-raj](/wiki/05-Swarms/Dormant-Swarm.md): így fizet egy főellenség kilövése.
- [Rakéták](/wiki/06-Items/Rockets.md#the-craft-only-rockets): a N.I.K.E. és a N.U.K.E., amelyet a lövegtorony lő.
- [Feketelyuk](/wiki/03-Mechanics/Black-Hole.md): a `DS-4` másik veszélye.
- [Rakományládák](/wiki/03-Mechanics/Cargo.md): a ládák, amelyeket az idegenek ejtenek.
