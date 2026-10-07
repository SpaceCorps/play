<!-- wiki-i18n source: 3d121321d2746bbe -->
<!-- wiki-i18n title: Klánok -->
# Klánok {#clans}

Klán alapítása vagy belépés egy klánba lehetővé teszi, hogy összevond az erőforrásaidat, fejleszd a közös bankot, adókulcsokat állíts be, összehangold magad a frakciótársaiddal, és diplomáciát folytass. A klánnak közös munkája is van: minden nap kap egy **napi vonalat** küldetésekből, amely egy olyan bosszal ér véget, akit csak a klán sebezhet, és az így szerzett pontokból **tartós bónuszokat** vehet minden tagnak. (A játék Klán oldalán a klánt *flottának* hívják, a pontjait és bónuszait flottapontnak és flottabónusznak.)

**Egy percben**

- Minden szezonnapon a klánod kap egy [napi vonalat](#daily-line): négy küldetést sorrendben (idegenek lelövése, egy távolság megtétele, néhány napon rajvezérek legyőzése), majd egy [klánőrzőt](#clan-wardens), egy bosszt, akit te idézel meg, és akit csak a klánod sebezhet.
- Minden befejezett lépés azonnal klánpontot ad: 15, 15, 20, 20 és 30, vagyis egy egész vonal **100 pontot**.
- A Vezér és az Alvezérek a pontokat három [bónuszra](#clan-points-and-boosts) költik, mindegyik tíz szintes: **Sebzés** (legfeljebb +5%), **Thulium** (legfeljebb +10%) és **Kredit** (legfeljebb +10%).
- Az a klán, amely minden vonalat teljesít, a **12. szezonnapon** megvett minden szintet. A pontok és a szintek minden wipe-nál újrakezdődnek.
- Legalább **három tag** kell, aki megtette a részét, és **nagy legénység** az őrző elleni harchoz: a 0.4.13 óta az őrzőnek ötször akkora a törzse, a pajzsa és a lézersebzése, mint volt, ezért azok a legénységek, amelyek korábban nyertek, nagyjából hét pilóta, most veszítenek ([mekkora legénység kell](#how-big-a-crew)). Egy túl kicsi legénység elveszíti a harcot: a klán ilyenkor megtartja a négy küldetés **70 pontját**, de a vonal nem készül el, és nem fizeti ki [a te jutalmadat](#the-reward-for-you).
- Az őrző nagy kasszát fizet, sebzés szerint elosztva, és **minden pilóta, aki a sebzés legalább 5%-át okozta, saját privát ládát kap** a zsákmányból járó részével, amelyet csak ő lát, és csak ő vehet fel ([fizetés és zsákmány](#warden-pay-and-loot)).
- A hajód a meglévő bónuszokat a **Boosterek** ablakban mutatja, egy külön kártyán ([hol látod őket](#the-three-boosts)).
- A vonalhoz és a bónuszokhoz 0.4.10-es vagy újabb verziójú játék kell, a Boosterek ablak kártyájához 0.4.12-es vagy újabb.

![The Boosters window in flight: the Clan boosts card under the timed boosters lists your clan's tag and each boost with its bonus and level](../../img/wiki-img/shots/clan-boosters-window.jpg)
![Buying a level of a clan boost: the sheet shows the level, the bonus the whole fleet gets and the cost in clan points](../../img/wiki-img/shots/clan-boosts.jpg)
![Summoning a Warden for the clan](../../img/wiki-img/shots/clan-warden.jpg)

## Klán fejlődése {#clan-progression}

A klánok az 1. szintről indulnak, és az 5. szintig fejleszthetők. A klán fejlesztéséhez a **Klánbankból** kell kreditet kifizetni. A fejlesztések növelik a taglétszámot és a napi kifizetési korlátot.

| Klánszint | Taglétszám-korlát | Napi kifizetési korlát (tagonként) | Fejlesztés ára (kredit) |
| :---: | :---: | :---: | :--- |
| **1. szint** | 10 | 1 000 000 kredit | — |
| **2. szint** | 25 | 2 000 000 kredit | 10 000 000 kredit |
| **3. szint** | 50 | 3 000 000 kredit | 100 000 000 kredit |
| **4. szint** | 75 | 4 000 000 kredit | 1 000 000 000 kredit |
| **5. szint** | 100 | 5 000 000 kredit | 10 000 000 000 kredit |

---

## Klángazdaság és adózás {#clan-economy-taxation}

A klánok adóalapú pénzügyi rendszerben működnek:

### 1. Napi adózás {#1-daily-taxation}

- **Adókulcs**: a Vezér vagy az Alvezérek **0% és 5%** közötti napi adókulcsot állíthatnak be.
- **Automatikus beszedés**: naponta egyszer (UTC) a szerver automatikusan beszedi az adót az összes klántagtól.
- **Képlet**: az adót minden tag aktuális kreditegyenlegének `ClanTaxRate` része adja.
  - *Példa*: ha 10 000 000 kredited van, és a klánadó 2%, 200 000 kredit vonódik le a számládról, és kerül a Klánbankba.
  - Önkéntes kreditadományok is tehetők, a következő szakaszban lévő korlátig.

### 2. Adományok {#2-donations}

- **Adományozás**: bármelyik tag küldhet kreditet a Klánbankba a Klán oldalról. Az adatlap megmutatja, mennyit küldhetsz még.
- **Adománykorlát**: egy pilóta **24 óra alatt legfeljebb 1 000 000 kreditet** küldhet klánokba, az összes klánt együtt számítva, amelyben a pilóta valaha volt. A klán elhagyása és egy másikhoz csatlakozás nem ad új keretet.
- **Nincs napi nullázás**: a 24 óra csúszik. Minden adomány pontosan 24 órával a megtétele után nem számít többé, és az adatlap megmondja, mikor jár le a legrégebbi, és mennyi tér vissza. A megmaradt keretet meghaladó adományt egészében elutasítják.
- A napi adó nem adomány, és nem használja fel a keretedet.

### 3. Bankkifizetések {#3-bank-payouts}

- **Kifizetési korlátok**: a klán vezetői és tisztjei kreditet oszthatnak ki a Klánbankból egyes tagoknak.
- **Napi korlát**: egy tag egyetlen naptári napon (UTC) legfeljebb `1,000,000 * ClanLevel` kreditet kaphat kifizetésben.

---

## Hierarchia és rangok {#hierarchy-roles}

A klánok szerepalapú rangrendszert használnak a jogosultságok kezelésére:

- **Vezér (3. szerep)**: teljes adminisztratív hozzáférése van, beleértve a fejlesztést, az adók beállítását, a diplomáciát, az előléptetéseket, a kizárást és a klán feloszlatását.
- **Alvezér (2. szerep)**: beállíthatja az adókulcsokat, kreditet fizethet ki, kezelheti a diplomáciát, és előléptetheti vagy lefokozhatja az alacsonyabb rangúakat.
- **Veterán (1. szerep)**: megbízható tag, aki elfogadhatja a klánhoz érkező új jelentkezéseket.
- **Tag (0. szerep)**: hétköznapi játékos, adminisztratív jogosultságok nélkül.

### Jogosultságok táblázata {#permissions-table}

| Művelet | Vezér | Alvezér | Veterán | Tag |
| :--- | :---: | :---: | :---: | :---: |
| **A klán feloszlatása** | ✅ | ❌ | ❌ | ❌ |
| **A klán fejlesztése** | ✅ | ❌ | ❌ | ❌ |
| **Adókulcs beállítása** | ✅ | ✅ | ❌ | ❌ |
| **Kredit kifizetése** | ✅ | ✅ | ❌ | ❌ |
| **Diplomácia kezelése** | ✅ | ✅ | ❌ | ❌ |
| **Klánbónuszok vásárlása** | ✅ | ✅ | ❌ | ❌ |
| **Klánőrző megidézése** | ✅ | ✅ | ❌ | ❌ |
| **Előléptetés / Kizárás** | ✅ | ✅* | ❌ | ❌ |
| **Jelentkezések elfogadása** | ✅ | ✅ | ✅ | ❌ |

*\*Az Alvezérek csak náluk alacsonyabb rangú tagokat léptethetnek elő, fokozhatnak le vagy zárhatnak ki.*

### Amikor a Vezér távozik {#when-the-leader-leaves}

A Vezér nem hagyhat el olyan klánt, amelyben még vannak más tagok: előbb léptess elő egy Alvezért Vezérré (a Vezér Alvezérré lép vissza), vagy lépj ki utolsóként, ami feloszlatja a klánt. Ha a Vezér törli a fiókját (Beállítások › Fiók), a vezetés a legmagasabb rangú tagra száll, holtverseny esetén a legrégebbi tagra; az egyedül lévő Vezér feloszlatja a klánt, a bankkal együtt.

---

## Napi vonal {#daily-line}

Minden klán naponta egy **napi vonalat** kap: öt lépést, amelyeket az egész klán együtt, **sorrendben** teljesít. Az első négy küldetés: annyi idegen lelövése, annyi távolság megtétele, vagy néhány napon rajvezérek legyőzése. Az ötödik egy **klánőrző**, egy boss, akit megidézel és elpusztítasz. Nyisd meg a **Közösség › Klán** oldalt és a **Műveletek** fület, hogy lásd a mai vonalat, a nyitott lépést a sávjával, a saját részedet és a hátralévő időt.

### Az öt lépés {#the-five-steps}

| Lépés | Mi | Klánpont |
| :---: | :--- | ---: |
| 1 | Első küldetés | 15 |
| 2 | Második küldetés | 15 |
| 3 | Harmadik küldetés | 20 |
| 4 | Negyedik küldetés | 20 |
| 5 | A nap klánőrzője | 30 |
| | **Egy befejezett vonal** | **100** |

- Csak a **nyitott lépés számít**. Az a lelövés, amely az 1. lépés nyitott ideje alatt történik, az 1. lépésnek számít, és semmi másnak. Ha az 1. lépés kész, a 2. lépés nulláról nyílik meg. Amit egy lépés célján túl lősz le, azt nem tartjuk meg a következőnek.
- Egy lépés a pontjait **abban a pillanatban fizeti ki, amikor kész**. Az a klán, amely megcsinálja a négy küldetést, aztán nem tud legénységet összehozni az őrzőhöz, vagy elveszíti a harcot, így is megtart **70 pontot**; [a te jutalmad](#the-reward-for-you) csak a kész vonallal jön.
- Mindenki munkája **egy közös számlálóba** megy: a nyitott lépés idegenének lelövései és az összes tagod megtett távolsága összeadódik, így senkinek sem kell egyedül végigvinnie egy lépést.

### A nap {#the-day}

- A klán napja egy **szezonnap**: 24 óra, a szezon kezdetétől számolva ([Wipe-idővonal](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule)). Az új vonal minden nap ugyanabban az időpontban indul, ez nem éjfél UTC (a klán napi adója továbbra is UTC éjfélkor fut). A Műveletek fül visszaszámol az újraindulásig.
- Az a vonal, amely nem készül el, a nap végén **lejár**. A már kész lépések megtartják a pontjaikat, a nyitott lépés haladása elvész, bepótolni nem lehet. A vonalak az 1–29. szezonnapon futnak.
- A klán online pilótái Rendszer-sort kapnak, amikor az új vonal elindul, amikor egy lépés elkészül, és **egy órával az újraindulás előtt**, ha a vonal nincs kész.

### Fokozatok {#difficulty-tiers}

A játék minden nap veszi a klán **öt legmagasabb szintű pilótájának átlagszintjét** (az összeset, ha ötnél kevesebb van), és ebből állapítja meg a nap fokozatát:

| Fokozat | Átlagszint | Őrző |
| :--- | :--- | :---: |
| Újonc | 4 alatt | I |
| Veterán | 4-től 7 alatt | II |
| Elit | 7 vagy több | III |

A fokozat dönti el, hány idegent kér a küldetés, melyik idegent kéri a „nehéz” lépés, és mennyire erős az őrző. **A pontok minden fokozatban ugyanannyi.** Az alacsony szintű új pilóták nem húzzák le a fokozatot: csak az öt legjobb számít.

### Ki számít {#who-counts}

- **A klán összege számít.** A Műveletek fül sávjai az egész klánéi.
- **A te minimumod.** Hogy részt kapj a nap jutalmából, a **nap munkájának 5%-át** kell elvégezned, nagyjából nyolc perc valódi vadászatot. A fül így mutatja: „A mai munkád: 312 / 469 egység”. Egy munkaegység egy másodpercnyi játék: egy lelövés annyit számít, amennyi idő alatt megtalálod és elpusztítod azt az idegent, egy repült szakasz annyit, amennyi idő alatt megteszed. Egy Veterán klánnál egy Seeker nagyjából 12 egységet ér, egy Phantasm 22-t, egy Bulwark 123-at, 1 000 megtett egység nagyjából 5-öt; a minimum 446–480 egység, bármelyik napon és bármelyik fokozatban.
- **Legalább három tagnak** el kell érnie a minimumát, mielőtt egy lépés befejeződhet. Ha egy lépés tele van, de kevesebben érték el, **vár** („a 3. lépés tele van, de még csak 2 tag érte el a minimumát”), és az adott lépés idegenének lelövései továbbra is hozzáadnak azoknak a tagoknak a munkájához, akik lőtték, amíg a harmadik is el nem éri. Három pilótánál kisebb klán nem tud lépést befejezni.
- **Kinek számít egy lelövés.** Annak a pilótának, akinek kifizetik, és a csoporttársainak 4 000 egységen belül, akik az utolsó 15 másodpercben lőttek ([Csoportok](/wiki/03-Mechanics/Groups.md#sharing-kills)). A klán egy lelövést **egyszer** számol, akárhány pilótája volt a csoportban, és a lelövés munkáját egyenlően elosztják köztük. Két klán egy csoportban egyszer-egyszer számolja.
- **Melyik lelövések.** Csak a nyitott lépés idegene: a hétköznapi Seeker, Phantasm, Bulwark vagy Goombah. A rajhajók, a más pilóták és az őrzők segítői nem számítanak ilyen idegennek. Bármelyik világ számít, és erősebb világban egy lelövés többet ér: **1 Alphában, 1,5 Betában, 2 Gammában** ([Világok](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)). A boss-lépés a [rajok](/wiki/05-Swarms/Swarms.md) bossait számolja, egyet minden klánnak, amelynek van pilótája, aki a sebzés legalább 5%-át okozta.
- **Repülés.** Az őrjárat-lépés azt a távolságot számolja, amelyet minden pilóta a védett zónákon kívül repül; öt együtt repülő pilóta ötszörös távolságot ad hozzá.
- **Belépés és kilépés.** Amit megtettél, megmarad, ha kilépsz. A belépő pilóta attól a pillanattól számít.

### A hét vonal {#the-seven-lines}

A vonalak hetes ciklusban követik egymást: a *d* szezonnap vonalának száma 1 + ((*d* − 1) mod 7), így mindegyik hétnaponta tér vissza. A számok **Újonc / Veterán / Elit** klánra vonatkoznak. A két **Swarm Break** vonal rajvezéreket kér, és csak a 4. naptól jön, amikor a [rajok](/wiki/05-Swarms/Swarms.md) megjelennek. Minden szám összesen nagyjából **2,6 óra játékra** készült, öt pilótánál fejenként fél órára (becslés, nem mérés).

| Vonal | Szezonnapok | 1. lépés | 2. lépés | 3. lépés | 4. lépés |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Seeker Sweep | 1, 8, 15, 22, 29 | 150 / 300 / 425 Seeker | 115 000 / 155 000 / 185 000 egység | 21 / 70 / 130 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah |
| Phantasm Purge | 2, 9, 16, 23 | 40 / 140 / 270 Phantasm | 60 / 120 / 170 Seeker | 175 000 / 230 000 / 275 000 egység | 26 Phantasm / 15 Bulwark / 17 Goombah |
| Long Haul | 3, 10, 17, 24 | 290 000 / 385 000 / 460 000 egység | 90 / 180 / 260 Seeker | 26 / 85 / 170 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah |
| Swarm Break I | 4, 11, 18, 25 | 75 / 150 / 220 Seeker | 3 Boss Seeker / 3 Boss Seeker / 2 Pirate Boss | 26 / 85 / 170 Phantasm | 30 Phantasm / 18 Bulwark / 21 Goombah |
| Heavy Iron | 5, 12, 19, 26 | 40 Phantasm / 24 Bulwark / 28 Goombah | 21 / 70 / 130 Phantasm | 175 000 / 230 000 / 275 000 egység | 75 / 150 / 220 Seeker |
| Swarm Break II | 6, 13, 20, 27 | 75 / 150 / 220 Seeker | 21 / 70 / 130 Phantasm | 4 Boss Seeker / 1 Pirate Boss / 3 Pirate Boss | 350 000 / 460 000 / 550 000 egység |
| Grand Round | 7, 14, 21, 28 | 100 / 210 / 300 Seeker | 26 / 85 / 170 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah | 230 000 / 305 000 / 365 000 egység |

### A te jutalmad {#the-reward-for-you}

Ha a vonal kész, vagyis az őrző elpusztult, minden tag kap kifizetést, aki elérte a minimumot és még a klánban van, még akkor is, ha offline. Az a vonal, amely az őrző nélkül ér véget, nem fizet jutalmat, bármit tettek is a négy küldetéssel. A kifizetés fix: a bónuszok, a boosterek és a világ nem változtatják.

| Fokozat | Kredit | Thulium |
| :--- | ---: | ---: |
| Újonc | 5 000 | 20 |
| Veterán | 15 000 | 60 |
| Elit | 22 000 | 90 |

---

## Klánőrzők {#clan-wardens}

A **klánőrző** a napi vonal végén álló boss. Nem egyike a szektorokban kóborló nyilvános [rajoknak](/wiki/05-Swarms/Swarms.md): a klánod **megidézi**, és **csak a klánod sebezheti**. Három őrző váltja egymást, naponta egy: az 1. napon **Brood**, a 2. napon **Siege**, a 3. napon **Wrath**, a 4. napon újra Brood, és így tovább (a 15. nap Wrath-nap). Mindegyik három erősségben létezik, **I, II és III**, amelyet a klán fokozata szab meg. Az őrző külön fajtájú idegen, mint a rajok hajói: nem számít Seekernek, Phantasmnak vagy más idegennek. Az őrző nagyon erős: ötször akkora a törzse, a pajzsa és a lézersebzése, mint a 0.4.13 előtt volt, ezért a lehető legnagyobb legénységnek való harc, amelyet a klánod össze tud hozni ([mekkora legénység kell](#how-big-a-crew)).

| Őrző | Szezonnapok | Szerep | Hogyan harcol |
| :--- | :--- | :--- | :--- |
| **Brood Warden** | 1, 4, 7, 10 … | A kaptár őre: oszd meg a tüzed | Négy kis **Brood Drone** gyógyítja a törzsét, és 8 másodpercenként újabb jön, amíg négynél kevesebb él. Előbb a drónokat lődd, aztán az őrzőt. |
| **Siege Warden** | 2, 5, 8, 11 … | Ostromtörő: maradj mozgásban | Kóborol, és egyenes [Rivet-rakétát](/wiki/06-Items/Rockets.md#the-twelve-rockets) lő arra a pilótára, aki először eltalálta, és magát is javítja. Két **Siege Escort** lézertüzet ad hozzá. Maradj mozgásban, és felváltva legyetek a célpont. |
| **Wrath Warden** | 3, 6, 9, 12 … | Hadúr: győzd le a dühöt | Egy helyben harcol, és magát is javítja. Fél törzs alatt a lézerei **másfélszer erősebben** ütnek. Két **Wrath Guard** lézertüzet ad hozzá. Gyorsan döntsd le, és tartsd fenn a pajzsot. |

### Őrző megidézése {#calling-a-warden}

- **Mikor.** A 4. lépés elkészülte után. Egy klánnak **napi két megidézése** van, egyszerre egy őrző lehet kint, és a napból **legalább 30 percnek** hátra kell lennie.
- **Ki.** A Vezér vagy egy Alvezér.
- **Hogyan.** Repülés közben: a **Megidézés itt** gomb a repülőképernyőn jelenik meg, amint a 4. lépés kész, és megerősítést kér. Légy a védett zónákon kívül, egy vállalat **x-2, x-3 vagy x-4** szektorában (bármelyik vállalatén) a világodban. A Műveletek fül mutatja a nap őrzőjét, a megmaradt megidézéseket és azt, miért szürke a gomb, de az őrzőt a hajóról idézik meg.
- **Hol jelenik meg.** A hajódtól 3 000–4 500 egységre, a világodban: csak az adott világ pilótái érhetik el. A fül **x-2-t ajánl Újonc klánnak, x-3-at Veteránnak és x-4-et Elitnek**. A kiválasztott szektor szokásos [PvP-szabályai](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) továbbra is érvényesek.
- **Bemelegítés.** **90 másodpercig** pajzsos és passzív („töltődik”), és minden online klánpilótát értesítenek, hol. Repülj oda, amíg töltődik: a 90 másodperc után élesítve van. Egy kapszula a repülési képernyőn a biztonságos zóna jelvénye alatt követi: a nevét, a „töltődik” állapotot a hátralévő idővel, majd az „élesítve” állapotot a szektorával és a visszavonulásig hátralévő idővel, a „dühöng” állapotot pedig akkor, amikor egy Wrath Warden a törzse felénél kevesebbel rendelkezik.
- **Csak a klánod.** Más klánok pilótáinak lövéseit figyelmen kívül hagyja, és nem váltanak ki viszontlövést.
- **Hogyan ér véget.** Amikor elpusztítják. **Visszavonul**, ha 40 perce élesedett, ha a nap véget ér, ha a klánod egyik pilótája sem volt 2 percig a térképén repülésben, vagy ha a szerver újraindul (ekkor a megidézést visszakapod). Egy visszavonuló őrző egy megidézésbe kerül, és a következő hívás ugyanaz az őrző teljes erővel.

### Őrző elleni harc {#fighting-a-warden}

- **Az őrző azzal a pilótával harcol, aki először eltalálta**, mint minden boss: hagyd, hogy a legszívósabb hajó kezdje, és használd a [Shield Surge-öt és az Emergency Repairt](/wiki/03-Mechanics/Abilities.md).
- **Vigyél akkora legénységet, amekkorát csak tudsz, x2 lőszerrel** ([Lézerek](/wiki/06-Items/Lasers.md#laser-ammunition)). Azok a legénységek, amelyek a 0.4.13 előtt nyertek, nagyjából hét pilóta, most veszítenek. Az alábbi táblázat számítás és a legjobb eset: még abban is tíz pilóta minden őrző ellen veszít, és a legkisebb nyerni képes legénység x2 lőszerrel 18–26, x1 lőszerrel 28–39 pilótából áll.
- **Brood:** a drónok gyógyítják a törzsét, és az a legénység, amely figyelmen kívül hagyja őket, veszít, még egy nagy is. Először őket lődd, és lődd tovább őket: 8 másodperc múlva új érkezik.
- **Siege:** a rakétái egyenesek és irányítatlanok, így a mozgásban maradó hajó a legtöbbet kikerüli. Maradj mozgásban, és felváltva legyetek a célpont.
- **Wrath:** amint a törzse a fele alá esik, minden sorozat másfélszer akkorát üt, így a harc második fele a veszélyes. Az első felét gyorsan döntsd le, tartsd fenn a pajzsot, és az Emergency Repairt tartogasd a dühre.

### Mekkora legénység kell {#how-big-a-crew}

> [!NOTE]
> A 0.4.13 óta minden őrzőnek és minden segítőjének **ötször akkora** a törzse, a pajzsa, a lézersebzése, az önjavítása és a gyógyítása, mint a 0.4.12-ben volt (a sebesség, a hatótáv és a segítők száma ugyanaz). Ötször tovább tart lebontani, és végig ötször keményebben üt, ezért azok a legénységek, amelyek korábban nyertek, most veszítenek. **A játékban még nem harcoltunk az új őrzők ellen: az alábbi idők számítottak, nem mértek.** A legénység **legjobb esetét** mutatják: a legénység azokban a hajókban és abban a felszerelésben van, amelyekre a fokozat készült, minden pilóta használja a Shield Surge-et és az Emergency Repairt, amint készen állnak, a legénység elsőként az őrző segítőire lő, ha az jobb, az őrző és a segítői mind arra a pilótára lőnek, aki először eltalálta, és senki sem hajt ki. A 0.4.12-ben ugyanez a számítás bizakodóbb volt, mint a játékban magával, szkriptelt pilótákkal lefuttatott harcok, ezért egy valódi harc keményebb lehet a táblázatnál, és egy jó legénység jobban is teljesíthet: vedd útmutatásnak, nem ígéretnek.

A táblázat a legjobb eset; játék közben vidd, akit csak tudsz.

| Legénység | x2 lőszerrel | x1 lőszerrel |
| :--- | :--- | :--- |
| 5 pilóta | minden őrző ellen veszítenek; az őrzőnek törzséből és pajzsából 88–96% megmarad | veszítenek |
| 10 pilóta | minden őrző ellen veszítenek; az őrzőnek törzséből és pajzsából 55–87% megmarad | veszítenek |
| 20 pilóta | csak a Siege Warden I és II ellen nyernek, 8,5–8,6 perc alatt, 7 hajót elvesztve | veszítenek |
| 30 pilóta | minden őrző ellen nyernek 4,5–5,1 perc alatt, 3–11 hajót elvesztve | csak a Siege Warden I és II ellen nyernek, 12,6–12,8 perc alatt, 10 hajót elvesztve |

A számításban a legkisebb legénység, amely x2 lőszerrel nyer, **18–26 pilótából** áll (a legkevesebből a Siege Warden I és II ellen), és közben **9–17** hajót veszít; x1 lőszerrel **28–39** pilótából áll, és 13–27 hajót veszít. Az őrző lézerei az I erősségnél százas nagyságrendet ütnek sorozatonként (240–645), a III erősségnél ezreset (9 225–15 450), és a segítői ehhez hozzáadódnak: a hajó, amellyel harcol, 19–59 másodperc alatt elesik, aztán a következőre fordul, így még egy nyerő legénység is sok hajót veszít.

A táblázat egy olyan legénységre vonatkozik, amely az őrző saját fokozatának felszerelésében van. A gyengébb hajók rosszabbul szerepelnek. A **te** klánod őrzője mindig a **te** fokozatodhoz igazodik, amelyet a klán öt legjobb pilótája határoz meg, ezért vidd őket.

**Az a klán, amely túl kicsi az őrzőjéhez,** nincs kizárva. A négy küldetés **70 pontot** fizet, bármi történik az őrzővel, a pontokból bónuszokat lehet venni, és a klán újra megidézheti az őrzőt, ha maradt még megidézése (naponta kettő van): ha a legénység elesik és távol marad, az őrző visszavonul, ami egy megidézésbe kerül, és a következő hívás teljes erővel hozza vissza. De a vonal nem készül el, így senki nem kapja meg [a te jutalmadat](#the-reward-for-you), és az a klán, amely sosem győzi le az őrzőjét, a 30 bónuszszintet leghamarabb a 18. szezonnapon éri el, nem a 12.-en ([mennyi ideig tart](#how-long-it-takes)).

### Az őrzők számai {#warden-numbers}

Az őrzők számai minden világban ugyanazok (az Alpha-számok), és a fizetésük is. Minden drón, kísérő és őr a második táblázat számaival rendelkezik, és az őrző mellett állnak: a Brood Drone az őrző törzsét gyógyítja, a Siege Escort vagy a Wrath Guard lézerrel lő. Egy sorozat egy hajó összes lézerének lövése egy másodperc alatt, a kijelzett szám 80 és 100%-a között kisorsolva; a félnél kevesebb törzzsel rendelkező Wrath Warden másfélszer keményebben üt. Az őrző és a segítői mind arra a pilótára lőnek, akivel az őrző harcol, így a sorozataik összeadódnak: egy Brood Warden III a négy drónjával akár 21 750-at is rak egy hajóra másodpercenként. A Siege Warden [Rivet-rakétája](/wiki/06-Items/Rockets.md#the-twelve-rockets) nincs kisorsolva: az I. erősségnél legfeljebb **2 500**, a II.-nál **5 000**, a III.-nál **7 500** sebzést okoz, míg egy pilóta Rivetjének sebzése egy legkisebb és egy legnagyobb szám között sorsolódik ki. Egyenesen repül, ezért a mozgásban maradó hajót elvéti.

| Őrző | Törzs | Pajzs | Lézersebzés (másodpercenként egy sorozat) | Sebesség | Lézer hatótávja | Magát javítja (törzs másodpercenként) | Rakéta és másodpercek a lövések között |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| Brood Warden I | 830 000 | 680 000 | 645 | 90 | 600 | – | – |
| Brood Warden II | 1 440 000 | 1 180 000 | 3 885 | 90 | 700 | – | – |
| Brood Warden III | 5 300 000 | 4 350 000 | 15 450 | 90 | 800 | – | – |
| Siege Warden I | 715 000 | 585 000 | 240 | 110 | 600 | 1 075 | Rivet I: 24 |
| Siege Warden II | 1 240 000 | 1 015 000 | 1 455 | 110 | 700 | 1 875 | Rivet II: 12 |
| Siege Warden III | 4 575 000 | 3 725 000 | 9 225 | 110 | 800 | 6 925 | Rivet III: 8 |
| Wrath Warden I | 815 000 | 665 000 | 480 | 90 | 700 | 1 075 | – |
| Wrath Warden II | 1 410 000 | 1 155 000 | 2 910 | 90 | 800 | 1 875 | – |
| Wrath Warden III | 5 200 000 | 4 250 000 | 12 300 | 90 | 900 | 6 925 | – |

| Segítő | Hány | Törzs | Pajzs | Lézersebzés (másodpercenként egy sorozat) | Sebesség | Gyógyítja az őrzőt (törzs másodpercenként) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Brood Drone I | 4 | 3 500 | 2 500 | 60 | 170 | 600 |
| Brood Drone II | 4 | 6 000 | 4 500 | 390 | 170 | 1 050 |
| Brood Drone III | 4 | 20 000 | 17 500 | 1 575 | 170 | 3 850 |
| Siege Escort I | 2 | 21 500 | 17 500 | 30 | 175 | – |
| Siege Escort II | 2 | 37 000 | 30 500 | 225 | 175 | – |
| Siege Escort III | 2 | 137 500 | 112 500 | 1 425 | 175 | – |
| Wrath Guard I | 2 | 24 500 | 20 000 | 90 | 180 | – |
| Wrath Guard II | 2 | 42 500 | 34 500 | 585 | 180 | – |
| Wrath Guard III | 2 | 155 000 | 127 500 | 2 475 | 180 | – |

### Fizetés és zsákmány {#warden-pay-and-loot}

Az őrző tízszer annyit fizet, mint amennyit a fokozat nehéz idegeneiből álló halom fizet: **300 Phantasm** egy I őrzőért, **240 Bulwark** egy II-ért és **160 Goombah** egy III-ért. Ez egyetlen kassza, sebzés szerint osztják szét azok között a pilóták között, akik a sebzés legalább 5%-át okozták, ugyanúgy, mint egy [raj](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays) vezérénél. A [klánbónuszaid](#what-the-boosts-apply-to) a te részedre érvényesek. Az összeg nem nő a kapott sebzéssel, az elégetett lőszerrel vagy az elvesztett hajókkal.

| Az őrző erőssége | Kredit | Thulium | Tapasztalat (XP) | Becsület |
| :--- | ---: | ---: | ---: | ---: |
| I | 900 000 | 3 600 | 90 000 | 1 800 |
| II | 1 200 000 | 6 000 | 192 000 | 2 400 |
| III | 2 400 000 | 12 000 | 480 000 | 3 840 |

**Minden fizetett pilóta saját ládát kap** a roncsnál, a zsákmányból járó részével. A táblázat azt sorolja fel, amit az egész kilövés kisorsol, és az a pilóta, aki a sebzés 20%-át okozta, nagyjából minden mennyiség ötödére dob: a részt véletlenszerűen kerekítik, így az átlag pontos, és egy kis rész is néha kap ritka sort. **Csak te látod a ládádat, és csak te veheted fel**, sem a klánod, sem a csoportod, és **10 percig** áll, a 30 másodperces várakozás nélkül ([privát ládák](/wiki/03-Mechanics/Cargo.md#private-boxes)). Egy [csoportban](/wiki/03-Mechanics/Groups.md#sharing-kills) a tagok egy pilótának számítanak az 5%-hoz, és a részét úgy osztják el, ahogy egy csoportban bármelyik kilövést (a közelben lévő és lövő társak, szint szerint): minden társ, aki részt kap, ennek a résznek privát ládáját kapja. A Játéknapló megmondja a részedet. Az a pilóta, aki 5%-nál kevesebbet okozott, nem kap fizetést, és neki nem rakunk le ládát; a Játéknapló ezt megmondja neki. A zárójelben lévő esély a megadott számú dobás mindegyikére vonatkozik: az (5 × 50%) öt dobás, egyenként 50% eséllyel.

| Őrző | Tárgy | I | II | III |
| :--- | :--- | :---: | :---: | :---: |
| Brood Warden | Ship Fragment | 30–50 | 80–120 | 150–250 |
| Brood Warden | Advanced Plasma | 2 000–4 000 | 6 000–12 000 | – |
| Brood Warden | Daraxium | 10–20 (5 × 50%) | – | – |
| Brood Warden | Nyxite | – | 20–40 (5 × 50%) | – |
| Brood Warden | Ultra Core | – | – | 6 000–10 000 |
| Brood Warden | Quorvium | – | – | 50–100 (60%) |
| Siege Warden | Ship Fragment | 20–40 | 60–100 | 120–200 |
| Siege Warden | Siphon Battery | 2 000–4 000 | 6 000–10 000 | 16 000–24 000 |
| Siege Warden | Kreditért vehető rakéta (egy fajta, véletlenszerűen) | 20–30 | 50–80 | 80–120 |
| Siege Warden | Reinforced Hull Plate | – | 10 (30%) | – |
| Siege Warden | Epikus rakéta (egy fajta, véletlenszerűen) | – | – | 10–20 (50%) |
| Wrath Warden | Ship Fragment | 40–60 | 80–120 | – |
| Wrath Warden | Cataclysite | 30–50 | 50–100 | – |
| Wrath Warden | Reinforced Hull Plate | 10 (25%) | 10 (50%) | 10–20 (70%) |
| Wrath Warden | Power Core | – | 10 (15%) | 10 (35%) |
| Wrath Warden | Quorvium | – | – | 50–100 (70%) |
| Wrath Warden | Ancient Control Unit | – | – | 10 (8%) |

Az őrző a saját nevén számít a lelövési statisztikádban, és PvE-pontot ad a [rangodhoz](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points): **13–35** a vezérért, az őrzőtől és erősségétől függően (a III őrző ér a legtöbbet), és **1–6** minden segítőért, erősebb legénységért többet.

---

## Klánpontok és bónuszok {#clan-points-and-boosts}

A klánpontok a klánéi. Minden lépés, amelyet a klán befejez, növeli az egyenlegét. A **Vezér és az Alvezérek** a **Flottabónuszok** kártyán költik el a Műveletek fülön: három bónusz, egyenként tíz szinttel, és minden tag azonnal megkapja őket. A vásárlás végleges: nincs visszatérítés és nincs újraosztás.

### A három bónusz {#the-three-boosts}

| Bónusz | Szintek | Szintenként | Legmagasabb szint | Mire hat |
| :--- | :---: | :---: | :---: | :--- |
| **Flotta sebzés** | 10 | +0,5% | +5% | Lézersebzés idegenekre és pilótákra |
| **Flotta Thulium** | 10 | +1% | +10% | Thulium lelövésekből és küldetésjutalmakból |
| **Flotta kredit** | 10 | +1% | +10% | Kredit lelövésekből és küldetésjutalmakból |

**Hol látod őket.** Repülés közben a **Boosterek** ablak egy külön **Flottabónuszok** kártyán listázza a hajód bónuszait az időzített boosterek alatt: a klánod címkéje, majd bónuszonként egy sor az értékével és a szintjével (Szint 3/10). Nincs időzítőjük, mert a klánbónusz addig tart, amíg a klánban vagy. Vidd az egeret egy sor fölé, hogy lásd, mire hat. Az a klán, amely még nem vett semmit, ezt mutatja: „A flottádnak még nincs bónusza”, a klán nélküli pilóta pedig nem lát kártyát. Az **Irányítópult** Boosterek kártyája és egy pilóta profilja is listázza őket. A kártya azt mutatja, amit a hajód alkalmaz, ahogy a szerver közli a játékkal, így egy szint, amelyet a tisztek épp most vettek, azonnal megjelenik. A 0.4.12-nél régebbi játék alkalmazza a bónuszokat, de nem mutat kártyát.

### Árak {#boost-prices}

Egy szint ára **22 klánpont plusz 4 minden előző szintért**, és a három bónusznál ugyanannyi: 400 pont egy bónuszért, **1 200 mindhárom**, ez tizenkét befejezett vonal.

| Szint | Ár | Összesen ehhez a bónuszhoz | Flotta sebzés | Flotta Thulium | Flotta kredit |
| :---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 22 | 22 | +0,5% | +1% | +1% |
| 2 | 26 | 48 | +1% | +2% | +2% |
| 3 | 30 | 78 | +1,5% | +3% | +3% |
| 4 | 34 | 112 | +2% | +4% | +4% |
| 5 | 38 | 150 | +2,5% | +5% | +5% |
| 6 | 42 | 192 | +3% | +6% | +6% |
| 7 | 46 | 238 | +3,5% | +7% | +7% |
| 8 | 50 | 288 | +4% | +8% | +8% |
| 9 | 54 | 342 | +4,5% | +9% | +9% |
| 10 | 58 | 400 | +5% | +10% | +10% |

### Mire hatnak a bónuszok {#what-the-boosts-apply-to}

- A **Flotta sebzés** hozzáad a hajód által okozott összes lézersebzéshez: idegenekre, rajhajókra, őrzőkre és más pilótákra. **Nem hat a rakétákra**, semmilyen fajtára.
- A **Flotta Thulium és a Flotta kredit** hozzáad az idegenek lelövéseinek fizetéséhez (a saját lelövéseidhez, a bossból és a csoportos lelövésből járó részedhez) és minden általad átvett küldetés jutalmához, legyen az szint-, állomás- vagy Kihívás-küldetés ([Küldetések](/wiki/03-Mechanics/Quests.md#rewards)). **Nem hatnak** a [Skylab](/wiki/03-Mechanics/Skylab.md#credit-farm-and-thulium-farm) farmjaira, a bankkifizetésekre, a bónuszkódokra és a napi vonal jutalmára.
- **Összeadódnak a többi bónuszoddal** (az olyan boosterek, mint a Laser Damage Booster, az [állandó buffok boltjának](/wiki/03-Mechanics/Wipe-Timeline.md#the-permanent-buff-store) buffjai): a százalékok összeadódnak. A lézererősítők (Ampek) nem tartoznak ide: fix sebzést adnak hozzá, a százalékok pedig az összegre vonatkoznak. Öt pont Flotta sebzés 50 mellett, más forrásból, 55-öt ad, ami 3,3%-kal több sebzés, mint azelőtt.
- **A tört nem vész el.** A bónusz gyakran egy egységnél kevesebbet ad egy lelövéshez: egy Seeker 4 Thuliumának 10%-a 0,4. A játék megjegyzi a törtet, és a következő lelövéseid egységeivel együtt fizeti ki, így tíz Seeker kifizeti a neked járó 4-et. A kezedben lévő tört kijelentkezéskor elvész.
- **Belépés és kilépés.** A pilóta attól a pillanattól kapja a bónuszokat, hogy belép a klánba, és abban a pillanatban veszíti el, hogy kilép, kizárják, vagy a klánt feloszlatják. A klán megtartja a szintjeit.

### Mennyi ideig tart {#how-long-it-takes}

Az a klán, amely minden vonalat teljesít, naponta 100 pontot szerez. Ha a tisztek egyenlően vásárolnak a három bónuszból, **az első vonal után 4 szintje van, a harmadik után 10, az ötödik után 16, és mind a 30 a 12. szezonnapon**. A 15. nap kezdetekor tizennégy vonal már lezárult, így az ilyen klánnak két vonalnyi tartaléka van. Az a nap, amely nem készül el, a kész lépéseket így is kifizeti: az a klán, amely megcsinálja a négy küldetést, de sosem győzi le az őrzőjét, napi 70 pontot szerez, és a 30 szintet leghamarabb a 18. szezonnapon éri el. Az utolsó szint után a vonal tovább fut, és tovább fizeti a te jutalmadat; a pontok tovább adódnak ahhoz, amit a klán ebben a szezonban szerzett, amit a klánpontok súgója mutat a Flottabónuszok kártyán.

### Pontok és a wipe {#clan-points-and-the-wipe}

Minden wipe-nál a klán **pontjai, bónuszszintjei és vonalai újrakezdődnek**, így minden szezon új verseny a teljes bónuszokért. Maga a klán, a tagjai, a bankja és az adója úgy marad, ahogy volt.

---

## Diplomácia {#diplomacy}

A klánok hivatalos diplomáciai kapcsolatokat létesíthetnek más szervezetekkel a célklán rövidítésének megadásával:

- **Szövetség**: hivatalosan szövetséges klánok. A baráti státusz megjelenik a térképen.
- **Megnemtámadási egyezmény (NAP)**: megegyezés az ellenségeskedéstől való tartózkodásról.
- **Háború**: hivatalos hadüzenet. A háborús célpontokat bárhol, büntetés nélkül meg lehet támadni.

---

## Barát hozása {#bringing-a-friend}

Egy barát, aki új a játékban, a személyes meghívókódoddal csatlakozhat, és kezdőcsomagot kap; lásd: [Barátok meghívása](/wiki/03-Mechanics/Invite-Friends.md). A játékban aztán bármelyik pilótához hasonlóan jelentkezhet a klánodba.
