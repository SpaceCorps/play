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
## 0.4.24 · 2026-10-19

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.24)

SpaceCorps 2027 0.4.24 sets four drone formations to the numbers players asked for (Shrike, Centurion, Gemini and Stiletto), draws the Shrike as a crab and the Gemini as a moth, brings the Auger's drill closer to the ship, fires lasers from the guns of each ship's model with a quick burst for the killing volley and a pew for every bolt, and fixes four small edges of the flight HUD.

### What's new

**Highlights**
- **Four formations, the numbers players asked for.** **Shrike:** laser damage to aliens +10 % (was +7.5), XP from alien kills +8 % (was +6), shield absorption -10 % (was -6). **Centurion:** **Honor +25 % on every honor you earn in flight** (it was +32 % of the honor of alien kills). **Gemini:** shield penetration +15 points (was 9). **Stiletto:** no laser penetration any more, **Rocket penetration +35 points** instead (direct rockets only). No price, tier or research moved.
- **The Shrike flies as a crab, the Gemini as a moth,** and **the Auger's drill sits closer to the ship:** its nearest drone passes the hull at 18 units on every ship, where it passed at 27 to 54.
- **Lasers leave the guns of the ship's model.** The Storm fires from its cannons and the ends of its two crescent rings, not from the middle of its hull: nine hulls have a table of gun mounts.
- **The volley that kills is one quick burst (about 0.18 seconds), and nothing is shot at a target that is already dead:** in 0.4.23 the later guns of the killing volley kept firing at the wreck.
- **Every bolt has its own pew** the moment it leaves its gun, not one a second: quieter each, about as loud together as the old one, your own ship first when many ships fire.
- **Four HUD edges:** the Active Quests title is whole, the chat tabs read whole at 1024 x 640, the ammo pop-up no longer covers the Danger Sector callout, and toasts keep off the headers of the Hangar, the Auction, the Clan and Mission Control.
- **Smaller:** a rocket's card prints its penetration with your formation's; the wiki's Formations article is rewritten in 13 languages and the Research and Extras pages are corrected; the 0.4.23 notes' stream figures are corrected on the site; two QA scripts are repaired (for developers).

**If you already play: what changes for you**
- **Update the game.** A 0.4.16 to 0.4.23 game installs a patch when the job made one for it (a Linux AppImage game from 0.4.21), else the whole package; a 0.4.15 or older game downloads the whole package.
- **There is nothing you have to do.** You keep the formations you own and wear. No price, tier or research moved, and no Credits, Thulium or items are paid, moved or removed.
- **A 0.4.23 game keeps working but shows the old numbers:** its cards still say Stiletto "Shield penetration +16 %" and Centurion "Honor from kills +32 %", and its Penetration chip still counts the Stiletto's 16 (the game has the formations file built in). **The server uses the new numbers at once,** so until you update the card is not what you get; the old shapes and laser origin are drawn too. A 0.4.24 game on a 0.4.23 server shows the new numbers, which that server does not apply.
- **The Stiletto lost its laser penetration:** if you wear it to cut through shields with lasers, those 16 points are gone (a laser pierces with its ammo and amps, and with the Gemini's 15 if you wear that); it pierces with direct rockets instead.
- **The Centurion pays less per kill and more elsewhere:** +25 % of the honor you earn in flight, where it was +32 % of the honor of kills. A quest you claim in flight and your share of a group's kill pay it too. It counts once the formation has been worn 10 seconds.
- **The Shrike trades absorption for damage and XP** (-10 % absorption, +10 % laser damage to aliens, +8 % XP); **the Gemini's penetration is 15 points** for lasers and direct rockets.
- **New texts in other languages have had no native review.**

**The four formations: the numbers**
- **Where they come from:** four formations whose numbers players asked for on Discord (2026-10-12). The owner took them up on 2026-10-17 and **ordered them as written, with no retuning**; the rule of 0.4.10 that no formation moves more than 15 points from its first list is lifted for these four.

| Formation | 0.4.23 | 0.4.24 | Not changed |
|---|---|---|---|
| **Shrike** | Laser damage to aliens +7.5 %, XP from alien kills +6 %, shield absorption -6 % | **+10 %, +8 %, -10 %** | tier 1 |
| **Centurion** | Honor from kills +32 % | **Honor +25 %**, on every honor you earn in flight | laser -5 %, hull -5 %, shield -7 %; tier 1 |
| **Gemini** | Shield penetration +9 | **+15** | shield -22 %; tier 3 |
| **Stiletto** | Shield penetration +16 | **no penetration for lasers; Rocket penetration +35** | hull +13 %, shield burn 3.5 % of the current shield a second in a fight; tier 3 |

- **Reading the numbers:** a percentage is a change of your ship's final number, as on the item cards; penetration is in points of the target's shield absorbance. **Nothing else moved:** the other twelve formations, the prices, the tiers, the research, the recipes, the 2 seconds a change takes and the 10 seconds a kill bonus waits are as they were. There is no data step, and existing pilots keep their formations.
- **The model's reading, ours and good for about 0.03 of a net:** the Gemini at +15 is the best single formation (net 1.092) and the Stiletto the weakest (0.916). The Stiletto is the best formation for a duel in which both ships fire the N.I.K.E. (1.46 against the plain ship, the Gemini 1.26) and weak with shop rockets, which are 8 to 24 % of a ship's fire. No number was retuned.

**Centurion: every honor you earn in flight**
- **Which honor it boosts** (+25 % of what is paid, once the formation has been worn 10 seconds, fractions carried so that rounding never loses a point):

| Honor | Boosted? |
|---|---|
| An alien kill: yours (swarm, boss, Warden and Davidski kills too) | **Yes**, +25 % of the kill's honor, in the pot before a group splits it |
| Your share of a group mate's kill | **Yes**, +25 % of your share by your own Centurion, on top of the killer's if the killer wears it too |
| A quest claimed in flight (a level quest, a Station mission, a Challenge) | **Yes**, +25 % of the honor the claim pays |
| A quest claimed while docked (Mission Control in the Station view) | No: a docked pilot has no ship and no formation |
| The Expedition Bay's collect | No |
| A loss (friendly fire, a change of company) and an administrator's grant | No: only gains are boosted |
| A player kill | Nothing to boost: it pays ranking points and no honor |

- **The 10 seconds cover claims too:** a Centurion put on just before a turn-in adds nothing, so swapping in and out around a claim does not farm it. Two pilots of equal level who split a pot of 30 honor are paid 15 and 15 with nothing worn, 19 and 18 with the killer's Centurion, 15 and 18 with the mate's and 19 and 22 with both (the mate's share is 1.25 times 1.25 of its plain one).
- **What it is worth:** hunting Phantasms at level 5 it adds about 249 honor an hour to 995 (+32 % of kills added 319), at level 8 482 to 1,929 (617 before). The quests are new: with it worn, a level's quests claimed once add 129 honor at level 5 and 560 at level 8, and all 116 honor-paying quests of the game add 9,796 honor to a pilot who claims every one with it worn. Honor stays a profile number.

**The Stiletto's rocket penetration**
- **Which rockets:** the **seven direct ones**, the Lancet I, II and III, the Rivet I, II and III and the N.I.K.E. The +35 points are added to the rocket's own; nothing caps the sum, the shield's share of a hit is what is clamped at zero. **Not lasers** (a laser gets nothing of it) **and not the seven area rockets** (Ember, Scatter and the N.U.K.E.): a blast has never pierced a shield, and the model's one-shot rule for the N.U.K.E. would break at 35 points (it would destroy a fresh Ostirion in one hit).
- **Numbers:** a Lancet III has 35 points of its own and 70 with the Stiletto (it was 51 with the old 16), a Lancet I 10 and 45, a Rivet I 5 and 40, the N.I.K.E. 35 and 70; the best direct rocket has 70 points now where it had 51, and the best laser build 61 where it had 62 (the Stiletto's 16 are gone and the Gemini's 15 are the only laser penetration a formation gives).
- **What it does to a hit:** the shields take what the target's absorbance leaves after the penetration. Against the best shield out of the box, which absorbs 80 %, a Lancet III alone puts 55 % of its damage into the hull and with the Stiletto 90 %, 1.64 times the hull damage; a Light Shield Core (45 %) keeps 10 % of a Lancet III's hit and none of it with the Stiletto. Aliens split every hit 80 / 20 less its penetration, so the same holds for them.
- **The cards print it:** in flight a rocket's card shows its penetration with the formation you wear.

**The crab, the moth and a closer drill**
- **The Shrike flies as a crab.** On each side an arm of three drones reaches forward round the nose, the tip curling back in (the claw tips stand 96 units ahead of the nose), one drone sits between the claws ahead of the nose and one behind the ship. With fewer drones the claws grow from their base outward, so an arm never has a gap: 1 drone is the one between the claws, 2 the two bases of the arms, 3 the bases and the one between the claws, 4 bases and elbows, 5 and the one between, 6 the claws whole, 7 and the one between, 8 and the one behind the ship.
- **The Gemini flies as a moth.** Three drones a side ahead of and beside the ship in two rows, a root by the nose, an outer tip far out in its row and a front tip between them a row ahead, and a pair behind the ship as the tail. With fewer drones the wings grow from the root outward and the tail comes last: 1 drone is a single behind the ship, 2 the two roots, 3 the single and the roots, 4 roots and front tips, 5 and the single, 6 the wings whole, 7 the single and the wings, 8 the wings and the tail pair (the tail takes the single's place).
- **The Auger's drill is closer.** Same 25-degree cone, four rings and one turn in 3 seconds, built from the clearance outward: **the nearest drone passes the hull at 18 units on every ship** through a whole turn (it passed at 27 units from the Protos and 54 from the Wraith, 42 from the Paragon), the mean drone is 24 to 53 % nearer the hull, the tip of the cone 44 to 47 % nearer the nose and the widest ring 9 to 36 % narrower. A Paragon with eight drones: nearest drone 42 to 18 units, widest ring 121 to 85, tip ahead of the nose 144 to 79, farthest drone 194 to 128 from the hull's middle. **Why 18 and not less:** the owner's word was closer, not touching; the Drill comes no nearer than the closest other formation does (the Testudo's roof passes at 17, and at 14.4 at the bottom of its bob).
- **The Gemini's card now describes its shape:** it says "Your drones open like a moth's wings" where it said "pair up like twin spears" (the item description in the seed and in all 13 languages); the Shrike's card text is unchanged.
- **The icons of the Shrike and the Gemini draw the crab and the moth** (in the Hangar, the hotbar, the formation picker, the Assembly cards and the wiki); the icons of the other fourteen formations are as they were.
- **What did not change:** a formation's drones glide into their shape in 0.8 seconds and never through the hull; the shapes of the other thirteen formations and of the plain layout are bit for bit as they were (a test pins them). Your game draws other pilots' drones in the same new shapes.

**Lasers leave the guns of the ship**
- **The rule:** a bolt, its muzzle flash and its afterglow leave a **mount of the ship's model**, turned with the ship's heading and sized with how big it is drawn. Through 0.4.23 one formula placed every gun of every ship, 13.2 units ahead of the middle and at most 11 to the side: a Storm's bolts left a spot in the middle of its hull. Now the Storm's guns are its two cannons (35 units out, 50 ahead) and the ends of its two crescent rings (55 out, 8 ahead).
- **Which mounts a ship draws:** one gun is the centre mount, two the first pair, three the first pair and the centre, four both pairs; they fire left, right, left, right. Your ship draws as many guns as it has lasers, two to four; another pilot's ship draws two, its first pair. **The number of guns drawn is the same as in 0.4.23:** the Storm carries 13 lasers and draws four, as it always drew at most four.
- **The mounts**, in hull units (how far out to the side and how far ahead of the model's origin; the hull's half width and the nose are beside the name for scale):

| Ship | Lasers | Half width, nose | Centre mount (ahead) | First pair (out, ahead) | Second pair (out, ahead) |
|---|---|---|---|---|---|
| Protos | 2 | 27.5, 7.5 | 7.4 | 7.05, 7.5 | 27.5, -5.0 |
| Kitefin | 3 | 29.0, 39.9 | 39.9 | 15.4, 21.6 | 28.1, 0.3 |
| Ostirion | 3 | 35.0, 50.7 | 28.5 | 5.7, 50.7 | 13.3, 44.3 |
| Nomad | 6 | 41.5, 47.5 | 37.0 | 25.3, 41.5 | 15.2, 45.0 |
| Paragon | 8 | 36.7, 55.2 | 55.2 | 16.75, 9.6 | 25.5, 36.8 |
| Storm | 13 | 63.8, 65.8 | 62.0 | 35.3, 50.5 | 54.6, 8.0 |
| Ironclad | 6 | 47.1, 58.3 | 57.0 | 41.8, 50.8 | 44.7, 32.8 |
| Wraith | 12 | 35.1, 72.1 | 53.0 | 20.8, 37.0 | 29.7, 14.8 |
| Echelon (no ship flies it) | - | 54.6, 53.1 | 53.1 | 20.1, 25.9 | 10.3, 38.2 |

- **Designs and other shooters:** a ship design draws its base ship's table, except three whose models moved their guns and have a table of their own (Storm NOTSUM, Storm RECON and one Ironclad design). The own ship, other pilots, company pilots and the swarm ships with a pilot's body (the Pirate Boss and its Scouts, the Dormant Force's Paragons, a Wraith) use the table of the model they are drawn with. A model that has no table keeps the old formula, so it still fires.
- **Server, damage, range and timing are unchanged:** it is only how it looks. A Storm's wing-tip bolt flies up to a hull width further than one from the middle, and the series takes that in (four guns at 500 units spread over 0.72 seconds where they took 0.75): the last bolt of a volley lands in time from every mount.

**The volley that kills is one quick burst**
- **What you saw in 0.4.23:** the guns of a volley leave one after another over up to three quarters of a second, and the target stayed drawn for them with its explosion held until the last landed: a pilot saw the damage number, the kill feed and the lost lock and then two or three more bolts hit a ship that was dead for the server.
- **Now** the volley that kills is fired as a **burst: its guns leave evenly over 0.18 seconds** (two guns 0.18 seconds apart, four 0.06), and the target's explosion goes off 0.1 to 0.5 seconds after the volley (0.9 seconds at the most for four guns before). The game knows a volley kills when the server tells the target's explosion after it in the same tick, or when its damage is all the hull and shield the last snapshot showed.
- **No bolt is shot at the dead:** the guns of any other volley still waiting at a target that blows up are let go, with their flash and pew; a bolt already in the air flies on to the wreck and ends there; a volley told for a ship that has already exploded shoots nothing (its damage number still shows). **A killing blow still looks like a hit:** sparks at the end of each bolt, the number and the hit sounds as before.
- **A volley that does not kill keeps the series of 0.4.23:** its guns spread over the second. With 400 bolts in the air a killing volley fires all its guns at once like any other.

**Every bolt has its own pew**
- **What you hear:** a pew per bolt, made where the bolt leaves its gun at that moment, so two to four guns sound like two to four shots spread over the second and in step with the bolts (it was one pew a second, and with a kill the pew had long gone). A gun that is let go makes none, and a killing burst's pews are its bolts' own within 0.18 seconds. Because the pew is made at the gun's place, it comes from that gun's side of a wide ship and moves as the guns alternate.
- **How loud:** quieter each, so that the pews of a volley together carry the old cue's energy and one decibel more: a steady second of your own volleys is within +1.7 and -1.3 dB of the old one (measured through the game's own mixer for all four ammo tiers, **not judged by ear**), and the last three pews of a four-gun burst are 5 to 8 dB under the old cue. No new sample: the bank's three variants of the laser and its pitch jitter make successive pews differ.
- **A crowd does not take yours:** the pews of other shooters are paid out one every 83 milliseconds (12 a second, never more than 2 at once and 13 in any second), the nearest first, so a crowd's pews are spread over the second and not bunched at its start; your own and those at your own ship are never limited and outrank the other laser voices. A volley of one bolt (an alien's single gun) is one pew at its gun, the Siphon Battery's two probes and the laser turrets keep one cue as before, and with Low particles each leaving bolt still has its pew.

**The flight HUD: four edges**
- **The Active Quests title** was cut ("Active Q...") because the quest dots took the title bar's room. The title is measured whole first and the dots fit themselves to what is left, 16 points wide down to 12; where even that does not fit (Russian, Japanese, Spanish and Hungarian at 1280 x 720, and every language at 1024 x 640 with seven quests) they stand in a row of their own at the top of the window, nothing cut. The title is whole in all 13 languages at both sizes; the window's default width stays 300. At 1024 x 640 the body then shows about 20 points less of the quest, which scrolls.
- **The chat tabs** read whole at the chat window's default width of 1024 x 640 in every language: Russian and Japanese letters are set a little smaller (10.5 or 10 points instead of 11.5). A window you made as narrow as it goes in Russian still scrolls its tabs, with an arrow at each end to say so.
- **The Danger Sector callout, the excavator's gauge and the channel bar** stand on top of an open ammo or rocket pop-up instead of under it. At 1280 x 720 nothing is covered (English, German and Japanese looked at); at 1024 x 640 the card stands over what is above the pop-up (the lower rows of the Group window, and with the tall Rockets list the Boosters window's text and the bottom of the Target window).
- **Toasts** no longer sit on the header of a window: the Hangar's inventory header (its title, the count, the selection's buttons), the Auction's first row (the four sections, the slots and Sell), the Clan's header and Mission Control's page heading with the first section's counters (the missions' "0/5 active" and the Station's "0/3"). The stack starts under them and covers what comes below (the Hangar's category chips, the right end of Mission Control's first mission). **Only those windows are asked:** a toast can still cover another window's header.
- **Contrast:** the Target window's "Immune" tag is 4.59:1 (it was 4.44) and the count of a switched-off filter chip in the Hangar's inventory row is over 4.5 (it was 3.5). In our contrast audit of the flight HUD (17 stops, 1280 x 720 in English) 15 of 2,364 text runs failed 4.5 in 0.4.23 and 2 of 2,359 fail now, none on a window: the excavator's name fading out and a rock's name tag (4.38 to 4.40) drawn over the dark scene.

**For administrators and the server**
- **At the first start:** **no schema change** (the backup gate prints nothing), **no data step**, no new table, column, route, message, client feature string or environment variable. **One data file changed,** `Formations.json` (the numbers above, the key `killHonorPct` renamed `honorPct` and the new `rocketPenetration`: 18 keys), and three item descriptions in the `items.json` seed (Gemini, Stiletto and Centurion), which the start syncs by name. A file of 0.4.23 with the old honor key still loads on a private server.
- **Two new counters, both with a label:** `formation_honor_paid{source}` (the whole honor points the formation added: `kill`, `quest` or `group`) and `formation_honor_dwell_misses{source}` (a quest claim or a group share that came before the 10 seconds were up).
- **A database from 0.4.23 starts on 0.4.24** with no ERROR line, and a Stiletto and a Centurion pilot load and wear their formations (the lanes' scratch runs, `scripts/qa-0424-formations.py`).
- **There is no switch for the formations' numbers:** a change is a release (`Formations.json` is written by `docs/design/formations-model.py`). The look and the sound of the lasers, the shapes and the HUD are the game's, not the server's.
- **Rolling back to 0.4.23:** a 0.4.23 server refuses to start on the new `Formations.json` (it does not know `rocketPenetration`), so the file and the server go back together (the image carries both); the database has nothing new, so a rollback loses nothing a pilot did, and what honor a Centurion paid stays paid. No volume backup is needed (the gate prints nothing). If a formation's numbers are wrong, the way is a fix release (docs/DEPLOY.md).

## All releases

Each line links the full notes of that release as Markdown (patchnotes/v<version>.md); its HTML page is patchnotes-v<version>.html.

- [0.4.24](https://spacecorps.github.io/play/patchnotes/v0.4.24.md) · 2026-10-19 · Sets four drone formations to the numbers players asked for (Shrike, Centurion, Gemini and Stiletto)…
- [0.4.23](https://spacecorps.github.io/play/patchnotes/v0.4.23.md) · 2026-10-18 · Redraws the station as floating islands, adds 19 Pilot technologies and the Auto-Rocket CPU…
- [0.4.22](https://spacecorps.github.io/play/patchnotes/v0.4.22.md) · 2026-10-15 · Adds Turkish as the 13th language, makes the P.E.T.
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
