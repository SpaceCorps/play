<!-- wiki-i18n source: 1adce749be3cd1f3 -->
<!-- wiki-i18n title: Sköldar -->
# Sköldar och försvar {#shields-defense}

Defensiva moduler ger sköldkapacitet, absorberar skada och laddar om ditt försvar.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Föremålsträd {#item-tree}

Det som Monteringen tillverkar kräver först sin teknologi; håll pekaren över ett föremål för att se hur lång tid forskningen tar. Teknologiträdet, bränslet och boosten: [Forskning](/wiki/03-Mechanics/Research.md).

```tree
Light Shield Core | shield, shoddy | buy 20000 Credits | /wiki/06-Items/Shields.md#shield-cores
Basic Shield Core | shield, common | buy 2000 Thulium | /wiki/06-Items/Shields.md#shield-cores
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cores
Adaptive Core I | hybrid-generator, shoddy | buy 100000 Credits | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core II | hybrid-generator, common | buy 4000 Thulium | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core III | hybrid-generator, rare | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Absorption Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells

Light Shield Core -> Basic Shield Core => Heavy Shield Core
Adaptive Core I -> Adaptive Core II -> Adaptive Core III
Absorption Shield Cell I => Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell I => Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```
<!-- item-tree:end -->

## Sköldkärnor {#shield-cores}

Utrusta sköldkärnor för att skapa aktiva defensiva barriärer, i skeppets generatorplatser eller på dina [drönare](/wiki/03-Mechanics/Drones.md) (en drönarplats räknas som en kärnplats). Observera att tunga sköldar tynger ner din fart. En sköldkärna i en **förmågeplats** ger i stället förmågan **Shield Surge** i kolumnen Specialeffekt, en sköldreparation över tio sekunder, och ger ingen egen sköld (se [Förmågor](/wiki/03-Mechanics/Abilities.md)).

| Namn | Sällsynthet | Kapacitet | Laddningstakt | Absorption | Sköld % | Fart % | Sköldcellsplatser | Specialeffekt | Kostnad |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Light Shield Core** | Skral | 10 000 | 333/s | 45 % | +5 % | −1 % | 1 | Shield Surge I | 20 000 krediter |
| **Basic Shield Core** | Vanlig | 15 000 | 500/s | 48 % | +10 % | −3 % | 2 | Shield Surge II | 2 000 Thulium |
| **Heavy Shield Core** | Sällsynt | 25 000 | 833/s | 50 % | +20 % | −5 % | 3 | Shield Surge III | Kan bara tillverkas |

**Heavy Shield Core** tillverkas i [Monteringen](/wiki/06-Items/Overview.md#upgrading-modules) av en Basic Shield Core, med 2 000 Thulium, 20 Cataclysite, 8 Reinforced Hull Plates och 6 Velkonite Reinforced Plates från din Skylab. Den behåller förtrollningsnivån hos den kärna den förbrukar, och dess bonusar slumpas på nytt ([Modulupgraderingar](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Ta först av Basic Shield Core från ditt skepp (och ta ut dess celler ur den): en kärna som sitter på ett skepp eller bär celler förbrukas inte.

**Absorption** är den andel av varje träff som dina sköldar tar; skrovet tar resten. En sköld ensam ger **45 till 50 %**, och dess celler lägger till resten: den bästa skölden med de bästa cellerna (en Heavy Shield Core med tre Absorption Shield Cell IV) ger **80 %**, det mest ett skepp har från start. Två permanenta förstärkningar lägger till det: säsongsbutikens Shield Absorbance Boost (+0,1 punkter per nivå, 100 nivåer, 25 wipepoäng var) och Smedjans absorptionsbonusar. Dagens källor till wipepoäng (855 sammanlagt vid sina tak, som följer med över wipes; fler källor är planerade) räcker till 34 av de 100 nivåerna (+3,4 punkter), vilket med en fullt smidd uppsättning på nivån Evig blir ungefär **95 %**. Värdet är dock inte begränsat till 100 %: en angripares *sköldgenomträngning* dras av från det, så det ett skepp har över 100 % är dess marginal mot genomträngning. Se [Sköldmekanik](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-).

---

## Hybridgeneratorer (adaptiva kärnor) {#hybrid-generators-adaptive-cores-}

Adaptiva kärnor fungerar som hybridgeneratorer och kombinerar sköld- och fartförmåga. De tar både styrraketer och sköldceller i sina platser (en modul per plats, av något av slagen). Deras sköld- och fartbonus räknas som en skölds eller en motors (de fyra bästa, gånger platsens andel). De har ingen absorption: de ändrar inte ditt skepps absorption, och celler i dem ger bara kapacitet och laddning. Bara sköldar tar en andel av en träff, så celler i en adaptiv kärna kräver också en sköld på skeppet.

| Namn | Sällsynthet | Sköldbonus % | Fartbonus % | Platser | Specialeffekt | Kostnad |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **Adaptive Core I** | Skral | +5 % | +3 % | 1 | — | 100 000 krediter |
| **Adaptive Core II** | Vanlig | +8 % | +4 % | 2 | — | 4 000 Thulium |
| **Adaptive Core III** | Sällsynt | +15 % | +5 % | 3 | — | Kan bara tillverkas |

---

## Sköldceller {#shield-cells}

Sköldceller monteras inuti sköldkärnor eller adaptiva kärnor (lika många som kärnans platser) för att förstärka den kärnan. I en sköldkärna höjer de också dess absorption, i punkter, och därmed den andel av varje träff som dina sköldar tar. Det finns två familjer med fyra nivåer var: **Capacity Shield Cell** ger mest sköld och laddning, **Absorption Shield Cell** mest absorption (på varje nivå dubbelt så mycket absorption och hälften så mycket sköld och laddning som Capacity på samma nivå). Capacity hjälper ett skepp där skölden avgör striden, Absorption ett skepp där skrovet gör det. En kärna med alla platser fyllda med samma cell: en Light Shield Core (1 plats) ger 47 till 55 %, en Basic Shield Core (2 platser) 52 till 68 % och en Heavy Shield Core (3 platser) 56 till 80 %, från Capacity-celler på nivå I till Absorption-celler på nivå IV. Att ta av kärnan, eller förbruka den som givare i en sammanslagning i [Smedjan](/wiki/06-Items/Forge.md), för tillbaka dess celler till inventariet.

| Namn | Sällsynthet | Kapacitetsökning | Laddningsökning | Absorptionsökning | Kostnad |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Capacity Shield Cell I** | Skral | +3 000 | +250/s | +2 % | 30 000 krediter |
| **Capacity Shield Cell II** | Vanlig | +6 000 | +500/s | +3 % | Kan bara tillverkas |
| **Capacity Shield Cell III** | Sällsynt | +9 000 | +750/s | +4 % | Kan bara tillverkas |
| **Capacity Shield Cell IV** | Episk | +12 000 | +1 000/s | +5 % | Kan bara tillverkas |
| **Absorption Shield Cell I** | Skral | +1 500 | +125/s | +4 % | 30 000 krediter |
| **Absorption Shield Cell II** | Vanlig | +3 000 | +250/s | +6 % | Kan bara tillverkas |
| **Absorption Shield Cell III** | Sällsynt | +4 500 | +375/s | +8 % | Kan bara tillverkas |
| **Absorption Shield Cell IV** | Episk | +6 000 | +500/s | +10 % | Kan bara tillverkas |

Nivå I i varje familj säljs för 30 000 krediter. Nivå II till IV tillverkas i [Monteringen](/wiki/06-Items/Overview.md#upgrading-modules), var och en av cellen i samma familj en nivå under (en Capacity Shield Cell II av en Capacity Shield Cell I, en III av en II, en IV av en III), med Thulium, byte och Velkonite Reinforced Plates från din Skylab (2, 4 och 6 plåtar). En cell byter aldrig familj: du väljer Capacity eller Absorption när du köper nivå I. Den nya cellen behåller förtrollningsnivån hos den cell den förbrukar, och dess bonusar slumpas på nytt ([Modulupgraderingar](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Celler passar inte i en [förmågeplats](/wiki/03-Mechanics/Abilities.md); de hör hemma inuti sköldar och adaptiva kärnor.
