# Drone Mechanics

Drones are autonomous support units that fly alongside your ship. They provide additional equipment slots and contribute directly to your ship's combat performance.

## Formation & Movement

Drones fly in a standard **"Wingman" Formation (2-2-4)**:

- **2 Drones** on the left flank.
- **2 Drones** on the right flank.
- **4 Drones** following behind.

They utilize a smooth following algorithm that adjusts their position based on your ship's speed and rotation, tightening the formation during sharp maneuvers.

## Equipment & Stats

Drones function as extending equipment racks for your ship.

- Each drone has a specific number of **Slots**.
- You can equip **Lasers**, **Shields**, or **Hybrid Generators** into these slots.
- **Stats Stack**: All items equipped on drones contribute 100% of their stats to your main ship totals.
  - A laser on a drone fires when you fire.
  - A shield on a drone adds to your total shield capacity.

## Combat Behavior

- **Lasers**: Drones will fire their equipped lasers at your locked target.
- **Damage**: Drones can take damage (if distinct entity logic exists, currently they share ship pool mostly but visually distinct). _Note: Currently, Drones are indestructible extensions of the ship._
