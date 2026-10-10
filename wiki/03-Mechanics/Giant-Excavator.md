# Giant Excavator

<!-- wiki-search: excavator; giant excavator; pulsar; mining; fuel; excavator fuel; control panel; overheat; radiation; slumbering void; voids; wave; ds-1; ds-2; ds-3 -->

A **pulsar** shines in each of the Danger Sectors `DS-1`, `DS-2` and `DS-3` from the first day of the season, and from season day 11 a **giant excavator** stands beside it. The excavator mines the pulsar for **Thulium and rare ores**, and it burns [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md) to do it. Anyone may fuel it, choose what it mines and start it, and everything it lays lies around it in boxes that anyone may take. A run is loud, though: the whole world is told when it starts, **Slumbering Voids** come for it in waves, and an excavator that is worked too long overheats and irradiates the whole area. This page says how a run goes, what it lays and how to live through it. The sectors are in [Danger Sectors](/wiki/01-General/Danger-Sectors.md); the Voids are in [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).

![The giant excavator's sheet: the fuel tank, the heat, the resource to mine, the excavator's hull and the Voids of the next wave](../img/wiki-img/shots/excavator-sheet.jpg)

## At a glance

<!-- excavator-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Where**: One pulsar with one giant excavator on each of `DS-1`, `DS-2` and `DS-3`, in every world
- **Appears**: The pulsar from the first day of the season, the excavator from season day 11 until the wipe
- **Fuel**: Dark Matter. One burns for 10 min; the tank holds 3, which is 30 min of mining. Anyone may add one at a time, from their own cargo
- **Panel**: The sheet works within 600 units of the excavator, and its label shows from 1,400 units. Anyone may fuel, choose and start; the choice is locked while it runs
- **Boxes**: A box every 20 s, 450 to 900 units from the excavator, free for anyone from the moment it lies. It lies for 5 min, and at most 24 lie on a map at once
- **Heat**: 30 min of mining, in as many runs as it takes, and the excavator overheats for 1 h. The heat is kept between runs and is gone after the rest
- **Radiation**: While it is overheated or destroyed, the excavator (within 1,100 units) and its pulsar (within 1,300 units) burn every ship inside: 10% of its total HP every second
- **Hull**: 200,000 HP in Alpha, 300,000 in Beta and 400,000 in Gamma. Only Slumbering Voids can hurt it, and only when no pilot is left to defend it
- **Voids**: 2 Slumbering Voids every 2 min while it mines, the first 1 min after the start; at most 8 alive on a map
- **Announced**: The pilots of the whole world are told when a run starts, when the excavator overheats and when it is destroyed; the rest goes to the pilots of its sector. These are System lines: they show in the chat's **System** tab and in the Game Log, and not in **Global** or **Local**.

<!-- excavator-glance:end -->

## How a run goes

1. **Find one.** From season day 11 each of the three Danger Sectors that has a pulsar has one excavator, in each world. A label, **Excavator**, hangs over it when you are near, and the Star System map marks every Danger Sector that has one: the mark's colour is the state of its excavator, and its tooltip tells the time to its next change.
2. **Open the panel.** Click the label. The **Giant excavator** sheet works while your ship is within the panel's range of the excavator (the *At a glance* list gives it). A cloaked ship can use it, and using it does not end the cloak.
3. **Fuel it.** **Add Dark Matter** puts one Dark Matter from your cargo into the tank. Anyone can. The tank never takes more than the excavator can still burn before it overheats, so no fuel is wasted.
4. **Choose what to mine** from the list, then press **Start mining**. It needs at least one Dark Matter in the tank and a resource. Anyone can change the choice until the start; once it runs the resource is locked. The start is told to every pilot of the world, naming you, the sector and the resource.
5. **Hold it.** While it mines a box lies down around the excavator every few seconds, and the first Slumbering Voids arrive soon after the start. Defend the excavator, and take the boxes.
6. **Watch the heat.** The Heat bar fills while the excavator mines and never empties while it waits. At its limit the excavator overheats. Leave before: the game warns the map twice.
7. **It rests.** Overheated or destroyed, the excavator and its pulsar are irradiated until the rest is over; then it is ready again, with its heat back to nothing and its hull full.

The sheet also shows the sector, the tank (one cell for each Dark Matter, the one that burns drawn partly), how much Dark Matter you carry, the excavator's hull, what each resource lays a minute in your world, and, while it mines, the time to the next wave and the Voids alive. When something is refused you read the reason in red: you are too far from the panel, you have no Dark Matter, the tank is full, there is no fuel yet or no resource chosen, the resource is locked while it runs, or the excavator is hot.

| State | What it is | What you can do |
| :--- | :--- | :--- |
| **Ready** | No fuel, or fuel and not started. The heat so far is kept. | Add Dark Matter, choose, start. |
| **Mining** | It burns Dark Matter and gathers heat; the resource is locked. | Add more Dark Matter up to the room left, fight the Voids, take the boxes. |
| **Overheated** | The heat reached its limit. The tank is emptied; the boxes already laid stay. | Nothing. The area is irradiated: stay out. |
| **Destroyed** | Voids brought the hull to zero. The fuel is lost, the hull is full again at once. | Nothing. The area is irradiated: stay out. |

If the fuel runs out before the limit, the excavator goes back to **Ready** with its heat kept, and the Voids that are left leave after a while unless they are fighting.

## What it mines

A full tank lays about what five pilots would make in half an hour of the best Thulium farming. Beta and Gamma lay more, as they pay more for every kill. You choose one resource per run. A box is the same for everyone, and a Thulium box is cash that pays when it is picked up, as the asteroids' Thulium is.

<!-- excavator-resources:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

A full tank (3 Dark Matter, 30 min of mining) lays the amounts below, in 90 boxes.

| Resource | Alpha | Beta | Gamma | A minute, in Alpha | A box, in Alpha |
| :--- | ---: | ---: | ---: | ---: | ---: |
| [Thulium](/wiki/06-Items/Resources.md#thulium) | 9,643 | 15,429 | 19,286 | 321.4 | 107.1 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | 2,314 | 3,703 | 4,629 | 77.1 | 25.7 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | 1,029 | 1,646 | 2,057 | 34.3 | 11.4 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | 640 | 640 | 640 | 21.3 | 7.1 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | 320 | 320 | 320 | 10.7 | 3.6 |

- A run of Velkonite or Orvium lays at most 8 hours of a level 20 [Skylab](/wiki/03-Mechanics/Skylab.md) collector of that ore (640 Velkonite, 320 Orvium), in every world: they are the Skylab's ores, and a run never speeds its pacing by more than that.
- A box holds about the amount of the last column, 15% more or less. A Thulium box is cash: the pickup pays it. An ore box holds the item.

<!-- excavator-resources:end -->

The pilot's own boosters work as for any cargo: the Resource Magnet Booster's bonus lifts a box of ore. There is no daily limit on the boxes: the fuel and the clock are what limit a run.

**What the ore is for.** The ore of a box goes into your cargo like any item. Cataclysite and Quorvium are used in Assembly and the Forge ([Resources](/wiki/06-Items/Resources.md)). The Forgery and the Research Centre of the Skylab take Velkonite and Orvium from the Resource Storage only, which the collectors fill, so the ore of a box is of no use in your cargo: park your ship and the [Ore Bay](/wiki/03-Mechanics/Skylab.md#ore-bay) of your Skylab (Core level 10) moves it into the storage, up to its allowance an hour, from where the Forgery and the [Research Centre](/wiki/03-Mechanics/Research.md#fuel) take it.

## The Slumbering Voids

A run draws **Slumbering Voids**, hunters of the lost civilisation that fly in from the edge of the map to protect the pulsar from anyone who would empty it. They hunt the pilots near the excavator, and when there is nobody left to hunt, they go for the excavator. The Void's numbers and its pay are in [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).

<!-- excavator-voids:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Waves.** 2 Slumbering Voids every 2 min; the first 1 min after the start, and none in the last 1 min of a run. At most 8 are alive on a map at once: a wave that finds the map full is skipped.
- **Coming in.** A wave appears at the edge of the map, 900 units inside it and at least 2,500 units from every gate ring, and flies to the excavator in about 20 s. The message names the side of the map it comes from.
- **Hunting.** A Void hunts the nearest pilot it can see within 2,500 units, and stays within 7,000 units of the excavator.
- **Siege.** When no pilot it can see is within 7,000 units of the excavator for 15 s, the Voids attack the excavator, and each laser does 25% of its usual damage. At zero the excavator is destroyed: its fuel is lost, its hull is full again at once, and it rests for 1 h.
- **Leaving.** When a run ends, the Voids that are left stay 90 s more and fight on if they are fought; then they go.

<!-- excavator-voids:end -->

- **A Void is a glass cannon.** Its shield is large but takes 80% of a hit, so the hull behind it is gone after a few times its size in damage, and much sooner with shield penetration. Two or three well-equipped pilots hold a run in Alpha; Beta and Gamma need larger groups, as for every alien.
- **A cloak is no defence of the site.** The Voids do not see cloaked ships, so a pilot who hides does not keep them from the excavator; and a pilot who shelters in a gate ring cannot be reached and does not count either.
- **Every Void pays,** by the damage you did to it, and drops a box ([how a boss kill pays](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Their kills add to your PvE ranking points like a swarm ship's.

## Heat and radiation

Mining adds heat second by second. The heat is **cumulative and never cools while the excavator waits**: a run that stops early leaves the next pilot a shorter run. When it reaches the limit the excavator **overheats**, and when its hull is brought to zero it is **destroyed**; either way the excavator and its pulsar radiate until the rest is over.

<!-- excavator-radiation:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

| Circle | Radius | Total HP a second | A full ship lasts |
| :--- | ---: | ---: | ---: |
| The giant excavator | 1,100 | 10% | 10 s |
| The pulsar | 1,300 | 10% | 10 s |

- **The dose.** 10% of a ship's total maximum HP (hull plus shield) every second, so a full ship lasts 10 s, whatever its class. The shield takes it first and its absorbance does not count.
- **Who.** Every ship inside the circles, cloaked ones included; no alien. It is damage taken: a Repair Drone stops and the shield does not recharge, as at the black hole.
- **Credit.** A pilot who burns to death is credited to the last enemy who hit them in the 15 s before.
- **Warnings.** The map is told 1 min and 15 s before the overheat.

<!-- excavator-radiation:end -->

- **The warning.** Twice before the overheat (the times are in the list above) the map is told, a ship inside the circles sees a warning, and the circles are drawn on the ground in flight and on the minimap. When they radiate the circles are red and the Radiation gauge shows the dose.
- **Leaving.** Every stock ship can leave from the panel's edge or from the farthest box alive, except the Ironclad, which is slow: it leaves during the warning, or it does not leave. Do not stand on a box when the heat runs out.
- **Loot in the circles.** Boxes laid before the overheat stay, in the radiation: a box lying there when it begins is taken at the cost of the dose.
- **The server restarting** pauses a run: the fuel and the heat come back as they were, the rest runs on the clock, and the first wave after the restart comes a minute later.

## Fighting over a run

The excavator has **no special ring**: the normal rules of your world apply, so rivals may come, shoot you and take the boxes (a box is free for anyone from the moment it lies). Stealing and ambushing are part of the event. A few things to plan for:

- **Who fuels is not who wins.** Anyone may fuel, choose and start; a rival can change the resource before you press Start. Check the choice before you press it.
- **The fuel is at risk.** If the excavator is destroyed the Dark Matter in its tank is lost, and nobody gets it back. The most that can be lost is the full tank.
- **Bring a group** and agree who stays near the excavator and who takes the boxes, and keep an eye on the heat: the pilots who take the last boxes are the ones the radiation catches.
- **The Voids come to the excavator, not to the boxes.** A group that holds the excavator keeps the Voids busy; one that wanders off leaves it to the siege.

## What the world is told

These are System lines (they show in the chat's **System** tab and in the Game Log, and not in **Global** or **Local**). The first three go to the whole world; the last goes to the pilots of the excavator's sector.

- The day event 2 begins: the Danger Sectors have changed.
- A pilot **starts** an excavator, naming the sector, the resource and the minutes of fuel.
- The excavator **overheats**, or is **destroyed**.
- The fuel runs out; the excavator is about to overheat (twice); a **wave** of Voids is coming, with its number and the side of the map it comes from; no pilot is left, so the Voids attack the excavator.

Each action of the panel and each warning has a quiet sound of its own, on the effects volume.

## Where to read more

- [Danger Sectors](/wiki/01-General/Danger-Sectors.md): where the pulsars stand and what else is new.
- [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md): the Slumbering Void, the Inert Mass and the Unwakened.
- [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md) and [The Black Hole](/wiki/03-Mechanics/Black-Hole.md): where the fuel comes from.
- [Resources](/wiki/06-Items/Resources.md): the ores the excavator lays.
- [Cargo](/wiki/03-Mechanics/Cargo.md): boxes, pickup and the Resource Magnet Booster.
- [Ranks](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points): the PvE points of a Void.
