# Dormant Swamp

<!-- wiki-search: swamp; dormant swamp; base; turret; turrets; nike turret; laser turret; inert mass; unwakened; the unwakened; slumbering void; void; dormant lance; ds-4 -->

Long ago an advanced civilisation lived in the middle of the galaxy. It built in purple-black crystal, with violet seams that glow, and for a reason nobody knows it collapsed. The **Dormant Swamp** is its outpost, in the top-left corner of `DS-4`. From season day 11 it stirs: guns in the middle fire on every ship they see, **Inert Masses** guard it, and in the very middle sleeps **the Unwakened**. You can fly under cloak up to the Unwakened. Since the [Deep Void](/wiki/03-Mechanics/Deep-Void.md) opened, the guns and the Unwakened can be destroyed, and each world's first kill of the Unwakened in a season opens that world's Threshold. The base itself cannot be entered, boarded or traded with.

The swamp is also where the [Dormant Swarm](/wiki/05-Swarms/Dormant-Swarm.md) appears from day 11, and **Slumbering Voids** patrol around it. The same Voids come in waves to the [giant excavators](/wiki/03-Mechanics/Giant-Excavator.md#the-slumbering-voids). The sectors are in [Danger Sectors](/wiki/01-General/Danger-Sectors.md).

![Flying in towards the Dormant Swamp: the amber notice ring and, inside it, the red ring of the zone the guns reach](../img/wiki-img/shots/swamp-rings.jpg)

## At a glance

<!-- swamp-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Where**: The top-left corner of `DS-4`: the middle is at 5,000 / 5,000
- **Appears**: From season day 11 until the wipe
- **The zone**: 4,300 units round the middle: the farthest the guns reach
- **The notice**: A ship that crosses the ring 4,800 units from the middle is told by a System line
- **Cloak**: No gun ever sees a cloaked ship, or one inside the window of an EMP
- **The aliens**: 5 Inert Masses stay within 2,400 units of the middle. The Unwakened sleeps in the middle. 2 Slumbering Voids patrol between 4,600 and 6,500 units from the middle.
- **The Dormant Swarm**: It appears at 9,417 / 6,606, 4,700 units from the middle and outside the zone
- **Rocks**: No asteroid lies within 4,900 units of the middle

<!-- swamp-glance:end -->

## The guns

The swamp's turrets fire on the **nearest ship they can see** inside their reach, and at no other: the zone is the circle that the farthest of them reaches. They are no ships, but since the Deep Void opened each of them has hit points: click a gun to fire your lasers at it, and a rocket that bursts near it hurts it too. A destroyed gun stays down until the Unwakened comes back. Their shots are real, and the world scales their damage as it scales every alien's weapon.

<!-- swamp-guns:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Damage of a shot, in each world:

| Gun | Place | Fires every | Reaches (units) | Alpha | Beta | Gamma |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) turret | 5,000 / 4,400 | 2 s | 3,640 | 75,000 | 112,500 | 150,000 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) turret | 5,000 / 4,400 | 5 s | 1,080 | 50,000 | 75,000 | 100,000 |
| Laser turret × 2 | 3,600 / 5,200; 6,400 / 5,200 | 1 s | 2,500 | 45,000–55,000 | 67,500–82,500 | 90,000–110,000 |

- A rocket is fired from 82% of the reach the same rocket has in a pilot's hands, so that it arrives; a laser turret fires once a second, and its damage is rolled in the range shown.
- A N.I.K.E. has 35% shield penetration, taken off a shield's absorbance.
- The turret's N.I.K.E. flies 25% faster and 2× as far as yours: 1,250 units a second, 8,910 units in all, so a ship that runs from it is followed a long way.
- A N.U.K.E. bursts over a radius of 1,013 units, hardest in the middle.
- The turret's N.U.K.E. flies 25% faster and 2× as far as yours: 375 units a second, 2,640 units in all, so a ship that runs from it is followed a long way.

<!-- swamp-guns:end -->

- **Nothing fires from outside the zone,** and inside it a ship is destroyed in seconds: more guns join the closer a ship comes to the middle, and even the best-shielded Wraith does not last. A rocket that is already in the air flies on, though, and the turret's rockets fly faster and farther than yours: running straight away from one does not shake it off.
- **A cloak gets you in.** No turret ever sees a cloaked ship, nor one inside the window of an EMP, at any distance. A blast aimed at a visible ship that bursts next to a cloaked one still hurts it and ends its cloak.
- **They shoot at pilots only,** never at aliens, company pilots or the swarm, and the protection of a ship that has just come back from a destruction holds against them.
- **The notice ring.** A ship that crosses the ring outside the zone is told by a System line: the turrets fire on every ship they see, and something sleeps in the middle. It is told again only when it has left the ring and come back.
- **Getting out.** If you are destroyed there you cannot come back on the spot (a Danger Sector offers only the base and the nearest portal), and if you log in inside the zone you are put outside it. A course you click is bent round the zone, and a toast warns you when the place you click lies inside it.

## The aliens

Three aliens of the lost civilisation live here, each with its own numbers. They are paid like a swarm's boss: **by the damage dealt**, to every pilot who did at least the share given in [Swarms](/wiki/05-Swarms/Swarms.md#the-rules-of-every-swarm), and the box goes to the pilot who dealt the most. Their kills add to your PvE ranking points like a swarm ship's, in proportion to their pay ([Ranks](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points)). The shield of each takes {{guide:vitals.absorbance@Slumbering Void;Inert Mass;The Unwakened}} of every hit while it lasts ([Shields](/wiki/03-Mechanics/Shields.md)).

- **Slumbering Void.** The sleek hunter, the fastest alien in the game (faster than a Storm on Afterburner III). Some patrol the swamp's surroundings, always, and others come in waves to the excavators. It is aggressive, hunts the nearest pilot it can see and never sees a cloaked ship.
- **Inert Mass.** A dead hulk with violet cracks, the size of a small station. They stay within a set distance of the swamp's middle and do not leave it for now. It fires **Dormant Lances**: guided rockets with a very long reach that follow a ship until it cloaks, opens an EMP window, enters a safe ring, jumps or dies. It outruns every ship, so only those breaks help. An asteroid in a Lance's way stops it, and the Lance damages that asteroid by its own damage (nobody is paid for it), so a rock is shelter from a Mass for a few hits only.
- **The Unwakened.** A monolith that sleeps in the swamp's middle, the biggest thing on any map, so slow that it never catches a ship. It fires nothing, but every ship within its aura burns, **cloaked or not**. Since the [Deep Void](/wiki/03-Mechanics/Deep-Void.md) opened it can be destroyed: it is paid by the damage dealt, comes back a day after its death, and each world's first kill of a season opens that world's Threshold. A pilot's **Radiation tech** lowers its burn, to 0.40 of it at level 100.

<!-- swamp-members:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

### Slumbering Void

2 Slumbering Voids patrol between 4,600 and 6,500 units from the middle of the swamp; one that is destroyed comes back {{guide:vitals.respawn@Slumbering Void}} later. The waves of an excavator bring more of the same alien.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | {{guide:vitals.hull@Slumbering Void}} | {{guide:vitals.hull*1.5@Slumbering Void}} | {{guide:vitals.hull*2@Slumbering Void}} |
| Shield | {{guide:vitals.shield@Slumbering Void}} | {{guide:vitals.shield*1.5@Slumbering Void}} | {{guide:vitals.shield*2@Slumbering Void}} |
| Shield absorbance | {{guide:vitals.absorbance@Slumbering Void}} | {{guide:vitals.absorbance@Slumbering Void}} | {{guide:vitals.absorbance@Slumbering Void}} |
| Laser damage (a volley a second) | {{guide:vitals.dps@Slumbering Void}} | {{guide:vitals.dps*1.5@Slumbering Void}} | {{guide:vitals.dps*2@Slumbering Void}} |
| Speed | {{guide:vitals.speed@Slumbering Void}} | {{guide:vitals.speed@Slumbering Void}} | {{guide:vitals.speed@Slumbering Void}} |
| Laser range | 800 | 800 | 800 |
| Aggro radius | {{guide:vitals.aggro@Slumbering Void}} | {{guide:vitals.aggro@Slumbering Void}} | {{guide:vitals.aggro@Slumbering Void}} |
| Credits | {{guide:spoils.pay.credits@Slumbering Void}} | {{guide:spoils.pay.credits*2@Slumbering Void}} | {{guide:spoils.pay.credits*3@Slumbering Void}} |
| Thulium | {{guide:spoils.pay.thulium@Slumbering Void}} | {{guide:spoils.pay.thulium*2@Slumbering Void}} | {{guide:spoils.pay.thulium*3@Slumbering Void}} |
| Experience (XP) | {{guide:spoils.pay.experience@Slumbering Void}} | {{guide:spoils.pay.experience*2@Slumbering Void}} | {{guide:spoils.pay.experience*3@Slumbering Void}} |
| Honor | {{guide:spoils.pay.honor@Slumbering Void}} | {{guide:spoils.pay.honor*2@Slumbering Void}} | {{guide:spoils.pay.honor*3@Slumbering Void}} |
| PvE points per kill | 10 | 10 | 10 |

**Drop**: one box, for the pilot who dealt the most damage.

| Item |
| :--- |
| {{guide:spoils.box@Slumbering Void}} |

### Inert Mass

5 Inert Masses stand within 2,400 units of the middle; one that is destroyed comes back {{guide:vitals.respawn@Inert Mass}} later. Fires a guided [Dormant Lance](/wiki/06-Items/Rockets.md#the-craft-only-rockets) every 6 s at the nearest ship it can see: speed 750, a flight of 5,250 units, 40% penetration.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | {{guide:vitals.hull@Inert Mass}} | {{guide:vitals.hull*1.5@Inert Mass}} | {{guide:vitals.hull*2@Inert Mass}} |
| Shield | {{guide:vitals.shield@Inert Mass}} | {{guide:vitals.shield*1.5@Inert Mass}} | {{guide:vitals.shield*2@Inert Mass}} |
| Shield absorbance | {{guide:vitals.absorbance@Inert Mass}} | {{guide:vitals.absorbance@Inert Mass}} | {{guide:vitals.absorbance@Inert Mass}} |
| Dormant Lance damage, each | {{guide:behaviour.ability:rocket.damageMin@Inert Mass}}–{{guide:behaviour.ability:rocket.damage@Inert Mass}} | {{guide:behaviour.ability:rocket.damageMin*1.5@Inert Mass}}–{{guide:behaviour.ability:rocket.damage*1.5@Inert Mass}} | {{guide:behaviour.ability:rocket.damageMin*2@Inert Mass}}–{{guide:behaviour.ability:rocket.damage*2@Inert Mass}} |
| Speed | {{guide:vitals.speed@Inert Mass}} | {{guide:vitals.speed@Inert Mass}} | {{guide:vitals.speed@Inert Mass}} |
| Rocket range | 5,000 | 5,000 | 5,000 |
| Aggro radius | {{guide:vitals.aggro@Inert Mass}} | {{guide:vitals.aggro@Inert Mass}} | {{guide:vitals.aggro@Inert Mass}} |
| Credits | {{guide:spoils.pay.credits@Inert Mass}} | {{guide:spoils.pay.credits*2@Inert Mass}} | {{guide:spoils.pay.credits*3@Inert Mass}} |
| Thulium | {{guide:spoils.pay.thulium@Inert Mass}} | {{guide:spoils.pay.thulium*2@Inert Mass}} | {{guide:spoils.pay.thulium*3@Inert Mass}} |
| Experience (XP) | {{guide:spoils.pay.experience@Inert Mass}} | {{guide:spoils.pay.experience*2@Inert Mass}} | {{guide:spoils.pay.experience*3@Inert Mass}} |
| Honor | {{guide:spoils.pay.honor@Inert Mass}} | {{guide:spoils.pay.honor*2@Inert Mass}} | {{guide:spoils.pay.honor*3@Inert Mass}} |
| PvE points per kill | 15 | 15 | 15 |

**Drop**: one box, for the pilot who dealt the most damage.

| Item |
| :--- |
| {{guide:spoils.box@Inert Mass}} |

### The Unwakened

There is one, in the middle of the swamp and nowhere else; it comes back {{guide:vitals.respawn@The Unwakened}} after it is destroyed. Since the Deep Void opened it can be destroyed, and it is paid by the damage dealt like the other aliens here.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | {{guide:vitals.hull@The Unwakened}} | {{guide:vitals.hull*1.5@The Unwakened}} | {{guide:vitals.hull*2@The Unwakened}} |
| Shield | {{guide:vitals.shield@The Unwakened}} | {{guide:vitals.shield*1.5@The Unwakened}} | {{guide:vitals.shield*2@The Unwakened}} |
| Shield absorbance | {{guide:vitals.absorbance@The Unwakened}} | {{guide:vitals.absorbance@The Unwakened}} | {{guide:vitals.absorbance@The Unwakened}} |
| Aura damage a second, to every ship inside | {{guide:behaviour.ability:aura.damagePerSecond@The Unwakened}} | {{guide:behaviour.ability:aura.damagePerSecond*1.5@The Unwakened}} | {{guide:behaviour.ability:aura.damagePerSecond*2@The Unwakened}} |
| Aura radius | 700 | 700 | 700 |
| Speed | {{guide:vitals.speed@The Unwakened}} | {{guide:vitals.speed@The Unwakened}} | {{guide:vitals.speed@The Unwakened}} |
| Aggro radius | {{guide:vitals.aggro@The Unwakened}} | {{guide:vitals.aggro@The Unwakened}} | {{guide:vitals.aggro@The Unwakened}} |
| Credits | {{guide:spoils.pay.credits@The Unwakened}} | {{guide:spoils.pay.credits*2@The Unwakened}} | {{guide:spoils.pay.credits*3@The Unwakened}} |
| Thulium | {{guide:spoils.pay.thulium@The Unwakened}} | {{guide:spoils.pay.thulium*2@The Unwakened}} | {{guide:spoils.pay.thulium*3@The Unwakened}} |
| Experience (XP) | {{guide:spoils.pay.experience@The Unwakened}} | {{guide:spoils.pay.experience*2@The Unwakened}} | {{guide:spoils.pay.experience*3@The Unwakened}} |
| Honor | {{guide:spoils.pay.honor@The Unwakened}} | {{guide:spoils.pay.honor*2@The Unwakened}} | {{guide:spoils.pay.honor*3@The Unwakened}} |
| PvE points per kill | 112 | 112 | 112 |

**Drop**: one box, for the pilot who dealt the most damage.

| Item |
| :--- |
| {{guide:spoils.box@The Unwakened}} |

<!-- swamp-members:end -->

## With the Deep Void

What the Deep Void changed here, in short:

- **The Unwakened can be destroyed.** It is no longer immune: it is paid by the damage dealt, like the other aliens here, and comes back a day after its death.
- **The guns can be destroyed.** Each of the three guns (the rocket turret, which fires both the N.I.K.E. and the N.U.K.E., and the two laser turrets) has hit points now, and lasers and rockets hurt them. A destroyed gun stays down until the Unwakened comes back.
- **The first kill opens the Threshold.** Each world's first kill of the Unwakened in a season opens that world's Threshold in the opposite corner of `DS-4`, where the [Deep Void](/wiki/03-Mechanics/Deep-Void.md) begins.

## What to do here

- **The first kill opens the way.** The first kill of the Unwakened in a season opens its world's Threshold, and with it the way to the [Deep Void](/wiki/03-Mechanics/Deep-Void.md); inside the zone the guns destroy a ship in seconds. Outside the zone, the patrolling Voids in a ring round it are the swamp's first line, and the place where a group can fight without the guns.
- **Fight the Voids with penetration.** A Void's large shield takes {{guide:vitals.absorbance@Slumbering Void;Inert Mass;The Unwakened}} of a hit and is nearly beside the point: the hull behind it is small. The more shield penetration your lasers have, the sooner it falls ([Lasers & Ammo](/wiki/06-Items/Lasers.md)).
- **Stay out of the Lances.** An Inert Mass sees a long way and a Lance cannot be outrun: break the hold with a cloak, an EMP, a safe ring or a jump, or leave its reach. A Mass is a long fight even for a large group of the strongest ships.
- **The Dormant Swarm** now appears just outside the zone, so a group can wait for it without the guns. See [Dormant Swarm](/wiki/05-Swarms/Dormant-Swarm.md).

## Where to read more

- [Danger Sectors](/wiki/01-General/Danger-Sectors.md): what changed on day 11.
- [Giant Excavator](/wiki/03-Mechanics/Giant-Excavator.md): the waves of Slumbering Voids and what they guard.
- [Swarms](/wiki/05-Swarms/Swarms.md) and [Dormant Swarm](/wiki/05-Swarms/Dormant-Swarm.md): how a boss kill pays.
- [Rockets](/wiki/06-Items/Rockets.md#the-craft-only-rockets): the N.I.K.E. and the N.U.K.E. the turret fires.
- [Black Hole](/wiki/03-Mechanics/Black-Hole.md): the other danger of `DS-4`.
- [Cargo](/wiki/03-Mechanics/Cargo.md): the boxes the aliens drop.
