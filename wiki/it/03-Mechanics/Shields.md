<!-- wiki-i18n source: 815a7ed973fd7e50 -->
<!-- wiki-i18n title: Scudi -->
# Meccaniche degli scudi {#shield-mechanics}

Gli scudi assorbono la maggior parte del danno in arrivo e proteggono lo scafo della tua nave dai danni diretti.

## Calcolo degli scudi {#shield-calculations}

I parametri finali dello scudo della tua nave si calcolano così:

\[\text{Capacità finale dello scudo} = \text{Capacità base totale} \times (1,0 + \text{Percentuale totale del bonus scudo})\]
\[\text{Velocità di ricarica finale dello scudo} = \text{Ricarica base totale} \times (1,0 + \text{Percentuale totale del bonus scudo})\]

### 1. Efficienza degli slot e rendimenti decrescenti {#1-slot-efficiency-diminishing-returns}

Come per i motori, gli scudi equipaggiati (e i generatori ibridi) vengono ordinati per capacità e soggetti all’efficienza dello slot (principale: 100%, di supporto: 75%, ausiliario: 50%, lo slot di un drone: 100%, come uno slot principale) e a una curva di rendimenti decrescenti basata sulla loro posizione. Uno scudo su uno dei tuoi [droni](/wiki/03-Mechanics/Drones.md) viene classificato insieme a quelli della nave:

- **Dal 1º al 4º scudo**: **100%** (1,0) di efficienza marginale.
- **5º scudo**: **85%** (0,85) di efficienza marginale.
- **6º scudo**: **70%** (0,70) di efficienza marginale.
- **7º scudo**: **55%** (0,55) di efficienza marginale.
- **8º e oltre**: **50%** (0,50) di efficienza marginale. (Fino alla versione 0.4.7 era il 25%, come per i motori; i motori restano al 25%, vedi [Velocità](/wiki/03-Mechanics/Speed.md).)

**L’hangar lo mostra.** Uno scudo, un motore o un nucleo adattivo che non conta con tutta la sua forza porta una piccola percentuale sul suo slot (per esempio `64%`: il 5º scudo, all’85%, in uno slot di supporto, al 75%), e passandoci sopra il cursore compare il dettaglio. Passa il cursore sulle caselle Scudi e Velocità delle statistiche di combattimento per vedere i tuoi oggetti per posizione e quanto conterebbe uno in più. La finestra Nave in volo mostra le stesse liste quando passi il cursore sulla sua barra dello scudo e sulla velocità.

### 2. Assorbimento dello scudo (ripartizione del danno) {#2-shield-absorbance-damage-split-}

L’assorbimento è la quota di ogni colpo che viene presa dai tuoi scudi; il resto va direttamente ai punti scafo.
- **Per scudo**: l’assorbimento di uno scudo più quello delle celle scudo montate al suo interno. Uno scudo da solo ha **dal 45 al 50%** (Light 45%, Basic 48%, Heavy 50%); ogni cella aggiunge da 2 a 10 punti (Capacity Shield Cell da I a IV +2%, +3%, +4%, +5%; Absorption Shield Cell da I a IV +4%, +6%, +8%, +10%).
- **Assorbimento medio**: l’assorbimento della tua nave è la semplice media degli scudi negli slot principali, di supporto e ausiliari e sui tuoi droni. I Nuclei adattivi non hanno un assorbimento proprio e non contano nella media (le celle in un Nucleo adattivo aggiungono solo capacità e ricarica). Senza uno scudo equipaggiato il tuo assorbimento è 0%: lo scafo subisce ogni colpo, e i punti scudo delle celle in un Nucleo adattivo restano inutilizzati, quindi monta anche uno scudo.
- **Il massimo di serie è l’80%**: il miglior scudo con le migliori celle, un Heavy Shield Core con tre Absorption Shield Cell IV in ogni slot. Mescolare scudi più deboli abbassa la media. Nessun potenziamento dell’Emporio e nessun bonus della Forgia fa parte di quel numero.
- **Esempio**: un Basic Shield Core (48%) con due Absorption Shield Cell I fa il 56%; aggiungi un Light Shield Core (45%) e la media è 50,5%.
- **La statistica non ha un tetto del 100%.** È ciò che gli scudi prenderebbero di un colpo, prima che venga tolta la *penetrazione dello scudo* dell’attaccante, quindi una nave può arrivare oltre un colpo intero: con il 112% gli scudi prendono comunque un colpo intero da un attaccante con una penetrazione fino al 12%.

#### Penetrazione dello scudo {#shield-penetration}

Alcuni attacchi hanno una **penetrazione dello scudo**: punti che vengono tolti al tuo assorbimento per quel colpo. La quota che prendono i tuoi scudi è

\[\text{Quota dello scudo} = \text{clamp}(\text{Assorbimento} - \text{Penetrazione},\ 0,\ 100\%)\]

- Gli scudi prendono al massimo `round(damage x share)` del colpo; lo scafo prende il resto. Uno scudo troppo basso per la sua quota passa la differenza ai punti scafo, e se gli scudi sono a 0 tutto il danno colpisce direttamente i punti scafo.
- **Da dove viene la penetrazione**: dalla *penetrazione dello scudo* di un razzo diretto (Lancet I 10%, Lancet II 25%, Lancet III 35%, Rivet I 5%, Rivet II 25%, Rivet III 35%, N.I.K.E. 35%; le esplosioni ad area non ne hanno, vedi [Razzi](/wiki/06-Items/Rockets.md)) e da quella delle munizioni laser (Ultra Core 5%, Experimental Fusion Core 10%; vedi [Laser e munizioni](/wiki/06-Items/Lasers.md)). Gli alieni non ne hanno, e nemmeno le munizioni x1 e x2.
- **Esempi**: con un assorbimento dell’80% contro un Lancet III (35%) gli scudi prendono il 45% del colpo, lo scafo il 55%. Con il 100%: 65% e 35%. Con il 112% contro una penetrazione del 12%: tutto il colpo. Con il 45% (un Light Shield Core da solo) contro il 35%: il 10% sullo scudo, il resto sullo scafo. Nessun razzo penetra completamente un Light Shield Core.
- Gli alieni non hanno una statistica di assorbimento: ripartiscono ogni colpo 80% / 20%, meno la penetrazione del colpo.
- Il danno di una Siphon Battery esce solo dallo scudo: assorbimento e penetrazione non c’entrano.

#### Raggiungere e superare il 100% {#reaching-and-passing-100-}

- **Di serie**: al massimo l’80% (vedi sopra).
- **Shield Absorbance Boost**: un potenziamento permanente dell’Emporio acquistato con i punti reset, **+0,1 punti per livello, al massimo +10 punti** (100 livelli, 25 PR ciascuno). Aggiunge punti fissi all’assorbimento della tua nave, gli stessi su qualsiasi nave con uno scudo: l’80% diventa 80,4% con 4 livelli (100 PR), e il 45% di un Light Shield Core diventa 46,2% con 12 livelli (300 PR). Una nave senza scudo equipaggiato resta allo 0%. I 100 livelli costano 2.500 PR, un obiettivo da più reset: le fonti attuali di punti reset (i traguardi degli abbattimenti e le missioni) pagano in tutto 855 PR al loro massimo, portati da un reset all’altro, e con quelli si comprano 34 livelli, +3,4 punti. Sono previste altre fonti di punti reset. Vedi [Stagione e punti reset](/wiki/03-Mechanics/Wipe-Timeline.md#cross-season-progression-permanent-buffs-).
- **Forgia**: scudi e celle scudo possono ricevere un bonus di **assorbimento**, che moltiplica la statistica: +5% su uno scudo al 50% sono +2,5 punti. Il miglior set Eterno forgiato al massimo (nucleo e tre celle, ogni bonus uscito al valore più alto, +15%) aggiunge fino a 12 punti, circa 10 in media (vedi [La Forgia](/wiki/06-Items/Forge.md)).
- **Insieme**: l’80% di serie, +3,4 punti di potenziamento (tutti gli 855 punti reset di oggi) e fino a +12 punti di bonus della Forgia fanno **95,4%** al massimo oggi; con tutti i 100 livelli del potenziamento (+10 punti, 2.500 PR) sarebbe il 102%. Né il potenziamento né la Forgia da soli arrivano al 100%; raggiungerlo è un obiettivo da più reset, e sono previste altre fonti di punti reset.

### Bonus agli scudi: capacità, assorbimento, ricarica {#shield-boosts-capacity-absorbance-recharge}

Ogni bonus agli scudi aumenta una delle tre statistiche e compare sotto il proprio tipo nella finestra Booster:

- **Capacità** (punti scudo massimi): i booster Shield Wall e lo Shield Capacity Boost permanente.
- **Assorbimento** (la quota di un colpo che prendono i tuoi scudi): lo Shield Absorbance Boost permanente (+0,1 punti per livello, al massimo +10 punti).
- **Ricarica** (punti scudo ripristinati al secondo): il booster Shield Regen.

Per i numeri vedi [Booster](/wiki/06-Items/Boosters.md).

---

## Rigenerazione passiva dello scudo {#shield-passive-regeneration}

Gli scudi si rigenerano passivamente nel tempo per tenerti pronto al combattimento.

- **Impulso di rigenerazione**: se gli scudi sono sotto la capacità massima, ripristinano ogni secondo punti scudo pari alla tua velocità di ricarica.
- **Interruzione da combattimento (ritardo di 15 s)**: la rigenerazione si ferma quando subisci danni e riprende solo dopo **15 secondi** senza subirne.
