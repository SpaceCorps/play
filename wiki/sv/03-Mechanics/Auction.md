<!-- wiki-i18n source: bdcaddfb3b50f7f5 -->
<!-- wiki-i18n title: Auktionen -->
# Auktionen {#auction}

Auktionen är piloternas marknad och samtidigt spelets egna lotter varje timme, på en sida i stationsmenyn. Under flygning öppnas den i ett fönster: knappen **Auktion** (en klubba) i verktygsfältet uppe till vänster visar samma sida över spelet, och fönstrets plats och storlek kommer ihåg. Den fungerar som på stationen, förutom att ammunition, raketer och EMP Charge räknas i flykt, så du lägger ut dem från stationen (säljbladet visar dem låsta, med orsaken); köpa och buda kan du göra var som helst. Den har fem delar. **Marknad** är det andra piloter säljer och, efter alla deras annonser, den flygande handlarens lager: alla sorter som Auktionen listar, till många gånger Butikens pris, som rader märkta med hans namn i guld, ett **NPC**-märke och ett oändlighetstecken; det Butiken inte säljer kostar så mycket att det är sista utvägen att köpa det av honom, och de sällsynta resurserna i tillverkning tusen gånger så mycket till ([Davidski](/wiki/03-Mechanics/Davidski.md)). **Köporder** är det piloter har bett om att få köpa, och där lägger du dina egna ([Köporder](#buy-orders)). **Lotter** är spelets egna erbjudanden, tre varje timme. **Mina annonser** är det du själv säljer. **Historik** är dina försäljningar, dina köp och de lotter du har vunnit, och hur din handel har gått.

![The hourly Lots: the ammo, rockets and EMP Charges the Auction puts up every hour, for Credits](../../img/wiki-img/shots/auction-lots.jpg)
![A listing picked in the Auction: the lots to buy, the price and what it leaves of your daily limit; Davidski's stock is in the list as rows marked NPC](../../img/wiki-img/shots/auction-market.jpg)
![My listings: the open ones with their time left, and what was sold or cancelled recently](../../img/wiki-img/shots/auction-mine.jpg)
![The sell sheet: the item, the lot size, the currency, the price with its Minimum, Quick and Fair chips, the time and the fees](../../img/wiki-img/shots/auction-sell.jpg)
![The Auction in flight: its page opens in a window over the game, from the gavel button of the toolbar](../../img/wiki-img/shots/auction-window.jpg)

<!-- market-glance:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- Du behöver **nivå 5** för att använda auktionen: för att lägga ut, köpa och buda.
- En annons prissätts per parti, i hela krediter eller hela Thulium (inte båda), och aldrig under föremålets lägsta pris. Det finns **inget högsta pris**.
- Ett pris i Thulium är minst det lägsta priset i krediter delat med kursen (1 000), avrundat uppåt, och bara för föremål vars lägsta pris kommer upp i 1 Thulium eller mer. Det är allt kursen gör: **1 Thulium = 1 000 krediter är en regel för det lägsta priset, inte en växelkurs.** Inget byts, inget värde visas, och krediter och Thulium läggs aldrig ihop.
- 84 föremål kan läggas ut, och 83 av dem kan även prissättas i Thulium.
- En annons löper 168 / 336 / 504 timmar, som du väljer: valen är desamma på alla nivåer.
- **Depositionen** är 0,25 % av priset för varje 24 timmar annonsen löper, minst 50 krediter eller 1 Thulium. Du betalar den när du lägger ut annonsen; den betalas aldrig tillbaka, inte ens om du avbryter.
- Från nivå 10 är depositionen 0,4 %.
- Dina första 10 annonser varje UTC-dag kostar ingen deposition alls, oavsett tid och pris. En annons du återkallar räknas ändå som utlagd. Skatten vid en försäljning är densamma för varje annons.
- **Skatten** är 5 % av priset. Den dras av från det säljaren får när annonsen säljs.
- Depositionen och skatten förbränns: de går till ingen.
- Från säsongsdag 28 till wipen är det varken deposition eller skatt.
- Från säsongsdag 30 är auktionen stängd tills den nya säsongen börjar: inget kan läggas ut, köpas eller budas på. Du kan fortfarande avbryta dina annonser.
- Varje valuta har sin egen gräns för hur mycket du kan sälja och hur mycket du kan köpa på 24 timmar (nivåtabellen nedan). Vunna lotter räknas inte.
- Mellan två piloter, där en köper av den andra, går högst 8 000 000 krediter eller 40 000 Thulium igenom på 24 timmar.

<!-- market-glance:end -->

## Säljbara föremål {#marketable-items}

Bara föremål du har **förtjänat** kan säljas. Allt du förtjänar får i [Hangaren](/wiki/03-Mechanics/Inventory.md#marketable-items) en liten etikett, **Säljbart**: det du plockar upp i rymden (byte från utomjordingar, svärmar, Wardens och det svarta hålet: [Last](/wiki/03-Mechanics/Cargo.md)), det ett uppdrag betalar ut ([Uppdrag](/wiki/03-Mechanics/Quests.md#rewards)) och allt som Monteringen och Smedjan tillverkar. Det du har **köpt** i Butiken, vunnit i en lott, köpt på Marknaden, köpt av [Davidski](/wiki/03-Mechanics/Davidski.md), fått med en bonuskod, ett inbjudningspaket eller startpaketet, eller fått tillbaka som återbetalning är inte säljbart och kan aldrig säljas igen, så att inget köps bara för att säljas vidare. Plattorna som Smedjan i Skylab tillverkar är inte heller säljbara; de Reinforced Plates som ett uppdrag betalar ut är det. Ammunitionen och raketerna som Ammunitionsskrivaren och Raketfabriken i Skylab tillverkar är inte heller säljbara.

Etiketten är ett antal enheter, inte en strömbrytare: en ammunitionshög kan innehålla både köpta och förtjänade skott, och kortet säger ”Säljbart (3 av 5)”. När du använder en del av en hög (skjuter, tillverkar) går de vanliga enheterna först, så att de säljbara räcker längst. När du slår ihop två delar i [Smedjan](/wiki/06-Items/Forge.md#merge) finns etiketten kvar bara om båda delarna hade den, och förhandsvisningen säger det; ett steg i Smedjan som misslyckas ger tillbaka sitt material som vanliga enheter.

Knappen **Endast säljbart** i Hangaren visar bara det du kan sälja, och **klubban** bredvid papperskorgen på ett märkt föremål öppnar Auktionens säljblad för det. I Monteringen säger ett recept vars resultat är säljbart det, och ett material du saknar har en länk som öppnar Auktionen med dess namn i sökrutan.

När Auktionen kom (0.4.12) märktes den utrustning du redan hade och som Butiken inte säljer, och resurserna, en gång. Dessa märktes inte, eftersom Butiken en gång sålde dem eller eftersom det du har blandar köpta och förtjänade delar: Quantum Laser III, Absorption Shield Cell II och III, Engine II, Adaptive Core II, Impulse Thruster II och III, de två Reinforced Plates och varje pilots äldsta Base CPU I (startpaketets). Nya av dem som du förtjänar eller tillverkar märks.

## Vad som kan säljas {#what-can-be-sold}

<!-- market-kinds:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Typ | Föremål du kan sälja | Antal |
| :--- | :--- | ---: |
| **Lasrar** | Quantum Laser I, Quantum Laser II, Quantum Laser III, Starfire-III, Helios Beam | 5 |
| **Laserförstärkare** | Damage Amp I, Crit Amp I, Penetration Amp I, Damage Amp II, Crit Amp II, Penetration Amp II, Damage Amp III, Crit Amp III, Penetration Amp III, Damage Amp IV, Crit Amp IV, Penetration Amp IV | 12 |
| **Sköldar** | Light Shield Core, Basic Shield Core, Heavy Shield Core | 3 |
| **Motorer** | Engine I, Engine II, Engine III | 3 |
| **Adaptive Cores** | Adaptive Core I, Adaptive Core II, Adaptive Core III | 3 |
| **Sköldceller** | Absorption Shield Cell I, Capacity Shield Cell I, Absorption Shield Cell II, Capacity Shield Cell II, Absorption Shield Cell III, Capacity Shield Cell III, Absorption Shield Cell IV, Capacity Shield Cell IV | 8 |
| **Styrraketer** | Impulse Thruster I, Momentum Thruster I, Impulse Thruster II, Momentum Thruster II, Impulse Thruster III, Momentum Thruster III, Impulse Thruster IV, Momentum Thruster IV | 8 |
| **Laseramunition** | Standard Battery (i partier om 100), Siphon Battery (i partier om 10), Advanced Plasma (i partier om 10), Ultra Core (i partier om 10), Experimental Fusion Core | 5 |
| **Raketer** | Ember I, Lancet I, Rivet I, Scatter I, Ember II, Lancet II, Rivet II, Scatter II, Ember III, Lancet III, Rivet III, Scatter III | 12 |
| **Förbrukningsvaror** | EMP Charge, Energetic Wall II | 2 |
| **Extrautrustning** | Repair Drone I, Repair Drone II, Repair Drone III, Repair Drone IV, Cloaking CPU S, Base CPU I, Cloaking CPU M, Auto-Repair CPU, Cloaking CPU L, Auto-Rocket CPU, Base CPU II | 11 |
| **Skrovpansar** | Hull Plating II, Hull Plating III | 2 |
| **Resurser** | Cataclysite (i partier om 100), Ship Fragment (i partier om 100), Daraxium (i partier om 100), Nyxite (i partier om 100), Quorvium (i partier om 10), Reinforced Hull Plate (i partier om 10), Power Core, Velkonite Reinforced Plate, Dark Matter, Orvium Reinforced Plate | 10 |

<!-- market-kinds:end -->

Skepp, drönare, drönarformationer, boosters, prenumerationer och [P.E.T.s](/wiki/03-Mechanics/Pets.md) kan aldrig säljas, inte heller Ancient Control Unit, malmerna Velkonite och Orvium, Dark Matter Plate, Jump CPU, Extra Slots CPU, P.E.T. Station I till III, de tre Cluster Chunk, Energetic Wall I, N.U.K.E. och N.I.K.E. Dark Matter Plates finns inte alls i Auktionen, varken som vara eller som pris. Ett föremål som är utrustat, infogat i ett annat föremål, monterat i Motormodulen eller Försvarsmodulen i ditt Skylab, innehåller moduler eller ligger i [Transportförrådet](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) kan inte läggas ut, och inte heller en använd Cloaking CPU, EMP Charge eller Base CPU. Ammunition och raketer säljs från stationen: landa skeppet först.

## Sälja {#selling}

Tryck på **Sälj ett föremål** (eller klubban i Hangaren), välj det du har förtjänat (en kategorimeny avgränsar listan, med samma kategorier som Marknaden), välj krediter eller Thulium, sätt priset för ett parti och hur länge annonsen ska löpa: 7, 14 eller 21 dagar (bladet börjar på 7). Bladet visar det lägsta priset, tre knappar som fyller i ett pris (**Minimum**; **Snabbförsäljning**, ett under den billigaste annonsen just nu; och **Rimligt**, priset på den senaste försäljningen) och depositionen, skatten och det du får, innan du lägger ut. Under priset visar **Liknande annonser** i ett diagram vad andra piloter begär för samma föremål med samma förtrollning, i den valuta du har valt: ditt pris är en linje i det, de andras billigaste och median, det lägsta priset, den senaste försäljningen och Butikens pris är markerade, en rad i ord säger var ditt pris skulle hamna, och de tre billigaste annonserna visas under (med färre än tre andra annonser tar en enkel lista diagrammets plats). **Diagramknappen** på en öppen annons i Mina annonser öppnar samma diagram för den annonsen. En enskild del är ett parti om ett; ammunition och en del resurser säljs i partier om 10 eller 100, och du säljer ett helt antal partier. Det du lägger ut lämnar ditt inventarie och hålls av servern tills det säljs, du avbryter eller det löper ut; då kommer det tillbaka, med sin etikett. Du kan avbryta när som helst, även under säsongens sista dagar. En annons är en ögonblicksbild: för att ändra ett pris avbryter du annonsen och lägger ut den igen (depositionen betalas på nytt).

Varje föremål har ett **lägsta pris**, och det finns **inget högsta pris**: be om vad du vill. Tabellen visar det lägsta priset för några föremål.

<!-- market-bands:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Föremål | Säljs i partier om | Lägsta pris, krediter | Lägsta pris, Thulium |
| :--- | ---: | ---: | ---: |
| Quantum Laser II | 1 | 32 000 | 32 |
| Quantum Laser III | 1 | 220 000 | 220 |
| Helios Beam | 1 | 1 800 000 | 1 800 |
| Absorption Shield Cell IV | 1 | 1 700 000 | 1 700 |
| Heavy Shield Core | 1 | 1 300 000 | 1 300 |
| Impulse Thruster IV | 1 | 1 600 000 | 1 600 |
| EMP Charge | 1 | 40 000 | 40 |
| Cloaking CPU S | 1 | 400 000 | 400 |
| Ultra Core | 10 | 800 | 1 |
| Lancet I | 1 | 200 | 1 |
| Ship Fragment | 100 | 600 | 1 |
| Dark Matter | 1 | 33 000 | 33 |

<!-- market-bands:end -->

Ett pris i Thulium följer en enda regel: det lägsta priset i krediter delat med kursen, avrundat uppåt. Kursen är inget värde som spelet sätter på Thulium. Den bestämmer bara hur det lägsta priset i Thulium räknas ut, och därför kan en annons i Thulium vara billig för en pilot som har Thulium. De flesta säljare kommer att begära krediter. Alla föremål utom **Quorvium** kan prissättas i Thulium, även de billiga (ammunition, raketer, de vanliga resurserna): deras lägsta pris är då 1 Thulium, det minsta steget. Bara Quorvium prissätts enbart i krediter, eftersom 1 Thulium vore mer än ett parti av det är värt.

Dina **öppna annonser** (och en annons som en admin har pausat) tar upp platser. När du går upp i nivå får du fler platser, upp till ett tak, och du kan sälja och köpa mer per dygn. Hur länge en annons får löpa är detsamma på alla nivåer.

<!-- market-limits:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Nivå | Öppna annonser | Längsta tid | Per dygn, krediter | Per dygn, Thulium | Deposition per 24 h |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 5 | 20 | 504 h | 4 500 000 | 22 500 | 0,25 % |
| 6 | 40 | 504 h | 6 000 000 | 30 000 | 0,25 % |
| 7 | 70 | 504 h | 7 500 000 | 37 500 | 0,25 % |
| 8 | 100 | 504 h | 8 500 000 | 42 500 | 0,25 % |
| 9 | 100 | 504 h | 10 000 000 | 50 000 | 0,25 % |
| 10 | 100 | 504 h | 15 000 000 | 75 000 | 0,4 % |
| 11 | 100 | 504 h | 15 000 000 | 75 000 | 0,4 % |
| 12 | 100 | 504 h | 15 000 000 | 75 000 | 0,4 % |
| 13 | 100 | 504 h | 20 000 000 | 100 000 | 0,4 % |
| 14 | 100 | 504 h | 20 000 000 | 100 000 | 0,4 % |
| 15 | 100 | 504 h | 20 000 000 | 100 000 | 0,4 % |
| 16 | 100 | 504 h | 20 000 000 | 100 000 | 0,4 % |
| 17 | 100 | 504 h | 20 000 000 | 100 000 | 0,4 % |
| 18 | 100 | 504 h | 20 000 000 | 100 000 | 0,4 % |
| 19 | 100 | 504 h | 20 000 000 | 100 000 | 0,4 % |
| 20 och uppåt | 100 | 504 h | 20 000 000 | 100 000 | 0,4 % |

<!-- market-limits:end -->

## Avgifter {#fees}

En annons kostar en **deposition**, som betalas när du lägger ut den och aldrig betalas tillbaka, och en försäljning kostar en **skatt**, som dras av från det säljaren får. Båda betalas i annonsens valuta och **förbränns**: de går till ingen, så ingen tjänar på att handla med sig själv. Dina **första tio annonser varje UTC-dag** kostar ingen deposition alls, oavsett tid och pris; en annons du återkallar räknas ändå som utlagd, och skatten vid en försäljning är densamma för varje annons. En annons som säsongens slut kortar av betalar depositionen för de dagar den löper, inte för den tid du valde. Under säsongens sista två dagar är det varken deposition eller skatt. En köporder betalar samma deposition när den läggs, och säljaren som fyller den betalar skatten ([Köporder](#buy-orders)).

<!-- market-fees:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Annons | Pris | Deposition | Skatt | Säljaren får |
| :--- | ---: | ---: | ---: | ---: |
| Quantum Laser III: nivå 6, 168 h | 220 000 krediter | 3 850 krediter | 11 000 krediter | 209 000 krediter |
| Quantum Laser III: nivå 10, 336 h | 220 Thulium | 13 Thulium | 11 Thulium | 209 Thulium |
| Helios Beam: nivå 12, 504 h | 2 500 000 krediter | 210 000 krediter | 125 000 krediter | 2 375 000 krediter |
| Helios Beam: nivå 12, 504 h, under säsongens sista dagar | 2 500 000 krediter | 0 krediter | 0 krediter | 2 500 000 krediter |

<!-- market-fees:end -->

## Köpa {#buying}

**Marknaden** visar det andra piloter säljer. Avgränsa listan med **kategoriknapparna** (en för varje sorts föremål, med antalet annonser i den), sök på namn, filtrera på förtrollning och valuta, och sortera efter pris, efter det som slutar först eller efter det som är nyast. Välj en annons för att se vad det är, vem som säljer, hur länge den löper och hur priset står sig mot den senaste försäljningen, det lägsta priset just nu och Butikens pris. En hög köps i hela partier. Ett stort köp ber dig bekräfta en gång till. Säljaren får betalt direkt, minus skatten; du betalar varken deposition eller skatt. Det du köper är **inte säljbart**: sidan säger ”Du får: inte säljbart” bredvid **Köp för …**, eftersom bara det du förtjänar kan säljas. Du kan inte köpa din egen annons. En annons som säljs medan du tittar på den säger ”Den annonsen finns inte längre.”

**Davidskis rader** står efter piloternas annonser. Varje sort han säljer har en rad i krediter och en i Thulium, med hans namn i guld, ett **NPC**-märke och ett oändlighetstecken för mängden och tiden som är kvar: hans lager tar aldrig slut, och han stänger aldrig. Sökningen, kategoriknapparna och filtren för förtrollning och valuta avgränsar hans rader som vilken annons som helst (hans föremål är Standard, så ingen annan förtrollning visar dem); i vilken ordning du än väljer, **Lägst pris**, **Slutar snart** eller **Nyast**, kommer de efter piloternas sista annons, hur billiga de än är, och inom var och en av de två grupperna gäller din ordning. Listan laddas en sida i taget, så de dyker upp när sista sidan av piloternas annonser är inladdad: tryck på **Visa fler** tills den försvinner. Välj en, så går **Köp för …** till honom, inte till en pilot ([Davidski](/wiki/03-Mechanics/Davidski.md#buying-from-him)): hans priser är många gånger butikens, den dagliga köpgränsen räknar inte honom, det finns ingen säljare att betala och det du får är inte säljbart. Han finns inte i någon prisledtråd, i historiken eller i statistiken, som bara är piloternas egna.

## Köporder {#buy-orders}

En **köporder** är Marknaden åt andra hållet. I stället för att vänta på att en pilot lägger ut det du behöver säger du vad du vill ha, hur många partier och vad du betalar för ett parti, och varje pilot som har det kan sälja det till dig. Delen **Köporder** har två vyer: **Efterfrågat**, de andra piloternas ordrar, och **Mina order**, dina egna. Du behöver nivå 5, som för allt på Auktionen.

**Lägga en order.** Tryck på **Ny köporder**, välj sort, antal partier, krediter eller Thulium, priset för ett parti och hur länge ordern löper: 7, 14 eller 21 dagar. Priset är aldrig lägre än sortens lägsta pris, och det finns inget högsta pris; Thulium står öppet för samma sorter som i en annons. Innan du lägger den visar bladet vad den kostar: **hela priset hålls kvar**, tas direkt från din plånbok (sidan räknar det som **I order**), och en **deposition** som en annons betalas och förbränns. Dina första tio utläggningar varje UTC-dag, annonser och ordrar tillsammans, kostar ingen deposition. Bladet varnar dig med ord när det redan finns annonser till ditt pris eller under (det är billigare att köpa en), när ditt pris ligger långt över den billigaste annonsen, när plånboken är för liten eller platserna är fulla, och en stor order ber dig bekräfta en gång till. Ordrar har platser som annonser, med samma tal per nivå (tabellen under Sälja), räknade skilt från dina annonser, och en order får inte vara värd mer än hela din dagsgräns för köp.

**Bara Standard-föremål.** En order ber om Standard-föremål: inte smidda, alltså inget Befläckat, Gudomligt, Rämnande eller Evigt föremål och inga slumpade bonusar. Ett pris måste betyda en enda sak, och ett smitt föremål är varje gång något annat. Smidda föremål säljs fortfarande som annonser, med förtrollning och bonusar synliga.

**När den fylls.** En pilot som säljer till din order får betalt direkt, och du får föremålen direkt, med ett meddelande och ett eget ljud; en följd av fyllda ordrar är ett meddelande. Föremålen är **inte säljbara**, som allt du köper. Ordern står öppen för de partier som fortfarande efterfrågas tills den fylls, du återkallar den eller den löper ut. Du kan återkalla när som helst, även under säsongens sista dagar: priset för de återstående partierna kommer tillbaka helt. Depositionen kommer inte tillbaka, och ingen får den: den förbränns.

**Sälja till en order.** Välj en order under **Efterfrågat** och tryck på **Sälj**. Bladet listar dina föremål som passar och orsaken för varje som inte gör det, en stegare ställer in antalet partier, och **Du får** visar vad du får: priset **minus skatten på 5 %**, som köparen inte betalar. Etiketten **Jag kan leverera** visar bara de ordrar du kan fylla från ditt Hangar. Det som fyller en order måste vara säljbart (förtjänat, inte köpt) och Standard, och får inte vara utrustat, monterat i ett annat föremål, i Transportförrådet eller innehålla moduler; ett Cloaking CPU, ett EMP Charge eller ett Base CPU får inte ha använts. Ammunition, raketer och EMP Charge säljer du från stationen, som i en annons. Du kan inte fylla din egen order, och en order som fylls medan du tittar på den säger ”Den köpordern finns inte längre.” Säljbladet för ett föremål du ska lägga ut visar den bästa öppna ordern för det, så du kan sälja till den i stället.

**Gränserna.** En order använder en annons och en försäljnings gränser: nivå 5, platserna, dagsgränserna och gränsen mellan två piloter. En fylld order räknas mot köparens dagsgräns för köp och säljarens dagsgräns för försäljning, var och en i sin egen valuta, så en fyllning kan nekas när köparen eller du har nått en. Bärregeln för raketer och EMP Charge räknar det du har beställt: du kan inte beställa mer än du får bära.

**Avgifter.** Köparen betalar depositionen när ordern läggs, för de dagar ordern löper, och säljaren betalar skatten vid varje fyllning. Båda betalas i orderns valuta och **förbränns**. Under säsongens sista två dagar finns ingen av dem. En order som ingen fyller kostar sin deposition och inget mer.

**Återbetalning.** När en order återkallas, löper ut, avbryts av en administratör eller tar slut vid wipen, går priset för de partier som fortfarande efterfrågas tillbaka helt till din plånbok. Ordrar möts aldrig av sig själva med annonser: vill du ha ett utlagt föremål till dess pris, köp det.

## Gränser {#limits}

Varje valuta har sin egen dagliga gräns för hur mycket du kan sälja och hur mycket du kan köpa, räknat över de senaste 24 timmarna, och en gräns för hur mycket som går mellan två piloter, så att ett andra konto inte är något snabbt sätt att flytta en förmögenhet. Krediter och Thulium läggs aldrig ihop: den som säljer för Thulium använder sin Thulium-gräns och inget annat. Säljbladet varnar dig när en försäljning skulle gå över din dagliga säljgräns, och när ett köp skulle gå över din dagliga köpgräns säger Marknaden det och låter **Köp för …** vara avstängd. Gränserna växer med nivån, och Premium ändrar ingen av dem. Vunna lotter räknas inte.

Raketer i en annons, i en lott du leder och i ditt lastrum räknas alla in i det största antal av en raket du får bära: med en annons kan du inte bära mer än Butikens hög tillåter.

## Mina annonser och Historik {#my-listings-and-history}

**Mina annonser** visar dina platser och varje annons med sitt tillstånd (öppen, såld, avbruten, utgången, återlämnad eller pausad), en knapp **Återkalla**, en **diagramknapp** som ställer ditt pris mot vad andra piloter begär för föremålet, **Lägg ut igen** för en avslutad och en etikett **Underbjuden** när en annan annons på samma föremål begär mindre. En annons som har löpt ut kommer av sig själv tillbaka till ditt inventarie. **Historik** börjar med din handel de senaste 30 dagarna: dina försäljningar och köp, vad du har tjänat och gett ut, avgifterna och skatterna du har betalat, ditt nettoresultat, din bästa försäljning, din genomsnittliga försäljning och det föremål du har handlat mest med, samt två linjediagram: dina intäkter per dag och ditt resultat hittills (för krediter eller för Thulium, en i taget). Under dem kommer listan över vad du har sålt, köpt och vunnit, med skatten. Spelet sparar Auktionens huvudbok i 90 dagar. Dina köpordrar har en egen lista, **Mina order**, med hur mycket av varje som är fyllt, priset som fortfarande hålls kvar, tiden som återstår och **Återkalla**; Historik visar en fylld order som en vanlig försäljning eller ett vanligt köp.

Du får veta när något säljs eller när din order fylls: genom ett meddelande, Auktionens ljud och det nya saldot, och genom en bricka vid Auktionens post så länge sidan är stängd. En följd av försäljningar är ett meddelande. Auktionen har egna dova ljud, ett för varje sak du gör eller som händer dig där (lägga ut, avsluta, en försäljning, ett bud, bli överbjuden, vinna, lägga en order, en fylld order, sälja till en order), och de följer gränssnittets volym.

## Lotterna varje timme {#the-hourly-lots}

Lotterna är spelets egna erbjudanden: ammunition, raketer och EMP Charges, tre lotter varje timme (tolv är öppna samtidigt), att buda på. De är ett sätt att köpa ammunition billigare än Butiken begär, och en sänka: det vinnande budet förbränns. Bara lotterna i dagstabellen nedan öppnas (aldrig x1- eller x4-ammunition, aldrig Siphon Batteries, aldrig en särskild raket). **Varje lott bjuds på i krediter**, vad Butiken än begär för varorna: en lott med varor som Butiken säljer för Thulium (till exempel x2- och x3-ammunitionen och EMP Charge) öppnar till värdet av det Thulium-priset i krediter, med 200 krediter per Thulium, så du kan buda på vilken lott som helst utan en enda Thulium. Du kan buda på vilken lott som helst, vad du än redan bär: en lott du vinner är din hel, även om den tar dig över den hög som Butiken låter dig köpa.

<!-- market-lots:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- I början av varje UTC-timme öppnas 3 nya lotter, var och en med olika varor, och var och en är öppen i 4 timmar, så att 12 är öppna samtidigt.
- Startbudet är 20 % av butikspriset på varorna. Varje bud därefter måste ligga minst 5 % över det högsta budet, och minst 100 krediter mer.
- Ditt bud betalas direkt och hålls kvar. Om någon överbjuder dig kommer det tillbaka direkt.
- Ett bud under de sista 2 min av en lott flyttar dess slut till 2 min efter budet, högst 5 gånger.
- Det du vinner är till för att flyga, inte för att handla med: det är aldrig säljbart. Det vinnande budet förbränns. En lott som ingen bjuder på säljs inte och kostar ingen något.
- Hur stor en lott är följer piloterna på nivå 5 eller högre som tittat på auktionen de senaste 3 dagarna: med ingen är den 10 % av storleken i tabellen, med 30 eller fler full storlek, i steg om 500 för ammunition, 50 för raketer och 1 för EMP Charges.
- Under de sista 6 timmarna av en säsong skapas ingen lott. Wipen avbryter de lotter som fortfarande är öppna, och varje bud går tillbaka.

<!-- market-lots:end -->

<!-- market-day:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| UTC-timme | Lott | Full storlek | Startbud vid full storlek |
| :--- | :--- | ---: | ---: |
| 00:00 | Scatter III | 1 250 | 250 000 krediter |
| 00:00 | Advanced Plasma | 50 000 | 1 000 000 krediter |
| 00:00 | Ultra Core | 10 000 | 400 000 krediter |
| 01:00 | Advanced Plasma | 25 000 | 500 000 krediter |
| 01:00 | Ultra Core | 50 000 | 2 000 000 krediter |
| 01:00 | Lancet III | 1 250 | 250 000 krediter |
| 02:00 | Lancet I | 12 500 | 1 250 000 krediter |
| 02:00 | Advanced Plasma | 25 000 | 500 000 krediter |
| 02:00 | EMP Charge | 5 | 100 000 krediter |
| 03:00 | EMP Charge | 5 | 100 000 krediter |
| 03:00 | Advanced Plasma | 50 000 | 1 000 000 krediter |
| 03:00 | Lancet I | 12 500 | 1 250 000 krediter |
| 04:00 | Ultra Core | 25 000 | 1 000 000 krediter |
| 04:00 | Advanced Plasma | 25 000 | 500 000 krediter |
| 04:00 | Rivet I | 12 500 | 1 250 000 krediter |
| 05:00 | Rivet II | 5 000 | 800 000 krediter |
| 05:00 | Advanced Plasma | 25 000 | 500 000 krediter |
| 05:00 | EMP Charge | 5 | 100 000 krediter |
| 06:00 | Advanced Plasma | 10 000 | 200 000 krediter |
| 06:00 | Ultra Core | 50 000 | 2 000 000 krediter |
| 06:00 | Ember II | 5 000 | 800 000 krediter |
| 07:00 | Advanced Plasma | 50 000 | 1 000 000 krediter |
| 07:00 | Ultra Core | 25 000 | 1 000 000 krediter |
| 07:00 | Rivet II | 5 000 | 800 000 krediter |
| 08:00 | Ember I | 12 500 | 1 250 000 krediter |
| 08:00 | Advanced Plasma | 10 000 | 200 000 krediter |
| 08:00 | EMP Charge | 5 | 100 000 krediter |
| 09:00 | Ultra Core | 50 000 | 2 000 000 krediter |
| 09:00 | Advanced Plasma | 10 000 | 200 000 krediter |
| 09:00 | Ember II | 5 000 | 800 000 krediter |
| 10:00 | Scatter II | 5 000 | 800 000 krediter |
| 10:00 | Advanced Plasma | 25 000 | 500 000 krediter |
| 10:00 | EMP Charge | 5 | 100 000 krediter |
| 11:00 | EMP Charge | 5 | 100 000 krediter |
| 11:00 | Advanced Plasma | 50 000 | 1 000 000 krediter |
| 11:00 | Lancet I | 12 500 | 1 250 000 krediter |
| 12:00 | Advanced Plasma | 50 000 | 1 000 000 krediter |
| 12:00 | Ultra Core | 25 000 | 1 000 000 krediter |
| 12:00 | Scatter II | 5 000 | 800 000 krediter |
| 13:00 | Lancet III | 1 250 | 250 000 krediter |
| 13:00 | Advanced Plasma | 50 000 | 1 000 000 krediter |
| 13:00 | Ultra Core | 10 000 | 400 000 krediter |
| 14:00 | Ultra Core | 10 000 | 400 000 krediter |
| 14:00 | Advanced Plasma | 50 000 | 1 000 000 krediter |
| 14:00 | Ember I | 12 500 | 1 250 000 krediter |
| 15:00 | Advanced Plasma | 25 000 | 500 000 krediter |
| 15:00 | Ultra Core | 50 000 | 2 000 000 krediter |
| 15:00 | Lancet III | 1 250 | 250 000 krediter |
| 16:00 | Ultra Core | 50 000 | 2 000 000 krediter |
| 16:00 | Advanced Plasma | 10 000 | 200 000 krediter |
| 16:00 | Scatter III | 1 250 | 250 000 krediter |
| 17:00 | Rivet I | 12 500 | 1 250 000 krediter |
| 17:00 | Advanced Plasma | 10 000 | 200 000 krediter |
| 17:00 | EMP Charge | 5 | 100 000 krediter |
| 18:00 | Advanced Plasma | 50 000 | 1 000 000 krediter |
| 18:00 | Ultra Core | 25 000 | 1 000 000 krediter |
| 18:00 | Scatter II | 5 000 | 800 000 krediter |
| 19:00 | Ember II | 5 000 | 800 000 krediter |
| 19:00 | Advanced Plasma | 25 000 | 500 000 krediter |
| 19:00 | EMP Charge | 5 | 100 000 krediter |
| 20:00 | Ultra Core | 25 000 | 1 000 000 krediter |
| 20:00 | Advanced Plasma | 25 000 | 500 000 krediter |
| 20:00 | Rivet I | 12 500 | 1 250 000 krediter |
| 21:00 | Advanced Plasma | 25 000 | 500 000 krediter |
| 21:00 | Ultra Core | 25 000 | 1 000 000 krediter |
| 21:00 | Rivet II | 5 000 | 800 000 krediter |
| 22:00 | Advanced Plasma | 10 000 | 200 000 krediter |
| 22:00 | Ultra Core | 50 000 | 2 000 000 krediter |
| 22:00 | Scatter III | 1 250 | 250 000 krediter |
| 23:00 | EMP Charge | 5 | 100 000 krediter |
| 23:00 | Advanced Plasma | 50 000 | 1 000 000 krediter |
| 23:00 | Ember I | 12 500 | 1 250 000 krediter |

<!-- market-day:end -->

När få piloter använder Auktionen är lotterna små, så att en handfull piloter inte erbjuds tusentals skott varje timme; de växer när fler piloter tittar.

**Buda med ett maxbud.** Slå på *Buda automatiskt upp till ett maxbud* i budfönstret och skriv det mesta du är beredd att betala. Auktionen bjuder då åt dig: den tar det lägsta bud som lottet godtar, och varje gång någon överbjuder dig bjuder den igen, ett lägsta steg över det högsta budet, upp till ditt maxbud och inte längre. Budet du leder på är det lägsta som slår nästa bästa maxbud, inte ditt maxbud: med maxbud på 500 och 800 krediter på ett lott som öppnade på 100 leder det högre på 600, inte på 800. Är två maxbud lika vinner det som lades först. Hela ditt maxbud reserveras från din plånbok när du lägger det, så inget automatiskt bud kan misslyckas för att pengar saknas; när lottet slutar betalar du bara det vinnande budet och resten betalas tillbaka, och om någon går över ditt maxbud kommer allt tillbaka direkt och du får veta det. På ett lott du leder höjer knappen **Maxbud** ditt maxbud när som helst eller sänker det ner till ditt nuvarande bud. Att lägga ett maxbud är inget bud, men varje bud räknas för förlängningsregeln, också Auktionens eget. Att lägga ett maxbud har ett eget lågmält ljud, på ljudeffektsvolymen.

## Säsongen och wipen {#the-season-and-the-wipe}

Auktionen följer säsongen (se [Wipe-tidslinje](/wiki/03-Mechanics/Wipe-Timeline.md)). Under de sista två dagarna finns inga avgifter. Från dag 30, när wipens femminutersnedräkning börjar, är den stängd: inget läggs ut, köps, beställs eller budas på, en lott som slutar då avbryts och budet betalas tillbaka, och du kan fortfarande avbryta dina egna annonser. En annons löper aldrig längre än säsongens slut.

Vid wipen **kommer varje öppen annons tillbaka till sin säljare** som lösa föremål, och wipen raderar sedan lösa föremål som alla andra (bara det du lägger i [Transportförrådet](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) finns kvar): sälj alltså, eller avbryt och lägg i förrådet det du vill behålla. De lotter som fortfarande är öppna avbryts och buden betalas tillbaka. Dina öppna köpordrar tar också slut: priset de fortfarande håller kvar går helt tillbaka till din plånbok, och depositionen är borta. Krediter och Thulium wipas inte heller, upp till [taken](/wiki/03-Mechanics/Wipe-Timeline.md#the-caps): pengarna som kommer tillbaka till din plånbok från bud på lotter och köpordrar räknas innan taken tillämpas.

## Vad Auktionen inte ger dig {#what-the-auction-does-not-give-you}

Auktionen finns för att handla med det du förtjänar, och den är ärlig om sina gränser.

- **Att sälja byte är ingen grind.** Rått byte från utomjordingar är bara resurser och är värt 0,4 till 0,9 procent av vad samma jakttimme på nivå 5 betalar i dödade fiender. Det Marknaden ger en ny pilot är utrustningen som hans uppdrag betalar ut och som han inte behöver (en gång), resurserna från Utmaningsuppdragen, svärmbossarnas lådor och det han tillverkar.
- **Det finns ingen mellanhand.** En köporder tillhör en pilot och täcks av hans egna pengar: spelet köper inte av dig till något pris. Köpordrar, där en pilot säger vad han vill köpa och för hur mycket, ger en säljare en köpare som alltid finns där, och hantverkaren, som köper material, tillverkar utrustning i Monteringen och säljer den, ett sätt att beställa det; en order kan också vänta på en säljare, eller löpa ut och förbränna sin deposition. De ändrar inget i den första punkten.
- **Butikens utrustning är inte till för vidareförsäljning.** Utrustning du köpte i Butiken kan inte säljas igen: hit hör Quantum Laser I och II, Light och Basic Shield Core, Engine I och II, första graden av celler och styrraketer, de amps som Butiken säljer och köpt ammunition. Den enda säljbara Quantum Laser II en pilot har är den som ett uppdrag betalar ut en gång.
- **Plattor kommer från uppdrag.** Velkonite och Orvium Reinforced Plates på Marknaden är de som Utmaningsuppdragen betalar ut. Smedjans plattor står utanför, annars skulle de bli den största varan på Marknaden.

Om en annons ser fel ut, anmäl den på vanligt sätt: spelets administratörer kan pausa en annons, återlämna den, pausa Auktionen eller stänga av en pilot från den, och varje sådan åtgärd registreras.
