# Special Abilities

<!-- wiki-search: special ability; special abilities; ability; abilities; mob; mobs; regenerate; mending; shield burst; hardened plating; plating; enrage; call reinforcements; reinforcements; clones; decoy; flee and return; flee; life drain; nova pulse; nova; rocket barrage; barrage; veil; sow mines; mines; split; fragments; boss steps; ladder; three steps; warning; tell; surprise; warlord; warden; leader -->

Some aliens carry a **special ability**: one thing they do, once in their life, when their hull is half gone. Mending, a burst of shield, a flight, a call for help. Nothing shows before it starts, so every hunt can end in a surprise. This page says what each ability does and how to answer it. The bosses work differently: they change how they fight in three steps as their hull falls, and the small aliens of the last tier can split into fragments when they are destroyed too fast.

## How it works

<!-- mob-rules:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **Once.** An alien that carries an ability uses it once in its life, when its hull (not its shield) falls under 50% of its maximum in a fight. A hit that destroys it from above that line never lets it fire, and an alien that is not in a fight waits until one starts.
- **A warning first.** The ability starts with a warning: a ring closing on the ship and a word over it. An ability whose entry below says that it starts at once has no warning. The alien can still be destroyed during the warning; then nothing happens and it pays as usual. The light kinds (Seeker and Phantasm) are quicker: their warnings and their effects last 50% as long.
- **Nothing shows before it.** An alien that carries an ability looks like every other one, in every detail, until its warning starts. Nothing in the game says which one it is, not even the [Traveler's Guide](/wiki/03-Mechanics/Travelers-Guide.md).
- **Who carries one.** A small share of the aliens of the company sectors and the Danger Sectors: the stronger the tier, the larger the share, and the leaders of the swarms (Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah and Boss Crystalys) are more likely to carry one than the rest. The aliens of the Deep Void, the clan dungeons and the solo gates never carry one, and neither do the followers of a swarm, the waves of a Warden, the Dormant Force or the Tesseract.
- **It pays what any alien pays.** An alien that uses an ability pays, drops and counts exactly as one that does not: the ability adds nothing to the kill and takes time from it. The kill stays with the pilot who held it: while the alien flees, mends or hides, the claim does not run out.
- **Called ships and copies are no kills.** The ships an alien calls and the copies it makes pay nothing, drop nothing and count for no quest, statistic or ranking. At most 6 live for one caller and 24 on a map, and the map's own aliens still come back on time.
- **Everyone on the map sees it.** The pilots of the map are told when an ability starts: the game draws the ring, the word and the effect and plays a sound.

<!-- mob-rules:end -->

## The twelve abilities

An ability starts with a **warning**, unless its entry says that it starts at once: a ring that closes on the ship and a word over it. The times and numbers below are for the heavy kinds. Where a number has several values they are for the tiers named in brackets, the Greek letter in front of an alien's name.

<!-- mob-abilities:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

### Regenerate

It holds still and restores 15% / 20% / 25% / 30% (α / β / γ / δ) of its hull and shield over 6 s, and fires nothing meanwhile. Damage that adds up to 10% of its hull and shield together breaks it, and it keeps what it has restored.

- **Warning**: 1.5 s
- **The word over the ship**: MENDING
- **Carried by**: any alien
- **Answer**: Burst it down with rockets or a crowd of ships, or destroy it during the warning.

### Shield burst

A fresh shield layer of 15% / 20% / 30% / 40% (α / β / γ / δ) of its maximum hull comes on top of its shield. While it stands it takes every point of a hit; it is gone when it is spent or after 10 s.

- **Warning**: 1 s
- **The word over the ship**: SHIELD UP
- **Carried by**: any alien
- **Answer**: Ammunition and rockets that pierce shields go through it better. Or shoot another alien until it is gone.

### Hardened plating

For 7 s / 8 s / 10 s (β / γ / δ) it takes only 50% of every hit, hull and shield alike: twice as tough. It keeps fighting, and the numbers of your hits turn grey.

- **Warning**: 1.5 s
- **The word over the ship**: PLATING
- **Carried by**: the heavy kinds (Bulwark, Goombah and Crystalys) and the heavy swarm leaders (Pirate Boss and Boss Phantasm), from β up
- **Answer**: Wait it out, hit another alien meanwhile and save your bursts for after it.

### Enrage

For 10 s its damage is multiplied by ×1.3 / ×1.4 / ×1.5 / ×1.75 (α / β / γ / δ) and its speed by ×1.25.

- **Warning**: 1 s
- **The word over the ship**: ENRAGED
- **Carried by**: any alien
- **Answer**: Keep your shield up, keep moving and stay out of its range.

### Call reinforcements

4 / 6 (γ / δ) smaller aliens come in from the nearest edge of the map, in 2 waves 3 s apart. The kind that comes: Phantasm (called by Bulwark and Goombah); Bulwark (called by Crystalys). Together they have 45% / 60% (γ / δ) of its hull and shield and fire 50% of its volley. They pay nothing, drop nothing and count for nothing, and they leave after 45 s, or when the caller is destroyed.

- **Warning**: 2 s
- **The word over the ship**: CALLING
- **Carried by**: the heavy kinds (Bulwark, Goombah and Crystalys) and the heavy swarm leaders (Boss Phantasm and Boss Goombah), from γ up
- **Answer**: Destroy the caller: its ships go with it. A weapon that hits an area clears them.

### Clones

3 (γ / δ) copies of it appear round it, with its name and its look. Between them they have 18% (γ / δ) of its hull and shield; they fire nothing and pay nothing, and they last 15 s or until the real one is destroyed. The real one wears a thin ring while the copies are out, and the Target window calls a copy Decoy.

- **Warning**: 1 s
- **The word over the ship**: CLONING
- **Carried by**: any alien, from γ up
- **Answer**: Follow the ring and the moving hull bar of the real one, or use a weapon that hits an area.

### Flee and return

It flies away from its attackers at ×2 speed for 5 s / 6 s / 7 s / 8 s (α / β / γ / δ), then turns back on the first pilot who hit it. It never leaves the map or enters a safe zone, it can be hit the whole time, and the pilot who held its kill keeps it.

- **Warning**: 0.5 s
- **The word over the ship**: FLEEING
- **Carried by**: any alien
- **Answer**: Chase it, or hit it with rockets while it flies.

### Life drain

For 10 s it fires nothing else: once a second it drains every ship within its range with a full volley that nothing dodges, and it heals 75% / 100% / 100% (β / γ / δ) of the damage it deals, at most 20% of its hull in all.

- **Warning**: 1 s
- **The word over the ship**: DRAINING
- **Carried by**: the heavy kinds (Bulwark, Goombah and Crystalys) and the heavy swarm leaders (Pirate Boss, Boss Phantasm, Boss Goombah and Boss Crystalys), from β up
- **Answer**: Put a rock or a wall in the line, cloak or leave its range.

### Nova pulse

A ring grows on the ground round it during the warning. When the ring is full it hits every ship inside it once, for 4 / 5 (γ / δ) of its volleys. Its radius, in units, is 700 / 800 (γ / δ).

- **Warning**: 2.5 s
- **The word over the ship**: NOVA
- **Carried by**: the heavy kinds (Bulwark, Goombah and Crystalys) and the heavy swarm leaders (Pirate Boss, Boss Phantasm and Boss Goombah), from γ up
- **Answer**: Fly out of the ring before it fills: it is the one burst you can dodge.

### Rocket barrage

Over 3 s it fires 4 / 6 / 8 (β / γ / δ) [Rivet rockets](/wiki/06-Items/Rockets.md#the-twelve-rockets) at its target: Rivet I / II / II (β / γ / δ). They fly straight and are not guided.

- **Warning**: 1.5 s
- **The word over the ship**: BARRAGE
- **Carried by**: the heavy kinds (Bulwark, Goombah and Crystalys) and the heavy swarm leaders (Boss Phantasm and Boss Goombah), from β up
- **Answer**: Keep moving: the rockets are straight. A rock in the way stops them.

### Veil

For 6 s / 8 s (γ / δ) a ship farther than 700 units from it cannot lock on it, and a lock it held is lost. Closer than that it is seen as usual. It keeps fighting, and a blast still hurts it.

- **Warning**: none, it starts at once.
- **The word over the ship**: VEILING
- **Carried by**: the heavy kinds (Bulwark, Goombah and Crystalys) and the heavy swarm leaders (Pirate Boss, Boss Phantasm, Boss Goombah and Boss Crystalys), from γ up
- **Answer**: Close in to within 700 units.

### Sow mines

It lays 4 / 6 / 8 (β / γ / δ) mines on a ring of 500 units round the place where its target stood. A mine arms 3 s after it lands, lasts 30 s and goes off once, under the first pilot ship that flies over it, for 2 / 3 / 3 (β / γ / δ) of the alien's volleys. A mine never hurts an alien.

- **Warning**: 1.5 s
- **The word over the ship**: SOWING MINES
- **Carried by**: the heavy kinds (Bulwark, Goombah and Crystalys) and the heavy swarm leaders (Pirate Boss, Boss Phantasm, Boss Goombah and Boss Crystalys), from β up
- **Answer**: Fly round them: they are drawn on the ground, and they arm late.


<!-- mob-abilities:end -->

## Splitting

<!-- mob-split:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

The small aliens of the last tier can split when they are destroyed too fast. It belongs to the Seeker, Phantasm, Bulwark, Goombah and Crystalys of tier δ and to no other alien, and it is not one of the abilities above: an alien can have both.

- **When**: a pilot destroys it within 5 s of the first damage it took. Not every alien that dies that fast splits.
- **What comes out**: 3 aliens of the same kind and tier, 70% of its size, each with 25% of its hull and shield and a full volley, round the place where it was destroyed. They go for the pilot who destroyed it and leave after 180 s.
- **They are ordinary aliens**: each one pays what its kind pays, drops what it drops and counts for quests and statistics. They carry no ability and never split.
- **Limits**: at most 60 fragments live on a map, and they do not hold back the map's own aliens.
- **What it means**: a crew that destroys its aliens fast enough can get up to 4 kills from one alien. A crew that does not gets nothing from it.

<!-- mob-split:end -->

## The bosses' three steps

Every boss changes how it fights in three steps: when the fight starts, when its hull falls under two thirds and when it falls under a third. A step happens once and never goes back, unless the boss starts over, as said below.

<!-- mob-ladders:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **A pause at each step.** When a step that has something to do begins after the first, the boss cannot be hurt for 1.5 s (3 s for the Dungeon Warlord and the solo gate bosses).
- **A special ability as well.** Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah and Boss Crystalys can carry a special ability too (Dormant Force and Tesseract never do): it comes between the second and the third step; when the two would start together, the later one waits 3 s at most. It is never an ability the leader's own steps use.
- **Starting over.** The Tesseract starts its steps over once it has mended itself whole.

### The swarm leaders

| Leader | At the start | Under two thirds | Under a third |
| :--- | :--- | :--- | :--- |
| **Pirate Boss** | Fires a fan of 3 rockets, 12 degrees apart, at the first pilot who hit it. | Calls 5 more Pirate Scouts at once, at most 10 alive. They pay nothing and leave after 45 s. | Flies at ×1.8 speed to the nearest gate for 10 s, then turns back on the pilots. |
| **Boss Seeker** | Its Seeker Slaves mend it ×2 as fast for 8 s. | 2 copies of it appear, and the real one wears a ring. | Flies away from the pilots for 4 s, then turns back. |
| **Boss Phantasm** | Each of its Phantasm Guards puts up a shield layer of 10% of its own hull. | 3 copies of it appear, and the real one wears a ring. | Blinks about 2,500 units away from the pilots, and its Phantasm Guards come back whole round it. |
| **Boss Goombah** | Takes 50% of every hit for 6 s. | Its damage is multiplied by ×1.5 and its speed by ×1.25 for 10 s. | Mends 25% of its hull and shield (a burst of damage breaks it), and its Goombah Guards mend it ×2 as fast meanwhile. |
| **Boss Crystalys** | Takes 50% of every hit for 8 s. | A ring of 700 units hits every ship inside it for 4 of its volleys, and it fires 4 rockets. | Mends 20% of its hull and shield (a burst of damage breaks it), and 3 more Crystalys Guards come, at most 6 alive. |
| **Dormant Force** | Takes 70% of every hit while one of its Dormant Pulses lives. | Its Dormant Pulses fire a rocket every 2.5 s for 15 s. | While all its Dormant Pulses live they mend it by 5% of its hull a second for 6 s. |
| **Tesseract** | – | 20 more Facets arrive at once, above their usual number. | – |

### The Clan Wardens

| Warden | At the start | Under two thirds | Under a third |
| :--- | :--- | :--- | :--- |
| **Brood Warden** (I, II, III) | All 4 drones come to its side at once. | Its drones mend it ×1.5 as fast for 15 s. | 2 more drones come, above their usual number, for 30 s. They pay nothing. |
| **Siege Warden** (I, II, III) | – | Fires its rocket ×2 as often for 20 s. | Mends 15% of its hull and shield (a burst of damage breaks it). |
| **Wrath Warden** (I, II, III) | – | Its lasers hit ×1.25 as hard. | Its lasers hit ×1.5 as hard in all, not on top of the step before. |

### The Dungeon Warlord

- **Under two thirds**: The gap between its abilities falls to 4 s and their waits to ×0.75.
- **Under a third**: The gap falls to 2 s, their waits to ×0.5 and its damage rises to ×1.25; it casts one free Meteor volley, and its Swarm never comes back faster than every 120 s.
- **A pause at each step.** When a step begins the Warlord cannot be hurt for 3 s.

### The solo gate bosses

The six bosses of the solo gates have three steps too, their phases: they are in the table of [the bosses](/wiki/03-Mechanics/Solo-Gates.md#the-bosses) of the Solo Gates article.

<!-- mob-ladders:end -->

## Where to read more

- [Combat](/wiki/03-Mechanics/Combat.md#who-an-alien-fights): who an alien fights, and who gets its kill.
- [Swarms](/wiki/05-Swarms/Swarms.md): the leaders and their steps, one article for each swarm.
- [Clan Wardens](/wiki/03-Mechanics/Clans.md#fighting-a-warden), the [Dungeon Warlord](/wiki/03-Mechanics/Dungeons.md#the-warlord) and the [bosses of the solo gates](/wiki/03-Mechanics/Solo-Gates.md#the-bosses).
- [Traveler's Guide](/wiki/03-Mechanics/Travelers-Guide.md): what you have learned about an alien. It never says which one carries an ability.
