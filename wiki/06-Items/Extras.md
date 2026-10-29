# Extras

Extras are the gadgets in a ship's **extra slots** (two on the Protos, Kitefin, Ostirion and Nomad, the ships you start with or buy, and three on the Paragon, Ironclad, Wraith and Storm, the ships you craft, per configuration, and 3, 5 or 7 more with the Extra Slots CPUs). You switch one on from the hotbar's Extras picker or from a hotbar slot you gave it. They only work from the configuration you fly: fit one in the other configuration and it waits until you swap.

| Extra | What it does | Uses | Price |
| :---- | :----------- | :--- | :---- |
| **Repair Drone I to IV** | Repairs your hull, 1.5%, 2.25%, 3.5% and 5% of the maximum a second | endless | 5,000 / 15,000 / 35,000 credits, 2,000 Thulium |
| **Cloaking CPU S** | Hides your ship | 10 | 5,000 Thulium |
| **Cloaking CPU M** | Hides your ship | 25 | 11,250 Thulium |
| **Cloaking CPU L** | Hides your ship | 50 | 20,000 Thulium |
| **P.E.T. Station I to III** | Switched ON, it lets 2, 3 or 5 docked [P.E.T.s](/wiki/03-Mechanics/Pets.md#the-station) boost your ship, earn experience and work; OFF, they do none of it | ON / OFF | Assembly, after its research (the item tree below) |
| **Auto-Rocket CPU** | Switched ON, it fires your armed rocket by itself at the target of a fight | ON / OFF | Assembly, after its research (the item tree below) |

The Cloaking CPUs are sold in the Shop only. They cannot be fused, and nothing gives them away. The **EMP Charge** is not an extra any more: since 0.4.21 it is a consumable, carried as a stack like a rocket and fitted in no slot, so it takes none of your extra slots (see [Rockets](/wiki/06-Items/Rockets.md#emp-charge)). The two **Energetic Walls** are not extras any more either: since 0.4.22 they are consumables too, carried as a stack and fitted in no slot (see [Energetic Wall](#energetic-wall)).

A new pilot's **starter kit** already fits two extras in the Protos' two extra slots: a **Base CPU I** (10 uses, a teleport to your company's base) and a **Repair Drone I**. Drag them from the Extras picker of the hotbar onto a slot to use them. Only new pilots get the kit: a pilot who enlisted before 0.4.10 has not got it.

Eight more CPUs are not sold: Assembly makes them once the Skylab's Research Centre has researched them (see [Research](/wiki/03-Mechanics/Research.md)). They are Extra Slots CPU I, II and III, the Jump CPU, Base CPU I and II, the Auto-Repair CPU and the Auto-Rocket CPU, and [the last section](#research-cpus) tells what each does. Like the Cloaking CPU, the Jump CPU and the Base CPUs are for a quiet moment: none of the three starts within 10 seconds of a shot you fire or a hit you take. The two warp CPUs, the Jump CPU and the Base CPUs, are also refused while you carry a quest item ("You can't use a warp CPU while carrying a mission item."): see [Quest items](/wiki/03-Mechanics/Quests.md#quest-items).

Each extra has a short label on its hotbar slot: **REP** for a Repair Drone, **CLK** for a Cloaking CPU and **ARP**, **ARL**, **BSE** and **JMP** for the Auto-Repair, Auto-Rocket, Base and Jump CPUs (the consumables have theirs: **EMP**, and **WAL** for an Energetic Wall). The Extra Slots CPUs have no slot: they install in your Skylab. The three **P.E.T. Station** items are extras like the others, with the label **PET**: fit one, and its slot switches the Station **ON** or **OFF** (a second between two presses) and shows which. While it is ON the docked [P.E.T.s](/wiki/03-Mechanics/Pets.md) count, while it is OFF they do not. The **Auto-Rocket CPU** is switched the same way, ON or OFF. Point at a slot to read what a press does now, or why it cannot.

![The Extras picker of the hotbar: the Repair Drone, the Auto-Repair, Cloaking, Base and Jump CPUs and the P.E.T. Station you have fitted (REP, ARP, CLK, BSE, JMP, PET): click one to use it, or drag it onto a slot](../img/wiki-img/shots/cpu-hotbar.jpg)
![The Consumables picker of the hotbar: the EMP Charge and the Energetic Wall I and II (EMP, WAL), with how many of each you hold: click one to use it, or drag it onto a slot](../img/wiki-img/shots/emp-hotbar.jpg)
![The hotbar with extras on its slots: a Repair Drone, a Cloaking CPU with its uses left, the P.E.T. Station that says ON, the EMP Charge and the Energetic Wall I and II with the number of each you carry](../img/wiki-img/shots/hotbar-slots.jpg)
![The Repair Drone of an extra slot docked to its ship and its wingmen](../img/wiki-img/shots/repair-drones-extra.jpg)
![The Shop's Consumables category: the EMP Charge and the Energetic Wall I with their prices in Thulium, and the Energetic Wall II, which only Assembly makes](../img/wiki-img/shots/shop-consumables.jpg)

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Item tree

What Assembly makes needs its technology first; point at an item to see how long it takes to research. The technology tree, the fuel and the boost: [Research](/wiki/03-Mechanics/Research.md).

```tree
P.E.T. Station I | extra, common | craft 100000 Credits, 2000 Thulium, 300 s | research 10800 s, 10800 science | 25 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md
Cloaking CPU S | extra, common | buy 5000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Repair Drone I | extra, common | buy 5000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone II | extra, common | buy 15000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone III | extra, common | buy 35000 Credits | /wiki/06-Items/Extras.md#repair-drones
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
P.E.T. Station II | extra, uncommon | craft 300000 Credits, 4000 Thulium, 600 s | research 36000 s, 36000 science | 1 P.E.T. Station I, 35 Ship Fragment, 6 Reinforced Hull Plate, 2 Power Core, 4 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md
Cloaking CPU M | extra, uncommon | buy 11250 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 2 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Extras.md#base-cpus
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu
P.E.T. Station III | extra, rare | craft 1100000 Credits, 12000 Thulium, 900 s | research 86400 s, 86400 science | 1 P.E.T. Station II, 60 Ship Fragment, 6 Reinforced Hull Plate, 4 Power Core, 2 Ancient Control Unit, 4 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md
Auto-Rocket CPU | extra, rare | craft 20000 Thulium, 900 s | research 36000 s, 36000 science | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 1 Ancient Control Unit, 8 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-rocket-cpu
Repair Drone IV | extra, rare | buy 2000 Thulium | /wiki/06-Items/Extras.md#repair-drones
Cloaking CPU L | extra, rare | buy 20000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 6 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu

P.E.T. Station I => P.E.T. Station II => P.E.T. Station III
Cloaking CPU S -> Cloaking CPU M -> Cloaking CPU L
Repair Drone I -> Repair Drone II -> Repair Drone III -> Repair Drone IV
Extra Slots CPU I -> Extra Slots CPU II -> Extra Slots CPU III
Base CPU I -> Base CPU II
```
<!-- item-tree:end -->

## Repair Drones

Switch a Repair Drone on (REP) and it mends the hull until it is full. It starts only after 10 seconds without a hit, and any hit switches it off. With several fitted, the best one works. An [Auto-Repair CPU](#auto-repair-cpu) switches it on again for you. The rates are in [Combat](/wiki/03-Mechanics/Combat.md). While it mends, little repair drones fly out of the ship, circle it and beam the hull, one for a Repair Drone I, two for a II, three for a III or IV, and the pilots near you see them; they dock again when the repair stops.

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
- **What you see.** Your ship turns see-through with a violet dashed outline, its drones fading with it, and a chip at the top of the screen says "Cloaked" with the uses left (no seconds: there is no timer). The CLK slot shows the uses left; while you are cloaked it glows violet and says ON, and when the cloak ends, however it ended, it shades over and counts the 60 seconds of recharge. A press the server refuses (recharging, a safe zone, a hit or shot in the last 10 seconds) flashes the slot red, and a message tells you why. An ally shows as a pale ghost with a ghost mark before its name, and a pilot who cloaks near you vanishes in a ripple. Drag CLK from the hotbar's Extras onto a slot to use it, like REP.
- **Uses** are saved with the CPU. Logging out, dying or restarting the game does not give any back, and an activation you cancel is still spent. When a pack's last use goes, it is used up and its slot is refilled from a spare of the same CPU in your inventory, if you own one.
- **Several CPUs** in one configuration do not add up. The one with the fewest uses left is used first.

The S, M and L behave the same: the bigger packs are only cheaper per use (500, 450 and 400 Thulium).

## Energetic Wall

Press the WAL slot and a **wall of plasma** stands **at your cursor**, across the line from your ship to it: a strip 360 units long (about three and a half ship models) and 10 units wide. Its middle is at most **450 units** from the ship's middle: a cursor farther away puts it 450 units out along the line, and a cursor closer than 120 units pushes it out to 120. While the slot is ready, a faint dotted line and a ghost outline show where it will stand. If the game does not know where your cursor is, it stands 220 units ahead of the ship's middle, across its heading. An Energetic Wall is a **consumable**, like the [EMP Charge](/wiki/06-Items/Rockets.md#emp-charge): a stack in your inventory that takes **no slot** on any ship (until 0.4.22 it was an extra). Drag it from the hotbar's **Consumables** onto a slot to use it; the two levels are two entries, so a slot holds one level. It is for hiding behind and for cutting a lane, not for standing in.

- **What it stops.** Every shot that crosses it hits the wall instead, whoever fired it and from whichever side: a laser volley, a rocket, an alien's volley. What stands behind it takes nothing and the wall's hit points take the damage. A rocket's blast that goes off at the wall hurts the ships on its near side and not the ones behind it. Your own shots too: you cannot shoot out through your own wall. The N.I.K.E. and the turrets of the Dormant Swamp fly over it, as they fly over asteroids.
- **What it burns.** Any ship whose hull touches the strip takes **2,500 damage a second**, shield first, your own included, aliens and company pilots too. A ship in a safe zone or under the protection of a respawn is not burnt, and two strips on one ship do not add up.
- **How long it lasts.** A level 1 wall has **30,000 hit points**, a level 2 wall **90,000**. A wall loses a sixtieth of them every second by itself, so one nobody shoots is gone after **60 seconds**. Shots shorten that: a Wraith with twelve Helios Beams on x4 ammo brings a level 1 wall down in about 3.5 seconds.
- **One at a time, one wall a press.** A new wall takes the place of your old one. After a press the item recharges for **90 seconds**; the wait is yours, not the ship's, so dying or logging out does not shorten it. A press uses up **one wall of the level its slot holds**, and only when the wall stands: a press the game refuses (below) uses nothing and starts no wait. With none of that level left it says "No Energetic Wall left." and the other level is never used in its place.
- **Where not.** Not while a safe zone or a respawn protects you, not where the strip would touch a safe zone or a gate, not while cloaked, and not where the middle of the strip would fall off the map. The game says which.
- **Kills.** A ship the wall destroys dies of radiation, and the kill goes to the last enemy pilot who hit it within 15 seconds, if there was one. Whoever put the wall down is credited with nothing it did not shoot itself. An alien the wall destroys pays nothing: no reward, no loot.
- **Aliens do not go round it.** They fly through it and burn, or stand on their side and shoot the wall.
- **What you see.** A strip of blue-white light with bright dashes running along it and a post of light at each end, flaring where a shot lands and flickering when it is nearly spent. A level 2 wall glows yellow instead, with a thicker, brighter core and a stronger glow, but its strip is the same 10 units wide as a level 1 wall's. A thin life bar beside it shortens and turns amber and then red; your slot shows the wall's remaining life as its arc, the wait as its shade and the walls of its level you have left as its number. A wall put down flares in, a wall shot down collapses in sparks, and one whose time ran out fades.
- **Getting it and carrying it.** The Energetic Wall I is sold in the Shop for **250 Thulium** a wall, and you carry up to **20** of it in one stack (what you have listed on the [Auction](/wiki/03-Mechanics/Auction.md) counts). The Energetic Wall II is made in Assembly, **one wall a craft**, for **600 Thulium**, 5 Ship Fragments and a Power Core, once the Research Centre has researched it (6 hours at the normal rate: [Research](/wiki/03-Mechanics/Research.md)); you carry up to **10** of it. Unlike the twelve rockets, of which 1,000 of each carry over by themselves, the walls you carry are lost with the season unless you put them in the Transport Cache, and walls in the cache cannot be used. An Energetic Wall II you made can be sold on the Auction; an Energetic Wall I, which the Shop sells, never.

## CPUs of the Research Centre {#research-cpus}

Two of the CPUs take Dark Matter Plates, like the last tier of every upgrade chain: **Extra Slots CPU III** asks for 4 (plus 2 Ancient Control Units and 6 Orvium Reinforced Plates) and **Base CPU II** for 4 (plus an Ancient Control Unit and 2 Orvium Reinforced Plates), so research the Dark Matter Plate first ([Dark Matter and Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)).

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | Research time | Needs first | Thulium to craft | Crafting time |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 min | – | 12,000 | 5 min |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10 h | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30,000 | 10 min |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1 d | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75,000 | 15 min |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3 h | – | 8,000 | 5 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10 h | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | 20,000 | 10 min |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1 d | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40,000 | 15 min |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6 h | – | 15,000 | 10 min |
| [Energetic Wall II](/wiki/06-Items/Extras.md#energetic-wall) | 6 h | – | 600 | 2 min |
| [Auto-Rocket CPU](/wiki/06-Items/Extras.md#auto-rocket-cpu) | 10 h | – | 20,000 | 15 min |

None of them is sold in the Shop: research the technology, then make the CPU in Assembly. Point at a CPU in its tree to see what Assembly asks for it.

### Extra Slots CPUs

- **What they do.** Extra Slots CPU I, II and III give every ship 3, 5 and 7 more extra slots, so 6, 8 and 10 in all on a ship that has 3 of its own, and 5, 7 and 9 on one that has 2. A higher CPU replaces the one before it: II does not add to I.
- **Installed, not carried.** An Extra Slots CPU is not an item: when you collect it in Assembly it installs itself in your Skylab, for every ship in both configurations, and it takes no slot. It stays through the wipe.
- **In order.** Craft them one after the other: II only when I is installed, III only when II is installed; until then Assembly tells you which one to install first. The three cost 117,000 Thulium in all: 12,000, 30,000 and 75,000.

### Jump CPU

- **What it does.** It jumps your ship to any company sector of your world, your own company's and the other companies' alike, their home sectors included (`M`, `T` and `G`, sectors 1 to 4), for **500 Thulium** a jump. It has no limit on uses: you only pay the Thulium. It never goes to a Danger Sector (`DS`) or a neutral sector (`N`).
- **The jump.** Press the JMP slot, pick the sector on the Star System map and confirm: the ship charges for 5 seconds, then arrives at a gate of that sector, protected as after any gate jump. The CPU cools down for 30 seconds after you arrive.
- **Not in a fight.** It cannot start within 10 seconds of firing or being hit, and a shot or a hit while it charges cancels the jump; nothing is paid then. You cannot jump while cloaked.
- **Not from a neutral sector:** a pilot in a neutral sector, or with no company, cannot use it.
- It may leave a Danger Sector when you are not in a fight.

### Base CPUs

- **What they do.** They teleport your ship to the base of your company, into the safe zone around its station (`M-1`, `T-1` or `G-1`, the sector with Mission Control), free of Thulium. You start them from the BSE slot of the hotbar.
- **Not in a fight.** A charge of 10 seconds, the same for both. It cannot start within 10 seconds of firing or being hit, while you are cloaked or when you are already inside the safe zone of your base, and a shot or a hit while it charges cancels it.

| CPU | Uses | Cooldown |
| :--- | ---: | ---: |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 10 | 10 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 25 | 5 min |

- **Used up, not recharged.** Each use takes one of the CPU's uses, and a CPU with none left is gone: craft a new one. With both fitted, the better one (II) is used first.

### Auto-Repair CPU

- **What it does.** It sends out the Repair Drone fitted in your extra slots by itself, whenever you could have sent it out by hand: your hull is not full, the drone is not already out and 10 seconds have passed since the last hit. There is no hull level to set.
- It takes an extra slot of its own and does nothing without a Repair Drone in an extra slot of the same configuration. It never sends out a Repair Drone in an ability slot (that one is the Emergency Repair button).
- **If you stop the drone by hand,** the CPU leaves it alone until your hull is full again, or until you send the drone out yourself.

### Auto-Rocket CPU

- **What it does.** While it is switched ON and you are in a fight (your lasers are on an alien or an enemy pilot), it fires your armed rocket, the one you fired last, at that target by itself, whenever a press of the Fire Rocket key would work: the rockets' timer is ready and you have one left. The server checks each launch as it checks yours.
- **The switch.** Fit it in an Extras slot and press its ARL slot to switch it ON or OFF. It starts OFF and stays as you left it, also when you sign in again. The slot says ON or OFF and glows when the CPU fires.
- **What it never does.** It never picks a target, never fires at asteroids, never fires from a safe zone or while you are cloaked, and never fires a N.U.K.E. or a N.I.K.E. A rocket you fire yourself always works. With no key, click or mouse move for 3 minutes it waits until you do something.
- **No rockets left.** It tells you once and fires again as soon as you have more.


<!-- research-cpus:end -->
