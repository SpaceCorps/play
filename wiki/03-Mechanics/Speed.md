# Speed Calculation

Speed determines how fast your ship moves on the spacemap, allowing you to chase targets, escape combat, or transit zones.

## The Speed Formula

Your ship's final speed is calculated on the server using the following formula:

\[\text{Final Speed} = (\text{Ship Base Speed} + \text{Total Engine Speed}) \times (1.0 + \text{Total Speed Bonus Percent})\]

A [ship design](/wiki/03-Mechanics/Ship-Designs.md) changes the first term (THUNDER has 40 more base speed, DUMA 20 less), and NOTSUM and RECON multiply the final speed by one more factor, +2% and +5%.

### 1. Effective Engine Speed

Every engine equipped generates speed, and so does every Adaptive Core that holds thrusters. If thrusters are nested in the engine, its speed is modified:

\[\text{Engine Speed} = (\text{Engine Base Speed} + \text{Thruster Flat Bonus}) \times \text{Thruster Multiplier}\]

- **Thruster Flat Bonus**: The sum of all flat speed additions from thrusters (e.g. Impulse Thruster III is `+12.75` speed).
- **Thruster Multiplier**: The product of all thruster speed multipliers slotted in that engine (e.g. Momentum Thruster III is `1.0765` or `+7.65%`, Impulse Thruster III `1.0255` or `+2.55%`). It multiplies everything the engine makes: its own base speed and the thrusters' flat bonuses. An Adaptive Core has no base speed of its own, and its thrusters' flat bonuses are multiplied all the same.

An Engine III (base speed 6) with three Momentum Thruster IVs (`+11.135`, `1.0935`) makes (6 + 3 x 11.135) x 1.0935 x 1.0935 x 1.0935 = 51.5, and with three Impulse Thruster IVs (`+14.025`, `1.02975`) (6 + 3 x 14.025) x 1.02975 x 1.02975 x 1.02975 = 52.5. A Forge buff on a thruster's multiplier grows the part above 1: +15% on `1.0935` makes `1.1075`.

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
- **Drone formations**: a worn [drone formation](/wiki/03-Mechanics/Formations.md) changes the final speed once more, as a factor of its own: Gyre +10%, Cordon −3%, Auger −9%, Culler −10%, Redoubt −11%, Rampart −17%. The Afterburner then multiplies the result.
