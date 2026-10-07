<!-- wiki-i18n source: 50c5c4d29dc44a89 -->
<!-- wiki-i18n title: Sciame Pirate -->
# Sciame Pirate {#pirate-swarm}

Lo sciame Pirate è un **Pirate Boss** con i suoi **Pirate Scout**: una nave enorme e lenta che non attacca nessuno e risponde con i razzi, e un branco di navi più veloci che la proteggono e la curano. Vive nei settori tra la base di una corporazione e il suo confine, dove si giocano i livelli intermedi del gioco, ed è uno scontro lungo per un gruppo di piloti, non un abbattimento rapido.

## In breve {#at-a-glance}

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dove**: I settori `x-2` e `x-3` di ogni corporazione
- **Quanti**: Uno in ciascuno di quei settori, 6 in ogni mondo
- **Compare**: Dal giorno 4 della stagione fino al reset
- **Capo**: Pirate Boss
- **Seguaci**: Fino a 5 × Pirate Scout, uno nuovo ogni 10 s
- **I seguaci restano vicini**: al massimo 900 unità dal capo
- **Cura**: Ogni Pirate Scout entro 600 unità dal capo ne cura lo scafo, 40 HP al secondo in Alpha
- **Capo distrutto**: I seguaci se ne vanno 1 min dopo la distruzione del capo, a meno che stiano attaccando
- **Ritorna**: 2 min dopo la distruzione del capo, nello stesso settore
- **Avvisi**: I piloti del settore vengono avvisati quando il capo compare e quando viene distrutto. Sono righe di Sistema: compaiono nella scheda **Sistema** della chat, con un conteggio delle righe non lette, e non in **Globale** né in **Locale**. Il kill feed nomina il pilota a cui viene accreditato l’abbattimento.

<!-- pirate-glance:end -->

## I membri {#the-members}

- **Pirate Boss**: una nave costruita sulla Ironclad, con una parte della sua forza (i valori sono qui sotto). È passivo e non spara **nessun laser**: la sua unica arma è un **razzo dritto** ([Razzi](/wiki/06-Items/Rockets.md); quale dipende dal settore, vedi la tabella) contro il pilota che lo ha attaccato, e continua a vagare mentre spara. Non ripara mai da solo il suo scafo.
- **Pirate Scout**: una nave costruita sulla Kitefin, con una parte della sua forza. Gli Scout attaccano qualsiasi pilota si avvicini, restano vicini al boss, e ognuno che è vicino al boss ne cura lo scafo.

## Come va lo scontro {#how-the-fight-goes}

- **Spara al boss, non agli Scout.** Gli Scout curano il boss, ma la cura è piccola rispetto al suo scafo, e un nuovo Scout arriva con la frequenza che dice l’elenco *In breve*: un gruppo che uccide prima gli Scout non li supera mai, e solo un gruppo molto grande può eliminarli e impiega comunque più tempo a finire il boss di uno che li ha lasciati stare. Gli Scout ti costano tempo, non decidono lo scontro.
- **Allontana gli Scout.** Uno Scout cura solo finché è alla portata del boss, quindi uno Scout che ti segue fuori portata non cura nulla, e un’Ostirion è più veloce di uno Scout.
- **Resta in movimento.** Il razzo del boss è dritto e non guidato: una nave che resta in movimento lo schiva, una ferma viene colpita.
- **Porta un gruppo.** Tre piloti su Ostirion con munizioni x2 possono abbatterlo in circa cinque minuti in Alpha, ma per poco e solo finché i colpi sono distribuiti: un trio che lascia a un pilota tutto il fuoco perde. Cinque lo abbattono in tre-quattro minuti; un’Ostirion da sola no, una Paragon da sola sì. Il boss risponde al primo pilota che lo ha colpito, quindi lascia cominciare la nave più robusta, e usa le tue abilità (Emergency Repair, Shield Surge: [Abilità](/wiki/03-Mechanics/Abilities.md)) in uno scontro così lungo. I piloti ancora di livello 2 o 3 sono troppo deboli per lui, anche dove volano: stai lontano finché non sei più forte.
- **Il boss ritorna** dopo il tempo indicato nell’elenco *In breve*, nello stesso settore.

## Ricompense e bottino {#rewards-and-drops}

Il Pirate Boss paga per lo scontro che è: un minuto di scontro con lui paga più di un minuto di scontro con un Goombah. La ricompensa si divide in base al danno tra i piloti che lo hanno combattuto ([come paga l’abbattimento di un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). La sua cassa è per il pilota che ha inflitto più danno e può contenere una **Reinforced Hull Plate**, razzi e munizioni. Gli Scout pagano poco e non lasciano nulla.

## I valori {#the-numbers}

I valori delle navi dello sciame nei tre mondi ([Mondi](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss

Base: Ironclad, con il 50% di scafo, scudo e danno; velocità e portata sono quelle della nave di partenza. Spara un razzo dritto ogni 5 s: [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) in `x-2`, [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) in `x-3`.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | 300.000 | 450.000 | 600.000 |
| Scudo | 50.100 | 75.150 | 100.200 |
| Danno dei laser (una raffica al secondo) | nessuno | nessuno | nessuno |
| Velocità | 92 | 92 | 92 |
| Portata dei laser | – | – | – |
| Raggio di aggressione | solo se attaccato | solo se attaccato | solo se attaccato |
| Danno dei razzi, al massimo | 2.500 (Rivet I) / 5.000 (Rivet II) | 3.750 (Rivet I) / 7.500 (Rivet II) | 5.000 (Rivet I) / 10.000 (Rivet II) |
| Crediti | 145.000 | 290.000 | 435.000 |
| Thulium | 725 | 1.450 | 2.175 |
| Esperienza (XP) | 29.000 | 58.000 | 87.000 |
| Onore | 232 | 464 | 696 |
| Punti PvE per abbattimento | 15 | 15 | 15 |

**Bottino**: una cassa, per il pilota che ha inflitto più danno.

| Oggetto | Probabilità | Quantità |
| :--- | ---: | ---: |
| Reinforced Hull Plate | 50% | 1 |
| Uno dei 8 [razzi](/wiki/06-Items/Rockets.md) acquistabili con i crediti, scelto a caso | 100% | 5–10 |
| Uno tra Advanced Plasma e Siphon Battery, scelto a caso | 100% | 500–1.000 |

### Pirate Scout

Base: Kitefin; rispetto all’originale, scafo 50% e danno dei laser 75%; velocità e portata sono quelle della nave di partenza.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | 12.000 | 18.000 | 24.000 |
| Scudo | 9.818 | 14.727 | 19.636 |
| Danno dei laser (una raffica al secondo) | 147 | 221 | 294 |
| Velocità | 175 | 175 | 175 |
| Portata dei laser | 700 | 700 | 700 |
| Raggio di aggressione | 700 | 700 | 700 |
| Cura il capo, ciascuno, al secondo (solo scafo) | 40 | 60 | 80 |
| Crediti | 1.000 | 2.000 | 3.000 |
| Thulium | 4 | 8 | 12 |
| Esperienza (XP) | 100 | 200 | 300 |
| Onore | 2 | 4 | 6 |
| Punti PvE per abbattimento | 4 | 4 | 4 |

**Bottino**: nessuno. L’abbattimento paga solo i suoi crediti, il Thulium, l’XP e l’onore.

<!-- pirate-members:end -->
