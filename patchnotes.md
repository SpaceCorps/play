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
## 0.4.20 · 2026-10-10

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.20)

SpaceCorps 2027 0.4.20 is the Ore Bay and the longer sign-in update: ore from a giant excavator can finally be moved into your Skylab, the game renews your sign-in while you play, the Wrath Wardens chase and call bigger waves, aliens fly round asteroids instead of into them, the Auction lists for 7 to 21 days with ten free listings a day, and the giant excavators lay twice as much.

### What's new

**Highlights**
- **The Ore Bay: a new Skylab module for the ore you carry.** Built on Core 2 from Core level 10 (5,000 Credits, 250 Thulium, 10 Ship Fragments): park your ship and it moves the Velkonite and the Orvium of your inventory, an excavator's boxes included, into the Resource storage, where the Forgery and the Research Centre take them. It moves 10 ore an hour at level 1 and 320 at level 20 and keeps a day of it; ore only goes in.
- **The giant excavators lay twice as much** of every resource (a run of Thulium is 9,643 in Alpha, it was 4,821); a run of Velkonite or Orvium is capped at 8 hours of a level 20 collector (4 before). The Star System map marks every Danger Sector's excavator in its state's colour, and the pulsars shine from the first day.
- **You are not signed out in the middle of a flight any more.** The game renews your sign-in at the start, every hour and when your computer wakes; it ends 30 days after you typed your password. **A 0.4.19 game cannot renew its sign-in until it updates.**
- **The Wrath Wardens chase** the pilot who hit them, so shooting one from afar is not free any more. **The Wrath Warden III calls a wave every 40 seconds (60 before), up to four at once (three), of 8, 15 and 15 aliens (5, 10 and 10), and every wave holds a Crystalys while it has less than half its hull.** What a Warden brings arrives aimed at its attackers. **The Brood Warden still stands where it was called.**
- **Aliens and company pilots fly round asteroids** and no longer shoot the rock you hide behind: they go round to see you. The Dormant Lances of the swamp's Inert Masses damage asteroids.
- **The Auction lists for 7, 14 or 21 days, the first 10 listings of every UTC day pay no deposit,** a chart shows what the other pilots ask for the same item, and **3 lots an hour** open instead of 1.
- **The Forge's list has an All / Equipped / In inventory switch** and shows the pieces fitted into other items. **A rewarded Engine II or III, or Adaptive Core II or III,** (a code, a quest, an invitation, an administrator) **comes with its research.**
- **Smaller:** the pulsar is remodelled as a neutron star, the excavator's hum swells once in the 4 seconds the pulsar takes to turn, and a laser that a rock stops ends at the rock's edge.

**If you already play: what changes for you**
- **Update the game.** A 0.4.12, 0.4.13, 0.4.14, 0.4.15, 0.4.16, 0.4.17, 0.4.18 or 0.4.19 game installs it as a patch (a Linux AppImage game from 0.4.14), and downloads the whole package if the patch cannot be used. A 0.4.11 or older game downloads the whole package.
- **The rules change on the server at once:** the Wardens, the aliens and the rocks, the excavators' output, the Auction's times, deposits and lots, the sign-in's renewal and the Ore Bay's route. A 0.4.19 game keeps working under them but cannot renew its sign-in, and it lacks what is new on the screen: the Ore Bay's card, the star map's marks, the chart and the free listings, the Forge's switch.
- **Nothing you own is taken, and no Credits, Thulium or items are paid, moved or removed.** Solar makes 35 to 100 more power from Core level 10 on (17,990 at level 20, it was 17,890) for the Ore Bay's draw, so a full station is covered as before; the producers that were dark under the old table resume from the start.
- **Your rewards from now on count:** an Engine II or Adaptive Core piece given to you after this update comes with its research. A reward of a rocket does not unlock its craft.
- **A listing you made keeps the days you chose** (1, 3 or 7 days before), and the lots that are open keep their price; the extra lots begin at the next hour.

**The Ore Bay**

| Level | 1 | 5 | 10 | 15 | 20 |
|---|---|---|---|---|---|
| Ore it moves an hour | 10 | 30 | 80 | 174 | 320 |
| A day of it, kept | 240 | 720 | 1,920 | 4,176 | 7,680 |
| Power | 15 | 22 | 35 | 57 | 92 |

- **What it moves.** Velkonite and Orvium, the two ores the Resource storage keeps; never what is in your Transport Cache. Cataclysite and Quorvium are fuel that the Research Centre and the Forge take from your inventory, and Thulium goes to your wallet when you pick it up.
- **How.** Your ship must be landed. Choose the ore on the Ore Bay's sheet, type an amount or press Max, and press Move: a transfer is instant, and it is cut at the ore you carry, at the room the Resource storage has left and at the allowance, and the sheet says which. A new Ore Bay starts with a full day and an upgrade keeps what was stored. It has a quiet sound of its own.
- **What it costs.** Its upgrades cost and take what the Resource storage's do (to level 10: 619,500 Credits and 359 Thulium with the build). It draws power and can be switched off; in a blackout it moves nothing.

**The giant excavators**
- **Twice the output.** Per run in Alpha, Beta and Gamma: Thulium 9,643, 15,429 and 19,286; Cataclysite 2,314, 3,703 and 4,629; Quorvium 1,029, 1,646 and 2,057; Velkonite 640 and Orvium 320 in every world. Fuel, heat, hull, waves and Voids did not change.
- **The ore of a box** goes into your cargo as before. The Forgery and the Research Centre take Velkonite and Orvium from the Resource storage only, so the Ore Bay is the way in.
- **Pulsars from day 1.** A pulsar shines on DS-1, DS-2 and DS-3 from the first day of the season and nothing else of the excavator exists before season day 11: no panel, no radiation, no boxes, no Voids. Rocks keep out of the pulsar's disk from day 1.

**The Wardens and the rocks**
- **What a Warden does when it is hit.** The three Wrath Wardens fly at the first pilot who hit them and stop in their laser's range (700, 800 and 900 units); the Siege Wardens keep roaming and fire their rocket; the Brood Warden fights in place, as its drones heal it. The Wrath Wardens are harder to farm from range for that reason.
- **What a Wrath Warden III sends.** The smallest crew of its gear that wins on x2 ammo is 31 pilots on x-2, 32 on x-3 and 38 on x-4 in the model's best case (26 before the waves); a level 3 clan holds 50. A whole wave pays 24,000, 45,000 or 75,000 Credits in Alpha to whoever kills it, and a Crystalys 75,000 Credits, 200 Thulium, 12,000 XP and 52 honor; the Wrath Warden III itself pays what it paid.
- **Rocks.** An alien's body stays out of a rock's circle with its hull and a little more; a wave and a Warden's crew are not made inside a rock. A laser of an alien is not fired at a rock at all, and a rocket of an alien that a rock stops takes nothing off it. The Dormant Lance of an Inert Mass takes its own damage off the rock it meets, and nobody is paid for it.

**Signing in**
- **What is renewed, and when.** The game asks for a new token at the start, every hour and the moment your computer wakes; the server also renews a token an hour old on any call. A token lives 24 hours from its last renewal and 30 days from the sign-in with your password, never longer.
- **Two games on one computer** keep their own sign-in and stop overwriting each other's remembered one; closing the second game, or docking, no longer shows you Offline to your group for a moment.
- **Changing a password** gives that game a fresh token and ends the other sessions of the account within the hour.

**The Auction**
- **7, 14 or 21 days.** The deposit is 0.25% of the price for each 24 hours the listing runs (0.4% from level 10), a quarter of what it was in 0.4.19 (1%; 1.5% from level 10): 1.75, 3.5 and 5.25% for 7, 14 and 21 days (2.8, 5.6 and 8.4% from level 10). A listing that the season's end shortens pays for the hours it actually runs. The first 10 listings of each UTC day, counted from the day's start whether they sell, expire or are cancelled, pay no deposit; the 5% sale tax is as it was.
- **The chart.** It shows the asking prices of the other pilots for the same item and enchant in the currency you chose, with your own price as a line and the cheapest, the median, the least price and the last sale marked; with fewer than three other listings it is a plain list. It never shows who sells.
- **Three lots an hour** (a table of 72 for the day, each hour one lot of x2 ammo, one of x3 ammo or EMP Charges and one of rockets). Twelve are open at once and the board lists the last 36 results.

**What you see and hear**
- One new quiet sound (the Ore Bay's transfer) and every new text in 12 languages.
- The Forge's filter says how many pieces it hides, and choosing a merge's donor is never blocked by it.

**For administrators and the server**
- **At the first start:** one data step (`skylab-solar-v5`, which brings every Skylab up to the start under the 0.4.19 power table and then applies the new one) and no schema change: the backup gate lists that one line. Six data files change (`SkylabConfig.json`, `Excavator.json`, `ClanWardens.json`, `ClanLines.json`, `Market.json` and `Auction.json`), none is new, and the seeder adds nothing. Three new routes (`POST /api/skylab/bay/transfer`, `GET /api/market/spread` and `POST /api/auth/refresh`) and one new hub message (`ExcavatorSectors`, sent to games that announce `dormant-ds`). A token now carries two more signed claims and the answer to any call may carry an `X-Refreshed-Token` header. No new environment variable, client feature string or dependency.
- **Rolling back to 0.4.19** is the job's code-only rollback; lots that are open with a held maximum have the proxy-bid hazard of 0.4.19 (docs/DEPLOY.md).

## All releases

Each line links the full notes of that release as Markdown (patchnotes/v<version>.md); its HTML page is patchnotes-v<version>.html.

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
