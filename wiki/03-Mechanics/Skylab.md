# Skylab

The Skylab is your personal orbital facility. It builds and upgrades modules that make Credits and Thulium, mine ore, forge the plates that Assembly turns into the best lasers and, from Core level 10, research the technologies Assembly needs. It works for you even while you are offline.

At Core level 10 the Skylab also grows: a **bridge** joins the Core to a second Core with six more module seats, and three more modules plug into it: the **Ammo Printer** and the **Rocket Factory**, which make ammo and rockets from nothing, and the **Ore Bay**, which moves the ore you carry into the Resource Storage (see [The bridge and Core 2](#the-bridge-and-core-2) and [Ore Bay](#ore-bay)).

At Core level 15 it grows once more and learns to fly: a **second bridge** joins the Core to a third Core, **Core 3**, with four more seats, and the four modules of the **Expedition** take them: the **Engine Module**, the **Defense Module**, the **Radar Module** and the **Trophies Bay**. With engines, lasers and ammo from your Ammo Printer the Skylab crosses a **universe map** of its own, hunts the aliens of the cells it reaches while you are away and brings the loot home (see [The second bridge and Core 3](#the-second-bridge-and-core-3) and [Expeditions](#expeditions)).

> [!NOTE]
> **What changed in 0.4.10.** Every Skylab module now has its own table of outputs, prices and times, level by level. You kept your levels: nothing was charged and nothing was refunded for the difference. What your farms and collectors were holding in their hoppers when the update arrived was paid out **once, at the old rate**: Credits and Thulium went to your account, the ore into your Resource Storage, and the hoppers started again from empty.
>
> Two rules are new. **Solar makes only 25% of its power while it upgrades**, so for most stations every farm and collector stops until the upgrade is done (see [Solar Module](#solar-module) and [Timing a Solar upgrade](#timing-a-solar-upgrade)). **The Resource Storage has its own cap for each ore**: one day of the collector's output at level 1, four days at level 20.

> [!NOTE]
> **What changed in 0.4.15.** The Core's step from level 9 to level 10 now costs **2,000 Thulium** more, and when it is done a **bridge** and a second Core, **Core 2**, appear with six new module seats. Solar moves to Core 2. Two new modules plug into it: the **Ammo Printer** and the **Rocket Factory**. Solar also makes more power from level 7, so a full station is still covered. Nothing you built is lost: a Core that is already at level 10 or higher has the bridge at once and pays nothing.

> [!NOTE]
> **What changed in 0.4.21.** The Core's step from level 14 to level 15 now costs **4,000 Thulium** more, and when it is done a second **bridge** and **Core 3** appear with four new seats. Solar moves to Core 3 and makes more power from level 15, so a full station is still covered. Four new modules take the seats: the **Engine Module**, the **Defense Module**, the **Radar Module** and the **Trophies Bay**, and with them your Skylab flies across the **universe map**, hunts on its own and brings its loot home (see [Expeditions](#expeditions)). Every module now has a **weight**, and the weight of the station and its engines decide how fast it flies (see [Weight and speed](#weight-and-speed)). The **Ore Bay** moves three times as much ore an hour and keeps three times as much allowance. Nothing you built is lost: a Core that is already at level 15 or higher has Core 3 at once and pays nothing.

![The Skylab of a Core 20 with the second bridge: Core 3 carries the Engine, Defense and Radar Modules and the Trophies Bay](../img/wiki-img/shots/skylab-core3.jpg)
![The Rocket Factory's sheet: the rocket it makes, the room to carry and its storage](../img/wiki-img/shots/skylab-factory.jpg)
![The Ore Bay's sheet: the ores it moves and banks for you and how much it holds](../img/wiki-img/shots/skylab-orebay.jpg)
![The Ammo Printer's Build sheet: its price in Credits, Thulium and Ship Fragments](../img/wiki-img/shots/skylab-printer-build.jpg)
![The Ammo Printer's sheet: its mode, rate, storage and what the next level gives](../img/wiki-img/shots/skylab-printer.jpg)
![The Skylab station fully grown, seen from the side as the page opens: three Cores in a row with their bridges, every module with its name tag, the Labels switch at the bottom left](../img/wiki-img/shots/skylab-station.jpg)
![The Resource Storage card of the Skylab](../img/wiki-img/shots/skylab-storage.jpg)
![The Skylab table of modules: level, production, storage, power and status of every module, from the Core to the Trophies Bay](../img/wiki-img/shots/skylab-table.jpg)
![The Skylab hunting in a cell of the Universe map: its hull and kills, the cell, the Defense and Engine Modules and the Trophies Bay filling, and Recall](../img/wiki-img/shots/skylab-trip.jpg)
![The Trophies Bay's sheet: its level and the capacity the trophies of a trip are kept in](../img/wiki-img/shots/skylab-trophies.jpg)
![The Universe map: 150 hexagonal cells, the ports, the cells you know and the cells the Radar can still scan, marked with a question mark](../img/wiki-img/shots/skylab-universe.jpg)

## In one minute

- Build **Solar** first: nothing in the Skylab runs without its power. The Credit Farm costs nothing to build, and the Thulium Farm costs 5,000 Credits and 500 Thulium.
- Farms and collectors fill a **hopper** (72 hours' worth) while you are away. **Collect** moves it to your account (Credits, Thulium) or to your Resource Storage (ore).
- The **Thulium Farm** is your main source of Thulium: 40 an hour at level 1, 1,280 at level 20. The Credit Farm makes 2,250 Credits an hour at level 1 and 225,000 at level 20.
- The **Core** is the clock: no module goes above it, and its own climb takes about 16 and a half days.
- At **Core level 10** a **bridge** builds **Core 2**, with six more module seats, and the **Ammo Printer**, the **Rocket Factory** and the **Ore Bay** plug into it. The step into level 10 costs 2,000 Thulium more.
- At **Core level 15** a second bridge builds **Core 3**, and the **Engine Module**, the **Defense Module**, the **Radar Module** and the **Trophies Bay** take its seats: with them the Skylab flies across the universe map and hunts on its own. The step into level 15 costs 4,000 Thulium more. [See Expeditions](#expeditions).
- **Solar makes only 25% of its power while it upgrades**, so your farms and collectors stop until it is done. [Plan it](#timing-a-solar-upgrade).

## Overview

The Skylab runs on its own clock, apart from your ship: modules produce and forge while you are away. What you do is build, upgrade, keep the power in balance and collect. The page has four views of the same station: **Station** (the 3D station, with a chip over every module; click one to open its sheet, or press **1** to **9**), **List** (a card for each module), **Table** (every module's numbers in one table) and **Research** (the Research Centre's own screen, see [Research](/wiki/03-Mechanics/Research.md)). Hovering **Build** or **Upgrade** shows what the next level changes, what it costs and how long it takes. The **Universe** button in the page's header opens the map of the Expedition (see [Expeditions](#expeditions)).

Sixteen modules make up the station:

| Module | Makes or does | Built from |
| :--- | :--- | :--- |
| **Core** | Sets the highest level of every other module | Always there |
| **Solar** | Makes power | Any Core level |
| **Credit Farm** | Makes [Credits](/wiki/01-General/Getting-Started.md) | Any Core level |
| **Thulium Farm** | Makes [Thulium](/wiki/01-General/Getting-Started.md) | Any Core level |
| **Velkonite Collector** | Mines Velkonite ore | Core level 5 |
| **Orvium Collector** | Mines Orvium ore | Core level 5 |
| **Resource Storage** | Keeps the ore | Core level 5 |
| **Forgery** | Forges ore into plates | Core level 5 |
| **Research Centre** | Turns resources into science and researches [technologies](/wiki/03-Mechanics/Research.md) | Core level 10 |
| **Ammo Printer** | Prints x2, x3 or x4 ammo from nothing | Core level 10, on Core 2 |
| **Rocket Factory** | Builds Shop rockets from nothing | Core level 10, on Core 2 |
| **Ore Bay** | Moves the Velkonite and the Orvium you carry into the Resource Storage | Core level 10, on Core 2 |
| **Engine Module** | Holds the engines that fly the Skylab | Core level 15, on Core 3 |
| **Defense Module** | Holds the lasers and the magazine that fight on an expedition | Core level 15, on Core 3 |
| **Radar Module** | Scans the fog of the universe map | Core level 15, on Core 3 |
| **Trophies Bay** | Keeps what the expeditions bring back | Core level 15, on Core 3 |

The two **bridges**, **Core 2** and **Core 3** are not modules: the first bridge and Core 2 appear when the Core reaches level 10, the second bridge and Core 3 at level 15, and neither Core has a level of its own (see [The bridge and Core 2](#the-bridge-and-core-2) and [The second bridge and Core 3](#the-second-bridge-and-core-3)).

**Missions for it.** Ten [Station missions](/wiki/03-Mechanics/Quests.md#station-missions) in Mission Control walk you through the Skylab: build Solar, a Credit Farm and a Thulium Farm, raise the Core and Solar, collect your first 50,000 credits and open the supply chain, and pay a little for each step. The first is open from level 1.

## The station at every level

These are the Skylab's Station view at each level from 1 to 20, all from the same angle, with every module at the same level. The view fits the whole station into the picture, so the scale is not the same in all of them: it jumps when the shape grows. The station grows in steps: its shape changes at **levels 1, 5, 10, 15 and 20**, and in between every level lights **one more lamp** on each module's collar (the number of lit lamps is the level, and the Core's ring of twenty lamps fills up the same way).

These pictures show the **first Core** and what hangs on it, with Solar beside it, as the station stood before the bridges. The station goes on past it, and the pictures do not show that part: from level 10 a bridge, Core 2 and the Ammo Printer, the Rocket Factory and the Ore Bay stand beyond it, and Solar moves to the far end (see [The bridge and Core 2](#the-bridge-and-core-2)); from level 15 a second bridge, Core 3 and the four modules of the Expedition stand beyond that (see [The second bridge and Core 3](#the-second-bridge-and-core-3)). The Station view of the page shows the whole station.

**Levels 1 to 4.** The first four modules around the Core: Solar, the Credit Farm, the Thulium Farm and the docking bay that holds your ship. The supply chain cannot be built yet.

![Level 1](../img/skylab/wiki/level-01.jpg)
![Level 2](../img/skylab/wiki/level-02.jpg)
![Level 3](../img/skylab/wiki/level-03.jpg)
![Level 4](../img/skylab/wiki/level-04.jpg)

**Levels 5 to 9.** With Core level 5 the supply chain can be built: the two collectors on their rigs above the station, the Resource Storage at the Core's north-east port and the Forgery at its north-west port (they are shown here as built).

![Level 5](../img/skylab/wiki/level-05.jpg)
![Level 6](../img/skylab/wiki/level-06.jpg)
![Level 7](../img/skylab/wiki/level-07.jpg)
![Level 8](../img/skylab/wiki/level-08.jpg)
![Level 9](../img/skylab/wiki/level-09.jpg)

**Levels 10 to 14.** The Core wears its ring, the farms and the collectors take their bigger form and the Thulium Farm gets its own ring.

![Level 10](../img/skylab/wiki/level-10.jpg)
![Level 11](../img/skylab/wiki/level-11.jpg)
![Level 12](../img/skylab/wiki/level-12.jpg)
![Level 13](../img/skylab/wiki/level-13.jpg)
![Level 14](../img/skylab/wiki/level-14.jpg)

**Levels 15 to 19.** The farms fill out with crates and crystals, the docking bay lights its approach and the Solar array grows its top. At level 15 the station also grows past the picture, by a second bridge and Core 3.

![Level 15](../img/skylab/wiki/level-15.jpg)
![Level 16](../img/skylab/wiki/level-16.jpg)
![Level 17](../img/skylab/wiki/level-17.jpg)
![Level 18](../img/skylab/wiki/level-18.jpg)
![Level 19](../img/skylab/wiki/level-19.jpg)

**Level 20.** The top of the ladder: the crown on the Core and the full-grown towers of the farms and the supply chain.

![Level 20](../img/skylab/wiki/level-20.jpg)

**The cards of the nine modules.** The List view of the same station at level 20: the four modules of the first release, the Velkonite Collector, Orvium Collector, Resource Storage and Forgery that came with the supply chain, and the Research Centre. Each card shows the module's level, its output, its power and its switch. Every card reads level 20 except the Research Centre's: it has levels 1 to 10, so its card reads level 10, its top. The cards of the Ammo Printer, the Rocket Factory and the Ore Bay are in the same view and are described [below](#the-bridge-and-core-2), and so are the four cards of the Expedition's modules, in [The second bridge and Core 3](#the-second-bridge-and-core-3).

![The List view at level 20: the cards of the Core, Solar, Credit Farm, Thulium Farm, Velkonite Collector, Orvium Collector, Resource Storage, Forgery and Research Centre](../img/skylab/wiki/modules.jpg)

## The first four modules

### Core Module

The heart of your Skylab. The level of the Core decides the highest level of every other module: you cannot upgrade any module higher than your Core. The Core goes up to level 20, and from **level 5** it opens the supply chain below. Its upgrades cost Credits, the step into **level 10** costs **2,000 Thulium** more and builds the bridge and Core 2 (see [The bridge and Core 2](#the-bridge-and-core-2)), and the step into **level 15** costs **4,000 Thulium** more and builds a second bridge and Core 3 (see [The second bridge and Core 3](#the-second-bridge-and-core-3)). In all it takes 112,326 Credits up to level 10 and 6,647,504 up to level 20, plus those 6,000 Thulium, and about 16 and a half days (see [Upgrade times](#upgrade-times)).

### Solar Module

Power is the lifeblood of the Skylab. The Solar Module makes the energy that every other module uses.

- **Importance**: if your power use is higher than your power made, your farms and collectors shut down.
- **Power made**: a Solar module at level N makes enough for **every other module at level N**, and about a tenth more: 255 at level 1, 965 at level 7, 18,575 at level 20. Level 7 Solar powers a whole station at level 7 (see Power Management for every level).
- **Price**: building Solar costs **500 Credits and 50 Thulium**. Its upgrades cost the same and take as long as the Forgery's: from 8,000 Credits and 25 Thulium for level 2 (5 minutes) to 9,000,000 Credits and 10,000 Thulium for level 20 (24 hours).
- **Upgrading**: while Solar upgrades it makes only **25%** of the power of its current level, and the new level's power from the moment the upgrade ends. A station that uses more than that stops: every farm and collector stops producing and the Forgery starts no new batch until the upgrade is done. For nearly every station this is the case: it runs through the upgrade only if all the other modules are at least five levels below Solar (six levels from Solar level 10). Plan a Solar upgrade like a blackout of your farms (see Building and Upgrading).
- **Place**: Solar stands at the far end of the station: on Core 2 from Core level 10 and on Core 3 from level 15 (see [The bridge and Core 2](#the-bridge-and-core-2) and [The second bridge and Core 3](#the-second-bridge-and-core-3)).

### Credit Farm and Thulium Farm

- **Credit Farm**: makes Credits over time: **2,250 an hour at level 1, 225,000 at level 20** (level 5: 11,250; level 10: 33,750; level 15: 76,500). It costs nothing to build.
- **Thulium Farm**: makes Thulium over time: **40 an hour at level 1, 1,280 at level 20** (level 5: 144; level 10: 360; level 15: 760). Building it costs 5,000 Credits and 500 Thulium.
- Both need power, and each holds 72 hours of what it makes until you collect it.

## The supply chain

Four modules turn time spent away from the keyboard into the plates for your best lasers. Ore comes **only** from the collectors (all the materials and currencies are on the [Resources](/wiki/06-Items/Resources.md) page): aliens do not drop it and the Shop does not sell it. (A [giant excavator](/wiki/03-Mechanics/Giant-Excavator.md) also lays some Velkonite and Orvium in boxes, but that ore goes to your cargo, and only the [Ore Bay](#ore-bay) moves it into the Resource Storage, from where the Forgery and the Research Centre take it.)

1. A **collector** mines ore, an amount an hour, into its own hopper (72 hours' worth).
2. **Collect** moves the ore from the hopper into the **Resource Storage**, the bank, where each ore is kept apart.
3. The **Forgery** takes the ore it needs from the bank when a batch starts, and makes plates, 10 seconds a plate, one batch at a time.
4. **Collect plates** moves the finished plates into your inventory (your ship must be landed). [Assembly](/wiki/06-Items/Lasers.md) turns them into a Quantum Laser III, a Starfire-III or a Helios Beam, and, one of each with 5 Dark Matter, into a Dark Matter Plate, which [The Forge](/wiki/06-Items/Forge.md) and the last tier of every upgrade chain ask for.

### Velkonite Collector and Orvium Collector

- **Ore**: the Velkonite Collector mines **10 Velkonite an hour** at level 1 and the Orvium Collector **10 Orvium an hour**, and every level has its own rate: up to 80 Velkonite and 40 Orvium an hour at level 20 (level 5: 18 and 14 an hour; level 10: 32 and 24).
- **Hopper**: each holds 72 hours of its ore and stops mining when it is full.
- **Collect**: moves the ore into the Resource Storage, as far as it has room. With no storage built, or with that ore's bank full, there is nowhere to put it and the button says why. The rest stays in the hopper.
- **Power**: 20 (Velkonite) and 30 (Orvium) at level 1, growing by 15% a level.

### Resource Storage

- **Bank**: keeps Velkonite and Orvium apart, and holds a different amount of each: **240 of each at level 1**, up to 7,680 Velkonite and 3,840 Orvium at level 20 (level 5: 720 and 560; level 10: 1,920 and 1,440).
- **Cap**: one day of its collector's output at level 1, growing to four days at level 20. A collector's hopper holds three days, so from level 13 on the bank holds at least a full hopper.
- **Above the cap**: if a bank holds more than its cap (the payout of the 0.4.10 update could leave one so), nothing is taken away, but Collect adds no more of that ore until you have used some of it.
- Ore goes in by collecting from a collector, or from your inventory through the [Ore Bay](#ore-bay), and out only into the Forgery and the Research Centre. It never comes back to your inventory.
- **The banked ore stays** through the season wipe.
- **Power**: 10 at level 1, growing by 10% a level. It cannot be switched off.

### Forgery

- **Plates**: the Forgery makes a **Velkonite Reinforced Plate** from Velkonite and an **Orvium Reinforced Plate** from Orvium: **40 Velkonite** or **80 Orvium** a plate at level 1, falling with every level to 30 and 60 at level 20 (never below 75%).
- **Batches**: one batch of one kind of plate at a time, **10 plates at level 1** and 5 more for every level above. The ore leaves the Resource Storage the moment the batch starts, and each plate takes **10 seconds**. The plates are made one after the other, also while you are away.
- **Collect plates**: moves the finished plates into your inventory while your **ship is landed**, and the rest of the batch keeps running. A new batch can start once the Forgery is empty.
- A batch that is running finishes even if you switch the Forgery off or upgrade it. A **new** batch needs the Forgery switched on, not being upgraded, and the Skylab's power in balance.
- **Power**: 30 at level 1, growing by 15% a level.
- **Not Marketable**: the plates the Forgery makes can't be sold on the [Auction](/wiki/03-Mechanics/Auction.md#marketable-items), or they would be the biggest good of its Market. They are still material for the Assembly and the Forge.

### Building them

The two collectors cost **10 Ship Fragments, 20,000 Credits and 500 Thulium** each, the Resource Storage **10 Ship Fragments, 5,000 Credits and 250 Thulium** and the Forgery **10 Ship Fragments, 5,000 Credits and 500 Thulium**; all four need Core level 5.

- The Ship Fragments are taken from your inventory (not from the Transport Cache) and your ship must be landed. The build sheet shows what you have against what it takes, and what you lack.
- They draw power. Before you build, the sheet shows your power balance now and after: **building can put a station into a deficit** when its Solar is behind the other modules, and one deficit stops every farm and collector. Switch a module off, or upgrade Solar first.
- The two collectors hang on rigs above the station, the Resource Storage sits at the Core's north-east port and the Forgery at its north-west port.

## The Research Centre

The ninth module turns resources into science and researches the technologies that Assembly needs before it will make anything new. It is built from Core level 10, has levels 1 to 10, draws power and cannot be switched off. Its numbers, what it burns as fuel, the boost and the whole technology tree are on the [Research](/wiki/03-Mechanics/Research.md) page. The highest technologies also need Dark Matter, which you add to the Centre: [Dark Matter and Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md) says how to get it. The levels of the Engine, Defense and Radar Modules are technologies too, researched here (see [Research](/wiki/03-Mechanics/Research.md#module-technologies)).

## The bridge and Core 2

The Core's upgrade into **level 10** builds a **bridge** and a second Core. The bridge docks at the Core's north port, where Solar stood, and joins it to **Core 2** at the far end.

- **Cost**: the step from level 9 to level 10 costs **2,000 Thulium** on top of its 38,443 Credits, and takes the same 1 h 20 min as before. The bridge and Core 2 cost nothing more and take no time of their own. An upgrade that was already running keeps the price it was started at, and a Core that is at level 10 or higher pays nothing.
- **Core 2 has no level**: there is nothing to upgrade or pay. It gives your station **six more module seats**, and the Core's card shows how many are free.
- **Solar moves**: Solar leaves the Core's north port, which the bridge now takes, for Core 2's north port at the far end of the station. Its level, its power and an upgrade in progress are untouched.
- **A rule, not a build**: where each module sits follows from the Core's level alone. The bridge appears the moment the Core's upgrade into level 10 is done (a quiet sound and a message tell you), and a Skylab whose Core is already at level 10 or higher has it at the next look. No module is lost or deleted, and only Solar changes its seat.
- **Seats**: the **Ammo Printer** takes Core 2's north-east seat, the **Rocket Factory** its north-west seat and the **Ore Bay** its east rig; the other three stay free for modules to come. All three can be built only once Core 2 stands: before that the Build button reads "Needs Core 2".
- **Levels**: a module on Core 2 follows the Core's level like every other module: none goes above the Core, so Core 2 adds seats, not levels.

### Ammo Printer

The Ammo Printer prints laser ammo from nothing, one kind at a time: no ore and no Credits, only power. It has levels 1 to 20.

- **Output**: **x2** (Advanced Plasma) **100 an hour at level 1, 2,000 at level 20** (100 more every level); **x3** (Ultra Core) half of that, 50 to 1,000; **x4** (Experimental Fusion Core) a quarter, 25 to 500.
- **Mode**: you pick x2, x3 or x4 on its card or sheet. A switch keeps the hours already stored and reads them at the new mode's rate from then on.
- **Store**: one day, 24 hours of production at the level and kind in use (2,400 x2 at level 1, 48,000 at level 20). Offline time counts, and a full store just stops.
- **Collect**: moves the whole units into your inventory while your **ship is landed**. Ammo has no carry limit, and a part of a unit stays and counts on.
- **Power**: 40 at level 1, growing by 20% a level. In a blackout it stops like the farms and collectors, and what it holds stays and can be collected.
- **Building**: 20,000 Credits, 500 Thulium and 10 Ship Fragments (from your inventory, with your ship landed), on Core 2 only. Its upgrades cost from 21,000 Credits and 140 Thulium to 5,600,000 Credits and 11,000 Thulium and take as long as the Forgery's, 5 minutes to 24 hours and 5 d 13 h in all (see the tables below).
- **Not Marketable**: what it prints can't be sold on the [Auction](/wiki/03-Mechanics/Auction.md#marketable-items).

### Rocket Factory

The Rocket Factory builds Shop rockets from nothing, one kind at a time. It has levels 1 to 20.

- **What it makes**: any one of the twelve Shop rockets, as you pick it: Lancet, Rivet, Scatter or Ember, tiers I, II and III. The N.U.K.E. and the N.I.K.E. are never made.
- **Output**: tier III **0.5 an hour at level 1, 10 at level 20** (0.5 more every level), tier II 1.25 times that and tier I twice that. Only whole rockets count: a part of one stays and counts on.
- **Store**: one day, 24 hours of production at the level and rocket in use (240 tier III at level 20). Offline time counts, a full store just stops, and a switch of rocket keeps the hours already stored.
- **Collect**: moves the rockets into your inventory while your **ship is landed**, as many as you can carry: at most 5,000 of a tier I rocket, 2,000 of a tier II and 500 of a tier III, the Shop's own limit. What does not fit stays in the Factory.
- **Power**: 24 at level 1, growing by 15% a level. In a blackout it stops like the Printer.
- **Building**: 20,000 Credits, 500 Thulium and 15 Ship Fragments (from your inventory, with your ship landed), on Core 2 only. Its upgrades cost a quarter of the Printer's, from 5,300 Credits and 35 Thulium to 1,400,000 Credits and 2,800 Thulium, and take as long: 5 d 13 h in all.
- **Not Marketable**: what it builds can't be sold on the [Auction](/wiki/03-Mechanics/Auction.md#marketable-items).

### Ore Bay

The Ore Bay moves the ore you carry into the Resource Storage. A [giant excavator](/wiki/03-Mechanics/Giant-Excavator.md) lays Velkonite and Orvium in boxes that go into your cargo, where no module uses them; the Ore Bay is the way from there into the bank, from which the Forgery and the Research Centre take it. It has levels 1 to 20.

- **What it moves**: **Velkonite and Orvium**, the two ores the Resource Storage keeps. Cataclysite and Quorvium are fuel that the Research Centre and the [Forge](/wiki/06-Items/Forge.md) take straight from your inventory, and Thulium goes to your wallet when you pick it up.
- **One way**: from your inventory into the Resource Storage, never back out. Only the loose ore in your inventory moves, never what is in the Transport Cache.
- **How**: your **ship must be landed**. A transfer is instant: on the Ore Bay's sheet choose the ore, type an amount or press Max, and press **Move**. The sheet shows what you carry and what the bank holds against its capacity.
- **Allowance**: the level sets how much ore it moves an hour, **30 at level 1, 960 at level 20**, and it keeps up to a day of it (720 at level 1, 23,040 at level 20). A new Ore Bay starts with a full day, and an upgrade keeps what was stored. A transfer is cut at the ore you carry, at the room the Resource Storage has left and at the allowance, and says which. A day of the allowance is about three times what the Resource Storage holds of one ore at the same level, so it is mostly the room that stops a transfer; the allowance matters only if you cycle ore through the storage again and again within a day.
- **Power**: 15 at level 1, growing by 10% a level (92 at level 20). It can be switched off. In a blackout, while it is switched off and while it upgrades it moves nothing.
- **Building**: 5,000 Credits, 250 Thulium and 10 Ship Fragments (from your inventory, with your ship landed), on Core 2 only. Its upgrades cost what the Resource Storage's do and take as long (see the tables below).
- **Not a way to more ore**: it moves ore you already hold. A run of the excavator is capped at its source, and the Resource Storage's own capacity bounds the bank.

## The second bridge and Core 3

The Core's upgrade into **level 15** builds a **second bridge** and a third Core, and the four modules of the Expedition take their seats there. Bridge II docks at Core 2's north port, where Solar stood, and joins it to **Core 3** at the far end of the station: the pattern of level 10 once more.

- **Cost**: the step from level 14 to level 15 costs **4,000 Thulium** on top of its Credits, and takes the same 14 h as before. Bridge II and Core 3 cost nothing more and take no time of their own. An upgrade that was already running keeps the price it was started at, and a Core that is at level 15 or higher pays nothing.
- **Core 3 has no level**: there is nothing to upgrade or pay. It gives your station **four more module seats**, and the Core's card shows how many are free.
- **Solar moves again**: Solar leaves Core 2's north port, which bridge II now takes, for Core 3's north port at the far end of the station. Its level, its power and an upgrade in progress are untouched.
- **A rule, not a build**: where each module sits follows from the Core's level alone. Core 3 appears the moment the Core's upgrade into level 15 is done, and a Skylab whose Core is already at level 15 or higher has it at the next look. No module is lost, and only Solar changes its seat.
- **Seats**: the **Defense Module** takes Core 3's north-east seat, the **Radar Module** its north-west seat, the **Trophies Bay** its east rig and the **Engine Module** its west rig. Its two south ports face the modules of Core 2 and stay empty. All four can be built only once Core 3 stands: before that the Build button is locked and says it needs Core level 15.
- **Levels**: a module on Core 3 follows the Core's level like every other: none goes above the Core. The Engine and Defense Modules stop at level 5, the Radar Module at level 3 and the Trophies Bay at level 20.
- **What a build asks for**: besides Credits and Thulium, **Ship Fragments** and, for the Engine, Defense and Radar Modules, **Dark Matter Plates** from your inventory (not from the Transport Cache), taken with your ship landed, and the **technology** of the level, researched in the Research Centre. A step that asks for plates asks for them the same way.

**The technologies.** Each level of the Engine, Defense and Radar Modules is a technology of the Skylab family in the Research view, researched in turn and needed before that level can be built or upgraded to. The three modules share the times (the Radar Module stops at level 3):

| Level | Research time | Dark Matter |
| :--- | ---: | ---: |
| 1 | 3 h | 0 |
| 2 | 10 h | 5 |
| 3 | 1 d | 10 |
| 4 | 2 d | 15 |
| 5 | 3 d | 20 |

The technologies of the three modules ask 115 Dark Matter and 14 d 15 h of research at the normal rate (see [Research](/wiki/03-Mechanics/Research.md#module-technologies)).

### Engine Module

The Engine Module holds the engines that fly your Skylab. It has levels 1 to 5, and each level takes one more engine. The engines you fit, and the weight of the whole station, decide how fast it flies (see [Weight and speed](#weight-and-speed)).

- **What fits**: [Engine](/wiki/06-Items/Propulsion.md) items with their thrusters in them, from your inventory: an Engine I, II or III. An Adaptive Core does not fit: its speed bonus is a ship's affair. An engine keeps its thrusters and its Forge buffs when you take it out again.
- **How**: your **ship must be landed** and the Skylab must not be under way. The Engine card of the Universe window lists your loose engines: drag one onto a free slot, or click it, and click a fitted engine to take it out. The card also shows the thrust, the weight, the speed and how long a hop takes.
- **A trip needs**: the module built, switched on, not being upgraded and holding at least one engine.
- **Research**: every level needs its own technology, Engine Module I to V (see the table above).
- **Power**: 60 at level 1, growing by 25% a level. It can be switched off, but not while the Skylab is under way.
- **Building**: 375,000 Credits, 1,500 Thulium, 20 Ship Fragments and 1 Dark Matter Plate, on Core 3 only.
- **Upgrading**: the module is offline while it upgrades. The upgrade of the Engine Module waits for the end of a trip, because the speed of a trip is fixed when it leaves.

| Level | Engines | Credits | Thulium | Plates | Time |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 1 (the build) | 1 | 375,000 | 1,500 | 1 | – |
| 2 | 2 | 825,000 | 3,300 | 2 | 2 h |
| 3 | 3 | 1,825,000 | 7,300 | 3 | 6 h |
| 4 | 4 | 4,000,000 | 16,000 | 5 | 1 d |
| 5 | 5 | 8,750,000 | 35,000 | 8 | 2 d |

The plates are Dark Matter Plates, and the time is the upgrade into the level. In all the five levels take 15,775,000 Credits, 63,100 Thulium, 19 plates and 3 d 8 h of upgrading.

### Defense Module

The Defense Module fights for your Skylab. It holds the lasers that shoot the aliens of the cells your Skylab flies to and the magazine they fire from. It has levels 1 to 5, and its level decides how many lasers it holds, how many rounds, what it may earn an hour and how dangerous a cell it may enter.

- **What fits**: [Laser](/wiki/06-Items/Lasers.md) items with their amps in them, from your inventory: a Quantum Laser I, II or III, a Starfire-III or a Helios Beam. All the lasers fire together, one round each a second. The amps count as they do on a ship (damage, crit chance and crit damage); a Penetration Amp adds nothing here.
- **The magazine** holds rounds of the Ammo Printer's kinds and is filled **only from the Ammo Printer**, never from your inventory (see [Fits and ammunition](#fits-and-ammunition)).
- **The gate**: a cell of difficulty 3, say, can be entered only by a Skylab whose Defense Module is at level 3 or higher. A Skylab with no Defense Module may fly through empty space and its port only.
- **The kill budget** is the most the Skylab may earn an hour: 108 bounty points at level 1 and 630 at level 5 (see [What a trip pays](#what-a-trip-pays)).
- **The hull** grows with the level (see [The hull, destruction and repair](#the-hull-and-repair)).
- **Research**: every level needs its own technology, Defense Module I to V (see the table above).
- **Power**: 80 at level 1, growing by 25% a level. It can be switched off, but not while the Skylab is under way. A module that is switched off, being upgraded or without power is dark: the Skylab fights nothing and passes the cells unfought.
- **Building**: 500,000 Credits, 2,000 Thulium, 25 Ship Fragments and 1 Dark Matter Plate, on Core 3 only.

| Level | Lasers | Magazine (rounds) | Kill budget (points an hour) | Highest difficulty |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 1 | 1,300 | 108 | 1 |
| 2 | 2 | 3,600 | 293 | 2 |
| 3 | 3 | 14,000 | 476 | 3 |
| 4 | 4 | 23,000 | 548 | 4 |
| 5 | 5 | 35,000 | 630 | 5 |

| Level | Credits | Thulium | Plates | Time |
| :--- | ---: | ---: | ---: | ---: |
| 1 (the build) | 500,000 | 2,000 | 1 | – |
| 2 | 1,150,000 | 4,600 | 2 | 3 h |
| 3 | 2,750,000 | 11,000 | 4 | 9 h |
| 4 | 6,000,000 | 24,000 | 7 | 1 d 12 h |
| 5 | 14,000,000 | 56,000 | 12 | 3 d |

In all the five levels take 24,400,000 Credits, 97,600 Thulium, 26 plates and 5 d of upgrading.

### Radar Module

The Radar Module lifts the fog of the universe map (see [Fog and scanning](#fog-and-scanning)). It has levels 1 to 3, and a higher level scans a cell faster.

- **What it does**: it scans **one cell at a time**, among the cells next to a cell you know, and keeps a **line of three**: the first is being scanned and the others wait. When a scan is done you know the cell, and your Skylab may fly there.
- **Time**: 90 minutes a cell at level 1, 40 at level 2 and 15 at level 3. A scan runs on the server's clock, also while you are away and while the Skylab flies. It stands still, and the time is not made up, while the module is switched off, being upgraded or without power and while the Skylab is destroyed. A scan costs time and nothing else.
- **Charting everything**: to chart the 131 cells you do not know at the start, one after the other, takes 8 d 4 h at level 1, 3 d 15 h at level 2 and 1 d 9 h at level 3.
- **Research**: every level needs its own technology, Radar Module I to III (see the table above).
- **Power**: 40 at level 1, growing by 30% a level. It can be switched off, but not while the Skylab is under way.
- **Building**: 250,000 Credits, 1,000 Thulium and 15 Ship Fragments, on Core 3 only.

| Level | Scan time | Credits | Thulium | Plates | Time |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 1 (the build) | 90 min | 250,000 | 1,000 | 0 | – |
| 2 | 40 min | 750,000 | 3,000 | 1 | 4 h |
| 3 | 15 min | 2,250,000 | 9,000 | 3 | 1 d |

In all the three levels take 3,250,000 Credits, 13,000 Thulium, 4 plates and 1 d 4 h of upgrading.

### Trophies Bay

The Trophies Bay keeps what your Skylab's kills bring until you collect it. It has levels 1 to 20, and it needs no technology.

- **What it holds**: Credits, Thulium, experience, honor and the loot of the kills.
- **Capacity** is counted in **bounty points**: a kill adds the bounty of its alien, Credits divided by 200 plus Thulium, whatever it drops (Alpha's figures in every world). It holds 650 points at level 1 and 45,000 at level 20.
- **Full**: a full Bay makes the Skylab **hold fire**: nothing is killed, paid or counted and no ammunition is spent until you collect (the hull still mends). A message, a toast, an amber **Bay full** pill on the station's bar, a notice on the Skylab page and the tip of the sidebar's Skylab row say so.
- **Collect** in the Universe window, with your ship landed: Credits and Thulium go to your account, experience and honor to your pilot and the loot to your inventory. Two collects at once pay once.
- **Loot** is rolled for each kill from the alien's drops, never Dark Matter, Ancient Control Units, N.I.K.E.s or N.U.K.E.s. It is **not Marketable**: it can't be sold on the [Auction](/wiki/03-Mechanics/Auction.md#marketable-items).
- **Power**: 20 at level 1, growing by 10% a level. It can be switched off, but not while the Skylab is under way.
- **Building**: 100,000 Credits, 400 Thulium and 10 Ship Fragments, on Core 3 only. Its upgrades cost from 117,500 Credits and 470 Thulium (15 minutes) to 2,325,000 Credits and 9,300 Thulium (1 d 13 h): 14,722,500 Credits and 58,890 Thulium in all, and 6 d 8 h.

| Level | Capacity (points) | Credits | Thulium | Time |
| :--- | ---: | ---: | ---: | ---: |
| 1 (the build) | 650 | 100,000 | 400 | – |
| 2 | 810 | 117,500 | 470 | 15 min |
| 5 | 1,600 | 195,000 | 780 | 34 min |
| 10 | 4,800 | 450,000 | 1,800 | 2 h 18 min |
| 15 | 15,000 | 1,025,000 | 4,100 | 9 h 14 min |
| 20 | 45,000 | 2,325,000 | 9,300 | 1 d 13 h |

How long a Bay takes to fill when the Skylab earns the whole kill budget of its Defense level (a smaller Bay fills faster, a smaller budget slower):

| Defense level | Bay level 1 | Bay level 5 | Bay level 10 | Bay level 15 | Bay level 20 |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 1 | 6 h 1 min | 14 h 49 min | 1 d 20 h | 5 d 19 h | 17 d 9 h |
| 2 | 2 h 13 min | 5 h 28 min | 16 h 23 min | 2 d 3 h | 6 d 10 h |
| 3 | 1 h 22 min | 3 h 22 min | 10 h 5 min | 1 d 8 h | 3 d 22 h |
| 4 | 1 h 11 min | 2 h 55 min | 8 h 46 min | 1 d 3 h | 3 d 10 h |
| 5 | 1 h 2 min | 2 h 32 min | 7 h 37 min | 23 h 49 min | 2 d 23 h |

## Weight and speed

Every module weighs something, in **mass units (MU)**, and a heavier station flies slower. A module weighs more with each level, one that is not built weighs nothing and one that is being upgraded weighs the level it has. The engines and lasers you fit are not counted: the module's weight covers them.

| Module | Level 1 | Level 5 | Level 10 | Level 15 | Top level |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Core | 100 | 148 | 208 | 268 | 328 |
| Solar | 60 | 84 | 114 | 144 | 174 |
| Credit Farm | 60 | 84 | 114 | 144 | 174 |
| Thulium Farm | 80 | 118 | 166 | 214 | 262 |
| Velkonite Collector | 70 | 92 | 120 | 148 | 176 |
| Orvium Collector | 70 | 92 | 120 | 148 | 176 |
| Resource Storage | 70 | 92 | 120 | 148 | 176 |
| Forgery | 80 | 112 | 152 | 192 | 232 |
| Research Centre | 60 | 89 | 125 | – | 125 |
| Ammo Printer | 60 | 84 | 114 | 144 | 174 |
| Rocket Factory | 60 | 84 | 114 | 144 | 174 |
| Ore Bay | 40 | 53 | 69 | 85 | 101 |
| Engine Module | 80 | 144 | – | – | 144 |
| Defense Module | 100 | 180 | – | – | 180 |
| Radar Module | 30 | – | – | – | 39 |
| Trophies Bay | 50 | 60 | 73 | 85 | 98 |
| **The whole station: every module that stands at that Core level, at that level** | 300 | 824 | 1,537 | 2,353 | 2,734 |

The top level is 20, but for the Research Centre (10), the Engine and Defense Modules (5) and the Radar Module (3). The whole station weighs 2,353 MU at Core level 15 and 2,734 MU at level 20.

- **Thrust** is the engines' own arithmetic of the ships, without a base speed: an engine adds its base speed plus the flat speed of its thrusters, times their multipliers; the engines are ranked best first and the first four count 100% and the fifth 85% (the module holds five at most); and the four best speed bonuses are added on top. A station with no engine has no thrust.
- **Speed** is 60 times the thrust over the weight of the station, in units a second, and a hop between two neighbouring cells is 15,000 units. Under the power, the Skylab page shows the line "Weight 2,353 MU, speed 7.8 units/s, a hop 32 min".
- **Fixed at departure**: a trip's speed is worked out when it leaves, from the weight and thrust of that moment. An upgrade that ends on the way, or an engine you change while the Skylab is stationed, counts for the next trip.

What engines do for a station with every module at level 15 (the Engine Module at the level that holds the engines):

| Engines fitted | Weight (MU) | Thrust | Speed (units a second) | One hop | Across the map (14 hops) |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 1 Engine I (Engine Module level 1) | 2,289 | 2.0 | 0.05 | 3 d 6 h | 45 d 11 h |
| 3 Engine II, each with 2 Impulse Thruster II (level 3) | 2,321 | 73.6 | 1.90 | 2 h 11 min | 1 d 7 h |
| 5 Engine III, each with 3 Impulse Thruster IV (level 5) | 2,353 | 305.5 | 7.79 | 32 min | 7 h 29 min |

At Core level 20 the station weighs 16% more, and the best engines take 37 minutes a hop and 8 h 42 min across the map.

## Expeditions

An **expedition** is a trip of your Skylab across the **universe map**. It flies to a cell, hunts the aliens there with the lasers of its Defense Module and fills the Trophies Bay with what the kills bring. It all runs on the server's clock, so it goes on while you are logged out, and no player can attack the Skylab: what hurts it is only the danger of the cell (see [The hull, destruction and repair](#the-hull-and-repair)). You plan a trip in the **Universe** window, which the Universe button in the Skylab page's header opens.

What it takes: a Core at level 15, a company (its port is your Skylab's home) and a world; for a trip, an Engine Module with an engine fitted; to earn anything, a Defense Module with a laser and ammunition from your Ammo Printer, and a Trophies Bay to keep it in. Everything else goes on while the Skylab is away: the farms, the collectors, the Forgery, the Printer, the Factory, the Ore Bay and the Research Centre run on their own clocks, and your ship can be flown as usual.

### The universe map

The map is the Skylab's **own layer**, not the game's sectors and not a view of them: its cells are not game maps, the gates are not on it, nothing on it is flown in real time and its aliens are only a count and a danger. It touches the rest of the game through what it pays: Credits, Thulium, experience, honor, loot and mission kills.

- **The field**: 15 columns and 10 rows of hexagonal cells, **150 in all**. A cell has a code, the column's letter and the row's number (A1 to O10), and, once you know it, a name and a kind.
- **Ports**: each company has one **port**, a cell of difficulty 0: Mars's is H3, Terra's D8 and Galactic's L8. Your Skylab starts in your company's port and comes back there after a wipe. Nothing is hunted at a port and nothing attacks the Skylab in it.
- **Difficulty** runs from 1 to 5 and grows with the distance from the nearest port: the six cells next to a port are always difficulty 1, and every hop away adds one, up to 5. About a fifth of the cells are a step easier than their distance says and a quarter a step harder, and a few are **empty space**, difficulty 0.
- **Kinds**: a **nest** holds all the aliens of its difficulty and a **drift**, most of the cells, three fifths of them. Empty space holds nothing and nobody, and a Skylab may fly through it with no Defense Module at all.
- **One map for a world**: every pilot of a world sees the same map, each world has its own, and every season (the wipe) makes a new one.

The aliens of a nest, by difficulty (a drift holds three fifths of them, rounded):

| Difficulty | Aliens |
| :--- | :--- |
| 1 | 30 [Seekers](/wiki/04-Aliens/Seeker.md) |
| 2 | 20 Seekers and 10 [Phantasms](/wiki/04-Aliens/Phantasm.md) |
| 3 | 20 Phantasms, 10 [Bulwarks](/wiki/04-Aliens/Bulwark.md) and 5 [Goombahs](/wiki/04-Aliens/Goombah.md) |
| 4 | 20 Bulwarks, 10 Goombahs and 5 [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| 5 | 6 [Slumbering Voids](/wiki/03-Mechanics/Dormant-Swamp.md), 3 [Dormant Pulses](/wiki/05-Swarms/Dormant-Swarm.md) and 1 Dormant Force |

### Fog and scanning

You see only the cells you know.

- **At the start of a season** you know your port and the two rings of cells round it: **19 cells**, the same for every company.
- **A cell becomes known** when your Skylab flies through it or stops in it, and when the Radar finishes scanning it.
- **A cell you do not know** shows nothing of itself: not its kind, its difficulty, its name or its aliens. A cell next to a known cell is marked with a **?** and can be scanned; any other unknown cell is dark.
- **A known cell** shows its code, kind, difficulty, name and aliens in its panel.
- **Flying** is only into known cells.
- **Scanning**: pick a **?** cell and press **Scan this cell**. The Radar scans one cell at a time and keeps a line of three; a cell can be taken out of the line again, and **Cancel all** empties it. The time of a scan is on the [Radar Module](#radar-module).

### The trip

Click a known cell on the map: the cell's panel shows the **preview** of the trip, which the server plans with your Skylab as it stands now, and **Depart** sends the Skylab there. It flies one hop at a time at the speed of its engines, arrives in the cell and **hunts there until you give another order**. **Recall** sends it home to its port by the shortest known way.

- **The route** is the fewest hops over cells you know whose difficulty your Defense Module's level allows. Among routes of the same length one is picked, always the same.
- **The clock** is the server's: the arrival is fixed when the Skylab leaves, and a trip goes on while you are logged out. A new order given on the way takes effect at the next cell: the hop it is on is finished.
- **What stops an order**: no Engine Module, or one that is switched off or being upgraded; no engine fitted; not enough power; a Skylab that is destroyed; the cell it is in already; a cell you do not know; a cell too hard for your Defense Module; no known route.
- **Under way**, the four modules of the Expedition cannot be switched, the Engine Module cannot be upgraded and nothing can be fitted or taken out. On the way it meets the aliens of the cells it passes through at half the rate it would if it stayed there.
- **Told**: a message tells you when the Skylab arrives, when it is destroyed or repaired and when its Bay is full, and all four come with a quiet sound of their own.

What the preview says, in the order of its rows (every figure is the server's, for the kit your Skylab has now):

| Row | What it tells |
| :--- | :--- |
| **Length** | the hops and the time of the trip |
| **Arrival** | the moment it would arrive, by your clock |
| **On the way** | about how many aliens it meets on the cells it passes through |
| **Kills an hour** | what the stay kills an hour, and which limit binds: the aliens that come by, the kill budget, your lasers' damage or your ammunition |
| **Bounty an hour** | what those kills are worth, in bounty points |
| **Your damage** | what your lasers deal a second with the best ammunition in the magazine |
| **The cell asks** | the damage at which the hull's regeneration just carries the cell at the rate it pays: with less, the hull falls |
| **Hull** | Holds, or Destroyed after a time |
| **Ammunition** | how long the magazine lasts, or that it is enough for the whole stay |
| **Trophies Bay** | after how long it is full, or that it does not fill at this rate |

Over the rows a **warning** says when the trip would earn nothing: nothing to fight in the cell, no lasers fitted, a magazine that is empty with nothing to feed it, no Trophies Bay, or a Defense Module that is dark.

### What a trip pays

A kill pays what its alien pays in your world: its Credits, Thulium, experience and honor times the world's pay (1, 2 and 3 in Alpha, Beta and Gamma), and its loot. Nothing is added to it: no booster, no premium, no formation bonus, no clan boost and no experience for your drones.

The kills an hour are the least of three limits: the aliens that come by, the **kill budget** of your Defense Module's level, and what your lasers and your ammunition can do. The budget is what keeps an unattended Skylab a supplement to the farms and not a second job: 108, 293, 476, 548 and 630 bounty points an hour at Defense levels 1 to 5, where a point is 1 Thulium or 200 Credits. **A cell pays by its tier**: a Skylab is paid the lower of its Defense level's budget and the budget of the cell's difficulty, so a Defense 5 Skylab in a difficulty 1 cell makes what a Defense 1 one does there.

What a day in a cell pays at most (Alpha; Beta and Gamma pay 1.6 and 2 times as much):

| Difficulty | Bounty points an hour | Kills a day | Thulium a day | Credits a day |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 108 | 288 | 1,152 | 288,000 |
| 2 | 293 | 469 | 3,124 | 780,911 |
| 3 | 476 | 224 | 5,524 | 1,181,375 |
| 4 | 548 | 86 | 5,503 | 1,528,510 |
| 5 | 630 | 32 | 5,255 | 1,972,329 |

A day in a cell is worth about two hours of hunting that cell by hand (3.4 hours in difficulty 4). From difficulty 3 on it is about 30% of what a Thulium Farm of Core level 15 makes in Thulium (18,240 a day) and 0.6 to 1.1 times what a Credit Farm of that level makes in Credits (1,836,000 a day). A difficulty 2 drift holds fewer aliens than its budget pays for and makes a little less.

The **loot** of a kill is rolled from its alien's drops: Ship Fragments, ores, Reinforced Hull Plates and Power Cores, and from difficulty 5 Ultra Core and Experimental Fusion Core ammunition.

### The hull, destruction and repair {#the-hull-and-repair}

The Skylab has a **hull**, a pool of hit points, which **mends 5% of itself an hour**, also under fire. The aliens it fights hurt it, in proportion to how many it fights, how strong they are and how long the fight lasts: the preview tells whether the hull holds and, if not, after how long the Skylab is destroyed. It is 4,000,000 at Core level 15 with the Defense Module at level 1, 12% more with every Core level above 15 and more with a higher Defense level. A Skylab with no Defense Module has the hull of level 1 and fights nothing.

| Defense level | Core level 15 | Core level 20 |
| :--- | ---: | ---: |
| 1 | 4,000,000 | 7,049,367 |
| 2 | 4,800,000 | 8,459,240 |
| 3 | 6,000,000 | 10,574,050 |
| 4 | 8,800,000 | 15,508,607 |
| 5 | 11,200,000 | 19,738,227 |

- **Destroyed**: when the hull runs out, the Skylab is destroyed where it stood, at that moment, and the trip is over. What the Trophies Bay held stays in it. Every producer of the station stops from that moment: the farms, the collectors, the Printer, the Factory and the Ore Bay make nothing, the Forgery starts no new batch and the Research Centre starts no new research (a batch or a research that is already running goes on), and the Radar's scans stand still.
- **Repair**: press **Repair** in the Universe window. It is free and takes **60 seconds**; then the hull is whole and the Skylab is back in the cell its trip began in. Production starts again from the end of the repair. Nothing is lost but the time.
- **Told**: the Skylab page shows a notice, and a pill on the station's bar, while the Skylab is destroyed or being repaired, and the tip of the sidebar's Skylab row says so too.

### Fits and ammunition

**Fitting.** Engines go into the Engine Module and lasers into the Defense Module, one to a slot, taken from the loose items of your inventory: not on a ship, not in the Transport Cache. Fitting and taking out need your **ship landed** and the Skylab **not under way**; a stationed Skylab can be refitted, and the new rates count from that moment. A fitted item keeps its Forge buffs and what is fitted into it (thrusters, amps) and is **reserved**: it cannot be put on a ship, deleted, listed on the Auction, put in the Transport Cache or used by the Forge and the Assembly until you take it out, and the Hangar, the Auction's sell sheet and the Assembly show it dimmed.

**Ammunition.** The magazine holds rounds of the kinds the Ammo Printer makes and fires the **highest multiplier first**, one round a laser a second. It is filled **only from the Ammo Printer**, never from your inventory:

- **Feed from the Ammo Printer** on: what the Printer makes goes into the magazine first, as far as there is room; only the rest waits in the Printer's hopper for you to collect.
- **Feed off**: what the Printer makes waits in its hopper, and **Load** moves what the hopper holds into the magazine, with your ship landed, as far as there is room.
- There is no unloading: rounds are fired or kept.

A Skylab with no lasers, no ammunition or no Trophies Bay fights nothing, and nothing hurts it either.

### Kills and missions {#expedition-kills}

The kills of an expedition advance a **kill step of your missions** only when the step **names no sector**, up to **250 kills a day** (UTC), and only the kills of the alien the step names. A cell is no sector, so a step that names one (`x-1` to `x-4`, `DS-x` or another company's `x-4`) never counts them, not even in a cell of the same difficulty. In practice these are the big hunts of the Challenge line whose aliens live in a cell, and none of the missions for levels 1 to 8. A mission with a time limit, or a step with a hull limit, never counts them either. Only kill steps count: items, visits and stays need you. The Skylab's card in the Universe window says "Expedition kills today: N of 250".

The kills pay no Wipe Points and count for no clan line, no kill statistics and no ranking points (see [Quests](/wiki/03-Mechanics/Quests.md#where-it-counts)).

### Your clan sees it {#clan-skylabs}

The pilots of your clan see where each other's Skylabs are: the **Skylab** column of the Members list gives the cell ("Docked at H3", "H3, to K7 in 3 h 12 min", "Stationed at K7", "Destroyed at H3"), and the Universe window draws them as small gold diamonds, with the pilot's name when you point at one. Only the clan sees it, a cloak does not hide a Skylab and there is no switch to hide it. A destruction shows to the clan only once its pilot has looked at the Skylab again or given it an order (see [Clans](/wiki/03-Mechanics/Clans.md#where-your-clan-mates-are)).

## Mechanics

### Building and Upgrading

- **Construction**: each module is built on its own. A module is at level 1 the moment it is built, and upgrading it raises its output (or its power made) and its storage, and also what it costs in power.
- **Time and cost**: upgrades cost Credits and Thulium and take time, and every module has its own price and time for each level (hover **Upgrade** to see the next one; the totals are below). The price is paid when you start the upgrade. The cost does not depend on the time. The Engine, Defense and Radar Modules also take Dark Matter Plates and need the technology of the level (see [The second bridge and Core 3](#the-second-bridge-and-core-3)).
- **Timers**: an upgrade runs on the server's clock, so it finishes while you are away, days later if it has to. Start it, log off, come back: the module is at its new level when you open the Skylab page.
- **Upgrade times**: the first levels are quick and the last ones take up to 37 hours, the Core's up to 6 days (see the tables below). Every module has its own timer, so you can upgrade several at once.
- **Production pause**: while a module is being upgraded it is offline: it makes nothing and uses no power. Solar is the exception: it keeps making a quarter of its power (see below).
- **Solar makes only 25% of its power while it upgrades**: Solar makes all of the Skylab's power, and while it upgrades (24 hours for the last level) it makes a quarter of the power of its **current** level; the new level's power takes over the moment the upgrade ends. A full station uses about 90% of what Solar makes at its own level, so a quarter of it carries a station only five to six levels below Solar. Otherwise every farm and collector stops for the whole upgrade, whatever you have stored stays and can be collected, and the Forgery starts no new batch. A module that is upgrading or switched off uses no power, so lifting the farms together with Solar costs nothing extra, and switching modules off makes room for the others; the Thulium Farm uses the most power by far.

### What it costs

The price of the whole climb, the build plus every upgrade, up to level 10 and up to level 20. The Core is always there and its steps cost Credits, with 2,000 Thulium more on the step into level 10 and 4,000 more on the step into level 15; the Research Centre has levels 1 to 10 and its numbers are on the [Research](/wiki/03-Mechanics/Research.md) page. The Ammo Printer, the Rocket Factory and the Ore Bay are built on Core 2, so only once the Core is at level 10, and their level 1 is the build. The four modules of the Expedition are built on Core 3, so only once the Core is at level 15, and the Engine, Defense and Radar Modules stop at level 5, 5 and 3: their two figures are the whole climb.

| Module | Credits to level 10 | Thulium to level 10 | Credits to level 20 | Thulium to level 20 |
| :--- | ---: | ---: | ---: | ---: |
| Core | 112,326 | 2,000 | 6,647,504 | 6,000 |
| Solar | 1,219,500 | 1,600 | 35,039,500 | 36,850 |
| Credit Farm | 840,000 | 109 | 26,240,000 | 2,399 |
| Thulium Farm | 1,154,000 | 4,190 | 32,254,000 | 67,890 |
| Velkonite Collector | 696,000 | 6,950 | 20,996,000 | 78,950 |
| Orvium Collector | 696,000 | 6,950 | 20,996,000 | 78,950 |
| Resource Storage | 619,500 | 359 | 18,169,500 | 2,649 |
| Forgery | 1,224,000 | 2,050 | 35,044,000 | 37,300 |
| Ammo Printer | 1,411,000 | 5,140 | 22,031,000 | 47,940 |
| Rocket Factory | 377,300 | 1,674 | 5,547,300 | 12,494 |
| Ore Bay | 619,500 | 359 | 18,169,500 | 2,649 |
| Engine Module | 15,775,000 | 63,100 | 15,775,000 | 63,100 |
| Defense Module | 24,400,000 | 97,600 | 24,400,000 | 97,600 |
| Radar Module | 3,250,000 | 13,000 | 3,250,000 | 13,000 |
| Trophies Bay | 2,372,500 | 9,490 | 14,722,500 | 58,890 |

The first steps are cheap and the last are dear: the Credit Farm's step from level 1 to 2 costs 5,000 Credits and 1 Thulium, its step from 19 to 20 costs 7,000,000 Credits and 550 Thulium. The Thulium Farm's cost 7,000 Credits and 45 Thulium, then 8,500,000 Credits and 16,000 Thulium. Solar's upgrades cost the same as the Forgery's at every level, and the two collectors cost the same as each other.

The four modules of the Expedition ask for more than Credits and Thulium: Ship Fragments to build, Dark Matter Plates and a technology for each level of the first three:

| Module | Ship Fragments to build | Plates in all | Research: Dark Matter | Research: time |
| :--- | ---: | ---: | ---: | ---: |
| Engine Module | 20 | 19 | 50 | 6 d 13 h |
| Defense Module | 25 | 26 | 50 | 6 d 13 h |
| Radar Module | 15 | 4 | 15 | 1 d 13 h |
| Trophies Bay | 10 | 0 | 0 | – |

All four together: 232,590 Thulium, 58,147,500 Credits, 49 plates, 115 Dark Matter and 14 d 15 h of research. The plates are Dark Matter Plates, and what a plate costs is on [Dark Matter and Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md#how-to-get-a-plate).

### Upgrade times

<!-- upgrade-times:start -->
<!-- Generated from server/Resources/SkylabConfig.json by the test skylab::duration_tests::the_wiki_page_is_the_config (run it with SKYLAB_WIKI_WRITE=1 to rewrite this part). -->

**Upgrade times**, per module (the upgrade from the level in the first column):

| Level | Core | Solar | Credit Farm | Thulium Farm | Resource Storage | Velkonite Collector | Orvium Collector | Forgery | Research Centre |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 to 2 | 72 s | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 78 s |
| 2 to 3 | 86 s | 15 min | 10 min | 15 min | 10 min | 15 min | 15 min | 15 min | 101 s |
| 3 to 4 | 104 s | 30 min | 15 min | 30 min | 15 min | 20 min | 20 min | 30 min | 132 s |
| 4 to 5 | 124 s | 45 min | 20 min | 45 min | 20 min | 30 min | 30 min | 45 min | 171 s |
| 5 to 6 | 149 s | 1 h | 30 min | 1 h | 30 min | 45 min | 45 min | 1 h | 223 s |
| 6 to 7 | 20 min | 1 h 15 min | 45 min | 1 h 30 min | 45 min | 50 min | 50 min | 1 h 15 min | 20 min |
| 7 to 8 | 30 min | 1 h 30 min | 1 h | 2 h | 1 h | 1 h | 1 h | 1 h 30 min | 30 min |
| 8 to 9 | 50 min | 2 h | 1 h 20 min | 3 h | 1 h 20 min | 1 h 15 min | 1 h 15 min | 2 h | 50 min |
| 9 to 10 | 1 h 20 min | 3 h | 1 h 40 min | 4 h | 1 h 40 min | 1 h 30 min | 1 h 30 min | 3 h | 1 h 20 min |
| 10 to 11 | 2 h 15 min | 4 h | 2 h | 5 h | 2 h | 2 h | 2 h | 4 h | – |
| 11 to 12 | 3 h 30 min | 5 h | 2 h 30 min | 6 h | 2 h 30 min | 3 h | 3 h | 5 h | – |
| 12 to 13 | 5 h 30 min | 6 h | 3 h | 8 h | 3 h | 4 h | 4 h | 6 h | – |
| 13 to 14 | 9 h | 8 h | 3 h 30 min | 10 h | 3 h 30 min | 6 h | 6 h | 8 h | – |
| 14 to 15 | 14 h | 10 h | 4 h | 11 h | 4 h | 8 h | 8 h | 10 h | – |
| 15 to 16 | 1 d | 12 h | 5 h | 12 h | 5 h | 10 h | 10 h | 12 h | – |
| 16 to 17 | 1 d 12 h | 16 h | 6 h | 14 h | 6 h | 12 h | 12 h | 16 h | – |
| 17 to 18 | 2 d 12 h | 18 h | 8 h | 18 h | 8 h | 16 h | 18 h | 18 h | – |
| 18 to 19 | 4 d | 20 h | 10 h | 1 d | 10 h | 20 h | 1 d | 20 h | – |
| 19 to 20 | 6 d | 1 d | 12 h | 1 d 12 h | 12 h | 1 d | 1 d 12 h | 1 d | – |
| **Total** | 16 d 13 h | 5 d 13 h | 2 d 14 h | 6 d 13 h | 2 d 14 h | 4 d 16 h | 5 d 10 h | 5 d 13 h | 3 h 12 min |
<!-- upgrade-times:end -->

<!-- upgrade-times-expedition:start -->
<!-- Generated from server/Resources/SkylabConfig.json by the test skylab::duration_tests::the_wiki_page_is_the_config (run it with SKYLAB_WIKI_WRITE=1 to rewrite this part). -->

**Upgrade times** of the Expedition's four modules (the upgrade from the level in the first column; a dash is past the module's highest level):

| Level | Engine Module | Defense Module | Radar Module | Trophies Bay |
| :--- | ---: | ---: | ---: | ---: |
| 1 to 2 | 2 h | 3 h | 4 h | 15 min |
| 2 to 3 | 6 h | 9 h | 1 d | 19 min |
| 3 to 4 | 1 d | 1 d 12 h | – | 26 min |
| 4 to 5 | 2 d | 3 d | – | 34 min |
| 5 to 6 | – | – | – | 45 min |
| 6 to 7 | – | – | – | 1 h |
| 7 to 8 | – | – | – | 1 h 19 min |
| 8 to 9 | – | – | – | 1 h 44 min |
| 9 to 10 | – | – | – | 2 h 18 min |
| 10 to 11 | – | – | – | 3 h 2 min |
| 11 to 12 | – | – | – | 4 h |
| 12 to 13 | – | – | – | 5 h 17 min |
| 13 to 14 | – | – | – | 6 h 59 min |
| 14 to 15 | – | – | – | 9 h 14 min |
| 15 to 16 | – | – | – | 12 h 11 min |
| 16 to 17 | – | – | – | 16 h 5 min |
| 17 to 18 | – | – | – | 21 h 14 min |
| 18 to 19 | – | – | – | 1 d 4 h |
| 19 to 20 | – | – | – | 1 d 13 h |
| **Total** | 3 d 8 h | 5 d | 1 d 4 h | 6 d 8 h |
<!-- upgrade-times-expedition:end -->

An upgrade that is already running when the times change keeps the finish time it was given. The Core alone takes about **16 and a half days** of upgrading in a row to go from level 1 to level 20. No module goes above the Core's level, so the last step of every other module (12 to 37 hours) can start only once the Core is at level 20: with every timer kept busy, and the Credits and Thulium there, the whole station takes about **18 days**.

### Power Management

Your Skylab has a limited power budget.

- **Balance**: keep your Solar output above the power all the other modules use. The Skylab page shows the balance, and warns before a build would push it below zero.
- **Solar keeps pace**: a Solar module at level N makes the power of **all the other modules at level N** (the Core, both farms, the Resource Storage, both collectors and the Forgery, and from level 10 the Research Centre and the Ore Bay) and about a tenth more, so a station whose modules are all at level 7 needs Solar 7, and has it covered. Solar one level lower is not enough for a full station (the last column), so Solar still has to follow the rest up. The Core draws little, so it may run ahead: Solar 5 and up covers a full station at its level with the Core at any level. The table below also counts the Ammo Printer from level 7, the Rocket Factory and the Ore Bay from level 10, and the Engine, Defense and Radar Modules and the Trophies Bay from level 11 (they are built from Core level 15, and count four levels earlier because the Core can run ahead of Solar), each at its own highest level at most.
- **Active state**: you can switch the farms, the collectors and the Forgery on or off to manage power. The Core, Solar, the Resource Storage and the Research Centre always run. The Ammo Printer, the Rocket Factory and the Ore Bay can be switched on and off too, and so can the four modules of the Expedition (not while a trip is under way).
- **Blackout**: if power use is higher than power made, all the farms and collectors stop producing until the balance is back. What they already hold stays, and you can still collect it. The Forgery starts no new batch, and the Research Centre starts no new research (a research already running goes on). The Ammo Printer, the Rocket Factory and the Ore Bay stop like the farms and collectors. The Defense Module fights nothing, the Radar's scans stand still and no trip can start (a trip that is under way goes on).
- **Solar upgrades**: while Solar upgrades it makes only a quarter of its power, so unless your other modules are far below it the station is in deficit and the farms and collectors stop until the upgrade is done (see [Solar Module](#solar-module)).

Solar's power at each level, against what the other modules use at the same level (every module at that level, the Core included, and the Research Centre and the Ore Bay from level 10, and the four modules of the Expedition from level 11):

<!-- skylab-power:start -->
<!-- Generated from server/Resources/SkylabConfig.json by docs/design/skylab-power-model.py --doc (--check fails while this part is behind). -->

| Level | Solar makes | The other modules use | Left over | With Solar one level lower |
| :--- | ---: | ---: | ---: | :--- |
| 1 | 255 | 230 | 25 | – |
| 2 | 310 | 278 | 32 | 255: 23 short |
| 3 | 375 | 337 | 38 | 310: 27 short |
| 4 | 455 | 410 | 45 | 375: 35 short |
| 5 | 555 | 501 | 54 | 455: 46 short |
| 6 | 680 | 615 | 65 | 555: 60 short |
| 7 | 965 | 875 | 90 | 680: 195 short |
| 8 | 1,185 | 1,076 | 109 | 965: 111 short |
| 9 | 1,460 | 1,327 | 133 | 1,185: 142 short |
| 10 | 2,035 | 1,849 | 186 | 1,460: 389 short |
| 11 | 2,995 | 2,721 | 274 | 2,035: 686 short |
| 12 | 3,565 | 3,241 | 324 | 2,995: 246 short |
| 13 | 4,285 | 3,893 | 392 | 3,565: 328 short |
| 14 | 5,185 | 4,713 | 472 | 4,285: 428 short |
| 15 | 6,325 | 5,748 | 577 | 5,185: 563 short |
| 16 | 7,765 | 7,055 | 710 | 6,325: 730 short |
| 17 | 9,585 | 8,711 | 874 | 7,765: 946 short |
| 18 | 11,895 | 10,812 | 1,083 | 9,585: 1,227 short |
| 19 | 14,835 | 13,483 | 1,352 | 11,895: 1,588 short |
| 20 | 18,575 | 16,885 | 1,690 | 14,835: 2,050 short |
<!-- skylab-power:end -->

The table counts every module at the same level. The Thulium Farm draws more than two thirds of it at the top (11,695 at level 20, against 16,885 for all fifteen), so a station with that farm far ahead of the rest needs more Solar than its Core suggests.

### Collecting

Every farm and collector has a hopper for about 72 hours of what it makes. You collect by hand.

- **Capacity**: once a hopper is full it stops producing until you collect.
- **Farms**: collected Credits and Thulium go straight to your account.
- **Collectors**: the ore goes to the Resource Storage, as far as it has room.
- **Forgery**: the plates go to your inventory, when your ship is landed.
- **Ammo Printer and Rocket Factory**: the ammo and the rockets go to your inventory, when your ship is landed. Each keeps only 24 hours of production (see [Ammo Printer](#ammo-printer) and [Rocket Factory](#rocket-factory)).
- **Ore Bay**: nothing to collect. It moves the ore of your inventory into the Resource Storage when you press Move, with your ship landed, up to its allowance (see [Ore Bay](#ore-bay)).
- **Trophies Bay**: collected in the Universe window, with your ship landed: Credits and Thulium go to your account, experience and honor to your pilot and the loot to your inventory. It keeps what it holds until you collect it, but a full Bay makes the Skylab hold fire (see [Trophies Bay](#trophies-bay)).
- **Collect All** takes everything at once, switched-off and upgrading modules included, but not the Trophies Bay, which you collect in the Universe window.
- A **(!)** badge points out a full hopper you can empty, and plates waiting in the Forgery, on the Skylab page and on the sidebar's Skylab row.

### The wipe

The Skylab is never wiped: modules keep their levels, the Resource Storage keeps its ore and the Research Centre keeps its technologies, its tank of science, the Dark Matter it holds and a research under way. The plates in your inventory are items like any other, so they follow the [wipe rules](/wiki/03-Mechanics/Wipe-Timeline.md). The Ammo Printer and the Rocket Factory keep their levels, what they are set to make and what they hold, and the Ore Bay keeps its level and its allowance. The four modules of the Expedition keep their levels too, with their technologies, and so do the magazine and the switch of the feed. The ore in your inventory is wiped like any item: move it into the Resource Storage first.

An **expedition** is settled up to the wipe: a trip under way is over, the Trophies Bay pays out its Credits, Thulium, experience and honor and is emptied (its loot is deleted like any loose item), and the Skylab starts the new season at home, in your company's port, with a new universe map, the 19 starting cells known and the Radar's line empty. The engines and lasers fitted in the Engine and Defense Modules are loose items like the others: take them out and put them in the Transport Cache to keep them.

## Planning your Skylab

The Skylab takes weeks to grow, so a little planning pays. The numbers are the tables above.

### What to upgrade first

1. **Solar, then the Credit Farm.** Solar costs 500 Credits and 50 Thulium and nothing runs without it; the Credit Farm costs nothing. The ten [Station missions](/wiki/03-Mechanics/Quests.md#station-missions) walk you through these first steps and pay you 52,000 Credits and 610 Thulium for them, at base: your world, boosters and clan boosts multiply it.
2. **Then the Thulium Farm: it is your main source of Thulium.** At level 10 it makes 360 Thulium an hour, 8,640 a day, about as much as 43 kills of a [Crystalys](/wiki/04-Aliens/Crystalys.md) pay in Alpha (200 each). The climb to level 10 costs 1,154,000 Credits and 4,190 Thulium, the build included. At level 15 the farm makes 18,240 a day and at level 20 30,720. Its hopper holds 72 hours, so come back at least every three days. What Thulium buys is on the [Resources](/wiki/06-Items/Resources.md#thulium) page.
3. **The Credit Farm is the steady side income.** At level 10 it makes 33,750 Credits an hour, 810,000 a day, for 840,000 Credits and 109 Thulium. The higher levels pay back in days: the step from level 9 to 10 costs 300,000 Credits for 4,500 more an hour, which is 67 hours. Raise it when you have Credits to spare.
4. **Keep the Core busy.** Nothing goes above the Core, and the Core alone takes about 16 and a half days to reach level 20. There is no queue, so start its next step every time you come back.
5. **Build the supply chain as a set.** The collectors, the Resource Storage and the Forgery open at Core level 5. A collector can bank ore only into a Resource Storage, and the bank holds one day of its collector's output at level 1 and four days at level 20, so raise the Storage with the collectors or the ore waits in their hoppers.
6. **Have 2,000 Thulium ready for Core level 10.** The Core's step from level 9 to level 10 asks for it, and it builds the bridge and Core 2, where the [Ammo Printer](#ammo-printer), the [Rocket Factory](#rocket-factory) and the [Ore Bay](#ore-bay) are built.
7. **Have 4,000 Thulium ready for Core level 15.** The Core's step from level 14 to level 15 asks for it, and it builds the second bridge and Core 3, where the four modules of the Expedition are built. The modules themselves ask for much more, 232,590 Thulium and 49 Dark Matter Plates in all (see [What it costs](#what-it-costs)): start with the Engine Module and the Defense Module at level 1.
8. **Build the Expedition in this order.** An engine in the Engine Module, a laser in the Defense Module with an Ammo Printer to feed it, and the Trophies Bay to keep what the kills bring: a trip earns nothing until all three are there. The Radar Module can wait: at Defense level 1 your Skylab reaches at least the six cells next to its port, and the 19 cells you know at the start hold cells up to difficulty 3.

### Timing a Solar upgrade

While Solar upgrades it makes a quarter of its power, and a station almost always uses more than that. The farms and collectors then stop for the whole upgrade: what they hold stays, but what they would have made is lost. The table gives, for each Solar step, its time, the biggest station that still runs through it (every module at the same level, the Core and the supply chain included; a smaller station fits a little more) and what a Credit Farm and a Thulium Farm of that level would have made in that time. For example, Solar from level 10 to 11 takes 4 hours, and farms of level 10 would have made 135,000 Credits and 1,440 Thulium in them. The table counts the Ammo Printer from level 7, the Rocket Factory and the Ore Bay from level 10, and the four modules of the Expedition from level 15, too.

| Solar upgrade | Time | Station that keeps running, up to level | Credit Farm makes meanwhile | Thulium Farm makes meanwhile |
| :--- | ---: | ---: | ---: | ---: |
| 1 to 2 | 5 min | none | 188 | 3 |
| 2 to 3 | 15 min | none | 1,125 | 16 |
| 3 to 4 | 30 min | none | 3,375 | 44 |
| 4 to 5 | 45 min | none | 6,750 | 84 |
| 5 to 6 | 1 h | none | 11,250 | 144 |
| 6 to 7 | 1 h 15 min | none | 19,688 | 230 |
| 7 to 8 | 1 h 30 min | 1 | 30,375 | 336 |
| 8 to 9 | 2 h | 2 | 49,500 | 528 |
| 9 to 10 | 3 h | 3 | 87,750 | 912 |
| 10 to 11 | 4 h | 5 | 135,000 | 1,440 |
| 11 to 12 | 5 h | 6 | 202,500 | 2,200 |
| 12 to 13 | 6 h | 7 | 297,000 | 3,120 |
| 13 to 14 | 8 h | 7 | 468,000 | 4,800 |
| 14 to 15 | 10 h | 8 | 675,000 | 6,800 |
| 15 to 16 | 12 h | 9 | 918,000 | 9,120 |
| 16 to 17 | 16 h | 10 | 1,440,000 | 14,080 |
| 17 to 18 | 18 h | 11 | 1,944,000 | 18,000 |
| 18 to 19 | 20 h | 12 | 2,610,000 | 22,400 |
| 19 to 20 | 1 d | 13 | 3,780,000 | 28,800 |

- **Lift the farms together with Solar.** A module that is upgrading makes nothing and uses no power anyway, so the time a farm spends upgrading during the pause costs nothing extra.
- **Keep the other modules low if you cannot afford a pause.** A station runs through a Solar upgrade only if all its other modules are at least five levels below Solar (six from Solar level 10), and a full station needs a little more, as the table shows.
- **Switch off what you can do without.** A module that is switched off uses no power, so switching off the Thulium Farm, the biggest user (80 at level 1, 30% more with every level), makes room for the others.
