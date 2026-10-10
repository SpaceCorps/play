<!-- wiki-i18n source: 1433a0058afe39fa -->
<!-- wiki-i18n title: Framdrivning -->
# Framdrivning och fart {#propulsion-speed}

Framdrivningssystem avgör ditt skepps hastighet och manövrerbarhet.

## På en minut {#in-one-minute}

- **Motorer ger fart, styrraketer sitter inuti dem och höjer den.** En motor rymmer en till tre styrraketer (en Engine I en, en Engine II två, en Engine III tre), och det gör en adaptiv kärna också (dess nivå säger hur många).
- **Två familjer med fyra nivåer var.** Impulse Thruster ger mest fast fart. Momentum Thruster ger mindre fast fart och multiplicerar farten mer. I båda familjerna är varje nivå bättre än den under, i båda talen.
- **Vilken var.** Som tumregel sätter du Impulse överallt: bara i en full Engine III (tre styrraketer) kommer Momentum på nivå I och II före. [Tabellen nedan](#which-thruster-where) har siffrorna. Den snabbaste Engine III rymmer tre Impulse Thruster IV och ger 52,5.
- **Så får du dem.** Nivå I i varje familj kostar 20 000 krediter. Nivå II till IV tillverkas i Monteringen, var och en av nivån under, och en styrraket byter aldrig familj.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Föremålsträd {#item-tree}

Det som Monteringen tillverkar kräver först sin teknologi; håll pekaren över ett föremål för att se hur lång tid forskningen tar. Teknologiträdet, bränslet och boosten: [Forskning](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Engine I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I => Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Motorer {#engines}

Motorer är skeppets främsta källa till framdrivning. En motor i en **förmågeplats** ger i stället förmågan **Afterburner** i kolumnen Specialeffekt, en fartstöt i tio sekunder (längre med fler motorer), och ger ingen egen framdrivning (se [Förmågor](/wiki/03-Mechanics/Abilities.md)).

| Namn | Sällsynthet | Grundhastighet | Fartbonus % | Sköldbonus % | Platser | Specialeffekt | Kostnad |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Skral | +2 | +2 % | −2 % | 1 | Afterburner I | 20 000 krediter |
| **Engine II** | Vanlig | +4 | +4 % | −8 % | 2 | Afterburner II | Kan bara tillverkas |
| **Engine III** | Sällsynt | +6 | +5 % | −15 % | 3 | Afterburner III | Kan bara tillverkas |

**Engine II** tillverkas i [Monteringen](/wiki/06-Items/Overview.md#upgrading-modules) av en Engine I, med 1 000 Thulium, 10 Ship Fragments, 1 Power Core och 2 Velkonite Reinforced Plates. **Engine III** tillverkas där av en Engine II, med 2 000 Thulium, 60 Ship Fragments, 3 Power Cores och 3 Dark Matter Plates ([Dark Matter och Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)). Var och en behåller förtrollningsnivån hos den motor den förbrukar, och dess bonusar slumpas på nytt ([Modulupgraderingar](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Ta först av motorn som ska förbrukas från ditt skepp (och ta ut dess styrraketer ur den): en motor som sitter på ett skepp eller bär styrraketer förbrukas inte.

Motorernas sköldbonus finns i föremålsdatan, men spelet har aldrig tillämpat den: motorer försvagar inte dina sköldar, och föremålskorten utelämnar den.

---

## Styrraketer {#thrusters}

Styrraketer sätts inuti motorer eller adaptiva kärnor för att höja farten de ger. Det finns två familjer med fyra nivåer var: **Impulse Thruster** ger mest fast fart och multiplicerar farten hos motorn de sitter i lite, **Momentum Thruster** ger mindre fast fart, men multiplicerar den mer. I båda familjerna är varje nivå bättre än den under, både i fast fart och i multiplikator. En motor (eller adaptiv kärna) med styrraketer ger **sin egen grundhastighet plus styrraketernas fasta fartökningar, alltihop gånger styrraketernas fartmultiplikatorer multiplicerade med varandra** ([så beräknas hastigheten](/wiki/03-Mechanics/Speed.md)): en Engine III med tre Momentum Thruster IV ger (6 + 3 x 11,135) x 1,0935 x 1,0935 x 1,0935 = 51,5, med tre Impulse Thruster IV (6 + 3 x 14,025) x 1,02975 x 1,02975 x 1,02975 = 52,5, och en Adaptive Core II med två Impulse Thruster IV ger (0 + 2 x 14,025) x 1,02975 x 1,02975 = 29,7 (26,6 med två Momentum Thruster IV).

| Namn | Sällsynthet | Fast fartökning | Fartmultiplikator | Kostnad |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Skral | +4,25 | ×1,017 | 20 000 krediter |
| **Impulse Thruster II** | Vanlig | +8,5 | ×1,02125 | Kan bara tillverkas |
| **Impulse Thruster III** | Sällsynt | +12,75 | ×1,0255 | Kan bara tillverkas |
| **Impulse Thruster IV** | Episk | +14,025 | ×1,02975 | Kan bara tillverkas |
| **Momentum Thruster I** | Skral | +3,825 | ×1,051 | 20 000 krediter |
| **Momentum Thruster II** | Vanlig | +7,65 | ×1,0595 | Kan bara tillverkas |
| **Momentum Thruster III** | Sällsynt | +10,625 | ×1,0765 | Kan bara tillverkas |
| **Momentum Thruster IV** | Episk | +11,135 | ×1,0935 | Kan bara tillverkas |

### Vilken styrraket var {#which-thruster-where}

Impulse ger mer fast fart, Momentum multiplicerar mer, så vilken familj som är snabbast beror på vad motorn redan ger. Fast fart räknas mest där det finns lite fart att multiplicera: i en adaptiv kärna (den har ingen egen fart) och i en motor med en eller två styrraketer. En multiplikator räknas mest i en full Engine III, där det finns mycket fart att multiplicera, men där vinner bara Momentum på nivå I och II. Farten som var och en ger med styrraketer på nivå IV i alla platser:

| Var styrraketerna sitter | Med Impulse Thruster IV | Med Momentum Thruster IV | Snabbast |
| :--- | :---: | :---: | :--- |
| Engine I, 1 styrraket | 16,5 | 14,4 | Impulse |
| Engine II, 2 styrraketer | 34,0 | 31,4 | Impulse |
| Engine III, 1 styrraket | 20,6 | 18,7 | Impulse |
| Engine III, 2 styrraketer | 36,1 | 33,8 | Impulse |
| Engine III, 3 styrraketer | 52,5 | 51,5 | Impulse |
| Adaptive Core II, 2 styrraketer | 29,7 | 26,6 | Impulse |

- **Lägre nivåer.** De lägre nivåerna går likadant, med två jämna fall och ett undantag: med två styrraketer i en Engine II är familjerna jämnstarka på nivå I och II (Impulse ligger före med 0,06 och 0,24), och med två i en Engine III också (inom 0,1). Från nivå III leder Impulse i båda, med 1,5 till 2,6. Undantaget är den fulla Engine III: där leder Momentum på nivå I och II, med 0,6 och 0,9, och Impulse på nivå III och IV, med 0,5 och 1,0.
- **Den snabbaste Engine III.** Den rymmer tre Impulse Thruster IV: 52,5, lite över en Impulse och två Momentum Thruster IV (52,1) eller tre Momentum (51,5).

En bonus på en styrrakets fartmultiplikator från [Smedjan](/wiki/06-Items/Forge.md) ökar delen över 1 (en bonus på +15 % på ×1,0935 ger ×1,1075), och Smedjan slumpar ingen bonus på en multiplikator på ×1,05 eller lägre: på en Impulse Thrusters ×1,017 till ×1,02975 skulle den ge under 0,005 (+15 % på ×1,02975 ger ×1,034). En Impulse Thruster rymmer en bonus (sin fasta fart), en Momentum Thruster två.

Nivå I i varje familj säljs för 20 000 krediter. Nivå II till IV tillverkas i [Monteringen](/wiki/06-Items/Overview.md#upgrading-modules), var och en av styrraketen i samma familj en nivå under (en Impulse Thruster II av en Impulse Thruster I, en III av en II, en IV av en III), med Thulium, byte och plåtar: 2 eller 4 Velkonite Reinforced Plates från din Skylab för nivå II eller III, och 3 Dark Matter Plates för nivå IV. En styrraket byter aldrig familj: du väljer Impulse eller Momentum när du köper nivå I. Var och en behåller förtrollningsnivån hos den styrraket den förbrukar, och dess bonusar slumpas på nytt ([Modulupgraderingar](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Styrraketer passar inte i en [förmågeplats](/wiki/03-Mechanics/Abilities.md); de hör hemma inuti motorer och adaptiva kärnor.

### Köra ifrån utomjordingar {#outrunning-aliens}

Utomjordingarnas fart är 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) och 230 (Crystalys). En Ostirion med en Engine II och två styrraketer når fart 221,4 med Impulse Thruster I: fortfarande under Crystalys, så det krävs en styrraket tillverkad i Monteringen för att köra ifrån den (230,8 med Impulse Thruster II, 240,3 med III, 243,3 med IV). Momentum Thruster flyger lika snabbt eller lite lägre på det skeppet (221,4 med en Momentum Thruster I; sedan 230,5, 238,4 och 240,7 med II till IV): nivå I i båda familjerna ligger under en Crystalys, och varje nivå som tillverkas i Monteringen ligger över, nivå II med bara 0,8 och 0,5.
