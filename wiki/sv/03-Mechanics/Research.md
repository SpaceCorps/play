<!-- wiki-i18n source: bf987d259afc1762 -->
<!-- wiki-i18n title: Forskning -->
# Forskning {#research}

**Forskningscentrumet** är laboratoriet i din [Skylab](/wiki/03-Mechanics/Skylab.md). Du matar det med resurser, det gör om dem till **vetenskap**, och vetenskapen forskar fram **teknologier**. All tillverkning i [Monteringen](/wiki/06-Items/Overview.md#upgrading-modules) kräver först sin teknologi: ett skepp, en laser, en styrraket eller en CPU går inte att tillverka förrän den är framforskad.

Den här sidan har hela teknologiträdet med tiden för varje teknologi, vetenskapen varje resurs ger, Thulium-boosten, regeln för Dark Matter och de nya CPU:erna. Siffrorna läses ur spelets egna data, så det är alltid spelets siffror.

![The Research view with a technology that needs Dark Matter picked: its Dark Matter row, the Add and Take back buttons, where Dark Matter comes from and the Wiki button](../../img/wiki-img/shots/research-dark-matter.jpg)
![The Research view filtered to the Defence tree: the shield and hull formations, each a technology with its Dark Matter](../../img/wiki-img/shots/research-formations.jpg)
![The Research view of the Skylab with the pointer on Impulse Thruster III: its kind and tier, what it does, its numbers, the four tiers of its family and what Assembly asks to craft it](../../img/wiki-img/shots/research-hover.jpg)

## Forskningscentrumet {#the-research-centre}

<!-- research-centre:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **Öppnas på kärnnivå 10.** Forskningscentrumet är en modul i din [Skylab](/wiki/03-Mechanics/Skylab.md) och byggs som de andra: 25 Ship Fragments från ditt inventarie (med landat skepp), 25 000 krediter och 500 Thulium. Dess skärm är vyn **Forskning** på Skylab-sidan.
- **Nivå 1 till 10.** En högre nivå ger en större tank och drar mer energi. Den gör inte forskningen snabbare: en teknologi tar lika lång tid på varje nivå.
- **Tanken.** Centret förvarar sin vetenskap i en tank som rymmer 12 h forskning på nivå 1 och 25 % mer för varje nivå (tabellen nedan).
- **Bränsle blir vetenskap.** En resurs du matar in blir vetenskap direkt, som bränsletabellen visar. En forskning bränner 1 vetenskap för varje sekund av sin forskningstid; när tanken är tom väntar den, och den fortsätter när du matar centret igen.
- **En gratis första timme.** Ett nytt centrum startar med 3 600 vetenskap i tanken, alltså 1 h forskning.
- **En i taget.** Centret forskar fram en teknologi i taget, men med knappen Köa kan du ställa upp till 5 till i kö bakom den. Varje teknologi startar av sig själv i samma ögonblick som den före är klar, även när du är borta. Det kostar inget att köa: en teknologi tar sin Dark Matter när den startar, och en köad teknologi kan tas bort gratis.
- **Medan du är borta.** En forskning går på serverns klocka, så den fortsätter när du har loggat ut, tills den är klar eller tanken är tom. Ett energiunderskott eller en uppgradering av centret stoppar den inte.
- **Energi.** Centret drar 25 på nivå 1 och 15 % mer för varje nivå, och det kan inte stängas av.
- **Wipen behåller allt:** dina teknologier, vetenskapen i tanken, den Dark Matter som satts i, en pågående forskning och boosten.
- **Det du har är ditt.** När forskningen kom till spelet fick varje pilot teknologin för varje föremål de redan hade, och de teknologier som krävdes för dem. Ett föremål som når dig senare (en gåva, en kod, en belöning) låser inte upp sin teknologi, med ett undantag: ett Engine II, Engine III, Adaptive Core II eller Adaptive Core III som en kod, ett uppdrag, en inbjudan eller en administratör ger dig låser genast upp sin teknologi och de som den kräver.
- **Under kärnnivå 10** kan du inte forska, så du kan inte tillverka något nytt i Monteringen än. Station-uppdragen leder dig uppför Kärnan.

<!-- research-centre:end -->

**Laserförstärkarna och sista nivån.** Damage Amp, Crit Amp och Penetration Amp på nivå II till IV forskas fram som allt annat som kan tillverkas. Piloter som hade eller hade köat förstärkare när förstärkarserierna kom fick teknologin för var och en av dem och för nivåerna under. Tretton teknologier kräver en teknologi i ett annat träd, Dark Matter Plates, i trädet Resurser, eftersom sista nivån i varje uppgraderingskedja kräver tre plattor: Damage Amp, Crit Amp och Penetration Amp av nivå IV, Absorption Shield Cell och Capacity Shield Cell av nivå IV, Impulse Thruster och Momentum Thruster av nivå IV, Heavy Shield Core, Engine III, Adaptive Core III, Helios Beam, Extra Slots CPU III och Base CPU II. En pilot som har forskat fram en av dem tidigare behåller den, men behöver plattans teknologi för att tillverka dess plattor. Trädet nedan ritar ingen pil för den, men tabellen listar den och kortet i spelet nämner den ([Dark Matter och Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)).

I vyn **Forskning** i din Skylab säger en teknologi mer än en ruta i träden nedan. Håll pekaren över en teknologi så öppnas ett kort med forskningstiden och vetenskapen den bränner och, under dem, vad föremålet **är och gör**: dess sort och nivå i familjen (till exempel den tredje av de fyra Impulse Thruster), dess beskrivning, dess värden så som Hangaren och butiken visar dem (skadan, den kritiska chansen och räckvidden för en laser, sköldkapaciteten, laddningstakten och absorptionen för en sköld, fartökningen och multiplikatorn för en styrraket, skadan, explosionsradien och räckvidden för en raket, vad en drönarformation ger och vad den kostar dig), en liten tabell över nivåerna i dess familj och vad Monteringen sedan kräver för att tillverka det: tiden, krediterna och Thulium samt materialen. Så ser du vad en nivå ger innan du forskar fram den. Klicka på en teknologi för att välja den: kortet bredvid trädet visar samma sak i sin helhet, under knappen **Starta forskning**. Medan en forskning pågår står **Köa** där startknappen annars är: en köad teknologi visar sitt ordningsnummer i trädet, och ett kökort under forskningen som pågår listar dem alla, var och en med ett kryss för att ta bort den. Om nästa inte kan starta (den Dark Matter den behöver finns inte i Centret, eller tanken är tom) väntar kön och säger varför, tills du har rättat till det och trycker på **Starta kön**.

### Tanken på varje nivå {#the-tank-at-every-level}

<!-- research-tank:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Nivå | Tank (vetenskap) | Rymmer forskning för | … med boosten | Energi |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 43 200 | 12 h | 6 h | 25 |
| 2 | 54 000 | 15 h | 7,5 h | 28,7 |
| 3 | 67 500 | 18,8 h | 9,4 h | 33,1 |
| 4 | 84 375 | 23,4 h | 11,7 h | 38 |
| 5 | 105 469 | 29,3 h | 14,6 h | 43,7 |
| 6 | 131 836 | 36,6 h | 18,3 h | 50,3 |
| 7 | 164 795 | 45,8 h | 22,9 h | 57,8 |
| 8 | 205 994 | 57,2 h | 28,6 h | 66,5 |
| 9 | 257 492 | 71,5 h | 35,8 h | 76,5 |
| 10 | 321 865 | 89,4 h | 44,7 h | 87,9 |

<!-- research-tank:end -->

## Bränsle {#fuel}

Du matar centret med resurser, och varje enhet blir vetenskap direkt. Ju mer arbete det kostar att få tag på en enhet, desto mer vetenskap ger den: värdena följer hur svår den är att få, inte dess raritetsetikett. Malmerna är undantaget: en enhet ger mer vetenskap än antalet sekunder som en samlare behöver för att bryta den, så en timmes malm från en samlare mitt i sina nivåer matar ungefär två timmars forskning. Malmerna kommer från Resurslagret i din [Skylab](/wiki/03-Mechanics/Skylab.md#resource-storage); varje annan resurs kommer från ditt inventarie, och ditt skepp måste vara landat. Velkonite Reinforced Plate, Orvium Reinforced Plate, Dark Matter Plate, Dark Matter, krediter och Thulium kan inte brännas; Reinforced Hull Plate kan det. Velkonite och Orvium som en grävmaskins lådor lägger i ditt inventarie kommer till Resurslagret genom [Malmviken](/wiki/03-Mechanics/Skylab.md#ore-bay).

<!-- research-fuel:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Resurs | Raritet | Tas från | Vetenskap per enhet | Enheter för 1 timme |
| :--- | :--- | :--- | ---: | ---: |
| [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) | Vanlig | Ditt inventarie | 5 | 720 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | Vanlig | Ditt inventarie | 5 | 720 |
| [Daraxium](/wiki/06-Items/Resources.md#daraxium) | Vanlig | Ditt inventarie | 7 | 515 |
| [Nyxite](/wiki/06-Items/Resources.md#nyxite) | Vanlig | Ditt inventarie | 7 | 515 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | Vanlig | Ditt inventarie | 8 | 450 |
| [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) | Vanlig | Ditt inventarie | 33 | 110 |
| [Power Core](/wiki/06-Items/Resources.md#power-core) | Ovanlig | Ditt inventarie | 100 | 36 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | Ovanlig | Resurslager | 210 | 18 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | Sällsynt | Resurslager | 321 | 12 |
| [Ancient Control Unit](/wiki/06-Items/Resources.md#ancient-control-unit) | Sällsynt | Ditt inventarie | 650 | 6 |

Sista kolumnen är antalet enheter som driver en timmes forskning utan boosten, avrundat uppåt; med boosten är det 2 gånger så många.

<!-- research-fuel:end -->

## Thulium-boosten {#the-thulium-boost}

<!-- research-boost:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **5 000 Thulium** köper en boost: centret forskar **2 gånger snabbare i 24 timmar**.
- Den **bränner också vetenskap 2 gånger så snabbt**, så en boost köper tid och aldrig bränsle: en teknologi bränner samma vetenskap, med eller utan boost.
- En boost börjar i samma ögonblick du köper den och går på klockan oavsett om tanken har bränsle eller inte, så köp den medan en forskning pågår. Centret nekar en boost när inget forskas fram.
- Boostar läggs ihop: köper du en medan en annan pågår förlängs dess slut med 24 timmar, högst 72 timmar framåt. En boost hör till ditt forskningscentrum, inte till en enskild forskning.

Vad en boost gör med tiden för en forskning, med boosten på från start:

| Forskningstid | Med boost | Boostar för hela | Thulium |
| :--- | :--- | ---: | ---: |
| 30 min | 15 min | 1 | 5 000 |
| 3 h | 1 h 30 min | 1 | 5 000 |
| 6 h | 3 h | 1 | 5 000 |
| 10 h | 5 h | 1 | 5 000 |
| 1 d | 12 h | 1 | 5 000 |
| 2 d | 1 d | 1 | 5 000 |

<!-- research-boost:end -->

## Dark Matter

Teknologierna högst upp i trädet kräver också Dark Matter. Den kommer från [det svarta hålet](/wiki/03-Mechanics/Black-Hole.md#dark-matter), där en N.I.K.E.-raket som når det lämnar något, och då och då från en Dormant Pulse i [Dormant-svärmen](/wiki/05-Swarms/Dormant-Swarm.md).

<!-- research-dark-matter:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **10 Dark Matter** för var och en av de 16 teknologierna i tabellen nedan, utöver vetenskapen: sätt i den i forskningscentrumet (från ditt inventarie, med landat skepp) innan du startar, så tar forskningen den när den börjar.
- **Regeln:** ett föremål med raritet Episk eller högre vars forskning tar 10 h eller mer. N.I.K.E., som är sättet att få fram Dark Matter, behöver den aldrig.
- **Drönarformationer** står utanför regeln: varje formationsforskning kräver Dark Matter, 5, 13 eller 20 efter styrka, som tabellen visar.
- **Skrovpansar** står också utanför regeln: dess två forskningar kräver mer, 25 Dark Matter för en dags forskning och 40 för två dagar, som tabellen visar.
- **Avbryter du en forskning** går den Dark Matter du satte i för den tillbaka till centret. Framsteget och vetenskapen som redan bränts gör det inte.
- Alla tillsammans kräver 414 Dark Matter.

| Teknologi | Raritet | Forskningstid | Dark Matter |
| :--- | :--- | :--- | ---: |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | Episk | 10 h | 10 |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | Episk | 10 h | 10 |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | Episk | 10 h | 10 |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | Episk | 10 h | 10 |
| [Starfire-III](/wiki/06-Items/Lasers.md#lasers) | Mytisk | 1 d | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | Mytisk | 1 d | 10 |
| [Damage Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Episk | 10 h | 10 |
| [Crit Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Episk | 10 h | 10 |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | Episk | 1 d | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | Episk | 1 d | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | Mytisk | 2 d | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | Mytisk | 1 d | 10 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | Legendarisk | 1 d | 10 |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | Episk | 1 d | 10 |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | Episk | 1 d | 10 |
| [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Episk | 10 h | 5 |
| [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Episk | 1 d | 13 |
| [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Episk | 10 h | 5 |
| [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Mytisk | 2 d | 20 |
| [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Episk | 10 h | 5 |
| [Ballista Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Episk | 1 d | 13 |
| [Stiletto Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Mytisk | 2 d | 20 |
| [Rampart Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Mytisk | 2 d | 20 |
| [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Episk | 1 d | 13 |
| [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Episk | 10 h | 5 |
| [Culler Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Episk | 1 d | 13 |
| [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Episk | 1 d | 13 |
| [Auger Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Episk | 1 d | 13 |
| [Cordon Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Episk | 1 d | 13 |
| [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Episk | 10 h | 5 |
| [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Episk | 1 d | 13 |
| [Penetration Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Episk | 10 h | 10 |
| [Hull Plating II](/wiki/06-Items/Hull-Plating.md#the-three-platings) | Sällsynt | 1 d | 25 |
| [Hull Plating III](/wiki/06-Items/Hull-Plating.md#the-three-platings) | Episk | 2 d | 40 |

<!-- research-dark-matter:end -->

## Teknologiträdet {#the-technology-tree}

Varje ruta är en teknologi: föremålet den låter dig tillverka, med forskningstiden under namnet (klockan) och, där den kräver Dark Matter, Dark Matter-märket. En pil leder från en teknologi till den som behöver den, och den forskar du fram först; en ruta utan pil kan forskas fram direkt. Håll pekaren över en ruta för att se forskningstiden, vetenskapen den bränner och vad Monteringen sedan kräver för föremålet, och klicka för att öppna föremålets sida. Träden ritas utifrån spelets egna data. Två av träden, **Försvar** och **Anfall och rörlighet**, rymmer de sexton [drönarformationerna](/wiki/03-Mechanics/Formations.md).

<!-- research-tree:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

### Framdrivning och fart {#tree-propulsion}

```tree research
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Engine I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Adaptive Core II | hybrid-generator, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Adaptive Core I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core III | hybrid-generator, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Adaptive Core II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-

Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
Engine II => Engine III
Adaptive Core II => Adaptive Core III
```

### Sköldar och försvar {#tree-shields}

```tree research
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cores

Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```

### Lasrar och ammunition {#tree-lasers}

```tree research
Quantum Laser III | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Quantum Laser II, 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-III | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser III, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-III, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Damage Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Crit Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Damage Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Damage Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Crit Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Crit Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Penetration Amp I, 20 Daraxium, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Penetration Amp II, 1 Power Core, 30 Nyxite, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp IV | laser-amp, epic | craft 1200 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Penetration Amp III, 1 Power Core, 30 Cataclysite, 40 Quorvium, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-

Quantum Laser III => Starfire-III => Helios Beam
Damage Amp II => Damage Amp III => Damage Amp IV
Crit Amp II => Crit Amp III => Crit Amp IV
Penetration Amp II => Penetration Amp III => Penetration Amp IV
```

### Boosters {#tree-boosters}

```tree research
Laser Damage Booster II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
```

### Drönare {#tree-drones}

```tree research
Master Drone | drone, rare | craft 40000 Thulium, 60 s | research 36000 s, 36000 science | 1 Slave Drone, 100 Ship Fragment | /wiki/06-Items/Drones.md#available-drones
```

### Skepp {#tree-ships}

```tree research
Paragon | ship, rare | craft 1500 Thulium, 900 s | research 21600 s, 21600 science | 120 Ship Fragment, 20 Reinforced Hull Plate, 5 Power Core | /wiki/02-Ships/Paragon.md
Ironclad | ship, epic | craft 10500 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit | /wiki/02-Ships/Ironclad.md
Storm | ship, epic | craft 15000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit | /wiki/02-Ships/Storm.md
Wraith | ship, mythical | craft 20000 Thulium, 900 s | research 172800 s, 172800 science, 10 Dark Matter | 300 Ship Fragment, 50 Reinforced Hull Plate, 15 Power Core, 3 Ancient Control Unit | /wiki/02-Ships/Wraith.md
```

### Resurser {#tree-resources}

```tree research
Dark Matter Plate | resource, mythical | craft 250 Thulium, 120 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Velkonite Reinforced Plate, 1 Orvium Reinforced Plate, 5 Dark Matter | /wiki/06-Items/Resources.md#dark-matter-plate
```

### Raketer {#tree-rockets}

```tree research
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
```

### CPU:er {#tree-cpus}

```tree research
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 6 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 2 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Extras.md#base-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu

Extra Slots CPU I => Extra Slots CPU II => Extra Slots CPU III
Base CPU I => Base CPU II => Jump CPU
```

### Försvar {#tree-defence}

```tree research
Testudo Formation | formation, epic | craft 7500 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Adamant Formation | formation, epic | craft 9000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Rampart Formation | formation, mythical | craft 38500 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Sanctum Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Redoubt Formation | formation, epic | craft 21000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Cordon Formation | formation, epic | craft 21500 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations

Testudo Formation => Sanctum Formation => Rampart Formation
Adamant Formation => Redoubt Formation => Cordon Formation
```

### Anfall och rörlighet {#tree-strike-mobility}

```tree research
Bodkin Formation | formation, epic | craft 21000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Asterism Formation | formation, epic | craft 7000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Gemini Formation | formation, mythical | craft 38000 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Ballista Formation | formation, epic | craft 24000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Stiletto Formation | formation, mythical | craft 46000 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Shrike Formation | formation, epic | craft 8500 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Culler Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Auger Formation | formation, epic | craft 20500 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Centurion Formation | formation, epic | craft 8000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Gyre Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations

Asterism Formation => Bodkin Formation => Ballista Formation
Gemini Formation => Stiletto Formation
Centurion Formation => Shrike Formation => Culler Formation
Gyre Formation => Auger Formation
```

### Skrovpansar {#tree-hull-plating}

```tree research
Hull Plating II | hull-plating, rare | craft 2500 Thulium, 300 s | research 86400 s, 86400 science, 25 Dark Matter | 1 Hull Plating I, 150 Ship Fragment, 20 Reinforced Hull Plate, 6 Power Core, 5 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating III | hull-plating, epic | craft 4000 Thulium, 600 s | research 172800 s, 172800 science, 40 Dark Matter | 1 Hull Plating II, 300 Ship Fragment, 40 Reinforced Hull Plate, 12 Power Core, 1 Ancient Control Unit, 8 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings

Hull Plating II => Hull Plating III
```


<!-- research-tree:end -->

## Skeppsdesigner och pansarplatser {#ship-technologies}

Skeppsfamiljen i forskningsvyn i din Skylab har två slags teknologier som inte är tillverkningar. Trädet ovan utelämnar dem, eftersom det de öppnar är en plats eller en ombyggnad, inte ett föremål.

- **Pansarplatser.** En teknologi för varje [pansarplats](/wiki/06-Items/Hull-Plating.md#hull-plate-slots) på de fyra skeppen du tillverkar. Var och en kommer efter den förra, den första efter skeppets egen teknologi. I spelet är ett skepps platser ett enda kort med en prick för varje plats.
- **Skeppsdesigner.** En teknologi för varje [design](/wiki/03-Mechanics/Ship-Designs.md). Var och en kräver teknologin för sitt skepp och den för Dark Matter Plate.

Deras tider, deras Dark Matter och summorna står på sidan [Skeppsdesigner](/wiki/03-Mechanics/Ship-Designs.md#the-technologies).

## Alla teknologier {#all-the-technologies}

<!-- research-technologies:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Teknologi | Kräver först | Klass | Forskningstid | Vetenskap | Dark Matter |
| :--- | :--- | :--- | ---: | ---: | ---: |
| [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 min | 1 800 | – |
| [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 h | 10 800 | – |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 h | 36 000 | 10 |
| [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 min | 1 800 | – |
| [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 h | 10 800 | – |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 h | 36 000 | 10 |
| [Engine III](/wiki/06-Items/Propulsion.md#engines) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Engine II](/wiki/06-Items/Propulsion.md#engines) | B | 3 h | 10 800 | – |
| [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 min | 1 800 | – |
| [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 h | 10 800 | – |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10 h | 36 000 | 10 |
| [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 min | 1 800 | – |
| [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 h | 10 800 | – |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10 h | 36 000 | 10 |
| [Heavy Shield Core](/wiki/06-Items/Shields.md#shield-cores) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | B | 3 h | 10 800 | – |
| [Quantum Laser III](/wiki/06-Items/Lasers.md#lasers) | – | B | 3 h | 10 800 | – |
| [Starfire-III](/wiki/06-Items/Lasers.md#lasers) | [Quantum Laser III](/wiki/06-Items/Lasers.md#lasers) | D | 1 d | 86 400 | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Starfire-III](/wiki/06-Items/Lasers.md#lasers) | D | 1 d | 86 400 | 10 |
| [Damage Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Damage Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10 h | 36 000 | 10 |
| [Crit Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Crit Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10 h | 36 000 | 10 |
| [Laser Damage Booster II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 h | 10 800 | – |
| [Shield Wall Booster II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 h | 10 800 | – |
| [Hull Plating Booster II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 h | 10 800 | – |
| [Master Drone](/wiki/06-Items/Drones.md#available-drones) | – | C | 10 h | 36 000 | – |
| [Paragon](/wiki/02-Ships/Paragon.md) | – | B | 6 h | 21 600 | – |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | – | D | 1 d | 86 400 | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | – | D | 1 d | 86 400 | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | – | D | 2 d | 172 800 | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | – | D | 1 d | 86 400 | 10 |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | B | 3 h | 10 800 | – |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | D | 1 d | 86 400 | 10 |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | – | A | 30 min | 1 800 | – |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | C | 10 h | 36 000 | – |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | D | 1 d | 86 400 | 10 |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | – | B | 3 h | 10 800 | – |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10 h | 36 000 | – |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | D | 1 d | 86 400 | 10 |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | – | B | 6 h | 21 600 | – |
| [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 h | 36 000 | 5 |
| [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 d | 86 400 | 13 |
| [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 h | 36 000 | 5 |
| [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | D | 2 d | 172 800 | 20 |
| [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 h | 36 000 | 5 |
| [Ballista Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 d | 86 400 | 13 |
| [Stiletto Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 2 d | 172 800 | 20 |
| [Rampart Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 2 d | 172 800 | 20 |
| [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 d | 86 400 | 13 |
| [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | C | 10 h | 36 000 | 5 |
| [Culler Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 d | 86 400 | 13 |
| [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 d | 86 400 | 13 |
| [Auger Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 d | 86 400 | 13 |
| [Cordon Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 d | 86 400 | 13 |
| [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 h | 36 000 | 5 |
| [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | D | 1 d | 86 400 | 13 |
| [Damage Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30 min | 1 800 | – |
| [Damage Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Damage Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3 h | 10 800 | – |
| [Crit Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30 min | 1 800 | – |
| [Crit Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Crit Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3 h | 10 800 | – |
| [Penetration Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30 min | 1 800 | – |
| [Penetration Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Penetration Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3 h | 10 800 | – |
| [Penetration Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Penetration Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10 h | 36 000 | 10 |
| [Hull Plating II](/wiki/06-Items/Hull-Plating.md#the-three-platings) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | D | 1 d | 86 400 | 25 |
| [Hull Plating III](/wiki/06-Items/Hull-Plating.md#the-three-platings) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Hull Plating II](/wiki/06-Items/Hull-Plating.md#the-three-platings) | D | 2 d | 172 800 | 40 |
| [Engine II](/wiki/06-Items/Propulsion.md#engines) | – | A | 30 min | 1 800 | – |
| [Adaptive Core II](/wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-) | – | A | 30 min | 1 800 | – |
| [Adaptive Core III](/wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-) | [Adaptive Core II](/wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | B | 3 h | 10 800 | – |

Klasserna efter forskningstid:

| Klass | Forskningstid | Teknologier | En efter en | Vetenskap | Dark Matter |
| :--- | :--- | ---: | ---: | ---: | ---: |
| A | 30 min | 10 | 5 h | 18 000 | 0 |
| B | 3 h till 6 h | 18 | 2 d 12 h | 216 000 | 0 |
| C | 10 h | 15 | 6 d 6 h | 540 000 | 95 |
| D | 1 d till 2 d | 22 | 27 d | 2 332 800 | 319 |
| Alla |  | 65 | 35 d 23 h | 3 106 800 | 414 |

Framforskat en efter en tar hela trädet 35 d 23 h. Med boosten på hela tiden tar det 17 d 23 h 30 min, alltså 18 boostar och 90 000 Thulium; vetenskapen är densamma.

<!-- research-technologies:end -->

## CPU:erna {#the-cpus}

De nya CPU:erna forskas också fram här och tillverkas sedan i Monteringen. Samma tabell och samma anteckningar finns på sidan [Extrautrustning](/wiki/06-Items/Extras.md#research-cpus).

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | Forskningstid | Kräver först | Thulium för tillverkning | Tillverkningstid |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 min | – | 12 000 | 5 min |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10 h | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 000 | 10 min |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1 d | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75 000 | 15 min |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3 h | – | 8 000 | 5 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10 h | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | 20 000 | 10 min |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1 d | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40 000 | 15 min |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6 h | – | 15 000 | 10 min |

Ingen av dem säljs i butiken: forska fram teknologin och tillverka sedan CPU:n i Monteringen. Håll pekaren över en CPU i trädet för att se vad Monteringen kräver för den.

### Extra Slots CPUs

- **Vad de gör.** Extra Slots CPU I, II och III ger varje skepp 3, 5 och 7 extraplatser till, alltså 6, 8 och 10 sammanlagt på ett skepp som har 3 egna och 5, 7 och 9 på ett som har 2. En högre CPU ersätter den förra: II läggs inte till I.
- **Installeras, bärs inte.** En Extra Slots CPU är inte ett föremål: när du hämtar den i Monteringen installerar den sig i din Skylab, för varje skepp i båda konfigurationerna, och tar ingen plats. Den finns kvar efter wipen.
- **I ordning.** Tillverka dem en efter en: II först när I är installerad, III först när II är installerad; till dess säger Monteringen vilken du ska installera först. De tre kostar 117 000 Thulium sammanlagt: 12 000, 30 000 och 75 000.

### Jump CPU

- **Vad den gör.** Den hoppar ditt skepp till vilken koncernsektor som helst i din värld, både din egen koncerns och de andras, hemsektorerna inräknade (`M`, `T` och `G`, sektor 1 till 4), för **500 Thulium** per hopp. Antalet användningar är obegränsat: du betalar bara Thulium. Den leder aldrig till en farosektor (`DS`) eller en neutral sektor (`N`).
- **Hoppet.** Tryck på platsen JMP, välj sektorn på kartan Stjärnsystem och bekräfta: skeppet laddar i 5 sekunder och kommer sedan fram vid en port i den sektorn, skyddat som efter ett hopp genom en port. CPU:n svalnar i 30 sekunder efter att du har kommit fram.
- **Inte i strid.** Den kan inte starta inom 10 sekunder efter ett skott eller en träff, och ett skott eller en träff under laddningen avbryter hoppet; då betalas inget. Du kan inte hoppa kamouflerad.
- **Inte från en neutral sektor:** en pilot i en neutral sektor, eller utan koncern, kan inte använda den.
- Den får lämna en farosektor när du inte är i strid.

### Base CPUs

- **Vad de gör.** De teleporterar ditt skepp till din koncerns bas, in i den säkra zonen runt dess station (`M-1`, `T-1` eller `G-1`, sektorn med Mission Control), utan Thulium-kostnad. Du startar dem från platsen BSE i snabbfältet.
- **Inte i strid.** En laddning på 10 sekunder, samma för båda. Den kan inte starta inom 10 sekunder efter ett skott eller en träff, inte medan du är kamouflerad och inte när du redan är inne i den säkra zonen vid din bas, och ett skott eller en träff under laddningen avbryter den.

| CPU | Användningar | Nedkylning |
| :--- | ---: | ---: |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 10 | 10 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 25 | 5 min |

- **Förbrukas, laddas inte om.** Varje användning tar en av CPU:ns användningar, och en CPU utan användningar kvar är borta: tillverka en ny. Är båda monterade används den bättre (II) först.

### Auto-Repair CPU

- **Vad den gör.** Den skickar ut den Repair Drone som sitter i dina extraplatser av sig själv, så fort du hade kunnat skicka ut den för hand: ditt skrov är inte fullt, drönaren är inte redan ute och det har gått 10 sekunder sedan den senaste träffen. Det finns ingen skrovnivå att ställa in.
- Den tar en egen extraplats och gör ingenting utan en Repair Drone i en extraplats i samma konfiguration. Den skickar aldrig ut en Repair Drone i en förmågeplats (den är knappen Emergency Repair).
- **Stoppar du drönaren för hand** låter CPU:n den vara tills ditt skrov är fullt igen, eller tills du själv skickar ut drönaren.


<!-- research-cpus:end -->
