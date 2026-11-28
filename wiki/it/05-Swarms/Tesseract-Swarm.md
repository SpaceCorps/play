<!-- wiki-i18n source: 98e91b2bd1dede81 -->
<!-- wiki-i18n title: Sciame Tesseract -->
# Sciame Tesseract {#tesseract-swarm}

Lo sciame Tesseract è un’unica enorme nave madre, il **Tesseract**, e i **Facet** che rilascia finché viene colpito. Il Tesseract vive in una posizione fissa del [settore pericoloso](/wiki/01-General/Danger-Sectors.md) `DS-4`, non ha armi proprie e non lascia mai il suo settore. È fatto per un gruppo molto grande dei piloti più forti: scafo e scudo superano di gran lunga un Crystalys, e si ripara da solo non appena viene lasciato in pace. I settori pericolosi sono settori PvP, quindi lo scontro può attirare rivali oltre ai Facet.

## In breve {#at-a-glance}

<!-- tesseract-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dove**: Il settore pericoloso `DS-4`
- **Quanti**: Uno in ogni mondo
- **Compare**: Dal giorno 4 della stagione fino al reset (Beta e Gamma: dal giorno 1 della stagione)
- **Capo**: Tesseract
- **Posizione**: Entro 2.500 unità dal punto 25.900, 11.900 della mappa del settore
- **Rigenerazione**: 125.000 HP al secondo in Alpha, prima lo scafo e poi lo scudo, dopo 5 s senza danni
- **Seguaci**: Fino a 100 × Facet, altri 20 ogni 5 s finché il capo viene colpito
- **Arrivo dei seguaci**: Solo finché il capo è stato colpito negli ultimi 5 s, entro 400 unità da lui
- **Cacciatori**: Ogni Facet vola tratti propri intorno al capo, entro 3.600 unità da lui, e non dà la caccia a nessuno. Spara al pilota più vicino che ha colpito il capo quando quel pilota è nel suo raggio. Senza nessuno a cui sparare continua a volare intorno al capo e se ne va 20 s dopo l’ultimo colpo
- **Capo distrutto**: I seguaci se ne vanno 1 min dopo la distruzione del capo, anche se stanno attaccando
- **Ritorna**: {{guide:vitals.respawn@Tesseract#1;Tesseract#2;Tesseract#3}} dopo la distruzione del capo, nello stesso settore
- **Avvisi**: I piloti del settore vengono avvisati quando il capo compare e quando viene distrutto. Sono righe di Sistema: compaiono nella scheda **Sistema** della chat, con un conteggio delle righe non lette, e non in **Globale** né in **Locale**. Il kill feed nomina il pilota a cui viene accreditato l’abbattimento.

<!-- tesseract-glance:end -->

## I membri {#the-members}

- **Tesseract**: una nave madre a forma di cubo, molte volte più grande di un Crystalys, di ferro forgiato scuro con venature di brace incandescenti e con il suo nome sopra. Una baia nella parete anteriore si apre mentre viene colpito, e un cubo luminoso ruota dentro una gabbia sul tetto. È passivo: si muove lentamente nella sua area finché nessuno lo ferisce, e appena un pilota lo colpisce si ferma e tiene la posizione. Non spara e non insegue nessuno; la sua difesa sono le dimensioni, la riparazione e i Facet che rilascia.
- **Facet**: una nave piccola e veloce dello stesso ferro scuro, con bordi incandescenti, una lente luminosa sul muso e due placche d’ala fluttuanti. Esiste solo finché il Tesseract viene colpito. Non insegue nessuno: resta vicino al Tesseract, vola brevi tratti propri verso punti casuali tutt’intorno e spara al pilota più vicino che ha colpito il Tesseract non appena uno è nel suo raggio. Se ne va quando il Tesseract viene lasciato in pace. È più veloce di qualsiasi nave, quindi scappare dallo sciame non serve, ma un pilota che resta lontano dal Tesseract non viene mai colpito.

## Come va lo scontro {#how-the-fight-goes}

- **Porta un gruppo molto grande e colpite insieme.** Scafo e scudo del Tesseract sono una riserva di milioni di punti, quindi lo scontro è lungo anche per un grande gruppo di navi forti, e la ricompensa si divide in base al danno: conta ogni pilota presente.
- **Non lasciarlo mai in pace.** Se nessuno lo ferisce per il tempo indicato nell’elenco *In breve*, ripara prima lo scafo e poi lo scudo a quella velocità, quindi una pausa di pochi secondi può cancellare un lungo minuto di lavoro. Un Tesseract completamente riparato dimentica chi lo ha ferito: ricompensa e bottino seguono il danno dello scontro che lo distrugge.
- **Ogni colpo chiama i Facet.** Finché il Tesseract viene colpito, ogni pochi secondi arriva vicino a lui un gruppo di Facet, fino al limite indicato nell’elenco *In breve*. Se nessuno lo colpisce non ne arriva nessuno, e quelli già presenti aspettano e se ne vanno.
- **I Facet volano tutt’intorno al Tesseract e sparano a chi è nel loro raggio.** Non danno la caccia a chi infligge più danno né a un pilota in particolare: ogni Facet vola brevi tratti propri verso punti casuali di un ampio anello intorno al Tesseract, in ogni direzione, e appena un pilota che ha colpito il Tesseract è nel suo raggio spara al più vicino di loro. Un gruppo che resta unito è nel raggio di meno Facet alla volta e ne divide il fuoco, a differenza di un gruppo sparso tutt’intorno al Tesseract. Un Facet ha poco scafo e poco scudo, e abbatterne uno paga quanto un [Phantasm](/wiki/04-Aliens/Phantasm.md), ma toglie una salva ai piloti vicini. Un pilota che non ha colpito il Tesseract non è il loro bersaglio.
- **Chi resta abbastanza lontano viene lasciato in pace.** I Facet non si allontanano mai dal Tesseract oltre la distanza indicata nell’elenco *In breve*; un pilota che resta oltre quella distanza e oltre il raggio del laser di un Facet non viene colpito, per quanto danno abbia inflitto. Un Facet senza nessuno a cui sparare continua a volare intorno al Tesseract e se ne va quando il Tesseract viene lasciato in pace.
- **Beta e Gamma sono più duri.** Gli sciami di quei mondi sono più forti ([Mondi](/wiki/05-Swarms/Swarms.md#the-worlds)), e lo sono anche la riparazione del Tesseract e la salva di ogni Facet.
- **I settori pericolosi sono PvP.** Un rivale può attaccare il gruppo in mezzo allo scontro. Non c’è nessuna cassa accanto al relitto da aspettare: il bottino è una [cassa privata](/wiki/03-Mechanics/Cargo.md#private-boxes) per ogni pilota pagato dall’abbattimento, che solo quel pilota può vedere e prendere. Non andare da solo.
- **Il Tesseract ritorna** dopo il tempo indicato nell’elenco *In breve*, a piena forza, nella sua posizione.

## Le tre fasi del capo {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Il suo scontro ha tre fasi ([come funzionano](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); ognuna avviene una volta, e ricominciano quando si è riparato del tutto.

- **Sotto i due terzi**: Arrivano 20 Facets in più in una volta, oltre il loro numero abituale.

<!-- mob-ladder:end -->

## Ricompense e bottino {#rewards-and-drops}

Il Tesseract paga per lo scontro che è: quanto molti Crystalys insieme, e più di un Crystalys, l’alieno meglio pagato, per il danno che incassa. La ricompensa si divide in base al danno tra i piloti che lo hanno combattuto ([come paga l’abbattimento di un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Non c’è nessuna cassa per il pilota che infligge più danno. Ogni pilota pagato dall’abbattimento riceve una propria [cassa privata](/wiki/03-Mechanics/Cargo.md#private-boxes), che solo lui vede e può prendere, per 10 minuti, con Reinforced Hull Plate, Velkonite e Orvium Reinforced Plate, Power Core, Ancient Control Unit e Dark Matter. Viene tirata per la sua parte di danno, come il bottino di un [Clan Warden](/wiki/03-Mechanics/Clans.md#warden-pay-and-loot): chi ha inflitto un quinto del danno riceve circa un quinto delle quantità della tabella, e in un gruppo ogni pilota riceve la sua parte di quella del gruppo, come viene divisa la ricompensa. La Dark Matter ha un tetto per pilota: da un abbattimento ne riceve al massimo 5, per quanto grande sia la sua parte (in un gruppo si separa prima la parte di ciascun pilota, e il tetto è quello di ognuno), e ciò che supera il tetto va perso, non viene dato agli altri. Un Facet paga quanto un [Phantasm](/wiki/04-Aliens/Phantasm.md) in Crediti, Thulium, XP e Onore, e il suo abbattimento conta come abbattimento (nelle tue statistiche, per gli obiettivi e per l’esperienza dei tuoi droni e P.E.T.), ma non lascia nulla e non dà punti PvE.

## I valori {#the-numbers}

I valori delle navi dello sciame nei tre mondi ([Mondi](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- tesseract-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Tesseract

Base: Crystalys, con 625% dello scafo; non ha armi, e scudo e velocità sono propri.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | {{guide:vitals.hull@Tesseract#1}} | {{guide:vitals.hull@Tesseract#2}} | {{guide:vitals.hull@Tesseract#3}} |
| Scudo | {{guide:vitals.shield@Tesseract#1}} | {{guide:vitals.shield@Tesseract#2}} | {{guide:vitals.shield@Tesseract#3}} |
| Danno dei laser (una raffica al secondo) | nessuno | nessuno | nessuno |
| Velocità | {{guide:vitals.speed@Tesseract#1}} | {{guide:vitals.speed@Tesseract#2}} | {{guide:vitals.speed@Tesseract#3}} |
| Portata dei laser | – | – | – |
| Raggio di aggressione | solo se attaccato | solo se attaccato | solo se attaccato |
| Ripara, al secondo, dopo 5 s senza danni (prima lo scafo, poi lo scudo) | 125.000 | 187.500 | 250.000 |
| Crediti | {{guide:spoils.pay.credits@Tesseract#1}} | {{guide:spoils.pay.credits@Tesseract#2}} | {{guide:spoils.pay.credits@Tesseract#3}} |
| Thulium | {{guide:spoils.pay.thulium@Tesseract#1}} | {{guide:spoils.pay.thulium@Tesseract#2}} | {{guide:spoils.pay.thulium@Tesseract#3}} |
| Esperienza (XP) | {{guide:spoils.pay.experience@Tesseract#1}} | {{guide:spoils.pay.experience@Tesseract#2}} | {{guide:spoils.pay.experience@Tesseract#3}} |
| Onore | {{guide:spoils.pay.honor@Tesseract#1}} | {{guide:spoils.pay.honor@Tesseract#2}} | {{guide:spoils.pay.honor@Tesseract#3}} |
| Punti PvE per abbattimento | 42 | 42 | 42 |

**Bottino per ogni pilota pagato dall’abbattimento**: una cassa ciascuno, solo per lui, con la sua parte di queste quantità.

| Oggetto |
| :--- |
| {{guide:spoils.box@Tesseract#1;Tesseract#2;Tesseract#3}} |

### Facet

Base: Seeker, con 2.500% dello scafo e 463% del danno dei laser; scudo, velocità e portata sono propri.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | {{guide:vitals.hull@Facet#1}} | {{guide:vitals.hull@Facet#2}} | {{guide:vitals.hull@Facet#3}} |
| Scudo | {{guide:vitals.shield@Facet#1}} | {{guide:vitals.shield@Facet#2}} | {{guide:vitals.shield@Facet#3}} |
| Danno dei laser (una raffica al secondo) | {{guide:vitals.dps@Facet#1}} | {{guide:vitals.dps@Facet#2}} | {{guide:vitals.dps@Facet#3}} |
| Velocità | {{guide:vitals.speed@Facet#1}} | {{guide:vitals.speed@Facet#2}} | {{guide:vitals.speed@Facet#3}} |
| Portata dei laser | 600 | 600 | 600 |
| Raggio di aggressione | solo se attaccato | solo se attaccato | solo se attaccato |
| Crediti | {{guide:spoils.pay.credits@Facet#1}} | {{guide:spoils.pay.credits@Facet#2}} | {{guide:spoils.pay.credits@Facet#3}} |
| Thulium | {{guide:spoils.pay.thulium@Facet#1}} | {{guide:spoils.pay.thulium@Facet#2}} | {{guide:spoils.pay.thulium@Facet#3}} |
| Esperienza (XP) | {{guide:spoils.pay.experience@Facet#1}} | {{guide:spoils.pay.experience@Facet#2}} | {{guide:spoils.pay.experience@Facet#3}} |
| Onore | {{guide:spoils.pay.honor@Facet#1}} | {{guide:spoils.pay.honor@Facet#2}} | {{guide:spoils.pay.honor@Facet#3}} |
| Punti PvE per abbattimento | 0 | 0 | 0 |

**Bottino**: nessuno. L’abbattimento paga solo i suoi crediti, il Thulium, l’XP e l’onore.

<!-- tesseract-members:end -->
