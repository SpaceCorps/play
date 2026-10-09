<!-- wiki-i18n source: 2bd1925e336e25b6 -->
<!-- wiki-i18n title: Corazza dello scafo -->
# Corazza dello scafo {#hull-plating}

<!-- wiki-search: hull plate; hull plate slot; hull plate slots; plate slot; plate; armour; armor; hpl; corazza; slot corazza; piastra dello scafo -->

Lo studio dello sciame Dormant ha mostrato progressi nella tecnologia delle corazze. Con questa tecnologia le navi possono migliorare il proprio scafo: la **corazza dello scafo** è una corazza che si monta in uno slot per piastre dello scafo di una nave costruita e le aggiunge punti scafo. Non è l’Hull Plating **Booster** della pagina [Booster](/wiki/06-Items/Boosters.md), che è un bonus a tempo.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Albero degli oggetti {#item-tree}

Ciò che crea l’Assemblaggio richiede prima la sua tecnologia; passa il puntatore su un oggetto per vedere quanto tempo serve a ricercarla. L’albero delle tecnologie, il carburante e il boost: [Ricerca](/wiki/03-Mechanics/Research.md).

```tree
Hull Plating I | hull-plating, uncommon | buy 5000 Thulium | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating II | hull-plating, rare | craft 2500 Thulium, 300 s | research 86400 s, 86400 science, 25 Dark Matter | 1 Hull Plating I, 150 Ship Fragment, 20 Reinforced Hull Plate, 6 Power Core, 5 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating III | hull-plating, epic | craft 4000 Thulium, 600 s | research 172800 s, 172800 science, 40 Dark Matter | 1 Hull Plating II, 300 Ship Fragment, 40 Reinforced Hull Plate, 12 Power Core, 1 Ancient Control Unit, 8 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings

Hull Plating I => Hull Plating II => Hull Plating III
```
<!-- item-tree:end -->

## Le tre corazze {#the-three-platings}

| Oggetto | Scafo aggiunto | Da dove viene |
| :--- | ---: | :--- |
| **Hull Plating I** | 5.000 | Negozio, 5.000 Thulium |
| **Hull Plating II** | 10.000 | Assemblaggio, da una Hull Plating I |
| **Hull Plating III** | 15.000 | Assemblaggio, da una Hull Plating II |

La Hull Plating I si compra. **La II e la III sono potenziamenti**: l’Assemblaggio consuma una corazza del grado inferiore (libera nel tuo inventario) e chiede Thulium, materiali e **Dark Matter Plate**, 5 per la II e 8 per la III, dove l’ultimo tier di qualsiasi altro pezzo di equipaggiamento ne chiede 3. Ciascuna ha prima bisogno della sua tecnologia, nell’albero Hull Plating della pagina [Ricerca](/wiki/03-Mechanics/Research.md#tree-hull-plating): 1 giorno e 25 Dark Matter per la II, 2 giorni e 40 per la III, oltre alla tecnologia della Dark Matter Plate stessa. L’albero qui sopra riporta i prezzi, i materiali e i tempi.

La [Forgia](/wiki/06-Items/Forge.md) accetta ogni corazza, e un potenziamento mantiene il grado di forgia della corazza consumata e ne tira di nuovo il bonus. Una corazza ha una sola statistica, lo scafo, quindi porta un solo bonus, da +2% a +15% in base al grado: una Hull Plating III di grado Eterno aggiunge fino a 17.250. All’[Asta](/wiki/03-Mechanics/Auction.md) si mettono in vendita la Hull Plating II e la III, mai la Hull Plating I, che vende il Negozio.

## Slot corazza {#hull-plate-slots}

La corazza dello scafo entra solo negli **slot corazza**, un tipo di slot a sé che le quattro navi che costruisci nell’Assemblaggio hanno oltre ai loro slot per laser, generatori, extra, abilità e droni:

| Nave | Slot corazza | Un set completo di Hull Plating III aggiunge |
| :--- | ---: | ---: |
| **Paragon** | 5 | 75.000 |
| **Storm** | 7 | 105.000 |
| **Ironclad** | 15 | 225.000 |
| **Wraith** | 9 | 135.000 |

- **Tutti bloccati all’inizio.** Uno slot si apre quando lo ricerchi nello Skylab: una tecnologia per ogni slot, 1 ora e 10 Dark Matter, in ordine a partire dal primo. La vista [Ricerca](/wiki/03-Mechanics/Research.md#ship-technologies) mostra gli slot di una nave come un’unica scheda con un punto per ognuno.
- **Un tipo di nave, non una sola nave.** Gli slot che hai aperto per la Paragon sono aperti anche su ogni design della Paragon ([Design delle navi](/wiki/03-Mechanics/Ship-Designs.md)). Una tecnologia è tua per sempre: il reset la mantiene.
- **Le due configurazioni li condividono.** Le corazze appartengono alla nave: cambiare configurazione le lascia montate, e l’Hangar mostra le stesse in entrambe.
- **Qualsiasi mescolanza.** Uno slot accetta qualsiasi corazza dello scafo, e due uguali vanno benissimo.
- **La tua quota di scafo resta.** Montare o smontare una corazza mantiene la quota di scafo che hai, quindi una corazza non ti cura mai e non ti ferisce mai.
- **Come ogni equipaggiamento**, le corazze si montano e si smontano nell’Hangar, o nella sua finestra da una zona sicura, mai sul campo. Uno slot che non hai ricercato rifiuta la corazza.

Nell’Hangar la scheda **Corazza dello scafo** mostra gli slot. In quello aperto si mette una corazza trascinandola, come in ogni slot; quello bloccato mostra un lucchetto, e un clic apre la ricerca dello Skylab. Un riquadro accanto alle altre statistiche somma ciò che danno le corazze montate.

## Come si somma lo scafo {#how-the-hull-adds-up}

Una corazza aggiunge il suo scafo a quello della nave, e l’Hangar e la finestra della nave mostrano il numero più grande. Lo scafo della nave più le sue corazze passa poi per i moltiplicatori di sempre: un [Hull Plating Booster](/wiki/06-Items/Boosters.md) e la [formazione di droni](/wiki/03-Mechanics/Formations.md) che indossi. Un design che cambia lo scafo (il BUCKY ne ha il 25% in più) cambia lo scafo proprio della nave, e le corazze si aggiungono sopra.

## Hull Plating o Hull Plating Booster? {#hull-plating-or-booster}

Due cose condividono il nome. La **corazza dello scafo** (questa pagina) è un’armatura: una piastra che sta in uno slot corazza di una nave costruita e aggiunge il suo scafo finché è montata. L’**Hull Plating Booster** è un bonus a tempo della pagina [Booster](/wiki/06-Items/Boosters.md), +10% di punti scafo massimi per 10 ore sulla nave che pilotti, e non c’è nulla da montare. Si sommano: prima vengono le corazze e il 10% del Booster si calcola sul totale.
