# Clans

Forming or joining a Clan allows you to pool resources, level up shared banking, set taxation rates, coordinate with faction members, and manage diplomacy. A clan also has work to do together: every day it gets a **daily line** of missions that ends with a boss only the clan can hurt, and the points it earns buy **permanent boosts** for every member. (On the game's Clan page a clan is called a *fleet*.)

**In one minute**

- Each season day your clan gets a [daily line](#daily-line): four missions done in order (kill aliens, fly a distance, sometimes bring down swarm bosses), then a [Clan Warden](#clan-wardens), a boss that you call and only your clan can hurt.
- Every finished step pays clan points at once: 15, 15, 20, 20 and 30, so **100 points** for a whole line.
- The Leader and the Co-Leaders spend the points on three [boosts](#clan-points-and-boosts) of ten levels each: **Damage** (up to +5%), **Thulium** (up to +10%) and **Credits** (up to +10%).
- A clan that finishes every line has bought every level on **season day 12**. Points and levels start again at every wipe.
- You need at least **three members** who did their part, and **about seven pilots** for the Warden's fight: five usually lose and ten win easily ([how big a crew](#how-big-a-crew)). A crew that is too small loses the fight: the clan then keeps the **70 points** of the four missions, but the line is not finished and pays no [reward for you](#the-reward-for-you).
- Your ship shows the boosts it has in the **Boosters window**, on a card of its own ([where you see them](#the-three-boosts)).
- The line and the boosts need a game of version 0.4.10 or later; the card in the Boosters window, 0.4.12 or later.

![The Boosters window in flight: the Clan boosts card under the timed boosters lists your clan's tag and each boost with its bonus and level](../img/wiki-img/shots/clan-boosters-window.jpg)
![Buying a level of a clan boost: the sheet shows the level, the bonus the whole fleet gets and the cost in clan points](../img/wiki-img/shots/clan-boosts.jpg)
![Summoning a Warden for the clan](../img/wiki-img/shots/clan-warden.jpg)

## Clan Progression

Clans start at Level 1 and can upgrade to Level 5. Upgrading the clan requires Credits to be paid from the **Clan Bank**. Upgrades increase member capacity and daily payout limits.

| Clan Level | Member Limit | Daily Payout Limit (Per Member) | Upgrade Cost (Credits) |
| :---: | :---: | :---: | :--- |
| **Level 1** | 10 | 1,000,000 Cr | — |
| **Level 2** | 25 | 2,000,000 Cr | 10,000,000 Cr |
| **Level 3** | 50 | 3,000,000 Cr | 100,000,000 Cr |
| **Level 4** | 75 | 4,000,000 Cr | 1,000,000,000 Cr |
| **Level 5** | 100 | 5,000,000 Cr | 10,000,000,000 Cr |

---

## Clan Economy & Taxation

Clans operate on a tax-based financial system:

### 1. Daily Taxation

- **Tax Rate**: The Leader or Co-Leaders can set a daily tax rate between **0% and 5%**.
- **Automated Collection**: Once per day (UTC), the server automatically collects taxes from all clan members.
- **Formula**: The tax is calculated as `ClanTaxRate` of each member's current Credit balance.
  - *Example*: If you have 10,000,000 Credits and the clan tax is 2%, 200,000 Credits will be deducted from your account and deposited into the Clan Bank.
  - Voluntary credit donations can also be made, up to the cap in the next section.

### 2. Donations

- **Donating**: any member can send Credits into the Clan Bank from the Clan page. The sheet shows what you can still send.
- **Donation Cap**: a pilot can send at most **1,000,000 Credits into clans in any 24 hours**, counted over every clan the pilot has been in. Leaving a clan and joining another does not give a new allowance.
- **No daily reset**: the 24 hours slide. Each donation stops counting exactly 24 hours after it was made, and the sheet tells you when the oldest one does and how much comes back. A donation over what is left is refused whole.
- The daily tax is not a donation and does not use up your allowance.

### 3. Bank Payouts

- **Payout Limits**: Clan leaders and officers can distribute credits from the Clan Bank to individual members.
- **Daily Cap**: A member cannot receive more than `1,000,000 * ClanLevel` Credits in payouts in a single calendar day (UTC).

---

## Hierarchy & Roles

Clans utilize a role-based rank structure to manage permissions:

- **Leader (Role 3)**: Has complete administrative access, including upgrading, sets taxes, diplomacy, promotions, kicking, and disbanding the clan.
- **Co-Leader (Role 2)**: Can set tax rates, payout credits, manage diplomacy, and promote/demote lower ranks.
- **Elder (Role 1)**: Trusted member who can accept new applications to the clan.
- **Member (Role 0)**: Standard player with no administrative permissions.

### Permissions Table

| Action | Leader | Co-Leader | Elder | Member |
| :--- | :---: | :---: | :---: | :---: |
| **Disband Clan** | ✅ | ❌ | ❌ | ❌ |
| **Upgrade Clan** | ✅ | ❌ | ❌ | ❌ |
| **Set Tax Rate** | ✅ | ✅ | ❌ | ❌ |
| **Payout Credits** | ✅ | ✅ | ❌ | ❌ |
| **Manage Diplomacy** | ✅ | ✅ | ❌ | ❌ |
| **Buy Clan Boosts** | ✅ | ✅ | ❌ | ❌ |
| **Summon the Clan Warden** | ✅ | ✅ | ❌ | ❌ |
| **Promote / Kick** | ✅ | ✅* | ❌ | ❌ |
| **Accept Applications** | ✅ | ✅ | ✅ | ❌ |

*\*Co-Leaders can only promote, demote, or kick members of a lower rank than themselves.*

### When the Leader Leaves

A Leader can't leave a clan that still has other members: promote a Co-Leader to Leader first (the Leader steps down to Co-Leader), or leave last, which disbands the clan. If the Leader deletes their account (Settings › Account), the lead passes to the highest-ranking member, the longest-serving on a tie; a Leader alone in the clan disbands it, bank included.

---

## Daily Line

Every clan gets one **daily line** a day: five steps, done **in order**, by the whole clan together. The first four are missions: kill so many aliens, fly so far, or on some days bring down swarm bosses. The fifth is a **Clan Warden**, a boss you call and destroy. Open **Community › Clan** and its **Operations** tab to see today's line, the open step with its bar, your own share and the time left.

### The five steps

| Step | What | Clan points |
| :---: | :--- | ---: |
| 1 | First mission | 15 |
| 2 | Second mission | 15 |
| 3 | Third mission | 20 |
| 4 | Fourth mission | 20 |
| 5 | The Clan Warden of the day | 30 |
| | **A finished line** | **100** |

- Only the **open step counts**. A kill made while step 1 is open counts for step 1 and for nothing else. When step 1 is done, step 2 opens at zero. What you kill above a step's target is not saved for the next one.
- A step pays its points **the moment it is done**. A clan that finishes the four missions and then cannot get a crew together for the Warden, or loses the fight, still keeps **70 points**; the [reward for you](#the-reward-for-you) comes only with the finished line.
- Everyone's work goes into **one shared count**: the kills of the open step's alien and the distance flown by all your members add up, so nobody has to do a step alone.

### The day

- A clan's day is a **season day**: 24 hours counted from the start of the season ([Wipe Timeline](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule)). A new line starts at the same time every day, which is not midnight UTC (the clan's daily tax still runs at midnight UTC). The Operations tab counts down to the reset.
- A line that is not finished **expires** when the day ends. The steps already done keep their points, the open step's progress is dropped, and there is no catching up. Lines run on season days 1 to 29.
- The clan's pilots who are online get a System line when the new line starts, when a step is done and **one hour before the reset** if the line is not finished.

### Difficulty tiers

Each day the game takes the **mean level of the five highest-level pilots** of the clan (all of them, if it has fewer than five) and sets the day's tier:

| Tier | Mean level | Warden |
| :--- | :--- | :---: |
| Recruit | under 4 | I |
| Veteran | 4 to under 7 | II |
| Elite | 7 or more | III |

The tier decides how many aliens the missions ask for, which alien the "heavy" step asks for and how strong the Warden is. **The points are the same in every tier.** New pilots of a low level do not pull the tier down: only the five best count.

### Who counts

- **The clan's total counts.** The bars on the Operations tab are the whole clan's.
- **Your minimum.** To share the day's reward you must do **5% of the day's work**, about eight minutes of real hunting. The tab shows it as "Your work today: 312 of 469 units". A work unit is a second of play: a kill counts as the time it takes to find and destroy that alien, and a stretch of flying as the time it takes. For a Veteran clan a Seeker is worth about 12 units, a Phantasm 22, a Bulwark 123 and 1,000 units flown about 5; the minimum is 446 to 480 units, whatever the day and the tier.
- **At least three members** must have reached their minimum before a step can be done. If a step is full and fewer have, it **waits** ("Step 3 is full but only 2 members have done their minimum"), and kills of that step's alien still add to the work of the members who made them until the third one gets there. A clan of fewer than three pilots cannot finish a step.
- **Who gets a kill.** The pilot who is paid for the kill and his group mates within 4,000 units who fired in the last 15 seconds ([Groups](/wiki/03-Mechanics/Groups.md#sharing-kills)). A clan counts a kill **once**, however many of its pilots were in the group, and the work of the kill is shared evenly between them. Two clans in one group count it once each.
- **Which kills.** Only the open step's alien: the ordinary Seeker, Phantasm, Bulwark or Goombah. Swarm ships, other pilots and the helpers of a Warden do not count as those aliens. Any world counts, and a kill counts more in a stronger world: **1 in Alpha, 1.5 in Beta, 2 in Gamma** ([Worlds](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)). A boss step counts the bosses of the [swarms](/wiki/05-Swarms/Swarms.md), one for each clan that has a pilot who dealt at least 5% of the damage.
- **Flying.** A patrol step counts the distance each pilot flies outside the safe zones; five pilots flying together add five times the distance.
- **Joining and leaving.** What you did stays counted if you leave. A pilot who joins counts from that moment.

### The seven lines

The lines come in a cycle of seven: the line of season day *d* is number 1 + ((*d* − 1) mod 7), so each one returns every seventh day. The counts are for a **Recruit / Veteran / Elite** clan. The two **Swarm Break** lines ask for swarm bosses and come only from day 4, when the [swarms](/wiki/05-Swarms/Swarms.md) appear. All counts are made for about **2.6 hours of play in all**, half an hour each for five pilots (an estimate, not a measurement).

| Line | Season days | Step 1 | Step 2 | Step 3 | Step 4 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Seeker Sweep | 1, 8, 15, 22, 29 | 150 / 300 / 425 Seeker | 115,000 / 155,000 / 185,000 units | 21 / 70 / 130 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah |
| Phantasm Purge | 2, 9, 16, 23 | 40 / 140 / 270 Phantasm | 60 / 120 / 170 Seeker | 175,000 / 230,000 / 275,000 units | 26 Phantasm / 15 Bulwark / 17 Goombah |
| Long Haul | 3, 10, 17, 24 | 290,000 / 385,000 / 460,000 units | 90 / 180 / 260 Seeker | 26 / 85 / 170 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah |
| Swarm Break I | 4, 11, 18, 25 | 75 / 150 / 220 Seeker | 3 Boss Seeker / 3 Boss Seeker / 2 Pirate Boss | 26 / 85 / 170 Phantasm | 30 Phantasm / 18 Bulwark / 21 Goombah |
| Heavy Iron | 5, 12, 19, 26 | 40 Phantasm / 24 Bulwark / 28 Goombah | 21 / 70 / 130 Phantasm | 175,000 / 230,000 / 275,000 units | 75 / 150 / 220 Seeker |
| Swarm Break II | 6, 13, 20, 27 | 75 / 150 / 220 Seeker | 21 / 70 / 130 Phantasm | 4 Boss Seeker / 1 Pirate Boss / 3 Pirate Boss | 350,000 / 460,000 / 550,000 units |
| Grand Round | 7, 14, 21, 28 | 100 / 210 / 300 Seeker | 26 / 85 / 170 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah | 230,000 / 305,000 / 365,000 units |

### The reward for you

When the line is finished, which means the Warden is destroyed, every member who reached the minimum and is still in the clan is paid, even if he is offline. A line that ends without the Warden pays no reward, whatever the four missions did. The payout is flat: it is not changed by boosts, boosters or the world.

| Tier | Credits | Thulium |
| :--- | ---: | ---: |
| Recruit | 5,000 | 20 |
| Veteran | 15,000 | 60 |
| Elite | 22,000 | 90 |

---

## Clan Wardens

A **Clan Warden** is the boss at the end of the daily line. It is not one of the public [swarms](/wiki/05-Swarms/Swarms.md) that roam a sector: your clan **calls it** and **only your clan can hurt it**. Three Wardens take turns, one a day: day 1 **Brood**, day 2 **Siege**, day 3 **Wrath**, day 4 Brood again, and so on (day 15 is a Wrath day). Each comes in three strengths, **I, II and III**, set by the clan's tier. A Warden is an alien of its own kind, like the ships of a swarm: it does not count as a Seeker, a Phantasm or any other alien. Its lasers hit hard, so a Warden is a fight for a full crew: bring about seven pilots, because five usually lose ([how big a crew](#how-big-a-crew)).

| Warden | Season days | Role | How it fights |
| :--- | :--- | :--- | :--- |
| **Brood Warden** | 1, 4, 7, 10 … | Hive keeper: split your fire | Four small **Brood Drones** heal its hull, and a new one comes every 8 seconds while fewer than four are alive. Shoot the drones first, then the Warden. |
| **Siege Warden** | 2, 5, 8, 11 … | Siegebreaker: keep moving | It roams and fires a straight [Rivet rocket](/wiki/06-Items/Rockets.md#the-twelve-rockets) at the first pilot who hit it, and it mends itself. Two **Siege Escorts** add laser fire. Keep moving and take turns being the target. |
| **Wrath Warden** | 3, 6, 9, 12 … | Warlord: beat the rage | It fights in place and mends itself. Below half its hull its lasers hit **half again as hard**. Two **Wrath Guards** add laser fire. Bring it down fast and keep your shields up. |

### Calling a Warden

- **When.** After step 4 is done. A clan has **two summons a day**, one Warden out at a time, and the day must have **at least 30 minutes** left.
- **Who.** The Leader or a Co-Leader.
- **How.** From flight: the **Summon here** button appears on the flight screen once step 4 is done, and asks you to confirm. Be outside the safe zones, in a company sector **x-2, x-3 or x-4** (any company's) of your world. The Operations tab shows the day's Warden, the summons left and why the button is dimmed, but a Warden is called from the ship.
- **Where it appears.** 3,000 to 4,500 units from your ship, in your world: only pilots of that world can reach it. The tab recommends **x-2 for a Recruit clan, x-3 for Veteran and x-4 for Elite**. The usual [PvP rules](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) of the sector you pick still hold.
- **Warm-up.** It stands shielded and passive for **90 seconds** ("powering up") and every clan pilot who is online is told where. Fly in while it warms up: when the 90 seconds are over it is armed. A capsule under the safe-zone badge on the flight screen follows it: its name, "powering up" and the time left, then "armed" with its sector and the time until it withdraws, and "enraged" once a Wrath Warden is under half its hull.
- **Only your clan.** The shots of any other clan's pilots are ignored and do not make it fight back.
- **How it ends.** When it is destroyed. It **withdraws** 40 minutes after it armed, when the day ends, when none of your clan's pilots has been out in flight on its map for 2 minutes, or when the server restarts (that summon is given back). A Warden that withdraws costs one summon, and the next call is the same Warden at full strength.

### Fighting a Warden

- **A Warden fights the first pilot who hit it**, like any boss: let the sturdiest ship of the crew start, and use [Shield Surge and Emergency Repair](/wiki/03-Mechanics/Abilities.md).
- **Bring about seven pilots, with x2 ammo** ([Lasers & Ammo](/wiki/06-Items/Lasers.md#laser-ammunition)). Five usually lose and ten win easily. The table below is the best case, and even in it three lose to every Warden and four win only against the Siege Warden I and II. In the table the smallest crew that can win has 4 to 5 pilots with x2 ammo and 6 to 8 with x1 ammo.
- **Brood:** the drones heal its hull, and a crew that ignores them loses: five pilots who shoot only the Warden all fall with about half of it standing, and ten take about a fifth longer. Kill them first: one dies in a second or less under the fire of five pilots, and the next one comes after 8 seconds.
- **Siege:** its rockets are straight and unguided, so a ship that keeps moving sidesteps most of them. Keep moving and take turns being the target.
- **Wrath:** once its hull is under half, every volley hurts half again as much, so the second half of the fight is the dangerous one. Bring the first half down fast, keep the shields up and save Emergency Repair for the rage.

### How big a crew

> [!NOTE]
> These times are **calculated** from the numbers below, not measured in play, and the table is the crew's **best case**: the crew is in the ships and gear the tier is made for, every pilot uses Shield Surge and Emergency Repair as soon as they are ready, the crew shoots the Warden's helpers first when that is better. The Warden and its helpers all fire at the pilot who hit first, and nobody dodges. **A real fight is harder than the table.** The five-pilot row is a close call even in the best case (a win that costs one or two ships), and in the same fights run in the game itself, with scripted pilots, five pilots lost most of the fights we ran, even when they used both abilities; seven won every one of theirs, and ten won easily. A crew of five that uses no ability and shoots only the Warden loses to seven of the nine Wardens; seven pilots who do the same win eight of them (all but the Brood Warden III, whose drones heal it) and lose one to three ships, and ten win all nine.

The table is the best case, with x2 ammo; in play, five pilots usually lose and about seven win.

| Crew | With x2 ammo | With x1 ammo |
| :--- | :--- | :--- |
| 3 pilots | lose to every Warden, after 4.7 to 13.8 minutes; the Warden keeps between a quarter and two thirds of its hull and shield | lose |
| 4 pilots | win only against the Siege Warden I and II, in about 8 minutes, losing 1 ship | lose |
| 5 pilots | win against every Warden in 5.3 to 6.5 minutes, losing 1 to 2 ships | lose |
| 7 pilots | win against every Warden in 3.3 to 3.6 minutes, losing 0 to 1 ships | win against every Warden but the Brood Warden II and III, in 8.7 to 12.3 minutes, losing 1 to 4 ships |
| 10 pilots | win against every Warden in 2.2 to 2.4 minutes, losing 0 to 1 ships | win against every Warden in 5.1 to 5.6 minutes, losing 1 to 2 ships |

In the best case the smallest crew that wins with x2 ammo has **4 pilots** (against the Siege Warden I and II) to **5** (against the other seven) and loses **1 to 2** ships doing it; with x1 ammo it has **6 to 8** pilots and loses 2 to 4. A crew of **seven** wins against every Warden with x2 ammo and loses at most one ship in the best case. A Warden's lasers hit for tens to over a hundred a volley at strength I (48 to 129) and thousands at strength III (1,845 to 3,090), and its helpers add to it: the ship it fights falls in one and a half to four minutes, and then it turns on the next one, so even a crew that wins loses ships.

The table is for a crew in the gear of the Warden's own tier. Weaker ships do worse: ten pilots in Recruit gear cannot kill a Veteran Warden, and ten in Veteran gear cannot kill an Elite one. The Warden of **your** clan always matches **your** tier, which the five best pilots of the clan set, so bring them.

**A clan too small for its Warden** (fewer than about seven pilots on the day) is not shut out. The four missions pay their **70 points** whatever happens to the Warden, the points buy boosts, and the clan can call the Warden again if it has a summon left (there are two a day): if the crew falls and stays away, the Warden withdraws, which costs one summon, and the next call brings it back at full strength. But the line is not finished, so nobody gets the [reward for you](#the-reward-for-you), and a clan that never kills its Warden has all 30 boost levels on season day 18 at the soonest, not on day 12 ([how long it takes](#how-long-it-takes)).

### Warden numbers

The Wardens have the same numbers in every world (the Alpha numbers), and so does their pay. Each drone, escort or guard has the numbers of the second table, and they stand with the Warden: a Brood Drone heals the Warden's hull, a Siege Escort or a Wrath Guard fires lasers. A volley is the shots of all of a ship's lasers in one second, rolled between 80 and 100% of the number shown; a Wrath Warden below half its hull hits half again as hard. The Warden and its helpers all fire at the pilot the Warden fights, so their volleys add up: a Brood Warden III with its four drones puts up to 4,350 a second on one ship. The Siege Warden's [Rivet rocket](/wiki/06-Items/Rockets.md#the-twelve-rockets) does not roll: it hits for at most **2,500** at strength I, **5,000** at II and **7,500** at III, where a pilot's Rivet rolls between a lowest and a highest number. It is straight, so a ship that keeps moving is missed.

| Warden | Hull | Shield | Laser damage (a volley a second) | Speed | Laser range | Mends itself (hull a second) | Rocket and seconds between shots |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| Brood Warden I | 166,000 | 136,000 | 129 | 90 | 600 | – | – |
| Brood Warden II | 288,000 | 236,000 | 777 | 90 | 700 | – | – |
| Brood Warden III | 1,060,000 | 870,000 | 3,090 | 90 | 800 | – | – |
| Siege Warden I | 143,000 | 117,000 | 48 | 110 | 600 | 215 | Rivet I: 24 |
| Siege Warden II | 248,000 | 203,000 | 291 | 110 | 700 | 375 | Rivet II: 12 |
| Siege Warden III | 915,000 | 745,000 | 1,845 | 110 | 800 | 1,385 | Rivet III: 8 |
| Wrath Warden I | 163,000 | 133,000 | 96 | 90 | 700 | 215 | – |
| Wrath Warden II | 282,000 | 231,000 | 582 | 90 | 800 | 375 | – |
| Wrath Warden III | 1,040,000 | 850,000 | 2,460 | 90 | 900 | 1,385 | – |

| Helper | How many | Hull | Shield | Laser damage (a volley a second) | Speed | Heals the Warden (hull a second) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Brood Drone I | 4 | 700 | 500 | 12 | 170 | 120 |
| Brood Drone II | 4 | 1,200 | 900 | 78 | 170 | 210 |
| Brood Drone III | 4 | 4,000 | 3,500 | 315 | 170 | 770 |
| Siege Escort I | 2 | 4,300 | 3,500 | 6 | 175 | – |
| Siege Escort II | 2 | 7,400 | 6,100 | 45 | 175 | – |
| Siege Escort III | 2 | 27,500 | 22,500 | 285 | 175 | – |
| Wrath Guard I | 2 | 4,900 | 4,000 | 18 | 180 | – |
| Wrath Guard II | 2 | 8,500 | 6,900 | 117 | 180 | – |
| Wrath Guard III | 2 | 31,000 | 25,500 | 495 | 180 | – |

### Pay and loot {#warden-pay-and-loot}

A Warden pays the same as a stack of the tier's heavy alien: **30 Phantasms** for a Warden I, **24 Bulwarks** for a II and **16 Goombahs** for a III. It is one pot, split by damage between the pilots who dealt at least 5% of the damage, the same way as the leader of a [swarm](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays). Your [clan boosts](#what-the-boosts-apply-to) apply to your share. In our calculation the credits cover about the x1 ammo that the smallest crew that can win burns, and x2 ammo costs more Thulium than the Warden pays: it is a fight for the points and the box. The pay did not change in 0.4.12, when the Wardens' lasers got stronger: the pot does not grow with the damage you take or the ships you lose.

| Strength of the Warden | Credits | Thulium | Experience (XP) | Honor |
| :--- | ---: | ---: | ---: | ---: |
| I | 90,000 | 360 | 9,000 | 180 |
| II | 120,000 | 600 | 19,200 | 240 |
| III | 240,000 | 1,200 | 48,000 | 384 |

The Warden drops **one box** for the pilot who dealt the most damage; it is that pilot's and his clan's for 30 seconds ([Cargo](/wiki/03-Mechanics/Cargo.md)). A chance in brackets is for each of that many rolls: (5 × 50%) is five rolls with a 50% chance each.

| Warden | Item | I | II | III |
| :--- | :--- | :---: | :---: | :---: |
| Brood Warden | Ship Fragment | 3–5 | 8–12 | 15–25 |
| Brood Warden | Advanced Plasma | 100–200 | 300–600 | – |
| Brood Warden | Daraxium | 1–2 (5 × 50%) | – | – |
| Brood Warden | Nyxite | – | 2–4 (5 × 50%) | – |
| Brood Warden | Ultra Core | – | – | 300–500 |
| Brood Warden | Quorvium | – | – | 5–10 (60%) |
| Siege Warden | Ship Fragment | 2–4 | 6–10 | 12–20 |
| Siege Warden | Siphon Battery | 100–200 | 300–500 | 800–1,200 |
| Siege Warden | Rocket bought with Credits (one kind, picked at random) | 2–3 | 5–8 | 8–12 |
| Siege Warden | Reinforced Hull Plate | – | 1 (30%) | – |
| Siege Warden | Epic rocket (one kind, picked at random) | – | – | 1–2 (50%) |
| Wrath Warden | Ship Fragment | 4–6 | 8–12 | – |
| Wrath Warden | Cataclysite | 3–5 | 5–10 | – |
| Wrath Warden | Reinforced Hull Plate | 1 (25%) | 1 (50%) | 1–2 (70%) |
| Wrath Warden | Power Core | – | 1 (15%) | 1 (35%) |
| Wrath Warden | Quorvium | – | – | 5–10 (70%) |
| Wrath Warden | Ancient Control Unit | – | – | 1 (8%) |

A Warden counts under its own name in your kill statistics and adds PvE points to your [rank](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points): **13 to 35** for the leader, by Warden and strength (a Warden III is worth the most), and **1 to 6** for each helper, more for a stronger crew.

---

## Clan Points and Boosts

Clan points belong to the clan. Every step the clan finishes adds to its balance. The **Leader and the Co-Leaders** spend it on the **Clan boosts** card of the Operations tab: three boosts of ten levels each, and every member has them at once. A purchase is final: there is no refund and no respec.

### The three boosts

| Boost | Levels | Each level | Highest level | Works on |
| :--- | :---: | :---: | :---: | :--- |
| **Clan Damage** | 10 | +0.5% | +5% | Laser damage to aliens and pilots |
| **Clan Thulium** | 10 | +1% | +10% | Thulium from kills and mission rewards |
| **Clan Credit** | 10 | +1% | +10% | Credits from kills and mission rewards |

**Where you see them.** In flight, the **Boosters window** lists the boosts your ship has on a **Clan boosts** card of its own, under the timed boosters: your clan's tag, then a row for each boost with its bonus and its level (Lv 3/10). They have no timer, because a clan boost lasts as long as you are in the clan. Hover a row to see what it works on. A clan that has bought nothing yet shows "Your clan has no boosts yet", and a pilot without a clan sees no card. The **Dashboard**'s Boosters card and a pilot's profile list them too. The card shows what your ship applies, as the server tells the game, so a level the officers have just bought shows at once. A game older than 0.4.12 applies the boosts and shows no card.

### Prices {#boost-prices}

The price of a level is **22 clan points plus 4 for every level before it**, and it is the same for the three boosts: 400 points for one boost, **1,200 for all three**, which is twelve finished lines.

| Level | Price | Total for this boost | Clan Damage | Clan Thulium | Clan Credit |
| :---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 22 | 22 | +0.5% | +1% | +1% |
| 2 | 26 | 48 | +1% | +2% | +2% |
| 3 | 30 | 78 | +1.5% | +3% | +3% |
| 4 | 34 | 112 | +2% | +4% | +4% |
| 5 | 38 | 150 | +2.5% | +5% | +5% |
| 6 | 42 | 192 | +3% | +6% | +6% |
| 7 | 46 | 238 | +3.5% | +7% | +7% |
| 8 | 50 | 288 | +4% | +8% | +8% |
| 9 | 54 | 342 | +4.5% | +9% | +9% |
| 10 | 58 | 400 | +5% | +10% | +10% |

### What the boosts apply to

- **Clan Damage** adds to all laser damage your ship deals: to aliens, swarm ships, Wardens and other pilots. It **does not touch rockets**, of any kind.
- **Clan Thulium and Clan Credit** add to the pay of alien kills (your own, your share of a boss and your share of a group kill) and to the reward of every mission you claim, level, Station and Challenge ([Quests](/wiki/03-Mechanics/Quests.md#rewards)). They **do not touch** the [Skylab](/wiki/03-Mechanics/Skylab.md#credit-farm-and-thulium-farm) farms, bank payouts, bonus codes or the reward of the daily line.
- **They add up with your other bonuses** (boosters such as the Laser Damage Booster, the buffs of the [Season Store](/wiki/03-Mechanics/Wipe-Timeline.md#the-permanent-buff-store)): the percentages are added. Laser amplifiers (Amps) are not among them: they add flat damage, and the percentages apply to the total. Five points of Clan Damage next to 50 from other sources make 55, which is 3.3% more damage than before.
- **A fraction is not lost.** A boost often adds less than one unit to a kill: 10% of a Seeker's 4 Thulium is 0.4. The game keeps the fraction and pays it with the units of your next kills, so ten Seekers pay the 4 you are owed. The fraction you hold is dropped when you log out.
- **Joining and leaving.** A pilot has the boosts from the moment he joins the clan and loses them the moment he leaves, is kicked or the clan is disbanded. The clan keeps its levels.

### How long it takes

A clan that finishes every line earns 100 points a day. If the officers buy evenly across the three boosts, it has **4 levels after the first line, 10 after the third, 16 after the fifth and all 30 on season day 12**. Fourteen lines are over when day 15 begins, so such a clan has two lines to spare. A day that is not finished still pays for the steps done: a clan that gets through the four missions but never kills its Warden earns 70 points a day and has all 30 levels on season day 18 at the soonest. After the last level the line keeps running and keeps paying the reward for you; the points go on adding to what the clan earned this season, which the hover tip of the clan points on the Clan boosts card shows.

### Points and the wipe {#clan-points-and-the-wipe}

At every wipe the clan's **points, boost levels and lines start again**, so every season is a new race to full boosts. The clan itself, its members, its bank and its tax stay as they are.

---

## Diplomacy

Clans can establish formal diplomatic relations with other organizations by entering the target clan's Tag:

- **Alliance**: Formally allied clans. Friendly status is displayed on the map.
- **NAP (Non-Aggression Pact)**: Agree not to engage in hostilities.
- **War**: Formal declaration of war. War targets can be engaged anywhere without penalty.

---

## Bringing a Friend

A friend who is new to the game can join with your personal invite code and gets a starter pack; see [Invite Friends](/wiki/03-Mechanics/Invite-Friends.md). Once in the game they can apply to your clan like any pilot.
