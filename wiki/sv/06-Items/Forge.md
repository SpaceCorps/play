<!-- wiki-i18n source: 1bd2092b2dd812be -->
<!-- wiki-i18n title: Smedjan -->
# Smedjan {#the-forge}

<!-- wiki-search: forge; smedjan; smedja; nivåhöjning; nivå upp; nivå; nivåer; sockel; socklar; sockets; stäm; stämma; stämning; omläggning; lägg om; shard; shards; echo; echo shard; lattice; lattice shard; heartshard; integritet; spricka; sprickor; reparera; reparation; sammanslagning; slå ihop; fusion; tainted; godly; rupturing; eternal; befläckad; gudomlig; rämnande; evig; awakened; resonant; radiant; ascendant; vaknad; strålande; uppstigen; tinkerer's badge -->

**Smedjan** är den andra fliken på sidan Montering (och i fönstret Montering under flygning). Den gör tre saker med utrustning du äger: den **höjer ett föremål en nivå** mot krediter och byte från utomjordingar, den **stämmer dess socklar** med shards (därifrån kommer dess bonusar) och den **slår ihop två exemplar** av ett föremål till ett som behåller det bästa från båda. En nivåhöjning misslyckas aldrig, och Smedjan lägger bara en ny bonus i ett föremål när du väljer den ur ett erbjudande. (Före 0.5.7 hette nivåerna Befläckad, Gudomlig, Rämnande och Evig, och ett steg kunde misslyckas; nu heter de Vaknad, Resonant, Strålande och Uppstigen.) Den ersatte den gamla Fusionskammaren, som krävde fem identiska föremål och lämnade resultatet åt ett slumpslag på 25 %.

## Vad som kan smidas {#what-can-be-forged}

Lasrar, laserförstärkare, sköldkärnor, sköldceller, motorer, styrraketer, adaptiva kärnor, Repair Drones och [skrovpansar](/wiki/06-Items/Hull-Plating.md): varje enskild utrustningsdel som kan bära [förtrollningsbonusar](/wiki/06-Items/Overview.md). Den kan ligga i ditt inventarie, sitta på ett skepp (där blir den kvar och fungerar med sin nya nivå direkt) eller vara monterad i ett annat föremål. Drönare, skepp, ammunition, resurser och boosters kan inte smidas, och inte heller något i transportförrådet eller monterat i Motormodulen eller Försvarsmodulen i ditt Skylab: ta ut det först.

Listan över utrustning har en växel **Alla / Utrustade / I inventariet** bredvid de andra filtren. **Utrustade** visar det som sitter på ett skepp eller är infogat i ett annat föremål, **I inventariet** det som ligger löst, och en rad under titeln säger hur många delar växeln döljer. Medan du väljer givaren till en sammanslagning är ”Utrustade” pausat, eftersom en givare måste ligga löst.

En rullgardin **Skepp** bredvid typfiltret visar bara delarna på ett av dina skepp (en del som sitter i ett annat föremål räknas till det skepp där dess värd sitter). Den är pausad under ”I inventariet” och medan du väljer givaren till en sammanslagning. Kortet vid hovring, panelens rubrik och sammanslagningens bas säger var en del finns: *På Kitefin, konfiguration 1* (ett skrovpansar: båda konfigurationerna) och vad den sitter i. **Ctrl+F** (Cmd+F på Mac) lägger markören i sökrutan i Monteringens rubrik; den smalnar av listan på den öppna fliken (recept efter vad de tillverkar och kräver, utrustning efter namn, typ och nivå), och Esc rensar den. Under *Vakna socklar* säger panelen till när ett värde hos delen är för lågt för en bonus, och därför rymmer en Impulse Thruster en bonus och en Momentum Thruster två.

## Nivå upp {#tier-up}

Välj ett föremål så visar panelen dess nivå, vilken nivå det skulle nå, vad det ändrar (hur många bonusar det kan rymma och hur stora de är), och priset med vad du har av varje del: grönt när du har tillräckligt, rött när du inte har det, och hur många du saknar. När du har allt höjer knappen **Höj till …** föremålet exakt en nivå. Det finns inga hopp: för att nå Uppstigen går ett föremål genom Vaknad, Resonant och Strålande, var och en med sitt eget pris.

| Steg | Krediter | Thulium | Material |
| :--- | :---: | :---: | :--- |
| Standard till Vaknad | 10 000 | – | 5 Ship Fragment, 15 Daraxium |
| Vaknad till Resonant | 56 000 | – | 32 Ship Fragment, 48 Nyxite |
| Resonant till Strålande | 267 000 | – | 23 Reinforced Hull Plate, 140 Cataclysite, 2 Dark Matter Plate |
| Strålande till Uppstigen | 833 000 | 2 667 | 11 Power Core, 320 Quorvium, 2 Dark Matter Plate |

- **Material** tas från dina lösa högar: föremål på ett skepp och högar i transportförrådet används inte. Panelen berättar när de som saknas ligger i förrådet.
- **Ett steg lyckas alltid.** Det kostar vad ett steg i genomsnitt kostade innan Smedjan hade socklar, och det väcker ytterligare en sockel i föremålet (se [Bonusar per nivå](#buffs-by-tier)).
- **Din Commerce-färdighet** sänker kreditkostnaden och Thulium-kostnaden för ett steg, och kreditkostnaden för en sammanslagning, med upp till 15 % på nivå 100 ([Pilotfärdigheter](/wiki/03-Mechanics/Pilot-Skills.md)). Tabellen visar priset på första nivån och panelen det pris du betalar; materialen ändras inte.
- **Varje bonus som föremålet har** slumpas på nytt inom den nya nivåns spann och behåller det bättre värdet. Resultatet visas ovanför panelen; föremålet förblir valt, så dess nästa steg syns redan på skärmen.
- En nivåhöjning sker direkt.
- **Socklarna ligger under steget.** Nivå upp och [Socklar](#sockets) är en enda vy, **Uppgradera**, med Nivå upp först: sockeln som ett steg väcker står i listan strax under knappen, med sin knapp Stäm, så du behöver inte byta vy för att använda den.
- **Ett Tinkerer's Badge** (ett [specialföremål](/wiki/06-Items/Special-Items.md#tinkerers-badge)) höjer en del en nivå utan krediter, utan Thulium och utan material, redan från Standard. Det är ett steg som inte kostar något: det väcker en sockel och slår om de bonusar delen har, som ett betalt steg.

### Dark Matter Plates

De två sista stegen kräver **2 Dark Matter Plates** vardera, utöver allt annat. En platta pressas i [Monteringen](/wiki/06-Items/Overview.md) av **5 Dark Matter, 1 Velkonite Reinforced Plate och 1 Orvium Reinforced Plate** (250 Thulium, 2 minuter), så ett steg kräver 10 Dark Matter, 2 Velkonite-plåtar och 2 Orvium-plåtar. Dark Matter kommer från [det svarta hålet](/wiki/03-Mechanics/Black-Hole.md): ungefär fem N.I.K.E.-raketer (se [Raketer](/wiki/06-Items/Rockets.md)) ger tio; en N.I.K.E. som möter ett skepp på vägen träffar det skeppet i stället och ger ingen Dark Matter. Plattorna tas från dina lösa högar som de andra materialen, och panelen nämner dem om du har för få. Sista nivån i varje uppgraderingskedja kräver också plattor, 4 vardera ([Dark Matter och Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)).

### Bonusar per nivå {#buffs-by-tier}

| Nivå | Högst antal bonusar | Storlek på varje bonus | Stegets kristall |
| :--- | :---: | :---: | :--- |
| Vaknad | 1 | +2 % till +5 % | Daraxium |
| Resonant | 2 | +4 % till +8 % | Nyxite |
| Strålande | 3 | +6 % till +11 % | Cataclysite |
| Uppstigen | 4 | +9 % till +15 % | Quorvium |

Utrustning som gjordes före Smedjan behåller de bonusar den slumpades med, och de är ofta mindre än tabellen anger (en Resonant del från den tiden kan ha +2 %). Ingenting höjer dem av sig självt: en nivåhöjning slumpar varje bonus på nytt inom den nya nivåns intervall och behåller det bättre värdet, och en sammanslagning behåller det bättre värdet för varje värde.

Ett föremål kan inte rymma fler bonusar än det har värden: en sköldkärna har fyra, en laser tre, en motor eller en adaptiv kärna två, en Momentum Thruster två, en Impulse Thruster en (dess multiplikator på 1,017 till 1,03 är för liten för en bonus, och Smedjan slumpar ingen på en multiplikator på 1,05 eller lägre, så dess bonus kan bara ligga på den fasta hastigheten), en Crit Amp I, en Repair Drone eller ett skrovpansar bara en (dess skrov), de högre kritförstärkarna två, skadeförstärkarna och sköldcellerna tre. När nästa nivå inte rymmer fler bonusar än föremålet kan bära säger panelen det: nivån gör då bara bonusarna starkare. Bonusar på räckvidd går aldrig över +5 %. En Penetration Amp har bara ett värde och rymmer därför en bonus.

**En nivå rymmer högst så många bonusar.** Varje nivåhöjning väcker en sockel i föremålet, den som hör till stegets kristall: Daraxium väcker den första, Nyxite den andra, Cataclysite den tredje och Quorvium den fjärde. Ett föremål har så många socklar som nivån rymmer och som föremålet har värden för: en sköldkärna på nivån Resonant har två, en på nivån Uppstigen alla fyra, och en motor, som har två värden, har ingen tredje sockel att väcka. En bonus hamnar i en sockel när du stämmer den med en Echo Shard och väljer den ur erbjudandet. En **sammanslagning** behåller den bästa bonusen för varje värde hos två exemplar, upp till nivåns gräns.

En **skölds absorptionsbonus** (och en sköldcells absorptionsökning) multiplicerar värdet, så den är värd punkter av [absorption](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-) i proportion till det: +5 % på en Heavy Shield Cores 55 % är +2,75 punkter, och +15 % på varje del i den bästa uppsättningen (en Heavy Shield Core och tre Absorption Shield Cell IV, 91 % sammanlagt) är +13,65 punkter. En Uppstigen uppsättning ger mellan +8,2 och +13,65 punkter, ungefär 11 i snitt; med säsongsbutikens Shield Absorbance Boost (+10 punkter vid sin gräns; en wipes wipepoäng räcker till 44 av dess 100 nivåer, +4,4 punkter) tar det ett skepp till omkring 106 %, och långt förbi det med Pilot-forskningen Field Theory (upp till +10 punkter), vilket värdet tillåter: en angripares sköldgenomträngning dras av från det. En Resonant uppsättning ger mellan 3,6 och 7,3 punkter. Det är siffrorna för bonusar utan någon spricka på sig ([Integritet och sprickor](#integrity-and-fractures)).

Motorer, styrraketer, adaptiva kärnor och Repair Drones påverkas mycket lite av en procentbonus (en Engine II ger 10 i fart, så +12 % är 1,2 punkter): smid dem om du vill ha nivån, inte för värdena.

**Bonusen på en Penetration Amp** multiplicerar dess genomträngning: en Uppstigen bonus (+9 % till +15 %) gör en Penetration Amp IV till 21,8 till 23 punkter per plats i stället för 20. Inget begränsar genomträngningen i en träff, så varje punkt räknas: i den bästa lasern (en Fusion Core, en Gemini och tre Penetration Amp IV i varje laser) blir 10 + 15 + 60 lika med 85 %, och tre Uppstigna bonusar lyfter det till så mycket som 94 % ([Lasrar och ammunition](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)).

### Varifrån materialen kommer {#where-the-materials-drop}

| Material | Byte från |
| :--- | :--- |
| **Ship Fragment** | alla utomjordingar |
| **Daraxium** | [Seeker](/wiki/04-Aliens/Seeker.md), [Phantasm](/wiki/04-Aliens/Phantasm.md) |
| **Nyxite** | [Phantasm](/wiki/04-Aliens/Phantasm.md), [Bulwark](/wiki/04-Aliens/Bulwark.md) |
| **Reinforced Hull Plate** | [Bulwark](/wiki/04-Aliens/Bulwark.md), [Goombah](/wiki/04-Aliens/Goombah.md) |
| **Cataclysite** | [Bulwark](/wiki/04-Aliens/Bulwark.md), [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Power Core** | [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Quorvium** | [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Dark Matter Plate** | ingen utomjording: Monteringen pressar den av Dark Matter ([det svarta hålet](/wiki/03-Mechanics/Black-Hole.md)) och Skylabs plåtar |

Kristallerna följer nivåerna: Daraxium har samma blå färg som Vaknad, Nyxite samma gula som Resonant, Cataclysite samma orange som Strålande och Quorvium samma violetta som Uppstigen. Varje källa, med chanser och mängder, finns på sidan [Resurser](/wiki/06-Items/Resources.md) och på varje utomjordings sida; Resource Magnet Booster ger 25 % mer i det en låda innehåller. [Asteroiderna](/wiki/03-Mechanics/Asteroid-Mining.md#the-kinds) lämnar allt utom Dark Matter Plate i sina bitar.

## Socklar {#sockets}

Blocket **Socklar** i Smedjans vy **Uppgradera**, under Nivå upp, är där en bonus hamnar i ett föremål. Välj en del så listar blocket dess socklar, dess integritet och de shards du har. En sockel är **låst** tills en nivåhöjning väcker den (dess rad säger på vilken nivå och med vilken kristalls steg), **tom** när den är vaken och **stämd** när den bär en bonus. Blocket Nivå upp räknar dem: *Vakna socklar 1 → 2 av 4*.

- **Stäm** en tom sockel med **Echo Shards**: 10 för den första sockeln på en del, sedan 20, 40 och 80, så priset stiger för varje sockel du stämmer (det nedtonade priset på varje senare tom sockel visar vad den kommer att kosta). Shards förbrukas när du trycker på Stäm, och Smedjan lägger då fram ett **erbjudande**: två av de värden som ännu är lediga, slumpade, vart och ett med den bonus det skulle ge. **Välj** ett: du får det erbjudandet visade. När bara ett värde är ledigt är båda raderna slag på det värdet, och de kan bli lika.
- Ett **Heartshard** kan läggas till en stämning eller en omläggning: slå först på *Använd ett Heartshard vid nästa stämning eller omläggning*, så listar erbjudandet i stället alla lediga värden på delen, vart och ett slumpat i övre halvan av sitt intervall, så du väljer värdet själv.
- **Lägg om** en stämd sockel med **Lattice Shards** när du vill ha ett annat värde där. Det kostar 2 Lattice Shards för den första omläggningen av en del, sedan 3, 4, 4, 5, 7 och så vidare (2 gånger 1,25 en gång för varje tidigare omläggning, uppåtavrundat) och en del av delens integritet: 6 poäng, färre med Tillverkning ([Integritet och sprickor](#integrity-and-fractures)). En ruta frågar först, eftersom shards och integritet förbrukas vad du än väljer. Erbjudandet görs som en stämnings, av de lediga värdena och det värde sockeln har nu, vart och ett slumpat på nytt, och det har, över hela bredden, en knapp **Behåll nuvarande**, för när inget av dem slår den bonus sockeln har.
- **Tills du väljer väntar delen.** Ett öppet erbjudande blockerar delen: inget annat fungerar på den, och panelen säger det. Att stänga spelet förlorar ingenting, erbjudandet finns kvar när du kommer tillbaka. Ett erbjudande som ingen svarar på avgörs åt dig efter 7 dagar, nästa gång Smedjan rör vid delen (det räcker att välja den där): en stämning tar erbjudandets första värde, en omläggning behåller den nuvarande bonusen. Auktionen och modulupgraderingarna i Monteringen avgör aldrig ett erbjudande, de vägrar delen tills Smedjan har gjort det, så öppna delen i Smedjan först.
- **Reparera** återställer 12 integritet för dubbla antalet Lattice Shards som nästa omläggning skulle kosta. Det sänker inte antalet omläggningar, så priset på nästa omläggning står kvar.
- **Mätaren** visar integriteten med ett märke vid varje punkt där ytterligare en spricka öppnas (den första öppnas med den första förlorade punkten), och när du håller muspekaren över den står det vilket värde varje spricka tog. En stämd sockel vars bonus har tappat poäng på grund av en spricka visar båda talen (en bonus på +9 % med två sprickor: *−4 % av sprickor (slumpat: +9 %)*), och en som är nere på noll säger *Bortsprucken: ingen bonus kvar*. Sockeln förblir stämd och dess bonus är +0 %.
- **Bara lösa högar förbrukas.** Shards i transportförrådet gör det inte, och panelen säger till när de som saknas ligger där. Shards kan inte köpas, säljas eller läggas ut på Auktionen, och varken tur eller Resource Magnet Booster ökar dem.

### Var shards kommer ifrån {#where-the-shards-come-from}

Att stämma alla fyra socklarna på en del kostar 150 Echo Shards (10 + 20 + 40 + 80), och dess första 16 omläggningar kostar 283 Lattice Shards. De kommer från [Soloportar](/wiki/03-Mechanics/Solo-Gates.md) och [Dungeons](/wiki/03-Mechanics/Dungeons.md), utöver vad de betalar i övrigt, och från några få Echo Shards från utomjordingar:

| Källa | Echo Shards | Lattice Shards |
| :--- | :---: | :---: |
| Soloport: Alpha Rift | 4 | 6 |
| Soloport: Beta Breach | 9 | 13 |
| Soloport: Gamma Foundry | 18 | 27 |
| Soloport: Delta Siege | 29 | 44 |
| Soloport: Omega Vault | 34 | 54 |
| Klandungeon: etapp 1 | 12 | 5 |
| Klandungeon: etapp 2 | 8 | 6 |
| Klandungeon: etapp 3 | 8 | 7 |

- **Soloportar** betalar sina shards vid varje avklarning, **klandungeons** vid varje betald avklarning av en etapp.
- **Heartshards** kommer med första avklarningen av varje port och varje dungeonetapp under en säsong (1) och med 5 % chans till 1 till vid varje avklarning. De sällsynta NPC:erna droppar dem också: 10 % Davidski, 5 % Dormant Force och Tesseract. Sidan [Resurser](/wiki/06-Items/Resources.md#heartshard) har resten.
- **Utomjordingar** droppar bara Echo Shards, och få: från 0,8 % per nedskjutning för en Seeker till 40 % för en Crystalys ([Echo Shard](/wiki/06-Items/Resources.md#echo-shard)).

## Slå ihop {#merge}

Två exemplar av samma föremål (två Light Shield Core, två Quantum Laser II) blir ett. Byt till **Slå ihop** och klicka på det föremål du vill behålla (**basen**), sedan på ett andra exemplar (**givaren**). Panelen visar resultatet innan du bekräftar.

- **Basen behålls.** Den behåller sin plats: den kan sitta på ett skepp eller vara monterad i ett annat föremål, och modulerna som sitter i den blir kvar. **Givaren förbrukas.** Den måste vara lös (inte på ett skepp, inte monterad), och modulerna som sitter i den går tillbaka till ditt inventarie.
- **Resultatet får den högre av de två nivåerna**, och för varje värde det **bättre av de två värdena**.
- **Det rymmer aldrig fler bonusar än nivån tillåter.** Har de två föremålen tillsammans fler bonusar än resultatets nivå kan rymma behålls de bästa och resten faller bort; tabellen markerar dem (överstrukna, ”över gränsen”). För att rymma fler bonusar, höj först föremålets nivå. En sammanslagning slumpar aldrig något: det förhandsvisningen visar är det du får.
- **En sammanslagning kostar krediter efter den nivå den ger**: 5 000 för Vaknad, 25 000 för Resonant, 100 000 för Strålande, 250 000 för Uppstigen. Inga material. Din Commerce-färdighet sänker kreditkostnaden som för ett steg.
- En sammanslagning som inte skulle ändra något (resultatet är inte bättre än basen) nekas. Bättre integritet enbart räknas inte: en sammanslagning är ingen reparation.
- **Integritet.** Resultatets integritet är medelvärdet av de två delarnas integritet (avrundat nedåt) minus 6, aldrig under 0, och dess antal omläggningar är det högsta av de två: två hela delar slås ihop till en del med 94. Resultatet behåller basens ordning av sprickor: samma värde träffas först. Se [Integritet och sprickor](#integrity-and-fractures).
- Efter en sammanslagning förblir resultatet valt och givarplatsen är tom: lägg i nästa givare, eller byt tillbaka till Uppgradera.
- **Etiketten**: den sammanslagna delen är bara **säljbar** (du kan sälja den i [Auktionen](/wiki/03-Mechanics/Auction.md#marketable-items)) om både basen och donatorn var det. Förhandsvisningen säger det.

En sammanslagning mångfaldigar inte ett föremål. Dess nytta är att välja: en sköldkärna på nivån Resonant med de värden du vill ha, eller en nivå som flyttas till föremålet på ditt skepp utan att du tar av det.

## Integritet och sprickor {#integrity-and-fractures}

Varje utrustningsdel har en **integritet** från 0 till 100. En del som ingen har arbetat med står på 100. En del som du tillverkar i Monteringen eller får som byte (ur en kista från en utomjording, en svärm eller en Warden, eller som utrustningskort från en klandungeon) börjar någonstans mellan 70 och 100; det du köper eller får i gåva, och allt du hade före 0.5.7, är helt. Att lägga om en sockel (det kostar ett Lattice Shard) kostar integritet: 6 poäng, 5 från nivå 29 i Tillverkning och 4 från nivå 84 ([Pilotfärdigheter](/wiki/03-Mechanics/Pilot-Skills.md)); en del som inte har mer än så kvar kan inte läggas om. En reparation ger tillbaka 12 poäng (se [Socklar](#sockets)).

Varje 12 poäng under 100 är en **spricka**, och påbörjade 12 räknas också: en del på 99 till 88 har en, på 87 till 76 två, och så vidare, högst 8. En spricka tar 2 poäng från ett värdes bonus: en bonus på +9 % med två sprickor på sig blir +5 %. Sprickorna träffar föremålets värden i tur och ordning, i en ordning som är fast för varje del: den första sprickan träffar ett värde, den andra nästa, och när varje värde har fått en börjar varvet om. Ett värde utan bonus träffas också: dess sprickor väntar och räknas i samma stund som du stämmer in en bonus på det. En bonus går aldrig under +0 %, så en spricka gör aldrig en del sämre än det vanliga föremålet. Ett föremål med bara ett enda värde att ge bonus (en Hull Plating, en Repair Drone, en Crit Amp I, en Penetration Amp, en Impulse Thruster) tar alla sprickor på det värdet: vid 8 sprickor, 16 poäng, blir inte ens en bonus på +15 % kvar.

Det som inventariet, hangaren, auktionen och Smedjan visar för en skadad del är det den **flyger med**: sprickorna är redan avdragna och en lista över sprickorna står bredvid. En nivåhöjning och en modulgradering lämnar integriteten som den är; en [sammanslagning](#merge) sätter den till medelvärdet av de två delarna minus 6.

## Säsongens wipe {#the-season-wipe}

En del som [wipen](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) behåller (en som sitter på skeppet som behåller sin utrustning, en som sitter i din Skylab, en i transportförrådet) behåller allt som Smedjan har gjort med den: dess nivå, dess stämda socklar och deras bonusar, dess integritet, dess antal omläggningar och ett erbjudande som fortfarande är öppet. Wipen reparerar ingenting och förstör ingenting. Shards är resurser som malmerna: wipen förstör de lösa, och de du lägger i transportförrådet behålls (1 kg styck).

## Modulupgraderingar i Monteringen {#module-upgrades-in-the-assembly}

De tre översta lasrarna, de översta laserförstärkarna, sköldcellerna och styrraketerna på nivå II till IV, motorerna och de adaptiva kärnorna på nivå II och III samt Heavy Shield Core säljs inte, och Monteringen tillverkar var och en först när du har forskat fram dess teknologi i Skylab ([Forskning](/wiki/03-Mechanics/Research.md)). Du tillverkar dem på Monteringens flik **Tillverkning** genom att uppgradera delen ett steg nedanför: en Damage Amp III till en **Damage Amp IV**, en Crit Amp III till en **Crit Amp IV**, en Capacity Shield Cell I till en **Capacity Shield Cell II** (och vidare till III och IV; Absorption Shield Cell, Impulse Thruster och Momentum Thruster stiger på samma sätt), en Basic Shield Core till en **Heavy Shield Core**, en Engine I till en **Engine II** och vidare till en **Engine III**, en Adaptive Core I till en **Adaptive Core II** och vidare till en **Adaptive Core III**, en Quantum Laser II till en **Quantum Laser III**, en Quantum Laser III till en **Starfire-III** och en Starfire-III till en **Helios Beam**. Det Smedjan har med saken att göra är nivån. Den första nivån i varje förstärkarserie (Damage Amp I, Crit Amp I och Penetration Amp I) säljs i butiken; nivå II till IV i varje serie tillverkas på samma sätt.

- **Nivån består.** En uppgradering förbrukar ett exemplar av delen, och det nya föremålet får det exemplarets nivå: en Resonant Damage Amp III ger en Resonant Damage Amp IV, en Standard Damage Amp III en Standard Damage Amp IV. Det du betalat Smedjan för går inte förlorat. Uppgraderingen lägger inte till någon egen nivå, så en del på Standard ger alltid ett resultat på Standard.
- **Bonusarna behålls.** Det nya föremålet behåller bonusarna hos delen du förbrukar: samma värden med samma storlek, inget slumpas på nytt (en Resonant Damage Amp III med två bonusar ger en Resonant Damage Amp IV med just de två, en med en enda bonus ger en med just den). Varje värde hos en del finns också hos dess uppgradering, så varje bonus hittar sin plats, och en uppgradering stämmer varken en tom sockel eller tar bort någon bonus. Bonusarna fastställs i samma stund som du köar jobbet, och det du hämtar är det som fastställdes: att vänta med att hämta ändrar ingenting, och avbryter du jobbet kommer exakt samma del tillbaka, med nivå och bonusar som de var. Ett jobb som köades före den här regeln behåller de bonusar det slumpades med. Det som kostar är det Smedjan gjorde av delen: en Uppstigen del kostar över en miljon krediter i Smedjans steg, och uppgraderingen behåller allt det. **Delens integritet och dess antal omläggningar följer också med den**: en uppgradering är ingen reparation och tar bort ingen spricka.
- **Plåtar.** Förutom Thulium och det utomjordingarna släpper kräver varje modulupgradering plåtar. Sista nivån kräver **4 Dark Matter Plates** och minst en Ancient Control Unit: en förstärkare, en cell eller styrraket på nivå IV, Heavy Shield Core, Engine III, Adaptive Core III och Helios Beam. Stegen före den kräver **Velkonite Reinforced Plates**: 2 för en förstärkare på nivå II eller III, 4 för en cell eller en styrraket på nivå II eller III, 3 för en Quantum Laser III, 4 för en Engine II eller en Adaptive Core II och 8 för en Starfire-III (Helios Beam kräver dessutom 18 Orvium Reinforced Plates). Utomjordingar släpper ingen av dem. Din [Skylabs](/wiki/03-Mechanics/Skylab.md) smedjemodul tillverkar Velkonite- och Orvium-plåtarna av malm, 40 Velkonite-malm per plåt på smedjemodulens nivå 1. En Velkonite-samlare på nivå 1 bryter 10 malm i timmen, så plåtarna till en förstärkare på nivå III är 8 timmars brytning och plåtarna till en cell eller en styrraket på nivå III 16 (4 och 9 timmar från en samlare på nivå 5). Monteringen pressar en [Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md) av 5 Dark Matter, en Velkonite Reinforced Plate, en Orvium Reinforced Plate och 250 Thulium, när du har forskat fram plattans recept. Varifrån varje material kommer står på sidan [Resurser](/wiki/06-Items/Resources.md). Smedjans egna steg kräver byte och krediter, och de översta stegen kräver också Dark Matter Plates (Resonant till Strålande: 23 Reinforced Hull Plates och 2 Dark Matter Plates; Strålande till Uppstigen: 2 Dark Matter Plates): samma plattor som sista nivån i en modulupgradering.
- **Vilket exemplar som används.** Du väljer. När du har exemplar som skiljer sig åt (en annan nivå eller andra bonusar) visar receptkortet dem som en rad rutor: klicka på det som ska användas, så visar raden under rutorna vad det blir (”Resonant Damage Amp III”, sedan ”Resultat: Resonant Damage Amp IV”). Väljer du inget går det enklaste åt: lägsta nivån först, och bland exemplar på samma nivå det äldsta, oavsett deras bonusar. Ett exemplar på Resonant nivå eller högre används aldrig så länge ett enklare ligger löst. Att använda ett exemplar över Standard frågar först och nämner föremålet vid namn.
- **Vilka exemplar som kan användas.** Lösa: ett exemplar på ett skepp (även på en förmågeplats), monterat i ett annat föremål, sittande i Motormodulen eller Försvarsmodulen i ditt Skylab, med egna celler eller styrraketer i sig eller i [transportförrådet](/wiki/03-Mechanics/Cargo.md) kan inte användas, och Monteringen säger det. Ta av det eller ta ut det ur förrådet först. Två uppgraderingar som startas samtidigt kan inte använda samma exemplar.

- **Quantum Laser III är också en uppgradering.** Den tillverkas av en **Quantum Laser II**, butikens laser (med 1 500 Thulium, 10 Ship Fragments och 3 Velkonite Reinforced Plates: se [Lasrar](/wiki/06-Items/Lasers.md)), och allt ovan gäller: en Resonant Quantum Laser II ger en Resonant Quantum Laser III med samma bonusar, du väljer exemplaret, kortet frågar innan det använder ett över Standard, och Quantum Laser II måste ligga löst: ta av den i hangaren först, och knappen Montera säger ”Ta ut Quantum Laser II först” tills du gjort det. Nivån går sedan vidare uppåt: en Resonant Quantum Laser III ger en Resonant Starfire-III.

- **Starfire-III är också en uppgradering.** Den tillverkas av en **Quantum Laser III** (med 1 500 Thulium, 100 000 krediter, byte och 8 Velkonite Reinforced Plates: se [Lasrar](/wiki/06-Items/Lasers.md)), och allt ovan gäller: en Resonant Quantum Laser III ger en Resonant Starfire-III med samma bonusar, du väljer exemplaret, kortet frågar innan det använder ett över Standard, och Quantum Laser III måste ligga löst: ta av den i hangaren först, och knappen Montera säger ”Ta ut Quantum Laser III först” tills du gjort det. Nivån går sedan vidare uppåt: en Resonant Starfire-III ger en Resonant Helios Beam.

- **Helios Beam är också en uppgradering.** Den tillverkas av en **Starfire-III** (med 2 000 Thulium, byte, 18 Orvium Reinforced Plates, 4 Dark Matter Plates och en Ancient Control Unit: se [Lasrar](/wiki/06-Items/Lasers.md)), och allt ovan gäller: en Resonant Starfire-III ger en Resonant Helios Beam med Starfire-III:s bonusar, du väljer exemplaret, kortet frågar innan det använder ett över Standard, och Starfire-III måste ligga löst. En laser är monterad på ett skepp och bär förstärkare, så den är ofta inte det: ta av den i hangaren först (dess förstärkare går tillbaka till ditt inventarie), och knappen Montera säger ”Ta ut Starfire-III först” tills du gjort det.

Recepten, deras kostnader och siffrorna bakom regeln finns i [Översikt över föremål](/wiki/06-Items/Overview.md#upgrading-modules) och, för Quantum Laser III, Starfire-III och Helios Beam, på sidan [Lasrar](/wiki/06-Items/Lasers.md).

## Gamla servrar {#old-servers}

En spelserver som inte har uppdaterats till Smedjan visar ”Smedjan finns inte på den här servern än” i stället för fliken; Tillverkning fungerar som förut. En spelklient från före Smedjan visar den gamla Fusion-fliken på en uppdaterad server och uppmanas att uppdatera. En server från före 0.5.7 har inget block Socklar, och ett spel från före 0.5.7 kan fortfarande öppna Smedjan och läsa den, men en uppdaterad server avvisar varje ändring det ber om (en nivåhöjning, en sammanslagning, en stämning, en omläggning, en reparation, ett Tinkerer's Badge) med ”Uppdatera spelet för att använda den här funktionen.”
