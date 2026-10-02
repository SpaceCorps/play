# The Forge

The **Forge** is the second tab of the Assembly page (and of the Assembly window in flight). It does two things with equipment you own: it **raises an item one tier** for credits and alien drops, and it **merges two copies** of an item into one that keeps the best of both. It replaced the old Fusion Chamber, which needed five identical items and left the result to a 25% roll.

## What can be forged

Lasers, Laser Amps, Shield Cores, Shield Cells, Engines, Thrusters, Adaptive Cores and Repair Drones: any single piece of equipment that can carry [enchant buffs](/wiki/05-Items/Overview.md). It can be in your inventory, on a ship (it stays there and works with its new tier at once) or fitted into another item. Drones, ships, ammo, resources and boosters can't be forged, and neither can anything in the Transport Cache: take it out first.

## Tier up

Pick an item and the panel shows its tier, the tier it would reach, what that changes (how many buffs it can hold and how big they are), and the price with what you have of each part: green when you have enough, red when you don't, and how many you are short. When you have it all, **Tier up** raises the item by exactly one tier. There is no jump: to reach Eternal an item goes through Tainted, Godly and Rupturing, each with its own price.

| Step | Success | Credits | Thulium | Materials |
| :--- | :---: | :---: | :---: | :--- |
| Standard to Tainted | 100% | 10,000 | – | 5 Ship Fragment, 15 Daraxium |
| Tainted to Godly | 90% | 50,000 | – | 30 Ship Fragment, 45 Nyxite |
| Godly to Rupturing | 75% | 200,000 | – | 20 Reinforced Hull Plate, 120 Cataclysite, 2 Dark Matter Plate |
| Rupturing to Eternal | 60% | 500,000 | 2,000 | 8 Power Core, 240 Quorvium, 2 Dark Matter Plate |

- **Materials** come from your loose stacks: items on a ship and stacks in the Transport Cache are not used. The panel tells you when the missing ones are in the cache.
- **A step can fail.** The item stays exactly as it was, the credits are gone, and half of the materials and half of the Thulium come back (rounded down; of two Dark Matter Plates, one). The panel says the chance and this before you press.
- **On success** each buff the item has is rolled again in the new tier's range and keeps the better value, and the tier's extra buff slots get new buffs on other stats of the item. The result is shown above the panel; the item stays selected, so its next step is already on screen.
- A tier-up is instant.

### Dark Matter Plates

The last two steps ask for **2 Dark Matter Plates** each, on top of everything else. A plate is pressed in [Assembly](/wiki/05-Items/Overview.md) from **5 Dark Matter, 1 Velkonite Reinforced Plate and 1 Orvium Reinforced Plate** (250 Thulium, 2 minutes), so one step takes 10 Dark Matter, 2 Velkonite plates and 2 Orvium plates. Dark Matter comes from the [black hole](/wiki/03-Mechanics/Black-Hole.md): about five N.I.K.E. rockets (see [Rockets](/wiki/05-Items/Rockets.md)) make ten; a N.I.K.E. that meets a ship on its way hits that ship instead and makes none. The plates are used from your loose stacks like the other materials, and the panel names them if you are short.

### Buffs by tier

| Tier | Buffs held at most | Size of each buff |
| :--- | :---: | :---: |
| Tainted | 1 | +2% to +5% |
| Godly | 2 | +4% to +8% |
| Rupturing | 3 | +6% to +11% |
| Eternal | 4 | +9% to +15% |

Equipment made before the Forge keeps the buffs it was rolled with, and those are often smaller than the table (a Godly piece from back then can hold +2%). Nothing raises them by itself: a tier-up rolls each buff again in the new tier's range and keeps the better value, and a merge keeps the better value of each stat.

An item can't hold more buffs than it has stats: a Shield Core has four, a laser three (the Quantum Laser 1 and 2 have two), an engine, a thruster or an Adaptive Core two, a Crit Amp 1 or a Repair Drone one, the higher crit amps two, the damage amps and shield cells three. When the next tier holds no more buffs than the item can carry, the panel says so: the tier then only makes the buffs stronger. Range buffs never pass +5%.

A **shield's Absorbance buff** (and a shield cell's Absorbance Boost) multiplies the stat, so it is worth points of [absorbance](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-) in proportion to it: +5% on a Heavy Shield Core's 50% is +2.5 points, and +15% on every piece of the best set (a Heavy Shield Core and three Sovereign cells, 80% in all) is +12 points. An Eternal set takes between +7 and +12 points, about 10 on average; with the Season Store's Shield Absorbance Boost (+10 points at its limit; the Wipe Points of the whole game buy 34 of its 100 levels, +3.4 points) that takes a ship to 95%, and past 100% only with the buff's limit, which the stat allows: an attacker's shield penetration is taken off it. A Godly set takes between 3 and 6 points.

Engines, thrusters, Adaptive Cores and Repair Drones move very little with a percentage buff (an Engine II adds 4 speed, so +12% is half a point): forge them if you want the tier, not for the stats.

### Where the materials drop

| Material | Dropped by |
| :--- | :--- |
| **Ship Fragment** | every alien |
| **Daraxium** | [Seeker](/wiki/04-Aliens/Seeker.md), [Phantasm](/wiki/04-Aliens/Phantasm.md) |
| **Nyxite** | [Phantasm](/wiki/04-Aliens/Phantasm.md), [Bulwark](/wiki/04-Aliens/Bulwark.md) |
| **Reinforced Hull Plate** | [Bulwark](/wiki/04-Aliens/Bulwark.md), [Gorvane](/wiki/04-Aliens/Gorvane.md) |
| **Cataclysite** | [Bulwark](/wiki/04-Aliens/Bulwark.md), [Gorvane](/wiki/04-Aliens/Gorvane.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Power Core** | [Gorvane](/wiki/04-Aliens/Gorvane.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Quorvium** | [Gorvane](/wiki/04-Aliens/Gorvane.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Dark Matter Plate** | no alien: Assembly presses it from Dark Matter (the [black hole](/wiki/03-Mechanics/Black-Hole.md)) and the Skylab's plates |

The crystals follow the tiers: Daraxium is blue like Tainted, Nyxite yellow like Godly, Cataclysite orange like Rupturing and Quorvium violet like Eternal. Every source, with the chances and amounts, is on the [Resources](/wiki/05-Items/Resources.md) page and on each alien's page; the Resource Magnet booster adds 25% to what a crate holds.

## Merge

Two copies of the same item (two Light Shield Cores, two Quantum Laser 2s) become one. Switch to **Merge** and click the item you want to keep (the **base**), then a second copy (the **donor**). The panel shows the result before you confirm.

- **The base is kept.** It keeps its place: it may be on a ship, or fitted into another item, and the modules fitted into it stay. **The donor is used up.** It must be loose (not on a ship, not fitted), and the modules fitted into it go back to your inventory.
- **The result has the higher of the two tiers**, and for each stat the **better of the two values**.
- **It never holds more buffs than its tier allows.** If the two items together have more buffs than the result's tier can hold, the best ones are kept and the rest are dropped; the table marks them (struck through, "over the limit"). To hold more buffs, tier the item up first. A merge never rolls anything: what the preview shows is what you get.
- **A merge costs credits by the tier it makes**: 5,000 for Tainted, 25,000 for Godly, 100,000 for Rupturing, 250,000 for Eternal. No materials.
- A merge that would change nothing (the result is no better than the base) is refused.
- After a merge the result stays selected and the donor slot is empty: put the next donor in, or switch back to Tier up.

A merge polishes an item; it doesn't multiply it. Two Godly Shield Cores merged are worth about a point and a half of buffs more than one. Its use is choosing: a Godly core with the stats you want, or a tier moved onto the item on your ship without taking it off.

## Module upgrades in the Assembly

The top laser, laser amps, shield cell and thruster are not sold. You make them in the Assembly's **Crafting** tab by upgrading the piece one step below: a Pulse Amp into a **Nova Amp**, a Prism Amp into an **Apex Amp**, a Prime Shield Cell into a **Sovereign Shield Cell**, an Ion Thruster into a **Plasma Thruster**, and a Starfire-3 into a **Helios Beam**. What the Forge has to do with it is the tier.

- **The tier stays.** An upgrade uses up one copy of the piece, and the new item has that copy's tier: a Godly Pulse Amp makes a Godly Nova Amp, a Standard one a Standard Nova Amp. What you paid the Forge for is not lost. The upgrade adds no tier of its own, so a Standard piece always makes a Standard result.
- **The buffs are rolled again.** The new item gets fresh buffs for its tier: as many as the tier holds and the new item has stats for (a Godly Nova Amp holds two), each in the tier's range from the table above, on stats the Nova Amp has. Nothing is copied from the old piece, so the new buffs can be better or worse than the ones it had; on average they are the same. The buffs are rolled the moment you queue the job, and what you collect is what was rolled: waiting to collect changes nothing. The reason is that the upgrade builds a new item, and the Forge's dice are cast on the item you hold. The tier is the part that costs: an Eternal piece is over a million credits of Forge steps, while a buff is a few percent of one stat.
- **Plates.** Besides Thulium and what the aliens drop, every module upgrade takes **Velkonite Reinforced Plates**: 3 for an amp, 6 for a cell or a thruster (the Helios Beam takes Orvium Reinforced Plates instead, 18 of them). Aliens don't drop them. Your [Skylab](/wiki/03-Mechanics/Skylab.md) Forgery makes them from Velkonite ore, 40 ore a plate at Forgery level 1. A level 1 Velkonite Collector mines 12 ore an hour, so an amp's plates are 10 hours of mining and a cell's or a thruster's 20 (4 and 8 hours from a level 5 collector). Where every material comes from is on the [Resources](/wiki/05-Items/Resources.md) page. The Forge's own steps take drops and credits, and its top steps take plates as well (Godly to Rupturing: 20 Reinforced Hull Plates and 2 Dark Matter Plates; Rupturing to Eternal: 2 Dark Matter Plates), which is a different thing from the Velkonite and Orvium plates of the module upgrades.
- **Which copy is used.** You choose. When you hold copies that differ (another tier or other buffs), the recipe card shows them as a row of tiles: click the one to use, and the line under the tiles shows what it becomes ("Godly Pulse Amp", then "Result: Godly Nova Amp"). If you choose none, the plainest goes: the lowest tier first, and among copies of one tier the oldest, whatever their buffs. A Godly or better copy is never used while a plainer one is loose. Using a copy above Standard asks first and names the item.
- **Which copies can be used.** Loose ones: a copy on a ship, fitted into another item or in the [Transport Cache](/wiki/03-Mechanics/Cargo.md) can't be used, and the Assembly tells you so. Take it off or out of the cache first. Two upgrades started together can't use the same copy.

- **The Helios Beam is an upgrade too.** It is made out of a **Starfire-3** (with 2,000 Thulium, drops and 18 Orvium Reinforced Plates: see [Lasers](/wiki/05-Items/Lasers.md)), and everything above applies: a Godly Starfire-3 makes a Godly Helios Beam with two new buffs (it holds two of its three stats), you choose the copy, the card asks before it uses one above Standard, and the Starfire-3 must be loose. A laser is fitted on a ship and carries amps, so it is often not: take it off in the Hangar first (its amps go back to your inventory), and the Assemble button says "Unequip your Starfire-3" until you do.

The recipes, their costs and the numbers behind the rule are on the [Items overview](/wiki/05-Items/Overview.md#upgrading-modules) and, for the Helios Beam, on the [Lasers](/wiki/05-Items/Lasers.md) page.

## Old servers

A game server that has not been updated to the Forge shows "The Forge is not on this server yet" in place of the tab; Crafting works as before. A game client from before the Forge shows the old Fusion tab on an updated server and is told to update.
