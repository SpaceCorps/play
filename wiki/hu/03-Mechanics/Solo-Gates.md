<!-- wiki-i18n source: b4ceac9f501a1ec2 -->
<!-- wiki-i18n title: Szólókapuk -->
# Szólókapuk {#solo-gates}

<!-- wiki-search: solo gates; solo gate; gate; gates; galaxy gates; rift; rifts; alpha rift; beta breach; gamma foundry; delta siege; omega vault; chrono gate; chrono-gate; materializer; energy materializer; scan; spin; gate part; gate parts; guarantee; pity; consolation; wave; waves; nuke wave; skip; boss; lives; resume; abandon; speedrun; no death; challenge; achievement; thulium cap; davidski's nightmare; nightmare; evil davidski; angry davidski; evil ships; golden ships; szólókapuk; szólókapu; galaxiskapuk; kapualkatrész; alkatrész; energiamaterializáló; pörgetés; garancia; hullám; hullámok; életek; folytatás; feladás; halál nélkül; kihívás; eredmény; thulium-plafon; evil hajók; arany hajók; dühös davidski -->

A **szólókapuk** a Galaxiskapuk öt kapuja, amelyeket egyedül repülsz be: **Alpha Rift**, **Beta Breach**, **Gamma Foundry**, **Delta Siege** és **Omega Vault**. Mindegyik külön üres aréna, ahol idegenek hullámai jönnek rád egymás után, és a végén egy boss vár. A **Davidski's Nightmare** egy hatodik kapu, az említett öttől elkülönülve: a hullámai nem idegenekből állnak, hanem **Evil hajókból**, a játék olyan hajóiból, amelyek ellened repülnek, és ez a legdrágább kapu az építéshez. A kaput az **alkatrészeivel** építed, amelyeket az Energiamaterializáló Thuliummal való pörgetésével találsz, és egy teljesítés Creditet, Thuliumot, tapasztalatot, becsületet, ércet, lemezeket és lőszert fizet.

A szólókapu nem [klánkazamata](/wiki/03-Mechanics/Dungeons.md). A kazamata egy labirintus, amelyet egy klán nyit egy csoportnak, a végén egy Hadúrral; a szólókapu olyan aréna, amelyben csak te vagy, és rajtad kívül senki sem léphet be. A kettőnek külön szabályai, fizetése és korlátai vannak. A Galaxiskapuk oldalon ott van a **Chrono-Gate** is, amely nem repülőhely, hanem az a kapu, amely a wipe-hoz megnyitja a [Tranzittárolódat](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-): az alkatrészeit ugyanazokkal a pörgetésekkel találod.

## Dióhéjban {#at-a-glance}

<!-- solo-glance:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Kapuk**: 7: a Chrono-Gate és 6 szólókapu, Alpha Rift, Beta Breach, Gamma Foundry, Delta Siege, Omega Vault és Davidski's Nightmare
- **Pörgetés**: 100 Thulium pörgetésenként, és 1, 5, 10, 100 vagy 1 000 pörgetés egyszerre
- **Alkatrész esélye**: 13% pörgetésenként, bármelyik kategóriát pörgeted. Az alkatrész az adott kategória kapuinak egyikéhez tartozik, mindegyik egyformán valószínű: a Chrono-Gate egyedül megkapja az egészet, Alpha Rift, Beta Breach és Gamma Foundry egyenként 4,33%-ot kap, Delta Siege és Omega Vault pedig egyenként 6,5%-ot. Ha a Chrono-Gate kész, a kategóriájában nincs mit pörgetni
- **Garancia**: 24 egymást követő alkatrész nélküli pörgetés után az esély minden pörgetéssel nő, 47 után pedig a következő pörgetés mindig talál egyet. Bármelyik kapu alkatrésze újraindítja a számlálást
- **Életek**: 3 kísérletenként; minden halál egyet elvesz
- **Visszaszámlálás**: 5 mp minden hullám előtt, az első és a boss hulláma előtt is. A hullámnak nincs időzítője, a menetnek sincs
- **Aréna**: 8 000 × 6 000 egység nyílt tér szikláktól mentesen, és egyedül vagy benne. Egy világban 16 van belőle, és ha mind foglalt, nem léphetsz be
- **Idegenek egyszerre**: Egy hullámból legfeljebb 60 él egyszerre, egy választható hullámból 250. A többi helyre vár
- **Bossok**: A bossot nem lehet sebezni 3 mp ideig, amikor fázist vált
- **Thulium-plafon**: A kapu legfeljebb a pörgetésekre költött Thulium 50%-át fizeti vissza. A többit levágják, és az eredmény megmondja, mennyit

<!-- solo-glance:end -->

## Kapualkatrészek megtalálása {#finding-gate-parts}

Nyisd meg a **Galaxiskapuk** oldalt, és pörgesd az Energiamaterializálót. Minden pörgetést Thuliummal kell fizetni, és legfeljebb egy alkatrészt talál. Előbb válassz egy **kategóriát**: a **Chrono-Gate**-et, az **Alpha–Gamma**-t (Alpha Rift, Beta Breach és Gamma Foundry), a **Delta–Omega**-t (Delta Siege és Omega Vault) vagy a **Davidski's Nightmare**-t, amelynek saját kategóriája van. Az alkatrész esélye minden kategóriában ugyanannyi, az alkatrész pedig a választott kategória kapuinak egyikéhez tartozik, mindegyik egyformán valószínű. A kapu megépítéséhez egy bizonyos számú alkatrész kell belőle, és az alkatrészek a tieid, amíg fel nem használod őket. Az a pörgetés, amely nem talál alkatrészt, nem vész el: nyereményt fizet ([lent](#a-spin-without-a-part)). Minden pörgetésért fizetni kell. Ha a Chrono-Gate kész, a gombja le van zárva, mert nincs benne mit találni, a másik két kategória pedig megtartja az esélyét, így egy szólókapu alkatrésze ugyanannyiba kerül vele vagy nélküle.

A táblázat megadja minden kapu költségét alkatrészekben és azt, hogy **a garanciával** átlagosan mibe kerülnek, ha azt a kategóriát pörgeted, amelyben a kapu van (a pörgetés lottó, így a szerencsés pilóta kevesebbet fizet, a peches többet, a garancia által megengedett leghosszabb pörgetéssorozatig).

<!-- solo-parts:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Kapu | Alkatrész a teljesítéséhez | Alkatrész esélye pörgetésenként | Pörgetés átlagosan | Thulium átlagosan |
| :--- | ---: | ---: | ---: | ---: |
| **Chrono-Gate** | 13 | 13% | 99 | 9 851 |
| **Alpha Rift** | 14 | 4,33% | 318 | 31 825 |
| **Beta Breach** | 33 | 4,33% | 750 | 75 016 |
| **Gamma Foundry** | 68 | 4,33% | 1 546 | 154 579 |
| **Delta Siege** | 96 | 6,5% | 1 455 | 145 486 |
| **Omega Vault** | 119 | 6,5% | 1 803 | 180 343 |
| **Davidski's Nightmare** | 238 | 13% | 1 803 | 180 343 |

<!-- solo-parts:end -->

A Chrono-Gate alkatrészei a wipe-nál nullára esnek vissza, és minden szezonban újra megtalálod őket. **A szólókapuk alkatrészei megmaradnak**, a garancia számlálója és a pörgetésekre költött és a kapuk által visszafizetett összeg nyilvántartása is; a wipe egyiket sem viszi el ([Kapuk és a wipe](#gates-and-the-wipe)).

### Pörgetés alkatrész nélkül {#a-spin-without-a-part}

A legtöbb pörgetés nem talál alkatrészt. Mindegyik egy nyereményt fizet, az alábbi esélyek szerint: a második szorzó vagy jobb lézerlőszert, a második vagy harmadik szint rakétacsomagját, és időnként egy [különleges tárgyat](/wiki/06-Items/Special-Items.md) vagy egy [konténert](/wiki/06-Items/Containers.md). A nyeremény, amely nem adható meg (például mert a különleges tárgyak vagy a konténerek ki vannak kapcsolva), ugyanazzal a dobással lőszercsomaggá vagy rakétacsomaggá válik, így a pörgetés soha nem fizet kevesebbet a táblázatánál. A nyeremény egyértelműen kevesebbet ér, mint amennyibe a pörgetés kerül: a kapuk Thulium-nyelők.

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
- a kapu még nincs felépítve: **minden** kaput felépíthetsz egyszerre, mindegyikhez külön portál tartozik, és egyszerre egyet játszol; a már felépített kapuba a portálján át lépsz be, vagy feladod, mielőtt újra felépítenéd;
- a fő szerver (kaput csak a fő szerveren építenek: regionális szerveren előbb visszatérsz a bázisra).

A felépített kapu a **bázisszektorodban** áll (`M-1`, `T-1` vagy `G-1`, a vállalatod szerint) egy róla elnevezett portálként, és a Galaxiskapuk oldal megmondja, hol. **Indulj el, repülj a portálhoz, és ugorj** át rajta, mint bármelyik portálon. Belépéskor szabad hasadéknak kell lennie a világodban: minden világban van belőlük egy bizonyos szám, és ha mind foglalt, vársz. Csak a **saját** kapuidat látod: más pilóták kapuinak portáljai ugyanabban a szektorban nem jelennek meg számodra. Mind az öt kaput **egyszerre felépítheted**, mindegyiknek saját portálja van, és egyszerre egyet játszol: **amíg arénában vagy, egyik portálod sem áll**, és ha kijössz, visszatérnek.

**A regionális szervereken (Singapore, US East).** Az épített kaput ott is lehet játszani. A kapud portálja regionális szerveren ugyanúgy a bázisszektorodban áll, mint a fő szerveren, és érkezéskor szólnak róla. **Ugorj át rajta, és a szerver egyik arénájába kerülsz**, a fő szerver helyett annak késleltetésével. Egy regionális szerveren világonként csak **két aréna** van, a fő szerveren jóval több: ha mindkettő foglalt, vársz, ahogy a fő szerveren is várnál egy szabad hasadékra. A fő szerver marad az egyetlen hely, amely a menetedet, az alkatrészeidet és a kifizetésedet nyilvántartja: a kifizetés akkor kerül a pénztárcádba, amikor a fő szerver megszámolta a menetet, pár másodperccel a vége után, a **repülési ablakod pénztárcája pedig dokkoláskor frissül**. A következő menetedbe csak akkor lépsz be, ha az utolsót már megszámolták. Az arénában otthagyott menetbe a portálon át lépsz vissza; ha fel akarod adni, azt az arénában vagy az állomáson teheted meg. Ha egy regionális szerver aréna-funkciója ki van kapcsolva, a portálja helyette visszavisz a fő szerverre, ahol a fent leírtak szerint indulsz a kapuba. Hogy mi más működik regionális szerveren, azt a [Szerverek](/wiki/03-Mechanics/Servers.md) írja le.

Egy üres aréna közepén landolsz, egyedül. Senki sem támadhat meg benne, és a Jump CPU és a Base CPU nem működik.

## Hogyan zajlik egy menet {#how-a-run-goes}

1. **Minden hullám előtt visszaszámlálás jön**, az első és a boss hulláma előtt is. A hullámnak nincs időzítője, és a menetnek sincs: addig tart, ameddig kell.
2. **Egy hullám** egy gyűrűn jelenik meg körülötted, és a kapu tempójában rád repül. Belőle egyszerre csak ennyi él, a többi helyre vár. Akkor ér véget, amikor az utolsó idegene meghal.
3. **Az előrehaladásod minden hullám után mentésre kerül.** Ha kilépsz, a folyamatban lévő hullám visszatérésedkor elölről kezdődik.
4. **A választható hullám** Seekerek hatalmas hulláma, és a Delta Siege-nek és az Omega Vaultnak van egy-egy. A visszaszámlálása alatt átugorhatod: ekkor késznek számít, és **semmit** sem fizet. Ha megküzdesz vele, a kilövései úgy fizetnek, mint bármelyik hullámé.
5. **Az utolsó hullám a boss.** Fázist vált, ahogy a hajóteste csökken, és minden váltásnál egy pillanatig nem sebezhető. Amikor a boss meghal, a menet teljesítve van, és a teljesítés azonnal kifizetésre kerül.

**Életek.** A halál egy életbe kerül, és a bázisodra küld, mint bármelyik másik halál; a menet vár rád, járó óra nélkül. Amíg a menet nyitva van, és az arénán kívül vagy, **minden felépített kapud portálja a bázisszektorodban áll**, és egy ugrás bármelyiken át visszavisz a mentett hullámba a megmaradt életeiddel, ahogy a **Folytatás** is; nem kér új alkatrészt. Ha az utolsó életed is elfogy, a kísérlet véget ér, de a menet nyitva marad az utolsó teljesített hullámnál, és az újbóli belépés újratölti az életeidet. A **Kilépés**, a kijelentkezés vagy a világváltás szünetelteti a menetet életbe kerülés nélkül. A szerver újraindítása is nyitva tartja a menetedet. A **Feladás** feladja a menetet: az alkatrészei elvesznek, és a megölt idegeneket úgy fizetik ki, ahogy állnak. A **Folytatás** csak repülő hajóból működik: halál után a gombja az eredményképernyőn vár, egy sorral, amely megmondja, miért, amíg újra nem éledtél. Az újraéledt hajó korlátozott hajótesttel tér vissza; ha a hajótested a fele alatt van, az eredményképernyő figyelmeztet, a **Folytatás** pedig így is úgy visz vissza, ahogy vagy. A bázisod javítóhajói az aurájukon belül megjavítanak.

Minden világ ugyanazt a kaput vívja: az idegenek ereje és fizetése nem függ attól a világtól, amelyben repülsz.

### A hullámok {#the-waves}

Az idegenek a játék idegenei (Seeker, Phantasm, Bulwark, Goombah és Crystalys), a kapu által keményebbre vagy puhábbra téve. A **Davidski's Nightmare** hullámai ehelyett **Evil hajók**: mindegyik hajótestből egy, amelyet egy pilóta repülhet, a Dormant-raj színeiben. A kis hajótestek jönnek először, és minden hullám többet és nagyobbakat hoz belőlük, a boss előtti utolsó hullámig. Egy Evil hajó azt viszi, amit egy pilóta hajója: lézereket, egy **rakétát**, amelyet néhány másodpercenként rád lő, és egy **javítódrónt**, amely gyógyítja a hajótestét, amíg semmi sem találja el, így az a hajó, amelyet békén hagysz, begyógyul. A tervezett idő az, amennyit a kapu egy pilótának a Lézertechnika kezdő szintjén vesz igénybe ([Pilótakészségek](/wiki/03-Mechanics/Pilot-Skills.md)); aki feljebb fejlesztette a Lézertechnikát, hamarabb végez.

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
| **Davidski's Nightmare** | 13 | 50 Evil Protos, 66 Evil Kitefin, 31 Evil Ostirion, 19 Evil Nomad, 22 Evil Paragon, 7 Evil Storm, 8 Evil Wraith, 2 Evil Ironclad |  | Evil Davidski | 45–60 perc |

- **Delta Siege**: 18. hullám (250 Seeker): választható, átugorhatod, amíg a visszaszámlálása fut, és nem fizet semmit
- **Omega Vault**: 17. hullám (250 Seeker): választható, átugorhatod, amíg a visszaszámlálása fut, és nem fizet semmit; a 22–24. hullámok elitek, ×1,5 hajótesttel, pajzzsal és sebzéssel

<!-- solo-waves:end -->

### A bossok {#the-bosses}

A boss egy idegen megnövelt hajója, saját hajótesttel, pajzzsal és sorozattal, amelyet a kapu vagy a világ egyetlen beállítása sem változtat. A fázis akkor kezdődik, amikor a boss hajóteste a táblázatbeli értékre esik: a pajzsa újra beállítható, a sorozata vagy az összes sebzése változik, és mozdulatba kezdhet. Minden mozdulatot bejelentenek: egy kör, egy gyűrű vagy egy jel a hajódon egy pillanattal a becsapódás előtt mutatja. A bossok által hívott idegenek nem fizetnek és nem ejtenek semmit.

Az **Evil Davidski**, a Davidski's Nightmare bossa, Davidski saját Ironcladját repüli sötétebb aranyban. Dormant Lance-eket lő, vezérelt rakétákat, amelyek hosszú úton követnek, és meteorokkal, egy gyűrűvel és általa hívott Evil hajókkal harcol. A hajótestének harmadánál **DÜHÖS DAVIDSKI**-vá válik: szól a dallama, erősebben üt, és körülötte megjelenik **a játék minden hajójának egy arany hajója**. Amíg bármelyik arany hajó él, egyáltalán nem sebezhető: a lézereid és a rakétáid nem tudnak ráreteszelni, és semmi, amit teszel, nem éri a hajótestét vagy a pajzsát, ezért előbb átvágod magad rajtuk. Amikor az utolsó elesik, a védelem végleg megszűnik. Minden hullám elején a saját ablakából gúnyol téged. Megölése Davidski megöléseként számít azoknak a küldetéseknek, amelyek ilyet kérnek, kapuban éppúgy, mint a veszélyes szektorokban. A nem naprakész játék nem mutatja a kaput.

<!-- solo-bosses:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Boss | Kapu | Hajótest | Pajzs | Lézersorozat |
| :--- | :--- | ---: | ---: | ---: |
| **Enhanced Phantasm** | Alpha Rift | {{guide:vitals.hull@Enhanced Phantasm}} | {{guide:vitals.shield@Enhanced Phantasm}} | {{guide:vitals.dps*0.9007633587786259~1.099236641221374@Enhanced Phantasm}} |
| **Enhanced Bulwark** | Beta Breach | {{guide:vitals.hull@Enhanced Bulwark}} | {{guide:vitals.shield@Enhanced Bulwark}} | {{guide:vitals.dps*0.9019607843137255~1.0980392156862746@Enhanced Bulwark}} |
| **Elite Crystalys** | Gamma Foundry | {{guide:vitals.hull@Elite Crystalys}} | {{guide:vitals.shield@Elite Crystalys}} | {{guide:vitals.dps*0.896551724137931~1.103448275862069@Elite Crystalys}} |
| **Siege Construct** | Delta Siege | {{guide:vitals.hull@Siege Construct}} | {{guide:vitals.shield@Siege Construct}} | {{guide:vitals.dps*0.8974358974358975~1.1025641025641026@Siege Construct}} |
| **Omega Guardian** | Omega Vault | {{guide:vitals.hull@Omega Guardian}} | {{guide:vitals.shield@Omega Guardian}} | {{guide:vitals.dps*0.896551724137931~1.103448275862069@Omega Guardian}} |
| **Evil Davidski** | Davidski's Nightmare | {{guide:vitals.hull@Evil Davidski}} | {{guide:vitals.shield@Evil Davidski}} | {{guide:vitals.dps*0.896551724137931~1.103448275862069@Evil Davidski}} |

| Boss | Fázis | Megmaradó hajótest | Mit csinál |
| :--- | :--- | :--- | :--- |
| **Enhanced Phantasm** | Enhanced Phantasm | 100%–66% | Csak lő. |
|  | Reinforced | 66%–33% | A pajzsa ×1 szorzóra van állítva a boss sajátjához képest. 10 perc időközönként 4 Phantasm hív, legfeljebb 4 él belőlük egyszerre; nem fizetnek és nem ejtenek semmit. |
|  | Second attack | 33%–0% | A sorozata ×1,3. 30 mp időközönként egy {{guide:behaviour.ability:phases.ringBlast@Enhanced Phantasm}} sebzésű robbanás mindent eltalál a boss körüli 500 egységen belül; a gyűrű a becsapódás előtt 2 mp-mel mutatkozik. |
| **Enhanced Bulwark** | Shielded | 100%–66% | A pajzsa ×4 szorzóra van állítva a boss sajátjához képest. |
|  | Rocket barrage | 66%–33% | 4 Dormant Lance rakétát lő rád, egyenként {{guide:behaviour.ability:phases.rocketBarrage@Enhanced Bulwark}} sebzéssel, 0,5 mp időközzel, 30 mp időközönként sortűzben. |
|  | Second attack | 33%–0% | A sorozata ×1,3. 10 perc időközönként 4 Phantasm hív, legfeljebb 4 él belőlük egyszerre; nem fizetnek és nem ejtenek semmit. |
| **Elite Crystalys** | Elite | 100%–66% | Csak lő. |
|  | Renewed shield | 66%–33% | A pajzsa ×1 szorzóra van állítva a boss sajátjához képest. |
|  | Reinforced | 33%–0% | A pajzsa ×2 szorzóra van állítva a boss sajátjához képest. 10 perc időközönként 10 Goombah hív, legfeljebb 10 él belőlük egyszerre; nem fizetnek és nem ejtenek semmit. |
| **Siege Construct** | Siege Construct | 100%–66% | 1 perc időközönként 3 sorozat, egyenként 8 meteor hullik, egyenként {{guide:behaviour.ability:phases.meteors@Siege Construct}} sebzéssel mindenre, ami a becsapódási ponttól 420 egységen belül van, ebből 50% rád célozva; minden kör a becsapódás előtt 3 mp-mel mutatkozik. |
|  | Rocket barrage | 66%–33% | 1 perc időközönként 3 sorozat, egyenként 8 meteor hullik, egyenként {{guide:behaviour.ability:phases.meteors2@Siege Construct}} sebzéssel mindenre, ami a becsapódási ponttól 420 egységen belül van, ebből 50% rád célozva; minden kör a becsapódás előtt 3 mp-mel mutatkozik. 6 Dormant Lance rakétát lő rád, egyenként {{guide:behaviour.ability:phases.rocketBarrage@Siege Construct}} sebzéssel, 0,5 mp időközzel, 1 perc időközönként sortűzben. |
|  | Frenzy | 33%–0% | 30 mp időközönként 3 sorozat, egyenként 8 meteor hullik, egyenként {{guide:behaviour.ability:phases.meteors3@Siege Construct}} sebzéssel mindenre, ami a becsapódási ponttól 420 egységen belül van, ebből 50% rád célozva; minden kör a becsapódás előtt 3 mp-mel mutatkozik. 6 Dormant Lance rakétát lő rád, egyenként {{guide:behaviour.ability:phases.rocketBarrage2@Siege Construct}} sebzéssel, 0,5 mp időközzel, 30 mp időközönként sortűzben. |
| **Omega Guardian** | Shield Fortress | 100%–66% | A pajzsa ×1,5 szorzóra van állítva a boss sajátjához képest. 40 mp időközönként 6 Bulwark hív, legfeljebb 12 él belőlük egyszerre; nem fizetnek és nem ejtenek semmit. |
|  | Swarm Protocol | 66%–33% | 25 mp időközönként 12 Phantasm hív, legfeljebb 24 él belőlük egyszerre; nem fizetnek és nem ejtenek semmit. 30 mp időközönként egy {{guide:behaviour.ability:phases.ringBlast@Omega Guardian}} sebzésű robbanás mindent eltalál a boss körüli 700 egységen belül; a gyűrű a becsapódás előtt 2 mp-mel mutatkozik. |
|  | Overload | 33%–0% | A pajzsa ×0,1 szorzóra van állítva a boss sajátjához képest. Az összes sebzése ×2,5. A fázisban töltött 2 perc után az összes sebzése még ×2 szorzót kap. 25 mp időközönként egy {{guide:behaviour.ability:phases.ringBlast2@Omega Guardian}} sebzésű robbanás mindent eltalál a boss körüli 700 egységen belül; a gyűrű a becsapódás előtt 2 mp-mel mutatkozik. |
| **Evil Davidski** | Evil Davidski | 100%–66% | Csak lő. |
|  | Davidski attacks | 66%–33% | 6 Dormant Lance rakétát lő rád, egyenként {{guide:behaviour.ability:phases.rocketBarrage@Evil Davidski}} sebzéssel, 0,5 mp időközzel, 30 mp időközönként sortűzben. 1 perc időközönként 2 sorozat, egyenként 8 meteor hullik, egyenként {{guide:behaviour.ability:phases.meteors@Evil Davidski}} sebzéssel mindenre, ami a becsapódási ponttól 400 egységen belül van, ebből 50% rád célozva; minden kör a becsapódás előtt 3 mp-mel mutatkozik. 40 mp időközönként 5 Evil Protos hív, legfeljebb 10 él belőlük egyszerre; nem fizetnek és nem ejtenek semmit. |
|  | Angry | 33%–0% | A pajzsa ×0,5 szorzóra van állítva a boss sajátjához képest. Az összes sebzése ×1,5. A fázisban töltött 8 perc után az összes sebzése még ×2 szorzót kap. 6 Dormant Lance rakétát lő rád, egyenként {{guide:behaviour.ability:phases.rocketBarrage2@Evil Davidski}} sebzéssel, 0,4 mp időközzel, 30 mp időközönként sortűzben. 1 perc időközönként 3 sorozat, egyenként 8 meteor hullik, egyenként {{guide:behaviour.ability:phases.meteors2@Evil Davidski}} sebzéssel mindenre, ami a becsapódási ponttól 420 egységen belül van, ebből 50% rád célozva; minden kör a becsapódás előtt 3 mp-mel mutatkozik. 45 mp időközönként egy {{guide:behaviour.ability:phases.ringBlast@Evil Davidski}} sebzésű robbanás mindent eltalál a boss körüli 700 egységen belül; a gyűrű a becsapódás előtt 2 mp-mel mutatkozik. 40 mp időközönként 3 Evil Kitefin hív, legfeljebb 6 él belőlük egyszerre; nem fizetnek és nem ejtenek semmit. |

<!-- solo-bosses:end -->

## Mit fizet egy teljesítés {#what-a-clear-pays}

A teljesítés a táblázatát **egyszer** fizeti, egyben, abban a pillanatban, amikor a boss meghal: a Creditet, a Thuliumot, a tapasztalatot és a becsületet, az ércet, a lemezeket és a Power Core-okat, valamint a lőszert. A tapasztalat és a becsület beleszámít a PvE-rangpontjaidba, ahogy a kazamatáé is.

<!-- solo-pay:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Kapu | Kredit | Thulium | XP | Becsület |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 450 000 | 5 000 | 70 000 | 1 000 |
| **Beta Breach** | 1 500 000 | 12 000 | 180 000 | 2 500 |
| **Gamma Foundry** | 4 000 000 | 25 000 | 400 000 | 5 500 |
| **Delta Siege** | 8 000 000 | 40 000 | 800 000 | 10 000 |
| **Omega Vault** | 15 000 000 | 60 000 | 1 500 000 | 20 000 |
| **Davidski's Nightmare** | 15 000 000 | 60 000 | 1 500 000 | 20 000 |

- **Alpha Rift**: Ship Fragment ×300, Nyxite ×300, Daraxium ×400, Echo Shard ×4, Lattice Shard ×6; lőszer: Advanced Plasma ×15 000, Ultra Core ×3 750, Experimental Fusion Core ×15 000
- **Beta Breach**: Ship Fragment ×700, Nyxite ×750, Daraxium ×800, Cataclysite ×400, Quorvium ×100, Echo Shard ×9, Lattice Shard ×13; lőszer: Advanced Plasma ×37 500, Ultra Core ×15 000, Experimental Fusion Core ×22 500
- **Gamma Foundry**: Ship Fragment ×1 150, Nyxite ×1 000, Cataclysite ×900, Quorvium ×400, Power Core ×15, Echo Shard ×18, Lattice Shard ×27; lőszer: Advanced Plasma ×22 500, Ultra Core ×45 000, Experimental Fusion Core ×37 500
- **Delta Siege**: Ship Fragment ×2 000, Nyxite ×1 750, Cataclysite ×1 500, Quorvium ×1 000, Reinforced Hull Plate ×70, Power Core ×40, Ancient Control Unit ×3, Echo Shard ×29, Lattice Shard ×44; lőszer: Advanced Plasma ×30 000, Ultra Core ×67 500, Experimental Fusion Core ×56 250
- **Omega Vault**: Ship Fragment ×3 250, Nyxite ×2 750, Cataclysite ×2 250, Quorvium ×1 600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10, Echo Shard ×34, Lattice Shard ×54; lőszer: Advanced Plasma ×37 500, Ultra Core ×75 000, Experimental Fusion Core ×75 000
- **Davidski's Nightmare**: Ship Fragment ×3 250, Nyxite ×2 750, Cataclysite ×2 250, Quorvium ×1 600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10, Echo Shard ×34, Lattice Shard ×54; lőszer: Advanced Plasma ×37 500, Ultra Core ×75 000, Experimental Fusion Core ×75 000
- **Heartshards**: 1 az évad során az egyes kapuk első teljesítésekor, és 5% eséllyel még 1 minden teljesítéskor.

<!-- solo-pay:end -->

**A Thulium plafonra van vágva.** A kapuk legfeljebb a pörgetésekre költött Thulium egy részét fizethetik vissza, az összes kapudon és az összes pörgetésedre számolva (a rész a legfelső listában van). Amit egy teljesítés és idegenei efölött fizetnének, levágják, és az eredményképernyő megmondja, mennyit. A Credit, a tapasztalat, a becsület, az érc, a lemezek és a lőszer soha nincs levágva.

### Az idegenek {#the-aliens}

Minden idegen, amelyet egy kapuban megölsz, az Alphában érvényes számokkal fizet, bármelyik világban repülsz: semmilyen világszorzó, booster vagy Prémium bónusz nem változtatja őket. Egy hullám az idegeneiért **egyszer** fizet menetenként, akárhányszor lépsz ki és vissza. A fizetés a menet minden szakaszának végén jön: amikor kilépsz, meghalsz, elfogynak az életeid, feladod vagy teljesíted. Egy szakasz kilövései csak a wipe-nál és a szerver újraindításakor maradnak kifizetetlenül, ha éppen bent vagy (a meneted nyitva marad, de annak a szakasznak a kilövései elvesznek). A kapu kilövései beleszámítanak a [küldetésekbe](/wiki/03-Mechanics/Quests.md#where-it-counts), amelyek nem neveznek meg szektort (például a Kihívások sorának nagy vadászatai), mégpedig abban a pillanatban, ahogy megtörténnek (egy hullám menetenként **egyszer** számít bele, ahogy egyszer fizet is), másra viszont nem számítanak: nem a kilövési statisztikákra, az eredmények számlálóira, a kill feedre és a drónjaid meg P.E.T.-jeid tapasztalatára sem. A tapasztalat és a becsület, amelyet fizetnek, viszont beleszámít a PvE-rangpontjaidba, ahogy egy teljesítés tapasztalata és becsülete is. Az idegenek zsákmánya a fizetéssel jön, közvetlenül a készletedbe.

<!-- solo-kills:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Idegen | Kredit | Thulium | XP | Becsület |
| :--- | ---: | ---: | ---: | ---: |
| **Seeker** | {{guide:spoils.pay.credits@Seeker#1}} | {{guide:spoils.pay.thulium@Seeker#1}} | {{guide:spoils.pay.experience@Seeker#1}} | {{guide:spoils.pay.honor@Seeker#1}} |
| **Phantasm** | {{guide:spoils.pay.credits@Phantasm#1}} | {{guide:spoils.pay.thulium@Phantasm#1}} | {{guide:spoils.pay.experience@Phantasm#1}} | {{guide:spoils.pay.honor@Phantasm#1}} |
| **Bulwark** | {{guide:spoils.pay.credits@Bulwark#1}} | {{guide:spoils.pay.thulium@Bulwark#1}} | {{guide:spoils.pay.experience@Bulwark#1}} | {{guide:spoils.pay.honor@Bulwark#1}} |
| **Goombah** | {{guide:spoils.pay.credits@Goombah#1}} | {{guide:spoils.pay.thulium@Goombah#1}} | {{guide:spoils.pay.experience@Goombah#1}} | {{guide:spoils.pay.honor@Goombah#1}} |
| **Crystalys** | {{guide:spoils.pay.credits@Crystalys#1}} | {{guide:spoils.pay.thulium@Crystalys#1}} | {{guide:spoils.pay.experience@Crystalys#1}} | {{guide:spoils.pay.honor@Crystalys#1}} |
| **Boss Seeker** | {{guide:spoils.pay.credits@Boss Seeker#1}} | {{guide:spoils.pay.thulium@Boss Seeker#1}} | {{guide:spoils.pay.experience@Boss Seeker#1}} | {{guide:spoils.pay.honor@Boss Seeker#1}} |
| **Seeker Slave** | {{guide:spoils.pay.credits@Seeker Slave#1}} | {{guide:spoils.pay.thulium@Seeker Slave#1}} | {{guide:spoils.pay.experience@Seeker Slave#1}} | {{guide:spoils.pay.honor@Seeker Slave#1}} |
| **Boss Phantasm** | {{guide:spoils.pay.credits@Boss Phantasm#1}} | {{guide:spoils.pay.thulium@Boss Phantasm#1}} | {{guide:spoils.pay.experience@Boss Phantasm#1}} | {{guide:spoils.pay.honor@Boss Phantasm#1}} |
| **Phantasm Guard** | {{guide:spoils.pay.credits@Phantasm Guard#1}} | {{guide:spoils.pay.thulium@Phantasm Guard#1}} | {{guide:spoils.pay.experience@Phantasm Guard#1}} | {{guide:spoils.pay.honor@Phantasm Guard#1}} |
| **Boss Goombah** | {{guide:spoils.pay.credits@Boss Goombah#1}} | {{guide:spoils.pay.thulium@Boss Goombah#1}} | {{guide:spoils.pay.experience@Boss Goombah#1}} | {{guide:spoils.pay.honor@Boss Goombah#1}} |
| **Goombah Guard** | {{guide:spoils.pay.credits@Goombah Guard#1}} | {{guide:spoils.pay.thulium@Goombah Guard#1}} | {{guide:spoils.pay.experience@Goombah Guard#1}} | {{guide:spoils.pay.honor@Goombah Guard#1}} |
| **Boss Crystalys** | {{guide:spoils.pay.credits@Boss Crystalys#1}} | {{guide:spoils.pay.thulium@Boss Crystalys#1}} | {{guide:spoils.pay.experience@Boss Crystalys#1}} | {{guide:spoils.pay.honor@Boss Crystalys#1}} |
| **Crystalys Guard** | {{guide:spoils.pay.credits@Crystalys Guard#1}} | {{guide:spoils.pay.thulium@Crystalys Guard#1}} | {{guide:spoils.pay.experience@Crystalys Guard#1}} | {{guide:spoils.pay.honor@Crystalys Guard#1}} |
| **Evil Protos** | {{guide:spoils.pay.credits@Evil Protos}} | {{guide:spoils.pay.thulium@Evil Protos}} | {{guide:spoils.pay.experience@Evil Protos}} | {{guide:spoils.pay.honor@Evil Protos}} |
| **Evil Kitefin** | {{guide:spoils.pay.credits@Evil Kitefin}} | {{guide:spoils.pay.thulium@Evil Kitefin}} | {{guide:spoils.pay.experience@Evil Kitefin}} | {{guide:spoils.pay.honor@Evil Kitefin}} |
| **Evil Ostirion** | {{guide:spoils.pay.credits@Evil Ostirion}} | {{guide:spoils.pay.thulium@Evil Ostirion}} | {{guide:spoils.pay.experience@Evil Ostirion}} | {{guide:spoils.pay.honor@Evil Ostirion}} |
| **Evil Nomad** | {{guide:spoils.pay.credits@Evil Nomad}} | {{guide:spoils.pay.thulium@Evil Nomad}} | {{guide:spoils.pay.experience@Evil Nomad}} | {{guide:spoils.pay.honor@Evil Nomad}} |
| **Evil Paragon** | {{guide:spoils.pay.credits@Evil Paragon}} | {{guide:spoils.pay.thulium@Evil Paragon}} | {{guide:spoils.pay.experience@Evil Paragon}} | {{guide:spoils.pay.honor@Evil Paragon}} |
| **Evil Storm** | {{guide:spoils.pay.credits@Evil Storm}} | {{guide:spoils.pay.thulium@Evil Storm}} | {{guide:spoils.pay.experience@Evil Storm}} | {{guide:spoils.pay.honor@Evil Storm}} |
| **Evil Wraith** | {{guide:spoils.pay.credits@Evil Wraith}} | {{guide:spoils.pay.thulium@Evil Wraith}} | {{guide:spoils.pay.experience@Evil Wraith}} | {{guide:spoils.pay.honor@Evil Wraith}} |
| **Evil Ironclad** | {{guide:spoils.pay.credits@Evil Ironclad}} | {{guide:spoils.pay.thulium@Evil Ironclad}} | {{guide:spoils.pay.experience@Evil Ironclad}} | {{guide:spoils.pay.honor@Evil Ironclad}} |

| Kapu | Kredit | Thulium | XP | Becsület |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 514 000 | 2 099 | 55 296 | 1 018 |
| **Beta Breach** | 1 298 500 | 5 939 | 187 744 | 2 470 |
| **Gamma Foundry** | 3 064 500 | 13 693 | 541 944 | 4 696 |
| **Delta Siege** | 5 239 625 | 22 338 | 882 676 | 7 850 |
| **Omega Vault** | 7 088 125 | 29 196 | 1 196 828 | 10 022 |
| **Davidski's Nightmare** | 7 081 950 | 29 124 | 1 196 445 | 9 968 |

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
