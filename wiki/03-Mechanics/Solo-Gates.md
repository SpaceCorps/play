# Solo Gates

<!-- wiki-search: solo gates; solo gate; gate; gates; galaxy gates; rift; rifts; alpha rift; beta breach; gamma foundry; delta siege; omega vault; chrono gate; chrono-gate; materializer; energy materializer; scan; spin; gate part; gate parts; guarantee; pity; consolation; wave; waves; nuke wave; skip; boss; lives; resume; abandon; speedrun; no death; challenge; achievement; thulium cap -->

The **solo gates** are five gates of the Galaxy Gates that you fly alone: **Alpha Rift**, **Beta Breach**, **Gamma Foundry**, **Delta Siege** and **Omega Vault**. Each is an empty arena of its own where waves of aliens come at you one after the other and a boss waits at the end. You open a gate with its **parts**, which you find by spinning the Energy Materializer with Thulium, and a clear pays Credits, Thulium, experience, honor, ore, plates and ammo.

A solo gate is not a [clan dungeon](/wiki/03-Mechanics/Dungeons.md). A dungeon is a maze that a clan opens for a group with a Warlord at its end; a solo gate is an arena that only you are in, and nobody else can enter it with you. The two have separate rules, pay and limits. The Galaxy Gates page also has the **Chrono-Gate**, which is not a place to fly but the gate that opens your [Transport Cache](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) for the wipe: its parts are found with the same spins.

## At a glance

<!-- solo-glance:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Gates**: 6: the Chrono-Gate and 5 solo gates, Alpha Rift, Beta Breach, Gamma Foundry, Delta Siege and Omega Vault
- **Spin**: 100 Thulium for each spin, and 1, 5, 10 or 100 spins at a time
- **Chance of a part**: 13% a spin. The gate the part belongs to is picked by chance, and each gate gets 2.17% of the spins. When the Chrono-Gate is complete its share leaves the wheel, and the solo gates keep 2.17% each
- **Guarantee**: After 24 spins in a row without a part the chance rises with every spin, and after 47 the next spin always finds one. A part of any gate starts the count again
- **Lives**: 3 in an attempt; every death costs one
- **Countdown**: 5 s before every wave, the first and the boss's too. A wave has no timer, and neither has a run
- **Arena**: Open space of 8,000 × 6,000 units with no rocks, and you are alone in it. A world has 16 of them, and when all are busy you cannot go in
- **Aliens at once**: At most 60 of a wave are alive at once, and 250 in an optional wave. The rest wait for room
- **Bosses**: A boss cannot be hurt for 3 s when it changes phase
- **Thulium cap**: A gate pays back no more than 50% of the Thulium you spent on spins. The rest is cut, and the result says how much

<!-- solo-glance:end -->

## Finding gate parts

Open the **Galaxy Gates** page and spin the Energy Materializer. Every spin is paid in Thulium and finds at most one part, and the part belongs to one of the six gates, picked by chance. You need a number of parts of a gate to open it, and the parts are yours until you use them. A spin that finds no part is not lost: it pays a prize ([below](#a-spin-without-a-part)). Every spin is charged, a complete Chrono-Gate's too. When the Chrono-Gate is complete its share of the spins finds nothing, and the solo gates keep their own chance, so a part of a solo gate costs the same with or without it.

The table gives the cost of each gate in parts and what they cost on average **with the guarantee** (a spin is a lottery, so a lucky pilot pays less and an unlucky one more, up to the longest run of spins the guarantee allows).

<!-- solo-parts:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Gate | Parts to complete it | Chance of a part per spin | Spins on average | Thulium on average |
| :--- | ---: | ---: | ---: | ---: |
| **Chrono-Gate** | 2 | 2.17% | 91 | 9,093 |
| **Alpha Rift** | 11 | 2.17% | 500 | 50,011 |
| **Beta Breach** | 26 | 2.17% | 1,182 | 118,208 |
| **Gamma Foundry** | 54 | 2.17% | 2,455 | 245,508 |
| **Delta Siege** | 87 | 2.17% | 3,955 | 395,541 |
| **Omega Vault** | 108 | 2.17% | 4,910 | 491,017 |

<!-- solo-parts:end -->

The parts of the Chrono-Gate go back to nothing at the wipe, and you find them again every season. **The parts of the solo gates stay**, and so do the guarantee's count and the record of what you spent on spins and what the gates paid back; the wipe takes none of them ([Gates and the wipe](#gates-and-the-wipe)).

### A spin without a part

Most spins find no part. Each of them pays one prize, picked by the chances below: laser ammo of the second multiplier or better, a rocket stack of the second or third tier, and now and then a [special item](/wiki/06-Items/Special-Items.md) or a [container](/wiki/06-Items/Containers.md). A prize that cannot be given (you already hold the most of that special item, say) becomes a stack of ammo or rockets by the same roll, so a spin never pays less than its table. The prize is worth clearly less than the spin costs: the gates are a Thulium sink.

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

You enter from the Galaxy Gates page, and only when:

- you have the parts of the gate: they are taken **once, when you first go in**, and a refused entry takes nothing;
- you are flying a ship, not in a jump or a CPU channel, not in combat and not in a Danger Sector, and you are on the home server (the regional servers have no gates);
- you have no other solo run open: you have one run at a time, and a run that you left is resumed or abandoned before another begins;
- a rift is free in your world. Each world has a number of them, and when all are busy you wait.

You land in the middle of an empty arena, alone. Nobody can attack you in it, and the Jump and Base CPUs do not work.

## How a run goes

1. **A countdown comes before every wave**, the first and the boss's too. A wave has no timer, and neither has the run: it takes as long as you need.
2. **A wave** appears on a ring round you and flies at you, at the pace of the gate. Only so many of it are alive at once, and the rest wait for room. It ends when its last alien is dead.
3. **Your progress is saved after every wave.** If you leave, a wave that was on begins again whole when you come back.
4. **An optional wave** is a huge wave of Seekers, and Delta Siege and Omega Vault have one each. During its countdown you may skip it: it then counts as done, and it pays **nothing**. If you fight it, its kills pay like the kills of any wave.
5. **The last wave is the boss.** It changes phase as its hull falls, and it cannot be hurt for a moment at every change. When the boss dies the run is cleared, and the clear is paid at once.

**Lives.** A death costs one life and sends you to your base like any other death; the run waits for you, with no clock running. **Resume** takes you back in at the saved wave with the lives you have left, and it asks for no new parts. When your last life is gone the attempt ends but the run stays open at the last cleared wave, and Resume refills your lives. **Leave**, a log-off or a change of world pauses the run without costing a life. A restart of the server keeps your run open too. **Abandon** gives the run up: its parts are gone, and the aliens you killed are paid as they stand. Resume works only from a flying ship: after a death its button on the result screen waits, with a line that says why, until you have respawned. A respawned ship returns with a capped hull, so when your hull is under half the result screen warns you; Resume still puts you back as you are. The repair ships at your base mend you inside their aura.

Every world fights the same gate: the aliens' strength and pay do not depend on the world you fly in.

### The waves

The aliens are the ones of the game (the Seeker, the Phantasm, the Bulwark, the Goombah and the Crystalys), made harder or softer by the gate. The planned time is what the gate is built to take a pilot at the starting level of Laser tech ([Pilot Skills](/wiki/03-Mechanics/Pilot-Skills.md)); a pilot who has levelled up Laser tech finishes sooner.

<!-- solo-waves:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Gate | Waves, the boss's included | Aliens in the waves | Boss | Planned time |
| :--- | ---: | :--- | :--- | :--- |
| **Alpha Rift** | 10 | 60 Seeker, 160 Phantasm | Enhanced Phantasm | 10 to 15 min |
| **Beta Breach** | 14 | 80 Seeker, 180 Phantasm, 80 Bulwark, 20 Goombah | Enhanced Bulwark | 15 to 25 min |
| **Gamma Foundry** | 18 | 100 Phantasm, 120 Bulwark, 100 Goombah, 8 Crystalys | Elite Crystalys | 25 to 35 min |
| **Delta Siege** | 22 | 250 Seeker, 200 Phantasm, 180 Bulwark, 140 Goombah, 15 Crystalys | Siege Construct | 35 to 45 min |
| **Omega Vault** | 26 | 250 Seeker, 250 Phantasm, 200 Bulwark, 200 Goombah, 25 Crystalys | Omega Guardian | 50 to 60 min |

- **Delta Siege**: wave 18 (250 Seeker) is optional: you may skip it while its countdown runs, and it pays nothing
- **Omega Vault**: wave 17 (250 Seeker) is optional: you may skip it while its countdown runs, and it pays nothing; waves 22 to 24 are elite, with ×1.5 the hull, shield and damage

<!-- solo-waves:end -->

### The bosses

A boss is an alien's ship made larger, with a hull, a shield and a volley of its own, which no setting of the gate or the world changes. A phase begins when the boss's hull falls to the figure in the table: its shield may be set again, its volley or all its damage change, and it may start a move. Every move is announced: a circle, a ring or a mark on your ship shows a moment before it lands. The aliens that a boss calls pay and drop nothing.

<!-- solo-bosses:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Boss | Gate | Hull | Shield | Laser volley |
| :--- | :--- | ---: | ---: | ---: |
| **Enhanced Phantasm** | Alpha Rift | 330,000 | 530,000 | 5,700–7,000 |
| **Enhanced Bulwark** | Beta Breach | 690,000 | 170,000 | 4,500–5,500 |
| **Elite Crystalys** | Gamma Foundry | 620,000 | 250,000 | 3,800–4,700 |
| **Siege Construct** | Delta Siege | 1,150,000 | 1,730,000 | 3,400–4,200 |
| **Omega Guardian** | Omega Vault | 1,340,000 | 840,000 | 2,600–3,200 |

| Boss | Phase | Hull left | What it does |
| :--- | :--- | :--- | :--- |
| **Enhanced Phantasm** | Enhanced Phantasm | 100% to 0% | It only shoots. |
| **Enhanced Bulwark** | Shielded | 100% to 50% | Its shield is set to ×4 of the boss's own. |
|  | Second attack | 50% to 0% | Its volley is ×1.3. It fires 4 Dormant Lance rockets at you, 61,000 each, one every 0.5 s, in a barrage every 30 s. |
| **Elite Crystalys** | Elite | 100% to 50% | It only shoots. |
|  | Reinforced | 50% to 0% | Its shield is set to ×2 of the boss's own. Every 10 min it calls 10 Goombah, at most 10 of them alive; they pay and drop nothing. |
| **Siege Construct** | Siege Construct | 100% to 0% | Every 1 min it drops 3 volleys of 8 meteors, 5,500 each to everything within 420 units of where it lands, 50% of them aimed at you; each circle shows 3 s before it lands. It fires 6 Dormant Lance rockets at you, 9,000 each, one every 0.5 s, in a barrage every 1 min. |
| **Omega Guardian** | Shield Fortress | 100% to 70% | Its shield is set to ×1.5 of the boss's own. Every 40 s it calls 6 Bulwark, at most 12 of them alive; they pay and drop nothing. |
|  | Swarm Protocol | 70% to 35% | Every 25 s it calls 12 Phantasm, at most 24 of them alive; they pay and drop nothing. Every 30 s a blast of 140,000 hits everything within 700 units of the boss; the ring shows 2 s before it lands. |
|  | Overload | 35% to 0% | Its shield is set to ×0.1 of the boss's own. All its damage is ×2.5. After 2 min in the phase all its damage is ×2 more. Every 25 s a blast of 28,000 hits everything within 700 units of the boss; the ring shows 2 s before it lands. |

<!-- solo-bosses:end -->

## What a clear pays

A clear pays its table **once**, in one go, the moment the boss dies: the Credits, the Thulium, the experience and the honor, the ore, plates and Power Cores, and the ammo. The experience counts for your PvE ranking points, as a dungeon's does.

<!-- solo-pay:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Gate | Credits | Thulium | XP | Honor |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 450,000 | 5,000 | 70,000 | 1,000 |
| **Beta Breach** | 1,500,000 | 12,000 | 180,000 | 2,500 |
| **Gamma Foundry** | 4,000,000 | 25,000 | 400,000 | 5,500 |
| **Delta Siege** | 8,000,000 | 40,000 | 800,000 | 10,000 |
| **Omega Vault** | 15,000,000 | 60,000 | 1,500,000 | 20,000 |

- **Alpha Rift**: Ship Fragment ×300, Nyxite ×300, Daraxium ×400; ammo: Advanced Plasma ×20,000, Ultra Core ×5,000
- **Beta Breach**: Ship Fragment ×700, Nyxite ×750, Daraxium ×800, Cataclysite ×400, Quorvium ×100; ammo: Advanced Plasma ×50,000, Ultra Core ×20,000, Experimental Fusion Core ×3,000
- **Gamma Foundry**: Ship Fragment ×1,150, Nyxite ×1,000, Cataclysite ×900, Quorvium ×400, Power Core ×15; ammo: Advanced Plasma ×30,000, Ultra Core ×60,000, Experimental Fusion Core ×20,000
- **Delta Siege**: Ship Fragment ×2,000, Nyxite ×1,750, Cataclysite ×1,500, Quorvium ×1,000, Reinforced Hull Plate ×70, Power Core ×40, Ancient Control Unit ×3; ammo: Advanced Plasma ×40,000, Ultra Core ×90,000, Experimental Fusion Core ×50,000
- **Omega Vault**: Ship Fragment ×3,250, Nyxite ×2,750, Cataclysite ×2,250, Quorvium ×1,600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10; ammo: Advanced Plasma ×50,000, Ultra Core ×100,000, Experimental Fusion Core ×85,000

<!-- solo-pay:end -->

**The Thulium is cut to a cap.** The gates may pay back no more than a share of the Thulium you spent on spins, counted over all your gates and all your spins (the share is in the list at the top). What a clear and its aliens would pay above that is cut, and the result screen says how much. Credits, experience, honor, ore, plates and ammo are never cut.

### The aliens

Every alien you kill in a gate pays, at the figures it has in Alpha whichever world you fly in: no world multiplier, no booster and no Premium bonus changes them. A wave pays for its aliens **once** for a run, however often you leave and come back. The pay comes with the end of each stretch of the run: when you leave, die, run out of lives, abandon or clear it. The kills of a stretch go unpaid only in the wipe and in a restart of the server while you are inside (your run stays open, but the kills of that stretch are lost). The kills of a gate count for nothing else: not for the missions, the kill statistics, the achievements' counters, the kill feed or the experience of your drones and P.E.T.s. The experience they pay does count for your PvE ranking points, as the experience of a clear does. The loot of the aliens comes with the pay, straight into your inventory.

<!-- solo-kills:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Alien | Credits | Thulium | XP | Honor |
| :--- | ---: | ---: | ---: | ---: |
| **Seeker** | 1,000 | 4 | 100 | 2 |
| **Phantasm** | 3,000 | 12 | 300 | 6 |
| **Bulwark** | 5,000 | 25 | 800 | 10 |
| **Goombah** | 15,000 | 75 | 3,000 | 24 |
| **Crystalys** | 75,000 | 200 | 12,000 | 52 |

| Gate | Credits | Thulium | XP | Honor |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 540,000 | 2,160 | 54,000 | 1,080 |
| **Beta Breach** | 1,320,000 | 5,980 | 186,000 | 2,520 |
| **Gamma Foundry** | 3,000,000 | 13,300 | 522,000 | 4,616 |
| **Delta Siege** | 4,975,000 | 21,400 | 829,000 | 7,640 |
| **Omega Vault** | 6,875,000 | 29,000 | 1,160,000 | 10,100 |

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
