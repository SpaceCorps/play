# Extras

Extras are the gadgets in a ship's **extra slots** (three on every ship, per configuration, and more with the Extra Slots CPUs). You switch one on from the hotbar's Extras picker or from a hotbar slot you gave it. They only work from the configuration you fly: fit one in the other configuration and it waits until you swap.

| Extra | What it does | Uses | Price |
| :---- | :----------- | :--- | :---- |
| **Repair Drone I to IV** | Repairs your hull, 1.5%, 2.25%, 3.5% and 5% of the maximum a second | endless | 5,000 / 15,000 / 35,000 credits, 2,000 Thulium |
| **Cloaking CPU S** | Hides your ship | 10 | 5,000 Thulium |
| **Cloaking CPU M** | Hides your ship | 25 | 11,250 Thulium |
| **Cloaking CPU L** | Hides your ship | 50 | 20,000 Thulium |
| **EMP Charge** | For 3 seconds nobody can target you, every lock on you breaks, and every cloak near you ends | 1 | 500 Thulium |

The Cloaking CPUs and the EMP Charge are sold in the Shop only. They cannot be fused, and nothing gives them away.

Seven more CPUs are not sold: Assembly makes them once the Skylab's Research Centre has researched them (see [Research](/wiki/03-Mechanics/Research.md)). They are Extra Slots CPU I, II and III, the Jump CPU, Base CPU I and II, and the Auto-Repair CPU, and [the last section](#research-cpus) tells what each does. Like the Cloaking CPU, the Jump CPU and the Base CPUs are for a quiet moment: none of the three starts within 10 seconds of a shot you fire or a hit you take.

Each extra has a short label on its hotbar slot: **REP** for a Repair Drone, **CLK** for a Cloaking CPU, **EMP** for the EMP Charge and **ARP**, **BSE** and **JMP** for the Auto-Repair, Base and Jump CPUs. The Extra Slots CPUs have no slot: they install in your Skylab. Point at a slot to read what a press does now, or why it cannot.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Item tree {#item-tree}

What Assembly makes needs its technology first; point at an item to see how long it takes to research. The technology tree, the fuel and the boost: [Research](/wiki/03-Mechanics/Research.md).

```tree
Cloaking CPU S | extra, common | buy 5000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Repair Drone I | extra, common | buy 5000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone II | extra, common | buy 15000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone III | extra, common | buy 35000 Credits | /wiki/06-Items/Extras.md#repair-drones
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
EMP Charge | extra, uncommon | buy 500 Thulium | /wiki/06-Items/Extras.md#emp-charge
Cloaking CPU M | extra, uncommon | buy 11250 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 8 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu
Repair Drone IV | extra, rare | buy 2000 Thulium | /wiki/06-Items/Extras.md#repair-drones
Cloaking CPU L | extra, rare | buy 20000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 20 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu

Cloaking CPU S -> Cloaking CPU M -> Cloaking CPU L
Repair Drone I -> Repair Drone II -> Repair Drone III -> Repair Drone IV
Extra Slots CPU I -> Extra Slots CPU II -> Extra Slots CPU III
Base CPU I -> Base CPU II
```
<!-- item-tree:end -->

## Repair Drones

Switch a Repair Drone on (REP) and it mends the hull until it is full. It starts only after 10 seconds without a hit, and any hit switches it off. With several fitted, the best one works. An [Auto-Repair CPU](#auto-repair-cpu) switches it on again for you. The rates are in [Combat](/wiki/03-Mechanics/Combat.md).

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

## CPUs of the Research Centre {#research-cpus}

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | Research time | Needs first | Thulium to craft | Crafting time |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 min | – | 12,000 | 5 min |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10 h | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30,000 | 10 min |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1 d | [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75,000 | 15 min |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3 h | – | 8,000 | 5 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10 h | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 20,000 | 10 min |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1 d | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40,000 | 15 min |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6 h | – | 15,000 | 10 min |

None of them is sold in the Shop: research the technology, then make the CPU in Assembly. Point at a CPU in its tree to see what Assembly asks for it.

### Extra Slots CPUs {#extra-slots-cpus}

- **What they do.** Extra Slots CPU I, II and III give every ship 3, 5 and 7 more extra slots, so 6, 8 and 10 in all with the 3 every ship has. A higher CPU replaces the one before it: II does not add to I.
- **Installed, not carried.** An Extra Slots CPU is not an item: when you collect it in Assembly it installs itself in your Skylab, for every ship in both configurations, and it takes no slot. It stays through the wipe.
- **In order.** Craft them one after the other: II only when I is installed, III only when II is installed; until then Assembly tells you which one to install first. The three cost 117,000 Thulium in all: 12,000, 30,000 and 75,000.

### Jump CPU {#jump-cpu}

- **What it does.** It jumps your ship to any company sector of your world, your own company's and the other companies' alike, their home sectors included (`M`, `T` and `G`, sectors 1 to 4), for **500 Thulium** a jump. It has no limit on uses: you only pay the Thulium. It never goes to a Danger Sector (`DS`) or a neutral sector (`N`).
- **The jump.** Press the JMP slot, pick the sector on the Star System map and confirm: the ship charges for 5 seconds, then arrives at a gate of that sector, protected as after any gate jump. The CPU cools down for 30 seconds after you arrive.
- **Not in a fight.** It cannot start within 10 seconds of firing or being hit, and a shot or a hit while it charges cancels the jump; nothing is paid then. You cannot jump while cloaked.
- **Not from a neutral sector:** a pilot in a neutral sector, or with no company, cannot use it.
- It may leave a Danger Sector when you are not in a fight.

### Base CPUs {#base-cpus}

- **What they do.** They teleport your ship to the base of your company, into the safe zone around its station (`M-1`, `T-1` or `G-1`, the sector with Mission Control), free of Thulium. You start them from the BSE slot of the hotbar.
- **Not in a fight.** A charge of 10 seconds, the same for both. It cannot start within 10 seconds of firing or being hit, while you are cloaked or when you are already inside the safe zone of your base, and a shot or a hit while it charges cancels it.

| CPU | Uses | Cooldown |
| :--- | ---: | ---: |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 10 | 10 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 25 | 5 min |

- **Used up, not recharged.** Each use takes one of the CPU's uses, and a CPU with none left is gone: craft a new one. With both fitted, the better one (II) is used first.

### Auto-Repair CPU {#auto-repair-cpu}

- **What it does.** It sends out the Repair Drone fitted in your extra slots by itself, whenever you could have sent it out by hand: your hull is not full, the drone is not already out and 10 seconds have passed since the last hit. There is no hull level to set.
- It takes an extra slot of its own and does nothing without a Repair Drone in an extra slot of the same configuration. It never sends out a Repair Drone in an ability slot (that one is the Emergency Repair button).
- **If you stop the drone by hand,** the CPU leaves it alone until your hull is full again, or until you send the drone out yourself.


<!-- research-cpus:end -->
