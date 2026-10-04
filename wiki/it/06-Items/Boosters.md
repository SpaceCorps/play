<!-- wiki-i18n source: 539575474f5854de -->
<!-- wiki-i18n title: Booster -->
# Booster {#boosters}

I booster forniscono modifiche temporanee alle statistiche per potenziare il combattimento, la difesa, la crescita di livello e la raccolta di risorse della tua nave.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Albero degli oggetti {#item-tree}

Ciò che crea l’Assemblaggio richiede prima la sua tecnologia; passa il puntatore su un oggetto per vedere quanto tempo serve a ricercarla. L’albero delle tecnologie, il carburante e il boost: [Ricerca](/wiki/03-Mechanics/Research.md).

```tree
Experience Kit | booster, common | buy 8000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Honor Beacon | booster, common | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Damage Amp II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Regen | booster, rare | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Resource Magnet | booster, rare | buy 18000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Damage Amp | booster, rare | buy 20000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Loot Luck | booster, legendary | buy 30000 Thulium | /wiki/06-Items/Boosters.md#active-boosters

Shield Wall -> Shield Wall II
Hull Plating -> Hull Plating II
Damage Amp -> Damage Amp II
```
<!-- item-tree:end -->

## Regole di cumulo {#stacking-rules}

I booster usano un sistema di scala additivo:
1. **Le percentuali di bonus si sommano**: se compri due booster diversi che danno entrambi +10% di danno laser, ottieni un bonus totale di **+20% di danno laser**.
2. **Le durate si cumulano in modo moltiplicativo**: comprare più volte lo _stesso_ booster ne prolunga la durata attiva. I timer di booster _diversi_ corrono in parallelo.
3. **Visualizzazione dei timer**: i booster attivi compaiono nell’HUD, nella finestra Booster, con il totale dei bonus attivi raggruppati e la prossima scadenza.

---

## Booster attivi {#active-boosters}

Ogni booster dura **10 ore** di base e si attiva subito all’acquisto, alla ricezione o al ritiro. I tre booster **II** non si vendono: ne ricerchi la tecnologia nello Skylab ([Ricerca](/wiki/03-Mechanics/Research.md)), poi li crei nell’Assemblaggio, e ritirarne uno fa partire subito le sue 10 ore, come comprarlo.

| Nome | Rarità | Effetto base (10 ore) | Prezzo (Thulium) |
| :--- | :--- | :--- | :--- |
| **Damage Amp** | Raro | +10% di danno laser | 20.000 |
| **Damage Amp II** | Raro | +10% di danno laser | Assemblaggio: 20.000 |
| **Shield Wall** | Raro | +25% di capacità scudo (punti scudo massimi) | 15.000 |
| **Shield Wall II** | Raro | +25% di capacità scudo (punti scudo massimi) | Assemblaggio: 15.000 |
| **Hull Plating** | Raro | +10% di punti scafo massimi | 15.000 |
| **Hull Plating II** | Raro | +10% di punti scafo massimi | Assemblaggio: 15.000 |
| **Shield Regen** | Raro | +25% di velocità di ricarica dello scudo (punti scudo ripristinati al secondo) | 10.000 |
| **Experience Kit** | Comune | +20% di esperienza guadagnata | 8000 |
| **Honor Beacon** | Comune | +20% di punti onore guadagnati | 10.000 |
| **Resource Magnet** | Raro | +25% di resa delle casse di carico | 18.000 |
| **Loot Luck** | Leggendario | +5% di probabilità di drop rari dagli NPC | 30.000 |

---

## Bonus agli scudi: tre tipi {#shield-boosts-three-kinds}

Gli scudi hanno tre statistiche distinte e ogni bonus agli scudi ne aumenta esattamente una. La finestra Booster le tiene separate, con un’icona e un totale per ciascuna:

| Tipo | Che cos’è | Bonus che lo aumentano |
| :--- | :--- | :--- |
| **Capacità dello scudo** | I tuoi punti scudo massimi | Shield Wall, Shield Wall II, lo **Shield Capacity Boost** permanente (Emporio) |
| **Assorbimento dello scudo** | La quota di ogni colpo che i tuoi scudi prendono (il resto colpisce lo scafo); può superare il 100% | Lo **Shield Absorbance Boost** permanente (Emporio): +0,1 punti a livello per 25 PR, al massimo +10 punti. Nessun booster lo aumenta |
| **Ricarica dello scudo** | Punti scudo ripristinati al secondo | Shield Regen. Nessun potenziamento permanente lo aumenta |

I bonus di un tipo si sommano tra loro e non contano mai per un altro tipo. I potenziamenti permanenti sono descritti in [Progressione tra le stagioni](/wiki/03-Mechanics/Wipe-Timeline.md); le statistiche vere e proprie in [Meccaniche degli scudi](/wiki/03-Mechanics/Shields.md).
