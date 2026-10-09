<!-- wiki-i18n source: 0c1a854ca2f3f87c -->
<!-- wiki-i18n title: Combattimento -->
# Meccaniche di combattimento {#combat-mechanics}

Questa sezione spiega nel dettaglio come il danno viene calcolato, applicato e riparato durante gli scontri in SpaceCorps.

![The death screen: respawn at the nearest portal or on the spot, each with its lock](../../img/wiki-img/shots/death.jpg)
![The flight screen in a fight: ship and pilot windows, the target, the hotbar, the chat, the log and the minimap](../../img/wiki-img/shots/hud-fight.jpg)
![The Target window: the alien, its distance, hull and shield](../../img/wiki-img/shots/hud-target.jpg)

## Calcolo del danno {#damage-calculation}

Quando una nave spara con i suoi laser, il server calcola il danno prodotto con questa sequenza:

### 1. Danno base e variazione casuale {#1-base-damage-random-variance}

Si somma il danno base di tutti i laser equipaggiati (compresi i laser sui droni) e dei loro amp laser montati.
- **Tiro casuale**: il danno effettivo di una raffica è casuale, tra l’**80%** e il **100%** del danno base totale.
  - Formula: `Roll = (0.8 + (Random * 0.2)) * BaseDamage`

### 2. Colpi critici {#2-critical-hits}

Ogni raffica ha una probabilità di essere un colpo critico.
- **Probabilità critica**: la probabilità critica media dei laser equipaggiati più la somma delle probabilità critiche di tutti gli amp laser equipaggiati.
- **Moltiplicatore critico**: se un colpo è critico, il tiro del danno viene moltiplicato per **1,5x**. Il numero del danno di una raffica critica è mostrato in azzurro ghiaccio, più grande, con un “!” (vedi [Numeri di danno e di cura](#damage-and-heal-numbers)).
- Quantum Laser I e II non hanno una probabilità critica propria: la danno i loro amp.
- **Danno critico fisso**: l’eventuale danno critico fisso degli amp laser viene aggiunto dopo il moltiplicatore.
  - Formula: `CritDamage = (Roll * 1.5) + FixedCritDamage`

### 3. Moltiplicatori globali {#3-global-multipliers}

Infine si applicano i moltiplicatori globali (come i booster attivi, per esempio il +10% di un Laser Damage Booster, o i moltiplicatori delle munizioni laser, per esempio x2, x3, x4) per ottenere il danno finale:
- Formula: `FinalDamage = Damage * AmmoMultiplier * (1.0 + BoosterDamagePercent)`
- Una [formazione di droni](/wiki/03-Mechanics/Formations.md) indossata può moltiplicare ancora il risultato: per esempio Auger +21% di danno laser, Gyre −11% e, contro gli alieni, Culler +12% (un fattore a parte, non compreso nella percentuale dei booster).
- Le munizioni **Siphon Battery** hanno il moltiplicatore x1 ma un bersaglio diverso: il loro danno esce solo dallo scudo del bersaglio (mai dallo scafo, qualunque sia l’assorbimento) e va nel tuo scudo, fino al tuo massimo. Vedi [Laser e munizioni](/wiki/06-Items/Lasers.md).

### 3b. Razzi {#3b-rockets}

Un [razzo](/wiki/06-Items/Rockets.md) ha un proprio danno (un Lancet I fa da 1.700 a 2.100, un Lancet III da 5.200 a 6.200, un N.U.K.E. da 45.000 a 50.000), stabilito a caso una volta quando lo lanci e uguale per ogni nave: i tuoi laser, amp, booster e munizioni non lo cambiano, e non ha colpo critico. Tutti i razzi condividono un’unica ricarica di **3 secondi**. Un razzo a bersaglio singolo ha una **penetrazione dello scudo**: viene tolta dall’assorbimento del tuo bersaglio (vedi Subire danni più sotto); un’esplosione danneggia ogni nave nel suo raggio, il numero intero al centro e la metà al bordo. Niente limita ciò che un razzo toglie alla nave di un pilota: prima lo scudo, poi lo scafo. I razzi non colpiscono mai la tua corporazione né il tuo [gruppo](/wiki/03-Mechanics/Groups.md), di qualunque corporazione siano i suoi membri. Una [formazione di droni](/wiki/03-Mechanics/Formations.md) indossata è l’unica cosa che cambia entrambe: una formazione per razzi aumenta il danno di ogni razzo (fino a +55%), e alcune allungano o accorciano il timer. Gli [asteroidi](/wiki/03-Mechanics/Asteroid-Mining.md) subiscono danni dai razzi e dai laser al 5% di quello che una raffica fa a una nave (contano i tuoi amp, booster, munizioni e colpi critici, poi si toglie la corazza dell’asteroide); i droni non fanno nulla, e un razzo colpisce solo l’asteroide contro cui è stato sparato.

### 4. Voltarsi verso il bersaglio {#4-facing-the-target}

Una nave o un alieno che ha agganciato un bersaglio e spara si volta verso di esso, in qualunque direzione stia volando (girando in cerchio, arretrando o fermo), e torna alla sua rotta quando smette di sparare.

### 5. Portata {#5-range}

Una nave spara una raffica al secondo finché il suo bersaglio è entro la sua **portata**, e trattiene il fuoco finché il bersaglio è più lontano: il fuoco smette di consumare munizioni finché il bersaglio non è di nuovo abbastanza vicino, e la finestra Bersaglio dice “Fuori portata”. La portata è **la media delle portate di tutti i tuoi laser** (compresi i laser nei tuoi droni), arrotondata all’unità più vicina, ed è un unico numero per tutta la nave: entro di essa spara ogni laser, fuori nessuno. Un laser a lungo raggio accanto a laser corti quindi non allunga la tua portata: una Starfire-III (850) e due Quantum Laser II (700) fanno 750. Un bonus di portata della Forgia conta sul proprio laser prima della media. Una nave senza laser non può sparare con i laser, e l’Hangar non mostra alcuna portata per essa (un trattino); i suoi razzi sparano comunque, ciascuno con la propria portata (vedi [Razzi](/wiki/06-Items/Rockets.md)). Per la portata di ciascun laser vedi [Laser e munizioni](/wiki/06-Items/Lasers.md).

## Numeri di danno e di cura {#damage-and-heal-numbers}

Un colpo appare come un numero che fluttua sopra la nave che colpisce. **I tuoi numeri** si vedono sempre: il danno che infliggi, il danno che subisci e le tue riparazioni. **La nave sotto il tuo cerchio di aggancio** ne mostra di più: ogni colpo e ogni cura che riceve, **da qualsiasi fonte**. Cioè i laser, i razzi e i droni di altri piloti, gli alieni, i Clan Warden e le riparazioni e la rigenerazione dello scudo della nave stessa. Quando un altro spara al tuo bersaglio, vedi il suo danno.

- **Colori.** Oro: danno a un alieno o a un pilota nemico. Rosso con un meno: danno a una nave che proteggi (un pilota della tua corporazione o del tuo gruppo) e il danno che subisci tu. Verde con un più: una cura, come una Emergency Repair, un Repair Drone o uno scudo che torna. “Miss” in argento chiaro: un colpo diretto che la schivata di una formazione ha deviato. Una raffica critica è più grande e finisce con un “!” (azzurro ghiaccio quando colpisce un alieno o un nemico).
- **I tuoi restano più luminosi.** I numeri degli altri sul tuo bersaglio sono un po’ più piccoli e più tenui, e stanno in una colonna a destra della nave, così non coprono mai i tuoi.
- **Un numero per una folla.** I colpi che arrivano insieme si sommano in un solo numero con un conteggio dopo (`×35`). Quaranta piloti che sparano a una nave fanno circa due numeri al secondo, e mai più di sette. Le cure compaiono una volta al secondo.
- **Solo la nave sotto il cerchio.** Ogni altra nave mostra solo i tuoi colpi e i colpi che subisci. Le radiazioni del buco nero e il drenaggio di scudo di una formazione non hanno numeri: si vedono sulle barre.
- **L’impostazione.** Impostazioni › Interfaccia › **Mostra il danno inflitto da altri al mio bersaglio**, attiva di default. Se la disattivi, vedi solo i tuoi numeri. **Riduci movimento** tiene fermi tutti i numeri: nessuno compare di scatto né sale.

---

## Ricompense degli abbattimenti: la rivendicazione del primo colpo {#kill-rewards-first-hit-claims}

Le ricompense di un alieno vanno al pilota che gli ha sparato per primo, non a chi mette a segno l’ultimo colpo.

- **Rivendicare**: il primo pilota il cui colpo danneggia un alieno lo rivendica. Ogni tuo colpo rinnova la tua rivendicazione.
- **Perderla**: se non colpisci l’alieno per **10 secondi**, la tua rivendicazione decade e il prossimo pilota che lo colpisce la ottiene. La tua rivendicazione finisce anche quando la tua nave viene distrutta o lasci la mappa (attraverso un portale, o uscendo dal gioco), e tornare entro i 10 secondi non la riporta indietro.
- **L’abbattimento**: quando l’alieno viene distrutto, il pilota che ne detiene la rivendicazione ottiene tutto: crediti, Thulium, XP, onore, l’abbattimento per le missioni e per i punti reset, e la cassa di [carico](/wiki/03-Mechanics/Cargo.md). Un pilota che finisce un alieno rivendicato da un altro non ottiene nulla, e il Registro di gioco lo dice. Quando la tua rivendicazione paga e un altro pilota mette a segno l’ultimo colpo, il Registro di gioco nomina quel pilota e dice che la tua rivendicazione paga te.
- **Punti classifica**: l’abbattimento aggiunge anche punti PvE alla classifica del pilota che detiene la rivendicazione, tanti di più quanto più è resistente l’alieno: 1 per un Seeker, 2 per un Phantasm, 4 per un Bulwark, 7 per un Goombah e 16 per un Crystalys (l’articolo di ogni alieno indica il suo). Sono solo del pilota che abbatte: la quota di ricompense di un gruppo non li comprende.
- **Vederla**: quando selezioni un alieno rivendicato da un altro pilota, la finestra Bersaglio mostra *Rivendicato da* quel pilota e *Senza premio*.
- I [piloti di corporazione](/wiki/03-Mechanics/Company-Pilots.md) non rivendicano mai un alieno, e un alieno che finiscono paga comunque il pilota che ne detiene la rivendicazione.
- Un pilota in un [gruppo](/wiki/03-Mechanics/Groups.md) condivide ciò che paga la sua rivendicazione con i compagni di gruppo che sono vicini e stanno sparando; la rivendicazione in sé è solo del pilota.
- **I capi degli [sciami](/wiki/05-Swarms/Swarms.md), le Dormant Pulse e i [Clan Warden](/wiki/03-Mechanics/Clans.md#warden-pay-and-loot) sono l’eccezione**: un boss di sciame, ogni Dormant Pulse e ogni Clan Warden pagano in base al danno che ha inflitto loro ogni pilota, non in base al primo colpo, e la loro cassa di carico va al pilota che ha inflitto più danno ([come paga l’abbattimento di un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Gli altri seguaci, i Pirate Scout e i Seeker Slave, pagano in base alla rivendicazione, come ogni alieno. I punti PvE di una nave di sciame sono nella pagina Sciami.

---

## Alieni che reagiscono soltanto {#aliens-that-only-fight-back}

Il Seeker e il Goombah non iniziano mai uno scontro. Ciascuno si rivolta contro un pilota che lo colpisce (un colpo che fa danno; il fuoco di un altro alieno non lo provoca mai), combatte il pilota descritto nella sezione [Contro chi combatte un alieno](#who-an-alien-fights) e lascia perdere **10 secondi** dopo che qualcuno l’ha colpito per l’ultima volta. Lasciato in pace per **30 secondi**, il suo scafo si ripara del 2% del massimo al secondo. Gli altri alieni (Phantasm, Bulwark, Crystalys) attaccano qualsiasi pilota non protetto che entra nel loro raggio di aggressione (700, 700 e 900 unità) e non riparano mai il loro scafo; lo scudo di ogni alieno si ricarica a partire da 15 secondi dopo l’ultimo colpo che ha subito.

---

## Contro chi combatte un alieno {#who-an-alien-fights}

Un alieno continua a combattere **il primo pilota che gli ha sparato**, finché può ancora inseguirlo: il pilota è sulla mappa, non è in una zona sicura, non è occultato né dentro la finestra dell’EMP, è vivo e l’ha colpito negli ultimi **10 secondi** (ogni colpo fa ripartire i 10 secondi: una raffica laser, un razzo o il bordo di un’esplosione allo stesso modo). Finché tutto questo vale, i colpi degli altri piloti non lo fanno mai voltare, per quanto siano vicini o per quanto spesso colpiscano, quindi un pilota può tenere impegnato un alieno mentre gli altri gli sparano.

Quando il primo pilota esce di scena (lascia la mappa, raggiunge una zona sicura, sparisce dai sensori, viene distrutto o smette di colpire l’alieno per 10 secondi), l’alieno si rivolta contro il **successivo** pilota che si è unito allo scontro, nell’ordine in cui gli hanno sparato per la prima volta, e non contro quello che l’ha colpito per ultimo. Un pilota che è uscito di scena e gli spara di nuovo entra in fondo alla fila. Un alieno tiene il conto dei primi **32** piloti che gli hanno sparato; un 33º pilota che gli spara non fa parte della fila finché uno di loro non esce di scena, e in una folla di qualsiasi dimensione l’alieno resta sul primo.

I [piloti di corporazione](/wiki/03-Mechanics/Company-Pilots.md) contano dopo ogni giocatore: un alieno combatte un pilota di corporazione solo finché nessun giocatore che può ancora inseguire gli ha sparato, un giocatore che spara a un alieno che sta combattendo un pilota di corporazione se lo prende, e un pilota di corporazione non distoglie mai un alieno da un giocatore. Niente di tutto questo cambia chi ottiene le ricompense dell’alieno: quello spetta alla rivendicazione ([Ricompense degli abbattimenti](#kill-rewards-first-hit-claims)).

---

## Gli alieni perdono interesse {#aliens-lose-interest}

Nessun alieno ti segue per tutta la mappa. Ma un alieno che stai **colpendo** non sta perdendo interesse, sta combattendo contro di te: per **10 secondi** dopo il tuo ultimo colpo (ogni colpo fa ripartire i 10 secondi, una raffica laser, un razzo o il bordo di un’esplosione allo stesso modo) ti vola contro, alla sua velocità, ogni volta che sei oltre la sua portata d’attacco (Seeker 600, Phantasm e Bulwark 700, Goombah 800, Crystalys 900), e continua ad avvicinarsi e a sparare finché non sei a portata. Non ha alcun limite alla distanza che percorre per seguirti finché continui a colpirlo. Un laser che arriva più lontano dell’arma dell’alieno (una Starfire-III arriva a 850 unità, un Helios Beam a 900) non ti permette di colpirlo da dove non può rispondere, e una nave più veloce lo tiene dietro di te solo finché continui a sparare. Ti lascia comunque subito se raggiungi una zona sicura, ti occulti o lasci la mappa.

Quando più piloti colpiscono lo stesso alieno, esso resta sul primo che gli ha sparato (vedi [Contro chi combatte un alieno](#who-an-alien-fights)): si avvicina a quel pilota e spara, così un gruppo fermo intorno a lui appena fuori dalla sua portata non può tenerlo in corsa dall’uno all’altro senza che mai risponda.

Un alieno che ti ha scelto come bersaglio (un Phantasm, un Bulwark o un Crystalys a cui ti sei avvicinato, o qualsiasi alieno a cui hai sparato) e che non colpisci da 10 secondi lascia perdere non appena una di queste condizioni è vera:

- **Non gli hai mai sparato:** sei a più di **1.200 unità** da lui, oppure lui ha percorso **2.000 unità** dal punto in cui l’inseguimento è iniziato.
- **Gli hai sparato nell’ultimo minuto:** sei a più di **2.500 unità** da lui, oppure lui ha percorso **3.000 unità** dal punto in cui l’inseguimento è iniziato. Uno scontro che hai iniziato tu resta leale.

Un alieno che lascia perdere vaga da dove si trova, mai verso il punto in cui ti ha visto per l’ultima volta (nemmeno quando ti occulti o lanci l’EMP), e non ti sceglie di nuovo come bersaglio per **8 secondi**, a meno che tu non gli spari. Ogni alieno decide per conto suo, quindi un branco misto si dirada man mano che voli via. Gli alieni non ti seguono mai in una zona sicura né attraverso un portale, e quelli che ti hanno perso vicino a uno si allontanano da esso, ciascuno per la sua strada, così non aspettano ammassati. L’interesse di un alieno non si spegne mai a una distanza inferiore alla sua portata d’attacco e al suo raggio di aggressione, più 100 unità.

Gli alieni non si spingono a vicenda: un branco dietro un pilota si avvicina senza lasciare spazio tra le sue navi, e un branco che ha perso il suo pilota si sparpaglia solo quando ogni alieno sceglie la propria strada. Un alieno però si tiene lontano da una **nave**: non finisce mai dentro lo scafo di un pilota, e un pilota che si ferma su uno lo spinge via.

Volare più veloci aiuta solo fino a un certo punto: una Protos (160) non è più veloce di nessun alieno che dà la caccia (Phantasm 160, Bulwark 175, Crystalys 230), quindi a far finire l’inseguimento è il limite di distanza, non la tua velocità.

---

## Subire danni e zone sicure {#taking-damage-safe-zones}

Quando la tua nave viene colpita da un nemico o da un NPC, il danno viene elaborato così:

### 1. Assorbimento dello scudo {#1-shield-absorption}

Il danno in arrivo viene diviso tra scudi e punti scafo in base all’**assorbimento medio** della tua nave: la media dell’assorbimento dei tuoi scudi, ciascuno con quello delle sue celle scudo, più lo Shield Absorbance Boost dell’Emporio (vedi [Meccaniche degli scudi](/wiki/03-Mechanics/Shields.md)). **Non ha un tetto del 100%**: ciò che gli scudi prendono di un colpo è il tuo assorbimento **meno la penetrazione dello scudo dell’attaccante**, tra 0% e 100%.
- L’**assorbimento** (ad es. 80% per il miglior scudo con le migliori celle, 56% per un Basic Shield Core con due Absorption Shield Cell I) di ogni colpo viene preso dagli scudi, meno la penetrazione del colpo: il 35% di un Lancet III lascia il 45% agli scudi di una nave all’80%, e il resto (il 55% in questo caso) colpisce direttamente i punti scafo.
- La **penetrazione dello scudo** viene dai razzi diretti (dal 10 al 35%) e dalle munizioni laser x3 e x4 (5% e 10%); gli alieni non ne hanno. Una nave oltre il 100% (il 112%, per esempio) regge un colpo intero contro una penetrazione fino alla differenza (qui il 12%). I Penetration Amp dei laser di chi spara (da +2% a +8% per slot) e una formazione di droni si sommano, e niente limita il totale.
- Uno scudo troppo basso per la sua quota passa la differenza ai punti scafo; se gli scudi sono completamente esauriti, il **100%** di tutto il danno restante colpisce i punti scafo.
- Gli alieni non hanno una statistica di assorbimento: i loro scudi prendono l’80% di ogni colpo (meno la penetrazione del colpo), il loro scafo il resto.
- **Formazioni di droni.** Rampart aumenta il tuo assorbimento del 17% (Shrike lo riduce del 6%), e Asterism dà a ogni colpo diretto contro di te il 7% di probabilità di non fare alcun danno (compare un “Mancato” fluttuante), e i colpi che arrivano si dividono tra scudo e scafo come al solito. Gemini (+9 punti) e Stiletto (+16) aggiungono penetrazione alle tue munizioni e ai razzi diretti, senza tetto ([Formazioni di droni](/wiki/03-Mechanics/Formations.md)). Per un laser contano anche i suoi amp.

### 2. Immunità della zona sicura {#2-safe-zone-immunity}

La base di ogni fazione (le mappe X-1) contiene zone sicure.
- Entrare in una zona sicura rende la tua nave completamente immune ai danni.
- **Rottura dell’immunità**: attaccare un nemico ti toglie subito l’immunità della zona sicura, anche se ti trovi fisicamente dentro una di esse.
- Un anello intorno a ogni stazione e portale ti protegge una volta passati 5 secondi da quando sei stato colpito e 15 da quando hai sparato. Finché ti protegge e sei fuori dal combattimento, la finestra Hangar ti permette di cambiare nave senza uscire dal gioco: vedi [L’Hangar in volo](/wiki/03-Mechanics/Hangar.md).
- Le stazioni si trovano solo nelle basi (`x-1`). I settori pericolosi (da `DS-1` a `DS-4`) non ne hanno: lì gli anelli intorno ai portali sono le uniche zone sicure.

### 3. Sotto attacco in un settore pericoloso {#3-under-attack-in-a-danger-sector}

Un salto attraverso un portale dura 3 secondi (vedi [Viaggiare sulla mappa spaziale](/wiki/01-General/Spacemap%20Travel.md)). Nei settori pericolosi (da `DS-1` a `DS-4`) un pilota la cui nave è stata colpita da un altro pilota o da un alieno negli ultimi **10 secondi** non può avviarne uno, e un colpo annulla un salto in corso. Ovunque altrove gli attacchi non interrompono mai un salto, e nulla interrompe la raccolta di una cassa di [carico](/wiki/03-Mechanics/Cargo.md).

---

## Recupero e riparazione {#recovery-repair}

Per riprendersi dal combattimento, i piloti possono contare sulla rigenerazione passiva e su robot di utilità attivi:

### 1. Rigenerazione passiva dello scudo {#1-shield-passive-regeneration}

- **Funzionamento**: ripristina ogni secondo punti scudo pari alla velocità di ricarica del tuo scudo.
- **Ritardo**: interrotta dal combattimento; la rigenerazione passiva riprende solo dopo **15 secondi** senza subire danni.
- **Formazioni di droni**: Adamant e Redoubt restituiscono scudo ogni secondo, anche in combattimento (vedi [Formazioni di droni](/wiki/03-Mechanics/Formations.md)).

### 1b. Siphon Battery

Le munizioni [Siphon Battery](/wiki/06-Items/Lasers.md) aggiungono subito al tuo scudo quello che drenano da un bersaglio, fino al tuo massimo. Guadagnare scudo non è danno subito, quindi non ritarda la tua rigenerazione passiva.

### 2. Repair Drone (riparazione dello scafo) {#2-repair-drones-hull-repair-}

- **Funzionamento**: se equipaggi un Repair Drone (negli Extra dell’Hangar), lo attivi dalla barra rapida (trascinalo dal selettore Extra su uno slot) e ripara il tuo scafo. Qualsiasi colpo lo disattiva, e si ferma a scafo pieno. Con una [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) montata non devi riattivarlo: la CPU lo lancia da sola appena è passato il ritardo indicato più sotto, a meno che tu non l’abbia fermato a mano.
- **Velocità di riparazione**: ripristina ogni secondo una percentuale dei tuoi punti scafo massimi (conta solo il miglior drone montato, non si sommano):
  - **Repair Drone I**: 1,5% dei punti scafo massimi / s
  - **Repair Drone II**: 2,25% dei punti scafo massimi / s
  - **Repair Drone III**: 3,5% dei punti scafo massimi / s
  - **Repair Drone IV**: 5% dei punti scafo massimi / s
- **Ritardo**: i Repair Drone iniziano a riparare lo scafo solo dopo **10 secondi** senza subire danni.
- **In uno slot abilità** un Repair Drone non ripara da solo: ti dà **Emergency Repair**, un pulsante che cura una quota dei tuoi punti scafo massimi nell’arco di dieci secondi, anche sotto il fuoco (vedi [Abilità](/wiki/03-Mechanics/Abilities.md)).

---

## Occultamento ed EMP {#cloaking-and-the-emp}

Un colpo ha bisogno di un aggancio. Due [extra](/wiki/06-Items/Extras.md) eliminano quello su di te:

- **Cloaking CPU**: finché sei occultato (non c’è limite di tempo) i piloti delle altre corporazioni, gli alieni e i piloti di corporazione non vedono la tua nave e non possono agganciarla; vedono un semplice punto rosso sulla minimappa dove ti trovi. La tua prima raffica pone fine all’occultamento, e non puoi occultarti di nuovo per un minuto, né entro 10 secondi da un colpo subito o sparato.
- **EMP Charge**: per 3 secondi nessuno può agganciarti, e ogni aggancio già su di te si spezza subito. Pone fine a ogni occultamento entro 1.500 unità dal pilota che lo lancia, tranne quelli dei membri del suo stesso gruppo. Non ti nasconde, e non è invulnerabilità: ferma ciò che ha bisogno di un aggancio.

Anche un razzo è un colpo: pone fine al tuo occultamento, e l’esplosione ad area del razzo di qualcun altro colpisce comunque una nave occultata e ne pone fine all’occultamento, perché un’esplosione non ha bisogno di un aggancio (vedi [Razzi](/wiki/06-Items/Rockets.md)). L’EMP ferma i laser agganciati e i razzi guidati, non un’esplosione.

Nessuno dei due cambia una rivendicazione: una rivendicazione è la storia di chi ha colpito un alieno, non un aggancio, e l’occultamento rilascia la tua.
