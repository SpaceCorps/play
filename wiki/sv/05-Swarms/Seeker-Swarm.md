<!-- wiki-i18n source: babc7a19c6dcab42 -->
<!-- wiki-i18n title: Seeker-svärm -->
# Seeker-svärm {#seeker-swarm}

Seeker-svärmen är den minsta av [svärmarna](/wiki/05-Swarms/Swarms.md): en **Boss Seeker** och de **Seeker Slaves** som vaktar och läker den. Den håller till i sektorerna där nya piloter börjar flyga, så den är den första svärmen de flesta möter. Boss Seeker börjar aldrig en strid, men så snart du skjuter på den är den mycket farligare än den [Seeker](/wiki/04-Aliens/Seeker.md) den bygger på.

## I korthet {#at-a-glance}

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Var**: Sektorerna `x-1` och `x-2` i varje koncern
- **Hur många**: En i var och en av de sektorerna, 6 i varje värld
- **Dyker upp**: Från säsongsdag 4 till wipen
- **Ledare**: Boss Seeker
- **Följeslagare**: Upp till 4 × Seeker Slave, en ny var 10 s
- **Följeslagarna håller sig inom**: högst 500 enheter från ledaren
- **Läkning**: Varje Seeker Slave inom 600 enheter från ledaren läker dess skrov, 50 HP per sekund i Alpha
- **När ledaren förstörs**: Följeslagarna försvinner 30 s efter att ledaren förstörts, om de inte just attackerar
- **Kommer tillbaka**: 2 min efter att ledaren förstörts, i samma sektor
- **Meddelanden**: Piloterna i sektorn får veta när ledaren dyker upp och när den förstörs. Det är systemrader: de syns på chattens flik **System**, med en räknare för olästa rader, och inte i **Global** eller **Lokal**. Dödsloggen nämner piloten som nedskjutningen tillskrivs.

<!-- seeker-glance:end -->

## Medlemmarna {#the-members}

- **Boss Seeker**: en mycket större Seeker, i svärmens nyans och med sitt namn ovanför, med många gånger en Seekers skrov, sköld och skada (värdena står nedan). Den är passiv: den drar omkring tills en pilot träffar den, stannar sedan där den är och skjuter på piloten, och svärmens skepp i närheten ansluter sig till striden. Vapnets räckvidd och hastigheten är en Seekers, och den reparerar aldrig sitt skrov själv.
- **Seeker Slave**: en vanlig Seeker i svärmens nyans. Slaves håller sig nära bossen, ansluter sig till striden när ett svärmskepp i närheten träffas, och var och en som är nära bossen läker dess skrov. En Slave reparerar sitt eget skrov efter en vila, som en Seeker gör.

## Hur striden går till {#how-the-fight-goes}

- **Låt den vara tills ditt skepp klarar den.** En Boss Seeker slår hårdare än en pilots första skepp tål: en ny pilots Protos, ännu utan sköld, förstörs på sekunder så snart bossen och dess Slaves är över den.
- **Håll dig utom räckhåll.** Bossen och dess Slaves är långsammare än en Protos, och deras vapen når kortare än en Quantum Laser 2 (se [Lasrar och ammunition](/wiki/06-Items/Lasers.md)): en pilot som har sådana lasrar och håller sig bortom deras räckvidd tar ingen skada medan de skjuter. En pilot med Quantum Laser 1 kan inte hålla sig utom räckhåll.
- **Slaves läker snabbare än en ensam ny pilot träffar.** Tillsammans läker de mer än en pilots lasrar gör med ammunition x1, så ta med en kamrat och ammunition x2. Två piloter med Quantum Laser 2 som håller avstånd fäller bossen på ungefär en minut i Alpha, och mycket snabbare med ammunition x2.
- **Bossen kommer tillbaka** efter tiden i listan *I korthet*, vid full styrka, i samma sektor, och dess Slaves kommer en efter en.

## Belöningar och byte {#rewards-and-drops}

Boss Seeker betalar **exakt tio Seekers**: tio gånger en Seekers krediter, Thulium, XP och heder, delat efter skada mellan piloterna som stred mot den ([hur nedskjutningen av en boss betalar](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Dess låda innehåller tio Seekers byte och därtill ammunition och raketer under Episk, för piloten som gjorde mest skada. Slaves betalar lite och tappar ingenting; att skjuta ner dem är ingen farmning, eftersom de kommer tillbaka med bossen.

## Värdena {#the-numbers}

Värdena för svärmens skepp i de tre världarna ([Världar](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker {#boss-seeker}

Bygger på Seeker med 400 % av skrov, sköld och skada; hastighet och räckvidd är förlagans.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | 3 200 | 4 800 | 6 400 |
| Sköld | 3 200 | 4 800 | 6 400 |
| Laserskada (en salva per sekund) | 720 | 1 080 | 1 440 |
| Hastighet | 120 | 120 | 120 |
| Laserräckvidd | 600 | 600 | 600 |
| Aggroradie | bara när den attackeras | bara när den attackeras | bara när den attackeras |
| Krediter | 10 000 | 20 000 | 30 000 |
| Thulium | 40 | 80 | 120 |
| Erfarenhet (XP) | 1 000 | 2 000 | 3 000 |
| Heder | 20 | 40 | 60 |
| PvE-poäng per nedskjutning | 5 | 5 | 5 |

**Byte**: en låda, för piloten som gjorde mest skada.

| Föremål | Chans | Mängd |
| :--- | ---: | ---: |
| Ship Fragment | 20 % på vart och ett av 10 slag | 1 |
| Daraxium | 50 % på vart och ett av 10 slag | 1–2 |
| Standard Battery | 100 % | 200–400 |
| Advanced Plasma | 100 % | 10–20 |
| Ultra Core | 100 % | 2–4 |
| En av de 8 [raketer](/wiki/06-Items/Rockets.md) som köps med krediter, slumpmässigt vald | 100 % | 2–3 |

### Seeker Slave {#seeker-slave}

Bygger på Seeker med 100 % av skrov, sköld och skada; hastighet och räckvidd är förlagans.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | 800 | 1 200 | 1 600 |
| Sköld | 800 | 1 200 | 1 600 |
| Laserskada (en salva per sekund) | 180 | 270 | 360 |
| Hastighet | 120 | 120 | 120 |
| Laserräckvidd | 600 | 600 | 600 |
| Aggroradie | bara när den attackeras | bara när den attackeras | bara när den attackeras |
| Läker ledaren, var och en, per sekund (bara skrovet) | 50 | 75 | 100 |
| Krediter | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Erfarenhet (XP) | 12 | 24 | 36 |
| Heder | 1 | 2 | 3 |
| PvE-poäng per nedskjutning | 1 | 1 | 1 |

**Byte**: inget. Nedskjutningen betalar bara sina krediter, sitt Thulium, sin XP och sin heder.

<!-- seeker-members:end -->
