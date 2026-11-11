<!-- wiki-i18n source: c3506248209cf351 -->
<!-- wiki-i18n title: Kazamaták -->
# Kazamaták {#dungeons}

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; portal; clan portal; join; clan gate alerts; clan dungeon window; clan dungeon alerts; dungeon goombah; dungeon pirate; dungeon crystalys; dungeon warlord; 75 percent; three quarters; start room; fog; guards; locked room; boss room; booster; boosters; swarm assist; focus most wanted; zone of chaos; rocket barrage; kazamata; kazamaták; kazamata; kazamaták; hadúr; labirintus; fokozat; zsákmányzóna; kártya; portál; klánportál; booster; köd; őrök; kezdőterem; lezárt terem; rajtámogatás; káoszzóna; klánkazamata-értesítések; klánkazamata; klánkazamata-értesítések; háromnegyed; 75 százalék -->

A **kazamata** zárt labirintus, amelynek végén egy **Hadúr** vár (a 0.5.2 előtt a játék KAPUNAK hívta). Egy [klán](/wiki/03-Mechanics/Clans.md) alvezére vagy vezére nyit egyet, és a klánbankból fizeti ki, a klán tagjai pedig egyetlen [csoportként](/wiki/03-Mechanics/Groups.md) együtt repülnek be. Végigverekszik magukat a labirintus idegenjein, zsákmányzónákat nyitnak, hogy mindegyikből választhassanak egy kártyát, és legyőzik a Hadúrt. Minden pilótát, aki részt vett a harcban, kifizetnek, amikor a Hadúr elesik, az alábbi korlátokon belül. A kazamaták a klán oldalának **Kazamaták** lapján vannak.

A kazamata csak az idegenek elleni harc: senki sem támadhat benne klántársat vagy bárki mást. Az idegenek elesésükkor fizetnek, mint a játék idegenei, amelyekről mintázták őket ([mit fizetnek az idegenek](#what-the-aliens-pay)). A teljesítés a Hadúré, ezért érte csak az kap fizetést, aki a harcban van, amikor az elesik.

A kazamata nem [szólókapu](/wiki/03-Mechanics/Solo-Gates.md). A szólókapu egy aréna, ahová csak te repülsz be, és az Energiamaterializálóval talált alkatrészekkel nyílik; a kettőnek külön szabályai, kifizetései és korlátai vannak.

## Dióhéjban {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Nyílik**: A szezon 1. napjától
- **Ki nyithat kazamatát**: Egy alvezér vagy a vezér, aki a klánbankból fizeti az árat
- **Csoport**: 4–10 klántag, egy csoportban
- **Kazamata naponta**: 3 klánonként és UTC-naponként, egyszerre csak egy nyitva
- **Kazamata egyszerre**: 6 egy világban
- **Térképek**: Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Labirintusok**: 8; a kazamata megnyitásakor az egyiket választja a játék
- **Főellenség terme**: Akkor nyílik meg, ha a Crystalysok és a Twinjeik 75%-a megsemmisült, felfelé kerekítve
- **Gyülekezés**: 10 perc a gyülekezésre és az indításra. Az a kazamata, amelyet senki sem indít el, bezárul, és az ára visszakerül a klánbankba
- **Időkorlát**: 1. fokozat: 95 perc, 2. fokozat: 130 perc, 3. fokozat: 165 perc az indítástól. Ha lejár, a kazamata elbukik, és a teljesítés semmit sem fizet
- **Üresen**: Az a kazamata, amelyben 3 perc ideig senki sincs, elbukik
- **Miután a Hadúr elesik**: A kazamata 2 perc ideig nyitva marad a bent lévő pilótáknak
- **Visszatérés**: Az a pilóta, aki kilépett vagy megsemmisült, akárhányszor visszarepülhet, két visszatérés között legalább 20 mp várakozással

<!-- dungeons-glance:end -->

## Hogyan zajlik egy menet {#how-a-run-goes}

1. **Megidézés.** A Kazamaták lapon egy [alvezér vagy a vezér](/wiki/03-Mechanics/Clans.md#hierarchy-roles) kiválaszt egy fokozatot, és megnyomja a **Megidézés** gombot. Az ár a [klánbankból](/wiki/03-Mechanics/Clans.md#clan-economy-taxation) fogy, a kazamata pedig a fent felsorolt térképek egyikét kapja. Az a kazamata, amelyet senki sem indít el, bezárul, és az ár visszakerül a bankba.
2. **Belépés.** A klán tagjai repülés közben a Klán ablakban a **Belépés** gombot nyomják meg, átugranak a klánportálon, vagy a **Csatlakozás** gombot nyomják meg a riasztókártyán (lásd Belépés). Mindenki a kezdőteremben landol, és a bent lévő pilóták a kazamata csoportja.
3. **Indítás.** A kezdőterem egy kis terem a labirintus egyik végén, és az ajtaja zárva marad, amíg a kazamata gyülekezik. Nincsenek benne idegenek, így biztonságosan lehet várakozni. A kazamata **magától elindul**, ha minden pilóta bent van, akire vár, és a csoport elég nagy. A klán azon tagjaira vár, akik online vannak, nincsenek távol, és egy bejutott pilóta csoportjában vannak, és azonnal elindul, ha a csoport megtelt. A pilóta, aki a kazamatát megnyitotta, vagy egy tiszt megnyomhatja az **Indítás** gombot, hogy korábban kezdjenek azokkal a pilótákkal, akik bent vannak, ha elegen vannak. Aki kilép, arra többé nem várnak. Amikor a kazamata elindul, az ajtó végleg kinyílik, és ezután csak azok a pilóták térhetnek vissza, akik már bent voltak.
4. **Át a labirintuson.** A labirintus egyik végén lépsz be, a másikon vár a Hadúr egy lezárt teremben. A labirintus sötét: csak azt látod, amit a csoport felfedezett, és ami a hajói közelében van. Az idegenek falkákban várakoznak a folyosókon, és egy falka abban a pillanatban kijön, amikor egy pilóta berepül a folyosószakaszba, ahol vár, majd végigüldözi a csoportot a labirintuson.
5. **A zsákmányzónák megnyitása.** A labirintusban gyűrűk jelölik a zónákat. Tarts meg egyet, és a csoport szavaz egy kártyára, amelyet a Hadúr fizetségével együtt fizetnek ki.
6. **A főnökterem feloldása.** Pusztítsd el a labirintus Crystalysainak és Twinjeinek háromnegyedét, és a Hadúr termének ajtaja kinyílik. Addig a Hadúr nem sebezhető. A többi idegen marad, ahol van, és őket is elpusztíthatod.
7. **A Hadúr legyőzése.** Törd át a pajzsát és a hajótestét, és válaszolj a képességeire. Amikor elesik, a kazamata teljesítve van.
8. **A fizetség.** A fizetség abban a pillanatban érkezik, amikor a Hadúr elesik. A kazamata még egy ideig nyitva marad a bent lévő pilótáknak, aztán bezárul.

## Belépés {#entering}

A kazamatába lépéshez **repülő hajó** kell, tehát előbb szállj fel, és utána nyisd meg a Klán ablakot, valamint egy [csoport](/wiki/03-Mechanics/Groups.md), amelyben elég klántag van. Kell még a fokozat által kért **szint**, és nem lehetsz egy másik kazamatában. A kazamata csoportjának van méretkorlátja: ha megtelt, senki más nem léphet be.

Egy alvezér vagy a vezér nyit kazamatát, a klánnak egyszerre csak egyet, és legfeljebb napi kazamataszámig. A klánbanknak rendelkeznie kell az árral. Egy klán csak akkor nyithat meg egy fokozatot, ha az előzőt már teljesítette.

A kazamatában nem válthatsz világot, és a Jump CPU és a Base CPU nem működik. A **Klánkazamata** ablak **Kilépés** gombja kivisz. Előbb megerősítést kér, kivéve ha a Hadúr már elesett: ilyenkor azonnal távozol. Az a pilóta, aki kilépett vagy megsemmisült, visszarepülhet; hogy hányszor, és két visszatérés között mennyit kell várnia, azt a **Dióhéjban** alatti lista mondja meg.

### A klánportál és a riasztás {#the-clan-portal-and-the-call}

Amikor egy kazamatát megnyitnak, a klán kap hozzá egy **portált** minden vállalat otthoni térképén (`M-1`, `T-1` és `G-1`), az állomás biztonságos zónáján kissé kívül. Csak a klán pilótái látják: mindenki más számára nincs ott. Saját biztonságos zónája nincs. Repülj hozzá, és ugorj át, mint bármely más portálon, és a **Belépés** szabályai szerint a kazamatába visz: repülő hajó, elég klántagot számláló csoport, a fokozat szintje és hely a csoportban. Miután a kazamata elindult, már csak azok a pilóták használhatják, akik bent voltak. A portál eltűnik, amikor a kazamata véget ér.

Amíg a klánod kazamataja gyülekezik, és te máshol repülsz, **riasztás** érkezik hozzád: egy kártya a repülési képernyő tetején, hanggal. Megmondja, ki nyitotta a kazamatát, hány pilóta van bent, és meddig marad nyitva a kazamata. A **Csatlakozás** bevisz, ahogy a **Belépés** a Kazamaták lapon, és amikor kilépsz a kazamatából, a hajód oda tér vissza, ahol volt. A Csatlakozás szürke, amíg a csoportod túl kicsi. A **Most nem** elrejti a kártyát ennél a kazamatánál. Ha a csoportod már bent van, és a kazamata rád vár, a kártya ezt mondja. A kártya a klánnak azokhoz a pilótáihoz jut el, akik repülnek (azokhoz nem, akik egy állomáson kikötöttek), és megvan a fokozat által kért szintjük. A kártyát és a hangját kikapcsolhatod a **Klánkazamata-értesítések** beállítással a Beállítások › Általános › Csoportok alatt.

### A Klánkazamata ablak {#the-clan-dungeon-window}

A kazamatában a menetnek saját ablaka van, a **Klánkazamata**. Mutatja az eltelt időt és ami hátravan, hány idegen repül és hányat semmisítettek meg, mit kell most tennie a csoportnak (felfedezni a labirintust, tartani egy zónát, megtalálni a főnököt, elpusztítani a Crystalysok és a Twinjeik háromnegyedét, legyőzni a Hadúrt), a tartósávot, amíg egy zónában állsz, a Hadúr képességét a visszaszámlálásával, és a **Kilépés** gombot. Ugyanolyan ablak, mint a többi: húzd a címsoránál fogva, és zárd be a sarkában lévő piros fénnyel. Magától kinyílik, amikor belépsz egy kazamatába, minden kazamatánál egyszer: ha bezárod, a következő kazamatáig zárva marad. Az eszköztáron van hozzá egy **Klánkazamata** gomb, amíg egy kazamatában vagy. Amíg az ablak zárva van, a Hadúr egy képessége, amely mindjárt indul vagy éppen hat, egyetlen soros sávként jelenik meg a nevével és a visszaszámlálásával. Kattints a sávra, hogy újra megnyisd az ablakot.

## A fokozatok {#the-stages}

Egy kazamatának van fokozata, és a fokozat a nehézsége. Magasabb fokozaton szívósabb idegenek vannak, amelyek erősebben ütnek, és többet fizet. A táblázat szorzói az idegeneké. A sebzés a lézereikre és a rakétáikra vonatkozik. A Hadúr nem követi a táblázatot: minden fokozathoz saját számai vannak, lejjebb. A táblázat azt is megmondja, hány idegent küld egy fokozat az elsőhöz képest. Az **ár** a klánbankból vonódik le, amikor a kazamatát megnyitják.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fokozat | Követelmény | Az idegenek hajótestje és pajzsa | Az idegenek száma | Az idegenek sebzése | A kazamata ára (kredit, a klánbankból) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **1. fokozat** | 6. szinttől | ×1 | ×1 | ×1 | 500 000 |
| **2. fokozat** | 7. szinttől | ×1,5 | ×1 | ×1,5 | 1 000 000 |
| **3. fokozat** | 8. szinttől | ×2 | ×1 | ×2 | 2 000 000 |

<!-- dungeons-stages:end -->

## A labirintus {#the-maze}

Minden kazamata egy zárt labirintus egy saját térképen, a fenti lista egyik térképén, és a labirintus több elrendezés egyike. A labirintus kitölti az egész térképet, szélétől szélig: termek és folyosók rácsa tömör falakkal. A hajók nem juthatnak át a falon, és a fal a lövéseket is blokkolja, így fedezék. A meteor fentről esik, és egy fal nem állítja meg.

**Termek és ajtók.** A kezdőteremnek, ahol landolsz, és a Hadúr termének a túlsó végen, egy-egy ajtaja van. A zárt ajtó fal a hajóknak, a lövéseknek és az idegeneknek egyaránt. A kezdőajtó kinyílik, amikor a kazamata elindul. A Hadúr ajtaja zárva marad, amíg a Crystalysok és a Twinjeik háromnegyede meg nem semmisül (lásd [A lezárt terem](#the-locked-room)). Köztük a labirintusban minden zsákmányzónához van egy zsákmányterem.

**Köd.** A labirintus sötét. Repülés közben a falait és az idegeneit csak ott látod, ahol a csoport járt, és a csoport minden hajója körül egy kis darabon. Egy terem felfedezettnek számít, amint egyikőtök bent van. A minitérkép ugyanígy működik: az egész szint térképe, amely a csoport felfedezésével tölt ki, a bejárattal, a Hadúr ajtajával, a megtalált zónákkal és a Hadúrral, ha megtaláltátok. A saját csoportod pilótái mindig látszanak.

## Az idegenek {#the-aliens}

Négyféle idegen őrzi a labirintust. Falkákban várakoznak a folyosókon, soha nem egy teremben, és egy falka abban a pillanatban kijön, amikor egy pilóta berepül a folyosószakaszba, ahol vár. Ahol még nem járt pilóta, ott semmi sincs a térképen, így egyetlen falka sem áll a falak mögött, mélyen a labirintusban, mielőtt odaérnél. Egy falka nem vár helyre: ugyanabban a pillanatban a térképen van, akárhány idegen van már kint. Egy folyosószakaszban egyetlen falka áll, így abban a szakaszban, ahová beröpülsz, egy falkával találkozol, nem több falka összegével (egy tízfős csoportnak több falkája van, mint ahány szakasz, és ott egy szakaszban két falka áll, mindkettő kijön). A kint lévő falka nem vár rád: végigüldözi a csoportot a labirintuson, és az a falka, amelyik mindenkit elveszít, visszamegy oda, ahol kijött, és meggyógyul. Egy falka csak egyszer jön ki: amelyiket elpusztítod, az nem tér vissza, és amelyiktől elrepülsz, az a térképen marad. A zsákmányzónák hullámai mások: a kazamata egyszerre csak annyi idegent tart a levegőben, és ez a szám a csoport méretével nő, így egy hullám, amely túllépné, helyre vár, és egy falka, amelyet elpusztítasz, beengedi a következő hullámot. Egy nagyobb csoport arányosan több idegennel találkozik, egy kisebb kevesebbel, és az idegenek egy fajtája soha nem esik egy alá.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Idegenek 5 fős csoportra | 1. fokozat | 2. fokozat | 3. fokozat |
| :--- | ---: | ---: | ---: |
| Dungeon Goombah | 156 | 156 | 156 |
| Dungeon Pirate | 34 | 34 | 34 |
| Dungeon Crystalys | 34 | 34 | 34 |
| Dungeon Crystalys Twin | 11 | 11 | 11 |
| Összesen | 235 | 235 | 235 |
| A főellenség termének megnyitásához | 34 | 34 | 34 |
| Egy zsákmányzóna hulláma | 12 × Dungeon Goombah és 1 × Dungeon Crystalys | 12 × Dungeon Goombah és 1 × Dungeon Crystalys | 12 × Dungeon Goombah és 1 × Dungeon Crystalys |

- **Egy zsákmányzóna hulláma helyre vár**: Amint a csoport minden pilótájára 10 él, vagy összesen 70

<!-- dungeons-population:end -->

Sorban az egyes fajták. A hajótest és a pajzs a szokásos érték szorozva az oszlop fokozatának szorzójával.

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Dungeon Goombah

- **Úgy néz ki, mint**: Goombah
- **Falkaméret**: 6
- **Jutalma és zsákmánya, mint**: Goombah

|  | 1. fokozat | 2. fokozat | 3. fokozat |
| :--- | ---: | ---: | ---: |
| Hajótest | 32 000 | 48 000 | 64 000 |
| Pajzs | 48 000 | 72 000 | 96 000 |
| Lézersebzés (másodpercenként egy sorozat) | 3 000 | 4 500 | 6 000 |
| Sebesség | 180 | 180 | 180 |
| Lézer hatótávja | 800 | 800 | 800 |
| Aggrósugár | 1 800 | 1 800 | 1 800 |
| Jutalom és zsákmány, az eredeti többszöröse | ×1 | ×1,5 | ×2 |
| Kredit megsemmisítésenként | 15 000 | 22 500 | 30 000 |
| Thulium megsemmisítésenként | 75 | 113 | 150 |
| Tapasztalat megsemmisítésenként | 3 000 | 4 500 | 6 000 |
| Becsület megsemmisítésenként | 24 | 36 | 48 |

### Dungeon Pirate

- **Úgy néz ki, mint**: Pirate Boss
- **Falkaméret**: 2
- **Jutalma és zsákmánya, mint**: Pirate Boss
- **Rakéta**: Egyenes rakéta 5 mp időközönként, hatótávolsága 1 000 egység

|  | 1. fokozat | 2. fokozat | 3. fokozat |
| :--- | ---: | ---: | ---: |
| Hajótest | 250 000 | 375 000 | 500 000 |
| Pajzs | 50 100 | 75 150 | 100 200 |
| Lézersebzés (másodpercenként egy sorozat) | 200 | 300 | 400 |
| Rakétasebzés | 5 000 | 7 500 | 10 000 |
| Sebesség | 110 | 110 | 110 |
| Lézer hatótávja | 700 | 700 | 700 |
| Aggrósugár | 1 800 | 1 800 | 1 800 |
| Jutalom és zsákmány, az eredeti többszöröse | ×1 | ×1,5 | ×2 |
| Kredit megsemmisítésenként | 145 000 | 217 500 | 290 000 |
| Thulium megsemmisítésenként | 725 | 1 088 | 1 450 |
| Tapasztalat megsemmisítésenként | 29 000 | 43 500 | 58 000 |
| Becsület megsemmisítésenként | 232 | 348 | 464 |

### Dungeon Crystalys

- **Úgy néz ki, mint**: Crystalys
- **Falkaméret**: 2
- **Jutalma és zsákmánya, mint**: Crystalys

|  | 1. fokozat | 2. fokozat | 3. fokozat |
| :--- | ---: | ---: | ---: |
| Hajótest | 256 000 | 384 000 | 512 000 |
| Pajzs | 160 000 | 240 000 | 320 000 |
| Lézersebzés (másodpercenként egy sorozat) | 10 000 | 15 000 | 20 000 |
| Sebesség | 230 | 230 | 230 |
| Lézer hatótávja | 900 | 900 | 900 |
| Aggrósugár | 2 400 | 2 400 | 2 400 |
| Jutalom és zsákmány, az eredeti többszöröse | ×1 | ×1,5 | ×2 |
| Kredit megsemmisítésenként | 75 000 | 112 500 | 150 000 |
| Thulium megsemmisítésenként | 200 | 300 | 400 |
| Tapasztalat megsemmisítésenként | 12 000 | 18 000 | 24 000 |
| Becsület megsemmisítésenként | 52 | 78 | 104 |

### Dungeon Crystalys Twin

- **Úgy néz ki, mint**: Crystalys, 1,4-szor akkora
- **Falkaméret**: 1
- **Jutalma és zsákmánya, mint**: Crystalys

|  | 1. fokozat | 2. fokozat | 3. fokozat |
| :--- | ---: | ---: | ---: |
| Hajótest | 512 000 | 768 000 | 1 024 000 |
| Pajzs | 320 000 | 480 000 | 640 000 |
| Lézersebzés (másodpercenként egy sorozat) | 20 000 | 30 000 | 40 000 |
| Sebesség | 230 | 230 | 230 |
| Lézer hatótávja | 900 | 900 | 900 |
| Aggrósugár | 2 400 | 2 400 | 2 400 |
| Jutalom és zsákmány, az eredeti többszöröse | ×2 | ×3 | ×4 |
| Kredit megsemmisítésenként | 150 000 | 225 000 | 300 000 |
| Thulium megsemmisítésenként | 400 | 600 | 800 |
| Tapasztalat megsemmisítésenként | 24 000 | 36 000 | 48 000 |
| Becsület megsemmisítésenként | 104 | 156 | 208 |

<!-- dungeons-enemies:end -->

## A Hadúr {#the-warlord}

A Hadúr a labirintus túlsó végén lévő teremben vár, és az ő bukása fizeti ki a teljesítést. Saját megsemmisítésért nem fizet, ahogy a többi idegen igen. Hatalmasra nőtt Crystalys. A hajótestét és a pajzsát a csoport mérete növeli: minél több pilóta lép be, annál szívósabb, arányosan. Soha nem hagyja el a termét, akár zárva van az ajtó, akár nyitva: a terem falai között marad, és nem üldöz a folyosókon. Egy kívül álló pilóta legfeljebb a terem széléig csalhatja ki, és nyitott ajtón át így is lő mindenre, amit a lézere elér. A képességeit egyenként használja, véletlen sorrendben, mindegyiket a saját újratöltési idejével.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Úgy néz ki, mint**: Crystalys, 3-szor akkora
- **Pajzstöltés**: 3 000 másodpercenként, 15 mp sebzésmentesség után

|  | 1. fokozat | 2. fokozat | 3. fokozat |
| :--- | ---: | ---: | ---: |
| Hajótest | 10 000 000 | 15 000 000 | 25 000 000 |
| Pajzs | 8 000 000 | 12 000 000 | 20 000 000 |
| Lézersebzés (másodpercenként egy sorozat) | 12 500–15 000 | 15 000–17 500 | 20 000–25 000 |
| Sebesség | 120 | 120 | 120 |
| Lézer hatótávja | 1 100 | 1 100 | 1 100 |

A fenti hajótest és pajzs 5 fős csoportra vonatkozik. A csoporttal együtt nőnek: ez a Hadúr hajótestének és pajzsának együttes értéke, a kazamata indulásakor a csoportban lévő pilóták száma szerint.

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

### A lezárt terem {#the-locked-room}

A Hadúr termének ajtaja attól a pillanattól zárva van, hogy a kazamatát megnyitják, és amíg zárva van, a Hadúr nem sebezhető: semmilyen lézer, rakéta vagy robbanás nem éri, és egyetlen képességet sem használ. Az ajtó végleg kinyílik, amikor megsemmisült **a Crystalysok és a Twinjeik háromnegyede**, amelyekkel a kazamatát létrehozták, felfelé kerekítve (a fenti idegentáblázat egy 5 fős csoportra számolja őket, és az utolsó sora megmondja, mennyi kell). A labirintus falkáiban lévő Crystalysok és Twinek számítanak, és mindegy, ki semmisíti meg őket. Egy falka csak akkor jön ki, amikor egy pilóta berepül a folyosószakaszába, ezért a csoportnak elég sokat meg kell találnia, hogy az ajtó kinyíljon. A többi idegen, a zsákmányzónák hullámai, a Goombahok, amelyeket a Hadúr hív, és maga a Hadúr nem számítanak az ajtó felé.

A Klánkazamata ablak számolja, hány ilyet kell még megsemmisíteni a terem megnyitásához, és egy jelzésben megmondja, hogy a Hadúr nem sebezhető, egy üzenet pedig szól, amikor a terem feloldódik. Egy falka, amely még nem jött ki, teljes egészében számít, így a csoportnak meg kell találnia a labirintusban a Crystalysokat és a Twinjeiket, és be kell repülnie a folyosószakaszaikba. **A többi idegen nem tűnik el, amikor az ajtó kinyílik.** Maradnak a labirintusban, kijönnek, amikor egy pilóta berepül a folyosószakaszukba, és ugyanúgy megsemmisíthetők, mint addig, így a csoport, ha akarja, mindet elpusztíthatja, mielőtt a Hadúrral harcol: az ablakban az idegenek száma egészen az összes idegenig megy, amellyel a kazamatát létrehozták, és tele van, amikor egy sem maradt. Elesésükkor fizetnek ([mit fizetnek az idegenek](#what-the-aliens-pay)), és akik még élnek, amikor a Hadúr elesik, a kazamatával együtt eltűnnek. A minitérképen az ajtó piros vonal, amíg zárva van, és zöld, amikor nyitva. Egy kazamata soha nem csapda: az időkorlát akkor is véget vet egy kazamatának, amelynek ajtaja zárva marad, és egy adminisztrátor feloldhatja egy elakadt kazamata termét.

### A képességei {#its-abilities}

- Az **Életszívó aura piros gyűrűje** megsebez minden pilótát a belsejében, és a sebzéssel gyógyítja a Hadúrt. A Pajzselnyelésnek is van piros gyűrűje: kiszívja a benne lévő pilóták pajzsát, és a Hadúrét tölti. Mindkét esetben hagyd el a gyűrűt, vagy állj egy fal mögé.
- A **Meteorzápor borostyán gyűrűi** megmutatják, hol csapódnak be a meteorok egy pillanattal később. Mozogj folyamatosan, és hagyd el a gyűrűt, mielőtt becsapódik.
- A **Fókusz a legkeresettebbre** megjelöli azt a pilótát, aki a legtöbb sebzést okozta a Hadúrnak, egy arany zárójellel a hajóján, és a Hadúr minden másodpercben egy extra lövést ad le rá, amíg tart. A célzása nem változik: tovább lő a legközelebbi pilótára, akit lát, így az a megjelölt pilóta, aki egyben a legközelebbi is, mindkettőt megkapja. Az extra lövéshez szabad rálátás és a Hadúr lézerének hatótávolsága kell, így egy fal vagy némi távolság megmenti. Nem indul el, amíg senki nem okozott sebzést.
- A **Rakétazápor** önirányító rakétákat küld véletlen pilótákra, de csak olyan pilótákra, akiket a Hadúr lát, és az útba eső fal megállít egy rakétát. Egy gyűrű mutatja, melyik pilótát követi egy rakéta. Egy EMP Charge vagy az álca lerázza őket.
- A **Rajtámogatás** az, amikor a Hadúr hívja a Goombahjait. Amíg élnek, nem sebezhető, és nem lő, és más képességet sem használ. Pusztítsd el mindet: a szalag számolja, hány maradt. Ha eltelik egy perc, a Hadúr újra sebezhető, és a megmaradt Goombahok maradnak és tovább harcolnak. Nem számítanak a főnökterem megnyitásához, és semmit nem fizetnek.
- A **Káoszzóna** egy lila gyűrű a földön, a Hadúr körül, és amíg tart, mindenhová megy, ahová a Hadúr. A gyűrűben senki nem támadhat, sem lézerrel, sem rakétával, a javítás, az álca és a repülés viszont működik, és a Hadúr és az idegenei úgy lőnek, mint mindig. A gyűrű egy pillanattal a hatása előtt megjelenik: lépj ki belőle, és maradj kint, mert követi a Hadúrt. A gyűrűn kívüli pilóta tovább lőhet, ameddig a fegyverei elérnek.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Képesség | Felfutás | Tartam | Töltődés | A gyűrű sugara (egység) | A Hadúr legfeljebb ennyit nyer vissza |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Életszívó aura** | 2 mp | 15 mp | 2 perc | 900 | Hajótest és pajzs: 8% |
| **Meteorzápor** | 1,5 mp | 3 sorozat, köztük 4 mp | 2 perc | 420 | – |
| **Fókusz a legkeresettebbre** | 1 mp | 20 mp | 2 perc | – | – |
| **Rakétazápor** | 1,5 mp | 45 mp | 2 perc | – | – |
| **Pajzselnyelés** | 2 mp | 15 mp | 2 perc | 900 | Pajzs: 6% |
| **Rajtámogatás** | 2 mp | Legfeljebb 1 perc | 3 perc | – | – |
| **Káoszzóna** | 2 mp | 15 mp | 2 perc | 900 | – |

| Képesség | 1. fokozat | 2. fokozat | 3. fokozat |
| :--- | :--- | :--- | :--- |
| **Életszívó aura** | 8 000 másodpercenként | 10 000 másodpercenként | 12 000 másodpercenként |
| **Meteorzápor** | 6 meteor sorozatonként, egyenként 40 000 | 8 meteor sorozatonként, egyenként 50 000 | 10 meteor sorozatonként, egyenként 60 000 |
| **Fókusz a legkeresettebbre** | 18 750–22 500 extra lövésenként a legtöbb sebzést okozó pilótára, 1 mp időközönként egy | 22 500–26 250 extra lövésenként a legtöbb sebzést okozó pilótára, 1 mp időközönként egy | 30 000–37 500 extra lövésenként a legtöbb sebzést okozó pilótára, 1 mp időközönként egy |
| **Rakétazápor** | 26 000 rakétánként, 15 mp időközönként egy | 32 500 rakétánként, 15 mp időközönként egy | 39 000 rakétánként, 15 mp időközönként egy |
| **Pajzselnyelés** | 10 000 pajzs másodpercenként | 12 500 pajzs másodpercenként | 15 000 pajzs másodpercenként |
| **Rajtámogatás** | 12 Goombah | 18 Goombah | 24 Goombah |
| **Káoszzóna** | A gyűrűben lévő pilóták nem támadhatnak | A gyűrűben lévő pilóták nem támadhatnak | A gyűrűben lévő pilóták nem támadhatnak |

<!-- dungeons-abilities:end -->

## Zsákmányzónák {#loot-zones}

Egy gyűrű a labirintus padlóján jelöli meg az egyes zsákmányzónákat, amint a csoport megtalálta. Állj egy ideig benne, és a zóna felébred, és egy hullám idegen indul rá. Ekkor a csoportnak **tartania** kell a zónát: egy pilótát bent kell tartani, amíg a sáv megtelik. Minél több pilóta áll a gyűrűben, annál gyorsabban telik a sáv: a sáv melletti szám megmondja, hányszor gyorsabban, az alábbi táblázat pedig megadja az időket. Elég sok idegen a gyűrűben megállítja a sávot (az alábbi lista megmondja, hány), és visszafut, amíg senki nincs bent, ezért előbb irtsd ki a hullámot. Amikor a zóna megnyílik, a csoport három különböző kártyát lát, és **szavaz** egyre. Egy zóna egyszer nyílik meg, és a zóna hulláma nem tér vissza.

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Zsákmányzónák**: 6 minden labirintusban
- **Sugár**: 450 egység
- **Ébresztés**: Maradj 2 mp a gyűrűben
- **Megtartás**: Tarts bent egy pilótát 30 mp ideig. A sáv megáll, amíg 3 vagy több idegen van a gyűrűben, és visszafelé fut, amíg senki sincs bent
- **Választás**: A csoportnak 45 mp van szavazni. A szavazás hamarabb véget ér, ha minden jelen lévő pilóta szavazott, vagy egy kártya megkapta a szavazatok több mint felét

Több pilóta a gyűrűben gyorsabban tartja a zónát. Ennyi ideig tart egy zóna megtartása:

| Pilóták a gyűrűben | A zóna megtartásának ideje |
| :--- | ---: |
| 1 | 30 mp |
| 2 | 20 mp |
| 3 | 15 mp |
| 4 | 12 mp |
| 5 vagy több | 10 mp |

<!-- dungeons-zones:end -->

### Boosterek {#boosters}

A 2. és a 3. fokozaton a csoport a kazamata idegeneinek elpusztításával szerez boostereket. Minden tizedüknél esik egy booster: amikor az idegenek egytizede elpusztult, aztán kéttizede, és így tovább egészen mindegyikig, összesen tíz esés. Minden idegen számít, amellyel a kazamatát létrehozták, bárki pusztítja is el (ez a Klánkazamata ablak elpusztított idegeneinek száma); a zsákmányzónák hullámai és az idegenek, amelyeket a Hadúr hív, nem számítanak, így egy zóna nem hoz boostert. Minden esésnél minden pilóta fél percnyi ablakot kap, hogy kiválasszon magának egy ideiglenes boostert abból a háromból, amelyet a játék véletlenszerűen húz az ötből: **Sebzés** (a lézereid erősebben ütnek), **Életerő** (a hajód több hajótestet bír), **Pajzs** (a pajzsod többet bír), **Sebesség** (a hajód gyorsabban repül) és **Pajzstöltődés** (a pajzsod gyorsabban töltődik újra). Nyomj egy kártyára a kiválasztásához. Ha nem válaszolsz időben, a játék választ helyetted Életerőt, vagy a három közül az elsőt, ha az Életerő nincs köztük. Egy választás a 3. fokozaton 3%-ot ér, a 2. fokozaton 1,5%-ot, így tíz választás legfeljebb harminc százalékig adódik össze a 3. fokozaton és tizenöt százalékig a 2. fokozaton, bármilyen fajtákból. Az 1. fokozaton nincsenek boosterek.

A tizedik esés az utolsó idegennel jön. Az a csoport, amely minden idegent elpusztít, mielőtt a Hadúrral harcol, mind a tíz esést megkapja; az a csoport, amely kinyitja a Hadúr termét, és továbbrepül, azoknak az idegeneknek az eséseit kapja, amelyeket addig elpusztított, a megmaradt idegenek pedig maradnak, és még elpusztíthatók. Amint a Hadúrral való harc megkezdődött, többé nem esik booster.

A booster addig tart, amíg a kazamatát teljesítik. Ha kilépsz a kazamatából, vagy megsemmisülsz, elveszíted a boostereidet, és visszakapod őket, amikor újra beszállsz. A Klánkazamata ablak alatti jelzés felsorolja, mid van.

### A kártyák {#the-cards}

A kártyákat egyenként húzzák az alábbi készletből. Az esély egy kártyáé egy húzásban. Minden kártya minden kifizetett pilótához kerül, a felszerelés-kártyák is: a sok példányos kártya mindegyiküknek ennyi példányt ad, a felszerelés-kártya pedig mindegyiküknek egy saját, neki kovácsolt darabot. Aki nem kap fizetséget, kártyát sem kap, és egy kudarcot vallott kazamatában megnyitott zóna nem fizet semmit.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Kártya | 1. fokozat | 2. fokozat | 3. fokozat | Esély | Ki kapja |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2 000 | 3 000 | 5 000 | 23,9% | Minden kifizetett pilóta |
| Velkonite Reinforced Plate | 10 | 15 | 25 | 13,65% | Minden kifizetett pilóta |
| Velkonite | 200 | 300 | 500 | 13,65% | Minden kifizetett pilóta |
| Orvium | 200 | 300 | 500 | 13,65% | Minden kifizetett pilóta |
| Ultra Core | 5 000 | 7 500 | 12 500 | 11,4% | Minden kifizetett pilóta |
| Experimental Fusion Core | 3 000 | 4 500 | 7 500 | 9,1% | Minden kifizetett pilóta |
| Dark Matter | 10 | 16 | 24 | 9,1% | Minden kifizetett pilóta |
| Dark Matter Plate | 1 | 1 | 2 | 4,55% | Minden kifizetett pilóta |
| Starfire-III | – | – | 1 | 0,07% | Minden kifizetett pilóta |
| Helios Beam | – | – | 1 | 0,07% | Minden kifizetett pilóta |
| Engine III | – | – | 1 | 0,07% | Minden kifizetett pilóta |
| Adaptive Core III | – | – | 1 | 0,07% | Minden kifizetett pilóta |
| Heavy Shield Core | – | – | 1 | 0,07% | Minden kifizetett pilóta |
| Momentum Thruster IV | – | – | 1 | 0,07% | Minden kifizetett pilóta |
| Impulse Thruster IV | – | – | 1 | 0,07% | Minden kifizetett pilóta |
| Hull Plating II | – | – | 1 | 0,07% | Minden kifizetett pilóta |
| Hull Plating III | – | – | 1 | 0,07% | Minden kifizetett pilóta |
| Damage Amp IV | – | – | 1 | 0,07% | Minden kifizetett pilóta |
| Crit Amp IV | – | – | 1 | 0,07% | Minden kifizetett pilóta |
| Penetration Amp IV | – | – | 1 | 0,07% | Minden kifizetett pilóta |
| Capacity Shield Cell IV | – | – | 1 | 0,08% | Minden kifizetett pilóta |
| Absorption Shield Cell IV | – | – | 1 | 0,08% | Minden kifizetett pilóta |

- **Felszerelés**: Az egy példányos kártyák felszerelések; arányuk együtt: 1%

<!-- dungeons-cards:end -->

Az egy példányos kártyák **felszerelések**, és csak egy 3. fokozatú kazamata kínálhat ilyet. A felszerelést minden kifizetett pilótának kifizetéskor kovácsolják: mindegyik saját [bűvölési fokozatot](/wiki/06-Items/Overview.md#item-enchants) dob, ugyanolyan eséllyel, mint egy darab, amelyet a Gyártásban építesz, így a legtöbb Normál fokozatú, és egy magasabb fokozat, egészen az Örökig, bónuszokkal, ritka lelet.

## Fizetség {#pay}

Amikor a Hadúr elesik, minden pilóta, aki kiérdemelte, egyszer kap fizetséget a menetért. A csoport által választott kártyák a fokozat fizetségén felül járnak. Nincs világszorzó: a fizetség minden világban ugyanaz.

Az **Orvium Reinforced Plates** nem a szavazás kártyája. A fokozat fizetségének része, és minden kifizetett pilóta egyszer kapja meg a teljesítésért. A tárgyak, amelyeket a teljesítés fizet, nem eladhatók: nem [adhatod el őket az Aukción](/wiki/03-Mechanics/Auction.md#marketable-items).

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fokozat | Becsület | Tapasztalat | Kredit | Thulium | x4 lőszer | Orvium Reinforced Plates | PvE-ranglistapont |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **1. fokozat** | 25 000 | 600 000 | 5 000 000 | 4 000 | 4 000 | 5 | 600 |
| **2. fokozat** | 50 000 | 1 500 000 | 10 000 000 | 9 000 | 9 000 | 10 | 1 500 |
| **3. fokozat** | 100 000 | 2 400 000 | 17 500 000 | 15 000 | 15 000 | 15 | 2 400 |

<!-- dungeons-pay:end -->

### Ki kap fizetséget {#who-is-paid}

Ezek a szabályok azt döntik el, ki kap fizetést **a teljesítésért**. Egy menetet akkor is végig lehet játszani, ha nem fizet semmit, és az eredményképernyő megmondja, miért. A belépést soha nem tagadják meg amiatt, hogy egy fokozatért már fizettek neked: a teljesítés egyszerűen nem fizet. Az idegenek ugyanezeket a szabályokat olvassák, megsemmisítésenként, a harcban való részesedés kivételével ([mit fizetnek az idegenek](#what-the-aliens-pay)).

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Egy nap**: Egy fokozat egy pilótának UTC-naponként egyszer fizet: azon a napon, amikor a Hadúr elesik
- **Egy hét**: Egy pilóta UTC-hetenként legfeljebb 10 teljesített fokozatért kap fizetséget, hétfőtől vasárnapig
- **Bent**: Összesen legalább 2 perc
- **Részvétel a harcban**: Legalább egy ezek közül: a Hadúr hajótestéből és pajzsából ennyit sebzett le: 2%; megsemmisített 10 idegent a kazamatában; 50 000 értékben gyógyított más pilótákat a Hadúr elleni harc alatt

<!-- dungeons-rules:end -->

### Mennyit ér egy nap és egy hét {#what-a-day-and-a-week-are-worth}

Amit egy pilóta egy nap alatt kaphat, és a korlátok által megengedett legjobb héten. Az utolsó oszlop azt mutatja, mennyit ad a fizetség a [PvE-pontjaidhoz](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points).

<!-- dungeons-totals:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fizetség pilótánként | Becsület | Tapasztalat | Kredit | Thulium | x4 lőszer | Orvium Reinforced Plates | PvE-ranglistapont |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Egy nap, minden fokozat egyszer | 175 000 | 4 500 000 | 32 500 000 | 28 000 | 28 000 | 30 | 4 500 |
| A legjobb hét: 7 × 3. fokozat és 3 × 2. fokozat | 850 000 | 21 300 000 | 152 500 000 | 132 000 | 132 000 | 135 | 21 300 |

Egy kifizetett teljesítés tapasztalata beleszámít a PvE-ranglistapontjaidba: minden 1 000 tapasztalat egy pont.

<!-- dungeons-totals:end -->

### Mit fizetnek az idegenek {#what-the-aliens-pay}

A kazamata minden idegene fizet, amikor elesik, és zsákmányt hullat, mint a játék idegene, amelyről mintázták: egy Dungeon Goombah mint egy [Goombah](/wiki/04-Aliens/Goombah.md), egy Dungeon Crystalys és a Twinje mint egy [Crystalys](/wiki/04-Aliens/Crystalys.md), egy Dungeon Pirate mint a Pirate Boss ([Pirate-raj](/wiki/05-Swarms/Pirate-Swarm.md)). Amit egy idegen megsemmisítése fizet és hullat, az az eredetié **szorozva a hajótestük és pajzsuk együttes arányával**: az az idegen, amely ugyanolyan szívós, mint az eredetije, annyit fizet, amennyit az eredeti; a kétszer olyan szívós kétszer annyit fizet, és minden tárgyból kétszer annyit hullat, és így tovább. Az idegenek minden fajtájának szakasza [Az idegenek](#the-aliens) alatt megadja az arányt és egy megsemmisítés fizetségét minden fokozatban.

- **Ki kap fizetést.** Azok a pilóták, akik megsebezték az idegent, az okozott sebzésük szerint, ahogy a rajok idegeneinél: az a pilóta vagy csoport, amely csak súrolta, semmit sem kap, a csoport egyként kap fizetést, a csoporton belül pedig a roncs közelében lévő, a közelmúltban lőtt tagok szint szerint osztoznak a kifizetésen. Az a pilóta, aki nem sebezte az idegent, semmit sem kap érte, bármilyen közel repült is, és az az idegen, akit egy pilóta sem sebzett meg, senkinek sem fizet. Csak azok a pilóták tartoznak bele, akiket a fenti szabályok fizetnek: aki kilépett, nem volt bent elég ideje, ma már kapott fizetést a fokozatért, vagy megkapta a hét összes fizetett teljesítését, az idegenekért semmit sem kap, és a többiek kapják az ő részét. A megsemmisítés nem kéri a harcban való részesedést: az idegen megsebzése a részesedés. Ha egy csoport legtöbb sebzést okozó tagja megsemmisült vagy már nincs a térképen, a roncs közelében lévő, a közelmúltban lőtt tagok nélküle osztoznak.
- **Mit fizet.** Kreditet, Thuliumot, tapasztalatot és becsületet, megsemmisítésenként egyszer. A fizetség az, amit az eredeti Alphában fizet, minden világban: a kazamatának nincs világszorzója. A boostereid, a Premium, a formáció és a klánod bónuszai úgy számítanak, mint bármely megsemmisítésnél, a tapasztalat pedig a [PvE-pontjaidhoz](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points) számít, mint a teljesítésé.
- **A zsákmány.** Az eredeti esélyeivel kisorsolják, majd minden mennyiséget megszoroznak az aránnyal (egy egység töredéke esély még egyre). Ládaként hullik a roncsnál, előbb a legtöbb sebzést okozó pilótának és a klánjának, később a térképen bárkinek, aztán eltűnik. A térkép egyszerre csak bizonyos számú ládát bír el, ezért szedd fel őket menet közben, és ami a térképen marad, amikor a kazamata bezár, azzal együtt elvész. A teljesítés tárgyaival ellentétben ezek egy idegen közönséges zsákmányai: [eladhatod őket az Aukción](/wiki/03-Mechanics/Auction.md#marketable-items), ha a tárgy eladható.
- **Ami nem fizet.** A Hadúr nem fizet megsemmisítésért, csak a teljesítésért. A Goombahok, amelyeket hív, semmit sem fizetnek, mert a hívás addig újra jön, amíg a harc tart.
- **Nem a játék megsemmisítése.** A kazamatában elért megsemmisítés nem számít bele a küldetésekbe, az eredményekbe, a megsemmisítés-számlálókba, a wipe-pontokba, egy megsemmisítés PvE-pontjaiba, a drónokba és a P.E.T.-ekbe: egy Dungeon Goombah nem a játék Goombahja.
- **A korlátok.** A fenti napi és heti korlátok az idegenek fizetségét is ugyanúgy visszatartják, mint a teljesítését: aki ma már kapott fizetést a fokozatért, vagy megkapta a hét összes fizetett teljesítését, az idegenekért sem kap semmit, és egy megsemmisítés összegét a többiek kapják. Az a kazamata, amelyet nem teljesítenek, a megsemmisítéseket azoknak a pilótáknak fizeti, akiket a szabályok fizetnek, a teljesítésért pedig semmit.

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
- **Kifizetett pilóták**: Legalább 3 a kazamatában

<!-- dungeons-clan:end -->

## Tippek {#tips}

- Számold fel egy zóna hullámát, mielőtt megpróbálnád tartani a zónát, és harcolj a gyűrűben, ha az idegenek bejönnek.
- Vidd az egész csoportot egy zónába: minél több pilóta áll a gyűrűben, annál gyorsabban tartható.
- Keresd meg a labirintusban a Crystalysokat és a Twinjeiket: a Hadúr ajtaja akkor nyílik ki, ha háromnegyedük elpusztult, korábban nem. A többi idegen várhat, vagy őket is elpusztíthatod.
- Használd a falakat: a lézerek nem hatolnak át rajtuk, a Hadúr aurái piros gyűrűi megállnak náluk, és egy fal a Hadúr rakétáit is megállítja.
- Tarts meg egy EMP Charge-ot a Rakétazáporra.
- Amikor a Hadúr hívja a Goombahjait, előbb azokat pusztítsd el: nem sebezhető, amíg el nem tűntek. A Káoszzónában lépj ki a gyűrűből, mielőtt lősz.
- Figyeld az órát a Klánkazamata ablakban. Ha lejár az idő, a kazamata kudarcot vall, és a teljesítés nem fizet semmit.
