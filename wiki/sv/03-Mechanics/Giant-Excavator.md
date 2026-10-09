<!-- wiki-i18n source: 5df6b18400b138dc -->
<!-- wiki-i18n title: Jättegrävmaskin -->
# Jättegrävmaskin {#giant-excavator}

<!-- wiki-search: excavator; giant excavator; pulsar; mining; fuel; excavator fuel; control panel; overheat; radiation; slumbering void; voids; wave; ds-1; ds-2; ds-3; grävmaskin; jättegrävmaskin; pulsar; bränsle; kontrollpanel; överhettning; strålning; våg -->

Från säsongsdag 11 lyser en **pulsar** i var och en av farosektorerna `DS-1`, `DS-2` och `DS-3`, och bredvid den står en **jättegrävmaskin**. Grävmaskinen bryter pulsaren på **Thulium och sällsynta malmer**, och den bränner [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md) för det. Vem som helst får tanka den, välja vad den bryter och starta den, och allt den lämnar ifrån sig ligger runt den i lådor som vem som helst får ta. En körning är dock högljudd: hela världen får veta när den startar, **Slumbering Voids** kommer efter den i vågor, och en grävmaskin som körs för länge överhettas och bestrålar hela området. Den här sidan berättar hur en körning går till, vad den ger och hur du överlever den. Sektorerna finns i [Farosektorer](/wiki/01-General/Danger-Sectors.md); Voids i [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).

## I korthet {#at-a-glance}

<!-- excavator-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Var**: En pulsar med en jättegrävmaskin i var och en av sektorerna `DS-1`, `DS-2` och `DS-3`, i varje värld
- **Dyker upp**: Från säsongsdag 11 till wipen
- **Bränsle**: Dark Matter. En brinner i 10 min; tanken rymmer 3, vilket är 30 min av brytning. Vem som helst får lägga till en i taget, ur den egna lasten
- **Panel**: Fönstret fungerar inom 600 enheter från grävmaskinen, och skylten syns från 1 400 enheter. Vem som helst får tanka, välja och starta; valet är låst medan den går
- **Lådor**: En låda var 20 s, 450 till 900 enheter från grävmaskinen, fri för vem som helst från det ögonblick den ligger. Den ligger kvar i 5 min, och högst 24 ligger på en karta samtidigt
- **Värme**: 30 min av brytning, i så många körningar som det behövs, och grävmaskinen överhettas i 1 h. Värmen finns kvar mellan körningarna och försvinner efter vilan
- **Strålning**: Medan den är överhettad eller förstörd bränner grävmaskinen (inom 1 100 enheter) och dess pulsar (inom 1 300 enheter) varje skepp inuti: 10 % av dess totala HP varje sekund
- **Skrov**: 200 000 HP i Alfa, 300 000 i Beta och 400 000 i Gamma. Bara Slumbering Voids kan skada den, och bara när ingen pilot är kvar för att försvara den
- **Voids**: 2 Slumbering Voids var 2 min medan den bryter, den första 1 min efter starten; högst 8 levande på en karta
- **Meddelanden**: Piloterna i hela världen får veta när en körning startar, när grävmaskinen överhettas och när den förstörs; resten går till piloterna i dess sektor. Det är systemrader: de syns på chattens flik **System** och i Spelloggen, och inte i **Global** eller **Lokal**.

<!-- excavator-glance:end -->

## Så går en körning till {#how-a-run-goes}

1. **Hitta en.** Var och en av de tre farosektorerna som har en pulsar har en grävmaskin, i varje värld. En skylt, **Grävmaskin**, hänger över den när du är nära, och Stjärnsystemskartan visar tillståndet för grävmaskinen i den sektor du flyger i.
2. **Öppna panelen.** Klicka på skylten. Fönstret **Jättegrävmaskin** fungerar så länge ditt skepp är inom kontrollpanelens räckvidd (listan *I korthet* anger den). Ett kamouflerat skepp kan använda den, och att använda den avslutar inte kamouflaget.
3. **Tanka den.** **Lägg till Dark Matter** lägger en Dark Matter från din last i tanken. Vem som helst kan göra det. Tanken tar aldrig emot mer än grävmaskinen hinner bränna innan den överhettas, så inget bränsle går till spillo.
4. **Välj vad som ska brytas** i listan och tryck sedan på **Starta brytning**. Det kräver minst en Dark Matter i tanken och en resurs. Vem som helst kan ändra valet fram till starten; när den går är resursen låst. Starten meddelas varje pilot i världen, med ditt namn, sektorn och resursen.
5. **Håll den.** Medan den bryter faller en låda runt grävmaskinen med några sekunders mellanrum, och strax efter starten anländer de första Slumbering Voids. Försvara grävmaskinen och ta lådorna.
6. **Håll koll på värmen.** Värmefältet fylls medan grävmaskinen bryter och töms aldrig medan den väntar. Vid gränsen överhettas grävmaskinen. Gå innan dess: spelet varnar kartan två gånger.
7. **Den vilar.** Överhettad eller förstörd är grävmaskinen och dess pulsar bestrålade tills vilan är över; sedan är den redo igen, med värmen nollställd och skrovet fullt.

Fönstret visar dessutom sektorn, tanken (en cell för varje Dark Matter, den som brinner ritad till en del), hur mycket Dark Matter du bär, grävmaskinens skrov, vad varje resurs ger per minut i din värld och, medan den bryter, tiden till nästa våg och de Voids som lever. När något nekas läser du skälet i rött: du är för långt från panelen, du har ingen Dark Matter, tanken är full, det finns inget bränsle eller ingen vald resurs än, resursen är låst medan den går, eller grävmaskinen är het.

| Tillstånd | Vad det är | Vad du kan göra |
| :--- | :--- | :--- |
| **Redo** | Inget bränsle, eller bränsle och inte startad. Värmen hittills finns kvar. | Lägga till Dark Matter, välja, starta. |
| **Bryter** | Den bränner Dark Matter och samlar värme; resursen är låst. | Lägga till mer Dark Matter upp till det utrymme som finns kvar, slåss mot Voids, ta lådorna. |
| **Överhettad** | Värmen nådde sin gräns. Tanken töms; lådorna som redan lagts ligger kvar. | Ingenting. Området är bestrålat: håll dig borta. |
| **Förstörd** | Voids tog skrovet till noll. Bränslet är förlorat, skrovet är fullt igen på en gång. | Ingenting. Området är bestrålat: håll dig borta. |

Om bränslet tar slut före gränsen går grävmaskinen tillbaka till **Redo** med sin värme kvar, och de Voids som är kvar går efter en stund, om de inte slåss.

## Vad den bryter {#what-it-mines}

En full tank är avvägd för att ge ungefär vad två eller tre piloter skulle tjäna på en halvtimme av det bästa Thulium-farmandet. Beta och Gamma ger mer, eftersom de betalar mer för varje nedskjutning. Du väljer en resurs per körning. En låda är densamma för alla, och en Thulium-låda är kontanter som betalas när den plockas upp, som asteroidernas Thulium.

<!-- excavator-resources:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

En full tank (3 Dark Matter, 30 min av brytning) ger mängderna nedan, i 90 lådor.

| Resurs | Alpha | Beta | Gamma | En minut, i Alfa | En låda, i Alfa |
| :--- | ---: | ---: | ---: | ---: | ---: |
| [Thulium](/wiki/06-Items/Resources.md#thulium) | 4 821 | 7 714 | 9 643 | 160,7 | 53,6 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | 1 157 | 1 851 | 2 314 | 38,6 | 12,9 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | 514 | 823 | 1 029 | 17,1 | 5,7 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | 320 | 320 | 320 | 10,7 | 3,6 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | 160 | 160 | 160 | 5,3 | 1,8 |

- En körning av Velkonite eller Orvium ger högst 4 timmar från en nivå 20-samlare i [Skylab](/wiki/03-Mechanics/Skylab.md) för den malmen (320 Velkonite, 160 Orvium), i varje värld: det är Skylabs malmer, och en körning påskyndar aldrig dess takt mer än så.
- En låda innehåller ungefär mängden i sista kolumnen, 15 % mer eller mindre. En Thulium-låda är kontanter: upplockningen betalar ut dem. En malmlåda innehåller föremålet.

<!-- excavator-resources:end -->

Pilotens egna boosters fungerar som för all last: Resource Magnet Boosters bonus ökar en malmlåda. Det finns ingen dagsgräns för lådorna: bränslet och klockan är det som begränsar en körning.

**Vad malmen är till för.** Malmen i en låda hamnar i din last som vilket föremål som helst. Cataclysite och Quorvium används i Monteringen och i Smedjan ([Resurser](/wiki/06-Items/Resources.md)). Skylabs smedja tar sin malm bara från Resurslagret, som samlarna fyller; Velkonite och Orvium i en låda är alltså bränsle för [Forskningscentrumet](/wiki/03-Mechanics/Research.md#fuel), inte för smedjan.

## Slumbering Voids {#the-slumbering-voids}

En körning lockar **Slumbering Voids**, jägare från den försvunna civilisationen som flyger in från kartans kant för att skydda pulsaren mot den som vill tömma den. De jagar piloterna nära grävmaskinen, och när det inte finns någon kvar att jaga går de på grävmaskinen. Voidens siffror och betalning finns i [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).

<!-- excavator-voids:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Vågor.** 2 Slumbering Voids var 2 min; den första 1 min efter starten, och ingen under körningens sista 1 min. Högst 8 lever på en karta samtidigt: en våg som finner kartan full hoppas över.
- **Ankomst.** En våg dyker upp vid kartans kant, 900 enheter innanför den och minst 2 500 enheter från varje portring, och flyger till grävmaskinen på ungefär 20 s. Meddelandet nämner den sida av kartan den kommer från.
- **Jakt.** En Void jagar den närmaste pilot den kan se inom 2 500 enheter, och håller sig inom 7 000 enheter från grävmaskinen.
- **Belägring.** När ingen pilot de kan se är inom 7 000 enheter från grävmaskinen på 15 s, anfaller Voids grävmaskinen, och varje laser gör 25 % av sin vanliga skada. Vid noll förstörs grävmaskinen: dess bränsle är förlorat, dess skrov är fullt igen på en gång, och den vilar i 1 h.
- **Avfärd.** När en körning tar slut stannar de Voids som är kvar ytterligare 90 s och slåss vidare om de bekämpas; sedan lämnar de.

<!-- excavator-voids:end -->

- **En Void är en glaskanon.** Dess sköld är stor men tar upp 80 % av en träff, så skrovet bakom är borta efter några gånger sin storlek i skada, och mycket tidigare med sköldpenetration. Två eller tre välutrustade piloter klarar en körning i Alfa; Beta och Gamma kräver större grupper, som för varje utomjording.
- **Kamouflage försvarar inte platsen.** Voids ser inte kamouflerade skepp, så en pilot som gömmer sig håller dem inte borta från grävmaskinen; och en pilot som tar skydd i en portring kan inte nås och räknas inte heller.
- **Varje Void betalar** efter skadan du gjorde på den och tappar en låda ([så betalar en bossnedskjutning](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Deras nedskjutningar räknas till dina PvE-poäng för grad som en svärmskepps.

## Värme och strålning {#heat-and-radiation}

Brytningen lägger på värme sekund för sekund. Värmen är **kumulativ och svalnar aldrig medan grävmaskinen väntar**: en körning som avslutas tidigt lämnar nästa pilot en kortare. När den når gränsen **överhettas** grävmaskinen, och när dess skrov tas till noll **förstörs** den; i båda fallen strålar grävmaskinen och dess pulsar tills vilan är över.

<!-- excavator-radiation:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

| Cirkel | Radie | Total HP per sekund | Ett fullt skepp håller |
| :--- | ---: | ---: | ---: |
| Jättegrävmaskinen | 1 100 | 10 % | 10 s |
| Pulsaren | 1 300 | 10 % | 10 s |

- **Dosen.** 10 % av ett skepps totala maximala HP (skrov plus sköld) varje sekund, så ett fullt skepp håller 10 s, oavsett klass. Skölden tar den först och dess absorption räknas inte.
- **Vem.** Varje skepp inom cirklarna, även kamouflerade; ingen utomjording. Det räknas som skada du tar: en Reparationsdrönare stannar och skölden laddas inte, som vid det svarta hålet.
- **Tillskrivning.** En pilot som brinner ihjäl tillskrivs den sista fienden som träffade piloten under de 15 s före.
- **Varningar.** Kartan får veta det 1 min och 15 s före överhettningen.

<!-- excavator-radiation:end -->

- **Varningen.** Två gånger före överhettningen (tiderna står i listan ovan) får kartan veta det, ett skepp inom cirklarna ser en varning, och cirklarna ritas på Stjärnsystemskartan och minikartan. När de strålar är cirklarna röda och Strålningsmätaren visar dosen.
- **Att lämna området.** Alla standardskepp kan ta sig ut från panelens kant eller från den längst bort belägna låda som finns kvar, utom den långsamma Ironclad: den lämnar under varningen, eller så lämnar den inte. Stå inte på en låda när värmen tar slut.
- **Byte i cirklarna.** Lådor som lagts före överhettningen ligger kvar i strålningen: en låda som ligger där när den börjar tas till priset av dosen.
- **En omstart av servern** pausar en körning: bränslet och värmen kommer tillbaka som de var, vilan går vidare efter klockan, och första vågen efter omstarten kommer en minut senare.

## Strid om en körning {#fighting-over-a-run}

Grävmaskinen har **ingen särskild ring**: din världs vanliga regler gäller, så rivaler kan komma, skjuta på dig och ta lådorna (en låda är fri för vem som helst från det ögonblick den ligger). Att stjäla och lägga bakhåll hör till eventet. Några saker att räkna med:

- **Den som tankar är inte den som vinner.** Vem som helst får tanka, välja och starta; en rival kan ändra resursen innan du trycker på Starta. Kontrollera valet innan du trycker.
- **Bränslet är i fara.** Om grävmaskinen förstörs är Dark Matter i dess tank förlorad, och ingen får tillbaka den. Det mesta som kan gå förlorat är den fulla tanken.
- **Ta med en grupp** och bestäm vem som stannar vid grävmaskinen och vem som tar lådorna, och håll ett öga på värmen: piloterna som tar de sista lådorna är de som strålningen fångar.
- **Voids kommer till grävmaskinen, inte till lådorna.** En grupp som håller grävmaskinen sysselsätter Voids; en som drar iväg lämnar den åt belägringen.

## Vad världen får veta {#what-the-world-is-told}

Det här är systemrader (de syns på chattens flik **System** och i Spelloggen, inte i **Global** eller **Lokal**). De tre första går till hela världen; den sista till piloterna i grävmaskinens sektor.

- Den dag event 2 börjar: farosektorerna har förändrats.
- En pilot **startar** en grävmaskin, med sektor, resurs och minuter av bränsle.
- Grävmaskinen **överhettas** eller **förstörs**.
- Bränslet tar slut; grävmaskinen är på väg att överhettas (två varningar); en **våg** av Voids är på väg, med sitt nummer och den sida av kartan den kommer från; ingen pilot är kvar, så Voids anfaller grävmaskinen.

Varje handling på panelen och varje varning har ett eget lågmält ljud, på effektvolymen.

## Läs mer {#where-to-read-more}

- [Farosektorer](/wiki/01-General/Danger-Sectors.md): var pulsarerna står och vad mer som är nytt.
- [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md): Slumbering Void, Inert Mass och Unwakened.
- [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md) och [Svart hål](/wiki/03-Mechanics/Black-Hole.md): var bränslet kommer ifrån.
- [Resurser](/wiki/06-Items/Resources.md): malmerna grävmaskinen ger.
- [Last](/wiki/03-Mechanics/Cargo.md): lådor, upplockning och Resource Magnet Booster.
- [Grader](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points): PvE-poängen för en Void.
