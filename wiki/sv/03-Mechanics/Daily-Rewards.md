<!-- wiki-i18n source: c6cf04f6e8e99425 -->
<!-- wiki-i18n title: Dagliga belöningar -->
# Dagliga belöningar {#daily-rewards}

<!-- wiki-search: daily reward; daily rewards; daily login; login bonus; login reward; calendar; advent calendar; chest; chests; season prize; souvenir; blueprint; streak; daglig belöning; dagliga belöningar; daglig inloggning; kalender; adventskalender; kista; säsongsbelöning; säsongsminne; ritning; svit -->

Varje säsong har en **kalender med dagliga belöningar**: en liten present för varje dag i säsongen. Tryck på **Hämta** vid stationen, så är dagens present din. Ju fler dagar du hämtar, desto mer får du: fyra **kistor** kommer vid 7, 14, 21 och 28 hämtade dagar, och under säsongens sista tre dagar kan du ta **säsongsbelöningen**. En missad dag kostar dig den dagens present och inget mer. Du hittar kalendern på **Översikt** (kortet **Dagliga belöningar**) och under **Säsong och profil › Kalender**.

## På en minut {#in-one-minute}

- **29 rutor.** En för varje UTC-dag i säsongen. En säsong har 30 dagar, men dag 30 är [wipens](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule) nedräkning på 5 minuter, så då finns inget att hämta.
- **Du trycker på Hämta.** Ett tryck hämtar en ruta, en gång per pilot. Inget hämtas åt dig.
- **6 timmars respit.** En ruta förblir öppen i 6 timmar efter att dess dag har tagit slut.
- **Ingen svit.** En missad dag förlorar bara den dagens ruta och inget mer. Det som räknas är hur många dagar du har hämtat, inte om de kom i rad.
- **4 kistor**, vid 7, 14, 21 och 28 hämtade dagar.
- **En säsongsbelöning** under säsongens sista tre dagar: ett minnesutseende vid 10 hämtade dagar och en ritning till en skeppsdesign vid 20.
- **En ny kalender vid varje wipe.** Du ser varje present i säsongen från dag 1.
- **Litet med flit.** Alla 29 dagarna tillsammans är värda ungefär några timmars jakt, utspridda över en säsong.

## Dagen {#the-day}

Kalenderns dag är en **UTC-dag**: den byts vid **00:00 UTC**, för alla piloter i samma ögonblick, och den räknas på samma sätt som klanernas dagliga linje (»Dag *n* av 29«, se [Klaner](/wiki/03-Mechanics/Clans.md#the-day)). Den följer inte din tidszon, och den är inte säsongsdagen på säsongssidan, som byts vid den tid på dygnet då säsongen började. Serverns klocka avgör allt: klockan i din dator ändrar ingenting.

Kortet och fliken säger båda när nästa belöning öppnas **i din egen tidszon** (»Nya belöningar öppnas kl. 02:00 i din tid (00:00 UTC)«). Vill du räkna ut det själv, omvandla 00:00 UTC. Några exempel:

| Var | UTC-midnatt är klockan |
| :--- | :--- |
| Centraleuropa | 01:00 (vinter) eller 02:00 (sommar) |
| Moskva, Istanbul | 03:00 |
| Japan, Korea | 09:00 |
| USA:s östkust | 19:00 (vinter) eller 20:00 (sommar) |
| USA:s västkust | 16:00 (vinter) eller 17:00 (sommar) |

- **Dag 1 är kort.** Säsongen börjar med wipen, mitt i en UTC-dag, så ruta 1 är öppen från då till slutet av den dagen, plus respiten.
- **Dag 29 är lång.** Den sista rutan förblir öppen tills wipens nedräkning startar, och det kan vara mer än 24 timmar efter att den öppnades. När nedräkningen har startat går inget att hämta förrän den nya säsongen börjar.
- **Administratörer kan flytta säsongsdagen.** Kalendern följer med: dagar som hoppas över räknas som missade för alla, och en ruta som du redan har hämtat förblir hämtad.

## Rutorna {#the-tiles}

Fliken Kalender visar ett rutnät med en ruta för varje dag: dagens nummer, presenten och ett tillstånd i ord. Varje present i säsongen syns från första dagen, så du ser vad som väntar. Den räknar också dina dagar (till exempel »11 av 29 dagar hämtade«) och säger när nästa kista kommer. Kortet på Översikt visar dagens present och en enda knapp **Hämta**.

| Tillstånd | Vad det betyder |
| :--- | :--- |
| **Idag** | Öppen nu. Tryck på **Hämta**. |
| **Hämtad** | Du har den. |
| **Igår** | Gårdagens ruta, fortfarande öppen under respiten. Den visar hur lång tid som är kvar och har en egen knapp **Hämta**. |
| **Missad** | Dagen och dess respit är över. Presenten är borta, och inget annat har ändrats. |
| **Öppnas om …** | En kommande dag. Du ser presenten men kan inte hämta den än. |
| **Innan du började** | En dag före din första inloggning. Den går inte att hämta. |

Medan en belöning väntar visas en liten **(!)** vid **Säsong och profil** i sidofältet och vid **Tillbaka till basen** under flygning, och ett meddelande vid inloggningen talar om det (en gång per dag och dator).

## Respit och missade dagar {#grace-and-missed-days}

En ruta stängs inte vid midnatt: den förblir öppen i **6 timmar** efter att dess UTC-dag har tagit slut. Under de 6 timmarna är två rutor öppna, gårdagens och dagens, och du hämtar var och en med ett eget tryck. Efter respiten är gårdagens ruta **Missad** för gott, och längre bakåt kommer du inte.

En missad dag kostar dig **den dagens present och inget mer**. Det finns ingen svit som kan brytas: ditt antal hämtade dagar, dina kistor och säsongsbelöningen fortsätter som förut. En ruta som du hämtar under respiten räknas precis som en som hämtades i tid.

## Kistor {#chests}

En kista kommer med det **Hämta** som gör att ditt antal hämtade dagar når ett visst tal, och inte förr: det finns inget att trycka på och ingen nyckel att hitta. Det är antalet som räknas, inte datumet: kistan vid 7 dagar kommer med din 7:e hämtade dag, vilken dag i säsongen det än är.

| Kista | Kommer vid |
| :---: | :--- |
| **1:a** | 7 hämtade dagar |
| **2:a** | 14 hämtade dagar |
| **3:e** | 21 hämtade dagar |
| **4:e** | 28 hämtade dagar |

Varje kista innehåller en **Specimen Vault**, containern som rymmer lite av varje. De senare kistorna kan lägga till en liten extra som wipen inte tar. Fliken Kalender visar vad varje kista innehåller. En container är bara din, och du öppnar den på sidan Containrar. En container som du inte har öppnat ligger kvar på ditt konto även genom [wipen](/wiki/03-Mechanics/Wipe-Timeline.md).

Kan spelet inte lämna ut containern, till exempel för att containrar inte är påslagna, betalar kistan i stället ut ett **paket** av krediter, Thulium och en booster av ungefär samma värde. En kista går aldrig förlorad, och du får aldrig båda.

## Säsongsbelöning {#season-prize}

Säsongsbelöningen har två steg. Du hämtar dem under säsongens **sista tre dagar** (dag 27 till 29), tills wipens nedräkning startar. Före dag 27 står det **Öppnas de tre sista dagarna** på fliken, även om du redan har dagarna. Varje steg hämtas en gång, i valfri ordning.

| Steg | Kräver | Pris |
| :---: | :--- | :--- |
| **1** | 10 hämtade dagar | Ett **säsongsminne**: ett utseende |
| **2** | 20 hämtade dagar | En **designritning**: tekniken för en skeppsdesign |

- **Minnet** är en skin, en färg, ett avgasspår eller en aura ([Kosmetik](/wiki/06-Items/Cosmetics.md)), vald för säsongen ur en kort lista med utseenden som är avsatta för det och aldrig över Episk. Som alla utseenden är det bara för syns skull, hör till ditt konto och finns kvar efter wipen. Har du det redan får du nästa minne som du saknar. Har du alla får du 250 Thulium.
- **Ritningen** är forskningen av en skeppsdesign, gjord åt dig: designens teknik och de tekniker den kräver. Att bygga om ett skepp till designen görs fortfarande i Monteringen och kostar fortfarande det som [Skeppsdesigner](/wiki/03-Mechanics/Ship-Designs.md#getting-a-design) säger. En säsongs design är en av de 13, tagna i en fast ordning, så en design kommer inte tillbaka på 13 säsonger. Känner du den redan får du nästa design som du saknar. Känner du alla 13 får du 4 Dark Matter Plate, som är föremål: lägg dem i Transportförrådet före wipen.

## Presenterna {#the-gifts}

Dagens present är liten. Det är en av dessa:

- **Ammunition och raketer**, i måttliga staplar.
- **Material, plåtar och förbrukningsvaror**, bland dem Forge kits (materialen till ett steg i Smedjan).
- **Boosters** på några timmar. En booster-present lägger sina timmar till dina [boosters](/wiki/06-Items/Boosters.md#active-boosters).
- **Krediter och Thulium**, i små mängder.
- **Några få specialföremål** (Workforce Contract, Forger's Seal): aldrig fler än 4 rutor i en säsong.

Den här sidan nämner ingen present från någon säsong, eftersom kalendern är olika vid varje wipe. Fliken Kalender visar den här säsongens presenter. En present är en present: föremål från kalendern har ingen **Säljbar**-märkning ([Säljbara föremål](/wiki/03-Mechanics/Inventory.md#marketable-items)) och kan inte läggas ut på [Auktionen](/wiki/03-Mechanics/Auction.md).

## Wipen {#the-wipe}

En ny säsong är en ny kalender. Vid [wipen](/wiki/03-Mechanics/Wipe-Timeline.md) stängs den gamla och den nya öppnas med sina egna 29 presenter, och ditt antal börjar om på 0. Wipen tar inget av det du har hämtat, utom det den tar från alla föremål:

- **Raderas:** presenter som är föremål (ammunition, raketer, material, plåtar, förbrukningsvaror) raderas av wipen om de inte ligger i ditt [Transportförråd](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-). Kalendern märker en sådan present med en anteckning.
- **Behålls:** boosters, krediter, Thulium, specialföremål, utseenden, tekniker (en ritning) och containrar.
- **De sista fyra dagarna (26 till 29) ger bara presenter som behålls**, så en present från sista veckan går aldrig förlorad i wipen.

## Sena spelare och sena kalendrar {#late-joiners-and-late-calendars}

**Om du kommer in mitt i en säsong** visar rutorna före din första inloggning **Innan du började** och går inte att hämta. Kistorna och säsongsbelöningen kräver lika många dagar av alla, så en pilot som kommer sent når färre av dem. En pilot som loggar in första gången dag 16 har 14 rutor kvar, så 14 dagar är det mesta som går att hämta: de första två kistorna och steg 1 av säsongsbelöningen är inom räckhåll, steg 2 (20 dagar) är det inte.

**En kalender kan också starta sent.** Vanligtvis öppnas den med säsongen. Den kan öppnas senare, till exempel när spelet får Dagliga belöningar mitt i en säsong. En sådan kalender har bara de dagar som är kvar, och allt skalas med: en som öppnas dag 14 har 16 rutor (»av 16«), kistor vid 4, 8, 12 och 15 hämtade dagar och steg i säsongsbelöningen vid 6 och 11. Kortet på Översikt säger vilken dag den öppnades. Är färre än 10 dagar kvar får den pågående säsongen ingen kalender alls (**Det finns ingen kalender den här säsongen**), och nästa börjar med wipen.

## Frågor {#questions}

- **Varför kan jag inte hämta dag N?** Det finns fyra skäl. Dagen har inte kommit än (**Öppnas om …**). Dagen och dess respit är över (**Missad**). Dagen låg före din första inloggning (**Innan du började**). Eller wipens nedräkning har startat. En säsong utan kalender, eller en avstängd kalender, har inget att hämta.
- **Följer den min tidszon?** Nej. Dagen är en UTC-dag. Bara de klockslag som visas omvandlas till din tidszon ([Dagen](#the-day)).
- **Vad händer om servern låg nere?** De 6 timmarnas respit täcker ett kort avbrott runt midnatt. Vid ett längre kan en administratör hålla en dag öppen längre för alla. Dess ruta visas då som **Igår** med en egen nedräkning.
- **Kan jag hämta två dagar på en gång?** Bara medan två rutor är öppna, under de 6 timmarna efter en UTC-midnatt: gårdagens och dagens, ett tryck var. En ruta går inte att hämta två gånger eller i förväg.
- **Måste jag logga in varje dag?** Nej. Det finns ingen svit: en dag du hoppar över kostar dig den dagens present, och kistorna och säsongsbelöningen räknar bara hur många dagar du har hämtat.
- **Ändrar Premium något?** Nej. Premium ger inga extra rutor och inga bättre presenter, och kalendern ger inga Premium-dagar.
- **Behöver jag en klan?** Nej. Kalendern använder samma dag som klanernas dagliga linje, men den är bara din.
- **Finns det en nivågräns?** Nej. Varje pilot kan hämta, från nivå 1.
- **Vad händer vid wipen?** Du får en ny kalender och börjar om på 0 dagar. Presenter som är föremål raderas om de inte ligger i Transportförrådet; resten behålls ([Wipen](#the-wipe)).

## Bra att veta {#good-to-know}

- Presenterna, siffrorna och respiten bestäms på spelservern och kan ändras med en uppdatering; fliken Kalender visar alltid de som gäller.
- En spelserver från före Dagliga belöningar har ingen kalender, och kortet och fliken förblir dolda. En administratör kan också stänga av kalendern; det du har hämtat förblir hämtat.
- Varje ny kalender görs i förväg före wipen, så att spelets administratörer kan titta på den innan den startar och byta ut en present som är fel.
