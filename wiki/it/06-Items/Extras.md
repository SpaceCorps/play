<!-- wiki-i18n source: 705e5e6b80d24ab7 -->
<!-- wiki-i18n title: Extra -->
# Extra {#extras}

Gli extra sono i gadget negli **slot extra** di una nave (due su Protos, Kitefin, Ostirion e Nomad, le navi con cui inizi o che compri, e tre su Paragon, Ironclad, Wraith e Storm, le navi che costruisci, per configurazione, e 3, 5 o 7 in più con le Extra Slots CPU). Ne attivi uno dal selettore Extra della barra rapida o da uno slot della barra rapida a cui l’hai assegnato. Funzionano solo dalla configurazione che stai usando: se ne monti uno nell’altra configurazione, resta in attesa finché non cambi configurazione.

| Extra | Che cosa fa | Usi | Prezzo |
| :---- | :----------- | :--- | :---- |
| **Repair Drone da I a IV** | Ripara il tuo scafo, 1,5%, 2,25%, 3,5% e 5% del massimo al secondo | illimitati | 5000 / 15.000 / 35.000 crediti, 2000 Thulium |
| **Cloaking CPU S** | Nasconde la tua nave | 10 | 5000 Thulium |
| **Cloaking CPU M** | Nasconde la tua nave | 25 | 11.250 Thulium |
| **Cloaking CPU L** | Nasconde la tua nave | 50 | 20.000 Thulium |
| **P.E.T. Station da I a III** | Su ON, lascia che 2, 3 o 5 [P.E.T.](/wiki/03-Mechanics/Pets.md#the-station) agganciati diano boost alla tua nave, guadagnino esperienza e lavorino; su OFF non fanno nulla di tutto questo | ON / OFF | Assemblaggio, dopo la sua ricerca (l’albero degli oggetti qui sotto) |
| **Auto-Rocket CPU** | Su ON, spara da sola il tuo razzo attivo sul bersaglio di un combattimento | ON / OFF | Assemblaggio, dopo la sua ricerca (l’albero degli oggetti qui sotto) |

Le Cloaking CPU si vendono solo nel Negozio. Non si possono fondere e non vengono mai regalate. L’**EMP Charge** non è più un extra: dalla 0.4.21 è un consumabile, che si porta in una pila come un razzo e non si monta in nessuno slot, quindi non occupa nessuno dei tuoi slot extra (vedi [Razzi](/wiki/06-Items/Rockets.md#emp-charge)). Anche le due **Energetic Wall** non sono più extra: dalla 0.4.22 sono consumabili anch’esse, si portano in una pila e non vanno in nessuno slot (vedi [Energetic Wall](#energetic-wall)).

Il **kit iniziale** di un nuovo pilota monta già due extra nei due slot extra della Protos: una **Base CPU I** (10 usi, un teletrasporto alla base della tua corporazione) e un **Repair Drone I**. Trascinali dal selettore Extra della barra rapida su uno slot per usarli. Solo i nuovi piloti ricevono il kit: chi si è arruolato prima della 0.4.10 non ce l’ha.

Altre otto CPU non si vendono: l’Assemblaggio le crea quando il Centro ricerche dello Skylab le ha ricercate (vedi [Ricerca](/wiki/03-Mechanics/Research.md)). Sono le Extra Slots CPU I, II e III, la Jump CPU, le Base CPU I e II, l’Auto-Repair CPU e l’Auto-Rocket CPU, e [l’ultima sezione](#research-cpus) dice che cosa fa ciascuna. Come la Cloaking CPU, la Jump CPU e le Base CPU sono per un momento tranquillo: nessuna delle tre parte entro 10 secondi da un colpo che spari o da un colpo che subisci. Le due CPU warp, la Jump CPU e le Base CPU, vengono rifiutate anche finché trasporti un oggetto della missione (“Non puoi usare un CPU warp mentre trasporti un oggetto della missione.”): vedi [Oggetti della missione](/wiki/03-Mechanics/Quests.md#quest-items).

Ogni extra ha una sigla breve sul suo slot della barra rapida: **REP** per un Repair Drone, **CLK** per una Cloaking CPU e **ARP**, **ARL**, **BSE** e **JMP** per l’Auto-Repair CPU, l’Auto-Rocket CPU, le Base CPU e la Jump CPU. I consumabili hanno le loro: **EMP** e **WAL** (per una Energetic Wall). I tre oggetti **P.E.T. Station** sono extra come gli altri, con la sigla **PET**: montane uno e il suo slot porta la Station su **ON** o **OFF** (un secondo fra due pressioni) e mostra quale. Su ON i [P.E.T.](/wiki/03-Mechanics/Pets.md) agganciati contano, su OFF no. L’**Auto-Rocket CPU** si commuta allo stesso modo, su ON o OFF. Punta uno slot per leggere che cosa fa ora una pressione, o perché non può.

![The Extras picker of the hotbar: the Repair Drone, the Auto-Repair, Cloaking, Base and Jump CPUs and the P.E.T. Station you have fitted (REP, ARP, CLK, BSE, JMP, PET): click one to use it, or drag it onto a slot](../../img/wiki-img/shots/cpu-hotbar.jpg)
![The Consumables picker of the hotbar: the EMP Charge and the Energetic Wall I and II (EMP, WAL), with how many of each you hold: click one to use it, or drag it onto a slot](../../img/wiki-img/shots/emp-hotbar.jpg)
![The hotbar with extras on its slots: a Repair Drone, a Cloaking CPU with its uses left, the P.E.T. Station that says ON, the EMP Charge and the Energetic Wall I and II with the number of each you carry](../../img/wiki-img/shots/hotbar-slots.jpg)
![The Repair Drone of an extra slot docked to its ship and its wingmen](../../img/wiki-img/shots/repair-drones-extra.jpg)
![The Shop's Consumables category: the EMP Charge and the Energetic Wall I with their prices in Thulium, and the Energetic Wall II, which only Assembly makes](../../img/wiki-img/shots/shop-consumables.jpg)

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Albero degli oggetti {#item-tree}

Ciò che crea l’Assemblaggio richiede prima la sua tecnologia; passa il puntatore su un oggetto per vedere quanto tempo serve a ricercarla. L’albero delle tecnologie, il carburante e il boost: [Ricerca](/wiki/03-Mechanics/Research.md).

```tree
P.E.T. Station I | extra, common | craft 100000 Credits, 2000 Thulium, 300 s | research 10800 s, 10800 science | 25 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md
Cloaking CPU S | extra, common | buy 5000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Repair Drone I | extra, common | buy 5000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone II | extra, common | buy 15000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone III | extra, common | buy 35000 Credits | /wiki/06-Items/Extras.md#repair-drones
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
P.E.T. Station II | extra, uncommon | craft 400000 Credits, 6000 Thulium, 600 s | research 36000 s, 36000 science | 60 Ship Fragment, 6 Reinforced Hull Plate, 4 Power Core, 8 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md
Cloaking CPU M | extra, uncommon | buy 11250 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 2 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Extras.md#base-cpus
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu
P.E.T. Station III | extra, rare | craft 1500000 Credits, 18000 Thulium, 900 s | research 86400 s, 86400 science | 120 Ship Fragment, 12 Reinforced Hull Plate, 8 Power Core, 2 Ancient Control Unit, 12 Velkonite Reinforced Plate, 4 Orvium Reinforced Plate | /wiki/06-Items/Extras.md
Auto-Rocket CPU | extra, rare | craft 20000 Thulium, 900 s | research 36000 s, 36000 science | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 1 Ancient Control Unit, 8 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-rocket-cpu
Repair Drone IV | extra, rare | buy 2000 Thulium | /wiki/06-Items/Extras.md#repair-drones
Cloaking CPU L | extra, rare | buy 20000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 6 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu

P.E.T. Station I -> P.E.T. Station II -> P.E.T. Station III
Cloaking CPU S -> Cloaking CPU M -> Cloaking CPU L
Repair Drone I -> Repair Drone II -> Repair Drone III -> Repair Drone IV
Extra Slots CPU I -> Extra Slots CPU II -> Extra Slots CPU III
Base CPU I -> Base CPU II
```
<!-- item-tree:end -->

## Repair Drone {#repair-drones}

Attiva un Repair Drone (REP) e ripara lo scafo finché non è pieno. Parte solo dopo 10 secondi senza subire colpi e qualsiasi colpo lo spegne. Se ne hai montati diversi, lavora il migliore. Una [Auto-Repair CPU](#auto-repair-cpu) lo riattiva al posto tuo. I valori sono in [Combattimento](/wiki/03-Mechanics/Combat.md). Mentre ripara, piccoli droni di riparazione escono dalla nave, le girano attorno e colpiscono lo scafo con i loro raggi, uno per un Repair Drone I, due per un II, tre per un III o un IV, e i piloti vicini li vedono; tornano ad agganciarsi quando la riparazione si ferma.

## Cloaking CPU

Premi lo slot CLK per occultarti. **Una pressione è un uso**, qualunque sia il pacchetto, e gli usi rimasti li vedi sullo slot e nell’Hangar. L’occultamento **non ha limite di tempo**: resta attivo finché non lo spegni o qualcosa non lo interrompe.

- **Chi non può vederti.** I piloti delle altre corporazioni e gli alieni non vedono affatto la tua nave: non è sul loro schermo né nella loro lista dei bersagli, e nessuno può agganciarla. Anche i piloti di corporazione delle altre corporazioni la ignorano.
- **Il punto sul radar.** Ogni altro pilota sulla mappa, tranne quelli della tua corporazione, vede sulla minimappa un semplice **punto rosso** dove ti trovi, così sa che nei paraggi c’è qualcuno occultato. Il punto non ha nome, nave, corporazione né ID e non si può cliccare né bersagliare; il suggerimento che compare passandoci sopra dice soltanto “Qui c’è qualcosa di occultato”. È rotondo, dentro un anello (le navi sulla minimappa sono quadrati), e l’anello “respira” lentamente, oppure resta fermo se hai attivato Riduci movimento. Il server lo aggiorna circa due volte al secondo e il tuo gioco lo muove in modo fluido nel frattempo. Dice che qualcuno c’è e dove, non chi: un pilota che ti ha visto occultarti può seguire il punto, e l’**esplosione di un razzo** mirata lì ti trova comunque.
- **Chi può vederti.** Tu vedi la tua nave, sbiadita e con un contorno. I piloti della tua corporazione ti vedono come un fantasma pallido; i compagni di clan di altre corporazioni no, perché un clan accoglie chiunque faccia domanda. Nessuno può bersagliare il fantasma, nemmeno la tua corporazione.
- **Non puoi occultarti** in una zona sicura, mentre la CPU si ricarica o entro **10 secondi** da un colpo subito o sparato.
- **Che cosa lo interrompe.** Premere di nuovo lo slot, la tua prima raffica o il tuo primo razzo (arriva a segno e vieni visto), entrare in una zona sicura, la CPU che esce dalla configurazione che stai usando, un **EMP che esplode entro 1500 unità** da te, chiunque l’abbia lanciato (anche quello della tua corporazione, ma non quello di un compagno di gruppo) e l’esplosione ad area di un razzo che ti colpisce. Il tempo no, raccogliere carico no (una cassa che prendi sparisce per tutti, quindi sanno che qualcosa era a portata da quel punto, non chi), le abilità no, e le radiazioni del buco nero danneggiano una nave occultata ma non ne interrompono l’occultamento. Disconnettersi o morire lo interrompe, perché una nave che non è pilotata non è occultata.
- **Ricarica.** Dopo la fine di un occultamento, comunque sia finito, la CPU si ricarica per **60 secondi**. La ricarica appartiene a te, non alla nave: continua se salti attraverso un portale, ti disconnetti o muori. Ogni pressione costa comunque un uso.
- Gli **alieni** che ti stavano inseguendo ti perdono. Le tue rivendicazioni di abbattimento vengono rilasciate quando ti occulti.
- **Razzi.** Nessuno può agganciarti con un razzo guidato e un razzo dritto a bersaglio singolo ti attraversa. Un’**esplosione ad area** danneggia comunque una nave che copre e ne interrompe l’occultamento, e ai piloti che possono vedere la posizione della nave questa viene mostrata prima che compaia il numero del danno. Lanciare un razzo è uno sparo: interrompe il tuo occultamento come una raffica (la CPU poi si ricarica per i 60 secondi indicati sopra) e, occultato o no, ti impedisce di occultarti per i 10 secondi successivi.
- Il **buco nero** inghiotte una nave occultata come qualsiasi altra, e lo sente tutta la mappa.
- **Che cosa vedi.** La tua nave diventa trasparente con un contorno viola tratteggiato, i suoi droni svaniscono con lei, e un indicatore in alto sullo schermo dice “Occultato” con gli usi rimasti (niente secondi: non c’è nessun timer). Lo slot CLK mostra gli usi rimasti; mentre sei occultato si illumina di viola e dice ON, e quando l’occultamento finisce, comunque sia finito, si oscura e conta i 60 secondi di ricarica. Una pressione rifiutata dal server (ricarica, zona sicura, un colpo subito o sparato negli ultimi 10 secondi) fa lampeggiare lo slot di rosso, e un messaggio ti dice perché. Un alleato appare come un fantasma pallido con un contrassegno da fantasma davanti al nome, e un pilota che si occulta vicino a te svanisce in un’increspatura. Trascina CLK dagli Extra della barra rapida su uno slot per usarlo, come REP.
- Gli **usi** sono salvati con la CPU. Disconnettersi, morire o riavviare il gioco non ne restituisce nessuno, e un’attivazione che annulli viene comunque spesa. Quando se ne va l’ultimo uso di un pacchetto, questo si esaurisce e il suo slot viene riempito con un’altra CPU dello stesso tipo che hai nell’inventario, se ne possiedi una di scorta.
- **Più CPU** nella stessa configurazione non si sommano. Si usa per prima quella con meno usi rimasti.

S, M e L si comportano allo stesso modo: i pacchetti più grandi costano solo meno per uso (500, 450 e 400 Thulium).

## Energetic Wall

Premi lo slot WAL e una **parete di plasma** si erge **sul tuo cursore**, di traverso rispetto alla linea che va dalla tua nave fino a lì: una striscia lunga 360 unità (circa tre modelli di nave e mezzo) e larga 10 unità. Il suo centro sta al massimo a **450 unità** dal centro della nave: un cursore più lontano la mette a 450 unità lungo la linea, uno a meno di 120 unità la spinge fuori fino a 120. Finché lo slot è pronto, una linea tratteggiata tenue e un contorno fantasma mostrano dove sorgerà. Se il gioco non sa dove sia il tuo cursore, si erge a 220 unità davanti al centro della nave, di traverso rispetto alla rotta. Una Energetic Wall è un **consumabile**, come l’[EMP Charge](/wiki/06-Items/Rockets.md#emp-charge): una pila nel tuo inventario che non occupa **nessuno slot** di nessuna nave (fino alla 0.4.22 era un extra). Trascinala dai Consumabili della barra rapida su uno slot per usarla; i due livelli sono due voci, quindi uno slot ne tiene uno. Serve per nascondersi dietro e per sbarrare un corridoio, non per starci dentro.

- **Cosa ferma.** Ogni colpo che la attraversa colpisce invece la parete, chiunque l’abbia sparato e da qualunque lato: una salva di laser, un razzo, la salva di un alieno. Ciò che sta dietro non subisce nulla e sono i punti ferita della parete a prendere il danno. L’esplosione di un razzo che scoppia sulla parete colpisce le navi sul suo lato vicino e non quelle dietro. Anche i tuoi colpi: non puoi sparare all’esterno attraverso la tua stessa parete. La N.I.K.E. e le torrette del Dormant Swamp la sorvolano, come sorvolano gli asteroidi.
- **Cosa brucia.** Ogni nave il cui scafo tocca la striscia subisce **2.500 di danno al secondo**, prima sullo scudo, anche la tua, anche alieni e piloti delle corporazioni. Una nave in una zona sicura o sotto la protezione di un respawn non brucia, e due strisce su una nave non si sommano.
- **Quanto dura.** Una parete di livello 1 ha **30.000 punti ferita**, una di livello 2 **90.000**. Una parete ne perde da sola un sessantesimo ogni secondo, quindi una che nessuno colpisce sparisce dopo **60 secondi**. I colpi accorciano questo tempo: una Wraith con dodici Helios Beam e munizioni x4 abbatte una parete di livello 1 in circa 3,5 secondi.
- **Una alla volta, una parete a pressione.** Una nuova parete prende il posto della vecchia. Dopo una pressione l’oggetto si ricarica per **90 secondi**; l’attesa è tua, non della nave: morire o disconnettersi non la accorcia. Una pressione consuma **una parete del livello che lo slot tiene**, e solo quando la parete sta in piedi: una pressione che il gioco rifiuta (più sotto) non consuma nulla e non avvia nessuna attesa. Se di quel livello non ne resta nessuna, dice «Non hai più Energetic Wall.» e l’altro livello non viene mai consumato al suo posto.
- **Dove no.** Non mentre una zona sicura o un respawn ti protegge, non dove la striscia toccherebbe una zona sicura o una porta, non con l’occultamento attivo e non dove il centro della striscia cadrebbe fuori dalla mappa. Il gioco dice qual è il caso.
- **Abbattimenti.** Una nave che la parete distrugge muore per radiazione, e l’abbattimento va all’ultimo pilota nemico che l’ha colpita nei 15 secondi precedenti, se ce n’è stato uno. Chi ha alzato la parete non riceve credito per ciò che non ha sparato lui stesso. Un alieno che la parete distrugge non paga nulla: né ricompensa né bottino.
- **Gli alieni non la aggirano.** La attraversano e bruciano, oppure restano sul loro lato e sparano alla parete.
- **Cosa vedi.** Una striscia di luce bianco-azzurra con trattini luminosi che la percorrono e un palo di luce a ogni estremità, che lampeggia dove cade un colpo e sfarfalla quando è quasi esaurita. Una parete di livello 2 brilla invece di giallo, con un nucleo più spesso e luminoso e un bagliore più forte, ma la sua striscia è larga 10 unità come quella di livello 1. Una sottile barra della vita accanto si accorcia e passa all’ambra e poi al rosso; il tuo slot mostra la vita residua della tua parete come arco e l’attesa come ombra. Una parete appena alzata si accende con un lampo, una abbattuta crolla in scintille e una il cui tempo è scaduto svanisce. Sul tuo slot un numero conta anche le pareti del suo livello che ti restano.
- **Come ottenerla e portarla.** L’Energetic Wall I si vende nel Negozio a **250 Thulium** la parete, e ne porti fino a **20** in una pila (conta anche ciò che hai messo in vendita all’[Asta](/wiki/03-Mechanics/Auction.md)). L’Energetic Wall II si crea in Assemblaggio, **una parete per lavorazione**, per **600 Thulium**, 5 Ship Fragment e un Power Core, quando il Centro ricerche l’ha ricercata (6 ore a velocità normale: [Ricerca](/wiki/03-Mechanics/Research.md)); ne porti fino a **10**. Come i razzi, le pareti che porti si perdono con la stagione se non le metti nel Deposito di trasporto, e quelle nel Deposito non si possono usare. Un’Energetic Wall II che hai creato si può vendere all’Asta; un’Energetic Wall I, che vende il Negozio, mai.

## CPU del Centro ricerche {#research-cpus}

Due delle CPU richiedono Dark Matter Plate, come l’ultimo tier di ogni catena di potenziamento: l’**Extra Slots CPU III** ne richiede 4 (più 2 Ancient Control Unit e 6 Orvium Reinforced Plate) e il **Base CPU II** 4 (più una Ancient Control Unit e 2 Orvium Reinforced Plate), quindi ricerca prima la Dark Matter Plate ([Dark Matter e Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)).

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | Tempo di ricerca | Richiede prima | Thulium per la creazione | Tempo di creazione |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 min | – | 12.000 | 5 min |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10 h | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30.000 | 10 min |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1 g | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75.000 | 15 min |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3 h | – | 8.000 | 5 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10 h | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | 20.000 | 10 min |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1 g | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40.000 | 15 min |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6 h | – | 15.000 | 10 min |
| [Energetic Wall II](/wiki/06-Items/Extras.md#energetic-wall) | 6 h | – | 600 | 2 min |
| [Auto-Rocket CPU](/wiki/06-Items/Extras.md#auto-rocket-cpu) | 10 h | – | 20.000 | 15 min |

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

### Auto-Rocket CPU

- **Che cosa fa.** Finché è su ON e sei in combattimento (i tuoi laser sono su un alieno o su un pilota nemico), spara da sola il tuo razzo attivo, l’ultimo che hai lanciato, su quel bersaglio, ogni volta che la pressione del tasto Lancia razzo funzionerebbe: il timer dei razzi è pronto e te ne resta uno. Il server controlla ogni lancio come controlla i tuoi.
- **L’interruttore.** Montala in uno slot Extra e premi il suo slot ARL per portarla su ON o OFF. Parte su OFF e resta come l’hai lasciata, anche quando accedi di nuovo. Lo slot dice ON o OFF e si illumina quando la CPU spara.
- **Che cosa non fa mai.** Non sceglie mai un bersaglio, non spara mai agli asteroidi, né da una zona sicura, né con l’occultamento attivo, e non spara mai un razzo N.U.K.E. o N.I.K.E. Un razzo che lanci tu funziona sempre. Se per 3 minuti non premi un tasto, non fai clic né muovi il mouse, aspetta che tu faccia qualcosa.
- **Razzi finiti.** Te lo dice una volta e torna a sparare appena ne hai altri.


<!-- research-cpus:end -->
