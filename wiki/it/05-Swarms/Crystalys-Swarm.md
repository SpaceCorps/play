<!-- wiki-i18n source: 62896aebea81e95a -->
<!-- wiki-i18n title: Sciame Crystalys -->
# Sciame Crystalys {#crystalys-swarm}

Lo sciame Crystalys è un **Boss Crystalys** con i suoi **Crystalys Guard**: il più resistente degli alieni, il [Crystalys](/wiki/04-Aliens/Crystalys.md), ingrandito, con guardie che restano vicine a lui e lo curano. Vive nei [settori pericolosi](/wiki/01-General/Danger-Sectors.md) `DS-1`, `DS-2` e `DS-3`, uno in ciascuno, e non lascia mai il suo settore. I settori pericolosi sono settori PvP, quindi lo scontro è per un grande gruppo dei piloti più forti, e il boss non è l’unico pericolo.

## In breve {#at-a-glance}

<!-- crystalys-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dove**: I settori pericolosi `DS-1`, `DS-2`, `DS-3`
- **Quanti**: Uno in ciascuno di quei settori, 3 in ogni mondo
- **Compare**: Dal giorno 4 della stagione fino al reset
- **Capo**: Boss Crystalys
- **Seguaci**: Fino a 3 × Crystalys Guard, uno nuovo ogni 10 s
- **I seguaci restano vicini**: al massimo 500 unità dal capo
- **Cura**: Ogni Crystalys Guard entro 600 unità dal capo ne cura lo scafo, 250 HP al secondo in Alpha
- **Capo distrutto**: I seguaci se ne vanno 30 s dopo la distruzione del capo, a meno che stiano attaccando
- **Ritorna**: 30 min dopo la distruzione del capo, nello stesso settore
- **Avvisi**: I piloti del settore vengono avvisati quando il capo compare e quando viene distrutto. Sono righe di Sistema: compaiono nella scheda **Sistema** della chat, con un conteggio delle righe non lette, e non in **Globale** né in **Locale**. Il kill feed nomina il pilota a cui viene accreditato l’abbattimento.

<!-- crystalys-glance:end -->

## I membri {#the-members}

- **Boss Crystalys**: un Crystalys più grande, con la tinta dello sciame e il suo nome sopra, con scafo, scudo e raffica laser propri (i valori sono qui sotto). È passivo: vaga finché un pilota non lo colpisce, poi va contro quel pilota e gli spara, e le navi del suo sciame vicine si uniscono allo scontro. La portata della sua arma e la sua velocità sono quelle di un Crystalys, e non ripara mai da solo il suo scafo.
- **Crystalys Guard**: un Crystalys più piccolo con la tinta dello sciame. I Guard restano vicini al boss, si uniscono allo scontro quando una nave di sciame vicina viene colpita, e ognuno che è vicino al boss ne cura lo scafo. Un Guard ripara il proprio scafo dopo una pausa, come fa un Crystalys.

## Come va lo scontro {#how-the-fight-goes}

- **Porta un grande gruppo.** Otto piloti di livello 8 su Paragon con munizioni x2 lo distruggono in circa un minuto in Alpha, perdendo al massimo una nave; quattro hanno bisogno di munizioni x4, e un pilota da solo viene distrutto.
- **Spara al boss, non ai Guard.** Un Guard cade in pochi secondi, ma ne arriva uno nuovo con la frequenza indicata nell’elenco *In breve*, e ciò che i Guard curano è una piccola parte di ciò che infligge un gruppo: lasciarli stare costa un po’ di tempo, dare loro la caccia ne costa di più.
- **Beta e Gamma sono più duri.** Gli sciami di quei mondi sono più forti ([Mondi](/wiki/05-Swarms/Swarms.md#the-worlds)), quindi servono più piloti o munizioni migliori.
- **I settori pericolosi sono PvP.** Un rivale può attaccare il gruppo in mezzo allo scontro e aspettare la cassa: è del pilota che ha inflitto più danno (e del suo clan) per 30 secondi, poi di chiunque ([Carico](/wiki/03-Mechanics/Cargo.md)). Non andare da solo.
- **Il boss ritorna** dopo il tempo indicato nell’elenco *In breve*, a piena forza, nello stesso settore, e i suoi Guard arrivano uno dopo l’altro.

## Ricompense e bottino {#rewards-and-drops}

Il Boss Crystalys paga per lo scontro che è: un minuto di scontro con lui paga più di un minuto di scontro con un Crystalys, l’alieno meglio pagato. La ricompensa si divide in base al danno tra i piloti che lo hanno combattuto ([come paga l’abbattimento di un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). La sua cassa va al pilota che ha inflitto più danno e contiene Cataclysite e Quorvium, ogni tanto un Power Core, un’Ancient Control Unit o Dark Matter, munizioni x3 e x4 e razzi Epici. I Guard pagano poco e non lasciano nulla; abbatterli non è un buon farming, perché tornano insieme al boss.

## I valori {#the-numbers}

I valori delle navi dello sciame nei tre mondi ([Mondi](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- crystalys-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Crystalys

Base: Crystalys; rispetto all’originale, scafo 175% e danno dei laser 50%; velocità e portata sono quelle della nave di partenza.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | 448.000 | 672.000 | 896.000 |
| Scudo | 280.000 | 420.000 | 560.000 |
| Danno dei laser (una raffica al secondo) | 5.000 | 7.500 | 10.000 |
| Velocità | 230 | 230 | 230 |
| Portata dei laser | 900 | 900 | 900 |
| Raggio di aggressione | solo se attaccato | solo se attaccato | solo se attaccato |
| Crediti | 393.750 | 787.500 | 1.181.250 |
| Thulium | 1.050 | 2.100 | 3.150 |
| Esperienza (XP) | 63.000 | 126.000 | 189.000 |
| Onore | 273 | 546 | 819 |
| Punti PvE per abbattimento | 21 | 21 | 21 |

**Bottino**: una cassa, per il pilota che ha inflitto più danno.

| Oggetto | Probabilità | Quantità |
| :--- | ---: | ---: |
| Cataclysite | 100% a ciascuno di 2 tiri | 8 |
| Quorvium | 100% a ciascuno di 2 tiri | 6–10 |
| Power Core | 30% | 1 |
| Ancient Control Unit | 15% | 1 |
| Dark Matter | 4% | 1 |
| Ultra Core e Experimental Fusion Core, divisi in parti uguali | 100% | 600–1.000 in tutto |
| Uno dei 4 [razzi](/wiki/06-Items/Rockets.md) Epici, scelto a caso | 100% | 8–15 |

### Crystalys Guard

Base: Crystalys, con il 15% di scafo, scudo e danno; velocità e portata sono quelle della nave di partenza.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | 38.400 | 57.600 | 76.800 |
| Scudo | 24.000 | 36.000 | 48.000 |
| Danno dei laser (una raffica al secondo) | 1.500 | 2.250 | 3.000 |
| Velocità | 230 | 230 | 230 |
| Portata dei laser | 900 | 900 | 900 |
| Raggio di aggressione | solo se attaccato | solo se attaccato | solo se attaccato |
| Cura il capo, ciascuno, al secondo (solo scafo) | 250 | 375 | 500 |
| Crediti | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Esperienza (XP) | 12 | 24 | 36 |
| Onore | 1 | 2 | 3 |
| Punti PvE per abbattimento | 6 | 6 | 6 |

**Bottino**: nessuno. L’abbattimento paga solo i suoi crediti, il Thulium, l’XP e l’onore.

<!-- crystalys-members:end -->
