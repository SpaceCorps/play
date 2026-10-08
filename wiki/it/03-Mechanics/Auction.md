<!-- wiki-i18n source: 9b9606619f84bd51 -->
<!-- wiki-i18n title: Asta -->
# Asta {#auction}

L’asta è il mercato dei piloti e, insieme, i lotti orari del gioco stesso, in una pagina del menu della stazione. Come il Negozio, è una pagina della stazione: la usi attraccato, non in volo. Ha quattro sezioni. **Mercato** è ciò che altri piloti hanno in vendita. **Lotti** sono le offerte del gioco stesso, una ogni ora. **Le mie inserzioni** è ciò che hai tu in vendita. **Cronologia** sono le tue vendite, i tuoi acquisti e i lotti che hai vinto, e come sono andati i tuoi scambi.

<!-- market-glance:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- Ti serve il **livello 5** per usare l’asta: per mettere in vendita, comprare e fare offerte.
- Un’inserzione ha un prezzo per lotto, in crediti interi o in Thulium interi (non entrambi), e mai sotto il prezzo minimo dell’oggetto. **Non esiste un prezzo massimo.**
- Un prezzo in Thulium è almeno il prezzo minimo in crediti diviso per il tasso (1.000), arrotondato per eccesso, e solo per gli oggetti il cui prezzo minimo arriva a 1 Thulium o più. È tutto ciò che fa il tasso: **1 Thulium = 1.000 crediti è una regola per il prezzo minimo, non un tasso di cambio.** Nulla viene scambiato, nessun valore viene mostrato, e crediti e Thulium non si sommano mai.
- 80 oggetti si possono mettere in vendita, e 79 di essi si possono anche prezzare in Thulium.
- Un’inserzione dura 24 / 72 / 168 ore, a tua scelta: le opzioni sono le stesse a ogni livello.
- Il **deposito** è pari a 1% del prezzo per ogni 24 ore di durata dell’inserzione, con un minimo di 50 crediti o 1 Thulium. Lo paghi quando metti in vendita; non viene mai restituito, nemmeno se annulli l’inserzione.
- Dal livello 10 il deposito è pari a 1,5%.
- L’**imposta** è pari a 5% del prezzo. Viene trattenuta da ciò che riceve il venditore quando l’inserzione si vende.
- Il deposito e l’imposta vengono distrutti: non vanno a nessuno.
- Dal giorno 28 della stagione fino al reset non ci sono né deposito né imposta.
- Dal giorno 30 della stagione l’asta è chiusa fino all’inizio della nuova stagione: non si può mettere in vendita, comprare o fare offerte. Puoi comunque annullare le tue inserzioni.
- Ogni valuta ha un suo limite su quanto puoi vendere e su quanto puoi comprare in 24 ore (tabella dei livelli qui sotto). I lotti vinti non contano.
- Tra due piloti, uno che compra dall’altro, passano al massimo 8.000.000 crediti o 40.000 Thulium in 24 ore.

<!-- market-glance:end -->

## Oggetti vendibili {#marketable-items}

Si possono vendere solo gli oggetti che hai **guadagnato**. Tutto ciò che guadagni porta nell’[Hangar](/wiki/03-Mechanics/Inventory.md#marketable-items) un piccolo contrassegno, **Vendibile**: ciò che raccogli nello spazio (bottino di alieni, sciami, Warden e buco nero: [Carico](/wiki/03-Mechanics/Cargo.md)), ciò che paga una missione ([Missioni](/wiki/03-Mechanics/Quests.md#rewards)) e tutto ciò che fanno l’Assemblaggio e la Forgia. Ciò che hai **comprato** al Negozio, vinto in un lotto, comprato sul Mercato, ricevuto con un codice bonus, un pacchetto d’invito o il kit iniziale, o riavuto come rimborso non è vendibile e non si può mai rivendere, così nulla viene comprato solo per essere rivenduto. Neppure le piastre prodotte dalla Fucina dello Skylab sono vendibili; le Reinforced Plate che paga una missione lo sono.

Il contrassegno è un numero di unità, non un interruttore: una pila di munizioni può contenere colpi comprati e guadagnati, e la scheda dice «Vendibile (3 / 5)». Quando usi una parte di una pila (sparare, creare), se ne vanno prima le unità semplici, così quelle vendibili durano più a lungo. Unire due pezzi nella [Forgia](/wiki/06-Items/Forge.md#merge) mantiene il contrassegno solo se lo avevano entrambi, e l’anteprima lo dice; un passaggio della Forgia che fallisce restituisce i suoi materiali come unità semplici.

Il filtro **Solo vendibile** dell’Hangar mostra solo ciò che puoi vendere, e il **martelletto** accanto al cestino di un oggetto contrassegnato apre per lui la scheda di vendita dell’Asta. Nell’Assemblaggio, una ricetta il cui risultato è vendibile lo dice, e un materiale che ti manca ha un collegamento che apre l’Asta con il suo nome nella ricerca.

Quando è arrivata l’Asta (0.4.12), l’equipaggiamento che già avevi e che il Negozio non vende, e le risorse, sono stati contrassegnati una volta. Questi no, perché il Negozio li ha venduti un tempo o perché ciò che hai mescola pezzi comprati e guadagnati: il Quantum Laser III, le Absorption Shield Cell II e III, gli Impulse Thruster II e III, le due Reinforced Plate e la Base CPU I più vecchia di ogni pilota (quella del kit iniziale). I nuovi di questi che guadagni o crei sono contrassegnati.

## Che cosa si può vendere {#what-can-be-sold}

<!-- market-kinds:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Tipo | Oggetti che puoi vendere | Numero |
| :--- | :--- | ---: |
| **Laser** | Quantum Laser I, Quantum Laser II, Quantum Laser III, Starfire-III, Helios Beam | 5 |
| **Amplificatori laser** | Damage Amp I, Crit Amp I, Penetration Amp I, Damage Amp II, Crit Amp II, Penetration Amp II, Damage Amp III, Crit Amp III, Penetration Amp III, Damage Amp IV, Crit Amp IV, Penetration Amp IV | 12 |
| **Shield Core** | Light Shield Core, Basic Shield Core, Heavy Shield Core | 3 |
| **Motori** | Engine I, Engine II, Engine III | 3 |
| **Adaptive Core** | Adaptive Core I, Adaptive Core II, Adaptive Core III | 3 |
| **Celle scudo** | Absorption Shield Cell I, Capacity Shield Cell I, Absorption Shield Cell II, Capacity Shield Cell II, Absorption Shield Cell III, Capacity Shield Cell III, Absorption Shield Cell IV, Capacity Shield Cell IV | 8 |
| **Propulsori** | Impulse Thruster I, Momentum Thruster I, Impulse Thruster II, Momentum Thruster II, Impulse Thruster III, Momentum Thruster III, Impulse Thruster IV, Momentum Thruster IV | 8 |
| **Munizioni laser** | Standard Battery (in lotti da 100), Siphon Battery (in lotti da 10), Advanced Plasma (in lotti da 10), Ultra Core (in lotti da 10), Experimental Fusion Core | 5 |
| **Razzi** | Ember I, Lancet I, Rivet I, Scatter I, Ember II, Lancet II, Rivet II, Scatter II, Ember III, Lancet III, Rivet III, Scatter III | 12 |
| **Extra** | Repair Drone I, Repair Drone II, Repair Drone III, EMP Charge, Repair Drone IV, Cloaking CPU S, Base CPU I, Cloaking CPU M, Auto-Repair CPU, Cloaking CPU L, Base CPU II | 11 |
| **Risorse** | Cataclysite (in lotti da 100), Ship Fragment (in lotti da 100), Daraxium (in lotti da 100), Nyxite (in lotti da 100), Quorvium (in lotti da 10), Reinforced Hull Plate (in lotti da 10), Power Core, Velkonite Reinforced Plate, Dark Matter, Orvium Reinforced Plate | 10 |

<!-- market-kinds:end -->

Navi, droni, formazioni di droni, booster e abbonamenti non si possono mai vendere, né l’Ancient Control Unit, i minerali Velkonite e Orvium, la Dark Matter Plate, la Jump CPU, le Extra Slots CPU, la N.U.K.E. e la N.I.K.E. Le Dark Matter Plate non sono affatto all’Asta, né come merce né come prezzo. Un oggetto equipaggiato, innestato in un altro oggetto, con moduli dentro o nel [Deposito di trasporto](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) non si può mettere in vendita, e nemmeno una Cloaking CPU, una EMP Charge o una Base CPU già usata. Munizioni e razzi si vendono dalla stazione: fai prima atterrare la nave.

## Vendere {#selling}

Premi **Vendi un oggetto** (o il martelletto nell’Hangar), scegli ciò che hai guadagnato (un menu a tendina delle categorie restringe l’elenco, con le stesse categorie del Mercato), scegli crediti o Thulium, fissa il prezzo di un lotto e quanto dura l’inserzione: 1, 3 o 7 giorni. La scheda mostra il prezzo minimo, tre filtri che inseriscono un prezzo (**Minimo**; **Vendita rapida**, uno sotto l’inserzione più bassa del momento; ed **Equo**, il prezzo dell’ultima vendita), e il deposito, l’imposta e ciò che ricevi, prima di mettere in vendita. Sotto il prezzo, **Inserzioni simili** mostra in un grafico a quali prezzi è in vendita ora lo stesso oggetto con lo stesso incantamento, nella valuta che hai scelto: il tuo prezzo è una linea sul grafico, il prezzo minimo, l’ultima vendita e il prezzo del Negozio sono segnati, una riga a parole dice dove starebbe il tuo prezzo e sotto compaiono le tre inserzioni più economiche. Un pezzo è un lotto di uno; le munizioni e alcune risorse si vendono in lotti da 10 o 100, e vendi un numero intero di lotti. Ciò che metti in vendita lascia il tuo inventario ed è tenuto dal server finché non si vende, non lo annulli o non scade; poi torna, con il suo contrassegno. Puoi annullare in qualsiasi momento, anche negli ultimi giorni di una stagione. Un’inserzione è un’istantanea: per cambiare un prezzo, annulla l’inserzione e rimettila in vendita (il deposito si paga di nuovo).

Ogni oggetto ha un **prezzo minimo** e **non esiste un prezzo massimo**: chiedi quello che vuoi. La tabella mostra il prezzo minimo di alcuni oggetti.

<!-- market-bands:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Oggetto | Venduto in lotti da | Prezzo minimo, crediti | Prezzo minimo, Thulium |
| :--- | ---: | ---: | ---: |
| Quantum Laser II | 1 | 32.000 | 32 |
| Quantum Laser III | 1 | 170.000 | 170 |
| Helios Beam | 1 | 1.600.000 | 1.600 |
| Absorption Shield Cell IV | 1 | 1.100.000 | 1.100 |
| Heavy Shield Core | 1 | 870.000 | 870 |
| Impulse Thruster IV | 1 | 980.000 | 980 |
| EMP Charge | 1 | 40.000 | 40 |
| Cloaking CPU S | 1 | 400.000 | 400 |
| Ultra Core | 10 | 800 | 1 |
| Lancet I | 1 | 200 | 1 |
| Ship Fragment | 100 | 600 | 1 |
| Dark Matter | 1 | 33.000 | 33 |

<!-- market-bands:end -->

Un prezzo in Thulium segue una sola regola: il prezzo minimo in crediti diviso per il tasso, arrotondato per eccesso. Il tasso non è un valore che il gioco dà al Thulium. Serve solo a calcolare il prezzo minimo in Thulium, e per questo un’inserzione in Thulium può essere economica per un pilota che ha Thulium. La maggior parte dei venditori chiederà crediti. Ogni oggetto tranne il **Quorvium** si può prezzare in Thulium, anche quelli economici (munizioni, razzi, risorse comuni): il loro prezzo minimo è allora 1 Thulium, il passo più piccolo. Solo il Quorvium si prezza unicamente in crediti, perché 1 Thulium varrebbe più di un suo lotto.

Le tue **inserzioni aperte** (e un’inserzione che un admin ha sospeso) occupano posti. Salendo di livello hai più posti, fino a un massimo, e puoi vendere e comprare di più al giorno. Quanto può durare un’inserzione è uguale a ogni livello.

<!-- market-limits:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Livello | Inserzioni aperte | Durata massima | Al giorno, crediti | Al giorno, Thulium | Deposito ogni 24 h |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 5 | 20 | 168 h | 4.500.000 | 22.500 | 1% |
| 6 | 40 | 168 h | 6.000.000 | 30.000 | 1% |
| 7 | 70 | 168 h | 7.500.000 | 37.500 | 1% |
| 8 | 100 | 168 h | 8.500.000 | 42.500 | 1% |
| 9 | 100 | 168 h | 10.000.000 | 50.000 | 1% |
| 10 | 100 | 168 h | 15.000.000 | 75.000 | 1,5% |
| 11 | 100 | 168 h | 15.000.000 | 75.000 | 1,5% |
| 12 | 100 | 168 h | 15.000.000 | 75.000 | 1,5% |
| 13 | 100 | 168 h | 20.000.000 | 100.000 | 1,5% |
| 14 | 100 | 168 h | 20.000.000 | 100.000 | 1,5% |
| 15 | 100 | 168 h | 20.000.000 | 100.000 | 1,5% |
| 16 | 100 | 168 h | 20.000.000 | 100.000 | 1,5% |
| 17 | 100 | 168 h | 20.000.000 | 100.000 | 1,5% |
| 18 | 100 | 168 h | 20.000.000 | 100.000 | 1,5% |
| 19 | 100 | 168 h | 20.000.000 | 100.000 | 1,5% |
| 20 e oltre | 100 | 168 h | 20.000.000 | 100.000 | 1,5% |

<!-- market-limits:end -->

## Commissioni {#fees}

Un’inserzione costa un **deposito**, pagato quando la metti in vendita e mai restituito, e una vendita costa un’**imposta**, trattenuta da ciò che riceve il venditore. Entrambi sono pagati nella valuta dell’inserzione e **distrutti**: non vanno a nessuno, quindi nessuno guadagna commerciando con se stesso. Negli ultimi due giorni di una stagione non ci sono né deposito né imposta.

<!-- market-fees:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Inserzione | Prezzo | Deposito | Imposta | Il venditore riceve |
| :--- | ---: | ---: | ---: | ---: |
| Quantum Laser III: livello 6, 24 h | 170.000 crediti | 1.700 crediti | 8.500 crediti | 161.500 crediti |
| Quantum Laser III: livello 10, 72 h | 170 Thulium | 8 Thulium | 8 Thulium | 162 Thulium |
| Helios Beam: livello 12, 168 h | 2.500.000 crediti | 262.500 crediti | 125.000 crediti | 2.375.000 crediti |
| Helios Beam: livello 12, 168 h, negli ultimi giorni di una stagione | 2.500.000 crediti | 0 crediti | 0 crediti | 2.500.000 crediti |

<!-- market-fees:end -->

## Comprare {#buying}

Il **Mercato** mostra ciò che vendono gli altri piloti. Restringi l’elenco con i **filtri di categoria** (uno per ogni tipo di oggetto, con il numero di inserzioni che contiene), cerca per nome, filtra per incantamento e valuta, e ordina per prezzo, per ciò che finisce prima o per ciò che è più nuovo. Scegli un’inserzione per vedere che cos’è, chi la vende, quanto dura e come sta il suo prezzo rispetto all’ultima vendita, al prezzo più basso del momento e al prezzo del Negozio. Una pila si compra a lotti interi. Un acquisto grande chiede un’ultima conferma. Il venditore è pagato subito, meno l’imposta; tu non paghi né deposito né imposta. Ciò che compri **non è vendibile**: la pagina dice «Ottieni: non commerciabile» accanto a **Compra**, perché si può vendere solo ciò che guadagni. Non puoi comprare la tua inserzione. Un’inserzione che si vende mentre la guardi dice «Questa inserzione non c’è più.»

## Limiti {#limits}

Ogni valuta ha un suo limite giornaliero su quanto puoi vendere e su quanto puoi comprare, contato sulle ultime 24 ore, e un limite su ciò che passa tra due piloti, così un secondo account non è un modo rapido per spostare una fortuna. Crediti e Thulium non si sommano mai: chi vende per Thulium usa il suo limite di Thulium, e nient’altro. La scheda di vendita ti avvisa quando una vendita supererebbe il tuo limite giornaliero di vendita, e quando un acquisto supererebbe il tuo limite giornaliero di acquisto, il Mercato te lo dice e lascia spento **Compra**. I limiti crescono con il livello, e Premium non ne cambia nessuno. I lotti vinti non contano.

I razzi in un’inserzione, in un lotto di cui sei in testa e nella tua stiva contano tutti nel massimo di un razzo che puoi portare: con un’inserzione non puoi portare più di quanto consente la pila del Negozio.

## Le mie inserzioni e Cronologia {#my-listings-and-history}

**Le mie inserzioni** mostra i tuoi posti e ogni inserzione con il suo stato (aperta, venduta, annullata, scaduta, restituita o sospesa), un pulsante **Annulla**, **Rimetti in vendita** per una chiusa e un’etichetta **Battuta** quando un’altra inserzione dello stesso oggetto chiede meno. Un’inserzione scaduta torna da sola nel tuo inventario. La **Cronologia** si apre con i tuoi scambi degli ultimi 30 giorni: le tue vendite e i tuoi acquisti, quanto hai incassato e speso, le commissioni e le imposte che hai pagato, il tuo risultato netto, la tua vendita migliore, la tua vendita media e l’oggetto che hai scambiato di più, e due grafici a linee: i tuoi incassi al giorno e il tuo risultato finora (in crediti o in Thulium, una valuta alla volta). Sotto c’è l’elenco di ciò che hai venduto, comprato e vinto, con l’imposta. Il gioco conserva il registro dell’Asta per 90 giorni.

Vieni avvisato quando qualcosa si vende: da una notifica, dal suono dell’Asta e dal nuovo saldo, e da un badge sulla voce dell’Asta finché la pagina è chiusa. Una serie di vendite è una sola notifica. L’Asta ha suoni discreti tutti suoi, uno per ogni cosa che fai o che ti accade lì (mettere in vendita, finire, una vendita, un’offerta, essere superato, vincere), e seguono il volume dell’interfaccia.

## I lotti orari {#the-hourly-lots}

I Lotti sono le offerte del gioco stesso: munizioni, razzi ed EMP Charge, ogni ora, per le offerte. Sono un modo per comprare munizioni a meno di quanto chiede il Negozio, e un pozzo: l’offerta vincente viene distrutta. Si aprono solo i lotti della tabella del giorno qui sotto (mai munizioni x1 o x4, mai Siphon Battery, mai un razzo speciale), nella valuta del Negozio. Un lotto di razzi non supera mai il massimo di quel razzo che puoi portare (la pila del Negozio), quindi un’offerta che ti farebbe superarlo viene rifiutata: fai un’offerta su un lotto di razzi quando ne porti pochi.

<!-- market-lots:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- All’inizio di ogni ora UTC si apre un nuovo lotto, che resta aperto 4 ore, così ne sono aperti 4 insieme.
- L’offerta iniziale è pari a 40% del prezzo di Negozio della merce. Ogni offerta successiva deve superare la più alta di almeno 5%, e di almeno 100 crediti o 1 Thulium.
- La tua offerta viene pagata subito e trattenuta. Se qualcuno rilancia, ti torna indietro subito.
- Un’offerta negli ultimi 2 min di un lotto sposta la sua fine a 2 min dopo l’offerta, al massimo 5 volte.
- Ciò che vinci serve per volare, non per commerciare: non è mai vendibile. L’offerta vincente viene distrutta. Un lotto su cui nessuno offre non viene venduto e non costa nulla a nessuno.
- La dimensione di un lotto segue i piloti di livello 5 o più che hanno guardato l’asta negli ultimi 3 giorni: con nessuno è pari a 10% della dimensione in tabella, da 30 in su la dimensione piena, a passi di 500 per le munizioni, 50 per i razzi e 1 per le EMP Charge.
- Nelle ultime 6 ore di una stagione non viene creato alcun lotto. Il reset annulla i lotti ancora aperti e ogni offerta viene restituita.

<!-- market-lots:end -->

<!-- market-day:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Ora UTC | Lotto | Dimensione piena | Pagato in | Offerta iniziale a dimensione piena |
| :--- | :--- | ---: | :--- | ---: |
| 00:00 | Scatter III | 1.250 | Thulium | 2.500 Thulium |
| 01:00 | Advanced Plasma | 25.000 | Thulium | 5.000 Thulium |
| 02:00 | Lancet I | 12.500 | Crediti | 2.500.000 crediti |
| 03:00 | EMP Charge | 5 | Thulium | 1.000 Thulium |
| 04:00 | Ultra Core | 25.000 | Thulium | 10.000 Thulium |
| 05:00 | Rivet II | 5.000 | Crediti | 1.600.000 crediti |
| 06:00 | Advanced Plasma | 10.000 | Thulium | 2.000 Thulium |
| 07:00 | Advanced Plasma | 50.000 | Thulium | 10.000 Thulium |
| 08:00 | Ember I | 12.500 | Crediti | 2.500.000 crediti |
| 09:00 | Ultra Core | 50.000 | Thulium | 20.000 Thulium |
| 10:00 | Scatter II | 5.000 | Crediti | 1.600.000 crediti |
| 11:00 | EMP Charge | 5 | Thulium | 1.000 Thulium |
| 12:00 | Advanced Plasma | 50.000 | Thulium | 10.000 Thulium |
| 13:00 | Lancet III | 1.250 | Thulium | 2.500 Thulium |
| 14:00 | Ultra Core | 10.000 | Thulium | 4.000 Thulium |
| 15:00 | Advanced Plasma | 25.000 | Thulium | 5.000 Thulium |
| 16:00 | Ultra Core | 50.000 | Thulium | 20.000 Thulium |
| 17:00 | Rivet I | 12.500 | Crediti | 2.500.000 crediti |
| 18:00 | Advanced Plasma | 50.000 | Thulium | 10.000 Thulium |
| 19:00 | Ember II | 5.000 | Crediti | 1.600.000 crediti |
| 20:00 | Ultra Core | 25.000 | Thulium | 10.000 Thulium |
| 21:00 | Advanced Plasma | 25.000 | Thulium | 5.000 Thulium |
| 22:00 | Advanced Plasma | 10.000 | Thulium | 2.000 Thulium |
| 23:00 | EMP Charge | 5 | Thulium | 1.000 Thulium |

<!-- market-day:end -->

Quando pochi piloti usano l’Asta, i lotti sono piccoli, così a una manciata di piloti non vengono offerte migliaia di munizioni ogni ora; crescono man mano che più piloti guardano.

## La stagione e il reset {#the-season-and-the-wipe}

L’Asta segue la stagione (vedi [Cronologia del reset](/wiki/03-Mechanics/Wipe-Timeline.md)). Negli ultimi due giorni non ci sono commissioni. Dal giorno 30, quando parte il conto alla rovescia di cinque minuti del reset, è chiusa: nulla viene messo in vendita, comprato o offerto, un lotto che finisce allora viene annullato e la sua offerta restituita, e puoi comunque annullare le tue inserzioni. Un’inserzione non dura mai oltre la fine della stagione.

Al reset **ogni inserzione aperta torna al suo venditore** come oggetti sfusi, e il reset cancella poi gli oggetti sfusi come tutti gli altri (resta solo ciò che metti nel [Deposito di trasporto](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-)): quindi vendi, oppure annulla e metti nel Deposito ciò che vuoi tenere. I lotti ancora aperti vengono annullati e le offerte rimborsate. Crediti e Thulium non vengono azzerati.

## Ciò che l’Asta non ti dà {#what-the-auction-does-not-give-you}

L’Asta serve a scambiare ciò che guadagni, ed è onesta sui suoi limiti.

- **Vendere bottino non è un grind.** Il bottino grezzo degli alieni è fatto solo di risorse e vale dallo 0,4 allo 0,9 per cento di ciò che la stessa ora di caccia al livello 5 paga in uccisioni. Ciò che il Mercato dà a un pilota nuovo è l’equipaggiamento che le sue missioni pagano e di cui non ha bisogno (una volta), le risorse delle missioni Sfida, le casse dei boss degli sciami e ciò che crea.
- **Non c’è un commerciante.** Gli ordini d’acquisto, in cui un pilota dice che cosa vuole comprare e a quanto, non sono in questa versione. Finché non ci sono, gli unici commercianti sono l’artigiano, che compra materiali, crea equipaggiamento nell’Assemblaggio e lo vende, e il pilota magazziniere, che tiene le scorte nel Deposito di trasporto attraverso il reset.
- **L’equipaggiamento del Negozio non è fatto per la rivendita.** L’equipaggiamento che hai comprato al Negozio non si può rivendere: ne fanno parte il Quantum Laser I e II, il Light e il Basic Shield Core, Engine I e II, il primo grado di celle e propulsori, gli amp che vende il Negozio e le munizioni comprate. L’unico Quantum Laser II vendibile di un pilota è quello che una missione paga una volta.
- **Le piastre vengono dalle missioni.** Le Velkonite e Orvium Reinforced Plate sul Mercato sono quelle che pagano le missioni Sfida. Le piastre della Fucina restano fuori, altrimenti sarebbero la merce più grande del Mercato.

Se un’inserzione ti sembra sbagliata, segnalala nel modo consueto: gli amministratori del gioco possono sospendere un’inserzione, restituirla, mettere in pausa l’Asta o escludere un pilota, e ogni azione di questo tipo viene registrata.
