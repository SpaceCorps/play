<!-- wiki-i18n source: 0dfda8fd6d9be79d -->
<!-- wiki-i18n title: Droni -->
# Droni {#drones}

I droni sono unità di supporto acquistabili o creabili. Puoi avere attivi fino a **8 droni** contemporaneamente, Slave Drone e Master Drone insieme.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Albero degli oggetti {#item-tree}

Ciò che crea l’Assemblaggio richiede prima la sua tecnologia; passa il puntatore su un oggetto per vedere quanto tempo serve a ricercarla. L’albero delle tecnologie, il carburante e il boost: [Ricerca](/wiki/03-Mechanics/Research.md).

```tree
Slave Drone | drone, common | buy 100000 Credits | /wiki/06-Items/Drones.md#available-drones
Master Drone | drone, rare | craft 40000 Thulium, 60 s | research 36000 s, 36000 science | 1 Slave Drone, 100 Ship Fragment | /wiki/06-Items/Drones.md#available-drones

Slave Drone => Master Drone
```
<!-- item-tree:end -->

## Droni disponibili {#available-drones}

| Nome             | Rarità | Slot  | Descrizione                                                                                  | Costo                            |
| :--------------- | :----- | :---- | :------------------------------------------------------------------------------------------- | :------------------------------- |
| **Slave Drone**  | Comune | 1     | Un drone di base con un solo slot per l’equipaggiamento. Cresce in 8 livelli man mano che distruggi alieni. | Da 100.000 crediti (vedi sotto) |
| **Master Drone** | Raro   | 2     | Uno Slave Drone potenziato nell’Assemblaggio. Vola in oro, mantiene il suo numero e ciò che trasporta, ottiene un secondo slot per l’equipaggiamento e riparte dal livello 1. | Potenzia uno Slave Drone: 40.000 Thulium e 100 Ship Fragment |

Uno Slave Drone parte come una piccola sfera e al livello 8 diventa una cannoniera corazzata. Ogni drone che possiedi guadagna la stessa esperienza ogni volta che distruggi un alieno, e un livello più alto aggiunge un po’ di danno al laser del suo slot (fino a +7% al livello 8). La pagina sulle meccaniche dei droni (nella categoria Meccaniche) riporta i livelli e ciò che ognuno richiede. Creare un Master Drone non consuma un drone: potenzia sul posto lo Slave Drone che scegli e, al termine del potenziamento, **il suo livello e la sua esperienza tornano a 0** (l’Assemblaggio te lo dice e chiede conferma). In cambio il drone ha **due slot per l’equipaggiamento** invece di uno: ciò che portava resta nel primo slot e il secondo è vuoto. I tuoi droni, con livelli ed esperienza, restano dopo il reset della stagione.

## Prezzi dello Slave Drone {#slave-drone-prices}

Ogni Slave Drone che compri costa più del precedente. Il prezzo dipende da quanti droni possiedi al momento dell’acquisto (un Master Drone conta come uno) e il Negozio mostra sempre il prezzo del successivo. I primi tre costano solo crediti; dal quarto in poi si aggiunge il Thulium.

| Drone | Crediti    | Thulium |
| :---- | :--------- | :------ |
| 1º    | 100.000    | –       |
| 2º    | 200.000    | –       |
| 3º    | 400.000    | –       |
| 4º    | 800.000    | 10.000  |
| 5º    | 1.600.000  | 20.000  |
| 6º    | 3.200.000  | 30.000  |
| 7º    | 6.400.000  | 40.000  |
| 8º    | 12.800.000 | 50.000  |

Tutti e otto insieme costano 25.500.000 crediti e 150.000 Thulium. I tuoi droni restano dopo il reset della stagione, quindi il prezzo prosegue dal numero che possiedi: con tre droni il prossimo è sempre il 4º e con otto non ne resta nessuno da comprare.

## Utilizzo {#usage}

1. **Compra** gli Slave Drone nel Negozio. **Potenzia** uno di essi in Master Drone nell’Assemblaggio quando vuoi quello dorato (livello ed XP ripartono da capo).
2. **Equipaggiali** nell’Hangar, nella scheda “Droni”.
3. **Caricali** con laser o scudi per aumentare la tua potenza: uno Slave Drone ha uno slot, un Master Drone due. Un laser spara insieme alla tua nave; uno scudo conta come uno scudo in uno slot principale, con tutte le sue statistiche.
4. **Falli salire di livello** distruggendo alieni: l’Hangar mostra il livello di ogni drone e quanta esperienza richiede il successivo.
