<!-- wiki-i18n source: 2614a979fa3ece0b -->
<!-- wiki-i18n title: Inventario -->
# Inventario ed equipaggiamento {#inventory-equipment}

L’Hangar ti permette di gestire le tue navi e il tuo equipaggiamento. Equipaggiare bene gli oggetti è la chiave per sopravvivere e dominare. Puoi farlo alla stazione, e in volo da dentro una zona sicura: vedi [L’Hangar in volo](/wiki/03-Mechanics/Hangar.md).

![The Hangar's inventory: the category chips are one glyph each (the name is the tooltip) with the count of what you hold](../../img/wiki-img/shots/inventory-chips.jpg)
![Dragging a rectangle over the empty space of the inventory: every tile it touches is selected and the title row counts them](../../img/wiki-img/shots/inventory-marquee.jpg)

## Slot dell’equipaggiamento ed efficienza delle statistiche {#equipment-slots-stat-efficiencies}

A differenza dei giochi spaziali tradizionali, SpaceCorps ha slot di equipaggiamento a livelli dinamici che scalano l’efficacia dei moduli montati.

- **Slot laser**: per le armi offensive (laser). Funzionano sempre al **100% di danno e portata**.
- **Slot generatore**: slot condivisi per scudi, motori e Nuclei adattivi. Sono divisi in tre fasce di efficienza, e la fascia decide quanta parte delle statistiche di base di un oggetto conta. Nell’Hangar ogni fascia ha una (i) accanto al nome che la spiega:
  - **Slot principali**: gli oggetti messi qui ricevono il **100%** delle loro statistiche di base. Ogni nave li ha: metti qui i tuoi scudi e motori più forti.
  - **Slot di supporto**: gli oggetti messi qui ricevono il **75%** delle loro statistiche di base (per esempio il 75% della velocità o della capacità dello scudo). Ogni nave li ha.
  - **Slot ausiliari**: gli oggetti messi qui ricevono il **50%** delle loro statistiche di base. Solo alcune navi li hanno (la Nomad ne ha 1, la Paragon e la Storm 2, l’Ironclad 3 e la Wraith 4; la Protos, la Kitefin e l’Ostirion non ne hanno). Sono ideali per scudi e motori extra più deboli, mentre i più forti vanno negli slot principali.
  - **Slot dei droni**: uno scudo su uno dei tuoi droni conta come uno in uno slot principale, il **100%** delle sue statistiche (vedi [Meccaniche dei droni](/wiki/03-Mechanics/Drones.md)).
  - **Slot non assegnati/obsoleti**: gli oggetti messi qui non contribuiscono alle statistiche.
  - **Anche il cumulo si attenua**: scudi e motori vengono ordinati dal più forte (in base a ciò che ciascuno conta dopo la quota del suo slot), e la quota della fascia viene poi moltiplicata per la quota del loro posto: dal 1º al 4º contano per intero, dal 5º al 7º l’85%, il 70% e il 55%, dall’8º in poi il 50% per gli scudi e il 25% per i motori. Vedi [Scudi](/wiki/03-Mechanics/Shields.md) e [Velocità](/wiki/03-Mechanics/Speed.md).
- **Slot extra**: per oggetti di utilità specializzati, come i Repair Drone. La Protos, la Kitefin, l’Ostirion e la Nomad ne hanno due; la Paragon, la Ironclad, la Wraith e la Storm, che costruisci, ne hanno tre. Le Extra Slots CPU ([Extra](/wiki/06-Items/Extras.md#extra-slots-cpus)) ne aggiungono 3, 5 o 7.
- **Slot corazza**: per la [corazza dello scafo](/wiki/06-Items/Hull-Plating.md#hull-plate-slots), che aggiunge scafo. Li hanno solo le quattro navi che costruisci (la Paragon 5, la Storm 7, la Ironclad 15 e la Wraith 9), ciascuno bloccato finché non lo ricerchi nello Skylab, e sono uguali nelle due configurazioni.

## Ordine dell’inventario {#inventory-order}

L’inventario elenca i tuoi oggetti nello stesso ordine del Negozio, qualunque sia l’ordine in cui li hai acquistati, creati o trovati. I tipi che stanno insieme sono vicini: laser, amp laser e munizioni laser; scudi e celle scudo; motori e propulsori; Nuclei adattivi; extra (Repair Drone); droni e formazioni di droni; poi le risorse. All’interno di un tipo viene per primo il più economico (crediti prima del Thulium), poi ciò che non ha prezzo: equipaggiamento solo da creare e bottino, a partire dalla rarità più bassa (i laser della stessa rarità, dal danno più basso). Le munizioni laser vanno da x1 a x4, poi la Siphon Battery. I razzi vanno per tipo (a bersaglio singolo prima di quelli ad area, guidati prima di quelli dritti) e poi per grado, quindi il razzo Epico, che costa Thulium, viene per ultimo nel suo tipo. Le copie di uno stesso oggetto vanno per grado di incantamento. Sopra la griglia, un chip per ogni tipo segue lo stesso ordine, ciascuno con il numero di oggetti che la ricerca vi trova. Ogni chip si attiva o disattiva da solo, così puoi nascondere munizioni e Repair Drone mentre lavori su laser, scudi e motori: clicca su un chip per mostrare o nascondere il suo tipo, Shift+clic (o doppio clic) per lasciare attivo solo quel tipo, e cliccalo di nuovo per riportare gli altri. **Tutte** mostra ogni tipo e **Nessuna** li nasconde tutti, per attivare solo quelli che vuoi. Un chip barrato è disattivato, un chip con un segno di spunta è attivo. La ricerca agisce sui tipi attivi, e la tua scelta viene ricordata con il tuo pilota. Se tutto è nascosto, la griglia lo dice e propone **Mostra tutte le categorie**.

## Oggetti vendibili {#marketable-items}

Gli oggetti che hai guadagnato (bottino, ricompense delle missioni e ciò che fanno l’Assemblaggio e la Forgia) portano un piccolo contrassegno **Vendibile** sulla casella, e la scheda dell’oggetto dice «Vendibile» oppure, per una pila di cui si può vendere solo una parte, «Vendibile (3 / 5)». Il filtro **Solo vendibile** accanto ai filtri di categoria mostra solo questi oggetti. Un **martelletto** accanto al cestino di un oggetto contrassegnato apre la scheda di vendita dell’[Asta](/wiki/03-Mechanics/Auction.md) (in volo non compare: vendere è una pagina della stazione). Ciò che hai comprato, vinto o ricevuto in regalo non ha contrassegno e non si può rivendere, e lo stesso vale per tutto ciò che dà un [contenitore](/wiki/06-Items/Containers.md).

## Selezionare più oggetti {#select-several-items}

Premi su una parte vuota dell’inventario (il margine accanto alle caselle, lo spazio tra due caselle o quello sotto l’ultima riga) e trascina: un rettangolo traslucido segue il puntatore, e ogni casella che tocca è selezionata finché trascini. Rilascia e la selezione resta; la riga del titolo la conta («3 selezionati»). Tieni premuto **Maiusc**, **Ctrl** o **Cmd** mentre trascini per aggiungere alla selezione: le caselle già selezionate che il rettangolo tocca vengono invece rilasciate. Un trascinamento normale inizia una nuova selezione. **Esc**, un clic su uno spazio vuoto o il pulsante accanto al cestino nella riga del titolo la annulla; **Esc** a metà trascinamento annulla il trascinamento. Al bordo alto o basso di un inventario lungo l’elenco scorre da solo. Una pressione su una casella resta della casella: clic per equipaggiare, trascinamento su uno slot. Il cestino nella riga del titolo elimina gli oggetti selezionati dopo una domanda che li elenca (una pila di Extra identici se ne va intera); non è offerto finché l’Hangar in volo è bloccato. Un oggetto montato nello Skylab non si può selezionare, e si può selezionare solo ciò che la ricerca e i filtri di categoria lasciano nella griglia. Si sente un lieve tic quando il rettangolo prende una casella in più (segue l’interruttore «Suoni dei pulsanti» delle impostazioni).

**Equipaggiare tutta la selezione.** Trascina una delle caselle selezionate e tutta la selezione viene con lei, come una pila di caselle con un numero davanti al puntatore (una casella non selezionata si trascina da sola, e un clic su una casella selezionata equipaggia sempre solo quell’oggetto). Se rilasci su uno slot o su una scheda, l’oggetto sotto il puntatore va lì se ci sta, e ogni altro oggetto nel suo slot migliore; se rilasci sulle parti vuote della nave, ogni oggetto va nel suo slot migliore; altrove non succede niente, ed **Esc** lascia andare il trascinamento. Il pulsante con la freccia accanto al cestino nella riga del titolo (il suo suggerimento dice che equipaggia gli oggetti selezionati nei loro slot migliori) fa lo stesso senza trascinare; non è offerto nella vista P.E.T. né finché l’Hangar in volo è bloccato. Lo slot migliore è quello in cui un clic metterebbe l’oggetto, calcolato un oggetto dopo l’altro: prima i laser, i più forti per primi, poi scudi, motori e Nuclei adattivi, gli extra, i Repair Drone (in uno slot abilità libero quando gli extra sono pieni), le corazze dello scafo e infine gli amp, le celle e i propulsori, che hanno bisogno che i loro laser, scudi e motori siano già montati. Ciò che non si è potuto sistemare resta selezionato, e un messaggio dice quanti sono andati («Equipaggiati 7 su 9.») e perché gli altri no. Per tutto il rilascio si sente un solo suono lieve.

## Equipaggiare un oggetto in un altro (sotto-slot) {#item-to-item-equipping-sub-sockets-}

Alcuni oggetti primari possono “equipaggiare” oggetti di supporto secondari (il cosiddetto montaggio in sotto-slot) per amplificare i loro parametri. Per montare in un sotto-slot, trascina l’oggetto di supporto direttamente sull’oggetto primario nell’inventario dell’Hangar.

### Tabella di compatibilità {#compatibility-table}

| Oggetto primario | Oggetti accettati nei sotto-slot | Effetto risultante |
| :--- | :--- | :--- |
| **Laser** | Amplificatore laser (Amp) | Aumenta il danno base e le statistiche dei colpi critici, oppure toglie punti all’assorbimento del bersaglio (Penetration Amp) |
| **Shield Core** | Cella scudo | Aumenta la capacità dello scudo e la velocità di ricarica |
| **Motore** | Propulsore | Aumenta la velocità del motore e i moltiplicatori |
| **Generatore ibrido** | Cella scudo OPPURE propulsore | Aumenta la capacità dello scudo, la velocità di ricarica o la velocità |
| **Drone** | Laser o scudo, in ciascuno dei suoi slot (un Master Drone ne ha due) | Un laser aggiunge il suo danno alla tua raffica; uno scudo conta come uno in uno slot principale (il 100% delle sue statistiche) |

---

## Gestione delle munizioni {#ammo-management}

Le munizioni laser sono una risorsa consumabile.
- Le munizioni si accumulano in pile nell’inventario.
- Puoi cambiare le munizioni laser attive dalla barra rapida dell’HUD.
- Le munizioni di qualità superiore offrono moltiplicatori di danno (per esempio standard x1, advanced plasma x2, ultra core x3, experimental fusion core x4). La Siphon Battery infligge danno x1 solo agli scudi e lo cede ai tuoi.
