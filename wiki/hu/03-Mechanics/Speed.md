<!-- wiki-i18n source: 431a488ba7a0842e -->
<!-- wiki-i18n title: Sebesség -->
# Sebességszámítás {#speed-calculation}

A sebesség határozza meg, milyen gyorsan mozog a hajód az űrtérképen: ezen múlik, hogy utol tudod-e érni a célpontjaidat, ki tudsz-e törni egy harcból, vagy át tudsz-e kelni a zónákon.

## A sebességképlet {#the-speed-formula}

A hajód végső sebességét a szerver a következő képlettel számolja ki:

\[\text{Végső sebesség} = (\text{A hajó alapsebessége} + \text{A hajtóművek összsebessége}) \times (1,0 + \text{Összes sebességbónusz-százalék})\]

### 1. Tényleges hajtóműsebesség {#1-effective-engine-speed}

Minden felszerelt hajtómű sebességet termel. Ha fúvókák vannak beszerelve a hajtóműbe, a sebessége módosul:

\[\text{Hajtómű sebessége} = (\text{Hajtómű alapsebessége} \times \text{Fúvókaszorzó}) + \text{Fúvókák fix bónusza}\]

- **Fúvókaszorzó**: az adott hajtóműbe szerelt összes fúvóka sebességszorzójának szorzata (pl. a Thruster III értéke `1.1`, vagyis `+10%`).
- **Fúvókák fix bónusza**: a fúvókák összes fix sebességnövelésének összege (pl. a Thruster III `+15` sebességet ad).

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
