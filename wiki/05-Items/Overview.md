# Items Overview

Items are the core components that upgrade your ship's capabilities. They can be purchased from the Shop, found as drops, crafted in Assembly, or raised and merged in the [Forge](/wiki/05-Items/Forge.md).

## Rarity Levels

Items come in different rarities, which determine their quality and base stats:

- **Shoddy**: Basic starter equipment.
- **Common**: Standard military grade.
- **Rare**: High-performance gear.
- **Epic**: Advanced technology.
- **Mythical**: Legendary experimental prototypes.
- **Legendary**: Rare and powerful relic modules.
- **Eternal**: Cosmic tier modules with unrivaled power.

## Upgrading Modules

The top laser amps, shield cell and thrusters, the Heavy Shield Core and the Engine III are not sold. You make each in Assembly from the Thulium piece below it (a Heavy Shield Core from a Basic Shield Core, an Engine III from an Engine II, a Thruster III from a Thruster II), some Thulium, what the aliens drop and plates from your Skylab's Forgery. The piece must be loose in your inventory: take it off your ship and out of its laser, shield or engine first (a shield or an engine must hold no cells or thrusters of its own), and out of the Transport Cache. **The new item keeps the [enchant](/wiki/05-Items/Overview.md#item-enchants) tier of the piece it uses up, and its buffs are rolled again** (a Godly Pulse Amp makes a Godly Nova Amp with two new buffs). Which copy goes is your choice: the recipe card in Assembly shows your copies when they differ, and asks first before it uses one above Standard. If you choose none, the ones with the lowest enchant tier are used first, so your highest-tier copies stay (among copies of one tier the oldest goes first, whatever their buffs). The whole rule is on the [Forge](/wiki/05-Items/Forge.md#module-upgrades-in-the-assembly) page.

| Upgrade | Takes | Thulium | Materials | Time |
| :--- | :--- | :---: | :--- | :---: |
| **Nova Amp** | 1 Pulse Amp | 1,200 | 30 Cataclysite, 1 Power Core, 3 Velkonite Reinforced Plate | 60 s |
| **Apex Amp** | 1 Prism Amp | 1,200 | 30 Cataclysite, 1 Power Core, 3 Velkonite Reinforced Plate | 60 s |
| **Sovereign Shield Cell** | 1 Prime Shield Cell | 2,500 | 20 Cataclysite, 8 Reinforced Hull Plate, 6 Velkonite Reinforced Plate | 90 s |
| **Plasma Thruster** | 1 Ion Thruster | 2,000 | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | 90 s |
| **Thruster III** | 1 Thruster II | 1,500 | 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | 60 s |
| **Heavy Shield Core** | 1 Basic Shield Core | 2,000 | 20 Cataclysite, 8 Reinforced Hull Plate, 6 Velkonite Reinforced Plate | 90 s |
| **Engine III** | 1 Engine II | 2,000 | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | 90 s |

On average a Goombah drops 4 Cataclysite, 3.25 Ship Fragments, 0.6 Reinforced Hull Plates and 0.25 Power Cores, so the drops of a Nova Amp or an Apex Amp take about 8 Goombahs, a Thruster III's about 10, a Sovereign Shield Cell's or a Heavy Shield Core's about 14 and a Plasma Thruster's or an Engine III's about 19. A Bulwark drops 2 Cataclysite, 2 Ship Fragments and 0.3 Reinforced Hull Plates, but no Power Core.

The Velkonite Reinforced Plates are not dropped: your [Skylab](/wiki/03-Mechanics/Skylab.md) Forgery makes them from Velkonite ore, 40 ore a plate at Forgery level 1. A level 1 Velkonite Collector mines 12 ore an hour, so an amp's 3 plates are 10 hours of mining and a cell's or a thruster's 6 plates 20 hours (4 and 8 hours from a level 5 collector); a Thruster III's 4 plates are 13 hours, a Heavy Shield Core's or an Engine III's 6 plates 20. See [Resources](/wiki/05-Items/Resources.md) for where every material comes from.

The **Helios Beam** is an upgrade of the same kind, a laser out of a laser: it uses up a Starfire-3 and takes 2,000 Thulium, 50 Cataclysite, 2 Power Cores, 4 Reinforced Hull Plates and 18 Orvium Reinforced Plates, and keeps the enchant tier of the Starfire-3 the same way. So is the **Starfire-3**: it uses up a Quantum Laser 3 and takes 1,500 Thulium, 100,000 Credits, 15 Ship Fragments, 1 Reinforced Hull Plate and 8 Velkonite Reinforced Plates, and keeps the Quantum Laser 3's enchant tier. Both are on the [Lasers](/wiki/05-Items/Lasers.md) page; the table above lists the amps, the cell, the thrusters, the Heavy Shield Core and the Engine III.

## Item Enchants

Equipment carries an **Enchant**: a tier that lets it hold up to a few **buffs**, each a percentage added to one of the item's stats (for example Shield Capacity +6.1%). There are 5 Enchant tiers:

| Tier | Buffs held at most | Size of each buff | Chance on a crafted item |
| :--- | :---: | :---: | :---: |
| 1. **Standard** | 0 | none | 88.89% |
| 2. **Tainted** | 1 | +2% to +5% | 10% |
| 3. **Godly** | 2 | +4% to +8% | 1% |
| 4. **Rupturing** | 3 | +6% to +11% | 0.1% |
| 5. **Eternal** | 4 | +9% to +15% | 0.01% |

- Shop items are always Standard. Equipment you build in the Assembly rolls a tier when you collect it (the chance column). Above that, the tier goes up in the [Forge](/wiki/05-Items/Forge.md), one step at a time; the one other way is a module upgrade in the Assembly (a Nova Amp, an Apex Amp, a Sovereign Shield Cell, a Plasma Thruster, a Thruster III, a Heavy Shield Core, an Engine III, the Helios Beam), which keeps the tier of the piece it is made from.
- An item never holds more buffs than it has stats: a shield core has four, a laser three (the Quantum Laser 1 and 2 two, since they have no critical chance of their own), an engine, a thruster or an Adaptive Core two, a Crit Amp 1 or a Repair Drone one, the higher crit amps two, the damage amps and shield cells three. The limit of the tier is the smaller of the two numbers.
- A **Range** buff never passes +5%, at any tier.
- Buffs stay small next to the next item up: a maxed Quantum Laser 1 still does less damage than a plain Quantum Laser 2.

Enchanted stats are displayed on the item icon grid card (e.g. `[T]` for Tainted, `[G]` for Godly) and outlined in the item's statistics tooltip.

## The Forge

The **Forge** (the second tab of the Assembly page) raises a piece of equipment one tier at a time for credits and alien drops, and merges two copies of an item into one. A tier can't be skipped: Standard, Tainted, Godly, Rupturing, Eternal, in that order. Every step costs more than the one before, and can fail. The steps, the materials and the rules of a merge are in [The Forge](/wiki/05-Items/Forge.md).

## Currencies

Every material and both currencies, with where each comes from and what it is for, are on the [Resources](/wiki/05-Items/Resources.md) page.

- **Credits**: Standard currency used for basic items. Earned by killing aliens and completing [quests](/wiki/03-Mechanics/Quests.md); each level's Special mission also pays items (lasers, shield parts, Power Cores, Ship Fragments).
- **Thulium**: Rare currency used for high-end equipment. Every alien pays some when it dies (more from the tougher ones), and missions and the Skylab's Thulium Farm give more. See [Thulium](/wiki/05-Items/Resources.md#thulium).

## Categories

The Shop, the Hangar's inventory and the other item lists read in one order: the ship, then a laser with its amps and ammo, a shield with its cells, an engine with its thrusters, the Adaptive Cores, extras, drones, boosters and resources. Inside a kind the cheapest comes first.

- **Lasers**: Your primary weapon systems, and the [amps](/wiki/05-Items/Lasers.md) that go into them.
- **Shields**: Generators and [cells](/wiki/05-Items/Shields.md) for defense.
- **Propulsion**: Engines and [thrusters](/wiki/05-Items/Propulsion.md) for speed.
- **Repair Drones**: Extras that repair your hull, each faster than the last: Repair Drone I, II and III cost 5,000, 15,000 and 35,000 credits, Repair Drone IV 2,000 Thulium. The rates are in [Combat](/wiki/03-Mechanics/Combat.md).
- **Cloaking CPUs and the EMP Charge**: Extras for a fight or a flight: a Cloaking CPU hides your ship until you end it (S, M and L: 10, 25 and 50 uses, 5,000, 11,250 and 20,000 Thulium), an EMP Charge makes you untargetable for 3 seconds, breaks every lock on you and ends every cloak nearby (500 Thulium). See [Extras](/wiki/05-Items/Extras.md).
- **Resources**: what aliens drop and the Skylab makes for crafting: Ship Fragments, the four crystals, Power Cores, the Velkonite and Orvium plates, and two that come from elsewhere: **Dark Matter**, which the [black hole](/wiki/03-Mechanics/Black-Hole.md) gives back for a N.I.K.E. rocket, and the **Dark Matter Plate** that Assembly presses from it for the top two steps of [The Forge](/wiki/05-Items/Forge.md).
