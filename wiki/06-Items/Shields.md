# Shields & Defense

Defensive modules provide shield capacity, absorb damage, and recharge your defenses.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Item tree

What Assembly makes needs its technology first; point at an item to see how long it takes to research. The technology tree, the fuel and the boost: [Research](/wiki/03-Mechanics/Research.md).

```tree
Light Shield Core | shield, shoddy | buy 20000 Credits | /wiki/06-Items/Shields.md#shield-cores
Basic Shield Core | shield, common | buy 2000 Thulium | /wiki/06-Items/Shields.md#shield-cores
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cores
Adaptive Core I | hybrid-generator, shoddy | buy 100000 Credits | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core II | hybrid-generator, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Adaptive Core I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core III | hybrid-generator, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Adaptive Core II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Absorption Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells

Light Shield Core -> Basic Shield Core => Heavy Shield Core
Adaptive Core I => Adaptive Core II => Adaptive Core III
Absorption Shield Cell I => Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell I => Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```
<!-- item-tree:end -->

## Shield Cores

Equip shield cores to generate active defensive barriers, in your ship's generator slots or on your [drones](/wiki/03-Mechanics/Drones.md) (a drone's slot counts as a core slot). Note that heavy shields weigh down your speed. A shield core in an **ability slot** instead gives you the **Shield Surge** in the Special Effect column, a shield repair over ten seconds, and adds no shield of its own (see [Abilities](/wiki/03-Mechanics/Abilities.md)).

| Name | Rarity | Capacity | Recharge Rate | Absorbance | Shield % | Speed % | Cell Slots | Special Effect | Cost |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Light Shield Core** | Shoddy | 10,000 | 333/s | 45% | +5% | -1% | 1 | Shield Surge I | 20,000 Credits |
| **Basic Shield Core** | Common | 15,000 | 500/s | 48% | +10% | -3% | 2 | Shield Surge II | 2,000 Thulium |
| **Heavy Shield Core** | Rare | 25,000 | 833/s | 50% | +20% | -5% | 3 | Shield Surge III | Craftable Only |

The **Heavy Shield Core** is made in [Assembly](/wiki/06-Items/Overview.md#upgrading-modules) from a Basic Shield Core, with 2,000 Thulium, 20 Cataclysite, 8 Reinforced Hull Plates and 3 Dark Matter Plates ([Dark Matter and Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)). It keeps the enchant tier of the core it uses up, and its buffs are rolled again ([Module upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Take the Basic Shield Core off your ship (and its cells out of it) first: a core that is fitted or holds cells is not used up.

**Absorbance** is the share of each hit your shields take; the hull takes the rest. A shield alone is **45 to 50%**, and its cells add the rest: the best shield with the best cells (a Heavy Shield Core with three Absorption Shield Cell IVs) is **80%**, the most a ship has out of the box. Two permanent boosts add to that: the Shield Absorbance Boost of the Season Store (+0.1 points a level, 100 levels, 25 Wipe Points each) and the Forge's absorbance buffs. Today's sources of Wipe Points (855 in total at their caps, carried across wipes; more sources are planned) buy 34 of those 100 levels (+3.4 points), which with a fully forged Eternal set is about **95%**. The stat is not capped at 100%, though: an attacker's *shield penetration* is taken off it, so what a ship has over 100% is its margin against penetration. See [Shield Mechanics](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-).

---

## Hybrid Generators (Adaptive Cores)

Adaptive cores act as hybrid generators, combining shield and speed capabilities. They accept both Thrusters and Shield Cells in their slots (one module per slot, of either kind). Their Shield and Speed Bonus count like a shield's or an engine's (the four best, times the slot's share). They have no absorbance: they don't change your ship's absorbance, and cells in them add capacity and recharge only. Only shields take a share of a hit, so cells in an Adaptive Core need a shield on the ship too.

| Name | Rarity | Shield Bonus % | Speed Bonus % | Slots | Special Effect | Cost |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **Adaptive Core I** | Shoddy | +4% | +2.4% | 1 | — | 100,000 Credits |
| **Adaptive Core II** | Common | +6.4% | +3.2% | 2 | — | Craftable Only |
| **Adaptive Core III** | Rare | +8% | +4% | 3 | — | Craftable Only |

The **Adaptive Core II** is made in [Assembly](/wiki/06-Items/Overview.md#upgrading-modules) from an Adaptive Core I, with 1,000 Thulium, 10 Ship Fragments, 1 Power Core and 2 Velkonite Reinforced Plates. The **Adaptive Core III** is made there from an Adaptive Core II, with 2,000 Thulium, 60 Ship Fragments, 3 Power Cores and 3 Dark Matter Plates ([Dark Matter and Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)). Each keeps the enchant tier of the core it uses up, and its buffs are rolled again ([Module upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Take the core you use up off your ship (and its thrusters and cells out of it) first: a core that is fitted or holds modules is not used up.

---

## Shield Cells

Shield Cells are fitted inside Shield Cores or Adaptive Cores (as many as the core's slots) to boost that core. In a Shield Core they raise its absorbance too, in points, and with it the share of each hit your shields take. There are two families of four tiers each: the **Capacity Shield Cells** add the most shield and recharge, the **Absorption Shield Cells** the most absorbance (at every tier twice the absorbance and half the shield and recharge of the Capacity cell of that tier). Capacity helps a ship whose shield ends the fight, Absorption a ship whose hull ends it. A core with all its slots full of one cell: a Light Shield Core (1 slot) is 47 to 55%, a Basic Shield Core (2 slots) 52 to 68% and a Heavy Shield Core (3 slots) 56 to 80%, from tier I Capacity cells to tier IV Absorption cells. Unequipping the core, or using it up as the donor of a [Forge](/wiki/06-Items/Forge.md) merge, returns its cells to the inventory.

| Name | Rarity | Capacity Boost | Recharge Boost | Absorbance Boost | Cost |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Capacity Shield Cell I** | Shoddy | +3,000 | +250/s | +2% | 30,000 Credits |
| **Capacity Shield Cell II** | Common | +6,000 | +500/s | +3% | Craftable Only |
| **Capacity Shield Cell III** | Rare | +9,000 | +750/s | +4% | Craftable Only |
| **Capacity Shield Cell IV** | Epic | +12,000 | +1,000/s | +5% | Craftable Only |
| **Absorption Shield Cell I** | Shoddy | +1,500 | +125/s | +4% | 30,000 Credits |
| **Absorption Shield Cell II** | Common | +3,000 | +250/s | +6% | Craftable Only |
| **Absorption Shield Cell III** | Rare | +4,500 | +375/s | +8% | Craftable Only |
| **Absorption Shield Cell IV** | Epic | +6,000 | +500/s | +10% | Craftable Only |

Tier I of each family is sold for 30,000 Credits. Tiers II to IV are made in [Assembly](/wiki/06-Items/Overview.md#upgrading-modules), each from the cell of the same family one tier below (a Capacity Shield Cell II from a Capacity Shield Cell I, a III from a II, a IV from a III), with Thulium, drops and plates: 2 or 4 Velkonite Reinforced Plates from your Skylab for tier II or III, and 3 Dark Matter Plates for tier IV. A cell never changes family: you choose Capacity or Absorption when you buy tier I. The new cell keeps the enchant tier of the cell it uses up, and its buffs are rolled again ([Module upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Cells don't fit an [ability slot](/wiki/03-Mechanics/Abilities.md); they belong inside shields and Adaptive Cores.
