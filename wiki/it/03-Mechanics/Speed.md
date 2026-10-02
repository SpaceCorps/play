<!-- wiki-i18n source: 431a488ba7a0842e -->
<!-- wiki-i18n title: Velocità -->
# Calcolo della velocità {#speed-calculation}

La velocità determina quanto rapidamente si muove la tua nave sulla mappa spaziale e ti permette di inseguire bersagli, sfuggire al combattimento o attraversare le zone.

## La formula della velocità {#the-speed-formula}

La velocità finale della tua nave viene calcolata dal server con questa formula:

\[\text{Velocità finale} = (\text{Velocità base della nave} + \text{Velocità totale dei motori}) \times (1,0 + \text{Percentuale totale del bonus di velocità})\]

### 1. Velocità effettiva dei motori {#1-effective-engine-speed}

Ogni motore equipaggiato genera velocità. Se nel motore sono montati dei propulsori, la sua velocità viene modificata:

\[\text{Velocità del motore} = (\text{Velocità base del motore} \times \text{Moltiplicatore dei propulsori}) + \text{Bonus fisso dei propulsori}\]

- **Moltiplicatore dei propulsori**: il prodotto dei moltiplicatori di velocità di tutti i propulsori montati in quel motore (ad es. il Thruster III è `1.1`, ovvero `+10%`).
- **Bonus fisso dei propulsori**: la somma di tutte le aggiunte fisse di velocità dei propulsori (ad es. il Thruster III dà `+15` di velocità).

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
