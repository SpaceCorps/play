<!-- wiki-i18n source: 2599ac53be69ec9b -->
<!-- wiki-i18n title: Razzi -->
# Razzi {#rockets}

I razzi sono una seconda arma accanto ai laser: un colpo ogni pochi secondi che colpisce molto più forte di una raffica laser. Dodici razzi in quattro tipi, tre fasce per ciascun tipo, altri due che produce solo l’Assemblaggio, e **un solo timer di ricarica di 5 secondi che condividono tutti**, qualunque tu lanci. I razzi Comuni e Rari si comprano con i **crediti**; i quattro razzi Epici si comprano con il **Thulium**.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Albero degli oggetti {#item-tree}

Ciò che crea l’Assemblaggio richiede prima la sua tecnologia; passa il puntatore su un oggetto per vedere quanto tempo serve a ricercarla. L’albero delle tecnologie, il carburante e il boost: [Ricerca](/wiki/03-Mechanics/Research.md).

```tree
Lancet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets

Lancet I -> Lancet II -> Lancet III
Rivet I -> Rivet II -> Rivet III
Ember I -> Ember II -> Ember III
Scatter I -> Scatter II -> Scatter III => N.U.K.E.
```
<!-- item-tree:end -->

## I quattro tipi {#the-four-kinds}

| | Bersaglio singolo: colpisce una nave | Esplosione ad area: esplode e colpisce tutto ciò che è vicino |
| :--- | :--- | :--- |
| **Guidato**: aggancia il bersaglio selezionato e lo insegue | Lancet I, Lancet II, Lancet III | Ember I, Ember II, Ember III |
| **Dritto**: vola verso il cursore | Rivet I, Rivet II, Rivet III | Scatter I, Scatter II, Scatter III |

Ogni tipo è una **famiglia**, che prende il nome dal suo razzo comune, e la fascia è un numero romano: **Lancet I**, **Lancet II** e **Lancet III** sono il razzo guidato a bersaglio singolo comune, raro ed epico, e le famiglie Rivet, Ember e Scatter seguono lo stesso schema. Il codice di un razzo sulla sua casella nel selettore dei razzi e nell’Hangar è formato dalle tre lettere della sua famiglia e dal suo numero (LNC II, RVT III, EMB I, SCT II); i due razzi che si ottengono solo con la creazione mantengono nome e codice (N.U.K.E., NUK; N.I.K.E., NIK).

- I razzi **guidati** richiedono un bersaglio selezionato entro la loro **portata di aggancio** quando partono. Lo inseguono con una velocità di virata limitata, quindi una nave veloce e lontana può seminare un razzo economico. Se il bersaglio muore, se ne va o raggiunge una zona sicura, il razzo continua dritto e non ne sceglie un altro.
- I razzi **dritti** non richiedono un bersaglio e ignorano quello che hai selezionato: volano sempre verso il tuo **cursore**, nel punto sotto di esso nella vista di volo. **Clicca sullo slot di un razzo dritto per armarlo** (lo slot ottiene una cornice bianca e un mirino, e il cursore del mouse diventa un mirino sullo spazio), poi **clicca nello spazio**: il razzo vola verso il punto che hai cliccato e la tua nave resta dov’è. Esc, un clic destro o di nuovo lo stesso slot lo disarma. Se i razzi si stanno ancora ricaricando, il clic te lo segnala soltanto e il razzo resta armato. I tasti numerici e **Lancia razzo** sparano subito verso l’ultimo punto in cui si trovava il cursore nella vista di volo; se il cursore non c’è ancora stato, volano nella direzione verso cui **punta** la tua nave. Volano dritti, quindi una nave che attraversa a velocità può schivarli.
- Un razzo a **bersaglio singolo** colpisce la prima nave che può colpire (uno guidato solo il suo bersaglio). Un’**esplosione ad area** esplode accanto alla prima nave che incontra, nel punto in cui l’hai mirata o dove finisce il suo volo, e danneggia ogni nave dentro il suo **raggio dell’esplosione**: danno pieno al centro, meno verso il bordo. L’anello che l’esplosione disegna sulla mappa è la sua portata esatta.

## I dodici razzi {#the-twelve-rockets}

Ogni razzo ha **il proprio danno, stabilito a caso quando lo lanci**: tra l’**80% e il 100%** del suo numero massimo, e la tabella mostra il più basso e il più alto. È lo stesso per chiunque lo lanci: non dipende dalla tua nave, dai tuoi laser, dai tuoi Damage Amp, dai tuoi booster, dalle tue munizioni o dai tuoi droni, e un razzo non fa mai colpi critici. Un razzo a bersaglio singolo infligge il danno stabilito alla nave che colpisce; un’esplosione lo stabilisce una volta sola e lo infligge a **ogni nave al suo interno**, l’intero valore al centro e meno verso il bordo. La *penetrazione dello scudo* viene tolta all’assorbimento del bersaglio per quel colpo (l’assorbimento di una nave è la quota di un colpo che i suoi scudi prendono, vedi [Meccaniche degli scudi](/wiki/03-Mechanics/Shields.md#shield-penetration)): il 35% di un Lancet III lascia agli scudi di una nave all’80% il 45% del colpo e manda l’altro 55% allo scafo. Un’esplosione non ne ha.

| Nome | Tipo | Rarità | Danno | Penetrazione scudo | Raggio dell’esplosione | Portata di aggancio | Portata | Velocità | Prezzo | Massimo trasportabile |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **Lancet I** | Guidato, bersaglio singolo | Comune | 1.600–2.000 | 10% | – | 700 | 1.040 | 520 | 500 crediti | 5.000 |
| **Lancet II** | Guidato, bersaglio singolo | Raro | 3.200–4.000 | 25% | – | 1.000 | 1.584 | 660 | 800 crediti | 2.000 |
| **Lancet III** | Guidato, bersaglio singolo | Epico | 4.800–6.000 | 35% | – | 1.300 | 2.296 | 820 | 5 Thulium | 500 |
| **Rivet I** | Dritto, bersaglio singolo | Comune | 2.000–2.500 | 5% | – | – | 1.080 | 900 | 500 crediti | 5.000 |
| **Rivet II** | Dritto, bersaglio singolo | Raro | 4.000–5.000 | 25% | – | – | 1.120 | 700 | 800 crediti | 2.000 |
| **Rivet III** | Dritto, bersaglio singolo | Epico | 6.000–7.500 | 35% | – | – | 1.100 | 500 | 5 Thulium | 500 |
| **Ember I** | Guidato, ad area | Comune | 1.120–1.400 | – | 170 | 700 | 1.000 | 500 | 500 crediti | 5.000 |
| **Ember II** | Guidato, ad area | Raro | 2.240–2.800 | – | 230 | 920 | 1.500 | 600 | 800 crediti | 2.000 |
| **Ember III** | Guidato, ad area | Epico | 3.360–4.200 | – | 300 | 1.150 | 2.030 | 700 | 5 Thulium | 500 |
| **Scatter I** | Dritto, ad area | Comune | 1.400–1.750 | – | 210 | – | 1.088 | 640 | 500 crediti | 5.000 |
| **Scatter II** | Dritto, ad area | Raro | 2.800–3.500 | – | 290 | – | 1.080 | 540 | 800 crediti | 2.000 |
| **Scatter III** | Dritto, ad area | Epico | 4.200–5.250 | – | 400 | – | 1.092 | 420 | 5 Thulium | 500 |

Più cara è la fascia, più forte colpisce un razzo, più lontano arriva, più penetrazione dello scudo ha e meno ne puoi trasportare; quelli cari sono anche quelli che rendono più danno in rapporto al costo. Un razzo dritto infligge il **25% in più** del razzo guidato della sua fascia e del suo tipo allo stesso prezzo, perché devi mirarlo. Un’esplosione infligge il 70% del razzo a bersaglio singolo della sua fascia, a ogni nave che copre. Il danno di un’esplosione è massimo al suo centro; al bordo scende al 25–35%. Un lancio infligge in media il 90% del suo numero massimo, e la tabella che conta i razzi qui sotto usa quel valore.

## Quanto costano {#what-they-cost}

Un razzo Comune costa 500 crediti, uno Raro 800 crediti e uno Epico 5 Thulium, in ogni tipo. Lanciati a ogni timer, fanno 6.000 crediti al minuto per un razzo Comune, 9.600 per uno Raro e 60 Thulium per uno Epico, contro i 1.800 crediti al minuto che bruciano a x1 i tre laser di una nave Ostirion. Una scorta piena è di 5.000 razzi Comuni (2.500.000 crediti), 2.000 Rari (1.600.000 crediti) o 500 Epici (2.500 Thulium): ne compri quanti vuoi fino a quel numero, e il *massimo trasportabile* di un razzo è l’unico tetto a quanti ne possiedi. I razzi non pesano nulla: non occupano spazio nel Deposito di trasporto. Un razzo ogni 5 secondi sono solo dodici al minuto, quindi un razzo è il picco di danno che si aggiunge ai tuoi laser: quelli economici per gli alieni deboli, quelli cari per gli scontri grossi.

Il Negozio elenca i razzi un tipo alla volta, ciascuno sotto il proprio nome, con il razzo Comune per primo e quello Epico per ultimo; l’Hangar, il Deposito di trasporto e il selettore Razzi usano lo stesso ordine.

## Contro gli alieni {#against-the-aliens}

I razzi necessari per distruggere un alieno, un tipo di razzo dopo l’altro (Alpha; gli alieni di Beta e Gamma sono rispettivamente 1,5 e 2 volte più forti). Per un’esplosione si conta il danno come lo subisce la nave accanto a cui esplode, un po’ prima del centro. Lo scudo di un alieno prende l’80% di un colpo, meno la penetrazione dello scudo del razzo. Qui ogni razzo fa la media. Con il valore più basso un abbattimento richiede circa il 10–15% di razzi in più rispetto alla tabella (un Lancet I ne richiede 50 per un Goombah, non 45); con il valore migliore, circa il 10% in meno (40). Un Rivet II distrugge un Phantasm con un colpo solo se il valore è almeno l’89%, sotto ne servono due.

| Razzi per distruggere | Seeker (1.600) | Phantasm (5.200) | Bulwark (26.000) | Goombah (80.000) | Crystalys (416.000) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Lancet I** | 1 | 3 | 15 | 45 | 232 |
| **Lancet II** | 1 | 2 | 8 | 20 | 116 |
| **Lancet III** | 1 | 1 | 5 | 11 | 78 |
| **Rivet I** | 1 | 3 | 12 | 36 | 185 |
| **Rivet II** | 1 | 1 | 6 | 16 | 93 |
| **Rivet III** | 1 | 1 | 4 | 9 | 62 |
| **Ember I** | 2 | 5 | 25 | 77 | 399 |
| **Ember II** | 1 | 3 | 13 | 37 | 193 |
| **Ember III** | 1 | 2 | 8 | 25 | 128 |
| **Scatter I** | 2 | 4 | 20 | 60 | 311 |
| **Scatter II** | 1 | 2 | 10 | 29 | 151 |
| **Scatter III** | 1 | 2 | 7 | 20 | 100 |

- I razzi **Comuni** a bersaglio singolo distruggono un Seeker con un colpo, con qualsiasi valore, e un Phantasm con tre (un Lancet I ne richiede un quarto con il suo valore più basso); sono i razzi di ogni giorno dei primi settori. Quelli **Rari** sono per il Bulwark e il Goombah: otto Lancet II abbattono un Bulwark in circa 35 secondi di timer. Quelli **Epici** distruggono un Phantasm con un colpo, con qualsiasi valore, e un Goombah con nove-undici colpi. Le esplosioni valgono il loro prezzo quando più alieni sono vicini: un Scatter III che esplode su un branco di cinque Phantasm infligge circa 18.000 danni al branco in un solo lancio.
- Un abbattimento solo con i razzi è una vera spesa, non un modo per arricchirsi: per l’alieno a cui è destinato, un razzo a bersaglio singolo costa da circa un settimo a tre quarti di ciò che paga l’abbattimento (crediti, e Thulium a 200 crediti l’uno), e i razzi deboli sugli alieni forti costano più di quanto paga l’abbattimento. Distruggere il **Crystalys** con un solo tipo richiede da 62 a 399 razzi e almeno cinque minuti di timer; una scorta piena di 500 razzi Epici basta per distruggerne da quattro a otto. L’alieno più forte richiede un piano: i tuoi laser con munizioni x2, un razzo di fascia media ogni 5 secondi fin dal primo secondo, e i razzi grossi qui sotto come picco di danno.
- Il compenso di un abbattimento è lo stesso comunque sia ottenuto (vedi [il Crystalys](/wiki/04-Aliens/Crystalys.md) per il più grosso), quindi un abbattimento con i razzi conviene quando ti fa risparmiare tempo e costa meno di quanto paga.
- **Anche gli alieni sparano razzi.** Il Pirate Boss, la Dormant Force e le Pulse degli [sciami](/wiki/05-Swarms/Swarms.md) lanciano razzi Rivet dritti al pilota che li ha attaccati, con lo stesso timer di 5 secondi. Una nave che resta in movimento li schiva. I boss degli sciami lasciano anche razzi nelle loro casse.

## I razzi solo da creare {#the-craft-only-rockets}

Due razzi non sono nel Negozio. Li produce l’**Assemblaggio** e seguono tutte le regole qui sotto (il timer condiviso, le zone sicure, la tua corporazione). Sono entrambi razzi dritti: volano verso il punto sotto il tuo cursore, come ogni razzo dritto (il gioco invia la direzione del cursore qualunque cosa tu abbia selezionato; solo un vecchio client 0.4.3, che non invia alcuna direzione, fa volare il razzo dal server verso il bersaglio selezionato, altrimenti verso il punto sotto il suo cursore, altrimenti nella direzione in cui punta la nave). Il loro danno è un valore casuale tra il **90% e il 100%** del numero massimo, una fascia più stretta di quella dei dodici, quindi ciò che distruggono con un colpo qui sotto vale anche con il valore più basso.

| Nome | Tipo | Rarità | Danno | Penetrazione scudo | Raggio dell’esplosione | Portata | Velocità | Massimo trasportabile | Si crea con |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **N.U.K.E.** | Dritto, ad area | Leggendario | 45.000–50.000 | – | 900 | 1.200 | 300 | 10 | 1 N.U.K.E. per creazione: 150.000 crediti, 3.000 Thulium, 6 Scatter III, 4 Power Core, 10 Reinforced Hull Plate, 40 Ship Fragment, 80 Cataclysite |
| **N.I.K.E.** | Dritto, bersaglio singolo | Mitico | 67.500–75.000 | 35% | – | 4.050 | 900 | 20 | 5 N.I.K.E. per creazione: 100.000 crediti, 1.500 Thulium, 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite |

- **N.U.K.E.**: la più grande esplosione del gioco. Un’esplosione di 900 unità, il doppio del raggio dei 400 del Scatter III e cinque volte la sua area: da 45.000 a 50.000 a ogni nave al suo interno al centro, che scendono alla metà, da 22.500 a 25.000, al bordo. È lenta (quattro secondi in aria). Un N.U.K.E. spazza via ogni Seeker e Phantasm in tutta la sua esplosione e un Bulwark entro 830 unità dallo scoppio (934 con il valore migliore), quasi tutta l’esplosione; toglie più della metà a un Goombah e un nono a un Crystalys. Contro i piloti è il colpo più grosso che esista: vedi le regole qui sotto. L’anello sulla mappa è la sua portata esatta.
- **N.I.K.E.**: un razzo a bersaglio singolo come un Rivet I, con un danno da 67.500 a 75.000 e una penetrazione dello scudo del 35%: **colpisce la prima nave che tocca e si esaurisce su di essa.** È anche il razzo che produce [Dark Matter](/wiki/03-Mechanics/Black-Hole.md): lanciato verso il buco nero al centro del Settore pericoloso 4, viene inghiottito quando attraversa l’orizzonte degli eventi, e il buco restituisce Dark Matter. Vola per 4.050 unità in 4,5 secondi: lancialo da qualsiasi punto tra il bordo delle radiazioni e 4.380 unità dal centro. Da più lontano non arriva e va sprecato. Cinque N.I.K.E. producono circa dieci Dark Matter.
- **L’insidia.** Un N.I.K.E. che incontra una nave lungo il percorso, un rivale in attesa sulla traiettoria o qualsiasi altra cosa che possa danneggiare, la colpisce con un danno da 67.500 a 75.000 e sparisce: il buco nero non riceve nulla, e nemmeno tu. Nient’altro si aggira dentro l’anello del buco per essere colpito per sbaglio (gli alieni e i piloti di corporazione ne stanno fuori): solo i piloti entrati per la Dark Matter o che ti aspettano al bordo. Attraversa la tua corporazione, le navi in una zona sicura e le navi che non puoi ancora danneggiare. Se lasci la mappa dopo averlo lanciato, vola avanti senza fare male a nessuno e produce comunque la tua Dark Matter.
- L’Assemblaggio non avvia una creazione che ti lascerebbe con più del *massimo trasportabile* di un razzo, contando ciò che hai messo in coda.

## Lancio {#firing}

1. Compra i razzi nel Negozio (la categoria **Razzi**), fino al *massimo trasportabile* di ciascuno: crediti per i Comuni e i Rari, Thulium per gli Epici.
2. Apri **Razzi** sopra la barra rapida e trascina quelli che vuoi sugli slot. Il selettore mostra una colonna per tipo e una riga per fascia, con ciò che trasporti di ciascuno. Sotto c’è una riga a parte, **Speciale · solo creazione**, per il N.U.K.E. e il N.I.K.E. (un piccolo martello segna quello di cui non porti nemmeno uno).
3. Premi il tasto dello slot. Cliccare sullo slot di un razzo **guidato** lo lancia contro il bersaglio selezionato; cliccare sullo slot di un razzo **dritto** lo arma, e il clic successivo nello spazio lo lancia lì. Il tasto **Lancia razzo** (`R` per impostazione predefinita, riassegnabile in Impostazioni › Comandi) lancia l’ultimo razzo che hai lanciato, o il primo sulla barra.
4. Un indicatore circolare di ricarica gira su **ogni** slot dei razzi per i 5 secondi che precedono il lancio successivo, con i secondi rimanenti al centro. Una pressione prima di allora ti dice soltanto che i razzi si stanno ricaricando (una pressione nell’ultimo decimo di secondo lancia comunque).

Passa il puntatore su uno slot di razzo per vederne i numeri (il suo danno più basso e più alto; il Negozio e l’Hangar dicono lo stesso) e, nel mondo, il suo anello di aggancio (verde quando il bersaglio selezionato è a portata) o la sua linea e il suo cerchio d’esplosione. Un razzo che ha agganciato **te** fa lampeggiare di rosso il bordo dello schermo.

Il **N.U.K.E.** disegna la sua esplosione sulla mappa prima che tu lo lanci (il cerchio di 900 unità nel punto mirato) e, quando esplode, un lampo bianco sulla vista, un anello che si allarga fino alla portata esatta in circa un secondo e resta per altri due, una nube che sale come un fungo e uno scossone della camera tanto più forte quanto più sei vicino. **Riduci scosse dello schermo** elimina lo scossone e **Riduci movimento** accorcia il lampo a un terzo di secondo con meno della metà della sua luce (entrambe sono in Impostazioni, sotto Grafica); una qualità delle particelle più bassa dirada la nube ed elimina le scintille, mai il lampo né l’anello. Il **N.I.K.E.** si mira come un Rivet I, con la linea dalla tua nave al cursore, e il gioco non lo rifiuta mai perché sei lontano dal buco nero o su una mappa che non ne ha: dove va lo decidi tu. La sua scheda dice **Buco nero: Produce Dark Matter** accanto al danno. Lascia una scia viola con scintille che vi si avvolgono; una nave che incontra subisce il colpo come da qualsiasi razzo, e quando invece attraversa l’orizzonte il buco si accende.

## Regole {#rules}

- Non ti serve **alcun laser montato** per lanciare un razzo, e i tuoi laser non cambiano ciò che infligge né quanto lontano arriva: un razzo guidato aggancia un bersaglio entro la propria portata di aggancio, uno dritto vola per la propria distanza. Senza laser montati il riquadro Portata dell’Hangar mostra un trattino, e sparano solo i tuoi razzi.
- Si consuma un razzo per lancio, che colpisca o no.
- I razzi seguono le regole dei laser: nulla dentro una **zona sicura** viene danneggiato, nessun pilota viene danneggiato prima che finisca il **Protocollo di pace** o dove un settore vieta il PvP, e **la tua corporazione e il tuo gruppo non vengono mai danneggiati** dai tuoi razzi, a colpo diretto o a esplosione.
- Lanciare un razzo termina subito la tua protezione della zona sicura. È uno sparo: termina anche il tuo **occultamento**, e il Cloaking CPU poi si ricarica per un minuto, come dopo qualsiasi fine di un occultamento. Occultato o no, un lancio ti impedisce di occultarti per i 10 secondi successivi (vedi [Extra](/wiki/06-Items/Extras.md)).
- Una nave **occultata** o nei **3 secondi del suo EMP** non può essere agganciata: un razzo guidato viene rifiutato, e uno già in volo verso di essa perde l’aggancio e prosegue dritto. Un razzo dritto a bersaglio singolo attraversa una nave così. Un’**esplosione ad area** non richiede aggancio, quindi danneggia le navi che copre, occultate o no, e ne interrompe l’occultamento (vedi [Extra](/wiki/06-Items/Extras.md)).
- **Nulla limita ciò che un razzo fa a un pilota.** La nave di un altro pilota subisce il danno pieno: prima lo scudo (il suo assorbimento meno la penetrazione dello scudo del razzo), poi lo scafo. Le navi piccole non reggono. Con gli scudi di serie (Light, 45% di assorbimento) un N.I.K.E. distrugge con un colpo, con qualsiasi valore, una nave Protos, Kitefin o Ostirion intatta (una Paragon perde dal 47 al 53% dello scafo, una Wraith circa un quinto), e un N.U.K.E. distrugge una Protos in qualsiasi punto della sua esplosione, una Kitefin entro circa 50 unità dallo scoppio (220 con il valore migliore) e nulla di più grosso con una sola esplosione. Due Lancet III o due Rivet III distruggono una Protos con qualsiasi valore; una Wraith ne richiede tra 48 e 75. Il Protocollo di pace, le zone sicure e la tua corporazione sono ciò che sta tra un pilota e un razzo.
- Solo il **colpo diretto** di un razzo rivendica un alieno (vedi [Combattimento](/wiki/03-Mechanics/Combat.md)); il bordo di un’esplosione può danneggiare un alieno già rivendicato senza rubarlo. Ogni alieno che un’esplosione danneggia, anche uno addormentato, si rivolta contro di te, come succede con un colpo di laser (compresi un Seeker o un Goombah, che reagiscono soltanto); uno che l’esplosione manca resta addormentato.
- Il timer è tuo: sopravvive a un salto, a una riconnessione, a un cambio di nave e a una nave distrutta.

I dodici razzi della prima tabella si comprano (crediti per i Comuni e i Rari, Thulium per gli Epici); il N.U.K.E. e il N.I.K.E. si creano.

Vedi anche: [Laser e munizioni](/wiki/06-Items/Lasers.md), [Combattimento](/wiki/03-Mechanics/Combat.md), [Il buco nero](/wiki/03-Mechanics/Black-Hole.md).
