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
