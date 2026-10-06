# The Hangar in Flight

You don't have to return to base to change your ship. From inside a safe zone you can open the **Hangar** window (the warehouse button in the top-left toolbar) and change what is fitted, swap to the other configuration or fly another ship you own, without leaving the game. The window is the Hangar page of the station, the same slots, stats and inventory, in a window over the game. See [Inventory & Equipment](/wiki/03-Mechanics/Inventory.md) for how items fit.

![The Hangar window in flight, opened at the station on its Drones view: the drones, the list of drone formations and the inventory](../img/wiki-img/shots/hangar-window.jpg)

## When It Is Open

A change is allowed only while all of these are true:

- **A safe zone protects you.** Every station and portal has a protective ring (see [Combat](/wiki/03-Mechanics/Combat.md)). Inside it you're protected once 5 seconds have passed since you were hit and 15 since you fired.
- **You have been out of combat** for a few more seconds: **10** by default. It matters when you arrive protected at once, through a portal, with a fight behind you.
- You are not cloaked, not inside your own EMP's window and not near the [black hole](/wiki/03-Mechanics/Black-Hole.md), and you have no rocket of yours still in the air.

Repairs going on don't stop you. Anywhere else the Hangar window still opens, but it is read-only. An amber banner says why, and counts the seconds down when it is a wait ("You were in combat a moment ago. Wait 6 s to change your ship."). The server enforces it too, so nothing can change a ship in the field.

## What You Can Change

- **Equip and unequip anything**, in every kind of slot: lasers, generators (shields, engines, Adaptive Cores), extras, ability slots and drone slots, and the amps, cells and thrusters fitted into them. Drag items onto slots, or click them, exactly as in the station. Your ship follows at once: stats, lasers, abilities and the hotbar.
- **Unequip all.** The **Unequip all** button in the Hangar's toolbar empties the configuration shown in the **Spaceship** view in one go: the lasers, shields, engines, Adaptive Cores, extras and ability slots **and the lasers and shields in your drones' slots**, with the amps, cells and thrusters fitted into them. Everything goes back to your inventory, all of it or none. Your **drones stay yours** (a drone is never fitted to a ship, so there is nothing to take off it) and the **drone formation** you wear stays on. The other configuration is not touched. In flight it follows the rules of any change: from a safe zone, out of combat. The **Drones** view has a button of its own that empties the drones' slots only.
- **Either configuration.** You can prepare Config 2 while flying Config 1, then swap with the Switch Config key. A **Fly config** button in the Hangar does the same swap.
- **Any ship.** Set another ship active and you fly it from where you are. Your ship's model changes in front of everyone nearby.
- **A new shield, engine or Adaptive Core starts empty**, as in the station: its configuration's shield charge is empty until it recharges.
- **Drone formations.** The Drones view lists the formations you own under your drones. They are not fitted: in flight you drag one from the hotbar's Formations list onto a slot, and that slot's click or key wears it, with no wait inside a safe zone ([Drone Formations](/wiki/03-Mechanics/Formations.md)).
- **Extras.** The four regular ships, the Protos, Kitefin, Ostirion and Nomad (the ones you start with or buy), have 2 extra slots in each configuration; the four ships you craft in Assembly, the Paragon, Ironclad, Wraith and Storm, have 3. The Extra Slots CPUs of your Skylab add 3, 5 or 7 on top: 5, 7 or 9 on the regular ships and 6, 8 or 10 on the crafted ones ([Extras](/wiki/06-Items/Extras.md#extra-slots-cpus)). When 0.4.10 came, a third extra on a regular ship was unequipped into your inventory: nothing was deleted, and you got one chat message.

## Changing Ship

The ship you switch to has **the hull and shields it had** when you last flew it, exactly as if you had launched it. The ring doesn't repair, so changing ship never heals you: the ship you leave keeps the damage it has, and comes back with it. A wrecked ship can't be flown until you revive it, which is free and brings it back with at most 10,000 hull and no shield, as a respawn does.

What is yours stays yours: your ammo, your rockets and their timer, your ability cooldowns, your boosters, your XP and your Slave Drones. What belonged to the ship ends: a running Shield Surge or Afterburner, repairs, your target lock, your attack and the course you were flying. Fittings stay on the ship they are fitted to.

## Requests From Other Tools

The Hangar changes only from a safe zone on the server too: fitting, unfitting, deleting an item, reviving a ship or setting the active ship while you fly answers "You can only change your ship in a safe zone." The configuration swap is the exception, and works anywhere (once every 5 seconds).
