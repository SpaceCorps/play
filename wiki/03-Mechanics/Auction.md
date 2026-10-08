# Auction

The Auction is the pilots' market and the game's own hourly lots, on one page of the station menu. Like the Shop, it is a page of the station: you use it docked, not in flight. It has four sections. **Market** is what other pilots have for sale. **Lots** are the game's own offers, one every hour. **My listings** is what you have for sale yourself. **History** is your sales, your purchases and the lots you won, and how your trading did.

<!-- market-glance:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- You need **level 5** to use the Auction: to list, to buy and to bid.
- A listing is priced per lot, in whole Credits or whole Thulium (not both), and never under the kind's least price. There is **no highest price**.
- A price in Thulium is at least the least price in Credits divided by 1,000, rounded up, and only for kinds whose least price comes to 1 Thulium or more. That is all the rate does: **1 Thulium = 1,000 Credits is a rule for the least price, not an exchange rate.** Nothing is swapped, no worth is shown, and Credits and Thulium are never added together.
- 80 kinds can be listed, and 79 of them can also be priced in Thulium.
- A listing runs for 24 / 72 / 168 hours, as you choose: the choice is the same at every level.
- The **deposit** is 1% of the price for every 24 hours the listing runs, at least 50 Credits or 1 Thulium. You pay it when you list; it is never returned, not even if you cancel.
- From level 10 the deposit is 1.5%.
- The **tax** is 5% of the price. It is taken out of what the seller receives when the listing sells.
- The deposit and the tax are burned: they go to nobody.
- From season day 28 until the wipe there is no deposit and no tax.
- From season day 30 the Auction is closed until the new season starts: nothing can be listed, bought or bid on. You can still cancel your listings.
- Each currency has its own limit on what you can sell and on what you can buy in 24 hours (the level table below). Lot wins do not count.
- Between two pilots, one buying from the other, at most 8,000,000 Credits or 40,000 Thulium pass in 24 hours.

<!-- market-glance:end -->

## Marketable items

Only items you **earned** can be sold. Everything you earn carries a small tag, **Marketable**, in the [Hangar](/wiki/03-Mechanics/Inventory.md#marketable-items): what you pick up in space (alien, swarm, Warden and black hole drops: [Cargo Boxes](/wiki/03-Mechanics/Cargo.md)), what a mission pays ([Quests](/wiki/03-Mechanics/Quests.md#rewards)) and everything the Assembly and the Forge make. What you **bought** in the Shop, won in a lot, bought on the Market, got from a bonus code, an invite pack or the starter kit, or got back as a refund is not Marketable and can never be sold again, so nothing is bought only to be resold. The plates the Skylab's Forgery makes are not Marketable either; the Reinforced Plates a mission pays are.

The tag is a number of units, not a switch: a stack of ammo can hold bought and earned rounds, and the card says "Marketable (3 of 5)". When you use part of a stack (firing, crafting) the plain units go first, so the Marketable ones last longest. Merging two pieces in the [Forge](/wiki/06-Items/Forge.md#merge) keeps the tag only when both pieces had it, and the merge preview says so; a Forge step that fails gives its materials back as plain units.

The Hangar's **Marketable only** chip shows only what you can sell, and the **gavel** beside the trash of a tagged item opens the Auction's sell sheet for it. In the Assembly, a recipe whose result is Marketable says so, and a material you are short of has a link that opens the Auction with its name in the search box.

When the Auction came (0.4.12) the gear you already held that the Shop does not sell, and the resources, were tagged once. These were not, because the Shop once sold them or because what you hold mixes bought and earned pieces: the Quantum Laser III, the Absorption Shield Cells II and III, the Impulse Thrusters II and III, the two Reinforced Plates, and the oldest Base CPU I of each pilot (the starter kit's). New ones of them that you earn or craft are tagged.

## What can be sold

<!-- market-kinds:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Type | Kinds you can sell | Number |
| :--- | :--- | ---: |
| **Lasers** | Quantum Laser I, Quantum Laser II, Quantum Laser III, Starfire-III, Helios Beam | 5 |
| **Laser amps** | Damage Amp I, Crit Amp I, Penetration Amp I, Damage Amp II, Crit Amp II, Penetration Amp II, Damage Amp III, Crit Amp III, Penetration Amp III, Damage Amp IV, Crit Amp IV, Penetration Amp IV | 12 |
| **Shield cores** | Light Shield Core, Basic Shield Core, Heavy Shield Core | 3 |
| **Engines** | Engine I, Engine II, Engine III | 3 |
| **Adaptive Cores** | Adaptive Core I, Adaptive Core II, Adaptive Core III | 3 |
| **Shield cells** | Absorption Shield Cell I, Capacity Shield Cell I, Absorption Shield Cell II, Capacity Shield Cell II, Absorption Shield Cell III, Capacity Shield Cell III, Absorption Shield Cell IV, Capacity Shield Cell IV | 8 |
| **Thrusters** | Impulse Thruster I, Momentum Thruster I, Impulse Thruster II, Momentum Thruster II, Impulse Thruster III, Momentum Thruster III, Impulse Thruster IV, Momentum Thruster IV | 8 |
| **Laser ammo** | Standard Battery (in lots of 100), Siphon Battery (in lots of 10), Advanced Plasma (in lots of 10), Ultra Core (in lots of 10), Experimental Fusion Core | 5 |
| **Rockets** | Ember I, Lancet I, Rivet I, Scatter I, Ember II, Lancet II, Rivet II, Scatter II, Ember III, Lancet III, Rivet III, Scatter III | 12 |
| **Extras** | Repair Drone I, Repair Drone II, Repair Drone III, EMP Charge, Repair Drone IV, Cloaking CPU S, Base CPU I, Cloaking CPU M, Auto-Repair CPU, Cloaking CPU L, Base CPU II | 11 |
| **Resources** | Cataclysite (in lots of 100), Ship Fragment (in lots of 100), Daraxium (in lots of 100), Nyxite (in lots of 100), Quorvium (in lots of 10), Reinforced Hull Plate (in lots of 10), Power Core, Velkonite Reinforced Plate, Dark Matter, Orvium Reinforced Plate | 10 |

<!-- market-kinds:end -->

Ships, drones, drone formations, boosters and subscriptions can never be sold, nor the Ancient Control Unit, the Velkonite and Orvium ores, the Dark Matter Plate, the Jump CPU, the Extra Slots CPUs, the N.U.K.E. and the N.I.K.E. Dark Matter Plates are not on the Auction at all, neither as goods nor as a price. An item that is equipped, fitted into another item, holding modules or in the [Transport Cache](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) cannot be listed, and neither can a Cloaking CPU, an EMP Charge or a Base CPU that has been used. Ammo and rockets are sold from the station: land your ship first.

## Selling

Press **Sell an item** (or the gavel in the Hangar), pick what you earned (a category drop-down narrows the list, with the same categories as the Market), choose Credits or Thulium, set the price of one lot and how long the listing runs: 1, 3 or 7 days. The sheet shows the least price, three chips that fill in a price (**Minimum**; **Quick sale**, one under the lowest listing now; and **Fair**, the price of the last sale), and the deposit, the tax and what you receive, before you list. Under the price, **Similar listings** charts the prices the same item and enchant is listed at now, in the currency you chose: your price is a line on it, the least price, the last sale and the Shop's price are marked, a line in words says where your price would stand, and the three cheapest listings are shown. A piece is a lot of one; ammo and some resources are sold in lots of 10 or 100, and you sell a whole number of lots. What you list leaves your inventory and is held by the server until it sells, you cancel it or it runs out; then it comes back, with its tag. You can cancel at any time, even in the last days of a season. A listing is a snapshot: to change a price, cancel the listing and list it again (the deposit is paid again).

Every kind has a **least price**, and there is **no highest price**: ask what you like. The table shows the least price of a few kinds.

<!-- market-bands:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Kind | Sold in lots of | Least price, Credits | Least price, Thulium |
| :--- | ---: | ---: | ---: |
| Quantum Laser II | 1 | 32,000 | 32 |
| Quantum Laser III | 1 | 170,000 | 170 |
| Helios Beam | 1 | 1,600,000 | 1,600 |
| Absorption Shield Cell IV | 1 | 1,100,000 | 1,100 |
| Heavy Shield Core | 1 | 870,000 | 870 |
| Impulse Thruster IV | 1 | 980,000 | 980 |
| EMP Charge | 1 | 40,000 | 40 |
| Cloaking CPU S | 1 | 400,000 | 400 |
| Ultra Core | 10 | 800 | 1 |
| Lancet I | 1 | 200 | 1 |
| Ship Fragment | 100 | 600 | 1 |
| Dark Matter | 1 | 33,000 | 33 |

<!-- market-bands:end -->

A price in Thulium follows one rule: the least price in Credits divided by the rate, rounded up. The rate is not a value the game puts on Thulium. It is only how the least Thulium price is worked out, and because of it a Thulium listing can be cheap for a pilot who has Thulium. Most sellers will ask Credits. Every kind but **Quorvium** can be priced in Thulium, the cheap ones too (ammo, rockets, the common resources): their least price is then 1 Thulium, the smallest step. Quorvium alone is Credits only, because 1 Thulium would be more than a lot of it is worth.

Your **open listings** (and a listing an admin has put on hold) use up slots. As you level up you get more slots, up to a top, and you may sell and buy more a day. How long a listing may run is the same at every level.

<!-- market-limits:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Level | Open listings | Longest listing | A day, Credits | A day, Thulium | Deposit per 24 h |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 5 | 20 | 168 h | 4,500,000 | 22,500 | 1% |
| 6 | 40 | 168 h | 6,000,000 | 30,000 | 1% |
| 7 | 70 | 168 h | 7,500,000 | 37,500 | 1% |
| 8 | 100 | 168 h | 8,500,000 | 42,500 | 1% |
| 9 | 100 | 168 h | 10,000,000 | 50,000 | 1% |
| 10 | 100 | 168 h | 15,000,000 | 75,000 | 1.5% |
| 11 | 100 | 168 h | 15,000,000 | 75,000 | 1.5% |
| 12 | 100 | 168 h | 15,000,000 | 75,000 | 1.5% |
| 13 | 100 | 168 h | 20,000,000 | 100,000 | 1.5% |
| 14 | 100 | 168 h | 20,000,000 | 100,000 | 1.5% |
| 15 | 100 | 168 h | 20,000,000 | 100,000 | 1.5% |
| 16 | 100 | 168 h | 20,000,000 | 100,000 | 1.5% |
| 17 | 100 | 168 h | 20,000,000 | 100,000 | 1.5% |
| 18 | 100 | 168 h | 20,000,000 | 100,000 | 1.5% |
| 19 | 100 | 168 h | 20,000,000 | 100,000 | 1.5% |
| 20 and up | 100 | 168 h | 20,000,000 | 100,000 | 1.5% |

<!-- market-limits:end -->

## Fees

A listing costs a **deposit**, paid when you list and never returned, and a sale costs a **tax**, taken from what the seller receives. Both are paid in the currency of the listing and **burned**: they go to nobody, so nobody gains by trading with himself. In the last two days of a season there is no deposit and no tax.

<!-- market-fees:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Listing | Price | Deposit | Tax | The seller receives |
| :--- | ---: | ---: | ---: | ---: |
| Quantum Laser III: level 6, 24 h | 170,000 Credits | 1,700 Credits | 8,500 Credits | 161,500 Credits |
| Quantum Laser III: level 10, 72 h | 170 Thulium | 8 Thulium | 8 Thulium | 162 Thulium |
| Helios Beam: level 12, 168 h | 2,500,000 Credits | 262,500 Credits | 125,000 Credits | 2,375,000 Credits |
| Helios Beam: level 12, 168 h, in the last days of a season | 2,500,000 Credits | 0 Credits | 0 Credits | 2,500,000 Credits |

<!-- market-fees:end -->

## Buying

The **Market** lists what other pilots sell. Narrow the list with the **category chips** (one for each type of item, with the number of listings in it), search by name, filter by enchant and currency, and sort by price, by what ends soonest or by what is newest. Pick a listing to see what it is, who sells it, how long it runs, and how its price compares with the last sale, the lowest price now and the Shop's price. A stack is bought in whole lots. A big purchase asks you to confirm once more. The seller is paid at once, less the tax; you pay no deposit and no tax. What you buy is **not Marketable**: the page says "You get: not marketable" beside **Buy**, because only what you earn can be sold. You cannot buy your own listing. A listing that sells while you look at it says "That listing is gone."

## Limits

Each currency has its own daily limit on what you can sell and on what you can buy, counted over the last 24 hours, and a limit on what passes between two pilots, so a second account is no quick way to move a fortune. Credits and Thulium are never added together: a pilot who sells for Thulium uses his Thulium limit, and nothing else. The sell sheet warns you when a sale would pass your daily selling limit, and the Market says so, and keeps **Buy** off, when a purchase would pass your daily buying limit. The limits grow with the level, and Premium changes none of them. Lot wins do not count.

Rockets in a listing, in a lot you lead and in your hold all count toward the most of a rocket you may carry: a listing cannot be used to carry more than the Shop's stack allows.

## My listings and History

**My listings** shows your slots, each listing with its state (open, sold, cancelled, expired, returned or on hold), a **Cancel** button, **List again** for a closed one and an **Undercut** chip when another listing of the same item asks less. A listing that ran out comes back to your inventory by itself. **History** opens with your trading of the last 30 days: your sales and purchases, what you earned and spent, the fees and taxes you paid, your net result, your best sale, your average sale and the item you traded most, and two line charts, what you earned each day and your result so far (for Credits or for Thulium, one at a time). Under them is the list of what you sold, bought and won, with the tax. The game keeps the ledger of the Auction for 90 days.

You are told when something sells: a toast, the Auction's sound and the new balance, and a badge on the Auction entry while the page is closed. A burst of sales is one toast. The Auction has its own quiet sounds, one for each thing you do or that happens to you there (posting, ending, a sale, a bid, being outbid, winning), and they follow the Interface volume.

## The hourly Lots

The Lots are the game's own offers: ammo, rockets and EMP Charges, every hour, for bids. They are a way to buy ammo for less than the Shop asks, and a sink: the winning bid is burned. Only the lots listed in the day table below ever open (never x1 or x4 ammo, never Siphon Batteries, never a special rocket), in the Shop's own currency. A rocket lot is never more than the most of that rocket you may carry (the Shop's stack), so a bid that would take you over it is refused: bid on a rocket lot when you carry little of that rocket.

<!-- market-lots:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- A new lot opens at the start of every UTC hour and stays open for 4 hours, so 4 are open at once.
- The opening bid is 40% of the Shop price of the goods. A bid after that must be at least 5% over the high bid, and at least 100 Credits or 1 Thulium more.
- Your bid is paid at once and held. If someone outbids you, it comes back to you at once.
- A bid in the last 2 min of a lot moves its end to 2 min after the bid, at most 5 times.
- What you win is for flying, not for trading: it is never Marketable. The winning bid is burned. A lot nobody bids on is not sold and costs nobody anything.
- How big a lot is follows the pilots of level 5 or more who looked at the Auction in the last 3 days: with none it is 10% of the size in the table, with 30 or more the full size, in steps of 500 for ammo, 50 for rockets and 1 for EMP Charges.
- No lot is made in the last 6 hours of a season. The wipe cancels the lots that are still open, and every bid goes back.

<!-- market-lots:end -->

<!-- market-day:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| UTC hour | Lot | Full size | Paid in | Opening bid at full size |
| :--- | :--- | ---: | :--- | ---: |
| 00:00 | Scatter III | 1,250 | Thulium | 2,500 Thulium |
| 01:00 | Advanced Plasma | 25,000 | Thulium | 5,000 Thulium |
| 02:00 | Lancet I | 12,500 | Credits | 2,500,000 Credits |
| 03:00 | EMP Charge | 5 | Thulium | 1,000 Thulium |
| 04:00 | Ultra Core | 25,000 | Thulium | 10,000 Thulium |
| 05:00 | Rivet II | 5,000 | Credits | 1,600,000 Credits |
| 06:00 | Advanced Plasma | 10,000 | Thulium | 2,000 Thulium |
| 07:00 | Advanced Plasma | 50,000 | Thulium | 10,000 Thulium |
| 08:00 | Ember I | 12,500 | Credits | 2,500,000 Credits |
| 09:00 | Ultra Core | 50,000 | Thulium | 20,000 Thulium |
| 10:00 | Scatter II | 5,000 | Credits | 1,600,000 Credits |
| 11:00 | EMP Charge | 5 | Thulium | 1,000 Thulium |
| 12:00 | Advanced Plasma | 50,000 | Thulium | 10,000 Thulium |
| 13:00 | Lancet III | 1,250 | Thulium | 2,500 Thulium |
| 14:00 | Ultra Core | 10,000 | Thulium | 4,000 Thulium |
| 15:00 | Advanced Plasma | 25,000 | Thulium | 5,000 Thulium |
| 16:00 | Ultra Core | 50,000 | Thulium | 20,000 Thulium |
| 17:00 | Rivet I | 12,500 | Credits | 2,500,000 Credits |
| 18:00 | Advanced Plasma | 50,000 | Thulium | 10,000 Thulium |
| 19:00 | Ember II | 5,000 | Credits | 1,600,000 Credits |
| 20:00 | Ultra Core | 25,000 | Thulium | 10,000 Thulium |
| 21:00 | Advanced Plasma | 25,000 | Thulium | 5,000 Thulium |
| 22:00 | Advanced Plasma | 10,000 | Thulium | 2,000 Thulium |
| 23:00 | EMP Charge | 5 | Thulium | 1,000 Thulium |

<!-- market-day:end -->

When few pilots use the Auction the lots are small, so a handful of pilots is not offered thousands of rounds every hour; they grow as more pilots look.

## The season and the wipe

The Auction follows the season (see [Wipe Timeline](/wiki/03-Mechanics/Wipe-Timeline.md)). In the last two days there are no fees. From day 30, when the wipe's five-minute countdown starts, it is closed: nothing is listed, bought or bid on, a lot that falls due then is cancelled and its bid returned, and you can still cancel your own listings. A listing never runs past the end of the season.

At the wipe, **every open listing comes back to its seller** as loose items, and the wipe then clears loose items like any other (only what you put in the [Transport Cache](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) stays): so sell, or cancel and cache what you want to keep. The lots that are still open are cancelled and the bids refunded. Credits and Thulium are not wiped.

## What the Auction does not give you

The Auction is for trading what you earn, and it is honest about its limits.

- **Selling loot is not a grind.** Raw alien drops are resources only and are worth 0.4 to 0.9 percent of what the same level-5 hunting hour pays in kills. What the Market gives a new pilot is the gear his missions pay and does not need (once), the resources of the Challenge missions, the boxes of the swarm bosses, and what he crafts.
- **There is no dealer.** Buy orders, where a pilot says what he wants to buy and for how much, are not in this version. Until they are, the only merchants are the crafter, who buys materials, makes gear in the Assembly and sells it, and the warehouse pilot, who keeps stock in the Transport Cache through the wipe.
- **Shop gear is not for resale.** Gear you bought from the Shop can't be sold again: that includes the Quantum Laser I and II, the Light and Basic Shield Cores, Engine I and II, the first tier of cells and thrusters, the amps the Shop sells, and bought ammo. The one Marketable Quantum Laser II a pilot has is the one a mission pays once.
- **Plates come from missions.** The Velkonite and Orvium Reinforced Plates on the Market are the ones the Challenge missions pay. The Forgery's plates stay out, or they would be the biggest good of the Market.

If a listing looks wrong, report it in the usual way: the game's administrators can put a listing on hold, return it, pause the Auction or ban a pilot from it, and every such action is recorded.
