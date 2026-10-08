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
## 0.4.15 · 2026-10-08

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.15)

SpaceCorps 2027 0.4.15 is the Skylab update: when your Core reaches level 10 a bridge builds a second Core with six module seats, and two new modules, the Ammo Printer and the Rocket Factory, plug into it. The Quantum Laser III is now crafted from a Quantum Laser II, and the Ship window shows your Penetration.

### What's new

**Highlights**
- **A bridge and a second Core at Core level 10.** The Core's step from level 9 to 10 costs 2,000 Thulium on top of its 38,443 Credits. When it finishes, a bridge builds Core 2 with six module seats and the Solar Array moves to Core 2's far end. The Skylab page draws it and labels the free seats; a quiet sound and a toast tell you when the bridge is built.
- **New module, the Ammo Printer** (levels 1 to 20), prints laser ammo from nothing: x2 (Advanced Plasma) 100 an hour at level 1 and 2,000 at level 20, x3 (Ultra Core) half of that, x4 (Experimental Fusion Core) a quarter. You pick one at a time.
- **New module, the Rocket Factory** (levels 1 to 20), builds any of the twelve Shop rockets (Lancet, Rivet, Scatter and Ember, tiers I to III): a tier III rocket 0.5 an hour at level 1 and 10 at level 20; tier II is 1.25 times as fast, tier I twice.
- **Both are 3D modules on Core 2:** five looks over their 20 levels, scaffolds and drones while they upgrade, and a sheet with the mode, storage, Collect and Upgrade.
- **Fix:** the Quantum Laser III is crafted from a Quantum Laser II (a Shop item) besides 10 Ship Fragments, 2 Velkonite Reinforced Plates and 1,500 Thulium. Its least price in the Auction rises to 210,000 Credits (170,000 before), the Starfire-III's to 470,000 (430,000).
- **The Ship window shows your Penetration.** A fourth chip, after the shields' share, reads the laser amps' share of the configuration you fly in whole percent: the number the Hangar's Penetration tile shows (0% without a Penetration Amp; it follows a configuration swap). To make room the Config and Speed chips show their icon and number only; hover them for the names. The tooltip says what penetration is and that a hit is capped at 50% for lasers and 40% for rockets.

**If you already play: what changes for you**
- **Update the game.** A 0.4.12, 0.4.13 or 0.4.14 game installs it as a patch, and downloads the whole package if the patch cannot be used. A 0.4.11 or older game downloads the whole package.
- **At Core level 10 or higher you have the bridge and Core 2 at your next look,** free. Nothing is stored for them; the Solar Array keeps its level, power and upgrade.
- **The 2,000 Thulium is paid by the step into level 10 only:** an upgrade already running keeps its price, and a Core at level 10 or higher pays nothing.
- **Solar makes more power from level 7** (965 at level 7, 17,890 at level 20; levels 1 to 6 as before), so a full station stays covered. At the first start a producer that stood dark for want of power under the old table, and is powered under the new one, runs again from then; the dark time is not counted. Nothing that ran stops.
- **The new recipe applies to crafts you start after the update;** a craft under way is not changed, and open listings keep their price.
- **The Ship window's Penetration chip needs the update, not a server change:** the number is the one the Hangar's tile already gets from the server.
- **A 0.4.14 game keeps working but draws the plain old station:** no bridge or Core 2, the Solar Array on Core 1, and no card for the Printer or the Factory, so it cannot build, switch or collect them. The step into level 10 shows 2,000 Thulium and works. Update before you build.

**The Ammo Printer and the Rocket Factory**
- **Build.** Both stand on Core 2 (Printer north-east, Factory north-west), so you build them from Core level 10; before that the Build button says "Needs Core 2". A build costs 20,000 Credits, 500 Thulium and Ship Fragments (10 for the Printer, 15 for the Factory). Their levels follow your Core's. All 19 upgrades: Printer 22,011,000 Credits and 47,440 Thulium, Factory 5,527,300 and 11,994.
- **Storage and Collect.** A module keeps up to 24 hours of what it makes, offline hours too, and stops when full; switching the mode counts the hours stored at the new mode's rate. Collect with your ship parked, in whole units: ammo has no carry limit, a rocket stops at your carry stack and the rest stays. What they make cannot be listed in the Auction. They draw Solar power and can be switched off.

**For administrators and the server**
- **At the first start:** one new table (`SkylabProduction`, empty) and one data step (`skylab-solar-v4`); the backup gate prints 2 lines. The bridge needs neither. Three data files change; the new route is `POST /api/skylab/mode/:type/:mode`. No new counter or environment variable.

## All releases

Each line links the full notes of that release as Markdown (patchnotes/v<version>.md); its HTML page is patchnotes-v<version>.html.

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
