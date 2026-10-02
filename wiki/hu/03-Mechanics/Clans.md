<!-- wiki-i18n source: 21f10d185095b346 -->
<!-- wiki-i18n title: Klánok -->
# Klánok {#clans}

Klán alapításával vagy egy klánhoz való csatlakozással összevonhatod az erőforrásokat, fejlesztheted a közös bankot, adókulcsokat állíthatsz be, összehangolhatod magad a frakció tagjaival, és kezelheted a diplomáciát.

## Klán fejlődése {#clan-progression}

A klánok az 1. szintről indulnak, és az 5. szintig fejleszthetők. A klán fejlesztéséhez a **Klánbankból** kell kreditet kifizetni. A fejlesztések növelik a taglétszámot és a napi kifizetési korlátot.

| Klánszint | Taglétszám-korlát | Napi kifizetési korlát (tagonként) | Fejlesztés ára (kredit) |
| :---: | :---: | :---: | :--- |
| **1. szint** | 10 | 1 000 000 kredit | — |
| **2. szint** | 25 | 2 000 000 kredit | 10 000 000 kredit |
| **3. szint** | 50 | 3 000 000 kredit | 100 000 000 kredit |
| **4. szint** | 75 | 4 000 000 kredit | 1 000 000 000 kredit |
| **5. szint** | 100 | 5 000 000 kredit | 10 000 000 000 kredit |

---

## Klángazdaság és adózás {#clan-economy-taxation}

A klánok adóalapú pénzügyi rendszerben működnek:

### 1. Napi adózás {#1-daily-taxation}

- **Adókulcs**: a Vezér vagy az Alvezérek **0% és 5%** közötti napi adókulcsot állíthatnak be.
- **Automatikus beszedés**: naponta egyszer (UTC) a szerver automatikusan beszedi az adót az összes klántagtól.
- **Képlet**: az adót minden tag aktuális kreditegyenlegének `ClanTaxRate` része adja.
  - *Példa*: ha 10 000 000 kredited van, és a klánadó 2%, 200 000 kredit vonódik le a számládról, és kerül a Klánbankba.
  - Önkéntes kreditadományok is tehetők, a következő szakaszban lévő korlátig.

### 2. Adományok {#2-donations}

- **Adományozás**: bármelyik tag küldhet kreditet a Klánbankba a Klán oldalról. Az adatlap megmutatja, mennyit küldhetsz még.
- **Adománykorlát**: egy pilóta **24 óra alatt legfeljebb 1 000 000 kreditet** küldhet klánokba, az összes klánt együtt számítva, amelyben a pilóta valaha volt. A klán elhagyása és egy másikhoz csatlakozás nem ad új keretet.
- **Nincs napi nullázás**: a 24 óra csúszik. Minden adomány pontosan 24 órával a megtétele után nem számít többé, és az adatlap megmondja, mikor jár le a legrégebbi, és mennyi tér vissza. A megmaradt keretet meghaladó adományt egészében elutasítják.
- A napi adó nem adomány, és nem használja fel a keretedet.

### 3. Bankkifizetések {#3-bank-payouts}

- **Kifizetési korlátok**: a klán vezetői és tisztjei kreditet oszthatnak ki a Klánbankból egyes tagoknak.
- **Napi korlát**: egy tag egyetlen naptári napon (UTC) legfeljebb `1,000,000 * ClanLevel` kreditet kaphat kifizetésben.

---

## Hierarchia és rangok {#hierarchy-roles}

A klánok szerepalapú rangrendszert használnak a jogosultságok kezelésére:

- **Vezér (3. szerep)**: teljes adminisztratív hozzáférése van, beleértve a fejlesztést, az adók beállítását, a diplomáciát, az előléptetéseket, a kizárást és a klán feloszlatását.
- **Alvezér (2. szerep)**: beállíthatja az adókulcsokat, kreditet fizethet ki, kezelheti a diplomáciát, és előléptetheti vagy lefokozhatja az alacsonyabb rangúakat.
- **Veterán (1. szerep)**: megbízható tag, aki elfogadhatja a klánhoz érkező új jelentkezéseket.
- **Tag (0. szerep)**: hétköznapi játékos, adminisztratív jogosultságok nélkül.

### Jogosultságok táblázata {#permissions-table}

| Művelet | Vezér | Alvezér | Veterán | Tag |
| :--- | :---: | :---: | :---: | :---: |
| **A klán feloszlatása** | ✅ | ❌ | ❌ | ❌ |
| **A klán fejlesztése** | ✅ | ❌ | ❌ | ❌ |
| **Adókulcs beállítása** | ✅ | ✅ | ❌ | ❌ |
| **Kredit kifizetése** | ✅ | ✅ | ❌ | ❌ |
| **Diplomácia kezelése** | ✅ | ✅ | ❌ | ❌ |
| **Előléptetés / Kizárás** | ✅ | ✅* | ❌ | ❌ |
| **Jelentkezések elfogadása** | ✅ | ✅ | ✅ | ❌ |

*\*Az Alvezérek csak náluk alacsonyabb rangú tagokat léptethetnek elő, fokozhatnak le vagy zárhatnak ki.*

### Amikor a Vezér távozik {#when-the-leader-leaves}

A Vezér nem hagyhat el olyan klánt, amelyben még vannak más tagok: előbb léptess elő egy Alvezért Vezérré (a Vezér Alvezérré lép vissza), vagy lépj ki utolsóként, ami feloszlatja a klánt. Ha a Vezér törli a fiókját (Beállítások › Fiók), a vezetés a legmagasabb rangú tagra száll, holtverseny esetén a legrégebbi tagra; az egyedül lévő Vezér feloszlatja a klánt, a bankkal együtt.

---

## Diplomácia {#diplomacy}

A klánok hivatalos diplomáciai kapcsolatokat létesíthetnek más szervezetekkel a célklán rövidítésének megadásával:

- **Szövetség**: hivatalosan szövetséges klánok. A baráti státusz megjelenik a térképen.
- **Megnemtámadási egyezmény (NAP)**: megegyezés az ellenségeskedéstől való tartózkodásról.
- **Háború**: hivatalos hadüzenet. A háborús célpontokat bárhol, büntetés nélkül meg lehet támadni.

---

## Barát hozása {#bringing-a-friend}

Egy barát, aki új a játékban, a személyes meghívókódoddal csatlakozhat, és kezdőcsomagot kap; lásd: [Barátok meghívása](/wiki/03-Mechanics/Invite-Friends.md). A játékban aztán bármelyik pilótához hasonlóan jelentkezhet a klánodba.
