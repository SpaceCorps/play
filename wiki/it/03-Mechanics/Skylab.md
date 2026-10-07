<!-- wiki-i18n source: 011fc9c31c4045f1 -->
<!-- wiki-i18n title: Skylab -->
# Skylab

Lo Skylab è la tua stazione orbitale personale. Costruisce e potenzia moduli che producono crediti e Thulium, estraggono minerale, forgiano le piastre che l’Assemblaggio trasforma nei laser migliori e, dal livello 10 del Nucleo, ricercano le tecnologie di cui l’Assemblaggio ha bisogno. Lavora per te anche quando sei offline.

> [!NOTE]
> **Cosa è cambiato nella 0.4.10.** Ogni modulo dello Skylab ha ora una propria tabella di produzione, prezzi e tempi, livello per livello. Hai mantenuto i tuoi livelli: non è stato addebitato nulla e non è stato rimborsato nulla per la differenza. Ciò che le tue fattorie e i tuoi collettori avevano nelle tramogge quando è arrivato l’aggiornamento è stato pagato **una sola volta, alla vecchia tariffa**: crediti e Thulium sono andati sul tuo account, il minerale nel tuo Magazzino risorse, e le tramogge sono ripartite da vuote.
>
> Due regole sono nuove. **Solare produce solo il 25% della sua energia mentre si potenzia**, quindi nella maggior parte delle stazioni tutte le fattorie e i collettori si fermano finché il potenziamento non è finito (vedi [Modulo Solare](#solar-module) e [Pianificare un potenziamento di Solare](#timing-a-solar-upgrade)). **Il Magazzino risorse ha un limite proprio per ogni minerale**: un giorno di produzione del collettore al livello 1, quattro giorni al livello 20.

![The Skylab station fully grown](../../img/wiki-img/shots/skylab-station.jpg)
![The Resource Storage card of the Skylab](../../img/wiki-img/shots/skylab-storage.jpg)
![The Skylab table of modules: level, production, storage and power of every module, with the 0.4.10 numbers](../../img/wiki-img/shots/skylab-table.jpg)

## In un minuto {#in-one-minute}

- Costruisci prima **Solare**: senza la sua energia nello Skylab non funziona niente. La Fattoria crediti non costa nulla da costruire, la Fattoria Thulium costa 5.000 crediti e 500 Thulium.
- Fattorie e collettori riempiono una **tramoggia** (da 72 ore) mentre sei via. **Raccogli** la sposta sul tuo account (crediti, Thulium) o nel tuo Magazzino risorse (minerale).
- La **Fattoria Thulium** è la tua principale fonte di Thulium: 50 all’ora al livello 1, 1.600 al livello 20. La Fattoria crediti produce 500 crediti all’ora al livello 1 e 50.000 al livello 20.
- Il **Nucleo** dà il ritmo: nessun modulo lo supera, e la sua salita richiede da sola circa 16 giorni e mezzo.
- **Solare produce solo il 25% della sua energia mentre si potenzia**, quindi le tue fattorie e i tuoi collettori si fermano finché non ha finito. [Pianificalo](#timing-a-solar-upgrade).

## Panoramica {#overview}

Lo Skylab segue un orologio tutto suo, indipendente dalla tua nave: i moduli producono e forgiano mentre sei via. Il tuo compito è costruire, potenziare, mantenere l’energia in equilibrio e raccogliere. La pagina offre quattro viste della stessa stazione: **Stazione** (la stazione in 3D, con un’etichetta sopra ogni modulo; clicca su una per aprirne il pannello, oppure premi da **1** a **9**), **Elenco** (una scheda per ogni modulo), **Tabella** (i valori di tutti i moduli in un’unica tabella) e **Ricerca** (la schermata propria del Centro ricerche, vedi [Ricerca](/wiki/03-Mechanics/Research.md)). Passando il puntatore su **Costruisci** o **Potenzia** vedi cosa cambia al livello successivo, quanto costa e quanto tempo richiede.

La stazione è composta da nove moduli:

| Modulo | Produce o fa | Disponibile da |
| :--- | :--- | :--- |
| **Nucleo** | Stabilisce il livello massimo di ogni altro modulo | Sempre presente |
| **Solare** | Produce energia | Qualsiasi livello del Nucleo |
| **Fattoria crediti** | Produce [crediti](/wiki/01-General/Getting-Started.md) | Qualsiasi livello del Nucleo |
| **Fattoria Thulium** | Produce [Thulium](/wiki/01-General/Getting-Started.md) | Qualsiasi livello del Nucleo |
| **Collettore Velkonite** | Estrae minerale di Velkonite | Nucleo al livello 5 |
| **Collettore Orvium** | Estrae minerale di Orvium | Nucleo al livello 5 |
| **Magazzino risorse** | Conserva il minerale | Nucleo al livello 5 |
| **Fucina** | Forgia il minerale in piastre | Nucleo al livello 5 |
| **Centro ricerche** | Trasforma le risorse in scienza e ricerca [tecnologie](/wiki/03-Mechanics/Research.md) | Nucleo al livello 10 |

**Missioni dedicate.** Dieci [missioni Stazione](/wiki/03-Mechanics/Quests.md#station-missions) in Mission Control ti guidano attraverso lo Skylab: costruisci Solare, una Fattoria crediti e una Fattoria Thulium, potenzia il Nucleo e Solare, raccogli i tuoi primi 50.000 crediti e apri la filiera, e ti pagano un po’ per ogni passo. La prima è aperta dal livello 1.

## La stazione a ogni livello {#the-station-at-every-level}

Ecco la vista Stazione dello Skylab a ogni livello da 1 a 20, tutte dalla stessa angolazione, con ogni modulo allo stesso livello. La vista inquadra l’intera stazione, quindi la scala non è la stessa in tutte le immagini: fa un salto quando la forma cresce. La stazione cresce a gradini: la sua forma cambia ai **livelli 1, 5, 10, 15 e 20**, e nel mezzo ogni livello accende **una luce in più** sul collare di ciascun modulo (il numero di luci accese è il livello, e l’anello di venti luci del Nucleo si riempie allo stesso modo).

**Livelli da 1 a 4.** I primi quattro moduli intorno al Nucleo: Solare, la Fattoria crediti, la Fattoria Thulium e la baia di attracco che ospita la tua nave. La filiera non si può ancora costruire.

![Livello 1](../../img/skylab/wiki/level-01.jpg)
![Livello 2](../../img/skylab/wiki/level-02.jpg)
![Livello 3](../../img/skylab/wiki/level-03.jpg)
![Livello 4](../../img/skylab/wiki/level-04.jpg)

**Livelli da 5 a 9.** Con il Nucleo al livello 5 si può costruire la filiera: i due collettori sulle loro strutture sopra la stazione, il Magazzino risorse alla porta nord-est del Nucleo e la Fucina alla sua porta nord-ovest (qui sono mostrati già costruiti).

![Livello 5](../../img/skylab/wiki/level-05.jpg)
![Livello 6](../../img/skylab/wiki/level-06.jpg)
![Livello 7](../../img/skylab/wiki/level-07.jpg)
![Livello 8](../../img/skylab/wiki/level-08.jpg)
![Livello 9](../../img/skylab/wiki/level-09.jpg)

**Livelli da 10 a 14.** Il Nucleo indossa il suo anello, le fattorie e i collettori assumono la loro forma più grande e la Fattoria Thulium riceve un anello tutto suo.

![Livello 10](../../img/skylab/wiki/level-10.jpg)
![Livello 11](../../img/skylab/wiki/level-11.jpg)
![Livello 12](../../img/skylab/wiki/level-12.jpg)
![Livello 13](../../img/skylab/wiki/level-13.jpg)
![Livello 14](../../img/skylab/wiki/level-14.jpg)

**Livelli da 15 a 19.** Le fattorie si riempiono di casse e cristalli, la baia di attracco illumina la sua via d’accesso e l’impianto Solare si completa in cima.

![Livello 15](../../img/skylab/wiki/level-15.jpg)
![Livello 16](../../img/skylab/wiki/level-16.jpg)
![Livello 17](../../img/skylab/wiki/level-17.jpg)
![Livello 18](../../img/skylab/wiki/level-18.jpg)
![Livello 19](../../img/skylab/wiki/level-19.jpg)

**Livello 20.** Il vertice della scala: la corona sul Nucleo e le torri al completo delle fattorie e della filiera.

![Livello 20](../../img/skylab/wiki/level-20.jpg)

**Le schede dei nove moduli.** La vista Elenco della stessa stazione al livello 20: i quattro moduli della prima versione, il Collettore Velkonite, il Collettore Orvium, il Magazzino risorse e la Fucina, arrivati con la filiera, e il Centro ricerche. Ogni scheda mostra il livello del modulo, la sua produzione, la sua energia e il suo interruttore. Tutte le schede riportano il livello 20, tranne quella del Centro ricerche: ha i livelli da 1 a 10, perciò la sua scheda riporta il livello 10, il massimo.

![La vista Elenco al livello 20: le schede di Nucleo, Solare, Fattoria crediti, Fattoria Thulium, Collettore Velkonite, Collettore Orvium, Magazzino risorse, Fucina e Centro ricerche](../../img/skylab/wiki/modules.jpg)

## I primi quattro moduli {#the-first-four-modules}

### Modulo Nucleo {#core-module}

Il cuore del tuo Skylab. Il livello del Nucleo decide il livello massimo di ogni altro modulo: non puoi potenziare nessun modulo oltre il tuo Nucleo. Il Nucleo arriva fino al livello 20, e dal **livello 5** sblocca la filiera descritta più sotto. I suoi potenziamenti costano solo crediti: 112.326 in tutto fino al livello 10 e 6.647.504 fino al livello 20, e richiedono circa 16 giorni e mezzo in tutto (vedi [Tempi di potenziamento](#upgrade-times)).

### Modulo Solare {#solar-module}

L’energia è la linfa vitale dello Skylab. Il modulo Solare produce l’energia che usano tutti gli altri moduli.

- **Importanza**: se l’energia che usi supera quella che produci, le tue fattorie e i tuoi collettori si spengono.
- **Energia prodotta**: un modulo Solare al livello N ne produce a sufficienza per **ogni altro modulo al livello N**, e circa un decimo in più: 255 al livello 1, 835 al livello 7, 16.110 al livello 20. Solare al livello 7 alimenta un’intera stazione al livello 7 (vedi Gestione dell’energia per ogni livello).
- **Prezzo**: costruire Solare costa **500 crediti e 50 Thulium**. I suoi potenziamenti costano come quelli della Fucina e durano quanto loro: da 8.000 crediti e 25 Thulium per il livello 2 (5 minuti) a 9.000.000 di crediti e 10.000 Thulium per il livello 20 (24 ore).
- **Potenziamento**: mentre si potenzia, Solare produce solo il **25%** dell’energia del livello attuale, e quella del nuovo livello dal momento in cui il potenziamento termina. Una stazione che usa più di così si ferma: ogni fattoria e ogni collettore smettono di produrre e la Fucina non avvia nuovi lotti finché il potenziamento non è finito. Per quasi ogni stazione è così: resta in funzione durante il potenziamento solo se tutti gli altri moduli sono almeno cinque livelli sotto Solare (sei livelli dal livello 10 di Solare). Pianifica un potenziamento di Solare come un blackout delle tue fattorie (vedi Costruzione e potenziamento).

### Fattoria crediti e Fattoria Thulium {#credit-farm-and-thulium-farm}

- **Fattoria crediti**: produce crediti nel tempo: **500 all’ora al livello 1, 50.000 al livello 20** (livello 5: 2.500; livello 10: 7.500; livello 15: 17.000). Costruirla non costa nulla.
- **Fattoria Thulium**: produce Thulium nel tempo: **50 all’ora al livello 1, 1.600 al livello 20** (livello 5: 180; livello 10: 450; livello 15: 950). Costruirla costa 5.000 crediti e 500 Thulium.
- Entrambe richiedono energia, e ciascuna conserva 72 ore della sua produzione finché non la raccogli.

## La filiera {#the-supply-chain}

Quattro moduli trasformano il tempo passato lontano dalla tastiera nelle piastre per i tuoi laser migliori. Il minerale arriva **solo** dai collettori (tutti i materiali e le valute sono nella pagina [Risorse](/wiki/06-Items/Resources.md)): gli alieni non lo rilasciano e il Negozio non lo vende.

1. Un **collettore** estrae minerale, una certa quantità all’ora, nella propria tramoggia (pari a 72 ore di produzione).
2. **Raccogli** sposta il minerale dalla tramoggia al **Magazzino risorse**, la riserva in cui ogni minerale è tenuto separato.
3. La **Fucina** preleva dalla riserva il minerale che le serve quando parte un lotto, e produce piastre, 10 secondi a piastra, un lotto alla volta.
4. **Ritira piastre** sposta le piastre finite nel tuo inventario (la tua nave deve essere atterrata). L’[Assemblaggio](/wiki/06-Items/Lasers.md) le trasforma in un Quantum Laser 3, una Starfire-3 o un Helios Beam e, una di ciascun tipo con 5 Dark Matter, in una Dark Matter Plate, che chiedono [la Forgia](/wiki/06-Items/Forge.md) e l’ultimo tier di ogni catena di potenziamento.

### Collettore Velkonite e Collettore Orvium {#velkonite-collector-and-orvium-collector}

- **Minerale**: al livello 1 il Collettore Velkonite estrae **10 Velkonite all’ora** e il Collettore Orvium **10 Orvium all’ora**, e ogni livello ha il suo ritmo: fino a 80 Velkonite e 40 Orvium all’ora al livello 20 (livello 5: 18 e 14 all’ora; livello 10: 32 e 24).
- **Tramoggia**: ciascuno contiene 72 ore del suo minerale e smette di estrarre quando è pieno.
- **Raccogli**: sposta il minerale nel Magazzino risorse, finché c’è posto. Se il magazzino non è costruito, o la riserva di quel minerale è piena, non c’è dove metterlo e il pulsante spiega perché. Il resto rimane nella tramoggia.
- **Energia**: 20 (Velkonite) e 30 (Orvium) al livello 1, con un aumento del 15% per livello.

### Magazzino risorse {#resource-storage}

- **Riserva**: tiene separati Velkonite e Orvium e ne contiene una quantità diversa per ciascuno: **240 di ciascuno al livello 1**, fino a 7.680 di Velkonite e 3.840 di Orvium al livello 20 (livello 5: 720 e 560; livello 10: 1.920 e 1.440).
- **Limite**: un giorno di produzione del suo collettore al livello 1, fino a quattro giorni al livello 20. La tramoggia di un collettore contiene tre giorni, quindi dal livello 13 la riserva contiene almeno una tramoggia piena.
- **Oltre il limite**: se una riserva contiene più del suo limite (il pagamento dell’aggiornamento 0.4.10 può averla lasciata così), non viene tolto nulla, ma Raccogli non aggiunge altro di quel minerale finché non ne hai usato un po’.
- Il minerale entra solo raccogliendolo da un collettore, ed esce solo verso la Fucina. Non entra mai nel tuo inventario.
- **Il minerale immagazzinato resta** dopo il reset della stagione.
- **Energia**: 10 al livello 1, con un aumento del 10% per livello. Non si può spegnere.

### Fucina {#forgery}

- **Piastre**: la Fucina produce una **Velkonite Reinforced Plate** dalla Velkonite e una **Orvium Reinforced Plate** dall’Orvium: **40 Velkonite** o **80 Orvium** a piastra al livello 1, in calo a ogni livello fino a 30 e 60 al livello 20 (mai sotto il 75%).
- **Lotti**: un lotto di un solo tipo di piastra alla volta, **10 piastre al livello 1** e 5 in più per ogni livello successivo. Il minerale esce dal Magazzino risorse nel momento in cui parte il lotto, e ogni piastra richiede **10 secondi**. Le piastre vengono prodotte una dopo l’altra, anche mentre sei via.
- **Ritira piastre**: sposta le piastre finite nel tuo inventario mentre la tua **nave è atterrata**, e il resto del lotto continua. Un nuovo lotto può partire quando la Fucina è vuota.
- Un lotto in corso si completa anche se spegni la Fucina o la potenzi. Un lotto **nuovo** richiede che la Fucina sia accesa, non in potenziamento, e che l’energia dello Skylab sia in equilibrio.
- **Energia**: 30 al livello 1, con un aumento del 15% per livello.
- **Non vendibile**: le piastre che produce la Fucina non si possono vendere all’[Asta](/wiki/03-Mechanics/Auction.md#marketable-items), altrimenti sarebbero la merce più grande del suo Mercato. Restano materiale per l’Assemblaggio e la Forgia.

### Costruirli {#building-them}

I due collettori costano **10 Ship Fragment, 20.000 crediti e 500 Thulium** ciascuno, il Magazzino risorse **10 Ship Fragment, 5.000 crediti e 250 Thulium** e la Fucina **10 Ship Fragment, 5.000 crediti e 500 Thulium**; tutti e quattro richiedono il Nucleo al livello 5.

- Gli Ship Fragment vengono presi dal tuo inventario (non dal Deposito di trasporto) e la tua nave deve essere atterrata. Il pannello di costruzione mostra ciò che hai rispetto a ciò che serve, e ciò che ti manca.
- Consumano energia. Prima di costruire, il pannello mostra il tuo bilancio energetico attuale e quello dopo la costruzione: **costruire può mandare in deficit una stazione** quando il suo Solare è indietro rispetto agli altri moduli, e un solo deficit ferma ogni fattoria e collettore. Spegni un modulo, oppure potenzia prima Solare.
- I due collettori sono sospesi su strutture sopra la stazione, il Magazzino risorse si trova alla porta nord-est del Nucleo e la Fucina alla sua porta nord-ovest.

## Il Centro ricerche {#the-research-centre}

Il nono modulo trasforma le risorse in scienza e ricerca le tecnologie di cui l’Assemblaggio ha bisogno prima di creare qualcosa di nuovo. Si costruisce dal livello 10 del Nucleo, ha i livelli da 1 a 10, consuma energia e non si può spegnere. I suoi numeri, ciò che brucia come carburante, il boost e l’intero albero delle tecnologie sono nella pagina [Ricerca](/wiki/03-Mechanics/Research.md). Le tecnologie più alte richiedono anche Dark Matter, che aggiungi al Centro: [Dark Matter e Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md) spiega come ottenerla.

## Meccaniche {#mechanics}

### Costruzione e potenziamento {#building-and-upgrading}

- **Costruzione**: ogni modulo si costruisce a sé. Un modulo è al livello 1 nel momento in cui viene costruito, e potenziarlo ne aumenta la produzione (o l’energia prodotta) e la capienza, ma anche il consumo di energia.
- **Tempo e costo**: i potenziamenti costano crediti e Thulium e richiedono tempo, e ogni modulo ha per ogni livello il proprio prezzo e il proprio tempo (passa il puntatore su **Potenzia** per vedere il successivo; i totali sono più sotto). Il prezzo si paga all’avvio del potenziamento. Il costo non dipende dal tempo.
- **Timer**: un potenziamento segue l’orologio del server, quindi si completa mentre sei via, anche giorni dopo se serve. Avvialo, disconnettiti, torna: il modulo è al nuovo livello quando apri la pagina Skylab.
- **Tempi di potenziamento**: i primi livelli sono rapidi e gli ultimi richiedono fino a 36 ore, quelli del Nucleo fino a 6 giorni (vedi le tabelle più sotto). Ogni modulo ha il proprio timer, quindi puoi potenziarne diversi contemporaneamente.
- **Pausa della produzione**: mentre un modulo è in potenziamento è offline: non produce nulla e non usa energia. Solare fa eccezione: continua a produrre un quarto della sua energia (vedi sotto).
- **Solare produce solo il 25% della sua energia mentre si potenzia**: Solare produce tutta l’energia dello Skylab e, mentre si potenzia (24 ore per l’ultimo livello), produce un quarto dell’energia del livello **attuale**; quella del nuovo livello subentra nel momento in cui il potenziamento termina. Una stazione completa usa circa il 90% di ciò che Solare produce al proprio livello, quindi un quarto di quella energia regge solo una stazione da cinque a sei livelli sotto Solare. Altrimenti ogni fattoria e ogni collettore si fermano per tutto il potenziamento, ciò che hai immagazzinato resta e si può raccogliere, e la Fucina non avvia nuovi lotti. Un modulo in potenziamento o spento non usa energia, quindi potenziare le fattorie insieme a Solare non costa niente in più, e spegnere dei moduli lascia spazio agli altri; la Fattoria Thulium è di gran lunga la più energivora.

### Quanto costa {#what-it-costs}

Il prezzo dell’intera salita, la costruzione più ogni potenziamento, fino al livello 10 e fino al livello 20. Il Nucleo c’è sempre e i suoi passi costano solo crediti; il Centro ricerche ha i livelli da 1 a 10 e i suoi numeri sono nella pagina [Ricerca](/wiki/03-Mechanics/Research.md).

| Modulo | Crediti fino al livello 10 | Thulium fino al livello 10 | Crediti fino al livello 20 | Thulium fino al livello 20 |
| :--- | ---: | ---: | ---: | ---: |
| Nucleo | 112.326 | 0 | 6.647.504 | 0 |
| Solare | 1.219.500 | 1.600 | 35.039.500 | 36.850 |
| Fattoria crediti | 840.000 | 109 | 26.240.000 | 2.399 |
| Fattoria Thulium | 1.154.000 | 4.190 | 32.254.000 | 67.890 |
| Collettore Velkonite | 696.000 | 6.950 | 20.996.000 | 78.950 |
| Collettore Orvium | 696.000 | 6.950 | 20.996.000 | 78.950 |
| Magazzino risorse | 619.500 | 359 | 18.169.500 | 2.649 |
| Fucina | 1.224.000 | 2.050 | 35.044.000 | 37.300 |

I primi passi costano poco e gli ultimi molto: il passo della Fattoria crediti dal livello 1 al 2 costa 5.000 crediti e 1 Thulium, quello dal 19 al 20 costa 7.000.000 di crediti e 550 Thulium. Quelli della Fattoria Thulium costano 7.000 crediti e 45 Thulium, poi 8.500.000 crediti e 16.000 Thulium. I potenziamenti di Solare costano a ogni livello come quelli della Fucina, e i due collettori costano uguale.

### Tempi di potenziamento {#upgrade-times}

<!-- upgrade-times:start -->
<!-- Generated from server/Resources/SkylabConfig.json by the test skylab::duration_tests::the_wiki_page_is_the_config (run it with SKYLAB_WIKI_WRITE=1 to rewrite this part). -->

**Tempi di potenziamento**, per modulo (il potenziamento dal livello indicato nella prima colonna):

| Livello | Nucleo | Solare | Fattoria crediti | Fattoria Thulium | Magazzino risorse | Collettore Velkonite | Collettore Orvium | Fucina | Centro ricerche |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| da 1 a 2 | 72 s | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 78 s |
| da 2 a 3 | 86 s | 15 min | 10 min | 15 min | 10 min | 15 min | 15 min | 15 min | 101 s |
| da 3 a 4 | 104 s | 30 min | 15 min | 30 min | 15 min | 20 min | 20 min | 30 min | 132 s |
| da 4 a 5 | 124 s | 45 min | 20 min | 45 min | 20 min | 30 min | 30 min | 45 min | 171 s |
| da 5 a 6 | 149 s | 1 h | 30 min | 1 h | 30 min | 45 min | 45 min | 1 h | 223 s |
| da 6 a 7 | 20 min | 1 h 15 min | 45 min | 1 h 30 min | 45 min | 50 min | 50 min | 1 h 15 min | 20 min |
| da 7 a 8 | 30 min | 1 h 30 min | 1 h | 2 h | 1 h | 1 h | 1 h | 1 h 30 min | 30 min |
| da 8 a 9 | 50 min | 2 h | 1 h 20 min | 3 h | 1 h 20 min | 1 h 15 min | 1 h 15 min | 2 h | 50 min |
| da 9 a 10 | 1 h 20 min | 3 h | 1 h 40 min | 4 h | 1 h 40 min | 1 h 30 min | 1 h 30 min | 3 h | 1 h 20 min |
| da 10 a 11 | 2 h 15 min | 4 h | 2 h | 5 h | 2 h | 2 h | 2 h | 4 h | – |
| da 11 a 12 | 3 h 30 min | 5 h | 2 h 30 min | 6 h | 2 h 30 min | 3 h | 3 h | 5 h | – |
| da 12 a 13 | 5 h 30 min | 6 h | 3 h | 8 h | 3 h | 4 h | 4 h | 6 h | – |
| da 13 a 14 | 9 h | 8 h | 3 h 30 min | 10 h | 3 h 30 min | 6 h | 6 h | 8 h | – |
| da 14 a 15 | 14 h | 10 h | 4 h | 11 h | 4 h | 8 h | 8 h | 10 h | – |
| da 15 a 16 | 1 g | 12 h | 5 h | 12 h | 5 h | 10 h | 10 h | 12 h | – |
| da 16 a 17 | 1 g 12 h | 16 h | 6 h | 14 h | 6 h | 12 h | 12 h | 16 h | – |
| da 17 a 18 | 2 g 12 h | 18 h | 8 h | 18 h | 8 h | 16 h | 18 h | 18 h | – |
| da 18 a 19 | 4 g | 20 h | 10 h | 1 g | 10 h | 20 h | 1 g | 20 h | – |
| da 19 a 20 | 6 g | 1 g | 12 h | 1 g 12 h | 12 h | 1 g | 1 g 12 h | 1 g | – |
| **Totale** | 16 g 13 h | 5 g 13 h | 2 g 14 h | 6 g 13 h | 2 g 14 h | 4 g 16 h | 5 g 10 h | 5 g 13 h | 3 h 12 min |
<!-- upgrade-times:end -->

Un potenziamento già in corso quando i tempi cambiano mantiene l’orario di fine che gli era stato assegnato. Il solo Nucleo richiede circa **16 giorni e mezzo** di potenziamenti consecutivi per passare dal livello 1 al livello 20. Nessun modulo supera il livello del Nucleo, quindi l’ultimo passo di ogni altro modulo (da 12 a 36 ore) può partire solo quando il Nucleo è al livello 20: tenendo sempre occupato ogni timer, e con i crediti e il Thulium a disposizione, l’intera stazione richiede circa **18 giorni**.

### Gestione dell’energia {#power-management}

Il tuo Skylab ha una disponibilità di energia limitata.

- **Bilancio**: mantieni la produzione di Solare al di sopra dell’energia usata da tutti gli altri moduli. La pagina Skylab mostra il bilancio, e ti avvisa prima che una costruzione lo porti sotto zero.
- **Solare tiene il passo**: un modulo Solare al livello N produce l’energia di **tutti gli altri moduli al livello N** (il Nucleo, entrambe le fattorie, il Magazzino risorse, entrambi i collettori e la Fucina, e dal livello 10 il Centro ricerche) e circa un decimo in più, quindi una stazione i cui moduli sono tutti al livello 7 ha bisogno di Solare 7, e ne è coperta. Solare un livello più basso non basta per una stazione al completo (l’ultima colonna), quindi Solare deve comunque seguire gli altri nella salita. Il Nucleo consuma poco, quindi può andare avanti: Solare 5 e oltre copre una stazione al completo al suo livello con il Nucleo a qualsiasi livello.
- **Stato attivo**: puoi accendere o spegnere le fattorie, i collettori e la Fucina per gestire l’energia. Il Nucleo, Solare, il Magazzino risorse e il Centro ricerche funzionano sempre.
- **Blackout**: se l’energia usata supera quella prodotta, tutte le fattorie e i collettori smettono di produrre finché il bilancio non si ristabilisce. Ciò che hanno già immagazzinato resta, e puoi comunque raccoglierlo. La Fucina non avvia nuovi lotti e il Centro ricerche non avvia nuove ricerche (una ricerca già in corso prosegue).
- **Potenziamento di Solare**: mentre si potenzia, Solare produce solo un quarto della sua energia, quindi, se gli altri moduli non sono molto più in basso, la stazione va in deficit e le fattorie e i collettori si fermano finché il potenziamento non è finito (vedi [Modulo Solare](#solar-module)).

L’energia di Solare a ogni livello, a confronto con quella usata dagli altri moduli allo stesso livello (ogni modulo a quel livello, Nucleo compreso, e il Centro ricerche dal livello 10):

<!-- skylab-power:start -->
<!-- Generated from server/Resources/SkylabConfig.json by docs/design/skylab-power-model.py --doc (--check fails while this part is behind). -->

| Livello | Solare produce | Gli altri sette moduli usano | Avanzo | Con Solare un livello più basso |
| :--- | ---: | ---: | ---: | :--- |
| 1 | 255 | 230 | 25 | – |
| 2 | 310 | 278 | 32 | 255: mancano 23 |
| 3 | 375 | 337 | 38 | 310: mancano 27 |
| 4 | 455 | 410 | 45 | 375: mancano 35 |
| 5 | 555 | 501 | 54 | 455: mancano 46 |
| 6 | 680 | 615 | 65 | 555: mancano 60 |
| 7 | 835 | 756 | 79 | 680: mancano 76 |
| 8 | 1.030 | 933 | 97 | 835: mancano 98 |
| 9 | 1.275 | 1.155 | 120 | 1.030: mancano 125 |
| 10 | 1.680 | 1.523 | 157 | 1.275: mancano 248 |
| 11 | 2.065 | 1.876 | 189 | 1.680: mancano 196 |
| 12 | 2.555 | 2.322 | 233 | 2.065: mancano 257 |
| 13 | 3.180 | 2.888 | 292 | 2.555: mancano 333 |
| 14 | 3.970 | 3.607 | 363 | 3.180: mancano 427 |
| 15 | 4.975 | 4.522 | 453 | 3.970: mancano 552 |
| 16 | 6.260 | 5.688 | 572 | 4.975: mancano 713 |
| 17 | 7.895 | 7.176 | 719 | 6.260: mancano 916 |
| 18 | 9.990 | 9.080 | 910 | 7.895: mancano 1.185 |
| 19 | 12.670 | 11.517 | 1.153 | 9.990: mancano 1.527 |
| 20 | 16.110 | 14.642 | 1.468 | 12.670: mancano 1.972 |
<!-- skylab-power:end -->

La tabella conta ogni modulo allo stesso livello. La Fattoria Thulium consuma quattro quinti di quel totale al vertice (11.695 al livello 20, contro 14.642 per tutti e otto), quindi una stazione con quella fattoria molto più avanti del resto ha bisogno di più Solare di quanto suggerisca il suo Nucleo.

### Raccolta {#collecting}

Ogni fattoria e collettore ha una tramoggia per circa 72 ore della sua produzione. La raccolta è manuale.

- **Capienza**: quando una tramoggia è piena, la produzione si ferma finché non raccogli.
- **Fattorie**: i crediti e il Thulium raccolti vanno direttamente sul tuo account.
- **Collettori**: il minerale va nel Magazzino risorse, finché c’è posto.
- **Fucina**: le piastre vanno nel tuo inventario, quando la tua nave è atterrata.
- **Raccogli tutto** prende tutto in una volta, compresi i moduli spenti e quelli in potenziamento.
- Un badge **(!)** segnala una tramoggia piena che puoi svuotare e le piastre in attesa nella Fucina, nella pagina Skylab e sulla riga Skylab della barra laterale.

### Il reset {#the-wipe}

Lo Skylab non viene mai azzerato: i moduli mantengono i loro livelli, il Magazzino risorse conserva il suo minerale e il Centro ricerche conserva le sue tecnologie, il suo serbatoio di scienza, la Dark Matter che contiene e una ricerca in corso. Le piastre nel tuo inventario sono oggetti come gli altri, quindi seguono le [regole del reset](/wiki/03-Mechanics/Wipe-Timeline.md).

## Pianificare il tuo Skylab {#planning-your-skylab}

Lo Skylab ci mette settimane a crescere, quindi un po’ di pianificazione ripaga. I numeri sono quelli delle tabelle qui sopra.

### Cosa potenziare per primo {#what-to-upgrade-first}

1. **Solare, poi la Fattoria crediti.** Solare costa 500 crediti e 50 Thulium e senza non funziona niente; la Fattoria crediti non costa nulla. Le dieci [missioni Stazione](/wiki/03-Mechanics/Quests.md#station-missions) ti guidano in questi primi passi e ti pagano 52.000 crediti e 610 Thulium, come base: il tuo mondo, i tuoi booster e i bonus del tuo clan la moltiplicano.
2. **Poi la Fattoria Thulium: è la tua principale fonte di Thulium.** Al livello 10 produce 450 Thulium all’ora, 10.800 al giorno, quanto pagano 54 uccisioni di un [Crystalys](/wiki/04-Aliens/Crystalys.md) in Alpha (200 ciascuna). La salita fino al livello 10 costa 1.154.000 crediti e 4.190 Thulium, costruzione compresa. Al livello 15 la fattoria produce 22.800 al giorno e al livello 20 38.400. La sua tramoggia contiene 72 ore, quindi torna almeno ogni tre giorni. Cosa si compra con il Thulium è nella pagina [Risorse](/wiki/06-Items/Resources.md#thulium).
3. **La Fattoria crediti è l’entrata costante di contorno.** Al livello 10 produce 7.500 crediti all’ora, 180.000 al giorno, per 840.000 crediti e 109 Thulium. I livelli alti si ripagano lentamente: il passo dal livello 9 al 10 costa 300.000 crediti per 1.000 in più all’ora, cioè 300 ore. Potenziala quando ti avanzano crediti.
4. **Tieni occupato il Nucleo.** Niente supera il Nucleo, e il Nucleo da solo richiede circa 16 giorni e mezzo per arrivare al livello 20. Non c’è una coda, quindi avvia il suo passo successivo ogni volta che torni.
5. **Costruisci la filiera come un insieme.** I collettori, il Magazzino risorse e la Fucina si aprono al livello 5 del Nucleo. Un collettore può mettere in riserva il minerale solo in un Magazzino risorse, e la riserva contiene un giorno di produzione del suo collettore al livello 1 e quattro giorni al livello 20, quindi potenzia il Magazzino insieme ai collettori, altrimenti il minerale aspetta nelle loro tramogge.

### Pianificare un potenziamento di Solare {#timing-a-solar-upgrade}

Mentre si potenzia, Solare produce un quarto della sua energia, e una stazione quasi sempre ne usa di più. Le fattorie e i collettori si fermano allora per tutto il potenziamento: ciò che contengono resta, ma ciò che avrebbero prodotto è perso. La tabella indica, per ogni passo di Solare, il suo tempo, la stazione più grande che continua a funzionare (ogni modulo allo stesso livello, Nucleo e filiera compresi; una stazione più piccola regge un po’ di più) e ciò che una Fattoria crediti e una Fattoria Thulium di quel livello avrebbero prodotto in quel tempo. Per esempio, Solare dal livello 10 all’11 richiede 4 ore, e fattorie di livello 10 ne avrebbero prodotto 30.000 crediti e 1.800 Thulium.

| Potenziamento di Solare | Tempo | Stazione che continua a funzionare, fino al livello | La Fattoria crediti produce nel frattempo | La Fattoria Thulium produce nel frattempo |
| :--- | ---: | ---: | ---: | ---: |
| da 1 a 2 | 5 min | nessuna | 42 | 4 |
| da 2 a 3 | 15 min | nessuna | 250 | 20 |
| da 3 a 4 | 30 min | nessuna | 750 | 55 |
| da 4 a 5 | 45 min | nessuna | 1.500 | 105 |
| da 5 a 6 | 1 h | nessuna | 2.500 | 180 |
| da 6 a 7 | 1 h 15 min | nessuna | 4.375 | 288 |
| da 7 a 8 | 1 h 30 min | nessuna | 6.750 | 420 |
| da 8 a 9 | 2 h | 1 | 11.000 | 660 |
| da 9 a 10 | 3 h | 2 | 19.500 | 1.140 |
| da 10 a 11 | 4 h | 4 | 30.000 | 1.800 |
| da 11 a 12 | 5 h | 5 | 45.000 | 2.750 |
| da 12 a 13 | 6 h | 6 | 66.000 | 3.900 |
| da 13 a 14 | 8 h | 7 | 104.000 | 6.000 |
| da 14 a 15 | 10 h | 8 | 150.000 | 8.500 |
| da 15 a 16 | 12 h | 9 | 204.000 | 11.400 |
| da 16 a 17 | 16 h | 10 | 320.000 | 17.600 |
| da 17 a 18 | 18 h | 11 | 432.000 | 22.500 |
| da 18 a 19 | 20 h | 12 | 580.000 | 28.000 |
| da 19 a 20 | 1 g | 13 | 840.000 | 36.000 |

- **Potenzia le fattorie insieme a Solare.** Un modulo in potenziamento non produce nulla e non usa energia comunque, quindi il tempo che una fattoria passa in potenziamento durante la pausa non costa niente in più.
- **Tieni bassi gli altri moduli se non puoi permetterti una pausa.** Una stazione resta in funzione durante un potenziamento di Solare solo se tutti i suoi altri moduli sono almeno cinque livelli sotto Solare (sei dal livello 10 di Solare), e una stazione completa richiede un po’ di più, come mostra la tabella.
- **Spegni ciò di cui puoi fare a meno.** Un modulo spento non usa energia, quindi spegnere la Fattoria Thulium, la più energivora (80 al livello 1, con il 30% in più a ogni livello), lascia spazio agli altri.
