<!-- wiki-i18n source: a3ead40fe6402d78 -->
<!-- wiki-i18n title: Kazamaták -->
# Kazamaták {#dungeons}

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; kazamata; kazamaták; kapu; kapuk; hadúr; labirintus; fokozat; zsákmányzóna; kártya -->

A **kazamata** a játékban **kapu** néven szerepel: zárt labirintus, amelynek végén egy **Hadúr** vár. Egy [klán](/wiki/03-Mechanics/Clans.md) alvezére vagy vezére nyit egyet, és a klánbankból fizeti ki, a klán tagjai pedig egyetlen [csoportként](/wiki/03-Mechanics/Groups.md) együtt repülnek be. Végigverekszik magukat a labirintus idegenjein, zsákmányzónákat nyitnak, hogy mindegyikből választhassanak egy kártyát, és legyőzik a Hadúrt. Minden pilótát, aki részt vett a harcban, kifizetnek, amikor a Hadúr elesik, az alábbi korlátokon belül. A kapuk a klán oldalának **Kapuk** lapján vannak.

A kapu csak az idegenek elleni harc: senki sem támadhat benne klántársat vagy bárki mást. Az idegenek nem fizetnek semmit. A fizetség egyedül a Hadúré, ezért csak az kap fizetést, aki a harcban van, amikor az elesik.

## Dióhéjban {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Nyílik**: A szezon 4. napjától
- **Ki nyithat kaput**: Egy alvezér vagy a vezér, aki a klánbankból fizeti az árat
- **Csoport**: 4–10 klántag, egy csoportban
- **Kapu naponta**: 3 klánonként és UTC-naponként, egyszerre csak egy nyitva
- **Kapu egyszerre**: 6 egy világban
- **Térképek**: Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Labirintusok**: 8; a kapu megnyitásakor az egyiket választja a játék
- **Gyülekezés**: 10 perc a gyülekezésre és az indításra. Az a kapu, amelyet senki sem indít el, bezárul, és az ára visszakerül a klánbankba
- **Időkorlát**: 1. fokozat: 80 perc, 2. fokozat: 110 perc, 3. fokozat: 150 perc az indítástól. Ha lejár, a kapu elbukik, és semmit sem fizet
- **Üresen**: Az a kapu, amelyben 3 perc ideig senki sincs, elbukik
- **Miután a Hadúr elesik**: A kapu 2 perc ideig nyitva marad a bent lévő pilótáknak
- **Visszatérés**: Az a pilóta, aki kilépett vagy megsemmisült, 3 alkalommal repülhet vissza, köztük 20 mp várakozással

<!-- dungeons-glance:end -->

## Hogyan zajlik egy menet {#how-a-run-goes}

1. **Megidézés.** A Kapuk lapon egy [alvezér vagy a vezér](/wiki/03-Mechanics/Clans.md#hierarchy-roles) kiválaszt egy fokozatot, és megnyomja a **Megidézés** gombot. Az ár a [klánbankból](/wiki/03-Mechanics/Clans.md#clan-economy-taxation) fogy, a kapu pedig a fent felsorolt térképek egyikét kapja. Az a kapu, amelyet senki sem indít el, bezárul, és az ár visszakerül a bankba.
2. **Belépés.** A klán tagjai a Klán ablakban a **Belépés** gombot nyomják meg, miközben repülnek. A bent lévő pilóták a kapu csoportja.
3. **Indítás.** A pilóta, aki a kaput megnyitotta, vagy egy tiszt az **Indítás** gombot nyomja meg, ha elég pilóta van bent. Ezután csak azok a pilóták térhetnek vissza, akik már bent voltak.
4. **Át a labirintuson.** A labirintus egyik végén lépsz be, a másikon vár a Hadúr. Az idegenek a termeikben alszanak, és falkákban ébrednek fel, ahogy a csoport közeledik.
5. **A zsákmányzónák megnyitása.** A labirintusban gyűrűk jelölik a zónákat. Tarts meg egyet, és a csoport szavaz egy kártyára, amelyet a Hadúr fizetségével együtt fizetnek ki.
6. **A Hadúr legyőzése.** Törd át a pajzsát és a hajótestét, és válaszolj a képességeire. Amikor elesik, a kapu teljesítve van.
7. **A fizetség.** A fizetség abban a pillanatban érkezik, amikor a Hadúr elesik. A kapu még egy ideig nyitva marad a bent lévő pilótáknak, aztán bezárul.

## Belépés {#entering}

A kapuba lépéshez **repülő hajó** kell, tehát előbb szállj fel, és utána nyisd meg a Klán ablakot, valamint egy [csoport](/wiki/03-Mechanics/Groups.md), amelyben elég klántag van. Kell még a fokozat által kért **szint**, és nem lehetsz egy másik kapuban. A kapu csoportjának van méretkorlátja: ha megtelt, senki más nem léphet be.

Egy alvezér vagy a vezér nyit kaput, a klánnak egyszerre csak egyet, és legfeljebb napi kapuszámig. A klánbanknak rendelkeznie kell az árral. Egy klán csak akkor nyithat meg egy fokozatot, ha az előzőt már teljesítette.

A kapuban nem válthatsz világot, és a Jump CPU és a Base CPU nem működik. A kapu sávján lévő **Kilépés** gomb megerősítés után kivisz. Az a pilóta, aki kilépett vagy megsemmisült, néhányszor visszarepülhet, rövid várakozással közöttük.

## A fokozatok {#the-stages}

A kapunak van egy fokozata, és a fokozat a nehézsége. Egy magasabb fokozaton szívósabb, erősebben ütő idegenek vannak, és többet fizet. A táblázat szorzói minden idegenre és a Hadúrra vonatkoznak. A sebzés a lézereket, a rakétákat és a Hadúr képességeit jelenti. A táblázat azt is megmutatja, hány idegent küld egy fokozat az elsőhöz képest. Az **ár** a kapu megnyitásakor kerül le a klánbankból.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fokozat | Követelmény | Az idegenek hajótestje és pajzsa | Az idegenek száma | Az idegenek sebzése | A kapu ára (kredit, a klánbankból) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **1. fokozat** | 6. szinttől | ×1 | ×1 | ×1 | 500 000 |
| **2. fokozat** | 7. szinttől | ×1,5 | ×1 | ×1,25 | 1 000 000 |
| **3. fokozat** | 8. szinttől | ×2,5 | ×1 | ×1,5 | 2 000 000 |

<!-- dungeons-stages:end -->

## A labirintus {#the-maze}

Minden kapu egy zárt labirintus a saját térképén, a fenti lista térképeinek egyikén, a labirintus pedig több elrendezés egyike. A labirintus termek és folyosók rácsa tömör falakkal. A hajók nem juthatnak át a falon, és a fal megállítja a lövéseket, vagyis fedezék. A meteor fentről esik, a fal pedig nem állítja meg.

## Az idegenek {#the-aliens}

Négyféle idegen őrzi a labirintust. A termeikben alszanak, és felébrednek, ha egy pilóta a közelbe ér. A kapu egyszerre csak bizonyos számú idegent tart a levegőben, és ez a szám a csoport méretével nő, így a megsemmisített falka beengedi a következőt. A nagyobb csoport arányosan több idegennel találkozik, a kisebb kevesebbel, és egy idegenfajta száma sosem esik egy alá.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Idegenek 5 fős csoportra | 1. fokozat | 2. fokozat | 3. fokozat |
| :--- | ---: | ---: | ---: |
| Gate Goombah | 130 | 130 | 130 |
| Gate Pirate | 28 | 28 | 28 |
| Gate Crystalys | 28 | 28 | 28 |
| Gate Crystalys Twin | 9 | 9 | 9 |
| Összesen | 195 | 195 | 195 |
| Egy zsákmányzóna hulláma | 10 × Gate Goombah és 1 × Gate Crystalys | 10 × Gate Goombah és 1 × Gate Crystalys | 10 × Gate Goombah és 1 × Gate Crystalys |

- **Egyszerre életben**: Legfeljebb 10 a csoport minden pilótájára, és összesen 70

<!-- dungeons-population:end -->

Sorban az egyes fajták. A hajótest és a pajzs a szokásos érték szorozva az oszlop fokozatának szorzójával.

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Gate Goombah

- **Úgy néz ki, mint**: Goombah
- **Falkaméret**: 6

|  | 1. fokozat | 2. fokozat | 3. fokozat |
| :--- | ---: | ---: | ---: |
| Hajótest | 32 000 | 48 000 | 80 000 |
| Pajzs | 48 000 | 72 000 | 120 000 |
| Lézersebzés (másodpercenként egy sorozat) | 3 000 | 3 750 | 4 500 |
| Sebesség | 180 | 180 | 180 |
| Lézer hatótávja | 800 | 800 | 800 |
| Aggrósugár | 1 800 | 1 800 | 1 800 |

### Gate Pirate

- **Úgy néz ki, mint**: Pirate Boss
- **Falkaméret**: 2
- **Rakéta**: Egyenes rakéta 5 mp időközönként, hatótávolsága 970 egység

|  | 1. fokozat | 2. fokozat | 3. fokozat |
| :--- | ---: | ---: | ---: |
| Hajótest | 300 000 | 450 000 | 750 000 |
| Pajzs | 50 100 | 75 150 | 125 250 |
| Lézersebzés (másodpercenként egy sorozat) | 200 | 250 | 300 |
| Rakétasebzés | 5 000 | 6 250 | 7 500 |
| Sebesség | 92 | 92 | 92 |
| Lézer hatótávja | 700 | 700 | 700 |
| Aggrósugár | 1 800 | 1 800 | 1 800 |

### Gate Crystalys

- **Úgy néz ki, mint**: Crystalys
- **Falkaméret**: 2

|  | 1. fokozat | 2. fokozat | 3. fokozat |
| :--- | ---: | ---: | ---: |
| Hajótest | 256 000 | 384 000 | 640 000 |
| Pajzs | 160 000 | 240 000 | 400 000 |
| Lézersebzés (másodpercenként egy sorozat) | 10 000 | 12 500 | 15 000 |
| Sebesség | 230 | 230 | 230 |
| Lézer hatótávja | 900 | 900 | 900 |
| Aggrósugár | 2 400 | 2 400 | 2 400 |

### Gate Crystalys Twin

- **Úgy néz ki, mint**: Crystalys, 1,4-szor akkora
- **Falkaméret**: 1

|  | 1. fokozat | 2. fokozat | 3. fokozat |
| :--- | ---: | ---: | ---: |
| Hajótest | 512 000 | 768 000 | 1 280 000 |
| Pajzs | 320 000 | 480 000 | 800 000 |
| Lézersebzés (másodpercenként egy sorozat) | 20 000 | 25 000 | 30 000 |
| Sebesség | 230 | 230 | 230 |
| Lézer hatótávja | 900 | 900 | 900 |
| Aggrósugár | 2 400 | 2 400 | 2 400 |

<!-- dungeons-enemies:end -->

## A Hadúr {#the-warlord}

A Hadúr a labirintus túlsó végén lévő teremben vár, és ő az egyetlen dolog a kapuban, ami fizet. Egy óriásira nőtt Crystalys. A hajótestének és a pajzsának az értéke a csoport méretével nő: minél több pilóta lép be, annál szívósabb, arányosan. A termében marad, és a képességeit egyenként, véletlen sorrendben használja, mindegyiknek külön töltődési ideje van.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Úgy néz ki, mint**: Crystalys, 3-szor akkora
- **Pajzstöltés**: 3 000 másodpercenként, 15 mp sebzésmentesség után

|  | 1. fokozat | 2. fokozat | 3. fokozat |
| :--- | ---: | ---: | ---: |
| Hajótest | 10 000 000 | 15 000 000 | 25 000 000 |
| Pajzs | 8 000 000 | 12 000 000 | 20 000 000 |
| Lézersebzés (másodpercenként egy sorozat) | 8 000 | 10 000 | 12 000 |
| Sebesség | 120 | 120 | 120 |
| Lézer hatótávja | 1 100 | 1 100 | 1 100 |

A fenti hajótest és pajzs 5 fős csoportra vonatkozik. A csoporttal együtt nőnek: ez a Hadúr hajótestének és pajzsának együttes értéke, a kapu indulásakor a csoportban lévő pilóták száma szerint.

| Pilóták a csoportban | 1. fokozat | 2. fokozat | 3. fokozat |
| :--- | ---: | ---: | ---: |
| 4 | 14 400 000 | 21 600 000 | 36 000 000 |
| 5 | 18 000 000 | 27 000 000 | 45 000 000 |
| 6 | 21 600 000 | 32 400 000 | 54 000 000 |
| 7 | 25 200 000 | 37 800 000 | 63 000 000 |
| 8 | 28 800 000 | 43 200 000 | 72 000 000 |
| 9 | 32 400 000 | 48 600 000 | 81 000 000 |
| 10 | 36 000 000 | 54 000 000 | 90 000 000 |

<!-- dungeons-boss:end -->

### A képességei {#its-abilities}

- Az **Életszívó aura piros gyűrűje** megsebez minden pilótát a belsejében, és a sebzéssel gyógyítja a Hadúrt. A Pajzselnyelésnek is van piros gyűrűje: kiszívja a benne lévő pilóták pajzsát, és a Hadúrét tölti. Mindkét esetben hagyd el a gyűrűt, vagy állj egy fal mögé.
- A **Meteorzápor borostyán gyűrűi** megmutatják, hol csapódnak be a meteorok egy pillanattal később. Mozogj folyamatosan, és hagyd el a gyűrűt, mielőtt becsapódik.
- A **Célkeresztben a gyógyítók** ráállítja a Hadúrt arra, aki egy másik pilótát gyógyít, és azt a pilótát erősebben üti. Oszd el a gyógyítást.
- A **Rakétazápor** önirányító rakétákat küld véletlen pilótákra. Egy EMP Charge vagy az álca lerázza őket.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Képesség | Felfutás | Tartam | Töltődés | A gyűrű sugara (egység) | A Hadúr legfeljebb ennyit nyer vissza |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Életszívó aura** | 2 mp | 15 mp | 2 perc | 900 | Hajótest és pajzs: 8% |
| **Meteorzápor** | 1,5 mp | 3 sorozat, köztük 4 mp | 2 perc | 420 | – |
| **Célkeresztben a gyógyítók** | 1 mp | 45 mp | 2 perc | – | – |
| **Rakétazápor** | 1,5 mp | 45 mp | 2 perc | – | – |
| **Pajzselnyelés** | 2 mp | 15 mp | 2 perc | 900 | Pajzs: 6% |

| Képesség | 1. fokozat | 2. fokozat | 3. fokozat |
| :--- | :--- | :--- | :--- |
| **Életszívó aura** | 8 000 másodpercenként | 10 000 másodpercenként | 12 000 másodpercenként |
| **Meteorzápor** | 6 meteor sorozatonként, egyenként 40 000 | 8 meteor sorozatonként, egyenként 50 000 | 10 meteor sorozatonként, egyenként 60 000 |
| **Célkeresztben a gyógyítók** | Lézere ×1,5 erősebben üti azt a pilótát, akire ráfordul | Lézere ×1,5 erősebben üti azt a pilótát, akire ráfordul | Lézere ×1,5 erősebben üti azt a pilótát, akire ráfordul |
| **Rakétazápor** | 6 500 rakétánként, 15 mp időközönként egy | 8 125 rakétánként, 15 mp időközönként egy | 9 750 rakétánként, 15 mp időközönként egy |
| **Pajzselnyelés** | 10 000 pajzs másodpercenként | 12 500 pajzs másodpercenként | 15 000 pajzs másodpercenként |

<!-- dungeons-abilities:end -->

## Zsákmányzónák {#loot-zones}

A labirintus padlóján egy gyűrű jelöli az egyes zsákmányzónákat, amint a csoport megtalálta. Állj egy pillanatra a belsejében, és a zóna felébred, az idegenek hulláma pedig megindul felé. Ekkor a csoportnak **tartania** kell a zónát: egy pilótának bent kell maradnia, amíg a sáv meg nem telik. A gyűrűben lévő idegenek megállítják a sávot, és az visszafut, amíg senki sincs bent, ezért előbb számolj fel a hullámot. Amikor a zóna megnyílik, a csoport három különböző kártyát lát, és **szavaz** egyre. Egy zóna egyszer nyílik meg, és a hulláma nem jön vissza.

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Zsákmányzónák**: 4 minden labirintusban
- **Sugár**: 450 egység
- **Ébresztés**: Maradj 2 mp a gyűrűben
- **Megtartás**: Tarts bent egy pilótát 30 mp ideig. A sáv megáll, amíg 3 vagy több idegen van a gyűrűben, és visszafelé fut, amíg senki sincs bent
- **Választás**: A csoportnak 45 mp van szavazni. A szavazás hamarabb véget ér, ha minden jelen lévő pilóta szavazott, vagy egy kártya megkapta a szavazatok több mint felét

<!-- dungeons-zones:end -->

### A kártyák {#the-cards}

A kártyákat egyenként húzzák az alábbi készletből. Az esély egy kártyáé egy húzásban. A sok példányos kártya minden kifizetett pilótához kerül, a felszerelés-kártya pedig egyetlen példánnyal a csoport egy pilótájához. Aki nem kap fizetséget, kártyát sem kap, és egy kudarcot vallott kapuban megnyitott zóna nem fizet semmit.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Kártya | 1. fokozat | 2. fokozat | 3. fokozat | Esély | Ki kapja |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2 000 | 3 000 | 5 000 | 21% | Minden kifizetett pilóta |
| Velkonite Reinforced Plate | 10 | 15 | 25 | 12% | Minden kifizetett pilóta |
| Orvium Reinforced Plate | 10 | 15 | 25 | 12% | Minden kifizetett pilóta |
| Velkonite | 200 | 300 | 500 | 12% | Minden kifizetett pilóta |
| Orvium | 200 | 300 | 500 | 12% | Minden kifizetett pilóta |
| Ultra Core | 5 000 | 7 500 | 12 500 | 10% | Minden kifizetett pilóta |
| Experimental Fusion Core | 3 000 | 4 500 | 7 500 | 8% | Minden kifizetett pilóta |
| Dark Matter | 5 | 8 | 12 | 8% | Minden kifizetett pilóta |
| Dark Matter Plate | 1 | 1 | 2 | 4% | Minden kifizetett pilóta |
| Engine III | 1 | 1 | 1 | 0,25% | A csoport egy pilótája |
| Heavy Shield Core | 1 | 1 | 1 | 0,25% | A csoport egy pilótája |
| Adaptive Core III | 1 | 1 | 1 | 0,25% | A csoport egy pilótája |
| Starfire-III | 1 | 1 | 1 | 0,25% | A csoport egy pilótája |

- **Felszerelés**: Az egy példányos kártyák felszerelések; arányuk együtt: 1%

<!-- dungeons-cards:end -->

## Fizetség {#pay}

Amikor a Hadúr elesik, minden pilóta, aki kiérdemelte, egyszer kap fizetséget a menetért. A csoport által választott kártyák a fokozat fizetségén felül járnak. Nincs világszorzó: a fizetség minden világban ugyanaz.

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fokozat | Becsület | Tapasztalat | Kredit | Thulium | x4 lőszer | PvE-ranglistapont |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| **1. fokozat** | 25 000 | 600 000 | 5 000 000 | 4 000 | 4 000 | 600 |
| **2. fokozat** | 50 000 | 1 500 000 | 10 000 000 | 9 000 | 9 000 | 1 500 |
| **3. fokozat** | 100 000 | 2 400 000 | 17 500 000 | 15 000 | 15 000 | 2 400 |

<!-- dungeons-pay:end -->

### Ki kap fizetséget {#who-is-paid}

Az idegenek sosem fizetnek. Egy menetet akkor is végig lehet játszani, ha nem fizet semmit, és az eredményképernyő megmondja, miért. A belépést soha nem tagadják meg amiatt, hogy egy fokozatért már fizettek neked: az a menet egyszerűen nem fizet.

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Egy nap**: Egy fokozat egy pilótának UTC-naponként egyszer fizet: azon a napon, amikor a Hadúr elesik
- **Egy hét**: Egy pilóta UTC-hetenként legfeljebb 10 teljesített fokozatért kap fizetséget, hétfőtől vasárnapig
- **Bent**: Összesen legalább 2 perc
- **Részvétel a harcban**: Legalább egy ezek közül: a Hadúr hajótestéből és pajzsából ennyit sebzett le: 2%; megsemmisített 10 idegent a kapuban; 50 000 értékben gyógyított más pilótákat a Hadúr elleni harc alatt

<!-- dungeons-rules:end -->

### Mennyit ér egy nap és egy hét {#what-a-day-and-a-week-are-worth}

Amit egy pilóta egy nap alatt kaphat, és a korlátok által megengedett legjobb héten. Az utolsó oszlop azt mutatja, mennyit ad a fizetség a [PvE-pontjaidhoz](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points).

<!-- dungeons-totals:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fizetség pilótánként | Becsület | Tapasztalat | Kredit | Thulium | x4 lőszer | PvE-ranglistapont |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Egy nap, minden fokozat egyszer | 175 000 | 4 500 000 | 32 500 000 | 28 000 | 28 000 | 4 500 |
| A legjobb hét: 7 × 3. fokozat és 3 × 2. fokozat | 850 000 | 21 300 000 | 152 500 000 | 132 000 | 132 000 | 21 300 |

Egy kifizetett teljesítés tapasztalata beleszámít a PvE-ranglistapontjaidba: minden 1 000 tapasztalat egy pont.

<!-- dungeons-totals:end -->

## A klánbank jutalma {#clan-bank-reward}

A klánbank is kap fizetséget, kreditben és nem Thuliumban, amikor a klán egy szezonban először teljesít egy fokozatot. A klánnak elég réginek kell lennie, és a menet elég pilótáját ki kell fizetni. A bank fokozatonként szezononként egyszer kap fizetséget.

<!-- dungeons-clan:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fokozat | Kredit a klánbanknak |
| :--- | ---: |
| **1. fokozat** | 10 000 000 |
| **2. fokozat** | 20 000 000 |
| **3. fokozat** | 30 000 000 |

- **A klán kora**: Legalább 3 nap
- **Kifizetett pilóták**: Legalább 3 a kapuban

<!-- dungeons-clan:end -->

## Tippek {#tips}

- Számold fel egy zóna hullámát, mielőtt megpróbálnád tartani a zónát, és harcolj a gyűrűben, ha az idegenek bejönnek.
- Használd a falakat: a lézerek nem hatolnak át rajtuk, és a Hadúr gyűrűi megállnak náluk.
- Tarts meg egy EMP Charge-ot a Rakétazáporra.
- Figyeld az órát a kapu sávján. Ha lejár az idő, a kapu kudarcot vall, és nem fizet semmit.
