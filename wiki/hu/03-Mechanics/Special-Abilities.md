<!-- wiki-i18n source: 0a2447734a603004 -->
<!-- wiki-i18n title: Különleges képességek -->
# Különleges képességek {#special-abilities}

<!-- wiki-search: special ability; special abilities; ability; abilities; mob; mobs; regenerate; mending; shield burst; hardened plating; plating; enrage; call reinforcements; reinforcements; clones; decoy; flee and return; flee; life drain; nova pulse; nova; rocket barrage; barrage; veil; sow mines; mines; split; fragments; boss steps; ladder; three steps; warning; tell; surprise; warlord; warden; leader; különleges képességek; regenerálás; pajzslöket; megerősített páncél; dühöngés; erősítés hívása; klónok; menekülés és visszatérés; életszívás; nóvaimpulzus; rakétasortűz; fátyol; aknatelepítés -->

Néhány idegen **különleges képességet** hordoz: valamit, amit életében egyszer tesz meg, amikor a hajóteste félig elfogyott. Gyógyulás, pajzslöket, menekülés, segélykérés. Előtte semmi sem látszik, így minden vadászat meglepetéssel végződhet. Ez az oldal azt mondja el, mit tesz az egyes képesség, és hogyan felelhetsz rá. A főellenségek másképp működnek: három lépésben változtatják a harcmodorukat, ahogy a hajótestük fogy, az utolsó szint kis idegenei pedig szilánkokra hullhatnak, ha túl gyorsan semmisítik meg őket.

## Hogyan működik {#how-it-works}

<!-- mob-rules:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **Egyszer.** A képességet hordozó idegen életében egyszer használja: amikor egy harcban a hajóteste (nem a pajzsa) a maximumának 50% része alá esik. Az a találat, amely e vonal fölül semmisíti meg, soha nem hagyja tüzelni, és a harcban nem álló idegen megvárja, míg egy harc elindul.
- **Először figyelmeztetés.** A képesség figyelmeztetéssel kezdődik: egy gyűrű zárul a hajó köré, és egy szó jelenik meg fölötte. Az a képesség, amelynek alább olvasható bejegyzése szerint azonnal elindul, nem ad figyelmeztetést. Az idegent a figyelmeztetés alatt még meg lehet semmisíteni; ekkor nem történik semmi, és a szokásos módon fizet. A könnyű fajták (Seeker és Phantasm) gyorsabbak: a figyelmeztetésük és a hatásuk a szokásos idő 50% részéig tart.
- **Előtte semmi sem látszik.** A képességet hordozó idegen minden részletében olyan, mint bármelyik másik, amíg el nem kezdődik a figyelmeztetése. A játékban semmi sem mondja meg, melyik az, még az [Utazó kalauza](/wiki/03-Mechanics/Travelers-Guide.md) sem.
- **Ki hordozza.** A cégszektorok és a Danger Sectorok idegenjeinek kis része: minél erősebb a szint, annál nagyobb ez a rész, és a rajok vezérei (Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah és Boss Crystalys) nagyobb eséllyel hordoznak ilyet, mint a többiek. A Deep Void, a klánkazamaták és a szólókapuk idegenei sosem hordoznak, és a raj követői, az őrzők hullámai, a Dormant Force és a Tesseract sem.
- **Annyit fizet, amennyit bármelyik idegen.** A képességet használó idegen pontosan úgy fizet, ejt zsákmányt és számít, mint az, amelyik nem használ: a képesség nem ad hozzá semmit a kilövéshez, és időt vesz el belőle. A kilövés annál a pilótánál marad, aki tartotta: amíg az idegen menekül, gyógyul vagy elrejtőzik, a foglalás nem jár le.
- **A hívott hajók és a másolatok nem kilövések.** Azok a hajók, amelyeket egy idegen hív, és azok a másolatok, amelyeket készít, nem fizetnek, nem ejtenek semmit, és egyetlen küldetésnek, statisztikának vagy ranglistának sem számítanak. Egy hívónál legfeljebb 6, egy térképen legfeljebb 24 él, és a térkép saját idegenei továbbra is időben visszatérnek.
- **A térképen mindenki látja.** A térkép pilótái értesülnek, amikor egy képesség elindul: a játék kirajzolja a gyűrűt, a szót és a hatást, és hangot játszik le.

<!-- mob-rules:end -->

## A tizenkét képesség {#the-twelve-abilities}

Egy képesség **figyelmeztetéssel** kezdődik, kivéve, ha a bejegyzése szerint azonnal elindul: egy gyűrű zárul a hajó köré, és egy szó jelenik meg fölötte. Az alábbi idők és számok a nehéz fajtákra vonatkoznak. Ahol egy számnak több értéke van, azok a zárójelben megnevezett szintekre érvényesek, vagyis az idegen neve előtti görög betűre.

<!-- mob-abilities:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

### Regenerálás {#regenerate}

Megáll, és 6 mp alatt visszaállítja a hajótestének és a pajzsának 15% / 20% / 25% / 30% (α / β / γ / δ) részét, közben semmit sem lő. Ha a sebzés együtt eléri a hajótestének és a pajzsának 10% részét, megszakad, és megtartja, amit addig visszaállított.

- **Figyelmeztetés**: 1,5 mp
- **A szó a hajó fölött**: GYÓGYUL
- **Hordozza**: bármelyik idegen
- **Válasz**: Rakétákkal vagy sok hajóval ontsd rá a sebzést, vagy semmisítsd meg a figyelmeztetés alatt.

### Pajzslöket {#shield-burst}

Friss pajzsréteg kerül a pajzsa fölé: a maximális hajótestének 15% / 20% / 30% / 40% (α / β / γ / δ) része. Amíg áll, a találat minden pontját felfogja; megszűnik, ha elfogy, vagy 10 mp múlva.

- **Figyelmeztetés**: 1 mp
- **A szó a hajó fölött**: PAJZS FEL
- **Hordozza**: bármelyik idegen
- **Válasz**: A pajzsot átütő lőszerek és rakéták jobban átmennek rajta. Vagy lőj egy másik idegenre, amíg el nem tűnik.

### Megerősített páncél {#hardened-plating}

7 mp / 8 mp / 10 mp (β / γ / δ) ideig minden találatnak csak 50% részét veszi fel, hajótestet és pajzsot egyaránt: kétszer olyan szívós. Tovább harcol, és a találataid számai szürkévé válnak.

- **Figyelmeztetés**: 1,5 mp
- **A szó a hajó fölött**: PÁNCÉL
- **Hordozza**: a nehéz fajták (Bulwark, Goombah és Crystalys) és a nehéz rajvezérek (Pirate Boss és Boss Phantasm), β szinttől
- **Válasz**: Várd ki, közben üss egy másik idegent, és tartogasd a löketeidet utána.

### Dühöngés {#enrage}

10 mp ideig a sebzésének szorzója ×1,3 / ×1,4 / ×1,5 / ×1,75 (α / β / γ / δ), a sebességének szorzója ×1,25.

- **Figyelmeztetés**: 1 mp
- **A szó a hajó fölött**: DÜHÖNG
- **Hordozza**: bármelyik idegen
- **Válasz**: Tartsd fenn a pajzsodat, mozogj, és maradj a hatótávján kívül.

### Erősítés hívása {#call-reinforcements}

4 / 6 (γ / δ) kisebb idegen érkezik a térkép legközelebbi széléről, 2 hullámban, 3 mp különbséggel. A fajta, amely jön: Phantasm (hívta: Bulwark és Goombah); Bulwark (hívta: Crystalys). Együtt a hajótestének és pajzsának 45% / 60% (γ / δ) része van meg nekik, és a sortüzének 50% részét lövik. Nem fizetnek, nem ejtenek semmit, és semmire sem számítanak, és 45 mp múlva, vagy a hívó megsemmisülésekor távoznak.

- **Figyelmeztetés**: 2 mp
- **A szó a hajó fölött**: HÍVÁS
- **Hordozza**: a nehéz fajták (Bulwark, Goombah és Crystalys) és a nehéz rajvezérek (Boss Phantasm és Boss Goombah), γ szinttől
- **Válasz**: Semmisítsd meg a hívót: a hajói vele mennek. Egy területre ható fegyver letarolja őket.

### Klónok {#clones}

3 (γ / δ) másolata jelenik meg körülötte, a nevével és a kinézetével. Együtt a hajótestének és pajzsának 18% (γ / δ) része van meg nekik; nem lőnek és nem fizetnek, és 15 mp ideig tartanak, vagy amíg a valódit meg nem semmisítik. A valódin vékony gyűrű van, amíg a másolatok kint vannak, és a célablak a másolatot így nevezi: Csali.

- **Figyelmeztetés**: 1 mp
- **A szó a hajó fölött**: KLÓNOZ
- **Hordozza**: bármelyik idegen, γ szinttől
- **Válasz**: Kövesd a valódi gyűrűjét és mozgó hajótestsávját, vagy használj területre ható fegyvert.

### Menekülés és visszatérés {#flee-and-return}

5 mp / 6 mp / 7 mp / 8 mp (α / β / γ / δ) ideig menekül a támadói elől, a sebességének szorzója ×2, aztán az első pilóta ellen fordul, aki eltalálta. Soha nem hagyja el a térképet, és nem lép be biztonságos zónába, végig eltalálható, és a pilóta, aki a kilövését tartotta, megtartja.

- **Figyelmeztetés**: 0,5 mp
- **A szó a hajó fölött**: MENEKÜL
- **Hordozza**: bármelyik idegen
- **Válasz**: Üldözd, vagy rakétákkal találd el, amíg repül.

### Életszívás {#life-drain}

10 mp ideig semmi mást nem lő: másodpercenként egyszer teljes sortűzzel szív le minden hajót a hatótávján belül, amelyet semmi sem kerül el, és az okozott sebzés 75% / 100% / 100% (β / γ / δ) részét meggyógyítja, legfeljebb a hajótestének 20% részéig összesen.

- **Figyelmeztetés**: 1 mp
- **A szó a hajó fölött**: SZÍV
- **Hordozza**: a nehéz fajták (Bulwark, Goombah és Crystalys) és a nehéz rajvezérek (Pirate Boss, Boss Phantasm, Boss Goombah és Boss Crystalys), β szinttől
- **Válasz**: Tegyél egy sziklát vagy falat a vonalba, álcázd magad, vagy hagyd el a hatótávját.

### Nóvaimpulzus {#nova-pulse}

A figyelmeztetés alatt egy gyűrű nő a földön körülötte. Ha a gyűrű megtelt, egyszer eltalál minden benne lévő hajót, a sortüzének 4 / 5 (γ / δ) adagjával. A sugara egységben: 700 / 800 (γ / δ).

- **Figyelmeztetés**: 2,5 mp
- **A szó a hajó fölött**: NÓVA
- **Hordozza**: a nehéz fajták (Bulwark, Goombah és Crystalys) és a nehéz rajvezérek (Pirate Boss, Boss Phantasm és Boss Goombah), γ szinttől
- **Válasz**: Menj ki a gyűrűből, mielőtt megtelik: ez az egyetlen löket, amelyet ki lehet kerülni.

### Rakétasortűz {#rocket-barrage}

3 mp alatt 4 / 6 / 8 (β / γ / δ) [Rivet-rakétát](/wiki/06-Items/Rockets.md#the-twelve-rockets) lő a célpontjára: Rivet I / II / II (β / γ / δ). Egyenesen repülnek, és nem irányítottak.

- **Figyelmeztetés**: 1,5 mp
- **A szó a hajó fölött**: SORTŰZ
- **Hordozza**: a nehéz fajták (Bulwark, Goombah és Crystalys) és a nehéz rajvezérek (Boss Phantasm és Boss Goombah), β szinttől
- **Válasz**: Mozogj: a rakéták egyenesen mennek. Egy szikla az útban megállítja őket.

### Fátyol {#veil}

6 mp / 8 mp (γ / δ) ideig egy hajó, amely 700 egységnél messzebb van tőle, nem tud rá célt zárolni, és a már meglévő zárolás elvész. Közelebb a szokásos módon látszik. Tovább harcol, és egy robbanás még sebzi.

- **Figyelmeztetés**: nincs, azonnal elindul.
- **A szó a hajó fölött**: REJTŐZIK
- **Hordozza**: a nehéz fajták (Bulwark, Goombah és Crystalys) és a nehéz rajvezérek (Pirate Boss, Boss Phantasm, Boss Goombah és Boss Crystalys), γ szinttől
- **Válasz**: Menj be 700 egységen belülre.

### Aknatelepítés {#sow-mines}

4 / 6 / 8 (β / γ / δ) aknát telepít egy 500 egység sugarú gyűrűre a célpontja helye körül. Egy akna leérkezése után 3 mp múlva élesedik, 30 mp ideig tart, és egyszer robban, az első pilótahajó alatt, amely átrepül rajta, az idegen sortüzének 2 / 3 / 3 (β / γ / δ) adagjával. Az akna soha nem árt idegennek.

- **Figyelmeztetés**: 1,5 mp
- **A szó a hajó fölött**: AKNÁZ
- **Hordozza**: a nehéz fajták (Bulwark, Goombah és Crystalys) és a nehéz rajvezérek (Pirate Boss, Boss Phantasm, Boss Goombah és Boss Crystalys), β szinttől
- **Válasz**: Kerüld ki őket: ki vannak rajzolva a földre, és későn élesednek.


<!-- mob-abilities:end -->

## Szétesés {#splitting}

<!-- mob-split:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Az utolsó szint kis idegenei széteshetnek, ha túl gyorsan semmisítik meg őket. Ez a(z) δ szint Seeker, Phantasm, Bulwark, Goombah és Crystalys fajtájához tartozik, és más idegenhez nem, és nem tartozik a fenti képességek közé: egy idegennek lehet mindkettő.

- **Mikor**: egy pilóta az első kapott sebzése után 5 mp belül megsemmisíti. Nem esik szét minden idegen, amely ilyen gyorsan elpusztul.
- **Mi jön ki belőle**: 3 azonos fajtájú és szintű idegen, a méretének 70% része, mindegyik a hajótestének és pajzsának 25% részével és teljes sortűzzel, a megsemmisülése helye körül. Arra a pilótára támadnak, aki megsemmisítette, és 180 mp múlva távoznak.
- **Közönséges idegenek**: mindegyik azt fizeti, amit a fajtája, azt ejti, amit az, és számít a küldetéseknek és a statisztikáknak. Nem hordoznak képességet, és soha nem esnek szét.
- **Korlátok**: egy térképen legfeljebb 60 szilánk él, és nem tartják vissza a térkép saját idegeneit.
- **Mit jelent ez**: az a legénység, amely elég gyorsan semmisíti meg az idegenjeit, egyetlen idegenből akár 4 kilövést is kihozhat. Amelyik nem, az semmit sem kap ebből.

<!-- mob-split:end -->

## A főellenségek három lépése {#the-bosses-three-steps}

Minden főellenség három lépésben változtatja a harcmodorát: amikor a harc elindul, amikor a hajóteste kétharmad alá esik, és amikor egyharmad alá esik. Egy lépés egyszer történik meg, és sosem fordul vissza, hacsak a főellenség nem kezdi elölről, ahogy alább olvasható.

<!-- mob-ladders:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **Szünet minden lépésnél.** Amikor az első után egy olyan lépés kezdődik, amelynek van tennivalója, a főellenség 1,5 mp ideig nem sebezhető (3 mp a kazamata hadurának és a szólókapuk főellenségeinek).
- **Különleges képesség is.** Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah és Boss Crystalys különleges képességet is hordozhatnak (Dormant Force és Tesseract soha): a második és a harmadik lépés között jön; ha a kettő egyszerre kezdődne, a későbbi legfeljebb 3 mp ideig vár. Soha nem olyan képesség, amelyet a vezér saját lépései használnak.
- **Elölről kezdi.** A Tesseract elölről kezdi a lépéseit, amint teljesen meggyógyult.

### A rajvezérek {#the-swarm-leaders}

| Vezér | Az elején | Kétharmad alatt | Egyharmad alatt |
| :--- | :--- | :--- | :--- |
| **Pirate Boss** | 3 rakétából álló legyezőt lő, 12 fokos közökkel, az első pilótára, aki eltalálta. | Egyszerre 5 újabb hajót hív: Pirate Scouts; legfeljebb 10 él egyszerre. Nem fizetnek, és 45 mp múlva távoznak. | 10 mp ideig a legközelebbi kapu felé repül, a sebességének szorzója ×1,8, aztán a pilóták ellen fordul. |
| **Boss Seeker** | A Seeker Slaves 8 mp ideig gyorsabban gyógyítják: a gyógyítás szorzója ×2. | 2 másolata jelenik meg, és a valódin gyűrű van. | 4 mp ideig menekül a pilóták elől, aztán visszafordul. |
| **Boss Phantasm** | A Phantasm Guards mindegyike a saját hajótestének 10% részét kitevő pajzsréteget emel. | 3 másolata jelenik meg, és a valódin gyűrű van. | Körülbelül 2 500 egységre ugrik a pilótáktól, és a Phantasm Guards sértetlenül térnek vissza körülötte. |
| **Boss Goombah** | 6 mp ideig minden találatnak csak 50% részét veszi fel. | 10 mp ideig a sebzésének szorzója ×1,5, a sebességének szorzója ×1,25. | Meggyógyítja a hajótestének és pajzsának 25% részét (egy sebzéslöket megszakítja), és közben a Goombah Guards gyorsabban gyógyítják: a szorzó ×2. |
| **Boss Crystalys** | 8 mp ideig minden találatnak csak 50% részét veszi fel. | Egy 700 egység sugarú gyűrű minden benne lévő hajót eltalál a sortüzének 4 adagjával, és 4 rakétát lő. | Meggyógyítja a hajótestének és pajzsának 20% részét (egy sebzéslöket megszakítja), és 3 újabb hajó jön: Crystalys Guards; legfeljebb 6 él egyszerre. |
| **Dormant Force** | Minden találatnak csak 70% részét veszi fel, amíg él egy a Dormant Pulses közül. | A Dormant Pulses 15 mp ideig 2,5 mp időközönként lőnek ki egy rakétát. | Amíg az összes Dormant Pulses él, 6 mp ideig másodpercenként a hajótestének 5% részét gyógyítják vissza. |
| **Tesseract** | – | 20 további hajó érkezik egyszerre a szokásos számuk fölött: Facets. | – |

### A klán-őrzők {#the-clan-wardens}

| Őrző | Az elején | Kétharmad alatt | Egyharmad alatt |
| :--- | :--- | :--- | :--- |
| **Brood Warden** (I, II, III) | Mind a 4 drón egyszerre a mellé áll. | A drónjai 15 mp ideig gyorsabban gyógyítják: a szorzó ×1,5. | 2 további drón érkezik a szokásos számuk fölött 30 mp ideig. Nem fizetnek. |
| **Siege Warden** (I, II, III) | – | 20 mp ideig gyakrabban lövi a rakétáját: a szorzó ×2. | Meggyógyítja a hajótestének és pajzsának 15% részét (egy sebzéslöket megszakítja). |
| **Wrath Warden** (I, II, III) | – | A lézerei keményebben ütnek: a szorzó ×1,25. | A lézerei összesen keményebben ütnek: a szorzó ×1,5, nem az előző lépésre ráadásul. |

### A kazamata hadura {#the-dungeon-warlord}

- **Kétharmad alatt**: A képességei közti szünet lecsökken: 4 mp, a várakozásaik szorzója ×0,75.
- **Egyharmad alatt**: A szünet 2 mp, a várakozások szorzója ×0,5, a sebzése szorzója ×1,25; egy ingyenes Meteor-sortüzet indít, és a Swarmja soha nem jön vissza gyorsabban, mint 120 mp időközönként.
- **Szünet minden lépésnél.** Amikor egy lépés elkezdődik, a hadúr 3 mp ideig nem sebezhető.

### A szólókapuk főellenségei {#the-solo-gate-bosses}

A szólókapuk hat főellenségének is három lépése van, a fázisaik: a szólókapuk cikkének [főellenségek](/wiki/03-Mechanics/Solo-Gates.md#the-bosses) táblázatában vannak.

<!-- mob-ladders:end -->

## További olvasnivaló {#where-to-read-more}

- [Harc](/wiki/03-Mechanics/Combat.md#who-an-alien-fights): kivel harcol egy idegen, és ki kapja a lelövését.
- [Rajok](/wiki/05-Swarms/Swarms.md): a vezérek és a lépéseik, minden rajról külön cikk.
- [Klán-Warden](/wiki/03-Mechanics/Clans.md#fighting-a-warden), a [kazamata Warlordja](/wiki/03-Mechanics/Dungeons.md#the-warlord) és a [szólókapuk főellenségei](/wiki/03-Mechanics/Solo-Gates.md#the-bosses).
- [Utazó kalauza](/wiki/03-Mechanics/Travelers-Guide.md): amit egy idegenről megtanultál. Sosem mondja meg, melyik hordoz képességet.
