# The Forge

The **Forge** is the second tab of the Assembly page (and of the Assembly window in flight). It does two things with equipment you own: it **raises an item one tier** for credits and alien drops, and it **merges two copies** of an item into one that keeps the best of both. It replaced the old Fusion Chamber, which needed five identical items and left the result to a 25% roll.

## What can be forged

Lasers, Laser Amps, Shield Cores, Shield Cells, Engines, Thrusters, Adaptive Cores and Repair Drones: any single piece of equipment that can carry [enchant buffs](/wiki/06-Items/Overview.md). It can be in your inventory, on a ship (it stays there and works with its new tier at once) or fitted into another item. Drones, ships, ammo, resources and boosters can't be forged, and neither can anything in the Transport Cache: take it out first.

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
- **On success** each buff the item has is rolled again in the new tier's range and keeps the better value. An item with no buff always gets its first one; every other slot the new tier opens is filled with a **50% chance, each on its own roll**, on other stats of the item, and a slot that misses can fill at a later tier-up (see [Buffs by tier](#buffs-by-tier)). The result is shown above the panel; the item stays selected, so its next step is already on screen.
- A tier-up is instant.

### Dark Matter Plates

The last two steps ask for **2 Dark Matter Plates** each, on top of everything else. A plate is pressed in [Assembly](/wiki/06-Items/Overview.md) from **5 Dark Matter, 1 Velkonite Reinforced Plate and 1 Orvium Reinforced Plate** (250 Thulium, 2 minutes), so one step takes 10 Dark Matter, 2 Velkonite plates and 2 Orvium plates. Dark Matter comes from the [black hole](/wiki/03-Mechanics/Black-Hole.md): about five N.I.K.E. rockets (see [Rockets](/wiki/06-Items/Rockets.md)) make ten; a N.I.K.E. that meets a ship on its way hits that ship instead and makes none. The plates are used from your loose stacks like the other materials, and the panel names them if you are short. The last tier of every upgrade chain asks for plates too, 3 each ([Dark Matter and Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)).

### Buffs by tier

| Tier | Buffs held at most | Size of each buff |
| :--- | :---: | :---: |
| Tainted | 1 | +2% to +5% |
| Godly | 2 | +4% to +8% |
| Rupturing | 3 | +6% to +11% |
| Eternal | 4 | +9% to +15% |

Equipment made before the Forge keeps the buffs it was rolled with, and those are often smaller than the table (a Godly piece from back then can hold +2%). Nothing raises them by itself: a tier-up rolls each buff again in the new tier's range and keeps the better value, and a merge keeps the better value of each stat.

An item can't hold more buffs than it has stats: a Shield Core has four, a laser three (the Quantum Laser I and II have two), an engine or an Adaptive Core two, a Momentum Thruster two, an Impulse Thruster one (its multiplier of 1.02 to 1.035 is too small to be worth a buff, and the Forge rolls none on a multiplier of 1.05 or less, so its buff can only be on the flat speed), a Crit Amp I or a Repair Drone one, the higher crit amps two, the damage amps and shield cells three. When the next tier holds no more buffs than the item can carry, the panel says so: the tier then only makes the buffs stronger. Range buffs never pass +5%. A Penetration Amp has one stat, so it holds one buff.

**A tier holds that many buffs at most.** A tier-up always gives an item its first buff; every other slot the new tier opens, and the item has a stat for, is filled with a **50% chance, each on its own roll**, and a slot that misses is tried again by the next tier-up. So a Godly Shield Core has two buffs half the time and one the other half; an Eternal one has all four about a third of the time (3.1 buffs on average), a laser with three stats has all three two times in three, and an engine nearly always has both. The panel says "up to" for the next tier and how often a new slot fills. Items with one stat, and every step to Tainted, are not affected, and equipment made before this rule keeps the buffs it has. A **merge** is how you fill a slot a tier-up missed: it keeps the best buff of each stat of two copies, up to the tier's limit. Because of the chance, a piece carries the Absorbance buff described next only part of the time (an Eternal Shield Core 78% of the time, an Eternal Shield Cell 88%): the figures there are for pieces that carry it.

A **shield's Absorbance buff** (and a shield cell's Absorbance Boost) multiplies the stat, so it is worth points of [absorbance](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-) in proportion to it: +5% on a Heavy Shield Core's 50% is +2.5 points, and +15% on every piece of the best set (a Heavy Shield Core and three Absorption Shield Cell IVs, 80% in all) is +12 points. An Eternal set takes between +7 and +12 points, about 10 on average; with the Season Store's Shield Absorbance Boost (+10 points at its limit; the Wipe Points of the whole game buy 34 of its 100 levels, +3.4 points) that takes a ship to 95%, and past 100% only with the buff's limit, which the stat allows: an attacker's shield penetration is taken off it. A Godly set takes between 3 and 6 points.

Engines, thrusters, Adaptive Cores and Repair Drones move very little with a percentage buff (an Engine II adds 4 speed, so +12% is half a point): forge them if you want the tier, not for the stats.

**A Penetration Amp's buff** multiplies its penetration: an Eternal buff (+9% to +15%) makes a Penetration Amp IV 8.7 to 9.2 points a slot instead of 8. In the best laser (a Fusion Core, a Stiletto and three Penetration Amp IV in every laser) 10 + 16 + 24 already reach the 50% cap of a laser hit, so that buff is wasted there; it pays where the sum is under the cap ([Lasers](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)).

### Where the materials drop

| Material | Dropped by |
| :--- | :--- |
| **Ship Fragment** | every alien |
| **Daraxium** | [Seeker](/wiki/04-Aliens/Seeker.md), [Phantasm](/wiki/04-Aliens/Phantasm.md) |
| **Nyxite** | [Phantasm](/wiki/04-Aliens/Phantasm.md), [Bulwark](/wiki/04-Aliens/Bulwark.md) |
| **Reinforced Hull Plate** | [Bulwark](/wiki/04-Aliens/Bulwark.md), [Goombah](/wiki/04-Aliens/Goombah.md) |
| **Cataclysite** | [Bulwark](/wiki/04-Aliens/Bulwark.md), [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Power Core** | [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Quorvium** | [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Dark Matter Plate** | no alien: Assembly presses it from Dark Matter (the [black hole](/wiki/03-Mechanics/Black-Hole.md)) and the Skylab's plates |

The crystals follow the tiers: Daraxium is blue like Tainted, Nyxite yellow like Godly, Cataclysite orange like Rupturing and Quorvium violet like Eternal. Every source, with the chances and amounts, is on the [Resources](/wiki/06-Items/Resources.md) page and on each alien's page; the Resource Magnet Booster adds 25% to what a crate holds. The [asteroids](/wiki/03-Mechanics/Asteroid-Mining.md#the-kinds) leave all of them but the Dark Matter Plate in their chunks.

## Merge

Two copies of the same item (two Light Shield Cores, two Quantum Laser II) become one. Switch to **Merge** and click the item you want to keep (the **base**), then a second copy (the **donor**). The panel shows the result before you confirm.

- **The base is kept.** It keeps its place: it may be on a ship, or fitted into another item, and the modules fitted into it stay. **The donor is used up.** It must be loose (not on a ship, not fitted), and the modules fitted into it go back to your inventory.
- **The result has the higher of the two tiers**, and for each stat the **better of the two values**.
- **It never holds more buffs than its tier allows.** If the two items together have more buffs than the result's tier can hold, the best ones are kept and the rest are dropped; the table marks them (struck through, "over the limit"). To hold more buffs, tier the item up first. A merge never rolls anything: what the preview shows is what you get.
- **A merge costs credits by the tier it makes**: 5,000 for Tainted, 25,000 for Godly, 100,000 for Rupturing, 250,000 for Eternal. No materials.
- A merge that would change nothing (the result is no better than the base) is refused.
- After a merge the result stays selected and the donor slot is empty: put the next donor in, or switch back to Tier up.
- **The tag**: the merged piece is **Marketable** (it can be sold on the [Auction](/wiki/03-Mechanics/Auction.md#marketable-items)) only if both the base and the donor were. The preview says so.

A merge doesn't multiply an item, but it fills the slots a tier-up missed: two Godly Shield Cores merged are worth about three and a half points of buffs more than one, on average. Its use is choosing: a Godly core with the stats you want, or a tier moved onto the item on your ship without taking it off.

## Module upgrades in the Assembly

The top three lasers, laser amps, the shield cells and thrusters of tiers II to IV, the Heavy Shield Core and the Engine III are not sold, and Assembly makes each only after you have researched its technology in the Skylab ([Research](/wiki/03-Mechanics/Research.md)). You make them in the Assembly's **Crafting** tab by upgrading the piece one step below: a Damage Amp III into a **Damage Amp IV**, a Crit Amp III into a **Crit Amp IV**, a Capacity Shield Cell I into a **Capacity Shield Cell II** (and on to III and IV; the Absorption cells, the Impulse Thrusters and the Momentum Thrusters climb the same way), a Basic Shield Core into a **Heavy Shield Core**, an Engine II into an **Engine III**, a Quantum Laser II into a **Quantum Laser III**, a Quantum Laser III into a **Starfire-III**, and a Starfire-III into a **Helios Beam**. What the Forge has to do with it is the tier. The first tier of each amp family (the Damage Amp I, the Crit Amp I and the Penetration Amp I) is sold in the Shop; tiers II to IV of every family are made like this.

- **The tier stays.** An upgrade uses up one copy of the piece, and the new item has that copy's tier: a Godly Damage Amp III makes a Godly Damage Amp IV, a Standard one a Standard Damage Amp IV. What you paid the Forge for is not lost. The upgrade adds no tier of its own, so a Standard piece always makes a Standard result.
- **The buffs are rolled again.** The new item gets fresh buffs for its tier: as many as the piece you use up had (a Godly Damage Amp III with two buffs makes a Godly Damage Amp IV with two, one with a single buff makes one with a single buff; at least one above Standard), at most what the tier holds and the new item has stats for, each in the tier's range from the table above, on stats the Damage Amp IV has. Nothing else is copied from the old piece, so the new buffs can be better or worse than the ones it had; on average they are the same. The number is kept so that an upgrade can't fill the slots the Forge missed, and it never takes one away: a piece made before this rule with every slot filled keeps every slot. The buffs are rolled the moment you queue the job, and what you collect is what was rolled: waiting to collect changes nothing. The reason is that the upgrade builds a new item, and the Forge's dice are cast on the item you hold. The tier is the part that costs: an Eternal piece is over a million credits of Forge steps, while a buff is a few percent of one stat.
- **Plates.** Besides Thulium and what the aliens drop, every module upgrade takes plates. The last tier takes **3 Dark Matter Plates**: a tier IV amp, cell or thruster, the Heavy Shield Core, the Engine III and the Helios Beam. The steps before it take **Velkonite Reinforced Plates**: 1 or 2 for an amp of tier II or III, 2 or 4 for a cell or a thruster of tier II or III, 2 for a Quantum Laser III and 8 for a Starfire-III (the Helios Beam takes 18 Orvium Reinforced Plates too). Aliens don't drop any of them. Your [Skylab](/wiki/03-Mechanics/Skylab.md) Forgery makes the Velkonite and Orvium plates from ore, 40 Velkonite ore a plate at Forgery level 1. A level 1 Velkonite Collector mines 10 ore an hour, so a tier III amp's plates are 8 hours of mining and a tier III cell's or thruster's 16 (4 and 9 hours from a level 5 collector). Assembly presses a [Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md) from 5 Dark Matter, a Velkonite and an Orvium Reinforced Plate and 250 Thulium, once you have researched the plate's recipe. Where every material comes from is on the [Resources](/wiki/06-Items/Resources.md) page. The Forge's own steps take drops and credits, and its top steps take Dark Matter Plates as well (Godly to Rupturing: 20 Reinforced Hull Plates and 2 Dark Matter Plates; Rupturing to Eternal: 2 Dark Matter Plates): the same plates as the last tier of a module upgrade.
- **Which copy is used.** You choose. When you hold copies that differ (another tier or other buffs), the recipe card shows them as a row of tiles: click the one to use, and the line under the tiles shows what it becomes ("Godly Damage Amp III", then "Result: Godly Damage Amp IV"). If you choose none, the plainest goes: the lowest tier first, and among copies of one tier the oldest, whatever their buffs. A Godly or better copy is never used while a plainer one is loose. Using a copy above Standard asks first and names the item.
- **Which copies can be used.** Loose ones: a copy on a ship (an ability slot too), fitted into another item, holding cells or thrusters of its own, or in the [Transport Cache](/wiki/03-Mechanics/Cargo.md) can't be used, and the Assembly tells you so. Take it off or out of the cache first. Two upgrades started together can't use the same copy.

- **The Quantum Laser III is an upgrade too.** It is made out of a **Quantum Laser II**, the Shop's laser (with 1,500 Thulium, 10 Ship Fragments and 2 Velkonite Reinforced Plates: see [Lasers](/wiki/06-Items/Lasers.md)), and everything above applies: a Godly Quantum Laser II makes a Godly Quantum Laser III with new buffs, you choose the copy, the card asks before it uses one above Standard, and the Quantum Laser II must be loose: take it off in the Hangar first, and the Assemble button says "Unequip your Quantum Laser II" until you do. The tier then goes on up: a Godly Quantum Laser III makes a Godly Starfire-III.

- **The Starfire-III is an upgrade too.** It is made out of a **Quantum Laser III** (with 1,500 Thulium, 100,000 Credits, drops and 8 Velkonite Reinforced Plates: see [Lasers](/wiki/06-Items/Lasers.md)), and everything above applies: a Godly Quantum Laser III makes a Godly Starfire-III with new buffs, you choose the copy, the card asks before it uses one above Standard, and the Quantum Laser III must be loose: take it off in the Hangar first, and the Assemble button says "Unequip your Quantum Laser III" until you do. The tier then goes on up: a Godly Starfire-III makes a Godly Helios Beam.

- **The Helios Beam is an upgrade too.** It is made out of a **Starfire-III** (with 2,000 Thulium, drops, 18 Orvium Reinforced Plates and 3 Dark Matter Plates: see [Lasers](/wiki/06-Items/Lasers.md)), and everything above applies: a Godly Starfire-III makes a Godly Helios Beam with new buffs (as many as the Starfire-III had, up to two of its three stats), you choose the copy, the card asks before it uses one above Standard, and the Starfire-III must be loose. A laser is fitted on a ship and carries amps, so it is often not: take it off in the Hangar first (its amps go back to your inventory), and the Assemble button says "Unequip your Starfire-III" until you do.

The recipes, their costs and the numbers behind the rule are on the [Items overview](/wiki/06-Items/Overview.md#upgrading-modules) and, for the Quantum Laser III, the Starfire-III and the Helios Beam, on the [Lasers](/wiki/06-Items/Lasers.md) page.

## Old servers

A game server that has not been updated to the Forge shows "The Forge is not on this server yet" in place of the tab; Crafting works as before. A game client from before the Forge shows the old Fusion tab on an updated server and is told to update.
