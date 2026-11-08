<!-- wiki-i18n source: 9679806228678ce2 -->
<!-- wiki-i18n title: Dungeon -->
# Dungeon {#dungeons}

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; portal; clan portal; join; clan gate alerts; clan dungeon window; clan dungeon alerts; dungeon goombah; dungeon pirate; dungeon crystalys; dungeon warlord; 75 percent; three quarters; start room; fog; guards; locked room; boss room; booster; boosters; swarm assist; focus most wanted; zone of chaos; rocket barrage; porta; porte; signore della guerra; labirinto; fase; zona del bottino; carta; portale; portale del clan; booster; nebbia; guardiani; sala di partenza; sala chiusa; supporto dello sciame; zona del caos; avvisi porta del clan; dungeon del clan; avvisi dungeon del clan; tre quarti; 75 per cento -->

Un **dungeon** è un labirinto chiuso con un **Signore della guerra** in fondo (prima della 0.5.2 il gioco lo chiamava porta). Un Co-leader o il Leader di un [clan](/wiki/03-Mechanics/Clans.md) ne apre uno e lo paga con la banca del clan, e i membri del clan ci volano dentro insieme come un unico [gruppo](/wiki/03-Mechanics/Groups.md). Si fanno strada tra gli alieni del labirinto, aprono zone del bottino per scegliere una carta da ciascuna e abbattono il Signore della guerra. Ogni pilota che ha preso parte allo scontro viene pagato quando il Signore della guerra cade, entro i limiti più sotto. I dungeon si trovano nella scheda **Dungeon** della pagina del clan.

Un dungeon è uno scontro solo contro gli alieni: dentro nessuno può attaccare un compagno di clan né nessun altro. Gli alieni non pagano nulla. La paga è solo quella del Signore della guerra, quindi l’unico modo per essere pagati è essere nello scontro quando cade.

## In breve {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Apre**: Dal giorno 1 della stagione
- **Chi apre un dungeon**: Un co-leader o il leader, che paga il prezzo con la banca del clan
- **Gruppo**: Da 4 a 10 membri del clan, in un solo gruppo
- **Dungeon al giorno**: 3 per clan in un giorno UTC, una sola aperta alla volta
- **Dungeon contemporanei**: 6 in un mondo
- **Mappe**: Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Labirinti**: 8; uno viene scelto all’apertura di un dungeon
- **Stanza del boss**: Si apre quando 75% degli alieni del labirinto è distrutto, arrotondato per eccesso
- **Raduno**: 10 min per radunarsi e avviare. Un dungeon che nessuno avvia si chiude, e il suo prezzo torna alla banca del clan
- **Limite di tempo**: Fase 1: 95 min, Fase 2: 130 min, Fase 3: 165 min dall’avvio. Quando scade, il dungeon fallisce e non paga nulla
- **Lasciata vuota**: Un dungeon con nessuno all’interno per 3 min fallisce
- **Dopo la caduta del Signore della guerra**: Il dungeon resta aperto per 2 min, per i piloti all’interno
- **Tornare dentro**: Un pilota che è uscito o è stato distrutto può rientrare in volo 3 volte, a 20 s di distanza

<!-- dungeons-glance:end -->

## Come si svolge una partita {#how-a-run-goes}

1. **Convoca.** Nella scheda Dungeon un [Co-leader o il Leader](/wiki/03-Mechanics/Clans.md#hierarchy-roles) sceglie una fase e preme **Convoca**. Il prezzo esce dalla [banca del clan](/wiki/03-Mechanics/Clans.md#clan-economy-taxation), e il dungeon prende una delle mappe elencate sopra. Un dungeon che nessuno avvia si chiude, e il prezzo torna alla banca.
2. **Entra.** I membri del clan premono **Entra** nella finestra del Clan mentre sono in volo, saltano attraverso il portale del clan o premono **Unisciti** sulla scheda di avviso (vedi Entrare). Tutti atterrano nella sala di partenza, e i piloti all’interno sono il gruppo del dungeon.
3. **Avvia.** La sala di partenza è una piccola sala a un’estremità del labirinto, e il suo portello resta chiuso mentre il dungeon si riunisce. Dentro non ci sono alieni, quindi si può aspettare in sicurezza. Il dungeon **parte da solo** quando ogni pilota che aspetta è dentro e il gruppo è abbastanza grande. Aspetta i membri del clan che sono online, non assenti e nel gruppo di un pilota che è entrato, e parte subito quando il gruppo è pieno. Il pilota che ha aperto il dungeon, o un ufficiale, può premere **Avvia** per cominciare prima con i piloti che sono dentro, se sono abbastanza. Un pilota che se ne va non viene più aspettato. Quando il dungeon parte, il portello si apre per sempre, e dopo possono tornare solo i piloti che erano già dentro.
4. **Aprirsi la strada nel labirinto.** Si entra a un’estremità del labirinto e il Signore della guerra aspetta all’altra, in una sala chiusa. Il labirinto è buio: si vede solo ciò che il gruppo ha esplorato e ciò che è vicino alle sue navi. Gli alieni dormono in branchi nei corridoi, e un branco che si sveglia dà la caccia al gruppo attraverso il labirinto.
5. **Aprire le zone del bottino.** Degli anelli nel labirinto segnano le zone. Tienine una e il gruppo vota una carta, che viene pagata insieme alla paga del Signore della guerra.
6. **Sbloccare la sala del boss.** Distruggi tre quarti degli alieni del labirinto, e il portello della sala del Signore della guerra si apre. Fino ad allora il Signore della guerra non può essere ferito.
7. **Sconfiggere il Signore della guerra.** Rompi il suo scudo e il suo scafo, e rispondi alle sue abilità. Quando cade, il dungeon è completato.
8. **Essere pagati.** La paga arriva nel momento in cui il Signore della guerra cade. Il dungeon resta aperto ancora un po’ per i piloti all’interno, poi si chiude.

## Entrare {#entering}

Per entrare in un dungeon ti serve una **nave in volo**, quindi decolla prima e poi apri la finestra del Clan, e un [gruppo](/wiki/03-Mechanics/Groups.md) con abbastanza membri del clan. Ti serve anche il **livello** richiesto dalla fase, e non puoi essere già dentro un altro dungeon. Il gruppo di un dungeon ha un limite di dimensione: quando è pieno, nessun altro può entrare.

Un Co-leader o il Leader apre un dungeon, uno alla volta per il clan, e solo fino al numero di dungeon al giorno. La banca del clan deve avere il prezzo. Un clan può aprire una fase solo dopo aver completato quella precedente.

Dentro un dungeon non puoi cambiare mondo, e la Jump CPU e la Base CPU non funzionano. Il pulsante **Esci** nella finestra Dungeon del clan ti porta fuori. Prima chiede conferma, a meno che il Signore della guerra non sia già caduto: allora esci subito. Un pilota che se n’è andato, o che è stato distrutto, può rientrare alcune volte, con una breve attesa tra l’una e l’altra.

### Il portale del clan e l’avviso {#the-clan-portal-and-the-call}

Quando un dungeon viene aperto, il clan riceve per essa un **portale** sulla mappa di casa di ogni corporazione (`M-1`, `T-1` e `G-1`), un po’ fuori dalla zona sicura della stazione. Solo i piloti del clan lo vedono: per tutti gli altri non c’è. Non ha una zona sicura propria. Vola fino a lui e salta come a ogni altro portale, e ti porta nel dungeon con le regole di **Entra**: una nave in volo, un gruppo con abbastanza membri del clan, il livello della fase e posto nel gruppo. Quando il dungeon è partito, possono usarlo solo i piloti che erano già dentro. Il portale sparisce quando il dungeon è finito.

Mentre il dungeon del tuo clan si sta riunendo e tu voli altrove, ti arriva un **avviso**: una scheda in alto nella schermata di volo, con un suono. Dice chi ha aperto il dungeon, quanti piloti ci sono dentro e per quanto tempo il dungeon resta aperto. **Unisciti** ti porta dentro, come **Entra** nella scheda Dungeon, e quando esci dal dungeon la tua nave torna dov’era. Unisciti è disattivato finché il tuo gruppo è troppo piccolo. **Non ora** nasconde la scheda per quel dungeon. Se il tuo gruppo è già dentro e il dungeon ti aspetta, la scheda lo dice. La scheda arriva ai piloti del clan che sono in volo (non a quelli attraccati a una stazione) e che hanno il livello richiesto dalla fase. Puoi disattivare la scheda e il suo suono con **Avvisi dungeon del clan** in Impostazioni › Generali › Gruppi.

### La finestra Dungeon del clan {#the-clan-dungeon-window}

Dentro un dungeon la partita ha una finestra tutta sua, **Dungeon del clan**. Mostra il tempo trascorso e quello che resta, quanti alieni volano e quanti sono stati distrutti, che cosa deve fare ora il gruppo (esplorare il labirinto, tenere una zona, trovare il boss, distruggere tre quarti degli alieni, sconfiggere il Signore della guerra), le barre dello scafo del gruppo, la barra di tenuta mentre sei in una zona, l’abilità del Signore della guerra con il suo conto alla rovescia e il pulsante **Esci**. È una finestra come le altre: trascinala dalla barra del titolo e chiudila con la luce rossa nel suo angolo. Si apre da sola quando entri in un dungeon, una volta per ogni dungeon: se la chiudi, resta chiusa fino al dungeon successivo. La barra degli strumenti ha un pulsante **Dungeon del clan** per esso finché sei in un dungeon. Mentre la finestra è chiusa, un’abilità del Signore della guerra che sta per iniziare o è in corso compare come una striscia di una riga con il suo nome e il conto alla rovescia. Fai clic sulla striscia per riaprire la finestra.

## Le fasi {#the-stages}

Un dungeon ha una fase, e la fase è la sua difficoltà. Una fase più alta ha alieni più resistenti che colpiscono più forte, e paga di più. I moltiplicatori della tabella sono quelli degli alieni. Il danno indica i loro laser e razzi. Il Signore della guerra non segue la tabella: ha numeri suoi per ogni fase, più in basso. La tabella dice anche quanti alieni manda una fase rispetto alla prima. Il **prezzo** viene prelevato dalla banca del clan quando il dungeon viene aperto.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fase | Richiede | Scafo e scudo degli alieni | Numero di alieni | Danno degli alieni | Prezzo del dungeon (crediti, dalla banca del clan) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Fase 1** | Dal livello 6 | ×1 | ×1 | ×1 | 500.000 |
| **Fase 2** | Dal livello 7 | ×1,5 | ×1 | ×1,5 | 1.000.000 |
| **Fase 3** | Dal livello 8 | ×2 | ×1 | ×2 | 2.000.000 |

<!-- dungeons-stages:end -->

## Il labirinto {#the-maze}

Ogni dungeon è un labirinto chiuso su una mappa a sé, una delle mappe dell’elenco qui sopra, e il labirinto è uno di diversi schemi. Il labirinto riempie tutta la mappa, da un bordo all’altro: una griglia di sale e corridoi con pareti piene. Le navi non possono attraversare una parete, e una parete blocca i colpi, quindi è una copertura. Un meteorite cade dall’alto, e una parete non lo ferma.

**Sale e portelli.** La sala di partenza, dove atterri, e la sala del Signore della guerra, all’estremità opposta, hanno ciascuna un portello. Un portello chiuso è un muro per navi, colpi e alieni allo stesso modo. Il portello di partenza si apre quando il dungeon parte. Quello del Signore della guerra resta bloccato finché tre quarti degli alieni non sono distrutti (vedi [La sala chiusa](#the-locked-room)). Tra i due, il labirinto ha una sala del bottino per ogni zona del bottino.

**Nebbia.** Il labirinto è buio. In volo vedi le sue pareti e i suoi alieni solo dove è stato il gruppo, e per un breve tratto attorno a ogni nave del gruppo. Una sala conta come esplorata appena uno di voi è dentro. La minimappa funziona allo stesso modo: è una mappa dell’intero piano che si riempie man mano che il gruppo lo esplora, con l’ingresso, il portello del Signore della guerra, le zone che avete trovato e il Signore della guerra una volta trovato. I piloti del tuo gruppo sono sempre mostrati.

## Gli alieni {#the-aliens}

Quattro tipi di alieni custodiscono il labirinto. Dormono in branchi nei corridoi, mai in una sala, e un branco si sveglia quando un pilota si avvicina. Un branco sveglio non ti aspetta: dà la caccia al gruppo attraverso il labirinto, e un branco che perde tutti torna dove dormiva e si cura. Alcuni branchi sono svegli fin dal primo secondo, fermi nei corridoi lontano dall’ingresso, finché un pilota non si avvicina. Il dungeon tiene in aria solo un certo numero di alieni alla volta, e quel numero cresce con la dimensione del gruppo, quindi un branco che si sveglia può dover aspettare posto, e un branco che distruggi fa entrare il successivo. Un gruppo più grande incontra più alieni, in proporzione, uno più piccolo meno, e un tipo di alieno non scende mai sotto uno.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Alieni, per un gruppo di 5 | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Dungeon Goombah | 156 | 156 | 156 |
| Dungeon Pirate | 34 | 34 | 34 |
| Dungeon Crystalys | 34 | 34 | 34 |
| Dungeon Crystalys Twin | 11 | 11 | 11 |
| Insieme | 235 | 235 | 235 |
| Per aprire la stanza del boss | 177 | 177 | 177 |
| L’ondata di una zona del bottino | 12 × Dungeon Goombah e 1 × Dungeon Crystalys | 12 × Dungeon Goombah e 1 × Dungeon Crystalys | 12 × Dungeon Goombah e 1 × Dungeon Crystalys |

- **Vivi contemporaneamente**: Al massimo 10 per ogni pilota del gruppo, e 70 in tutto

<!-- dungeons-population:end -->

Un tipo alla volta. Scafo e scudo sono i valori usuali moltiplicati per il fattore della fase della colonna.

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Dungeon Goombah

- **Ha l’aspetto di**: Goombah
- **Vola in branchi da**: 6

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Scafo | 32.000 | 48.000 | 64.000 |
| Scudo | 48.000 | 72.000 | 96.000 |
| Danno dei laser (una raffica al secondo) | 3.000 | 4.500 | 6.000 |
| Velocità | 180 | 180 | 180 |
| Portata dei laser | 800 | 800 | 800 |
| Raggio di aggressione | 1.800 | 1.800 | 1.800 |

### Dungeon Pirate

- **Ha l’aspetto di**: Pirate Boss
- **Vola in branchi da**: 2
- **Razzo**: Un razzo diritto ogni 5 s, gittata 970 unità

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Scafo | 300.000 | 450.000 | 600.000 |
| Scudo | 50.100 | 75.150 | 100.200 |
| Danno dei laser (una raffica al secondo) | 200 | 300 | 400 |
| Danno dei razzi | 5.000 | 7.500 | 10.000 |
| Velocità | 110 | 110 | 110 |
| Portata dei laser | 700 | 700 | 700 |
| Raggio di aggressione | 1.800 | 1.800 | 1.800 |

### Dungeon Crystalys

- **Ha l’aspetto di**: Crystalys
- **Vola in branchi da**: 2

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Scafo | 256.000 | 384.000 | 512.000 |
| Scudo | 160.000 | 240.000 | 320.000 |
| Danno dei laser (una raffica al secondo) | 10.000 | 15.000 | 20.000 |
| Velocità | 230 | 230 | 230 |
| Portata dei laser | 900 | 900 | 900 |
| Raggio di aggressione | 2.400 | 2.400 | 2.400 |

### Dungeon Crystalys Twin

- **Ha l’aspetto di**: Crystalys, 1,4 volte più grande
- **Vola in branchi da**: 1

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Scafo | 512.000 | 768.000 | 1.024.000 |
| Scudo | 320.000 | 480.000 | 640.000 |
| Danno dei laser (una raffica al secondo) | 20.000 | 30.000 | 40.000 |
| Velocità | 230 | 230 | 230 |
| Portata dei laser | 900 | 900 | 900 |
| Raggio di aggressione | 2.400 | 2.400 | 2.400 |

<!-- dungeons-enemies:end -->

## Il Signore della guerra {#the-warlord}

Il Signore della guerra aspetta nella sala all’estremità opposta del labirinto, ed è l’unica cosa in un dungeon che paga. È un Crystalys diventato enorme. Il suo scafo e il suo scudo crescono con la dimensione del gruppo: più piloti entrano, più è resistente, in proporzione. Non lascia mai la sua sala, con la porta chiusa o aperta: resta tra le pareti della sala e non dà la caccia nei corridoi. Un pilota all’esterno può attirarlo solo fino al bordo della sala, e da una porta aperta spara comunque a tutto ciò che il suo laser raggiunge. Usa le sue abilità una alla volta, in ordine casuale, ognuna con il suo tempo di ricarica.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Ha l’aspetto di**: Crystalys, 3 volte più grande
- **Ricarica dello scudo**: 3.000 al secondo, dopo 15 s senza danni

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Scafo | 10.000.000 | 15.000.000 | 25.000.000 |
| Scudo | 8.000.000 | 12.000.000 | 20.000.000 |
| Danno dei laser (una raffica al secondo) | 12.500–15.000 | 15.000–17.500 | 20.000–25.000 |
| Velocità | 120 | 120 | 120 |
| Portata dei laser | 1.100 | 1.100 | 1.100 |

Lo scafo e lo scudo qui sopra valgono per un gruppo di 5. Crescono con il gruppo: sono lo scafo e lo scudo del Signore della guerra insieme, in base al numero di piloti nel gruppo all’avvio del dungeon.

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

### La sala chiusa {#the-locked-room}

Il portello della sala del Signore della guerra è chiuso dal momento in cui il dungeon viene aperto, e finché è chiuso il Signore della guerra non può essere ferito: nessun laser, razzo o esplosione lo tocca, e non usa nessuna abilità. Il portello si apre per sempre quando sono stati distrutti **tre quarti degli alieni** con cui il dungeon è stato creato, arrotondati per eccesso (la tabella degli alieni qui sopra li conta per un gruppo di 5). Contano gli alieni dei branchi del labirinto, compresi i branchi che stanno nei corridoi fin dal primo secondo, di tutti e quattro i tipi e chiunque li distrugga. Non contano le ondate delle zone del bottino, i Goombah che il Signore della guerra chiama e il Signore della guerra stesso.

La finestra Dungeon del clan conta quanti alieni restano da distruggere per aprire la sala e dice, in un’etichetta, che il Signore della guerra non può essere ferito, e un messaggio ti avvisa quando la sala viene sbloccata. Un branco che dorme ancora conta per intero, quindi il gruppo deve esplorare il labirinto, ma può lasciare in pace l’ultimo quarto degli alieni. Sulla minimappa il portello è una linea rossa finché è bloccato e una verde quando è aperto. Un dungeon non è mai una trappola: il limite di tempo pone comunque fine a un dungeon il cui portello resta chiuso, e un amministratore può sbloccare la sala di un dungeon in stallo.

### Le sue abilità {#its-abilities}

- **L’anello rosso** dell’Aura di furto vitale ferisce ogni pilota al suo interno e cura il Signore della guerra con il danno. Anche l’Assorbimento dello scudo ha un anello rosso: svuota gli scudi dei piloti all’interno e carica quello del Signore della guerra. In entrambi i casi, esci dall’anello o mettiti dietro una parete.
- **Gli anelli ambra** della Pioggia di meteore mostrano dove i meteoriti cadranno un istante dopo. Continua a muoverti ed esci dall’anello prima che cada.
- **Focus sul più ricercato** segna il pilota che ha inflitto più danno al Signore della guerra, con una parentesi dorata sulla sua nave, e il Signore della guerra gli spara un colpo in più ogni secondo finché dura. La sua mira non cambia: continua a sparare al pilota più vicino che riesce a vedere, quindi un pilota segnato che è anche il più vicino prende entrambi. Il colpo in più richiede una linea libera e la portata del laser del Signore della guerra, quindi una parete o un po’ di distanza lo salva. Non inizia finché nessuno ha inflitto danno.
- **La Raffica di razzi** manda razzi a ricerca su piloti casuali, ma solo su piloti che il Signore della guerra può vedere, e una parete sulla strada ferma un razzo. Un anello mostra quale pilota un razzo segue. Una EMP Charge o l’occultamento li scrolla di dosso.
- **Il Supporto dello sciame** è il Signore della guerra che chiama i suoi Goombah. Finché vivono, non può essere ferito, e non spara né usa altre abilità. Distruggili tutti: lo striscione conta quanti ne restano. Se passa un minuto, il Signore della guerra può di nuovo essere ferito e i Goombah rimasti restano a combattere. Non contano per la sala del boss, e non pagano nulla.
- **La Zona del Caos** è un anello viola sul terreno, attorno al punto in cui si trovava il Signore della guerra quando l’ha lanciata. Nessuno dentro l’anello può attaccare, né con i laser né con i razzi, ma riparazioni, occultamento e volo funzionano ancora, e il Signore della guerra e i suoi alieni sparano come sempre. L’anello compare un attimo prima di fare effetto: esci da esso, e spara dentro da fuori.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Abilità | Preparazione | Durata | Ricarica | Raggio dell’anello (unità) | Il Signore della guerra recupera, al massimo |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Aura di furto vitale** | 2 s | 15 s | 2 min | 900 | 8% di scafo e scudo |
| **Pioggia di meteore** | 1,5 s | 3 raffiche, a 4 s di distanza | 2 min | 420 | – |
| **Focus sul più ricercato** | 1 s | 20 s | 2 min | – | – |
| **Raffica di razzi** | 1,5 s | 45 s | 2 min | – | – |
| **Assorbimento dello scudo** | 2 s | 15 s | 2 min | 900 | 6% del suo scudo |
| **Supporto dello sciame** | 2 s | Fino a 1 min | 3 min | – | – |
| **Zona del Caos** | 2 s | 15 s | 2 min | 900 | – |

| Abilità | Fase 1 | Fase 2 | Fase 3 |
| :--- | :--- | :--- | :--- |
| **Aura di furto vitale** | 8.000 al secondo | 10.000 al secondo | 12.000 al secondo |
| **Pioggia di meteore** | 6 meteoriti per raffica, 40.000 ciascuno | 8 meteoriti per raffica, 50.000 ciascuno | 10 meteoriti per raffica, 60.000 ciascuno |
| **Focus sul più ricercato** | 18.750–22.500 per colpo extra al pilota che ha inflitto più danni, uno ogni 1 s | 22.500–26.250 per colpo extra al pilota che ha inflitto più danni, uno ogni 1 s | 30.000–37.500 per colpo extra al pilota che ha inflitto più danni, uno ogni 1 s |
| **Raffica di razzi** | 6.500 a razzo, uno ogni 15 s | 8.125 a razzo, uno ogni 15 s | 9.750 a razzo, uno ogni 15 s |
| **Assorbimento dello scudo** | 10.000 di scudo al secondo | 12.500 di scudo al secondo | 15.000 di scudo al secondo |
| **Supporto dello sciame** | 12 Goombahs | 18 Goombahs | 24 Goombahs |
| **Zona del Caos** | I piloti dentro l’anello non possono attaccare | I piloti dentro l’anello non possono attaccare | I piloti dentro l’anello non possono attaccare |

<!-- dungeons-abilities:end -->

## Zone del bottino {#loot-zones}

Un anello sul pavimento del labirinto segna ogni zona del bottino non appena il gruppo l’ha trovata. Resta un momento al suo interno e la zona si sveglia, e un’ondata di alieni si dirige verso di essa. Allora il gruppo deve **tenere** la zona: lasciare un pilota dentro finché la barra si riempie. Più piloti ci sono nell’anello, più in fretta si riempie la barra: un numero accanto alla barra dice quante volte più in fretta, e la tabella qui sotto dà i tempi. Abbastanza alieni nell’anello fermano la barra (l’elenco qui sotto dice quanti), e la barra torna indietro finché nessuno è dentro, quindi elimina prima l’ondata. Quando la zona si apre, il gruppo vede tre carte diverse e **vota** per una. Una zona si apre una volta sola, e la sua ondata non torna.

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Zone del bottino**: 6 in ogni labirinto
- **Raggio**: 450 unità
- **Risveglio**: Resta dentro l’anello per 2 s
- **Tenuta**: Tieni un pilota dentro per 30 s. La barra si ferma finché ci sono 3 o più alieni nell’anello e torna indietro finché non c’è nessuno
- **Scelta**: Il gruppo ha 45 s per votare. Il voto finisce prima se ogni pilota presente ha votato o se una carta ha più della metà dei voti

Più piloti nell’anello tengono una zona più in fretta. Quanto ci vuole per tenere una zona:

| Piloti nell’anello | Tempo per tenere la zona |
| :--- | ---: |
| 1 | 30 s |
| 2 | 20 s |
| 3 | 15 s |
| 4 | 12 s |
| 5 o più | 10 s |

<!-- dungeons-zones:end -->

### Booster {#boosters}

Alle fasi 2 e 3 le ondate delle zone del bottino portano anche dei booster. Quando il gruppo ha distrutto tutti gli alieni di un’ondata, l’ondata conta, e dopo ogni seconda ondata (la seconda, la quarta e la sesta) ogni pilota riceve una finestra di mezzo minuto per scegliere un booster temporaneo per sé: **Danni** (i tuoi laser colpiscono più forte), **Punti scafo** (la tua nave regge più scafo) o **Velocità** (la tua nave vola più veloce). Premi una carta per sceglierla. Se non rispondi in tempo, il gioco sceglie Punti scafo per te. Una scelta vale il 3% alla fase 3 e l’1,5% alla fase 2, e un tipo si somma fino al 9% alla fase 3 e al 4,5% alla fase 2, per quante volte lo scegli. La fase 1 non ha booster. Un gruppo che lascia viva un’ondata non ottiene la finestra per essa.

Un booster dura finché il dungeon non è completato. Se esci dal dungeon, o vieni distrutto, perdi i tuoi booster, e li riottieni quando rientri in volo. Un’etichetta sotto la finestra Dungeon del clan elenca quelli che hai.

### Le carte {#the-cards}

Le carte vengono estratte una alla volta dal mazzo qui sotto. La probabilità è quella di una carta in un’estrazione. Ogni carta va a ogni pilota pagato, comprese le carte di equipaggiamento: una carta con molte copie ne dà altrettante a ciascuno, e una carta di equipaggiamento dà a ciascuno un pezzo suo, forgiato per lui. Un pilota che non viene pagato non riceve nemmeno la carta, e una zona aperta in un dungeon che fallisce non paga nulla.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Carta | Fase 1 | Fase 2 | Fase 3 | Probabilità | Va a |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2.000 | 3.000 | 5.000 | 23,9% | Ogni pilota pagato |
| Velkonite Reinforced Plate | 10 | 15 | 25 | 13,65% | Ogni pilota pagato |
| Velkonite | 200 | 300 | 500 | 13,65% | Ogni pilota pagato |
| Orvium | 200 | 300 | 500 | 13,65% | Ogni pilota pagato |
| Ultra Core | 5.000 | 7.500 | 12.500 | 11,4% | Ogni pilota pagato |
| Experimental Fusion Core | 3.000 | 4.500 | 7.500 | 9,1% | Ogni pilota pagato |
| Dark Matter | 5 | 8 | 12 | 9,1% | Ogni pilota pagato |
| Dark Matter Plate | 1 | 1 | 2 | 4,55% | Ogni pilota pagato |
| Starfire-III | – | – | 1 | 0,07% | Ogni pilota pagato |
| Helios Beam | – | – | 1 | 0,07% | Ogni pilota pagato |
| Engine III | – | – | 1 | 0,07% | Ogni pilota pagato |
| Adaptive Core III | – | – | 1 | 0,07% | Ogni pilota pagato |
| Heavy Shield Core | – | – | 1 | 0,07% | Ogni pilota pagato |
| Momentum Thruster IV | – | – | 1 | 0,07% | Ogni pilota pagato |
| Impulse Thruster IV | – | – | 1 | 0,07% | Ogni pilota pagato |
| Hull Plating II | – | – | 1 | 0,07% | Ogni pilota pagato |
| Hull Plating III | – | – | 1 | 0,07% | Ogni pilota pagato |
| Damage Amp IV | – | – | 1 | 0,07% | Ogni pilota pagato |
| Crit Amp IV | – | – | 1 | 0,07% | Ogni pilota pagato |
| Penetration Amp IV | – | – | 1 | 0,07% | Ogni pilota pagato |
| Capacity Shield Cell IV | – | – | 1 | 0,08% | Ogni pilota pagato |
| Absorption Shield Cell IV | – | – | 1 | 0,08% | Ogni pilota pagato |

- **Equipaggiamento**: Le carte con un solo esemplare sono equipaggiamento: insieme 1% delle carte

<!-- dungeons-cards:end -->

Le carte con una sola copia sono **equipaggiamento**, e solo un dungeon di fase 3 può offrirle. Un pezzo di equipaggiamento viene forgiato per ogni pilota pagato al momento del pagamento: ciascuno tira un proprio [grado di incantamento](/wiki/06-Items/Overview.md#item-enchants) con le stesse probabilità di un pezzo che costruisci nell’Assemblaggio, quindi la maggior parte esce Standard, e un grado più alto, fino a Eterno, con potenziamenti, è un ritrovamento raro.

## Paga {#pay}

Quando il Signore della guerra cade, ogni pilota che se l’è guadagnata viene pagato, una volta per partita. Le carte scelte dal gruppo si aggiungono alla paga della fase. Non c’è moltiplicatore di mondo: la paga è la stessa in ogni mondo.

Le **Orvium Reinforced Plates** non sono una carta del voto. Fanno parte della paga della fase, e ogni pilota pagato le riceve una volta per il completamento. Gli oggetti che un dungeon paga non sono vendibili: non puoi [venderli all’Asta](/wiki/03-Mechanics/Auction.md#marketable-items).

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fase | Onore | Esperienza | Crediti | Thulium | Munizioni x4 | Orvium Reinforced Plates | Punti classifica PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Fase 1** | 25.000 | 600.000 | 5.000.000 | 4.000 | 4.000 | 5 | 600 |
| **Fase 2** | 50.000 | 1.500.000 | 10.000.000 | 9.000 | 9.000 | 10 | 1.500 |
| **Fase 3** | 100.000 | 2.400.000 | 17.500.000 | 15.000 | 15.000 | 15 | 2.400 |

<!-- dungeons-pay:end -->

### Chi viene pagato {#who-is-paid}

Gli alieni non pagano mai. Una partita si gioca per intero anche quando non paga nulla, e la schermata dei risultati dice perché. L’ingresso non viene mai rifiutato perché sei già stato pagato per una fase: quella partita semplicemente non paga.

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Un giorno**: Una fase paga un pilota una volta per giorno UTC: il giorno in cui cade il Signore della guerra
- **Una settimana**: Un pilota è pagato per al massimo 10 fasi completate per settimana UTC, da lunedì a domenica
- **Dentro**: Almeno 2 min in tutto
- **Parte nello scontro**: Almeno una di queste: ha inflitto 2% dello scafo e dello scudo del Signore della guerra; ha distrutto 10 alieni del dungeon; ha curato altri piloti per 50.000 durante lo scontro con il Signore della guerra

<!-- dungeons-rules:end -->

### Quanto valgono un giorno e una settimana {#what-a-day-and-a-week-are-worth}

Ciò che un pilota può ricevere in un giorno, e nella settimana migliore che i limiti consentono. L’ultima colonna è ciò che la paga aggiunge ai tuoi [punti PvE](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points).

<!-- dungeons-totals:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Paga per ogni pilota | Onore | Esperienza | Crediti | Thulium | Munizioni x4 | Orvium Reinforced Plates | Punti classifica PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Un giorno, ogni fase una volta | 175.000 | 4.500.000 | 32.500.000 | 28.000 | 28.000 | 30 | 4.500 |
| La settimana migliore: 7 × Fase 3 e 3 × Fase 2 | 850.000 | 21.300.000 | 152.500.000 | 132.000 | 132.000 | 135 | 21.300 |

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
- **Piloti pagati**: Almeno 3 nel dungeon

<!-- dungeons-clan:end -->

## Consigli {#tips}

- Elimina l’ondata di una zona prima di provare a tenerla, e combatti dentro l’anello se gli alieni entrano.
- Porta tutto il gruppo in una zona: più piloti ci sono nell’anello, più in fretta viene tenuta.
- Esplora il labirinto e distruggi gli alieni che incontri: il portello del Signore della guerra si apre quando tre quarti di loro sono morti, e non prima.
- Usa le pareti: i laser non le attraversano, gli anelli rossi delle aure del Signore della guerra si fermano contro di esse, e una parete ferma anche i razzi del Signore della guerra.
- Tieni da parte una EMP Charge per la Raffica di razzi.
- Quando il Signore della guerra chiama i suoi Goombah, distruggili per primi: non può essere ferito finché non sono spariti. Nella Zona del Caos, esci dall’anello prima di sparare.
- Controlla l’orologio nella finestra Dungeon del clan. Quando il tempo finisce, il dungeon fallisce e non paga nulla.
