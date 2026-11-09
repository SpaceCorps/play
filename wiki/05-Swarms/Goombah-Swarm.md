# Goombah Swarm

The Goombah Swarm is a **Boss Goombah** with its **Goombah Guards**: a huge [Goombah](/wiki/04-Aliens/Goombah.md) that never starts a fight, and smaller ones that stay close to it and heal it. It lives on the same sectors as the [Phantasm Swarm](/wiki/05-Swarms/Phantasm-Swarm.md), `x-3` and `x-4`, and it is a fight for a group of the strongest pilots of the companies' sectors.

## At a glance

<!-- goombah-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Where**: The sectors `x-3` and `x-4` of every company
- **How many**: One in each of those sectors, 6 in each world
- **Appears**: From season day 4 until the wipe (Beta and Gamma: from season day 1)
- **Leader**: Boss Goombah
- **Followers**: Up to 4 × Goombah Guard, a new one every 10 s
- **Followers stay within**: 500 units of the leader
- **Healing**: Each Goombah Guard within 600 units of the leader heals its hull, 110 HP a second in Alpha
- **Leader destroyed**: The followers leave 30 s after the leader is destroyed, unless they are attacking
- **Comes back**: 5 min after the leader is destroyed, in the same sector
- **Announced**: The pilots of the sector are told when the leader appears and when it is destroyed. These are System lines: they show in the chat's **System** tab, with an unread count, and not in **Global** or **Local**. The kill feed names the pilot credited with the kill.

<!-- goombah-glance:end -->

## The members

- **Boss Goombah**: a larger Goombah, in the swarm's tint and with its name over it, with a hull, a shield and a laser volley of its own (the numbers are below). It is passive: it roams until a pilot hits it, then goes after that pilot and fires at it, and the ships of its swarm that are close join in. Its weapon's range and its speed are those of a Goombah, and it never mends its hull by itself.
- **Goombah Guard**: a smaller Goombah in the swarm's tint. Guards keep close to the boss, join the fight when a swarm ship near them is hit, and each one that is near the boss heals its hull. A guard mends its own hull after a rest, as a Goombah does.

## How the fight goes

- **Bring a group of the strongest ships.** Three level 8 pilots with x2 ammo destroy it in about a minute and a quarter in Alpha, losing at most one ship; two of them need x4 ammo, and pilots of lower levels do not deal enough damage to win.
- **Shoot the boss, not the guards.** A guard falls in seconds, but a new one comes as often as the *At a glance* list says, and what the guards heal is a small part of what a group deals: leaving them alone costs a little time, chasing them costs more.
- **Beta and Gamma are harder.** The swarms of those worlds are stronger ([Worlds](/wiki/05-Swarms/Swarms.md#the-worlds)), so they need more pilots or better ammo.
- **Watch the sector.** `x-4` is a PvP sector in Alpha, and `x-3` and `x-4` are in Beta and Gamma ([Worlds](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): a rival can join the fight or wait for the box. Keep a ship of the group on watch.
- **The boss comes back** after the time in the *At a glance* list, at full strength, in the same sector, and its guards come one after the other.

## Rewards and drops

The Boss Goombah pays for the fight it is: a minute of fighting it pays more than a minute of fighting a Goombah, the best-paid alien of these sectors. The pay is split by damage among the pilots who fought it ([how a boss kill pays](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Its box is for the pilot who dealt the most damage and holds a Goombah's own drops several times over (Cataclysite, Quorvium, Power Cores, Reinforced Hull Plates and Ship Fragments), with ammo and rockets. The guards pay a small amount and drop nothing; killing them is no way to farm, since they come back with the boss.

## The numbers

The numbers of the swarm's ships in the three worlds ([Worlds](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- goombah-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Goombah

Built from the Goombah at 400% of its hull and 100% of its laser damage; its speed and range are the ship's own.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | 128,000 | 192,000 | 256,000 |
| Shield | 192,000 | 288,000 | 384,000 |
| Laser damage (a volley a second) | 3,000 | 4,500 | 6,000 |
| Speed | 180 | 180 | 180 |
| Laser range | 800 | 800 | 800 |
| Aggro radius | only when attacked | only when attacked | only when attacked |
| Credits | 120,000 | 240,000 | 360,000 |
| Thulium | 600 | 1,200 | 1,800 |
| Experience (XP) | 24,000 | 48,000 | 72,000 |
| Honor | 192 | 384 | 576 |
| PvE points per kill | 14 | 14 | 14 |

**Drop**: one box, for the pilot who dealt the most damage.

| Item | Chance | Amount |
| :--- | ---: | ---: |
| Ship Fragment | 100% on each of 8 rolls | 3 |
| Reinforced Hull Plate | 60% on each of 8 rolls | 1 |
| Power Core | 25% on each of 8 rolls | 1 |
| Cataclysite | 100% on each of 8 rolls | 4 |
| Quorvium | 100% on each of 8 rolls | 2–4 |
| Advanced Plasma | 100% | 100–200 |
| Ultra Core | 100% | 100–200 |
| One of the 4 [rockets](/wiki/06-Items/Rockets.md) bought with Credits, picked at random | 100% | 6–10 |

### Goombah Guard

Built from the Goombah at 20% of its hull, shield and damage; its speed and range are the ship's own.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | 6,400 | 9,600 | 12,800 |
| Shield | 9,600 | 14,400 | 19,200 |
| Laser damage (a volley a second) | 600 | 900 | 1,200 |
| Speed | 180 | 180 | 180 |
| Laser range | 800 | 800 | 800 |
| Aggro radius | only when attacked | only when attacked | only when attacked |
| Heals the leader, each, per second (hull only) | 110 | 165 | 220 |
| Credits | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Experience (XP) | 12 | 24 | 36 |
| Honor | 1 | 2 | 3 |
| PvE points per kill | 3 | 3 | 3 |

**Drop**: none. The kill pays its Credits, Thulium, XP and Honor only.

<!-- goombah-members:end -->
