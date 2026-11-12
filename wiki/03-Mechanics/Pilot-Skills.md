# Pilot Skills

<!-- wiki-search: skills; skill tree; pilot skill tree; pilot skills; skill xp; xp; level up; stats; attributes; heft; grit; reflex; instinct; laser tech; rocket tech; antimatter; marksmanship; sabotage; evasion; tactics; radiation tech; thruster theory; science; extraction; logistics; fabrication; commerce; soft cap; hold; training; day one; pilot button; pilot page; buffs -->

Your pilot has a **skill tree**: a set of stats that level up by what you do. Fight, and your Laser tech and Grit rise; collect from your Skylab, and your Extraction rises. Each level gives a small permanent buff to something you already do, and nothing is spent or chosen: there are no points to place and nothing to respec. You level what you use.

The tree belongs to **you**, not to a ship. Every ship you fly has your levels, a ship you buy tomorrow too, and the levels are kept through every wipe ([what is kept](#what-is-kept)).

A new pilot is not at full strength. At level 1 a laser and a rocket do less than the item pages list, and Laser tech and Rocket tech lift them past the listed numbers as they level. Every figure on the item pages is the item's own, before your skills.

## At a glance

<!-- skills-glance:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

- **Stats**: 19 stats: 4 attributes and 15 skills in 5 groups
- **Levels**: 1 to 100. Every pilot starts every stat at level 1, and there is nothing to spend and nothing to respec
- **Cost of a level**: 40 XP from level 1 to 2, 875 XP from level 50 to 51, 19,157 XP from level 99 to 100; 313,258 XP in all
- **What a level gives**: A buff grows in a straight line from its value at level 1 to its value at level 100. Nothing is capped
- **Your laser at level 1**: It deals 100% of its damage and hits 80% of the time, so 80% of the damage the item pages list
- **Your rocket at level 1**: It deals 100% of its damage and is a dud 10% of the time, so 90% of the damage the item pages list
- **Dodging**: Every pilot's ship dodges 3% of the hits that can be dodged, before any skill or formation adds to it
- **Hull tier**: The rarity of your ship sets it, as the table below shows. The size of your hold and the XP of Heft follow it
- **Hold**: It counts the resource units you pick up after you launch, up to the size its hull tier gives it. It is full from 90% of that, and a full hold makes Heft pay ×1.5. Nothing is ever refused
- **Hourly soft cap**: Most stats pay full XP only up to a cap an hour, counted in the stat's own unit over the UTC clock hour. Above it an event pays 25% of its XP
- **Training**: The XP of a skill also pays 10% of itself to its attribute. An attribute at level 100 trains its skills 25% faster than at level 1

| Hull tier | Rarity of the ship | Size of the hold |
| :--- | :--- | ---: |
| 1 | Shoddy / Common | 60 |
| 2 | Uncommon | 120 |
| 3 | Rare | 250 |
| 4 | Epic | 500 |
| 5 | Mythical / Legendary / Eternal | 1,000 |

<!-- skills-glance:end -->

## The stats

The stats are of two kinds. The **attributes** (Heft, Grit, Reflex and Instinct) are the basics of a pilot. The **skills** are in five groups, and each skill is governed by one attribute, which the tables name in brackets: the XP of a skill also feeds its attribute, and a high attribute trains its skills faster ([how XP is paid](#how-xp-is-paid)). The names are the ones of the Pilot Skills page of the game.

The tables give every buff at level 1 and at the last level; between them a buff grows in a straight line. A **factor** multiplies a number: one above 1 makes it bigger, one below 1 smaller. Most buffs change a number of your ship, and the tooltip of a number that a skill moved has a line that says how much of it comes from your skills.

<!-- skills-buffs:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

### Attributes

| Stat | What it changes | Level 1 | Level 100 |
| :--- | :--- | ---: | ---: |
| **Heft** | Hull | +0% | +20% |
| **Grit** | Damage you take | ×1 | ×0.92 |
| **Reflex** | Speed at which abilities cool down | ×1 | ×1.1 |
| **Instinct** | Chance of every loot line | +0 points | +7.5 points |
|  | Orvium and Velkonite from the collectors | ×1 | ×1.5 |

### Weapons

| Stat | What it changes | Level 1 | Level 100 |
| :--- | :--- | ---: | ---: |
| **Laser tech** (Reflex) | Laser damage | ×1 | ×1.3 |
|  | Chance a laser volley hits | 80% | 89% |
| **Rocket tech** (Reflex) | Rocket damage | ×1 | ×1.3 |
|  | Chance a rocket is a dud | 10% | 1% |
| **Antimatter** (Instinct) | Dark Matter from pick-ups | ×1 | ×1.25 |

### Combat

| Stat | What it changes | Level 1 | Level 100 |
| :--- | :--- | ---: | ---: |
| **Marksmanship** (Reflex) | How far a Mine is thrown | ×1 | ×1.15 |
|  | Speed of a thrown Mine | ×1 | ×1.15 |
| **Sabotage** (Reflex) | Damage of poisons and Mines | ×1 | ×1.3 |
|  | Duration of poisons | ×1 | ×1.2 |
| **Evasion** (Reflex) | Chance to dodge a hit, added to the ship's own | 0% | 15% |
| **Tactics** (Reflex) | Duration of abilities | ×1 | ×1.2 |
| **Shield absorption** (Grit) | Absorbance of your shields | +0 points | +5 points |

### Ship control

| Stat | What it changes | Level 1 | Level 100 |
| :--- | :--- | ---: | ---: |
| **Radiation tech** (Grit) | Dose of radiation | ×1 | ×0.4 |
| **Thruster theory** (Heft) | Speed | +0% | +10% |
| **Science** (Instinct) | Science from each unit of fuel | ×1 | ×1.25 |

### Skylab

| Stat | What it changes | Level 1 | Level 100 |
| :--- | :--- | ---: | ---: |
| **Extraction** (Instinct) | What the Skylab makes | ×1 | ×1.3 |
| **Logistics** (Heft) | What the Resource Storage's bank holds | ×1 | ×1.4 |
| **Fabrication** (Reflex) | Time of a craft | ×1 | ×0.65 |

### Trading

| Stat | What it changes | Level 1 | Level 100 |
| :--- | :--- | ---: | ---: |
| **Commerce** (Instinct) | Prices in the Shop | ×1 | ×0.85 |
|  | What the Shop pays when it buys back | ×1 | ×1.1 |
|  | Deposit of an Auction listing | ×1 | ×0.5 |


<!-- skills-buffs:end -->

## Where you feel it

- **Lasers.** Laser tech changes the damage of every volley and the chance that it hits; a volley that goes wide shows a floating "Miss" and still uses its ammo ([Combat](/wiki/03-Mechanics/Combat.md#laser-tech)). The range of your lasers is the ship's own: Marksmanship levels from your hits with ammo other than plain x1, but it only works on Mines (below).
- **Rockets.** Rocket tech changes the damage of every rocket and the chance that one is a dud ([Rocket tech](/wiki/06-Items/Rockets.md#rocket-tech)).
- **Taking hits.** Grit takes a share off every hit you take, Evasion adds to the chance that a direct hit does nothing, and Shield absorption adds to the share of a hit that your shields take ([Combat](/wiki/03-Mechanics/Combat.md#grit-and-evasion)). Heft adds to your hull.
- **Abilities.** Reflex shortens the cooldown of your abilities and Tactics makes them last longer ([Abilities](/wiki/03-Mechanics/Abilities.md#pilot-skills)). Sabotage strengthens the poisons.
- **Mines.** Sabotage adds to the damage of a Mine, and Marksmanship throws it faster and farther ([Extras](/wiki/06-Items/Extras.md#mine)).
- **Speed.** Thruster theory adds to your speed, on top of the engines and an Afterburner ([Speed](/wiki/03-Mechanics/Speed.md)).
- **Pick-ups.** Instinct raises the chance of every loot line, as a Loot Luck Booster does, and the two add up; Antimatter raises the Dark Matter you pick up ([Cargo](/wiki/03-Mechanics/Cargo.md), [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md)).
- **Radiation.** Radiation tech lowers the dose of the black hole, the excavators' circles, the pulsars and the Unwakened's aura ([Black Hole](/wiki/03-Mechanics/Black-Hole.md)).
- **Home.** Extraction and Logistics change what the [Skylab](/wiki/03-Mechanics/Skylab.md) makes and holds, Instinct adds to its two collectors, Fabrication shortens the crafts of the Assembly, Science fills the [Research](/wiki/03-Mechanics/Research.md) Centre faster, and Commerce lowers the prices of the Shop, raises what it pays when it buys back, and lowers the deposit of an [Auction](/wiki/03-Mechanics/Auction.md) listing.

## How XP is paid

The server pays XP for what you do, wherever you fly, in this order:

1. **The anti-farm rule.** A hit from or to a company mate or a groupmate pays nothing, and neither does anything done to or by a ship in a safe zone or under the shelter of a respawn. The seconds of Heft, of Grit's low hull and of Thruster theory count only while your ship is alive, outside a shelter, and you have given an order in the last minute: a ship parked in the open earns nothing.
2. **The hourly soft cap.** A stat with a cap pays full XP up to it and a share of it above it, counted in the stat's own unit (the shots you fire, the commands you give, the XP it earned) over the UTC clock hour. A new login does not reopen the window, and the numbers are in the list above and in the table below.
3. **Training speed.** The attribute that governs a skill raises the XP the skill earns, more with every level of the attribute (the cap is counted before this, so the cap limits the activity and not the speed).
4. **The attribute's share.** The skill gets the XP, and its attribute gets a share of it, which is never capped or sped up.

The table lists what pays XP, stat by stat. The XP is for each unit of what is named in the second column.

<!-- skills-xp:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

| Stat | What pays XP | XP | Hourly soft cap |
| :--- | :--- | ---: | ---: |
| **Heft** | Each 10 s of flying with an order given in the last 1 min: the ship's hull tier, plus 0.2 for each fitted plate, ×1.5 with a full hold | 1 | None |
| **Grit** | Each 1% of your maximum hull lost to an enemy or a hazard | 1 | 300 XP an hour |
|  | Each 10 s below 25% of your maximum hull | 5 |  |
| **Reflex** | Each command the game takes: an ability, an extra, a new target, a pick-up, a craft, a formation swap, a rocket or a jump. A new target pays at most once in 4 s, a pick-up at most once in 1 s and a rocket at most once in 1 s | 1 | 600 commands an hour |
| **Instinct** | Each cargo box you pick up, by hand or with a Retriever | 2 | 600 XP an hour |
|  | Each item of a quest reward you claim | 10 |  |
|  | The first time you pick up an item of Rare quality or better (once for each item, ever) | 25 |  |
| **Laser tech** (Reflex) | Each volley you fire | 0.1 | 1,800 shots an hour |
|  | Each volley that lands on a ship | 0.1 |  |
| **Rocket tech** (Reflex) | Each rocket you launch | 0.15 | 130 rockets an hour |
|  | Each rocket that hits a ship (once for each rocket, however many ships its blast hurts) | 0.3 |  |
| **Antimatter** (Instinct) | Each Dark Matter you receive at a pick-up | 2.2 | None |
| **Marksmanship** (Reflex) | Each hit of a volley fired with ammo other than plain x1 (×1.5 for the first 10 min of each kind of ammo in a clock hour) | 0.1 | 3,000 hits an hour |
|  | Each hit of a Mine, and each second an enemy spends in your Energetic Wall | 0.1 |  |
| **Sabotage** (Reflex) | Each hit of a Mine, and each second an enemy spends in your Energetic Wall | 0.5 | 1,200 XP an hour |
|  | Each second a poison of yours runs on an enemy | 0.05 |  |
| **Evasion** (Reflex) | Each hostile attack on you that misses or is dodged | 1 | 600 XP an hour |
| **Tactics** (Reflex) | Each ability you press with a hostile in laser range | 2 | 600 XP an hour |
| **Shield absorption** (Grit) | Each 1% of your maximum shield that enemy hits take | 0.1 | 300 XP an hour |
| **Radiation tech** (Grit) | Each second inside a radiation band | 0.2 | None |
|  | Each 1% of your maximum hull the radiation takes | 1 |  |
| **Thruster theory** (Heft) | Each second flown above 80% of your ship's speed, twice as much under an Afterburner | 0.1 | None |
| **Science** (Instinct) | Each unit of science the Research Centre burns | 0.1 | None |
|  | Each technology you finish | 50 |  |
| **Extraction** (Instinct) | Each resource unit your Skylab makes, paid when you collect | 0.1 | None |
| **Logistics** (Heft) | Each resource unit you deposit into the Skylab bank | 0.05 | None |
| **Fabrication** (Reflex) | Each second of craft time you complete, paid when you collect | 0.1 | None |
| **Commerce** (Instinct) | Each trade in the Auction or the Shop, counted as the common logarithm of 1 plus its worth in credits (a Thulium is worth what the Auction values it at) | 2 | 600 XP an hour |

<!-- skills-xp:end -->

While you fly, the flight screen shows the XP you earn in short lines, gathered every few seconds, and a banner tells you when a stat levels up and what changed (the Game Log keeps a line for it). A stat that earns its first XP is announced once. The tooltips of the numbers that skills moved say so too, in a Pilot line of their own, and the Damage tile of the Hangar leaves the skills out and says so: they apply when you fire.

## Levelling up

A level costs more XP than the one before it, by a fixed share, so the first levels come quickly and the last ones take long. Every stat has the same curve. The buff you have at a level is the same for every pilot: only the speed at which you reach it depends on what you do.

<!-- skills-curve:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

| Level | XP for the level | XP in all from level 1 | Share of every buff |
| :--- | ---: | ---: | ---: |
| 2 | 40 | 40 | 1.01% |
| 10 | 66 | 468 | 9.09% |
| 25 | 170 | 2,174 | 24.24% |
| 50 | 822 | 12,851 | 49.49% |
| 75 | 3,968 | 64,397 | 74.75% |
| 100 | 19,157 | 313,258 | 100% |

<!-- skills-curve:end -->

## The Pilot Skills page

The **Pilot Skills** page is a page of the station, with a row of its own in the sidebar. It is one compact sheet of the whole tree: the attributes and the five groups of skills stand side by side in columns (three on a wide screen, fewer on a narrow one), a line for each stat with its level at the right edge and a thin XP bar under it. A stat that has earned no XP yet is grey, with a dash for its level. Rest the pointer on a line to see what the stat does, which attribute governs it or which skills it trains, its XP and what makes it grow. Click a line to open its details under its row of columns: the same words, the XP bar, and a slider to preview any level from 1 to the last, with a small table of what the stat changes at level 1, at your level now, at the level you preview and at the last level. One stat is open at a time; click the line again, use the close button or press Esc to put it away. The row in the sidebar carries a badge when a stat has levelled since you last opened the page, and a card in the Boosters window sums up what your skills change.

In flight the same sheet is the **Pilot Skills** window. Open it with the Pilot Skills button of the toolbar (on a wide screen) or with its key, K by default (Settings, Controls). It is a window like the others: move it, resize it, and it remembers its place and whether it was open. It only shows your skills: the levels move as the XP lines of the flight arrive, and a click on a line opens the same details inside the window.

## What is kept

- **Through every wipe.** The tree is a part of your account: a wipe changes no level and no XP, and the Transport Cache has nothing to do with it ([What you keep](/wiki/03-Mechanics/Wipe-Timeline.md#what-you-keep)).
- **On the regional servers.** The XP you earn flying on Singapore or US East is added to your skills when you come home, a stat you used for the first time there included, and the hourly cap you used up there goes with you. The Pilot Skills page of a pilot who is flying there reads the regional server's numbers, with the XP the ship has earned since its last save.
- **Until the account is deleted.** Deleting an account deletes its levels.

The buffs have no ceiling but the last level: a pilot who has levelled everything is as strong as the tables say.
