# Seeker Swarm

The Seeker Swarm is the smallest of the [swarms](/wiki/05-Swarms/Swarms.md): a **Boss Seeker** and the **Seeker Slaves** that guard it and heal it. It lives in the sectors where new pilots start to fly, so it is the first swarm most pilots meet. The Boss Seeker never starts a fight, but once you shoot it, it is far more dangerous than the [Seeker](/wiki/04-Aliens/Seeker.md) it is built from.

## At a glance

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Where**: The sectors `x-1` and `x-2` of every company
- **How many**: One in each of those sectors, 6 in each world
- **Appears**: From season day 4 until the wipe (Beta and Gamma: from season day 1)
- **Leader**: Boss Seeker
- **Followers**: Up to 4 × Seeker Slave, a new one every 10 s
- **Followers stay within**: 500 units of the leader
- **Healing**: Each Seeker Slave within 600 units of the leader heals its hull, 50 HP a second in Alpha
- **Leader destroyed**: The followers leave 30 s after the leader is destroyed, unless they are attacking
- **Comes back**: {{guide:vitals.respawn@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} after the leader is destroyed, in the same sector
- **Announced**: The pilots of the sector are told when the leader appears and when it is destroyed. These are System lines: they show in the chat's **System** tab, with an unread count, and not in **Global** or **Local**. The kill feed names the pilot credited with the kill.

<!-- seeker-glance:end -->

## The members

- **Boss Seeker**: a much larger Seeker, in the swarm's tint and with its name over it, with many times a Seeker's hull, shield and damage (the numbers are below). It is passive: it roams until a pilot hits it, then stops where it is and fires at that pilot, and the ships of its swarm that are close join in. Its weapon's range and its speed are a Seeker's, and it never mends its hull by itself. Its [three steps](#the-leaders-three-steps) and a [special ability](/wiki/03-Mechanics/Special-Abilities.md) can change that.
- **Seeker Slave**: a plain Seeker in the swarm's tint. Slaves keep close to the boss, join the fight when a swarm ship near them is hit, and each one that is near the boss heals its hull. A slave mends its own hull after a rest, as a Seeker does.

## How the fight goes

- **Leave it alone until your ship can take it.** A Boss Seeker hits harder than any pilot's first ship can bear: a new pilot's Protos, with no shield yet, is destroyed in seconds once the boss and its slaves are on it.
- **Stay out of reach.** The boss and its slaves are slower than a Protos, and their weapons reach less far than a Quantum Laser II's (see [Lasers & Ammo](/wiki/06-Items/Lasers.md)): a pilot who has such lasers and keeps beyond their range takes no damage while it fires. A pilot with Quantum Laser I cannot stay out of reach.
- **The slaves heal faster than a lone new pilot hits.** Together they mend more than one pilot's lasers deal with x1 ammo, so bring a partner and x2 ammo. Two pilots with Quantum Laser II who keep their distance take the boss down in about a minute in Alpha, and much faster with x2 ammo.
- **The boss comes back** after the time in the *At a glance* list, at full strength, in the same sector, and its slaves come one after the other.

## The leader's three steps {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Its fight has three steps ([how they work](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); each one happens once.

- **At the start**: Its Seeker Slaves mend it ×2 as fast for 8 s.
- **Under two thirds**: 2 copies of it appear, and the real one wears a ring.
- **Under a third**: Flies away from the pilots for 4 s, then turns back.

<!-- mob-ladder:end -->

## Rewards and drops

The Boss Seeker pays **exactly ten Seekers**: ten times a Seeker's Credits, Thulium, XP and Honor, split by damage among the pilots who fought it ([how a boss kill pays](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Its box holds ten Seekers' loot and, on top of it, ammo and rockets below Epic, for the pilot who dealt the most damage. The slaves pay a small amount and drop nothing; killing them is no way to farm, since they come back with the boss.

## The numbers

The numbers of the swarm's ships in the three worlds ([Worlds](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker

Built from the Seeker at 400% of its hull, shield and damage; its speed and range are the ship's own.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | {{guide:vitals.hull@Boss Seeker#1}} | {{guide:vitals.hull@Boss Seeker#2}} | {{guide:vitals.hull@Boss Seeker#3}} |
| Shield | {{guide:vitals.shield@Boss Seeker#1}} | {{guide:vitals.shield@Boss Seeker#2}} | {{guide:vitals.shield@Boss Seeker#3}} |
| Laser damage (a volley a second) | {{guide:vitals.dps@Boss Seeker#1}} | {{guide:vitals.dps@Boss Seeker#2}} | {{guide:vitals.dps@Boss Seeker#3}} |
| Speed | {{guide:vitals.speed@Boss Seeker#1}} | {{guide:vitals.speed@Boss Seeker#2}} | {{guide:vitals.speed@Boss Seeker#3}} |
| Laser range | 600 | 600 | 600 |
| Aggro radius | only when attacked | only when attacked | only when attacked |
| Credits | {{guide:spoils.pay.credits@Boss Seeker#1}} | {{guide:spoils.pay.credits@Boss Seeker#2}} | {{guide:spoils.pay.credits@Boss Seeker#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Seeker#1}} | {{guide:spoils.pay.thulium@Boss Seeker#2}} | {{guide:spoils.pay.thulium@Boss Seeker#3}} |
| Experience (XP) | {{guide:spoils.pay.experience@Boss Seeker#1}} | {{guide:spoils.pay.experience@Boss Seeker#2}} | {{guide:spoils.pay.experience@Boss Seeker#3}} |
| Honor | {{guide:spoils.pay.honor@Boss Seeker#1}} | {{guide:spoils.pay.honor@Boss Seeker#2}} | {{guide:spoils.pay.honor@Boss Seeker#3}} |
| PvE points per kill | 5 | 5 | 5 |

**Drop**: one box, for the pilot who dealt the most damage.

| Item |
| :--- |
| {{guide:spoils.box@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} |

### Seeker Slave

Built from the Seeker at 100% of its hull, shield and damage; its speed and range are the ship's own.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | {{guide:vitals.hull@Seeker Slave#1}} | {{guide:vitals.hull@Seeker Slave#2}} | {{guide:vitals.hull@Seeker Slave#3}} |
| Shield | {{guide:vitals.shield@Seeker Slave#1}} | {{guide:vitals.shield@Seeker Slave#2}} | {{guide:vitals.shield@Seeker Slave#3}} |
| Laser damage (a volley a second) | {{guide:vitals.dps@Seeker Slave#1}} | {{guide:vitals.dps@Seeker Slave#2}} | {{guide:vitals.dps@Seeker Slave#3}} |
| Speed | {{guide:vitals.speed@Seeker Slave#1}} | {{guide:vitals.speed@Seeker Slave#2}} | {{guide:vitals.speed@Seeker Slave#3}} |
| Laser range | 600 | 600 | 600 |
| Aggro radius | only when attacked | only when attacked | only when attacked |
| Heals the leader, each, per second (hull only) | 50 | 75 | 100 |
| Credits | {{guide:spoils.pay.credits@Seeker Slave#1}} | {{guide:spoils.pay.credits@Seeker Slave#2}} | {{guide:spoils.pay.credits@Seeker Slave#3}} |
| Thulium | {{guide:spoils.pay.thulium@Seeker Slave#1}} | {{guide:spoils.pay.thulium@Seeker Slave#2}} | {{guide:spoils.pay.thulium@Seeker Slave#3}} |
| Experience (XP) | {{guide:spoils.pay.experience@Seeker Slave#1}} | {{guide:spoils.pay.experience@Seeker Slave#2}} | {{guide:spoils.pay.experience@Seeker Slave#3}} |
| Honor | {{guide:spoils.pay.honor@Seeker Slave#1}} | {{guide:spoils.pay.honor@Seeker Slave#2}} | {{guide:spoils.pay.honor@Seeker Slave#3}} |
| PvE points per kill | 1 | 1 | 1 |

**Drop**: none. The kill pays its Credits, Thulium, XP and Honor only.

<!-- seeker-members:end -->
