# Combat Mechanics

This section details how damage is calculated, applied, and repaired during engagements in SpaceCorps.

## Damage Calculation

When a ship fires its lasers, the server calculates the damage output using the following sequence:

### 1. Base Damage & Random Variance

The base damage of all equipped lasers (including lasers on drones) and their slotted laser amplifiers is summed.
- **Random Roll**: The actual damage of a volley is randomized between **80%** and **100%** of the total base damage.
  - Formula: `Roll = (0.8 + (Random * 0.2)) * BaseDamage`

### 2. Critical Hits

Every volley has a chance to be a Critical Hit.
- **Critical Chance**: The average critical chance of equipped lasers plus the sum of all equipped laser amplifier critical chances.
- **Critical Multiplier**: If a shot is critical, the damage roll is multiplied by **1.5x**.
- **Fixed Critical Damage**: Any flat critical damage from laser amplifiers is added after the multiplier.
  - Formula: `CritDamage = (Roll * 1.5) + FixedCritDamage`

### 3. Global Multipliers

Finally, global multipliers (such as active boosters or laser ammunition multipliers like x2, x3, x4) are applied to obtain the final damage output:
- Formula: `FinalDamage = Damage * AmmoMultiplier * (1.0 + BoosterDamagePercent)`

### 4. Facing the Target

A ship or alien locked on and firing turns to face its target, whichever way it is flying (circling, backing off or holding still), and turns back to its course when it stops firing.

---

## Kill Rewards: First Hit Claims

An alien's rewards go to the pilot who shot it first, not to whoever lands the last hit.

- **Claiming**: the first pilot whose shot damages an alien claims it. Every hit of yours renews your claim.
- **Losing it**: if you don't hit the alien for **10 seconds**, your claim lapses and the next pilot to hit it claims it. Your claim also ends when your ship is destroyed or you leave the map (through a portal, or by logging off), and coming back within the 10 seconds doesn't bring it back.
- **The kill**: when the alien is destroyed, the pilot holding its claim gets everything: Credits, Thulium, XP, Honor, the kill for quests and Wipe Points, and the [cargo](/wiki/03-Mechanics/Cargo.md) crate. A pilot who finishes an alien someone else claimed gets nothing, and the Game Log says so.
- **Seeing it**: when you select an alien another pilot has claimed, the target panel shows *Claimed by* that pilot and *No reward*.
- [Company pilots](/wiki/03-Mechanics/Company-Pilots.md) never claim an alien, and an alien they finish still pays the pilot holding its claim.

---

## Taking Damage & Safe Zones

When your ship is hit by an enemy or NPC, damage is processed as follows:

### 1. Shield Absorption

Incoming damage is divided between shields and hitpoints by your ship's **Average Absorbance**: the average of your shields' absorbance, each with its Shield Cells', at most 100% (see [Shield Mechanics](/wiki/03-Mechanics/Shields.md)):
- **Absorbance** (e.g. 88% for a Basic Shield Core with two Advanced cells) of each hit is taken by the shields.
- The rest (12% there) bypasses shields and hits HP directly ("Shield Penetration").
- A shield too low for its share passes the difference to HP; if shields are fully depleted, **100%** of all remaining damage hits HP.
- Aliens have no absorbance: their shields take 80% of each hit, their hull 20%.

### 2. Safe Zone Immunity

Each faction's home base (X-1 maps) contains safe zones.
- Entering a safe zone makes your ship completely immune to damage.
- **Aggro Break**: Attacking an enemy will immediately remove your safe zone immunity, even if you are physically located inside one.

---

## Recovery & Repair

To recover from combat, pilots can rely on passive regeneration and active utility bots:

### 1. Shield Passive Regeneration

- **Operation**: Restores shield points equal to your shield's recharge rate per second.
- **Delay**: Interrupted by combat; passive regeneration resumes only after **15 seconds** of taking no damage.

### 2. Repair Drones (Hull Repair)

- **Operation**: If you equip a Repair Drone (under Hangar extras), it will automatically repair your hull (HP).
- **Repair Rate**: Restores a percentage of your maximum hitpoints per second:
  - **Repair Drone I**: 0.5% max HP / s
  - **Repair Drone II**: 0.75% max HP / s
  - **Repair Drone III**: 1.25% max HP / s
- **Delay**: Repair drones will only begin patching the hull after **10 seconds** of taking no damage.
