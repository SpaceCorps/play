# Active Ship Abilities

Active Ship Abilities are powerful tactical options that you can trigger in the heat of combat or navigation. These abilities are granted directly by equipping specialized modules in your ship's **Ability Slots**.

## How It Works

Every ship has a fixed number of **Ability Slots** available in the Hangar:
- **Protos** (Starter): 1 Slot
- **Kitefin**: 1 Slot
- **Ostirion**: 2 Slots
- **Paragon**: 3 Slots
- **Wraith**: 3 Slots

Equipping **Shield Cells (Type 7)** or **Thrusters (Type 8)** directly to these slots grants their corresponding active ability.

---

## Active Abilities List

### 1. Shield Regen (Shield Cells)
* **Trigger Key**: `Q` (Default, configurable in settings)
* **Description**: Activates a temporary shield regeneration field. No matter what, you will start regenerating a percentage of your maximum shield capacity over a set duration. This regeneration is **uninterrupted by damage**.
* **Potency**: Calculated as the **average** potency of all equipped Shield Cells. (e.g., equipping a 10% regen cell and a 20% regen cell will yield a 15% regen ability).

### 2. Speed Boost (Thrusters)
* **Trigger Key**: `W` (Default, configurable in settings)
* **Description**: Overcharges your ship's thrusters, increasing your engine speed by a percentage for a short duration.
* **Potency**: Calculated as the base boost scaling factor multiplied by the average quality factor of the equipped Thrusters.

---

## Ability Scaling Table

Equipping multiple modules of the same type increases efficiency by drastically reducing the cooldown and duration of the ability, allowing for more frequent tactical bursts:

| Modules Equipped | Cooldown | Duration | Base Potency (Shield Cells / Thrusters) |
| :--- | :--- | :--- | :--- |
| **1 Module** | 60 seconds | 5 seconds | +10.0% / +10.0% Speed |
| **2 Modules** | 45 seconds | 4 seconds | +Average Cell % / +15.0% Speed |
| **3 Modules** | 30 seconds | 3 seconds | +Average Cell % / +20.0% Speed |
| **4+ Modules** | 20 seconds | 2 seconds | +Average Cell % / +25.0% Speed |

> [!NOTE]
> Equipping mixed modules (e.g. 1 Shield Cell and 1 Thruster on an Ostirion) grants both abilities separately, each using their respective "1 Module" scaling tier (60s cooldown, 5s duration). Equipping 2 of the same module upgrades that specific ability to the "2 Modules" scaling tier (45s cooldown, 4s duration).

---

## Technical Specifications

- **Damage Interruption**: Standard passive shield regeneration has a 15-second combat delay. **Active Shield Regen ignores this delay** and regenerates shields even while taking continuous damage.
- **Speed Overlap**: Speed Boost stacks multiplicatively with passive engine bonuses, but does not stack with other active speed bursts of the same type.
