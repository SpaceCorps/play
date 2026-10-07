<!-- wiki-i18n source: 7af844c9c2785078 -->
<!-- wiki-i18n title: Pajzsok -->
# Pajzsmechanika {#shield-mechanics}

A pajzsok elnyelik a beérkező sebzés nagy részét, és megvédik a hajód hajótestét a közvetlen sebzéstől.

## Pajzsszámítások {#shield-calculations}

A hajód végső pajzsparaméterei a következőképpen alakulnak:

\[\text{Végső pajzskapacitás} = \text{Összes alapkapacitás} \times (1,0 + \text{Összes pajzsbónusz-százalék})\]
\[\text{Végső töltődési sebesség} = \text{Összes alaptöltődés} \times (1,0 + \text{Összes pajzsbónusz-százalék})\]

### 1. Foglalathatékonyság és csökkenő hozadék {#1-slot-efficiency-diminishing-returns}

A hajtóművekhez hasonlóan a felszerelt pajzsok (és hibridgenerátorok) a legjobbtól kezdve vannak sorba rendezve, és rájuk a foglalathatékonyság (magfoglalat: 100%, támogató foglalat: 75%, segédfoglalat: 50%, a drón foglalata: 100%, mint egy magfoglalat), valamint a sorrendjükön alapuló csökkenő hozadék görbéje vonatkozik. Egy pajzsot az alapján rangsorolnak, hogy mi számít belőle: a kapacitása szorozva a foglalata részesedésével. A töltődésnek saját sorrendje van (az értéke szorozva a foglalat részesedésével), és a **négy legjobb** pajzsbónusz számít. A [drónjaid](/wiki/03-Mechanics/Drones.md) egyikén lévő pajzs a hajó saját pajzsaival együtt kerül sorba:

- **1–4. pajzs**: **100%** (1,0) határhatékonyság.
- **5. pajzs**: **85%** (0,85) határhatékonyság.
- **6. pajzs**: **70%** (0,70) határhatékonyság.
- **7. pajzs**: **55%** (0,55) határhatékonyság.
- **8. és a további**: **50%** (0,50) határhatékonyság. (A 0.4.7-es verzióig ez 25% volt, mint a hajtóműveknél; a hajtóművek továbbra is 25%-ot kapnak, lásd: [Sebesség](/wiki/03-Mechanics/Speed.md).)

**A több felszerelés sosem csökkenti a pajzsodat.** Egy pajzs vagy pajzscella hozzáadása sosem csökkenti a pajzskapacitásodat vagy a töltődésedet: minden szám a legjobbtól kezdve van sorba rendezve aszerint, hogy mi számít, így az új darab azt a helyet foglalja el, amelyet megérdemel. Az elnyelés a pajzsaid átlaga, ezért azt egy új, az átlagodnál gyengébb pajzs csökkenti; egy cella soha.

**A hangár megmutatja.** Az a pajzs, hajtómű vagy adaptív mag, amely nem a teljes erejével számít, kis százalékot visel a foglalatán (például `64%`: az 5. pajzs 85%-kal, támogató foglalatban, 75%-kal), és ráhúzva a kurzort megjelenik a részletezés. Ha a harci statisztikák Pajzsok és Sebesség csempéire viszed a kurzort, rang szerint látod a tárgyaidat, és azt, hogy egy újabb mennyit számítana. A repülés közbeni Hajó ablak ugyanezeket a listákat mutatja, ha a pajzssávjára és a sebességére viszed a kurzort.

### 2. Pajzselnyelés (a sebzés megosztása) {#2-shield-absorbance-damage-split-}

Az elnyelés az a rész, amelyet a pajzsaid minden találatból felfognak; a többi közvetlenül az életerőre (HP) megy.
- **Pajzsonként**: egy pajzs elnyelése plusz a beleszerelt pajzscellák elnyelése. Egy pajzs önmagában **45–50%** (Light 45%, Basic 48%, Heavy 50%); a cellák darabonként 2–10 pontot adnak (Capacity Shield Cell I–IV +2%, +3%, +4%, +5%; Absorption Shield Cell I–IV +4%, +6%, +8%, +10%).
- **Átlagos elnyelés**: a hajód elnyelése a mag-, támogató és segédfoglalatokban és a drónjaidon lévő pajzsok egyszerű átlaga. Az adaptív magoknak nincs saját elnyelésük, és nem számítanak bele az átlagba (az adaptív magba tett cellák csak kapacitást és töltődést adnak). Felszerelt pajzs nélkül az elnyelésed 0%: a hajótest minden találatot elvisel, és az adaptív magban lévő cellák pajzspontjai kihasználatlanok maradnak, ezért szerelj mellé egy pajzsot.
- **Alapból legfeljebb 80% érhető el**: a legjobb pajzs a legjobb cellákkal, vagyis mindegyik foglalatban egy Heavy Shield Core három Absorption Shield Cell IV-gyel. A gyengébb pajzsok bekeverése lehúzza az átlagot. Ebbe a számba sem a Szezonbolt buffjai, sem a Kovácsműhely buffjai nem számítanak bele.
- **Példa**: egy Basic Shield Core (48%) két Absorption Shield Cell I-gyel 56%; ha mellé veszel egy Light Shield Core-t (45%), az átlag 50,5%.
- **Az érték nincs 100%-ra korlátozva.** Ez az a rész, amelyet a pajzsok egy találatból felfognának, mielőtt levonják a támadó *pajzsáthatolását*, így egy hajó akár egy teljes találatnál is többet bírhat: a 112% még egy legfeljebb 12% áthatolású támadó teljes találatát is felfogja.

#### Pajzsáthatolás {#shield-penetration}

Egyes támadásoknak van **pajzsáthatolásuk**: annyi pontot vonnak le az elnyelésedből az adott találatnál. Az a rész, amelyet a pajzsaid felfognak:

\[\text{Pajzsarány} = \text{korlátozás}(\text{Elnyelés} - \text{Áthatolás};\ 0;\ 100\%)\]

- A pajzsok legfeljebb `round(damage x share)` sebzést vesznek fel a találatból; a többit a hajótest kapja. Ha egy pajzs túl alacsony az arányához, a különbséget az életerőre engedi át, és ha a pajzsok 0-n állnak, az egész sebzés közvetlenül az életerőt éri.
- **Honnan jön az áthatolás**: az egycélpontos rakéták *pajzsáthatolásából* (Lancet I 10%, Lancet II 25%, Lancet III 35%, Rivet I 5%, Rivet II 25%, Rivet III 35%, N.I.K.E. 35%; a területi robbanásoknak nincs, lásd [Rakéták](/wiki/06-Items/Rockets.md)) és a lézerlőszerből (Ultra Core 5%, Experimental Fusion Core 10%; lásd [Lézerek és lőszer](/wiki/06-Items/Lasers.md)). Az idegeneknek nincs, és az x1 és x2 lőszernek sincs. Egy lézertalálat levonja a lövő lézereinek Penetration Amp-jeit is (+2% és +8% között foglalatonként, a lézerei átlaga) és egy drónformáció áthatolását (Gemini +9%, Stiletto +16%): az összeg lézer esetén **50%**-nál, rakéta esetén 40%-nál megáll ([hogyan adódik össze egy lézertalálat](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)).
- **Példák**: 80% elnyelés egy Lancet III (35%) ellen: a pajzsok a találat 45%-át fogják fel, a hajótest az 55%-át. 100% elnyelés ellene: 65% és 35%. 112% 12% áthatolás ellen: a teljes találat. 45% (egy Light Shield Core önmagában) 35% ellen: 10% a pajzsra, a többi a hajótestre. Egyetlen rakéta sem hatol át teljesen egy Light Shield Core-on. A legjobb lézer (50%) megteszi: ellene a legjobb pajzs (80%) a találat 30%-át, a hajótest 70%-át kapja, egy Light Shield Core egyedül (45%) semmit.
- Az idegeneknek nincs elnyelés értékük: minden találatot 80% / 20% arányban osztanak meg, a találat áthatolását levonva.
- A Siphon Battery sebzése kizárólag a pajzsból jön: az elnyelés és az áthatolás nem játszik szerepet.

#### A 100% elérése és túllépése {#reaching-and-passing-100-}

- **Alapból**: legfeljebb 80% (fent).
- **Shield Absorbance Boost**: egy állandó Szezonbolt-buff, amelyet wipe-pontokkal vásárolsz, **szintenként +0,1 pont, legfeljebb +10 pont** (100 szint, egyenként 25 WP). Fix pontokat ad a hajód elnyeléséhez, bármely pajzzsal rendelkező hajón ugyanannyit: a 80% 4 szinttel (100 WP) 80,4%-ra nő, egy Light Shield Core 45%-a pedig 12 szinttel (300 WP) 46,2%-ra. A pajzs nélküli hajó 0%-on marad. A 100 szint 2 500 WP-ba kerül, ami több wipe-ra szóló cél: a wipe-pontok mai forrásai (a kilövési mérföldkövek és a küldetések) a felső határukat elérve összesen 855 WP-t fizetnek, a wipe-okon át megőrizve, és ez 34 szintet ér, vagyis +3,4 pontot. További wipe-pont-források vannak tervben. Lásd: [Szezon és wipe-pontok](/wiki/03-Mechanics/Wipe-Timeline.md#cross-season-progression-permanent-buffs-).
- **Kovácsműhely**: a pajzsok és a pajzscellák kaphatnak **Elnyelésnövelés** buffot, amely megszorozza az értéket: egy 50%-os pajzson a +5% +2,5 pont. Egy teljesen kovácsolt, Örök ritkaságú legjobb szett (mag és három cella, minden buff a maximumon, +15%) legfeljebb 12 pontot ad, átlagosan körülbelül 10-et (lásd [A Kovácsműhely](/wiki/06-Items/Forge.md)).
- **Együtt**: alapból 80%, +3,4 pont buff (a mai 855 wipe-pont mind) és legfeljebb +12 pont Kovácsműhely-buff együtt ma legfeljebb **95,4%**-ot tesz ki; a buff mind a 100 szintjével (+10 pont, 2 500 WP) ez 102% lenne. Sem a buff, sem a Kovácsműhely önmagában nem éri el a 100%-ot; eljutni odáig több wipe-ra szóló cél, és további wipe-pont-források vannak tervben.

### Pajzsboostok: kapacitás, elnyelés, töltődés {#shield-boosts-capacity-absorbance-recharge}

Minden pajzsboost a három érték egyikét növeli, és a Boosterek ablakban a saját fajtája alatt szerepel:

- **Kapacitás** (a pajzspontok maximuma): a Shield Wall Booster 1 és 2, valamint az állandó Shield Capacity Boost.
- **Elnyelés** (a találatnak az a része, amelyet a pajzsaid felfognak): az állandó Shield Absorbance Boost (szintenként +0,1 pont, legfeljebb +10 pont).
- **Töltődés** (a másodpercenként visszatöltődő pajzspontok): a Shield Regen Booster.

A számokat lásd: [Boosterek](/wiki/06-Items/Boosters.md).

---

## Passzív pajzsregeneráció {#shield-passive-regeneration}

A pajzsok idővel passzívan regenerálódnak, hogy harcra készen tartsanak.

- **Regenerációs ütem**: ha a pajzsok a maximális kapacitás alatt vannak, másodpercenként a töltődési sebességednek megfelelő pajzspontot állítanak vissza.
- **Megszakítás harcban (15 mp késleltetés)**: a regeneráció leáll, ha sebzést kapsz, és csak **15 másodpercnyi** sebzésmentesség után indul újra. Az Adamant és a Redoubt drónformáció ([Drónformációk](/wiki/03-Mechanics/Formations.md)) kivétel: másodpercenként pajzsot ad vissza, harcban is.
