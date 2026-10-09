<!-- wiki-i18n source: 54910cbb508beed2 -->
<!-- wiki-i18n title: Boosterek -->
# Boosterek {#boosters}

<!-- wiki-search: damage amp; damage amp ii; shield wall; shield wall ii; hull plating; hull plating ii; shield regen; experience kit; honor beacon; resource magnet; loot luck -->

A boosterek ideiglenesen módosítják a hajód értékeit, hogy erősítsék a harci, a védelmi, a szintlépési és a nyersanyaggyűjtési képességeidet.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Tárgyfa {#item-tree}

Amit a Gyártás elkészít, ahhoz előbb a technológiája kell; vidd az egeret egy tárgy fölé, hogy lásd, mennyi ideig tart a kutatása. A technológiafa, az üzemanyag és a boost: [Kutatás](/wiki/03-Mechanics/Research.md).

```tree
Experience Booster | booster, common | buy 8000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Honor Booster | booster, common | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Laser Damage Booster II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Regen Booster | booster, rare | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster I | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster I | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Resource Magnet Booster | booster, rare | buy 18000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Laser Damage Booster I | booster, rare | buy 20000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Loot Luck Booster | booster, legendary | buy 30000 Thulium | /wiki/06-Items/Boosters.md#active-boosters

Shield Wall Booster I -> Shield Wall Booster II
Hull Plating Booster I -> Hull Plating Booster II
Laser Damage Booster I -> Laser Damage Booster II
```
<!-- item-tree:end -->

## Halmozási szabályok {#stacking-rules}

A boosterek additív skálázási rendszert használnak:
1. **A bónuszszázalékok összeadódnak**: ha két különböző boostert veszel, amelyek mindegyike +10% lézersebzést ad, összesen **+20% lézersebzést** kapsz.
2. **Az időtartamok szorzódva halmozódnak**: ha _ugyanazt_ a boostert többször megveszed, meghosszabbodik az aktív ideje. A _különböző_ boosterek időzítői párhuzamosan futnak.
3. **Időzítőnézet**: az aktív boosterek a HUD Boosterek ablakában jelennek meg, az összesített, csoportosított aktív bónuszokkal és a következő lejárattal.

---

## Aktív boosterek {#active-boosters}

Minden booster alapesetben **10 órán** át tart, és vásárláskor, megszerzéskor vagy átvételkor azonnal aktiválódik. A három **másodikszintű** booster (Laser Damage Booster II, Shield Wall Booster II és Hull Plating Booster II) nem kapható: a technológiájukat a Skylabban kutatod ki ([Kutatás](/wiki/03-Mechanics/Research.md)), majd a Gyártásban elkészíted őket, és az átvételkor a 10 órájuk azonnal elindul, ahogy vásárláskor is.

| Név | Ritkaság | Alaphatás (10 óra) | Ár (Thulium) |
| :--- | :--- | :--- | :--- |
| **Laser Damage Booster I** | Ritka | +10% lézersebzés | 20 000 |
| **Laser Damage Booster II** | Ritka | +10% lézersebzés | Gyártás: 20 000 |
| **Shield Wall Booster I** | Ritka | +25% pajzskapacitás (a pajzspontok maximuma) | 15 000 |
| **Shield Wall Booster II** | Ritka | +25% pajzskapacitás (a pajzspontok maximuma) | Gyártás: 15 000 |
| **Hull Plating Booster I** | Ritka | +10% max. életerő | 15 000 |
| **Hull Plating Booster II** | Ritka | +10% max. életerő | Gyártás: 15 000 |
| **Shield Regen Booster** | Ritka | +25% pajzstöltődési sebesség (másodpercenként visszatöltődő pajzspontok) | 10 000 |
| **Experience Booster** | Gyakori | +20% szerzett tapasztalat | 8 000 |
| **Honor Booster** | Gyakori | +20% szerzett becsületpont | 10 000 |
| **Resource Magnet Booster** | Ritka | +25% rakományláda-hozam | 18 000 |
| **Loot Luck Booster** | Legendás | +5% esély ritka zsákmányra az NPC-ktől | 30 000 |

> [!NOTE]
> **Booster vagy erősítő?** Két különböző dolog. Minden boosternek **Booster** van a nevében, időzítőn fut, és nincs mibe szerelni: a **Laser Damage Booster I** és a **Laser Damage Booster II** 10 órára +10% lézersebzést ad, a Boltból vagy a Gyártásból. A **Damage Amp**, a **Crit Amp** és a **Penetration Amp** (I–IV. szint) lézererősítők: modulok, amelyeket a lézer erősítőfoglalatába szerelsz, időzítő nélkül ([Lézerek és lőszer](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-)). 0.4.12 előtt a boosterek neve Damage Amp és Damage Amp II, Shield Wall és Shield Wall II, Hull Plating és Hull Plating II, Shield Regen, Experience Kit, Honor Beacon, Resource Magnet és Loot Luck volt; a futó boostereid az új neveiken futottak tovább. A Hull Plating **Booster** nem az a **Hull Plating** páncélzat, amely a hajó páncélzatfoglalataiba kerül ([hajótest-páncélzat](/wiki/06-Items/Hull-Plating.md#hull-plating-or-booster)).

---

## Pajzsboostok: háromféle {#shield-boosts-three-kinds}

A pajzsnak három külön értéke van, és minden pajzsboost pontosan egyet növel közülük. A Boosterek ablak külön tartja őket, mindegyiket ikonnal és összesítéssel:

| Fajta | Mi ez | Mi növeli |
| :--- | :--- | :--- |
| **Pajzskapacitás** | A pajzspontjaid maximuma | Shield Wall Booster I, Shield Wall Booster II, az állandó **Shield Capacity Boost** (Szezonbolt) |
| **Pajzselnyelés** | A találatok azon része, amelyet a pajzsaid felfognak (a többit a hajótest kapja); meghaladhatja a 100%-ot | Az állandó **Shield Absorbance Boost** (Szezonbolt): szintenként +0,1 pont 25 WP-ért, legfeljebb +10 pont. Booster nem növeli |
| **Pajzstöltődés** | Másodpercenként visszatöltődő pajzspontok | Shield Regen Booster. Állandó buff nem növeli |

Az azonos fajtájú boostok összeadódnak; sosem számítanak bele egy másik fajtába. Az állandó buffokat a [Szezonokon átívelő fejlődés](/wiki/03-Mechanics/Wipe-Timeline.md) írja le; magukat az értékeket a [Pajzsmechanika](/wiki/03-Mechanics/Shields.md).
