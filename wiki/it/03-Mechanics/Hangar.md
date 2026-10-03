<!-- wiki-i18n source: d888495e0809faa2 -->
<!-- wiki-i18n title: Hangar -->
# L’Hangar in volo {#the-hangar-in-flight}

Non devi tornare alla base per cambiare la tua nave. Da dentro una zona sicura puoi aprire la finestra **Hangar** (il pulsante del magazzino nella barra degli strumenti in alto a sinistra) e cambiare ciò che è montato, passare all’altra configurazione o volare con un’altra nave che possiedi, senza uscire dal gioco. La finestra è la pagina Hangar della stazione, con gli stessi slot, le stesse statistiche e lo stesso inventario, in una finestra sopra il gioco. Vedi [Inventario ed equipaggiamento](/wiki/03-Mechanics/Inventory.md) per come si montano gli oggetti.

## Quando è aperto {#when-it-is-open}

Una modifica è consentita solo finché sono vere tutte queste condizioni:

- **Una zona sicura ti protegge.** Ogni stazione e ogni portale ha un anello protettivo (vedi [Combattimento](/wiki/03-Mechanics/Combat.md)). Al suo interno la protezione scatta quando sono passati 5 secondi dall’ultimo colpo che hai subito e 15 dall’ultimo sparo.
- **Sei fuori dal combattimento** da qualche secondo in più: **10** per impostazione predefinita. Conta quando arrivi già sotto protezione, attraverso un portale, con uno scontro alle spalle.
- Non hai l’occultamento attivo, non sei dentro la finestra del tuo EMP né vicino al [buco nero](/wiki/03-Mechanics/Black-Hole.md), e non hai ancora in aria nessun tuo razzo.

Le riparazioni in corso non ti fermano. In qualsiasi altro posto la finestra Hangar si apre comunque, ma è in sola lettura. Un banner ambra ne spiega il motivo, e conta alla rovescia i secondi quando si tratta di un’attesa (“Hai combattuto un attimo fa. Attendi 6 s per cambiare la tua nave.”). Lo fa rispettare anche il server, quindi nulla può cambiare una nave sul campo.

## Cosa puoi cambiare {#what-you-can-change}

- **Equipaggia e rimuovi qualsiasi cosa**, in ogni tipo di slot: laser, generatori (scudi, motori, Nuclei adattivi), extra, slot abilità e slot drone, e gli amp, le celle e i propulsori montati al loro interno. Trascina gli oggetti sugli slot, o cliccaci sopra, esattamente come alla stazione. La tua nave si adegua subito: statistiche, laser, abilità e barra rapida.
- **Entrambe le configurazioni.** Puoi preparare la Config 2 mentre voli con la Config 1, poi passare all’altra con il tasto Cambia conf.; un pulsante **Usa config** nell’Hangar fa lo stesso cambio.
- **Qualsiasi nave.** Imposta attiva un’altra nave e voli con essa da dove ti trovi. Il modello della tua nave cambia davanti a tutti quelli nelle vicinanze.
- **Un nuovo scudo, motore o Nucleo adattivo parte vuoto**, come alla stazione: la carica di scudo della sua configurazione è vuota finché non si ricarica.

## Cambiare nave {#changing-ship}

La nave a cui passi ha **lo scafo e gli scudi che aveva** l’ultima volta che l’hai pilotata, esattamente come se l’avessi fatta decollare. L’anello non ripara, quindi cambiare nave non ti cura mai: la nave che lasci conserva i danni che ha, e torna con essi. Una nave distrutta non può volare finché non la ripristini; è gratis e la riporta con al massimo 10.000 di scafo e senza scudo, come un respawn.

Ciò che è tuo resta tuo: le tue munizioni, i tuoi razzi e il loro timer, le ricariche delle tue abilità, i tuoi booster, i tuoi XP e i tuoi Slave Drone. Ciò che apparteneva alla nave finisce: uno Shield Surge o un Afterburner in corso, le riparazioni, il tuo aggancio del bersaglio, il tuo attacco e la rotta che stavi seguendo. Gli equipaggiamenti restano sulla nave su cui sono montati.

## Richieste da altri strumenti {#requests-from-other-tools}

Anche sul server l’Hangar cambia solo da una zona sicura: montare, smontare, eliminare un oggetto, ripristinare una nave o impostare la nave attiva mentre voli risponde “Puoi cambiare la tua nave solo in una zona sicura.” Il cambio di configurazione è l’eccezione, e funziona ovunque (una volta ogni 5 secondi).
