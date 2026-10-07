<!-- wiki-i18n source: 0ed9858d316d7ddd -->
<!-- wiki-i18n title: Sciame Seeker -->
# Sciame Seeker {#seeker-swarm}

Lo sciame Seeker è il più piccolo degli [sciami](/wiki/05-Swarms/Swarms.md): un **Boss Seeker** e i **Seeker Slave** che lo proteggono e lo curano. Vive nei settori in cui i piloti nuovi cominciano a volare, quindi è il primo sciame in cui si imbatte la maggior parte. Il Boss Seeker non inizia mai uno scontro, ma appena gli spari è molto più pericoloso del [Seeker](/wiki/04-Aliens/Seeker.md) su cui è costruito.

## In breve {#at-a-glance}

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dove**: I settori `x-1` e `x-2` di ogni corporazione
- **Quanti**: Uno in ciascuno di quei settori, 6 in ogni mondo
- **Compare**: Dal giorno 4 della stagione fino al reset
- **Capo**: Boss Seeker
- **Seguaci**: Fino a 4 × Seeker Slave, uno nuovo ogni 10 s
- **I seguaci restano vicini**: al massimo 500 unità dal capo
- **Cura**: Ogni Seeker Slave entro 600 unità dal capo ne cura lo scafo, 50 HP al secondo in Alpha
- **Capo distrutto**: I seguaci se ne vanno 30 s dopo la distruzione del capo, a meno che stiano attaccando
- **Ritorna**: 2 min dopo la distruzione del capo, nello stesso settore
- **Avvisi**: I piloti del settore vengono avvisati quando il capo compare e quando viene distrutto. Sono righe di Sistema: compaiono nella scheda **Sistema** della chat, con un conteggio delle righe non lette, e non in **Globale** né in **Locale**. Il kill feed nomina il pilota a cui viene accreditato l’abbattimento.

<!-- seeker-glance:end -->

## I membri {#the-members}

- **Boss Seeker**: un Seeker molto più grande, con la tinta dello sciame e il suo nome sopra, con molte volte lo scafo, lo scudo e il danno di un Seeker (i valori sono qui sotto). È passivo: vaga finché un pilota non lo colpisce, poi si ferma dov’è e spara a quel pilota, e le navi del suo sciame vicine si uniscono allo scontro. La portata della sua arma e la sua velocità sono quelle di un Seeker, e non ripara mai da solo il suo scafo.
- **Seeker Slave**: un Seeker comune con la tinta dello sciame. Gli Slave restano vicini al boss, si uniscono allo scontro quando una nave di sciame vicina viene colpita, e ognuno che è vicino al boss ne cura lo scafo. Uno Slave ripara il proprio scafo dopo una pausa, come fa un Seeker.

## Come va lo scontro {#how-the-fight-goes}

- **Lascialo stare finché la tua nave non può affrontarlo.** Un Boss Seeker colpisce più forte di quanto regga la prima nave di un pilota: il Protos di un pilota nuovo, ancora senza scudo, viene distrutto in pochi secondi appena il boss e i suoi Slave gli sono addosso.
- **Resta fuori portata.** Il boss e i suoi Slave sono più lenti di un Protos e le loro armi arrivano meno lontano di un Quantum Laser 2 (vedi [Laser e munizioni](/wiki/06-Items/Lasers.md)): un pilota che ha quei laser e resta oltre la loro portata non subisce danni mentre sparano. Un pilota con Quantum Laser 1 non può restare fuori portata.
- **Gli Slave curano più in fretta di quanto colpisca un pilota nuovo da solo.** Insieme curano più di quanto infliggano i laser di un pilota con munizioni x1, quindi porta un compagno e munizioni x2. Due piloti con Quantum Laser 2 che mantengono la distanza abbattono il boss in circa un minuto in Alpha, e molto più in fretta con munizioni x2.
- **Il boss ritorna** dopo il tempo indicato nell’elenco *In breve*, a piena forza, nello stesso settore, e i suoi Slave arrivano uno dopo l’altro.

## Ricompense e bottino {#rewards-and-drops}

Il Boss Seeker paga **esattamente dieci Seeker**: dieci volte i crediti, il Thulium, l’XP e l’onore di un Seeker, divisi in base al danno tra i piloti che lo hanno combattuto ([come paga l’abbattimento di un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). La sua cassa contiene il bottino di dieci Seeker e, in più, munizioni e razzi sotto l’Epico, per il pilota che ha inflitto più danno. Gli Slave pagano poco e non lasciano nulla; abbatterli non è un buon farming, perché tornano insieme al boss.

## I valori {#the-numbers}

I valori delle navi dello sciame nei tre mondi ([Mondi](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker

Base: Seeker, con il 400% di scafo, scudo e danno; velocità e portata sono quelle della nave di partenza.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | 3.200 | 4.800 | 6.400 |
| Scudo | 3.200 | 4.800 | 6.400 |
| Danno dei laser (una raffica al secondo) | 720 | 1.080 | 1.440 |
| Velocità | 120 | 120 | 120 |
| Portata dei laser | 600 | 600 | 600 |
| Raggio di aggressione | solo se attaccato | solo se attaccato | solo se attaccato |
| Crediti | 10.000 | 20.000 | 30.000 |
| Thulium | 40 | 80 | 120 |
| Esperienza (XP) | 1.000 | 2.000 | 3.000 |
| Onore | 20 | 40 | 60 |
| Punti PvE per abbattimento | 5 | 5 | 5 |

**Bottino**: una cassa, per il pilota che ha inflitto più danno.

| Oggetto | Probabilità | Quantità |
| :--- | ---: | ---: |
| Ship Fragment | 20% a ciascuno di 10 tiri | 1 |
| Daraxium | 50% a ciascuno di 10 tiri | 1–2 |
| Standard Battery | 100% | 200–400 |
| Advanced Plasma | 100% | 10–20 |
| Ultra Core | 100% | 2–4 |
| Uno dei 8 [razzi](/wiki/06-Items/Rockets.md) acquistabili con i crediti, scelto a caso | 100% | 2–3 |

### Seeker Slave

Base: Seeker, con il 100% di scafo, scudo e danno; velocità e portata sono quelle della nave di partenza.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | 800 | 1.200 | 1.600 |
| Scudo | 800 | 1.200 | 1.600 |
| Danno dei laser (una raffica al secondo) | 180 | 270 | 360 |
| Velocità | 120 | 120 | 120 |
| Portata dei laser | 600 | 600 | 600 |
| Raggio di aggressione | solo se attaccato | solo se attaccato | solo se attaccato |
| Cura il capo, ciascuno, al secondo (solo scafo) | 50 | 75 | 100 |
| Crediti | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Esperienza (XP) | 12 | 24 | 36 |
| Onore | 1 | 2 | 3 |
| Punti PvE per abbattimento | 1 | 1 | 1 |

**Bottino**: nessuno. L’abbattimento paga solo i suoi crediti, il Thulium, l’XP e l’onore.

<!-- seeker-members:end -->
