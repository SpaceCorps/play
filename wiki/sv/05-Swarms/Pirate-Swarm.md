<!-- wiki-i18n source: 33448f95d2520b3a -->
<!-- wiki-i18n title: Pirate-svärm -->
# Pirate-svärm {#pirate-swarm}

Pirate-svärmen är en **Pirate Boss** med sina **Pirate Scouts**: ett stort, långsamt skepp som inte angriper någon och svarar med raketer, och en flock snabbare skepp som vaktar och läker det. Den håller till i sektorerna mellan en koncerns bas och dess gräns, där spelets mellannivåer spelas, och är en lång strid för en grupp piloter, inte en snabb nedskjutning.

## I korthet {#at-a-glance}

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Var**: Sektorerna `x-2` och `x-3` i varje koncern
- **Hur många**: En i var och en av de sektorerna, 6 i varje värld
- **Dyker upp**: Från säsongsdag 4 till wipen (Beta och Gamma: från säsongsdag 1)
- **Ledare**: Pirate Boss
- **Följeslagare**: Upp till 5 × Pirate Scout, en ny var 10 s
- **Följeslagarna håller sig inom**: högst 900 enheter från ledaren
- **Läkning**: Varje Pirate Scout inom 600 enheter från ledaren läker dess skrov, 40 HP per sekund i Alpha
- **När ledaren förstörs**: Följeslagarna försvinner 1 min efter att ledaren förstörts, om de inte just attackerar
- **Kommer tillbaka**: {{guide:vitals.respawn@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} efter att ledaren förstörts, i samma sektor
- **Meddelanden**: Piloterna i sektorn får veta när ledaren dyker upp och när den förstörs. Det är systemrader: de syns på chattens flik **System**, med en räknare för olästa rader, och inte i **Global** eller **Lokal**. Dödsloggen nämner piloten som nedskjutningen tillskrivs.

<!-- pirate-glance:end -->

## Medlemmarna {#the-members}

- **Pirate Boss**: ett skepp som bygger på Ironclad, med en del av dess styrka (värdena står nedan). Den är passiv och skjuter **inga lasrar**: dess enda vapen är en **rak raket** ([Raketer](/wiki/06-Items/Rockets.md); vilken beror på sektorn, se tabellen) mot piloten som attackerade den, och den drar vidare medan den skjuter. Den reparerar aldrig sitt skrov själv. Dess [tre steg](#the-leaders-three-steps) och en [specialförmåga](/wiki/03-Mechanics/Special-Abilities.md) kan ändra på det.
- **Pirate Scout**: ett skepp som bygger på Kitefin, med en del av dess styrka. Scouts attackerar varje pilot som kommer nära, håller sig nära bossen, och var och en som är nära bossen läker dess skrov.

## Hur striden går till {#how-the-fight-goes}

- **Skjut på bossen, inte på Scouts.** Scouts läker bossen, men läkningen är liten jämfört med dess skrov, och en ny Scout kommer så ofta som listan *I korthet* säger: en grupp som skjuter Scouts först kommer aldrig före dem, och bara en mycket stor grupp kan röja dem och behöver ändå längre tid på bossen än en grupp som lät dem vara. Scouts kostar dig tid, de avgör inte striden.
- **Led bort Scouts.** En Scout läker bara så länge den är inom bossens räckhåll, så en Scout som följer dig utanför det läker ingenting, och en Ostirion är snabbare än en Scout.
- **Fortsätt röra dig.** Bossens raket är rak och ostyrd: ett skepp som håller sig i rörelse undviker den, ett som står still blir träffat.
- **Ta med en grupp.** Tre piloter i Ostirion med ammunition x2 fäller den på `x-2` utan att förlora något skepp, om än med knapp nöd, och förstörs på `x-3`, även medan träffarna fördelas; fyra fäller den på ungefär tre minuter i Alpha. Med ammunition x4 fäller tre den på `x-3` på ungefär två minuter. Fem fäller den på ungefär två och en halv minut när träffarna fördelas och på ungefär tre när en pilot tar all eld, och förlorar då två skepp: en grupp där en pilot tar all eld behöver fem. I Beta krävs fem piloter och i Gamma sju, med fördelade träffar (bossen är större där och dess Scouts läker mer). I Alpha, på `x-3` med ammunition x2, klarar en Ostirion ensam det inte, en Paragon ensam klarar det inte heller, och två Paragon klarar det med god marginal. I Beta och Gamma, på `x-3`, förstörs en Paragon ensam med ammunition x2 och med ammunition x4. Bossen går mot den första piloten som träffade den, så låt det tåligaste skeppet börja, och använd dina förmågor (Emergency Repair, Shield Surge: [Förmågor](/wiki/03-Mechanics/Abilities.md)) i en så lång strid. Piloter som fortfarande är nivå 2 eller 3 är för svaga för den, även där de flyger: håll dig borta tills du är starkare.
- **Bossen kommer tillbaka** efter tiden i listan *I korthet*, i samma sektor.

## Ledarens tre steg {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Striden har tre steg ([hur de fungerar](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); vart och ett sker en gång.

- **I början**: Avfyrar en solfjäder av 3 raketer, 12 grader isär, mot den första piloten som träffade den.
- **Under två tredjedelar**: Kallar på 5 fler Pirate Scouts på en gång, högst 10 levande. De betalar ingenting och lämnar efter 45 s.
- **Under en tredjedel**: Flyger med farten ×1,8 till närmaste port i 10 s, och vänder sedan om mot piloterna.

<!-- mob-ladder:end -->

## Belöningar och byte {#rewards-and-drops}

Pirate Boss betalar efter den strid den är: en minuts strid mot den betalar mer än en minuts strid mot en Goombah. Betalningen delas efter skada mellan piloterna som stred mot den ([hur nedskjutningen av en boss betalar](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Dess låda är för piloten som gjorde mest skada och kan innehålla en **Reinforced Hull Plate**, raketer och ammunition. Dess låda är värd lite mindre än hälften av vad själva nedskjutningen betalar. Scouts betalar lite och tappar ingenting.

## Värdena {#the-numbers}

Värdena för svärmens skepp i de tre världarna ([Världar](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss

Bygger på Ironclad med 50 % av skrov, sköld och skada; hastighet och räckvidd är förlagans. Skjuter en rak raket var 5 s: [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) i `x-2`, [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) i `x-3`.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | {{guide:vitals.hull@Pirate Boss#1}} | {{guide:vitals.hull@Pirate Boss#2}} | {{guide:vitals.hull@Pirate Boss#3}} |
| Sköld | {{guide:vitals.shield@Pirate Boss#1}} | {{guide:vitals.shield@Pirate Boss#2}} | {{guide:vitals.shield@Pirate Boss#3}} |
| Laserskada (en salva per sekund) | ingen | ingen | ingen |
| Hastighet | {{guide:vitals.speed@Pirate Boss#1}} | {{guide:vitals.speed@Pirate Boss#2}} | {{guide:vitals.speed@Pirate Boss#3}} |
| Laserräckvidd | – | – | – |
| Aggroradie | bara när den attackeras | bara när den attackeras | bara när den attackeras |
| Raketskada, högst | {{guide:behaviour.ability:rocket.damage@Pirate Boss#1}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#2}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#3}} |
| Krediter | {{guide:spoils.pay.credits@Pirate Boss#1}} | {{guide:spoils.pay.credits@Pirate Boss#2}} | {{guide:spoils.pay.credits@Pirate Boss#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Boss#1}} | {{guide:spoils.pay.thulium@Pirate Boss#2}} | {{guide:spoils.pay.thulium@Pirate Boss#3}} |
| Erfarenhet (XP) | {{guide:spoils.pay.experience@Pirate Boss#1}} | {{guide:spoils.pay.experience@Pirate Boss#2}} | {{guide:spoils.pay.experience@Pirate Boss#3}} |
| Heder | {{guide:spoils.pay.honor@Pirate Boss#1}} | {{guide:spoils.pay.honor@Pirate Boss#2}} | {{guide:spoils.pay.honor@Pirate Boss#3}} |
| PvE-poäng per nedskjutning | 15 | 15 | 15 |

**Byte**: en låda, för piloten som gjorde mest skada.

| Föremål |
| :--- |
| {{guide:spoils.box@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} |

### Pirate Scout

Bygger på Kitefin med 50 % av skrovet och 113 % av laserskadan; hastighet och räckvidd är förlagans.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | {{guide:vitals.hull@Pirate Scout#1}} | {{guide:vitals.hull@Pirate Scout#2}} | {{guide:vitals.hull@Pirate Scout#3}} |
| Sköld | {{guide:vitals.shield@Pirate Scout#1}} | {{guide:vitals.shield@Pirate Scout#2}} | {{guide:vitals.shield@Pirate Scout#3}} |
| Laserskada (en salva per sekund) | {{guide:vitals.dps@Pirate Scout#1}} | {{guide:vitals.dps@Pirate Scout#2}} | {{guide:vitals.dps@Pirate Scout#3}} |
| Hastighet | {{guide:vitals.speed@Pirate Scout#1}} | {{guide:vitals.speed@Pirate Scout#2}} | {{guide:vitals.speed@Pirate Scout#3}} |
| Laserräckvidd | 700 | 700 | 700 |
| Aggroradie | {{guide:vitals.aggro@Pirate Scout#1}} | {{guide:vitals.aggro@Pirate Scout#2}} | {{guide:vitals.aggro@Pirate Scout#3}} |
| Läker ledaren, var och en, per sekund (bara skrovet) | 40 | 60 | 80 |
| Krediter | {{guide:spoils.pay.credits@Pirate Scout#1}} | {{guide:spoils.pay.credits@Pirate Scout#2}} | {{guide:spoils.pay.credits@Pirate Scout#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Scout#1}} | {{guide:spoils.pay.thulium@Pirate Scout#2}} | {{guide:spoils.pay.thulium@Pirate Scout#3}} |
| Erfarenhet (XP) | {{guide:spoils.pay.experience@Pirate Scout#1}} | {{guide:spoils.pay.experience@Pirate Scout#2}} | {{guide:spoils.pay.experience@Pirate Scout#3}} |
| Heder | {{guide:spoils.pay.honor@Pirate Scout#1}} | {{guide:spoils.pay.honor@Pirate Scout#2}} | {{guide:spoils.pay.honor@Pirate Scout#3}} |
| PvE-poäng per nedskjutning | 4 | 4 | 4 |

**Byte**: inget. Nedskjutningen betalar bara sina krediter, sitt Thulium, sin XP och sin heder.

<!-- pirate-members:end -->
