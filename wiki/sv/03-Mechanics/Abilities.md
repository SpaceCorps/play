<!-- wiki-i18n source: 46f445f1a971775a -->
<!-- wiki-i18n title: Förmågor -->
# Skeppets aktiva förmågor {#active-ship-abilities}

Förmågor är knapparna du trycker på i stridens hetta: en sköld som kommer tillbaka, ett fartutbrott för att ta dig ur räckvidd, en reparation när skrovet nästan är borta. De kommer från den **sköld, motor eller Repair Drone** du monterar i ditt skepps **förmågeplatser**, och ju bättre föremålet är, desto bättre blir förmågan. De är gjorda för stunden då du behöver dem, inte för att tryckas på vid varje återhämtning: var och en varar ungefär tio sekunder och vilar sedan i en och en halv till två minuter.

En ny pilot börjar med en: **Repair Drone I** i startpaketet sitter redan i Protos förmågeplats, så knappen för Emergency Repair (`E`) finns där från första minuten.

## Förmågeplatser {#ability-slots}

Varje skepp har ett fast antal förmågeplatser i hangaren:

- **Protos** (startskepp): 1 plats
- **Kitefin**: 1 plats
- **Ostirion**: 2 platser
- **Nomad**: 2 platser
- **Paragon**: 3 platser
- **Storm**: 3 platser
- **Ironclad**: 3 platser
- **Wraith**: 3 platser

En förmågeplats tar en **sköld**, en **motor** eller en **Repair Drone**, och var och en ger sin egen förmåga. Dra föremålet till platsen. Konfiguration 1 och konfiguration 2 har sina egna platser.

- **Sköldceller och styrraketer passar inte i en förmågeplats.** De är moduler för sköldar, motorer och adaptiva kärnor.
- **Ett föremål i en förmågeplats tillför inget annat.** Det ger ingen sköldkapacitet, laddning, absorption eller fart, och inte heller den fartminskning en sköld ger. Samma Heavy Shield Core sitter antingen i en generatorplats för sin sköld hela tiden, eller i en förmågeplats för sin Surge. Du väljer.
- En sköld eller motor som rymmer celler eller styrraketer ger tillbaka dem till ditt inventarie när du drar den till en förmågeplats.
- En Repair Drone i en förmågeplats ger Emergency Repair och reparerar inte skrovet av sig själv. Den långsamma drönaren (**REP**) kräver en Repair Drone i en extraplats.

## Flera moduler av ett slag {#several-modules-of-one-kind}

Du kan montera **flera sköldar, motorer eller Repair Drones** i förmågeplatserna i en konfiguration. De är fortfarande en förmåga, en knapp och en återhämtning, men en starkare:

- **Den lägst rankade modulen sätter basen.** Dess rang ger styrkan och återhämtningen. En Heavy Shield Core bredvid en Light Shield Core fungerar som två moduler av rang I: en bättre andra modul ger bonusen och aldrig en bättre styrka eller en kortare återhämtning.
- **Varje övrig modul lägger till 50 % av basen**, summerat, inte multiplicerat. Motorer gör att Afterburner **varar längre**: 10 s, 15 s med två motorer, 20 s med tre (fartbonusen och återhämtningen ändras inte). Sköldar gör att Shield Surge **återställer mer**, och Repair Drones gör att Emergency Repair **läker mer**, under samma tio sekunder: 100 %, 150 % och 200 % av totalen för en, två och tre moduler.
- **De extra modulerna kostar platser.** Ett skepp med tre förmågeplatser kan ha tre av ett slag, eller en av varje, eller två och en. En Protos eller en Kitefin har en enda plats och kan inte stapla; en Ostirion eller en Nomad kan ha två av ett slag.
- Lika rang är helt enkelt den rangen. Av två moduler av samma rang sätter den med den svagare förtrollningen basen.

## De tre förmågorna {#the-three-abilities}

### Shield Surge (sköldar), tangent `Q` {#shield-surge-shields-key-q}

Under tio sekunder **repareras** ditt skepps sköld: Surge återställer en andel av din max. sköld jämnt fördelat, upp till max och aldrig över. Det är ingen barriär och ändrar inte hur träffar fördelas; den lägger tillbaka sköld, och det den lade tillbaka stannar kvar. Den avbryts inte när du träffas (den vanliga laddningen väntar 15 sekunder efter en träff; Surge gör det inte). Ett skepp med full sköld har inte mycket nytta av den, så tryck på den när skölden är på väg att ta slut. Totalen är aldrig mindre än sköldkärnans egen kapacitet, så ett skepp med lite sköld får ändå en riktig reparation (upp till sitt max).

- Går inte att använda inom en säker zons skydd, och inte på ett skepp utan någon sköld alls, så att ett felklick inte förbrukar den.
- Genomträngande raketer går fortfarande delvis förbi sköldarna, som de alltid gjort.

### Afterburner (motorer), tangent `W` {#afterburner-engines-key-w}

Din slutliga fart multipliceras med rangens bonus under dess varaktighet. Den ändrar inte svängning, siktning eller skada du tar: den gör tid till sträcka. Använd den för att lämna en strid, för att nå en stations eller portals ring, eller för att komma ikapp ett mål som flyr. Den fungerar överallt, säkra zoner inräknade. Fler motorer gör att den varar längre, inte snabbare.

### Emergency Repair (Repair Drones), tangent `E` {#emergency-repair-repair-drones-key-e}

Läker en andel av ditt **max. skrov jämnt fördelat över tio sekunder**, aldrig över max. Träffar avbryter den inte: det är en nödförmåga, och den fungerar under eld, i det svarta hålets strålning, under kamouflage och inom ett EMP-fönster. Den tar slut när tiden är ute eller när ditt skepp förstörs. Den rör inte din sköld, räknas inte som en träff och lämnar den långsamma REP-reparationen som den var. Går inte att använda vid fullt skrov.

## Rangerna {#ranks}

En förmågas styrka är en **andel av ditt eget skepps värde** (max. sköld, fart, max. skrov), så den växer med skeppet. Rangen kommer från föremålet: en bättre modell ger en bättre förmåga. Ett förtrollat föremål lägger sin förtrollningsbonus till styrkan, högst 15 %. Tabellen gäller en modul; staplingen står under den.

<!-- abilities:begin -->
<!-- Generated from server/Resources/AbilityConfig.json and the items' stats by scripts/abilities-wiki.sh: don't edit by hand. -->

| Förmåga | Rang | Föremål | Styrka (en modul) | Varar | Återhämtning | Uppe |
| :--- | :---: | :--- | :--- | --: | --: | --: |
| **Shield Surge** | I | Light Shield Core | återställer 30 % av din max. sköld | 10 s | 120 s | 8,3 % |
| **Shield Surge** | II | Basic Shield Core | återställer 60 % av din max. sköld | 10 s | 105 s | 9,5 % |
| **Shield Surge** | III | Heavy Shield Core | återställer 100 % av din max. sköld | 10 s | 90 s | 11,1 % |
| **Afterburner** | I | Engine I | +30 % fart | 10 s | 120 s | 8,3 % |
| **Afterburner** | II | Engine II | +45 % fart | 10 s | 105 s | 9,5 % |
| **Afterburner** | III | Engine III | +60 % fart | 10 s | 90 s | 11,1 % |
| **Emergency Repair** | I | Repair Drone I | läker 20 % av ditt max. skrov | 10 s | 120 s | 8,3 % |
| **Emergency Repair** | II | Repair Drone II | läker 25 % av ditt max. skrov | 10 s | 105 s | 9,5 % |
| **Emergency Repair** | III | Repair Drone III | läker 32 % av ditt max. skrov | 10 s | 90 s | 11,1 % |
| **Emergency Repair** | IV | Repair Drone IV | läker 40 % av ditt max. skrov | 10 s | 75 s | 13,3 % |

Flera moduler av ett slag i en konfiguration: den lägst rankade sätter styrkan och återhämtningen ovan, och varje övrig lägger till 50 % av den.

| Moduler av ett slag | Afterburner varar | Shield Surge återställer | Emergency Repair läker |
| :---: | --: | --: | --: |
| 1 | 10 s | 100 % | 100 % |
| 2 | 15 s | 150 % | 150 % |
| 3 | 20 s | 200 % | 200 % |

<!-- abilities:end -->

Sköldar och motorer av rang III (Heavy Shield Core, Engine III) säljs inte: du tillverkar dem i [Monteringen](/wiki/06-Items/Overview.md#upgrading-modules) av en Basic Shield Core och en Engine II, med Thulium, det utomjordingarna släpper och Velkonite Reinforced Plates från smedjan i din [Skylab](/wiki/03-Mechanics/Skylab.md). Emergency Repair har en fjärde rang, Repair Drone IV.

## Återhämtning och gränser {#cooldowns-and-limits}

- **Återhämtningen börjar när du trycker** på förmågan och inkluderar dess varaktighet. En Surge på 10 sekunder med 90 sekunders återhämtning är alltså uppe högst 11 % av tiden, och otillgänglig i 80 sekunder efter att den har tagit slut. Flera moduler förkortar den inte (det är den lägst rankade modulens återhämtning som gäller); inte ens tre Afterburner är uppe mer än 22 % av tiden.
- **Återhämtningen tillhör dig, inte föremålet.** Att byta konfiguration, byta föremål, hoppa till en annan sektor och logga ut nollställer den inte. Ett skepp som förstörs börjar nästa flygning med alla förmågor redo.
- **Varje förmåga har sin egen återhämtning.** Att använda en låser inte de andra.
- **En pågående effekt behåller de värden den startade med.** Att ta av föremålet eller byta konfiguration ändrar eller avslutar den inte. Ett hopp eller en återanslutning avslutar den inte heller; att logga ut gör det, och dess återhämtning finns kvar.
- Andra piloter ser dina förmågors timers på kartan, som de alltid gjort: en förbrukad Surge talar om för dem att de närmaste minuterna är öppna.

## Tangenter och knappar {#keys-and-buttons}

`Q` Shield Surge, `W` Afterburner, `E` Emergency Repair (alla går att ändra i inställningarna). Varje knapp visas bredvid snabbfältet bara när din konfiguration har den förmågan, så en ny pilots `E` finns där från första minuten. Ringen runt ikonen visar var förmågan står: den är hel i förmågans färg när förmågan är redo, töms medan förmågan pågår, med sekunderna kvar (även för Emergency Repair, nu när den läker över tio sekunder), och fylls på igen medan den laddas om, med sekunderna kvar i mitten. En stapel med flera moduler bär sitt märke (`x2`, `x3`) i knappens hörn. Knappen för Emergency Repair är nedtonad medan ditt skrov är helt, och knappen för Shield Surge på ett skepp helt utan sköld. Håll pekaren över en knapp för siffrorna på ditt skepp, staplingen inräknad (till exempel *Afterburner II x2: +45 % fart i 15 s*), och, medan en Surge eller en reparation pågår, hur mycket den ger per sekund och hur mycket som återstår.

## I hangaren {#in-the-hangar}

Dra en sköld, en motor eller en Repair Drone till en förmågeplats, eller högerklicka på den i ditt inventarie för att sätta den i den första lediga. En andra och en tredje av samma slag hamnar i nästa lediga platser och staplas. Förmågans namn och rang står under varje fylld plats, med stapelmärket och siffrorna för alla dess moduler tillsammans (*Afterburner II x2*, *x2 · 15 s*; för en Repair Drone II på en Wraith *+81 000 skrov*), och att hålla pekaren över en plats visar vad den är värd på ditt skepp, staplingen inräknad, och vilken modul i staplingen som sätter rangen. Varje modul av ett slag visar samma förmåga, eftersom de är en. Att hålla pekaren över föremålet var som helst annars visar förmågan med andelarna av ditt eget skepp och en mening om vad ytterligare en modul ger.

## Vad alla ser {#what-everyone-sees}

En Shield Surge är en bubbla runt skeppet så länge den pågår, som flimrar de sista två sekunderna och dras ihop när den tar slut. Sköldstaplarna (din i fönstret Skepp, och ett måls i målfönstret) fylls helt enkelt på när Surge lägger tillbaka sköld, och staplen pulserar lätt så länge det finns plats för den. En Afterburner får motorerna att brinna hetare så länge den pågår, 10, 15 eller 20 sekunder, och skickar ut en ring från skeppet när den startar, bredare för en stapel. En Emergency Repair skickar ut en grön puls när den startar, lindar sedan under sina tio sekunder in skrovet i ett mjukt grönt sken med några plustecken som stiger från det, låter det skrov den läker varje sekund sväva upp över ditt eget skepp, och slutar med ett sista blixtljus. Medan den pågår cirklar små reparationsdrönare runt skeppet och lagar det: en för en Repair Drone I, två för en II, tre för en III eller IV, och en till för varje ytterligare Repair Drone i en stapel (aldrig fler än tre). De lämnar skrovet, riktar mjuka gröna strålar mot plåtar på det, skickar pulser längs strålarna från II och uppåt, och flyger tillbaka för att docka när de tio sekunderna är över; en Shield Surge har upp till två blå inne i sin bubbla. Varje pilot på kartan ser alla tre förmågorna, drönarna också (mindre på en annan pilots skepp, och färre på de lägre grafikinställningarna, där Låg visar strålar och sken utan drönarmodeller, och en stråle som är lite bredare för varje rang hos drönaren), så en förbrukad Surge är en signal till fienden lika mycket som till dig. Drönarna har tre egna, tysta ljud, långt tystare än reparationens klockljud: ett mjukt pip när de lämnar skrovet, ett när de dockar och en svag ton under strålarna medan de arbetar (en Surges drönare lite högre); du hör dem från skepp på din skärm, högst några åt gången, och volymen för Ljudeffekter dämpar dem. Med *Minska rörelser* på hålls skenet stadigt, plustecknen utelämnas, det sista blixtljuset är en toning och drönarna står parkerade bredvid skeppet med en stadig stråle (ljuden finns kvar).

## Vad som har ändrats {#what-changed}

Före uppdateringen 0.4.3 tog förmågeplatserna sköldceller (Sköldregen) och styrraketer (Fartökning). Sköldceller och styrraketer som satt i förmågeplatser gick tillbaka till ditt inventarie när spelet uppdaterades, och du behåller dem: de är fortfarande moduler för sköldar, motorer och adaptiva kärnor. Sedan dess ger Shield Surge inte längre en barriär av extra sköld utan reparerar din sköld över tio sekunder, Emergency Repair läker över tio sekunder i stället för på en gång, och du kan montera flera moduler av ett slag för en längre Afterburner, en större Surge eller en större reparation.
