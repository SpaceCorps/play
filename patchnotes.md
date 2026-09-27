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
