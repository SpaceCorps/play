# Propulsion & Speed

Propulsion systems determine your ship's movement velocity and maneuverability.

## In one minute

- **Engines make speed, thrusters sit inside them and add to it.** An engine holds one to three thrusters (an Engine I one, an Engine II two, an Engine III three), and so does an Adaptive Core (its tier says how many).
- **Two families, four tiers each.** Impulse Thrusters add the most flat speed. Momentum Thrusters add less flat speed and multiply the speed more. In both families every tier is better than the one below it, in both numbers.
- **Which one where.** As a rule, put Impulse Thrusters everywhere: only in a full Engine III (three thrusters) do the Momentum Thrusters of tiers I and II come out ahead. [The table below](#which-thruster-where) has the numbers. The fastest Engine III holds three Impulse Thruster IVs and makes 52.5.
- **Getting them.** Tier I of each family costs 20,000 Credits. Tiers II to IV are made in Assembly, each from the tier below, and a thruster never changes family.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Item tree

What Assembly makes needs its technology first; point at an item to see how long it takes to research. The technology tree, the fuel and the boost: [Research](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Engine I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I => Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Engines

Engines are the primary source of thrust for your ship. An engine in an **ability slot** instead gives you the **Afterburner** in the Special Effect column, a burst of speed for ten seconds (longer with more engines), and adds no thrust of its own (see [Abilities](/wiki/03-Mechanics/Abilities.md)).

| Name | Rarity | Base Speed | Speed Bonus % | Shield Bonus % | Slots | Special Effect | Cost |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Shoddy | +2 | +2% | -2% | 1 | Afterburner I | 20,000 Credits |
| **Engine II** | Common | +4 | +4% | -8% | 2 | Afterburner II | Craftable Only |
| **Engine III** | Rare | +6 | +5% | -15% | 3 | Afterburner III | Craftable Only |

The **Engine II** is made in [Assembly](/wiki/06-Items/Overview.md#upgrading-modules) from an Engine I, with 1,000 Thulium, 10 Ship Fragments, 1 Power Core and 2 Velkonite Reinforced Plates. The **Engine III** is made there from an Engine II, with 2,000 Thulium, 60 Ship Fragments, 3 Power Cores and 3 Dark Matter Plates ([Dark Matter and Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)). Each keeps the enchant tier of the engine it uses up, and its buffs are rolled again ([Module upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Take the engine you use up off your ship (and its thrusters out of it) first: an engine that is fitted or holds thrusters is not used up.

The engines' Shield Bonus is in the item data, but the game has never applied it: engines don't weaken your shields, and the item cards leave it out.

---

## Thrusters

Thrusters are nested inside Engines or Adaptive Cores to boost their speed output. There are two families of four tiers each: the **Impulse Thrusters** add the most flat speed and multiply the speed of the engine they sit in a little, the **Momentum Thrusters** add less flat speed and multiply it more. In both families every tier is better than the one below it, in the flat speed and in the multiplier. An engine (or Adaptive Core) with thrusters makes **its own Base Speed plus the thrusters' Flat Speed Boosts, all of it times the thrusters' Speed Multipliers multiplied together** ([how speed is calculated](/wiki/03-Mechanics/Speed.md)): an Engine III with three Momentum Thruster IVs makes (6 + 3 x 11.135) x 1.0935 x 1.0935 x 1.0935 = 51.5, with three Impulse Thruster IVs (6 + 3 x 14.025) x 1.02975 x 1.02975 x 1.02975 = 52.5, and an Adaptive Core II with two Impulse Thruster IVs makes (0 + 2 x 14.025) x 1.02975 x 1.02975 = 29.7 (26.6 with two Momentum Thruster IVs).

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

Impulse adds more flat speed, Momentum multiplies more, so which is faster depends on what the engine already makes. Flat speed counts most where there is little speed to multiply: in an Adaptive Core (it has no speed of its own) and in an engine with one or two thrusters. A multiplier counts most in a full Engine III, where there is a lot of speed to multiply, but only the Momentum Thrusters of tiers I and II win there. The speed each makes with its tier IV thrusters in every socket:

| Where the thrusters sit | With Impulse Thruster IV | With Momentum Thruster IV | Faster |
| :--- | :---: | :---: | :--- |
| Engine I, one thruster | 16.5 | 14.4 | Impulse |
| Engine II, two thrusters | 34.0 | 31.4 | Impulse |
| Engine III, one thruster | 20.6 | 18.7 | Impulse |
| Engine III, two thrusters | 36.1 | 33.8 | Impulse |
| Engine III, three thrusters | 52.5 | 51.5 | Impulse |
| Adaptive Core II, two thrusters | 29.7 | 26.6 | Impulse |

- **Lower tiers.** The lower tiers go the same way, with two close calls and one exception. With two thrusters in an Engine II the families are level at tiers I and II (Impulse ahead by 0.06 and 0.24), and with two in an Engine III they are level too (within 0.1). From tier III on Impulse leads in both, by 1.5 to 2.6. The exception is the full Engine III: Momentum leads there at tiers I and II, by 0.6 and 0.9, and Impulse at tiers III and IV, by 0.5 and 1.0.
- **The fastest Engine III.** It holds three Impulse Thruster IVs: 52.5, a little above one Impulse and two Momentum Thruster IVs (52.1) or three Momentum (51.5).

A thruster's Speed Multiplier buff from the [Forge](/wiki/06-Items/Forge.md) grows the part above 1 (a +15% buff on 1.0935x makes 1.1075x), and the Forge rolls no buff on a multiplier of 1.05x or less: on an Impulse Thruster's 1.017x to 1.02975x it would add under 0.005 (+15% on 1.02975x makes 1.034x). An Impulse Thruster holds one buff (its flat speed), a Momentum Thruster two.

Tier I of each family is sold for 20,000 Credits. Tiers II to IV are made in [Assembly](/wiki/06-Items/Overview.md#upgrading-modules), each from the thruster of the same family one tier below (an Impulse Thruster II from an Impulse Thruster I, a III from a II, a IV from a III), with Thulium, drops and plates: 2 or 4 Velkonite Reinforced Plates from your Skylab for tier II or III, and 3 Dark Matter Plates for tier IV. A thruster never changes family: you choose Impulse or Momentum when you buy tier I. Each keeps the enchant tier of the thruster it uses up, and its buffs are rolled again ([Module upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Thrusters don't fit an [ability slot](/wiki/03-Mechanics/Abilities.md); they belong inside engines and Adaptive Cores.

### Outrunning aliens

The aliens fly at 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) and 230 (Crystalys). An Ostirion with one Engine II and two thrusters flies at 221.4 with Impulse Thruster I: still under the Crystalys, so it takes a thruster made in Assembly to outrun it (230.8 with Impulse Thruster II, 240.3 with III, 243.3 with IV). The Momentum Thrusters fly the same or a little lower on that ship (221.4 with a Momentum Thruster I, then 230.5, 238.4 and 240.7 with II to IV): tier I of either family is under a Crystalys, and every tier made in Assembly is over it, tier II by only 0.8 and 0.5.
