# The Forge

<!-- wiki-search: forge; tier up; tier-up; tiers; sockets; tune; attune; attuning; re-lay; relay; reforge; shard; shards; echo; echo shard; lattice; lattice shard; heartshard; heart shard; integrity; fracture; fractures; fractured; repair; merge; fusion; tainted; godly; rupturing; eternal; awakened; resonant; radiant; ascendant; tinkerer's badge -->

The **Forge** is the second tab of the Assembly page (and of the Assembly window in flight). It does three things with equipment you own: it **raises an item one tier** for credits and alien drops, it **tunes its sockets** with shards, which is how you choose its buffs, and it **merges two copies** of an item into one that keeps the best of both. A step up never fails, and a new buff goes into an item when you choose it from an offer or, with a 25% chance at each step up, as a free buff. (Before 0.5.7 the tiers were called Tainted, Godly, Rupturing and Eternal, and a step could fail; they are now Awakened, Resonant, Radiant and Ascendant.) The Forge replaced the old Fusion Chamber, which needed five identical items and left the result to a 25% roll.

## What can be forged

Lasers, Laser Amps, Shield Cores, Shield Cells, Engines, Thrusters, Adaptive Cores, Repair Drones and [Hull Plating](/wiki/06-Items/Hull-Plating.md): any single piece of equipment that can carry [enchant buffs](/wiki/06-Items/Overview.md). It can be in your inventory, on a ship (it stays there and works with its new tier at once) or fitted into another item. Drones, ships, ammo, resources and boosters can't be forged, and neither can anything in the Transport Cache or fitted in your Skylab's Engine or Defense module: take it out first.

The list of equipment has an **All / Equipped / In inventory** switch next to the tier and type filters. **Equipped** shows what is on a ship or fitted into another item, **In inventory** what lies loose, and a line under the title says how many pieces the switch hides. While you choose the donor of a merge, Equipped is paused, because a donor must be loose.

A **Ship** drop-down beside the type filter shows only the pieces on one of your ships (a piece fitted into another item counts for the ship its host is on). It is paused under *In inventory* and while you choose the donor of a merge. A piece's hover card, the panel's header and the merge's base say where it is: *On Kitefin, configuration 1* (a Hull Plating: both configurations), and what it is fitted into. **Ctrl+F** (Cmd+F on a Mac) puts the cursor in the search box in the Assembly's header; it narrows the open tab's list (recipes by what they make and ask for, equipment by name, type and tier), and Esc clears it. Under *Sockets awake* the panel says when a stat of the piece is too low to carry a buff, which is why an Impulse Thruster holds one buff and a Momentum Thruster two.

## Tier up

Pick an item and the **Upgrade** view shows its tier, the tier it would reach, what that changes (how many buffs it can hold and how big they are), and the price with what you have of each part: green when you have enough, red when you don't, and how many you are short. When you have it all, **Tier up** raises the item by exactly one tier. There is no jump: to reach Ascendant an item goes through Awakened, Resonant and Radiant, each with its own price.

| Step | Credits | Thulium | Materials |
| :--- | :---: | :---: | :--- |
| Standard to Awakened | 10,000 | – | 5 Ship Fragment, 15 Daraxium |
| Awakened to Resonant | 56,000 | – | 32 Ship Fragment, 48 Nyxite |
| Resonant to Radiant | 267,000 | – | 23 Reinforced Hull Plate, 140 Cataclysite, 2 Dark Matter Plate |
| Radiant to Ascendant | 833,000 | 2,667 | 11 Power Core, 320 Quorvium, 2 Dark Matter Plate |

- **Materials** come from your loose stacks: items on a ship and stacks in the Transport Cache are not used. The panel tells you when the missing ones are in the cache.
- **A step always works.** It costs what a step cost on average before the Forge had sockets, and it wakes one more socket in the item (see [Buffs by tier](#buffs-by-tier)).
- **Your Commerce skill** lowers the credits and the Thulium of a step, and the credits of a merge, by up to 15% at level 100 ([Pilot Skills](/wiki/03-Mechanics/Pilot-Skills.md)). The table shows the price at the first level and the panel the price you pay; the materials do not change.
- **Each buff the item has** is rolled again in the new tier's range and keeps the better value. The result is shown above the panel; the item stays selected, so its next step is already on screen.
- **A free buff, with a 25% chance.** Each step up rolls once. On a hit, one buff is put into an empty socket of the item for free: no Echo Shard, no Lattice Shard and no integrity are spent. Its stat is picked at random among the item's stats that have no buff yet, all with the same chance, and there is no offer to choose from. The buff is rolled in the size range of the tier the item has just reached, and from then on it is an ordinary tuned socket (a re-lay, a merge and the fractures treat it like any other buff). The socket the step wakes counts as empty, so a step that wakes a socket always has one to fill; with no empty socket there is no roll. Under *Sockets awake* the panel says whether a step can give one, and the result above the panel names the stat and its value when one landed.
- A tier-up is instant.
- **The sockets are under the step.** Tier up and [Sockets](#sockets) are one view, **Upgrade**, with Tier up first: the socket a step wakes is in the list right below the button, with its Tune button, so you don't switch anywhere to use it.
- **A Tinkerer's Badge** (a [special item](/wiki/06-Items/Special-Items.md#tinkerers-badge)) raises a piece one tier with no Credits, no Thulium and no materials, from Standard on. It is a step that costs nothing: it wakes a socket, rolls the buffs the piece holds again and rolls the free buff with the same chance, as a paid step does.

### Dark Matter Plates

The last two steps ask for **2 Dark Matter Plates** each, on top of everything else. A plate is pressed in [Assembly](/wiki/06-Items/Overview.md) from **5 Dark Matter, 1 Velkonite Reinforced Plate and 1 Orvium Reinforced Plate** (250 Thulium, 2 minutes), so one step takes 10 Dark Matter, 2 Velkonite plates and 2 Orvium plates. Dark Matter comes from the [black hole](/wiki/03-Mechanics/Black-Hole.md): about five N.I.K.E. rockets (see [Rockets](/wiki/06-Items/Rockets.md)) make ten; a N.I.K.E. that meets a ship on its way hits that ship instead and makes none. The plates are used from your loose stacks like the other materials, and the panel names them if you are short. The last tier of every upgrade chain asks for plates too, 4 each ([Dark Matter and Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)).

### Buffs by tier

| Tier | Buffs held at most | Size of each buff | Crystal of the step |
| :--- | :---: | :---: | :--- |
| Awakened | 1 | +2% to +5% | Daraxium |
| Resonant | 2 | +4% to +8% | Nyxite |
| Radiant | 3 | +6% to +11% | Cataclysite |
| Ascendant | 4 | +9% to +15% | Quorvium |

Equipment made before the Forge keeps the buffs it was rolled with, and those are often smaller than the table (a Resonant piece from back then can hold +2%). Nothing raises them by itself: a tier-up rolls each buff again in the new tier's range and keeps the better value, and a merge keeps the better value of each stat.

An item can't hold more buffs than it has stats: a Shield Core has four, a laser three, an engine or an Adaptive Core two, a Momentum Thruster two, an Impulse Thruster one (its multiplier of 1.017 to 1.03 is too small to be worth a buff, and the Forge rolls none on a multiplier of 1.05 or less, so its buff can only be on the flat speed), a Crit Amp I, a Repair Drone or a Hull Plating one (its hull), the higher crit amps two, the damage amps and shield cells three. When the next tier holds no more buffs than the item can carry, the panel says so: the tier then only makes the buffs stronger. Range buffs never pass +5%. A Penetration Amp has one stat, so it holds one buff.

**A tier holds that many buffs at most.** Each tier-up wakes one socket in the item, the one that goes with the crystal of the step: Daraxium wakes the first, Nyxite the second, Cataclysite the third and Quorvium the fourth. An item has as many sockets as its tier holds and it has stats for: a Resonant Shield Core has two, an Ascendant one all four, and an engine, which has two stats, has no third socket to wake. A buff goes into a socket when you tune it with an Echo Shard and choose it from the offer, or when a step up gives it for free. A **merge** keeps the best buff of each stat of two copies, up to the tier's limit.

A **shield's Absorbance buff** (and a shield cell's Absorbance Boost) multiplies the stat, so it is worth points of [absorbance](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-) in proportion to it: +5% on a Heavy Shield Core's 55% is +2.75 points, and +15% on every piece of the best set (a Heavy Shield Core and three Absorption Shield Cell IVs, 91% in all) is +13.65 points. An Ascendant set takes between +8.2 and +13.65 points, about 11 on average; with the Season Store's Shield Absorbance Boost (+10 points at its limit; the Wipe Points of one wipe buy 44 of its 100 levels, +4.4 points) that takes a ship to about 106%, and well past it with the Pilot research Field Theory (up to +10 points), which the stat allows: an attacker's shield penetration is taken off it. A Resonant set takes between 3.6 and 7.3 points. These are the numbers of buffs with no fracture on them ([Integrity and fractures](#integrity-and-fractures)).

Engines, thrusters, Adaptive Cores and Repair Drones move very little with a percentage buff (an Engine II adds 10 speed, so +12% is 1.2 points): forge them if you want the tier, not for the stats.

**A Penetration Amp's buff** multiplies its penetration: an Ascendant buff (+9% to +15%) makes a Penetration Amp IV 27.3 to 28.8 points a slot instead of 25. Nothing caps the penetration of a hit, so every point counts: in the best laser (a Fusion Core, a Gemini and three Penetration Amp IV in every laser) 10 + 15 + 75 make 100%, and three Ascendant buffs raise it to as much as 111% ([Lasers](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)).

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

The crystals follow the tiers: Daraxium is blue like Awakened, Nyxite yellow like Resonant, Cataclysite orange like Radiant and Quorvium violet like Ascendant. Every source, with the chances and amounts, is on the [Resources](/wiki/06-Items/Resources.md) page and on each alien's page; the Resource Magnet Booster adds 25% to what a crate holds. The [asteroids](/wiki/03-Mechanics/Asteroid-Mining.md#the-kinds) leave all of them but the Dark Matter Plate in their chunks.

## Sockets

The **Sockets** block of the Forge's Upgrade view, under Tier up, is where you choose a buff for an item. Pick a piece and the block lists its sockets, its integrity and the shards you hold. A socket is **locked** until a tier-up wakes it (its row says at which tier and with which crystal's step), **empty** once it is awake, and **tuned** when it holds a buff. The Tier up block counts them: *Sockets awake 1 → 2 of 4*.

- **Tune** an empty socket with **Echo Shards**: 10 for the first socket of a piece, then 20, 40 and 80, so the price rises with every socket that holds a buff, and a free buff of a step up counts as one: a piece that got free buffs needs fewer Echo Shards in all (the dimmed price on each later empty socket says what it will cost). The shards are spent when you press Tune, and the Forge then lays out an **offer**: two of the stats that are still free, picked at random, each with the buff it would give. **Choose** one: you get what the offer showed. When only one stat is left free, both lines are rolls of that stat, and they can come out the same.
- **A Heartshard** can be added to a tune or a re-lay: switch on *Use a Heartshard* first, and the offer lists every free stat of the piece instead, each rolled in the upper half of its range, so you choose the stat.
- **Re-lay** a tuned socket with **Lattice Shards** when you want another stat there. It costs 2 Lattice Shards for the first re-lay of a piece, then 3, 4, 4, 5, 7 and on (2 multiplied by 1.25 once for every earlier re-lay, rounded up), and some of the piece's integrity: 6 points, fewer with Fabrication ([Integrity and fractures](#integrity-and-fractures)). A sheet asks first, because the shards and the integrity are spent whatever you choose. The offer is made like a tune's, from the free stats and the stat the socket has now, each rolled anew, and it has a **Keep current** button across the whole width, for when none of them beats the buff the socket has.
- **Until you choose, the piece waits.** An open offer blocks the piece: nothing else works on it, and the panel says so. Closing the game loses nothing, the offer is there when you come back. An offer nobody answers is settled for you after 7 days, the next time the Forge touches the piece (selecting it there is enough): a tune takes the first stat of the offer, a re-lay keeps the current buff. The Auction and the Assembly's module upgrades never settle an offer, they refuse the piece until the Forge has, so open the piece in the Forge first.
- **Repair** restores 12 integrity for twice the Lattice Shards the next re-lay would cost. It does not lower the re-lay count, so the price of the next re-lay stays.
- **The gauge** shows the integrity with a mark at each point where a further fracture opens (the first opens with the first point lost), and its hover says which stat each fracture took. A tuned socket whose buff lost points to a fracture shows both numbers (a +9% buff with two fractures: *−4% fractured (rolled +9%)*), and one that is down to nothing says *Fractured away: no bonus left*: the socket stays tuned and its buff is +0%.
- **Only loose stacks are spent.** Shards in the Transport Cache are not, and the panel says when the missing ones are there. Shards can't be bought, sold or listed on the Auction, and neither luck nor the Resource Magnet Booster adds to them.

### Where the shards come from

Tuning all four sockets of a piece takes 150 Echo Shards (10 + 20 + 40 + 80), and its first 16 re-lays take 283 Lattice Shards. They come from [Solo Gates](/wiki/03-Mechanics/Solo-Gates.md) and [Dungeons](/wiki/03-Mechanics/Dungeons.md), on top of what those pay otherwise, and a few Echo Shards from aliens:

| Source | Echo Shards | Lattice Shards |
| :--- | :---: | :---: |
| Solo gate: Alpha Rift | 4 | 6 |
| Solo gate: Beta Breach | 9 | 13 |
| Solo gate: Gamma Foundry | 18 | 27 |
| Solo gate: Delta Siege | 29 | 44 |
| Solo gate: Omega Vault | 34 | 54 |
| Solo gate: Davidski's Nightmare | 34 | 54 |
| Clan dungeon: stage 1 | 12 | 5 |
| Clan dungeon: stage 2 | 8 | 6 |
| Clan dungeon: stage 3 | 8 | 7 |

- **Solo gates** pay their shards with every clear, **clan dungeons** with every paid clear of a stage.
- **Heartshards** come with the first clear of each gate and of each dungeon stage in a season (1) and with a 5% chance of 1 more at every clear. The rare NPCs drop them too: 10% for Davidski, 5% for Dormant Force and for Tesseract. The [Resources](/wiki/06-Items/Resources.md#heartshard) page has the rest.
- **Aliens** drop Echo Shards only, and few: from 0.8% a kill for a Seeker to 40% for a Crystalys ([Echo Shard](/wiki/06-Items/Resources.md#echo-shard)).

## Merge

Two copies of the same item (two Light Shield Cores, two Quantum Laser II) become one. Switch to **Merge** and click the item you want to keep (the **base**), then a second copy (the **donor**). The panel shows the result before you confirm.

- **The base is kept.** It keeps its place: it may be on a ship, or fitted into another item, and the modules fitted into it stay. **The donor is used up.** It must be loose (not on a ship, not fitted), and the modules fitted into it go back to your inventory.
- **The result has the higher of the two tiers**, and for each stat the **better of the two values**.
- **It never holds more buffs than its tier allows.** If the two items together have more buffs than the result's tier can hold, the best ones are kept and the rest are dropped; the table marks them (struck through, "over the limit"). To hold more buffs, tier the item up first. A merge never rolls anything: what the preview shows is what you get.
- **A merge costs credits by the tier it makes**: 5,000 for Awakened, 25,000 for Resonant, 100,000 for Radiant, 250,000 for Ascendant. No materials. Your Commerce skill lowers the credits like those of a step.
- A merge that would change nothing (the result is no better than the base) is refused. A better integrity alone does not count: a merge is not a repair.
- **Integrity.** The result's integrity is the average of the two pieces' integrity (rounded down) minus 6, never under 0, and its re-lay count is the higher of the two: two whole pieces merge into a piece at 94. The result keeps the base's order of fractures: the same stat is hit first. See [Integrity and fractures](#integrity-and-fractures).
- After a merge the result stays selected and the donor slot is empty: put the next donor in, or switch back to Upgrade.
- **The tag**: the merged piece is **Marketable** (it can be sold on the [Auction](/wiki/03-Mechanics/Auction.md#marketable-items)) only if both the base and the donor were. The preview says so.

A merge doesn't multiply an item. Its use is choosing: a Resonant core with the stats you want, or a tier moved onto the item on your ship without taking it off.

## Integrity and fractures

Every piece of equipment has an **integrity** from 0 to 100. A piece nobody has worked on is at 100. A piece you craft in the Assembly or loot (from the box of an alien, a swarm or a Warden, or as a clan dungeon's gear card) starts anywhere from 70 to 100; what you buy or are given, and everything you had before 0.5.7, is whole. Re-laying a socket (it takes a Lattice Shard) costs integrity: 6 points, 5 from Fabrication level 29 and 4 from level 84 ([Pilot Skills](/wiki/03-Mechanics/Pilot-Skills.md)), and a piece with no more than that left can't be re-laid. A repair gives 12 points back (see [Sockets](#sockets)).

Every 12 points under 100 is a **fracture**, and a started 12 counts: a piece at 99 to 88 has one, at 87 to 76 two, and so on, up to 8. A fracture takes 2 points off the buff of one stat: a +9% buff with two fractures on it is +5%. The fractures take the item's stats in turn, in an order that is fixed for each piece: the first fracture hits one stat, the second the next, and when every stat has had one the round starts again. A stat with no buff yet is hit too: its fractures wait, and count the moment you tune a buff into it. A buff never goes below +0%, so a fracture never makes a piece worse than the plain item. An item with a single stat to buff (a Hull Plating, a Repair Drone, a Crit Amp I, a Penetration Amp, an Impulse Thruster) takes every fracture on that stat: at 8 fractures, 16 points, not even a +15% buff is left.

What the inventory, the Hangar, the Auction and the Forge show for a damaged piece is what it **flies with**: the fractures are already taken off, and a list of the fractures stands beside it. A tier-up and a module upgrade leave the integrity as it is; a [merge](#merge) sets it to the average of the two pieces minus 6.

## The season wipe

A piece that the [wipe](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) keeps (one fitted on the ship that keeps its gear, one fitted in your Skylab, one in the Transport Cache) keeps everything the Forge did to it: its tier, its tuned sockets and their buffs, its integrity, its re-lay count and an offer that is still open. The wipe repairs nothing and breaks nothing. The shards are resources like the ores: the wipe destroys the loose ones, and the ones you put in the Transport Cache are kept (1 kg each).

## Module upgrades in the Assembly

The top three lasers, laser amps, the shield cells and thrusters of tiers II to IV, the engines and Adaptive Cores of tiers II and III, and the Heavy Shield Core are not sold, and Assembly makes each only after you have researched its technology in the Skylab ([Research](/wiki/03-Mechanics/Research.md)). You make them in the Assembly's **Crafting** tab by upgrading the piece one step below: a Damage Amp III into a **Damage Amp IV**, a Crit Amp III into a **Crit Amp IV**, a Capacity Shield Cell I into a **Capacity Shield Cell II** (and on to III and IV; the Absorption cells, the Impulse Thrusters and the Momentum Thrusters climb the same way), a Basic Shield Core into a **Heavy Shield Core**, an Engine I into an **Engine II** and on into an **Engine III**, an Adaptive Core I into an **Adaptive Core II** and on into an **Adaptive Core III**, a Quantum Laser II into a **Quantum Laser III**, a Quantum Laser III into a **Starfire-III**, and a Starfire-III into a **Helios Beam**. What the Forge has to do with it is the tier. The first tier of each amp family (the Damage Amp I, the Crit Amp I and the Penetration Amp I) is sold in the Shop; tiers II to IV of every family are made like this.

- **The tier stays.** An upgrade uses up one copy of the piece, and the new item has that copy's tier: a Resonant Damage Amp III makes a Resonant Damage Amp IV, a Standard one a Standard Damage Amp IV. What you paid the Forge for is not lost. The upgrade adds no tier of its own, so a Standard piece always makes a Standard result.
- **The buffs stay.** The new item keeps the buffs of the piece you use up: the same stats with the same values, nothing is rolled again (a Resonant Damage Amp III with two buffs makes a Resonant Damage Amp IV with those two buffs, one with a single buff makes one with that single buff). Every stat of a piece is also a stat of its upgrade, so each buff finds its place, and an upgrade neither tunes an empty socket nor takes a buff away. The buffs are settled the moment you queue the job, and what you collect is what was settled: waiting to collect changes nothing, and if you cancel the job the very same piece comes back, tier and buffs as they were. A job queued before this rule keeps the buffs it was rolled with. What the Forge made of the piece is the part that costs: an Ascendant piece is over a million credits of Forge steps, and the upgrade keeps all of it. **The piece's integrity and its re-lay count stay with it too**: an upgrade is no repair and wipes no fracture.
- **Plates.** Besides Thulium and what the aliens drop, every module upgrade takes plates. The last tier takes **4 Dark Matter Plates** and at least one Ancient Control Unit: a tier IV amp, cell or thruster, the Heavy Shield Core, the Engine III, the Adaptive Core III and the Helios Beam. The steps before it take **Velkonite Reinforced Plates**: 2 for an amp of tier II or III, 4 for a cell or a thruster of tier II or III, 3 for a Quantum Laser III, 4 for an Engine II or an Adaptive Core II and 8 for a Starfire-III (the Helios Beam takes 18 Orvium Reinforced Plates too). Aliens don't drop any of them. Your [Skylab](/wiki/03-Mechanics/Skylab.md) Forgery makes the Velkonite and Orvium plates from ore, 40 Velkonite ore a plate at Forgery level 1. A level 1 Velkonite Collector mines 10 ore an hour, so a tier III amp's plates are 8 hours of mining and a tier III cell's or thruster's 16 (4 and 9 hours from a level 5 collector). Assembly presses a [Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md) from 5 Dark Matter, a Velkonite and an Orvium Reinforced Plate and 250 Thulium, once you have researched the plate's recipe. Where every material comes from is on the [Resources](/wiki/06-Items/Resources.md) page. The Forge's own steps take drops and credits, and its top steps take Dark Matter Plates as well (Resonant to Radiant: 23 Reinforced Hull Plates and 2 Dark Matter Plates; Radiant to Ascendant: 2 Dark Matter Plates): the same plates as the last tier of a module upgrade.
- **Which copy is used.** You choose. When you hold copies that differ (another tier or other buffs), the recipe card shows them as a row of tiles: click the one to use, and the line under the tiles shows what it becomes ("Resonant Damage Amp III", then "Result: Resonant Damage Amp IV"). If you choose none, the plainest goes: the lowest tier first, and among copies of one tier the oldest, whatever their buffs. A Resonant or better copy is never used while a plainer one is loose. Using a copy above Standard asks first and names the item.
- **Which copies can be used.** Loose ones: a copy on a ship (an ability slot too), fitted into another item, fitted in your Skylab's Engine or Defense module, holding cells or thrusters of its own, or in the [Transport Cache](/wiki/03-Mechanics/Cargo.md) can't be used, and the Assembly tells you so. Take it off or out of the cache first. Two upgrades started together can't use the same copy.

- **The Quantum Laser III is an upgrade too.** It is made out of a **Quantum Laser II**, the Shop's laser (with 1,500 Thulium, 10 Ship Fragments and 3 Velkonite Reinforced Plates: see [Lasers](/wiki/06-Items/Lasers.md)), and everything above applies: a Resonant Quantum Laser II makes a Resonant Quantum Laser III with the same buffs, you choose the copy, the card asks before it uses one above Standard, and the Quantum Laser II must be loose: take it off in the Hangar first, and the Assemble button says "Unequip your Quantum Laser II" until you do. The tier then goes on up: a Resonant Quantum Laser III makes a Resonant Starfire-III.

- **The Starfire-III is an upgrade too.** It is made out of a **Quantum Laser III** (with 1,500 Thulium, 100,000 Credits, drops and 8 Velkonite Reinforced Plates: see [Lasers](/wiki/06-Items/Lasers.md)), and everything above applies: a Resonant Quantum Laser III makes a Resonant Starfire-III with the same buffs, you choose the copy, the card asks before it uses one above Standard, and the Quantum Laser III must be loose: take it off in the Hangar first, and the Assemble button says "Unequip your Quantum Laser III" until you do. The tier then goes on up: a Resonant Starfire-III makes a Resonant Helios Beam.

- **The Helios Beam is an upgrade too.** It is made out of a **Starfire-III** (with 2,000 Thulium, drops, 18 Orvium Reinforced Plates, 4 Dark Matter Plates and an Ancient Control Unit: see [Lasers](/wiki/06-Items/Lasers.md)), and everything above applies: a Resonant Starfire-III makes a Resonant Helios Beam with the Starfire-III's buffs, you choose the copy, the card asks before it uses one above Standard, and the Starfire-III must be loose. A laser is fitted on a ship and carries amps, so it is often not: take it off in the Hangar first (its amps go back to your inventory), and the Assemble button says "Unequip your Starfire-III" until you do.

The recipes, their costs and the numbers behind the rule are on the [Items overview](/wiki/06-Items/Overview.md#upgrading-modules) and, for the Quantum Laser III, the Starfire-III and the Helios Beam, on the [Lasers](/wiki/06-Items/Lasers.md) page.

## Old servers

A game server that has not been updated to the Forge shows "The Forge is not on this server yet" in place of the tab; Crafting works as before. A game client from before the Forge shows the old Fusion tab on an updated server and is told to update. A server from before 0.5.7 has no Sockets block, and a game from before 0.5.7 can still open the Forge and read it, but an updated server turns away every change it asks for (a tier-up, a merge, a tune, a re-lay, a repair, a Tinkerer's Badge) with "Update the game to use this feature."
