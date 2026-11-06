# Swarms

A **swarm** is a group of aliens that roams part of the galaxy under a **leader**: a boss, far stronger than any alien around it, with **followers** that guard it and, in most of the swarms, heal it. There are seven, and each has an article of its own:

- [Seeker Swarm](/wiki/05-Swarms/Seeker-Swarm.md): the Boss Seeker and its Seeker Slaves, the smallest swarm, in the sectors where new pilots fly.
- [Pirate Swarm](/wiki/05-Swarms/Pirate-Swarm.md): the Pirate Boss and its Pirate Scouts, a long fight for a group.
- [Dormant Swarm](/wiki/05-Swarms/Dormant-Swarm.md): the Dormant Force and its Dormant Pulses, the strongest swarm, with the richest drops.
- [Phantasm Swarm](/wiki/05-Swarms/Phantasm-Swarm.md): the Boss Phantasm and its Phantasm Guards, a huge Phantasm for a group of mid-level pilots, on the outer sectors of the companies.
- [Goombah Swarm](/wiki/05-Swarms/Goombah-Swarm.md): the Boss Goombah and its Goombah Guards, a huge Goombah for a group of the strongest pilots, on the same sectors.
- [Crystalys Swarm](/wiki/05-Swarms/Crystalys-Swarm.md): the Boss Crystalys and its Crystalys Guards, the toughest alien grown larger, in three of the Danger Sectors.
- [Tesseract Swarm](/wiki/05-Swarms/Tesseract-Swarm.md): the Tesseract, a huge mothership that releases Facets while it is being hit, for a very large group, in the Danger Sector `DS-4`.

Their ships are **aliens of kinds of their own**: they have their own names and their own kill counts, and none of them counts as a Seeker, a Phantasm or any other alien. A swarm ship has the shape of the ship it is built on, in a tint of its own, with its name over it; the Boss Seeker is a much larger Seeker.

The **Clan Wardens** are not public swarms. A clan calls its own Warden for the last step of its daily line, and only that clan can hurt it: no pilot meets one roaming a sector, and the tables below do not list them. A Warden is paid by damage like a swarm boss, but its loot is not one box for the top dealer: every pilot who dealt 5% or more gets a [private box](/wiki/03-Mechanics/Cargo.md#private-boxes) of his own. See [Clans](/wiki/03-Mechanics/Clans.md#clan-wardens).

## The swarms

<!-- swarms-list:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Swarm | Where | How many | Leader | Followers | Comes back |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**Pirate Swarm**](/wiki/05-Swarms/Pirate-Swarm.md) | The sectors `x-2` and `x-3` of every company | One in each of those sectors, 6 in each world | **Pirate Boss** | Up to 5 × Pirate Scout, a new one every 10 s | 2 min after the leader is destroyed, in the same sector |
| [**Dormant Swarm**](/wiki/05-Swarms/Dormant-Swarm.md) | The Danger Sectors `DS-1`, `DS-2`, `DS-3`, `DS-4`, flying from one to another | One in each world | **Dormant Force** | 2 × Dormant Pulse, flying with the leader | 1 h after the whole swarm is destroyed, in a random Danger Sector. From season day 11: 30 min, at the [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md), and every ship pays ×2 |
| [**Seeker Swarm**](/wiki/05-Swarms/Seeker-Swarm.md) | The sectors `x-1` and `x-2` of every company | One in each of those sectors, 6 in each world | **Boss Seeker** | Up to 4 × Seeker Slave, a new one every 10 s | 2 min after the leader is destroyed, in the same sector |
| [**Phantasm Swarm**](/wiki/05-Swarms/Phantasm-Swarm.md) | The sectors `x-3` and `x-4` of every company | One in each of those sectors, 6 in each world | **Boss Phantasm** | Up to 4 × Phantasm Guard, a new one every 10 s | 2 min after the leader is destroyed, in the same sector |
| [**Goombah Swarm**](/wiki/05-Swarms/Goombah-Swarm.md) | The sectors `x-3` and `x-4` of every company | One in each of those sectors, 6 in each world | **Boss Goombah** | Up to 4 × Goombah Guard, a new one every 10 s | 5 min after the leader is destroyed, in the same sector |
| [**Crystalys Swarm**](/wiki/05-Swarms/Crystalys-Swarm.md) | The Danger Sectors `DS-1`, `DS-2`, `DS-3` | One in each of those sectors, 3 in each world | **Boss Crystalys** | Up to 3 × Crystalys Guard, a new one every 10 s | 30 min after the leader is destroyed, in the same sector |
| [**Tesseract Swarm**](/wiki/05-Swarms/Tesseract-Swarm.md) | The Danger Sector `DS-4` | One in each world | **Tesseract** | Up to 100 × Facet, 20 more every 5 s while the leader is being hit | 30 min after the leader is destroyed, in the same sector |

<!-- swarms-list:end -->

## When and where

The swarms begin to appear at **First Contact** and stay until the wipe (see the [Wipe Timeline](/wiki/03-Mechanics/Wipe-Timeline.md); the day is the first line of the rules below). **Every world has its own swarms** in the same places, so the Pirate Boss of Alpha and the one of Beta are two different ships, and a swarm you destroy in your world is not destroyed in another. A swarm that is destroyed comes back after the time in the table above. The Dormant Swarm changes on season day 11 (event 2): it appears at the [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md), comes back sooner and pays twice as much. In Beta and Gamma the swarms appear from the first day of the season.

## The rules of every swarm

<!-- swarms-rules:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- The swarms appear from season day 4 until the wipe; in Beta and Gamma they appear from season day 1.
- When a swarm ship is hit, the ships of its swarm within 1,500 units of it join the fight against the first pilot who hit it.
- A leader appears at least 2,500 units from the edge of every station and gate ring.
- A pilot who dealt at least 5% of the damage done to a boss is paid for its kill.

<!-- swarms-rules:end -->

## The worlds

The world scales a swarm as it scales every alien ([Worlds](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): a swarm ship's hull, shield, shield recharge, laser damage, rocket damage and healing are the Alpha numbers times the strength below, and a kill pays the pay below. Speed, range and drops are the same in every world. The articles give each ship's numbers in all three worlds.

<!-- swarms-world:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| World | Strength | Pay |
| :--- | ---: | ---: |
| **Alpha** | ×1 | ×1 |
| **Beta** | ×1.5 | ×2 |
| **Gamma** | ×2 | ×3 |

<!-- swarms-world:end -->

## What the pilots are told

The Seeker, Pirate, Phantasm, Goombah, Crystalys and Tesseract swarms tell the pilots of their own sector when a boss appears and when it is destroyed. The Dormant Swarm tells its whole world, and it is marked on the maps of the Danger Sectors and on the galaxy map, so that pilots can find it. These are System lines: they show in the chat's **System** tab, with an unread count, and not in **Global** or **Local**. A boss kill also gets a line in the kill feed that names the pilot credited with it. The *At a glance* list of each article says who is told.

## Fighting a swarm

- **The leaders never start a fight.** A leader roams until a pilot hits it, then fights back, and the ships of its swarm close to it join in against the first pilot who hit it (the distance is in the rules above). The Pirate Scouts are the exception: they attack any pilot who comes near. A leader never mends its hull by itself, so the damage you did stays on it unless its followers heal it; its shield recharges as every alien's does. Only the Tesseract is different: it has no weapon, it mends its hull and shield by itself once nobody has hurt it for a few seconds, and its Facets fly round it and fire on the nearest pilot who has hit it, instead of going after the first one who hit it.
- **Swarm ships fight pilots only.** They do not shoot aliens and aliens do not shoot them, and [company pilots](/wiki/03-Mechanics/Company-Pilots.md) ignore them: they neither hunt a swarm ship nor come to your help against one.
- **Rockets.** The Pirate Boss and the Dormant Force and Pulses fire **straight** rockets, [Rivet rockets](/wiki/06-Items/Rockets.md), at the pilot who attacked them. A ship that keeps moving sidesteps them, one that stands still is hit.
- **The shape of the fights.** The Seeker Swarm is for two pilots, the Pirate Swarm and the Phantasm Swarm for a small group, the Goombah Swarm for a group of the strongest ships, the Crystalys Swarm and the Dormant Swarm for a large group of them, the Tesseract Swarm for a very large one; the bigger worlds need more pilots, as for every alien.

## What to bring

- **A group.** Fly in a [group](/wiki/03-Mechanics/Groups.md): the swarms are balanced for groups, a lone pilot of a low level is destroyed fast, and only the strongest ships can take a Pirate Boss alone. Nobody takes the Dormant Swarm alone. A swarm fights the first pilot who hit it ([Who an Alien Fights](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)), so let the sturdiest ship of the group start.
- **Better ammo.** Bring x2 ammo or better (see [Lasers & Ammo](/wiki/06-Items/Lasers.md)). The healing of a swarm's followers can be more than a small group deals with x1 ammo.
- **Shields and repairs** for a long fight: the abilities of your ship ([Abilities](/wiki/03-Mechanics/Abilities.md)) matter most in the Pirate fight, which takes minutes.
- **Room to move.** Stay beyond the reach of a weapon you out-range, and keep moving against a rocket.

## How a boss kill pays

An ordinary alien pays the pilot who hit it first ([Combat](/wiki/03-Mechanics/Combat.md#kill-rewards-first-hit-claims)). The leader of a swarm, and each Dormant Pulse, pay **by the damage dealt** instead:

- **The pay is split by damage.** Every pilot who dealt at least the share given in the rules above is paid, in proportion to the damage dealt: the Credits, Thulium, XP and Honor of the kill are split among them. A pilot below the share is paid nothing.
- **The cargo box goes to the pilot who dealt the most damage.** It is that pilot's (and its clan's) for 30 seconds, as for any alien, and then anyone can take it ([Cargo](/wiki/03-Mechanics/Cargo.md)). Each Dormant ship has its own damage count and its own box.
- **Followers pay the usual way**: the Pirate Scouts, the Seeker Slaves and the guards of the Phantasm, Goombah and Crystalys swarms pay the pilot who hit them first, and their pay is small next to a boss's.
- **The pay of a boss is made to beat the aliens around it.** A minute of fighting a Pirate Boss, a Boss Phantasm or a Boss Goombah pays more than a minute of fighting a Goombah, and a minute of fighting the Dormant Swarm or a Boss Crystalys pays more than a minute of fighting a Crystalys; the Boss Seeker pays exactly ten Seekers.
- **The Dormant Swamp's aliens** (the Slumbering Void, the Inert Mass and the Unwakened) are paid like a boss, by damage, and add PvE points to your ranking; their numbers are in [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#the-aliens).

Every kill is counted under the ship's own name in your kill statistics, and adds PvE points to your ranking:

<!-- swarms-points:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Swarm ship | Swarm | PvE points per kill |
| :--- | :--- | ---: |
| **Pirate Boss** | Pirate Swarm | 15 |
| **Pirate Scout** | Pirate Swarm | 4 |
| **Dormant Force** | Dormant Swarm | 25 |
| **Dormant Pulse** | Dormant Swarm | 11 |
| **Boss Seeker** | Seeker Swarm | 5 |
| **Seeker Slave** | Seeker Swarm | 1 |
| **Boss Phantasm** | Phantasm Swarm | 8 |
| **Phantasm Guard** | Phantasm Swarm | 1 |
| **Boss Goombah** | Goombah Swarm | 14 |
| **Goombah Guard** | Goombah Swarm | 3 |
| **Boss Crystalys** | Crystalys Swarm | 30 |
| **Crystalys Guard** | Crystalys Swarm | 6 |
| **Tesseract** | Tesseract Swarm | 42 |
| **Facet** | Tesseract Swarm | 0 |

<!-- swarms-points:end -->

A swarm kill does not count as a kill of any other alien: a Boss Seeker or a Seeker Slave is no Seeker for a mission that asks for Seekers, and the Wipe Point milestones ([Wipe Timeline](/wiki/03-Mechanics/Wipe-Timeline.md#earning-wipe-points)) are those of the five aliens only. The missions that ask for swarm ships are listed under [Swarm missions](/wiki/03-Mechanics/Quests.md#swarm-missions).
