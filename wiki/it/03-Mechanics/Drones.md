<!-- wiki-i18n source: e65164e763773d17 -->
<!-- wiki-i18n title: Droni -->
# Meccaniche dei droni {#drone-mechanics}

I droni sono unità di supporto autonome che volano accanto alla tua nave. Forniscono slot di equipaggiamento aggiuntivi e contribuiscono direttamente alle prestazioni di combattimento della tua nave. Uno Slave Drone cresce anche: guadagna esperienza ogni volta che distruggi un alieno e sale attraverso **otto livelli**, da una piccola sfera corazzata a una cannoniera dalle ali a mezzaluna. In Assemblaggio uno Slave Drone può essere potenziato a **Master Drone**, che ricomincia i suoi livelli (vedi Master Drone più sotto). I droni ti permettono anche di indossare una **formazione di droni**: funziona solo se hai almeno un drone nella tua flotta (vedi [Formazioni di droni](/wiki/03-Mechanics/Formations.md)).

![Emergency Repair: repair drones beam the hull](../../img/wiki-img/shots/emergency-repair.jpg)

## Ottenere droni {#getting-drones}

Ogni drone che possiedi, uno **Slave Drone** o un Master Drone, apre i suoi slot per droni (uno per uno Slave Drone, due per un Master Drone), fino a **8** droni. Il Negozio vende gli Slave Drone in cambio di crediti, e dal quarto in poi anche di Thulium. Ognuno costa più del precedente: i prezzi sono in [Droni](/wiki/06-Items/Drones.md).

## Disposizione di volo e movimento {#formation-movement}

I droni volano in una disposizione standard **“Gregario” (2-2-4)**:

- **2 droni** accanto alla nave, uno per fianco.
- **2 droni** accanto e appena dietro di essa.
- **4 droni** in coda, dietro.

Usano un algoritmo di inseguimento fluido che regola la loro posizione in base alla velocità e alla rotazione della tua nave, stringendo la disposizione durante le manovre brusche. Nessuno vola davanti a te.

I droni sono piccoli e restano vicini: un drone di livello 8 misura circa 19,5 unità di larghezza (una Protos 50) e un drone di livello 1 è una palla di circa 8, quindi l’intera disposizione sta entro circa 135 unità dalla tua nave. Il drone che hai comprato per primo ha più esperienza e vola sul tuo fianco sinistro, il secondo sul destro, e i più recenti seguono dietro.

Questa disposizione è solo l’aspetto dei droni, ed è la stessa qualunque [formazione di droni](/wiki/03-Mechanics/Formations.md) tu indossi. Una formazione di droni è un insieme di bonus e costi, non un altro modo di volare.

## Equipaggiamento e statistiche {#equipment-stats}

I droni funzionano come supporti di equipaggiamento che ampliano la tua nave.

- Uno Slave Drone ha **1 slot** e un Master Drone **2**, fino a **8 droni**.
- In questi slot puoi equipaggiare **laser** e **scudi**, in entrambi gli slot di un Master Drone. Nient’altro ci sta: niente motori, niente Nuclei adattivi.
- **I laser contano per intero.** Un laser su un drone spara quando spari tu, aggiunge il suo danno alla tua raffica e usa munizioni come qualsiasi altro laser (ogni laser brucia un’unità di munizioni a raffica). I due laser di un Master Drone sono due laser.
- **Anche gli scudi contano per intero.** Uno scudo su un drone conta come uno in uno slot principale, in entrambi gli slot: la sua capacità e la sua ricarica con le sue celle, il suo assorbimento nella media della tua nave, il suo bonus scudo e la sua penalità di velocità. Viene classificato insieme agli scudi della nave in base a ciò che conta dopo la quota dello slot (lo slot di un drone conta il 100%; i quattro migliori contano per intero, dal quinto in poi contano meno, vedi [Meccaniche degli scudi](/wiki/03-Mechanics/Shields.md)), e i bonus della Forgia, i bonus dell’Emporio e la penetrazione dello scudo di un attaccante agiscono su di esso come su qualsiasi scudo. Il livello del drone potenzia solo il suo laser, mai il suo scudo. Mentre un drone viene potenziato, i suoi slot sono offline, lo scudo come il laser. Prima dell’aggiornamento 0.4.7 uno scudo su un drone non aggiungeva nulla.
- **Un laser o uno scudo?** Uno slot ne ospita uno solo dei due: un laser aggiunge un laser alla tua raffica, uno scudo aggiunge i suoi punti scudo. Su una nave piccola con buoni scudi i punti in più aggiungono poco, perché lo scafo finisce prima; su uno scafo grande ti permettono di incassare molto di più.
- **Le formazioni richiedono un drone, non uno slot.** Una [formazione di droni](/wiki/03-Mechanics/Formations.md) funziona finché possiedi almeno un drone. Non occupa nessuno slot drone, e il numero di droni, i loro livelli e ciò che portano non la cambiano.

## Livelli {#levels}

Ogni Slave Drone parte dal livello 1 e guadagna esperienza (XP) ogni volta che distruggi un alieno. Anche un Master Drone parte dal livello 1, senza XP, e sale di livello allo stesso modo. Ogni livello richiede più del precedente, e con esso cambia l’aspetto, così vedi a che punto è arrivato un drone. La tabella indica, per ogni livello, gli XP necessari per salirvi dal livello precedente e a quanti abbattimenti di un solo tipo di alieno corrispondono (nel mondo Alpha: Beta ne richiede circa la metà, Gamma circa un terzo):

<!-- drones:begin -->
<!-- Generated from server/Resources/drone-levels.json by scripts/drones-wiki.sh: don't edit by hand. -->

- **Livello 1, Seme:** una piccola sfera corazzata con una lente ciano.
- **Livello 2, Alone:** la sfera in un anello fluttuante.
- **Livello 3, Disco:** un disco piatto sotto una cupola di vetro.
- **Livello 4, Disco volante:** un disco volante con piastre corazzate e prese d’aria.
- **Livello 5, Cannoniera:** una prua e due cannoni si aggiungono al disco volante.
- **Livello 6, Germogli alari:** cannoni e corte lame alari su piloni.
- **Livello 7, Mezze ali:** lame alari più lunghe con punte dorate.
- **Livello 8, Mezzaluna:** la cannoniera completa: ali a mezzaluna intere con strisce di luce ciano.

| Livello | XP per raggiungerlo | XP del livello | Danno laser | Abbattimenti di Seeker | Abbattimenti di Bulwark | Abbattimenti di Goombah |
| --: | --: | --: | --: | --: | --: | --: |
| 1 | 0 | – | – | – | – | – |
| 2 | 350 | 350 | – | 350 | 44 | 15 |
| 3 | 900 | 550 | +1% | 550 | 69 | 23 |
| 4 | 2.000 | 1.100 | +2% | 1.100 | 138 | 46 |
| 5 | 3.700 | 1.700 | +3% | 1.700 | 213 | 71 |
| 6 | 6.000 | 2.300 | +4% | 2.300 | 288 | 96 |
| 7 | 9.500 | 3.500 | +5% | 3.500 | 438 | 146 |
| 8 | 14.000 | 4.500 | +7% | 4.500 | 563 | 188 |

| Alieno | XP per ogni drone |
| :--- | --: |
| Seeker | 1 |
| Phantasm | 2 |
| Bulwark | 8 |
| Goombah | 24 |
| Crystalys | 72 |

<!-- drones:end -->

### Come i droni guadagnano XP {#how-drones-earn-xp}

- **Ogni drone che possiedi guadagna gli stessi XP** per ogni abbattimento di alieno che ti viene pagato: i primi 8 droni, che portino o no un laser. Un drone che compri più tardi parte dal livello 1 senza XP, quindi i tuoi primi droni sono sempre quelli di livello più alto.
- **Gli alieni più duri valgono di più.** Gli XP che dà un alieno sono nella seconda tabella qui sopra (un Crystalys vale 72 Seeker). Qualsiasi altro alieno ne dà 1.
- **I mondi pagano di più.** Beta raddoppia gli XP, Gamma li triplica (lì anche gli alieni hanno più punti scafo). Booster e Premium non li cambiano.
- **Contano gli abbattimenti che ti vengono pagati.** Un alieno che finisci mentre un altro pilota ne detiene la rivendicazione non paga nulla ai tuoi droni, proprio come non paga nulla a te. Gli abbattimenti di altri piloti, le missioni e gli abbattimenti dei piloti di corporazione non danno XP ai droni.
- **Il livello 8 è l’ultimo.** Gli XP continuano a contare anche dopo.

### Cosa dà un livello {#what-a-level-gives}

Il **laser montato nello slot di un drone** infligge più danno base man mano che il suo drone sale di livello: niente ai livelli 1 e 2, poi +1% al livello 3 fino a **+7% al livello 8**. Il bonus moltiplica il danno proprio di quel laser (dopo il suo incantamento); gli amp montati al suo interno si aggiungono sopra e non vengono moltiplicati. L’Hangar mostra il livello di ogni drone, la sua barra degli XP e gli abbattimenti che richiede il livello successivo, e le sue cifre di danno includono già il bonus. Quando un drone sale di livello, il Registro di gioco lo dice (“Il drone 2 ha raggiunto il livello 4.”) e il drone si illumina con un anello di luce.

### Quanto ci vuole {#how-long-it-takes}

La curva è tarata in modo che un drone nuovo raggiunga il livello 2 in circa un’ora di gioco normale (a caccia di Bulwark e Goombah) e il livello 8 in circa 27 ore di gioco. Quelle ore valgono per un pilota che compra il primo drone verso le missioni del livello 7; con un equipaggiamento più debole ci vuole di più (fino a circa 4 ore per il livello 2 e 150 ore per il livello 8). Dare la caccia a un solo tipo di alieno è al massimo circa il 50% più veloce di un mix normale. I droni restano dopo il reset della stagione con i loro livelli e la loro esperienza, quindi quelle ore si spendono una sola volta, nel numero di stagioni che servono: un pilota che gioca mezz’ora al giorno ci arriva in un paio di stagioni.

### Master Drone

Uno Slave Drone diventa un **Master Drone** quando lo potenzi in Assemblaggio, una volta ricercata la tecnologia del Master Drone ([Ricerca](/wiki/03-Mechanics/Research.md)). La ricetta costa 40.000 Thulium e 100 Ship Fragment e richiede 60 secondi, e non consuma un drone: **scegli tu quale Slave Drone è** (il selettore mostra livello e XP di ciascuno), e quello stesso drone, con il suo numero, il suo slot e tutto ciò che vi è montato, diventa un Master Drone quando il lavoro finisce, con un secondo slot vuoto. Niente va nel tuo inventario e non c’è nulla da ritirare: il Registro di gioco ti dice quando è finito, anche per un potenziamento terminato mentre eri via.

**Livello e XP tornano a 0 quando il potenziamento finisce.** Un Master Drone riparte dal livello 1, senza XP, e sale di livello come uno Slave Drone (la tabella qui sopra); il bonus laser del livello che aveva si perde. L’Assemblaggio lo dice prima che tu inizi, e ti chiede di confermare, indicando il drone, quando ha degli XP. La scelta predefinita è il drone con meno XP.

Mentre il potenziamento è in corso il drone è bloccato: non puoi potenziarlo di nuovo né eliminarlo, e il suo slot è **offline**, quindi il laser al suo interno non spara finché il lavoro non finisce (fino ad allora è ancora uno Slave Drone con un solo slot). Viene messo in coda dietro agli altri tuoi lavori, come qualsiasi creazione.

Un Master Drone è uno dei tuoi 8 droni: conta per il limite dei droni e per il prezzo del prossimo Slave Drone, quindi potenziare non cambia né l’uno né l’altro, e resta dopo il reset della stagione con il suo livello e i suoi XP. In volo è la cannoniera finita, in oro. Un Master Drone ha **due slot di equipaggiamento** dove uno Slave Drone ne ha uno: ognuno accetta un laser o uno scudo, e il bonus di livello si applica al laser in entrambi. Per il resto è uno Slave Drone: gli stessi otto livelli e lo stesso bonus laser. I Master Drone che hai creato prima che avessero il secondo slot ora ce l’hanno, con ciò che portavano rimasto al suo posto. I Master Drone creati prima che esistessero i potenziamenti sul posto sono normali oggetti nel tuo inventario e non volano.

## Comportamento in combattimento {#combat-behavior}

- **Laser**: i droni sparano con i loro laser equipaggiati contro il tuo bersaglio agganciato.
- **Danno**: i droni possono subire danni (se esiste una logica di entità distinta; attualmente condividono per lo più la riserva della nave ma sono visivamente distinti). _Nota: attualmente i droni sono estensioni indistruttibili della nave._
- **Repair Drone**: gli oggetti Repair Drone (da I a IV) sono [extra](/wiki/06-Items/Extras.md#repair-drones), non droni della tua flotta. Mentre uno ripara il tuo scafo, piccoli droni di riparazione escono dalla nave, le girano attorno e la colpiscono con i loro raggi, e i piloti vicini li vedono.
