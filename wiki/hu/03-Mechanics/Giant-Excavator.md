<!-- wiki-i18n source: 5df6b18400b138dc -->
<!-- wiki-i18n title: Óriás kotrógép -->
# Óriás kotrógép {#giant-excavator}

<!-- wiki-search: excavator; giant excavator; pulsar; mining; fuel; excavator fuel; control panel; overheat; radiation; slumbering void; voids; wave; ds-1; ds-2; ds-3; kotrógép; óriás kotrógép; pulzár; üzemanyag; vezérlőpult; túlmelegedés; sugárzás; hullám -->

A szezon 11. napjától egy **pulzár** ragyog a `DS-1`, a `DS-2` és a `DS-3` veszélyes szektorban, és mellette egy **óriás kotrógép** áll. A kotrógép **Thuliumot és ritka érceket** bányászik ki a pulzárból, és ehhez [Dark Mattert](/wiki/03-Mechanics/Dark-Matter.md) éget el. Bárki feltöltheti, kiválaszthatja, mit bányásszon, és elindíthatja, és amit kiad, az körülötte hever ládákban, amelyeket bárki felvehet. Egy menet azonban hangos: az egész világ értesül, amikor elindul, **Slumbering Voidok** jönnek érte hullámokban, és a túl sokáig hajtott kotrógép túlmelegszik, és besugározza az egész környéket. Ez az oldal elmondja, hogyan zajlik egy menet, mit ad, és hogyan élheted túl. A szektorok itt vannak: [Veszélyes szektorok](/wiki/01-General/Danger-Sectors.md); a Voidok itt: [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).

## Dióhéjban {#at-a-glance}

<!-- excavator-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Hol**: Egy pulzár egy óriás kotrógéppel a következő szektorok mindegyikében: `DS-1`, `DS-2` és `DS-3`, minden világban
- **Megjelenik**: A szezon 11. napjától a wipe-ig
- **Üzemanyag**: Dark Matter. Egy 10 perc ideig ég; a tartály 3 egységet fogad be, ez 30 perc bányászat. Bárki hozzáadhat egyet-egyet a saját rakományából
- **Vezérlőpult**: Az ablak a kotrógéptől 600 egységen belül működik, a felirata 1 400 egységtől látszik. Bárki tankolhat, választhat és indíthat; a választás zárolva van, amíg fut
- **Ládák**: 20 mp időnként egy láda, a kotrógéptől 450–900 egységre, attól a pillanattól szabad mindenkinek, hogy lehullik. 5 perc ideig hever, és egy térképen egyszerre legfeljebb 24 fekszik
- **Hő**: 30 perc bányászat, annyi menetben, amennyi kell, és a kotrógép 1 óra ideig túlmelegszik. A hő megmarad a menetek között, és a pihenő után eltűnik
- **Sugárzás**: Amíg túlmelegedett vagy megsemmisült, a kotrógép (1 100 egységen belül) és a pulzárja (1 300 egységen belül) minden bent lévő hajót éget: összes HP-jának 10% részét másodpercenként
- **Hajótest**: 200 000 HP Alphában, 300 000 Betában és 400 000 Gammában. Csak a Slumbering Voidok sebezhetik, és csak ha nincs már pilóta, aki védje
- **Voidok**: 2 Slumbering Void 2 perc időnként, amíg bányászik, az első 1 perc múlva az indítás után; egy térképen legfeljebb 8 él
- **Értesítés**: Az egész világ pilótái értesülnek, amikor egy menet elindul, amikor a kotrógép túlmelegszik, és amikor megsemmisül; a többi a szektora pilótáihoz megy. Ezek rendszersorok: a chat **Rendszer** lapján és a Játéknaplóban jelennek meg, nem a **Globális** vagy a **Helyi** lapon.

<!-- excavator-glance:end -->

## Hogyan zajlik egy menet {#how-a-run-goes}

1. **Keress egyet.** A három pulzáros veszélyes szektor mindegyikében van egy kotrógép, minden világban. Egy felirat, a **Kotrógép**, lebeg fölötte, ha a közelben vagy, a Csillagrendszer-térkép pedig megmutatja annak a szektornak a kotrógépét, amelyben repülsz.
2. **Nyisd meg a vezérlőpultot.** Kattints a feliratra. Az **Óriás kotrógép** ablak addig működik, amíg a hajód a kotrógép vezérlőpultjának hatótávolságán belül van (a *Dióhéjban* lista megadja). Álcázott hajó is használhatja, és a használata nem szünteti meg az álcát.
3. **Tankold fel.** A **Dark Matter hozzáadása** egy Dark Mattert tesz a rakományodból a tartályba. Ezt bárki megteheti. A tartály sosem fogad be többet, mint amennyit a kotrógép el tud égetni a túlmelegedés előtt, így nem megy kárba üzemanyag.
4. **Válaszd ki, mit bányásszon** a listából, majd nyomd meg a **Bányászat indítása** gombot. Legalább egy Dark Matter kell hozzá a tartályban, és egy erőforrás. Az indításig bárki megváltoztathatja a választást; amint fut, az erőforrás zárolva van. Az indításról a világ minden pilótája értesül, a nevedet, a szektort és az erőforrást megnevezve.
5. **Tartsd meg.** Amíg bányászik, néhány másodpercenként egy láda hullik a kotrógép körül, az indítás után nem sokkal pedig megérkeznek az első Slumbering Voidok. Védd a kotrógépet, és szedd fel a ládákat.
6. **Figyeld a hőt.** A Hő sáv telik, amíg a kotrógép bányászik, és sosem ürül, amíg vár. A határán a kotrógép túlmelegszik. Menj el előtte: a játék kétszer figyelmezteti a térképet.
7. **Pihen.** Túlmelegedve vagy megsemmisülve a kotrógép és a pulzárja sugároz, amíg a pihenő le nem telik; utána újra kész, nullára állt hővel és teli hajótesttel.

Az ablak megmutatja még a szektort, a tartályt (minden Dark Matterhez egy cella, az égő részlegesen kirajzolva), hogy mennyi Dark Mattert hordasz, a kotrógép hajótestét, hogy az egyes erőforrások mennyit adnak percenként a világodban, és amíg bányászik, a következő hullámig hátralévő időt és az élő Voidokat. Ha valamit elutasít, az okát pirosban olvasod: túl messze vagy a vezérlőpulttól, nincs Dark Mattered, a tartály tele van, még nincs üzemanyag vagy kiválasztott erőforrás, az erőforrás zárolva van, amíg fut, vagy a kotrógép forró.

| Állapot | Mi ez | Mit tehetsz |
| :--- | :--- | :--- |
| **Kész** | Nincs üzemanyag, vagy van, de nincs elindítva. Az eddigi hő megmarad. | Dark Mattert hozzáadni, választani, indítani. |
| **Bányászik** | Dark Mattert éget és hőt gyűjt; az erőforrás zárolva van. | Még több Dark Mattert hozzáadni a megmaradt helyig, harcolni a Voidokkal, felvenni a ládákat. |
| **Túlmelegedett** | A hő elérte a határát. A tartály kiürül; a már lerakott ládák maradnak. | Semmit. A terület besugárzott: maradj távol. |
| **Megsemmisült** | A Voidok nullára vitték a hajótestet. Az üzemanyag elvész, a hajótest azonnal újra teli. | Semmit. A terület besugárzott: maradj távol. |

Ha az üzemanyag a határ előtt elfogy, a kotrógép **Kész** állapotba tér vissza megmaradt hővel, a megmaradt Voidok pedig egy idő után elmennek, hacsak nem harcolnak.

## Mit bányászik {#what-it-mines}

Egy teli tartály úgy van kiegyensúlyozva, hogy nagyjából annyit adjon, amennyit két-három pilóta keresne fél óra legjobb Thulium-farmolással. A Beta és a Gamma többet ad, ahogy minden kilövésért többet is fizetnek. Menetenként egy erőforrást választasz. Egy láda mindenkinek ugyanaz, a Thulium-láda pedig készpénz, amelyet a felvétel fizet ki, mint az aszteroidák Thuliumát.

<!-- excavator-resources:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Egy teli tartály (3 Dark Matter, 30 perc bányászat) az alábbi mennyiségeket adja, 90 ládában.

| Erőforrás | Alpha | Beta | Gamma | Egy perc, Alphában | Egy láda, Alphában |
| :--- | ---: | ---: | ---: | ---: | ---: |
| [Thulium](/wiki/06-Items/Resources.md#thulium) | 4 821 | 7 714 | 9 643 | 160,7 | 53,6 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | 1 157 | 1 851 | 2 314 | 38,6 | 12,9 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | 514 | 823 | 1 029 | 17,1 | 5,7 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | 320 | 320 | 320 | 10,7 | 3,6 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | 160 | 160 | 160 | 5,3 | 1,8 |

- A Velkonite vagy Orvium menete legfeljebb egy 20. szintű [Skylab](/wiki/03-Mechanics/Skylab.md)-gyűjtő 4 órányi ércét adja (320 Velkonite, 160 Orvium), minden világban: ezek a Skylab ércei, és egy menet sosem gyorsítja a tempóját ennél jobban.
- Egy láda nagyjából az utolsó oszlop mennyiségét tartalmazza, 15% eltéréssel. A Thulium-láda készpénz: a felvétel fizeti ki. Az érclába a tárgyat tartalmazza.

<!-- excavator-resources:end -->

A pilóta saját boosterei úgy működnek, mint bármely rakománynál: a Resource Magnet Booster bónusza megnöveli az ércládát. A ládáknak nincs napi korlátja: az üzemanyag és az óra szabja meg a menetet.

**Mire jó az érc.** Egy láda ércét úgy kapod a rakományodba, mint bármely tárgyat. A Cataclysite-ot és a Quorviumot a Gyártásban és a Kovácsműhelyben használják ([Erőforrások](/wiki/06-Items/Resources.md)). A Skylab kovácsműhelye az ércét csak az Erőforrás-raktárból veszi, amelyet a gyűjtők töltenek, így egy láda Velkonite-ja és Orviumja a [Kutatóközpont](/wiki/03-Mechanics/Research.md#fuel) üzemanyaga, nem a kovácsműhelyé.

## A Slumbering Voidok {#the-slumbering-voids}

Egy menet **Slumbering Voidokat** vonz, az elveszett civilizáció vadászait, amelyek a térkép széléről repülnek be, hogy megvédjék a pulzárt mindenkitől, aki ki akarná üríteni. A kotrógép közelében lévő pilótákra vadásznak, és ha már nincs kire vadászni, a kotrógépre mennek. A Void számai és a fizetése itt vannak: [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).

<!-- excavator-voids:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Hullámok.** 2 Slumbering Void 2 perc időnként; az első 1 perc múlva az indítás után, és egy sem a menet utolsó 1 perc idejében. Egy térképen egyszerre legfeljebb 8 él: az a hullám, amely tele találja a térképet, kimarad.
- **Érkezés.** Egy hullám a térkép szélén jelenik meg, 900 egységre befelé és minden kapugyűrűtől legalább 2 500 egységre, és nagyjából 20 mp alatt repül a kotrógéphez. Az üzenet megnevezi a térkép azon oldalát, ahonnan jön.
- **Vadászat.** A Void a legközelebbi pilótára vadászik, akit 2 500 egységen belül lát, és a kotrógéptől 7 000 egységen belül marad.
- **Ostrom.** Ha 15 mp ideig nincs látható pilóta a kotrógéptől 7 000 egységen belül, a Voidok megtámadják a kotrógépet, és minden lézer a szokásos sebzésének 25% részét okozza. Nullánál a kotrógép megsemmisül: az üzemanyaga elvész, a hajóteste azonnal újra teli, és 1 óra ideig pihen.
- **Távozás.** Amikor egy menet véget ér, a megmaradt Voidok még 90 mp ideig maradnak, és tovább harcolnak, ha harcolnak velük; aztán elmennek.

<!-- excavator-voids:end -->

- **A Void üvegágyú.** A pajzsa nagy, de egy találat 80 %-át elnyeli, így a mögötte lévő hajótest a saját méretének néhányszorosa sebzés után elfogy, pajzsáthatolással pedig sokkal előbb. Két-három jól felszerelt pilóta kitart egy menetet Alphában; a Beta és a Gamma nagyobb csoportot kíván, mint bármely idegen esetében.
- **Az álca nem védi a helyet.** A Voidok nem látják az álcázott hajókat, így az elrejtőző pilóta nem tartja távol őket a kotrógéptől; a kapugyűrűben menedéket kereső pilóta pedig nem érhető el, és az sem számít.
- **Minden Void fizet** az általad okozott sebzés szerint, és ládát ejt ([így fizet egy főellenség kilövése](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). A kilövéseik a PvE rangpontjaidat gyarapítják, mint egy rajhajóé.

## Hő és sugárzás {#heat-and-radiation}

A bányászat másodpercről másodpercre hőt ad hozzá. A hő **halmozódik, és sosem hűl le, amíg a kotrógép vár**: a korán abbahagyott menet rövidebbet hagy a következő pilótának. Amikor eléri a határt, a kotrógép **túlmelegszik**, és amikor a hajótestét nullára viszik, **megsemmisül**; mindkét esetben a kotrógép és a pulzárja sugároz, amíg a pihenő le nem telik.

<!-- excavator-radiation:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

| Kör | Sugár | Összes HP másodpercenként | Egy teli hajó kibírja |
| :--- | ---: | ---: | ---: |
| Az óriás kotrógép | 1 100 | 10% | 10 mp |
| A pulzár | 1 300 | 10% | 10 mp |

- **Az adag.** Egy hajó összes maximális HP-jának (hajótest plusz pajzs) 10% része másodpercenként, így egy teli hajó 10 mp ideig bírja, bármilyen osztályú. A pajzs kapja először, és az elnyelése nem számít.
- **Kit.** Minden hajót a körökben, az álcázottakat is; idegent nem. Elszenvedett sebzésnek számít: a Javítódrón leáll, és a pajzs nem töltődik, mint a feketelyuknál.
- **Jóváírás.** Az elégő pilóta az utolsó ellenségnek íródik jóvá, aki az előző 15 mp alatt eltalálta.
- **Figyelmeztetések.** A térkép a túlmelegedés előtt 1 perc, illetve 15 mp értesül.

<!-- excavator-radiation:end -->

- **A figyelmeztetés.** A túlmelegedés előtt kétszer (az idők a fenti listában vannak) értesül a térkép, a körökben lévő hajó figyelmeztetést lát, és a köröket megrajzolja a Csillagrendszer-térkép és a minitérkép. Amikor sugároznak, a körök pirosak, és a Sugárzás-mérő mutatja az adagot.
- **Távozás.** Minden sorozatgyártású hajó el tud menni a vezérlőpult széléről vagy a legtávolabbi még meglévő ládától, kivéve a lassú Ironclad-et: az a figyelmeztetés alatt távozik, vagy nem távozik. Ne állj ládán, amikor a hő a határra ér.
- **Zsákmány a körökben.** A túlmelegedés előtt lerakott ládák a sugárzásban maradnak: az ott fekvő, amikor az elkezdődik, az adag árán vehető fel.
- **A szerver újraindulása** szünetelteti a menetet: az üzemanyag és a hő úgy tér vissza, ahogy volt, a pihenő az óra szerint telik tovább, és az újraindulás utáni első hullám egy perccel később jön.

## Harc egy menetért {#fighting-over-a-run}

A kotrógépnek **nincs külön gyűrűje**: a világod szokásos szabályai érvényesek, így riválisok jöhetnek, rád lőhetnek, és elvehetik a ládákat (a láda attól a pillanattól szabad mindenkinek, hogy lehullik). A lopás és a lesvetés az esemény része. Néhány dolog, amire számíts:

- **Aki tankol, nem feltétlenül nyer.** Bárki tankolhat, választhat és indíthat; egy rivális megváltoztathatja az erőforrást, mielőtt az Indításra nyomsz. Ellenőrizd a választást, mielőtt megnyomod.
- **Az üzemanyag veszélyben van.** Ha a kotrógép megsemmisül, a tartályában lévő Dark Matter elvész, és senki sem kapja vissza. A legtöbb, amit elveszíthetsz, a teli tartály.
- **Hozz csoportot,** és beszéljétek meg, ki marad a kotrógép közelében és ki szedi a ládákat, és tartsd szemmel a hőt: az utolsó ládákat szedő pilótákat éri utol a sugárzás.
- **A Voidok a kotrógéphez jönnek, nem a ládákhoz.** Egy csoport, amely tartja a kotrógépet, lefoglalja a Voidokat; amelyik elkóborol, az ostromra hagyja.

## Mit tudhat meg a világ {#what-the-world-is-told}

Ezek rendszersorok (a chat **Rendszer** lapján és a Játéknaplóban jelennek meg, nem a **Globális** vagy a **Helyi** lapon). Az első három az egész világhoz megy; az utolsó a kotrógép szektorának pilótáihoz.

- Azon a napon, amikor a 2. esemény elkezdődik: a veszélyes szektorok megváltoztak.
- Egy pilóta **elindít** egy kotrógépet, a szektort, az erőforrást és az üzemanyag perceit megnevezve.
- A kotrógép **túlmelegszik** vagy **megsemmisül**.
- Elfogy az üzemanyag; a kotrógép mindjárt túlmelegszik (kétszer jelzik); a Voidok **hulláma** közeledik, a számával és a térkép azon oldalával, ahonnan jön; nem maradt pilóta, ezért a Voidok megtámadják a kotrógépet.

A vezérlőpult minden műveletének és minden figyelmeztetésnek saját halk hangja van, a hanghatások hangerején.

## Hol olvass tovább {#where-to-read-more}

- [Veszélyes szektorok](/wiki/01-General/Danger-Sectors.md): hol állnak a pulzárok, és mi más új.
- [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md): a Slumbering Void, az Inert Mass és az Unwakened.
- [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md) és [A feketelyuk](/wiki/03-Mechanics/Black-Hole.md): honnan jön az üzemanyag.
- [Erőforrások](/wiki/06-Items/Resources.md): az érc, amelyet a kotrógép ad.
- [Rakományládák](/wiki/03-Mechanics/Cargo.md): ládák, felvétel és a Resource Magnet Booster.
- [Rangok](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points): egy Void PvE-pontjai.
