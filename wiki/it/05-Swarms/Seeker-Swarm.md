<!-- wiki-i18n source: 7c6bc3eaf70223f5 -->
<!-- wiki-i18n title: Sciame Seeker -->
# Sciame Seeker {#seeker-swarm}

Lo sciame Seeker è il più piccolo degli [sciami](/wiki/05-Swarms/Swarms.md): un **Boss Seeker** e i **Seeker Slave** che lo proteggono e lo curano. Vive nei settori in cui i piloti nuovi cominciano a volare, quindi è il primo sciame in cui si imbatte la maggior parte. Il Boss Seeker non inizia mai uno scontro, ma appena gli spari è molto più pericoloso del [Seeker](/wiki/04-Aliens/Seeker.md) su cui è costruito.

## In breve {#at-a-glance}

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dove**: I settori `x-1` e `x-2` di ogni corporazione
- **Quanti**: Uno in ciascuno di quei settori, 6 in ogni mondo
- **Compare**: Dal giorno 4 della stagione fino al reset (Beta e Gamma: dal giorno 1 della stagione)
- **Capo**: Boss Seeker
- **Seguaci**: Fino a 4 × Seeker Slave, uno nuovo ogni 10 s
- **I seguaci restano vicini**: al massimo 500 unità dal capo
- **Cura**: Ogni Seeker Slave entro 600 unità dal capo ne cura lo scafo, 50 HP al secondo in Alpha
- **Capo distrutto**: I seguaci se ne vanno 30 s dopo la distruzione del capo, a meno che stiano attaccando
- **Ritorna**: {{guide:vitals.respawn@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} dopo la distruzione del capo, nello stesso settore
- **Avvisi**: I piloti del settore vengono avvisati quando il capo compare e quando viene distrutto. Sono righe di Sistema: compaiono nella scheda **Sistema** della chat, con un conteggio delle righe non lette, e non in **Globale** né in **Locale**. Il kill feed nomina il pilota a cui viene accreditato l’abbattimento.

<!-- seeker-glance:end -->

## I membri {#the-members}

- **Boss Seeker**: un Seeker molto più grande, con la tinta dello sciame e il suo nome sopra, con molte volte lo scafo, lo scudo e il danno di un Seeker (i valori sono qui sotto). È passivo: vaga finché un pilota non lo colpisce, poi si ferma dov’è e spara a quel pilota, e le navi del suo sciame vicine si uniscono allo scontro. La portata della sua arma e la sua velocità sono quelle di un Seeker, e non ripara mai da solo il suo scafo. Le sue [tre fasi](#the-leaders-three-steps) e un’[abilità speciale](/wiki/03-Mechanics/Special-Abilities.md) possono cambiare questo.
- **Seeker Slave**: un Seeker comune con la tinta dello sciame. Gli Slave restano vicini al boss, si uniscono allo scontro quando una nave di sciame vicina viene colpita, e ognuno che è vicino al boss ne cura lo scafo. Uno Slave ripara il proprio scafo dopo una pausa, come fa un Seeker.

## Come va lo scontro {#how-the-fight-goes}

- **Lascialo stare finché la tua nave non può affrontarlo.** Un Boss Seeker colpisce più forte di quanto regga la prima nave di un pilota: il Protos di un pilota nuovo, ancora senza scudo, viene distrutto in pochi secondi appena il boss e i suoi Slave gli sono addosso.
- **Resta fuori portata.** Il boss e i suoi Slave sono più lenti di un Protos e le loro armi arrivano meno lontano di un Quantum Laser II (vedi [Laser e munizioni](/wiki/06-Items/Lasers.md)): un pilota che ha quei laser e resta oltre la loro portata non subisce danni mentre sparano. Un pilota con Quantum Laser I non può restare fuori portata.
- **Gli Slave curano più in fretta di quanto colpisca un pilota nuovo da solo.** Insieme curano più di quanto infliggano i laser di un pilota con munizioni x1, quindi porta un compagno e munizioni x2. Due piloti con Quantum Laser II che mantengono la distanza abbattono il boss in circa un minuto in Alpha, e molto più in fretta con munizioni x2.
- **Il boss ritorna** dopo il tempo indicato nell’elenco *In breve*, a piena forza, nello stesso settore, e i suoi Slave arrivano uno dopo l’altro.

## Le tre fasi del capo {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Il suo scontro ha tre fasi ([come funzionano](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); ognuna avviene una volta.

- **All’inizio**: I suoi Seeker Slaves lo riparano ×2 più in fretta per 8 s.
- **Sotto i due terzi**: 2 copie di lui compaiono, e quello vero porta un anello.
- **Sotto un terzo**: Vola via dai piloti per 4 s, poi si rivolta.

<!-- mob-ladder:end -->

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
| Scafo | {{guide:vitals.hull@Boss Seeker#1}} | {{guide:vitals.hull@Boss Seeker#2}} | {{guide:vitals.hull@Boss Seeker#3}} |
| Scudo | {{guide:vitals.shield@Boss Seeker#1}} | {{guide:vitals.shield@Boss Seeker#2}} | {{guide:vitals.shield@Boss Seeker#3}} |
| Danno dei laser (una raffica al secondo) | {{guide:vitals.dps@Boss Seeker#1}} | {{guide:vitals.dps@Boss Seeker#2}} | {{guide:vitals.dps@Boss Seeker#3}} |
| Velocità | {{guide:vitals.speed@Boss Seeker#1}} | {{guide:vitals.speed@Boss Seeker#2}} | {{guide:vitals.speed@Boss Seeker#3}} |
| Portata dei laser | 600 | 600 | 600 |
| Raggio di aggressione | solo se attaccato | solo se attaccato | solo se attaccato |
| Crediti | {{guide:spoils.pay.credits@Boss Seeker#1}} | {{guide:spoils.pay.credits@Boss Seeker#2}} | {{guide:spoils.pay.credits@Boss Seeker#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Seeker#1}} | {{guide:spoils.pay.thulium@Boss Seeker#2}} | {{guide:spoils.pay.thulium@Boss Seeker#3}} |
| Esperienza (XP) | {{guide:spoils.pay.experience@Boss Seeker#1}} | {{guide:spoils.pay.experience@Boss Seeker#2}} | {{guide:spoils.pay.experience@Boss Seeker#3}} |
| Onore | {{guide:spoils.pay.honor@Boss Seeker#1}} | {{guide:spoils.pay.honor@Boss Seeker#2}} | {{guide:spoils.pay.honor@Boss Seeker#3}} |
| Punti PvE per abbattimento | 5 | 5 | 5 |

**Bottino**: una cassa, per il pilota che ha inflitto più danno.

| Oggetto |
| :--- |
| {{guide:spoils.box@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} |

### Seeker Slave

Base: Seeker, con il 100% di scafo, scudo e danno; velocità e portata sono quelle della nave di partenza.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | {{guide:vitals.hull@Seeker Slave#1}} | {{guide:vitals.hull@Seeker Slave#2}} | {{guide:vitals.hull@Seeker Slave#3}} |
| Scudo | {{guide:vitals.shield@Seeker Slave#1}} | {{guide:vitals.shield@Seeker Slave#2}} | {{guide:vitals.shield@Seeker Slave#3}} |
| Danno dei laser (una raffica al secondo) | {{guide:vitals.dps@Seeker Slave#1}} | {{guide:vitals.dps@Seeker Slave#2}} | {{guide:vitals.dps@Seeker Slave#3}} |
| Velocità | {{guide:vitals.speed@Seeker Slave#1}} | {{guide:vitals.speed@Seeker Slave#2}} | {{guide:vitals.speed@Seeker Slave#3}} |
| Portata dei laser | 600 | 600 | 600 |
| Raggio di aggressione | solo se attaccato | solo se attaccato | solo se attaccato |
| Cura il capo, ciascuno, al secondo (solo scafo) | 50 | 75 | 100 |
| Crediti | {{guide:spoils.pay.credits@Seeker Slave#1}} | {{guide:spoils.pay.credits@Seeker Slave#2}} | {{guide:spoils.pay.credits@Seeker Slave#3}} |
| Thulium | {{guide:spoils.pay.thulium@Seeker Slave#1}} | {{guide:spoils.pay.thulium@Seeker Slave#2}} | {{guide:spoils.pay.thulium@Seeker Slave#3}} |
| Esperienza (XP) | {{guide:spoils.pay.experience@Seeker Slave#1}} | {{guide:spoils.pay.experience@Seeker Slave#2}} | {{guide:spoils.pay.experience@Seeker Slave#3}} |
| Onore | {{guide:spoils.pay.honor@Seeker Slave#1}} | {{guide:spoils.pay.honor@Seeker Slave#2}} | {{guide:spoils.pay.honor@Seeker Slave#3}} |
| Punti PvE per abbattimento | 1 | 1 | 1 |

**Bottino**: nessuno. L’abbattimento paga solo i suoi crediti, il Thulium, l’XP e l’onore.

<!-- seeker-members:end -->
