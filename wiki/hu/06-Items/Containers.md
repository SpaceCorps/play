<!-- wiki-i18n source: 9cb279aeecb3bbc8 -->
<!-- wiki-i18n title: Konténerek -->
# Konténerek {#containers}

<!-- wiki-search: konténer; konténerek; láda; lootbox; loot box; esélyek; esély; valószínűség; garancia; pity; görgetés; nyitás; trezor; tégely; archívum; tartály; állvány; container; case; crate; odds; drop rate; vault; crucible; archive; canister; rack -->

A **konténer** a Mission Control lezárt lelete. Amikor megnyitsz egyet, a szerver egy jutalmat húz egy táblából, és a tábla minden jutalmának esélye ezen az oldalon áll. A játék Konténerek oldala ugyanezt a táblát mutatja.

> [!NOTE]
> **A konténerek a játékban szerzett véletlenszerű jutalmak. Soha nem árulják őket, és az esélyek itt közzé vannak téve.** Konténert nem lehet megvenni, cserélni vagy elajándékozni.

## Mi az a konténer {#what-a-container-is}

- **Megszerzett.** A konténereket a játékban szerzed. Nincs ára és nincs kulcsa: a Bolt nem árulja, és senki más sem.
- **Csak a tiéd.** A konténer a fiókodhoz kötött. Nem cserélheted el, nem adhatod egy barátodnak, és nem teheted fel az [Aukcióra](/wiki/03-Mechanics/Auction.md); ami egy konténerből kerül elő, az sem tehető fel oda.
- **Minden pilótának ugyanaz.** A Prémium semmit sem változtat: nem ad extra nyitást és jobb esélyeket sem.
- **A wipe-on át megmarad.** A meg nem nyitott konténer a fiókodon marad, amikor jön a [wipe](/wiki/03-Mechanics/Wipe-Timeline.md). Hogy a wipe mit tesz a jutalmakkal, az [A wipe](#the-wipe) alatt áll.
- **Az állomáson nyitható.** A konténert dokkolva nyitod meg, a Konténerek oldalon. A szerver a jutalmat akkor húzza, amikor a Megnyitásra kattintasz, és maga a kattintás nem változtat semmin. Hogy mi számít, azt a [Hogyan választódik ki egy jutalom](#how-a-prize-is-chosen) rész mondja el.

## Honnan jönnek a konténerek {#where-containers-come-from}

<!-- containers-sources:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

A konténerek így jutnak el hozzád:

- A játék adminjaitól
- Jutalomként a rangodért a wipe-nál
- A bejelentkezési naptárban
- Eredményekért

<!-- containers-sources:end -->

## Az öt konténer {#the-five-containers}

<!-- containers-glance:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Konténer | Mit tartalmaz | Ajánlott | Bezár a wipe-nál | Garancia | Legritkább jutalom |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Mintatrezor (Specimen Vault)** | Egy kicsit mindenből: kredit, Thulium, lőszer, rakéták, felszerelés, lemezek, Dark Matter, boosterek és színek | Bármely pilóta | A szezon 30. napjától | Legalább Ritka fokozatú jutalom 10 nyitáson belül | 60 000 Thulium; 12 000 000 kredit: egyenként 0,100% |
| **Öntödei tégely (Foundry Crucible)** | Lőszer, rakéták, lézerek, erősítők, pajzscellák, fúvókák és felszerelés, valamint 5 hajó | 5. szinttől | A szezon 30. napjától | Legalább Ritka fokozatú jutalom 8 nyitáson belül | hajó: Wraith: 0,020% |
| **Króma-archívum (Chroma Archive)** | Csak kinézetek: skinek, színek, kipufogóeffektek és aurák | Bármely pilóta | Nyitva marad | Legalább Epikus fokozatú jutalom 12 nyitáson belül | Crystal Ice; Comet; Halo: egyenként 0,667% |
| **Felmérő tartály (Survey Canister)** | Skylab-érc, lemezek, Dark Matter, Cluster Chunks és Thulium | Skylab-mag 10. szinttől | A szezon 30. napjától | Legalább Ritka fokozatú jutalom 8 nyitáson belül | 32 × Dark Matter Plate; 50 000 Thulium: egyenként 0,150% |
| **Reagensállvány (Reagent Rack)** | Boosterek, EMP Charges, Energetic Walls és lőszer | 4. szinttől | A szezon 30. napjától | Legalább Ritka fokozatú jutalom 10 nyitáson belül | **Teljes spektrum**; Cloaking CPU L: egyenként 0,100% |

<!-- containers-glance:end -->

Az **Ajánlott** csak tanács: a játék bármelyik konténert megnyitni engedi bármelyik szinten.

## Fokozatok {#grades}

Minden jutalomnak van egy **fokozata**, a játék egyik ritkasági szava. A fokozatot dönti el a húzás először. A görgetésen ez a jutalom csempéjének kerete, színben és alakban, hogy a szín soha ne legyen az egyetlen jel.

| Fokozat | Szín | Alak |
| :--- | :--- | :--- |
| Gyakori | Szürke | Kör |
| Szokatlan | Zöld | Négyzet |
| Ritka | Kék | Rombusz |
| Epikus | Lila | Hatszög |
| Mitikus | Rózsaszín | Csillag |
| Legendás | Arany | Korona |

Minden konténernek megvan a saját esélye minden fokozatra, lent kifejtve. Az, amid van, soha nem változtatja egy fokozat esélyét.

## Mintatrezor (Specimen Vault) {#specimen-vault}

*A Mission Control xenoarchivistái minden olyan leletet, amelyet nem tudnak egyetlen szakterület alá sorolni, számozott trezorba zárnak, és bontatlanul elküldik. Az állomáson senki sem tudja, mi van egy trezorban, amíg egy pilóta fel nem töri a pecsétet.*

### A fokozatok esélyei {#specimen-vault-grades}

<!-- containers-specimen-vault-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Fokozat | Esély | Benne lévő jutalmak |
| :--- | ---: | ---: |
| Gyakori | 38,000% | 9 |
| Szokatlan | 38,000% | 8 |
| Ritka | 17,000% | 8 |
| Epikus | 5,500% | 5 |
| Mitikus | 1,300% | 4 |
| Legendás | 0,200% | 2 |

<!-- containers-specimen-vault-grades:end -->

### Minden jutalom {#specimen-vault-prizes}

<!-- containers-specimen-vault-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Fokozat | Jutalom | Esély |
| :--- | :--- | ---: |
| Gyakori | 50 000 kredit | 5,000% |
| Gyakori | 250 Thulium | 4,000% |
| Gyakori | 10 000 × Standard Battery | 4,000% |
| Gyakori | 500 × Advanced Plasma | 4,000% |
| Gyakori | 250 × Ultra Core | 3,000% |
| Gyakori | **I. rakétacsomag**: 4 közül egy, 100 darab, azonos eséllyel: Ember I, Lancet I, Rivet I, Scatter I | 6,000% |
| Gyakori | **Kovácsolópor**: 1 500 × Daraxium + 1 500 × Nyxite | 3,000% |
| Gyakori | 4 000 × Ship Fragment | 3,000% |
| Gyakori | 1 óra Experience Booster | 6,000% |
| Szokatlan | 150 000 kredit | 6,000% |
| Szokatlan | 750 Thulium | 6,000% |
| Szokatlan | 750 × Ultra Core | 4,500% |
| Szokatlan | 340 × Experimental Fusion Core | 4,000% |
| Szokatlan | **II. rakétacsomag**: 4 közül egy, 190 darab, azonos eséllyel: Ember II, Lancet II, Rivet II, Scatter II | 6,000% |
| Szokatlan | 10 × Velkonite Reinforced Plate | 4,000% |
| Szokatlan | 1 óra Laser Damage Booster I | 4,000% |
| Szokatlan | **Színminta**: 11 közül egy, azonos eséllyel: Cobalt, Indigo, Violet, Magenta, Crimson, Ember, Sunset, Gold, Emerald, Jade, Teal | 3,500% |
| Ritka | 400 000 kredit | 2,500% |
| Ritka | 2 000 Thulium | 2,500% |
| Ritka | 10 × Dark Matter | 1,500% |
| Ritka | **III. rakétacsomag**: 4 közül egy, 400 darab, azonos eséllyel: Ember III, Lancet III, Rivet III, Scatter III | 2,000% |
| Ritka | 1 000 × Experimental Fusion Core | 1,500% |
| Ritka | 9 × Orvium Reinforced Plate | 1,500% |
| Ritka | 4 óra Laser Damage Booster I | 1,500% |
| Ritka | **Egy II. szintű alkatrész**: 4 közül egy, azonos eséllyel: Absorption Shield Cell II, Capacity Shield Cell II, Impulse Thruster II, Momentum Thruster II | 4,000% |
| Epikus | 1 200 000 kredit | 1,200% |
| Epikus | 6 000 Thulium | 1,200% |
| Epikus | 30 × Dark Matter | 0,900% |
| Epikus | 26 × Orvium Reinforced Plate | 0,900% |
| Epikus | **Egy III. szintű alkatrész**: 5 közül egy, azonos eséllyel: Absorption Shield Cell III, Capacity Shield Cell III, Impulse Thruster III, Momentum Thruster III, Starfire-III | 1,300% |
| Mitikus | 18 000 Thulium | 0,400% |
| Mitikus | 12 × Dark Matter Plate | 0,300% |
| Mitikus | Helios Beam | 0,300% |
| Mitikus | **Egy IV. szintű erősítő**: 3 közül egy, azonos eséllyel: Damage Amp IV, Crit Amp IV, Penetration Amp IV | 0,300% |
| Legendás | 60 000 Thulium | 0,100% |
| Legendás | 12 000 000 kredit | 0,100% |

<!-- containers-specimen-vault-prizes:end -->

A **Színminta** egy olyan színt ad, amely még nincs meg neked. Ha a minta minden színe megvan, helyette hasznosítási Thuliumot fizet ([Duplikátumok és hasznosítás](#duplicates-and-salvage)).

### A garancia {#specimen-vault-guarantee}

<!-- containers-specimen-vault-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Garancia**: legalább Ritka fokozatú jutalom legalább minden 10. nyitásnál
- **Ritka fokozatú vagy jobb jutalom esélye garancia nélkül**: 24,000%
- **A garanciával, sok nyitás alatt**: 25,649%
- **A garancia által kikényszerített nyitások**: 2,170%
- **Két ilyen jutalom között átlagosan eltelt nyitások**: 3,899

<!-- containers-specimen-vault-guarantee:end -->

## Öntödei tégely (Foundry Crucible) {#foundry-crucible}

*A Dormant öntödék kihűltek úgy, hogy az utolsó adag még a tégelyben maradt: lőszer, felszerelt alkatrészek, és a legmélyebbekben egy soha el nem készült hajótest. A Mission Control mérnökei kivágták a tégelyeket a romok közül, és lezárva adják át a pilótáknak, mert senki sem mondhatja meg, melyikben van hajótest.*

### A fokozatok esélyei {#foundry-crucible-grades}

<!-- containers-foundry-crucible-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Fokozat | Esély | Benne lévő jutalmak |
| :--- | ---: | ---: |
| Gyakori | 45,000% | 6 |
| Szokatlan | 30,000% | 7 |
| Ritka | 16,000% | 6 |
| Epikus | 6,500% | 6 |
| Mitikus | 2,200% | 5 |
| Legendás | 0,300% | 2 |

<!-- containers-foundry-crucible-grades:end -->

### Minden jutalom {#foundry-crucible-prizes}

<!-- containers-foundry-crucible-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Fokozat | Jutalom | Esély |
| :--- | :--- | ---: |
| Gyakori | 30 000 × Standard Battery | 7,000% |
| Gyakori | 1 500 × Advanced Plasma | 7,000% |
| Gyakori | 750 × Ultra Core | 7,000% |
| Gyakori | 340 × Experimental Fusion Core | 5,000% |
| Gyakori | **I. rakétacsomag**: 4 közül egy, 300 darab, azonos eséllyel: Ember I, Lancet I, Rivet I, Scatter I | 11,000% |
| Gyakori | **Lézerkészlet**: Quantum Laser II + Damage Amp I + Crit Amp I + Penetration Amp I | 8,000% |
| Szokatlan | 2 250 × Ultra Core | 4,500% |
| Szokatlan | 1 020 × Experimental Fusion Core | 4,500% |
| Szokatlan | **II. rakétacsomag**: 4 közül egy, 560 darab, azonos eséllyel: Ember II, Lancet II, Rivet II, Scatter II | 8,500% |
| Szokatlan | Basic Shield Core | 4,500% |
| Szokatlan | **II. szintű erősítőtrió**: Damage Amp II + Crit Amp II + Penetration Amp II | 4,000% |
| Szokatlan | Repair Drone IV | 3,900% |
| Szokatlan | hajó: Nomad | 0,100% |
| Ritka | 1 800 × Experimental Fusion Core | 2,500% |
| Ritka | **III. rakétacsomag**: 4 közül egy, 500 darab, azonos eséllyel: Ember III, Lancet III, Rivet III, Scatter III | 3,000% |
| Ritka | Quantum Laser III | 2,400% |
| Ritka | **Egy II. szintű alkatrész**: 4 közül egy, azonos eséllyel: Absorption Shield Cell II, Capacity Shield Cell II, Impulse Thruster II, Momentum Thruster II | 4,500% |
| Ritka | **Egy III. szintű erősítő**: 3 közül egy, azonos eséllyel: Damage Amp III, Crit Amp III, Penetration Amp III | 3,500% |
| Ritka | hajó: Paragon | 0,100% |
| Epikus | **Egy III. szintű cella vagy fúvóka**: 4 közül egy, azonos eséllyel: Absorption Shield Cell III, Capacity Shield Cell III, Impulse Thruster III, Momentum Thruster III | 3,000% |
| Epikus | Starfire-III | 1,200% |
| Epikus | Heavy Shield Core | 1,200% |
| Epikus | Cloaking CPU M | 1,000% |
| Epikus | hajó: Storm | 0,050% |
| Epikus | hajó: Ironclad | 0,050% |
| Mitikus | Helios Beam | 0,600% |
| Mitikus | **Egy IV. szintű cella vagy fúvóka**: 4 közül egy, azonos eséllyel: Absorption Shield Cell IV, Capacity Shield Cell IV, Impulse Thruster IV, Momentum Thruster IV | 0,700% |
| Mitikus | **Egy IV. szintű erősítő**: 3 közül egy, azonos eséllyel: Damage Amp IV, Crit Amp IV, Penetration Amp IV | 0,480% |
| Mitikus | Cloaking CPU L | 0,400% |
| Mitikus | hajó: Wraith | 0,020% |
| Legendás | **Helios fegyvertár**: Helios Beam + Damage Amp IV + Crit Amp IV + Penetration Amp IV | 0,150% |
| Legendás | 50 000 Thulium | 0,150% |

<!-- containers-foundry-crucible-prizes:end -->

A hajók az alapesélyükkel szerepelnek. A hajó, amely már megvan neked, soha nem esik, ezért a saját esélyeid kissé eltérhetnek ettől a táblától: lásd [A hajók](#the-ships).

### A garancia {#foundry-crucible-guarantee}

<!-- containers-foundry-crucible-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Garancia**: legalább Ritka fokozatú jutalom legalább minden 8. nyitásnál
- **Ritka fokozatú vagy jobb jutalom esélye garancia nélkül**: 25,000%
- **A garanciával, sok nyitás alatt**: 27,781%
- **A garancia által kikényszerített nyitások**: 3,708%
- **Két ilyen jutalom között átlagosan eltelt nyitások**: 3,600

<!-- containers-foundry-crucible-guarantee:end -->

## Króma-archívum (Chroma Archive) {#chroma-archive}

*A Dormant lila-fekete kristályból épített, ibolyaszín erekkel, és az archivistáik a színt vékony üveglemezeken tárolták, amelyek újrafestenek mindent, amihez hozzányomják őket. Minden Króma-archívum ilyen lemezek lezárt kötege, amelyet a Mission Control koloristái katalogizáltak, és senki sem olvasott, amíg egy pilóta meg nem nyitja.*

A Króma-archívum először a fokozatot húzza, majd az adott fokozat egy olyan kinézetét, amely még nincs meg neked, minden kinézet egyenlő eséllyel. A gyűjtemény egy jutalom: minden skinjét megkapod, amely még nincs meg. A táblázat esélye olyan pilótára vonatkozik, akinek a fokozat egyik kinézete sincs meg. Gyűjtés közben nő, mert kevesebb kinézet marad a húzásban. Magukat a kinézeteket a [Kozmetika](/wiki/06-Items/Cosmetics.md) írja le.

### A fokozatok esélyei {#chroma-archive-grades}

<!-- containers-chroma-archive-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Fokozat | Esély | Benne lévő kinézetek |
| :--- | ---: | ---: |
| Gyakori | 6,000% | 1 |
| Szokatlan | 50,000% | 14 |
| Ritka | 30,000% | 8 |
| Epikus | 12,000% | 12 |
| Mitikus | 2,000% | 3 |
| Legendás | 0,000% | – |

<!-- containers-chroma-archive-grades:end -->

### Minden jutalom {#chroma-archive-prizes}

<!-- containers-chroma-archive-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Fokozat | Kinézet | Esély, ha a fokozatból egyik sincs meg |
| :--- | :--- | ---: |
| Gyakori | Glow (aura) | 6,000% |
| Szokatlan | Company Supporter (gyűjtemény) | 3,571% |
| Szokatlan | Cobalt (szín) | 3,571% |
| Szokatlan | Indigo (szín) | 3,571% |
| Szokatlan | Violet (szín) | 3,571% |
| Szokatlan | Magenta (szín) | 3,571% |
| Szokatlan | Crimson (szín) | 3,571% |
| Szokatlan | Ember (szín) | 3,571% |
| Szokatlan | Sunset (szín) | 3,571% |
| Szokatlan | Gold (szín) | 3,571% |
| Szokatlan | Emerald (szín) | 3,571% |
| Szokatlan | Jade (szín) | 3,571% |
| Szokatlan | Teal (szín) | 3,571% |
| Szokatlan | Twin (kipufogóeffekt) | 3,571% |
| Szokatlan | Breath (aura) | 3,571% |
| Ritka | Nature White (gyűjtemény) | 3,750% |
| Ritka | Sunrise Orbit (gyűjtemény) | 3,750% |
| Ritka | Seeker Burnt (szín) | 3,750% |
| Ritka | Pirate Brick (szín) | 3,750% |
| Ritka | Pulse (kipufogóeffekt) | 3,750% |
| Ritka | Helix (kipufogóeffekt) | 3,750% |
| Ritka | Motes (aura) | 3,750% |
| Ritka | Shimmer (aura) | 3,750% |
| Epikus | Midnight Gala (gyűjtemény) | 1,000% |
| Epikus | Blue Marble (gyűjtemény) | 1,000% |
| Epikus | Mimosa (gyűjtemény) | 1,000% |
| Epikus | Olive Branch (gyűjtemény) | 1,000% |
| Epikus | Steady Pulse (gyűjtemény) | 1,000% |
| Epikus | Hollow Night (gyűjtemény) | 1,000% |
| Epikus | Dormant Void (szín) | 1,000% |
| Epikus | Ancient Amethyst (szín) | 1,000% |
| Epikus | Embers (kipufogóeffekt) | 1,000% |
| Epikus | Gradient (kipufogóeffekt) | 1,000% |
| Epikus | Sparkle (aura) | 1,000% |
| Epikus | Wreath (aura) | 1,000% |
| Mitikus | Crystal Ice (szín) | 0,667% |
| Mitikus | Comet (kipufogóeffekt) | 0,667% |
| Mitikus | Halo (aura) | 0,667% |

<!-- containers-chroma-archive-prizes:end -->

### A garancia {#chroma-archive-guarantee}

<!-- containers-chroma-archive-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Garancia**: legalább Epikus fokozatú jutalom legalább minden 12. nyitásnál
- **Epikus fokozatú vagy jobb jutalom esélye garancia nélkül**: 14,000%
- **A garanciával, sok nyitás alatt**: 16,740%
- **A garancia által kikényszerített nyitások**: 3,186%
- **Két ilyen jutalom között átlagosan eltelt nyitások**: 5,974

<!-- containers-chroma-archive-guarantee:end -->

## Felmérő tartály (Survey Canister) {#survey-canister}

*A felmérő szondák a Skylabokból a világegyetem-térkép ködébe repülnek, és mindegyik magmintákat tartalmazó lezárt tartályként tér vissza. Érc egy fel nem térképezett telérből, anomáliák, és néha egy darab valamiből, ami régebbi a térképnél: a Mission Control cellák szerint iktatja a tartályt, és az olvasást a Skylab tulajdonosára hagyja.*

### A fokozatok esélyei {#survey-canister-grades}

<!-- containers-survey-canister-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Fokozat | Esély | Benne lévő jutalmak |
| :--- | ---: | ---: |
| Gyakori | 45,000% | 8 |
| Szokatlan | 30,000% | 7 |
| Ritka | 16,000% | 6 |
| Epikus | 6,500% | 5 |
| Mitikus | 2,200% | 3 |
| Legendás | 0,300% | 2 |

<!-- containers-survey-canister-grades:end -->

### Minden jutalom {#survey-canister-prizes}

<!-- containers-survey-canister-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Fokozat | Jutalom | Esély |
| :--- | :--- | ---: |
| Gyakori | 240 × Velkonite (a Skylabba) | 7,000% |
| Gyakori | 160 × Orvium (a Skylabba) | 7,000% |
| Gyakori | 1 300 × Reinforced Hull Plate | 5,000% |
| Gyakori | 9 000 × Ship Fragment | 6,000% |
| Gyakori | **Kovácsolókristályok**: 4 000 × Cataclysite + 3 000 × Quorvium | 5,000% |
| Gyakori | 450 × Power Core | 5,000% |
| Gyakori | 450 Thulium | 5,000% |
| Gyakori | 4 × Regular Cluster Chunk | 5,000% |
| Szokatlan | 780 × Velkonite (a Skylabba) | 5,000% |
| Szokatlan | 510 × Orvium (a Skylabba) | 5,000% |
| Szokatlan | 19 × Velkonite Reinforced Plate | 4,000% |
| Szokatlan | 7 × Dark Matter | 5,000% |
| Szokatlan | 8 × Ancient Control Unit | 3,000% |
| Szokatlan | 1 450 Thulium | 4,000% |
| Szokatlan | 3 × Mythical Cluster Chunk | 4,000% |
| Ritka | 17 × Dark Matter | 3,500% |
| Ritka | 15 × Orvium Reinforced Plate | 3,000% |
| Ritka | 1 900 × Velkonite (a Skylabba) | 2,500% |
| Ritka | 1 230 × Orvium (a Skylabba) | 2,500% |
| Ritka | 2 × Legendary Cluster Chunk | 1,500% |
| Ritka | 3 500 Thulium | 3,000% |
| Epikus | 45 × Dark Matter | 1,500% |
| Epikus | 39 × Orvium Reinforced Plate | 1,200% |
| Epikus | **Vegyes lemezláda**: 60 × Velkonite Reinforced Plate + 20 × Orvium Reinforced Plate | 1,200% |
| Epikus | 9 000 Thulium | 1,500% |
| Epikus | 6 × Dark Matter Plate | 1,100% |
| Mitikus | 13 × Dark Matter Plate | 0,900% |
| Mitikus | 20 000 Thulium | 0,800% |
| Mitikus | 100 × Dark Matter | 0,500% |
| Legendás | 32 × Dark Matter Plate | 0,150% |
| Legendás | 50 000 Thulium | 0,150% |

<!-- containers-survey-canister-prizes:end -->

A *(a Skylabba)* jelölésű érc a Skylab ércraktárába kerül, amennyit az Erőforrás-tároló helye enged. A többi ugyanaz az érc a készletedben. Lásd [Skylab](/wiki/03-Mechanics/Skylab.md).

### A garancia {#survey-canister-guarantee}

<!-- containers-survey-canister-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Garancia**: legalább Ritka fokozatú jutalom legalább minden 8. nyitásnál
- **Ritka fokozatú vagy jobb jutalom esélye garancia nélkül**: 25,000%
- **A garanciával, sok nyitás alatt**: 27,781%
- **A garancia által kikényszerített nyitások**: 3,708%
- **Két ilyen jutalom között átlagosan eltelt nyitások**: 3,600

<!-- containers-survey-canister-guarantee:end -->

## Reagensállvány (Reagent Rack) {#reagent-rack}

*A Skylab Kutatóközpontja reagensampullákból desztillálja a boostereket, amelyekkel repülsz, és az állvány az, ami egy megszakított adagból megmarad: minden reagensből egy kimért adag a saját lezárt ampullájában. Az adagok csak akkor öregszenek, amíg egy hajó repül, ezért az állvány a polcon marad, ameddig csak akarod.*

### A fokozatok esélyei {#reagent-rack-grades}

<!-- containers-reagent-rack-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Fokozat | Esély | Benne lévő jutalmak |
| :--- | ---: | ---: |
| Gyakori | 45,000% | 5 |
| Szokatlan | 33,000% | 8 |
| Ritka | 15,000% | 8 |
| Epikus | 5,500% | 6 |
| Mitikus | 1,300% | 2 |
| Legendás | 0,200% | 2 |

<!-- containers-reagent-rack-grades:end -->

### Minden jutalom {#reagent-rack-prizes}

<!-- containers-reagent-rack-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Fokozat | Jutalom | Esély |
| :--- | :--- | ---: |
| Gyakori | 1 óra Experience Booster | 11,000% |
| Gyakori | 1 óra Honor Booster | 11,000% |
| Gyakori | 1 óra Shield Regen Booster | 9,000% |
| Gyakori | Energetic Wall I | 8,000% |
| Gyakori | 500 × Advanced Plasma | 6,000% |
| Szokatlan | 1 óra Laser Damage Booster I | 5,000% |
| Szokatlan | 1 óra Shield Wall Booster I | 5,000% |
| Szokatlan | 1 óra Hull Plating Booster I | 5,000% |
| Szokatlan | 1 óra Resource Magnet Booster | 3,500% |
| Szokatlan | 2 óra Experience Booster | 4,500% |
| Szokatlan | 2 óra Honor Booster | 3,500% |
| Szokatlan | EMP Charge | 3,500% |
| Szokatlan | 3 × Energetic Wall I | 3,000% |
| Ritka | 2 óra Laser Damage Booster I | 2,500% |
| Ritka | 2 óra Shield Wall Booster I | 2,000% |
| Ritka | 2 óra Hull Plating Booster I | 2,000% |
| Ritka | 4 óra Experience Booster | 2,000% |
| Ritka | 4 óra Honor Booster | 2,000% |
| Ritka | 2 óra Loot Luck Booster | 1,500% |
| Ritka | 3 × EMP Charge | 2,000% |
| Ritka | 2 óra Resource Magnet Booster | 1,000% |
| Epikus | 4 óra Laser Damage Booster I | 1,200% |
| Epikus | 4 óra Shield Wall Booster I | 1,000% |
| Epikus | 4 óra Hull Plating Booster I | 1,000% |
| Epikus | 4 óra Resource Magnet Booster | 0,700% |
| Epikus | 4 óra Loot Luck Booster | 0,900% |
| Epikus | 8 × EMP Charge | 0,700% |
| Mitikus | **Harci állvány**: 4 óra Laser Damage Booster I + 4 óra Shield Wall Booster I + 4 óra Hull Plating Booster I | 0,700% |
| Mitikus | **Tudós állványa**: 4 óra Experience Booster + 4 óra Honor Booster + 4 óra Resource Magnet Booster + 4 óra Loot Luck Booster | 0,600% |
| Legendás | **Teljes spektrum**: 4 óra Laser Damage Booster I + 4 óra Shield Wall Booster I + 4 óra Hull Plating Booster I + 4 óra Shield Regen Booster + 4 óra Experience Booster + 4 óra Honor Booster + 4 óra Resource Magnet Booster + 4 óra Loot Luck Booster | 0,100% |
| Legendás | Cloaking CPU L | 0,100% |

<!-- containers-reagent-rack-prizes:end -->

A booster ideje hozzáadódik ugyanahhoz a boosterhez, ha már fut, és csak repülés közben fogy. Lásd [Boosterek](/wiki/06-Items/Boosters.md).

### A garancia {#reagent-rack-guarantee}

<!-- containers-reagent-rack-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Garancia**: legalább Ritka fokozatú jutalom legalább minden 10. nyitásnál
- **Ritka fokozatú vagy jobb jutalom esélye garancia nélkül**: 22,000%
- **A garanciával, sok nyitás alatt**: 24,001%
- **A garancia által kikényszerített nyitások**: 2,565%
- **Két ilyen jutalom között átlagosan eltelt nyitások**: 4,167

<!-- containers-reagent-rack-guarantee:end -->

## Hogyan választódik ki egy jutalom {#how-a-prize-is-chosen}

A szerver három lépésben választ, amikor megnyitsz egy konténert:

1. **A fokozat.** Egy véletlen számot a fokozatok esélyeihez illesztenek.
2. **A jutalom.** Egy második számot az adott fokozat jutalmainak esélyeihez illesztenek. A hajó, amely már megvan neked, nem tartozik közéjük (lásd [A hajók](#the-ships)).
3. **A választás az egyenlők közül.** Az a jutalom, amely azt mondja, *egy a következők közül*, az egyiket adja, mindegyik egyenlő eséllyel.

A számok a szerver operációs rendszerének véletlenszám-generátorából jönnek, és azután húzódnak, hogy a konténert elvették tőled. Semmi, amit küldesz, nem változtathatja meg őket: sem a gomb, sem az idő.

Két korábbi dolog viszont számít. A garancia számlálója az egyik nyitásról a másikra átmegy; fent az egyes konténerek garanciája írja le. És az, ami már megvan neked, a korábbi nyitásokban nyert dolgokkal együtt, megváltoztatja, hogy mely jutalmak maradnak a húzásban: a hajó, amely megvan neked, nincs köztük, és a kinézet, amely megvan neked, nem húzódik ki, amíg a fokozatában van olyan, amely még nincs meg (lásd: [Duplikátumok és hasznosítás](#duplicates-and-salvage) és [A hajók](#the-ships)). Az, ami megvan neked, soha nem változtatja meg a fokozatok esélyeit.

<!-- containers-draw:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- Minden esély egész számú rész, összesen 100 000 részből. Egy rész 0,001%.

<!-- containers-draw:end -->

**Minden nyitás rögzítésre kerül** a magjával (a véletlen számmal, amelyet a szerver használt), a kihúzott számokkal, a tábla hashével, amelyből húzott, és azokkal a jutalmakkal, amelyeket a birtokod kivett a húzásból. Elolvashatod őket a Konténerek oldal **Előzmények** részében, a **Részletek** alatt.

**Egyet magad is ellenőrizhetsz.** A játék forráskódjában lévő `scripts/containers-verify.py` eszköz beolvassa a táblát és egy nyitás részleteit, és megmondja, hogy a fokozat, a jutalom és a választás következik-e a magból. A módszer rövid:

```text
stream(seed, id): value i, for i = 0, 1, 2, ...
  = the first 8 bytes (big endian) of HMAC-SHA256(
      key     = seed,
      message = "sc-container-v1|" + id + "|" + i )
  where i is written as 4 bytes, big endian
below(n): take values until one is under 2^64 - (2^64 mod n),
  then use it modulo n (no modulo bias)
grade:    roll = below(total of the grades in play);
  the grade is the first whose running sum is above the roll
prize:    sub = below(total of the prizes left in that grade);
  the prize is the first whose running sum is above sub
choice:   a prize that is "one of N" gives the alternative
  number below(N)
seed = the 32 bytes shown under Details; id = the container's id.
When the guarantee forces an opening, only the guaranteed grade
and better are in play.
```

## Duplikátumok és hasznosítás {#duplicates-and-salvage}

- Egy **kinézetet**, amely megvan neked, nem húz ki, amíg a fokozatban van olyan kinézet, amely még nincs meg. A gyűjtemény akkor számít megvettnek, ha minden skinje megvan.
- Ha a fokozat minden kinézete megvan, a jutalom helyette **hasznosítást** fizet: Thuliumot, fokozat szerint. A garancia szempontjából ennek a fokozatnak a jutalmaként számít.
- A **tárgyakat** soha nem váltják Thuliumra: halmozódnak, vagy úgy érkeznek, ahogy vannak.
- A **hajókat** soha nem adják kétszer, és soha nem fizetik hasznosításként (lásd [A hajók](#the-ships)).

<!-- containers-salvage:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Fokozat | Thulium |
| :--- | ---: |
| Gyakori | 25 |
| Szokatlan | 100 |
| Ritka | 400 |
| Epikus | 1 200 |
| Mitikus | 4 000 |

<!-- containers-salvage:end -->

## A hajók {#the-ships}

Az Öntödei tégely tartalmazhat hajót. A tábla a hajókat az **alapesélyükkel** sorolja fel, azzal az eséllyel, amely olyan pilótára vonatkozik, akinek egyik sincs meg. Ezek a közzétett esélyek.

A hajó, amely már megvan neked, soha nem eshet. Kikerül a húzásból, és a részesedése ugyanannak a fokozatnak a többi jutalmára megy, a saját esélyeik arányában. Tehát az, amid van, megváltoztatja a saját esélyeidet: kicsit magasabb lesz az adott fokozat többi jutalmán. A fokozatok esélyei soha nem változnak, és a garancia sem. Egy hajóból készült dizájn úgy számít, mintha a hajó megvolna: egy Paragon THUNDER úgy számít, mintha megvolna a Paragon.

<!-- containers-ships:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Hajó | Fokozat | Esély |
| :--- | :--- | ---: |
| Nomad | Szokatlan | 0,100% |
| Paragon | Ritka | 0,100% |
| Storm | Epikus | 0,050% |
| Ironclad | Epikus | 0,050% |
| Wraith | Mitikus | 0,020% |
| **Összesen 5** | | **0,320%** |

Példa: neked megvan a hajó: Nomad. A Szokatlan fokozat megtartja az esélyét, de a fokozat 30 000 részéből kikerül a hajó (Nomad) 100 része a húzásból, így a Szokatlan fokozat minden más jutalma 30 000 / 29 900 = 1,0033-szer valószínűbb, mint ahogy a tábla mondja.

A következő tábla arra az esetre vonatkozik, ha a fokozat minden hajója megvan neked. Ha csak néhány van meg, csak azok részei kerülnek ki a húzásból, ezért a szorzó kisebb.

| Fokozat | A fokozat részei | Az összes hajó részei | A fokozat minden más jutalma ennyivel valószínűbb |
| :--- | ---: | ---: | ---: |
| Szokatlan | 30 000 | 100 | ×1,0033 |
| Ritka | 16 000 | 100 | ×1,0063 |
| Epikus | 6 500 | 100 | ×1,0156 |
| Mitikus | 2 200 | 20 | ×1,0092 |

Példa: a Epikus fokozatban 2 hajó van. Ha csak ez a hajó van meg neked: Storm, a fokozat 6 500 részéből csak ennek a hajónak a 50 része kerül ki a húzásból, így a Epikus fokozat minden más jutalmának esélye 6 500 / 6 450 = 1,0078 szorosára nő, nem 1,0156 szorosára.

<!-- containers-ships:end -->

A játék Konténerek oldala a saját esélyeidet a közzétettek mellett mutatja, ha eltérnek. A hajó, amely megvan neked, szürkén marad a listában, ezzel a sorral: „Ez a hajó megvan neked, ezért nem eshet konténerből.”

## A wipe {#the-wipe}

- **A meg nem nyitott konténerek megmaradnak.** A wipe-on át a fiókodon maradnak.
- **A konténerből kapott tárgyak közönséges tárgyak.** A wipe-nál elvesznek, ha nem viszed át őket a Tranzittárolóban ([Wipe-idővonal](/wiki/03-Mechanics/Wipe-Timeline.md)).
- **A kinézetek és a hajók nálad maradnak**, mint bármely kinézet és bármely hajó. A kreditek, a Thulium és a boosterek hátralévő ideje a wipe-nál a saját szabályaik szerint alakulnak.
- **Konténerből semmi nem tehető fel az Aukcióra.**

<!-- containers-wipe:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Zárva a szezon 30. napjától**: Mintatrezor, Öntödei tégely, Felmérő tartály, Reagensállvány. Amit tartalmaznak, elveszne a wipe-nál, ezért a wipe végéig nem nyithatók meg.
- **Sáv**: a Konténerek oldal a szezon 28. napjától figyelmeztet.
- **Nyitva marad**: Króma-archívum. Csak kinézeteket tartalmaz, és a wipe megtartja a kinézeteket.

<!-- containers-wipe:end -->

## A tábla verziója {#version-of-the-table}

Az oldalon minden esély a játék szerverének táblája. Ha egy esély változik, a tábla új verziót és új hasht kap, és minden nyitás rögzíti annak a táblának a hashét, amelyből húztak.

<!-- containers-version:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **A tábla verziója**: 1
- **A tábla hashe (az első 12 karakter)**: `23aa20f1a5ad`

Mi változott:

- 1. verzió: Az első közzétett tábla.

<!-- containers-version:end -->
