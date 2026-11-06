<!-- wiki-i18n source: 76933ad9dd56b71f -->
<!-- wiki-i18n title: Dungeons -->
# Dungeons

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; portal; clan portal; join; clan gate alerts; clan dungeon window; start room; fog; guards; locked room; boss room; booster; boosters; swarm assist; focus most wanted; zone of chaos; rocket barrage; port; portar; krigsherre; labyrint; steg; bytezon; kort; portal; klanportal; booster; dimma; väktare; startrum; låst rum; svärmhjälp; kaoszon; klanens portaviseringar -->

En **dungeon** kallas **port** i spelet: en sluten labyrint med en **krigsherre** i änden. En vice ledare eller ledaren i en [klan](/wiki/03-Mechanics/Clans.md) öppnar en och betalar för den ur klanbanken, och klanens medlemmar flyger in tillsammans som en [grupp](/wiki/03-Mechanics/Groups.md). De kämpar sig igenom labyrintens utomjordingar, öppnar bytezoner för att välja ett kort i var och en och fäller krigsherren. Varje pilot som deltog i striden får betalt när krigsherren faller, inom gränserna längre ner. Portarna finns på fliken **Portar** på klansidan.

En port är en strid enbart mot utomjordingarna: ingen kan attackera en klankamrat eller någon annan därinne. Utomjordingarna betalar ingenting. Betalningen kommer enbart från krigsherren, så det enda sättet att få betalt är att vara med i striden när den faller.

## I korthet {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Öppnar**: Från säsongsdag 1
- **Vem som öppnar en port**: En vice ledare eller ledaren, som betalar priset ur klanbanken
- **Grupp**: 4 till 10 medlemmar av klanen, i en grupp
- **Portar per dag**: 3 per klan och UTC-dag, en öppen åt gången
- **Portar samtidigt**: 6 i en värld
- **Kartor**: Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Labyrinter**: 8; en väljs när en port öppnas
- **Samling**: 10 min att samlas och starta. En port som ingen startar stängs, och dess pris går tillbaka till klanbanken
- **Tidsgräns**: Steg 1: 95 min, Steg 2: 130 min, Steg 3: 165 min från starten. När tiden tar slut misslyckas porten och betalar ingenting
- **Lämnad tom**: En port där ingen är inne på 3 min misslyckas
- **När krigsherren faller**: Porten förblir öppen i 2 min för piloterna som är inne
- **Komma tillbaka**: En pilot som har lämnat porten eller blivit förstörd kan flyga in igen 3 gånger, med 20 s emellan

<!-- dungeons-glance:end -->

## Hur en omgång går till {#how-a-run-goes}

1. **Kalla fram.** På fliken Portar väljer en [vice ledare eller ledaren](/wiki/03-Mechanics/Clans.md#hierarchy-roles) ett steg och trycker på **Kalla fram**. Priset tas ur [klanbanken](/wiki/03-Mechanics/Clans.md#clan-economy-taxation), och porten får en av kartorna som listas ovan. En port som ingen startar stängs, och priset går tillbaka till banken.
2. **Gå in.** Klanens medlemmar trycker på **Gå in** i klanfönstret medan de flyger, hoppar genom klanportalen eller trycker på **Gå med** på aviseringskortet (se Gå in). Alla landar i startrummet, och piloterna därinne är portens grupp.
3. **Starta.** Startrummet är ett litet rum i ena änden av labyrinten, och dess dörr är stängd medan porten samlas. Det finns inga utomjordingar där, så det är säkert att vänta. Porten **startar av sig själv** när varje pilot den väntar på är inne och gruppen är tillräckligt stor. Den väntar på klanens medlemmar som är online, inte borta och i gruppen hos en pilot som har gått in, och den startar genast när gruppen är full. Piloten som öppnade porten, eller en officer, kan trycka på **Starta** för att börja tidigare med de piloter som är inne, om de är tillräckligt många. En pilot som lämnar väntas inte längre på. När porten startar öppnas dörren för gott, och därefter kan bara piloter som redan var inne komma tillbaka.
4. **Kämpa dig genom labyrinten.** Du kommer in i ena änden av labyrinten och krigsherren väntar i den andra, i ett låst rum. Labyrinten är mörk: du ser bara det gruppen har utforskat och det som är nära dess skepp. Utomjordingarna sover i flockar i korridorerna, och en flock som vaknar jagar gruppen genom labyrinten.
5. **Öppna bytezonerna.** Ringar i labyrinten markerar zonerna. Håll en och gruppen röstar om ett kort, som betalas ut tillsammans med krigsherrens betalning.
6. **Lås upp bossrummet.** Förstör väktarna, Crystalys och deras tvillingar, så öppnas dörren till krigsherrens rum. Tills dess kan krigsherren inte skadas.
7. **Besegra krigsherren.** Bryt hans sköld och skrov och svara på hans förmågor. När han faller är porten avklarad.
8. **Få betalt.** Betalningen kommer i samma ögonblick som krigsherren faller. Porten står öppen en stund till för piloterna därinne och stängs sedan.

## Gå in {#entering}

För att gå in i en port behöver du ett **skepp i flykt**, så starta först och öppna sedan klanfönstret, och en [grupp](/wiki/03-Mechanics/Groups.md) med tillräckligt många klanmedlemmar. Du behöver också den **nivå** som steget kräver, och du får inte redan vara inne i en annan port. Portens grupp har en storleksgräns: när den är full kan ingen annan gå in.

En vice ledare eller ledaren öppnar en port, en i taget för klanen, och bara upp till antalet portar per dag. Klanbanken måste ha priset. En klan kan öppna ett steg först när den har klarat steget före.

Inne i en port kan du inte byta värld, och Jump CPU och Base CPU fungerar inte. Knappen **Lämna** i fönstret Klanport tar ut dig. Den ber först om bekräftelse, utom när krigsherren redan har fallit: då går du ut direkt. En pilot som har lämnat, eller blivit förstörd, kan flyga in igen några gånger, med en kort väntan emellan.

### Klanportalen och aviseringen {#the-clan-portal-and-the-call}

När en port öppnas får klanen en **portal** till den på varje koncerns hemkarta (`M-1`, `T-1` och `G-1`), en bit utanför stationens säkra zon. Bara klanens piloter ser den: för alla andra finns den inte. Den har ingen egen säker zon. Flyg fram till den och hoppa som vid vilken portal som helst, så tar den dig in i porten enligt reglerna för **Gå in**: ett skepp i flykt, en grupp med tillräckligt många klanmedlemmar, stegets nivå och plats i gruppen. När porten har startat kan bara piloter som redan var inne använda den. Portalen försvinner när porten är över.

Medan din klans port samlas och du flyger någon annanstans får du en **avisering**: ett kort högst upp på flygskärmen, med ett ljud. Det säger vem som öppnade porten, hur många piloter som är inne och hur länge porten står öppen. **Gå med** flyger in dig, som **Gå in** på fliken Portar, och när du lämnar porten kommer ditt skepp tillbaka dit det var. Gå med är nedtonad medan din grupp är för liten. **Inte nu** döljer kortet för den porten. Om din grupp redan är inne och porten väntar på dig står det på kortet. Kortet når klanens piloter som flyger (inte dem som är dockade vid en station) och som har den nivå steget kräver. Du kan stänga av kortet och dess ljud med **Klanens portaviseringar** i Inställningar › Allmänt › Grupper.

### Fönstret Klanport {#the-clan-dungeon-window}

Inne i en port har omgången ett eget fönster, **Klanport**. Det visar tiden som har gått och det som är kvar, hur många utomjordingar som flyger och hur många som har förstörts, vad gruppen ska göra nu (utforska labyrinten, hålla en zon, hitta bossen, förstöra väktarna, besegra krigsherren), gruppens skrovstaplar, hållstapeln medan du står i en zon, krigsherrens förmåga med nedräkningen och knappen **Lämna**. Det är ett fönster som de andra: dra det i titelraden och stäng det med det röda ljuset i hörnet. Det öppnas av sig självt när du går in i en port, en gång för varje port: om du stänger det förblir det stängt till nästa port. Verktygsfältet har en knapp **Klanport** för det medan du är i en port. Medan fönstret är stängt visas en förmåga hos krigsherren som snart startar eller är igång som ett enradigt fält med namnet och nedräkningen. Klicka på fältet för att öppna fönstret igen.

## Stegen {#the-stages}

En port har ett steg, och steget är dess svårighet. Ett högre steg har segare utomjordingar som slår hårdare, och det betalar mer. Faktorerna i tabellen är utomjordingarnas. Skada betyder deras lasrar och raketer. Krigsherren följer inte tabellen: han har egna tal för varje steg, längre ned. Tabellen säger också hur många utomjordingar ett steg skickar jämfört med det första. **Priset** tas ur klanbanken när porten öppnas.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Steg | Kräver | Utomjordingarnas skrov och sköld | Antal utomjordingar | Utomjordingarnas skada | Portens pris (krediter, ur klanbanken) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Steg 1** | Från nivå 6 | ×1 | ×1 | ×1 | 500 000 |
| **Steg 2** | Från nivå 7 | ×1,5 | ×1 | ×1,5 | 1 000 000 |
| **Steg 3** | Från nivå 8 | ×2 | ×1 | ×2 | 2 000 000 |

<!-- dungeons-stages:end -->

## Labyrinten {#the-maze}

Varje port är en sluten labyrint på en egen karta, en av kartorna i listan ovan, och labyrinten är en av flera utformningar. Labyrinten fyller hela kartan, från kant till kant: ett rutnät av rum och korridorer med massiva väggar. Skepp kan inte passera en vägg, och en vägg blockerar skott, så den är skydd. En meteor faller uppifrån, och en vägg stoppar den inte.

**Rum och dörrar.** Startrummet, där du landar, och krigsherrens rum, i andra änden, har var sin dörr. En stängd dörr är en vägg för skepp, skott och utomjordingar likadant. Startdörren öppnas när porten startar. Krigsherrens dörr förblir låst tills väktarna är förstörda (se [Det låsta rummet](#the-locked-room)). Mellan dem har labyrinten ett bytesrum för varje bytezon.

**Dimma.** Labyrinten är mörk. I flykt ser du dess väggar och utomjordingar bara där gruppen har varit, och en kort bit runt varje skepp i gruppen. Ett rum räknas som utforskat så fort en av er är i det. Minikartan fungerar likadant: en karta över hela våningen som fylls i allteftersom gruppen utforskar den, med ingången, krigsherrens dörr, de zoner ni har hittat och krigsherren när ni har hittat honom. Piloterna i din egen grupp visas alltid.

## Utomjordingarna {#the-aliens}

Fyra sorters utomjordingar vaktar labyrinten. De sover i flockar i korridorerna, aldrig i ett rum, och en flock vaknar när en pilot kommer nära. En flock som är vaken väntar inte på dig: den jagar gruppen genom labyrinten, och en flock som tappar alla går tillbaka dit den sov och läker. Några flockar är vakna från första sekunden och står i korridorerna långt från ingången tills en pilot kommer nära. Porten håller bara ett visst antal utomjordingar i luften åt gången, och det antalet växer med gruppens storlek, så en flock som vaknar kan behöva vänta på plats, och en flock du förstör släpper in nästa. En större grupp möter fler utomjordingar, i proportion, en mindre färre, och en sorts utomjording faller aldrig under en.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Utomjordingar, för en grupp på 5 | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| Gate Goombah | 156 | 156 | 156 |
| Gate Pirate | 34 | 34 | 34 |
| Gate Crystalys | 34 | 34 | 34 |
| Gate Crystalys Twin | 11 | 11 | 11 |
| Tillsammans | 235 | 235 | 235 |
| Vågen i en bytezon | 12 × Gate Goombah och 1 × Gate Crystalys | 12 × Gate Goombah och 1 × Gate Crystalys | 12 × Gate Goombah och 1 × Gate Crystalys |

- **Levande samtidigt**: Högst 10 per pilot i gruppen, och 70 totalt

<!-- dungeons-population:end -->

Varje sort i tur och ordning. Skrov och sköld är de vanliga värdena gånger multiplikatorn för steget i kolumnen.

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Gate Goombah

- **Ser ut som**: Goombah
- **Flyger i flockar om**: 6

|  | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| Skrov | 32 000 | 48 000 | 64 000 |
| Sköld | 48 000 | 72 000 | 96 000 |
| Laserskada (en salva per sekund) | 3 000 | 4 500 | 6 000 |
| Hastighet | 180 | 180 | 180 |
| Laserräckvidd | 800 | 800 | 800 |
| Aggroradie | 1 800 | 1 800 | 1 800 |

### Gate Pirate

- **Ser ut som**: Pirate Boss
- **Flyger i flockar om**: 2
- **Raket**: En rak raket var 5 s, räckvidd 970 enheter

|  | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| Skrov | 300 000 | 450 000 | 600 000 |
| Sköld | 50 100 | 75 150 | 100 200 |
| Laserskada (en salva per sekund) | 200 | 300 | 400 |
| Raketskada | 5 000 | 7 500 | 10 000 |
| Hastighet | 92 | 92 | 92 |
| Laserräckvidd | 700 | 700 | 700 |
| Aggroradie | 1 800 | 1 800 | 1 800 |

### Gate Crystalys

- **Ser ut som**: Crystalys
- **Flyger i flockar om**: 2

|  | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| Skrov | 256 000 | 384 000 | 512 000 |
| Sköld | 160 000 | 240 000 | 320 000 |
| Laserskada (en salva per sekund) | 10 000 | 15 000 | 20 000 |
| Hastighet | 230 | 230 | 230 |
| Laserräckvidd | 900 | 900 | 900 |
| Aggroradie | 2 400 | 2 400 | 2 400 |

### Gate Crystalys Twin

- **Ser ut som**: Crystalys, 1,4 gånger så stor
- **Flyger i flockar om**: 1

|  | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| Skrov | 512 000 | 768 000 | 1 024 000 |
| Sköld | 320 000 | 480 000 | 640 000 |
| Laserskada (en salva per sekund) | 20 000 | 30 000 | 40 000 |
| Hastighet | 230 | 230 | 230 |
| Laserräckvidd | 900 | 900 | 900 |
| Aggroradie | 2 400 | 2 400 | 2 400 |

<!-- dungeons-enemies:end -->

## Krigsherren {#the-warlord}

Krigsherren väntar i rummet i andra änden av labyrinten, och han är det enda i en port som betalar. Han är en Crystalys som vuxit enorm. Hans skrov och sköld växer med gruppens storlek: ju fler piloter som går in, desto segare är han, i proportion. Han lämnar aldrig sitt rum, vare sig dörren är stängd eller öppen: han håller sig innanför rummets väggar och jagar inte genom korridorerna. En pilot utanför kan bara locka honom till kanten av rummet, och genom en öppen dörr skjuter han ändå på allt hans laser når. Han använder sina förmågor en i taget, i slumpmässig ordning, var och en med sin egen återhämtningstid.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Ser ut som**: Crystalys, 3 gånger så stor
- **Sköldladdning**: 3 000 per sekund, efter 15 s utan skada

|  | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| Skrov | 10 000 000 | 15 000 000 | 25 000 000 |
| Sköld | 8 000 000 | 12 000 000 | 20 000 000 |
| Laserskada (en salva per sekund) | 12 500–15 000 | 15 000–17 500 | 20 000–25 000 |
| Hastighet | 120 | 120 | 120 |
| Laserräckvidd | 1 100 | 1 100 | 1 100 |

Skrovet och skölden ovan gäller för en grupp på 5. De växer med gruppen: det är krigsherrens skrov och sköld tillsammans, efter antalet piloter i gruppen när porten startar.

| Piloter i gruppen | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| 4 | 14 400 000 | 21 600 000 | 36 000 000 |
| 5 | 18 000 000 | 27 000 000 | 45 000 000 |
| 6 | 21 600 000 | 32 400 000 | 54 000 000 |
| 7 | 25 200 000 | 37 800 000 | 63 000 000 |
| 8 | 28 800 000 | 43 200 000 | 72 000 000 |
| 9 | 32 400 000 | 48 600 000 | 81 000 000 |
| 10 | 36 000 000 | 54 000 000 | 90 000 000 |

<!-- dungeons-boss:end -->

### Det låsta rummet {#the-locked-room}

Dörren till krigsherrens rum är stängd från det ögonblick porten öppnas, och medan den är stängd kan krigsherren inte skadas: ingen laser, raket eller explosion träffar honom, och han använder ingen förmåga. Dörren öppnas för gott när gruppen har förstört **väktarna**: Gate Crystalys och Gate Crystalys Twin som porten skapades med, ungefär en femtedel av dess utomjordingar. Gate Goombah och Gate Pirate räknas inte, inte heller bytezonernas vågor eller de Goombahs som krigsherren kallar på.

Fönstret Klanport räknar väktarna som är kvar och säger, i en bricka, att krigsherren inte kan skadas, och ett meddelande talar om när rummet låses upp. En flock väktare som fortfarande sover räknas fullt ut, så gruppen måste utforska labyrinten och hitta alla. På minikartan är dörren en röd linje medan den är låst och en grön när den är öppen. En port är aldrig en fälla: tidsgränsen avslutar ändå en port vars sista väktare inte går att hitta, och en administratör kan låsa upp rummet i en port som har kört fast.

### Hans förmågor {#its-abilities}

- **Den röda ringen** för Livsstjälande aura skadar varje pilot i den och läker krigsherren med skadan. Sköldabsorptionen har också en röd ring: den dränerar sköldarna på piloterna därinne och laddar krigsherrens. I båda fallen ska du lämna ringen eller ställa dig bakom en vägg.
- **De bärnstensfärgade ringarna** för Meteorregn visar var meteorerna slår ner ett ögonblick senare. Fortsätt röra dig och lämna ringen innan den slår ner.
- **Fokus på mest efterlysta** markerar piloten som har gjort mest skada på krigsherren, med en guldfärgad parentes på dennes skepp, och krigsherren skjuter ett extra skott mot piloten varje sekund så länge det varar. Hans sikte ändras inte: han fortsätter skjuta på närmaste pilot han kan se, så en markerad pilot som också är närmast får båda. Det extra skottet kräver fri sikt och räckvidden hos krigsherrens laser, så en vägg eller lite avstånd räddar piloten. Förmågan börjar inte medan ingen har gjort skada.
- **Raketsalvan** skickar målsökande raketer mot slumpmässiga piloter, men bara mot piloter som krigsherren kan se, och en vägg i vägen stoppar en raket. En ring visar vilken pilot en raket följer. En EMP Charge eller kamouflage skakar av dem.
- **Svärmhjälpen** är krigsherren som kallar på sina Goombahs. Medan de lever kan han inte skadas, och han skjuter inte och använder ingen annan förmåga. Förstör dem alla: banderollen räknar hur många som är kvar. Om en minut går kan krigsherren skadas igen, och de Goombahs som är kvar stannar och kämpar vidare. De är inte väktare, och de betalar ingenting.
- **Kaoszonen** är en violett ring på marken, runt platsen där krigsherren stod när han kastade den. Ingen inne i ringen kan attackera, varken med lasrar eller raketer, men reparationer, kamouflage och flygning fungerar fortfarande, och krigsherren och hans utomjordingar skjuter som vanligt. Ringen syns ett ögonblick innan den tar verkan: kliv ut ur den och skjut in utifrån.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Förmåga | Förberedelse | Varar | Återhämtning | Ringens radie (enheter) | Krigsherren återfår högst |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Livsstjälande aura** | 2 s | 15 s | 2 min | 900 | 8 % av skrov och sköld |
| **Meteorregn** | 1,5 s | 3 salvor, 4 s emellan | 2 min | 420 | – |
| **Fokus på mest efterlysta** | 1 s | 20 s | 2 min | – | – |
| **Raketsalva** | 1,5 s | 45 s | 2 min | – | – |
| **Sköldabsorption** | 2 s | 15 s | 2 min | 900 | 6 % av skölden |
| **Svärmhjälp** | 2 s | Upp till 1 min | 3 min | – | – |
| **Kaoszonen** | 2 s | 15 s | 2 min | 900 | – |

| Förmåga | Steg 1 | Steg 2 | Steg 3 |
| :--- | :--- | :--- | :--- |
| **Livsstjälande aura** | 8 000 per sekund | 10 000 per sekund | 12 000 per sekund |
| **Meteorregn** | 6 meteorer per salva, 40 000 vardera | 8 meteorer per salva, 50 000 vardera | 10 meteorer per salva, 60 000 vardera |
| **Fokus på mest efterlysta** | 18 750–22 500 per extra skott mot piloten som gjort mest skada, ett var 1 s | 22 500–26 250 per extra skott mot piloten som gjort mest skada, ett var 1 s | 30 000–37 500 per extra skott mot piloten som gjort mest skada, ett var 1 s |
| **Raketsalva** | 6 500 per raket, en var 15 s | 8 125 per raket, en var 15 s | 9 750 per raket, en var 15 s |
| **Sköldabsorption** | 10 000 sköld per sekund | 12 500 sköld per sekund | 15 000 sköld per sekund |
| **Svärmhjälp** | 12 × Goombah | 18 × Goombah | 24 × Goombah |
| **Kaoszonen** | Piloter i ringen kan inte attackera | Piloter i ringen kan inte attackera | Piloter i ringen kan inte attackera |

<!-- dungeons-abilities:end -->

## Bytezoner {#loot-zones}

En ring på labyrintens golv markerar varje bytezon så fort gruppen har hittat den. Stå en stund inne i den så vaknar zonen, och en våg utomjordingar kommer mot den. Då måste gruppen **hålla** zonen: ha kvar en pilot inne tills stapeln är full. Ju fler piloter i ringen, desto snabbare fylls stapeln: en siffra bredvid stapeln säger hur många gånger snabbare, och tabellen nedan ger tiderna. Tillräckligt många utomjordingar i ringen stoppar stapeln (listan nedan säger hur många), och den går tillbaka medan ingen är inne, så rensa vågen först. När zonen öppnas ser gruppen tre olika kort och **röstar** om ett. En zon öppnas bara en gång, och dess våg kommer inte tillbaka.

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Bytezoner**: 6 i varje labyrint
- **Radie**: 450 enheter
- **Väckning**: Stå inne i ringen i 2 s
- **Hålla**: Håll en pilot inne i 30 s. Mätaren stannar medan 3 eller fler utomjordingar är i ringen och går tillbaka medan ingen är inne
- **Välja**: Gruppen har 45 s på sig att rösta. Omröstningen slutar tidigare om varje närvarande pilot har röstat eller ett kort har mer än hälften av rösterna

Fler piloter i ringen håller en zon snabbare. Så lång tid tar det att hålla en zon:

| Piloter i ringen | Tid för att hålla zonen |
| :--- | ---: |
| 1 | 30 s |
| 2 | 20 s |
| 3 | 15 s |
| 4 | 12 s |
| 5 eller fler | 10 s |

<!-- dungeons-zones:end -->

### Boosters

Vid steg 2 och 3 ger bytezonernas vågor också boosters. När gruppen har förstört varenda utomjording i en våg räknas vågen, och efter var annan våg (den andra, den fjärde och den sjätte) får varje pilot ett fönster på en halv minut för att välja en tillfällig booster åt sig själv: **Skada** (dina lasrar slår hårdare), **Träffpoäng** (ditt skepp tål mer skrov) eller **Hastighet** (ditt skepp flyger snabbare). Tryck på ett kort för att välja det. Om du inte svarar i tid väljer spelet Träffpoäng åt dig. Ett val är värt 3 % vid steg 3 och 1,5 % vid steg 2, och en sort adderas upp till högst 9 % vid steg 3 och 4,5 % vid steg 2, hur ofta du än väljer den. Steg 1 har inga boosters. En grupp som lämnar en våg vid liv får inget fönster för den.

En booster varar tills porten är avklarad. Om du lämnar porten, eller blir förstörd, förlorar du dina boosters, och du får tillbaka dem när du flyger in igen. En bricka under fönstret Klanport listar vad du har.

### Korten {#the-cards}

Korten dras ett i taget ur poolen nedan. Chansen är ett korts chans i en dragning. Varje kort går till varje pilot som får betalt, utrustningskorten också: ett kort med många exemplar ger var och en lika många, och ett utrustningskort ger var och en ett eget stycke, smitt särskilt för var och en. En pilot som inte får betalt får inte heller något kort, och en zon som öppnats i en port som misslyckas betalar ingenting.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Kort | Steg 1 | Steg 2 | Steg 3 | Chans | Går till |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2 000 | 3 000 | 5 000 | 23,9 % | Varje betald pilot |
| Velkonite Reinforced Plate | 10 | 15 | 25 | 13,65 % | Varje betald pilot |
| Velkonite | 200 | 300 | 500 | 13,65 % | Varje betald pilot |
| Orvium | 200 | 300 | 500 | 13,65 % | Varje betald pilot |
| Ultra Core | 5 000 | 7 500 | 12 500 | 11,4 % | Varje betald pilot |
| Experimental Fusion Core | 3 000 | 4 500 | 7 500 | 9,1 % | Varje betald pilot |
| Dark Matter | 5 | 8 | 12 | 9,1 % | Varje betald pilot |
| Dark Matter Plate | 1 | 1 | 2 | 4,55 % | Varje betald pilot |
| Starfire-III | – | – | 1 | 0,07 % | Varje betald pilot |
| Helios Beam | – | – | 1 | 0,07 % | Varje betald pilot |
| Engine III | – | – | 1 | 0,07 % | Varje betald pilot |
| Adaptive Core III | – | – | 1 | 0,07 % | Varje betald pilot |
| Heavy Shield Core | – | – | 1 | 0,07 % | Varje betald pilot |
| Momentum Thruster IV | – | – | 1 | 0,07 % | Varje betald pilot |
| Impulse Thruster IV | – | – | 1 | 0,07 % | Varje betald pilot |
| Hull Plating II | – | – | 1 | 0,07 % | Varje betald pilot |
| Hull Plating III | – | – | 1 | 0,07 % | Varje betald pilot |
| Damage Amp IV | – | – | 1 | 0,07 % | Varje betald pilot |
| Crit Amp IV | – | – | 1 | 0,07 % | Varje betald pilot |
| Penetration Amp IV | – | – | 1 | 0,07 % | Varje betald pilot |
| Capacity Shield Cell IV | – | – | 1 | 0,08 % | Varje betald pilot |
| Absorption Shield Cell IV | – | – | 1 | 0,08 % | Varje betald pilot |

- **Utrustning**: Korten med ett enda exemplar är utrustning: tillsammans 1 % av korten

<!-- dungeons-cards:end -->

Korten med ett exemplar är **utrustning**, och bara en port av steg 3 kan erbjuda dem. Ett utrustningsstycke smids för varje pilot som får betalt när det betalas ut: var och en slår en egen [förtrollningsnivå](/wiki/06-Items/Overview.md#item-enchants) med samma chanser som ett stycke du bygger i Monteringen, så de flesta blir Standard, och en högre nivå, upp till Evig, med bonusar, är ett sällsynt fynd.

## Betalning {#pay}

När krigsherren faller får varje pilot som förtjänat det betalt, en gång per genomförd omgång. Korten som gruppen valde kommer ovanpå stegets betalning. Det finns ingen världsmultiplikator: betalningen är densamma i varje värld.

**Orvium Reinforced Plates** är inte ett kort i omröstningen. De hör till stegets betalning, och varje betald pilot får dem en gång för klarningen. Föremålen som en port betalar är inte säljbara: du kan inte [sälja dem på Auktionen](/wiki/03-Mechanics/Auction.md#marketable-items).

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Steg | Heder | Erfarenhet | Krediter | Thulium | x4-ammunition | Orvium Reinforced Plates | PvE-rankingpoäng |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Steg 1** | 25 000 | 600 000 | 5 000 000 | 4 000 | 4 000 | 5 | 600 |
| **Steg 2** | 50 000 | 1 500 000 | 10 000 000 | 9 000 | 9 000 | 10 | 1 500 |
| **Steg 3** | 100 000 | 2 400 000 | 17 500 000 | 15 000 | 15 000 | 15 | 2 400 |

<!-- dungeons-pay:end -->

### Vem som får betalt {#who-is-paid}

Utomjordingarna betalar aldrig. En omgång spelas klart även när den inte betalar något, och resultatskärmen säger varför. Inträde nekas aldrig för att du redan fått betalt för ett steg: den omgången betalar bara ingenting.

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **En dag**: Ett steg betalar en pilot en gång per UTC-dag: den dag då krigsherren faller
- **En vecka**: En pilot får betalt för högst 10 avklarade steg per UTC-vecka, måndag till söndag
- **Inne**: Minst 2 min totalt
- **Del i striden**: Minst ett av dessa: orsakat 2 % av krigsherrens skrov och sköld; förstört 10 av portens utomjordingar; läkt andra piloter för 50 000 under striden mot krigsherren

<!-- dungeons-rules:end -->

### Vad en dag och en vecka är värda {#what-a-day-and-a-week-are-worth}

Vad en pilot kan få betalt på en dag, och under den bästa vecka som gränserna tillåter. Sista kolumnen är vad betalningen lägger till dina [PvE-poäng](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points).

<!-- dungeons-totals:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Betalning per pilot | Heder | Erfarenhet | Krediter | Thulium | x4-ammunition | Orvium Reinforced Plates | PvE-rankingpoäng |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| En dag, varje steg en gång | 175 000 | 4 500 000 | 32 500 000 | 28 000 | 28 000 | 30 | 4 500 |
| Den bästa veckan: 7 × Steg 3 och 3 × Steg 2 | 850 000 | 21 300 000 | 152 500 000 | 132 000 | 132 000 | 135 | 21 300 |

Erfarenheten från ett betalt, avklarat steg räknas med i dina PvE-rankingpoäng: en poäng för varje 1 000 erfarenhet.

<!-- dungeons-totals:end -->

## Klanbankens belöning {#clan-bank-reward}

Klanbanken får också betalt, i krediter och inte i Thulium, första gången klanen klarar ett steg under en säsong. Klanen måste vara gammal nog, och tillräckligt många piloter i den omgången måste få betalt. Banken får betalt en gång per steg under en säsong.

<!-- dungeons-clan:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Steg | Krediter till klanbanken |
| :--- | ---: |
| **Steg 1** | 10 000 000 |
| **Steg 2** | 20 000 000 |
| **Steg 3** | 30 000 000 |

- **Klanens ålder**: Minst 3 d
- **Betalda piloter**: Minst 3 i porten

<!-- dungeons-clan:end -->

## Tips

- Rensa en zons våg innan du försöker hålla zonen, och strid inne i ringen om utomjordingar kommer in.
- Ta med hela gruppen till en zon: ju fler piloter i ringen, desto snabbare hålls den.
- Utforska varje hörn av labyrinten: en flock väktare som du aldrig hittar håller krigsherrens dörr stängd.
- Använd väggarna: lasrar går inte igenom dem, de röda ringarna från krigsherrens auror slutar vid dem, och en vägg stoppar också krigsherrens raketer.
- Spara en EMP Charge till Raketsalvan.
- När krigsherren kallar på sina Goombahs, förstör dem först: han kan inte skadas förrän de är borta. Kliv ut ur ringen innan du skjuter i Kaoszonen.
- Håll koll på klockan i fönstret Klanport. När tiden tar slut misslyckas porten och betalar ingenting.
