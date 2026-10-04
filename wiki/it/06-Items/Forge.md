<!-- wiki-i18n source: b6b66c2f84c6d17c -->
<!-- wiki-i18n title: Forgia -->
# La Forgia {#the-forge}

La **Forgia** è la seconda scheda della pagina Assemblaggio (e della finestra Assemblaggio in volo). Fa due cose con l’equipaggiamento che possiedi: **fa salire un oggetto di un grado** in cambio di crediti e drop di alieni e **unisce due copie** di un oggetto in una che mantiene il meglio di entrambe. Ha sostituito la vecchia Camera di Fusione, che richiedeva cinque oggetti identici e lasciava il risultato a una probabilità del 25%.

## Che cosa si può forgiare {#what-can-be-forged}

Laser, amp laser, Shield Core, celle scudo, motori, propulsori, Nuclei adattivi e Repair Drone: qualsiasi singolo pezzo di equipaggiamento che possa portare [bonus di incantamento](/wiki/06-Items/Overview.md). Può trovarsi nel tuo inventario, su una nave (ci resta e funziona subito con il nuovo grado) o essere montato in un altro oggetto. Droni, navi, munizioni, risorse e booster non si possono forgiare, e nemmeno nulla che si trovi nel Deposito di trasporto: toglilo prima.

## Sali di grado {#tier-up}

Scegli un oggetto e il pannello mostra il suo grado, il grado che raggiungerebbe, che cosa cambia (quanti bonus può contenere e quanto sono grandi) e il prezzo con ciò che possiedi di ogni parte: in verde se ne hai abbastanza, in rosso se no, con quanti te ne mancano. Quando hai tutto, **Sali di grado** alza l’oggetto di esattamente un grado. Non si salta: per arrivare a Eterno un oggetto passa per Corrotto, Divino e Lacerante, ciascuno con il proprio prezzo.

| Passo | Successo | Crediti | Thulium | Materiali |
| :--- | :---: | :---: | :---: | :--- |
| Da Standard a Corrotto | 100% | 10.000 | – | 5 Ship Fragment, 15 Daraxium |
| Da Corrotto a Divino | 90% | 50.000 | – | 30 Ship Fragment, 45 Nyxite |
| Da Divino a Lacerante | 75% | 200.000 | – | 20 Reinforced Hull Plate, 120 Cataclysite, 2 Dark Matter Plate |
| Da Lacerante a Eterno | 60% | 500.000 | 2.000 | 8 Power Core, 240 Quorvium, 2 Dark Matter Plate |

- I **materiali** vengono dalle tue scorte libere: gli oggetti su una nave e le scorte nel Deposito di trasporto non si usano. Il pannello ti avvisa quando quelli che mancano sono nel deposito.
- **Un passo può fallire.** L’oggetto resta esattamente com’era, i crediti sono persi e metà dei materiali e metà del Thulium tornano indietro (arrotondando per difetto; di due Dark Matter Plate, una). Il pannello ti indica la probabilità e questo prima che tu prema.
- **In caso di successo** ogni bonus dell’oggetto viene generato di nuovo nell’intervallo del nuovo grado e mantiene il valore migliore. Un oggetto senza alcun bonus riceve sempre il primo; ogni altro slot che il nuovo grado apre viene riempito con il **50% di probabilità, ciascuno con il proprio tiro**, con un nuovo bonus su un’altra statistica dell’oggetto, e uno slot che fallisce può riempirsi a un successivo passo di grado (vedi [Bonus per grado](#buffs-by-tier)). Il risultato appare sopra il pannello; l’oggetto resta selezionato, quindi il suo passo successivo è già sullo schermo.
- Un salto di grado è istantaneo.

### Dark Matter Plate {#dark-matter-plates}

Gli ultimi due passi richiedono ciascuno **2 Dark Matter Plate**, in aggiunta a tutto il resto. Una piastra viene pressata in [Assemblaggio](/wiki/06-Items/Overview.md) da **5 Dark Matter, 1 Velkonite Reinforced Plate e 1 Orvium Reinforced Plate** (250 Thulium, 2 minuti), quindi un passo richiede 10 Dark Matter, 2 piastre di Velkonite e 2 piastre di Orvium. La Dark Matter viene dal [buco nero](/wiki/03-Mechanics/Black-Hole.md): circa cinque razzi N.I.K.E. (vedi [Razzi](/wiki/06-Items/Rockets.md)) ne producono dieci; un N.I.K.E. che incontra una nave lungo il percorso colpisce quella nave e non ne produce. Le piastre si prelevano dalle tue scorte libere come gli altri materiali, e il pannello le nomina se ti mancano.

### Bonus per grado {#buffs-by-tier}

| Grado | Bonus contenuti al massimo | Entità di ogni bonus |
| :--- | :---: | :---: |
| Corrotto | 1 | da +2% a +5% |
| Divino | 2 | da +4% a +8% |
| Lacerante | 3 | da +6% a +11% |
| Eterno | 4 | da +9% a +15% |

L’equipaggiamento creato prima della Forgia mantiene i bonus con cui è stato generato, e spesso sono più piccoli di quelli della tabella (un pezzo Divino di allora può contenere +2%). Nulla li aumenta da solo: un salto di grado genera di nuovo ogni bonus nell’intervallo del nuovo grado e mantiene il valore migliore, e un’unione mantiene il valore migliore di ogni statistica.

Un oggetto non può contenere più bonus di quante statistiche ha: uno Shield Core ne ha quattro, un laser tre (il Quantum Laser 1 e il 2 ne hanno due), un motore o un Nucleo adattivo due, un Momentum Thruster due, un Impulse Thruster uno (il suo moltiplicatore di 1,02 o 1,03 è troppo piccolo per un bonus, e la Forgia non ne genera su un moltiplicatore di 1,05 o inferiore, quindi il suo bonus può stare solo sulla velocità fissa), un Crit Amp 1 o un Repair Drone uno, gli amp critici più alti due, gli amp di danno e le celle scudo tre. Quando il grado successivo non contiene più bonus di quanti l’oggetto ne possa portare, il pannello lo dice: il grado rende allora solo più forti i bonus. I bonus di portata non superano mai +5%.

**Un grado contiene al massimo questo numero di bonus.** Un passo di grado dà sempre a un oggetto il suo primo bonus; ogni altro slot che il nuovo grado apre, e per cui l’oggetto ha una statistica, viene riempito con il **50% di probabilità, ciascuno con il proprio tiro**, e uno slot che fallisce viene ritentato dal passo di grado successivo. Quindi uno Shield Core Divino ha due bonus metà delle volte e uno l’altra metà; uno Eterno ha tutti e quattro circa una volta su tre (3,1 in media), un laser con tre statistiche ha tutti e tre due volte su tre, e un motore li ha quasi sempre entrambi. Il pannello dice “fino a” per il grado successivo e indica quanto spesso si riempie un nuovo slot. Gli oggetti con una sola statistica e ogni passo verso Corrotto non sono toccati, e l’equipaggiamento fatto prima di questa regola mantiene i suoi bonus. Un’**unione** riempie uno slot che un passo di grado ha mancato: mantiene il miglior bonus di ogni statistica di due copie, fino al limite del grado. Per via della probabilità, un pezzo porta il bonus di assorbimento descritto qui sotto solo in parte dei casi (uno Shield Core Eterno il 78% delle volte, una cella scudo Eterna l’88%): le cifre lì valgono per i pezzi che lo portano.

Il **bonus di assorbimento di uno scudo** (e il Bonus assorbimento di una cella scudo) moltiplica la statistica, quindi vale punti di [assorbimento](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-) in proporzione: +5% sul 50% di un Heavy Shield Core sono +2,5 punti, e +15% su ogni pezzo del miglior set (un Heavy Shield Core e tre Absorption Shield Cell IV, 80% in tutto) sono +12 punti. Un set Eterno porta tra +7 e +12 punti, circa 10 in media; con lo Shield Absorbance Boost dell’Emporio (+10 punti al suo limite; i punti reset di tutto il gioco comprano 34 dei suoi 100 livelli, +3,4 punti) una nave arriva al 95%, e supera il 100% solo con il limite di quel potenziamento, cosa che la statistica consente: la penetrazione dello scudo di un attaccante viene tolta da essa. Un set Divino porta tra 3 e 6 punti.

Motori, propulsori, Nuclei adattivi e Repair Drone cambiano pochissimo con un bonus percentuale (un Engine II aggiunge 4 di velocità, quindi +12% è mezzo punto): forgiali se vuoi il grado, non per le statistiche.

### Da dove arrivano i materiali {#where-the-materials-drop}

| Materiale | Lasciato da |
| :--- | :--- |
| **Ship Fragment** | ogni alieno |
| **Daraxium** | [Seeker](/wiki/04-Aliens/Seeker.md), [Phantasm](/wiki/04-Aliens/Phantasm.md) |
| **Nyxite** | [Phantasm](/wiki/04-Aliens/Phantasm.md), [Bulwark](/wiki/04-Aliens/Bulwark.md) |
| **Reinforced Hull Plate** | [Bulwark](/wiki/04-Aliens/Bulwark.md), [Goombah](/wiki/04-Aliens/Goombah.md) |
| **Cataclysite** | [Bulwark](/wiki/04-Aliens/Bulwark.md), [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Power Core** | [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Quorvium** | [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Dark Matter Plate** | nessun alieno: l’Assemblaggio la pressa dalla Dark Matter (il [buco nero](/wiki/03-Mechanics/Black-Hole.md)) e dalle piastre dello Skylab |

I cristalli seguono i gradi: Daraxium è blu come Corrotto, Nyxite giallo come Divino, Cataclysite arancione come Lacerante e Quorvium viola come Eterno. Ogni fonte, con probabilità e quantità, è nella pagina [Risorse](/wiki/06-Items/Resources.md) e in quella di ciascun alieno; il booster Resource Magnet aggiunge il 25% a ciò che contiene una cassa.

## Unione {#merge}

Due copie dello stesso oggetto (due Light Shield Core, due Quantum Laser 2) diventano una sola. Passa a **Unisci** e clicca sull’oggetto che vuoi tenere (la **base**), poi su una seconda copia (il **donatore**). Il pannello mostra il risultato prima che tu confermi.

- **La base viene conservata.** Mantiene il suo posto: può essere su una nave o montata in un altro oggetto, e i moduli montati al suo interno restano. **Il donatore viene consumato.** Deve essere libero (non su una nave, non montato), e i moduli montati al suo interno tornano nel tuo inventario.
- **Il risultato ha il più alto dei due gradi** e, per ogni statistica, il **migliore dei due valori**.
- **Non contiene mai più bonus di quanti ne consenta il suo grado.** Se i due oggetti insieme hanno più bonus di quanti ne possa contenere il grado del risultato, si tengono i migliori e gli altri vengono scartati; la tabella li segna (barrati, “oltre il limite”). Per contenere più bonus, fai prima salire di grado l’oggetto. Un’unione non estrae mai nulla a caso: ciò che mostra l’anteprima è ciò che ottieni.
- **Un’unione costa crediti in base al grado che produce**: 5.000 per Corrotto, 25.000 per Divino, 100.000 per Lacerante, 250.000 per Eterno. Nessun materiale.
- Un’unione che non cambierebbe nulla (il risultato non è migliore della base) viene rifiutata.
- Dopo un’unione il risultato resta selezionato e lo slot del donatore è vuoto: inserisci il donatore successivo oppure torna a Sali di grado.

Un’unione non moltiplica un oggetto, ma riempie gli slot che un passo di grado ha mancato: due Shield Core Divini uniti valgono in media circa tre punti e mezzo di bonus in più di uno solo. Serve a scegliere: un nucleo Divino con le statistiche che vuoi, oppure un grado trasferito sull’oggetto della tua nave senza doverlo togliere.

## Potenziamenti dei moduli nell’Assemblaggio {#module-upgrades-in-the-assembly}

I due laser, gli amp laser, le celle scudo e i propulsori dei tier da II a IV, l’Heavy Shield Core e l’Engine III non si vendono, e l’Assemblaggio crea ciascuno solo dopo che ne hai ricercato la tecnologia nello Skylab ([Ricerca](/wiki/03-Mechanics/Research.md)). Li crei nella scheda **Creazione** dell’Assemblaggio potenziando il pezzo di un gradino inferiore: un Pulse Amp in un **Nova Amp**, un Prism Amp in un **Apex Amp**, una Capacity Shield Cell I in una **Capacity Shield Cell II** (e poi III e IV; le Absorption Shield Cell, gli Impulse Thruster e i Momentum Thruster salgono allo stesso modo), un Basic Shield Core in un **Heavy Shield Core**, un Engine II in un **Engine III**, un Quantum Laser 3 in una **Starfire-3** e una Starfire-3 in un **Helios Beam**. Ciò che la Forgia c’entra con tutto questo è il grado.

- **Il grado resta.** Un potenziamento consuma una copia del pezzo e il nuovo oggetto ha il grado di quella copia: un Pulse Amp Divino produce un Nova Amp Divino, uno Standard un Nova Amp Standard. Ciò che hai pagato alla Forgia non va perso. Il potenziamento non aggiunge alcun grado per conto suo, quindi un pezzo Standard produce sempre un risultato Standard.
- **I bonus vengono generati di nuovo.** Il nuovo oggetto riceve bonus nuovi per il suo grado: tanti quanti ne aveva il pezzo che consumi (un Pulse Amp Divino con due bonus produce un Nova Amp Divino con due, uno con un solo bonus ne produce uno con uno solo; sopra Standard, almeno uno), al massimo quelli che il grado contiene e che le statistiche del nuovo oggetto permettono, ciascuno nell’intervallo del grado indicato nella tabella qui sopra, su statistiche che il Nova Amp possiede. Per il resto nulla viene copiato dal vecchio pezzo, quindi i nuovi bonus possono essere migliori o peggiori di quelli che aveva; in media sono uguali. Il numero viene mantenuto perché un potenziamento non riempia gli slot che la Forgia ha mancato, e non ne toglie mai uno: un pezzo fatto prima di questa regola, con tutti gli slot pieni, li mantiene tutti. I bonus vengono generati nel momento in cui metti il lavoro in coda, e ciò che ritiri è ciò che è stato generato: aspettare a ritirare non cambia nulla. Il motivo è che il potenziamento costruisce un nuovo oggetto, mentre i dadi della Forgia si tirano sull’oggetto che hai in mano. Il costo sta nel grado: un pezzo Eterno vale oltre un milione di crediti di passi della Forgia, mentre un bonus è pochi punti percentuali di una statistica.
- **Piastre.** Oltre al Thulium e a ciò che lasciano gli alieni, ogni potenziamento di un modulo richiede **Velkonite Reinforced Plate**: 3 per un amp, 2, 4 o 6 per una cella o un propulsore di tier II, III o IV, 6 per un Heavy Shield Core o un Engine III e 8 per una Starfire-3 (l’Helios Beam richiede invece Orvium Reinforced Plate, 18). Gli alieni non le lasciano. La Fucina del tuo [Skylab](/wiki/03-Mechanics/Skylab.md) le produce dal minerale di Velkonite, 40 unità di minerale per piastra al livello 1 della Fucina. Un Collettore Velkonite di livello 1 estrae 12 unità di minerale all’ora, quindi le piastre di un amp richiedono 10 ore di estrazione e quelle di una cella o di un propulsore di tier IV 20 (4 e 8 ore con un collettore di livello 5). Da dove arriva ogni materiale è spiegato nella pagina [Risorse](/wiki/06-Items/Resources.md). I passi della Forgia richiedono drop e crediti, e quelli più alti richiedono anche piastre (da Divino a Lacerante: 20 Reinforced Hull Plate e 2 Dark Matter Plate; da Lacerante a Eterno: 2 Dark Matter Plate), che è una cosa diversa dalle piastre di Velkonite e Orvium dei potenziamenti dei moduli.
- **Quale copia viene usata.** La scegli tu. Quando possiedi copie diverse (un altro grado o altri bonus), la scheda della ricetta le mostra come una fila di riquadri: clicca su quella da usare, e la riga sotto i riquadri mostra che cosa diventa (“Pulse Amp Divino”, poi “Risultato: Nova Amp Divino”). Se non ne scegli nessuna, va la più semplice: prima il grado più basso e, tra le copie dello stesso grado, la più vecchia, qualunque siano i loro bonus. Una copia Divina o superiore non viene mai usata finché ce n’è una più semplice libera. Usare una copia sopra Standard chiede prima conferma e nomina l’oggetto.
- **Quali copie si possono usare.** Quelle libere: una copia su una nave (anche in uno slot abilità), montata in un altro oggetto, che contiene celle o propulsori propri o che si trova nel [Deposito di trasporto](/wiki/03-Mechanics/Cargo.md) non si può usare, e l’Assemblaggio te lo dice. Toglila prima dalla nave o dal deposito. Due potenziamenti avviati insieme non possono usare la stessa copia.

- **Anche la Starfire-3 è un potenziamento.** Si ottiene da un **Quantum Laser 3** (con 1.500 Thulium, 100.000 crediti, drop e 8 Velkonite Reinforced Plate: vedi [Laser](/wiki/06-Items/Lasers.md)) e vale tutto quanto detto sopra: un Quantum Laser 3 Divino produce una Starfire-3 Divina con nuovi bonus, scegli tu la copia, la scheda chiede conferma prima di usarne una sopra Standard e il Quantum Laser 3 deve essere libero: toglilo prima nell’Hangar e il pulsante Assembla dice “Rimuovi Quantum Laser 3” finché non lo fai. Il grado poi continua a salire: una Starfire-3 Divina produce un Helios Beam Divino.

- **Anche l’Helios Beam è un potenziamento.** Si ottiene da una **Starfire-3** (con 2.000 Thulium, drop e 18 Orvium Reinforced Plate: vedi [Laser](/wiki/06-Items/Lasers.md)) e vale tutto quanto detto sopra: una Starfire-3 Divina produce un Helios Beam Divino con nuovi bonus (tanti quanti ne aveva la Starfire-3, al massimo due delle sue tre statistiche), scegli tu la copia, la scheda chiede conferma prima di usarne una sopra Standard e la Starfire-3 deve essere libera. Un laser è montato su una nave e porta degli amp, quindi spesso non lo è: toglilo prima nell’Hangar (i suoi amp tornano nel tuo inventario) e il pulsante Assembla dice “Rimuovi Starfire-3” finché non lo fai.

Le ricette, i loro costi e i numeri dietro la regola sono nella [panoramica degli oggetti](/wiki/06-Items/Overview.md#upgrading-modules) e, per la Starfire-3 e l’Helios Beam, nella pagina [Laser](/wiki/06-Items/Lasers.md).

## Vecchi server {#old-servers}

Un server di gioco non ancora aggiornato alla Forgia mostra “La Forgia non è ancora su questo server” al posto della scheda; la Creazione funziona come prima. Un client di gioco precedente alla Forgia mostra la vecchia scheda Fusione su un server aggiornato e riceve l’invito ad aggiornarsi.
