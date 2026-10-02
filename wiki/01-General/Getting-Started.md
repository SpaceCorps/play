# Getting Started in SpaceCorps

Welcome to the ultimate space warfare experience. As a pilot in SpaceCorps, you will represent your chosen faction to battle for galactic dominance, gather precious resources, and build your prestige in the universe.

## Core Resources

To survive and thrive, you must manage two currencies and keep an eye on your Honor. The materials you build with are on the [Resources](/wiki/05-Items/Resources.md) page, with where to get each one and what it is for:
- **Credits**: The primary standard currency, paid by every alien you defeat and by finished missions, and made by the Credit Farm of your [Skylab](/wiki/03-Mechanics/Skylab.md). Used to buy basic gear, ships, and standard equipment.
- **Thulium**: The rare radioactive ore and high-value currency, paid by every alien you defeat and by finished missions, and made by the Thulium Farm of your Skylab. Used to purchase elite weaponry, propulsion thrusters, hybrid shields, and powerful booster packs.
- **Honor**: A score, not money: a measure of your faction rank, loyalty, and standing. Earning Honor increases your rank title, but attacking friendly pilots from your own faction will heavily penalize your Honor rating: destroying a pilot of your own company, a player's ship or one of its [Company Pilots](/wiki/03-Mechanics/Company-Pilots.md), costs 100 Honor. So does hitting one in the 15 seconds before something else destroys it: softening up a company mate for an alien to finish costs as much as the kill. Killing a company mate is no PvP kill and earns no PvP points.

## Playing With Friends

Join a [Clan](/wiki/03-Mechanics/Clans.md) or fly in a [Group](/wiki/03-Mechanics/Groups.md) of up to five pilots, and bring new friends along with your personal code: **Community › Invite Friends** gives them a starter pack and you a Thulium reward when they reach level 5. See [Invite Friends](/wiki/03-Mechanics/Invite-Friends.md).

## Missions

Missions are the fastest way to level up. Open **Mission Control** from the toolbar (inside a station's safe zone) or by clicking the **Mission Control** bubble that floats above the station: 88 missions take you from level 1 to 8, ten a level in any order plus a **Special** that opens when the ten are done. Each level's missions lead you one sector further out, from your base to the border and the PvP centre. See [Quests](/wiki/03-Mechanics/Quests.md) for how they work and what every mission pays.

## Dying and Coming Back

When your hull reaches 0 the ship is destroyed and the death screen asks where you want to come back. Three places are always listed, and you choose with a click or with the keys `1`, `2` and `3` (the choice opens three seconds after the explosion, so a key you were pressing in the fight picks nothing):

| Choice | Key | Where you appear | Locked after use |
| :--- | :---: | :--- | :--- |
| **At base** | `1` | Your company's base in your world (`M-1`, `T-1` or `G-1`), inside the station's safe zone, wherever you were destroyed. | Never |
| **At the nearest portal** | `2` | Next to the portal of that sector that is nearest, in a straight line, to the place you were destroyed, 150 to 300 units from it. A sector with one portal uses it. A sector with no portal (the neutral sectors) greys this choice out. | 3 minutes |
| **On the spot** | `3` | The place where you were destroyed, in the same sector. | 5 minutes |

- **The lock starts when you respawn with that choice**, not when you die, and it belongs to that choice alone: using the portal does not lock the spot. A locked choice is greyed out on the death screen with a countdown (minutes and seconds) and opens by itself when it runs out. The locks are kept by the server: logging out and in does not reset them. A new season (the wipe) does.
- **A choice the server refuses costs nothing.** If a choice cannot be used (still locked, no portal in the sector, you changed world since you died) the lock is not spent and your ship is not moved; you pick again.
- **Protection.** A ship that comes back at a portal or on the spot cannot be damaged or locked on to for **5 seconds**, and aliens lose interest in it, so whoever destroyed you cannot destroy you again at once. The HUD shows the seconds left. Your **first shot** (a laser volley or a rocket) ends the protection, and you are told when it ends. At base the station's safe zone protects you as it always does.
- **The black hole.** A place inside the ring of radiation of the [black hole](/wiki/03-Mechanics/Black-Hole.md) (4,200 units from the centre of Danger Sector 4) is never a place to come back to: if you were destroyed there, "on the spot" puts you at the nearest point outside the ring, on the line from the centre through your place, and tells you.
- **Danger Sectors.** All three choices work there too.
- **What a destruction costs is unchanged:** you come back with your ship's base hull and empty shields, you lose no items, and the choice only decides where you appear. Your abilities are ready, and you come back uncloaked and out of any EMP window. You stay in your [group](/wiki/03-Mechanics/Groups.md).
- **Docking.** "Return to Base" on the death screen brings you back at base, as always. If the game closes before you choose, revive the ship for free in the [Hangar](/wiki/03-Mechanics/Hangar.md); you are at your base.

## Keyboard Controls & Keybindings

SpaceCorps supports customizable keyboard layout controls (accessible via the in-game Settings panel). Below are the default keybindings:

| Action | Control / Keybind | Description |
| :--- | :--- | :--- |
| **Move Ship** | `Left Click` on Spacemap | Directs your ship to fly to the clicked destination coordinates. |
| **Turn and Zoom the Camera** | `Right Drag`, `Mouse Wheel` | Right drag turns the view around your ship; the wheel (or a middle drag) zooms in and out, from 30 units away out to 1,500, which shows about 4,400 by 2,650 units of space (2.25 times the area of a 1,000-unit view). Your turn and your zoom ease back to the resting view two seconds after you let go, unless you switch on **Camera stays where I put it** in Settings › General: then the view keeps the angle and distance you gave it (the **Reset view** button next to that switch puts it back at the resting view once, and so does switching it off). **Camera Zoom** in Settings › General sets the resting distance, from 50 % to 338 % (150 % is the default); with the switch on, moving it takes the camera to the new distance. |
| **Select Target** | `Left Click` on Entity | Selects an alien, enemy pilot, or portal as your active target. The Target window (see below) shows its name, distance, hull and shield. |
| **Attack Selected Target** | `Key A` (or `Ctrl + Click`) | Starts firing your lasers and rockets at the selected target. |
| **Fire Rocket** | `Key R` | Fires the rocket you launched last (or the first on the hotbar): a guided rocket at your selected target, a straight one toward your cursor. To aim a straight rocket with the mouse, click its hotbar slot to arm it, then click in space. All rockets share a 5 second timer. |
| **Jump Portal** | `Key J` | Starts a jump when you are within 500 units of a portal (inside its safe zone). The jump takes 3 seconds (a bar over the hotbar shows it) and you must stay in range until it is done. In the Danger Sectors you cannot start one while you are under attack. |
| **Swap Configuration** | `Key C` | Swaps between Config 1 and Config 2 (swaps active lasers/shields/speed setup). |
| **Primary Hotbar** | `Digits 1 - 9` | Activates items/actions in your primary HUD hotbar slot (e.g., ammo, repair bots). |
| **Secondary Hotbar** | `Shift + Digits 1 - 9` | Activates items/actions in your secondary hotbar slots. The row shows above the primary one once it holds something; open the Ammo, Rockets or Extras picker (or drag a slot) to place an item there. |
| **Fullscreen** | `F11` or `Alt + Enter` (Windows) | Switches borderless fullscreen on or off; the button in the top right of the flight screen does the same on Windows and macOS. These two keys are fixed and don't appear among the bindings you can change. `Alt + Enter` waits while you type in the chat. |
| **Choose where to respawn** | `Keys 1 - 3` | On the death screen: `1` at base, `2` at the nearest portal, `3` on the spot. See *Dying and Coming Back* above. |
| **Target Window** | `Key V` | Shows or hides the Target window. The first button of the toolbar at the top left does the same. |
| **Group Window** | `Key B` | Shows or hides the Group window: your group's ships, hull and shield. While a group invitation waits, `Y` accepts and `Escape` denies it. See [Groups](/wiki/03-Mechanics/Groups.md). |

## The Target Window

Click an alien or a pilot and the **Target window** shows what you have selected: its name, its distance, the hull and shield bars, and whether you are firing at it. Its **crosshair** button starts and stops the attack (the same as `A`), and the **X** button drops the target (the same as `Esc`). With nothing selected it says so in one line.

It is a window like the others. Drag it by its title bar to put it anywhere, close it with the red light in its corner or with the **first button of the toolbar at the top left** (or `V`), and open it again the same way. Where you leave it and whether it is open are remembered for your account. It starts at the top of the screen, between the two toolbars. Closing it only hides the readout: your target stays selected and your attack goes on.

## When the Game Lags

Switch on **Settings › General › Show network info** and a small card appears at the top right (it keeps out of the way of the windows, and it is off until you switch it on). It tells you which side is slow:

| Reading | What it is | Good, slow |
| :--- | :--- | :--- |
| **Ping** | The round trip to the game server (the icon beside it has three bars when it is good, two when it is slow and one when it is bad; every other reading gets a triangle when it is slow and an octagon when it is bad). | Under 80 ms is good, over 150 ms is bad. |
| **Jitter**, **Snapshot age** | How evenly and how freshly the server's updates (20 a second) arrive. | Jitter under 25 ms and an age under 100 ms are good. |
| **Longest gap** | The longest time without an update from the server in the last ten seconds. | Over a second is a stall. |
| **Server** | How long the server's own 50 ms step takes (its 99th percentile). It says *n/a* when the server is too old to report it. | Under 20 ms is good, over 35 ms is bad. |
| **Client** | Your computer's frame time (95th percentile). | Under 25 ms is good, over 33 ms is bad. |

When something is bad, one line under the numbers says whose fault it is: *Network slow*, *Network lagging* or *Connection stalled* is your connection or the way to the server, *Server busy* is the server (a busy server also raises the ping and can hold the updates back), *Client slow* is your computer (lower the graphics detail), and *Client froze* means the game itself stopped drawing for a moment (an alt-tab, a minimised window). The same numbers are written to the game's log file once a minute, and at once for a stall, so a report of "it lagged at 21:10" can be answered from the log.

## Quick Pro-Tips for Beginners

1. **Configurations**: Always prepare two distinct setups. For example, use **Config 1** with all engines/thrusters in your generator slots for fast escaping or traveling, and **Config 2** with shields and lasers for combat.
2. **Safe Zones**: Portals and bases have **Safe Zones** around them. In these areas, other pilots cannot attack you, allowing you to recover shields or wait out combat cooldowns safely.
3. **Your first ability**: your starter kit already has a Repair Drone I fitted in the Protos' ability slot, so the Emergency Repair button (`E`, beside the hotbar) heals your hull over ten seconds whenever it is damaged. See [Abilities](/wiki/03-Mechanics/Abilities.md).
4. **Daily Faction Taxes**: If you are a member of a Clan, be aware that the clan treasury deducts a tax percentage (0% to 5%) from your daily Credits balance at UTC midnight. Make sure to choose your clan wisely!
