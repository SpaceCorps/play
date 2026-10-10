<!-- wiki-i18n source: 27056100dc9d4562 -->
<!-- wiki-i18n title: Aukció -->
# Aukció {#auction}

Az aukció a pilóták piaca és egyben a játék saját óránkénti tételei, az állomás menüjének egyetlen oldalán. A Bolthoz hasonlóan ez is az állomás egyik oldala: dokkolva használod, nem repülés közben. Négy része van. A **Piac** azt mutatja, amit más pilóták árulnak. A **Tételek** a játék saját ajánlatai, óránként egy. A **Hirdetéseim** azt mutatja, amit te magad árulsz. Az **Előzmények** az eladásaidat, a vásárlásaidat és a megnyert tételeidet mutatja, és azt, hogyan alakult a kereskedésed.

<!-- market-glance:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- Az aukció használatához **5. szint** kell: hirdetéshez, vásárláshoz és licitáláshoz.
- A hirdetés ára csomagonként értendő, egész kreditben vagy egész Thuliumban (nem mindkettőben), és sosem lehet a tárgy legkisebb ára alatt. **Legmagasabb ár nincs.**
- A Thulium-ár legalább a kreditben megadott legkisebb ár osztva az árfolyammal (1 000 kredit Thuliumonként), felfelé kerekítve, és csak azoknál a tárgyaknál, amelyeknél a legkisebb ár legalább 1 Thulium. Az árfolyam csak ennyit csinál: **az 1 Thulium = 1 000 kredit a legkisebb ár szabálya, nem átváltási árfolyam.** Semmi nem cserélődik, értéket sem mutat a játék, és a kreditet meg a Thuliumot soha nem adja össze.
- 82 tárgy hirdethető meg, és 81 közülük Thuliumban is árazható.
- Egy hirdetés 24 / 72 / 168 órán át fut, ahogy te választod: a lehetőségek minden szinten ugyanazok.
- A **letét**: az ár 1%, a hirdetés minden 24 órájára, legalább 50 kredit vagy 1 Thulium. Hirdetéskor fizeted ki; soha nem jár vissza, akkor sem, ha visszavonod a hirdetést.
- 10. szinttől a letét 1,5%.
- Az **adó**: az ár 5%. Az eladó bevételéből vonják le, amikor a hirdetés elkel.
- A letét és az adó megsemmisül: senkihez nem jut.
- A szezon 28. napjától a wipe-ig nincs letét és nincs adó.
- A szezon 30. napjától az aukció zárva van az új szezon kezdetéig: semmit nem lehet meghirdetni, megvenni vagy licitálni. A hirdetéseidet továbbra is visszavonhatod.
- Minden pénznemnek külön korlátja van arra, mennyit adhatsz el és mennyit vehetsz 24 óra alatt (lásd lent a szinttáblázatot). A megnyert tételek nem számítanak.
- Két pilóta között, ha az egyik a másiktól vásárol, 24 óra alatt legfeljebb 8 000 000 kredit vagy 40 000 Thulium mehet át.

<!-- market-glance:end -->

## Eladható tárgyak {#marketable-items}

Csak olyan tárgyat adhatsz el, amelyet **megszereztél**. Minden, amit megszerzel, kis címkét kap a [Hangárban](/wiki/03-Mechanics/Inventory.md#marketable-items), **Eladható**: amit az űrben felveszel (idegenek, rajok, Wardenek és a feketelyuk zsákmánya: [Rakomány](/wiki/03-Mechanics/Cargo.md)), amit egy küldetés kifizet ([Küldetések](/wiki/03-Mechanics/Quests.md#rewards)), és minden, amit a Gyártás és a Kovácsműhely előállít. Amit a Boltban **megvettél**, egy tételben megnyertél, a Piacon megvettél, bónuszkóddal, meghívócsomaggal vagy a kezdőcsomaggal kaptál, vagy visszatérítésként kaptál vissza, az nem eladható, és soha nem adható el újra, így semmit nem vesznek csak azért, hogy továbbadják. A Skylab Kovácsműhelyének lemezei sem eladhatók; a Reinforced Plate-ek, amelyeket egy küldetés fizet ki, igen. A Skylab Lőszernyomtatójának és Rakétagyárának lőszerei és rakétái sem eladhatók.

A címke egységek száma, nem kapcsoló: egy lőszerköteg tartalmazhat vásároltat és megszerzettet, a kártya pedig azt írja: „Eladható (3 / 5)”. Ha a köteg egy részét felhasználod (lövés, gyártás), először a közönséges egységek fogynak, így az eladhatók tartanak a legtovább. Két darab összevonásakor a [Kovácsműhelyben](/wiki/06-Items/Forge.md#merge) a címke csak akkor marad meg, ha mindkét darabnak megvolt, és az előnézet ezt jelzi; egy meghiúsult kovácsműhelyi lépés a nyersanyagait közönséges egységként adja vissza.

A Hangár **Csak eladható** chipje csak azt mutatja, amit el tudsz adni, a címkézett tárgy szemetese melletti **kalapács** pedig megnyitja hozzá az Aukció eladólapját. A Gyártásban az a recept, amelynek eredménye eladható, ezt kiírja, és a hiányzó nyersanyagnál van egy hivatkozás, amely megnyitja az Aukciót a nevével a keresőmezőben.

Amikor az Aukció megérkezett (0.4.12), a már meglévő felszerelésedet, amelyet a Bolt nem árul, és az erőforrásaidat egyszer megcímkézték. Ezeket nem, mert a Bolt egykor árulta őket, vagy mert amid van, az vásárolt és megszerzett darabokat is vegyít: a Quantum Laser III, az Absorption Shield Cell II és III, az Engine II, az Adaptive Core II, az Impulse Thruster II és III, a két Reinforced Plate és minden pilóta legrégebbi Base CPU I-e (a kezdőcsomagé). Az újakat, amelyeket megszerzel vagy elkészítesz, megcímkézik.

## Mi adható el {#what-can-be-sold}

<!-- market-kinds:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Típus | Amit eladhatsz | Darab |
| :--- | :--- | ---: |
| **Lézerek** | Quantum Laser I, Quantum Laser II, Quantum Laser III, Starfire-III, Helios Beam | 5 |
| **Lézererősítők** | Damage Amp I, Crit Amp I, Penetration Amp I, Damage Amp II, Crit Amp II, Penetration Amp II, Damage Amp III, Crit Amp III, Penetration Amp III, Damage Amp IV, Crit Amp IV, Penetration Amp IV | 12 |
| **Pajzsok** | Light Shield Core, Basic Shield Core, Heavy Shield Core | 3 |
| **Hajtóművek** | Engine I, Engine II, Engine III | 3 |
| **Adaptive Core-ok** | Adaptive Core I, Adaptive Core II, Adaptive Core III | 3 |
| **Pajzscellák** | Absorption Shield Cell I, Capacity Shield Cell I, Absorption Shield Cell II, Capacity Shield Cell II, Absorption Shield Cell III, Capacity Shield Cell III, Absorption Shield Cell IV, Capacity Shield Cell IV | 8 |
| **Fúvókák** | Impulse Thruster I, Momentum Thruster I, Impulse Thruster II, Momentum Thruster II, Impulse Thruster III, Momentum Thruster III, Impulse Thruster IV, Momentum Thruster IV | 8 |
| **Lézerlőszer** | Standard Battery (100 darabos csomagokban), Siphon Battery (10 darabos csomagokban), Advanced Plasma (10 darabos csomagokban), Ultra Core (10 darabos csomagokban), Experimental Fusion Core | 5 |
| **Rakéták** | Ember I, Lancet I, Rivet I, Scatter I, Ember II, Lancet II, Rivet II, Scatter II, Ember III, Lancet III, Rivet III, Scatter III | 12 |
| **Extrák** | Repair Drone I, Repair Drone II, Repair Drone III, EMP Charge, Repair Drone IV, Cloaking CPU S, Base CPU I, Cloaking CPU M, Auto-Repair CPU, Cloaking CPU L, Base CPU II | 11 |
| **Hajótest-páncélzat** | Hull Plating II, Hull Plating III | 2 |
| **Erőforrások** | Cataclysite (100 darabos csomagokban), Ship Fragment (100 darabos csomagokban), Daraxium (100 darabos csomagokban), Nyxite (100 darabos csomagokban), Quorvium (10 darabos csomagokban), Reinforced Hull Plate (10 darabos csomagokban), Power Core, Velkonite Reinforced Plate, Dark Matter, Orvium Reinforced Plate | 10 |

<!-- market-kinds:end -->

Hajók, drónok, drónformációk, boosterek és előfizetések soha nem adhatók el, és az Ancient Control Unit, a Velkonite és Orvium érc, a Dark Matter Plate, a Jump CPU, az Extra Slots CPU-k, a N.U.K.E. és a N.I.K.E. sem. A Dark Matter Plate-ek egyáltalán nincsenek az Aukción, sem áruként, sem árként. Nem hirdethető meg az a tárgy, amely fel van szerelve, be van építve egy másik tárgyba, modulokat tartalmaz, vagy a [Tranzittárolóban](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) van, és a használt Cloaking CPU, EMP Charge vagy Base CPU sem. A lőszert és a rakétákat az állomásról adják el: előbb szállj le a hajóddal.

## Eladás {#selling}

Nyomd meg a **Tárgy eladása** gombot (vagy a kalapácsot a Hangárban), válaszd ki, amit megszereztél (egy kategóriaválasztó szűkíti a listát, ugyanazokkal a kategóriákkal, mint a Piacon), döntsd el, kreditben vagy Thuliumban kéred, add meg egy csomag árát, és azt, hogy meddig fusson a hirdetés: 1, 3 vagy 7 napig. A lap megmutatja a legkisebb árat, három chipet, amely beírja az árat (**Minimum**; **Gyors eladás**, eggyel a jelenleg legolcsóbb hirdetés alatt; és **Reális**, az utolsó eladás ára), valamint a letétet, az adót és azt, amit kapsz, még mielőtt meghirdetnéd. Az ár alatt a **Hasonló hirdetések** egy diagramon mutatja, milyen áron hirdetik most ugyanazt a tárgyat ugyanazzal a varázslattal, a választott pénznemben: az árad egy vonal rajta, a legkisebb ár, az utolsó eladás és a Bolt ára meg van jelölve, egy szöveges sor megmondja, hol állna az árad, és alatta látszik a három legolcsóbb hirdetés. Egy darab egy csomag; a lőszert és néhány erőforrást 10 vagy 100 darabos csomagokban árulják, és egész számú csomagot adsz el. Amit meghirdetsz, elhagyja a készletedet, és a szerver őrzi, amíg el nem kel, vissza nem vonod, vagy le nem jár; akkor visszajön, a címkéjével együtt. Bármikor visszavonhatod, a szezon utolsó napjaiban is. A hirdetés pillanatkép: az ár módosításához vond vissza a hirdetést, és hirdesd meg újra (a letétet újra ki kell fizetni).

Minden tárgynak van **legkisebb ára**, és **legmagasabb ár nincs**: kérj annyit, amennyit akarsz. A táblázat néhány tárgy legkisebb árát mutatja.

<!-- market-bands:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Tárgy | Csomagméret | Legkisebb ár, kredit | Legkisebb ár, Thulium |
| :--- | ---: | ---: | ---: |
| Quantum Laser II | 1 | 32 000 | 32 |
| Quantum Laser III | 1 | 210 000 | 210 |
| Helios Beam | 1 | 1 600 000 | 1 600 |
| Absorption Shield Cell IV | 1 | 1 100 000 | 1 100 |
| Heavy Shield Core | 1 | 870 000 | 870 |
| Impulse Thruster IV | 1 | 980 000 | 980 |
| EMP Charge | 1 | 40 000 | 40 |
| Cloaking CPU S | 1 | 400 000 | 400 |
| Ultra Core | 10 | 800 | 1 |
| Lancet I | 1 | 200 | 1 |
| Ship Fragment | 100 | 600 | 1 |
| Dark Matter | 1 | 33 000 | 33 |

<!-- market-bands:end -->

A Thulium-ár egyetlen szabályt követ: a kreditben megadott legkisebb ár osztva az árfolyammal, felfelé kerekítve. Az árfolyam nem olyan érték, amelyet a játék a Thuliumnak tulajdonít. Csak azt adja meg, hogyan számolják ki a legkisebb Thulium-árat, és emiatt egy Thulium-hirdetés olcsó lehet annak a pilótának, akinek van Thuliuma. A legtöbb eladó krediteket fog kérni. A Quorvium kivételével minden tárgy árazható Thuliumban, az olcsók is (lőszer, rakéták, a közönséges erőforrások): a legkisebb áruk ilyenkor 1 Thulium, a legkisebb lépés. Egyedül a Quorvium árazható kizárólag kreditben, mert 1 Thulium többet érne, mint egy csomagja.

A **nyitott hirdetéseid** (és az a hirdetés, amelyet egy admin felfüggesztett) helyeket foglalnak. Ahogy szintet lépsz, több helyed lesz, egy felső határig, és naponta többet adhatsz el és vehetsz. Az, hogy egy hirdetés meddig futhat, minden szinten ugyanannyi.

<!-- market-limits:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Szint | Nyitott hirdetések | Leghosszabb futamidő | Naponta, kredit | Naponta, Thulium | Letét 24 óránként |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 5 | 20 | 168 óra | 4 500 000 | 22 500 | 1% |
| 6 | 40 | 168 óra | 6 000 000 | 30 000 | 1% |
| 7 | 70 | 168 óra | 7 500 000 | 37 500 | 1% |
| 8 | 100 | 168 óra | 8 500 000 | 42 500 | 1% |
| 9 | 100 | 168 óra | 10 000 000 | 50 000 | 1% |
| 10 | 100 | 168 óra | 15 000 000 | 75 000 | 1,5% |
| 11 | 100 | 168 óra | 15 000 000 | 75 000 | 1,5% |
| 12 | 100 | 168 óra | 15 000 000 | 75 000 | 1,5% |
| 13 | 100 | 168 óra | 20 000 000 | 100 000 | 1,5% |
| 14 | 100 | 168 óra | 20 000 000 | 100 000 | 1,5% |
| 15 | 100 | 168 óra | 20 000 000 | 100 000 | 1,5% |
| 16 | 100 | 168 óra | 20 000 000 | 100 000 | 1,5% |
| 17 | 100 | 168 óra | 20 000 000 | 100 000 | 1,5% |
| 18 | 100 | 168 óra | 20 000 000 | 100 000 | 1,5% |
| 19 | 100 | 168 óra | 20 000 000 | 100 000 | 1,5% |
| 20. szinttől | 100 | 168 óra | 20 000 000 | 100 000 | 1,5% |

<!-- market-limits:end -->

## Díjak {#fees}

Egy hirdetésnek **letétje** van, amelyet hirdetéskor kell kifizetni, és soha nem jár vissza, egy eladásnak pedig **adója**, amelyet az eladó bevételéből vonnak le. Mindkettőt a hirdetés pénznemében fizetik, és **megsemmisülnek**: senkihez nem jutnak, így senki nem nyer azzal, hogy önmagával kereskedik. A szezon utolsó két napján nincs letét és nincs adó.

<!-- market-fees:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Hirdetés | Ár | Letét | Adó | Az eladó kapja |
| :--- | ---: | ---: | ---: | ---: |
| Quantum Laser III: 6. szint, 24 óra | 210 000 kredit | 2 100 kredit | 10 500 kredit | 199 500 kredit |
| Quantum Laser III: 10. szint, 72 óra | 210 Thulium | 10 Thulium | 10 Thulium | 200 Thulium |
| Helios Beam: 12. szint, 168 óra | 2 500 000 kredit | 262 500 kredit | 125 000 kredit | 2 375 000 kredit |
| Helios Beam: 12. szint, 168 óra, a szezon utolsó napjaiban | 2 500 000 kredit | 0 kredit | 0 kredit | 2 500 000 kredit |

<!-- market-fees:end -->

## Vásárlás {#buying}

A **Piac** azt mutatja, amit más pilóták árulnak. Szűkítsd a listát a **kategória-chipekkel** (minden tárgytípushoz egy, a bennük lévő hirdetések számával), keress név szerint, szűrj varázslat és pénznem szerint, és rendezz ár szerint, aszerint, mi ér véget leghamarabb, vagy aszerint, mi a legújabb. Válassz egy hirdetést, hogy lásd, mi az, ki árulja, meddig fut, és hogyan viszonyul az ára az utolsó eladáshoz, a jelenlegi legalacsonyabb árhoz és a Bolt árához. A köteget egész csomagokban veszed meg. Egy nagy vásárlás még egyszer megerősítést kér. Az eladó azonnal megkapja a pénzét, az adó levonásával; te nem fizetsz sem letétet, sem adót. Amit megveszel, az **nem eladható**: az oldal a **Vásárlás** gomb mellett azt írja: „Amit kapsz: nem eladható”, mert csak az adható el, amit megszerzel. A saját hirdetésedet nem veheted meg. Az a hirdetés, amely elkel, miközben nézed, azt írja: „Ez a hirdetés már nincs meg.”

## Korlátok {#limits}

Minden pénznemnek külön napi korlátja van arra, mennyit adhatsz el és mennyit vehetsz, az utolsó 24 órában számolva, és van korlát arra is, mennyi mehet át két pilóta között, hogy egy második fiók ne legyen gyors módja egy vagyon áthelyezésének. A kreditet és a Thuliumot soha nem adják össze: aki Thuliumért ad el, az a Thulium-korlátját használja, mást nem. Az eladási lap figyelmeztet, ha egy eladás átlépné a napi eladási korlátodat, és ha egy vásárlás átlépné a napi vásárlási korlátodat, a Piac szól, és nem engedi a **Vásárlás** gombot. A korlátok a szinttel nőnek, és a Premium egyiket sem változtatja meg. A megnyert tételek nem számítanak.

A hirdetésben lévő, a vezetett tételben lévő és a rakteredben lévő rakéták mind beleszámítanak abba a legnagyobb számba, amennyit egy rakétából vihetsz: egy hirdetéssel nem vihetsz többet, mint amennyit a Bolt köteg megenged.

## Hirdetéseim és Előzmények {#my-listings-and-history}

A **Hirdetéseim** megmutatja a helyeidet és minden hirdetést az állapotával (nyitott, eladott, visszavont, lejárt, visszaadott vagy felfüggesztett), egy **Visszavonás** gombbal, egy lezárthoz **Újra meghirdet** gombbal, és **Alákínálták** chippel, ha ugyanannak a tárgynak egy másik hirdetése kevesebbet kér. A lejárt hirdetés magától visszakerül a készletedbe. Az **Előzmények** az elmúlt 30 nap kereskedésével kezdődik: az eladásaid és a vásárlásaid, mennyit kerestél és költöttél, a kifizetett díjak és adók, a nettó eredményed, a legjobb eladásod, az átlagos eladásod és a legtöbbet forgalmazott tárgyad, valamint két vonaldiagram: a napi bevételed és az eredményed eddig (kreditben vagy Thuliumban, egyszerre eggyel). Alatta áll annak a listája, mit adtál el, vettél és nyertél, az adóval együtt. A játék az Aukció főkönyvét 90 napig őrzi.

Arról, hogy valami elkelt, értesítést kapsz: üzenetet, az Aukció hangját és az új egyenleget, az Aukció bejegyzésén pedig jelvényt, amíg az oldal zárva van. Egy eladássorozat egy üzenet. Az Aukciónak saját halk hangjai vannak, mindenre egy, amit ott teszel vagy ami ott veled történik (meghirdetés, lejárat, eladás, licit, túllicitálás, nyerés), és követik a kezelőfelület hangerejét.

## Az óránkénti tételek {#the-hourly-lots}

A Tételek a játék saját ajánlatai: lőszer, rakéták és EMP Charge-ok, óránként, licitre. Arra jók, hogy lőszert olcsóbban szerezz, mint a Bolt kéri, és nyelőként is szolgálnak: a nyertes licit megsemmisül. Csak az alábbi napi táblázat tételei nyílnak meg (soha nem x1 vagy x4 lőszer, soha nem Siphon Battery, soha nem különleges rakéta), a Bolt saját pénznemében. Bármelyik tételre licitálhatsz, bármit viszel is már: a megnyert tétel egészében a tiéd, még ha a Bolt által engedett köteg fölé is visz.

<!-- market-lots:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- Minden UTC-óra elején új tétel nyílik, és 4 órán át nyitva marad, így egyszerre 4 van nyitva.
- A kikiáltási ár az áru bolti árának 20%. Minden további licitnek legalább 5% értékkel meg kell haladnia a legmagasabb ajánlatot, és legalább 100 kredit vagy 1 Thulium többnek kell lennie.
- Az ajánlatod azonnal kifizetődik és zárolva marad. Ha valaki túllicitál, azonnal visszakapod.
- Ha egy tétel utolsó 2 perc idejében licitálsz, a tétel vége a licit után 2 perc múlva lesz, legfeljebb 5 alkalommal.
- Amit nyersz, repülésre való, nem kereskedésre: sosem eladható. A nyertes licit megsemmisül. Az a tétel, amelyre senki nem licitál, nem kel el, és senkinek nem kerül semmibe.
- A tétel mérete azokon a pilótákon múlik, akik legalább 5. szintűek, és az utolsó 3 napban megnézték az aukciót: ha egy sincs, a táblázatbeli méret 10%, 30 vagy több pilótánál a teljes méret, lépésekben: 500 (lőszer), 50 (rakéta) és 1 (EMP Charge).
- A szezon utolsó 6 órájában nem készül új tétel. A wipe lemondja a még nyitott tételeket, és minden licit visszamegy.

<!-- market-lots:end -->

<!-- market-day:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| UTC-óra | Tétel | Teljes méret | Fizetőeszköz | Kikiáltási ár teljes méretnél |
| :--- | :--- | ---: | :--- | ---: |
| 00:00 | Scatter III | 1 250 | Thulium | 1 250 Thulium |
| 01:00 | Advanced Plasma | 25 000 | Thulium | 2 500 Thulium |
| 02:00 | Lancet I | 12 500 | Kredit | 1 250 000 kredit |
| 03:00 | EMP Charge | 5 | Thulium | 500 Thulium |
| 04:00 | Ultra Core | 25 000 | Thulium | 5 000 Thulium |
| 05:00 | Rivet II | 5 000 | Kredit | 800 000 kredit |
| 06:00 | Advanced Plasma | 10 000 | Thulium | 1 000 Thulium |
| 07:00 | Advanced Plasma | 50 000 | Thulium | 5 000 Thulium |
| 08:00 | Ember I | 12 500 | Kredit | 1 250 000 kredit |
| 09:00 | Ultra Core | 50 000 | Thulium | 10 000 Thulium |
| 10:00 | Scatter II | 5 000 | Kredit | 800 000 kredit |
| 11:00 | EMP Charge | 5 | Thulium | 500 Thulium |
| 12:00 | Advanced Plasma | 50 000 | Thulium | 5 000 Thulium |
| 13:00 | Lancet III | 1 250 | Thulium | 1 250 Thulium |
| 14:00 | Ultra Core | 10 000 | Thulium | 2 000 Thulium |
| 15:00 | Advanced Plasma | 25 000 | Thulium | 2 500 Thulium |
| 16:00 | Ultra Core | 50 000 | Thulium | 10 000 Thulium |
| 17:00 | Rivet I | 12 500 | Kredit | 1 250 000 kredit |
| 18:00 | Advanced Plasma | 50 000 | Thulium | 5 000 Thulium |
| 19:00 | Ember II | 5 000 | Kredit | 800 000 kredit |
| 20:00 | Ultra Core | 25 000 | Thulium | 5 000 Thulium |
| 21:00 | Advanced Plasma | 25 000 | Thulium | 2 500 Thulium |
| 22:00 | Advanced Plasma | 10 000 | Thulium | 1 000 Thulium |
| 23:00 | EMP Charge | 5 | Thulium | 500 Thulium |

<!-- market-day:end -->

Ha kevés pilóta használja az Aukciót, a tételek kicsik, hogy egy maroknyi pilótának ne kínáljanak óránként több ezer lövést; ahogy többen nézik, úgy nőnek.

**Licit maximummal.** A licitablakban kapcsold be az *Automatikus licit egy maximumig* kapcsolót, és írd be, legfeljebb mennyit fizetnél. Az Aukció ekkor licitál helyetted: a tétel által elfogadott legalacsonyabb ajánlatot teszi, és valahányszor valaki túllicitál, újra licitál, mindig a legkisebb emeléssel a legmagasabb ajánlat fölé, a maximumodig és nem tovább. Az ajánlat, amellyel vezetsz, a következő legjobb maximumot éppen megverő legalacsonyabb ajánlat, nem a maximumod: 500 és 800 kredites maximumnál egy 100-ról induló tételen a magasabb 600-zal vezet, nem 800-zal. Ha két maximum egyenlő, az nyer, amelyiket előbb állították be. A teljes maximumod beállításkor lefoglalódik a pénztárcádból, ezért egy automatikus licit sem hiúsulhat meg pénz hiányában; a tétel végén csak a nyertes ajánlatot fizeted, a többi visszajön, és ha valaki túllépi a maximumodat, az egész azonnal visszajön, és értesítést kapsz. Egy tételen, amelyen vezetsz, a **Maximum** gomb bármikor emeli a maximumodat, vagy leviszi a jelenlegi ajánlatodig. A maximum beállítása nem licit, de a hosszabbítási szabály minden licitet számol, az Aukcióét is. A maximum beállításának saját halk hangja van, a hangeffektek hangerején.

## A szezon és a wipe {#the-season-and-the-wipe}

Az Aukció követi a szezont (lásd [Wipe-idővonal](/wiki/03-Mechanics/Wipe-Timeline.md)). Az utolsó két napon nincs díj. A 30. naptól, amikor a wipe ötperces visszaszámlálása elindul, zárva van: semmit nem hirdetnek meg, nem vesznek és nem licitálnak, az akkor véget érő tételt lemondják, és a licitet visszaadják, a saját hirdetéseidet pedig továbbra is visszavonhatod. A hirdetés soha nem fut tovább a szezon végénél.

A wipe-kor **minden nyitott hirdetés visszakerül az eladójához** laza tárgyként, a wipe pedig a laza tárgyakat ezután úgy törli, mint a többit (csak az marad meg, amit a [Tranzittárolóba](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) teszel): ezért add el, vagy vond vissza és tedd tárolóba, amit meg akarsz tartani. A még nyitott tételeket lemondják, és a liciteket visszatérítik. A kredit és a Thulium nem törlődik.

## Amit az Aukció nem ad meg {#what-the-auction-does-not-give-you}

Az Aukció arra való, hogy kereskedj azzal, amit megszerzel, és őszinte a korlátairól.

- **A zsákmány eladása nem grind.** A nyers idegenzsákmány csak erőforrás, és annak 0,4–0,9 százalékát éri, amit ugyanaz az 5. szintű vadászóra a lelövésekért kifizet. Amit a Piac egy új pilótának ad, az a felszerelés, amelyet a küldetései kifizetnek, és amelyre nincs szüksége (egyszer), a Kihívás-küldetések erőforrásai, a rajvezérek dobozai és amit maga gyárt.
- **Nincs kereskedő.** A vételi megbízások, amelyekben a pilóta megmondja, mit akar venni és mennyiért, nincsenek ebben a változatban. Addig az egyetlen kereskedő a kézműves, aki anyagot vesz, a Gyártásban felszerelést készít, és eladja, valamint a raktáros pilóta, aki a készletét a Tranzittárolóban tartja a wipe-on át.
- **A Bolt felszerelése nem továbbeladásra való.** A Boltban vásárolt felszerelés nem adható el újra: idetartozik a Quantum Laser I és II, a Light és a Basic Shield Core, az Engine I és II, a cellák és fúvókák első fokozata, a Bolt által árult amp-ok és a vásárolt lőszer. Egy pilóta egyetlen eladható Quantum Laser II-je az, amelyet egy küldetés egyszer kifizet.
- **A lemezek küldetésekből jönnek.** A Piacon lévő Velkonite és Orvium Reinforced Plate-ek azok, amelyeket a Kihívás-küldetések fizetnek ki. A Kovácsműhely lemezei kimaradnak, különben ők lennének a Piac legnagyobb árucikke.

Ha egy hirdetés furcsának tűnik, jelezd a szokásos módon: a játék adminisztrátorai felfüggeszthetnek egy hirdetést, visszaadhatják, szüneteltethetik az Aukciót vagy kitilthatnak belőle egy pilótát, és minden ilyen műveletet rögzítenek.
