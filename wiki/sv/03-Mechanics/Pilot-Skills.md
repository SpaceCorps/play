<!-- wiki-i18n source: d75ffd5e6e894c46 -->
<!-- wiki-i18n title: Pilotfärdigheter -->
# Pilotfärdigheter {#pilot-skills}

<!-- wiki-search: skills; skill tree; pilot skill tree; pilot skills; skill xp; xp; level up; stats; attributes; heft; grit; reflex; instinct; laser tech; rocket tech; antimatter; marksmanship; sabotage; evasion; tactics; radiation tech; thruster theory; science; extraction; logistics; fabrication; commerce; soft cap; hold; training; day one; pilot button; pilot page; buffs; färdigheter; pilotfärdigheter; färdighetsträd; erfarenhet; nivåhöjning; värden; attribut; tyngd; seghet; reflexer; instinkt; laserteknik; raketteknik; antimateria; skytte; undanmanöver; taktik; strålningsteknik; thrusterteori; vetenskap; utvinning; logistik; tillverkning; handel; mjuk gräns; lastrum -->

Din pilot har ett **färdighetsträd**: en uppsättning värden som stiger i nivå av det du gör. Strid, och din Laserteknik och din Seghet stiger; samla in från din Skylab, och din Utvinning stiger. Varje nivå ger en liten permanent buff på något du redan gör, och inget spenderas eller väljs: det finns inga poäng att fördela och inget att nollställa. Du höjer det du använder.

Trädet tillhör **dig**, inte ett skepp. Varje skepp du flyger har dina nivåer, ett skepp du köper i morgon också, och nivåerna behålls genom varje wipe ([vad som behålls](#what-is-kept)).

En ny pilot är inte på full styrka. På nivå 1 gör en laser och en raket mindre skada än föremålssidorna anger, och Laserteknik och Raketteknik lyfter dem förbi de angivna talen allteftersom de stiger. Varje tal på föremålssidorna är föremålets eget, före dina färdigheter.

## I korthet {#at-a-glance}

<!-- skills-glance:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

- **Värden**: 18 värden: 4 attribut och 14 färdigheter i 5 grupper
- **Nivåer**: 1 till 100. Varje pilot startar varje värde på nivå 1, och det finns inget att spendera och inget att nollställa
- **Kostnad för en nivå**: 40 XP från nivå 1 till 2, 875 XP från nivå 50 till 51, 19 157 XP från nivå 99 till 100; 313 258 XP totalt
- **Vad en nivå ger**: En buff växer i rät linje från sitt värde på nivå 1 till sitt värde på nivå 100. Inget har tak
- **Din laser på nivå 1**: Den gör 80 % av sin skada och träffar 80 % av gångerna, alltså 64 % av den skada föremålssidorna anger
- **Din raket på nivå 1**: Den gör 80 % av sin skada och är en blindgångare 20 % av gångerna, alltså 64 % av den skada föremålssidorna anger
- **Undanmanöver**: Varje pilots skepp viker undan för 3 % av de träffar som går att väja för, innan någon färdighet eller formation lägger till
- **Skrovnivå**: Skeppets sällsynthet avgör den, som tabellen nedan visar. Lastrummets storlek och Tyngds XP följer den
- **Lastrum**: Det räknar de resursenheter du plockar upp efter start, upp till den storlek som dess skrovnivå ger det. Det är fullt från 90 % av det, och ett fullt lastrum gör att Tyngd betalar ×1,5. Inget nekas någonsin
- **Mjuk timgräns**: De flesta värden betalar full XP bara upp till en gräns per timme, räknad i värdets egen enhet över UTC-klockans timme. Över den betalar en händelse 25 % av sin XP
- **Träning**: En färdighets XP betalar också 10 % av sig själv till sitt attribut. Ett attribut på nivå 100 tränar sina färdigheter 25 % snabbare än på nivå 1

| Skrovnivå | Skeppets sällsynthet | Lastrummets storlek |
| :--- | :--- | ---: |
| 1 | Skral / Vanlig | 60 |
| 2 | Ovanlig | 120 |
| 3 | Sällsynt | 250 |
| 4 | Episk | 500 |
| 5 | Mytisk / Legendarisk / Evig | 1 000 |

<!-- skills-glance:end -->

## Värdena {#the-stats}

Värdena är av två slag. **Attributen** (Tyngd, Seghet, Reflexer och Instinkt) är en pilots grunder. **Färdigheterna** finns i fem grupper, och varje färdighet styrs av ett attribut, som tabellerna nämner inom parentes: en färdighets XP matar också dess attribut, och ett högt attribut tränar sina färdigheter snabbare ([hur XP betalas](#how-xp-is-paid)). Namnen är de på sidan Pilotfärdigheter i spelet.

Tabellerna anger varje buff på nivå 1 och på sista nivån; däremellan växer en buff i rät linje. En **faktor** multiplicerar ett tal: en över 1 gör det större, en under 1 mindre. De flesta buffar ändrar ett tal på ditt skepp, och verktygstipset för ett tal som en färdighet har flyttat har en rad som säger hur mycket av det som kommer från dina färdigheter.

<!-- skills-buffs:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

### Attribut {#attributes}

| Värde | Vad det ändrar | Nivå 1 | Nivå 100 |
| :--- | :--- | ---: | ---: |
| **Tyngd** | Skrov | +0 % | +10 % |
| **Seghet** | Skada du tar | ×1 | ×0,9 |
| **Reflexer** | Uppladdningsfart för förmågor | ×1 | ×1,11 |
| **Instinkt** | Chans för varje bytesrad | +0 punkter | +5 punkter |
|  | Orvium och Velkonite från samlarna | ×1 | ×1,5 |

### Vapen {#weapons}

| Värde | Vad det ändrar | Nivå 1 | Nivå 100 |
| :--- | :--- | ---: | ---: |
| **Laserteknik** (Reflexer) | Laserskada | ×0,8 | ×1,1 |
|  | Chans att en lasersalva träffar | 80 % | 90 % |
| **Raketteknik** (Reflexer) | Raketskada | ×0,8 | ×1,1 |
|  | Chans att en raket blir en blindgångare | 20 % | 0 % |
| **Antimateria** (Instinkt) | Dark Matter från plock | ×1 | ×1,25 |

### Strid {#combat}

| Värde | Vad det ändrar | Nivå 1 | Nivå 100 |
| :--- | :--- | ---: | ---: |
| **Skytte** (Reflexer) | Hur långt en Mine kastas | ×1 | ×1,15 |
|  | Hastighet på en kastad Mine | ×1 | ×1,15 |
| **Sabotage** (Reflexer) | Skada från gifter och Minor | ×1 | ×1,3 |
|  | Giftens varaktighet | ×1 | ×1,2 |
| **Undanmanöver** (Reflexer) | Chans att väja för en träff, lagd till skeppets egen | 0 % | 15 % |
| **Taktik** (Reflexer) | Förmågornas varaktighet | ×1 | ×1,2 |

### Skeppsstyrning {#ship-control}

| Värde | Vad det ändrar | Nivå 1 | Nivå 100 |
| :--- | :--- | ---: | ---: |
| **Strålningsteknik** (Seghet) | Strålningsdos | ×1 | ×0,4 |
| **Thrusterteori** (Tyngd) | Hastighet | +0 % | +15 % |
| **Vetenskap** (Instinkt) | Vetenskap från varje enhet bränsle | ×1 | ×1,25 |

### Skylab

| Värde | Vad det ändrar | Nivå 1 | Nivå 100 |
| :--- | :--- | ---: | ---: |
| **Utvinning** (Instinkt) | Vad Skylab tillverkar | ×1 | ×1,3 |
| **Logistik** (Tyngd) | Vad Resurslagrets bank rymmer | ×1 | ×1,4 |
| **Tillverkning** (Reflexer) | Tid för en tillverkning | ×1 | ×0,65 |

### Handel {#trading}

| Värde | Vad det ändrar | Nivå 1 | Nivå 100 |
| :--- | :--- | ---: | ---: |
| **Handel** (Instinkt) | Priser i butiken | ×1 | ×0,85 |
|  | Vad butiken betalar vid återköp | ×1 | ×1,1 |
|  | Deposition för en annons på Auktionen | ×1 | ×0,5 |


<!-- skills-buffs:end -->

## Var du märker det {#where-you-feel-it}

- **Lasrar.** Laserteknik ändrar skadan i varje salva och chansen att den träffar; en salva som går fel visar ett svävande ”Miss” och förbrukar ändå sin ammunition ([Strid](/wiki/03-Mechanics/Combat.md#laser-tech)). Räckvidden på dina lasrar är skeppets egen: Skytte stiger av dina träffar med annan ammunition än vanlig x1, men verkar bara på Mine (nedan).
- **Raketer.** Raketteknik ändrar skadan i varje raket och chansen att en blir en blindgångare ([Raketteknik](/wiki/06-Items/Rockets.md#rocket-tech)).
- **Att ta träffar.** Seghet tar en andel av varje träff du får, och Undanmanöver ökar chansen att en direktträff inte gör något ([Strid](/wiki/03-Mechanics/Combat.md#grit-and-evasion)). Tyngd ökar ditt skrov.
- **Förmågor.** Reflexer förkortar nedkylningen av dina förmågor och Taktik får dem att vara längre ([Förmågor](/wiki/03-Mechanics/Abilities.md#pilot-skills)). Sabotage förstärker gifterna.
- **Mine.** Sabotage ökar skadan av en Mine, och Skytte kastar den snabbare och längre ([Extrautrustning](/wiki/06-Items/Extras.md#mine)).
- **Hastighet.** Thrusterteori lägger till din hastighet, utöver motorerna och en Afterburner ([Hastighet](/wiki/03-Mechanics/Speed.md)).
- **Plock.** Instinkt ökar chansen för varje bytesrad, som en Loot Luck Booster gör, och de två läggs ihop; Antimateria ökar den Dark Matter du plockar upp ([Last](/wiki/03-Mechanics/Cargo.md), [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md)).
- **Strålning.** Strålningsteknik sänker dosen från det svarta hålet, grävmaskinernas cirklar, pulsarerna och Unwakened-auran ([Svart hål](/wiki/03-Mechanics/Black-Hole.md)).
- **Hemma.** Utvinning och Logistik ändrar vad [Skylab](/wiki/03-Mechanics/Skylab.md) tillverkar och rymmer, Instinkt ökar dess två samlare, Tillverkning förkortar tillverkningarna i Montering, Vetenskap fyller [Forskningscentrum](/wiki/03-Mechanics/Research.md) snabbare, och Handel sänker priserna i butiken, höjer vad den betalar vid återköp och sänker depositionen för en annons på [Auktionen](/wiki/03-Mechanics/Auction.md).

## Hur XP betalas {#how-xp-is-paid}

Servern betalar XP för det du gör, var du än flyger, i den här ordningen:

1. **Anti-farm-regeln.** En träff från eller mot en koncernkamrat eller gruppkamrat betalar ingenting, och ingenting heller för det som görs mot eller av ett skepp i en säker zon eller under skydd av en återuppståndelse. Sekunderna för Tyngd, för Seghetens låga skrov och för Thrusterteori räknas bara medan ditt skepp lever, är utanför ett skydd och du har gett en order den senaste minuten: ett skepp som står parkerat i det fria tjänar ingenting.
2. **Den mjuka timgränsen.** Ett värde med en gräns betalar full XP upp till den och en andel över den, räknat i värdets egen enhet (skotten du skjuter, kommandona du ger, den XP det tjänade) över UTC-klockans timme. En ny inloggning öppnar inte fönstret igen, och talen finns i listan ovan och i tabellen nedan.
3. **Träningstakt.** Attributet som styr en färdighet höjer den XP färdigheten tjänar, mer för varje nivå av attributet (gränsen räknas före detta, så gränsen begränsar aktiviteten och inte takten).
4. **Attributets andel.** Färdigheten får XP:n, och dess attribut får en andel av den, som aldrig begränsas eller skyndas på.

Tabellen listar vad som betalar XP, värde för värde. XP:n gäller för varje enhet av det som nämns i andra kolumnen.

<!-- skills-xp:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

| Värde | Vad som betalar XP | XP | Mjuk timgräns |
| :--- | :--- | ---: | ---: |
| **Tyngd** | Var 10 s flygning med en order given de senaste 1 min: skeppets skrovnivå, plus 0,2 för varje monterad plåt, ×1,5 med fullt lastrum | 1 | Ingen |
| **Seghet** | Varje 1 % av ditt maximala skrov som går förlorat till en fiende eller en fara | 1 | 300 XP i timmen |
|  | Var 10 s under 25 % av ditt maximala skrov | 5 |  |
| **Reflexer** | Varje kommando som spelet tar emot: en förmåga, ett extra, ett nytt mål, ett plock, en tillverkning, ett formationsbyte, en raket eller ett hopp. Ett nytt mål betalar högst en gång per 4 s, ett plock högst en gång per 1 s och en raket högst en gång per 1 s | 1 | 600 kommandon i timmen |
| **Instinkt** | Varje lastlåda du plockar upp, för hand eller med en Retriever | 2 | 600 XP i timmen |
|  | Varje föremål i en uppdragsbelöning som du hämtar | 10 |  |
|  | Första gången du plockar upp ett föremål av kvaliteten Sällsynt eller bättre (en gång för varje föremål, för alltid) | 25 |  |
| **Laserteknik** (Reflexer) | Varje salva du avfyrar | 0,1 | 1 800 skott i timmen |
|  | Varje salva som träffar ett skepp | 0,1 |  |
| **Raketteknik** (Reflexer) | Varje raket du skjuter upp | 0,15 | 130 raketer i timmen |
|  | Varje raket som träffar ett skepp (en gång för varje raket, hur många skepp dess explosion än skadar) | 0,3 |  |
| **Antimateria** (Instinkt) | Varje enhet Dark Matter du får vid ett plock | 0,1 | Ingen |
| **Skytte** (Reflexer) | Varje träff av en salva avfyrad med annan ammunition än vanlig x1 (×1,5 under de första 10 min av varje ammunitionstyp i en klocktimme) | 0,1 | 3 000 träffar i timmen |
|  | Varje träff av en Mine, och varje sekund en fiende tillbringar i din Energetic Wall | 0,1 |  |
| **Sabotage** (Reflexer) | Varje träff av en Mine, och varje sekund en fiende tillbringar i din Energetic Wall | 0,5 | 1 200 XP i timmen |
|  | Varje sekund ett gift från dig verkar på en fiende | 0,05 |  |
| **Undanmanöver** (Reflexer) | Varje fientlig attack mot dig som missar eller väjs för | 1 | 600 XP i timmen |
| **Taktik** (Reflexer) | Varje förmåga du trycker på med en fiende inom laserräckvidd | 2 | 600 XP i timmen |
| **Strålningsteknik** (Seghet) | Varje sekund inne i ett strålningsband | 0,2 | Ingen |
|  | Varje 1 % av ditt maximala skrov som strålningen tar | 1 |  |
| **Thrusterteori** (Tyngd) | Varje sekund flugen över 80 % av ditt skepps hastighet, dubbelt så mycket under en Afterburner | 0,1 | Ingen |
| **Vetenskap** (Instinkt) | Varje enhet vetenskap som Forskningscentrum bränner | 0,1 | Ingen |
|  | Varje teknologi du slutför | 50 |  |
| **Utvinning** (Instinkt) | Varje resursenhet din Skylab tillverkar, betald när du samlar in | 0,1 | Ingen |
| **Logistik** (Tyngd) | Varje resursenhet du sätter in i Skylab-banken | 0,05 | Ingen |
| **Tillverkning** (Reflexer) | Varje sekund tillverkningstid du slutför, betald när du samlar in | 0,1 | Ingen |
| **Handel** (Instinkt) | Varje affär på Auktionen eller i butiken, räknad som tiologaritmen av 1 plus dess värde i krediter (ett Thulium är värt vad Auktionen värderar det till) | 2 | 600 XP i timmen |

<!-- skills-xp:end -->

Medan du flyger visar flygskärmen den XP du tjänar i korta rader, samlade med några sekunders mellanrum, och en banderoll berättar när ett värde stiger i nivå och vad som ändrades (Spelloggen behåller en rad om det). Ett värde som tjänar sin första XP kungörs en gång. Verktygstipsen för talen som färdigheter har flyttat säger det också, i en egen Pilot-rad, och Skada-rutan i hangaren lämnar färdigheterna utanför och säger det: de gäller när du skjuter.

## Nivåhöjning {#levelling-up}

En nivå kostar mer XP än den förra, med en fast andel, så de första nivåerna kommer snabbt och de sista tar lång tid. Varje värde har samma kurva. Buffen du har på en nivå är densamma för varje pilot: bara takten du når den i beror på vad du gör.

<!-- skills-curve:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

| Nivå | XP för nivån | XP totalt från nivå 1 | Andel av varje buff |
| :--- | ---: | ---: | ---: |
| 2 | 40 | 40 | 1,01 % |
| 10 | 66 | 468 | 9,09 % |
| 25 | 170 | 2 174 | 24,24 % |
| 50 | 822 | 12 851 | 49,49 % |
| 75 | 3 968 | 64 397 | 74,75 % |
| 100 | 19 157 | 313 258 | 100 % |

<!-- skills-curve:end -->

## Sidan Pilotfärdigheter {#the-pilot-skills-page}

Sidan **Pilotfärdigheter** är en sida i stationen, med en egen rad i sidofältet. Den visar hela trädet: attributen och färdigheterna i sina grupper, var och en med sin nivå. Välj ett värde för att se vad det gör, vilket attribut som styr det, vilka färdigheter det tränar, dess XP-fält och vad som får det att växa, och använd reglaget för att förhandsvisa vilken nivå som helst från 1 till den sista: en liten tabell anger vad värdet ändrar på nivån du förhandsvisar och på din nivå nu. Ett värde som ännu inte har tjänat någon XP är markerat som oanvänt, med ett streck som nivå. Raden i sidofältet får ett märke när ett värde har stigit i nivå sedan du senast öppnade sidan, och ett kort i Boosters-fönstret sammanfattar vad dina färdigheter ändrar.

## Vad som behålls {#what-is-kept}

- **Genom varje wipe.** Trädet är en del av ditt konto: en wipe ändrar ingen nivå och ingen XP, och Transportförrådet har inget med det att göra ([Vad du behåller](/wiki/03-Mechanics/Wipe-Timeline.md#what-you-keep)).
- **På de regionala servrarna.** Den XP du tjänar när du flyger på Singapore eller US East läggs till dina färdigheter när du kommer hem, ett värde du använde där för första gången inräknat, och den timgräns du förbrukade där följer med dig. Sidan Pilotfärdigheter för en pilot som flyger där läser den regionala serverns tal, med den XP skeppet har tjänat sedan sin senaste sparning.
- **Tills kontot raderas.** Att radera ett konto raderar dess nivåer.

Buffarna har inget annat tak än den sista nivån: en pilot som har höjt allt är så stark som tabellerna säger.
