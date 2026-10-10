# Shield Mechanics

Shields absorb the majority of incoming damage, protecting your ship's hull from direct damage.

## Shield Calculations

Your ship's final shield parameters are calculated as follows:

\[\text{Final Shield Capacity} = \text{Total Base Capacity} \times (1.0 + \text{Total Shield Bonus Percent})\]
\[\text{Final Shield Recharge Rate} = \text{Total Base Recharge} \times (1.0 + \text{Total Shield Bonus Percent})\]

### 1. Slot Efficiency & Diminishing Returns

Similar to engines, equipped shields (and hybrid generators) are ranked best first and subjected to slot efficiency (Core: 100%, Support: 75%, Auxiliary: 50%, a drone's slot: 100%, as a core slot) and a diminishing returns curve based on their rank. A shield is ranked by what of it counts: its capacity times its slot's share. The recharge has its own order (its value times the slot's share), and the **four best** shield bonuses count. A shield on one of your [drones](/wiki/03-Mechanics/Drones.md) is ranked with the ship's own:

- **1st to 4th shield**: **100%** (1.0) marginal efficiency.
- **5th shield**: **85%** (0.85) marginal efficiency.
- **6th shield**: **70%** (0.70) marginal efficiency.
- **7th shield**: **55%** (0.55) marginal efficiency.
- **8th and beyond**: **50%** (0.50) marginal efficiency. (Up to version 0.4.7 this was 25%, the same as engines; engines still use 25%, see [Speed](/wiki/03-Mechanics/Speed.md).)

**Fitting more never lowers your shield.** Adding a shield or a shield cell never lowers your shield capacity or your recharge: every number is ranked best first by what counts, so a new piece takes the place it earns. Absorbance is the average of your shields, so a new shield weaker than your average lowers it; a cell never does.

**The Hangar shows it.** A shield, engine or Adaptive Core that counts for less than all of its strength wears a small percentage on its slot (for example `64%`: the 5th shield, at 85%, in a support slot, at 75%), and hovering it gives the breakdown. Hover the Shields and Speed tiles of the combat stats to see your items by place and what one more would count for. The Ship window in flight shows the same lists when you hover its shield bar and its speed.

### 2. Shield Absorbance (Damage Split)

Absorbance is the share of every hit your shields take; the rest goes directly to hitpoints (HP).
- **Per shield**: a shield's absorbance plus the absorbance of the Shield Cells fitted into it. A shield alone is **45 to 50%** (Light 45%, Basic 48%, Heavy 50%); cells add 2 to 10 points each (Capacity Shield Cell I to IV +2%, +3%, +4%, +5%; Absorption Shield Cell I to IV +4%, +6%, +8%, +10%).
- **Average Absorbance**: your ship's absorbance is the simple average over the shields in core, support and auxiliary slots and on your drones. Adaptive Cores have no absorbance of their own and don't count in the average (cells in an Adaptive Core add capacity and recharge only). With no shield equipped your absorbance is 0%: the hull takes every hit, and shield points from cells in an Adaptive Core go unused, so fit a shield alongside.
- **The most out of the box is 80%**: the best shield with the best cells, a Heavy Shield Core with three Absorption Shield Cell IVs in every slot. Mixing in weaker shields lowers the average. No Season Store buff and no Forge buff is part of that number.
- **Example**: a Basic Shield Core (48%) with two Absorption Shield Cell Is is 56%; add a Light Shield Core (45%) and the average is 50.5%.
- **The stat is not capped at 100%.** It is what the shields would take of a hit, before the attacker's *shield penetration* is taken off, so a ship can carry more than a whole hit: 112% still takes a whole hit from an attacker with up to 12% penetration.

#### Shield penetration

Some attacks have a **shield penetration**: points taken off your absorbance for that hit. The share your shields take is

\[\text{Shield Share} = \text{clamp}(\text{Absorbance} - \text{Penetration},\ 0,\ 100\%)\]

- The shields take `round(damage x share)` of the hit at most; the hull takes the rest. A shield too low for its share passes the difference to HP, and if shields are at 0, all damage hits HP directly.
- **Where penetration comes from**: a direct rocket's *Shield penetration* (Lancet I 10%, Lancet II 25%, Lancet III 35%, Rivet I 5%, Rivet II 25%, Rivet III 35%, N.I.K.E. 35%; area blasts have none, see [Rockets](/wiki/06-Items/Rockets.md)) and the laser ammo's (Ultra Core 5%, Experimental Fusion Core 10%; see [Lasers & Ammo](/wiki/06-Items/Lasers.md)). Aliens have none, and neither do the x1 and x2 ammo. A laser hit also takes the Penetration Amps of the shooter's lasers (+3% to +12% a slot, the mean over its lasers) and a drone formation's penetration (Gemini +9%, Stiletto +16%); a direct rocket adds the formation's to its own. **Nothing caps the total**: the shields take the absorbance less all of it, down to none of the hit ([how a laser hit adds up](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)).
- **Examples**: 80% absorbance against a Lancet III (35%): the shields take 45% of the hit, the hull 55%. 100% against it: 65% and 35%. 112% against 12% penetration: all of the hit. 45% (a Light Shield Core alone) against 35%: 10% on the shield, the rest on the hull. A rocket on its own penetrates no core completely, but a Lancet III with a Stiletto (35% + 16% = 51%) leaves a Light Shield Core alone (45%) no share of the hit, and so does the best laser (62%): against that laser the best shield (80%) takes 18% of the hit and the hull 82%.
- Aliens have no absorbance stat: they split every hit 80% / 20%, less the penetration of the hit.
- A Siphon Battery's damage comes out of the shield alone: absorbance and penetration do not come into it.

**Where the shields take nothing.** A penetration at or above the absorbance leaves the shields none of the hit: the hull takes all of it. The table shows what the shields take of one hit from the best laser (62%) and from the best direct rocket (a Lancet III or a Rivet III with a Stiletto, 51%):

| Shield | Absorbance | Shields take, best laser (62%) | Shields take, best direct rocket (51%) |
| :--- | ---: | ---: | ---: |
| Light Shield Core | 45% | 0% | 0% |
| Basic Shield Core | 48% | 0% | 0% |
| Heavy Shield Core | 50% | 0% | 0% |
| The best shield out of the box | 80% | 18% | 29% |
| A shield at 100% | 100% | 38% | 49% |
| A shield at 120% | 120% | 58% | 69% |

#### Reaching and passing 100%

- **Out of the box**: at most 80% (above).
- **Shield Absorbance Boost**: a permanent Season Store buff bought with Wipe Points, **+0.1 points per level, at most +10 points** (100 levels, 25 WP each). It adds flat points to your ship's absorbance, the same on any ship with a shield: 80% becomes 80.4% with 4 levels (100 WP), and a Light Shield Core's 45% becomes 46.2% with 12 levels (300 WP). A ship with no shield equipped stays at 0%. The 100 levels cost 2,500 WP, a goal for several wipes: today's sources of Wipe Points (the kill milestones and the missions) pay 855 WP in all at their caps, carried across wipes, and that buys 34 levels, +3.4 points. More sources of Wipe Points are planned. See [Season & Wipe Points](/wiki/03-Mechanics/Wipe-Timeline.md#cross-season-progression-permanent-buffs-).
- **Forge**: shields and shield cells can roll an **Absorbance** buff, which multiplies the stat: +5% on a 50% shield is +2.5 points. A fully forged Eternal best set (core and three cells, every buff rolled at the top, +15%) adds up to 12 points, about 10 on average (see [The Forge](/wiki/06-Items/Forge.md)).
- **Together**: 80% out of the box, +3.4 points of buff (all of today's 855 Wipe Points) and up to +12 points of Forge buffs make **95.4%** at the most today; with every one of the buff's 100 levels (+10 points, 2,500 WP) it would be 102%. Neither the buff nor the Forge alone reaches 100%; getting there is a goal for several wipes, and more sources of Wipe Points are planned.

### Shield Boosts: Capacity, Absorbance, Recharge

Every shield boost raises one of the three stats and is listed under its own kind in the Boosters window:

- **Capacity** (maximum shield points): Shield Wall Booster I and II and the permanent Shield Capacity Boost.
- **Absorbance** (the share of a hit your shields take): the permanent Shield Absorbance Boost (+0.1 points per level, +10 points at most).
- **Recharge** (shield points restored per second): the Shield Regen Booster.

See [Boosters](/wiki/06-Items/Boosters.md) for the numbers.

---

## Shield Passive Regeneration

Shields regenerate passively over time to keep you combat-ready.

- **Regeneration Tick**: If shields are below maximum capacity, they restore shield points equal to your Recharge Rate per second.
- **Combat Interrupt (15s delay)**: Regeneration ceases when taking damage and only resumes after **15 seconds** of taking no damage. The Adamant and Redoubt [drone formations](/wiki/03-Mechanics/Formations.md) are the exception: they give shield back every second, in a fight too.
