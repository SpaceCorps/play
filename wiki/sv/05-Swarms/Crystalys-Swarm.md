<!-- wiki-i18n source: 2b3edf7bcb1d9673 -->
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
- **Kommer tillbaka**: {{guide:vitals.respawn@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} efter att ledaren förstörts, i samma sektor
- **Meddelanden**: Piloterna i sektorn får veta när ledaren dyker upp och när den förstörs. Det är systemrader: de syns på chattens flik **System**, med en räknare för olästa rader, och inte i **Global** eller **Lokal**. Dödsloggen nämner piloten som nedskjutningen tillskrivs.

<!-- crystalys-glance:end -->

## Medlemmarna {#the-members}

- **Boss Crystalys**: en större Crystalys, i svärmens nyans och med sitt namn ovanför, med eget skrov, egen sköld och egen lasersalva (värdena står nedan). Den är passiv: den drar omkring tills en pilot träffar den, går sedan efter den piloten och skjuter, och svärmens skepp i närheten ansluter sig till striden. Vapnets räckvidd och hastigheten är desamma som hos en Crystalys, och den reparerar aldrig sitt skrov själv. Dess [tre steg](#the-leaders-three-steps) och en [specialförmåga](/wiki/03-Mechanics/Special-Abilities.md) kan ändra på det.
- **Crystalys Guard**: en mindre Crystalys i svärmens nyans. Guards håller sig nära bossen, ansluter sig till striden när ett svärmskepp i närheten träffas, och var och en som är nära bossen läker dess skrov. En Guard reparerar sitt eget skrov efter en vila, som en Crystalys gör.

## Hur striden går till {#how-the-fight-goes}

- **Ta med en stor grupp.** I Alpha räcker sex piloter på nivå 8 i Paragons med ammunition x2 om dess eld fördelas på dem, nio om den går på en enda pilot; med ammunition x4 är det fem och sex. Fler piloter avslutar striden snabbare och förlorar färre skepp, och en ensam pilot förstörs.
- **Skjut på bossen, inte på Guards.** En Guard faller på sekunder, men en ny kommer lika ofta som listan *I korthet* säger, och det Guards läker är en liten del av vad en grupp gör: att låta dem vara kostar lite tid, att jaga dem kostar mer.
- **Beta och Gamma är hårdare.** Svärmarna i de världarna är starkare ([Världar](/wiki/05-Swarms/Swarms.md#the-worlds)), så de kräver fler piloter eller bättre ammunition.
- **Farosektorerna är PvP.** En rival kan attackera gruppen mitt i striden och vänta på lådan: den tillhör piloten som gjorde mest skada (och dennes klan) i 30 sekunder, och sedan vem som helst ([Last](/wiki/03-Mechanics/Cargo.md)). Kom inte ensam.
- **Bossen kommer tillbaka** efter tiden i listan *I korthet*, vid full styrka, i samma sektor, och dess Guards kommer en efter en.

## Ledarens tre steg {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Striden har tre steg ([hur de fungerar](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); vart och ett sker en gång.

- **I början**: Tar 50 % av varje träff i 8 s.
- **Under två tredjedelar**: En ring på 700 enheter träffar varje skepp inuti med 4 av dess salvor, och den avfyrar 4 raketer.
- **Under en tredjedel**: Läker 20 % av skrovet och skölden (en skadestöt bryter det), och 3 fler Crystalys Guards kommer, högst 6 levande.

<!-- mob-ladder:end -->

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
| Skrov | {{guide:vitals.hull@Boss Crystalys#1}} | {{guide:vitals.hull@Boss Crystalys#2}} | {{guide:vitals.hull@Boss Crystalys#3}} |
| Sköld | {{guide:vitals.shield@Boss Crystalys#1}} | {{guide:vitals.shield@Boss Crystalys#2}} | {{guide:vitals.shield@Boss Crystalys#3}} |
| Laserskada (en salva per sekund) | {{guide:vitals.dps@Boss Crystalys#1}} | {{guide:vitals.dps@Boss Crystalys#2}} | {{guide:vitals.dps@Boss Crystalys#3}} |
| Hastighet | {{guide:vitals.speed@Boss Crystalys#1}} | {{guide:vitals.speed@Boss Crystalys#2}} | {{guide:vitals.speed@Boss Crystalys#3}} |
| Laserräckvidd | 900 | 900 | 900 |
| Aggroradie | bara när den attackeras | bara när den attackeras | bara när den attackeras |
| Krediter | {{guide:spoils.pay.credits@Boss Crystalys#1}} | {{guide:spoils.pay.credits@Boss Crystalys#2}} | {{guide:spoils.pay.credits@Boss Crystalys#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Crystalys#1}} | {{guide:spoils.pay.thulium@Boss Crystalys#2}} | {{guide:spoils.pay.thulium@Boss Crystalys#3}} |
| Erfarenhet (XP) | {{guide:spoils.pay.experience@Boss Crystalys#1}} | {{guide:spoils.pay.experience@Boss Crystalys#2}} | {{guide:spoils.pay.experience@Boss Crystalys#3}} |
| Heder | {{guide:spoils.pay.honor@Boss Crystalys#1}} | {{guide:spoils.pay.honor@Boss Crystalys#2}} | {{guide:spoils.pay.honor@Boss Crystalys#3}} |
| PvE-poäng per nedskjutning | 30 | 30 | 30 |

**Byte**: en låda, för piloten som gjorde mest skada.

| Föremål |
| :--- |
| {{guide:spoils.box@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} |

### Crystalys Guard

Bygger på Crystalys med 15 % av skrov, sköld och skada; hastighet och räckvidd är förlagans.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | {{guide:vitals.hull@Crystalys Guard#1}} | {{guide:vitals.hull@Crystalys Guard#2}} | {{guide:vitals.hull@Crystalys Guard#3}} |
| Sköld | {{guide:vitals.shield@Crystalys Guard#1}} | {{guide:vitals.shield@Crystalys Guard#2}} | {{guide:vitals.shield@Crystalys Guard#3}} |
| Laserskada (en salva per sekund) | {{guide:vitals.dps@Crystalys Guard#1}} | {{guide:vitals.dps@Crystalys Guard#2}} | {{guide:vitals.dps@Crystalys Guard#3}} |
| Hastighet | {{guide:vitals.speed@Crystalys Guard#1}} | {{guide:vitals.speed@Crystalys Guard#2}} | {{guide:vitals.speed@Crystalys Guard#3}} |
| Laserräckvidd | 900 | 900 | 900 |
| Aggroradie | bara när den attackeras | bara när den attackeras | bara när den attackeras |
| Läker ledaren, var och en, per sekund (bara skrovet) | 250 | 375 | 500 |
| Krediter | {{guide:spoils.pay.credits@Crystalys Guard#1}} | {{guide:spoils.pay.credits@Crystalys Guard#2}} | {{guide:spoils.pay.credits@Crystalys Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Crystalys Guard#1}} | {{guide:spoils.pay.thulium@Crystalys Guard#2}} | {{guide:spoils.pay.thulium@Crystalys Guard#3}} |
| Erfarenhet (XP) | {{guide:spoils.pay.experience@Crystalys Guard#1}} | {{guide:spoils.pay.experience@Crystalys Guard#2}} | {{guide:spoils.pay.experience@Crystalys Guard#3}} |
| Heder | {{guide:spoils.pay.honor@Crystalys Guard#1}} | {{guide:spoils.pay.honor@Crystalys Guard#2}} | {{guide:spoils.pay.honor@Crystalys Guard#3}} |
| PvE-poäng per nedskjutning | 6 | 6 | 6 |

**Byte**: inget. Nedskjutningen betalar bara sina krediter, sitt Thulium, sin XP och sin heder.

<!-- crystalys-members:end -->
