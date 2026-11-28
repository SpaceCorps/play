<!-- wiki-i18n source: 38ffa8ba7cbf5000 -->
<!-- wiki-i18n title: Goombah-svärm -->
# Goombah-svärm {#goombah-swarm}

Goombah-svärmen är en **Boss Goombah** med sina **Goombah Guards**: en jättelik [Goombah](/wiki/04-Aliens/Goombah.md) som aldrig börjar en strid, och mindre som håller sig nära den och läker den. Den håller till i samma sektorer som [Phantasm-svärmen](/wiki/05-Swarms/Phantasm-Swarm.md), `x-3` och `x-4`, och är en strid för en grupp av koncernsektorernas starkaste piloter.

## I korthet {#at-a-glance}

<!-- goombah-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Var**: Sektorerna `x-3` och `x-4` i varje koncern
- **Hur många**: En i var och en av de sektorerna, 6 i varje värld
- **Dyker upp**: Från säsongsdag 4 till wipen (Beta och Gamma: från säsongsdag 1)
- **Ledare**: Boss Goombah
- **Följeslagare**: Upp till 4 × Goombah Guard, en ny var 10 s
- **Följeslagarna håller sig inom**: högst 500 enheter från ledaren
- **Läkning**: Varje Goombah Guard inom 600 enheter från ledaren läker dess skrov, 110 HP per sekund i Alpha
- **När ledaren förstörs**: Följeslagarna försvinner 30 s efter att ledaren förstörts, om de inte just attackerar
- **Kommer tillbaka**: {{guide:vitals.respawn@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} efter att ledaren förstörts, i samma sektor
- **Meddelanden**: Piloterna i sektorn får veta när ledaren dyker upp och när den förstörs. Det är systemrader: de syns på chattens flik **System**, med en räknare för olästa rader, och inte i **Global** eller **Lokal**. Dödsloggen nämner piloten som nedskjutningen tillskrivs.

<!-- goombah-glance:end -->

## Medlemmarna {#the-members}

- **Boss Goombah**: en större Goombah, i svärmens nyans och med sitt namn ovanför, med eget skrov, egen sköld och egen lasersalva (värdena står nedan). Den är passiv: den drar omkring tills en pilot träffar den, går sedan efter den piloten och skjuter, och svärmens skepp i närheten ansluter sig till striden. Vapnets räckvidd och hastigheten är desamma som hos en Goombah, och den reparerar aldrig sitt skrov själv. Dess [tre steg](#the-leaders-three-steps) och en [specialförmåga](/wiki/03-Mechanics/Special-Abilities.md) kan ändra på det.
- **Goombah Guard**: en mindre Goombah i svärmens nyans. Guards håller sig nära bossen, ansluter sig till striden när ett svärmskepp i närheten träffas, och var och en som är nära bossen läker dess skrov. En Guard reparerar sitt eget skrov efter en vila, som en Goombah gör.

## Hur striden går till {#how-the-fight-goes}

- **Ta med en grupp av de starkaste skeppen.** Tre piloter på nivå 8 med ammunition x2 förstör den på ungefär 75 sekunder i Alpha och förlorar högst ett skepp; två av dem behöver ammunition x4, och piloter på lägre nivåer gör inte tillräckligt med skada för att vinna.
- **Skjut på bossen, inte på Guards.** En Guard faller på sekunder, men en ny kommer lika ofta som listan *I korthet* säger, och det Guards läker är en liten del av vad en grupp gör: att låta dem vara kostar lite tid, att jaga dem kostar mer.
- **Beta och Gamma är hårdare.** Svärmarna i de världarna är starkare ([Världar](/wiki/05-Swarms/Swarms.md#the-worlds)), så de kräver fler piloter eller bättre ammunition.
- **Håll koll på sektorn.** `x-4` är en PvP-sektor i Alpha, och `x-3` och `x-4` är det i Beta och Gamma ([Världar](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): en rival kan ansluta sig till striden eller vänta på lådan. Låt ett skepp i gruppen hålla utkik.
- **Bossen kommer tillbaka** efter tiden i listan *I korthet*, vid full styrka, i samma sektor, och dess Guards kommer en efter en.

## Ledarens tre steg {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Striden har tre steg ([hur de fungerar](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); vart och ett sker en gång.

- **I början**: Tar 50 % av varje träff i 6 s.
- **Under två tredjedelar**: Dess skada multipliceras med ×1,5 och dess fart med ×1,25 i 10 s.
- **Under en tredjedel**: Läker 25 % av skrovet och skölden (en skadestöt bryter det), och dess Goombah Guards läker den ×2 så fort under tiden.

<!-- mob-ladder:end -->

## Belöningar och byte {#rewards-and-drops}

Boss Goombah betalar för den strid den är: en minuts strid mot den betalar mer än en minuts strid mot en Goombah, de här sektorernas bäst betalda utomjording. Betalningen delas efter skada mellan piloterna som stred mot den ([hur nedskjutningen av en boss betalar](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Dess låda går till piloten som gjorde mest skada och innehåller en Goombahs eget byte flera gånger om (Cataclysite, Quorvium, Power Cores, Reinforced Hull Plates och Ship Fragments), med ammunition och raketer. Guards betalar lite och tappar ingenting; att skjuta ner dem är ingen farmning, eftersom de kommer tillbaka med bossen.

## Värdena {#the-numbers}

Värdena för svärmens skepp i de tre världarna ([Världar](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- goombah-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Goombah

Bygger på Goombah med 400 % av skrovet och 100 % av laserskadan; hastighet och räckvidd är förlagans.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | {{guide:vitals.hull@Boss Goombah#1}} | {{guide:vitals.hull@Boss Goombah#2}} | {{guide:vitals.hull@Boss Goombah#3}} |
| Sköld | {{guide:vitals.shield@Boss Goombah#1}} | {{guide:vitals.shield@Boss Goombah#2}} | {{guide:vitals.shield@Boss Goombah#3}} |
| Laserskada (en salva per sekund) | {{guide:vitals.dps@Boss Goombah#1}} | {{guide:vitals.dps@Boss Goombah#2}} | {{guide:vitals.dps@Boss Goombah#3}} |
| Hastighet | {{guide:vitals.speed@Boss Goombah#1}} | {{guide:vitals.speed@Boss Goombah#2}} | {{guide:vitals.speed@Boss Goombah#3}} |
| Laserräckvidd | 800 | 800 | 800 |
| Aggroradie | bara när den attackeras | bara när den attackeras | bara när den attackeras |
| Krediter | {{guide:spoils.pay.credits@Boss Goombah#1}} | {{guide:spoils.pay.credits@Boss Goombah#2}} | {{guide:spoils.pay.credits@Boss Goombah#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Goombah#1}} | {{guide:spoils.pay.thulium@Boss Goombah#2}} | {{guide:spoils.pay.thulium@Boss Goombah#3}} |
| Erfarenhet (XP) | {{guide:spoils.pay.experience@Boss Goombah#1}} | {{guide:spoils.pay.experience@Boss Goombah#2}} | {{guide:spoils.pay.experience@Boss Goombah#3}} |
| Heder | {{guide:spoils.pay.honor@Boss Goombah#1}} | {{guide:spoils.pay.honor@Boss Goombah#2}} | {{guide:spoils.pay.honor@Boss Goombah#3}} |
| PvE-poäng per nedskjutning | 14 | 14 | 14 |

**Byte**: en låda, för piloten som gjorde mest skada.

| Föremål |
| :--- |
| {{guide:spoils.box@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} |

### Goombah Guard

Bygger på Goombah med 20 % av skrov, sköld och skada; hastighet och räckvidd är förlagans.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | {{guide:vitals.hull@Goombah Guard#1}} | {{guide:vitals.hull@Goombah Guard#2}} | {{guide:vitals.hull@Goombah Guard#3}} |
| Sköld | {{guide:vitals.shield@Goombah Guard#1}} | {{guide:vitals.shield@Goombah Guard#2}} | {{guide:vitals.shield@Goombah Guard#3}} |
| Laserskada (en salva per sekund) | {{guide:vitals.dps@Goombah Guard#1}} | {{guide:vitals.dps@Goombah Guard#2}} | {{guide:vitals.dps@Goombah Guard#3}} |
| Hastighet | {{guide:vitals.speed@Goombah Guard#1}} | {{guide:vitals.speed@Goombah Guard#2}} | {{guide:vitals.speed@Goombah Guard#3}} |
| Laserräckvidd | 800 | 800 | 800 |
| Aggroradie | bara när den attackeras | bara när den attackeras | bara när den attackeras |
| Läker ledaren, var och en, per sekund (bara skrovet) | 110 | 165 | 220 |
| Krediter | {{guide:spoils.pay.credits@Goombah Guard#1}} | {{guide:spoils.pay.credits@Goombah Guard#2}} | {{guide:spoils.pay.credits@Goombah Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Goombah Guard#1}} | {{guide:spoils.pay.thulium@Goombah Guard#2}} | {{guide:spoils.pay.thulium@Goombah Guard#3}} |
| Erfarenhet (XP) | {{guide:spoils.pay.experience@Goombah Guard#1}} | {{guide:spoils.pay.experience@Goombah Guard#2}} | {{guide:spoils.pay.experience@Goombah Guard#3}} |
| Heder | {{guide:spoils.pay.honor@Goombah Guard#1}} | {{guide:spoils.pay.honor@Goombah Guard#2}} | {{guide:spoils.pay.honor@Goombah Guard#3}} |
| PvE-poäng per nedskjutning | 3 | 3 | 3 |

**Byte**: inget. Nedskjutningen betalar bara sina krediter, sitt Thulium, sin XP och sin heder.

<!-- goombah-members:end -->
