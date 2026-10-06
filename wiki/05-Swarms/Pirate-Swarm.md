# Pirate Swarm

The Pirate Swarm is a **Pirate Boss** with its **Pirate Scouts**: a huge, slow ship that attacks nobody and answers with rockets, and a pack of faster ships that guard it and heal it. It lives in the sectors between a company's base and its border, where the middle levels of the game are played, and it is a long fight for a group of pilots, not a quick kill.

## At a glance

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Where**: The sectors `x-2` and `x-3` of every company
- **How many**: One in each of those sectors, 6 in each world
- **Appears**: From season day 4 until the wipe
- **Leader**: Pirate Boss
- **Followers**: Up to 5 × Pirate Scout, a new one every 10 s
- **Followers stay within**: 900 units of the leader
- **Healing**: Each Pirate Scout within 600 units of the leader heals its hull, 40 HP a second in Alpha
- **Leader destroyed**: The followers leave 1 min after the leader is destroyed, unless they are attacking
- **Comes back**: 2 min after the leader is destroyed, in the same sector
- **Announced**: The pilots of the sector are told when the leader appears and when it is destroyed. These are System lines: they show in the chat's **System** tab, with an unread count, and not in **Global** or **Local**. The kill feed names the pilot credited with the kill.

<!-- pirate-glance:end -->

## The members

- **Pirate Boss**: a ship built on the Ironclad, at a share of its strength (the numbers are below). It is passive and fires **no lasers**: its one weapon is a **straight rocket** ([Rockets](/wiki/06-Items/Rockets.md); which one depends on the sector, see the table), at the pilot who attacked it, and it keeps roaming while it fires. It never mends its hull by itself.
- **Pirate Scout**: a ship built on the Kitefin, at a share of its strength. Scouts attack any pilot who comes near them, stay close to the boss, and each one near the boss heals its hull.

## How the fight goes

- **Shoot the boss, not the scouts.** The scouts heal the boss, but the heal is small next to the boss's hull, and a new scout comes as often as the *At a glance* list says: a group that kills the scouts first never gets ahead of them, and only a very large group can clear them and still takes longer to finish the boss than one that left them alone. The scouts cost you time, they do not decide the fight.
- **Lead the scouts away.** A scout heals only while it is within reach of the boss, so a scout that follows you out of reach heals nothing, and an Ostirion is faster than a scout.
- **Keep moving.** The boss's rocket is straight and unguided: a ship that keeps moving sidesteps it, a ship that stands still is hit.
- **Bring a group.** Three pilots in Ostirions with x2 ammo can take it in about five minutes in Alpha; one Ostirion alone cannot, and one Paragon alone can. The boss answers the first pilot who hit it, so let the sturdiest ship start, and use your abilities (Emergency Repair, Shield Surge: [Abilities](/wiki/03-Mechanics/Abilities.md)) in a fight that long. Pilots who are still level 2 or 3 are too weak for it, even where they fly: keep away until you are stronger.
- **The boss comes back** after the time in the *At a glance* list, in the same sector.

## Rewards and drops

The Pirate Boss pays for the fight it is: a minute of fighting it pays more than a minute of fighting a Goombah. The credit is split by damage among the pilots who fought it ([how a boss kill pays](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Its box is for the pilot who dealt the most damage and can hold a **Reinforced Hull Plate**, rockets and ammo. The scouts pay a small amount and drop nothing.

## The numbers

The numbers of the swarm's ships in the three worlds ([Worlds](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss

Built from the Ironclad at 50% of its hull, shield and damage; its speed and range are the ship's own. Fires a straight rocket every 5 s: [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) on `x-2`, [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) on `x-3`.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | 300,000 | 450,000 | 600,000 |
| Shield | 50,100 | 75,150 | 100,200 |
| Laser damage (a volley a second) | none | none | none |
| Speed | 92 | 92 | 92 |
| Laser range | – | – | – |
| Aggro radius | only when attacked | only when attacked | only when attacked |
| Rocket damage, at most | 2,500 (Rivet I) / 5,000 (Rivet II) | 3,750 (Rivet I) / 7,500 (Rivet II) | 5,000 (Rivet I) / 10,000 (Rivet II) |
| Credits | 145,000 | 290,000 | 435,000 |
| Thulium | 725 | 1,450 | 2,175 |
| Experience (XP) | 29,000 | 58,000 | 87,000 |
| Honor | 232 | 464 | 696 |
| PvE points per kill | 15 | 15 | 15 |

**Drop**: one box, for the pilot who dealt the most damage.

| Item | Chance | Amount |
| :--- | ---: | ---: |
| Reinforced Hull Plate | 50% | 1 |
| One of the 8 [rockets](/wiki/06-Items/Rockets.md) bought with Credits, picked at random | 100% | 5–10 |
| One of Advanced Plasma and Siphon Battery, picked at random | 100% | 500–1,000 |

### Pirate Scout

Built from the Kitefin at 50% of its hull, shield and damage; its speed and range are the ship's own.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | 12,000 | 18,000 | 24,000 |
| Shield | 9,818 | 14,727 | 19,636 |
| Laser damage (a volley a second) | 98 | 147 | 196 |
| Speed | 175 | 175 | 175 |
| Laser range | 700 | 700 | 700 |
| Aggro radius | 700 | 700 | 700 |
| Heals the leader, each, per second (hull only) | 40 | 60 | 80 |
| Credits | 1,000 | 2,000 | 3,000 |
| Thulium | 4 | 8 | 12 |
| Experience (XP) | 100 | 200 | 300 |
| Honor | 2 | 4 | 6 |
| PvE points per kill | 4 | 4 | 4 |

**Drop**: none. The kill pays its Credits, Thulium, XP and Honor only.

<!-- pirate-members:end -->
