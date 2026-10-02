<!-- wiki-i18n source: ac17fd77713a030e -->
<!-- wiki-i18n title: Inventario -->
# Inventario ed equipaggiamento {#inventory-equipment}

L’Hangar ti permette di gestire le tue navi e il tuo equipaggiamento. Equipaggiare bene gli oggetti è la chiave per sopravvivere e dominare. Puoi farlo alla stazione, e in volo da dentro una zona sicura: vedi [L’Hangar in volo](/wiki/03-Mechanics/Hangar.md).

## Slot dell’equipaggiamento ed efficienza delle statistiche {#equipment-slots-stat-efficiencies}

A differenza dei giochi spaziali tradizionali, SpaceCorps ha slot di equipaggiamento a livelli dinamici che scalano l’efficacia dei moduli montati.

- **Slot laser**: per le armi offensive (laser). Funzionano sempre al **100% di danno e portata**.
- **Slot generatore**: slot condivisi per scudi, motori e Nuclei adattivi. Sono divisi in tre fasce di efficienza, e la fascia decide quanta parte delle statistiche di base di un oggetto conta. Nell’Hangar ogni fascia ha una (i) accanto al nome che la spiega:
  - **Slot principali**: gli oggetti messi qui ricevono il **100%** delle loro statistiche di base. Ogni nave li ha: metti qui i tuoi scudi e motori più forti.
  - **Slot di supporto**: gli oggetti messi qui ricevono il **75%** delle loro statistiche di base (per esempio il 75% della velocità o della capacità dello scudo). Ogni nave li ha.
  - **Slot ausiliari**: gli oggetti messi qui ricevono il **50%** delle loro statistiche di base. Solo alcune navi li hanno (la Paragon ne ha 2, l’Ironclad 3 e la Wraith 4; la Protos, la Kitefin e l’Ostirion non ne hanno). Sono ideali per scudi e motori extra più deboli, mentre i più forti vanno negli slot principali.
  - **Slot dei droni**: uno scudo su uno dei tuoi droni conta come uno in uno slot principale, il **100%** delle sue statistiche (vedi [Meccaniche dei droni](/wiki/03-Mechanics/Drones.md)).
  - **Slot non assegnati/obsoleti**: gli oggetti messi qui non contribuiscono alle statistiche.
  - **Anche il cumulo si attenua**: scudi e motori vengono ordinati dal più forte, e la quota della fascia viene poi moltiplicata per la quota del loro posto: dal 1º al 4º contano per intero, dal 5º al 7º l’85%, il 70% e il 55%, dall’8º in poi il 25%. Vedi [Scudi](/wiki/03-Mechanics/Shields.md) e [Velocità](/wiki/03-Mechanics/Speed.md).
- **Slot extra**: per oggetti di utilità specializzati, come i Repair Drone.

## Ordine dell’inventario {#inventory-order}

L’inventario elenca i tuoi oggetti nello stesso ordine del Negozio, qualunque sia l’ordine in cui li hai acquistati, creati o trovati. I tipi che stanno insieme sono vicini: laser, amp laser e munizioni laser; scudi e celle scudo; motori e propulsori; Nuclei adattivi; extra (Repair Drone); droni; poi le risorse. All’interno di un tipo viene per primo il più economico (crediti prima del Thulium), poi ciò che non ha prezzo: equipaggiamento solo da creare e bottino, a partire dalla rarità più bassa (i laser della stessa rarità, dal danno più basso). Le munizioni laser vanno da x1 a x4, poi la Siphon Battery. I razzi vanno per tipo (a bersaglio singolo prima di quelli ad area, guidati prima di quelli dritti) e poi per grado, quindi il razzo Epico, che costa Thulium, viene per ultimo nel suo tipo. Le copie di uno stesso oggetto vanno per grado di incantamento. Sopra la griglia, un chip per ogni tipo segue lo stesso ordine, ciascuno con il numero di oggetti che la ricerca vi trova. Ogni chip si attiva o disattiva da solo, così puoi nascondere munizioni e Repair Drone mentre lavori su laser, scudi e motori: clicca su un chip per mostrare o nascondere il suo tipo, Shift+clic (o doppio clic) per lasciare attivo solo quel tipo, e cliccalo di nuovo per riportare gli altri. **Tutte** mostra ogni tipo e **Nessuna** li nasconde tutti, per attivare solo quelli che vuoi. Un chip barrato è disattivato, un chip con un segno di spunta è attivo. La ricerca agisce sui tipi attivi, e la tua scelta viene ricordata con il tuo pilota. Se tutto è nascosto, la griglia lo dice e propone **Mostra tutte le categorie**.

## Equipaggiare un oggetto in un altro (sotto-slot) {#item-to-item-equipping-sub-sockets-}

Alcuni oggetti primari possono “equipaggiare” oggetti di supporto secondari (il cosiddetto montaggio in sotto-slot) per amplificare i loro parametri. Per montare in un sotto-slot, trascina l’oggetto di supporto direttamente sull’oggetto primario nell’inventario dell’Hangar.

### Tabella di compatibilità {#compatibility-table}

| Oggetto primario | Oggetti accettati nei sotto-slot | Effetto risultante |
| :--- | :--- | :--- |
| **Laser** | Amplificatore laser (Amp) | Aumenta il danno base e le statistiche dei colpi critici |
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
