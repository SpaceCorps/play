# Inventory & Equipment

The Hangar allows you to manage your ships and equipment. Equipping items effectively is key to survival and dominance. You can do it at the station, and in flight from inside a safe zone: see [The Hangar in Flight](/wiki/03-Mechanics/Hangar.md).

## Equipment Slots & Stat Efficiencies

Unlike traditional space games, SpaceCorps features dynamically tiered equipment slots that scale the effectiveness of fitted modules.

- **Laser Slots**: For offensive weapons (Lasers). These always operate at **100% damage and range**.
- **Generator Slots**: Shared slots for shields, engines and Adaptive Cores. They are divided into three efficiency bands, and the band decides how much of an item's base stats count. In the Hangar each band has an (i) next to its name that explains it:
  - **Core Slots**: Items placed here receive **100%** of their base stats. Every ship has them: put your strongest shields and engines here.
  - **Support Slots**: Items placed here receive **75%** of their base stats (e.g. 75% speed or shield capacity). Every ship has them.
  - **Auxiliary Slots**: Items placed here receive **50%** of their base stats. Only some ships have them (the Nomad has 1, the Paragon and the Storm 2, the Ironclad 3 and the Wraith 4; the Protos, Kitefin and Ostirion have none). They are best for extra, weaker shields and engines, while your strongest go in the core slots.
  - **Drone Slots**: a shield on one of your drones counts like one in a core slot, **100%** of its stats (see [Drone Mechanics](/wiki/03-Mechanics/Drones.md)).
  - **Unassigned/Legacy Slots**: Items placed here do not contribute to stats.
  - **Stacking fades too**: shields and engines are ranked strongest first (by what each counts after its slot's share), and the band's share is then multiplied by their rank's: the 1st to 4th count in full, the 5th to 7th 85%, 70% and 55%, the 8th onward 50% for shields and 25% for engines. See [Shields](/wiki/03-Mechanics/Shields.md) and [Speed](/wiki/03-Mechanics/Speed.md).
- **Extra Slots**: For specialized utility items, such as Repair Drones. The Protos, Kitefin, Ostirion and Nomad have two; the Paragon, Ironclad, Wraith and Storm, which you craft, have three. The Extra Slots CPUs ([Extras](/wiki/06-Items/Extras.md#extra-slots-cpus)) add 3, 5 or 7 more.

## Inventory Order

The inventory lists your items in the same order as the Shop, whatever order you bought, crafted or found them in. Kinds that belong together sit together: lasers, laser amps and laser ammo; shields and shield cells; engines and thrusters; Adaptive Cores; extras (Repair Drones); drones and drone formations; then resources. Inside a kind the cheapest comes first (credits before Thulium), then what has no price: craft-only gear and drops, weakest rarity first (lasers of one rarity, weakest damage first). Laser ammo reads x1 to x4, then the Siphon Battery. Rockets go by kind (single target before area blast, guided before straight) and then by tier, so the Epic rocket, which costs Thulium, comes last in its kind. Copies of one item go by their enchant tier. Above the grid, one chip per kind uses the same order, each with the number of items the search finds in it. Every chip switches on or off by itself, so you can hide ammo and Repair Drones while you work on lasers, shields and engines: click a chip to show or hide its kind, Shift-click (or double-click) to leave only that kind on, and click it again to bring the rest back. **All** shows every kind and **None** hides them all, to switch on only the ones you want. A crossed-out chip is off, a chip with a check mark is on. The search works on the kinds that are on, and your choice is remembered with your pilot. If everything is hidden, the grid says so and offers **Show all categories**.

## Item-to-Item Equipping (Sub-Sockets)

Some primary items can "equip" secondary support items (called sub-socketing) to amplify their parameters. To sub-socket, drag the support item directly onto the primary item in your Hangar inventory.

### Compatibility Table

| Primary Item | Acceptable Sub-Socket Items | Resulting Effect |
| :--- | :--- | :--- |
| **Laser** | Laser Amplifier (Amp) | Boosts base damage and critical hit stats |
| **Shield Core** | Shield Cell | Boosts shield capacity and recharge rate |
| **Engine** | Thruster | Boosts engine speed and multipliers |
| **Hybrid Generator** | Shield Cell OR Thruster | Boosts shield capacity, recharge rate, or speed |
| **Drone** | Laser or Shield, in each of its slots (a Master Drone has two) | A laser adds its damage to your volley; a shield counts as one in a core slot (100% of its stats) |

---

## Ammo Management

Laser Ammo is a consumable resource.
- Ammo stacks in your inventory.
- You can change active laser ammo via your HUD hotbar.
- Higher quality ammo provides damage multipliers (e.g., standard x1, advanced plasma x2, ultra core x3, experimental fusion core x4). The Siphon Battery deals x1 damage to shields only and gives it to yours.
