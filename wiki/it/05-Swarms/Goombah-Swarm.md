<!-- wiki-i18n source: 38ffa8ba7cbf5000 -->
<!-- wiki-i18n title: Sciame Goombah -->
# Sciame Goombah {#goombah-swarm}

Lo sciame Goombah è un **Boss Goombah** con i suoi **Goombah Guard**: un enorme [Goombah](/wiki/04-Aliens/Goombah.md) che non inizia mai uno scontro, e altri più piccoli che restano vicini a lui e lo curano. Vive negli stessi settori dello [sciame Phantasm](/wiki/05-Swarms/Phantasm-Swarm.md), `x-3` e `x-4`, ed è uno scontro per un gruppo dei piloti più forti dei settori delle corporazioni.

## In breve {#at-a-glance}

<!-- goombah-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dove**: I settori `x-3` e `x-4` di ogni corporazione
- **Quanti**: Uno in ciascuno di quei settori, 6 in ogni mondo
- **Compare**: Dal giorno 4 della stagione fino al reset (Beta e Gamma: dal giorno 1 della stagione)
- **Capo**: Boss Goombah
- **Seguaci**: Fino a 4 × Goombah Guard, uno nuovo ogni 10 s
- **I seguaci restano vicini**: al massimo 500 unità dal capo
- **Cura**: Ogni Goombah Guard entro 600 unità dal capo ne cura lo scafo, 110 HP al secondo in Alpha
- **Capo distrutto**: I seguaci se ne vanno 30 s dopo la distruzione del capo, a meno che stiano attaccando
- **Ritorna**: {{guide:vitals.respawn@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} dopo la distruzione del capo, nello stesso settore
- **Avvisi**: I piloti del settore vengono avvisati quando il capo compare e quando viene distrutto. Sono righe di Sistema: compaiono nella scheda **Sistema** della chat, con un conteggio delle righe non lette, e non in **Globale** né in **Locale**. Il kill feed nomina il pilota a cui viene accreditato l’abbattimento.

<!-- goombah-glance:end -->

## I membri {#the-members}

- **Boss Goombah**: un Goombah più grande, con la tinta dello sciame e il suo nome sopra, con scafo, scudo e raffica laser propri (i valori sono qui sotto). È passivo: vaga finché un pilota non lo colpisce, poi va contro quel pilota e gli spara, e le navi del suo sciame vicine si uniscono allo scontro. La portata della sua arma e la sua velocità sono quelle di un Goombah, e non ripara mai da solo il suo scafo. Le sue [tre fasi](#the-leaders-three-steps) e un’[abilità speciale](/wiki/03-Mechanics/Special-Abilities.md) possono cambiare questo.
- **Goombah Guard**: un Goombah più piccolo con la tinta dello sciame. I Guard restano vicini al boss, si uniscono allo scontro quando una nave di sciame vicina viene colpita, e ognuno che è vicino al boss ne cura lo scafo. Un Guard ripara il proprio scafo dopo una pausa, come fa un Goombah.

## Come va lo scontro {#how-the-fight-goes}

- **Porta un gruppo delle navi più forti.** Tre piloti di livello 8 con munizioni x2 lo distruggono in circa 75 secondi in Alpha, perdendo al massimo una nave; due di loro hanno bisogno di munizioni x4, e i piloti di livello più basso non infliggono abbastanza danno per vincere.
- **Spara al boss, non ai Guard.** Un Guard cade in pochi secondi, ma ne arriva uno nuovo con la frequenza indicata nell’elenco *In breve*, e ciò che i Guard curano è una piccola parte di ciò che infligge un gruppo: lasciarli stare costa un po’ di tempo, dare loro la caccia ne costa di più.
- **Beta e Gamma sono più duri.** Gli sciami di quei mondi sono più forti ([Mondi](/wiki/05-Swarms/Swarms.md#the-worlds)), quindi servono più piloti o munizioni migliori.
- **Tieni d’occhio il settore.** `x-4` è un settore PvP in Alpha, e `x-3` e `x-4` lo sono in Beta e Gamma ([Mondi](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): un rivale può unirsi allo scontro o aspettare la cassa. Lascia una nave del gruppo di guardia.
- **Il boss ritorna** dopo il tempo indicato nell’elenco *In breve*, a piena forza, nello stesso settore, e i suoi Guard arrivano uno dopo l’altro.

## Le tre fasi del capo {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Il suo scontro ha tre fasi ([come funzionano](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); ognuna avviene una volta.

- **All’inizio**: Subisce solo 50% di ogni colpo per 6 s.
- **Sotto i due terzi**: Il suo danno è moltiplicato per ×1,5 e la sua velocità per ×1,25 per 10 s.
- **Sotto un terzo**: Ripristina 25% del suo scafo e del suo scudo (una raffica di danni la interrompe), e nel frattempo i suoi Goombah Guards lo riparano ×2 più in fretta.

<!-- mob-ladder:end -->

## Ricompense e bottino {#rewards-and-drops}

Il Boss Goombah paga per lo scontro che è: un minuto di scontro con lui paga più di un minuto di scontro con un Goombah, l’alieno meglio pagato di questi settori. La ricompensa si divide in base al danno tra i piloti che lo hanno combattuto ([come paga l’abbattimento di un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). La sua cassa va al pilota che ha inflitto più danno e contiene più volte il bottino di un Goombah (Cataclysite, Quorvium, Power Core, Reinforced Hull Plate e Ship Fragment), con munizioni e razzi. I Guard pagano poco e non lasciano nulla; abbatterli non è un buon farming, perché tornano insieme al boss.

## I valori {#the-numbers}

I valori delle navi dello sciame nei tre mondi ([Mondi](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- goombah-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Goombah

Base: Goombah; rispetto all’originale, scafo 400% e danno dei laser 100%; velocità e portata sono quelle della nave di partenza.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | {{guide:vitals.hull@Boss Goombah#1}} | {{guide:vitals.hull@Boss Goombah#2}} | {{guide:vitals.hull@Boss Goombah#3}} |
| Scudo | {{guide:vitals.shield@Boss Goombah#1}} | {{guide:vitals.shield@Boss Goombah#2}} | {{guide:vitals.shield@Boss Goombah#3}} |
| Danno dei laser (una raffica al secondo) | {{guide:vitals.dps@Boss Goombah#1}} | {{guide:vitals.dps@Boss Goombah#2}} | {{guide:vitals.dps@Boss Goombah#3}} |
| Velocità | {{guide:vitals.speed@Boss Goombah#1}} | {{guide:vitals.speed@Boss Goombah#2}} | {{guide:vitals.speed@Boss Goombah#3}} |
| Portata dei laser | 800 | 800 | 800 |
| Raggio di aggressione | solo se attaccato | solo se attaccato | solo se attaccato |
| Crediti | {{guide:spoils.pay.credits@Boss Goombah#1}} | {{guide:spoils.pay.credits@Boss Goombah#2}} | {{guide:spoils.pay.credits@Boss Goombah#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Goombah#1}} | {{guide:spoils.pay.thulium@Boss Goombah#2}} | {{guide:spoils.pay.thulium@Boss Goombah#3}} |
| Esperienza (XP) | {{guide:spoils.pay.experience@Boss Goombah#1}} | {{guide:spoils.pay.experience@Boss Goombah#2}} | {{guide:spoils.pay.experience@Boss Goombah#3}} |
| Onore | {{guide:spoils.pay.honor@Boss Goombah#1}} | {{guide:spoils.pay.honor@Boss Goombah#2}} | {{guide:spoils.pay.honor@Boss Goombah#3}} |
| Punti PvE per abbattimento | 14 | 14 | 14 |

**Bottino**: una cassa, per il pilota che ha inflitto più danno.

| Oggetto |
| :--- |
| {{guide:spoils.box@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} |

### Goombah Guard

Base: Goombah, con il 20% di scafo, scudo e danno; velocità e portata sono quelle della nave di partenza.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | {{guide:vitals.hull@Goombah Guard#1}} | {{guide:vitals.hull@Goombah Guard#2}} | {{guide:vitals.hull@Goombah Guard#3}} |
| Scudo | {{guide:vitals.shield@Goombah Guard#1}} | {{guide:vitals.shield@Goombah Guard#2}} | {{guide:vitals.shield@Goombah Guard#3}} |
| Danno dei laser (una raffica al secondo) | {{guide:vitals.dps@Goombah Guard#1}} | {{guide:vitals.dps@Goombah Guard#2}} | {{guide:vitals.dps@Goombah Guard#3}} |
| Velocità | {{guide:vitals.speed@Goombah Guard#1}} | {{guide:vitals.speed@Goombah Guard#2}} | {{guide:vitals.speed@Goombah Guard#3}} |
| Portata dei laser | 800 | 800 | 800 |
| Raggio di aggressione | solo se attaccato | solo se attaccato | solo se attaccato |
| Cura il capo, ciascuno, al secondo (solo scafo) | 110 | 165 | 220 |
| Crediti | {{guide:spoils.pay.credits@Goombah Guard#1}} | {{guide:spoils.pay.credits@Goombah Guard#2}} | {{guide:spoils.pay.credits@Goombah Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Goombah Guard#1}} | {{guide:spoils.pay.thulium@Goombah Guard#2}} | {{guide:spoils.pay.thulium@Goombah Guard#3}} |
| Esperienza (XP) | {{guide:spoils.pay.experience@Goombah Guard#1}} | {{guide:spoils.pay.experience@Goombah Guard#2}} | {{guide:spoils.pay.experience@Goombah Guard#3}} |
| Onore | {{guide:spoils.pay.honor@Goombah Guard#1}} | {{guide:spoils.pay.honor@Goombah Guard#2}} | {{guide:spoils.pay.honor@Goombah Guard#3}} |
| Punti PvE per abbattimento | 3 | 3 | 3 |

**Bottino**: nessuno. L’abbattimento paga solo i suoi crediti, il Thulium, l’XP e l’onore.

<!-- goombah-members:end -->
