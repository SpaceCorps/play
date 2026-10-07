<!-- wiki-i18n source: 011fc9c31c4045f1 -->
<!-- wiki-i18n title: Skylab -->
# Skylab

Skylab är din personliga omloppsanläggning. Den bygger och uppgraderar moduler som producerar krediter och Thulium, bryter malm, smider de plåtar som Monteringen gör om till de bästa lasrarna och, från kärnnivå 10, forskar fram de teknologier som Monteringen behöver. Den arbetar åt dig även medan du är offline.

> [!NOTE]
> **Vad som ändrades i 0.4.10.** Varje modul i Skylab har nu sin egen tabell med produktion, priser och tider, nivå för nivå. Du behöll dina nivåer: ingenting debiterades och ingenting återbetalades för skillnaden. Det som dina farmer och samlare hade i sina lager när uppdateringen kom betalades ut **en enda gång, till det gamla priset**: krediter och Thulium gick till ditt konto, malmen till ditt Resurslager, och lagren började om från tomt.
>
> Två regler är nya. **Solkraft producerar bara 25 % av sin energi medan den uppgraderas**, så på de flesta stationer stannar alla farmer och samlare tills uppgraderingen är klar (se [Solkraftsmodulen](#solar-module) och [Planera en Solkraft-uppgradering](#timing-a-solar-upgrade)). **Resurslagret har ett eget tak för varje malm**: en dags produktion från samlaren på nivå 1, fyra dagar på nivå 20.

![The Skylab station fully grown](../../img/wiki-img/shots/skylab-station.jpg)
![The Resource Storage card of the Skylab](../../img/wiki-img/shots/skylab-storage.jpg)
![The Skylab table of modules: level, production, storage and power of every module, with the 0.4.10 numbers](../../img/wiki-img/shots/skylab-table.jpg)

## På en minut {#in-one-minute}

- Bygg **Solkraft** först: utan dess energi går ingenting i Skylab. Kreditfarmen kostar ingenting att bygga, och Thuliumfarmen kostar 5 000 krediter och 500 Thulium.
- Farmer och samlare fyller ett **lager** (för 72 timmar) medan du är borta. **Hämta** flyttar det till ditt konto (krediter, Thulium) eller till ditt Resurslager (malm).
- **Thuliumfarmen** är din viktigaste källa till Thulium: 50 i timmen på nivå 1, 1 600 på nivå 20. Kreditfarmen ger 500 krediter i timmen på nivå 1 och 50 000 på nivå 20.
- **Kärnan** ger takten: ingen modul går över den, och dess egen uppgradering tar ungefär 16 och en halv dag.
- **Solkraft producerar bara 25 % av sin energi medan den uppgraderas**, så dina farmer och samlare stannar tills den är klar. [Planera det](#timing-a-solar-upgrade).

## Översikt {#overview}

Skylab går på sin egen klocka, skild från ditt skepp: modulerna producerar och smider medan du är borta. Det du gör är att bygga, uppgradera, hålla energin i balans och hämta. Sidan har fyra vyer av samma station: **Station** (3D-stationen, med en etikett över varje modul; klicka på en för att öppna dess dialog, eller tryck på **1** till **9**), **Lista** (ett kort för varje modul), **Tabell** (alla moduls värden i en tabell) och **Forskning** (forskningscentrumets egen skärm, se [Forskning](/wiki/03-Mechanics/Research.md)). Att hålla pekaren över **Bygg** eller **Uppgradera** visar vad nästa nivå ändrar, vad den kostar och hur lång tid den tar.

Nio moduler utgör stationen:

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

**Uppdrag för den.** Tio [Station-uppdrag](/wiki/03-Mechanics/Quests.md#station-missions) i Mission Control leder dig genom Skylab: bygg Solkraft, en Kreditfarm och en Thuliumfarm, höj Kärna och Solkraft, hämta dina första 50 000 krediter och öppna försörjningskedjan, och få lite betalt för varje steg. Det första är öppet från nivå 1.

## Stationen på varje nivå {#the-station-at-every-level}

Det här är Skylabs stationsvy på varje nivå från 1 till 20, alla från samma vinkel, med varje modul på samma nivå. Vyn passar in hela stationen i bilden, så skalan är inte densamma i alla: den hoppar när formen växer. Stationen växer i steg: dess form ändras vid **nivå 1, 5, 10, 15 och 20**, och däremellan tänder varje nivå **ytterligare en lampa** på varje moduls krage (antalet tända lampor är nivån, och kärnans ring av tjugo lampor fylls upp på samma sätt).

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

**Nivå 15 till 19.** Farmerna fylls ut med lådor och kristaller, dockningsviken tänder sin inflygning och Solkraftens paneler får en topp.

![Nivå 15](../../img/skylab/wiki/level-15.jpg)
![Nivå 16](../../img/skylab/wiki/level-16.jpg)
![Nivå 17](../../img/skylab/wiki/level-17.jpg)
![Nivå 18](../../img/skylab/wiki/level-18.jpg)
![Nivå 19](../../img/skylab/wiki/level-19.jpg)

**Nivå 20.** Stegens topp: kronan på kärnan och de fullvuxna tornen på farmerna och försörjningskedjan.

![Nivå 20](../../img/skylab/wiki/level-20.jpg)

**De nio modulernas kort.** Listvyn för samma station på nivå 20: de fyra modulerna från den första versionen, Velkonite-samlaren, Orvium-samlaren, Resurslagret och Smedjan som kom med försörjningskedjan, samt Forskningscentrum. Varje kort visar modulens nivå, dess produktion, dess energi och dess strömbrytare. Alla kort visar nivå 20 utom Forskningscentrumets: det har nivå 1 till 10, så dess kort visar nivå 10, den högsta.

![Listvyn på nivå 20: korten för Kärnan, Solkraft, Kreditfarmen, Thuliumfarmen, Velkonite-samlaren, Orvium-samlaren, Resurslagret, Smedjan och Forskningscentrum](../../img/skylab/wiki/modules.jpg)

## De första fyra modulerna {#the-first-four-modules}

### Kärnmodulen {#core-module}

Hjärtat i din Skylab. Kärnans nivå avgör högsta nivån för varje annan modul: du kan inte uppgradera någon modul högre än din kärna. Kärnan går upp till nivå 20, och från **nivå 5** öppnar den försörjningskedjan nedan. Dess uppgraderingar kostar bara krediter: 112 326 sammanlagt upp till nivå 10 och 6 647 504 upp till nivå 20, och de tar ungefär 16 och en halv dag sammanlagt (se [Uppgraderingstider](#upgrade-times)).

### Solkraftsmodulen {#solar-module}

Energi är Skylabs livsnerv. Solkraftsmodulen producerar den energi som alla andra moduler använder.

- **Betydelse**: om din energiförbrukning är högre än din energiproduktion stängs dina farmer och samlare av.
- **Producerad energi**: en Solkraftsmodul på nivå N producerar tillräckligt för **varje annan modul på nivå N**, och ungefär en tiondel till: 255 på nivå 1, 835 på nivå 7, 16 110 på nivå 20. Solkraft på nivå 7 driver en hel station på nivå 7 (se Energihantering för varje nivå).
- **Pris**: att bygga Solkraft kostar **500 krediter och 50 Thulium**. Dess uppgraderingar kostar lika mycket och tar lika lång tid som Smedjans: från 8 000 krediter och 25 Thulium för nivå 2 (5 minuter) till 9 000 000 krediter och 10 000 Thulium för nivå 20 (24 timmar).
- **Uppgradering**: medan Solkraft uppgraderas producerar den bara **25 %** av energin för sin nuvarande nivå, och den nya nivåns energi från det att uppgraderingen är klar. En station som förbrukar mer än så stannar: varje farm och samlare slutar producera, och Smedjan startar ingen ny sats förrän uppgraderingen är klar. För nästan varje station är det så: den går igenom uppgraderingen bara om alla andra moduler ligger minst fem nivåer under Solkraft (sex nivåer från Solkraft nivå 10). Planera en Solkraft-uppgradering som ett blackout för dina farmer (se Bygga och uppgradera).

### Kreditfarm och Thuliumfarm {#credit-farm-and-thulium-farm}

- **Kreditfarm**: producerar krediter över tid: **500 i timmen på nivå 1, 50 000 på nivå 20** (nivå 5: 2 500; nivå 10: 7 500; nivå 15: 17 000). Den kostar ingenting att bygga.
- **Thuliumfarm**: producerar Thulium över tid: **50 i timmen på nivå 1, 1 600 på nivå 20** (nivå 5: 180; nivå 10: 450; nivå 15: 950). Att bygga den kostar 5 000 krediter och 500 Thulium.
- Båda kräver energi, och var och en lagrar 72 timmars produktion tills du hämtar den.

## Försörjningskedjan {#the-supply-chain}

Fyra moduler gör tid borta från tangentbordet till plåtar för dina bästa lasrar. Malm kommer **bara** från samlarna (alla material och valutor finns på sidan [Resurser](/wiki/06-Items/Resources.md)): utomjordingar tappar den inte och butiken säljer den inte.

1. En **samlare** bryter malm, en viss mängd i timmen, in i sitt eget lager (72 timmars produktion).
2. **Hämta** flyttar malmen från samlarens lager in i **Resurslagret**, malmbanken, där varje malm förvaras för sig.
3. **Smedjan** tar den malm den behöver från malmbanken när en sats startar, och gör plåtar, 10 sekunder per plåt, en sats i taget.
4. **Hämta plåtar** flyttar de färdiga plåtarna till ditt inventarie (ditt skepp måste vara landat). [Monteringen](/wiki/06-Items/Lasers.md) gör dem till en Quantum Laser 3, en Starfire-3 eller en Helios Beam, och, en av varje tillsammans med 5 Dark Matter, till en Dark Matter Plate, som [Smedjan](/wiki/06-Items/Forge.md) och sista nivån i varje uppgraderingskedja kräver.

### Velkonite-samlare och Orvium-samlare {#velkonite-collector-and-orvium-collector}

- **Malm**: Velkonite-samlaren bryter **10 Velkonite i timmen** på nivå 1 och Orvium-samlaren **10 Orvium i timmen**, och varje nivå har sin egen takt: upp till 80 Velkonite och 40 Orvium i timmen på nivå 20 (nivå 5: 18 och 14 i timmen; nivå 10: 32 och 24).
- **Lager**: var och en rymmer 72 timmar av sin malm och slutar bryta när lagret är fullt.
- **Hämta**: flyttar malmen in i Resurslagret, så långt det finns plats. Utan byggt resurslager, eller när den malmens lager är fullt, finns ingenstans att lägga den och knappen säger varför. Resten stannar kvar i samlarens lager.
- **Energi**: 20 (Velkonite) och 30 (Orvium) på nivå 1, och det ökar med 15 % per nivå.

### Resurslager {#resource-storage}

- **Lager**: förvarar Velkonite och Orvium var för sig och rymmer olika mycket av varje: **240 av varje på nivå 1**, upp till 7 680 Velkonite och 3 840 Orvium på nivå 20 (nivå 5: 720 och 560; nivå 10: 1 920 och 1 440).
- **Tak**: en dags produktion från dess samlare på nivå 1, upp till fyra dagar på nivå 20. En samlares lager rymmer tre dagar, så från nivå 13 rymmer Resurslagret minst ett fullt lager.
- **Över taket**: om Resurslagret rymmer mer av en malm än dess tak (utbetalningen vid uppdateringen 0.4.10 kan ha lämnat det så), tas ingenting bort, men Hämta lägger inte till mer av den malmen förrän du har använt en del.
- Malm kommer in bara genom att hämta från en samlare, och ut bara till Smedjan. Den hamnar aldrig i ditt inventarie.
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

Den nionde modulen gör om resurser till vetenskap och forskar fram de teknologier som Monteringen behöver innan den tillverkar något nytt. Den byggs från kärnnivå 10, har nivå 1 till 10, drar energi och kan inte stängas av. Dess siffror, vad den bränner som bränsle, boosten och hela teknologiträdet finns på sidan [Forskning](/wiki/03-Mechanics/Research.md). De högsta teknikerna kräver också Dark Matter, som du lägger till i centret: [Dark Matter och Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md) säger hur du får tag på den.

## Mekanik {#mechanics}

### Bygga och uppgradera {#building-and-upgrading}

- **Konstruktion**: varje modul byggs för sig. En modul är på nivå 1 i samma stund som den byggs, och att uppgradera den höjer dess produktion (eller dess energiproduktion) och dess lager, och även vad den kostar i energi.
- **Tid och kostnad**: uppgraderingar kostar krediter och Thulium och tar tid, och varje modul har sitt eget pris och sin egen tid för varje nivå (håll pekaren över **Uppgradera** för att se nästa; summorna står nedan). Priset betalas när du startar uppgraderingen. Kostnaden beror inte på tiden.
- **Timers**: en uppgradering går på serverns klocka, så den blir klar medan du är borta, dagar senare om den måste. Starta den, logga ut, kom tillbaka: modulen är på sin nya nivå när du öppnar Skylab-sidan.
- **Uppgraderingstider**: de första nivåerna går fort och de sista tar upp till 36 timmar, kärnans upp till 6 dagar (se tabellerna nedan). Varje modul har sin egen timer, så du kan uppgradera flera samtidigt.
- **Produktionspaus**: medan en modul uppgraderas är den offline: den producerar ingenting och använder ingen energi. Solkraft är undantaget: den fortsätter producera en fjärdedel av sin energi (se nedan).
- **Solkraft producerar bara 25 % av sin energi medan den uppgraderas**: Solkraft producerar all energi i Skylab, och medan den uppgraderas (24 timmar för den sista nivån) producerar den en fjärdedel av energin för sin **nuvarande** nivå; den nya nivåns energi tar över i samma ögonblick som uppgraderingen är klar. En full station förbrukar ungefär 90 % av vad Solkraft producerar på sin egen nivå, så en fjärdedel av det bär bara en station som ligger fem till sex nivåer under Solkraft. Annars stannar varje farm och samlare under hela uppgraderingen, det du har lagrat finns kvar och kan hämtas, och Smedjan startar ingen ny sats. En modul som uppgraderas eller är avstängd använder ingen energi, så att höja farmerna tillsammans med Solkraft kostar inget extra, och att stänga av moduler ger plats åt de andra; Thuliumfarmen förbrukar överlägset mest energi.

### Vad det kostar {#what-it-costs}

Priset för hela uppgången, bygget plus varje uppgradering, upp till nivå 10 och upp till nivå 20. Kärnan finns alltid och dess steg kostar bara krediter; Forskningscentrumet har nivå 1 till 10 och dess siffror står på sidan [Forskning](/wiki/03-Mechanics/Research.md).

| Modul | Krediter till nivå 10 | Thulium till nivå 10 | Krediter till nivå 20 | Thulium till nivå 20 |
| :--- | ---: | ---: | ---: | ---: |
| Kärna | 112 326 | 0 | 6 647 504 | 0 |
| Solkraft | 1 219 500 | 1 600 | 35 039 500 | 36 850 |
| Kreditfarm | 840 000 | 109 | 26 240 000 | 2 399 |
| Thuliumfarm | 1 154 000 | 4 190 | 32 254 000 | 67 890 |
| Velkonite-samlare | 696 000 | 6 950 | 20 996 000 | 78 950 |
| Orvium-samlare | 696 000 | 6 950 | 20 996 000 | 78 950 |
| Resurslager | 619 500 | 359 | 18 169 500 | 2 649 |
| Smedja | 1 224 000 | 2 050 | 35 044 000 | 37 300 |

De första stegen är billiga och de sista dyra: Kreditfarmens steg från nivå 1 till 2 kostar 5 000 krediter och 1 Thulium, och steget från 19 till 20 kostar 7 000 000 krediter och 550 Thulium. Thuliumfarmens kostar 7 000 krediter och 45 Thulium, sedan 8 500 000 krediter och 16 000 Thulium. Solkrafts uppgraderingar kostar på varje nivå lika mycket som Smedjans, och de två samlarna kostar lika mycket som varandra.

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

En uppgradering som redan pågår när tiderna ändras behåller den sluttid den fick. Enbart kärnan tar ungefär **16 och en halv dag** av uppgraderande i rad för att gå från nivå 1 till nivå 20. Ingen modul går över kärnans nivå, så det sista steget för varje annan modul (12 till 36 timmar) kan starta först när kärnan är på nivå 20: med varje timer sysselsatt, och med krediterna och Thuliumet på plats, tar hela stationen ungefär **18 dagar**.

### Energihantering {#power-management}

Din Skylab har en begränsad energibudget.

- **Balans**: håll din Solkraftsproduktion över den energi som alla andra moduler använder. Skylab-sidan visar balansen och varnar innan ett bygge skulle trycka den under noll.
- **Solkraft hänger med**: en Solkraftsmodul på nivå N producerar energin för **alla andra moduler på nivå N** (Kärnan, båda farmerna, Resurslagret, båda samlarna och Smedjan, och från nivå 10 Forskningscentrumet) och ungefär en tiondel till, så en station vars moduler alla är på nivå 7 behöver Solkraft 7, och har det täckt. Solkraft en nivå lägre räcker inte för en full station (sista kolumnen), så Solkraft måste ändå följa med de andra uppåt. Kärnan drar lite, så den kan ligga före: Solkraft 5 och uppåt täcker en full station på sin nivå med Kärnan på vilken nivå som helst.
- **Aktivt läge**: du kan slå på eller av farmerna, samlarna och Smedjan för att hantera energin. Kärnan, Solkraft, Resurslagret och Forskningscentrumet är alltid igång.
- **Energiunderskott**: om energiförbrukningen är högre än energiproduktionen slutar alla farmer och samlare att producera tills balansen är tillbaka. Det de redan lagrat finns kvar, och du kan fortfarande hämta det. Smedjan startar ingen ny sats, och Forskningscentrumet startar ingen ny forskning (en forskning som redan pågår fortsätter).
- **Solkraft-uppgradering**: medan Solkraft uppgraderas producerar den bara en fjärdedel av sin energi, så om dina andra moduler inte ligger långt under hamnar stationen i underskott och farmerna och samlarna stannar tills uppgraderingen är klar (se [Solkraftsmodulen](#solar-module)).

Solkrafts energi på varje nivå, mot vad de andra modulerna förbrukar på samma nivå (varje modul på den nivån, Kärnan inräknad, och Forskningscentrumet från nivå 10):

<!-- skylab-power:start -->
<!-- Generated from server/Resources/SkylabConfig.json by docs/design/skylab-power-model.py --doc (--check fails while this part is behind). -->

| Nivå | Solkraft ger | De andra sju modulerna förbrukar | Blir över | Med Solkraft en nivå lägre |
| :--- | ---: | ---: | ---: | :--- |
| 1 | 255 | 230 | 25 | – |
| 2 | 310 | 278 | 32 | 255: 23 för lite |
| 3 | 375 | 337 | 38 | 310: 27 för lite |
| 4 | 455 | 410 | 45 | 375: 35 för lite |
| 5 | 555 | 501 | 54 | 455: 46 för lite |
| 6 | 680 | 615 | 65 | 555: 60 för lite |
| 7 | 835 | 756 | 79 | 680: 76 för lite |
| 8 | 1 030 | 933 | 97 | 835: 98 för lite |
| 9 | 1 275 | 1 155 | 120 | 1 030: 125 för lite |
| 10 | 1 680 | 1 523 | 157 | 1 275: 248 för lite |
| 11 | 2 065 | 1 876 | 189 | 1 680: 196 för lite |
| 12 | 2 555 | 2 322 | 233 | 2 065: 257 för lite |
| 13 | 3 180 | 2 888 | 292 | 2 555: 333 för lite |
| 14 | 3 970 | 3 607 | 363 | 3 180: 427 för lite |
| 15 | 4 975 | 4 522 | 453 | 3 970: 552 för lite |
| 16 | 6 260 | 5 688 | 572 | 4 975: 713 för lite |
| 17 | 7 895 | 7 176 | 719 | 6 260: 916 för lite |
| 18 | 9 990 | 9 080 | 910 | 7 895: 1 185 för lite |
| 19 | 12 670 | 11 517 | 1 153 | 9 990: 1 527 för lite |
| 20 | 16 110 | 14 642 | 1 468 | 12 670: 1 972 för lite |
<!-- skylab-power:end -->

Tabellen räknar varje modul på samma nivå. Thuliumfarmen drar fyra femtedelar av det på toppen (11 695 på nivå 20, mot 14 642 för alla åtta), så en station med den farmen långt före resten behöver mer Solkraft än Kärnans nivå tyder på.

### Hämtning {#collecting}

Varje farm och samlare har ett lager för ungefär 72 timmars produktion. Du hämtar för hand.

- **Kapacitet**: när ett lager är fullt slutar modulen producera tills du hämtar.
- **Farmer**: hämtade krediter och Thulium går direkt till ditt konto.
- **Samlare**: malmen går till Resurslagret, så långt det finns plats.
- **Smedja**: plåtarna går till ditt inventarie, när ditt skepp är landat.
- **Hämta allt** tar allt på en gång, avstängda och uppgraderande moduler inräknade.
- Ett **(!)**-märke pekar ut ett fullt lager du kan tömma, och plåtar som väntar i Smedjan, på Skylab-sidan och på sidofältets Skylab-rad.

### Wipen {#the-wipe}

Skylab nollställs aldrig: modulerna behåller sina nivåer, Resurslagret behåller sin malm och Forskningscentrumet behåller sina teknologier, sin tank med vetenskap, den Dark Matter som finns i det och en pågående forskning. Plåtarna i ditt inventarie är föremål som alla andra, så de följer [wipereglerna](/wiki/03-Mechanics/Wipe-Timeline.md).

## Planera din Skylab {#planning-your-skylab}

En Skylab tar veckor att växa, så lite planering lönar sig. Siffrorna är tabellerna ovan.

### Vad du uppgraderar först {#what-to-upgrade-first}

1. **Solkraft, sedan Kreditfarmen.** Solkraft kostar 500 krediter och 50 Thulium och utan den går ingenting; Kreditfarmen kostar ingenting. De tio [Station-uppdragen](/wiki/03-Mechanics/Quests.md#station-missions) leder dig genom de här första stegen och betalar dig 52 000 krediter och 610 Thulium för dem, som grundvärde: din värld, dina boosters och din klans bonusar multiplicerar det.
2. **Sedan Thuliumfarmen: den är din viktigaste källa till Thulium.** På nivå 10 producerar den 450 Thulium i timmen, 10 800 om dagen, lika mycket som 54 nedskjutna [Crystalys](/wiki/04-Aliens/Crystalys.md) betalar i Alpha (200 vardera). Vägen upp till nivå 10 kostar 1 154 000 krediter och 4 190 Thulium, bygget inräknat. På nivå 15 producerar farmen 22 800 om dagen och på nivå 20 38 400. Dess lager rymmer 72 timmar, så kom tillbaka minst var tredje dag. Vad Thulium köper står på sidan [Resurser](/wiki/06-Items/Resources.md#thulium).
3. **Kreditfarmen är den jämna extrainkomsten.** På nivå 10 producerar den 7 500 krediter i timmen, 180 000 om dagen, för 840 000 krediter och 109 Thulium. De högre nivåerna betalar sig långsamt: steget från nivå 9 till 10 kostar 300 000 krediter för 1 000 mer i timmen, alltså 300 timmar. Uppgradera den när du har krediter över.
4. **Håll kärnan sysselsatt.** Ingenting går över kärnan, och kärnan ensam tar ungefär 16 och en halv dag till nivå 20. Det finns ingen kö, så starta dess nästa steg varje gång du kommer tillbaka.
5. **Bygg försörjningskedjan som en uppsättning.** Samlarna, Resurslagret och Smedjan öppnas på kärnnivå 5. En samlare kan lägga malm i lager bara i ett Resurslager, och Resurslagret rymmer en dags produktion från sin samlare på nivå 1 och fyra dagar på nivå 20, så uppgradera Resurslagret tillsammans med samlarna, annars väntar malmen i deras lager.

### Planera en Solkraft-uppgradering {#timing-a-solar-upgrade}

Medan Solkraft uppgraderas producerar den en fjärdedel av sin energi, och en station förbrukar nästan alltid mer. Farmerna och samlarna stannar då under hela uppgraderingen: det de håller finns kvar, men det de skulle ha producerat går förlorat. Tabellen anger för varje Solkraft-steg dess tid, den största stationen som ändå går igenom (varje modul på samma nivå, Kärnan och försörjningskedjan inräknade; en mindre station klarar sig lite längre) och vad en Kreditfarm och en Thuliumfarm på den nivån skulle ha producerat under tiden. Till exempel tar Solkraft från nivå 10 till 11 fyra timmar, och farmer på nivå 10 skulle ha producerat 30 000 krediter och 1 800 Thulium under den tiden.

| Solkraft-uppgradering | Tid | Station som fortsätter gå, upp till nivå | Kreditfarmen producerar under tiden | Thuliumfarmen producerar under tiden |
| :--- | ---: | ---: | ---: | ---: |
| 1 till 2 | 5 min | ingen | 42 | 4 |
| 2 till 3 | 15 min | ingen | 250 | 20 |
| 3 till 4 | 30 min | ingen | 750 | 55 |
| 4 till 5 | 45 min | ingen | 1 500 | 105 |
| 5 till 6 | 1 h | ingen | 2 500 | 180 |
| 6 till 7 | 1 h 15 min | ingen | 4 375 | 288 |
| 7 till 8 | 1 h 30 min | ingen | 6 750 | 420 |
| 8 till 9 | 2 h | 1 | 11 000 | 660 |
| 9 till 10 | 3 h | 2 | 19 500 | 1 140 |
| 10 till 11 | 4 h | 4 | 30 000 | 1 800 |
| 11 till 12 | 5 h | 5 | 45 000 | 2 750 |
| 12 till 13 | 6 h | 6 | 66 000 | 3 900 |
| 13 till 14 | 8 h | 7 | 104 000 | 6 000 |
| 14 till 15 | 10 h | 8 | 150 000 | 8 500 |
| 15 till 16 | 12 h | 9 | 204 000 | 11 400 |
| 16 till 17 | 16 h | 10 | 320 000 | 17 600 |
| 17 till 18 | 18 h | 11 | 432 000 | 22 500 |
| 18 till 19 | 20 h | 12 | 580 000 | 28 000 |
| 19 till 20 | 1 d | 13 | 840 000 | 36 000 |

- **Uppgradera farmerna tillsammans med Solkraft.** En modul som uppgraderas producerar ingenting och använder ingen energi ändå, så den tid en farm tillbringar i uppgradering under pausen kostar inget extra.
- **Håll de andra modulerna låga om du inte har råd med en paus.** En station går bara igenom en Solkraft-uppgradering om alla dess andra moduler ligger minst fem nivåer under Solkraft (sex från Solkraft nivå 10), och en full station behöver lite mer, som tabellen visar.
- **Stäng av det du kan klara dig utan.** En avstängd modul använder ingen energi, så att stänga av Thuliumfarmen, den som förbrukar mest (80 på nivå 1, och 30 % mer för varje nivå), ger plats åt de andra.
