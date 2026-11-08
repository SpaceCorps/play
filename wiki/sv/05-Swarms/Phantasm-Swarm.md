<!-- wiki-i18n source: abb582fd63389ab9 -->
<!-- wiki-i18n title: Phantasm-svärm -->
# Phantasm-svärm {#phantasm-swarm}

Phantasm-svärmen är en **Boss Phantasm** med sina **Phantasm Guards**: en enorm [Phantasm](/wiki/04-Aliens/Phantasm.md) som aldrig börjar en strid, och mindre som håller sig nära den och läker den. Den håller till i koncernernas yttre sektorer, `x-3` och `x-4`, och är en strid för en grupp piloter på mellannivå.

## I korthet {#at-a-glance}

<!-- phantasm-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Var**: Sektorerna `x-3` och `x-4` i varje koncern
- **Hur många**: En i var och en av de sektorerna, 6 i varje värld
- **Dyker upp**: Från säsongsdag 4 till wipen (Beta och Gamma: från säsongsdag 1)
- **Ledare**: Boss Phantasm
- **Följeslagare**: Upp till 4 × Phantasm Guard, en ny var 10 s
- **Följeslagarna håller sig inom**: högst 500 enheter från ledaren
- **Läkning**: Varje Phantasm Guard inom 600 enheter från ledaren läker dess skrov, 30 HP per sekund i Alpha
- **När ledaren förstörs**: Följeslagarna försvinner 30 s efter att ledaren förstörts, om de inte just attackerar
- **Kommer tillbaka**: 2 min efter att ledaren förstörts, i samma sektor
- **Meddelanden**: Piloterna i sektorn får veta när ledaren dyker upp och när den förstörs. Det är systemrader: de syns på chattens flik **System**, med en räknare för olästa rader, och inte i **Global** eller **Lokal**. Dödsloggen nämner piloten som nedskjutningen tillskrivs.

<!-- phantasm-glance:end -->

## Medlemmarna {#the-members}

- **Boss Phantasm**: en större Phantasm, i svärmens nyans och med sitt namn ovanför, med eget skrov, egen sköld och egen lasersalva (värdena står nedan). Den är passiv: den drar omkring tills en pilot träffar den, går sedan efter den piloten och skjuter, och svärmens skepp i närheten ansluter sig till striden. Vapnets räckvidd och hastigheten är desamma som hos en Phantasm, och den reparerar aldrig sitt skrov själv.
- **Phantasm Guard**: en mindre Phantasm i svärmens nyans. Guards håller sig nära bossen, ansluter sig till striden när ett svärmskepp i närheten träffas, och var och en som är nära bossen läker dess skrov. En Guard reparerar sitt eget skrov efter en vila, som en Phantasm gör.

## Hur striden går till {#how-the-fight-goes}

- **Ta med en grupp.** Tre piloter på nivå 4–5 med ammunition x2 förstör den på ungefär en och en halv minut i Alpha och förlorar högst ett skepp; en ensam pilot på den nivån förstörs, och två vinner med knapp nöd, och bara medan träffarna fördelas. Bättre skepp och ammunition x4 gör det mycket snabbare.
- **Skjut på bossen, inte på Guards.** En Guard faller på sekunder, men en ny kommer lika ofta som listan *I korthet* säger, och det Guards läker är en liten del av vad en grupp gör: att låta dem vara kostar lite tid, att jaga dem kostar mer.
- **Beta och Gamma är hårdare.** Svärmarna i de världarna är starkare ([Världar](/wiki/05-Swarms/Swarms.md#the-worlds)), så de kräver fler piloter eller bättre ammunition.
- **Håll koll på sektorn.** `x-4` är en PvP-sektor i Alpha, och `x-3` och `x-4` är det i Beta och Gamma ([Världar](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): en rival kan ansluta sig till striden eller vänta på lådan. Låt ett skepp i gruppen hålla utkik.
- **Bossen kommer tillbaka** efter tiden i listan *I korthet*, vid full styrka, i samma sektor, och dess Guards kommer en efter en.

## Belöningar och byte {#rewards-and-drops}

Boss Phantasm betalar för den strid den är: en minuts strid mot den betalar mer än en minuts strid mot en Goombah, de här sektorernas bäst betalda utomjording. Betalningen delas efter skada mellan piloterna som stred mot den ([hur nedskjutningen av en boss betalar](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Dess låda går till piloten som gjorde mest skada och innehåller en Phantasms eget byte många gånger om (Ship Fragments, Daraxium och Nyxite), med ammunition och raketer. Guards betalar lite och tappar ingenting; att skjuta ner dem är ingen farmning, eftersom de kommer tillbaka med bossen.

## Värdena {#the-numbers}

Värdena för svärmens skepp i de tre världarna ([Världar](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- phantasm-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Phantasm

Bygger på Phantasm med 2 000 % av skrovet och 300 % av laserskadan; hastighet och räckvidd är förlagans.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | 40 000 | 60 000 | 80 000 |
| Sköld | 64 000 | 96 000 | 128 000 |
| Laserskada (en salva per sekund) | 1 050 | 1 575 | 2 100 |
| Hastighet | 160 | 160 | 160 |
| Laserräckvidd | 700 | 700 | 700 |
| Aggroradie | bara när den attackeras | bara när den attackeras | bara när den attackeras |
| Krediter | 39 000 | 78 000 | 117 000 |
| Thulium | 195 | 390 | 585 |
| Erfarenhet (XP) | 7 800 | 15 600 | 23 400 |
| Heder | 62 | 124 | 186 |
| PvE-poäng per nedskjutning | 8 | 8 | 8 |

**Byte**: en låda, för piloten som gjorde mest skada.

| Föremål | Chans | Mängd |
| :--- | ---: | ---: |
| Ship Fragment | 100 % på vart och ett av 13 slag | 1 |
| Daraxium | 60 % på vart och ett av 13 slag | 1–2 |
| Nyxite | 60 % på vart och ett av 13 slag | 1–2 |
| Standard Battery | 100 % | 600–1 200 |
| Advanced Plasma | 100 % | 60–100 |
| Ultra Core | 100 % | 10–20 |
| En av de 8 [raketer](/wiki/06-Items/Rockets.md) som köps med krediter, slumpmässigt vald | 100 % | 4–6 |

### Phantasm Guard

Bygger på Phantasm med 50 % av skrov, sköld och skada; hastighet och räckvidd är förlagans.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | 1 000 | 1 500 | 2 000 |
| Sköld | 1 600 | 2 400 | 3 200 |
| Laserskada (en salva per sekund) | 175 | 263 | 350 |
| Hastighet | 160 | 160 | 160 |
| Laserräckvidd | 700 | 700 | 700 |
| Aggroradie | bara när den attackeras | bara när den attackeras | bara när den attackeras |
| Läker ledaren, var och en, per sekund (bara skrovet) | 30 | 45 | 60 |
| Krediter | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Erfarenhet (XP) | 12 | 24 | 36 |
| Heder | 1 | 2 | 3 |
| PvE-poäng per nedskjutning | 1 | 1 | 1 |

**Byte**: inget. Nedskjutningen betalar bara sina krediter, sitt Thulium, sin XP och sin heder.

<!-- phantasm-members:end -->
