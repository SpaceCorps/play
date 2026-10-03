# Spacemap Travel

The Spacemap is your navigational interface for traversing the SpaceCorps universe. Each company controls a sector of space, arranged in a specific topology that facilitates both safe exploration and dangerous PvP encounters.

## The Universe Structure

The universe comprises three main company sectors (Mars, Terra, Galactic) and a central PvP zone.

- **x-1 (Home Base)**: The starting map for each company (M-1, T-1, G-1). Safest zone.
- **x-2 -> x-3**: Expansion zones with progressively tougher aliens.
- **x-4 (Border)**: The gateway to the PvP sector.
- **DS-x (Danger Sectors)**: The central PvP zone connecting all companies: DS-1 to DS-4.

Only the home bases have a station. It is where **Mission Control** opens, and its safe zone reaches 1,600 units around it. The Danger Sectors have no station, `DS-1` included: the only safe zones there are the rings of 660 units around the jump gates, and Mission Control cannot be opened there; fly back to your base for your missions.

Each [world](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) (Alpha, Beta, Gamma) has its own copy of this whole map, and where pilots may fight each other depends on it: in Alpha only in `x-4` and `DS-x`, in Beta everywhere except `x-1`, in Gamma everywhere. The galaxy map colours the sectors by your world's rule.

## Visualization

The Galaxy Map below shows the real-time layout of the known universe.

```spacemap

```

## How to Travel

Spacemap travel is conducted via **Jump Gates** (Portals).

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

### Jump Links

- **The Company Loop**: Mars, Terra and Galactic have the same layout. Connections flow as `1 <-> 2 <-> 3` and `2 <-> 4` and `3 <-> 4`. This forms a loop between the secondary maps (`x-2` and `x-3`) and the border map (`x-4`), with `x-1` functioning as a secure entry-point tail connected only to `x-2`: your starting map has just one portal.
- **Danger Sector Access Gates**: Each company's border map (`x-4`) connects directly to its own Danger Sector:
  - `M-4` connects to `DS-1`
  - `T-4` connects to `DS-2`
  - `G-4` connects to `DS-3`
- **Invasion Paths (Inter-Company Travel)**: To enter enemy company territory, you must cross through the PvP zone. For example, a Mars pilot seeking to invade Terra must fly from `M-4` into Danger Sector `DS-1`, cross the jump gate to `DS-2`, and then enter Terra space through `T-4`; to reach Galactic, cross the jump gate to `DS-3` and enter through `G-4`.
- **The Danger Sector Triangle**: `DS-1`, `DS-2` and `DS-3` all connect to each other. Each of them has one company's gate (Mars in `DS-1`, Terra in `DS-2`, Galactic in `DS-3`); `DS-4` has none.
- **The Core Center**: All three outer Danger Sectors (`DS-1`, `DS-2`, and `DS-3`) connect directly to the center map **`DS-4`**, the most dangerous and rewarding PvP zone in the universe. A **black hole** hangs in the exact middle of it: the portals and the lanes between them stay well clear, but a ship that flies in feels its radiation, then its pull, and is destroyed at its event horizon. See [The Black Hole](/wiki/03-Mechanics/Black-Hole.md).
