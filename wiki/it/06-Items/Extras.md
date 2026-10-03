<!-- wiki-i18n source: 46436d9c65bc6c7e -->
<!-- wiki-i18n title: Extra -->
# Extra {#extras}

Gli extra sono i gadget negli **slot extra** di una nave (tre su ogni nave, per configurazione). Ne attivi uno dal selettore Extra della barra rapida o da uno slot della barra rapida a cui l’hai assegnato. Funzionano solo dalla configurazione che stai usando: se ne monti uno nell’altra configurazione, resta in attesa finché non cambi configurazione.

| Extra | Che cosa fa | Usi | Prezzo |
| :---- | :----------- | :--- | :---- |
| **Repair Drone da I a IV** | Ripara il tuo scafo, 1,5%, 2,25%, 3,5% e 5% del massimo al secondo | illimitati | 5000 / 15.000 / 35.000 crediti, 2000 Thulium |
| **Cloaking CPU S** | Nasconde la tua nave | 10 | 5000 Thulium |
| **Cloaking CPU M** | Nasconde la tua nave | 25 | 11.250 Thulium |
| **Cloaking CPU L** | Nasconde la tua nave | 50 | 20.000 Thulium |
| **EMP Charge** | Per 3 secondi nessuno può bersagliarti, ogni aggancio su di te si spezza e ogni occultamento vicino a te termina | 1 | 500 Thulium |

I Cloaking CPU e l’EMP Charge si vendono solo nel Negozio. Non si possono fondere e non vengono mai regalati.

## Repair Drone {#repair-drones}

Attiva un Repair Drone (REP) e ripara lo scafo finché non è pieno. Parte solo dopo 10 secondi senza subire colpi e qualsiasi colpo lo spegne. Se ne hai montati diversi, lavora il migliore. I valori sono in [Combattimento](/wiki/03-Mechanics/Combat.md).

## Cloaking CPU {#cloaking-cpu}

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
- **Che cosa vedi.** La tua nave diventa trasparente con un contorno viola tratteggiato, e un indicatore in alto sullo schermo dice “Occultato” con gli usi rimasti (niente secondi: non c’è nessun timer). Lo slot CLK mostra gli usi rimasti; mentre sei occultato si illumina di viola e dice ON, e quando l’occultamento finisce, comunque sia finito, si oscura e conta i 60 secondi di ricarica. Una pressione rifiutata dal server (ricarica, zona sicura, un colpo subito o sparato negli ultimi 10 secondi) fa lampeggiare lo slot di rosso, e un messaggio ti dice perché. Un alleato appare come un fantasma pallido con un contrassegno da fantasma davanti al nome, e un pilota che si occulta vicino a te svanisce in un’increspatura. Trascina CLK dagli Extra della barra rapida su uno slot per usarlo, come REP.
- Gli **usi** sono salvati con la CPU. Disconnettersi, morire o riavviare il gioco non ne restituisce nessuno, e un’attivazione che annulli viene comunque spesa. Quando se ne va l’ultimo uso di un pacchetto, questo si esaurisce e il suo slot viene riempito con un’altra CPU dello stesso tipo che hai nell’inventario, se ne possiedi una di scorta.
- **Più CPU** nella stessa configurazione non si sommano. Si usa per prima quella con meno usi rimasti.

S, M e L si comportano allo stesso modo: i pacchetti più grandi costano solo meno per uso (500, 450 e 400 Thulium).

## EMP Charge {#emp-charge}

Premi lo slot EMP durante uno scontro. Per **3 secondi** nessuno può agganciarti e **tutti quelli che ti avevano agganciato perdono l’aggancio** all’istante, ovunque si trovino: piloti, alieni e piloti di corporazione. A un pilota il cui aggancio si spezza compare il messaggio “Aggancio perso: il bersaglio ha usato un EMP”. Chi prova ad agganciarti in quei 3 secondi viene rifiutato.

- **Non è invulnerabilità.** Ferma ciò che richiede un aggancio: i laser, i razzi guidati e il tocco di un razzo dritto a bersaglio singolo, che ti attraversa. Un’**esplosione ad area** non richiede aggancio, quindi ti colpisce comunque se sei al suo interno, e il buco nero non è affatto uno sparo.
- **Puoi comunque agire.** Sparare non lo interrompe. Puoi occultarti (se lo permettono le regole dell’occultamento) e usare altri extra.
- **Interrompe gli occultamenti vicini.** Ogni nave occultata entro **1500 unità** da te quando l’impulso esplode viene mostrata subito e la sua CPU inizia i suoi 60 secondi di ricarica, a qualunque corporazione appartenga, compresa la tua; le navi del tuo [gruppo](/wiki/03-Mechanics/Groups.md) sono l’eccezione: mantengono l’occultamento. Al pilota compare “Occultamento interrotto: un EMP è esploso nelle vicinanze.”, vede la nave riapparire con la stessa increspatura di qualsiasi fine di un occultamento, e lo slot inizia la sua ricarica. Non puoi usare un EMP mentre sei occultato.
- **Non nasconde nulla.** Tutti ti vedono ancora, con un guscio elettrico crepitante attorno alla nave per i 3 secondi.
- **Non puoi usarlo** mentre una zona sicura ti protegge, mentre sei occultato o entro **30 secondi** dall’ultimo. Funziona ovunque altrove, compresi i primi giorni di una stagione (il Protocollo di pace): in quel periodo gli alieni danno comunque la caccia.
- Un alieno che colpisci durante i 3 secondi non si rivolta contro di te finché non sono finiti. Le tue rivendicazioni di abbattimento e le regole del primo colpo non cambiano.
- **Che cosa vedi.** Un impulso di spazio deformato parte dal pilota e si allarga fino a dove l’impulso interrompe gli occultamenti (1500 unità), lo vedono tutti quelli nel raggio, e un guscio elettrico crepitante circonda la nave per i 3 secondi, con un anello attorno alla tua nave e un indicatore in alto sullo schermo che contano il tempo. L’anello del bersaglio di chiunque ti avesse selezionato si spezza, con una breve scarica. Lo slot EMP mostra le cariche che possiedi, si illumina di blu finché il guscio è attivo e si oscura mentre si ricarica.
- **Una carica, un uso.** Lo slot viene riempito dal tuo inventario se ne possiedi altre. I **30 secondi** di ricarica non vengono salvati: disconnetterti o saltare attraverso un portale li azzera, e l’impulso successivo costa una carica.
