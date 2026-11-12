<!-- wiki-i18n source: fe0e51ce5e04b430 -->
<!-- wiki-i18n title: Dungeons -->
# Dungeons

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; portal; clan portal; join; clan gate alerts; clan dungeon window; clan dungeon alerts; dungeon goombah; dungeon pirate; dungeon crystalys; dungeon warlord; 75 percent; three quarters; start room; fog; guards; locked room; boss room; booster; boosters; swarm assist; focus most wanted; zone of chaos; rocket barrage; dungeon; dungeons; krigsherre; labyrint; steg; bytezon; kort; portal; klanportal; booster; dimma; väktare; startrum; låst rum; svärmhjälp; kaoszon; klanens dungeonaviseringar; klandungeon; klanens dungeonaviseringar; tre fjärdedelar; 75 procent -->

En **dungeon** är en sluten labyrint med en **krigsherre** i änden (före 0.5.2 kallade spelet den port). En vice ledare eller ledaren i en [klan](/wiki/03-Mechanics/Clans.md) öppnar en och betalar för den ur klanbanken, och klanens medlemmar flyger in tillsammans som en [grupp](/wiki/03-Mechanics/Groups.md). De kämpar sig igenom labyrintens utomjordingar, öppnar bytezoner för att välja ett kort i var och en och fäller krigsherren. Varje pilot som deltog i striden får betalt när krigsherren faller, inom gränserna längre ner. Dungeonerna finns på fliken **Dungeons** på klansidan.

En dungeon är en strid enbart mot utomjordingarna: ingen kan attackera en klankamrat eller någon annan därinne. Utomjordingarna betalar när de faller, som utomjordingarna i spelet som de är byggda efter ([vad utomjordingarna betalar](#what-the-aliens-pay)). Klarningen tillhör krigsherren, så det enda sättet att få betalt för den är att vara med i striden när den faller.

En dungeon är inte en [soloport](/wiki/03-Mechanics/Solo-Gates.md). En soloport är en arena som bara du flyger in i, öppnad med delar du hittar med Energimaterialiseraren; de två har skilda regler, utbetalningar och gränser.

## I korthet {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Öppnar**: Från säsongsdag 1
- **Vem som öppnar en dungeon**: En vice ledare eller ledaren, som betalar priset ur klanbanken
- **Grupp**: 4 till 10 medlemmar av klanen, i en grupp
- **Dungeons per dag**: 3 per klan och UTC-dag, en öppen åt gången
- **Dungeons samtidigt**: 6 i en värld
- **Kartor**: Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Labyrinter**: 8; en väljs när en dungeon öppnas
- **Bossrummet**: Öppnas när 75 % av Crystalys och deras Twins är förstörda, avrundat uppåt
- **Samling**: 10 min att samlas och starta. En dungeon som ingen startar stängs, och dess pris går tillbaka till klanbanken
- **Tidsgräns**: Steg 1: 95 min, Steg 2: 130 min, Steg 3: 165 min från starten. När tiden tar slut misslyckas dungeonen och klarningen betalar ingenting
- **Lämnad tom**: En dungeon där ingen är inne på 3 min misslyckas
- **När krigsherren faller**: Dungeonen förblir öppen i 2 min för piloterna som är inne
- **Komma tillbaka**: En pilot som har lämnat dungeonen eller blivit förstörd kan flyga in igen hur många gånger som helst, med minst 20 s emellan

<!-- dungeons-glance:end -->

## Hur en omgång går till {#how-a-run-goes}

1. **Kalla fram.** På fliken Dungeons väljer en [vice ledare eller ledaren](/wiki/03-Mechanics/Clans.md#hierarchy-roles) ett steg och trycker på **Kalla fram**. Priset tas ur [klanbanken](/wiki/03-Mechanics/Clans.md#clan-economy-taxation), och dungeonen får en av kartorna som listas ovan. En dungeon som ingen startar stängs, och priset går tillbaka till banken.
2. **Gå in.** Klanens medlemmar trycker på **Gå in** i klanfönstret medan de flyger, hoppar genom klanportalen eller trycker på **Gå med** på aviseringskortet (se Gå in). Alla landar i startrummet, och piloterna därinne är dungeonens grupp.
3. **Starta.** Startrummet är ett litet rum i ena änden av labyrinten, och dess dörr är stängd medan dungeonen samlas. Det finns inga utomjordingar där, så det är säkert att vänta. Dungeonen **startar av sig själv** när varje pilot den väntar på är inne och gruppen är tillräckligt stor. Den väntar på klanens medlemmar som är online, inte borta och i gruppen hos en pilot som har gått in, och den startar genast när gruppen är full. Piloten som öppnade dungeonen, eller en officer, kan trycka på **Starta** för att börja tidigare med de piloter som är inne, om de är tillräckligt många. En pilot som lämnar väntas inte längre på. När dungeonen startar öppnas dörren för gott, och därefter kan bara piloter som redan var inne komma tillbaka.
4. **Kämpa dig genom labyrinten.** Du kommer in i ena änden av labyrinten och krigsherren väntar i den andra, i ett låst rum. Labyrinten är mörk: du ser bara det gruppen har utforskat och det som är nära dess skepp. Utomjordingarna väntar i flockar i korridorerna, och en flock kommer ut i samma ögonblick som en pilot flyger in i den korridorsträcka där den väntar, och jagar sedan gruppen genom labyrinten.
5. **Öppna bytezonerna.** Ringar i labyrinten markerar zonerna. Håll en och gruppen röstar om ett kort, som betalas ut tillsammans med krigsherrens betalning.
6. **Lås upp bossrummet.** Förstör tre fjärdedelar av labyrintens Crystalys och deras Twins, så öppnas dörren till krigsherrens rum. Tills dess kan krigsherren inte skadas. De andra utomjordingarna blir kvar där de är, och du kan förstöra dem också.
7. **Besegra krigsherren.** Bryt hans sköld och skrov och svara på hans förmågor. När han faller är dungeonen avklarad.
8. **Få betalt.** Betalningen kommer i samma ögonblick som krigsherren faller. Dungeonen står öppen en stund till för piloterna därinne och stängs sedan.

## Gå in {#entering}

För att gå in i en dungeon behöver du ett **skepp i flykt**, så starta först och öppna sedan klanfönstret, och en [grupp](/wiki/03-Mechanics/Groups.md) med tillräckligt många klanmedlemmar. Du behöver också den **nivå** som steget kräver, och du får inte redan vara inne i en annan dungeon. Dungeonens grupp har en storleksgräns: när den är full kan ingen annan gå in.

En vice ledare eller ledaren öppnar en dungeon, en i taget för klanen, och bara upp till antalet dungeons per dag. Klanbanken måste ha priset. En klan kan öppna ett steg först när den har klarat steget före.

Inne i en dungeon kan du inte byta värld, och Jump CPU och Base CPU fungerar inte. Knappen **Lämna** i fönstret Klandungeon tar ut dig. Den ber först om bekräftelse, utom när krigsherren redan har fallit: då går du ut direkt. En pilot som har lämnat, eller blivit förstörd, kan flyga in igen; listan under **I korthet** säger hur många gånger och hur länge han väntar mellan två återvändanden.

### Klanportalen och aviseringen {#the-clan-portal-and-the-call}

När en dungeon öppnas får klanen en **portal** till den på varje koncerns hemkarta (`M-1`, `T-1` och `G-1`), en bit utanför stationens säkra zon. Bara klanens piloter ser den: för alla andra finns den inte. Den har ingen egen säker zon. Flyg fram till den och hoppa som vid vilken portal som helst, så tar den dig in i dungeonen enligt reglerna för **Gå in**: ett skepp i flykt, en grupp med tillräckligt många klanmedlemmar, stegets nivå och plats i gruppen. När dungeonen har startat kan bara piloter som redan var inne använda den. Portalen försvinner när dungeonen är över.

Medan din klans dungeon samlas och du flyger någon annanstans får du en **avisering**: ett kort högst upp på flygskärmen, med ett ljud. Det säger vem som öppnade dungeonen, hur många piloter som är inne och hur länge dungeonen står öppen. **Gå med** flyger in dig, som **Gå in** på fliken Dungeons, och när du lämnar dungeonen kommer ditt skepp tillbaka dit det var. Gå med är nedtonad medan din grupp är för liten. **Inte nu** döljer kortet för den dungeonen. Om din grupp redan är inne och dungeonen väntar på dig står det på kortet. Kortet når klanens piloter som flyger (inte dem som är dockade vid en station) och som har den nivå steget kräver. Du kan stänga av kortet och dess ljud med **Klanens dungeonaviseringar** i Inställningar › Allmänt › Grupper.

### Fönstret Klandungeon {#the-clan-dungeon-window}

Inne i en dungeon har omgången ett eget fönster, **Klandungeon**. Det visar tiden som har gått och det som är kvar, hur många utomjordingar som flyger och hur många som har förstörts, vad gruppen ska göra nu (utforska labyrinten, hålla en zon, hitta bossen, förstöra tre fjärdedelar av Crystalys och deras Twins, besegra krigsherren), hållstapeln medan du står i en zon, krigsherrens förmåga med nedräkningen och knappen **Lämna**. Det är ett fönster som de andra: dra det i titelraden och stäng det med det röda ljuset i hörnet. Det öppnas av sig självt när du går in i en dungeon, en gång för varje dungeon: om du stänger det förblir det stängt till nästa dungeon. Verktygsfältet har en knapp **Klandungeon** för det medan du är i en dungeon. Medan fönstret är stängt visas en förmåga hos krigsherren som snart startar eller är igång som ett enradigt fält med namnet och nedräkningen. Klicka på fältet för att öppna fönstret igen. Medan en omröstning om belöningen eller ett val av booster är öppet och dess fönster stängt har fönstret Klandungeon en rad för det, med dess nedräkning och en knapp **Välj** som öppnar det igen.

## Stegen {#the-stages}

En dungeon har ett steg, och steget är dess svårighet. Ett högre steg har segare utomjordingar som slår hårdare, och det betalar mer. Faktorerna i tabellen är utomjordingarnas. Skada betyder deras lasrar och raketer. Krigsherren följer inte tabellen: han har egna tal för varje steg, längre ned. Tabellen säger också hur många utomjordingar ett steg skickar jämfört med det första. **Priset** tas ur klanbanken när dungeonen öppnas.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Steg | Kräver | Utomjordingarnas skrov och sköld | Antal utomjordingar | Utomjordingarnas skada | Dungeonens pris (krediter, ur klanbanken) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Steg 1** | Från nivå 6 | ×1 | ×1 | ×1 | 500 000 |
| **Steg 2** | Från nivå 7 | ×1,5 | ×1 | ×1,5 | 1 000 000 |
| **Steg 3** | Från nivå 8 | ×2 | ×1 | ×2 | 2 000 000 |

<!-- dungeons-stages:end -->

## Labyrinten {#the-maze}

Varje dungeon är en sluten labyrint på en egen karta, en av kartorna i listan ovan, och labyrinten är en av flera utformningar. Labyrinten fyller hela kartan, från kant till kant: ett rutnät av rum och korridorer med massiva väggar. Skepp kan inte passera en vägg, och en vägg blockerar skott, så den är skydd. En meteor faller uppifrån, och en vägg stoppar den inte.

**Rum och dörrar.** Startrummet, där du landar, och krigsherrens rum, i andra änden, har var sin dörr. En stängd dörr är en vägg för skepp, skott och utomjordingar likadant. Startdörren öppnas när dungeonen startar. Krigsherrens dörr förblir låst tills tre fjärdedelar av Crystalys och deras Twins är förstörda (se [Det låsta rummet](#the-locked-room)). Mellan dem har labyrinten ett bytesrum för varje bytezon.

**Dimma.** Labyrinten är mörk. I flykt ser du dess väggar och utomjordingar bara där gruppen har varit, och en kort bit runt varje skepp i gruppen. Ett rum räknas som utforskat så fort en av er är i det. Minikartan fungerar likadant: en karta över hela våningen som fylls i allteftersom gruppen utforskar den, med ingången, krigsherrens dörr, de zoner ni har hittat och krigsherren när ni har hittat honom. Piloterna i din egen grupp visas alltid.

## Utomjordingarna {#the-aliens}

Fyra sorters utomjordingar vaktar labyrinten. De väntar i flockar i korridorerna, aldrig i ett rum, och en flock kommer ut i samma ögonblick som en pilot flyger in i den korridorsträcka där den väntar. Där ingen pilot har varit finns inget på kartan, så ingen flock står bakom väggarna djupt inne i labyrinten innan du kommer dit. En flock väntar inte på plats: den är på kartan i samma ögonblick, hur många utomjordingar som än redan är ute. En korridorsträcka rymmer en flock, så på den sträcka du flyger in i möter du en flock och inte summan av flera (en grupp på tio har fler flockar än sträckor, och där rymmer en sträcka två, som båda kommer ut). En flock som är ute väntar inte på dig: den jagar gruppen genom labyrinten, och en flock som tappar alla går tillbaka dit den kom ut och läker. En flock kommer ut bara en gång: en du förstör kommer inte tillbaka, och en du flyger ifrån blir kvar på kartan. Vågorna i bytezonerna är annorlunda: dungeonen håller bara ett visst antal utomjordingar i luften åt gången, och det antalet växer med gruppens storlek, så en våg som skulle passera det väntar på plats, och en flock du förstör släpper in nästa våg. En större grupp möter fler utomjordingar, i proportion, en mindre färre, och en sorts utomjording faller aldrig under en.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Utomjordingar, för en grupp på 5 | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| Dungeon Goombah | 156 | 156 | 156 |
| Dungeon Pirate | 34 | 34 | 34 |
| Dungeon Crystalys | 34 | 34 | 34 |
| Dungeon Crystalys Twin | 11 | 11 | 11 |
| Tillsammans | 235 | 235 | 235 |
| För att öppna bossrummet | 34 | 34 | 34 |
| Vågen i en bytezon | 12 × Dungeon Goombah och 1 × Dungeon Crystalys | 12 × Dungeon Goombah och 1 × Dungeon Crystalys | 12 × Dungeon Goombah och 1 × Dungeon Crystalys |

- **Vågen i en bytezon väntar på plats**: När 10 per pilot i gruppen lever, eller 70 totalt

<!-- dungeons-population:end -->

Varje sort i tur och ordning. Skrov och sköld är de vanliga värdena gånger multiplikatorn för steget i kolumnen.

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Dungeon Goombah

- **Ser ut som**: Goombah
- **Flyger i flockar om**: 6
- **Belöning och byte som**: Goombah

|  | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| Skrov | 32 000 | 48 000 | 64 000 |
| Sköld | 48 000 | 72 000 | 96 000 |
| Laserskada (en salva per sekund) | 3 000 | 4 500 | 6 000 |
| Hastighet | 180 | 180 | 180 |
| Laserräckvidd | 800 | 800 | 800 |
| Aggroradie | 1 800 | 1 800 | 1 800 |
| Belöning och byte, gånger originalets | ×1 | ×1,5 | ×2 |
| Krediter för varje förstörd | 15 000 | 22 500 | 30 000 |
| Thulium för varje förstörd | 75 | 113 | 150 |
| Erfarenhet för varje förstörd | 3 000 | 4 500 | 6 000 |
| Heder för varje förstörd | 24 | 36 | 48 |

### Dungeon Pirate

- **Ser ut som**: Pirate Boss
- **Flyger i flockar om**: 2
- **Belöning och byte som**: Pirate Boss
- **Raket**: En rak raket var 5 s, räckvidd 1 000 enheter

|  | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| Skrov | 250 000 | 375 000 | 500 000 |
| Sköld | 50 100 | 75 150 | 100 200 |
| Laserskada (en salva per sekund) | 200 | 300 | 400 |
| Raketskada | 5 000 | 7 500 | 10 000 |
| Hastighet | 100 | 100 | 100 |
| Laserräckvidd | 700 | 700 | 700 |
| Aggroradie | 1 800 | 1 800 | 1 800 |
| Belöning och byte, gånger originalets | ×1 | ×1,5 | ×2 |
| Krediter för varje förstörd | 145 000 | 217 500 | 290 000 |
| Thulium för varje förstörd | 725 | 1 088 | 1 450 |
| Erfarenhet för varje förstörd | 29 000 | 43 500 | 58 000 |
| Heder för varje förstörd | 232 | 348 | 464 |

### Dungeon Crystalys

- **Ser ut som**: Crystalys
- **Flyger i flockar om**: 2
- **Belöning och byte som**: Crystalys

|  | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| Skrov | 256 000 | 384 000 | 512 000 |
| Sköld | 160 000 | 240 000 | 320 000 |
| Laserskada (en salva per sekund) | 10 000 | 15 000 | 20 000 |
| Hastighet | 230 | 230 | 230 |
| Laserräckvidd | 900 | 900 | 900 |
| Aggroradie | 2 400 | 2 400 | 2 400 |
| Belöning och byte, gånger originalets | ×1 | ×1,5 | ×2 |
| Krediter för varje förstörd | 75 000 | 112 500 | 150 000 |
| Thulium för varje förstörd | 200 | 300 | 400 |
| Erfarenhet för varje förstörd | 12 000 | 18 000 | 24 000 |
| Heder för varje förstörd | 52 | 78 | 104 |

### Dungeon Crystalys Twin

- **Ser ut som**: Crystalys, 1,4 gånger så stor
- **Flyger i flockar om**: 1
- **Belöning och byte som**: Crystalys

|  | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| Skrov | 512 000 | 768 000 | 1 024 000 |
| Sköld | 320 000 | 480 000 | 640 000 |
| Laserskada (en salva per sekund) | 20 000 | 30 000 | 40 000 |
| Hastighet | 230 | 230 | 230 |
| Laserräckvidd | 900 | 900 | 900 |
| Aggroradie | 2 400 | 2 400 | 2 400 |
| Belöning och byte, gånger originalets | ×2 | ×3 | ×4 |
| Krediter för varje förstörd | 150 000 | 225 000 | 300 000 |
| Thulium för varje förstörd | 400 | 600 | 800 |
| Erfarenhet för varje förstörd | 24 000 | 36 000 | 48 000 |
| Heder för varje förstörd | 104 | 156 | 208 |

<!-- dungeons-enemies:end -->

## Krigsherren {#the-warlord}

Krigsherren väntar i rummet i andra änden av labyrinten, och hans fall är det som betalar klarningen. Han betalar ingen egen förstörd utomjording, som de andra utomjordingarna gör. Han är en Crystalys som vuxit enorm. Hans skrov och sköld växer med gruppens storlek: ju fler piloter som går in, desto segare är han, i proportion. Han lämnar aldrig sitt rum, vare sig dörren är stängd eller öppen: han håller sig innanför rummets väggar och jagar inte genom korridorerna. En pilot utanför kan bara locka honom till kanten av rummet, och genom en öppen dörr skjuter han ändå på allt hans laser når. Han använder sina förmågor en i taget, i slumpmässig ordning, var och en med sin egen återhämtningstid.

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

Skrovet och skölden ovan gäller för en grupp på 5. De växer med gruppen: det är krigsherrens skrov och sköld tillsammans, efter antalet piloter i gruppen när dungeonen startar.

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

Dörren till krigsherrens rum är stängd från det ögonblick dungeonen öppnas, och medan den är stängd kan krigsherren inte skadas: ingen laser, raket eller explosion träffar honom, och han använder ingen förmåga. Dörren öppnas för gott när **tre fjärdedelar av Crystalys och deras Twins** som dungeonen skapades med är förstörda, avrundat uppåt (tabellen över utomjordingarna ovan räknar dem för en grupp på 5, och dess sista rad säger hur många det krävs). Det som räknas är Crystalys och Twins i labyrintens flockar, och vem som än förstör dem. En flock kommer bara ut när en pilot flyger in i dess korridorsträcka, så gruppen måste hitta tillräckligt många för att öppna dörren. De andra utomjordingarna, bytezonernas vågor, de Goombahs som krigsherren kallar på och krigsherren själv räknas inte för dörren.

Fönstret Klandungeon räknar hur många av dem som fortfarande måste förstöras för att öppna rummet och säger, i en bricka, att krigsherren inte kan skadas, och ett meddelande talar om när rummet låses upp. En flock som ännu inte har kommit ut räknas fullt ut, så gruppen måste hitta Crystalys och deras Twins i labyrinten och flyga in i deras korridorsträckor. **De andra utomjordingarna försvinner inte när dörren öppnas.** De blir kvar i labyrinten, kommer ut när en pilot flyger in i deras korridorsträcka och kan förstöras som förut, så en grupp som vill kan förstöra alla innan den möter krigsherren: räknaren för utomjordingar i fönstret går vidare till alla utomjordingar som dungeonen skapades med och står full när ingen är kvar. De betalar när de faller ([vad utomjordingarna betalar](#what-the-aliens-pay)), och de som fortfarande lever när krigsherren faller försvinner med dungeonen. På minikartan är dörren en röd linje medan den är låst och en grön när den är öppen. En dungeon är aldrig en fälla: tidsgränsen avslutar ändå en dungeon vars dörr förblir stängd, och en administratör kan låsa upp rummet i en dungeon som har kört fast.

### Hans förmågor {#its-abilities}

- **Den röda ringen** för Livsstjälande aura skadar varje pilot i den och läker krigsherren med skadan. Sköldabsorptionen har också en röd ring: den dränerar sköldarna på piloterna därinne och laddar krigsherrens. I båda fallen ska du lämna ringen eller ställa dig bakom en vägg.
- **De bärnstensfärgade ringarna** för Meteorregn visar var meteorerna slår ner ett ögonblick senare. Fortsätt röra dig och lämna ringen innan den slår ner.
- **Fokus på mest efterlysta** markerar piloten som har gjort mest skada på krigsherren, med en guldfärgad parentes på dennes skepp, och krigsherren skjuter ett extra skott mot piloten varje sekund så länge det varar. Hans sikte ändras inte: han fortsätter skjuta på närmaste pilot han kan se, så en markerad pilot som också är närmast får båda. Det extra skottet kräver fri sikt och räckvidden hos krigsherrens laser, så en vägg eller lite avstånd räddar piloten. Förmågan börjar inte medan ingen har gjort skada.
- **Raketsalvan** skickar målsökande raketer mot slumpmässiga piloter, men bara mot piloter som krigsherren kan se, och en vägg i vägen stoppar en raket. En ring visar vilken pilot en raket följer. En EMP Charge eller kamouflage skakar av dem.
- **Svärmhjälpen** är krigsherren som kallar på sina Goombahs. Medan de lever kan han inte skadas, och han skjuter inte och använder ingen annan förmåga. Förstör dem alla: banderollen räknar hur många som är kvar. Om en minut går kan krigsherren skadas igen, och de Goombahs som är kvar stannar och kämpar vidare. De räknas inte för bossrummet, och de betalar ingenting.
- **Kaoszonen** är en violett ring på marken, runt krigsherren, och så länge den varar följer den med krigsherren vart han än går. Ingen inne i ringen kan attackera, varken med lasrar eller raketer, men reparationer, kamouflage och flygning fungerar fortfarande, och krigsherren och hans utomjordingar skjuter som vanligt. Ringen syns ett ögonblick innan den tar verkan: kliv ut ur den och håll dig utanför, eftersom den följer krigsherren. En pilot utanför kan fortfarande skjuta, så långt hans vapen når.

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
| **Raketsalva** | 26 000 per raket, en var 15 s | 32 500 per raket, en var 15 s | 39 000 per raket, en var 15 s |
| **Sköldabsorption** | 10 000 sköld per sekund | 12 500 sköld per sekund | 15 000 sköld per sekund |
| **Svärmhjälp** | 12 × Goombah | 18 × Goombah | 24 × Goombah |
| **Kaoszonen** | Piloter i ringen kan inte attackera | Piloter i ringen kan inte attackera | Piloter i ringen kan inte attackera |

<!-- dungeons-abilities:end -->

## Bytezoner {#loot-zones}

En ring på labyrintens golv markerar varje bytezon så fort gruppen har hittat den. Stå en stund inne i den så vaknar zonen, och en våg utomjordingar kommer mot den. Då måste gruppen **hålla** zonen: ha kvar en pilot inne tills stapeln är full. Ju fler piloter i ringen, desto snabbare fylls stapeln: en siffra bredvid stapeln säger hur många gånger snabbare, och tabellen nedan ger tiderna. Tillräckligt många utomjordingar i ringen stoppar stapeln (listan nedan säger hur många), och den går tillbaka medan ingen är inne, så rensa vågen först. När zonen öppnas ser gruppen tre olika kort och **röstar** om ett. En zon öppnas bara en gång, och dess våg kommer inte tillbaka. Omröstningen är ett litet eget fönster på skärmens högra sida, med en rad för varje belöning: dess bild, dess namn, hur många du får och hur många röster den har. Peka på en rad för att läsa vad det är och vem som får den, och tryck på en rad för att rösta på den (tryck på en annan rad för att ändra din röst). Fönstret öppnas av sig självt för varje omröstning och täcker inte striden, så du kan flyga vidare medan gruppen väljer. Dra det vart du vill eller stäng det med det röda ljuset; knappen **Välj** i fönstret Klandungeon öppnar det igen. Din röst räknas fortfarande, och nedräkningen går vidare, medan fönstret är stängt.

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

Vid steg 2 och 3 tjänar gruppen boosters genom att förstöra dungeonens utomjordingar. En booster delas ut vid var tionde del av dem: när en tiondel av utomjordingarna är förstörd, sedan två tiondelar, och så vidare upp till alla, tio utdelningar sammanlagt. Varenda utomjording som dungeonen skapades med räknas, vem som än förstör den (det är räkningen av förstörda utomjordingar i fönstret Klandungeon); bytezonernas vågor och de utomjordingar som krigsherren kallar på räknas inte, så en zon ger ingen booster. Vid varje utdelning får varje pilot ett fönster på en halv minut för att välja en tillfällig booster åt sig själv bland tre som spelet drar slumpmässigt ur fem: **Skada** (dina lasrar slår hårdare), **Träffpoäng** (ditt skepp tål mer skrov), **Sköld** (din sköld tål mer), **Hastighet** (ditt skepp flyger snabbare) och **Sköldladdning** (din sköld laddas snabbare). Tryck på ett kort för att välja det. Om du inte svarar i tid väljer spelet Träffpoäng åt dig, eller den första av de tre om Träffpoäng inte är bland dem. Ett val är värt 3 % vid steg 3 och 1,5 % vid steg 2, så tio val adderas upp till högst trettio procent vid steg 3 och femton procent vid steg 2, vilka sorter det än är. Steg 1 har inga boosters. De tre boosterna är raderna i ett litet eget fönster, som omröstningen om belöningen: det öppnas av sig självt vid varje utdelning på skärmens högra sida, och halvminuten är dess nedräkning. Peka på en rad för att läsa vad sorten gör och hur mycket av den du redan har. Dra fönstret, stäng det med det röda ljuset eller öppna det igen med knappen **Välj** i fönstret Klandungeon.

Den tionde utdelningen kommer med den sista utomjordingen. En grupp som förstör varenda utomjording innan den möter krigsherren får alla tio utdelningarna; en grupp som öppnar krigsherrens rum och flyger vidare får utdelningarna för de utomjordingar den hittills har förstört, och de som är kvar blir kvar och kan fortfarande förstöras. När striden mot krigsherren har börjat delas ingen booster ut längre.

En booster varar tills dungeonen är avklarad. Om du lämnar dungeonen, eller blir förstörd, förlorar du dina boosters, och du får tillbaka dem när du flyger in igen. En bricka under fönstret Klandungeon listar vad du har.

### Korten {#the-cards}

Korten dras ett i taget ur poolen nedan. Chansen är ett korts chans i en dragning. Varje kort går till varje pilot som får betalt, utrustningskorten också: ett kort med många exemplar ger var och en lika många, och ett utrustningskort ger var och en ett eget stycke, smitt särskilt för var och en. En pilot som inte får betalt får inte heller något kort, och en zon som öppnats i en dungeon som misslyckas betalar ingenting.

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
| Dark Matter | 10 | 16 | 24 | 9,1 % | Varje betald pilot |
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

Korten med ett exemplar är **utrustning**, och bara en dungeon av steg 3 kan erbjuda dem. Ett utrustningsstycke smids för varje pilot som får betalt när det betalas ut: var och en slår en egen [förtrollningsnivå](/wiki/06-Items/Overview.md#item-enchants) med samma chanser som ett stycke du bygger i Monteringen, så de flesta blir Standard, och en högre nivå, upp till Evig, med bonusar, är ett sällsynt fynd.

## Betalning {#pay}

När krigsherren faller får varje pilot som förtjänat det betalt, en gång per genomförd omgång. Korten som gruppen valde kommer ovanpå stegets betalning. Det finns ingen världsmultiplikator: betalningen är densamma i varje värld.

**Orvium Reinforced Plates** är inte ett kort i omröstningen. De hör till stegets betalning, och varje betald pilot får dem en gång för klarningen. Föremålen som klarningen betalar är inte säljbara: du kan inte [sälja dem på Auktionen](/wiki/03-Mechanics/Auction.md#marketable-items).

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Steg | Heder | Erfarenhet | Krediter | Thulium | x4-ammunition | Orvium Reinforced Plates | PvE-rankingpoäng |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Steg 1** | 25 000 | 600 000 | 5 000 000 | 4 000 | 4 000 | 5 | 600 |
| **Steg 2** | 50 000 | 1 500 000 | 10 000 000 | 9 000 | 9 000 | 10 | 1 500 |
| **Steg 3** | 100 000 | 2 400 000 | 17 500 000 | 15 000 | 15 000 | 15 | 2 400 |

<!-- dungeons-pay:end -->

### Vem som får betalt {#who-is-paid}

Dessa regler avgör vem som får betalt **för klarningen**. En omgång spelas klart även när den inte betalar något, och resultatskärmen säger varför. Inträde nekas aldrig för att du redan fått betalt för ett steg: klarningen betalar bara ingenting. Utomjordingarna läser samma regler, en förstörd i taget, utom andelen i striden ([vad utomjordingarna betalar](#what-the-aliens-pay)).

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **En dag**: Ett steg betalar en pilot en gång per UTC-dag: den dag då krigsherren faller
- **En vecka**: En pilot får betalt för högst 10 avklarade steg per UTC-vecka, måndag till söndag
- **Inne**: Minst 2 min totalt
- **Del i striden**: Minst ett av dessa: orsakat 2 % av krigsherrens skrov och sköld; förstört 10 av dungeonens utomjordingar; läkt andra piloter för 50 000 under striden mot krigsherren

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

### Vad utomjordingarna betalar {#what-the-aliens-pay}

Varje utomjording i en dungeon betalar när den faller och släpper byte, som utomjordingen i spelet som den är byggd efter: en Dungeon Goombah som en [Goombah](/wiki/04-Aliens/Goombah.md), en Dungeon Crystalys och dess Twin som en [Crystalys](/wiki/04-Aliens/Crystalys.md), en Dungeon Pirate som Pirate Boss (se [Pirate-svärm](/wiki/05-Swarms/Pirate-Swarm.md)). Vad en förstörd utomjording betalar och släpper är originalets **gånger förhållandet mellan deras skrov och sköld tillsammans**: en utomjording som är lika seg som sitt original betalar vad originalet betalar, en som är dubbelt så seg betalar dubbelt så mycket och släpper dubbelt så mycket av varje föremål, och så vidare. Avsnittet för varje sorts utomjording under [Utomjordingarna](#the-aliens) anger förhållandet och betalningen för en förstörd utomjording i varje steg.

- **Vem som får betalt.** Piloterna som skadade utomjordingen, efter skadan de gjorde, som med svärmarnas utomjordingar: en pilot eller grupp som bara snuddade vid den får ingenting, en grupp får betalt som en, och inom en grupp delar de medlemmar som är nära vraket och har skjutit nyligen på betalningen efter nivå. En pilot som inte skadade utomjordingen får inget för den, hur nära han än flög, och en utomjording som ingen pilot skadade betalar ingen. Bara de piloter som reglerna ovan betalar är med: den som har lämnat, inte varit inne tillräckligt länge, redan fått betalt för steget idag eller haft alla betalda klarningar för veckan får ingenting för utomjordingarna, och de andra får hans del. En förstörd utomjording kräver inte andelen i striden: att ha skadat den är andelen. Om gruppmedlemmen som gjorde mest skada har blivit förstörd eller inte är kvar på kartan, delar de medlemmar som är nära vraket och har skjutit nyligen på betalningen utan honom.
- **Vad som betalas.** Krediter, Thulium, erfarenhet och heder, en gång per förstörd utomjording. Betalningen är vad originalet betalar i Alpha, i alla världar: en dungeon har ingen världsmultiplikator. Dina boosters, Premium, formation och din klans bonusar räknas som vid vilken förstörd utomjording som helst, och erfarenheten räknas för dina [PvE-poäng](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points) som klarningens.
- **Bytet.** Det slumpas med originalets chanser, och sedan multipliceras varje mängd med förhållandet (en bråkdel av en enhet är en chans till en till). Det faller som en låda vid vraket, först för piloten som gjorde mest skada och hans klan, sedan för vem som helst på kartan, och sedan är det borta. Kartan rymmer bara ett visst antal lådor åt gången, så plocka upp dem under tiden, och det som ligger kvar på kartan när dungeonen stänger försvinner med den. Till skillnad från klarningens föremål är det vanligt byte från en utomjording: det kan [säljas på Auktionen](/wiki/03-Mechanics/Auction.md#marketable-items) när föremålet är säljbart.
- **Vad som inte betalar.** Krigsherren betalar ingen förstörd utomjording, bara klarningen. Goombahs som han kallar på betalar ingenting, eftersom kallelsen kommer tillbaka så länge striden pågår.
- **Inte en förstörd utomjording i spelet.** En förstörd utomjording i en dungeon räknas inte för uppdrag, prestationer, räknare över förstörda, wipepoäng, PvE-poängen för en förstörd, drönare eller P.E.T.s: en Dungeon Goombah är ingen Goombah i spelet.
- **Gränserna.** Dag- och veckogränserna ovan håller tillbaka utomjordingarnas betalning precis som klarningens: den som redan fått betalt för steget idag, eller haft alla betalda klarningar för veckan, får inget heller för dess utomjordingar, och potten för en förstörd går till de andra. En dungeon som inte klaras betalar sina förstörda utomjordingar till de piloter som reglerna betalar, och ingenting för klarningen.

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
- **Betalda piloter**: Minst 3 i dungeonen

<!-- dungeons-clan:end -->

## Tips

- Rensa en zons våg innan du försöker hålla zonen, och strid inne i ringen om utomjordingar kommer in.
- Ta med hela gruppen till en zon: ju fler piloter i ringen, desto snabbare hålls den.
- Leta efter Crystalys och deras Twins i labyrinten: krigsherrens dörr öppnas när tre fjärdedelar av dem är döda, och inte förr. De andra utomjordingarna kan vänta, eller förstöras också.
- Använd väggarna: lasrar går inte igenom dem, de röda ringarna från krigsherrens auror slutar vid dem, och en vägg stoppar också krigsherrens raketer.
- Spara en EMP Charge till Raketsalvan.
- När krigsherren kallar på sina Goombahs, förstör dem först: han kan inte skadas förrän de är borta. Kliv ut ur ringen innan du skjuter i Kaoszonen.
- Håll koll på klockan i fönstret Klandungeon. När tiden tar slut misslyckas dungeonen och klarningen betalar ingenting.
