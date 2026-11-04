# Dungeons

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys -->

A **dungeon** is what the game calls a **gate**: a closed maze with a **Warlord** at its end. A co-leader or the leader of a [clan](/wiki/03-Mechanics/Clans.md) opens one and pays for it from the clan bank, and members of the clan fly in together as one [group](/wiki/03-Mechanics/Groups.md). They fight through the aliens of the maze, open loot zones to choose a card from each, and bring the Warlord down. Every pilot who took part in the fight is paid when the Warlord falls, within the limits further down. The gates are on the **Gates** tab of the clan page.

A gate is a fight against the aliens only: nobody can attack a clan mate, or anyone else, inside one. The aliens pay nothing. The pay is the Warlord's alone, so the only way to be paid is to be in the fight when it falls.

## At a glance

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Opens**: From season day 4
- **Who opens a gate**: A co-leader or the leader, who pays the price from the clan bank
- **Party**: 4 to 10 members of the clan, in one group
- **Gates a day**: 3 for each clan in a UTC day, one open at a time
- **Gates at once**: 6 in a world
- **Maps**: Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Mazes**: 8; one is picked when a gate is opened
- **Gathering**: 10 min to gather and start. A gate nobody starts closes, and its price goes back to the clan bank
- **Time limit**: Stage 1: 80 min, Stage 2: 110 min, Stage 3: 150 min from the start. When it runs out the gate fails and pays nothing
- **Left empty**: A gate with nobody inside for 3 min fails
- **After the Warlord falls**: The gate stays open for 2 min, for the pilots inside
- **Coming back**: A pilot who left or was destroyed can fly back in 3 times, 20 s apart

<!-- dungeons-glance:end -->

## How a run goes

1. **Summon.** On the Gates tab a [co-leader or the leader](/wiki/03-Mechanics/Clans.md#hierarchy-roles) picks a stage and presses **Summon**. The price comes out of the [clan bank](/wiki/03-Mechanics/Clans.md#clan-economy-taxation), and the gate takes one of the maps listed above. A gate that nobody starts closes, and the price goes back to the bank.
2. **Enter.** Members of the clan press **Enter** in the Clan window while they are flying. The pilots inside are the gate's party.
3. **Start.** The pilot who opened the gate, or an officer, presses **Start** once enough pilots are inside. After that only the pilots who were already inside can come back.
4. **Fight through the maze.** You come in at one end of the maze and the Warlord waits at the other. The aliens sleep in their rooms and wake in packs as the party comes near.
5. **Open the loot zones.** Rings in the maze mark the zones. Hold one and the party votes for a card, which is paid out with the Warlord's pay.
6. **Defeat the Warlord.** Break its shield and hull, and answer its abilities. When it falls the gate is cleared.
7. **Get paid.** The pay comes at the moment the Warlord falls. The gate stays open a little longer for the pilots inside, then closes.

## Entering

To enter a gate you need a **ship in flight**, so launch first and then open the Clan window, and a [group](/wiki/03-Mechanics/Groups.md) with enough members of the clan in it. You also need the **level** that the stage asks for, and you cannot be inside another gate. The gate's party has a size limit: once it is full nobody else can enter.

A co-leader or the leader opens a gate, one at a time for the clan, and only up to the number of gates a day. The clan bank has to hold the price. A clan can open a stage only after it has cleared the stage before it.

Inside a gate you cannot change world, and the Jump CPU and the Base CPU do not work. The **Leave** button on the gate's bar takes you out after you confirm. A pilot who left, or who was destroyed, can fly back in a few times, with a short wait between them.

## The stages

A gate has a stage, and the stage is its difficulty. A higher stage has tougher aliens that hit harder, and it pays more. The multipliers in the table apply to every alien and to the Warlord. Damage means lasers, rockets and the Warlord's abilities. The table also says how many aliens a stage sends compared with the first. The **price** is taken from the clan bank when the gate is opened.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Stage | Needs | Hull and shield of the aliens | Number of aliens | Damage of the aliens | Price of the gate (credits, from the clan bank) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Stage 1** | From level 6 | ×1 | ×1 | ×1 | 500,000 |
| **Stage 2** | From level 7 | ×1.5 | ×1 | ×1.25 | 1,000,000 |
| **Stage 3** | From level 8 | ×2.5 | ×1 | ×1.5 | 2,000,000 |

<!-- dungeons-stages:end -->

## The maze

Each gate is a closed maze on a map of its own, one of the maps in the list above, and the maze is one of several layouts. A maze is a grid of rooms and corridors with solid walls. Ships cannot cross a wall, and a wall blocks shots, so a wall is cover. A meteor falls from above, and a wall does not stop it.

## The aliens

Four kinds of alien guard the maze. They sleep in their rooms and wake when a pilot comes near. The gate keeps only so many aliens in the air at once, and that number grows with the size of the party, so a pack that you destroy lets the next one in. A bigger party meets more aliens in proportion, a smaller party fewer, and a kind of alien never drops below one.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Aliens, for a party of 5 | Stage 1 | Stage 2 | Stage 3 |
| :--- | ---: | ---: | ---: |
| Gate Goombah | 130 | 130 | 130 |
| Gate Pirate | 28 | 28 | 28 |
| Gate Crystalys | 28 | 28 | 28 |
| Gate Crystalys Twin | 9 | 9 | 9 |
| Together | 195 | 195 | 195 |
| The wave of a loot zone | 10 × Gate Goombah and 1 × Gate Crystalys | 10 × Gate Goombah and 1 × Gate Crystalys | 10 × Gate Goombah and 1 × Gate Crystalys |

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
| Hull | 32,000 | 48,000 | 80,000 |
| Shield | 48,000 | 72,000 | 120,000 |
| Laser damage (a volley a second) | 3,000 | 3,750 | 4,500 |
| Speed | 180 | 180 | 180 |
| Laser range | 800 | 800 | 800 |
| Aggro radius | 1,800 | 1,800 | 1,800 |

### Gate Pirate

- **Looks like**: Pirate Boss
- **Flies in packs of**: 2
- **Rocket**: A straight rocket every 5 s, range 970 units

|  | Stage 1 | Stage 2 | Stage 3 |
| :--- | ---: | ---: | ---: |
| Hull | 300,000 | 450,000 | 750,000 |
| Shield | 50,100 | 75,150 | 125,250 |
| Laser damage (a volley a second) | 200 | 250 | 300 |
| Rocket damage | 5,000 | 6,250 | 7,500 |
| Speed | 92 | 92 | 92 |
| Laser range | 700 | 700 | 700 |
| Aggro radius | 1,800 | 1,800 | 1,800 |

### Gate Crystalys

- **Looks like**: Crystalys
- **Flies in packs of**: 2

|  | Stage 1 | Stage 2 | Stage 3 |
| :--- | ---: | ---: | ---: |
| Hull | 256,000 | 384,000 | 640,000 |
| Shield | 160,000 | 240,000 | 400,000 |
| Laser damage (a volley a second) | 10,000 | 12,500 | 15,000 |
| Speed | 230 | 230 | 230 |
| Laser range | 900 | 900 | 900 |
| Aggro radius | 2,400 | 2,400 | 2,400 |

### Gate Crystalys Twin

- **Looks like**: Crystalys, 1.4 times as big
- **Flies in packs of**: 1

|  | Stage 1 | Stage 2 | Stage 3 |
| :--- | ---: | ---: | ---: |
| Hull | 512,000 | 768,000 | 1,280,000 |
| Shield | 320,000 | 480,000 | 800,000 |
| Laser damage (a volley a second) | 20,000 | 25,000 | 30,000 |
| Speed | 230 | 230 | 230 |
| Laser range | 900 | 900 | 900 |
| Aggro radius | 2,400 | 2,400 | 2,400 |

<!-- dungeons-enemies:end -->

## The Warlord

The Warlord waits in the room at the far end of the maze, and it is the only thing in a gate that pays. It is a Crystalys grown huge. Its hull and shield grow with the size of the party: the more pilots enter, the tougher it is, in proportion. It stays in its room and uses its abilities one at a time, in a random order, each with a cooldown of its own.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Looks like**: Crystalys, 3 times as big
- **Shield recharge**: 3,000 a second, after 15 s without damage

|  | Stage 1 | Stage 2 | Stage 3 |
| :--- | ---: | ---: | ---: |
| Hull | 10,000,000 | 15,000,000 | 25,000,000 |
| Shield | 8,000,000 | 12,000,000 | 20,000,000 |
| Laser damage (a volley a second) | 8,000 | 10,000 | 12,000 |
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

### Its abilities

- **The red ring** of the Lifesteal aura hurts every pilot inside it and heals the Warlord with the damage. The Shield absorption has a red ring too: it drains the shields of the pilots inside and charges the Warlord's. In both, leave the ring, or stand behind a wall.
- **The amber rings** of the Meteor drop show where meteors will land a moment later. Keep moving and get out of the ring before it lands.
- **Focus on healers** turns the Warlord on whoever heals another pilot, and it hits that pilot harder. Spread the healing.
- **The Rocket barrage** sends homing rockets at random pilots. An EMP Charge or a cloak shakes them off.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Ability | Warm-up | Lasts | Cooldown | Ring radius (units) | The Warlord regains, at most |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Lifesteal aura** | 2 s | 15 s | 2 min | 900 | 8% of its hull and shield |
| **Meteor drop** | 1.5 s | 3 volleys, 4 s apart | 2 min | 420 | – |
| **Focus on healers** | 1 s | 45 s | 2 min | – | – |
| **Rocket barrage** | 1.5 s | 45 s | 2 min | – | – |
| **Shield absorption** | 2 s | 15 s | 2 min | 900 | 6% of its shield |

| Ability | Stage 1 | Stage 2 | Stage 3 |
| :--- | :--- | :--- | :--- |
| **Lifesteal aura** | 8,000 a second | 10,000 a second | 12,000 a second |
| **Meteor drop** | 6 meteors a volley, 40,000 each | 8 meteors a volley, 50,000 each | 10 meteors a volley, 60,000 each |
| **Focus on healers** | Its laser hits ×1.5 as hard on the pilot it turns on | Its laser hits ×1.5 as hard on the pilot it turns on | Its laser hits ×1.5 as hard on the pilot it turns on |
| **Rocket barrage** | 6,500 a rocket, one every 15 s | 8,125 a rocket, one every 15 s | 9,750 a rocket, one every 15 s |
| **Shield absorption** | 10,000 shield a second | 12,500 shield a second | 15,000 shield a second |

<!-- dungeons-abilities:end -->

## Loot zones

A ring on the floor of the maze marks each loot zone once the party has found it. Stand inside it for a moment and the zone wakes, and a wave of aliens comes for it. Then the party has to **hold** the zone: keep a pilot inside until the bar fills. Aliens in the ring stop the bar, and it runs back while nobody is inside, so clear the wave first. When the zone opens, the party sees three different cards and **votes** for one. A zone opens once, and its wave does not come again.

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Loot zones**: 4 in every maze
- **Radius**: 450 units
- **Waking**: Stand inside the ring for 2 s
- **Holding**: Keep a pilot inside for 30 s. The hold stops while 3 or more aliens are in the ring, and runs back while nobody is
- **Choosing**: The party has 45 s to vote. The vote ends sooner when every pilot present has voted, or one card has more than half of the votes

<!-- dungeons-zones:end -->

### The cards

The cards are drawn one by one from the pool below. The chance is that of a card in one draw. A card with many copies goes to every pilot who is paid, and a gear card, with one copy, goes to one pilot of the party. A pilot who is not paid gets no card either, and a zone that was opened in a gate that fails pays nothing.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Card | Stage 1 | Stage 2 | Stage 3 | Chance | Goes to |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2,000 | 3,000 | 5,000 | 21% | Every paid pilot |
| Velkonite Reinforced Plate | 10 | 15 | 25 | 12% | Every paid pilot |
| Orvium Reinforced Plate | 10 | 15 | 25 | 12% | Every paid pilot |
| Velkonite | 200 | 300 | 500 | 12% | Every paid pilot |
| Orvium | 200 | 300 | 500 | 12% | Every paid pilot |
| Ultra Core | 5,000 | 7,500 | 12,500 | 10% | Every paid pilot |
| Experimental Fusion Core | 3,000 | 4,500 | 7,500 | 8% | Every paid pilot |
| Dark Matter | 5 | 8 | 12 | 8% | Every paid pilot |
| Dark Matter Plate | 1 | 1 | 2 | 4% | Every paid pilot |
| Engine III | 1 | 1 | 1 | 0.25% | One pilot of the party |
| Heavy Shield Core | 1 | 1 | 1 | 0.25% | One pilot of the party |
| Adaptive Core III | 1 | 1 | 1 | 0.25% | One pilot of the party |
| Starfire-III | 1 | 1 | 1 | 0.25% | One pilot of the party |

- **Gear**: The cards with one copy are gear: together 1% of the cards

<!-- dungeons-cards:end -->

## Pay

When the Warlord falls, every pilot who earned it is paid, once for the clear. The cards that the party chose come on top of the pay of the stage. There is no world multiplier: the pay is the same in every world.

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Stage | Honor | Experience | Credits | Thulium | x4 ammo | PvE ranking points |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| **Stage 1** | 25,000 | 600,000 | 5,000,000 | 4,000 | 4,000 | 600 |
| **Stage 2** | 50,000 | 1,500,000 | 10,000,000 | 9,000 | 9,000 | 1,500 |
| **Stage 3** | 100,000 | 2,400,000 | 17,500,000 | 15,000 | 15,000 | 2,400 |

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

| Pay for each pilot | Honor | Experience | Credits | Thulium | x4 ammo | PvE ranking points |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| One day, every stage once | 175,000 | 4,500,000 | 32,500,000 | 28,000 | 28,000 | 4,500 |
| The best week: 7 × Stage 3 and 3 × Stage 2 | 850,000 | 21,300,000 | 152,500,000 | 132,000 | 132,000 | 21,300 |

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
- Use the walls: lasers do not cross them, and the Warlord's rings stop at them.
- Keep an EMP Charge for the Rocket barrage.
- Watch the clock on the gate's bar. When the time runs out the gate fails and pays nothing.
