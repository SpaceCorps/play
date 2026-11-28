<!-- wiki-i18n source: 7c6bc3eaf70223f5 -->
<!-- wiki-i18n title: Seeker-svärm -->
# Seeker-svärm {#seeker-swarm}

Seeker-svärmen är den minsta av [svärmarna](/wiki/05-Swarms/Swarms.md): en **Boss Seeker** och de **Seeker Slaves** som vaktar och läker den. Den håller till i sektorerna där nya piloter börjar flyga, så den är den första svärmen de flesta möter. Boss Seeker börjar aldrig en strid, men så snart du skjuter på den är den mycket farligare än den [Seeker](/wiki/04-Aliens/Seeker.md) den bygger på.

## I korthet {#at-a-glance}

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Var**: Sektorerna `x-1` och `x-2` i varje koncern
- **Hur många**: En i var och en av de sektorerna, 6 i varje värld
- **Dyker upp**: Från säsongsdag 4 till wipen (Beta och Gamma: från säsongsdag 1)
- **Ledare**: Boss Seeker
- **Följeslagare**: Upp till 4 × Seeker Slave, en ny var 10 s
- **Följeslagarna håller sig inom**: högst 500 enheter från ledaren
- **Läkning**: Varje Seeker Slave inom 600 enheter från ledaren läker dess skrov, 50 HP per sekund i Alpha
- **När ledaren förstörs**: Följeslagarna försvinner 30 s efter att ledaren förstörts, om de inte just attackerar
- **Kommer tillbaka**: {{guide:vitals.respawn@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} efter att ledaren förstörts, i samma sektor
- **Meddelanden**: Piloterna i sektorn får veta när ledaren dyker upp och när den förstörs. Det är systemrader: de syns på chattens flik **System**, med en räknare för olästa rader, och inte i **Global** eller **Lokal**. Dödsloggen nämner piloten som nedskjutningen tillskrivs.

<!-- seeker-glance:end -->

## Medlemmarna {#the-members}

- **Boss Seeker**: en mycket större Seeker, i svärmens nyans och med sitt namn ovanför, med många gånger en Seekers skrov, sköld och skada (värdena står nedan). Den är passiv: den drar omkring tills en pilot träffar den, stannar sedan där den är och skjuter på piloten, och svärmens skepp i närheten ansluter sig till striden. Vapnets räckvidd och hastigheten är en Seekers, och den reparerar aldrig sitt skrov själv. Dess [tre steg](#the-leaders-three-steps) och en [specialförmåga](/wiki/03-Mechanics/Special-Abilities.md) kan ändra på det.
- **Seeker Slave**: en vanlig Seeker i svärmens nyans. Slaves håller sig nära bossen, ansluter sig till striden när ett svärmskepp i närheten träffas, och var och en som är nära bossen läker dess skrov. En Slave reparerar sitt eget skrov efter en vila, som en Seeker gör.

## Hur striden går till {#how-the-fight-goes}

- **Låt den vara tills ditt skepp klarar den.** En Boss Seeker slår hårdare än en pilots första skepp tål: en ny pilots Protos, ännu utan sköld, förstörs på sekunder så snart bossen och dess Slaves är över den.
- **Håll dig utom räckhåll.** Bossen och dess Slaves är långsammare än en Protos, och deras vapen når kortare än en Quantum Laser II (se [Lasrar och ammunition](/wiki/06-Items/Lasers.md)): en pilot som har sådana lasrar och håller sig bortom deras räckvidd tar ingen skada medan de skjuter. En pilot med Quantum Laser I kan inte hålla sig utom räckhåll.
- **Slaves läker snabbare än en ensam ny pilot träffar.** Tillsammans läker de mer än en pilots lasrar gör med ammunition x1, så ta med en kamrat och ammunition x2. Två piloter med Quantum Laser II som håller avstånd fäller bossen på ungefär en minut i Alpha, och mycket snabbare med ammunition x2.
- **Bossen kommer tillbaka** efter tiden i listan *I korthet*, vid full styrka, i samma sektor, och dess Slaves kommer en efter en.

## Ledarens tre steg {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Striden har tre steg ([hur de fungerar](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); vart och ett sker en gång.

- **I början**: Dess Seeker Slaves läker den ×2 så fort i 8 s.
- **Under två tredjedelar**: 2 kopior av den dyker upp, och den riktiga bär en ring.
- **Under en tredjedel**: Flyr från piloterna i 4 s och vänder sedan om.

<!-- mob-ladder:end -->

## Belöningar och byte {#rewards-and-drops}

Boss Seeker betalar **exakt tio Seekers**: tio gånger en Seekers krediter, Thulium, XP och heder, delat efter skada mellan piloterna som stred mot den ([hur nedskjutningen av en boss betalar](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Dess låda innehåller tio Seekers byte och därtill ammunition och raketer under Episk, för piloten som gjorde mest skada. Slaves betalar lite och tappar ingenting; att skjuta ner dem är ingen farmning, eftersom de kommer tillbaka med bossen.

## Värdena {#the-numbers}

Värdena för svärmens skepp i de tre världarna ([Världar](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker

Bygger på Seeker med 400 % av skrov, sköld och skada; hastighet och räckvidd är förlagans.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | {{guide:vitals.hull@Boss Seeker#1}} | {{guide:vitals.hull@Boss Seeker#2}} | {{guide:vitals.hull@Boss Seeker#3}} |
| Sköld | {{guide:vitals.shield@Boss Seeker#1}} | {{guide:vitals.shield@Boss Seeker#2}} | {{guide:vitals.shield@Boss Seeker#3}} |
| Laserskada (en salva per sekund) | {{guide:vitals.dps@Boss Seeker#1}} | {{guide:vitals.dps@Boss Seeker#2}} | {{guide:vitals.dps@Boss Seeker#3}} |
| Hastighet | {{guide:vitals.speed@Boss Seeker#1}} | {{guide:vitals.speed@Boss Seeker#2}} | {{guide:vitals.speed@Boss Seeker#3}} |
| Laserräckvidd | 600 | 600 | 600 |
| Aggroradie | bara när den attackeras | bara när den attackeras | bara när den attackeras |
| Krediter | {{guide:spoils.pay.credits@Boss Seeker#1}} | {{guide:spoils.pay.credits@Boss Seeker#2}} | {{guide:spoils.pay.credits@Boss Seeker#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Seeker#1}} | {{guide:spoils.pay.thulium@Boss Seeker#2}} | {{guide:spoils.pay.thulium@Boss Seeker#3}} |
| Erfarenhet (XP) | {{guide:spoils.pay.experience@Boss Seeker#1}} | {{guide:spoils.pay.experience@Boss Seeker#2}} | {{guide:spoils.pay.experience@Boss Seeker#3}} |
| Heder | {{guide:spoils.pay.honor@Boss Seeker#1}} | {{guide:spoils.pay.honor@Boss Seeker#2}} | {{guide:spoils.pay.honor@Boss Seeker#3}} |
| PvE-poäng per nedskjutning | 5 | 5 | 5 |

**Byte**: en låda, för piloten som gjorde mest skada.

| Föremål |
| :--- |
| {{guide:spoils.box@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} |

### Seeker Slave

Bygger på Seeker med 100 % av skrov, sköld och skada; hastighet och räckvidd är förlagans.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | {{guide:vitals.hull@Seeker Slave#1}} | {{guide:vitals.hull@Seeker Slave#2}} | {{guide:vitals.hull@Seeker Slave#3}} |
| Sköld | {{guide:vitals.shield@Seeker Slave#1}} | {{guide:vitals.shield@Seeker Slave#2}} | {{guide:vitals.shield@Seeker Slave#3}} |
| Laserskada (en salva per sekund) | {{guide:vitals.dps@Seeker Slave#1}} | {{guide:vitals.dps@Seeker Slave#2}} | {{guide:vitals.dps@Seeker Slave#3}} |
| Hastighet | {{guide:vitals.speed@Seeker Slave#1}} | {{guide:vitals.speed@Seeker Slave#2}} | {{guide:vitals.speed@Seeker Slave#3}} |
| Laserräckvidd | 600 | 600 | 600 |
| Aggroradie | bara när den attackeras | bara när den attackeras | bara när den attackeras |
| Läker ledaren, var och en, per sekund (bara skrovet) | 50 | 75 | 100 |
| Krediter | {{guide:spoils.pay.credits@Seeker Slave#1}} | {{guide:spoils.pay.credits@Seeker Slave#2}} | {{guide:spoils.pay.credits@Seeker Slave#3}} |
| Thulium | {{guide:spoils.pay.thulium@Seeker Slave#1}} | {{guide:spoils.pay.thulium@Seeker Slave#2}} | {{guide:spoils.pay.thulium@Seeker Slave#3}} |
| Erfarenhet (XP) | {{guide:spoils.pay.experience@Seeker Slave#1}} | {{guide:spoils.pay.experience@Seeker Slave#2}} | {{guide:spoils.pay.experience@Seeker Slave#3}} |
| Heder | {{guide:spoils.pay.honor@Seeker Slave#1}} | {{guide:spoils.pay.honor@Seeker Slave#2}} | {{guide:spoils.pay.honor@Seeker Slave#3}} |
| PvE-poäng per nedskjutning | 1 | 1 | 1 |

**Byte**: inget. Nedskjutningen betalar bara sina krediter, sitt Thulium, sin XP och sin heder.

<!-- seeker-members:end -->
