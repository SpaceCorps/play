# Spacemap Travel

The Spacemap is your navigational interface for traversing the SpaceCorps universe. Each company controls a sector of space, arranged in a specific topology that facilitates both safe exploration and dangerous PvP encounters.

![Galaxy Gates](../img/wiki-img/shots/gates.jpg)
![Sector DS-1 as the game draws it](../img/wiki-img/shots/sector-DS-1.jpg)
![Sector DS-2 as the game draws it](../img/wiki-img/shots/sector-DS-2.jpg)
![Sector DS-3 as the game draws it](../img/wiki-img/shots/sector-DS-3.jpg)
![Sector DS-4 as the game draws it](../img/wiki-img/shots/sector-DS-4.jpg)
![Sector G-1 as the game draws it](../img/wiki-img/shots/sector-G-1.jpg)
![Sector G-2 as the game draws it](../img/wiki-img/shots/sector-G-2.jpg)
![Sector G-3 as the game draws it](../img/wiki-img/shots/sector-G-3.jpg)
![Sector G-4 as the game draws it](../img/wiki-img/shots/sector-G-4.jpg)
![Sector M-1 as the game draws it](../img/wiki-img/shots/sector-M-1.jpg)
![Sector M-2 as the game draws it](../img/wiki-img/shots/sector-M-2.jpg)
![Sector M-3 as the game draws it](../img/wiki-img/shots/sector-M-3.jpg)
![Sector M-4 as the game draws it](../img/wiki-img/shots/sector-M-4.jpg)
![Sector T-1 as the game draws it](../img/wiki-img/shots/sector-T-1.jpg)
![Sector T-2 as the game draws it](../img/wiki-img/shots/sector-T-2.jpg)
![Sector T-3 as the game draws it](../img/wiki-img/shots/sector-T-3.jpg)
![Sector T-4 as the game draws it](../img/wiki-img/shots/sector-T-4.jpg)
![The Star System map: the sectors, the PvP sectors, the gates and the company routes, with the portal ring that joins each company's x-4 sector to the next company's x-3 sector](../img/wiki-img/shots/star-system.jpg)

## The Universe Structure

The universe comprises three main company sectors (Mars, Terra, Galactic) and a central PvP zone.

- **x-1 (Home Base)**: The starting map for each company (M-1, T-1, G-1). Safest zone.
- **x-2 -> x-3**: Expansion zones with progressively tougher aliens.
- **x-4 (Border)**: The gateway to the PvP sector, and to another company's `x-3` (the Ring, below).
- **DS-x (Danger Sectors)**: The central PvP zone connecting all companies: DS-1 to DS-4. From season day 11 it also holds pulsars with giant excavators and the Dormant Swamp ([Danger Sectors](/wiki/01-General/Danger-Sectors.md)).

Only the home bases have a station. It is where **Mission Control** opens, and its safe zone reaches 1,600 units around it. The Danger Sectors have no station, `DS-1` included: the only safe zones there are the rings of 660 units around the jump gates, and Mission Control cannot be opened there; fly back to your base for your missions.

Each [world](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) (Alpha, Beta, Gamma) has its own copy of this whole map, and where pilots may fight each other depends on it: in Alpha only in `x-4` and `DS-x`, in Beta everywhere except `x-1`, in Gamma everywhere. The galaxy map colours the sectors by your world's rule.

## Visualization

The Galaxy Map below shows the real-time layout of the known universe. In the game the same chart is the **Star System** window.

```spacemap

```

With a [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) fitted, the chart also picks your destination: press the CPU's hotbar slot (**JMP**) and the Star System window opens in picking mode. The sectors the CPU can take you to are lit; your own sector and the Danger Sectors are not. Point at a lit sector to read the price, click it, and confirm the jump when the chart asks (500 Thulium).

## How to Travel

Spacemap travel is conducted via **Jump Gates** (Portals). A [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) is the other way: it needs no gate (see the end of this page).

1. **Locate a Portal**: Portals are typically found at the corners or edges of a map.
2. **Navigation**: Fly your ship close to the portal structure.
3. **Activation**: Press **'J'** within 500 units of the portal to start the jump.
4. **Wait for it**: The jump **takes 3 seconds**. A bar over your hotbar ("Jumping…") fills meanwhile, and the portal glows brighter as it charges; other pilots see the same charge on the portal when you jump. Your ship keeps flying, but you have to stay within 500 units of the portal until the time is up: fly out of range and the jump is called off ("Portal too far to jump.", and the bar turns red). Pressing **'J'** again while you jump does nothing but tell you so.
5. **Destination**: You will arrive at the corresponding portal in the target map.

### Jumping Under Fire

- **Outside the Danger Sectors**, being attacked, by aliens or by other pilots, does **not** interrupt your jump: it completes.
- **In the Danger Sectors (`DS-1` to `DS-4`)** you cannot jump out while you are being attacked. If a pilot or an alien has hit your ship (its shields or its hull) in the last **10 seconds**, the jump will not start ("You are under attack: you cannot jump out of a Danger Sector."), and a hit while you are jumping cancels the jump (the bar turns red and the game tells you why). Damage you take from the black hole's radiation is not an attack, and neither is a shot that a safe zone stopped. A hit you took on the map you jumped from does not follow you through the portal: you arrive with a clean record.
- You do one thing at a time: you cannot collect a [cargo crate](/wiki/03-Mechanics/Cargo.md) while you jump, and starting a jump gives up a pickup you had begun.
- Closing the game or returning to base in the middle of a jump cancels it: you do not arrive.
- **A CPU's warp charges like a portal jump.** A Jump CPU charges for 5 seconds and a Base CPU for 10, with a bar over the hotbar. A shot you fire or a hit you take, in any sector, cancels the warp (nothing is paid or used), and neither CPU starts within 10 seconds of a shot or a hit. Press the CPU's slot again to cancel it yourself.

### Jump Links

- **The Company Loop**: Mars, Terra and Galactic have the same layout. Connections flow as `1 <-> 2 <-> 3` and `2 <-> 4` and `3 <-> 4`. This forms a loop between the secondary maps (`x-2` and `x-3`) and the border map (`x-4`), with `x-1` functioning as a secure entry-point tail connected only to `x-2`: your starting map has just one portal.
- **Danger Sector Access Gates**: Each company's border map (`x-4`) connects directly to its own Danger Sector:
  - `M-4` connects to `DS-1`
  - `T-4` connects to `DS-2`
  - `G-4` connects to `DS-3`
- **The Ring**: Each company's border map (`x-4`) has one more gate, to the `x-3` of the **next company**, and every `x-3` has the gate back. The three links make a ring round the Danger Sectors, so every company has one way out and one way in:
  - `M-4` connects to Terra's `T-3`
  - `T-4` connects to Galactic's `G-3`
  - `G-4` connects to Mars' `M-3`

  The ring is open to every pilot, whatever company they fly for: it is a second way to travel between the companies' maps that does not cross the PvP zone. A ring gate stands in a corner of its own, away from the other gates of its map, with the usual safe zone of 660 units around it, and the jump works as at any gate. Where you may be attacked on the other side depends on your world, as everywhere: in Alpha `T-3` is not a PvP sector but `T-4` is, in Beta both are, in Gamma every sector is.
- **Invasion Paths (Inter-Company Travel)**: There are two ways into another company's territory through the gates. The short one is the Ring: a Mars pilot flies from `M-4` through the ring gate into Terra's `T-3` (three jumps from the Mars base, `M-1` → `M-2` → `M-4` → `T-3`), and on to `T-4` or `T-2`; Galactic's `G-4` leads into Mars' `M-3` and Terra's `T-4` into Galactic's `G-3` the same way. The long one crosses the PvP zone: from `M-4` into Danger Sector `DS-1`, across the jump gate to `DS-2`, and into Terra space through `T-4`; to reach Galactic, cross the jump gate to `DS-3` and enter through `G-4`.
- **The Danger Sector Triangle**: `DS-1`, `DS-2` and `DS-3` all connect to each other. Each of them has one company's gate (Mars in `DS-1`, Terra in `DS-2`, Galactic in `DS-3`); `DS-4` has none.
- **The Core Center**: All three outer Danger Sectors (`DS-1`, `DS-2`, and `DS-3`) connect directly to the center map **`DS-4`**, the most dangerous and rewarding PvP zone in the universe. A **black hole** hangs in the exact middle of it: the portals and the lanes between them stay well clear, but a ship that flies in feels its radiation, then its pull, and is destroyed at its event horizon. See [The Black Hole](/wiki/03-Mechanics/Black-Hole.md). From season day 11 the top-left corner of `DS-4` holds the [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md), whose guns fire on every ship they see.

### The Jump CPU

The [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) takes your ship to any company sector of your world without a gate, for 500 Thulium a jump, enemy home sectors included. It never goes to a Danger Sector, it does not start in a fight, and you research it first in the Skylab's Research Centre ([Research](/wiki/03-Mechanics/Research.md)). The [Base CPUs](/wiki/06-Items/Extras.md#base-cpus) take you home the same way. A warp CPU, the Jump CPU or a Base CPU, is refused while you carry a quest item ("You can't use a warp CPU while carrying a mission item."): fly home through the gates ([Quest items](/wiki/03-Mechanics/Quests.md#quest-items)).
