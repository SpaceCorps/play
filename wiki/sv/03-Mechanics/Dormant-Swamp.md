<!-- wiki-i18n source: a8a96edb9a5070f1 -->
<!-- wiki-i18n title: Dormant Swamp -->
# Dormant Swamp

<!-- wiki-search: swamp; dormant swamp; base; turret; turrets; nike turret; laser turret; inert mass; unwakened; the unwakened; slumbering void; void; dormant lance; ds-4; träsk; torn; kanon; kanoner -->

För länge sedan levde en avancerad civilisation mitt i galaxen. Den byggde i lila-svart kristall med lysande violetta ådror, och av ett skäl som ingen känner till föll den samman. **Dormant Swamp** är dess utpost, i det övre vänstra hörnet av `DS-4`. Från säsongsdag 11 rör det på sig: kanoner i mitten skjuter på varje skepp de ser, **Inert Masses** vaktar det, och allra längst in i mitten sover **Unwakened**. Det är en plats som piloter **ännu inte är avsedda att besöka**. Kamouflerad kan du flyga ända fram till Unwakened, och mer går inte att göra där just nu: basen och dess kanoner kan inte skadas, beträdas, borda eller handlas med.

Träsket är också dit [Dormant-svärmen](/wiki/05-Swarms/Dormant-Swarm.md) kommer från dag 11, och **Slumbering Voids** patrullerar runt det. Samma Voids kommer i vågor till [jättegrävmaskinerna](/wiki/03-Mechanics/Giant-Excavator.md#the-slumbering-voids). Sektorerna finns i [Farosektorer](/wiki/01-General/Danger-Sectors.md).

## I korthet {#at-a-glance}

<!-- swamp-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Var**: Det övre vänstra hörnet av `DS-4`: mitten ligger vid 5 000 / 5 000
- **Dyker upp**: Från säsongsdag 11 till wipen
- **Zonen**: 4 300 enheter runt mitten: så långt kanonerna når, och platsen som ingen ännu är avsedd att besöka
- **Varningen**: Ett skepp som korsar ringen 4 800 enheter från mitten får en systemrad
- **Kamouflage**: Ingen kanon ser någonsin ett kamouflerat skepp, eller ett inne i en EMP:s fönster
- **Utomjordingarna**: 5 Inert Masses håller sig inom 2 400 enheter från mitten. Unwakened sover i mitten. 2 Slumbering Voids patrullerar mellan 4 600 och 6 500 enheter från mitten.
- **Dormant-svärmen**: Den dyker upp vid 9 417 / 6 606, 4 700 enheter från mitten och utanför zonen
- **Stenar**: Ingen asteroid ligger inom 4 900 enheter från mitten

<!-- swamp-glance:end -->

## Kanonerna {#the-guns}

Träskets torn skjuter på det **närmaste skepp de kan se** inom sin räckvidd, och på inget annat: zonen är den cirkel som den av dem som når längst når. De är inga entiteter av något slag: de har inga träffpoäng, kan inte väljas som mål, och inget du skjuter på dem gör något. Deras skott är verkliga, och världen skalar deras skada som den skalar varje utomjordings vapen.

<!-- swamp-guns:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Skada per skott, i varje värld:

| Kanon | Plats | Skjuter var | Räckvidd (enheter) | Alpha | Beta | Gamma |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets)-torn | 5 000 / 4 400 | 2 s | 3 640 | 75 000 | 112 500 | 150 000 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets)-torn | 5 000 / 4 400 | 5 s | 1 080 | 50 000 | 75 000 | 100 000 |
| Laserkanon × 2 | 3 600 / 5 200; 6 400 / 5 200 | 1 s | 2 500 | 45 000–55 000 | 67 500–82 500 | 90 000–110 000 |

- En raket avfyras från 90 % av sin räckvidd, så att den når fram; ett lasertorn skjuter en gång i sekunden, och dess skada slumpas inom det visade intervallet.
- En N.I.K.E. har 35 % sköldgenomträngning, som dras av från en sköldabsorption.
- En N.U.K.E. exploderar över en radie på 900 enheter, hårdast i mitten.

<!-- swamp-guns:end -->

- **Ingenting når utanför zonen,** och inne i den förstörs ett skepp på sekunder: ju närmare mitten det kommer, desto fler kanoner tillkommer, och inte ens den bäst skyddade Wraith håller.
- **Kamouflage tar dig in.** Inget torn ser någonsin ett kamouflerat skepp, eller ett inne i en EMP:s fönster, på något avstånd. En explosion riktad mot ett synligt skepp som brister bredvid ett kamouflerat skadar det ändå och avslutar dess kamouflage.
- **De skjuter bara på piloter,** aldrig på utomjordingar, koncernpiloter eller svärmen, och skyddet hos ett skepp som nyss kommit tillbaka efter en förstörelse gäller också mot dem.
- **Varningsringen.** Ett skepp som korsar ringen utanför zonen får en systemrad: tornen skjuter på varje skepp de ser, och något sover i mitten. Det varnas igen först när det har lämnat ringen och kommit tillbaka.
- **Att ta sig ut.** Om du förstörs där och återvänder på platsen, eller loggar in inne i zonen, placeras du utanför. En kurs du klickar böjs runt zonen, och ett meddelande varnar när platsen du klickar på ligger innanför.

## Utomjordingarna {#the-aliens}

Tre utomjordingar från den försvunna civilisationen lever här, var och en med egna siffror. De betalas som en svärms boss: **efter den skada som gjorts**, till varje pilot som gjort minst den andel som anges i [Svärmar](/wiki/05-Swarms/Swarms.md#the-rules-of-every-swarm), och lådan går till piloten som gjorde mest skada. Deras nedskjutningar räknas till dina PvE-poäng för grad som en svärmskepps, i proportion till betalningen ([Grader](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points)). Var och ens sköld tar upp 80 % av varje träff så länge den håller ([Sköldar](/wiki/03-Mechanics/Shields.md)).

- **Slumbering Void.** Den smäckra jägaren, den snabbaste utomjordingen i spelet (lika snabb som en Storm med Afterburner III). Några patrullerar alltid träskets omgivning, och andra kommer i vågor till grävmaskinerna. Den är aggressiv, jagar den närmaste pilot den kan se och ser aldrig ett kamouflerat skepp.
- **Inert Mass.** Ett dött vrak med violetta sprickor, stort som en liten station. De håller sig inom ett fast avstånd från träskets mitt och lämnar det inte just nu. Den skjuter **Dormant Lances**: styrda raketer med mycket lång räckvidd som följer ett skepp tills det kamouflerar sig, öppnar ett EMP-fönster, går in i en säker ring, hoppar eller dör. Den är snabbare än varje skepp, så bara de avbrotten hjälper.
- **Unwakened.** En monolit som sover i träskets mitt, det största på någon karta, så långsam att den aldrig hinner ikapp ett skepp. Den skjuter ingenting, men varje skepp inom dess aura brinner, **kamouflerat eller inte**. Den är **immun**: skott och raketer träffar och gör ingenting, målfönstret visar fulla staplar och ordet Immun. Ett senare event kommer att göra det möjligt att strida mot den; dess belöningar nedan är nedskrivna och går ännu inte att få.

<!-- swamp-members:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

### Slumbering Void

2 Slumbering Voids patrullerar mellan 4 600 och 6 500 enheter från träskets mitt; en som förstörs kommer tillbaka 1 h senare. En grävmaskins vågor för med sig fler av samma utomjording.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | 25 000 | 37 500 | 50 000 |
| Sköld | 150 000 | 225 000 | 300 000 |
| Sköldabsorption | 80 % | 80 % | 80 % |
| Laserskada (en salva per sekund) | 3 000 | 4 500 | 6 000 |
| Hastighet | 400 | 400 | 400 |
| Laserräckvidd | 800 | 800 | 800 |
| Aggroradie | 2 500 | 2 500 | 2 500 |
| Krediter | 23 000 | 46 000 | 69 000 |
| Thulium | 60 | 120 | 180 |
| Erfarenhet (XP) | 3 600 | 7 200 | 10 800 |
| Heder | 16 | 32 | 48 |
| PvE-poäng per nedskjutning | 10 | 10 | 10 |

**Byte**: en låda, för piloten som gjorde mest skada.

| Föremål | Chans | Mängd |
| :--- | ---: | ---: |
| En av Ultra Core och Experimental Fusion Core, slumpmässigt vald | 60 % | 30–60 |
| En av de 4 Episka [raketerna](/wiki/06-Items/Rockets.md), slumpmässigt vald | 40 % | 1–3 |

### Inert Mass

5 Inert Masses står inom 2 400 enheter från mitten; en som förstörs kommer tillbaka 1 h senare. Skjuter var 6 s en styrd [Dormant Lance](/wiki/06-Items/Rockets.md#the-craft-only-rockets) mot det närmaste skepp den kan se: hastighet 750, flygsträcka 5 250 enheter, 40 % penetration.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | 250 000 | 375 000 | 500 000 |
| Sköld | 100 000 | 150 000 | 200 000 |
| Sköldabsorption | 80 % | 80 % | 80 % |
| Skada per Dormant Lance | 5 000–8 000 | 7 500–12 000 | 10 000–16 000 |
| Hastighet | 60 | 60 | 60 |
| Raketräckvidd | 5 000 | 5 000 | 5 000 |
| Aggroradie | 5 000 | 5 000 | 5 000 |
| Krediter | 125 000 | 250 000 | 375 000 |
| Thulium | 335 | 670 | 1 005 |
| Erfarenhet (XP) | 20 200 | 40 400 | 60 600 |
| Heder | 88 | 176 | 264 |
| PvE-poäng per nedskjutning | 15 | 15 | 15 |

**Byte**: en låda, för piloten som gjorde mest skada.

| Föremål | Chans | Mängd |
| :--- | ---: | ---: |
| Ultra Core och Experimental Fusion Core, delat lika | 100 % | 400–800 totalt |
| En av de 4 Episka [raketerna](/wiki/06-Items/Rockets.md), slumpmässigt vald | 100 % | 20–40 |
| N.I.K.E. | 5 % | 1–2 |
| Dark Matter | 5 % | 1–3 |
| Ancient Control Unit | 10 % | 1 |
| Power Core | 25 % | 1–2 |

### The Unwakened

Det finns en, i träskets mitt och ingen annanstans; den kommer tillbaka 24 h efter att den förstörts. Den är **immun** tills ett senare uppdrag stänger av flaggan: skott och raketer träffar den och gör ingenting. Dess belöningar är nedskrivna och går ännu inte att få.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Skrov | 10 000 000 | 15 000 000 | 20 000 000 |
| Sköld | 10 000 000 | 15 000 000 | 20 000 000 |
| Sköldabsorption | 80 % | 80 % | 80 % |
| Auraskada per sekund, på varje skepp inuti | 75 000 | 112 500 | 150 000 |
| Auraradie | 700 | 700 | 700 |
| Hastighet | 10 | 10 | 10 |
| Aggroradie | 3 000 | 3 000 | 3 000 |
| Krediter | 7 500 000 | 15 000 000 | 22 500 000 |
| Thulium | 20 000 | 40 000 | 60 000 |
| Erfarenhet (XP) | 1 200 000 | 2 400 000 | 3 600 000 |
| Heder | 5 200 | 10 400 | 15 600 |
| PvE-poäng per nedskjutning | 112 | 112 | 112 |

**Byte**: en låda, för piloten som gjorde mest skada.

| Föremål | Chans | Mängd |
| :--- | ---: | ---: |
| Ultra Core och Experimental Fusion Core, delat lika | 100 % | 10 000–15 000 totalt |
| En av de 4 Episka [raketerna](/wiki/06-Items/Rockets.md), slumpmässigt vald | 100 % | 500–800 |
| N.I.K.E. | 100 % | 20–30 |
| N.U.K.E. | 100 % | 5–10 |
| Dark Matter | 100 % | 40–60 |
| Ancient Control Unit | 100 % | 10–20 |
| Power Core | 100 % | 100–200 |

<!-- swamp-members:end -->

## Vad du kan göra här {#what-to-do-here}

- **Titta, rör inte.** Träsket är till senare. Det enda du når utan kamouflage ligger utanför zonen: de patrullerande Voids, i en ring runt zonen, är träskets första linje och platsen där en grupp kan slåss utan kanonerna.
- **Bekämpa Voids med penetration.** En Voids stora sköld tar upp 80 % av en träff och betyder nästan ingenting: skrovet bakom är litet. Ju mer sköldpenetration dina lasrar har, desto förr faller den ([Lasrar och ammunition](/wiki/06-Items/Lasers.md)).
- **Håll dig undan Lances.** En Inert Mass ser långt och en Lance går inte att köra ifrån: bryt dess grepp med kamouflage, en EMP, en säker ring eller ett hopp, eller lämna dess räckvidd. En Mass är en lång strid även för en stor grupp av de starkaste skeppen.
- **Dormant-svärmen** dyker nu upp strax utanför zonen, så en grupp kan vänta på den utan kanonerna. Se [Dormant-svärm](/wiki/05-Swarms/Dormant-Swarm.md).

## Läs mer {#where-to-read-more}

- [Farosektorer](/wiki/01-General/Danger-Sectors.md): vad som förändrades på dag 11.
- [Jättegrävmaskin](/wiki/03-Mechanics/Giant-Excavator.md): vågorna av Slumbering Voids och det de vaktar.
- [Svärmar](/wiki/05-Swarms/Swarms.md) och [Dormant-svärm](/wiki/05-Swarms/Dormant-Swarm.md): så betalar en bossnedskjutning.
- [Raketer](/wiki/06-Items/Rockets.md#the-craft-only-rockets): N.I.K.E. och N.U.K.E. som tornet skjuter.
- [Svart hål](/wiki/03-Mechanics/Black-Hole.md): `DS-4`:s andra fara.
- [Last](/wiki/03-Mechanics/Cargo.md): lådorna som utomjordingarna tappar.
