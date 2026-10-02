<!-- wiki-i18n source: 301d58f06f810979 -->
<!-- wiki-i18n title: Sköldar -->
# Sköldar och försvar {#shields-defense}

Defensiva moduler ger sköldkapacitet, absorberar skada och laddar om ditt försvar.

## Sköldkärnor {#shield-cores}

Utrusta sköldkärnor för att skapa aktiva defensiva barriärer, i skeppets generatorplatser eller på dina [drönare](/wiki/03-Mechanics/Drones.md) (en drönarplats räknas som en kärnplats). Observera att tunga sköldar tynger ner din fart. En sköldkärna i en **förmågeplats** ger i stället förmågan **Shield Surge** i kolumnen Specialeffekt, en sköldreparation över tio sekunder, och ger ingen egen sköld (se [Förmågor](/wiki/03-Mechanics/Abilities.md)).

| Namn | Sällsynthet | Kapacitet | Laddningstakt | Absorption | Sköld % | Fart % | Sköldcellsplatser | Specialeffekt | Kostnad |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Light Shield Core** | Skral | 10 000 | 333/s | 45 % | +5 % | −1 % | 1 | Shield Surge I | 20 000 krediter |
| **Basic Shield Core** | Vanlig | 15 000 | 500/s | 48 % | +10 % | −3 % | 2 | Shield Surge II | 2 000 Thulium |
| **Heavy Shield Core** | Sällsynt | 25 000 | 833/s | 50 % | +20 % | −5 % | 3 | Shield Surge III | Kan bara tillverkas |

**Heavy Shield Core** tillverkas i [Monteringen](/wiki/05-Items/Overview.md#upgrading-modules) av en Basic Shield Core, med 2 000 Thulium, 20 Cataclysite, 8 Reinforced Hull Plates och 6 Velkonite Reinforced Plates från din Skylab. Den behåller förtrollningsnivån hos den kärna den förbrukar, och dess bonusar slumpas på nytt ([Modulupgraderingar](/wiki/05-Items/Forge.md#module-upgrades-in-the-assembly)). Ta först av Basic Shield Core från ditt skepp (och ta ut dess celler ur den): en kärna som sitter på ett skepp eller bär celler förbrukas inte.

**Absorption** är den andel av varje träff som dina sköldar tar; skrovet tar resten. En sköld ensam ger **45 till 50 %**, och dess celler lägger till resten: den bästa skölden med de bästa cellerna (en Heavy Shield Core med tre Sovereign-celler) ger **80 %**, det mest ett skepp har från start. Två permanenta förstärkningar lägger till det: säsongsbutikens Shield Absorbance Boost (+0,1 punkter per nivå, 100 nivåer, 25 wipepoäng var) och Smedjans absorptionsbonusar. Dagens källor till wipepoäng (855 sammanlagt vid sina tak, som följer med över wipes; fler källor är planerade) räcker till 34 av de 100 nivåerna (+3,4 punkter), vilket med en fullt smidd uppsättning på nivån Evig blir ungefär **95 %**. Värdet är dock inte begränsat till 100 %: en angripares *sköldgenomträngning* dras av från det, så det ett skepp har över 100 % är dess marginal mot genomträngning. Se [Sköldmekanik](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-).

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

Sköldceller monteras inuti sköldkärnor eller adaptiva kärnor (lika många som kärnans platser) för att förstärka den kärnan. I en sköldkärna höjer de också dess absorption, i punkter, och därmed den andel av varje träff som dina sköldar tar. En kärna med alla platser fyllda med samma cell: en Light Shield Core (1 plats) ger 47 till 55 %, en Basic Shield Core (2 platser) 52 till 68 % och en Heavy Shield Core (3 platser) 56 till 80 %, från Basic Shield Cell till Sovereign Shield Cell. Att ta av kärnan, eller förbruka den som givare i en sammanslagning i [Smedjan](/wiki/05-Items/Forge.md), för tillbaka dess celler till inventariet.

| Namn | Sällsynthet | Kapacitetsökning | Laddningsökning | Absorptionsökning | Kostnad |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Basic Shield Cell** | Skral | +1 000 | +100/s | +2 % | 10 000 krediter |
| **Advanced Shield Cell** | Vanlig | +2 500 | +250/s | +4 % | 30 000 krediter |
| **Reinforced Shield Cell** | Ovanlig | +4 200 | +350/s | +6 % | 90 000 krediter |
| **Elite Shield Cell** | Sällsynt | +6 000 | +500/s | +7 % | 5 000 Thulium |
| **Prime Shield Cell** | Sällsynt | +8 500 | +700/s | +8 % | 8 000 Thulium |
| **Sovereign Shield Cell** | Episk | +12 000 | +1 000/s | +10 % | Kan bara tillverkas |

Sovereign Shield Cell tillverkas i [Monteringen](/wiki/05-Items/Overview.md#upgrading-modules) av en Prime Shield Cell, med Thulium, byte och 6 Velkonite Reinforced Plates från din Skylab. Den behåller förtrollningsnivån hos den cell den förbrukar, och dess bonusar slumpas på nytt ([Modulupgraderingar](/wiki/05-Items/Forge.md#module-upgrades-in-the-assembly)). Celler passar inte i en [förmågeplats](/wiki/03-Mechanics/Abilities.md); de hör hemma inuti sköldar och adaptiva kärnor.
