# Swarms

A **swarm** is a group of aliens that roams part of the galaxy under a **leader**: a boss, far stronger than any alien around it, with **followers** that guard it and, in two of the swarms, heal it. There are three, and each has an article of its own:

- [Seeker Swarm](/wiki/05-Swarms/Seeker-Swarm.md): the Boss Seeker and its Seeker Slaves, the smallest swarm, in the sectors where new pilots fly.
- [Pirate Swarm](/wiki/05-Swarms/Pirate-Swarm.md): the Pirate Boss and its Pirate Scouts, a long fight for a group.
- [Dormant Swarm](/wiki/05-Swarms/Dormant-Swarm.md): the Dormant Force and its Dormant Pulses, the strongest swarm, with the richest drops.

Their ships are **aliens of kinds of their own**: they have their own names and their own kill counts, and none of them counts as a Seeker, a Phantasm or any other alien. A swarm ship has the shape of the ship it is built on, in a tint of its own, with its name over it; the Boss Seeker is a much larger Seeker.

## The three swarms {#the-three-swarms}

<!-- swarms-list:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Swarm | Where | How many | Leader | Followers | Comes back |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**Pirate Swarm**](/wiki/05-Swarms/Pirate-Swarm.md) | The sectors `x-2` and `x-3` of every company | One in each of those sectors, 6 in each world | **Pirate Boss** | Up to 5 × Pirate Scout, a new one every 10 s | 2 min after the leader is destroyed, in the same sector |
| [**Dormant Swarm**](/wiki/05-Swarms/Dormant-Swarm.md) | The Danger Sectors `DS-1`, `DS-2`, `DS-3`, `DS-4`, flying from one to another | One in each world | **Dormant Force** | 2 × Dormant Pulse, flying with the leader | 1 h after the whole swarm is destroyed, in a random Danger Sector |
| [**Seeker Swarm**](/wiki/05-Swarms/Seeker-Swarm.md) | The sectors `x-1` and `x-2` of every company | One in each of those sectors, 6 in each world | **Boss Seeker** | Up to 4 × Seeker Slave, a new one every 10 s | 2 min after the leader is destroyed, in the same sector |

<!-- swarms-list:end -->

## When and where {#when-and-where}

The swarms begin to appear at **First Contact** and stay until the wipe (see the [Wipe Timeline](/wiki/03-Mechanics/Wipe-Timeline.md); the day is the first line of the rules below). **Every world has its own swarms** in the same places, so the Pirate Boss of Alpha and the one of Beta are two different ships, and a swarm you destroy in your world is not destroyed in another. A swarm that is destroyed comes back after the time in the table above.

## The rules of every swarm {#the-rules-of-every-swarm}

<!-- swarms-rules:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- The swarms appear from season day 4 until the wipe.
- When a swarm ship is hit, the ships of its swarm within 1,500 units of it join the fight against the first pilot who hit it.
- A leader appears at least 2,500 units from the edge of every station and gate ring.
- A pilot who dealt at least 5% of the damage done to a boss is paid for its kill.

<!-- swarms-rules:end -->

## The worlds {#the-worlds}

The world scales a swarm as it scales every alien ([Worlds](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): a swarm ship's hull, shield, shield recharge, laser damage, rocket damage and healing are the Alpha numbers times the strength below, and a kill pays the pay below. Speed, range and drops are the same in every world. The articles give each ship's numbers in all three worlds.

<!-- swarms-world:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| World | Strength | Pay |
| :--- | ---: | ---: |
| **Alpha** | ×1 | ×1 |
| **Beta** | ×1.5 | ×2 |
| **Gamma** | ×2 | ×3 |

<!-- swarms-world:end -->

## What the pilots are told {#what-the-pilots-are-told}

The Seeker and Pirate swarms tell the pilots of their own sector when a boss appears and when it is destroyed. The Dormant Swarm tells its whole world, and it is marked on the maps of the Danger Sectors and on the galaxy map, so that pilots can find it. These are System lines: they show in the chat's **System** tab, with an unread count, and not in **Global** or **Local**. A boss kill also gets a line in the kill feed that names the pilot credited with it. The *At a glance* list of each article says who is told.

## Fighting a swarm {#fighting-a-swarm}

- **The leaders never start a fight.** A leader roams until a pilot hits it, then fights back, and the ships of its swarm close to it join in against the first pilot who hit it (the distance is in the rules above). The Pirate Scouts are the exception: they attack any pilot who comes near. A leader never mends its hull by itself, so the damage you did stays on it unless its followers heal it; its shield recharges as every alien's does.
- **Swarm ships fight pilots only.** They do not shoot aliens and aliens do not shoot them, and [company pilots](/wiki/03-Mechanics/Company-Pilots.md) ignore them: they neither hunt a swarm ship nor come to your help against one.
- **Rockets.** The Pirate Boss and the Dormant Force and Pulses fire **straight** rockets, [Rivet rockets](/wiki/06-Items/Rockets.md), at the pilot who attacked them. A ship that keeps moving sidesteps them, one that stands still is hit.
- **The shape of the fights.** The Seeker Swarm is for two pilots, the Pirate Swarm for a small group, the Dormant Swarm for a large group of the strongest ships; the bigger worlds need more pilots, as for every alien.

## What to bring {#what-to-bring}

- **A group.** Fly in a [group](/wiki/03-Mechanics/Groups.md): the swarms are balanced for groups, a lone pilot of a low level is destroyed fast, and only the strongest ships can take a Pirate Boss alone. Nobody takes the Dormant Swarm alone. A swarm fights the first pilot who hit it ([Who an Alien Fights](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)), so let the sturdiest ship of the group start.
- **Better ammo.** Bring x2 ammo or better (see [Lasers & Ammo](/wiki/06-Items/Lasers.md)). The healing of a swarm's followers can be more than a small group deals with x1 ammo.
- **Shields and repairs** for a long fight: the abilities of your ship ([Abilities](/wiki/03-Mechanics/Abilities.md)) matter most in the Pirate fight, which takes minutes.
- **Room to move.** Stay beyond the reach of a weapon you out-range, and keep moving against a rocket.

## How a boss kill pays {#how-a-boss-kill-pays}

An ordinary alien pays the pilot who hit it first ([Combat](/wiki/03-Mechanics/Combat.md#kill-rewards-first-hit-claims)). The leader of a swarm, and each Dormant Pulse, pay **by the damage dealt** instead:

- **The pay is split by damage.** Every pilot who dealt at least the share given in the rules above is paid, in proportion to the damage dealt: the Credits, Thulium, XP and Honor of the kill are split among them. A pilot below the share is paid nothing.
- **The cargo box goes to the pilot who dealt the most damage.** It is that pilot's (and its clan's) for 30 seconds, as for any alien, and then anyone can take it ([Cargo](/wiki/03-Mechanics/Cargo.md)). Each Dormant ship has its own damage count and its own box.
- **Followers pay the usual way**: the Pirate Scouts and the Seeker Slaves pay the pilot who hit them first, and their pay is small next to a boss's.
- **The pay of a boss is made to beat the aliens around it.** A minute of fighting a Pirate Boss pays more than a minute of fighting a Goombah, and the Dormant Swarm pays more still; the Boss Seeker pays exactly ten Seekers.

Every kill is counted under the ship's own name in your kill statistics, and adds PvE points to your ranking:

<!-- swarms-points:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Swarm ship | Swarm | PvE points per kill |
| :--- | :--- | ---: |
| **Pirate Boss** | Pirate Swarm | 10 |
| **Pirate Scout** | Pirate Swarm | 1 |
| **Dormant Force** | Dormant Swarm | 25 |
| **Dormant Pulse** | Dormant Swarm | 10 |
| **Boss Seeker** | Seeker Swarm | 5 |
| **Seeker Slave** | Seeker Swarm | 1 |

<!-- swarms-points:end -->

A swarm kill does not count as a kill of any other alien: a Boss Seeker or a Seeker Slave is no Seeker for a mission that asks for Seekers, and the Wipe Point milestones ([Wipe Timeline](/wiki/03-Mechanics/Wipe-Timeline.md#earning-wipe-points)) are those of the five aliens only.
