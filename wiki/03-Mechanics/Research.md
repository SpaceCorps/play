# Research

The **Research Centre** is the laboratory of your [Skylab](/wiki/03-Mechanics/Skylab.md). You feed it resources, it turns them into **science**, and the science researches **technologies**. Every craft in [Assembly](/wiki/06-Items/Overview.md#upgrading-modules) needs its technology first: a ship, a laser, a thruster or a CPU cannot be made until it has been researched.

This page has the whole technology tree with the time each technology takes, the science each resource gives, the Thulium boost, the rule for Dark Matter and the new CPUs. Its numbers are read from the game's own data, so they are always the ones in the game.

## The Research Centre

<!-- research-centre:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **Unlocks at Core level 10.** The Research Centre is a module of your [Skylab](/wiki/03-Mechanics/Skylab.md), built like the others: 25 Ship Fragments from your inventory (with your ship landed), 25,000 Credits and 500 Thulium. Its screen is the **Research** view of the Skylab page.
- **Levels 1 to 10.** A higher level gives a bigger tank and draws more power. It does not make research faster: a technology takes the same time at every level.
- **The tank.** The Centre keeps its science in a tank that holds 12 h of research at level 1 and 25% more with every level (the table below).
- **Fuel into science.** A resource you feed becomes science at once, as the fuel table shows. A research burns 1 science for every second of its research time; with the tank empty it waits, and it goes on when you feed the Centre.
- **A free first hour.** A new Centre starts with 3,600 science in its tank, 1 h of research.
- **One at a time.** The Centre researches one technology at a time. There is no queue.
- **While you are away.** A research runs on the server's clock, so it goes on after you log out, until it is finished or the tank is empty. A blackout or an upgrade of the Centre does not stop it.
- **Power.** The Centre draws 25 at level 1 and 15% more with every level, and it cannot be switched off.
- **The wipe keeps all of it:** your technologies, the science in the tank, the Dark Matter plugged in, a research under way and the boost.
- **What you own is yours.** When research came into the game, every pilot received the technology of each item they already held, and the technologies those needed. An item that reaches you later (a gift, a code, a reward) does not unlock its technology.
- **Below Core level 10** you cannot research, so you cannot make anything new in Assembly yet. The Station missions walk you up the Core.

<!-- research-centre:end -->

### The tank at every level

<!-- research-tank:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Level | Tank (science) | Holds research for | … with the boost | Power |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 43,200 | 12 h | 6 h | 25 |
| 2 | 54,000 | 15 h | 7.5 h | 28.7 |
| 3 | 67,500 | 18.8 h | 9.4 h | 33.1 |
| 4 | 84,375 | 23.4 h | 11.7 h | 38 |
| 5 | 105,469 | 29.3 h | 14.6 h | 43.7 |
| 6 | 131,836 | 36.6 h | 18.3 h | 50.3 |
| 7 | 164,795 | 45.8 h | 22.9 h | 57.8 |
| 8 | 205,994 | 57.2 h | 28.6 h | 66.5 |
| 9 | 257,492 | 71.5 h | 35.8 h | 76.5 |
| 10 | 321,865 | 89.4 h | 44.7 h | 87.9 |

<!-- research-tank:end -->

## Fuel

You feed the Centre with resources, and each unit becomes science at once. The more work a unit takes to get, the more science it gives: the figures follow how hard a unit is to get, not its rarity label, so an Uncommon Power Core gives more than a Rare Orvium. The ores come from the Resource Storage of your [Skylab](/wiki/03-Mechanics/Skylab.md#resource-storage); every other resource comes from your inventory, and your ship must be landed. The Velkonite Reinforced Plate, the Orvium Reinforced Plate, the Dark Matter Plate, Dark Matter, Credits and Thulium cannot be burnt; the Reinforced Hull Plate can.

<!-- research-fuel:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Resource | Rarity | Taken from | Science a unit | Units for 1 hour |
| :--- | :--- | :--- | ---: | ---: |
| [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) | Common | Your inventory | 5 | 720 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | Common | Your inventory | 5 | 720 |
| [Daraxium](/wiki/06-Items/Resources.md#daraxium) | Common | Your inventory | 7 | 515 |
| [Nyxite](/wiki/06-Items/Resources.md#nyxite) | Common | Your inventory | 7 | 515 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | Common | Your inventory | 8 | 450 |
| [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) | Common | Your inventory | 33 | 110 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | Uncommon | Resource Storage | 40 | 90 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | Rare | Resource Storage | 80 | 45 |
| [Power Core](/wiki/06-Items/Resources.md#power-core) | Uncommon | Your inventory | 100 | 36 |
| [Ancient Control Unit](/wiki/06-Items/Resources.md#ancient-control-unit) | Rare | Your inventory | 650 | 6 |

The last column is the number of units that run one hour of research without the boost, rounded up; with the boost it is 2 times as many.

<!-- research-fuel:end -->

## The Thulium boost

<!-- research-boost:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **5,000 Thulium** buys a boost: the Centre researches **2 times faster for 24 hours**.
- It also **burns science 2 times as fast**, so a boost buys time and never fuel: a technology burns the same science, boosted or not.
- A boost starts the moment you buy it and runs on the clock whether the tank has fuel or not, so buy it while a research is running. The Centre refuses one when nothing is being researched.
- Boosts add up: buying one while another runs adds 24 hours to its end, up to 72 hours ahead. A boost belongs to your Research Centre, not to one research.

What a boost does to the time of a research, boosted from its start:

| Research time | With the boost | Boosts for all of it | Thulium |
| :--- | :--- | ---: | ---: |
| 30 min | 15 min | 1 | 5,000 |
| 3 h | 1 h 30 min | 1 | 5,000 |
| 6 h | 3 h | 1 | 5,000 |
| 10 h | 5 h | 1 | 5,000 |
| 1 d | 12 h | 1 | 5,000 |
| 2 d | 1 d | 1 | 5,000 |

<!-- research-boost:end -->

## Dark Matter

The technologies at the top of the tree need Dark Matter as well. It comes from the [black hole](/wiki/03-Mechanics/Black-Hole.md#dark-matter), where a N.I.K.E. rocket that reaches it leaves some, and now and then from a Pulse of the [Dormant Swarm](/wiki/05-Swarms/Dormant-Swarm.md).

<!-- research-dark-matter:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **10 Dark Matter** for each of the 15 technologies in the table below, on top of the science: plug it into the Research Centre (from your inventory, with your ship landed) before you start, and the research takes it when it starts.
- **The rule:** an item of rarity Epic or higher whose research takes 10 h or more. The N.I.K.E., which is how Dark Matter is made, never needs it.
- **Cancel a research** and the Dark Matter you plugged in for it comes back to the Centre. The progress and the science already burnt do not.
- All of them together ask 150 Dark Matter.

| Technology | Rarity | Research time | Dark Matter |
| :--- | :--- | :--- | ---: |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | Epic | 10 h | 10 |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | Epic | 10 h | 10 |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | Epic | 10 h | 10 |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | Epic | 10 h | 10 |
| [Starfire-3](/wiki/06-Items/Lasers.md#lasers) | Mythical | 1 d | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | Mythical | 1 d | 10 |
| [Nova Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Epic | 10 h | 10 |
| [Apex Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Epic | 10 h | 10 |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | Epic | 1 d | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | Epic | 1 d | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | Mythical | 2 d | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | Mythical | 1 d | 10 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | Legendary | 1 d | 10 |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | Epic | 1 d | 10 |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | Epic | 1 d | 10 |

<!-- research-dark-matter:end -->

## The technology tree

Each box is a technology: the item it lets you make, with its research time under the name (the clock) and, where it needs Dark Matter, the Dark Matter badge. An arrow leads from a technology to the one that needs it, which you research first; a box with no arrow can be researched at once. Point at a box to see the research time, the science it burns and what Assembly then asks for the item, and click it to open the item's page. The trees are drawn from the game's own data.

<!-- research-tree:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

### Propulsion & Speed {#tree-propulsion}

```tree research
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines

Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```

### Shields & Defense {#tree-shields}

```tree research
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cores

Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```

### Lasers & Ammo {#tree-lasers}

```tree research
Quantum Laser 3 | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-3 | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser 3, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-3, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Nova Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Pulse Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Apex Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Prism Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-

Quantum Laser 3 => Starfire-3 => Helios Beam
```

### Boosters {#tree-boosters}

```tree research
Damage Amp II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
```

### Drones {#tree-drones}

```tree research
Master Drone | drone, rare | craft 40000 Thulium, 60 s | research 36000 s, 36000 science | 1 Slave Drone, 100 Ship Fragment | /wiki/06-Items/Drones.md#available-drones
```

### Ships {#tree-ships}

```tree research
Paragon | ship, rare | craft 1500 Thulium, 900 s | research 21600 s, 21600 science | 120 Ship Fragment, 20 Reinforced Hull Plate, 5 Power Core | /wiki/02-Ships/Paragon.md
Ironclad | ship, epic | craft 10500 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit | /wiki/02-Ships/Ironclad.md
Storm | ship, epic | craft 15000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit | /wiki/02-Ships/Storm.md
Wraith | ship, mythical | craft 20000 Thulium, 900 s | research 172800 s, 172800 science, 10 Dark Matter | 300 Ship Fragment, 50 Reinforced Hull Plate, 15 Power Core, 3 Ancient Control Unit | /wiki/02-Ships/Wraith.md
```

### Resources {#tree-resources}

```tree research
Dark Matter Plate | resource, mythical | craft 250 Thulium, 120 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Velkonite Reinforced Plate, 1 Orvium Reinforced Plate, 5 Dark Matter | /wiki/06-Items/Resources.md#dark-matter-plate
```

### Rockets {#tree-rockets}

```tree research
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
```

### CPUs {#tree-cpus}

```tree research
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 20 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 8 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu

Extra Slots CPU I => Extra Slots CPU II => Extra Slots CPU III
Base CPU I => Base CPU II => Jump CPU
```


<!-- research-tree:end -->

## All the technologies

<!-- research-technologies:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Technology | Needs first | Class | Research time | Science | Dark Matter |
| :--- | :--- | :--- | ---: | ---: | ---: |
| [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 min | 1,800 | – |
| [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 h | 10,800 | – |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 h | 36,000 | 10 |
| [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 min | 1,800 | – |
| [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 h | 10,800 | – |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 h | 36,000 | 10 |
| [Engine III](/wiki/06-Items/Propulsion.md#engines) | – | B | 3 h | 10,800 | – |
| [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 min | 1,800 | – |
| [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 h | 10,800 | – |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | C | 10 h | 36,000 | 10 |
| [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 min | 1,800 | – |
| [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 h | 10,800 | – |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | C | 10 h | 36,000 | 10 |
| [Heavy Shield Core](/wiki/06-Items/Shields.md#shield-cores) | – | B | 3 h | 10,800 | – |
| [Quantum Laser 3](/wiki/06-Items/Lasers.md#lasers) | – | B | 3 h | 10,800 | – |
| [Starfire-3](/wiki/06-Items/Lasers.md#lasers) | [Quantum Laser 3](/wiki/06-Items/Lasers.md#lasers) | D | 1 d | 86,400 | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | [Starfire-3](/wiki/06-Items/Lasers.md#lasers) | D | 1 d | 86,400 | 10 |
| [Nova Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | C | 10 h | 36,000 | 10 |
| [Apex Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | C | 10 h | 36,000 | 10 |
| [Damage Amp II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 h | 10,800 | – |
| [Shield Wall II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 h | 10,800 | – |
| [Hull Plating II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 h | 10,800 | – |
| [Master Drone](/wiki/06-Items/Drones.md#available-drones) | – | C | 10 h | 36,000 | – |
| [Paragon](/wiki/02-Ships/Paragon.md) | – | B | 6 h | 21,600 | – |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | – | D | 1 d | 86,400 | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | – | D | 1 d | 86,400 | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | – | D | 2 d | 172,800 | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | – | D | 1 d | 86,400 | 10 |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | B | 3 h | 10,800 | – |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | D | 1 d | 86,400 | 10 |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | – | A | 30 min | 1,800 | – |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | C | 10 h | 36,000 | – |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | D | 1 d | 86,400 | 10 |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | – | B | 3 h | 10,800 | – |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | C | 10 h | 36,000 | – |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | D | 1 d | 86,400 | 10 |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | – | B | 6 h | 21,600 | – |

The classes, by research time:

| Class | Research time | Technologies | One after another | Science | Dark Matter |
| :--- | :--- | ---: | ---: | ---: | ---: |
| A | 30 min | 5 | 2 h 30 min | 9,000 | 0 |
| B | 3 h to 6 h | 14 | 2 d | 172,800 | 0 |
| C | 10 h | 9 | 3 d 18 h | 324,000 | 60 |
| D | 1 d to 2 d | 9 | 10 d | 864,000 | 90 |
| All |  | 37 | 15 d 20 h 30 min | 1,369,800 | 150 |

Researched one after another, the whole tree takes 15 d 20 h 30 min. With the boost on all the time it takes 7 d 22 h 15 min, which is 8 boosts and 40,000 Thulium; the science is the same.

<!-- research-technologies:end -->

## The CPUs

The new CPUs are researched here too, then made in Assembly. The same table and notes are on the [Extras](/wiki/06-Items/Extras.md#research-cpus) page.

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
