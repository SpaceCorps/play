# Asteroid Mining

**Asteroids** are big rocks that lie in the flight plane of the company sectors and the Danger Sectors. They never move and they never shoot. Break one with **rockets** or **lasers** and it bursts into small **chunks** of Credits, Thulium and ore, which you pick up like [cargo](/wiki/03-Mechanics/Cargo.md). Rockets are the tool for the job: your lasers hurt an asteroid too, but only at 5% of what they do to a ship, and drones do nothing to it.

Mining is a different job from hunting, not a replacement for it: it earns no XP, honor or ranking points, and the rockets you fire cost Credits or Thulium. What it gives you is Credits and Thulium, ore for the [Forge](/wiki/06-Items/Forge.md) and for crafting without a fight, and a job that a [group](/wiki/03-Mechanics/Groups.md) can share. It pays well: by the game's own model an hour at the right asteroids with the right rocket earns about 2.6 to 6.8 times the best hunting hour of your level, once the rockets are paid for. The daily limits of [The worlds](#the-worlds) cap it, and you reach them soon: in Alpha, a steady miner on a good sector reaches the Thulium limit in under 2 hours and the Credits limit in about 2.7 hours.

## What an asteroid is

- **At the level of the ships.** An asteroid lies in the flight plane, behind every ship, rocket and chunk that passes over it, and it stays where it is. Nothing collides with it: ships, aliens and rockets fly through it. Each asteroid is drawn in its real proportions, so the Motherlode and the Prism Cluster stand tall instead of lying flat. The dim rocks far behind the map are scenery: you cannot hit them and they hold nothing.
- **A kind and a family.** Every asteroid is one of the kinds in [The kinds](#the-kinds), and each kind belongs to a family that says what it is like. The glow of an asteroid says what is inside it. A **single ring** on the ground marks an ordinary asteroid, a **double ring** an armoured one and a **dashed ring** a brittle one.
- **On the minimap.** Every asteroid of the sector is a small hexagon in its kind's colour, hollow until it is hit and filled after; the chunks are small round dots.
- **The Target window.** Click an asteroid to select it. The circle on a selected asteroid stays on it while you fly around it: a click on empty space, or just beside the asteroid, only flies your ship, and Esc or the cross in the Target window lets go. The window shows its name, family and size, its hull, the badges **Armour** and **Blasts**, about how many of the rocket you hold it takes and about how many volleys of your lasers, what it breaks into in your world, and who has dealt how much of the damage. Selecting an asteroid does not change your ship or alien target, so your lasers keep their lock.

## Breaking one

1. **Aim at it.** Click the asteroid to select it: your rockets then go at it. A straight rocket (Rivet, Scatter) goes at an asteroid under your cursor instead, if no ship or alien is under it too (a short way outside the asteroid's edge counts, and so does its hexagon on the minimap). With no asteroid selected, a guided rocket (Lancet, Ember) goes at an asteroid under the cursor only when you have no ship or alien selected, so a hunter fighting beside an asteroid keeps shooting at the alien. A rocket that has no asteroid to go at is an ordinary rocket and flies through every asteroid.
2. **Fire.** Any of the twelve [rockets](/wiki/06-Items/Rockets.md#the-twelve-rockets) of the Shop works, and so does the N.U.K.E. A guided rocket needs the asteroid inside its lock range and a straight one inside its flight range, measured to the asteroid's centre. Either kind flies to the centre, so it does not matter where on the asteroid the cursor is. The [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) cannot hurt an asteroid.
3. **Keep firing.** All rockets share the one recharge timer, and every rocket costs what it costs: the rocket is the price of the job.

- **A rocket hits only the asteroid it is fired at.** It flies through every other asteroid and every ship on the way, and a rocket that was not fired at an asteroid flies through all of them. When a rocket of yours ends beside an asteroid it was not aimed at, the game tells you why. The blast of an area rocket still hurts any ship it reaches, as everywhere; the other asteroids in it take nothing.
- **Lasers hurt a little; drones do nothing.** Select the asteroid, then double-click it, press the attack key or press an ammo slot: your lasers fire at it once a second while its centre is inside your laser range, and use ammo as they do at a ship. A double click always fires at the asteroid; the attack key and the ammo slots do when no ship or alien is selected. Siphon ammo drains shields and nothing else, so it cannot hurt an asteroid and that order is refused.
- **Damage.** A rocket takes its own roll off the asteroid's hull, and your [drone formation](/wiki/03-Mechanics/Formations.md)'s rocket bonus counts as it does against a ship (a Ballista's +55% too); your lasers, amps, boosters and ammo do not change a rocket's roll. A laser volley takes 5% of what it would do to a ship with no shield, with your amps, boosters, ammo, critical hits and formation counted. The bonus comes first: an **armoured** asteroid takes the armour's points off every hit after it, and an area blast does more to a **brittle** crystal one (the numbers are in The rules and The kinds). An asteroid has no shield and never heals: a rock you whittled down stays whittled until somebody breaks it.
- **How many.** Each kind is made for one rocket, and The kinds says about how many of it a break takes; the Target window and the hover card say it for the rocket in your hand, and, next to it, about how many volleys of your lasers it takes. A stronger world means a bigger hull (The worlds). A rocket of yours in flight when somebody else breaks the asteroid flies on as an ordinary rocket and is lost.

## What a break leaves

Nothing is paid when an asteroid breaks. It bursts into rubble and throws a few **chunks**: small gold nuggets for Credits, lavender crystals for Thulium and a rough stone for the ore. They drift out of the rubble and bob like any [crate](/wiki/03-Mechanics/Cargo.md): click one, your ship flies to it and the pickup takes its short channel, as for any crate ([collecting](/wiki/03-Mechanics/Cargo.md#collecting)). The ore goes to your Hangar inventory, the Credits and Thulium to your wallet, and a toast tells you what you got.

A bigger asteroid leaves more pieces (the Cash chunks column of The kinds: the Credits and the Thulium come in that many pieces, and the ore in one more). After a pickup your ship goes on by itself to the next chunk of an asteroid that is close by and yours to take; any move order of yours stops it.

## Who gets the chunks

An asteroid is shared work: any number of pilots can hit one, with rockets or lasers, and the chunks go by the damage each dealt, not by who fires first or last. The Target window's damage line shows who has dealt how much, and what was dealt before you came. The Credits and Thulium of a break are rolled once and split by damage; the ore is shared out between the pilots who dealt the most; the rare finds go to the one who dealt the most. A pilot who dealt less than the share in The rules gets nothing, and the Game Log says so. The chunks are laid for each pilot paid, and they are kept for that pilot and its clan for a while, then free for everyone.

## The rules

<!-- asteroids-rules:begin -->
<!-- Generated from server/Resources/Asteroids.json (and Rockets.json) by scripts/asteroids-wiki.sh: don't edit by hand. -->

- A pilot who dealt at least 5% of the damage done to an asteroid gets a share of its chunks, in proportion to the damage dealt. When nobody reaches 5%, the pilot who dealt the most gets all of them.
- A [group](/wiki/03-Mechanics/Groups.md#sharing-kills) counts as one pilot, and its part is split by level between the group mates who are close and shooting.
- The chunks of a break are kept for the pilot they were laid for, and that pilot's clan, for 30 s. After that anyone on the map can take them. A chunk nobody takes is gone after 3 min.
- A map holds at most 36 chunks, inside the 64 crates it can hold: chunks never push the aliens' crates out, and those never push a chunk out. When the map has no room for a chunk, the pilot it was for is paid at once.
- Credits and Thulium are paid when a chunk is collected, not when the asteroid breaks. Over any 24 h a pilot is paid at most the limits of [The worlds](#the-worlds): a chunk over the limit is used up and pays only what is left under it, and the Game Log says so.
- The pay is the same for everybody: no Premium bonus, Season Store boost, clan boost, Loot Luck or booster changes the Credits, the Thulium or the finds. The [Resource Magnet Booster](/wiki/06-Items/Boosters.md) adds to the resources of an ore chunk when you collect it, as it does to any crate.
- Armour takes its points off every hit, but at least 20% of a hit always gets through.
- An area blast does 1.6 times as much to a brittle asteroid as to any other.
- An asteroid never stands within 1,500 units of the edge of a safe ring, 4,200 units of the black hole's centre or 600 units of the map's edge, and it never appears within 1,200 units of a pilot.
- After a break, an asteroid of the same kind grows back somewhere else on the map after the time in the sector's row, give or take 25%.
- The Motherlode comes back after 1 h, whatever the sector.

<!-- asteroids-rules:end -->

## The worlds

Each world, Alpha, Beta and Gamma, has asteroids of its own in the same places ([Worlds](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)), so the asteroid you break in your world is not broken in another. A bigger world means a bigger hull and a bigger pay.

<!-- asteroids-worlds:begin -->
<!-- Generated from server/Resources/Asteroids.json (and Rockets.json) by scripts/asteroids-wiki.sh: don't edit by hand. -->

| World | Hull | Pay | Thulium limit | Credits limit |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha** | ×1 | ×1 | 3,000 | 13,000,000 |
| **Beta** | ×1.5 | ×2 | 4,500 | 18,000,000 |
| **Gamma** | ×2 | ×3 | 6,000 | 21,000,000 |

The tables below give the numbers of an Alpha asteroid. **Hull** is the world's factor on every asteroid's hull and **Pay** its factor on the Credits and Thulium of a break; the ore and the rare finds are the same in every world. The two limits are the most one pilot is paid by chunks over any 24 h.

<!-- asteroids-worlds:end -->

## Where they are

Every sector of the three companies' home sectors and of the Danger Sectors has asteroids, in a mix of its own: mostly the kinds of its ring, with a guest or two from the next ring up or down. The neutral sectors, which no gate leads to, have none. The asteroids of the Danger Sectors appear from the season day in the table, the day PvP opens ([First Contact](/wiki/03-Mechanics/Wipe-Timeline.md)), and the others from the first day. After a break, a new asteroid of the same kind grows back after the time of the sector's row. From season day 11 no asteroid lies near a pulsar, a giant excavator or the middle of the Dormant Swamp ([Danger Sectors](/wiki/01-General/Danger-Sectors.md#where-everything-is)), and a rock that stood there when event 2 began is gone.

<!-- asteroids-maps:begin -->
<!-- Generated from server/Resources/Asteroids.json (and Rockets.json) by scripts/asteroids-wiki.sh: don't edit by hand. -->

| Sector | Asteroids | From day | Comes back | Kinds |
| :--- | ---: | ---: | ---: | :--- |
| `M-1` | 12 | 1 | 2 min | 3 × Pebble, 3 × Cobble, 2 × Glimmer, 2 × Cache Pod, 2 × Ironhide |
| `T-1` | 12 | 1 | 2 min | 3 × Rime, 3 × Cache Pod, 2 × Cobble, 2 × Pebble, 2 × Dark Chondrite |
| `G-1` | 12 | 1 | 2 min | 4 × Glimmer, 2 × Pebble, 2 × Rime, 2 × Cobble, 2 × Nyx Geode |
| `M-2` | 14 | 1 | 3 min | 4 × Ironhide, 3 × Dark Chondrite, 3 × Scrap Hulk, 2 × Vein Rock, 1 × Cobble, 1 × Pebble |
| `T-2` | 14 | 1 | 3 min | 4 × Scrap Hulk, 3 × Dark Chondrite, 3 × Vein Rock, 2 × Nyx Geode, 2 × Rime |
| `G-2` | 14 | 1 | 3 min | 4 × Nyx Geode, 3 × Vein Rock, 3 × Dark Chondrite, 2 × Ironhide, 2 × Glimmer |
| `M-3` | 16 | 1 | 5 min | 3 × Plateback, 3 × Slag Block, 3 × Lode Rock, 3 × Cataclast, 2 × Derelict Hulk, 2 × Cataclysite Mass |
| `T-3` | 16 | 1 | 5 min | 3 × Derelict Hulk, 3 × Slag Block, 3 × Cataclast, 3 × Lode Rock, 2 × Thulium Geode, 2 × Derelict Cruiser |
| `G-3` | 16 | 1 | 5 min | 4 × Cataclast, 3 × Slag Block, 3 × Thulium Geode, 2 × Plateback, 2 × Lode Rock, 2 × Quorvium Boulder |
| `M-4` | 18 | 1 | 5 min | 4 × Anvil, 4 × Cataclysite Mass, 4 × Quorvium Boulder, 2 × Derelict Cruiser, 2 × Vault Rock, 2 × Plateback |
| `T-4` | 18 | 1 | 5 min | 4 × Derelict Cruiser, 4 × Quorvium Boulder, 4 × Cataclysite Mass, 2 × Thulium Cluster, 2 × Vault Rock, 2 × Thulium Geode |
| `G-4` | 18 | 1 | 5 min | 5 × Quorvium Boulder, 3 × Cataclysite Mass, 3 × Anvil, 3 × Lode Rock, 2 × Thulium Cluster, 2 × Vault Rock |
| `DS-1` | 24 | 4 | 5 min | 8 × Rich Lode, 6 × Prism Cluster, 4 × Ancient Husk, 3 × Star Crystal, 2 × Vault Rock, 1 × Motherlode |
| `DS-2` | 24 | 4 | 5 min | 7 × Rich Lode, 7 × Ancient Husk, 3 × Star Crystal, 3 × Anvil, 3 × Derelict Cruiser, 1 × Motherlode |
| `DS-3` | 24 | 4 | 5 min | 9 × Prism Cluster, 5 × Rich Lode, 4 × Star Crystal, 3 × Quorvium Boulder, 2 × Cataclysite Mass, 1 × Motherlode |
| `DS-4` | 24 | 4 | 5 min | 9 × Rich Lode, 5 × Prism Cluster, 4 × Ancient Husk, 3 × Cataclysite Mass, 2 × Derelict Cruiser, 1 × Motherlode |

<!-- asteroids-maps:end -->

## The kinds

<!-- asteroids-kinds:begin -->
<!-- Generated from server/Resources/Asteroids.json (and Rockets.json) by scripts/asteroids-wiki.sh: don't edit by hand. -->

There are 27 kinds of asteroid, in 8 families. **Made for** names the rocket a kind is balanced for and about how many of it a break takes in Alpha. **Finds** are the ore and rare finds a break rolls, which its chunks share out: a percentage is the chance of that line, the other lines are always found. The Credits and the Thulium are the Alpha amounts of a break.

### Stone

Plain rock: no armour and no weak spot.

| Kind | Hull | Size | Special | Cash chunks | Made for | Credits | Thulium | Finds | Found in |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Pebble** | 8,500 | Tiny | – | 1 | About 4× [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 6,600–11,100 | 22% for 3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3 (49%) | `M-1`, `T-1`, `G-1`, `M-2` |
| **Cobble** | 10,000 | Small | – | 1 | About 5× [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 6,300–10,500 | 25% for 3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–9 (89%) | `M-1`, `T-1`, `G-1`, `M-2` |
| **Dark Chondrite** | 12,000 | Small | – | 1 | About 3× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 7,050–11,850 | 65% for 3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–12 (91%), [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (93%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `T-1`, `M-2`, `T-2`, `G-2` |
| **Vein Rock** | 18,000 | Small | – | 1 | About 4× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 13,350–22,200 | 50% for 3–9 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–6 (73%), [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (45%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `M-2`, `T-2`, `G-2` |
| **Slag Block** | 24,000 | Medium | – | 2 | About 5× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 18,600–31,050 | 50% for 3–9 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (95%), [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 3–6 (84%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1.5%) | `M-3`, `T-3`, `G-3` |
| **Cataclast** | 36,000 | Medium | – | 2 | About 8× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 22,350–37,200 | 50% for 6–15 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 9–18, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–24; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1.5%) | `M-3`, `T-3`, `G-3` |
| **Lode Rock** | 52,000 | Medium | – | 2 | About 11× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 34,950–58,200 | 50% for 18–39 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 9–18, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–24; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1.5%) | `M-3`, `T-3`, `G-3`, `G-4` |
| **Cataclysite Mass** | 72,000 | Large | – | 2 | About 10× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 44,700–74,550 | 50% for 21–45 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 15–30, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 9–15; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `M-3`, `M-4`, `T-4`, `G-4`, `DS-3`, `DS-4` |
| **Rich Lode** | 80,000 | Large | – | 3 | About 11× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 61,800–103,050 | 50% for 39–90 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–24, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 6–12; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (8%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (5%) | `DS-1`, `DS-2`, `DS-3`, `DS-4` |

### Ice

Frozen rock: no armour and no weak spot.

| Kind | Hull | Size | Special | Cash chunks | Made for | Credits | Thulium | Finds | Found in |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Rime** | 12,000 | Small | – | 1 | About 5× [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 8,250–13,800 | 55% for 3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–9 (77%) | `T-1`, `G-1`, `T-2` |

### Crystal

Brittle: an area blast does more to a crystal asteroid than a direct hit does.

| Kind | Hull | Size | Special | Cash chunks | Made for | Credits | Thulium | Finds | Found in |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Glimmer** | 9,000 | Tiny | Blasts ×1.6 | 1 | About 4× [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 6,150–10,350 | 41% for 3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–6 (77%) | `M-1`, `G-1`, `G-2` |
| **Nyx Geode** | 26,000 | Medium | Blasts ×1.6 | 2 | About 6× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 16,650–27,750 | 50% for 9–21 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 6–15, [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3–6 (96%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `G-1`, `T-2`, `G-2` |
| **Quorvium Boulder** | 48,000 | Medium | Blasts ×1.6 | 2 | About 7× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 29,850–49,650 | 50% for 12–30 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–21, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 3–15 (86%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `G-3`, `M-4`, `T-4`, `G-4`, `DS-3` |
| **Prism Cluster** | 100,000 | Large | Blasts ×1.6 | 3 | About 14× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 71,700–119,550 | 50% for 27–60 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 24–42, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 12–21; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (8%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (5%) | `DS-1`, `DS-3`, `DS-4` |

### Salvage

Wrecks and pods: they hold Ship Fragments.

| Kind | Hull | Size | Special | Cash chunks | Made for | Credits | Thulium | Finds | Found in |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Cache Pod** | 14,000 | Tiny | – | 1 | About 6× [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 9,000–15,000 | 29% for 3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–6 (83%), [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 3–9 (78%) | `M-1`, `T-1` |
| **Scrap Hulk** | 20,000 | Small | – | 1 | About 5× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 12,150–20,250 | 92% for 3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–9 (95%), [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (77%), [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 6–12; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `M-2`, `T-2` |
| **Derelict Hulk** | 52,000 | Medium | – | 2 | About 11× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 33,150–55,200 | 50% for 9–18 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 6–12, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 9–18, [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 30–54; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1.5%) | `M-3`, `T-3` |
| **Derelict Cruiser** | 72,000 | Large | – | 2 | About 10× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 46,200–76,950 | 50% for 18–39 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 9–15, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 3–9 (97%), [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 21–36; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `T-3`, `M-4`, `T-4`, `DS-2`, `DS-4` |

### Iron

Armoured: every hit loses points to the armour, so they ask for stronger rockets than their hull suggests.

| Kind | Hull | Size | Special | Cash chunks | Made for | Credits | Thulium | Finds | Found in |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Ironhide** | 14,000 | Small | Armour 500 | 1 | About 4× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 13,650–22,650 | 50% for 3–9 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–6 (74%), [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (46%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `M-1`, `M-2`, `G-2` |
| **Plateback** | 36,000 | Medium | Armour 1,500 | 2 | About 11× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 31,650–52,800 | 50% for 9–18 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 6–12, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 9–15, [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 27–51; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1.5%) | `M-3`, `G-3`, `M-4` |
| **Anvil** | 80,000 | Large | Armour 3,000 | 2 | About 18× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 84,900–141,450 | 50% for 30–72 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 15–27, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 6–15, [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 36–69; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `M-4`, `G-4`, `DS-2` |

### Treasure

The best payers: each pays more Credits and Thulium than the average asteroid of its ring.

| Kind | Hull | Size | Special | Cash chunks | Made for | Credits | Thulium | Finds | Found in |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Thulium Geode** | 66,000 | Medium | Blasts ×1.6 | 2 | About 14× [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 42,450–70,800 | 18–42 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 9–15, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–21; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1.5%) | `T-3`, `G-3`, `T-4` |
| **Thulium Cluster** | 100,000 | Large | – | 2 | About 14× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 62,100–103,500 | 42–99 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–21, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 3–15 (90%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `T-4`, `G-4` |
| **Vault Rock** | 130,000 | Large | – | 3 | About 18× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 101,400–169,050 | 50% for 36–87 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 9–18, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 3–12 (90%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `M-4`, `T-4`, `G-4`, `DS-1` |
| **Star Crystal** | 150,000 | Large | Blasts ×1.6 | 3 | About 21× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 109,650–182,700 | 60–141 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 18–33, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 9–15; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (8%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (5%) | `DS-1`, `DS-2`, `DS-3` |

### Relic

The shell of a dead swarm ship: armoured, and rich in rare finds.

| Kind | Hull | Size | Special | Cash chunks | Made for | Credits | Thulium | Finds | Found in |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Ancient Husk** | 120,000 | Large | Armour 2,000 | 3 | About 22× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 114,300–190,350 | 50% for 57–129 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 24–45, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 12–24; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (16%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (10%) | `DS-1`, `DS-2`, `DS-4` |

### Titan

The biggest of all, a rock for a group.

| Kind | Hull | Size | Special | Cash chunks | Made for | Credits | Thulium | Finds | Found in |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Motherlode** | 450,000 | Huge | – | 3 | About 61× [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 348,900–581,400 | 165–381 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 69–126, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 36–66; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (8%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (5%) | `DS-1`, `DS-2`, `DS-3`, `DS-4` |

<!-- asteroids-kinds:end -->

## What it does not give

An asteroid is no kill. Breaking one gives no XP, no honor, no kill count, no PvE or PvP points, no ranking, no [Wipe Points](/wiki/03-Mechanics/Wipe-Timeline.md#earning-wipe-points), no drone XP and no progress on a [mission](/wiki/03-Mechanics/Quests.md), except the [Asteroids mission of each level](/wiki/03-Mechanics/Quests.md#levels). The Season Store's boosts do not touch it either. What it gives is what is in the tables: Credits, Thulium and ore, which the [Resources](/wiki/06-Items/Resources.md) page lists with the aliens' drops.

## Tips

- **Start with the rocket the kind is made for.** A weaker rocket breaks the asteroid too, but it takes more rockets and more of the timer. A stronger one is faster, but what a hit deals beyond the hull that is left is lost, and a rocket costs the same whatever it hits.
- **Bring blasts for crystal and strength for iron.** A Scatter or an Ember is the rocket for a brittle asteroid, and an armoured one asks for a stronger rocket than its hull suggests, because the armour takes its points off every hit.
- **Let your lasers work between the rockets.** They fire once a second and cost ammo, not rockets, but a volley does only 5% of what it does to a ship: they add to the rockets and do not replace them.
- **Mind the daily limit.** Chunks pay no more once you have collected the limit of your world over a day, and mining pays so well that you reach it within a few hours; the limit is in The worlds.
- **Break the big ones together.** The Motherlode is a rock for a group: a group counts as one pilot and its part is split by level between the group mates who are close and shooting.
- **Keep an eye on the sector.** Asteroids do not fight back, but the sectors around them still hold aliens and, in the Danger Sectors, other pilots.
