<!-- wiki-i18n source: 46436d9c65bc6c7e -->
<!-- wiki-i18n title: Extrák -->
# Extrák {#extras}

Az extrák a hajó **extrafoglalataiban** lévő kütyük (minden hajón három van, konfigurációnként). A gyorssáv Extrák menüjéből vagy egy általad hozzájuk rendelt gyorssáv-helyről kapcsolhatod be őket. Csak abban a konfigurációban működnek, amellyel repülsz: ha a másik konfigurációba szerelsz fel egyet, az megvárja, amíg váltasz.

| Extra | Mit csinál | Használatok | Ár |
| :---- | :----------- | :--- | :---- |
| **Repair Drone I–IV** | Javítja a hajótestedet: másodpercenként a maximum 1,5%-át, 2,25%-át, 3,5%-át, illetve 5%-át | korlátlan | 5 000 / 15 000 / 35 000 kredit, 2 000 Thulium |
| **Cloaking CPU S** | Elrejti a hajódat | 10 | 5 000 Thulium |
| **Cloaking CPU M** | Elrejti a hajódat | 25 | 11 250 Thulium |
| **Cloaking CPU L** | Elrejti a hajódat | 50 | 20 000 Thulium |
| **EMP Charge** | 3 másodpercig senki sem vehet célba, minden rád irányuló célzás megszakad, és a közeledben minden álcázás véget ér | 1 | 500 Thulium |

A Cloaking CPU-kat és az EMP Charge-ot csak a Boltban árulják. Nem vonhatók össze, és semmi sem adja őket ingyen.

## Repair Drone-ok {#repair-drones}

Kapcsolj be egy Repair Drone-t (REP), és az javítja a hajótestet, amíg tele nem lesz. Csak akkor indul el, ha 10 másodperce nem ért találat, és minden találat kikapcsolja. Ha többet is felszereltél, a legjobb működik. A javítási ütemek a [Harc](/wiki/03-Mechanics/Combat.md) oldalon vannak.

## Cloaking CPU {#cloaking-cpu}

Az álcázáshoz nyomd meg a CLK foglalatot. **Egy megnyomás egy használat**, bármelyik csomagról legyen szó, a hátralévő használatokat pedig a foglalaton és a hangárban látod. Az álcázásnak **nincs időkorlátja**: addig marad bekapcsolva, amíg ki nem kapcsolod, vagy valami meg nem szakítja.

- **Ki nem lát téged.** Más vállalatok pilótái és az idegenek egyáltalán nem látják a hajódat: nincs rajta a képernyőjükön vagy a célpontlistájukon, és senki sem veheti célba. Más vállalatok vállalati pilótái szintén figyelmen kívül hagyják.
- **A radarpont.** A térképen minden más pilóta – a saját vállalatodat kivéve – egy egyszerű **piros pontot** lát a minitérképen ott, ahol vagy, így tudják, hogy a közelben valaki álcázva van. A pontnak nincs neve, hajója, vállalata vagy azonosítója, nem lehet rákattintani, és nem vehető célba; ha fölé viszed az egeret, csak ennyit ír: „Itt valami álcázva van”. Kerek, és egy gyűrűben áll (a minitérképen a hajók négyzetek); a gyűrű lassan lélegzik, vagy mozdulatlan, ha bekapcsoltad a Kevesebb mozgás beállítást. A szerver körülbelül másodpercenként kétszer frissíti, a játékod pedig simán mozgatja közben. Azt mutatja, hogy valaki ott van, és hol, de azt nem, hogy ki: az a pilóta, aki látta, hogy álcázol, követheti a pontot, és egy rá irányított **rakétarobbanás** így is megtalál.
- **Ki láthat.** A saját hajódat halványan, körvonallal látod. A saját vállalatod pilótái sápadt szellemként látnak; a más vállalatba tartozó klántársak nem, mert a klán bárkit felvesz, aki jelentkezik. A szellemet senki sem veheti célba, a saját vállalatod sem.
- **Nem álcázhatsz** biztonságos zónában, amíg a CPU tölt, és találat vagy lövés után **10 másodpercen** belül.
- **Mi szünteti meg.** Ha újra megnyomod a foglalatot; az első sortüzed vagy rakétád (becsapódik, és meglátnak); ha biztonságos zónába lépsz; ha a CPU kikerül abból a konfigurációból, amellyel repülsz; az **EMP, amely 1 500 egységen belül sül el** tőled, bárki lőtte is ki (a saját vállalatodé is, de a csoporttársadé nem); és a rád találó rakéta területi robbanása. Az idő nem, a rakomány felvétele nem (a felvett doboz mindenki számára eltűnik, így mindenki megtudja, hogy valami elérhető közelségben járt arról a helyről, de azt nem, hogy ki), a képességek nem, a feketelyuk sugárzása pedig sebzi az álcázott hajót, de nem szünteti meg az álcázását. A kijelentkezés vagy a megsemmisülés megszünteti, mert a hajó, amelyet senki sem repül, nincs álcázva.
- **Töltődés.** Az álcázás végét követően, bárhogy ért is véget, a CPU **60 másodpercig** tölt. A töltődés a tiéd, nem a hajóé: akkor is folytatódik, ha portálon át ugrasz, kijelentkezel vagy megsemmisülsz. Minden megnyomás így is egy használatot visz el.
- Az **idegenek**, amelyek utánad jöttek, elvesztenek. A kilövési foglalásaid feloldódnak, amikor álcázol.
- **Rakéták.** Irányított rakétával senki sem foghat be téged, az egyenes, egy célpontú rakéta pedig átrepül rajtad. A **területi robbanás** viszont továbbra is megsebzi a hatókörébe eső hajót, és megszünteti az álcázását, és azok a pilóták, akik látják a hajó helyét, látni fogják a hajót, mielőtt a sebzésszám megjelenik. A rakéta kilövése lövésnek számít: a sortűzhöz hasonlóan megszünteti a saját álcázásodat (a CPU ekkor a fenti 60 másodpercig tölt), és álcázva voltál vagy sem, a kilövés után 10 másodpercig nem álcázhatsz.
- A **feketelyuk** az álcázott hajót is elnyeli, mint bármelyiket, és a térkép tudomást szerez róla.
- **Mit látsz.** A hajód átlátszóvá válik, lila szaggatott körvonallal, a képernyő tetején pedig egy címke ezt írja: „Álcázva”, a hátralévő használatokkal (másodperc nélkül: nincs időzítő). A CLK foglalat a hátralévő használatokat mutatja; amíg álcázva vagy, lilán világít, és BE felirat látszik rajta, amikor pedig az álcázás véget ér, bárhogy is, elsötétül, és számolja a 60 másodpercnyi töltődést. Ha a szerver elutasít egy megnyomást (töltődés, biztonságos zóna, az elmúlt 10 másodpercben ért találat vagy leadott lövés), a foglalat pirosan felvillan, és egy üzenet megmondja, miért. A szövetséges halvány szellemként jelenik meg, a neve előtt egy „álcázva” felirattal, az a pilóta pedig, aki a közeledben álcáz, hullámzás kíséretében eltűnik. A használathoz húzd a CLK-t a gyorssáv Extrák menüjéből egy helyre, akárcsak a REP-et.
- A **használatok** a CPU-val együtt mentődnek. A kijelentkezés, a megsemmisülés vagy a játék újraindítása nem ad vissza egyet sem, és a megszakított aktiválás is elfogy. Amikor egy csomag utolsó használata is elfogy, a csomag elhasználódik, és a foglalatát a leltáradban lévő, ugyanilyen CPU egy tartaléka tölti újra, ha van ilyen.
- Egy konfigurációban **több CPU** nem adódik össze. Először a legkevesebb hátralévő használatú CPU fogy.

Az S, M és L ugyanúgy viselkedik: a nagyobb csomagok csak használatonként olcsóbbak (500, 450, illetve 400 Thulium).

## EMP Charge {#emp-charge}

Harc közben nyomd meg az EMP foglalatot. **3 másodpercig** senki sem vehet célba, és **mindenki, aki célba vett, azonnal elveszti a célzást**, bárhol legyen is: pilóták, idegenek és vállalati pilóták. Az a pilóta, akinek megszakad a célzása, ezt az üzenetet kapja: „Célzás elveszett: a célpont EMP-t használt”. Aki a 3 másodperc alatt próbál célba venni, azt elutasítja a játék.

- **Nem sebezhetetlenség.** Azt állítja meg, amihez célzás kell: a lézereket, az irányított rakétákat és az egyenes, egy célpontú rakéta érintését, amely átrepül rajtad. A **területi robbanáshoz** nem kell célzás, ezért ha a hatókörében vagy, így is megsebez, a feketelyuk pedig egyáltalán nem lövés.
- **Cselekedhetsz.** A tüzelés nem szünteti meg. Álcázhatsz (ha az álcázás saját szabályai megengedik), és használhatsz más extrákat.
- **Megszünteti a közeledben lévő álcázásokat.** Minden hajó, amely az impulzus elsülésekor **1 500 egységen** belül álcázva van, azonnal láthatóvá válik, és a CPU-ja elkezdi a 60 másodperces töltődést, bármelyik vállalathoz tartozik is, a tiédhez is; kivétel a saját [csoportod](/wiki/03-Mechanics/Groups.md) hajói: azok megtartják az álcázásukat. A pilóta ezt az üzenetet kapja: „Álcázás megszakadt: a közelben EMP sült el.”, a hajó ugyanazzal a hullámzással jelenik meg újra, mint bármelyik leleplezésnél, és a foglalat elkezdi a töltődést. Magad nem használhatsz EMP-t, amíg álcázva vagy.
- **Nem rejt el semmit.** Mindenki továbbra is lát téged, a 3 másodpercig egy sercegő elektromos burokkal.
- **Nem használhatod**, amíg biztonságos zóna véd, amíg álcázva vagy, és az előző használat után **30 másodpercen** belül. Máshol mindenhol működik, a szezon első napjaiban is (Békeprotokoll): az idegenek ilyenkor is vadásznak.
- Az az idegen, amelyet a 3 másodperc alatt eltalálsz, csak a vége után fordul ellened. A kilövési foglalásaid és az első találat szabályai nem változnak.
- **Mit látsz.** A meghajlított tér hulláma száguld ki a pilótából addig, ameddig az impulzus az álcázásokat megszünteti (1 500 egység), mindenki látja, aki hatótávon belül van, és a 3 másodpercig egy sercegő elektromos burok veszi körül, a saját hajód körül egy gyűrűvel és a képernyő tetején egy címkével, amelyek számolják az időt. Mindenkinek, aki téged jelölt ki, szétesik a célzógyűrűje, egy rövid sercenéssel. Az EMP foglalat a birtokolt töltetek számát mutatja, kéken világít, amíg a burok él, és elsötétül, amíg tölt.
- **Egy töltet, egy használat.** A foglalatot a leltáradból töltik újra, ha több is van nálad. A **30 másodperces** töltődés nem mentődik: a kijelentkezés vagy a portálon át ugrás törli, a következő impulzus pedig egy töltetbe kerül.
