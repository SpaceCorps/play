<!-- wiki-i18n source: b98e7995bde4597b -->
<!-- wiki-i18n title: Klaner -->
# Klaner {#clans}

Att grunda en klan eller gå med i en låter dig samla resurser, uppgradera den gemensamma banken, ställa in skattesatser, samordna dig med medlemmar i din fraktion och sköta diplomati. En klan har också arbete att göra tillsammans: varje dag får den en **dagslinje** av uppdrag som slutar med en boss som bara klanen kan skada, och poängen den tjänar köper **permanenta bonusar** åt varje medlem. (På spelets Klan-sida kallas en klan en *flotta*, och dess poäng och bonusar heter där flottpoäng och flottbonusar.)

**På en minut**

- Varje säsongsdag får din klan en [dagslinje](#daily-line): fyra uppdrag som görs i ordning (skjuta ned utomjordingar, flyga en sträcka, vissa dagar fälla svärmbossar), sedan en [klanväktare](#clan-wardens), en boss som du kallar fram och som bara din klan kan skada.
- Varje klart steg betalar klanpoäng direkt: 15, 15, 20, 20 och 30, alltså **100 poäng** för en hel linje.
- Ledaren och vice ledarna lägger poängen på tre [bonusar](#clan-points-and-boosts) med tio nivåer vardera: **Skada** (upp till +5 %), **Thulium** (upp till +10 %) och **Krediter** (upp till +10 %).
- En klan som klarar varje linje har köpt alla nivåer på **säsongsdag 12**. Poäng och nivåer börjar om vid varje wipe.
- Du behöver minst **tre medlemmar** som gjort sin del och ungefär fem piloter för striden mot väktaren.
- Linjen och bonusarna kräver ett spel av version 0.4.10 eller senare.

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
- Ett steg betalar sina poäng **i samma stund som det är klart**. En klan som klarar de fyra uppdragen och sedan inte får ihop en besättning till väktaren behåller ändå **70 poäng**.
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

När linjen är klar får varje medlem som nått minimum och fortfarande är i klanen en utbetalning, även om hen är offline. Utbetalningen är fast: bonusar, boosters och världen ändrar den inte.

| Nivå | Krediter | Thulium |
| :--- | ---: | ---: |
| Rekryt | 5 000 | 20 |
| Veteran | 15 000 | 60 |
| Elit | 22 000 | 90 |

---

## Klanväktare {#clan-wardens}

En **klanväktare** är bossen i slutet av dagslinjen. Den är ingen av de publika [svärmarna](/wiki/05-Swarms/Swarms.md) som ströftar omkring i en sektor: din klan **kallar fram den** och **bara din klan kan skada den**. Tre väktare turas om, en per dag: dag 1 **Brood**, dag 2 **Siege**, dag 3 **Wrath**, dag 4 Brood igen, och så vidare (dag 15 är en Wrath-dag). Var och en finns i tre styrkor, **I, II och III**, som klanens nivå bestämmer. En väktare är en utomjording av en egen sort, som svärmarnas skepp: den räknas inte som Seeker, Phantasm eller någon annan utomjording.

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
- **Uppvärmning.** Den står **90 sekunder** skärmad och passiv (»startar upp«), och varje klanpilot som är online får veta var. Flyg dit medan den startar upp: när de 90 sekunderna är över är den aktiv.
- **Bara din klan.** Skott från andra klaners piloter ignoreras och får den inte att slå tillbaka.
- **Hur det tar slut.** När den förgörs. Den **drar sig tillbaka** 40 minuter efter att den aktiverades, när dagen tar slut, när ingen pilot i din klan har varit ute i flygning på dess karta på 2 minuter, eller när servern startar om (den frammaningen ges tillbaka). En väktare som drar sig tillbaka kostar en frammaning, och nästa anrop är samma väktare med full styrka.

### Strida mot en väktare {#fighting-a-warden}

- **En väktare strider mot den pilot som träffade den först**, som varje boss: låt besättningens kraftigaste skepp börja och använd [Shield Surge och Emergency Repair](/wiki/03-Mechanics/Abilities.md).
- **Ta med x2-ammunition** ([Lasrar](/wiki/06-Items/Lasers.md#laser-ammunition)). En besättning på fem vinner även med x1-ammunition, långsammare; en på tre gör det inte.
- **Brood:** drönarna läker dess skrov, och en besättning på tre som struntar i dem förlorar. Skjut dem först: en dör på en sekund eller mindre under eld från fem piloter, och nästa kommer efter 8 sekunder.
- **Siege:** dess raketer är raka och ostyrda, så ett skepp som fortsätter röra sig väjer för de flesta. Fortsätt röra dig och turas om att vara måltavla.
- **Wrath:** när dess skrov är under hälften träffar varje salva en och en halv gång så hårt, så stridens andra hälft är den farliga. Ta ned första hälften snabbt, håll sköldarna uppe och spara Emergency Repair till raseriet.

### Hur stor besättning som behövs {#how-big-a-crew}

> [!NOTE]
> Dessa tider är **uträknade** från siffrorna nedan, inte mätta i spelet: en besättning i de skepp och med den utrustning som nivån är gjord för, alla skjuter på väktaren. Ett streck betyder att vi inte har räknat ut det.

| Besättning | Med x2-ammunition | Med x1-ammunition |
| :--- | :--- | :--- |
| 2 piloter | förlorar mot Brood och Siege; vinner mot Wrath på ungefär 17 minuter | – |
| 3 piloter | vinner på 9 till 10 minuter, knappt: tankens skrov är lågt på slutet och en pilot kan gå förlorad | förlorar |
| 5 piloter | vinner på ungefär 5 minuter | vinner på 12 till 14 minuter |
| 7 piloter | vinner på ungefär 3,4 minuter | – |
| 10 piloter | vinner på ungefär 2,3 minuter | – |

En besättning på lägre nivå än väktaren förlorar: en Rekryt-besättning på fem kan inte döda en Veteran-väktare, och en Veteran-besättning ingen Elit-väktare. **Din** klans väktare matchar alltid **din** nivå.

### Väktarnas siffror {#warden-numbers}

Väktarna har samma siffror i varje värld (Alpha-siffrorna), och det har deras betalning också. Varje drönare, eskort eller vakt har siffrorna i den andra tabellen, och de står vid väktaren: en Brood Drone läker väktarens skrov, en Siege Escort eller en Wrath Guard avfyrar lasrar.

| Väktare | Skrov | Sköld | Laserskada (en salva per sekund) | Hastighet | Laserräckvidd | Lagar sig själv (skrov per sekund) | Raket och sekunder mellan skotten |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| Brood Warden I | 166 000 | 136 000 | 43 | 90 | 600 | – | – |
| Brood Warden II | 288 000 | 236 000 | 259 | 90 | 700 | – | – |
| Brood Warden III | 1 060 000 | 870 000 | 1 030 | 90 | 800 | – | – |
| Siege Warden I | 143 000 | 117 000 | 16 | 110 | 600 | 215 | Rivet I: 24 |
| Siege Warden II | 248 000 | 203 000 | 97 | 110 | 700 | 375 | Rivet II: 12 |
| Siege Warden III | 915 000 | 745 000 | 615 | 110 | 800 | 1 385 | Rivet III: 8 |
| Wrath Warden I | 163 000 | 133 000 | 32 | 90 | 700 | 215 | – |
| Wrath Warden II | 282 000 | 231 000 | 194 | 90 | 800 | 375 | – |
| Wrath Warden III | 1 040 000 | 850 000 | 820 | 90 | 900 | 1 385 | – |

| Hjälpare | Hur många | Skrov | Sköld | Laserskada (en salva per sekund) | Hastighet | Läker väktaren (skrov per sekund) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Brood Drone I | 4 | 700 | 500 | 4 | 170 | 120 |
| Brood Drone II | 4 | 1 200 | 900 | 26 | 170 | 210 |
| Brood Drone III | 4 | 4 000 | 3 500 | 105 | 170 | 770 |
| Siege Escort I | 2 | 4 300 | 3 500 | 2 | 175 | – |
| Siege Escort II | 2 | 7 400 | 6 100 | 15 | 175 | – |
| Siege Escort III | 2 | 27 500 | 22 500 | 95 | 175 | – |
| Wrath Guard I | 2 | 4 900 | 4 000 | 6 | 180 | – |
| Wrath Guard II | 2 | 8 500 | 6 900 | 39 | 180 | – |
| Wrath Guard III | 2 | 31 000 | 25 500 | 165 | 180 | – |

### Betalning och byte {#warden-pay-and-loot}

En väktare betalar lika mycket som en hög av nivåns tunga utomjording: **30 Phantasm** för en väktare I, **24 Bulwark** för en II och **16 Goombah** för en III. Det är en enda pott, delad efter skada mellan de piloter som gjort minst 5 % av skadan, på samma sätt som för ledaren i en [svärm](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays). Dina [klanbonusar](#what-the-boosts-apply-to) gäller din andel. Enligt vår beräkning täcker kredierna den x1-ammunition som en besättning på fem bränner, och x2-ammunition kostar mer Thulium än väktaren betalar: det är en strid om poängen och lådan.

| Väktarens styrka | Krediter | Thulium | Erfarenhet (XP) | Heder |
| :--- | ---: | ---: | ---: | ---: |
| I | 90 000 | 360 | 9 000 | 180 |
| II | 120 000 | 600 | 19 200 | 240 |
| III | 240 000 | 1 200 | 48 000 | 384 |

Väktaren släpper **en låda** åt den pilot som gjorde mest skada; den är pilotens och hens klans i 30 sekunder ([Last](/wiki/03-Mechanics/Cargo.md)). En chans inom parentes gäller för vart och ett av de angivna kasten: (5 × 50 %) är fem kast med 50 % chans vardera.

| Väktare | Föremål | I | II | III |
| :--- | :--- | :---: | :---: | :---: |
| Brood Warden | Ship Fragment | 3–5 | 8–12 | 15–25 |
| Brood Warden | Advanced Plasma | 100–200 | 300–600 | – |
| Brood Warden | Daraxium | 1–2 (5 × 50 %) | – | – |
| Brood Warden | Nyxite | – | 2–4 (5 × 50 %) | – |
| Brood Warden | Ultra Core | – | – | 300–500 |
| Brood Warden | Quorvium | – | – | 5–10 (60 %) |
| Siege Warden | Ship Fragment | 2–4 | 6–10 | 12–20 |
| Siege Warden | Siphon Battery | 100–200 | 300–500 | 800–1 200 |
| Siege Warden | Raket som köps för krediter (en sort, slumpad) | 2–3 | 5–8 | 8–12 |
| Siege Warden | Reinforced Hull Plate | – | 1 (30 %) | – |
| Siege Warden | Episk raket (en sort, slumpad) | – | – | 1–2 (50 %) |
| Wrath Warden | Ship Fragment | 4–6 | 8–12 | – |
| Wrath Warden | Cataclysite | 3–5 | 5–10 | – |
| Wrath Warden | Reinforced Hull Plate | 1 (25 %) | 1 (50 %) | 1–2 (70 %) |
| Wrath Warden | Power Core | – | 1 (15 %) | 1 (35 %) |
| Wrath Warden | Quorvium | – | – | 5–10 (70 %) |
| Wrath Warden | Ancient Control Unit | – | – | 1 (8 %) |

En väktare räknas under sitt eget namn i din nedskjutningsstatistik och ger PvE-poäng till din [grad](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points): **10, 15 eller 25** för ledaren av en väktare I, II eller III, och 1 för varje hjälpare.

---

## Klanpoäng och bonusar {#clan-points-and-boosts}

Klanpoängen tillhör klanen. Varje steg som klanen gör klart ökar dess saldo. **Ledaren och vice ledarna** lägger ut det på kortet **Flottbonusar** på fliken Operationer: tre bonusar med tio nivåer vardera, och varje medlem har dem direkt. Ett köp är slutgiltigt: ingen återbetalning och ingen omfördelning.

### De tre bonusarna {#the-three-boosts}

| Bonus | Nivåer | Per nivå | Högsta nivå | Gäller för |
| :--- | :---: | :---: | :---: | :--- |
| **Flottskada** | 10 | +0,5 % | +5 % | Laserskada mot utomjordingar och piloter |
| **Flott-Thulium** | 10 | +1 % | +10 % | Thulium från nedskjutningar och uppdragsbelöningar |
| **Flottkrediter** | 10 | +1 % | +10 % | Krediter från nedskjutningar och uppdragsbelöningar |

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
- **De läggs ihop med dina andra bonusar** (boosters som Damage Amp, buffarna i [butiken för permanenta buffar](/wiki/03-Mechanics/Wipe-Timeline.md#the-permanent-buff-store)): procenten läggs ihop. Laserförstärkare (Amps) hör inte dit: de ger fast skada, och procenten gäller summan. Fem poäng Flottskada bredvid 50 från andra källor blir 55, vilket är 3,3 % mer skada än förut.
- **En bråkdel går inte förlorad.** En bonus lägger ofta till mindre än en enhet på en nedskjutning: 10 % av en Seekers 4 Thulium är 0,4. Spelet sparar bråkdelen och betalar ut den med enheterna från dina nästa nedskjutningar, så att tio Seekers betalar de 4 du har rätt till. Bråkdelen du håller i försvinner när du loggar ut.
- **Gå med och lämna.** En pilot har bonusarna från det att hen går med i klanen och förlorar dem i samma stund som hen lämnar, avskedas eller klanen upplöses. Klanen behåller sina nivåer.

### Hur lång tid det tar {#how-long-it-takes}

En klan som klarar varje linje tjänar 100 poäng om dagen. Om officerarna köper jämnt över de tre bonusarna har den **4 nivåer efter första linjen, 10 efter tredje, 16 efter femte och alla 30 på säsongsdag 12**. Fjorton linjer är över när dag 15 börjar, så en sådan klan har två linjer att gå på. En dag som inte blir klar betalar ändå för de steg som gjorts. Efter sista nivån fortsätter linjen och betalar fortfarande din belöning; poängen fortsätter läggas till det klanen tjänat den här säsongen, vilket verktygstipset för klanpoängen på kortet Flottbonusar visar.

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
