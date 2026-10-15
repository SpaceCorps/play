<!-- wiki-i18n source: 0a5a114c67d5c795 -->
<!-- wiki-i18n title: Skylab -->
# Skylab

Skylab är din personliga omloppsanläggning. Den bygger och uppgraderar moduler som producerar krediter och Thulium, bryter malm, smider de plåtar som Monteringen gör om till de bästa lasrarna och, från kärnnivå 10, forskar fram de teknologier som Monteringen behöver. Den arbetar åt dig även medan du är offline.

På kärnnivå 10 växer Skylab ytterligare: en **bro** kopplar ihop kärnan med en andra kärna med sex fler modulplatser, och ytterligare tre moduler kopplas in där: **Ammunitionsskrivaren** och **Raketfabriken**, som gör ammunition och raketer ur ingenting, och **Malmviken**, som flyttar den malm du bär på till Resurslagret (se [Bron och Kärna 2](#the-bridge-and-core-2) och [Malmviken](#ore-bay)).

På kärnnivå 15 växer Skylab en gång till och lär sig flyga: en **andra bro** kopplar ihop kärnan med en tredje kärna, **Kärna 3**, med fyra fler modulplatser, och expeditionens fyra moduler tar dem: **Motormodulen**, **Försvarsmodulen**, **Radarmodulen** och **Trofélagret**. Med motorer, lasrar och ammunition från din Ammunitionsskrivare korsar Skylab en egen **universumkarta**, jagar utomjordingarna i de celler det når medan du är borta och tar hem bytet (se [Den andra bron och Kärna 3](#the-second-bridge-and-core-3) och [Expeditioner](#expeditions)).

> [!NOTE]
> **Vad som ändrades i 0.4.10.** Varje modul i Skylab har nu sin egen tabell med produktion, priser och tider, nivå för nivå. Du behöll dina nivåer: ingenting debiterades och ingenting återbetalades för skillnaden. Det som dina farmer och samlare hade i sina lager när uppdateringen kom betalades ut **en enda gång, till det gamla priset**: krediter och Thulium gick till ditt konto, malmen till ditt Resurslager, och lagren började om från tomt.
>
> Två regler är nya. **Solkraft producerar bara 25 % av sin energi medan den uppgraderas**, så på de flesta stationer stannar alla farmer och samlare tills uppgraderingen är klar (se [Solkraftsmodulen](#solar-module) och [Planera en Solkraft-uppgradering](#timing-a-solar-upgrade)). **Resurslagret har ett eget tak för varje malm**: en dags produktion från samlaren på nivå 1, fyra dagar på nivå 20.

> [!NOTE]
> **Vad som ändrades i 0.4.15.** Kärnans steg från nivå 9 till nivå 10 kostar nu **2 000 Thulium** mer, och när det är klart dyker en **bro** och en andra kärna, **Kärna 2**, upp med sex nya modulplatser. Solkraft flyttar till Kärna 2. Två nya moduler kopplas in där: **Ammunitionsskrivaren** och **Raketfabriken**. Solkraft ger dessutom mer energi från nivå 7, så att en full station fortfarande är täckt. Inget du har byggt går förlorat: en kärna som redan är på nivå 10 eller högre har bron direkt och betalar ingenting.

> [!NOTE]
> **Vad som ändrades i 0.4.21.** Kärnans steg från nivå 14 till nivå 15 kostar nu **4 000 Thulium** extra, och när det är klart dyker en andra **bro** och **Kärna 3** upp med fyra nya modulplatser. Solkraft flyttar till Kärna 3 och ger mer energi från nivå 15, så att en full station fortfarande täcks. Fyra nya moduler tar platserna: **Motormodulen**, **Försvarsmodulen**, **Radarmodulen** och **Trofélagret**, och med dem flyger ditt Skylab över **universumkartan**, jagar på egen hand och tar hem sitt byte (se [Expeditioner](#expeditions)). Varje modul har nu en **vikt**, och stationens och motorernas vikt avgör hur fort den flyger (se [Vikt och fart](#weight-and-speed)). **Malmviken** flyttar tre gånger så mycket malm i timmen och håller tre gånger så stor kvot. Inget du har byggt går förlorat: en kärna som redan är på nivå 15 eller högre har Kärna 3 direkt och betalar ingenting.

![The Skylab of a Core 20 with the second bridge: Core 3 carries the Engine, Defense and Radar Modules and the Trophies Bay](../../img/wiki-img/shots/skylab-core3.jpg)
![The Rocket Factory's sheet: the rocket it makes, the room to carry and its storage](../../img/wiki-img/shots/skylab-factory.jpg)
![The Ore Bay's sheet: the ores it moves and banks for you and how much it holds](../../img/wiki-img/shots/skylab-orebay.jpg)
![The Ammo Printer's Build sheet: its price in Credits, Thulium and Ship Fragments](../../img/wiki-img/shots/skylab-printer-build.jpg)
![The Ammo Printer's sheet: its mode, rate, storage and what the next level gives](../../img/wiki-img/shots/skylab-printer.jpg)
![The Skylab station fully grown, seen from the side as the page opens: three Cores in a row with their bridges, every module with its name tag, the Labels switch at the bottom left](../../img/wiki-img/shots/skylab-station.jpg)
![The Resource Storage card of the Skylab](../../img/wiki-img/shots/skylab-storage.jpg)
![The Skylab table of modules: level, production, storage, power and status of every module, from the Core to the Trophies Bay](../../img/wiki-img/shots/skylab-table.jpg)
![The Skylab hunting in a cell of the Universe map: its hull and kills, the cell, the Defense and Engine Modules and the Trophies Bay filling, and Recall](../../img/wiki-img/shots/skylab-trip.jpg)
![The Trophies Bay's sheet: its level and the capacity the trophies of a trip are kept in](../../img/wiki-img/shots/skylab-trophies.jpg)
![The Universe map: 150 hexagonal cells, the ports, the cells you know and the cells the Radar can still scan, marked with a question mark](../../img/wiki-img/shots/skylab-universe.jpg)

## På en minut {#in-one-minute}

- Bygg **Solkraft** först: utan dess energi går ingenting i Skylab. Kreditfarmen kostar ingenting att bygga, och Thuliumfarmen kostar 5 000 krediter och 500 Thulium.
- Farmer och samlare fyller ett **lager** (för 72 timmar) medan du är borta. **Hämta** flyttar det till ditt konto (krediter, Thulium) eller till ditt Resurslager (malm).
- **Thuliumfarmen** är din viktigaste källa till Thulium: 40 i timmen på nivå 1, 1 280 på nivå 20. Kreditfarmen ger 750 krediter i timmen på nivå 1 och 75 000 på nivå 20.
- **Kärnan** ger takten: ingen modul går över den, och dess egen uppgradering tar ungefär 16 och en halv dag.
- På **kärnnivå 10** bygger en **bro** **Kärna 2** med sex fler modulplatser, och **Ammunitionsskrivaren**, **Raketfabriken** och **Malmviken** kopplas in där. Steget till nivå 10 kostar 2 000 Thulium mer.
- På **kärnnivå 15** bygger en andra bro **Kärna 3**, och **Motormodulen**, **Försvarsmodulen**, **Radarmodulen** och **Trofélagret** tar dess platser: med dem flyger Skylab över universumkartan och jagar på egen hand. Steget till nivå 15 kostar 4 000 Thulium extra. [Se Expeditioner](#expeditions).
- **Solkraft producerar bara 25 % av sin energi medan den uppgraderas**, så dina farmer och samlare stannar tills den är klar. [Planera det](#timing-a-solar-upgrade).

## Översikt {#overview}

Skylab går på sin egen klocka, vid sidan av ditt skepp: modulerna producerar och smider medan du är borta. Du bygger, uppgraderar, håller energin i balans och hämtar. Sidan har fyra vyer av samma station: **Station** (3D-stationen, med en bricka över varje modul; klicka på en för att öppna dess fönster, eller tryck **1** till **9**), **Lista** (ett kort för varje modul), **Tabell** (alla modulers värden i en tabell) och **Forskning** (Forskningscentrumets egen skärm, se [Forskning](/wiki/03-Mechanics/Research.md)). Pekar du på **Bygg** eller **Uppgradera** ser du vad nästa nivå ändrar, vad den kostar och hur lång tid den tar. Knappen **Universum** i sidans huvud öppnar expeditionens karta (se [Expeditioner](#expeditions)).

Sexton moduler utgör stationen:

| Modul | Gör eller utför | Byggs från |
| :--- | :--- | :--- |
| **Kärna** | Anger högsta nivån för varje annan modul | Finns alltid |
| **Solkraft** | Producerar energi | Valfri kärnnivå |
| **Kreditfarm** | Producerar [krediter](/wiki/01-General/Getting-Started.md) | Valfri kärnnivå |
| **Thuliumfarm** | Producerar [Thulium](/wiki/01-General/Getting-Started.md) | Valfri kärnnivå |
| **Velkonite-samlare** | Bryter Velkonite-malm | Kärnnivå 5 |
| **Orvium-samlare** | Bryter Orvium-malm | Kärnnivå 5 |
| **Resurslager** | Förvarar malmen | Kärnnivå 5 |
| **Smedja** | Smider malm till plåtar | Kärnnivå 5 |
| **Forskningscentrum** | Gör om resurser till vetenskap och forskar fram [teknologier](/wiki/03-Mechanics/Research.md) | Kärnnivå 10 |
| **Ammunitionsskrivare** | Skriver ut x2-, x3- eller x4-ammunition ur ingenting | Kärnnivå 10, på Kärna 2 |
| **Raketfabrik** | Bygger butikens raketer ur ingenting | Kärnnivå 10, på Kärna 2 |
| **Malmviken** | Flyttar den Velkonite och Orvium du bär på till Resurslagret | Kärnnivå 10, på Kärna 2 |
| **Motormodul** | Rymmer motorerna som flyger Skylab | Kärnnivå 15, på Kärna 3 |
| **Försvarsmodul** | Rymmer lasrarna och magasinet som strider på en expedition | Kärnnivå 15, på Kärna 3 |
| **Radarmodul** | Skannar dimman på universumkartan | Kärnnivå 15, på Kärna 3 |
| **Trofélager** | Förvarar det expeditionerna för hem | Kärnnivå 15, på Kärna 3 |

De två **broarna**, **Kärna 2** och **Kärna 3** är inte moduler: den första bron och Kärna 2 dyker upp när kärnan når nivå 10, den andra bron och Kärna 3 på nivå 15, och ingen av kärnorna har en egen nivå (se [Bron och Kärna 2](#the-bridge-and-core-2) och [Den andra bron och Kärna 3](#the-second-bridge-and-core-3)).

**Uppdrag för den.** Tio [Station-uppdrag](/wiki/03-Mechanics/Quests.md#station-missions) i Mission Control leder dig genom Skylab: bygg Solkraft, en Kreditfarm och en Thuliumfarm, höj Kärna och Solkraft, hämta dina första 50 000 krediter och öppna försörjningskedjan, och få lite betalt för varje steg. Det första är öppet från nivå 1.

## Stationen på varje nivå {#the-station-at-every-level}

Det här är Skylabs stationsvy på varje nivå från 1 till 20, alla från samma vinkel, med varje modul på samma nivå. Vyn passar in hela stationen i bilden, så skalan är inte densamma i alla: den hoppar när formen växer. Stationen växer i steg: dess form ändras vid **nivå 1, 5, 10, 15 och 20**, och däremellan tänder varje nivå **ytterligare en lampa** på varje moduls krage (antalet tända lampor är nivån, och kärnans ring av tjugo lampor fylls upp på samma sätt).

De här bilderna visar den **första kärnan** och det som hänger på den, med Solkraft bredvid, så som stationen såg ut före broarna. Stationen fortsätter bortom den, och bilderna visar inte den delen: från nivå 10 står en bro, Kärna 2 och Ammunitionsskrivaren, Raketfabriken och Malmviken bortom den, och Solkraft flyttar till den andra änden (se [Bron och Kärna 2](#the-bridge-and-core-2)); från nivå 15 står en andra bro, Kärna 3 och expeditionens fyra moduler bortom det (se [Den andra bron och Kärna 3](#the-second-bridge-and-core-3)). Sidans vy Station visar hela stationen.

**Nivå 1 till 4.** De första fyra modulerna runt kärnan: Solkraft, Kreditfarmen, Thuliumfarmen och dockningsviken som rymmer ditt skepp. Försörjningskedjan kan inte byggas än.

![Nivå 1](../../img/skylab/wiki/level-01.jpg)
![Nivå 2](../../img/skylab/wiki/level-02.jpg)
![Nivå 3](../../img/skylab/wiki/level-03.jpg)
![Nivå 4](../../img/skylab/wiki/level-04.jpg)

**Nivå 5 till 9.** Med kärnnivå 5 kan försörjningskedjan byggas: de två samlarna på sina ställningar ovanför stationen, Resurslagret vid kärnans nordöstra port och Smedjan vid dess nordvästra port (de visas här som byggda).

![Nivå 5](../../img/skylab/wiki/level-05.jpg)
![Nivå 6](../../img/skylab/wiki/level-06.jpg)
![Nivå 7](../../img/skylab/wiki/level-07.jpg)
![Nivå 8](../../img/skylab/wiki/level-08.jpg)
![Nivå 9](../../img/skylab/wiki/level-09.jpg)

**Nivå 10 till 14.** Kärnan bär sin ring, farmerna och samlarna får sin större form och Thuliumfarmen får en egen ring.

![Nivå 10](../../img/skylab/wiki/level-10.jpg)
![Nivå 11](../../img/skylab/wiki/level-11.jpg)
![Nivå 12](../../img/skylab/wiki/level-12.jpg)
![Nivå 13](../../img/skylab/wiki/level-13.jpg)
![Nivå 14](../../img/skylab/wiki/level-14.jpg)

**Nivå 15 till 19.** Farmerna fylls ut med lådor och kristaller, dockningsviken tänder sin inflygning och Solkrafts paneler får en topp. På nivå 15 växer stationen också bortom bilden, med en andra bro och Kärna 3.

![Nivå 15](../../img/skylab/wiki/level-15.jpg)
![Nivå 16](../../img/skylab/wiki/level-16.jpg)
![Nivå 17](../../img/skylab/wiki/level-17.jpg)
![Nivå 18](../../img/skylab/wiki/level-18.jpg)
![Nivå 19](../../img/skylab/wiki/level-19.jpg)

**Nivå 20.** Stegens topp: kronan på kärnan och de fullvuxna tornen på farmerna och försörjningskedjan.

![Nivå 20](../../img/skylab/wiki/level-20.jpg)

**Korten för de nio modulerna.** Vyn Lista för samma station på nivå 20: de fyra modulerna från första versionen, Velkonite-samlaren, Orvium-samlaren, Resurslagret och Smedjan som kom med försörjningskedjan, och Forskningscentrumet. Varje kort visar modulens nivå, dess produktion, dess energi och dess strömbrytare. Varje kort visar nivå 20 utom Forskningscentrumets: det har nivå 1 till 10, så dess kort visar nivå 10, dess högsta. Korten för Ammunitionsskrivaren, Raketfabriken och Malmviken finns i samma vy och beskrivs [längre ned](#the-bridge-and-core-2), liksom de fyra korten för expeditionens moduler, i [Den andra bron och Kärna 3](#the-second-bridge-and-core-3).

![Listvyn på nivå 20: korten för Kärnan, Solkraft, Kreditfarmen, Thuliumfarmen, Velkonite-samlaren, Orvium-samlaren, Resurslagret, Smedjan och Forskningscentrum](../../img/skylab/wiki/modules.jpg)

## De första fyra modulerna {#the-first-four-modules}

### Kärnmodulen {#core-module}

Hjärtat i ditt Skylab. Kärnans nivå avgör högsta nivån för varje annan modul: ingen modul går att uppgradera högre än din kärna. Kärnan går upp till nivå 20, och från **nivå 5** öppnar den försörjningskedjan nedan. Dess uppgraderingar kostar krediter, steget till **nivå 10** kostar **2 000 Thulium** extra och bygger bron och Kärna 2 (se [Bron och Kärna 2](#the-bridge-and-core-2)), och steget till **nivå 15** kostar **4 000 Thulium** extra och bygger en andra bro och Kärna 3 (se [Den andra bron och Kärna 3](#the-second-bridge-and-core-3)). Sammanlagt går det åt 112 326 krediter till nivå 10 och 6 647 504 till nivå 20, plus de 6 000 Thulium, och ungefär 16,5 dygn (se [Uppgraderingstider](#upgrade-times)).

### Solkraftsmodulen {#solar-module}

Energi är Skylabs livsnerv. Solkraftsmodulen producerar den energi som alla andra moduler använder.

- **Betydelse**: om din energiförbrukning är högre än din energiproduktion stängs dina farmer och samlare av.
- **Producerad energi**: en Solkraftsmodul på nivå N producerar tillräckligt för **varje annan modul på nivå N**, och ungefär en tiondel till: 255 på nivå 1, 965 på nivå 7, 18 575 på nivå 20. Solkraft på nivå 7 driver en hel station på nivå 7 (se Energihantering för varje nivå).
- **Pris**: att bygga Solkraft kostar **500 krediter och 50 Thulium**. Dess uppgraderingar kostar lika mycket och tar lika lång tid som Smedjans: från 8 000 krediter och 25 Thulium för nivå 2 (5 minuter) till 9 000 000 krediter och 10 000 Thulium för nivå 20 (24 timmar).
- **Uppgradering**: medan Solkraft uppgraderas producerar den bara **25 %** av energin för sin nuvarande nivå, och den nya nivåns energi från det att uppgraderingen är klar. En station som förbrukar mer än så stannar: varje farm och samlare slutar producera, och Smedjan startar ingen ny sats förrän uppgraderingen är klar. För nästan varje station är det så: den går igenom uppgraderingen bara om alla andra moduler ligger minst fem nivåer under Solkraft (sex nivåer från Solkraft nivå 10). Planera en Solkraft-uppgradering som ett blackout för dina farmer (se Bygga och uppgradera).
- **Plats**: Solkraft står i stationens andra ände: på Kärna 2 från kärnnivå 10 och på Kärna 3 från nivå 15 (se [Bron och Kärna 2](#the-bridge-and-core-2) och [Den andra bron och Kärna 3](#the-second-bridge-and-core-3)).

### Kreditfarm och Thuliumfarm {#credit-farm-and-thulium-farm}

- **Kreditfarm**: producerar krediter över tid: **750 i timmen på nivå 1, 75 000 på nivå 20** (nivå 5: 3 750; nivå 10: 11 250; nivå 15: 25 500). Den kostar ingenting att bygga.
- **Thuliumfarm**: producerar Thulium över tid: **40 i timmen på nivå 1, 1 280 på nivå 20** (nivå 5: 144; nivå 10: 360; nivå 15: 760). Att bygga den kostar 5 000 krediter och 500 Thulium.
- Båda kräver energi, och var och en lagrar 72 timmars produktion tills du hämtar den.

## Försörjningskedjan {#the-supply-chain}

Fyra moduler gör tid borta från tangentbordet till plåtar för dina bästa lasrar. Malm kommer **bara** från samlarna (alla material och valutor finns på sidan [Resurser](/wiki/06-Items/Resources.md)): utomjordingar tappar den inte och butiken säljer den inte. (En [jättegrävmaskin](/wiki/03-Mechanics/Giant-Excavator.md) lämnar också lite Velkonite och Orvium i lådor, men den malmen hamnar i din last, och bara [Malmviken](#ore-bay) flyttar den till Resurslagret, varifrån Smedjan och Forskningscentrumet tar den.)

1. En **samlare** bryter malm, en viss mängd i timmen, in i sitt eget lager (72 timmars produktion).
2. **Hämta** flyttar malmen från samlarens lager in i **Resurslagret**, malmbanken, där varje malm förvaras för sig.
3. **Smedjan** tar den malm den behöver från malmbanken när en sats startar, och gör plåtar, 10 sekunder per plåt, en sats i taget.
4. **Hämta plåtar** flyttar de färdiga plåtarna till ditt inventarie (ditt skepp måste vara landat). [Monteringen](/wiki/06-Items/Lasers.md) gör dem till en Quantum Laser III, en Starfire-III eller en Helios Beam, och, en av varje tillsammans med 5 Dark Matter, till en Dark Matter Plate, som [Smedjan](/wiki/06-Items/Forge.md) och sista nivån i varje uppgraderingskedja kräver.

### Velkonite-samlare och Orvium-samlare {#velkonite-collector-and-orvium-collector}

- **Malm**: Velkonite-samlaren bryter **10 Velkonite i timmen** på nivå 1 och Orvium-samlaren **10 Orvium i timmen**, och varje nivå har sin egen takt: upp till 80 Velkonite och 40 Orvium i timmen på nivå 20 (nivå 5: 18 och 14 i timmen; nivå 10: 32 och 24).
- **Lager**: var och en rymmer 72 timmar av sin malm och slutar bryta när lagret är fullt.
- **Hämta**: flyttar malmen in i Resurslagret, så långt det finns plats. Utan byggt resurslager, eller när den malmens lager är fullt, finns ingenstans att lägga den och knappen säger varför. Resten stannar kvar i samlarens lager.
- **Energi**: 20 (Velkonite) och 30 (Orvium) på nivå 1, och det ökar med 15 % per nivå.

### Resurslager {#resource-storage}

- **Lager**: förvarar Velkonite och Orvium var för sig och rymmer olika mycket av varje: **240 av varje på nivå 1**, upp till 7 680 Velkonite och 3 840 Orvium på nivå 20 (nivå 5: 720 och 560; nivå 10: 1 920 och 1 440).
- **Tak**: en dags produktion från dess samlare på nivå 1, upp till fyra dagar på nivå 20. En samlares lager rymmer tre dagar, så från nivå 13 rymmer Resurslagret minst ett fullt lager.
- **Över taket**: om Resurslagret rymmer mer av en malm än dess tak (utbetalningen vid uppdateringen 0.4.10 kan ha lämnat det så), tas ingenting bort, men Hämta lägger inte till mer av den malmen förrän du har använt en del.
- Malm kommer in genom att hämta från en samlare, eller från ditt inventarie genom [Malmviken](#ore-bay), och ut bara till Smedjan och Forskningscentrumet. Den kommer aldrig tillbaka till ditt inventarie.
- **Den inlagrade malmen finns kvar** genom säsongens wipe.
- **Energi**: 10 på nivå 1, och det ökar med 10 % per nivå. Det går inte att stänga av.

### Smedja {#forgery}

- **Plåtar**: Smedjan gör en **Velkonite Reinforced Plate** av Velkonite och en **Orvium Reinforced Plate** av Orvium: **40 Velkonite** eller **80 Orvium** per plåt på nivå 1, och det blir mindre för varje nivå, ner till 30 och 60 på nivå 20 (aldrig under 75 %).
- **Satser**: en sats av ett slags plåt i taget, **10 plåtar på nivå 1** och 5 till för varje nivå över. Malmen lämnar Resurslagret i samma stund som satsen startar, och varje plåt tar **10 sekunder**. Plåtarna görs en efter en, även medan du är borta.
- **Hämta plåtar**: flyttar de färdiga plåtarna till ditt inventarie medan ditt **skepp är landat**, och resten av satsen fortsätter. En ny sats kan startas när Smedjan är tom.
- En sats som pågår blir klar även om du stänger av Smedjan eller uppgraderar den. En **ny** sats kräver att Smedjan är påslagen, inte uppgraderas, och att Skylabs energi är i balans.
- **Energi**: 30 på nivå 1, och det ökar med 15 % per nivå.
- **Inte säljbart**: plattorna som Smedjan tillverkar kan inte säljas i [Auktionen](/wiki/03-Mechanics/Auction.md#marketable-items), annars skulle de bli den största varan på dess Marknad. De duger fortfarande som material för Monteringen och Smedjan.

### Att bygga dem {#building-them}

De två samlarna kostar **10 Ship Fragments, 20 000 krediter och 500 Thulium** var, Resurslagret **10 Ship Fragments, 5 000 krediter och 250 Thulium** och Smedjan **10 Ship Fragments, 5 000 krediter och 500 Thulium**; alla fyra kräver kärnnivå 5.

- Ship Fragments tas från ditt inventarie (inte från transportförrådet) och ditt skepp måste vara landat. Byggdialogen visar vad du har mot vad som krävs, och vad du saknar.
- De förbrukar energi. Innan du bygger visar dialogen din energibalans nu och efteråt: **att bygga kan sätta en station i underskott** när dess Solkraft ligger efter de andra modulerna, och ett underskott stoppar varje farm och samlare. Stäng av en modul, eller uppgradera Solkraft först.
- De två samlarna hänger på ställningar ovanför stationen, Resurslagret sitter vid kärnans nordöstra port och Smedjan vid dess nordvästra port.

## Forskningscentrumet {#the-research-centre}

Den nionde modulen gör om resurser till vetenskap och forskar fram de teknologier som Monteringen behöver innan den gör något nytt. Den byggs från kärnnivå 10, har nivå 1 till 10, drar energi och går inte att stänga av. Dess siffror, vad den bränner som bränsle, boosten och hela teknologiträdet finns på sidan [Forskning](/wiki/03-Mechanics/Research.md). De högsta teknologierna kräver också Dark Matter, som du lägger i centrumet: [Dark Matter och Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md) berättar hur du får tag på det. Nivåerna för Motormodulen, Försvarsmodulen och Radarmodulen är också teknologier och forskas fram här (se [Forskning](/wiki/03-Mechanics/Research.md#module-technologies)).

## Bron och Kärna 2 {#the-bridge-and-core-2}

Kärnans uppgradering till **nivå 10** bygger en **bro** och en andra kärna. Bron dockar vid kärnans norra port, där Solkraft stod, och kopplar den i andra änden till **Kärna 2**.

- **Kostnad**: steget från nivå 9 till nivå 10 kostar **2 000 Thulium** utöver sina 38 443 krediter och tar lika lång tid som förut, 1 h 20 min. Bron och Kärna 2 kostar inget extra och tar ingen egen tid. En uppgradering som redan pågick behåller priset den startades med, och en kärna på nivå 10 eller högre betalar ingenting.
- **Kärna 2 har ingen nivå**: det finns inget att uppgradera eller betala. Den ger din station **sex fler modulplatser**, och kärnans kort visar hur många som är lediga.
- **Solkraft flyttar**: Solkraft lämnar kärnans norra port, som bron nu upptar, för Kärna 2:s norra port i stationens andra ände. Dess nivå, dess energi och en pågående uppgradering rörs inte.
- **En regel, inget bygge**: var varje modul sitter följer av kärnans nivå ensam. Bron dyker upp i samma stund som kärnans uppgradering till nivå 10 är klar (ett lågmält ljud och ett meddelande säger till), och en Skylab vars kärna redan är på nivå 10 eller högre har den vid nästa titt. Ingen modul går förlorad eller raderas, och bara Solkraft byter plats.
- **Platser**: **Ammunitionsskrivaren** tar Kärna 2:s nordöstra plats, **Raketfabriken** den nordvästra och **Malmviken** den östra ställningen; de andra tre är lediga för kommande moduler. Alla tre kan byggas först när Kärna 2 står: innan dess står det ”Kräver Kärna 2” på byggknappen.
- **Nivåer**: en modul på Kärna 2 följer kärnans nivå som alla andra moduler: ingen går över kärnan, så Kärna 2 ger platser, inte nivåer.

### Ammunitionsskrivare {#ammo-printer}

Ammunitionsskrivaren skriver ut laserammunition ur ingenting, en sort i taget: ingen malm och inga krediter, bara energi. Den har nivå 1 till 20.

- **Produktion**: **x2** (Advanced Plasma) **100 i timmen på nivå 1, 2 000 på nivå 20** (100 mer för varje nivå); **x3** (Ultra Core) hälften av det, 50 till 1 000; **x4** (Experimental Fusion Core) en fjärdedel, 25 till 500.
- **Läge**: du väljer x2, x3 eller x4 på dess kort eller i dess fönster. Ett byte behåller de timmar som redan är lagrade och räknar dem sedan med det nya lägets takt.
- **Lager**: ett dygn, 24 timmars produktion på den nivå och i den sort som används (2 400 x2 på nivå 1, 48 000 på nivå 20). Tid offline räknas, och ett fullt lager stannar helt enkelt.
- **Hämta**: flyttar de hela enheterna till ditt inventarie medan ditt **skepp är landat**. Ammunition har ingen bärgräns, och en bråkdel av en enhet blir kvar och räknas vidare.
- **Energi**: 40 på nivå 1, och det ökar med 20 % per nivå. Vid ett energiunderskott stannar den som farmerna och samlarna, och det den håller finns kvar och kan hämtas.
- **Bygge**: 20 000 krediter, 500 Thulium och 10 Ship Fragments (från ditt inventarie, med skeppet landat), bara på Kärna 2. Dess uppgraderingar kostar från 21 000 krediter och 140 Thulium till 5 600 000 krediter och 11 000 Thulium och tar lika lång tid som Smedjans, från 5 minuter till 24 timmar och 5 d 13 h sammanlagt (se tabellerna nedan).
- **Inte säljbart**: det den skriver ut kan inte säljas i [Auktionen](/wiki/03-Mechanics/Auction.md#marketable-items).

### Raketfabrik {#rocket-factory}

Raketfabriken bygger butikens raketer ur ingenting, en sort i taget. Den har nivå 1 till 20.

- **Vad den gör**: en enda av butikens tolv raketer, den du väljer: Lancet, Rivet, Scatter eller Ember, nivå I, II och III. N.U.K.E. och N.I.K.E. byggs aldrig.
- **Produktion**: raketer av nivå III **0,5 i timmen på nivå 1, 10 på nivå 20** (0,5 mer för varje nivå), nivå II 1,25 gånger det och nivå I dubbelt så mycket. Bara hela raketer räknas: en bråkdel av en blir kvar och räknas vidare.
- **Lager**: ett dygn, 24 timmars produktion på den nivå och med den raket som används (240 raketer av nivå III på nivå 20). Tid offline räknas, ett fullt lager stannar helt enkelt, och ett byte av raket behåller de timmar som redan är lagrade.
- **Hämta**: flyttar raketerna till ditt inventarie medan ditt **skepp är landat**, så många du kan bära: högst 5 000 av nivå I, 2 000 av nivå II och 500 av nivå III, butikens egen gräns. Det som inte ryms blir kvar i fabriken.
- **Energi**: 24 på nivå 1, och det ökar med 15 % per nivå. Vid ett energiunderskott stannar den som skrivaren.
- **Bygge**: 20 000 krediter, 500 Thulium och 15 Ship Fragments (från ditt inventarie, med skeppet landat), bara på Kärna 2. Dess uppgraderingar kostar en fjärdedel av skrivarens, från 5 300 krediter och 35 Thulium till 1 400 000 krediter och 2 800 Thulium, och tar lika lång tid: 5 d 13 h sammanlagt.
- **Inte säljbart**: det den bygger kan inte säljas i [Auktionen](/wiki/03-Mechanics/Auction.md#marketable-items).

### Malmviken {#ore-bay}

Malmviken flyttar den malm du bär på till Resurslagret. En [jättegrävmaskin](/wiki/03-Mechanics/Giant-Excavator.md) lämnar Velkonite och Orvium i lådor som hamnar i din last, där ingen modul använder dem; Malmviken är vägen därifrån till banken, varifrån Smedjan och Forskningscentrumet tar dem. Den har nivå 1 till 20.

- **Vad den flyttar**: **Velkonite och Orvium**, de två malmer som Resurslagret förvarar. Cataclysite och Quorvium är bränsle som Forskningscentrumet och [Smedjan](/wiki/06-Items/Forge.md) tar direkt från ditt inventarie, och Thulium går till ditt konto när du plockar upp det.
- **Åt ett håll**: från ditt inventarie till Resurslagret, aldrig tillbaka. Bara den lösa malmen i ditt inventarie flyttas, aldrig den som ligger i Transportförrådet.
- **Hur**: ditt **skepp måste vara landat**. En överföring sker direkt: välj malmen på Malmvikens blad, skriv en mängd eller tryck på Max och tryck sedan på **Flytta**. Bladet visar vad du bär på och vad banken håller mot sin kapacitet.
- **Kvot**: nivån bestämmer hur mycket malm den flyttar i timmen, **30 på nivå 1, 960 på nivå 20**, och den sparar upp till ett dygn av det (720 på nivå 1, 23 040 på nivå 20). En ny Malmvik börjar med ett helt dygn, och en uppgradering behåller det som var sparat. En överföring begränsas av malmen du bär, av platsen som finns kvar i Resurslagret och av kvoten, och bladet säger vilket. Ett dygns kvot är ungefär tre gånger så mycket som Resurslagret rymmer av en malmsort på samma nivå, så det är oftast platsen som stoppar en överföring; kvoten spelar bara roll om du skickar malm genom lagret om och om igen under samma dygn.
- **Energi**: 15 på nivå 1, och det ökar med 10 % per nivå (92 på nivå 20). Den kan slås av. Vid ett energiunderskott, medan den är avslagen och medan den uppgraderas flyttar den ingenting.
- **Bygge**: 5 000 krediter, 250 Thulium och 10 Ship Fragments (från ditt inventarie, med skeppet landat), bara på Kärna 2. Uppgraderingarna kostar det Resurslagrets kostar och tar lika lång tid (se tabellerna nedan).
- **Inget sätt att få mer malm**: den flyttar malm du redan har. En körning av grävmaskinen är begränsad vid källan, och Resurslagrets kapacitet begränsar banken.

## Den andra bron och Kärna 3 {#the-second-bridge-and-core-3}

Kärnans uppgradering till **nivå 15** bygger en **andra bro** och en tredje kärna, och expeditionens fyra moduler tar sina platser där. Bro II dockar vid Kärna 2:s norra port, där Solkraft stod, och kopplar den i stationens andra ände till **Kärna 3**: samma mönster som på nivå 10, en gång till.

- **Kostnad**: steget från nivå 14 till nivå 15 kostar **4 000 Thulium** utöver sina krediter och tar lika lång tid som förut, 14 h. Bro II och Kärna 3 kostar inget extra och tar ingen egen tid. En uppgradering som redan pågick behåller priset den startades med, och en kärna på nivå 15 eller högre betalar ingenting.
- **Kärna 3 har ingen nivå**: det finns inget att uppgradera eller betala. Den ger din station **fyra fler modulplatser**, och kärnans kort visar hur många som är lediga.
- **Solkraft flyttar igen**: Solkraft lämnar Kärna 2:s norra port, som Bro II nu upptar, för Kärna 3:s norra port i stationens andra ände. Dess nivå, dess energi och en pågående uppgradering rörs inte.
- **En regel, inget bygge**: var varje modul sitter följer av kärnans nivå ensam. Kärna 3 dyker upp i samma stund som kärnans uppgradering till nivå 15 är klar, och en Skylab vars kärna redan är på nivå 15 eller högre har den vid nästa titt. Ingen modul går förlorad, och bara Solkraft byter plats.
- **Platser**: **Försvarsmodulen** tar Kärna 3:s nordöstra plats, **Radarmodulen** den nordvästra, **Trofélagret** den östra ställningen och **Motormodulen** den västra. Dess två södra portar vetter mot Kärna 2:s moduler och förblir tomma. Alla fyra kan byggas först när Kärna 3 står: innan dess är byggknappen låst och säger att den kräver kärnnivå 15.
- **Nivåer**: en modul på Kärna 3 följer kärnans nivå som alla andra: ingen går över kärnan. Motormodulen och Försvarsmodulen går upp till nivå 5, Radarmodulen till nivå 3 och Trofélagret till nivå 20.
- **Vad ett bygge kräver**: förutom krediter och Thulium **Ship Fragments** och, för Motor-, Försvars- och Radarmodulen, **Dark Matter Plates** från ditt inventarie (inte från transportförrådet), tagna med skeppet landat, och nivåns **teknologi**, erforskad i Forskningscentrumet. Ett steg som kräver plåtar kräver dem på samma sätt.

**Teknologierna.** Varje nivå av Motor-, Försvars- och Radarmodulen är en teknologi i Skylab-familjen i vyn Forskning, erforskas i tur och ordning och behövs innan nivån kan byggas eller uppgraderas till. De tre modulerna delar tiderna (Radarmodulen går upp till nivå 3):

| Nivå | Forskningstid | Dark Matter |
| :--- | ---: | ---: |
| 1 | 3 h | 0 |
| 2 | 10 h | 5 |
| 3 | 1 d | 10 |
| 4 | 2 d | 15 |
| 5 | 3 d | 20 |

De tre modulernas teknologier kräver 115 Dark Matter och 14 d 15 h forskning i normal takt (se [Forskning](/wiki/03-Mechanics/Research.md#module-technologies)).

### Motormodul {#engine-module}

Motormodulen rymmer motorerna som flyger ditt Skylab. Den har nivå 1 till 5, och varje nivå tar en motor till. Motorerna du monterar och hela stationens vikt avgör hur fort den flyger (se [Vikt och fart](#weight-and-speed)).

- **Vad som passar**: [Engine](/wiki/06-Items/Propulsion.md)-föremål med sina thrusters i, från ditt inventarie: en Engine I, II eller III. En Adaptive Core passar inte: dess fartbonus är ett skepps sak. En motor behåller sina thrusters och sina Smedje-buffar när du tar ut den igen.
- **Hur**: ditt **skepp måste vara landat** och Skylab får inte vara på väg. Motorkortet i fönstret Universum listar dina lösa motorer: dra en till en ledig plats eller klicka på den, och klicka på en monterad motor för att ta ut den. Kortet visar också dragkraften, vikten, farten och hur länge ett hopp tar.
- **En resa kräver**: modulen byggd, påslagen, inte under uppgradering och med minst en motor i.
- **Forskning**: varje nivå kräver sin egen teknologi, Motormodul I till V (se tabellen ovan).
- **Energi**: 60 på nivå 1, och det ökar med 25 % per nivå. Den går att stänga av, men inte medan Skylab är på väg.
- **Bygge**: 375 000 krediter, 1 500 Thulium, 20 Ship Fragments och 1 Dark Matter Plate, bara på Kärna 3.
- **Uppgradering**: modulen är offline medan den uppgraderas. Motormodulens uppgradering väntar till slutet av en resa, eftersom en resas fart är bestämd när den startar.

| Nivå | Motorer | Krediter | Thulium | Plåtar | Tid |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 1 (bygget) | 1 | 375 000 | 1 500 | 1 | – |
| 2 | 2 | 825 000 | 3 300 | 2 | 2 h |
| 3 | 3 | 1 825 000 | 7 300 | 3 | 6 h |
| 4 | 4 | 4 000 000 | 16 000 | 5 | 1 d |
| 5 | 5 | 8 750 000 | 35 000 | 8 | 2 d |

Plåtarna är Dark Matter Plates, och tiden är uppgraderingen till nivån. Alla fem nivåerna kostar sammanlagt 15 775 000 krediter, 63 100 Thulium, 19 plåtar och 3 d 8 h uppgradering.

### Försvarsmodul {#defense-module}

Försvarsmodulen strider för ditt Skylab. Den rymmer lasrarna som skjuter på utomjordingarna i de celler ditt Skylab flyger till och magasinet de skjuter ur. Den har nivå 1 till 5, och dess nivå avgör hur många lasrar den rymmer, hur många skott, vad den får tjäna i timmen och hur farlig en cell den får gå in i.

- **Vad som passar**: [Laser](/wiki/06-Items/Lasers.md)-föremål med sina förstärkare i, från ditt inventarie: en Quantum Laser I, II eller III, en Starfire-III eller en Helios Beam. Alla lasrar skjuter samtidigt, ett skott var per sekund. Förstärkarna räknas som på ett skepp (skada, chans till kritisk träff och kritisk skada); en Penetration Amp tillför ingenting här.
- **Magasinet** rymmer skott av Ammunitionsskrivarens sorter och fylls **bara från Ammunitionsskrivaren**, aldrig från ditt inventarie (se [Montering och ammunition](#fits-and-ammunition)).
- **Porten**: en cell med svårighet 3, till exempel, kan bara beträdas av ett Skylab vars Försvarsmodul är på nivå 3 eller högre. Ett Skylab utan Försvarsmodul får bara flyga genom tomt rymdrum och sin hamn.
- **Nedgörningsbudgeten** är det mesta Skylab får tjäna i timmen: 108 prispengapoäng på nivå 1 och 630 på nivå 5 (se [Vad en resa betalar](#what-a-trip-pays)).
- **Skrovet** växer med nivån (se [Skrovet, förstörelsen och reparationen](#the-hull-and-repair)).
- **Forskning**: varje nivå kräver sin egen teknologi, Försvarsmodul I till V (se tabellen ovan).
- **Energi**: 80 på nivå 1, och det ökar med 25 % per nivå. Den går att stänga av, men inte medan Skylab är på väg. En modul som är avstängd, under uppgradering eller utan ström är mörk: Skylab bekämpar ingenting och passerar cellerna utan strid.
- **Bygge**: 500 000 krediter, 2 000 Thulium, 25 Ship Fragments och 1 Dark Matter Plate, bara på Kärna 3.

| Nivå | Lasrar | Magasin (skott) | Nedgörningsbudget (poäng i timmen) | Högsta svårighet |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 1 | 1 300 | 108 | 1 |
| 2 | 2 | 3 600 | 293 | 2 |
| 3 | 3 | 14 000 | 476 | 3 |
| 4 | 4 | 23 000 | 548 | 4 |
| 5 | 5 | 35 000 | 630 | 5 |

| Nivå | Krediter | Thulium | Plåtar | Tid |
| :--- | ---: | ---: | ---: | ---: |
| 1 (bygget) | 500 000 | 2 000 | 1 | – |
| 2 | 1 150 000 | 4 600 | 2 | 3 h |
| 3 | 2 750 000 | 11 000 | 4 | 9 h |
| 4 | 6 000 000 | 24 000 | 7 | 1 d 12 h |
| 5 | 14 000 000 | 56 000 | 12 | 3 d |

Alla fem nivåerna kostar sammanlagt 24 400 000 krediter, 97 600 Thulium, 26 plåtar och 5 d uppgradering.

### Radarmodul {#radar-module}

Radarmodulen lättar dimman på universumkartan (se [Dimma och skanning](#fog-and-scanning)). Den har nivå 1 till 3, och en högre nivå skannar en cell snabbare.

- **Vad den gör**: den skannar **en cell i taget**, bland cellerna bredvid en cell du känner till, och håller en **kö på tre**: den första skannas och de andra väntar. När en skanning är klar känner du till cellen, och ditt Skylab får flyga dit.
- **Tid**: 90 minuter per cell på nivå 1, 40 på nivå 2 och 15 på nivå 3. En skanning går på serverns klocka, även medan du är borta och medan Skylab flyger. Den står stilla, och tiden tas inte igen, medan modulen är avstängd, under uppgradering eller utan ström och medan Skylab är förstört. En skanning kostar tid och inget annat.
- **Kartlägga allt**: att kartlägga de 131 celler du inte känner till från början, en efter en, tar 8 d 4 h på nivå 1, 3 d 15 h på nivå 2 och 1 d 9 h på nivå 3.
- **Forskning**: varje nivå kräver sin egen teknologi, Radarmodul I till III (se tabellen ovan).
- **Energi**: 40 på nivå 1, och det ökar med 30 % per nivå. Den går att stänga av, men inte medan Skylab är på väg.
- **Bygge**: 250 000 krediter, 1 000 Thulium och 15 Ship Fragments, bara på Kärna 3.

| Nivå | Skanningstid | Krediter | Thulium | Plåtar | Tid |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 1 (bygget) | 90 min | 250 000 | 1 000 | 0 | – |
| 2 | 40 min | 750 000 | 3 000 | 1 | 4 h |
| 3 | 15 min | 2 250 000 | 9 000 | 3 | 1 d |

Alla tre nivåerna kostar sammanlagt 3 250 000 krediter, 13 000 Thulium, 4 plåtar och 1 d 4 h uppgradering.

### Trofélager {#trophies-bay}

Trofélagret förvarar det ditt Skylabs nedgjorda fiender ger tills du hämtar det. Det har nivå 1 till 20 och kräver ingen teknologi.

- **Vad det rymmer**: krediter, Thulium, erfarenhet, heder och bytet från de nedgjorda.
- **Kapaciteten** räknas i **prispengapoäng**: en nedgörning lägger till utomjordingens prispeng, krediter delat med 200 plus Thulium, vad den än tappar (Alphas siffror i varje värld). Det rymmer 650 poäng på nivå 1 och 45 000 på nivå 20.
- **Fullt**: ett fullt lager får Skylab att **sluta skjuta**: inget skjuts ned, betalas eller räknas och ingen ammunition går åt förrän du hämtar (skrovet återhämtar sig ändå). Ett meddelande och tipset på sidofältets Skylab-rad säger det.
- **Hämta** i fönstret Universum, med skeppet landat: krediter och Thulium går till ditt konto, erfarenhet och heder till din pilot och bytet till ditt inventarie. Två hämtningar samtidigt betalar en gång.
- **Bytet** lottas för varje nedgörning ur det utomjordingen tappar, aldrig Dark Matter, Ancient Control Units, N.I.K.E. eller N.U.K.E. Det är **inte säljbart**: det kan inte säljas i [Auktionen](/wiki/03-Mechanics/Auction.md#marketable-items).
- **Energi**: 20 på nivå 1, och det ökar med 10 % per nivå. Det går att stänga av, men inte medan Skylab är på väg.
- **Bygge**: 100 000 krediter, 400 Thulium och 10 Ship Fragments, bara på Kärna 3. Dess uppgraderingar kostar från 117 500 krediter och 470 Thulium (15 minuter) till 2 325 000 krediter och 9 300 Thulium (1 d 13 h): 14 722 500 krediter och 58 890 Thulium sammanlagt, och 6 d 8 h.

| Nivå | Kapacitet (poäng) | Krediter | Thulium | Tid |
| :--- | ---: | ---: | ---: | ---: |
| 1 (bygget) | 650 | 100 000 | 400 | – |
| 2 | 810 | 117 500 | 470 | 15 min |
| 5 | 1 600 | 195 000 | 780 | 34 min |
| 10 | 4 800 | 450 000 | 1 800 | 2 h 18 min |
| 15 | 15 000 | 1 025 000 | 4 100 | 9 h 14 min |
| 20 | 45 000 | 2 325 000 | 9 300 | 1 d 13 h |

Hur lång tid ett lager tar att fylla när Skylab tjänar hela nedgörningsbudgeten för sin försvarsnivå (ett mindre lager fylls snabbare, en mindre budget långsammare):

| Försvarsnivå | Lager nivå 1 | Lager nivå 5 | Lager nivå 10 | Lager nivå 15 | Lager nivå 20 |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 1 | 6 h 1 min | 14 h 49 min | 1 d 20 h | 5 d 19 h | 17 d 9 h |
| 2 | 2 h 13 min | 5 h 28 min | 16 h 23 min | 2 d 3 h | 6 d 10 h |
| 3 | 1 h 22 min | 3 h 22 min | 10 h 5 min | 1 d 8 h | 3 d 22 h |
| 4 | 1 h 11 min | 2 h 55 min | 8 h 46 min | 1 d 3 h | 3 d 10 h |
| 5 | 1 h 2 min | 2 h 32 min | 7 h 37 min | 23 h 49 min | 2 d 23 h |

## Vikt och fart {#weight-and-speed}

Varje modul väger något, i **massenheter (MU)**, och en tyngre station flyger långsammare. En modul väger mer för varje nivå, en som inte är byggd väger ingenting och en som uppgraderas väger den nivå den har. Motorerna och lasrarna du monterar räknas inte: modulens vikt omfattar dem.

| Modul | Nivå 1 | Nivå 5 | Nivå 10 | Nivå 15 | Högsta nivå |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Kärna | 100 | 148 | 208 | 268 | 328 |
| Solkraft | 60 | 84 | 114 | 144 | 174 |
| Kreditfarm | 60 | 84 | 114 | 144 | 174 |
| Thuliumfarm | 80 | 118 | 166 | 214 | 262 |
| Velkonite-samlare | 70 | 92 | 120 | 148 | 176 |
| Orvium-samlare | 70 | 92 | 120 | 148 | 176 |
| Resurslager | 70 | 92 | 120 | 148 | 176 |
| Smedja | 80 | 112 | 152 | 192 | 232 |
| Forskningscentrum | 60 | 89 | 125 | – | 125 |
| Ammunitionsskrivare | 60 | 84 | 114 | 144 | 174 |
| Raketfabrik | 60 | 84 | 114 | 144 | 174 |
| Malmviken | 40 | 53 | 69 | 85 | 101 |
| Motormodul | 80 | 144 | – | – | 144 |
| Försvarsmodul | 100 | 180 | – | – | 180 |
| Radarmodul | 30 | – | – | – | 39 |
| Trofélager | 50 | 60 | 73 | 85 | 98 |
| **Hela stationen: varje modul som står på den kärnnivån, på den nivån** | 300 | 824 | 1 537 | 2 353 | 2 734 |

Högsta nivå är 20, utom för Forskningscentrumet (10), Motor- och Försvarsmodulen (5) och Radarmodulen (3). Hela stationen väger 2 353 MU på kärnnivå 15 och 2 734 MU på nivå 20.

- **Dragkraften** är skeppens motorräkning, utan grundfart: en motor ger sin grundfart plus sina thrusters fasta fart, gånger deras multiplikatorer; motorerna rangordnas bäst först, de fyra första räknas till 100 % och den femte till 85 % (modulen rymmer högst fem); och de fyra bästa fartbonusarna läggs på ovanpå. En station utan motor har ingen dragkraft.
- **Farten** är 60 gånger dragkraften delat med stationens vikt, i enheter per sekund, och ett hopp mellan två grannceller är 15 000 enheter. Under energin visar Skylab-sidan raden ”Vikt 2 353 MU, fart 7,8 enheter/s, ett hopp 32 min”.
- **Bestäms vid start**: en resas fart räknas ut när den startar, ur vikten och dragkraften i det ögonblicket. En uppgradering som slutar på vägen, eller en motor du byter medan Skylab är stationerat, räknas för nästa resa.

Vad motorerna gör för en station med varje modul på nivå 15 (Motormodulen på den nivå som rymmer motorerna):

| Monterade motorer | Vikt (MU) | Dragkraft | Fart (enheter per sekund) | Ett hopp | Över kartan (14 hopp) |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 1 Engine I (Motormodul nivå 1) | 2 289 | 2,0 | 0,05 | 3 d 6 h | 45 d 11 h |
| 3 Engine II, var och en med 2 Impulse Thruster II (nivå 3) | 2 321 | 73,6 | 1,90 | 2 h 11 min | 1 d 7 h |
| 5 Engine III, var och en med 3 Impulse Thruster IV (nivå 5) | 2 353 | 305,5 | 7,79 | 32 min | 7 h 29 min |

På kärnnivå 20 väger stationen 16 % mer, och de bästa motorerna tar 37 minuter per hopp och 8 h 42 min över kartan.

## Expeditioner {#expeditions}

En **expedition** är en resa för ditt Skylab över **universumkartan**. Det flyger till en cell, jagar utomjordingarna där med lasrarna i sin Försvarsmodul och fyller Trofélagret med det nedgörningarna ger. Allt går på serverns klocka, så det fortsätter medan du är utloggad, och ingen spelare kan angripa Skylab: det som skadar det är bara cellens fara (se [Skrovet, förstörelsen och reparationen](#the-hull-and-repair)). Du planerar en resa i fönstret **Universum**, som knappen Universum i Skylab-sidans huvud öppnar.

Vad som krävs: en kärna på nivå 15, en koncern (dess hamn är ditt Skylabs hemmahamn) och en värld; för en resa en Motormodul med en monterad motor; för att tjäna något en Försvarsmodul med en laser och ammunition från din Ammunitionsskrivare, och ett Trofélager att förvara det i. Allt annat fortsätter medan Skylab är borta: farmerna, samlarna, Smedjan, Skrivaren, Fabriken, Malmviken och Forskningscentrumet går på sina egna klockor, och ditt skepp kan flygas som vanligt.

### Universumkartan {#the-universe-map}

Kartan är Skylabs **egna skikt**, inte spelets sektorer och ingen vy av dem: dess celler är inga spelkartor, portarna finns inte på den, ingenting på den flygs i realtid och dess utomjordingar är bara ett antal och en fara. Den berör resten av spelet genom det den betalar: krediter, Thulium, erfarenhet, heder, byte och nedgörningar för uppdrag.

- **Fältet**: 15 kolumner och 10 rader sexkantiga celler, **150 sammanlagt**. En cell har en kod, kolumnens bokstav och radens nummer (A1 till O10), och, när du känner till den, ett namn och en sort.
- **Hamnar**: varje koncern har en **hamn**, en cell med svårighet 0: Mars är H3, Terras D8 och Galactics L8. Ditt Skylab startar i din koncerns hamn och kommer tillbaka dit efter en wipe. Ingenting jagas i en hamn och ingenting angriper Skylab där.
- **Svårigheten** går från 1 till 5 och växer med avståndet till närmaste hamn: de sex cellerna bredvid en hamn har alltid svårighet 1, och varje hopp längre bort lägger till ett, upp till 5. Ungefär en femtedel av cellerna är ett steg lättare än avståndet säger och en fjärdedel ett steg svårare, och några är **tomt rymdrum**, svårighet 0.
- **Sorter**: ett **näste** rymmer alla utomjordingar av sin svårighet och en **drift**, de flesta celler, tre femtedelar av dem. Tomt rymdrum rymmer ingenting och ingen, och ett Skylab får flyga genom det helt utan Försvarsmodul.
- **En karta per värld**: alla piloter i en värld ser samma karta, varje värld har sin egen, och varje säsong (wipen) gör en ny.

Utomjordingarna i ett näste, efter svårighet (en drift rymmer tre femtedelar av dem, avrundat):

| Svårighet | Utomjordingar |
| :--- | :--- |
| 1 | 30 [Seekers](/wiki/04-Aliens/Seeker.md) |
| 2 | 20 Seekers och 10 [Phantasms](/wiki/04-Aliens/Phantasm.md) |
| 3 | 20 Phantasms, 10 [Bulwarks](/wiki/04-Aliens/Bulwark.md) och 5 [Goombahs](/wiki/04-Aliens/Goombah.md) |
| 4 | 20 Bulwarks, 10 Goombahs och 5 [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| 5 | 6 [Slumbering Voids](/wiki/03-Mechanics/Dormant-Swamp.md), 3 [Dormant Pulses](/wiki/05-Swarms/Dormant-Swarm.md) och 1 Dormant Force |

### Dimma och skanning {#fog-and-scanning}

Du ser bara de celler du känner till.

- **I början av en säsong** känner du till din hamn och de två ringarna av celler runt den: **19 celler**, desamma för varje koncern.
- **En cell blir känd** när ditt Skylab flyger genom den eller stannar i den, och när radarn är klar med att skanna den.
- **En cell du inte känner till** visar ingenting om sig själv: varken sort, svårighet, namn eller utomjordingar. En cell bredvid en känd cell är markerad med ett **?** och kan skannas; varje annan okänd cell är mörk.
- **En känd cell** visar i sin panel kod, sort, svårighet, namn och utomjordingar.
- **Flyga** går bara till kända celler.
- **Skanning**: välj en **?**-cell och tryck på **Skanna den här cellen**. Radarn skannar en cell i taget och håller en kö på tre; en cell kan tas ur kön igen, och **Avbryt alla** tömmer den. Tiden för en skanning står under [Radarmodul](#radar-module).

### Resan {#the-trip}

Klicka på en känd cell på kartan: cellens panel visar resans **förhandsvisning**, som servern planerar med ditt Skylab som det är nu, och **Avgå** skickar Skylab dit. Det flyger ett hopp i taget med sina motorers fart, kommer fram till cellen och **jagar där tills du ger en ny order**. **Kalla tillbaka** skickar hem det till hamnen längs den kortaste kända vägen.

- **Rutten** har så få hopp som möjligt över celler du känner till och vars svårighet din Försvarsmoduls nivå tillåter. Bland rutter av samma längd väljs en, alltid samma.
- **Klockan** är serverns: ankomsten är bestämd när Skylab startar, och en resa fortsätter medan du är utloggad. En ny order som ges på vägen gäller från nästa cell: hoppet som pågår flygs färdigt.
- **Vad som stoppar en order**: ingen Motormodul, eller en som är avstängd eller under uppgradering; ingen motor monterad; för lite energi; ett förstört Skylab; cellen det redan är i; en cell du inte känner till; en cell som är för svår för din Försvarsmodul; ingen känd rutt.
- **På väg** går de fyra expeditionsmodulerna inte att slå på eller av, Motormodulen går inte att uppgradera och ingenting går att montera eller ta ut. På vägen möter det utomjordingarna i cellerna det passerar i halva den takt det skulle ha om det stannade där.
- **Meddelanden**: ett meddelande säger till när Skylab kommer fram, när det förstörs eller repareras och när lagret är fullt, och de tre första får dessutom ett eget lågmält ljud.

Vad förhandsvisningen säger, i radernas ordning (varje siffra är serverns, för den utrustning ditt Skylab har nu):

| Rad | Vad den säger |
| :--- | :--- |
| **Sträcka** | hoppen och resans tid |
| **Ankomst** | stunden då det skulle komma fram, efter din klocka |
| **På vägen** | ungefär hur många utomjordingar det möter i cellerna det passerar |
| **Nedgjorda i timmen** | hur många vistelsen skjuter ned i timmen och vilken gräns som styr: utomjordingarna som kommer förbi, nedgörningsbudgeten, dina lasrars skada eller din ammunition |
| **Prispengar i timmen** | vad de nedgörningarna är värda, i prispengapoäng |
| **Din skada** | vad dina lasrar gör per sekund med den bästa ammunitionen i magasinet |
| **Cellen kräver** | den skada vid vilken skrovets regenerering precis bär cellen i den takt den betalar: med mindre sjunker skrovet |
| **Skrov** | Håller, eller Förstört efter en tid |
| **Ammunition** | hur länge magasinet räcker, eller att det räcker för hela vistelsen |
| **Trofélager** | efter hur lång tid det är fullt, eller att det inte fylls i den här takten |

Över raderna säger en **varning** när resan inte skulle ge något: inget att bekämpa i cellen, inga lasrar monterade, ett tomt magasin som inget fyller på, inget Trofélager eller en mörk Försvarsmodul.

### Vad en resa betalar {#what-a-trip-pays}

En nedgörning betalar det dess utomjording betalar i din värld: dess krediter, Thulium, erfarenhet och heder gånger världens betalning (1, 2 och 3 i Alpha, Beta och Gamma), och dess byte. Ingenting läggs till: ingen booster, ingen premium, ingen formationsbonus, ingen klanboost och ingen erfarenhet för dina drönare.

Nedgörningarna i timmen är det minsta av tre tak: utomjordingarna som kommer förbi, din Försvarsmoduls nivås **nedgörningsbudget**, och vad dina lasrar och din ammunition klarar. Budgeten är det som håller ett Skylab utan uppsikt som ett komplement till farmerna och inte ett andra jobb: 108, 293, 476, 548 och 630 prispengapoäng i timmen på försvarsnivå 1 till 5, där en poäng är 1 Thulium eller 200 krediter. **En cell betalar efter sin klass**: ett Skylab får det lägsta av sin försvarsnivås budget och cellens svårighets budget, så ett Skylab med Försvar 5 i en cell med svårighet 1 gör där vad ett med Försvar 1 gör.

Vad en dag i en cell betalar som mest (Alpha; Beta och Gamma betalar 1,6 och 2 gånger så mycket):

| Svårighet | Prispengapoäng i timmen | Nedgjorda per dag | Thulium per dag | Krediter per dag |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 108 | 288 | 1 152 | 288 000 |
| 2 | 293 | 469 | 3 124 | 780 911 |
| 3 | 476 | 224 | 5 524 | 1 181 375 |
| 4 | 548 | 86 | 5 503 | 1 528 510 |
| 5 | 630 | 32 | 5 255 | 1 972 329 |

En dag i en cell är värd ungefär två timmars handjakt på den cellen (3,4 timmar på svårighet 4). Från svårighet 3 är det ungefär 30 % av vad en Thuliumfarm på kärnnivå 15 ger i Thulium (18 240 per dag) och 1,9 till 3,2 gånger vad en Kreditfarm på den nivån ger i krediter (612 000 per dag). En drift med svårighet 2 rymmer färre utomjordingar än budgeten betalar för och ger lite mindre.

**Bytet** från en nedgörning lottas ur det utomjordingen tappar: Ship Fragments, malmer, Reinforced Hull Plates och Power Cores, och från svårighet 5 Ultra Core- och Experimental Fusion Core-ammunition.

### Skrovet, förstörelsen och reparationen {#the-hull-and-repair}

Skylab har ett **skrov**, en pool av träffpoäng, som **återhämtar 5 % av sig själv i timmen**, även under eld. Utomjordingarna det bekämpar skadar det, i proportion till hur många det bekämpar, hur starka de är och hur länge striden varar: förhandsvisningen säger om skrovet håller och, om inte, efter hur lång tid Skylab förstörs. Det är 4 000 000 på kärnnivå 15 med Försvarsmodulen på nivå 1, 12 % mer för varje kärnnivå över 15 och mer med en högre försvarsnivå. Ett Skylab utan Försvarsmodul har skrovet för nivå 1 och bekämpar ingenting.

| Försvarsnivå | Kärnnivå 15 | Kärnnivå 20 |
| :--- | ---: | ---: |
| 1 | 4 000 000 | 7 049 367 |
| 2 | 4 800 000 | 8 459 240 |
| 3 | 6 000 000 | 10 574 050 |
| 4 | 8 800 000 | 15 508 607 |
| 5 | 11 200 000 | 19 738 227 |

- **Förstört**: när skrovet är slut förstörs Skylab där det stod, i det ögonblicket, och resan är över. Det Trofélagret höll finns kvar i det. Alla stationens producenter stannar från det ögonblicket: farmerna, samlarna, Skrivaren, Fabriken och Malmviken tillverkar ingenting, Smedjan startar ingen ny sats och Forskningscentrumet ingen ny forskning (en sats eller forskning som redan pågår fortsätter), och radarns skanningar står stilla.
- **Reparation**: tryck på **Reparera** i fönstret Universum. Den är gratis och tar **60 sekunder**; sedan är skrovet helt och Skylab är tillbaka i den cell där resan började. Produktionen börjar igen från reparationens slut. Inget går förlorat utom tiden.
- **Meddelanden**: Skylab-sidan visar en notis och en bricka på stationens fält medan Skylab är förstört eller repareras, och tipset på sidofältets Skylab-rad säger det också.

### Montering och ammunition {#fits-and-ammunition}

**Montering.** Motorer går i Motormodulen och lasrar i Försvarsmodulen, en per plats, tagna ur de lösa föremålen i ditt inventarie: inte på ett skepp, inte i transportförrådet. Montering och uttagning kräver att ditt **skepp är landat** och att Skylab **inte är på väg**; ett stationerat Skylab kan utrustas om, och de nya takterna gäller från det ögonblicket. Ett monterat föremål behåller sina Smedje-buffar och det som sitter i det (thrusters, förstärkare) och är **reserverat**: det går inte att sätta på ett skepp, radera, lägga ut i Auktionen, lägga i transportförrådet eller använda i Smedjan och Monteringen förrän du tar ut det, och Hangaren, Auktionens säljblad och Monteringen visar det nedtonat.

**Ammunition.** Magasinet rymmer skott av de sorter Ammunitionsskrivaren gör och skjuter **den högsta multiplikatorn först**, ett skott per laser och sekund. Det fylls **bara från Ammunitionsskrivaren**, aldrig från ditt inventarie:

- **Mata från Ammunitionsskrivaren** på: det Skrivaren gör går först in i magasinet, så långt det finns plats; bara resten väntar i Skrivarens tratt på att du hämtar det.
- **Matning** av: det Skrivaren gör väntar i dess tratt, och **Ladda** flyttar det som tratten håller till magasinet, med skeppet landat, så långt det finns plats.
- Det går inte att ladda ur: skott skjuts eller sparas.

Ett Skylab utan lasrar, utan ammunition eller utan Trofélager bekämpar ingenting, och ingenting skadar det heller.

### Nedgörningar och uppdrag {#expedition-kills}

Expeditionens nedgörningar för ett **nedgörningssteg i dina uppdrag** framåt bara när steget **inte anger någon sektor**, upp till **250 nedgörningar om dagen** (UTC) och bara nedgörningar av den utomjording som steget anger. En cell är ingen sektor, så ett steg som anger en (`x-1` till `x-4`, `DS-x` eller en annan koncerns `x-4`) räknar dem aldrig, inte heller i en cell med samma svårighet. I praktiken är det de stora jakterna i Utmaningslinjen vars utomjordingar finns i en cell, och inget av uppdragen för nivå 1 till 8. Ett uppdrag med tidsgräns eller skrovgräns räknar dem inte heller. Bara nedgörningssteg räknas: föremål, besök och vistelser kräver dig. Skylabs kort i fönstret Universum säger ”Expeditionsmål nedgjorda i dag: N av 250”.

Nedgörningarna ger inga wipepoäng och räknas inte för någon klanlinje, någon nedgörningsstatistik eller några rankingpoäng (se [Uppdrag](/wiki/03-Mechanics/Quests.md#where-it-counts)).

### Din klan ser det {#clan-skylabs}

Piloterna i din klan ser var varandras Skylab är: kolumnen **Skylab** i medlemslistan anger cellen (”Dockat vid H3”, ”H3, till K7 om 3 h 12 min”, ”Stationerat vid K7”, ”Förstört vid H3”), och fönstret Universum ritar dem som små guldrutrar, med pilotens namn när du pekar på en. Bara klanen ser det, en kamouflage döljer inte ett Skylab och det finns ingen knapp för att dölja det. En förstörelse visas för klanen först när dess pilot har tittat på Skylab igen eller gett det en order (se [Klaner](/wiki/03-Mechanics/Clans.md#where-your-clan-mates-are)).

## Mekanik {#mechanics}

### Bygga och uppgradera {#building-and-upgrading}

- **Konstruktion**: varje modul byggs för sig. En modul är på nivå 1 i samma stund som den byggs, och att uppgradera den höjer dess produktion (eller dess energiproduktion) och dess lager, och även vad den kostar i energi.
- **Tid och kostnad**: uppgraderingar kostar krediter och Thulium och tar tid, och varje modul har ett eget pris och en egen tid för varje nivå (peka på **Uppgradera** för att se nästa; summorna står nedan). Priset betalas när du startar uppgraderingen. Kostnaden beror inte på tiden. Motor-, Försvars- och Radarmodulen tar också Dark Matter Plates och kräver nivåns teknologi (se [Den andra bron och Kärna 3](#the-second-bridge-and-core-3)).
- **Timers**: en uppgradering går på serverns klocka, så den blir klar medan du är borta, dagar senare om den måste. Starta den, logga ut, kom tillbaka: modulen är på sin nya nivå när du öppnar Skylab-sidan.
- **Uppgraderingstider**: de första nivåerna går snabbt och de sista tar upp till 37 timmar, kärnans upp till 6 dygn (se tabellerna nedan). Varje modul har sin egen timer, så du kan uppgradera flera samtidigt.
- **Produktionspaus**: medan en modul uppgraderas är den offline: den producerar ingenting och använder ingen energi. Solkraft är undantaget: den fortsätter producera en fjärdedel av sin energi (se nedan).
- **Solkraft producerar bara 25 % av sin energi medan den uppgraderas**: Solkraft producerar all energi i Skylab, och medan den uppgraderas (24 timmar för den sista nivån) producerar den en fjärdedel av energin för sin **nuvarande** nivå; den nya nivåns energi tar över i samma ögonblick som uppgraderingen är klar. En full station förbrukar ungefär 90 % av vad Solkraft producerar på sin egen nivå, så en fjärdedel av det bär bara en station som ligger fem till sex nivåer under Solkraft. Annars stannar varje farm och samlare under hela uppgraderingen, det du har lagrat finns kvar och kan hämtas, och Smedjan startar ingen ny sats. En modul som uppgraderas eller är avstängd använder ingen energi, så att höja farmerna tillsammans med Solkraft kostar inget extra, och att stänga av moduler ger plats åt de andra; Thuliumfarmen förbrukar överlägset mest energi.

### Vad det kostar {#what-it-costs}

Priset för hela klättringen, bygget plus varje uppgradering, till nivå 10 och till nivå 20. Kärnan finns alltid och dess steg kostar krediter, med 2 000 Thulium extra på steget till nivå 10 och 4 000 extra på steget till nivå 15; Forskningscentrumet har nivå 1 till 10 och dess siffror finns på sidan [Forskning](/wiki/03-Mechanics/Research.md). Ammunitionsskrivaren, Raketfabriken och Malmviken byggs på Kärna 2, alltså först när kärnan är på nivå 10, och deras nivå 1 är bygget. Expeditionens fyra moduler byggs på Kärna 3, alltså först när kärnan är på nivå 15, och Motor-, Försvars- och Radarmodulen går upp till nivå 5, 5 och 3: deras två siffror är hela klättringen.

| Modul | Krediter till nivå 10 | Thulium till nivå 10 | Krediter till nivå 20 | Thulium till nivå 20 |
| :--- | ---: | ---: | ---: | ---: |
| Kärna | 112 326 | 2 000 | 6 647 504 | 6 000 |
| Solkraft | 1 219 500 | 1 600 | 35 039 500 | 36 850 |
| Kreditfarm | 840 000 | 109 | 26 240 000 | 2 399 |
| Thuliumfarm | 1 154 000 | 4 190 | 32 254 000 | 67 890 |
| Velkonite-samlare | 696 000 | 6 950 | 20 996 000 | 78 950 |
| Orvium-samlare | 696 000 | 6 950 | 20 996 000 | 78 950 |
| Resurslager | 619 500 | 359 | 18 169 500 | 2 649 |
| Smedja | 1 224 000 | 2 050 | 35 044 000 | 37 300 |
| Ammunitionsskrivare | 1 411 000 | 5 140 | 22 031 000 | 47 940 |
| Raketfabrik | 377 300 | 1 674 | 5 547 300 | 12 494 |
| Malmviken | 619 500 | 359 | 18 169 500 | 2 649 |
| Motormodul | 15 775 000 | 63 100 | 15 775 000 | 63 100 |
| Försvarsmodul | 24 400 000 | 97 600 | 24 400 000 | 97 600 |
| Radarmodul | 3 250 000 | 13 000 | 3 250 000 | 13 000 |
| Trofélager | 2 372 500 | 9 490 | 14 722 500 | 58 890 |

De första stegen är billiga och de sista dyra: Kreditfarmens steg från nivå 1 till 2 kostar 5 000 krediter och 1 Thulium, och steget från 19 till 20 kostar 7 000 000 krediter och 550 Thulium. Thuliumfarmens kostar 7 000 krediter och 45 Thulium, sedan 8 500 000 krediter och 16 000 Thulium. Solkrafts uppgraderingar kostar på varje nivå lika mycket som Smedjans, och de två samlarna kostar lika mycket som varandra.

Expeditionens fyra moduler kräver mer än krediter och Thulium: Ship Fragments för att bygga, Dark Matter Plates och en teknologi för varje nivå av de tre första:

| Modul | Ship Fragments för att bygga | Plåtar sammanlagt | Forskning: Dark Matter | Forskning: tid |
| :--- | ---: | ---: | ---: | ---: |
| Motormodul | 20 | 19 | 50 | 6 d 13 h |
| Försvarsmodul | 25 | 26 | 50 | 6 d 13 h |
| Radarmodul | 15 | 4 | 15 | 1 d 13 h |
| Trofélager | 10 | 0 | 0 | – |

Alla fyra tillsammans: 232 590 Thulium, 58 147 500 krediter, 49 plåtar, 115 Dark Matter och 14 d 15 h forskning. Plåtarna är Dark Matter Plates, och vad en plåt kostar står på [Dark Matter och Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md#how-to-get-a-plate).

### Uppgraderingstider {#upgrade-times}

<!-- upgrade-times:start -->
<!-- Generated from server/Resources/SkylabConfig.json by the test skylab::duration_tests::the_wiki_page_is_the_config (run it with SKYLAB_WIKI_WRITE=1 to rewrite this part). -->

**Uppgraderingstider**, per modul (uppgraderingen från nivån i första kolumnen):

| Nivå | Kärna | Solkraft | Kreditfarm | Thuliumfarm | Resurslager | Velkonite-samlare | Orvium-samlare | Smedja | Forskningscentrum |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 till 2 | 72 s | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 78 s |
| 2 till 3 | 86 s | 15 min | 10 min | 15 min | 10 min | 15 min | 15 min | 15 min | 101 s |
| 3 till 4 | 104 s | 30 min | 15 min | 30 min | 15 min | 20 min | 20 min | 30 min | 132 s |
| 4 till 5 | 124 s | 45 min | 20 min | 45 min | 20 min | 30 min | 30 min | 45 min | 171 s |
| 5 till 6 | 149 s | 1 h | 30 min | 1 h | 30 min | 45 min | 45 min | 1 h | 223 s |
| 6 till 7 | 20 min | 1 h 15 min | 45 min | 1 h 30 min | 45 min | 50 min | 50 min | 1 h 15 min | 20 min |
| 7 till 8 | 30 min | 1 h 30 min | 1 h | 2 h | 1 h | 1 h | 1 h | 1 h 30 min | 30 min |
| 8 till 9 | 50 min | 2 h | 1 h 20 min | 3 h | 1 h 20 min | 1 h 15 min | 1 h 15 min | 2 h | 50 min |
| 9 till 10 | 1 h 20 min | 3 h | 1 h 40 min | 4 h | 1 h 40 min | 1 h 30 min | 1 h 30 min | 3 h | 1 h 20 min |
| 10 till 11 | 2 h 15 min | 4 h | 2 h | 5 h | 2 h | 2 h | 2 h | 4 h | – |
| 11 till 12 | 3 h 30 min | 5 h | 2 h 30 min | 6 h | 2 h 30 min | 3 h | 3 h | 5 h | – |
| 12 till 13 | 5 h 30 min | 6 h | 3 h | 8 h | 3 h | 4 h | 4 h | 6 h | – |
| 13 till 14 | 9 h | 8 h | 3 h 30 min | 10 h | 3 h 30 min | 6 h | 6 h | 8 h | – |
| 14 till 15 | 14 h | 10 h | 4 h | 11 h | 4 h | 8 h | 8 h | 10 h | – |
| 15 till 16 | 1 d | 12 h | 5 h | 12 h | 5 h | 10 h | 10 h | 12 h | – |
| 16 till 17 | 1 d 12 h | 16 h | 6 h | 14 h | 6 h | 12 h | 12 h | 16 h | – |
| 17 till 18 | 2 d 12 h | 18 h | 8 h | 18 h | 8 h | 16 h | 18 h | 18 h | – |
| 18 till 19 | 4 d | 20 h | 10 h | 1 d | 10 h | 20 h | 1 d | 20 h | – |
| 19 till 20 | 6 d | 1 d | 12 h | 1 d 12 h | 12 h | 1 d | 1 d 12 h | 1 d | – |
| **Totalt** | 16 d 13 h | 5 d 13 h | 2 d 14 h | 6 d 13 h | 2 d 14 h | 4 d 16 h | 5 d 10 h | 5 d 13 h | 3 h 12 min |
<!-- upgrade-times:end -->

<!-- upgrade-times-expedition:start -->
<!-- Generated from server/Resources/SkylabConfig.json by the test skylab::duration_tests::the_wiki_page_is_the_config (run it with SKYLAB_WIKI_WRITE=1 to rewrite this part). -->

**Uppgraderingstider** för expeditionens fyra moduler (uppgraderingen från nivån i första kolumnen; ett streck ligger bortom modulens högsta nivå):

| Nivå | Motormodul | Försvarsmodul | Radarmodul | Trofélager |
| :--- | ---: | ---: | ---: | ---: |
| 1 till 2 | 2 h | 3 h | 4 h | 15 min |
| 2 till 3 | 6 h | 9 h | 1 d | 19 min |
| 3 till 4 | 1 d | 1 d 12 h | – | 26 min |
| 4 till 5 | 2 d | 3 d | – | 34 min |
| 5 till 6 | – | – | – | 45 min |
| 6 till 7 | – | – | – | 1 h |
| 7 till 8 | – | – | – | 1 h 19 min |
| 8 till 9 | – | – | – | 1 h 44 min |
| 9 till 10 | – | – | – | 2 h 18 min |
| 10 till 11 | – | – | – | 3 h 2 min |
| 11 till 12 | – | – | – | 4 h |
| 12 till 13 | – | – | – | 5 h 17 min |
| 13 till 14 | – | – | – | 6 h 59 min |
| 14 till 15 | – | – | – | 9 h 14 min |
| 15 till 16 | – | – | – | 12 h 11 min |
| 16 till 17 | – | – | – | 16 h 5 min |
| 17 till 18 | – | – | – | 21 h 14 min |
| 18 till 19 | – | – | – | 1 d 4 h |
| 19 till 20 | – | – | – | 1 d 13 h |
| **Totalt** | 3 d 8 h | 5 d | 1 d 4 h | 6 d 8 h |
<!-- upgrade-times-expedition:end -->

En uppgradering som redan pågår när tiderna ändras behåller den sluttid den fick. Enbart kärnan tar ungefär **16,5 dygn** av uppgradering i följd för att gå från nivå 1 till nivå 20. Ingen modul går över kärnans nivå, så sista steget för varje annan modul (12 till 37 timmar) kan starta först när kärnan är på nivå 20: med varje timer upptagen och krediterna och Thulium på plats tar hela stationen ungefär **18 dygn**.

### Energihantering {#power-management}

Din Skylab har en begränsad energibudget.

- **Balans**: håll din Solkraftsproduktion över den energi som alla andra moduler använder. Skylab-sidan visar balansen och varnar innan ett bygge skulle trycka den under noll.
- **Solkraft hänger med**: en Solkraft-modul på nivå N ger energi åt **alla andra moduler på nivå N** (kärnan, båda farmerna, Resurslagret, båda samlarna och Smedjan, och från nivå 10 Forskningscentrumet och Malmviken) och ungefär en tiondel till, så en station vars moduler alla står på nivå 7 behöver Solkraft 7 och har den täckt. Solkraft en nivå lägre räcker inte för en full station (sista kolumnen), så Solkraft måste fortsätta följa med de andra uppåt. Kärnan drar lite, så den får gå före: Solkraft 5 och uppåt täcker en full station på sin nivå med kärnan på vilken nivå som helst. Tabellen nedan räknar också Ammunitionsskrivaren från nivå 7, Raketfabriken och Malmviken från nivå 10, och Motor-, Försvars- och Radarmodulen och Trofélagret från nivå 11 (de byggs från kärnnivå 15 och räknas fyra nivåer tidigare, eftersom kärnan kan ligga före Solkraft), var och en högst på sin egen högsta nivå.
- **Aktivt läge**: du kan slå på och av farmerna, samlarna och Smedjan för att hantera energin. Kärnan, Solkraft, Resurslagret och Forskningscentrumet går alltid. Ammunitionsskrivaren, Raketfabriken och Malmviken går också att slå på och av, och det gör expeditionens fyra moduler också (inte medan en resa pågår).
- **Energiunderskott**: om energiförbrukningen är högre än produktionen slutar alla farmer och samlare att producera tills balansen är tillbaka. Det de redan håller finns kvar, och du kan fortfarande hämta det. Smedjan startar ingen ny sats och Forskningscentrumet ingen ny forskning (en forskning som redan pågår fortsätter). Ammunitionsskrivaren, Raketfabriken och Malmviken stannar som farmerna och samlarna. Försvarsmodulen bekämpar ingenting, radarns skanningar står stilla och ingen resa kan starta (en resa som pågår fortsätter).
- **Solkraft-uppgradering**: medan Solkraft uppgraderas producerar den bara en fjärdedel av sin energi, så om dina andra moduler inte ligger långt under hamnar stationen i underskott och farmerna och samlarna stannar tills uppgraderingen är klar (se [Solkraftsmodulen](#solar-module)).

Solkrafts energi på varje nivå, mot vad de andra modulerna drar på samma nivå (varje modul på den nivån, kärnan inräknad, och Forskningscentrumet och Malmviken från nivå 10, och expeditionens fyra moduler från nivå 11):

<!-- skylab-power:start -->
<!-- Generated from server/Resources/SkylabConfig.json by docs/design/skylab-power-model.py --doc (--check fails while this part is behind). -->

| Nivå | Solkraft ger | De andra modulerna förbrukar | Blir över | Med Solkraft en nivå lägre |
| :--- | ---: | ---: | ---: | :--- |
| 1 | 255 | 230 | 25 | – |
| 2 | 310 | 278 | 32 | 255: 23 för lite |
| 3 | 375 | 337 | 38 | 310: 27 för lite |
| 4 | 455 | 410 | 45 | 375: 35 för lite |
| 5 | 555 | 501 | 54 | 455: 46 för lite |
| 6 | 680 | 615 | 65 | 555: 60 för lite |
| 7 | 965 | 875 | 90 | 680: 195 för lite |
| 8 | 1 185 | 1 076 | 109 | 965: 111 för lite |
| 9 | 1 460 | 1 327 | 133 | 1 185: 142 för lite |
| 10 | 2 035 | 1 849 | 186 | 1 460: 389 för lite |
| 11 | 2 995 | 2 721 | 274 | 2 035: 686 för lite |
| 12 | 3 565 | 3 241 | 324 | 2 995: 246 för lite |
| 13 | 4 285 | 3 893 | 392 | 3 565: 328 för lite |
| 14 | 5 185 | 4 713 | 472 | 4 285: 428 för lite |
| 15 | 6 325 | 5 748 | 577 | 5 185: 563 för lite |
| 16 | 7 765 | 7 055 | 710 | 6 325: 730 för lite |
| 17 | 9 585 | 8 711 | 874 | 7 765: 946 för lite |
| 18 | 11 895 | 10 812 | 1 083 | 9 585: 1 227 för lite |
| 19 | 14 835 | 13 483 | 1 352 | 11 895: 1 588 för lite |
| 20 | 18 575 | 16 885 | 1 690 | 14 835: 2 050 för lite |
<!-- skylab-power:end -->

Tabellen räknar varje modul på samma nivå. Thuliumfarmen drar där uppe mer än två tredjedelar av det (11 695 på nivå 20, mot 16 885 för alla femton), så en station med den farmen långt före resten behöver mer Solkraft än kärnan antyder.

### Hämtning {#collecting}

Varje farm och samlare har ett lager för ungefär 72 timmars produktion. Du hämtar för hand.

- **Kapacitet**: när ett lager är fullt slutar modulen producera tills du hämtar.
- **Farmer**: hämtade krediter och Thulium går direkt till ditt konto.
- **Samlare**: malmen går till Resurslagret, så långt det finns plats.
- **Smedja**: plåtarna går till ditt inventarie, när ditt skepp är landat.
- **Ammunitionsskrivaren och Raketfabriken**: ammunitionen och raketerna går till ditt inventarie, när ditt skepp är landat. Var och en lagrar bara 24 timmars produktion (se [Ammunitionsskrivare](#ammo-printer) och [Raketfabrik](#rocket-factory)).
- **Malmviken**: inget att hämta. Den flyttar malmen i ditt inventarie till Resurslagret när du trycker på **Flytta**, med skeppet landat, upp till sin kvot (se [Malmviken](#ore-bay)).
- **Trofélager**: hämtas i fönstret Universum, med skeppet landat: krediter och Thulium går till ditt konto, erfarenhet och heder till din pilot och bytet till ditt inventarie. Det behåller det det håller tills du hämtar, men ett fullt lager får Skylab att sluta skjuta (se [Trofélager](#trophies-bay)).
- **Hämta allt** tar allt på en gång, även från avstängda moduler och moduler under uppgradering, men inte Trofélagret, som du hämtar i fönstret Universum.
- Ett **(!)**-märke pekar ut ett fullt lager du kan tömma, och plåtar som väntar i Smedjan, på Skylab-sidan och på sidofältets Skylab-rad.

### Wipen {#the-wipe}

Skylab påverkas aldrig av wipen: modulerna behåller sina nivåer, Resurslagret behåller sin malm och Forskningscentrumet behåller sina teknologier, sin vetenskapstank, den Dark Matter som sitter i det och en pågående forskning. Plåtarna i ditt inventarie är föremål som alla andra, så de följer [wipereglerna](/wiki/03-Mechanics/Wipe-Timeline.md). Ammunitionsskrivaren och Raketfabriken behåller sina nivåer, det de är inställda på att tillverka och det de håller, och Malmviken behåller sin nivå och sin kvot. Expeditionens fyra moduler behåller också sina nivåer, med sina teknologier, och det gör magasinet och matningens strömbrytare också. Malmen i ditt inventarie nollställs som vilket föremål som helst: flytta den till Resurslagret först.

En **expedition** avräknas fram till wipen: en resa som pågår är över, Trofélagret betalar ut sina krediter, sitt Thulium, sin erfarenhet och sin heder och töms (dess byte raderas som alla lösa föremål), och Skylab börjar den nya säsongen hemma, i din koncerns hamn, med en ny universumkarta, de 19 startcellerna kända och radarns kö tom. Motorerna och lasrarna som är monterade i Motor- och Försvarsmodulen är lösa föremål som de andra: ta ut dem och lägg dem i transportförrådet för att behålla dem.

## Planera din Skylab {#planning-your-skylab}

En Skylab tar veckor att växa, så lite planering lönar sig. Siffrorna är tabellerna ovan.

### Vad du uppgraderar först {#what-to-upgrade-first}

1. **Solkraft, sedan Kreditfarmen.** Solkraft kostar 500 krediter och 50 Thulium och utan den går ingenting; Kreditfarmen kostar ingenting. De tio [Station-uppdragen](/wiki/03-Mechanics/Quests.md#station-missions) leder dig genom de här första stegen och betalar dig 52 000 krediter och 610 Thulium för dem, som grundvärde: din värld, dina boosters och din klans bonusar multiplicerar det.
2. **Sedan Thuliumfarmen: den är din viktigaste källa till Thulium.** På nivå 10 producerar den 360 Thulium i timmen, 8 640 om dagen, ungefär lika mycket som 43 nedskjutna [Crystalys](/wiki/04-Aliens/Crystalys.md) betalar i Alpha (200 vardera). Vägen upp till nivå 10 kostar 1 154 000 krediter och 4 190 Thulium, bygget inräknat. På nivå 15 producerar farmen 18 240 om dagen och på nivå 20 30 720. Dess lager rymmer 72 timmar, så kom tillbaka minst var tredje dag. Vad Thulium köper står på sidan [Resurser](/wiki/06-Items/Resources.md#thulium).
3. **Kreditfarmen är den jämna extrainkomsten.** På nivå 10 producerar den 11 250 krediter i timmen, 270 000 om dagen, för 840 000 krediter och 109 Thulium. De högre nivåerna betalar sig långsamt: steget från nivå 9 till 10 kostar 300 000 krediter för 1 500 mer i timmen, alltså 200 timmar. Uppgradera den när du har krediter över.
4. **Håll kärnan sysselsatt.** Ingenting går över kärnan, och kärnan ensam tar ungefär 16 och en halv dag till nivå 20. Det finns ingen kö, så starta dess nästa steg varje gång du kommer tillbaka.
5. **Bygg försörjningskedjan som en uppsättning.** Samlarna, Resurslagret och Smedjan öppnas på kärnnivå 5. En samlare kan lägga malm i lager bara i ett Resurslager, och Resurslagret rymmer en dags produktion från sin samlare på nivå 1 och fyra dagar på nivå 20, så uppgradera Resurslagret tillsammans med samlarna, annars väntar malmen i deras lager.
6. **Ha 2 000 Thulium redo för kärnnivå 10.** Kärnans steg från nivå 9 till nivå 10 kräver dem, och det bygger bron och Kärna 2, där [Ammunitionsskrivaren](#ammo-printer), [Raketfabriken](#rocket-factory) och [Malmviken](#ore-bay) byggs.
7. **Ha 4 000 Thulium redo för kärnnivå 15.** Kärnans steg från nivå 14 till nivå 15 kräver dem, och det bygger den andra bron och Kärna 3, där expeditionens fyra moduler byggs. Modulerna själva kräver mycket mer, 232 590 Thulium och 49 Dark Matter Plates sammanlagt (se [Vad det kostar](#what-it-costs)): börja med Motormodulen och Försvarsmodulen på nivå 1.
8. **Bygg expeditionen i den här ordningen.** En motor i Motormodulen, en laser i Försvarsmodulen med en Ammunitionsskrivare som matar den, och Trofélagret som förvarar det nedgörningarna ger: en resa ger ingenting förrän alla tre finns. Radarmodulen kan vänta: med Försvar 1 når ditt Skylab åtminstone de sex cellerna bredvid sin hamn, och de 19 celler du känner till från början innehåller celler upp till svårighet 3.

### Planera en Solkraft-uppgradering {#timing-a-solar-upgrade}

Medan Solkraft uppgraderas ger den en fjärdedel av sin energi, och en station drar nästan alltid mer än så. Farmerna och samlarna står då stilla under hela uppgraderingen: det de håller finns kvar, men det de skulle ha gjort går förlorat. Tabellen ger för varje Solkraft-steg dess tid, den största station som ännu klarar det (varje modul på samma nivå, kärnan och försörjningskedjan inräknade; en mindre station klarar lite mer) och vad en Kreditfarm och en Thuliumfarm på den nivån skulle ha gjort under den tiden. Till exempel tar Solkraft från nivå 10 till 11 4 timmar, och farmer på nivå 10 skulle ha gjort 45 000 krediter och 1 440 Thulium under den. Tabellen räknar också Ammunitionsskrivaren från nivå 7, Raketfabriken och Malmviken från nivå 10 och expeditionens fyra moduler från nivå 15.

| Solkraft-uppgradering | Tid | Station som fortsätter gå, upp till nivå | Kreditfarmen producerar under tiden | Thuliumfarmen producerar under tiden |
| :--- | ---: | ---: | ---: | ---: |
| 1 till 2 | 5 min | ingen | 63 | 3 |
| 2 till 3 | 15 min | ingen | 375 | 16 |
| 3 till 4 | 30 min | ingen | 1 125 | 44 |
| 4 till 5 | 45 min | ingen | 2 250 | 84 |
| 5 till 6 | 1 h | ingen | 3 750 | 144 |
| 6 till 7 | 1 h 15 min | ingen | 6 563 | 230 |
| 7 till 8 | 1 h 30 min | 1 | 10 125 | 336 |
| 8 till 9 | 2 h | 2 | 16 500 | 528 |
| 9 till 10 | 3 h | 3 | 29 250 | 912 |
| 10 till 11 | 4 h | 5 | 45 000 | 1 440 |
| 11 till 12 | 5 h | 6 | 67 500 | 2 200 |
| 12 till 13 | 6 h | 7 | 99 000 | 3 120 |
| 13 till 14 | 8 h | 7 | 156 000 | 4 800 |
| 14 till 15 | 10 h | 8 | 225 000 | 6 800 |
| 15 till 16 | 12 h | 9 | 306 000 | 9 120 |
| 16 till 17 | 16 h | 10 | 480 000 | 14 080 |
| 17 till 18 | 18 h | 11 | 648 000 | 18 000 |
| 18 till 19 | 20 h | 12 | 870 000 | 22 400 |
| 19 till 20 | 1 d | 13 | 1 260 000 | 28 800 |

- **Uppgradera farmerna tillsammans med Solkraft.** En modul som uppgraderas producerar ingenting och använder ingen energi ändå, så den tid en farm tillbringar i uppgradering under pausen kostar inget extra.
- **Håll de andra modulerna låga om du inte har råd med en paus.** En station går bara igenom en Solkraft-uppgradering om alla dess andra moduler ligger minst fem nivåer under Solkraft (sex från Solkraft nivå 10), och en full station behöver lite mer, som tabellen visar.
- **Stäng av det du kan klara dig utan.** En avstängd modul använder ingen energi, så att stänga av Thuliumfarmen, den som förbrukar mest (80 på nivå 1, och 30 % mer för varje nivå), ger plats åt de andra.
