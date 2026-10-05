# Seeker Swarm

The Seeker Swarm is the smallest of the [swarms](/wiki/05-Swarms/Swarms.md): a **Boss Seeker** and the **Seeker Slaves** that guard it and heal it. It lives in the sectors where new pilots start to fly, so it is the first swarm most pilots meet. The Boss Seeker never starts a fight, but once you shoot it, it is far more dangerous than the [Seeker](/wiki/04-Aliens/Seeker.md) it is built from.

## At a glance

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Where**: The sectors `x-1` and `x-2` of every company
- **How many**: One in each of those sectors, 6 in each world
- **Appears**: From season day 4 until the wipe
- **Leader**: Boss Seeker
- **Followers**: Up to 4 × Seeker Slave, a new one every 10 s
- **Followers stay within**: 500 units of the leader
- **Healing**: Each Seeker Slave within 600 units of the leader heals its hull, 50 HP a second in Alpha
- **Leader destroyed**: The followers leave 30 s after the leader is destroyed, unless they are attacking
- **Comes back**: 2 min after the leader is destroyed, in the same sector
- **Announced**: The pilots of the sector are told when the leader appears and when it is destroyed. These are System lines: they show in the chat's **System** tab, with an unread count, and not in **Global** or **Local**. The kill feed names the pilot credited with the kill.

<!-- seeker-glance:end -->

## The members

- **Boss Seeker**: a much larger Seeker, in the swarm's tint and with its name over it, with many times a Seeker's hull, shield and damage (the numbers are below). It is passive: it roams until a pilot hits it, then stops where it is and fires at that pilot, and the ships of its swarm that are close join in. Its weapon's range and its speed are a Seeker's, and it never mends its hull by itself.
- **Seeker Slave**: a plain Seeker in the swarm's tint. Slaves keep close to the boss, join the fight when a swarm ship near them is hit, and each one that is near the boss heals its hull. A slave mends its own hull after a rest, as a Seeker does.

## How the fight goes

- **Leave it alone until your ship can take it.** A Boss Seeker hits harder than any pilot's first ship can bear: a new pilot's Protos, with no shield yet, is destroyed in seconds once the boss and its slaves are on it.
- **Stay out of reach.** The boss and its slaves are slower than a Protos, and their weapons reach less far than a Quantum Laser 2's (see [Lasers & Ammo](/wiki/06-Items/Lasers.md)): a pilot who has such lasers and keeps beyond their range takes no damage while it fires. A pilot with Quantum Laser 1 cannot stay out of reach.
- **The slaves heal faster than a lone new pilot hits.** Together they mend more than one pilot's lasers deal with x1 ammo, so bring a partner and x2 ammo. Two pilots with Quantum Laser 2 who keep their distance take the boss down in about a minute in Alpha, and much faster with x2 ammo.
- **The boss comes back** after the time in the *At a glance* list, at full strength, in the same sector, and its slaves come one after the other.

## Rewards and drops

The Boss Seeker pays **exactly ten Seekers**: ten times a Seeker's Credits, Thulium, XP and Honor, split by damage among the pilots who fought it ([how a boss kill pays](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Its box holds ten Seekers' loot and, on top of it, ammo and rockets below Epic, for the pilot who dealt the most damage. The slaves pay a small amount and drop nothing; killing them is no way to farm, since they come back with the boss.

## The numbers

The numbers of the swarm's ships in the three worlds ([Worlds](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker

Built from the Seeker at 400% of its hull, shield and damage; its speed and range are the ship's own.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | 3,200 | 4,800 | 6,400 |
| Shield | 3,200 | 4,800 | 6,400 |
| Laser damage (a volley a second) | 720 | 1,080 | 1,440 |
| Speed | 120 | 120 | 120 |
| Laser range | 600 | 600 | 600 |
| Aggro radius | only when attacked | only when attacked | only when attacked |
| Credits | 10,000 | 20,000 | 30,000 |
| Thulium | 40 | 80 | 120 |
| Experience (XP) | 1,000 | 2,000 | 3,000 |
| Honor | 20 | 40 | 60 |
| PvE points per kill | 5 | 5 | 5 |

**Drop**: one box, for the pilot who dealt the most damage.

| Item | Chance | Amount |
| :--- | ---: | ---: |
| Ship Fragment | 20% on each of 10 rolls | 1 |
| Daraxium | 50% on each of 10 rolls | 1–2 |
| Standard Battery | 100% | 200–400 |
| Advanced Plasma | 100% | 10–20 |
| Ultra Core | 100% | 2–4 |
| One of the 8 [rockets](/wiki/06-Items/Rockets.md) bought with Credits, picked at random | 100% | 2–3 |

### Seeker Slave

Built from the Seeker at 100% of its hull, shield and damage; its speed and range are the ship's own.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | 800 | 1,200 | 1,600 |
| Shield | 800 | 1,200 | 1,600 |
| Laser damage (a volley a second) | 180 | 270 | 360 |
| Speed | 120 | 120 | 120 |
| Laser range | 600 | 600 | 600 |
| Aggro radius | only when attacked | only when attacked | only when attacked |
| Heals the leader, each, per second (hull only) | 50 | 75 | 100 |
| Credits | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Experience (XP) | 12 | 24 | 36 |
| Honor | 1 | 2 | 3 |
| PvE points per kill | 1 | 1 | 1 |

**Drop**: none. The kill pays its Credits, Thulium, XP and Honor only.

<!-- seeker-members:end -->
