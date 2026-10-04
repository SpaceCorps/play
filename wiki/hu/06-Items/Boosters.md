<!-- wiki-i18n source: 539575474f5854de -->
<!-- wiki-i18n title: Boosterek -->
# Boosterek {#boosters}

A boosterek ideiglenesen módosítják a hajód értékeit, hogy erősítsék a harci, a védelmi, a szintlépési és a nyersanyaggyűjtési képességeidet.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Tárgyfa {#item-tree}

Amit a Gyártás elkészít, ahhoz előbb a technológiája kell; vidd az egeret egy tárgy fölé, hogy lásd, mennyi ideig tart a kutatása. A technológiafa, az üzemanyag és a boost: [Kutatás](/wiki/03-Mechanics/Research.md).

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

## Halmozási szabályok {#stacking-rules}

A boosterek additív skálázási rendszert használnak:
1. **A bónuszszázalékok összeadódnak**: ha két különböző boostert veszel, amelyek mindegyike +10% lézersebzést ad, összesen **+20% lézersebzést** kapsz.
2. **Az időtartamok szorzódva halmozódnak**: ha _ugyanazt_ a boostert többször megveszed, meghosszabbodik az aktív ideje. A _különböző_ boosterek időzítői párhuzamosan futnak.
3. **Időzítőnézet**: az aktív boosterek a HUD Boosterek ablakában jelennek meg, az összesített, csoportosított aktív bónuszokkal és a következő lejárattal.

---

## Aktív boosterek {#active-boosters}

Minden booster alapesetben **10 órán** át tart, és vásárláskor, megszerzéskor vagy átvételkor azonnal aktiválódik. A három **II** booster nem kapható: a technológiájukat a Skylabban kutatod ki ([Kutatás](/wiki/03-Mechanics/Research.md)), majd a Gyártásban elkészíted őket, és az átvételkor a 10 órájuk azonnal elindul, ahogy vásárláskor is.

| Név | Ritkaság | Alaphatás (10 óra) | Ár (Thulium) |
| :--- | :--- | :--- | :--- |
| **Damage Amp** | Ritka | +10% lézersebzés | 20 000 |
| **Damage Amp II** | Ritka | +10% lézersebzés | Gyártás: 20 000 |
| **Shield Wall** | Ritka | +25% pajzskapacitás (a pajzspontok maximuma) | 15 000 |
| **Shield Wall II** | Ritka | +25% pajzskapacitás (a pajzspontok maximuma) | Gyártás: 15 000 |
| **Hull Plating** | Ritka | +10% max. életerő | 15 000 |
| **Hull Plating II** | Ritka | +10% max. életerő | Gyártás: 15 000 |
| **Shield Regen** | Ritka | +25% pajzstöltődési sebesség (másodpercenként visszatöltődő pajzspontok) | 10 000 |
| **Experience Kit** | Gyakori | +20% szerzett tapasztalat | 8 000 |
| **Honor Beacon** | Gyakori | +20% szerzett becsületpont | 10 000 |
| **Resource Magnet** | Ritka | +25% rakományláda-hozam | 18 000 |
| **Loot Luck** | Legendás | +5% esély ritka zsákmányra az NPC-ktől | 30 000 |

---

## Pajzsboostok: háromféle {#shield-boosts-three-kinds}

A pajzsnak három külön értéke van, és minden pajzsboost pontosan egyet növel közülük. A Boosterek ablak külön tartja őket, mindegyiket ikonnal és összesítéssel:

| Fajta | Mi ez | Mi növeli |
| :--- | :--- | :--- |
| **Pajzskapacitás** | A pajzspontjaid maximuma | Shield Wall, Shield Wall II, az állandó **Shield Capacity Boost** (Szezonbolt) |
| **Pajzselnyelés** | A találatok azon része, amelyet a pajzsaid felfognak (a többit a hajótest kapja); meghaladhatja a 100%-ot | Az állandó **Shield Absorbance Boost** (Szezonbolt): szintenként +0,1 pont 25 WP-ért, legfeljebb +10 pont. Booster nem növeli |
| **Pajzstöltődés** | Másodpercenként visszatöltődő pajzspontok | Shield Regen. Állandó buff nem növeli |

Az azonos fajtájú boostok összeadódnak; sosem számítanak bele egy másik fajtába. Az állandó buffokat a [Szezonokon átívelő fejlődés](/wiki/03-Mechanics/Wipe-Timeline.md) írja le; magukat az értékeket a [Pajzsmechanika](/wiki/03-Mechanics/Shields.md).
