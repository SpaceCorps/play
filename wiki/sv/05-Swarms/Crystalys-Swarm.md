<!-- wiki-i18n source: 5f873edc2b653495 -->
<!-- wiki-i18n title: Crystalys-svärm -->
# Crystalys-svärm {#crystalys-swarm}

Crystalys-svärmen är en **Boss Crystalys** med sina **Crystalys Guards**: den segaste av utomjordingarna, [Crystalys](/wiki/04-Aliens/Crystalys.md), men större, med vakter som håller sig nära den och läker den. Den håller till i [farosektorerna](/wiki/01-General/Danger-Sectors.md) `DS-1`, `DS-2` och `DS-3`, en i varje, och lämnar aldrig sin sektor. Farosektorerna är PvP-sektorer, så striden är för en stor grupp av de starkaste piloterna, och bossen är inte den enda faran där.

## I korthet {#at-a-glance}

<!-- crystalys-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Var**: Farosektorerna `DS-1`, `DS-2`, `DS-3`
- **Hur många**: En i var och en av de sektorerna, 3 i varje värld
- **Dyker upp**: Från säsongsdag 4 till wipen (Beta och Gamma: från säsongsdag 1)
- **Ledare**: Boss Crystalys
- **Följeslagare**: Upp till 3 × Crystalys Guard, en ny var 10 s
- **Följeslagarna håller sig inom**: högst 500 enheter från ledaren
- **Läkning**: Varje Crystalys Guard inom 600 enheter från ledaren läker dess skrov, 250 HP per sekund i Alpha
- **När ledaren förstörs**: Följeslagarna försvinner 30 s efter att ledaren förstörts, om de inte just attackerar
- **Kommer tillbaka**: 30 min efter att ledaren förstörts, i samma sektor
- **Meddelanden**: Piloterna i sektorn får veta när ledaren dyker upp och när den förstörs. Det är systemrader: de syns på chattens flik **System**, med en räknare för olästa rader, och inte i **Global** eller **Lokal**. Dödsloggen nämner piloten som nedskjutningen tillskrivs.

<!-- crystalys-glance:end -->

## Medlemmarna {#the-members}

- **Boss Crystalys**: en större Crystalys, i svärmens nyans och med sitt namn ovanför, med eget skrov, egen sköld och egen lasersalva (värdena står nedan). Den är passiv: den drar omkring tills en pilot träffar den, går sedan efter den piloten och skjuter, och svärmens skepp i närheten ansluter sig till striden. Vapnets räckvidd och hastigheten är desamma som hos en Crystalys, och den reparerar aldrig sitt skrov själv.
- **Crystalys Guard**: en mindre Crystalys i svärmens nyans. Guards håller sig nära bossen, ansluter sig till striden när ett svärmskepp i närheten träffas, och var och en som är nära bossen läker dess skrov. En Guard reparerar sitt eget skrov efter en vila, som en Crystalys gör.

## Hur striden går till {#how-the-fight-goes}

- **Ta med en stor grupp.** I Alpha räcker sex piloter på nivå 8 i Paragons med ammunition x2 om dess eld fördelas på dem, nio om den går på en enda pilot; med ammunition x4 är det fem och sex. Fler piloter avslutar striden snabbare och förlorar färre skepp, och en ensam pilot förstörs.
- **Skjut på bossen, inte på Guards.** En Guard faller på sekunder, men en ny kommer lika ofta som listan *I korthet* säger, och det Guards läker är en liten del av vad en grupp gör: att låta dem vara kostar lite tid, att jaga dem kostar mer.
- **Beta och Gamma är hårdare.** Svärmarna i de världarna är starkare ([Världar](/wiki/05-Swarms/Swarms.md#the-worlds)), så de kräver fler piloter eller bättre ammunition.
- **Farosektorerna är PvP.** En rival kan attackera gruppen mitt i striden och vänta på lådan: den tillhör piloten som gjorde mest skada (och dennes klan) i 30 sekunder, och sedan vem som helst ([Last](/wiki/03-Mechanics/Cargo.md)). Kom inte ensam.
- **Bossen kommer tillbaka** efter tiden i listan *I korthet*, vid full styrka, i samma sektor, och dess Guards kommer en efter en.

## Belöningar och byte {#rewards-and-drops}

Boss Crystalys betalar för den strid den är: en minuts strid mot den betalar mer än en minuts strid mot en Crystalys, den bäst betalda utomjordingen. Betalningen delas efter skada mellan piloterna som stred mot den ([hur nedskjutningen av en boss betalar](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Dess låda går till piloten som gjorde mest skada och innehåller Cataclysite och Quorvium, då och då en Power Core, en Ancient Control Unit eller Dark Matter, ammunition x3 och x4 samt episka raketer. Guards betalar lite och tappar ingenting; att skjuta ner dem är ingen farmning, eftersom de kommer tillbaka med bossen.

## Värdena {#the-numbers}

Värdena för svärmens skepp i de tre världarna ([Världar](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- crystalys-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Crystalys

Bygger på Crystalys med 350 % av skrovet och 100 % av laserskadan; hastighet och räckvidd är förlagans.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | 896 000 | 1 344 000 | 1 792 000 |
| Sköld | 560 000 | 840 000 | 1 120 000 |
| Laserskada (en salva per sekund) | 10 000 | 15 000 | 20 000 |
| Hastighet | 230 | 230 | 230 |
| Laserräckvidd | 900 | 900 | 900 |
| Aggroradie | bara när den attackeras | bara när den attackeras | bara när den attackeras |
| Krediter | 393 750 | 787 500 | 1 181 250 |
| Thulium | 1 050 | 2 100 | 3 150 |
| Erfarenhet (XP) | 63 000 | 126 000 | 189 000 |
| Heder | 273 | 546 | 819 |
| PvE-poäng per nedskjutning | 30 | 30 | 30 |

**Byte**: en låda, för piloten som gjorde mest skada.

| Föremål | Chans | Mängd |
| :--- | ---: | ---: |
| Cataclysite | 100 % på vart och ett av 2 slag | 8 |
| Quorvium | 100 % på vart och ett av 2 slag | 6–10 |
| Power Core | 30 % | 1 |
| Ancient Control Unit | 15 % | 1 |
| Dark Matter | 4 % | 1 |
| Ultra Core och Experimental Fusion Core, delat lika | 100 % | 600–1 000 totalt |
| En av de 4 Episka [raketerna](/wiki/06-Items/Rockets.md), slumpmässigt vald | 100 % | 8–15 |

### Crystalys Guard

Bygger på Crystalys med 15 % av skrov, sköld och skada; hastighet och räckvidd är förlagans.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | 38 400 | 57 600 | 76 800 |
| Sköld | 24 000 | 36 000 | 48 000 |
| Laserskada (en salva per sekund) | 1 500 | 2 250 | 3 000 |
| Hastighet | 230 | 230 | 230 |
| Laserräckvidd | 900 | 900 | 900 |
| Aggroradie | bara när den attackeras | bara när den attackeras | bara när den attackeras |
| Läker ledaren, var och en, per sekund (bara skrovet) | 250 | 375 | 500 |
| Krediter | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Erfarenhet (XP) | 12 | 24 | 36 |
| Heder | 1 | 2 | 3 |
| PvE-poäng per nedskjutning | 6 | 6 | 6 |

**Byte**: inget. Nedskjutningen betalar bara sina krediter, sitt Thulium, sin XP och sin heder.

<!-- crystalys-members:end -->
