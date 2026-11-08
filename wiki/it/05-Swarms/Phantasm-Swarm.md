<!-- wiki-i18n source: abb582fd63389ab9 -->
<!-- wiki-i18n title: Sciame Phantasm -->
# Sciame Phantasm {#phantasm-swarm}

Lo sciame Phantasm è un **Boss Phantasm** con i suoi **Phantasm Guard**: un enorme [Phantasm](/wiki/04-Aliens/Phantasm.md) che non inizia mai uno scontro, e altri più piccoli che restano vicini a lui e lo curano. Vive nei settori esterni delle corporazioni, `x-3` e `x-4`, ed è uno scontro per un gruppo di piloti di livello medio.

## In breve {#at-a-glance}

<!-- phantasm-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dove**: I settori `x-3` e `x-4` di ogni corporazione
- **Quanti**: Uno in ciascuno di quei settori, 6 in ogni mondo
- **Compare**: Dal giorno 4 della stagione fino al reset (Beta e Gamma: dal giorno 1 della stagione)
- **Capo**: Boss Phantasm
- **Seguaci**: Fino a 4 × Phantasm Guard, uno nuovo ogni 10 s
- **I seguaci restano vicini**: al massimo 500 unità dal capo
- **Cura**: Ogni Phantasm Guard entro 600 unità dal capo ne cura lo scafo, 30 HP al secondo in Alpha
- **Capo distrutto**: I seguaci se ne vanno 30 s dopo la distruzione del capo, a meno che stiano attaccando
- **Ritorna**: 2 min dopo la distruzione del capo, nello stesso settore
- **Avvisi**: I piloti del settore vengono avvisati quando il capo compare e quando viene distrutto. Sono righe di Sistema: compaiono nella scheda **Sistema** della chat, con un conteggio delle righe non lette, e non in **Globale** né in **Locale**. Il kill feed nomina il pilota a cui viene accreditato l’abbattimento.

<!-- phantasm-glance:end -->

## I membri {#the-members}

- **Boss Phantasm**: un Phantasm più grande, con la tinta dello sciame e il suo nome sopra, con scafo, scudo e raffica laser propri (i valori sono qui sotto). È passivo: vaga finché un pilota non lo colpisce, poi va contro quel pilota e gli spara, e le navi del suo sciame vicine si uniscono allo scontro. La portata della sua arma e la sua velocità sono quelle di un Phantasm, e non ripara mai da solo il suo scafo.
- **Phantasm Guard**: un Phantasm più piccolo con la tinta dello sciame. I Guard restano vicini al boss, si uniscono allo scontro quando una nave di sciame vicina viene colpita, e ognuno che è vicino al boss ne cura lo scafo. Un Guard ripara il proprio scafo dopo una pausa, come fa un Phantasm.

## Come va lo scontro {#how-the-fight-goes}

- **Porta un gruppo.** Tre piloti di livello 4–5 con munizioni x2 lo distruggono in circa un minuto e mezzo in Alpha, perdendo al massimo una nave; un pilota di quel livello da solo viene distrutto, e due vincono a malapena, e solo finché i colpi sono distribuiti. Navi migliori e munizioni x4 lo rendono molto più rapido.
- **Spara al boss, non ai Guard.** Un Guard cade in pochi secondi, ma ne arriva uno nuovo con la frequenza indicata nell’elenco *In breve*, e ciò che i Guard curano è una piccola parte di ciò che infligge un gruppo: lasciarli stare costa un po’ di tempo, dare loro la caccia ne costa di più.
- **Beta e Gamma sono più duri.** Gli sciami di quei mondi sono più forti ([Mondi](/wiki/05-Swarms/Swarms.md#the-worlds)), quindi servono più piloti o munizioni migliori.
- **Tieni d’occhio il settore.** `x-4` è un settore PvP in Alpha, e `x-3` e `x-4` lo sono in Beta e Gamma ([Mondi](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): un rivale può unirsi allo scontro o aspettare la cassa. Lascia una nave del gruppo di guardia.
- **Il boss ritorna** dopo il tempo indicato nell’elenco *In breve*, a piena forza, nello stesso settore, e i suoi Guard arrivano uno dopo l’altro.

## Ricompense e bottino {#rewards-and-drops}

Il Boss Phantasm paga per lo scontro che è: un minuto di scontro con lui paga più di un minuto di scontro con un Goombah, l’alieno meglio pagato di questi settori. La ricompensa si divide in base al danno tra i piloti che lo hanno combattuto ([come paga l’abbattimento di un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). La sua cassa va al pilota che ha inflitto più danno e contiene molte volte il bottino di un Phantasm (Ship Fragment, Daraxium e Nyxite), con munizioni e razzi. I Guard pagano poco e non lasciano nulla; abbatterli non è un buon farming, perché tornano insieme al boss.

## I valori {#the-numbers}

I valori delle navi dello sciame nei tre mondi ([Mondi](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- phantasm-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Phantasm

Base: Phantasm; rispetto all’originale, scafo 2.000% e danno dei laser 300%; velocità e portata sono quelle della nave di partenza.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | 40.000 | 60.000 | 80.000 |
| Scudo | 64.000 | 96.000 | 128.000 |
| Danno dei laser (una raffica al secondo) | 1.050 | 1.575 | 2.100 |
| Velocità | 160 | 160 | 160 |
| Portata dei laser | 700 | 700 | 700 |
| Raggio di aggressione | solo se attaccato | solo se attaccato | solo se attaccato |
| Crediti | 39.000 | 78.000 | 117.000 |
| Thulium | 195 | 390 | 585 |
| Esperienza (XP) | 7.800 | 15.600 | 23.400 |
| Onore | 62 | 124 | 186 |
| Punti PvE per abbattimento | 8 | 8 | 8 |

**Bottino**: una cassa, per il pilota che ha inflitto più danno.

| Oggetto | Probabilità | Quantità |
| :--- | ---: | ---: |
| Ship Fragment | 100% a ciascuno di 13 tiri | 1 |
| Daraxium | 60% a ciascuno di 13 tiri | 1–2 |
| Nyxite | 60% a ciascuno di 13 tiri | 1–2 |
| Standard Battery | 100% | 600–1.200 |
| Advanced Plasma | 100% | 60–100 |
| Ultra Core | 100% | 10–20 |
| Uno dei 8 [razzi](/wiki/06-Items/Rockets.md) acquistabili con i crediti, scelto a caso | 100% | 4–6 |

### Phantasm Guard

Base: Phantasm, con il 50% di scafo, scudo e danno; velocità e portata sono quelle della nave di partenza.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | 1.000 | 1.500 | 2.000 |
| Scudo | 1.600 | 2.400 | 3.200 |
| Danno dei laser (una raffica al secondo) | 175 | 263 | 350 |
| Velocità | 160 | 160 | 160 |
| Portata dei laser | 700 | 700 | 700 |
| Raggio di aggressione | solo se attaccato | solo se attaccato | solo se attaccato |
| Cura il capo, ciascuno, al secondo (solo scafo) | 30 | 45 | 60 |
| Crediti | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Esperienza (XP) | 12 | 24 | 36 |
| Onore | 1 | 2 | 3 |
| Punti PvE per abbattimento | 1 | 1 | 1 |

**Bottino**: nessuno. L’abbattimento paga solo i suoi crediti, il Thulium, l’XP e l’onore.

<!-- phantasm-members:end -->
