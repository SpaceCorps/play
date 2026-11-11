<!-- wiki-i18n source: 4d2749864875137f -->
<!-- wiki-i18n title: Porte solo -->
# Porte solo {#solo-gates}

<!-- wiki-search: solo gates; solo gate; gate; gates; galaxy gates; rift; rifts; alpha rift; beta breach; gamma foundry; delta siege; omega vault; chrono gate; chrono-gate; materializer; energy materializer; scan; spin; gate part; gate parts; guarantee; pity; consolation; wave; waves; nuke wave; skip; boss; lives; resume; abandon; speedrun; no death; challenge; achievement; thulium cap; porte solo; porta solo; porte galattiche; pezzo; pezzi; materializzatore di energia; giro; garanzia; ondata; ondate; vite; riprendi; abbandona; senza morire; sfida; obiettivo; limite di thulium -->

Le **porte solo** sono cinque porte delle Porte galattiche che piloti da solo: **Alpha Rift**, **Beta Breach**, **Gamma Foundry**, **Delta Siege** e **Omega Vault**. Ognuna è un’arena vuota tutta sua dove ondate di alieni ti vengono incontro una dopo l’altra e in fondo aspetta un boss. Costruisci una porta con i suoi **pezzi**, che trovi girando il Materializzatore di energia con il Thulium, e una vittoria paga Crediti, Thulium, esperienza, onore, minerale, piastre e munizioni.

Una porta solo non è un [dungeon di clan](/wiki/03-Mechanics/Dungeons.md). Un dungeon è un labirinto che un clan apre per un gruppo, con un Signore della guerra in fondo; una porta solo è un’arena in cui ci sei solo tu, e nessun altro può entrarvi con te. Le due hanno regole, pagamenti e limiti separati. La pagina delle Porte galattiche ha anche il **Chrono-Gate**, che non è un posto in cui volare ma la porta che apre il tuo [Deposito di trasporto](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) per il reset: i suoi pezzi si trovano con gli stessi giri.

## In breve {#at-a-glance}

<!-- solo-glance:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Porte**: 6: il Chrono-Gate e 5 porte solo, Alpha Rift, Beta Breach, Gamma Foundry, Delta Siege e Omega Vault
- **Giro**: 100 Thulium per giro, e 1, 5, 10 o 100 giri alla volta
- **Probabilità di un pezzo**: 13% a giro. La porta a cui appartiene il pezzo viene scelta a caso, e ogni porta riceve il 2,17% dei giri. Quando il Chrono-Gate è completo la sua quota esce dalla ruota, e le porte solo mantengono il 2,17% ciascuna
- **Garanzia**: Dopo 24 giri di fila senza pezzo la probabilità sale a ogni giro, e dopo 47 il giro successivo ne trova sempre uno. Un pezzo di qualsiasi porta fa ripartire il conteggio
- **Vite**: 3 per tentativo; ogni morte ne costa una
- **Conto alla rovescia**: 5 s prima di ogni ondata, anche la prima e quella del boss. Un’ondata non ha timer, e nemmeno una partita
- **Arena**: Spazio aperto di 8.000 × 6.000 unità senza rocce, e ci sei solo tu. Un mondo ne ha 16, e quando sono tutti occupati non puoi entrare
- **Alieni alla volta**: Al massimo 60 di un’ondata sono vivi alla volta, e 250 in un’ondata facoltativa. Gli altri aspettano spazio
- **Boss**: Un boss non può essere colpito per 3 s quando cambia fase
- **Limite di Thulium**: Una porta restituisce al massimo il 50% del Thulium che hai speso in giri. Il resto viene tagliato, e il risultato dice quanto

<!-- solo-glance:end -->

## Trovare i pezzi delle porte {#finding-gate-parts}

Apri la pagina delle **Porte galattiche** e gira il Materializzatore di energia. Ogni giro si paga in Thulium e trova al massimo un pezzo, e il pezzo appartiene a una delle sei porte, scelta a caso. Servono un certo numero di pezzi di una porta per costruirla, e i pezzi sono tuoi finché non li usi. Un giro che non trova alcun pezzo non è perso: paga un premio ([sotto](#a-spin-without-a-part)). Ogni giro si paga, anche con il Chrono-Gate completo. Quando il Chrono-Gate è completo la sua quota dei giri non trova nulla, e le porte solo mantengono la propria probabilità, quindi un pezzo di una porta solo costa lo stesso con o senza di esso.

La tabella dà il costo di ogni porta in pezzi e quanto costano in media **con la garanzia** (un giro è una lotteria, quindi un pilota fortunato paga meno e uno sfortunato di più, fino alla serie di giri più lunga che la garanzia consente).

<!-- solo-parts:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Porta | Pezzi per completarla | Probabilità di un pezzo per giro | Giri in media | Thulium in media |
| :--- | ---: | ---: | ---: | ---: |
| **Chrono-Gate** | 2 | 2,17% | 91 | 9.093 |
| **Alpha Rift** | 11 | 2,17% | 500 | 50.011 |
| **Beta Breach** | 26 | 2,17% | 1.182 | 118.208 |
| **Gamma Foundry** | 54 | 2,17% | 2.455 | 245.508 |
| **Delta Siege** | 87 | 2,17% | 3.955 | 395.541 |
| **Omega Vault** | 108 | 2,17% | 4.910 | 491.017 |

<!-- solo-parts:end -->

I pezzi del Chrono-Gate tornano a zero al reset, e li ritrovi a ogni stagione. **I pezzi delle porte solo restano**, e restano anche il conteggio della garanzia e il registro di ciò che hai speso in giri e di ciò che le porte hanno restituito; il reset non ne toglie nessuno ([Porte e reset](#gates-and-the-wipe)).

### Un giro senza pezzo {#a-spin-without-a-part}

La maggior parte dei giri non trova alcun pezzo. Ognuno di essi paga un premio, scelto secondo le probabilità qui sotto: munizioni laser del secondo moltiplicatore o migliori, una scorta di razzi del secondo o terzo livello e, di tanto in tanto, un [oggetto speciale](/wiki/06-Items/Special-Items.md) o un [contenitore](/wiki/06-Items/Containers.md). Un premio che non può essere dato (hai già il massimo di quell’oggetto speciale, ad esempio) diventa una scorta di munizioni o di razzi con lo stesso tiro, quindi un giro non paga mai meno della sua tabella. Il premio vale chiaramente meno di quanto costa il giro: le porte sono un pozzo di Thulium.

<!-- solo-prizes:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Premio | Probabilità per giro |
| :--- | ---: |
| Un contenitore: Chroma Archive | 0,01% |
| Un oggetto speciale: Magic Hammer | 0,2% |
| Un oggetto speciale: Schematics | 0,2% |
| Un oggetto speciale: Philosopher's Stone | 0,2% |
| Un oggetto speciale: Forger's Seal | 0,2% |
| Un oggetto speciale: Workforce Contract | 0,2% |
| Un oggetto speciale: Tinkerer's Badge | 0,1% |
| Munizioni laser: Advanced Plasma ×75 | 12,88% |
| Munizioni laser: Antimatter Battery I ×62 | 8,59% |
| Munizioni laser: Ultra Core ×40 | 8,59% |
| Munizioni laser: Antimatter Battery II ×29 | 4,29% |
| Munizioni laser: Dark Matter Ammo I ×31 | 4,29% |
| Munizioni laser: Experimental Fusion Core ×17 | 2,15% |
| Munizioni laser: Dark Matter Ammo II ×17 | 2,15% |
| Razzi: Lancet II ×4 | 8,59% |
| Razzi: Rivet II ×4 | 8,59% |
| Razzi: Ember II ×4 | 8,59% |
| Razzi: Scatter II ×4 | 8,59% |
| Razzi: Lancet III ×1 | 2,15% |
| Razzi: Rivet III ×1 | 2,15% |
| Razzi: Ember III ×1 | 2,15% |
| Razzi: Scatter III ×1 | 2,15% |

<!-- solo-prizes:end -->

## Entrare {#going-in}

**Costruisci** una porta dalla pagina delle Porte galattiche e **salti** dentro dal suo portale. Si costruisce dalla stazione, con la nave attraccata: non devi essere in volo. Servono:

- i pezzi della porta: vengono presi **una sola volta, quando la costruisci**, e una costruzione rifiutata non toglie nulla;
- nessun’altra partita solo aperta: hai una partita alla volta, e una partita che hai lasciato si rientra dal suo portale o si abbandona prima che tu costruisca un’altra porta;
- il server principale (i server regionali non hanno porte).

La porta costruita sta nel tuo **settore base** (`M-1`, `T-1` o `G-1`, secondo la tua corporazione) come un portale che porta il suo nome, e la pagina delle Porte galattiche dice dove si trova. **Decolla, vola fino al portale e salta** come in qualsiasi portale. Un varco deve essere libero nel tuo mondo quando entri: ogni mondo ne ha un certo numero, e quando sono tutti occupati aspetti.

Atterri da solo in mezzo a un’arena vuota. Nessuno può attaccarti al suo interno, e la Jump CPU e la Base CPU non funzionano.

## Come si svolge una partita {#how-a-run-goes}

1. **Prima di ogni ondata c’è un conto alla rovescia**, anche prima della prima e prima di quella del boss. Un’ondata non ha timer, e nemmeno la partita: dura quanto ti serve.
2. **Un’ondata** appare su un anello intorno a te e ti vola incontro, al ritmo della porta. Ne vive solo un certo numero alla volta, e il resto aspetta spazio. Finisce quando muore il suo ultimo alieno.
3. **I tuoi progressi vengono salvati dopo ogni ondata.** Se esci, un’ondata in corso ricomincia da capo quando torni.
4. **Un’ondata facoltativa** è un’enorme ondata di Seeker, e Delta Siege e Omega Vault ne hanno una ciascuna. Durante il suo conto alla rovescia puoi saltarla: conta allora come fatta e **non paga nulla**. Se la combatti, le sue uccisioni pagano come quelle di qualsiasi ondata.
5. **L’ultima ondata è il boss.** Cambia fase man mano che il suo scafo cala, e a ogni cambio non può essere colpito per un attimo. Quando il boss muore la partita è vinta, e la vittoria viene pagata subito.

**Vite.** Una morte costa una vita e ti manda alla tua base come qualsiasi altra morte; la partita ti aspetta, senza orologio che corre. Finché la partita è aperta e sei fuori dall’arena, **il portale della tua porta sta nel tuo settore base**, e un salto attraverso di esso ti riporta all’ondata salvata con le vite che ti restano, come **Riprendi**; non chiede nuovi pezzi. Quando la tua ultima vita è finita il tentativo termina ma la partita resta aperta all’ultima ondata superata, e rientrare ti rende le vite. **Esci**, una disconnessione o un cambio di mondo mette in pausa la partita senza costare una vita. Anche il riavvio del server mantiene aperta la tua partita. **Abbandona** rinuncia alla partita: i suoi pezzi sono persi, e gli alieni che hai ucciso vengono pagati così come sono. **Riprendi** funziona solo da una nave in volo: dopo una morte il suo pulsante nella schermata del risultato aspetta, con una riga che dice perché, finché non hai fatto respawn. Una nave che fa respawn torna con lo scafo limitato, quindi quando il tuo scafo è sotto la metà la schermata del risultato ti avvisa; **Riprendi** ti riporta comunque così come sei. Le navi riparatrici della tua base ti riparano dentro la loro aura.

Ogni mondo combatte la stessa porta: la forza e il pagamento degli alieni non dipendono dal mondo in cui voli.

### Le ondate {#the-waves}

Gli alieni sono quelli del gioco (Seeker, Phantasm, Bulwark, Goombah e Crystalys), resi più duri o più morbidi dalla porta. Il tempo previsto è quello che la porta è costruita per richiedere a un pilota al livello iniziale della Tecnica laser ([Competenze del pilota](/wiki/03-Mechanics/Pilot-Skills.md)); un pilota che ha fatto salire la Tecnica laser finisce prima.

<!-- solo-waves:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Porta | Ondate, quella del boss compresa | Alieni nelle ondate | Boss | Tempo previsto |
| :--- | ---: | :--- | :--- | :--- |
| **Alpha Rift** | 10 | 60 Seeker, 160 Phantasm | Enhanced Phantasm | da 10 a 15 min |
| **Beta Breach** | 14 | 80 Seeker, 180 Phantasm, 80 Bulwark, 20 Goombah | Enhanced Bulwark | da 15 a 25 min |
| **Gamma Foundry** | 18 | 100 Phantasm, 120 Bulwark, 100 Goombah, 8 Crystalys | Elite Crystalys | da 25 a 35 min |
| **Delta Siege** | 22 | 250 Seeker, 200 Phantasm, 180 Bulwark, 140 Goombah, 15 Crystalys | Siege Construct | da 35 a 45 min |
| **Omega Vault** | 26 | 250 Seeker, 250 Phantasm, 200 Bulwark, 200 Goombah, 25 Crystalys | Omega Guardian | da 50 a 60 min |

- **Delta Siege**: l’ondata 18 (250 Seeker) è facoltativa: puoi saltarla mentre corre il suo conto alla rovescia, e non paga nulla
- **Omega Vault**: l’ondata 17 (250 Seeker) è facoltativa: puoi saltarla mentre corre il suo conto alla rovescia, e non paga nulla; le ondate da 22 a 24 sono d’élite, con ×1,5 di scafo, scudo e danno

<!-- solo-waves:end -->

### I boss {#the-bosses}

Un boss è la nave di un alieno ingrandita, con uno scafo, uno scudo e una raffica suoi, che nessuna impostazione della porta o del mondo cambia. Una fase inizia quando lo scafo del boss scende alla cifra della tabella: il suo scudo può essere reimpostato, la sua raffica o tutto il suo danno cambiano, e può iniziare una mossa. Ogni mossa è annunciata: un cerchio, un anello o un segno sulla tua nave la mostra un attimo prima che colpisca. Gli alieni che un boss chiama non pagano né lasciano nulla.

<!-- solo-bosses:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Boss | Porta | Scafo | Scudo | Raffica laser |
| :--- | :--- | ---: | ---: | ---: |
| **Enhanced Phantasm** | Alpha Rift | 330.000 | 530.000 | 5.700–7.000 |
| **Enhanced Bulwark** | Beta Breach | 690.000 | 170.000 | 4.500–5.500 |
| **Elite Crystalys** | Gamma Foundry | 620.000 | 250.000 | 3.800–4.700 |
| **Siege Construct** | Delta Siege | 1.150.000 | 1.730.000 | 3.400–4.200 |
| **Omega Guardian** | Omega Vault | 1.340.000 | 840.000 | 2.600–3.200 |

| Boss | Fase | Scafo rimasto | Cosa fa |
| :--- | :--- | :--- | :--- |
| **Enhanced Phantasm** | Enhanced Phantasm | da 100% a 0% | Si limita a sparare. |
| **Enhanced Bulwark** | Shielded | da 100% a 50% | Il suo scudo è impostato a ×4 di quello proprio del boss. |
|  | Second attack | da 50% a 0% | La sua raffica è ×1,3. Ti spara 4 razzi Dormant Lance, da 61.000 ciascuno, uno ogni 0,5 s, in una salva ogni 30 s. |
| **Elite Crystalys** | Elite | da 100% a 50% | Si limita a sparare. |
|  | Reinforced | da 50% a 0% | Il suo scudo è impostato a ×2 di quello proprio del boss. Ogni 10 min chiama 10 Goombah, al massimo 10 vivi; non pagano né lasciano nulla. |
| **Siege Construct** | Siege Construct | da 100% a 0% | Ogni 1 min fa cadere 3 salve di 8 meteore, da 5.500 ciascuna su tutto ciò che si trova entro 420 unità dal punto in cui cade, 50% delle quali puntate su di te; ogni cerchio compare 3 s prima di cadere. Ti spara 6 razzi Dormant Lance, da 9.000 ciascuno, uno ogni 0,5 s, in una salva ogni 1 min. |
| **Omega Guardian** | Shield Fortress | da 100% a 70% | Il suo scudo è impostato a ×1,5 di quello proprio del boss. Ogni 40 s chiama 6 Bulwark, al massimo 12 vivi; non pagano né lasciano nulla. |
|  | Swarm Protocol | da 70% a 35% | Ogni 25 s chiama 12 Phantasm, al massimo 24 vivi; non pagano né lasciano nulla. Ogni 30 s un’esplosione da 140.000 colpisce tutto ciò che si trova entro 700 unità dal boss; l’anello compare 2 s prima di cadere. |
|  | Overload | da 35% a 0% | Il suo scudo è impostato a ×0,1 di quello proprio del boss. Tutto il suo danno è ×2,5. Dopo 2 min nella fase tutto il suo danno è ancora ×2. Ogni 25 s un’esplosione da 28.000 colpisce tutto ciò che si trova entro 700 unità dal boss; l’anello compare 2 s prima di cadere. |

<!-- solo-bosses:end -->

## Cosa paga una vittoria {#what-a-clear-pays}

Una vittoria paga la sua tabella **una volta**, in un colpo solo, nel momento in cui il boss muore: i Crediti, il Thulium, l’esperienza e l’onore, il minerale, le piastre e i Power Core, e le munizioni. L’esperienza conta per i tuoi punti classifica PvE, come quella di un dungeon.

<!-- solo-pay:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Porta | Crediti | Thulium | XP | Onore |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 450.000 | 5.000 | 70.000 | 1.000 |
| **Beta Breach** | 1.500.000 | 12.000 | 180.000 | 2.500 |
| **Gamma Foundry** | 4.000.000 | 25.000 | 400.000 | 5.500 |
| **Delta Siege** | 8.000.000 | 40.000 | 800.000 | 10.000 |
| **Omega Vault** | 15.000.000 | 60.000 | 1.500.000 | 20.000 |

- **Alpha Rift**: Ship Fragment ×300, Nyxite ×300, Daraxium ×400; munizioni: Advanced Plasma ×20.000, Ultra Core ×5.000, Experimental Fusion Core ×20.000
- **Beta Breach**: Ship Fragment ×700, Nyxite ×750, Daraxium ×800, Cataclysite ×400, Quorvium ×100; munizioni: Advanced Plasma ×50.000, Ultra Core ×20.000, Experimental Fusion Core ×30.000
- **Gamma Foundry**: Ship Fragment ×1.150, Nyxite ×1.000, Cataclysite ×900, Quorvium ×400, Power Core ×15; munizioni: Advanced Plasma ×30.000, Ultra Core ×60.000, Experimental Fusion Core ×50.000
- **Delta Siege**: Ship Fragment ×2.000, Nyxite ×1.750, Cataclysite ×1.500, Quorvium ×1.000, Reinforced Hull Plate ×70, Power Core ×40, Ancient Control Unit ×3; munizioni: Advanced Plasma ×40.000, Ultra Core ×90.000, Experimental Fusion Core ×75.000
- **Omega Vault**: Ship Fragment ×3.250, Nyxite ×2.750, Cataclysite ×2.250, Quorvium ×1.600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10; munizioni: Advanced Plasma ×50.000, Ultra Core ×100.000, Experimental Fusion Core ×100.000

<!-- solo-pay:end -->

**Il Thulium è tagliato a un limite.** Le porte non possono restituire più di una quota del Thulium che hai speso in giri, contata su tutte le tue porte e tutti i tuoi giri (la quota è nell’elenco in cima). Ciò che una vittoria e i suoi alieni pagherebbero oltre viene tagliato, e la schermata del risultato dice quanto. Crediti, esperienza, onore, minerale, piastre e munizioni non vengono mai tagliati.

### Gli alieni {#the-aliens}

Ogni alieno che uccidi in una porta paga alle cifre che ha in Alpha, qualunque mondo tu stia volando: nessun moltiplicatore del mondo, nessun booster e nessun bonus Premium le cambia. Un’ondata paga per i suoi alieni **una volta** per partita, per quante volte tu esca e rientri. Il pagamento arriva alla fine di ogni tratto della partita: quando esci, muori, finisci le vite, abbandoni o vinci. Le uccisioni di un tratto restano non pagate solo con il reset e con un riavvio del server mentre sei dentro (la tua partita resta aperta, ma le uccisioni di quel tratto vanno perse). Le uccisioni di una porta non contano per nient’altro: non per le missioni, le statistiche delle uccisioni, i contatori degli obiettivi, il kill feed o l’esperienza dei tuoi droni e P.E.T. L’esperienza che pagano conta invece per i tuoi punti classifica PvE, come quella di una vittoria. Il bottino degli alieni arriva con il pagamento, direttamente nel tuo inventario.

<!-- solo-kills:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Alieno | Crediti | Thulium | XP | Onore |
| :--- | ---: | ---: | ---: | ---: |
| **Seeker** | 1.000 | 4 | 100 | 2 |
| **Phantasm** | 3.000 | 12 | 300 | 6 |
| **Bulwark** | 5.000 | 25 | 800 | 10 |
| **Goombah** | 15.000 | 75 | 3.000 | 24 |
| **Crystalys** | 75.000 | 200 | 12.000 | 52 |

| Porta | Crediti | Thulium | XP | Onore |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 540.000 | 2.160 | 54.000 | 1.080 |
| **Beta Breach** | 1.320.000 | 5.980 | 186.000 | 2.520 |
| **Gamma Foundry** | 3.000.000 | 13.300 | 522.000 | 4.616 |
| **Delta Siege** | 4.975.000 | 21.400 | 829.000 | 7.640 |
| **Omega Vault** | 6.875.000 | 29.000 | 1.160.000 | 10.100 |

<!-- solo-kills:end -->

## Sfide e obiettivi {#challenges-and-achievements}

Due sfide facoltative possono essere vinte a ogni vittoria, e ognuna paga un obiettivo e **nessun Thulium**. Una vittoria **senza morire** è una senza alcuna morte in tutta la partita, su tutte le volte che sei entrato. Una **speedrun** è una vittoria entro il tempo previsto più breve della porta, contato dal tempo che passi dentro l’arena. Gli altri sei obiettivi sono per aver vinto ogni porta, e tutte e cinque:

<!-- solo-achievements:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Fenditura chiusa** (Comune): Completa da solo l’Alpha Rift.
- **Breccia sigillata** (Non comune): Completa da solo il Beta Breach.
- **Fonderia fermata** (Raro): Completa da solo la Gamma Foundry.
- **Assedio spezzato** (Raro): Spezza da solo il Delta Siege.
- **Caveau scassinato** (Epico): Scassina da solo l’Omega Vault.
- **Custode delle porte** (Leggendario): Completa tutte e cinque le porte singole: Alpha, Beta, Gamma, Delta e Omega.
- **Intoccabile** (Raro): Completa una porta singola senza perdere una vita.
- **Contro il tempo** (Raro): Completa una porta singola nel suo tempo più breve o meno: 10, 15, 25, 35 o 50 minuti, da Alpha a Omega.

<!-- solo-achievements:end -->

## Oggetti di una porta {#items-from-a-gate}

Ciò che una porta ti dà è **commerciabile**: il minerale, le piastre, i Power Core, le munizioni e il bottino degli alieni possono essere messi in vendita all’[Asta](/wiki/03-Mechanics/Auction.md) come un drop o una ricompensa di missione, con le stesse eccezioni di qualsiasi oggetto. I premi di un giro senza pezzo non lo sono: vengono da un giro, non da una porta.

## Porte e reset {#gates-and-the-wipe}

- **Il reset termina ogni partita aperta** e ti restituisce i suoi pezzi. Una partita non prosegue nella stagione successiva.
- **Conservati attraverso il reset:** i pezzi delle cinque porte solo, il conteggio della garanzia e il registro di ciò che hai speso in giri e di ciò che le porte hanno restituito, così il limite del Thulium prosegue di stagione in stagione. Gli obiettivi sono tuoi per sempre.
- **Persi al reset:** i pezzi del Chrono-Gate, come prima. I tuoi giri li ricomprano.
- **Eliminare un account** elimina i pezzi, il conteggio e il registro.
