<!-- wiki-i18n source: 9b254c924e79c7e8 -->
<!-- wiki-i18n title: Szólókapuk -->
# Szólókapuk {#solo-gates}

<!-- wiki-search: solo gates; solo gate; gate; gates; galaxy gates; rift; rifts; alpha rift; beta breach; gamma foundry; delta siege; omega vault; chrono gate; chrono-gate; materializer; energy materializer; scan; spin; gate part; gate parts; guarantee; pity; consolation; wave; waves; nuke wave; skip; boss; lives; resume; abandon; speedrun; no death; challenge; achievement; thulium cap; szólókapuk; szólókapu; galaxiskapuk; kapualkatrész; alkatrész; energiamaterializáló; pörgetés; garancia; hullám; hullámok; életek; folytatás; feladás; halál nélkül; kihívás; eredmény; thulium-plafon -->

A **szólókapuk** a Galaxiskapuk öt kapuja, amelyeket egyedül repülsz be: **Alpha Rift**, **Beta Breach**, **Gamma Foundry**, **Delta Siege** és **Omega Vault**. Mindegyik külön üres aréna, ahol idegenek hullámai jönnek rád egymás után, és a végén egy boss vár. A kaput az **alkatrészeivel** építed, amelyeket az Energiamaterializáló Thuliummal való pörgetésével találsz, és egy teljesítés Creditet, Thuliumot, tapasztalatot, becsületet, ércet, lemezeket és lőszert fizet.

A szólókapu nem [klánkazamata](/wiki/03-Mechanics/Dungeons.md). A kazamata egy labirintus, amelyet egy klán nyit egy csoportnak, a végén egy Hadúrral; a szólókapu olyan aréna, amelyben csak te vagy, és rajtad kívül senki sem léphet be. A kettőnek külön szabályai, fizetése és korlátai vannak. A Galaxiskapuk oldalon ott van a **Chrono-Gate** is, amely nem repülőhely, hanem az a kapu, amely a wipe-hoz megnyitja a [Tranzittárolódat](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-): az alkatrészeit ugyanazokkal a pörgetésekkel találod.

## Dióhéjban {#at-a-glance}

<!-- solo-glance:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Kapuk**: 6: a Chrono-Gate és 5 szólókapu, Alpha Rift, Beta Breach, Gamma Foundry, Delta Siege és Omega Vault
- **Pörgetés**: 100 Thulium pörgetésenként, és 1, 5, 10 vagy 100 pörgetés egyszerre
- **Alkatrész esélye**: 13% pörgetésenként. Az alkatrész kapuját véletlenszerűen választják, és minden kapu a pörgetések 2,17%-át kapja. Ha a Chrono-Gate kész, a része kikerül a kerékből, és a szólókapuk egyenként megtartják a 2,17%-ot
- **Garancia**: 24 egymást követő alkatrész nélküli pörgetés után az esély minden pörgetéssel nő, 47 után pedig a következő pörgetés mindig talál egyet. Bármelyik kapu alkatrésze újraindítja a számlálást
- **Életek**: 3 kísérletenként; minden halál egyet elvesz
- **Visszaszámlálás**: 5 mp minden hullám előtt, az első és a boss hulláma előtt is. A hullámnak nincs időzítője, a menetnek sincs
- **Aréna**: 8 000 × 6 000 egység nyílt tér szikláktól mentesen, és egyedül vagy benne. Egy világban 16 van belőle, és ha mind foglalt, nem léphetsz be
- **Idegenek egyszerre**: Egy hullámból legfeljebb 60 él egyszerre, egy választható hullámból 250. A többi helyre vár
- **Bossok**: A bossot nem lehet sebezni 3 mp ideig, amikor fázist vált
- **Thulium-plafon**: A kapu legfeljebb a pörgetésekre költött Thulium 50%-át fizeti vissza. A többit levágják, és az eredmény megmondja, mennyit

<!-- solo-glance:end -->

## Kapualkatrészek megtalálása {#finding-gate-parts}

Nyisd meg a **Galaxiskapuk** oldalt, és pörgesd az Energiamaterializálót. Minden pörgetést Thuliummal kell fizetni, és legfeljebb egy alkatrészt talál, az alkatrész pedig a hat kapu valamelyikéhez tartozik, véletlenszerűen kiválasztva. A kapu megépítéséhez egy bizonyos számú alkatrész kell belőle, és az alkatrészek a tieid, amíg fel nem használod őket. Az a pörgetés, amely nem talál alkatrészt, nem vész el: nyereményt fizet ([lent](#a-spin-without-a-part)). Minden pörgetésért fizetni kell, a kész Chrono-Gate mellett is. Ha a Chrono-Gate kész, a pörgetésekből rá eső rész nem talál semmit, a szólókapuk pedig megtartják a saját esélyüket, így egy szólókapu alkatrésze ugyanannyiba kerül vele vagy nélküle.

A táblázat megadja minden kapu költségét alkatrészekben és azt, hogy **a garanciával** átlagosan mibe kerülnek (a pörgetés lottó, így a szerencsés pilóta kevesebbet fizet, a peches többet, a garancia által megengedett leghosszabb pörgetéssorozatig).

<!-- solo-parts:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Kapu | Alkatrész a teljesítéséhez | Alkatrész esélye pörgetésenként | Pörgetés átlagosan | Thulium átlagosan |
| :--- | ---: | ---: | ---: | ---: |
| **Chrono-Gate** | 2 | 2,17% | 91 | 9 093 |
| **Alpha Rift** | 11 | 2,17% | 500 | 50 011 |
| **Beta Breach** | 26 | 2,17% | 1 182 | 118 208 |
| **Gamma Foundry** | 54 | 2,17% | 2 455 | 245 508 |
| **Delta Siege** | 87 | 2,17% | 3 955 | 395 541 |
| **Omega Vault** | 108 | 2,17% | 4 910 | 491 017 |

<!-- solo-parts:end -->

A Chrono-Gate alkatrészei a wipe-nál nullára esnek vissza, és minden szezonban újra megtalálod őket. **A szólókapuk alkatrészei megmaradnak**, a garancia számlálója és a pörgetésekre költött és a kapuk által visszafizetett összeg nyilvántartása is; a wipe egyiket sem viszi el ([Kapuk és a wipe](#gates-and-the-wipe)).

### Pörgetés alkatrész nélkül {#a-spin-without-a-part}

A legtöbb pörgetés nem talál alkatrészt. Mindegyik egy nyereményt fizet, az alábbi esélyek szerint: a második szorzó vagy jobb lézerlőszert, a második vagy harmadik szint rakétacsomagját, és időnként egy [különleges tárgyat](/wiki/06-Items/Special-Items.md) vagy egy [konténert](/wiki/06-Items/Containers.md). A nyeremény, amely nem adható meg (például már a legtöbb van meg abból a különleges tárgyból), ugyanazzal a dobással lőszercsomaggá vagy rakétacsomaggá válik, így a pörgetés soha nem fizet kevesebbet a táblázatánál. A nyeremény egyértelműen kevesebbet ér, mint amennyibe a pörgetés kerül: a kapuk Thulium-nyelők.

<!-- solo-prizes:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Jutalom | Esély pörgetésenként |
| :--- | ---: |
| Egy konténer: Chroma Archive | 0,01% |
| Egy különleges tárgy: Magic Hammer | 0,2% |
| Egy különleges tárgy: Schematics | 0,2% |
| Egy különleges tárgy: Philosopher's Stone | 0,2% |
| Egy különleges tárgy: Forger's Seal | 0,2% |
| Egy különleges tárgy: Workforce Contract | 0,2% |
| Egy különleges tárgy: Tinkerer's Badge | 0,1% |
| Lézerlőszer: Advanced Plasma ×75 | 12,88% |
| Lézerlőszer: Antimatter Battery I ×62 | 8,59% |
| Lézerlőszer: Ultra Core ×40 | 8,59% |
| Lézerlőszer: Antimatter Battery II ×29 | 4,29% |
| Lézerlőszer: Dark Matter Ammo I ×31 | 4,29% |
| Lézerlőszer: Experimental Fusion Core ×17 | 2,15% |
| Lézerlőszer: Dark Matter Ammo II ×17 | 2,15% |
| Rakéták: Lancet II ×4 | 8,59% |
| Rakéták: Rivet II ×4 | 8,59% |
| Rakéták: Ember II ×4 | 8,59% |
| Rakéták: Scatter II ×4 | 8,59% |
| Rakéták: Lancet III ×1 | 2,15% |
| Rakéták: Rivet III ×1 | 2,15% |
| Rakéták: Ember III ×1 | 2,15% |
| Rakéták: Scatter III ×1 | 2,15% |

<!-- solo-prizes:end -->

## Belépés {#going-in}

A kaput a Galaxiskapuk oldalon **építed meg**, és a portálján **ugrasz be**. Az építés az állomásról megy, dokkolt hajóval, és repülés közben is: a **Galaxiskapuk ablak**, amelyet az eszköztár kapu gombja nyit meg, ugyanúgy pörget, épít és választ úti célt, mint az oldal. Ehhez kell:

- a kapu alkatrészei: **egyszer, az építéskor** veszik el őket, az elutasított építés semmit sem vesz el;
- nincs más nyitott szólómenet: egyszerre egy menetet játszol, és az elhagyott menetbe a portálján át lépsz vissza, vagy fel kell adnod, mielőtt másik kaput építesz;
- a fő szerver (a regionális szervereken nincsenek kapuk).

A felépített kapu a **bázisszektorodban** áll (`M-1`, `T-1` vagy `G-1`, a vállalatod szerint) egy róla elnevezett portálként, és a Galaxiskapuk oldal megmondja, hol. **Indulj el, repülj a portálhoz, és ugorj** át rajta, mint bármelyik portálon. Belépéskor szabad hasadéknak kell lennie a világodban: minden világban van belőlük egy bizonyos szám, és ha mind foglalt, vársz.

**A regionális szervereken (Singapore, US East).** Maga a kapu a fő szerveren marad: regionális szerveren semmit sem építenek, játszanak vagy fizetnek ki. Az épített kapu ott sem merül feledésbe: érkezéskor szólnak róla, és a kapud portálja ott is a bázisszektorodban áll. Ugorj át rajta, és visszakerülsz a fő szerverre, ahol a fent leírtak szerint indulsz a kapuba.

Egy üres aréna közepén landolsz, egyedül. Senki sem támadhat meg benne, és a Jump CPU és a Base CPU nem működik.

## Hogyan zajlik egy menet {#how-a-run-goes}

1. **Minden hullám előtt visszaszámlálás jön**, az első és a boss hulláma előtt is. A hullámnak nincs időzítője, és a menetnek sincs: addig tart, ameddig kell.
2. **Egy hullám** egy gyűrűn jelenik meg körülötted, és a kapu tempójában rád repül. Belőle egyszerre csak ennyi él, a többi helyre vár. Akkor ér véget, amikor az utolsó idegene meghal.
3. **Az előrehaladásod minden hullám után mentésre kerül.** Ha kilépsz, a folyamatban lévő hullám visszatérésedkor elölről kezdődik.
4. **A választható hullám** Seekerek hatalmas hulláma, és a Delta Siege-nek és az Omega Vaultnak van egy-egy. A visszaszámlálása alatt átugorhatod: ekkor késznek számít, és **semmit** sem fizet. Ha megküzdesz vele, a kilövései úgy fizetnek, mint bármelyik hullámé.
5. **Az utolsó hullám a boss.** Fázist vált, ahogy a hajóteste csökken, és minden váltásnál egy pillanatig nem sebezhető. Amikor a boss meghal, a menet teljesítve van, és a teljesítés azonnal kifizetésre kerül.

**Életek.** A halál egy életbe kerül, és a bázisodra küld, mint bármelyik másik halál; a menet vár rád, járó óra nélkül. Amíg a menet nyitva van, és az arénán kívül vagy, **a kapud portálja a bázisszektorodban áll**, és egy ugrás rajta át visszavisz a mentett hullámba a megmaradt életeiddel, ahogy a **Folytatás** is; nem kér új alkatrészt. Ha az utolsó életed is elfogy, a kísérlet véget ér, de a menet nyitva marad az utolsó teljesített hullámnál, és az újbóli belépés újratölti az életeidet. A **Kilépés**, a kijelentkezés vagy a világváltás szünetelteti a menetet életbe kerülés nélkül. A szerver újraindítása is nyitva tartja a menetedet. A **Feladás** feladja a menetet: az alkatrészei elvesznek, és a megölt idegeneket úgy fizetik ki, ahogy állnak. A **Folytatás** csak repülő hajóból működik: halál után a gombja az eredményképernyőn vár, egy sorral, amely megmondja, miért, amíg újra nem éledtél. Az újraéledt hajó korlátozott hajótesttel tér vissza; ha a hajótested a fele alatt van, az eredményképernyő figyelmeztet, a **Folytatás** pedig így is úgy visz vissza, ahogy vagy. A bázisod javítóhajói az aurájukon belül megjavítanak.

Minden világ ugyanazt a kaput vívja: az idegenek ereje és fizetése nem függ attól a világtól, amelyben repülsz.

### A hullámok {#the-waves}

Az idegenek a játék idegenei (Seeker, Phantasm, Bulwark, Goombah és Crystalys), a kapu által keményebbre vagy puhábbra téve. A tervezett idő az, amennyit a kapu egy pilótának a Lézertechnika kezdő szintjén vesz igénybe ([Pilótakészségek](/wiki/03-Mechanics/Pilot-Skills.md)); aki feljebb fejlesztette a Lézertechnikát, hamarabb végez.

Egyes hullámok **rajt** hoznak: a játék egy boss NPC-jét (Boss Seeker, Boss Phantasm, Boss Goombah vagy Boss Crystalys) az őreivel, akik egy csoportként támadnak. A raj minden hajója a hullámához tartozik, és a hullám akkor ér véget, amikor az utolsó is elpusztult. Úgy fizetnek, mint a hullám többi hajója, [az idegenek táblázatának](#the-aliens) értékeivel. **A boss NPC elejti a zsákmányát, ahogy a játék szektoraiban is**: érc, lemezek, lőszer és rakéták (hogy melyik mit ejt, azt [a rajok oldalain](/wiki/05-Swarms/Swarms.md) találod). Egy kapuban nincs felvehető láda: a zsákmány a fizetéssel jön, közvetlenül a készletedbe, és a fizetéshez hasonlóan menetenként csak egyszer. Az őrei nem ejtenek semmit, a kapuban sem, a szektorokban sem, és nem gyógyítják a bossukat, és nem térnek vissza. Az alábbi táblázat megmondja, hogy az egyes kapuk mely hullámai hoznak rajt.

<!-- solo-waves:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Kapu | Hullámok, a boss hulláma is | Idegenek a hullámokban | Boss NPC-k és rajok | Boss | Tervezett idő |
| :--- | ---: | :--- | :--- | :--- | :--- |
| **Alpha Rift** | 10 | 44 Seeker, 140 Phantasm | 5. hullám: 1 Seeker Swarm, 1 Phantasm Swarm | Enhanced Phantasm | 10–15 perc |
| **Beta Breach** | 14 | 64 Seeker, 158 Phantasm, 80 Bulwark, 20 Goombah | 4. hullám: 2 Seeker Swarm; 9. hullám: 1 Phantasm Swarm | Enhanced Bulwark | 15–25 perc |
| **Gamma Foundry** | 18 | 78 Phantasm, 117 Bulwark, 91 Goombah, 8 Crystalys | 4. hullám: 1 Phantasm Swarm; 9. hullám: 1 Goombah Swarm; 14. hullám: 1 Goombah Swarm | Elite Crystalys | 25–35 perc |
| **Delta Siege** | 22 | 250 Seeker, 200 Phantasm, 141 Bulwark, 130 Goombah, 12 Crystalys | 5. hullám: 2 Phantasm Swarm; 10. hullám: 2 Goombah Swarm; 15. hullám: 1 Goombah Swarm; 20. hullám: 1 Crystalys Swarm | Siege Construct | 35–45 perc |
| **Omega Vault** | 26 | 250 Seeker, 236 Phantasm, 170 Bulwark, 174 Goombah, 25 Crystalys | 6. hullám: 1 Goombah Swarm; 11. hullám: 2 Goombah Swarm; 16. hullám: 1 Crystalys Swarm; 22. hullám: 1 Phantasm Swarm | Omega Guardian | 50–60 perc |

- **Delta Siege**: 18. hullám (250 Seeker): választható, átugorhatod, amíg a visszaszámlálása fut, és nem fizet semmit
- **Omega Vault**: 17. hullám (250 Seeker): választható, átugorhatod, amíg a visszaszámlálása fut, és nem fizet semmit; a 22–24. hullámok elitek, ×1,5 hajótesttel, pajzzsal és sebzéssel

<!-- solo-waves:end -->

### A bossok {#the-bosses}

A boss egy idegen megnövelt hajója, saját hajótesttel, pajzzsal és sorozattal, amelyet a kapu vagy a világ egyetlen beállítása sem változtat. A fázis akkor kezdődik, amikor a boss hajóteste a táblázatbeli értékre esik: a pajzsa újra beállítható, a sorozata vagy az összes sebzése változik, és mozdulatba kezdhet. Minden mozdulatot bejelentenek: egy kör, egy gyűrű vagy egy jel a hajódon egy pillanattal a becsapódás előtt mutatja. A bossok által hívott idegenek nem fizetnek és nem ejtenek semmit.

<!-- solo-bosses:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Boss | Kapu | Hajótest | Pajzs | Lézersorozat |
| :--- | :--- | ---: | ---: | ---: |
| **Enhanced Phantasm** | Alpha Rift | 330 000 | 530 000 | 5 700–7 000 |
| **Enhanced Bulwark** | Beta Breach | 690 000 | 170 000 | 4 500–5 500 |
| **Elite Crystalys** | Gamma Foundry | 620 000 | 250 000 | 3 800–4 700 |
| **Siege Construct** | Delta Siege | 1 150 000 | 1 730 000 | 3 400–4 200 |
| **Omega Guardian** | Omega Vault | 1 340 000 | 840 000 | 2 600–3 200 |

| Boss | Fázis | Megmaradó hajótest | Mit csinál |
| :--- | :--- | :--- | :--- |
| **Enhanced Phantasm** | Enhanced Phantasm | 100%–0% | Csak lő. |
| **Enhanced Bulwark** | Shielded | 100%–50% | A pajzsa ×4 szorzóra van állítva a boss sajátjához képest. |
|  | Second attack | 50%–0% | A sorozata ×1,3. 4 Dormant Lance rakétát lő rád, egyenként 61 000 sebzéssel, 0,5 mp időközzel, 30 mp időközönként sortűzben. |
| **Elite Crystalys** | Elite | 100%–50% | Csak lő. |
|  | Reinforced | 50%–0% | A pajzsa ×2 szorzóra van állítva a boss sajátjához képest. 10 perc időközönként 10 Goombah hív, legfeljebb 10 él belőlük egyszerre; nem fizetnek és nem ejtenek semmit. |
| **Siege Construct** | Siege Construct | 100%–0% | 1 perc időközönként 3 sorozat, egyenként 8 meteor hullik, egyenként 5 500 sebzéssel mindenre, ami a becsapódási ponttól 420 egységen belül van, ebből 50% rád célozva; minden kör a becsapódás előtt 3 mp-mel mutatkozik. 6 Dormant Lance rakétát lő rád, egyenként 9 000 sebzéssel, 0,5 mp időközzel, 1 perc időközönként sortűzben. |
| **Omega Guardian** | Shield Fortress | 100%–70% | A pajzsa ×1,5 szorzóra van állítva a boss sajátjához képest. 40 mp időközönként 6 Bulwark hív, legfeljebb 12 él belőlük egyszerre; nem fizetnek és nem ejtenek semmit. |
|  | Swarm Protocol | 70%–35% | 25 mp időközönként 12 Phantasm hív, legfeljebb 24 él belőlük egyszerre; nem fizetnek és nem ejtenek semmit. 30 mp időközönként egy 140 000 sebzésű robbanás mindent eltalál a boss körüli 700 egységen belül; a gyűrű a becsapódás előtt 2 mp-mel mutatkozik. |
|  | Overload | 35%–0% | A pajzsa ×0,1 szorzóra van állítva a boss sajátjához képest. Az összes sebzése ×2,5. A fázisban töltött 2 perc után az összes sebzése még ×2 szorzót kap. 25 mp időközönként egy 28 000 sebzésű robbanás mindent eltalál a boss körüli 700 egységen belül; a gyűrű a becsapódás előtt 2 mp-mel mutatkozik. |

<!-- solo-bosses:end -->

## Mit fizet egy teljesítés {#what-a-clear-pays}

A teljesítés a táblázatát **egyszer** fizeti, egyben, abban a pillanatban, amikor a boss meghal: a Creditet, a Thuliumot, a tapasztalatot és a becsületet, az ércet, a lemezeket és a Power Core-okat, valamint a lőszert. A tapasztalat beleszámít a PvE-rangpontjaidba, ahogy a kazamatáé is.

<!-- solo-pay:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Kapu | Kredit | Thulium | XP | Becsület |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 450 000 | 5 000 | 70 000 | 1 000 |
| **Beta Breach** | 1 500 000 | 12 000 | 180 000 | 2 500 |
| **Gamma Foundry** | 4 000 000 | 25 000 | 400 000 | 5 500 |
| **Delta Siege** | 8 000 000 | 40 000 | 800 000 | 10 000 |
| **Omega Vault** | 15 000 000 | 60 000 | 1 500 000 | 20 000 |

- **Alpha Rift**: Ship Fragment ×300, Nyxite ×300, Daraxium ×400; lőszer: Advanced Plasma ×20 000, Ultra Core ×5 000, Experimental Fusion Core ×20 000
- **Beta Breach**: Ship Fragment ×700, Nyxite ×750, Daraxium ×800, Cataclysite ×400, Quorvium ×100; lőszer: Advanced Plasma ×50 000, Ultra Core ×20 000, Experimental Fusion Core ×30 000
- **Gamma Foundry**: Ship Fragment ×1 150, Nyxite ×1 000, Cataclysite ×900, Quorvium ×400, Power Core ×15; lőszer: Advanced Plasma ×30 000, Ultra Core ×60 000, Experimental Fusion Core ×50 000
- **Delta Siege**: Ship Fragment ×2 000, Nyxite ×1 750, Cataclysite ×1 500, Quorvium ×1 000, Reinforced Hull Plate ×70, Power Core ×40, Ancient Control Unit ×3; lőszer: Advanced Plasma ×40 000, Ultra Core ×90 000, Experimental Fusion Core ×75 000
- **Omega Vault**: Ship Fragment ×3 250, Nyxite ×2 750, Cataclysite ×2 250, Quorvium ×1 600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10; lőszer: Advanced Plasma ×50 000, Ultra Core ×100 000, Experimental Fusion Core ×100 000

<!-- solo-pay:end -->

**A Thulium plafonra van vágva.** A kapuk legfeljebb a pörgetésekre költött Thulium egy részét fizethetik vissza, az összes kapudon és az összes pörgetésedre számolva (a rész a legfelső listában van). Amit egy teljesítés és idegenei efölött fizetnének, levágják, és az eredményképernyő megmondja, mennyit. A Credit, a tapasztalat, a becsület, az érc, a lemezek és a lőszer soha nincs levágva.

### Az idegenek {#the-aliens}

Minden idegen, amelyet egy kapuban megölsz, az Alphában érvényes számokkal fizet, bármelyik világban repülsz: semmilyen világszorzó, booster vagy Prémium bónusz nem változtatja őket. Egy hullám az idegeneiért **egyszer** fizet menetenként, akárhányszor lépsz ki és vissza. A fizetés a menet minden szakaszának végén jön: amikor kilépsz, meghalsz, elfogynak az életeid, feladod vagy teljesíted. Egy szakasz kilövései csak a wipe-nál és a szerver újraindításakor maradnak kifizetetlenül, ha éppen bent vagy (a meneted nyitva marad, de annak a szakasznak a kilövései elvesznek). A kapu kilövései beleszámítanak a [küldetésekbe](/wiki/03-Mechanics/Quests.md#where-it-counts), amelyek nem neveznek meg szektort (például a Kihívások sorának nagy vadászatai), mégpedig abban a pillanatban, ahogy megtörténnek (egy hullám menetenként **egyszer** számít bele, ahogy egyszer fizet is), másra viszont nem számítanak: nem a kilövési statisztikákra, az eredmények számlálóira, a kill feedre és a drónjaid meg P.E.T.-jeid tapasztalatára sem. A tapasztalat, amelyet fizetnek, viszont beleszámít a PvE-rangpontjaidba, ahogy egy teljesítés tapasztalata is. Az idegenek zsákmánya a fizetéssel jön, közvetlenül a készletedbe.

<!-- solo-kills:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Idegen | Kredit | Thulium | XP | Becsület |
| :--- | ---: | ---: | ---: | ---: |
| **Seeker** | 1 000 | 4 | 100 | 2 |
| **Phantasm** | 3 000 | 12 | 300 | 6 |
| **Bulwark** | 5 000 | 25 | 800 | 10 |
| **Goombah** | 15 000 | 75 | 3 000 | 24 |
| **Crystalys** | 75 000 | 200 | 12 000 | 52 |
| **Boss Seeker** | 10 000 | 40 | 1 000 | 20 |
| **Seeker Slave** | 125 | 1 | 12 | 1 |
| **Boss Phantasm** | 39 000 | 195 | 7 800 | 62 |
| **Phantasm Guard** | 125 | 1 | 12 | 1 |
| **Boss Goombah** | 120 000 | 600 | 24 000 | 192 |
| **Goombah Guard** | 125 | 1 | 12 | 1 |
| **Boss Crystalys** | 393 750 | 1 050 | 63 000 | 273 |
| **Crystalys Guard** | 125 | 1 | 12 | 1 |

| Kapu | Kredit | Thulium | XP | Becsület |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 514 000 | 2 099 | 55 296 | 1 018 |
| **Beta Breach** | 1 298 500 | 5 939 | 187 744 | 2 470 |
| **Gamma Foundry** | 3 064 500 | 13 693 | 541 944 | 4 696 |
| **Delta Siege** | 5 239 625 | 22 338 | 882 676 | 7 850 |
| **Omega Vault** | 7 088 125 | 29 196 | 1 196 828 | 10 022 |

<!-- solo-kills:end -->

## Kihívások és eredmények {#challenges-and-achievements}

Két választható kihívás nyerhető bármelyik teljesítéssel, és mindegyik egy eredményt fizet és **nem fizet Thuliumot**. A **halál nélküli** teljesítés az, amelyben az egész menetben egyetlen halál sem volt, az összes belépésedet együtt számolva. A **speedrun** a kapu legrövidebb tervezett idején belüli teljesítés, az arénában töltött idővel számolva. A másik hat eredmény az egyes kapuk teljesítéséért jár, és mind az ötért:

<!-- solo-achievements:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Hasadék lezárva** (Gyakori): Teljesítsd egyedül az Alpha Riftet.
- **Áttörés lezárva** (Szokatlan): Teljesítsd egyedül a Beta Breacht.
- **Öntöde leállítva** (Ritka): Teljesítsd egyedül a Gamma Foundryt.
- **Ostrom megtörve** (Ritka): Törd meg egyedül a Delta Siege-et.
- **Trezor feltörve** (Epikus): Törd fel egyedül az Omega Vaultot.
- **Kapuőr** (Legendás): Teljesítsd mind az öt szóló kaput: Alpha, Beta, Gamma, Delta és Omega.
- **Sérthetetlen** (Ritka): Teljesíts egy szóló kaput úgy, hogy nem veszítesz el életet.
- **Verseny az idővel** (Ritka): Teljesíts egy szóló kaput a legrövidebb idején belül vagy gyorsabban: 10, 15, 25, 35 vagy 50 perc Alphától Omegáig.

<!-- solo-achievements:end -->

## Tárgyak egy kapuból {#items-from-a-gate}

Amit egy kapu ad, az **eladható**: az érc, a lemezek, a Power Core-ok, a lőszer és az idegenek zsákmánya felkerülhet az [Aukcióra](/wiki/03-Mechanics/Auction.md), mint egy zsákmány vagy küldetésjutalom, ugyanazokkal a kivételekkel, mint bármelyik tárgynál. Az alkatrész nélküli pörgetés nyereményei nem azok: pörgetésből jönnek, nem kapuból.

## Kapuk és a wipe {#gates-and-the-wipe}

- **A wipe véget vet minden nyitott menetnek**, és visszaadja az alkatrészeit. A menet nem megy át a következő szezonba.
- **A wipe-on át megmaradnak:** az öt szólókapu alkatrészei, a garancia számlálója, valamint a pörgetésekre költött és a kapuk által visszafizetett összeg nyilvántartása, így a Thulium plafonja szezonról szezonra tart. Az eredményeid örökre a tieid.
- **A wipe-nál elvesznek:** a Chrono-Gate alkatrészei, mint eddig. A pörgetéseid újra megveszik őket.
- **A fiók törlése** törli az alkatrészeket, a számlálót és a nyilvántartást.
