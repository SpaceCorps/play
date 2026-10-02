# The Black Hole

In the exact middle of Danger Sector 4 (`DS-4`, the centre of the PvP zone), a black hole hangs in the dark. It is the same in every world (Alpha, Beta and Gamma), on every day of the season, the Peace Protocol included. It takes what comes too close, and it gives back one thing: [Dark Matter](#dark-matter), for a N.I.K.E. rocket fired into it.

## The Rings

Distances are from the centre of the sector, in map units. The sector is 32,000 by 18,000 units.

| Ring | Distance | What happens |
| :--- | ---: | :--- |
| **Radiation** | 4,000 | Your ship takes damage every second, a share of its total maximum HP. The closer, the more. |
| **Pull** | 3,000 | The black hole pulls your ship toward the centre, harder the closer you are. A ship that is not flying is carried. |
| **Point of no return** | about 1,200 to 2,600 | Where the pull equals your ship's speed. Inside it, even at full power, you are drawn in. It depends on your speed. |
| **Event horizon** | 300 | Any ship that reaches it is destroyed at once, whatever its hull and shield. |

The portals of Danger Sector 4 and the lanes between them all pass well outside the radiation, so you never meet it by accident on the way through.

## Radiation

The damage is a **percentage of your ship's total maximum HP** (hull plus shield) every second, so every ship class lasts exactly as long at a given distance: a Protos and a Wraith at 2,000 units both burn through a full ship in 50 seconds.

| Distance | Damage a second | A full ship lasts |
| ---: | ---: | ---: |
| 4,000 | 0.3 % | 333 s |
| 3,500 | 0.55 % | 182 s |
| 3,000 | 0.8 % | 125 s |
| 2,000 | 2 % | 50 s |
| 1,200 | 5 % | 20 s |
| 700 | 11 % | 9 s |
| 300 | 24 % | 4 s |

Between two rows the damage rises in a straight line. In hit points a second, for the stock builds:

| Ship | Total max HP | At 3,500 | At 3,000 | At 2,000 | At 1,200 | At 700 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Protos | 30,000 | 165 | 240 | 600 | 1,500 | 3,300 |
| Kitefin | 46,000 | 253 | 368 | 920 | 2,300 | 5,060 |
| Ostirion | 82,500 | 454 | 660 | 1,650 | 4,125 | 9,075 |
| Paragon | 162,500 | 894 | 1,300 | 3,250 | 8,125 | 17,875 |
| Wraith | 372,000 | 2,046 | 2,976 | 7,440 | 18,600 | 40,920 |
| Ironclad | 673,200 | 3,703 | 5,386 | 13,464 | 33,660 | 74,052 |

- The **shield takes it first**, then the hull. It is not a hit: the shield's absorbance does not come into it, and it cannot be dodged.
- Radiation counts as **damage taken**: your shield does not recharge, a Repair Drone stops ("Repairs interrupted: radiation.") and cannot be started, and a safe zone would not protect you until 5 seconds after the last dose.
- Boosters and upgrades change how big your total is, not how long you last: the damage is a share of it.
- Nothing makes a ship immune. Radiation is not a hit, so nothing soaks it up; but the abilities go on in it: a Shield Surge keeps restoring your shield and an Emergency Repair keeps healing your hull for their ten seconds (they are not the natural repairs the dose stops). A cloak does not hide the ship from it.

## The Pull

Inside 3,000 units the black hole pulls every ship toward the centre, and the pull only grows the closer you are. It starts gently at the edge and is already felt 200 units in:

| Distance | Pull (units a second) | A ship that is not flying is carried |
| ---: | ---: | :--- |
| 3,000 | 0 | nothing yet |
| 2,800 | 25 | 25 units in a second |
| 2,300 | 60 | 60 units in a second |
| 1,800 | 120 | 120 units in a second |
| 1,300 | 220 | 220 units in a second |
| 1,000 | 262 | 262 units in a second, and rising |
| 900 | 289 | 289 units in a second, and rising fast |
| 700 | 496 | to the horizon in about a second |
| 300 | 2,829 | the event horizon |

From 3,000 down to 925 units the pull rises in a straight line between two rows; inside 925 it follows a steeper curve (the last three rows are on it). It is a current: it moves your ship, and your engines fight it.

- **A ship that does not fly cannot be still.** If you stop (you reach the place you clicked, or you never gave an order), the black hole carries your ship toward the centre and your order goes with it, so your ship keeps falling however fast its engines could fly. To hold a place you have to keep flying there: hold the mouse on it, and your ship holds where its speed is above the pull, sagging a little between two orders. Two ships that stop to trade fire inside the pull are both carried in.
- **A ship that flies feels a headwind.** Flying straight away from the centre, your ship's speed is cut by the pull where you are: at speed 155 you make 130 units a second at 2,800, 95 at 2,300 and 35 at 1,800, and at 1,500 (a pull of 180) no headway at all.

Your **point of no return** is the distance where the pull equals your speed. A ship with speed 150 has it at 1,650 units; the faster you are, the deeper it lies:

| Ship (stock build) | Speed | Point of no return |
| :--- | ---: | ---: |
| Ironclad | 99 | 1,974 |
| Protos | 155 | 1,627 |
| Kitefin | 184 | 1,480 |
| Ostirion | 208 | 1,362 |
| Paragon | 222 | 1,287 |
| Wraith | 238 | 1,171 |

A ship faster than 272 units a second (a runner build, or a stock Wraith with a running Afterburner) has its point of no return where it always was: at speed 300 it is 885, at 432 it is 747.

Build for speed and you can leave from deeper; load up on heavy shields and you cannot (an Ironclad, the slowest ship, with a Heavy Shield Core in all of its 14 slots flies at 39.1, with its point of no return at about 2,600). Only a burst of speed turns a ship back from just inside its point of no return: a running [Afterburner](/wiki/03-Mechanics/Abilities.md) counts, and moves the point of no return deeper for as long as it runs (ten seconds with one engine, fifteen with two, twenty with three; Afterburner III takes a stock Protos's from 1,627 to 1,105 and a stock Wraith's from 1,171 to 793). Nothing can leave from within about 380 units, even a ship built for speed with every speed stat enchanted to the top and the strongest burst running (an Afterburner III enchanted to the cap, x1.69); an unenchanted ship built for speed (Engine IIIs and Adaptive Core IIs with Plasma Thrusters), with an Afterburner III, leaves from outside 424 at best.

The fall from the point of no return starts slowly: a ship a few units inside it, at full power, is drawn in over twenty seconds or more, then faster and faster. The pull is not flight: it counts for no distance flown.

## The Event Horizon

A ship that reaches 300 units from the centre is destroyed. A ship whose hull runs out under the radiation on the way is destroyed by the radiation instead. Either way:

- It is an ordinary destruction: you choose where to come back (see [Dying and Coming Back](/wiki/01-General/Getting-Started.md)), with a full hull and empty shields, and it costs what a destruction always costs. "On the spot" never puts you back inside the ring: it moves you to the nearest point outside it (4,500 units from the centre) and tells you.
- **No wreck, no crate, no loot**, and no honor lost.
- Your destruction is credited like a PvP kill to the **last enemy pilot who hit your ship in the 15 seconds before it died**: a pilot of another company (where and when PvP is allowed), however small the hit. It is a kill in their statistics and PvP ranking points by your ship type, nothing else. A single shot is enough, and if nobody of another company hit you in those 15 seconds, nobody gets anything.
- Company mates who hit your ship in those 15 seconds still lose the friendly-fire honor, whatever destroyed it.
- Aliens and company pilots never go near it. If one ends up inside anyway it vanishes without loot, reward or claim.

## What You See and Hear

The view is small (about 1,900 by 1,150 units on screen at the default zoom, 4,400 by 2,650 zoomed all the way out), so the black hole's own picture only shows within about three thousand units of it (3,600 zoomed all the way out). From farther off nothing on the screen points to it (look at the minimap or the Star System map, below); the warning on the interface is for when you are near:

- **From far away.** If you turn the camera down to look across the plane, the black hole is drawn where it lies on the screen, from anywhere in the sector, whenever it is in the frame: a black disc with a ring in a glow of accretion light, scaled to stay easy to see (about 2 % of the view's height from the far corner, which is about 18,000 units away), and it grows into its own picture as you close in. Nothing in it moves by itself. With the black hole out of the view there is no marker on the screen for it.
- **Rings on the flight plane.** A violet band glows up to a crisp edge at the radiation's rim (4,000 units), and a thinner amber one marks the edge of the pull (3,000). Inside the pull a **red line** shows *your own* point of no return. It follows your speed, so it moves as your ship gets faster or slower.
- **The gauge**, above the hotbar, appears within a thousand units of the rim and stays while you burn. It shows the radiation in percent of your ship's total HP a second, how long the radiation alone would take to burn through what is left ("Lethal in 31 s", red under ten), a bar of that HP, the pull where you are against your speed, and the distance still to fly to your point of no return, or a flashing warning once you are past it. Hover a row for what it means; the (i) opens a card.
- **The screen edges** glow violet, turning red as the dose climbs, and pulse once a second.
- **The minimap** draws the black hole with its rings as ellipses (the chart stretches with its window), and its tooltip names the radii. The star chart marks the sector with a small black hole.
- **A radiation counter** clicks faster as the dose rises, over the fight. A two-tone warning sounds as you cross the rim and again at your point of no return, and a low rumble is heard from about 6,500 units, lower the closer you are.
- **The picture:** a black disc with a bright ring, an accretion disk of three counter-rotating layers, streaks of matter falling in along the pull (they fall at the pull's own speed, so a ship that does not fly is carried in step with them, and one flying out against the pull sees them stream past), and (from Medium graphics up, with post-processing on) a lens that bends the stars around it. A ship the pull carries burns no engine flame and leaves no wake; one flying out against it burns for its full speed through the current, and its wake streams toward the hole. The camera's tremor grows with the pull, in shares of your ship's speed, is at its set level at your point of no return, and keeps rising to the horizon. A ship the hole is burning gives off violet sparks; one it swallows is drawn toward the centre and stretched thin. The sector's sky is the dark violet-and-green one of `DS-3`.
- **The debris:** rocks and pieces of wrecked hulls circle the black hole and fall in along spirals, from the edge of its pull to the horizon: slowly at first, then faster and faster, sweeping around it and tumbling quicker the closer they get. They glow orange in the disk's light, are stretched into needles as they are torn apart, and are gone before they reach the horizon. There are a few big rocks among them, and some drift above the flight plane so that ships pass under them. They are scenery only: nothing hits them and they hit nothing, and they show only within about four thousand units of the black hole, fading out toward 6,500. The disk's light also falls on your ship when it is near.
- **When you die** the overlay says why: "Swallowed by the black hole" or "Burnt up by radiation", and the Game Log has the line.

Settings help where the hole is heavy or hard on the eyes: **Reduce Motion** stops the disk and the streaks, holds the debris still, and stops the pulsing of the screen edges, and **Reduce screen shaking** stops the camera's tremor near the hole; **Low graphics** leaves out the lens and draws fewer streaks (40, against 100 on Medium and 200 above) and fewer pieces of debris (30, against 80 on Medium and 160 above), burns the ring brighter to make up for it, and draws the far view with one glow fewer. A lower **particle quality** thins the debris the way it thins the rocks in the background.

## Staying Out

- The server steers you: a move order that would take your ship across the ring of radiation (4,200 units from the centre, a little wider than the radiation itself) is flown **around** it, along its edge, instead. Orders that end inside the ring are flown as given; going in is your choice. Routes across the sector cost up to a fifth longer, the lanes between the portals nothing.
- The chat warns you as you cross the edge of the radiation, the edge of the pull and your own point of no return, and again when you are clear.
- If you leave the game in the radiation, outside the pull, you come back on the ring's outer edge, holding position, with the hull you had. If you leave it **inside the pull** (3,000 units), you come back exactly where you left it, with the hull you had, and the fall goes on: logging out is no way out of the black hole.
- An older version of the game does not show the black hole. It still gets the warnings and the steering, and it can still fly into the ring by ordering it.

Drones fly with their ship. Cargo is never laid down inside the ring: a crate that would land there is put on its edge. Dark Matter crates are the one exception.

## Dark Matter

The hole gives back **Dark Matter** for a **N.I.K.E.** rocket that reaches it. A N.I.K.E. is a 75,000-damage rocket that hits the first ship it may hurt and is spent on it; if nothing is in the way it flies to the hole and is used up when it crosses the event horizon. [Assembly](/wiki/05-Items/Rockets.md) makes N.I.K.E.s, five a craft (100,000 Credits, 1,500 Thulium, 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite).

- **Firing.** A N.I.K.E. flies 4,050 units in 4.5 seconds (900 a second) straight at where you aimed it: with no target selected, put the cursor on the black hole (or point your ship at it). It reaches the horizon from anywhere between the rim of the radiation (4,000 units) and 4,380 units from the centre. Farther out it falls short and is wasted. Like every rocket it uses the shared 5-second timer (no laser needs to be fitted); firing it ends your safe-zone protection and your cloak. **A ship on the line takes it instead**: a rival waiting at the rim, or a pilot of another company collecting crates in the way, is hit for 75,000 and the hole gets nothing. Aliens and company pilots never come inside the ring, so a clear line is yours to keep clear; it flies through your own company and through ships that are safe from you. If you leave the map after the shot, it flies on without hurting anyone and still makes your Dark Matter.
- **What comes back.** Each N.I.K.E. that reaches the horizon gives **1, 2 or 3 Dark Matter** (2 on average, so about five N.I.K.E.s make ten), in one or two small crates that appear on the rim of the hole's zone, **3,050 to 3,950 units from the centre**, near the line your shot came in on. The pull ends at 3,000, so the crates and the ships taking them are not pulled, and the radiation there is 0.3 to 0.8 % of a ship's HP a second: a minute in the middle of the band costs a third of your ship. A full ship lasts three minutes there.
- **Whose.** The crates are yours, and your clan's, for **60 seconds** from the shot. After that anyone on the map may take them, and they drift away after **4 minutes**. The Danger Sector is a PvP sector, so expect company. A pilot who logs out after firing still has its crates.
- **How many.** A map holds at most 32 Dark Matter crates; a new one pushes out the oldest of them, and never another kind of crate. The [Resource Magnet](/wiki/03-Mechanics/Cargo.md) adds nothing to Dark Matter.
- **What you see.** When a N.I.K.E. crosses the horizon it is stretched into the hole, space ripples out from where it went in, and the disk and the photon ring flare for about a second and a half (a third of that, at half the light, under **Reduce Motion**). A moment later the crates come out of the hole and drift to their places on the rim: each is a violet-black orb with a bright rim and sparkles, easy to see from far, and titled **Dark Matter** when you hover it. Yours show the seconds you have left over them, and show on the minimap as a small violet mark, as they do for your clan; other pilots' crates show on the minimap only once their minute is over.
- **What it is for.** Assembly presses 5 Dark Matter with a Velkonite and an Orvium Reinforced Plate into a **Dark Matter Plate**, and [The Forge](/wiki/05-Items/Forge.md) asks for two of them to raise an item from Godly to Rupturing and again from Rupturing to Eternal: ten Dark Matter a step.
