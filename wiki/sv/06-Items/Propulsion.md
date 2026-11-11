<!-- wiki-i18n source: fe17f46644fd6072 -->
<!-- wiki-i18n title: Framdrivning -->
# Framdrivning och fart {#propulsion-speed}

Framdrivningssystem avgör ditt skepps hastighet och manövrerbarhet.

## På en minut {#in-one-minute}

- **Motorer ger fart, styrraketer sitter inuti dem och höjer den.** En motor rymmer en till tre styrraketer (en Engine I en, en Engine II två, en Engine III tre), och det gör en adaptiv kärna också (dess nivå säger hur många).
- **Två familjer med fyra nivåer var.** Impulse Thruster ger mest fast fart. Momentum Thruster ger mindre fast fart och multiplicerar farten mer. I båda familjerna är varje nivå bättre än den under, i båda talen.
- **Vilken var.** Som tumregel sätter du Momentum i en full Engine III (tre styrraketer) och Impulse i en adaptiv kärna; i de mindre motorerna ligger de två nära varandra på nivå I och II, och från nivå III leder Impulse. [Tabellen nedan](#which-thruster-where) har siffrorna. Den snabbaste Engine III rymmer tre Momentum Thruster IV och ger 63,3.
- **Så får du dem.** Nivå I i varje familj kostar 20 000 krediter. Nivå II till IV tillverkas i Monteringen, var och en av nivån under, och en styrraket byter aldrig familj.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Föremålsträd {#item-tree}

Det som Monteringen tillverkar kräver först sin teknologi; håll pekaren över ett föremål för att se hur lång tid forskningen tar. Teknologiträdet, bränslet och boosten: [Forskning](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Engine I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 4000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 80 Ship Fragment, 4 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 80 Ship Fragment, 4 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 4000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 4000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I => Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Motorer {#engines}

Motorer är skeppets främsta källa till framdrivning. En motor i en **förmågeplats** ger i stället förmågan **Afterburner** i kolumnen Specialeffekt, en fartstöt i femton sekunder (längre med fler motorer), och ger ingen egen framdrivning (se [Förmågor](/wiki/03-Mechanics/Abilities.md)).

| Namn | Sällsynthet | Grundhastighet | Fartbonus % | Sköldbonus % | Platser | Specialeffekt | Kostnad |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Skral | +5 | +2 % | −2 % | 1 | Afterburner I | 20 000 krediter |
| **Engine II** | Vanlig | +10 | +3 % | −8 % | 2 | Afterburner II | Kan bara tillverkas |
| **Engine III** | Sällsynt | +15 | +4 % | −15 % | 3 | Afterburner III | Kan bara tillverkas |

**Engine II** tillverkas i [Monteringen](/wiki/06-Items/Overview.md#upgrading-modules) av en Engine I, med 2 000 Thulium, 60 Ship Fragments, 1 Power Core och 4 Velkonite Reinforced Plates. **Engine III** tillverkas där av en Engine II, med 4 000 Thulium, 110 Ship Fragments, 5 Power Cores, 1 Ancient Control Unit och 4 Dark Matter Plates ([Dark Matter och Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)). Var och en behåller förtrollningsnivån och bonusarna hos den motor den förbrukar ([Modulupgraderingar](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Ta först av motorn som ska förbrukas från ditt skepp (och ta ut dess styrraketer ur den): en motor som sitter på ett skepp eller bär styrraketer förbrukas inte.

Motorernas sköldbonus finns i föremålsdatan, men spelet har aldrig tillämpat den: motorer försvagar inte dina sköldar, och föremålskorten utelämnar den.

---

## Styrraketer {#thrusters}

Styrraketer sätts inuti motorer eller adaptiva kärnor för att höja farten de ger. Det finns två familjer med fyra nivåer var: **Impulse Thruster** ger mest fast fart och multiplicerar farten hos motorn de sitter i lite, **Momentum Thruster** ger mindre fast fart, men multiplicerar den mer. I båda familjerna är varje nivå bättre än den under, både i fast fart och i multiplikator. En motor (eller adaptiv kärna) med styrraketer ger **sin egen grundhastighet plus styrraketernas fasta fartökningar, alltihop gånger styrraketernas fartmultiplikatorer multiplicerade med varandra** ([så beräknas hastigheten](/wiki/03-Mechanics/Speed.md)): en Engine III med tre Momentum Thruster IV ger (15 + 3 x 11,135) x 1,0935 x 1,0935 x 1,0935 = 63,3, med tre Impulse Thruster IV (15 + 3 x 14,025) x 1,02975 x 1,02975 x 1,02975 = 62,3, och en Adaptive Core II med två Impulse Thruster IV ger (0 + 2 x 14,025) x 1,02975 x 1,02975 = 29,7 (26,6 med två Momentum Thruster IV).

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

Impulse ger mer fast fart, Momentum multiplicerar mer, så vilken familj som är snabbast beror på vad motorn redan ger. Fast fart räknas mest där det finns lite fart att multiplicera: i en adaptiv kärna (den har ingen egen fart) och i en motor med en eller två styrraketer. En multiplikator räknas mest i en full Engine III, där det finns mycket fart att multiplicera, och där vinner Momentum på varje nivå. Farten som var och en ger med styrraketer på nivå IV i alla platser:

| Var styrraketerna sitter | Med Impulse Thruster IV | Med Momentum Thruster IV | Snabbast |
| :--- | :---: | :---: | :--- |
| Engine I, 1 styrraket | 19,6 | 17,6 | Impulse |
| Engine II, 2 styrraketer | 40,3 | 38,6 | Impulse |
| Engine III, 1 styrraket | 29,9 | 28,6 | Impulse |
| Engine III, 2 styrraketer | 45,6 | 44,6 | Impulse |
| Engine III, 3 styrraketer | 62,3 | 63,3 | Momentum |
| Adaptive Core II, 2 styrraketer | 29,7 | 26,6 | Impulse |

- **Lägre nivåer.** Från nivå III leder Impulse överallt utom i den fulla Engine III, med 0,6 till 3,1. På nivå I och II skiljer familjerna mindre än en punkt utanför den fulla Engine III: Impulse ligger före i en Engine I och i en Adaptive Core I eller II, Momentum ligger före eller jämnt i en Engine III med en eller två styrraketer och i en Engine II med två. Undantaget är den fulla Engine III: där leder Momentum på varje nivå, med 1,0 till 2,0.
- **Den snabbaste Engine III.** Den rymmer tre Momentum Thruster IV: 63,3, lite över en Impulse och två Momentum Thruster IV (63,2) eller tre Impulse (62,3).

En bonus på en styrrakets fartmultiplikator från [Smedjan](/wiki/06-Items/Forge.md) ökar delen över 1 (en bonus på +15 % på ×1,0935 ger ×1,1075), och Smedjan slumpar ingen bonus på en multiplikator på ×1,05 eller lägre: på en Impulse Thrusters ×1,017 till ×1,02975 skulle den ge under 0,005 (+15 % på ×1,02975 ger ×1,034). En Impulse Thruster rymmer en bonus (sin fasta fart), en Momentum Thruster två.

Nivå I i varje familj säljs för 20 000 krediter. Nivå II till IV tillverkas i [Monteringen](/wiki/06-Items/Overview.md#upgrading-modules), var och en av styrraketen i samma familj en nivå under (en Impulse Thruster II av en Impulse Thruster I, en III av en II, en IV av en III), med Thulium, byte och plåtar: 4 Velkonite Reinforced Plates från din Skylab för nivå II eller III, och 4 Dark Matter Plates och en Ancient Control Unit för nivå IV. En styrraket byter aldrig familj: du väljer Impulse eller Momentum när du köper nivå I. Var och en behåller förtrollningsnivån och bonusarna hos den styrraket den förbrukar ([Modulupgraderingar](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Styrraketer passar inte i en [förmågeplats](/wiki/03-Mechanics/Abilities.md); de hör hemma inuti motorer och adaptiva kärnor.

### Köra ifrån utomjordingar {#outrunning-aliens}

Utomjordingarnas fart är 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) och 230 (Crystalys). En Ostirion (grundfart 220) med en Engine II och två styrraketer når fart 246,3 med Impulse Thruster I, 255,6 med II, 265,1 med III och 268,2 med IV: varje nivå kör ifrån Crystalys, till och med Impulse Thruster I som går att köpa. Momentum Thruster flyger inom två punkter från det på det skeppet (246,7 med en Momentum Thruster I; sedan 255,9, 263,9 och 266,3 med II till IV): varje nivå i båda familjerna ligger över en Crystalys, med minst 16,3.
