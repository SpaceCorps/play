# Propulsion & Speed

Propulsion systems determine your ship's movement velocity and maneuverability.

## In one minute

- **Engines make speed, thrusters sit inside them and add to it.** An engine holds one to three thrusters (an Engine I one, an Engine II two, an Engine III three), and so does an Adaptive Core (its tier says how many).
- **Two families, four tiers each.** Impulse Thrusters add the most flat speed. Momentum Thrusters add less flat speed and multiply the speed more. In both families every tier is better than the one below it, in both numbers.
- **Which one where.** As a rule, put Momentum Thrusters in a full Engine III (three thrusters) and Impulse Thrusters in an Adaptive Core; in the smaller engines the two are close at tiers I and II and Impulse leads from tier III on. [The table below](#which-thruster-where) has the numbers. The fastest Engine III holds three Momentum Thruster IVs and makes 63.3.
- **Getting them.** Tier I of each family costs 20,000 Credits. Tiers II to IV are made in Assembly, each from the tier below, and a thruster never changes family.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Item tree

What Assembly makes needs its technology first; point at an item to see how long it takes to research. The technology tree, the fuel and the boost: [Research](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Engine I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 4000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 80 Ship Fragment, 4 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 80 Ship Fragment, 4 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 4000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 4000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I => Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Engines

Engines are the primary source of thrust for your ship. An engine in an **ability slot** instead gives you the **Afterburner** in the Special Effect column, a burst of speed for fifteen seconds (longer with more engines), and adds no thrust of its own (see [Abilities](/wiki/03-Mechanics/Abilities.md)).

| Name | Rarity | Base Speed | Speed Bonus % | Shield Bonus % | Slots | Special Effect | Cost |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Shoddy | +5 | +2% | -2% | 1 | Afterburner I | 20,000 Credits |
| **Engine II** | Common | +10 | +3% | -8% | 2 | Afterburner II | Craftable Only |
| **Engine III** | Rare | +15 | +4% | -15% | 3 | Afterburner III | Craftable Only |

The **Engine II** is made in [Assembly](/wiki/06-Items/Overview.md#upgrading-modules) from an Engine I, with 2,000 Thulium, 60 Ship Fragments, 1 Power Core and 4 Velkonite Reinforced Plates. The **Engine III** is made there from an Engine II, with 4,000 Thulium, 110 Ship Fragments, 5 Power Cores, 1 Ancient Control Unit and 4 Dark Matter Plates ([Dark Matter and Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)). Each keeps the enchant tier and the buffs of the engine it uses up ([Module upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Take the engine you use up off your ship (and its thrusters out of it) first: an engine that is fitted or holds thrusters is not used up.

The engines' Shield Bonus is in the item data, but the game has never applied it: engines don't weaken your shields, and the item cards leave it out.

---

## Thrusters

Thrusters are nested inside Engines or Adaptive Cores to boost their speed output. There are two families of four tiers each: the **Impulse Thrusters** add the most flat speed and multiply the speed of the engine they sit in a little, the **Momentum Thrusters** add less flat speed and multiply it more. In both families every tier is better than the one below it, in the flat speed and in the multiplier. An engine (or Adaptive Core) with thrusters makes **its own Base Speed plus the thrusters' Flat Speed Boosts, all of it times the thrusters' Speed Multipliers multiplied together** ([how speed is calculated](/wiki/03-Mechanics/Speed.md)): an Engine III with three Momentum Thruster IVs makes (15 + 3 x 11.135) x 1.0935 x 1.0935 x 1.0935 = 63.3, with three Impulse Thruster IVs (15 + 3 x 14.025) x 1.02975 x 1.02975 x 1.02975 = 62.3, and an Adaptive Core II with two Impulse Thruster IVs makes (0 + 2 x 14.025) x 1.02975 x 1.02975 = 29.7 (26.6 with two Momentum Thruster IVs).

| Name | Rarity | Flat Speed Boost | Speed Multiplier | Cost |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Shoddy | +4.25 | 1.017x | 20,000 Credits |
| **Impulse Thruster II** | Common | +8.5 | 1.02125x | Craftable Only |
| **Impulse Thruster III** | Rare | +12.75 | 1.0255x | Craftable Only |
| **Impulse Thruster IV** | Epic | +14.025 | 1.02975x | Craftable Only |
| **Momentum Thruster I** | Shoddy | +3.825 | 1.051x | 20,000 Credits |
| **Momentum Thruster II** | Common | +7.65 | 1.0595x | Craftable Only |
| **Momentum Thruster III** | Rare | +10.625 | 1.0765x | Craftable Only |
| **Momentum Thruster IV** | Epic | +11.135 | 1.0935x | Craftable Only |

### Which thruster where

Impulse adds more flat speed, Momentum multiplies more, so which is faster depends on what the engine already makes. Flat speed counts most where there is little speed to multiply: in an Adaptive Core (it has no speed of its own) and in an engine with one or two thrusters. A multiplier counts most in a full Engine III, where there is a lot of speed to multiply, and the Momentum Thrusters win there at every tier. The speed each makes with its tier IV thrusters in every socket:

| Where the thrusters sit | With Impulse Thruster IV | With Momentum Thruster IV | Faster |
| :--- | :---: | :---: | :--- |
| Engine I, one thruster | 19.6 | 17.6 | Impulse |
| Engine II, two thrusters | 40.3 | 38.6 | Impulse |
| Engine III, one thruster | 29.9 | 28.6 | Impulse |
| Engine III, two thrusters | 45.6 | 44.6 | Impulse |
| Engine III, three thrusters | 62.3 | 63.3 | Momentum |
| Adaptive Core II, two thrusters | 29.7 | 26.6 | Impulse |

- **Lower tiers.** From tier III on Impulse leads in every host but the full Engine III, by 0.6 to 3.1. At tiers I and II the two families are less than a point apart outside the full Engine III: Impulse is ahead in an Engine I and in an Adaptive Core I or II, Momentum is ahead or level in an Engine III with one or two thrusters and in an Engine II with two. The exception is the full Engine III: Momentum leads there at every tier, by 1.0 to 2.0.
- **The fastest Engine III.** It holds three Momentum Thruster IVs: 63.3, a little above one Impulse and two Momentum Thruster IVs (63.2) or three Impulse (62.3).

A thruster's Speed Multiplier buff from the [Forge](/wiki/06-Items/Forge.md) grows the part above 1 (a +15% buff on 1.0935x makes 1.1075x), and the Forge rolls no buff on a multiplier of 1.05x or less: on an Impulse Thruster's 1.017x to 1.02975x it would add under 0.005 (+15% on 1.02975x makes 1.034x). An Impulse Thruster holds one buff (its flat speed), a Momentum Thruster two.

Tier I of each family is sold for 20,000 Credits. Tiers II to IV are made in [Assembly](/wiki/06-Items/Overview.md#upgrading-modules), each from the thruster of the same family one tier below (an Impulse Thruster II from an Impulse Thruster I, a III from a II, a IV from a III), with Thulium, drops and plates: 4 Velkonite Reinforced Plates from your Skylab for tier II or III, and 4 Dark Matter Plates and an Ancient Control Unit for tier IV. A thruster never changes family: you choose Impulse or Momentum when you buy tier I. Each keeps the enchant tier and the buffs of the thruster it uses up ([Module upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Thrusters don't fit an [ability slot](/wiki/03-Mechanics/Abilities.md); they belong inside engines and Adaptive Cores.

### Outrunning aliens

The aliens fly at 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) and 230 (Crystalys). An Ostirion (base speed 220) with one Engine II and two thrusters flies at 246.3 with Impulse Thruster I, 255.6 with II, 265.1 with III and 268.2 with IV: every tier outruns the Crystalys, even the Impulse Thruster I you can buy. The Momentum Thrusters fly within two points of that (246.7 with a Momentum Thruster I, then 255.9, 263.9 and 266.3 with II to IV): every tier of either family is over a Crystalys, by at least 16.3.
