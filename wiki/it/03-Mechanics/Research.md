<!-- wiki-i18n source: ee1ab2403a7af6d8 -->
<!-- wiki-i18n title: Ricerca -->
# Ricerca {#research}

Il **Centro ricerche** è il laboratorio del tuo [Skylab](/wiki/03-Mechanics/Skylab.md). Gli dai risorse, le trasforma in **scienza**, e la scienza ricerca **tecnologie**. Ogni creazione nell’[Assemblaggio](/wiki/06-Items/Overview.md#upgrading-modules) richiede prima la sua tecnologia: una nave, un laser, un propulsore o una CPU non si possono creare finché non sono stati ricercati.

Questa pagina riunisce l’intero albero delle tecnologie con il tempo di ciascuna, la scienza che dà ogni risorsa, il boost di Thulium, la regola della Dark Matter e le nuove CPU. I suoi numeri sono letti dai dati stessi del gioco, quindi sono sempre quelli del gioco.

![The Research view filtered to the Defence tree: the shield and hull formations, each a technology with its Dark Matter](../../img/wiki-img/shots/research-formations.jpg)

## Il Centro ricerche {#the-research-centre}

<!-- research-centre:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **Si sblocca al livello 10 del Nucleo.** Il Centro ricerche è un modulo del tuo [Skylab](/wiki/03-Mechanics/Skylab.md), che si costruisce come gli altri: 25 Ship Fragment dal tuo inventario (con la nave atterrata), 25.000 crediti e 500 Thulium. Il suo schermo è la vista **Ricerca** della pagina dello Skylab.
- **Livelli da 1 a 10.** Un livello più alto dà un serbatoio più grande e consuma più energia. Non rende la ricerca più veloce: una tecnologia richiede lo stesso tempo a ogni livello.
- **Il serbatoio.** Il Centro tiene la sua scienza in un serbatoio che al livello 1 contiene 12 h di ricerca e, a ogni livello, 25% in più (vedi la tabella qui sotto).
- **Dal carburante alla scienza.** Una risorsa che inserisci diventa subito scienza, come mostra la tabella del carburante. Una ricerca brucia 1 di scienza per ogni secondo del suo tempo di ricerca; con il serbatoio vuoto aspetta, e riprende quando alimenti il Centro.
- **Una prima ora gratis.** Un nuovo Centro parte con 3.600 di scienza nel serbatoio, cioè 1 h di ricerca.
- **Una alla volta.** Il Centro ricerca una tecnologia alla volta. Non c’è nessuna coda.
- **Mentre sei via.** Una ricerca segue l’orologio del server, quindi prosegue dopo che ti sei disconnesso, finché non è finita o il serbatoio non è vuoto. Un blackout o un potenziamento del Centro non la fermano.
- **Energia.** Il Centro consuma 25 al livello 1 e, a ogni livello, 15% in più, e non si può spegnere.
- **Il reset conserva tutto:** le tue tecnologie, la scienza nel serbatoio, la Dark Matter inserita, una ricerca in corso e il boost.
- **Ciò che possiedi è tuo.** Quando la ricerca è arrivata nel gioco, ogni pilota ha ricevuto la tecnologia di ogni oggetto che già possedeva, e le tecnologie che quelli richiedevano. Un oggetto che ti arriva dopo (un regalo, un codice, una ricompensa) non sblocca la sua tecnologia.
- **Sotto il livello 10 del Nucleo** non puoi ricercare, quindi non puoi ancora creare nulla di nuovo nell’Assemblaggio. Le missioni Stazione ti accompagnano a salire con il Nucleo.

<!-- research-centre:end -->

### Il serbatoio a ogni livello {#the-tank-at-every-level}

<!-- research-tank:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Livello | Serbatoio (scienza) | Contiene ricerca per | … con il boost | Energia |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 43.200 | 12 h | 6 h | 25 |
| 2 | 54.000 | 15 h | 7,5 h | 28,7 |
| 3 | 67.500 | 18,8 h | 9,4 h | 33,1 |
| 4 | 84.375 | 23,4 h | 11,7 h | 38 |
| 5 | 105.469 | 29,3 h | 14,6 h | 43,7 |
| 6 | 131.836 | 36,6 h | 18,3 h | 50,3 |
| 7 | 164.795 | 45,8 h | 22,9 h | 57,8 |
| 8 | 205.994 | 57,2 h | 28,6 h | 66,5 |
| 9 | 257.492 | 71,5 h | 35,8 h | 76,5 |
| 10 | 321.865 | 89,4 h | 44,7 h | 87,9 |

<!-- research-tank:end -->

## Carburante {#fuel}

Alimenti il Centro con le risorse, e ogni unità diventa subito scienza. Più lavoro serve per ottenere un’unità, più scienza dà: i valori seguono quanto è difficile ottenerla, non la sua etichetta di rarità. I minerali fanno eccezione: un’unità dà più scienza dei secondi che un collettore impiega a estrarla, quindi un’ora del minerale di un collettore a metà dei suoi livelli alimenta circa due ore di ricerca. I minerali vengono dal Magazzino risorse del tuo [Skylab](/wiki/03-Mechanics/Skylab.md#resource-storage); ogni altra risorsa viene dal tuo inventario, e la tua nave deve essere atterrata. La Velkonite Reinforced Plate, l’Orvium Reinforced Plate, la Dark Matter Plate, la Dark Matter, i crediti e il Thulium non si possono bruciare; la Reinforced Hull Plate sì.

<!-- research-fuel:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Risorsa | Rarità | Prelevata da | Scienza per unità | Unità per 1 ora |
| :--- | :--- | :--- | ---: | ---: |
| [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) | Comune | Il tuo inventario | 5 | 720 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | Comune | Il tuo inventario | 5 | 720 |
| [Daraxium](/wiki/06-Items/Resources.md#daraxium) | Comune | Il tuo inventario | 7 | 515 |
| [Nyxite](/wiki/06-Items/Resources.md#nyxite) | Comune | Il tuo inventario | 7 | 515 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | Comune | Il tuo inventario | 8 | 450 |
| [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) | Comune | Il tuo inventario | 33 | 110 |
| [Power Core](/wiki/06-Items/Resources.md#power-core) | Non comune | Il tuo inventario | 100 | 36 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | Non comune | Magazzino risorse | 210 | 18 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | Raro | Magazzino risorse | 321 | 12 |
| [Ancient Control Unit](/wiki/06-Items/Resources.md#ancient-control-unit) | Raro | Il tuo inventario | 650 | 6 |

L’ultima colonna è il numero di unità che alimentano un’ora di ricerca senza il boost, arrotondato per eccesso; con il boost sono 2 volte tante.

<!-- research-fuel:end -->

## Il boost di Thulium {#the-thulium-boost}

<!-- research-boost:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **5.000 Thulium** comprano un boost: il Centro ricerca **2 volte più in fretta per 24 ore**.
- Brucia anche **la scienza 2 volte più in fretta**, quindi un boost compra tempo e mai carburante: una tecnologia brucia la stessa scienza, con il boost o senza.
- Un boost parte nel momento in cui lo compri e segue l’orologio, che il serbatoio abbia carburante o no, quindi compralo mentre una ricerca è in corso. Il Centro lo rifiuta quando non si sta ricercando nulla.
- I boost si sommano: comprarne uno mentre un altro è in corso aggiunge 24 ore alla sua fine, fino a 72 ore in anticipo. Un boost appartiene al tuo Centro ricerche, non a una singola ricerca.

Che cosa fa un boost al tempo di una ricerca, con il boost attivo dal suo inizio:

| Tempo di ricerca | Con il boost | Boost per tutta la ricerca | Thulium |
| :--- | :--- | ---: | ---: |
| 30 min | 15 min | 1 | 5.000 |
| 3 h | 1 h 30 min | 1 | 5.000 |
| 6 h | 3 h | 1 | 5.000 |
| 10 h | 5 h | 1 | 5.000 |
| 1 g | 12 h | 1 | 5.000 |
| 2 g | 1 g | 1 | 5.000 |

<!-- research-boost:end -->

## Dark Matter

Le tecnologie in cima all’albero richiedono anche Dark Matter. Viene dal [buco nero](/wiki/03-Mechanics/Black-Hole.md#dark-matter), dove un razzo N.I.K.E. che lo raggiunge ne lascia un po’, e ogni tanto da un Dormant Pulse dello [Sciame Dormant](/wiki/05-Swarms/Dormant-Swarm.md).

<!-- research-dark-matter:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **10 Dark Matter** per ciascuna delle 15 tecnologie della tabella qui sotto, oltre alla scienza: inseriscila nel Centro ricerche (dal tuo inventario, con la nave atterrata) prima di iniziare, e la ricerca la prende quando parte.
- **La regola:** un oggetto di rarità Epico o superiore la cui ricerca dura 10 h o più. La N.I.K.E., con cui si produce la Dark Matter, non ne ha mai bisogno.
- **Le formazioni di droni** sono fuori dalla regola: ogni ricerca di formazione richiede Dark Matter, 5, 13 o 20 in base alla potenza, come mostra la tabella.
- **Se annulli una ricerca,** la Dark Matter che hai inserito per essa torna al Centro. L’avanzamento e la scienza già bruciata, no.
- Tutte insieme richiedono 339 Dark Matter.

| Tecnologia | Rarità | Tempo di ricerca | Dark Matter |
| :--- | :--- | :--- | ---: |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | Epico | 10 h | 10 |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | Epico | 10 h | 10 |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | Epico | 10 h | 10 |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | Epico | 10 h | 10 |
| [Starfire-3](/wiki/06-Items/Lasers.md#lasers) | Mitico | 1 g | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | Mitico | 1 g | 10 |
| [Nova Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Epico | 10 h | 10 |
| [Apex Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Epico | 10 h | 10 |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | Epico | 1 g | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | Epico | 1 g | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | Mitico | 2 g | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | Mitico | 1 g | 10 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | Leggendario | 1 g | 10 |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | Epico | 1 g | 10 |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | Epico | 1 g | 10 |
| [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epico | 10 h | 5 |
| [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epico | 1 g | 13 |
| [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epico | 10 h | 5 |
| [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Mitico | 2 g | 20 |
| [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epico | 10 h | 5 |
| [Ballista Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epico | 1 g | 13 |
| [Stiletto Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Mitico | 2 g | 20 |
| [Rampart Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Mitico | 2 g | 20 |
| [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epico | 1 g | 13 |
| [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epico | 10 h | 5 |
| [Culler Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epico | 1 g | 13 |
| [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epico | 1 g | 13 |
| [Auger Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epico | 1 g | 13 |
| [Cordon Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epico | 1 g | 13 |
| [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epico | 10 h | 5 |
| [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Epico | 1 g | 13 |

<!-- research-dark-matter:end -->

## L’albero delle tecnologie {#the-technology-tree}

Ogni riquadro è una tecnologia: l’oggetto che ti permette di creare, con il tempo di ricerca sotto il nome (l’orologio) e, dove serve Dark Matter, il distintivo della Dark Matter. Una freccia va da una tecnologia a quella che ne ha bisogno, che ricerchi prima; un riquadro senza frecce si può ricercare subito. Passa il puntatore su un riquadro per vedere il tempo di ricerca, la scienza che brucia e ciò che l’Assemblaggio chiede poi per l’oggetto, e clicca per aprire la pagina dell’oggetto. Gli alberi sono disegnati dai dati stessi del gioco. Due degli alberi, **Difesa** e **Attacco e mobilità**, contengono le sedici [formazioni di droni](/wiki/03-Mechanics/Formations.md).

<!-- research-tree:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

### Propulsione e velocità {#tree-propulsion}

```tree research
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines

Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```

### Scudi e difesa {#tree-shields}

```tree research
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cores

Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```

### Laser e munizioni {#tree-lasers}

```tree research
Quantum Laser 3 | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-3 | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser 3, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-3, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Nova Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Pulse Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Apex Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Prism Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-

Quantum Laser 3 => Starfire-3 => Helios Beam
```

### Booster {#tree-boosters}

```tree research
Damage Amp II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
```

### Droni {#tree-drones}

```tree research
Master Drone | drone, rare | craft 40000 Thulium, 60 s | research 36000 s, 36000 science | 1 Slave Drone, 100 Ship Fragment | /wiki/06-Items/Drones.md#available-drones
```

### Navi {#tree-ships}

```tree research
Paragon | ship, rare | craft 1500 Thulium, 900 s | research 21600 s, 21600 science | 120 Ship Fragment, 20 Reinforced Hull Plate, 5 Power Core | /wiki/02-Ships/Paragon.md
Ironclad | ship, epic | craft 10500 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit | /wiki/02-Ships/Ironclad.md
Storm | ship, epic | craft 15000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit | /wiki/02-Ships/Storm.md
Wraith | ship, mythical | craft 20000 Thulium, 900 s | research 172800 s, 172800 science, 10 Dark Matter | 300 Ship Fragment, 50 Reinforced Hull Plate, 15 Power Core, 3 Ancient Control Unit | /wiki/02-Ships/Wraith.md
```

### Risorse {#tree-resources}

```tree research
Dark Matter Plate | resource, mythical | craft 250 Thulium, 120 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Velkonite Reinforced Plate, 1 Orvium Reinforced Plate, 5 Dark Matter | /wiki/06-Items/Resources.md#dark-matter-plate
```

### Razzi {#tree-rockets}

```tree research
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
```

### CPU {#tree-cpus}

```tree research
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 20 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 8 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu

Extra Slots CPU I => Extra Slots CPU II => Extra Slots CPU III
Base CPU I => Base CPU II => Jump CPU
```

### Difesa {#tree-defence}

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

### Attacco e mobilità {#tree-strike-mobility}

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


<!-- research-tree:end -->

## Tutte le tecnologie {#all-the-technologies}

<!-- research-technologies:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Tecnologia | Richiede prima | Classe | Tempo di ricerca | Scienza | Dark Matter |
| :--- | :--- | :--- | ---: | ---: | ---: |
| [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 min | 1.800 | – |
| [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 h | 10.800 | – |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 h | 36.000 | 10 |
| [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 min | 1.800 | – |
| [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 h | 10.800 | – |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 h | 36.000 | 10 |
| [Engine III](/wiki/06-Items/Propulsion.md#engines) | – | B | 3 h | 10.800 | – |
| [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 min | 1.800 | – |
| [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 h | 10.800 | – |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | C | 10 h | 36.000 | 10 |
| [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 min | 1.800 | – |
| [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 h | 10.800 | – |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | C | 10 h | 36.000 | 10 |
| [Heavy Shield Core](/wiki/06-Items/Shields.md#shield-cores) | – | B | 3 h | 10.800 | – |
| [Quantum Laser 3](/wiki/06-Items/Lasers.md#lasers) | – | B | 3 h | 10.800 | – |
| [Starfire-3](/wiki/06-Items/Lasers.md#lasers) | [Quantum Laser 3](/wiki/06-Items/Lasers.md#lasers) | D | 1 g | 86.400 | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | [Starfire-3](/wiki/06-Items/Lasers.md#lasers) | D | 1 g | 86.400 | 10 |
| [Nova Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | C | 10 h | 36.000 | 10 |
| [Apex Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | C | 10 h | 36.000 | 10 |
| [Damage Amp II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 h | 10.800 | – |
| [Shield Wall II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 h | 10.800 | – |
| [Hull Plating II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 h | 10.800 | – |
| [Master Drone](/wiki/06-Items/Drones.md#available-drones) | – | C | 10 h | 36.000 | – |
| [Paragon](/wiki/02-Ships/Paragon.md) | – | B | 6 h | 21.600 | – |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | – | D | 1 g | 86.400 | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | – | D | 1 g | 86.400 | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | – | D | 2 g | 172.800 | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | – | D | 1 g | 86.400 | 10 |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | B | 3 h | 10.800 | – |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | D | 1 g | 86.400 | 10 |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | – | A | 30 min | 1.800 | – |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | C | 10 h | 36.000 | – |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | D | 1 g | 86.400 | 10 |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | – | B | 3 h | 10.800 | – |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | C | 10 h | 36.000 | – |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | D | 1 g | 86.400 | 10 |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | – | B | 6 h | 21.600 | – |
| [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 h | 36.000 | 5 |
| [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 g | 86.400 | 13 |
| [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 h | 36.000 | 5 |
| [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | D | 2 g | 172.800 | 20 |
| [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 h | 36.000 | 5 |
| [Ballista Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 g | 86.400 | 13 |
| [Stiletto Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 2 g | 172.800 | 20 |
| [Rampart Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 2 g | 172.800 | 20 |
| [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 g | 86.400 | 13 |
| [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | C | 10 h | 36.000 | 5 |
| [Culler Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 g | 86.400 | 13 |
| [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 g | 86.400 | 13 |
| [Auger Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 g | 86.400 | 13 |
| [Cordon Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 g | 86.400 | 13 |
| [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 h | 36.000 | 5 |
| [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | D | 1 g | 86.400 | 13 |

Le classi, per tempo di ricerca:

| Classe | Tempo di ricerca | Tecnologie | Una dopo l’altra | Scienza | Dark Matter |
| :--- | :--- | ---: | ---: | ---: | ---: |
| A | 30 min | 5 | 2 h 30 min | 9.000 | 0 |
| B | da 3 h a 6 h | 14 | 2 g | 172.800 | 0 |
| C | 10 h | 14 | 5 g 20 h | 504.000 | 85 |
| D | da 1 g a 2 g | 20 | 24 g | 2.073.600 | 254 |
| Tutte |  | 53 | 31 g 22 h 30 min | 2.759.400 | 339 |

Ricercato una tecnologia dopo l’altra, l’intero albero richiede 31 g 22 h 30 min. Con il boost sempre attivo richiede 15 g 23 h 15 min, cioè 16 boost e 80.000 Thulium; la scienza è la stessa.

<!-- research-technologies:end -->

## Le CPU {#the-cpus}

Anche le nuove CPU si ricercano qui, poi si creano nell’Assemblaggio. La stessa tabella e le stesse note sono nella pagina [Extra](/wiki/06-Items/Extras.md#research-cpus).

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | Tempo di ricerca | Richiede prima | Thulium per la creazione | Tempo di creazione |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 min | – | 12.000 | 5 min |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10 h | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30.000 | 10 min |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1 g | [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75.000 | 15 min |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3 h | – | 8.000 | 5 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10 h | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 20.000 | 10 min |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1 g | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40.000 | 15 min |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6 h | – | 15.000 | 10 min |

Nessuna si vende nel Negozio: ricerca la tecnologia, poi crea la CPU nell’Assemblaggio. Passa il puntatore su una CPU nel suo albero per vedere che cosa chiede l’Assemblaggio per crearla.

### Extra Slots CPUs

- **Che cosa fanno.** Le Extra Slots CPU I, II e III danno a ogni nave 3, 5 e 7 slot extra in più, cioè 6, 8 e 10 in tutto su una nave che ne ha già 3, e 5, 7 e 9 su una che ne ha già 2. Una CPU superiore sostituisce la precedente: la II non si somma alla I.
- **Installata, non trasportata.** Una Extra Slots CPU non è un oggetto: quando la ritiri nell’Assemblaggio si installa da sola nel tuo Skylab, per ogni nave in entrambe le configurazioni, e non occupa nessuno slot. Resta anche dopo il reset.
- **In ordine.** Creale una dopo l’altra: la II solo quando la I è installata, la III solo quando la II è installata; fino ad allora l’Assemblaggio ti dice quale installare prima. Le tre costano 117.000 Thulium in tutto: 12.000, 30.000 e 75.000.

### Jump CPU

- **Che cosa fa.** Fa saltare la tua nave in qualsiasi settore di corporazione del tuo mondo, della tua corporazione come delle altre, settori base inclusi (`M`, `T` e `G`, settori da 1 a 4), per **500 Thulium** a salto. Non ha limiti di utilizzi: paghi solo il Thulium. Non porta mai in un settore pericoloso (`DS`) né in un settore neutrale (`N`).
- **Il salto.** Premi lo slot JMP, scegli il settore sulla mappa del Sistema stellare e conferma: la nave si carica per 5 secondi, poi arriva a un portale di quel settore, protetta come dopo qualsiasi salto di portale. Dopo il tuo arrivo la CPU si raffredda per 30 secondi.
- **Non in combattimento.** Non può partire entro 10 secondi da uno sparo o da un colpo subito, e uno sparo o un colpo durante la carica annulla il salto; allora non si paga nulla. Non puoi saltare mentre sei occultato.
- **Non da un settore neutrale:** un pilota in un settore neutrale o senza corporazione non può usarla.
- Può lasciare un settore pericoloso quando non sei in combattimento.

### Base CPUs

- **Che cosa fanno.** Teletrasportano la tua nave alla base della tua corporazione, nella zona sicura attorno alla sua stazione (`M-1`, `T-1` o `G-1`, il settore con Mission Control), senza costi in Thulium. Si avviano dallo slot BSE della barra rapida.
- **Non in combattimento.** Una carica di 10 secondi, uguale per entrambe. Non può partire entro 10 secondi da uno sparo o da un colpo subito, né mentre sei occultato o se sei già nella zona sicura della tua base, e uno sparo o un colpo durante la carica la annulla.

| CPU | Utilizzi | Ricarica |
| :--- | ---: | ---: |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 10 | 10 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 25 | 5 min |

- **Si esaurisce, non si ricarica.** Ogni utilizzo consuma uno degli utilizzi della CPU, e una CPU senza utilizzi rimasti sparisce: creane una nuova. Con entrambe montate, si usa per prima la migliore (II).

### Auto-Repair CPU

- **Che cosa fa.** Lancia da solo il Repair Drone montato nei tuoi slot extra, ogni volta che avresti potuto lanciarlo a mano: il tuo scafo non è pieno, il drone non è già fuori e sono passati 10 secondi dall’ultimo colpo. Non c’è nessuna soglia di scafo da impostare.
- Occupa uno slot extra tutto suo e non fa nulla senza un Repair Drone in uno slot extra della stessa configurazione. Non lancia mai un Repair Drone in uno slot abilità (quello è il pulsante Emergency Repair).
- **Se fermi il drone a mano,** la CPU lo lascia stare finché il tuo scafo non è di nuovo pieno, o finché non lanci tu il drone.


<!-- research-cpus:end -->
