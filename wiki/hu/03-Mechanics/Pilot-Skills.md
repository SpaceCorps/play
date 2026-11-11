<!-- wiki-i18n source: d75ffd5e6e894c46 -->
<!-- wiki-i18n title: Pilótakészségek -->
# Pilótakészségek {#pilot-skills}

<!-- wiki-search: skills; skill tree; pilot skill tree; pilot skills; skill xp; xp; level up; stats; attributes; heft; grit; reflex; instinct; laser tech; rocket tech; antimatter; marksmanship; sabotage; evasion; tactics; radiation tech; thruster theory; science; extraction; logistics; fabrication; commerce; soft cap; hold; training; day one; pilot button; pilot page; buffs; készségek; pilótakészségek; készségfa; tapasztalat; szintlépés; értékek; attribútumok; tömeg; szívósság; reflexek; ösztön; lézertechnika; rakétatechnika; antianyag; lövészet; szabotázs; kitérés; taktika; sugárzásvédelem; hajtóműelmélet; tudomány; kitermelés; logisztika; gyártás; kereskedelem; óránkénti plafon; raktér -->

A pilótádnak van egy **készségfája**: olyan értékek halmaza, amelyek attól lépnek szintet, amit csinálsz. Harcolj, és nő a Lézertechnikád és a Szívósságod; gyűjts a Skylabodból, és nő a Kitermelésed. Minden szint egy kis, tartós buffot ad valamire, amit amúgy is csinálsz, és semmit sem költesz el, semmit sem választasz: nincs elosztandó pont, és nincs mit újraosztani. Azt fejleszted, amit használsz.

A fa **a tiéd**, nem egy hajóé. Minden hajónak, amelyet vezetsz, megvannak a szintjeid, a holnap vásárolt hajónak is, és a szintek minden wipe-on át megmaradnak ([mi marad meg](#what-is-kept)).

Az új pilóta nem teljes erejű. Az 1. szinten a lézer és a rakéta kevesebb sebzést okoz, mint amit a tárgyoldalak megadnak, a Lézertechnika és a Rakétatechnika pedig szintenként a megadott számok fölé emeli őket. A tárgyoldalak minden száma a tárgy saját értéke, a készségeid előtt.

## Dióhéjban {#at-a-glance}

<!-- skills-glance:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

- **Értékek**: 18 érték: 4 attribútum és 14 készség 5 csoportban
- **Szintek**: 1-től 100-ig. Minden pilóta minden értéket az 1. szinten kezd, és nincs mit elkölteni, sem újraosztani
- **Egy szint ára**: 1. szint → 2. szint: 40 XP; 50. szint → 51. szint: 875 XP; 99. szint → 100. szint: 19 157 XP; összesen 313 258 XP
- **Mit ad egy szint**: A buff egyenesen nő az 1. szinten felvett értékétől a 100. szinten felvett értékéig. Semmi sem korlátozott
- **A lézered az 1. szinten**: A sebzésének 80%-át okozza, és az idő 80%-ában talál, vagyis a tárgyoldalak által megadott sebzés 64%-át
- **A rakétád az 1. szinten**: A sebzésének 100%-át okozza, és az idő 10%-ában hibás gyújtású, vagyis a tárgyoldalak által megadott sebzés 90%-át
- **Kitérés**: Minden pilóta hajója kikerüli a kitérhető találatok 3%-át, mielőtt bármely készség vagy formáció hozzátenne
- **Hajótestszint**: A hajód ritkasága határozza meg, ahogy az alábbi táblázat mutatja. A raktéred mérete és a Tömeg XP-je ezt követi
- **Raktér**: Az indulás után felvett erőforrás-egységeket számolja, a hajótestszintje által adott méretig. Ennek 90%-ától tele van, és teli raktérnél a Tömeg fizetése ×1,5. Soha semmit nem utasít el
- **Óránkénti puha plafon**: A legtöbb érték csak óránként egy plafonig fizet teljes XP-t, az érték saját egységében számolva az UTC óra szerinti órára. Fölötte egy esemény az XP-jének 25%-át fizeti
- **Edzés**: Egy készség XP-jének 10%-át a készség az attribútumának is kifizeti. A 100. szintű attribútum 25%-kal gyorsabban edzi a készségeit, mint az 1. szinten

| Hajótestszint | A hajó ritkasága | A raktér mérete |
| :--- | :--- | ---: |
| 1 | Silány / Gyakori | 60 |
| 2 | Szokatlan | 120 |
| 3 | Ritka | 250 |
| 4 | Epikus | 500 |
| 5 | Mitikus / Legendás / Örök | 1 000 |

<!-- skills-glance:end -->

## Az értékek {#the-stats}

Az értékek kétfélék. Az **attribútumok** (Tömeg, Szívósság, Reflexek és Ösztön) a pilóta alapjai. A **készségek** öt csoportban vannak, és mindegyiket egy attribútum irányítja, amelyet a táblázatok zárójelben neveznek meg: egy készség XP-je az attribútumát is táplálja, a magas attribútum pedig gyorsabban edzi a készségeit ([hogyan fizet az XP](#how-xp-is-paid)). A nevek a játék Pilótakészségek oldalának nevei.

A táblázatok minden buffot az 1. és az utolsó szinten adnak meg; közöttük a buff egyenesen nő. A **szorzó** megszoroz egy számot: az 1 fölötti nagyobbá, az 1 alatti kisebbé teszi. A legtöbb buff a hajód egy számát változtatja, és annak a számnak a tooltipjében, amelyet egy készség mozdított, van egy sor, amely megmondja, mennyi jön belőle a készségeidből.

<!-- skills-buffs:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

### Attribútumok {#attributes}

| Érték | Mit változtat | 1. szint | 100. szint |
| :--- | :--- | ---: | ---: |
| **Tömeg** | Hajótest | +0% | +10% |
| **Szívósság** | Elszenvedett sebzés | ×1 | ×0,9 |
| **Reflexek** | A képességek töltődési sebessége | ×1 | ×1,11 |
| **Ösztön** | Minden zsákmánysor esélye | +0 pont | +5 pont |
|  | Orvium és Velkonite a gyűjtőkből | ×1 | ×1,5 |

### Fegyverek {#weapons}

| Érték | Mit változtat | 1. szint | 100. szint |
| :--- | :--- | ---: | ---: |
| **Lézertechnika** (Reflexek) | Lézersebzés | ×0,8 | ×1,1 |
|  | Az esély, hogy egy lézersorozat talál | 80% | 90% |
| **Rakétatechnika** (Reflexek) | Rakétasebzés | ×1 | ×1,3 |
|  | Az esély, hogy egy rakéta hibás gyújtású | 10% | 0% |
| **Antianyag** (Ösztön) | Dark Matter a felvételekből | ×1 | ×1,25 |

### Harc {#combat}

| Érték | Mit változtat | 1. szint | 100. szint |
| :--- | :--- | ---: | ---: |
| **Lövészet** (Reflexek) | A Mine dobásának távolsága | ×1 | ×1,15 |
|  | A dobott Mine sebessége | ×1 | ×1,15 |
| **Szabotázs** (Reflexek) | A mérgek és a Mine-ok sebzése | ×1 | ×1,3 |
|  | A mérgek időtartama | ×1 | ×1,2 |
| **Kitérés** (Reflexek) | A találat elől kitérés esélye, a hajó sajátjához adva | 0% | 15% |
| **Taktika** (Reflexek) | A képességek időtartama | ×1 | ×1,2 |

### Hajóvezetés {#ship-control}

| Érték | Mit változtat | 1. szint | 100. szint |
| :--- | :--- | ---: | ---: |
| **Sugárzásvédelem** (Szívósság) | Sugárzási dózis | ×1 | ×0,4 |
| **Hajtóműelmélet** (Tömeg) | Sebesség | +0% | +15% |
| **Tudomány** (Ösztön) | Tudomány az üzemanyag minden egységéből | ×1 | ×1,25 |

### Skylab

| Érték | Mit változtat | 1. szint | 100. szint |
| :--- | :--- | ---: | ---: |
| **Kitermelés** (Ösztön) | Mit termel a Skylab | ×1 | ×1,3 |
| **Logisztika** (Tömeg) | Mennyit tart az Erőforrás-raktár bankja | ×1 | ×1,4 |
| **Gyártás** (Reflexek) | Egy gyártás ideje | ×1 | ×0,65 |

### Kereskedelem {#trading}

| Érték | Mit változtat | 1. szint | 100. szint |
| :--- | :--- | ---: | ---: |
| **Kereskedelem** (Ösztön) | Árak a Boltban | ×1 | ×0,85 |
|  | Mit fizet a Bolt visszavásárláskor | ×1 | ×1,1 |
|  | Egy aukciós hirdetés letétje | ×1 | ×0,5 |


<!-- skills-buffs:end -->

## Hol érzed {#where-you-feel-it}

- **Lézerek.** A Lézertechnika megváltoztatja minden sorozat sebzését és találati esélyét; a mellémenő sorozat lebegő „Miss” feliratot mutat, és a lőszerét így is elhasználja ([Harc](/wiki/03-Mechanics/Combat.md#laser-tech)). A lézereid hatótávja a hajód sajátja: a Lövészet az egyszerű x1-től eltérő lőszerrel elért találataidtól lép szintet, de csak a Mine-ra hat (lent).
- **Rakéták.** A Rakétatechnika megváltoztatja minden rakéta sebzését és az esélyt, hogy egy rakéta hibás gyújtású lesz ([Rakétatechnika](/wiki/06-Items/Rockets.md#rocket-tech)).
- **Találatok elviselése.** A Szívósság levesz egy részt minden találatból, amelyet kapsz, a Kitérés pedig növeli az esélyt, hogy egy egyenes találat semmit sem tesz ([Harc](/wiki/03-Mechanics/Combat.md#grit-and-evasion)). A Tömeg növeli a hajótestedet.
- **Képességek.** A Reflexek rövidítik a képességeid töltődési idejét, a Taktika pedig tovább tartja őket ([Képességek](/wiki/03-Mechanics/Abilities.md#pilot-skills)). A Szabotázs erősíti a mérgeket.
- **Mine.** A Szabotázs növeli a Mine sebzését, a Lövészet pedig gyorsabban és messzebbre dobja ([Extrák](/wiki/06-Items/Extras.md#mine)).
- **Sebesség.** A Hajtóműelmélet hozzátesz a sebességedhez, a hajtóművek és az Afterburner mellett ([Sebesség](/wiki/03-Mechanics/Speed.md)).
- **Felvétel.** Az Ösztön növeli minden zsákmánysor esélyét, ahogy egy Loot Luck Booster is, és a kettő összeadódik; az Antianyag növeli a felvett Dark Mattert ([Rakomány](/wiki/03-Mechanics/Cargo.md), [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md)).
- **Sugárzás.** A Sugárzásvédelem csökkenti a sugárzás dózisát a fekete lyuknál, a kotrók köreiben, a pulzároknál és az Unwakened aurájában ([Feketelyuk](/wiki/03-Mechanics/Black-Hole.md)).
- **Otthon.** A Kitermelés és a Logisztika megváltoztatja, mit termel és mennyit tárol a [Skylab](/wiki/03-Mechanics/Skylab.md), az Ösztön növeli a két gyűjtőjét, a Gyártás rövidíti az állomáson zajló gyártásokat, a Tudomány gyorsabban tölti a [Kutatóközpontot](/wiki/03-Mechanics/Research.md), a Kereskedelem pedig csökkenti a Bolt árait, növeli, amennyit visszavásárláskor fizet, és csökkenti egy hirdetés letétjét az [Aukción](/wiki/03-Mechanics/Auction.md).

## Hogyan fizet az XP {#how-xp-is-paid}

A szerver XP-t fizet azért, amit csinálsz, bárhol repülsz, ebben a sorrendben:

1. **A farmolásellenes szabály.** A vállalati vagy csoporttársnak okozott, vagy tőle kapott találat nem fizet semmit, és semmit sem fizet az sem, ami egy biztonságos zónában vagy újraéledési védelem alatt álló hajóval vagy hajón történik. A Tömeg, a Szívósság alacsony hajótestének és a Hajtóműelmélet másodpercei csak addig számítanak, amíg a hajód él, nem áll védelem alatt, és az utolsó percben adtál parancsot: a szabad ég alatt parkoló hajó semmit sem keres.
2. **Az óránkénti puha plafon.** A plafonnal rendelkező érték addig teljes XP-t fizet, fölötte csak egy részét, az érték saját egységében számolva (a leadott lövések, a kiadott parancsok, a megkeresett XP) az UTC óra szerinti órára. Az új bejelentkezés nem nyitja újra az ablakot, a számok a fenti listában és az alábbi táblázatban vannak.
3. **Edzési sebesség.** A készséget irányító attribútum növeli a készség által keresett XP-t, az attribútum minden szintjével jobban (a plafont ez előtt számolják, így a plafon a tevékenységet korlátozza, nem a sebességet).
4. **Az attribútum része.** A készség kapja az XP-t, az attribútuma pedig egy részét, amelyet soha nem plafonoznak és nem gyorsítanak.

A táblázat felsorolja, mi fizet XP-t, értékenként. Az XP a második oszlopban megnevezett dolog minden egységére jár.

<!-- skills-xp:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

| Érték | Mi fizet XP-t | XP | Óránkénti puha plafon |
| :--- | :--- | ---: | ---: |
| **Tömeg** | Minden 10 mp repülés, ha az utolsó 1 perc alatt adtál parancsot: a hajó hajótestszintje, plusz 0,2 minden beszerelt lemezért, ×1,5 teli raktérnél | 1 | Nincs |
| **Szívósság** | A maximális hajótestedből minden 1%, amelyet ellenségnek vagy veszélynek veszítesz | 1 | 300 XP óránként |
|  | Minden 10 mp, amíg a maximális hajótested 25%-a alatt vagy | 5 |  |
| **Reflexek** | Minden parancs, amelyet a játék elfogad: egy képesség, egy extra, egy új célpont, egy felvétel, egy gyártás, egy formációcsere, egy rakéta vagy egy ugrás. Egy új célpont legfeljebb 4 mp alatt egyszer fizet, egy felvétel legfeljebb 1 mp alatt egyszer, egy rakéta legfeljebb 1 mp alatt egyszer | 1 | 600 parancs óránként |
| **Ösztön** | Minden rakománydoboz, amelyet felveszel, kézzel vagy Retrieverrel | 2 | 600 XP óránként |
|  | Minden tárgy egy küldetésjutalomból, amelyet átveszel | 10 |  |
|  | Az első alkalom, amikor Ritka vagy jobb minőségű tárgyat veszel fel (tárgyanként egyszer, örökre) | 25 |  |
| **Lézertechnika** (Reflexek) | Minden sorozat, amelyet leadsz | 0,1 | 1 800 lövés óránként |
|  | Minden sorozat, amely hajót talál el | 0,1 |  |
| **Rakétatechnika** (Reflexek) | Minden rakéta, amelyet kilősz | 0,15 | 130 rakéta óránként |
|  | Minden rakéta, amely hajót talál el (rakétánként egyszer, akárhány hajót sebez a robbanása) | 0,3 |  |
| **Antianyag** (Ösztön) | Minden Dark Matter egység, amelyet egy felvételnél kapsz | 0,1 | Nincs |
| **Lövészet** (Reflexek) | Minden találat egy olyan sorozatból, amelyet az egyszerű x1-től eltérő lőszerrel lőttek (×1,5 minden lőszerfajta első 10 perc idejére egy óra szerinti órában) | 0,1 | 3 000 találat óránként |
|  | A Mine minden találata és minden másodperc, amelyet egy ellenség az Energetic Wallodban tölt | 0,1 |  |
| **Szabotázs** (Reflexek) | A Mine minden találata és minden másodperc, amelyet egy ellenség az Energetic Wallodban tölt | 0,5 | 1 200 XP óránként |
|  | Minden másodperc, amíg egy méregod hat egy ellenségen | 0,05 |  |
| **Kitérés** (Reflexek) | Minden rád irányuló ellenséges támadás, amely célt téveszt, vagy amely elől kitérsz | 1 | 600 XP óránként |
| **Taktika** (Reflexek) | Minden képesség, amelyet lézerhatótávon belüli ellenséggel nyomsz meg | 2 | 600 XP óránként |
| **Sugárzásvédelem** (Szívósság) | Minden másodperc egy sugárzási sávban | 0,2 | Nincs |
|  | A maximális hajótestedből minden 1%, amelyet a sugárzás elvesz | 1 |  |
| **Hajtóműelmélet** (Tömeg) | Minden másodperc a hajód sebességének 80%-a fölötti repülésből, Afterburner alatt kétszer annyi | 0,1 | Nincs |
| **Tudomány** (Ösztön) | Minden tudományegység, amelyet a Kutatóközpont eléget | 0,1 | Nincs |
|  | Minden technológia, amelyet befejezel | 50 |  |
| **Kitermelés** (Ösztön) | Minden erőforrás-egység, amelyet a Skylabod termel, begyűjtéskor fizetve | 0,1 | Nincs |
| **Logisztika** (Tömeg) | Minden erőforrás-egység, amelyet a Skylab bankjába betéteszel | 0,05 | Nincs |
| **Gyártás** (Reflexek) | Minden másodpercnyi gyártási idő, amelyet befejezel, begyűjtéskor fizetve | 0,1 | Nincs |
| **Kereskedelem** (Ösztön) | Minden kereskedés az Aukción vagy a Boltban, az 1 plusz Credit-értéke tízes alapú logaritmusaként számolva (egy Thulium annyit ér, amennyire az Aukció értékeli) | 2 | 600 XP óránként |

<!-- skills-xp:end -->

Repülés közben a repülési képernyő rövid sorokban mutatja a keresett XP-t, néhány másodpercenként összegyűjtve, egy szalagcím pedig megmondja, ha egy érték szintet lép, és mi változott (a Játéknapló egy sort megőriz róla). Az az érték, amely megkapja az első XP-jét, egyszer kerül bejelentésre. A készségek által mozdított számok tooltipjei ezt is megmondják, külön Pilóta sorban, a Hangár Sebzés csempéje pedig kihagyja a készségeket, és ezt ki is írja: akkor érvényesülnek, amikor lősz.

## Szintlépés {#levelling-up}

Egy szint több XP-be kerül, mint az előző, egy rögzített aránnyal, így az első szintek gyorsan jönnek, az utolsók sokáig tartanak. Minden értéknek ugyanez a görbéje. A buff, amelyet egy szinten kapsz, minden pilótának ugyanaz: csak az függ attól, mit csinálsz, milyen gyorsan éred el.

<!-- skills-curve:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

| Szint | A szint XP-je | XP összesen az 1. szinttől | Minden buff hányada |
| :--- | ---: | ---: | ---: |
| 2 | 40 | 40 | 1,01% |
| 10 | 66 | 468 | 9,09% |
| 25 | 170 | 2 174 | 24,24% |
| 50 | 822 | 12 851 | 49,49% |
| 75 | 3 968 | 64 397 | 74,75% |
| 100 | 19 157 | 313 258 | 100% |

<!-- skills-curve:end -->

## A Pilótakészségek oldal {#the-pilot-skills-page}

A **Pilótakészségek** oldal az állomás egyik oldala, saját sorral az oldalsávban. Az egész fát mutatja: az attribútumokat és a készségeket a csoportjaikban, mindegyiket a szintjével. Válassz ki egy értéket, hogy lásd, mit csinál, melyik attribútum irányítja, mely készségeket edzi, az XP-sávját és mitől nő, és a csúszkával megnézheted bármelyik szintet az 1-től az utolsóig: egy kis táblázat megadja, mit változtat az érték az előnézett szinten és a mostani szintedén. Az az érték, amely még nem keresett XP-t, nem használtként van jelölve, a szintje helyén kötőjellel. Az oldalsáv sora jelvényt kap, ha egy érték szintet lépett azóta, hogy utoljára megnyitottad az oldalt, és a Boosterek ablak egy kártyája összegzi, mit változtatnak a készségeid.

## Mi marad meg {#what-is-kept}

- **Minden wipe-on át.** A fa a fiókod része: a wipe nem változtat egyetlen szinten és XP-n sem, és a Tranzittárolónak semmi köze hozzá ([Amit megtartasz](/wiki/03-Mechanics/Wipe-Timeline.md#what-you-keep)).
- **A regionális szervereken.** Az XP, amelyet a Singaporen vagy az US Easten repülve keresel, hazatértedkor hozzáadódik a készségeidhez, az ott először használt érték is, és az ott felhasznált óránkénti plafon veled jön. Az ott repülő pilóta Pilótakészségek oldala a regionális szerver számait olvassa, azzal az XP-vel, amelyet a hajója az utolsó mentése óta keresett.
- **A fiók törléséig.** Egy fiók törlése törli a szintjeit.

A buffoknak nincs más plafonjuk, mint az utolsó szint: aki mindent felfejlesztett, olyan erős, mint ahogy a táblázatok mondják.
