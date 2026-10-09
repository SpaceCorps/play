<!-- wiki-i18n source: 1b81da9c3cf72282 -->
<!-- wiki-i18n title: Viaggiare sulla mappa -->
# Viaggiare sulla mappa spaziale {#spacemap-travel}

La mappa spaziale è la tua interfaccia di navigazione per attraversare l’universo di SpaceCorps. Ogni corporazione controlla un settore dello spazio, disposto secondo una topologia precisa che permette sia un’esplorazione sicura sia scontri PvP pericolosi.

![Galaxy Gates](../../img/wiki-img/shots/gates.jpg)
![Sector DS-1 as the game draws it](../../img/wiki-img/shots/sector-DS-1.jpg)
![Sector DS-2 as the game draws it](../../img/wiki-img/shots/sector-DS-2.jpg)
![Sector DS-3 as the game draws it](../../img/wiki-img/shots/sector-DS-3.jpg)
![Sector DS-4 as the game draws it](../../img/wiki-img/shots/sector-DS-4.jpg)
![Sector G-1 as the game draws it](../../img/wiki-img/shots/sector-G-1.jpg)
![Sector G-2 as the game draws it](../../img/wiki-img/shots/sector-G-2.jpg)
![Sector G-3 as the game draws it](../../img/wiki-img/shots/sector-G-3.jpg)
![Sector G-4 as the game draws it](../../img/wiki-img/shots/sector-G-4.jpg)
![Sector M-1 as the game draws it](../../img/wiki-img/shots/sector-M-1.jpg)
![Sector M-2 as the game draws it](../../img/wiki-img/shots/sector-M-2.jpg)
![Sector M-3 as the game draws it](../../img/wiki-img/shots/sector-M-3.jpg)
![Sector M-4 as the game draws it](../../img/wiki-img/shots/sector-M-4.jpg)
![Sector T-1 as the game draws it](../../img/wiki-img/shots/sector-T-1.jpg)
![Sector T-2 as the game draws it](../../img/wiki-img/shots/sector-T-2.jpg)
![Sector T-3 as the game draws it](../../img/wiki-img/shots/sector-T-3.jpg)
![Sector T-4 as the game draws it](../../img/wiki-img/shots/sector-T-4.jpg)
![The Star System map: the sectors, the PvP sectors, the gates and the company routes, with the portal ring that joins each company's x-4 sector to the next company's x-3 sector](../../img/wiki-img/shots/star-system.jpg)

## La struttura dell’universo {#the-universe-structure}

L’universo comprende tre grandi settori di corporazione (Mars, Terra, Galactic) e una zona PvP centrale.

- **x-1 (base)**: la mappa di partenza di ogni corporazione (M-1, T-1, G-1). La zona più sicura.
- **x-2 -> x-3**: zone di espansione con alieni via via più duri.
- **x-4 (confine)**: il passaggio verso il settore PvP e verso l’`x-3` di un’altra corporazione (l’Anello, più sotto).
- **DS-x (settori pericolosi)**: la zona PvP centrale che collega tutte le corporazioni: da DS-1 a DS-4. Dal giorno 11 della stagione contiene anche pulsar con escavatori giganti e il Dormant Swamp ([Settori pericolosi](/wiki/01-General/Danger-Sectors.md)).

Solo le basi hanno una stazione. È lì che si apre **Mission Control**, e la sua zona sicura si estende per 1.600 unità intorno a essa. I settori pericolosi non hanno stazioni, `DS-1` compreso: le uniche zone sicure lì sono gli anelli di 660 unità intorno alle porte di salto, e lì Mission Control non si può aprire; torna in volo alla tua base per le tue missioni.

Ogni [mondo](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) (Alpha, Beta, Gamma) ha la sua copia di tutta questa mappa, e da essa dipende dove i piloti possono combattere tra loro: in Alpha solo in `x-4` e `DS-x`, in Beta ovunque tranne `x-1`, in Gamma ovunque. La mappa galattica colora i settori secondo la regola del tuo mondo.

## Visualizzazione {#visualization}

La mappa galattica qui sotto mostra in tempo reale la disposizione dell’universo conosciuto. Nel gioco, la stessa mappa è la finestra **Sistema stellare**.

```spacemap

```

Con una [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) montata, la mappa serve anche a scegliere la destinazione: premi lo slot della CPU nella barra rapida (**JMP**) e la finestra Sistema stellare si apre in modalità di selezione. I settori in cui la CPU può portarti sono illuminati; il tuo settore e i settori pericolosi no. Punta un settore illuminato per leggere il prezzo, fai clic e conferma il salto quando la mappa lo chiede (500 Thulium).

## Come viaggiare {#how-to-travel}

Sulla mappa spaziale si viaggia attraverso le **porte di salto** (portali). La [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) è l’altra via: non ha bisogno di portali (vedi la fine di questa pagina).

1. **Individua un portale**: i portali di solito si trovano agli angoli o ai bordi di una mappa.
2. **Navigazione**: porta la nave vicino alla struttura del portale.
3. **Attivazione**: premi **J** entro 500 unità dal portale per avviare il salto.
4. **Aspetta**: il salto **dura 3 secondi**. Nel frattempo una barra sopra la barra rapida (“Salto in corso…”) si riempie e il portale brilla sempre di più mentre si carica; gli altri piloti vedono la stessa carica sul portale quando salti. La tua nave continua a volare, ma devi restare entro 500 unità dal portale fino allo scadere del tempo: se esci dal raggio il salto viene annullato (“Portale troppo lontano per saltare.” e la barra diventa rossa). Premere di nuovo **J** durante il salto non fa altro che mostrarti un messaggio.
5. **Destinazione**: arriverai al portale corrispondente nella mappa di destinazione.

### Saltare sotto attacco {#jumping-under-fire}

- **Fuori dai settori pericolosi**, essere attaccati, da alieni o da altri piloti, **non** interrompe il salto: si completa.
- **Nei settori pericolosi (da `DS-1` a `DS-4`)** non puoi saltare via mentre sei sotto attacco. Se un pilota o un alieno ha colpito la tua nave (i suoi scudi o il suo scafo) negli ultimi **10 secondi**, il salto non parte (“Sei sotto attacco: non puoi saltare fuori da un settore pericoloso.”), e un colpo subito durante il salto lo annulla (la barra diventa rossa e il gioco ti spiega perché). Il danno delle radiazioni del buco nero non è un attacco, e nemmeno lo è un colpo fermato da una zona sicura. Un colpo che hai subito sulla mappa da cui sei saltato non ti segue attraverso il portale: arrivi con la fedina pulita.
- Fai una cosa alla volta: non puoi raccogliere una [cassa di carico](/wiki/03-Mechanics/Cargo.md) mentre salti, e avviare un salto interrompe una raccolta che avevi iniziato.
- Chiudere il gioco o tornare alla base a metà salto lo annulla: non arrivi.
- **Il teletrasporto di una CPU si carica come un salto da portale.** Una Jump CPU si carica per 5 secondi e una Base CPU per 10, con una barra sopra la barra rapida. Un colpo che spari o che subisci, in qualsiasi settore, lo annulla (non si paga né si consuma nulla), e nessuna delle due CPU parte entro 10 secondi da un colpo sparato o subito. Premi di nuovo lo slot della CPU per annullarlo tu stesso.

### Collegamenti di salto {#jump-links}

- **L’anello della corporazione**: Mars, Terra e Galactic hanno la stessa disposizione. I collegamenti seguono lo schema `1 <-> 2 <-> 3`, `2 <-> 4` e `3 <-> 4`. Si forma un anello tra le mappe secondarie (`x-2` e `x-3`) e la mappa di confine (`x-4`), con `x-1` che fa da coda di ingresso sicura, collegata solo a `x-2`: la tua mappa di partenza ha un solo portale.
- **Portali di accesso ai settori pericolosi**: la mappa di confine (`x-4`) di ogni corporazione è collegata direttamente al suo settore pericoloso:
  - `M-4` porta a `DS-1`
  - `T-4` porta a `DS-2`
  - `G-4` porta a `DS-3`
- **L’Anello**: la mappa di confine (`x-4`) di ogni corporazione ha un’altra porta, verso l’`x-3` della **corporazione successiva**, e ogni `x-3` ha la porta di ritorno. I tre collegamenti formano un anello attorno ai settori pericolosi, così ogni corporazione ha una via d’uscita e una d’ingresso:
  - `M-4` porta al `T-3` di Terra
  - `T-4` porta al `G-3` di Galactic
  - `G-4` porta all’`M-3` di Mars

  L’Anello è aperto a ogni pilota, per qualunque corporazione voli: è un secondo modo di viaggiare tra le mappe delle corporazioni che non attraversa la zona PvP. Una porta dell’Anello sorge in un angolo tutto suo, lontano dalle altre porte della sua mappa, con la solita zona sicura di 660 unità attorno, e il salto funziona come a qualsiasi altra porta. Dove puoi essere attaccato dall’altra parte dipende dal tuo mondo, come ovunque: in Alpha `T-3` non è un settore PvP ma `T-4` sì, in Beta lo sono entrambi, in Gamma lo è ogni settore.
- **Vie d’invasione (viaggi tra corporazioni)**: ci sono due modi per entrare dalle porte nel territorio di un’altra corporazione. Quello breve è l’Anello: un pilota di Mars vola da `M-4` al `T-3` di Terra attraverso la porta dell’Anello (tre salti dalla base di Mars, `M-1` → `M-2` → `M-4` → `T-3`) e prosegue verso `T-4` o `T-2`; allo stesso modo il `G-4` di Galactic porta all’`M-3` di Mars e il `T-4` di Terra al `G-3` di Galactic. Quello lungo attraversa la zona PvP: da `M-4` nel settore pericoloso `DS-1`, attraverso la porta di salto verso `DS-2` e poi nello spazio di Terra attraverso `T-4`; per raggiungere Galactic si attraversa la porta di salto verso `DS-3` e si entra attraverso `G-4`.
- **Il triangolo dei settori pericolosi**: `DS-1`, `DS-2` e `DS-3` sono tutti collegati tra loro. Ognuno ha il portale di una corporazione (Mars in `DS-1`, Terra in `DS-2`, Galactic in `DS-3`); `DS-4` non ne ha.
- **Il nucleo centrale**: tutti e tre i settori pericolosi esterni (`DS-1`, `DS-2` e `DS-3`) sono collegati direttamente alla mappa centrale **`DS-4`**, la zona PvP più pericolosa e ricca di ricompense dell’universo. Un **buco nero** si trova esattamente al centro: i portali e le rotte tra di essi restano ben lontani, ma una nave che vi si addentra sente prima le sue radiazioni, poi la sua attrazione, e viene distrutta al suo orizzonte degli eventi. Vedi [Il buco nero](/wiki/03-Mechanics/Black-Hole.md). Dal giorno 11 della stagione l’angolo in alto a sinistra di `DS-4` contiene il [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md), i cui cannoni sparano a ogni nave che vedono.

### La Jump CPU {#the-jump-cpu}

La [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) porta la tua nave in qualsiasi settore di corporazione del tuo mondo senza passare da un portale, per 500 Thulium a salto, compresi i settori d’origine dei nemici. Non porta mai in un settore pericoloso, non parte in combattimento e la ricerchi prima nel Centro ricerche dello Skylab ([Ricerca](/wiki/03-Mechanics/Research.md)). Le [Base CPU](/wiki/06-Items/Extras.md#base-cpus) ti riportano a casa allo stesso modo. Una CPU warp, cioè la Jump CPU o una Base CPU, viene rifiutata finché trasporti un oggetto della missione (“Non puoi usare un CPU warp mentre trasporti un oggetto della missione.”): torna a casa attraverso i portali ([Oggetti della missione](/wiki/03-Mechanics/Quests.md#quest-items)).
