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
## 0.4.11 · 2026-10-06

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.11)

SpaceCorps 2027 0.4.11 makes ranks per company, draws the drone formations as shapes round your ship, gives the Group window a new layout, makes Unequip all take the equipment off your drones too, and sets the PvE points of the swarm aliens and Clan Wardens by their toughness like the older aliens (their kills already counted; only the figures change). Your rank is now your place among the pilots of your company: the best pilot is its only Senior Admiral (20,000 PvE points at least), the others follow by place, and each rank needs a minimum of PvE points. Each of the 16 formations places your drones in a pattern of its own, other pilots see it, and the Auger is a cone with its tip ahead of your ship. Your rank can go down now, and many ranks will at the first start: read "If you already play".

### What's new

**Highlights**
- **Ranks per company.** Your rank is your place among the pilots of your company, all three worlds together. The best pilot is the only **Senior Admiral** and needs 20,000 PvE points; the others follow down 23 ranks by place, a fifth of them Junior Pilots and the best tenth Captains or better, and each rank also has a **minimum of PvE points**. Only pilots who flew in the last **30 days** are on the ladder. A rank can fall when pilots pass you (never announced); a rise is. The Company page shows your place, percentile, the pilot to pass and the whole pyramid.
- **Drone formations are shapes you can see.** Each of the 16 formations places your drones in a pattern round your ship, turning with it, and other pilots see yours: Testudo a roof of shields, Sanctum a heart, Stiletto a sword, Gyre a wheel and **Auger a cone round the ship with its tip ahead**. With no formation (Standard) they fly the escort you know.
- **The Group window** puts the shield bar (blue) under the hull bar (green), and a groupmate's target to the right of the bars.
- **Unequip all** in the Hangar's Spaceship view also takes the lasers and shields off your drones, with the amps and cells in them. Your drones and the formation you wear stay.
- **Swarm aliens and Clan Wardens count by their toughness.** Their kills counted before; their PvE points now follow the same rule as the Seeker, Phantasm, Bulwark, Goombah and Crystalys, and the PvE card (the (i) on the PvE tiles) lists them.

**If you already play: what changes for you**
- **Many ranks fall at the update, once.** The ladder is relative, so the rank your PvE points gave in 0.4.10 is not the rank your place gives now (the Senior Admiral needed 750,000 points; it needs 20,000 and first place). Nobody sees a "rank down" message; if your place now gives a rank above the best one you were told, you see **Promoted** once at your next launch.
- **A rank is no longer for life.** The season wipe keeps your points and so your place, but your rank follows the company: it falls when others pass you, and rises when you pass them or pilots leave the ladder.
- **30 days away takes you off the ladder:** you count as a Junior Pilot until you launch again or open the Company page, and then you take your place back with the points you left. The 30 days start at the update, so nobody is off the ladder on the first day.
- **Your PvE points can go up at the first start** if you killed swarm aliens or Clan Wardens (Pirate Boss 15, Pirate Scout 4, Wardens 13 to 35): the server counts every pilot's kills again at its start. No figure went down, so the new figures take no point away.
- **Unequip all** in the Spaceship view now also empties your drones' slots; the items go to your inventory.
- **Small changes:** your drones appear in place when you launch instead of flying out from the ship, and each Group window row is 4 points taller (44, it was 40).
- **A 0.4.10 client keeps working** against the 0.4.11 server, but the new Company page, the shapes, the Group window and the drones in Unequip all need the 0.4.11 client.

**Company ranks: the ladder**
- **The order:** the pilots of a company, all worlds together, are ordered by their stored PvE points (a tie goes to the higher level, then to the older pilot). Nothing else counts: not PvP points, honor, credits, the clan or Wipe Points.
- **The shares:** place 1 is the Senior Admiral, alone. Of the pilots behind him 20.1% are Junior Pilots, and each rank above holds fewer: the best 10.2% are Captains or better, the best 4.9% Majors or better, the best 0.86% Generals or better, and 0.15% are Admirals.
- **The minimum:** a rank also needs PvE points, and your rank is the lower of what your place gives and what your points allow. A company that has only just begun cannot hand out the top ranks for nothing.
- **Small companies:** the cuts round down, so a company has a pilot at a rank by place only when it is big enough to fill it with a whole pilot: 11 pilots for a Captain, 46 for a Colonel, 118 for a General, 301 for a Junior Admiral, 675 for an Admiral. In a company of 30 the second pilot is a Senior Major at best. The last column of the table is the smallest company that has a pilot at the rank by place; at a slightly larger size the band can be empty again when a cut moves.
- **Who is on the ladder:** pilots of a company with PvE points above zero who flew in the last 30 days. Everybody else is a Junior Pilot wherever a rank shows (ship tags, chat, the Hall of Fame, profiles) and has no place. A pilot who comes back is placed with the points he left, when he launches or opens the Company page.
- **How a rank moves:** a kill moves you up the order at once and every symbol on the screen follows in the next update. **Promoted** shows when you reach a rank above the best you were told since you last launched, so a pilot who is passed and passes back is not told twice. A fall is silent. From Junior Major up your company, flying in your world, hears about a promotion your own points earned.
- **The Company page** (Company ranking) shows your rank and your place ("Place 16 of 31") with your percentile ("Top 52%"); under the bar to your next rank either "301 PvE points to pass nova and reach Sergeant" (the place holds you) or "600 PvE points to Junior Colonel" (the minimum holds you); the best pilot of your company; **All ranks**, the pyramid of the 24 ranks with the share of the company each holds, how many pilots hold it now and its minimum points; and the best 50 pilots of your company across all three worlds.

  | # | Rank | PvE points needed in 0.4.10 | Minimum in 0.4.11 | Share of the pilots behind the leader | Held by place from a company of |
  |--:|---|--:|--:|--:|--:|
  | 1 | Junior Pilot | 0 | 0 | 20.1% | 2 |
  | 2 | Pilot | 150 | 150 | 16.1% | 4 |
  | 3 | Senior Pilot | 350 | 350 | 12.9% | 6 |
  | 4 | Junior Sergeant | 700 | 610 | 10.3% | 3 |
  | 5 | Sergeant | 1,200 | 800 | 8.24% | 4 |
  | 6 | Senior Sergeant | 2,000 | 1,000 | 6.59% | 8 |
  | 7 | Junior Lieutenant | 3,000 | 1,300 | 5.27% | 5 |
  | 8 | Lieutenant | 4,500 | 1,500 | 4.22% | 6 |
  | 9 | Senior Lieutenant | 6,500 | 1,900 | 3.38% | 8 |
  | 10 | Junior Captain | 9,000 | 2,200 | 2.70% | 9 |
  | 11 | Captain | 12,500 | 2,600 | 2.16% | 11 |
  | 12 | Senior Captain | 17,000 | 3,000 | 1.73% | 14 |
  | 13 | Junior Major | 23,000 | 3,500 | 1.38% | 17 |
  | 14 | Major | 31,000 | 4,100 | 1.11% | 22 |
  | 15 | Senior Major | 42,000 | 4,700 | 0.88% | 28 |
  | 16 | Junior Colonel | 58,000 | 5,600 | 0.71% | 35 |
  | 17 | Colonel | 80,000 | 6,500 | 0.57% | 46 |
  | 18 | Senior Colonel | 110,000 | 7,700 | 0.45% | 61 |
  | 19 | Junior General | 150,000 | 8,900 | 0.36% | 84 |
  | 20 | General | 200,000 | 10,000 | 0.29% | 118 |
  | 21 | Senior General | 280,000 | 12,000 | 0.23% | 178 |
  | 22 | Junior Admiral | 380,000 | 14,000 | 0.19% | 301 |
  | 23 | Admiral | 520,000 | 17,000 | 0.15% | 675 |
  | 24 | Senior Admiral | 750,000 | 20,000 | the best pilot, alone | 1 |

**Drone formations you can see**
- **One pattern for each formation,** drawn for your ship and for every other pilot's, turning with the ship's heading: the pattern is built for exactly the number of drones you own (1 to 8), not cut from a bigger one, so with one more drone the pattern is made again and the others move a little to make room. Which formation a ship wears is told to everybody who sees the ship; a ship that comes into view has its drones in place from the first frame.

  | Formation | The shape round the ship | Moves |
  |---|---|---|
  | Testudo | a roof of shield tiles in two columns over the wings, the ship's spine left open | hovers |
  | Adamant | a diamond: a corner ahead, behind and to each side | hovers |
  | Sanctum | a heart ahead of the nose, its point towards the ship | hovers |
  | Redoubt | a dome: a ring hugging the hull, a pair over the flanks and a crown on top | hovers |
  | Cordon | a wide oval ring round the ship | turns once in 24 seconds |
  | Rampart | a wall across the nose, its ends reaching forward like claws | hovers |
  | Asterism | a four-pointed star round the ship | twinkles every 1.5 seconds |
  | Bodkin | an arrow with your ship as its head: a tip ahead, barbs on the flanks, a shaft behind | hovers |
  | Ballista | a V ahead of the ship, its arms sweeping back along the sides | hovers |
  | Centurion | a block: a rectangle of guards round the ship | hovers |
  | Shrike | a trident: a row of three across the nose and three tines ahead, the middle one longest | hovers |
  | Culler | wings: a fan of four drones on each side | flap every 2.4 seconds |
  | Gemini | twin spears: a column of four along each flank, the tips ahead of the nose | hovers |
  | Stiletto | a sword with your ship as its hilt: a blade of drones ahead of the nose and a pair at the nose as the crossguard | hovers |
  | Gyre | a wheel round the ship, a rim and a hub | spins once in 6 seconds |
  | Auger | **the drill: a cone round the ship**, its tip ahead of the nose and opening backward at 25 degrees to the line you look along | spirals about that line once in 3 seconds |

- **The Auger** is the owner's drill: its axis is the line your ship looks along, so it points where you point and turns with you. With eight drones they sit on the tip and three rings behind it (1, 2, 2 and 3). From the usual camera, looking down at 70 degrees, eight drones read as a sparse spiral; tilt the camera with a right-drag to see the cone.
- **Changing formation** glides each drone to its new place in 0.8 seconds, round your hull and never through it, never a jump. A swap during a glide starts from where the drones are.
- **Standard** (no formation worn) is the escort of 0.4.10, the 2-2-4 layout, unchanged. Your drones now appear in it in place at launch instead of flying out from the ship.
- **Other pilots see your shape** (the server told them which formation you wear since 0.4.10; 0.4.11 also says it in the join, so a ship that is already there is not drawn in the wrong shape for a moment).
- **A picture of each pattern** turns in the tooltip of a formation slot, of an entry of the Formations menu and on the formation's item card (the Hangar's Drones view, Assembly and the Shop). It shows the pattern round a Paragon with eight drones.
- **Settings:** Show My Drones and Show Enemy Drones turn the drones off as before. **Reduce Motion** holds the turning, flapping and twinkling patterns still and shortens the glide to 0.2 seconds. Ships more than 3,500 units from the camera draw no drones, and at most the nearest 64 ships do.
- **What did not change:** every formation's bonuses and prices, the 2-second limit, the sound of a change (the one 0.4.10 added) and which drones you own. The shapes are the client's drawing; the server does not know where a drone flies.

**The Group window**
- **Hull above shield:** each member's green hull bar has the blue shield bar beneath it, both as wide as the row's text column while the member has no target beside them. A ship with no shield fitted shows the hull bar alone, in the same place.
- **The target to the right:** a member who is shooting has the mark, name and two thin bars of what he shoots at to the right of his bars, in the lines of the two bars; beside a target the member's bars are shorter (at the default width 105 points long, 195 without a target). The distance and the arrow stay at the top right of the row. In the new form a row is **44 points tall (it was 40) with or without a target**, so nothing jumps when a mate starts or stops shooting.
- **Narrow windows keep the old form:** below about 240 points of window width there is no room beside the bars, and the target goes beneath them as in 0.4.10, making that row 21 points taller. The default width of 250 points is wide enough; a width you saved is kept.
- **Long names:** the name keeps at least 90 points; when it would be cut shorter the level text leaves the line (it stays in the hover card), and the place text is cut with an ellipsis before it could lie over the name. At the default width a long target name such as "Pirate Boss Xerxes" is cut with an ellipsis (the hover card has it whole).
- **Hover** shows one card at a time: the hull bar's, the shield bar's, the target's or the member's.

**Unequip all**
- **What it does now:** in the Hangar's Spaceship view the button takes off every item of the configuration on show, **including the lasers and shields in your drones' slots** and the amps and cells fitted in them. They return to your inventory. Its tip reads "Unequip every ship and drone item in this configuration". The Drones view's button, which took only the drones' items, is unchanged.
- **What stays:** your drones. A drone is owned, never fitted, so there is nothing to take off a ship; what you fit "on a drone" are the lasers and shields in its slots. The formation you wear stays too: it is a choice, not equipment.
- **All or nothing:** the server now does the whole list in one step, so a failure half way leaves everything as it was. No item is lost or duplicated. The other configuration is not touched. The same rules as before apply: docked, or in flight from a safe zone and out of combat, and an item in the Transport Cache refuses the whole list.
- **In flight** your ship follows at once: no laser, no shield. Your hull does not change (nothing in a drone slot adds to it), and your shield is only cut to the new maximum.

**PvE points: the swarm aliens and the Clan Wardens**
- **The rule is the old aliens' rule:** a kill pays the square root of the alien's hull plus shield over 1,600 (a Seeker's), rounded: Seeker 1, Phantasm 2, Bulwark 4, Goombah 7, Crystalys 16. The swarm aliens and the Clan Wardens' crews are held to it now. A kill of one counted before (since 0.4.8, and the Wardens since 0.4.10); their figures were set by hand and some paid less than an old alien of about the same toughness (a Pirate Scout paid 1 where a Bulwark pays 4).
- **19 of the 29 figures changed, none went down:**

  | Alien | Before | Now |
  |---|--:|--:|
  | Pirate Boss | 10 | 15 |
  | Pirate Scout | 1 | 4 |
  | Dormant Pulse | 10 | 11 |
  | Brood Warden I, II, III | 10, 15, 25 | 14, 18, 35 |
  | Siege Warden I, II, III | 10, 15, 25 | 13, 17, 32 |
  | Wrath Warden I, II, III | 10, 15, 25 | 14, 18, 34 |
  | Brood Drone III | 1 | 2 |
  | Siege Escort I, II, III | 1 | 2, 3, 6 |
  | Wrath Guard I, II, III | 1 | 2, 3, 6 |

- **What stays:** Seeker 1, Phantasm 2, Bulwark 4, Goombah 7, Crystalys 16, Seeker Slave 1, Brood Drone I and II 1, and two kinds that pay **more** than the rule: the Boss Seeker 5 (the rule says 2) and the Dormant Force 25 (the rule says 16), so nobody loses points at the recount.
- **The PvE card** (the (i) on the PvE tiles) lists the five old aliens and now a row for each swarm (Seeker Swarm 1 to 5, Pirate Swarm 4 to 15, Dormant Swarm 11 to 25) and one for the Clan Wardens (1 to 35), each from the member's figure to the boss's. The Ranking calculation's line "Points per alien kill" lists every alien with its figure.
- **Who is paid:** as for any alien, the pilot whose hit claimed it, or, for a swarm's leader and a Dormant Pulse, every party with at least 5% of the damage; a group's kill pays the weight to its payee and the others their share of the experience.
- **Not changed:** the Wipe Point kill milestones count the five old aliens only and pay nothing for a swarm alien; a group mate gets experience but not the weight.

**The wiki**
- **Ranks** is rewritten for the company ladder (place and minimum, who is on the ladder, how a rank moves, the Company page, how long it takes) with a new picture of the pyramid, and the Company page picture is retaken. The Clans, Company Pilots, Getting Started and Wipe Timeline articles carry the matching sentences, and the PvE tables have the new figures. All in the game's 12 languages.

**For administrators and the server**
- **One new table, `PilotSeen`** (`PlayerId` primary key, `Day`: the Unix day a pilot last flew), made when the server starts, only while `dormantDays` is above 0, with one row for each pilot; at the first start every pilot gets today's date. A 0.4.10 server ignores it. **No data step, no rename, no startup repair, no new file under `Resources/`, no new environment variable.** The release job's backup check finds exactly one line: `schema CREATE TABLE IF NOT EXISTS PILOTSEEN`.
- **Changed files:** `Resources/Ranks.json` (version 2: `scale`, `dormantDays` 30, `rebuildSeconds` 600 and the share of each rank; `points` is the minimum now) and `Values/ranking-config.json` (the 19 figures). **Deploy the image, never a 0.4.11 binary on 0.4.10's files:** the old `Ranks.json` stops the start with "Refusing to start: Resources/Ranks.json: ...".
- **The ladders** are lists in memory, read at the start and again every 10 minutes; a kill moves one entry. The start logs `Company ladders: N pilots in M companies, K left off for not having been seen in 30 days` and one line for each company with its best pilot's points and rank. An admin's edit of a pilot's level, experience or company and a deleted account move the ladder too.
- **One new key on the wire:** the join (`MapDetails`) says which formation each ship wears; older clients ignore it.
- **Rolling back to 0.4.10** (code only) starts cleanly. A pilot whose stored rank is lower than his 0.4.10 rank sees **Promoted** once at his next join.

## 0.4.10 · 2026-10-05

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.10)

SpaceCorps 2027 0.4.10 rebuilds the Skylab's numbers and adds 16 drone formations in two new research trees, reworked level missions (quest items, visits, stays, hull limits) with a Challenge line of 50 very hard missions, a daily line of missions for clans with three Clan Wardens and permanent clan boosts, company ranks, a ring of jump gates between the companies, and a wiki with pictures and search. The Skylab's farms, collectors, Storage, Forgery and Solar each have their own output, price and upgrade time at every one of their 20 levels; you keep your levels, nothing is charged or refunded, and what your farms had stored is paid out once at the old rate. A Solar upgrade now stops the farms of almost every station until it is done. The 16 formations change your ship's shield, hull, speed, lasers, rockets and kill rewards, and you change the one you wear from the hotbar every 2 seconds. It also fixes a ship's total shield falling when you add a shield or a cell, and closes two loopholes in how lasers and extras are fitted. Some things get stricter or cheaper, so the "If you already play" list below is worth reading.

### What's new

**Highlights**
- **The Skylab has new tables.** The Credit Farm makes 500 credits an hour at level 1 and 50,000 at level 20, the Thulium Farm 50 to 1,600 Thulium an hour, the Velkonite Collector 10 to 80 and the Orvium Collector 10 to 40 ore an hour. The first upgrade of each of the farms, collectors, Storage, Forgery and Solar takes 5 minutes and the last 12 to 36 hours, and the climbs cost far less Thulium than before. The Credit Farm is now built free. The whole station to level 20 takes about 18 days instead of 22.6.
- **Solar makes only 25% of its power while it upgrades.** For almost every station that means the farms and collectors stop until the upgrade is done (up to 24 hours at the top). Plan a Solar upgrade like a blackout of your farms.
- **16 drone formations**, researched in two new trees of the Research Centre (Defence 6, Strike & Mobility 10) and crafted in Assembly for 7,000 to 46,000 Thulium each. You own them, drag any of them (and a built-in Standard) from the hotbar's Formations menu onto a slot, and click the slot or press its key to wear that formation. You can change once every 2 seconds, in a fight too. A formation works while you own at least one drone.
- **Level missions are chains.** Of the ten missions of every level, three carry a **quest item** home to Mission Control, two visit marked points, two hold a sector for a number of minutes and three stay plain kill missions; the new steps are added to the kills, and a step can say "do not lose more than N hull points" or "do not die". 64 missions were reworked; levels 3 and 4 are no longer one long Phantasm grind.
- **The Challenge line:** 50 hard missions in five tiers (Proving Ground, Iron Border, The Centre, The Abyss, Legends), from pilot level 3, with kills by the thousand, vigils of up to 3 hours, convoys, clean runs and a black hole walk, paid in credits, Thulium, experience, items and boosters (honor in tier I). They take your boosters, the world multiplier and your clan's boosts like any other mission.
- **Clans have a daily line:** four hunts or patrols in order and then the day's **Clan Warden**, a boss only your clan can hurt (three Wardens in rotation, each in three strengths). A finished line pays 100 clan points, which the Leader and Co-Leaders spend on three permanent boosts of ten levels: **Clan Damage** (+0.5% per level), **Clan Thulium** and **Clan Credit** (+1% per level).
- **Company ranks:** your PvE points earn a military rank, 24 of them from Junior Pilot to Senior Admiral. A small symbol shows before your name on ship tags, in chat, in the kill feed and on profiles, and your rank keeps through the season wipe.
- **Ships:** the **Storm** has 13 lasers (it had 10), 4 core and 2 auxiliary generator slots and 150,000 hull, and flies at 250. The **Protos** flies at 160 and the **Wraith** at 220. The four ships you buy (Protos, Kitefin, Ostirion and Nomad) have **2 extra slots** instead of 3; the four you craft keep 3. A new pilot starts with a Base CPU I and a Repair Drone I fitted in the Protos' two extra slots.
- **A ring of jump gates:** each company's x-4 sector has a second gate, to another company's x-3 (Mars M-4 to Terra T-3, Terra T-4 to Galactic G-3, Galactic G-4 to Mars M-3), so there is a loop between the maps that does not cross the Danger Sectors.
- **Fixes:** adding a shield or a shield cell can no longer lower a ship's total shield, adding a thruster or an engine can no longer lower its speed, an extra now has to sit in a box the ship really has, and a laser fitted with no slot named takes a free laser slot.
- **Aliens no longer push each other apart**, which takes work off the server on every tick. **Repair Drones fitted as extras** now fly out and beam your hull for everyone to see. **20 new quiet sounds.**
- **The wiki has pictures and a search:** every article has its own icon, most open with a banner, small icons stand in front of names, a click shows a picture large, and a search box finds text across all articles in your language. New articles: Drone Formations and Ranks.

**If you already play: what changes for you**
- **Your Skylab keeps its levels, and its numbers change.** Nothing is charged or refunded for the difference. At the update everything your farms and collectors had stored (up to 72 hours of each, the "hopper") is **paid out once, at the old hourly rate,** and the hoppers start empty. At high levels the new farms make much less than the old ones (a level-20 Credit Farm 50,000 credits an hour, it made 597,630; a level-15 Thulium Farm 950 Thulium an hour, it made 1,969), the Thulium Farm at levels 2 to 8 and the Orvium Collector at levels 1 to 4 make more than before (up to 30% and up to two thirds). Prices and times follow the new tables from level 1 on, so a climb you have not made yet costs far less Thulium and its last steps take hours, not days; its first upgrade takes 5 minutes where it took 36 seconds to 3 minutes, and some climbs cost more credits (see "Skylab: the new tables").
- **Solar:** while it upgrades it makes 25% of the power of its current level. The farms and collectors stop for the whole upgrade unless everything else in your station is at least five levels below Solar (a full station needs more); what they hold stays and can be collected. A Solar upgrade that is running at the update makes 25% from then on. The price of a Solar upgrade is now the Forgery's (24,000 credits for the climb from level 1 to 3 instead of 1,679).
- **The Resource Storage holds a different amount of each ore** (240 of each at level 1, 7,680 Velkonite and 3,840 Orvium at level 20). **Ore you hold above the new limit stays,** but your collectors stop collecting that ore until you spend it below the limit.
- **Mission Control has new missions.** If you finished one of the 64 reworked level missions, it is offered again and you do the new version for its **full reward** (credits, Thulium, experience, honor, items). A reward you had finished but not yet claimed is paid at the larger of the old and the new amount. A mission you have under way is carried over to its new steps by the share you had done, never dropped. Your mission count and your Wipe Points never go down, and a mission never earns Wipe Points twice in a season. The 24 level missions that did not change and the 10 Station missions stay as they are. A level's Special is locked again until you have done that level's missions again. You see one notice at your first flight.
- **The four ships you buy have 2 extra slots** (Protos, Kitefin, Ostirion, Nomad), so with the Extra Slots CPUs I, II and III they have 5, 7 and 9 extra slots; the Paragon, Ironclad, Wraith and Storm keep 3 (6, 8 and 10). If you had a third extra fitted on one of the four, it is **unequipped into your inventory** at the update (nothing is deleted; you get one notice at your first flight).
- **The Storm** is now a Class IV Dreadnought by the wiki's rule (more than 10 lasers). The Wraith is a little slower and the Protos a little faster. No ship's price or recipe changed.
- **Shield totals can go up, never down.** If your loadout was hit by the shield bug (a shield or a cell lowered the total), it reads more now.
- **Formations work for every pilot who owns a drone.** You do not fit them: owning one is enough, and **all the formations you own stay through the season wipe** like your drones. Research and crafting of a formation are once per account.
- **Aliens may overlap** and several can stand on the same spot; they still keep out of your ship's hull. An alien that gives up on a pilot flies to a random point of the map again.
- **A Warden is not a Seeker:** a Clan Warden does not count for any alien-kill mission. Hard (Challenge) missions pay base x world x boosters x your clan's boosts, so in Gamma a mission pays three times its printed numbers before any booster.
- **Clan points, boost levels and the daily lines start at zero** at the update (nothing existed before) and again at every season wipe. **Ranks keep through the wipe.**
- **A 0.4.9 client keeps working** against the 0.4.10 server, but it cannot take the missions that need the new game, wear a formation or see the clan line and the ranks (see Updating).

**Skylab: the new tables**
- **Every module has its own numbers at each of its 20 levels** (the Credit Farm, Thulium Farm, Velkonite Collector, Orvium Collector, Resource Storage, Forgery and Solar; the Core and the Research Centre keep theirs):

  | | Level 1 | Level 10 | Level 20 | 0.4.9 at level 20 | First upgrade | Last upgrade |
  |---|--:|--:|--:|--:|--:|--:|
  | Credit Farm (credits an hour) | 500 | 7,500 | 50,000 | 597,630 | 5 min | 12 h |
  | Thulium Farm (Thulium an hour) | 50 | 450 | 1,600 | 7,310 | 5 min | 36 h |
  | Velkonite Collector (ore an hour) | 10 | 32 | 80 | 833 | 5 min | 24 h |
  | Orvium Collector (ore an hour) | 10 | 24 | 40 | 416 | 5 min | 36 h |
  | Resource Storage (Velkonite / Orvium held) | 240 / 240 | 1,920 / 1,440 | 7,680 / 3,840 | 62,450 each | 5 min | 12 h |
  | Forgery (ore per plate, Velkonite / Orvium) | 40 / 80 | 35.5 / 71 | 30 / 60 | 28.6 / 57.2 | 5 min | 24 h |
  | Solar | same power as before | | | | 5 min | 24 h |

  A farm's price and time follow the table for every step: for example the Credit Farm costs 5,000 credits and 1 Thulium for the first upgrade and 7,000,000 credits and 550 Thulium for the last, and the Thulium Farm 7,000 credits and 45 Thulium for the first and 8,500,000 credits and 16,000 Thulium for the last. The numbers are in the Skylab's help cards and on the wiki's Skylab page.
- **What a module costs from its build to level 20** (the build and all 19 upgrades):

  | Module | Credits before | Credits now | Thulium before | Thulium now |
  |---|--:|--:|--:|--:|
  | Credit Farm | 20.1 million | 26.2 million | 2.0 million | 2,399 |
  | Thulium Farm | 796.8 million | 32.3 million | 79.7 million | 67,890 |
  | Velkonite or Orvium Collector | 66.5 million | 21.0 million | 3.3 million | 78,950 |
  | Resource Storage | 20.9 million | 18.2 million | 1.0 million | 2,649 |
  | Forgery | 66.5 million | 35.0 million | 3.3 million | 37,300 |
  | Solar | 1.0 million | 35.0 million | 104,000 | 36,850 |

- **Whole station:** to take the seven tabled modules from their builds to level 20 now costs 188,739,000 credits and 304,988 Thulium in all. The Core's timers are unchanged and still set the pace: the whole station to level 20 takes about 18 days (it took 22.6), the Thulium Farm and the Orvium Collector finishing last, 36 hours after the Core.
- **Build prices:** the Credit Farm is built free (it cost 1,000 credits and 100 Thulium). Solar is still 500 credits and 50 Thulium. The Velkonite and Orvium Collectors cost 20,000 credits and 500 Thulium (10,000 credits before), the Resource Storage 5,000 credits and 250 Thulium (10,000 and 500), the Forgery 5,000 credits and 500 Thulium (10,000 and 500). The Thulium Farm, the Core and the Research Centre are as before.
- **Solar:** its power at each level is unchanged. It is built for 500 credits and 50 Thulium; its upgrades now cost and take what the Forgery's do. **While it upgrades it makes 25% of the power of its current level;** the new level's power starts when the upgrade ends. A station that then uses more than it makes stops: every farm and collector stops producing, and the Forgery starts no new batch, until the upgrade is done. Only a station whose other modules are at least five levels below Solar runs through it (a full station with the whole supply chain needs a little more). A module that is upgrading or switched off draws no power, so lifting the farms together with Solar costs nothing extra. The help cards, the power tip and the Station missions' briefings say so in all 12 languages.
- **Storage:** a bank holds its own amount of each ore. Ore above the new limit stays and the collector stops until you are below it.
- **Forgery:** a plate takes a little less ore with every level, from 40 to 30 Velkonite and from 80 to 60 Orvium (level 14 Orvium: 67.5).
- **One payout at the update:** every uncollected pile of the farms and collectors, at most 72 hours of each, is paid once at the old rate of that module's level and the hopper is emptied. It is a payout, not a collection: the Station missions that ask you to collect do not count it, and no booster touches it. A level-10 pilot gets at most 1,487,595 credits, 38,176 Thulium, 6,437 Velkonite and 3,218 Orvium; a level-20 pilot at most 43,029,388 credits and 526,291 Thulium.
- **Research from ore:** a Velkonite is now worth 210 science and an Orvium 321 to the Research Centre (they were 40 and 80), to match the smaller collectors. **This means cheaper ore, not faster research:** a research still burns 1 science a second (2 with a boost), so an hour of research costs 17 Velkonite or 11 Orvium instead of 90 or 45, and the time and the tank limit you, not the ore.
- **Station missions:** the briefings of First Farm, Payday, Brighter Panels, Growing Season and Open the Supply Line quote the new prices, timers and the Solar rule. Their goals and rewards are unchanged; they are paid with the same multipliers as other missions (see Missions).

**Drone formations**
- **What a formation is:** a pattern your drones take round the ship. Each gives some bonuses and charges some prices, for example a bigger shield for weaker guns. **You own a formation; you do not fit it.** A formation works while you own at least one drone (a Slave Drone or a Master Drone; it need not be fitted), and more drones do not make it stronger. One formation is worn at a time.
- **Wearing one:** the hotbar has a **Formations** menu next to Ammo, Rockets and Extras. It lists every formation you own and a built-in **Standard** (no formation, always there). Drag any entry onto a slot of the hotbar; clicking that slot or pressing its key makes that formation the one you wear, and a Standard slot takes the formation off. You can change **once every 2 seconds**, with no lock in a fight; in a safe zone a change starts no timer. Swapping between your two configurations does not change the formation you wear and does not start the timer. The Ship window shows the formation you wear and the Target window the one your target wears. A quiet sound plays when you change.
- **Research and crafting:** the 16 formations are 16 technologies in two new Research Centre trees, **Defence** (6: Testudo, Adamant, Sanctum, Redoubt, Cordon, Rampart) and **Strike & Mobility** (10: Asterism, Centurion, Shrike, Gyre, Culler, Auger, Bodkin, Ballista, Gemini, Stiletto). A research takes 10 hours, 1 day or 2 days and needs **5, 13 or 20 Dark Matter** (189 for all sixteen; 339 for the whole tree with the 15 older technologies). Then you craft the formation in Assembly (a new Drones category) for Thulium, 330,500 for all sixteen, plus ship fragments, plates and power cores (the strongest also Ancient Control Units). The chains: Testudo, Sanctum, Rampart; Adamant, Redoubt, Cordon; Asterism, Bodkin, Ballista; Centurion, Shrike, Culler; Gemini, Stiletto; Gyre, Auger. All sixteen researches one after another take 16 days 2 hours (half of it with the Thulium boost).

  | Formation | Gives | Costs | Research | Dark Matter | Thulium |
  |---|---|---|--:|--:|--:|
  | **Defence** | | | | | |
  | Testudo | +14% shield | -5% all damage | 10 h | 5 | 7,500 |
  | Adamant | regenerates 1.2% of your maximum shield a second (up to 5,750) | -15% hull | 10 h | 5 | 9,000 |
  | Sanctum | +10% shield, +15% hull | -9% laser damage | 1 day | 13 | 20,000 |
  | Redoubt | +38% shield, regenerates 0.7% a second (up to 4,500), rocket reload 27% shorter | -12% laser damage, -11% speed | 1 day | 13 | 21,000 |
  | Cordon | +95% shield | -3% speed, -11% laser damage, rocket reload 11% longer | 1 day | 13 | 21,500 |
  | Rampart | +17% shield absorbance | -17% speed | 2 days | 20 | 38,500 |
  | **Strike & Mobility** | | | | | |
  | Asterism | +24% rocket damage, 7% chance to dodge a direct hit | rocket reload 35% longer | 10 h | 5 | 7,000 |
  | Centurion | +32% honor from alien kills | -5% laser damage, -5% hull, -7% shield | 10 h | 5 | 8,000 |
  | Shrike | +7.5% laser damage to aliens, +6% XP from alien kills | -6% shield absorbance | 10 h | 5 | 8,500 |
  | Gyre | +10% speed | -11% laser damage, drains 0.5% of your current shield a second in a fight | 1 day | 13 | 20,000 |
  | Culler | +12% damage to aliens, +12% XP from alien kills | -10% speed | 1 day | 13 | 20,000 |
  | Auger | +21% laser damage | -9% speed | 1 day | 13 | 20,500 |
  | Bodkin | +29% rocket damage | -6% laser damage | 1 day | 13 | 21,000 |
  | Ballista | +55% rocket damage | -13% hull | 1 day | 13 | 24,000 |
  | Gemini | +9 points of shield penetration | -22% shield | 2 days | 20 | 38,000 |
  | Stiletto | +16 points of shield penetration, +13% hull | drains 3.5% of your current shield a second in a fight | 2 days | 20 | 46,000 |

- **Rockets:** a formation changes all 14 rockets, the N.U.K.E. and the N.I.K.E. included. A rocket's damage factor is fixed the moment you fire it (changing formation while it flies changes nothing), and so is the wait after a launch: Asterism lengthens it by 35 percent, Cordon by 11 percent, Redoubt shortens it by 27 percent, but never below the rocket's flight time plus a tenth of a second (a N.U.K.E. waits at least 4.1 s, a N.I.K.E. at least 4.6 s). The rocket cards show the damage you would deal with your formation. A formation's rocket bonuses together can never raise a rocket's damage by more than 59 percent, so the one-shot limits of the big rockets hold (a N.I.K.E. with the best formation still cannot destroy a fresh Paragon at once).
- **Hull and shield:** a formation with a hull percent changes your ship's **maximum hull** everywhere you read it (flight, the Ship window, the Hangar tile). A change keeps your hull's fraction: 80 percent of the old maximum becomes 80 percent of the new one, both ways, so changing back and forth gives no free hull. Your current shield is only cut when the maximum falls, and nothing is refilled when it rises. Shield Surge and Emergency Repair heal the same amount whatever you wear.
- **Evasion** (Asterism, 7%) is a **chance to dodge**: each direct hit on you (a laser volley, a direct rocket, an alien's shot) has that chance to do no damage at all, and a floating **"Miss"** shows over your ship, with one quiet sound. The other hits land whole. An area blast has no aim and is never dodged.
- **Shield regeneration and drain:** Adamant and Redoubt regenerate part of your shield every second, in a fight or not, up to the cap shown. Stiletto and Gyre take a share of your current shield every second while you are in a fight (10 seconds after a hit or a shot) and never inside a safe zone; the drain stops the moment you change formation.
- **Penetration** adds to your ammo's and a direct rocket's shield penetration; the sum stops at 40 percent. **XP and honor** bonuses (Shrike, Culler, Centurion) count only after the formation has been worn for 10 seconds, and only for alien kills (swarms included), not for missions or pilots, so changing in and out does not farm them.
- **The Hangar and the item cards:** the Hangar's Drones view lists the formations you own; a formation's item card lists its bonuses in green and its prices in red, and each of the 16 has its own picture (a block under a roof, an arrow, a star, twin spears, a diamond and so on, coloured by role). Other pilots see which formation you wear.
- **What it is worth:** the model puts the best formation of the moment at about 14 percent over a plain ship for a pilot who owns all sixteen and changes between hunting, a duel and a flight; the best single formation in a duel (Gemini) about 18.5 percent. A pilot who swaps formations with N.I.K.E.s in hand is about 1.3 times a plain ship in a duel. These are the balance model's numbers, not measured in play; the first season will retune them.

**Missions: levels 1 to 8**
- **New steps.** *Quest items:* an item that drops only for you from an alien (after enough kills it is guaranteed), one that lies on the map, or one that comes from the Nth kill; you pick it up and **carry it home to Mission Control**. A cyan beacon marks it for you alone, and the Active Quests window shows "Carrying" and how far Mission Control is. *Visit:* fly to a marked point (a gold ring on the map and the minimap). *Stay:* hold a sector for a number of minutes outside the safe zones, in total or in one stretch (a death starts a one-stretch stay again). Items stay in the company sectors; visits and stays can go to the Danger Sectors. A Base CPU or Jump CPU cannot be used while you carry an item.
- **Conditions.** A whole mission or a single step can say **"Hull limit N HP"** (do not lose more than that many hull points while it runs: the number the hull bar shows, after shields and absorbance; black hole radiation counts, shields do not) and **"No death."** Mission Control and the Active Quests window show a pill and a live bar ("Hull damage: 1,240 / 3,000"). If you break a condition the step starts again, a carried item is lost and must be fetched again; nothing is lost for good. The limits are set generously on purpose: aliens hit hard and a pilot has about half of it absorbed.
- **The mix.** Every level has ten regular missions and its Special: **3** with an item, **2** with a visit, **2** with a stay and **3** plain kill missions. A mission with a new step is a chain of two to five steps (kill specific aliens, fly to a point, hold a sector, take an item home) in order, or steps open together ("hold the gate for 4 minutes while you destroy 8 Seekers"). One set serves Mars, Terra and Galactic; only the officer's portrait differs.
- **Kills stay, with more variety.** Every mission that had a kill in 0.4.9 still has one. Level 3's kill steps add up to 108 kills (92 in 0.4.9, all Phantasm): 36 Seekers, 57 Phantasm and, from season day 4, the Seeker swarm (3 Boss Seekers and 12 Seeker Slaves). Level 4's kill steps add up to 134 (152 in 0.4.9, 150 of them Phantasm): 46 Seekers, 60 Phantasm, 13 Bulwarks and the swarm. The Specials of levels 3 and 4 hunt the Seeker swarm and open once the swarms appear on season day 4. Missions that ask for swarm members cannot be taken before that day.
- **Pace.** The chains are longer than the patrols they replace: by the balance model a level takes 1.1 to 1.5 times as long (levels 4 to 8 about 1.3 to 1.5 times). A level's experience is still 85 percent of its gap to the next level, so a level pays a little less an hour.
- **Redo, carry-over and notice:** see "If you already play". A mission that is not reworked is untouched; the 10 Station missions are untouched.
- **Pay:** Station missions and Challenge missions are now paid like level missions: the printed number is the **base**, and the world multiplier (Alpha 1, Beta 2, Gamma 3), your boosters and Premium experience and your clan's Credit and Thulium boosts multiply it. A Station mission has no world of its own and pays the world you fly in when you claim it. A claim is one write: a second claim is refused and nothing is paid twice.

**Missions: the Challenge line**
- **50 missions in five tiers of ten,** opening when your **pilot reaches level 3**: **Proving Ground** (tier I), **Iron Border** (II), **The Centre** (III), **The Abyss** (IV) and **Legends** (V, lifetime totals and a capstone, Warden of the Line, about 20 hours). Up to three Challenge missions are active at once, beside your level missions. Each can be done once. They survive the wipe and do not count for the Wipe Points of missions.
- **A tier opens when the missions of the tier before are claimed.** Tiers IV and V open when nine of the ten are claimed: the Dormant Force missions (Dormant Dawn, Dormant Dusk), sized for a crew of about eight, are not asked for. The Challenges tab of Mission Control shows the tiers, the next one locked, and what each mission asks.
- **What they ask:** kill grinds (1,000 to 10,000 Seekers or Phantasm, up to 2,000 Bulwarks, 1,000 Goombahs and 150 Crystalys), swarm hunts (from season day 4; the Pirate Boss and Dormant missions are group missions), stays (45 minutes in a company sector up to 3 hours in the Danger Sectors, where a ship that moves 300 units every 30 seconds counts, since nothing there can be shot), convoys (bring down the guards of a core and carry it home under a hull limit and no death), clean "Untouched" runs (a number of kills while losing no more than a limit of hull, up to 556,000 points), a tour of the four corners of a Danger Sector and a walk round the black hole's rim.
- **Kills count for your group:** the killer and the group mates within 4,000 units who fired in the last 15 seconds (the level missions keep their own rule).
- **The pay** is the base below, multiplied as above; the line is balanced at the lower end of its range, so it can be raised later.

  | Tier | Hours (model) | Credits | Thulium | Experience | Honor |
  |---|--:|--:|--:|--:|--:|
  | I Proving Ground | 22 | 9,355,000 | 70,125 | 435,500 | 26,140 |
  | II Iron Border | 46 | 6,200,000 | 46,450 | 471,000 | none |
  | III The Centre | 56 | 11,995,000 | 90,020 | 887,000 | none |
  | IV The Abyss | 74 | 26,215,000 | 196,615 | 1,880,500 | none |
  | V Legends | 176 | 48,390,000 | 362,865 | 3,110,000 | none |
  | All 50 | 374 | 102,155,000 | 766,075 | 6,784,000 | 26,140 |

  Honor is paid in tier I only (honor has no use yet). Items are resources that gate real builds (Power Cores, Cataclysite, plates, at most three Ancient Control Units a tier, no Dark Matter) and a booster on most missions. **What a multiplier does:** Crystalys Reign prints 7,725,000 credits and 57,925 Thulium. In Alpha you are paid that; in Gamma three times it (23,175,000 credits and 173,775 Thulium) before any booster; with the largest Thulium buff and your clan's full Thulium boost on top the most it can pay is 243,285 Thulium.

**Clans: the daily line, the Wardens and the boosts**
- **The line:** every clan has one line a day, four hunts or patrols in order and then the day's Clan Warden. The whole clan's kills and flying add to **one shared total**. Counts depend on the clan's tier, which the server takes from the five highest-level members: under mean level 4 Recruit, 4 to under 7 Veteran, 7 or more Elite (a Veteran clan asks for 300 Seekers on a Seeker Sweep day). A pilot **takes part from 5 percent of the day's work** (about 8 minutes of hunting) and at least **three** pilots must reach it before a step closes. The line resets every season day (24-hour blocks from the season's start), not at midnight UTC. The Operations tab in the Fleet window shows the steps, their progress, your own work against the minimum and how many members have reached it.
- **Pay:** a finished line pays the clan **100 clan points** (15, 15, 20 and 20 for the four steps and 30 for the Warden); each pilot who took part gets a personal reward (Recruit 5,000 credits and 20 Thulium, Veteran 15,000 and 60, Elite 22,000 and 90).
- **The Wardens:** the Brood Warden (day 1, then every third day) has four drones that heal it, so split your fire; the Siege Warden (day 2, 5, ...) keeps moving, mends itself and fires Rivet rockets at the pilot who hurt it, so keep moving and rotate the tank; the Wrath Warden (day 3, 6, ...) fights in place, mends itself and hits 1.5 times as hard below half hull, so get it under half hull fast. Each comes in three strengths (I, II, III) that follow the clan's tier. **The Leader or a Co-Leader summons it** from flight, in a company sector x-2, x-3 or x-4 outside the safe zones, once step 4 is done and at least 30 minutes of the day are left; two summons a day, one Warden out at a time. It appears 3,000 to 4,500 units from the caller, stands shielded for a 90-second warm-up and stays up for 40 minutes; **only pilots of the calling clan can hurt it.** A Warden has Alpha strength and Alpha pay in every world. By the model **5 pilots win in about 5 minutes and 3 pilots slowly (9 to 10 minutes, narrowly), best on x2 ammo**; those times are calculated, not measured. Its pay is that of 30 Phantasm (tier I: 90,000 credits, 360 Thulium, 9,000 XP, 180 honor), 24 Bulwarks (tier II: 120,000, 600, 19,200, 240) or 16 Goombahs (tier III: 240,000, 1,200, 48,000, 384), split by damage, plus a loot box. A Warden is worth PvE points like any alien (10, 15 or 25 by strength), is drawn in a fourth colour (the clan's) and is named with its clan in the kill feed.
- **Clan boosts:** the Leader and the Co-Leaders spend clan points on **Clan Damage** (10 levels of +0.5%, +5% in all), **Clan Thulium** (10 levels of +1%) and **Clan Credit** (10 levels of +1%). A level costs 22 points for the first and 58 for the tenth (400 for one boost, 1,200 for all three), so a clan that finishes every line has all 30 levels by season day 12 (the season has 29 days). A purchase is final and takes effect at once, even in flight, for every member. **Damage** applies to your lasers against aliens and pilots, not to rockets. **Thulium and Credit** apply to what kills and mission claims pay (your own share, a boss share and a group share), not to the Skylab's farms, rockets, bonus codes or the clan's own payouts. A boost that is under one whole unit on a kill is carried and paid when it adds up, so +10% on a Seeker's 4 Thulium is not rounded away.
- **Wipe:** clan points, boost levels and lines start again at every wipe; the clan, its roster and its bank stay.

**Company ranks**
- **24 ranks:** Junior Pilot, Pilot, Senior Pilot; the same three grades of Sergeant, Lieutenant, Captain, Major, Colonel, General and Admiral, up to Senior Admiral. The rank is a function of your **PvE points** (150 for Pilot, 700 for Junior Sergeant, 9,000 for Junior Captain, 23,000 for Junior Major, 150,000 for Junior General, 750,000 for Senior Admiral), so it follows what the points do, and **it keeps through the season wipe**, which keeps the points.
- **Where you see it:** only the symbol (chevrons, bars, stars, laurels) shows, before the name: on ship tags, in the Target window, in chat, in groups, in the kill feed, in the Hall of Fame and on pilot profiles. The words appear when you hover over it, and on the Company page.
- **The Company page** has a new **Company ranking**: the pilots of your company by PvE points, your own place, a bar to your next rank and the list of all 24 ranks with the points each needs. The ranking is per world. A promotion shows a toast with a quiet sound of its own; from Junior Major up your company sees it in the chat.

**Ships, slots and the starter kit**
- **The numbers:**

  | | Protos | Storm | Wraith |
  |---|--:|--:|--:|
  | Base speed | 160 (was 150) | 250 (was 240) | 220 (was 225) |
  | Hull | 8,000 | 150,000 (was 160,000) | 324,000 |
  | Lasers | 2 | 13 (was 10) | 12 |
  | Generator slots (core, support, auxiliary) | 4 (2, 2, 0) | 10 (4, 4, 2) (was 3, 4, 3) | 12 (4, 4, 4) |

  The **Storm** is still the fastest ship and now has the most lasers of any ship; with more than 10 lasers the wiki rates it a Class IV Dreadnought. The Dormant Force swarm flies at the Wraith's new 220. No ship's price, recipe or crafting time changed.
- Momentum Thrusters: speed multiplier I 1.08 -> 1.06, II 1.10 -> 1.07, III 1.13 -> 1.09, IV 1.14 -> 1.11.
- **Extra slots:** the four ships you **buy** (Protos, Kitefin, Ostirion, Nomad) have **2**, the four you **craft** (Paragon, Ironclad, Wraith, Storm) have **3**; the Extra Slots CPUs I, II and III add 3, 5 and 7 on top (5, 7 and 9 on the regular ships, 6, 8 and 10 on the craftable ones). Extras above the limit are unequipped into the inventory at the update, the highest box first, with their uses (nothing is deleted).
- **Starter kit:** a new pilot's Protos also gets a **Base CPU I** (10 uses; it takes your ship back to your company's base) and a **Repair Drone I** that slowly repairs your hull, both fitted in its two extra slots. The Emergency Repair drone in the ability slot, the Quantum Laser 1 and the starting ammo are unchanged. Pilots who enlisted before this update get no kit.

**Combat, fixes and loopholes**
- **Shields:** a ship's total shield capacity and recharge **never go down when you add a shield or a cell.** The game ranked a ship's shields by raw capacity alone and ignored which slot each sits in, so a cell in a support or auxiliary shield could lift it above a core shield and cost more than the cell gave: an Ostirion with six Heavy cores and 18 Capacity IV cells read 494,828 after the 17th cell and 483,120 after the 18th; it now reads 524,409. A shield's absorbance is still the average of the shields, so a new, weaker shield can lower it; a cell never does.
- **Speed:** adding a thruster or an engine can no longer lower a ship's speed, and the order your items are listed in no longer changes the number (the same kind of ordering mistake). A Kitefin with five engines read 227.50 and fell to 226.58 when a thruster was added; it now reads 231.55 with it.
- **Aliens no longer push each other apart.** Packs can overlap and several aliens attacking you can stand on the same spot; they still keep out of your ship's hull. The server does less work every tick, most on maps with many aliens.
- **Repair Drones fitted in an extra slot** show their drones: press REP, or let the Auto-Repair CPU do it, and small drones leave your ship, circle it and aim soft green beams at its hull while it repairs, then dock when it stops. Other pilots see them. They follow the Repair Drone's rank (I to IV: one, two, three, three drones), your graphics setting and Reduce Motion.
- **Two loopholes in fitting, closed.** (1) **An extra (a CPU, a Repair Drone) now has to sit in a box the ship really has:** the extras limit holds for any slot number a hand-made request names, and an extra fitted with no slot named, or with a slot number the ship does not have, goes into a free extra slot or is refused ("No free slot for this item on this ship."). (2) **A laser fitted with no slot named (-1) takes a free laser slot of the ship** and no longer keeps a drone-slot number into the other configuration, which let a pilot stack lasers beyond the laser limit. **Naming a drone's slot works exactly as before, for lasers and for shields:** a laser or a shield in a drone slot is as legitimate as it was (a Slave Drone has 1 slot, a Master Drone 2). The game's Hangar never sends -1, so no pilot who plays through the Hangar notices either change. **Pilots who used a loophole keep what they have:** lasers already stacked stay where they are, and nothing was reset or deleted for it; the one thing that moves is the regular ships' extras cut above, which sends any extras above a regular ship's new limit back to the inventory, those fitted through the loophole included.
- **Gear can no longer be hidden in a third loadout slot that survives the wipe.** A ship has two loadouts, 1 and 2; naming a laser, a shield or an extra into any other number is refused ("This ship has no such slot."), and gear a hand-made request had already parked in another loadout number no longer survives the season wipe.
- **Needs the new game:** missions with an item, a hull limit or "No death" and the Warden's summon are refused to a game from before 0.4.10 with an "Update the game" line (see Updating).

**Portals: the ring**
- **Three new links:** your company's border sector (x-4) has a second jump gate to another company's x-3: Mars' M-4 opens on Terra's T-3, Terra's T-4 on Galactic's G-3, Galactic's G-4 on Mars' M-3, and each of those x-3 maps has a gate back (6 gates). They are open to every pilot of any company, with the usual 3-second jump and a protected ring of 660 units round the gate. Where you can be attacked on the other side still depends on your world (in Alpha, x-3 is safe from pilots and x-4 is not). The Star System window and the wiki's chart are redrawn so the new routes are clear: the Danger Sectors in the middle, the three companies round them. The gates are added to existing worlds at the update.

**Sounds**
- **20 new quiet sounds** for your actions, each limited so it never stacks: seven for quest items and missions (finding, picking up, delivering and losing an item, reaching a spot, finishing a stay, breaking a run), ten for the clan line (a step done, the line done, a new line, the one-hour warning, a summon, a Warden armed, destroyed or lost, a boost bought, your reward), one when you change formation, one for a rank-up and one for a dodged hit. The sound bank in memory grows from 23.8 to about 27.5 MiB.

**The wiki**
- **Pictures:** every article has its own icon in the list, most open with a banner, and screenshots of the game's windows, ships, aliens, swarms, abilities and sectors sit in the pages they describe; the Black Hole article shows the black hole of Danger Sector 4 as the game draws it. Small icons stand in front of names in headings, lists and tables. Click a picture to see it large; Esc or a click outside closes it and the arrow keys flip through the page's pictures.
- **Search:** type in the box at the top of the article list (or press Ctrl+K, Cmd+K or / in the wiki) and the list turns into results across every article in your language, best match first, with the article's picture, its category and a snippet with your words highlighted. Use Up, Down and Enter, or click; the article opens at the first match with every match highlighted and a bar to step through them. Case and accents do not matter and several words find pages that have all of them.
- **New and changed pages:** the new articles Drone Formations and Ranks; Skylab, Resources, Research, Quests, Clans, Getting Started, Hangar, Drones, Rockets, Shields, Speed, Combat, Wipe Timeline, Extras, Spacemap Travel and the Storm page changed. All in the game's 12 languages.

**For administrators and the server**
- **New files under `Resources/`:** `Formations.json`, `Ranks.json`, `ClanLines.json`, `ClanWardens.json` and `QuestCarry.json`. Changed: `SkylabConfig.json` (per-level arrays and Solar's `powerWhileUpgradingShare`; the old formula keys are gone, so **deploy the image, never a 0.4.10 binary on 0.4.9 files or the other way round**), `Research.json` (the 16 formations, the ores' science), `quests.json` (148 definitions), `Rockets.json` and `AlienLeash.json` (their notes only), `Swarms.json` (the Dormant Force's speed), `Values/ranking-config.json` (the Wardens count as aliens for PvE points: 10, 15 or 25 by strength) and the seeds (the formation items and recipes, the ships' numbers; the 18 Warden alien kinds are added to the alien table from `ClanWardens.json`). **The server checks the new files at the start** and refuses to start on a wrong one ("Refusing to start: <file>: ..."), before it touches the database.
- **Four data steps at the first start** (each guarded by a `DataMigrations` row, logged once): `star-system-ring-v1` (the six ring gates), `skylab-tables-v1` (every pile paid once at the old rate; it stops the start with exit code 2 if it fails, leaving the database untouched), `quests-levels-mix-v1` (active missions carried, waiting claims frozen at the larger reward, completions of reworked missions cleared for the redo, the one-time notice) and `extras-limit-v1` (extras over the limit unequipped). **Five new tables:** `ClanSeason`, `ClanLineDays`, `ClanLineContrib`, `ClanPointLedger` (with an index) and `PilotRanks`. **No backup was taken for this release and these steps are one-way for the data** (docs/DEPLOY.md, "The deploy of 0.4.10: the checklist").
- **Client features:** the game announces what it understands (`X-Client-Features`); the server requires `quest-points` for a mission with an item, a hull limit or no-death and `clans` for the Warden's summon; `formations` is announced but not required.
- **Counters** for the first season (formation changes and time worn, clan lines and Wardens, quest starts, kills per hour) at `GET /api/admin/counters`. New admin tools for clans (`/api/admin/clans/:id/...`: the line, points, skip a step, reset a day, summon a Warden).
- **The release job:** `marketing/**` and `scripts/marketing/**` never make a release (since 0.3.4), so a marketing-only change set, the Reddit pack included, merges without one. The installed job is a copy and only changes when it is reinstalled; the copy in use already has the startup-repair gate (it is byte for byte the script of 0.4.9), so for 0.4.10 a reinstall (`scripts/release/install-auto-release.sh`) is optional and changes a comment only.

## 0.4.9 · 2026-10-04

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.9)

SpaceCorps 2027 0.4.9 adds the Research Centre to the Skylab: from Core level 10 you feed it resources and research technologies, and every craft in Assembly now needs its technology (you keep the technology of everything you already own). It brings seven new CPUs (Extra Slots I, II and III, the Jump CPU, Base CPU I and II and the Auto-Repair CPU), two new ships (the Nomad cruiser, sold in the Shop, and the Storm, a glass-cannon starfighter made in Assembly), a chat with rules (a System tab, a speed limit, Latin letters and no links), a black hole drawn by ray tracing that bends the sky behind it, 25 percent more credits from every alien, a Company page where you change company for 5,000 Thulium, new sounds, item trees and a Research page in the wiki, and a faster Assembly page. A few things get stricter or cost more, so the "If you already play" list below is worth reading.

### What's new

**Highlights**
- **The Research Centre** is a new Skylab module, built from Core level 10 (25 Ship Fragments, 25,000 credits, 500 Thulium). You feed it ten kinds of resource (the rarer, the more science), it turns them into science points, and it spends them researching technologies, one at a time, also while you are away. A new **Research** view next to Station, List and Table shows the tree, the tank and the Centre's controls.
- **Every craft in Assembly needs its technology.** There are **37 technologies**, one for each thing Assembly makes. **You keep the technology of everything you own, have queued or have booster time left of** (see below); what you do not have yet you research: from 30 minutes (Impulse Thruster II) to 2 days (the Wraith). The whole tree takes 15.9 days one after another.
- **A Thulium boost** (5,000 Thulium) doubles the speed of a running research for 24 hours and burns the fuel twice as fast, so the same fuel in half the time. Boosts stack up to 72 hours. **The 15 highest technologies also need 10 Dark Matter** plugged into the Centre (150 in all).
- **Seven new CPUs**, researched and then **crafted in Assembly** (they are not sold): **Extra Slots CPU I, II and III** give every ship +3, +5 or +7 extra slots (6, 8 or 10 in all), the **Jump CPU** jumps you to any company sector for 500 Thulium, **Base CPU I and II** teleport you to your company's base (10 and 25 uses), and the **Auto-Repair CPU** launches your Repair Drone by itself.
- **Two new ships.** The **Nomad** (Class II Cruiser, Shop, 1,275,000 credits and 500 Thulium): 96,000 hull, 6 lasers, twice an Ostirion's hull and guns. The **Storm** (Class III Starfighter, made in Assembly for 15,000 Thulium): the fastest ship (base speed 240) with 10 lasers and a light hull of 160,000. Both are new models; their previews need the new client.
- **Chat with rules.** A **System** tab holds the server's own lines, Enter keeps you typing, and a speed limit, a 200-character cut, Latin letters only and no links keep the channels readable. Chat takes the Latin alphabet with accents, so Cyrillic, Chinese, Japanese, Korean and emoji are no longer allowed.
- **Sounds for your actions:** 16 new interface sounds (collecting in the Skylab, building and upgrading, switching views, every step of the Forge, sending a chat line, feeding the Research Centre, starting and finishing a research) and 3 new in-world sounds (a warp CPU charging and being called off, the Auto-Repair CPU launching the drone).
- **The black hole bends light.** From Medium graphics up it is drawn by ray tracing: a black shadow with a thin photon ring, the far side of the glowing disk arched over the top and under the hole as in Interstellar, the sky behind it pulled around it, and ships that pass in front of it drawn in front. Low keeps the old picture.
- **Every alien pays 25 percent more credits** (Seeker 1,000, Phantasm 3,000, Bulwark 5,000, Goombah 15,000, Crystalys 75,000), and so do the swarm members (the Dormant Pulse a little more: 95,000 for 75,000). Thulium, experience and honor are as before.
- **Company page** (Economy > Company): change company for **5,000 Thulium** (it used to be 5,000 credits, with no screen to do it) and **half of your honor**. Not while your ship is in flight.
- **Assembly and the Shop are smooth again** for pilots with a big inventory: a frame of the Assembly page took about 60 milliseconds with 600 items and takes about 1 now.
- **The wiki draws item trees** on the Lasers, Rockets, Shields, Propulsion, Extras, Drones and Boosters pages and on a new Item Trees page, has a new **Research** page and articles for the **Nomad** and the **Storm**, and explains the chat rules, the Company page and the CPUs, in 12 languages.
- **Fixes:** swarm followers no longer fly off the edge of the map, a boss's damage record no longer stops counting new pilots after 256, and the recipes' material lines no longer change their order after every server restart.

**If you already play: what changes for you**
- **Crafting needs research, but you keep what you own.** At the first start of 0.4.9 every pilot is given the technology of everything it holds: items equipped, fitted into another item, loose or in the Transport Cache, rocket stacks you still have, your ships, the boosters you have time left of (Damage Amp II, Hull Plating II, Shield Wall II), and the crafts waiting in your Production Queue. You also get the technologies those needed (holding an Impulse Thruster III gives you the II). **Items that reach you later** (a gift, a bonus code, a quest reward) **do not unlock their technology**, and **a veteran who made a Wraith last season and holds none now has no claim to it**: you research it.
- **What you lose is the next step, not what you have.** To craft the next tier of anything you do not have a technology for, you research it first. **A pilot below Core 10 cannot research**, so it crafts nothing new until it has Core 10, the Research Centre and a research: the Core climb from level 1 to 10 takes about 3 hours of timers and 112,326 credits, then the Centre's 25,000 credits, 500 Thulium and 25 Ship Fragments; the Centre starts with one free hour of research in its tank.
- **Research, the tank, the plugged Dark Matter and the boost are kept across the season wipe.**
- **Extra Slots CPUs are crafted in order:** CPU II only when CPU I is installed, CPU III only when CPU II is installed (12,000 + 30,000 + 75,000 = 117,000 Thulium for the 10 slots). They install in your Skylab when you collect them; there is no item to fit and they take none of the slots they add. A level replaces the one before (CPU II is +5 in all, not +3 and +5).
- **Aliens pay 25 percent more credits,** and rocket prices did not change, so rockets are about 20 percent cheaper against the pay. Quest rewards are as before.
- **Changing company costs Thulium now (5,000, not credits) and halves your honor** (rounded down; honor at 0 or below stays as it is). Your first enlistment in Setup is still free and keeps all your honor.
- **The chat takes fewer characters and no links.** Messages in Cyrillic, Chinese, Japanese or Korean are refused, so are emoji and symbols outside the Latin alphabet, and you can no longer post a link, an invite included (admins can).
- **Solar makes 95 to 100 more power from level 10 to level 20** so it still covers a full station with the Research Centre. Levels 1 to 9 are unchanged.
- **The ship pictures in Assembly (the Paragon, Wraith and Ironclad recipes and any ship in your queue) stand still until you point at their card.**
- **A 0.4.8 client keeps working** against the 0.4.9 server, but it does not have the Jump and Base CPUs, the Company page, the Research view or the new chat (see Updating).

**Research: the Research Centre**
- **Build:** Skylab, Core level 10 or higher, once: 25 Ship Fragments from your inventory (the ship parked), 25,000 credits and 500 Thulium. It has **10 levels** (each upgrade costs 1.5 times more). A level makes the **tank** bigger by a quarter, from 12 hours of research at level 1 (43,200 science) to 89 hours at level 10 (321,865 science), and the Centre draws more power (25 at level 1, 88 at level 10); **no level makes a research faster.** The page says what building needs before you press Build.
- **Fuel:** ten resources turn into science points at once, and the rarer the resource, the more it gives:

  | Resource | Science points | Goes in from |
  |---|--:|---|
  | Ship Fragment | 5 | your inventory (ship parked) |
  | Cataclysite | 5 | your inventory (ship parked) |
  | Daraxium | 7 | your inventory (ship parked) |
  | Nyxite | 7 | your inventory (ship parked) |
  | Quorvium | 8 | your inventory (ship parked) |
  | Reinforced Hull Plate | 33 | your inventory (ship parked) |
  | Velkonite | 40 | the Resource storage |
  | Orvium | 80 | the Resource storage |
  | Power Core | 100 | your inventory (ship parked) |
  | Ancient Control Unit | 650 | your inventory (ship parked) |

  Ship Fragments and the other inventory resources go in while your ship is parked; Velkonite and Orvium come out of the Resource storage. The Velkonite and Orvium Reinforced Plates cannot be burnt (they are made of the ore, which can). The Max button puts in as much as fits, and a feed that does not all fit takes what fits.
- **Burn:** a research burns **1 science point for every second of its base time**: a day-long research burns 86,400 points. With no fuel in the tank a research pauses, and fuel put in resumes it.
- **One research at a time,** also while you are away: it keeps going until it ends or the tank runs dry. It also keeps going through a blackout or an upgrade of the Centre; only starting a new one is refused when the station is short of power. Cancelling loses the progress and the fuel already burnt; the Dark Matter goes back to the Centre's socket.
- **The Research view:** the technology tree drawn by family (Propulsion, Shields, Lasers, Boosters, Drones, Ships, Rockets, CPUs, Resources) with the research time of every technology, what each one needs and a Dark Matter badge on the 15 top ones; and the Centre's panel with the tank, the running research and when it ends, the feed rows (+1, +10, Max), the boost and the Dark Matter socket. Cancel asks twice. A toast tells you when a research is finished (with an Open Assembly button in the station) or when the tank has run dry.
- **Boost:** 5,000 Thulium buys 24 hours of double speed for the research that is running, per Centre. It never brings fuel (the same fuel is burnt in half the time). You can buy another while 48 hours or less of boost are left, so they stack up to 72 hours.
- **Dark Matter:** 15 technologies, the Epic or better ones that take 10 hours or more, need **10 Dark Matter** each, plugged into the Centre before the research starts. They are used up when it starts and given back if you cancel. Impulse IV, Momentum IV, Absorption IV, Capacity IV, Starfire-3, Helios Beam, Nova Amp, Apex Amp, the Ironclad, the Storm, the Wraith, the Dark Matter Plate, the N.U.K.E., Extra Slots CPU III and the Jump CPU need it; the N.I.K.E. (which is how Dark Matter is made) does not.
- **Where to see it:** the Research Centre is the ninth card in the Skylab's list and table, and the Station view has no 3D model of it yet.

**Research: the technologies**
- **37 technologies** for the 37 things Assembly makes: the thrusters, the shield cells and the shield core, the engine, the lasers and amps, the three boosters, the Master Drone, the Paragon, Ironclad, Storm and Wraith, the Dark Matter Plate, the N.I.K.E. and N.U.K.E. rockets and the seven CPUs. The Shop is not gated, nor are the Forge, plates made in the Skylab's Forgery, or the rewards of quests and codes.
- **Research times (base rate):**

  | Research time | Technologies |
  |---|---|
  | 30 min (5) | Impulse Thruster II, Momentum Thruster II, Absorption Shield Cell II, Capacity Shield Cell II, Extra Slots CPU I |
  | 3 h (12) | Impulse Thruster III, Momentum Thruster III, Engine III, Absorption Shield Cell III, Capacity Shield Cell III, Heavy Shield Core, Quantum Laser 3, Damage Amp II, Shield Wall II, Hull Plating II, N.I.K.E., Base CPU I |
  | 6 h (2) | Paragon, Auto-Repair CPU |
  | 10 h (9) | Impulse Thruster IV *, Momentum Thruster IV *, Absorption Shield Cell IV *, Capacity Shield Cell IV *, Nova Amp *, Apex Amp *, Master Drone, Extra Slots CPU II, Base CPU II |
  | 1 day (8) | Starfire-3 *, Helios Beam *, Ironclad *, Storm *, Dark Matter Plate *, N.U.K.E. *, Extra Slots CPU III *, Jump CPU * |
  | 2 days (1) | Wraith * |
  | | \* needs 10 Dark Matter plugged into the Centre |

- **Chains:** each family's tiers follow each other (Impulse II, III, IV; Momentum II, III, IV; Absorption II, III, IV; Capacity II, III, IV; Quantum Laser 3, Starfire-3, Helios Beam; Extra Slots CPU I, II, III; Base CPU I, II, then the Jump CPU). Everything else can be researched on its own. All 37 together take 15.9 days (7.9 days with the boost always on) and 1,369,800 science points; the 28 technologies that are not rockets or CPUs take 11.5 days.
- **The wiki** has the same tree, the fuel table and the numbers on a new Research page, and every ship's article says what its technology needs.

**CPUs: seven new ones, crafted in Assembly**
- **They are researched first, then crafted for Thulium and materials, and only crafted** (no Shop, no free gift from the research). The cost of all seven is 200,000 Thulium:

  | CPU | Research | Needs first | Thulium | Materials | Crafting time |
  |---|--:|---|--:|---|--:|
  | Extra Slots CPU I | 30 min | nothing | 12,000 | 60 Ship Fragments, 3 Power Cores, 6 Velkonite Reinforced Plates | 5 min |
  | Extra Slots CPU II | 10 h | Extra Slots CPU I | 30,000 | 120 Ship Fragments, 10 Reinforced Hull Plates, 6 Power Cores, 12 Velkonite Reinforced Plates, 2 Orvium Reinforced Plates | 10 min |
  | Extra Slots CPU III | 1 day + 10 Dark Matter | Extra Slots CPU II | 75,000 | 240 Ship Fragments, 25 Reinforced Hull Plates, 12 Power Cores, 2 Ancient Control Units, 20 Velkonite Reinforced Plates, 6 Orvium Reinforced Plates | 15 min |
  | Jump CPU | 1 day + 10 Dark Matter | Base CPU II | 40,000 | 200 Ship Fragments, 20 Reinforced Hull Plates, 10 Power Cores, 3 Ancient Control Units, 15 Velkonite Reinforced Plates, 10 Orvium Reinforced Plates | 15 min |
  | Base CPU I | 3 h | nothing | 8,000 | 40 Ship Fragments, 2 Power Cores, 4 Velkonite Reinforced Plates | 5 min |
  | Base CPU II | 10 h | Base CPU I | 20,000 | 100 Ship Fragments, 5 Power Cores, 8 Velkonite Reinforced Plates, 2 Orvium Reinforced Plates | 10 min |
  | Auto-Repair CPU | 6 h | nothing | 15,000 | 80 Ship Fragments, 8 Reinforced Hull Plates, 4 Power Cores, 6 Velkonite Reinforced Plates | 10 min |

- **Extra Slots CPU I, II and III:** +3, +5 and +7 extra slots on every ship in both configurations, 6, 8 and 10 in all. The Hangar and the Pilot page count them. A CPU that would add nothing (that level or a better one is installed or in your Production Queue) is refused, and so is one out of order ("Install Extra Slots CPU I first.").
- **Jump CPU:** opens the Star System chart; click a company sector of your world (M, T, G, 1 to 4: all twelve, the other companies' home sectors too) and confirm. **500 Thulium a jump, no limit of uses,** a 5 second charge, 30 seconds before the next jump. The Danger Sectors can't be reached, a neutral sector can't be jumped from or to, and you can leave a Danger Sector. The 500 Thulium are taken when the charge ends and given back if the move fails.
- **Base CPU I and II:** teleport you to your company's base (inside the station's ring on your home map) after a 10 second charge, for free. Base CPU I has **10 uses and recharges in 10 minutes;** Base CPU II **25 uses and 5 minutes.** A used-up Base CPU is gone and you craft another (about 800 Thulium of crafting a use for both). When two are fitted, the better one is used first.
- **A warp CPU is out of combat:** it can't start within **10 seconds of a shot you fired or a hit you took,** and a shot or a hit while it charges cancels it, as does pressing the slot again or cloaking. A warp that charges shows a bar over the hotbar and a glow on your ship that other pilots see.
- **Auto-Repair CPU:** launches the Repair Drone fitted in the same configuration **by itself** whenever you could launch it by hand (the hull is damaged, the drone is not out and its 10 seconds after a hit have passed). It does nothing without a Repair Drone and takes one extra slot. If you stop the drone by hand it waits until your hull is full or you start the drone yourself; the slot shows AUTO, or Paused.
- **On the hotbar:** the Jump CPU is JMP, Base CPUs BSE, the Auto-Repair CPU ARP. The slots show the charge, the recharge and the uses left, and keep counting through a death, a jump and a log-out. A restart of the server clears the recharges.
- **Help cards** for the Jump, Base and Auto-Repair CPUs are new, and the Extras card lists what the Extra Slots CPUs add, in all 12 languages.

**Ships: the Nomad and the Storm**
- **The numbers:**

  | | Ostirion | Nomad | Paragon | Storm | Ironclad | Wraith |
  |---|--:|--:|--:|--:|--:|--:|
  | Hull | 48,000 | 96,000 | 128,000 | 160,000 | 600,000 | 324,000 |
  | Base speed | 200 | 200 | 210 | 240 | 92 | 225 |
  | Lasers | 3 | 6 | 8 | 10 | 6 | 12 |
  | Generator slots (core, support, auxiliary) | 6 (3, 3, 0) | 7 (3, 3, 1) | 8 (3, 3, 2) | 10 (3, 4, 3) | 14 (7, 4, 3) | 12 (4, 4, 4) |
  | Ability slots | 2 | 2 | 3 | 3 | 3 | 3 |
  | Extra slots (before the Extra Slots CPUs) | 3 | 3 | 3 | 3 | 3 | 3 |
  | How to get it | Shop: 425,000 credits | Shop: 1,275,000 credits and 500 Thulium | Assembly: 1,500 Thulium | Assembly: 15,000 Thulium | Assembly: 10,500 Thulium | Assembly: 20,000 Thulium |
  | PvP points for a kill | 20 | 30 | 40 | 80 | 160 | 640 |

- **The Nomad** is a Class II Cruiser: twice the hull and guns of an Ostirion, between it and the Paragon. It is open to everybody in the Shop. It is a sand-coloured hammerhead cruiser with dusk-indigo plates, violet running lights, six guns along its front edge and two big engine pods. A kill of a Nomad is worth 30 PvP points.
- **The Storm** is a Class III Starfighter and the glass cannon of the fleet: the highest base speed of any ship, ten lasers and 160,000 hull, the lightest of the Storm, Ironclad and Wraith. It is made in Assembly after you have researched it (1 day and 10 Dark Matter): 1 Ancient Control Unit, 200 Ship Fragments, 35 Reinforced Hull Plates, 10 Power Cores and 15,000 Thulium, in 15 minutes. Its look follows a concept drawing: a needle-nosed fighter between two open crescent-ring wings with a glowing engine in each ring, two long forward cannons and eight smaller gun emitters, in bone, teal and orange. A kill of a Storm is worth 80 PvP points.
- **What the balance model says** (the model, not play): the Storm is the fastest ship in the stock build (it flies 255.5 where a stock Wraith flies 238.0), and the Wraith keeps the fastest best build. One to one, a Storm beats a Paragon, and an Ironclad and a Wraith beat a Storm. A Nomad beats an Ostirion, and a Paragon beats a Nomad.
- **The wiki rates a ship by its lasers:** more than 10 a Class IV Dreadnought, 9 or 10 a Class III Starfighter, 5 to 8 a Class II Cruiser, up to 4 a Class I Scout. The Black Hole page lists both ships, and its help card now puts the point of no return at about 1,000 units for the fastest ship (it said 1,200). The help cards for hull, speed, lasers, slots and PvP points list both.
- **With a 0.4.8 client** the Nomad and the Storm are drawn as a Protos in flight and show a "Model not found" tile in the Shop and the Hangar; their stats, prices and recipe are right.

**Chat: a System tab, typing, and rules**
- **A System tab,** last in the row, holds what the server says on its own and what your ship reports: the abilities' answers, repairs, the black hole's warnings, rocket hits, the swarms', the restart's and the wipe's announcements. Global, Local and Group show pilots only (the kill feed stays in Global, with its switch). The tab counts the announcements you have not read (the black hole's warnings are System lines too, but are not counted). Restart and update warnings (each minute mark) and the wipe alert, start, end and failure also pop up as a message on screen.
- **Typing goes on after Enter:** press Enter, type, press Enter, and your line is sent and you keep typing. Esc, Enter on an empty box, a left click on the map (which still steers your ship), 15 seconds with an empty box and no key pressed, your ship being destroyed, or closing the window ends it.
- **A counter** shows from 120 characters (200 is the most; amber at 180, red at 200), and a line is cut at 200 on the server too. Letters the chat does not take are dropped as you type, with a hint.
- **Speed limit:** you can send **5 lines in a row, then one more every 2 seconds, in Local, Global and Group together.** Run out and send again and the chat **pauses for 10 seconds, then 30 seconds, 2 minutes and 5 minutes** if you keep running into it (the pause is forgotten after 10 minutes without a new one). The input says "Chat paused: N s" and counts down, and your text stays in the box.
- **A message is refused,** with the reason under the input and the line back in the box, when it has **characters chat does not allow** (letters of the Latin alphabet with accents, digits and punctuation are allowed, so French, German, Spanish, Italian, Portuguese, Swedish, Hungarian and the other Latin-script languages work), **a link** (in any spelling: "example [dot] com", spaced-out letters, Discord invites; you can still talk about Discord), **one character over and over** (more than 8 in a row), **no letter or digit at all** (a lone "?" or ":)"), or when it **repeats your last message within 10 seconds.** A refused message is sent to nobody and uses up 2 of your 5 lines. Admins are exempt from these rules (not from the 200 cut).
- **Chat no longer takes the minimap's dots for links** ("a red dot to the north" goes through), nor a point in Portuguese, Italian, German or Hungarian.
- **If the server pauses you,** your text and your keyboard stay in the box (Esc or a click on the map lets go). Text pasted with no-break spaces or an ellipsis keeps its words.
- **Sending a line plays a short soft blip** (see Sounds).

**Sounds**
- **Skylab answers your actions with sound:** collecting from a farm, collector or the Forgery plays a soft pour and three plucks, **Collect All** one rising cascade however many modules it takes from, confirming a Build or an Upgrade a short power-up that ends on a muted bell. A refused request plays the error sound.
- **Switching views has a soft swipe:** Skylab's Station, List and Table, picking or letting go of a module in the station, and Assembly's Crafting and Forge tabs.
- **Every action in Assembly > Forge has a sound of its own:** taking an item into a tier-up or merge slot is a small bright tap, letting it go is the same tap lower; a tier-up starts with a strike on the anvil and rising heat, a tier-up that held rings the anvil with three climbing bells, a failed roll is a dull dud (three coin tinks follow if materials or Thulium came back); a merge starts with two sweeps that converge and ends with two bells gliding into one tone.
- **The Research Centre** has its own: a soft pour when you feed the tank or plug Dark Matter in, a lab humming up when a research starts, and a two-note chime when one finishes. **The CPUs:** a rising hum while a Jump or Base CPU charges (it fades out if you call it off or a hit breaks it), a short soft drop when a charge is called off, and two soft pips when the Auto-Repair CPU sends out the drone (about every 10 seconds at most).
- **All of these are quiet** (at least 2 dB under the purchase chime), limited so they never stack. The 16 interface sounds follow the **Interface** volume; the 3 in-world ones (the CPU charge and cancel and the Auto-Repair pips) follow **Sound Effects.** The view, pick and chat sounds also follow Settings > Audio > Button Sounds; the answers to actions play whatever that says.

**The black hole**
- **From Medium graphics up** the black hole is traced ray by ray: the shadow (the kill radius, 300 units) is black and sharp with a thin bright photon ring around it; from a low camera the far side of the disk arches over the top of the hole and under it, as in Interstellar; from above a thin ring surrounds the shadow and the disk swirls around it.
- **The sky behind it bends:** the stars, the nebula, planets and asteroids near it are pulled and stretched around it, and the lines on the map bow round it (moderately). Ships and drones that pass between you and the hole are drawn in front of it instead of vanishing into black. The HUD, name tags and the minimap are not bent.
- **Low graphics keeps the old picture,** and so does a card whose graphics system cannot build the new shader. On the machine we measured (an M4 Max) the lens costs about 0.1 to 0.4 millisecond a frame while the hole covers up to a quarter of the screen, and under 1 millisecond when it fills the screen.
- **From a low camera inside the disk's radius** the near side of the disk is a heavy orange veil over the lower half of the screen, and moons and asteroids behind the hole's plane look washed out. It follows from the physically correct picture; see Known limits.

**Aliens pay 25 percent more credits**
- **Credits only:** Thulium, experience, honor and quest rewards are unchanged; boosters and the Beta (x2) and Gamma (x3) world multipliers stack as before. A 0.4.8 client sees the new pay at once.

  | Alien | Credits before | Credits now |
  |---|--:|--:|
  | Seeker | 800 | 1,000 |
  | Phantasm | 2,400 | 3,000 |
  | Bulwark | 4,000 | 5,000 |
  | Goombah | 12,000 | 15,000 |
  | Crystalys | 60,000 | 75,000 |
  | Seeker Slave (swarm) | 100 | 125 |
  | Boss Seeker (swarm) | 8,000 | 10,000 |
  | Pirate Scout (swarm) | 800 | 1,000 |
  | Pirate Boss (swarm) | 116,000 | 145,000 |
  | Dormant Pulse (swarm) | 75,000 | 95,000 (a round figure, 26.7 percent more) |
  | Dormant Force (swarm) | 160,000 | 200,000 |

- **Rocket prices did not change,** so against the pay a rocket costs about 20 percent less than before. At the best roll the cheapest rocket-only kill (a Rivet II on a Phantasm) costs 14.8 percent of the kill's pay (credits and Thulium counted at 200 credits each; it was 16.7), killing a Crystalys with Rivet III alone 48.7 percent (it was 56.0), and a Scatter III clearing five Phantasms in a pile 4.8 percent (it was 5.4). **The rockets model's three floors that guarded these moved** from 15 percent, half and 5 percent to 14 percent, 48 percent and 4.5 percent; no rocket price changed.

**Company page**
- **Economy > Company** (right after Season & Profile) shows your company and lets you change it. A change costs **5,000 Thulium and halves your honor** (12,400 honor becomes 6,200; honor at 0 or below stays as it is), repairs your ship in full and moves you to the new company's home sector. You keep your clan, group, ships, items and Skylab.
- **A confirmation** shows the price and your Thulium and honor before and after; if you are short of Thulium the buttons are off and say how much is missing. A refusal from the server is shown in your language. The Honor help card says that changing company halves honor.
- **Not while your ship is in flight,** also when you are flying on another device: dock first. Nothing is charged or changed when it is refused. (If you launch at the very moment a change is being written, you are told to try again in a moment.)
- **The page only offers the change on a server running 0.4.9 or newer;** on an older server it is read-only.

**Skylab: Solar and the Station hint**
- **Solar makes 95 to 100 more power from level 10 to 20** (1,680 at level 10, 16,110 at level 20; levels 1 to 9 are unchanged) so a full station with the Research Centre still has a tenth to spare. A station that was short of power under the old table and is not under the new one has its producers resumed at the first start.
- **The Power help card** says the Research Centre uses power too, and **the Station's hint** names the number keys of the modules your server lists (1-9 with the Research Centre).
- **Toasts with a button last 6 seconds** and keep clear of the Skylab's view switch.

**Assembly and Shop speed**
- **The Assembly page takes about 1 millisecond a frame whatever you carry** (it took about 60 with 600 items, 30 with 300, 11 with 100); the whole frame went from 63 to 3 milliseconds with 600 items. The Shop page went from 9.4 to 0.2 milliseconds with 600 items. Measured on a Mac.
- **The ship pictures in Assembly stand still until you point at their card,** then they turn (the Paragon, Wraith and Ironclad recipes and any ship in your production queue). Each of them was drawn with its own camera and a 4x anti-aliased pass every frame.
- **Assembly refreshes your inventory every 30 seconds** instead of every 5. It still refreshes at once when you open the page and after anything you do (assemble, collect, forge, buy).
- **A price in the millions on a Shop card keeps its thousands:** the Nomad's 1,275,000 reads 1.275M, not 1.3M.

**The wiki**
- **Item trees:** the Lasers, Rockets, Shields, Propulsion, Extras, Drones and Boosters pages open with a tree of their items, and the new **Item Trees** page shows all of them with the ships and the materials. A box shows the item's picture and name; a solid arrow means the item is made from the one before it (Assembly uses it up), a dashed arrow the next tier, got on its own; a wrench marks what Assembly makes, a storefront what the Shop sells. Hover to see the Shop price or what Assembly takes (Thulium, credits, time, how many it makes, materials); click to open the page. The trees come from the game's own item and recipe data and scroll sideways in a narrow window.
- **Research page:** the Research Centre, how research runs, what each resource gives as fuel, the boost, the Dark Matter rule, the technology trees with the research time of every technology (and in the item trees, a technology's time and Dark Matter), a table of all 37 technologies and the seven CPUs. The numbers are read from the game's data.
- **New articles:** the Nomad and the Storm. Every ship's article has a Research card (the technology, its time and Dark Matter, and what the Extra Slots CPUs add).
- **Pages that changed:** Groups (the System tab, typing, the chat rules), Getting Started (where to change company, honor, what Thulium is for), Extras (the Jump, Base and Auto-Repair CPUs in full), Skylab (nine modules, four views, what the wipe keeps), Combat, Spacemap Travel, Quests, Inventory, Abilities, Boosters (Damage Amp II, Shield Wall II and Hull Plating II are made in Assembly after research), Rockets ("about a seventh to three quarters" of what a kill pays), Black Hole, Wipe Timeline, Forge, Drones, the Items overview, the swarm pages (the announcements are System lines) and Resources.
- **All of it in the game's 12 languages.**

**Fixes**
- **Swarm followers** (Pirate Scouts, Seeker Slaves, Dormant Pulses) no longer fly off the edge of the map when their leader roams near it; they keep to their place beside the leader, on the map.
- **A boss's damage record** no longer stops counting new pilots once 256 different pilots have hit it: the pilots who deal the most are always counted for the pay split and the box.
- **The recipe cards' material lines** no longer reshuffle after every server restart; they stay in the order of the item names.
- **The chat's lines under the input** wrap and show in full in every language; the Honor card fits.

**For administrators and the server**
- **New config files:** `Resources/Research.json` (the technologies, fuels, boost and tank; the server does not start without it), `Resources/CpuConfig.json` (the Jump, Base and Auto-Repair CPUs' numbers) and `Resources/Chat.json` (the alphabet, the 200 cut, the rate gate, the pauses). `Resources/Groups.json` lost `globalBurst` and `globalIntervalMs` (the gate is Chat.json's `burst` and `refillMs`, for all three channels). `SkylabConfig.json` has the `ResearchCentre` module and Solar's new table. Changed: `Rockets.json` (hit radius of the Nomad 48 and the Storm 54), `Swarms.json` (+25 percent credits), `ranking-config.json` (PvP weights of the Nomad 30 and the Storm 80), the alien, item and recipe seeds.
- **`CHAT_RULES_ENABLED=false`** turns the chat rules and the rate gate off (the chat of 0.4.8: the 200 cut and Global's old limit); unset means on.
- **Research tools for admins:** the Admin page grants or revokes a pilot's technology (with or without its prerequisites) and sets the Dark Matter plugged into its Centre (`GET /api/admin/players/:id/research`, `POST .../research/grant`, `POST .../research/revoke`, `PUT .../research/dark-matter`); they are recorded as `research-grant`, `research-revoke` and `research-dark-matter` (a 0.4.8 admin page lists them as "other"). Player routes: `GET /api/research/tree` (public), `GET /api/research`, and `POST /api/skylab/research/start/:tech`, `cancel`, `feed`, `plug`, `unplug` and `boost`.
- **The server at its first start** adds three tables (`PlayerTechnologies`, `ResearchStates`, `PlayerInstalls`, all kept by the season wipe), runs two data steps (`research-v1`, the technologies of what pilots own; `skylab-solar-v3`, which resumes the producers the old Solar table left dark, if any), appends 9 item definitions and 8 recipes, and changes the 11 aliens' credits. **Take a volume backup first** (`docs/DEPLOY.md`, "The deploy of 0.4.9: the checklist").

## 0.4.8 · 2026-10-03

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.8)

SpaceCorps 2027 0.4.8 puts three swarms of alien bosses on the map. It also splits the six shield cells and the six thrusters into two families of four tiers each, names the twelve rockets by family and tier (Lancet I, II and III) and rolls their damage when they are fired, counts the eighth shield at 50 percent, gives a respawned ship 3 safe seconds and a hull of at most 10,000, and pays a PvE kill by how tough the alien is. Your cells and thrusters are converted in place and some of them are worth less, so the "If you already play" list below is worth reading.

### What's new

**Highlights**
- **The Seeker Swarm:** from season day 4 a **Boss Seeker** (four times a Seeker) with up to four healing **Seeker Slaves** roams the first two sectors of every company. It pays ten Seekers, split by damage, and drops a cargo box.
- **The Pirate Swarm** (a Pirate Boss with up to five healing scouts that fires rockets at the pilot who shot it) and **the Dormant Swarm** (a Force and two Pulses that fly between the Danger Sectors through the real gates) are the hardest aliens in the game: the Pirate Boss, the Force and each Pulse pay more than a Crystalys in credits, Thulium, experience and honor.
- **All three swarms start on season day 4** (First Contact) and last until the wipe; a server that restarts after day 4 puts every boss on its map at once. A **Swarms** category under the Aliens in the in-game wiki, in 12 languages, tells how each one fights and what it pays. **Until you update the game, a 0.4.7 client draws every swarm ship as a small plain green alien** (see Updating).
- **Shield cells in two families:** **Capacity** (more shield and recharge) and **Absorption** (more absorbance), tiers I to IV: tier I from the Shop for 30,000 credits, II to IV made in Assembly.
- **Thrusters in two families:** **Impulse** (the most flat speed and a small multiplier) and **Momentum** (less flat speed and a bigger multiplier), tiers I to IV: tier I for 20,000 credits. **A thruster's multiplier now acts on the whole engine.**
- **Your old cells and thrusters are converted in place,** and some are worth less (see below).
- **The eighth shield and every one after counts 50 percent** (it was 25), and the Hangar shows what each slot counts for.
- **Rockets are named by family and tier** (Lancet I, II, III) and **their damage is rolled** when fired: 80 to 100 percent of its number (90 to 100 for the N.U.K.E. and N.I.K.E.).
- **The Forge:** the first buff is sure, each further buff slot of a tier-up fills with a 50 percent chance, and an Assembly upgrade keeps the number of buffs.
- **Respawn:** no welcome line, 3 seconds in which you cannot be hurt and cannot attack, and a hull of at most 10,000 with an empty shield.
- **PvE points by toughness:** Seeker 1, Phantasm 2, Bulwark 4, Goombah 7, Crystalys 16.
- **The Group window shows what a mate shoots.** **Station missions** 6, 7 and 9 ask for Solar levels, **Solar keeps making power while it upgrades,** and **DS-1 has no Mission Control.**
- **Menus:** no status bar, credits and Thulium at the top right, descriptions on hover in Assembly, a new **Interface** tab in Settings, selectable wiki text and a **Copy page** button, and no kill-log capsules at the top of the screen.
- **Windows memory:** the game's memory no longer grows with every Materializer spin on the Galaxy Gates page, and the log file gets a memory line a minute.

**If you already play: what changes for you**
- **Your shield cells and thrusters are converted in place** to the nearest new item: Basic and Advanced cells become Absorption I, Reinforced II, Elite and Prime III, Sovereign IV; Thruster I becomes Impulse I, Vector and Thruster II become II, Ion and Thruster III become III, Plasma becomes IV. Each piece keeps its row, its place, its Forge tier and its buffs, and takes the new tier's numbers (the tables are under "Ships and items: what your old cells and thrusters become"). **Big ships with a full set of cells have 11 to 16 percent less to take, and the owners of a Plasma Thruster fly slower.**
- **The cells in detail.** A Basic cell gains in everything; an Elite gains a point of absorbance and loses a quarter of its capacity and recharge; an Advanced, a Reinforced, a Prime and a Sovereign keep their absorbance and lose 29 to 50 percent of their capacity and recharge. Nobody is given a Capacity cell: the family starts empty for everyone.
- **Who has less shield, and why.** The Sovereign was both the Capacity IV's capacity and the Absorption IV's absorbance, and no new cell is both. A ship with a full set (three cells in every Heavy Shield Core) has less shield after the update. What the ship takes before its hull is gone changes only where the shield, not the hull, was the limit. The same sets in the Hangar, measured on a real 0.4.7 server and then on the 0.4.8 server, are in the table under "Ships and items: what your old cells and thrusters become", and they include the eighth shield counting 50 percent. With a full set a Paragon took 640,000 before its hull was gone and now takes 537,172 (16 percent less), a Wraith took 1,011,622 and now takes 861,930 (15 percent less), an Ironclad took 1,393,305 and now takes 1,246,290 (11 percent less); the Protos, Kitefin and Ostirion take the same as before. **To get the capacity back, fit Capacity cells.** A Capacity Shield Cell IV has the Sovereign's 12,000 capacity and 1,000 recharge with +5 points of absorbance instead of +10. Mixing the two families is the best fit for a big ship: a Wraith with 25 Capacity IV and 11 Absorption IV cells in its twelve Heavy Shield Cores, the Capacity cells in the slots that count most (the Hangar shows what each slot counts), takes 1,057,410 before its hull is gone, where 36 Sovereigns took 1,011,622.
- **Your thrusters are converted in place** to the nearest Impulse Thruster, which multiplies a little too (x1.02 to x1.03). **Only the owners of a Plasma Thruster fly slower, on every ship:** up to 1.94 of the 62.4 engine points of an Engine III with three of them (3.1 percent; a Wraith with that engine goes from 301.8 to 299.8, a Protos from 223.1 to 221.0, 0.9 percent; about 2 percent of a ship's speed when every engine holds three of them). The owners of a Thruster I, a Vector, a Thruster II, an Ion Thruster and a Thruster III fly faster or just as fast in every host (the table is in the same section). It adds up per engine. **A thruster with a Forge buff on its multiplier can lose a little more,** because a buff on the new thrusters' small multiplier is worth a thousandth: with every stat at the top of the Eternal tier (x1.15), the worst host loses 5.7 engine points for a Plasma Thruster, 1.7 for a Thruster II, 1.5 for a Thruster I and 0.8 for a Thruster III (the Vector and the Ion Thruster still gain). Such a buff keeps working until the piece is forged again.
- **Queued crafts, the Transport Cache and bonus codes follow:** a cell or thruster in a queued craft collects as the renamed piece, a cached piece stays cached, and a bonus code that named an old cell gives the new one. The Shop no longer sells any cell or thruster for Thulium.
- **Rockets have new names:** Lancet is Lancet I, Javelin Lancet II, Harpoon Lancet III, Rivet I, II and III were Rivet, Mallet and Piledriver, Ember I, II and III were Ember, Corona and Eclipse, Scatter I, II and III were Scatter, Barrage and Maelstrom. Your stacks, your hotbar slots, your ammo statistics and your bonus codes are renamed with them. Prices, stacks and reach are unchanged, but **their damage now varies:** on average a rocket hits 10 percent below its old number (5 percent for the N.U.K.E. and N.I.K.E.), because the old number is now the top of the band.
- **Forge:** items you have keep every buff. From now on a tier-up fills a further slot only half the time, so a Godly piece has its second buff half the time; merging two copies fills a slot a tier-up missed.
- **Respawn:** a ship that comes back from a death has at most 10,000 hull and no shield, so a Wraith or an Ironclad must repair after it. "Return to Base" docks it at 10,000 and the Hangar does not repair it.
- **Your PvE score is recounted** at the server's first start from your kill statistics, so your old kills count at the new weights. Nobody loses points for kills: every weight is 1 or more.
- **Station missions you have accepted** are carried over. A mission that the old tasks already called complete completes, and the others keep what they have and start the new Solar goals.
- **Settings:** your saved values carry over to the new General and Interface tabs.

**Swarms: the Seeker Swarm**
- **Where and when:** from season day 4 (First Contact) until the wipe, each of the sectors M-1, M-2, T-1, T-2, G-1 and G-2 has one swarm in every world: a **Boss Seeker** and up to four **Seeker Slaves.** A boss never appears within 2,500 units of the edge of a station or a gate ring.
- **The Boss Seeker** is four times a Seeker in hull, shield and damage: 3,200 hull, 3,200 shield and a laser volley of 720 in Alpha (a Seeker has 800, 800 and 180). Its speed (120) and range (600) are a Seeker's. It is drawn twice the Seeker's size in an amber livery with a name tag. It does nothing until it is hit; then it stands where it is and fires, and the swarm's members within 1,500 units join against the first pilot who shot.
- **Seeker Slaves** are plain Seekers (800 hull, 800 shield, 180 a volley). One comes every 10 seconds, up to four. Each one within 600 units heals the boss 50 hull points a second (hull only, never shield). They stay within 500 units of it and leave 30 seconds after it dies, unless they are attacking.
- **The worlds:** in Beta and Gamma the hull, shield, damage and heal are 1.5 and 2 times these numbers, and the pay 2 and 3 times, as for every alien.
- **Pay:** exactly ten Seekers. Pilots share it by the damage they dealt to the boss; you need 5 percent of it to share, and a group counts as one entry. Under 5 percent you are paid nothing and the Game Log tells you. Your boosters and premium apply to your part.

  | World | Credits | Thulium | Experience | Honor |
  |---|--:|--:|--:|--:|
  | Alpha | 8,000 | 40 | 1,000 | 20 |
  | Beta | 16,000 | 80 | 2,000 | 40 |
  | Gamma | 24,000 | 120 | 3,000 | 60 |

- **The cargo box** goes to the pilot who dealt the most damage (reserved for that pilot and their clan for 30 seconds, then anyone): the loot of ten Seekers (a 20 percent Ship Fragment and a 50 percent 1 to 2 Daraxium, each rolled ten times), 200 to 400 Standard Battery, 10 to 20 Advanced Plasma, 2 to 4 Ultra Core and 2 to 3 rockets of one random credit-shop kind.
- **Back and gone:** a new Boss Seeker appears 2 minutes after one is destroyed.
- **What you are told:** the sector's chat says "Seeker Swarm: Boss Seeker has appeared in this sector." and "Seeker Swarm: Boss Seeker was destroyed." The Global chat's kill feed names the pilot who is credited on every map ("alpha destroyed Boss Seeker"), in every world, without the world's name.
- **Counted by itself:** the Boss Seeker and the Seeker Slave are kinds of their own in your kill statistics. They do not count for the Seeker's quests or Wipe Points; a boss kill earns 5 PvE points, a slave 1.
- **It is dangerous to start the fight.** A new pilot (a Protos, 8,000 hull, no shield) is destroyed in 12 seconds by the boss alone and in 6 with its slaves. A Quantum Laser 2 reaches 700, past the boss's 600, and a Protos is faster than its 120: kept out of its range, two level 3 pilots kill it in 37 to 51 seconds with x1 ammo in the model. Measured on a scratch server, two pilots (a level 3 and a level 2 kit) destroyed one in 17 seconds of fire with x2 ammo and 112 seconds with x1.
- **Other aliens and the company pilots:** an alien never shoots a swarm member and no swarm member shoots an alien; the company pilots (the NPC squads) ignore the swarms.

**Swarms: the Pirate Swarm**
- **Where and when:** from season day 4 until the wipe, each of the sectors M-2, M-3, T-2, T-3, G-2 and G-3 has one Pirate Swarm in every world (18 in all): a **Pirate Boss** and up to five **Pirate Scouts.**
- **The Pirate Boss** is an Ironclad at 50 percent of its hull, shield and damage: 300,000 hull and 50,100 shield in Alpha, speed 92, range 700. It is passive and fires no lasers, and it does nothing until it is hit. It is drawn as an Ironclad in a dark brick-red livery with a name tag.
- **Its weapon is a rocket:** every 5 seconds it fires a straight, unguided rocket at the first pilot who shot it, as long as that pilot is within 970 units (1,000 in the -3 sectors): a Rivet I (2,500 damage) in the -2 sectors and a Rivet II (5,000) in the -3 sectors. It keeps roaming its route while it does. The rocket's damage grows with the world as the lasers' do (1.5 and 2 times in Beta and Gamma).
- **A rocket from an alien** is one of the Rivets above, drawn red, with a quiet sound of its own, and its damage is not rolled. It hurts pilots only: never an alien, a swarm ship or a company pilot, and nothing in a safe ring, in the 3 seconds after a respawn or cloaked. A pilot it destroys dies to an alien. Being straight, it hits the first pilot on its line, so a bystander can take a rocket meant for the attacker, and a ship that keeps moving sidesteps it.
- **Pirate Scouts** are Kitefins at 50 percent in the same livery: 12,000 hull, 9,818 shield, a 98 volley, speed 175, range 700. Up to five, one every 10 seconds, within 900 units of the boss, attacking on sight within 700. Each scout within 600 units heals the boss 40 hull points a second (hull only; 60 and 80 in Beta and Gamma). They leave 60 seconds after the boss dies unless they are attacking.
- **Pay:** the Pirate Boss 116,000 credits, 725 Thulium, 29,000 experience and 232 honor in Alpha (9.7 Goombahs, and more than a Crystalys's 60,000, 200, 12,000 and 52 in each; twice and three times that in Beta and Gamma; split by damage as the Boss Seeker's is); a Pirate Scout 800, 4, 100 and 2, a Seeker's, for the pilot who hit it first.
- **The box**, for the pilot who dealt the most damage: 5 to 10 rockets of one random credit-shop kind and 500 to 1,000 of Advanced Plasma or Siphon Battery, and half the time 1 Reinforced Hull Plate. A new boss appears 2 minutes after one is destroyed.
- **How hard:** in the model, three level 4-5 pilots with x2 ammo destroy it in about 5.6 minutes if the damage is spread over them (it takes four or five pilots if all of it falls on one of them), a level 8 Paragon alone in about 4.4, and a lone level 4-5 pilot cannot. The group it needs grows with the world: 3, 4 and 6 level 4-5 pilots in Alpha, Beta and Gamma if they spread the damage. Killing the scouts first does not pay, since a new one comes every 10 seconds. On a scratch server three level 4-5 Ostirions with x2 ammo destroyed one in 5.4 to 5.7 minutes.

**Swarms: the Dormant Swarm**
- **Where and when:** from season day 4 until the wipe, one Dormant Swarm lives in each world, on the Danger Sectors DS-1 to DS-4, and starts on a random one of them.
- **The Dormant Force** is a Wraith at 100 percent with lasers three times a typical fit's: 324,000 hull, 83,400 shield and a 2,880 volley in Alpha, speed 225, range 800. **Two Dormant Pulses** are Paragons at 100 percent (128,000 hull, 64,570 shield, a 1,920 volley, speed 210) and follow it. They are drawn in a violet livery with name tags.
- **They sleep until they are hit.** Then every member within 1,500 units joins against the first pilot who shot. Each fires a straight rocket every 5 seconds, as the Pirate Boss does (and from up to 990 and 1,000 units): a Rivet III (7,500) for the Force, a Rivet II (5,000) for each Pulse.
- **They travel.** The swarm stays 8 to 15 minutes on a Danger Sector, then flies to the gate of another one and jumps through it as a pilot does: a 3-second charge, a warp flash and a quiet sound of its own. It never takes the three gates out to the company maps and never enters the black hole's circle, and it neither starts nor ends a jump within 10 seconds of a hit (a hit in the charge ends it); a pilot who keeps it under fire keeps it where it is, and can jump after it.
- **Back:** 1 hour after all three are destroyed, on a random Danger Sector. If the Force is destroyed first, a Pulse leads the others. A server restart starts the swarm anew.
- **What you are told:** every pilot flying in the world, on any map, gets a chat and Game Log line when the swarm appears ("Dormant Swarm: Dormant Force has appeared on DS-2."), every hour it lives ("The Dormant Swarm is still out there: it is on DS-3 now.") and when the last of its ships is destroyed. A violet marker shows its sector on the galaxy map and its ships on the minimap of that sector, and the Global chat's kill feed names the pilot credited with the Force.
- **Pay** (Alpha; 2 and 3 times in Beta and Gamma), split by damage, each ship its own kill: the Force 160,000 credits, 535 Thulium, 32,100 experience, 139 honor; each Pulse 75,000, 255, 15,200 and 66.
- **The Force's box:** 2,000 to 3,000 Ultra Core and Experimental Fusion Core in total, 30 to 50 rockets of one random Epic kind, and half the time a N.I.K.E. or a N.U.K.E. Each Pulse drops, 20 percent each, an Ancient Control Unit, a Power Core and 1 to 5 Dark Matter.
- **How hard:** in the model eight level 8 Paragons win with x2 and with x4 ammo and one never does. The smallest winning group is 4 pilots on x2 ammo (3 on x4) in Alpha, 6 (4) in Beta and 8 (6) in Gamma.

**Ships and items: what your old cells and thrusters become**
- **The cells:** the row, owner, place, Forge tier and buffs are kept; the numbers become the new tier's (capacity, recharge a second, absorbance in points):

  | Old cell | Becomes | Old: capacity, recharge, absorbance | New |
  |---|---|---|---|
  | Basic | Absorption I | 1,000, 100, +2 | 1,500, 125, +4 |
  | Advanced | Absorption I | 2,500, 250, +4 | 1,500, 125, +4 |
  | Reinforced | Absorption II | 4,200, 350, +6 | 3,000, 250, +6 |
  | Elite | Absorption III | 6,000, 500, +7 | 4,500, 375, +8 |
  | Prime | Absorption III | 8,500, 700, +8 | 4,500, 375, +8 |
  | Sovereign | Absorption IV | 12,000, 1,000, +10 | 6,000, 500, +10 |

- **A full set** (three cells in every Heavy Shield Core) in the Hangar, measured on a real 0.4.7 server and then on the 0.4.8 server, with the eighth shield counting 50 percent. "Takes before its hull is gone" is the shield and the hull together, but no more than the hull divided by one minus the absorbance:

  | Ship (generator slots) | Shield | Recharge a second | Takes before its hull is gone |
  |---|--:|--:|--:|
  | Protos (4) | 362,950 to 255,850 | 22,806 to 13,881 | 40,000, the same |
  | Kitefin (5) | 429,059 to 302,451 | 26,960 to 16,410 | 120,000, the same |
  | Ostirion (6) | 524,409 to 369,666 | 32,952 to 20,057 | 240,000, the same |
  | Paragon (8) | 567,109 to 409,172 | 35,635 to 22,200 | 640,000 to 537,172 (16 percent less) |
  | Wraith (12) | 687,622 to 537,930 | 43,207 to 29,186 | 1,011,622 to 861,930 (15 percent less) |
  | Ironclad (14) | 793,305 to 646,290 | 49,848 to 35,065 | 1,393,305 to 1,246,290 (11 percent less) |

- **The thrusters** (speed and multiplier; the engine points of an Engine III with three of them, before and after; and the speed of a Wraith with that engine):

  | Old thruster | Becomes | Old: speed, multiplier | New | An Engine III with three | A Wraith with an Engine III and three |
  |---|---|---|---|--:|--:|
  | Thruster I | Impulse I | +5, x1.00 | +5, x1.02 | 21.0 to 22.3 | 258.3 to 259.6 |
  | Vector | Impulse II | +7, x1.02 | +10, x1.02 | 27.4 to 38.2 | 265.0 to 276.4 |
  | Thruster II | Impulse II | +10, x1.05 | +10, x1.02 | 36.9 to 38.2 | 275.0 to 276.4 |
  | Ion | Impulse III | +13, x1.08 | +15, x1.03 | 46.6 to 55.7 | 285.1 to 294.8 |
  | Thruster III | Impulse III | +15, x1.10 | +15, x1.03 | 53.0 to 55.7 | 291.9 to 294.8 |
  | Plasma | Impulse IV | +18, x1.12 | +17, x1.02 | 62.4 to 60.5 | 301.8 to 299.8 |

**Ships and items: the shield cells**
- **Two families, four tiers each.** Capacity cells hold and recharge twice as much as the Absorption cell of the same tier, Absorption cells add twice the absorbance. Absorbance is in points added to the core's own 45, 48 or 50 percent.

  | Cell | Rarity | Capacity | Recharge a second | Absorbance |
  |---|---|--:|--:|--:|
  | Capacity Shield Cell I | Shoddy | 3,000 | 250 | +2 |
  | Capacity Shield Cell II | Common | 6,000 | 500 | +3 |
  | Capacity Shield Cell III | Rare | 9,000 | 750 | +4 |
  | Capacity Shield Cell IV | Epic | 12,000 | 1,000 | +5 |
  | Absorption Shield Cell I | Shoddy | 1,500 | 125 | +4 |
  | Absorption Shield Cell II | Common | 3,000 | 250 | +6 |
  | Absorption Shield Cell III | Rare | 4,500 | 375 | +8 |
  | Absorption Shield Cell IV | Epic | 6,000 | 500 | +10 |

- **No stat of any cell is above the Sovereign's** (12,000, 1,000, +10), so no set of the new cells beats a set of Sovereigns counted the same way. The best Heavy-core set is still exactly 80 percent, and only with three Absorption IV in the core; a set of Capacity cells is 65 percent.
- **Where you get them:** the Shop sells tier I of each family for 30,000 credits and nothing else (no cell is sold for Thulium any more). Tiers II to IV are made in Assembly out of one loose piece of the tier below, which keeps its Forge tier while its buffs are rolled again:

  | Step | Takes | Thulium | Also | Time |
  |---|---|--:|---|--:|
  | II | a tier I cell | 1,000 | 10 Cataclysite, 4 Reinforced Hull Plates, 2 Velkonite Reinforced Plates | 1 min |
  | III | a tier II cell | 1,500 | 15 Cataclysite, 6 Reinforced Hull Plates, 4 Velkonite Reinforced Plates | 1 min |
  | IV | a tier III cell | 2,500 | 20 Cataclysite, 8 Reinforced Hull Plates, 6 Velkonite Reinforced Plates | 1 min 30 s |

- **The quests that paid a cell** now pay an Absorption Shield Cell I (quest 7), a Capacity Shield Cell I (quest 23) and an Absorption Shield Cell II (quest 66), and the ALPHATESTER code gives an Absorption Shield Cell I.
- **A rule of thumb** (it has a help card on the Shop's cell page): a ship held by its hull (the Protos, Kitefin, Ostirion and most of the Paragon) wants Absorption; a ship held by its shield (the Ironclad, and the Wraith in a mix) wants Capacity.

**Ships and items: the thrusters and the speed formula**
- **Impulse** adds the most flat speed and multiplies a little; **Momentum** adds less flat speed and multiplies more. Tier I is sold for 20,000 credits, tiers II to IV are made in Assembly out of the tier below.

  | Thruster | Speed | Multiplier | Step: Thulium, also, time |
  |---|--:|--:|---|
  | Impulse I | +5 | x1.02 | Shop, 20,000 credits |
  | Impulse II | +10 | x1.02 | 1,000, 10 Ship Fragments, 1 Power Core, 2 Velkonite Reinforced Plates, 1 min |
  | Impulse III | +15 | x1.03 | 1,500, 30 Ship Fragments, 2 Power Cores, 4 Velkonite Reinforced Plates, 1 min |
  | Impulse IV | +17 | x1.02 | 2,000, 60 Ship Fragments, 3 Power Cores, 6 Velkonite Reinforced Plates, 1 min 30 s |
  | Momentum I | +4 | x1.08 | Shop, 20,000 credits |
  | Momentum II | +8 | x1.10 | as Impulse II |
  | Momentum III | +11 | x1.13 | as Impulse III |
  | Momentum IV | +12 | x1.14 | as Impulse IV |

- **The new formula:** an engine or Adaptive Core adds `(its own base speed + the flat speeds of its thrusters) x the product of their multipliers` to the ship's speed. Until 0.4.7 the multipliers acted on the engine's own base speed alone (2, 4 or 6, and nothing for an Adaptive Core), so a multiplier was worth almost nothing. A Momentum Thruster's multiplier is worth more in a bigger host: an Engine III with three Momentum IV makes 62.2 where three Impulse IV make 60.5.
- **The best builds:** the best Engine III holds an Impulse IV and two Momentum IV (62.3), the best Adaptive Core II two Impulse IV (35.4, where a Momentum pair makes 31.2). **The Wraith's best build, 872.2, is still the fastest of the six ships,** the Ironclad's best is 822.3, and the Ironclad's base speed stays 92. The best builds move down by 0.5 (the Protos) to 5.0 (the Ironclad) from the Plasma Thruster builds of 0.4.7.
- **Against an Ostirion with an Engine II and two thrusters,** an Impulse Thruster I flies it at 223.1 and a Momentum Thruster I at 222.6, which is slower than a Crystalys (230). From tier II both families outrun it: 234.0, 245.5 and 249.1 for Impulse II, III and IV, 233.2, 242.5 and 245.8 for Momentum II, III and IV (the Momentum II by 3.2).
- **The Forge's buff on a multiplier** acts on the part above 1 only: a x1.15 buff on a Momentum IV's x1.14 makes x1.161, not x1.311, and on an Impulse IV's x1.02 it makes x1.023. The Forge rolls no buff on a multiplier of 1.05 or less, so an Impulse Thruster holds one buff (its flat speed) at every tier and a Momentum Thruster two.
- **Every thruster card shows its Speed Multiplier,** the Impulse Thrusters' x1.02 and x1.03 too.

**Ships and items: the eighth shield counts 50 percent**
- **The rule:** the shields of a ship are counted by place, best first: the first four count 100 percent, then 85, 70 and 55, and **from the eighth on 50 percent (it was 25).** The slot's share (core 100, support 75, auxiliary 50 percent, a drone's slot 100) applies on top. The engines' places are as they were, 25 percent from the eighth on. An Adaptive Core takes the shields' tail for its shield and the engines' for its speed.
- **Who gains:** only a ship with eight or more shields. The Protos (4 generator slots), Kitefin (5) and Ostirion (6) do not change on their own slots. In the best fit of each ship (the best mix of Capacity IV and Absorption IV cells): the Paragon's shield on its own slots +2.1 percent, the Wraith's +9.0, the Ironclad's +15.6 (793,305 to 916,830). Shields on drones gain the most: an Ironclad with 16 drone shields goes from 1,128,555 to 1,587,330 (+40.7 percent).
- **The Hangar shows it.** A generator slot that counts less than all of its item carries a small percent badge (for example 64 percent for the 5th shield, 85 percent, in a support slot, 75 percent). The item's card says "Counts 64%: shield no. 5 (85%), support slot (75%)", and the Shield and Speed tiles list the items by place and say what a further one would add. The flight Ship window shows the same lists on hover.

**Ships and items: the Forge**
- **After the first buff, a further buff is a 50 percent chance.** A tier-up gives an item with no buff its first for sure. For every other slot the new tier holds, it rolls a 50 percent chance on its own; a slot that misses stays free, and the next tier-up tries it again. The Forge panel says "up to N" buffs.
- **What it means on average** for an item with four stats (a Shield Core): 1.0 buff at Tainted, 1.5 at Godly, 2.25 at Rupturing, 3.1 at Eternal (it was 1, 2, 3, 4). Merging two copies still fills what was missed. Items that exist are not touched.
- **An Assembly upgrade keeps the number of buffs of the piece it uses up** (a Pulse Amp into a Nova Amp, a Quantum Laser 3 into a Starfire-3, a cell or a thruster into the next tier), at least one above Standard; the buffs themselves are rolled again as before. A piece that has one buff rolls it again on a random stat.
- **The lottery at collection** (the tier a craft can win) is not changed: a won tier still carries the whole set.

**Ships and items: rockets**
- **Names:** Lancet I, II and III (guided, single target), Rivet I, II and III (straight, single target), Ember I, II and III (guided, blast) and Scatter I, II and III (straight, blast). I is Common, II Rare, III Epic. The N.U.K.E., the N.I.K.E. and the admin Kick Rocket keep their names. The hotbar codes are LNC I, LNC II, LNC III, and likewise RVT, EMB and SCT. Speed, reach, price and stack of each rocket are as before (a Lancet I costs 500 credits, a Lancet III 5 Thulium), and so is the number that is now the top of its damage band.
- **Damage is rolled once, when the rocket is fired,** uniformly from a lowest share of its number to all of it, and a blast deals that one roll to every ship in it. The number of the old tables is now the top of the band:

  | Rocket | Damage |
  |---|---|
  | Lancet I, II, III | 1,600-2,000, 3,200-4,000, 4,800-6,000 |
  | Rivet I, II, III | 2,000-2,500, 4,000-5,000, 6,000-7,500 |
  | Ember I, II, III (at the centre) | 1,120-1,400, 2,240-2,800, 3,360-4,200 |
  | Scatter I, II, III (at the centre) | 1,400-1,750, 2,800-3,500, 4,200-5,250 |
  | N.U.K.E. (at the centre) | 45,000-50,000 |
  | N.I.K.E. | 67,500-75,000 |

  The twelve roll 80 to 100 percent (a laser volley's own band); the N.U.K.E. and N.I.K.E. roll 90 to 100, so what they destroy in one hit stays reliable. There is no critical hit, and nothing about your ship, amps, ammo or drones changes the roll. The Shop's cards and the hotbar tooltips print the range.
- **What it does to the fights:** a Lancet I still kills a Seeker in one hit at every roll, and a Phantasm in three on average (four at the lowest roll). A Rivet II kills a Phantasm in one hit at a roll of 89 percent or more, else in two. A N.I.K.E. still destroys a fresh Protos, Kitefin or Ostirion in one hit at every roll. A N.U.K.E. still destroys a fresh Protos anywhere in its blast, but a fresh Kitefin only within 50 units of the burst (220 units at the best roll).

**Combat and respawn: dying and coming back**
- **No welcome line** after a respawn or a reconnect; a launch still welcomes you.
- **3 seconds of protection after every respawn** (base, portal or the spot): the ship cannot be hurt and **cannot attack.** A laser or a rocket is refused with "You can't attack while your spawn protection lasts." and only the time ends the window, not a refused shot. This replaces the old 5 seconds that your first shot ended. The EMP, the Cloaking CPU and the three abilities still work, since none of them deals damage. The chip on the screen counts the seconds.
- **At most 10,000 hull and an empty shield.** A ship returns with the smaller of its hull and 10,000: a Protos (8,000) returns whole, a Kitefin (24,000), Ostirion (48,000), Paragon (128,000), Wraith (324,000) and Ironclad (600,000) at 10,000 of their own maximum. The death screen says so. A Repair Drone I needs about 65 seconds from 10,000 to full on a big ship, a Repair Drone IV about 19. Reviving a wrecked ship in the Hangar gives the same hull; changing company (5,000 credits) still repairs in full.

**Combat and respawn: PvE points by toughness**
- **A kill pays PvE points by how tough the alien is,** the square root of its hull plus shield divided by 1,600, rounded: **Seeker 1, Phantasm 2, Bulwark 4, Goombah 7, Crystalys 16.** The weight is the same in every world. Swarm kinds: Boss Seeker 5, Seeker Slave 1; Pirate Boss 10, Pirate Scout 1, Dormant Force 25, Dormant Pulse 10.
- **Existing scores are recounted at the server's start** (and at every start after it) from your kill statistics: level times 100, experience divided by 1,000, and every kill at its weight. A pilot with 100 Seekers and 10 Crystalys goes from 455 to 605 in the test; a pilot who killed every kind from 1,108 to 1,333. The PvE ranking reorders: a hunter of Goombahs and Crystalys can pass a pilot killer.
- The Rankings page, Statistics > Ranking and the in-flight Ranking window list "Points per alien kill"; the PvE help card and the alien articles state the weights.

**Combat and respawn: no station in the Danger Sectors**
- **DS-1 has no Mission Control station** any more (DS-2, DS-3 and DS-4 never had one). The safe zones of a Danger Sector are its gate rings. A pilot parked at the old station launches there unprotected. Take and claim missions at a base; the missions you have keep counting.

**Groups: what a mate shoots**
- **A mate's row shows their target:** its name (a skull for an alien, a person for a pilot, a robot for a company pilot) and two thin bars, hull and shield. The hover card gives the exact numbers ("Hull 13,936 / 16,000 (87%)"). It shows for 5 seconds after your mate's last lock, only for mates on your map in your world. A cloaked pilot's bars reach only the mates who could see that pilot anyway. Stations and gates are never targets. You never see your own target in the group (you have the Target window).
- **The Group window opens 380 points tall,** enough for a full group of five fighting. A pilot who once dragged the window keeps a saved height of 296 points and can have the last row cut until they resize it.
- **Fixed:** hovering a bar in the Group window drew two cards on top of each other; there is one card at a time now.

**Missions and Skylab**
- **Station missions 6 and 7 ask for a Solar level** where they asked to keep the power at 0 or more (which has been true for almost everybody since 0.4.7's Solar), and **mission 9 asks for Core and Solar 6** where it asked for 5. Nothing may go above the Core, so the Core comes first. Pay is unchanged.

  | # | Mission | Now asks for |
  |--:|---|---|
  | 5 | Brighter Panels | Raise Solar to level 3 (the briefing says the farms keep running) |
  | 6 | The Thulium Line | Build a Thulium Farm and raise Solar to level 4 (take the Core to 4 first) |
  | 7 | Growing Season | Raise the Credit Farm to level 3 and Solar to level 5 (the Core goes to 5 first) |
  | 9 | Open the Supply Line | Raise the Core and Solar to level 6 (it asked for 5); it opens after mission 7 |
  | 10 | Core Ten | Raise the Core to level 10: it climbs from Core 6 now, in four steps, about 93,000 credits and 3 hours of timers |

- **Solar keeps making the power of its current level while it upgrades.** Until now a Solar upgrade switched every farm and collector off for its timer. Now nothing is switched off, and the Forgery can start new batches.
- **A 0.4.7 client** keeps showing "Offline while upgrading" on the Solar card and the old warning before a Solar upgrade; the server is right.

**Menus, Settings and wiki**
- **The station menu has no status bar or ticker** at the bottom any more. It only ever showed a welcome tip and an echo of the page you had opened, never anything from the server.
- **Credits and Thulium are at the top right of the toolbar,** beside the honor and the sector: Premium, credits, Thulium, honor, sector, Launch. On a narrow window the amounts shorten from 10,000 up (987.7M) before Premium drops to its crown, and hovering an amount shows the whole number.
- **Assembly shows the full description on hover** of a recipe, a queue row, a material, a Forge cost row, an upgrade chain tile or a Forge piece. A cut description line gets one wrapped tip.
- **Settings has a new Interface tab,** second in the switch. **General** keeps the language, Camera Zoom, "Camera stays where I put it" and Reset view, Do Not Disturb and the crash-report switch. **Interface** holds HUD Opacity, Show Stats Overlay, Show network info, Show My Drones, Show Enemy Drones and Show Map Grid, and Show kill feed, Hide Global chat and Ignored pilots. No setting changed its name or its value.
- **The kill-log capsules at the top centre of the screen are gone.** The Game Log window (the Log button) lists the same lines, and the chat's Global kill feed is untouched. "Portal too far to jump." is a toast. The claim-denied line ("X hit it first: the reward is theirs"), friendly-fire honor penalties, "Quest Failed" and the Shield Surge and Emergency Repair end reports are in the Game Log only.
- **Wiki text can be selected and copied.** Drag across paragraphs, lists, headings, tables, formulas and quotes, and press Ctrl+C (Cmd+C on a Mac); links still follow a click. A **Copy page** button over every article copies the page as Markdown, in your language, and shows "Copied". A drag has to start on text and does not scroll the page: for a long page use Copy page.
- **The wiki's pages** for the shield cells, the thrusters, the Forge, the rockets, the speed, the shields and inventory, the respawn and the Groups follow these numbers, in all 12 languages. A Swarms category, beneath the Aliens, has an overview and an article for each of the three swarms, and the Wipe Timeline says that the swarms begin at First Contact (day 4); the swarms' numbers in those pages are written from `Swarms.json`.
- **Help cards** for the generators' places, the cells' rule of thumb, rocket damage, the Forge, PvE points, respawn and groups are new or changed, in 12 languages.

**Windows memory**
- **What was found:** the Chrono-Gate's count on the Galaxy Gates page was drawn at a new font size every frame of a Materializer spin, and every new size grew the font texture, which never shrinks and exists three times. On a Mac, 236 spins took the game's live memory from 316 to 1,276 MB and the texture to 16384 x 8192 pixels (537 MB a copy).
- **What was fixed:** text sizes that follow an animation, a drag or a window are snapped to whole pixels (the gate's count steps in 3 percent rungs), and the texture is at most 2048 x 2048 pixels (16.8 MB a copy). The same run now stays flat, 222 to 258 MB in our runs. The hub copies a map update's data far less often (4,888 allocations to 1,699 for one update, 20 times a second).
- **A memory line in the log file:** once a minute `spacecorps2027.log` gets a `mem` line with the process's memory, the font texture, the textures and meshes, the connection's inbox and the cache. It holds numbers only, no account data. If the game takes more memory than you expect, send the log.
- **Not proven:** this is the only thing we found that made memory climb in our runs, and it is not proven to be what some Windows PCs showed (the Windows heap and the graphics driver could not be measured here). An optional test build of the game with another memory allocator exists for A/B tests; the release uses the default one.

**Fixes**
- **Item names keep their tier** where a tile or card cuts them (the Transport Cache, the Shop), and a cut name has no space before its ellipsis.
- **The rocket picker's tiles fit the new codes:** the code has the bottom of the tile and the count moved to the top left, so LNC III, RVT III and the others fit.
- **A price or a badge that fits keeps its size;** only text made smaller to fit snaps to whole pixels.
- **A refused jump** ("Portal too far to jump.") is a toast now, so it is not lost with the kill-log capsules.

**For administrators and the server**
- **Swarm tools:** `GET /api/admin/swarms` and `POST /api/admin/swarms/spawn`, `/remove`, `/gate`, `/move` and `/timing` spawn a swarm on a map now, take it off, move the season day the swarms start on in a world, send the Dormant Swarm to a Danger Sector (at once or by its gate) and set its dwell and return times. They are recorded in the admin actions (`swarm-spawn`, `swarm-remove`, `swarm-gate`, `swarm-move`, `swarm-timing`); a 0.4.7 admin page lists them as "other".
- **Config files:** `Resources/Swarms.json` is new (the swarms' strength, pay, drops and timers; the server refuses to start with a wrong one and says which field). `RespawnConfig.json` has `respawnInvulnerableSecs` (3) and `respawnHull` (10000) in place of `protectionSecs`. `Rockets.json` has `rollMin` (0.8) and `specialRollMin` (0.9); 1.0 makes the damage fixed again. `ForgeConfig.json` has `extra_buff_chance` (0.5; 1.0 restores 0.4.7). `Groups.json` has `targetSecs` (5). `ranking-config.json` has the PvE weights.
- **The server renames in place at its first start** the cells and thrusters (twelve names) and the rockets (twelve), with their stacks, hotbars, statistics, admin records and bonus codes, and recounts the PvE points at every start. Take a volume backup first (`docs/DEPLOY.md`, "The deploy of 0.4.8").

## 0.4.7 · 2026-10-02

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.7)

SpaceCorps 2027 0.4.7 puts ten missions about your Skylab into Mission Control and gives Solar enough power for the whole station. Rockets hold ten times more, weigh nothing and fire with no laser fitted; a shield on a drone counts; the Engine III, Thruster III and Heavy Shield Core are made in Assembly; and aliens stay on the first pilot who shot them. The Ironclad is slower (base speed 92), so the "If you already play" list below is worth reading.

### What's new

**Highlights**
- **Ten Station missions** in Mission Control, from your first Solar panel to Core 10, with a section, three slots and a flat pay of their own.
- **Solar powers the whole station:** at level N it makes what every module draws at level N, and a tenth more.
- **Rockets:** stacks ten times larger, no weight, no laser needed to fire; the N.U.K.E. does 50 percent at the edge of its blast (it was 25).
- **A shield on a drone counts** as a shield in a core slot.
- **Engine III, Thruster III and the Heavy Shield Core are made in Assembly.** The **Starfire-3** is made out of a Quantum Laser 3 and keeps its tier.
- **The Ironclad's base speed is 92** (it was 140): a nerf of its speed.
- **Aliens stay on the first pilot who shot them,** and packs keep apart.
- **The galaxy gate's standard scan finds a part 5 percent of the time** (it was 1).
- **Numbers of 1,000 and more are grouped in every language.**
- **In-order missions are unmistakable;** **Reduce screen shaking** is its own switch; a **network readout** (off by default) tells whose side lags.
- **The wiki is in all 11 other languages** (first translations, not read by native speakers yet).
- For administrators: a **server console** and `TCP_NODELAY` on every connection.

**If you already play: what changes for you**
- **The Ironclad is slower.** Base speed 92, not 140: a stock one flies at about 99 (it was 147), with Basic Shield Cores at about 60 (92), with Heavy ones at about 39 (60). A nerf of its speed, made after the Engine III became craftable. Its hull, slots, lasers and price are as they were.
- **Solar makes more power at every level,** so nothing that ran stops, and farms the old Solar left dark produce again from the server's first start.
- **Station missions** are in Mission Control. A Skylab you already built counts: a mission already true when you accept it is done at once and pays in full.
- **Rockets:** carry 5,000 common, 2,000 rare and 500 epic ones (N.U.K.E. 10, N.I.K.E. 20), at no weight, so a Transport Cache they filled has room again.
- **A shield on a drone now works,** its speed penalty included, and a weak one lowers your absorbance: check the Hangar before you fly.
- **Starfire-3:** the recipe asks for a Quantum Laser 3, at the same total cost. Yours are as they were.
- **Aliens** turn on the first pilot who shot them and stay on them.
- **One alien has a new name:** the one that fights from 800 units (speed 180, between the Bulwark and the Crystalys) is the **Goombah**. Its kill statistics, Wipe Points progress and missions carry over.
- **The standard gate scan is 5 percent;** the deep scan is still 10.
- **Reduce Motion no longer stops the camera shake:** that is Reduce screen shaking now. If Reduce Motion was on, both are.
- **Numbers:** Spanish, Italian and Hungarian group four-digit numbers (1.234, 1 234) like the others.

**The Station missions**
- **Where:** a Station section at the top of Mission Control's Missions page, with how many of the ten you have done and its own pill of three slots. The Active Quests window shows them with a Station mark and the Skylab's own reading ("Core 2 / 3", "Collected 340 / 1,000 credits").
- **The ten** (a mission opens at a pilot level, and after the missions it names are **claimed**, not just done):

  | # | Mission | Opens at | After | Asks for | Pays (credits, Thulium, XP) |
  |--:|---|:-:|:-:|---|---|
  | 1 | Light the Station | pilot 1 | – | Build Solar | 1,500, 100, 300 |
  | 2 | First Farm | pilot 1 | 1 | Build a Credit Farm | 3,000, 100, 350 |
  | 3 | Payday | pilot 1 | 2 | Collect 1,000 credits from the Credit Farm | 2,000, 20, 350 |
  | 4 | Heart of the Station | pilot 2 | 2 | Raise the Core to level 3 | 4,000, 10, 400 |
  | 5 | Brighter Panels | pilot 2 | 4 | Raise Solar to level 3 | 2,000, 40, 600 |
  | 6 | The Thulium Line | pilot 3 | 5 | Build a Thulium Farm and keep the power at 0 or more | 5,000, 100, 1,000 |
  | 7 | Growing Season | pilot 4 | 6 | Raise the Credit Farm to level 3 and keep the power at 0 or more | 4,000, 80, 800 |
  | 8 | Fifty Thousand | pilot 4 | 3 and 7 | Collect 50,000 credits from the Credit Farm | 5,000, 50, 1,500 |
  | 9 | Open the Supply Line | pilot 4 | 4 and 5 | Raise the Core and Solar to level 5 | 5,500, 60, 1,500 |
  | 10 | Core Ten | pilot 5 | 9 | Raise the Core to level 10 | 20,000, 50, 1,500 |

  They pay 80 honor in all, too. A locked card says what it waits for ("Reach level 2", "Finish ... first", "Claim ... first").
- **Their own allowance:** you may have **three Station missions active** at the same time as your five other missions; a Station mission can wait hours for an upgrade timer and must not hold one of the five. Accepting one does not take the tracking from a mission you are flying with.
- **Paid flat:** exactly what the card prints, in credits, Thulium, experience and honor. No world bonus, no boosters, no Season Store boost, no premium experience, no items.
- **If you already have a Skylab:** a mission that asks for a level or for power is done the moment you accept it if it is true then, and pays in full. The two that collect credits (Payday and Fifty Thousand) count only what you collect after you accept.
- **A pilot who has not started** sees the Skylab row in the station menu pulse (in the accent of the Galaxy Gates row) until they build Solar or take the first mission; Reduce Motion makes it a still mark.

**Solar powers the whole station**
- **The rule:** at every level, Solar makes what the Core, both farms, the Resource storage, both collectors and the Forgery draw at that level together, and a tenth more (10 to 11.5 percent). A Solar one level lower is not enough for the full station at any level, so upgrading Solar still matters. The numbers are a table of 20 levels; the old Solar made 100 at level 1 and 30 percent more at each level:

  | Solar level | 1 | 3 | 5 | 7 | 10 | 15 | 20 |
  |---|--:|--:|--:|--:|--:|--:|--:|
  | Now | 255 | 375 | 555 | 835 | 1,580 | 4,880 | 16,010 |
  | Before | 100 | 169 | 286 | 483 | 1,060 | 3,937 | 14,619 |

- **Nothing else about the Skylab changed:** no module's draw, cost, timer or output. Solar makes more at every level, so no pilot loses power.
- **Farms that were dark start again.** A farm or collector the old Solar had left without power produces again from the server's first start. This is a one-time step it does then (`skylab-solar-v2`); what the farm had stored is kept and nothing is made up for the dark time.

**Rockets**
- **Stacks ten times larger:** Common rockets (Lancet, Rivet, Ember, Scatter) 5,000 (it was 500), Rare ones (Javelin, Mallet, Corona, Barrage) 2,000 (200), Epic ones (Harpoon, Piledriver, Eclipse, Maelstrom) 500 (50). The N.U.K.E. stays at 10 and the N.I.K.E. at 20. The Shop sells up to the new stack.
- **Rockets weigh nothing.** They weighed 2, 3 or 5 kg each by rarity, 40 the N.U.K.E. and 8 the N.I.K.E.; now they take no room in the Transport Cache, and their one limit is the stack.
- **The N.U.K.E. does 50 percent of its damage at the edge of its blast** (it was 25). A ship at the edge takes 25,000 of its 50,000 where it took 12,500; the ship whose fuse sets it off takes 47,222 where it took 45,833.
- **Rockets can be fired with no laser fitted.** The report was that rockets could not be shot without lasers: that check is gone from both the game and the server. Each rocket is held to its own rules only (the timer, the stack, a guided rocket's lock). The laser attack itself still needs a laser. The Hangar and the pilot page show a dash for the range of a ship with no laser, since only lasers have one.
- **The Kick Rocket (admins only):** the slowest rocket (speed 150), homing with a lock of 10,000 units and a flight of 70 seconds. It follows the ship it was fired at, passing through every other ship, through safe zones, cloaks and the EMP window; it does no damage, and the pilot it reaches is disconnected and can log straight back in. A ship faster than it can outrun it.

**Drones**
- **A shield on a drone counts as a shield in a core slot,** in either slot of a Master Drone: its capacity and recharge with its cells, its absorbance in the plain mean of your shields, its shield bonus when it is one of your first four, and its speed penalty (Light 1, Basic 3, Heavy 5 percent). It is ranked with your ship's own shields by capacity. The drone's level still raises only its laser. The Hangar, the Ship window and the pilot sheet show the same numbers.
- **A laser on a drone being upgraded no longer counts after you change ship in flight** (a bug fix): its slot is offline while the drone upgrades, as it already was at a launch, but a change of ship in a station left the laser firing until the next recalculation.
- A shield on a drone lowers your absorbance the way a weak shield in a core slot does: see Known issues.

**Assembly**
- **Engine III, Thruster III and the Heavy Shield Core are made in Assembly,** each out of its lower tier. They had no source at all before:

  | | Takes | Thulium | Also | Time |
  |---|---|--:|---|--:|
  | Engine III | an Engine II | 2,000 | 60 Ship Fragments, 3 Power Cores, 6 Velkonite Reinforced Plates | 1 min 30 s |
  | Thruster III | a Thruster II | 1,500 | 30 Ship Fragments, 2 Power Cores, 4 Velkonite Reinforced Plates | 1 min |
  | Heavy Shield Core | a Basic Shield Core | 2,000 | 20 Cataclysite, 8 Reinforced Hull Plates, 6 Velkonite Reinforced Plates | 1 min 30 s |

  They are upgrades like the Helios Beam: the piece you use must be loose (not on a ship, not fitted into another item), keeps its tier, and rolls its buffs again.
- **The Starfire-3 is made out of a Quantum Laser 3.** The step takes the Quantum Laser 3, 15 Ship Fragments, 8 Velkonite Reinforced Plates, 1 Reinforced Hull Plate, 1,500 Thulium and the same 100,000 credits, in 60 seconds; a Quantum Laser 3 and the step together cost exactly what the old recipe did (3,000 Thulium, 25 Ship Fragments, 10 plates, 120 seconds). A Quantum Laser 3 of a higher tier gives a Starfire-3 of the same tier, with its buffs rolled again. So the dice are rolled where the laser is made, which costs no credits: a roll for a good tier no longer costs 100,000 credits, you pay them once for the one you keep.

**The Ironclad's speed**
- **Base speed 92,** the lowest of the roster by far (Protos 150, Wraith 225). It was 140. With the Engine III craftable, an Ironclad built for speed passed the Wraith's best build, and the rules the ships were balanced by broke; 92 is the highest base speed at which every one of them holds.
- **The numbers:** a stock Ironclad about 99 (147 before), a typical build about 215 (269), the fastest build of the model's table about 545 (602). The Wraith's best build, at about 876, is the fastest of the six ships (the Ironclad's best, about 827, is next). A build of Heavy Shield Cores in every slot flies at about 39: the slowest ship a pilot can build, and the black hole's point of no return for it is about 2,600 units (the help card says 1,200 to 2,600).
- **Why it is a nerf:** only its speed changed, after the Engine III made the old figure too fast. Fit Engine IIIs and Plasma Thrusters if you want it quick.

**Aliens**
- **The first pilot who shot an alien keeps it** while the alien can still chase them (they are on the map, outside a safe zone, not dark, alive, and hitting it within the last 10 seconds). Others who shoot it do not take it, however near they are; when the first drops out it turns to the next in order of first hits. It follows up to **32 pilots** per alien. Company pilots count after every player.
- **Packs keep apart:** aliens after the same pilot keep 150 more units between their hulls, and an alien that lets go of a pilot, by a cloak, an EMP, a safe zone or distance, roams from where it stands, away from other aliens within 600 units. They no longer pile up on one spot or fly to the place they last saw you.
- **A siphon volley that finds no shield** to take no longer turns an aggressive alien on the shooter.
- A pilot who shot an alien first can hold it with a shot every few seconds while a partner hits it from outside its reach: see Known issues.

**The Goombah**
- The alien that fights from 800 units and flies at 180 (the fourth of the five, between the Bulwark and the Crystalys) is called **Goombah** now, in the game, the wiki, the missions, the statistics and the Wipe Points page. Its stats, spawns, loot, model and Wipe Points milestones (4 Wipe Points for each 50 kills) are as they were.
- **Your progress carries over:** at its first start the server renames the alien in the database and in every pilot's kill, death and sector statistics and Wipe Points progress, and adds up counts that were kept under two names. A mission that names it keeps its progress and now reads "Goombah".

**The galaxy gate**
- The standard scan, for credits (5,000 a scan), finds a part **5 percent** of the time, where it found one 1 percent of the time. A 100-part gate took about 10,000 credit scans (50 million credits) and now takes about 2,000 (10 million). The deep scan, for Thulium, stays at 10 percent.

**Numbers and fields**
- **Every number of 1,000 and more is grouped in every language,** in the pilot window, a world's pilot count, the map's sizes, the Skylab's power, positions on a board and the amounts in the server's messages. Spanish, Italian and Hungarian used to leave four-digit numbers ungrouped ("Honor 1234" beside "1 234 567" experience).
- **A number you edit in a field ignores the separator:** a group separator is only a display aid, so typing 1,5 in English reads 15 and typing 1,00 reads 100. A tile too small for its digits shows 2.2k, not 2234.

**Missions in order**
- A mission whose tasks must be done in order shows an accent **In order** tag in Active Quests and in Mission Control, and its tasks as numbered steps joined by a line: done steps are checked, the current one is lit and bold, later ones are locked ("Locked until the step before it is done"). Missions in any order keep their quiet "Any order" caption.

**Reduce screen shaking**
- A new switch, **Reduce screen shaking** (Settings, Graphics, directly under Reduce Motion), turns off the camera shake from explosions and blasts, hits on your ship, the Afterburner and a black hole's pull. **Reduce Motion** keeps holding effects still (repair drones, the black hole's disk and warning, ability glows, the pulses of the HUD, softer N.U.K.E. flashes) but no longer touches the shake. If your Reduce Motion was on, Reduce screen shaking is on too. The part count of the Galaxy Gates' scanner, which shook while a scan played, is held still by Reduce Motion now.

**The network readout**
- **Settings, General, Show network info** (off by default) shows a small card at the top right with the **ping** (the round trip to the server), the **jitter** and **snapshot age** of the server's updates, the **longest gap** without one, the **server's** own tick time and your computer's **frame** time, and one line that says which side is slow: Network slow, Network uneven, Network lagging, Server busy, Client slow, Connection stalled or Client froze. The numbers also go to `spacecorps2027.log` once a minute and at every stall, so "it lagged at 21:10" can be answered from a log you send.
- **It needs a 0.4.7 server for the ping and the server's tick** (an older one shows n/a there; every other number is measured by the game).

**The wiki in 11 more languages**
- All **39 wiki pages** exist in German, Spanish, French, Hungarian, Italian, Japanese, Korean, Brazilian Portuguese, Russian, Swedish and Simplified Chinese, shown in your interface language, with the English page where a page is missing. The tables the game writes itself (quests, abilities, drones, the Skylab, Resources) are written in each language from the game's own texts and numbers. A translation whose English page has changed since says so, with a link to the English page. **These are first translations, made by AI and not yet read by native speakers:** please tell us what reads wrong.

**For administrators and the server**
- **The server console:** Admin, Server, Console, and `scripts/server-console.sh` in a terminal. The server's own ticks per second, the tick time (median, 99th percentile, worst) and the time of each of its phases, late and missed ticks, the container's CPU throttling and the VM's steal time, memory, connections, a table of the pilots online, and a log viewer (the last 5,000 lines) with a log level an admin can raise for one module for ten minutes: it goes back by itself, and both changes are in the admin actions. Chat lines are in the log it reads, for admins only.
- **`TCP_NODELAY` on every connection** the server accepts (`SPACECORPS_TCP_NODELAY`, on by default, shown as `tcpNoDelay` in `/health`), so a small message written right after a snapshot is not held for the delayed acknowledgement.
- **Admin seed saves:** a save that failed before it changed the file says so, and a save that failed and could not put the old file back shows as failed in Recent admin actions.
- For the record: the release job can upload each release's Windows build to a private Steam branch by itself; nothing changes for players.

**Smaller changes**
- **Texts and help:** the Speed, Range, Drones, Shield absorbance, Reduce Motion and Gate cards and the wiki follow the numbers above. A Master Drone's third slot, which does not exist, is refused with a text that says so (API only). The Reduce Motion help of French, Swedish, Russian and Brazilian Portuguese names the Repair Drone as the other languages do.
- **The Mission Control cards** show the Skylab's reading of a Station task on a line of its own under the task text.

## 0.4.6 · 2026-10-01

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.6)

SpaceCorps 2027 0.4.6 adds the Ironclad, a crafted tank with the most hull of any ship, and reworks the shields: the best set is 80 percent, the number can pass 100, and rockets and the strong laser ammo penetrate. The Master Drone gets its second slot, aliens fly at whoever hits them, the target panel is a window, Wipe Points from alien kills need half the kills, and the camera zooms out farther and can stay where you put it. Shields, Wipe Points and ranges change, so the "If you already play" list below is worth reading.

### What's new

**Highlights**
- **The Ironclad:** a crafted Epic tank with 600,000 hull, 14 generator slots and 6 lasers, for 10,500 Thulium and parts in Assembly. Its base speed is the lowest of the roster.
- **Shields reworked:** cores of 45, 48 and 50 percent, cells of 2 to 10 points, the best set exactly 80. The number may pass 100; rockets and the x3 and x4 ammo penetrate. Small ships are less tanky.
- **The Master Drone has two slots,** the ones you already upgraded too.
- **Aliens fly at whoever hits them,** blasts of area rockets included: no more free hits on a Gorvane from just outside its range.
- **A ship shoots as far as the average of its lasers,** not its longest: mixed fits reach less.
- **The target panel is a window** (key **V**).
- **Wipe Points from alien kills need half the kills.** **Clan donations are capped** at 1,000,000 credits per pilot in 24 hours.
- **The camera zooms out 50 percent farther** and can stay where you put it.
- **Repair drones fly,** with quiet sounds. The Mission Control label is a **bubble above the station** you click.
- **Windows:** the picture keeps moving while you drag the window, and Copy, Ctrl+C, Ctrl+X and Ctrl+V work (new, and not yet tried by us on every Windows setup). Copy and paste now reach the system clipboard on macOS and Linux too.
- Also: a quieter engine hum, the login music at your volume, no salvage from company pilots, no black hole bubble on the screen, a pilot sheet of one width, soft clicks on toolbar buttons, and password resets for administrators.

**If you already play: what changes for you**
- **Your shields give less out of the box.** Light 45 percent (it was 70), Basic 48 (80), Heavy 50 (85); cells add 2 to 10 points; the best set is 80, not 100. A stock Protos takes 14,545 damage before it is destroyed instead of 26,667; the Wraith is as it was. Forge buffs and Season Store levels stay (a level is now +0.1 point).
- **Your range may be shorter.** A ship shoots as far as the average of its lasers (a Protos with a Quantum Laser 1 and 2: 650, not 700). Equal lasers are as before. The level 6 to 8 quest fits now reach 750 to 775 against a Gorvane's 800.
- **Your next Wipe Points claim may pay more.** What you claimed counts at the new size once, so you are paid up to the new rate for the kills you have. Nobody loses points.
- **A Master Drone you upgraded has a second slot,** empty, and keeps what it carried.
- **Clan donations stop at 1,000,000 credits in any 24 hours,** over all clans.
- **Company pilots drop no salvage.** Ship Fragments and Reinforced Hull Plates come from aliens and mission rewards.
- **The target panel is the Target window,** open at the top centre until you move or close it. **V** shows or hides it; a key you bound to V shows a conflict in Settings.
- **The black hole's bubble on the screen is gone.** The minimap and the warnings still show it.
- **Engine hums are half as loud,** and toolbar buttons click softly (Settings › Button Sounds).

**The Ironclad**
- **What it is:** an Epic tank made in Assembly, between the Paragon (Rare) and the Wraith (Mythical) in rarity and recipe. It has more hull than either: **600,000** (the Wraith 324,000, the Paragon 128,000), and more generator slots: **14**, 7 core, 4 support and 3 auxiliary (the Wraith 12, the Paragon 8). It has **6 lasers** (the Paragon 8, the Wraith 12), 3 extra slots and 3 ability slots. It is a tank, not a better ship.
- **The price:** 10,500 Thulium, 200 Ship Fragments, 35 Reinforced Hull Plates, 10 Power Cores and 1 Ancient Control Unit, 15 minutes of crafting. Ancient Control Units come from Crystalys and mission rewards.
- **Speed:** its base speed is **140**, the lowest of the roster (Protos 150, Wraith 225). With the usual fits it is slower than the Wraith: a stock Ironclad flies at about 147 against the Wraith's 238, a typical build at about 269 against 345, and with a Basic Shield Core in all 14 slots it flies at 92, the slowest ship a pilot can build (its point of no return at the black hole is then about 2,040 units, and the black hole's card says 1,200 to 2,000). **The Wraith stays faster in every ordinary build.** A build fitted only for speed, with Adaptive Cores and Plasma Thrusters, can match or edge past a Wraith with the same fit, by a few percent (up to about 8 percent in the fits we measured), and Forge buffs on the speed stats move it further ahead (with every speed stat at the top of the Eternal tier, by up to about 17 percent in the fits we measured).
- **In a fight:** a Wraith destroys an Ironclad faster than the other way round, and an Ironclad destroys a Paragon.
- **Looks:** a new ship model in teal, cream and orange with twin engines and glowing strips. A 0.4.5 client draws it as a Protos.

**Shields reworked**
- **The cores alone:** Light 45 percent, Basic 48, Heavy 50 (they were 70, 80 and 85). **The cells add points:** Basic +2, Advanced +4, Reinforced +6, Elite +7, Prime +8, Sovereign +10. **The best set, a Heavy core with three Sovereign cells, is exactly 80 percent,** and nothing out of the box is more. A Light core with its cell is at most 55, a Basic core with two cells at most 68.
- **It may pass 100.** Absorbance is the share of a hit your shields take; the rest goes to the hull. Now it is not cut at 100: a hit's penetration is taken off it (between 0 and 100 percent), so what you have above 100 is a margin. The Hangar, the Ship window and the pilot sheet show the same number, with the Season Store buff counted.
- **Penetration:** rockets take points off the absorbance: Lancet 10, Javelin 25, Harpoon 35, Rivet 5, Mallet 25, Piledriver 35, N.I.K.E. 35 (they were shares of it, 10 to 50). The Ultra Core (x3 ammo) takes 5 and the Experimental Fusion Core (x4 ammo) 10. Blasts, aliens, company pilots and the x1 and x2 ammo take none.
- **Ways to 100 and beyond:** the Season Store's Shield Absorbance Boost is now **+0.1 point a level** (it was 0.1 percent of the stat), up to +10 at 100 levels, still **25 Wipe Points a level**. The levels you bought stay and are worth the same or more. Forge buffs multiply the stat as before: an Eternal piece rolled at the top adds up to 12 points to the best set. Today's sources of Wipe Points (855 in total at their caps, carried across wipes) buy 34 levels, +3.4 points, which with a fully forged Eternal set is about 95 percent; the top of the Boost is a goal for several wipes, and more sources of Wipe Points are planned.
- **Small ships are less tanky.** Damage taken before the hull is gone, with no repair: a stock Protos 14,545 (it was 26,667), a Protos with the best cells 40,000 (it was 370,950), a Kitefin with mid shields 54,545 (135,712), an Ostirion with mid shields 109,091 (183,094), a Paragon with the best build 640,000 (695,109). The Wraith is unchanged. A stock Protos lasts 18 seconds against a Bulwark where it lasted 33. Rockets hurt more too: a Harpoon puts 90 percent of its damage on the hull of a stock Protos where 65 percent went before.
- Forged and enchanted shields keep their multipliers: a Heavy core forged to x1.12 is now 0.5 x 1.12 = 56 percent.

**The Master Drone's second slot**
- A Master Drone has **two slots,** each taking a laser or a shield, as its item card always said. Both lasers add their damage, count in the volley, use ammo and get the drone's level bonus. The Drones view draws a box for each slot; a drop goes to the box under the pointer, and a click fills the boxes in order.
- **Every Master Drone you already upgraded has the second slot,** empty, and its first slot keeps what it carried. Nothing is moved and nothing is charged.
- **A shield in a drone slot adds no capacity,** as before, in either slot. It still takes a place in the order your shields are counted in, so keep shields in the ship's own slots.
- A Slave Drone still has one slot; upgrading stays 40,000 Thulium and 100 Ship Fragments.

**Aliens fly at whoever hits them**
- **Area rockets provoke aliens.** The edge of a blast from an Ember, Corona, Eclipse, Scatter, Barrage, Maelstrom or N.U.K.E. now turns every alien it hurts on the pilot who fired it, as a laser hit does; before, only the alien the rocket burst beside did. An alien out of the blast stays where it was. Damage, the kill claim and the rewards are as before. As for lasers, a pilot inside its 3 seconds of EMP provokes nobody.
- **An alien you are hitting comes for you.** For 10 seconds after your last hit (each hit starts the 10 seconds again) it flies at you at its own speed whenever you are beyond its weapon range (Seeker 600, Phantasm and Bulwark 700, Gorvane 800, Crystalys 900), and fires once you are in range. It no longer stands still, and it no longer lets go at 2,500 units while you keep hitting it. So there is no spot from where a Starfire-3 (850) or a Helios Beam (900) hits a Gorvane for free.
- **Several pilots:** the alien still goes for the last pilot to hit it, with one exception: it does not turn from the pilot it is flying at to another who hits it from beyond its range and is no nearer, so a group just outside its range cannot keep it running from one to the next without ever answering.
- **Company pilots answer rockets too:** a squad pilot hit by an enemy player's rocket, direct or blast, now fights back as it does for a laser.
- **A bystander's blast can pull an alien off the pilot tanking it,** as a bystander's laser always could. The kill claim stays with the first pilot.

**Shooting range is the average of the lasers**
- A ship's range is the **average of the ranges of its lasers** (the lasers on the flown configuration and in the drone slots), one number for all of them, rounded to the nearest. Before, it was the longest laser's, so one Helios Beam among cheap lasers set the whole volley's reach. Ships whose lasers are all alike are unchanged. The Hangar tile reads "Avg. range" where they differ, and its tip lists each laser's own.
- **Examples** (Quantum Laser 1 reaches 600, Quantum Laser 2 700, Quantum Laser 3 800, Starfire-3 850, Helios Beam 900):

  | Ship | Fit | Before | Now |
  |---|---|--:|--:|
  | Protos | 2 Quantum Laser 2 | 700 | 700 |
  | Protos | Quantum Laser 1 + Quantum Laser 2 | 700 | 650 |
  | Kitefin | Quantum Laser 3 + 2 Quantum Laser 1 | 800 | 667 |
  | Ostirion | 3 Starfire-3 | 850 | 850 |
  | Ostirion | Starfire-3 + 2 Quantum Laser 2 (the level 6 quest's fit) | 850 | 750 |
  | Ostirion | Helios Beam + 2 Quantum Laser 1 | 900 | 700 |
  | Paragon | 3 Starfire-3 + 3 Quantum Laser 2 (the level 8 quest's fit) | 850 | 775 |
  | Wraith | 12 Helios Beam | 900 | 900 |

- **The quests that kite a Gorvane:** the level 6, 7 and 8 fits (Starfire-3 beside Quantum Laser 2) reach 750, 750 and 775, still past a Bulwark's 700 but 50, 50 and 25 short of a Gorvane's 800. A fit of Starfire-3 only still reaches 850. The quests' times for the Gorvane were not changed.
- **A long laser among short ones counts for less:** a Helios Beam in place of a Quantum Laser 1 adds 100 units to a 3-laser ship and 25 to a 12-laser one. A Forge range buff moves the ship's range by only its laser's share. A fit that averages under 700 is out-reached by company pilots (700), and a Phantasm or Bulwark (aggro radius 700) starts its chase before such a ship can fire.

**The Target window**
- The panel that showed your target (name, distance, hull and shield, the attack and clear buttons) is now a **window:** drag it anywhere, close it with its light, open it with the first button of the top-left toolbar or with **V** (change the key in Settings › Controls, "Target Window"). The game remembers where you put it and whether it is open.
- It is open at the top centre, in the toolbars' row, on every account, and says "No target. Click a ship or an alien." while nothing is selected. Once you close it, it stays closed until you open it.
- Closing it hides only the readout: the target stays selected and the attack key (A), Esc and the hotbar work as before.

**Wipe Points from alien kills: half the kills**
- A Wipe Points milestone takes **100 kills** of a Seeker, Phantasm or Bulwark (it was 200) and **50** of a Gorvane or Crystalys (it was 100). The points per milestone (1, 2, 3, 4 and 5 WP) and the 50 milestones per alien are unchanged, so the most an alien ever pays (50, 100, 150, 200 and 250 WP, 750 in all) is the same: you reach it with half the kills (5,000 of the first three, 2,500 of the last two). The Season page and the help card show the new sizes.
- **Your earlier claims are adjusted once,** at the first start of the 0.4.6 server: what you were paid counts as milestones at the new size, so your next claim pays what the new rate gives for the kills you already have, up to the same maximum. A pilot with 1,000 Seekers who had claimed 5 times can claim 5 more. Nobody is paid at the update, nobody loses points and nobody is paid twice.
- **Update the game.** A 0.4.5 client keeps counting in the old size: its Season page shows milestones of 200 and 100 kills, its Claim button can offer a different amount than the server pays, and a pilot who has been paid everything can still see a button that pays nothing.

**Clan donations are capped**
- A pilot can send **at most 1,000,000 credits into clans in any 24 hours,** summed over every clan. The window slides: a donation counts for 24 hours from its second. Leaving a clan, joining another or a season wipe do not give a new allowance.
- The donate sheet shows **what you can still send,** a bar, the cap, and when the next credits come back. **Max** fills in the most you may send now. A donation over the allowance is refused whole, with the amount you still may send.
- The numbers are a file on the server (`ClanBank.json`) and may change.

**Company pilots leave no salvage**
- A destroyed company pilot (the friendly squad ships of the home sectors) no longer leaves a salvage box, whoever or whatever destroys it. Aliens leave their loot as before, and so do the mission rewards. This takes a source away from Ship Fragments and Reinforced Hull Plates: they still come from aliens and from mission rewards, and the Shop does not sell them.

**The camera**
- **Zoom out another 50 percent:** the mouse wheel (and the middle-button drag) now goes out to 1,500 units from the ship (it was 1,000), which shows about 4,400 by 2,650 units of space, and the **Camera Zoom** slider in Settings goes up to **338 percent** (it was 225). The default is still 150 percent. The server already sends the whole map to every pilot, so nothing pops in at the edge.
- **Camera stays where I put it** (Settings › General, under Camera Zoom; off by default): normally your turn and your zoom ease back to the resting view two seconds after you let go. With the switch on, the view keeps the angle and distance you gave it. **Reset view** next to the switch puts it back once, and so does switching it off. The Camera Zoom slider still moves the camera to its distance.
- A 0.4.5 client stops at 225 percent and may write 225 back over a saved 338 when it saves your settings.

**Repair drones**
- While **Emergency Repair** runs, one to three small drones fly out of your ship, circle the hull and aim soft green beams at its plates, and dock again when the ten seconds end. A **Shield Surge** gets up to two blue drones inside its bubble. Every pilot on the map sees them. Graphics: High draws up to three drone models for your own ship (two for another pilot's), Medium one drone model plus a second drone as a glow (another pilot's repair: one model), Low only the beams and a glow, with no model; Reduce Motion parks them.
- **Quiet sounds go with it:** a blip as the drones leave, one as they dock (the Shield Surge's a fourth higher) and a faint tone under the beams, all far under the repair's own sound. They follow the Sound Effects volume and mute. Nobody has heard them on a real speaker yet; tell us if they are too loud or too quiet.

**Mission Control is a bubble above the station**
- The Mission Control label is no longer a button that slid to the corner of the screen: it is a **bubble in the world above the station** with its tail pointing down at it. Click it to open Mission Control without flying the ship. It keeps its size at every zoom and fades out near the edges of the screen; the "Safe zone active" chip slides out of its way, and a window you drag over it covers it.
- With the station's roof off the screen there is no bubble. Zoomed all the way in, the station's name tag shows instead and opens Mission Control when you click it; at the start of a flight far from the station, with the station off the screen, nothing shows. The Mission Control button in the toolbar still works in the safe zone.

**The black hole's bubble is gone**
- The small black hole in a glow at the edge of the flight view, with "Black hole, N units", is removed. The hole itself is drawn in the world as before, the warnings (the gauge, the red vignette, the point-of-no-return line, the sounds) and the marks on the minimap and the maps stay. In the default camera the hole is on the screen only within about 3,000 units, so from farther off nothing in the flight view shows where it is, unless you turn the camera down to look across the plane: look at the minimap.

**Sounds**
- **The engine hum is 6 dB quieter:** half the amplitude, for the own ship, other players, aliens and company pilots, at idle, cruise and full speed alike. Nothing else changed: lasers, hits, explosions, the interface and the music are as before. If it is still too loud, say so.
- **The music starts at your volume on the login screen too.** The engine's volume buses used to start at full and reach your level a moment after the first sound; they start at your level now, and the screens before sign-in play the volume the last pilot on this computer had (15 percent on a new one). An account that saved a music volume of 40 before 0.4.4 still plays 40 after it signs in.
- **Toolbar buttons click softly.** The buttons of both toolbars, the lights that close a window, the buttons in window headers, the hotbar's picker chips, the chat's tabs and the fold rows now make the kit's soft click, and a tick as the pointer settles on a button. The tick never played for any button before, because of a counter it relied on that stood still; it plays now, on the kit's own buttons too. Settings › Button Sounds switches them off.

**The pilot sheet keeps one width**
- The sheet that opens when you click a pilot (Rankings, the Hall of Fame, the clan roster) grew wider with every item and module the pilot carried. It is now one width (at most 720 points) whatever the pilot carries: the name and a line of totals stay on top, and the equipment scrolls under them in groups (Lasers, Generators, Ability slots, Extras, Drones), one tile per item, with the modules it carries as a "+n" badge. Stat tiles shrink their text before cutting it, on every page.

**Windows: dragging the window and copy and paste**
- **The picture keeps moving while you drag or resize the window** by its title bar. Windows stops the game's frames while it moves a window; the game now asks for frames from a second thread during the move. **We have not been able to run this on a real Windows PC.** The log (`spacecorps2027.log`) has a line per drag with its frames per second, and a line ending "the picture did not update" means it did not work on your PC. If it misbehaves, start the game with `SPACECORPS_NO_MOVE_FIX` set to `1` (or add `"move_fix": false` to `client.json`) to turn it off. The system menu (right-click on the title bar, Alt+Space) still freezes the picture while it is open.
- **Copy, Ctrl+C, Ctrl+X and Ctrl+V work.** The game never used the system clipboard: the Copy button next to your invite code said "Copied" for text only the game could read, and Ctrl+V pasted only what the game itself had copied. Now the Copy buttons (invite code, invite message, About's build line) and Ctrl+C, Ctrl+X and Ctrl+V in text fields use the system clipboard on **Windows, macOS and Linux** (Cmd on a Mac). The invite code is a selectable field. If the system refuses, a message says so. **The Windows part has never been through a real Windows PC and Linux only through stand-in tools;** on Linux the game needs `wl-copy`, `xclip` or `xsel` installed. Ctrl+C, Ctrl+X and Ctrl+V are no longer keys you can bind to a game action.

**Administrators**
- Administrators can **reset a pilot's forgotten password** (typed, or generated and shown once; the server keeps only the scrambled form), **set exact values** (credits, Thulium, Wipe Points, honor, experience, level) and **edit a pilot's inventory,** on the Admin page. **Every change an administrator makes to an account is recorded** (who, which pilot, what, the values before and after, when; never a password) and kept for a year. Records of the older admin buttons are kept too.

**Smaller changes**
- **Invite Friends:** the scrambled network address a redemption stores is **erased from our database 30 days after the redemption** (before, it was kept for good). Unused space inside the database file can still hold a stale copy until it is reused. The rest of the record stays.
- **The Season Store card** for the Shield Absorbance Boost says "points", not a percentage. The Boosters window shows the buff in points.
- **Texts and help:** the Master Drone's description says it has 2 slots; the wiki's Rockets page says a blast turns every alien it hurts; the help cards for Range, Shield absorbance, Clan donations and the Black hole are updated.
- **The wiki:** pages for the Ironclad, the new range rule, the new shields (Shields, Combat, Rockets, Lasers, Forge, Wipe Timeline) and the clan donation cap; the hull bars of the ship articles are drawn against 700,000 now.
- **Credits page:** the clan line names the donation cap.

## 0.4.5 · 2026-10-01

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.5)

SpaceCorps 2027 0.4.5 lets you choose where to come back when your ship is destroyed, adds a kill feed with funny lines to the Global chat, Invite Friends with a starter pack for new pilots, ways to hide the Global chat, ignore a pilot and report one, and Italian as the twelfth language. The server's refusals and notices are now translated too. Dying works differently, so the "If you already play" list below is worth reading.

### What's new

**Highlights**
- **Choose where to respawn:** the death screen offers your base (always open), the nearest portal (locked for 3 minutes after you use it) and the spot where you died (locked for 5 minutes). Press **1**, **2** or **3**. A portal or spot respawn protects you for 5 seconds, until your first shot.
- **A kill feed in the Global chat:** a short, funny line in your language whenever a pilot is destroyed. Switch it off in the chat window's menu.
- **Invite Friends** (Community): every pilot has a personal code. A friend with a new account (level 4 or lower) who uses it gets 100,000 credits, 5,000 Thulium, a N.I.K.E., a Quantum Laser 2, an Engine II and 1,000 Advanced Plasma. You collect 2,500 Thulium for each friend who reaches level 5, and more at 3, 5, 10 and 25 friends.
- **Chat safety:** hide the Global chat, ignore a pilot, or report one to the admins (right-click a name in the chat).
- **Italiano** is the twelfth language. A native speaker has not read it yet.
- **The server's refusals and notices are translated:** Assembly, Hangar, Skylab, Shop, clan, wipe and bonus code messages now show in your language.
- Also: the empty Epic rocket slot sends you to the Shop, the help cards and some texts are corrected, Settings, About and the sign-in card link to the privacy policy, and Settings says plainly what happens to a crash report you send.

**If you already play: what changes for you**
- **Your ship no longer respawns by itself.** After the explosion you stay on the death screen until you pick a place (**1** base, **2** portal, **3** spot) or dock with Return to Base, which is the base and spends nothing. No timer picks for you. A pilot who closes the game on the death screen meets "Your active ship is destroyed. Please revive it in the hangar first." at the next launch: revive the ship in the Hangar, which costs nothing and puts you at your base.
- **The nearest portal and the spot are locked after you use them,** for 3 and 5 minutes. The base never is. The locks stay through a logout and a server restart, and a new season clears them.
- **After a portal or spot respawn nobody can hurt you for 5 seconds.** Your first shot (a laser volley or a rocket) ends it, and aliens drop you as a target meanwhile.
- **The Global tab has kill feed lines now,** between the pilots' words. They never count as unread, and the switch is in the chat window's menu and in Settings › General › Chat.
- **The chat's right-click menu has Ignore and Report…** next to Invite to group. Ignoring a pilot hides its Global and Local lines and turns down its group invitations. It is not told, and it still hears you.
- **Some texts promise less.** The station's news line no longer promises a double-XP weekend, and the texts of the First Contact, Tech Surge and War Games phases no longer promise themed rewards or effects the game does not have. The welcome line in the chat no longer says "private Beta".
- **The Master Drone and the Helios Beam have new item texts** ("Advanced drone, upgraded from a Slave Drone." and "Ultimate laser weapon, upgraded from a Starfire-3."). Their stats are as before.
- **Pilot avatars are a little brighter,** so that the initials stay readable on every colour.

**Choose where to respawn**
- When your hull reaches 0 the ship is destroyed and the death screen, headed "Choose where to respawn", shows three rows: your base, the nearest portal and the spot where you died, in the order of the keys. Click one, or press its key. The keys work on the number row and the keypad, and only once the explosion is over (about 3 seconds), so a thumb on the hotbar's **1** does not pick a place.

  | Choice | Key | Where you appear | Locked after use |
  |---|---|---|---|
  | At base | **1** | your company's base, as before | never |
  | At the nearest portal | **2** | next to the portal of the map you died on that is nearest to where you died, 150 to 300 units from it | 3 minutes |
  | On the spot | **3** | where you died, on the same map and in the same world | 5 minutes |

- **The lock starts when you respawn that way,** not when you die. A locked row is greyed out with a countdown and opens by itself. If the server says a choice is still locked, the game tells you and reads the choices again. A refusal never uses up a lock.
- **A sector with no portal** greys the portal row out ("No portal in this sector."), and it never falls back to another map or to the base. If the server was updated while you were destroyed, or an admin moved you to another world, the place you died at is not known any more and only the base is offered.
- **Spawn protection:** a chip with the seconds left shows while it runs. During it, lasers, rockets and blasts do nothing to you, nobody can lock on to you and aliens drop you. It ends when you fire a laser volley or a rocket (the game tells you), or after 5 seconds. The base has no protection of its own: the station's safe zone has it.
- **The black hole:** in Danger Sector 4, a place within 4,200 units of the black hole's middle is moved out to 4,500 units on the same bearing, for the spot and for the portal. You are told ("You were moved out of the black hole's radiation.") and the lock is spent as for any respawn.
- Everything else about dying is as it was: no items lost, no cost, the ship comes back with its base hull and empty shields, and every ability is ready.
- The **Death** help card explains the choices, and a test checks its numbers against the server's file.

**The kill feed in the Global chat**
- Whenever a pilot's ship is destroyed, the **Global** tab gets a line with a skull: who died, who or what did it, and a joke about it. For example "vega asked the black hole for directions", "rex sent cyd a Lancet. It was not a gift." or "kai tried to hug a Gorvane". The names have their company's colour.
- **There are 62 lines in nine groups** (lasers 8, rockets 8, the N.U.K.E. 6, the N.I.K.E. 6, aliens 8, the black hole's horizon 8, its radiation 6, a pilot pushing someone into the hole 6, anything else 6). The server picks one at random and never the one it used last for that group.
- **The line is written in your language.** The server sends who died, who killed, the cause and a number, never the text, so a Japanese pilot reads the joke in Japanese. The jokes were adapted for each language and not translated word for word.
- **It tells nothing about where.** The line carries no map, position or world, so a cloaked pilot's death does not give the pilot away.
- **Only pilots' deaths are posted,** not aliens' or company pilots'. A pilot who logs out in a fight is not destroyed and posts nothing.
- **A mass death does not spam.** The server lets at most 4 lines a second into the channel, and the game folds a burst (more than 4 lines in 3 seconds) into one line, "N more pilots died", that grows in place.
- **Switch it off** with **Show kill feed** in the chat window's menu (the ⋮ button in its title bar) or in Settings › General › Chat. Turning it off only hides the lines, which come back when you turn it on. The game keeps the last 100 lines, and earlier deaths are not kept: you see what happens while you are online.

**Invite Friends**
- Open **Community › Invite Friends.** Your personal code looks like `XXXX-XXXX`: eight letters and digits, with no vowels and no 0, 1 or L, so it cannot spell a word or be misread. It is yours alone and never changes. You can copy the code, or a ready message with the download link and the code. The page lists your friends, the pack, the milestones and what you can collect now.
- **A friend who is new enters your code once** on the same page ("Have a code from a friend?"). The rules are: the friend's level is **4 or lower**, **once per account,** never your own code, and **at most 3 codes per network address in 24 hours.** The friend gets the pack, all at once:

  | Starter pack |
  |---|
  | 100,000 credits |
  | 5,000 Thulium |
  | 1 N.I.K.E. |
  | 1 Quantum Laser 2 |
  | 1 Engine II |
  | 1,000 Advanced Plasma (the x2 damage ammo) |

- **You get 2,500 Thulium for each friend who reaches level 5.** It waits on your page and you collect it yourself, once per friend. A badge on the Invite Friends row of the sidebar, and on Return to Base in flight, says that something is ready.
- **The milestones** count friends who reached level 5. Each step pays once, in any order:

  | Friends at level 5 | Thulium |
  |---|---|
  | 3 | 5,000 |
  | 5 | 10,000 |
  | 10 | 25,000 |
  | 25 | 75,000 |

- The numbers sit in a file on the server (`Invites.json`) and may change as we see how it goes. A reward you have collected stays collected.
- **What we keep.** Your page shows a friend's name and whether the friend has reached level 5, and the server sends nothing more about a friend (no level, email or address). It stores a code per pilot, who used which code and when, and a scrambled form of the network address, never the address itself. Deleting an account does not take back what the other pilot earned.
- **A season wipe does not touch codes or rewards,** and it does not reset levels either.

**Chat safety: hide Global, ignore, report**
- **Hide Global chat** is in the chat window's menu and in Settings › General › Chat. The Global tab then shows no lines (the kill feed's included) and counts no unread lines. The tab says "Global is hidden" with a button, **Show Global**. The lines you send there still go out, and the lines that arrived meanwhile are back when you show it.
- **Ignore:** right-click a pilot's name in the chat and choose **Ignore**. Its lines in **Global and Local** are hidden, and its group invitations are turned down at once, with no prompt. A pilot in your own group still shows in the **Group** tab. Nothing is mutual: the pilot is never told, and it still hears you.
- **The list** is in Settings › General › Chat, with a **Remove** button for each pilot. It holds up to 200 pilots, follows your account to your other computers, and a full list says so rather than dropping someone.
- **Report:** right-click a name and choose **Report…**. The sheet shows what is sent: your name, the pilot's, the channel, the last line of that pilot you could see (up to 200 characters) and the reason, which is Spam, Abuse or harassment, Cheating or Something else. You can send up to 5 reports an hour.
- **Nobody is punished automatically.** A report is a note for the admins, who read them on a new Chat reports card in the Admin page and decide what to do with the tools they already had. The pilot reported is not told who reported it. The server cannot check the quoted line, and the card says so.
- **Needs the 0.4.5 server for reports:** hiding and ignoring work on any server.

**Italian**
- **Italiano** is the twelfth language, after English, Deutsch, Español, Français, Magyar, 日本語, 한국어, Português (Brasil), Русский, Svenska and 简体中文. All 4,274 texts are in it, the kill feed's jokes and Invite Friends included. It is written with *tu*, the loan words Italian players use (slot, booster, respawn, clan) and the key names of an Italian keyboard (Invio, Canc, Maiusc).
- Pick it on the sign-in screen (the language button at the bottom right) or in Settings › General › Interface Language. Automatic picks it when your system is set to Italian.
- **It has not been read by a native speaker yet.** The same is true of the new texts in the ten other languages. Please tell us what reads wrong.

**The server's texts, translated**
- The refusals and notices the server sends now show in your language: the Assembly (a craft that cannot start, a piece that is fitted or missing), the Hangar, the Skylab, the Shop, the clan, the wipe and the bonus codes, plus the restart countdown. The messages that follow an action (the toasts after a click in those pages) are translated too. In 0.4.4 many of them came in English whatever you had picked.
- **A test keeps it that way:** the build fails if the server can send a text that has no translation in every language.

**Smaller changes**
- **The empty Epic rocket message is right:** when you run out of Harpoons, Piledrivers, Eclipses or Maelstroms and press their slot, the game tells you to buy more in the Shop (5 Thulium each), as a click on the slot does too. Only the N.U.K.E. and the N.I.K.E. say Assembly.
- **Help cards:** the Rockets card says groupmates are safe from your rockets as well as your company. The Ability slots card says new pilots start with a Repair Drone I and that a stack of Afterburners runs 15 to 20 seconds. The Death card describes the three choices. The chat's card has rows for the kill feed, hiding Global, ignoring a pilot and reporting one. Invite Friends has a card of its own.
- **The wiki:** a page for Invite Friends, sections on the kill feed, hiding, ignoring and reporting on the Groups page, a Wipe Timeline that says what a wipe really resets (items and ships, not level, credits, Thulium or ranking points), and the Rockets, Forge, Abilities and Black Hole pages corrected where they were out of date.
- **Privacy:** the sign-in card, Settings and About link to the privacy policy (https://spacecorps.github.io/play/privacy/). In Settings, the crash report switch says that a report you send becomes a public issue on GitHub (SpaceCorps/play) that anyone can read, without your name. Off, the reports stay on your computer.
- **About:** the build line wraps short of the Copy button in a narrow window.

## 0.4.4 · 2026-09-30

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.4)

SpaceCorps 2027 0.4.4 brings groups of up to five pilots from any company with three chat channels, a rework of the rockets with fixed damage, two craft-only rockets that make Dark Matter for the Forge's top tiers, abilities that stack, a Cloaking CPU without a timer, a stronger black hole, the Hangar in flight, twelve new modules and fullscreen on Windows. Terra's four sectors are a loop again, and Skylab upgrades from level 6 take longer and longer. Some setups change or get weaker, and this page says which.

### What's new

**Highlights**
- **Groups:** up to 5 pilots of any company see each other's ship, hull and shield, share the rewards of an alien kill and count for each other's kill missions. The chat has Global, Local and Group tabs, and the Group window opens on **B**.
- **Rockets, reworked:** every rocket does a fixed amount of damage (2,000 for a Lancet up to 7,500 for a Piledriver) and costs 500 or 800 credits, or 5 Thulium. Rockets without a lock fly toward your cursor, and a slot click arms one. Nothing caps what a rocket does to a pilot.
- **N.U.K.E., N.I.K.E. and Dark Matter:** two rockets that only Assembly makes. The N.U.K.E. is the biggest blast in the game. The N.I.K.E. hits a ship for 75,000, or makes Dark Matter if it falls into the black hole first. The Forge's steps to Rupturing and Eternal now need 2 Dark Matter Plates each.
- **Twelve new modules:** four laser amps, two shield cells, two thrusters, and an upgrade at the top of each family that keeps the Forge tier of the piece it uses up.
- **Abilities stack:** several shields, engines or Repair Drones in your ability slots add 50% each. The Shield Surge puts shield back over 10 seconds and Emergency Repair heals over 10 seconds. New pilots start with a Repair Drone I fitted.
- **The Cloaking CPU has no timer.** Other companies see a red dot on the minimap, an EMP within 1,500 units ends your cloak, and any end costs a minute of recharge.
- **The black hole** pulls harder and carries a ship that stops, can be seen from anywhere in Danger Sector 4, and has debris that spirals in.
- **The Hangar works in flight,** inside a safe zone's ring: fit items, swap configuration or fly another of your ships.
- **Jumping takes 3 seconds** and picking up a cargo box 1. In a Danger Sector you can't jump while under attack.
- **Skylab upgrades take days at the top:** from level 6 each takes 1.6 times as long as the one before, up to 6 days for the last step.
- **Terra is a loop again.** The 0.4.3 diamond is taken back: `T-1` has one portal.
- **Fullscreen on Windows** (button, F11, Alt+Enter). It is new and nobody has run it on a real Windows PC yet.
- Also: the Helios Beam is made from a Starfire-3, a Slave Drone becomes a Master Drone in place, a Resources page in the wiki, aliens let go of a pilot they have not shot at, Chrono-Gate scans cost a tenth, Shift no longer stops the flight keys, and alt-tab no longer leaves the game behind the server.

**If you already play: what changes for you**
- **Rocket prices change for everyone.** Common rockets cost 500 credits (the Lancet was 100, the Rivet and Scatter 60), Rare ones 800, and the four Epic ones (Harpoon, Piledriver, Eclipse, Maelstrom) cost 5 Thulium instead of credits. Rockets you own stay yours, and nobody is refunded.
- **A rocket no longer depends on your ship.** It does its own fixed damage, so a rocket from a weak ship hits harder than before and one from a strong ship may hit softer.
- **Rockets have no cap on pilots any more.** A N.I.K.E. destroys a fresh Protos, Kitefin or Ostirion in one hit (an Ostirion with Light Shield Cores). Safe zones, the Peace Protocol, sectors without PvP, your company and your group still protect you.
- **Rockets without a lock** (Rivet, Mallet, Piledriver, Scatter, Barrage, Maelstrom) fly toward your cursor, whatever you have selected. A click on their slot arms them and your next click in space fires.
- **The Forge's steps to Rupturing and Eternal need 2 Dark Matter Plates each,** on top of what they took. Only N.I.K.E.s fired into the black hole make Dark Matter, so until you have plates a Godly item stays Godly. Gear that is already Rupturing or Eternal keeps its tier.
- **The Shield Surge no longer gives an overshield.** It puts back 30, 60 or 100% of your maximum shield over 10 seconds. **Emergency Repair heals over 10 seconds** instead of at once. You can fit several modules of a kind in your ability slots. Pilots who already play are not given a starter Repair Drone.
- **The Cloaking CPU no longer runs out,** and the recharge after any end is 60 seconds instead of 20. Other companies see where you are as a red dot. **An EMP now ends every cloak within 1,500 units of it,** your own company's too.
- **Jumps and cargo take time.** A jump takes 3 seconds and a cargo box 1. **Return to Base is still an instant exit,** also in a Danger Sector fight.
- **Skylab upgrades from level 6 take longer,** up to 6 days at the top. Upgrades already running keep the time they were given. **Upgrading Solar switches off every farm and collector until it is done,** as it always did, but now that can be days. The upgrade sheet warns you.
- **The Helios Beam needs a Starfire-3** and uses it up. Crafts you already started keep what you paid.
- **Crafting a Master Drone** upgrades one of your Slave Drones in place, and its level and experience start again at 0. Nothing lands in your inventory.
- **Terra's sectors are a loop again.** The `T-1` to `T-3` portal of 0.4.3 is gone.
- **The black hole** carries a ship that stops. Slow ships have their point of no return farther out: a stock Protos at about 1,630 units instead of about 1,190.
- **Aliens** you have not shot at lose interest at 1,200 units. Aliens you did shoot follow you a little farther than before (2,500 units).
- **The Hangar's equip, unequip, delete and revive routes answer 409 outside a safe zone's ring** while you fly. Tools and scripts that changed equipment in flight from anywhere now get a refusal.
- **Chrono-Gate scans cost 5,000 credits and 5 Thulium,** a tenth of before. The chances are the same.
- **Music starts at volume 15.** Settings you saved keep their value.
- **The chat has a Global tab now.** What you type goes to the tab in view, and Global reaches every pilot online, so look at which tab is open before you type.

**Groups and chat channels**
- A **group** is up to 5 pilots of **any company**. Friends who fly for different companies can be one group, even enemies in the PvP sectors. Members see each other's ship, hull and shield, how far away they are and where, and members who are cloaked too. The Group window opens on **B** (rebind it in Settings › Controls) or from its button in the toolbar.
- **Invite** a pilot by selecting them and pressing **Invite to group** in the target panel, by right-clicking their name in the chat, or with **+** in the Group window. The pilot gets a card with **Accept** (Y) and **Deny** (Escape) and 60 seconds to answer. You can't invite a pilot who is in a group, who has **Do Not Disturb** on (the bell in the Group window, or Settings › General › Groups) or who has too many invitations waiting. You can send 10 invitations a minute, and 3 of them to other companies.
- An invitation from **another company** names the company, is marked **Enemy** and warns what accepting means, so nobody joins by mistake: its members see your ship, hull, shield and the map you are on, even when you are cloaked, and you can't attack each other. A pilot of another company who leaves your group can't be invited by you again for a minute.
- The first invitation that is accepted makes its sender the **leader**. The leader invites, removes members and hands the lead on. Anyone can leave, a group of one ends by itself, and when the leader leaves the member who has been in longest leads. You can be in one group at a time. If your connection drops or you dock, your place is kept for 2 minutes.
- **Members can't hurt each other.** You can't lock on to a groupmate with a laser or a guided rocket, your shots and blasts pass through them, and nothing you do to one counts as a kill for anyone. That holds for company mates in one group too. Company mates who are not in the same group are as before: destroying one costs 100 honor. An EMP doesn't break the cloak of its owner's groupmates. When you leave or are removed, a former mate is fair game again at once.
- **A kill's rewards are shared.** When a member destroys an alien, its credits, Thulium, experience and honor are split by level among the members who are on the same map, alive, within 4,000 units of the wreck and **fired a laser or a rocket in the last 15 seconds**. The one who made the kill always has a share and gets what rounding leaves. The cargo crate, the kill in the statistics and the ranking, and the drones' experience stay with the killer. Kills of pilots are not shared.
- **Missions count for the group.** A kill also counts for the kill missions of every member on the same map who fired in the last 15 seconds, wherever they are on it. The mission's own rules still decide what counts.
- The chat has three tabs: **Global** (every pilot online, in every world), **Local** (your map) and **Group** (your group, wherever it is). Each has its colour, a tab counts the lines you have not read, and the line you type goes to the tab in view. You can also start a line with `/g`, `/l` or `/p`. Global allows 3 lines in a burst and then one every 2 seconds.
- **Groups live in the server's memory,** so every server update ends them: invite each other again. A new season ends them too.

**Rockets: fixed damage, new prices**
- A rocket now has **its own damage, a fixed number of points.** It is the same whoever fires it: your ship, lasers, amps, boosters, ammo and drones change nothing, and a rocket never crits. A single-target rocket deals its damage to the ship it hits. A blast deals it to every ship inside, the whole number at the centre and 25 to 35% at the edge. The timer is still 5 seconds for all rockets together.

  | Rocket | Kind | Damage | Skips the shield | Blast radius | Price | Carry at most |
  |---|---|---|---|---|---|---|
  | Lancet | guided, one ship | 2,000 | 15% | | 500 credits | 500 |
  | Javelin | guided, one ship | 4,000 | 30% | | 800 credits | 200 |
  | Harpoon | guided, one ship | 6,000 | 50% | | 5 Thulium | 50 |
  | Rivet | straight, one ship | 2,500 | 10% | | 500 credits | 500 |
  | Mallet | straight, one ship | 5,000 | 30% | | 800 credits | 200 |
  | Piledriver | straight, one ship | 7,500 | 50% | | 5 Thulium | 50 |
  | Ember | guided, blast | 1,400 | | 170 | 500 credits | 500 |
  | Corona | guided, blast | 2,800 | | 230 | 800 credits | 200 |
  | Eclipse | guided, blast | 4,200 | | 300 | 5 Thulium | 50 |
  | Scatter | straight, blast | 1,750 | | 210 | 500 credits | 500 |
  | Barrage | straight, blast | 3,500 | | 290 | 800 credits | 200 |
  | Maelstrom | straight, blast | 5,250 | | 400 | 5 Thulium | 50 |

- A straight rocket does 25% more than the guided rocket of its tier for the same price, because you have to aim it. A blast does 70% of the single-target rocket of its tier, to every ship it covers.
- **Nothing caps a hit on a pilot.** In 0.4.3 one rocket took at most a quarter of another pilot's hull. Now a rocket hits a pilot like any hit: the shield takes its share (less what the rocket skips) and the rest goes to the hull. By our model two Piledrivers or three Harpoons destroy a fresh Protos, five to seven rockets a Kitefin, and ten to thirteen an Ostirion. The rest of the rules are as in 0.4.3: no rocket hurts a ship in a safe zone, before the Peace Protocol ends, in a sector where pilots may not fight, or in your own company or group, and you need a laser fitted to fire one.
- **Rockets without a lock always fly toward your cursor,** at the point under it in the flight view, even with a target selected. **Click the slot of a Rivet, Mallet, Piledriver, Scatter, Barrage or Maelstrom to arm it.** The slot gets a white frame, the cursor becomes a crosshair, and your next click in space fires the rocket toward that click without moving your ship. Escape, a right click, the same slot again, another slot, a jump, a death, or opening Settings or the Galaxy map lets go of it. If the timer is still running the click only tells you so and the rocket stays armed. The number keys and **R** fire at once toward the cursor. Guided rockets still lock the target you selected.
- The Shop, the Hangar, the Transport Cache and the Rockets picker list the rockets one kind at a time (guided single target, straight single target, guided blast, straight blast), cheapest tier first.
- The five missions you start with now give rockets to try: Basic Training: Combat 50 Lancets, Speed Trial 50 Rivets, Combined Operations 30 Embers, Frontier Defense 30 Scatters and Phantasm Hunter 20 Javelins. Only pilots who finish them from now on get them.

**The N.U.K.E., the N.I.K.E. and Dark Matter**
- Two rockets are not in the Shop. **Assembly makes them** and they follow every rule above. Both fly toward your cursor.

  | Rocket | Damage | Reach | Carry at most | Assembly |
  |---|---|---|---|---|
  | N.U.K.E. | 50,000 at the centre of a 900-unit blast, 12,500 at its edge | flies 1,200 units, 4 seconds | 10 | one: 150,000 credits, 3,000 Thulium, 6 Maelstrom, 4 Power Cores, 10 Reinforced Hull Plates, 40 Ship Fragments, 80 Cataclysite (900 s) |
  | N.I.K.E. | 75,000 to one ship, half of it skipping the shield | flies 4,050 units, 4.5 seconds | 20 | five: 100,000 credits, 1,500 Thulium, 20 Ship Fragments, 4 Reinforced Hull Plates, 40 Cataclysite (300 s) |

- The **N.U.K.E.** is the biggest blast in the game, more than twice the reach of the Maelstrom. It wipes out every Seeker and Phantasm in its blast. Against pilots it destroys a fresh Protos within about 560 units of the burst (160 with Heavy Shield Cores) and no bigger ship in one blast. It bursts with a white flash, a ring showing its reach, a mushroom cloud and a shake of the camera (a short dim flash and no shake with Reduce Motion).
- The **N.I.K.E.** hits the first ship it touches and is spent on it. A fresh Protos, Kitefin or Ostirion is destroyed in one hit (an Ostirion with Light Shield Cores only). It takes about a third of a Paragon's hull and about a seventh of a Wraith's. It flies through your own company and group, ships in a safe zone and ships you may not hurt yet.
- **The N.I.K.E. also feeds the black hole.** Fired from within about 4,380 units of the middle of Danger Sector 4, a N.I.K.E. that crosses the event horizon before it touches a ship is swallowed, and the hole gives back **Dark Matter** for it. If a ship is in the way, it is hit for 75,000 and you get no Dark Matter. Aliens and company pilots keep out of the hole's ring, so only pilots who went in for Dark Matter, or who wait for you at the rim, can be in the way. If you leave the map after firing, the N.I.K.E. flies on, hurts nobody and still makes your Dark Matter.
- **Dark Matter** lies in small crates on the rim of the hole's zone, 3,050 to 3,950 units from its centre, about two Dark Matter per N.I.K.E. (one to three, a crate holds up to two). The crates are yours and your clan's for 60 seconds, then anyone's, and they are gone after 240 seconds. A map holds at most 32. They look like violet-black orbs that come out of the hole, show the seconds you still have them to yourself and have a violet mark on the minimap.
- **Assembly presses a Dark Matter Plate** from 5 Dark Matter, 1 Velkonite Reinforced Plate, 1 Orvium Reinforced Plate and 250 Thulium (120 s).
- **The Forge's steps to Rupturing and Eternal take 2 Dark Matter Plates each.** The steps to Tainted and Godly are as before. A failed step gives half of the materials and half of the Thulium back (of the 2 plates, 1).

  | Step | Success | Credits | Materials |
  |---|---|---|---|
  | Rupturing | 75% | 200,000 | 20 Reinforced Hull Plates, 120 Cataclysite, 2 Dark Matter Plates |
  | Eternal | 60% | 500,000 and 2,000 Thulium | 8 Power Cores, 240 Quorvium, 2 Dark Matter Plates |

- Two plates are 10 Dark Matter, about 5 N.I.K.E.s. Counting failed steps, a successful step costs about 6 to 7 N.I.K.E.s, and each N.I.K.E. costs 20,000 credits and 300 Thulium in Assembly fees, besides its materials. As a weapon a N.I.K.E. is the worst value in the game and the best single hit.

**Twelve new modules**
- Laser amps, shield cells and thrusters are the modules you fit into lasers, shield cores and engines. Each family now has a credit rung, a Thulium rung and an upgrade.

  | Family | Credits | Thulium | Upgrade (Assembly) |
  |---|---|---|---|
  | Damage amps | **Arc Amp** 60,000: +16 damage, +5% crit | **Pulse Amp** 1,500: +26, +6% | **Nova Amp**: +38 damage, +7% crit |
  | Crit amps | **Focus Amp** 60,000: +20% crit, +14 crit damage | **Prism Amp** 1,500: +25%, +24 | **Apex Amp**: +25% crit, +44 crit damage |
  | Shield cells | **Reinforced Shield Cell** 90,000: +4,200 capacity, +350 recharge, +5% absorbance | **Prime Shield Cell** 8,000: +8,500, +700, +7% | **Sovereign Shield Cell**: +12,000, +1,000, +8% |
  | Thrusters | **Vector Thruster** 80,000: +7 speed, x1.02 | **Ion Thruster** 3,000: +13, x1.08 | **Plasma Thruster**: +18, x1.12 |

- **The upgrades are made in Assembly** from the Thulium piece below them. You can't buy them.
  - **Nova Amp:** 1 Pulse Amp, 30 Cataclysite, 1 Power Core, 3 Velkonite Reinforced Plates and 1,200 Thulium (60 s).
  - **Apex Amp:** 1 Prism Amp, 30 Cataclysite, 1 Power Core, 3 Velkonite Reinforced Plates and 1,200 Thulium (60 s).
  - **Sovereign Shield Cell:** 1 Prime Shield Cell, 20 Cataclysite, 8 Reinforced Hull Plates, 6 Velkonite Reinforced Plates and 2,500 Thulium (90 s).
  - **Plasma Thruster:** 1 Ion Thruster, 60 Ship Fragments, 3 Power Cores, 6 Velkonite Reinforced Plates and 2,000 Thulium (90 s).
- **An upgrade keeps the Forge tier of the piece it uses up and rolls its buffs again.** A Godly Pulse Amp makes a Godly Nova Amp with new buffs. A Standard piece makes a Standard one. The Velkonite Reinforced Plates come from your Skylab Forgery.
- When you hold copies of the piece in several tiers, the recipe card shows them so you can choose which one is used, and asks first before it uses one above Standard. A piece that is fitted on a ship or holds other modules can't be used, and the card tells you what to take out.
- The Heavy Shield Core, Engine III, Thruster III and Adaptive Core III still have no price and no recipe.

**Abilities that stack**
- An ability slot may now hold **several modules of one kind.** All the shield cores, engines or Repair Drones in one configuration's ability slots are one ability. **The worst-ranked one sets the strength and the cooldown, and every other module adds 50% of that base** (two modules make 1.5 times, three make 2 times).

  | Ability | What a stack changes | What it keeps |
  |---|---|---|
  | Afterburner (engines) | lasts 10 seconds plus 5 for each extra engine: two engines 15 s, three 20 s | the speed bonus and the cooldown |
  | Shield Surge (shield cores) | puts back 100% plus 50% per extra core of its total | the 10 seconds and the cooldown |
  | Emergency Repair (Repair Drones) | heals 100% plus 50% per extra drone of its total | the 10 seconds and the cooldown |

- A module takes the slot of another ability, so a ship trades breadth for depth. The hulls have 1 ability slot (Protos, Kitefin), 2 (Ostirion) or 3 (Paragon, Wraith). A Protos or Kitefin can't stack. A better module beside a worse one buys the bonus and never a better base: a Light core beside a Basic one restores 45% of your shield (30% plus half of it), less than the Basic core alone (60%).
- **The Shield Surge puts shield back** instead of giving an overshield. Over 10 seconds it restores 30%, 60% or 100% of your maximum shield (Light, Basic, Heavy core), evenly, and never less than the core's own capacity (10,000, 15,000, 25,000). Hits don't stop it, the shield never goes above its maximum, and what it restored stays when it ends. It is still refused inside a safe zone, and now also on a ship with no shield. **A Surge pressed on a full shield starts the cooldown and restores nothing.**
- **Emergency Repair heals over 10 seconds** what it used to heal at once: 20%, 25%, 32% or 40% of your maximum hull. Hits don't interrupt it, and it is still refused at full hull. The cooldowns are as before (120, 105, 90 and 75 seconds).
- The black hole's radiation doesn't stop a running Surge or repair.
- **New pilots start with a Repair Drone I fitted** in the first ability slot of their Protos, so the Emergency Repair button (E) works from the first minute. Pilots who already play get nothing extra.
- The Surge keeps its bubble, and your shield bar (and a target's) fills while it runs. The Hangar shows a stack as "x2" or "x3" with the real numbers, and Emergency Repair glows, sends out motes and shows "+N" a second while it heals.

**Cloaking CPU and EMP Charge**
- **A cloak has no timer.** It lasts until you press the CPU again, fire a laser or launch a rocket, enter a safe zone, an area blast hits you, an EMP goes off within 1,500 units of you, or you jump, die or log out. The chip at the top says "Cloaked" and the uses you have left, without seconds, and the slot glows "ON". Collecting cargo still doesn't end it.
- **The recharge is one minute, however the cloak ends** (it was 20 seconds). It stays with you when you log out, die or jump, and a server restart clears it. If you press too early the slot flashes red. You still can't cloak inside a safe zone or within 10 seconds of a hit or a shot, and one press is still one use.
- **Other pilots see a red dot** at your position on their minimap, from anywhere on the map, refreshed twice a second. The dot has no name, ship or company, can't be clicked or targeted and can't be locked. Your own company still sees you as a pale ghost, and so does your group. A new (i) on the minimap explains the dot. Aliens don't see you, as before.
- **An EMP ends cloaks.** Every cloaked ship within **1,500 units** of the EMP's owner is revealed, pilots of other companies and **your own company's too**, except the owner's groupmates. A pilot whose cloak breaks is told "Cloak broken: an EMP went off nearby" and starts the minute of recharge. The ring of the EMP is drawn out to its full reach. The EMP is otherwise as before: 3 seconds without locks, every lock on you breaks, a 30 second recharge, 500 Thulium a charge.
- A pilot who saw you cloak can follow your dot as it moves, since the dot is still a position. We left that as it is.

**The black hole: pull, sight and debris**
- **The pull moves you.** A ship that stops anywhere inside 3,000 units of the middle is carried toward it: 25 units a second at 2,800 units from the middle, 60 at 2,300, 120 at 1,800 and 220 at 1,300. In 0.4.3 a ship could hold still wherever the pull was weaker than its speed. The last 900 units are as before, and the radiation (4,000) and the event horizon (300) are unchanged.
- **Slow ships pass their point of no return farther out.** Ships faster than about 272 units a second keep theirs.

  | Ship or speed | Point of no return in 0.4.3 | Now |
  |---|---|---|
  | slowest possible ship (124) | 1,299 | 1,781 |
  | stock Protos (155) | 1,185 | 1,627 |
  | stock Kitefin (184) | 1,100 | 1,480 |
  | stock Ostirion (208) | 1,044 | 1,362 |
  | stock Paragon (222) | 1,014 | 1,287 |
  | stock Wraith (238) | 982 | 1,171 |
  | Protos with Afterburner III (247) | 966 | 1,105 |
  | runner Protos (265) | 936 | 976 |
  | anything over about 272 | unchanged | unchanged |

- **You can see it from anywhere in Danger Sector 4.** A small black hole in a glow on the edge of your screen points to it and shows the distance, and it grows into the real picture as you get close. The stars of the inflow fall at the pull's own speed, and your engine flame and wake follow the current.
- **Debris** (real rocks and hull fragments) circles the hole and falls in along spirals, faster and tumbling quicker the closer it gets, glowing orange in the disk's light and torn apart before the horizon.
- The Star System map marks the hole in the middle of `DS-4`.

**Jumping and cargo take time**
- **A jump takes 3 seconds,** picking up a **cargo box takes 1.** Your ship keeps flying. A bar over the hotbar fills, and it turns red with the reason if the server calls it off. Everyone can see a portal charge while a pilot jumps, and a crate being scanned while a pilot collects it.
- The jump needs a portal within 500 units the whole time, and is cancelled if you leave that range. The pick-up needs the box within 200 units.
- **Outside the Danger Sectors an attack doesn't interrupt a jump.** In a Danger Sector (`DS-1` to `DS-4`) **you can't start a jump if you were hit in the last 10 seconds, and a hit while you jump cancels it.** The black hole's radiation is not an attack.
- **Return to Base is not covered.** It is still an instant exit, also from a Danger Sector fight. We left it that way on purpose.

**The Hangar in flight**
- Open the **Hangar** window (the warehouse button in the top-left toolbar) inside the ring of a safe zone (a station or a portal) and you can fit and unfit items in any slot, swap configuration and **make another ship of yours active, without returning to base.** A ship you switch to keeps the hull and shields it had, so changing ship never repairs. Cooldowns, ammo, rockets, experience and your Slave Drones stay with you.
- It opens only when the ship is alive and protected by the ring, not cloaked or inside its own EMP window, and **quiet for 10 seconds:** no hit taken, no shot or rocket fired and no rocket of yours still in the air. Everywhere else the window opens read-only and says why.
- The server refuses too: equip, unequip, delete, revive and making a ship active answer **409** ("You can only change your ship in a safe zone.") while you fly outside a ring. The configuration swap (C) still works anywhere, every 5 seconds.
- In the Hangar's inventory every category is now its own on/off switch, so you can hide ammo and Repair Drones while you manage lasers, shields and engines. It remembers your choice. Double-clicking the only category that is on brings all of them back.

**Skylab: upgrades that take days**
- Getting a module from level 1 to level 6 takes what it did. **From level 6 to 7 it takes 20 minutes, and every step after that about 1.6 times as long as the one before,** the same for all eight modules: 20 minutes, 30 minutes, 50 minutes, 1 h 20 min, 2 h 15 min, 3 h 30 min, 5 h 30 min, 9 h and 14 h, then **1 day from level 15 to 16,** 1 d 12 h, 2 d 12 h, 4 d and **6 days for the last step, 19 to 20.**
- No module goes above the Core, so the Core sets the pace. Bringing the Core from level 1 to 20 takes about 16 and a half days, and the whole station about 22 and a half. The costs are as before, and there is no way to hurry an upgrade.
- **Upgrades already running keep the time they were given,** and a module that was upgrading when the server updated finishes when it would have.
- **Solar is the module to plan around.** A module being upgraded is offline, and Solar is the only one that makes power, so **a Solar upgrade switches every farm and collector off for its whole length** and the production lost is never made up. The upgrade sheet, the module sheet and the preview of Solar's Upgrade button warn you before you click. The build sheet says the station has no power meanwhile.
- The Skylab wiki page has the station at every level from 1 to 20 as pictures, the cards of all eight modules and the table of times. The wiki can show pictures now.

**Assembly: the Helios Beam and the Master Drone**
- **The Helios Beam is made from a Starfire-3:** 1 Starfire-3, 50 Cataclysite, 2 Power Cores, 18 Orvium Reinforced Plates, 4 Reinforced Hull Plates and 2,000 Thulium (180 s). It was 5,000 Thulium, 20 Orvium plates and 5 hull plates with no Starfire-3 (300 s). The Starfire-3 and the Helios Beam together cost as much Thulium as the Helios Beam alone did, and the Starfire-3 adds its own 25 Ship Fragments, 10 Velkonite Reinforced Plates, 1 Reinforced Hull Plate and 100,000 credits.
- Like the module upgrades, it **keeps the Forge tier of the Starfire-3 and rolls its buffs again.** The Assembly tells you when the piece an upgrade needs is missing, fitted on a ship, holding amps or in the Transport Cache, and what to do: take your Starfire-3 off its ship and its amps out before you upgrade it. A Helios Beam you queued before the update is collected as you paid for it.
- **A Slave Drone becomes a Master Drone in place.** In Assembly you pick which drone (the one with the least experience is pre-selected). It keeps its number, slot and fittings, nothing goes into your inventory and there is nothing to collect. **Its level and experience start again at 0** when the 60 second upgrade finishes: the Assembly warns you and asks you to confirm when the drone has experience. The price is as before, 100 Ship Fragments and 40,000 Thulium. While it is queued the drone's slot is offline. The Master Drone flies as a gold gunship.
- Master Drones crafted in 0.4.3 stay as they are: loose items that do nothing. The number of drones, their prices and the limit of eight are unchanged.

**Terra is a loop again**
- **This corrects the 0.4.3 notes,** which said Terra's four sectors form a diamond and that `T-3` is one gate from Terra's home. The diamond showed two portals in `T-1` while Mars and Galactic have one, and we took it back.
- Every company has the same loop now. The base `x-1` has **one portal, to `x-2`.** `x-2` opens on `x-3` and `x-4`, and `x-3` and `x-4` are linked. Terra's `T-4` still opens on `DS-2`. `T-3` is two gates from home again.
- The server moves the live gates back when it starts: `T-1` to `T-3` goes and `T-2` to `T-3` returns. Your position stays where it was. If you stood next to the old `T-1` to `T-3` portal, it is gone.
- The Star System map draws one dot for each portal and one line for each pair of sectors, and tells you which sector a portal leads to when you point at its dot.

**Aliens let go**
- An alien you have **not** shot gives up the chase when you are more than **1,200 units** away, or when it has flown **2,000 units** from where the chase began. An alien you **did** shoot (in the last minute) holds on to 2,500 units and flies at most 3,000. Before, the only limit was a gap of 2,000 units, which a ship as fast as the alien never reached.
- An alien that lets go roams from where it is, ignores you for 8 seconds unless you shoot it again, and near a gate or a safe zone heads away from it instead of waiting there. A pack no longer follows you across the map to the gate.
- The trade-off: a pilot who shoots an alien and then outruns it is followed about 500 units farther than in 0.4.3. An alien that gives up because you reached a safe zone also ignores you for 8 seconds after you leave it.

**Fullscreen on Windows, and a log file**
- **Fullscreen is new on Windows.** The button at the top right, **F11** and **Alt+Enter** switch the game to a borderless window that covers the whole screen, taskbar included. Alt+Enter waits while you type in the chat. Settings › Controls lists both keys under "Fixed keys", and an action of yours bound to F11 or Alt+Enter is shown in red as sharing a key. On macOS the button works as before, and Linux has no fullscreen yet.
- **It has never been run on a real Windows PC.** We wrote it and built it on a Mac. If it misbehaves, press F11 again to leave it. **To turn it off completely,** start the game with the environment variable `SPACECORPS_NO_FULLSCREEN` set to `1`, or add `"fullscreen": false` to the file `.spacecorps2027\client.json` in your user folder.
- **The game keeps a log file,** `.spacecorps2027\spacecorps2027.log` in your user folder (`~/.spacecorps2027/spacecorps2027.log` on macOS and Linux), so you can send it to us when something misbehaves. It holds warnings, errors, the fullscreen steps and one line with your version and system. The game writes no account data to it, and passwords, tokens and your home folder's name are cut out before a line is written as a second lock (the cutting has known gaps for formats the game doesn't write today). It is 1 MB at most, and the older half is `spacecorps2027.log.1`.

**Keys, chat and alt-tab**
- **Shift no longer stops the flight keys.** J (jump), A (attack), C, R, Q, W and E work while you hold Shift, unless you bound Shift plus that key to something else (then that binding wins). Ctrl or Alt held still blocks them, and the number keys keep their Shift row.
- **The chat and the ability keys could go dead together.** A Shift, Ctrl or Alt the system never told the game you had let go of stayed "held", so Enter wouldn't open the chat, Escape wouldn't leave it and Q, W and E did nothing. The game now checks those keys against the system, lets go of them when you come back to its window, lets Escape always get you out of the chat, and Enter brings the chat in front of a window covering it. We never reproduced the exact cause, so these are fail-safes (see Known issues).
- **Alt-tab no longer leaves the game behind.** When the game stopped drawing for a few seconds (alt-tab, minimising, a stall), your ship and the ones around you were drawn 0.7 to 1.1 seconds behind the server and stayed there until you changed map. Now the game catches up within a tenth of a second.

**Smaller changes**
- **The wiki has a Resources page:** every material and currency, where to get each one, what it is for and the best way to farm it, with the figures for Alpha (Beta pays 2 times, Gamma 3 times). It explains which plates the crafts and upgrades need. The wiki also has a Groups page, and its Rockets, Forge, Abilities, Black Hole, Skylab, Hangar, Drones and Extras pages follow the new rules.
- **Chrono-Gate scans** (the Energy Materializer's scans for Chrono-Gate parts) cost 5,000 credits (1% chance of a part) or 5 Thulium (10%). They cost 50,000 and 50 before, and the chances are the same.
- **Music** starts at volume 15, where it was 40. A volume you saved keeps its value.

## 0.4.3 · 2026-09-30

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.3)

SpaceCorps 2027 0.4.3 brings rockets, three active abilities, the Cloaking CPU and the EMP, the Forge, four Skylab modules that make the plates for your best lasers, a black hole in the middle of the PvP sectors and Slave Drones that level up. The PvP sectors are now the Danger Sectors, repeated kills of the same pilot pay less, and flying, planets, the Shop and the Siphon Battery look and feel better. Some setups change or get weaker, and this page says which.

### What's new

**Highlights**
- **Rockets:** twelve rockets in four kinds, bought for credits (60 to 900 each) and fired on one 5 second timer. Press R or a slot's key.
- **Abilities:** a shield, an engine or a Repair Drone in an ability slot gives you Shield Surge (Q), Afterburner (W) or Emergency Repair (E).
- **Cloaking CPU and EMP Charge:** disappear from other companies for up to 30 seconds, or break every lock on you for 3.
- **The Forge** replaces the Fusion Chamber: raise gear one tier at a time, or merge two copies into one.
- **Skylab supply chain:** two collectors, a storage and a Forgery make the plates that the Quantum Laser 3, Starfire-3 and Helios Beam are now made from.
- **Danger Sectors:** the PvP sectors are DS-1 to DS-4, with a black hole in the middle of DS-4, and Terra's four sectors form a diamond.
- **Drones level up** through 8 levels, stay through the season wipe and now cost by a price table.
- Repeated kills of the same pilot pay less, and the Ostirion and Kitefin now count their proper PvP points.
- Smoother flight, solid planets, one order for the Shop and your inventory, the Siphon Battery's stolen shield flowing back to you, and bonus codes in Admin.

**If you already play: what changes for you**
- **Ability slots** take a shield, an engine or a Repair Drone now. Shield Cells and Thrusters that sat in them are back in your inventory, and a notice tells you the first time you fly.
- **The Fusion Chamber is gone.** The Forge takes its place. Your gear keeps the buffs it has, and a tier-up can fail.
- **The Shield Absorbance Boost** (the Season Store buff that was called Shield Absorption) raises your absorbance now. It no longer speeds up shield recharge: pilots who bought it lose that recharge bonus, up to 10%. Your levels stay.
- **Quantum Laser 3** is no longer sold in the Shop. It is made in Assembly from Skylab plates, as are the Starfire-3 and the Helios Beam. If you own one, you keep it. Nobody is refunded.
- **Slave Drone prices** follow a table (the first is 100,000 credits, and every later one costs less than before), and **your drones are kept at the wipe** with their levels. Every veteran will end up with eight level-8 drones: +7% on the base damage of the lasers in the drone slots for everyone who plays long enough.
- **PvP:** destroying the same pilot again pays less and less. Pilots' PvP points are recounted when the server updates (nobody loses any). The sectors `4-1` to `4-4` are called `DS-1` to `DS-4`.
- The black hole in `DS-4` kills a ship that flies too close.

**Rockets**
- Rockets are a second weapon beside your lasers: one shot every few seconds that hits harder than a volley. There are twelve, in four kinds and three prices each (cheap, middle, dear):
  - **Guided** rockets lock the target you selected and steer after it. Hit one ship: Lancet, Javelin, Harpoon. Burst and hurt everything near the blast: Ember, Corona, Eclipse.
  - **Straight** rockets fly where you aim. Hit one ship: Rivet, Mallet, Piledriver. Burst: Scatter, Barrage, Maelstrom.
- The prices are 60 to 900 credits a rocket. The cheap ones carry up to 500, the middle ones 200 and the dear ones 50. The dearer a rocket, the harder it hits, the farther it reaches and the more of a shield it skips (guided and straight single-target rockets skip 10% to 50% of the shield; blasts skip none).
- A rocket does a multiple of your own laser volley (0.6 to 3.6 times), so a stronger ship hits harder and the rocket keeps up when lasers change. It never crits, ignores laser ammo, and one rocket takes at most a quarter of another pilot's hull. A blast is strongest at its centre and falls to 25 to 35% at its edge.
- **All rockets share one 5 second timer,** whichever you fire. It goes on through a jump, a reconnect and a ship swap, and a destroyed ship does not reset it.
- A new **Rockets** picker sits beside Ammo on the hotbar: drag rockets onto slots. Press the slot's key or click it, or press **R** to fire the rocket you fired last (rebind it in Settings › Controls › Fire Rocket). A pie counts the timer down on every rocket slot. If a rocket can't fire, you are told why.
- Guided rockets show a green lock ring on your target when it is in range, a dim red one when it is too far. Straight rockets show a dashed line and the circle a blast would fill. The Shop and the Hangar have a Rockets category with the numbers on your ship. If a rocket is locked on your ship, the screen edges flash red and a warning sounds.
- Rockets follow the rules of lasers: none hurts a ship in a safe zone, before the Peace Protocol ends, in sectors where pilots may not fight, or in your own company. You need a laser fitted to fire one. Launching a rocket ends your own safe-zone protection, and a rocket that loses its target keeps flying straight. A straight single-target rocket needs a moment to arm, so it can't hit a ship that is almost touching yours: use your lasers at point blank.
- Only a direct hit claims an alien, so blasts don't steal your kills, and a blast doesn't wake a sleeping pack.
- A rocket is a shot: it ends your own cloak. A cloaked ship or one inside its EMP cannot be locked on, and a straight single-target rocket flies through it. An **area blast** still hurts a ship it covers, cloaked or not, and ends its cloak.

**Abilities: Shield Surge, Afterburner and Emergency Repair**
- The item you put in an ability slot decides the ability. A ship can carry one of each in a configuration: a Paragon or Wraith all three, an Ostirion two, a Protos or Kitefin one.

  | Ability (key) | Item | Strength | Lasts | Cooldown |
  |---|---|---|---|---|
  | Shield Surge (Q) | Light, Basic, Heavy Shield Core | an overshield of 30%, 60%, 100% of your max shield, and shields take at least 90%, 95%, 100% of every hit | 10 s | 120, 105, 90 s |
  | Afterburner (W) | Engine I, II, III | speed +30%, +45%, +60% | 10 s | 120, 105, 90 s |
  | Emergency Repair (E) | Repair Drone I, II, III, IV | heals 20%, 25%, 32%, 40% of your max hull at once | instant | 120, 105, 90, 75 s |

- They are made for the moment a fight is being lost or a group opens fire, not for every cooldown. The Afterburner works everywhere, safe zones included, so you can run home. Emergency Repair works under fire and is refused at full hull. A Surge is refused inside a safe zone. When a Surge ends, what is left of the overshield is gone and the shield you had is untouched.
- The cooldown starts when you press and belongs to you: it is saved when you leave, and time offline doesn't count. Swapping configuration, changing the item or jumping doesn't reset it, and each ability has its own. A destroyed ship starts the next flight ready.
- An item in an ability slot adds nothing else, and a Repair Drone there does not repair by itself. Enchanting the item makes its ability stronger by the same percentage as its main stat, up to +15%.
- **Only ranks I and II of shields and engines exist so far:** the Heavy Shield Core and Engine III cannot be bought or crafted yet. Repair Drone IV (40% of your hull every 75 seconds, 2,000 Thulium) is the strongest ability you can reach today.
- A Surge does not add to the Shield Absorbance Boost: while it runs, the shields take the higher of the two. A rocket that pierces the shield partly skips the Surge as well.
- Drag a shield, engine or Repair Drone onto an ability slot, or right-click it in your inventory. The slot shows the ability and its rank, and hovering it tells what it is worth on your ship. A shield or engine that holds cells or thrusters gives them back when you put it into an ability slot.
- The buttons beside the hotbar have a ring that drains while the ability runs and fills while it recharges. Everyone on the map sees a Surge (a bubble that fades with the overshield), an Afterburner (a ring and hotter engines) and a repair (a green pulse), each with a sound. The Ship window and the target panel show the overshield beside the shield.

**Cloaking CPU and EMP Charge**
- **Cloaking CPU S, M and L** are sold in the Shop for Thulium only: 10 uses for 5,000, 25 uses for 11,250 and 50 uses for 20,000 (500, 450 and 400 Thulium a use). Uses are saved with the CPU; logging out or dying gives none back.
- Drag CLK from the hotbar's Extras onto a slot and press it. One press is one use, and the cloak lasts up to 30 seconds. Pilots of other companies, aliens and company pilots of other companies do not see your ship and cannot lock on to it. **Your own company sees you as a pale ghost that nobody can target.** Clan mates from another company do not: a clan takes anyone who applies.
- You cannot cloak inside a safe zone, while the CPU recharges (20 seconds after any cloak ends), or within 10 seconds of a hit or a shot. Your first volley or rocket launch ends the cloak, and so do a second press and entering a safe zone. You can still collect cargo while cloaked, but the box you take is gone for everyone, so others learn that something was near that spot, not who. Aliens that were after you lose you, and your kill claims are released.
- **EMP Charge** is a single-use Extra for 500 Thulium. Press the EMP slot in a fight: for 3 seconds nobody can lock on to you, and every lock already on you breaks at once, wherever the attackers are. Pilots are told "Lock lost: target used an EMP", and aliens go back to roaming. It does not hide you and it is not invulnerability: you stay visible and can keep firing, and a blast or the black hole still hurts. It recharges for 30 seconds, and it does not work inside a safe zone or while cloaked. It works in the first days of a season too, because aliens hunt then.
- The recharge of both is not saved: logging out or jumping through a portal clears it, but every press still costs a use or a charge.
- Your ship shows see-through with a violet outline while cloaked, with a chip at the top counting the seconds and the uses left. The EMP shows a crackling shell and a ring counting the 3 seconds, and the target ring of everyone who had you selected breaks apart. Identical spare CPUs and EMP Charges stack into one tile. Aliens no longer steer around a cloaked ship, so their movement doesn't give it away.

**The Forge (replaces the Fusion Chamber)**
- The second tab of the Assembly page is the Forge, in flight too. It works on lasers, laser amps, shield cores, shield cells, engines, thrusters, Adaptive Cores and Repair Drones, in your inventory, on a ship or fitted into another item.
- **Tier up** raises an item one tier at a time: Standard, Tainted, Godly, Rupturing, Eternal. You can't skip a tier. Every step costs more, and can fail:

  | Step | Success | Credits | Materials |
  |---|---|---|---|
  | Tainted | 100% | 10,000 | 5 Ship Fragments, 15 Daraxium |
  | Godly | 90% | 50,000 | 30 Ship Fragments, 45 Nyxite |
  | Rupturing | 75% | 200,000 | 20 Reinforced Hull Plates, 120 Cataclysite |
  | Eternal | 60% | 500,000 and 2,000 Thulium | 8 Power Cores, 240 Quorvium |

- A failed step leaves the item as it was, costs the credits, and gives half of the materials and half of the Thulium back. The panel shows the chance, what you have (green) and what you lack (red, with a note when the missing part sits in your Transport Cache) before you press. The last step asks you to confirm.
- Every tier holds one more buff than the one below (up to four on a shield core) and the buffs are bigger: Tainted +2 to 5%, Godly +4 to 8%, Rupturing +6 to 11%, Eternal +9 to 15% (Range stays at +5% at most). A tier-up rolls each buff again in the new range, keeps the better value and adds the new buff. **Gear made before the Forge keeps the buffs it has.**
- **Merge** two copies of the same item into one: it has the higher tier and the best value of each buff, never more buffs than its tier holds (the panel shows what is left out, and why), and costs credits by the tier it makes, from 5,000 to 250,000. The copy you merge into can stay on your ship, the other is used up. Merging a Godly or better item, or one with buffs, asks first.
- The crystals drop from aliens now: Daraxium from Seekers and Phantasms, Nyxite from Phantasms and Bulwarks, Cataclysite from Bulwarks, Gorvanes and Crystalys, Quorvium from Gorvanes and Crystalys. The Forge stays on your item after each step: there is no "Fuse More" button.
- The Quantum Laser 1 and 2 hold damage and range buffs only (they have no crit chance of their own). An old crit buff on them is dropped at the next tier-up or merge.
- The Forge has an (i) help card and a wiki page, and it is in all 11 languages. A 0.4.2 client still shows the Fusion tab and tells you to update.

**Skylab: the supply chain and your best lasers**
- Four new modules from Core level 5: **Velkonite Collector, Orvium Collector, Resource Storage and Forgery**. Each costs 10 Ship Fragments (from your inventory, and you must be landed), 10,000 credits and 500 Thulium, and they show in the Station, List and Table views.
- The collectors mine ore by the hour (12 Velkonite and 6 Orvium at level 1, 25% more a level) and hold 72 hours of it. **Collect** moves the ore into the Resource Storage, which keeps 900 of each at level 1 (25% more a level) and keeps it through the season wipe. Ore comes from the collectors only.
- The **Forgery** turns banked ore into plates, 10 seconds a plate, one batch at a time: 10 plates at level 1 and 5 more a level. A Velkonite Reinforced Plate takes 40 Velkonite and an Orvium Reinforced Plate 80 Orvium (1.5% less for every level above 1). Ore leaves the storage when a batch starts. Collect finished plates into your inventory while your ship is landed.
- The new modules draw power (20, 30, 10 and 30 at level 1). **A station that uses more power than it makes stops every farm and collector,** so read the build sheet's power balance before you build.
- **Assembly recipes changed:**
  - Quantum Laser 3: 10 Ship Fragments, 2 Velkonite Reinforced Plates and 1,500 Thulium (60 s).
  - Starfire-3: 25 Ship Fragments, 10 Velkonite Reinforced Plates, 1 Reinforced Hull Plate, 3,000 Thulium and 100,000 credits (120 s).
  - Helios Beam: 50 Cataclysite, 2 Power Cores, 20 Orvium Reinforced Plates, 5 Reinforced Hull Plates and 5,000 Thulium (300 s).
- The old Starfire-3 and Helios Beam recipes are gone. A craft you already started keeps what you paid, and the Iron Tide quest still gives a Starfire-3.
- A (!) badge shows when ore can be collected and when plates wait. New help cards cover the storage, the Forgery and the whole chain, the wiki's Skylab and Lasers pages are rewritten, and the four modules have pictures in the List view.

**Danger Sectors and Terra**
- The four PvP sectors are the **Danger Sectors:** `4-1` to `4-4` are now `DS-1` to `DS-4`. They keep their place, size, sky, planet and rocks. Pilots parked in one stay there, and their kill, loss and distance statistics move to the new names. Each company keeps its own entrance: Mars' `M-4` opens on `DS-1`, Terra's `T-4` on `DS-2`, Galactic's `G-4` on `DS-3`.
- **Terra is a diamond.** `T-1` has gates to `T-2` and `T-3`, both lead on to `T-4`, and `T-2` and `T-3` no longer have a gate to each other. The Galaxy map draws it that way. The trade-off: `T-3`, with its tougher aliens, is one gate from Terra's home, so new Terra pilots meet them sooner.
- Quests that count "in the PvP centre" read `DS-x`, and the wiki, help texts and store text use the new names in all languages. The Galaxy map shows the full name ("Danger Sector 2") when you point at one.
- If you are still on 0.4.2 when the server updates, the game keeps working but shows the new sectors under their ids (`DS-1`), gives them the sky of `G-1` and leaves them out of its Galaxy map. Update the game to see them properly.

**The black hole**
- A black hole hangs in the exact middle of `DS-4`, the same in Alpha, Beta and Gamma, every day of the season, the Peace Protocol included. The portals and the lanes between them stay well outside it.

  | Ring | Distance | What happens |
  |---|---|---|
  | Radiation | 4,000 | your ship loses a share of its total max HP (hull plus shield) every second: 0.3% at the rim, 2% at 2,000, 5% at 1,200, 24% at the event horizon. The shield goes first. |
  | Pull | 3,000 | the hole pulls your ship toward the centre, harder the closer you are |
  | Point of no return | about 1,000 to 1,300 | where the pull equals your speed. A faster ship leaves from deeper, and a running Afterburner counts |
  | Event horizon | 300 | any ship that reaches it is destroyed at once |

- While the radiation burns you, your shield does not recharge and your Repair Drone stops. It is not a hit: a Surge's overshield does not soak it up and a cloak doesn't hide you from it. Emergency Repair still heals.
- A ship the hole destroys respawns at its company base like any destruction, with no wreck, no crate and no honor lost. **The last enemy pilot who hit your ship in the 15 seconds before it died is credited with the kill** (a kill in their statistics and the PvP points of your ship type, no loot). Company mates who hit you still lose the friendly-fire honor, and nothing is credited during the Peace Protocol.
- Your move orders fly around the outer ring (4,200 units); an order that ends inside is obeyed, and going in is your choice. The chat warns you at each edge and at your own point of no return. Leaving the game in the radiation puts you back on the outer edge, holding position. Leaving inside the pull (3,000) does not save you: you come back where you left and keep falling.
- Pilots who were parked in the middle of `DS-4` are moved out once, when the server updates. Aliens and company pilots keep out of it, and no crate is dropped inside.
- You see it: a black disc with a bright ring, an accretion disk, matter streaming in and (Medium graphics and up, with post-processing on) a lens that bends the stars. Rings mark the radiation and the pull, and a red line shows your own point of no return. A gauge above the hotbar shows the dose in % of your HP a second, "Lethal in N s", the pull against your speed and the distance to your point of no return. The screen edges glow violet and turn red as the dose grows, a Geiger counter clicks faster, a two-tone warning sounds at the rim and at your point of no return, and the death card says "Swallowed by the black hole" or "Burnt up by radiation". The minimap and the star chart show it, and Reduce Motion stills it.
- A 0.4.2 client does not draw it, but it gets the chat warnings, the steering and the kill-log line.

**Drones that grow**
- Every Slave Drone you own has a level from 1 to 8 and earns experience whenever you destroy an alien: 1 for a Seeker, 2 for a Phantasm, 8 for a Bulwark, 24 for a Gorvane and 72 for a Crystalys, doubled in Beta and tripled in Gamma. Player kills, quests and company pilots' kills give none. Levels 2 to 8 ask for 350, 900, 2,000, 3,700, 6,000, 9,500 and 14,000 experience. For a pilot with the gear of the level-7 quests hunting Bulwarks and Gorvanes, a new drone reaches level 2 in about an hour and level 8 in about 27 hours (this is an estimate from our model).
- The laser in a drone's slot deals more damage as the drone levels: +1% at level 3, then +2%, +3%, +4%, +5% and +7% at level 8. The bonus multiplies the laser's own damage, and the amps fitted into it are added on top. The Hangar's damage figures include it.
- A new drone is a small armoured sphere and grows into a crescent-winged gunship at level 8. Other pilots see your drones at their levels. Drones fly in a tighter formation, and a level-8 drone is about 19.5 units across. A drone that levels up pops, sends out a ring of light and chimes, and the Game Log says so. The Hangar's Drones view shows each drone's level, an experience bar, its laser bonus and how many kills the next level needs.
- **Drones are kept at the season wipe** with their levels, their slots and the lasers in the drone slots of your active ship. Before, a wipe took them and the next price started over. Slave Drones can no longer be put in the Transport Cache, because they stay by themselves.
- **The Slave Drone price follows a table:** 100,000, 200,000 and 400,000 credits for the first three; then 800,000 credits and 10,000 Thulium for the 4th, rising to 12,800,000 credits and 50,000 Thulium for the 8th (25,500,000 credits and 150,000 Thulium for all eight). The price goes on from the number you hold, and with eight there is none left to buy. This is cheaper than in 0.4.2, where the first cost 100,000 credits and 10,000 Thulium and the 8th 25,600,000 credits and 1,280,000 Thulium. Nobody is refunded for drones bought at the old prices.
- Crafting a Master Drone uses the Slave Drone with the least experience. Drones you already own start at level 1.

**PvP: repeated kills pay less, and the ranking weights**
- Destroying the same pilot again within 24 hours pays fewer PvP points: the first kill pays all of them, the second half, the third a quarter and every one after that none. The count is per killer and victim, and the 24 hours restart with every kill of that pilot, even one that paid nothing, so hunting the same pilot every few hours stops paying until you leave them alone for a day. The rule applies from 0.4.3 on.
- Your Game Log says when a kill paid less ("Repeated kill of the same pilot: 50% rewards"), and the Rankings calculation shows the points as their own line. The kill still counts in your kill totals, and the pilot you destroyed loses what it always lost. Destroying a pilot of your own company and the Peace Protocol work as before.
- **Ranking fix:** Ostirion kills were counted as 10 PvP points instead of 20 because of a misspelling, and Kitefin kills had no weight of their own. An Ostirion kill is worth 20 points now and a Kitefin kill 15.
- When the server starts with 0.4.3, every pilot's PvP points are recounted from the kill statistics (the server counts them again at every start, and a second count changes nothing): each Ostirion you destroyed adds 10 points and each Kitefin (since 0.4.0) adds 5. Nobody loses points and PvE points don't change, but your ranking points and your clan's PvP score go up, and PvP Hall of Fame places can shift, mostly upward for pilots who hunt Ostirions.

**Shield boosts, told apart**
- The Boosters window and your pilot profile list three kinds of shield boost on their own rows, each with its icon and total: **Shield Capacity** (your maximum shield points), **Shield Absorbance** (the share of each hit your shields take) and **Shield Recharge** (points restored a second). The permanent buffs read "Permanent Shield Capacity Boost" and "Permanent Shield Absorbance Boost". The help cards and the wiki use the same names in all 11 languages.
- In the Season Store, Shield Boost is now **Shield Capacity Boost** and Shield Absorption is now **Shield Absorbance Boost**. Prices, limits and your levels are unchanged.
- **The Shield Absorbance Boost now raises your absorbance.** Each level adds 0.1% of your absorbance itself, up to +10% of it, and never past 100%: a Basic Shield Core with two Advanced Shield Cells goes from 88% to 96.8% at the top level, so the hull takes 3.2% of a hit instead of 12% while the shields hold. A ship with no shield still takes every hit on the hull.
- **The trade-off:** until now this buff sped up shield recharge (+0.1% a level, up to +10%) and did not touch absorbance. It no longer does: a shield that recharged 1,100 points a second at the top level recharges 1,000 now, and only the Shield Regen booster raises recharge. If you bought it for the recharge, tell us.
- The profile counts absorbance with your buffs like your other combat stats, and its tip shows the loadout's own number. A long booster name wraps onto a second line.

**Shop and inventory order**
- The Shop's categories read from the ship down to what you fit on it: Ships; Lasers, Laser Amps, Laser Ammo, Rockets; Shields, Shield Cells; Engines, Thrusters; Hybrid Generators; Extras; Drones; Boosters; Resources. Inside a category the cheapest item comes first (credits before Thulium), then what only Assembly makes, weakest rarity first. The rockets go by kind and then by price, and the Extras by family: Repair Drones, Cloaking CPUs, then the EMP Charge. Ships go by hull, so the Kitefin sits between the Protos and the Ostirion, and laser ammo reads Standard Battery, Advanced Plasma, Ultra Core, Experimental Fusion Core, Siphon Battery.
- The Shop shows the **Protos**, the ship every pilot starts with, as the first ship, marked Owned, with its 3D model and stats. It is not for sale, and a Protos a wipe took from you can't be bought back.
- The Hangar's inventory lists your items in the Shop's order, not the order you got them in. Your ships are listed smallest hull first. The empty "Generators" entry is gone from the inventory and the Transport Cache, and the Cache has a Rockets filter. The Forge's grid, Assembly's recipes and filters, and the Cache lists use the same order.
- Fixed: the Shop showed the Siphon Battery's price of 0.25 Thulium as 0.2. Thulium prices show up to two decimals now.

**Smoother flight**
- Your ship no longer trembles when the camera is close. Zoomed in on a ship flying straight, it used to swim a few pixels against the middle of the screen, more on an uneven connection: the game chased the server's 20-a-second position updates with two smoothing steps in a row. Now the ship is drawn moving at a steady speed between the updates and the camera stays exactly on it, so the stars, other ships and your escort drones glide past evenly at 60, 120 or 144 frames a second. Other pilots, aliens, engine flames and drones move the same way.
- The trade-off: the world is drawn about 60 ms behind the server's newest update (more on an uneven connection), plus about 80 ms of path rounding. Your orders are not delayed, and the ship's nose turns as fast as before. After a respawn or a jump the camera is on your ship at once.

**Planets, kill log and a test alien**
- **Planets are solid.** On M-4, T-1, G-4, M-1 and the other sectors the nebula clouds, the stars and the map grid used to shine through the planet's disc, so it looked like glass. The disc hides them now, and the haze still hangs in the sky around it. Ships, asteroids, shots and effects draw in front of it, and rings stay see-through. The trade-off: a grid line disappears behind a planet instead of crossing it.

  ![The planets of M-4, T-1, G-4 and M-1, before and after](https://spacecorps.github.io/play/img/releases/v0.4.3-planets.jpg)

- **Kill log:** when you hold the claim on an alien and another pilot (or a company pilot) lands the last hit, your Game Log says "Seeker was destroyed by nova; your claim pays you. REWARDS: ..." instead of "You killed Seeker." The rewards, kills and quest progress are yours, as before. A company mate paid for a company pilot's kill when nobody held a claim still reads "You killed ...".
- **The test alien is gone.** The Brood Matriarch, drawn as a Seeker, flew on M-1 in Alpha and its kills counted as Seeker kills. It is gone from the public server.
- **Release notes can show pictures.** They appear on the download page and in the GitHub release. The game's What's New can't draw images yet, so it shows each picture as a link with its description.

**The Siphon Battery, seen and heard**
- The Siphon Battery no longer fires a laser beam. A thin, faint teal probe goes out to the target, its shield flares teal where the probe lands, and the shield you drained streams back to your ship as glowing teal packets over about half a second (three to ten packets, more for a bigger drain, brighter for a crit). Each packet pulses your shield, and "+2,600" in teal floats over your ship. The gold number over the target still shows what was taken.
- You see the same for every pilot's Siphon Battery. When another pilot drains you, the probe flies at your ship, the shield you lost shows as a red number and the packets leave for theirs. Low and Medium particle quality draw fewer packets. Damage, gain and the cost of a round are as in 0.4.2.
- The Siphon Battery has an icon of its own (a magazine with a teal vortex) and a sound of its own, a rising chirp.

**Hotbar and fights**
- The ammo picker and the hotbar show pictures of your ammo and of the Repair Drone, as the Shop and Hangar do, instead of x1 to x4, SB and REP labels. The amount you own stays on each tile, and pointing at one shows its name and damage multiplier. The target panel's Firing pill shows the ammo's picture too. Your saved hotbar keeps working.
- Aliens keep room for each ship by its own size. They used to stay the same distance from every ship, so they clipped a Wraith's wing tips and hung farther from a small Protos than they needed to. The red lock ring is bigger around a Wraith.
- The Settings window no longer jumps when you switch tabs, and the Item injection card on the admin page wraps in narrow windows.

**Admin: bonus codes**
- The Admin page has a **Bonus codes** tab (admins only). It lists every code with its state (active, switched off, expired or used up), what it gives, how many pilots have claimed it and when it ends, and who claimed it and when.
- Admins can make a code, change what it gives (credits, Thulium, items, boosters and ships picked by name), its claim limit, minimum level and end time (UTC), switch it on and off, copy it and delete it. A change applies to the next claim, with no update and no restart.
- The codes live in the server's database now. The first start with 0.4.3 copies them from the file that held them, and after that the file is only the starting set for a new server.
- Nothing changes for pilots: a code can be claimed once per pilot, the claim limit counts every claim ever made, and a wrong, switched-off or expired code gets the same answer.
- A code that has been claimed can be switched off but not deleted, and a code's text can't be renamed (copy it under a new text; the copy starts switched off). A code whose item has left the game stops working and shows "Needs a look".

## 0.4.2 · 2026-09-29

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.2)

SpaceCorps 2027 0.4.2 rebalances weapons, ships, Repair Drones and aliens (some setups got weaker, and this page says which), draws critical hits differently, adds an ammo that steals shields and stops a destroyed ship from leaving a wreck. It also brings a smaller target panel, explanations for the generator slots, a better Shop and Assembly, and fixes for a batch of pilot reports.

### What's new

**Highlights**
- Lasers, ships, Repair Drones and aliens are rebalanced (some setups got weaker, listed below), and a new Repair Drone IV mends 5% a second.
- The new **Siphon Battery** ammo steals shields from your target and adds them to yours, for 0.25 Thulium a round.
- Critical hits are easy to spot: ice cyan numbers ending in "!".
- A destroyed player ship no longer leaves a wreck.
- The Seeker and the Gorvane only fight back, aliens stop stacking on your ship, and the last laser that kills an alien is always drawn.
- A smaller target panel, ships 10% bigger in flight, and the camera starts farther out (150%).
- The Shop has a Max button and greys out what you already own, and Assembly shows item cards on hover.
- Fixes for a batch of pilot reports: the Skylab tooltip, the Mission Control button, long German mission cards and more.

**Balance: lasers**
- The lasers have new numbers. A critical hit still does 1.5 times the damage, and Damage Amps and Crit Amps still add crit chance.

  | Laser | Damage | Crit chance | Amp slots | Price |
  |---|---|---|---|---|
  | Quantum Laser 1 | 50 → 55 | 10% → none | 1 | 10,000 → 8,000 credits |
  | Quantum Laser 2 | 60 → 65 | 20% → none | 2 | 100,000 → 80,000 credits |
  | Quantum Laser 3 | 70 → 80 | 30% → 10% | 3 | 15,000 Thulium |
  | Starfire-3 | 120 → 135 | 35% → 15% | 3 | craftable |
  | Helios Beam | 180 → 185 | 40% → 25% | 1 → 3 | craftable |

- The Quantum Laser 1 and 2 have no crit chance of their own any more. A Damage Amp or a Crit Amp in their slots brings it.
- **What got weaker.** Measured as the average damage of a volley with x1 ammo, most setups do more than before, but these do less:
  - the Quantum Laser 2 in every setup: 1.5% less with no amp, 0.9% less with one Crit Amp, 3.6% less with one Damage Amp, 2.9% less with one of each, 5.0% less with Damage Amps in both slots and 0.3% less with Crit Amps in both;
  - the Quantum Laser 3 with Damage Amps in all three slots: 1.4% less;
  - the Starfire-3 with three Damage Amps: 0.4% less;
  - the Helios Beam with no amp: 3.6% less, with one Damage Amp 3.9% less (211.5 → 203.2) and with one Crit Amp 3.3% less (206.6 → 199.8). With its new second and third amp slot filled, the Helios Beam does far more (237.6 with three Damage Amps).

**Balance: ships and Repair Drones**
- **Ostirion:** 655,000 → 425,000 credits, and the hull grows from 32,000 to 48,000.
- **Kitefin:** the hull grows from 16,000 to 24,000, but it now costs 600 Thulium and no credits. It used to cost 200,000 credits.
- **Paragon:** eight laser slots instead of six.
- Every Ostirion and Kitefin you own has its saved hull raised in the same proportion, once, when the server starts with 0.4.2, so a ship that was full stays full.
- **Repair Drones** mend more: Repair Drone I 1.5% of the hull a second (was 0.5%), II 2.25% (was 0.75%), III 3.5% (was 1.25%). They now cost credits: 5,000, 15,000 and 35,000 (they were 10 Thulium each). A new **Repair Drone IV** mends 5% a second and costs 2,000 Thulium. With several fitted, the best one works, as before.

**No more wrecks for player ships**
- A destroyed player ship no longer leaves a wreck. No cargo box appears, whoever or whatever destroyed the ship (a pilot, an alien, a company pilot). The "Your wreck" card and its message are gone. Aliens still drop their loot as boxes and company pilots' ships still leave salvage. Player wrecks are removed for now: their salvage was made from nothing and respawning is free, so dying on purpose next to a station would have paid. How they could come back with balanced rules is tracked at https://github.com/SpaceCorps/play/issues/40.

**Critical hits**
- A critical hit is now easy to spot: its number is ice cyan, 45% bigger, ends in "!" (for example "1,320!") and stays a little longer. A critical hit you take is red, bigger and ends in "!" too. The old orange "heavy hit" guess is gone. The server now tells the game which volleys crit, so this works for your lasers, company pilots and the Siphon Battery alike. The cyan is also told apart from the gold and red numbers with the usual kinds of colour blindness.

**A new ammo: the Siphon Battery**
- The Shop sells a new laser ammo, the **Siphon Battery**, for 0.25 Thulium a round. It steals shields instead of breaking hulls: each volley does x1 damage to the target's shield and adds the same amount to your own shield, up to your maximum. A critical volley drains 1.5 times as much.
- It never touches the hull, so it can't destroy anything, and the target's absorbance doesn't matter. Against a target with no shield left it does nothing, and the volley still costs one battery per laser.
- Pick it in the hotbar's ammo picker (label SB), next to x1 to x4. Its beam is teal, your shield pulses teal when it takes some in, and the number over the target shows the shield it took.
- Taking shield doesn't delay your own shield regeneration. Draining an alien's shield counts as your first hit for its kill claim, and it wakes a Seeker or a Gorvane like any hit. The ammo a pilot fires before picking one, and the company pilots' ammo, is still x1.

**Balance: aliens**
- **Seeker:** damage 200 → 180.
- **Phantasm:** hull 1,600 → 2,000, damage 400 → 350, speed 140 → 160. It now flies faster than a starter Protos (150).
- **Bulwark:** shield 16,000 → 10,000, damage 1,200 → 900, speed 170 → 175.
- **Gorvane:** hull 64,000 → 32,000, damage 4,000 → 3,000, speed 200 → 180. It no longer attacks first (see below).
- The Crystalys and every alien's rewards are unchanged.
- **The Seeker and the Gorvane only fight back.** They never go after a ship that comes near. Shoot one and it turns on the pilot who hit it last, whoever else is around. It lets go 10 seconds after anybody last hit it, and after 30 seconds alone its hull mends by 2% of its maximum a second, so a Gorvane you shot from afar and left is not there half-dead for the next pilot. The Phantasm, the Bulwark and the Crystalys work as before: they go after the nearest ship in their range and don't mend. A hit that does no damage doesn't wake a Seeker or a Gorvane, and one alien never calls another.
- The wiki's alien pages have a new "Rules of Engagement" card with this.

**Balance: company pilots**
- A company pilot's Ostirion has the new 48,000 hull, its Quantum Laser 2 has no crit, and its Repair Drone mends 1.5% a second.
- Company pilots now help only in fights they can win. An alien that attacks your company mate on its own is still fought off, as before. What your mate is shooting at, and a Seeker or a Gorvane that turned on your mate because your mate hit it, they join only if the squad can take it. A mate who tags a Gorvane from afar no longer pulls the squad into a fight it cannot win and takes the kill.

**Fights**
- The laser that destroys a target is always drawn now. Before, the last volley could vanish when the target died in the same moment: no beam, no muzzle flash and no damage number. Every beam flies to the target, including each pilot's when several of you finish an alien together, and the explosion follows when the last one lands.
- Aliens no longer fly through each other or park on top of your ship. Each alien keeps room around its hull, bigger aliens more than smaller ones, and gives way to a ship instead of sitting on it. Fights work as before: aliens still chase you, stop at their attack range and leave you alone inside a safe zone.

**Target panel**
- The target panel is smaller and sits higher. The name has the distance and the fire state under it, beside the fire and clear buttons, and the hull and shield bars sit side by side. It sits at the top edge between the two toolbars when the window has room; in a narrow window it keeps to the row under them, and it slides aside for a window in its way.
- In long languages, the target panel shows the pilot who claimed an alien in full; "No reward" moves to the line below when the name needs the room.

**Flight view and controls**
- Pilots' ships are 10% bigger in flight: yours, other players' and your company's pilots'. Aliens, jump gates and the station keep their size.
- The flight camera starts farther out: Camera Zoom (Settings > General) now starts at 150% instead of 100%. If you were still on the old 100%, it moves to 150% once; pick another zoom and it stays. The slider still goes from 50% to 225%.
- A click beside another pilot's ship locks it only when you click close to it. Before, a click three ship-lengths away could still lock a small ship. Clicking an alien works as before.
- A double click on an alien is no longer lost when the game hitches for a moment just before your first click.
- Dragging a hotbar slot onto another slot now moves the item. If the other slot holds something, the two swap. Hold Alt (Option on a Mac) while you drop to copy instead. Dragging a slot off the bar still clears it.
- The next sector's sky no longer loads just because you fly past a jump gate. It loads when you are close to the gate or flying toward it, so the game uses less graphics memory near gates.

**Shop and Assembly**
- The Shop shows what you can't buy again. A ship you own says "Owned" on its card, and its Purchase button is greyed out and says why. The Slave Drone does the same once you hold 8.
- A new **Max** button next to the quantity fills in the most you can afford, so buying all the ammo you can pay for takes one click. Equipment still stops at 100 per purchase. Ships and the Slave Drone are bought one at a time, so they no longer show a quantity.
- In Assembly, hover a recipe's picture or name to see the same card as in your hangar: stats, bonuses and weight for equipment and boosters, and the specifications of a ship. Items in the Production Queue show it too.
- Assemble is greyed out, with the reason, for a ship you already own or already have in the queue.
- A booster you buy in the Shop or collect in Assembly at the moment you leave flight no longer loses its time.

**Hangar and wiki**
- The Hangar explains the generator slots. Next to the captions Core, Support and Auxiliary there is now an (i): a Core slot counts an item at full strength (100%), a Support slot at 75% and an Auxiliary slot at 50%, and the card lists how many of each every ship has. Only some ships have auxiliary slots (the Paragon 2, the Wraith 4).
- The wiki's ship pages have the same (i) on their slot tiles, the Inventory article explains the three kinds, and the ship pages call the extra slots "Extra slots".
- The help cards and the wiki articles quote the new numbers.

**Skylab**
- The tooltip over a module in the 3D station fits its text. After hovering something short, the Credit Farm's tooltip no longer breaks into pieces like "Cre-dit Far-m": words stay whole and long lines wrap at spaces. The tooltip is also a bit bigger, with larger text, and slightly see-through so the station shows behind it.
- Thulium prices in Skylab are whole numbers. Solar's next level costs 269 Thulium, not 268.912, and that is exactly what the upgrade takes.
- The white plating on the station (rings, tanks, deck tops) glares less when you turn the station towards the sun.

**HUD and Mission Control**
- Panels you have set to a low HUD opacity (under about 35%) fill in while your pointer is over them, so the quest tracker, chat, minimap, windows and toolbars stay easy to read in front of a station. They go clear again when you move away.
- The Mission Control button on a station holds still. It no longer flips back and forth when a window or notice sits near it; if a window pushes it aside it stays put and slides back once its own spot is free.
- On a mission card, the Accept, Abandon and Claim buttons, the reward icons and the task progress stay inside the window in every language. Before, a long German task line pushed the card past the window edge and cut them off. The "Ready to claim" badge no longer runs over a mission's title in German and Russian.

**Admin**
- Giving an item from the Admin menu makes separate items for everything that doesn't stack: ten lasers are ten lasers you can fit one by one. Ammo and resources still stack. A ship is given one at a time and goes to the hangar, a booster adds 10 hours of boost time per unit, and a pilot can hold at most 8 Slave Drones, as in the Shop, which the quantity stepper now stops at. Stacks an admin gave before 0.4.2 stay as one item.
- The ranking configuration no longer lists the names of aliens the game never spawns. Nobody's points change.

## 0.4.1 · 2026-09-28

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.1)

SpaceCorps 2027 0.4.1 stops the flicker on the login screen and in Skylab, and shows each pilot's clan tag next to their company letter.

### What's new

**Flicker fixed**
- The screens around sign-in no longer flicker. The stars and nebula behind the login card, the start screen and the station menu used to jump back and forth while the view drifted; now they hold still, and the ship beside the login card no longer shimmers.
- The 3D station in Skylab no longer flickers when the camera turns or you zoom. The coloured stripes and panels on the ring and the modules stay put, and so do the stars behind the station.
- The spinning shape on the start screen has smooth edges: its thin lines no longer crawl as it turns.

**Clan tags**
- Your clan's tag now shows in gold after your company's letter, for example "[M] [VNGD] nova": on the name tags in flight (your own included), in the target panel and in chat.
- When a pilot joins, leaves or changes clan in flight, their tag changes at once for everyone around them. A chat line keeps the tag its pilot had when they sent it.
- Pilots outside a clan show only their company letter, and company pilots keep their names as before.
- When a chat line wraps, the company letter, clan tag and name always stay together on one line.

## 0.4.0 · 2026-09-27

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.0)

SpaceCorps 2027 0.4.0 is a graphics overhaul. Every alien now has a body of its own that moves and shows when it attacks, Skylab becomes a 3D space station that grows as you build it, ships and stations are lit by the nebula around them, the sun casts real shadows, hulls show their panels, rivets and running lights, explosions and warps bend space, and a new Graphics Quality setting picks the right detail for your computer. An alien's rewards now go to the pilot who hit it first, a double click attacks, and every pilot's company shows before their name. This release also brings a new ship, the Kitefin, 88 missions for levels 1 to 8, respawns at your company's base, a new logo, bonus codes, the game in Hungarian and new names for two aliens.

### What's new

**The Swarm gets real bodies**
- Every alien has its own model instead of a recoloured Seeker: the Seeker (a slim scaled lancet), the Phantasm (a violet pinwheel around a floating core), the Bulwark (an isopod in forged bronze armour with glowing amber seams and claw legs), the Gorvane (a crimson manta with a glass crest) and the Crystalys (a crystal star with orbiting shards).
- Aliens move: fins flap, plates breathe, wings ripple, crowns and orbiting shards turn.
- You can see when an alien turns on you, not only from its laser. The Bulwark raises its armour plates and bares its glowing seams, the Gorvane arches its wings and spreads its pincers, the Crystalys spins up its crown and orbiting shards, and every alien's weak points flare.
- The pointing hand now covers the big aliens all the way to their wing tips and shards.
- WP Sources and the wiki show the new aliens: their icons on the milestones (hover one to see the alien move) and in the wiki's list, and each alien's own model in its wiki article.

**New alien names**
- The Class IV cruiser of x-3 and x-4 has a new name, the Gorvane, and the test alien on Alpha is now the Brood Matriarch. Same aliens, same rewards: your kills, statistics and WP Sources progress carry over under the new names.

**First hit claims the kill**
- An alien's rewards now go to the pilot who hit it first, not to whoever lands the last shot. Your first hit claims the alien, and every hit after renews your claim.
- If you don't hit it for 10 seconds, your claim lapses and the next pilot to hit it claims it. It also ends when your ship is destroyed or you leave the map, and coming back doesn't bring it back.
- When the alien is destroyed, the pilot holding its claim gets everything: credits, Thulium, XP, honor, the kill for quests and Wipe Points, and its cargo crate. If you finish an alien someone else claimed, you get nothing, and the Game Log says so.
- Select an alien another pilot has claimed and the target panel shows "Claimed by" that pilot and "No reward". Hover it for the details.
- Company pilots never claim an alien. One they finish still pays the pilot holding its claim.

**Attacking**
- Double-click an alien or a pilot of another company to select it and open fire, as the attack key does. A pilot of your own company is only selected.
- The lock holds when you fly past your target. Before, clicking just beyond it often dropped the lock and stopped your fire, and with the camera turned a click could select an alien out of sight behind the view.
- The Flight controls card on the Dashboard and the Firing help card show the double click.

**A new ship: the Kitefin**
- The Shop sells a fifth ship, the **Kitefin**, for 200,000 credits. It sits between the starter Protos and the Ostirion.
- It carries three lasers, five generator slots (2 core, 3 support), 16,000 hull and a base speed of 175. That is twice the Protos's hull, with a third gun and a faster drive.
- The Ostirion still has twice its hull, a third core generator slot, a second ability slot and more speed.
- The Kitefin is a kite-shaped light gunship with a forked tail, in sea teal and coral. Its wiki page has the full stats.

**Missions for levels 1 to 8**
- Mission Control has 88 missions for pilot levels 1 to 8, grouped by level on its Missions page. Take a level's missions in any order, up to five at a time. Each level's missions give most of the experience you need to reach the next level.
- Every level ends with a **Special**. It opens once the level's ten other missions are done, and it also pays items: lasers, shield parts, cores, ship fragments. Level 1's missions come with a few starter items too.
- From level 2 on, the missions take you to higher sectors step by step, up to the PvP centre and other companies' borders at level 8. Each task names its sector, and only kills and flying there count. Distance flown inside a safe zone doesn't count toward a patrol.
- A timed mission shows its limit before you accept it, and a countdown after. In Beta and Gamma, where aliens are tougher, the limits are longer.
- Rewards show their item icons. Experience, credits, Thulium and honor are multiplied by your world as before; items and booster hours are the same in every world.
- Missions you already completed stay completed. A reward you hadn't claimed yet pays the better of the old and the new reward. An active mission whose tasks changed is dropped without penalty, and you can take it again.
- The wiki lists every mission under Mechanics › Quests.

**Skylab becomes a station you build**
- Skylab is now a 3D space station you can orbit. The Core sits in the middle with six docking ports: Solar, the Credit Farm and the Thulium Farm dock at theirs, and your active ship waits in the docking bay.
- Every module changes shape as it levels (at levels 5, 10, 15 and 20), and a row of lamps on its collar shows its exact level.
- You can see what each module is doing. Upgrades put up scaffolding with construction drones and a hologram of what is being built. Modules you haven't built yet show as holograms. A full farm stacks its cargo and sends up a beacon of light, a switched-off module goes grey, and in a power deficit the lights flicker red.
- A chip over each module shows its name and level, with a ring for a farm's storage or an upgrade's progress. Hovering a module lights up its outline.
- Click a module or its chip, or press 1–4, to open its panel beside the station: production, power, storage, Collect, the power switch, and what the next level costs. The camera swings round to show the module with the rest of the station behind it. The old card list is still there under **List**.
- **Collect All** empties every farm at once, and a meter shows how much of your power you use.
- What your farms have stored is always yours to collect. Switching a farm off, upgrading it or running out of power only stops its production: Collect and Collect All still take what it holds. Until now such a farm couldn't be collected until it was back on, done upgrading or powered again.
- In a power deficit your farms now stop producing (they used to keep producing while collecting was paused), and a notice says so. They start again when you make enough power.
- A module already at the Core's level now says which Core level it needs, instead of offering an upgrade that fails.
- A new station, with only its Core, shows **Build Solar** instead of a power alarm.
- The page's subtitle no longer says "(WIP)".

**Light and shadow**
- Each sector's nebula now lights the ships and stations in it. The sides the sun misses take a soft glow from the sky instead of going flat grey, and metal panels reflect the nebula's clouds.
- The sun casts shadows. Ships shadow each other and the station's deck as they fly over it.
- Space is black again, and each sector keeps the colours of its sky.
- Edges are smoother: 4× multisampling on most computers instead of a blur filter.

**Ships and stations up close**
- Every hull now shows the detail painted into it: panel lines, rivets, worn edges, glossy and matte plating.
- Engines, canopies and conduits glow only where they were painted to. Navigation lights and the station's window rows shine and bloom.
- The jump gates show their plating and hazard stripes, and the space inside their ring shimmers.
- Ship previews in the Hangar, Shop and Wiki are sharper, with studio reflections and deep, true paint colours.

**Effects**
- Warps twist the space around the vortex, and a ring of bent space follows the flash.
- Explosions burn white-hot at the core and push a wave of bent space outward. Their smoke is darker and thinner.
- On High and Ultra, engines leave a faint heat haze.
- Engine trails stay smooth at any frame rate, even at 30 fps.
- Shield hits stay on your ship while it turns.
- When you jump, the new sector's sky is there the moment you arrive.

**Graphics settings**
- **Settings › Graphics › Graphics Quality** is now a preset: Auto, Low, Medium, High or Ultra. It sets Detail, Resolution and Particle Quality together. Change any of those and the preset shows Custom.
  - **Auto** picks for your graphics card:
    - Low on basic graphics.
    - Medium on integrated and Apple graphics, at 75% resolution on very large screens such as a Retina MacBook's.
    - High on dedicated graphics cards and on Apple's Pro, Max and Ultra chips.
  - **Detail** is new. It sets anti-aliasing, lighting, shadow and glow quality.
  - **Resolution** is the old Graphics Quality setting (50, 75 or 100%).
- Your graphics choices are remembered on your computer, so the start and login screens already use them.
- Your graphics preset stays on this computer. It doesn't change the settings the web client or your other computers use.
- If you used to play with low graphics or particles, you keep the cheapest settings.
- Changing the quality in flight may pause the game for a moment while it prepares the new settings. Texture detail changes the next time you start the game.
- Damage you take is now a brighter orange-red, easier to read over red nebulae.

**In flight**
- The minimap is divided into squares, lettered A, B, C… across and numbered 1, 2, 3… down, lined up with the grid under your ship. Your square shows next to your coordinates, like B-4.
- **Settings › General › Show Map Grid** turns off the grid lines under your ship.
- Damage numbers now show only for your own fights: the damage you deal and the damage you take. Other pilots' fights still show their lasers, but no numbers, wherever you look.
- Mission Control opens from the **Mission Control** bubble on the station, which shows whenever any part of the station is on screen, or from the new **Mission Control** button in the toolbar while you are in a station's safe zone. Clicking the station itself now flies you there, like clicking anywhere else.
- Click **Config** in the Ship window to switch configuration, or press your Switch Config key (C by default). After a switch, a small countdown shows the seconds until you can switch again.

**Skylab numbers**
- Skylab has a third view, **Table**: every module's level against its cap, production per hour, what its storage holds against its capacity, power and status in one table, with each module's Build or Upgrade. A module being upgraded always shows its time left.
- Hover any Build or Upgrade button (the cards, the station's module sheet, the table) to preview the next level: what changes ("2,744/h → 3,842/h"), what it costs, how long an upgrade takes (building is instant), and whether the Core has to go up first.
- The upgrade comparison now shows storage too, and the Core's upgrade shows how far it lets the other modules go.
- With the Core at level 20, a module at level 20 now shows **Max Level**. It used to offer an upgrade to level 21, which was refused.

**Ready to claim**
- A small **(!)** marks what you can do right away: Wipe Point rewards ready to claim, and Skylab farms whose storage is full. It shows on the sidebar's Season & Profile and Skylab rows, on the WP Sources tab and its milestones, and on a full farm's card and its chip over the station. In flight, the Return to Base button carries it. Hover it to see what is waiting and where.
- A full farm has stopped producing until you collect it, and you can collect it whatever it is doing.

**A new logo**
- SpaceCorps 2027 has a new logo, a crescent planet with its orbit and moon. It is the app icon on macOS, Windows and Linux, and it heads the start screen, the sign-in card, the sidebar and About.
- **Settings › About** has a Special Thanks section.

**Company tags**
- Every pilot's company now shows before their name as a letter in the company's colour, for example "[M] nova": on the name tags in flight, your own included, in the target panel and in chat.
- Company pilots keep their names as before, and pilots who haven't joined a company show no tag.

**Bonus codes**
- The Thulium page has a new Bonus code card. Type a code you got from us, for example at an event or on Discord, and click **Claim** (or press Enter).
- What the code gives goes straight to your account, and the card lists it: credits, Thulium, items with their icons, booster time, and ships, which go to your hangar. A code never gives you a second copy of a ship you already own.
- Each code works once per pilot, and it stays claimed after a season ends. Some codes may only be claimed by a limited number of pilots, until a given date, or from a given pilot level.
- Codes aren't case-sensitive. If a code doesn't work, the card tells you whether it isn't valid, you already claimed it, or you already own the ship it gives.

**One program on Windows and Linux**
- The Windows download unpacks to one program: `spacecorps2027.exe` now holds all of the game's files, with no `assets` folder next to it. The Linux tar.gz's `spacecorps2027` does the same.
- Updating from an earlier version removes the old `assets` folder once the new version has started correctly.

**Languages**
- The game is now available in Hungarian: every page, the HUD, the help cards, quests and server messages. Pick Magyar in Settings › General › Interface Language, or in the language menu in the bottom-right corner of the start screen. On a system set to Hungarian the game picks it by itself.
- Everything new in this release is in all eleven of the game's languages.

**Respawn and launch**
- When your ship is destroyed you now always respawn at your company's base (M-1, T-1 or G-1) in your world, wherever you died, and also when you close the game on the death screen. You used to come back in the sector you died in when it was one of your company's. The death screen says where you'll respawn.
- The launch window names the sector you'll actually fly to. It used to say "sector 1-1" every time.

**Fixes**
- The mouse pointer now shows what you can do: a hand over buttons, links and anything else you can click, a text cursor in text fields, grab and resize arrows on windows you can move or resize. Before, it stayed an arrow everywhere, on every system.
- Holding Shift in flight shows the second hotbar row, the one Shift+1 to Shift+9 use, even when it's empty. Before, an empty row only appeared while you picked Ammo, Rockets or Extras for it.
- Windows: Shift no longer stays held after you press both Shift keys and let go. The second hotbar row stayed on screen, and 1 to 9 used the Shift+1 to Shift+9 slots.
- Windows: the game's taskbar button, Alt+Tab entry and title bar show the SpaceCorps icon instead of a blank one.
- Admins: the Admin menu shows for every pilot the server names as an admin, and a refused restart or update keeps the Admin page open and says why.
- The server version at the bottom of the flight screen is the server's own. It always said 1.0.0.
- The Brood Matriarch, the test alien on Alpha, starts on M-1 after every server restart instead of on a random sector.
- After a respawn, the cargo of your own wreck, which often lies where you come back, no longer looks like loot: its card says **Your wreck**, and a click on it flies you there and says that only other pilots can salvage it.
- Chinese and Japanese text wraps by stricter line-breaking rules: "——" and "……" stay together, and wrapped lines no longer run past the edge of their box.

## 0.3.4 · 2026-09-27

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.3.4)

SpaceCorps 2027 0.3.4 gives every item a real 3D model, with its icon rendered from it. You can resize every window in flight from any side or corner, so the Game Log can grow as tall as you like, and the minimap shows the pilots of your own company in green.

### What's new

**New item art**
- Every item now has a real 3D model, and its icon is a render of that model. The flat drawn icons are gone from the hangar, shop, fusion (Assembly), Galaxy Gates, cargo, hotbar, item tooltips and the wiki's item tables.
- Items of the same family share a look, and tiers read at a glance: higher tiers get more parts, more tick lights on the item and a darker, polished finish. Mark II boosters have twin chambers, fins and two lights.
- Laser ammo colours now match the lasers you see in flight: x1 red, x2 green, x3 blue, x4 magenta.
- Repair drones share one green repair colour; their tier shows in their arms and lights.
- The frame around an item still shows its rarity and fusion level exactly as before.

**Windows in flight**
- Drag any side or corner of a window to resize it, not only the bottom-right corner. The pointer shows the resize arrows over a window's edges.
- The Game Log grows vertically. Drag its top edge up to make it taller over the minimap, or its bottom edge down. Before, dragging it taller did nothing until enough lines had come in.
- The Game Log, Boosters and Active Quests hug their contents until you resize them. After that they keep the size you chose, also on your next flight, and longer contents scroll.
- Chat grows upward when you drag its top edge.

**Minimap**
- Pilots of your own company show as green squares. Before, every other pilot was red like the aliens. Aliens and pilots of other companies stay red.

## 0.3.3 · 2026-09-27

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.3.3)

SpaceCorps 2027 0.3.3 gives every mission a face: each company's officers now hand out its quests. It also lets you open any pilot's profile from the Hall of Fame, makes fusion work for every item with bonuses, and shows every bonus an item carries.

### What's new

**Meet your quest givers**
- Every mission now comes from a person. Each company has three officers who hand out its missions: one for combat, one for scouting and one for timed and special operations. You get your own company's officers, and the same mission always comes from the same one.
  - **Mars Colonization Corporation:** Col. Radomir "Anvil" Haskov, Lt. Tamsin "Dustdevil" Orlec and Maj. Veska "Fuse" Roan.
  - **Terra Space Group:** Cdr. Helena "Bastion" Marchetti, Dr. Rafael "Parallax" Quenby and Insp. Aurel "Meridian" Wren.
  - **Galactic Ventures Group:** Capt. Esmé "Tally" Castellane, Ife "Wisp" Adeyemi and Teodor "Glass" Ruskai.
- Each officer has a portrait: a backlit silhouette in their company's colours.
- **Mission Control:** each mission card shows who is offering it, with their portrait, name and role. Rewards waiting to be claimed show it too.
- **Hover a portrait or a name** to see a larger portrait, the officer's role and company, and a line in their own words.
- **Active Quests:** each quest shows its giver's portrait, "From Col. Haskov" (or whoever gave it) and their line under the briefing.
- **Operator Nyx,** who runs Mission Control for every company, now has a portrait in the sidebar. Pilots who haven't joined a company yet get their missions from her.
- Officers' roles and lines are translated into all ten languages. Their names stay the same in every language.

**Pilot profiles**
- Click a pilot in the Hall of Fame (Rankings, or Stats › Hall of Fame) or a name in your clan's member list to open their profile.
- A profile shows the pilot's company, world, clan and rank, level, experience, honor, ranking points and Hall of Fame positions, and how many aliens and pilots they have destroyed.
- It also shows their active loadout: the ship they fly in its 3D preview, every equipped item with its enchant tier and fitted modules, and their combat stats. Hover an item to see its full card with bonuses.
- Active boosters and season buffs are listed with what they add up to, and the combat stats include them the way they work in flight.
- Nothing private is shown: no credits, thulium, inventory, other ships, position or settings.

**Fusion**
- Every item that carries enchant bonuses can be fused: lasers, laser amps, shields, shield cells, engines, thrusters, Adaptive Cores and repair drones. Plain items from the Shop (Standard tier) can be fused too. The Fusion page has a new Repair Drones filter.
- Fusing now keeps the best bonus of each stat across the five items. When the result moves up a tier, every bonus is rolled again in the new tier's range and the better value stays, so a tier-up never gives you less.
- Bonuses only land on stats the item actually has. An Adaptive Core can now roll shield and speed bonuses, and a Crit Amp no longer gets a bonus on damage it doesn't deal.
- Slave and Master Drones can't be fused any more. They carry no bonuses, so fusing them only used up drone slots.
- If one of the items you fuse away holds modules, the Fusion chamber tells you, and the modules go back to your inventory.
- The result screen lists the bonuses of the item you got.

**Item bonuses**
- Every item card (hangar, ship slots, drone slots, Fusion) now lists all the bonuses the item carries, for example "Shield Capacity +3.2% · Absorbance +1.5%".
- Fitted modules show their tier, what they add with their bonuses and their own bonus line, and the "With modules" totals include module bonuses. Hovering the small module markers on a hangar slot shows the module's full card.
- Repair rates read as a percentage per second ("1.38%/s"), and enchanted numbers are rounded to one decimal.

**Thulium and premium**
- Payments will never be pay-to-win. There will only be an optional subscription, and for now it isn't available: the Thulium page says so, and the top bar's button now just reads "Premium".
- Premium you already have keeps running until it ends, and Restore Purchases still works.

**Fixes**
- Enchant tier letters on item tiles no longer fade in and out: the tile's glow still pulses for Rupturing and Eternal items, and the letter stays easy to read.

## 0.3.2 · 2026-09-27

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.3.2)

SpaceCorps 2027 0.3.2 makes text easier to read everywhere: every label, number and button now stands out clearly from what is behind it.

### What's new

**Easier to read**
- The numbers on the hull and shield bars (the target panel, the Ship window and others) are dark over the coloured part of the bar and light over the empty part, so they read at any level. They used to be white on light green and blue.
- The Log In button and every other orange button have dark text now, which reads far better than white did.
- Dim grey text (hints, secondary labels) is a little brighter, and nothing is dimmed below it any more, so locked tabs and empty slots stay legible.
- Name tags and other text drawn straight over space have a soft dark halo, and the version line in the corner of the HUD sits on a small dark plate, so they stay readable over a bright station or nebula.
- Disabled buttons are now a neutral grey instead of a dimmed orange, so they read as "not available right now".
- Every screen was checked with a contrast test in English, Japanese and German.

**Fixes**
- While an update is being verified, its notice no longer shows a stray "0.0" under the progress bar.

## 0.3.1 · 2026-09-27

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.3.1)

SpaceCorps 2027 0.3.1 is a small maintenance update: the game runs on the latest version of its engine. Nothing changes in how the game looks or plays.

### What's new

- The engine's developer panels (F3 overlay and profiler) fit next to each other in a small window instead of overlapping.

## 0.3.0 · 2026-09-26

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.3.0)

SpaceCorps 2027 0.3.0 splits the galaxy into three separate worlds: Alpha, Beta and Gamma. Each has its own copy of every sector, its own aliens and its own pilots. Higher worlds have stronger aliens and pay more for kills and quests.

### What's new

**Three separate worlds**
- Until now, pilots of every tier flew the same sectors and met the same aliens. Your tier only changed your pay and where you could fight. Now Alpha, Beta and Gamma are separate worlds. You fly only in your own world, and you only meet its pilots, aliens and company pilots. Chat and cargo stay in your world too.
- Your account is shared by all three: your items, credits, clan, the season and the leaderboards.
- The HUD shows your world before the sector ("Beta · M-2"). The station and the Dashboard say which world you are in.

**Aliens and pay**

| | Alpha | Beta | Gamma |
|---|---|---|---|
| Alien strength (hit points, shields, shield recharge, damage) | 1.0x | 1.5x | 2.0x |
| Kill and quest pay (credits, thulium, XP, honor) | 1.0x | 2.0x | 3.0x |
| Where pilots can fight each other | only x-4 and 4-x | everywhere but x-1 | everywhere |

- Pay used to be 1.5x in Beta and 2.0x in Gamma. It is now 2.0x and 3.0x, so a higher world clearly earns more per hour, even with stronger aliens.
- A kill pays by the world it happens in. A quest pays by the world you did it in.
- Loot drops and company pilots are the same in every world.
- Safe zones and the Peace Protocol (days 1 to 3) protect you in every world.
- The galaxy map colors the PvP sectors by your world's rules.

**Joining a world and moving**
- A new pilot picks a world at Setup, once per season. The game asks you to confirm first.
- Each world takes up to 1,000 pilots per season. A full world can't be joined.
- You move to another world only at the Blackhole Eruption (day 30), to the destination you pick under Galaxy Gates › Destination. If you don't pick one, you choose a world again at Setup.
- Destinations count against the next season's room, so a full destination can't be picked.
- Every pilot starts the new season at their company's home sector (M-1, T-1 or G-1), also when keeping the same world. So does every change of world.
- A pilot without a world can't pick a destination.
- There is no switching worlds during a season. The Travel Token has no use for now.

**What happens to your pilot with this update**
- You keep the world you picked. Nobody has to pick again.
- **Alpha pilots:** nothing changes.
- **Beta and Gamma pilots:** you are moved once to your company's home sector (M-1, T-1 or G-1) in your world. This way nobody starts among the stronger aliens deep in x-3 or x-4. Your ship, items and everything else stay as they were.
- A pilot without a world picks one at Setup before launching.

**Pages**
- Season › Worlds (it was Server Status) shows each world's pilots this season, how many are flying now, and how many are heading there next season. Your own world is marked.
- The Hall of Fame has a World column and can show one world's pilots (All, Alpha, Beta, Gamma).
- The (i) help cards and the wiki explain the worlds. Everything is translated into all 10 languages.

**Also in this release**
- SpaceCorps 2027 is on Hangar, SpaceCorps' own store: https://hangar.sliplane.app/p/spacecorps/spacecorps-2027. The downloads there are the same files as on the download page.
- A copy installed with Hangar's desktop app is kept up to date by Hangar. Settings › About says so and offers **Open in Hangar** instead of installing updates itself. Copies from the download page keep updating themselves.
- The game runs on the latest version of its engine. The engine's debug overlay (F3) is more compact and stays clear of the HUD.

## 0.2.3 · 2026-09-26

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.2.3)

SpaceCorps 2027 0.2.3 makes shields, shield cells, thrusters and laser amps work the way the item cards say: your absorbance now decides how much of each hit your shields take.

### What's new

**Absorbance decides the damage split**
- Until now every hit went 80% to your shields and 20% to your hull, whatever your absorbance. Now your absorbance is your shields' share of each hit, and the hull takes the rest.
- Your absorbance is the average of your shields, each with the shield cells fitted into it, at most 100%. A Light Shield Core alone is 70%, a Basic Shield Core 80%, a Heavy Shield Core 85%. Shield cells add 2%, 4% or 6% each. A Basic Shield Core with two Advanced cells is 88%, so your hull takes 12% instead of 20%.
- When your shields run out, the hull takes the whole hit, as before.
- Aliens still split every hit 80/20. Company pilots fly two Light Shield Cores, so their hull takes 30%.
- The hangar's combat stats show the split under the tiles ("Each hit: shields 88% · hull 12%"). In flight, the Ship window shows your shields' share on its bottom line, after Speed (hover it for the split).

**Modules**
- Adaptive Cores now take shield cells and thrusters, one per slot, of either kind. Their squares on the hangar board are real slots.
- Clicking a shield cell or thruster fits it into the first shield or engine with room, then into an Adaptive Core. If nothing has room, it goes to an ability slot, and the game now tells you it gives an ability there, not shield stats or speed.
- Only shields take a share of a hit. A shield cell in an Adaptive Core adds shield points, but with no shield equipped they go unused: the hangar says so, and a clicked cell prefers an ability slot on a ship without a shield.
- An item's tooltip lists its module slots, what is fitted and what each module adds, and the item's own totals with them. A module's tooltip says what it fits into.
- A refused fit says why: no free module slot, or the item doesn't take that kind of module.
- Fusing items now works when the items fused away hold modules. Those modules go back to your inventory. The item you keep keeps its own.
- Your modules count in flight exactly as the hangar shows, after a launch, a respawn, a reconnect and a configuration swap. Swapping configurations in flight now also switches Shield Regen and Speed Boost to the new configuration's ability slots, and a booster you add in flight counts at once.

**Balance changes you will notice**
- Adaptive Cores now give their bonuses: AC-I +5% shields and +3% speed, AC-II +8% and +4%, AC-III +15% and +5% (times the slot's share). Before, they added nothing and even halved your absorbance.
- Shields slow your ship again, as the item cards always said: Light Shield Core −1%, Basic −3%, Heavy −5% speed each (times the slot's share). Company pilots fly at 202 instead of 206.

## 0.2.2 · 2026-09-26

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.2.2)

SpaceCorps 2027 0.2.2 is the first version that arrives through the game's own updater. It makes everything you can click show the pointing hand.

### What's new

**The pointer**
- Every button, tab, switch, link, list row and menu shows the pointing hand when you hover it. Many showed the arrow before.
- Buttons drawn over a 3D view get the hand too. These are the wiki viewer's rotate toggle and the hangar's Set active and Revive, which used to show the grab hand.
- In flight, the hand appears over what a click acts on: cargo boxes, the station, ships and aliens. Empty space keeps the arrow. A click just beside a ship still selects it.
- Empty hotbar slots and other drop targets keep the arrow, since clicking them does nothing.
- Disabled buttons keep the arrow.

## 0.2.1 · 2026-09-26

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.2.1)

SpaceCorps 2027 0.2.1 keeps itself up to date, adds an About screen, and fixes the repair drone.

### What's new

**Updates from inside the game**
- New versions download in the background and install when you click **Restart to Update**, or when you quit the game.
- Settings › About has **Check for Updates** and two switches: check automatically, and download and install automatically. Both are on by default.
- The game installs only updates signed by SpaceCorps whose checksums match. It tests a new version before keeping it, and if the new version doesn't start, it puts the old one back.
- During a flight nothing interrupts you. Restart to Update asks first.

**About**
- Settings › About shows the game's version and build, the engine version, the server you play on and its version, and links to the website, release notes and Discord.
- The start screen shows the version in the bottom-left corner. Click it to open About.

**Fixes**
- The repair drone repairs again. Before, it did nothing after a launch until something changed your loadout in flight. Now:
  - the REP slot glows while repairing, counts down after a hit, and is dimmed when the drone is fitted in your other configuration;
  - you get a message when repairs start, stop, finish, are interrupted by a hit, or can't start and why;
  - small hulls repair at the full rate.
- Clicking text no longer leaves the selection following your cursor.
- Switching to another app in the middle of a drag cancels the drag. It no longer drops the item or clicks a button.
- A hotbar slot dragged off the bar is cleared every time, also when the second row was hidden.
- The Discord link points to the community's new invite.

## 0.2.0 · 2026-09-26

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.2.0)

SpaceCorps 2027 0.2.0 brings new graphics, company pilots flying alongside you, cargo to pick up, a new sound system, and the whole game in ten languages.

### What's new

**Graphics**
- HDR rendering with tonemapping and bloom. Engines, canopies and lights on the ships glow.
- GPU particle effects: engine flames and ion trails, explosions with smoke, hull hit sparks and warp effects.
- Settings › Graphics has new Post-Processing and Bloom options. Turn Post-Processing off on older machines.

**In flight**
- Friendly company pilots: small squads of your company patrol the company maps, fight aliens and help you in fights. Your fire never moves onto one of them by itself.
- Cargo drops: alien loot and ship salvage drop into space as cargo boxes. Left-click a box to pick it up. Hover over a box to see what it holds. Boxes show on the minimap and disappear after 3 minutes.
- Ships turn to face their targets.
- Name tags stay steady over the ships.

**Sound**
- A new sound system with original music that follows the fight, and every sound levelled to the same loudness.
- Overload protection: big fights no longer distort, and close explosions dip the music.
- Button sounds can be turned off under Settings › Audio.

**Interface**
- The whole game in 10 languages: English, Svenska, Deutsch, Français, Русский, Español, Português (Brasil), 日本語, 한국어 and 简体中文. Quests, items and server messages are translated too, and Chinese and Japanese text wraps correctly.
- The (i) help cards are translated and name the keys you have bound.
- Key caps show your own keyboard layout (AZERTY, QWERTZ, Dvorak, JIS and others).
- A tighter interface: smaller text and controls, a more compact HUD, target panel and station pages. The hotbar keeps its width in every language.
- An update notice: from this version on, the start screen and the station tell you when a newer version is out.
- Opt-in crash reports: when the game crashes it saves a report on your computer. Turn on Settings › General › Send Crash Reports to send saved reports to the developers. It is off by default, and reports never include your name or a screenshot.
- Delete your account under Settings › Account › Delete account. This asks for your password first.

**Rules (server)**
- PvP points come from player kills only. Alien kills used to count too. Existing points were recounted.
- Rewards are paid by your own tier. A tier you pick in flight applies at once.
- Friendly fire costs honor. Company mates who destroy each other both pay.
- Each tier has its own PvP sectors. The Ship window shows whether you are in a safe or a PvP sector.
- Seekers drop a Ship Fragment about one kill in five.

## 0.1.0 · 2026-09-25

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.1.0)

The first public build of **SpaceCorps 2027**: the SpaceCorps space MMO, rebuilt as a native desktop game. Fly for one of three corporations, fight aliens and other pilots in real time, found or join a clan, craft and fuse equipment, and climb the ranking through a 30-day season. The interface is available in ten languages.
<!-- /patchnotes:list -->
