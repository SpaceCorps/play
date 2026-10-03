<!-- wiki-i18n source: f06b4c7b561b1789 -->
<!-- wiki-i18n title: Pirate-svärm -->
# Pirate-svärm {#pirate-swarm}

Pirate-svärmen är en **Pirate Boss** med sina **Pirate Scouts**: ett stort, långsamt skepp som inte angriper någon och svarar med raketer, och en flock snabbare skepp som vaktar och läker det. Den håller till i sektorerna mellan en koncerns bas och dess gräns, där spelets mellannivåer spelas, och är en lång strid för en grupp piloter, inte en snabb nedskjutning.

## I korthet {#at-a-glance}

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Var**: Sektorerna `x-2` och `x-3` i varje koncern
- **Hur många**: En i var och en av de sektorerna, 6 i varje värld
- **Dyker upp**: Från säsongsdag 4 till wipen
- **Ledare**: Pirate Boss
- **Följeslagare**: Upp till 5 × Pirate Scout, en ny var 10 s
- **Följeslagarna håller sig inom**: högst 900 enheter från ledaren
- **Läkning**: Varje Pirate Scout inom 600 enheter från ledaren läker dess skrov, 40 HP per sekund i Alpha
- **När ledaren förstörs**: Följeslagarna försvinner 1 min efter att ledaren förstörts, om de inte just attackerar
- **Kommer tillbaka**: 2 min efter att ledaren förstörts, i samma sektor
- **Meddelanden**: Sektorns chatt meddelar när ledaren dyker upp och när den förstörs. Dödsloggen nämner piloten som nedskjutningen tillskrivs.

<!-- pirate-glance:end -->

## Medlemmarna {#the-members}

- **Pirate Boss**: ett skepp som bygger på Ironclad, med en del av dess styrka (värdena står nedan). Den är passiv och skjuter **inga lasrar**: dess enda vapen är en **rak raket** ([Raketer](/wiki/06-Items/Rockets.md); vilken beror på sektorn, se tabellen) mot piloten som attackerade den, och den drar vidare medan den skjuter. Den reparerar aldrig sitt skrov själv.
- **Pirate Scout**: ett skepp som bygger på Kitefin, med en del av dess styrka. Scouts attackerar varje pilot som kommer nära, håller sig nära bossen, och var och en som är nära bossen läker dess skrov.

## Hur striden går till {#how-the-fight-goes}

- **Skjut på bossen, inte på Scouts.** Scouts läker bossen, men läkningen är liten jämfört med dess skrov, och en ny Scout kommer så ofta som listan *I korthet* säger: en grupp som skjuter Scouts först kommer aldrig före dem, och bara en mycket stor grupp kan röja dem och behöver ändå längre tid på bossen än en grupp som lät dem vara. Scouts kostar dig tid, de avgör inte striden.
- **Led bort Scouts.** En Scout läker bara så länge den är inom bossens räckhåll, så en Scout som följer dig utanför det läker ingenting, och en Ostirion är snabbare än en Scout.
- **Fortsätt röra dig.** Bossens raket är rak och ostyrd: ett skepp som håller sig i rörelse undviker den, ett som står still blir träffat.
- **Ta med en grupp.** Tre piloter i Ostirion med ammunition x2 kan fälla den på ungefär fem minuter i Alpha; en Ostirion ensam klarar det inte, en Paragon ensam gör det. Bossen går mot den första piloten som träffade den, så låt det tåligaste skeppet börja, och använd dina förmågor (Emergency Repair, Shield Surge: [Förmågor](/wiki/03-Mechanics/Abilities.md)) i en så lång strid. Piloter som fortfarande är nivå 2 eller 3 är för svaga för den, även där de flyger: håll dig borta tills du är starkare.
- **Bossen kommer tillbaka** efter tiden i listan *I korthet*, i samma sektor.

## Belöningar och byte {#rewards-and-drops}

Pirate Boss betalar efter den strid den är: en minuts strid mot den betalar mer än en minuts strid mot en Goombah. Betalningen delas efter skada mellan piloterna som stred mot den ([hur nedskjutningen av en boss betalar](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Dess låda är för piloten som gjorde mest skada och kan innehålla en **Reinforced Hull Plate**, raketer och ammunition. Scouts betalar lite och tappar ingenting.

## Värdena {#the-numbers}

Värdena för svärmens skepp i de tre världarna ([Världar](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss {#pirate-boss}

Bygger på Ironclad med 50 % av skrov, sköld och skada; hastighet och räckvidd är förlagans. Skjuter en rak raket var 5 s: [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) i `x-2`, [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) i `x-3`.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | 300 000 | 450 000 | 600 000 |
| Sköld | 50 100 | 75 150 | 100 200 |
| Laserskada (en salva per sekund) | ingen | ingen | ingen |
| Hastighet | 92 | 92 | 92 |
| Laserräckvidd | – | – | – |
| Aggroradie | bara när den attackeras | bara när den attackeras | bara när den attackeras |
| Raketskada, högst | 2 500 (Rivet I) / 5 000 (Rivet II) | 3 750 (Rivet I) / 7 500 (Rivet II) | 5 000 (Rivet I) / 10 000 (Rivet II) |
| Krediter | 116 000 | 232 000 | 348 000 |
| Thulium | 725 | 1 450 | 2 175 |
| Erfarenhet (XP) | 29 000 | 58 000 | 87 000 |
| Heder | 232 | 464 | 696 |
| PvE-poäng per nedskjutning | 10 | 10 | 10 |

**Byte**: en låda, för piloten som gjorde mest skada.

| Föremål | Chans | Mängd |
| :--- | ---: | ---: |
| Reinforced Hull Plate | 50 % | 1 |
| En av de 8 [raketer](/wiki/06-Items/Rockets.md) som köps med krediter, slumpmässigt vald | 100 % | 5–10 |
| En av Advanced Plasma och Siphon Battery, slumpmässigt vald | 100 % | 500–1 000 |

### Pirate Scout {#pirate-scout}

Bygger på Kitefin med 50 % av skrov, sköld och skada; hastighet och räckvidd är förlagans.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | 12 000 | 18 000 | 24 000 |
| Sköld | 9 818 | 14 727 | 19 636 |
| Laserskada (en salva per sekund) | 98 | 147 | 196 |
| Hastighet | 175 | 175 | 175 |
| Laserräckvidd | 700 | 700 | 700 |
| Aggroradie | 700 | 700 | 700 |
| Läker ledaren, var och en, per sekund (bara skrovet) | 40 | 60 | 80 |
| Krediter | 800 | 1 600 | 2 400 |
| Thulium | 4 | 8 | 12 |
| Erfarenhet (XP) | 100 | 200 | 300 |
| Heder | 2 | 4 | 6 |
| PvE-poäng per nedskjutning | 1 | 1 | 1 |

**Byte**: inget. Nedskjutningen betalar bara sina krediter, sitt Thulium, sin XP och sin heder.

<!-- pirate-members:end -->
