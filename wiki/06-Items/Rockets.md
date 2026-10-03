# Rockets

Rockets are a second weapon beside your lasers: one shot every few seconds that hits far harder than a laser volley. Twelve rockets in four kinds, three tiers each, two more that only Assembly makes, and **one recharge timer of 5 seconds that all of them share**, whichever you fire. The Common and Rare rockets are bought with **Credits**; the four Epic rockets are bought with **Thulium**.

## The four kinds

| | Single target: hits one ship | Area blast: bursts, hurts everything close |
| :--- | :--- | :--- |
| **Guided**: locks the target you selected and steers after it | Lancet I, Lancet II, Lancet III | Ember I, Ember II, Ember III |
| **Straight**: flies toward your cursor | Rivet I, Rivet II, Rivet III | Scatter I, Scatter II, Scatter III |

Each kind is a **family**, named after its Common rocket, and the tier is a Roman numeral: **Lancet I**, **Lancet II** and **Lancet III** are the Common, Rare and Epic guided single-target rockets, and the Rivet, Ember and Scatter families go the same way. A rocket's code on its tile in the Rockets picker and in the Hangar is its family's three letters and its numeral (LNC II, RVT III, EMB I, SCT II); the two craft-only rockets keep their names and codes (N.U.K.E., NUK; N.I.K.E., NIK).

- **Guided** rockets need a selected target inside their **lock range** when they leave. They steer after it at a limited turn rate, so a fast ship far away can outrun a cheap one. If the target dies, leaves or reaches a safe zone, the rocket keeps flying straight and does not pick another.
- **Straight** rockets need no target, and ignore the one you have selected: they always fly toward your **cursor**, at the point under it in the flight view. **Click a straight rocket's slot to arm it** (the slot gets a white frame and a crosshair, and your mouse cursor turns into a crosshair over space), then **click in space**: the rocket flies toward the point you clicked and your ship stays where it is. Esc, a right click or the same slot again lets go. If the rockets are still recharging, the click only tells you so and the rocket stays armed. The number keys and **Fire Rocket** fire at once toward the last point the cursor had in the flight view; before the cursor has been there, they fly the way your ship **points**. They fly straight, so a ship crossing at speed can sidestep them.
- A **single target** rocket hits the first ship it may hit (a guided one only its target). An **area blast** bursts beside the first ship it meets, at the point you aimed it, or where its flight ends, and hurts every ship inside its **blast radius**: full damage at the centre, less toward the edge. The ring the blast draws on the map is its exact reach.

## The twelve rockets

Every rocket has **its own damage, rolled when you fire it**: between **80% and 100%** of its top number, and the table shows the lowest and the highest. It is the same whoever fires it: it does not depend on your ship, your lasers, your Damage Amps, your boosters, your ammo or your drones, and a rocket never crits. A single-target rocket deals the damage it rolled to the ship it hits; a blast rolls once and deals that to **every ship inside it**, the whole number at the centre and less toward the edge. *Shield penetration* is taken off your target's absorbance for that hit (a ship's absorbance is the share of a hit its shields take, see [Shield Mechanics](/wiki/03-Mechanics/Shields.md#shield-penetration)): a Lancet III's 35% leaves the shields of an 80% ship 45% of the hit and sends the other 55% to the hull. A blast has none.

| Name | Kind | Rarity | Damage | Shield penetration | Blast radius | Lock range | Range | Speed | Price | Carry at most |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **Lancet I** | Guided, single target | Common | 1,600–2,000 | 10% | – | 700 | 1,040 | 520 | 500 Credits | 5,000 |
| **Lancet II** | Guided, single target | Rare | 3,200–4,000 | 25% | – | 1,000 | 1,584 | 660 | 800 Credits | 2,000 |
| **Lancet III** | Guided, single target | Epic | 4,800–6,000 | 35% | – | 1,300 | 2,296 | 820 | 5 Thulium | 500 |
| **Rivet I** | Straight, single target | Common | 2,000–2,500 | 5% | – | – | 1,080 | 900 | 500 Credits | 5,000 |
| **Rivet II** | Straight, single target | Rare | 4,000–5,000 | 25% | – | – | 1,120 | 700 | 800 Credits | 2,000 |
| **Rivet III** | Straight, single target | Epic | 6,000–7,500 | 35% | – | – | 1,100 | 500 | 5 Thulium | 500 |
| **Ember I** | Guided, area blast | Common | 1,120–1,400 | – | 170 | 700 | 1,000 | 500 | 500 Credits | 5,000 |
| **Ember II** | Guided, area blast | Rare | 2,240–2,800 | – | 230 | 920 | 1,500 | 600 | 800 Credits | 2,000 |
| **Ember III** | Guided, area blast | Epic | 3,360–4,200 | – | 300 | 1,150 | 2,030 | 700 | 5 Thulium | 500 |
| **Scatter I** | Straight, area blast | Common | 1,400–1,750 | – | 210 | – | 1,088 | 640 | 500 Credits | 5,000 |
| **Scatter II** | Straight, area blast | Rare | 2,800–3,500 | – | 290 | – | 1,080 | 540 | 800 Credits | 2,000 |
| **Scatter III** | Straight, area blast | Epic | 4,200–5,250 | – | 400 | – | 1,092 | 420 | 5 Thulium | 500 |

The dearer the tier, the harder a rocket hits, the farther it reaches, the more shield penetration it has and the fewer you can carry; the dear ones also give the most damage for what they cost. A straight rocket deals **25% more** than the guided rocket of its tier and kind for the same price, because you have to aim it. A blast deals 70% of the single-target rocket of its tier, to every ship it covers. Damage in a blast is at its centre; it falls to 25 to 35% at the edge. A launch deals 90% of its top number on average, and the table that counts rockets below uses that.

## What they cost

A Common rocket costs 500 Credits, a Rare one 800 Credits and an Epic one 5 Thulium, in every kind. Fired on every timer, that is 6,000 Credits a minute for a Common rocket, 9,600 for a Rare one and 60 Thulium for an Epic one, against the 1,800 Credits a minute that an Ostirion's three lasers burn at x1. A full stack is 5,000 Common rockets (2,500,000 Credits), 2,000 Rare ones (1,600,000 Credits) or 500 Epic ones (2,500 Thulium): you buy as many as you like up to that, and the *carry at most* of a rocket is the only limit on how many you hold. Rockets weigh nothing: they take no room in the Transport Cache. A rocket every 5 seconds is only twelve a minute, so a rocket is the burst on top of your lasers: the cheap ones for the weak aliens, the dear ones for the big fights.

The Shop lists the rockets one kind at a time, each under its name, the Common rocket first and the Epic one last; the Hangar, the Transport Cache and the Rockets picker use the same order.

## Against the aliens

The rockets it takes to kill one alien, one kind of rocket after the other, every rocket rolling the average (Alpha; Beta and Gamma aliens are 1.5 and 2 times as strong). A blast counts as the ship it bursts beside takes it, a little short of the centre. An alien's shield takes 80% of a hit, less the rocket's shield penetration. At the lowest roll a kill takes about 10 to 15% more rockets than the table says (a Lancet I needs 50 for a Goombah, not 45), at the best roll about 10% fewer (40). A Rivet II kills a Phantasm in one hit only on a roll of 89% or more, and needs two below that.

| Rockets to kill | Seeker (1,600) | Phantasm (5,200) | Bulwark (26,000) | Goombah (80,000) | Crystalys (416,000) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Lancet I** | 1 | 3 | 15 | 45 | 232 |
| **Lancet II** | 1 | 2 | 8 | 20 | 116 |
| **Lancet III** | 1 | 1 | 5 | 11 | 78 |
| **Rivet I** | 1 | 3 | 12 | 36 | 185 |
| **Rivet II** | 1 | 1 | 6 | 16 | 93 |
| **Rivet III** | 1 | 1 | 4 | 9 | 62 |
| **Ember I** | 2 | 5 | 25 | 77 | 399 |
| **Ember II** | 1 | 3 | 13 | 37 | 193 |
| **Ember III** | 1 | 2 | 8 | 25 | 128 |
| **Scatter I** | 2 | 4 | 20 | 60 | 311 |
| **Scatter II** | 1 | 2 | 10 | 29 | 151 |
| **Scatter III** | 1 | 2 | 7 | 20 | 100 |

- The **Common** single-target rockets kill a Seeker in one hit at any roll and a Phantasm in three (a Lancet I needs a fourth on its lowest roll); they are the everyday rockets of the first sectors. The **Rare** ones are for the Bulwark and the Goombah: eight Lancet II rockets take a Bulwark in about 35 seconds of timer. The **Epic** ones kill a Phantasm in one hit at any roll and a Goombah in nine to eleven. The blasts are worth their price when several aliens are close together: a Scatter III bursting over a pack of five Phantasms deals about 18,000 damage across the pack in one cast.
- A kill by rockets alone is a real spend, not a way to get rich: for the alien it is meant for, a single-target rocket costs a sixth to five sixths of what the kill pays (Credits, and Thulium at 200 Credits each), and the weak rockets on the strong aliens cost more than the kill pays. Killing the **Crystalys** with one kind alone takes 62 to 399 rockets and at least five minutes of timer; a full stack of 500 Epic rockets is enough for four to eight of them. The strongest alien needs a plan: your lasers on x2 ammo, a mid-tier rocket every 5 seconds from the first second, and the big rockets below as the burst.
- The pay of a kill is the same however it was made (see [the Crystalys](/wiki/04-Aliens/Crystalys.md) for the biggest), so a rocket kill is worth it when it saves you time and costs less than it pays.
- **Aliens fire rockets too.** The Pirate Boss and the Dormant Force and Pulses of the [swarms](/wiki/05-Swarms/Swarms.md) launch straight Rivet rockets at the pilot who attacked them, on the same 5 second timer. A ship that keeps moving sidesteps them. The swarms' bosses also drop rockets in their boxes.

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
4. A pie sweeps over **every** rocket slot for the 5 seconds until the next launch, with the seconds left in the middle. A press before then only tells you the rockets are recharging (a press in the last tenth of a second still fires).

Hover a rocket slot to see its numbers (its lowest and highest damage; the Shop and the Hangar say the same) and, in the world, its lock ring (green when the selected target is in range) or its line and blast circle. A rocket locked on **you** flashes the edge of your screen red.

The **N.U.K.E.** draws its blast on the map before you fire (the circle of 900 units at the aimed point) and, when it goes off, a white flash over the view, a ring that runs out to the exact reach in about a second and stays for two more, a cloud that rises like a mushroom, and a shake of the camera that is stronger the nearer you are. **Reduce screen shaking** removes the shake, and **Reduce Motion** shortens the flash to a third of a second at less than half its light (both are in Settings, under Graphics); a lower particle quality thins the cloud and drops the sparks, never the flash or the ring. The **N.I.K.E.** is aimed like a Rivet I, by the line from your ship to the cursor, and the game never refuses it for being far from the black hole or on a map without one: where it goes is yours to judge. Its card says **Black hole: Makes Dark Matter** beside its damage. It leaves a violet trail with sparks winding round it; a ship it meets takes the hit like from any rocket, and when it crosses the horizon instead the hole flares.

## Rules

- You need **no laser fitted** to fire a rocket, and your lasers do not change what it deals or how far it reaches: a guided rocket locks a target within its own lock range, a straight one flies its own distance. With no laser fitted the Hangar's Range tile shows a dash, and only your rockets fire.
- One rocket is used per launch, whether it hits or not.
- Rockets follow the rules of lasers: nothing inside a **safe zone** is hurt, no pilot is hurt before the **Peace Protocol** ends or where a sector forbids PvP, and **your own company and your own group are never hurt** by your rockets, direct or blast.
- Launching a rocket ends your own safe-zone protection at once. It is a shot: it also ends your own **cloak**, and the cloaking CPU then recharges for a minute, as after any end of a cloak. Cloaked or not, a launch keeps you from cloaking for the 10 seconds after it (see [Extras](/wiki/06-Items/Extras.md)).
- A ship that is **cloaked** or inside the **3 seconds of its EMP** cannot be locked on: a guided rocket is refused, and one already flying at it loses its lock and flies straight on. A straight single-target rocket flies through such a ship. An **area blast** needs no lock, so it hurts the ships it covers, cloaked or not, and it ends a cloak (see [Extras](/wiki/06-Items/Extras.md)).
- **Nothing caps what a rocket does to a pilot.** Another pilot's ship takes the full damage: the shield first (its absorbance less the rocket's shield penetration), then the hull. The small ships do not last. On the stock shield cores (Light, 45% absorbance) a N.I.K.E. destroys a fresh Protos, Kitefin or Ostirion in one hit at any roll (a Paragon loses 47 to 53% of its hull, a Wraith about a fifth), and a N.U.K.E. destroys a Protos anywhere in its blast, a Kitefin within about 50 units of the burst (220 at the best roll) and nothing bigger in one blast. Two Lancet III rockets or two Rivet III rockets destroy a Protos at any roll; a Wraith takes between 48 and 75 of them. The Peace Protocol, the safe zones and your company are what stand between a pilot and a rocket.
- Only a rocket's **direct hit** claims an alien (see [Combat](/wiki/03-Mechanics/Combat.md)); a blast's edge can hurt a claimed alien without stealing it. Every alien a blast hurts, a sleeping one too, turns on you, as it does for a laser hit (a Seeker or a Goombah, which only fight back, included); one the blast misses stays asleep.
- The timer is yours: it survives a jump, a reconnect, a ship swap and a destroyed ship.

The twelve rockets of the first table are bought (Credits for the Common and Rare ones, Thulium for the Epic ones); the N.U.K.E. and the N.I.K.E. are crafted.

See also: [Lasers & Ammo](/wiki/06-Items/Lasers.md), [Combat](/wiki/03-Mechanics/Combat.md), [The Black Hole](/wiki/03-Mechanics/Black-Hole.md).
