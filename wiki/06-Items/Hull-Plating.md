# Hull Plating

<!-- wiki-search: hull plate; hull plate slot; hull plate slots; plate slot; plate; armour; armor; hpl -->

The study of the Dormant swarm showed advancements in armour technology. Using this technology, ships are able to improve their hull: **Hull Plating** is armour that fits a hull plate slot of a crafted ship and adds hull points to it. It is not the Hull Plating **Booster** of the [Boosters](/wiki/06-Items/Boosters.md) page, which is a timed bonus.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Item tree

What Assembly makes needs its technology first; point at an item to see how long it takes to research. The technology tree, the fuel and the boost: [Research](/wiki/03-Mechanics/Research.md).

```tree
Hull Plating I | hull-plating, uncommon | buy 5000 Thulium | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating II | hull-plating, rare | craft 2500 Thulium, 300 s | research 86400 s, 86400 science, 25 Dark Matter | 1 Hull Plating I, 150 Ship Fragment, 20 Reinforced Hull Plate, 6 Power Core, 5 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating III | hull-plating, epic | craft 4000 Thulium, 600 s | research 172800 s, 172800 science, 40 Dark Matter | 1 Hull Plating II, 300 Ship Fragment, 40 Reinforced Hull Plate, 12 Power Core, 1 Ancient Control Unit, 8 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings

Hull Plating I => Hull Plating II => Hull Plating III
```
<!-- item-tree:end -->

## The three platings

| Item | Hull it adds | Where it comes from |
| :--- | ---: | :--- |
| **Hull Plating I** | 5,000 | Shop, 5,000 Thulium |
| **Hull Plating II** | 10,000 | Assembly, from a Hull Plating I |
| **Hull Plating III** | 15,000 | Assembly, from a Hull Plating II |

Hull Plating I is bought. **II and III are upgrades**: Assembly uses up one plating of the tier below (loose in your inventory) and asks for Thulium, materials and **Dark Matter Plates**, 5 for the II and 8 for the III, where the last tier of any other piece of equipment asks 3. Each one needs its technology first, in the Hull Plating tree of the [Research](/wiki/03-Mechanics/Research.md#tree-hull-plating) page: 1 day and 25 Dark Matter for the II, 2 days and 40 for the III, on top of the technology of the Dark Matter Plate itself. The tree above has the prices, the materials and the times.

The [Forge](/wiki/06-Items/Forge.md) takes every plating, and an upgrade keeps the Forge tier of the plating it used up and rolls its buff again. A plating has one stat, its hull, so it holds one buff, +2% to +15% by tier: a Hull Plating III at Eternal adds up to 17,250. The [Auction](/wiki/03-Mechanics/Auction.md) lists Hull Plating II and III, never Hull Plating I, which the Shop sells.

## Hull plate slots

Hull Plating fits only in **hull plate slots**, a kind of slot of its own that the four ships you craft in Assembly have besides their laser, generator, extra, ability and drone slots:

| Ship | Hull plate slots | A full set of Hull Plating III adds |
| :--- | ---: | ---: |
| **Paragon** | 5 | 75,000 |
| **Storm** | 7 | 105,000 |
| **Ironclad** | 15 | 225,000 |
| **Wraith** | 9 | 135,000 |

- **All locked at first.** A slot opens when you research it in the Skylab: one technology for each slot, 1 hour and 10 Dark Matter, in order from the first. The [Research](/wiki/03-Mechanics/Research.md#ship-technologies) view shows a ship's slots as one card with a pip for each.
- **A kind of ship, not one ship.** The slots you opened for the Paragon are open on every Paragon design too ([Ship Designs](/wiki/03-Mechanics/Ship-Designs.md)). A technology is yours for good: the wipe keeps it.
- **Both configurations share them.** The plates belong to the ship: swapping configuration leaves them on, and the Hangar shows the same plates in both.
- **Any mix.** A slot takes any Hull Plating, and two of a kind are fine.
- **Your share of hull stays.** Fitting or taking off a plate keeps the share of hull you have, so a plate never heals you and never hurts you.
- **Like any gear**, you fit and take off plates in the Hangar, or in its window from a safe zone, never in the field. A slot you have not researched refuses a plate.

In the Hangar the **Hull plates** card shows the slots. An open one takes a plate by drag and drop, as every slot does; a locked one shows a padlock and a click opens the Skylab's research. A tile beside the other stats adds up what the fitted plates give.

## How the hull adds up

A plate adds its hull to the ship's own, and the Hangar and the Ship window show the bigger number. The ship's hull plus its plates then goes through the multipliers it always did: a [Hull Plating Booster](/wiki/06-Items/Boosters.md) and the [drone formation](/wiki/03-Mechanics/Formations.md) you wear. A design that changes the hull (BUCKY has 25% more) changes the ship's own hull, and the plates come on top of that.

## Hull Plating or Hull Plating Booster? {#hull-plating-or-booster}

Two things share the name. **Hull Plating** (this page) is armour: a plate that sits in a hull plate slot of a crafted ship and adds its hull for as long as it is fitted. The **Hull Plating Booster** is a timed bonus of the [Boosters](/wiki/06-Items/Boosters.md) page, +10% max hitpoints for 10 hours on whatever ship you fly, and has nothing to fit. They add up: the plates come first and the Booster's 10% is taken from the total.
