<!-- wiki-i18n source: aaaba3fffe8e8a67 -->
<!-- wiki-i18n title: Hangár -->
# A hangár repülés közben {#the-hangar-in-flight}

A hajód cseréjéhez nem kell visszatérned a bázisra. Biztonságos zónán belülről megnyithatod a **hangár** ablakot (a bal felső eszköztár raktár ikonú gombja), és megváltoztathatod, mi van felszerelve, átválthatsz a másik konfigurációra, vagy repülhetsz egy másik hajóval, amely a tiéd, a játék elhagyása nélkül. Az ablak az állomás hangár oldala, ugyanazokkal a foglalatokkal, értékekkel és leltárral, egy ablakban a játék fölött. A tárgyak illeszkedéséről lásd: [Leltár és felszerelés](/wiki/03-Mechanics/Inventory.md).

![The Hangar window in flight, opened at the station on its Drones view: the drones, the list of drone formations and the inventory](../../img/wiki-img/shots/hangar-window.jpg)

## Mikor nyitott {#when-it-is-open}

Egy módosítás csak akkor engedélyezett, amíg mindez igaz:

- **Biztonságos zóna véd.** Minden állomásnak és portálnak védőgyűrűje van (lásd: [Harc](/wiki/03-Mechanics/Combat.md)). Ezen belül akkor vagy védett, ha 5 másodperc telt el azóta, hogy eltaláltak, és 15 azóta, hogy lőttél.
- **Harcon kívül voltál** még néhány másodpercig: alapértelmezetten **10**. Ez akkor számít, ha azonnal védetten érkezel, egy portálon át, harccal a hátad mögött.
- Nem vagy álcázva, nem vagy a saját EMP-d ablakában, és nem vagy a [feketelyuk](/wiki/03-Mechanics/Black-Hole.md) közelében, és nincs a levegőben egyetlen saját rakétád sem.

A folyamatban lévő javítások nem akadályoznak. Bárhol máshol a hangár ablak még megnyílik, de csak olvasható. Egy borostyánsárga sáv megmondja, miért, és visszaszámolja a másodperceket, ha várakozásról van szó („Az imént még harcban voltál. Várj 6 másodpercet a hajód módosításához.”). A szerver is érvényesíti, így a harcmezőn semmi sem módosíthat hajót.

## Mit módosíthatsz {#what-you-can-change}

- **Bármit felszerelhetsz és leszerelhetsz**, mindenféle foglalatban: lézerek, generátorok (pajzsok, hajtóművek, adaptív magok), extrák, képességfoglalatok és drónfoglalatok, és a beléjük szerelt erősítők, cellák és fúvókák. Húzd a tárgyakat a foglalatokra, vagy kattints rájuk, pontosan úgy, mint az állomáson. A hajód azonnal követi: az értékek, a lézerek, a képességek és a gyorssáv.
- **Bármelyik konfiguráció.** Előkészítheted a Konfig 2-t, miközben a Konfig 1-gyel repülsz, aztán átválthatsz a **Konfigváltás** billentyűvel. A hangár **Repülés: Konfig** gombja ugyanezt a váltást végzi.
- **Bármelyik hajó.** Állíts be egy másik hajót aktívnak, és onnan repülsz vele, ahol vagy. A hajód modellje megváltozik a közelben lévők előtt.
- **Egy új pajzs, hajtómű vagy adaptív mag üresen indul**, mint az állomáson: a konfigurációjának pajzstöltése üres, amíg újra nem töltődik.
- **Drónformációk.** A Drónok nézet a drónjaid alatt felsorolja a formációkat, amelyek a tieid. Nem kell őket felszerelni: repülés közben húzol egyet a gyorssáv Formációk listájából egy helyre, és a hely kattintása vagy billentyűje viseli, biztonságos zónában várakozás nélkül ([Drónformációk](/wiki/03-Mechanics/Formations.md)).
- **Extrák.** A négy átlagos hajónak, a Protosnak, a Kitefinnek, az Ostirionnak és a Nomadnak (azoknak, amelyekkel kezdesz vagy amelyeket megveszel) konfigurációnként 2 extrafoglalata van; a négy hajónak, amelyet a Gyártásban készítesz, a Paragonnak, az Ironcladnek, a Wraithnek és a Stormnak, 3. A Skylabod Extra Slots CPU-i 3, 5 vagy 7 foglalatot adnak még hozzá: 5, 7 vagy 9 az átlagos hajóknál és 6, 8 vagy 10 a gyártottaknál ([Extrák](/wiki/06-Items/Extras.md#extra-slots-cpus)). A 0.4.10-zel egy átlagos hajó harmadik extráját leszerelték, és a leltáradba került: semmi sem törlődött, és egy csevegőüzenetet kaptál.

## Hajócsere {#changing-ship}

A hajónak, amelyre váltasz, **ugyanaz a hajóteste és ugyanazok a pajzsai** vannak, **mint amikor** utoljára repültél vele, pontosan úgy, mintha elindítottad volna. A gyűrű nem javít, így a hajócsere sosem gyógyít: a hajó, amelyet elhagysz, megtartja a sérülését, és azzal tér vissza. Egy megsemmisült hajóval nem repülhetsz, amíg újra nem éleszted; ez ingyen van, és az újraéledéshez hasonlóan legfeljebb 10 000 hajótesttel és pajzs nélkül hozza vissza.

Ami a tiéd, a tiéd marad: a lőszered, a rakétáid és az időzítőjük, a képességeid töltődései, a boosterid, az XP-d és a Slave Drone-jaid. Ami a hajóhoz tartozott, véget ér: egy futó Shield Surge vagy Afterburner, a javítások, a célzásod, a támadásod és az irány, amelyen repültél. A felszerelések azon a hajón maradnak, amelyre fel vannak szerelve.

## Más eszközökből érkező kérések {#requests-from-other-tools}

A hangár a szerveren is csak biztonságos zónából változik: egy tárgy felszerelése, leszerelése, törlése, egy hajó újraélesztése vagy az aktív hajó beállítása repülés közben azt a választ kapja: „A hajódat csak biztonságos zónában módosíthatod.” A konfigurációváltás a kivétel, és bárhol működik (5 másodpercenként egyszer).
