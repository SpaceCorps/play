# Boosters

<!-- wiki-search: damage amp; damage amp ii; shield wall; shield wall ii; hull plating; hull plating ii; shield regen; experience kit; honor beacon; resource magnet; loot luck -->

Boosters provide temporary stat modifications to enhance your ship's combat, defense, leveling, and resource collection capabilities.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Item tree

What Assembly makes needs its technology first; point at an item to see how long it takes to research. The technology tree, the fuel and the boost: [Research](/wiki/03-Mechanics/Research.md).

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

## Stacking Rules

Boosters use an additive scaling system:
1. **Bonus Percentages Stack Additively**: If you buy two different boosters that both grant +10% Laser Damage, you will receive a total bonus of **+20% Laser Damage**.
2. **Durations Stack Multiplicatively**: Purchasing the _same_ booster multiple times extends its active duration. Timers for _different_ boosters run in parallel.
3. **Timer View**: Active boosters are displayed on the HUD under the Booster window, showing total grouped active bonuses and the next expiration event.

---

## Active Boosters

Every booster lasts for a base duration of **10 hours** and activates immediately upon purchase, receipt or collection. The three **second-tier** boosters (Laser Damage Booster II, Shield Wall Booster II and Hull Plating Booster II) are not sold: you research their technology in the Skylab ([Research](/wiki/03-Mechanics/Research.md)), then make them in Assembly, and collecting one starts its 10 hours at once, like buying one.

| Name | Rarity | Base Effect (10 Hours) | Price (Thulium) |
| :--- | :--- | :--- | :--- |
| **Laser Damage Booster I** | Rare | +10% Laser Damage | 20,000 |
| **Laser Damage Booster II** | Rare | +10% Laser Damage | Assembly: 20,000 |
| **Shield Wall Booster I** | Rare | +25% Shield Capacity (maximum shield points) | 15,000 |
| **Shield Wall Booster II** | Rare | +25% Shield Capacity (maximum shield points) | Assembly: 15,000 |
| **Hull Plating Booster I** | Rare | +10% Max Hitpoints | 15,000 |
| **Hull Plating Booster II** | Rare | +10% Max Hitpoints | Assembly: 15,000 |
| **Shield Regen Booster** | Rare | +25% Shield Recharge Rate (shield points restored per second) | 10,000 |
| **Experience Booster** | Common | +20% Experience gain | 8,000 |
| **Honor Booster** | Common | +20% Honor points gain | 10,000 |
| **Resource Magnet Booster** | Rare | +25% Cargo box yield | 18,000 |
| **Loot Luck Booster** | Legendary | +5% Rare drop chance from NPCs | 30,000 |

> [!NOTE]
> **Booster or amp?** They are different things. Every booster has **Booster** in its name, runs on a timer and has nothing to fit: the **Laser Damage Booster I** and **Laser Damage Booster II** give +10% laser damage for 10 hours, from the Shop or from Assembly. The **Damage Amp**, **Crit Amp** and **Penetration Amp** (tiers I to IV) are laser amplifiers: modules you fit into a laser's amp slot, with no timer ([Lasers & Ammo](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-)). Before 0.4.12 the boosters were called Damage Amp and Damage Amp II, Shield Wall and Shield Wall II, Hull Plating and Hull Plating II, Shield Regen, Experience Kit, Honor Beacon, Resource Magnet and Loot Luck; the boosters you had running went on under their new names. The Hull Plating **Booster** is not the armour **Hull Plating** that fits a ship's hull plate slots ([Hull Plating](/wiki/06-Items/Hull-Plating.md#hull-plating-or-booster)).

---

## Shield Boosts: Three Kinds

Shields have three separate stats, and every shield boost raises exactly one of them. The Boosters window keeps them apart, with an icon and a total for each:

| Kind | What it is | Boosts that raise it |
| :--- | :--- | :--- |
| **Shield Capacity** | Your maximum shield points | Shield Wall Booster I, Shield Wall Booster II, the permanent **Shield Capacity Boost** (Season Store) |
| **Shield Absorbance** | The share of every hit your shields take (the rest hits the hull); it may pass 100% | The permanent **Shield Absorbance Boost** (Season Store): +0.1 points a level for 25 WP, +10 points at most. No booster raises it |
| **Shield Recharge** | Shield points restored per second | Shield Regen Booster. No permanent buff raises it |

Boosts of one kind add up; they never count toward another kind. The permanent buffs are described under [Cross-Season Progression](/wiki/03-Mechanics/Wipe-Timeline.md); the stats themselves under [Shield Mechanics](/wiki/03-Mechanics/Shields.md).
