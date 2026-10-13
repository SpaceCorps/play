<!-- wiki-i18n source: b15e3e40418c232b -->
<!-- wiki-i18n title: Receptkönyv -->
# Receptkönyv és buildek {#recipe-book-and-builds}

<!-- wiki-search: recipe; recipes; recipe book; bill; steps; chart; craft tree; what do i need; build; builds; loadout; preset; presets; import; export; json; my builds; share a build; recept; receptek; költség; lépések; ábra; gyártás; felszerelés; előbeállítás; importálás; exportálás; saját buildek; build megosztása -->

A **Receptkönyv** a játék bármelyik tárgyánál megválaszolja a „Mi kell ehhez?” kérdést: ábrán mutatja, miből készül, sorrendben a lépéseket, a teljes költséget, és azt, honnan származik minden nyersanyag. A **Buildek** ugyanezt egy egész hajóra teszik meg: importáld a hangárod felszerelését vagy egy barátod buildjét, indulj ki a 15 előbeállítás egyikéből vagy készíts sajátot, és nézd meg az értékeit és a teljes költségét lépésről lépésre. Mindkettő az állomás **Könyvtárában** van, a Wiki alatt.

A Receptkönyv nem vezet saját árlistát: a számait akkor számolja ki, amikor ránézel, azokból a receptekből, árakból, technológiákból és zsákmánytáblákból, amelyeket a Bolt, a [Gyártás](/wiki/06-Items/Overview.md#upgrading-modules) és a [Kutatás](/wiki/03-Mechanics/Research.md) is használ, így követi a játékot, ha egy ár vagy egy recept megváltozik. Ezért ez az oldal nem közöl sem árat, sem értéket: nyisd meg a tárgyat vagy a buildet.

## Megnyitás {#open-it}

Nyisd meg az állomás menüjét, és válaszd a **Könyvtár › Receptkönyv** vagy a **Könyvtár › Buildek** pontot. A Receptkönyv megjegyzi az utoljára megnézett tárgyat, a szűrőit és a nagyítását, de csak ezen a számítógépen; a buildjeid ebbe nem tartoznak bele ([A fiókodban mentve](#saved-on-your-account)). Ha a játék újabb annál a szervernél, amellyel beszél, az oldal ezt kiírja, és kevesebbet mutat: a Receptkönyv továbbra is kiszámol mindent, ami megvásárolható, legyártható vagy fejleszthető, de nem tudja megmondani, honnan adja a világ az adott tárgyat (csak annyit ír: „Szerzés”), a Buildek pedig megnevezi azokat a részeket, amelyekhez az újabb szerver kell: az előbeállításokat, a Saját buildeket és az értékeket.

## Tárgy keresése {#find-an-item}

A bal oldali nagy lista a játék minden tárgyát tartalmazza, típus szerint csoportosítva, egy típuson belül pedig a játék saját sorrendjében: a leggyengébb szint az első. Az EMP Charge, az egyetlen fogyóeszköz, szintén rajta van.

- **Keresés.** Kezdj el gépelni bárhol az oldalon, és a szöveg a keresőmezőbe kerül. A lista egyetlen listává válik, aszerint rendezve, mennyire illik hozzá a név (a teljes név, az eleje, egy szó eleje, bármelyik része, aztán a típus). A kis- és nagybetű, valamint az ékezet nem számít, és egy átnevezett tárgy régi neve is megtalálja a tárgyat. Az `Esc` törli a keresést.
- **Típus.** A lista feletti legördülő menü egyetlen típusra szűkíti a listát, és megmondja, hány tárgya van az egyes típusoknak. A mellette lévő kapcsoló az egyes típusokon belül A–Z szerint rendez.
- **Sorok.** Egy sor mutatja a tárgy képét, nevét, típusát és ritkaságát, egy kis jelet arról a módról, ahogy általában megszerezhető (a Gyártásban készül, a Boltban kapható, zsákmányolható vagy megtalálható, sajtolják, vagy a feketelyukban állítják elő), és egy pipát, ha megvan.
- **Billentyűk.** A nyilak, a Page Up, a Page Down, a Home és az End végigvisznek a listán, az `Enter` pedig az ábrára ugrik. Az `Alt+Left` és az `Alt+Right` visszalép és előrelép a megnyitott tárgyak között.

## Az ábra {#the-chart}

Kattints egy tárgyra, és a jobb oldal megmutatja. Fent látható a képe, a neve, a ritkasága és a típusa, valamint egy címke minden **módhoz**, ahogyan megszerezhető: **Gyártás** (a Gyártásban, idővel és költséggel), **Vásárlás** (a Boltban, az árával), **Sajtolás** (ércből, a Skylab kovácsműhelyében), **Zsákmány** (a világ adja: idegenek, sziklák, jutalmak) és **Előállítás** ([Dark Matter](/wiki/03-Mechanics/Dark-Matter.md), a feketelyukba lőtt N.I.K.E.-kből). A kitöltött címke az a mód, amelyet az ábra és a költség követ; kattints egy másik címkére, hogy ehelyett azt kövesse. Ha nem kutattad ki, ami a tárgy legyártásához kell, egy sor megmondja, melyik technológia kell hozzá és mennyi ideig tart, egy gombbal, amely megnyitja a Kutatást.

Az **Ábra** fát rajzol a tárgyból balról jobbra: balra a tárgy, tőle jobbra az, amiből készül, egészen a nyersanyagokig.

- Minden doboz megmutatja a tárgyat, hányat kell belőle szerezned, és egy jelet arról, hogyan szerezhető meg (annak a módnak a fenti címkéjén látható jel; vidd az egeret a doboz fölé a szavakért, így a szín soha nem az egyetlen jelzés). A lakat azt jelzi, hogy a technológiája még nincs kikutatva, a számmal ellátott zöld pipa pedig azt, hány van belőle nálad.
- Az ágakkal rendelkező dobozon van egy kis fogantyú, amely összecsukja őket; egy nagy fa mély ágai összecsukva indulnak. A **Mind kinyit**, a **Mind összezár**, az **Illesztés** és a nagyítógombok az ábra felett vannak.
- Kattints egy dobozra, hogy elolvasd a kártyáját az ábra alatt: a tárgyat, a megszerzési módokat (egy másik címkére kattintva azt a módot követed), mit kér a mód (egy gyártás köreit, idejét és költségét, vagy az árát a Boltban), hány van belőle nálad, és zárolt doboz esetén a szükséges technológiát. Egy dupla kattintás vagy az `Enter` megnyitja azt a tárgyat a Receptkönyvben. A nyilak dobozról dobozra lépnek, a szóköz (`Space`) összecsukja vagy kinyitja az ágat, a `0` pedig illeszti az ábrát. Görgess a mozgáshoz; a `Ctrl` és az egérgörgő nagyít.
- Egy tárgy, amelyet csak venni vagy találni lehet, egyetlen doboz, amely ezt írja: „Nincs mit gyártani: megvásárolható vagy megtalálható. Lásd: Források.”

Széles ablakban az ábra a bal oldalt foglalja el, a többi panel pedig egy oszlopban áll tőle jobbra; keskeny ablakban az **Ábra**, **Lépések**, **Költség**, **Források** és **Felhasználása** fülek egyszerre egy panelt mutatnak.

## Lépések és költség {#steps-and-the-bill}

A fejléc alatt három vezérlő dönti el, mi számít: **Mennyi** (hány példányt szeretnél), **Számítson a birtokomban lévőkkel** (bekapcsolva: amid már megvan, azt levonja) és **A felszereltek is számítsanak** (kikapcsolva: a hajón felszerelt darab nem számít, mert a fejlesztés elhasznál egy darabot, a felszerelt pedig elhagyná a helyét).

- A **Lépések** az ábra számozott listaként, olyan sorrendben, ahogyan el kell végezni, csoportokban: Kutatás, Szerzés, Vásárlás, Sajtolás és gyártás, valamint A készletedből. A kutatás áll az élen, mert a Gyártás semmit nem gyárt le, amíg a technológiája nincs kikutatva. Minden lépés megmondja, mit és hányat, mibe kerül és mennyi ideig tart, a Szerzés lépés pedig megmutathatja, hol szerezhető meg. A **Lépések másolása** szövegként másolja a listát.
- A **Költség** összesít mindent: a Credits- és Thulium-egyenleged összevetve azzal, amid van, minden nyersanyagot a **Kell**, **Megvan** és **Hiányzik** oszlopokkal, a kutatáshoz szükséges Dark Mattert, a gyártás és sajtolás idejét, a kutatás idejét (egyszerre egy technológia) és egy **Értéket**. Az Érték két megszerzési mód összehasonlítására szolgál, a Thuliumot és a megtalálandó dolgokat Creditsben számolva: nem ár. A **Költség másolása** táblázatként másolja a költséget, amelyet beilleszthetsz egy csevegésbe vagy jegyzetbe.

## Források és Felhasználása {#sources-and-used-in}

- A **Források** megmondja, honnan adja a világ a tárgyat és minden nyersanyagot, amelyre a tervnek szüksége van, fajta szerint: idegenek, aszteroidák és sziklák, rajok, a Dormant Swamp, klánőrzők, [Davidski](/wiki/03-Mechanics/Davidski.md), Skylab-expedíciók, az óriás kotrógép, Skylab-termelés, küldetések, Barátok meghívása és a kezdőcsomag. Egy sor megnevezi, ki adja és hol, az esélyt és hányat. A „Még itt” felsorolja az [Aukciót](/wiki/03-Mechanics/Auction.md), Davidski készletét és a többi pilótát. Az esély esély, nem óránkénti ütem: azt, hogy egy leszedés mennyi ideig tart, te döntöd el.
- A **Felhasználása** felsorolja azokat a tárgyakat, amelyek ebből készülnek. Kattints egyre a megnyitásához.

## Hozzáadás a buildhez {#add-to-build}

Az a tárgy, amely foglalatba kerül vagy amit magaddal viszel, kap egy **Hozzáadás a buildhez** gombot: hajók, hajótest-páncélzatok, lézerek, lézererősítők, pajzsok, cellák, hajtóművek, fúvókák, Adaptive Corek, extrák, drónok, formációk, lőszer, rakéták és az EMP Charge. A tárgyat abba a buildbe teszi, amelyet a **Buildekben** szerkesztesz, az első helyre, ahová befér (ha nincs ilyen, „Új build” néven új buildet hoz létre), és egy üzenet megmondja, hová került, vagy miért nem fért be („Először válassz egy hajót.”). Ha olyan buildhez adsz hajót, amelyben már van, a cseréhez még egyszer kattintanod kell. Az EMP Charge-ot viszik, nem szerelik fel: a build rakétái közé kerül.

## Buildek {#builds}

A **build** egy hajó felszerelése, tárgyneveken leírva, hogy minden szerveren ugyanazt jelentse: a hajó, a lézerek az erősítőikkel, a pajzsok, hajtóművek és Adaptive Corek a celláikkal és fúvókáikkal, az extrák, a képességfoglalatok darabjai, a hajótest-páncélzatok, a drónok azzal, amit visznek, egy formáció, valamint a magunkkal vitt lőszer és rakéták. Van még neve, megjegyzése, szakasza (Korai, Közép vagy Késői) és típusa.

A bal oldali lista az **Előbeállításokat** szakaszonként, a **Saját buildeket**, az **Új buildet** és az **Importálást** tartalmazza; keskeny ablakban fülekből álló sor. Válassz egy buildet, és látod a tábláját, az értékeit és a költségét.

### Importálás {#import}

Az **Importálás** egy lapot nyit három ajtóval:

- **Beillesztés**: illeszd be egy build szövegét, vagy nyomd meg a **Beillesztés a vágólapról** gombot.
- **Fájlból**: a build-fájlok a játék adatmappájának `exports` mappájában (`.spacecorps2027` a saját mappádban), abban a mappában, ahová a **Mentés fájlba** ír.
- **A hangáromból**: válassz egy hajót és egy konfigurációt, és a játék beolvassa, ami fel van szerelve: lézerek és erősítők, generátorok a celláikkal és fúvókáikkal, extrák, képességdarabok, hajótest-páncélzatok, drónok azzal, amit visznek, és az Extra Slots CPU szintje. Felkínálja a gyorssávod formációját, lőszerét és rakétáit is; pipáld be, amelyiket kéred.

Látod, mi érkezik, mielőtt bármi mentésre kerülne, és a játék pontosan megmondja, mit nem tudott importálni: egy tárgyat, amely nincs ebben a játékban, egy darabot, amely nem a helyére való, több darabot, mint ahány foglalata a hajónak van, egy újabb játékkal készült buildet. A **Változtatás nélkül importálva** azt jelenti, hogy minden bekerült. Utána **Mentés a saját buildek közé**, **Megnyitás a szerkesztőben**, vagy zárd be a lapot. A [kovácsolási](/wiki/06-Items/Forge.md) szintjeid, a kovácsolási bónuszok, a drónszintek, a boosterek, a P.E.T., a hajód kinézete és a [Hangár](/wiki/03-Mechanics/Hangar.md) másik konfigurációja nem része a buildnek (a másik konfigurációt importáld második buildként).

### A 15 előbeállítás {#the-15-presets}

Tizenöt build áll készen: a játék három szakasza, **Korai**, **Közép** és **Késői**, mindegyikben öt fajtával. A **Farmolás** a költségéhez képest a legtöbb leszedést hozza, a **Védelem** a legnagyobb pajzzsal és a leggyorsabb regenerációval bír, a **Támadás** a legtöbb sebzéssel és áthatolással, a **Szituatív** az álcázással, ugrásokkal és sebességgel válogat a harcok között, a **Tank** pedig együtt a legnagyobb hajótesttel és pajzzsal rendelkezik. Egy előbeállítás nem módosítható: a **Másolat szerkesztése** a saját vázlatodként nyitja meg, a **Hozzáadás a saját buildekhez** pedig úgy tartja meg, ahogy van. Minden sor néhány karakterben mutatja az Értékét, a receptekből számolva, miközben nézed; nyiss meg egy előbeállítást az értékeiért és a költségéért.

### Szerkesztés {#edit}

A build úgy van megrajzolva, mint egy hangár: lézerek, generátorok, extrák, képességek, páncélzatok és drónok, aztán az Extra Slots CPU szintje, egy formáció és a magunkkal vitt lőszer és rakéták. Kattints egy üres foglalatra, és egy lista csak azt mutatja, ami belefér, az árával vagy a megszerzés módjával; kattints egy darabra, hogy **Csere**, **Modul hozzáadása** vagy **Eltávolítás**. Egy drón lézert vagy pajzsmagot visz. Ha hajót váltasz, a még beférő darabok maradnak, a többi levettként szerepel a listán. Adj a buildnek nevet, szakaszt, típust és megjegyzést, aztán **Mentés**, **Mentés másolatként**, **Törlés** vagy **Bezárás** (a Bezárás előbb rákérdez, ha vannak nem mentett módosítások).

### Értékek {#stats}

A tábla alatt a hangár saját értékkártyája áll: életerő, sebzés, hatótáv, krit. esély, pajzsok és töltődésük, elnyelés, sebesség, pajzs- és sebességbónusz, áthatolás, valamint olyan hajónál, amelynek vannak páncélzatfoglalatai, a páncélzatok által hozzáadott életerő. A kártyán nincsenek sorok a képességeknek: a képességfoglalatok darabjai a táblán vannak. A szerver ugyanazzal a kóddal számolja ki a számokat, mint a hangárod, olyan buildre, amely egyetlen hajón sincs felszerelve. Két kapcsoló állítja be a **Kovácsolási szintet** és a **Drónok szintjét**, amelyből a számok kiindulnak. A formáció repülés közben hat, ezért szövegként szerepel, és nem számít bele a számokba, a boosterek és a saját kovácsolási szintjeid sem.

### Költség {#cost}

A költségnek négy blokkja van:

- **Összesen**: Credits, Thulium, Dark Matter, minden nyersanyag a Kell, Megvan és Hiányzik oszloppal, az idők és az Érték. A **Még kell** az, ami marad, miután levontad, amid van.
- **Hová megy a pénz**: minden darab, a legdrágább elöl.
- **Lépések**: kutatás, szerzés, vásárlás, sajtolás és gyártás, sorrendben, az egész buildre. Kattints egy Szerzés lépésre, hogy lásd, honnan adja a világ, vagy nyisd meg a tárgyat a Receptkönyvben.
- **Mielőtt elkezdesz**: ami nem darab, például az Extra Slots CPU szintjei, a páncélzatfoglalatok kutatása, a drónok, amelyeket még meg kell vásárolnod, és a Skylab-mag szintje, amelyet a Kovácsműhely igényel.

Három kapcsoló: **Amim van, levonom** (bekapcsolva), **A felszereltek is** (kikapcsolva) és **Lőszer és rakéták is** (kikapcsolva: újra és újra elhasználódnak, ezért nem a build árához tartoznak).

## A fiókodban mentve {#saved-on-your-account}

**A Saját buildek a fiókodban vannak mentve**, a szerveren és nem ezen a számítógépen, így bármelyik számítógépre követnek. Legfeljebb 50-et tarthatsz meg; a lista megmutatja, mennyi van, és ha megtelt, az oldal arra kér, hogy törölj egyet egy újabb mentéséhez. Egy build akkor van elmentve, ha a szerver ezt mondja: az oldal addig **Mentés...** feliratot mutat, és ha a szerver elutasítja vagy nem érhető el, megmondja, miért, a build pedig mentetlen marad, a módosításaid pedig továbbra is a szerkesztőben vannak. Egy elmentett build csak tárgynevekből, néhány címkéből, valamint az általad beírt névből és megjegyzésből áll, és más pilóta nem látja. Ha egy barátodnak szeretnél adni egyet, exportáld.

## Megosztás és exportálás {#share-and-export}

Az **Exportálás** egy buildnél lapot nyit, rajta a build szövegként (JSON). **Másold** a vágólapra, hogy beilleszd egy csevegésbe, vagy válaszd a **Mentés fájlba** gombot, amely a `spacecorps-build-<name>.json` fájlt az `exports` mappába írja, és soha nem ír felül régebbi fájlt. Egy barát az **Importálás › Beillesztés** alatt illeszti be a szöveget, vagy a fájlt a saját `exports` mappájába teszi, és a **Fájlból** pont alatt választja ki. A szöveg a felszerelés tárgyneveit, a hajót, valamint a build nevét és megjegyzését tartalmazza, a fiókodból semmit.

## Tippek {#tips}

1. **Nézz utána, mielőtt farmolsz.** Nyiss meg egy tárgyat a Receptkönyvben, és olvasd el a Forrásait és a Lépéseit, mielőtt egy egész napot olyan zsákmányra töltesz, amely nem az, ami kell.
2. **Számolj a nulláról.** Kapcsold ki a **Számítson a birtokomban lévőkkel** kapcsolót (a Buildekben: **Amim van, levonom**), hogy lásd, mibe kerül egy tárgy vagy egy build a semmiből; hagyd bekapcsolva, hogy lásd, mi kell még.
3. **Indulj egy előbeállításból.** **Másolat szerkesztése**, cserélj ki egy darabot, és az értékek meg a költség követik.
4. **Olvasd a fákat is.** A [Tárgyfák](/wiki/06-Items/Item-Trees.md) minden tárgyfajtát egymás mellett mutatnak, és a Receptkönyv bármelyiknek kiszámolja az árát.
