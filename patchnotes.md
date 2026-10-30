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
## 0.4.27 · 2026-10-30

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.27)

SpaceCorps 2027 0.4.27 puts two repair ships at every company base, lets every docked Mole mine, shows a pilot's title above their name on the map, counts the clan's and the P.E.T.s' boosts in the Boosters totals, and makes the Trophies Bay count loot only. Rockets blast 50 % wider (the N.U.K.E. over 1,350 units), the Ammo Printer and the Rocket Factory make twice as much, the Ironclad costs 100 Reinforced Hull Plates, not 450, Excavator Mining enlarges the boxes of the run its owner starts, and two quests drop a P.E.T. chunk.

### What's new

**Highlights**
- **Two repair ships at every company base.** They hover just outside the safe ring of Mission Control and **heal every pilot of the base's company within 2,000 units by 250 hull a second each** (a pilot in reach of both gets 500), also in combat. **They are real ships: enemy pilots and aggressive aliens can shoot them down,** and each is back on its post 120 seconds later. A ring on the map shows the reach; the Target window says "Repair ship".
- **Every docked Mole mines,** up to five, each on a rock of its own with its own beam and drone. More Moles now mean more mining income.
- **Titles over names.** The title a pilot wears stands in small, dim type in its rarity colour above their name on the map, yours too. In a crowd (more than eight plates) the titles of strangers are hidden and only names show.
- **Boosters count the clan and the P.E.T.s.** The Boosters window and the Dashboard card now list the clan's and the docked P.E.T.s' boosts as lines of the category they raise (Damage, Shield, Credits, Luck ...), so **a category's total is what your ship gets.**
- **Rockets blast 50 % wider** (damage unchanged): Ember 255 / 345 / 450, Scatter 315 / 435 / 600 and the **N.U.K.E. over 1,350 units** (900 before). The Dormant Swamp's turret fires the same N.U.K.E.
- **The Trophies Bay counts loot only.** A kill's Credits, Thulium, experience and honor take no room in the Bay any more; the "Bay full" notice shows the moment it fills, also while the Skylab is under way. **The Bay therefore fills far more slowly** (Bay 1 at Defense level 3 in about 15 hours, Bay 20 in about 44 days).
- **Skylab:** the **Ammo Printer and the Rocket Factory make twice as much** at every level. The Universe window no longer says "Planning the trip..." while the Skylab is flying: it shows where it is heading and when it arrives.
- **Smaller:** the **Ironclad** (both designs) costs **100 Reinforced Hull Plates**, not 450; **Excavator Mining** enlarges every box of a run for whoever picks the boxes up, by the research of the pilot who started the run; **Hive Breaker** and **Iron Tide** also drop a **P.E.T. chunk** (a Regular and a Mythical Cluster Chunk, on the first claim only); new pilots start with the **REP button** in hotbar slot 2; the **Production Queue's time left no longer flickers.**

**If you already play: what changes for you**
- **Update the game.** A recent game installs a patch when the job made one for it, else the whole package; an older game downloads the whole package.
- **The update itself pays, moves and removes no Credits, Thulium or items.** Nothing you own changes, except the Ironclad's price for the next one you build.
- **The server uses the new numbers at once,** for every version of the game: the wider blasts, the repair ships, the Moles, the Bay's rule, the Skylab output. **A 0.4.26 game keeps working but shows the old screens:** the clan's and the pets' boosts on cards of their own, no title above names, the Bay card with its old labels, one beam for your Moles, and the repair ships as company pilots. It also draws a **Scatter III blast like a N.U.K.E.** (flash and shock ring), because its size test is 600 units and Scatter III now reaches exactly that.
- **Moles:** if you dock several, all of them work now. Your mining income grows with them; the Station's rooms (2, 3 and 5) still decide how many you can dock.
- **Excavator Mining:** the research counts for **the pilot who starts the run,** and the boxes of that run are larger for everyone who picks them up. A pilot who picks up boxes from someone else's run no longer gets a bonus from their own Excavator Mining.
- **A Bay that was full under the old rule may have room now:** one test Bay that held 650 bounty points, full under the old rule, reads 60 of 650 loot units. A trip under way carries on under the new rule from its next look; nothing is lost.
- **The Dormant Swarm:** the leftover Pulses leave 30 seconds after the Force dies, and the swarm returns on schedule. The Force's "destroyed" line comes with the despawn, up to 30 seconds after the kill line.
- **New texts in other languages have had no native review.**

**Company base repair ships**
- **Where:** two at each company base (`x-1`) in Alpha, Beta and Gamma, 9 bases in all, on posts 1,904 units from Mission Control, outside the safe ring of 1,600. They are company pilots to the game: the rules for PvP, honor, safe zones and kill lines apply, and **killing one is a kill of a company pilot.**
- **What they do:** the aura heals every pilot of the base's company, and the company's own squad pilots, within 2,000 units by 250 hull a second each, never above the maximum. A rival company gets nothing.
- **How hard they are to kill:** a hull of 200,000 and a shield of 100,000. Aggressive aliens go for them like for a pilot.
- **All the numbers are in one file,** `server/Resources/BaseRepair.json`; a wrong file stops the server's start.

**Moles**
- **One beam each:** the server names each Mole by its place among your docked P.E.T.s, and the game keeps a beam and a drone for each place. A game before 0.4.27 reads only the strongest Mole.
- **Rocks:** a pilot's Moles never share a rock. `traits.mining.workers` (now 5) is the lever that limits how many work.

**Titles over ships**
- **How the game knows:** the map's compact snapshot carries no title. The game asks the server for the pilots in view that it does not know, at most once a second and 50 at a time (`GET /api/titles/of?ids=`), and keeps the answers for a few minutes. Past 120 asks a minute from one pilot the server answers *try again later* and the game shows nothing meanwhile.
- **Cut:** a title is cut at 24 characters.

**The Trophies Bay and the Skylab**
- **The rule:** a kill puts in the Bay the loot units its mix brings on average; Credits, Thulium, experience and honor are paid by the budget as before and take no room. **The capacities are the same numbers as before, now in loot units,** and a kill's loot is far smaller than its bounty, so the Bay lasts about ten times longer. **Income an hour is unchanged;** what changes is how long a Skylab can stay out before it holds fire.
- **Old rows:** nothing is migrated. The Bay's load is read off its items; a row written before 0.4.27 says bounty points in its `Load`, which is read past.
- **Fill times** (a Skylab firing at its own tier's budget):

| Defense level | Bay 1 | Bay 5 | Bay 10 | Bay 15 | Bay 20 |
|---|---|---|---|---|---|
| 1 | 2 d 9 h | 5 d 20 h | 17 d 13 h | 54 d 20 h | 164 d 11 h |
| 3 | 15 h 13 min | 1 d 13 h | 4 d 16 h | 14 d 15 h | 43 d 22 h |
| 5 | 12 h 13 min | 1 d 6 h | 3 d 18 h | 11 d 18 h | 35 d 6 h |

- **The printers:** the Ammo Printer and the Rocket Factory make twice as much at every level (storage stays 24 hours). A Skylab on an expedition fires at the rate its printer supplies, so it can fire for longer.

**Rockets**

| Rocket | Blast radius, 0.4.26 | 0.4.27 |
|---|---|---|
| Ember I / II / III | 170 / 230 / 300 | **255 / 345 / 450** |
| Scatter I / II / III | 210 / 290 / 400 | **315 / 435 / 600** |
| N.U.K.E. | 900 | **1,350** |

- **Damage, speed, lock and price are unchanged.** A wider blast hits more ships, hardest at the centre as ever; the area rockets still do not pierce shields. The N.U.K.E.'s ring on the map runs out to 1,350.

**Smaller changes**
- **Excavator Mining** is a Pilot research of the Research Centre: it now enlarges every box of a run its owner starts (the share rides above the per-run cap and is saved with the run), so a run started by a pilot with the research pays the pickers more.
- **The REP button** is the starter Repair Drone in primary slot 2 (next to x1 in slot 1) for **new accounts only;** pilots who exist keep their hotbars.
- **Wiki:** the generated parts of the wiki are updated in 13 languages. Pages about Achievements, Asteroid Mining, Clans, Pets, Boosters, Company Pilots, Skylab, Getting Started, Giant Excavator, Quests, Research, Ship Designs, Extras and Rockets were rewritten in English; their translations are older until they are translated again.

**For administrators and the server**
- **Release order:** the release job stages the downloads as a draft GitHub release (nobody can see it) and the Windows build on Steam's private branch before the server deploys, then publishes the draft as soon as `/health` reports the new version, so the server and the downloads go live together. `AUTORELEASE_STAGE=0` gives the old order. (`docs/DEVELOPMENT.md`, "Releases".)
- **Achievements payout:** the veterans' achievements unlocked by the 0.4.26 backfill carried no reward. `POST /api/admin/achievements/backfill-pay {pay: bool}` pays them once, only the rows the backfill wrote; with `pay: false` it only counts. It is run by an administrator after a dry run, not by the release.
- **Admin quest tools:** an administrator can read a pilot's quest state and count a quest as done. The pilot then claims the reward in the game as usual.
- **Containers in bonus codes:** a bonus code can give containers (1 to 1,000 of each) with the rest of its reward; they are given in the same step as the claim and show in the claim's answer. A code whose container the server no longer has cannot be claimed and gives nothing.
- **Containers and skins in the admin tools:** the Resources tab has a card to give a container, a skin, a colour, an effect or a collection to a pilot, and the pilot's Inventory sheet has the same as a second Add row.
- **The release job** builds without build paths in the binaries, uses a real Python on Windows and looks the macOS build up from GitHub's runner.
- **Tests:** the server has new tests for the repair ships (14), the title lookup, the Moles, the Bay, the payout and the Excavator; the game has new tests for the plates, the clock and the beams.

## All releases

Each line links the full notes of that release as Markdown (patchnotes/v<version>.md); its HTML page is patchnotes-v<version>.html.

- [0.4.27](https://spacecorps.github.io/play/patchnotes/v0.4.27.md) · 2026-10-30 · Puts two repair ships at every company base, lets every docked Mole mine, shows a pilot's title above their name on the map…
- [0.4.26](https://spacecorps.github.io/play/patchnotes/v0.4.26.md) · 2026-10-29 · Rebuilds the Universe Wipe and adds what it pays out: the next wipe keeps every ship, your drones, formations, P.E.T.s and P.E.T.
- [0.4.25](https://spacecorps.github.io/play/patchnotes/v0.4.25.md) · 2026-10-22 · The release the first Universe Wipe runs under: the wipe keeps every ship you own and takes your items…
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
