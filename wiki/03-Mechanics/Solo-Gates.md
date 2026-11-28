# Solo Gates

<!-- wiki-search: solo gates; solo gate; gate; gates; galaxy gates; rift; rifts; alpha rift; beta breach; gamma foundry; delta siege; omega vault; chrono gate; chrono-gate; materializer; energy materializer; scan; spin; gate part; gate parts; guarantee; pity; consolation; wave; waves; nuke wave; skip; boss; lives; resume; abandon; speedrun; no death; challenge; achievement; thulium cap; davidski's nightmare; nightmare; evil davidski; angry davidski; evil ships; golden ships -->

The **solo gates** are five gates of the Galaxy Gates that you fly alone: **Alpha Rift**, **Beta Breach**, **Gamma Foundry**, **Delta Siege** and **Omega Vault**. Each is an empty arena of its own where waves of aliens come at you one after the other and a boss waits at the end. **Davidski's Nightmare** is a sixth gate, set apart from those five: its waves are not aliens but **Evil ships**, ships of the game that fly against you, and it is the dearest gate to build. You build a gate with its **parts**, which you find by spinning the Energy Materializer with Thulium, and a clear pays Credits, Thulium, experience, honor, ore, plates and ammo.

A solo gate is not a [clan dungeon](/wiki/03-Mechanics/Dungeons.md). A dungeon is a maze that a clan opens for a group with a Warlord at its end; a solo gate is an arena that only you are in, and nobody else can enter it with you. The two have separate rules, pay and limits. The Galaxy Gates page also has the **Chrono-Gate**, which is not a place to fly but the gate that opens your [Transport Cache](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) for the wipe: its parts are found with the same spins.

## At a glance

<!-- solo-glance:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Gates**: 7: the Chrono-Gate and 6 solo gates, Alpha Rift, Beta Breach, Gamma Foundry, Delta Siege, Omega Vault and Davidski's Nightmare
- **Spin**: 100 Thulium for each spin, and 1, 5, 10, 100 or 1,000 spins at a time
- **Chance of a part**: 13% a spin, in whichever category you scan. The part belongs to one of the gates of that category, all equally likely: the Chrono-Gate alone gets all of it, Alpha Rift, Beta Breach and Gamma Foundry get 4.33% each, and Delta Siege and Omega Vault get 6.5% each. Once the Chrono-Gate is complete there is nothing left to scan in its category
- **Guarantee**: After 24 spins in a row without a part the chance rises with every spin, and after 47 the next spin always finds one. A part of any gate starts the count again
- **Lives**: 3 in an attempt; every death costs one
- **Countdown**: 5 s before every wave, the first and the boss's too. A wave has no timer, and neither has a run
- **Arena**: Open space of 8,000 × 6,000 units with no rocks, and you are alone in it. A world has 16 of them, and when all are busy you cannot go in
- **Aliens at once**: At most 60 of a wave are alive at once, and 250 in an optional wave. The rest wait for room
- **Bosses**: A boss cannot be hurt for 3 s when it changes phase
- **Thulium cap**: A gate pays back no more than 50% of the Thulium you spent on spins. The rest is cut, and the result says how much

<!-- solo-glance:end -->

## Finding gate parts

Open the **Galaxy Gates** page and spin the Energy Materializer. Every spin is paid in Thulium and finds at most one part. Pick a **category** first: the **Chrono-Gate**, **Alpha–Gamma** (Alpha Rift, Beta Breach and Gamma Foundry) **Delta–Omega** (Delta Siege and Omega Vault) or **Davidski's Nightmare**, which has a category to itself. The chance of a part is the same in every category, and the part belongs to one of the gates of the category you picked, all equally likely. You need a number of parts of a gate to build it, and the parts are yours until you use them. A spin that finds no part is not lost: it pays a prize ([below](#a-spin-without-a-part)). Every spin is charged. When the Chrono-Gate is complete its entry is shut, because there is nothing left to find in it, and the other two categories keep their chance, so a part of a solo gate costs the same with or without it.

The table gives the cost of each gate in parts and what they cost on average **with the guarantee** when you scan the category the gate is in (a spin is a lottery, so a lucky pilot pays less and an unlucky one more, up to the longest run of spins the guarantee allows).

<!-- solo-parts:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Gate | Parts to complete it | Chance of a part per spin | Spins on average | Thulium on average |
| :--- | ---: | ---: | ---: | ---: |
| **Chrono-Gate** | 13 | 13% | 99 | 9,851 |
| **Alpha Rift** | 14 | 4.33% | 318 | 31,825 |
| **Beta Breach** | 33 | 4.33% | 750 | 75,016 |
| **Gamma Foundry** | 68 | 4.33% | 1,546 | 154,579 |
| **Delta Siege** | 96 | 6.5% | 1,455 | 145,486 |
| **Omega Vault** | 119 | 6.5% | 1,803 | 180,343 |
| **Davidski's Nightmare** | 238 | 13% | 1,803 | 180,343 |

<!-- solo-parts:end -->

The parts of the Chrono-Gate go back to nothing at the wipe, and you find them again every season. **The parts of the solo gates stay**, and so do the guarantee's count and the record of what you spent on spins and what the gates paid back; the wipe takes none of them ([Gates and the wipe](#gates-and-the-wipe)).

### A spin without a part

Most spins find no part. Each of them pays one prize, picked by the chances below: laser ammo of the second multiplier or better, a rocket stack of the second or third tier, and now and then a [special item](/wiki/06-Items/Special-Items.md) or a [container](/wiki/06-Items/Containers.md). A prize that cannot be given (the special items or the containers are switched off, say) becomes a stack of ammo or rockets by the same roll, so a spin never pays less than its table. The prize is worth clearly less than the spin costs: the gates are a Thulium sink.

<!-- solo-prizes:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Prize | Chance per spin |
| :--- | ---: |
| A container: Chroma Archive | 0.01% |
| A special item: Magic Hammer | 0.2% |
| A special item: Schematics | 0.2% |
| A special item: Philosopher's Stone | 0.2% |
| A special item: Forger's Seal | 0.2% |
| A special item: Workforce Contract | 0.2% |
| A special item: Tinkerer's Badge | 0.1% |
| Laser ammo: Advanced Plasma ×75 | 12.88% |
| Laser ammo: Antimatter Battery I ×62 | 8.59% |
| Laser ammo: Ultra Core ×40 | 8.59% |
| Laser ammo: Antimatter Battery II ×29 | 4.29% |
| Laser ammo: Dark Matter Ammo I ×31 | 4.29% |
| Laser ammo: Experimental Fusion Core ×17 | 2.15% |
| Laser ammo: Dark Matter Ammo II ×17 | 2.15% |
| Rockets: Lancet II ×4 | 8.59% |
| Rockets: Rivet II ×4 | 8.59% |
| Rockets: Ember II ×4 | 8.59% |
| Rockets: Scatter II ×4 | 8.59% |
| Rockets: Lancet III ×1 | 2.15% |
| Rockets: Rivet III ×1 | 2.15% |
| Rockets: Ember III ×1 | 2.15% |
| Rockets: Scatter III ×1 | 2.15% |

<!-- solo-prizes:end -->

## Going in

You **build** a gate on the Galaxy Gates page and **jump in** through its portal. Building works from the station, with your ship docked, and in flight too: the **Galaxy Gates window**, which the gates button of the toolbar opens, spins, builds and picks the destination as the page does. It needs:

- the parts of the gate: they are taken **once, when you build it**, and a refused build takes nothing;
- the gate itself not built yet: you may have **every** gate built at once, with a portal for each, and you play one at a time; a gate you built is entered through its portal or abandoned before you build it again;
- the home server (a gate is built at the home server only: on a regional server you return to base first).

The built gate stands in your **home sector** (`M-1`, `T-1` or `G-1`, by your company) as a portal named after it, and the Galaxy Gates page says where it stands. **Launch, fly to the portal and jump** through it as through any portal. A rift has to be free in your world when you go in: each world has a number of them, and when all are busy you wait. You see only **your own** gates: the portals of other pilots' gates standing in the same sector are not shown to you. You may have **all five gates built at the same time**, each with a portal of its own, and you play one at a time: **while you are in an arena none of your portals stands**, and they come back when you are out.

**On the regional servers (Singapore, US East).** A built gate is played there too. Its portal stands in your home sector on a regional server as it does at the home server, and you are told about it when you arrive. **Jump through it and you go into an arena of that server**, at its latency instead of the home server's. A regional server holds only **two arenas in each world**, where the home server has many more: when both are busy you wait, as you do for a free rift at the home server. The home server stays the one place that keeps your run, your parts and your pay: the pay reaches your wallet when the home server has counted the run, a few seconds after it ends, and the **wallet in your flight window catches up when you dock**. You enter your next run only after the last one has been counted. A run you leave in the arena is entered again through the portal; one you want to give up is abandoned in the arena or at the station. If the arena of a regional server is switched off, its portal takes you back to the home server instead, where you launch into your gate as above. What else works on a regional server is in [Servers](/wiki/03-Mechanics/Servers.md).

You land in the middle of an empty arena, alone. Nobody can attack you in it, and the Jump and Base CPUs do not work.

## How a run goes

1. **A countdown comes before every wave**, the first and the boss's too. A wave has no timer, and neither has the run: it takes as long as you need.
2. **A wave** appears on a ring round you and flies at you, at the pace of the gate. Only so many of it are alive at once, and the rest wait for room. It ends when its last alien is dead.
3. **Your progress is saved after every wave.** If you leave, a wave that was on begins again whole when you come back.
4. **An optional wave** is a huge wave of Seekers, and Delta Siege and Omega Vault have one each. During its countdown you may skip it: it then counts as done, and it pays **nothing**. If you fight it, its kills pay like the kills of any wave.
5. **The last wave is the boss.** It changes phase as its hull falls, and it cannot be hurt for a moment at every change. When the boss dies the run is cleared, and the clear is paid at once.

**Lives.** A death costs one life and sends you to your base like any other death; the run waits for you, with no clock running. While the run is open and you are outside the arena, **the portal of each gate you built stands in your home sector**, and a jump through one of them takes you back in at the saved wave with the lives you have left, as **Resume** does; it asks for no new parts. When your last life is gone the attempt ends but the run stays open at the last cleared wave, and going back in refills your lives. **Leave**, a log-off or a change of world pauses the run without costing a life. A restart of the server keeps your run open too. **Abandon** gives the run up: its parts are gone, and the aliens you killed are paid as they stand. Resume works only from a flying ship: after a death its button on the result screen waits, with a line that says why, until you have respawned. A respawned ship returns with a capped hull, so when your hull is under half the result screen warns you; Resume still puts you back as you are. The repair ships at your base mend you inside their aura.

Every world fights the same gate: the aliens' strength and pay do not depend on the world you fly in.

### The waves

The aliens are the ones of the game (the Seeker, the Phantasm, the Bulwark, the Goombah and the Crystalys), made harder or softer by the gate. The waves of **Davidski's Nightmare** are **Evil ships** instead: one for each hull a pilot can fly, in the livery of the Dormant swarm. The small hulls come first, and each wave brings more of them and bigger ones, until the last wave before the boss. An Evil ship carries what a pilot's ship carries: lasers, a **rocket** that it fires at you every few seconds, and a **repair drone** that mends its hull while nothing is hitting it, so a ship you leave alone heals. The planned time is what the gate is built to take a pilot at the starting level of Laser tech ([Pilot Skills](/wiki/03-Mechanics/Pilot-Skills.md)); a pilot who has levelled up Laser tech finishes sooner.

Some waves bring a **swarm**: a boss NPC of the game (a Boss Seeker, Boss Phantasm, Boss Goombah or Boss Crystalys) with its guards, who attack as one group. Every ship of a swarm is part of its wave, and the wave ends when the last of them is dead. They pay like the other ships of the wave, at the figures in [the table of the aliens](#the-aliens). **A boss NPC drops its loot as it does in the sectors of the game**: ore, plates, ammo and rockets (what each one drops is on [the pages of the swarms](/wiki/05-Swarms/Swarms.md)). There is no box to pick up in a gate: the loot comes with the pay, straight into your inventory, and once for a run like the pay. Its guards drop nothing, in a gate as in the sectors, and they neither heal their boss nor come back. The table below says which waves of each gate bring a swarm.

<!-- solo-waves:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Gate | Waves, the boss's included | Aliens in the waves | Boss NPCs and swarms | Boss | Planned time |
| :--- | ---: | :--- | :--- | :--- | :--- |
| **Alpha Rift** | 10 | 44 Seeker, 140 Phantasm | wave 5: 1 Seeker Swarm, 1 Phantasm Swarm | Enhanced Phantasm | 10 to 15 min |
| **Beta Breach** | 14 | 64 Seeker, 158 Phantasm, 80 Bulwark, 20 Goombah | wave 4: 2 Seeker Swarm; wave 9: 1 Phantasm Swarm | Enhanced Bulwark | 15 to 25 min |
| **Gamma Foundry** | 18 | 78 Phantasm, 117 Bulwark, 91 Goombah, 8 Crystalys | wave 4: 1 Phantasm Swarm; wave 9: 1 Goombah Swarm; wave 14: 1 Goombah Swarm | Elite Crystalys | 25 to 35 min |
| **Delta Siege** | 22 | 250 Seeker, 200 Phantasm, 141 Bulwark, 130 Goombah, 12 Crystalys | wave 5: 2 Phantasm Swarm; wave 10: 2 Goombah Swarm; wave 15: 1 Goombah Swarm; wave 20: 1 Crystalys Swarm | Siege Construct | 35 to 45 min |
| **Omega Vault** | 26 | 250 Seeker, 236 Phantasm, 170 Bulwark, 174 Goombah, 25 Crystalys | wave 6: 1 Goombah Swarm; wave 11: 2 Goombah Swarm; wave 16: 1 Crystalys Swarm; wave 22: 1 Phantasm Swarm | Omega Guardian | 50 to 60 min |
| **Davidski's Nightmare** | 13 | 50 Evil Protos, 66 Evil Kitefin, 31 Evil Ostirion, 19 Evil Nomad, 22 Evil Paragon, 7 Evil Storm, 8 Evil Wraith, 2 Evil Ironclad |  | Evil Davidski | 45 to 60 min |

- **Delta Siege**: wave 18 (250 Seeker) is optional: you may skip it while its countdown runs, and it pays nothing
- **Omega Vault**: wave 17 (250 Seeker) is optional: you may skip it while its countdown runs, and it pays nothing; waves 22 to 24 are elite, with ×1.5 the hull, shield and damage

<!-- solo-waves:end -->

### The bosses

A boss is an alien's ship made larger, with a hull, a shield and a volley of its own, which no setting of the gate or the world changes. A phase begins when the boss's hull falls to the figure in the table: its shield may be set again, its volley or all its damage change, and it may start a move. Every move is announced: a circle, a ring or a mark on your ship shows a moment before it lands. The aliens that a boss calls pay and drop nothing.

**Evil Davidski**, the boss of Davidski's Nightmare, flies Davidski's own Ironclad in a darker gold. He fires Dormant Lances, guided rockets that follow you over a long way, and fights with meteors, a ring and Evil ships that he calls. At a third of his hull he becomes **ANGRY DAVIDSKI**: his tune plays, he hits harder, and a **golden ship of every ship in the game** appears round him. While any of the golden ships is alive he cannot be hurt at all: your lasers and rockets cannot lock on to him and nothing you do touches his hull or his shield, so you cut through them first; when the last one falls the protection is gone for good. He mocks you from his own window at the start of every wave. Killing him counts as a kill of Davidski for the missions that ask for one, in a gate as in the Danger Sectors. A game that is not up to date does not show the gate.

<!-- solo-bosses:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Boss | Gate | Hull | Shield | Laser volley |
| :--- | :--- | ---: | ---: | ---: |
| **Enhanced Phantasm** | Alpha Rift | {{guide:vitals.hull@Enhanced Phantasm}} | {{guide:vitals.shield@Enhanced Phantasm}} | {{guide:vitals.dps*0.9007633587786259~1.099236641221374@Enhanced Phantasm}} |
| **Enhanced Bulwark** | Beta Breach | {{guide:vitals.hull@Enhanced Bulwark}} | {{guide:vitals.shield@Enhanced Bulwark}} | {{guide:vitals.dps*0.9019607843137255~1.0980392156862746@Enhanced Bulwark}} |
| **Elite Crystalys** | Gamma Foundry | {{guide:vitals.hull@Elite Crystalys}} | {{guide:vitals.shield@Elite Crystalys}} | {{guide:vitals.dps*0.896551724137931~1.103448275862069@Elite Crystalys}} |
| **Siege Construct** | Delta Siege | {{guide:vitals.hull@Siege Construct}} | {{guide:vitals.shield@Siege Construct}} | {{guide:vitals.dps*0.8974358974358975~1.1025641025641026@Siege Construct}} |
| **Omega Guardian** | Omega Vault | {{guide:vitals.hull@Omega Guardian}} | {{guide:vitals.shield@Omega Guardian}} | {{guide:vitals.dps*0.896551724137931~1.103448275862069@Omega Guardian}} |
| **Evil Davidski** | Davidski's Nightmare | {{guide:vitals.hull@Evil Davidski}} | {{guide:vitals.shield@Evil Davidski}} | {{guide:vitals.dps*0.896551724137931~1.103448275862069@Evil Davidski}} |

| Boss | Phase | Hull left | What it does |
| :--- | :--- | :--- | :--- |
| **Enhanced Phantasm** | Enhanced Phantasm | 100% to 66% | It only shoots. |
|  | Reinforced | 66% to 33% | Its shield is set to ×1 of the boss's own. Every 10 min it calls 4 Phantasm, at most 4 of them alive; they pay and drop nothing. |
|  | Second attack | 33% to 0% | Its volley is ×1.3. Every 30 s a blast of {{guide:behaviour.ability:phases.ringBlast@Enhanced Phantasm}} hits everything within 500 units of the boss; the ring shows 2 s before it lands. |
| **Enhanced Bulwark** | Shielded | 100% to 66% | Its shield is set to ×4 of the boss's own. |
|  | Rocket barrage | 66% to 33% | It fires 4 Dormant Lance rockets at you, {{guide:behaviour.ability:phases.rocketBarrage@Enhanced Bulwark}} each, one every 0.5 s, in a barrage every 30 s. |
|  | Second attack | 33% to 0% | Its volley is ×1.3. Every 10 min it calls 4 Phantasm, at most 4 of them alive; they pay and drop nothing. |
| **Elite Crystalys** | Elite | 100% to 66% | It only shoots. |
|  | Renewed shield | 66% to 33% | Its shield is set to ×1 of the boss's own. |
|  | Reinforced | 33% to 0% | Its shield is set to ×2 of the boss's own. Every 10 min it calls 10 Goombah, at most 10 of them alive; they pay and drop nothing. |
| **Siege Construct** | Siege Construct | 100% to 66% | Every 1 min it drops 3 volleys of 8 meteors, {{guide:behaviour.ability:phases.meteors@Siege Construct}} each to everything within 420 units of where it lands, 50% of them aimed at you; each circle shows 3 s before it lands. |
|  | Rocket barrage | 66% to 33% | Every 1 min it drops 3 volleys of 8 meteors, {{guide:behaviour.ability:phases.meteors2@Siege Construct}} each to everything within 420 units of where it lands, 50% of them aimed at you; each circle shows 3 s before it lands. It fires 6 Dormant Lance rockets at you, {{guide:behaviour.ability:phases.rocketBarrage@Siege Construct}} each, one every 0.5 s, in a barrage every 1 min. |
|  | Frenzy | 33% to 0% | Every 30 s it drops 3 volleys of 8 meteors, {{guide:behaviour.ability:phases.meteors3@Siege Construct}} each to everything within 420 units of where it lands, 50% of them aimed at you; each circle shows 3 s before it lands. It fires 6 Dormant Lance rockets at you, {{guide:behaviour.ability:phases.rocketBarrage2@Siege Construct}} each, one every 0.5 s, in a barrage every 30 s. |
| **Omega Guardian** | Shield Fortress | 100% to 66% | Its shield is set to ×1.5 of the boss's own. Every 40 s it calls 6 Bulwark, at most 12 of them alive; they pay and drop nothing. |
|  | Swarm Protocol | 66% to 33% | Every 25 s it calls 12 Phantasm, at most 24 of them alive; they pay and drop nothing. Every 30 s a blast of {{guide:behaviour.ability:phases.ringBlast@Omega Guardian}} hits everything within 700 units of the boss; the ring shows 2 s before it lands. |
|  | Overload | 33% to 0% | Its shield is set to ×0.1 of the boss's own. All its damage is ×2.5. After 2 min in the phase all its damage is ×2 more. Every 25 s a blast of {{guide:behaviour.ability:phases.ringBlast2@Omega Guardian}} hits everything within 700 units of the boss; the ring shows 2 s before it lands. |
| **Evil Davidski** | Evil Davidski | 100% to 66% | It only shoots. |
|  | Davidski attacks | 66% to 33% | It fires 6 Dormant Lance rockets at you, {{guide:behaviour.ability:phases.rocketBarrage@Evil Davidski}} each, one every 0.5 s, in a barrage every 30 s. Every 1 min it drops 2 volleys of 8 meteors, {{guide:behaviour.ability:phases.meteors@Evil Davidski}} each to everything within 400 units of where it lands, 50% of them aimed at you; each circle shows 3 s before it lands. Every 40 s it calls 5 Evil Protos, at most 10 of them alive; they pay and drop nothing. |
|  | Angry | 33% to 0% | Its shield is set to ×0.5 of the boss's own. All its damage is ×1.5. After 8 min in the phase all its damage is ×2 more. It fires 6 Dormant Lance rockets at you, {{guide:behaviour.ability:phases.rocketBarrage2@Evil Davidski}} each, one every 0.4 s, in a barrage every 30 s. Every 1 min it drops 3 volleys of 8 meteors, {{guide:behaviour.ability:phases.meteors2@Evil Davidski}} each to everything within 420 units of where it lands, 50% of them aimed at you; each circle shows 3 s before it lands. Every 45 s a blast of {{guide:behaviour.ability:phases.ringBlast@Evil Davidski}} hits everything within 700 units of the boss; the ring shows 2 s before it lands. Every 40 s it calls 3 Evil Kitefin, at most 6 of them alive; they pay and drop nothing. |

<!-- solo-bosses:end -->

## What a clear pays

A clear pays its table **once**, in one go, the moment the boss dies: the Credits, the Thulium, the experience and the honor, the ore, plates and Power Cores, and the ammo. The experience and the honor count for your PvE ranking points, as a dungeon's do.

<!-- solo-pay:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Gate | Credits | Thulium | XP | Honor |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 450,000 | 5,000 | 70,000 | 1,000 |
| **Beta Breach** | 1,500,000 | 12,000 | 180,000 | 2,500 |
| **Gamma Foundry** | 4,000,000 | 25,000 | 400,000 | 5,500 |
| **Delta Siege** | 8,000,000 | 40,000 | 800,000 | 10,000 |
| **Omega Vault** | 15,000,000 | 60,000 | 1,500,000 | 20,000 |
| **Davidski's Nightmare** | 15,000,000 | 60,000 | 1,500,000 | 20,000 |

- **Alpha Rift**: Ship Fragment ×300, Nyxite ×300, Daraxium ×400, Echo Shard ×4, Lattice Shard ×6; ammo: Advanced Plasma ×15,000, Ultra Core ×3,750, Experimental Fusion Core ×15,000
- **Beta Breach**: Ship Fragment ×700, Nyxite ×750, Daraxium ×800, Cataclysite ×400, Quorvium ×100, Echo Shard ×9, Lattice Shard ×13; ammo: Advanced Plasma ×37,500, Ultra Core ×15,000, Experimental Fusion Core ×22,500
- **Gamma Foundry**: Ship Fragment ×1,150, Nyxite ×1,000, Cataclysite ×900, Quorvium ×400, Power Core ×15, Echo Shard ×18, Lattice Shard ×27; ammo: Advanced Plasma ×22,500, Ultra Core ×45,000, Experimental Fusion Core ×37,500
- **Delta Siege**: Ship Fragment ×2,000, Nyxite ×1,750, Cataclysite ×1,500, Quorvium ×1,000, Reinforced Hull Plate ×70, Power Core ×40, Ancient Control Unit ×3, Echo Shard ×29, Lattice Shard ×44; ammo: Advanced Plasma ×30,000, Ultra Core ×67,500, Experimental Fusion Core ×56,250
- **Omega Vault**: Ship Fragment ×3,250, Nyxite ×2,750, Cataclysite ×2,250, Quorvium ×1,600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10, Echo Shard ×34, Lattice Shard ×54; ammo: Advanced Plasma ×37,500, Ultra Core ×75,000, Experimental Fusion Core ×75,000
- **Davidski's Nightmare**: Ship Fragment ×3,250, Nyxite ×2,750, Cataclysite ×2,250, Quorvium ×1,600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10, Echo Shard ×34, Lattice Shard ×54; ammo: Advanced Plasma ×37,500, Ultra Core ×75,000, Experimental Fusion Core ×75,000
- **Heartshards**: 1 with the first clear of each gate in a season, and a 5% chance of 1 more with every clear.

<!-- solo-pay:end -->

**The Thulium is cut to a cap.** The gates may pay back no more than a share of the Thulium you spent on spins, counted over all your gates and all your spins (the share is in the list at the top). What a clear and its aliens would pay above that is cut, and the result screen says how much. Credits, experience, honor, ore, plates and ammo are never cut.

### The aliens

Every alien you kill in a gate pays, at the figures it has in Alpha whichever world you fly in: no world multiplier, no booster and no Premium bonus changes them. A wave pays for its aliens **once** for a run, however often you leave and come back. The pay comes with the end of each stretch of the run: when you leave, die, run out of lives, abandon or clear it. The kills of a stretch go unpaid only in the wipe and in a restart of the server while you are inside (your run stays open, but the kills of that stretch are lost). The kills of a gate count for the [missions](/wiki/03-Mechanics/Quests.md#where-it-counts) that name no sector, such as the big hunts of the Challenge line, as they happen (a wave counts for them **once** for a run, as it pays once), and for nothing else: not for the kill statistics, the achievements' counters, the kill feed or the experience of your drones and P.E.T.s. The experience and the honor they pay do count for your PvE ranking points, as the experience and the honor of a clear do. The loot of the aliens comes with the pay, straight into your inventory.

<!-- solo-kills:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Alien | Credits | Thulium | XP | Honor |
| :--- | ---: | ---: | ---: | ---: |
| **Seeker** | {{guide:spoils.pay.credits@Seeker#1}} | {{guide:spoils.pay.thulium@Seeker#1}} | {{guide:spoils.pay.experience@Seeker#1}} | {{guide:spoils.pay.honor@Seeker#1}} |
| **Phantasm** | {{guide:spoils.pay.credits@Phantasm#1}} | {{guide:spoils.pay.thulium@Phantasm#1}} | {{guide:spoils.pay.experience@Phantasm#1}} | {{guide:spoils.pay.honor@Phantasm#1}} |
| **Bulwark** | {{guide:spoils.pay.credits@Bulwark#1}} | {{guide:spoils.pay.thulium@Bulwark#1}} | {{guide:spoils.pay.experience@Bulwark#1}} | {{guide:spoils.pay.honor@Bulwark#1}} |
| **Goombah** | {{guide:spoils.pay.credits@Goombah#1}} | {{guide:spoils.pay.thulium@Goombah#1}} | {{guide:spoils.pay.experience@Goombah#1}} | {{guide:spoils.pay.honor@Goombah#1}} |
| **Crystalys** | {{guide:spoils.pay.credits@Crystalys#1}} | {{guide:spoils.pay.thulium@Crystalys#1}} | {{guide:spoils.pay.experience@Crystalys#1}} | {{guide:spoils.pay.honor@Crystalys#1}} |
| **Boss Seeker** | {{guide:spoils.pay.credits@Boss Seeker#1}} | {{guide:spoils.pay.thulium@Boss Seeker#1}} | {{guide:spoils.pay.experience@Boss Seeker#1}} | {{guide:spoils.pay.honor@Boss Seeker#1}} |
| **Seeker Slave** | {{guide:spoils.pay.credits@Seeker Slave#1}} | {{guide:spoils.pay.thulium@Seeker Slave#1}} | {{guide:spoils.pay.experience@Seeker Slave#1}} | {{guide:spoils.pay.honor@Seeker Slave#1}} |
| **Boss Phantasm** | {{guide:spoils.pay.credits@Boss Phantasm#1}} | {{guide:spoils.pay.thulium@Boss Phantasm#1}} | {{guide:spoils.pay.experience@Boss Phantasm#1}} | {{guide:spoils.pay.honor@Boss Phantasm#1}} |
| **Phantasm Guard** | {{guide:spoils.pay.credits@Phantasm Guard#1}} | {{guide:spoils.pay.thulium@Phantasm Guard#1}} | {{guide:spoils.pay.experience@Phantasm Guard#1}} | {{guide:spoils.pay.honor@Phantasm Guard#1}} |
| **Boss Goombah** | {{guide:spoils.pay.credits@Boss Goombah#1}} | {{guide:spoils.pay.thulium@Boss Goombah#1}} | {{guide:spoils.pay.experience@Boss Goombah#1}} | {{guide:spoils.pay.honor@Boss Goombah#1}} |
| **Goombah Guard** | {{guide:spoils.pay.credits@Goombah Guard#1}} | {{guide:spoils.pay.thulium@Goombah Guard#1}} | {{guide:spoils.pay.experience@Goombah Guard#1}} | {{guide:spoils.pay.honor@Goombah Guard#1}} |
| **Boss Crystalys** | {{guide:spoils.pay.credits@Boss Crystalys#1}} | {{guide:spoils.pay.thulium@Boss Crystalys#1}} | {{guide:spoils.pay.experience@Boss Crystalys#1}} | {{guide:spoils.pay.honor@Boss Crystalys#1}} |
| **Crystalys Guard** | {{guide:spoils.pay.credits@Crystalys Guard#1}} | {{guide:spoils.pay.thulium@Crystalys Guard#1}} | {{guide:spoils.pay.experience@Crystalys Guard#1}} | {{guide:spoils.pay.honor@Crystalys Guard#1}} |
| **Evil Protos** | {{guide:spoils.pay.credits@Evil Protos}} | {{guide:spoils.pay.thulium@Evil Protos}} | {{guide:spoils.pay.experience@Evil Protos}} | {{guide:spoils.pay.honor@Evil Protos}} |
| **Evil Kitefin** | {{guide:spoils.pay.credits@Evil Kitefin}} | {{guide:spoils.pay.thulium@Evil Kitefin}} | {{guide:spoils.pay.experience@Evil Kitefin}} | {{guide:spoils.pay.honor@Evil Kitefin}} |
| **Evil Ostirion** | {{guide:spoils.pay.credits@Evil Ostirion}} | {{guide:spoils.pay.thulium@Evil Ostirion}} | {{guide:spoils.pay.experience@Evil Ostirion}} | {{guide:spoils.pay.honor@Evil Ostirion}} |
| **Evil Nomad** | {{guide:spoils.pay.credits@Evil Nomad}} | {{guide:spoils.pay.thulium@Evil Nomad}} | {{guide:spoils.pay.experience@Evil Nomad}} | {{guide:spoils.pay.honor@Evil Nomad}} |
| **Evil Paragon** | {{guide:spoils.pay.credits@Evil Paragon}} | {{guide:spoils.pay.thulium@Evil Paragon}} | {{guide:spoils.pay.experience@Evil Paragon}} | {{guide:spoils.pay.honor@Evil Paragon}} |
| **Evil Storm** | {{guide:spoils.pay.credits@Evil Storm}} | {{guide:spoils.pay.thulium@Evil Storm}} | {{guide:spoils.pay.experience@Evil Storm}} | {{guide:spoils.pay.honor@Evil Storm}} |
| **Evil Wraith** | {{guide:spoils.pay.credits@Evil Wraith}} | {{guide:spoils.pay.thulium@Evil Wraith}} | {{guide:spoils.pay.experience@Evil Wraith}} | {{guide:spoils.pay.honor@Evil Wraith}} |
| **Evil Ironclad** | {{guide:spoils.pay.credits@Evil Ironclad}} | {{guide:spoils.pay.thulium@Evil Ironclad}} | {{guide:spoils.pay.experience@Evil Ironclad}} | {{guide:spoils.pay.honor@Evil Ironclad}} |

| Gate | Credits | Thulium | XP | Honor |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 514,000 | 2,099 | 55,296 | 1,018 |
| **Beta Breach** | 1,298,500 | 5,939 | 187,744 | 2,470 |
| **Gamma Foundry** | 3,064,500 | 13,693 | 541,944 | 4,696 |
| **Delta Siege** | 5,239,625 | 22,338 | 882,676 | 7,850 |
| **Omega Vault** | 7,088,125 | 29,196 | 1,196,828 | 10,022 |
| **Davidski's Nightmare** | 7,081,950 | 29,124 | 1,196,445 | 9,968 |

<!-- solo-kills:end -->

## Challenges and achievements

Two optional challenges can be won on any clear, and they pay an achievement each and **no Thulium**. A **no-death** clear is one with no death at all in the whole run, over every time you went in. A **speedrun** is a clear within the shortest planned time of the gate, counted by the time you spend inside the arena. The other six achievements are for clearing each gate, and all five:

<!-- solo-achievements:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Rift Closed** (Common): Clear the Alpha Rift on your own.
- **Breach Sealed** (Uncommon): Clear the Beta Breach on your own.
- **Foundry Shutdown** (Rare): Clear the Gamma Foundry on your own.
- **Siege Broken** (Rare): Break the Delta Siege on your own.
- **Vault Cracked** (Epic): Crack the Omega Vault on your own.
- **Gatekeeper** (Legendary): Clear all five solo gates: Alpha, Beta, Gamma, Delta and Omega.
- **Untouchable** (Rare): Clear a solo gate without losing a life.
- **Against the Clock** (Rare): Clear a solo gate in no more than its shortest time: 10, 15, 25, 35 or 50 minutes for Alpha to Omega.

<!-- solo-achievements:end -->

## Items from a gate

What a gate gives you is **Marketable**: the ore, the plates, the Power Cores, the ammo and the loot of the aliens can be listed on the [Auction](/wiki/03-Mechanics/Auction.md) like a drop or a quest reward, with the same exceptions as for any item. The prizes of a spin without a part are not: they come from a spin, not from a gate.

## Gates and the wipe

- **The wipe ends any run that is open** and gives its parts back to you. A run does not go on into the next season.
- **Kept through the wipe:** the parts of the five solo gates, the guarantee's count, and the record of what you spent on spins and what the gates paid back, so the cap on the Thulium goes on across seasons. The achievements are yours for good.
- **Lost at the wipe:** the parts of the Chrono-Gate, as before. Your spins buy them again.
- **Deleting an account** deletes the parts, the count and the record.
