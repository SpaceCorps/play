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
## 0.4.21 · 2026-10-13

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.21)

SpaceCorps 2027 0.4.21 is the expeditions and companions update: your Skylab flies out on trips across a map of 150 cells, P.E.T.s fly beside your ship and two of them work for you, ships wear skins, auras and exhaust colours, the Energetic Wall stands where you aim it, Davidski flies out once a day and sells everything, the Recipe Book shows how to get any item, and the Ore Bay moves three times as much ore.

### What's new

**Highlights**
- **Your Skylab goes on expeditions.** From Core level 15 it gets a second bridge and four new modules. Scan a 150-cell map with the Radar, fit engines and lasers, pick a cell and **Depart**: the trip runs on the server's clock, **also while you are logged out**, and the Trophies Bay fills until you **Collect**.
- **P.E.T.s** (made in the Hangar's Cradle, docked for boosts): ten types, and two of them work for you while you fly. The **Retriever** collects the boxes around your ship and the **Mole** mines asteroids, at the top as fast as a pilot with the best rockets, and never rests.
- **Looks.** 43 skins, 24 aura and exhaust colours with nine effects each, drone liveries, a Look section and a Wardrobe in the Hangar. **For now an admin issues looks.**
- **The Recipe Book and Builds** in the Library: how to get any item as a chart, steps and a bill; import your Hangar's loadout or a friend's, edit it, see its stats and cost, or start from 15 presets. Your builds are saved on your account.
- **The Energetic Wall** stands where your cursor is, across the line from your ship; level 2 is yellow. It stops every shot from either side and burns whoever flies into it, you too.
- **Davidski, a trader who flies,** comes out once a day at a time nobody announces; only the pilots on his Danger Sector see him. He pays like a boss when he falls and sells everything the Auction lists, at many times the Shop's price.
- **63 recipes changed:** the Storm, the Ironclad, the amps, thrusters, shield cells, cores, the Master Drone, the formations and the designs ask for more, and every last-tier craft asks 4 Dark Matter Plates and an Ancient Control Unit.
- **The EMP Charge is a consumable** (a stack of up to 20, no Extras slot), the **Production Queue is a timeline** with a number field, the Clan and the Auction have **windows in flight**, and the station pages have a **chat dock**.
- **The Ore Bay moves 3 times as much** ore an hour and keeps 3 times the day's worth.
- **Smaller:** Shield Surge and Emergency Repair restore 40 % less, the hourly Lots are bid in credits, the excavator switches resource while it mines, the Universe map is roomier, and 52 new quiet sounds.

**If you already play: what changes for you**
- **Update the game.** A 0.4.12 to 0.4.20 game installs it as a patch (a Linux AppImage game from 0.4.14), and downloads the whole package if the patch cannot be used. A 0.4.11 or older game downloads the whole package.
- **A 0.4.20 game keeps working against the 0.4.21 server but sees none of the new windows until it updates:** it draws Davidski as a grey swarm ship it may shoot, and shows the EMP Charge stack as one tile it cannot equip. It can still fire a saved EMP slot, but it cannot buy an EMP until it updates.
- **The rules change on the server at once:** the crafts' prices, the abilities, the Ore Bay, Davidski, walls as cover, the chunks that asteroids drop, the hourly Lots and the expeditions.
- **Nothing you own is taken, and no Credits, Thulium or items are paid or removed.** Your EMP Charges become one stack, crafts you queued keep the price they were paid, and Solar makes 535 to 585 more power from Core level 15 (18,575 at level 20, it was 17,990).
- **Trips run while you are logged out,** and a destroyed Skylab stops all production from that moment until you press Repair.
- **The wipe keeps your P.E.T.s and your looks,** and pays out the Trophies Bay. An EMP Charge stack is lost at the wipe unless it is in the Transport Cache (in 0.4.20 one fitted on the active ship survived it).

**The Skylab's expeditions**
- **The step into Core level 15** builds a second bridge and Core 3 with four seats for these modules, and costs 4,000 Thulium more. Every level of the Engine, Defense and Radar modules needs its own technology, researched in the Skylab (a new family in the Research tree: 13 technologies, 3 hours to 3 days each, 115 Dark Matter in all); a module is built or upgraded with your ship landed. Every module has a weight and **the engines you fit decide how fast the whole station flies**: the heavier it is, the slower.

| Module (from Core level 15, on Core 3) | Levels | What a level gives | Build, level 1 |
|---|---|---|---|
| Engine module | 5 | engine slots, 1 to 5 | 375,000 Credits, 1,500 Thulium, 20 Ship Fragments, 1 Dark Matter Plate |
| Defense module | 5 | laser slots 1 to 5, a magazine of 1,300 to 35,000 rounds, the highest difficulty it may enter (1 to 5) | 500,000 Credits, 2,000 Thulium, 25 Ship Fragments, 1 Dark Matter Plate |
| Radar module | 3 | a scan of 90, 40 or 15 minutes a cell | 250,000 Credits, 1,000 Thulium, 15 Ship Fragments |
| Trophies Bay | 20 | room for 650 to 45,000 bounty points | 100,000 Credits, 400 Thulium, 10 Ship Fragments |

- **The map.** 15 by 10 cells, its own map and not the game's sectors. Three company ports (H3 Mars, D8 Terra, L8 Galactic); you start knowing your port and the two rings round it (19 cells). Cells have a difficulty from 0 to 5 that grows with the distance from the nearest port, a code (H3) and a name. The map is the same for everybody in a world and new every season. The Universe window draws its cells about 20 % bigger than the first build did, with more air round the planets, codes and difficulty numbers, and opens larger on a big screen; on a small screen it opens zoomed in a little (drag to move, and **Fit** shows all 150 cells).
- **The Radar** scans the unknown cells next to the ones you know, one at a time, queue of three; it does not run while the module is off, upgrading, without power or the Skylab destroyed. You can only fly to cells you know.
- **A trip.** Fit an engine in the Engine module and lasers in the Defense module (their amplifiers go with them), feed the magazine from the Ammo Printer (automatically, or with **Load**), pick a known cell the Defense level may enter and read the preview: the time, the aliens met, the kills and bounty an hour, what binds them, whether the hull holds and when it would not. **Depart,** and **Recall** whenever you like. Nothing attacks the Skylab on the map: its hull is lost and regained by the arithmetic of the trip.
- **What it pays.** A day out pays at most what 2 hours of active hunting in the cell's tier would (3.4 hours in tier 4); **a cell pays by its own tier**, so a stronger Defense module in an easier cell is paid what that cell pays. A full Bay holds fire; Collect empties it into your wallet and inventory in one go. The loot is Expedition loot: it can never be listed on the Auction.
- **Kills made on expeditions count only for kill missions that name no sector** (up to 250 a UTC day), also for the Challenge line when it has no time and no hull limit. A cell is no sector, so a mission that names one (`x-1` to `x-4`, a Danger Sector or a rival's `x-4`) never takes them, not even in a cell of the same difficulty, and a kill counts for the mission of its own alien. With the missions as they are, that is 21 of the 50 Challenge quests (the big hunts of Seekers, Phantasm, Bulwarks, Goombahs, Crystalys and the Dormant Force) and none of the missions for levels 1 to 8. They never count for Wipe Points, the kill statistics, the ranking or the clans' lines.
- **Destroyed.** At the moment the hull runs out, all production stops (not only the trip); **Repair** is free, takes 60 seconds, and sends the Skylab back to the cell the trip began in. New research and Forgery batches are refused while it is dark. A company change while destroyed keeps it destroyed until you press Repair.
- **The clan sees where its Skylabs are:** the Members list has a Skylab column and the Universe map draws gold markers (a dashed arrow with the time left for a trip, a skull for a wreck). A wreck shows as a trip until its owner looks again.

**P.E.T.s**

| Type | Made from | Boosts it can carry |
|---|---|---|
| Magpie, Tardigrade, Hornet, Retriever | Regular chunk | Credits, Luck, Thulium / HP, Shield, Damage / Damage, Thulium, Shield / Luck, Shield, Credits |
| Pangolin, Packrat, Mole | Mythical chunk (also the four above) | Shield, Credits, HP / Thulium, Luck, Shield / HP, Damage, Thulium |
| Fox, Owl, Drake | Legendary chunk (also the seven above) | Luck, HP, Credits / Damage, Luck, HP / Thulium, Damage, Credits |

| Boost | A boost at level 0 | Each level adds | The most a Station adds |
|---|---|---|---|
| Credits | 1.5 % | 0.2 points | 27.5 % |
| Thulium | 1 % | 0.2 points | 25 % |
| HP | 2 % | 0.2 points | 30 % |
| Shield | 2 % | 0.2 points | 30 % |
| Damage | 1 % | 0.2 points | 25 % |
| Luck | 0.5 points | 0.06 points | 8.5 points |

- **The Station** is a research-unlocked install on your ships, like the Extra Slots CPUs: P.E.T. Station I, II and III (3 hours, 10 hours and 1 day of research, no Dark Matter; 100,000 Credits and 2,000 Thulium, 400,000 and 6,000, 1,500,000 and 18,000 to make) hold 2, 3 and 5 pets.
- **The Cradle** (the Hangar's P.E.T. page) makes a pet from one Cluster Chunk and one Orvium Reinforced Plate: 30 minutes, 3 hours or 12 hours by grade, four jobs in the queue, room for 24 pets and jobs. A Regular chunk makes one of 4 types, a Mythical one of 7, a Legendary one of 10; **Discover** lets the server draw a type you have not found, which is shown when you collect it. The Codex keeps the ten types you have found.
- **Docked pets** add their boosts from your next launch, on top of everything else, and fly beside the ship as tiny drones. They grow from the EXP of your kills, of the rocks you break and of every minute flown outside a safe zone: level 1 at 810 EXP, level 20 at 40,000. Docking, undocking and letting go need the ship parked.
- **The Retriever collects boxes for you.** It takes the nearest box in reach, one box at a time at the normal pickup speed (half a second), and only boxes you could take yourself: the same rules as your own pickup, which reaches 200 units. Its reach grows with grade and level, from 264 units (2.4 ship lengths) for a Regular at level 1 to 880 (8 ship lengths) for a Legendary at level 20. Its tiny drone flies to the box and back.
- **The Mole mines for you.** Every 3 seconds it hits the nearest rock within 600 units with a pulse, in your name: the pay, the Cluster Chunks, the mission progress and the pets' rock EXP are as if you had broken it, and it spends no ammo. It never works the Motherlode or a rock another pilot is breaking (a group mate's rock is fine). A Legendary Mole at level 20 breaks **at least as many rocks an hour as a pilot firing the best rockets** (100 % to 118 % on every map, 105 % on average in Alpha); the weakest Mole the Cradle makes, a Mythical at level 0, breaks 10.5 % as many. Its tiny drone flies to the rock and shines a thin beam on it.
- **Both work whenever you fly,** also when you are not touching the keys, but not from a safe zone, while cloaked, in a jump or while dead. Of each kind the best one in your Station works; a second one only boosts. **The Mole has no daily limit,** so an idle ship that is mining is a target; the asteroid belts' daily limits on credits and Thulium still hold for every pilot, Moles included.
- **Crossbreeding** merges two pets into one of the higher grade: you pick the body and the boosts to keep, never more boosts than the grade holds, and the Retriever's and the Mole's work follows the body; a preview shows the result and the fee (20,000 Credits, 100,000 Credits and 25 Thulium, 400,000 Credits and 150 Thulium by the result's grade). "Nothing to gain" is told when the result equals a parent.
- **Cluster Chunks** drop from broken asteroids with a small chance: Regular from the second tier of rocks up, Mythical from the third, Legendary from the fourth, most often from a Motherlode. The chunk goes whole to the pilot who dealt the most damage and no Luck changes its chance. It is a resource: it cannot be listed.
- **P.E.T.s are yours alone** (not tradeable), stay through the wipe with their Cradle jobs, the Codex and the Station; Cluster Chunks lying in the inventory go with the wipe, those in the Transport Cache stay.
- **Settings > Interface > Show P.E.T.s** shows everyone's tiny drones, only yours, or none.

**Looks: skins, auras and exhausts**
- **Skins** are paint schemes made from each ship's own hull, in ten collections (43 skins): Nature White (snow white with orange), Company Supporter (your company's colour, one skin for each of seven ships), Bloody R.E.D (black and blood red with the clan's logo), and seven holiday collections: Midnight Gala (New Year), Blue Marble (Earth Day), Mimosa (Women's Day), Olive Branch (Peace Day), Sunrise Orbit (equinoxes and solstices), Steady Pulse (World Health Day and Mental Health Day) and Hollow Night (Halloween). The Company Supporter skin always takes the wearer's company colour, so a ship's company stays readable in PvP. Designs wear their ship's skin; your drones wear a livery of a collection.
- **Aura and exhaust:** 24 colours and nine exhaust effects (the plain Ion, twin and helix ribbons, pulses, embers, comet trails, a three-hue prism) and nine aura effects (a soft glow with turning motes and more). Effects are drawn for the nearest 4, 8, 12 or 16 ships by graphics quality; everyone else keeps the standard engine glow.
- **Rarity.** Every look has a rarity, from Common to Eternal, shown on its tile and on another pilot's ship in the Target window.
- **The Hangar's Look section and Wardrobe:** move over a skin, aura or exhaust to try it on your turning ship, click to wear it, on one ship or on all your ships of a model. You change a look in the Hangar or in a safe zone, like your gear.
- **What you own:** skins belong to your account and to a ship model (worn on any ship of that model), and stay through the wipe. **For now an admin issues them:** you get a toast and a soft chime when one arrives. Nothing shows a price.
- **Settings > Interface:** *Show other pilots' looks* (All / Mine only / Off) and *Show pilot effects* (All / Mine only / Off).

**The Energetic Wall**
- **Level 1** is a new Extras item (250 Thulium in the Shop); **level 2** is made in Assembly from a level 1 with 10 Ship Fragments, 2 Power Cores and 600 Thulium after you research it (6 hours). Level 2 looks different: a thicker, solid yellow core and a stronger glow, where level 1 is a thin blue-white line.

| | Level 1 | Level 2 |
|---|---|---|
| Hit points | 30,000 | 90,000 |
| Burns whoever is inside | 2,500 a second, shield first, the owner too | the same |
| Fades | in 60 seconds untouched (a sixtieth of its hit points a second) | the same |

- **Press the slot** (WAL on the hotbar) and a strip 360 units long and 10 wide stands **where your cursor is**, across the line from your ship to it. Its middle is at least 120 and at most 450 units from your ship: a cursor farther away or nearer is moved along the line. While the slot is ready a faint dotted line and a ghost outline show where it will land, red where the server would refuse it. With no aim it stands 220 units ahead of your ship, across your heading. Every laser volley and rocket that crosses it, from either side, hits the wall instead of what is behind it; a blast is shaded by it. A ship destroyed by it dies of radiation, credited to the last enemy pilot who hit it.
- **One wall at a time,** and a 90 second wait of its own. It cannot be put in a safe zone, on a gate or while cloaked.
- **Aliens and company pilots burn in it too** and are not told to go round it; asteroids and walls both stop shots, and the nearer of the two takes it. Davidski is no exception.

**Davidski**
- **Once a day in each world, at a time nobody announces:** at a random moment between 00:00 and 20:00 UTC (it differs from world to world and from day to day) a Davidski comes out on that day's Danger Sector and flies until he is destroyed or the UTC day ends. The sector follows the day: when the day's number divides by 3 he flies DS-1, the next day DS-2, the day after DS-3, in each world.

| UTC day | His sector | For example |
|---|---|---|
| number divides by 3 | DS-1 | 13 and 16 October |
| one more | DS-2 | 14 and 17 October |
| two more | DS-3 | 15 and 18 October |

- **Nobody is told, and only the pilots on his Danger Sector see him:** there is no chat line, no Game Log line, no toast and no kill-feed line when he comes out, moves or falls, except the pay lines of the pilots who fought him: the Game Log tells them *You killed Davidski. REWARDS: ...*, or that he has paid already when their cap for the day or the world's is reached. His name is gold, the Target window shows him and that sector's minimap marks him; the Galaxy map does not. The Auction's Davidski section says only whether he is out today (*Flying today, Not out today, Killed today*), never where or when.
- **A peaceful, killable boss:** he never shoots first, shoots back at whoever hurt him, lets go 10 seconds after the last hit and heals when left alone. He is stronger in the higher worlds, and pays more:

| World | Hull | Shield | A second of fire | Credits a kill | Thulium a kill |
|---|---:|---:|---:|---:|---:|
| Alpha | 858,750 | 1,309,534 | 2,052 | 1,060,000 | 2,850 |
| Beta | 1,288,125 | 1,964,301 | 3,078 | 2,120,000 | 5,700 |
| Gamma | 1,717,500 | 2,619,068 | 4,104 | 3,180,000 | 8,550 |

- **Dead until the next day.** When he is destroyed he stays gone until the next UTC day's moment: there is no comeback after 30 minutes. At the day's end he leaves once nobody has hit him for a minute (a fight is never cut by midnight; after 15 minutes he goes whatever is going on). A wipe or a server restart does not bring him back: his day is remembered, so one who was out and whole is back at once and one who was destroyed stays gone until tomorrow.
- **His pay,** split by the damage dealt as every swarm boss's, also holds 170,000 experience and 740 honor in Alpha (x2 in Beta, x3 in Gamma) and a box for the top dealer. He falls once a day in a world, so the limits of **two paid kills a pilot and eight a world a UTC day** are a safety net (group mates count against their own limit): past them he can still be destroyed and pays nobody.
- **The Auction's Davidski section** lists every kind the Auction lists (83), with unlimited stock. For what the Shop sells he asks **100 times the Shop's price in Credits and 40 times in Thulium** (a Repair Drone I is 500,000 Credits or 1,000 Thulium), the two prices no longer the same worth. The gear the Shop does not sell is his **last resort:** 200 times its reference value in Credits and 80 times in Thulium, and at least 50 times the cheapest other way to get it (a Helios Beam is 682,192,400 Credits or 1,364,388 Thulium). The **rare crafting resources** cost 1,000 times more again (a Power Core is 20,000,000 Credits or 40,000 Thulium). Last resort and rare rows wear a small badge. What you buy from him is plain and **can never be listed again.** The Market's daily buying caps do not apply to his sale. His prices follow the crafts: 29 of the crafts changed in this release cost more from him.
- **In the Rankings** he stands like a pilot, in the Hall of Fame: a row in each world's PvE and PvP board (three rows in the All view, one for each world, told apart by a World column, also in the Ranking window in flight) with a real rank number, no company, and the points of a level 20 pilot: 5,244,880 on the PvE board and 0 on the PvP board. The pilots below him move down one place (three in the All view, where he has three rows). His row opens no profile, he is in no company ladder and he cannot wear the crown. "Davidski" is a reserved name.

**The Recipe Book and Builds**
- **Library > Recipe Book:** every item the game lists, with a search and a filter by type. Pick one and see a chart of what it needs (fold and open its branches), the steps in the order to do them, the full bill (Credits, Thulium, every raw resource, Dark Matter, craft and research time) with what you own taken off, where each part comes from (drops, rocks, bosses, the Skylab, rewards, the Shop), what it is used in, and **Add to build** for equipment. The prices come live from the server's data, so the book follows every rebalance.
- **Library > Builds:** a build is a full loadout of one ship: the ship, lasers and their amps, shields, engines and cores with their cells and thrusters, extras, hull plates, drones with what they carry, a formation, and the ammo and rockets to carry. See its stats (the server's own numbers) and its full cost, step by step, with what you own taken off. **Import** your Hangar's ship or a friend's JSON (paste, clipboard or a file), **edit** it, and export it as text or as a file. The game tells you exactly what it could not import.
- **15 presets:** farming, defense, offense, situative and tank builds for the early, mid and late game. This is a **first set** that will be tuned in later releases.
- **My builds are saved on your account** (up to 50), so they follow you to any computer. The season wipe keeps them; deleting the account deletes them.

**Crafting changes: 63 recipes**
- **Ships.** The **Storm** asks 20 Power Cores and 3 Ancient Control Units (it was 10 and 1). The **Ironclad** asks 500 Ship Fragments, 200 Reinforced Hull Plates, 10 Power Cores and 3 Ancient Control Units (it was 200, 35, 10 and 1). The **Wraith** asks at least as much of every part as both: 500, 200, 20 and 3.
- **Laser parts.** The **Quantum Laser III** takes a third Velkonite Reinforced Plate. The Damage, Crit and Penetration **Amps II to IV** ask twice the Thulium and more parts (II: 20 Cataclysite, 2 Velkonite plates and 50 Ship Fragments; III: 2 Power Cores and 50 Ship Fragments; IV: 4 Dark Matter Plates and an Ancient Control Unit).
- **Propulsion and shields.** The Impulse and Momentum **Thrusters**, the **Engines**, the Absorption and Capacity **Shield Cells**, the **Heavy Shield Core** and the **Adaptive Cores** (the tiers II to IV and the cores' II and III) ask twice the Thulium and more Ship Fragments, Power Cores and plates.
- **The last tier.** Every last-tier craft now asks 4 Dark Matter Plates and at least 1 Ancient Control Unit: the 13 of the Amps IV, the Shield Cells IV, the Thrusters IV, Engine III, Adaptive Core III, the Heavy Shield Core, the Helios Beam, the Base CPU II and the Extra Slots CPU III.
- **The Master Drone upgrade** asks 50,000 Thulium (it was 40,000), 250 Ship Fragments (it was 100), 20 Dark Matter Plates, and the Slave Drone. Its research now needs the Dark Matter Plate research first; pilots who hold the Master Drone research keep it.
- **The 16 formations** ask twice the Thulium and five times the Orvium plates where they ask any: 661,000 Thulium for all sixteen (it was 330,500).
- **Designs.** The Paragon designs cost half the Thulium. The Storm designs ask 5 times the plates, Power Cores, Reinforced Hull Plates and Ship Fragments and 3 times the Ancient Control Units, the Ironclad designs 50 times the Reinforced Hull Plates and 5 times the Power Cores and Ancient Control Units, and the five Wraith designs 5 times the plates and parts and 3 times the Ancient Control Units.
- **Crafts you queued before the update keep the price they were paid.** One edge: a refund of an in-place job whose drone or ship an admin removed before it finished pays what the recipe costs now.

**The EMP Charge**
- **A consumable, carried like a rocket:** a stack of up to 20 (the Shop sells one for 500 Thulium and stops at 20 carried), no Extras slot. Pick it from the new **Consumables** picker on the hotbar; a press spends one charge, with the same pulse, refusals, wait and sound as before. At zero you are told "No EMP Charge left."
- **When the server starts,** every EMP you had (fitted in an Extras slot, loose, in the Transport Cache, on the Auction or in a Lot) becomes one stack. None is lost, and a charge in the Transport Cache stays in the cache. The Auction and Davidski trade it, and it is listed from the station only.
- **The wipe follows the rockets' rule:** the stack is lost unless it is in the Transport Cache.

**The Production Queue**
- **A timeline** that scrolls sideways (Shift and the wheel, drag, the edge arrows or the arrow keys): the finished crafts at the left with Collect, the running one with its progress bar and a Now line, the waiting ones after it. The recipes below no longer jump when the queue grows.
- **Crafts of one recipe stack** into one block (for example Laser Damage Booster II x8); click it to see the single crafts, and Collect takes them all.
- **Every recipe card has a number field:** type any amount, use minus and plus or the x1, x5, x10 and Max chips, and press Enter to assemble. If you ask for more than you can make, it tells you the most you can make and what limits it.

**In flight and at the station**
- **Windows in flight.** The Clan and the Auction each have a button in the toolbar at the top left and open as windows over the game, which keep their place and size. In flight the Warden's summon says why it cannot be pressed (inside a safe zone, or outside a company's sectors 2 to 4), and ammo, rockets and EMP Charges are listed from the station only.
- **A chat dock on the station pages** (the Hangar, Research and the others): a bar along the foot that shows how many lines you have not read and the newest one; a click opens the chat with its tabs and input. You can write in Global and Group from the station; Local needs a map. It remembers whether it is open and how tall it is; Enter types and Esc folds it. **Settings > Interface > Chat > Chat dock on station pages** turns it off.

**More changes**
- **Abilities.** Shield Surge restores 18, 36 and 60 % of your maximum shield (it was 30, 60 and 100 %) and its floor is 40 % lower; Emergency Repair restores 12, 15, 19.2 and 24 % of your maximum hull (it was 20, 25, 32 and 40 %). Cooldowns and the 10 second duration did not change. Fights that relied on them are harder: the Pirate Boss needs a slightly bigger group.
- **The hourly Lots** that the System puts up are bid in credits only. The goods the Shop sells for Thulium open at the same worth in credits, at 200 credits to a Thulium. A Lot that is open when the update lands is settled in Thulium, as it was opened.
- **The Giant Excavator.** Anyone at the panel can switch the mined resource while it mines, once every 10 seconds: each box is cut by the seconds spent on each resource, so nothing mined is lost or counted twice. While it works, a stream of light flows from the pulsar into the machine, and flickers in the last minute before the overheat. Each wave brings 3 Slumbering Voids instead of 2, with up to 12 alive on a map, so a run's Voids pay 9,999 Thulium with their boxes where 6,666 were paid.
- **Dark Matter from N.I.K.E.s** has a sound: a soft, low swell as the crates come out of the black hole, for your own N.I.K.E.s wherever you are on the map and for another pilot's when their crates come out within 3,200 units of your ship, once in three seconds at most.

**The Ore Bay**

| Level | 1 | 5 | 10 | 15 | 20 |
|---|---|---|---|---|---|
| Ore it moves an hour | 30 | 90 | 240 | 522 | 960 |
| A day of it, kept | 720 | 2,160 | 5,760 | 12,528 | 23,040 |

- **Three times the 0.4.20 rates and cap.** A Bay you already built keeps what it had stored, now worth three times as much. The Resource storage's own capacity did not change, so the room it has left is what usually limits a transfer from Bay level 5 up.

**What you see and hear**
- **52 new quiet sounds,** each with its own cue: 41 interface cues (the Universe window's scans, the trip's depart, arrive, repair, destroyed, collect and fit, the pets' eight, six for the looks, Davidski's purchase, the queue's stack opening and closing, and eight for the Recipe Book and Builds) and 11 in the world (seven for the wall, the Mole's hum, the Retriever's blip, the excavator's switch and Dark Matter being made). All are on the Sound Effects volume and rate limited.
- **Fifteen new Help cards** (the Engine, Defense and Radar modules, the Trophies Bay, weight, the Universe window, difficulty, the fog, the trip, the preview, the hull and Repair, the magazine, the looks, the Energetic Wall and the Recipe Book), the cards of the P.E.T.s, the Production Queue, the EMP Charge and the wipe rewritten, and every new text in 12 languages.

**For administrators and the server**
- **At the first start:** two data steps (`skylab-solar-v6`, and `emp-stack-v1`, which turns every EMP Charge into one stack per pilot), **twelve new tables** (`SkylabExpedition`, `SkylabFits`, `SkylabTrophies`, `PlayerPets`, `PetJobs`, `PetState`, `PlayerLooks`, `ShipLooks`, `PlayerDroneLook`, `DavidskiLedger`, `DavidskiDay` and `PlayerBuilds`), four indexes and three guarded `ALTER TABLE`s (one adds the column `Laid` to the live `ExcavatorStates`), all idempotent; the backup gate lists 21 lines. Six new data files (`Builds.json`, `Cosmetics.json`, `Davidski.json`, `EnergeticWall.json`, `Expedition.json`, `Pets.json`) and eight changed (`AbilityConfig.json`, `Auction.json`, `Designs.json`, `Excavator.json`, `Market.json`, `Research.json`, `SkylabConfig.json`, `ranking-config.json`), the item, recipe and wipe seeds, 41 new routes, one new client feature string, `expedition`, **two optional environment switches,** `PETS_ENABLED` and `PETS_TRAITS_ENABLED`, and `EMP_STACK_V1_DRY_RUN` for a dry run of the EMP step on a copy of the volume.
- **Admin tools:** a Looks sheet on the pilot editor (give, take back, dress), Davidski's list, move, respawn and remove (a respawn also brings him out before his moment or after a death), a list of the Skylabs on trips, a grant of a pet, and the rewritten **invite code statistics page, visible to admins only:** the Admin Invites tab lists every code with its owner, uses, friends who reached level 5 or played in the last 7 days, what it paid, and its first and last use, with a 30-day chart and the best inviters, sorted, filtered and paged.
- **Rolling back to 0.4.20 after the first start means restoring the volume backup,** not the job's code-only rollback: a 0.4.20 server sets the EMP Charge back to an Extras item, lets a pilot fit the stack, and the first press deletes the whole stack (docs/DEPLOY.md).

## All releases

Each line links the full notes of that release as Markdown (patchnotes/v<version>.md); its HTML page is patchnotes-v<version>.html.

- [0.4.21](https://spacecorps.github.io/play/patchnotes/v0.4.21.md) · 2026-10-13 · The expeditions and companions update: your Skylab flies out on trips across a map of 150 cells…
- [0.4.20](https://spacecorps.github.io/play/patchnotes/v0.4.20.md) · 2026-10-10 · The Ore Bay and the longer sign-in update: ore from a giant excavator can finally be moved into your Skylab…
- [0.4.19](https://spacecorps.github.io/play/patchnotes/v0.4.19.md) · 2026-10-10 · The gear and economy update: every thruster gives 15% less, the Engine II and the Adaptive Core II are made in Assembly…
- [0.4.18](https://spacecorps.github.io/play/patchnotes/v0.4.18.md) · 2026-10-09 · Fixes the Danger Sector update: the pulsars, the giant excavators and the Dormant Swamp now show when you fly into a Danger Sector through…
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
