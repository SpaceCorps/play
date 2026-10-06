<!-- wiki-i18n source: 7ed6ed3056da695a -->
<!-- wiki-i18n title: Drönare -->
# Drönarmekanik {#drone-mechanics}

Drönare är autonoma stödenheter som flyger vid sidan av ditt skepp. De ger extra utrustningsplatser och bidrar direkt till skeppets stridsprestanda. En Slave Drone växer dessutom: den får erfarenhet varje gång du förstör en utomjording och stiger genom **åtta nivåer**, från ett litet pansrat klot till ett kanonskepp med vingar som en månskära. I Monteringen kan en Slave Drone uppgraderas till en **Master Drone**, som börjar om sina nivåer (se Master Drone nedan). Drönare låter dig också bära en **drönarformation**: den fungerar bara om du har minst en drönare i din flotta (se [Drönarformationer](/wiki/03-Mechanics/Formations.md)).

![Emergency Repair: repair drones beam the hull](../../img/wiki-img/shots/emergency-repair.jpg)

## Skaffa drönare {#getting-drones}

Varje drönare du har, en **Slave Drone** eller en Master Drone, öppnar sina drönarplatser (en för en Slave Drone, två för en Master Drone), upp till **8** drönare. Butiken säljer Slave Drone för krediter, och från den fjärde även för Thulium. Varje drönare kostar mer än den förra: priserna finns under [Drönare](/wiki/06-Items/Drones.md).

## Flyguppställning och rörelse {#formation-movement}

Utan någon bärd [drönarformation](/wiki/03-Mechanics/Formations.md) flyger dina drönare i standarduppställningen **”Wingman” (2-2-4)**, uppställningen **Standard**:

- **2 drönare** bredvid skeppet, en på varje flank.
- **2 drönare** bredvid och strax bakom det.
- **4 drönare** som följer efter.

De använder en mjuk följealgoritm som justerar deras position efter ditt skepps hastighet och rotation och drar ihop uppställningen under skarpa manövrar. I den här uppställningen flyger ingen framför dig.

Drönare är små och håller sig nära: en drönare på nivå 8 är omkring 19,5 enheter bred (en Protos är 50) och en drönare på nivå 1 är ett klot på ungefär 8, så hela uppställningen ryms inom ungefär 135 enheter på var sida om ditt skepp och bakom det. Drönaren du köpte först har mest erfarenhet och flyger i den här uppställningen på din vänstra flank, den andra på din högra, och de nyaste följer efter bakom.

Bär du en [drönarformation](/wiki/03-Mechanics/Formations.md) lämnar drönarna den här uppställningen: **var och en av de 16 formationerna har en egen form**, ett tak över vingarna, en romb, ett hjärta, vingar, ett svärd, en borr och fler, och drönarna glider dit på mindre än en sekund. Formen byggs för de drönare du har, upp till 8, och vrider sig med ditt skepp. Andra piloter ser den också. [Så flyger de](/wiki/03-Mechanics/Formations.md#how-they-fly) visar alla sexton. Bär **Standard**, posten i Formationslistan som inte är någon formation, så flyger drönarna ”Wingman”-uppställningen igen.

Du kan stänga av drönarna under Inställningar › Gränssnitt: **Visa mina drönare** för dina egna och **Visa fientliga drönare** för andra pilotars.

## Utrustning och värden {#equipment-stats}

Drönare fungerar som utbyggbara utrustningsställ för ditt skepp.

- En Slave Drone har **1 plats** och en Master Drone **2**, upp till **8 drönare**.
- Du kan utrusta **lasrar** och **sköldar** i de här platserna, i vilken plats som helst på en Master Drone. Inget annat passar: inga motorer, inga adaptiva kärnor.
- **Lasrar räknas fullt ut.** En laser på en drönare skjuter när du skjuter, lägger sin skada till din salva och förbrukar ammunition som vilken annan laser som helst (varje laser gör av med ett skott ammunition per salva). De två lasrarna på en Master Drone är två lasrar.
- **Sköldar räknas fullt ut också.** En sköld på en drönare räknas som en i en kärnplats, i vilken plats som helst: dess kapacitet och återladdning med dess celler, dess absorption i ditt skepps medelvärde, dess sköldbonus och dess fartavdrag. Den rangordnas med skeppets egna sköldar efter vad som räknas efter platsens andel (en drönares plats räknas 100 %; de fyra bästa räknas fullt ut, den femte och senare för mindre, se [Sköldmekanik](/wiki/03-Mechanics/Shields.md)), och Smedjans bonusar, säsongsbutikens buffar och en angripares sköldgenomträngning verkar på den som på vilken sköld som helst. Drönarens nivå höjer bara dess laser, aldrig dess sköld. Medan en drönare uppgraderas är dess platser offline, både skölden och lasern. Före 0.4.7 gav en sköld på en drönare ingenting.
- **Laser eller sköld?** En plats rymmer det ena eller det andra: en laser lägger en laser till din salva, en sköld lägger till sina sköldpoäng. På ett litet skepp med bra sköldar tillför de extra poängen lite, eftersom skrovet tar slut först; på ett stort skrov gör de att du tål mycket mer.
- **Formationer kräver en drönare, inte en plats.** En [drönarformation](/wiki/03-Mechanics/Formations.md) fungerar så länge du äger minst en drönare. Den tar ingen drönarplats, och antalet drönare, deras nivåer och vad de bär ändrar ingenting.

## Nivåer {#levels}

Varje Slave Drone börjar på nivå 1 och får erfarenhet (XP) varje gång du förstör en utomjording. En Master Drone börjar också på nivå 1, utan XP, och stiger på samma sätt. Varje nivå kräver mer än den förra, och utseendet ändras med den, så att du kan se hur långt en drönare har kommit. Tabellen visar för varje nivå hur mycket XP det krävs för att ta sig dit från nivån före och hur många nedskjutningar av en enda sorts utomjording det motsvarar ensamt (i världen Alpha: i Beta behövs ungefär hälften så många, i Gamma ungefär en tredjedel):

<!-- drones:begin -->
<!-- Generated from server/Resources/drone-levels.json by scripts/drones-wiki.sh: don't edit by hand. -->

- **Nivå 1, Frö:** ett litet pansrat klot med en cyanfärgad lins.
- **Nivå 2, Halo:** klotet i en svävande ring.
- **Nivå 3, Skiva:** en platt skiva under en glaskupol.
- **Nivå 4, Tefat:** ett tefat med pansarplattor och luftintag.
- **Nivå 5, Kanonskepp:** en nos och två kanoner ansluter till tefatet.
- **Nivå 6, Vingknoppar:** kanoner och korta vingblad på pyloner.
- **Nivå 7, Halvvingar:** längre vingblad med guldspetsar.
- **Nivå 8, Månskära:** det färdiga kanonskeppet: fulla månskärevingar med cyanfärgade ljusremsor.

| Nivå | XP för att nå nivån | XP för nivån | Laserskada | Seeker-nedskjutningar | Bulwark-nedskjutningar | Goombah-nedskjutningar |
| --: | --: | --: | --: | --: | --: | --: |
| 1 | 0 | – | – | – | – | – |
| 2 | 350 | 350 | – | 350 | 44 | 15 |
| 3 | 900 | 550 | +1 % | 550 | 69 | 23 |
| 4 | 2 000 | 1 100 | +2 % | 1 100 | 138 | 46 |
| 5 | 3 700 | 1 700 | +3 % | 1 700 | 213 | 71 |
| 6 | 6 000 | 2 300 | +4 % | 2 300 | 288 | 96 |
| 7 | 9 500 | 3 500 | +5 % | 3 500 | 438 | 146 |
| 8 | 14 000 | 4 500 | +7 % | 4 500 | 563 | 188 |

| Utomjording | XP för varje drönare |
| :--- | --: |
| Seeker | 1 |
| Phantasm | 2 |
| Bulwark | 8 |
| Goombah | 24 |
| Crystalys | 72 |

<!-- drones:end -->

### Så får drönare XP {#how-drones-earn-xp}

- **Varje drönare du har får samma XP** för varje nedskjutning av en utomjording som du får betalt för: de första 8 drönarna, oavsett om de bär en laser eller inte. En drönare du köper senare börjar på nivå 1 utan XP, så dina första drönare har alltid högst nivå.
- **Tuffare utomjordingar är värda mer.** Den XP en utomjording ger står i den andra tabellen ovan (en Crystalys är värd 72 Seeker). Varje annan utomjording ger 1.
- **Världar betalar mer.** Beta fördubblar XP, Gamma tredubblar den (utomjordingarna där har också mer träffpoäng). Boosters och Premium ändrar den inte.
- **Nedskjutningar räknas när de betalar dig.** En utomjording du gör slut på medan en annan pilot har paxet på den ger ingenting till dina drönare, precis som den inte ger dig något. Nedskjutningar av spelare, uppdrag och koncernpiloters egna nedskjutningar ger ingen drönar-XP.
- **Nivå 8 är den sista nivån.** XP fortsätter att räknas efter den.

### Vad en nivå ger {#what-a-level-gives}

**Lasern som sitter i en drönares plats** gör mer grundskada när drönaren stiger i nivå: ingenting på nivå 1 och 2, sedan +1 % på nivå 3 upp till **+7 % på nivå 8**. Bonusen multiplicerar laserns egen skada (efter dess förtrollning); förstärkarna som sitter i den läggs på ovanpå och multipliceras inte. Hangaren visar varje drönares nivå, dess XP-stapel och de nedskjutningar nästa nivå kräver, och dess skadesiffror inkluderar redan bonusen. När en drönare stiger i nivå säger Spelloggen det (”Drönare 2 nådde nivå 4.”) och drönaren lyser upp med en ljusring.

### Hur lång tid det tar {#how-long-it-takes}

Kurvan är ställd så att en ny drönare når nivå 2 på ungefär en timmes normalt spel (jakt på Bulwark och Goombah), och nivå 8 på ungefär 27 timmars spel. De timmarna gäller en pilot som köper den första drönaren vid ungefär uppdragen på nivå 7; med svagare utrustning tar det längre (upp till ungefär 4 timmar för nivå 2 och 150 timmar för nivå 8). Att jaga en enda sorts utomjording är i bästa fall ungefär 1,5 gånger så snabbt som en vanlig blandning. Drönare följer med genom säsongens wipe med sina nivåer och sin erfarenhet, så de timmarna läggs ner en gång, över så många säsonger som det tar: en pilot som spelar en halvtimme om dagen kommer dit på ett par säsonger.

### Master Drone

En Slave Drone blir en **Master Drone** när du uppgraderar den i Monteringen, sedan Master Drones teknologi är framforskad ([Forskning](/wiki/03-Mechanics/Research.md)). Receptet kostar 40 000 Thulium och 100 Ship Fragment och tar 60 sekunder, och det förbrukar ingen drönare: **du väljer vilken Slave Drone det gäller** (väljaren visar nivå och XP för var och en), och just den drönaren, med sitt nummer, sin drönarplats och allt som sitter i den, förvandlas till en Master Drone när jobbet är klart, med en andra plats som är tom. Ingenting hamnar i ditt inventarie och det finns inget att hämta: Spelloggen talar om när det är klart, även för en uppgradering som blev klar medan du var borta.

**Dess nivå och XP nollställs till 0 när uppgraderingen är klar.** En Master Drone börjar om på nivå 1, utan XP, och stiger på samma sätt som en Slave Drone (tabellen ovan); laserbonusen för den nivå den hade försvinner också. Monteringen säger det innan du startar, och ber dig bekräfta, där drönaren nämns vid namn, när den har någon XP. Standardvalet är drönaren med minst XP.

Medan uppgraderingen pågår är drönaren låst: du kan inte uppgradera den igen eller ta bort den, och dess plats är **offline**, så lasern i den skjuter inte förrän jobbet är klart (den är fortfarande en Slave Drone med en plats tills dess). Den ställs i kö efter dina andra jobb, som all annan tillverkning.

En Master Drone är en av dina 8 drönare: den räknas mot drönargränsen och mot priset på nästa Slave Drone, så en uppgradering ändrar ingetdera, och den följer med genom säsongens wipe med sin nivå och sin XP. Under flygning är den det färdiga kanonskeppet i guld. En Master Drone har **två utrustningsplatser** där en Slave Drone har en: varje plats tar en laser eller en sköld, och nivåbonusen gäller lasern i vilken som helst av dem. I övrigt är den en Slave Drone: samma åtta nivåer och samma laserbonus. Master Drone som du gjorde innan den andra platsen fanns har nu fått den, med det de bar kvar på sin plats. Master Drone som tillverkades innan uppgraderingar på plats fanns är vanliga föremål i ditt inventarie och flyger inte.

## Stridsbeteende {#combat-behavior}

- **Lasrar**: Drönare avfyrar sina utrustade lasrar mot ditt låsta mål.
- **Skada**: Drönare kan ta skada (om logik för separata enheter finns; för närvarande delar de mest skeppets pool men är visuellt separata). _Obs: För närvarande är drönare oförstörbara förlängningar av skeppet._
- **Repair Drones**: föremålen Repair Drone (I till IV) är [extrautrustning](/wiki/06-Items/Extras.md#repair-drones), inte drönare i din flotta. Medan en lagar ditt skrov flyger små reparationsdrönare ut ur skeppet, cirklar runt det och riktar strålar mot det, och piloter i närheten ser dem.
