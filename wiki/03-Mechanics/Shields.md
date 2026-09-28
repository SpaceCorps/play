# Shield Mechanics

Shields absorb the majority of incoming damage, protecting your ship's hull from direct damage.

## Shield Calculations

Your ship's final shield parameters are calculated as follows:

\[\text{Final Shield Capacity} = \text{Total Base Capacity} \times (1.0 + \text{Total Shield Bonus Percent})\]
\[\text{Final Shield Recharge Rate} = \text{Total Base Recharge} \times (1.0 + \text{Total Shield Bonus Percent})\]

### 1. Slot Efficiency & Diminishing Returns

Similar to engines, equipped shields (and hybrid generators) are sorted by capacity and subjected to slot efficiency (Core: 100%, Support: 75%, Auxiliary: 50%) and a diminishing returns curve based on their rank:

- **1st to 4th shield**: **100%** (1.0) marginal efficiency.
- **5th shield**: **85%** (0.85) marginal efficiency.
- **6th shield**: **70%** (0.70) marginal efficiency.
- **7th shield**: **55%** (0.55) marginal efficiency.
- **8th and beyond**: **25%** (0.25) marginal efficiency.

### 2. Shield Absorbance (Damage Split)

Absorbance is the share of every hit your shields take; the rest goes directly to hitpoints (HP).
- **Per shield**: a shield's absorbance plus the absorbance of the Shield Cells fitted into it (Basic +2%, Advanced +4%, Elite +6%).
- **Average Absorbance**: your ship's absorbance is the simple average over the shields in core, support and auxiliary slots, **at most 100%**. Adaptive Cores have no absorbance of their own and don't count in the average (cells in an Adaptive Core add capacity and recharge only). With no shield equipped your absorbance is 0%: the hull takes every hit, and shield points from cells in an Adaptive Core go unused, so fit a shield alongside.
- **Example**: a Basic Shield Core (80%) with two Advanced Shield Cells is 88%; add a Light Shield Core (70%) and the average is 79%. A Heavy Shield Core with three Elite cells (103%) is capped at 100%.
- **Damage Allocation**: With 88% absorbance:
  - **88%** of damage is subtracted from Shields.
  - **12%** of damage goes directly to HP (Shield Penetration).
- A shield too low for its share passes the difference to HP; if shields are at 0, all damage hits HP directly.
- Aliens have no absorbance: they split every hit 80% / 20%.

---

## Shield Passive Regeneration

Shields regenerate passively over time to keep you combat-ready.

- **Regeneration Tick**: If shields are below maximum capacity, they restore shield points equal to your Recharge Rate per second.
- **Combat Interrupt (15s delay)**: Regeneration ceases when taking damage and only resumes after **15 seconds** of taking no damage.
