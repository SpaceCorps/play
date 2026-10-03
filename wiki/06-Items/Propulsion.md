# Propulsion & Speed

Propulsion systems determine your ship's movement velocity and maneuverability.

## Engines

Engines are the primary source of thrust for your ship. An engine in an **ability slot** instead gives you the **Afterburner** in the Special Effect column, a burst of speed for ten seconds (longer with more engines), and adds no thrust of its own (see [Abilities](/wiki/03-Mechanics/Abilities.md)).

| Name | Rarity | Base Speed | Speed Bonus % | Shield Bonus % | Slots | Special Effect | Cost |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Shoddy | +2 | +2% | -2% | 1 | Afterburner I | 20,000 Credits |
| **Engine II** | Common | +4 | +4% | -8% | 2 | Afterburner II | 2,000 Thulium |
| **Engine III** | Rare | +6 | +5% | -15% | 3 | Afterburner III | Craftable Only |

The **Engine III** is made in [Assembly](/wiki/06-Items/Overview.md#upgrading-modules) from an Engine II, with 2,000 Thulium, 60 Ship Fragments, 3 Power Cores and 6 Velkonite Reinforced Plates from your Skylab. It keeps the enchant tier of the engine it uses up, and its buffs are rolled again ([Module upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Take the Engine II off your ship (and its thrusters out of it) first: an engine that is fitted or holds thrusters is not used up.

The engines' Shield Bonus is in the item data, but the game has never applied it: engines don't weaken your shields, and the item cards leave it out.

---

## Thrusters

Thrusters are nested inside Engines or Adaptive Cores to boost their speed output. There are two families of four tiers each: the **Impulse Thrusters** add the most flat speed and multiply the speed of the engine they sit in a little, the **Momentum Thrusters** add less flat speed and multiply it more. An engine (or Adaptive Core) with thrusters makes **its own Base Speed plus the thrusters' Flat Speed Boosts, all of it times the thrusters' Speed Multipliers multiplied together** ([how speed is calculated](/wiki/03-Mechanics/Speed.md)): an Engine III with three Momentum Thruster IVs makes (6 + 3 x 12) x 1.14 x 1.14 x 1.14 = 62.2, with three Impulse Thruster IVs (6 + 3 x 17) x 1.02 x 1.02 x 1.02 = 60.5, and an Adaptive Core II with two Impulse Thruster IVs makes (0 + 2 x 17) x 1.02 x 1.02 = 35.4 (31.2 with two Momentum Thruster IVs).

| Name | Rarity | Flat Speed Boost | Speed Multiplier | Cost |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Shoddy | +5 | 1.02x | 20,000 Credits |
| **Impulse Thruster II** | Common | +10 | 1.02x | Craftable Only |
| **Impulse Thruster III** | Rare | +15 | 1.03x | Craftable Only |
| **Impulse Thruster IV** | Epic | +17 | 1.02x | Craftable Only |
| **Momentum Thruster I** | Shoddy | +4 | 1.08x | 20,000 Credits |
| **Momentum Thruster II** | Common | +8 | 1.10x | Craftable Only |
| **Momentum Thruster III** | Rare | +11 | 1.13x | Craftable Only |
| **Momentum Thruster IV** | Epic | +12 | 1.14x | Craftable Only |

Which family is faster depends on where it sits. The Impulse Thrusters make more in an Adaptive Core and in an engine with one or two thrusters in it; the Momentum Thrusters of the same tier make more in an Engine III with all three sockets filled (62.2 against 60.5 at tier IV, and one Impulse Thruster IV with two Momentum Thruster IVs, 62.3, is the best an Engine III can be).

A thruster's Speed Multiplier buff from the [Forge](/wiki/06-Items/Forge.md) grows the part above 1 (a +15% buff on 1.14x makes 1.161x), and the Forge rolls no buff on a multiplier of 1.05x or less: on an Impulse Thruster's 1.02x or 1.03x it would be worth a thousandth. An Impulse Thruster holds one buff (its flat speed), a Momentum Thruster two.

Tier I of each family is sold for 20,000 Credits. Tiers II to IV are made in [Assembly](/wiki/06-Items/Overview.md#upgrading-modules), each from the thruster of the same family one tier below (an Impulse Thruster II from an Impulse Thruster I, a III from a II, a IV from a III), with Thulium, drops and Velkonite Reinforced Plates from your Skylab (2, 4 and 6 plates). A thruster never changes family: you choose Impulse or Momentum when you buy tier I. Each keeps the enchant tier of the thruster it uses up, and its buffs are rolled again ([Module upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Thrusters don't fit an [ability slot](/wiki/03-Mechanics/Abilities.md); they belong inside engines and Adaptive Cores.

### Outrunning aliens

The aliens fly at 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) and 230 (Crystalys). An Ostirion with one Engine II and two thrusters flies at 223.1 with Impulse Thruster I: still under the Crystalys, so it takes a thruster made in Assembly to outrun it (234.0 with Impulse Thruster II, 245.5 with III, 249.1 with IV). The Momentum Thrusters fly a little lower on that ship (222.6 with a Momentum Thruster I, 233.2, 242.5 and 245.8 with II to IV): tier I of either family is under a Crystalys, and every tier made in Assembly is over it.
