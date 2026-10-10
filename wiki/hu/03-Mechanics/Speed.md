<!-- wiki-i18n source: 74226336693d1ae9 -->
<!-- wiki-i18n title: Sebesség -->
# Sebességszámítás {#speed-calculation}

A sebesség határozza meg, milyen gyorsan mozog a hajód az űrtérképen: ezen múlik, hogy utol tudod-e érni a célpontjaidat, ki tudsz-e törni egy harcból, vagy át tudsz-e kelni a zónákon.

## A sebességképlet {#the-speed-formula}

A hajód végső sebességét a szerver a következő képlettel számolja ki:

\[\text{Végső sebesség} = (\text{A hajó alapsebessége} + \text{A hajtóművek összsebessége}) \times (1,0 + \text{Összes sebességbónusz-százalék})\]

A [hajódizájn](/wiki/03-Mechanics/Ship-Designs.md) az első tagot változtatja meg (a THUNDER alapsebessége 40-nel nagyobb, a DUMA-é 20-szal kisebb), a NOTSUM és a RECON pedig a végső sebességet még egy tényezővel szorozza, +2%-kal és +5%-kal.

### 1. Tényleges hajtóműsebesség {#1-effective-engine-speed}

Minden felszerelt hajtómű sebességet termel, és minden olyan adaptív mag is, amelyben fúvókák vannak. Ha fúvókák vannak beszerelve a hajtóműbe, a sebessége módosul:

\[\text{Hajtómű sebessége} = (\text{Hajtómű alapsebessége} + \text{Fúvókák fix bónusza}) \times \text{Fúvókaszorzó}\]

- **Fúvókák fix bónusza**: a fúvókák összes fix sebességnövelésének összege (pl. az Impulse Thruster III `+12.75` sebességet ad).
- **Fúvókaszorzó**: az adott hajtóműbe szerelt összes fúvóka sebességszorzójának szorzata (pl. a Momentum Thruster III értéke `1.0765`, vagyis `+7.65%`, az Impulse Thruster III-é `1.0255`, vagyis `+2.55%`). Mindent megszoroz, amit a hajtómű termel: a saját alapsebességét és a fúvókák fix bónuszait is. Az adaptív magnak nincs saját alapsebessége, de a fúvókái fix bónuszait a szorzó így is megszorozza.

Egy Engine III (alapsebesség 6) három Momentum Thruster IV-gyel (`+11.135`, `1.0935`) (6 + 3 x 11,135) x 1,0935 x 1,0935 x 1,0935 = 51,5 sebességet termel, három Impulse Thruster IV-gyel (`+14.025`, `1.02975`) pedig (6 + 3 x 14,025) x 1,02975 x 1,02975 x 1,02975 = 52,5-öt. A Kovácsműhely bónusza egy fúvóka szorzóján az 1 feletti részt növeli: +15% a `1.0935` szorzón `1.1075` értéket ad.

### 2. Csökkenő hozadék (határhatékonyság) {#2-diminishing-returns-marginal-efficiency-}

Hogy senki ne halmozhasson végtelen sok hajtóművet végtelen sebességért, a számítás **csökkenő hozadék (határhatékonyság)** görbét alkalmaz. Az összes hajtómű a sebességhozzájárulása szerint van sorba rendezve, és ebben a sorrendben kerül feldolgozásra. Az adaptív magok (hibridek) és a pajzsmagok ugyanígy kapnak sorrendet, mindegyik fajta a saját csoportjában, így az a hajó, amelyen hajtóművek és adaptív magok is vannak, mindegyik fajtából külön számolja az első négyet:

| Hajtómű sorrendje | Hatékonysági szorzó |
| :---: | :--- |
| **1–4.** | **100%** (1,0) |
| **5.** | **85%** (0,85) |
| **6.** | **70%** (0,70) |
| **7.** | **55%** (0,55) |
| **8. és a további** | **25%** (0,25) |

Ezenfelül a hajtómű sebességét megszorozza a foglalatának hatékonysága (magfoglalat: 100%, támogató foglalat: 75%, segédfoglalat: 50%).

### 3. Sebességbónusz-százalék és pajzsbüntetések {#3-speed-bonus-percent-shield-penalties}

Az összes sebességbónusz-százalék a felszerelt hajtóművek (és hibridek) sebességbónuszainak összege, mínusz a felszerelt pajzsok büntetései:

- **Hajtómű sebességbónusza**: a hajtóművek pozitív sebességszázalékot adnak (pl. az Engine III bónusza `+5%`).
- **Pajzsok sebességbüntetése**: a nehéz pajzsok lehúzzák a hajódat, ezért negatív sebességszázalékot adnak (pl. a Heavy Shield Core `-5%` sebességet jelent).
- **Skálázás a foglalat szerint**: ezeket a százalékos bónuszokat és büntetéseket is a foglalat hatékonysága skálázza, amelybe a tárgy be van szerelve. A drónjaid egyikén lévő pajzs úgy lassít, mint a magfoglalatban lévő.
- **Soha nem megy nulla alá**: bármennyi pajzsot viszel, a sebességed nem csökken 0 alá.
- **Drónformációk**: a viselt [drónformáció](/wiki/03-Mechanics/Formations.md) még egyszer módosítja a végső sebességet, önálló tényezőként: Gyre +10%, Cordon −3%, Auger −9%, Culler −10%, Redoubt −11%, Rampart −17%. Az Afterburner ezután az eredményt szorozza.
