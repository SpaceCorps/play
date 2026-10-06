---
title: "SpaceCorps 2027 · Download"
description: "Download SpaceCorps 2027, a space MMO for macOS, Windows and Linux: fly for a corporation, hunt aliens with your clan and climb the season ranking."
canonical: "https://spacecorps.github.io/play/"
publisher: "SpaceCorps"
license: "Proprietary client, Free to play"
engine: "Space3d Engine"
# release:front
version: "0.4.11"
date: "2026-10-06"
server: "https://spacecorps-game.sliplane.app"
platforms:
  - os: "macOS"
    arch: "universal (Apple Silicon & Intel)"
    format: "dmg"
    filename: "SpaceCorps2027-macos-universal.dmg"
    size: 133975864
    sha256: "edb976b5c6e6692accb4b6c7997befeaf4013cc25d187d07877284eb379ab3e3"
    url: "https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-macos-universal.dmg"
  - os: "Windows"
    arch: "x86_64"
    format: "zip"
    filename: "SpaceCorps2027-windows-x86_64.zip"
    size: 128417513
    sha256: "da074f723dbfd5ebc16d44d68ea5f39bf3c7be0c333b54a4849705c4fc04871e"
    url: "https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-windows-x86_64.zip"
  - os: "Linux"
    arch: "x86_64"
    format: "appimage"
    filename: "SpaceCorps2027-linux-x86_64.AppImage"
    size: 124107256
    sha256: "feeded82801029d9137f5ab0d180632572442e129f1fdafb9979801e42fda1f0"
    url: "https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-linux-x86_64.AppImage"
  - os: "Linux"
    arch: "x86_64"
    format: "tar.gz"
    filename: "SpaceCorps2027-linux-x86_64.tar.gz"
    size: 129219571
    sha256: "df3d8d5bd32ed0cf9309f19a1e320226d0d449340e1b8f9ab6b6bb117f65c29a"
    url: "https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-linux-x86_64.tar.gz"
# /release:front
---

# SpaceCorps 2027 · Downloads & System Guide

SpaceCorps 2027 is a multiplayer space action simulator built on the native Space3d engine for macOS, Windows, and Linux. Choose a corporation, customize your starship, coordinate tactical strikes with your clan, hunt alien incursions, and compete for seasonal leaderboards.

- Canonical URL: [https://spacecorps.github.io/play/](https://spacecorps.github.io/play/)
- Machine Interface: [llms.txt](https://spacecorps.github.io/play/llms.txt) | [llms-full.txt](https://spacecorps.github.io/play/llms-full.txt)
- Release Manifest: [release.json](https://spacecorps.github.io/play/release.json)
- Patch Notes: [patchnotes.md](https://spacecorps.github.io/play/patchnotes.md) | [patchnotes.json](https://spacecorps.github.io/play/patchnotes.json)
- GitHub Releases: [https://github.com/SpaceCorps/play/releases/latest](https://github.com/SpaceCorps/play/releases/latest)
- Discord Community: [https://discord.gg/VjW67tkrTb](https://discord.gg/VjW67tkrTb)

---

<!-- release:downloads -->
## Downloads (Version 0.4.11)

| Operating System | Architecture | Package Format | Download Link | SHA-256 Checksum |
| :--- | :--- | :--- | :--- | :--- |
| **macOS** | Universal (Apple Silicon & Intel) | `.dmg` (134.0 MB) | [SpaceCorps2027-macos-universal.dmg](https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-macos-universal.dmg) | `edb976b5c6e6692accb4b6c7997befeaf4013cc25d187d07877284eb379ab3e3` |
| **Windows** | x86_64 | `.zip` (128.4 MB) | [SpaceCorps2027-windows-x86_64.zip](https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-windows-x86_64.zip) | `da074f723dbfd5ebc16d44d68ea5f39bf3c7be0c333b54a4849705c4fc04871e` |
| **Linux** | x86_64 | `.AppImage` (124.1 MB) | [SpaceCorps2027-linux-x86_64.AppImage](https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-linux-x86_64.AppImage) | `feeded82801029d9137f5ab0d180632572442e129f1fdafb9979801e42fda1f0` |
| **Linux** | x86_64 | `.tar.gz` (129.2 MB) | [SpaceCorps2027-linux-x86_64.tar.gz](https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-linux-x86_64.tar.gz) | `df3d8d5bd32ed0cf9309f19a1e320226d0d449340e1b8f9ab6b6bb117f65c29a` |
<!-- /release:downloads -->

---

## What's New

The latest release's patch notes (in English). Every release: [patchnotes.md](https://spacecorps.github.io/play/patchnotes.md) · [patchnotes.html](https://spacecorps.github.io/play/patchnotes.html)

<!-- patchnotes:latest -->
### 0.4.11 · 2026-10-06

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.11)

SpaceCorps 2027 0.4.11 makes ranks per company, draws the drone formations as shapes round your ship, gives the Group window a new layout, makes Unequip all take the equipment off your drones too, and sets the PvE points of the swarm aliens and Clan Wardens by their toughness like the older aliens (their kills already counted; only the figures change). Your rank is now your place among the pilots of your company: the best pilot is its only Senior Admiral (20,000 PvE points at least), the others follow by place, and each rank needs a minimum of PvE points. Each of the 16 formations places your drones in a pattern of its own, other pilots see it, and the Auger is a cone with its tip ahead of your ship. Your rank can go down now, and many ranks will at the first start: read "If you already play".

#### What's new

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
<!-- /patchnotes:latest -->

---

<!-- release:checksums -->
## Checksum Verification

Verify the integrity of downloaded binaries prior to execution:

### macOS
```bash
shasum -a 256 SpaceCorps2027-macos-universal.dmg
# Expected: edb976b5c6e6692accb4b6c7997befeaf4013cc25d187d07877284eb379ab3e3
```

### Windows (PowerShell)
```powershell
Get-FileHash SpaceCorps2027-windows-x86_64.zip -Algorithm SHA256
# Expected: da074f723dbfd5ebc16d44d68ea5f39bf3c7be0c333b54a4849705c4fc04871e
```

### Linux
```bash
echo "feeded82801029d9137f5ab0d180632572442e129f1fdafb9979801e42fda1f0  SpaceCorps2027-linux-x86_64.AppImage" | sha256sum -c -
```
<!-- /release:checksums -->

---

## Installation & First Launch

Early alpha release binaries are unsigned; system security prompts will appear on first launch:

### macOS Installation
1. Open `SpaceCorps2027-macos-universal.dmg` and drag **SpaceCorps 2027** into `/Applications`.
2. **macOS 15 Sequoia and newer:** Launch the app once, click *Done*. Then open *System Settings > Privacy & Security*, scroll down to *"SpaceCorps 2027" was blocked*, and click **Open Anyway**.
3. **macOS 12 to 14:** Right-click (or Control-click) `SpaceCorps 2027.app`, choose **Open**, then confirm **Open**.
4. **Terminal Alternative:** Strip the quarantine attribute directly:
   ```bash
   xattr -dr com.apple.quarantine "/Applications/SpaceCorps 2027.app"
   ```

### Windows Installation
1. Right-click `SpaceCorps2027-windows-x86_64.zip` and select **Extract All**.
2. The whole game is in `spacecorps2027.exe`: there is no `assets` folder to keep next to it.
3. Launch `spacecorps2027.exe`. If Windows Defender SmartScreen displays a warning, click **More info** followed by **Run anyway**.

### Linux Installation
1. Make the AppImage executable and launch:
   ```bash
   chmod +x SpaceCorps2027-linux-x86_64.AppImage
   ./SpaceCorps2027-linux-x86_64.AppImage
   ```
2. If your distribution lacks FUSE (`libfuse2`), launch using the extract flag:
   ```bash
   ./SpaceCorps2027-linux-x86_64.AppImage --appimage-extract-and-run
   ```
   Or extract the `.tar.gz` archive:
   ```bash
   tar -xzf SpaceCorps2027-linux-x86_64.tar.gz
   ./SpaceCorps2027/spacecorps2027
   ```

---

## Server Connectivity & Game Data

- **Primary Server:** `https://spacecorps-game.sliplane.app`
- **Health Check Endpoint:** `https://spacecorps-game.sliplane.app/health`
- **Alternative Servers:** Switch game servers at runtime via the login screen (*Change server*) or in *Settings > Account > Server*.
- **Local Data Directory:**
  - macOS / Linux: `~/.spacecorps2027`
  - Windows: `%USERPROFILE%\.spacecorps2027`

---

<!-- release:languages -->
## Supported Languages

SpaceCorps 2027 is localized (every page, the HUD, help cards, quests and server messages) in 12 languages:
- English (`en`)
- German (`de`)
- Spanish (`es`)
- French (`fr`)
- Italian (`it`)
- Hungarian (`hu`)
- Portuguese (Brazil) (`pt-BR`)
- Swedish (`sv`)
- Russian (`ru`)
- Japanese (`ja`)
- Korean (`ko`)
- Chinese (Simplified) (`zh-CN`)

This download page (`?lang=<code>`) is translated into 10 of them: `en`, `de`, `es`, `fr`, `pt-BR`, `sv`, `ru`, `ja`, `ko`, `zh-CN`.
<!-- /release:languages -->

---

## Technical Specifications & Requirements

- **Graphics Backend:** Native Vulkan, Metal, and DirectX 12 via Space3d Engine.
- **Minimum RAM:** 4 GB.
- **Recommended RAM:** 8 GB.
- **Storage:** 200 MB free disk space.
- **Network:** Broadband internet connection for real-time multiplayer state synchronization.

---

## Pilot Codex & Game Wiki

Access detailed ship specifications, mechanics, alien encounter logs, and Skylab guides:
- Web: [SpaceCorps 2027 Wiki](https://spacecorps.github.io/play/wiki.html)
- JSON Feed: [wiki.json](https://spacecorps.github.io/play/wiki.json)
- Markdown Mirror: [wiki/](https://spacecorps.github.io/play/wiki/)

