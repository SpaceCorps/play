<!-- wiki-i18n source: 0f9ae19e1c5f8f9d -->
<!-- wiki-i18n title: Strid -->
# Stridsmekanik {#combat-mechanics}

Det här avsnittet beskriver hur skada beräknas, tillämpas och repareras under strider i SpaceCorps.

![The death screen: respawn at the nearest portal or on the spot, each with its lock](../../img/wiki-img/shots/death.jpg)
![The flight screen in a fight: ship and pilot windows, the target, the hotbar, the chat, the log and the minimap](../../img/wiki-img/shots/hud-fight.jpg)
![The Target window: the alien, its distance, hull and shield](../../img/wiki-img/shots/hud-target.jpg)

## Skadeberäkning {#damage-calculation}

När ett skepp avfyrar sina lasrar beräknar servern skadan i följande ordning:

### 1. Grundskada och slumpvariation {#1-base-damage-random-variance}

Grundskadan hos alla utrustade lasrar (även lasrar på drönare) och deras laserförstärkare i platserna summeras.
- **Slumputfall**: Den faktiska skadan i en salva slumpas mellan **80 %** och **100 %** av den totala grundskadan.
  - Formel: `Roll = (0.8 + (Random * 0.2)) * BaseDamage`

### 2. Kritiska träffar {#2-critical-hits}

Varje salva har en chans att bli en kritisk träff.
- **Kritisk chans**: Den genomsnittliga kritiska chansen hos utrustade lasrar plus summan av alla utrustade laserförstärkares kritiska chanser.
- **Kritisk multiplikator**: Om ett skott är kritiskt multipliceras skadeutfallet med **1,5×**. Skadetalet för en kritisk salva visas i isblått, större, med ett ”!” (se [Skade- och läkningssiffror](#damage-and-heal-numbers)).
- Quantum Laser I och II har ingen egen kritisk chans: deras förstärkare ger den.
- **Fast kritisk skada**: All fast kritisk skada från laserförstärkare läggs till efter multiplikatorn.
  - Formel: `CritDamage = (Roll * 1.5) + FixedCritDamage`

### 3. Globala multiplikatorer {#3-global-multipliers}

Till sist tillämpas globala multiplikatorer (som aktiva boosters, till exempel en Laser Damage Boosters +10 %, eller multiplikatorer för laserammunition som x2, x3, x4) för att få den slutliga skadan:
- Formel: `FinalDamage = Damage * AmmoMultiplier * (1.0 + BoosterDamagePercent)`
- En buren [drönarformation](/wiki/03-Mechanics/Formations.md) kan multiplicera resultatet en gång till: till exempel Auger +21 % laserskada, Gyre −11 % och, mot utomjordingar, Culler +12 % (en egen faktor, inte en del av boosterprocenten).
- Ammunitionen **Siphon Battery** har multiplikatorn x1 men ett annat mål: dess skada tas enbart ur målets sköld (aldrig skrovet, oavsett absorption) och går in i din egen sköld, upp till ditt maximum. Se [Lasrar och ammunition](/wiki/06-Items/Lasers.md).

### 3b. Raketer {#3b-rockets}

En [raket](/wiki/06-Items/Rockets.md) har sin egen skada (en Lancet I gör 1 700 till 2 100, en Lancet III 5 200 till 6 200, en N.U.K.E. 45 000 till 50 000), som slumpas fram en gång när den avfyras och är densamma för alla skepp: dina lasrar, förstärkare, boosters och ammunition ändrar den inte, och den har ingen kritisk träff. Alla raketer delar en enda omladdningstid på **3 sekunder**. En enkelmålsraket har en **sköldgenomträngning**: den dras av från ditt måls absorption (se Att ta skada och säkra zoner nedan); en explosion skadar varje skepp inom sin radie, hela talet i mitten och hälften av det vid kanten. Ingenting begränsar vad en raket tar från en pilots skepp: först skölden, sedan skrovet. Raketer skadar aldrig din egen koncern eller din egen [grupp](/wiki/03-Mechanics/Groups.md), oavsett vilka koncerner som ingår i den. En buren [drönarformation](/wiki/03-Mechanics/Formations.md) är det enda som ändrar båda: en raketformation höjer skadan hos varje raket (upp till +55 %), och några gör timern längre eller kortare. [Asteroider](/wiki/03-Mechanics/Asteroid-Mining.md) tar skada av raketer och av lasrar med 5 % av vad en salva gör mot ett skepp (dina förstärkare, boosters, ammunition och kritiska träffar räknas, och därefter dras asteroidens pansar av); drönare gör ingenting med dem, och en asteroid i vägen för ett skott tar träffen i stället för skeppet bakom den ([Skydd](/wiki/03-Mechanics/Asteroid-Mining.md#cover)).

### 4. Att vända sig mot målet {#4-facing-the-target}

Ett skepp eller en utomjording som har låst på ett mål och skjuter vänder sig mot målet, oavsett åt vilket håll det flyger (cirklar, backar eller ligger still), och vänder tillbaka mot sin kurs när det slutar skjuta.

### 5. Räckvidd {#5-range}

Ett skepp avfyrar en salva i sekunden medan dess mål är inom dess **räckvidd**, och håller elden medan målet är längre bort: elden slutar kosta ammunition tills målet är tillräckligt nära igen, och Målfönstret visar ”Utom räckhåll”. Räckvidden är **medelvärdet av räckvidden hos alla dina lasrar** (även lasrarna i dina drönare), avrundat till närmaste enhet, och det är ett enda tal för hela skeppet: inom den skjuter varje laser, utanför den ingen. En långräckviddig laser bredvid korta förlänger därför inte din räckvidd: en Starfire-III (850) och två Quantum Laser II (700) ger 750. En räckviddsbonus från Smedjan räknas på sin egen laser före medelvärdet. Ett skepp utan laser kan inte avfyra sina lasrar, och Hangaren visar ingen räckvidd för det (ett streck); dess raketer avfyras ändå, var och en med sin egen räckvidd (se [Raketer](/wiki/06-Items/Rockets.md)). Se [Lasrar och ammunition](/wiki/06-Items/Lasers.md) för varje lasers egen räckvidd.

## Skade- och läkningssiffror {#damage-and-heal-numbers}

En träff visas som en siffra som svävar över skeppet den träffar. **Dina egna siffror** visas alltid: skadan du gör, skadan du tar och dina egna reparationer. **Skeppet under din målfixering** visar mer: varje träff och varje läkning det får, **från vilken källa som helst**. Det betyder andra pilotes lasrar, raketer och drönare, utomjordingar, Clan Wardens samt skeppets egna reparationer och sköldregenerering. När någon annan skjuter på ditt mål ser du deras skada.

- **Färger.** Guld: skada på en utomjording eller en fientlig pilot. Rött med ett minustecken: skada på ett skepp du skyddar (en pilot i din egen koncern eller grupp) och skadan du själv tar. Grönt med ett plustecken: en läkning, till exempel en Emergency Repair, en Repair Drone eller en sköld som kommer tillbaka. Blekt silver ”Miss”: en direktträff som en formations undanmanöver avledde. En kritisk salva är större och slutar på ett ”!” (isblå när den träffar en utomjording eller en fiende).
- **Dina förblir ljusare.** Andras siffror på ditt mål är lite mindre och svagare och står i en kolumn till höger om skeppet, så att de aldrig täcker dina.
- **En siffra för en folkmassa.** Träffar som landar samtidigt läggs ihop till en siffra med ett antal efter sig (`×35`). Fyrtio piloter som skjuter på ett skepp ger ungefär två siffror i sekunden, och aldrig fler än sju. Läkningar visas en gång i sekunden.
- **Bara skeppet under ringen.** Varje annat skepp visar bara dina egna träffar och träffarna på dig. Svarta hålets strålning och en formations sköldavtappning har inga siffror: de syns på staplarna.
- **Inställningen.** Inställningar › Gränssnitt › **Visa andras skada på mitt mål**, på som standard. Avstängd ser du bara dina egna siffror. **Minska rörelser** håller alla siffror stilla: ingen poppar upp eller stiger.

---

## Belöning för nedskjutning: första träffen paxar {#kill-rewards-first-hit-claims}

En utomjordings belöning går till piloten som sköt den först, inte till den som landar den sista träffen.

- **Att paxa**: den första piloten vars skott skadar en utomjording paxar den. Varje träff du gör förnyar ditt pax.
- **Att förlora paxet**: om du inte träffar utomjordingen på **10 sekunder** släpper ditt pax och nästa pilot som träffar den paxar den. Ditt pax tar också slut när ditt skepp förstörs eller du lämnar kartan (genom en portal, eller genom att logga ut), och att komma tillbaka inom de 10 sekunderna ger inte tillbaka det.
- **Nedskjutningen**: när utomjordingen förstörs får piloten som har paxet allt: krediter, Thulium, XP, heder, nedskjutningen för uppdrag och wipepoäng, och [lastlådan](/wiki/03-Mechanics/Cargo.md). En pilot som gör slut på en utomjording som någon annan har paxat får ingenting, och Spelloggen säger det. När ditt pax betalar och en annan pilot landar den sista träffen nämner Spelloggen den piloten och säger att ditt pax betalar dig.
- **Rankingpoäng**: nedskjutningen ger också PvE-poäng till rankingen för piloten som har paxet, fler ju tåligare utomjordingen är: 1 för en Seeker, 2 för en Phantasm, 4 för en Bulwark, 7 för en Goombah och 16 för en Crystalys (varje utomjordings artikel anger sitt värde). De är pilotens ensam: gruppens andel av belöningarna omfattar dem inte.
- **Att se det**: när du väljer en utomjording som en annan pilot har paxat visar Målfönstret *Paxad av* den piloten och *Ingen belöning*.
- [Koncernpiloter](/wiki/03-Mechanics/Company-Pilots.md) paxar aldrig en utomjording, och en utomjording de gör slut på betalar ändå piloten som har paxet.
- En pilot i en [grupp](/wiki/03-Mechanics/Groups.md) delar det som dess pax betalar med de gruppkamrater som är nära och skjuter; själva paxet är pilotens ensam.
- **[Svärmarnas](/wiki/05-Swarms/Swarms.md) ledare, Dormant Pulses och [Clan Wardens](/wiki/03-Mechanics/Clans.md#warden-pay-and-loot) är undantaget**: en svärmboss, varje Dormant Pulse och varje Clan Warden betalar efter den skada varje pilot gjort på dem, inte efter första träffen, och deras lastlåda går till piloten som gjorde mest skada ([hur nedskjutningen av en boss betalar](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). De övriga följeslagarna, Pirate Scouts och Seeker Slaves, betalar efter paxet som vilken utomjording som helst. Ett svärmskepps PvE-poäng står på sidan Svärmar.

---

## Utomjordingar som bara slår tillbaka {#aliens-that-only-fight-back}

Seeker och Goombah startar aldrig en strid. Var och en vänder sig mot en pilot som träffar den (en träff som gör skada; en annan utomjordings eld provocerar den aldrig), slåss mot den pilot som beskrivs under [Vem en utomjording slåss mot](#who-an-alien-fights) och släpper **10 sekunder** efter att någon senast träffade den. Lämnad i fred i **30 sekunder** läker dess skrov 2 % av sitt maximum per sekund. De andra utomjordingarna (Phantasm, Bulwark, Crystalys) går på varje oskyddad pilot som kommer inom deras aggroradie (700, 700 och 900 enheter) och läker aldrig sitt skrov; varje utomjordings sköld laddas från 15 sekunder efter dess senaste träff.

---

## Vem en utomjording slåss mot {#who-an-alien-fights}

En utomjording fortsätter att slåss mot **den första piloten som sköt på den**, så länge den fortfarande kan jaga den piloten: piloten är kvar på kartan, inte i en säker zon, inte kamouflerad eller inom sitt EMP-fönster, vid liv, och har träffat den under de senaste **10 sekunderna** (varje träff startar de 10 sekunderna om: en lasersalva, en raket eller kanten av en explosion lika). Så länge det gäller får andra pilotars skott den aldrig att vända sig, hur nära de än är och hur ofta de än träffar, så en pilot kan hålla fast en utomjording medan andra skjuter på den.

När den första piloten faller bort (lämnar kartan, når en säker zon, blir omöjlig att låsa på, förstörs eller slutar träffa utomjordingen i 10 sekunder) vänder sig utomjordingen mot den **nästa** piloten som gick med i striden, i den ordning de först sköt på den, inte mot den som träffade den senast. En pilot som har fallit bort och skjuter på den igen ställer sig sist i kön. En utomjording håller reda på de **32** första piloterna som sköt på den; en 33:e skytt ingår inte i kön förrän någon av dem faller bort, och hur stor skaran än är håller sig utomjordingen till den första.

[Koncernpiloter](/wiki/03-Mechanics/Company-Pilots.md) kommer efter varje spelare: en utomjording slåss mot en koncernpilot bara så länge ingen spelare som den fortfarande kan jaga har skjutit på den, en spelare som skjuter på en utomjording som en koncernpilot slåss mot tar över den, och en koncernpilot drar aldrig bort en utomjording från en spelare. Inget av detta ändrar vem som får utomjordingens belöning: det avgörs av paxet ([Belöning för nedskjutning](#kill-rewards-first-hit-claims)).

---

## Utomjordingar tappar intresset {#aliens-lose-interest}

Ingen utomjording följer dig över hela kartan. Men en utomjording som du **träffar** tappar inte intresset, den strider mot dig: under **10 sekunder** efter din senaste träff (varje träff startar de 10 sekunderna om, en lasersalva, en raket eller kanten av en explosion lika) flyger den mot dig, i sin egen hastighet, så snart du är utanför dess anfallsräckvidd (Seeker 600, Phantasm och Bulwark 700, Goombah 800, Crystalys 900), och fortsätter att närma sig och skjuta tills du är inom räckvidd. Det finns ingen gräns för hur långt den följer medan du fortsätter att träffa den. En laser som når längre än utomjordingens vapen (en Starfire-III når 850 enheter, en Helios Beam 900) låter dig inte träffa den från ett avstånd där den inte kan svara, och ett snabbare skepp håller den bara bakom dig så länge du fortsätter skjuta. Den släpper dig ändå direkt om du når en säker zon, kamouflerar dig eller lämnar kartan.

När flera piloter träffar samma utomjording håller den sig till den som sköt först (se [Vem en utomjording slåss mot](#who-an-alien-fights)): den närmar sig den piloten och skjuter, så en grupp som står runt den precis utanför dess räckvidd kan inte få den att flyga fram och tillbaka mellan dem utan att den någonsin svarar.

En utomjording som har valt dig som mål (en Phantasm, Bulwark eller Crystalys som du kom nära, eller vilken utomjording som helst som du sköt på) och som du inte har träffat på 10 sekunder ger upp så snart något av detta stämmer:

- **Du sköt aldrig på den:** du är mer än **1 200 enheter** från den, eller den har flugit **2 000 enheter** från där jakten började.
- **Du sköt på den under den senaste minuten:** du är mer än **2 500 enheter** från den, eller den har flugit **3 000 enheter** från där jakten började. En strid som du startade förblir rättvis.

En utomjording som ger upp strövar vidare från där den står, aldrig vidare till där den senast såg dig (inte ens när du kamouflerar dig eller avfyrar en EMP), och väljer dig inte som mål igen på **8 sekunder**, om du inte skjuter på den. Varje utomjording bestämmer själv, så en blandad flock glesnar när du flyger iväg. Utomjordingar följer dig aldrig in i en säker zon eller genom en portal, och de som tappade bort dig nära en sådan tar sig därifrån, var och en åt sitt håll, så att de inte väntar i en hög. En utomjordings intressegräns är aldrig kortare än dess anfallsräckvidd och aggroradie, plus 100 enheter.

Utomjordingar skjuter inte undan varandra: en flock efter en pilot närmar sig utan att lämna något utrymme mellan sina skepp, och en flock som tappat sin pilot sprids först när varje utomjording väljer sin egen väg. En utomjording håller däremot avstånd till ett **skepp**: den hamnar aldrig inuti en pilots skrov, och en pilot som parkerar på en knuffar den med sig.

Att flyga fortare hjälper bara till en viss gräns: en Protos (160) är inte snabbare än någon utomjording som jagar (Phantasm 160, Bulwark 175, Crystalys 230), så det är avståndsgränsen, inte din hastighet, som avslutar jakten.

---

## Att ta skada och säkra zoner {#taking-damage-safe-zones}

När ditt skepp träffas av en fiende eller en NPC hanteras skadan så här:

### 1. Sköldabsorption {#1-shield-absorption}

Inkommande skada delas mellan sköldar och träffpoäng efter ditt skepps **genomsnittliga absorption**: medelvärdet av dina sköldars absorption, var och en med sina sköldcellers, plus Shield Absorbance Boost från säsongsbutiken (se [Sköldmekanik](/wiki/03-Mechanics/Shields.md)). Den har **inget tak vid 100 %**: det sköldarna tar av en träff är din absorption **minus angriparens sköldgenomträngning**, mellan 0 % och 100 %.
- **Absorption** (t.ex. 80 % för den bästa skölden med de bästa cellerna, 56 % för en Basic Shield Core med två Absorption Shield Cell I) av varje träff tas av sköldarna, minus träffens genomträngning: en Lancet IIIs 35 % lämnar 45 % på sköldarna hos ett skepp med 80 %, och resten (55 % där) träffar HP direkt.
- **Sköldgenomträngning** kommer från enkelmålsraketer (10 till 35 %) och x3- och x4-laserammunitionen (5 % och 10 %); utomjordingar har ingen. Ett skepp över 100 % (112 %, till exempel) tål en hel träff mot genomträngning upp till skillnaden (12 % där). Penetration Amps i skyttens lasrar (+3 % till +12 % per plats) och en drönarformation läggs till, och inget sätter tak för summan.
- En sköld som är för låg för sin andel för över skillnaden till HP; om sköldarna är helt tömda träffar **100 %** av all återstående skada HP.
- Utomjordingar har inget absorptionsvärde: deras sköldar tar 80 % av varje träff (minus träffens genomträngning), deras skrov resten.
- **Drönarformationer.** Rampart höjer din absorption med 17 % (Shrike sänker den med 6 %), och Asterism ger varje direkt träff på dig 7 % chans att inte göra någon skada alls (ett flytande ”Miss” visas), och de träffar som landar delas av sköld och skrov som vanligt. Gemini (+9 poäng) och Stiletto (+16) lägger genomträngning till din egen ammunition och direkta raketer, utan tak ([Drönarformationer](/wiki/03-Mechanics/Formations.md)). För en laser räknas även dess förstärkare.

### 2. Immunitet i säker zon {#2-safe-zone-immunity}

Varje fraktions hembas (X-1-kartor) innehåller säkra zoner.
- Att gå in i en säker zon gör ditt skepp helt immunt mot skada.
- **Aggrobrott**: Att attackera en fiende tar omedelbart bort din immunitet i säker zon, även om du fysiskt befinner dig inne i en.
- En ring runt varje station och portal skyddar dig när 5 sekunder har gått sedan du träffades och 15 sedan du sköt. Medan den skyddar dig och du inte är i strid låter Hangarfönstret dig byta skepp utan att lämna spelet: se [Hangaren under flygning](/wiki/03-Mechanics/Hangar.md).
- Stationer finns bara i hembaserna (`x-1`). Farosektorerna (`DS-1` till `DS-4`) har inga: där är ringarna runt portalerna de enda säkra zonerna.

### 3. Under attack i en farosektor {#3-under-attack-in-a-danger-sector}

Ett hopp genom en portal tar 3 sekunder (se [Resor på rymdkartan](/wiki/01-General/Spacemap%20Travel.md)). I farosektorerna (`DS-1` till `DS-4`) kan en pilot vars skepp träffades av en annan pilot eller en utomjording under de senaste **10 sekunderna** inte starta ett hopp, och en träff avbryter ett hopp som pågår. Överallt annars avbryter attacker aldrig ett hopp, och ingenting avbryter upplockningen av en [lastlåda](/wiki/03-Mechanics/Cargo.md).

---

## Återhämtning och reparation {#recovery-repair}

För att återhämta sig efter strid kan piloter förlita sig på passiv regenerering och aktiva hjälpbottar:

### 1. Passiv sköldregenerering {#1-shield-passive-regeneration}

- **Funktion**: Återställer sköldpoäng motsvarande din skölds laddningstakt per sekund.
- **Fördröjning**: Avbryts av strid; den passiva regenereringen återupptas först efter **15 sekunder** utan skada.
- **Drönarformationer**: Adamant och Redoubt ger tillbaka sköld varje sekund, även i strid (se [Drönarformationer](/wiki/03-Mechanics/Formations.md)).

### 1b. Siphon Battery

Ammunitionen [Siphon Battery](/wiki/06-Items/Lasers.md) lägger den sköld den dränerar från ett mål till din direkt, upp till ditt maximum. Att få sköld är ingen skada du tar, så det fördröjer inte din passiva regenerering.

### 2. Reparationsdrönare (skrovreparation) {#2-repair-drones-hull-repair-}

- **Funktion**: Om du utrustar en Repair Drone (under Hangarens extrautrustning) slår du på den från snabbfältet (dra den från väljaren Extra till en plats) och den reparerar ditt skrov (HP). Varje träff stänger av den, och den stannar vid fullt skrov. Med en [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) monterad behöver du inte slå på den igen: CPU:n skickar ut drönaren själv så fort fördröjningen nedan har gått, om du inte stoppade den för hand.
- **Reparationstakt**: Återställer en procentandel av dina maximala träffpoäng per sekund (bara den bästa drönaren som är monterad räknas, de adderas inte):
  - **Repair Drone I**: 1,5 % av max HP / s
  - **Repair Drone II**: 2,25 % av max HP / s
  - **Repair Drone III**: 3,5 % av max HP / s
  - **Repair Drone IV**: 5 % av max HP / s
- **Fördröjning**: Reparationsdrönare börjar laga skrovet först efter **10 sekunder** utan skada.
- **I en förmågeplats** reparerar en Repair Drone inte av sig själv: den ger dig **Emergency Repair**, en knapp som läker en andel av dina maximala träffpoäng under tio sekunder, även under eld (se [Förmågor](/wiki/03-Mechanics/Abilities.md)).

---

## Kamouflage och EMP {#cloaking-and-the-emp}

Ett skott kräver målfixering. Två [extrautrustningar](/wiki/06-Items/Extras.md) tar din ifrån dig:

- **Cloaking CPU**: medan du är kamouflerad (det finns ingen tidsgräns) ser andra koncerners piloter, utomjordingar och koncernpiloter inte ditt skepp och kan inte låsa på det; de ser en vanlig röd prick på minikartan där du är. Din första salva avslutar kamouflaget, och du kan inte kamouflera dig igen på en minut, inte heller inom 10 sekunder efter en träff eller ett skott.
- **EMP Charge**: i 3 sekunder kan ingen låsa på dig, och varje målfixering som redan ligger på dig bryts direkt. Den avslutar varje kamouflage inom 1 500 enheter från piloten som avfyrar den, utom de som tillhör pilotens egen grupp. Den döljer dig inte, och det är ingen osårbarhet: den stoppar det som kräver målfixering.

En raket är också ett skott: den avslutar ditt eget kamouflage, och områdesskadan från någon annans raket skadar fortfarande ett kamouflerat skepp och avslutar dess kamouflage, eftersom en explosion inte kräver målfixering (se [Raketer](/wiki/06-Items/Rockets.md)). EMP:n stoppar målfixerade lasrar och målsökande raketer, inte en explosion.

Ingetdera ändrar ett pax: ett pax är historiken över vem som har träffat en utomjording, inte en målfixering, och kamouflage släpper ditt.
