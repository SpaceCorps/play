<!-- wiki-i18n source: 2b3edf7bcb1d9673 -->
<!-- wiki-i18n title: Sciame Crystalys -->
# Sciame Crystalys {#crystalys-swarm}

Lo sciame Crystalys è un **Boss Crystalys** con i suoi **Crystalys Guard**: il più resistente degli alieni, il [Crystalys](/wiki/04-Aliens/Crystalys.md), ingrandito, con guardie che restano vicine a lui e lo curano. Vive nei [settori pericolosi](/wiki/01-General/Danger-Sectors.md) `DS-1`, `DS-2` e `DS-3`, uno in ciascuno, e non lascia mai il suo settore. I settori pericolosi sono settori PvP, quindi lo scontro è per un grande gruppo dei piloti più forti, e il boss non è l’unico pericolo.

## In breve {#at-a-glance}

<!-- crystalys-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dove**: I settori pericolosi `DS-1`, `DS-2`, `DS-3`
- **Quanti**: Uno in ciascuno di quei settori, 3 in ogni mondo
- **Compare**: Dal giorno 4 della stagione fino al reset (Beta e Gamma: dal giorno 1 della stagione)
- **Capo**: Boss Crystalys
- **Seguaci**: Fino a 3 × Crystalys Guard, uno nuovo ogni 10 s
- **I seguaci restano vicini**: al massimo 500 unità dal capo
- **Cura**: Ogni Crystalys Guard entro 600 unità dal capo ne cura lo scafo, 250 HP al secondo in Alpha
- **Capo distrutto**: I seguaci se ne vanno 30 s dopo la distruzione del capo, a meno che stiano attaccando
- **Ritorna**: {{guide:vitals.respawn@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} dopo la distruzione del capo, nello stesso settore
- **Avvisi**: I piloti del settore vengono avvisati quando il capo compare e quando viene distrutto. Sono righe di Sistema: compaiono nella scheda **Sistema** della chat, con un conteggio delle righe non lette, e non in **Globale** né in **Locale**. Il kill feed nomina il pilota a cui viene accreditato l’abbattimento.

<!-- crystalys-glance:end -->

## I membri {#the-members}

- **Boss Crystalys**: un Crystalys più grande, con la tinta dello sciame e il suo nome sopra, con scafo, scudo e raffica laser propri (i valori sono qui sotto). È passivo: vaga finché un pilota non lo colpisce, poi va contro quel pilota e gli spara, e le navi del suo sciame vicine si uniscono allo scontro. La portata della sua arma e la sua velocità sono quelle di un Crystalys, e non ripara mai da solo il suo scafo. Le sue [tre fasi](#the-leaders-three-steps) e un’[abilità speciale](/wiki/03-Mechanics/Special-Abilities.md) possono cambiare questo.
- **Crystalys Guard**: un Crystalys più piccolo con la tinta dello sciame. I Guard restano vicini al boss, si uniscono allo scontro quando una nave di sciame vicina viene colpita, e ognuno che è vicino al boss ne cura lo scafo. Un Guard ripara il proprio scafo dopo una pausa, come fa un Crystalys.

## Come va lo scontro {#how-the-fight-goes}

- **Porta un grande gruppo.** In Alpha bastano sei piloti di livello 8 su Paragon con munizioni x2 se il suo fuoco si distribuisce tra loro, nove se va tutto su un solo pilota; con munizioni x4 sono cinque e sei. Più piloti chiudono lo scontro prima e perdono meno navi, e un pilota da solo viene distrutto.
- **Spara al boss, non ai Guard.** Un Guard cade in pochi secondi, ma ne arriva uno nuovo con la frequenza indicata nell’elenco *In breve*, e ciò che i Guard curano è una piccola parte di ciò che infligge un gruppo: lasciarli stare costa un po’ di tempo, dare loro la caccia ne costa di più.
- **Beta e Gamma sono più duri.** Gli sciami di quei mondi sono più forti ([Mondi](/wiki/05-Swarms/Swarms.md#the-worlds)), quindi servono più piloti o munizioni migliori.
- **I settori pericolosi sono PvP.** Un rivale può attaccare il gruppo in mezzo allo scontro e aspettare la cassa: è del pilota che ha inflitto più danno (e del suo clan) per 30 secondi, poi di chiunque ([Carico](/wiki/03-Mechanics/Cargo.md)). Non andare da solo.
- **Il boss ritorna** dopo il tempo indicato nell’elenco *In breve*, a piena forza, nello stesso settore, e i suoi Guard arrivano uno dopo l’altro.

## Le tre fasi del capo {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Il suo scontro ha tre fasi ([come funzionano](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); ognuna avviene una volta.

- **All’inizio**: Subisce solo 50% di ogni colpo per 8 s.
- **Sotto i due terzi**: Un anello di 700 unità colpisce ogni nave al suo interno con 4 delle sue raffiche, e spara 4 razzi.
- **Sotto un terzo**: Ripristina 20% del suo scafo e del suo scudo (una raffica di danni la interrompe), e arrivano 3 Crystalys Guards in più, al massimo 6 vivi.

<!-- mob-ladder:end -->

## Ricompense e bottino {#rewards-and-drops}

Il Boss Crystalys paga per lo scontro che è: un minuto di scontro con lui paga più di un minuto di scontro con un Crystalys, l’alieno meglio pagato. La ricompensa si divide in base al danno tra i piloti che lo hanno combattuto ([come paga l’abbattimento di un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). La sua cassa va al pilota che ha inflitto più danno e contiene Cataclysite e Quorvium, ogni tanto un Power Core, un’Ancient Control Unit o Dark Matter, munizioni x3 e x4 e razzi Epici. I Guard pagano poco e non lasciano nulla; abbatterli non è un buon farming, perché tornano insieme al boss.

## I valori {#the-numbers}

I valori delle navi dello sciame nei tre mondi ([Mondi](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- crystalys-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Crystalys

Base: Crystalys; rispetto all’originale, scafo 350% e danno dei laser 100%; velocità e portata sono quelle della nave di partenza.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | {{guide:vitals.hull@Boss Crystalys#1}} | {{guide:vitals.hull@Boss Crystalys#2}} | {{guide:vitals.hull@Boss Crystalys#3}} |
| Scudo | {{guide:vitals.shield@Boss Crystalys#1}} | {{guide:vitals.shield@Boss Crystalys#2}} | {{guide:vitals.shield@Boss Crystalys#3}} |
| Danno dei laser (una raffica al secondo) | {{guide:vitals.dps@Boss Crystalys#1}} | {{guide:vitals.dps@Boss Crystalys#2}} | {{guide:vitals.dps@Boss Crystalys#3}} |
| Velocità | {{guide:vitals.speed@Boss Crystalys#1}} | {{guide:vitals.speed@Boss Crystalys#2}} | {{guide:vitals.speed@Boss Crystalys#3}} |
| Portata dei laser | 900 | 900 | 900 |
| Raggio di aggressione | solo se attaccato | solo se attaccato | solo se attaccato |
| Crediti | {{guide:spoils.pay.credits@Boss Crystalys#1}} | {{guide:spoils.pay.credits@Boss Crystalys#2}} | {{guide:spoils.pay.credits@Boss Crystalys#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Crystalys#1}} | {{guide:spoils.pay.thulium@Boss Crystalys#2}} | {{guide:spoils.pay.thulium@Boss Crystalys#3}} |
| Esperienza (XP) | {{guide:spoils.pay.experience@Boss Crystalys#1}} | {{guide:spoils.pay.experience@Boss Crystalys#2}} | {{guide:spoils.pay.experience@Boss Crystalys#3}} |
| Onore | {{guide:spoils.pay.honor@Boss Crystalys#1}} | {{guide:spoils.pay.honor@Boss Crystalys#2}} | {{guide:spoils.pay.honor@Boss Crystalys#3}} |
| Punti PvE per abbattimento | 30 | 30 | 30 |

**Bottino**: una cassa, per il pilota che ha inflitto più danno.

| Oggetto |
| :--- |
| {{guide:spoils.box@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} |

### Crystalys Guard

Base: Crystalys, con il 15% di scafo, scudo e danno; velocità e portata sono quelle della nave di partenza.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | {{guide:vitals.hull@Crystalys Guard#1}} | {{guide:vitals.hull@Crystalys Guard#2}} | {{guide:vitals.hull@Crystalys Guard#3}} |
| Scudo | {{guide:vitals.shield@Crystalys Guard#1}} | {{guide:vitals.shield@Crystalys Guard#2}} | {{guide:vitals.shield@Crystalys Guard#3}} |
| Danno dei laser (una raffica al secondo) | {{guide:vitals.dps@Crystalys Guard#1}} | {{guide:vitals.dps@Crystalys Guard#2}} | {{guide:vitals.dps@Crystalys Guard#3}} |
| Velocità | {{guide:vitals.speed@Crystalys Guard#1}} | {{guide:vitals.speed@Crystalys Guard#2}} | {{guide:vitals.speed@Crystalys Guard#3}} |
| Portata dei laser | 900 | 900 | 900 |
| Raggio di aggressione | solo se attaccato | solo se attaccato | solo se attaccato |
| Cura il capo, ciascuno, al secondo (solo scafo) | 250 | 375 | 500 |
| Crediti | {{guide:spoils.pay.credits@Crystalys Guard#1}} | {{guide:spoils.pay.credits@Crystalys Guard#2}} | {{guide:spoils.pay.credits@Crystalys Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Crystalys Guard#1}} | {{guide:spoils.pay.thulium@Crystalys Guard#2}} | {{guide:spoils.pay.thulium@Crystalys Guard#3}} |
| Esperienza (XP) | {{guide:spoils.pay.experience@Crystalys Guard#1}} | {{guide:spoils.pay.experience@Crystalys Guard#2}} | {{guide:spoils.pay.experience@Crystalys Guard#3}} |
| Onore | {{guide:spoils.pay.honor@Crystalys Guard#1}} | {{guide:spoils.pay.honor@Crystalys Guard#2}} | {{guide:spoils.pay.honor@Crystalys Guard#3}} |
| Punti PvE per abbattimento | 6 | 6 | 6 |

**Bottino**: nessuno. L’abbattimento paga solo i suoi crediti, il Thulium, l’XP e l’onore.

<!-- crystalys-members:end -->
