<!-- wiki-i18n source: e186cfbf8fcfa1d0 -->
<!-- wiki-i18n title: Képességek -->
# Aktív hajóképességek {#active-ship-abilities}

A képességek azok a gombok, amelyeket a harc hevében nyomsz meg: egy visszatérő pajzs, egy sebességlöket, hogy hatótávon kívülre kerülj, egy javítás, amikor a hajótestednek már alig van hátra. A hajód **képességfoglalataiba** szerelt **pajzsból, hajtóműből vagy Repair Drone-ból** származnak, és minél jobb az a tárgy, annál jobb a képesség. Arra a pillanatra valók, amikor szükséged van rájuk, nem arra, hogy minden töltődésnél megnyomd őket: mindegyik nagyjából tíz másodpercig tart, aztán másfél-két percet pihen.

Az új pilóta eggyel indul: a kezdőcsomagban lévő **Repair Drone I** már be van szerelve a Protos képességfoglalatába, így az Emergency Repair gombja (`E`) az első perctől ott van. A csomag egy második Repair Drone I-e egy extrafoglalatban van: az magától, lassan javítja a hajótestet, és nem képesség (lásd: [Extrák](/wiki/06-Items/Extras.md#repair-drones)).

![The Afterburner](../../img/wiki-img/shots/afterburner.jpg)
![Emergency Repair: repair drones beam the hull](../../img/wiki-img/shots/emergency-repair.jpg)
![Shield Surge: a bubble of shield around the ship and its drones](../../img/wiki-img/shots/surge.jpg)

## Képességfoglalatok {#ability-slots}

Minden hajónak rögzített számú képességfoglalata van a hangárban:

- **Protos** (kezdő hajó): 1 foglalat
- **Kitefin**: 1 foglalat
- **Ostirion**: 2 foglalat
- **Nomad**: 2 foglalat
- **Paragon**: 3 foglalat
- **Storm**: 3 foglalat
- **Ironclad**: 3 foglalat
- **Wraith**: 3 foglalat

Egy képességfoglalatba **pajzs**, **hajtómű** vagy **Repair Drone** kerül, és mindegyik a saját képességét adja. Húzd a tárgyat a foglalatra. A Konfig 1-nek és a Konfig 2-nek saját foglalatai vannak.

- **A pajzscellák és a fúvókák nem férnek a képességfoglalatba.** Ezek a pajzsok, a hajtóművek és az adaptív magok moduljai.
- **A képességfoglalatban lévő tárgy semmi mást nem ad.** Nem ad pajzskapacitást, töltődést, elnyelést vagy sebességet, és a pajzs okozta lassulás sem terheli a hajót. Ugyanaz a Heavy Shield Core vagy egy generátorfoglalatban ül, hogy minden pillanatban a pajzsát adja, vagy egy képességfoglalatban a Shield Surge-ért. Te döntesz.
- Ha egy cellákat vagy fúvókákat tartó pajzsot vagy hajtóművet képességfoglalatra húzol, a cellák és a fúvókák visszakerülnek a leltáradba.
- A képességfoglalatban lévő Repair Drone Emergency Repairt ad, és magától nem javítja a hajótestet. A lassú drónhoz (**REP**) egy extrafoglalatban lévő Repair Drone kell.

## Több azonos fajtájú modul {#several-modules-of-one-kind}

Egy konfiguráció képességfoglalataiba **több pajzsot, hajtóművet vagy Repair Drone-t** is szerelhetsz. Ez továbbra is egy képesség, egy gomb és egy töltődés, de erősebb:

- **A legalacsonyabb rangú modul szabja meg az alapot.** A rangja adja az erőt és a töltődést. Egy Heavy Shield Core egy Light Shield Core mellett két I. rangú modulként viselkedik: egy jobb második modul a bónuszt hozza, de sosem jobb erőt vagy rövidebb töltődést.
- **Minden további modul az alap 50%-át adja hozzá**, összeadva, nem szorozva. A hajtóművek **hosszabb ideig tartóvá** teszik az Afterburnert: 10 mp, két hajtóművel 15 mp, hárommal 20 mp (a sebességbónusz és a töltődés nem változik). A pajzsok azt érik el, hogy a Shield Surge **többet állítson vissza**, a Repair Drone-ok pedig azt, hogy az Emergency Repair **többet gyógyítson**, ugyanabban a tíz másodpercben: az összeg 100%-a, 150%-a és 200%-a egy, két és három modulnál.
- **A további modulok foglalatokba kerülnek.** Egy három képességfoglalatos hajón lehet három egyfajta, vagy egy-egy mindegyikből, vagy kettő és egy. A Protosnak és a Kitefinnek egyetlen foglalata van, és nem halmozhat; az Ostirionon és a Nomadon lehet két egyfajta.
- Az egyenlő rangok egyszerűen azt a rangot adják. Két azonos rangú modul közül a gyengébb bűvölésű szabja meg az alapot.

## A három képesség {#the-three-abilities}

### Shield Surge (pajzsok), `Q` billentyű {#shield-surge-shields-key-q}

Tíz másodpercig a hajód pajzsa **javul**: a Surge a maximális pajzsod egy részét állítja vissza egyenletesen, a maximumig, soha azon túl. Nem gát, és nem változtatja meg, hogyan oszlanak meg a találatok; pajzsot ad vissza, és ami visszakerült, az marad. Nem áll le, ha eltalálnak (a szokásos újratöltés találat után 15 másodpercet vár; a Surge nem). Egy teli pajzsú hajónak keveset ér, ezért akkor nyomd meg, amikor a pajzs fogy. Az összeg sosem kevesebb a pajzsmag saját kapacitásánál, így egy kevés pajzzsal bíró hajó is valódi javítást kap (a maximumáig).

- Biztonságos zóna védelme alatt és pajzs nélküli hajón nem indítható, hogy egy félrekattintás ne égesse el.
- Az áthatoló rakéták továbbra is részben megkerülik a pajzsokat, mint mindig.

### Afterburner (hajtóművek), `W` billentyű {#afterburner-engines-key-w}

A végső sebességedet megszorozza a rang bónuszával az időtartama alatt. Nem változtatja meg a fordulást, a célzást és a kapott sebzést: az időt távolsággá alakítja. Használd harc elhagyására, egy állomás- vagy portálgyűrű elérésére, vagy egy menekülő célpont utolérésére. Bárhol működik, a biztonságos zónákban is. Több hajtómű hosszabb ideig tartóvá teszi, nem gyorsabbá.

### Emergency Repair (Repair Drone-ok), `E` billentyű {#emergency-repair-repair-drones-key-e}

A **maximális hajótestednek** egy részét gyógyítja **egyenletesen tíz másodperc alatt**, a maximum fölé soha. A találatok nem szakítják meg: vészképesség, és tűz alatt, a feketelyuk sugárzásában, álcázás alatt és EMP-ablakon belül is működik. Akkor ér véget, amikor letelik az idő, vagy a hajód megsemmisül. A pajzsodhoz nem nyúl, nem számít találatnak, és a lassú REP-javítást úgy hagyja, ahogy volt. Teli hajótestnél nem indítható.

## Rangok {#ranks}

Egy képesség ereje a **saját hajód számának egy része** (maximális pajzs, sebesség, maximális hajótest), így a hajóval együtt nő. A rang a tárgyból jön: egy jobb modell jobb képességet ad. Egy bűvölt tárgy hozzáadja a bűvölési bónuszát az erőhöz, legfeljebb 15%-ot. A táblázat egy modulra vonatkozik; a halmozás alatta van.

<!-- abilities:begin -->
<!-- Generated from server/Resources/AbilityConfig.json and the items' stats by scripts/abilities-wiki.sh: don't edit by hand. -->

| Képesség | Rang | Tárgy | Erő (egy modul) | Tartam | Töltődés | Aktív |
| :--- | :---: | :--- | :--- | --: | --: | --: |
| **Shield Surge** | I | Light Shield Core | a maximális pajzsod 30%-át állítja vissza | 10 mp | 120 mp | 8,3% |
| **Shield Surge** | II | Basic Shield Core | a maximális pajzsod 60%-át állítja vissza | 10 mp | 105 mp | 9,5% |
| **Shield Surge** | III | Heavy Shield Core | a maximális pajzsod 100%-át állítja vissza | 10 mp | 90 mp | 11,1% |
| **Afterburner** | I | Engine I | +30% sebesség | 10 mp | 120 mp | 8,3% |
| **Afterburner** | II | Engine II | +45% sebesség | 10 mp | 105 mp | 9,5% |
| **Afterburner** | III | Engine III | +60% sebesség | 10 mp | 90 mp | 11,1% |
| **Emergency Repair** | I | Repair Drone I | a maximális hajótested 20%-át gyógyítja | 10 mp | 120 mp | 8,3% |
| **Emergency Repair** | II | Repair Drone II | a maximális hajótested 25%-át gyógyítja | 10 mp | 105 mp | 9,5% |
| **Emergency Repair** | III | Repair Drone III | a maximális hajótested 32%-át gyógyítja | 10 mp | 90 mp | 11,1% |
| **Emergency Repair** | IV | Repair Drone IV | a maximális hajótested 40%-át gyógyítja | 10 mp | 75 mp | 13,3% |

Egy konfiguráción belül több azonos fajtájú modul esetén a legalacsonyabb rangú szabja meg a fenti erőt és töltődést, minden további pedig ennek 50%-át adja hozzá.

| Azonos fajtájú modulok | Az Afterburner tartama | A Shield Surge ennyit állít vissza | Az Emergency Repair ennyit gyógyít |
| :---: | --: | --: | --: |
| 1 | 10 mp | 100% | 100% |
| 2 | 15 mp | 150% | 150% |
| 3 | 20 mp | 200% | 200% |

<!-- abilities:end -->

A III. rangú pajzsokat és hajtóműveket (a Heavy Shield Core-t és az Engine III-at) nem árulják: a [Gyártásban](/wiki/06-Items/Overview.md#upgrading-modules) készíted el őket egy Basic Shield Core-ból és egy Engine II-ből, Thulium, zsákmány és 3 Dark Matter Plate ([Dark Matter és Dark Matter Plate-ek](/wiki/03-Mechanics/Dark-Matter.md)) felhasználásával. Az Emergency Repairnek van egy negyedik rangja, a Repair Drone IV.

## Töltődés és korlátok {#cooldowns-and-limits}

- **A töltődés a megnyomáskor indul**, és magában foglalja az időtartamot. Így egy 10 másodperces Surge 90 másodperces töltődéssel legfeljebb az idő 11%-ában aktív, és a vége után 80 másodpercig nem érhető el. Több modul nem rövidíti (a legalacsonyabb rangú moduláé); még három hajtóművel is az Afterburner legfeljebb az idő 22%-ában aktív.
- **A töltődés téged illet, nem a tárgyat.** A konfigurációváltás, a tárgycsere, egy másik szektorba ugrás és a kijelentkezés nem nullázza őket. A megsemmisült hajó minden képességgel készen kezdi a következő repülést.
- **Mindegyik képességnek saját töltődése van.** Egy használata nem zárolja a többit.
- **Egy futó hatás megtartja azokat a számokat, amelyekkel elindult.** A tárgy leszerelése vagy a konfigurációváltás nem változtatja meg és nem szakítja meg. Egy ugrás vagy újracsatlakozás sem szakítja meg; a kijelentkezés igen, és a töltődése megmarad.
- A többi pilóta látja a képességeid időzítőit a térképen, mint mindig: egy elhasznált Surge azt mondja nekik, hogy a következő percek nyitva állnak előttük.

## Billentyűk és gombok {#keys-and-buttons}

`Q` Shield Surge, `W` Afterburner, `E` Emergency Repair (mind átállítható a beállításokban). Mindegyik gomb csak akkor jelenik meg a gyorssáv mellett, ha a konfigurációdban megvan az a képesség, így egy új pilóta `E` gombja az első perctől ott van. Az ikonja körüli gyűrű megmutatja, hol tart a képesség: teljes a képesség színében, amikor kész, fogy a hátralévő másodpercekkel, amíg fut (az Emergency Repair is, most, hogy tíz másodperc alatt gyógyít), és újra telik, amíg töltődik, közepén a hátralévő másodpercekkel. Több modul halmozása a jelét (`x2`, `x3`) viseli a gomb sarkában. Az Emergency Repair gombja halvány, amíg a hajótested teli van, a Shield Surge gombja pedig a pajzs nélküli hajón. Vidd az egeret egy gomb fölé a hajódon érvényes számokért, a halmozást beszámítva (például *Afterburner II x2: +45% sebesség 15 mp-ig*), és, amíg egy Surge vagy egy javítás fut, azért, hogy másodpercenként mennyit ad, és mennyi van még hátra.

## A hangárban {#in-the-hangar}

Húzz egy pajzsot, egy hajtóművet vagy egy Repair Drone-t egy képességfoglalatra, vagy kattints rá jobb gombbal a leltáradban, hogy az első szabadba kerüljön. Egy második és egy harmadik ugyanabból a fajtából a következő szabad foglalatokba kerül, és halmozódik. Minden kitöltött foglalat alatt ott a képesség neve és rangja, a halmozás jele és az összes moduljának együttes értékei (*Afterburner II x2*, *x2 · 15 mp*; egy Wraithen lévő Repair Drone II-nél *+81 000 hajótest*), és a foglalat fölé víve látszik, mennyit ér a hajódon, a halmozást beszámítva, és hogy a halmozás melyik modulja szabja meg a rangot. Egy fajta minden modulja ugyanazt a képességet mutatja, mert egyek. A tárgy fölé víve bárhol máshol megjelenik a képesség a saját hajód arányaival, és egy mondat arról, mit ad egy további modul.

## Amit mindenki lát {#what-everyone-sees}

A Shield Surge egy buborék a hajó körül, amíg fut, amely az utolsó két másodpercében vibrál, és a végén bezárul. A pajzssávok (a tiéd a Hajó ablakban, a célpontodé a Célpontablakban) egyszerűen telnek, ahogy a Surge pajzsot ad vissza, és a sáv könnyedén pulzál, amíg van hely a visszaadott pajzsnak. Az Afterburner forróbban égeti a hajtóműveket, amíg fut, 10, 15 vagy 20 másodpercig, és gyűrűt küld ki a hajóból, amikor elindul, halmozásnál szélesebbet. Az Emergency Repair zöld impulzust küld ki, amikor elindul, aztán a tíz másodperce alatt puha zöld fénybe burkolja a hajótestet, amelyről néhány plusz jel száll fel, a másodpercenként gyógyított hajótestpontokat a saját hajód fölött lebegteti, és egy utolsó villanással ér véget. Amíg fut, kis javítódrónok keringenek a hajó körül, és javítják: egy a Repair Drone I-hez, kettő a II-höz, három a III-hoz vagy a IV-hez, és eggyel több minden további Repair Drone-hoz egy halmozásban (háromnál sosem több). Elhagyják a hajótestet, puha zöld sugarakat irányítanak a lemezeire, a II. rangtól impulzusokat küldenek a sugarak mentén, és visszarepülnek dokkolni, amikor letelt a tíz másodperc; a Shield Surge buborékján belül legfeljebb két kék drón van. A térképen minden pilóta látja mindhárom képességet, a drónokat is (kisebbek egy másik pilóta hajóján, és kevesebb az alacsonyabb grafikai beállításokon, ahol az Alacsony sugarakat és izzást mutat drónmodellek nélkül, és a sugár a drón minden rangjával egy kicsit szélesebb), így egy elhasznált Surge jel az ellenségnek éppúgy, mint neked. A drónok három halk hangot adnak ki maguktól, jóval a javítás csengőhangja alatt: egy puha pittyenést, amikor elhagyják a hajótestet, egyet, amikor dokkolnak, és egy halvány hangot a sugaraik alatt, amíg dolgoznak (a Surge drónjaié egy kicsit magasabb); a képernyődön lévő hajókról hallod őket, egyszerre legfeljebb néhányat, és a Hangeffektek hangereje halkítja őket. A *Kevesebb mozgás* bekapcsolva a ragyogás egyenletes marad, a plusz jelek kimaradnak, az utolsó villanás elhalványulás, a drónok pedig a hajó mellett parkolva maradnak egyenletes sugárral (a hangok megmaradnak). Az extrafoglalatban lévő Repair Drone (REP) is megrajzolja a drónjait, amíg a hajótestet javítja: egyet a Repair Drone I, kettőt a II, hármat a III vagy IV esetén, amelyek körbeszállják a hajót és sugárral érik, és a térképen minden pilóta látja őket. Visszarepülnek és dokkolnak, amikor a javítás véget ér.

## Mi változott {#what-changed}

A 0.4.3-as frissítés előtt a képességfoglalatok pajzscellákat (Pajzsregeneráció) és fúvókákat (Gyorsítás) fogadtak. A képességfoglalatokban lévő pajzscellák és fúvókák visszakerültek a leltáradba, amikor a játék frissült, és megtartod őket: továbbra is a pajzsok, a hajtóművek és az adaptív magok moduljai. Azóta a Shield Surge nem extra pajzsréteget ad, hanem tíz másodperc alatt javítja a pajzsodat, az Emergency Repair tíz másodperc alatt gyógyít, nem egyszerre, és egy fajtából több modult is felszerelhetsz hosszabb Afterburnerért, nagyobb Shield Surge-ért vagy nagyobb javításért.
