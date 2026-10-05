# Combat Mechanics

This section details how damage is calculated, applied, and repaired during engagements in SpaceCorps.

![The death screen: respawn at the nearest portal or on the spot, each with its lock](../img/wiki-img/shots/death.jpg)
![The flight screen in a fight: ship and pilot windows, the target, the hotbar, the chat, the log and the minimap](../img/wiki-img/shots/hud-fight.jpg)
![The Target window: the alien, its distance, hull and shield](../img/wiki-img/shots/hud-target.jpg)

## Damage Calculation

When a ship fires its lasers, the server calculates the damage output using the following sequence:

### 1. Base Damage & Random Variance

The base damage of all equipped lasers (including lasers on drones) and their slotted laser amplifiers is summed.
- **Random Roll**: The actual damage of a volley is randomized between **80%** and **100%** of the total base damage.
  - Formula: `Roll = (0.8 + (Random * 0.2)) * BaseDamage`

### 2. Critical Hits

Every volley has a chance to be a Critical Hit.
- **Critical Chance**: The average critical chance of equipped lasers plus the sum of all equipped laser amplifier critical chances.
- **Critical Multiplier**: If a shot is critical, the damage roll is multiplied by **1.5x**. The damage number of a critical volley is shown in ice cyan, larger, with a "!".
- Quantum Laser 1 and 2 have no critical chance of their own: their amplifiers give it.
- **Fixed Critical Damage**: Any flat critical damage from laser amplifiers is added after the multiplier.
  - Formula: `CritDamage = (Roll * 1.5) + FixedCritDamage`

### 3. Global Multipliers

Finally, global multipliers (such as active boosters or laser ammunition multipliers like x2, x3, x4) are applied to obtain the final damage output:
- Formula: `FinalDamage = Damage * AmmoMultiplier * (1.0 + BoosterDamagePercent)`
- A worn [drone formation](/wiki/03-Mechanics/Formations.md) can multiply the result once more: for example Auger +21% laser damage, Gyre −11%, and against aliens Culler +12% (a separate factor, not part of the booster percent).
- **Siphon Battery** ammo has the x1 multiplier but a different target: its damage comes out of the target's shield alone (never the hull, whatever the absorbance) and goes into your own shield, up to your maximum. See [Lasers & Ammo](/wiki/06-Items/Lasers.md).

### 3b. Rockets

A [rocket](/wiki/06-Items/Rockets.md) has its own damage (a Lancet I deals 1,600 to 2,000, a Lancet III 4,800 to 6,000, a N.U.K.E. 45,000 to 50,000), rolled once when you fire it and the same for every ship: your lasers, amps, boosters and ammo do not change it, and it has no critical hit. All rockets share one **5 second** timer. A single-target rocket has a **shield penetration**: it comes off your target's absorbance (see Taking Damage below); a blast hurts every ship in its radius, less toward the edge. Nothing caps what a rocket takes from a pilot's ship: the shield first, then the hull. Rockets never hurt your own company or your own [group](/wiki/03-Mechanics/Groups.md), whatever the companies in it. A worn [drone formation](/wiki/03-Mechanics/Formations.md) is the one thing that changes both: a rocket formation raises the damage of every rocket (up to +55%), and a few lengthen or shorten the timer.

### 4. Facing the Target

A ship or alien locked on and firing turns to face its target, whichever way it is flying (circling, backing off or holding still), and turns back to its course when it stops firing.

### 5. Range

A ship fires one volley a second while its target is inside its **range**, and holds fire while the target is farther: the fire stops costing ammo until the target is close enough again, and the target panel says "Out of range". The range is **the average of the ranges of all your lasers** (the lasers in your drones too), rounded to the nearest unit, and it is one number for the whole ship: inside it every laser fires, outside it none does. A long-range laser beside short ones therefore does not stretch your reach: a Starfire-3 (850) and two Quantum Laser 2 (700) make 750. A Forge range buff counts on its own laser before the average. A ship with no laser cannot fire its lasers, and the Hangar shows no range for it (a dash); its rockets still fire, each with its own range (see [Rockets](/wiki/06-Items/Rockets.md)). See [Lasers & Ammo](/wiki/06-Items/Lasers.md) for each laser's own range.

---

## Kill Rewards: First Hit Claims

An alien's rewards go to the pilot who shot it first, not to whoever lands the last hit.

- **Claiming**: the first pilot whose shot damages an alien claims it. Every hit of yours renews your claim.
- **Losing it**: if you don't hit the alien for **10 seconds**, your claim lapses and the next pilot to hit it claims it. Your claim also ends when your ship is destroyed or you leave the map (through a portal, or by logging off), and coming back within the 10 seconds doesn't bring it back.
- **The kill**: when the alien is destroyed, the pilot holding its claim gets everything: Credits, Thulium, XP, Honor, the kill for quests and Wipe Points, and the [cargo](/wiki/03-Mechanics/Cargo.md) crate. A pilot who finishes an alien someone else claimed gets nothing, and the Game Log says so. When your claim pays and another pilot lands the last hit, the Game Log names that pilot and says your claim pays you.
- **Ranking points**: the kill also adds PvE points to the claim holder's ranking, more for a tougher alien: 1 for a Seeker, 2 for a Phantasm, 4 for a Bulwark, 7 for a Goombah and 16 for a Crystalys (each alien's article lists its own). They are the killer's alone: a group's share of the rewards doesn't include them.
- **Seeing it**: when you select an alien another pilot has claimed, the Target window shows *Claimed by* that pilot and *No reward*.
- [Company pilots](/wiki/03-Mechanics/Company-Pilots.md) never claim an alien, and an alien they finish still pays the pilot holding its claim.
- A pilot in a [group](/wiki/03-Mechanics/Groups.md) shares what its claim pays with the group mates who are close and shooting; the claim itself is the pilot's alone.
- **The leaders of the [swarms](/wiki/05-Swarms/Swarms.md), the Dormant Pulses and the [Clan Wardens](/wiki/03-Mechanics/Clans.md#warden-pay-and-loot) are the exception**: a swarm boss, a Dormant Pulse or a Clan Warden is paid by the damage each pilot dealt to it, not by the first hit, and its cargo box goes to the pilot who dealt the most ([how a boss kill pays](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). The other followers, the Pirate Scouts and the Seeker Slaves, pay by the claim like any alien. A swarm ship's PvE points are on the Swarms page.

---

## Aliens That Only Fight Back

The Seeker and the Goombah never start a fight. Each turns on a pilot who hits it (a hit that does damage; another alien's fire never provokes it), fights the one described under [Who an Alien Fights](#who-an-alien-fights), and lets go **10 seconds** after anybody last hit it. Left alone for **30 seconds**, its hull mends by 2% of its maximum a second. The other aliens (Phantasm, Bulwark, Crystalys) go after any unprotected pilot who comes within their aggro radius (700, 700 and 900 units) and never mend their hull; every alien's shield recharges from 15 seconds after its last hit.

---

## Who an Alien Fights

An alien keeps fighting **the first pilot who shot it**, for as long as it can still chase that pilot: the pilot is on the map, not in a safe zone, not cloaked or inside its EMP window, alive, and has hit it in the last **10 seconds** (every hit starts the 10 seconds again: a laser volley, a rocket or the edge of a blast alike). While that holds, other pilots' shots never turn it, however close they are or however often they hit, so one pilot can hold an alien while others shoot it.

When the first pilot drops out (it leaves the map, reaches a safe zone, goes dark, is destroyed, or stops hitting the alien for 10 seconds), the alien turns on the **next** pilot who joined the fight, in the order they first shot it, not on the one who hit it last. A pilot who dropped out and shoots it again joins the queue at the back. An alien keeps track of the first **32** pilots who shot it; a 33rd shooter takes no part in the queue until one of them drops out, and in a crowd of any size the alien stays on the first.

[Company pilots](/wiki/03-Mechanics/Company-Pilots.md) count after every player: an alien fights a company pilot only while no player it can still chase has shot it, a player who shoots an alien a company pilot is fighting takes it over, and a company pilot never draws an alien off a player. None of this changes who gets the alien's rewards: that is the claim's ([Kill Rewards](#kill-rewards-first-hit-claims)).

---

## Aliens Lose Interest

No alien follows you across the map. But an alien you are **hitting** is not losing interest, it is fighting you: for **10 seconds** after your last hit (every hit starts the 10 seconds again, a laser volley, a rocket or the edge of a blast alike) it flies at you, at its own speed, whenever you are beyond its attack range (Seeker 600, Phantasm and Bulwark 700, Goombah 800, Crystalys 900), and keeps closing in and firing until you are in range. It has no limit on how far it follows while you keep hitting it. A laser that reaches farther than the alien's weapon (a Starfire-3 reaches 850 units, a Helios Beam 900) does not let you hit it from where it cannot answer, and a faster ship only keeps it behind you for as long as you keep shooting. It still drops you at once if you reach a safe zone, cloak, or leave the map.

When several pilots hit the same alien, it stays on the first who shot it (see [Who an Alien Fights](#who-an-alien-fights)): it closes in on that pilot and fires, so a group standing around it just outside its range cannot keep it running from one to the next without ever answering.

An alien that has taken you for its target (a Phantasm, Bulwark or Crystalys that you came near, or any alien you shot) and that you have not hit for 10 seconds lets go as soon as one of these is true:

- **You never shot it:** you are more than **1,200 units** away from it, or it has flown **2,000 units** from where the chase began.
- **You shot it in the last minute:** you are more than **2,500 units** away from it, or it has flown **3,000 units** from where the chase began. A fight you started stays fair.

An alien that lets go roams from where it stands, never on to where it last saw you (not even when you cloak or fire an EMP), and does not pick you as a target again for **8 seconds**, unless you shoot it. Every alien decides for itself, so a mixed pack thins out as you fly away. Aliens never follow you into a safe zone or through a gate, and those that lost you near one head away from it, each its own way, so they do not wait in a heap. An alien's interest never reaches less than its attack range and aggro radius, plus 100 units.

Aliens do not push each other apart: a pack after one pilot closes in without keeping any room between its ships, and a pack that lost its pilot breaks up only as each alien picks its own way. An alien does keep clear of a **ship**, though: it never ends up inside a pilot's hull, and a pilot who parks on one pushes it along.

Flying faster only helps you so far: a Protos (160) is no faster than any alien that hunts (Phantasm 160, Bulwark 175, Crystalys 230), so the leash, not your speed, ends the chase.

---

## Taking Damage & Safe Zones

When your ship is hit by an enemy or NPC, damage is processed as follows:

### 1. Shield Absorption

Incoming damage is divided between shields and hitpoints by your ship's **Average Absorbance**: the average of your shields' absorbance, each with its Shield Cells', plus the Season Store's Shield Absorbance Boost (see [Shield Mechanics](/wiki/03-Mechanics/Shields.md)). It is **not capped at 100%**: what the shields take of a hit is your absorbance **less the attacker's shield penetration**, between 0% and 100%.
- **Absorbance** (e.g. 80% for the best shield with the best cells, 56% for a Basic Shield Core with two Absorption Shield Cell Is) of each hit is taken by the shields, less the penetration of the hit: a Lancet III's 35% leaves 45% on the shields of a 80% ship, and the rest (55% there) hits HP directly.
- **Shield penetration** comes from direct rockets (10 to 35%) and the x3 and x4 laser ammo (5% and 10%); aliens have none. A ship over 100% (112%, say) holds a whole hit against penetration up to the difference (12% there).
- A shield too low for its share passes the difference to HP; if shields are fully depleted, **100%** of all remaining damage hits HP.
- Aliens have no absorbance stat: their shields take 80% of each hit (less the hit's penetration), their hull the rest.
- **Drone formations.** Rampart raises your absorbance by 17% (Shrike lowers it by 6%), and Asterism gives every direct hit on you a 7% chance to do no damage at all (a floating "Miss" shows), and the hits that land are split between shield and hull as usual. Gemini (+9 points) and Stiletto (+16) add penetration to your own ammo and direct rockets, up to 40% in all ([Drone Formations](/wiki/03-Mechanics/Formations.md)).

### 2. Safe Zone Immunity

Each faction's home base (X-1 maps) contains safe zones.
- Entering a safe zone makes your ship completely immune to damage.
- **Aggro Break**: Attacking an enemy will immediately remove your safe zone immunity, even if you are physically located inside one.
- A ring around every station and portal protects you once 5 seconds have passed since you were hit and 15 since you fired. While it protects you and you're out of combat, the Hangar window lets you change your ship without leaving the game: see [The Hangar in Flight](/wiki/03-Mechanics/Hangar.md).
- Stations stand only in the home bases (`x-1`). The Danger Sectors (`DS-1` to `DS-4`) have none: there the rings around the jump gates are the only safe zones.

### 3. Under Attack in a Danger Sector

A jump through a portal takes 3 seconds (see [Spacemap Travel](/wiki/01-General/Spacemap%20Travel.md)). In the Danger Sectors (`DS-1` to `DS-4`) a pilot whose ship was hit by another pilot or an alien in the last **10 seconds** cannot start one, and a hit cancels a jump under way. Everywhere else, attacks never interrupt a jump, and nothing interrupts collecting a [cargo](/wiki/03-Mechanics/Cargo.md) crate.

---

## Recovery & Repair

To recover from combat, pilots can rely on passive regeneration and active utility bots:

### 1. Shield Passive Regeneration

- **Operation**: Restores shield points equal to your shield's recharge rate per second.
- **Delay**: Interrupted by combat; passive regeneration resumes only after **15 seconds** of taking no damage.
- **Drone formations**: Adamant and Redoubt give shield back every second, in a fight too (see [Drone Formations](/wiki/03-Mechanics/Formations.md)).

### 1b. Siphon Battery

[Siphon Battery](/wiki/06-Items/Lasers.md) ammo adds the shield it drains from a target to yours at once, up to your maximum. Gaining shield is no damage taken, so it doesn't delay your passive regeneration.

### 2. Repair Drones (Hull Repair)

- **Operation**: If you equip a Repair Drone (under Hangar extras), you switch it on from the hotbar (drag it from the Extras picker onto a slot) and it repairs your hull (HP). Any hit switches it off, and it stops at a full hull. With an [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) fitted you do not have to switch it on again: it sends the drone out by itself as soon as the delay below has passed, unless you stopped it by hand.
- **Repair Rate**: Restores a percentage of your maximum hitpoints per second (only the best drone fitted counts, they do not add up):
  - **Repair Drone I**: 1.5% max HP / s
  - **Repair Drone II**: 2.25% max HP / s
  - **Repair Drone III**: 3.5% max HP / s
  - **Repair Drone IV**: 5% max HP / s
- **Delay**: Repair drones will only begin patching the hull after **10 seconds** of taking no damage.
- **In an ability slot** a Repair Drone does not repair by itself: it gives you **Emergency Repair**, a button that heals a share of your maximum hitpoints over ten seconds, even under fire (see [Abilities](/wiki/03-Mechanics/Abilities.md)).

---

## Cloaking and the EMP

A shot needs a lock. Two [extras](/wiki/06-Items/Extras.md) take yours away:

- **Cloaking CPU**: while you are cloaked (there is no time limit) other companies' pilots, aliens and company pilots do not see your ship and cannot lock on to it; they see a plain red dot on the minimap where you are. Your first volley ends the cloak, and you cannot cloak again for a minute, nor within 10 seconds of a hit or a shot.
- **EMP Charge**: for 3 seconds nobody can lock on to you, and every lock already on you breaks at once. It ends every cloak within 1,500 units of the pilot who fires it, except those of the pilot's own group. It does not hide you, and it is not invulnerability: it stops what needs a lock.

A rocket is a shot too: it ends your own cloak, and the area blast of someone else's rocket still hurts a cloaked ship and ends its cloak, because a blast needs no lock (see [Rockets](/wiki/06-Items/Rockets.md)). The EMP stops locked lasers and guided rockets, not a blast.

Neither changes a kill claim: a claim is the history of who hit an alien, not a lock, and cloaking releases yours.
