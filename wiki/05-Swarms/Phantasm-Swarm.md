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
- **Comes back**: {{guide:vitals.respawn@Boss Phantasm#1;Boss Phantasm#2;Boss Phantasm#3}} after the leader is destroyed, in the same sector
- **Announced**: The pilots of the sector are told when the leader appears and when it is destroyed. These are System lines: they show in the chat's **System** tab, with an unread count, and not in **Global** or **Local**. The kill feed names the pilot credited with the kill.

<!-- phantasm-glance:end -->

## The members

- **Boss Phantasm**: a larger Phantasm, in the swarm's tint and with its name over it, with a hull, a shield and a laser volley of its own (the numbers are below). It is passive: it roams until a pilot hits it, then goes after that pilot and fires at it, and the ships of its swarm that are close join in. Its weapon's range and its speed are those of a Phantasm, and it never mends its hull by itself. Its [three steps](#the-leaders-three-steps) and a [special ability](/wiki/03-Mechanics/Special-Abilities.md) can change that.
- **Phantasm Guard**: a smaller Phantasm in the swarm's tint. Guards keep close to the boss, join the fight when a swarm ship near them is hit, and each one that is near the boss heals its hull. A guard mends its own hull after a rest, as a Phantasm does.

## How the fight goes

- **Bring a group.** Three level 4–5 pilots with x2 ammo destroy it in about a minute and a half in Alpha, losing at most one ship; one pilot of that level alone is destroyed, and two only just win it, and only while the hits are shared. Better ships and x4 ammo make it much quicker.
- **Shoot the boss, not the guards.** A guard falls in seconds, but a new one comes as often as the *At a glance* list says, and what the guards heal is a small part of what a group deals: leaving them alone costs a little time, chasing them costs more.
- **Beta and Gamma are harder.** The swarms of those worlds are stronger ([Worlds](/wiki/05-Swarms/Swarms.md#the-worlds)), so they need more pilots or better ammo.
- **Watch the sector.** `x-4` is a PvP sector in Alpha, and `x-3` and `x-4` are in Beta and Gamma ([Worlds](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): a rival can join the fight or wait for the box. Keep a ship of the group on watch.
- **The boss comes back** after the time in the *At a glance* list, at full strength, in the same sector, and its guards come one after the other.

## The leader's three steps {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Its fight has three steps ([how they work](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); each one happens once.

- **At the start**: Each of its Phantasm Guards puts up a shield layer of 10% of its own hull.
- **Under two thirds**: 3 copies of it appear, and the real one wears a ring.
- **Under a third**: Blinks about 2,500 units away from the pilots, and its Phantasm Guards come back whole round it.

<!-- mob-ladder:end -->

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
| Hull | {{guide:vitals.hull@Boss Phantasm#1}} | {{guide:vitals.hull@Boss Phantasm#2}} | {{guide:vitals.hull@Boss Phantasm#3}} |
| Shield | {{guide:vitals.shield@Boss Phantasm#1}} | {{guide:vitals.shield@Boss Phantasm#2}} | {{guide:vitals.shield@Boss Phantasm#3}} |
| Laser damage (a volley a second) | {{guide:vitals.dps@Boss Phantasm#1}} | {{guide:vitals.dps@Boss Phantasm#2}} | {{guide:vitals.dps@Boss Phantasm#3}} |
| Speed | {{guide:vitals.speed@Boss Phantasm#1}} | {{guide:vitals.speed@Boss Phantasm#2}} | {{guide:vitals.speed@Boss Phantasm#3}} |
| Laser range | 700 | 700 | 700 |
| Aggro radius | only when attacked | only when attacked | only when attacked |
| Credits | {{guide:spoils.pay.credits@Boss Phantasm#1}} | {{guide:spoils.pay.credits@Boss Phantasm#2}} | {{guide:spoils.pay.credits@Boss Phantasm#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Phantasm#1}} | {{guide:spoils.pay.thulium@Boss Phantasm#2}} | {{guide:spoils.pay.thulium@Boss Phantasm#3}} |
| Experience (XP) | {{guide:spoils.pay.experience@Boss Phantasm#1}} | {{guide:spoils.pay.experience@Boss Phantasm#2}} | {{guide:spoils.pay.experience@Boss Phantasm#3}} |
| Honor | {{guide:spoils.pay.honor@Boss Phantasm#1}} | {{guide:spoils.pay.honor@Boss Phantasm#2}} | {{guide:spoils.pay.honor@Boss Phantasm#3}} |
| PvE points per kill | 8 | 8 | 8 |

**Drop**: one box, for the pilot who dealt the most damage.

| Item |
| :--- |
| {{guide:spoils.box@Boss Phantasm#1;Boss Phantasm#2;Boss Phantasm#3}} |

### Phantasm Guard

Built from the Phantasm at 50% of its hull, shield and damage; its speed and range are the ship's own.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | {{guide:vitals.hull@Phantasm Guard#1}} | {{guide:vitals.hull@Phantasm Guard#2}} | {{guide:vitals.hull@Phantasm Guard#3}} |
| Shield | {{guide:vitals.shield@Phantasm Guard#1}} | {{guide:vitals.shield@Phantasm Guard#2}} | {{guide:vitals.shield@Phantasm Guard#3}} |
| Laser damage (a volley a second) | {{guide:vitals.dps@Phantasm Guard#1}} | {{guide:vitals.dps@Phantasm Guard#2}} | {{guide:vitals.dps@Phantasm Guard#3}} |
| Speed | {{guide:vitals.speed@Phantasm Guard#1}} | {{guide:vitals.speed@Phantasm Guard#2}} | {{guide:vitals.speed@Phantasm Guard#3}} |
| Laser range | 700 | 700 | 700 |
| Aggro radius | only when attacked | only when attacked | only when attacked |
| Heals the leader, each, per second (hull only) | 30 | 45 | 60 |
| Credits | {{guide:spoils.pay.credits@Phantasm Guard#1}} | {{guide:spoils.pay.credits@Phantasm Guard#2}} | {{guide:spoils.pay.credits@Phantasm Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Phantasm Guard#1}} | {{guide:spoils.pay.thulium@Phantasm Guard#2}} | {{guide:spoils.pay.thulium@Phantasm Guard#3}} |
| Experience (XP) | {{guide:spoils.pay.experience@Phantasm Guard#1}} | {{guide:spoils.pay.experience@Phantasm Guard#2}} | {{guide:spoils.pay.experience@Phantasm Guard#3}} |
| Honor | {{guide:spoils.pay.honor@Phantasm Guard#1}} | {{guide:spoils.pay.honor@Phantasm Guard#2}} | {{guide:spoils.pay.honor@Phantasm Guard#3}} |
| PvE points per kill | 1 | 1 | 1 |

**Drop**: none. The kill pays its Credits, Thulium, XP and Honor only.

<!-- phantasm-members:end -->
