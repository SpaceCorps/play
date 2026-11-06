# Dungeons

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; portal; clan portal; join; clan gate alerts; clan dungeon window; start room; fog; guards; locked room; boss room; booster; boosters; swarm assist; focus most wanted; zone of chaos; rocket barrage -->

A **dungeon** is what the game calls a **gate**: a closed maze with a **Warlord** at its end. A co-leader or the leader of a [clan](/wiki/03-Mechanics/Clans.md) opens one and pays for it from the clan bank, and members of the clan fly in together as one [group](/wiki/03-Mechanics/Groups.md). They fight through the aliens of the maze, open loot zones to choose a card from each, and bring the Warlord down. Every pilot who took part in the fight is paid when the Warlord falls, within the limits further down. The gates are on the **Gates** tab of the clan page.

A gate is a fight against the aliens only: nobody can attack a clan mate, or anyone else, inside one. The aliens pay nothing. The pay is the Warlord's alone, so the only way to be paid is to be in the fight when it falls.

## At a glance

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Opens**: From season day 1
- **Who opens a gate**: A co-leader or the leader, who pays the price from the clan bank
- **Party**: 4 to 10 members of the clan, in one group
- **Gates a day**: 3 for each clan in a UTC day, one open at a time
- **Gates at once**: 6 in a world
- **Maps**: Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Mazes**: 8; one is picked when a gate is opened
- **Gathering**: 10 min to gather and start. A gate nobody starts closes, and its price goes back to the clan bank
- **Time limit**: Stage 1: 95 min, Stage 2: 130 min, Stage 3: 165 min from the start. When it runs out the gate fails and pays nothing
- **Left empty**: A gate with nobody inside for 3 min fails
- **After the Warlord falls**: The gate stays open for 2 min, for the pilots inside
- **Coming back**: A pilot who left or was destroyed can fly back in 3 times, 20 s apart

<!-- dungeons-glance:end -->

## How a run goes

1. **Summon.** On the Gates tab a [co-leader or the leader](/wiki/03-Mechanics/Clans.md#hierarchy-roles) picks a stage and presses **Summon**. The price comes out of the [clan bank](/wiki/03-Mechanics/Clans.md#clan-economy-taxation), and the gate takes one of the maps listed above. A gate that nobody starts closes, and the price goes back to the bank.
2. **Enter.** Members of the clan press **Enter** in the Clan window while they are flying, jump through the clan portal, or press **Join** on the call card (see Entering). Everyone lands in the start room, and the pilots inside are the gate's party.
3. **Start.** The start room is a small room at one end of the maze, and its door is shut while the gate gathers. There are no aliens in it, so it is safe to wait there. The gate **starts by itself** when every pilot it is waiting for is inside and the party is big enough. It waits for the members of the clan who are online, not away and in the group of a pilot who has come in, and it starts at once when the party is full. The pilot who opened the gate, or an officer, can press **Start** to begin sooner with the pilots who are inside, if there are enough of them. A pilot who leaves is not waited for any more. When the gate starts, the door opens for good, and after that only the pilots who were already inside can come back.
4. **Fight through the maze.** You come in at one end of the maze and the Warlord waits at the other, in a locked room. The maze is dark: you see only what the party has explored and what is close to its ships. The aliens sleep in packs in the corridors, and a pack that wakes hunts the party through the maze.
5. **Open the loot zones.** Rings in the maze mark the zones. Hold one and the party votes for a card, which is paid out with the Warlord's pay.
6. **Unlock the boss room.** Destroy the guards, the Crystalys and their Twins, and the door of the Warlord's room opens. Until then the Warlord cannot be hurt.
7. **Defeat the Warlord.** Break its shield and hull, and answer its abilities. When it falls the gate is cleared.
8. **Get paid.** The pay comes at the moment the Warlord falls. The gate stays open a little longer for the pilots inside, then closes.

## Entering

To enter a gate you need a **ship in flight**, so launch first and then open the Clan window, and a [group](/wiki/03-Mechanics/Groups.md) with enough members of the clan in it. You also need the **level** that the stage asks for, and you cannot be inside another gate. The gate's party has a size limit: once it is full nobody else can enter.

A co-leader or the leader opens a gate, one at a time for the clan, and only up to the number of gates a day. The clan bank has to hold the price. A clan can open a stage only after it has cleared the stage before it.

Inside a gate you cannot change world, and the Jump CPU and the Base CPU do not work. The **Leave** button in the Clan dungeon window takes you out. It asks you to confirm first, unless the Warlord has already fallen: then you go at once. A pilot who left, or who was destroyed, can fly back in a few times, with a short wait between them.

### The clan portal and the call

When a gate is opened, the clan gets a **portal** for it on the home map of each company (`M-1`, `T-1` and `G-1`), a little way outside the safe zone of the station. Only the pilots of the clan can see it: for everyone else it is not there. It has no safe zone of its own. Fly up to it and jump as at any other portal, and it takes you into the gate under the rules of **Enter**: a ship in flight, a group with enough members of the clan, the level of the stage and room in the party. Once the gate has started, only the pilots who were already inside can use it. The portal is gone when the gate is over.

While the clan's gate is gathering and you are flying somewhere else, a **call** comes to you: a card at the top of the flight screen, with a sound. It says who opened the gate, how many pilots are inside and how long the gate stays open. **Join** flies you in, as **Enter** does on the Gates tab, and when you leave the gate your ship comes back to where it was. Join is greyed out while your group is too small. **Not now** hides the card for that gate. If your group is already inside and the gate is waiting for you, the card says so. The card reaches the pilots of the clan who are flying, not the ones docked at a station, and who have the level that the stage asks. You can turn the card and its sound off with **Clan gate alerts** in Settings › General › Groups.

### The Clan dungeon window

Inside a gate the run has a window of its own, **Clan dungeon**. It shows the time that has gone and what is left, how many aliens fly and how many have been destroyed, what the party should do now (explore the maze, hold a zone, find the boss, destroy the guards, defeat the Warlord), the hull bars of the party, the hold bar while you stand in a zone, the Warlord's ability with its countdown, and the **Leave** button. It is a window like the others: drag it by its title bar and close it with the red light in its corner. It opens by itself when you enter a gate, once for each gate: if you close it, it stays closed until the next gate. The toolbar has a **Clan dungeon** button for it while you are in a gate. While the window is closed, an ability of the Warlord that is about to start or is at work shows as a one-line strip with its name and countdown. Click the strip to open the window again.

## The stages

A gate has a stage, and the stage is its difficulty. A higher stage has tougher aliens that hit harder, and it pays more. The multipliers in the table are the aliens'. Damage means their lasers and rockets. The Warlord does not follow the table: it keeps its own numbers for each stage, further down. The table also says how many aliens a stage sends compared with the first. The **price** is taken from the clan bank when the gate is opened.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Stage | Needs | Hull and shield of the aliens | Number of aliens | Damage of the aliens | Price of the gate (credits, from the clan bank) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Stage 1** | From level 6 | ×1 | ×1 | ×1 | 500,000 |
| **Stage 2** | From level 7 | ×1.5 | ×1 | ×1.5 | 1,000,000 |
| **Stage 3** | From level 8 | ×2 | ×1 | ×2 | 2,000,000 |

<!-- dungeons-stages:end -->

## The maze

Each gate is a closed maze on a map of its own, one of the maps in the list above, and the maze is one of several layouts. The maze fills the whole map, from edge to edge: a grid of rooms and corridors with solid walls. Ships cannot cross a wall, and a wall blocks shots, so a wall is cover. A meteor falls from above, and a wall does not stop it.

**Rooms and doors.** The start room, where you land, and the Warlord's room, at the far end, each have one door. A shut door is a wall to ships, shots and aliens alike. The start door opens when the gate starts. The Warlord's door stays locked until the guards are destroyed (see [the locked room](#the-locked-room)). Between them the maze has a loot room for each loot zone.

**Fog.** The maze is dark. In flight you see its walls and its aliens only where the party has been, and a short way round each ship of the party. A room counts as explored as soon as one of you is in it. The minimap is the same: a chart of the whole floor that fills in as the party explores it, with the entrance, the door of the Warlord's room, the zones you have found and the Warlord once you have found it. The pilots of your own party are always shown.

## The aliens

Four kinds of alien guard the maze. They sleep in packs in the corridors, never in a room, and a pack wakes when a pilot comes near. A pack that is awake does not wait for you: it hunts the party through the maze, and a pack that loses everyone goes back to where it slept and heals. A few packs are awake from the first second, standing in the corridors away from the entrance until a pilot comes near. The gate keeps only so many aliens in the air at once, and that number grows with the size of the party, so a pack that wakes may have to wait for room, and a pack that you destroy lets the next one in. A bigger party meets more aliens in proportion, a smaller party fewer, and a kind of alien never drops below one.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Aliens, for a party of 5 | Stage 1 | Stage 2 | Stage 3 |
| :--- | ---: | ---: | ---: |
| Gate Goombah | 156 | 156 | 156 |
| Gate Pirate | 34 | 34 | 34 |
| Gate Crystalys | 34 | 34 | 34 |
| Gate Crystalys Twin | 11 | 11 | 11 |
| Together | 235 | 235 | 235 |
| The wave of a loot zone | 12 × Gate Goombah and 1 × Gate Crystalys | 12 × Gate Goombah and 1 × Gate Crystalys | 12 × Gate Goombah and 1 × Gate Crystalys |

- **Alive at once**: At most 10 for each pilot of the party, and 70 in all

<!-- dungeons-population:end -->

Each kind in turn. The hull and shield are the usual ones times the multiplier of the stage in the column.

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Gate Goombah

- **Looks like**: Goombah
- **Flies in packs of**: 6

|  | Stage 1 | Stage 2 | Stage 3 |
| :--- | ---: | ---: | ---: |
| Hull | 32,000 | 48,000 | 64,000 |
| Shield | 48,000 | 72,000 | 96,000 |
| Laser damage (a volley a second) | 3,000 | 4,500 | 6,000 |
| Speed | 180 | 180 | 180 |
| Laser range | 800 | 800 | 800 |
| Aggro radius | 1,800 | 1,800 | 1,800 |

### Gate Pirate

- **Looks like**: Pirate Boss
- **Flies in packs of**: 2
- **Rocket**: A straight rocket every 5 s, range 970 units

|  | Stage 1 | Stage 2 | Stage 3 |
| :--- | ---: | ---: | ---: |
| Hull | 300,000 | 450,000 | 600,000 |
| Shield | 50,100 | 75,150 | 100,200 |
| Laser damage (a volley a second) | 200 | 300 | 400 |
| Rocket damage | 5,000 | 7,500 | 10,000 |
| Speed | 92 | 92 | 92 |
| Laser range | 700 | 700 | 700 |
| Aggro radius | 1,800 | 1,800 | 1,800 |

### Gate Crystalys

- **Looks like**: Crystalys
- **Flies in packs of**: 2

|  | Stage 1 | Stage 2 | Stage 3 |
| :--- | ---: | ---: | ---: |
| Hull | 256,000 | 384,000 | 512,000 |
| Shield | 160,000 | 240,000 | 320,000 |
| Laser damage (a volley a second) | 10,000 | 15,000 | 20,000 |
| Speed | 230 | 230 | 230 |
| Laser range | 900 | 900 | 900 |
| Aggro radius | 2,400 | 2,400 | 2,400 |

### Gate Crystalys Twin

- **Looks like**: Crystalys, 1.4 times as big
- **Flies in packs of**: 1

|  | Stage 1 | Stage 2 | Stage 3 |
| :--- | ---: | ---: | ---: |
| Hull | 512,000 | 768,000 | 1,024,000 |
| Shield | 320,000 | 480,000 | 640,000 |
| Laser damage (a volley a second) | 20,000 | 30,000 | 40,000 |
| Speed | 230 | 230 | 230 |
| Laser range | 900 | 900 | 900 |
| Aggro radius | 2,400 | 2,400 | 2,400 |

<!-- dungeons-enemies:end -->

## The Warlord

The Warlord waits in the room at the far end of the maze, and it is the only thing in a gate that pays. It is a Crystalys grown huge. Its hull and shield grow with the size of the party: the more pilots enter, the tougher it is, in proportion. It never leaves its room, whether the door is shut or open: it keeps inside the room's walls and does not hunt through the corridors. A pilot outside can draw it only to the edge of the room, and it still shoots through an open door at whatever its laser reaches. It uses its abilities one at a time, in a random order, each with a cooldown of its own.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Looks like**: Crystalys, 3 times as big
- **Shield recharge**: 3,000 a second, after 15 s without damage

|  | Stage 1 | Stage 2 | Stage 3 |
| :--- | ---: | ---: | ---: |
| Hull | 10,000,000 | 15,000,000 | 25,000,000 |
| Shield | 8,000,000 | 12,000,000 | 20,000,000 |
| Laser damage (a volley a second) | 12,500–15,000 | 15,000–17,500 | 20,000–25,000 |
| Speed | 120 | 120 | 120 |
| Laser range | 1,100 | 1,100 | 1,100 |

The hull and shield above are for a party of 5. They grow with the party: these are the Warlord's hull and shield together, by the number of pilots in the party when the gate starts.

| Pilots in the party | Stage 1 | Stage 2 | Stage 3 |
| :--- | ---: | ---: | ---: |
| 4 | 14,400,000 | 21,600,000 | 36,000,000 |
| 5 | 18,000,000 | 27,000,000 | 45,000,000 |
| 6 | 21,600,000 | 32,400,000 | 54,000,000 |
| 7 | 25,200,000 | 37,800,000 | 63,000,000 |
| 8 | 28,800,000 | 43,200,000 | 72,000,000 |
| 9 | 32,400,000 | 48,600,000 | 81,000,000 |
| 10 | 36,000,000 | 54,000,000 | 90,000,000 |

<!-- dungeons-boss:end -->

### The locked room

The door of the Warlord's room is shut from the moment the gate is opened, and while it is shut the Warlord cannot be hurt: no laser, rocket or blast touches it, and it uses no ability. The door opens, for good, when the party has destroyed the **guards**: the Gate Crystalys and the Gate Crystalys Twin that the gate was made with, about a fifth of its aliens. The Gate Goombah and the Gate Pirate do not count, and neither do the waves of the loot zones or the Goombahs that the Warlord calls.

The Clan dungeon window counts the guards that are left and says, in a chip, that the Warlord cannot be hurt, and a message tells you when the room is unlocked. A pack of guards that still sleeps counts in full, so the party has to explore the maze and find them all. On the minimap the door is a red line while it is locked and a green one when it is open. A gate is never a trap: the time limit still ends a gate whose last guards cannot be found, and an administrator can unlock the room of a stuck gate.

### Its abilities

- **The red ring** of the Lifesteal aura hurts every pilot inside it and heals the Warlord with the damage. The Shield absorption has a red ring too: it drains the shields of the pilots inside and charges the Warlord's. In both, leave the ring, or stand behind a wall.
- **The amber rings** of the Meteor drop show where meteors will land a moment later. Keep moving and get out of the ring before it lands.
- **Focus Most Wanted** marks the pilot who has dealt the most damage to the Warlord, with a gold bracket on his ship, and the Warlord fires an extra bolt at him every second while it lasts. Its aim does not change: it goes on shooting the nearest pilot it can see, so a marked pilot who is also the nearest takes both. The extra bolt needs a clear line and the reach of the Warlord's laser, so a wall or some distance saves him. It does not start while nobody has dealt any damage.
- **The Rocket barrage** sends homing rockets at random pilots, but only at pilots the Warlord can see, and a wall in the way stops a rocket. A ring shows which pilot a rocket follows. An EMP Charge or a cloak shakes them off.
- **The Swarm assist** is the Warlord calling its Goombahs. While they live it cannot be hurt, and it does not fire or use any other ability. Destroy them all: the banner counts how many are left. If a minute goes by, the Warlord can be hurt again and the Goombahs that are left stay and fight on. They are not guards, and they pay nothing.
- **The Zone of Chaos** is a violet ring on the ground, round the place where the Warlord stood when it cast it. Nobody inside the ring can attack, with lasers or rockets, though repairs, cloaks and flying still work, and the Warlord and its aliens fire as ever. The ring shows a moment before it takes hold: step out of it, and shoot into it from outside.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Ability | Warm-up | Lasts | Cooldown | Ring radius (units) | The Warlord regains, at most |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Lifesteal aura** | 2 s | 15 s | 2 min | 900 | 8% of its hull and shield |
| **Meteor drop** | 1.5 s | 3 volleys, 4 s apart | 2 min | 420 | – |
| **Focus Most Wanted** | 1 s | 20 s | 2 min | – | – |
| **Rocket barrage** | 1.5 s | 45 s | 2 min | – | – |
| **Shield absorption** | 2 s | 15 s | 2 min | 900 | 6% of its shield |
| **Swarm assist** | 2 s | Up to 1 min | 3 min | – | – |
| **Zone of Chaos** | 2 s | 15 s | 2 min | 900 | – |

| Ability | Stage 1 | Stage 2 | Stage 3 |
| :--- | :--- | :--- | :--- |
| **Lifesteal aura** | 8,000 a second | 10,000 a second | 12,000 a second |
| **Meteor drop** | 6 meteors a volley, 40,000 each | 8 meteors a volley, 50,000 each | 10 meteors a volley, 60,000 each |
| **Focus Most Wanted** | 18,750–22,500 an extra bolt at the pilot with the most damage dealt, one every 1 s | 22,500–26,250 an extra bolt at the pilot with the most damage dealt, one every 1 s | 30,000–37,500 an extra bolt at the pilot with the most damage dealt, one every 1 s |
| **Rocket barrage** | 6,500 a rocket, one every 15 s | 8,125 a rocket, one every 15 s | 9,750 a rocket, one every 15 s |
| **Shield absorption** | 10,000 shield a second | 12,500 shield a second | 15,000 shield a second |
| **Swarm assist** | 12 Goombahs | 18 Goombahs | 24 Goombahs |
| **Zone of Chaos** | Pilots inside the ring cannot attack | Pilots inside the ring cannot attack | Pilots inside the ring cannot attack |

<!-- dungeons-abilities:end -->

## Loot zones

A ring on the floor of the maze marks each loot zone once the party has found it. Stand inside it for a moment and the zone wakes, and a wave of aliens comes for it. Then the party has to **hold** the zone: keep a pilot inside until the bar fills. The more pilots stand in the ring, the faster the bar fills: a number beside the bar says how many times faster, and the table below gives the times. Enough aliens in the ring stop the bar (the list below says how many), and it runs back while nobody is inside, so clear the wave first. When the zone opens, the party sees three different cards and **votes** for one. A zone opens once, and its wave does not come again.

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Loot zones**: 6 in every maze
- **Radius**: 450 units
- **Waking**: Stand inside the ring for 2 s
- **Holding**: Keep a pilot inside for 30 s. The hold stops while 3 or more aliens are in the ring, and runs back while nobody is
- **Choosing**: The party has 45 s to vote. The vote ends sooner when every pilot present has voted, or one card has more than half of the votes

More pilots in the ring hold a zone faster. How long a zone takes to hold:

| Pilots in the ring | Time to hold the zone |
| :--- | ---: |
| 1 | 30 s |
| 2 | 20 s |
| 3 | 15 s |
| 4 | 12 s |
| 5 or more | 10 s |

<!-- dungeons-zones:end -->

### Boosters

At stages 2 and 3 the waves of the loot zones bring boosters too. When the party has destroyed every alien of a wave, the wave counts, and after every second wave (the second, the fourth and the sixth) each pilot gets a window of half a minute to pick a temporary booster for himself: **Damage** (your lasers hit harder), **HP** (your ship holds more hull) or **Speed** (your ship flies faster). Press a card to pick it. If you do not answer in time, the game picks HP for you. A pick is worth 3% at stage 3 and 1.5% at stage 2, and a kind adds up to 9% at stage 3 and 4.5% at stage 2, however often you pick it. Stage 1 has no boosters. A party that leaves a wave alive gets no window for it.

A booster lasts until the gate is cleared. If you leave the gate, or are destroyed, you lose your boosters, and you get them back when you fly in again. A chip under the Clan dungeon window lists what you have.

### The cards

The cards are drawn one by one from the pool below. The chance is that of a card in one draw. Every card goes to every pilot who is paid, gear cards too: a card with many copies gives each of them that many, and a gear card gives each of them a piece of his own, forged for him. A pilot who is not paid gets no card either, and a zone that was opened in a gate that fails pays nothing.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Card | Stage 1 | Stage 2 | Stage 3 | Chance | Goes to |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2,000 | 3,000 | 5,000 | 23.9% | Every paid pilot |
| Velkonite Reinforced Plate | 10 | 15 | 25 | 13.65% | Every paid pilot |
| Velkonite | 200 | 300 | 500 | 13.65% | Every paid pilot |
| Orvium | 200 | 300 | 500 | 13.65% | Every paid pilot |
| Ultra Core | 5,000 | 7,500 | 12,500 | 11.4% | Every paid pilot |
| Experimental Fusion Core | 3,000 | 4,500 | 7,500 | 9.1% | Every paid pilot |
| Dark Matter | 5 | 8 | 12 | 9.1% | Every paid pilot |
| Dark Matter Plate | 1 | 1 | 2 | 4.55% | Every paid pilot |
| Starfire-III | – | – | 1 | 0.07% | Every paid pilot |
| Helios Beam | – | – | 1 | 0.07% | Every paid pilot |
| Engine III | – | – | 1 | 0.07% | Every paid pilot |
| Adaptive Core III | – | – | 1 | 0.07% | Every paid pilot |
| Heavy Shield Core | – | – | 1 | 0.07% | Every paid pilot |
| Momentum Thruster IV | – | – | 1 | 0.07% | Every paid pilot |
| Impulse Thruster IV | – | – | 1 | 0.07% | Every paid pilot |
| Hull Plating II | – | – | 1 | 0.07% | Every paid pilot |
| Hull Plating III | – | – | 1 | 0.07% | Every paid pilot |
| Damage Amp IV | – | – | 1 | 0.07% | Every paid pilot |
| Crit Amp IV | – | – | 1 | 0.07% | Every paid pilot |
| Penetration Amp IV | – | – | 1 | 0.07% | Every paid pilot |
| Capacity Shield Cell IV | – | – | 1 | 0.08% | Every paid pilot |
| Absorption Shield Cell IV | – | – | 1 | 0.08% | Every paid pilot |

- **Gear**: The cards with one copy are gear: together 1% of the cards

<!-- dungeons-cards:end -->

The cards with one copy are **gear**, and only a stage 3 gate can offer them. A piece of gear is forged for every paid pilot as it is paid out: each of them rolls an [enchant tier](/wiki/06-Items/Overview.md#item-enchants) of his own with the same chances as a piece you build in the Assembly, so most come as Standard, and a higher tier, up to Eternal, with buffs, is a rare find.

## Pay

When the Warlord falls, every pilot who earned it is paid, once for the clear. The cards that the party chose come on top of the pay of the stage. There is no world multiplier: the pay is the same in every world.

The **Orvium Reinforced Plates** are not a card of the vote. They are part of the pay of the stage, and each paid pilot gets them once for the clear. The items that a gate pays are not Marketable: you cannot [sell them at the Auction](/wiki/03-Mechanics/Auction.md#marketable-items).

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Stage | Honor | Experience | Credits | Thulium | x4 ammo | Orvium Reinforced Plates | PvE ranking points |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Stage 1** | 25,000 | 600,000 | 5,000,000 | 4,000 | 4,000 | 5 | 600 |
| **Stage 2** | 50,000 | 1,500,000 | 10,000,000 | 9,000 | 9,000 | 10 | 1,500 |
| **Stage 3** | 100,000 | 2,400,000 | 17,500,000 | 15,000 | 15,000 | 15 | 2,400 |

<!-- dungeons-pay:end -->

### Who is paid

The aliens never pay. A clear is played in full even when it pays nothing, and the result screen says why. Entering is never refused because you were paid for a stage already: that clear just pays nothing.

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **A day**: A stage pays a pilot once in a UTC day: the day the Warlord falls
- **A week**: A pilot is paid for at most 10 stage clears in a UTC week, Monday to Sunday
- **Inside**: At least 2 min in all
- **A share in the fight**: At least one of these: dealt 2% of the Warlord's hull and shield; destroyed 10 of the gate's aliens; healed other pilots for 50,000 during the fight with the Warlord

<!-- dungeons-rules:end -->

### What a day and a week are worth

What a pilot can be paid in one day, and in the best week that the limits allow. The last column is what the pay adds to your [PvE ranking points](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points).

<!-- dungeons-totals:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Pay for each pilot | Honor | Experience | Credits | Thulium | x4 ammo | Orvium Reinforced Plates | PvE ranking points |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| One day, every stage once | 175,000 | 4,500,000 | 32,500,000 | 28,000 | 28,000 | 30 | 4,500 |
| The best week: 7 × Stage 3 and 3 × Stage 2 | 850,000 | 21,300,000 | 152,500,000 | 132,000 | 132,000 | 135 | 21,300 |

The experience of a paid clear counts for your PvE ranking points: one point for every 1,000 experience.

<!-- dungeons-totals:end -->

## The clan bank's reward {#clan-bank-reward}

The clan bank is paid too, in credits and not in Thulium, the first time the clan clears a stage in a season. The clan has to be old enough, and enough pilots of that clear have to be paid. The bank is paid once for each stage in a season.

<!-- dungeons-clan:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Stage | Credits for the clan bank |
| :--- | ---: |
| **Stage 1** | 10,000,000 |
| **Stage 2** | 20,000,000 |
| **Stage 3** | 30,000,000 |

- **Clan age**: At least 3 d
- **Paid pilots**: At least 3 in the gate

<!-- dungeons-clan:end -->

## Tips

- Clear a zone's wave before you try to hold the zone, and fight inside the ring if the aliens come in.
- Bring the whole party to a zone: the more pilots in the ring, the faster it is held.
- Explore every corner of the maze: a pack of guards that you never find keeps the Warlord's door shut.
- Use the walls: lasers do not cross them, the red rings of the Warlord's auras stop at them, and a wall stops the Warlord's rockets too.
- Keep an EMP Charge for the Rocket barrage.
- When the Warlord calls its Goombahs, destroy them first: it cannot be hurt until they are gone. In the Zone of Chaos, step out of the ring before you shoot.
- Watch the clock in the Clan dungeon window. When the time runs out the gate fails and pays nothing.
