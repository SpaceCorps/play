# Pirate Swarm

The Pirate Swarm is a **Pirate Boss** with its **Pirate Scouts**: a huge, slow ship that attacks nobody and answers with rockets, and a pack of faster ships that guard it and heal it. It lives in the sectors between a company's base and its border, where the middle levels of the game are played, and it is a long fight for a group of pilots, not a quick kill.

## At a glance

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Where**: The sectors `x-2` and `x-3` of every company
- **How many**: One in each of those sectors, 6 in each world
- **Appears**: From season day 4 until the wipe (Beta and Gamma: from season day 1)
- **Leader**: Pirate Boss
- **Followers**: Up to 5 × Pirate Scout, a new one every 10 s
- **Followers stay within**: 900 units of the leader
- **Healing**: Each Pirate Scout within 600 units of the leader heals its hull, 40 HP a second in Alpha
- **Leader destroyed**: The followers leave 1 min after the leader is destroyed, unless they are attacking
- **Comes back**: {{guide:vitals.respawn@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} after the leader is destroyed, in the same sector
- **Announced**: The pilots of the sector are told when the leader appears and when it is destroyed. These are System lines: they show in the chat's **System** tab, with an unread count, and not in **Global** or **Local**. The kill feed names the pilot credited with the kill.

<!-- pirate-glance:end -->

## The members

- **Pirate Boss**: a ship built on the Ironclad, at a share of its strength (the numbers are below). It is passive and fires **no lasers**: its one weapon is a **straight rocket** ([Rockets](/wiki/06-Items/Rockets.md); which one depends on the sector, see the table), at the pilot who attacked it, and it keeps roaming while it fires. It never mends its hull by itself. Its [three steps](#the-leaders-three-steps) and a [special ability](/wiki/03-Mechanics/Special-Abilities.md) can change that.
- **Pirate Scout**: a ship built on the Kitefin, at a share of its strength. Scouts attack any pilot who comes near them, stay close to the boss, and each one near the boss heals its hull.

## How the fight goes

- **Shoot the boss, not the scouts.** The scouts heal the boss, but the heal is small next to the boss's hull, and a new scout comes as often as the *At a glance* list says: a group that kills the scouts first never gets ahead of them, and only a very large group can clear them and still takes longer to finish the boss than one that left them alone. The scouts cost you time, they do not decide the fight.
- **Lead the scouts away.** A scout heals only while it is within reach of the boss, so a scout that follows you out of reach heals nothing, and an Ostirion is faster than a scout.
- **Keep moving.** The boss's rocket is straight and unguided: a ship that keeps moving sidesteps it, a ship that stands still is hit.
- **Bring a group.** Three pilots in Ostirions with x2 ammo take `x-2` without losing a ship, though only just, and are destroyed on `x-3` even while the hits are shared; four take it in about three minutes in Alpha. With x4 ammo three take it on `x-3` in about two minutes. Five take it in about two and a half minutes when the hits are shared and in about three when one pilot takes all the fire, and then they lose two ships: a group that lets one pilot take all the fire needs five. In Beta it takes five pilots and in Gamma seven, with the hits shared (the boss is bigger there and its scouts heal more). In Alpha on `x-3` with x2 ammo, one Ostirion alone cannot win it, one Paragon alone cannot either, and two Paragons win it safely. In Beta and Gamma on `x-3`, one Paragon alone is destroyed with x2 and with x4 ammo. The boss answers the first pilot who hit it, so let the sturdiest ship start, and use your abilities (Emergency Repair, Shield Surge: [Abilities](/wiki/03-Mechanics/Abilities.md)) in a fight that long. Pilots who are still level 2 or 3 are too weak for it, even where they fly: keep away until you are stronger.
- **The boss comes back** after the time in the *At a glance* list, in the same sector.

## The leader's three steps {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Its fight has three steps ([how they work](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); each one happens once.

- **At the start**: Fires a fan of 3 rockets, 12 degrees apart, at the first pilot who hit it.
- **Under two thirds**: Calls 5 more Pirate Scouts at once, at most 10 alive. They pay nothing and leave after 45 s.
- **Under a third**: Flies at ×1.8 speed to the nearest gate for 10 s, then turns back on the pilots.

<!-- mob-ladder:end -->

## Rewards and drops

The Pirate Boss pays for the fight it is: a minute of fighting it pays more than a minute of fighting a Goombah. The credit is split by damage among the pilots who fought it ([how a boss kill pays](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Its box is for the pilot who dealt the most damage and can hold a **Reinforced Hull Plate**, rockets and ammo. Its box is worth a little under half of what the kill itself pays. The scouts pay a small amount and drop nothing.

## The numbers

The numbers of the swarm's ships in the three worlds ([Worlds](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss

Built from the Ironclad at 50% of its hull, shield and damage; its speed and range are the ship's own. Fires a straight rocket every 5 s: [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) on `x-2`, [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) on `x-3`.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | {{guide:vitals.hull@Pirate Boss#1}} | {{guide:vitals.hull@Pirate Boss#2}} | {{guide:vitals.hull@Pirate Boss#3}} |
| Shield | {{guide:vitals.shield@Pirate Boss#1}} | {{guide:vitals.shield@Pirate Boss#2}} | {{guide:vitals.shield@Pirate Boss#3}} |
| Laser damage (a volley a second) | none | none | none |
| Speed | {{guide:vitals.speed@Pirate Boss#1}} | {{guide:vitals.speed@Pirate Boss#2}} | {{guide:vitals.speed@Pirate Boss#3}} |
| Laser range | – | – | – |
| Aggro radius | only when attacked | only when attacked | only when attacked |
| Rocket damage, at most | {{guide:behaviour.ability:rocket.damage@Pirate Boss#1}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#2}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#3}} |
| Credits | {{guide:spoils.pay.credits@Pirate Boss#1}} | {{guide:spoils.pay.credits@Pirate Boss#2}} | {{guide:spoils.pay.credits@Pirate Boss#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Boss#1}} | {{guide:spoils.pay.thulium@Pirate Boss#2}} | {{guide:spoils.pay.thulium@Pirate Boss#3}} |
| Experience (XP) | {{guide:spoils.pay.experience@Pirate Boss#1}} | {{guide:spoils.pay.experience@Pirate Boss#2}} | {{guide:spoils.pay.experience@Pirate Boss#3}} |
| Honor | {{guide:spoils.pay.honor@Pirate Boss#1}} | {{guide:spoils.pay.honor@Pirate Boss#2}} | {{guide:spoils.pay.honor@Pirate Boss#3}} |
| PvE points per kill | 15 | 15 | 15 |

**Drop**: one box, for the pilot who dealt the most damage.

| Item |
| :--- |
| {{guide:spoils.box@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} |

### Pirate Scout

Built from the Kitefin at 50% of its hull and 113% of its laser damage; its speed and range are the ship's own.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | {{guide:vitals.hull@Pirate Scout#1}} | {{guide:vitals.hull@Pirate Scout#2}} | {{guide:vitals.hull@Pirate Scout#3}} |
| Shield | {{guide:vitals.shield@Pirate Scout#1}} | {{guide:vitals.shield@Pirate Scout#2}} | {{guide:vitals.shield@Pirate Scout#3}} |
| Laser damage (a volley a second) | {{guide:vitals.dps@Pirate Scout#1}} | {{guide:vitals.dps@Pirate Scout#2}} | {{guide:vitals.dps@Pirate Scout#3}} |
| Speed | {{guide:vitals.speed@Pirate Scout#1}} | {{guide:vitals.speed@Pirate Scout#2}} | {{guide:vitals.speed@Pirate Scout#3}} |
| Laser range | 700 | 700 | 700 |
| Aggro radius | {{guide:vitals.aggro@Pirate Scout#1}} | {{guide:vitals.aggro@Pirate Scout#2}} | {{guide:vitals.aggro@Pirate Scout#3}} |
| Heals the leader, each, per second (hull only) | 40 | 60 | 80 |
| Credits | {{guide:spoils.pay.credits@Pirate Scout#1}} | {{guide:spoils.pay.credits@Pirate Scout#2}} | {{guide:spoils.pay.credits@Pirate Scout#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Scout#1}} | {{guide:spoils.pay.thulium@Pirate Scout#2}} | {{guide:spoils.pay.thulium@Pirate Scout#3}} |
| Experience (XP) | {{guide:spoils.pay.experience@Pirate Scout#1}} | {{guide:spoils.pay.experience@Pirate Scout#2}} | {{guide:spoils.pay.experience@Pirate Scout#3}} |
| Honor | {{guide:spoils.pay.honor@Pirate Scout#1}} | {{guide:spoils.pay.honor@Pirate Scout#2}} | {{guide:spoils.pay.honor@Pirate Scout#3}} |
| PvE points per kill | 4 | 4 | 4 |

**Drop**: none. The kill pays its Credits, Thulium, XP and Honor only.

<!-- pirate-members:end -->
