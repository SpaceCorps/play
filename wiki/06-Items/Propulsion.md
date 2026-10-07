# Propulsion & Speed

Propulsion systems determine your ship's movement velocity and maneuverability.

## In one minute

- **Engines make speed, thrusters sit inside them and add to it.** An engine holds one to three thrusters (an Engine I one, an Engine II two, an Engine III three), and so does an Adaptive Core (its tier says how many).
- **Two families, four tiers each.** Impulse Thrusters add the most flat speed. Momentum Thrusters add less flat speed and multiply the speed more. In both families every tier is better than the one below it, in both numbers.
- **Which one where.** As a rule, Momentum goes in a full Engine III (three thrusters) and Impulse everywhere else: [the table below](#which-thruster-where) has the numbers. The fastest Engine III mixes them: one Impulse Thruster IV and two Momentum Thruster IVs make 62.1.
- **Getting them.** Tier I of each family costs 20,000 Credits. Tiers II to IV are made in Assembly, each from the tier below, and a thruster never changes family.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Item tree

What Assembly makes needs its technology first; point at an item to see how long it takes to research. The technology tree, the fuel and the boost: [Research](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | buy 2000 Thulium | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I -> Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Engines

Engines are the primary source of thrust for your ship. An engine in an **ability slot** instead gives you the **Afterburner** in the Special Effect column, a burst of speed for ten seconds (longer with more engines), and adds no thrust of its own (see [Abilities](/wiki/03-Mechanics/Abilities.md)).

| Name | Rarity | Base Speed | Speed Bonus % | Shield Bonus % | Slots | Special Effect | Cost |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Shoddy | +2 | +2% | -2% | 1 | Afterburner I | 20,000 Credits |
| **Engine II** | Common | +4 | +4% | -8% | 2 | Afterburner II | 2,000 Thulium |
| **Engine III** | Rare | +6 | +5% | -15% | 3 | Afterburner III | Craftable Only |

The **Engine III** is made in [Assembly](/wiki/06-Items/Overview.md#upgrading-modules) from an Engine II, with 2,000 Thulium, 60 Ship Fragments, 3 Power Cores and 3 Dark Matter Plates ([Dark Matter and Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)). It keeps the enchant tier of the engine it uses up, and its buffs are rolled again ([Module upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Take the Engine II off your ship (and its thrusters out of it) first: an engine that is fitted or holds thrusters is not used up.

The engines' Shield Bonus is in the item data, but the game has never applied it: engines don't weaken your shields, and the item cards leave it out.

---

## Thrusters

Thrusters are nested inside Engines or Adaptive Cores to boost their speed output. There are two families of four tiers each: the **Impulse Thrusters** add the most flat speed and multiply the speed of the engine they sit in a little, the **Momentum Thrusters** add less flat speed and multiply it more. In both families every tier is better than the one below it, in the flat speed and in the multiplier. An engine (or Adaptive Core) with thrusters makes **its own Base Speed plus the thrusters' Flat Speed Boosts, all of it times the thrusters' Speed Multipliers multiplied together** ([how speed is calculated](/wiki/03-Mechanics/Speed.md)): an Engine III with three Momentum Thruster IVs makes (6 + 3 x 13.1) x 1.11 x 1.11 x 1.11 = 62.0, with three Impulse Thruster IVs (6 + 3 x 16.5) x 1.035 x 1.035 x 1.035 = 61.5, and an Adaptive Core II with two Impulse Thruster IVs makes (0 + 2 x 16.5) x 1.035 x 1.035 = 35.4 (32.3 with two Momentum Thruster IVs).

| Name | Rarity | Flat Speed Boost | Speed Multiplier | Cost |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Shoddy | +5 | 1.02x | 20,000 Credits |
| **Impulse Thruster II** | Common | +10 | 1.025x | Craftable Only |
| **Impulse Thruster III** | Rare | +15 | 1.03x | Craftable Only |
| **Impulse Thruster IV** | Epic | +16.5 | 1.035x | Craftable Only |
| **Momentum Thruster I** | Shoddy | +4.5 | 1.06x | 20,000 Credits |
| **Momentum Thruster II** | Common | +9 | 1.07x | Craftable Only |
| **Momentum Thruster III** | Rare | +12.5 | 1.09x | Craftable Only |
| **Momentum Thruster IV** | Epic | +13.1 | 1.11x | Craftable Only |

### Which thruster where

Impulse adds more flat speed, Momentum multiplies more, so which is faster depends on what the engine already makes. Flat speed counts most where there is little speed to multiply: in an Adaptive Core (it has no speed of its own) and in an engine with one or two thrusters. A multiplier counts most in a full Engine III, where there is a lot of speed to multiply. The speed each makes with its tier IV thrusters in every socket:

| Where the thrusters sit | With Impulse Thruster IV | With Momentum Thruster IV | Faster |
| :--- | :---: | :---: | :--- |
| Engine I, one thruster | 19.1 | 16.8 | Impulse |
| Engine II, two thrusters | 39.6 | 37.2 | Impulse |
| Engine III, one thruster | 23.3 | 21.2 | Impulse |
| Engine III, two thrusters | 41.8 | 39.7 | Impulse |
| Engine III, three thrusters | 61.5 | 62.0 | Momentum |
| Adaptive Core II, two thrusters | 35.4 | 32.3 | Impulse |

- **Lower tiers.** Tiers I to III go the same way, with two close calls. With two thrusters in an Engine II the families are level at tiers I and II (within 0.05), and with two in an Engine III Momentum is ahead by about 0.2 at tiers I and II. From tier III on Impulse leads in both, by 1.4 to 2.4. In a full Engine III Momentum leads at every tier, by 0.4 to 1.7.
- **Mix them in an Engine III.** The fastest Engine III holds one Impulse Thruster IV and two Momentum Thruster IVs: (6 + 16.5 + 2 x 13.1) x 1.035 x 1.11 x 1.11 = 62.1, a little above three Momentum (62.0) or three Impulse (61.5).

A thruster's Speed Multiplier buff from the [Forge](/wiki/06-Items/Forge.md) grows the part above 1 (a +15% buff on 1.11x makes 1.1265x), and the Forge rolls no buff on a multiplier of 1.05x or less: on an Impulse Thruster's 1.02x to 1.035x it would add under 0.006 (+15% on 1.035x makes 1.040x). An Impulse Thruster holds one buff (its flat speed), a Momentum Thruster two.

Tier I of each family is sold for 20,000 Credits. Tiers II to IV are made in [Assembly](/wiki/06-Items/Overview.md#upgrading-modules), each from the thruster of the same family one tier below (an Impulse Thruster II from an Impulse Thruster I, a III from a II, a IV from a III), with Thulium, drops and plates: 2 or 4 Velkonite Reinforced Plates from your Skylab for tier II or III, and 3 Dark Matter Plates for tier IV. A thruster never changes family: you choose Impulse or Momentum when you buy tier I. Each keeps the enchant tier of the thruster it uses up, and its buffs are rolled again ([Module upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Thrusters don't fit an [ability slot](/wiki/03-Mechanics/Abilities.md); they belong inside engines and Adaptive Cores.

### Outrunning aliens

The aliens fly at 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) and 230 (Crystalys). An Ostirion with one Engine II and two thrusters flies at 223.1 with Impulse Thruster I: still under the Crystalys, so it takes a thruster made in Assembly to outrun it (234.2 with Impulse Thruster II, 245.5 with III, 249.2 with IV). The Momentum Thrusters fly the same or a little lower on that ship (223.2 with a Momentum Thruster I, then 234.2, 243.8 and 246.7 with II to IV): tier I of either family is under a Crystalys, and every tier made in Assembly is over it.
