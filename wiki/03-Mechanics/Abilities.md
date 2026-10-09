# Active Ship Abilities

Abilities are the buttons you press in the heat of a fight: a shield that comes back, a burst of speed to get out of range, a repair when your hull is nearly gone. They come from the **shield, engine or Repair Drone** you fit into your ship's **Ability Slots**, and the better that item, the better the ability. They are made for the moment you need them, not for pressing on every cooldown: each one takes about ten seconds and then rests for a minute and a half to two minutes. A few [ship designs](/wiki/03-Mechanics/Ship-Designs.md) have one more, of their own: see [Ship abilities](#ship-abilities).

A new pilot starts with one: the **Repair Drone I** of the starter kit is already fitted in the Protos' ability slot, so the Emergency Repair button (`E`) is there from the first minute. A second Repair Drone I from the kit sits in an extra slot: that one mends the hull slowly by itself and is not an ability (see [Extras](/wiki/06-Items/Extras.md#repair-drones)).

![The Afterburner](../img/wiki-img/shots/afterburner.jpg)
![Emergency Repair: repair drones beam the hull](../img/wiki-img/shots/emergency-repair.jpg)
![Shield Surge: a bubble of shield around the ship and its drones](../img/wiki-img/shots/surge.jpg)

## Ability slots

Every ship has a fixed number of Ability Slots in the Hangar:

- **Protos** (starter): 1 slot
- **Kitefin**: 1 slot
- **Ostirion**: 2 slots
- **Nomad**: 2 slots
- **Paragon**: 3 slots
- **Storm**: 3 slots
- **Ironclad**: 3 slots
- **Wraith**: 3 slots

An ability slot takes a **Shield Core**, an **Engine** or a **Repair Drone**, and each makes its own ability. Drag the item onto the slot. Configuration 1 and configuration 2 have their own slots.

- **Shield Cells and Thrusters do not fit an ability slot.** They are modules of shields, engines and Adaptive Cores.
- **An item in an ability slot adds nothing else.** It gives no shield capacity, recharge, absorbance or speed, and none of a shield's slowdown. The same Heavy Shield Core either sits in a generator slot for its shield at every moment, or in an ability slot for its Surge. You choose.
- A shield or engine that holds cells or thrusters gives them back to your inventory when you drag it onto an ability slot.
- A Repair Drone in an ability slot makes Emergency Repair and does not repair the hull by itself. The slow drone (**REP**) needs a Repair Drone in an extra slot.

## Several modules of one kind

You may fit **several shields, engines or Repair Drones** into the ability slots of one configuration. They are still one ability, one button and one cooldown, but a stronger one:

- **The worst-ranked module sets the base.** Its rank gives the strength and the cooldown. A Heavy Shield Core next to a Light Shield Core behaves as two Rank I modules: a better second module buys the bonus and never a better strength or a shorter cooldown.
- **Every other module adds 50% of the base**, added up, not multiplied. Engines make the Afterburner **last longer**: 10 s, 15 s with two engines, 20 s with three (the speed bonus and the cooldown do not change). Shields make the Shield Surge **restore more**, and Repair Drones make Emergency Repair **heal more**, in the same ten seconds: 100%, 150% and 200% of the total for one, two and three modules.
- **The extra modules cost slots.** A ship with three ability slots can have three of one kind, or one of each, or two and one. A Protos or a Kitefin has a single slot and cannot stack; an Ostirion or a Nomad can have two of one kind.
- Equal ranks are simply that rank. Of two modules of one rank the one with the weaker enchant sets the base.

## The three abilities

### Shield Surge (shields), key `Q`

For ten seconds your ship's shield is **repaired**: the Surge restores a share of your max shield evenly, up to the max and never over it. It is not a barrier and does not change how hits are split; it puts shield back, and what it put back stays. It does not stop when you are hit (the ordinary recharge waits 15 seconds after a hit; the Surge does not). A ship with a full shield gets little from it, so press it when the shield is going. The total is never less than the core's own capacity, so a ship with little shield still gets a real repair (up to its max).

- Refused inside a safe zone's protection, and on a ship with no shield at all, so a misclick doesn't burn it.
- Piercing rockets still partly bypass the shields, as they always did.

### Afterburner (engines), key `W`

Your final speed is multiplied by the rank's bonus for its duration. It does not change turning, targeting or damage taken: it turns time into distance. Use it to leave a fight, to reach a station or gate ring, or to close in on a target that runs. It works anywhere, safe zones included. More engines make it last longer, not faster.

### Emergency Repair (Repair Drones), key `E`

Heals a share of your **max hull evenly over ten seconds**, never above the max. Hits do not interrupt it: it is an emergency ability, and it works under fire, in the black hole's radiation, under a cloak and inside an EMP window. It ends when the time is up or when your ship is destroyed. It does not touch your shield, does not count as a hit, and leaves the slow REP repair as it was. Refused at full hull.

## Ship abilities

Eight of the thirteen [ship designs](/wiki/03-Mechanics/Ship-Designs.md) come with an ability that belongs to the design, not to an item. It takes **no ability slot** and needs nothing fitted: it is there as long as you fly the design. It has a button of its own, the fourth in the hotbar's column, and its key is `F` (you can change it in the settings). It has its own cooldown, kept like the others: swapping configuration, jumping and logging out do not reset it, and a ship that is destroyed starts the next flight with every ability ready.

| Ability | Design | What it does | Lasts | Cooldown |
| :--- | :--- | :--- | ---: | ---: |
| **Blink** | Storm NOTSUM, Ironclad TITANIC | Speed 2,500 (TITANIC: 1,500) toward your move order | 1 s | 120 s |
| **Chameleon** | Storm RECON | Invisible to every other pilot, the minimap too | until it breaks | 60 s |
| **Focus Fire** | Ironclad DUMA | Enemy ships within 1,000 units are forced to attack you | 5 s | 60 s |
| **Venom** | Wraith RAPTOR | 100,000 damage straight to a target's hull | 30 s | 120 s |
| **Diminisher** | Wraith BILLY | You take 75% less damage and deal 25% less | 10 s | 120 s |
| **Heal Pod** | Wraith MENATI | A pod heals friendly ships within 600 units 10,000 + 1% of their max hull a second | 5 s | 120 s |
| **Shield Buff** | Wraith ATARAXIS | Your shield capacity doubles and regenerates 2% of its maximum a second | 10 s | 120 s |

- **Blink.** For 1 second your speed is 2,500 (a TITANIC's is capped at 1,500), toward your move order. You stop where the order ends, and the edge of the map stops you. Then it rests for 120 seconds.
- **Chameleon.** You vanish: no other pilot sees you, on the map or on the minimap, and nobody can lock you. Your own company still sees you, as a ghost. An EMP cannot break it. It ends when you take any damage, fire a laser volley, launch a rocket, collect a box or enter a safe zone, or when you press the button again, and its 60 seconds start when it ends, however it ends. You cannot start it within 10 seconds of a shot or a hit, or inside a safe zone's ring, and not while a Cloaking CPU is on.
- **Focus Fire.** For 5 seconds every enemy pilot and alien within 1,000 units is forced to attack you: a pilot's lock is set on you and cannot be changed, an alien turns on you. Pilots of your group and company, ships inside a safe zone's protection and cloaked ships are left alone, and it is refused inside a safe zone or with no enemy in range. They can still fly where they like.
- **Venom.** Lock a target within your laser range and press: 100,000 damage goes straight to its hull over 30 seconds, evenly, and its shield takes no share. It works on pilots of other companies and on aliens alike, not on your group or company, not on a ship a safe zone protects, and not where a laser lock is refused (the Peace Protocol, a sector without PvP). A ship carries one Venom at a time. Every tick counts as a hit, so the target cannot hide in a safe zone until it ends. Repair, a Heal Pod and a Diminisher on the target cut it, it ends when the target or you die, and the kill and its points are yours.
- **Diminisher.** For 10 seconds every hit you take is cut to a quarter before your shield takes its share, so shield and hull both lose a quarter, and every hit you deal is cut to three quarters: lasers, direct rockets and blasts. A second press does nothing while it runs.
- **Heal Pod.** A pod drops where you are and stays for 5 seconds. Each second it heals every friendly ship within 600 units by 10,000 plus 1% of that ship's maximum hull: you, your group and your company, nobody else, and never above the maximum. Nothing can lock the pod or shoot it, and it goes on healing if you die.
- **Shield Buff.** For 10 seconds your shield capacity is doubled, with the shield you hold doubled too, and the shield regenerates 2% of the doubled maximum each second. When it ends the capacity goes back and the shield goes with it, keeping its share, so the buff never heals you: it is room to be hit in. It is refused on a ship with no shield.

An **EMP** that goes off near you jams the button for 5 seconds: a press is refused and no cooldown starts. An ability that is already running goes on, and a Chameleon stays hidden. The other pilots see these abilities too: a streak behind a Blink, a red ring and lines to the ships a Focus Fire forces, a Chameleon only as a ghost to its own company.

## Ranks

The strength of an ability is a **share of your own ship's number** (max shield, speed, max hull), so it grows with the ship. The rank comes from the item: a better model gives a better ability. An enchanted item adds its enchant bonus to the strength, at most 15%. The table is for one module; the stack is below it.

<!-- abilities:begin -->
<!-- Generated from server/Resources/AbilityConfig.json and the items' stats by scripts/abilities-wiki.sh: don't edit by hand. -->

| Ability | Rank | Item | Strength (one module) | Lasts | Cooldown | Up |
| :--- | :---: | :--- | :--- | --: | --: | --: |
| **Shield Surge** | I | Light Shield Core | restores 30% of your max shield | 10 s | 120 s | 8.3% |
| **Shield Surge** | II | Basic Shield Core | restores 60% of your max shield | 10 s | 105 s | 9.5% |
| **Shield Surge** | III | Heavy Shield Core | restores 100% of your max shield | 10 s | 90 s | 11.1% |
| **Afterburner** | I | Engine I | +30% speed | 10 s | 120 s | 8.3% |
| **Afterburner** | II | Engine II | +45% speed | 10 s | 105 s | 9.5% |
| **Afterburner** | III | Engine III | +60% speed | 10 s | 90 s | 11.1% |
| **Emergency Repair** | I | Repair Drone I | heals 20% of your max hull | 10 s | 120 s | 8.3% |
| **Emergency Repair** | II | Repair Drone II | heals 25% of your max hull | 10 s | 105 s | 9.5% |
| **Emergency Repair** | III | Repair Drone III | heals 32% of your max hull | 10 s | 90 s | 11.1% |
| **Emergency Repair** | IV | Repair Drone IV | heals 40% of your max hull | 10 s | 75 s | 13.3% |

Several modules of a kind in one configuration: the worst-ranked sets the strength and the cooldown above, and every other one adds 50% of it.

| Modules of a kind | Afterburner lasts | Shield Surge restores | Emergency Repair heals |
| :---: | --: | --: | --: |
| 1 | 10 s | 100% | 100% |
| 2 | 15 s | 150% | 150% |
| 3 | 20 s | 200% | 200% |

<!-- abilities:end -->

Rank III shields and engines (the Heavy Shield Core, Engine III) are not sold: you make them in [Assembly](/wiki/06-Items/Overview.md#upgrading-modules) from a Basic Shield Core and an Engine II, with Thulium, drops and 3 Dark Matter Plates ([Dark Matter and Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)). Emergency Repair has a fourth rank, the Repair Drone IV.

## Cooldowns and limits

- **The cooldown starts when you press** the ability and includes its duration. So a 10-second Surge on a 90-second cooldown is up 11% of the time at most, and unavailable for 80 seconds after it ends. Several modules do not shorten it (it is the worst-ranked module's); even three Afterburners are up at most 22% of the time.
- **Cooldowns belong to you, not to the item.** Swapping configuration, changing the item, jumping to another sector and logging out do not reset them. A ship that is destroyed starts the next flight with every ability ready.
- **Each ability has its own cooldown.** Using one does not lock the others.
- **A running effect keeps the numbers it started with.** Unfitting the item or swapping configuration does not change or end it. A jump or a reconnect does not end it either; logging out does, and its cooldown stays.
- Other pilots see your abilities' timers on the map, as they always did: a spent Surge tells them the next minutes are open.

## Keys and buttons

`Q` Shield Surge, `W` Afterburner, `E` Emergency Repair and `F` the ability of your ship's design (all configurable in the settings). Each button appears beside the hotbar only when your configuration has that ability (the `F` button, when the ship you fly has one), so a new pilot's `E` is there from the first minute. The ring around its icon tells where the ability is: whole in the ability's colour when it is ready, draining with the seconds left while it runs (the Emergency Repair too, now that it heals over ten seconds), and filling up again while it recharges, with the seconds left in the middle. A stack of several modules wears its mark (`x2`, `x3`) in the button's corner. The Emergency Repair button is dimmed while your hull is full, and the Shield Surge button on a ship with no shield at all. Hover a button for the numbers on your ship, the stack counted (for example *Afterburner II x2: +45% speed for 15 s*), and, while a Surge or a repair runs, how much it gives a second and how much is still to come.

## In the Hangar

Drag a shield, an engine or a Repair Drone onto an ability slot, or right-click it in your inventory to put it in the first free one. A second and a third of the same kind go into the next free slots and stack. The name and rank of the ability sit under each filled slot, with the stack mark and the numbers of all its modules together (*Afterburner II x2*, *x2 · 15 s*; for one Repair Drone II on a Wraith *+81,000 hull*), and hovering a slot shows what it is worth on your ship, the stack counted, and which module of the stack sets the rank. Every module of a kind shows the same ability, because they are one. Hovering the item anywhere else shows the ability with the shares of your own ship and one sentence on what a further module adds.

## What everyone sees

A Shield Surge is a bubble around the ship for as long as it runs, that flickers for its last two seconds and closes in when it ends. The shield bars (yours in the Ship window, and a target's in the Target window) simply fill as the Surge puts shield back, and the bar pulses lightly while there is room for it. An Afterburner burns the engines hotter for as long as it runs, 10, 15 or 20 seconds, and sends a ring out from the ship when it starts, wider for a stack. An Emergency Repair sends out a green pulse when it starts, then for its ten seconds wraps the hull in a soft green glow with a few plus signs rising off it, floats the hull it heals each second over your own ship, and ends with a last flash. While it runs, small repair drones circle the ship and mend it: one for a Repair Drone I, two for a II, three for a III or IV, and one more for each further Repair Drone in a stack (never more than three). They leave the hull, aim soft green beams at plates of it, send pulses along the beams from tier II on, and fly back to dock when the ten seconds are over; a Shield Surge has up to two blue ones inside its bubble. Every pilot on the map sees all three abilities, the drones too (smaller on another pilot's ship, and fewer on the lower graphics settings, where Low shows beams and glows without drone models, and a beam a little wider for each rank of the drone), so a spent Surge is a signal to the enemy as much as to you. The drones make three quiet sounds of their own, far under the repair's bell: a soft blip as they leave the hull, one as they dock and a faint tone under their beams while they work (a Surge's drones a little higher); you hear them from ships on your screen, at most a few at once, and the Sound Effects volume turns them down. With *Reduce Motion* on, the glow stays steady, the plus signs are left out, the last flash is a fade, and the drones stay parked beside the ship with a steady beam (the sounds stay). A Repair Drone in an extra slot (REP) draws its drones too, for as long as it mends the hull: one for a Repair Drone I, two for a II, three for a III or IV, circling the ship and beaming it, and every pilot on the map sees them. They fly back to dock when the repair stops.

## What changed

Before the 0.4.3 update the ability slots took Shield Cells (Shield Regen) and Thrusters (Speed Boost). Shield Cells and Thrusters that sat in ability slots went back to your inventory when the game updated, and you keep them: they are still modules of shields, engines and Adaptive Cores. Since then the Shield Surge no longer gives an overshield barrier but repairs your shield over ten seconds, Emergency Repair heals over ten seconds instead of at once, and you can fit several modules of a kind for a longer Afterburner, a bigger Surge or a bigger repair.
