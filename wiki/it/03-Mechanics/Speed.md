<!-- wiki-i18n source: fde0e896bc82b2a3 -->
<!-- wiki-i18n title: Velocità -->
# Calcolo della velocità {#speed-calculation}

La velocità determina quanto rapidamente si muove la tua nave sulla mappa spaziale e ti permette di inseguire bersagli, sfuggire al combattimento o attraversare le zone.

## La formula della velocità {#the-speed-formula}

La velocità finale della tua nave viene calcolata dal server con questa formula:

\[\text{Velocità finale} = (\text{Velocità base della nave} + \text{Velocità totale dei motori}) \times (1,0 + \text{Percentuale totale del bonus di velocità})\]

### 1. Velocità effettiva dei motori {#1-effective-engine-speed}

Ogni motore equipaggiato genera velocità, e così ogni Nucleo adattivo che contiene propulsori. Se nel motore sono montati dei propulsori, la sua velocità viene modificata:

\[\text{Velocità del motore} = (\text{Velocità base del motore} + \text{Bonus fisso dei propulsori}) \times \text{Moltiplicatore dei propulsori}\]

- **Bonus fisso dei propulsori**: la somma di tutte le aggiunte fisse di velocità dei propulsori (ad es. l’Impulse Thruster III dà `+15` di velocità).
- **Moltiplicatore dei propulsori**: il prodotto dei moltiplicatori di velocità di tutti i propulsori montati in quel motore (ad es. il Momentum Thruster III è `1.09`, ovvero `+9%`, l’Impulse Thruster III `1.03`, ovvero `+3%`). Moltiplica tutto ciò che il motore produce: la sua velocità base e i bonus fissi dei propulsori. Un Nucleo adattivo non ha una velocità base propria, e i bonus fissi dei suoi propulsori vengono moltiplicati lo stesso.

Un Engine III (velocità base 6) con tre Momentum Thruster IV (`+12`, `1.11`) produce (6 + 3 x 12) x 1,11 x 1,11 x 1,11 = 57,4, e con tre Impulse Thruster IV (`+17`, `1.02`) (6 + 3 x 17) x 1,02 x 1,02 x 1,02 = 60,5. Un bonus della Forgia sul moltiplicatore di un propulsore fa crescere la parte sopra 1: +15% su `1.11` dà `1.1265`.

### 2. Rendimenti decrescenti (efficienza marginale) {#2-diminishing-returns-marginal-efficiency-}

Per evitare che si accumulino motori all’infinito in cambio di una velocità infinita, si applica una curva di **rendimenti decrescenti (efficienza marginale)**. Tutti i motori vengono ordinati in base al loro contributo di velocità ed elaborati in quest’ordine. I Nuclei adattivi (ibridi) e gli Shield Core seguono la stessa classifica, ciascun tipo in un gruppo a sé, quindi una nave con sia motori sia Nuclei adattivi ha i primi quattro di ciascun tipo:

| Posizione del motore | Moltiplicatore di efficienza |
| :---: | :--- |
| **dal 1º al 4º** | **100%** (1,0) |
| **5º** | **85%** (0,85) |
| **6º** | **70%** (0,70) |
| **7º** | **55%** (0,55) |
| **8º e oltre** | **25%** (0,25) |

Inoltre, la velocità del motore viene moltiplicata per l’efficienza del suo slot (principale: 100%, di supporto: 75%, ausiliario: 50%).

### 3. Percentuale di bonus velocità e penalità degli scudi {#3-speed-bonus-percent-shield-penalties}

La percentuale totale del bonus di velocità è la somma di tutti i bonus di velocità dei motori equipaggiati (e degli ibridi), meno le penalità degli scudi equipaggiati:

- **Bonus di velocità dei motori**: i motori aggiungono percentuali di velocità positive (ad es. l’Engine III aggiunge `+5%`).
- **Penalità di velocità degli scudi**: gli scudi pesanti appesantiscono la nave e aggiungono percentuali di velocità negative (ad es. un Heavy Shield Core aggiunge `-5%` di velocità).
- **Scala degli slot**: anche questi bonus e queste penalità percentuali vengono scalati dall’efficienza dello slot in cui è montato l’oggetto. Uno scudo montato su uno dei tuoi droni ti rallenta come uno scudo in uno slot principale.
- **Mai sotto zero**: per quanti scudi tu porti, la tua velocità non scende sotto 0.
- **Formazioni di droni**: una [formazione di droni](/wiki/03-Mechanics/Formations.md) indossata cambia ancora la velocità finale, come fattore a parte: Gyre +10%, Cordon −3%, Auger −9%, Culler −10%, Redoubt −11%, Rampart −17%. L’Afterburner moltiplica poi il risultato.
