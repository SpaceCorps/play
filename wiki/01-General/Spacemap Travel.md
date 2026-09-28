# Spacemap Travel

The Spacemap is your navigational interface for traversing the SpaceCorps universe. Each company controls a sector of space, arranged in a specific topology that facilitates both safe exploration and dangerous PvP encounters.

## The Universe Structure

The universe comprises three main company sectors (Mars, Terra, Galactic) and a central PvP zone.

- **x-1 (Home Base)**: The starting map for each company (M-1, T-1, G-1). Safest zone.
- **x-2 -> x-3**: Expansion zones with progressively tougher aliens.
- **x-4 (Border)**: The gateway to the PvP sector.
- **4-x (PvP Zone)**: The central conflict zone connecting all companies.

Each [world](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) (Alpha, Beta, Gamma) has its own copy of this whole map, and where pilots may fight each other depends on it: in Alpha only in `x-4` and `4-x`, in Beta everywhere except `x-1`, in Gamma everywhere. The galaxy map colours the sectors by your world's rule.

## Visualization

The Galaxy Map below shows the real-time layout of the known universe.

```spacemap

```

## How to Travel

Spacemap travel is conducted via **Jump Gates** (Portals).

1. **Locate a Portal**: Portals are typically found at the corners or edges of a map.
2. **Navigation**: Fly your ship close to the portal structure.
3. **Activation**: Press **'J'** to initiate the jump sequence.
4. **Destination**: You will arrive at the corresponding portal in the target map.

### Jump Links

- **Standard Company Routes**: Connections flow as `1 <-> 2 <-> 3` and `2 <-> 4` and `3 <-> 4`. This forms a loop between the secondary maps (`x-2` and `x-3`) and the border map (`x-4`), with `x-1` functioning as a secure entry-point tail connected only to `x-2`.
- **PvP Access Gates**: Each company's border map (`x-4`) connects directly to a dedicated PvP sector:
  - `M-4` connects to `4-1`
  - `T-4` connects to `4-2`
  - `G-4` connects to `4-3`
- **Invasion Paths (Inter-Company Travel)**: To enter enemy company territory, you must cross through the PvP zones. For example, a Mars pilot seeking to invade Terra must fly from `M-4` into PvP sector `4-1`, cross the jump gate to PvP sector `4-2`, and then enter Terra space through `T-4`.
- **The Core Center**: All three outer PvP sectors (`4-1`, `4-2`, and `4-3`) connect directly to the center map **`4-4`**, the most dangerous and rewarding PvP zone in the universe.
