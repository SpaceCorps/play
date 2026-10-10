<!-- wiki-i18n source: 42731fd43a13e953 -->
<!-- wiki-i18n title: Skylab -->
# Skylab

A Skylab a te személyes orbitális létesítményed. Modulokat épít és fejleszt, amelyek kreditet és Thuliumot termelnek, ércet bányásznak, olyan lemezeket kovácsolnak, amelyekből a Gyártás a legjobb lézereket készíti, és a Mag 10. szintjétől kikutatják azokat a technológiákat, amelyekre a Gyártásnak szüksége van. Akkor is dolgozik neked, amikor offline vagy.

A Mag 10. szintjén a Skylab tovább is nő: egy **híd** összeköti a Magot egy második Maggal, amelyen hat további modulfoglalat van, és három újabb modul csatlakozik hozzá: a **Lőszernyomtató** és a **Rakétagyár**, amelyek a semmiből állítanak elő lőszert és rakétát, valamint az **Ércrakodó**, amely a nálad lévő ércet az Erőforrás-raktárba rakja át (lásd: [A híd és a 2. Mag](#the-bridge-and-core-2) és [Ércrakodó](#ore-bay)).

> [!NOTE]
> **Mi változott a 0.4.10-ben.** A Skylab minden moduljának most saját táblázata van a termelésről, az árakról és az időkről, szintről szintre. A szintjeidet megtartottad: semmit nem vontunk le, és a különbözetet sem térítettük vissza. Amit a farmjaid és a gyűjtőid a frissítés érkezésekor a tárolóikban tartottak, azt **egyszer, a régi áron** fizettük ki: a kredit és a Thulium a számládra, az érc az Erőforrás-raktáradba került, a tárolók pedig üresen indultak újra.
>
> Két szabály új. **A Napelem fejlesztés közben csak az energiája 25%-át termeli**, ezért a legtöbb állomáson minden farm és gyűjtő leáll a fejlesztés végéig (lásd: [Napelem modul](#solar-module) és [A Napelem fejlesztésének időzítése](#timing-a-solar-upgrade)). **Az Erőforrás-raktárnak minden ércre külön korlátja van**: az 1. szinten a gyűjtő egynapi termelése, a 20. szinten négynapi.

> [!NOTE]
> **Mi változott a 0.4.15-ben.** A Mag 9. szintről a 10. szintre lépése mostantól **2 000 Thuliummal** többe kerül, és amikor elkészül, megjelenik egy **híd** és egy második Mag, a **2. Mag**, hat új modulfoglalattal. A Napelem átköltözik a 2. Magra. Két új modul csatlakozik hozzá: a **Lőszernyomtató** és a **Rakétagyár**. A Napelem a 7. szinttől több energiát is termel, hogy a teljes állomás továbbra is fedezve legyen. Semmi sem vész el abból, amit építettél: az a Mag, amely már a 10. szinten vagy afölött van, azonnal megkapja a hidat, és nem fizet semmit.

![The Skylab station fully grown](../../img/wiki-img/shots/skylab-station.jpg)
![The Resource Storage card of the Skylab](../../img/wiki-img/shots/skylab-storage.jpg)
![The Skylab table of modules: level, production, storage and power of every module, with the 0.4.10 numbers](../../img/wiki-img/shots/skylab-table.jpg)

## Egy percben {#in-one-minute}

- Először a **Napelemet** építsd meg: az energiája nélkül a Skylabban semmi sem működik. A Kreditfarm megépítése nem kerül semmibe, a Thuliumfarm 5 000 kreditbe és 500 Thuliumba kerül.
- A farmok és a gyűjtők egy **tárolót** töltenek (72 órányit), amíg távol vagy. A **Begyűjtés** a számládra viszi (kredit, Thulium) vagy az Erőforrás-raktáradba (érc).
- A **Thuliumfarm** a fő Thulium-forrásod: az 1. szinten óránként 40-et, a 20. szinten 1 280-at termel. A Kreditfarm az 1. szinten óránként 750 kreditet, a 20. szinten 75 000-et termel.
- A **Mag** adja az ütemet: egyetlen modul sem léphet fölé, és a saját fejlesztése nagyjából 16 és fél napig tart.
- A **Mag 10. szintjén** egy **híd** felépíti a **2. Magot** hat további modulfoglalattal, és a **Lőszernyomtató**, a **Rakétagyár** meg az **Ércrakodó** csatlakozik hozzá. A 10. szintre lépés 2 000 Thuliummal többe kerül.
- **A Napelem fejlesztés közben csak az energiája 25%-át termeli**, ezért a farmjaid és a gyűjtőid leállnak, amíg el nem készül. [Tervezd meg](#timing-a-solar-upgrade).

## Áttekintés {#overview}

A Skylab a saját órája szerint jár, a hajódtól függetlenül: a modulok termelnek és kovácsolnak, amíg távol vagy. Neked építened, fejlesztened, az energiát egyensúlyban tartanod és begyűjtened kell. Az oldal ugyanannak az állomásnak négy nézetét mutatja: **Állomás** (a 3D-s állomás, minden modul fölött egy címkével; kattints az egyikre az adatlapjának megnyitásához, vagy nyomd meg az **1**–**9** billentyűt), **Lista** (egy kártya minden modulhoz), **Táblázat** (minden modul értékei egy táblázatban) és **Kutatás** (a Kutatóközpont saját képernyője, lásd: [Kutatás](/wiki/03-Mechanics/Research.md)). Ha az egeret az **Építés** vagy a **Fejlesztés** gomb fölé viszed, megmutatja, mit változtat a következő szint, mennyibe kerül, és mennyi ideig tart.

Tizenkét modul alkotja az állomást:

| Modul | Mit termel vagy mit tesz | Építhető |
| :--- | :--- | :--- |
| **Mag** | Ez szabja meg az összes többi modul legmagasabb szintjét | Mindig megvan |
| **Napelem** | Energiát termel | A Mag bármely szintjétől |
| **Kreditfarm** | [Kreditet](/wiki/01-General/Getting-Started.md) termel | A Mag bármely szintjétől |
| **Thuliumfarm** | [Thuliumot](/wiki/01-General/Getting-Started.md) termel | A Mag bármely szintjétől |
| **Velkonite-gyűjtő** | Velkonite-ércet bányászik | A Mag 5. szintjétől |
| **Orvium-gyűjtő** | Orvium-ércet bányászik | A Mag 5. szintjétől |
| **Erőforrás-raktár** | Tárolja az ércet | A Mag 5. szintjétől |
| **Kovácsműhely** | Lemezekké kovácsolja az ércet | A Mag 5. szintjétől |
| **Kutatóközpont** | A nyersanyagokat tudománnyá alakítja, és [technológiákat](/wiki/03-Mechanics/Research.md) kutat | A Mag 10. szintjétől |
| **Lőszernyomtató** | A semmiből nyomtat x2, x3 vagy x4 lőszert | A Mag 10. szintjétől, a 2. Magon |
| **Rakétagyár** | A semmiből gyártja a Bolt rakétáit | A Mag 10. szintjétől, a 2. Magon |
| **Ércrakodó** | A nálad lévő Velkonite-ot és Orviumot az Erőforrás-raktárba rakja át | A Mag 10. szintjétől, a 2. Magon |

A **híd** és a **2. Mag** nem modulok: akkor jelennek meg, amikor a Mag eléri a 10. szintet, és a 2. Magnak nincs saját szintje (lásd: [A híd és a 2. Mag](#the-bridge-and-core-2)).

**Küldetések a Skylabhoz.** Tíz [állomásküldetés](/wiki/03-Mechanics/Quests.md#station-missions) a Küldetésirányításban végigvezet a Skylabon: építs Napelemet, Kreditfarmot és Thuliumfarmot, fejleszd a Magot és a Napelemet, gyűjtsd be az első 50 000 kreditedet, nyisd meg az ellátási láncot, és minden lépésért fizetnek is egy keveset. Az első az 1. szinttől nyitva van.

## Az állomás minden szinten {#the-station-at-every-level}

Ezek a Skylab Állomás nézetének képei az 1-től 20-ig terjedő szintek mindegyikén, mind ugyanabból a szögből, minden modullal ugyanazon a szinten. A nézet az egész állomást belefoglalja a képbe, ezért a méretarány nem azonos mindegyiken: ugrik, amikor az alak nő. Az állomás lépcsőkben nő: az alakja az **1., 5., 10., 15. és 20. szinten** változik, köztük pedig minden szint **eggyel több lámpát** gyújt meg minden modul gallérján (a meggyújtott lámpák száma a szint, és a Mag húszlámpás gyűrűje is így telik meg).

A 10. szinttől látható képek az állomást úgy mutatják, ahogy a híd előtt kinézett: a 0.4.15 óta a Mag 10. szintre lépése a hidat és a 2. Magot is megépíti, és a Napelem a 2. Magon áll (lásd: [A híd és a 2. Mag](#the-bridge-and-core-2)).

**1–4. szint.** Az első négy modul a Mag körül: a Napelem, a Kreditfarm, a Thuliumfarm és a dokkoló, amely a hajódat tartja. Az ellátási lánc még nem építhető meg.

![1. szint](../../img/skylab/wiki/level-01.jpg)
![2. szint](../../img/skylab/wiki/level-02.jpg)
![3. szint](../../img/skylab/wiki/level-03.jpg)
![4. szint](../../img/skylab/wiki/level-04.jpg)

**5–9. szint.** A Mag 5. szintjétől az ellátási lánc megépíthető: a két gyűjtő az állomás feletti tartószerkezetein, az Erőforrás-raktár a Mag északkeleti portjánál, a Kovácsműhely pedig az északnyugati portjánál (itt megépítve láthatók).

![5. szint](../../img/skylab/wiki/level-05.jpg)
![6. szint](../../img/skylab/wiki/level-06.jpg)
![7. szint](../../img/skylab/wiki/level-07.jpg)
![8. szint](../../img/skylab/wiki/level-08.jpg)
![9. szint](../../img/skylab/wiki/level-09.jpg)

**10–14. szint.** A Mag felölti a gyűrűjét, a farmok és a gyűjtők nagyobb alakot öltenek, a Thuliumfarm pedig saját gyűrűt kap.

![10. szint](../../img/skylab/wiki/level-10.jpg)
![11. szint](../../img/skylab/wiki/level-11.jpg)
![12. szint](../../img/skylab/wiki/level-12.jpg)
![13. szint](../../img/skylab/wiki/level-13.jpg)
![14. szint](../../img/skylab/wiki/level-14.jpg)

**15–19. szint.** A farmok megtelnek ládákkal és kristályokkal, a dokkoló kivilágítja a bejáratát, a Napelem-mező pedig felső részt növeszt.

![15. szint](../../img/skylab/wiki/level-15.jpg)
![16. szint](../../img/skylab/wiki/level-16.jpg)
![17. szint](../../img/skylab/wiki/level-17.jpg)
![18. szint](../../img/skylab/wiki/level-18.jpg)
![19. szint](../../img/skylab/wiki/level-19.jpg)

**20. szint.** A létra teteje: a korona a Magon, a farmok és az ellátási lánc teljesen kinőtt tornyai.

![20. szint](../../img/skylab/wiki/level-20.jpg)

**A kilenc modul kártyái.** Ugyanennek az állomásnak a Lista nézete a 20. szinten: az első kiadás négy modulja, az ellátási lánccal érkezett Velkonite-gyűjtő, Orvium-gyűjtő, Erőforrás-raktár és Kovácsműhely, valamint a Kutatóközpont. Minden kártya mutatja a modul szintjét, a termelését, az energiáját és a kapcsolóját. Minden kártyán 20. szint áll, kivéve a Kutatóközpontét: annak 1–10. szintje van, ezért a kártyáján a 10. szint áll, a legmagasabb. A Lőszernyomtatónak és a Rakétagyárnak saját kártyája van ugyanebben a nézetben; őket [lentebb](#the-bridge-and-core-2) írjuk le.

![A Lista nézet a 20. szinten: a Mag, a Napelem, a Kreditfarm, a Thuliumfarm, a Velkonite-gyűjtő, az Orvium-gyűjtő, az Erőforrás-raktár, a Kovácsműhely és a Kutatóközpont kártyái](../../img/skylab/wiki/modules.jpg)

## Az első négy modul {#the-first-four-modules}

### Mag modul {#core-module}

A Skylabod szíve. A Mag szintje dönti el az összes többi modul legmagasabb szintjét: egyetlen modult sem fejleszthetsz magasabbra a Magnál. A Mag a 20. szintig fejleszthető, és az **5. szinttől** megnyitja az alábbi ellátási láncot. A fejlesztései kreditbe kerülnek, a **10. szintre** lépés pedig **2 000 Thuliummal** többe kerül, és felépíti a hidat és a 2. Magot (lásd: [A híd és a 2. Mag](#the-bridge-and-core-2)). Összesen 112 326 kredit a 10. szintig és 6 647 504 a 20. szintig, hozzá az a 2 000 Thulium, és nagyjából 16 és fél napig tart (lásd: [Fejlesztési idők](#upgrade-times)).

### Napelem modul {#solar-module}

Az energia a Skylab éltető ereje. A Napelem modul termeli azt az energiát, amelyet az összes többi modul használ.

- **Fontosság**: ha az energiafogyasztásod nagyobb a termelt energiánál, a farmjaid és a gyűjtőid leállnak.
- **Termelt energia**: egy N. szintű Napelem elég energiát termel **minden más modulnak az N. szinten**, és még nagyjából egy tizedet: 255-öt az 1. szinten, 965-öt a 7. szinten, 17 990-et a 20. szinten. A 7. szintű Napelem egy egész, 7. szintű állomást ellát (az összes szinthez lásd: Energiagazdálkodás).
- **Ár**: a Napelem megépítése **500 kreditbe és 50 Thuliumba** kerül. A fejlesztései ugyanannyiba kerülnek és ugyanannyi ideig tartanak, mint a Kovácsműhelyé: a 2. szintért 8 000 kredit és 25 Thulium (5 perc), a 20. szintért 9 000 000 kredit és 10 000 Thulium (24 óra).
- **Fejlesztés**: amíg a Napelemet fejlesztik, csak a jelenlegi szintje energiájának **25%-át** termeli, a fejlesztés végétől pedig az új szintét. Az az állomás, amely ennél többet használ, leáll: minden farm és gyűjtő abbahagyja a termelést, és a Kovácsműhely nem indít új adagot, amíg a fejlesztés el nem készül. Szinte minden állomás ilyen: csak akkor megy tovább a fejlesztés alatt, ha az összes többi modul legalább öt szinttel a Napelem alatt van (a Napelem 10. szintjétől hat szinttel). A Napelem fejlesztését úgy tervezd, mint a farmjaid áramkimaradását (lásd: Építés és fejlesztés).
- **Hely**: a Mag 10. szintjétől a Napelem a 2. Magon áll, az állomás túlsó végén (lásd: [A híd és a 2. Mag](#the-bridge-and-core-2)).

### Kreditfarm és Thuliumfarm {#credit-farm-and-thulium-farm}

- **Kreditfarm**: idővel kreditet termel: **az 1. szinten óránként 750-at, a 20. szinten 75 000-et** (5. szint: 3 750; 10. szint: 11 250; 15. szint: 25 500). Megépítése nem kerül semmibe.
- **Thuliumfarm**: idővel Thuliumot termel: **az 1. szinten óránként 40-et, a 20. szinten 1 280-at** (5. szint: 144; 10. szint: 360; 15. szint: 760). Megépítése 5 000 kreditbe és 500 Thuliumba kerül.
- Mindkettőnek energia kell, és mindkettő 72 órányi termelését tárolja, amíg be nem gyűjtöd.

## Az ellátási lánc {#the-supply-chain}

Négy modul alakítja a billentyűzettől távol töltött időt a legjobb lézereid lemezeivé. Az érc **kizárólag** a gyűjtőktől származik (az összes anyag és pénznem a [Nyersanyagok](/wiki/06-Items/Resources.md) oldalon található): az idegenek nem dobják el, és a Bolt sem árulja. (Az [óriás kotrógép](/wiki/03-Mechanics/Giant-Excavator.md) is hagy némi Velkonite-ot és Orviumot ládákban, de ez az érc a rakományodba kerül, és csak az [Ércrakodó](#ore-bay) rakja át az Erőforrás-raktárba, ahonnan a kovácsműhely és a Kutatóközpont veszi.)

1. Egy **gyűjtő** ércet bányászik, óránként egy meghatározott mennyiséget, a saját tárolójába (72 órányi termelés fér bele).
2. A **begyűjtés** áthelyezi az ércet a tárolóból az **Erőforrás-raktárba**, a bankba, ahol minden érc külön van tárolva.
3. A **Kovácsműhely** az adag indulásakor kiveszi a raktárból a szükséges ércet, és lemezeket készít, lemezenként 10 másodperc alatt, egyszerre egy adagot.
4. A **Lemezek begyűjtése** a kész lemezeket a készletedbe helyezi (a hajódnak leszállt állapotban kell lennie). A [Gyártás](/wiki/06-Items/Lasers.md) ezekből Quantum Laser III-at, Starfire-III-at vagy Helios Beamet készít, és mindkét fajta lemezből egyet-egyet 5 Dark Matterrel együtt egy Dark Matter Plate-té alakít, amelyet a Gyártás [Kovácsműhelye](/wiki/06-Items/Forge.md) és minden fejlesztési lánc utolsó szintje kér.

### Velkonite-gyűjtő és Orvium-gyűjtő {#velkonite-collector-and-orvium-collector}

- **Érc**: a Velkonite-gyűjtő az 1. szinten **óránként 10 Velkonite-ércet** bányászik, az Orvium-gyűjtő pedig **óránként 10 Orvium-ércet**, és minden szintnek saját üteme van: a 20. szinten legfeljebb óránként 80 Velkonite és 40 Orvium (5. szint: óránként 18 és 14; 10. szint: 32 és 24).
- **Tároló**: mindkettő 72 órányi ércet tárol, és ha megtelt, leáll a bányászattal.
- **Begyűjtés**: az ércet az Erőforrás-raktárba helyezi, amennyi belefér. Ha nincs raktár megépítve, vagy az adott érc raktára tele van, nincs hová tenni, és a gomb megmondja, miért. A maradék a tárolóban marad.
- **Energia**: 20 (Velkonite) és 30 (Orvium) az 1. szinten, szintenként 15%-kal növekedve.

### Erőforrás-raktár {#resource-storage}

- **Raktár**: külön tartja a Velkonite- és az Orvium-ércet, és mindkettőből más mennyiséget tárol: **ércenként 240-et** az 1. szinten, a 20. szinten legfeljebb 7 680 Velkonite-ot és 3 840 Orviumot (5. szint: 720 és 560; 10. szint: 1 920 és 1 440).
- **Korlát**: az 1. szinten a gyűjtőjének egynapi termelése, a 20. szinten legfeljebb négynapi. Egy gyűjtő tárolója három napot bír, ezért a 13. szinttől a raktár legalább egy teli tárolót elbír.
- **A korlát fölött**: ha egy raktárban több van, mint a korlátja (a 0.4.10-es frissítés kifizetése ilyen helyzetet hagyhatott), semmit nem vesznek el, de a Begyűjtés nem tesz hozzá több ilyen ércet, amíg el nem használtál belőle valamennyit.
- Érc a gyűjtőből való begyűjtéssel vagy a készletedből az [Ércrakodón](#ore-bay) át kerül be, és csak a Kovácsműhelybe és a Kutatóközpontba kerülhet ki. Sosem kerül vissza a készletedbe.
- **A raktárban lévő érc megmarad** a szezon wipe-ja után is.
- **Energia**: 10 az 1. szinten, szintenként 10%-kal növekedve. Nem kapcsolható ki.

### Kovácsműhely {#forgery}

- **Lemezek**: a Kovácsműhely **Velkonite Reinforced Plate**-et készít Velkonite-ércből és **Orvium Reinforced Plate**-et Orvium-ércből: lemezenként **40 Velkonite** vagy **80 Orvium** az 1. szinten, és minden szinttel kevesebb, a 20. szinten már csak 30 és 60 (75% alá sosem).
- **Adagok**: egyszerre egy adag egyfajta lemezből, **10 lemez az 1. szinten**, és az 1. szint fölötti minden szinttel 5-tel több. Az érc abban a pillanatban elhagyja az Erőforrás-raktárat, amikor az adag elindul, és minden lemez **10 másodpercig** készül. A lemezek egymás után készülnek, akkor is, amikor távol vagy.
- **Lemezek begyűjtése**: a kész lemezeket a készletedbe helyezi, miközben a **hajód leszállt**, és az adag többi része tovább készül. Új adag akkor indítható, amikor a Kovácsműhely üres.
- Egy futó adag akkor is befejeződik, ha kikapcsolod a Kovácsműhelyt, vagy fejleszted. Egy **új** adaghoz a Kovácsműhelynek bekapcsolva kell lennie, nem állhat fejlesztés alatt, és a Skylab energiájának egyensúlyban kell lennie.
- **Energia**: 30 az 1. szinten, szintenként 15%-kal növekedve.
- **Nem eladható**: a Kovácsműhely lemezei nem adhatók el az [Aukción](/wiki/03-Mechanics/Auction.md#marketable-items), különben ők lennének a Piac legnagyobb árucikke. Anyagként továbbra is használhatók a Gyártásban és a Kovácsműhelyben.

### Építésük {#building-them}

A két gyűjtő darabja **10 Ship Fragments, 20 000 kredit és 500 Thulium**, az Erőforrás-raktár **10 Ship Fragments, 5 000 kredit és 250 Thulium**, a Kovácsműhely **10 Ship Fragments, 5 000 kredit és 500 Thulium**; mind a négyhez a Mag 5. szintje kell.

- A Ship Fragments a készletedből vonódik le (nem a tranzittárolóból), és a hajódnak leszállt állapotban kell lennie. Az építési adatlap megmutatja, mid van, mennyi kell hozzá, és mi hiányzik.
- Energiát használnak. Építés előtt az adatlap megmutatja az energiaegyenlegedet most és utána: **az építés energiahiányba vihet egy állomást**, ha a Napelem lemaradt a többi modul mögött, és egyetlen energiahiány minden farmot és gyűjtőt leállít. Kapcsolj ki egy modult, vagy előbb fejleszd a Napelemet.
- A két gyűjtő az állomás feletti tartószerkezeteken függ, az Erőforrás-raktár a Mag északkeleti portjánál, a Kovácsműhely pedig az északnyugati portjánál van.

## A Kutatóközpont {#the-research-centre}

A kilencedik modul a nyersanyagokat tudománnyá alakítja, és kikutatja azokat a technológiákat, amelyekre a Gyártásnak szüksége van, mielőtt bármi újat elkészítene. A Mag 10. szintjétől építhető, 1–10. szintje van, energiát fogyaszt, és nem kapcsolható ki. A számai, az, hogy mit éget el üzemanyagként, a boost és a teljes technológiafa a [Kutatás](/wiki/03-Mechanics/Research.md) oldalon található. A legmagasabb technológiákhoz Dark Matter is kell, amelyet a Központhoz adsz: a [Dark Matter és Dark Matter Plate-ek](/wiki/03-Mechanics/Dark-Matter.md) leírja, hogyan szerezhetsz.

## A híd és a 2. Mag {#the-bridge-and-core-2}

A Mag **10. szintre** fejlesztése felépít egy **hidat** és egy második Magot. A híd a Mag északi csatlakozójához kapcsolódik, ahol a Napelem állt, és a túlsó végén a **2. Maghoz** köti.

- **Költség**: a 9. szintről a 10.-re lépés a 38 443 kreditje mellett **2 000 Thuliumba** kerül, és ugyanannyi ideig tart, mint eddig, 1 h 20 min. A híd és a 2. Mag semmibe sem kerül többe, és nincs saját idejük. A már futó fejlesztés megtartja azt az árat, amelyen elindult, a 10. szinten vagy afölött lévő Mag pedig nem fizet semmit.
- **A 2. Magnak nincs szintje**: nincs mit fejleszteni vagy fizetni. **Hat további modulfoglalatot** ad az állomásodnak, és a Mag kártyája megmutatja, hány szabad közülük.
- **A Napelem átköltözik**: a Napelem elhagyja a Mag északi csatlakozóját, amelyet most a híd foglal el, és a 2. Mag északi csatlakozójára kerül, az állomás túlsó végére. A szintje, az energiája és a folyamatban lévő fejlesztés érintetlen marad.
- **Szabály, nem építkezés**: hogy melyik modul hol áll, kizárólag a Mag szintjétől függ. A híd abban a pillanatban megjelenik, amikor a Mag 10. szintre fejlesztése elkészül (egy halk hang és egy üzenet szól róla), a Skylab pedig, amelynek Magja már a 10. szinten vagy afölött van, a következő megnézéskor megkapja. Egyetlen modul sem vész el vagy törlődik, csak a Napelem helye változik.
- **Foglalatok**: a **Lőszernyomtató** a 2. Mag északkeleti foglalatát foglalja el, a **Rakétagyár** az északnyugatit, az **Ércrakodó** pedig a keleti tartószerkezetet; a másik három szabad marad a későbbi moduloknak. Mindhárom csak akkor építhető, ha a 2. Mag már áll: addig az Építés gomb azt írja: „2. Mag kell”.
- **Szintek**: a 2. Magon álló modul ugyanúgy követi a Mag szintjét, mint bármelyik másik modul: egyik sem léphet a Mag fölé, így a 2. Mag foglalatokat ad, nem szinteket.

### Lőszernyomtató {#ammo-printer}

A Lőszernyomtató a semmiből nyomtat lézerlőszert, egyszerre egy fajtát: nem kell hozzá érc és kredit, csak energia. Az 1–20. szintje van.

- **Termelés**: **x2** (Advanced Plasma) **óránként 100 az 1. szinten, 2 000 a 20. szinten** (szintenként 100-zal több); **x3** (Ultra Core) ennek a fele, 50–1 000; **x4** (Experimental Fusion Core) a negyede, 25–500.
- **Mód**: az x2, x3 vagy x4 módot a kártyáján vagy az adatlapján választod. Váltáskor a már eltárolt órák megmaradnak, és onnantól az új mód ütemében számítanak.
- **Tárolás**: egy nap, 24 órányi termés az éppen használt szinten és módban (2 400 x2 az 1. szinten, 48 000 a 20. szinten). Az offline idő is számít, a megtelt tároló pedig egyszerűen megáll.
- **Begyűjtés**: a teljes egységeket a készletedbe helyezi, miközben a **hajód leszállt**. A lőszernek nincs szállítási korlátja, az egység törtrésze pedig megmarad, és tovább számít.
- **Energia**: 40 az 1. szinten, szintenként 20%-kal növekedve. Energiahiányban ugyanúgy leáll, mint a farmok és a gyűjtők, amit pedig tárol, az megmarad, és begyűjthető.
- **Építés**: 20 000 kredit, 500 Thulium és 10 Ship Fragments (a készletedből, leszállt hajóval), csak a 2. Magon. A fejlesztései 21 000 kredittől és 140 Thuliumtól 5 600 000 kreditig és 11 000 Thuliumig kerülnek, és ugyanannyi ideig tartanak, mint a Kovácsműhelyé: 5 perctől 24 óráig, összesen 5 d 13 h (lásd az alábbi táblázatokat).
- **Nem eladható**: amit nyomtat, azt nem lehet eladni az [Aukción](/wiki/03-Mechanics/Auction.md#marketable-items).

### Rakétagyár {#rocket-factory}

A Rakétagyár a semmiből gyártja a Bolt rakétáit, egyszerre egy fajtát. Az 1–20. szintje van.

- **Mit gyárt**: a Bolt tizenkét rakétája közül mindig csak egyet, azt, amelyiket kiválasztod: Lancet, Rivet, Scatter vagy Ember, I., II. és III. fokozat. Az N.U.K.E.-ot és az N.I.K.E.-ot sosem gyártja.
- **Termelés**: a III. fokozat **óránként 0,5 az 1. szinten, 10 a 20. szinten** (szintenként 0,5-del több), a II. fokozat ennek 1,25-szerese, az I. fokozat a kétszerese. Csak a teljes rakéták számítanak: egy rakéta törtrésze megmarad, és tovább számít.
- **Tárolás**: egy nap, 24 órányi termés az éppen használt szinten és rakétával (240 III. fokozatú a 20. szinten). Az offline idő is számít, a megtelt tároló egyszerűen megáll, a rakétaváltás pedig megtartja a már eltárolt órákat.
- **Begyűjtés**: a rakétákat a készletedbe helyezi, miközben a **hajód leszállt**, annyit, amennyit elbírsz: legfeljebb 5 000 I. fokozatút, 2 000 II. fokozatút és 500 III. fokozatút, a Bolt saját korlátját. Ami nem fér el, az a gyárban marad.
- **Energia**: 24 az 1. szinten, szintenként 15%-kal növekedve. Energiahiányban ugyanúgy leáll, mint a nyomtató.
- **Építés**: 20 000 kredit, 500 Thulium és 15 Ship Fragments (a készletedből, leszállt hajóval), csak a 2. Magon. A fejlesztései a nyomtatóénak negyedébe kerülnek, 5 300 kredittől és 35 Thuliumtól 1 400 000 kreditig és 2 800 Thuliumig, és ugyanannyi ideig tartanak: összesen 5 d 13 h.
- **Nem eladható**: amit gyárt, azt nem lehet eladni az [Aukción](/wiki/03-Mechanics/Auction.md#marketable-items).

### Ércrakodó {#ore-bay}

Az Ércrakodó a nálad lévő ércet az Erőforrás-raktárba rakja át. Az [óriás kotrógép](/wiki/03-Mechanics/Giant-Excavator.md) Velkonite-ot és Orviumot hagy ládákban, amelyek a rakományodba kerülnek, ahol egyetlen modul sem használja őket; az Ércrakodó az út onnan a raktárba, ahonnan a Kovácsműhely és a Kutatóközpont veszi. Az 1–20. szintje van.

- **Mit rak át**: a **Velkonite-ot és az Orviumot**, a két ércet, amelyet az Erőforrás-raktár tárol. A Cataclysite és a Quorvium üzemanyag, amelyet a Kutatóközpont és a Gyártás [Kovácsműhelye](/wiki/06-Items/Forge.md) közvetlenül a készletedből vesz, a Thulium pedig felvételkor a számládra kerül.
- **Egy irányba**: a készletedből az Erőforrás-raktárba, soha vissza. Csak a készletedben lévő laza érc kerül át, soha nem az, ami a Tranzittárolóban van.
- **Hogyan**: a **hajódnak le kell szállnia**. Az átrakás azonnali: az Ércrakodó lapján válaszd ki az ércet, írj be egy mennyiséget vagy nyomd meg a Max gombot, majd az **Átrakás** gombot. A lap mutatja, mennyit hordasz, és mennyi van a raktárban a kapacitásához képest.
- **Keret**: a szint határozza meg, óránként mennyi ércet rak át, **1. szinten 10-et, a 20. szinten 320-at**, és ebből legfeljebb egy napnyit tart készenlétben (1. szinten 240-et, a 20. szinten 7 680-at). Az új Ércrakodó teli nappal indul, a fejlesztés megtartja, ami el volt tárolva. Az átrakást korlátozza a nálad lévő érc, a hely, amely az Erőforrás-raktárban még maradt, és a keret, és a lap megmondja, melyik.
- **Energia**: 15 az 1. szinten, szintenként 10%-kal növekedve (a 20. szinten 92). Kikapcsolható. Energiahiányban, amíg ki van kapcsolva, és amíg fejlesztik, nem rak át semmit.
- **Építés**: 5 000 kredit, 250 Thulium és 10 Ship Fragments (a készletedből, leszállt hajóval), csak a 2. Magon. A fejlesztései annyiba kerülnek, mint az Erőforrás-raktáréi, és ugyanannyi ideig tartanak (lásd az alábbi táblázatokat).
- **Nem út több ércért**: olyan ércet rak át, amid már van. Az óriás kotrógép egy menete a forrásnál korlátozott, a bankot pedig az Erőforrás-raktár kapacitása korlátozza.

## Mechanika {#mechanics}

### Építés és fejlesztés {#building-and-upgrading}

- **Építés**: minden modul külön épül meg. Egy modul az építése pillanatában 1. szintű, és a fejlesztése növeli a termelését (vagy a termelt energiáját) és a raktárát, és azt is, mennyi energiát használ.
- **Idő és költség**: a fejlesztések kreditbe és Thuliumba kerülnek, és időt vesznek igénybe, és minden modulnak minden szintre saját ára és ideje van (vidd az egeret a **Fejlesztés** gomb fölé a következő megtekintéséhez; az összegek lent vannak). Az árat a fejlesztés indításakor fizeted. A költség nem függ az időtől.
- **Időzítők**: a fejlesztés a szerver óráján fut, ezért akkor is befejeződik, amikor távol vagy, ha kell, napokkal később. Indítsd el, jelentkezz ki, gyere vissza: a modul az új szintjén van, amikor megnyitod a Skylab oldalt.
- **Fejlesztési idők**: az első szintek gyorsak, az utolsók akár 36 óráig tartanak, a Magé akár 6 napig (lásd az alábbi táblázatokat). Minden modulnak saját időzítője van, így többet is fejleszthetsz egyszerre.
- **Termelési szünet**: amíg egy modult fejlesztenek, offline: nem termel, és nem használ energiát. A Napelem kivétel: az energiája negyedét tovább termeli (lásd lent).
- **A Napelem fejlesztés közben csak az energiája 25%-át termeli**: a Napelem termeli a Skylab összes energiáját, és fejlesztés közben (az utolsó szintnél 24 óra) a **jelenlegi** szintje energiájának egynegyedét termeli; az új szint energiája attól a pillanattól veszi át, hogy a fejlesztés véget ér. Egy teljes állomás nagyjából annak a 90%-át használja, amit a Napelem a saját szintjén termel, ennek az egynegyede tehát csak egy olyan állomást bír el, amely öt-hat szinttel a Napelem alatt van. Különben minden farm és gyűjtő leáll a teljes fejlesztés idejére, amit tárolsz, megmarad és begyűjthető, a Kovácsműhely pedig nem indít új adagot. Az a modul, amelyet fejlesztenek vagy kikapcsoltak, nem használ energiát, ezért a farmok fejlesztése a Napelemmel együtt nem kerül semmibe, a modulok kikapcsolása pedig helyet csinál a többinek; a Thuliumfarm használ messze a legtöbb energiát.

### Mibe kerül {#what-it-costs}

Az egész út ára, az építés plusz minden fejlesztés, a 10. szintig és a 20. szintig. A Mag mindig ott van, és a lépései kreditbe kerülnek, a 10. szintre vezető lépés még 2 000 Thuliumba; a Kutatóközpontnak 1–10. szintje van, és a számai a [Kutatás](/wiki/03-Mechanics/Research.md) oldalon vannak. A Lőszernyomtató, a Rakétagyár és az Ércrakodó a 2. Magon épül, tehát csak akkor, ha a Mag a 10. szinten van, és az 1. szintjük maga az építés.

| Modul | Kredit a 10. szintig | Thulium a 10. szintig | Kredit a 20. szintig | Thulium a 20. szintig |
| :--- | ---: | ---: | ---: | ---: |
| Mag | 112 326 | 2 000 | 6 647 504 | 2 000 |
| Napelem | 1 219 500 | 1 600 | 35 039 500 | 36 850 |
| Kreditfarm | 840 000 | 109 | 26 240 000 | 2 399 |
| Thuliumfarm | 1 154 000 | 4 190 | 32 254 000 | 67 890 |
| Velkonite-gyűjtő | 696 000 | 6 950 | 20 996 000 | 78 950 |
| Orvium-gyűjtő | 696 000 | 6 950 | 20 996 000 | 78 950 |
| Erőforrás-raktár | 619 500 | 359 | 18 169 500 | 2 649 |
| Kovácsműhely | 1 224 000 | 2 050 | 35 044 000 | 37 300 |
| Lőszernyomtató | 1 411 000 | 5 140 | 22 031 000 | 47 940 |
| Rakétagyár | 377 300 | 1 674 | 5 547 300 | 12 494 |
| Ércrakodó | 619 500 | 359 | 18 169 500 | 2 649 |

Az első lépések olcsók, az utolsók drágák: a Kreditfarm lépése az 1. szintről a 2.-ra 5 000 kreditbe és 1 Thuliumba kerül, a 19.-ről a 20.-ra 7 000 000 kreditbe és 550 Thuliumba. A Thuliumfarmé 7 000 kredit és 45 Thulium, majd 8 500 000 kredit és 16 000 Thulium. A Napelem fejlesztései minden szinten ugyanannyiba kerülnek, mint a Kovácsműheléi, és a két gyűjtő ugyanannyiba kerül.

### Fejlesztési idők {#upgrade-times}

<!-- upgrade-times:start -->
<!-- Generated from server/Resources/SkylabConfig.json by the test skylab::duration_tests::the_wiki_page_is_the_config (run it with SKYLAB_WIKI_WRITE=1 to rewrite this part). -->

**Fejlesztési idők**, modulonként (a fejlesztés az első oszlopban szereplő szintről indul):

| Szint | Mag | Napelem | Kreditfarm | Thuliumfarm | Erőforrás-raktár | Velkonite-gyűjtő | Orvium-gyűjtő | Kovácsműhely | Kutatóközpont |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 → 2 | 72 mp | 5 perc | 5 perc | 5 perc | 5 perc | 5 perc | 5 perc | 5 perc | 78 mp |
| 2 → 3 | 86 mp | 15 perc | 10 perc | 15 perc | 10 perc | 15 perc | 15 perc | 15 perc | 101 mp |
| 3 → 4 | 104 mp | 30 perc | 15 perc | 30 perc | 15 perc | 20 perc | 20 perc | 30 perc | 132 mp |
| 4 → 5 | 124 mp | 45 perc | 20 perc | 45 perc | 20 perc | 30 perc | 30 perc | 45 perc | 171 mp |
| 5 → 6 | 149 mp | 1 óra | 30 perc | 1 óra | 30 perc | 45 perc | 45 perc | 1 óra | 223 mp |
| 6 → 7 | 20 perc | 1 óra 15 perc | 45 perc | 1 óra 30 perc | 45 perc | 50 perc | 50 perc | 1 óra 15 perc | 20 perc |
| 7 → 8 | 30 perc | 1 óra 30 perc | 1 óra | 2 óra | 1 óra | 1 óra | 1 óra | 1 óra 30 perc | 30 perc |
| 8 → 9 | 50 perc | 2 óra | 1 óra 20 perc | 3 óra | 1 óra 20 perc | 1 óra 15 perc | 1 óra 15 perc | 2 óra | 50 perc |
| 9 → 10 | 1 óra 20 perc | 3 óra | 1 óra 40 perc | 4 óra | 1 óra 40 perc | 1 óra 30 perc | 1 óra 30 perc | 3 óra | 1 óra 20 perc |
| 10 → 11 | 2 óra 15 perc | 4 óra | 2 óra | 5 óra | 2 óra | 2 óra | 2 óra | 4 óra | – |
| 11 → 12 | 3 óra 30 perc | 5 óra | 2 óra 30 perc | 6 óra | 2 óra 30 perc | 3 óra | 3 óra | 5 óra | – |
| 12 → 13 | 5 óra 30 perc | 6 óra | 3 óra | 8 óra | 3 óra | 4 óra | 4 óra | 6 óra | – |
| 13 → 14 | 9 óra | 8 óra | 3 óra 30 perc | 10 óra | 3 óra 30 perc | 6 óra | 6 óra | 8 óra | – |
| 14 → 15 | 14 óra | 10 óra | 4 óra | 11 óra | 4 óra | 8 óra | 8 óra | 10 óra | – |
| 15 → 16 | 1 nap | 12 óra | 5 óra | 12 óra | 5 óra | 10 óra | 10 óra | 12 óra | – |
| 16 → 17 | 1 nap 12 óra | 16 óra | 6 óra | 14 óra | 6 óra | 12 óra | 12 óra | 16 óra | – |
| 17 → 18 | 2 nap 12 óra | 18 óra | 8 óra | 18 óra | 8 óra | 16 óra | 18 óra | 18 óra | – |
| 18 → 19 | 4 nap | 20 óra | 10 óra | 1 nap | 10 óra | 20 óra | 1 nap | 20 óra | – |
| 19 → 20 | 6 nap | 1 nap | 12 óra | 1 nap 12 óra | 12 óra | 1 nap | 1 nap 12 óra | 1 nap | – |
| **Összesen** | 16 nap 13 óra | 5 nap 13 óra | 2 nap 14 óra | 6 nap 13 óra | 2 nap 14 óra | 4 nap 16 óra | 5 nap 10 óra | 5 nap 13 óra | 3 óra 12 perc |
<!-- upgrade-times:end -->

Egy fejlesztés, amely már fut, amikor az idők megváltoznak, megtartja a neki adott befejezési időt. Csak a Mag fejlesztése az 1. szintről a 20. szintre egymás után nagyjából **16 és fél napig** tart. Egyetlen modul sem mehet a Mag szintje fölé, így minden más modul utolsó lépése (12–36 óra) csak akkor indulhat, amikor a Mag a 20. szinten van: ha minden időzítő végig foglalt, és megvan a kredit meg a Thulium, az egész állomás nagyjából **18 nap** alatt készül el.

### Energiagazdálkodás {#power-management}

A Skylabodnak korlátozott az energiakerete.

- **Egyenleg**: tartsd a Napelem termelését az összes többi modul által használt energia fölött. A Skylab oldal mutatja az egyenleget, és figyelmeztet, mielőtt egy építés nulla alá nyomná.
- **A Napelem lépést tart**: egy N. szintű Napelem **az összes többi modul energiáját fedezi az N. szinten** (a Mag, mindkét farm, az Erőforrás-raktár, mindkét gyűjtő és a Kovácsműhely, a 10. szinttől pedig a Kutatóközpont és az Ércrakodó), és még nagyjából egy tizedet, így az az állomás, amelynek minden modulja a 7. szinten van, 7. szintű Napelemet igényel, és az fedezi is. Egy szinttel alacsonyabb Napelem nem elég egy teljes állomásnak (az utolsó oszlop), ezért a Napelemnek továbbra is követnie kell a többit felfelé. A Mag keveset fogyaszt, ezért előrefuthat: az 5. vagy magasabb szintű Napelem egy teljes, a saját szintjén álló állomást fedez, a Mag bármelyik szintjével. Az alábbi táblázat a Lőszernyomtatót is a 7. szinttől, a Rakétagyárat és az Ércrakodót pedig a 10. szinttől számolja.
- **Aktív állapot**: a farmokat, a gyűjtőket és a Kovácsműhelyt be- vagy kikapcsolhatod az energia kezeléséhez. A Mag, a Napelem, az Erőforrás-raktár és a Kutatóközpont mindig működik. A Lőszernyomtató, a Rakétagyár és az Ércrakodó is be- és kikapcsolható.
- **Energiahiány**: ha az energiafogyasztás nagyobb a termelt energiánál, minden farm és gyűjtő leáll a termeléssel, amíg az egyenleg helyre nem áll. Amit már tárolnak, megmarad, és továbbra is begyűjtheted. A Kovácsműhely nem indít új adagot, a Kutatóközpont pedig új kutatást (a már futó kutatás tovább megy). A Lőszernyomtató, a Rakétagyár és az Ércrakodó ugyanúgy leáll, mint a farmok és a gyűjtők.
- **A Napelem fejlesztése**: amíg a Napelemet fejlesztik, az energiájának csak a negyedét termeli, ezért ha a többi modulod nincs jóval alatta, az állomás hiányba kerül, és a farmok meg a gyűjtők leállnak, amíg a fejlesztés el nem készül (lásd: [Napelem modul](#solar-module)).

A Napelem energiája minden szinten, szemben azzal, amit a többi modul használ ugyanazon a szinten (minden modul azon a szinten, a Magot is beleértve, a Kutatóközpontot és az Ércrakodót pedig a 10. szinttől):

<!-- skylab-power:start -->
<!-- Generated from server/Resources/SkylabConfig.json by docs/design/skylab-power-model.py --doc (--check fails while this part is behind). -->

| Szint | A Napelem termel | A többi modul használ | Marad | Egy szinttel alacsonyabb Napelemmel |
| :--- | ---: | ---: | ---: | :--- |
| 1 | 255 | 230 | 25 | – |
| 2 | 310 | 278 | 32 | 255: 23 hiányzik |
| 3 | 375 | 337 | 38 | 310: 27 hiányzik |
| 4 | 455 | 410 | 45 | 375: 35 hiányzik |
| 5 | 555 | 501 | 54 | 455: 46 hiányzik |
| 6 | 680 | 615 | 65 | 555: 60 hiányzik |
| 7 | 965 | 875 | 90 | 680: 195 hiányzik |
| 8 | 1 185 | 1 076 | 109 | 965: 111 hiányzik |
| 9 | 1 460 | 1 327 | 133 | 1 185: 142 hiányzik |
| 10 | 2 035 | 1 849 | 186 | 1 460: 389 hiányzik |
| 11 | 2 490 | 2 260 | 230 | 2 035: 225 hiányzik |
| 12 | 3 055 | 2 774 | 281 | 2 490: 284 hiányzik |
| 13 | 3 765 | 3 421 | 344 | 3 055: 366 hiányzik |
| 14 | 4 660 | 4 235 | 425 | 3 765: 470 hiányzik |
| 15 | 5 790 | 5 262 | 528 | 4 660: 602 hiányzik |
| 16 | 7 220 | 6 562 | 658 | 5 790: 772 hiányzik |
| 17 | 9 035 | 8 209 | 826 | 7 220: 989 hiányzik |
| 18 | 11 335 | 10 301 | 1 034 | 9 035: 1 266 hiányzik |
| 19 | 14 260 | 12 962 | 1 298 | 11 335: 1 627 hiányzik |
| 20 | 17 990 | 16 353 | 1 637 | 14 260: 2 093 hiányzik |
<!-- skylab-power:end -->

A táblázat minden modult ugyanazon a szinten számol. A Thuliumfarm a csúcson ennek közel a háromnegyedét használja (11 695-öt a 20. szinten, szemben a mind a tizenegy modul 16 353-ével), ezért az az állomás, amelyen ez a farm messze a többi előtt jár, több Napelemet igényel, mint amennyit a Magja sugall.

### Begyűjtés {#collecting}

Minden farmnak és gyűjtőnek van egy tárolója nagyjából 72 órányi termeléséhez. Kézzel gyűjtesz be.

- **Kapacitás**: ha egy tároló megtelt, leáll a termeléssel, amíg be nem gyűjtesz.
- **Farmok**: a begyűjtött kredit és Thulium egyenesen a számládra kerül.
- **Gyűjtők**: az érc az Erőforrás-raktárba kerül, amennyi belefér.
- **Kovácsműhely**: a lemezek a készletedbe kerülnek, ha a hajód leszállt.
- **Lőszernyomtató és Rakétagyár**: a lőszer és a rakéták a készletedbe kerülnek, ha a hajód leszállt. Mindegyik csak 24 órányi termést tárol (lásd: [Lőszernyomtató](#ammo-printer) és [Rakétagyár](#rocket-factory)).
- **Ércrakodó**: nincs mit begyűjteni. A készleted ércét az Erőforrás-raktárba rakja át, amikor megnyomod az **Átrakás** gombot, leszállt hajóval, a keretéig (lásd: [Ércrakodó](#ore-bay)).
- Az **Összes begyűjtése** mindent egyszerre elvisz, a kikapcsolt és a fejlesztés alatt álló modulokat is.
- Egy **(!)** jelvény mutatja a kiüríthető, tele tárolót és a Kovácsműhelyben várakozó lemezeket a Skylab oldalon és az oldalsáv Skylab feliratú sorában.

### A wipe {#the-wipe}

A wipe sosem érinti a Skylabot: a modulok megtartják a szintjüket, az Erőforrás-raktár az ércét, a Kutatóközpont pedig a technológiáit, a tudománytartályát, a benne lévő Dark Mattert és a folyamatban lévő kutatást. A készletedben lévő lemezek olyan tárgyak, mint bármelyik másik, ezért a [wipe-szabályokat](/wiki/03-Mechanics/Wipe-Timeline.md) követik. A Lőszernyomtató és a Rakétagyár megtartja a szintjét, azt, hogy mit kell gyártania, és azt, amit tárol, az Ércrakodó pedig a szintjét és a keretét. A készletedben lévő érc a többi tárgyhoz hasonlóan elvész: előtte rakd át az Erőforrás-raktárba.

## A Skylabod megtervezése {#planning-your-skylab}

A Skylab hetekig nő, ezért egy kis tervezés megtérül. A számok a fenti táblázatok.

### Mit fejlessz először {#what-to-upgrade-first}

1. **Először a Napelem, aztán a Kreditfarm.** A Napelem 500 kreditbe és 50 Thuliumba kerül, és nélküle semmi sem működik; a Kreditfarm semmibe sem kerül. A tíz [állomásküldetés](/wiki/03-Mechanics/Quests.md#station-missions) végigvisz ezeken az első lépéseken, és 52 000 kreditet meg 610 Thuliumot fizet értük, alapértékben: a világod, a boostereid és a klánod bónuszai megszorozzák.
2. **Aztán a Thuliumfarm: ez a fő Thulium-forrásod.** A 10. szinten óránként 360 Thuliumot termel, naponta 8 640-at, nagyjából annyit, amennyit 43 [Crystalys](/wiki/04-Aliens/Crystalys.md) lelövése fizet Alphában (egyenként 200). A 10. szintig vezető út 1 154 000 kreditbe és 4 190 Thuliumba kerül, az építést is beleszámítva. A 15. szinten a farm naponta 18 240-at, a 20. szinten 30 720-at termel. A tárolója 72 órát bír, ezért legalább háromnaponta nézz vissza. Hogy mit lehet venni Thuliumért, azt a [Nyersanyagok](/wiki/06-Items/Resources.md#thulium) oldal mutatja.
3. **A Kreditfarm az egyenletes mellékjövedelem.** A 10. szinten óránként 11 250 kreditet, naponta 270 000-et termel, 840 000 kreditért és 109 Thuliumért. A magasabb szintek lassan térülnek meg: a 9.-ről a 10. szintre vezető lépés 300 000 kreditbe kerül óránként 1 500 többletért, vagyis 200 óra alatt térül meg. Akkor fejleszd, ha marad felesleges kredited.
4. **Tartsd foglalkoztatva a Magot.** Semmi sem megy a Mag fölé, és a Mag egyedül nagyjából 16 és fél nap alatt ér el a 20. szintre. Nincs sor, ezért minden visszatéréskor indítsd el a következő lépését.
5. **Az ellátási láncot egy csomagban építsd.** A gyűjtők, az Erőforrás-raktár és a Kovácsműhely a Mag 5. szintjén nyílnak meg. Egy gyűjtő csak Erőforrás-raktárba tud ércet betenni, és a raktár az 1. szinten a gyűjtője egynapi termelését, a 20. szinten négynapit bír el, ezért az Erőforrás-raktárt a gyűjtőkkel együtt fejleszd, különben az érc a tárolójukban vár.
6. **Tarts készenlétben 2 000 Thuliumot a Mag 10. szintjéhez.** A Mag 9-ről 10-re lépése kéri, és felépíti a hidat és a 2. Magot, ahol a [Lőszernyomtató](#ammo-printer), a [Rakétagyár](#rocket-factory) és az [Ércrakodó](#ore-bay) épül.

### A Napelem fejlesztésének időzítése {#timing-a-solar-upgrade}

Amíg a Napelemet fejlesztik, az energiája negyedét termeli, és egy állomás szinte mindig többet használ ennél. A farmok és a gyűjtők ilyenkor leállnak a teljes fejlesztés idejére: amit tárolnak, megmarad, de amit termelhettek volna, elvész. A táblázat minden Napelem-lépésnél megadja az idejét, a legnagyobb állomást, amely még átmegy rajta (minden modul ugyanazon a szinten, a Maggal és az ellátási lánccal együtt; egy kisebb állomás kicsit tovább bírja), és azt, hogy egy ilyen szintű Kreditfarm és Thuliumfarm mennyit termelt volna közben. Például a Napelem 10-ről 11-re négy óra, és a 10. szintű farmok ennyi idő alatt 45 000 kreditet és 1 440 Thuliumot termeltek volna. A táblázat a Lőszernyomtatót is a 7. szinttől, a Rakétagyárat és az Ércrakodót pedig a 10. szinttől számolja.

| Napelem-fejlesztés | Idő | Állomás, amely tovább működik, a szintig | A Kreditfarm közben ennyit termel | A Thuliumfarm közben ennyit termel |
| :--- | ---: | ---: | ---: | ---: |
| 1 → 2 | 5 perc | egy sem | 63 | 3 |
| 2 → 3 | 15 perc | egy sem | 375 | 16 |
| 3 → 4 | 30 perc | egy sem | 1 125 | 44 |
| 4 → 5 | 45 perc | egy sem | 2 250 | 84 |
| 5 → 6 | 1 óra | egy sem | 3 750 | 144 |
| 6 → 7 | 1 óra 15 perc | egy sem | 6 563 | 230 |
| 7 → 8 | 1 óra 30 perc | 1 | 10 125 | 336 |
| 8 → 9 | 2 óra | 2 | 16 500 | 528 |
| 9 → 10 | 3 óra | 3 | 29 250 | 912 |
| 10 → 11 | 4 óra | 5 | 45 000 | 1 440 |
| 11 → 12 | 5 óra | 6 | 67 500 | 2 200 |
| 12 → 13 | 6 óra | 6 | 99 000 | 3 120 |
| 13 → 14 | 8 óra | 7 | 156 000 | 4 800 |
| 14 → 15 | 10 óra | 8 | 225 000 | 6 800 |
| 15 → 16 | 12 óra | 9 | 306 000 | 9 120 |
| 16 → 17 | 16 óra | 9 | 480 000 | 14 080 |
| 17 → 18 | 18 óra | 10 | 648 000 | 18 000 |
| 18 → 19 | 20 óra | 12 | 870 000 | 22 400 |
| 19 → 20 | 1 nap | 13 | 1 260 000 | 28 800 |

- **Fejleszd a farmokat a Napelemmel együtt.** A fejlesztés alatt álló modul amúgy sem termel és nem használ energiát, ezért az az idő, amelyet egy farm a szünet alatt fejlesztéssel tölt, nem kerül semmibe.
- **Tartsd alacsonyan a többi modult, ha nem engedhetsz meg magadnak szünetet.** Egy állomás csak akkor megy át egy Napelem-fejlesztésen, ha az összes többi modulja legalább öt szinttel a Napelem alatt van (a Napelem 10. szintjétől hattal), és egy teljes állomásnak valamivel több kell, ahogy a táblázat mutatja.
- **Kapcsold ki, amire nincs szükséged.** A kikapcsolt modul nem használ energiát, ezért a Thuliumfarm kikapcsolása, amely a legtöbbet használ (az 1. szinten 80-at, szintenként 30%-kal többet), helyet csinál a többinek.
