---
title: "SpaceCorps 2027 · Patch notes"
description: "Every update of SpaceCorps 2027, newest first: what changed for players in each release."
canonical: "https://spacecorps.github.io/play/patchnotes.html"
---

# SpaceCorps 2027 · Patch notes

Every update of SpaceCorps 2027, newest first: each release's summary and what is new for players.
The full text of a release (updating, platforms, first launch, known issues, checksums) is on its GitHub release.

- HTML page: [https://spacecorps.github.io/play/patchnotes.html](https://spacecorps.github.io/play/patchnotes.html)
- Machine-readable: [patchnotes.json](https://spacecorps.github.io/play/patchnotes.json) (version, date, GitHub URL, summary and "What's new" in Markdown)
- Download page: [https://spacecorps.github.io/play/](https://spacecorps.github.io/play/)

---

<!-- patchnotes:list -->
## 0.4.17 · 2026-10-09

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.17)

SpaceCorps 2027 0.4.17 is the Danger Sector update: when a season reaches day 11 (the Tech Surge), the machines of a lost civilisation wake up. DS-1, DS-2 and DS-3 get a pulsar and a giant excavator that mines Thulium and rare ore when you fuel it with Dark Matter, DS-4 gets the Dormant Swamp and its guns, three new dormant aliens (the Slumbering Void, the Inert Mass and The Unwakened) defend them, and the Dormant Swarm comes back twice as fast and pays twice.

### What's new

**Highlights**
- **A pulsar and a giant excavator** on DS-1, DS-2 and DS-3 of every world. Put Dark Matter in its tank (3 at most; 1 burns for 10 minutes), choose Thulium, Cataclysite, Quorvium, Orvium or Velkonite at the control panel and start it: everyone in the world is told in chat. A box lands around it every 20 seconds for anyone to take. A full run of 30 minutes is worth about what 2 to 3 pilots hunting for Thulium the best way make in that time (4,821 Thulium in Alpha).
- **Mining calls Slumbering Voids:** 2 every 2 minutes, 8 at most, each 25,000 hull and 150,000 shield at speed 400. If no pilot is left to fight them they attack the excavator (200,000 hull in Alpha): destroyed, it rests for an hour and its fuel is lost.
- **After 30 minutes of mining in all, the excavator overheats** and rests for an hour, and it and its pulsar radiate: 10% of a ship's hull and shield every second, so a ship dies in 10 seconds. You are warned 60 and 15 seconds before.
- **The Dormant Swamp,** the top-left corner of DS-4: a N.I.K.E. every 2 seconds, a N.U.K.E. every 5 seconds and two laser turrets of about 50,000 a hit fire at every ship they see within 4,300 units, and none of them sees a cloaked ship. Five **Inert Masses** and two patrolling Voids live there, and **The Unwakened** (10 million hull and 10 million shield, 75,000 damage a second within 700 units) sleeps in the middle and cannot be hurt yet.
- **The Dormant Swarm** starts from the swamp, is back 30 minutes after its last ship dies (it was an hour) and pays twice the Credits, Thulium, experience and honor.
- **Ranking:** a Slumbering Void gives 10 PvE points, an Inert Mass 15 and The Unwakened 112.
- **New look and sound:** purple-black models with glowing violet seams, the excavator's control panel, a radiation gauge, 15 new quiet sounds and every new text in 12 languages.

**If you already play: what changes for you**
- **Nothing changes before season day 11.** From that day (event 2, the Tech Surge) to the next Wipe the Danger Sectors hold all of the above. A world that is past day 11 when you update gets it at once.
- **Update the game.** A 0.4.12, 0.4.13, 0.4.14, 0.4.15 or 0.4.16 game installs it as a patch (a Linux AppImage game from 0.4.14), and downloads the whole package if the patch cannot be used. A 0.4.11 or older game downloads the whole package.
- **A game that has not updated cannot see the swamp, the pulsars or the radiation, and they still hurt it.** A 0.4.16 game keeps working, but it draws no pulsar, excavator or swamp, has no control panel, and sees the new aliens as ordinary ones.
- **The Dormant Swarm changes from day 11:** it starts at the swamp, is back after 30 minutes and pays twice (the loot box is the same).
- **Rocks near the new places are gone:** there are none within 2,600 units of a pulsar, 2,200 of an excavator or 4,900 of the swamp.
- **A login or an "on the spot" respawn never puts you inside the radiation or the swamp's zone:** you are moved out of it and told so.
- **Dark Matter has a new use** (the excavator's fuel). An Inert Mass can drop it, and The Unwakened would drop a lot.
- No Credits, Thulium or items are paid, moved or removed by the update.

**The pulsar and the giant excavator**
- **Where.** One pulsar and one giant excavator on each of DS-1, DS-2 and DS-3 in every world (nine pairs). The excavator stands 900 units from its pulsar, in the open part of the map, far from the gates. DS-4 has the black hole instead. A label "Excavator" hangs over the machine within 1,400 units: click it to open the **Giant excavator** sheet.
- **The control panel.** The sheet works within 600 units of the excavator. It shows the fuel tank (three cells), the heat, the hull, the five resources with what each lays a minute in your world, **Add Dark Matter** and **Start mining**. Anyone can add fuel, choose and start; the choice can be changed until Start and is locked while it runs. A refusal ("You are too far from the control panel", "You have no Dark Matter", "The tank can hold no more Dark Matter") shows in red.
- **Fuel.** Add Dark Matter takes 1 Dark Matter from your cargo (not one that is fitted, not one in the Transport Cache). The tank holds 3, never more than the excavator can still burn before it overheats; 1 burns for 10 minutes. **If the excavator is destroyed, the fuel in its tank is lost.**
- **Mining.** Start tells the whole world in chat and the Game Log ("[pilot] started the giant excavator on DS-1: mining Thulium, 30 minutes of fuel. Slumbering Voids will come for it."). A box lies 450 to 900 units from the excavator every 20 seconds (90 in a full run) for 5 minutes. Anyone can pick one up, first come, with no daily limit on its Thulium. Normal PvP rules apply here: nothing protects a miner from a raider.
- **Out of fuel before the heat limit,** it is ready again with its heat kept: add Dark Matter and start again.

| A full run lays (30 minutes, 3 Dark Matter) | Alpha | Beta | Gamma |
|---|---|---|---|
| Thulium | 4,821 | 7,714 | 9,643 |
| Cataclysite | 1,157 | 1,851 | 2,314 |
| Quorvium | 514 | 823 | 1,029 |
| Velkonite | 320 | 320 | 320 |
| Orvium | 160 | 160 | 160 |

Velkonite and Orvium, the Skylab's two ores, are capped at 4 hours of a level 20 collector of that ore, so a run never speeds the Skylab up by more than that. Thulium, Cataclysite and Quorvium are laid at the same worth, in the model's figures about what 2.5 pilots make in half an hour hunting for Thulium the best way (3,857 Thulium an hour each, counted before the cost of their ammo); Beta and Gamma scale it by 1.6 and 2, and the Voids' pay and boxes come on top.

- **Overheating.** Mining adds heat, and the heat never cools while the excavator stands idle: after 30 minutes of mining in all, however many runs it takes, the excavator overheats and rests for an hour. The tank is emptied, the boxes already on the ground stay, and the map is warned 60 and 15 seconds before.
- **Radiation.** While it rests, overheated or destroyed, the excavator and its pulsar radiate. A ship within 1,100 units of the excavator or 1,300 of the pulsar loses 10% of its hull and shield every second, shield first, cloaked or not: a ship at full strength dies in 10 seconds, and the kill is credited to the last enemy who hit it. Aliens are not hurt. The circles are drawn on the flight view and the minimap (an amber ring in the last minute, red and dashed while they radiate) and a gauge shows the dose. **The Ironclad (speed 92) cannot leave the circles in 10 seconds from the panel or the far boxes: leave in the 60-second warning.**
- **Slumbering Voids.** The first wave comes 60 seconds after a start, then every 120 seconds: 2 Voids from the edge of the map, at most 8 alive, none in the last 60 seconds before the overheat. They hunt the pilots near the excavator; the ones left over start flying away 90 seconds after the run ends, unless they are fighting.
- **The siege.** When no pilot is left for them to hunt (dead, cloaked, in a safe ring or farther than 7,000 units) for 15 seconds, the Voids shoot the excavator for a quarter of their laser damage. At 0 hull it is destroyed: it rests for an hour, its hull is full again and its fuel is lost. Pilots cannot hurt it, and nothing but the Voids does. Its hull is 200,000 in Alpha, 300,000 in Beta and 400,000 in Gamma.
- **A server restart pauses a run:** fuel, heat, choice and cooldown are saved; the next wave comes 60 seconds after.

**The Dormant Swamp**
- **Where.** The top-left corner of DS-4: a zone of 4,300 units around its middle, more than 6,700 units from the nearest portal ring and clear of the black hole. A ship that crosses the notice ring at 4,800 units is told once ("Warning: the Dormant Swamp. Its turrets fire on every ship they see, and something sleeps in the middle.").
- **The guns** stand in the middle and cannot be hurt. Each aims at the nearest ship it sees, with the world's strength on its damage (1.5 times in Beta, 2 in Gamma):

| Gun | Fires | Hits for | Reaches |
|---|---|---|---|
| N.I.K.E. | every 2 seconds | 75,000, 35% penetration | 3,640 units |
| N.U.K.E. | every 5 seconds | 50,000, blast of 900 units | 1,080 units |
| Two laser turrets | every second | 45,000 to 55,000 each | 2,500 units |

- **A cloak is the way in.** No gun sees a cloaked ship, a ship in an EMP's window, a ship in a safe ring or one in its 3 seconds of respawn protection, so a cloaked ship can fly through the whole zone up to The Unwakened's aura. Nothing else can be done to the base yet. A Wraith with the best shields lasts 3 to 13 seconds inside the zone in Alpha.
- **Five Inert Masses** stay within 2,400 units of the middle. Each fires a **Dormant Lance** every 6 seconds at the nearest ship it sees: a homing rocket (speed 750) that hits for 5,000 to 8,000 with 40% penetration and follows you for 7 seconds. Only a cloak, an EMP, a safe ring or a jump breaks its hold. A dead Mass is back 60 minutes later. Nobody else can fire, craft or sell a Lance.
- **Two Slumbering Voids** patrol 4,600 to 6,500 units from the middle, outside the guns' reach, and are back 60 minutes after one dies.
- **The Unwakened** stands in the middle at speed 10 and burns every ship within 700 units for 75,000 a second (cloaked ships too; 1.5 and 2 times in Beta and Gamma). **He is immune for now:** shots and rockets land and do nothing, the Target window shows full bars and the hit says "Immune". Quests and events of a later update are meant to turn that off.
- Nothing in the swamp ever follows a cloaked pilot or enters the black hole's circle.

**The three new dormant aliens** (Alpha numbers; Beta and Gamma have 1.5 and 2 times the hull, shield and damage and pay 2 and 3 times as much)

| | Slumbering Void | Inert Mass | The Unwakened |
|---|---|---|---|
| Hull / shield | 25,000 / 150,000 | 250,000 / 100,000 | 10,000,000 / 10,000,000 |
| Shield takes | 80% of each hit | 80% of each hit | 80% of each hit |
| Speed | 400 | 60 | 10 |
| Weapon | lasers, 2,400 to 3,000 a volley | Dormant Lance, 5,000 to 8,000 | aura, 75,000 a second |
| Where | in waves at a mining excavator; 2 patrol the swamp | 5 in the swamp | 1 in the middle of the swamp |
| Pays | 23,000 Credits, 60 Thulium, 3,600 experience, 16 honor | 125,000 Credits, 335 Thulium, 20,200 experience, 88 honor | 7,500,000 Credits, 20,000 Thulium, 1,200,000 experience, 5,200 honor (nobody can earn it yet) |
| PvE points | 10 | 15 | 112 |

- **Pay and box.** A kill pays every pilot who did at least 5% of the damage, by their share, and the loot box is first reserved for the pilot who did the most. A Void's box holds, 60% of the time, 30 to 60 of one laser ammo (Ultra Core or Experimental Fusion Core) and, 40% of the time, 1 to 3 of one Epic rocket; never Dark Matter and never a N.I.K.E. An Inert Mass's box: 400 to 800 of the two ammos, 20 to 40 of one Epic rocket, and by chance 1 to 2 N.I.K.E. (5%), 1 to 3 Dark Matter (5%), an Ancient Control Unit (10%) and 1 to 2 Power Cores (25%). The Unwakened's box is written down and out of reach: 10,000 to 15,000 of the two ammos, 500 to 800 Epic rockets, 20 to 30 N.I.K.E., 5 to 10 N.U.K.E., 40 to 60 Dark Matter, 10 to 20 Ancient Control Units and 100 to 200 Power Cores.
- **How hard.** A Void's shield takes 80% of every hit while it stands, so its hull goes after about 125,000 damage with no shield penetration, 55,556 with 25% and 35,714 with 50%. An Inert Mass takes about 350,000. In the model three level 8 Paragons with x2 ammo destroy a Void in 27 seconds and an Inert Mass in 76.
- **The Voids are fast:** speed 400 is a Storm on Afterburner III. Only a gate, a safe ring or a cloak gets away from one.
- **They count.** Every kill goes in your kill statistics under the alien's own name and gives the PvE points above, toward your rank and the gold crown, as the swarms' kills do (they have counters of their own); no quest or Challenge asks for them yet. A Void's death is told to nobody, an Inert Mass's to its map and the kill feed.

**The Dormant Swarm from day 11**
- **It starts at the swamp** (4,700 units from the middle, outside the zone) and flies out through the gates as before, keeping 450 units clear of the zone. It is **back 30 minutes after the whole swarm is destroyed** (it was 60), and **pays twice:** a Dormant Force now pays 400,000 Credits and 1,070 Thulium, a Dormant Pulse 190,000 and 510 (Alpha), and experience and honor double too. The loot box, its strength, speed and route are the same. Before day 11 nothing about it changes.

**What you see and hear**
- The pulsar is a violet core with two sweeping beams, the excavator a hexagonal frame with a spiral drill and three fuel cells, the swamp's zone, its notice ring and its turrets are drawn, and the aliens have their own purple-black models with violet trails. The minimap and the Star System map mark the pulsar, the excavator (with its state and time) and the swamp.
- The flight view warns you when a flight order leads into the radiation or the swamp's guns, and the death screen says "Moved out of a danger zone" when an on-the-spot respawn was moved.
- **15 new quiet sounds,** each with its own rate limit on the effects volume: the sheet opening, a unit of fuel, one tick for each resource, the start, the overheat warning and the overheat, a wave, the radiation, the swamp's warning, each of the three guns, an immune hit, and two hums (a mining excavator and The Unwakened).

**For administrators and the server**
- **At the first start:** one new table (`ExcavatorStates`, one row for each of the nine excavators, written on every change and every 60 seconds; the Wipe empties it), and the seeder adds three alien rows (Inert Mass, The Unwakened, Slumbering Void) and one rocket row, the Dormant Lance, that nobody can fire, craft or list. No data step. The backup gate lists one line. Two data files are new (`Excavator.json`, `DormantSwamp.json`) and four change (`Swarms.json`, `Rockets.json`, `Market.json`, `ranking-config.json`). New routes: `GET /api/admin/excavators`, `POST /api/admin/excavators/:tool` (fuel, resource, start, stop, heat, cooldown, destroy, overheat, wave, reset), `GET /api/admin/swamp`, `POST /api/admin/swamp/immunity` and `POST /api/admin/swamp/voids`, every call recorded. One new client feature string, `dormant-ds`, thirteen new `excavator_*` counters. No new environment variable.

## All releases

Each line links the full notes of that release as Markdown (patchnotes/v<version>.md); its HTML page is patchnotes-v<version>.html.

- [0.4.17](https://spacecorps.github.io/play/patchnotes/v0.4.17.md) · 2026-10-09 · The Danger Sector update: when a season reaches day 11 (the Tech Surge), the machines of a lost civilisation wake up.
- [0.4.16](https://spacecorps.github.io/play/patchnotes/v0.4.16.md) · 2026-10-09 · The clans and ships update: clans get a page, posts, a daily bonus and wars that end by consent…
- [0.4.15](https://spacecorps.github.io/play/patchnotes/v0.4.15.md) · 2026-10-08 · The Skylab update: when your Core reaches level 10 a bridge builds a second Core with six module seats, and two new modules…
- [0.4.14](https://spacecorps.github.io/play/patchnotes/v0.4.14.md) · 2026-10-08 · Adds a research queue of five, an asteroid mission at every level from 1 to 8 and a mark for the missions and Challenges you can accept.
- [0.4.13](https://spacecorps.github.io/play/patchnotes/v0.4.13.md) · 2026-10-07 · Lets lasers hurt asteroids, shortens every rocket's recharge to 3 seconds and triples what rocks pay.
- [0.4.12](https://spacecorps.github.io/play/patchnotes/v0.4.12.md) · 2026-10-07 · Opens the Auction, where pilots of level 5 and up sell what they earned to each other, and asteroid mining…
- [0.4.11](https://spacecorps.github.io/play/patchnotes/v0.4.11.md) · 2026-10-06 · Makes ranks per company, draws the drone formations as shapes round your ship, gives the Group window a new layout…
- [0.4.10](https://spacecorps.github.io/play/patchnotes/v0.4.10.md) · 2026-10-05 · Rebuilds the Skylab's numbers and adds 16 drone formations in two new research trees, reworked level missions…
- [0.4.9](https://spacecorps.github.io/play/patchnotes/v0.4.9.md) · 2026-10-04 · Adds the Research Centre to the Skylab: from Core level 10 you feed it resources and research technologies…
- [0.4.8](https://spacecorps.github.io/play/patchnotes/v0.4.8.md) · 2026-10-03 · Puts three swarms of alien bosses on the map.
- [0.4.7](https://spacecorps.github.io/play/patchnotes/v0.4.7.md) · 2026-10-02 · Puts ten missions about your Skylab into Mission Control and gives Solar enough power for the whole station.
- [0.4.6](https://spacecorps.github.io/play/patchnotes/v0.4.6.md) · 2026-10-01 · Adds the Ironclad, a crafted tank with the most hull of any ship, and reworks the shields: the best set is 80 percent…
- [0.4.5](https://spacecorps.github.io/play/patchnotes/v0.4.5.md) · 2026-10-01 · Lets you choose where to come back when your ship is destroyed, adds a kill feed with funny lines to the Global chat…
- [0.4.4](https://spacecorps.github.io/play/patchnotes/v0.4.4.md) · 2026-09-30 · Brings groups of up to five pilots from any company with three chat channels, a rework of the rockets with fixed damage…
- [0.4.3](https://spacecorps.github.io/play/patchnotes/v0.4.3.md) · 2026-09-30 · Brings rockets, three active abilities, the Cloaking CPU and the EMP, the Forge…
- [0.4.2](https://spacecorps.github.io/play/patchnotes/v0.4.2.md) · 2026-09-29 · Rebalances weapons, ships, Repair Drones and aliens (some setups got weaker, and this page says which), draws critical hits differently…
- [0.4.1](https://spacecorps.github.io/play/patchnotes/v0.4.1.md) · 2026-09-28 · Stops the flicker on the login screen and in Skylab, and shows each pilot's clan tag next to their company letter.
- [0.4.0](https://spacecorps.github.io/play/patchnotes/v0.4.0.md) · 2026-09-27 · A graphics overhaul.
- [0.3.4](https://spacecorps.github.io/play/patchnotes/v0.3.4.md) · 2026-09-27 · Gives every item a real 3D model, with its icon rendered from it.
- [0.3.3](https://spacecorps.github.io/play/patchnotes/v0.3.3.md) · 2026-09-27 · Gives every mission a face: each company's officers now hand out its quests.
- [0.3.2](https://spacecorps.github.io/play/patchnotes/v0.3.2.md) · 2026-09-27 · Makes text easier to read everywhere: every label, number and button now stands out clearly from what is behind it.
- [0.3.1](https://spacecorps.github.io/play/patchnotes/v0.3.1.md) · 2026-09-27 · A small maintenance update: the game runs on the latest version of its engine.
- [0.3.0](https://spacecorps.github.io/play/patchnotes/v0.3.0.md) · 2026-09-26 · Splits the galaxy into three separate worlds: Alpha, Beta and Gamma.
- [0.2.3](https://spacecorps.github.io/play/patchnotes/v0.2.3.md) · 2026-09-26 · Makes shields, shield cells, thrusters and laser amps work the way the item cards say: your absorbance now decides how much of each hit…
- [0.2.2](https://spacecorps.github.io/play/patchnotes/v0.2.2.md) · 2026-09-26 · The first version that arrives through the game's own updater.
- [0.2.1](https://spacecorps.github.io/play/patchnotes/v0.2.1.md) · 2026-09-26 · Keeps itself up to date, adds an About screen, and fixes the repair drone.
- [0.2.0](https://spacecorps.github.io/play/patchnotes/v0.2.0.md) · 2026-09-26 · Brings new graphics, company pilots flying alongside you, cargo to pick up, a new sound system, and the whole game in ten languages.
- [0.1.0](https://spacecorps.github.io/play/patchnotes/v0.1.0.md) · 2026-09-25 · The first public build of SpaceCorps 2027: the SpaceCorps space MMO, rebuilt as a native desktop game.
<!-- /patchnotes:list -->
