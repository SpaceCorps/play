<!-- wiki-i18n source: 6ff3251582e96a39 -->
<!-- wiki-i18n title: Ricettario -->
# Ricettario e build {#recipe-book-and-builds}

<!-- wiki-search: recipe; recipes; recipe book; bill; steps; chart; craft tree; what do i need; build; builds; loadout; preset; presets; import; export; json; my builds; share a build; ricetta; ricette; costi; passaggi; diagramma; creare; equipaggiamento; importare; esportare; i miei build; condividere un build -->

Il **Ricettario** risponde a “che cosa serve per questo?” per qualsiasi oggetto del gioco: un diagramma di ciò di cui è fatto, i passaggi in ordine, i costi completi e da dove viene ogni materia prima. **Build** fa lo stesso per un’intera nave: importa l’equipaggiamento del tuo Hangar o il build di un amico, parti da uno dei 15 preset o creane uno tuo, e guarda le sue statistiche e i suoi costi completi, passo dopo passo. Entrambi sono nella **Biblioteca** della stazione, sotto la Wiki.

Il Ricettario non tiene un listino prezzi suo: calcola i numeri nel momento in cui guardi, a partire dalle ricette, dai prezzi, dalle tecnologie e dalle tabelle di bottino che usano il Negozio, l’[Assemblaggio](/wiki/06-Items/Overview.md#upgrading-modules) e la [Ricerca](/wiki/03-Mechanics/Research.md), e quindi segue il gioco quando cambia un prezzo o una ricetta. Per questo questa pagina non cita nessun prezzo e nessuna statistica: apri l’oggetto o il build.

![The Builds page: the presets from early to late, and a build with its lasers, generators, extras and drones laid out in slots](../../img/wiki-img/shots/builds.jpg)
![The Bill tab: what the item takes in Credits, Thulium and raw items, with what you have and what is missing](../../img/wiki-img/shots/recipe-book-bill.jpg)
![An item in the Recipe Book: its ways to get it, the switches for the bill and the chart of what it takes down to the raw items](../../img/wiki-img/shots/recipe-book-chart.jpg)

## Aprirlo {#open-it}

Apri il menu della stazione e scegli **Biblioteca › Ricettario** o **Biblioteca › Build**. Il Ricettario ricorda l’ultimo oggetto che hai guardato, i suoi filtri e il suo zoom, solo su questo computer; i tuoi build non ne fanno parte ([Salvati sul tuo account](#saved-on-your-account)). Quando il gioco è più recente del server con cui parla, la pagina lo dice e mostra meno: il Ricettario calcola comunque tutto ciò che si compra, si crea o si potenzia, ma non può dire dove il mondo dà un oggetto (scrive soltanto “Ottenere”), e Build nomina le parti che richiedono il server più recente: i preset, I miei build e le statistiche.

## Trovare un oggetto {#find-an-item}

La grande lista a sinistra contiene tutti gli oggetti del gioco, raggruppati per tipo e, dentro un tipo, nell’ordine proprio del gioco: prima il livello più debole. C’è anche l’EMP Charge, l’unico consumabile.

- **Ricerca.** Comincia a scrivere in un punto qualsiasi della pagina e il testo va nel campo di ricerca. La lista diventa una sola lista, ordinata in base a quanto il nome corrisponde (il nome intero, il suo inizio, l’inizio di una parola, una parte qualsiasi, poi il tipo). Maiuscole e accenti non contano, e il vecchio nome di un oggetto rinominato trova l’oggetto. `Esc` cancella la ricerca.
- **Tipo.** Il menu a tendina sopra la lista la restringe a un tipo e dice quanti oggetti ha ogni tipo. L’interruttore accanto ordina dalla A alla Z dentro ogni tipo.
- **Righe.** Una riga mostra l’immagine, il nome, il tipo e la rarità dell’oggetto, un piccolo simbolo per la via con cui di solito lo ottieni (creato in Assemblaggio, in vendita nel Negozio, bottino o scoperta, pressato, oppure prodotto nel buco nero) e un segno di spunta quando ce l’hai.
- **Tasti.** Le frecce, Pag su, Pag giù, Home e Fine scorrono la lista, e `Enter` passa al diagramma. `Alt+Left` e `Alt+Right` tornano indietro e vanno avanti tra gli oggetti che hai aperto.

## Il diagramma {#the-chart}

Clicca su un oggetto e il lato destro lo mostra. In alto ci sono la sua immagine, il nome, la rarità e il tipo, e un’etichetta per ogni **via** con cui ottenerlo: **Creare** (in Assemblaggio, con il suo tempo e il suo costo), **Comprare** (nel Negozio, con il suo prezzo), **Pressare** (dal minerale, nella Fucina dello Skylab), **Bottino** (lo dà il mondo: alieni, rocce, ricompense) e **Produrre** ([Dark Matter](/wiki/03-Mechanics/Dark-Matter.md), dai N.I.K.E. sparati nel buco nero). L’etichetta piena è la via che seguono il diagramma e i costi; clicca su un’altra etichetta per seguire quella. Se non hai ricercato ciò che ti permette di creare l’oggetto, una riga dice quale tecnologia serve e quanto dura, con un pulsante che apre la Ricerca.

Il **Diagramma** disegna l’oggetto come un albero da sinistra a destra: l’oggetto a sinistra, ciò di cui è fatto alla sua destra, fino alle materie prime.

- Ogni riquadro mostra l’oggetto, quanti te ne servono e un simbolo di come si ottiene (quello dell’etichetta di quella via, qui sopra; passa il mouse sul riquadro per leggere le parole, così il colore non è mai l’unico segno). Un lucchetto dice che la sua tecnologia non è ancora ricercata, e un segno di spunta verde con un numero dice quanti ne hai.
- Un riquadro con dei rami ha una piccola maniglia che li ripiega; i rami profondi di un albero grande partono ripiegati. **Espandi tutto**, **Comprimi tutto**, **Adatta** e i pulsanti dello zoom sono sopra il diagramma.
- Clicca su un riquadro per leggere la sua scheda sotto il diagramma: l’oggetto, le vie per ottenerlo (clicca su un’altra etichetta per seguire quella via), ciò che richiede la via (i cicli, il tempo e il costo di una creazione, o il suo prezzo nel Negozio), quanti ne hai e, per un riquadro bloccato, la tecnologia che serve. Un doppio clic, o `Enter`, apre quell’oggetto nel Ricettario. Le frecce passano da un riquadro all’altro, `Space` ripiega o apre un ramo e `0` adatta il diagramma. Scorri per spostarti; `Ctrl` e la rotellina fanno lo zoom.
- Un oggetto che si può solo comprare o trovare è un riquadro singolo che dice “Niente da creare: si compra o si trova. Vedi Fonti.”

In una finestra larga il diagramma occupa la sinistra e gli altri pannelli stanno in una colonna alla sua destra; in una stretta, le schede **Diagramma**, **Passaggi**, **Costi**, **Fonti** e **Usato in** mostrano un pannello alla volta.

## Passaggi e costi {#steps-and-the-bill}

Sotto l’intestazione, tre comandi decidono che cosa viene contato: **Quanti** esemplari vuoi, **Conta ciò che ho** (attivo: ciò che hai già viene tolto) e **Includi ciò che è montato** (disattivo: un pezzo montato su una nave non viene contato, perché potenziare consuma un pezzo e uno montato lascerebbe il suo slot).

- **Passaggi** è il diagramma come elenco numerato, nell’ordine in cui va fatto, in gruppi: Ricerca, Ottenere, Comprare, Pressare e creare, e Dalle tue scorte. La ricerca viene per prima perché l’Assemblaggio non crea nulla prima che la sua tecnologia sia ricercata. Ogni passaggio dice che cosa e quanti, quanto costa e quanto dura, e un passaggio Ottenere può mostrare dove ottenerlo. **Copia i passaggi** copia l’elenco come testo.
- **Costi** somma tutto: i tuoi Credits e il tuo Thulium a confronto con ciò che hai, ogni materia prima con le colonne **Serve**, **Hai** e **Manca**, il Dark Matter che prende la ricerca, il tempo per creare e pressare, il tempo per ricercare (una tecnologia alla volta) e un **Valore**. Il Valore serve a confrontare due vie per ottenere un oggetto, con il Thulium e le cose da trovare contati in Credits: non è un prezzo. **Copia i costi** copia i costi come una tabella che puoi incollare in una chat o in una nota.

## Fonti e Usato in {#sources-and-used-in}

- **Fonti** dice dove il mondo dà l’oggetto e ogni materia prima di cui il piano ha bisogno, per genere: alieni, asteroidi e rocce, sciami, il Dormant Swamp, custodi del clan, [Davidski](/wiki/03-Mechanics/Davidski.md), spedizioni dello Skylab, l’escavatore gigante, produzione dello Skylab, missioni, Invita amici e il pacchetto iniziale. Una riga nomina chi lo dà e dove, la probabilità e quanti. “Anche da” elenca l’[Asta](/wiki/03-Mechanics/Auction.md), le scorte di Davidski e altri piloti. Una probabilità è una probabilità, non un ritmo orario: quanto dura una distruzione dipende da te.
- **Usato in** elenca gli oggetti che si creano con questo. Clicca su uno per aprirlo.

## Aggiungi al build {#add-to-build}

Un oggetto che sta in uno slot o che si porta con sé ha un pulsante **Aggiungi al build**: navi, corazze dello scafo, laser, amplificatori, scudi, celle, motori, propulsori, Adaptive Core, extra, droni, formazioni, munizioni, razzi e l’EMP Charge. Mette l’oggetto nel build che stai modificando in **Build**, nel primo posto in cui entra (se non ce n’è nessuno, viene creato un nuovo build chiamato “Nuovo build”), e un messaggio dice dove è andato o perché non ci stava (“Scegli prima una nave.”). Aggiungere una nave a un build che ne ha già una ti chiede di cliccare ancora per sostituirla. L’EMP Charge si porta, non si monta: va nei razzi del build.

## Build {#builds}

Un **build** è l’equipaggiamento di una nave, scritto con i nomi degli oggetti perché significhi la stessa cosa su ogni server: la nave, i laser con i loro amplificatori, gli scudi, i motori e gli Adaptive Core con le loro celle e i loro propulsori, gli extra, i pezzi negli slot delle abilità, le corazze dello scafo, i droni con ciò che portano, una formazione, e le munizioni e i razzi da portare. Ha anche un nome, una nota, una fase (Inizio, Metà o Fine) e un tipo.

La lista a sinistra ha i **Preset** per fase, **I miei build**, **Nuovo build** e **Importa**; in una finestra stretta è una fila di schede. Scegli un build e vedi la sua plancia, le sue statistiche e i suoi costi.

### Importa {#import}

**Importa** apre un foglio con tre porte:

- **Incolla**: incolla il testo di un build, oppure premi **Incolla dagli appunti**.
- **Da un file**: i file di build nella cartella `exports` della cartella dei dati del gioco (`.spacecorps2027` nella tua cartella personale), la stessa in cui scrive **Salva su file**.
- **Dal mio Hangar**: scegli una delle tue navi e una configurazione, e il gioco legge ciò che è montato: laser e amplificatori, generatori con le loro celle e i loro propulsori, extra, pezzi delle abilità, corazze dello scafo, droni con ciò che portano e il livello della tua Extra Slots CPU. Propone anche la formazione, le munizioni e i razzi della tua barra rapida; spunta quelli che vuoi.

Vedi ciò che entra prima che venga salvato qualcosa, e il gioco ti dice esattamente che cosa non ha potuto importare: un oggetto che non esiste in questo gioco, un pezzo che non va nel suo posto, più pezzi di quanti slot abbia la nave, un build fatto da un gioco più recente. **Importato senza modifiche** significa che è entrato tutto. Poi **Salva in I miei build**, **Apri nell’editor**, oppure chiudi il foglio. I tuoi livelli di [Forgia](/wiki/06-Items/Forge.md), i bonus della Forgia, i livelli dei droni, i booster, il P.E.T., l’aspetto della tua nave e l’altra configurazione dell’[Hangar](/wiki/03-Mechanics/Hangar.md) non fanno parte di un build (importa l’altra configurazione come secondo build).

### I 15 preset {#the-15-presets}

Quindici build sono pronti all’uso: tre fasi del gioco, **Inizio**, **Metà** e **Fine**, con cinque generi in ciascuna. **Farming** ottiene più distruzioni per ciò che costa, **Difesa** ha lo scudo più grande e la rigenerazione più veloce, **Attacco** il danno e la penetrazione maggiori, **Situazionale** sceglie i suoi scontri con occultamento, salti e velocità, e **Tank** ha lo scafo e lo scudo più alti insieme. Un preset non si può modificare: **Modifica una copia** lo apre come tua bozza, e **Aggiungi a I miei build** lo tiene così com’è. Ogni riga mostra il suo Valore in pochi caratteri, calcolato dalle ricette mentre guardi; apri un preset per le sue statistiche e i suoi costi.

### Modifica {#edit}

Un build è disegnato come un hangar: laser, generatori, extra, abilità, corazze e droni, poi il livello della Extra Slots CPU, una formazione e le munizioni e i razzi da portare. Clicca su uno slot vuoto e una lista mostra solo ciò che ci sta, con il suo prezzo o la via per ottenerlo; clicca su un pezzo per **Sostituirlo**, **Aggiungere un modulo** o **Rimuoverlo**. Un drone porta un laser o un nucleo scudo. Se cambi nave, i pezzi che ci stanno ancora restano e il resto viene elencato come tolto. Dai al build un nome, una fase, un tipo e una nota, poi **Salva**, **Salva come copia**, **Elimina** o **Chiudi** (Chiudi chiede prima conferma se ci sono modifiche non salvate).

### Statistiche {#stats}

Sotto la plancia c’è la scheda delle statistiche dell’hangar: punti scafo, danno, portata, prob. critico, scudi e la loro ricarica, assorbimento, velocità, bonus scudo e velocità, penetrazione e, su una nave con slot corazza, lo scafo che le sue corazze aggiungono. La scheda non ha righe per le abilità: i pezzi negli slot delle abilità sono sulla plancia. Il server calcola i numeri con lo stesso codice del tuo hangar, per un build che non è montato su nessuna nave. Due interruttori fissano il **Livello di forgiatura** e il **Livello dei droni** da cui partono i numeri. Una formazione agisce in volo, quindi è elencata come testo e non è contata nei numeri, e lo stesso vale per i booster e per i tuoi livelli di forgiatura.

### Costi {#cost}

I costi hanno quattro blocchi:

- **Totali**: Credits, Thulium, Dark Matter, ogni materia prima con Serve, Hai e Manca, i tempi e il Valore. **Ti serve ancora** è ciò che resta una volta tolto ciò che possiedi.
- **Dove vanno i soldi**: ogni pezzo, il più caro per primo.
- **Passi**: ricerca, ottenere, comprare, pressare e creare, in ordine, per l’intero build. Clicca su un passo Ottenere per vedere dove lo dà il mondo, oppure apri l’oggetto nel Ricettario.
- **Prima di iniziare**: ciò che non è un pezzo, come i livelli della Extra Slots CPU, la ricerca degli slot corazza, i droni che devi ancora comprare e il livello del Nucleo dello Skylab che richiede la Fucina.

Tre interruttori: **Conta quello che ho** (attivo), **Includi quello che è montato** (disattivo) e **Includi munizioni e razzi** (disattivo: si consumano di continuo, quindi non sono il prezzo del build).

## Salvati sul tuo account {#saved-on-your-account}

**I miei build sono salvati sul tuo account**, sul server e non su questo computer, così ti seguono su qualsiasi computer. Puoi tenerne fino a 50; la lista mostra quanti ne hai e, quando è piena, la pagina ti chiede di eliminarne uno per salvarne un altro. Un build è salvato quando lo dice il server: la pagina mostra **Salvataggio…** mentre aspetta, e se il server rifiuta o non è raggiungibile dice perché e il build resta non salvato, con le tue modifiche ancora nell’editor. Un build salvato è fatto solo di nomi di oggetti, qualche etichetta e del nome e della nota che hai scritto, e nessun altro pilota può vederlo. Per darne uno a un amico, esportalo.

## Condividere ed esportare {#share-and-export}

**Esporta** su un build apre un foglio con il build come testo (JSON). **Copialo** per incollarlo in una chat, oppure scegli **Salva su file**, che scrive `spacecorps-build-<name>.json` nella cartella `exports` e non sovrascrive mai un file più vecchio. Un amico incolla il testo in **Importa › Incolla**, oppure mette il file nella propria cartella `exports` e lo sceglie in **Da un file**. Il testo contiene i nomi degli oggetti dell’equipaggiamento, la nave e il nome e la nota del build, e nulla del tuo account.

## Consigli {#tips}

1. **Guarda prima di fare farming.** Apri un oggetto nel Ricettario e leggi le sue Fonti e i suoi Passaggi prima di passare una giornata su un bottino che non è quello che ti serve.
2. **Conta da zero.** Disattiva **Conta ciò che ho** (in Build: **Conta quello che ho**) per vedere quanto costa un oggetto o un build da zero; lascialo attivo per vedere che cosa ti serve ancora.
3. **Parti da un preset.** **Modifica una copia**, cambia un pezzo, e le statistiche e i costi ti seguono.
4. **Leggi anche gli alberi.** Gli [Alberi degli oggetti](/wiki/06-Items/Item-Trees.md) mostrano ogni genere di oggetto uno accanto all’altro, e il Ricettario calcola il prezzo di ognuno per te.
