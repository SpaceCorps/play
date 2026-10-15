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
## 0.4.22 · 2026-10-15

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.22)

SpaceCorps 2027 0.4.22 adds Turkish as the 13th language, makes the P.E.T. Station an Extra with an ON and OFF switch (your P.E.T.s are silent until one is fitted and ON) and the Energetic Wall a consumable like the EMP Charge, lets a group hold ten pilots, sends a Crystalys with every Clan Warden's waves and puts every Warden after the pilot who hit it, fixes the Group window, the research queue and the Skylab's camera, and should fix the Windows 11 icon and alt-tab.

### What's new

**Highlights**
- **Turkish (Türkçe) is the 13th language:** the whole interface and all 61 wiki articles. It was written by AI and **no native speaker has read it yet**: tell us what reads wrong.
- **The P.E.T. Station is an Extra.** Fit it in an Extras slot and switch it ON or OFF with its PET slot on the hotbar. **Your P.E.T.s are silent until a Station is fitted and ON:** fit one after the update (if you had a Station, each ship you own got one). It is a docking ring on your hull; the ten P.E.T.s are small animated drones.
- **The Energetic Wall is a consumable** like the EMP Charge: a stack of up to 20 Wall I and 10 Wall II, one spent for each wall that stands. Your fitted and loose walls became one stack per level.
- **A group holds ten pilots,** up from five.
- **All nine Clan Wardens** send a Crystalys with each wave once under half their hull and fly at the pilot who hit them. **They are harder:** a Recruit Warden's best-case crew on x-2 grows from 28, 21 and 27 pilots to 43, 39 and 44.
- **The Daily Clan Quest resets at 00:00 UTC** for every clan, and so do the daily bonus and the Warden of the day.
- **Private messages:** `/m name text` (also `/msg` and `/w`), `/r text` answers.
- **Inventory:** drag a rectangle over empty space to select several items; a trash button deletes the selection after one question.
- **Skylab:** a better station view with a Labels switch; the Research tree scrolls to your pick and takes the arrow keys; the queue takes the Dark Matter of the whole queue; Solar makes 505 to 525 more power at levels 11 to 14.
- **The Ammo Printer and the Rocket Factory** stand on their pads. **The pulsar** is seen from anywhere on its map. **The Swamp's turret rockets** are 25 % faster and fly twice as far.
- **The Target window** shows an asteroid's tier and the chances of P.E.T. parts. **Davidski's stock** stands among the Auction's listings.
- **Smaller:** icon-only hotbar and Auction chips, the Shop's "Are you sure?" above ten, the clan on a Warden's kill feed line, a backup route to the server, fixes that should repair the Windows 11 icon and alt-tab, steadier Group window rows and six quiet sounds.

**If you already play: what changes for you**
- **Update the game.** A 0.4.14 to 0.4.21 game installs it as a patch when the job made one for it (a Linux AppImage game from 0.4.19), and downloads the whole package if not. A 0.4.13 or older game downloads the whole package.
- **A 0.4.21 game keeps working but misses the new screens:** its wall slot shows an infinity mark for your count, it has no PET slot (it can fit a Station but not switch it OFF), and a private message is an English line in its System tab. **The rules change on the server at once.**
- **Your P.E.T.s are silent until a Station is fitted and ON.** If you had a Station you got an item of its level for each ship you own, loose in the inventory; with every Extras slot full, unfit something.
- **Nothing you own is taken.** Your Energetic Walls became one stack of each level. **A wall stack is lost at the wipe unless it is in the Transport Cache** (a wall fitted on your active ship survived it in 0.4.21).
- **The Wardens are harder,** and the clan day is shorter or longer once, at the update (below). New texts in other languages have had no native review.

**Turkish**
- **`tr`, Türkçe,** is a language of its own in the language menu of the sign-in screens and in Settings > General > Interface Language; a computer set to Turkish starts the game in it.
- **All of it:** 8,288 messages (the same as English and every other language), the Help cards, the server's texts and the 61 wiki articles with their generated tables. The game's word list is written down in `docs/design/turkish-terms.md`; item, ship, alien and company names stay English, as in every language.
- **The register is informal (sen)** and the percent sign comes before the number (`%50`, `-%25 temel gövde`).
- **How it was made:** written by AI from the English, checked by tests (every message has its placeholders, no English is left, the Turkish letters and the dotted and dotless I are held) and by looking at screenshots. **A native speaker has not read it.** The places the writers were unsure of are listed for a proofreader in `docs/design/turkish-doubts.md`.

**The P.E.T. Station**
- **An Extra, fitted on one ship's configuration:** Station I, II and III hold 2, 3 and 5 docked pets. The three Station items are in the Extras picker, in the Hangar and in the Assembly like any Extra; research, recipes and prices are those of 0.4.21 (3 hours, 10 hours and a day of research; 100,000 Credits and 2,000 Thulium, 400,000 and 6,000, 1,500,000 and 18,000 to make). A Station II needs a Station I that you own, a III a II or better (carried, fitted or in the Transport Cache).
- **ON and OFF:** the **PET** slot of the hotbar switches the Station in flight and at once, one press a second, with a quiet sound of its own each way. ON is lit, OFF dim. **The switch is yours and is kept** when you land, die or sign in again. ON is where a Station starts.
- **What you were given:** each pilot who had a Station got **one Station item of his level for each ship he owns** (at least one), loose in the inventory; nothing is fitted for you, nothing is taken and your old install is left as it was.
- **What counts:** the boosts, the pets' EXP and the Mole's and the Retriever's work count only on a ship flying with a Station fitted and ON, and only for the first 2, 3 or 5 docked pets (the ones in the first places). **A docked pet that does not count earns no EXP**, as a stored pet earns none.
- **The Hangar** (landed) docks into the best Station you own (carried or fitted; not one in the Transport Cache), so you can arrange your pets before you fit one; the Hangar's P.E.T. page says "Not fitted" and "Not counted" where that is so.
- **The Station is yours to keep:** the wipe keeps the three Station items wherever they are, like drones and formations. They are not on the Auction.
- **What you see:** the Station is a **docking ring** over your hull with a berth for each place, and a berth lights in the colour of the pet docked in it. **The ten P.E.T.s are ten small animated models** (wings beat, legs walk, a hoop turns, claws dig); they fly out of their berths one after another when you switch ON and fly back and dock when you switch OFF, and the ring folds up dark on your own ship. Other pilots see your Station and your pets while it is ON (nobody sees an OFF Station but its owner). Reduce Motion takes the final state at once. At the default camera a pet is 4 to 6 pixels: zoom in. Low graphics draw a ring of light instead of the model.

**The Energetic Wall**
- **A consumable, carried like a rocket:** Wall I and Wall II are item type 23 like the EMP Charge, one stack for each level, on no ship and in no slot. **Wall I:** the Shop sells it for 250 Thulium a charge and stops at 20 carried (the card says "You carry N of 20"). **Wall II:** made in Assembly, **600 Thulium, 5 Ship Fragments and 1 Power Core for each charge**, after the same research (6 hours), up to 10 carried. It used to be a Wall I, 10 Ship Fragments, 2 Power Cores and 600 Thulium.
- **A press spends one charge** of the level the slot holds, and only when the wall actually stands: every refusal (a safe zone, a gate, a cloak, the 90 second wait) spends nothing and starts no wait. A slot holds a level and never falls back to the other one. At zero you are told "No Energetic Wall left." Pick them from the **Consumables** picker, which now lists the EMP Charge and both walls. The wall itself (360 units long, 10 wide, 30,000 and 90,000 hit points, 2,500 a second, gone in 60 seconds, at your cursor 120 to 450 units out) did not change.
- **When the server starts,** every wall you had (fitted, loose or in the Transport Cache) became one stack of its level, **none lost** (the step is refused if the count would change). A wall stack is lost at the wipe unless it is in the Transport Cache.
- **The Auction:** the Wall II is a kind (a lot of one, reference value 120,250, floor 61,000; it was 170,500 and 86,000) and the Wall I is never listed; Davidski's last-resort price of a Wall II falls with it, from 34,100,000 to 24,050,000 Credits. Five preset builds that fitted a wall (Iron Wall, Aegis, Bastion, Citadel, Leviathan) carry three with their rockets.

**Groups of ten**
- **A group holds up to ten pilots** (it held five): the Group window and the minimap show every member. Nothing changed on the wire except more rows.
- **A kill's pay is shared by level** among the members who fought it, as before. The pot is fixed, so ten members share what five did; **the killer keeps the rounding remainder** (a small Thulium or honor pot rounds to nothing for the mates).
- **The Group window** keeps its rows; with more than about seven members the list scrolls (or fold it to the strip, or drag any edge). On a 1024 by 640 screen its default height is shorter so that it never covers the hotbar's tabs. **Its rows no longer jump.** In a window narrower than about 239 points a mate's target stood beneath the bars and every row below moved 21 points whenever a mate selected a target or lost it: the room is always there now, so every mate's row is 21 points taller whether or not he shoots. At the default width the target stands beside the bars and the rows never moved; there the mates' bars are about 55 % of the column, with the room beside them.

**The Clan Wardens**
- **Every Warden sends a Crystalys:** all nine rows (Brood, Siege and Wrath, Recruit, Veteran and Elite) add one Crystalys to each wave once the Warden is under half its hull, as the Wrath Warden III did since 0.4.20. Waves keep their size and timing (3 alive, 60 seconds apart; the Wrath Warden III's 4 and 40 seconds); no hull, shield, damage or pay number moved.
- **Every Warden flies at the pilot who hit it,** each at its own speed (Brood 90, Siege 110, Wrath 90): the Brood Warden no longer stands still (its four drones go with it and keep healing it) and the Siege Warden, which roamed, now fires its Rivet at the pilot it chases. It lets go 10 seconds after the last hit and stands where it ended.
- **They are harder.** The model's best case (Alpha, the tier's own gear, x2 ammo) says the Crystalys takes the smallest crew on x-2 from 28, 21 and 27 pilots to 43, 39 and 44 for the Recruit Brood, Siege and Wrath Wardens, from 26, 19 and 25 to 39, 27 and 33 for the Veteran ones and from 18 and 22 to 21 and 26 for the Brood and Siege Wardens III (the Wrath Warden III had it already, at 32). The Recruit Wardens on x-4 need 69, 56 and 62, more than a level 3 clan's 50 (57, 52 and 56 before the Crystalys). **No row needs more than a level 5 clan's 100.** In Gamma, where the aliens of the waves are twice as strong, seven rows ask more than a level 3 clan's 50: the Brood Warden I on x-3 and x-4 (63 and 79), the Siege Warden I on x-4 (66), the Wrath Warden I on x-4 (73), the Brood Warden II on x-4 (58), the Wrath Warden II on x-4 (52) and the Wrath Warden III on x-4 (51). Nobody has played these fights.
- **The kill feed names the clan:** when a clan destroys its Warden the Global feed reads "Clan [TAG] Clan Name destroyed Brood Warden II" instead of one pilot. Pay and the clan line are unchanged.

**The clan day**
- **The daily line rolls at 00:00:00 UTC** for every clan at the same moment (it rolled at the time of day the season started). The countdown on the Operations tab, "Day n of 29", the daily bonus and the day's Warden follow it. A Warden of the day leaves at midnight and none is called in the last 30 minutes of the UTC day.
- **At the update the running day keeps its number and its progress** and ends at the next 00:00 UTC: it is shorter than 24 hours if the update lands after the season's old time of turn and longer if it lands before it. Every later day is exactly 24 hours. **The last line (29) runs until the wipe's countdown begins.** The season day (PvP, swarms, the wipe) is unchanged, so "Day 5" of a clan can read one ahead of the season's for some hours of a day.

**Private messages**
- **`/m name text`** (also `/msg` and `/w`) writes to one pilot who is online; **`/r text`** answers the last pilot who wrote to you (else the last you wrote to). It works in flight and at the station's chat dock.
- **You see "To nova:" and "From nova:" in violet** among the lines of the tab in view; an unread count lights the toolbar's Chat button, the dock and the sidebar's Messages row, and two quiet sounds tell sent from received. Right-click a name for Reply, Invite, Ignore and Report; **Ignore hides a pilot's private messages** and Report names the channel `private`.
- **The chat's rules apply:** 200 characters counting the command and the name, no links, the alphabet and spam rules and the send limit. The name must match exactly (never its beginning). An offline pilot is refused ("nova is offline."): nothing is stored. The server's log says who wrote to whom and how long it was, never the words.
- **A 0.4.21 game** is told the same line as "Private message from nova: text", in English, in its System tab; its own `/m` works.

**The inventory**
- **Drag over empty space** (the margin beside the tiles, a gap, the strip under the last row) to draw a rectangle: every tile it touches is selected as you drag. Shift, Ctrl or Cmd adds and toggles, Esc or a click on empty space clears, the list scrolls itself near its edge. The title row counts the selection ("9 selected") and has a clear button.
- **The one action is a bulk delete:** the trash button asks once, lists the items (six names, then "and 3 more"), and deletes them. **It is the same delete as the per-tile trash**; a stack of identical Extras goes whole. Items fitted in the Skylab cannot be selected. The tiles are about 6 pixels smaller to leave room at the sides. A very quiet tick sounds as the rectangle takes a tile (it follows Button Sounds).

**The Skylab**
- **The station view.** From the second Core on the camera opens at the angle that shows the whole station biggest (from the side of the chain), not end on; one Core keeps the classic angle. Picking a module frames it up close from its outer side; the idle turn is a sway of at most 32 degrees either way (about 20 on a Core 15) instead of a full turn; **Reset View** goes home.
- **A Labels switch** beside Reset View hides the module chips, the Core tags and the leader lines for a clean view. The "!" alerts (a full hopper, plates, ore for the Bay) and the dock row of modules not built yet stay. It is remembered on your computer.
- **The Research tree.** Clicking a technology brings its card into view (the card's top and buttons, so the queue stays in sight); picking from the queue, the running research's name or Open Research scrolls the tree to the node, and a filter that would hide your pick is let go. **The tree is one Tab stop and takes the arrow keys** (the nearest node; along a ship's ladder, the slots); Escape lets go of the keyboard and keeps the pick. A whole queue row picks, and a resize keeps the pick in view.
- **The research queue and Dark Matter.** The plug used to stop at the picked technology's own need, so five researches that need Dark Matter could never be covered. **Add** now fills the Research Centre up to the need of the whole queue plus the picked technology's, the queue card has an Add of its own, and each queued technology shows green with a check when its Dark Matter is covered or "Needs N more Dark Matter". **A queue that stopped for Dark Matter starts by itself the moment you add what was missing.** Take back works as before.
- **Solar's table:** entries 11 to 14 rise from 2,490, 3,055, 3,765 and 4,660 to 2,995, 3,565, 4,285 and 5,185 (**+505, +510, +520, +525**), so a Core 15 Skylab with the four expedition modules built no longer runs dark while Solar and the rest are still at 11 to 14. Nobody loses power; a producer that was dark resumes at the update.
- **The Ammo Printer and the Rocket Factory** stand on their pads at every level: the racks, halls, towers, cranes, fuel spheres, the great rocket and the Printer's drum no longer hang over the edge, and where a stage grows past its pad it has a foundation slab. Same footprint, same places for ports and chips.

**Danger Sectors and asteroids**
- **The pulsar is seen from anywhere on its map.** The picture of 0.4.21 stays whole to 5,100 units and fades by 6,500; beyond it a far star (a white-hot core, its two jets and a haze in the state's colour, a lighthouse swell twice a turn) shows when it is in the view, and a soft glow bleeds in from the screen's edge on its side when it is not. It is light only: nothing to click. Reduce Motion stops the breath and the swell.
- **The Dormant Swamp's rocket turrets:** the N.I.K.E. and the N.U.K.E. they fire are **25 % faster** (900 to 1,125 and 300 to 375 units a second) and **their flight is twice as long** (4,050 to 8,100 and 1,200 to 2,400 units; 7.2 and 6.4 seconds in the air). They start to fire at the same distance (3,640 and 1,080 units, inside the 4,300-unit zone); the rockets are still straight. A N.I.K.E. fired at a ship inside the zone now flies on to about 8,700 units from the swamp's middle, past the notice ring.
- **Asteroids say their tier and their P.E.T. parts.** The Target window and the hover card read "Iron · Medium · Tier 3" and a "P.E.T. parts" row ("Regular 0.8%, Mythical 0.15%", or "none" for tier 1). A tier is the ring of sectors a kind belongs to: tiers 1 to 4 are x-1 to x-4 and tier 5 the Danger Sectors. A Regular Cluster Chunk is 0.4 %, 0.8 %, 1 % and 1.2 % from tier 2 to 5, a Mythical one 0.15 %, 0.25 % and 0.3 % from tier 3, a Legendary one 0.03 % and 0.1 % from tier 4; the Motherlode 25 %, 8 % and 3 %. The Asteroid Mining page and its Help card say it.

**The Auction, the Shop and the lists**
- **Davidski among the listings.** His stock stands as rows in the Market, one for each item and currency (83 kinds make 166 rows), with a gold name and an NPC badge, sorted by price among the pilots', searchable and filterable like any listing; the separate Davidski tab is gone. Click a row for the details and Buy: prices, "last resort" badges and "can never be listed again" are as in 0.4.21, and a row looks the same whether he flies today or not.
- **Icons only.** The five picker buttons above the hotbar (Ammo, Rockets, Extras, Consumables, Formations) show an icon and a caret; hover for the name. The Auction's category chips are an icon and a number, on one row at 1280 by 720. **Every kind of item has the same icon** in the Hangar, the Auction, the Shop and the hotbar; the Hybrid Generators have a plug with a bolt (they looked like drones). The Hangar's chips were icons already; All and None stay words.
- **The Shop asks "Are you sure?"** before more than 10 of an item that is not a consumable is bought (laser amps, shield cells, lasers, drones, hull plating and so on): the sheet shows the item, how many and the total price; Cancel is the default, Escape cancels, and nothing answers it for 0.4 seconds. Ammo, rockets, the EMP Charge, boosters and resources never ask.

**In flight and at the station**
- **The backup route.** If the usual address does not answer within 6 seconds the game asks the backup address `https://play.spacecorps.xyz` as well and goes to the first that answers ("Trying another route…", then "Connected via backup route", also in Settings > Account). **The usual address is asked first at every start;** an address you typed yourself is never replaced.
- **The Windows 11 taskbar icon and alt-tab: two fixes that should work.** The game now gives Windows its icon in the sizes the taskbar asks for, with its own taskbar identity and an application manifest; **if you pinned the game to the taskbar, unpin it and pin the running game again once.** When the window is minimised or alt-tabbed (a screen under 200 by 120 points) the HUD keeps its layout instead of squeezing every window into the corner and saving that. **Neither has been tried on Windows 11 or on a real alt-tab:** if it is still wrong, send `spacecorps2027.log` (the lines "taskbar identity:", "window icon:" and "window:").
- **Spacing.** The Recipe Book and Builds use the margins of the rest of the game: the list and the detail no longer touch the dividing line, cards stand 12 points apart like the Hangar's, and Builds' cost column ends at the window's edge.

**What you see and hear**
- **Six new quiet sounds,** each with its own cue and on the Sound Effects volume: the Shop's question, the inventory's tick, a private message sent and received, and the Station ON and OFF.
- **One new Help card** (the P.E.T. Station), and the cards of the P.E.T.s, the Asteroids, the Power, the Chat and the clan line updated. **The wiki has pictures on all 61 pages** (163 pictures: the Skylab's new sheets, P.E.T.s, Davidski, the Recipe Book, the Auction), and every new text is in 13 languages.

**For administrators and the server**
- **At the first start:** three data steps (`skylab-solar-v7`, `wall-stack-v1` and `pet-station-extra-v1`, each with its `DataMigrations` row), one new table (`ClanDayClock`) and one guarded `ALTER TABLE` (`PetState.StationOff`), all idempotent; the backup gate lists 5 lines. No data file is new and seven changed (`Builds.json`, `ClanLines.json`, `ClanWardens.json`, `DormantSwamp.json`, `Groups.json`, `Market.json`, `SkylabConfig.json`), with the item and recipe seeds. One new route, `POST /api/admin/players/:id/forge/max`; one new client feature string, `private-chat`; three optional environment variables of the front door (`TRUSTED_PROXIES`, `TRUSTED_PROXY_HEADER`, `TRUSTED_PROXY_SECRET`, off unless `TRUSTED_PROXIES` is set) and two dry-run switches (`WALL_STACK_V1_DRY_RUN`, `PET_STATION_V1_DRY_RUN`).
- **Admin tools:** **Max Forge** (Admin > Players > Inventory) sets chosen pieces of a pilot's equipment to the top of the Forge at no cost (Eternal, every buff at the top of its range); pieces in the Transport Cache, fitted in the Skylab or listed on the Auction are left alone and reported; **a piece keeps its Marketable label**, so a maxed piece that was Marketable can still be sold on the Auction (an admin power the owner may want to limit); 1 to 200 pieces a request, 20 requests an admin per 10 minutes, every use in Recent admin actions.
- **The release job:** the patch notes go in a `patchnotes/` folder of the download site (the one-time move is a script that is not part of the deploy), `scripts/clips/*` is a docs path, and the Windows build checks the exe's icon, manifest and version resources.
- **There is no safe rollback to 0.4.21 after the first start,** and no volume backup is taken (the owner does not want one): a 0.4.21 server reads the wall stacks as Extras again, lets a pilot fit a stack in a slot and the walls come out wrong. The way is forward, a fix release (docs/DEPLOY.md).

## All releases

Each line links the full notes of that release as Markdown (patchnotes/v<version>.md); its HTML page is patchnotes-v<version>.html.

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
