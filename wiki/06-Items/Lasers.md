# Lasers & Ammo

Weapons are the primary means of dealing damage in SpaceCorps.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Item tree

What Assembly makes needs its technology first; point at an item to see how long it takes to research. The technology tree, the fuel and the boost: [Research](/wiki/03-Mechanics/Research.md).

```tree
Quantum Laser 1 | laser, shoddy | buy 8000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser 2 | laser, common | buy 80000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser 3 | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-3 | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser 3, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-3, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp 1 | laser-amp, shoddy | buy 10000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp 1 | laser-amp, shoddy | buy 15000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Arc Amp | laser-amp, uncommon | buy 60000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Focus Amp | laser-amp, uncommon | buy 60000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Pulse Amp | laser-amp, rare | buy 1500 Thulium | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Prism Amp | laser-amp, rare | buy 1500 Thulium | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Nova Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Pulse Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Apex Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Prism Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Standard Battery | ammo, common | buy 10 Credits | /wiki/06-Items/Lasers.md#laser-ammunition
Siphon Battery | ammo, rare | buy 0.25 Thulium | /wiki/06-Items/Lasers.md#siphon-battery
Advanced Plasma | ammo, rare | buy 0.5 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Ultra Core | ammo, rare | buy 1 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Experimental Fusion Core | ammo, epic | buy 2.2 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition

Quantum Laser 1 -> Quantum Laser 2 -> Quantum Laser 3 => Starfire-3 => Helios Beam
Damage Amp 1 -> Arc Amp -> Pulse Amp => Nova Amp
Crit Amp 1 -> Focus Amp -> Prism Amp => Apex Amp
Standard Battery -> Advanced Plasma -> Ultra Core -> Experimental Fusion Core
```
<!-- item-tree:end -->

## Lasers

Equip lasers directly on ship weapon slots or inside drones to increase your offensive capabilities.

| Name | Rarity | Base Damage | Critical Chance | Range | Amp Slots | Cost |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Quantum Laser 1** | Shoddy | 55 | – | 600 | 1 | 8,000 Credits |
| **Quantum Laser 2** | Common | 65 | – | 700 | 2 | 80,000 Credits |
| **Quantum Laser 3** | Rare | 80 | 10% | 800 | 3 | Craftable Only |
| **Starfire-3** | Mythical | 135 | 15% | 850 | 3 | Craftable Only |
| **Helios Beam** | Mythical | 185 | 25% | 900 | 3 | Craftable Only |

The Range column is each laser's own. **Your ship fires at the average of the ranges of its lasers** (the lasers in your drones count too), rounded to the nearest unit, and every laser fires once the target is inside that distance. A Starfire-3 beside two Quantum Laser 2 gives a ship range of 750, not 850; three Starfire-3 keep 850, and lasers that are all alike change nothing. A Forge range buff counts on its own laser before the average is taken. With no laser the Hangar shows no range (a dash) and the lasers cannot fire, but your rockets still can, each with its own range (see [Rockets](/wiki/06-Items/Rockets.md)). In the Hangar the tile says "Avg. range" where your lasers differ, and hovering it lists each laser's range.

The Quantum Laser 1 and 2 have no critical chance of their own ("–"): a Damage Amp or a Crit Amp in their slots brings it. Critical hits show in a different colour in the floating damage numbers (ice cyan, larger, with a "!").

### Making the top three lasers

The **Quantum Laser 3**, the **Starfire-3** and the **Helios Beam** are made only in **Assembly**. The Quantum Laser 3 is no longer sold in the Shop; a pilot who already owns one keeps it. Each recipe asks for plates from the [Skylab's](/wiki/03-Mechanics/Skylab.md) Forgery:

| Laser | Crafting time | What it takes |
| :--- | :---: | :--- |
| Quantum Laser 3 | 1 min | 10 Ship Fragments, 2 Velkonite Reinforced Plates, 1,500 Thulium |
| Starfire-3 | 1 min | 1 Quantum Laser 3, 15 Ship Fragments, 8 Velkonite Reinforced Plates, 1 Reinforced Hull Plate, 1,500 Thulium, 100,000 Credits |
| Helios Beam | 3 min | 1 Starfire-3, 50 Cataclysite, 2 Power Cores, 18 Orvium Reinforced Plates, 4 Reinforced Hull Plates, 2,000 Thulium |

The Assembly page shows what you have against what a recipe takes, and the Assemble button says what you lack. Point at a recipe's picture or name, or at one of its materials, to read the item's full description and stats.

**The Starfire-3 is made out of a Quantum Laser 3.** You make the Quantum Laser 3 first and the Starfire-3 uses it up. Nothing the Quantum Laser 3 already took is asked again, so the two together cost exactly what a Starfire-3 cost on its own: 3,000 Thulium, 100,000 Credits, 25 Ship Fragments, 10 Velkonite Reinforced Plates, 1 Reinforced Hull Plate and 2 minutes. If you already have a Quantum Laser 3, you pay only the Starfire-3's own part. The rules are the Helios Beam's, below: the Starfire-3 keeps the enchant tier of the Quantum Laser 3 it uses up (a Godly Quantum Laser 3 makes a Godly Starfire-3) and its buffs are rolled again; you choose which Quantum Laser 3 goes, the card asks first before it uses one above Standard, and the Quantum Laser 3 must be loose: **take it off your ship first** (its amps go back to your inventory), and out of the Transport Cache. The Assemble button says "Unequip your Quantum Laser 3" when it is on a ship.

**The Helios Beam is made out of a Starfire-3.** You make the Starfire-3 first (3,000 Thulium and 100,000 Credits with its Quantum Laser 3) and the Helios Beam uses it up, as the [Master Drone](/wiki/06-Items/Drones.md) uses up a Slave Drone. Nothing the Starfire-3 already took is asked again, so the two together cost the 5,000 Thulium, the Cataclysite, Power Cores and Reinforced Hull Plates the Helios Beam asked for on its own, and 18 Orvium plates instead of 20 (the Starfire-3's ten Velkonite plates stand in for the missing two); what you pay besides is the Starfire-3's 100,000 Credits and 25 Ship Fragments. The rule is the one of the [module upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly): the Helios Beam keeps the enchant tier of the Starfire-3 it uses up (a Godly Starfire-3 makes a Godly Helios Beam) and its buffs are rolled again; you choose which Starfire-3 goes when you hold several, and the card asks first before it uses one above Standard. The Starfire-3 must be loose: **take it off your ship first** (the amps fitted into it go back to your inventory), and out of the Transport Cache. The Assemble button says "Unequip your Starfire-3" when it is on a ship.

Where the plates come from:

- **Velkonite Reinforced Plates** (Quantum Laser 3 and Starfire-3) are forged from Velkonite, 40 ore a plate at Forgery level 1. **Orvium Reinforced Plates** (Helios Beam) are forged from Orvium, 80 ore a plate.
- The ore comes only from your Skylab's collectors. A level 5 Velkonite Collector mines 18 Velkonite an hour, so the plates of a Quantum Laser 3 take about 4 hours of mining and a Starfire-3's ten (two in its Quantum Laser 3, eight in its own step) about 22. The Helios Beam is the long one: its 18 plates need 1,440 Orvium, about 4 days from a level 5 Orvium Collector.
- The Resource Storage holds 240 of each ore at level 1: 6 Velkonite plates or 3 Orvium plates at Forgery level 1. So forge as you go (a Forgery batch is up to 10 plates at level 1) or upgrade the storage.
- Forged plates wait in the Forgery until you collect them while your ship is landed, and land in your inventory as ordinary items.

Ship Fragments, Cataclysite, Power Cores and Reinforced Hull Plates drop from aliens; every source and use of each material is on the [Resources](/wiki/06-Items/Resources.md) page; the loot lists on the pages of the [Bulwark](/wiki/04-Aliens/Bulwark.md) and the [Goombah](/wiki/04-Aliens/Goombah.md) show how much.

---

## Laser Amplifiers (Amps)

Equip these directly into a laser's slot to augment its characteristics. There are two lines, four rungs each: the **damage line** adds a flat amount of damage, and the **crit line** adds critical chance and flat critical damage.

| Name | Rarity | Base Damage Boost | Critical Chance Boost | Flat Critical Damage | Cost |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Damage Amp 1** | Shoddy | +10 | +5% | +5 | 10,000 Credits |
| **Arc Amp** | Uncommon | +16 | +5% | +8 | 60,000 Credits |
| **Pulse Amp** | Rare | +26 | +6% | +13 | 1,500 Thulium |
| **Nova Amp** | Epic | +38 | +7% | +20 | Craftable Only |
| **Crit Amp 1** | Shoddy | +0 | +15% | +0 | 15,000 Credits |
| **Focus Amp** | Uncommon | +0 | +20% | +14 | 60,000 Credits |
| **Prism Amp** | Rare | +0 | +25% | +24 | 1,500 Thulium |
| **Apex Amp** | Epic | +0 | +25% | +44 | Craftable Only |

The Nova Amp and the Apex Amp are made in [Assembly](/wiki/06-Items/Overview.md#upgrading-modules) from a Pulse Amp and a Prism Amp, with Thulium, drops and 3 Velkonite Reinforced Plates from your Skylab each. They keep the enchant tier of the amp they use up, and their buffs are rolled again ([Module upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)).

### Which amp goes where

A damage amp adds the same damage to any laser, so it is worth the most on the **Quantum lasers**. A crit amp multiplies what the laser already does, so it is worth more the harder the laser hits: it draws level with the damage line on the **Starfire-3** and comes out about 3.5% ahead on the **Helios Beam**. A laser's critical chance stops at 100%: three Prism Amps or Apex Amps take a Helios Beam to exactly that.

Filled with the same amp, a laser is always stronger than the one below it, so a better amp never replaces a better laser: a Quantum Laser 3 with three Nova Amps does less than a Helios Beam with three Damage Amp 1 (with pieces of the same enchant tier: a Quantum Laser 3 and Nova Amps forged to Godly or better, with the best rolls, can pass a plain Helios Beam in Damage Amp 1, by a hair at Godly).

---

## Laser Ammunition

Consumable batteries that multiply the damage of your laser volleys:

| Name | Rarity | Damage Multiplier | Shield Penetration | Price Per Unit |
| :--- | :--- | :---: | :---: | :--- |
| **Standard Battery** | Common | 1.0x | – | 10 Credits |
| **Advanced Plasma** | Rare | 2.0x | – | 0.5 Thulium |
| **Ultra Core** | Rare | 3.0x | 5% | 1.0 Thulium |
| **Experimental Fusion Core** | Epic | 4.0x | 10% | 2.2 Thulium |
| **Siphon Battery** | Rare | 1.0x, shields only | – | 0.25 Thulium |

**Shield penetration** is taken off your target's absorbance for every hit of your volleys: the shields take the target's absorbance less the penetration (see [Shield Mechanics](/wiki/03-Mechanics/Shields.md#shield-penetration)). Against a ship at 80% (the best shield with the best cells) the x4 ammo's 10% leaves the shields 70% of the hit and the hull 30%. It matters most against ships whose hull is small next to their shield; a very large ship at 80% holds up the same either way. Aliens have no absorbance stat to speak of (their shields take 80% of a hit), and the penetration comes off that too.

### Siphon Battery

The Siphon Battery is ammo for stealing shields instead of breaking hulls. It deals **x1 damage directly to the target's shield** and adds the same amount to **your own shield**, up to your maximum. Choose it on the hotbar's ammo picker like any other ammo (it is the tile with the teal vortex). It does not fire a beam: a thin, faint teal probe goes out to the target, the target's shield flares teal where it lands, and the shield you drained visibly streams back to your ship as glowing teal packets (three to ten, more for a bigger drain), one after another over about half a second. Each packet that arrives pulses your shield. You see the same for every pilot's Siphon Battery that is in view, whoever it drains: aliens, other pilots and company pilots' ships.

- **Shield only**: the hull is never touched, the target's absorbance doesn't split the damage, and a Siphon Battery can never destroy anything. Its damage is capped by what the target's shield still holds.
- **Nothing to take**: against a target with no shield left it drains and gives nothing. The volley is still spent, one battery per laser, as with every ammo. You see only the probe and a dull flicker on the hull, and no packets.
- **Gain**: your shield never goes above its maximum, and taking shield in doesn't delay your own shield regeneration.
- **Aliens and pilots** alike have shields to drain. A drain that takes shield from an alien counts as a hit for the [first-hit claim](/wiki/03-Mechanics/Combat.md); one that finds no shield doesn't. It also wakes a Seeker or a Goombah, which only fight back, like any other hit.
- **Critical hits** count: a critical volley drains 1.5 times as much, and its number is drawn as a critical hit. Its packets are bigger and brighter, and the target's shield flares harder.
- [Company pilots](/wiki/03-Mechanics/Company-Pilots.md) fire standard x1 ammo.
