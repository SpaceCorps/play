<!-- wiki-i18n source: a3ead40fe6402d78 -->
<!-- wiki-i18n title: Dungeon -->
# Dungeon {#dungeons}

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; porta; porte; signore della guerra; labirinto; fase; zona del bottino; carta -->

Un **dungeon** è ciò che il gioco chiama una **porta**: un labirinto chiuso con un **Signore della guerra** in fondo. Un Co-leader o il Leader di un [clan](/wiki/03-Mechanics/Clans.md) ne apre una e la paga con la banca del clan, e i membri del clan ci volano dentro insieme come un unico [gruppo](/wiki/03-Mechanics/Groups.md). Si fanno strada tra gli alieni del labirinto, aprono zone del bottino per scegliere una carta da ciascuna e abbattono il Signore della guerra. Ogni pilota che ha preso parte allo scontro viene pagato quando il Signore della guerra cade, entro i limiti più sotto. Le porte si trovano nella scheda **Porte** della pagina del clan.

Una porta è uno scontro solo contro gli alieni: dentro nessuno può attaccare un compagno di clan né nessun altro. Gli alieni non pagano nulla. La paga è solo quella del Signore della guerra, quindi l’unico modo per essere pagati è essere nello scontro quando cade.

## In breve {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Apre**: Dal giorno 4 della stagione
- **Chi apre una porta**: Un co-leader o il leader, che paga il prezzo con la banca del clan
- **Gruppo**: Da 4 a 10 membri del clan, in un solo gruppo
- **Porte al giorno**: 3 per clan in un giorno UTC, una sola aperta alla volta
- **Porte contemporanee**: 6 in un mondo
- **Mappe**: Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Labirinti**: 8; una viene scelta all’apertura di una porta
- **Raduno**: 10 min per radunarsi e avviare. Una porta che nessuno avvia si chiude, e il suo prezzo torna alla banca del clan
- **Limite di tempo**: Fase 1: 80 min, Fase 2: 110 min, Fase 3: 150 min dall’avvio. Quando scade, la porta fallisce e non paga nulla
- **Lasciata vuota**: Una porta con nessuno all’interno per 3 min fallisce
- **Dopo la caduta del Signore della guerra**: La porta resta aperta per 2 min, per i piloti all’interno
- **Tornare dentro**: Un pilota che è uscito o è stato distrutto può rientrare in volo 3 volte, a 20 s di distanza

<!-- dungeons-glance:end -->

## Come si svolge una partita {#how-a-run-goes}

1. **Convoca.** Nella scheda Porte un [Co-leader o il Leader](/wiki/03-Mechanics/Clans.md#hierarchy-roles) sceglie una fase e preme **Convoca**. Il prezzo esce dalla [banca del clan](/wiki/03-Mechanics/Clans.md#clan-economy-taxation), e la porta prende una delle mappe elencate sopra. Una porta che nessuno avvia si chiude, e il prezzo torna alla banca.
2. **Entra.** I membri del clan premono **Entra** nella finestra del Clan mentre sono in volo. I piloti all’interno sono il gruppo della porta.
3. **Avvia.** Il pilota che ha aperto la porta, o un ufficiale, preme **Avvia** quando ci sono abbastanza piloti all’interno. Dopo, possono tornare solo i piloti che erano già dentro.
4. **Aprirsi la strada nel labirinto.** Si entra a un’estremità del labirinto e il Signore della guerra aspetta all’altra. Gli alieni dormono nelle loro sale e si svegliano in branchi quando il gruppo si avvicina.
5. **Aprire le zone del bottino.** Degli anelli nel labirinto segnano le zone. Tienine una e il gruppo vota una carta, che viene pagata insieme alla paga del Signore della guerra.
6. **Sconfiggere il Signore della guerra.** Rompi il suo scudo e il suo scafo, e rispondi alle sue abilità. Quando cade, la porta è completata.
7. **Essere pagati.** La paga arriva nel momento in cui il Signore della guerra cade. La porta resta aperta ancora un po’ per i piloti all’interno, poi si chiude.

## Entrare {#entering}

Per entrare in una porta ti serve una **nave in volo**, quindi decolla prima e poi apri la finestra del Clan, e un [gruppo](/wiki/03-Mechanics/Groups.md) con abbastanza membri del clan. Ti serve anche il **livello** richiesto dalla fase, e non puoi essere già dentro un’altra porta. Il gruppo di una porta ha un limite di dimensione: quando è pieno, nessun altro può entrare.

Un Co-leader o il Leader apre una porta, una alla volta per il clan, e solo fino al numero di porte al giorno. La banca del clan deve avere il prezzo. Un clan può aprire una fase solo dopo aver completato quella precedente.

Dentro una porta non puoi cambiare mondo, e la Jump CPU e la Base CPU non funzionano. Il pulsante **Esci** nella barra della porta ti porta fuori dopo la conferma. Un pilota che se n’è andato, o che è stato distrutto, può rientrare alcune volte, con una breve attesa tra l’una e l’altra.

## Le fasi {#the-stages}

Una porta ha una fase, e la fase è la sua difficoltà. Una fase più alta ha alieni più resistenti che colpiscono più forte, e paga di più. I moltiplicatori della tabella valgono per ogni alieno e per il Signore della guerra. Per danno si intendono laser, razzi e abilità del Signore della guerra. La tabella dice anche quanti alieni manda una fase rispetto alla prima. Il **prezzo** viene prelevato dalla banca del clan quando si apre la porta.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fase | Richiede | Scafo e scudo degli alieni | Numero di alieni | Danno degli alieni | Prezzo della porta (crediti, dalla banca del clan) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Fase 1** | Dal livello 6 | ×1 | ×1 | ×1 | 500.000 |
| **Fase 2** | Dal livello 7 | ×1,5 | ×1 | ×1,25 | 1.000.000 |
| **Fase 3** | Dal livello 8 | ×2,5 | ×1 | ×1,5 | 2.000.000 |

<!-- dungeons-stages:end -->

## Il labirinto {#the-maze}

Ogni porta è un labirinto chiuso su una mappa tutta sua, una delle mappe dell’elenco sopra, e il labirinto è uno di diversi schemi. Un labirinto è una griglia di sale e corridoi con pareti solide. Le navi non possono attraversare una parete, e una parete ferma i colpi, quindi è un riparo. Un meteorite cade dall’alto, e una parete non lo ferma.

## Gli alieni {#the-aliens}

Quattro tipi di alieni sorvegliano il labirinto. Dormono nelle loro sale e si svegliano quando un pilota si avvicina. La porta tiene in aria solo un certo numero di alieni alla volta, e quel numero cresce con la dimensione del gruppo, così un branco che distruggi lascia entrare il successivo. Un gruppo più grande incontra più alieni in proporzione, uno più piccolo meno, e un tipo di alieno non scende mai sotto uno.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Alieni, per un gruppo di 5 | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Gate Goombah | 130 | 130 | 130 |
| Gate Pirate | 28 | 28 | 28 |
| Gate Crystalys | 28 | 28 | 28 |
| Gate Crystalys Twin | 9 | 9 | 9 |
| Insieme | 195 | 195 | 195 |
| L’ondata di una zona del bottino | 10 × Gate Goombah e 1 × Gate Crystalys | 10 × Gate Goombah e 1 × Gate Crystalys | 10 × Gate Goombah e 1 × Gate Crystalys |

- **Vivi contemporaneamente**: Al massimo 10 per ogni pilota del gruppo, e 70 in tutto

<!-- dungeons-population:end -->

Un tipo alla volta. Scafo e scudo sono i valori usuali moltiplicati per il fattore della fase della colonna.

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Gate Goombah

- **Ha l’aspetto di**: Goombah
- **Vola in branchi da**: 6

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Scafo | 32.000 | 48.000 | 80.000 |
| Scudo | 48.000 | 72.000 | 120.000 |
| Danno dei laser (una raffica al secondo) | 3.000 | 3.750 | 4.500 |
| Velocità | 180 | 180 | 180 |
| Portata dei laser | 800 | 800 | 800 |
| Raggio di aggressione | 1.800 | 1.800 | 1.800 |

### Gate Pirate

- **Ha l’aspetto di**: Pirate Boss
- **Vola in branchi da**: 2
- **Razzo**: Un razzo diritto ogni 5 s, gittata 970 unità

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Scafo | 300.000 | 450.000 | 750.000 |
| Scudo | 50.100 | 75.150 | 125.250 |
| Danno dei laser (una raffica al secondo) | 200 | 250 | 300 |
| Danno dei razzi | 5.000 | 6.250 | 7.500 |
| Velocità | 92 | 92 | 92 |
| Portata dei laser | 700 | 700 | 700 |
| Raggio di aggressione | 1.800 | 1.800 | 1.800 |

### Gate Crystalys

- **Ha l’aspetto di**: Crystalys
- **Vola in branchi da**: 2

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Scafo | 256.000 | 384.000 | 640.000 |
| Scudo | 160.000 | 240.000 | 400.000 |
| Danno dei laser (una raffica al secondo) | 10.000 | 12.500 | 15.000 |
| Velocità | 230 | 230 | 230 |
| Portata dei laser | 900 | 900 | 900 |
| Raggio di aggressione | 2.400 | 2.400 | 2.400 |

### Gate Crystalys Twin

- **Ha l’aspetto di**: Crystalys, 1,4 volte più grande
- **Vola in branchi da**: 1

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Scafo | 512.000 | 768.000 | 1.280.000 |
| Scudo | 320.000 | 480.000 | 800.000 |
| Danno dei laser (una raffica al secondo) | 20.000 | 25.000 | 30.000 |
| Velocità | 230 | 230 | 230 |
| Portata dei laser | 900 | 900 | 900 |
| Raggio di aggressione | 2.400 | 2.400 | 2.400 |

<!-- dungeons-enemies:end -->

## Il Signore della guerra {#the-warlord}

Il Signore della guerra aspetta nella sala all’estremità opposta del labirinto, ed è l’unica cosa in una porta che paga. È un Crystalys diventato enorme. Il suo scafo e il suo scudo crescono con la dimensione del gruppo: più piloti entrano, più è resistente, in proporzione. Resta nella sua sala e usa le sue abilità una alla volta, in ordine casuale, ciascuna con una propria ricarica.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Ha l’aspetto di**: Crystalys, 3 volte più grande
- **Ricarica dello scudo**: 3.000 al secondo, dopo 15 s senza danni

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Scafo | 10.000.000 | 15.000.000 | 25.000.000 |
| Scudo | 8.000.000 | 12.000.000 | 20.000.000 |
| Danno dei laser (una raffica al secondo) | 8.000 | 10.000 | 12.000 |
| Velocità | 120 | 120 | 120 |
| Portata dei laser | 1.100 | 1.100 | 1.100 |

Lo scafo e lo scudo qui sopra valgono per un gruppo di 5. Crescono con il gruppo: sono lo scafo e lo scudo del Signore della guerra insieme, in base al numero di piloti nel gruppo all’avvio della porta.

| Piloti nel gruppo | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| 4 | 14.400.000 | 21.600.000 | 36.000.000 |
| 5 | 18.000.000 | 27.000.000 | 45.000.000 |
| 6 | 21.600.000 | 32.400.000 | 54.000.000 |
| 7 | 25.200.000 | 37.800.000 | 63.000.000 |
| 8 | 28.800.000 | 43.200.000 | 72.000.000 |
| 9 | 32.400.000 | 48.600.000 | 81.000.000 |
| 10 | 36.000.000 | 54.000.000 | 90.000.000 |

<!-- dungeons-boss:end -->

### Le sue abilità {#its-abilities}

- **L’anello rosso** dell’Aura di furto vitale ferisce ogni pilota al suo interno e cura il Signore della guerra con il danno. Anche l’Assorbimento dello scudo ha un anello rosso: svuota gli scudi dei piloti all’interno e carica quello del Signore della guerra. In entrambi i casi, esci dall’anello o mettiti dietro una parete.
- **Gli anelli ambra** della Pioggia di meteore mostrano dove i meteoriti cadranno un istante dopo. Continua a muoverti ed esci dall’anello prima che cada.
- **Bersaglio: i curatori** rivolge il Signore della guerra contro chi cura un altro pilota, e colpisce quel pilota più forte. Distribuisci le cure.
- **La Raffica di razzi** manda razzi a ricerca su piloti casuali. Una EMP Charge o l’occultamento li scrolla di dosso.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Abilità | Preparazione | Durata | Ricarica | Raggio dell’anello (unità) | Il Signore della guerra recupera, al massimo |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Aura di furto vitale** | 2 s | 15 s | 2 min | 900 | 8% di scafo e scudo |
| **Pioggia di meteore** | 1,5 s | 3 raffiche, a 4 s di distanza | 2 min | 420 | – |
| **Bersaglio: i curatori** | 1 s | 45 s | 2 min | – | – |
| **Raffica di razzi** | 1,5 s | 45 s | 2 min | – | – |
| **Assorbimento dello scudo** | 2 s | 15 s | 2 min | 900 | 6% del suo scudo |

| Abilità | Fase 1 | Fase 2 | Fase 3 |
| :--- | :--- | :--- | :--- |
| **Aura di furto vitale** | 8.000 al secondo | 10.000 al secondo | 12.000 al secondo |
| **Pioggia di meteore** | 6 meteoriti per raffica, 40.000 ciascuno | 8 meteoriti per raffica, 50.000 ciascuno | 10 meteoriti per raffica, 60.000 ciascuno |
| **Bersaglio: i curatori** | Il suo laser colpisce ×1,5 più forte il pilota contro cui si volge | Il suo laser colpisce ×1,5 più forte il pilota contro cui si volge | Il suo laser colpisce ×1,5 più forte il pilota contro cui si volge |
| **Raffica di razzi** | 6.500 a razzo, uno ogni 15 s | 8.125 a razzo, uno ogni 15 s | 9.750 a razzo, uno ogni 15 s |
| **Assorbimento dello scudo** | 10.000 di scudo al secondo | 12.500 di scudo al secondo | 15.000 di scudo al secondo |

<!-- dungeons-abilities:end -->

## Zone del bottino {#loot-zones}

Un anello sul pavimento del labirinto segna ogni zona del bottino, una volta che il gruppo l’ha trovata. Resta un momento al suo interno e la zona si sveglia, e un’ondata di alieni le va incontro. Poi il gruppo deve **tenere** la zona: mantenere un pilota all’interno finché la barra non si riempie. Gli alieni nell’anello fermano la barra, e questa torna indietro finché nessuno è dentro, quindi elimina prima l’ondata. Quando la zona si apre, il gruppo vede tre carte diverse e **vota** per una. Una zona si apre una sola volta, e la sua ondata non torna.

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Zone del bottino**: 4 in ogni labirinto
- **Raggio**: 450 unità
- **Risveglio**: Resta dentro l’anello per 2 s
- **Tenuta**: Tieni un pilota dentro per 30 s. La barra si ferma finché ci sono 3 o più alieni nell’anello e torna indietro finché non c’è nessuno
- **Scelta**: Il gruppo ha 45 s per votare. Il voto finisce prima se ogni pilota presente ha votato o se una carta ha più della metà dei voti

<!-- dungeons-zones:end -->

### Le carte {#the-cards}

Le carte vengono estratte una alla volta dal mazzo qui sotto. La probabilità è quella di una carta in un’estrazione. Una carta con molte copie va a ogni pilota pagato, e una carta di equipaggiamento, con una sola copia, va a un pilota del gruppo. Un pilota che non viene pagato non riceve nemmeno la carta, e una zona aperta in una porta che fallisce non paga nulla.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Carta | Fase 1 | Fase 2 | Fase 3 | Probabilità | Va a |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2.000 | 3.000 | 5.000 | 21% | Ogni pilota pagato |
| Velkonite Reinforced Plate | 10 | 15 | 25 | 12% | Ogni pilota pagato |
| Orvium Reinforced Plate | 10 | 15 | 25 | 12% | Ogni pilota pagato |
| Velkonite | 200 | 300 | 500 | 12% | Ogni pilota pagato |
| Orvium | 200 | 300 | 500 | 12% | Ogni pilota pagato |
| Ultra Core | 5.000 | 7.500 | 12.500 | 10% | Ogni pilota pagato |
| Experimental Fusion Core | 3.000 | 4.500 | 7.500 | 8% | Ogni pilota pagato |
| Dark Matter | 5 | 8 | 12 | 8% | Ogni pilota pagato |
| Dark Matter Plate | 1 | 1 | 2 | 4% | Ogni pilota pagato |
| Engine III | 1 | 1 | 1 | 0,25% | Un pilota del gruppo |
| Heavy Shield Core | 1 | 1 | 1 | 0,25% | Un pilota del gruppo |
| Adaptive Core III | 1 | 1 | 1 | 0,25% | Un pilota del gruppo |
| Starfire-III | 1 | 1 | 1 | 0,25% | Un pilota del gruppo |

- **Equipaggiamento**: Le carte con un solo esemplare sono equipaggiamento: insieme 1% delle carte

<!-- dungeons-cards:end -->

## Paga {#pay}

Quando il Signore della guerra cade, ogni pilota che se l’è guadagnata viene pagato, una volta per partita. Le carte scelte dal gruppo si aggiungono alla paga della fase. Non c’è moltiplicatore di mondo: la paga è la stessa in ogni mondo.

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fase | Onore | Esperienza | Crediti | Thulium | Munizioni x4 | Punti classifica PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| **Fase 1** | 25.000 | 600.000 | 5.000.000 | 4.000 | 4.000 | 600 |
| **Fase 2** | 50.000 | 1.500.000 | 10.000.000 | 9.000 | 9.000 | 1.500 |
| **Fase 3** | 100.000 | 2.400.000 | 17.500.000 | 15.000 | 15.000 | 2.400 |

<!-- dungeons-pay:end -->

### Chi viene pagato {#who-is-paid}

Gli alieni non pagano mai. Una partita si gioca per intero anche quando non paga nulla, e la schermata dei risultati dice perché. L’ingresso non viene mai rifiutato perché sei già stato pagato per una fase: quella partita semplicemente non paga.

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Un giorno**: Una fase paga un pilota una volta per giorno UTC: il giorno in cui cade il Signore della guerra
- **Una settimana**: Un pilota è pagato per al massimo 10 fasi completate per settimana UTC, da lunedì a domenica
- **Dentro**: Almeno 2 min in tutto
- **Parte nello scontro**: Almeno una di queste: ha inflitto 2% dello scafo e dello scudo del Signore della guerra; ha distrutto 10 alieni della porta; ha curato altri piloti per 50.000 durante lo scontro con il Signore della guerra

<!-- dungeons-rules:end -->

### Quanto valgono un giorno e una settimana {#what-a-day-and-a-week-are-worth}

Ciò che un pilota può ricevere in un giorno, e nella settimana migliore che i limiti consentono. L’ultima colonna è ciò che la paga aggiunge ai tuoi [punti PvE](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points).

<!-- dungeons-totals:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Paga per ogni pilota | Onore | Esperienza | Crediti | Thulium | Munizioni x4 | Punti classifica PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Un giorno, ogni fase una volta | 175.000 | 4.500.000 | 32.500.000 | 28.000 | 28.000 | 4.500 |
| La settimana migliore: 7 × Fase 3 e 3 × Fase 2 | 850.000 | 21.300.000 | 152.500.000 | 132.000 | 132.000 | 21.300 |

L’esperienza di una fase completata e pagata conta per i tuoi punti classifica PvE: un punto ogni 1.000 di esperienza.

<!-- dungeons-totals:end -->

## La ricompensa della banca del clan {#clan-bank-reward}

Viene pagata anche la banca del clan, in crediti e non in Thulium, la prima volta che il clan completa una fase in una stagione. Il clan deve essere abbastanza vecchio, e devono essere pagati abbastanza piloti di quella partita. La banca viene pagata una volta per fase in una stagione.

<!-- dungeons-clan:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fase | Crediti per la banca del clan |
| :--- | ---: |
| **Fase 1** | 10.000.000 |
| **Fase 2** | 20.000.000 |
| **Fase 3** | 30.000.000 |

- **Età del clan**: Almeno 3 g
- **Piloti pagati**: Almeno 3 nella porta

<!-- dungeons-clan:end -->

## Consigli {#tips}

- Elimina l’ondata di una zona prima di provare a tenerla, e combatti dentro l’anello se gli alieni entrano.
- Usa le pareti: i laser non le attraversano, e gli anelli del Signore della guerra si fermano contro di esse.
- Tieni da parte una EMP Charge per la Raffica di razzi.
- Controlla l’orologio nella barra della porta. Quando il tempo finisce, la porta fallisce e non paga nulla.
