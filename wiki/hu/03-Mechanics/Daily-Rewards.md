<!-- wiki-i18n source: c6cf04f6e8e99425 -->
<!-- wiki-i18n title: Napi jutalmak -->
# Napi jutalmak {#daily-rewards}

<!-- wiki-search: daily reward; daily rewards; daily login; login bonus; login reward; calendar; advent calendar; chest; chests; season prize; souvenir; blueprint; streak; napi jutalom; napi jutalmak; napi belépés; naptár; adventi naptár; láda; szezonjutalom; szezonemlék; tervrajz; sorozat -->

Minden szezonnak van egy **napi jutalmak naptára**: egy kis ajándék a szezon minden napjára. Az állomáson nyomd meg az **Átvétel** gombot, és a nap ajándéka a tiéd. Minél több napot veszel át, annál többet kapsz: négy **láda** érkezik 7, 14, 21 és 28 átvett napnál, a szezon utolsó három napján pedig elvihetsz egy **szezonjutalmat**. Egy kihagyott nap csak az aznapi ajándékba kerül, másba nem. A naptárat az **Irányítópulton** találod (a **Napi jutalmak** kártya), illetve a **Szezon és profil › Naptár** alatt.

## Egy percben {#in-one-minute}

- **29 mező.** Egy-egy a szezon minden UTC-napjára. Egy szezon 30 napos, de a 30. nap a [wipe](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule) 5 perces visszaszámlálása, így azon nincs mit átvenni.
- **Te nyomod meg az Átvételt.** Egy nyomás egy mezőt vesz át, pilótánként egyszer. Helyetted semmi sem kerül átvételre.
- **6 óra türelmi idő.** Egy mező a napja vége után még 6 óráig nyitva marad.
- **Nincs sorozat.** Egy kihagyott nap az aznapi mezőbe kerül, másba nem. Az számít, hány napot vettél át, nem az, hogy egymás után voltak-e.
- **4 láda**, 7, 14, 21 és 28 átvett napnál.
- **Egy szezonjutalom** a szezon utolsó három napján: egy emlék-kinézet 10 átvett napnál és egy hajódizájn tervrajza 20-nál.
- **Minden wipe új naptárat hoz.** A szezon minden ajándékát látod az 1. naptól.
- **Szándékosan kicsi.** A 29 nap együtt nagyjából pár óra vadászat értékét adja, egy szezonra elosztva.

## A nap {#the-day}

A naptár napja egy **UTC-nap**: **00:00 UTC-kor** vált, minden pilótánál ugyanabban a pillanatban, és ugyanaz a napszámlálás, mint a klánok napi vonalán („29 nap közül az *n*.”, lásd [Klánok](/wiki/03-Mechanics/Clans.md#the-day)). Nem követi az időzónádat, és nem a Szezon oldal szezonnapja, az ugyanis azon a napszakon vált, amikor a szezon elkezdődött. A szerver órája dönt mindenről: a géped órája semmin nem változtat.

A kártya és a fül is megmondja, mikor nyílik a következő jutalom **a saját időzónádban** („Az új jutalmak nyitása: 02:00 a te idődben (00:00 UTC)”). Ha magad akarod kiszámolni, váltsd át a 00:00 UTC-t. Néhány példa:

| Hol | Az UTC éjfél ekkor van |
| :--- | :--- |
| Közép-Európa | 01:00 (télen) vagy 02:00 (nyáron) |
| Moszkva, Isztambul | 03:00 |
| Japán, Korea | 09:00 |
| USA keleti partja | 19:00 (télen) vagy 20:00 (nyáron) |
| USA nyugati partja | 16:00 (télen) vagy 17:00 (nyáron) |

- **Az 1. nap rövid.** A szezon a wipe-pal kezdődik, egy UTC-nap közepén, így az 1. mező attól fogva az adott nap végéig nyitva van, plusz a türelmi idő.
- **A 29. nap hosszú.** Az utolsó mező addig marad nyitva, amíg a wipe visszaszámlálása el nem indul, és ez több mint 24 órával a megnyílása után is lehet. A visszaszámlálás indulásától az új szezon kezdetéig semmit sem lehet átvenni.
- **Az adminisztrátorok áthelyezhetik a szezon napját.** A naptár követi: a kihagyott napok mindenkinek elmulasztottnak számítanak, az általad már átvett mező pedig átvett marad.

## A mezők {#the-tiles}

A Naptár fül egy rácsot mutat, minden naphoz egy mezővel: a nap száma, az ajándék és egy szavakkal kiírt állapot. A szezon minden ajándéka az első naptól látszik, így látod, mi következik. Azt is számolja, hány napot vettél át (például „11 / 29 nap átvéve”), és megmondja, mikor jön a következő láda. Az Irányítópult kártyája a mai ajándékot és egyetlen **Átvétel** gombot mutat.

| Állapot | Mit jelent |
| :--- | :--- |
| **Ma** | Most nyitva van. Nyomd meg az **Átvétel** gombot. |
| **Átvéve** | Megvan. |
| **Tegnap** | A tegnapi mező, a türelmi idő alatt még nyitva. Mutatja, mennyi idő van hátra, és saját **Átvétel** gombja van. |
| **Lemaradt** | A nap és a türelmi ideje lejárt. Az ajándék elveszett, más nem változott. |
| **Nyílik … múlva** | Egy eljövendő nap. Látod az ajándékát, de még nem veheted át. |
| **Csatlakozás előtt** | Az első bejelentkezésed előtti nap. Nem vehető át. |

Amíg egy jutalom vár, egy kis **(!)** jelenik meg az oldalsávban a **Szezon és profil** mellett, repülés közben pedig a **Vissza a bázisra** mellett, és bejelentkezéskor egy üzenet is szól róla (naponta és gépenként egyszer).

## Türelmi idő és kihagyott napok {#grace-and-missed-days}

Egy mező nem zár be éjfélkor: az UTC-napja vége után még **6 óráig** nyitva marad. Ez alatt a 6 óra alatt két mező nyitva van, a tegnapi és a mai, és mindkettőt külön nyomással veszed át. A türelmi idő után a tegnapi mező végleg **Lemaradt**, és ennél messzebb nem mehetsz vissza.

Egy kihagyott nap **az aznapi ajándékba kerül, másba nem**. Nincs sorozat, ami megszakadhatna: az átvett napjaid száma, a ládáid és a szezonjutalom mind folytatódnak. A türelmi idő alatt átvett mező pontosan úgy számít, mint az időben átvett.

## Ládák {#chests}

Egy láda azzal az **Átvétellel** érkezik, amelytől az átvett napjaid száma elér egy számot, korábban nem: nincs mit megnyomni, és nem kell kulcsot keresni. A darabszám számít, nem a dátum: a 7 napos láda a 7. átvett nappal jön, akármelyik napja is az a szezonnak.

| Láda | Ennyi átvett napnál jön |
| :---: | :--- |
| **1.** | 7 |
| **2.** | 14 |
| **3.** | 21 |
| **4.** | 28 |

Minden láda egy **Specimen Vault**-ot tartalmaz, azt a konténert, amelyben mindenből van egy kevés. A későbbi ládák hozzátehetnek egy kis extrát, amelyet a wipe nem visz el. A Naptár fül megmutatja, mi van az egyes ládákban. A konténer csak a tiéd, és a Konténerek oldalon nyitod ki. A ki nem nyitott konténer a [wipe](/wiki/03-Mechanics/Wipe-Timeline.md) után is a fiókodon marad.

Ha a játék nem tudja kiadni a konténert, például mert a konténerek nincsenek bekapcsolva, a láda helyette egy **csomagot** fizet ki kreditekből, Thuliumból és egy nagyjából egyenértékű boosterből. Egy láda sosem vész el, és sosem kapod meg mindkettőt.

## Szezonjutalom {#season-prize}

A szezonjutalomnak két lépcsője van. Ezeket a szezon **utolsó három napján** veheted át (a 27–29. napon), a wipe visszaszámlálásának indulásáig. A 27. nap előtt a fül azt mondja: **Az utolsó három napban nyílik**, még ha megvan is hozzá a napok száma. Minden lépcsőt egyszer lehet átvenni, tetszőleges sorrendben.

| Lépcső | Feltétele | Díj |
| :---: | :--- | :--- |
| **1** | 10 átvett nap | Egy **szezonemlék**: egy kinézet |
| **2** | 20 átvett nap | Egy **dizájn-tervrajz**: egy hajódizájn technológiája |

- **Az emlék** egy skin, egy szín, egy kipufogóeffekt vagy egy aura ([Kozmetika](/wiki/06-Items/Cosmetics.md)), amelyet a szezonra egy erre félretett kinézetekből álló rövid listáról választanak, és sosem Epikusnál magasabb. Mint minden kinézet, csak díszítés, a fiókodhoz tartozik, és a wipe után is megmarad. Ha már megvan, a következő olyan emléket kapod, amilyened még nincs. Ha mind megvan, 250 Thuliumot kapsz.
- **A tervrajz** egy hajódizájn kutatása, helyetted elvégezve: a dizájn technológiája és a technológiák, amelyekre szüksége van. A hajó átalakítása az új dizájnra továbbra is az Összeszerelésben történik, és továbbra is annyiba kerül, amennyit a [Hajódizájnok](/wiki/03-Mechanics/Ship-Designs.md#getting-a-design) oldal mond. Egy szezon dizájnja a 13 egyike, rögzített sorrendben véve, így egy dizájn 13 szezonig nem jön vissza. Ha már ismered, a következő olyan dizájnt kapod, amelyik még hiányzik. Ha mind a 13-at ismered, 4 Dark Matter Plate-et kapsz, amelyek tárgyak: a wipe előtt tedd őket a Tranzittárolóba.

## Az ajándékok {#the-gifts}

Egy nap ajándéka kicsi. Ezek egyike:

- **Lőszer és rakéták**, szerény halmokban.
- **Anyagok, lemezek és fogyóeszközök**, köztük Forge kitek (a Kovácsműhely egy lépésének anyagai).
- **Boosterek** pár órára. Egy booster-ajándék a saját óráit adja hozzá a [boostereidhez](/wiki/06-Items/Boosters.md#active-boosters).
- **Kreditek és Thulium**, kis mennyiségben.
- **Néhány különleges tárgy** (Workforce Contract, Forger's Seal): egy szezonban sosem több mint 4 mezőn.

Ez az oldal egyetlen szezon egyetlen ajándékát sem nevezi meg, mert a naptár minden wipe-nál más. A Naptár fül ennek a szezonnak az ajándékait mutatja. Az ajándék ajándék: a naptárból származó tárgyakon nincs **Eladható** címke ([Eladható tárgyak](/wiki/03-Mechanics/Inventory.md#marketable-items)), és nem tehetők fel az [Aukcióra](/wiki/03-Mechanics/Auction.md).

## A wipe {#the-wipe}

Egy új szezon új naptár. A [wipe](/wiki/03-Mechanics/Wipe-Timeline.md)-nál a régi bezár, az új pedig megnyílik a maga 29 ajándékával, és a számlálód újra 0-ról indul. A wipe semmit sem visz el abból, amit átvettél, kivéve azt, amit minden tárgytól elvisz:

- **Törlődik:** az ajándékok, amelyek tárgyak (lőszer, rakéták, anyagok, lemezek, fogyóeszközök), törlődnek a wipe-nál, ha nincsenek a [Tranzittárolódban](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-). A Naptár egy megjegyzéssel jelöli az ilyen ajándékot.
- **Megmarad:** boosterek, kreditek, Thulium, különleges tárgyak, kinézetek, technológiák (egy tervrajz) és konténerek.
- **Az utolsó négy nap (26–29) csak megmaradó ajándékot ad**, így az utolsó hét ajándékát a wipe sosem viszi el.

## Későn érkezők és késői naptárak {#late-joiners-and-late-calendars}

**Ha egy szezon közepén csatlakozol,** az első bejelentkezésed előtti mezők **Csatlakozás előtt** feliratot mutatnak, és nem vehetők át. A ládák és a szezonjutalom mindenkitől ugyanannyi napot kérnek, így a későn érkező pilóta kevesebbet érhet el belőlük. Aki először a 16. napon jelentkezik be, annak 14 mezője marad, tehát legfeljebb 14 napot vehet át: az első két láda és a szezonjutalom 1. lépcsője elérhető, a 2. lépcső (20 nap) nem.

**Egy naptár is indulhat későn.** Általában a szezonnal együtt nyílik. Nyílhat később is, például ha a játék egy szezon közepén kapja meg a Napi jutalmakat. Egy ilyen naptárnak csak a hátralévő napjai vannak, és minden ehhez igazodik: amelyik a 14. napon nyílik, annak 16 mezője van („16-ból”), ládái 4, 8, 12 és 15 átvett napnál jönnek, a szezonjutalom lépcsői pedig 6-nál és 11-nél. Az Irányítópult kártyája megmondja, melyik napon nyílt meg. Ha 10 napnál kevesebb van hátra, a folyó szezon egyáltalán nem kap naptárat (**Ebben a szezonban nincs naptár**), és a következő a wipe-pal indul.

## Kérdések {#questions}

- **Miért nem veheted át az N. napot?** Négy oka lehet. A nap még nem jött el (**Nyílik … múlva**). A nap és a türelmi ideje lejárt (**Lemaradt**). A nap az első bejelentkezésed előtt volt (**Csatlakozás előtt**). Vagy elindult a wipe visszaszámlálása. A naptár nélküli szezonban, vagy kikapcsolt naptárnál nincs mit átvenni.
- **Követi az időzónámat?** Nem. A nap egy UTC-nap. Csak a megjelenített óraidők vannak átváltva az időzónádra ([A nap](#the-day)).
- **Mi van, ha leállt a szerver?** A 6 óra türelmi idő fedez egy rövid kiesést éjfél körül. Hosszabbnál egy adminisztrátor tovább nyitva tarthat egy napot mindenki számára. Annak a mezője ekkor **Tegnap** állapotban látszik, saját visszaszámlálóval.
- **Átvehetek két napot egyszerre?** Csak amíg két mező nyitva van, egy UTC-éjfél utáni 6 órában: a tegnapi és a mai, mindegyik egy-egy nyomással. Egy mezőt nem lehet kétszer, sem előre átvenni.
- **Minden nap be kell jelentkeznem?** Nem. Nincs sorozat: egy kihagyott nap az aznapi ajándékba kerül, a ládák és a szezonjutalom pedig csak azt számolják, hány napot vettél át.
- **Változtat valamit a Prémium?** Nem. A Prémium nem ad extra mezőket és jobb ajándékokat, és a naptár nem ad Prémium napokat.
- **Kell hozzá klán?** Nem. A naptár ugyanazt a napot használja, mint a klánok napi vonala, de csak a tiéd.
- **Van szintkorlát?** Nem. Minden pilóta átvehet, az 1. szinttől.
- **Mi történik a wipe-nál?** Új naptárat kapsz, és újra 0 naptól kezded. Az ajándékok, amelyek tárgyak, törlődnek, ha nincsenek a Tranzittárolóban; a többi megmarad ([A wipe](#the-wipe)).

## Jó tudni {#good-to-know}

- Az ajándékokat, a számokat és a türelmi időt a játékszerver állítja, és egy frissítéssel változhatnak; a Naptár fül mindig az érvényeseket mutatja.
- A Napi jutalmak előtti játékszervernek nincs naptára, és a kártya meg a fül rejtve marad. Az adminisztrátor ki is kapcsolhatja a naptárat; amit átvettél, átvett marad.
- Minden új naptár a wipe előtt elkészül, hogy a játék adminisztrátorai megnézhessék az indulás előtt, és kicserélhessenek egy hibás ajándékot.
