# Inventory & Equipment

The Hangar allows you to manage your ships and equipment. Equipping items effectively is key to survival and dominance. You can do it at the station, and in flight from inside a safe zone: see [The Hangar in Flight](/wiki/03-Mechanics/Hangar.md).

![The Hangar's inventory: the category chips are one glyph each (the name is the tooltip) with the count of what you hold](../img/wiki-img/shots/inventory-chips.jpg)
![Dragging a rectangle over the empty space of the inventory: every tile it touches is selected and the title row counts them](../img/wiki-img/shots/inventory-marquee.jpg)

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
- **Hull Plate Slots**: For [Hull Plating](/wiki/06-Items/Hull-Plating.md#hull-plate-slots), which adds hull. Only the four ships you craft have them (the Paragon 5, the Storm 7, the Ironclad 15 and the Wraith 9), each locked until you research it in the Skylab, and they are the same in both configurations.

## Inventory Order

The inventory lists your items in the same order as the Shop, whatever order you bought, crafted or found them in. Kinds that belong together sit together: lasers, laser amps and laser ammo; shields and shield cells; engines and thrusters; Adaptive Cores; extras (Repair Drones); drones and drone formations; then resources. Inside a kind the cheapest comes first (credits before Thulium), then what has no price: craft-only gear and drops, weakest rarity first (lasers of one rarity, weakest damage first). Laser ammo reads x1 to x4, then the Siphon Battery. Rockets go by kind (single target before area blast, guided before straight) and then by tier, so the Epic rocket, which costs Thulium, comes last in its kind. Copies of one item go by their enchant tier. Above the grid, one chip per kind uses the same order, each with the number of items the search finds in it. Every chip switches on or off by itself, so you can hide ammo and Repair Drones while you work on lasers, shields and engines: click a chip to show or hide its kind, Shift-click (or double-click) to leave only that kind on, and click it again to bring the rest back. **All** shows every kind and **None** hides them all, to switch on only the ones you want. A crossed-out chip is off, a chip with a check mark is on. The search works on the kinds that are on, and your choice is remembered with your pilot. If everything is hidden, the grid says so and offers **Show all categories**.

## Marketable items

Items you earned (drops, mission rewards, and what the Assembly and the Forge make) carry a small **Marketable** tag on their tile, and the item card reads "Marketable", or "Marketable (3 of 5)" for a stack of which only some units can be sold. The **Marketable only** chip beside the category chips shows only those items. A **gavel** beside the trash of a tagged item opens the sell sheet of the [Auction](/wiki/03-Mechanics/Auction.md) (it is not shown in flight: selling is a page of the station). What you bought, won or were given has no tag and can't be sold again.

## Select several items

Press on an empty part of the inventory (the margin beside the tiles, the gap between two tiles or the space under the last row) and drag: a translucent rectangle follows the pointer, and every tile it touches is selected while you drag. Let go and the selection stays; the title row counts it ("3 selected"). Hold **Shift**, **Ctrl** or **Cmd** while you drag to add to the selection: tiles it already holds that the rectangle touches are let go instead. A plain drag starts a new selection. **Esc**, a click on empty space or the button beside the trash in the title row clears it; **Esc** in the middle of a drag cancels the drag. At the top or bottom edge of a long inventory the list scrolls by itself. A press on a tile is still the tile's own: click to equip, drag to a slot. The trash button in the title row deletes the selected items after a question that lists them (a stack of identical Extras goes as a whole); it is not offered while the Hangar in flight is locked. An item fitted in the Skylab cannot be selected, and only what the search and the category chips leave on the grid can be. A soft tick sounds when the rectangle takes one more tile (it follows the Button Sounds switch in the settings).

**Equip the whole selection.** Drag one of the selected tiles and the whole selection comes with it, a stack of tiles with a count in front of the pointer (a tile that is not selected drags alone, and a click on a selected tile still equips only that item). Let go on a slot or a card and the item under the pointer goes there if it fits, and every other item to its best slot; let go on the ship's empty parts and every item goes to its best slot; let go anywhere else and nothing happens, and **Esc** lets go of the drag. The arrow button beside the trash in the title row (its tip says it equips the selected items in their best slots) does the same without a drag; it is not offered in the P.E.T. view or while the Hangar in flight is locked. The best slot is where a click would put the item, worked out for one item after the other: lasers first, the strongest first, then shields, engines and Adaptive Cores, the extras, the Repair Drones (in a free ability slot when the extras are full), the hull plates and last the amps, cells and thrusters, which need their lasers, shields and engines to be fitted by then. What could not be placed stays selected, and one message says how many went ("Equipped 7 of 9.") and why the rest did not. One quiet sound plays for the whole drop.

## Item-to-Item Equipping (Sub-Sockets)

Some primary items can "equip" secondary support items (called sub-socketing) to amplify their parameters. To sub-socket, drag the support item directly onto the primary item in your Hangar inventory.

### Compatibility Table

| Primary Item | Acceptable Sub-Socket Items | Resulting Effect |
| :--- | :--- | :--- |
| **Laser** | Laser Amplifier (Amp) | Boosts base damage and critical hit stats, or takes points off the target's absorbance (Penetration Amp) |
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
