<!-- wiki-i18n source: 50aa8bb9bc3f2a03 -->
<!-- wiki-i18n title: Estrazione di asteroidi -->
# Estrazione di asteroidi {#asteroid-mining}

Gli **asteroidi** sono grandi rocce che giacciono nel piano di volo dei settori delle corporazioni e dei settori pericolosi. Non si muovono mai e non sparano mai. Spezzane uno con i **razzi** o con i **laser** e si frantuma in piccoli **frammenti** di crediti, Thulium e minerale, che raccogli come un [carico](/wiki/03-Mechanics/Cargo.md). I razzi sono lo strumento per questo lavoro: anche i tuoi laser danneggiano un asteroide, ma solo al 5% di quello che fanno a una nave, e i droni non gli fanno nulla. Un’altra cosa spezza asteroidi per te: un P.E.T. **Mole** agganciato ([più sotto](#the-mole-pet)).

L’estrazione è un lavoro diverso dalla caccia, non un suo sostituto: non dà XP, onore né punti classifica, e i razzi che spari costano crediti o Thulium. Ti dà crediti e Thulium, minerale per la [Forgia](/wiki/06-Items/Forge.md) e per la fabbricazione senza combattere, e un lavoro che un [gruppo](/wiki/03-Mechanics/Groups.md) può condividere. Rende bene: secondo il modello del gioco stesso, un’ora sugli asteroidi giusti con il razzo giusto vale da 2,6 a 6,8 volte la migliore ora di caccia del tuo livello, una volta pagati i razzi. Non c’è un limite giornaliero: ogni frammento che raccogli paga per intero, perciò ciò che limita la tua giornata sono gli asteroidi che il settore contiene e la velocità con cui ricrescono.

![An asteroid of tier 5 selected: the Target window gives its tier, its hull, what it breaks into and the Cluster Chunks (P.E.T. parts) it can leave](../../img/wiki-img/shots/rock-target.jpg)

## Che cos’è un asteroide {#what-an-asteroid-is}

- **All’altezza delle navi.** Un asteroide giace nel piano di volo, dietro a ogni nave, razzo e frammento che gli passa sopra, e resta dov’è. È solido: la tua nave non può entrarvi, i colpi non lo attraversano e gli alieni lo aggirano (vedi il punto seguente e [Copertura](#cover)). Ogni asteroide è disegnato nelle sue proporzioni reali, così il Motherlode e il Prism Cluster svettano invece di apparire schiacciati. Le rocce scure lontane dietro la mappa sono scenografia: non puoi colpirle e non contengono nulla.
- **Solido.** Gli asteroidi sono solidi: spezzali o aggirali in volo. La tua nave non può entrare in nessuno. Se le ordini di andare in un punto oltre un asteroide, lo aggira alla sua velocità, dal lato in cui si trova il tuo ordine; se le ordini di andare in un punto dentro un asteroide, vola fin lì e si ferma sul bordo, dal tuo lato. Il centro della nave si ferma a un raggio della nave e 4 unità dal bordo dell’asteroide, quindi lo scafo come disegnato non lo tocca mai, e un varco tra due asteroidi lo attraversa solo una nave che ci sta. Una nave su cui è stato messo un asteroide ne esce volando per la via più breve e non subisce danni. Le casse e i frammenti non sono navi: ondeggiano dove sono.
- **Un tipo e una famiglia.** Ogni asteroide è uno dei tipi elencati in [I tipi](#the-kinds), e ogni tipo appartiene a una famiglia che dice com’è fatto. Il bagliore di un asteroide dice che cosa contiene. Un **anello singolo** a terra segna un asteroide normale, un **anello doppio** uno corazzato e un **anello tratteggiato** uno fragile.
- **Sulla minimappa.** Ogni asteroide del settore è un piccolo esagono del colore del suo tipo, vuoto finché non viene colpito e pieno dopo; i frammenti sono piccoli punti tondi.
- **La finestra bersaglio.** Clicca su un asteroide per selezionarlo. Il cerchio su un asteroide selezionato resta su di lui mentre ci voli intorno: un clic nello spazio vuoto, o subito accanto all’asteroide, fa solo volare la tua nave, e Esc o la croce nella finestra bersaglio lo lascia. La finestra mostra il suo nome, la famiglia e le dimensioni, lo scafo, i contrassegni **Corazza** ed **Esplosioni**, più o meno quanti razzi del tipo che hai in mano servono e più o meno quante raffiche dei tuoi laser, che cosa lascia nel tuo mondo e chi ha inflitto quanta parte dei danni. Selezionare un asteroide non cambia il bersaglio della tua nave o di un alieno, quindi i tuoi laser mantengono l’aggancio.

## Spezzarne uno {#breaking-one}

1. **Mira.** Clicca sull’asteroide per selezionarlo: un razzo guidato (Lancet, Ember) va allora verso di lui. Senza un asteroide selezionato, un razzo guidato va verso un asteroide sotto il cursore solo se non hai selezionato nemmeno una nave né un alieno, così un cacciatore che combatte accanto a un asteroide continua a sparare all’alieno (conta anche un po’ oltre il suo bordo, come il suo esagono sulla minimappa). Un razzo dritto (Rivet, Scatter) ignora l’asteroide selezionato: vola verso il cursore, come verso qualsiasi bersaglio, e con il cursore sull’asteroide (la sua immagine o il suo anello a terra, senza margine) vola verso il centro dell’asteroide. Un razzo che non ha un asteroide da raggiungere è un razzo normale, ma un asteroide sul suo cammino lo ferma comunque ([Copertura](#cover)).
2. **Spara.** Va bene uno qualsiasi dei dodici [razzi](/wiki/06-Items/Rockets.md#the-twelve-rockets) del Negozio, e anche il N.U.K.E. Un razzo guidato ha bisogno dell’asteroide entro la sua portata di aggancio, misurata fino al centro dell’asteroide, e vola verso il centro. Un razzo dritto non ha alcuna portata verso l’asteroide da controllare: vola verso il punto sotto il cursore e, come contro qualsiasi bersaglio, cade corto se quel punto è più lontano del suo volo. Con il cursore sull’asteroide va verso il centro, quindi non importa in quale punto dell’asteroide sia il cursore; con il cursore accanto all’asteroide va lì, e rompe l’asteroide solo se questo è sul suo cammino. Il [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) non può danneggiare un asteroide.
3. **Continua a sparare.** Tutti i razzi condividono un solo timer di ricarica, e ogni razzo costa quello che costa: il razzo è il prezzo del lavoro.

- **Un razzo guidato diretto contro un asteroide vola verso di esso.** Supera ogni nave sul cammino, e il primo altro asteroide che incontra lo prende al suo posto ([Copertura](#cover)). Un razzo dritto è un razzo normale: una nave sulla sua linea viene colpita per prima, e un asteroide sulla sua linea lo ferma. L’esplosione di un razzo ad area ferisce comunque ogni nave che raggiunge, come ovunque; gli altri asteroidi al suo interno non subiscono nulla.
- **I laser fanno poco, i droni nulla.** Seleziona l’asteroide, poi fai doppio clic su di esso, premi il tasto di attacco o uno slot delle munizioni: i tuoi laser gli sparano una volta al secondo finché il suo centro è entro la portata dei tuoi laser, e consumano munizioni come contro una nave. Un doppio clic spara sempre all’asteroide; il tasto di attacco e gli slot delle munizioni lo fanno quando non è selezionata alcuna nave né alcun alieno. Le munizioni Siphon drenano solo gli scudi, quindi non possono danneggiare un asteroide e quell’ordine viene rifiutato.
- **La tua nave si volta verso di esso.** Finché i tuoi laser sparano a un asteroide entro la loro portata, la tua nave si volta verso di esso, in qualunque direzione voli, come fa con un alieno che attacchi.
- **Danno.** Un razzo toglie dallo scafo dell’asteroide il suo tiro, e il bonus ai razzi della tua [formazione di droni](/wiki/03-Mechanics/Formations.md) conta come contro una nave (anche il +55% di Ballista); i tuoi laser, amplificatori, booster e munizioni non cambiano il tiro di un razzo. Una raffica di laser toglie il 5% di quello che farebbe a una nave senza scudo, con i tuoi amplificatori, booster, munizioni, colpi critici e formazione contati. Il bonus viene prima: un asteroide **corazzato** poi toglie da ogni colpo i punti della sua corazza, e un’esplosione ad area fa di più a uno **fragile** di cristallo (i numeri sono in Le regole e I tipi). Un asteroide non ha scudo e non guarisce mai: una roccia che hai intaccato resta intaccata finché qualcuno non la spezza.
- **Quanti.** Ogni tipo è fatto per un razzo, e I tipi dice più o meno quanti ne servono per spezzarlo; la finestra bersaglio e la scheda che compare al passaggio del mouse lo dicono per il razzo che hai in mano e, accanto, più o meno quante raffiche dei tuoi laser servono. Un mondo più forte significa uno scafo più grande (I mondi). Un tuo razzo in volo quando qualcun altro spezza l’asteroide continua come razzo normale e va perso.

## Copertura {#cover}

Un asteroide è una copertura. **Il primo asteroide sul cammino di un colpo prende il colpo.** Una raffica di laser, un razzo o l’esplosione di un razzo ad area, sparati contro un pilota, un alieno o un altro asteroide, vengono fermati dal primo asteroide sulla linea retta dal tiratore al suo bersaglio: il bersaglio non subisce nulla e l’asteroide prende il colpo. Così puoi nasconderti dietro un asteroide, dai piloti e dagli alieni. Un aggancio non è un colpo e non viene fermato: puoi agganciare un pilota dietro un asteroide, ma i tuoi laser colpiranno l’asteroide. Una [Energetic Wall](/wiki/06-Items/Extras.md#energetic-wall) ferma i colpi allo stesso modo, da entrambi i lati.

- **Da dentro.** Le navi non volano dentro gli asteroidi: vale solo per una nave su cui è stato messo un asteroide, finché ne esce volando. Il suo centro è dentro l’asteroide, e colpisce quell’asteroide a ogni colpo, ovunque miri.
- **Che cosa viene fermato.** Ogni raffica di laser e ogni razzo di un pilota, di un alieno (le navi degli sciami, i Clan Warden, gli Slumbering Void) e di un pilota di corporazione, il N.U.K.E. compreso. Due cose volano sopra gli asteroidi: il [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) e i cannoni del Dormant Swamp. Abilità come Venom e il buco nero non sono colpi.
- **Che cosa prende l’asteroide.** Un razzo toglie quello che toglie un razzo; una raffica di laser quello che i laser tolgono a un asteroide: il 5% di quello che farebbe a una nave, meno la corazza dell’asteroide. Conta come danno inflitto all’asteroide come ogni altro, così il pilota i cui colpi ne spezzano uno viene pagato per essi ([Chi riceve i frammenti](#who-gets-the-chunks)). Un alieno non spara mai a un asteroide, e un razzo di alieno che un asteroide ferma non gli toglie nulla: non c’è nessuno da pagare. L’unica eccezione è l’Inert Mass del [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md): la sua Dormant Lance danneggia l’asteroide che incontra con il proprio danno, e nessuno viene pagato per questo.
- **La linea.** Un asteroide è il cerchio che lo racchiude appena, così com’è disegnato, e un razzo lo tocca qualche unità prima del suo bordo, come tocca una nave. Un bersaglio dietro un asteroide, o con il centro dentro uno, è coperto; uno esattamente sul suo bordo no. Un asteroide accanto alla linea, dietro il bersaglio o dietro il tiratore non è di intralcio.
- **Speso come sempre.** Un colpo che un asteroide ferma costa le sue munizioni, il suo razzo e il suo timer, come ogni colpo.
- **Gli alieni aggirano.** Un alieno non vola mai dentro un asteroide: lo aggira, qualunque cosa stia facendo, e un alieno su cui è stato messo un asteroide ne esce volando. Se ti nascondi dietro un asteroide, un alieno che ti dà la caccia non si ferma a sparare all’asteroide: lo aggira in volo fino a un punto da cui la sua linea verso di te è libera, e spara da lì. Tieni l’asteroide tra te e lui, e continuerà a girare. Anche il pilota di una compagnia fa lo stesso. La tua nave aggira l’asteroide come un alieno (vedi sopra).

## Che cosa lascia uno spezzato {#what-a-break-leaves}

Nulla viene pagato quando un asteroide si spezza. Esplode in detriti e getta qualche **frammento**: piccole pepite dorate per i crediti, cristalli color lavanda per il Thulium e una pietra ruvida per il minerale. Escono alla deriva dai detriti e ondeggiano come qualsiasi [cassa](/wiki/03-Mechanics/Cargo.md): clicca su uno, la tua nave vola fin lì e la raccolta dura il suo breve canale, come per qualsiasi cassa ([raccolta](/wiki/03-Mechanics/Cargo.md#collecting)). Il minerale va nell’inventario dell’Hangar, i crediti e il Thulium sul tuo conto, e una notifica ti dice che cosa hai ottenuto.

Un asteroide più grande lascia più pezzi (la colonna Frammenti di denaro di I tipi: i crediti e il Thulium arrivano in altrettanti pezzi, e il minerale in uno in più). Dopo una raccolta la tua nave passa da sola al frammento successivo di un asteroide vicino che puoi prendere; qualsiasi tuo ordine di movimento la ferma.

Dal livello 2 delle rocce in su, una rottura può lasciare anche un **Cluster Chunk** intero, nel blocco di minerale del gruppo che ha inflitto più danni: un **Regular Cluster Chunk** dal livello 2, un **Mythical Cluster Chunk** dal livello 3 e un **Legendary Cluster Chunk** dal livello 4; la Motherlode li dà più spesso. Le probabilità sono in [Risorse](/wiki/06-Items/Resources.md#regular-cluster-chunk). La fortuna non le cambia, nemmeno quella di un P.E.T. Con una Orvium Reinforced Plate, un chunk diventa un [P.E.T.](/wiki/03-Mechanics/Pets.md) nella Culla dell’Hangar.

## Chi riceve i frammenti {#who-gets-the-chunks}

Un asteroide è un lavoro condiviso: qualsiasi numero di piloti può colpirlo, con razzi, con laser o con gli impulsi di un Mole, e i frammenti vanno in base al danno inflitto da ciascuno, non a chi spara per primo o per ultimo. La riga dei danni nella finestra bersaglio mostra chi ha inflitto quanto e che cosa era già stato inflitto prima del tuo arrivo. I crediti e il Thulium di una rottura vengono estratti una volta e divisi in base al danno; il minerale si divide tra i piloti che hanno inflitto più danno; i ritrovamenti rari vanno a chi ne ha inflitto di più. Un pilota che ha inflitto meno della quota indicata in Le regole non riceve nulla, e il Registro di gioco lo dice. I frammenti vengono posati per ogni pilota pagato e restano per un po’ riservati a lui e al suo clan, poi liberi per tutti.

## Il P.E.T. Mole {#the-mole-pet}

Un **Mole** agganciato (un tipo di [P.E.T.](/wiki/03-Mechanics/Pets.md#the-mole)) lavora per te mentre voli: ogni 3 secondi dà un impulso all’asteroide più vicino entro circa cinque lunghezze di nave e mezzo dalla tua nave, finché non si spezza, poi prende il successivo. I suoi impulsi entrano a tuo nome nel danno dell’asteroide, quindi una rottura ti paga come se l’avessi rotto con un razzo: i frammenti, i ritrovamenti, la probabilità di un Cluster Chunk e la tua missione degli asteroidi.

- **Quanto ne spezza.** Un Mole al massimo (un Legendary di livello 20) spezza almeno tanti asteroidi all’ora quanti ne spezza un pilota che spara loro il razzo migliore, Rivet III, e i gradi e i livelli più bassi ne spezzano meno ([la tabella](/wiki/03-Mechanics/Pets.md#how-strong)). Non usa munizioni né razzi. I tuoi laser, razzi, amplificatori, booster, formazione e il Danno dei tuoi P.E.T. non cambiano un impulso, e l’armatura rallenta un impulso come rallenta un razzo.
- **Quali asteroidi.** Il più vicino a portata che nessun altro asteroide né Energetic Wall copra. Va bene ogni asteroide che un razzo potrebbe colpire: anche la Motherlode e i relitti (Cache Pod, Scrap Hulk, Derelict Hulk, Derelict Cruiser), anche un asteroide che altri piloti hanno colpito, e i chunk vanno allora in base al danno, come sempre. I relitti che vedi vagare sullo sfondo sono solo scenario, non asteroidi. Non lavora in una zona sicura, occultato, mentre salti né mentre la tua nave è distrutta.
- **Nessun limite proprio.** Un Mole lavora ogni ora in cui voli, che tu tocchi i tasti o no (una nave inattiva è un bersaglio), e nessun limite giornaliero lo ferma, né proprio né del mondo. Resta ciò che limita tutti: gli asteroidi alla sua portata e la velocità con cui ricrescono. I suoi frammenti pagano per intero, come i tuoi.
- **Lavora solo uno.** Tra i Mole della tua Station lavora solo il più forte; gli altri danno solo boost.

## Le regole {#the-rules}

<!-- asteroids-rules:begin -->
<!-- Generated from server/Resources/Asteroids.json (and Rockets.json, Pets.json) by scripts/asteroids-wiki.sh: don't edit by hand. -->

- Un pilota che ha inflitto almeno 5% dei danni a un asteroide riceve una parte dei suoi frammenti, in proporzione ai danni inflitti. Se nessuno arriva a 5%, il pilota che ha inflitto di più li riceve tutti.
- Un [gruppo](/wiki/03-Mechanics/Groups.md#sharing-kills) conta come un solo pilota, e la sua parte è divisa per livello tra i compagni vicini che sparano.
- I frammenti di una rottura restano riservati per 30 s al pilota per cui sono stati posati e al suo clan. Dopo, chiunque sulla mappa può prenderli. Un frammento che nessuno prende sparisce dopo 3 min.
- Una mappa contiene al massimo 36 frammenti, entro il limite di 64 casse per mappa: i frammenti non scacciano mai le casse degli alieni, e queste non scacciano mai un frammento. Quando la mappa non ha posto per un frammento, il pilota a cui era destinato viene pagato subito.
- I crediti e il Thulium vengono pagati quando si raccoglie un frammento, non quando l’asteroide si spezza. Non c’è un limite giornaliero a ciò che ti può essere pagato: ogni frammento paga per intero i suoi crediti e il suo Thulium, indipendentemente da quanti ne raccogli in un giorno.
- La ricompensa è uguale per tutti: nessun bonus Premium, potenziamento dell’Emporio, potenziamento del clan, Loot Luck o booster cambia i crediti, il Thulium o i ritrovamenti. Il [Resource Magnet Booster](/wiki/06-Items/Boosters.md) aggiunge alle risorse di un frammento di minerale quando lo raccogli, come a qualsiasi cassa.
- La corazza toglie i suoi punti da ogni colpo, ma almeno 20% di un colpo passa sempre.
- Un’esplosione ad area fa 1,6 volte tanto a un asteroide fragile rispetto a qualsiasi altro.
- Un asteroide non sta mai a meno di 1.500 unità dal bordo di un anello sicuro, a meno di 5.000 unità dal centro del buco nero né a meno di 600 unità dal bordo della mappa, e non compare mai a meno di 1.200 unità da un pilota.
- Dopo una rottura, un asteroide dello stesso tipo ricresce altrove sulla mappa dopo il tempo indicato nella riga del settore, con uno scarto di 25%.
- Motherlode ritorna dopo 1 h, in qualsiasi settore.

<!-- asteroids-rules:end -->

## I mondi {#the-worlds}

Ogni mondo, Alpha, Beta e Gamma, ha asteroidi propri negli stessi posti ([Mondi](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)), quindi l’asteroide che spezzi nel tuo mondo non è spezzato in un altro. Un mondo più grande significa uno scafo più grande e una ricompensa più grande.

<!-- asteroids-worlds:begin -->
<!-- Generated from server/Resources/Asteroids.json (and Rockets.json, Pets.json) by scripts/asteroids-wiki.sh: don't edit by hand. -->

| Mondo | Scafo | Ricompensa |
| :--- | ---: | ---: |
| **Alpha** | ×1 | ×1 |
| **Beta** | ×1,5 | ×2 |
| **Gamma** | ×2 | ×3 |

Le tabelle qui sotto riportano i numeri di un asteroide di Alpha. **Scafo** è il fattore del mondo sullo scafo di ogni asteroide e **Ricompensa** il suo fattore sui crediti e sul Thulium di una rottura; il minerale e i ritrovamenti rari sono uguali in ogni mondo. I frammenti pagano per intero: non c’è un limite giornaliero.

<!-- asteroids-worlds:end -->

## Dove si trovano {#where-they-are}

Ogni settore di casa delle tre corporazioni e dei settori pericolosi ha asteroidi, in un mix proprio: soprattutto i tipi del suo anello, con uno o due ospiti dall’anello sopra o sotto. I settori neutrali, a cui non porta nessun portale, non ne hanno. Gli asteroidi dei settori pericolosi compaiono dal giorno di stagione indicato in tabella, il giorno in cui si apre il PvP ([Primo contatto](/wiki/03-Mechanics/Wipe-Timeline.md)), gli altri dal primo giorno. Dopo una rottura, un nuovo asteroide dello stesso tipo ricresce dopo il tempo indicato nella riga del settore. Nessun asteroide si trova vicino a un pulsar, che brilla dal primo giorno della stagione; dal giorno 11 nessuno si trova nemmeno vicino a un escavatore gigante o al centro del Dormant Swamp ([Settori pericolosi](/wiki/01-General/Danger-Sectors.md#where-everything-is)), e una roccia che stava lì quando è iniziato l’evento 2 è sparita.

<!-- asteroids-maps:begin -->
<!-- Generated from server/Resources/Asteroids.json (and Rockets.json, Pets.json) by scripts/asteroids-wiki.sh: don't edit by hand. -->

| Settore | Asteroidi | Dal giorno | Ritorna | Tipi |
| :--- | ---: | ---: | ---: | :--- |
| `M-1` | 12 | 1 | 2 min | 3 × Pebble, 3 × Cobble, 2 × Glimmer, 2 × Cache Pod, 2 × Ironhide |
| `T-1` | 12 | 1 | 2 min | 3 × Rime, 3 × Cache Pod, 2 × Cobble, 2 × Pebble, 2 × Dark Chondrite |
| `G-1` | 12 | 1 | 2 min | 4 × Glimmer, 2 × Pebble, 2 × Rime, 2 × Cobble, 2 × Nyx Geode |
| `M-2` | 14 | 1 | 3 min | 4 × Ironhide, 3 × Dark Chondrite, 3 × Scrap Hulk, 2 × Vein Rock, 1 × Cobble, 1 × Pebble |
| `T-2` | 14 | 1 | 3 min | 4 × Scrap Hulk, 3 × Dark Chondrite, 3 × Vein Rock, 2 × Nyx Geode, 2 × Rime |
| `G-2` | 14 | 1 | 3 min | 4 × Nyx Geode, 3 × Vein Rock, 3 × Dark Chondrite, 2 × Ironhide, 2 × Glimmer |
| `M-3` | 16 | 1 | 5 min | 3 × Plateback, 3 × Slag Block, 3 × Lode Rock, 3 × Cataclast, 2 × Derelict Hulk, 2 × Cataclysite Mass |
| `T-3` | 16 | 1 | 5 min | 3 × Derelict Hulk, 3 × Slag Block, 3 × Cataclast, 3 × Lode Rock, 2 × Thulium Geode, 2 × Derelict Cruiser |
| `G-3` | 16 | 1 | 5 min | 4 × Cataclast, 3 × Slag Block, 3 × Thulium Geode, 2 × Plateback, 2 × Lode Rock, 2 × Quorvium Boulder |
| `M-4` | 18 | 1 | 5 min | 4 × Anvil, 4 × Cataclysite Mass, 4 × Quorvium Boulder, 2 × Derelict Cruiser, 2 × Vault Rock, 2 × Plateback |
| `T-4` | 18 | 1 | 5 min | 4 × Derelict Cruiser, 4 × Quorvium Boulder, 4 × Cataclysite Mass, 2 × Thulium Cluster, 2 × Vault Rock, 2 × Thulium Geode |
| `G-4` | 18 | 1 | 5 min | 5 × Quorvium Boulder, 3 × Cataclysite Mass, 3 × Anvil, 3 × Lode Rock, 2 × Thulium Cluster, 2 × Vault Rock |
| `DS-1` | 24 | 4 | 5 min | 8 × Rich Lode, 6 × Prism Cluster, 4 × Ancient Husk, 3 × Star Crystal, 2 × Vault Rock, 1 × Motherlode |
| `DS-2` | 24 | 4 | 5 min | 7 × Rich Lode, 7 × Ancient Husk, 3 × Star Crystal, 3 × Anvil, 3 × Derelict Cruiser, 1 × Motherlode |
| `DS-3` | 24 | 4 | 5 min | 9 × Prism Cluster, 5 × Rich Lode, 4 × Star Crystal, 3 × Quorvium Boulder, 2 × Cataclysite Mass, 1 × Motherlode |
| `DS-4` | 24 | 4 | 5 min | 9 × Rich Lode, 5 × Prism Cluster, 4 × Ancient Husk, 3 × Cataclysite Mass, 2 × Derelict Cruiser, 1 × Motherlode |

<!-- asteroids-maps:end -->

## I tipi {#the-kinds}

<!-- asteroids-kinds:begin -->
<!-- Generated from server/Resources/Asteroids.json (and Rockets.json, Pets.json) by scripts/asteroids-wiki.sh: don't edit by hand. -->

### Livelli e parti di P.E.T. {#tiers-and-pet-parts}

Il **livello** di un asteroide è l’anello di settori a cui appartiene il suo tipo: i livelli da 1 a 4 sono i settori da x-1 a x-4 delle tre corporazioni e il livello 5 i settori pericolosi. Il livello sale con le dimensioni: più grande è l’asteroide, più alto è il suo livello. Le due cose però non coincidono: la maggior parte dei livelli comprende due dimensioni, riportate in tabella. La finestra bersaglio e la scheda che compare al passaggio del mouse mostrano famiglia, dimensioni e livello di un asteroide.

Il livello decide anche un ritrovamento a parte: una **parte di P.E.T.**, un Cluster Chunk che prende la Culla dei [P.E.T.](/wiki/03-Mechanics/Pets.md). La tabella dà la probabilità che un asteroide spezzato lasci ciascun grado (un trattino: mai). Gli asteroidi di livello 1 non ne lasciano. Ogni grado viene tirato una volta per asteroide spezzato, il pilota che ha inflitto più danni riceve il chunk intero e la fortuna non cambia le probabilità. La Motherlode ha probabilità proprie. Seleziona un asteroide e la finestra bersaglio elenca le parti di P.E.T. del suo tipo.

| Livello | Settori | Dimensioni | Tipi | [Regular Cluster Chunk](/wiki/06-Items/Resources.md#regular-cluster-chunk) | [Mythical Cluster Chunk](/wiki/06-Items/Resources.md#mythical-cluster-chunk) | [Legendary Cluster Chunk](/wiki/06-Items/Resources.md#legendary-cluster-chunk) |
| :--- | :--- | :--- | :--- | ---: | ---: | ---: |
| 1 | `x-1` | Minuscolo, Piccolo | Pebble, Cobble, Glimmer, Rime, Cache Pod | – | – | – |
| 2 | `x-2` | Piccolo, Medio | Dark Chondrite, Ironhide, Vein Rock, Nyx Geode, Scrap Hulk | 0,4% | – | – |
| 3 | `x-3` | Medio | Slag Block, Plateback, Cataclast, Lode Rock, Derelict Hulk, Thulium Geode | 0,8% | 0,15% | – |
| 4 | `x-4` | Medio, Grande | Quorvium Boulder, Cataclysite Mass, Anvil, Derelict Cruiser, Thulium Cluster, Vault Rock | 1% | 0,25% | 0,03% |
| 5 | Settori pericolosi | Grande | Rich Lode, Prism Cluster, Ancient Husk, Star Crystal | 1,2% | 0,3% | 0,1% |
| 5 | Settori pericolosi | Enorme | Motherlode | 25% | 8% | 3% |

Ci sono 27 tipi di asteroide, in 8 famiglie. **Fatto per** indica il razzo per cui un tipo è bilanciato e più o meno quanti ne servono per una rottura in Alpha. **Ritrovamenti** sono il minerale e i ritrovamenti rari che una rottura estrae e che i suoi frammenti si dividono: una percentuale è la probabilità di quella riga, le altre righe si trovano sempre. I crediti e il Thulium sono gli importi di Alpha di una rottura.

### Roccia {#stone}

Roccia normale: nessuna corazza e nessun punto debole.

| Tipo | Scafo | Dimensioni | Livello | Particolarità | Frammenti di denaro | Fatto per | Crediti | Thulium | Ritrovamenti | Si trova in |
| :--- | ---: | :--- | ---: | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Pebble** | 8.500 | Minuscolo | 1 | – | 1 | Circa 4× [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 6.600–11.100 | 22% per 3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3 (49%) | `M-1`, `T-1`, `G-1`, `M-2` |
| **Cobble** | 10.000 | Piccolo | 1 | – | 1 | Circa 5× [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 6.300–10.500 | 25% per 3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–9 (89%) | `M-1`, `T-1`, `G-1`, `M-2` |
| **Dark Chondrite** | 12.000 | Piccolo | 2 | – | 1 | Circa 3× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 7.050–11.850 | 65% per 3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–12 (91%), [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (93%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `T-1`, `M-2`, `T-2`, `G-2` |
| **Vein Rock** | 18.000 | Piccolo | 2 | – | 1 | Circa 4× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 13.350–22.200 | 50% per 3–9 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–6 (73%), [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (45%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `M-2`, `T-2`, `G-2` |
| **Slag Block** | 24.000 | Medio | 3 | – | 2 | Circa 5× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 18.600–31.050 | 50% per 3–9 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (95%), [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 3–6 (84%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1,5%) | `M-3`, `T-3`, `G-3` |
| **Cataclast** | 36.000 | Medio | 3 | – | 2 | Circa 8× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 22.350–37.200 | 50% per 6–15 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 9–18, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–24; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1,5%) | `M-3`, `T-3`, `G-3` |
| **Lode Rock** | 52.000 | Medio | 3 | – | 2 | Circa 11× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 34.950–58.200 | 50% per 18–39 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 9–18, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–24; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1,5%) | `M-3`, `T-3`, `G-3`, `G-4` |
| **Cataclysite Mass** | 72.000 | Grande | 4 | – | 2 | Circa 10× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 44.700–74.550 | 50% per 21–45 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 15–30, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 9–15; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `M-3`, `M-4`, `T-4`, `G-4`, `DS-3`, `DS-4` |
| **Rich Lode** | 80.000 | Grande | 5 | – | 3 | Circa 11× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 61.800–103.050 | 50% per 39–90 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–24, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 6–12; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (8%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (5%) | `DS-1`, `DS-2`, `DS-3`, `DS-4` |

### Ghiaccio {#ice}

Roccia ghiacciata: nessuna corazza e nessun punto debole.

| Tipo | Scafo | Dimensioni | Livello | Particolarità | Frammenti di denaro | Fatto per | Crediti | Thulium | Ritrovamenti | Si trova in |
| :--- | ---: | :--- | ---: | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Rime** | 12.000 | Piccolo | 1 | – | 1 | Circa 5× [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 8.250–13.800 | 55% per 3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–9 (77%) | `T-1`, `G-1`, `T-2` |

### Cristallo {#crystal}

Fragile: un’esplosione ad area fa più danno a un asteroide di cristallo di un colpo diretto.

| Tipo | Scafo | Dimensioni | Livello | Particolarità | Frammenti di denaro | Fatto per | Crediti | Thulium | Ritrovamenti | Si trova in |
| :--- | ---: | :--- | ---: | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Glimmer** | 9.000 | Minuscolo | 1 | Esplosioni ×1,6 | 1 | Circa 4× [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 6.150–10.350 | 41% per 3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–6 (77%) | `M-1`, `G-1`, `G-2` |
| **Nyx Geode** | 26.000 | Medio | 2 | Esplosioni ×1,6 | 2 | Circa 6× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 16.650–27.750 | 50% per 9–21 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 6–15, [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3–6 (96%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `G-1`, `T-2`, `G-2` |
| **Quorvium Boulder** | 48.000 | Medio | 4 | Esplosioni ×1,6 | 2 | Circa 7× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 29.850–49.650 | 50% per 12–30 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–21, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 3–15 (86%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `G-3`, `M-4`, `T-4`, `G-4`, `DS-3` |
| **Prism Cluster** | 100.000 | Grande | 5 | Esplosioni ×1,6 | 3 | Circa 14× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 71.700–119.550 | 50% per 27–60 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 24–42, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 12–21; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (8%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (5%) | `DS-1`, `DS-3`, `DS-4` |

### Relitti {#salvage}

Relitti e capsule: contengono Ship Fragment.

| Tipo | Scafo | Dimensioni | Livello | Particolarità | Frammenti di denaro | Fatto per | Crediti | Thulium | Ritrovamenti | Si trova in |
| :--- | ---: | :--- | ---: | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Cache Pod** | 14.000 | Minuscolo | 1 | – | 1 | Circa 6× [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 9.000–15.000 | 29% per 3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–6 (83%), [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 3–9 (78%) | `M-1`, `T-1` |
| **Scrap Hulk** | 20.000 | Piccolo | 2 | – | 1 | Circa 5× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 12.150–20.250 | 92% per 3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–9 (95%), [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (77%), [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 6–12; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `M-2`, `T-2` |
| **Derelict Hulk** | 52.000 | Medio | 3 | – | 2 | Circa 11× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 33.150–55.200 | 50% per 9–18 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 6–12, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 9–18, [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 30–54; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1,5%) | `M-3`, `T-3` |
| **Derelict Cruiser** | 72.000 | Grande | 4 | – | 2 | Circa 10× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 46.200–76.950 | 50% per 18–39 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 9–15, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 3–9 (97%), [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 21–36; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `T-3`, `M-4`, `T-4`, `DS-2`, `DS-4` |

### Ferro {#iron}

Corazzato: ogni colpo perde punti per la corazza, quindi chiedono razzi più forti di quanto il loro scafo faccia pensare.

| Tipo | Scafo | Dimensioni | Livello | Particolarità | Frammenti di denaro | Fatto per | Crediti | Thulium | Ritrovamenti | Si trova in |
| :--- | ---: | :--- | ---: | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Ironhide** | 14.000 | Piccolo | 2 | Corazza 500 | 1 | Circa 4× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 13.650–22.650 | 50% per 3–9 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–6 (74%), [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (46%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `M-1`, `M-2`, `G-2` |
| **Plateback** | 36.000 | Medio | 3 | Corazza 1.500 | 2 | Circa 11× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 31.650–52.800 | 50% per 9–18 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 6–12, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 9–15, [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 27–51; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1,5%) | `M-3`, `G-3`, `M-4` |
| **Anvil** | 80.000 | Grande | 4 | Corazza 3.000 | 2 | Circa 18× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 84.900–141.450 | 50% per 30–72 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 15–27, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 6–15, [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 36–69; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `M-4`, `G-4`, `DS-2` |

### Tesoro {#treasure}

I migliori pagatori: ognuno paga più crediti e Thulium dell’asteroide medio del suo anello.

| Tipo | Scafo | Dimensioni | Livello | Particolarità | Frammenti di denaro | Fatto per | Crediti | Thulium | Ritrovamenti | Si trova in |
| :--- | ---: | :--- | ---: | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Thulium Geode** | 66.000 | Medio | 3 | Esplosioni ×1,6 | 2 | Circa 14× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 42.450–70.800 | 36–84 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 9–15, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–21; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1,5%) | `T-3`, `G-3`, `T-4` |
| **Thulium Cluster** | 100.000 | Grande | 4 | – | 2 | Circa 14× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 62.100–103.500 | 42–99 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–21, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 3–15 (90%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `T-4`, `G-4` |
| **Vault Rock** | 130.000 | Grande | 4 | – | 3 | Circa 18× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 101.400–169.050 | 50% per 36–87 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 9–18, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 3–12 (90%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `M-4`, `T-4`, `G-4`, `DS-1` |
| **Star Crystal** | 150.000 | Grande | 5 | Esplosioni ×1,6 | 3 | Circa 21× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 109.650–182.700 | 60–141 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 18–33, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 9–15; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (8%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (5%) | `DS-1`, `DS-2`, `DS-3` |

### Reliquia {#relic}

Il guscio di una nave di sciame morta: corazzato e ricco di ritrovamenti rari.

| Tipo | Scafo | Dimensioni | Livello | Particolarità | Frammenti di denaro | Fatto per | Crediti | Thulium | Ritrovamenti | Si trova in |
| :--- | ---: | :--- | ---: | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Ancient Husk** | 120.000 | Grande | 5 | Corazza 2.000 | 3 | Circa 22× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 114.300–190.350 | 50% per 57–129 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 24–45, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 12–24; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (16%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (10%) | `DS-1`, `DS-2`, `DS-4` |

### Titano {#titan}

Il più grande di tutti, una roccia per un gruppo.

| Tipo | Scafo | Dimensioni | Livello | Particolarità | Frammenti di denaro | Fatto per | Crediti | Thulium | Ritrovamenti | Si trova in |
| :--- | ---: | :--- | ---: | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Motherlode** | 450.000 | Enorme | 5 | – | 3 | Circa 61× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 348.900–581.400 | 165–381 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 69–126, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 36–66; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (8%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (5%) | `DS-1`, `DS-2`, `DS-3`, `DS-4` |

<!-- asteroids-kinds:end -->

## Che cosa non dà {#what-it-does-not-give}

Un asteroide non è un abbattimento. Spezzarlo non dà XP, onore, conteggio di abbattimenti, punti PvE o PvP, classifica, [punti reset](/wiki/03-Mechanics/Wipe-Timeline.md#earning-wipe-points), XP dei droni né progressi in una [missione](/wiki/03-Mechanics/Quests.md), tranne la [missione degli asteroidi di ogni livello](/wiki/03-Mechanics/Quests.md#levels). Neppure i potenziamenti dell’Emporio lo toccano. Dà quello che c’è nelle tabelle: crediti, Thulium e minerale, che la pagina [Risorse](/wiki/06-Items/Resources.md) elenca insieme al bottino degli alieni.

## Consigli {#tips}

- **Comincia con il razzo per cui è fatto il tipo.** Un razzo più debole spezza comunque l’asteroide, ma servono più razzi e più timer. Uno più forte è più veloce, ma il danno di un colpo oltre lo scafo rimasto va perso, e un razzo costa lo stesso qualunque cosa colpisca.
- **Porta esplosioni per il cristallo e forza per il ferro.** Uno Scatter o un Ember è il razzo per un asteroide fragile, e uno corazzato chiede un razzo più forte di quanto il suo scafo faccia pensare, perché la corazza toglie i suoi punti da ogni colpo.
- **Lascia lavorare i laser tra un razzo e l’altro.** Sparano una volta al secondo e costano munizioni, non razzi, ma una raffica fa solo il 5% di quello che fa a una nave: si aggiungono ai razzi e non li sostituiscono.
- **Occhio all’offerta.** I frammenti non hanno un limite giornaliero, ma un settore contiene solo un certo numero di asteroidi e ciascuno ricresce solo dopo un po’; in un settore affollato ogni pilota ne ottiene meno, perciò spostati in uno più tranquillo.
- **Spezzate insieme i grandi.** L’asteroide Motherlode è una roccia per un gruppo: un gruppo conta come un solo pilota e la sua parte è divisa per livello tra i compagni vicini che sparano. Anche un Mole lo lavora, per chi vola con lui.
- **Tieni d’occhio il settore.** Gli asteroidi non rispondono al fuoco, ma i settori intorno a loro hanno ancora alieni e, nei settori pericolosi, altri piloti.
- **Usali, e stai attento.** Un asteroide tra te e un rivale o un alieno tiene i tuoi laser e i loro lontani gli uni dagli altri. Un rivale che ti spara attraverso l’asteroide che stai estraendo lo danneggia e viene pagato in base al danno inflitto, come ogni altro pilota.
