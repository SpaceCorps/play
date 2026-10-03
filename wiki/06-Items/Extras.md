# Extras

Extras are the gadgets in a ship's **extra slots** (three on every ship, per configuration). You switch one on from the hotbar's Extras picker or from a hotbar slot you gave it. They only work from the configuration you fly: fit one in the other configuration and it waits until you swap.

| Extra | What it does | Uses | Price |
| :---- | :----------- | :--- | :---- |
| **Repair Drone I to IV** | Repairs your hull, 1.5%, 2.25%, 3.5% and 5% of the maximum a second | endless | 5,000 / 15,000 / 35,000 credits, 2,000 Thulium |
| **Cloaking CPU S** | Hides your ship | 10 | 5,000 Thulium |
| **Cloaking CPU M** | Hides your ship | 25 | 11,250 Thulium |
| **Cloaking CPU L** | Hides your ship | 50 | 20,000 Thulium |
| **EMP Charge** | For 3 seconds nobody can target you, every lock on you breaks, and every cloak near you ends | 1 | 500 Thulium |

The Cloaking CPUs and the EMP Charge are sold in the Shop only. They cannot be fused, and nothing gives them away.

## Repair Drones

Switch a Repair Drone on (REP) and it mends the hull until it is full. It starts only after 10 seconds without a hit, and any hit switches it off. With several fitted, the best one works. The rates are in [Combat](/wiki/03-Mechanics/Combat.md).

## Cloaking CPU

Press the CLK slot to cloak. **One press is one use**, whatever the pack, and you can see the uses left on the slot and in the Hangar. A cloak has **no time limit**: it stays on until you switch it off or something breaks it.

- **Who cannot see you.** Pilots of other companies and aliens do not see your ship at all: it is not on their screen or their target list, and nobody can lock on to it. Company pilots of other companies ignore it too.
- **The radar dot.** Every other pilot on the map, your own company excepted, sees a plain **red dot** on the minimap where you are, so they know somebody cloaked is around. The dot has no name, ship, company or id and cannot be clicked or targeted; hovering it says only "Something is cloaked here". It is round, inside a ring (ships on the minimap are squares), and the ring breathes slowly, or stands still if you set Reduce Motion. The server refreshes it about twice a second and your game moves it smoothly in between. It says that someone is there and where, not who: a pilot who saw you cloak can follow the dot, and a **rocket's blast** aimed at it still finds you.
- **Who can.** You see your own ship, faint, with an outline. Pilots of your company see you as a pale ghost; clan mates of other companies do not, because a clan takes anyone who applies. Nobody can target the ghost, not even your company.
- **You cannot cloak** inside a safe zone, while the CPU recharges, or within **10 seconds** of taking a hit or firing a shot.
- **What ends it.** Pressing the slot again, your first volley or rocket (it lands, and you are seen), entering a safe zone, the CPU leaving the configuration you fly, an **EMP going off within 1,500 units** of you, whoever fired it (your own company's too, but not a groupmate's), and the area blast of a rocket that hits you. Time does not, collecting cargo does not (a box you take is gone for everyone, so they learn that something was within reach of that spot, not who), abilities do not, and the black hole's radiation hurts a cloaked ship but does not end its cloak. Logging out or dying ends it, because a ship that is not flown is not cloaked.
- **Recharge.** After a cloak ends, however it ended, the CPU recharges for **60 seconds**. The recharge belongs to you, not to the ship: it goes on if you jump through a portal, log out or die. Every press still costs a use.
- **Aliens** that were after you lose you. Your kill claims are released when you cloak.
- **Rockets.** Nobody can lock a guided rocket on you and a straight single-target rocket flies through you. An **area blast** still hurts a ship it covers and ends its cloak, and the pilots who can see the ship's place are shown it before the damage number appears. Launching a rocket is a shot: it ends your own cloak like a volley does (the CPU then recharges for the 60 seconds above) and, cloaked or not, keeps you from cloaking for 10 seconds after it.
- **The black hole** swallows a cloaked ship like any other, and the map hears it.
- **What you see.** Your ship turns see-through with a violet dashed outline, and a chip at the top of the screen says "Cloaked" with the uses left (no seconds: there is no timer). The CLK slot shows the uses left; while you are cloaked it glows violet and says ON, and when the cloak ends, however it ended, it shades over and counts the 60 seconds of recharge. A press the server refuses (recharging, a safe zone, a hit or shot in the last 10 seconds) flashes the slot red, and a message tells you why. An ally shows as a pale ghost with a ghost mark before its name, and a pilot who cloaks near you vanishes in a ripple. Drag CLK from the hotbar's Extras onto a slot to use it, like REP.
- **Uses** are saved with the CPU. Logging out, dying or restarting the game does not give any back, and an activation you cancel is still spent. When a pack's last use goes, it is used up and its slot is refilled from a spare of the same CPU in your inventory, if you own one.
- **Several CPUs** in one configuration do not add up. The one with the fewest uses left is used first.

The S, M and L behave the same: the bigger packs are only cheaper per use (500, 450 and 400 Thulium).

## EMP Charge

Press the EMP slot in a fight. For **3 seconds** nobody can lock on to you, and **everyone who was locked on to you loses the lock** at once, wherever they are: pilots, aliens and company pilots. A pilot whose lock breaks is told "Lock lost: target used an EMP". Someone who tries to lock on in those 3 seconds is refused.

- **It is not invulnerability.** It stops what needs a lock: lasers, guided rockets, and the touch of a straight single-target rocket, which flies through you. An **area blast** needs no lock, so it still hurts you if you are inside it, and the black hole is not a shot at all.
- **You can still act.** Firing does not end it. You can cloak (if the cloak's own rules allow it) and use other extras.
- **It ends cloaks near you.** Every ship cloaked within **1,500 units** of you when the pulse goes off is shown at once and its CPU starts its 60 seconds of recharge, whichever company it belongs to, yours included; the ships of your own [group](/wiki/03-Mechanics/Groups.md) are the exception: they keep their cloaks. The pilot is told "Cloak broken: an EMP went off nearby.", sees the ship reappear with the same ripple as any decloak, and the slot starts its recharge. You cannot use an EMP while cloaked yourself.
- **It hides nothing.** Everybody still sees you, with a crackling electric shell for the 3 seconds.
- **You cannot use it** while a safe zone protects you, while cloaked, or within **30 seconds** of the last one. It works everywhere else, including the first days of a season (the Peace Protocol): aliens still hunt then.
- An alien you hit during the 3 seconds does not turn on you until they are over. Your kill claims and the first-hit rules do not change.
- **What you see.** A pulse of bent space races out from the pilot as far as the pulse ends cloaks (1,500 units), everybody in range sees it, and a crackling electric shell surrounds it for the 3 seconds, with a ring round your own ship and a chip at the top of the screen that count the time. The target ring of everybody who had you selected breaks apart, with a short zap. The EMP slot shows the charges you own, lights blue while the shell is up, and shades over while it recharges.
- **One charge, one use.** The slot is refilled from your inventory when you own more. The **30 seconds** of recharge are not saved: logging out or jumping through a portal clears them, and the next pulse costs a charge.
