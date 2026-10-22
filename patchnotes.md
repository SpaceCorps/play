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
## 0.4.25 · 2026-10-22

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.25)

SpaceCorps 2027 0.4.25 is the release the first Universe Wipe runs under: the wipe keeps every ship you own and takes your items, except the gear on your active ship, your drones, formations, P.E.T. Stations and your Transport Cache. It adds Auction buy orders and a News card, lets chat take Cyrillic and other scripts, doubles the Thulium Geode's Thulium, ends the daily mining limit, makes Davidski hit twice as hard and pay 1.5 times, and lets the Mole work every rock and the Cradle work in flight.

### What's new

**Highlights**
- **The first Universe Wipe keeps all your ships.** It also keeps the gear fitted to your **active ship**, your **drones**, **drone formations**, **P.E.T. Stations** and your **Transport Cache**. **Every other item is removed,** the gear on your other ships and the engines and lasers fitted in your Skylab too. **Clans end.** **Credits, Thulium, XP, honor, level, ranks, Skylab, technologies, skins, P.E.T.s, Wipe Points and permanent buffs stay;** nothing is capped.
- **Buy orders on the Auction:** say what you want and what you pay for a lot, for 7, 14 or 21 days; the price is held until a seller (level 5 or more, with a Standard item he earned) fills the order or you cancel. The seller pays the 5 % tax. Three new sounds.
- **A News card on the Dashboard** shows the newest three posts of the SpaceCorps team; the game server fetches them every 15 minutes, the game never contacts GitHub.
- **Mining and aliens:** the **Thulium Geode pays 36 to 84 Thulium** (it paid 18 to 42); **the daily mining limit is gone**; **Davidski** is out of every ranking, hits twice as hard and pays 1.5 times (Alpha: 1,590,000 Credits, 4,275 Thulium); the **x-2 maps hold 30 Seekers and 15 Phantasms** (they held 20 and 10).
- **The Mole works every rock a rocket can hurt,** the Motherlode too; Moles of different pilots can share a rock, and the card shows its real damage. **The P.E.T. Cradle works in flight.** Dock and Undock still need a parked ship.
- **Chat takes Cyrillic, Japanese, Korean and Chinese** text and the numero sign. Links stay refused, in Russian words too. The sidebar's Messages row is hidden.
- **Interface:** **drones on the pilot sheet**, **Ctrl+F search in the Assembly**, the **Forge** names a piece's ship and has a Ship filter, **short numbers** (1.2M, 1.5B), a **volume button** on the start and sign-in screens, a **full Trophies Bay** told by a toast, a pill and a sound, and a clan timer that reads `--:--`, not 00:00, when the clock is unknown.
- **Smaller:** the wiki is updated in 13 languages; the admin action **Set season day** moves the season day without freezing the clocks.

**If you already play: what changes for you**
- **Update the game.** A 0.4.17 to 0.4.24 game installs a patch when the job made one for it (a Linux AppImage game from 0.4.22), else the whole package; an older game downloads the whole package.
- **Before the wipe:** put what you want to keep in the **Transport Cache** (50 t; it opens with the Chrono-Gate's 100 parts), make the ship you want geared your active ship, and leaders pay out the Fleet Treasury. Take the engines and lasers out of your Skylab's modules and put them in the Cache too: they are loose items. Open Auction listings come back as loose items and go with the rest; buy orders return their price whole.
- **Your PvE ranking points fall by 37 for each Davidski kill** you made, once, at the first start of the server (he is out of the ranking systems). Level, XP and PvP points stay; a company rank can drop a step.
- **The update itself pays, moves and removes no Credits, Thulium or items.**
- **A 0.4.24 game keeps working but has none of the new screens** (buy orders, News, drone cards, the Cradle in flight, the Bay-full notice); it can type Cyrillic, and an emoji costs it 2 lines. A 0.4.25 game on an older server hides buy orders and News.
- **New texts in other languages have had no native review.**

**The first Universe Wipe**
- **When:** a season ends on day 30. As day 30 begins the System chat says *Universe Wipe in 5 minutes* and counts down (at 240, 180, 120, 60 and 30 seconds and in the last 10); 300 seconds later the wipe takes every pilot who has a world off the maps. A pilot without a world is left as he was. **The first wipe is expected on 24 or 25 October 2026:** its countdown begins when the season's day 30 does, somewhere between about 07:41 UTC on Saturday the 24th and 07:41 UTC on Sunday the 25th, and the wipe is five minutes later (09:46 CEST on the 24th at the earliest, 08:46 CET on the 25th at the latest). That hour is worked out from one line of the live server's log, not read from its clock; it is read and announced once this version is live. If the live season is still held on the day override, no wipe is scheduled until an administrator changes that. The first wipe of the game runs under the rules below, which are those of this version.

| Yours | After the wipe |
|---|---|
| **Every ship** | **Kept,** whole again: full hull (its plates counted), empty shields, its skin and any conversion under way. Exactly one is active |
| The gear fitted to your **active ship** in configurations 1 and 2, with what is fitted into it | Kept |
| Your **drones** (level and experience), **drone formations** and **P.E.T. Stations**, wherever they are | Kept |
| Your **Transport Cache** (up to 50 t) | Kept |
| **Every other item:** loose gear, the gear on your other ships, resources, ammo, rockets, boosters, CPUs, plates | **Removed** |
| Credits, Thulium, XP, honor, level, ranking points and rank, Premium, quests, Wipe Points, permanent buffs | **Unchanged:** nothing is capped in this wipe |
| Skylab (modules, ore, research), technologies, P.E.T.s, skins | Unchanged. A Skylab expedition under way is settled and the Trophies Bay is paid out and emptied (its loot is removed like any loose item). **The engines and lasers fitted in the Engine and Defense Modules are loose items and are removed:** take them out and put them in the Cache |
| Your **clan** | **Ends,** with its Fleet Treasury, posts, log, treaties, points and boosts. What a clan paid you stays |
| **Auction** | Listings come back as loose items and go with the rest; bids in lots are refunded; buy orders return the price they hold whole (the deposit is gone) |
| Chrono-Gate parts, the Cache, your destination | Reset: 0 parts, the Cache empty and unlocked (what it held is in your inventory, loose), the destination cleared. You land at your company's home in the world you chose under Galaxy Gates (else you choose at Setup) |

- **What is new about it:** before this version the wipe deleted every ship but the active one. Now each ship you own comes through; only the **items** are removed, and only the active ship keeps what is fitted to it. To keep the gear of another ship, put it in the Cache, or make that ship the active one before the wipe.
- **The server writes down the wipe:** for each pilot, his rank, his place on his company's ladder, whether he wore the crown, his PvE and PvP points, his totals (level, experience, honor, Credits, Thulium, kills, deaths, shots, play time), his wallet before and after, the ships he kept and the items and units removed. No screen shows it yet. It is kept as long as the account and removed when you delete it.
- **The Auction is closed from day 30,** but you can still cancel your own listings and orders.
- **Rehearsed, not run:** the wipe was run twice on a synthetic database of 200 pilots (193 with a world): 0 failures, 994 ships before and 994 after, 3,937 item rows kept and 6,548 removed, and a second wipe a fixed point. It took 1.3 seconds on an idle Mac and 4.4 seconds on a busy one. The live game's data was not available, so it has not been run on that.

**Buy orders on the Auction**
- **Where:** the Auction bar has a fifth section, **Buy orders**, with two views: **Wanted** (everyone's open orders, with search, category chips, a currency, a sort and the chip **I can fill**) and **My orders**. Place one with **New buy order**: the kind, the lots, Credits or Thulium, the price of one lot and 7, 14 or 21 days. There is no highest price; the least price is the kind's.
- **What it costs:** the **whole price is held** (the page counts it as *In orders*) and the **deposit** of a listing is burned. Your first ten postings of a UTC day, listings and orders together, pay no deposit. Orders have slots by level, counted apart from listings: 20 at level 5, 40 at level 6, 70 at level 7 and 100 from level 8. The server holds at most 25,000 open orders.
- **Standard items only:** an order asks for a kind in its plain form, not forged and with no rolled buffs. A seller of level 5 or more fills it with Marketable (earned, not bought) Standard items that are not fitted, cached or holding modules, a few lots at a time (a sale of unique pieces takes up to 25). He receives the price less the 5 % tax; the buyer's items are not Marketable. Nothing matches an order with a listing by itself.
- **It ends** when it is filled, when you cancel (the held price of the lots left comes back whole, the deposit does not), when it runs out, at the wipe, when you delete the account, or when an administrator cancels it.
- **The sell sheet** of an item shows the best open order for it and **Sell to it**. Fills, expiries and returns come as a toast, a burst of fills as one growing toast.
- **Three new sounds:** an order placed, an order filled (to the buyer) and a sale to an order.

**The News card**
- **Where:** the last card of the Dashboard's left column, under the boosters: the newest three posts, each with a thumbnail, a title, the date and a line of text, a *New* pill and **Mark all read**. A click opens the whole post with all its pictures; Newer, Older and the arrow keys go through the last 20. What you have read follows your account to your other computers.
- **Where it comes from:** the server reads a public repository (`SpaceCorps/news`, folder `posts`) every 15 minutes and keeps the newest 20 posts in memory; the game only calls its own server. A post has a title of up to 120 characters, a body of up to 4,000, three pictures of at most 2 MiB and 1,600 pixels, and a small Markdown (paragraphs, headings, lists, bold, italic, links to https addresses). HTML and pictures by address are dropped. A link shows where it goes and opens your browser; in the Steam build links are plain text.
- **If there is no news** (the repository is empty, or a server without the service) the card shows its empty text or, on a server of an older version, does not appear.

**Mining and aliens**
- **The Thulium Geode** (grows on T-3, G-3 and T-4) pays **36 to 84 Thulium** a rock in Alpha, twice what it paid (18 to 42); Beta pays twice and Gamma three times that, as for every asteroid. Its Credits (42,450 to 70,800), ore and rare finds are as they were. No other kind changed. The models read a solo miner's Thulium an hour in Alpha on T-3, G-3 and T-4 at 875, 960 and 1,701 before and 1,175, 1,433 and 1,944 now.
- **The daily mining limit is gone,** in Alpha, Beta and Gamma: every chunk is paid whole, "Daily mining limit reached" is never sent, the asteroid Help card reads *Daily limit: None* and the Target window and the wiki say there is none. The Mole is held by no limit either. **It is a switch, shipped off:** the caps (Thulium 3,000, 4,500 and 6,000 and Credits 13, 18 and 21 million a pilot a day in Alpha, Beta and Gamma) stay in the file, and an administrator can turn a world's limit back on without a release. The models' reading of what the limit held back: a solo miner's 6 hours up to 2.4 times the Credits and 3.2 times the Thulium of the limit; a Mole that works all 24 hours 4.4 to 9.6 times the Credits and 2.7 to 13.1 times the Thulium. Nothing of this is measured yet.
- **Davidski** is out of every ranking: no row in the Hall of Fame, no place on a profile, and his kills add no ranking point (the experience still counts). **He hits twice as hard:** his volley is 4,104 a second in Alpha, 6,156 in Beta and 8,208 in Gamma; his hull, shield, speed and range did not move. **He pays 1.5 times:** Alpha 1,590,000 Credits, 4,275 Thulium, 255,000 XP and 1,110 honor, Beta twice and Gamma three times that. The limits stand: 2 paid kills a pilot and 8 a world a day. The model's fight: in Alpha the smallest group that kills him goes from 3 to 4 late-offense pilots and the smallest that loses no ship from 5 to 9.
- **The x-2 maps** (M-2, T-2 and G-2, in every world) hold **30 Seekers and 15 Phantasms,** where they held 20 and 10. On the scratch server a pilot on an x-2 map is sent 12.2 KB/s before and 14.4 after (+2.2 KB/s, +18 %), and the server's tick costs 4.4 to 14.3 microseconds more per extra alien.

**The Mole and the P.E.T. Cradle**
- **The Mole works every asteroid a rocket could hurt** in your world and reach: the Motherlode, rocks another pilot has already damaged, and the four wrecks you can mine (Cache Pod, Scrap Hulk, Derelict Hulk, Derelict Cruiser). The wrecks drifting in the background are scenery and cannot be hit. Moles of different pilots can work the same rock; the break is paid by damage dealt, as with rockets, and a share under 5 % pays nothing. A Mole keeps the rock it began until it breaks.
- **Its card shows the real damage:** *Hits 2,125 to 4,800 every 3 s* for a top Mole in Alpha, the least and the most one pulse takes off a rock of tier 1 to 5; hover for the five tiers. The model reads a top Mole at 100 to 118 % of the rocks an hour that a miner with the best rockets breaks.
- **The Cradle works in flight.** With the Hangar open over the game, **New assembly, Collect, Collect all, Cancel, Crossbreed** and **Let go** work anywhere, with no need to land. A Cluster Chunk picked up while mining can go into the Cradle in the same flight, and a job started in flight survives a jump or a death. **Dock and Undock** still need a parked ship; the greyed buttons say why on hover, and the green "Hangar is open" banner no longer stands over the P.E.T. view.

**Chat takes more scripts**
- **What is allowed:** Latin, Cyrillic (Russian, Ukrainian...), Japanese, Korean and Chinese text, and the numero sign. Emoji, symbols and other scripts (Greek, Arabic, Hebrew, Thai) are still refused and the box drops them, with a hint of its own in 13 languages. The 200-character limit, the pause for sending too fast, the spam and repeat rules and the no-links rule are as they were.
- **Links in Russian words are refused too:** "discord tochka gg" written in Cyrillic, a dot word in brackets, the Russian names of the usual sites (Discord, YouTube, Twitch, TikTok, Instagram and others) and the domains .ru, .rf, .rus, .ukr and .org. A word that is also an everyday word (gg, net) counts only after a spoken dot or a known host, so "tochka sbora" stays chat.
- **The Messages row** of the sidebar is hidden for now. Private messages work as before, and their unread numbers still show on the chat bar and the Chat button.

**The interface**
- **Drones on the pilot sheet** (Rankings, Stats, the clan list, your own): one card per drone, up to 8, with its picture by level (the gold gunship for a Master Drone), *Lv n* and a box for each slot with the item it carries or an empty box. Hover for its name, level, laser damage bonus and what it carries; the count in the header is the number of drones (5 / 8). A drone being upgraded is dimmed with empty boxes. A pilot with no drones has no group.
- **The Assembly search:** Ctrl+F (Cmd+F on a Mac) focuses a box in the header; it filters the open tab. Crafting matches recipes by what they make and what they need; the Forge matches equipment by name, type and tier. Several words match in any order, a pill counts the matches, Esc clears it.
- **The Forge says where a piece is:** "On Kitefin, configuration 2" (a Hull Plating: "both configurations"; a fitted piece takes its host's ship and says "Fitted into Quantum Laser II"), on the card, in the panel and in the Merge. A **Ship drop-down** beside the type filter shows only the pieces on one of your ships (it appears from two ships). A piece fitted in a Skylab module is named by that module ("Fitted in your Skylab's Engine Module") instead of "In the Transport Cache".
- **Why a thruster holds fewer buffs:** the Forge's quote carries the stats too low to carry a buff, and a caption under *Buff slots* names it. An Impulse Thruster's speed multiplier is under the floor, so it holds one buff, a Momentum Thruster two; the tier ladder no longer says "up to 4 buffs" for them.
- **Short numbers:** from 1,000 a count reads 1k, 1.2k, 999k, 1M, 1.2M, 1B, 1.5B, **cut, not rounded** (1,260,000 reads 1.2M, 999,999 reads 999k), on the hotbar (a slot shows its whole count up to 99,999), in the ammo and rocket pop-ups and on inventory tiles. **Money and charts are rounded, not cut, and start at 10,000:** when the toolbar is short of room, its pills for Credits, Thulium and honor read 987.7M or 1.5B where they read 1,500M (the hover has the whole number); chart axes, the Builds table and the admin metrics use the same function.
- **A volume button** (a speaker, left of the language button) on the start and sign-in screens opens the master volume and a mute. Your pick is remembered, wins over the volume saved on your account when you sign in, and is saved to it.
- **A full Trophies Bay is told:** a toast with a quiet sound of its own at the first look of a session and when it fills while you play, an amber *Bay full* pill on the Skylab station bar and a notice on the Skylab page with the Open the Universe button, until you collect. The server pushes nothing for the Skylab, so the game finds out at its next look: every 15 seconds with the Universe window open and every 3 minutes while a Skylab hunts.
- **The clan timer:** when the server cannot say when the clan day ends, the countdown on the Operations tab reads `--:--` where it read 00:00 and refused every Warden with "Less than 30 minutes of the day are left". The server's rule is unchanged: no Warden from 23:30 UTC, the last 30 minutes of the clan day.

**For administrators and the server**
- **At the first start: 13 schema lines, no data step.** `backup_risks v0.4.24 HEAD` prints these (the job prints the same as warnings); they are additive and made in place, and a 0.4.24 server ignores them. **A Sliplane volume backup before the deploy is advised** (money is held in a table the old code ignores).

```
schema ALTER TABLE MARKETTRADES ADD COLUMN ORDERID
schema ALTER TABLE WIPETIMELINESTATES ADD COLUMN CLOCKSTART
schema CREATE INDEX IF NOT EXISTS IX_MARKETORDERS_BOOK
schema CREATE INDEX IF NOT EXISTS IX_MARKETORDERS_BUYER
schema CREATE INDEX IF NOT EXISTS IX_MARKETORDERS_EXPIRY
schema CREATE INDEX IF NOT EXISTS IX_PILOTSEASONS_SEASON
schema CREATE INDEX IF NOT EXISTS IX_PLAYERITEMS_EQUIPPEDSHIPID
schema CREATE INDEX IF NOT EXISTS IX_PLAYERITEMS_PARENTITEMID
schema CREATE INDEX IF NOT EXISTS IX_PLAYERITEMS_PLAYERID
schema CREATE TABLE IF NOT EXISTS ASTEROIDBELTDIAL
schema CREATE TABLE IF NOT EXISTS MARKETORDERS
schema CREATE TABLE IF NOT EXISTS PILOTSEASONS
schema CREATE TABLE IF NOT EXISTS WIPERUNS
```

- **Also at every start:** the PvE ranking recount takes the 37 points of each Davidski kill off a pilot's stored points (once; a second start finds nothing; it works every pilot's points out again from his kills, as at every start before, so a pilot whose experience grew since his last kill can also gain a few), and the seed sync sets the x-2 maps' spawn counts to 30 and 15.
- **Seven data files changed:** `Asteroids.json` (the Geode's Thulium and `belts.enabled` false), `Chat.json` (alphabet `scripts`), `Davidski.json` (`damageFactor` 2 and the pay), `Market.json` (`limits.globalOpenOrders` and `orders.enabled`), `Pets.json` (the Mole: Motherlode on, `startRule` any), `ranking-config.json` (Davidski 0 points) and `map-spawns.json`. No price, tier or research moved.
- **New:** 12 routes (`/api/market/orders` with `mine`, `cancel` and `fill`; `/api/news` and `/api/news/img/...`; admin `news/status` and `news/refresh`, `market/orders` with `cancel` and `hold`, and `timeline/season-day`), 9 optional environment variables (`MARKET_ORDERS_ENABLED`, `CHAT_ALPHABET`, `NEWS_ENABLED`, `NEWS_REPO`, `NEWS_BRANCH`, `NEWS_DIR`, `NEWS_POLL_SECS`, and `NEWS_API_URL` and `NEWS_RAW_URL` for tests), one dependency of the server (`sha1`, already in the lock), the client feature `market-orders`, and counters `market_order_*` and `news_*`. The `Dockerfile` and the release job's scripts are unchanged.
- **Set season day N** (Admin, Controls tab) is how a season is held or moved now, instead of the day override that freezes every clock: today becomes day N and the clocks run on from there, so the clan reset, the Warden rule, the Auction and the wipe follow the real clock. It shows a review sheet first (the new day, when day 30 begins, where the wipe's countdown starts, the clan day, the Wardens that will be withdrawn) and refuses day 30. `GET /api/admin/timeline` gains `seasonStart`, `clockStart`, `wipeCountdownAt` and the clan clock's `clanDay`, `clanSecondsLeft`, `clanClock` and `clanClockReason`. **Deploying changes no live season:** a season held on the override keeps its frozen day, with no wipe scheduled, until Set season day or Reset is pressed.
- **At the countdown** the server writes `/data/spacecorps-prewipe.db` beside the periodic snapshot (one file, replaced by the next wipe) and logs `Pre-wipe snapshot: <path>, <bytes> bytes (<ms> ms)`; a failure is a warning and the wipe goes on. Three new indexes on `PlayerItems` keep the wipe quick on a big table (a pilot with 35,006 loose rows: 11 seconds before, 0.1 after).
- **Switches without a release:** `MARKET_ORDERS_ENABLED=false` (refunds every open order at the next start and removes the order routes), `NEWS_ENABLED=false`, `CHAT_ALPHABET=latin` and the live admin dial `POST /api/admin/asteroids/gate {"world", "beltsEnabled"}`, which turns a world's mining limit back on and survives a restart.
- **Rolling back to 0.4.24:** a 0.4.24 server refuses the new `Market.json`, `Asteroids.json` and `Davidski.json` (they carry fields it denies), so the image and its files go back together. With open buy orders, set `MARKET_ORDERS_ENABLED=false` and let a 0.4.25 server start once (it refunds them), or restore the volume backup. A wipe that went through is not undone by a rollback; the way back from a bad wipe is the pre-wipe copy.
- **Privacy:** two new things are kept about a pilot, both removed with the account: his buy orders and the wipe record above. The text for the privacy page is in `docs/privacy-addendum.md`.

## All releases

Each line links the full notes of that release as Markdown (patchnotes/v<version>.md); its HTML page is patchnotes-v<version>.html.

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
