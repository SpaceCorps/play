# Rockets

Rockets are a second weapon beside your lasers: one shot every few seconds that hits far harder than a laser volley. Twelve rockets in four kinds, three tiers each, two more that only Assembly makes, and **one recharge timer of 3 seconds that all of them share**, whichever you fire (the two that only Assembly makes wait a little longer, for their long flight). The Common and Rare rockets are bought with **Credits**; the four Epic rockets are bought with **Thulium**. A [drone formation](/wiki/03-Mechanics/Formations.md) can raise a rocket's damage and make that timer longer or shorter: see [Drone formations and rockets](#drone-formations-and-rockets).

## In one minute

- **Twelve rockets to buy.** Four kinds (Lancet, Rivet, Ember, Scatter), three tiers each. The Common and Rare ones cost Credits, the Epic ones Thulium. Two more rockets, the N.U.K.E. and the N.I.K.E., are made in Assembly.
- **Each rocket rolls its damage.** When you fire it, the game picks a number between the rocket's lowest and highest damage (a Lancet I: 1,700 to 2,100). Your ship, lasers, amps and boosters change nothing, only a drone formation does. The rockets that aliens fire do not roll: they deal a fixed number ([Against the aliens](#against-the-aliens)).
- **Blasts are strongest in the middle.** Ember and Scatter rockets burst and hurt every ship inside the ring: the full number at the centre, half of it at the edge.
- **One timer for all of them.** After any launch you wait 3 seconds before the next one, whichever rocket it is. Only the N.U.K.E. and the N.I.K.E. make you wait longer (4.1 and 4.6 seconds), because they stay in the air that long.
- **Guided or straight.** A guided rocket (Lancet, Ember) needs a target you have selected. A straight one (Rivet, Scatter) flies to your cursor.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Item tree

What Assembly makes needs its technology first; point at an item to see how long it takes to research. The technology tree, the fuel and the boost: [Research](/wiki/03-Mechanics/Research.md).

```tree
Lancet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets

Lancet I -> Lancet II -> Lancet III
Rivet I -> Rivet II -> Rivet III
Ember I -> Ember II -> Ember III
Scatter I -> Scatter II -> Scatter III => N.U.K.E.
```
<!-- item-tree:end -->

## The four kinds

| | Single target: hits one ship | Area blast: bursts, hurts everything close |
| :--- | :--- | :--- |
| **Guided**: locks the target you selected and steers after it | Lancet I, Lancet II, Lancet III | Ember I, Ember II, Ember III |
| **Straight**: flies toward your cursor | Rivet I, Rivet II, Rivet III | Scatter I, Scatter II, Scatter III |

Each kind is a **family**, named after its Common rocket, and the tier is a Roman numeral: **Lancet I**, **Lancet II** and **Lancet III** are the Common, Rare and Epic guided single-target rockets, and the Rivet, Ember and Scatter families go the same way. A rocket's code on its tile in the Rockets picker and in the Hangar is its family's three letters and its numeral (LNC II, RVT III, EMB I, SCT II); the two craft-only rockets keep their names and codes (N.U.K.E., NUK; N.I.K.E., NIK).

- **Guided** rockets need a selected target inside their **lock range** when they leave. They steer after it at a limited turn rate, so a fast ship far away can outrun a cheap one. If the target dies, leaves or reaches a safe zone, the rocket keeps flying straight and does not pick another.
- **Straight** rockets need no target, and ignore the one you have selected: they always fly toward your **cursor**, at the point under it in the flight view. **Click a straight rocket's slot to arm it** (the slot gets a white frame and a crosshair, and your mouse cursor turns into a crosshair over space), then **click in space**: the rocket flies toward the point you clicked and your ship stays where it is. Esc, a right click or the same slot again lets go. If the rockets are still recharging, the click only tells you so and the rocket stays armed. The number keys and **Fire Rocket** fire at once toward the last point the cursor had in the flight view; before the cursor has been there, they fly the way your ship **points**. They fly straight, so a ship crossing at speed can sidestep them.
- A **single target** rocket hits the first ship it may hit (a guided one only its target). An **area blast** bursts beside the first ship it meets, at the point you aimed it, or where its flight ends, and hurts every ship inside its **blast radius**: full damage at the centre, half of it at the edge. The ring the blast draws on the map is its exact reach.
- **Asteroids.** A rocket fired at an [asteroid](/wiki/03-Mechanics/Asteroid-Mining.md) flies to it, and the first asteroid in the way of any rocket stops it and takes the hit instead of the ship behind it ([Cover](/wiki/03-Mechanics/Asteroid-Mining.md#cover)). The twelve rockets of the Shop and the N.U.K.E. can break one; the N.I.K.E. cannot be fired at one and flies over them. Your lasers hurt an asteroid too, but only at 5% of what they do to a ship: the rocket is the tool for the job.

## The twelve rockets

Every rocket has **its own damage, rolled when you fire it**: anywhere from its lowest to its highest number, and the table shows both and the average. It does not depend on your ship, your lasers and their amps, your boosters, your ammo or your drones, and a rocket never crits. Only a **drone formation** changes it: the table here gives the damage with no formation (see [Drone formations and rockets](#drone-formations-and-rockets)). A single-target rocket deals the damage it rolled to the ship it hits; a blast rolls once and deals that to **every ship inside it**, the whole number at the centre and half of it at the edge. *Shield penetration* is taken off your target's absorbance for that hit (a ship's absorbance is the share of a hit its shields take, see [Shield Mechanics](/wiki/03-Mechanics/Shields.md#shield-penetration)): a Lancet III's 35% leaves the shields of an 80% ship 45% of the hit and sends the other 55% to the hull. A blast has none.

| Name | Kind | Rarity | Damage | Average | Shield penetration | Blast radius | Lock range | Range | Speed | Price | Carry at most |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **Lancet I** | Guided, single target | Common | 1,700–2,100 | 1,900 | 10% | – | 700 | 1,040 | 520 | 500 Credits | 5,000 |
| **Lancet II** | Guided, single target | Rare | 3,500–4,200 | 3,850 | 25% | – | 1,000 | 1,584 | 660 | 800 Credits | 2,000 |
| **Lancet III** | Guided, single target | Epic | 5,200–6,200 | 5,700 | 35% | – | 1,300 | 2,296 | 820 | 5 Thulium | 500 |
| **Rivet I** | Straight, single target | Common | 2,200–2,700 | 2,450 | 5% | – | – | 1,080 | 900 | 500 Credits | 5,000 |
| **Rivet II** | Straight, single target | Rare | 4,500–5,250 | 4,875 | 25% | – | – | 1,120 | 700 | 800 Credits | 2,000 |
| **Rivet III** | Straight, single target | Epic | 7,000–8,000 | 7,500 | 35% | – | – | 1,100 | 500 | 5 Thulium | 500 |
| **Ember I** | Guided, area blast | Common | 1,200–1,400 | 1,300 | – | 170 | 700 | 1,000 | 500 | 500 Credits | 5,000 |
| **Ember II** | Guided, area blast | Rare | 2,400–2,900 | 2,650 | – | 230 | 920 | 1,500 | 600 | 800 Credits | 2,000 |
| **Ember III** | Guided, area blast | Epic | 3,500–4,500 | 4,000 | – | 300 | 1,150 | 2,030 | 700 | 5 Thulium | 500 |
| **Scatter I** | Straight, area blast | Common | 1,500–1,750 | 1,625 | – | 210 | – | 1,088 | 640 | 500 Credits | 5,000 |
| **Scatter II** | Straight, area blast | Rare | 3,000–3,500 | 3,250 | – | 290 | – | 1,080 | 540 | 800 Credits | 2,000 |
| **Scatter III** | Straight, area blast | Epic | 4,500–5,500 | 5,000 | – | 400 | – | 1,092 | 420 | 5 Thulium | 500 |

The dearer the tier, the harder a rocket hits, the farther it reaches, the more shield penetration it has and the fewer you can carry; the dear ones also give the most damage for what they cost. A straight rocket deals a quarter to a third more than the guided rocket of its tier and kind for the same price (23 to 32% on average), because you have to aim it. A blast deals about two thirds of the single-target rocket of its tier and kind (66 to 70% on average: an Ember against a Lancet, a Scatter against a Rivet), to every ship it covers. Damage in a blast is full at its centre and falls in a straight line to **half of it at the edge**: a ship whose hull is halfway out takes 75%, and one whose hull is outside the ring takes nothing. On average a launch deals the middle of its range, 89 to 94% of its top number, and the table that counts rockets below uses that.

## What they cost

A Common rocket costs 500 Credits, a Rare one 800 Credits and an Epic one 5 Thulium, in every kind. Fired on every timer, that is 10,000 Credits a minute for a Common rocket, 16,000 for a Rare one and 100 Thulium for an Epic one, against the 900 Credits a minute that an Ostirion's three lasers burn at x1. A full stack is 5,000 Common rockets (2,500,000 Credits), 2,000 Rare ones (1,600,000 Credits) or 500 Epic ones (2,500 Thulium): you buy as many as you like up to that, and the *carry at most* of a rocket is the only limit on how many you hold. Rockets weigh nothing: they take no room in the Transport Cache. A rocket every 3 seconds is only twenty a minute, so a rocket is the burst on top of your lasers: the cheap ones for the weak aliens, the dear ones for the big fights. What you have listed on the [Auction](/wiki/03-Mechanics/Auction.md#limits) and the lots you lead there count toward that limit when you buy or bid on a rocket.

The Shop lists the rockets one kind at a time, each under its name, the Common rocket first and the Epic one last; the Hangar, the Transport Cache and the Rockets picker use the same order.

## Against the aliens

The rockets it takes to kill one alien, one kind of rocket after the other, every rocket rolling the average of its range (Alpha; Beta and Gamma aliens are 1.5 and 2 times as strong). A blast counts as the ship it bursts beside takes it, a little short of the centre (87 to 93% of the centre damage). An alien's shield takes 80% of a hit, less the rocket's shield penetration. At the lowest roll a kill takes up to 15% more rockets than the table says (a Lancet I needs 48 for a Goombah, not 43), at the best roll up to 13% fewer (39). A Rivet II, a Lancet III and a Rivet III kill a Phantasm in one hit at any roll; a Rivet I needs two on a roll of 2,600 or more, and three below that.

| Rockets to kill | Seeker (1,600) | Phantasm (5,200) | Bulwark (26,000) | Goombah (80,000) | Crystalys (416,000) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Lancet I** | 1 | 3 | 14 | 43 | 219 |
| **Lancet II** | 1 | 2 | 7 | 19 | 109 |
| **Lancet III** | 1 | 1 | 5 | 11 | 73 |
| **Rivet I** | 1 | 3 | 11 | 33 | 170 |
| **Rivet II** | 1 | 1 | 6 | 15 | 86 |
| **Rivet III** | 1 | 1 | 4 | 8 | 56 |
| **Ember I** | 2 | 5 | 24 | 71 | 369 |
| **Ember II** | 1 | 3 | 12 | 34 | 177 |
| **Ember III** | 1 | 2 | 8 | 23 | 116 |
| **Scatter I** | 2 | 4 | 18 | 56 | 287 |
| **Scatter II** | 1 | 2 | 9 | 27 | 141 |
| **Scatter III** | 1 | 2 | 6 | 18 | 90 |

- The **Common** single-target rockets kill a Seeker in one hit at any roll and a Phantasm in three (a Lancet I needs a fourth on its lowest roll); they are the everyday rockets of the first sectors. The **Rare** ones are for the Bulwark and the Goombah: seven Lancet II rockets take a Bulwark in about 20 seconds of timer. The **Epic** single-target ones kill a Goombah in eight (Rivet III) to eleven (Lancet III). The blasts are worth their price when several aliens are close together: a Scatter III bursting over a pack of five Phantasms (all within 250 units of the one you aimed at) deals about 21,000 damage across the pack in one cast.
- A kill by rockets alone is a real spend, not a way to get rich: a single-target rocket costs between 15% (a Rivet II on a Phantasm) and 95% (a Lancet I on a Crystalys) of what the kill pays (Credits, and Thulium at 200 Credits each), and the weak blasts on the strong aliens cost more than the kill pays (an Ember I on a Bulwark: 120%). Killing the **Crystalys** with one kind alone takes 56 to 369 rockets and nearly three minutes of timer; a full stack of 500 Epic rockets is enough for four to eight of them. The strongest alien needs a plan: your lasers on x2 ammo, a mid-tier rocket every 3 seconds from the first second, and the big rockets below as the burst.
- The pay of a kill is the same however it was made (see [the Crystalys](/wiki/04-Aliens/Crystalys.md) for the biggest), so a rocket kill is worth it when it saves you time and costs less than it pays.
- **Aliens fire rockets too.** The Pirate Boss and the Dormant Force and Pulses of the [swarms](/wiki/05-Swarms/Swarms.md) and the Siege Wardens of the [clans](/wiki/03-Mechanics/Clans.md#clan-wardens) launch straight Rivet rockets at the pilot who attacked them, on timers of their own (5 seconds for the swarms, 8 to 24 for the Siege Wardens) that your formation does not change. **An alien's rocket does not roll and does not use the ranges above**: it deals a fixed 2,500 (Rivet I), 5,000 (Rivet II) or 7,500 (Rivet III), more in Beta and Gamma, where aliens are 1.5 and 2 times as strong (a Clan Warden's rocket is the same in every world). A ship that keeps moving sidesteps them. The swarms' bosses also drop rockets in their boxes.

## The craft-only rockets

Two rockets are not in the Shop. **Assembly** makes them, and they follow every rule below (the shared timer, safe zones, your company). They roll between **90% and 100%** of their top number, a narrower band than the twelve's, so what they destroy in one hit below holds at the lowest roll too. Both are straight rockets: they fly toward the point under your cursor, like every straight rocket (the game sends the cursor's direction whatever you have selected; only an old 0.4.3 client, which sends no direction, has the server fly them at the selected target, else the point under its cursor, else the way the ship points).

| Name | Kind | Rarity | Damage | Shield penetration | Blast radius | Range | Speed | Carry at most | Made from |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **N.U.K.E.** | Straight, area blast | Legendary | 45,000–50,000 | – | 900 | 1,200 | 300 | 10 | 1 N.U.K.E. a craft: 150,000 Credits, 3,000 Thulium, 6 Scatter III, 4 Power Core, 10 Reinforced Hull Plate, 40 Ship Fragment, 80 Cataclysite |
| **N.I.K.E.** | Straight, single target | Mythical | 67,500–75,000 | 35% | – | 4,050 | 900 | 20 | 5 N.I.K.E. a craft: 100,000 Credits, 1,500 Thulium, 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite |

- **N.U.K.E.**: the biggest blast in the game. A blast of 900 units, twice the reach of the Scatter III's 400 and five times its area: 45,000 to 50,000 to every ship in it at the centre, falling to half that, 22,500 to 25,000, at the edge. It is slow (four seconds in the air). One N.U.K.E. wipes out every Seeker and Phantasm in its whole blast and a Bulwark within 830 units of the burst (934 at the best roll), nearly all of it; it takes more than half of a Goombah and a ninth of a Crystalys. Against pilots it is the biggest hit there is: see the rules below. The ring on the map is its exact reach.
- **N.I.K.E.**: a single-target rocket like a Rivet I, with 67,500 to 75,000 damage and a shield penetration of 35%: **it hits the first ship it touches and is spent on it.** It is also the rocket that makes [Dark Matter](/wiki/03-Mechanics/Black-Hole.md): fired at the black hole in the middle of Danger Sector 4, it is swallowed when it crosses the event horizon, and the hole gives back Dark Matter. It flies 4,050 units in 4.5 seconds: fire it from anywhere between the rim of the radiation and 4,380 units from the centre. From farther out it falls short and is wasted. Five N.I.K.E.s make about ten Dark Matter.
- **The catch.** A N.I.K.E. that meets a ship on its way, a rival waiting on the line or anything else it may hurt, hits it for 67,500 to 75,000 and is gone: the black hole gets nothing, and neither do you. Nothing else roams inside the hole's ring for it to hit by accident (aliens and company pilots keep out of it): only pilots who went in for Dark Matter, or are waiting for you at the rim. It flies through your own company, ships in a safe zone and ships you may not hurt yet. If you leave the map after firing it, it flies on without hurting anyone and still makes your Dark Matter.
- Assembly won't start a craft that would leave you holding more than the *carry at most* of a rocket, counting what you have queued.

## Firing

1. Buy rockets in the Shop (the **Rockets** category), up to the *carry at most* of each: Credits for the Common and Rare ones, Thulium for the Epic ones.
2. Open **Rockets** above the hotbar, and drag the ones you want onto slots. The picker shows a column per kind and a row per tier, with what you carry on each. Under them is a row of its own, **Special · craft only**, for the N.U.K.E. and the N.I.K.E. (a small hammer marks the one you carry none of).
3. Press the slot's key. Clicking the slot of a **guided** rocket fires it at your selected target; clicking a **straight** rocket's slot arms it, and your next click in space fires it there. The **Fire Rocket** key (`R` by default, rebindable in Settings › Controls) fires the rocket you fired last, or the first one on the bar.
4. A pie sweeps over **every** rocket slot for the 3 seconds until the next launch (4.1 after a N.U.K.E., 4.6 after a N.I.K.E.), with the seconds left in the middle. A press before then only tells you the rockets are recharging (a press in the last tenth of a second still fires). A drone formation can make the wait anything from 2.19 to 4.05 seconds (see below).

Hover a rocket slot to see its numbers (its lowest and highest damage; the Shop and the Hangar say the same) and, in the world, its lock ring (green when the selected target is in range) or its line and blast circle. A rocket locked on **you** flashes the edge of your screen red.

The **N.U.K.E.** draws its blast on the map before you fire (the circle of 900 units at the aimed point) and, when it goes off, a white flash over the view, a ring that runs out to the exact reach in about a second and stays for two more, a cloud that rises like a mushroom, and a shake of the camera that is stronger the nearer you are. **Reduce screen shaking** removes the shake, and **Reduce Motion** shortens the flash to a third of a second at less than half its light (both are in Settings, under Graphics); a lower particle quality thins the cloud and drops the sparks, never the flash or the ring. The **N.I.K.E.** is aimed like a Rivet I, by the line from your ship to the cursor, and the game never refuses it for being far from the black hole or on a map without one: where it goes is yours to judge. Its card says **Black hole: Makes Dark Matter** beside its damage. It leaves a violet trail with sparks winding round it; a ship it meets takes the hit like from any rocket, and when it crosses the horizon instead the hole flares.

## Drone formations and rockets

A worn [drone formation](/wiki/03-Mechanics/Formations.md) is the one thing that changes a rocket. Every damage figure on this page is for a ship with no formation.

- **Damage.** The rocket bonus of Ballista (+55%), Bodkin (+29%) and Asterism (+24%) multiplies the damage of all 14 rockets, the N.U.K.E. and the N.I.K.E. included. Testudo's all-damage price counts on rockets, and Culler's damage to aliens counts on a rocket that hits an alien. All the factors on one rocket together stop at ×1.59. The bonus counts against an [asteroid](/wiki/03-Mechanics/Asteroid-Mining.md#breaking-one) just as against a ship, and the asteroid's armour comes off after it.
- **Reload.** Asterism makes the shared timer 35% longer (4.05 seconds), Cordon 11% longer (3.33) and Redoubt 27% shorter (2.19), but never shorter than the rocket's flight plus a moment. Under Redoubt the quick rockets (Lancet I, Rivet I and II, Ember I, Scatter I and II) wait the 2.19 seconds, a Rivet III waits 2.3, a Lancet III 2.9 and an Ember III the full 3; the N.U.K.E. and the N.I.K.E. wait 4.1 and 4.6 seconds whatever you wear. The wait is set when you fire, so changing formation afterwards does not shorten it, and the pie over the rocket slots follows it.
- **The limits of the big two hold.** With the best formation a N.I.K.E. hits for up to 116,250, which a fresh Paragon (128,000) survives, and a N.U.K.E. for up to 77,500, which a Goombah (80,000) survives.
- **Evasion.** Asterism's 7% evasion gives a direct rocket that hits you a 7% chance to do no damage at all, and a floating "Miss" shows over your ship; an area blast has no aim and is never dodged.
- **Penetration.** Gemini and Stiletto add their points to the shield penetration of a direct rocket (a blast has none), with no cap: a Lancet III with a Stiletto is 51%. A laser hit adds them to its ammo's and its amps' the same way ([Lasers & Ammo](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)).

## Rules

- You need **no laser fitted** to fire a rocket, and your lasers do not change what it deals or how far it reaches: a guided rocket locks a target within its own lock range, a straight one flies its own distance. With no laser fitted the Hangar's Range tile shows a dash, and only your rockets fire.
- One rocket is used per launch, whether it hits or not.
- Rockets follow the rules of lasers: nothing inside a **safe zone** is hurt, no pilot is hurt before the **Peace Protocol** ends or where a sector forbids PvP, and **your own company and your own group are never hurt** by your rockets, direct or blast.
- Launching a rocket ends your own safe-zone protection at once. It is a shot: it also ends your own **cloak**, and the cloaking CPU then recharges for a minute, as after any end of a cloak. Cloaked or not, a launch keeps you from cloaking for the 10 seconds after it (see [Extras](/wiki/06-Items/Extras.md)).
- A ship that is **cloaked** or inside the **3 seconds of its EMP** cannot be locked on: a guided rocket is refused, and one already flying at it loses its lock and flies straight on. A straight single-target rocket flies through such a ship. An **area blast** needs no lock, so it hurts the ships it covers, cloaked or not, and it ends a cloak (see [Extras](/wiki/06-Items/Extras.md)).
- **Nothing caps what a rocket does to a pilot.** Another pilot's ship takes the full damage: the shield first (its absorbance less the rocket's shield penetration), then the hull. The small ships do not last. On the stock shield cores (Light, 45% absorbance) a N.I.K.E. destroys a fresh Protos, Kitefin or Ostirion in one hit at any roll (a Paragon loses 47 to 53% of its hull, a Wraith about a fifth), and a N.U.K.E. destroys a Protos anywhere in its blast, a Kitefin within about 50 units of the burst (220 at the best roll) and nothing bigger in one blast. Two Lancet III rockets or two Rivet III rockets destroy a Protos at any roll; a Wraith takes between 45 and 70 of them. The Peace Protocol, the safe zones and your company are what stand between a pilot and a rocket. These figures are for a ship with no formation; a rocket formation raises them by up to 55% (see [Drone formations and rockets](#drone-formations-and-rockets)).
- Only a rocket's **direct hit** claims an alien (see [Combat](/wiki/03-Mechanics/Combat.md)); a blast's edge can hurt a claimed alien without stealing it. Every alien a blast hurts, a sleeping one too, turns on you, as it does for a laser hit (a Seeker or a Goombah, which only fight back, included); one the blast misses stays asleep.
- The timer is yours: it survives a jump, a reconnect, a ship swap and a destroyed ship.

The twelve rockets of the first table are bought (Credits for the Common and Rare ones, Thulium for the Epic ones); the N.U.K.E. and the N.I.K.E. are crafted.

See also: [Lasers & Ammo](/wiki/06-Items/Lasers.md), [Combat](/wiki/03-Mechanics/Combat.md), [The Black Hole](/wiki/03-Mechanics/Black-Hole.md).
