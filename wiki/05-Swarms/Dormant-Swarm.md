# Dormant Swarm

The Dormant Swarm is a **Dormant Force** with its **Dormant Pulses**: a group of ships that never start a fight and hit very hard once they are woken. There is only one in each world's Danger Sectors (the [Deep Void](/wiki/03-Mechanics/Deep-Void.md#the-dormant-swarms-visit) has a visit of its own, once a day). It wanders from one Danger Sector to the next, and it is the hardest fight and the richest drop of the swarms: a fight for a large group of the strongest ships. From season day 11 it starts at the [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) on `DS-4`, comes back sooner and pays twice as much (see the *At a glance* list).

## At a glance

<!-- dormant-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Where**: The Danger Sectors `DS-1`, `DS-2`, `DS-3`, `DS-4`, flying from one to another
- **How many**: One in each world
- **Appears**: From season day 4 until the wipe (Beta and Gamma: from season day 1)
- **Leader**: Dormant Force
- **Followers**: 2 × Dormant Pulse, flying with the leader
- **Followers stay within**: 700 units of the leader
- **Leader destroyed**: A Dormant Pulse takes over as leader
- **Leader destroyed**: The followers leave 30 s after the leader is destroyed, attacking or not
- **Travels**: Stays 8 to 15 min on a map, then flies to the gate of another Danger Sector. It never takes the gates out of the Danger Sectors and never enters the black hole's ring
- **Comes back**: {{guide:vitals.respawn@Dormant Force#1;Dormant Force#2;Dormant Force#3}} after the whole swarm is destroyed, in a random Danger Sector
- **From season day 11**: It appears at the [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) on `DS-4` instead of a random Danger Sector, comes back 30 min after the whole swarm is destroyed, and every ship pays ×2 (Credits, Thulium, XP and Honor; the drop stays the same)
- **Announced**: The pilots of the whole world are told when the swarm appears and when it is destroyed. These are System lines: they show in the chat's **System** tab, with an unread count, and not in **Global** or **Local**. A marker shows it on the maps of the Danger Sectors and on the galaxy map. The kill feed names the pilot credited with the kill.

<!-- dormant-glance:end -->

## The members

- **Dormant Force**: a Wraith at full strength, with lasers that hit three times as hard as a typical fit's. It leads the swarm, is passive until it is hit, and fires **straight rockets** at the first pilot who hit it.
- **Dormant Pulse**: a Paragon at full strength, with heavy lasers of the same kind, each hitting twice as hard as one of the Force's, and its own rockets. A Pulse has fewer lasers than the Force, so its whole volley is bigger than the Force's, not twice as big (the numbers are below). The Pulses fly close to the Force, and when the Force is destroyed one of them takes over as leader.

They are passive: they never go after a pilot. Hit one of them, and the others close to it join in against the first pilot who hit it.

## How the fight goes

- **Find it.** The whole world is told when it appears, and a marker shows it on the maps of the Danger Sectors and on the galaxy map. It stays on a map for the time in the *At a glance* list, then flies to the gate of another Danger Sector and jumps; it never takes a gate out of the Danger Sectors and never goes into the black hole's ring. It flies at the speed of its slowest ship, and like a pilot it does not start or end a jump while it is under fire. From season day 11 it first appears just outside the zone of the [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md), where a group can wait for it out of the swamp's guns, and then flies out through a gate of `DS-4`.
- **It cannot be taken alone, or by a few.** Eight level 8 pilots in Paragons with x2 or x4 ammo destroy it in about a minute in Alpha, losing at most one ship; one Paragon alone is destroyed, and so are three or four with x2 ammo. The swarms of Beta and Gamma are stronger ([Worlds](/wiki/05-Swarms/Swarms.md#the-worlds)), so those worlds need larger groups.
- **Its lasers decide the fight.** Together they can destroy a Paragon in under a minute, and even one with the best shields in under two, rockets or not: bring your damage fast, with the best shields you have.
- **Ship by ship.** Each ship has its own hull and its own pay, so the Force or a Pulse can be destroyed first. The swarm is replaced only when all of it is destroyed, after the time in the *At a glance* list.

## The leader's three steps {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Its fight has three steps ([how they work](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); each one happens once.

- **At the start**: Takes 70% of every hit while one of its Dormant Pulses lives.
- **Under two thirds**: Its Dormant Pulses fire a rocket every 2.5 s for 15 s.
- **Under a third**: While all its Dormant Pulses live they mend it by 5% of its hull a second for 6 s.

<!-- mob-ladder:end -->

## Rewards and drops

Each ship pays by itself, by the damage dealt to it ([how a boss kill pays](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)), and each drops a box for the pilot who dealt the most damage to it. The **Force's box** is the prize: a great deal of x3 and x4 ammo, Epic rockets of one kind, and, now and then, a N.I.K.E. or a N.U.K.E. The **Pulses** may drop an Ancient Control Unit, a Power Core or Dark Matter. A minute of fighting the swarm pays more than a minute of fighting the Crystalys, the best-paid alien. From season day 11 every ship pays twice as much (the *At a glance* list); the boxes are the same.

## The numbers

The numbers of the swarm's ships in the three worlds ([Worlds](/wiki/05-Swarms/Swarms.md#the-worlds)). The Credits, Thulium, XP and Honor of the tables are the pay before season day 11; from that day a kill pays twice as much.

<!-- dormant-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Dormant Force

Built from the Wraith at 100% of its hull and 300% of its laser damage; its speed and range are the ship's own. Fires a straight rocket every 5 s: [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | {{guide:vitals.hull@Dormant Force#1}} | {{guide:vitals.hull@Dormant Force#2}} | {{guide:vitals.hull@Dormant Force#3}} |
| Shield | {{guide:vitals.shield@Dormant Force#1}} | {{guide:vitals.shield@Dormant Force#2}} | {{guide:vitals.shield@Dormant Force#3}} |
| Laser damage (a volley a second) | {{guide:vitals.dps@Dormant Force#1}} | {{guide:vitals.dps@Dormant Force#2}} | {{guide:vitals.dps@Dormant Force#3}} |
| Speed | {{guide:vitals.speed@Dormant Force#1}} | {{guide:vitals.speed@Dormant Force#2}} | {{guide:vitals.speed@Dormant Force#3}} |
| Laser range | 800 | 800 | 800 |
| Aggro radius | only when attacked | only when attacked | only when attacked |
| Rocket damage, at most | {{guide:behaviour.ability:rocket.damage@Dormant Force#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#3}} |
| Credits | {{guide:spoils.pay.credits@Dormant Force#1}} | {{guide:spoils.pay.credits@Dormant Force#2}} | {{guide:spoils.pay.credits@Dormant Force#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Force#1}} | {{guide:spoils.pay.thulium@Dormant Force#2}} | {{guide:spoils.pay.thulium@Dormant Force#3}} |
| Experience (XP) | {{guide:spoils.pay.experience@Dormant Force#1}} | {{guide:spoils.pay.experience@Dormant Force#2}} | {{guide:spoils.pay.experience@Dormant Force#3}} |
| Honor | {{guide:spoils.pay.honor@Dormant Force#1}} | {{guide:spoils.pay.honor@Dormant Force#2}} | {{guide:spoils.pay.honor@Dormant Force#3}} |
| PvE points per kill | 25 | 25 | 25 |

**Drop**: one box, for the pilot who dealt the most damage.

| Item |
| :--- |
| {{guide:spoils.box@Dormant Force#1;Dormant Force#2;Dormant Force#3}} |

### Dormant Pulse

Built from the Paragon at 100% of its hull and 600% of its laser damage; its speed and range are the ship's own. Fires a straight rocket every 5 s: [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | {{guide:vitals.hull@Dormant Pulse#1}} | {{guide:vitals.hull@Dormant Pulse#2}} | {{guide:vitals.hull@Dormant Pulse#3}} |
| Shield | {{guide:vitals.shield@Dormant Pulse#1}} | {{guide:vitals.shield@Dormant Pulse#2}} | {{guide:vitals.shield@Dormant Pulse#3}} |
| Laser damage (a volley a second) | {{guide:vitals.dps@Dormant Pulse#1}} | {{guide:vitals.dps@Dormant Pulse#2}} | {{guide:vitals.dps@Dormant Pulse#3}} |
| Speed | {{guide:vitals.speed@Dormant Pulse#1}} | {{guide:vitals.speed@Dormant Pulse#2}} | {{guide:vitals.speed@Dormant Pulse#3}} |
| Laser range | 800 | 800 | 800 |
| Aggro radius | only when attacked | only when attacked | only when attacked |
| Rocket damage, at most | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#3}} |
| Credits | {{guide:spoils.pay.credits@Dormant Pulse#1}} | {{guide:spoils.pay.credits@Dormant Pulse#2}} | {{guide:spoils.pay.credits@Dormant Pulse#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Pulse#1}} | {{guide:spoils.pay.thulium@Dormant Pulse#2}} | {{guide:spoils.pay.thulium@Dormant Pulse#3}} |
| Experience (XP) | {{guide:spoils.pay.experience@Dormant Pulse#1}} | {{guide:spoils.pay.experience@Dormant Pulse#2}} | {{guide:spoils.pay.experience@Dormant Pulse#3}} |
| Honor | {{guide:spoils.pay.honor@Dormant Pulse#1}} | {{guide:spoils.pay.honor@Dormant Pulse#2}} | {{guide:spoils.pay.honor@Dormant Pulse#3}} |
| PvE points per kill | 11 | 11 | 11 |

**Drop**: one box, for the pilot who dealt the most damage.

| Item |
| :--- |
| {{guide:spoils.box@Dormant Pulse#1;Dormant Pulse#2;Dormant Pulse#3}} |

<!-- dormant-members:end -->
