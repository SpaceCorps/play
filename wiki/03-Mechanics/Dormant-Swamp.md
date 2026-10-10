# Dormant Swamp

<!-- wiki-search: swamp; dormant swamp; base; turret; turrets; nike turret; laser turret; inert mass; unwakened; the unwakened; slumbering void; void; dormant lance; ds-4 -->

Long ago an advanced civilisation lived in the middle of the galaxy. It built in purple-black crystal, with violet seams that glow, and for a reason nobody knows it collapsed. The **Dormant Swamp** is its outpost, in the top-left corner of `DS-4`. From season day 11 it stirs: guns in the middle fire on every ship they see, **Inert Masses** guard it, and in the very middle sleeps **the Unwakened**. It is a place pilots are **not meant to visit yet**. You can fly under cloak up to the Unwakened, and nothing else can be done there for now: the base and its guns cannot be hurt, entered, boarded or traded with.

The swamp is also where the [Dormant Swarm](/wiki/05-Swarms/Dormant-Swarm.md) appears from day 11, and **Slumbering Voids** patrol around it. The same Voids come in waves to the [giant excavators](/wiki/03-Mechanics/Giant-Excavator.md#the-slumbering-voids). The sectors are in [Danger Sectors](/wiki/01-General/Danger-Sectors.md).

![Flying in towards the Dormant Swamp: the amber notice ring and, inside it, the red ring of the zone the guns reach](../img/wiki-img/shots/swamp-rings.jpg)

## At a glance

<!-- swamp-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Where**: The top-left corner of `DS-4`: the middle is at 5,000 / 5,000
- **Appears**: From season day 11 until the wipe
- **The zone**: 4,300 units round the middle: the farthest the guns reach, and the place nobody is meant to visit yet
- **The notice**: A ship that crosses the ring 4,800 units from the middle is told by a System line
- **Cloak**: No gun ever sees a cloaked ship, or one inside the window of an EMP
- **The aliens**: 5 Inert Masses stay within 2,400 units of the middle. The Unwakened sleeps in the middle. 2 Slumbering Voids patrol between 4,600 and 6,500 units from the middle.
- **The Dormant Swarm**: It appears at 9,417 / 6,606, 4,700 units from the middle and outside the zone
- **Rocks**: No asteroid lies within 4,900 units of the middle

<!-- swamp-glance:end -->

## The guns

The swamp's turrets fire on the **nearest ship they can see** inside their reach, and at no other: the zone is the circle that the farthest of them reaches. They are not entities of any kind: they have no hit points, they cannot be targeted, and nothing you shoot at them does anything. Their shots are real, and the world scales their damage as it scales every alien's weapon.

<!-- swamp-guns:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Damage of a shot, in each world:

| Gun | Place | Fires every | Reaches (units) | Alpha | Beta | Gamma |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) turret | 5,000 / 4,400 | 2 s | 3,640 | 75,000 | 112,500 | 150,000 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) turret | 5,000 / 4,400 | 5 s | 1,080 | 50,000 | 75,000 | 100,000 |
| Laser turret × 2 | 3,600 / 5,200; 6,400 / 5,200 | 1 s | 2,500 | 45,000–55,000 | 67,500–82,500 | 90,000–110,000 |

- A rocket is fired from 90% of its reach, so that it arrives; a laser turret fires once a second, and its damage is rolled in the range shown.
- A N.I.K.E. has 35% shield penetration, taken off a shield's absorbance.
- A N.U.K.E. bursts over a radius of 900 units, hardest in the middle.

<!-- swamp-guns:end -->

- **Nothing reaches outside the zone,** and inside it a ship is destroyed in seconds: more guns join the closer a ship comes to the middle, and even the best-shielded Wraith does not last.
- **A cloak gets you in.** No turret ever sees a cloaked ship, nor one inside the window of an EMP, at any distance. A blast aimed at a visible ship that bursts next to a cloaked one still hurts it and ends its cloak.
- **They shoot at pilots only,** never at aliens, company pilots or the swarm, and the protection of a ship that has just come back from a destruction holds against them.
- **The notice ring.** A ship that crosses the ring outside the zone is told by a System line: the turrets fire on every ship they see, and something sleeps in the middle. It is told again only when it has left the ring and come back.
- **Getting out.** If you are destroyed there and come back on the spot, or you log in inside the zone, you are put outside it. A course you click is bent round the zone, and a toast warns you when the place you click lies inside it.

## The aliens

Three aliens of the lost civilisation live here, each with its own numbers. They are paid like a swarm's boss: **by the damage dealt**, to every pilot who did at least the share given in [Swarms](/wiki/05-Swarms/Swarms.md#the-rules-of-every-swarm), and the box goes to the pilot who dealt the most. Their kills add to your PvE ranking points like a swarm ship's, in proportion to their pay ([Ranks](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points)). The shield of each takes 80% of every hit while it lasts ([Shields](/wiki/03-Mechanics/Shields.md)).

- **Slumbering Void.** The sleek hunter, the fastest alien in the game (as fast as a Storm on Afterburner III). Some patrol the swamp's surroundings, always, and others come in waves to the excavators. It is aggressive, hunts the nearest pilot it can see and never sees a cloaked ship.
- **Inert Mass.** A dead hulk with violet cracks, the size of a small station. They stay within a set distance of the swamp's middle and do not leave it for now. It fires **Dormant Lances**: guided rockets with a very long reach that follow a ship until it cloaks, opens an EMP window, enters a safe ring, jumps or dies. It outruns every ship, so only those breaks help. An asteroid in a Lance's way stops it, and the Lance damages that asteroid by its own damage (nobody is paid for it), so a rock is shelter from a Mass for a few hits only.
- **The Unwakened.** A monolith that sleeps in the swamp's middle, the biggest thing on any map, so slow that it never catches a ship. It fires nothing, but every ship within its aura burns, **cloaked or not**. It is **immune**: shots and rockets hit and do nothing, the target window shows full bars and the word Immune. A later event will let it be fought; its rewards below are written down and cannot be earned yet.

<!-- swamp-members:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

### Slumbering Void

2 Slumbering Voids patrol between 4,600 and 6,500 units from the middle of the swamp; one that is destroyed comes back 1 h later. The waves of an excavator bring more of the same alien.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | 25,000 | 37,500 | 50,000 |
| Shield | 150,000 | 225,000 | 300,000 |
| Shield absorbance | 80% | 80% | 80% |
| Laser damage (a volley a second) | 3,000 | 4,500 | 6,000 |
| Speed | 400 | 400 | 400 |
| Laser range | 800 | 800 | 800 |
| Aggro radius | 2,500 | 2,500 | 2,500 |
| Credits | 23,000 | 46,000 | 69,000 |
| Thulium | 60 | 120 | 180 |
| Experience (XP) | 3,600 | 7,200 | 10,800 |
| Honor | 16 | 32 | 48 |
| PvE points per kill | 10 | 10 | 10 |

**Drop**: one box, for the pilot who dealt the most damage.

| Item | Chance | Amount |
| :--- | ---: | ---: |
| One of Ultra Core and Experimental Fusion Core, picked at random | 60% | 30–60 |
| One of the 4 Epic [rockets](/wiki/06-Items/Rockets.md), picked at random | 40% | 1–3 |

### Inert Mass

5 Inert Masses stand within 2,400 units of the middle; one that is destroyed comes back 1 h later. Fires a guided [Dormant Lance](/wiki/06-Items/Rockets.md#the-craft-only-rockets) every 6 s at the nearest ship it can see: speed 750, a flight of 5,250 units, 40% penetration.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | 250,000 | 375,000 | 500,000 |
| Shield | 100,000 | 150,000 | 200,000 |
| Shield absorbance | 80% | 80% | 80% |
| Dormant Lance damage, each | 5,000–8,000 | 7,500–12,000 | 10,000–16,000 |
| Speed | 60 | 60 | 60 |
| Rocket range | 5,000 | 5,000 | 5,000 |
| Aggro radius | 5,000 | 5,000 | 5,000 |
| Credits | 125,000 | 250,000 | 375,000 |
| Thulium | 335 | 670 | 1,005 |
| Experience (XP) | 20,200 | 40,400 | 60,600 |
| Honor | 88 | 176 | 264 |
| PvE points per kill | 15 | 15 | 15 |

**Drop**: one box, for the pilot who dealt the most damage.

| Item | Chance | Amount |
| :--- | ---: | ---: |
| Ultra Core and Experimental Fusion Core, shared evenly | 100% | 400–800 in all |
| One of the 4 Epic [rockets](/wiki/06-Items/Rockets.md), picked at random | 100% | 20–40 |
| N.I.K.E. | 5% | 1–2 |
| Dark Matter | 5% | 1–3 |
| Ancient Control Unit | 10% | 1 |
| Power Core | 25% | 1–2 |

### The Unwakened

There is one, in the middle of the swamp and nowhere else; it comes back 24 h after it is destroyed. It is **immune** until a later quest turns the flag off: shots and rockets hit it and do nothing. Its rewards are written down and cannot be earned yet.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hull | 10,000,000 | 15,000,000 | 20,000,000 |
| Shield | 10,000,000 | 15,000,000 | 20,000,000 |
| Shield absorbance | 80% | 80% | 80% |
| Aura damage a second, to every ship inside | 75,000 | 112,500 | 150,000 |
| Aura radius | 700 | 700 | 700 |
| Speed | 10 | 10 | 10 |
| Aggro radius | 3,000 | 3,000 | 3,000 |
| Credits | 7,500,000 | 15,000,000 | 22,500,000 |
| Thulium | 20,000 | 40,000 | 60,000 |
| Experience (XP) | 1,200,000 | 2,400,000 | 3,600,000 |
| Honor | 5,200 | 10,400 | 15,600 |
| PvE points per kill | 112 | 112 | 112 |

**Drop**: one box, for the pilot who dealt the most damage.

| Item | Chance | Amount |
| :--- | ---: | ---: |
| Ultra Core and Experimental Fusion Core, shared evenly | 100% | 10,000–15,000 in all |
| One of the 4 Epic [rockets](/wiki/06-Items/Rockets.md), picked at random | 100% | 500–800 |
| N.I.K.E. | 100% | 20–30 |
| N.U.K.E. | 100% | 5–10 |
| Dark Matter | 100% | 40–60 |
| Ancient Control Unit | 100% | 10–20 |
| Power Core | 100% | 100–200 |

<!-- swamp-members:end -->

## What to do here

- **Look, do not touch.** The swamp is for later. The only content you can reach without a cloak is outside the zone: the patrolling Voids, in a ring round the zone, are the swamp's first line, and the place where a group can fight without the guns.
- **Fight the Voids with penetration.** A Void's large shield takes 80% of a hit and is nearly beside the point: the hull behind it is small. The more shield penetration your lasers have, the sooner it falls ([Lasers & Ammo](/wiki/06-Items/Lasers.md)).
- **Stay out of the Lances.** An Inert Mass sees a long way and a Lance cannot be outrun: break the hold with a cloak, an EMP, a safe ring or a jump, or leave its reach. A Mass is a long fight even for a large group of the strongest ships.
- **The Dormant Swarm** now appears just outside the zone, so a group can wait for it without the guns. See [Dormant Swarm](/wiki/05-Swarms/Dormant-Swarm.md).

## Where to read more

- [Danger Sectors](/wiki/01-General/Danger-Sectors.md): what changed on day 11.
- [Giant Excavator](/wiki/03-Mechanics/Giant-Excavator.md): the waves of Slumbering Voids and what they guard.
- [Swarms](/wiki/05-Swarms/Swarms.md) and [Dormant Swarm](/wiki/05-Swarms/Dormant-Swarm.md): how a boss kill pays.
- [Rockets](/wiki/06-Items/Rockets.md#the-craft-only-rockets): the N.I.K.E. and the N.U.K.E. the turret fires.
- [Black Hole](/wiki/03-Mechanics/Black-Hole.md): the other danger of `DS-4`.
- [Cargo](/wiki/03-Mechanics/Cargo.md): the boxes the aliens drop.
