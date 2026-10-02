# Speed Calculation

Speed determines how fast your ship moves on the spacemap, allowing you to chase targets, escape combat, or transit zones.

## The Speed Formula

Your ship's final speed is calculated on the server using the following formula:

\[\text{Final Speed} = (\text{Ship Base Speed} + \text{Total Engine Speed}) \times (1.0 + \text{Total Speed Bonus Percent})\]

### 1. Effective Engine Speed

Every engine equipped generates speed. If thrusters are nested in the engine, its speed is modified:

\[\text{Engine Speed} = (\text{Engine Base Speed} \times \text{Thruster Multiplier}) + \text{Thruster Flat Bonus}\]

- **Thruster Multiplier**: The product of all thruster speed multipliers slotted in that engine (e.g. Thruster III is `1.1` or `+10%`).
- **Thruster Flat Bonus**: The sum of all flat speed additions from thrusters (e.g. Thruster III is `+15` speed).

### 2. Diminishing Returns (Marginal Efficiency)

To prevent players from stacking infinite engines for infinite speed, a **Diminishing Returns (Marginal Efficiency)** curve is applied. All engines are sorted by their speed contribution and processed in order. Adaptive Cores (hybrids) and shield cores are ranked the same way, each kind in a group of its own, so a ship with both engines and Adaptive Cores has a first four of each:

| Engine Rank | Efficiency Multiplier |
| :---: | :--- |
| **1st to 4th** | **100%** (1.0) |
| **5th** | **85%** (0.85) |
| **6th** | **70%** (0.70) |
| **7th** | **55%** (0.55) |
| **8th and beyond** | **25%** (0.25) |

Additionally, the engine speed is multiplied by its slot efficiency (Core: 100%, Support: 75%, Auxiliary: 50%).

### 3. Speed Bonus Percent & Shield Penalties

Total speed bonus percent is the sum of all speed bonuses from equipped engines (and hybrids) minus the penalties from equipped shields:

- **Engine speed bonus**: Engines add positive speed percentages (e.g. Engine III adds `+5%`).
- **Shield speed penalty**: Heavy shields weigh down your ship, adding negative speed percentages (e.g. Heavy Shield Core adds `-5%` speed).
- **Slot scaling**: These percentage bonuses and penalties are also scaled by the slot efficiency where the item is equipped. A shield on one of your drones slows you as one in a core slot does.
- **Never below zero**: however many shields you carry, your speed does not go below 0.
