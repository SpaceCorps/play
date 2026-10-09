<!-- wiki-i18n source: a8a96edb9a5070f1 -->
<!-- wiki-i18n title: Dormant Swamp -->
# Dormant Swamp

<!-- wiki-search: swamp; dormant swamp; base; turret; turrets; nike turret; laser turret; inert mass; unwakened; the unwakened; slumbering void; void; dormant lance; ds-4; mocsár; lövegtorony; lövegtornyok; löveg -->

Réges-rég egy fejlett civilizáció élt a galaxis közepén. Lilásfekete kristályból épített, világító ibolya erekkel, és ismeretlen okból összeomlott. A **Dormant Swamp** az előőrse, a `DS-4` bal felső sarkában. A szezon 11. napjától megmozdul: a középen lévő lövegek minden hajóra tüzelnek, amit látnak, az **Inert Massek** őrzik, és a legközepén alszik **az Unwakened**. Ez egy olyan hely, amelyet a pilótáknak **még nem szabad meglátogatniuk**. Álca alatt eljuthatsz az Unwakenedig, és egyelőre semmi mást nem lehet ott tenni: a bázist és a lövegeit nem lehet megrongálni, belépni, megrohamozni vagy velük kereskedni.

A mocsárnál jelenik meg a 11. naptól a [Dormant-raj](/wiki/05-Swarms/Dormant-Swarm.md) is, és **Slumbering Voidok** járőröznek körülötte. Ugyanezek a Voidok hullámokban jönnek az [óriás kotrógépekhez](/wiki/03-Mechanics/Giant-Excavator.md#the-slumbering-voids). A szektorok itt vannak: [Veszélyes szektorok](/wiki/01-General/Danger-Sectors.md).

## Dióhéjban {#at-a-glance}

<!-- swamp-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Hol**: A(z) `DS-4` bal felső sarka: a közepe itt van: 5 000 / 5 000
- **Megjelenik**: A szezon 11. napjától a wipe-ig
- **A zóna**: 4 300 egység a közép körül: ameddig a lövegek legfeljebb elérnek, és az a hely, amelyet még senkinek sem kell meglátogatnia
- **A figyelmeztetés**: Az a hajó, amely átlépi a középtől 4 800 egységre lévő gyűrűt, rendszersort kap
- **Álca**: Egyetlen löveg sem lát soha álcázott hajót, sem EMP-ablakban lévőt
- **Az idegenek**: 5 Inert Mass marad a középtől 2 400 egységen belül. Az Unwakened a közepén alszik. 2 Slumbering Void járőrözik a középtől 4 600 és 6 500 egység között.
- **A Dormant-raj**: Itt jelenik meg: 9 417 / 6 606, a középtől 4 700 egységre, a zónán kívül
- **Sziklák**: Egyetlen aszteroida sem fekszik a középtől 4 900 egységen belül

<!-- swamp-glance:end -->

## A lövegek {#the-guns}

A mocsár lövegtornyai a **legközelebbi hajóra tüzelnek, amelyet látnak**, a hatótávolságukon belül, és semmilyen másikra: a zóna az a kör, amelyet a legtávolabbra érő közülük elér. Nem entitások semmilyen értelemben: nincs életerejük, nem lehet célpontul választani őket, és semmi, amit rájuk lősz, nem hat. A lövéseik valódiak, és a világ úgy skálázza a sebzésüket, ahogy bármely idegen fegyverét.

<!-- swamp-guns:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Egy lövés sebzése, minden világban:

| Löveg | Hely | Tüzel | Hatótáv (egység) | Alpha | Beta | Gamma |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets)-lövegtorony | 5 000 / 4 400 | 2 mp | 3 640 | 75 000 | 112 500 | 150 000 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets)-lövegtorony | 5 000 / 4 400 | 5 mp | 1 080 | 50 000 | 75 000 | 100 000 |
| Lézertorony × 2 | 3 600 / 5 200; 6 400 / 5 200 | 1 mp | 2 500 | 45 000–55 000 | 67 500–82 500 | 90 000–110 000 |

- A rakétát a hatótávja 90% részénél lövik ki, hogy odaérjen; a lézertorony másodpercenként egyszer tüzel, a sebzése a megadott tartományban dobódik.
- Egy N.I.K.E. pajzsáthatolása 35%, amelyet levonnak a pajzs elnyeléséből.
- Egy N.U.K.E. 900 egység sugarú körben robban, középen a legerősebben.

<!-- swamp-guns:end -->

- **Semmi sem ér túl a zónán,** és benne egy hajó másodpercek alatt megsemmisül: minél közelebb ér a középhez, annál több löveg kapcsolódik be, és még a legjobban védett Wraith sem bírja.
- **Az álca bejuttat.** Egyetlen lövegtorony sem lát soha álcázott hajót, sem EMP-ablakban lévőt, semmilyen távolságból. Egy látható hajóra célzott robbanás, amely egy álcázott hajó mellett robban, azt mégis megsebzi, és megszünteti az álcáját.
- **Csak pilótákra lőnek,** soha idegenekre, vállalati pilótákra vagy a rajra, és az éppen megsemmisülésből visszatért hajó védelme velük szemben is érvényes.
- **A figyelmeztető gyűrű.** A zónán kívüli gyűrűt átlépő hajó rendszersort kap: a lövegtornyok minden hajóra tüzelnek, amit látnak, és a közepén valami alszik. Újra csak akkor értesül, ha elhagyta a gyűrűt, és visszatért.
- **Kijutás.** Ha ott semmisülsz meg, és helyben élsz újra, vagy a zónában jelentkezel be, kívülre tesznek. Az általad kattintott útvonalat a játék a zóna köré hajlítja, és egy értesítés figyelmeztet, ha a kattintott hely beleesik.

## Az idegenek {#the-aliens}

Az elveszett civilizáció három idegene él itt, mindegyiknek megvannak a saját számai. Úgy fizetnek, mint egy raj főellensége: **az okozott sebzés szerint**, minden pilótának, aki legalább a [Rajok](/wiki/05-Swarms/Swarms.md#the-rules-of-every-swarm) oldalán megadott részt elérte, a láda pedig a legtöbb sebzést okozó pilótáé. A kilövéseik a PvE rangpontjaidat gyarapítják, mint egy rajhajóé, a fizetésükkel arányosan ([Rangok](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points)). Mindegyikük pajzsa egy találat 80 %-át elnyeli, amíg tart ([Pajzsok](/wiki/03-Mechanics/Shields.md)).

- **Slumbering Void.** A karcsú vadász, a játék leggyorsabb idegene (olyan gyors, mint egy Storm Afterburner III-mal). Néhány mindig a mocsár környékét járőrözi, mások hullámokban érkeznek a kotrógépekhez. Agresszív, a legközelebbi pilótára vadászik, akit lát, és soha nem lát álcázott hajót.
- **Inert Mass.** Egy holt roncsóriás ibolya repedésekkel, egy kis állomás méretű. Állandó távolságon belül maradnak a mocsár közepétől, és egyelőre nem hagyják el. **Dormant Lance-eket** lő: nagyon nagy hatótávú, irányított rakétákat, amelyek követik a hajót, amíg az nem álcázza magát, nem nyit EMP-ablakot, nem lép biztonsági gyűrűbe, nem ugrik, vagy meg nem hal. Minden hajónál gyorsabb, ezért csak ezek a megszakítások segítenek.
- **Az Unwakened.** Egy monolit, amely a mocsár közepén alszik, a legnagyobb dolog bármely térképen, olyan lassú, hogy soha nem ér utol hajót. Semmit nem lő, de minden hajó, amely az aurájában van, elég, **álcázva vagy sem**. **Immunis**: a lövések és a rakéták eltalálják, és nem csinálnak semmit, a célablak teli sávokat és az Immunis szót mutatja. Egy későbbi esemény lehetővé teszi majd a leküzdését; az alábbi jutalmai fel vannak jegyezve, és még nem szerezhetők meg.

<!-- swamp-members:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

### Slumbering Void

2 Slumbering Void járőrözik a mocsár közepétől 4 600 és 6 500 egység között; amelyik megsemmisül, 1 óra múlva visszatér. A kotrógép hullámai ugyanebből az idegenből hoznak többet.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | 25 000 | 37 500 | 50 000 |
| Pajzs | 150 000 | 225 000 | 300 000 |
| Pajzs elnyelése | 80% | 80% | 80% |
| Lézersebzés (másodpercenként egy sorozat) | 3 000 | 4 500 | 6 000 |
| Sebesség | 400 | 400 | 400 |
| Lézer hatótávja | 800 | 800 | 800 |
| Aggrósugár | 2 500 | 2 500 | 2 500 |
| Kredit | 23 000 | 46 000 | 69 000 |
| Thulium | 60 | 120 | 180 |
| Tapasztalat (XP) | 3 600 | 7 200 | 10 800 |
| Becsület | 16 | 32 | 48 |
| PvE-pont kilövésenként | 10 | 10 | 10 |

**Zsákmány**: egy láda, annak a pilótának, aki a legtöbb sebzést okozta.

| Tárgy | Esély | Mennyiség |
| :--- | ---: | ---: |
| Egy a következők közül: Ultra Core és Experimental Fusion Core, véletlenszerűen | 60% | 30–60 |
| Egy a 4 Epikus [rakéta](/wiki/06-Items/Rockets.md) közül, véletlenszerűen | 40% | 1–3 |

### Inert Mass

5 Inert Mass áll a középtől 2 400 egységen belül; amelyik megsemmisül, 1 óra múlva visszatér. 6 mp időnként irányított [Dormant Lance](/wiki/06-Items/Rockets.md#the-craft-only-rockets)-et lő a legközelebbi hajóra, amelyet lát: sebesség 750, 5 250 egységnyi repülés, 40% áthatolás.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | 250 000 | 375 000 | 500 000 |
| Pajzs | 100 000 | 150 000 | 200 000 |
| Pajzs elnyelése | 80% | 80% | 80% |
| Egy Dormant Lance sebzése | 5 000–8 000 | 7 500–12 000 | 10 000–16 000 |
| Sebesség | 60 | 60 | 60 |
| Rakéta hatótávja | 5 000 | 5 000 | 5 000 |
| Aggrósugár | 5 000 | 5 000 | 5 000 |
| Kredit | 125 000 | 250 000 | 375 000 |
| Thulium | 335 | 670 | 1 005 |
| Tapasztalat (XP) | 20 200 | 40 400 | 60 600 |
| Becsület | 88 | 176 | 264 |
| PvE-pont kilövésenként | 15 | 15 | 15 |

**Zsákmány**: egy láda, annak a pilótának, aki a legtöbb sebzést okozta.

| Tárgy | Esély | Mennyiség |
| :--- | ---: | ---: |
| Ultra Core és Experimental Fusion Core, egyenlően elosztva | 100% | összesen 400–800 |
| Egy a 4 Epikus [rakéta](/wiki/06-Items/Rockets.md) közül, véletlenszerűen | 100% | 20–40 |
| N.I.K.E. | 5% | 1–2 |
| Dark Matter | 5% | 1–3 |
| Ancient Control Unit | 10% | 1 |
| Power Core | 25% | 1–2 |

### The Unwakened

Egy van belőle, a mocsár közepén és sehol máshol; megsemmisítése után 24 óra múlva visszatér. **Immunis**, amíg egy későbbi küldetés ki nem kapcsolja a jelzőt: a lövések és a rakéták eltalálják, és nem csinálnak semmit. A jutalmai fel vannak jegyezve, és még nem szerezhetők meg.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | 10 000 000 | 15 000 000 | 20 000 000 |
| Pajzs | 10 000 000 | 15 000 000 | 20 000 000 |
| Pajzs elnyelése | 80% | 80% | 80% |
| Aurasebzés másodpercenként minden bent lévő hajónak | 75 000 | 112 500 | 150 000 |
| Aura sugara | 700 | 700 | 700 |
| Sebesség | 10 | 10 | 10 |
| Aggrósugár | 3 000 | 3 000 | 3 000 |
| Kredit | 7 500 000 | 15 000 000 | 22 500 000 |
| Thulium | 20 000 | 40 000 | 60 000 |
| Tapasztalat (XP) | 1 200 000 | 2 400 000 | 3 600 000 |
| Becsület | 5 200 | 10 400 | 15 600 |
| PvE-pont kilövésenként | 112 | 112 | 112 |

**Zsákmány**: egy láda, annak a pilótának, aki a legtöbb sebzést okozta.

| Tárgy | Esély | Mennyiség |
| :--- | ---: | ---: |
| Ultra Core és Experimental Fusion Core, egyenlően elosztva | 100% | összesen 10 000–15 000 |
| Egy a 4 Epikus [rakéta](/wiki/06-Items/Rockets.md) közül, véletlenszerűen | 100% | 500–800 |
| N.I.K.E. | 100% | 20–30 |
| N.U.K.E. | 100% | 5–10 |
| Dark Matter | 100% | 40–60 |
| Ancient Control Unit | 100% | 10–20 |
| Power Core | 100% | 100–200 |

<!-- swamp-members:end -->

## Mit csinálj itt {#what-to-do-here}

- **Nézd, ne érintsd.** A mocsár későbbre való. Az egyetlen, amit álca nélkül elérhetsz, a zónán kívül van: a járőröző Voidok egy gyűrűben a zóna körül a mocsár első vonala, és az a hely, ahol egy csoport a lövegek nélkül harcolhat.
- **A Voidokkal áthatolással harcolj.** A Void nagy pajzsa egy találat 80 %-át elnyeli, és szinte mellékes: a mögötte lévő hajótest kicsi. Minél több pajzsáthatolása van a lézereidnek, annál előbb esik el ([Lézerek és lőszer](/wiki/06-Items/Lasers.md)).
- **Maradj távol a Lance-ektől.** Egy Inert Mass messzire lát, és egy Lance elől nem lehet elfutni: törd meg a tapadását álcával, EMP-vel, biztonsági gyűrűvel vagy ugrással, vagy hagyd el a hatótávját. Egy Mass hosszú harc még a legerősebb hajók nagy csoportjának is.
- **A Dormant-raj** mostantól közvetlenül a zónán kívül jelenik meg, így egy csoport a lövegek nélkül várhatja. Lásd: [Dormant-raj](/wiki/05-Swarms/Dormant-Swarm.md).

## Hol olvass tovább {#where-to-read-more}

- [Veszélyes szektorok](/wiki/01-General/Danger-Sectors.md): mi változott a 11. napon.
- [Óriás kotrógép](/wiki/03-Mechanics/Giant-Excavator.md): a Slumbering Voidok hullámai és amit védenek.
- [Rajok](/wiki/05-Swarms/Swarms.md) és [Dormant-raj](/wiki/05-Swarms/Dormant-Swarm.md): így fizet egy főellenség kilövése.
- [Rakéták](/wiki/06-Items/Rockets.md#the-craft-only-rockets): a N.I.K.E. és a N.U.K.E., amelyet a lövegtorony lő.
- [Feketelyuk](/wiki/03-Mechanics/Black-Hole.md): a `DS-4` másik veszélye.
- [Rakományládák](/wiki/03-Mechanics/Cargo.md): a ládák, amelyeket az idegenek ejtenek.
