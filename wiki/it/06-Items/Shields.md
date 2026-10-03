<!-- wiki-i18n source: e87936a3f4fc8e12 -->
<!-- wiki-i18n title: Scudi -->
# Scudi e difesa {#shields-defense}

I moduli difensivi forniscono capacità scudo, assorbono il danno e ricaricano le tue difese.

## Shield Core {#shield-cores}

Equipaggia gli Shield Core per generare barriere difensive attive, negli slot dei generatori della tua nave o sui tuoi [droni](/wiki/03-Mechanics/Drones.md) (lo slot di un drone conta come slot principale). Nota che gli scudi pesanti riducono la tua velocità. Uno Shield Core in uno **slot abilità** ti dà invece lo **Shield Surge** indicato nella colonna Effetto speciale, un ripristino dello scudo in dieci secondi, e non aggiunge scudo proprio (vedi [Abilità](/wiki/03-Mechanics/Abilities.md)).

| Nome | Rarità | Capacità | Vel. ricarica | Assorbimento | Scudo % | Velocità % | Slot celle | Effetto speciale | Costo |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Light Shield Core** | Scadente | 10.000 | 333/s | 45% | +5% | -1% | 1 | Shield Surge I | 20.000 crediti |
| **Basic Shield Core** | Comune | 15.000 | 500/s | 48% | +10% | -3% | 2 | Shield Surge II | 2.000 Thulium |
| **Heavy Shield Core** | Raro | 25.000 | 833/s | 50% | +20% | -5% | 3 | Shield Surge III | Solo da creare |

L’**Heavy Shield Core** si crea in [Assemblaggio](/wiki/06-Items/Overview.md#upgrading-modules) da un Basic Shield Core, con 2.000 Thulium, 20 Cataclysite, 8 Reinforced Hull Plate e 6 Velkonite Reinforced Plate dal tuo Skylab. Mantiene il grado di incantamento del nucleo che consuma, e i suoi bonus vengono generati di nuovo ([Potenziamenti dei moduli](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Togli prima il Basic Shield Core dalla tua nave (e togli da esso le sue celle): uno Shield Core montato sulla nave o che contiene celle non viene consumato.

L’**assorbimento** è la quota di ogni colpo che i tuoi scudi prendono; il resto lo prende lo scafo. Uno scudo da solo ha **dal 45 al 50%** e le sue celle aggiungono il resto: il miglior scudo con le migliori celle (un Heavy Shield Core con tre Absorption Shield Cell IV) arriva all’**80%**, il massimo che una nave ha di serie. A questo si aggiungono due potenziamenti permanenti: lo Shield Absorbance Boost dell’Emporio (+0,1 punti a livello, 100 livelli, 25 punti reset ciascuno) e i bonus di assorbimento della Forgia. Le fonti attuali di punti reset (855 in totale al loro massimo, portati da un reset all’altro; altre fonti sono previste) comprano 34 di quei 100 livelli (+3,4 punti), il che con un set Eterno completamente forgiato fa circa il **95%**. La statistica però non ha un tetto al 100%: la *penetrazione dello scudo* di un attaccante viene tolta da essa, quindi ciò che una nave ha oltre il 100% è il suo margine contro la penetrazione. Vedi [Meccaniche degli scudi](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-).

---

## Generatori ibridi (Nuclei adattivi) {#hybrid-generators-adaptive-cores-}

I Nuclei adattivi fanno da generatori ibridi, combinando capacità di scudo e di velocità. Accettano nei loro slot sia propulsori sia celle scudo (un modulo per slot, dell’uno o dell’altro tipo). Il loro Bonus scudo e il loro Bonus velocità contano come quelli di uno scudo o di un motore (i quattro migliori, per la quota dello slot). Non hanno assorbimento: non cambiano l’assorbimento della tua nave, e le celle al loro interno aggiungono solo capacità e ricarica. Solo gli scudi prendono una quota di un colpo, quindi le celle in un Nucleo adattivo richiedono anche uno scudo sulla nave.

| Nome | Rarità | Bonus scudo % | Bonus velocità % | Slot | Effetto speciale | Costo |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **Adaptive Core I** | Scadente | +5% | +3% | 1 | — | 100.000 crediti |
| **Adaptive Core II** | Comune | +8% | +4% | 2 | — | 4.000 Thulium |
| **Adaptive Core III** | Raro | +15% | +5% | 3 | — | Solo da creare |

---

## Celle scudo {#shield-cells}

Le celle scudo si montano dentro gli Shield Core o i Nuclei adattivi (tante quanti sono gli slot del nucleo) per potenziarli. In uno Shield Core aumentano anche il suo assorbimento, in punti, e con esso la quota di ogni colpo che i tuoi scudi prendono. Ci sono due famiglie di quattro tier ciascuna: le **Capacity Shield Cell** danno più scudo e ricarica, le **Absorption Shield Cell** più assorbimento (a ogni tier il doppio dell’assorbimento e la metà di scudo e ricarica della Capacity dello stesso tier). La Capacity aiuta una nave in cui è lo scudo a decidere lo scontro, l’Absorption una nave in cui è lo scafo. Un nucleo con tutti gli slot pieni di una sola cella: un Light Shield Core (1 slot) fa dal 47 al 55%, un Basic Shield Core (2 slot) dal 52 al 68% e un Heavy Shield Core (3 slot) dal 56 all’80%, dalle celle Capacity di tier I a quelle Absorption di tier IV. Rimuovere il nucleo, o consumarlo come donatore di un’unione della [Forgia](/wiki/06-Items/Forge.md), restituisce le sue celle all’inventario.

| Nome | Rarità | Bonus capacità | Bonus ricarica | Bonus assorbimento | Costo |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Capacity Shield Cell I** | Scadente | +3.000 | +250/s | +2% | 30.000 crediti |
| **Capacity Shield Cell II** | Comune | +6.000 | +500/s | +3% | Solo da creare |
| **Capacity Shield Cell III** | Raro | +9.000 | +750/s | +4% | Solo da creare |
| **Capacity Shield Cell IV** | Epico | +12.000 | +1.000/s | +5% | Solo da creare |
| **Absorption Shield Cell I** | Scadente | +1.500 | +125/s | +4% | 30.000 crediti |
| **Absorption Shield Cell II** | Comune | +3.000 | +250/s | +6% | Solo da creare |
| **Absorption Shield Cell III** | Raro | +4.500 | +375/s | +8% | Solo da creare |
| **Absorption Shield Cell IV** | Epico | +6.000 | +500/s | +10% | Solo da creare |

Il tier I di ogni famiglia si compra a 30.000 crediti. I tier da II a IV si creano in [Assemblaggio](/wiki/06-Items/Overview.md#upgrading-modules), ciascuno dalla cella della stessa famiglia un tier più in basso (una Capacity Shield Cell II da una Capacity Shield Cell I, una III da una II, una IV da una III), con Thulium, drop e Velkonite Reinforced Plate dal tuo Skylab (2, 4 e 6 piastre). Una cella non cambia mai famiglia: scegli Capacity o Absorption quando compri il tier I. La nuova cella mantiene il grado di incantamento della cella che consuma, e i suoi bonus vengono generati di nuovo ([Potenziamenti dei moduli](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Le celle non entrano in uno [slot abilità](/wiki/03-Mechanics/Abilities.md): vanno dentro gli scudi e i Nuclei adattivi.
