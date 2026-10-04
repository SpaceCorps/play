<!-- wiki-i18n source: bbd76eb145ce6188 -->
<!-- wiki-i18n title: Sciami -->
# Sciami {#swarms}

Uno **sciame** è un gruppo di alieni che percorre una parte della galassia sotto un **capo**: un boss molto più forte di qualsiasi alieno intorno a lui, con dei **seguaci** che lo proteggono e, in due degli sciami, lo curano. Ce ne sono tre, e ciascuno ha un articolo tutto suo:

- [Sciame Seeker](/wiki/05-Swarms/Seeker-Swarm.md): il Boss Seeker e i suoi Seeker Slave, lo sciame più piccolo, nei settori in cui volano i piloti nuovi.
- [Sciame Pirate](/wiki/05-Swarms/Pirate-Swarm.md): il Pirate Boss e i suoi Pirate Scout, uno scontro lungo per un gruppo.
- [Sciame Dormant](/wiki/05-Swarms/Dormant-Swarm.md): la Dormant Force e le sue Dormant Pulse, lo sciame più forte, con il bottino più ricco.

Le loro navi sono **alieni di specie a sé**: hanno nomi propri e contatori di abbattimenti propri, e nessuna conta come un Seeker, un Phantasm o un altro alieno. Una nave di sciame ha la forma della nave su cui è costruita, con una tinta tutta sua e il suo nome sopra; il Boss Seeker è un Seeker molto più grande.

## I tre sciami {#the-three-swarms}

<!-- swarms-list:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Sciame | Dove | Quanti | Capo | Seguaci | Ritorna |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**Sciame Pirate**](/wiki/05-Swarms/Pirate-Swarm.md) | I settori `x-2` e `x-3` di ogni corporazione | Uno in ciascuno di quei settori, 6 in ogni mondo | **Pirate Boss** | Fino a 5 × Pirate Scout, uno nuovo ogni 10 s | 2 min dopo la distruzione del capo, nello stesso settore |
| [**Sciame Dormant**](/wiki/05-Swarms/Dormant-Swarm.md) | I settori pericolosi `DS-1`, `DS-2`, `DS-3`, `DS-4`, volando dall’uno all’altro | Uno in ogni mondo | **Dormant Force** | 2 × Dormant Pulse, che volano con il capo | 1 h dopo la distruzione dell’intero sciame, in un settore pericoloso casuale |
| [**Sciame Seeker**](/wiki/05-Swarms/Seeker-Swarm.md) | I settori `x-1` e `x-2` di ogni corporazione | Uno in ciascuno di quei settori, 6 in ogni mondo | **Boss Seeker** | Fino a 4 × Seeker Slave, uno nuovo ogni 10 s | 2 min dopo la distruzione del capo, nello stesso settore |

<!-- swarms-list:end -->

## Quando e dove {#when-and-where}

Gli sciami cominciano ad apparire con il **Primo contatto** e restano fino al reset (vedi la [Cronologia del reset](/wiki/03-Mechanics/Wipe-Timeline.md); il giorno è la prima riga delle regole qui sotto). **Ogni mondo ha i suoi sciami** negli stessi posti: il Pirate Boss di Alpha e quello di Beta sono due navi diverse, e uno sciame che distruggi nel tuo mondo non è distrutto in un altro. Uno sciame distrutto torna dopo il tempo indicato nella tabella qui sopra.

## Le regole di ogni sciame {#the-rules-of-every-swarm}

<!-- swarms-rules:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- Gli sciami compaiono dal giorno 4 della stagione fino al reset.
- Quando una nave di sciame viene colpita, le navi del suo sciame entro 1.500 unità da essa si uniscono allo scontro contro il primo pilota che l’ha colpita.
- Un capo compare ad almeno 2.500 unità dal bordo di ogni anello di stazione e di porta.
- Un pilota che ha inflitto almeno 5% del danno fatto a un boss viene pagato per il suo abbattimento.

<!-- swarms-rules:end -->

## I mondi {#the-worlds}

Il mondo scala uno sciame come scala ogni alieno ([Mondi](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): scafo, scudo, ricarica dello scudo, danno dei laser, danno dei razzi e cura di una nave di sciame sono i valori di Alpha moltiplicati per la potenza qui sotto, e un abbattimento paga la ricompensa qui sotto. Velocità, portata e bottino sono uguali in ogni mondo. Gli articoli danno i valori di ogni nave nei tre mondi.

<!-- swarms-world:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Mondo | Potenza | Ricompensa |
| :--- | ---: | ---: |
| **Alpha** | ×1 | ×1 |
| **Beta** | ×1,5 | ×2 |
| **Gamma** | ×2 | ×3 |

<!-- swarms-world:end -->

## Cosa vengono a sapere i piloti {#what-the-pilots-are-told}

Gli sciami Seeker e Pirate avvisano i piloti del loro settore quando compare un boss e quando viene distrutto. Lo sciame Dormant avvisa tutto il suo mondo, ed è segnato sulle mappe dei settori pericolosi e sulla mappa galattica, così i piloti possono trovarlo. Sono righe di Sistema: compaiono nella scheda **Sistema** della chat, con un conteggio delle righe non lette, e non in **Globale** né in **Locale**. L’abbattimento di un boss ha anche una riga nel kill feed, che nomina il pilota a cui viene accreditato. L’elenco *In breve* di ogni articolo dice chi viene avvisato.

## Combattere uno sciame {#fighting-a-swarm}

- **I capi non iniziano mai uno scontro.** Un capo vaga finché un pilota non lo colpisce, poi risponde, e le navi del suo sciame vicine a lui si uniscono allo scontro contro il primo pilota che lo ha colpito (la distanza è nelle regole qui sopra). I Pirate Scout sono l’eccezione: attaccano qualsiasi pilota si avvicini. Un capo non ripara mai da solo il suo scafo, quindi il danno che hai inflitto resta su di lui, a meno che i suoi seguaci non lo curino; il suo scudo si ricarica come quello di ogni alieno.
- **Le navi di sciame combattono solo i piloti.** Non sparano agli alieni e gli alieni non sparano a loro, e i [piloti di corporazione](/wiki/03-Mechanics/Company-Pilots.md) le ignorano: non danno la caccia a una nave di sciame né vengono in tuo aiuto contro una.
- **Razzi.** Il Pirate Boss, la Dormant Force e le Pulse sparano razzi **dritti**, i [razzi Rivet](/wiki/06-Items/Rockets.md), al pilota che le ha attaccate. Una nave che resta in movimento li schiva, una ferma viene colpita.
- **La taglia degli scontri.** Lo sciame Seeker è per due piloti, lo sciame Pirate per un piccolo gruppo, lo sciame Dormant per un grande gruppo delle navi più forti; i mondi più alti richiedono più piloti, come per ogni alieno.

## Cosa portare {#what-to-bring}

- **Un gruppo.** Vola in [gruppo](/wiki/03-Mechanics/Groups.md): gli sciami sono bilanciati per i gruppi, un pilota solo di livello basso viene distrutto in fretta, e solo le navi più forti possono battere un Pirate Boss da sole. Nessuno batte lo sciame Dormant da solo. Uno sciame combatte il primo pilota che lo ha colpito ([Chi combatte un alieno](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)), quindi lascia cominciare la nave più robusta del gruppo.
- **Munizioni migliori.** Porta munizioni x2 o migliori (vedi [Laser e munizioni](/wiki/06-Items/Lasers.md)). La cura dei seguaci di uno sciame può superare quello che un piccolo gruppo infligge con munizioni x1.
- **Scudi e riparazioni** per uno scontro lungo: le abilità della tua nave ([Abilità](/wiki/03-Mechanics/Abilities.md)) contano soprattutto nello scontro con i pirati, che dura minuti.
- **Spazio per muoverti.** Resta fuori dalla portata di un’arma che superi in portata, e non smettere di muoverti contro un razzo.

## Come paga l’abbattimento di un boss {#how-a-boss-kill-pays}

Un alieno normale paga il pilota che lo ha colpito per primo ([Combattimento](/wiki/03-Mechanics/Combat.md#kill-rewards-first-hit-claims)). Il capo di uno sciame, e ogni Dormant Pulse, pagano invece **in base al danno inflitto**:

- **La ricompensa si divide in base al danno.** Ogni pilota che ha inflitto almeno la quota indicata nelle regole qui sopra viene pagato, in proporzione al danno inflitto: crediti, Thulium, XP e onore dell’abbattimento si dividono tra loro. Un pilota sotto la quota non riceve nulla.
- **La cassa di carico va al pilota che ha inflitto più danno.** È sua (e del suo clan) per 30 secondi, come per ogni alieno, poi chiunque può prenderla ([Carico](/wiki/03-Mechanics/Cargo.md)). Ogni nave Dormant ha il suo conteggio del danno e la sua cassa.
- **I seguaci pagano come al solito**: i Pirate Scout e i Seeker Slave pagano il pilota che li ha colpiti per primo, e la loro ricompensa è piccola rispetto a quella di un boss.
- **La ricompensa di un boss è fatta per battere gli alieni attorno a lui.** Un minuto di scontro con un Pirate Boss paga più di un minuto di scontro con un Goombah, e lo sciame Dormant paga ancora di più; il Boss Seeker paga esattamente dieci Seeker.

Ogni abbattimento viene contato con il nome proprio della nave nelle tue statistiche degli abbattimenti e aggiunge punti PvE alla tua classifica:

<!-- swarms-points:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Nave di sciame | Sciame | Punti PvE per abbattimento |
| :--- | :--- | ---: |
| **Pirate Boss** | Sciame Pirate | 10 |
| **Pirate Scout** | Sciame Pirate | 1 |
| **Dormant Force** | Sciame Dormant | 25 |
| **Dormant Pulse** | Sciame Dormant | 10 |
| **Boss Seeker** | Sciame Seeker | 5 |
| **Seeker Slave** | Sciame Seeker | 1 |

<!-- swarms-points:end -->

L’abbattimento di una nave di sciame non conta come abbattimento di un altro alieno: un Boss Seeker o un Seeker Slave non è un Seeker per una missione che chiede Seeker, e le soglie dei punti reset ([Cronologia del reset](/wiki/03-Mechanics/Wipe-Timeline.md#earning-wipe-points)) sono solo quelle dei cinque alieni.
