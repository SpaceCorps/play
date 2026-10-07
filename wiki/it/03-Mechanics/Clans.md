<!-- wiki-i18n source: 5326d0eb87e5eb5c -->
<!-- wiki-i18n title: Clan -->
# Clan {#clans}

Fondare un clan o entrare in uno ti permette di mettere in comune le risorse, potenziare la banca condivisa, fissare le aliquote fiscali, coordinarti con i membri della tua fazione e gestire la diplomazia. Un clan ha anche del lavoro da fare insieme: ogni giorno riceve una **linea giornaliera** di missioni che termina con un boss che solo il clan può danneggiare, e i punti che guadagna comprano **potenziamenti permanenti** per ogni membro. (Nella pagina Clan del gioco un clan si chiama *flotta*; i suoi punti e potenziamenti vi sono chiamati punti flotta e potenziamenti della flotta.)

**In un minuto**

- Ogni giorno di stagione il tuo clan riceve una [linea giornaliera](#daily-line): quattro missioni da fare in ordine (abbattere alieni, percorrere una distanza, in alcuni giorni sconfiggere boss degli sciami), poi un [Custode del clan](#clan-wardens), un boss che convochi tu e che solo il tuo clan può danneggiare.
- Ogni fase completata paga subito punti clan: 15, 15, 20, 20 e 30, cioè **100 punti** per una linea intera.
- Il Leader e i Co-leader spendono i punti in tre [potenziamenti](#clan-points-and-boosts) di dieci livelli ciascuno: **Danno** (fino a +5%), **Thulium** (fino a +10%) e **Crediti** (fino a +10%).
- Un clan che completa ogni linea ha comprato ogni livello al **giorno 12 della stagione**. I punti e i livelli ricominciano a ogni reset.
- Servono almeno **tre membri** che abbiano fatto la loro parte e **circa sette piloti** per lo scontro con il Custode: cinque di solito perdono e dieci vincono con facilità ([quale equipaggio serve](#how-big-a-crew)). Un equipaggio troppo piccolo perde lo scontro: il clan tiene allora i **70 punti** delle quattro missioni, ma la linea non è completata e non paga [la tua ricompensa](#the-reward-for-you).
- La tua nave mostra i potenziamenti che ha nella finestra **Booster**, su una scheda a parte ([dove vederli](#the-three-boosts)).
- La linea e i potenziamenti richiedono un gioco della versione 0.4.10 o successiva; la scheda nella finestra Booster, la 0.4.12 o successiva.

![The Boosters window in flight: the Clan boosts card under the timed boosters lists your clan's tag and each boost with its bonus and level](../../img/wiki-img/shots/clan-boosters-window.jpg)
![Buying a level of a clan boost: the sheet shows the level, the bonus the whole fleet gets and the cost in clan points](../../img/wiki-img/shots/clan-boosts.jpg)
![Summoning a Warden for the clan](../../img/wiki-img/shots/clan-warden.jpg)

## Progressione del clan {#clan-progression}

I clan iniziano al livello 1 e possono essere potenziati fino al livello 5. Potenziare il clan richiede crediti pagati dalla **banca del clan**. I potenziamenti aumentano la capacità di membri e i limiti giornalieri dei pagamenti.

| Livello del clan | Limite di membri | Limite giornaliero di pagamenti (per membro) | Costo di potenziamento (crediti) |
| :---: | :---: | :---: | :--- |
| **Livello 1** | 10 | 1.000.000 Cr | — |
| **Livello 2** | 25 | 2.000.000 Cr | 10.000.000 Cr |
| **Livello 3** | 50 | 3.000.000 Cr | 100.000.000 Cr |
| **Livello 4** | 75 | 4.000.000 Cr | 1.000.000.000 Cr |
| **Livello 5** | 100 | 5.000.000 Cr | 10.000.000.000 Cr |

---

## Economia e tassazione del clan {#clan-economy-taxation}

I clan funzionano con un sistema finanziario basato sulle tasse:

### 1. Tassazione giornaliera {#1-daily-taxation}

- **Aliquota**: il Leader o i Co-leader possono fissare un’aliquota fiscale giornaliera tra lo **0% e il 5%**.
- **Prelievo automatico**: una volta al giorno (UTC), il server preleva automaticamente le tasse da tutti i membri del clan.
- **Formula**: la tassa è calcolata come `ClanTaxRate` del saldo attuale di crediti di ciascun membro.
  - *Esempio*: se hai 10.000.000 crediti e la tassa del clan è del 2%, 200.000 crediti verranno detratti dal tuo account e versati nella banca del clan.
  - Si possono fare anche donazioni volontarie di crediti, fino al limite indicato nella sezione successiva.

### 2. Donazioni {#2-donations}

- **Donare**: qualsiasi membro può inviare crediti alla banca del clan dalla pagina Clan. Il pannello mostra quanto puoi ancora inviare.
- **Limite di donazioni**: un pilota può inviare al massimo **1.000.000 crediti ai clan in qualsiasi periodo di 24 ore**, contando tutti i clan in cui è stato. Lasciare un clan ed entrare in un altro non azzera il limite.
- **Nessun azzeramento giornaliero**: le 24 ore scorrono. Ogni donazione smette di contare esattamente 24 ore dopo essere stata fatta, e il pannello ti dice quando succede per la più vecchia e quanto torna disponibile. Una donazione superiore a ciò che resta viene rifiutata per intero.
- La tassa giornaliera non è una donazione e non consuma il tuo limite.

### 3. Pagamenti dalla banca {#3-bank-payouts}

- **Limiti dei pagamenti**: i leader e gli ufficiali del clan possono distribuire crediti dalla banca del clan ai singoli membri.
- **Limite giornaliero**: un membro non può ricevere più di `1,000,000 * ClanLevel` crediti in pagamenti in un singolo giorno di calendario (UTC).

---

## Gerarchia e ruoli {#hierarchy-roles}

I clan usano una struttura di gradi basata sui ruoli per gestire i permessi:

- **Leader (ruolo 3)**: ha accesso amministrativo completo, compresi potenziamento, tasse, diplomazia, promozioni, espulsioni e scioglimento del clan.
- **Co-leader (ruolo 2)**: può fissare le aliquote fiscali, pagare crediti, gestire la diplomazia e promuovere o retrocedere i gradi inferiori.
- **Veterano (ruolo 1)**: membro di fiducia che può accettare le nuove richieste di ingresso nel clan.
- **Membro (ruolo 0)**: giocatore standard senza permessi amministrativi.

### Tabella dei permessi {#permissions-table}

| Azione | Leader | Co-leader | Veterano | Membro |
| :--- | :---: | :---: | :---: | :---: |
| **Sciogliere il clan** | ✅ | ❌ | ❌ | ❌ |
| **Potenziare il clan** | ✅ | ❌ | ❌ | ❌ |
| **Fissare l’aliquota** | ✅ | ✅ | ❌ | ❌ |
| **Pagare crediti** | ✅ | ✅ | ❌ | ❌ |
| **Gestire la diplomazia** | ✅ | ✅ | ❌ | ❌ |
| **Comprare i potenziamenti del clan** | ✅ | ✅ | ❌ | ❌ |
| **Convocare il Custode del clan** | ✅ | ✅ | ❌ | ❌ |
| **Promuovere / espellere** | ✅ | ✅* | ❌ | ❌ |
| **Accettare le richieste** | ✅ | ✅ | ✅ | ❌ |

*\*I Co-leader possono promuovere, retrocedere o espellere solo membri di grado inferiore al proprio.*

### Quando il Leader se ne va {#when-the-leader-leaves}

Un Leader non può lasciare un clan che ha ancora altri membri: prima promuovi un Co-leader a Leader (il Leader passa a Co-leader), oppure esci per ultimo, cosa che scioglie il clan. Se il Leader elimina il proprio account (Impostazioni › Account), la guida passa al membro di grado più alto, a parità a quello con più anzianità nel clan; un Leader rimasto solo nel clan lo scioglie, banca compresa.

---

## Linea giornaliera {#daily-line}

Ogni clan riceve una **linea giornaliera** al giorno: cinque fasi, da fare **in ordine**, da tutto il clan insieme. Le prime quattro sono missioni: abbattere tanti alieni, percorrere tanta distanza o, in alcuni giorni, sconfiggere boss degli sciami. La quinta è un **Custode del clan**, un boss che convochi e distruggi. Apri **Comunità › Clan** e la sua scheda **Operazioni** per vedere la linea di oggi, la fase aperta con la sua barra, la tua parte e il tempo che resta.

### Le cinque fasi {#the-five-steps}

| Fase | Cosa | Punti clan |
| :---: | :--- | ---: |
| 1 | Prima missione | 15 |
| 2 | Seconda missione | 15 |
| 3 | Terza missione | 20 |
| 4 | Quarta missione | 20 |
| 5 | Il Custode del clan del giorno | 30 |
| | **Una linea completata** | **100** |

- Conta solo la **fase aperta**. Un abbattimento fatto mentre la fase 1 è aperta conta per la fase 1 e per nient’altro. Quando la fase 1 è completata, la fase 2 si apre da zero. Quello che abbatti oltre l’obiettivo di una fase non viene conservato per la successiva.
- Una fase paga i suoi punti **nel momento in cui è completata**. Un clan che completa le quattro missioni e poi non riesce a mettere insieme un equipaggio per il Custode, o perde lo scontro, tiene comunque **70 punti**; [la tua ricompensa](#the-reward-for-you) arriva solo con la linea completata.
- Il lavoro di tutti confluisce in **un unico conteggio condiviso**: gli abbattimenti dell’alieno della fase aperta e la distanza percorsa da tutti i tuoi membri si sommano, così nessuno deve fare una fase da solo.

### Il giorno {#the-day}

- Il giorno di un clan è un **giorno di stagione**: 24 ore contate dall’inizio della stagione ([Cronologia del reset](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule)). Una nuova linea parte alla stessa ora ogni giorno, che non è la mezzanotte UTC (la tassa giornaliera del clan continua a scattare a mezzanotte UTC). La scheda Operazioni fa il conto alla rovescia fino al cambio.
- Una linea che non viene completata **scade** quando finisce il giorno. Le fasi già completate tengono i loro punti, il progresso della fase aperta va perso e non si recupera. Le linee vanno dai giorni di stagione 1 a 29.
- I piloti del clan che sono online ricevono una riga di Sistema quando parte la nuova linea, quando una fase è completata e **un’ora prima del cambio** se la linea non è completata.

### Livelli di difficoltà {#difficulty-tiers}

Ogni giorno il gioco prende il **livello medio dei cinque piloti di livello più alto** del clan (tutti, se ne ha meno di cinque) e ne ricava il livello di difficoltà del giorno:

| Difficoltà | Livello medio | Custode |
| :--- | :--- | :---: |
| Recluta | meno di 4 | I |
| Veterano | da 4 a meno di 7 | II |
| Élite | 7 o più | III |

La difficoltà decide quanti alieni chiedono le missioni, quale alieno chiede la fase «pesante» e quanto è forte il Custode. **I punti sono gli stessi a ogni difficoltà.** I nuovi piloti di livello basso non abbassano la difficoltà: contano solo i cinque migliori.

### Chi conta {#who-counts}

- **Conta il totale del clan.** Le barre della scheda Operazioni sono quelle dell’intero clan.
- **Il tuo minimo.** Per condividere la ricompensa del giorno devi fare il **5% del lavoro del giorno**, circa otto minuti di vera caccia. La scheda lo mostra come «Il tuo lavoro di oggi: 312 su 469 unità». Un’unità di lavoro è un secondo di gioco: un abbattimento conta quanto ci vuole per trovare e distruggere quell’alieno, e un tratto di volo quanto ci vuole per percorrerlo. Per un clan Veterano un Seeker vale circa 12 unità, un Phantasm 22, un Bulwark 123 e 1.000 unità percorse circa 5; il minimo è da 446 a 480 unità, qualunque sia il giorno e la difficoltà.
- **Almeno tre membri** devono aver raggiunto il proprio minimo prima che una fase possa essere completata. Se una fase è piena e meno membri ci sono arrivati, **aspetta** («La fase 3 è piena, ma solo 2 membri hanno raggiunto il minimo»), e gli abbattimenti dell’alieno di quella fase continuano ad aggiungersi al lavoro dei membri che li hanno fatti finché non ci arriva il terzo. Un clan con meno di tre piloti non può completare nessuna fase.
- **A chi va un abbattimento.** Al pilota che viene pagato per l’abbattimento e ai suoi compagni di gruppo entro 4.000 unità che hanno sparato negli ultimi 15 secondi ([Gruppi](/wiki/03-Mechanics/Groups.md#sharing-kills)). Un clan conta un abbattimento **una sola volta**, quanti che siano i suoi piloti nel gruppo, e il lavoro dell’abbattimento viene diviso in parti uguali tra loro. Due clan in un gruppo lo contano una volta ciascuno.
- **Quali abbattimenti.** Solo l’alieno della fase aperta: il Seeker, Phantasm, Bulwark o Goombah normale. Le navi degli sciami, gli altri piloti e gli aiutanti di un Custode non contano come quegli alieni. Vale qualsiasi mondo, e un abbattimento conta di più in un mondo più forte: **1 in Alpha, 1,5 in Beta, 2 in Gamma** ([Mondi](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)). Una fase di boss conta i boss degli [sciami](/wiki/05-Swarms/Swarms.md), uno per ogni clan che ha un pilota che ha inflitto almeno il 5% dei danni.
- **Volare.** Una fase di pattuglia conta la distanza che ogni pilota percorre fuori dalle zone sicure; cinque piloti che volano insieme aggiungono cinque volte la distanza.
- **Entrare e uscire.** Quello che hai fatto resta contato se te ne vai. Un pilota che entra conta da quel momento.

### Le sette linee {#the-seven-lines}

Le linee seguono un ciclo di sette: la linea del giorno di stagione *d* è la numero 1 + ((*d* − 1) mod 7), quindi ognuna ritorna ogni sette giorni. I numeri sono per un clan **Recluta / Veterano / Élite**. Le due linee **Swarm Break** chiedono boss degli sciami e arrivano solo dal giorno 4, quando compaiono gli [sciami](/wiki/05-Swarms/Swarms.md). Tutti i numeri sono fatti per circa **2,6 ore di gioco in tutto**, mezz’ora a testa per cinque piloti (una stima, non una misura).

| Linea | Giorni di stagione | Fase 1 | Fase 2 | Fase 3 | Fase 4 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Seeker Sweep | 1, 8, 15, 22, 29 | 150 / 300 / 425 Seeker | 115.000 / 155.000 / 185.000 unità | 21 / 70 / 130 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah |
| Phantasm Purge | 2, 9, 16, 23 | 40 / 140 / 270 Phantasm | 60 / 120 / 170 Seeker | 175.000 / 230.000 / 275.000 unità | 26 Phantasm / 15 Bulwark / 17 Goombah |
| Long Haul | 3, 10, 17, 24 | 290.000 / 385.000 / 460.000 unità | 90 / 180 / 260 Seeker | 26 / 85 / 170 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah |
| Swarm Break I | 4, 11, 18, 25 | 75 / 150 / 220 Seeker | 3 Boss Seeker / 3 Boss Seeker / 2 Pirate Boss | 26 / 85 / 170 Phantasm | 30 Phantasm / 18 Bulwark / 21 Goombah |
| Heavy Iron | 5, 12, 19, 26 | 40 Phantasm / 24 Bulwark / 28 Goombah | 21 / 70 / 130 Phantasm | 175.000 / 230.000 / 275.000 unità | 75 / 150 / 220 Seeker |
| Swarm Break II | 6, 13, 20, 27 | 75 / 150 / 220 Seeker | 21 / 70 / 130 Phantasm | 4 Boss Seeker / 1 Pirate Boss / 3 Pirate Boss | 350.000 / 460.000 / 550.000 unità |
| Grand Round | 7, 14, 21, 28 | 100 / 210 / 300 Seeker | 26 / 85 / 170 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah | 230.000 / 305.000 / 365.000 unità |

### La tua ricompensa {#the-reward-for-you}

Quando la linea è completata, cioè quando il Custode è distrutto, ogni membro che ha raggiunto il minimo ed è ancora nel clan viene pagato, anche se è offline. Una linea che finisce senza il Custode non paga nessuna ricompensa, qualunque cosa abbiano fatto le quattro missioni. Il pagamento è fisso: non lo cambiano potenziamenti, booster né mondo.

| Difficoltà | Crediti | Thulium |
| :--- | ---: | ---: |
| Recluta | 5.000 | 20 |
| Veterano | 15.000 | 60 |
| Élite | 22.000 | 90 |

---

## Custodi del clan {#clan-wardens}

Un **Custode del clan** è il boss alla fine della linea giornaliera. Non è uno degli [sciami](/wiki/05-Swarms/Swarms.md) pubblici che si aggirano in un settore: il tuo clan **lo convoca** e **solo il tuo clan può danneggiarlo**. Tre Custodi si alternano, uno al giorno: giorno 1 **Brood**, giorno 2 **Siege**, giorno 3 **Wrath**, giorno 4 di nuovo Brood, e così via (il giorno 15 è un giorno Wrath). Ognuno esiste in tre potenze, **I, II e III**, stabilite dalla difficoltà del clan. Un Custode è un alieno di un genere a parte, come le navi di uno sciame: non conta come Seeker, Phantasm né altro alieno. I suoi laser colpiscono duro, quindi un Custode è uno scontro per un equipaggio al completo: porta circa sette piloti, perché cinque di solito perdono ([quale equipaggio serve](#how-big-a-crew)).

| Custode | Giorni di stagione | Ruolo | Come combatte |
| :--- | :--- | :--- | :--- |
| **Brood Warden** | 1, 4, 7, 10 … | Custode dell’alveare: dividi il fuoco | Quattro piccoli **Brood Drone** curano il suo scafo, e ne arriva uno nuovo ogni 8 secondi finché ne sono vivi meno di quattro. Abbatti prima i droni, poi il Custode. |
| **Siege Warden** | 2, 5, 8, 11 … | Spezzaassedi: non fermarti mai | Si aggira e lancia un [razzo Rivet](/wiki/06-Items/Rockets.md#the-twelve-rockets) dritto contro il primo pilota che lo ha colpito, e si ripara da solo. Due **Siege Escort** aggiungono fuoco laser. Non fermarti e fate a turno da bersaglio. |
| **Wrath Warden** | 3, 6, 9, 12 … | Signore della guerra: batti la furia | Combatte sul posto e si ripara da solo. Sotto metà scafo i suoi laser colpiscono **una volta e mezza più forte**. Due **Wrath Guard** aggiungono fuoco laser. Abbattilo in fretta e tieni alti gli scudi. |

### Convocare un Custode {#calling-a-warden}

- **Quando.** Dopo che la fase 4 è completata. Un clan ha **due convocazioni al giorno**, un solo Custode fuori alla volta, e al giorno devono restare **almeno 30 minuti**.
- **Chi.** Il Leader o un Co-leader.
- **Come.** In volo: il pulsante **Convoca qui** compare sulla schermata di volo appena la fase 4 è completata, e ti chiede di confermare. Stai fuori dalle zone sicure, in un settore di corporazione **x-2, x-3 o x-4** (di qualsiasi corporazione) del tuo mondo. La scheda Operazioni mostra il Custode del giorno, le convocazioni rimaste e perché il pulsante è attenuato, ma un Custode si convoca dalla nave.
- **Dove compare.** A 3.000–4.500 unità dalla tua nave, nel tuo mondo: solo i piloti di quel mondo possono raggiungerlo. La scheda consiglia **x-2 per un clan Recluta, x-3 per Veterano e x-4 per Élite**. Valgono ancora le consuete [regole PvP](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) del settore che scegli.
- **Riscaldamento.** Resta per **90 secondi** schermato e passivo («in carica») e ogni pilota del clan online viene informato di dove. Vola verso di lui mentre si carica: passati i 90 secondi è attivo. Una capsula sotto il distintivo della zona sicura sulla schermata di volo lo segue: il suo nome, «in carica» con il tempo che manca, poi «attivo» con il suo settore e il tempo che manca al ritiro, e «furioso» quando un Wrath Warden scende sotto metà scafo.
- **Solo il tuo clan.** I colpi dei piloti di qualsiasi altro clan vengono ignorati e non lo fanno reagire.
- **Come finisce.** Quando viene distrutto. Si **ritira** 40 minuti dopo essersi attivato, quando finisce il giorno, quando nessun pilota del tuo clan è in volo sulla sua mappa da 2 minuti, o quando il server si riavvia (quella convocazione ti viene restituita). Un Custode che si ritira costa una convocazione, e la chiamata successiva è lo stesso Custode a piena potenza.

### Combattere un Custode {#fighting-a-warden}

- **Un Custode combatte il primo pilota che lo ha colpito**, come ogni boss: lascia cominciare la nave più robusta dell’equipaggio e usa [Shield Surge ed Emergency Repair](/wiki/03-Mechanics/Abilities.md).
- **Porta circa sette piloti, con munizioni x2** ([Laser](/wiki/06-Items/Lasers.md#laser-ammunition)). Cinque di solito perdono e dieci vincono con facilità. La tabella qui sotto è il caso migliore, e anche in esso tre perdono contro ogni Custode e quattro vincono solo contro i Siege Warden I e II. Nella tabella l’equipaggio più piccolo che può vincere ha da 4 a 5 piloti con munizioni x2 e da 6 a 8 con munizioni x1.
- **Brood:** i droni curano il suo scafo, e un equipaggio che li ignora perde: cinque piloti che sparano solo al Custode cadono tutti quando ne resta in piedi circa la metà, e dieci impiegano circa un quinto di tempo in più. Abbattili per primi: uno muore in un secondo o meno sotto il fuoco di cinque piloti, e il successivo arriva dopo 8 secondi.
- **Siege:** i suoi razzi sono dritti e non guidati, quindi una nave che continua a muoversi ne schiva la maggior parte. Non fermarti e fate a turno da bersaglio.
- **Wrath:** quando il suo scafo scende sotto la metà, ogni raffica colpisce una volta e mezza più forte, quindi la seconda metà dello scontro è quella pericolosa. Abbatti in fretta la prima metà, tieni alti gli scudi e conserva Emergency Repair per la furia.

### Quale equipaggio serve {#how-big-a-crew}

> [!NOTE]
> Questi tempi sono **calcolati** dai numeri qui sotto, non misurati in gioco. L’equipaggio ha le navi e l’equipaggiamento per cui è pensata la difficoltà, e la tabella è il suo **caso migliore**: ogni pilota usa Shield Surge ed Emergency Repair appena sono pronti, e l’equipaggio spara prima agli aiutanti del Custode quando è meglio. Il Custode e i suoi aiutanti sparano tutti al pilota che ha colpito per primo e nessuno schiva. **Uno scontro vero è più duro della tabella.** La riga dei cinque piloti è risicata anche nel caso migliore (una vittoria che costa una o due navi), e negli stessi scontri svolti nel gioco vero e proprio, con piloti guidati da script, cinque piloti hanno perso la maggior parte degli scontri che abbiamo fatto, anche usando entrambe le abilità; sette li hanno vinti tutti e dieci hanno vinto con facilità. Un equipaggio di cinque piloti che non usa nessuna abilità e spara solo al Custode perde contro sette dei nove Custodi; sette piloti che fanno lo stesso ne battono otto (tutti tranne il Brood Warden III, che i suoi droni curano) e perdono da una a tre navi, e dieci li battono tutti e nove.

La tabella è il caso migliore, con munizioni x2; in gioco cinque piloti di solito perdono e circa sette vincono.

| Equipaggio | Con munizioni x2 | Con munizioni x1 |
| :--- | :--- | :--- |
| 3 piloti | perdono contro ogni Custode, dopo 4,7–13,8 minuti; il Custode conserva tra un quarto e due terzi di scafo e scudo | perdono |
| 4 piloti | vincono solo contro i Siege Warden I e II, in circa 8 minuti, perdendo 1 nave | perdono |
| 5 piloti | vincono contro ogni Custode in 5,3–6,5 minuti, perdendo da 1 a 2 navi | perdono |
| 7 piloti | vincono contro ogni Custode in 3,3–3,6 minuti, perdendo da 0 a 1 navi | vincono contro ogni Custode tranne i Brood Warden II e III, in 8,7–12,3 minuti, perdendo da 1 a 4 navi |
| 10 piloti | vincono contro ogni Custode in 2,2–2,4 minuti, perdendo da 0 a 1 navi | vincono contro ogni Custode in 5,1–5,6 minuti, perdendo da 1 a 2 navi |

Nel caso migliore l’equipaggio più piccolo che vince con munizioni x2 ha da **4 piloti** (contro i Siege Warden I e II) a **5** (contro gli altri sette) e perde da **1 a 2** navi nel farlo; con munizioni x1 ha da **6 a 8** piloti e ne perde da 2 a 4. Un equipaggio di **sette** vince contro ogni Custode con munizioni x2 e nel caso migliore perde al massimo una nave. I laser di un Custode colpiscono con decine di danni a raffica, fino a oltre cento, in potenza I (da 48 a 129) e con migliaia in potenza III (da 1.845 a 3.090), e i suoi aiutanti si sommano: la nave contro cui combatte cade tra un minuto e mezzo e quattro minuti, poi passa alla successiva, quindi anche un equipaggio che vince perde delle navi.

La tabella vale per un equipaggio con l’equipaggiamento della difficoltà propria del Custode. Navi più deboli fanno peggio: dieci piloti con equipaggiamento da Recluta non possono uccidere un Custode Veterano, né dieci da Veterano un Custode Élite. Il Custode del **tuo** clan corrisponde sempre alla **tua** difficoltà, che fissano i cinque migliori piloti del clan, quindi portali.

**Un clan troppo piccolo per il suo Custode** (meno di circa sette piloti quel giorno) non resta escluso. Le quattro missioni pagano i loro **70 punti** qualunque cosa succeda al Custode, i punti comprano potenziamenti e il clan può richiamare il Custode se gli resta una convocazione (sono due al giorno): se l’equipaggio cade e resta lontano, il Custode si ritira, il che costa una convocazione, e la chiamata successiva lo riporta a piena potenza. Ma la linea non è completata, quindi nessuno riceve [la tua ricompensa](#the-reward-for-you), e un clan che non uccide mai il suo Custode ha tutti i 30 livelli di potenziamento al più presto il giorno di stagione 18, non il giorno 12 ([quanto ci vuole](#how-long-it-takes)).

### I numeri dei Custodi {#warden-numbers}

I Custodi hanno gli stessi numeri in ogni mondo (quelli di Alpha), e così la loro ricompensa. Ogni drone, scorta o guardia ha i numeri della seconda tabella, e restano accanto al Custode: un Brood Drone cura lo scafo del Custode, una Siege Escort o una Wrath Guard spara con i laser. Una raffica sono i colpi di tutti i laser di una nave in un secondo, estratti tra l’80 e il 100% del numero mostrato; un Wrath Warden sotto metà dello scafo colpisce una volta e mezza più forte. Il Custode e i suoi aiutanti sparano tutti al pilota contro cui combatte il Custode, quindi le loro raffiche si sommano: un Brood Warden III con i suoi quattro droni mette fino a 4.350 al secondo su una sola nave. Il [razzo Rivet](/wiki/06-Items/Rockets.md#the-twelve-rockets) del Siege Warden non è estratto a sorte: colpisce con al massimo **2.500** in potenza I, **5.000** in potenza II e **7.500** in potenza III, mentre il Rivet di un pilota è estratto tra un numero minimo e uno massimo. Va dritto, quindi una nave che continua a muoversi viene mancata.

| Custode | Scafo | Scudo | Danno dei laser (una raffica al secondo) | Velocità | Portata dei laser | Si ripara da solo (scafo al secondo) | Razzo e secondi tra i colpi |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| Brood Warden I | 166.000 | 136.000 | 129 | 90 | 600 | – | – |
| Brood Warden II | 288.000 | 236.000 | 777 | 90 | 700 | – | – |
| Brood Warden III | 1.060.000 | 870.000 | 3.090 | 90 | 800 | – | – |
| Siege Warden I | 143.000 | 117.000 | 48 | 110 | 600 | 215 | Rivet I: 24 |
| Siege Warden II | 248.000 | 203.000 | 291 | 110 | 700 | 375 | Rivet II: 12 |
| Siege Warden III | 915.000 | 745.000 | 1.845 | 110 | 800 | 1.385 | Rivet III: 8 |
| Wrath Warden I | 163.000 | 133.000 | 96 | 90 | 700 | 215 | – |
| Wrath Warden II | 282.000 | 231.000 | 582 | 90 | 800 | 375 | – |
| Wrath Warden III | 1.040.000 | 850.000 | 2.460 | 90 | 900 | 1.385 | – |

| Aiutante | Quanti | Scafo | Scudo | Danno dei laser (una raffica al secondo) | Velocità | Cura il Custode (scafo al secondo) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Brood Drone I | 4 | 700 | 500 | 12 | 170 | 120 |
| Brood Drone II | 4 | 1.200 | 900 | 78 | 170 | 210 |
| Brood Drone III | 4 | 4.000 | 3.500 | 315 | 170 | 770 |
| Siege Escort I | 2 | 4.300 | 3.500 | 6 | 175 | – |
| Siege Escort II | 2 | 7.400 | 6.100 | 45 | 175 | – |
| Siege Escort III | 2 | 27.500 | 22.500 | 285 | 175 | – |
| Wrath Guard I | 2 | 4.900 | 4.000 | 18 | 180 | – |
| Wrath Guard II | 2 | 8.500 | 6.900 | 117 | 180 | – |
| Wrath Guard III | 2 | 31.000 | 25.500 | 495 | 180 | – |

### Ricompensa e bottino {#warden-pay-and-loot}

Un Custode paga quanto una pila dell’alieno pesante della difficoltà: **30 Phantasm** per un Custode I, **24 Bulwark** per un II e **16 Goombah** per un III. È un unico montepremi, diviso in base ai danni tra i piloti che hanno inflitto almeno il 5% dei danni, come per il capo di uno [sciame](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays). I tuoi [potenziamenti del clan](#what-the-boosts-apply-to) valgono per la tua parte. Secondo i nostri calcoli i crediti coprono più o meno le munizioni x1 che brucia l’equipaggio più piccolo che può vincere, e le munizioni x2 costano più Thulium di quanto ne paghi il Custode: è uno scontro per i punti e per la cassa. La ricompensa non è cambiata nella 0.4.12, quando i laser dei Custodi sono diventati più forti: la somma non cresce con il danno che subisci né con le navi che perdi.

| Potenza del Custode | Crediti | Thulium | Esperienza (XP) | Onore |
| :--- | ---: | ---: | ---: | ---: |
| I | 90.000 | 360 | 9.000 | 180 |
| II | 120.000 | 600 | 19.200 | 240 |
| III | 240.000 | 1.200 | 48.000 | 384 |

Il Custode lascia **una cassa** per il pilota che ha inflitto più danni; è sua e del suo clan per 30 secondi ([Carico](/wiki/03-Mechanics/Cargo.md)). Una probabilità tra parentesi vale per ciascuno dei tiri indicati: (5 × 50%) sono cinque tiri con il 50% di probabilità ciascuno.

| Custode | Oggetto | I | II | III |
| :--- | :--- | :---: | :---: | :---: |
| Brood Warden | Ship Fragment | 3–5 | 8–12 | 15–25 |
| Brood Warden | Advanced Plasma | 100–200 | 300–600 | – |
| Brood Warden | Daraxium | 1–2 (5 × 50%) | – | – |
| Brood Warden | Nyxite | – | 2–4 (5 × 50%) | – |
| Brood Warden | Ultra Core | – | – | 300–500 |
| Brood Warden | Quorvium | – | – | 5–10 (60%) |
| Siege Warden | Ship Fragment | 2–4 | 6–10 | 12–20 |
| Siege Warden | Siphon Battery | 100–200 | 300–500 | 800–1.200 |
| Siege Warden | Razzo acquistabile con i crediti (un tipo, a caso) | 2–3 | 5–8 | 8–12 |
| Siege Warden | Reinforced Hull Plate | – | 1 (30%) | – |
| Siege Warden | Razzo epico (un tipo, a caso) | – | – | 1–2 (50%) |
| Wrath Warden | Ship Fragment | 4–6 | 8–12 | – |
| Wrath Warden | Cataclysite | 3–5 | 5–10 | – |
| Wrath Warden | Reinforced Hull Plate | 1 (25%) | 1 (50%) | 1–2 (70%) |
| Wrath Warden | Power Core | – | 1 (15%) | 1 (35%) |
| Wrath Warden | Quorvium | – | – | 5–10 (70%) |
| Wrath Warden | Ancient Control Unit | – | – | 1 (8%) |

Un Custode viene contato con il proprio nome nelle tue statistiche degli abbattimenti e aggiunge punti PvE al tuo [grado](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points): **da 13 a 35** per il capo, secondo il Custode e la sua forza (un Custode III vale di più), e **da 1 a 6** per ogni aiutante, di più per un equipaggio più forte.

---

## Punti e potenziamenti del clan {#clan-points-and-boosts}

I punti clan appartengono al clan. Ogni fase che il clan completa si aggiunge al suo saldo. Il **Leader e i Co-leader** lo spendono nella scheda **Potenziamenti della flotta** della scheda Operazioni: tre potenziamenti di dieci livelli ciascuno, e ogni membro li ha subito. Un acquisto è definitivo: niente rimborso e niente riassegnazione.

### I tre potenziamenti {#the-three-boosts}

| Potenziamento | Livelli | Per livello | Livello massimo | Agisce su |
| :--- | :---: | :---: | :---: | :--- |
| **Danno flotta** | 10 | +0,5% | +5% | Danno laser contro alieni e piloti |
| **Thulium flotta** | 10 | +1% | +10% | Thulium da abbattimenti e ricompense delle missioni |
| **Crediti flotta** | 10 | +1% | +10% | Crediti da abbattimenti e ricompense delle missioni |

**Dove vederli.** In volo, la finestra **Booster** elenca i potenziamenti che ha la tua nave su una scheda a parte, **Potenziamenti della flotta**, sotto i booster a tempo: il tag del tuo clan, poi una riga per ogni potenziamento con il suo bonus e il suo livello (Liv. 3/10). Non hanno timer, perché un potenziamento del clan dura finché sei nel clan. Passa il mouse su una riga per vedere su cosa agisce. Un clan che non ha ancora comprato nulla mostra «La tua flotta non ha ancora potenziamenti», e un pilota senza clan non vede la scheda. Li elencano anche la scheda Booster della **Dashboard** e il profilo di un pilota. La scheda mostra ciò che la tua nave applica, come il server lo comunica al gioco, quindi un livello che gli ufficiali hanno appena comprato compare subito. Un gioco precedente alla 0.4.12 applica i potenziamenti e non mostra la scheda.

### Prezzi {#boost-prices}

Il prezzo di un livello è **22 punti clan più 4 per ogni livello precedente**, ed è lo stesso per i tre potenziamenti: 400 punti per un potenziamento, **1.200 per tutti e tre**, cioè dodici linee completate.

| Livello | Prezzo | Totale per questo potenziamento | Danno flotta | Thulium flotta | Crediti flotta |
| :---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 22 | 22 | +0,5% | +1% | +1% |
| 2 | 26 | 48 | +1% | +2% | +2% |
| 3 | 30 | 78 | +1,5% | +3% | +3% |
| 4 | 34 | 112 | +2% | +4% | +4% |
| 5 | 38 | 150 | +2,5% | +5% | +5% |
| 6 | 42 | 192 | +3% | +6% | +6% |
| 7 | 46 | 238 | +3,5% | +7% | +7% |
| 8 | 50 | 288 | +4% | +8% | +8% |
| 9 | 54 | 342 | +4,5% | +9% | +9% |
| 10 | 58 | 400 | +5% | +10% | +10% |

### Su cosa agiscono i potenziamenti {#what-the-boosts-apply-to}

- **Danno flotta** si aggiunge a tutto il danno laser che infligge la tua nave: ad alieni, navi degli sciami, Custodi e altri piloti. **Non tocca i razzi**, di nessun tipo.
- **Thulium flotta e Crediti flotta** si aggiungono alla ricompensa degli abbattimenti di alieni (i tuoi, la tua parte di un boss e la tua parte di un abbattimento di gruppo) e alla ricompensa di ogni missione che riscuoti, di livello, Stazione o Sfida ([Missioni](/wiki/03-Mechanics/Quests.md#rewards)). **Non toccano** le fattorie dello [Skylab](/wiki/03-Mechanics/Skylab.md#credit-farm-and-thulium-farm), i pagamenti della banca, i codici bonus né la ricompensa della linea giornaliera.
- **Si sommano ai tuoi altri bonus** (booster come il Laser Damage Booster, i bonus dell’[Emporio dei potenziamenti permanenti](/wiki/03-Mechanics/Wipe-Timeline.md#the-permanent-buff-store)): le percentuali si sommano. Gli amplificatori laser (Amp) non ne fanno parte: aggiungono danno fisso, e le percentuali si applicano al totale. Cinque punti di Danno flotta accanto a 50 da altre fonti fanno 55, cioè il 3,3% di danno in più di prima.
- **Una frazione non si perde.** Un potenziamento spesso aggiunge meno di un’unità a un abbattimento: il 10% dei 4 Thulium di un Seeker è 0,4. Il gioco conserva la frazione e la paga con le unità dei tuoi abbattimenti successivi, così dieci Seeker pagano i 4 che ti spettano. La frazione che hai in mano va persa quando esci dal gioco.
- **Entrare e uscire.** Un pilota ha i potenziamenti dal momento in cui entra nel clan e li perde nel momento in cui esce, viene espulso o il clan viene sciolto. Il clan conserva i suoi livelli.

### Quanto ci vuole {#how-long-it-takes}

Un clan che completa ogni linea guadagna 100 punti al giorno. Se gli ufficiali comprano in parti uguali nei tre potenziamenti, ha **4 livelli dopo la prima linea, 10 dopo la terza, 16 dopo la quinta e tutti e 30 al giorno di stagione 12**. Quando comincia il giorno 15 sono finite quattordici linee, quindi un clan così ha due linee di margine. Un giorno che non viene completato paga comunque le fasi fatte: un clan che supera le quattro missioni ma non uccide mai il suo Custode guadagna 70 punti al giorno e ha tutti i 30 livelli al più presto il giorno di stagione 18. Dopo l’ultimo livello la linea continua a girare e continua a pagare la tua ricompensa; i punti continuano ad aggiungersi a quanto il clan ha guadagnato in questa stagione, che il suggerimento dei punti clan sulla scheda Potenziamenti della flotta mostra.

### Punti e reset {#clan-points-and-the-wipe}

A ogni reset i **punti, i livelli dei potenziamenti e le linee del clan ricominciano da zero**, così ogni stagione è una nuova corsa ai potenziamenti al massimo. Il clan stesso, i suoi membri, la sua banca e la sua tassa restano come sono.

---

## Diplomazia {#diplomacy}

I clan possono stabilire relazioni diplomatiche formali con altre organizzazioni inserendo il tag del clan bersaglio:

- **Alleanza**: clan alleati in modo formale. Lo stato di amicizia viene mostrato sulla mappa.
- **Patto di non aggressione (NAP)**: ci si accorda per non avviare ostilità.
- **Guerra**: dichiarazione formale di guerra. I bersagli di guerra possono essere attaccati ovunque senza penalità.

---

## Portare un amico {#bringing-a-friend}

Un amico nuovo del gioco può entrare con il tuo codice invito personale e riceve un pacchetto iniziale; vedi [Invita amici](/wiki/03-Mechanics/Invite-Friends.md). Una volta nel gioco può candidarsi al tuo clan come qualsiasi pilota.
