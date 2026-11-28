<!-- wiki-i18n source: b4ceac9f501a1ec2 -->
<!-- wiki-i18n title: Porte solo -->
# Porte solo {#solo-gates}

<!-- wiki-search: solo gates; solo gate; gate; gates; galaxy gates; rift; rifts; alpha rift; beta breach; gamma foundry; delta siege; omega vault; chrono gate; chrono-gate; materializer; energy materializer; scan; spin; gate part; gate parts; guarantee; pity; consolation; wave; waves; nuke wave; skip; boss; lives; resume; abandon; speedrun; no death; challenge; achievement; thulium cap; davidski's nightmare; nightmare; evil davidski; angry davidski; evil ships; golden ships; porte solo; porta solo; porte galattiche; pezzo; pezzi; materializzatore di energia; giro; garanzia; ondata; ondate; vite; riprendi; abbandona; senza morire; sfida; obiettivo; limite di thulium; navi evil; navi dorate; davidski furioso -->

Le **porte solo** sono cinque porte delle Porte galattiche che piloti da solo: **Alpha Rift**, **Beta Breach**, **Gamma Foundry**, **Delta Siege** e **Omega Vault**. Ognuna è un’arena vuota tutta sua dove ondate di alieni ti vengono incontro una dopo l’altra e in fondo aspetta un boss. **Davidski's Nightmare** è una sesta porta, a parte rispetto a quelle cinque: le sue ondate non sono di alieni ma di **navi Evil**, navi del gioco che volano contro di te, ed è la porta più costosa da costruire. Costruisci una porta con i suoi **pezzi**, che trovi girando il Materializzatore di energia con il Thulium, e una vittoria paga Crediti, Thulium, esperienza, onore, minerale, piastre e munizioni.

Una porta solo non è un [dungeon di clan](/wiki/03-Mechanics/Dungeons.md). Un dungeon è un labirinto che un clan apre per un gruppo, con un Signore della guerra in fondo; una porta solo è un’arena in cui ci sei solo tu, e nessun altro può entrarvi con te. Le due hanno regole, pagamenti e limiti separati. La pagina delle Porte galattiche ha anche il **Chrono-Gate**, che non è un posto in cui volare ma la porta che apre il tuo [Deposito di trasporto](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) per il reset: i suoi pezzi si trovano con gli stessi giri.

## In breve {#at-a-glance}

<!-- solo-glance:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Porte**: 7: il Chrono-Gate e 6 porte solo, Alpha Rift, Beta Breach, Gamma Foundry, Delta Siege, Omega Vault e Davidski's Nightmare
- **Giro**: 100 Thulium per giro, e 1, 5, 10, 100 o 1.000 giri alla volta
- **Probabilità di un pezzo**: 13% a giro, in qualunque categoria giri. Il pezzo appartiene a una delle porte di quella categoria, tutte ugualmente probabili: il Chrono-Gate da solo prende tutto, Alpha Rift, Beta Breach e Gamma Foundry prendono il 4,33% ciascuna e Delta Siege e Omega Vault prendono il 6,5% ciascuna. Quando il Chrono-Gate è completo, nella sua categoria non c’è più nulla da girare
- **Garanzia**: Dopo 24 giri di fila senza pezzo la probabilità sale a ogni giro, e dopo 47 il giro successivo ne trova sempre uno. Un pezzo di qualsiasi porta fa ripartire il conteggio
- **Vite**: 3 per tentativo; ogni morte ne costa una
- **Conto alla rovescia**: 5 s prima di ogni ondata, anche la prima e quella del boss. Un’ondata non ha timer, e nemmeno una partita
- **Arena**: Spazio aperto di 8.000 × 6.000 unità senza rocce, e ci sei solo tu. Un mondo ne ha 16, e quando sono tutti occupati non puoi entrare
- **Alieni alla volta**: Al massimo 60 di un’ondata sono vivi alla volta, e 250 in un’ondata facoltativa. Gli altri aspettano spazio
- **Boss**: Un boss non può essere colpito per 3 s quando cambia fase
- **Limite di Thulium**: Una porta restituisce al massimo il 50% del Thulium che hai speso in giri. Il resto viene tagliato, e il risultato dice quanto

<!-- solo-glance:end -->

## Trovare i pezzi delle porte {#finding-gate-parts}

Apri la pagina delle **Porte galattiche** e gira il Materializzatore di energia. Ogni giro si paga in Thulium e trova al massimo un pezzo. Scegli prima una **categoria**: il **Chrono-Gate**, **Alpha–Gamma** (Alpha Rift, Beta Breach e Gamma Foundry), **Delta–Omega** (Delta Siege e Omega Vault) oppure **Davidski's Nightmare**, che ha una categoria tutta per sé. La probabilità di un pezzo è la stessa in ogni categoria, e il pezzo appartiene a una delle porte della categoria scelta, tutte ugualmente probabili. Servono un certo numero di pezzi di una porta per costruirla, e i pezzi sono tuoi finché non li usi. Un giro che non trova alcun pezzo non è perso: paga un premio ([sotto](#a-spin-without-a-part)). Ogni giro si paga. Quando il Chrono-Gate è completo la sua voce è chiusa, perché non c’è più nulla da trovare, e le altre due categorie mantengono la loro probabilità, quindi un pezzo di una porta solo costa lo stesso con o senza di esso.

La tabella dà il costo di ogni porta in pezzi e quanto costano in media **con la garanzia** quando giri la categoria in cui si trova la porta (un giro è una lotteria, quindi un pilota fortunato paga meno e uno sfortunato di più, fino alla serie di giri più lunga che la garanzia consente).

<!-- solo-parts:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Porta | Pezzi per completarla | Probabilità di un pezzo per giro | Giri in media | Thulium in media |
| :--- | ---: | ---: | ---: | ---: |
| **Chrono-Gate** | 13 | 13% | 99 | 9.851 |
| **Alpha Rift** | 14 | 4,33% | 318 | 31.825 |
| **Beta Breach** | 33 | 4,33% | 750 | 75.016 |
| **Gamma Foundry** | 68 | 4,33% | 1.546 | 154.579 |
| **Delta Siege** | 96 | 6,5% | 1.455 | 145.486 |
| **Omega Vault** | 119 | 6,5% | 1.803 | 180.343 |
| **Davidski's Nightmare** | 238 | 13% | 1.803 | 180.343 |

<!-- solo-parts:end -->

I pezzi del Chrono-Gate tornano a zero al reset, e li ritrovi a ogni stagione. **I pezzi delle porte solo restano**, e restano anche il conteggio della garanzia e il registro di ciò che hai speso in giri e di ciò che le porte hanno restituito; il reset non ne toglie nessuno ([Porte e reset](#gates-and-the-wipe)).

### Un giro senza pezzo {#a-spin-without-a-part}

La maggior parte dei giri non trova alcun pezzo. Ognuno di essi paga un premio, scelto secondo le probabilità qui sotto: munizioni laser del secondo moltiplicatore o migliori, una scorta di razzi del secondo o terzo livello e, di tanto in tanto, un [oggetto speciale](/wiki/06-Items/Special-Items.md) o un [contenitore](/wiki/06-Items/Containers.md). Un premio che non può essere dato (gli oggetti speciali o i contenitori sono disattivati, ad esempio) diventa una scorta di munizioni o di razzi con lo stesso tiro, quindi un giro non paga mai meno della sua tabella. Il premio vale chiaramente meno di quanto costa il giro: le porte sono un pozzo di Thulium.

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

**Costruisci** una porta dalla pagina delle Porte galattiche e **salti** dentro dal suo portale. Si costruisce dalla stazione, con la nave attraccata, e anche in volo: la **finestra delle Porte galattiche**, che il pulsante delle porte della barra degli strumenti apre, gira, costruisce e sceglie la destinazione come la pagina. Servono:

- i pezzi della porta: vengono presi **una sola volta, quando la costruisci**, e una costruzione rifiutata non toglie nulla;
- la porta non ancora costruita: puoi avere **tutte** le porte costruite insieme, con un portale per ciascuna, e ne giochi una alla volta; una porta già costruita si rientra dal suo portale o si abbandona prima di costruirla di nuovo;
- il server principale (una porta si costruisce solo sul server principale: su un server regionale torni prima alla base).

La porta costruita sta nel tuo **settore base** (`M-1`, `T-1` o `G-1`, secondo la tua corporazione) come un portale che porta il suo nome, e la pagina delle Porte galattiche dice dove si trova. **Decolla, vola fino al portale e salta** come in qualsiasi portale. Un varco deve essere libero nel tuo mondo quando entri: ogni mondo ne ha un certo numero, e quando sono tutti occupati aspetti. Vedi solo le **tue** porte: i portali delle porte di altri piloti nello stesso settore non ti vengono mostrati. Puoi avere **tutte e cinque le porte costruite insieme**, ciascuna con il suo portale, e ne giochi una alla volta: **mentre sei in un’arena non c’è nessuno dei tuoi portali**, e tornano quando esci.

**Sui server regionali (Singapore, US East).** Una porta costruita si gioca anche lì. Il suo portale sta nel tuo settore base su un server regionale come sul server principale, e te lo dicono quando arrivi. **Saltaci dentro e entri in un’arena di quel server**, con la sua latenza invece di quella del server principale. Un server regionale ha solo **due arene per mondo**, contro molte di più sul server principale: quando sono entrambe occupate aspetti, come aspetti un varco libero sul server principale. Il server principale resta l’unico posto che tiene la tua partita, i tuoi pezzi e il tuo pagamento: il pagamento arriva nel tuo portafoglio quando il server principale ha contato la partita, pochi secondi dopo la fine, e il **portafoglio della tua finestra di volo si aggiorna quando attracchi**. Entri nella partita successiva solo quando l’ultima è stata contata. Una partita che lasci nell’arena si riprende dal portale; per abbandonarla lo fai nell’arena o alla stazione. Se l’arena di un server regionale è disattivata, il suo portale ti riporta invece al server principale, dove decolli verso la tua porta come sopra. Che cos’altro funziona su un server regionale è descritto in [Server](/wiki/03-Mechanics/Servers.md).

Atterri da solo in mezzo a un’arena vuota. Nessuno può attaccarti al suo interno, e la Jump CPU e la Base CPU non funzionano.

## Come si svolge una partita {#how-a-run-goes}

1. **Prima di ogni ondata c’è un conto alla rovescia**, anche prima della prima e prima di quella del boss. Un’ondata non ha timer, e nemmeno la partita: dura quanto ti serve.
2. **Un’ondata** appare su un anello intorno a te e ti vola incontro, al ritmo della porta. Ne vive solo un certo numero alla volta, e il resto aspetta spazio. Finisce quando muore il suo ultimo alieno.
3. **I tuoi progressi vengono salvati dopo ogni ondata.** Se esci, un’ondata in corso ricomincia da capo quando torni.
4. **Un’ondata facoltativa** è un’enorme ondata di Seeker, e Delta Siege e Omega Vault ne hanno una ciascuna. Durante il suo conto alla rovescia puoi saltarla: conta allora come fatta e **non paga nulla**. Se la combatti, le sue uccisioni pagano come quelle di qualsiasi ondata.
5. **L’ultima ondata è il boss.** Cambia fase man mano che il suo scafo cala, e a ogni cambio non può essere colpito per un attimo. Quando il boss muore la partita è vinta, e la vittoria viene pagata subito.

**Vite.** Una morte costa una vita e ti manda alla tua base come qualsiasi altra morte; la partita ti aspetta, senza orologio che corre. Finché la partita è aperta e sei fuori dall’arena, **il portale di ogni porta che hai costruito sta nel tuo settore base**, e un salto attraverso uno di essi ti riporta all’ondata salvata con le vite che ti restano, come **Riprendi**; non chiede nuovi pezzi. Quando la tua ultima vita è finita il tentativo termina ma la partita resta aperta all’ultima ondata superata, e rientrare ti rende le vite. **Esci**, una disconnessione o un cambio di mondo mette in pausa la partita senza costare una vita. Anche il riavvio del server mantiene aperta la tua partita. **Abbandona** rinuncia alla partita: i suoi pezzi sono persi, e gli alieni che hai ucciso vengono pagati così come sono. **Riprendi** funziona solo da una nave in volo: dopo una morte il suo pulsante nella schermata del risultato aspetta, con una riga che dice perché, finché non hai fatto respawn. Una nave che fa respawn torna con lo scafo limitato, quindi quando il tuo scafo è sotto la metà la schermata del risultato ti avvisa; **Riprendi** ti riporta comunque così come sei. Le navi riparatrici della tua base ti riparano dentro la loro aura.

Ogni mondo combatte la stessa porta: la forza e il pagamento degli alieni non dipendono dal mondo in cui voli.

### Le ondate {#the-waves}

Gli alieni sono quelli del gioco (Seeker, Phantasm, Bulwark, Goombah e Crystalys), resi più duri o più morbidi dalla porta. Le ondate di **Davidski's Nightmare** sono invece di **navi Evil**: una per ogni scafo che un pilota può pilotare, con la livrea dello Sciame Dormant. Gli scafi piccoli vengono per primi, e ogni ondata ne porta di più e più grandi, fino all’ultima ondata prima del boss. Una nave Evil porta ciò che porta la nave di un pilota: laser, un **razzo** che ti spara ogni pochi secondi e un **drone di riparazione** che ripara il suo scafo finché nulla lo colpisce, quindi una nave che lasci in pace si cura. Il tempo previsto è quello che la porta è costruita per richiedere a un pilota al livello iniziale della Tecnica laser ([Competenze del pilota](/wiki/03-Mechanics/Pilot-Skills.md)); un pilota che ha fatto salire la Tecnica laser finisce prima.

Alcune ondate portano uno **sciame**: un boss NPC del gioco (un Boss Seeker, Boss Phantasm, Boss Goombah o Boss Crystalys) con le sue guardie, che attaccano come un unico gruppo. Ogni nave di uno sciame fa parte della sua ondata, e l’ondata finisce quando l’ultima di loro è morta. Pagano come le altre navi dell’ondata, con le cifre della [tabella degli alieni](#the-aliens). **Un boss NPC lascia il suo bottino come nei settori del gioco**: minerale, piastre, munizioni e razzi (cosa lascia ciascuno è nelle [pagine degli sciami](/wiki/05-Swarms/Swarms.md)). In una porta non c’è nessuna cassa da raccogliere: il bottino arriva con il pagamento, direttamente nel tuo inventario, e una sola volta per partita, come il pagamento. Le sue guardie non lasciano nulla, nella porta come nei settori, e non lo curano né tornano. La tabella qui sotto dice quali ondate di ogni porta portano uno sciame.

<!-- solo-waves:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Porta | Ondate, quella del boss compresa | Alieni nelle ondate | Boss NPC e sciami | Boss | Tempo previsto |
| :--- | ---: | :--- | :--- | :--- | :--- |
| **Alpha Rift** | 10 | 44 Seeker, 140 Phantasm | ondata 5: 1 Seeker Swarm, 1 Phantasm Swarm | Enhanced Phantasm | da 10 a 15 min |
| **Beta Breach** | 14 | 64 Seeker, 158 Phantasm, 80 Bulwark, 20 Goombah | ondata 4: 2 Seeker Swarm; ondata 9: 1 Phantasm Swarm | Enhanced Bulwark | da 15 a 25 min |
| **Gamma Foundry** | 18 | 78 Phantasm, 117 Bulwark, 91 Goombah, 8 Crystalys | ondata 4: 1 Phantasm Swarm; ondata 9: 1 Goombah Swarm; ondata 14: 1 Goombah Swarm | Elite Crystalys | da 25 a 35 min |
| **Delta Siege** | 22 | 250 Seeker, 200 Phantasm, 141 Bulwark, 130 Goombah, 12 Crystalys | ondata 5: 2 Phantasm Swarm; ondata 10: 2 Goombah Swarm; ondata 15: 1 Goombah Swarm; ondata 20: 1 Crystalys Swarm | Siege Construct | da 35 a 45 min |
| **Omega Vault** | 26 | 250 Seeker, 236 Phantasm, 170 Bulwark, 174 Goombah, 25 Crystalys | ondata 6: 1 Goombah Swarm; ondata 11: 2 Goombah Swarm; ondata 16: 1 Crystalys Swarm; ondata 22: 1 Phantasm Swarm | Omega Guardian | da 50 a 60 min |
| **Davidski's Nightmare** | 13 | 50 Evil Protos, 66 Evil Kitefin, 31 Evil Ostirion, 19 Evil Nomad, 22 Evil Paragon, 7 Evil Storm, 8 Evil Wraith, 2 Evil Ironclad |  | Evil Davidski | da 45 a 60 min |

- **Delta Siege**: l’ondata 18 (250 Seeker) è facoltativa: puoi saltarla mentre corre il suo conto alla rovescia, e non paga nulla
- **Omega Vault**: l’ondata 17 (250 Seeker) è facoltativa: puoi saltarla mentre corre il suo conto alla rovescia, e non paga nulla; le ondate da 22 a 24 sono d’élite, con ×1,5 di scafo, scudo e danno

<!-- solo-waves:end -->

### I boss {#the-bosses}

Un boss è la nave di un alieno ingrandita, con uno scafo, uno scudo e una raffica suoi, che nessuna impostazione della porta o del mondo cambia. Una fase inizia quando lo scafo del boss scende alla cifra della tabella: il suo scudo può essere reimpostato, la sua raffica o tutto il suo danno cambiano, e può iniziare una mossa. Ogni mossa è annunciata: un cerchio, un anello o un segno sulla tua nave la mostra un attimo prima che colpisca. Gli alieni che un boss chiama non pagano né lasciano nulla.

**Evil Davidski**, il boss di Davidski's Nightmare, pilota l’Ironclad di Davidski stesso in un oro più scuro. Spara Dormant Lance, razzi guidati che ti seguono per un lungo tratto, e combatte con meteore, un anello e navi Evil che chiama. A un terzo dello scafo diventa **DAVIDSKI FURIOSO**: parte la sua musica, colpisce più forte e intorno a lui compare una **nave dorata di ogni nave del gioco**. Finché una qualsiasi delle navi dorate è viva non può essere ferito affatto: i tuoi laser e i tuoi razzi non possono agganciarlo e nulla di ciò che fai tocca il suo scafo o il suo scudo, quindi prima ti apri la strada tra loro. Quando cade l’ultima, la protezione sparisce per sempre. Ti deride dalla sua finestra all’inizio di ogni ondata. Ucciderlo conta come un’uccisione di Davidski per le missioni che ne chiedono una, in una porta come nei Settori pericolosi. Un gioco non aggiornato non mostra la porta.

<!-- solo-bosses:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Boss | Porta | Scafo | Scudo | Raffica laser |
| :--- | :--- | ---: | ---: | ---: |
| **Enhanced Phantasm** | Alpha Rift | {{guide:vitals.hull@Enhanced Phantasm}} | {{guide:vitals.shield@Enhanced Phantasm}} | {{guide:vitals.dps*0.9007633587786259~1.099236641221374@Enhanced Phantasm}} |
| **Enhanced Bulwark** | Beta Breach | {{guide:vitals.hull@Enhanced Bulwark}} | {{guide:vitals.shield@Enhanced Bulwark}} | {{guide:vitals.dps*0.9019607843137255~1.0980392156862746@Enhanced Bulwark}} |
| **Elite Crystalys** | Gamma Foundry | {{guide:vitals.hull@Elite Crystalys}} | {{guide:vitals.shield@Elite Crystalys}} | {{guide:vitals.dps*0.896551724137931~1.103448275862069@Elite Crystalys}} |
| **Siege Construct** | Delta Siege | {{guide:vitals.hull@Siege Construct}} | {{guide:vitals.shield@Siege Construct}} | {{guide:vitals.dps*0.8974358974358975~1.1025641025641026@Siege Construct}} |
| **Omega Guardian** | Omega Vault | {{guide:vitals.hull@Omega Guardian}} | {{guide:vitals.shield@Omega Guardian}} | {{guide:vitals.dps*0.896551724137931~1.103448275862069@Omega Guardian}} |
| **Evil Davidski** | Davidski's Nightmare | {{guide:vitals.hull@Evil Davidski}} | {{guide:vitals.shield@Evil Davidski}} | {{guide:vitals.dps*0.896551724137931~1.103448275862069@Evil Davidski}} |

| Boss | Fase | Scafo rimasto | Cosa fa |
| :--- | :--- | :--- | :--- |
| **Enhanced Phantasm** | Enhanced Phantasm | da 100% a 66% | Si limita a sparare. |
|  | Reinforced | da 66% a 33% | Il suo scudo è impostato a ×1 di quello proprio del boss. Ogni 10 min chiama 4 Phantasm, al massimo 4 vivi; non pagano né lasciano nulla. |
|  | Second attack | da 33% a 0% | La sua raffica è ×1,3. Ogni 30 s un’esplosione da {{guide:behaviour.ability:phases.ringBlast@Enhanced Phantasm}} colpisce tutto ciò che si trova entro 500 unità dal boss; l’anello compare 2 s prima di cadere. |
| **Enhanced Bulwark** | Shielded | da 100% a 66% | Il suo scudo è impostato a ×4 di quello proprio del boss. |
|  | Rocket barrage | da 66% a 33% | Ti spara 4 razzi Dormant Lance, da {{guide:behaviour.ability:phases.rocketBarrage@Enhanced Bulwark}} ciascuno, uno ogni 0,5 s, in una salva ogni 30 s. |
|  | Second attack | da 33% a 0% | La sua raffica è ×1,3. Ogni 10 min chiama 4 Phantasm, al massimo 4 vivi; non pagano né lasciano nulla. |
| **Elite Crystalys** | Elite | da 100% a 66% | Si limita a sparare. |
|  | Renewed shield | da 66% a 33% | Il suo scudo è impostato a ×1 di quello proprio del boss. |
|  | Reinforced | da 33% a 0% | Il suo scudo è impostato a ×2 di quello proprio del boss. Ogni 10 min chiama 10 Goombah, al massimo 10 vivi; non pagano né lasciano nulla. |
| **Siege Construct** | Siege Construct | da 100% a 66% | Ogni 1 min fa cadere 3 salve di 8 meteore, da {{guide:behaviour.ability:phases.meteors@Siege Construct}} ciascuna su tutto ciò che si trova entro 420 unità dal punto in cui cade, 50% delle quali puntate su di te; ogni cerchio compare 3 s prima di cadere. |
|  | Rocket barrage | da 66% a 33% | Ogni 1 min fa cadere 3 salve di 8 meteore, da {{guide:behaviour.ability:phases.meteors2@Siege Construct}} ciascuna su tutto ciò che si trova entro 420 unità dal punto in cui cade, 50% delle quali puntate su di te; ogni cerchio compare 3 s prima di cadere. Ti spara 6 razzi Dormant Lance, da {{guide:behaviour.ability:phases.rocketBarrage@Siege Construct}} ciascuno, uno ogni 0,5 s, in una salva ogni 1 min. |
|  | Frenzy | da 33% a 0% | Ogni 30 s fa cadere 3 salve di 8 meteore, da {{guide:behaviour.ability:phases.meteors3@Siege Construct}} ciascuna su tutto ciò che si trova entro 420 unità dal punto in cui cade, 50% delle quali puntate su di te; ogni cerchio compare 3 s prima di cadere. Ti spara 6 razzi Dormant Lance, da {{guide:behaviour.ability:phases.rocketBarrage2@Siege Construct}} ciascuno, uno ogni 0,5 s, in una salva ogni 30 s. |
| **Omega Guardian** | Shield Fortress | da 100% a 66% | Il suo scudo è impostato a ×1,5 di quello proprio del boss. Ogni 40 s chiama 6 Bulwark, al massimo 12 vivi; non pagano né lasciano nulla. |
|  | Swarm Protocol | da 66% a 33% | Ogni 25 s chiama 12 Phantasm, al massimo 24 vivi; non pagano né lasciano nulla. Ogni 30 s un’esplosione da {{guide:behaviour.ability:phases.ringBlast@Omega Guardian}} colpisce tutto ciò che si trova entro 700 unità dal boss; l’anello compare 2 s prima di cadere. |
|  | Overload | da 33% a 0% | Il suo scudo è impostato a ×0,1 di quello proprio del boss. Tutto il suo danno è ×2,5. Dopo 2 min nella fase tutto il suo danno è ancora ×2. Ogni 25 s un’esplosione da {{guide:behaviour.ability:phases.ringBlast2@Omega Guardian}} colpisce tutto ciò che si trova entro 700 unità dal boss; l’anello compare 2 s prima di cadere. |
| **Evil Davidski** | Evil Davidski | da 100% a 66% | Si limita a sparare. |
|  | Davidski attacks | da 66% a 33% | Ti spara 6 razzi Dormant Lance, da {{guide:behaviour.ability:phases.rocketBarrage@Evil Davidski}} ciascuno, uno ogni 0,5 s, in una salva ogni 30 s. Ogni 1 min fa cadere 2 salve di 8 meteore, da {{guide:behaviour.ability:phases.meteors@Evil Davidski}} ciascuna su tutto ciò che si trova entro 400 unità dal punto in cui cade, 50% delle quali puntate su di te; ogni cerchio compare 3 s prima di cadere. Ogni 40 s chiama 5 Evil Protos, al massimo 10 vivi; non pagano né lasciano nulla. |
|  | Angry | da 33% a 0% | Il suo scudo è impostato a ×0,5 di quello proprio del boss. Tutto il suo danno è ×1,5. Dopo 8 min nella fase tutto il suo danno è ancora ×2. Ti spara 6 razzi Dormant Lance, da {{guide:behaviour.ability:phases.rocketBarrage2@Evil Davidski}} ciascuno, uno ogni 0,4 s, in una salva ogni 30 s. Ogni 1 min fa cadere 3 salve di 8 meteore, da {{guide:behaviour.ability:phases.meteors2@Evil Davidski}} ciascuna su tutto ciò che si trova entro 420 unità dal punto in cui cade, 50% delle quali puntate su di te; ogni cerchio compare 3 s prima di cadere. Ogni 45 s un’esplosione da {{guide:behaviour.ability:phases.ringBlast@Evil Davidski}} colpisce tutto ciò che si trova entro 700 unità dal boss; l’anello compare 2 s prima di cadere. Ogni 40 s chiama 3 Evil Kitefin, al massimo 6 vivi; non pagano né lasciano nulla. |

<!-- solo-bosses:end -->

## Cosa paga una vittoria {#what-a-clear-pays}

Una vittoria paga la sua tabella **una volta**, in un colpo solo, nel momento in cui il boss muore: i Crediti, il Thulium, l’esperienza e l’onore, il minerale, le piastre e i Power Core, e le munizioni. L’esperienza e l’onore contano per i tuoi punti classifica PvE, come quelli di un dungeon.

<!-- solo-pay:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Porta | Crediti | Thulium | XP | Onore |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 450.000 | 5.000 | 70.000 | 1.000 |
| **Beta Breach** | 1.500.000 | 12.000 | 180.000 | 2.500 |
| **Gamma Foundry** | 4.000.000 | 25.000 | 400.000 | 5.500 |
| **Delta Siege** | 8.000.000 | 40.000 | 800.000 | 10.000 |
| **Omega Vault** | 15.000.000 | 60.000 | 1.500.000 | 20.000 |
| **Davidski's Nightmare** | 15.000.000 | 60.000 | 1.500.000 | 20.000 |

- **Alpha Rift**: Ship Fragment ×300, Nyxite ×300, Daraxium ×400, Echo Shard ×4, Lattice Shard ×6; munizioni: Advanced Plasma ×15.000, Ultra Core ×3.750, Experimental Fusion Core ×15.000
- **Beta Breach**: Ship Fragment ×700, Nyxite ×750, Daraxium ×800, Cataclysite ×400, Quorvium ×100, Echo Shard ×9, Lattice Shard ×13; munizioni: Advanced Plasma ×37.500, Ultra Core ×15.000, Experimental Fusion Core ×22.500
- **Gamma Foundry**: Ship Fragment ×1.150, Nyxite ×1.000, Cataclysite ×900, Quorvium ×400, Power Core ×15, Echo Shard ×18, Lattice Shard ×27; munizioni: Advanced Plasma ×22.500, Ultra Core ×45.000, Experimental Fusion Core ×37.500
- **Delta Siege**: Ship Fragment ×2.000, Nyxite ×1.750, Cataclysite ×1.500, Quorvium ×1.000, Reinforced Hull Plate ×70, Power Core ×40, Ancient Control Unit ×3, Echo Shard ×29, Lattice Shard ×44; munizioni: Advanced Plasma ×30.000, Ultra Core ×67.500, Experimental Fusion Core ×56.250
- **Omega Vault**: Ship Fragment ×3.250, Nyxite ×2.750, Cataclysite ×2.250, Quorvium ×1.600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10, Echo Shard ×34, Lattice Shard ×54; munizioni: Advanced Plasma ×37.500, Ultra Core ×75.000, Experimental Fusion Core ×75.000
- **Davidski's Nightmare**: Ship Fragment ×3.250, Nyxite ×2.750, Cataclysite ×2.250, Quorvium ×1.600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10, Echo Shard ×34, Lattice Shard ×54; munizioni: Advanced Plasma ×37.500, Ultra Core ×75.000, Experimental Fusion Core ×75.000
- **Heartshards**: 1 con il primo completamento di ogni porta in una stagione, e il 5% di probabilità di 1 in più a ogni completamento.

<!-- solo-pay:end -->

**Il Thulium è tagliato a un limite.** Le porte non possono restituire più di una quota del Thulium che hai speso in giri, contata su tutte le tue porte e tutti i tuoi giri (la quota è nell’elenco in cima). Ciò che una vittoria e i suoi alieni pagherebbero oltre viene tagliato, e la schermata del risultato dice quanto. Crediti, esperienza, onore, minerale, piastre e munizioni non vengono mai tagliati.

### Gli alieni {#the-aliens}

Ogni alieno che uccidi in una porta paga alle cifre che ha in Alpha, qualunque mondo tu stia volando: nessun moltiplicatore del mondo, nessun booster e nessun bonus Premium le cambia. Un’ondata paga per i suoi alieni **una volta** per partita, per quante volte tu esca e rientri. Il pagamento arriva alla fine di ogni tratto della partita: quando esci, muori, finisci le vite, abbandoni o vinci. Le uccisioni di un tratto restano non pagate solo con il reset e con un riavvio del server mentre sei dentro (la tua partita resta aperta, ma le uccisioni di quel tratto vanno perse). Le uccisioni di una porta contano per le [missioni](/wiki/03-Mechanics/Quests.md#where-it-counts) che non indicano alcun settore (come le grandi cacce della linea delle Sfide), nel momento in cui avvengono (un’ondata conta per loro **una volta** per partita, come paga una volta sola), e per nient’altro: non per le statistiche delle uccisioni, i contatori degli obiettivi, il kill feed o l’esperienza dei tuoi droni e P.E.T. L’esperienza e l’onore che pagano contano invece per i tuoi punti classifica PvE, come quelli di una vittoria. Il bottino degli alieni arriva con il pagamento, direttamente nel tuo inventario.

<!-- solo-kills:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Alieno | Crediti | Thulium | XP | Onore |
| :--- | ---: | ---: | ---: | ---: |
| **Seeker** | {{guide:spoils.pay.credits@Seeker#1}} | {{guide:spoils.pay.thulium@Seeker#1}} | {{guide:spoils.pay.experience@Seeker#1}} | {{guide:spoils.pay.honor@Seeker#1}} |
| **Phantasm** | {{guide:spoils.pay.credits@Phantasm#1}} | {{guide:spoils.pay.thulium@Phantasm#1}} | {{guide:spoils.pay.experience@Phantasm#1}} | {{guide:spoils.pay.honor@Phantasm#1}} |
| **Bulwark** | {{guide:spoils.pay.credits@Bulwark#1}} | {{guide:spoils.pay.thulium@Bulwark#1}} | {{guide:spoils.pay.experience@Bulwark#1}} | {{guide:spoils.pay.honor@Bulwark#1}} |
| **Goombah** | {{guide:spoils.pay.credits@Goombah#1}} | {{guide:spoils.pay.thulium@Goombah#1}} | {{guide:spoils.pay.experience@Goombah#1}} | {{guide:spoils.pay.honor@Goombah#1}} |
| **Crystalys** | {{guide:spoils.pay.credits@Crystalys#1}} | {{guide:spoils.pay.thulium@Crystalys#1}} | {{guide:spoils.pay.experience@Crystalys#1}} | {{guide:spoils.pay.honor@Crystalys#1}} |
| **Boss Seeker** | {{guide:spoils.pay.credits@Boss Seeker#1}} | {{guide:spoils.pay.thulium@Boss Seeker#1}} | {{guide:spoils.pay.experience@Boss Seeker#1}} | {{guide:spoils.pay.honor@Boss Seeker#1}} |
| **Seeker Slave** | {{guide:spoils.pay.credits@Seeker Slave#1}} | {{guide:spoils.pay.thulium@Seeker Slave#1}} | {{guide:spoils.pay.experience@Seeker Slave#1}} | {{guide:spoils.pay.honor@Seeker Slave#1}} |
| **Boss Phantasm** | {{guide:spoils.pay.credits@Boss Phantasm#1}} | {{guide:spoils.pay.thulium@Boss Phantasm#1}} | {{guide:spoils.pay.experience@Boss Phantasm#1}} | {{guide:spoils.pay.honor@Boss Phantasm#1}} |
| **Phantasm Guard** | {{guide:spoils.pay.credits@Phantasm Guard#1}} | {{guide:spoils.pay.thulium@Phantasm Guard#1}} | {{guide:spoils.pay.experience@Phantasm Guard#1}} | {{guide:spoils.pay.honor@Phantasm Guard#1}} |
| **Boss Goombah** | {{guide:spoils.pay.credits@Boss Goombah#1}} | {{guide:spoils.pay.thulium@Boss Goombah#1}} | {{guide:spoils.pay.experience@Boss Goombah#1}} | {{guide:spoils.pay.honor@Boss Goombah#1}} |
| **Goombah Guard** | {{guide:spoils.pay.credits@Goombah Guard#1}} | {{guide:spoils.pay.thulium@Goombah Guard#1}} | {{guide:spoils.pay.experience@Goombah Guard#1}} | {{guide:spoils.pay.honor@Goombah Guard#1}} |
| **Boss Crystalys** | {{guide:spoils.pay.credits@Boss Crystalys#1}} | {{guide:spoils.pay.thulium@Boss Crystalys#1}} | {{guide:spoils.pay.experience@Boss Crystalys#1}} | {{guide:spoils.pay.honor@Boss Crystalys#1}} |
| **Crystalys Guard** | {{guide:spoils.pay.credits@Crystalys Guard#1}} | {{guide:spoils.pay.thulium@Crystalys Guard#1}} | {{guide:spoils.pay.experience@Crystalys Guard#1}} | {{guide:spoils.pay.honor@Crystalys Guard#1}} |
| **Evil Protos** | {{guide:spoils.pay.credits@Evil Protos}} | {{guide:spoils.pay.thulium@Evil Protos}} | {{guide:spoils.pay.experience@Evil Protos}} | {{guide:spoils.pay.honor@Evil Protos}} |
| **Evil Kitefin** | {{guide:spoils.pay.credits@Evil Kitefin}} | {{guide:spoils.pay.thulium@Evil Kitefin}} | {{guide:spoils.pay.experience@Evil Kitefin}} | {{guide:spoils.pay.honor@Evil Kitefin}} |
| **Evil Ostirion** | {{guide:spoils.pay.credits@Evil Ostirion}} | {{guide:spoils.pay.thulium@Evil Ostirion}} | {{guide:spoils.pay.experience@Evil Ostirion}} | {{guide:spoils.pay.honor@Evil Ostirion}} |
| **Evil Nomad** | {{guide:spoils.pay.credits@Evil Nomad}} | {{guide:spoils.pay.thulium@Evil Nomad}} | {{guide:spoils.pay.experience@Evil Nomad}} | {{guide:spoils.pay.honor@Evil Nomad}} |
| **Evil Paragon** | {{guide:spoils.pay.credits@Evil Paragon}} | {{guide:spoils.pay.thulium@Evil Paragon}} | {{guide:spoils.pay.experience@Evil Paragon}} | {{guide:spoils.pay.honor@Evil Paragon}} |
| **Evil Storm** | {{guide:spoils.pay.credits@Evil Storm}} | {{guide:spoils.pay.thulium@Evil Storm}} | {{guide:spoils.pay.experience@Evil Storm}} | {{guide:spoils.pay.honor@Evil Storm}} |
| **Evil Wraith** | {{guide:spoils.pay.credits@Evil Wraith}} | {{guide:spoils.pay.thulium@Evil Wraith}} | {{guide:spoils.pay.experience@Evil Wraith}} | {{guide:spoils.pay.honor@Evil Wraith}} |
| **Evil Ironclad** | {{guide:spoils.pay.credits@Evil Ironclad}} | {{guide:spoils.pay.thulium@Evil Ironclad}} | {{guide:spoils.pay.experience@Evil Ironclad}} | {{guide:spoils.pay.honor@Evil Ironclad}} |

| Porta | Crediti | Thulium | XP | Onore |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 514.000 | 2.099 | 55.296 | 1.018 |
| **Beta Breach** | 1.298.500 | 5.939 | 187.744 | 2.470 |
| **Gamma Foundry** | 3.064.500 | 13.693 | 541.944 | 4.696 |
| **Delta Siege** | 5.239.625 | 22.338 | 882.676 | 7.850 |
| **Omega Vault** | 7.088.125 | 29.196 | 1.196.828 | 10.022 |
| **Davidski's Nightmare** | 7.081.950 | 29.124 | 1.196.445 | 9.968 |

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
