<!-- wiki-i18n source: fcba1b51b68a9123 -->
<!-- wiki-i18n title: Dormant-svärm -->
# Dormant-svärm {#dormant-swarm}

Dormant-svärmen är en **Dormant Force** med sina **Dormant Pulses**: en grupp skepp som aldrig börjar en strid och slår mycket hårt när de väl väckts. Det finns bara en i varje världs farosektorer ([Deep Void](/wiki/03-Mechanics/Deep-Void.md#the-dormant-swarms-visit) har ett eget besök, en gång om dagen). Den drar från en farosektor till nästa, och den är den hårdaste striden och det rikaste bytet bland svärmarna: en strid för en stor grupp av de starkaste skeppen. Från säsongsdag 11 börjar den vid [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) på `DS-4`, kommer tillbaka tidigare och betalar dubbelt (se listan *I korthet*).

## I korthet {#at-a-glance}

<!-- dormant-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Var**: Farosektorerna `DS-1`, `DS-2`, `DS-3`, `DS-4`, flyger från den ena till den andra
- **Hur många**: En i varje värld
- **Dyker upp**: Från säsongsdag 4 till wipen (Beta och Gamma: från säsongsdag 1)
- **Ledare**: Dormant Force
- **Följeslagare**: 2 × Dormant Pulse, som flyger med ledaren
- **Följeslagarna håller sig inom**: högst 700 enheter från ledaren
- **När ledaren förstörs**: Dormant Pulse tar över som ledare
- **När ledaren förstörs**: Följeslagarna försvinner 30 s efter att ledaren förstörts, även om de just attackerar
- **Förflyttning**: Stannar 8 till 15 min på en karta och flyger sedan till porten till en annan farosektor. Den tar aldrig portarna ut ur farosektorerna och flyger aldrig in i det svarta hålets ring
- **Kommer tillbaka**: {{guide:vitals.respawn@Dormant Force#1;Dormant Force#2;Dormant Force#3}} efter att hela svärmen förstörts, i en slumpmässig farosektor
- **Från säsongsdag 11**: Den dyker upp vid [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) på `DS-4` i stället för i en slumpmässig farosektor, kommer tillbaka 30 min efter att hela svärmen förstörts, och varje skepp betalar ×2 (krediter, Thulium, XP och heder; bytet förblir detsamma)
- **Meddelanden**: Piloterna i hela världen får veta när svärmen dyker upp och när den förstörs. Det är systemrader: de syns på chattens flik **System**, med en räknare för olästa rader, och inte i **Global** eller **Lokal**. En markering visar den på kartorna över farosektorerna och på galaxkartan. Dödsloggen nämner piloten som nedskjutningen tillskrivs.

<!-- dormant-glance:end -->

## Medlemmarna {#the-members}

- **Dormant Force**: en Wraith med full styrka, med lasrar som slår tre gånger så hårt som en typisk utrustnings. Den leder svärmen, är passiv tills den träffas och skjuter **raka raketer** på den första piloten som träffade den.
- **Dormant Pulse**: en Paragon med full styrka, med tunga lasrar av samma slag, där varje laser slår dubbelt så hårt som en av Forces, och egna raketer. En Pulse har färre lasrar än Force, så dess hela salva är större än Forces men inte dubbelt så stor (siffrorna står nedan). Pulses flyger nära Force, och när Force förstörs tar en av dem över ledningen.

De är passiva: de går aldrig på en pilot. Träffas en av dem ansluter sig de andra i närheten till striden mot den första piloten som träffade den.

## Hur striden går till {#how-the-fight-goes}

- **Hitta den.** Hela världen får veta när den dyker upp, och en markering visar den på kartorna över farosektorerna och på galaxkartan. Den stannar på en karta så länge listan *I korthet* anger, flyger sedan till porten till en annan farosektor och hoppar; den tar aldrig en port ut ur farosektorerna och flyger aldrig in i det svarta hålets ring. Den flyger med hastigheten hos sitt långsammaste skepp och startar eller avslutar, liksom en pilot, inget hopp under beskjutning. Från säsongsdag 11 dyker den först upp strax utanför zonen kring [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md), där en grupp kan vänta på den utanför träskets kanoner, och flyger sedan ut genom en port i `DS-4`.
- **Den går inte att besegra ensam, eller med några få.** Åtta piloter på nivå 8 i Paragon med ammunition x2 eller x4 förstör den på ungefär en minut i Alpha och förlorar högst ett skepp; en Paragon ensam förstörs, och det gör även tre eller fyra med ammunition x2. Svärmarna i Beta och Gamma är starkare ([Världar](/wiki/05-Swarms/Swarms.md#the-worlds)), så de världarna kräver större grupper.
- **Dess lasrar avgör striden.** Tillsammans kan de förstöra en Paragon på under en minut, och till och med en med de bästa sköldarna på under två, med eller utan raketer: få in din skada snabbt, med de bästa sköldarna du har.
- **Skepp för skepp.** Varje skepp har sitt eget skrov och sin egen betalning, så Force eller en Pulse kan förstöras först. Svärmen ersätts först när den är helt förstörd, efter tiden i listan *I korthet*.

## Ledarens tre steg {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Striden har tre steg ([hur de fungerar](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); vart och ett sker en gång.

- **I början**: Tar 70 % av varje träff så länge en av dess Dormant Pulses lever.
- **Under två tredjedelar**: Dess Dormant Pulses avfyrar en raket var 2,5 s i 15 s.
- **Under en tredjedel**: Så länge alla dess Dormant Pulses lever läker de den med 5 % av skrovet per sekund i 6 s.

<!-- mob-ladder:end -->

## Belöningar och byte {#rewards-and-drops}

Varje skepp betalar för sig, efter den skada det fick ([hur nedskjutningen av en boss betalar](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)), och varje skepp tappar en låda till piloten som gjorde mest skada på det. **Forces låda** är priset: väldigt mycket x3- och x4-ammunition, Episka raketer av ett slag och då och då en N.I.K.E. eller en N.U.K.E. **Pulses** kan tappa en Ancient Control Unit, en Power Core eller Dark Matter. En minuts strid mot svärmen betalar mer än en minuts strid mot Crystalys, den bäst betalande utomjordingen. Från säsongsdag 11 betalar varje skepp dubbelt (se listan *I korthet*); lådorna är desamma.

## Värdena {#the-numbers}

Värdena för svärmens skepp i de tre världarna ([Världar](/wiki/05-Swarms/Swarms.md#the-worlds)). Krediterna, Thulium, XP och heder i tabellerna är betalningen före säsongsdag 11; från den dagen betalar en nedskjutning dubbelt.

<!-- dormant-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Dormant Force

Bygger på Wraith med 100 % av skrovet och 300 % av laserskadan; hastighet och räckvidd är förlagans. Skjuter en rak raket var 5 s: [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | {{guide:vitals.hull@Dormant Force#1}} | {{guide:vitals.hull@Dormant Force#2}} | {{guide:vitals.hull@Dormant Force#3}} |
| Sköld | {{guide:vitals.shield@Dormant Force#1}} | {{guide:vitals.shield@Dormant Force#2}} | {{guide:vitals.shield@Dormant Force#3}} |
| Laserskada (en salva per sekund) | {{guide:vitals.dps@Dormant Force#1}} | {{guide:vitals.dps@Dormant Force#2}} | {{guide:vitals.dps@Dormant Force#3}} |
| Hastighet | {{guide:vitals.speed@Dormant Force#1}} | {{guide:vitals.speed@Dormant Force#2}} | {{guide:vitals.speed@Dormant Force#3}} |
| Laserräckvidd | 800 | 800 | 800 |
| Aggroradie | bara när den attackeras | bara när den attackeras | bara när den attackeras |
| Raketskada, högst | {{guide:behaviour.ability:rocket.damage@Dormant Force#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#3}} |
| Krediter | {{guide:spoils.pay.credits@Dormant Force#1}} | {{guide:spoils.pay.credits@Dormant Force#2}} | {{guide:spoils.pay.credits@Dormant Force#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Force#1}} | {{guide:spoils.pay.thulium@Dormant Force#2}} | {{guide:spoils.pay.thulium@Dormant Force#3}} |
| Erfarenhet (XP) | {{guide:spoils.pay.experience@Dormant Force#1}} | {{guide:spoils.pay.experience@Dormant Force#2}} | {{guide:spoils.pay.experience@Dormant Force#3}} |
| Heder | {{guide:spoils.pay.honor@Dormant Force#1}} | {{guide:spoils.pay.honor@Dormant Force#2}} | {{guide:spoils.pay.honor@Dormant Force#3}} |
| PvE-poäng per nedskjutning | 25 | 25 | 25 |

**Byte**: en låda, för piloten som gjorde mest skada.

| Föremål |
| :--- |
| {{guide:spoils.box@Dormant Force#1;Dormant Force#2;Dormant Force#3}} |

### Dormant Pulse

Bygger på Paragon med 100 % av skrovet och 600 % av laserskadan; hastighet och räckvidd är förlagans. Skjuter en rak raket var 5 s: [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | {{guide:vitals.hull@Dormant Pulse#1}} | {{guide:vitals.hull@Dormant Pulse#2}} | {{guide:vitals.hull@Dormant Pulse#3}} |
| Sköld | {{guide:vitals.shield@Dormant Pulse#1}} | {{guide:vitals.shield@Dormant Pulse#2}} | {{guide:vitals.shield@Dormant Pulse#3}} |
| Laserskada (en salva per sekund) | {{guide:vitals.dps@Dormant Pulse#1}} | {{guide:vitals.dps@Dormant Pulse#2}} | {{guide:vitals.dps@Dormant Pulse#3}} |
| Hastighet | {{guide:vitals.speed@Dormant Pulse#1}} | {{guide:vitals.speed@Dormant Pulse#2}} | {{guide:vitals.speed@Dormant Pulse#3}} |
| Laserräckvidd | 800 | 800 | 800 |
| Aggroradie | bara när den attackeras | bara när den attackeras | bara när den attackeras |
| Raketskada, högst | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#3}} |
| Krediter | {{guide:spoils.pay.credits@Dormant Pulse#1}} | {{guide:spoils.pay.credits@Dormant Pulse#2}} | {{guide:spoils.pay.credits@Dormant Pulse#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Pulse#1}} | {{guide:spoils.pay.thulium@Dormant Pulse#2}} | {{guide:spoils.pay.thulium@Dormant Pulse#3}} |
| Erfarenhet (XP) | {{guide:spoils.pay.experience@Dormant Pulse#1}} | {{guide:spoils.pay.experience@Dormant Pulse#2}} | {{guide:spoils.pay.experience@Dormant Pulse#3}} |
| Heder | {{guide:spoils.pay.honor@Dormant Pulse#1}} | {{guide:spoils.pay.honor@Dormant Pulse#2}} | {{guide:spoils.pay.honor@Dormant Pulse#3}} |
| PvE-poäng per nedskjutning | 11 | 11 | 11 |

**Byte**: en låda, för piloten som gjorde mest skada.

| Föremål |
| :--- |
| {{guide:spoils.box@Dormant Pulse#1;Dormant Pulse#2;Dormant Pulse#3}} |

<!-- dormant-members:end -->
