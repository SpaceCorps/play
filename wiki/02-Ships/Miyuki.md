# Miyuki

The Miyuki is a support ship in five levels. You make level I in Assembly like any other ship, then turn that same ship, in place, into level II, III, IV and V: each level is made from the one below, and everything fitted to the ship stays on it. Every level adds a laser slot and a hull plate slot, and each of those slots is a technology you research.

## Stats

- **Hitpoints (HP)**: 128,000
- **Base Speed**: 250
- **Laser Slots**: 5
- **Extra Slots**: 3
- **Hull Plate Slots**: 5

### Generator & Support Slots

- **Core Slots (100% efficiency)**: 3
- **Support Slots (75% efficiency)**: 3
- **Auxiliary Slots (50% efficiency)**: 2

---

## Price

- **Credits**: 0 (Crafted in Assembly)
- **Thulium**: 0

## Levels

The Stats above are level I. A level above the first is made in Assembly from the Miyuki one level below it: the same ship, turned in place, so its fit and its configurations stay. A level cannot be skipped or bought.

| Level | Hull | Base speed | Lasers | Hull plates | Core / support / auxiliary | Shield capacity | Absorbance |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Miyuki** | 128,000 | 250 | 5 | 5 | 3 / 3 / 2 | – | – |
| **Miyuki II** | 134,400 | 250 | 6 | 6 | 3 / 3 / 2 | +5% | +2% |
| **Miyuki III** | 141,120 | 250 | 7 | 7 | 3 / 3 / 2 | +10.25% | +4.04% |
| **Miyuki IV** | 148,176 | 300 | 8 | 8 | 3 / 3 / 2 | +15.76% | +6.12% |
| **Miyuki V** | 155,585 | 300 | 9 | 9 | 4 / 4 / 4 | +21.55% | +8.24% |

Shield capacity and absorbance are bonuses over level I.

What a level takes in Assembly, besides the Miyuki below it, which is turned into the new level:

| Level | Research | Craft time | Thulium | Materials |
| :--- | :--- | ---: | ---: | :--- |
| **Miyuki** | 1 d, 10 Dark Matter | 15 min | 6,000 | 160 Ship Fragment, 25 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit |
| **Miyuki II** | 1 d, 10 Dark Matter | 10 min | 20,000 | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 8 Dark Matter Plate |
| **Miyuki III** | 1 d, 10 Dark Matter | 10 min | 35,000 | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 1 Ancient Control Unit, 8 Dark Matter Plate |
| **Miyuki IV** | 2 d, 10 Dark Matter | 15 min | 50,000 | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 2 Ancient Control Unit, 8 Dark Matter Plate |
| **Miyuki V** | 2 d, 10 Dark Matter | 15 min | 75,000 | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 3 Ancient Control Unit, 8 Dark Matter Plate |

## Abilities

The Miyuki's abilities belong to the ship, not to an item: they take no ability slot and need nothing fitted. [Ship abilities](/wiki/03-Mechanics/Abilities.md#ship-abilities) says how each works; this table says what each level has.

| Level | Heal Pod | Channel Heal | Channel Shield |
| :--- | :--- | :--- | :--- |
| **Miyuki** | 7.5 s, 20,000 + 2% | – | – |
| **Miyuki II** | 7.5 s, 20,000 + 2% | 50,000 hull a second (you 10,000), 120 s | – |
| **Miyuki III** | 7.5 s, 30,000 + 3% | 50,000 hull a second (you 10,000), 120 s | 150,000 + 3% shield a second (you 30,000 + 3%), 120 s |
| **Miyuki IV** | 7.5 s, 30,000 + 3% | 75,000 hull a second (you 10,000), 100 s | 150,000 + 4% shield a second (you 30,000 + 4%), 120 s |
| **Miyuki V** | 7.5 s, 30,000 + 3% | 75,000 hull a second (you 10,000), 100 s | 150,000 + 5% shield a second (you 30,000 + 5%), 80 s |

A link lasts 5 seconds and reaches a ship of your group or company within 1,200 units. The Heal Pod reaches 600. A Channel Shield also restores a share of each ship's own maximum shield every second on top of its points: 3% on Miyuki III, 4% on IV and 5% on V (the percent in the table).

Your [Healing](/wiki/03-Mechanics/Pilot-Skills.md) pilot skill works on all three: at level 100 it makes the Heal Pod, the Channel Heal and the Channel Shield (its points and its share of the maximum shield) 30% stronger and shortens their waits by 10%, so a Channel Heal that rests 100 seconds rests 90. The tables above give the numbers without it.

## Research

- **Levels.** Miyuki II to V are technologies of their own in the Skylab, each behind the level below: 1 d for II and III, 2 d for IV and V, and 10 Dark Matter each. In the Research view the five levels are drawn one under the other with an arrow from each level to the next: you research II after I, III after II, IV after III and V after IV.
- **Slots.** The hull plate slots, the laser slots from the sixth and the generator slots from the ninth are technologies of their own in the Skylab, 1 h and 10 Dark Matter each: hull plate slots 1 to 9 in order from the first, laser slots 6 to 9 (each behind its level) and generator slots 9 to 12 (each behind level V). A slot opens on the ship, at whatever level it is, as soon as you have researched it; one you have not is shown locked in the Hangar.
- **Hull plate slots.** The Miyuki has 5 [hull plate slots](/wiki/06-Items/Hull-Plating.md#hull-plate-slots) for [Hull Plating](/wiki/06-Items/Hull-Plating.md) at level I and 9 at level V, all locked when you make it. All 9 filled with Hull Plating III add 180,000 hull.

<!-- research-ship:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **Research first.** Assembly makes this ship only after you have researched its technology: 1 d of research and 10 Dark Matter plugged into the Research Centre. The technology is in the [Ships tree](/wiki/03-Mechanics/Research.md#tree-ships) of the [Research](/wiki/03-Mechanics/Research.md) page.
- **More extra slots.** Extra Slots CPU I, II and III, installed in your Skylab, give this ship 3, 5 and 7 more extra slots: 6, 8 and 10 in all with its own 3. You research and make them like any other item: see [Extra Slots CPUs](/wiki/06-Items/Extras.md#extra-slots-cpus).

<!-- research-ship:end -->

## Lore

The Miyuki came out of the Skylab yards as a question: what if the ship that keeps a fleet alive could grow with the pilot who flies her? Every refit keeps her fit and her configurations and adds a little of everything. A Miyuki V is the ship her pilot launched on the first day, grown into a flagship's frame.
