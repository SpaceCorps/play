<!-- wiki-i18n source: 1ad7127494a07e66 -->
<!-- wiki-i18n title: Svart hål -->
# Det svarta hålet {#the-black-hole}

<!-- wiki-search: black hole -->

Mitt i Farosektor 4 (`DS-4`, mitten av PvP-zonen) hänger ett svart hål i mörkret. Det är likadant i alla världar (Alpha, Beta och Gamma), varje dag under säsongen, Fredsprotokollet inräknat. Det tar det som kommer för nära, och det ger tillbaka en enda sak: [Dark Matter](#dark-matter), för en N.I.K.E.-raket som avfyras in i det. Hela vägen, från forskningen till plattan, finns i [Dark Matter och Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md).

![A Wraith approaches the black hole from 3,500 units: the radiation and pull rings lie around it like a gravity well](../../img/wiki-img/shots/black-hole-approach.jpg)
![Looking down on the black hole from 1,300 units: the shadow, the photon ring and the spiral of the accretion disk, with the starfield bent around it](../../img/wiki-img/shots/black-hole-closeup.jpg)

## Ringarna {#the-rings}

Avstånden räknas från sektorns mitt, i kartenheter. Sektorn är 32 000 gånger 18 000 enheter.

| Ring | Avstånd | Vad som händer |
| :--- | ---: | :--- |
| **Strålning** | 4 000 | Ditt skepp tar skada varje sekund, en andel av dess totala maximala HP. Ju närmare, desto mer. |
| **Dragning** | 3 000 | Det svarta hålet drar ditt skepp mot mitten, hårdare ju närmare du är. Ett skepp som inte flyger förs med. |
| **Punkt utan återvändo** | ungefär 1 000 till 2 600 | Där dragningen är lika stark som ditt skepps fart. Innanför den dras du in, även med full kraft. Den beror på din fart. |
| **Händelsehorisont** | 300 | Varje skepp som når den förstörs på stört, oavsett skrov och sköld. |

Farosektor 4:s portaler och lederna mellan dem ligger alla långt utanför strålningen, så du råkar aldrig in i den på vägen igenom.

## Strålning {#radiation}

Skadan är en **andel av ditt skepps totala maximala HP** (skrov plus sköld) varje sekund, så alla skeppsklasser håller precis lika länge på ett givet avstånd: en Protos och en Wraith på 2 000 enheter bränns båda genom ett helt skepp på 50 sekunder.

| Avstånd | Skada per sekund | Ett helt skepp håller i |
| ---: | ---: | ---: |
| 4 000 | 0,3 % | 333 s |
| 3 500 | 0,55 % | 182 s |
| 3 000 | 0,8 % | 125 s |
| 2 000 | 2 % | 50 s |
| 1 200 | 5 % | 20 s |
| 700 | 11 % | 9 s |
| 300 | 24 % | 4 s |

Mellan två rader ökar skadan längs en rät linje. I träffpoäng per sekund, för grundutrustningarna:

| Skepp | Totalt max. HP | Vid 3 500 | Vid 3 000 | Vid 2 000 | Vid 1 200 | Vid 700 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Protos | 30 000 | 165 | 240 | 600 | 1 500 | 3 300 |
| Kitefin | 46 000 | 253 | 368 | 920 | 2 300 | 5 060 |
| Ostirion | 82 500 | 454 | 660 | 1 650 | 4 125 | 9 075 |
| Nomad | 130 500 | 718 | 1 044 | 2 610 | 6 525 | 14 355 |
| Paragon | 162 500 | 894 | 1 300 | 3 250 | 8 125 | 17 875 |
| Storm | 198 000 | 1 089 | 1 584 | 3 960 | 9 900 | 21 780 |
| Wraith | 372 000 | 2 046 | 2 976 | 7 440 | 18 600 | 40 920 |
| Ironclad | 673 200 | 3 703 | 5 386 | 13 464 | 33 660 | 74 052 |

- **Skölden tar skadan först**, sedan skrovet. Det är ingen träff: sköldens absorption kommer inte in i bilden, och strålningen går inte att väja undan.
- Strålning räknas som **skada du tar**: din sköld laddas inte om, en Repair Drone stannar (”Reparationer avbrutna: strålning.”) och går inte att starta, och en säker zon skyddar dig inte förrän 5 sekunder efter den sista dosen.
- Boosters och uppgraderingar ändrar hur stor din totalsumma är, inte hur länge du håller: skadan är en andel av den.
- Inget gör ett skepp immunt. Strålning är ingen träff, så ingenting suger upp den; men förmågorna fortsätter att fungera i den: en Shield Surge fortsätter att återställa din sköld och en Emergency Repair fortsätter att läka ditt skrov under sina tio sekunder (de är inte de naturliga reparationer som dosen stoppar). Kamouflage döljer inte skeppet för den.

## Dragningen {#the-pull}

Innanför 3 000 enheter drar det svarta hålet varje skepp mot mitten, och dragningen blir bara starkare ju närmare du kommer. Den börjar milt vid kanten och märks redan 200 enheter in:

| Avstånd | Dragning (enheter per sekund) | Ett skepp som inte flyger förs med |
| ---: | ---: | :--- |
| 3 000 | 0 | inget än |
| 2 800 | 25 | 25 enheter på en sekund |
| 2 300 | 60 | 60 enheter på en sekund |
| 1 800 | 120 | 120 enheter på en sekund |
| 1 300 | 220 | 220 enheter på en sekund |
| 1 000 | 262 | 262 enheter på en sekund, och ökar |
| 900 | 289 | 289 enheter på en sekund, och ökar snabbt |
| 700 | 496 | till horisonten på ungefär en sekund |
| 300 | 2 829 | händelsehorisonten |

Från 3 000 ner till 925 enheter ökar dragningen längs en rät linje mellan två rader; innanför 925 följer den en brantare kurva (de tre sista raderna ligger på den). Det är en ström: den för ditt skepp med sig, och dina motorer kämpar emot.

- **Ett skepp som inte flyger kan inte hålla sig stilla.** Om du stannar (du når platsen du klickade på, eller du gav aldrig någon order) bär det svarta hålet ditt skepp mot mitten och din order följer med, så ditt skepp fortsätter att falla hur snabbt dess motorer än skulle kunna flyga. För att hålla en plats måste du fortsätta flyga dit: håll musen på den, så håller sig ditt skepp kvar där dess fart är högre än dragningen, och sjunker en aning tillbaka mellan två order. Två skepp som stannar för att byta eld innanför dragningen förs båda in.
- **Ett skepp som flyger möter motvind.** När du flyger rakt bort från mitten dras ditt skepps fart ner av dragningen där du är: med fart 155 klarar du 130 enheter i sekunden vid 2 800, 95 vid 2 300 och 35 vid 1 800, och vid 1 500 (en dragning på 180) kommer du ingenstans alls.

Din **punkt utan återvändo** är avståndet där dragningen är lika stark som din fart. Ett skepp med fart 150 har den vid 1 650 enheter; ju snabbare du är, desto djupare ligger den:

| Skepp (grundutrustning) | Fart | Punkt utan återvändo |
| :--- | ---: | ---: |
| Ironclad | 99 | 1 974 |
| Protos | 165 | 1 577 |
| Kitefin | 184 | 1 480 |
| Ostirion | 208 | 1 362 |
| Nomad | 211 | 1 347 |
| Paragon | 222 | 1 287 |
| Wraith | 233 | 1 208 |
| Storm | 263 | 995 |

Ett skepp som är snabbare än 272 enheter i sekunden (en utrustning byggd för fart, eller en Wraith med grundutrustning och en pågående Afterburner) har sin punkt utan återvändo kvar där den alltid låg: vid fart 300 är den 885, vid 432 är den 747.

Bygg för fart så kan du ta dig ut från djupare; lasta på tunga sköldar så kan du inte (en Ironclad, det långsammaste skeppet, med en Heavy Shield Core i alla sina 14 platser flyger med fart 39,1, med punkten utan återvändo vid ungefär 2 600). Bara ett fartutbrott kan vända ett skepp som just kommit innanför sin punkt utan återvändo: en pågående [Afterburner](/wiki/03-Mechanics/Abilities.md) räknas, och flyttar punkten utan återvändo djupare så länge den varar (tio sekunder med en motor, femton med två, tjugo med tre; Afterburner III flyttar punkten för en Protos med grundutrustning från 1 577 till 989 och för en Wraith med grundutrustning från 1 208 till 801). Ingenting tar sig ut inifrån ungefär 390 enheter, inte ens ett skepp byggt för fart med varje fartvärde förtrollat till max och det starkaste fartutbrottet igång (en Afterburner III förtrollad till taket, x1,69); ett oförtrollat skepp byggt för fart (Engine III med en Impulse Thruster IV och två Momentum Thruster IV, Adaptive Core II med två Impulse Thruster IV), med en Afterburner III, tar sig i bästa fall ut från utanför 427.

Fallet från punkten utan återvändo börjar långsamt: ett skepp som ligger några enheter innanför den dras in på tjugo sekunder eller mer, även med full kraft, och sedan allt snabbare. Dragningen är ingen flygning: den räknas inte som flugen sträcka.

## Händelsehorisonten {#the-event-horizon}

Ett skepp som når 300 enheter från mitten förstörs. Ett skepp vars skrov tar slut under strålningen på vägen dit förstörs i stället av strålningen. Hur som helst:

- Det är en vanlig förstörelse: du väljer var du återvänder (se [Förstörelse och återkomst](/wiki/01-General/Getting-Started.md)), med högst 10 000 skrov och tom sköld (se den sidan), och den kostar det en förstörelse alltid kostar. ”På platsen” sätter dig aldrig tillbaka innanför ringen: det flyttar dig till närmaste punkt utanför den (4 500 enheter från mitten) och talar om det för dig.
- **Inget vrak, ingen låda, inget byte**, och ingen heder går förlorad.
- Din förstörelse räknas som en PvP-nedskjutning för den **sista fientliga pilot som träffade ditt skepp under de 15 sekunderna innan det förstördes**: en pilot från en annan koncern (där och när PvP är tillåtet), hur liten träffen än var. Det är en nedskjutning i dennes statistik och ger PvP-rankingpoäng efter din skeppstyp, inget mer. Ett enda skott räcker, och om ingen från en annan koncern träffade dig under de 15 sekunderna får ingen något.
- Koncernkamrater som träffade ditt skepp under de 15 sekunderna förlorar ändå hedern för vådaeld, vad som än förstörde det.
- Utomjordingar och koncernpiloter går aldrig i närheten av det. Om en ändå hamnar innanför försvinner den utan byte, belöning eller pax.

## Vad du ser och hör {#what-you-see-and-hear}

Vyn är liten (ungefär 1 900 gånger 1 150 enheter på skärmen med standardzoomen, 4 400 gånger 2 650 helt utzoomad), så det svarta hålets egen bild syns bara inom ungefär tretusen enheter från det (3 600 helt utzoomad). Från längre bort pekar ingenting på skärmen ut det (titta på minikartan eller kartan Stjärnsystem, nedan); varningen i gränssnittet är till för när du är nära:

- **Från långt håll.** Om du vinklar kameran nedåt för att titta längs planet ritas det svarta hålet ut där det ligger på skärmen, från var som helst i sektorn, så fort det är i bild: en svart skiva med en ring i ett sken av ackretionsljus, skalad så att den förblir lätt att se (ungefär 2 % av vyns höjd från det bortre hörnet, som ligger ungefär 18 000 enheter bort), och den växer till sin egen bild när du kommer närmare. Ingenting i den rör sig av sig själv. När det svarta hålet är utanför bild finns ingen markör för det på skärmen.
- **Ringar på flygplanet.** Ett violett band glöder upp mot en skarp kant vid strålningens rand (4 000 enheter), och ett tunnare bärnstensfärgat markerar dragningens kant (3 000). Innanför dragningen visar en **röd linje** *din egen* punkt utan återvändo. Den följer din fart, så den flyttar sig när ditt skepp blir snabbare eller långsammare.
- **Mätaren**, ovanför snabbfältet, visas inom tusen enheter från randen och finns kvar medan du bränns. Den visar strålningen i procent av ditt skepps totala HP per sekund, hur lång tid strålningen ensam skulle behöva för att bränna genom det som är kvar (”Dödligt om 31 s”, rött under tio), en stapel för den HP:n, dragningen där du är mot din fart, och avståndet som återstår att flyga till din punkt utan återvändo, eller en blinkande varning när du är förbi den. Håll pekaren över en rad för att se vad den betyder; (i) öppnar ett hjälpkort.
- **Skärmkanterna** glöder violetta, blir röda när dosen stiger, och pulserar en gång i sekunden.
- **Minikartan** ritar det svarta hålet med dess ringar som ellipser (kartan sträcks ut med sitt fönster), och dess verktygstips anger radierna. Kartan Stjärnsystem markerar sektorn med ett litet svart hål.
- **En strålningsräknare** tickar snabbare när dosen stiger, ovanpå striden. En varningssignal i två toner ljuder när du korsar randen och igen vid din punkt utan återvändo, och ett lågt mullrande hörs från ungefär 6 500 enheter, djupare ju närmare du är.
- **Bilden:** från grafikkvaliteten **Medel** och uppåt (med efterbehandling på) ritas hålet genom att ljuset följs runt det, stråle för stråle: en svart skugga med en tunn vit fotonring runt sig, och ackretionsskivan så som dess ljus skulle nå dig. Med kameran högt är det en klar ring runt mörkret; tippa kameran lågt och skivans bortre sida böjer sig upp över hålet och dess undersida under det, medan den närmare sidan går förbi framför. Himlen bakom hålet böjs också, måttligt: stjärnorna, nebulosan, planeterna och asteroiderna trycks utåt runt skuggan och deras linjer böjs runt den. Skeppen ritas över hålet och svärtas inte längre av det: ett skrov mellan dig och hålet stannar framför. Medel följer ljuset färre varv, ritar färre bilder av skivan och utelämnar uppljusningen av den sida som vrider sig mot dig, som Hög och Ultra lägger till. **Låg grafikkvalitet**, och en bildruta utan efterbehandling, behåller den äldre bilden: en svart skiva med en klar ring och en ackretionsskiva av tre motroterande lager, utan böjd himmel. Ett grafikkort som inte kan bygga den nya bilden går också tillbaka till den äldre bilden, med den svaga böjning av stjärnorna som den hade. På alla nivåer tillkommer strimmor av materia som faller in längs dragningen (de faller med dragningens egen fart, så ett skepp som inte flyger förs med i takt med dem, och ett som flyger ut mot dragningen ser dem strömma förbi). Ett skepp som dragningen för med sig har ingen motorlåga och drar ingen svans efter sig; ett som flyger ut mot den brinner med full fart genom strömmen, och dess svans strömmar mot hålet. Kamerans skakningar växer med dragningen, räknat som andelar av ditt skepps fart, ligger på sin inställda nivå vid din punkt utan återvändo och fortsätter att öka till horisonten. Ett skepp som hålet bränner sprutar violetta gnistor; ett som det sväljer dras mot mitten och sträcks ut tunt. Sektorns himmel är den mörkt violetta och gröna från `DS-3`.
- **Vrakdelarna:** stenar och bitar av vrakade skrov cirklar runt det svarta hålet och faller in längs spiraler, från kanten av dess dragning till horisonten: först långsamt, sedan allt snabbare, svepande runt det och tumlande fortare ju närmare de kommer. De glöder orange i skivans ljus, sträcks ut till nålar när de slits sönder, och är borta innan de når horisonten. Bland dem finns några stora stenar, och en del driver ovanför flygplanet så att skepp passerar under dem. De är bara kuliss: ingenting träffar dem och de träffar ingenting, och de syns bara inom ungefär fyratusen enheter från det svarta hålet och bleknar ut mot 6 500. Skivans ljus faller också på ditt skepp när det är nära.
- **När du förstörs** förklarar överlägget varför: ”Uppslukad av det svarta hålet” eller ”Bränd av strålning”, och Spelloggen har raden.

Inställningar hjälper där hålet är tungt eller jobbigt för ögonen: **Minska rörelser** stoppar skivan och strimmorna, håller vrakdelarna stilla och stoppar pulserandet i skärmkanterna, och **Minska skärmskakning** stoppar kamerans skakningar nära hålet; **Låg grafikkvalitet** behåller den äldre bilden utan strålföljningslinsen och ritar färre strimmor (40, mot 100 på Medel och 200 över det) och färre vrakdelar (30, mot 80 på Medel och 160 över det), låter ringen brinna starkare som kompensation, och ritar fjärrvyn med en glöd mindre. En lägre **partikelkvalitet** tunnar ut vrakdelarna på samma sätt som den tunnar ut stenarna i bakgrunden.

## Hålla sig undan {#staying-out}

- Servern styr dig: en förflyttningsorder som skulle ta ditt skepp över strålningsringen (4 200 enheter från mitten, något bredare än själva strålningen) flygs i stället **runt** den, längs dess kant. Order som slutar innanför ringen flygs som de gavs; att flyga in är ditt eget val. Rutter över sektorn blir upp till en femtedel längre, lederna mellan portalerna inte alls.
- Chattens flik **System** varnar dig när du korsar strålningens kant, dragningens kant och din egen punkt utan återvändo, och igen när du är fri. Raderna finns inte i **Global** eller **Lokal**.
- Om du lämnar spelet i strålningen, utanför dragningen, kommer du tillbaka på ringens yttre kant, stillastående, med det skrov du hade. Lämnar du det **innanför dragningen** (3 000 enheter) kommer du tillbaka exakt där du lämnade det, med det skrov du hade, och fallet fortsätter: att logga ut är ingen väg ut ur det svarta hålet.
- En äldre version av spelet visar inte det svarta hålet. Den får ändå varningarna och styrningen, och kan fortfarande flyga in i ringen om du beordrar det.

Drönare flyger med sitt skepp. Last läggs aldrig ut innanför ringen: en låda som skulle hamna där läggs på dess kant. Lådor med Dark Matter är det enda undantaget.

## Skaffa Dark Matter {#dark-matter}

Ny med Dark Matter? [Dark Matter och Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md) har hela vägen, från forskningen till plattan. Det här avsnittet är det svarta hålets sida.

Hålet ger tillbaka **Dark Matter** för en **N.I.K.E.**-raket som når det. En N.I.K.E. är en raket med 67 500 till 75 000 i skada som träffar det första skepp den kan skada och förbrukas på det; om inget är i vägen flyger den till hålet och förbrukas när den korsar händelsehorisonten. [Monteringen](/wiki/06-Items/Rockets.md) tillverkar N.I.K.E.-raketer när deras teknologi är framforskad ([Forskning](/wiki/03-Mechanics/Research.md)), fem per tillverkning (100 000 krediter, 1 500 Thulium, 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite).

- **Avfyrning.** En N.I.K.E. flyger 4 050 enheter på 4,5 sekunder (900 i sekunden) rakt mot det du siktade på: utan valt mål, lägg markören på det svarta hålet (eller rikta skeppet mot det). Den når horisonten från var som helst mellan strålningens rand (4 000 enheter) och 4 380 enheter från mitten. Längre bort faller den kort och går till spillo. Som alla raketer använder den den gemensamma omladdningen, och efter den väntar du 4,6 sekunder på nästa raket (ingen laser behöver vara monterad); att avfyra den avslutar ditt skydd i den säkra zonen och ditt kamouflage. **Ett skepp på linjen tar den i stället**: en rival som väntar vid randen, eller en pilot från en annan koncern som plockar upp lådor i vägen, träffas av 67 500 till 75 000 och hålet får ingenting. Utomjordingar och koncernpiloter kommer aldrig innanför ringen, så en fri linje är din att hålla fri; den flyger genom din egen koncern och genom skepp som är säkra för dig. Lämnar du kartan efter skottet flyger den vidare utan att skada någon och ger ändå din Dark Matter. En drönarformation kan ändra träffens skada, men inte väntan efter en N.I.K.E. (se [Drönarformationer och raketer](/wiki/06-Items/Rockets.md#drone-formations-and-rockets)).
- **Vad som kommer tillbaka.** Varje N.I.K.E. som når horisonten ger **1, 2 eller 3 Dark Matter** (2 i snitt, så ungefär fem N.I.K.E.-raketer ger tio), i en eller två små lådor som dyker upp vid randen av hålets zon, **3 050 till 3 950 enheter från mitten**, nära linjen ditt skott kom in på. Dragningen slutar vid 3 000, så lådorna och skeppen som tar dem dras inte, och strålningen där är 0,3 till 0,8 % av ett skepps HP i sekunden: en minut mitt i bandet kostar en tredjedel av ditt skepp. Ett helt skepp håller tre minuter där.
- **Vems.** Lådorna är dina, och din klans, i **60 sekunder** från skottet. Därefter får vem som helst på kartan ta dem, och de driver bort efter **4 minuter**. Farosektorn är en PvP-sektor, så räkna med sällskap. En pilot som loggar ut efter att ha avfyrat har fortfarande sina lådor.
- **Hur många.** En karta rymmer högst 32 lådor med Dark Matter; en ny knuffar ut den äldsta av dem, och aldrig någon annan sorts låda. [Resource Magnet Booster](/wiki/03-Mechanics/Cargo.md) lägger inget till Dark Matter.
- **Vad du ser.** När en N.I.K.E. korsar horisonten sträcks den ut in i hålet, rymden krusar sig ut från där den gick in, och skivan och fotonringen blossar upp i ungefär en och en halv sekund (en tredjedel av det, med hälften av ljuset, under **Minska rörelser**). Ett ögonblick senare kommer lådorna ut ur hålet och driver till sina platser vid randen: var och en är ett violettsvart klot med en ljus kant och gnistor, lätt att se på långt håll, och med titeln **Dark Matter** när du håller pekaren över den. Dina visar sekunderna du har kvar över dem, och syns på minikartan som ett litet violett märke, liksom för din klan; andra piloters lådor syns på minikartan först när deras minut är slut.
- **Vad den är till för.** Monteringen pressar 5 Dark Matter med en Velkonite Reinforced Plate och en Orvium Reinforced Plate till en **Dark Matter Plate**, och [Smedjan](/wiki/06-Items/Forge.md) kräver två av dem för att höja ett föremål från Gudomlig till Rämnande och igen från Rämnande till Evig: tio Dark Matter per steg. Sista nivån i varje uppgraderingskedja kräver 3 plattor, 15 Dark Matter per del: Amp, sköldceller och styrraketer av nivå IV, Heavy Shield Core, Engine III, Helios Beam, Extra Slots CPU III och Base CPU II. Skylabs [forskningscentrum](/wiki/03-Mechanics/Research.md#dark-matter) behöver också Dark Matter: 10 för var och en av de 16 teknologierna högst upp i trädet, 160 sammanlagt, tillagda i centret innan forskningen börjar. Drönarformationerna kräver också Dark Matter, 5, 13 eller 20 efter styrka: 189 till, 349 sammanlagt. En Helios Beam med sina tre Amp av nivå IV rymmer 60 Dark Matter, och en Wraith som bara bär delar av sista nivån 900 ([Dark Matter och Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md#what-the-last-tier-asks-for)).
