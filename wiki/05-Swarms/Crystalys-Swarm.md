# Crystalys Swarm

The Crystalys Swarm is a **Boss Crystalys** with its **Crystalys Guards**: the toughest of the aliens, the [Crystalys](/wiki/04-Aliens/Crystalys.md), grown larger, with guards that stay close to it and heal it. It lives in the [Danger Sectors](/wiki/01-General/Danger-Sectors.md) `DS-1`, `DS-2` and `DS-3`, one in each, and it never leaves its sector. The Danger Sectors are PvP sectors, so the fight is for a large group of the strongest pilots, and the boss is not the only danger there.

## At a glance

<!-- crystalys-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Where**: The Danger Sectors `DS-1`, `DS-2`, `DS-3`
- **How many**: One in each of those sectors, 3 in each world
- **Appears**: From season day 4 until the wipe (Beta and Gamma: from season day 1)
- **Leader**: Boss Crystalys
- **Followers**: Up to 3 × Crystalys Guard, a new one every 10 s
- **Followers stay within**: 500 units of the leader
- **Healing**: Each Crystalys Guard within 600 units of the leader heals its hull, 250 HP a second in Alpha
- **Leader destroyed**: The followers leave 30 s after the leader is destroyed, unless they are attacking
- **Comes back**: 30 min after the leader is destroyed, in the same sector
- **Announced**: The pilots of the sector are told when the leader appears and when it is destroyed. These are System lines: they show in the chat's **System** tab, with an unread count, and not in **Global** or **Local**. The kill feed names the pilot credited with the kill.

<!-- crystalys-glance:end -->

## The members

- **Boss Crystalys**: a larger Crystalys, in the swarm's tint and with its name over it, with a hull, a shield and a laser volley of its own (the numbers are below). It is passive: it roams until a pilot hits it, then goes after that pilot and fires at it, and the ships of its swarm that are close join in. Its weapon's range and its speed are those of a Crystalys, and it never mends its hull by itself.
- **Crystalys Guard**: a smaller Crystalys in the swarm's tint. Guards keep close to the boss, join the fight when a swarm ship near them is hit, and each one that is near the boss heals its hull. A guard mends its own hull after a rest, as a Crystalys does.

## How the fight goes

- **Bring a large group.** In Alpha, six level 8 pilots in Paragons with x2 ammo are enough if its fire is spread over them, nine if it is all on one pilot; with x4 ammo it is five and six. More pilots end the fight sooner and lose fewer ships, and a pilot alone is destroyed.
- **Shoot the boss, not the guards.** A guard falls in seconds, but a new one comes as often as the *At a glance* list says, and what the guards heal is a small part of what a group deals: leaving them alone costs a little time, chasing them costs more.
- **Beta and Gamma are harder.** The swarms of those worlds are stronger ([Worlds](/wiki/05-Swarms/Swarms.md#the-worlds)), so they need more pilots or better ammo.
- **The Danger Sectors are PvP.** A rival can attack the group in the middle of the fight and wait for the box: it is the top dealer's (and its clan's) for 30 seconds, and then anyone's ([Cargo](/wiki/03-Mechanics/Cargo.md)). Bring company.
- **The boss comes back** after the time in the *At a glance* list, at full strength, in the same sector, and its guards come one after the other.

## Rewards and drops

The Boss Crystalys pays for the fight it is: a minute of fighting it pays more than a minute of fighting a Crystalys, the best-paid alien. The pay is split by damage among the pilots who fought it ([how a boss kill pays](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Its box is for the pilot who dealt the most damage and holds Cataclysite and Quorvium, now and then a Power Core, an Ancient Control Unit or Dark Matter, x3 and x4 ammo and Epic rockets. The guards pay a small amount and drop nothing; killing them is no way to farm, since they come back with the boss.

## The numbers

The numbers of the swarm's ships in the three worlds ([Worlds](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- crystalys-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Crystalys

Built from the Crystalys at 350% of its hull and 100% of its laser damage; its speed and range are the ship's own.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | 896,000 | 1,344,000 | 1,792,000 |
| Shield | 560,000 | 840,000 | 1,120,000 |
| Laser damage (a volley a second) | 10,000 | 15,000 | 20,000 |
| Speed | 230 | 230 | 230 |
| Laser range | 900 | 900 | 900 |
| Aggro radius | only when attacked | only when attacked | only when attacked |
| Credits | 393,750 | 787,500 | 1,181,250 |
| Thulium | 1,050 | 2,100 | 3,150 |
| Experience (XP) | 63,000 | 126,000 | 189,000 |
| Honor | 273 | 546 | 819 |
| PvE points per kill | 30 | 30 | 30 |

**Drop**: one box, for the pilot who dealt the most damage.

| Item | Chance | Amount |
| :--- | ---: | ---: |
| Cataclysite | 100% on each of 2 rolls | 8 |
| Quorvium | 100% on each of 2 rolls | 6–10 |
| Power Core | 30% | 1 |
| Ancient Control Unit | 15% | 1 |
| Dark Matter | 4% | 1 |
| Ultra Core and Experimental Fusion Core, shared evenly | 100% | 600–1,000 in all |
| One of the 4 Epic [rockets](/wiki/06-Items/Rockets.md), picked at random | 100% | 8–15 |

### Crystalys Guard

Built from the Crystalys at 15% of its hull, shield and damage; its speed and range are the ship's own.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | 38,400 | 57,600 | 76,800 |
| Shield | 24,000 | 36,000 | 48,000 |
| Laser damage (a volley a second) | 1,500 | 2,250 | 3,000 |
| Speed | 230 | 230 | 230 |
| Laser range | 900 | 900 | 900 |
| Aggro radius | only when attacked | only when attacked | only when attacked |
| Heals the leader, each, per second (hull only) | 250 | 375 | 500 |
| Credits | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Experience (XP) | 12 | 24 | 36 |
| Honor | 1 | 2 | 3 |
| PvE points per kill | 6 | 6 | 6 |

**Drop**: none. The kill pays its Credits, Thulium, XP and Honor only.

<!-- crystalys-members:end -->
