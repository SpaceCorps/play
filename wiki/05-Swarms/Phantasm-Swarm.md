# Phantasm Swarm

The Phantasm Swarm is a **Boss Phantasm** with its **Phantasm Guards**: an enormous [Phantasm](/wiki/04-Aliens/Phantasm.md) that never starts a fight, and smaller ones that stay close to it and heal it. It lives on the outer sectors of the companies, `x-3` and `x-4`, and it is a fight for a group of pilots at the middle levels.

## At a glance

<!-- phantasm-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Where**: The sectors `x-3` and `x-4` of every company
- **How many**: One in each of those sectors, 6 in each world
- **Appears**: From season day 4 until the wipe (Beta and Gamma: from season day 1)
- **Leader**: Boss Phantasm
- **Followers**: Up to 4 × Phantasm Guard, a new one every 10 s
- **Followers stay within**: 500 units of the leader
- **Healing**: Each Phantasm Guard within 600 units of the leader heals its hull, 30 HP a second in Alpha
- **Leader destroyed**: The followers leave 30 s after the leader is destroyed, unless they are attacking
- **Comes back**: 2 min after the leader is destroyed, in the same sector
- **Announced**: The pilots of the sector are told when the leader appears and when it is destroyed. These are System lines: they show in the chat's **System** tab, with an unread count, and not in **Global** or **Local**. The kill feed names the pilot credited with the kill.

<!-- phantasm-glance:end -->

## The members

- **Boss Phantasm**: a larger Phantasm, in the swarm's tint and with its name over it, with a hull, a shield and a laser volley of its own (the numbers are below). It is passive: it roams until a pilot hits it, then goes after that pilot and fires at it, and the ships of its swarm that are close join in. Its weapon's range and its speed are those of a Phantasm, and it never mends its hull by itself.
- **Phantasm Guard**: a smaller Phantasm in the swarm's tint. Guards keep close to the boss, join the fight when a swarm ship near them is hit, and each one that is near the boss heals its hull. A guard mends its own hull after a rest, as a Phantasm does.

## How the fight goes

- **Bring a group.** Three level 4–5 pilots with x2 ammo destroy it in about a minute and a half in Alpha, losing at most one ship; one pilot of that level alone is destroyed, and so are two. Better ships and x4 ammo make it much quicker.
- **Shoot the boss, not the guards.** A guard falls in seconds, but a new one comes as often as the *At a glance* list says, and what the guards heal is a small part of what a group deals: leaving them alone costs a little time, chasing them costs more.
- **Beta and Gamma are harder.** The swarms of those worlds are stronger ([Worlds](/wiki/05-Swarms/Swarms.md#the-worlds)), so they need more pilots or better ammo.
- **Watch the sector.** `x-4` is a PvP sector in Alpha, and `x-3` and `x-4` are in Beta and Gamma ([Worlds](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): a rival can join the fight or wait for the box. Keep a ship of the group on watch.
- **The boss comes back** after the time in the *At a glance* list, at full strength, in the same sector, and its guards come one after the other.

## Rewards and drops

The Boss Phantasm pays for the fight it is: a minute of fighting it pays more than a minute of fighting a Goombah, the best-paid alien of these sectors. The pay is split by damage among the pilots who fought it ([how a boss kill pays](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Its box is for the pilot who dealt the most damage and holds a Phantasm's own drops many times over (Ship Fragments, Daraxium and Nyxite), with ammo and rockets. The guards pay a small amount and drop nothing; killing them is no way to farm, since they come back with the boss.

## The numbers

The numbers of the swarm's ships in the three worlds ([Worlds](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- phantasm-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Phantasm

Built from the Phantasm at 2,000% of its hull and 300% of its laser damage; its speed and range are the ship's own.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | 40,000 | 60,000 | 80,000 |
| Shield | 64,000 | 96,000 | 128,000 |
| Laser damage (a volley a second) | 1,050 | 1,575 | 2,100 |
| Speed | 160 | 160 | 160 |
| Laser range | 700 | 700 | 700 |
| Aggro radius | only when attacked | only when attacked | only when attacked |
| Credits | 39,000 | 78,000 | 117,000 |
| Thulium | 195 | 390 | 585 |
| Experience (XP) | 7,800 | 15,600 | 23,400 |
| Honor | 62 | 124 | 186 |
| PvE points per kill | 8 | 8 | 8 |

**Drop**: one box, for the pilot who dealt the most damage.

| Item | Chance | Amount |
| :--- | ---: | ---: |
| Ship Fragment | 100% on each of 13 rolls | 1 |
| Daraxium | 60% on each of 13 rolls | 1–2 |
| Nyxite | 60% on each of 13 rolls | 1–2 |
| Standard Battery | 100% | 600–1,200 |
| Advanced Plasma | 100% | 60–100 |
| Ultra Core | 100% | 10–20 |
| One of the 8 [rockets](/wiki/06-Items/Rockets.md) bought with Credits, picked at random | 100% | 4–6 |

### Phantasm Guard

Built from the Phantasm at 50% of its hull, shield and damage; its speed and range are the ship's own.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | 1,000 | 1,500 | 2,000 |
| Shield | 1,600 | 2,400 | 3,200 |
| Laser damage (a volley a second) | 175 | 263 | 350 |
| Speed | 160 | 160 | 160 |
| Laser range | 700 | 700 | 700 |
| Aggro radius | only when attacked | only when attacked | only when attacked |
| Heals the leader, each, per second (hull only) | 30 | 45 | 60 |
| Credits | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Experience (XP) | 12 | 24 | 36 |
| Honor | 1 | 2 | 3 |
| PvE points per kill | 1 | 1 | 1 |

**Drop**: none. The kill pays its Credits, Thulium, XP and Honor only.

<!-- phantasm-members:end -->
