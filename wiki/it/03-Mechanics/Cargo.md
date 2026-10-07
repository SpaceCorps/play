<!-- wiki-i18n source: e8ccf0e85479a269 -->
<!-- wiki-i18n title: Carico -->
# Casse di carico {#cargo-boxes}

Gli alieni distrutti lasciano il loro bottino nello spazio sotto forma di casse di carico luminose. Sorvolale e raccoglile prima che lo faccia qualcun altro.

![Picking up a cargo box: the channel bar fills while the ship stays near](../../img/wiki-img/shots/cargo-pickup.jpg)

## Cosa viene rilasciato {#what-drops}

- Gli **alieni** rilasciano il loro bottino in un’unica cassa nel punto in cui sono esplosi: le risorse e i pezzi elencati sotto il *Bottino* di ogni alieno (vedi gli articoli sugli [Alieni](/wiki/04-Aliens/Phantasm.md)). Crediti, Thulium, XP e onore vengono comunque pagati nel momento in cui abbatti l’alieno. Un alieno il cui bottino non produce nulla (un Seeker quattro volte su cinque) non lascia nessuna cassa.
- I **piloti di corporazione** non lasciano nessuna cassa quando vengono distrutti, chiunque o qualunque cosa li distrugga. Vedi [Piloti di corporazione](/wiki/03-Mechanics/Company-Pilots.md).
- Le **navi dei giocatori** non lasciano né relitto né cassa quando vengono distrutte, chiunque o qualunque cosa le distrugga, e al pilota non viene tolto nulla dall’inventario.
- Il **buco nero** posa casse di **Dark Matter** sul bordo della sua zona per ogni razzo N.I.K.E. lanciato al suo interno (vedi [Il buco nero](/wiki/03-Mechanics/Black-Hole.md)). Sono l’unico tipo di cassa che si trova dentro l’anello del buco nero.
- **I capi degli [sciami](/wiki/05-Swarms/Swarms.md) e le Dormant Pulse** lasciano una cassa tutta loro, con munizioni, razzi e risorse. È riservata al pilota che ha inflitto più danno alla nave (e al clan di quel pilota), non al primo che l’ha colpita.
- **Un [Clan Warden](/wiki/03-Mechanics/Clans.md#warden-pay-and-loot)** non lascia una cassa del genere: ogni pilota che ha inflitto almeno il 5% dei danni riceve una [cassa privata](#private-boxes) tutta sua, con la sua parte del bottino.
- Gli **[asteroidi](/wiki/03-Mechanics/Asteroid-Mining.md)** lasciano **frammenti** invece di una cassa: piccole pepite e cristalli che contengono crediti e Thulium, e una pietra che contiene minerale. I crediti e il Thulium vengono pagati quando si raccoglie un frammento, non quando l’asteroide si spezza, e vale un limite per ogni periodo di 24 ore. Un frammento si raccoglie come una cassa, ed è riservato ai piloti che l’hanno meritato e poi libero, come una cassa.

Un alieno finito da un pilota di corporazione rilascia il suo bottino per il pilota a cui l’abbattimento viene attribuito (chi ne detiene la rivendicazione, altrimenti il pilota della stessa corporazione che lo sta combattendo); uno combattuto da un pilota di corporazione da solo non rilascia nulla, perché i piloti di corporazione non raccolgono mai.

Le luci della cassa prendono il colore dell’oggetto più raro al suo interno: verde acqua per il bottino comune, poi verde, blu, viola, rosa, oro e rosso arancio da non comune a eterno.

## Raccolta {#collecting}

- **Clic sinistro** su una cassa: la tua nave vola verso di essa e la prende una volta a portata (200 unità). Un clic su una cassa non conta mai come ordine di movimento; qualsiasi altro ordine di movimento (un clic nello spazio, la minimappa) annulla la raccolta. Quando sotto il puntatore c’è anche una nave o un alieno, il clic va a quello più vicino al puntatore, così uno scontro che passa sopra una cassa mantiene i suoi bersagli.
- **La raccolta dura mezzo secondo.** Appena la tua nave è a portata e autorizzata a prendere la cassa, la raccolta inizia: una barra sopra la tua barra rapida (“Raccolta in corso…”) si riempie e un raggio scansiona la cassa. La tua nave continua a volare, e la cassa è tua quando la barra è piena. Esci dalla portata, o perdi la cassa a favore di un altro pilota, e la raccolta viene annullata. Essere attaccati non la interrompe, in nessun luogo.
- Fai una cosa alla volta: non puoi raccogliere mentre [salti](/wiki/01-General/Spacemap%20Travel.md), e avviare un salto fa rinunciare alla raccolta. Chiedere di nuovo una cassa che stai già raccogliendo non cambia nulla.
- Passa il puntatore su una cassa per vedere cosa contiene, per chi è riservata e, nel suo ultimo minuto, quanto tempo le resta.
- Raccogliere una cassa riproduce un breve suono di raccolta nel punto in cui si trovava; senti anche le raccolte degli altri piloti vicini, più piano.
- Ciò che raccogli va direttamente nell’inventario dell’Hangar, sulla tua pila libera di quell’oggetto (mai su un equipaggiamento né su qualcosa nel Deposito di trasporto). Una notifica ti dice cosa hai ottenuto; le casse raccolte una dopo l’altra si sommano nella stessa notifica.
- Ciò che raccogli è **vendibile**: puoi venderlo all’[Asta](/wiki/03-Mechanics/Auction.md#marketable-items).
- Quando un frammento di un [asteroide](/wiki/03-Mechanics/Asteroid-Mining.md) è tuo, la tua nave passa da sola al frammento successivo a portata che puoi prendere; qualsiasi tuo ordine di movimento la ferma.

## A chi spetta {#who-gets-it}

- Il pilota pagato per l’abbattimento, e i membri del **clan** di quel pilota, hanno la cassa tutta per sé per **30 secondi**. Per un alieno è il pilota che ne detiene la rivendicazione, il primo a colpirlo (vedi [Combattimento](/wiki/03-Mechanics/Combat.md)), chiunque l’abbia finito. Gli altri piloti la vedono attenuata e non possono ancora prenderla; una nave mandata verso di essa attende nelle vicinanze finché il tempo non scade.
- Dopo, **chiunque** sulla mappa può prenderla.
- Solo una nave presente sulla mappa della cassa può prenderla: se vieni distrutto, salti o ti disconnetti lungo la strada (o durante il mezzo secondo che la raccolta richiede), la cassa resta agli altri.
- Se due piloti raccolgono la stessa cassa contemporaneamente, la ottiene quello la cui raccolta finisce per prima, una sola volta; all’altro viene detto che non c’è più.
- Una cassa che nessuno prende va alla deriva dopo **3 minuti** (lampeggia negli ultimi 10 secondi). Una mappa contiene al massimo 64 casse; quando una nuova supererebbe il limite, la più vecchia sparisce. I frammenti di asteroide hanno un gruppo tutto loro all’interno delle 64: non scacciano nessun’altra cassa, e nessun’altra cassa scaccia un frammento ([le regole](/wiki/03-Mechanics/Asteroid-Mining.md#the-rules)). Le casse di Dark Matter durano 4 minuti, e sono solo tue per il primo minuto.

## Casse private {#private-boxes}

Il bottino di un [Clan Warden](/wiki/03-Mechanics/Clans.md#warden-pay-and-loot) non è una cassa per un solo pilota: **ogni pilota che ha inflitto almeno il 5% dei danni riceve una cassa tutta sua**, estratta per la sua parte (per il 20% dei danni, circa un quinto di ogni quantità; [i dettagli](/wiki/03-Mechanics/Clans.md#warden-pay-and-loot)).

- **Solo tu la vedi e solo tu puoi raccoglierla.** Il tuo clan e il tuo gruppo non la vedono e non possono prenderla; per tutti gli altri semplicemente non c’è. Sul tuo schermo ha un anello sottile sotto.
- **Resta lì 10 minuti** dall’abbattimento, e per tutto il tempo è tua: non c’è l’attesa di 30 secondi. Poi se ne va alla deriva come ogni cassa. Il Registro di gioco ti dice la tua parte del bottino quando il Custode cade.
- **Non scaccia altre casse.** Le casse private hanno una riserva a sé accanto alle 64 di una mappa (al massimo 32), così l’abbattimento di un Custode non prende mai il posto di un’altra cassa e una mappa piena non ti fa mai perdere la tua.
- La raccolta è la stessa di ogni cassa ([sopra](#collecting)): la tua nave vola fino a lei e la raccolta dura mezzo secondo.

## Booster {#boosters}

- **Loot Luck Booster** (e il potenziamento permanente Fortuna) aumentano la probabilità di ogni voce del bottino quando chi abbatte l’alieno mette a segno l’abbattimento.
- **Resource Magnet Booster** aggiunge il **25%** alle risorse di ogni cassa che raccogli, chiunque abbia fatto l’abbattimento. La Dark Matter è l’eccezione: il Magnet non le aggiunge nulla, quindi cinque N.I.K.E. sono dieci Dark Matter per tutti.
