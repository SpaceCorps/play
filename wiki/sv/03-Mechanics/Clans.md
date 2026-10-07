<!-- wiki-i18n source: 3d121321d2746bbe -->
<!-- wiki-i18n title: Klaner -->
# Klaner {#clans}

Att grunda en klan eller gå med i en låter dig samla resurser, uppgradera den gemensamma banken, ställa in skattesatser, samordna dig med medlemmar i din fraktion och sköta diplomati. En klan har också arbete att göra tillsammans: varje dag får den en **dagslinje** av uppdrag som slutar med en boss som bara klanen kan skada, och poängen den tjänar köper **permanenta bonusar** åt varje medlem. (På spelets Klan-sida kallas en klan en *flotta*, och dess poäng och bonusar heter där flottpoäng och flottbonusar.)

**På en minut**

- Varje säsongsdag får din klan en [dagslinje](#daily-line): fyra uppdrag som görs i ordning (skjuta ned utomjordingar, flyga en sträcka, vissa dagar fälla svärmbossar), sedan en [klanväktare](#clan-wardens), en boss som du kallar fram och som bara din klan kan skada.
- Varje klart steg betalar klanpoäng direkt: 15, 15, 20, 20 och 30, alltså **100 poäng** för en hel linje.
- Ledaren och vice ledarna lägger poängen på tre [bonusar](#clan-points-and-boosts) med tio nivåer vardera: **Skada** (upp till +5 %), **Thulium** (upp till +10 %) och **Krediter** (upp till +10 %).
- En klan som klarar varje linje har köpt alla nivåer på **säsongsdag 12**. Poäng och nivåer börjar om vid varje wipe.
- Du behöver minst **tre medlemmar** som gjort sin del och **en stor besättning** för striden mot väktaren: sedan 0.4.13 har en väktare fem gånger så mycket skrov, sköld och laserskada som tidigare, så besättningarna som förut vann, ungefär sju piloter, förlorar nu ([hur stor besättning som behövs](#how-big-a-crew)). En för liten besättning förlorar striden: klanen behåller då de **70 poängen** från de fyra uppdragen, men linjen blir inte klar och betalar ingen [belöning till dig](#the-reward-for-you).
- En väktare betalar en stor pott, delad efter skada, och **varje pilot som gjort 5 % av skadan eller mer får en privat låda** med sin del av bytet, som bara hen ser och bara hen kan ta ([betalning och byte](#warden-pay-and-loot)).
- Ditt skepp visar de bonusar det har i fönstret **Boosters**, på ett eget kort ([var du ser dem](#the-three-boosts)).
- Linjen och bonusarna kräver ett spel av version 0.4.10 eller senare, kortet i fönstret Boosters version 0.4.12 eller senare.

![The Boosters window in flight: the Clan boosts card under the timed boosters lists your clan's tag and each boost with its bonus and level](../../img/wiki-img/shots/clan-boosters-window.jpg)
![Buying a level of a clan boost: the sheet shows the level, the bonus the whole fleet gets and the cost in clan points](../../img/wiki-img/shots/clan-boosts.jpg)
![Summoning a Warden for the clan](../../img/wiki-img/shots/clan-warden.jpg)

## Klanens utveckling {#clan-progression}

Klaner börjar på nivå 1 och kan uppgraderas till nivå 5. För att uppgradera klanen måste krediter betalas från **Klanbanken**. Uppgraderingar ökar medlemskapaciteten och de dagliga utbetalningsgränserna.

| Klannivå | Medlemsgräns | Daglig utbetalningsgräns (per medlem) | Uppgraderingskostnad (krediter) |
| :---: | :---: | :---: | :--- |
| **Nivå 1** | 10 | 1 000 000 KRD | — |
| **Nivå 2** | 25 | 2 000 000 KRD | 10 000 000 KRD |
| **Nivå 3** | 50 | 3 000 000 KRD | 100 000 000 KRD |
| **Nivå 4** | 75 | 4 000 000 KRD | 1 000 000 000 KRD |
| **Nivå 5** | 100 | 5 000 000 KRD | 10 000 000 000 KRD |

---

## Klanekonomi och beskattning {#clan-economy-taxation}

Klaner drivs av ett skattebaserat ekonomiskt system:

### 1. Daglig skatt {#1-daily-taxation}

- **Skattesats**: Ledaren eller vice ledarna kan ställa in en daglig skattesats mellan **0 % och 5 %**.
- **Automatisk indrivning**: En gång per dag (UTC) tar servern automatiskt ut skatt från alla klanmedlemmar.
- **Formel**: Skatten beräknas som `ClanTaxRate` av varje medlems aktuella kreditsaldo.
  - *Exempel*: Om du har 10 000 000 krediter och klanskatten är 2 % dras 200 000 krediter från ditt konto och sätts in i Klanbanken.
  - Frivilliga kreditdonationer kan också göras, upp till gränsen i nästa avsnitt.

### 2. Donationer {#2-donations}

- **Donera**: alla medlemmar kan skicka krediter till Klanbanken från sidan Klan. Dialogrutan visar vad du fortfarande kan skicka.
- **Donationsgräns**: en pilot kan skicka högst **1 000 000 krediter till klaner under valfria 24 timmar**, räknat över alla klaner piloten har varit med i. Att lämna en klan och gå med i en annan ger ingen ny gräns.
- **Ingen daglig nollställning**: de 24 timmarna glider. Varje donation slutar räknas exakt 24 timmar efter att den gjordes, och dialogrutan visar när den äldsta gör det och hur mycket som kommer tillbaka. En donation över det som är kvar avvisas helt.
- Den dagliga skatten är ingen donation och förbrukar inte din gräns.

### 3. Utbetalningar från banken {#3-bank-payouts}

- **Utbetalningsgränser**: Klanens ledare och officerare kan fördela krediter från Klanbanken till enskilda medlemmar.
- **Daglig gräns**: En medlem kan inte ta emot mer än `1,000,000 * ClanLevel` krediter i utbetalningar under en enda kalenderdag (UTC).

---

## Hierarki och roller {#hierarchy-roles}

Klaner använder en rollbaserad gradstruktur för att hantera behörigheter:

- **Ledare (roll 3)**: Har full administrativ åtkomst, inklusive uppgradering, att ställa in skatter, diplomati, befordringar, att avskeda medlemmar och att upplösa klanen.
- **Vice ledare (roll 2)**: Kan ställa in skattesatser, betala ut krediter, hantera diplomati och befordra eller degradera lägre grader.
- **Äldste (roll 1)**: Betrodd medlem som kan godkänna nya ansökningar till klanen.
- **Medlem (roll 0)**: Vanlig spelare utan administrativa behörigheter.

### Behörighetstabell {#permissions-table}

| Åtgärd | Ledare | Vice ledare | Äldste | Medlem |
| :--- | :---: | :---: | :---: | :---: |
| **Upplösa klanen** | ✅ | ❌ | ❌ | ❌ |
| **Uppgradera klanen** | ✅ | ❌ | ❌ | ❌ |
| **Ställa in skattesats** | ✅ | ✅ | ❌ | ❌ |
| **Betala ut krediter** | ✅ | ✅ | ❌ | ❌ |
| **Hantera diplomati** | ✅ | ✅ | ❌ | ❌ |
| **Köpa klanbonusar** | ✅ | ✅ | ❌ | ❌ |
| **Kalla fram klanväktaren** | ✅ | ✅ | ❌ | ❌ |
| **Befordra / avskeda** | ✅ | ✅* | ❌ | ❌ |
| **Godkänna ansökningar** | ✅ | ✅ | ✅ | ❌ |

*\*Vice ledare kan bara befordra, degradera eller avskeda medlemmar med lägre grad än sin egen.*

### När ledaren lämnar {#when-the-leader-leaves}

En ledare kan inte lämna en klan som fortfarande har andra medlemmar: befordra först en vice ledare till ledare (ledaren går då ner till vice ledare), eller lämna sist, vilket upplöser klanen. Om ledaren raderar sitt konto (Inställningar › Konto) går ledarskapet till den medlem som har högst grad, vid lika den som varit med längst; en ledare som är ensam i klanen upplöser den, banken inräknad.

---

## Dagslinje {#daily-line}

Varje klan får en **dagslinje** per dag: fem steg som hela klanen gör tillsammans, **i ordning**. De fyra första är uppdrag: skjuta ned så många utomjordingar, flyga så långt eller, vissa dagar, fälla svärmbossar. Det femte är en **klanväktare**, en boss som du kallar fram och förgör. Öppna **Gemenskap › Klan** och fliken **Operationer** för att se dagens linje, det öppna steget med sin stapel, din egen andel och tiden som är kvar.

### De fem stegen {#the-five-steps}

| Steg | Vad | Klanpoäng |
| :---: | :--- | ---: |
| 1 | Första uppdraget | 15 |
| 2 | Andra uppdraget | 15 |
| 3 | Tredje uppdraget | 20 |
| 4 | Fjärde uppdraget | 20 |
| 5 | Dagens klanväktare | 30 |
| | **En klar linje** | **100** |

- Bara det **öppna steget räknas**. En nedskjutning som sker medan steg 1 är öppet räknas för steg 1 och inget annat. När steg 1 är klart öppnas steg 2 från noll. Det du skjuter ned utöver ett stegs mål sparas inte till nästa.
- Ett steg betalar sina poäng **i samma stund som det är klart**. En klan som klarar de fyra uppdragen och sedan inte får ihop en besättning till väktaren, eller förlorar striden, behåller ändå **70 poäng**; [belöningen till dig](#the-reward-for-you) kommer först när linjen är klar.
- Allas arbete går in i **en gemensam räknare**: nedskjutningarna av det öppna stegets utomjording och sträckan som alla dina medlemmar flyger läggs ihop, så ingen behöver göra ett steg ensam.

### Dagen {#the-day}

- En klans dag är en **säsongsdag**: 24 timmar räknade från säsongens start ([Wipe-tidslinje](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule)). En ny linje börjar vid samma klockslag varje dag, och det är inte midnatt UTC (klanens dagliga skatt tas fortfarande ut vid midnatt UTC). Fliken Operationer räknar ned till bytet.
- En linje som inte blir klar **förfaller** när dagen tar slut. De steg som redan är klara behåller sina poäng, det öppna stegets framsteg försvinner och man kan inte ta igen det. Linjerna går på säsongsdag 1 till 29.
- Klanens piloter som är online får en Systemrad när den nya linjen börjar, när ett steg blir klart och **en timme före bytet** om linjen inte är klar.

### Svårighetsnivåer {#difficulty-tiers}

Varje dag tar spelet **medelnivån för de fem piloterna med högst nivå** i klanen (alla, om den har färre än fem) och sätter dagens nivå utifrån den:

| Nivå | Medelnivå | Väktare |
| :--- | :--- | :---: |
| Rekryt | under 4 | I |
| Veteran | 4 till under 7 | II |
| Elit | 7 eller mer | III |

Nivån avgör hur många utomjordingar uppdragen kräver, vilken utomjording det »tunga« steget kräver och hur stark väktaren är. **Poängen är desamma på varje nivå.** Nya piloter med låg nivå drar inte ned nivån: bara de fem bästa räknas.

### Vem som räknas {#who-counts}

- **Klanens totalsumma räknas.** Staplarna på fliken Operationer är hela klanens.
- **Ditt minimum.** För att få del av dagens belöning måste du göra **5 % av dagens arbete**, ungefär åtta minuters riktig jakt. Fliken visar det som »Ditt arbete i dag: 312 av 469 enheter«. En arbetsenhet är en sekund av spelande: en nedskjutning räknas som den tid det tar att hitta och förgöra den utomjordingen, och en flygsträcka som den tid det tar att flyga den. För en Veteran-klan är en Seeker värd ungefär 12 enheter, en Phantasm 22, en Bulwark 123 och 1 000 flugna enheter ungefär 5; minimum är 446 till 480 enheter, oavsett dag och nivå.
- **Minst tre medlemmar** måste ha nått sitt minimum innan ett steg kan bli klart. Är ett steg fullt och färre har nått det **väntar** det (»Steg 3 är fullt, men bara 2 medlemmar har nått sitt minimum«), och nedskjutningar av det stegets utomjording läggs fortfarande till arbetet för de medlemmar som gjorde dem tills den tredje kommer upp. En klan med färre än tre piloter kan inte göra klart något steg.
- **Vem som får en nedskjutning.** Piloten som får betalt för nedskjutningen och hens gruppkamrater inom 4 000 enheter som sköt de senaste 15 sekunderna ([Grupper](/wiki/03-Mechanics/Groups.md#sharing-kills)). En klan räknar en nedskjutning **en gång**, hur många av dess piloter som än var med i gruppen, och nedskjutningens arbete delas lika mellan dem. Två klaner i en grupp räknar den en gång var.
- **Vilka nedskjutningar.** Bara det öppna stegets utomjording: den vanliga Seeker, Phantasm, Bulwark eller Goombah. Svärmskepp, andra piloter och en väktares hjälpare räknas inte som dessa utomjordingar. Vilken värld som helst räknas, och en nedskjutning räknas mer i en starkare värld: **1 i Alpha, 1,5 i Beta, 2 i Gamma** ([Världar](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)). Ett bossteg räknar [svärmarnas](/wiki/05-Swarms/Swarms.md) bossar, en för varje klan som har en pilot som gjorde minst 5 % av skadan.
- **Flygning.** Ett patrullsteg räknar sträckan varje pilot flyger utanför skyddszonerna; fem piloter som flyger tillsammans lägger till fem gånger sträckan.
- **Gå med och lämna.** Det du gjorde förblir räknat om du lämnar. En pilot som går med räknas från det ögonblicket.

### De sju linjerna {#the-seven-lines}

Linjerna går i en cykel om sju: linjen för säsongsdag *d* har nummer 1 + ((*d* − 1) mod 7), så varje linje kommer tillbaka var sjunde dag. Siffrorna gäller en **Rekryt- / Veteran- / Elit-**klan. De två **Swarm Break**-linjerna kräver svärmbossar och kommer först från dag 4, när [svärmarna](/wiki/05-Swarms/Swarms.md) dyker upp. Alla siffror är gjorda för ungefär **2,6 timmars spelande totalt**, en halvtimme var för fem piloter (en uppskattning, inte en mätning).

| Linje | Säsongsdagar | Steg 1 | Steg 2 | Steg 3 | Steg 4 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Seeker Sweep | 1, 8, 15, 22, 29 | 150 / 300 / 425 Seeker | 115 000 / 155 000 / 185 000 enheter | 21 / 70 / 130 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah |
| Phantasm Purge | 2, 9, 16, 23 | 40 / 140 / 270 Phantasm | 60 / 120 / 170 Seeker | 175 000 / 230 000 / 275 000 enheter | 26 Phantasm / 15 Bulwark / 17 Goombah |
| Long Haul | 3, 10, 17, 24 | 290 000 / 385 000 / 460 000 enheter | 90 / 180 / 260 Seeker | 26 / 85 / 170 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah |
| Swarm Break I | 4, 11, 18, 25 | 75 / 150 / 220 Seeker | 3 Boss Seeker / 3 Boss Seeker / 2 Pirate Boss | 26 / 85 / 170 Phantasm | 30 Phantasm / 18 Bulwark / 21 Goombah |
| Heavy Iron | 5, 12, 19, 26 | 40 Phantasm / 24 Bulwark / 28 Goombah | 21 / 70 / 130 Phantasm | 175 000 / 230 000 / 275 000 enheter | 75 / 150 / 220 Seeker |
| Swarm Break II | 6, 13, 20, 27 | 75 / 150 / 220 Seeker | 21 / 70 / 130 Phantasm | 4 Boss Seeker / 1 Pirate Boss / 3 Pirate Boss | 350 000 / 460 000 / 550 000 enheter |
| Grand Round | 7, 14, 21, 28 | 100 / 210 / 300 Seeker | 26 / 85 / 170 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah | 230 000 / 305 000 / 365 000 enheter |

### Din belöning {#the-reward-for-you}

När linjen är klar, alltså när väktaren är förgjord, får varje medlem som nått minimum och fortfarande är i klanen en utbetalning, även om hen är offline. En linje som slutar utan väktaren betalar ingen belöning, vad de fyra uppdragen än gjort. Utbetalningen är fast: bonusar, boosters och världen ändrar den inte.

| Nivå | Krediter | Thulium |
| :--- | ---: | ---: |
| Rekryt | 5 000 | 20 |
| Veteran | 15 000 | 60 |
| Elit | 22 000 | 90 |

---

## Klanväktare {#clan-wardens}

En **klanväktare** är bossen i slutet av dagslinjen. Den är ingen av de publika [svärmarna](/wiki/05-Swarms/Swarms.md) som ströftar omkring i en sektor: din klan **kallar fram den** och **bara din klan kan skada den**. Tre väktare turas om, en per dag: dag 1 **Brood**, dag 2 **Siege**, dag 3 **Wrath**, dag 4 Brood igen, och så vidare (dag 15 är en Wrath-dag). Var och en finns i tre styrkor, **I, II och III**, som klanens nivå bestämmer. En väktare är en utomjording av en egen sort, som svärmarnas skepp: den räknas inte som Seeker, Phantasm eller någon annan utomjording. En väktare är mycket stark: den har fem gånger så mycket skrov, sköld och laserskada som före 0.4.13, så den är en strid för den största besättning som din klan kan få ihop ([hur stor besättning som behövs](#how-big-a-crew)).

| Väktare | Säsongsdagar | Roll | Hur den strider |
| :--- | :--- | :--- | :--- |
| **Brood Warden** | 1, 4, 7, 10 … | Kupans väktare: dela upp din eld | Fyra små **Brood Drones** läker dess skrov, och en ny kommer var 8:e sekund så länge färre än fyra lever. Skjut drönarna först, sedan väktaren. |
| **Siege Warden** | 2, 5, 8, 11 … | Belägringsbrytare: fortsätt röra dig | Den ströftar omkring och avfyrar en rak [Rivet-raket](/wiki/06-Items/Rockets.md#the-twelve-rockets) mot den pilot som träffade den först, och lagar sig själv. Två **Siege Escorts** lägger till laserelden. Fortsätt röra dig och turas om att vara måltavla. |
| **Wrath Warden** | 3, 6, 9, 12 … | Krigsherre: slå ned raseriet | Den strider på stället och lagar sig själv. Under halv skrovstyrka träffar dess lasrar **en och en halv gång så hårt**. Två **Wrath Guards** lägger till laserelden. Ta ned den snabbt och håll sköldarna uppe. |

### Kalla fram en väktare {#calling-a-warden}

- **När.** Efter att steg 4 är klart. En klan har **två frammaningar per dag**, bara en väktare ute åt gången, och dagen måste ha **minst 30 minuter** kvar.
- **Vem.** Ledaren eller en vice ledare.
- **Hur.** Under flygning: knappen **Kalla fram här** dyker upp på flygskärmen så fort steg 4 är klart och ber dig bekräfta. Var utanför skyddszonerna, i en koncerns sektor **x-2, x-3 eller x-4** (vilken koncern som helst) i din värld. Fliken Operationer visar dagens väktare, frammaningarna som är kvar och varför knappen är nedtonad, men en väktare kallas fram från skeppet.
- **Var den dyker upp.** 3 000 till 4 500 enheter från ditt skepp, i din värld: bara piloter i den världen kan nå den. Fliken rekommenderar **x-2 för en Rekryt-klan, x-3 för Veteran och x-4 för Elit**. De vanliga [PvP-reglerna](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) för sektorn du väljer gäller fortfarande.
- **Uppvärmning.** Den står **90 sekunder** skärmad och passiv (»startar upp«), och varje klanpilot som är online får veta var. Flyg dit medan den startar upp: när de 90 sekunderna är över är den aktiv. En kapsel under skyddszonsmärket på flygskärmen följer den: dess namn, ”startar upp” med tiden som är kvar, sedan ”aktiv” med dess sektor och tiden tills den drar sig tillbaka, och ”rasande” när en Wrath Warden har under halva skrovet.
- **Bara din klan.** Skott från andra klaners piloter ignoreras och får den inte att slå tillbaka.
- **Hur det tar slut.** När den förgörs. Den **drar sig tillbaka** 40 minuter efter att den aktiverades, när dagen tar slut, när ingen pilot i din klan har varit ute i flygning på dess karta på 2 minuter, eller när servern startar om (den frammaningen ges tillbaka). En väktare som drar sig tillbaka kostar en frammaning, och nästa anrop är samma väktare med full styrka.

### Strida mot en väktare {#fighting-a-warden}

- **En väktare strider mot den pilot som träffade den först**, som varje boss: låt besättningens kraftigaste skepp börja och använd [Shield Surge och Emergency Repair](/wiki/03-Mechanics/Abilities.md).
- **Ta med den största besättning du kan, med x2-ammunition** ([Lasrar](/wiki/06-Items/Lasers.md#laser-ammunition)). Besättningarna som vann före 0.4.13, ungefär sju piloter, förlorar nu. Tabellen nedan är en beräkning och bästa fallet: även i den förlorar tio piloter mot varje väktare, och den minsta besättning som kan vinna har 18 till 26 piloter med x2-ammunition och 28 till 39 med x1-ammunition.
- **Brood:** drönarna läker dess skrov, och en besättning som struntar i dem förlorar, även en stor. Skjut dem först och fortsätt skjuta dem: en ny kommer efter 8 sekunder.
- **Siege:** dess raketer är raka och ostyrda, så ett skepp som fortsätter röra sig väjer för de flesta. Fortsätt röra dig och turas om att vara måltavla.
- **Wrath:** när dess skrov är under hälften träffar varje salva en och en halv gång så hårt, så stridens andra hälft är den farliga. Ta ned första hälften snabbt, håll sköldarna uppe och spara Emergency Repair till raseriet.

### Hur stor besättning som behövs {#how-big-a-crew}

> [!NOTE]
> Sedan 0.4.13 har varje väktare och varje hjälpare **fem gånger** så mycket skrov, sköld, laserskada, självreparation och läkning som i 0.4.12 (fart, räckvidd och antalet hjälpare är desamma). Den tar fem gånger så lång tid att fälla och slår fem gånger så hårt hela tiden, så besättningarna som förut vann förlorar nu. **Vi har ännu inte slagits mot de nya väktarna i spelet: tiderna nedan är beräknade, inte uppmätta.** De visar besättningens **bästa fall**: besättningen sitter i de skepp och den utrustning som nivån är gjord för, varje pilot använder Shield Surge och Emergency Repair så snart de är redo, besättningen skjuter först på väktarens hjälpare när det är bättre, väktaren och dess hjälpare skjuter alla på piloten som träffade först, och ingen väjer. I 0.4.12 var samma beräkning mer hoppfull än striderna vi körde i själva spelet med skriptade piloter, så en riktig strid kan vara tuffare än tabellen, och en bra besättning kan klara sig bättre: ta den som en vägledning, inte ett löfte.

Tabellen visar bästa fallet; i spelet, ta med så många du kan.

| Besättning | Med x2-ammunition | Med x1-ammunition |
| :--- | :--- | :--- |
| 5 piloter | förlorar mot varje väktare; väktaren behåller 88 till 96 % av sitt skrov och sin sköld | förlorar |
| 10 piloter | förlorar mot varje väktare; väktaren behåller 55 till 87 % av sitt skrov och sin sköld | förlorar |
| 20 piloter | vinner bara mot Siege Warden I och II, på 8,5 till 8,6 minuter, och förlorar 7 skepp | förlorar |
| 30 piloter | vinner mot alla väktare på 4,5 till 5,1 minuter och förlorar 3 till 11 skepp | vinner bara mot Siege Warden I och II, på 12,6 till 12,8 minuter, och förlorar 10 skepp |

I beräkningen har den minsta besättning som vinner med x2-ammunition **18 till 26 piloter** (som minst mot Siege Warden I och II) och förlorar **9 till 17** skepp på köpet; med x1-ammunition har den **28 till 39** piloter och förlorar 13 till 27. En väktares lasrar slår med hundratals per salva i styrka I (240 till 645) och tusentals i styrka III (9 225 till 15 450), och dess hjälpare läggs till: skeppet den slåss mot faller på 19 till 59 sekunder, och sedan vänder den sig mot nästa, så även en besättning som vinner förlorar många skepp.

Tabellen gäller en besättning med utrustning för väktarens egen nivå. Svagare skepp klarar sig sämre. **Din** klans väktare matchar alltid **din** nivå, som klanens fem bästa piloter bestämmer, så ta med dem.

**En klan som är för liten för sin väktare** är inte utestängd. De fyra uppdragen betalar sina **70 poäng** vad som än händer med väktaren, poängen köper bonusar, och klanen kan kalla fram väktaren igen om den har en frammaning kvar (det finns två per dag): faller besättningen och håller sig borta drar sig väktaren tillbaka, vilket kostar en frammaning, och nästa anrop för tillbaka den med full styrka. Men linjen blir inte klar, så ingen får [belöningen till dig](#the-reward-for-you), och en klan som aldrig dödar sin väktare har alla 30 bonusnivåer tidigast på säsongsdag 18, inte på dag 12 ([hur lång tid det tar](#how-long-it-takes)).

### Väktarnas siffror {#warden-numbers}

Väktarna har samma siffror i varje värld (Alpha-siffrorna), och det har deras betalning också. Varje drönare, eskort eller vakt har siffrorna i den andra tabellen, och de står vid väktaren: en Brood Drone läker väktarens skrov, en Siege Escort eller en Wrath Guard avfyrar lasrar. En salva är skotten från alla lasrar på ett skepp under en sekund, slumpade mellan 80 och 100 % av siffran som visas; en Wrath Warden under halva skrovet slår en och en halv gång så hårt. Väktaren och dess hjälpare skjuter alla på piloten som väktaren slåss mot, så deras salvor läggs ihop: en Brood Warden III med sina fyra drönare lägger upp till 21 750 i sekunden på ett skepp. [Rivet-raketen](/wiki/06-Items/Rockets.md#the-twelve-rockets) från Siege Warden slumpas inte: den slår med högst **2 500** i styrka I, **5 000** i styrka II och **7 500** i styrka III, medan en pilots Rivet slumpas mellan ett lägsta och ett högsta tal. Den flyger rakt, så ett skepp som fortsätter röra sig missas.

| Väktare | Skrov | Sköld | Laserskada (en salva per sekund) | Hastighet | Laserräckvidd | Lagar sig själv (skrov per sekund) | Raket och sekunder mellan skotten |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| Brood Warden I | 830 000 | 680 000 | 645 | 90 | 600 | – | – |
| Brood Warden II | 1 440 000 | 1 180 000 | 3 885 | 90 | 700 | – | – |
| Brood Warden III | 5 300 000 | 4 350 000 | 15 450 | 90 | 800 | – | – |
| Siege Warden I | 715 000 | 585 000 | 240 | 110 | 600 | 1 075 | Rivet I: 24 |
| Siege Warden II | 1 240 000 | 1 015 000 | 1 455 | 110 | 700 | 1 875 | Rivet II: 12 |
| Siege Warden III | 4 575 000 | 3 725 000 | 9 225 | 110 | 800 | 6 925 | Rivet III: 8 |
| Wrath Warden I | 815 000 | 665 000 | 480 | 90 | 700 | 1 075 | – |
| Wrath Warden II | 1 410 000 | 1 155 000 | 2 910 | 90 | 800 | 1 875 | – |
| Wrath Warden III | 5 200 000 | 4 250 000 | 12 300 | 90 | 900 | 6 925 | – |

| Hjälpare | Hur många | Skrov | Sköld | Laserskada (en salva per sekund) | Hastighet | Läker väktaren (skrov per sekund) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Brood Drone I | 4 | 3 500 | 2 500 | 60 | 170 | 600 |
| Brood Drone II | 4 | 6 000 | 4 500 | 390 | 170 | 1 050 |
| Brood Drone III | 4 | 20 000 | 17 500 | 1 575 | 170 | 3 850 |
| Siege Escort I | 2 | 21 500 | 17 500 | 30 | 175 | – |
| Siege Escort II | 2 | 37 000 | 30 500 | 225 | 175 | – |
| Siege Escort III | 2 | 137 500 | 112 500 | 1 425 | 175 | – |
| Wrath Guard I | 2 | 24 500 | 20 000 | 90 | 180 | – |
| Wrath Guard II | 2 | 42 500 | 34 500 | 585 | 180 | – |
| Wrath Guard III | 2 | 155 000 | 127 500 | 2 475 | 180 | – |

### Betalning och byte {#warden-pay-and-loot}

En väktare betalar tio gånger så mycket som en hög av nivåns tunga utomjording: **300 Phantasm** för en väktare I, **240 Bulwark** för en II och **160 Goombah** för en III. Det är en enda pott, delad efter skada mellan de piloter som gjort minst 5 % av skadan, på samma sätt som för ledaren i en [svärm](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays). Dina [klanbonusar](#what-the-boosts-apply-to) gäller din andel. Potten växer inte med skadan du tar, ammunitionen du bränner eller skeppen du förlorar.

| Väktarens styrka | Krediter | Thulium | Erfarenhet (XP) | Heder |
| :--- | ---: | ---: | ---: | ---: |
| I | 900 000 | 3 600 | 90 000 | 1 800 |
| II | 1 200 000 | 6 000 | 192 000 | 2 400 |
| III | 2 400 000 | 12 000 | 480 000 | 3 840 |

**Varje pilot som får betalt får en egen låda** vid vraket, med sin del av bytet. Tabellen listar vad hela nedskjutningen slumpar fram, och en pilot som gjort 20 % av skadan slumpar för ungefär en femtedel av varje mängd: en del avrundas slumpmässigt, så medelvärdet är exakt och en liten del får ändå ibland en sällsynt rad. **Bara du ser din låda och bara du kan ta den**, inte din klan och inte din grupp, och den ligger kvar i **10 minuter**, utan väntan på 30 sekunder ([privata lådor](/wiki/03-Mechanics/Cargo.md#private-boxes)). I en [grupp](/wiki/03-Mechanics/Groups.md#sharing-kills) räknas medlemmarna som en enda pilot för de 5 %, och dess del delas som varje nedskjutning delas i en grupp (kamraterna som är nära och skjuter, efter nivå): varje kamrat som får en del får en privat låda med den delen. Spelloggen berättar din del. En pilot som gjort mindre än 5 % får inget betalt och ingen låda läggs ut åt hen; Spelloggen säger det. En chans inom parentes gäller för vart och ett av de angivna kasten: (5 × 50 %) är fem kast med 50 % chans vardera.

| Väktare | Föremål | I | II | III |
| :--- | :--- | :---: | :---: | :---: |
| Brood Warden | Ship Fragment | 30–50 | 80–120 | 150–250 |
| Brood Warden | Advanced Plasma | 2 000–4 000 | 6 000–12 000 | – |
| Brood Warden | Daraxium | 10–20 (5 × 50 %) | – | – |
| Brood Warden | Nyxite | – | 20–40 (5 × 50 %) | – |
| Brood Warden | Ultra Core | – | – | 6 000–10 000 |
| Brood Warden | Quorvium | – | – | 50–100 (60 %) |
| Siege Warden | Ship Fragment | 20–40 | 60–100 | 120–200 |
| Siege Warden | Siphon Battery | 2 000–4 000 | 6 000–10 000 | 16 000–24 000 |
| Siege Warden | Raket som köps för krediter (en sort, slumpad) | 20–30 | 50–80 | 80–120 |
| Siege Warden | Reinforced Hull Plate | – | 10 (30 %) | – |
| Siege Warden | Episk raket (en sort, slumpad) | – | – | 10–20 (50 %) |
| Wrath Warden | Ship Fragment | 40–60 | 80–120 | – |
| Wrath Warden | Cataclysite | 30–50 | 50–100 | – |
| Wrath Warden | Reinforced Hull Plate | 10 (25 %) | 10 (50 %) | 10–20 (70 %) |
| Wrath Warden | Power Core | – | 10 (15 %) | 10 (35 %) |
| Wrath Warden | Quorvium | – | – | 50–100 (70 %) |
| Wrath Warden | Ancient Control Unit | – | – | 10 (8 %) |

En väktare räknas under sitt eget namn i din nedskjutningsstatistik och ger PvE-poäng till din [grad](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points): **13 till 35** för ledaren, efter väktare och styrka (en väktare III är värd mest), och **1 till 6** för varje hjälpare, mer för en starkare besättning.

---

## Klanpoäng och bonusar {#clan-points-and-boosts}

Klanpoängen tillhör klanen. Varje steg som klanen gör klart ökar dess saldo. **Ledaren och vice ledarna** lägger ut det på kortet **Flottbonusar** på fliken Operationer: tre bonusar med tio nivåer vardera, och varje medlem har dem direkt. Ett köp är slutgiltigt: ingen återbetalning och ingen omfördelning.

### De tre bonusarna {#the-three-boosts}

| Bonus | Nivåer | Per nivå | Högsta nivå | Gäller för |
| :--- | :---: | :---: | :---: | :--- |
| **Flottskada** | 10 | +0,5 % | +5 % | Laserskada mot utomjordingar och piloter |
| **Flott-Thulium** | 10 | +1 % | +10 % | Thulium från nedskjutningar och uppdragsbelöningar |
| **Flottkrediter** | 10 | +1 % | +10 % | Krediter från nedskjutningar och uppdragsbelöningar |

**Var du ser dem.** Under flygning visar fönstret **Boosters** de bonusar ditt skepp har på ett eget kort, **Flottbonusar**, under de tidsbegränsade boostersen: din klans tagg, sedan en rad per bonus med dess värde och nivå (Nivå 3/10). De har ingen timer, eftersom en klanbonus gäller så länge du är med i klanen. För musen över en rad för att se vad den verkar på. En klan som inte köpt något än visar ”Din flotta har inga bonusar än”, och en pilot utan klan ser inget kort. **Översiktens** Boosters-kort och en pilots profil listar dem också. Kortet visar vad ditt skepp tillämpar, så som servern säger det till spelet, så en nivå som officerarna just köpt syns direkt. Ett spel äldre än 0.4.12 tillämpar bonusarna men visar inget kort.

### Priser {#boost-prices}

Priset för en nivå är **22 klanpoäng plus 4 för varje nivå före den**, och det är detsamma för de tre bonusarna: 400 poäng för en bonus, **1 200 för alla tre**, vilket är tolv klara linjer.

| Nivå | Pris | Summa för den här bonusen | Flottskada | Flott-Thulium | Flottkrediter |
| :---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 22 | 22 | +0,5 % | +1 % | +1 % |
| 2 | 26 | 48 | +1 % | +2 % | +2 % |
| 3 | 30 | 78 | +1,5 % | +3 % | +3 % |
| 4 | 34 | 112 | +2 % | +4 % | +4 % |
| 5 | 38 | 150 | +2,5 % | +5 % | +5 % |
| 6 | 42 | 192 | +3 % | +6 % | +6 % |
| 7 | 46 | 238 | +3,5 % | +7 % | +7 % |
| 8 | 50 | 288 | +4 % | +8 % | +8 % |
| 9 | 54 | 342 | +4,5 % | +9 % | +9 % |
| 10 | 58 | 400 | +5 % | +10 % | +10 % |

### Vad bonusarna gäller för {#what-the-boosts-apply-to}

- **Flottskada** läggs till all laserskada ditt skepp gör: mot utomjordingar, svärmskepp, väktare och andra piloter. Den **påverkar inte raketer**, av något slag.
- **Flott-Thulium och Flottkrediter** läggs till betalningen för nedskjutningar av utomjordingar (dina egna, din andel av en boss och din andel av en gruppnedskjutning) och till belöningen för varje uppdrag du hämtar ut, nivå-, Station- eller Utmaningsuppdrag ([Uppdrag](/wiki/03-Mechanics/Quests.md#rewards)). De **påverkar inte** [Skylab](/wiki/03-Mechanics/Skylab.md#credit-farm-and-thulium-farm)-farmarna, bankutbetalningar, bonuskoder eller belöningen för dagslinjen.
- **De läggs ihop med dina andra bonusar** (boosters som Laser Damage Booster, buffarna i [butiken för permanenta buffar](/wiki/03-Mechanics/Wipe-Timeline.md#the-permanent-buff-store)): procenten läggs ihop. Laserförstärkare (Amps) hör inte dit: de ger fast skada, och procenten gäller summan. Fem poäng Flottskada bredvid 50 från andra källor blir 55, vilket är 3,3 % mer skada än förut.
- **En bråkdel går inte förlorad.** En bonus lägger ofta till mindre än en enhet på en nedskjutning: 10 % av en Seekers 4 Thulium är 0,4. Spelet sparar bråkdelen och betalar ut den med enheterna från dina nästa nedskjutningar, så att tio Seekers betalar de 4 du har rätt till. Bråkdelen du håller i försvinner när du loggar ut.
- **Gå med och lämna.** En pilot har bonusarna från det att hen går med i klanen och förlorar dem i samma stund som hen lämnar, avskedas eller klanen upplöses. Klanen behåller sina nivåer.

### Hur lång tid det tar {#how-long-it-takes}

En klan som klarar varje linje tjänar 100 poäng om dagen. Om officerarna köper jämnt över de tre bonusarna har den **4 nivåer efter första linjen, 10 efter tredje, 16 efter femte och alla 30 på säsongsdag 12**. Fjorton linjer är över när dag 15 börjar, så en sådan klan har två linjer att gå på. En dag som inte blir klar betalar ändå för de steg som gjorts: en klan som klarar de fyra uppdragen men aldrig dödar sin väktare tjänar 70 poäng om dagen och har alla 30 nivåer tidigast på säsongsdag 18. Efter sista nivån fortsätter linjen och betalar fortfarande din belöning; poängen fortsätter läggas till det klanen tjänat den här säsongen, vilket verktygstipset för klanpoängen på kortet Flottbonusar visar.

### Poäng och wipe {#clan-points-and-the-wipe}

Vid varje wipe **börjar klanens poäng, bonusnivåer och linjer om från början**, så varje säsong är ett nytt lopp mot fulla bonusar. Själva klanen, dess medlemmar, dess bank och dess skatt förblir som de är.

---

## Diplomati {#diplomacy}

Klaner kan upprätta formella diplomatiska förbindelser med andra organisationer genom att ange målklanens tagg:

- **Allians**: Formellt allierade klaner. Vänlig status visas på kartan.
- **Icke-angreppspakt (NAP)**: Man kommer överens om att inte inleda fientligheter.
- **Krig**: Formell krigsförklaring. Krigsmål kan angripas var som helst utan straff.

---

## Ta med en vän {#bringing-a-friend}

En vän som är ny i spelet kan gå med med din personliga inbjudningskod och får ett startpaket; se [Bjud in vänner](/wiki/03-Mechanics/Invite-Friends.md). Väl i spelet kan vännen ansöka till din klan som vilken pilot som helst.
