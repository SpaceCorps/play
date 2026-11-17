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
## 0.5.8 · 2026-11-17

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.5.8)

SpaceCorps 2027 0.5.8 is the alien tiers and Galaxy Gates update. Aliens now wear a Greek letter for their tier and pay by it, the Materializer lets you pick a category of gates and every gate needs new part counts, the clan dungeon boss hits harder and has a new ability, the Storm RECON gets Target and Slow, and your own rocket blast hurts you. It also brings controller support, a new font and skins for the Miyuki and for the clan LOU, and phone controls in the code only. The web version at web.spacecorps.xyz is live too (it has been up since 2026-11-15). Nobody has flown most of the new numbers yet.

### What's new

**Highlights**
- **Alien tiers:** a Greek letter in front of an alien's name shows its tier: Alpha, Beta (1.5 times as tough, pays 2 times), Gamma (2 times, 3 times) and a new Delta (4 times, 6 times). Each world rolls the tiers of its aliens from a table.
- **Galaxy Gates:** the Materializer asks for a category: the Chrono-Gate, Alpha-Beta-Gamma or Delta-Omega. The part counts are new (Chrono-Gate 13, Alpha 14, Beta 33, Gamma 68, Delta 96, Omega 119), the completion's ammo is 75 % of what it was, and Alpha Rift's aliens are 4 times as tough as the definition (2 before) at the pace of the other gates.
- **A harder clan dungeon boss:** from stage 2 it fires at two pilots at once, the Rocket barrage hits every pilot for 50,000 to 75,000, the Meteor drop is 30 % wider and hits twice as hard, and a new ability, Phantom's Lance, brings two illusions that heal it. Clan dungeons pay four times the Echo Shards of 0.5.7, and the five aliens that drop them do so twice as often.
- **Storm RECON:** Target (+20 % damage taken for 5 s), Slow (60 % slower for 4 s) and a 3 second Ambush bonus when its own attack ends the cloak.
- **Your own rocket blast hurts you** for half of what it does to others, the N.U.K.E. too.
- **Pilot Skills:** a new skill, Cloak Recharge; Antimatter now runs up to x2.00; and Wipe Points for skill levels 10, 25, 50, 75 and 100.
- **A cloak survives a safe zone** and a portal jump.
- **Skins:** a Miyuki skin in every collection (63 skins in 12 collections now) and a LOU collection for the clan LOU.
- **Phones and pads:** thumb layout and quick wheel for phones and a two-finger turn (all three are for the Android and iOS apps, which are not part of this release's downloads), Xbox and PlayStation controllers on computers. **The web version** at web.spacecorps.xyz runs the game in a browser (up since 2026-11-15). **A new font** (Ubuntu) on every system.
- **Balance:** THUNDER, BUCKY, DUMA, NOTSUM and BRATAN change, Facets hit 1.5 times harder, and the group share radius is 8,000 units.
- **Premium** no longer doubles experience.

**New**
- **Alien tiers.** Every ordinary alien the sky respawns rolls a tier when it appears, from the table of the world it is in, and its name shows it: `-=α-Seeker=-` on its name tag and in the Target window. The tier multiplies its hit points, shield, shield recharge and damage (its rocket too) and what its kill pays: credits, Thulium, experience and honor, and the experience of your drones and P.E.T.s. The loot is as it was.

  | Tier | Letter | Tougher by | Pays |
  |---|---|---|---|
  | Alpha | α | 1x | 1x |
  | Beta | β | 1.5x | 2x |
  | Gamma | γ | 2x | 3x |
  | Delta | δ | 4x | 6x |

  | World | Alpha | Beta | Gamma | Delta | Whole world against before |
  |---|---|---|---|---|---|
  | Alpha world | 90 % | 9 % | 0.9 % | 0.1 % | 5.7 % tougher, 11.3 % more pay |
  | Beta world | 4.9 % | 90 % | 4.9 % | 0.2 % | 0.3 % tougher, 0.4 % more pay |
  | Gamma world | 0.1 % | 4.9 % | 90 % | 4.9 % | 3.6 % tougher, 3.2 % more pay |

  The Gamma world's row adds up to 99.9 %; the game divides by the sum it finds, so the Gamma world's figures are 3.6 % and 3.2 % (3.5 % and 3.1 % without the division). The number of aliens a map holds does not change. Swarms (leaders and followers), Davidski, the Dormant, a Clan Warden's waves, the aliens of a dungeon and the admin's spawns wear no letter and keep what their world gives. The Game Log line stays `You killed Seeker. REWARDS: ...`. The Help's Worlds card says it in 13 languages. Only ordinary sky aliens wear a letter, and a solo gate's kills pay by the kind, not by the tier.
- **The Materializer asks for a category.** Pick the **Chrono-Gate**, **Alpha-Beta-Gamma** or **Delta-Omega**. A spin still costs 100 Thulium and finds a part with 13 % in every category; the part belongs to one gate of the category, all equally likely: the Chrono-Gate alone gets all of it, Alpha Rift, Beta Breach and Gamma Foundry 4.33 % each, Delta Siege and Omega Vault 6.5 % each. The guarantee (the chance rises after 24 spins in a row without a part, certain after 47) is one counter for all categories. A complete Chrono-Gate shuts its category, and a multi-spin of it stops at the spin that completes it. A game from before 0.5.8 has no picker: a Thulium spin without a category is answered "Update the game to spin the Galaxy Gates." and charges nothing.
- **New part counts for every gate.** The parts of a run and what they cost on average with the guarantee, when you scan the gate's own category:

  | Gate | Parts (0.5.7) | Thulium on average with the guarantee (0.5.7) |
  |---|---|---|
  | Chrono-Gate | 13 (2) | 9,851 (9,093) |
  | Alpha Rift | 14 (11) | 31,825 (50,011) |
  | Beta Breach | 33 (26) | 75,016 (118,208) |
  | Gamma Foundry | 68 (54) | 154,579 (245,508) |
  | Delta Siege | 96 (87) | 145,486 (395,541) |
  | Omega Vault | 119 (108) | 180,343 (491,017) |

  A part of Alpha Rift to Omega Vault is found two to three times as often as on the old wheel of six gates (4.33 % a scan in Alpha to Gamma and 6.5 % in Delta and Omega, against 13 % / 6 = 2.17 %), because you scan one category. So the parts of a run cost less Thulium on average in five of the six gates. The Chrono-Gate is the exception: a part of it is found six times as often (13 % a scan), but it needs 6.5 times the parts and a run costs a little more (9,851, was 9,093). Known limits says what a pilot who spends all his Thulium on one category gets. The wipe still takes the Chrono-Gate's parts and leaves the solo gates' parts.
- **The completion's ammo is 75 % of what it was** (the swarm leaders' loot and the consolation prize of a spin without a part are as they were):

  | Gate | Advanced Plasma | Ultra Core | Experimental Fusion Core |
  |---|---|---|---|
  | Alpha Rift | 15,000 (20,000) | 3,750 (5,000) | 15,000 (20,000) |
  | Beta Breach | 37,500 (50,000) | 15,000 (20,000) | 22,500 (30,000) |
  | Gamma Foundry | 22,500 (30,000) | 45,000 (60,000) | 37,500 (50,000) |
  | Delta Siege | 30,000 (40,000) | 67,500 (90,000) | 56,250 (75,000) |
  | Omega Vault | 37,500 (50,000) | 75,000 (100,000) | 75,000 (100,000) |
- **Alpha Rift: normal pace, tougher aliens.** It had a pace of its own (0.46 aliens a second); now it releases them at the run's 4 a second like the other gates, and its aliens have 4 times the hull and shield of the definition (2 times before).
- **The aliens of a solo gate's waves wear tiers too,** for their strength only: 31.7 % Alpha, 31.7 % Beta, 31.6 % Gamma and 5 % Delta. A wave takes as long to destroy on average as before, but the damage you take rises (see Known limits). What a gate kill pays is the kind's, not the tier's.
- **A portal is sent only to its owner.** The server no longer sends the portal of your solo gate to other pilots (0.5.7 only hid it in the game).
- **All gates can be built at once.** You may have every solo gate (Alpha Rift to Omega Vault) built at the same time, each with a portal of its own in your home sector, and you play one at a time: while you are in an arena none of your portals stands, and they come back when you are out. Only the gate you have already built is refused ("That gate is already built. Go in through its portal or abandon it first."); another gate is built as usual when you have its parts. Resume and Abandon name the gate they act on. Your own portals stand 1,200 units apart; another pilot's portal may stand on the same spot as one of yours, because each portal is sent only to its owner. Changed in code and tests (the real server ticker over the real gate data); nobody has played with five gates built.
- **The clan dungeon boss (the Dungeon Warlord).** It fires its laser at **two pilots at once from stage 2** (the two nearest it can see, each takes a whole volley; one pilot in stage 1). **Rocket barrage** now sends a rocket at **every** pilot it can see, one every 15 seconds for 45 seconds, for 50,000 to 75,000 (62,500 to 93,750 at stage 2, 75,000 to 112,500 at stage 3); it was 26,000 (32,500, 39,000) at random pilots. **Meteor drop:** the ring is 546 units (420) and a meteor does 80,000, 100,000 and 120,000 by stage (40,000, 50,000, 60,000). **Phantom's Lance** is new: the Warlord vanishes for a second and comes back somewhere in its room with 2 illusions of 500,000 hull. While an illusion lives it fires 50 % of the Warlord's volley at the nearest pilot it can see and heals the Warlord 50,000 hull and 50,000 shield a second (100,000 and 100,000 with both). Illusions pay nothing, leave with the Warlord, and the Warlord can be destroyed while they live.
- **More Echo Shards.** The five aliens that drop an Echo Shard do so at twice the chance, wherever they die: Seeker 0.8 %, Phantasm 2 %, Bulwark 4 %, Goombah 10 %, Crystalys 40 % a kill (0.4, 1, 2, 5 and 20 % in 0.5.7). A paid clear of a clan dungeon gives 12, 8 and 8 Echo Shards for stages 1, 2 and 3 (3, 2, 2 in 0.5.7), and the aliens' boxes inside a dungeon drop Echo Shards at twice the new chance, four times the chance of 0.5.7 (Goombah 20 %, Crystalys 80 %). The Lattice Shards, the Heartshards and what a solo gate's completion pays in shards (Alpha Rift 4 Echo and 6 Lattice up to Omega Vault 34 and 54) did not change; a gate's kills pay the doubled chances, so a run gives 28 % (Alpha Rift) to 38 % (Omega Vault) more Echo Shards than in 0.5.7. A full piece (150 Echo Shards) now takes a clan pilot about 4 hours of play by the model, 11 in 0.5.7; nobody has played it.
- **Storm RECON gets three buttons.** **Chameleon** (as before; a safe zone no longer breaks it), **Target** (a selected enemy ship within your laser range takes 20 % more damage from everyone for 5 seconds, the Marking Rocket's effect) and **Slow** (it flies 60 % slower for 4 seconds), each recharging in 60 seconds. Target and Slow need an enemy pilot or alien selected, work only within laser range, not on your group or company and not in a safe zone, and they count as an attack: they end the cloak. When your own attack ends the Chameleon you get an **Ambush** for 3 seconds: 25 % more damage and 25 % more speed.
- **Your own area blast hurts you.** Every rocket that bursts (a blast, the N.U.K.E. too) now counts the pilot who fired it among the ships it can hurt, for half of what the same blast does to a ship at his distance. You can be destroyed by it. A group mate is never hurt by your blast. A safe zone, a respawn's protection and an Energetic Wall between you and the burst spare you as they spare every ship. Direct rockets and alien rockets are unchanged.
- **A cloak survives a safe zone and a portal jump.** The Cloaking CPU and the Chameleon no longer end when you enter a safe zone (the CPU's Help card and the wiki say so); you still cannot start one inside a safe zone's ring.
- **Pilot Skills: Cloak Recharge, the 21st stat** (Combat, governed by Reflex). The recharge that starts when a cloak ends runs x1.00 at level 1 (60 seconds), x0.75 at level 50 (45.2 s) and x0.50 at level 100 (30 s), for the Cloaking CPU and the Chameleon. It trains with 0.1 XP for every second you are cloaked, only on a ship that is alive, outside a safe zone and flown in the last minute. The numbers are first values.
- **Antimatter runs up to x2.00.** x1.00 at level 1 to x2.00 at level 100 (it was x1.25 at most) in a straight line, so level 2 is x1.0101. The rounding is fair: a line of Dark Matter is the whole part of quantity times the factor and one more with the chance of the fraction. The black hole lays boxes of one unit now, so a box from it pays one or two depending on the level (exactly one at level 1, exactly two at level 100), and its map keeps 52 boxes (32). Boxes from other sources double as the skill says (a Tesseract box of 5 pays up to 10).
- **Wipe Points for skill levels.** Every stat pays Wipe Points the first time it reaches level 10, 25, 50, 75 and 100: 2, 5, 10, 20 and 40 (77 for one stat, 1,617 for all 21). Once ever for each stat and level, wipes do not take them back. Claim them with one button on the Season page; a pilot who is already above a level is paid it at his first claim.
- **Miyuki.** A link (Channel Heal and Channel Shield) can be put on an enemy pilot or alien too: it heals or shields whoever it joins, you get no Healing XP for an enemy, and a boss of a dungeon or a gate cannot be linked. A link to a ship that was destroyed says "destroyed", not "left the map". The five levels are one row of their own in the Shop's Ships category, and the Research tree draws an arrow from each level to the next. The Support Rocket stays friend-only.
- **Skins.** A Miyuki skin in each of the 12 collections, worn by all five levels. A new collection, **LOU**, for the clan LOU: Bloody R.E.D's black body with deep violet lights and no logo, for the Paragon, Storm, Ironclad, Wraith and Miyuki. The LOU skins have no in-game route yet: an administrator gives them to the clan's members. The catalogue has 63 skins in 12 collections (47 in 11 before). No skin has a Thulium price, and the update gives nobody a Miyuki skin: hers are found the way the other ships' skins are: nine of the collections in the Chroma Archive (which hands out one skin for one ship, for your active ship first, as in 0.5.7), the Abductee's from the same Archive for a pilot who finished the Static, and an administrator gives those of Bloody R.E.D and LOU.
- **Forge: one Upgrade view.** Tier up and Sockets are one view now (Upgrade | Merge): the ladder and the Tier up block first, the Sockets below. Rules and prices are as in 0.5.7.
- **Clan Members list: Last seen.** A column says how many whole days ago each member played ("Today", "1 day ago", "12 days ago"), amber from 14 days and red from 30. Only members of the clan see it, about their own clan, and a pilot cannot switch it off. A pilot with no record reads a dash.
- **Chat tells when a pilot is muted, kicked or banned:** every pilot connected to Home reads "{name} was muted by an admin." (or kicked, or banned), flying or at the station, in any world. It names only the pilot. Pilots flying on a regional server do not see it.
- **Phone controls.** On a phone the flight controls stand on three arcs round the right thumb with badges on Attack and Rocket, the ship's abilities at seats under it and a Config switch; a virtual stick flies; a slim HUD replaces the toolbars. **Quick bar** in Settings is Hotbar (the default) or Wheel: a hold of 0.35 s on Attack or Rocket, or a touch on the Items button, opens a ring of choices. **Two fingers dragged across turn the view** and a phone's camera stays where you put it by default. **The Android and iOS apps are not part of this release's downloads,** and by the game's code a computer or a browser does not use the phone layout, so these controls reach no pilot with this release's downloads.
- **Gamepads.** An Xbox, PlayStation or other Bluetooth or USB controller works in flight on a computer (run on Windows with a scripted pad only; the Linux x86_64 package builds with the pad code, but no pad was used on Linux, macOS was not built or run, and the Android code was never run): the left stick flies, right stick zooms and turns, A attacks, X selects the nearest, Y fires the rocket, bumpers choose ammo and rockets, LT is the ship's ability, RT the hotbar. Settings, Controls lists it under Controller. No flight sticks (no HOTAS), no iOS, no web.
- **The web version** at web.spacecorps.xyz runs the game in a browser; it has been up since 2026-11-15. A web player chooses the server to fly from as on a computer. In a browser the game leaves out Steam, the updater, gamepads and the system fonts: Japanese, Korean and Chinese texts are drawn as boxes (a fix is planned for the next patch).
- **A new font.** Ubuntu Light, with Ubuntu Medium and Bold and Hack for monospace, are the faces on every system and in the browser (before, each system drew its own font). Japanese, Korean, Chinese, Thai, Arabic and Hebrew texts still use the system's faces on a computer. Layouts were retuned for the new font (a line is shorter, the letters about 1 % wider). The font files are in the program, and the Ubuntu Font Licence travels with the game's files.
- **Premium.** The Level and Premium help cards no longer say that Premium doubles experience, and the Thulium page lists no perks: for now Premium gives no gameplay advantage and shows a Premium badge on your pilot. Premium is not on sale yet (the Thulium page says "Not available yet"). The Thulium page now also says what is planned for Premium: "Planned for Premium, not available yet and subject to change: emoji support in chat, a reaction wheel and chat translations." The Steam build's Thulium page has no Premium text. The Premium help card says the same once the offers open. None of them is a gameplay advantage.
- **Admin menu modes (administrators):** infinite ammo and rockets, no cooldowns for the admin's own ship.

**Changed**
- **THUNDER, BUCKY, DUMA, NOTSUM, BRATAN.** THUNDER loses the 25 % hull penalty (128,000 hull, 96,000 before; still +40 base speed and +1 laser slot, 11 lasers). BUCKY loses the minus 1 laser slot (10 lasers, 9 before). DUMA's laser penalty goes from minus 3 to minus 2 slots (6 laser slots, 5 before) and its shield absorption from +10 % to +15 %. NOTSUM and BRATAN get +5 % all damage, which also lifts the two Library builds that use them. Converting a Paragon to THUNDER now takes 5 Dark Matter Plates (4) and to BUCKY 6 (5). A THUNDER you already own keeps its share of hull: its saved hull is scaled by 128,000 / 96,000 once.
- **The Storm RECON's design lines name all three buttons.** The Assembly's recipe, the Shop's design rows, the Hangar's badge and card, the Target window and the wiki's Ship Designs and Storm pages say Chameleon, Target, Slow, not Chameleon alone. A game of 0.5.7 still says Chameleon only.
- **Tesseract Facets hit 1.5 times harder:** 834 in Alpha, 1,251 in Beta and 1,668 in Gamma (556, 834, 1,112).
- **The group share radius is 8,000 units** (4,000): group mates alive and within 8,000 units of a wreck share the kill, and a clan counts the kill once by the same radius.
- **The hidden series of missions** pays 10 Orvium Reinforced Plates more for each mission, on top of what it paid.
- **The Help's Cloaking CPU card** no longer lists a safe zone among what ends a cloak.
- **Premium gives no experience bonus.** Until 0.5.7 an active Premium doubled the experience you earned from kills and quests; now it is paid 1.0 times. The Quests, Groups and Dungeons wiki pages no longer list Premium among the reward boosts.
- **The guards of a swarm keep their target.** A follower of a swarm (the guards of a Crystalys, for one) that had been hit once, long ago, let go of a pilot on the very next tick when he shot its leader. It keeps him now while its attackers are still shooting.

**Fixed**
- **US East and Singapore joins:** a pilot could be refused when he joined a regional server because an item made on that server took the number of an item of another pilot. The servers count their own new items from 1,000,000,000 now, and a refusal names no other pilot. This is changed in code and covered by unit tests; it has not been seen live on a regional server.
- **An administrator's mute holds on Singapore and US East.** A muted pilot is refused in Local, Group, Clan, Global and private chat on a regional server too, with the same line "You are muted by an admin.", and Home drops the Global and Clan lines a node pushes for him; a mute set or lifted while he flies reaches him within one beat (5 seconds). In 0.5.7 it did not reach a pilot flying there. A regional server of 0.5.7 keeps only Home's drop of his Global and Clan lines. Tested against a real Home and two node states; not seen on a deployed server.
- **Loot pop-up and Game Log:** the pop-up (4 times the Antimatter skill's 1.25 = 5) was right and the log said 4. The Game Log now has a "Collected: ..." line with the amounts you were paid at every pick-up (not for asteroid chunks).
- **Dormant Knowledge:** the card said "146 of 146 researched" and the server counted 129. The card counts only the technologies that count for knowledge, as the server does.
- **Blink:** the light no longer swells or glitches when the ship faces away from the camera. Tests keep the streak's size sane for every heading, and a scripted real-client run drew it before and after; no pilot has seen it.
- **A Miyuki's ability buttons** keep their places and keys under the "Ship destroyed" dialog.
- **Android camera:** two fingers dragged across turn the view; before only the vertical move worked. This is changed in code; no real phone has run it.
- **Wiki and Help texts** follow the game: the Shields page (DUMA +15 %), the Tesseract page (Facets 834 / 1,251 / 1,668), the Dungeons page (12 / 8 / 8 Echo Shards, ring 546), the Alien, Forge and Resources pages (the Echo Shard chances), the Solo Gates and Rockets pages, the Extras page (the Cloaking CPU) and the Help cards in 13 languages.

**Servers and privacy**
- **The server and the game go live together, on all three servers.** Home (Helsinki), Singapore and US East must run the same build: two tables are new at Home, the flight data of a regional server changed, and a game or a node of 0.5.7 does not take the new part counts.
- **Two new tables at Home only** (a regional server's copy of each stays empty): the Stripe customer number of a pilot who buys Premium (no card data; deleted with the account, which first cancels subscriptions at Stripe) and the record of which skill levels paid Wipe Points (deleted with the account; no wipe touches it).
- **Clan members see the days since a clanmate last played** (see New). Nothing new is stored for it: the server reads the days it already keeps.
- **The web version** is allowed to call a regional server directly only where that server lists the page's address.

**If you already play**
- Update the game; the server and the game go live together. A game from before 0.5.8 cannot spin the Materializer ("Update the game to spin the Galaxy Gates." and nothing is charged), does not show tier letters and flies as before otherwise.
- **The update moves no Credits, Thulium or items.** It converts your **gate parts** once with `floor(parts held x new parts needed / old parts needed)`, so a complete gate stays complete, an empty one stays empty and a partial one is rounded down: the Chrono-Gate 0, 1 or 2 of 2 becomes 0, 6 or 13 of 13; Alpha 11 becomes 14, Beta 26 becomes 33, Gamma 54 becomes 68, Delta 87 becomes 96 and Omega 108 becomes 119 (5 of 11 Alpha parts become 6 of 14). The parts already paid into a gate you built and not finished are converted the same way, so a wipe (or an administrator's abort) gives back whole new parts. Abandon, as before, gives none back.
- A THUNDER you own keeps its share of hull (see Changed). Pilots already above a Pilot Skill level of 10, 25, 50, 75 or 100 are paid those Wipe Points at their first claim on the Season page (the first claim of a pilot with every stat at level 100 is 1,617).
- A pilot with an active Premium no longer earns double experience. His days are not touched.
- A pilot who held every skin of a collection now lacks its Miyuki skin. Nothing is given back: for the nine collections of the Chroma Archive (and the Abductee's, for a pilot who finished the Static) the collection can drop again for him and the Miyuki skin has to come out of a Chroma Archive; an administrator gives that of Bloody R.E.D and LOU.

## All releases

Each line links the full notes of that release as Markdown (patchnotes/v<version>.md); its HTML page is patchnotes-v<version>.html.

- [0.5.8](https://spacecorps.github.io/play/patchnotes/v0.5.8.md) · 2026-11-17 · The alien tiers and Galaxy Gates update.
- [0.5.7](https://spacecorps.github.io/play/patchnotes/v0.5.7.md) · 2026-11-15 · The Forge Sockets and Miyuki update.
- [0.5.6](https://spacecorps.github.io/play/patchnotes/v0.5.6.md) · 2026-11-12 · The Pilot Skills and Galaxy Gates window update.
- [0.5.5](https://spacecorps.github.io/play/patchnotes/v0.5.5.md) · 2026-11-11 · A quick patch for 0.5.4: the five solo Galaxy Gates can be entered now.
- [0.5.4](https://spacecorps.github.io/play/patchnotes/v0.5.4.md) · 2026-11-11 · The balance patch and the first release of the Pilot Skill Tree, the six Galaxy Gates and Mines.
- [0.5.3](https://spacecorps.github.io/play/patchnotes/v0.5.3.md) · 2026-11-09 · The patch for the regional servers.
- [0.5.2](https://spacecorps.github.io/play/patchnotes/v0.5.2.md) · 2026-11-08 · Rebalances the ships: every base ship has new hull, speed and laser numbers, the thirteen designs follow their ships…
- [0.5.1](https://spacecorps.github.io/play/patchnotes/v0.5.1.md) · 2026-11-06 · Reworks the Clan Gates: the maze is the whole map under fog, the party starts together from a shut room…
- [0.5.0](https://spacecorps.github.io/play/patchnotes/v0.5.0.md) · 2026-11-04 · The PvE update: clans open Gates, mazes with a Warlord at their end, three boss swarms and the Tesseract mothership roam the sectors…
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
