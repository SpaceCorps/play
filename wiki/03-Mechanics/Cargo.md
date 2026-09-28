# Cargo Boxes

Destroyed aliens and ships leave their spoils in space as glowing cargo crates. Fly over and pick them up before someone else does.

## What Drops

- **Aliens** drop their loot as one crate where they blew up: the resources and parts listed under each alien's *Loot Drops* (see the [Aliens](/wiki/04-Aliens/Phantasm.md) articles). Credits, Thulium, XP and Honor are still paid the moment you make the kill. An alien whose loot rolls nothing (a Seeker four times in five) leaves no crate.
- **Ships** leave salvage: parts scavenged from the hull, never anything from the pilot's own inventory, so being destroyed costs you no items. Bigger hulls give more:

| Ship | Salvage |
| :--- | :--- |
| **Protos** (and any other hull) | 1–2 Ship Fragments |
| **Kitefin** | 1–3 Ship Fragments, 15% chance of a Reinforced Hull Plate |
| **Ostirion** | 2–3 Ship Fragments, 30% chance of a Reinforced Hull Plate |
| **Paragon** | 3–5 Ship Fragments, 60% chance of 1–2 Reinforced Hull Plates, 25% chance of a Power Core |
| **Wraith** | 5–8 Ship Fragments, 2–3 Reinforced Hull Plates, 50% chance of a Power Core, 10% chance of an Ancient Control Unit |

A ship drops salvage at most once every **5 minutes**, however often it is destroyed, and its own pilot can never salvage it: the wreck is for everyone else.

[Company pilots](/wiki/03-Mechanics/Company-Pilots.md) count as ships here: a destroyed one leaves an Ostirion's salvage. An alien a company pilot finishes drops its loot for the pilot the kill counts for (the one holding its claim, else the pilot of its company fighting it); one a company pilot fought alone drops nothing, since company pilots never collect.

The crate's lights take the colour of the rarest item inside: teal for common loot, amber for common salvage, green, blue, purple, pink, gold and orange-red from uncommon to eternal.

## Collecting

- **Left-click** a crate: your ship flies to it and takes it once within reach (200 units). A click on a crate never counts as a move order; any other move order (a click in space, the minimap) calls the pickup off. When a ship or alien is right under the pointer too, the click goes to whichever is nearer the pointer, so a fight passing over a crate keeps its targets.
- Hover a crate to see what's inside, who it's reserved for and, in its last minute, how long it has left.
- Picking a crate up plays a short pickup sound where it was; you hear other pilots' pickups nearby too, more quietly.
- What you collect goes straight to your Hangar inventory, onto your loose stack of that item (never onto equipment or anything in the Transport Cache). A toast tells you what you got; crates collected one after another add up in the same toast.

## Who Gets It

- The pilot paid for the kill, and the members of that pilot's **clan**, have the crate to themselves for **30 seconds**. For an alien that is the pilot holding its claim, the first to hit it (see [Combat](/wiki/03-Mechanics/Combat.md)), whoever finished it. Other pilots see it dimmed and can't take it yet; a ship sent to it waits nearby until the time is up.
- After that, **anyone** on the map may take it. Salvage from a ship destroyed by an alien is free for everyone at once, except the pilot who flew it.
- Only a ship on the crate's map can take it: if you are destroyed, jump or log off on the way, the crate stays for the others.
- If two pilots reach a crate at the same moment, exactly one of them gets it.
- A crate nobody takes drifts away after **3 minutes** (it blinks in its last 10 seconds). A map holds at most 64 crates; when a new one would pass that, the oldest goes.

## Boosters

- **Loot Luck** (and the Luck Boost permanent buff) raise the chance of each loot entry when the killer makes the kill.
- **Resource Magnet** adds **25%** to the resources in every crate you collect, whoever made the kill.
