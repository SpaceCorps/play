<!-- wiki-i18n source: 2329e422c8d1d27c -->
<!-- wiki-i18n title: Harc -->
# Harci mechanika {#combat-mechanics}

Ez a szakasz részletezi, hogyan számolódik ki, hogyan érvényesül és hogyan javítódik a sebzés a SpaceCorps összecsapásaiban.

![The death screen: respawn at the nearest portal or on the spot, each with its lock](../../img/wiki-img/shots/death.jpg)
![The flight screen in a fight: ship and pilot windows, the target, the hotbar, the chat, the log and the minimap](../../img/wiki-img/shots/hud-fight.jpg)
![The Target window: the alien, its distance, hull and shield](../../img/wiki-img/shots/hud-target.jpg)

## Sebzésszámítás {#damage-calculation}

Amikor egy hajó tüzel a lézereivel, a szerver a következő sorrendben számítja ki a leadott sebzést:

### 1. Alapsebzés és véletlen szórás {#1-base-damage-random-variance}

Az összes felszerelt lézer (a drónokon lévőket is beleértve) és a beleszerelt lézererősítők alapsebzése összeadódik.
- **Véletlen dobás**: a sortűz tényleges sebzése az összes alapsebzés **80%-a** és **100%-a** között véletlenszerűen alakul.
  - Képlet: `Roll = (0.8 + (Random * 0.2)) * BaseDamage`

### 2. Kritikus találatok {#2-critical-hits}

Minden sortűz kritikus találat is lehet.
- **Kritikus esély**: a felszerelt lézerek kritikus esélyének átlaga, plusz az összes felszerelt lézererősítő kritikus esélyének összege.
- **Kritikus szorzó**: ha egy lövés kritikus, a sebzésdobás **1,5-szeresére** nő. A kritikus sortűz sebzésszáma jégkékben, nagyobb méretben, „!” jellel jelenik meg.
- A Quantum Laser 1 és 2 lézernek nincs saját kritikus esélye: azt az erősítőik adják.
- **Fix kritikus sebzés**: a lézererősítők bármilyen fix kritikus sebzése a szorzó után adódik hozzá.
  - Képlet: `CritDamage = (Roll * 1.5) + FixedCritDamage`

### 3. Globális szorzók {#3-global-multipliers}

Végül a globális szorzók (például az aktív boosterek vagy a lézerlőszer szorzói, mint az x2, x3, x4) érvényesülnek, hogy kijöjjön a végső sebzés:
- Képlet: `FinalDamage = Damage * AmmoMultiplier * (1.0 + BoosterDamagePercent)`
- A viselt [drónformáció](/wiki/03-Mechanics/Formations.md) még egyszer szorozhatja az eredményt: például az Auger +21% lézersebzéssel, a Gyre −11%-kal, idegenek ellen a Culler +12%-kal (külön tényező, nem része a booster-százaléknak).
- A **Siphon Battery** lőszer szorzója x1, de a célpontja más: a sebzése kizárólag a célpont pajzsából jön (sosem a hajótestből, bármekkora is az elnyelés), és a saját pajzsodba kerül, a maximumodig. Lásd: [Lézerek és lőszer](/wiki/06-Items/Lasers.md).

### 3b. Rakéták {#3b-rockets}

Egy [rakéta](/wiki/06-Items/Rockets.md) saját sebzéssel rendelkezik (egy Lancet I 1 600–2 000, egy Lancet III 4 800–6 000, egy N.U.K.E. 45 000–50 000), amelyet kilövéskor egyszer sorsol a rendszer, és amely minden hajónál ugyanannyi: a lézereid, az erősítőid, a boosterek és a lőszer nem változtatják meg, és nincs kritikus találata. Az összes rakéta egyetlen **5 másodperces** időzítőn osztozik. Az egycélpontos rakétának **pajzsáthatolása** van: ez levonódik a célpontod elnyeléséből (lásd lent: Sebzés és biztonságos zónák); a robbanás a sugarán belül minden hajót megsebez, a széle felé kevésbé. Semmi sem korlátozza, mennyit vesz el egy rakéta egy pilóta hajójától: előbb a pajzsot, aztán a hajótestet. A rakéták sosem sebzik a saját vállalatodat vagy a saját [csoportodat](/wiki/03-Mechanics/Groups.md), akkor sem, ha a csoport tagjai különböző vállalatokból valók. A viselt [drónformáció](/wiki/03-Mechanics/Formations.md) az egyetlen, ami mindkettőt megváltoztatja: egy rakétaformáció növeli minden rakéta sebzését (legfeljebb +55%), néhány pedig hosszabbá vagy rövidebbé teszi az időzítőt.

### 4. Szembefordulás a célponttal {#4-facing-the-target}

Az a hajó vagy idegen, amely célba vett valakit és tüzel, a célpontja felé fordul, bárhogy repül is (körözve, hátrálva vagy egy helyben állva), és visszafordul az útirányába, amikor abbahagyja a tüzelést.

### 5. Hatótáv {#5-range}

Egy hajó másodpercenként egy sortüzet ad le, amíg a célpontja a **hatótávján** belül van, és visszatartja a tüzet, amíg a célpont távolabb van: ilyenkor a tűz nem fogyaszt lőszert, amíg a célpont újra elég közel nem kerül, és a célpontablak azt írja: „Hatótávon kívül”. A hatótáv **az összes lézered hatótávjának átlaga** (a drónjaidban lévő lézereket is beleértve), a legközelebbi egységre kerekítve, és egyetlen szám az egész hajóra: azon belül minden lézer tüzel, azon kívül egyik sem. Egy nagy hatótávú lézer a rövidebbek mellett ezért nem növeli meg a hatótávodat: egy Starfire-3 (850) és két Quantum Laser 2 (700) együtt 750-et ad. A Kovácsműhely hatótávbuffja a saját lézerén számít, az átlagolás előtt. A lézer nélküli hajó nem tud a lézereivel tüzelni, és a hangár nem mutat hozzá hatótávot (gondolatjel áll helyette): a rakétái továbbra is tüzelnek, mindegyik a saját hatótávjával (lásd: [Rakéták](/wiki/06-Items/Rockets.md)). Az egyes lézerek saját hatótávját lásd: [Lézerek és lőszer](/wiki/06-Items/Lasers.md).

---

## Kilövési jutalmak: az első találat foglal {#kill-rewards-first-hit-claims}

Az idegen jutalmai ahhoz a pilótához kerülnek, aki először lőtt rá, nem ahhoz, aki a végső találatot viszi be.

- **Foglalás**: az a pilóta foglalja le az idegent, akinek a lövése először sebzi meg. Minden találatod megújítja a foglalásodat.
- **Elvesztése**: ha **10 másodpercig** nem találod el az idegent, a foglalásod lejár, és a következő pilóta, aki eltalálja, lefoglalja. A foglalásod akkor is véget ér, ha a hajód megsemmisül, vagy elhagyod a térképet (portálon át vagy kijelentkezéssel), és ha a 10 másodpercen belül visszatérsz, az sem hozza vissza.
- **A kilövés**: amikor az idegen megsemmisül, a foglalását tartó pilóta kap mindent: kreditet, Thuliumot, XP-t, becsületet, a kilövést a küldetésekhez és a wipe-pontokhoz, valamint a [rakományládát](/wiki/03-Mechanics/Cargo.md). Az a pilóta, aki egy olyan idegent lő ki, amelyet más foglalt le, semmit sem kap, és a Játéknapló ezt jelzi. Ha a te foglalásod fizet, és a végső találatot egy másik pilóta viszi be, a Játéknapló megnevezi azt a pilótát, és azt írja, hogy a foglalásod után te kapod a jutalmat.
- **Rangpontok**: a kilövés PvE-pontokat is hozzáad a foglalást tartó pilóta rangsorához, annál többet, minél keményebb az idegen: 1-et egy Seeker, 2-t egy Phantasm, 4-et egy Bulwark, 7-et egy Goombah és 16-ot egy Crystalys után (minden idegen cikke megadja a sajátját). Ezek egyedül a pilótáé: a csoport jutalomrészesedése nem tartalmazza őket.
- **Hogyan látod**: ha kijelölsz egy olyan idegent, amelyet másik pilóta foglalt le, a Célpontablak azt mutatja: *Lefoglalta:* az a pilóta, és *Nincs jutalom*.
- A [vállalati pilóták](/wiki/03-Mechanics/Company-Pilots.md) sosem foglalnak le idegent, és az általuk kilőtt idegen is a foglalását tartó pilótát fizeti.
- A [csoportban](/wiki/03-Mechanics/Groups.md) lévő pilóta megosztja azt, amit a foglalása fizet, azokkal a csoporttársaival, akik közel vannak és lőnek; maga a foglalás egyedül a pilótáé.
- **A [rajok](/wiki/05-Swarms/Swarms.md) vezérei, a Dormant Pulse-ok és a [Clan Wardenek](/wiki/03-Mechanics/Clans.md#warden-pay-and-loot) kivételek**: egy rajboss, minden Dormant Pulse és minden Clan Warden annak a sebzésnek megfelelően fizet, amelyet minden pilóta okozott nekik, nem az első találat szerint, a rakományládájuk pedig ahhoz a pilótához kerül, aki a legtöbb sebzést okozta ([hogyan fizet egy boss megölése](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). A többi kísérő, a Pirate Scoutok és a Seeker Slave-ek, a foglalás szerint fizetnek, mint bármelyik idegen. A rajhajók PvE-pontjai a Rajok oldalon vannak.

---

## Idegenek, amelyek csak visszatámadnak {#aliens-that-only-fight-back}

A Seeker és a Goombah sosem kezd harcot. Mindegyik egy olyan pilótára fordul, aki eltalálja (sebzést okozó találat; egy másik idegen tüze sosem provokálja), azzal harcol, akit a [Kivel harcol egy idegen](#who-an-alien-fights) szakasz leír, és **10 másodperccel** azután engedi el a pilótát, hogy bárki utoljára eltalálta. Ha **30 másodpercig** békén hagyják, a hajótestét másodpercenként a maximumának 2%-ával javítja. A többi idegen (Phantasm, Bulwark, Crystalys) bármelyik védtelen pilótára rátámad, aki az aggrósugarukon belülre kerül (700, 700 és 900 egység), és a hajótestüket sosem javítják; minden idegen pajzsa az utolsó találat után 15 másodperccel kezd töltődni.

---

## Kivel harcol egy idegen {#who-an-alien-fights}

Egy idegen **az első pilótával, aki rálőtt**, harcol tovább, mindaddig, amíg még üldözni tudja azt a pilótát: a pilóta a térképen van, nincs biztonságos zónában, nincs álcázva és nincs a saját EMP-ablakában, életben van, és az elmúlt **10 másodpercben** eltalálta az idegent (minden találat újraindítja a 10 másodpercet: egy lézersortűz, egy rakéta vagy egy robbanás széle egyaránt). Amíg ez fennáll, más pilóták lövései sosem fordítják el, akármilyen közel vannak, és akárhányszor találják el, így egy pilóta lekötheti az idegent, miközben mások lőnek rá.

Amikor az első pilóta kiesik (elhagyja a térképet, biztonságos zónába ér, álcázásba vagy a saját EMP-ablakába kerül, megsemmisül, vagy 10 másodpercig nem találja el az idegent), az idegen a **következő** pilótára fordul, aki beszállt a harcba, abban a sorrendben, ahogy elsőként rálőttek, nem arra, aki utoljára eltalálta. Az a pilóta, aki kiesett, majd újra rálő, a sor végére áll be. Az idegen az első **32** pilótát tartja számon, aki rálőtt; a 33. lövő addig nem vesz részt a sorban, amíg valamelyikük ki nem esik, és akármekkora tömegben az idegen az elsőnél marad.

A [vállalati pilóták](/wiki/03-Mechanics/Company-Pilots.md) minden játékos után következnek: az idegen csak addig harcol vállalati pilótával, amíg egyetlen olyan játékos sem lőtt rá, akit még üldözni tud; az a játékos, aki egy olyan idegenre lő, amellyel egy vállalati pilóta harcol, átveszi azt, és egy vállalati pilóta sosem húz el egy idegent egy játékostól. Mindez nem változtatja meg, ki kapja az idegen jutalmait: az a foglalásé ([Kilövési jutalmak](#kill-rewards-first-hit-claims)).

---

## Az idegenek elvesztik az érdeklődésüket {#aliens-lose-interest}

Egyetlen idegen sem követ téged keresztül az egész térképen. De az az idegen, amelyet **találsz**, nem veszíti el az érdeklődését, hanem harcol veled: az utolsó találatod után **10 másodpercig** (minden találat újraindítja a 10 másodpercet, egy lézersortűz, egy rakéta vagy egy robbanás széle egyaránt) a saját sebességével rád repül, valahányszor a támadási hatótávján kívül vagy (Seeker 600, Phantasm és Bulwark 700, Goombah 800, Crystalys 900), és addig közeledik és tüzel, amíg hatótávon belülre nem kerülsz. Nincs korlátja annak, mekkora távolságra követ, amíg te találod. Az a lézer, amely az idegen fegyverénél messzebbre hat (a Starfire-3 hatótávja 850 egység, a Helios Beam hatótávja 900), nem teszi lehetővé, hogy olyan helyről találd el, ahonnan az nem tud válaszolni, és egy gyorsabb hajó is csak addig tartja maga mögött, amíg lősz rá. Azonnal elenged viszont, ha biztonságos zónába érsz, álcázod magad, vagy elhagyod a térképet.

Ha több pilóta találja el ugyanazt az idegent, az az elsőnél marad, aki rálőtt (lásd [Kivel harcol egy idegen](#who-an-alien-fights)): afelé a pilóta felé közeledik, és tüzel rá, így egy csoport, amely épp a hatótávján kívül áll körülötte, nem tudja egyikről a másikra futtatni anélkül, hogy az idegen valaha is válaszolna.

Az az idegen, amely téged választott célpontjának (egy Phantasm, Bulwark vagy Crystalys, amelynek a közelébe kerültél, vagy bármelyik idegen, amelyre rálőttél), és amelyet 10 másodperce nem találtál el, elenged, amint az alábbiak egyike igaz:

- **Sosem lőttél rá:** több mint **1 200 egységre** vagy tőle, vagy **2 000 egységet** repült onnan, ahol az üldözés kezdődött.
- **Az elmúlt percben rálőttél:** több mint **2 500 egységre** vagy tőle, vagy **3 000 egységet** repült onnan, ahol az üldözés kezdődött. Az általad indított harc tisztességes marad.

Az az idegen, amely elenged, onnan kóborol tovább, ahol áll, sosem oda, ahol utoljára látott (még akkor sem, ha álcázod magad, vagy EMP-t sütsz el), és **8 másodpercig** nem választ újra célpontnak, hacsak rá nem lősz. Minden idegen magától dönt, így egy vegyes falka megritkul, ahogy távolodsz. Az idegenek sosem követnek be egy biztonságos zónába vagy egy kapun át, és azok, amelyek egy ilyen közelében elvesztettek téged, mindegyik a maga irányába elmegy onnan, hogy ne várjanak egy csomóban. Egy idegen érdeklődése sosem ér kevesebb távolságra, mint a támadási hatótávja és az aggrósugara, plusz 100 egység.

Az idegenek nem tolják szét egymást: az egy pilóta nyomában lévő falka úgy közeledik, hogy nem hagy helyet a hajói között, a pilótáját elvesztett falka pedig csak úgy bomlik fel, hogy minden idegen a maga útját választja. Hajótól viszont az idegen távol marad: sosem kerül egy pilóta hajótestének belsejébe, és ha egy pilóta rááll egyre, azt maga előtt tolja.

A gyorsabb repülés csak egy pontig segít: a Protos (160) nem gyorsabb egyetlen vadászó idegennél sem (Phantasm 160, Bulwark 175, Crystalys 230), így az üldözésnek a póráz vet véget, nem a sebességed.

---

## Sebzés és biztonságos zónák {#taking-damage-safe-zones}

Amikor a hajódat egy ellenség vagy NPC eltalálja, a sebzés a következőképpen dolgozódik fel:

### 1. Pajzselnyelés {#1-shield-absorption}

A beérkező sebzés a pajzsok és az életerő között oszlik meg a hajód **átlagos elnyelése** szerint: a pajzsaid elnyelésének átlaga, mindegyik a pajzscelláival együtt, plusz a Szezonbolt Shield Absorbance Boost buffja (lásd [Pajzsmechanika](/wiki/03-Mechanics/Shields.md)). **Nincs 100%-ra korlátozva**: az, amit a pajzsok egy találatból felfognak, az elnyelésed **mínusz a támadó pajzsáthatolása**, 0% és 100% között.
- Minden találatnak az **elnyelés** (pl. 80% a legjobb pajzsnál a legjobb cellákkal, 56% egy Basic Shield Core-nál két Absorption Shield Cell I-gyel) szerinti részét a pajzsok fogják fel, levonva a találat áthatolását: egy Lancet III 35%-a 45%-ot hagy a pajzsokon egy 80%-os hajónál, a többi (itt 55%) pedig közvetlenül az életerőt éri.
- A **pajzsáthatolás** az egycélpontos rakétákból (10–35%) és az x3 és x4 lézerlőszerből (5% és 10%) származik; az idegeneknek nincs. Egy 100% fölötti hajó (mondjuk 112%) a különbségig (itt 12%) terjedő áthatolás ellen is egész találatot tart.
- Ha egy pajzs túl alacsony az arányához, a különbséget az életerőre engedi át; ha a pajzsok teljesen kiürültek, a maradék sebzés **100%-a** közvetlenül az életerőt éri.
- Az idegeneknek nincs elnyelési értékük: a pajzsuk minden találat 80%-át fogja fel (levonva a találat áthatolását), a hajótestük a többit.
- **Drónformációk.** A Rampart 17%-kal növeli az elnyelésedet (a Shrike 6%-kal csökkenti), az Asterism pedig a rád érkező minden közvetlen találatot 7% eséllyel hatástalanná tesz (egy lebegő „Mellé” felirat jelenik meg), a célba érő találatokon pedig a pajzs és a hajótest a szokásos módon osztozik. A Gemini (+9 pont) és a Stiletto (+16) átütést ad a saját lőszeredhez és a közvetlen rakétákhoz, összesen legfeljebb 40%-ig ([Drónformációk](/wiki/03-Mechanics/Formations.md)).

### 2. Sebezhetetlenség a biztonságos zónában {#2-safe-zone-immunity}

Minden vállalat otthoni bázisa (az X-1 térképek) biztonságos zónákat tartalmaz.
- Ha belépsz egy biztonságos zónába, a hajód teljesen sebezhetetlenné válik.
- **A védelem megszakadása**: ha megtámadsz egy ellenséget, azonnal megszűnik a biztonságos zóna adta sebezhetetlenséged, még akkor is, ha fizikailag egy zónán belül tartózkodsz.
- Minden állomás és portál körül egy gyűrű véd, ha eltelt 5 másodperc azóta, hogy találat ért, és 15 azóta, hogy tüzeltél. Amíg véd, és nem vagy harcban, a hangár ablak lehetővé teszi, hogy a játék elhagyása nélkül hajót válts: lásd [A hangár repülés közben](/wiki/03-Mechanics/Hangar.md).
- Állomások csak az otthoni bázisokon (`x-1`) vannak. A veszélyes szektorokban (`DS-1`–`DS-4`) nincs egy sem: ott a portálok körüli gyűrűk az egyetlen biztonságos zónák.

### 3. Támadás alatt egy veszélyes szektorban {#3-under-attack-in-a-danger-sector}

A portálon át történő ugrás 3 másodpercig tart (lásd [Utazás az űrtérképen](/wiki/01-General/Spacemap%20Travel.md)). A veszélyes szektorokban (`DS-1`–`DS-4`) az a pilóta, akinek a hajóját az elmúlt **10 másodpercben** egy másik pilóta vagy egy idegen eltalálta, nem indíthat ugrást, és egy találat megszakítja a folyamatban lévőt. Máshol a támadások sosem szakítják meg az ugrást, és semmi sem szakítja meg a [rakományláda](/wiki/03-Mechanics/Cargo.md) felvételét.

---

## Regeneráció és javítás {#recovery-repair}

A harc utáni felépüléshez a pilóták a passzív regenerációra és az aktív segédrobotokra támaszkodhatnak:

### 1. Passzív pajzsregeneráció {#1-shield-passive-regeneration}

- **Működés**: másodpercenként a pajzsod töltődési sebességének megfelelő pajzspontot állít vissza.
- **Késleltetés**: a harc megszakítja; a passzív regeneráció csak **15 másodpercnyi** sebzésmentesség után indul újra.
- **Drónformációk**: az Adamant és a Redoubt másodpercenként pajzsot ad vissza, harcban is (lásd: [Drónformációk](/wiki/03-Mechanics/Formations.md)).

### 1b. Siphon Battery

A [Siphon Battery](/wiki/06-Items/Lasers.md) lőszer a célpontból elszívott pajzsot azonnal hozzáadja a tiédhez, a maximumodig. A pajzsnyereség nem számít kapott sebzésnek, ezért nem késlelteti a passzív regenerációdat.

### 2. Javítódrónok (hajótest-javítás) {#2-repair-drones-hull-repair-}

- **Működés**: ha felszerelsz egy Repair Drone-t (a hangár Extrák között), a gyorssávról kapcsolod be (húzd az Extrák menüjéből egy helyre), és javítja a hajótestedet (HP). Bármilyen találat kikapcsolja, és teli hajótestnél leáll. Ha fel van szerelve egy [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu), nem kell újra bekapcsolnod: a CPU magától kiküldi, amint letelt az alábbi késleltetés, hacsak kézzel le nem állítottad.
- **Javítási ütem**: másodpercenként a maximális életerőd egy százalékát állítja vissza (csak a legjobb felszerelt drón számít, nem adódnak össze):
  - **Repair Drone I**: 1,5% max. HP / mp
  - **Repair Drone II**: 2,25% max. HP / mp
  - **Repair Drone III**: 3,5% max. HP / mp
  - **Repair Drone IV**: 5% max. HP / mp
- **Késleltetés**: a javítódrónok csak **10 másodpercnyi** sebzésmentesség után kezdik foltozni a hajótestet.
- **Képességfoglalatban** a Repair Drone nem javít magától: egy **Emergency Repair** nevű gombot ad, amely tíz másodperc alatt gyógyítja a maximális életerőd egy részét, még tűz alatt is (lásd [Képességek](/wiki/03-Mechanics/Abilities.md)).

---

## Álcázás és az EMP {#cloaking-and-the-emp}

A lövéshez célzás kell. Két [extra](/wiki/06-Items/Extras.md) elveszi a tiédet:

- **Cloaking CPU**: amíg álcázva vagy (nincs időkorlát), más vállalatok pilótái, az idegenek és a vállalati pilóták nem látják a hajódat, és nem vehetnek célba; a minitérképen egy egyszerű piros pontot látnak ott, ahol vagy. Az első sortűzöd megszünteti az álcázást, és egy percig nem álcázhatsz újra, sem találat vagy lövés után 10 másodpercig.
- **EMP Charge**: 3 másodpercig senki sem vehet célba, és minden rád irányuló célzás azonnal megszakad. Megszüntet minden álcázást a használó pilótától 1 500 egységen belül, kivéve a pilóta saját csoportjáét. Nem rejt el, és nem sebezhetetlenség: azt állítja meg, ami célzást igényel.

A rakéta is lövésnek számít: megszünteti a saját álcázásodat, valaki más rakétájának területi robbanása pedig még így is megsebez egy álcázott hajót, és megszünteti az álcázását, mert a robbanáshoz nem kell célzás (lásd [Rakéták](/wiki/06-Items/Rockets.md)). Az EMP a célzáshoz kötött lézereket és az irányított rakétákat állítja meg, a robbanást nem.

Egyik sem változtat egy kilövési foglaláson: a foglalás annak a története, hogy ki találta el az idegent, nem célzás, és az álcázás elengedi a tiédet.
