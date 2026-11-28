<!-- wiki-i18n source: 33448f95d2520b3a -->
<!-- wiki-i18n title: Sciame Pirate -->
# Sciame Pirate {#pirate-swarm}

Lo sciame Pirate è un **Pirate Boss** con i suoi **Pirate Scout**: una nave enorme e lenta che non attacca nessuno e risponde con i razzi, e un branco di navi più veloci che la proteggono e la curano. Vive nei settori tra la base di una corporazione e il suo confine, dove si giocano i livelli intermedi del gioco, ed è uno scontro lungo per un gruppo di piloti, non un abbattimento rapido.

## In breve {#at-a-glance}

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dove**: I settori `x-2` e `x-3` di ogni corporazione
- **Quanti**: Uno in ciascuno di quei settori, 6 in ogni mondo
- **Compare**: Dal giorno 4 della stagione fino al reset (Beta e Gamma: dal giorno 1 della stagione)
- **Capo**: Pirate Boss
- **Seguaci**: Fino a 5 × Pirate Scout, uno nuovo ogni 10 s
- **I seguaci restano vicini**: al massimo 900 unità dal capo
- **Cura**: Ogni Pirate Scout entro 600 unità dal capo ne cura lo scafo, 40 HP al secondo in Alpha
- **Capo distrutto**: I seguaci se ne vanno 1 min dopo la distruzione del capo, a meno che stiano attaccando
- **Ritorna**: {{guide:vitals.respawn@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} dopo la distruzione del capo, nello stesso settore
- **Avvisi**: I piloti del settore vengono avvisati quando il capo compare e quando viene distrutto. Sono righe di Sistema: compaiono nella scheda **Sistema** della chat, con un conteggio delle righe non lette, e non in **Globale** né in **Locale**. Il kill feed nomina il pilota a cui viene accreditato l’abbattimento.

<!-- pirate-glance:end -->

## I membri {#the-members}

- **Pirate Boss**: una nave costruita sulla Ironclad, con una parte della sua forza (i valori sono qui sotto). È passivo e non spara **nessun laser**: la sua unica arma è un **razzo dritto** ([Razzi](/wiki/06-Items/Rockets.md); quale dipende dal settore, vedi la tabella) contro il pilota che lo ha attaccato, e continua a vagare mentre spara. Non ripara mai da solo il suo scafo. Le sue [tre fasi](#the-leaders-three-steps) e un’[abilità speciale](/wiki/03-Mechanics/Special-Abilities.md) possono cambiare questo.
- **Pirate Scout**: una nave costruita sulla Kitefin, con una parte della sua forza. Gli Scout attaccano qualsiasi pilota si avvicini, restano vicini al boss, e ognuno che è vicino al boss ne cura lo scafo.

## Come va lo scontro {#how-the-fight-goes}

- **Spara al boss, non agli Scout.** Gli Scout curano il boss, ma la cura è piccola rispetto al suo scafo, e un nuovo Scout arriva con la frequenza che dice l’elenco *In breve*: un gruppo che uccide prima gli Scout non li supera mai, e solo un gruppo molto grande può eliminarli e impiega comunque più tempo a finire il boss di uno che li ha lasciati stare. Gli Scout ti costano tempo, non decidono lo scontro.
- **Allontana gli Scout.** Uno Scout cura solo finché è alla portata del boss, quindi uno Scout che ti segue fuori portata non cura nulla, e un’Ostirion è più veloce di uno Scout.
- **Resta in movimento.** Il razzo del boss è dritto e non guidato: una nave che resta in movimento lo schiva, una ferma viene colpita.
- **Porta un gruppo.** Tre piloti su Ostirion con munizioni x2 lo vincono su `x-2` senza perdere una nave, anche se di poco, e vengono distrutti su `x-3`, anche finché i colpi sono distribuiti; quattro lo abbattono in circa tre minuti in Alpha. Con munizioni x4 tre lo abbattono su `x-3` in circa due minuti. Cinque lo abbattono in circa due minuti e mezzo quando i colpi sono distribuiti e in circa tre quando un pilota prende tutto il fuoco, e allora perdono due navi: un gruppo che lascia a un pilota tutto il fuoco ne richiede cinque. In Beta servono cinque piloti e in Gamma sette, con i colpi distribuiti (il boss lì è più grande e i suoi Scout curano di più). In Alpha, su `x-3` con munizioni x2, un’Ostirion da sola non ce la fa, una Paragon da sola non ce la fa neppure, e due Paragon ce la fanno senza rischi. In Beta e Gamma, su `x-3`, una Paragon da sola viene distrutta con munizioni x2 e con munizioni x4. Il boss risponde al primo pilota che lo ha colpito, quindi lascia cominciare la nave più robusta, e usa le tue abilità (Emergency Repair, Shield Surge: [Abilità](/wiki/03-Mechanics/Abilities.md)) in uno scontro così lungo. I piloti ancora di livello 2 o 3 sono troppo deboli per lui, anche dove volano: stai lontano finché non sei più forte.
- **Il boss ritorna** dopo il tempo indicato nell’elenco *In breve*, nello stesso settore.

## Le tre fasi del capo {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Il suo scontro ha tre fasi ([come funzionano](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); ognuna avviene una volta.

- **All’inizio**: Spara un ventaglio di 3 razzi, distanziati di 12 gradi, contro il primo pilota che l’ha colpito.
- **Sotto i due terzi**: Chiama 5 Pirate Scouts in più in una volta, al massimo 10 vivi. Non pagano nulla e se ne vanno dopo 45 s.
- **Sotto un terzo**: Vola a velocità ×1,8 verso la porta più vicina per 10 s, poi si rivolta contro i piloti.

<!-- mob-ladder:end -->

## Ricompense e bottino {#rewards-and-drops}

Il Pirate Boss paga per lo scontro che è: un minuto di scontro con lui paga più di un minuto di scontro con un Goombah. La ricompensa si divide in base al danno tra i piloti che lo hanno combattuto ([come paga l’abbattimento di un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). La sua cassa è per il pilota che ha inflitto più danno e può contenere una **Reinforced Hull Plate**, razzi e munizioni. La sua cassa vale poco meno della metà di ciò che paga l’abbattimento stesso. Gli Scout pagano poco e non lasciano nulla.

## I valori {#the-numbers}

I valori delle navi dello sciame nei tre mondi ([Mondi](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss

Base: Ironclad, con il 50% di scafo, scudo e danno; velocità e portata sono quelle della nave di partenza. Spara un razzo dritto ogni 5 s: [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) in `x-2`, [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) in `x-3`.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | {{guide:vitals.hull@Pirate Boss#1}} | {{guide:vitals.hull@Pirate Boss#2}} | {{guide:vitals.hull@Pirate Boss#3}} |
| Scudo | {{guide:vitals.shield@Pirate Boss#1}} | {{guide:vitals.shield@Pirate Boss#2}} | {{guide:vitals.shield@Pirate Boss#3}} |
| Danno dei laser (una raffica al secondo) | nessuno | nessuno | nessuno |
| Velocità | {{guide:vitals.speed@Pirate Boss#1}} | {{guide:vitals.speed@Pirate Boss#2}} | {{guide:vitals.speed@Pirate Boss#3}} |
| Portata dei laser | – | – | – |
| Raggio di aggressione | solo se attaccato | solo se attaccato | solo se attaccato |
| Danno dei razzi, al massimo | {{guide:behaviour.ability:rocket.damage@Pirate Boss#1}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#2}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#3}} |
| Crediti | {{guide:spoils.pay.credits@Pirate Boss#1}} | {{guide:spoils.pay.credits@Pirate Boss#2}} | {{guide:spoils.pay.credits@Pirate Boss#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Boss#1}} | {{guide:spoils.pay.thulium@Pirate Boss#2}} | {{guide:spoils.pay.thulium@Pirate Boss#3}} |
| Esperienza (XP) | {{guide:spoils.pay.experience@Pirate Boss#1}} | {{guide:spoils.pay.experience@Pirate Boss#2}} | {{guide:spoils.pay.experience@Pirate Boss#3}} |
| Onore | {{guide:spoils.pay.honor@Pirate Boss#1}} | {{guide:spoils.pay.honor@Pirate Boss#2}} | {{guide:spoils.pay.honor@Pirate Boss#3}} |
| Punti PvE per abbattimento | 15 | 15 | 15 |

**Bottino**: una cassa, per il pilota che ha inflitto più danno.

| Oggetto |
| :--- |
| {{guide:spoils.box@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} |

### Pirate Scout

Base: Kitefin; rispetto all’originale, scafo 50% e danno dei laser 113%; velocità e portata sono quelle della nave di partenza.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | {{guide:vitals.hull@Pirate Scout#1}} | {{guide:vitals.hull@Pirate Scout#2}} | {{guide:vitals.hull@Pirate Scout#3}} |
| Scudo | {{guide:vitals.shield@Pirate Scout#1}} | {{guide:vitals.shield@Pirate Scout#2}} | {{guide:vitals.shield@Pirate Scout#3}} |
| Danno dei laser (una raffica al secondo) | {{guide:vitals.dps@Pirate Scout#1}} | {{guide:vitals.dps@Pirate Scout#2}} | {{guide:vitals.dps@Pirate Scout#3}} |
| Velocità | {{guide:vitals.speed@Pirate Scout#1}} | {{guide:vitals.speed@Pirate Scout#2}} | {{guide:vitals.speed@Pirate Scout#3}} |
| Portata dei laser | 700 | 700 | 700 |
| Raggio di aggressione | {{guide:vitals.aggro@Pirate Scout#1}} | {{guide:vitals.aggro@Pirate Scout#2}} | {{guide:vitals.aggro@Pirate Scout#3}} |
| Cura il capo, ciascuno, al secondo (solo scafo) | 40 | 60 | 80 |
| Crediti | {{guide:spoils.pay.credits@Pirate Scout#1}} | {{guide:spoils.pay.credits@Pirate Scout#2}} | {{guide:spoils.pay.credits@Pirate Scout#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Scout#1}} | {{guide:spoils.pay.thulium@Pirate Scout#2}} | {{guide:spoils.pay.thulium@Pirate Scout#3}} |
| Esperienza (XP) | {{guide:spoils.pay.experience@Pirate Scout#1}} | {{guide:spoils.pay.experience@Pirate Scout#2}} | {{guide:spoils.pay.experience@Pirate Scout#3}} |
| Onore | {{guide:spoils.pay.honor@Pirate Scout#1}} | {{guide:spoils.pay.honor@Pirate Scout#2}} | {{guide:spoils.pay.honor@Pirate Scout#3}} |
| Punti PvE per abbattimento | 4 | 4 | 4 |

**Bottino**: nessuno. L’abbattimento paga solo i suoi crediti, il Thulium, l’XP e l’onore.

<!-- pirate-members:end -->
