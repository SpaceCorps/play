---
title: "SpaceCorps 2027 · Download"
description: "Download SpaceCorps 2027, a space MMO for macOS, Windows and Linux: fly for a corporation, hunt aliens with your clan and climb the season ranking."
canonical: "https://spacecorps.github.io/play/"
publisher: "SpaceCorps"
license: "Proprietary client, Free to play"
engine: "Space3d Engine"
# release:front
version: "0.5.3"
date: "2026-11-09"
server: "https://spacecorps-game.sliplane.app"
platforms:
  - os: "macOS"
    arch: "universal (Apple Silicon & Intel)"
    format: "dmg"
    filename: "SpaceCorps2027-macos-universal.dmg"
    size: 172341635
    sha256: "07b7f4a9316e99d9d72c5b00815c79f279ced071038dccc5ef4aa8b4748feafc"
    url: "https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-macos-universal.dmg"
  - os: "Windows"
    arch: "x86_64"
    format: "zip"
    filename: "SpaceCorps2027-windows-x86_64.zip"
    size: 165697303
    sha256: "4f5e1883d4186c6d949a539f57426e47e2b3763249c9a6d38bc93cc6b1e2418c"
    url: "https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-windows-x86_64.zip"
  - os: "Linux"
    arch: "x86_64"
    format: "appimage"
    filename: "SpaceCorps2027-linux-x86_64.AppImage"
    size: 160057848
    sha256: "4607f5e97fee9b07dfb727832739e15432ef6770f049de634e0f73d6f6f10c2e"
    url: "https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-linux-x86_64.AppImage"
  - os: "Linux"
    arch: "x86_64"
    format: "tar.gz"
    filename: "SpaceCorps2027-linux-x86_64.tar.gz"
    size: 166582093
    sha256: "616ab3548aca0dd8ea1572910a405fb885fd773057fa7e36e1dd90a750e5c1d8"
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
## Downloads (Version 0.5.3)

| Operating System | Architecture | Package Format | Download Link | SHA-256 Checksum |
| :--- | :--- | :--- | :--- | :--- |
| **macOS** | Universal (Apple Silicon & Intel) | `.dmg` (172.3 MB) | [SpaceCorps2027-macos-universal.dmg](https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-macos-universal.dmg) | `07b7f4a9316e99d9d72c5b00815c79f279ced071038dccc5ef4aa8b4748feafc` |
| **Windows** | x86_64 | `.zip` (165.7 MB) | [SpaceCorps2027-windows-x86_64.zip](https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-windows-x86_64.zip) | `4f5e1883d4186c6d949a539f57426e47e2b3763249c9a6d38bc93cc6b1e2418c` |
| **Linux** | x86_64 | `.AppImage` (160.1 MB) | [SpaceCorps2027-linux-x86_64.AppImage](https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-linux-x86_64.AppImage) | `4607f5e97fee9b07dfb727832739e15432ef6770f049de634e0f73d6f6f10c2e` |
| **Linux** | x86_64 | `.tar.gz` (166.6 MB) | [SpaceCorps2027-linux-x86_64.tar.gz](https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-linux-x86_64.tar.gz) | `616ab3548aca0dd8ea1572910a405fb885fd773057fa7e36e1dd90a750e5c1d8` |
<!-- /release:downloads -->

---

## What's New

The latest release's patch notes (in English). Every release: [patchnotes.md](https://spacecorps.github.io/play/patchnotes.md) · [patchnotes.html](https://spacecorps.github.io/play/patchnotes.html)

<!-- patchnotes:latest -->
### 0.5.3 · 2026-11-09

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.5.3)

SpaceCorps 2027 0.5.3 is the patch for the regional servers. The regional servers of 0.5.2 (Singapore and US East) went public with the hotbar icons broken, with no way to equip or fire rockets there and no way to turn in quests there. 0.5.3 fixes that: the hotbar icons, the ammo list and the rockets work on the regional servers as they do in Helsinki, and a finished mission can be turned in there (Claim Reward in Mission Control; the reward is paid to your account at the home server and shows in your wallet when you return to base). It also carries what was finished meanwhile: a rework of the rockets (only Tier I is sold, the tiers move up, Rocket Launcher II to V, ten special rockets), Clan Dungeons v2 (the Warlord's room opens at 75 % of the Crystalys and their Twins, boosters drop by kills), hull limits of missions that follow the world, one Global chat for every server, a choice of server before you log in, and a sidebar that lists every page again. Singapore and US East were closed to the public again on 2026-11-09 (staff only) until this fix is live; they will be open again when 0.5.3 is live.

#### What's new

**Highlights**
- **Singapore and US East work like Helsinki again for the hotbar, the rockets and your missions.** The hotbar shows its pictures and counts again, the rocket list can be dragged to the bar and fired, and **Claim Reward works on a regional server**: the Reward Claimed window shows the amounts at once, and the reward itself (Credits, Thulium, XP, honor, items, research, booster time) is paid once to your account at the home server and shows in your wallet when you return to base. Equip, Shop, crafting and the other station windows stay the home server's (Return to Base first).
- **Davidski plays music as he flies.** When your ship is within about 3,000 units of him, his song **"Gold Ironclad"** (a gangster-rap track about the game's lore, AI-generated with ACE-Step 1.5, 3 minutes) plays around his ship: full next to him, fading with the distance, panned by the side of the screen, on the Sound Effects volume; the game's music dips under it. It plays through, pauses 30 seconds, and plays again; fly away and it stops. Only pilots on the Danger Sector he flies hear it (he comes out once a day). A game-only change: the new game is needed.
- **Of the normal rockets, only Tier I is sold, for 1,000 credits (500).** Tier II and Tier III are crafted, won at the Auction, or made by the Skylab Rocket Factory.
- **The tiers moved up.** The new Tier I has the stats of the old Tier II, the new Tier II the old Tier III's, and the new Tier III is the old Tier III with its damage x 1.4 (blast radius x 1.1).
- **Rocket Launcher II to V** (permanent, like the Auto-Rocket CPU): II fires **2** rockets per 5 s, III **3**, IV **4**, V **5**, the shots 0.15 s apart.
- **Two cooldowns:** normal rockets share one, set by your launcher (default one shot every 3 s); special rockets share their own 5 s cooldown, which launchers do not change, and each special rocket has its own on top.
- **Ten new special rockets:** Freeze, EMP, Shield Breaker, Toxic, Marking, Cooldown rocket, Flares, Ricochet, Support and the Gravitational N.U.K.E. (the tables below).
- **Do not feed the black hole a N.U.K.E.:** a normal N.U.K.E. that is swallowed by the Danger Sector 4 black hole wakes 10 Slumbering Voids round the ship that fired it, and they hunt that pilot for 10 minutes. To feed the hole the shooter has to be deep in its radiation (a N.U.K.E. flies 1,200 units, the radiation reaches 4,000), and the Voids do not attack a pilot parked inside the hole's 4,200-unit circle. This is read from the server's code and tests; nobody has flown it.
- **Research: 20 new technologies** (Tier II and III of the four families, the eight crafted special rockets and the four Rocket Launchers), so there are **179** technologies in all (159), and the Archivist goal is 179. Flares and Ricochet are sold in the Shop and have none. The N.U.K.E.'s technology now asks for Scatter III (the N.U.K.E. is crafted from it), and the Gravitational N.U.K.E.'s asks for the N.U.K.E.'s.
- **Mining and rock missions pay differently.** The eight rock-breaking missions pay less (Husk and Crystal: **70,000** credits and **560** Thulium, 90,000 and 720 before), Pebble, Cobble and Glimmer have more hit points and pay more, the Anvil and the Ancient Husk pay less, and every rock gives about a quarter less ore (see "Mining and rocks" below).
- **Missions: hull limits follow the world.** A mission that says "hull loss at most N points" gives you **1.5 times N in Beta and 2 times N in Gamma** (Alpha as it was), 42 missions in all.
- **Clan Dungeons v2: the Warlord's room opens when 75 % of the Crystalys and their Twins are destroyed:** **34 of the 45** for a party of 5 (0.5.2: 177 of the 235 aliens). The other aliens stay and can still be destroyed.
- **Boosters drop by kills:** **ten drops** in a run, one at every tenth of all the aliens destroyed, each offering **three kinds drawn at random from five** (Damage, Hull, Shield, Speed, Shield Recharge), at most **15 %** (stage 2) and **30 %** (stage 3).
- **Packs wake and attack at 4 cells** (they woke at 6). **The Zone of Chaos follows the Warlord**, so no laser reaches him from outside it. **The Rocket barrage hits four times as hard:** **26,000** at stage 1 (6,500). **The Dark Matter card gives twice as much:** **10 / 16 / 24** at stages 1 / 2 / 3 (5 / 8 / 12).
- **Global chat is one chat for every server and every world** (with the new game, a pilot's name card also says his server).
- **Choose the server before you log in (needs the new game):** the rows of the start card are clickable, and the game remembers the pick for the main server you play on.
- **The sidebar lists every page again** (the More row of 0.5.2 is gone), **the icon rail is 48 pt wide** (56), **Launch is back in the header of every page**, the Dashboard's included, and **the first-flight tour card no longer flickers or jumps** (all need the new game).

**If you already play: what changes for you**
- **The server and the game update together.** The new numbers (rockets, Dungeons, mission limits) are the server's; the new words and screens are in the game. The release puts the new server and the new game on the table at the same moment.
- **Home and the regional servers update together,** and **the new game is needed for** Davidski's song, the server picker, the hover card's server row, the sidebar, Launch and tour changes (below) and the new Dungeon words. The relay of the Global chat pairs servers of the same build only.
- **Update the game.** A 0.5.2 game can still log in and fly on a 0.5.3 server, but it is not a supported pair: the game and the server go live together. It files Tier II and III rockets in the row of the craft-only rockets, and knows nothing of the Rocket Launchers, the two cooldowns and the new special rockets; see "What a 0.5.2 game sees on a 0.5.3 server". Only chat was looked at with a released 0.5.2 game, on a scratch server of the chat work: signed in at Home, it showed a line of a pilot of another server in its Global tab like any Global line, without the server's name, and its tip still says "every pilot online".
- **The update moves no Credits, Thulium or items.** No rocket stack is removed. Your Tier II and Tier III rockets keep their ids, and their stats move up one step (an old Tier II rocket now hits like the old Tier III).
- **Shop and rocks.** Shop prices: Tier I 1,000 credits; Tier II and III are no longer in the Shop. Three rocks of the first ring have more hit points (Pebble 11,500, was 8,500; Cobble 11,500, was 10,000; Glimmer 12,500, was 9,000), because the rock floor follows the strongest shop rocket; the pay of the rocks and of the eight rock-breaking missions was struck again (see "Mining and rocks"). Mining with Tier II or III costs more per hit than before, because they are crafted (see the known limits).
- **The Pirate Boss's rocket changed.** On `x-3` maps it fires Rivet II, which pierces 0.35 (0.25) and reaches 990 (1,000); on `x-2` maps it fires Rivet I, which pierces 0.25 (0.05) and reaches 1,000 (970). In the model (level 8 Paragons, Alpha, x2 ammo), a lone Paragon no longer wins the fight on `x-3`, two Paragons win it safely. The Dormant Pulses' Rivet II reaches 990 (1,000) too.
- **The Skylab Rocket Factory still makes Tier II and III without crafting.** The Dormant Force's box still holds 30 to 50 of one Tier III rocket (one of the four families, drawn at random), and a N.I.K.E. or a N.U.K.E. half of the time, and the Boss Crystalys's box 8 to 15 of one Tier III rocket, as before; none of the ten new special rockets drops from an alien. The rocket boxes of the Pirate, Seeker, Phantasm and Goombah Bosses now draw from the four Tier I only (from the eight Tier I and II before). The Auction's rocket lots are all Tier I now; the day is worth about 339 M credit-equivalents (273.75 M before).
- **Achievements are off on regional servers.** A flight from Singapore or US East unlocks no achievement; fly from Helsinki for them.
- **A Dungeon that is open when the server updates ends** with the restart, as for any restart; its price goes back to the clan bank. The boosters of a run end with it and nothing is saved.
- **Mission limits.** A mission you are doing when this goes live takes the bigger limit the next time you log in or move on a step, and keeps the hull points you have lost so far. Nothing restarts. A timed mission keeps its clock. If you change world at a wipe with a hull-limited mission under way, you get the limit of the world you fly in then; the points you have lost stay. The mission card, the "Hull limit" pill and Active Quests ("Hull damage: taken / limit") show your world's numbers; the briefing text of a mission still names Alpha's number, as the briefings of the timed missions name Alpha's minutes, and the numbers in the wiki tables are Alpha's.
- **Global chat: the rules are the same** (200 characters, 5 lines at once and then one every 2 seconds, the pauses, no links, no repeats, the alphabet). They run on the server you play on, before your line leaves it: a line the rules refuse, or that comes while you are paused, is shown to nobody. The main server also holds each pilot to one allowance of his own for the lines that come from the regional servers, so changing servers does not give a fresh one.
- **Ignore, Hide Global and Report work for a line from another server** as for any line (they follow the pilot, not the server). Report is still refused while you fly on a regional server (the report sheet shows the refusal): dock first.
- **A line from another server comes a moment after it was said,** and two lines said at nearly the same time on different servers can appear in a different order on different servers. Your own line shows at once. There is no history: you read what is said while you are connected; nothing is stored for later and nothing is replayed when you arrive. If a regional server cannot reach the main server, its Global shows its own pilots until the link is back; a short break is made up late, and what was said during a longer one is not told afterwards.
- **What stays on your server:** Local (the pilots on your map, in your world, on your server), Group chat, private messages (`/m`), the kill feed and the server's own System lines (restart and wipe countdowns, swarm announcements). A private message to a pilot who flies on another server says he is offline, as before.
- **Global chat is shared by all of our servers.**
- **Choosing the server.** On the start card the server rows are clickable, signed out and signed in; a server that is down, updating, full or of another version is dimmed and cannot be picked, as in the Launch sheet. Home's row is the choice until something else is picked. The pick is saved on your computer for the main server you play on, so a pick made at one main server does not apply at another after "Change server", and applies again when you are back. If you flew from Singapore in 0.5.2, that choice is adopted once, at your first sign-in, when nothing was ever picked on this computer.
- **If the picked server cannot take you,** you fly from Helsinki and one line says why: "Singapore is not open right now (Full). You fly from Helsinki instead." (on the start card, in the Launch sheet, and as a toast when the flight starts). If the list could not be read at the launch, you fly from the home server and a toast says "Could not check the servers. You fly from the home server instead." A server that is down or full stays picked and is used again when it opens.
- **Sidebar.** Every page is in the list again, as in 0.5.1, for every pilot and with or without the tour. The `sidebarMore` setting that a 0.5.2 game saved stays in your settings and does nothing, so a pilot who had shut the fold sees all pages again.
- **Launch.** The header's Launch button is on every page again, the Dashboard's included. The active ship's card on the Dashboard keeps its own Launch, so the Dashboard has two.
- **The tour.** The card of the flight tour keeps its side, ignores a small wobble of the thing it points at, and for a thing that moves (the nearest Seeker, your target) docks above the hotbar, so it no longer flickers or jumps.

**What a 0.5.2 game sees on a 0.5.3 server**

A 0.5.2 game can still open the Dungeon window and enter a Dungeon (no new feature gate was added), and nothing crashes. It reads the server's numbers, but it has the 0.5.2 words:
- The door's objective line still says "Destroy 75 % of the aliens to unlock the boss room (N left)". N is right: it counts the Crystalys and their Twins the door asks for.
- The alien count in the window reads the older pair (all aliens killed of all sent, the loot waves included), not the plan-wide count.
- When a booster window offers Shield or Shield Recharge, the game does not know the kind and shows a card named "Booster" with "A temporary booster"; with three kinds offered there are none, one or two such cards. Picking works.
- The window still draws the party list (the server still sends it), the Zone of Chaos ring is drawn at the place the server last told, up to a second behind the Warlord, and the wiki page of Dungeons shows the old numbers (the wiki is part of the game files).
- The Dark Matter card shows the new numbers on the vote screen, which reads the server's.
- Chat: a line from another server shows like any Global line, with no server name; the Global tab's tip is the old one.
- Server choice, sidebar, Launch and the tour card: they are in the game, so a 0.5.2 game keeps the 0.5.2 start card (rows read only; the choice is in the Launch sheet), the More row, the Dashboard without the header's Launch, and the old tour card. It reads the same `client.json` as the new game and keeps the new key when it saves.
- Mission limits: the numbers are the server's.
- Rockets (read from the 0.5.2 game's code): the game takes every rocket with no Shop price for a craft-only rocket, and Tier II and III have none now. It lists them in the row of the craft-only rockets (with the N.U.K.E. and the N.I.K.E.), marks them "craft only", and its Auto-Rocket CPU does not fire them. It has no code for the Rocket Launchers, for the shared special cooldown or for the cooldown of each special rocket (it has one 3 s rocket timer, so it can offer a shot the server then refuses), and it draws none of the effects of the new special rockets (the gravity well, the Support pulse, the puff of Flares, the rings under a ship). The server holds the real rules.

The release puts the new server and the new game on the table at the same moment, so this is a window for a pilot who has not updated yet, not a state to plan for. (These lists are read from the 0.5.2 game's code; nobody has flown a 0.5.2 game on the whole 0.5.3 server.)

**The rockets**

The tiers (damage per hit, lowest to top, from `Rockets.json`):

| Family | Tier I | Tier II | Tier III |
|---|---|---|---|
| Lancet | 3,500-4,200 | 5,200-6,200 | 7,300-8,700 |
| Rivet | 4,500-5,250 | 7,000-8,000 | 9,800-11,200 |
| Ember | 2,400-2,900 | 3,500-4,500 | 4,900-6,300 |
| Scatter | 3,000-3,500 | 4,500-5,500 | 6,300-7,700 |

Crafting (the signature material: Lancet Nyxite, Rivet Daraxium, Ember Cataclysite, Scatter Quorvium). Each Tier II and Tier III rocket has a research technology (Tier II 30 min, Tier III 3 h, and it asks for the Tier II of its family).

| Craft | Needs | Credits | Thulium | Time |
|---|---|---|---|---|
| Tier II | 100 Tier I, 5 Ship Fragments, 10 signature material | 50,000 | 200 | 120 s |
| Tier III | 100 Tier II, 15 Ship Fragments, 2 Reinforced Hull Plates, 20 signature material | 150,000 | 800 | 300 s |

The Rocket Launchers (permanent; the ship's own launcher fires one rocket, then the normal rockets wait 3 s):

| Launcher | Rockets a press | Wait after the press | Research | Craft | Thulium |
|---|---|---|---|---|---|
| Rocket Launcher II | 2 | 5 s | 48 h | 8 h | 150k |
| Rocket Launcher III | 3 | 5 s | 96 h | 12 h | 400k |
| Rocket Launcher IV | 4 | 5 s | 168 h | 16 h | 900k |
| Rocket Launcher V | 5 | 5 s | 240 h | 24 h | 2M |

Each launcher also asks for materials: II 300 Ship Fragments, 50 Reinforced Hull Plates, 30 Power Cores and 5 Ancient Control Units; III 800, 120, 80 and 15; IV 1,800, 250, 160 and 30; V 4,000, 500, 300 and 60. The shots of a press are 0.15 s apart.

The ten special rockets (each has its own cooldown, and all of them share the 5 s special cooldown):

| Rocket | Own cooldown | What it does |
|---|---|---|
| Freeze | 30 s | the target's speed is cut by 60 % for 4 s |
| EMP | 30 s | for 3 s the target can fire no laser, launch no rocket and press no ability |
| Shield Breaker | 15 s | 5,000 hull damage, or 25,000 to the shield while any shield is left |
| Toxic | 20 s | 5 s of poison, 0.5 % of the hull and shield together a second, taken from the hull |
| Marking | 30 s | +20 % damage taken for 5 s |
| Cooldown rocket | 60 s | ability and timed-item cooldowns run at half speed (for 8 s) |
| Flares | 60 s | 25,000 credits, stack of 20: breaks every guided rocket locked on you |
| Ricochet | 3 s | 4,000 credits: 75 % of the damage jumps to a second ship |
| Support | 120 s | placed at the cursor: heals the ships within 500 units of where it bursts (you, your group and your company) by 40 % of their hull and shield |
| Gravitational N.U.K.E. | 120 s | a gravity well at the cursor for 15 s that pulls ships and guided rockets; one per map |

Flares and Ricochet are sold in the Shop and have no recipe or technology. The other eight are crafted in Assembly (one craft makes the number in the second column) and each has a technology of its own:

| Rocket | One craft makes | Needs | Credits | Thulium | Time | Research |
|---|---|---|---|---|---|---|
| Freeze | 5 | 10 Ship Fragments, 30 Cataclysite, 1 Power Core | 50,000 | 1,000 | 300 s | 4 h |
| EMP | 5 | 10 Ship Fragments, 20 Quorvium, 2 Power Cores | 60,000 | 1,200 | 300 s | 4 h |
| Shield Breaker | 5 | 15 Ship Fragments, 40 Cataclysite, 3 Reinforced Hull Plates | 80,000 | 1,500 | 300 s | 6 h |
| Toxic | 5 | 10 Ship Fragments, 30 Nyxite, 10 Quorvium | 60,000 | 1,000 | 300 s | 4 h |
| Marking | 5 | 10 Ship Fragments, 30 Daraxium, 10 Nyxite | 50,000 | 800 | 300 s | 4 h |
| Cooldown rocket | 3 | 20 Ship Fragments, 40 Quorvium, 3 Power Cores, 1 Ancient Control Unit | 100,000 | 2,500 | 600 s | 8 h |
| Support | 3 | 20 Ship Fragments, 40 Nyxite, 20 Quorvium, 2 Power Cores | 90,000 | 2,000 | 600 s | 6 h |
| Gravitational N.U.K.E. | 1 | 1 N.U.K.E., 40 Quorvium, 4 Power Cores, 2 Ancient Control Units | 150,000 | 3,000 | 900 s | 24 h and 10 Dark Matter |

- **The Gravitational N.U.K.E.** is crafted from a normal N.U.K.E.; its technology asks for the N.U.K.E.'s, which now asks for Scatter III (the N.U.K.E. is crafted from Scatter III). It cannot be sold at the Auction.
- **The client shows** the gravity well, the Support pulse, a puff when Flares break a lock, and a ring on a ship under Freeze, EMP, Toxic, Marking or Cooldown.

**Mining and rocks** (`quests.json` and `Asteroids.json`; Alpha's numbers. The rocks' file is struck on the Rivet of each ring: Rivet I on x-1, Rivet II on x-2 and x-3, Rivet III on x-4 and the Danger Sectors. Those rockets moved up a step, so the pay and the ore were struck again.)
- **The eight rock-breaking missions pay less** (ids 149 to 156; the items they give are as before; the pay before in brackets):

| Mission | Level | Experience | Credits | Thulium | Honor |
|---|---|---|---|---|---|
| Rock Breaker (149) | 1 | 350 (400) | 2,000 | 5 | 4 |
| Deeper Rock (150) | 2 | 300 (350) | 2,000 (2,500) | 5 | 3 (4) |
| Heavy Stone (151) | 3 | 800 (1,000) | 6,500 (8,000) | 20 (25) | 8 (10) |
| Armoured Seams (152) | 4 | 1,250 (1,500) | 6,000 (8,000) | 40 (45) | 12 (15) |
| The Rich Border (153) | 5 | 3,000 (3,500) | 12,000 (14,000) | 90 (105) | 22 (26) |
| Anvil Country (154) | 6 | 7,000 (9,000) | 25,000 (30,000) | 210 (270) | 52 (68) |
| Danger Sector Lodes (155) | 7 | 13,000 (16,000) | 40,000 (50,000) | 325 (400) | 65 (80) |
| Husk and Crystal (156) | 8 | 28,000 (36,000) | 70,000 (90,000) | 560 (720) | 140 (180) |

- **Hit points.** Three rocks of the first ring have more: Pebble 11,500 (8,500), Cobble 11,500 (10,000), Glimmer 12,500 (9,000). The others keep theirs: Rime 12,000 and Cache Pod 14,000; x-2 rocks 12,000 to 26,000; x-3 24,000 to 66,000; x-4 48,000 to 130,000; the Danger Sectors 80,000 to 150,000, and the Motherlode 450,000. A rock has 1.5 times the hit points in Beta and twice in Gamma, and pays 2 and 3 times.
- **Fewer rockets break a rock,** because the rockets hit harder. By the file's count of rockets of the ring's Rivet, the Pebble takes 3 (4 before), the Anvil 11 (18.2), the Ancient Husk 14.7 (22.2) and the Motherlode 43.3 (60.5).
- **Pay.** Three rocks of the first ring pay more: Pebble 9,000 to 14,850 credits (6,600 to 11,100) and 3 Thulium 29 % of the time (22 %); Cobble 7,200 to 12,000 (6,300 to 10,500), 28 % (25 %); Glimmer 8,550 to 14,250 (6,150 to 10,350), 57 % (41 %). Four armoured rocks pay less: Ironhide 13,050 to 21,750 (13,650 to 22,650); Plateback 29,700 to 49,650 (31,650 to 52,800) and 6 to 18 Thulium (9 to 18); Anvil 70,650 to 117,750 (84,900 to 141,450) and 24 to 60 Thulium (30 to 72); Ancient Husk 103,950 to 173,250 (114,300 to 190,350) and 51 to 117 Thulium (57 to 129). The other 20 rocks pay what they did, give or take 150 credits and a few Thulium.
- **Ore.** Every rock gives less ore: 13 to 37 % less on average, 27 % less for the middle one. The Anvil gives 9 to 18 Cataclysite (15 to 27), 3 to 12 Quorvium 89 % of the time (6 to 15) and 24 to 48 Ship Fragments (36 to 69); the Plateback 18 to 36 Ship Fragments (27 to 51); the Motherlode 51 to 96 Cataclysite (69 to 126) and 27 to 48 Quorvium (36 to 66); the Pebble 3 Daraxium 42 % of the time (49 %).

**Clan Dungeons v2** (the designer's list and the owner's orders of 2026-11-08)
- **The Warlord's room opens when 75 % of the Crystalys and their Twins are destroyed.** 0.5.2 asked for 75 % of all the aliens (177 of 235 for a party of 5), 0.5.1 for every Crystalys and Twin. Now it is three quarters of the Crystalys and their Twins, rounded up: **34 of the 45 for a party of 5** (the table below), the same in the three stages. The other aliens do not count toward the door, **none of them is removed when it opens**: they stay, wake, hunt you and can be destroyed. The objective line reads "Destroy 75 % of the Crystalys and their Twins to unlock the boss room (N left)", and the chip, the minimap, the toast and the wiki say the same. Once the room is open it stays open.
- **The alien count in the window runs to all the aliens.** "37 aliens - 110 of 235 destroyed" counts every alien the dungeon was made with (the waves of the loot zones and the Goombahs the Warlord calls are not in it), goes on after the door opens and reads full when the last one is destroyed. Destroying the rest pays nothing extra: a run is still paid for the Warlord alone.
- **Packs wake and attack at 4 cells.** A pack woke at 6 cells and attacked at 4; now both are 4 cells (3,200 units), so a pack that wakes is already after you. A pack that woke but has not come out yet goes back to sleep when none of the party is within 4 cells, and wakes again when one comes back. The pre-spawned packs, the cap on aliens alive and the hunt through up to 16 cells of corridor are as before. With a smaller radius you walk more to find the packs: a party may have to leave the loot route to reach three quarters of the Crystalys and their Twins.
- **The Zone of Chaos follows the Warlord.** The violet ring (radius 900) now moves with the Warlord from the warning to the end of the 15 seconds, and the client draws it on the Warlord's ship. The longest laser reaches 900, so **from outside the ring no laser reaches the Warlord** while it lasts (rockets still can). Stay out of the ring, or fly out of it and let the Warlord follow. The 0.5.1 text "the ring stays there, pilots outside can fire into it" is gone from the hint and the wiki.
- **The Dungeon Pirates' rocket reaches 1,000 (970).** Its damage (5,000) and rhythm (a rocket every 5 s) are as before.
- **The Rocket barrage hits four times as hard.** A rocket does **26,000** at stage 1 (6,500), **32,500** at stage 2 and **39,000** at stage 3; a cast of three is 78,000 / 97,500 / 117,000. Its rhythm (a rocket every 15 s for 45 s, a cooldown of 120 s) is as before.
- **Boosters drop by kills, not by zones.** There are **ten drops** in a run (stages 2 and 3), **one at every tenth of all the aliens destroyed** (24, 47, 71, 94, 118, 141, 165, 188, 212 and 235 of 235 for a party of 5). Each drop opens the 30-second window for every pilot, and it offers **three kinds drawn at random from five: Damage, Hull, Shield, Speed and Shield Recharge** (the same three for the whole party, and for a pilot who flies back in). A pick is **+1.5 %** at stage 2 and **+3 %** at stage 3 of its kind: at most **15 % and 30 %** in all, a kind alone may reach all of it. Shield is the ship's maximum shield, Shield Recharge how fast it refills. A pilot who does not answer gets Hull, or the first kind offered when Hull is not among the three. Stage 1 has none; no drop falls once the fight with the Warlord has begun, and one that was earned but not opened by then is lost. The loot zones no longer open booster windows. All ten need all the aliens: a party that stops at the door gets fewer (about 8 in the model, 6 to 9), a full clear gets all ten.
- **The party list is gone from the Clan dungeon window.** The list of the party's pilots with a hull bar each is removed (the minimap still shows the party's dots). The lobby keeps a count and no names: "3 inside, 2 still missing".
- **Twice the Dark Matter in the Dark Matter card.** The loot card gives **10 / 16 / 24** Dark Matter at stages 1 / 2 / 3 (5 / 8 / 12). How often the card is offered is as before (it is in an offer of three about 3 times in 10), the Dark Matter Plate card is not changed (1 / 1 / 2), and every paid pilot gets the card the party picks, as for every card. This Dark Matter cannot be sold at the Auction.
- **Run lengths, in the model:** a party of 5 that opens the door and goes on to the Warlord takes about **33 / 55 / 62 minutes** (stages 1 / 2 / 3), a full clear about 38 / 64 / 72, against 32 / 51 / 58 as the 0.5.2 notes had it (the model now puts the 0.5.2 rule at about 32 / 49 / 57). The time limits stay **95 / 130 / 165 minutes** and the pay is as it was, except for the Dark Matter card.

The door by party size (the Crystalys and their Twins that must be destroyed, of all of them):

| Party | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|
| Must be destroyed (75 %) | 27 | 34 | 41 | 48 | 54 | 61 | 68 |
| Crystalys and Twins | 36 | 45 | 54 | 63 | 72 | 81 | 90 |

**Missions: hull limits follow the world** (the owner, 2026-11-08: the timed missions give more time in Beta and Gamma because the aliens are harder; the missions that limit the damage you may take should do the same)
- **Hull limits follow the world, like the time limits.** A mission that says "hull loss at most N points" (on the whole mission or on a step) gives you **1.5 times N in Beta and 2 times N in Gamma**. A 3,000-point carry is 4,500 in Beta and 6,000 in Gamma. Beta's aliens hit 1.5 times as hard and Gamma's twice, so you can now take as many hits as in Alpha (in Beta and Gamma you could take fewer before). Alpha is as it was.
- **It covers all 42 missions that have a hull limit:** the carries, the holds, the tours and the Challenge missions (the five Untouched runs and the Convoys).
- **The numbers on the mission card, the "Hull limit" pill and Active Quests ("Hull damage: taken / limit") are your world's.** The briefing text of a mission still names Alpha's number, as the briefings of the timed missions name Alpha's minutes. The numbers in the wiki tables are Alpha's.
- **A server rule; the numbers need no new game.** The rule is `Tier::strength()` of the pilot's world (Alpha 1, Beta 1.5, Gamma 2) times the seed's number (`quest::world_hull_limit`, `world_hull_pct`; a percent limit stops at 90). `quests.json` and the model stay Alpha's. The wiki text about the limits (Conditions, Time limits, the note above the tables) is new in all 13 languages; it needs the new game to be read.

**Global chat between the servers**
- **Global chat is one chat for every server and every world.** What you write in **Global** is heard by every pilot on Home and on every regional server (Singapore, US East), in Alpha, Beta and Gamma, in flight and at the station. Before, each server had a Global of its own, so a pilot in Asia and a pilot in Europe could not read each other.
- **Which server is he on?** Rest the pointer on a pilot's name: the card that opens now also says **Server: Singapore** (or the server's name) when he flies on another server than you (needs the new game). There is no server tag in the line.
- **"Invite to group" on a line another server relayed is disabled,** with the reason, in 13 languages: a group lives on one server.
- **The words:** the Global tab's tip and the Help card for the chat channels say it in the 13 languages, and so does the wiki's Groups page.

**Choosing the server before you log in** (needs the new game; the server is unchanged)

The owner's complaint after 0.5.2: the start card listed the servers but the rows were read only, the choice existed only in the Launch sheet, and a pilot who signed in and went to the station had no list there.
- **The start card (the Landing card):** the rows are clickable, signed out and in the "signed in as" state, under one line, "Choose the server you fly from" (13 languages). A server that is down, updating, full or of another version is dimmed and cannot be picked. Home's row is the choice until something else is picked.
- **Remembered on the computer, for the main server it was made at.** The game keeps the pick in `client.json` (key `play_server_picks`), for the address of the main server you chose. A pick made at Home A does not apply at Home B after "Change server", and applies again when you are back at A. The pick is written at the click and read at the next start before any sign-in.
- **The choice of 0.5.2 is adopted once.** A pilot who flew from Singapore in 0.5.2 has only the per-pilot choice. At the pilot's first sign-in, when nothing was ever picked on this computer, that choice becomes the pick of the main server signed in to. It is not copied to a second main server, and a click made on the card before the sign-in is more recent and wins.
- **It applies everywhere you launch.** The Launch sheet opens with the picked row selected, and a launch from anywhere uses it. If the picked server is not in the list, is down, full or of another version, the launch is Helsinki's and one line says why and from where the flight is. A launch that does not start (the setup guard) toasts nothing. A Home with no list plays as before.
- **It cannot nag.** The toast comes once for each (pick, reason) in a run; a new reason is told, and so is the same one after you pick the line again. A pick whose server is gone from the list is told and then forgotten at that launch, so a Home that lists only itself cannot hold a stale pick.
- **A list that could not be read.** When the list is still unknown at the launch and the pick is not Home's, the flight is Home's and a toast says "Could not check the servers. You fly from the home server instead." (13 languages).
- **The list stays in the station.** A sign-in keeps the list that is known and asks again at once (an administrator's staff lines appear); a sign-out and another Home drop it. The game asks every 5 seconds while the start card or the Launch sheet is on screen, once a minute while the station is shown (a conditional request, answered "not changed" when the list is the same), and not at all otherwise (flight at Home, other screens). In a window that cannot be seen (minimised, hidden, suspended) nothing is read and no server is pinged. A read that fails is repeated after 15 s, then 30 s, then 60 s, each wait a little longer by a share of up to 25 % that is the client's own, so the pilots of a Home that was down do not all come back in the same second.
- **The rules stay:** a launch ticket goes only to a host on the list of suffixes the game accepts, your token goes only to Home, a 404 is no list, and Home alone is no list (no row is drawn).
- **Not changed on purpose:** the sign-in (Login) screen has no list of its own, and the typed-address sheet and the Settings page are as they were.

**The sidebar, the rail, Launch and the tour card** (needs the new game)
- **The sidebar lists every page again, as 0.5.1 did,** on the owner's order of 2026-11-08. The More fold of 0.5.2 hid fourteen of nineteen pages from a pilot at level 1 and from every pilot while the tour ran; the owner wants the whole list in view for everyone, with no level or tour rule. The four groups (Command, Economy, Community, Library) have their headers and every page of them that the game lists for you, then Settings, Admin (admins only) and Sign out stay at the foot. There is no More row. The attention "!" is on the page's own row again. The keys, the Dashboard's Next-step card, the toolbar's ? guide, the window cascade and the one vocabulary of 0.5.2 are kept.
- **The icon rail is narrower:** the sidebar folded with the panel button at the top is **48 pt** wide (it was 56). The attention badge on a rail row is a smaller disc on the row's top-right corner, clear of the icon; the rail's list has no scroll bar over the icons (the wheel still scrolls, and a fade at the foot says there is more). The open sidebar is unchanged. The page gets 8 pt more on the rail (936 pt at a 1024 wide window).
- **The header's Launch is back on every page,** the Dashboard included. In 0.5.2 it was hidden on the Dashboard; at 1024 x 640 with the chat dock open, the wipe card and the Next-step card above the ship card (level 1) put the ship card's own Launch 18 pt under the fold, with no Launch left in view. The ship card keeps its own Launch. The tour's last station step points at the header's Launch on every page.
- **The first-flight tour card no longer flickers or jumps** (the owner on the live 0.5.2: "flight tour fly panel flickers and jumps around all over the place"). Before, the card was placed again every frame from the rectangles of the thing it pointed at, and in flight those are never still. Now:
  - **It keeps its side** while the side still fits, with 4 pt of slack, and forgets it when the card points at something else.
  - **It ignores a small wobble:** a move of the card's place under 3.5 pt is not followed; a bigger one is.
  - **A target that is not drawn** is held, ring and card, for 0.3 s in the flight (the station lets go of it at once).
  - **For a thing that moves of itself** (the nearest Seeker, the target, the bubble over the station) the card docks at the bottom centre, above the hotbar when it is drawn, and only the ring goes after the thing. The card never stands on the ring (at least 10 pt clear): it moves to the top centre or a side when the ring comes down on it, and stays there until it must move again. A docked card on a moving thing has no arrow. In a window under 900 pt wide the card is full width and has only the bottom and the top.
  - **The card's height** is the tallest its content has been in the step and is measured again when the width or the language changes; a new card is laid out in the frame it first shows, so there is no blank frame between two cards.

**Texts and the wiki**
- The Global tab's tip, the Help card for the chat channels, the wiki's Groups page and the reason on the disabled "Invite to group" entry are in all 13 languages. The wiki text about mission hull limits is new in all 13 languages.
- The wiki page of Dungeons, the objective line, the chip, the minimap and the toast carry the new door and the new numbers.
- The new rockets' texts have keys in the 13 languages (the rockets design notes).

**Needs the new game, and what does not**
- **Needs the new game:** the server choice on the start card (the line "Choose the server you fly from" and the "Could not check the servers" toast are in 13 languages), the server row on a pilot's name card, the sidebar, the rail, the Launch button in the header of every page and the tour card; the new Dungeon words (the door line, the plan-wide count, the three booster kinds, the lobby count, the ring on the Warlord's ship); the drawings of the new rockets (the gravity well, the Support pulse, the puff of Flares, the rings under the status rockets); the new wiki and Help texts.
- **Server only, live with the server:** the rockets' stats, prices, recipes and cooldowns, the launchers, the rocks' hit points, pay and ore, the pay of the eight rock-breaking missions, the Pirate Boss's rocket, the Auction's rocket lots, every Dungeon number, the mission hull limits and the Global chat relay.

**For administrators and the server**
- **Clan Dungeons: no new table, column, route, setting or data step.** The only data that moved is `server/Resources/Dungeons.json` (written by `docs/design/dungeons-model.py --json`, never by hand), so `GET /api/admin/dungeons` shows a new `file.hash`. The file is read at the start and checked whole: a file that is there and wrong stops the start with nothing changed. `python -X utf8 docs/design/dungeons-model.py --check` was green on the Dungeons v2 lane's branch (run 2026-11-09; not run again on this note's branch).
- **The file and the code belong together.** A 0.5.2 server does not know the door rule `eliteShare`: given the 0.5.3 `Dungeons.json` it fails to read the file and the start is stopped. A 0.5.3 server with the 0.5.2 file runs no boosters. A rollback brings the 0.5.2 image together with its own file. Server and game go live together (stage both, flip together).
- **First days, the counters** (`GET /api/admin/counters?prefix=dungeon`; the healthy values are expectations from the rules and the model, not seen on a live server): `dungeon_boost_window{stage}` up to ten a run and none at stage 1, about 8 for a party that opens the door and flies on; `dungeon_boost_picked{kind,auto}` has five kinds; `dungeon_door_opened{door=boss, why=kills}` at 75 % of the elites; `why=admin` stays rare. The admin overview's `boosts` object of an active run has new keys, `{kills, earned, windows, of, open, answered, picks: {damage, hull, shield, speed, recharge}}`.
- **The Dark Matter model:** the dungeons now give more than the Dark Matter model's single source (a clan of five that runs the three stages every day gets 74 to 222 Dark Matter a day before, twice that now). Read the Dark Matter stock of the first days against the excavators' burn.
- **Global chat between the servers: nothing to set up** (the node uses its `NODE_SECRET`; a Home with no node registered behaves as before). Look at it with `GET /health`, `flight.chat` (`relay`, `ringHead`, `ringLen`, and per node `pushAgeMs`, `pullAgeMs`, `pushed`, `pulled`, `dropped`). Home's log has every Global line as `CHAT: [global] [<node>/<World>] name: text`, and the speaker's own server logs it as well.
- **Chat kill switch, no restart:** `PUT /api/admin/flight/dials` with `{"chat": {"relay": false}}`; each server then keeps its own Global. The dials replace each other as a whole (a PUT without `asteroids` lifts the asteroid dials, one without `chat` turns the relay on), and they live in memory, so Home's restart is the default (on). A `chat.relay` that is not a JSON boolean is a `400 BAD_DIALS`.
- **Chat: two things nobody has looked at on the real boxes** (`docs/DEPLOY.md`, "Global chat between the servers (0.5.3)"): whether Sliplane's edge holds a request for 8 seconds (a cut is taken as an empty answer, so chat still works), and which address Home sees for each node (it decides what is counted per address).
- **Missions:** a server rule (`quest::world_hull_limit`, `world_hull_pct`); no data step.
- **`GET /api/servers` with a token costs one account read on every request,** a 304 included, because the list differs for administrators. At the station that is about one primary-key read per signed-in pilot per minute, and one per 5 seconds while the start card or the Launch dialog is open. A cheap fix is known (cache the admin flag per user for a short window) and is not done; this is a client release.
- **Proof of the tour card:** `tour::tests_settle`, `tour::tests_flicker` and `tour::tests_card` hold each cause; several of the flicker tests failed on 0.5.2's code when they were written (not run again for this note).
<!-- /patchnotes:latest -->

---

<!-- release:checksums -->
## Checksum Verification

Verify the integrity of downloaded binaries prior to execution:

### macOS
```bash
shasum -a 256 SpaceCorps2027-macos-universal.dmg
# Expected: 07b7f4a9316e99d9d72c5b00815c79f279ced071038dccc5ef4aa8b4748feafc
```

### Windows (PowerShell)
```powershell
Get-FileHash SpaceCorps2027-windows-x86_64.zip -Algorithm SHA256
# Expected: 4f5e1883d4186c6d949a539f57426e47e2b3763249c9a6d38bc93cc6b1e2418c
```

### Linux
```bash
echo "4607f5e97fee9b07dfb727832739e15432ef6770f049de634e0f73d6f6f10c2e  SpaceCorps2027-linux-x86_64.AppImage" | sha256sum -c -
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

SpaceCorps 2027 is localized (every page, the HUD, help cards, quests and server messages) in 13 languages:
- English (`en`)
- German (`de`)
- Spanish (`es`)
- French (`fr`)
- Italian (`it`)
- Hungarian (`hu`)
- Portuguese (Brazil) (`pt-BR`)
- Swedish (`sv`)
- Turkish (`tr`)
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

