<!-- wiki-i18n source: 3a89595b53c5603f -->
<!-- wiki-i18n title: Viaggiare sulla mappa -->
# Viaggiare sulla mappa spaziale {#spacemap-travel}

La mappa spaziale è la tua interfaccia di navigazione per attraversare l’universo di SpaceCorps. Ogni corporazione controlla un settore dello spazio, disposto secondo una topologia precisa che permette sia un’esplorazione sicura sia scontri PvP pericolosi.

## La struttura dell’universo {#the-universe-structure}

L’universo comprende tre grandi settori di corporazione (Mars, Terra, Galactic) e una zona PvP centrale.

- **x-1 (base)**: la mappa di partenza di ogni corporazione (M-1, T-1, G-1). La zona più sicura.
- **x-2 -> x-3**: zone di espansione con alieni via via più duri.
- **x-4 (confine)**: il passaggio verso il settore PvP.
- **DS-x (settori pericolosi)**: la zona PvP centrale che collega tutte le corporazioni: da DS-1 a DS-4.

Solo le basi hanno una stazione. È lì che si apre **Mission Control**, e la sua zona sicura si estende per 1.600 unità intorno a essa. I settori pericolosi non hanno stazioni, `DS-1` compreso: le uniche zone sicure lì sono gli anelli di 660 unità intorno alle porte di salto, e lì Mission Control non si può aprire; torna in volo alla tua base per le tue missioni.

Ogni [mondo](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) (Alpha, Beta, Gamma) ha la sua copia di tutta questa mappa, e da essa dipende dove i piloti possono combattere tra loro: in Alpha solo in `x-4` e `DS-x`, in Beta ovunque tranne `x-1`, in Gamma ovunque. La mappa galattica colora i settori secondo la regola del tuo mondo.

## Visualizzazione {#visualization}

La mappa galattica qui sotto mostra in tempo reale la disposizione dell’universo conosciuto.

```spacemap

```

## Come viaggiare {#how-to-travel}

Sulla mappa spaziale si viaggia attraverso le **porte di salto** (portali).

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

### Collegamenti di salto {#jump-links}

- **L’anello della corporazione**: Mars, Terra e Galactic hanno la stessa disposizione. I collegamenti seguono lo schema `1 <-> 2 <-> 3`, `2 <-> 4` e `3 <-> 4`. Si forma un anello tra le mappe secondarie (`x-2` e `x-3`) e la mappa di confine (`x-4`), con `x-1` che fa da coda di ingresso sicura, collegata solo a `x-2`: la tua mappa di partenza ha un solo portale.
- **Portali di accesso ai settori pericolosi**: la mappa di confine (`x-4`) di ogni corporazione è collegata direttamente al suo settore pericoloso:
  - `M-4` porta a `DS-1`
  - `T-4` porta a `DS-2`
  - `G-4` porta a `DS-3`
- **Vie d’invasione (viaggi tra corporazioni)**: per entrare nel territorio di una corporazione nemica devi attraversare la zona PvP. Per esempio, un pilota di Mars che vuole invadere Terra deve volare da `M-4` nel settore pericoloso `DS-1`, attraversare la porta di salto verso `DS-2` e poi entrare nello spazio di Terra attraverso `T-4`; per raggiungere Galactic, attraversa la porta di salto verso `DS-3` ed entra attraverso `G-4`.
- **Il triangolo dei settori pericolosi**: `DS-1`, `DS-2` e `DS-3` sono tutti collegati tra loro. Ognuno ha il portale di una corporazione (Mars in `DS-1`, Terra in `DS-2`, Galactic in `DS-3`); `DS-4` non ne ha.
- **Il nucleo centrale**: tutti e tre i settori pericolosi esterni (`DS-1`, `DS-2` e `DS-3`) sono collegati direttamente alla mappa centrale **`DS-4`**, la zona PvP più pericolosa e ricca di ricompense dell’universo. Un **buco nero** si trova esattamente al centro: i portali e le rotte tra di essi restano ben lontani, ma una nave che vi si addentra sente prima le sue radiazioni, poi la sua attrazione, e viene distrutta al suo orizzonte degli eventi. Vedi [Il buco nero](/wiki/03-Mechanics/Black-Hole.md).
