# Recipe Book and Builds

<!-- wiki-search: recipe; recipes; recipe book; bill; steps; chart; craft tree; what do i need; build; builds; loadout; preset; presets; import; export; json; my builds; share a build -->

The **Recipe Book** answers "what does this take?" for any item in the game: a chart of what it is made from, the steps in order, the full bill and where every raw item comes from. **Builds** does the same for a whole ship: import your Hangar loadout or a friend's build, start from one of 15 presets or make your own, and see its stats and its full cost, step by step. Both are in the station's **Library**, under the Wiki.

The Recipe Book keeps no list of prices of its own: it works its numbers out as you look, from the recipes, prices, technologies and drop tables that the Shop, [Assembly](/wiki/06-Items/Overview.md#upgrading-modules) and [Research](/wiki/03-Mechanics/Research.md) use, so it follows the game when a price or a recipe changes. That is why this page quotes no price and no stat: open the item or the build.

![The Builds page: the presets from early to late, and a build with its lasers, generators, extras and drones laid out in slots](../img/wiki-img/shots/builds.jpg)
![The Bill tab: what the item takes in Credits, Thulium and raw items, with what you have and what is missing](../img/wiki-img/shots/recipe-book-bill.jpg)
![An item in the Recipe Book: its ways to get it, the switches for the bill and the chart of what it takes down to the raw items](../img/wiki-img/shots/recipe-book-chart.jpg)

## Open it

Open the station menu and choose **Library › Recipe Book** or **Library › Builds**. The Recipe Book remembers the last item you looked at, its filters and its zoom, on this computer only; your builds are not part of that ([Saved on your account](#saved-on-your-account)). When the game is newer than the server it talks to, the pages say so and show less: the Recipe Book still works out everything that is bought, crafted or upgraded, but cannot say where the world gives an item (it just says "Get"), and Builds names the parts that need the newer server: the presets, My builds and the stats.

## Find an item

The big list on the left holds every item of the game, grouped by type and, inside a type, in the game's own order: the weakest tier first. The EMP Charge, the one consumable, is in it.

- **Search.** Start typing anywhere on the page and the text goes to the search field. The list becomes one list ranked by how well the name matches (the whole name, the start of it, the start of a word, any part of it, then the type). Capitals and accents do not matter, and the old name of a renamed item finds the item. `Esc` clears the search.
- **Type.** The drop-down above the list narrows it to one type and says how many items each type has. The switch beside it sorts A to Z inside each type.
- **Rows.** A row shows the item's picture, name, type and rarity, a small glyph for the way you would normally get it (made in Assembly, sold in the Shop, dropped or found, pressed, or made in the black hole) and a check when you have it.
- **Keys.** The arrow keys, Page Up, Page Down, Home and End walk the list, and `Enter` moves to the chart. `Alt+Left` and `Alt+Right` go back and forward through the items you opened.

## The chart

Click an item and the right side shows it. At the top are its picture, name, rarity and type, and a chip for every **way** to get it: **Craft** (in Assembly, with its time and cost), **Buy** (in the Shop, with its price), **Press** (from ore, in the Skylab's Forgery), **Drop** (the world gives it: aliens, rocks, rewards) and **Make** ([Dark Matter](/wiki/03-Mechanics/Dark-Matter.md), from N.I.K.E.s shot into the black hole). The filled chip is the way the chart and the bill follow; click another chip to follow that one instead. If you have not researched what lets you craft the item, a line says which technology and how long it takes, with a button that opens Research.

The **Chart** draws the item as a tree from left to right: the item at the left, what it is made from to its right, down to the raw items.

- Each box shows the item, how many of it you need and a glyph for how it is got (the glyph of that way's chip above; hover the box for the words, so the colour is never the only sign). A lock says its technology is not researched yet, and a green check with a number says how many of it you have.
- A box with branches has a small handle that folds them away; the deep branches of a big tree start folded. **Expand all**, **Collapse all**, **Fit** and the zoom buttons are above the chart.
- Click a box to read its card under the chart: the item, the ways to get it (click another chip to follow that way), what the way takes (a craft's runs, time and cost, or its price in the Shop), how many you have and, for a locked box, the technology it needs. Double-click it, or press `Enter`, to open that item in the Recipe Book. The arrow keys move from box to box, `Space` folds a branch and `0` fits the chart. Scroll to move around; `Ctrl` and the wheel zoom.
- An item that is only bought or found is a single box that says "Nothing to craft: it is bought or found. See Sources."

In a wide window the chart takes the left and the other panels sit in a column at its right; in a narrow one the tabs **Chart**, **Steps**, **Bill**, **Sources** and **Used in** show one panel at a time.

## Steps and the bill

Under the header, three controls decide what is counted: **How many** copies you want, **Count what I own** (on: what you already have is taken off) and **Include what is fitted** (off: a piece fitted on a ship is not counted, because crafting an upgrade uses a piece up and a fitted one would leave its slot).

- **Steps** is the chart as a numbered list, in the order to do it, in groups: Research, Get, Buy, Press and craft, and From your stock. Research comes first because Assembly crafts nothing before its technology is researched. Each step says what and how many, what it costs and how long it takes, and a Get step can show where to get it. **Copy steps** copies the list as text.
- **Bill** adds it up: your Credits and Thulium against what you have, every raw item with what you **Need**, **Have** and are **Missing**, the Dark Matter the research takes, the time to craft and press, the time to research (one technology at a time) and a **Value**. The Value is a way to compare two ways of getting an item, with Thulium and the things you have to find counted in Credits: it is not a price. **Copy bill** copies the bill as a table you can paste into a chat or a note.

## Sources and Used in

- **Sources** says where the world gives the item and every raw item the plan needs, by kind: aliens, asteroids and rocks, swarms, the Dormant Swamp, Clan Wardens, [Davidski](/wiki/03-Mechanics/Davidski.md), Skylab expeditions, the Giant Excavator, Skylab production, quests, Invite Friends and the starter kit. A row names who gives it and where, the chance and how many. "Also at" lists the [Auction](/wiki/03-Mechanics/Auction.md), Davidski's stock and other pilots. A chance is a chance, not a rate per hour: how long a kill takes is up to you.
- **Used in** lists the items that are made from this one. Click one to open it.

## Add to build

An item that sits in a slot or is carried has an **Add to build** button: ships, hull plates, lasers, amps, shields, cells, engines, thrusters, Adaptive Cores, extras, drones, formations, ammo, rockets and the EMP Charge. It puts the item in the build you are editing in **Builds**, in the first place where it fits (a new build called "New build" is made if there is none), and a message says where it went or why it did not fit ("Pick a ship first"). Adding a ship to a build that has one asks you to click again to replace it. The EMP Charge is carried, not fitted: it goes in the build's rockets.

## Builds

A **build** is the loadout of one ship, written as item names so that it means the same on every server: the ship, the lasers with their amps, the shields, engines and Adaptive Cores with their cells and thrusters, the extras, the pieces in the ability slots, the hull plates, the drones with what they carry, a formation, and the ammo and rockets to carry. It also has a name, a note, a stage (Early, Mid or Late) and an archetype.

The list on the left has the **Presets** by stage, **My builds**, **New build** and **Import**; in a narrow window it is a row of tabs. Pick a build and you see its board, its stats and its cost.

### Import

**Import** opens a sheet with three doors:

- **Paste**: paste the text of a build, or press **Paste from clipboard**.
- **From a file**: the build files in the `exports` folder of the game's data folder (`.spacecorps2027` in your home folder), the folder that **Save to file** writes to.
- **From my Hangar**: pick one of your ships and a configuration, and the game reads what is fitted: lasers and amps, generators with their cells and thrusters, extras, ability pieces, hull plates, drones with what they carry and your Extra Slots CPU level. It also offers your hotbar's formation, ammo and rockets; tick the ones you want.

You see what comes in before anything is saved, and the game tells you exactly what it could not import: an item that is not in this game, a piece that does not go in its place, more pieces than the ship has slots, a build made by a newer game. **Imported without changes** means all of it came in. Then **Save to My builds**, **Open in the editor**, or close the sheet. Your [Forge](/wiki/06-Items/Forge.md) tiers, enchant rolls, drone levels, boosters, P.E.T., the look of your ship and the other [Hangar](/wiki/03-Mechanics/Hangar.md) configuration are not part of a build (import the other configuration as a second build).

### The 15 presets

Fifteen builds are ready to use: three stages of the game, **Early**, **Mid** and **Late**, with five kinds in each. **Farming** gets the most kills for what it costs, **Defense** has the biggest shield and the fastest regeneration, **Offense** the most damage and penetration, **Situative** picks its fights with cloaking, jumping and speed, and **Tank** has the most hull and shield together. A preset cannot be changed: **Edit a copy** opens it as your own draft, and **Add to My builds** keeps it as it is. Each row shows its Value in a few characters, worked out from the recipes as you look; open a preset for its stats and its cost.

### Edit

A build is drawn like a Hangar: lasers, generators, extras, abilities, plates and drones, then the Extra Slots CPU level, a formation and the ammo and rockets to carry. Click an empty slot and a list shows only what fits it, with its price or the way to get it; click a piece to **Replace** it, **Add a module** or **Remove** it. A drone carries a laser or a shield core. Change the ship and the pieces that still fit stay, and the rest are listed as kept off. Give the build a name, a stage, an archetype and a note, then **Save**, **Save as copy**, **Delete** or **Close** (Close asks first when changes are not saved).

### Stats

Under the board is the Hangar's own stat card: hitpoints, damage, range, critical chance, shields and their recharge, absorbance, speed, the shield and speed bonuses, penetration and, on a ship with hull plate slots, the hull its plates add. It has no lines for abilities: the pieces in the ability slots are on the board. The server works the numbers out with the same code as your Hangar, for a build that is not fitted on any ship. Two switches set the **Forge tier** and the **Drone level** the numbers assume. A formation works in flight, so it is listed as text and not counted in the numbers, and nor are boosters or your own Forge tiers.

### Cost

The cost has four blocks:

- **Totals**: Credits, Thulium, Dark Matter, every raw item with Need, Have and Missing, the times and the Value. **You still need** is what is left once what you own is taken off.
- **Where the money goes**: every part, the dearest first.
- **Steps**: research, get, buy, press and craft, in order, for the whole build. Click a Get step to see where the world gives it, or open the item in the Recipe Book.
- **Before you start**: what is not a part, such as the Extra Slots CPU levels, the research of hull plate slots, the drones you still have to buy and the Skylab Core level the Forgery needs.

Three switches: **Count what I own** (on), **Include what is fitted** (off) and **Include ammo and rockets** (off: they are used up again and again, so they are not the price of the build).

## Saved on your account

**My builds are saved on your account**, on the server and not on this computer, so they follow you to any computer. You can keep up to 50; the list shows how many you have, and when it is full the page asks you to delete one to save another. A build is saved when the server says so: the page shows **Saving...** while it waits, and if the server refuses or cannot be reached it says why and the build stays unsaved, with your changes still in the editor. A saved build is only item names, a few labels and the name and note you typed, and no other pilot can see it. To give one to a friend, export it.

## Share and export

**Export** on a build opens a sheet with the build as text (JSON). **Copy** it to paste into a chat, or **Save to file**, which writes `spacecorps-build-<name>.json` into the `exports` folder and never overwrites an older file. A friend pastes the text under **Import › Paste**, or puts the file in their own `exports` folder and picks it under **From a file**. The text holds the loadout's item names, the ship and the build's name and note, and nothing of your account.

## Tips

1. **Look before you farm.** Open an item in the Recipe Book and read its Sources and its Steps before you spend a day on a drop that is not the one you need.
2. **Count from nothing.** Switch **Count what I own** off to see what an item or a build costs from scratch; leave it on to see what you still need.
3. **Start from a preset.** **Edit a copy**, swap one part, and the stats and the cost follow.
4. **Read the trees too.** [Item Trees](/wiki/06-Items/Item-Trees.md) shows every kind of item side by side, and the Recipe Book prices any of them for you.
