<!-- wiki-i18n source: 68b8f5293ad88b67 -->
<!-- wiki-i18n title: Framdrivning -->
# Framdrivning och fart {#propulsion-speed}

Framdrivningssystem avgör ditt skepps hastighet och manövrerbarhet.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Föremålsträd {#item-tree}

Det som Monteringen tillverkar kräver först sin teknologi; håll pekaren över ett föremål för att se hur lång tid forskningen tar. Teknologiträdet, bränslet och boosten: [Forskning](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | buy 2000 Thulium | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I -> Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Motorer {#engines}

Motorer är skeppets främsta källa till framdrivning. En motor i en **förmågeplats** ger i stället förmågan **Afterburner** i kolumnen Specialeffekt, en fartstöt i tio sekunder (längre med fler motorer), och ger ingen egen framdrivning (se [Förmågor](/wiki/03-Mechanics/Abilities.md)).

| Namn | Sällsynthet | Grundhastighet | Fartbonus % | Sköldbonus % | Platser | Specialeffekt | Kostnad |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Skral | +2 | +2 % | −2 % | 1 | Afterburner I | 20 000 krediter |
| **Engine II** | Vanlig | +4 | +4 % | −8 % | 2 | Afterburner II | 2 000 Thulium |
| **Engine III** | Sällsynt | +6 | +5 % | −15 % | 3 | Afterburner III | Kan bara tillverkas |

**Engine III** tillverkas i [Monteringen](/wiki/06-Items/Overview.md#upgrading-modules) av en Engine II, med 2 000 Thulium, 60 Ship Fragments, 3 Power Cores och 6 Velkonite Reinforced Plates från din Skylab. Den behåller förtrollningsnivån hos den motor den förbrukar, och dess bonusar slumpas på nytt ([Modulupgraderingar](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Ta först av Engine II från ditt skepp (och ta ut dess styrraketer ur den): en motor som sitter på ett skepp eller bär styrraketer förbrukas inte.

Motorernas sköldbonus finns i föremålsdatan, men spelet har aldrig tillämpat den: motorer försvagar inte dina sköldar, och föremålskorten utelämnar den.

---

## Styrraketer {#thrusters}

Styrraketer sätts inuti motorer eller adaptiva kärnor för att höja farten de ger. Det finns två familjer med fyra nivåer var: **Impulse Thruster** ger mest fast fart och multiplicerar farten hos motorn de sitter i lite, **Momentum Thruster** ger mindre fast fart, men multiplicerar den mer. En motor (eller adaptiv kärna) med styrraketer ger **sin egen grundhastighet plus styrraketernas fasta fartökningar, alltihop gånger styrraketernas fartmultiplikatorer multiplicerade med varandra** ([så beräknas hastigheten](/wiki/03-Mechanics/Speed.md)): en Engine III med tre Momentum Thruster IV ger (6 + 3 x 12) x 1,14 x 1,14 x 1,14 = 62,2, med tre Impulse Thruster IV (6 + 3 x 17) x 1,02 x 1,02 x 1,02 = 60,5, och en Adaptive Core II med två Impulse Thruster IV ger (0 + 2 x 17) x 1,02 x 1,02 = 35,4 (31,2 med två Momentum Thruster IV).

| Namn | Sällsynthet | Fast fartökning | Fartmultiplikator | Kostnad |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Skral | +5 | ×1,02 | 20 000 krediter |
| **Impulse Thruster II** | Vanlig | +10 | ×1,02 | Kan bara tillverkas |
| **Impulse Thruster III** | Sällsynt | +15 | ×1,03 | Kan bara tillverkas |
| **Impulse Thruster IV** | Episk | +17 | ×1,02 | Kan bara tillverkas |
| **Momentum Thruster I** | Skral | +4 | ×1,08 | 20 000 krediter |
| **Momentum Thruster II** | Vanlig | +8 | ×1,10 | Kan bara tillverkas |
| **Momentum Thruster III** | Sällsynt | +11 | ×1,13 | Kan bara tillverkas |
| **Momentum Thruster IV** | Episk | +12 | ×1,14 | Kan bara tillverkas |

Vilken familj som är snabbast beror på var den sitter. Impulse Thruster ger mer i en adaptiv kärna och i en motor med en eller två styrraketer; Momentum Thruster på samma nivå ger mer i en Engine III där alla tre platserna är fyllda (62,2 mot 60,5 på nivå IV, och en Impulse Thruster IV med två Momentum Thruster IV, 62,3, är det bästa en Engine III kan bli).

En bonus på en styrrakets fartmultiplikator från [Smedjan](/wiki/06-Items/Forge.md) ökar delen över 1 (en bonus på +15 % på ×1,14 ger ×1,161), och Smedjan slumpar ingen bonus på en multiplikator på ×1,05 eller lägre: på en Impulse Thrusters ×1,02 eller ×1,03 vore den värd en tusendel. En Impulse Thruster rymmer en bonus (sin fasta fart), en Momentum Thruster två.

Nivå I i varje familj säljs för 20 000 krediter. Nivå II till IV tillverkas i [Monteringen](/wiki/06-Items/Overview.md#upgrading-modules), var och en av styrraketen i samma familj en nivå under (en Impulse Thruster II av en Impulse Thruster I, en III av en II, en IV av en III), med Thulium, byte och Velkonite Reinforced Plates från din Skylab (2, 4 och 6 plåtar). En styrraket byter aldrig familj: du väljer Impulse eller Momentum när du köper nivå I. Var och en behåller förtrollningsnivån hos den styrraket den förbrukar, och dess bonusar slumpas på nytt ([Modulupgraderingar](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Styrraketer passar inte i en [förmågeplats](/wiki/03-Mechanics/Abilities.md); de hör hemma inuti motorer och adaptiva kärnor.

### Köra ifrån utomjordingar {#outrunning-aliens}

Utomjordingarnas fart är 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) och 230 (Crystalys). En Ostirion med en Engine II och två styrraketer når fart 223,1 med Impulse Thruster I: fortfarande under Crystalys, så det krävs en styrraket tillverkad i Monteringen för att köra ifrån den (234,0 med Impulse Thruster II, 245,5 med III, 249,1 med IV). Momentum Thruster flyger lite lägre på det skeppet (222,6 med en Momentum Thruster I; 233,2, 242,5 och 245,8 med II till IV): nivå I i båda familjerna ligger under en Crystalys, och varje nivå som tillverkas i Monteringen ligger över.
