<!-- wiki-i18n source: 6b964707b3b7ca22 -->
<!-- wiki-i18n title: Escavatore gigante -->
# Escavatore gigante {#giant-excavator}

<!-- wiki-search: excavator; giant excavator; pulsar; mining; fuel; excavator fuel; control panel; overheat; radiation; slumbering void; voids; wave; ds-1; ds-2; ds-3; escavatore; escavatore gigante; carburante; pannello di controllo; surriscaldamento; radiazioni; ondata -->

Dal primo giorno della stagione un **pulsar** brilla in ciascuno dei settori pericolosi `DS-1`, `DS-2` e `DS-3`, e dal giorno 11 della stagione accanto a lui sorge un **escavatore gigante**. L’escavatore estrae il pulsar per ricavarne **Thulium e minerali rari**, e per farlo brucia [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md). Chiunque può rifornirlo, scegliere cosa estrae e avviarlo, e tutto ciò che deposita sta intorno a lui in casse che chiunque può prendere. Un ciclo però è rumoroso: l’intero mondo viene avvisato quando parte, gli **Slumbering Void** arrivano a ondate per fermarlo, e un escavatore spinto troppo a lungo si surriscalda e irradia tutta la zona. Questa pagina spiega come va un ciclo, cosa deposita e come uscirne vivi. I settori sono in [Settori pericolosi](/wiki/01-General/Danger-Sectors.md); i Void in [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).

![The giant excavator's sheet: the fuel tank, the heat, the resource to mine, the excavator's hull and the Voids of the next wave](../../img/wiki-img/shots/excavator-sheet.jpg)

## In breve {#at-a-glance}

<!-- excavator-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Dove**: Un pulsar con un escavatore gigante in ciascuno dei settori `DS-1`, `DS-2` e `DS-3`, in ogni mondo
- **Compare**: Il pulsar dal primo giorno della stagione, l’escavatore dal giorno 11 della stagione fino al reset
- **Carburante**: Dark Matter. Una brucia per 10 min; il serbatoio ne contiene 3, cioè 30 min di estrazione. Chiunque può aggiungerne una alla volta, dal proprio carico
- **Pannello**: La finestra funziona entro 600 unità dall’escavatore, e la sua etichetta si vede da 1.400 unità. Chiunque può rifornire, scegliere e avviare; la scelta è bloccata finché è in funzione
- **Casse**: Una cassa ogni 20 s, tra 450 e 900 unità dall’escavatore, libera per chiunque dal momento in cui cade. Resta per 5 min, e su una mappa ce ne sono al massimo 24 insieme
- **Calore**: 30 min di estrazione, in quanti cicli servono, e l’escavatore si surriscalda per 1 h. Il calore resta tra un ciclo e l’altro e sparisce dopo il riposo
- **Radiazioni**: Finché è surriscaldato o distrutto, l’escavatore (entro 1.100 unità) e il suo pulsar (entro 1.300 unità) bruciano ogni nave all’interno: 10% dei suoi HP totali ogni secondo
- **Scafo**: 200.000 HP in Alpha, 300.000 in Beta e 400.000 in Gamma. Solo gli Slumbering Void possono danneggiarlo, e solo quando non resta nessun pilota a difenderlo
- **Void**: 2 Slumbering Void ogni 2 min mentre estrae, i primi 1 min dopo l’avvio; al massimo 8 vivi su una mappa
- **Avvisi**: I piloti del mondo intero vengono avvisati quando un ciclo parte, quando l’escavatore si surriscalda e quando viene distrutto; il resto va ai piloti del suo settore. Sono righe di Sistema: compaiono nella scheda **Sistema** della chat e nel Registro di gioco, e non in **Globale** né in **Locale**.

<!-- excavator-glance:end -->

## Come va un ciclo {#how-a-run-goes}

1. **Trovane uno.** Dal giorno 11 della stagione ciascuno dei tre settori pericolosi con un pulsar ha un escavatore, in ogni mondo. Un’etichetta, **Escavatore**, gli sta sopra quando sei vicino, e la mappa del Sistema stellare segna ogni settore pericoloso che ne ha uno: il colore del segno è lo stato del suo escavatore, e il suo suggerimento indica il tempo al prossimo cambio.
2. **Apri il pannello.** Clicca l’etichetta. La finestra **Escavatore gigante** funziona finché la tua nave è nel raggio del pannello dell’escavatore (l’elenco *In breve* lo indica). Una nave occultata può usarlo, e usarlo non pone fine all’occultamento.
3. **Rifornisci.** **Aggiungi Dark Matter** mette una Dark Matter dal tuo carico nel serbatoio. Può farlo chiunque. Il serbatoio non ne accetta mai più di quante l’escavatore possa bruciarne prima di surriscaldarsi, così non si spreca carburante.
4. **Scegli cosa estrarre** dall’elenco, poi premi **Avvia l’estrazione**. Serve almeno una Dark Matter nel serbatoio e una risorsa. Chiunque può cambiare la scelta fino all’avvio; una volta in funzione, la risorsa è bloccata. L’avvio viene annunciato a ogni pilota del mondo, con il tuo nome, il settore e la risorsa.
5. **Difendilo.** Mentre estrae, ogni pochi secondi cade una cassa intorno all’escavatore, e poco dopo l’avvio arrivano i primi Slumbering Void. Difendi l’escavatore e prendi le casse.
6. **Controlla il calore.** La barra del Calore si riempie mentre l’escavatore estrae e non si svuota mai mentre aspetta. Al limite l’escavatore si surriscalda. Vai via prima: il gioco avvisa la mappa due volte.
7. **Riposa.** Surriscaldato o distrutto, l’escavatore e il suo pulsar sono irradiati finché il riposo non finisce; poi è di nuovo pronto, con il calore azzerato e lo scafo pieno.

La finestra mostra anche il settore, il serbatoio (una cella per ogni Dark Matter, quella che brucia disegnata a metà), quanta Dark Matter trasporti, lo scafo dell’escavatore, quanto deposita ogni risorsa al minuto nel tuo mondo e, mentre estrae, il tempo alla prossima ondata e i Void vivi. Quando qualcosa viene rifiutato, leggi il motivo in rosso: sei troppo lontano dal pannello, non hai Dark Matter, il serbatoio è pieno, non c’è ancora carburante o una risorsa scelta, la risorsa è bloccata mentre è in funzione, oppure l’escavatore è caldo.

| Stato | Che cos’è | Cosa puoi fare |
| :--- | :--- | :--- |
| **Pronto** | Senza carburante, oppure con carburante e non avviato. Il calore accumulato resta. | Aggiungere Dark Matter, scegliere, avviare. |
| **In estrazione** | Brucia Dark Matter e accumula calore; la risorsa è bloccata. | Aggiungere altra Dark Matter fino al posto rimasto, combattere i Void, prendere le casse. |
| **Surriscaldato** | Il calore ha raggiunto il limite. Il serbatoio è svuotato; le casse già deposte restano. | Niente. La zona è irradiata: stai fuori. |
| **Distrutto** | I Void hanno portato lo scafo a zero. Il carburante è perso, lo scafo torna subito pieno. | Niente. La zona è irradiata: stai fuori. |

Se il carburante finisce prima del limite, l’escavatore torna **Pronto** con il suo calore, e i Void rimasti se ne vanno dopo un po’, a meno che stiano combattendo.

## Cosa estrae {#what-it-mines}

Un serbatoio pieno deposita circa quanto guadagnerebbero cinque piloti in mezz’ora del miglior farming di Thulium. Beta e Gamma depositano di più, come pagano di più per ogni abbattimento. Scegli una risorsa per ciclo. Una cassa è uguale per tutti, e una cassa di Thulium è denaro contante che viene pagato alla raccolta, come il Thulium degli asteroidi.

<!-- excavator-resources:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Un serbatoio pieno (3 Dark Matter, 30 min di estrazione) deposita le quantità qui sotto, in 90 casse.

| Risorsa | Alpha | Beta | Gamma | Un minuto, in Alpha | Una cassa, in Alpha |
| :--- | ---: | ---: | ---: | ---: | ---: |
| [Thulium](/wiki/06-Items/Resources.md#thulium) | 9.643 | 15.429 | 19.286 | 321,4 | 107,1 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | 2.314 | 3.703 | 4.629 | 77,1 | 25,7 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | 1.029 | 1.646 | 2.057 | 34,3 | 11,4 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | 640 | 640 | 640 | 21,3 | 7,1 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | 320 | 320 | 320 | 10,7 | 3,6 |

- Un ciclo di Velkonite o Orvium deposita al massimo 8 ore di un collettore di livello 20 dello [Skylab](/wiki/03-Mechanics/Skylab.md) per quel minerale (640 Velkonite, 320 Orvium), in ogni mondo: sono i minerali dello Skylab, e un ciclo non ne accelera mai il ritmo più di così.
- Una cassa contiene circa la quantità dell’ultima colonna, con uno scarto di 15%. Una cassa di Thulium è denaro contante: la raccolta lo paga. Una cassa di minerale contiene l’oggetto.

<!-- excavator-resources:end -->

I booster del pilota funzionano come per qualsiasi carico: il bonus del Resource Magnet Booster aumenta una cassa di minerale. Non c’è un limite giornaliero per le casse: il carburante e l’orologio limitano un ciclo.

**A cosa serve il minerale.** Il minerale di una cassa va nel tuo carico come qualsiasi oggetto. Cataclysite e Quorvium servono all’Assemblaggio e alla Fucina ([Risorse](/wiki/06-Items/Resources.md)). La Fucina e il Centro ricerche dello Skylab prendono Velkonite e Orvium solo dal Magazzino risorse, che i collettori riempiono; il minerale di una cassa non serve a niente nel tuo carico: ferma la nave e la [Baia del minerale](/wiki/03-Mechanics/Skylab.md#ore-bay) del tuo Skylab (Nucleo al livello 10) lo sposta nel magazzino, fino alla sua quota all’ora, e da lì lo prendono la Fucina e il [Centro ricerche](/wiki/03-Mechanics/Research.md#fuel).

## Gli Slumbering Void {#the-slumbering-voids}

Un ciclo attira gli **Slumbering Void**, cacciatori della civiltà perduta che arrivano in volo dal bordo della mappa per proteggere il pulsar da chiunque voglia svuotarlo. Danno la caccia ai piloti vicini all’escavatore, e quando non c’è più nessuno a cui dare la caccia, attaccano l’escavatore. I numeri del Void e la sua ricompensa sono in [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).

<!-- excavator-voids:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Ondate.** 2 Slumbering Void ogni 2 min; i primi 1 min dopo l’avvio, e nessuno negli ultimi 1 min di un ciclo. Su una mappa ce ne sono vivi al massimo 8 insieme: un’ondata che trova la mappa piena viene saltata.
- **Arrivo.** Un’ondata compare al bordo della mappa, 900 unità verso l’interno e ad almeno 2.500 unità da ogni anello di portale, e vola all’escavatore in circa 20 s. Il messaggio indica il lato della mappa da cui arriva.
- **Caccia.** Un Void dà la caccia al pilota più vicino che vede entro 2.500 unità, e resta entro 7.000 unità dall’escavatore.
- **Assedio.** Quando per 15 s nessun pilota visibile si trova entro 7.000 unità dall’escavatore, i Void attaccano l’escavatore, e ogni laser fa 25% del suo danno abituale. A zero l’escavatore viene distrutto: il suo carburante è perso, il suo scafo torna subito pieno, e riposa per 1 h.
- **Partenza.** Quando un ciclo finisce, i Void rimasti restano ancora 90 s e continuano a combattere se vengono combattuti; poi se ne vanno.

<!-- excavator-voids:end -->

- **Un Void è un cannone di vetro.** Il suo scudo è grande ma assorbe l’80% di un colpo, quindi lo scafo dietro è finito dopo poche volte la sua dimensione in danni, e molto prima con la penetrazione dello scudo. Due o tre piloti ben equipaggiati reggono un ciclo in Alpha; Beta e Gamma richiedono gruppi più grandi, come per ogni alieno.
- **Un occultamento non difende il sito.** I Void non vedono le navi occultate, quindi un pilota che si nasconde non li tiene lontani dall’escavatore; e un pilota che si ripara in un anello di portale non può essere raggiunto e non conta nemmeno.
- **Ogni Void paga,** in base al danno che gli hai inflitto, e lascia una cassa ([come paga l’abbattimento di un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). I loro abbattimenti si sommano ai tuoi punti PvE di grado come quelli di una nave di sciame.

## Calore e radiazioni {#heat-and-radiation}

L’estrazione aggiunge calore secondo dopo secondo. Il calore è **cumulativo e non si raffredda mai mentre l’escavatore aspetta**: un ciclo interrotto presto lascia al pilota successivo un ciclo più corto. Quando raggiunge il limite, l’escavatore **si surriscalda**, e quando il suo scafo è portato a zero viene **distrutto**; in entrambi i casi l’escavatore e il suo pulsar irradiano finché il riposo non finisce.

<!-- excavator-radiation:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

| Cerchio | Raggio | HP totali al secondo | Una nave piena resiste |
| :--- | ---: | ---: | ---: |
| L’escavatore gigante | 1.100 | 10% | 10 s |
| Il pulsar | 1.300 | 10% | 10 s |

- **La dose.** 10% degli HP massimi totali di una nave (scafo più scudo) ogni secondo, quindi una nave piena resiste 10 s, qualunque sia la sua classe. Lo scudo la riceve per primo e il suo assorbimento non conta.
- **Chi.** Ogni nave dentro i cerchi, anche quelle occultate; nessun alieno. È danno subito: un Drone riparatore si ferma e lo scudo non si ricarica, come al buco nero.
- **Accredito.** Un pilota che muore bruciato viene accreditato all’ultimo nemico che lo ha colpito nei 15 s precedenti.
- **Avvisi.** La mappa viene avvisata 1 min e 15 s prima del surriscaldamento.

<!-- excavator-radiation:end -->

- **L’avviso.** Due volte prima del surriscaldamento (i tempi sono nell’elenco qui sopra) la mappa viene avvisata, una nave dentro i cerchi vede un avvertimento, e i cerchi vengono disegnati a terra in volo e sulla minimappa. Quando irradiano, i cerchi sono rossi e l’indicatore delle Radiazioni mostra la dose.
- **Andarsene.** Ogni nave di serie può uscire dal bordo del pannello o dalla cassa più lontana rimasta, tranne la Ironclad, che è lenta: se ne va durante l’avviso, oppure non se ne va. Non startene su una cassa quando il calore arriva al limite.
- **Bottino nei cerchi.** Le casse deposte prima del surriscaldamento restano, nelle radiazioni: una cassa che si trova lì quando iniziano si prende al prezzo della dose.
- **Il riavvio del server** mette in pausa un ciclo: carburante e calore tornano com’erano, il riposo continua secondo l’orologio, e la prima ondata dopo il riavvio arriva un minuto più tardi.

## Combattere per un ciclo {#fighting-over-a-run}

L’escavatore non ha **nessun anello speciale**: valgono le regole normali del tuo mondo, quindi possono arrivare rivali, spararti e prendere le casse (una cassa è libera per chiunque dal momento in cui cade). Rubare e tendere imboscate fa parte dell’evento. Alcune cose da prevedere:

- **Chi rifornisce non è chi vince.** Chiunque può rifornire, scegliere e avviare; un rivale può cambiare la risorsa prima che premi Avvia. Controlla la scelta prima di premere.
- **Il carburante è a rischio.** Se l’escavatore viene distrutto, la Dark Matter nel suo serbatoio è persa e nessuno la riavrà. Il massimo che si può perdere è il serbatoio pieno.
- **Porta un gruppo** e decidete chi resta vicino all’escavatore e chi prende le casse, e tieni d’occhio il calore: i piloti che prendono le ultime casse sono quelli che le radiazioni colgono.
- **I Void vengono all’escavatore, non alle casse.** Un gruppo che tiene l’escavatore tiene occupati i Void; chi si allontana lo lascia all’assedio.

## Cosa viene detto al mondo {#what-the-world-is-told}

Sono righe di Sistema (compaiono nella scheda **Sistema** della chat e nel Registro di gioco, e non in **Globale** né in **Locale**). Le prime tre vanno al mondo intero; l’ultima ai piloti del settore dell’escavatore.

- Il giorno in cui inizia l’evento 2: i settori pericolosi sono cambiati.
- Un pilota **avvia** un escavatore, con il settore, la risorsa e i minuti di carburante.
- L’escavatore **si surriscalda**, oppure viene **distrutto**.
- Il carburante finisce; l’escavatore sta per surriscaldarsi (due avvisi); sta arrivando una **ondata** di Void, con il suo numero e il lato della mappa da cui viene; non resta nessun pilota, quindi i Void attaccano l’escavatore.

Ogni azione del pannello e ogni avviso ha un suono discreto tutto suo, al volume degli effetti.

## Dove leggere ancora {#where-to-read-more}

- [Settori pericolosi](/wiki/01-General/Danger-Sectors.md): dove stanno i pulsar e cos’altro c’è di nuovo.
- [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md): lo Slumbering Void, l’Inert Mass e l’Unwakened.
- [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md) e [Il buco nero](/wiki/03-Mechanics/Black-Hole.md): da dove viene il carburante.
- [Risorse](/wiki/06-Items/Resources.md): i minerali che deposita l’escavatore.
- [Casse di carico](/wiki/03-Mechanics/Cargo.md): casse, raccolta e il Resource Magnet Booster.
- [Gradi](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points): i punti PvE di un Void.
