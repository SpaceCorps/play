<!-- wiki-i18n source: b15e3e40418c232b -->
<!-- wiki-i18n title: Receptbok -->
# Receptbok och builds {#recipe-book-and-builds}

<!-- wiki-search: recipe; recipes; recipe book; bill; steps; chart; craft tree; what do i need; build; builds; loadout; preset; presets; import; export; json; my builds; share a build; recept; kostnad; steg; diagram; tillverka; utrustning; förinställning; importera; exportera; mina builds; dela en build -->

**Receptboken** svarar på ”vad krävs för det här?” för vilket föremål som helst i spelet: ett diagram över vad det är gjort av, stegen i ordning, hela kostnaden och var varje råvara kommer ifrån. **Builds** gör detsamma för ett helt skepp: importera utrustningen från ditt hangar eller en väns build, börja med en av de 15 förinställningarna eller gör en egen, och se dess värden och hela kostnaden, steg för steg. Båda finns i stationens **Bibliotek**, under Wikin.

Receptboken har ingen egen prislista: den räknar ut sina siffror medan du tittar, av de recept, priser, teknologier och droptabeller som Butiken, [Monteringen](/wiki/06-Items/Overview.md#upgrading-modules) och [Forskningen](/wiki/03-Mechanics/Research.md) använder, och följer därför spelet när ett pris eller ett recept ändras. Det är därför den här sidan inte anger något pris eller några värden: öppna föremålet eller builden.

## Öppna den {#open-it}

Öppna stationens meny och välj **Bibliotek › Receptbok** eller **Bibliotek › Builds**. Receptboken minns det föremål du senast tittade på, dess filter och dess zoom, men bara på den här datorn; dina builds ingår inte i det ([Sparade på ditt konto](#saved-on-your-account)). När spelet är nyare än servern det pratar med säger sidan det och visar mindre: Receptboken räknar fortfarande ut allt som köps, tillverkas eller uppgraderas, men kan inte säga var världen ger ett föremål (det står bara ”Skaffa”), och Builds nämner de delar som kräver den nyare servern: förinställningarna, Mina builds och värdena.

## Hitta ett föremål {#find-an-item}

Den stora listan till vänster innehåller alla föremål i spelet, grupperade efter typ och, inom en typ, i spelets egen ordning: den svagaste nivån först. Där finns också EMP Charge, den enda förbrukningsvaran.

- **Sök.** Börja skriva var som helst på sidan så hamnar texten i sökfältet. Listan blir en enda lista, rankad efter hur väl namnet stämmer (hela namnet, början av det, början av ett ord, någon del av det, sedan typen). Versaler och accenter spelar ingen roll, och det gamla namnet på ett omdöpt föremål hittar föremålet. `Esc` rensar sökningen.
- **Typ.** Rullgardinsmenyn ovanför listan snävar in den till en typ och visar hur många föremål varje typ har. Omkopplaren bredvid sorterar A–Z inom varje typ.
- **Rader.** En rad visar föremålets bild, namn, typ och sällsynthet, en liten symbol för den väg du vanligtvis skaffar det på (tillverkas i Monteringen, säljs i Butiken, droppas eller hittas, pressas eller framställs i det svarta hålet) och en bock när du har det.
- **Tangenter.** Piltangenterna, Page Up, Page Down, Home och End bläddrar i listan, och `Enter` flyttar till diagrammet. `Alt+Left` och `Alt+Right` går bakåt och framåt bland de föremål du har öppnat.

## Diagrammet {#the-chart}

Klicka på ett föremål så visar högersidan det. Överst finns dess bild, namn, sällsynthet och typ, och en chip för varje **väg** att skaffa det: **Tillverka** (i Monteringen, med tid och kostnad), **Köp** (i Butiken, med pris), **Pressa** (av malm, i Skylabs smedja), **Drop** (världen ger det: utomjordingar, klippor, belöningar) och **Framställ** ([Dark Matter](/wiki/03-Mechanics/Dark-Matter.md), av N.I.K.E. som skjuts in i det svarta hålet). Den fyllda chipen är den väg diagrammet och kostnaden följer; klicka på en annan chip för att följa den i stället. Om du inte har forskat fram det som låter dig tillverka föremålet står det på en rad vilken teknologi som krävs och hur länge den tar, med en knapp som öppnar Forskning.

**Diagrammet** ritar föremålet som ett träd från vänster till höger: föremålet till vänster, det det är gjort av till höger om det, ända ner till råvarorna.

- Varje ruta visar föremålet, hur många du behöver och en symbol för hur det skaffas (symbolen på chipet för den vägen ovanför; håll muspekaren över rutan för orden, så att färgen aldrig är det enda tecknet). Ett lås betyder att dess teknologi inte är framforskad än, och en grön bock med ett tal anger hur många du har.
- En ruta med grenar har ett litet handtag som viker ihop dem; de djupa grenarna i ett stort träd börjar hopvikta. **Fäll ut alla**, **Fäll ihop alla**, **Anpassa** och zoomknapparna finns ovanför diagrammet.
- Klicka på en ruta för att läsa dess kort under diagrammet: föremålet, vägarna att skaffa det (klicka på ett annat chip för att följa den vägen), vad vägen kräver (omgångarna, tiden och kostnaden för en tillverkning, eller priset i Butiken), hur många du har och, för en låst ruta, teknologin den behöver. Ett dubbelklick, eller `Enter`, öppnar det föremålet i Receptboken. Piltangenterna går från ruta till ruta, `Space` viker ihop eller fäller ut en gren och `0` anpassar diagrammet. Scrolla för att förflytta dig; `Ctrl` och hjulet zoomar.
- Ett föremål som bara köps eller hittas är en enda ruta som säger ”Inget att tillverka: det köps eller hittas. Se Källor.”

I ett brett fönster tar diagrammet vänstersidan och de andra panelerna står i en kolumn till höger om det; i ett smalt visar flikarna **Diagram**, **Steg**, **Kostnad**, **Källor** och **Används i** en panel i taget.

## Steg och kostnad {#steps-and-the-bill}

Under rubriken avgör tre reglage vad som räknas: **Hur många** exemplar du vill ha, **Räkna det jag äger** (på: det du redan har dras av) och **Ta med det som är monterat** (av: en del som sitter på ett skepp räknas inte, eftersom en uppgradering förbrukar en del och en monterad skulle lämna sin plats).

- **Steg** är diagrammet som en numrerad lista, i den ordning det ska göras, i grupper: Forskning, Skaffa, Köp, Pressa och tillverka samt Från ditt lager. Forskningen kommer först eftersom Monteringen inte tillverkar något innan dess teknologi är framforskad. Varje steg säger vad och hur många, vad det kostar och hur lång tid det tar, och ett Skaffa-steg kan visa var man skaffar det. **Kopiera stegen** kopierar listan som text.
- **Kostnad** räknar ihop allt: dina Credits och ditt Thulium mot det du har, varje råvara med kolumnerna **Behövs**, **Har** och **Saknas**, det Dark Matter som forskningen tar, tiden att tillverka och pressa, tiden att forska (en teknologi i taget) och ett **Värde**. Värdet är ett sätt att jämföra två vägar att skaffa ett föremål, där Thulium och sådant du måste hitta räknas i Credits: det är inget pris. **Kopiera kostnad** kopierar kostnaden som en tabell du kan klistra in i en chatt eller en anteckning.

## Källor och Används i {#sources-and-used-in}

- **Källor** säger var världen ger föremålet och varje råvara planen behöver, per slag: utomjordingar, asteroider och klippor, svärmar, Dormant Swamp, klanväktare, [Davidski](/wiki/03-Mechanics/Davidski.md), Skylab-expeditioner, jättegrävmaskinen, Skylab-produktion, uppdrag, Bjud in vänner och startpaketet. En rad nämner vem som ger det och var, chansen och hur många. ”Även hos” räknar upp [Auktionen](/wiki/03-Mechanics/Auction.md), Davidskis lager och andra piloter. En chans är en chans, inte en takt per timme: hur lång tid en nedskjutning tar beror på dig.
- **Används i** räknar upp de föremål som tillverkas av det här. Klicka på ett för att öppna det.

## Lägg till i build {#add-to-build}

Ett föremål som sitter i en plats eller som bärs med har en knapp **Lägg till i build**: skepp, skrovpansar, lasrar, laserförstärkare, sköldar, sköldceller, motorer, styrraketer, Adaptive Cores, extrautrustning, drönare, formationer, ammunition, raketer och EMP Charge. Den lägger föremålet i den build du redigerar i **Builds**, på första plats där det får plats (finns ingen skapas en ny build som heter ”Ny build”), och ett meddelande säger vart det tog vägen eller varför det inte fick plats (”Välj ett skepp först.”). Lägger du till ett skepp i en build som redan har ett ber den dig klicka igen för att byta ut det. EMP Charge bärs med, den monteras inte: den hamnar i buildens raketer.

## Builds

En **build** är utrustningen för ett skepp, skriven med föremålsnamn så att den betyder detsamma på varje server: skeppet, lasrarna med sina förstärkare, sköldarna, motorerna och Adaptive Cores med sina celler och styrraketer, extrautrustningen, delarna i förmågeplatserna, skrovpansaren, drönarna med det de bär, en formation samt ammunitionen och raketerna man tar med. Den har också ett namn, en anteckning, en fas (Tidig, Mitten eller Sen) och en typ.

Listan till vänster har **Förinställningar** per fas, **Mina builds**, **Ny build** och **Importera**; i ett smalt fönster är den en rad flikar. Välj en build så ser du dess bräde, dess värden och dess kostnad.

### Importera {#import}

**Importera** öppnar ett blad med tre dörrar:

- **Klistra in**: klistra in texten till en build, eller tryck på **Klistra in från urklipp**.
- **Från en fil**: build-filerna i mappen `exports` i spelets datamapp (`.spacecorps2027` i din hemmapp), samma mapp som **Spara till fil** skriver till.
- **Från mitt hangar**: välj ett av dina skepp och en konfiguration så läser spelet det som är monterat: lasrar och förstärkare, generatorer med sina celler och styrraketer, extrautrustning, förmågedelar, skrovpansar, drönare med det de bär och nivån på din Extra Slots CPU. Det erbjuder också formationen, ammunitionen och raketerna i ditt snabbfält; kryssa i de du vill ha.

Du ser vad som kommer in innan något sparas, och spelet säger exakt vad det inte kunde importera: ett föremål som inte finns i det här spelet, en del som inte hör hemma på sin plats, fler delar än skeppet har platser, en build gjord av ett nyare spel. **Importerad utan ändringar** betyder att allt kom in. Sedan **Spara i Mina builds**, **Öppna i redigeraren**, eller stäng bladet. Dina nivåer i [Smedjan](/wiki/06-Items/Forge.md), smedjebonusar, drönarnivåer, boosters, P.E.T., skeppets utseende och den andra konfigurationen i [hangaren](/wiki/03-Mechanics/Hangar.md) ingår inte i en build (importera den andra konfigurationen som en andra build).

### De 15 förinställningarna {#the-15-presets}

Femton builds är redo att användas: tre faser i spelet, **Tidig**, **Mitten** och **Sen**, med fem slag i varje. **Farmning** ger flest nedskjutningar för vad den kostar, **Försvar** har den största skölden och den snabbaste regenereringen, **Anfall** mest skada och genomträngning, **Situationsstyrd** väljer sina strider med osynlighet, hopp och fart, och **Tank** har skrov och sköld tillsammans högst. En förinställning kan inte ändras: **Redigera en kopia** öppnar den som ditt eget utkast, och **Lägg till i Mina builds** behåller den som den är. Varje rad visar dess Värde i några få tecken, uträknat av recepten medan du tittar; öppna en förinställning för dess värden och dess kostnad.

### Redigera {#edit}

En build ritas som ett hangar: lasrar, generatorer, extrautrustning, förmågor, pansar och drönare, sedan nivån på Extra Slots CPU, en formation och ammunitionen och raketerna man tar med. Klicka på en tom plats så visar en lista bara det som passar i den, med sitt pris eller vägen att skaffa det; klicka på en del för att **Byta ut** den, **Lägga till en modul** eller **Ta bort** den. En drönare bär en laser eller en sköldkärna. Byter du skepp stannar de delar som fortfarande passar, och resten räknas upp som borttaget. Ge builden ett namn, en fas, en typ och en anteckning, och välj sedan **Spara**, **Spara som kopia**, **Ta bort** eller **Stäng** (Stäng frågar först när ändringar inte är sparade).

### Värden {#stats}

Under brädet finns hangarens eget värdekort: träffpoäng, skada, räckvidd, kritisk chans, sköldar och deras återladdning, absorption, hastighet, sköld- och fartbonus, genomträngning och, på ett skepp med pansarplatser, det skrov som dess pansar lägger till. Kortet har inga rader för förmågor: delarna i förmågeplatserna finns på brädet. Servern räknar ut siffrorna med samma kod som ditt hangar, för en build som inte är monterad på något skepp. Två omkopplare ställer in den **Smedjenivå** och den **Drönarnivå** som siffrorna utgår från. En formation verkar under flygning, så den räknas upp som text och ingår inte i siffrorna, och det gör inte heller boosters eller dina egna smedjenivåer.

### Kostnad {#cost}

Kostnaden har fyra block:

- **Summor**: Credits, Thulium, Dark Matter, varje råvara med Behövs, Har och Saknas, tiderna och Värdet. **Du behöver fortfarande** är det som blir kvar när det du äger har dragits av.
- **Vart pengarna går**: varje del, den dyraste först.
- **Steg**: forskning, skaffa, köp, pressa och tillverka, i ordning, för hela builden. Klicka på ett Skaffa-steg för att se var världen ger det, eller öppna föremålet i Receptboken.
- **Innan du börjar**: det som inte är en del, som nivåerna på Extra Slots CPU, forskningen av pansarplatserna, de drönare du fortfarande måste köpa och den nivå på Skylab-kärnan som Smedjan kräver.

Tre omkopplare: **Dra av det jag har** (på), **Räkna med det som är monterat** (av) och **Räkna med ammunition och raketer** (av: de förbrukas om och om igen, så de är inte buildens pris).

## Sparade på ditt konto {#saved-on-your-account}

**Mina builds sparas på ditt konto**, på servern och inte på den här datorn, så de följer med dig till vilken dator som helst. Du kan ha upp till 50; listan visar hur många du har, och när den är full ber sidan dig ta bort en för att spara en ny. En build är sparad när servern säger det: sidan visar **Sparar...** medan den väntar, och om servern vägrar eller inte går att nå säger den varför och builden förblir osparad, med dina ändringar kvar i redigeraren. En sparad build är bara föremålsnamn, några etiketter och det namn och den anteckning du skrev, och ingen annan pilot kan se den. Vill du ge en till en vän, exportera den.

## Dela och exportera {#share-and-export}

**Exportera** på en build öppnar ett blad med builden som text (JSON). **Kopiera** den för att klistra in i en chatt, eller välj **Spara till fil**, som skriver `spacecorps-build-<name>.json` i mappen `exports` och aldrig skriver över en äldre fil. En vän klistrar in texten under **Importera › Klistra in**, eller lägger filen i sin egen `exports`-mapp och väljer den under **Från en fil**. Texten innehåller utrustningens föremålsnamn, skeppet samt buildens namn och anteckning, och inget från ditt konto.

## Tips

1. **Titta innan du farmar.** Öppna ett föremål i Receptboken och läs dess Källor och Steg innan du ägnar en dag åt en drop som inte är den du behöver.
2. **Räkna från noll.** Stäng av **Räkna det jag äger** (i Builds: **Dra av det jag har**) för att se vad ett föremål eller en build kostar från grunden; låt det vara på för att se vad du fortfarande behöver.
3. **Börja med en förinställning.** **Redigera en kopia**, byt ut en del, så följer värdena och kostnaden med.
4. **Läs träden också.** [Föremålsträden](/wiki/06-Items/Item-Trees.md) visar varje slags föremål sida vid sida, och Receptboken räknar ut priset på vilket som helst av dem åt dig.
