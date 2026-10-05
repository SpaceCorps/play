<!-- wiki-i18n source: aaaba3fffe8e8a67 -->
<!-- wiki-i18n title: Hangar -->
# Hangaren under flygning {#the-hangar-in-flight}

Du behöver inte återvända till basen för att ändra ditt skepp. Inifrån en säker zon kan du öppna fönstret **Hangar** (knappen med en lagerbyggnad i verktygsfältet uppe till vänster) och ändra vad som är monterat, byta till den andra konfigurationen eller flyga ett annat skepp du äger, utan att lämna spelet. Fönstret är stationens Hangar-sida, med samma platser, värden och inventarie, i ett fönster över spelet. Se [Inventarie och utrustning](/wiki/03-Mechanics/Inventory.md) för hur föremål monteras.

![The Hangar window in flight, opened at the station on its Drones view: the drones, the list of drone formations and the inventory](../../img/wiki-img/shots/hangar-window.jpg)

## När den är öppen {#when-it-is-open}

En ändring tillåts bara så länge allt det här stämmer:

- **En säker zon skyddar dig.** Varje station och portal har en skyddsring (se [Strid](/wiki/03-Mechanics/Combat.md)). Innanför den är du skyddad när 5 sekunder har gått sedan du träffades och 15 sedan du sköt.
- **Du har varit utanför strid** några sekunder till: **10** som standard. Det spelar roll när du anländer skyddad direkt, genom en portal, med en strid bakom dig.
- Du är inte kamouflerad, inte inom din egen EMP:s fönster och inte nära det [svarta hålet](/wiki/03-Mechanics/Black-Hole.md), och ingen av dina raketer är fortfarande på väg.

Pågående reparationer hindrar dig inte. Överallt annars öppnas Hangarfönstret ändå, men det är skrivskyddat. Ett bärnstensfärgat fält förklarar varför, och räknar ned sekunderna när det är en väntan (”Du var i strid alldeles nyss. Vänta 6 s för att ändra ditt skepp.”). Servern kräver det också, så ingenting kan ändra ett skepp ute i fältet.

## Vad du kan ändra {#what-you-can-change}

- **Utrusta och ta av vad som helst**, i alla slags platser: lasrar, generatorer (sköldar, motorer, adaptiva kärnor), extrautrustning, förmågeplatser och drönarplatser, samt förstärkarna, cellerna och styrraketerna som sitter i dem. Dra föremål till platserna, eller klicka på dem, precis som på stationen. Ditt skepp följer med direkt: värden, lasrar, förmågor och snabbfältet.
- **Båda konfigurationerna.** Du kan förbereda Konfig 2 medan du flyger med Konfig 1 och sedan byta med tangenten Byt konfig. En knapp **Flyg konfig** i hangaren gör samma byte.
- **Vilket skepp som helst.** Gör ett annat skepp aktivt så flyger du det därifrån du är. Ditt skepps modell byts inför ögonen på alla i närheten.
- **En ny sköld, motor eller adaptiv kärna börjar tom**, som på stationen: konfigurationens sköldladdning är tom tills den har laddats upp.
- **Drönarformationer.** Vyn Drönare listar under dina drönare de formationer du äger. De sätts inte på: under flygning drar du en från Formationslistan i snabbfältet till en plats, och platsens klick eller tangent bär den, inne i en säker zon utan väntan ([Drönarformationer](/wiki/03-Mechanics/Formations.md)).
- **Extrautrustning.** De fyra vanliga skeppen, Protos, Kitefin, Ostirion och Nomad (de du börjar med eller köper), har 2 extraplatser per konfiguration; de fyra skepp du tillverkar i Monteringen, Paragon, Ironclad, Wraith och Storm, har 3. Extra Slots CPU i din Skylab lägger till 3, 5 eller 7: 5, 7 eller 9 på de vanliga och 6, 8 eller 10 på de tillverkade ([Extrautrustning](/wiki/06-Items/Extras.md#extra-slots-cpus)). När 0.4.10 kom togs en tredje extrautrustning på ett vanligt skepp av och hamnade i ditt inventarie: inget raderades, och du fick ett chattmeddelande.

## Byta skepp {#changing-ship}

Skeppet du byter till har **det skrov och de sköldar det hade** när du senast flög det, precis som om du hade flugit ut med det. Ringen reparerar inte, så att byta skepp läker dig aldrig: skeppet du lämnar behåller sin skada och kommer tillbaka med den. Ett vrakat skepp går inte att flyga förrän du har reparerat det, vilket är gratis och ger det högst 10 000 skrov och ingen sköld, som en återkomst.

Det som är ditt förblir ditt: din ammunition, dina raketer och deras omladdning, dina förmågors återhämtning, dina boosters, din XP och dina Slave Drones. Det som hörde till skeppet upphör: en pågående Shield Surge eller Afterburner, reparationer, din målfixering, ditt anfall och kursen du flög. Utrustning sitter kvar på det skepp den är monterad på.

## Förfrågningar från andra verktyg {#requests-from-other-tools}

Hangaren ändras bara från en säker zon även på servern: att montera, ta av, radera ett föremål, reparera ett skepp eller göra ett skepp aktivt medan du flyger besvaras med ”Du kan bara ändra ditt skepp i en säker zon.” Konfigurationsbytet är undantaget och fungerar var som helst (en gång var 5:e sekund).
