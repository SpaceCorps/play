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
- **Comes back**: {{guide:vitals.respawn@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} after the leader is destroyed, in the same sector
- **Announced**: The pilots of the sector are told when the leader appears and when it is destroyed. These are System lines: they show in the chat's **System** tab, with an unread count, and not in **Global** or **Local**. The kill feed names the pilot credited with the kill.

<!-- goombah-glance:end -->

## The members

- **Boss Goombah**: a larger Goombah, in the swarm's tint and with its name over it, with a hull, a shield and a laser volley of its own (the numbers are below). It is passive: it roams until a pilot hits it, then goes after that pilot and fires at it, and the ships of its swarm that are close join in. Its weapon's range and its speed are those of a Goombah, and it never mends its hull by itself. Its [three steps](#the-leaders-three-steps) and a [special ability](/wiki/03-Mechanics/Special-Abilities.md) can change that.
- **Goombah Guard**: a smaller Goombah in the swarm's tint. Guards keep close to the boss, join the fight when a swarm ship near them is hit, and each one that is near the boss heals its hull. A guard mends its own hull after a rest, as a Goombah does.

## How the fight goes

- **Bring a group of the strongest ships.** Three level 8 pilots with x2 ammo destroy it in about a minute and a quarter in Alpha, losing at most one ship; two of them need x4 ammo, and pilots of lower levels do not deal enough damage to win.
- **Shoot the boss, not the guards.** A guard falls in seconds, but a new one comes as often as the *At a glance* list says, and what the guards heal is a small part of what a group deals: leaving them alone costs a little time, chasing them costs more.
- **Beta and Gamma are harder.** The swarms of those worlds are stronger ([Worlds](/wiki/05-Swarms/Swarms.md#the-worlds)), so they need more pilots or better ammo.
- **Watch the sector.** `x-4` is a PvP sector in Alpha, and `x-3` and `x-4` are in Beta and Gamma ([Worlds](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): a rival can join the fight or wait for the box. Keep a ship of the group on watch.
- **The boss comes back** after the time in the *At a glance* list, at full strength, in the same sector, and its guards come one after the other.

## The leader's three steps {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Its fight has three steps ([how they work](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); each one happens once.

- **At the start**: Takes 50% of every hit for 6 s.
- **Under two thirds**: Its damage is multiplied by ×1.5 and its speed by ×1.25 for 10 s.
- **Under a third**: Mends 25% of its hull and shield (a burst of damage breaks it), and its Goombah Guards mend it ×2 as fast meanwhile.

<!-- mob-ladder:end -->

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
| Hull | {{guide:vitals.hull@Boss Goombah#1}} | {{guide:vitals.hull@Boss Goombah#2}} | {{guide:vitals.hull@Boss Goombah#3}} |
| Shield | {{guide:vitals.shield@Boss Goombah#1}} | {{guide:vitals.shield@Boss Goombah#2}} | {{guide:vitals.shield@Boss Goombah#3}} |
| Laser damage (a volley a second) | {{guide:vitals.dps@Boss Goombah#1}} | {{guide:vitals.dps@Boss Goombah#2}} | {{guide:vitals.dps@Boss Goombah#3}} |
| Speed | {{guide:vitals.speed@Boss Goombah#1}} | {{guide:vitals.speed@Boss Goombah#2}} | {{guide:vitals.speed@Boss Goombah#3}} |
| Laser range | 800 | 800 | 800 |
| Aggro radius | only when attacked | only when attacked | only when attacked |
| Credits | {{guide:spoils.pay.credits@Boss Goombah#1}} | {{guide:spoils.pay.credits@Boss Goombah#2}} | {{guide:spoils.pay.credits@Boss Goombah#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Goombah#1}} | {{guide:spoils.pay.thulium@Boss Goombah#2}} | {{guide:spoils.pay.thulium@Boss Goombah#3}} |
| Experience (XP) | {{guide:spoils.pay.experience@Boss Goombah#1}} | {{guide:spoils.pay.experience@Boss Goombah#2}} | {{guide:spoils.pay.experience@Boss Goombah#3}} |
| Honor | {{guide:spoils.pay.honor@Boss Goombah#1}} | {{guide:spoils.pay.honor@Boss Goombah#2}} | {{guide:spoils.pay.honor@Boss Goombah#3}} |
| PvE points per kill | 14 | 14 | 14 |

**Drop**: one box, for the pilot who dealt the most damage.

| Item |
| :--- |
| {{guide:spoils.box@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} |

### Goombah Guard

Built from the Goombah at 20% of its hull, shield and damage; its speed and range are the ship's own.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | {{guide:vitals.hull@Goombah Guard#1}} | {{guide:vitals.hull@Goombah Guard#2}} | {{guide:vitals.hull@Goombah Guard#3}} |
| Shield | {{guide:vitals.shield@Goombah Guard#1}} | {{guide:vitals.shield@Goombah Guard#2}} | {{guide:vitals.shield@Goombah Guard#3}} |
| Laser damage (a volley a second) | {{guide:vitals.dps@Goombah Guard#1}} | {{guide:vitals.dps@Goombah Guard#2}} | {{guide:vitals.dps@Goombah Guard#3}} |
| Speed | {{guide:vitals.speed@Goombah Guard#1}} | {{guide:vitals.speed@Goombah Guard#2}} | {{guide:vitals.speed@Goombah Guard#3}} |
| Laser range | 800 | 800 | 800 |
| Aggro radius | only when attacked | only when attacked | only when attacked |
| Heals the leader, each, per second (hull only) | 110 | 165 | 220 |
| Credits | {{guide:spoils.pay.credits@Goombah Guard#1}} | {{guide:spoils.pay.credits@Goombah Guard#2}} | {{guide:spoils.pay.credits@Goombah Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Goombah Guard#1}} | {{guide:spoils.pay.thulium@Goombah Guard#2}} | {{guide:spoils.pay.thulium@Goombah Guard#3}} |
| Experience (XP) | {{guide:spoils.pay.experience@Goombah Guard#1}} | {{guide:spoils.pay.experience@Goombah Guard#2}} | {{guide:spoils.pay.experience@Goombah Guard#3}} |
| Honor | {{guide:spoils.pay.honor@Goombah Guard#1}} | {{guide:spoils.pay.honor@Goombah Guard#2}} | {{guide:spoils.pay.honor@Goombah Guard#3}} |
| PvE points per kill | 3 | 3 | 3 |

**Drop**: none. The kill pays its Credits, Thulium, XP and Honor only.

<!-- goombah-members:end -->
