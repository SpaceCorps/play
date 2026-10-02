# Drone Mechanics

Drones are autonomous support units that fly alongside your ship. They provide additional equipment slots and contribute directly to your ship's combat performance. A Slave Drone also grows: it earns experience every time you destroy an alien and rises through **eight levels**, from a small armoured sphere to a crescent-winged gunship. In the Assembly a Slave Drone can be upgraded into a **Master Drone**, which starts its levels again (see Master Drone below).

## Getting Drones

Every drone you hold, a **Slave Drone** or a Master Drone, opens its drone slots (one for a Slave Drone, two for a Master Drone), up to **8** drones. The Shop sells Slave Drones for Credits, and from the fourth on for Thulium too. Each one costs more than the last: the prices are in [Drones](/wiki/05-Items/Drones.md).

## Formation & Movement

Drones fly in a standard **"Wingman" Formation (2-2-4)**:

- **2 Drones** beside the ship, one on each flank.
- **2 Drones** beside and just behind it.
- **4 Drones** trailing behind.

They utilize a smooth following algorithm that adjusts their position based on your ship's speed and rotation, tightening the formation during sharp maneuvers. Nobody flies ahead of you.

Drones are small, and they stay close: a level-8 drone is about 19.5 units across (a Protos is 50) and a level-1 drone is a ball of about 8, so the whole formation fits within roughly 135 units of your ship. The drone you bought first has the most experience and flies on your left flank, the second on your right, and the newest trail behind.

## Equipment & Stats

Drones function as extending equipment racks for your ship.

- A Slave Drone has **1 slot** and a Master Drone **2**, up to **8 drones**.
- You can equip **Lasers** and **Shields** into these slots, in either slot of a Master Drone. Nothing else fits: no engines, no Adaptive Cores.
- **Lasers count fully.** A laser on a drone fires when you fire, adds its damage to your volley and uses ammo like any other laser (each laser burns one unit of ammo a volley). The two lasers of a Master Drone are two lasers.
- **Shields do not add capacity yet.** A shield on a drone does not add to your shield total, in either slot. It is not harmless, though: a drone's shield still takes a place in the order your shields are counted in (the biggest first, the fifth and later count for less), so it can push a real shield of yours down a rank and lower your total a little. Keep shields in the ship's own slots.

## Levels

Every Slave Drone starts at level 1 and gains experience (XP) whenever you destroy an alien. A Master Drone starts at level 1 too, with no XP, and levels the same way. Each level asks for more than the one before, and the look changes with it, so you can see how far a drone has come. The table gives, for each level, the XP it takes to climb there from the level before and how many kills of one kind of alien that is on its own (in the Alpha world: Beta needs about half as many, Gamma about a third):

<!-- drones:begin -->
<!-- Generated from server/Resources/drone-levels.json by scripts/drones-wiki.sh: don't edit by hand. -->

- **Level 1, Seed:** a small armoured sphere with one cyan lens.
- **Level 2, Halo:** the sphere in a floating ring.
- **Level 3, Disc:** a flat disc under a glass dome.
- **Level 4, Saucer:** a saucer with armour plates and intakes.
- **Level 5, Gunship:** a prow and two cannons join the saucer.
- **Level 6, Wingbuds:** cannons and short wing blades on pylons.
- **Level 7, Halfwings:** longer wing blades with gold tips.
- **Level 8, Crescent:** the finished gunship: full crescent wings with cyan light strips.

| Level | XP to reach | XP for the level | Laser damage | Seeker kills | Bulwark kills | Gorvane kills |
| --: | --: | --: | --: | --: | --: | --: |
| 1 | 0 | – | – | – | – | – |
| 2 | 350 | 350 | – | 350 | 44 | 15 |
| 3 | 900 | 550 | +1% | 550 | 69 | 23 |
| 4 | 2,000 | 1,100 | +2% | 1,100 | 138 | 46 |
| 5 | 3,700 | 1,700 | +3% | 1,700 | 213 | 71 |
| 6 | 6,000 | 2,300 | +4% | 2,300 | 288 | 96 |
| 7 | 9,500 | 3,500 | +5% | 3,500 | 438 | 146 |
| 8 | 14,000 | 4,500 | +7% | 4,500 | 563 | 188 |

| Alien | XP for each drone |
| :--- | --: |
| Seeker | 1 |
| Phantasm | 2 |
| Bulwark | 8 |
| Gorvane | 24 |
| Crystalys | 72 |

<!-- drones:end -->

### How drones earn XP

- **Every drone you own earns the same XP** for each alien kill you are paid for: the first 8 drones, whether or not they carry a laser. A drone you buy later starts at level 1 with no XP, so your first drones are always the highest level.
- **Tougher aliens are worth more.** The XP an alien gives is in the second table above (the Crystalys is worth 72 Seekers). Any other alien gives 1.
- **Worlds pay more.** Beta doubles the XP, Gamma triples it (the aliens there also have more health). Boosters and Premium do not change it.
- **Kills count when they pay you.** An alien you finish while another pilot holds its claim pays nothing to your drones, just as it pays nothing to you. Player kills, quests and company pilots' own kills give no drone XP.
- **Level 8 is the last level.** XP keeps counting after it.

### What a level gives

The **laser fitted in a drone's slot** deals more base damage as its drone levels up: nothing at levels 1 and 2, then +1% at level 3 up to **+7% at level 8**. The bonus multiplies that laser's own damage (after its enchant); the amps fitted into it are added on top and are not multiplied. The Hangar shows each drone's level, its XP bar and the kills the next level asks for, and its damage figures already include the bonus. When a drone levels up, the Game Log says so ("Drone 2 reached level 4.") and the drone pops with a ring of light.

### How long it takes

The curve is set so that a new drone reaches level 2 in about an hour of normal play (hunting Bulwarks and Gorvanes), and level 8 in roughly 27 hours of play. Those hours are for a pilot who buys the first drone at about the level-7 quests; with weaker gear it takes longer (up to about 4 hours for level 2 and 150 hours for level 8). Hunting one kind of alien on its own is at best about half as fast again as a normal mix. Drones stay through the season wipe with their levels and experience, so those hours are spent once, over as many seasons as it takes: a pilot who plays half an hour a day gets there in a couple of seasons.

### Master Drone

A Slave Drone becomes a **Master Drone** when you upgrade it in the Assembly. The recipe costs 40,000 Thulium and 100 Ship Fragments and takes 60 seconds, and it does not use up a drone: **you pick which Slave Drone it is** (the picker shows the level and XP of each), and that same drone, with its number, its drone slot and everything fitted in it, turns into a Master Drone when the job finishes, with a second slot that is empty. Nothing goes into your inventory and there is nothing to collect: the Game Log tells you when it is done, also for an upgrade that finished while you were away.

**Its level and XP are reset to 0 when the upgrade finishes.** A Master Drone starts again at level 1, with no XP, and levels the way a Slave Drone does (the table above); the laser bonus of the level it had goes with it. The Assembly says so before you start, and asks you to confirm, naming the drone, when it has any XP. The default choice is the drone with the least XP.

While the upgrade runs the drone is locked: you cannot upgrade it again or delete it, and its slot is **offline**, so the laser in it does not fire until the job finishes (it is still a Slave Drone with one slot until then). It is queued behind your other jobs, like any craft.

A Master Drone is one of your 8 drones: it counts for the drone limit and for the price of the next Slave Drone, so upgrading changes neither, and it stays through the season wipe with its level and XP. In flight it is the finished gunship in gold. A Master Drone has **two equipment slots** where a Slave Drone has one: each takes a laser or a shield, and the level bonus applies to the laser in either. Otherwise it is a Slave Drone: the same eight levels and the same laser bonus. Master Drones you made before it had the second slot have it now, with what they carried where it was. Master Drones crafted before upgrades in place existed are ordinary items in your inventory and do not fly.

## Combat Behavior

- **Lasers**: Drones will fire their equipped lasers at your locked target.
- **Damage**: Drones can take damage (if distinct entity logic exists, currently they share ship pool mostly but visually distinct). _Note: Currently, Drones are indestructible extensions of the ship._
