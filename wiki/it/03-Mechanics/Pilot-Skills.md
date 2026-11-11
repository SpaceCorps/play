<!-- wiki-i18n source: d75ffd5e6e894c46 -->
<!-- wiki-i18n title: Competenze del pilota -->
# Competenze del pilota {#pilot-skills}

<!-- wiki-search: skills; skill tree; pilot skill tree; pilot skills; skill xp; xp; level up; stats; attributes; heft; grit; reflex; instinct; laser tech; rocket tech; antimatter; marksmanship; sabotage; evasion; tactics; radiation tech; thruster theory; science; extraction; logistics; fabrication; commerce; soft cap; hold; training; day one; pilot button; pilot page; buffs; competenze; competenze del pilota; albero delle competenze; esperienza; salire di livello; statistiche; attributi; massa; tenacia; riflessi; istinto; tecnica laser; tecnica dei razzi; antimateria; mira; sabotaggio; evasione; tattica; tecnica antiradiazioni; teoria dei propulsori; scienza; estrazione; logistica; fabbricazione; commercio; limite orario; stiva -->

Il tuo pilota ha un **albero delle competenze**: un insieme di statistiche che salgono di livello in base a quello che fai. Combatti, e salgono la tua Tecnica laser e la tua Tenacia; raccogli dal tuo Skylab, e sale la tua Estrazione. Ogni livello dà un piccolo bonus permanente a qualcosa che già fai, e non si spende né si sceglie nulla: non ci sono punti da assegnare e niente da azzerare. Fai salire ciò che usi.

L’albero è **tuo**, non di una nave. Ogni nave che piloti ha i tuoi livelli, anche una nave che comprerai domani, e i livelli si conservano attraverso ogni reset ([cosa si conserva](#what-is-kept)).

Un pilota nuovo non è a piena forza. Al livello 1 un laser e un razzo fanno meno danno di quanto indichino le pagine degli oggetti, e la Tecnica laser e la Tecnica dei razzi li portano oltre i numeri indicati man mano che salgono. Ogni cifra delle pagine degli oggetti è quella dell’oggetto stesso, prima delle tue competenze.

## In breve {#at-a-glance}

<!-- skills-glance:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

- **Statistiche**: 18 statistiche: 4 attributi e 14 competenze in 5 gruppi
- **Livelli**: Da 1 a 100. Ogni pilota parte con ogni statistica al livello 1, e non c’è nulla da spendere né da azzerare
- **Costo di un livello**: 40 XP dal livello 1 al 2, 875 XP dal livello 50 al 51, 19.157 XP dal livello 99 al 100; 313.258 XP in tutto
- **Cosa dà un livello**: Un bonus cresce in linea retta dal suo valore al livello 1 al suo valore al livello 100. Nulla è limitato
- **Il tuo laser al livello 1**: Fa il 80% del suo danno e colpisce il 80% delle volte, quindi il 64% del danno indicato dalle pagine degli oggetti
- **Il tuo razzo al livello 1**: Fa il 100% del suo danno ed è un fallimento il 10% delle volte, quindi il 90% del danno indicato dalle pagine degli oggetti
- **Schivata**: La nave di ogni pilota schiva il 3% dei colpi che si possono schivare, prima che qualsiasi competenza o formazione vi aggiunga
- **Livello dello scafo**: La rarità della tua nave lo fissa, come mostra la tabella qui sotto. La dimensione della tua stiva e gli XP della Massa lo seguono
- **Stiva**: Conta le unità di risorse che raccogli dopo il lancio, fino alla dimensione che le dà il suo livello dello scafo. È piena a partire dal 90% di questo, e una stiva piena fa pagare la Massa ×1,5. Nulla viene mai rifiutato
- **Limite orario morbido**: La maggior parte delle statistiche paga l’XP piena solo fino a un limite orario, contato nell’unità propria della statistica sull’ora dell’orologio UTC. Oltre, un evento paga il 25% della sua XP
- **Allenamento**: L’XP di una competenza paga anche il 10% di sé al suo attributo. Un attributo al livello 100 allena le sue competenze il 25% più in fretta che al livello 1

| Livello dello scafo | Rarità della nave | Dimensione della stiva |
| :--- | :--- | ---: |
| 1 | Scadente / Comune | 60 |
| 2 | Non comune | 120 |
| 3 | Raro | 250 |
| 4 | Epico | 500 |
| 5 | Mitico / Leggendario / Eterno | 1.000 |

<!-- skills-glance:end -->

## Le statistiche {#the-stats}

Le statistiche sono di due tipi. Gli **attributi** (Massa, Tenacia, Riflessi e Istinto) sono le basi di un pilota. Le **competenze** sono in cinque gruppi, e ciascuna è governata da un attributo, che le tabelle nominano tra parentesi: l’XP di una competenza alimenta anche il suo attributo, e un attributo alto allena più in fretta le sue competenze ([come si paga l’XP](#how-xp-is-paid)). I nomi sono quelli della pagina Competenze del pilota del gioco.

Le tabelle danno ogni bonus al livello 1 e all’ultimo livello; tra i due un bonus cresce in linea retta. Un **fattore** moltiplica un numero: uno sopra 1 lo rende più grande, uno sotto 1 più piccolo. La maggior parte dei bonus cambia una cifra della tua nave, e il suggerimento di una cifra che una competenza ha mosso ha una riga che dice quanto ne viene dalle tue competenze.

<!-- skills-buffs:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

### Attributi {#attributes}

| Statistica | Cosa cambia | Livello 1 | Livello 100 |
| :--- | :--- | ---: | ---: |
| **Massa** | Scafo | +0% | +10% |
| **Tenacia** | Danni subiti | ×1 | ×0,9 |
| **Riflessi** | Velocità di ricarica delle abilità | ×1 | ×1,11 |
| **Istinto** | Probabilità di ogni riga di bottino | +0 punti | +5 punti |
|  | Orvium e Velkonite dai collettori | ×1 | ×1,5 |

### Armi {#weapons}

| Statistica | Cosa cambia | Livello 1 | Livello 100 |
| :--- | :--- | ---: | ---: |
| **Tecnica laser** (Riflessi) | Danno laser | ×0,8 | ×1,1 |
|  | Probabilità che una raffica laser colpisca | 80% | 90% |
| **Tecnica dei razzi** (Riflessi) | Danno dei razzi | ×1 | ×1,3 |
|  | Probabilità che un razzo sia un fallimento | 10% | 0% |
| **Antimateria** (Istinto) | Dark Matter dalle raccolte | ×1 | ×1,25 |

### Combattimento {#combat}

| Statistica | Cosa cambia | Livello 1 | Livello 100 |
| :--- | :--- | ---: | ---: |
| **Mira** (Riflessi) | Distanza di lancio di una Mine | ×1 | ×1,15 |
|  | Velocità di una Mine lanciata | ×1 | ×1,15 |
| **Sabotaggio** (Riflessi) | Danno di veleni e Mine | ×1 | ×1,3 |
|  | Durata dei veleni | ×1 | ×1,2 |
| **Evasione** (Riflessi) | Probabilità di schivare un colpo, aggiunta a quella della nave | 0% | 15% |
| **Tattica** (Riflessi) | Durata delle abilità | ×1 | ×1,2 |

### Controllo della nave {#ship-control}

| Statistica | Cosa cambia | Livello 1 | Livello 100 |
| :--- | :--- | ---: | ---: |
| **Tecnica antiradiazioni** (Tenacia) | Dose di radiazioni | ×1 | ×0,4 |
| **Teoria dei propulsori** (Massa) | Velocità | +0% | +15% |
| **Scienza** (Istinto) | Scienza per ogni unità di carburante | ×1 | ×1,25 |

### Skylab

| Statistica | Cosa cambia | Livello 1 | Livello 100 |
| :--- | :--- | ---: | ---: |
| **Estrazione** (Istinto) | Cosa produce lo Skylab | ×1 | ×1,3 |
| **Logistica** (Massa) | Cosa contiene la banca del Magazzino risorse | ×1 | ×1,4 |
| **Fabbricazione** (Riflessi) | Tempo di una fabbricazione | ×1 | ×0,65 |

### Commercio {#trading}

| Statistica | Cosa cambia | Livello 1 | Livello 100 |
| :--- | :--- | ---: | ---: |
| **Commercio** (Istinto) | Prezzi del Negozio | ×1 | ×0,85 |
|  | Cosa paga il Negozio quando ricompra | ×1 | ×1,1 |
|  | Caparra di un annuncio all’Asta | ×1 | ×0,5 |


<!-- skills-buffs:end -->

## Dove lo senti {#where-you-feel-it}

- **Laser.** La Tecnica laser cambia il danno di ogni raffica e la probabilità che colpisca; una raffica che va a vuoto mostra un “Miss” fluttuante e consuma comunque le munizioni ([Combattimento](/wiki/03-Mechanics/Combat.md#laser-tech)). La portata dei tuoi laser è quella della tua nave: la Mira sale con i tuoi colpi a segno con munizioni diverse dalle semplici x1, ma agisce solo sulle Mine (sotto).
- **Razzi.** La Tecnica dei razzi cambia il danno di ogni razzo e la probabilità che uno sia un fallimento ([Tecnica dei razzi](/wiki/06-Items/Rockets.md#rocket-tech)).
- **Subire colpi.** La Tenacia toglie una parte a ogni colpo che subisci, e l’Evasione aumenta la probabilità che un colpo diretto non faccia nulla ([Combattimento](/wiki/03-Mechanics/Combat.md#grit-and-evasion)). La Massa aumenta il tuo scafo.
- **Abilità.** I Riflessi accorciano il tempo di ricarica delle tue abilità e la Tattica le fa durare di più ([Abilità](/wiki/03-Mechanics/Abilities.md#pilot-skills)). Il Sabotaggio rafforza i veleni.
- **Mine.** Il Sabotaggio aumenta il danno di una Mine, e la Mira la lancia più veloce e più lontano ([Extra](/wiki/06-Items/Extras.md#mine)).
- **Velocità.** La Teoria dei propulsori si aggiunge alla tua velocità, oltre ai motori e a un Afterburner ([Velocità](/wiki/03-Mechanics/Speed.md)).
- **Raccolte.** L’Istinto aumenta la probabilità di ogni riga di bottino, come fa un Loot Luck Booster, e i due si sommano; l’Antimateria aumenta la Dark Matter che raccogli ([Carico](/wiki/03-Mechanics/Cargo.md), [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md)).
- **Radiazioni.** La Tecnica antiradiazioni riduce la dose del buco nero, dei cerchi degli escavatori, delle pulsar e dell’aura degli Unwakened ([Buco nero](/wiki/03-Mechanics/Black-Hole.md)).
- **A casa.** L’Estrazione e la Logistica cambiano ciò che lo [Skylab](/wiki/03-Mechanics/Skylab.md) produce e contiene, l’Istinto aumenta i suoi due collettori, la Fabbricazione accorcia le fabbricazioni dell’Assemblaggio, la Scienza riempie più in fretta il Centro [ricerche](/wiki/03-Mechanics/Research.md), e il Commercio abbassa i prezzi del Negozio, alza ciò che paga quando ricompra e abbassa la caparra di un annuncio all’[Asta](/wiki/03-Mechanics/Auction.md).

## Come si paga l’XP {#how-xp-is-paid}

Il server paga XP per ciò che fai, ovunque tu voli, in quest’ordine:

1. **La regola anti-farm.** Un colpo da o verso un compagno di corporazione o di gruppo non paga nulla, e nulla paga ciò che è fatto a una nave in una zona sicura o sotto il riparo di una rigenerazione, o da essa. I secondi di Massa, dello scafo basso della Tenacia e della Teoria dei propulsori contano solo finché la tua nave è viva, fuori da un riparo, e hai dato un ordine nell’ultimo minuto: una nave parcheggiata all’aperto non guadagna nulla.
2. **Il limite orario morbido.** Una statistica con un limite paga l’XP piena fino a esso e una parte oltre, contata nell’unità propria della statistica (i colpi che spari, i comandi che dai, l’XP che ha guadagnato) sull’ora dell’orologio UTC. Un nuovo accesso non riapre la finestra, e i numeri sono nell’elenco sopra e nella tabella sotto.
3. **Velocità di allenamento.** L’attributo che governa una competenza aumenta l’XP che la competenza guadagna, di più a ogni livello dell’attributo (il limite è contato prima di questo, quindi limita l’attività e non la velocità).
4. **La quota dell’attributo.** La competenza riceve l’XP, e il suo attributo ne riceve una quota, che non è mai limitata né accelerata.

La tabella elenca cosa paga XP, statistica per statistica. L’XP è per ogni unità di ciò che è nominato nella seconda colonna.

<!-- skills-xp:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

| Statistica | Cosa paga XP | XP | Limite orario morbido |
| :--- | :--- | ---: | ---: |
| **Massa** | Ogni 10 s di volo con un ordine dato negli ultimi 1 min: il livello dello scafo della nave, più 0,2 per ogni piastra montata, ×1,5 con la stiva piena | 1 | Nessuno |
| **Tenacia** | Ogni 1 % del tuo scafo massimo perso a causa di un nemico o di un pericolo | 1 | 300 XP all’ora |
|  | Ogni 10 s sotto il 25% del tuo scafo massimo | 5 |  |
| **Riflessi** | Ogni comando che il gioco accetta: un’abilità, un extra, un nuovo bersaglio, una raccolta, una fabbricazione, uno scambio di formazione, un razzo o un salto. Un nuovo bersaglio paga al massimo una volta ogni 4 s, una raccolta al massimo una volta ogni 1 s e un razzo al massimo una volta ogni 1 s | 1 | 600 comandi all’ora |
| **Istinto** | Ogni cassa di carico che raccogli, a mano o con un Retriever | 2 | 600 XP all’ora |
|  | Ogni oggetto di una ricompensa di missione che riscuoti | 10 |  |
|  | La prima volta che raccogli un oggetto di qualità Raro o migliore (una volta per oggetto, per sempre) | 25 |  |
| **Tecnica laser** (Riflessi) | Ogni raffica che spari | 0,1 | 1.800 colpi all’ora |
|  | Ogni raffica che colpisce una nave | 0,1 |  |
| **Tecnica dei razzi** (Riflessi) | Ogni razzo che lanci | 0,15 | 130 razzi all’ora |
|  | Ogni razzo che colpisce una nave (una volta per razzo, quante navi ferisca la sua esplosione) | 0,3 |  |
| **Antimateria** (Istinto) | Ogni unità di Dark Matter che ricevi a una raccolta | 0,1 | Nessuno |
| **Mira** (Riflessi) | Ogni colpo di una raffica sparata con munizioni diverse dalle semplici x1 (×1,5 per i primi 10 min di ogni tipo di munizioni in un’ora dell’orologio) | 0,1 | 3.000 colpi all’ora |
|  | Ogni colpo di una Mine, e ogni secondo che un nemico passa nel tuo Energetic Wall | 0,1 |  |
| **Sabotaggio** (Riflessi) | Ogni colpo di una Mine, e ogni secondo che un nemico passa nel tuo Energetic Wall | 0,5 | 1.200 XP all’ora |
|  | Ogni secondo in cui un tuo veleno agisce su un nemico | 0,05 |  |
| **Evasione** (Riflessi) | Ogni attacco ostile contro di te che manca o viene schivato | 1 | 600 XP all’ora |
| **Tattica** (Riflessi) | Ogni abilità che premi con un ostile nella portata del laser | 2 | 600 XP all’ora |
| **Tecnica antiradiazioni** (Tenacia) | Ogni secondo dentro una banda di radiazioni | 0,2 | Nessuno |
|  | Ogni 1 % del tuo scafo massimo che le radiazioni tolgono | 1 |  |
| **Teoria dei propulsori** (Massa) | Ogni secondo volato oltre il 80% della velocità della tua nave, il doppio sotto un Afterburner | 0,1 | Nessuno |
| **Scienza** (Istinto) | Ogni unità di scienza che il Centro ricerche brucia | 0,1 | Nessuno |
|  | Ogni tecnologia che completi | 50 |  |
| **Estrazione** (Istinto) | Ogni unità di risorsa che il tuo Skylab produce, pagata alla raccolta | 0,1 | Nessuno |
| **Logistica** (Massa) | Ogni unità di risorsa che depositi nella banca dello Skylab | 0,05 | Nessuno |
| **Fabbricazione** (Riflessi) | Ogni secondo di tempo di fabbricazione che completi, pagato alla raccolta | 0,1 | Nessuno |
| **Commercio** (Istinto) | Ogni scambio all’Asta o al Negozio, contato come il logaritmo decimale di 1 più il suo valore in Crediti (un Thulium vale quanto lo valuta l’Asta) | 2 | 600 XP all’ora |

<!-- skills-xp:end -->

Mentre voli, la schermata di volo mostra l’XP che guadagni in brevi righe, raccolte ogni pochi secondi, e un banner ti dice quando una statistica sale di livello e cosa è cambiato (il Registro di gioco ne conserva una riga). Una statistica che guadagna la sua prima XP viene annunciata una volta. I suggerimenti delle cifre che le competenze hanno mosso lo dicono anch’essi, in una riga Pilota a parte, e il riquadro Danno dell’hangar lascia fuori le competenze e lo dice: si applicano quando spari.

## Salire di livello {#levelling-up}

Un livello costa più XP del precedente, di una quota fissa, quindi i primi livelli arrivano in fretta e gli ultimi richiedono tempo. Ogni statistica ha la stessa curva. Il bonus che hai a un livello è lo stesso per ogni pilota: solo la velocità con cui lo raggiungi dipende da ciò che fai.

<!-- skills-curve:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

| Livello | XP del livello | XP in tutto dal livello 1 | Quota di ogni bonus |
| :--- | ---: | ---: | ---: |
| 2 | 40 | 40 | 1,01% |
| 10 | 66 | 468 | 9,09% |
| 25 | 170 | 2.174 | 24,24% |
| 50 | 822 | 12.851 | 49,49% |
| 75 | 3.968 | 64.397 | 74,75% |
| 100 | 19.157 | 313.258 | 100% |

<!-- skills-curve:end -->

## La pagina Competenze del pilota {#the-pilot-skills-page}

La pagina **Competenze del pilota** è una pagina della stazione, con una riga tutta sua nella barra laterale. Mostra tutto l’albero: gli attributi e le competenze nei loro gruppi, ciascuno col suo livello. Scegli una statistica per vedere cosa fa, quale attributo la governa, quali competenze allena, la sua barra dell’XP e cosa la fa crescere, e usa il cursore per vedere in anteprima qualsiasi livello dal 1 all’ultimo: una piccola tabella dà ciò che la statistica cambia al livello in anteprima e al tuo livello attuale. Una statistica che non ha ancora guadagnato XP è segnata come non usata, con un trattino al posto del livello. La riga nella barra laterale porta un badge quando una statistica è salita di livello da quando hai aperto la pagina l’ultima volta, e una scheda della finestra dei Booster riassume ciò che le tue competenze cambiano.

## Cosa si conserva {#what-is-kept}

- **Attraverso ogni reset.** L’albero è parte del tuo account: un reset non cambia alcun livello né alcuna XP, e il Deposito di trasporto non c’entra nulla ([Cosa conservi](/wiki/03-Mechanics/Wipe-Timeline.md#what-you-keep)).
- **Sui server regionali.** L’XP che guadagni volando su Singapore o US East viene aggiunta alle tue competenze quando torni a casa, comprese le statistiche usate lì per la prima volta, e il limite orario che hai consumato lì viene con te. La pagina Competenze del pilota di un pilota che vola lì legge i numeri del server regionale, con l’XP che la sua nave ha guadagnato dall’ultimo salvataggio.
- **Fino all’eliminazione dell’account.** Eliminare un account elimina i suoi livelli.

I bonus non hanno altro tetto che l’ultimo livello: un pilota che ha fatto salire tutto è forte quanto dicono le tabelle.
