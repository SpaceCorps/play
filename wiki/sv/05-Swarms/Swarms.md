<!-- wiki-i18n source: c1ec7aa1207d519d -->
<!-- wiki-i18n title: Svärmar -->
# Svärmar {#swarms}

En **svärm** är en grupp utomjordingar som drar runt i en del av galaxen under en **ledare**: en boss, mycket starkare än någon utomjording omkring den, med **följeslagare** som vaktar den och, i två av svärmarna, läker den. Det finns tre, och var och en har sin egen artikel:

- [Seeker-svärm](/wiki/05-Swarms/Seeker-Swarm.md): Boss Seeker och dess Seeker Slaves, den minsta svärmen, i sektorerna där nya piloter flyger.
- [Pirate-svärm](/wiki/05-Swarms/Pirate-Swarm.md): Pirate Boss och dess Pirate Scouts, en lång strid för en grupp.
- [Dormant-svärm](/wiki/05-Swarms/Dormant-Swarm.md): Dormant Force och dess Dormant Pulses, den starkaste svärmen, med det rikaste bytet.

Deras skepp är **utomjordingar av egna slag**: de har egna namn och egna nedskjutningsräknare, och inget av dem räknas som en Seeker, en Phantasm eller någon annan utomjording. Ett svärmskepp har formen av skeppet det bygger på, i en egen nyans och med sitt namn ovanför; Boss Seeker är en mycket större Seeker.

**Klanväktarna** är inga publika svärmar. En klan kallar fram sin egen väktare för sista steget i sin dagslinje, och bara den klanen kan skada den: ingen pilot möter en som ströftar omkring i en sektor, och tabellerna nedan listar dem inte. Se [Klaner](/wiki/03-Mechanics/Clans.md#clan-wardens).

## De tre svärmarna {#the-three-swarms}

<!-- swarms-list:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Svärm | Var | Hur många | Ledare | Följeslagare | Kommer tillbaka |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**Pirate-svärm**](/wiki/05-Swarms/Pirate-Swarm.md) | Sektorerna `x-2` och `x-3` i varje koncern | En i var och en av de sektorerna, 6 i varje värld | **Pirate Boss** | Upp till 5 × Pirate Scout, en ny var 10 s | 2 min efter att ledaren förstörts, i samma sektor |
| [**Dormant-svärm**](/wiki/05-Swarms/Dormant-Swarm.md) | Farosektorerna `DS-1`, `DS-2`, `DS-3`, `DS-4`, flyger från den ena till den andra | En i varje värld | **Dormant Force** | 2 × Dormant Pulse, som flyger med ledaren | 1 h efter att hela svärmen förstörts, i en slumpmässig farosektor |
| [**Seeker-svärm**](/wiki/05-Swarms/Seeker-Swarm.md) | Sektorerna `x-1` och `x-2` i varje koncern | En i var och en av de sektorerna, 6 i varje värld | **Boss Seeker** | Upp till 4 × Seeker Slave, en ny var 10 s | 2 min efter att ledaren förstörts, i samma sektor |

<!-- swarms-list:end -->

## När och var {#when-and-where}

Svärmarna börjar dyka upp vid **Första kontakten** och finns kvar till wipen (se [Wipe-tidslinjen](/wiki/03-Mechanics/Wipe-Timeline.md); dagen står på första raden i reglerna nedan). **Varje värld har sina egna svärmar** på samma platser, så Pirate Boss i Alpha och den i Beta är två olika skepp, och en svärm du förstör i din värld är inte förstörd i en annan. En förstörd svärm kommer tillbaka efter tiden i tabellen ovan.

## Reglerna för varje svärm {#the-rules-of-every-swarm}

<!-- swarms-rules:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- Svärmarna dyker upp från säsongsdag 4 till wipen.
- När ett svärmskepp träffas ansluter sig svärmens skepp inom 1 500 enheter från det till striden mot den första piloten som träffade det.
- En ledare dyker upp minst 2 500 enheter från kanten av varje station- och portring.
- En pilot som gjort minst 5 % av skadan på en boss får betalt för dess nedskjutning.

<!-- swarms-rules:end -->

## Världarna {#the-worlds}

Världen skalar en svärm som den skalar varje utomjording ([Världar](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): ett svärmskepps skrov, sköld, sköldladdning, laserskada, raketskada och läkning är Alphas värden gånger styrkan nedan, och en nedskjutning betalar den betalning som anges nedan. Hastighet, räckvidd och byte är desamma i alla världar. Artiklarna anger varje skepps värden i alla tre världar.

<!-- swarms-world:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Värld | Styrka | Betalning |
| :--- | ---: | ---: |
| **Alpha** | ×1 | ×1 |
| **Beta** | ×1,5 | ×2 |
| **Gamma** | ×2 | ×3 |

<!-- swarms-world:end -->

## Vad piloterna får veta {#what-the-pilots-are-told}

Seeker- och Pirate-svärmarna meddelar piloterna i sin egen sektor när en boss dyker upp och när den förstörs. Dormant-svärmen meddelar hela sin värld, och den är markerad på kartorna över farosektorerna och på galaxkartan, så att piloter kan hitta den. Det är systemrader: de syns på chattens flik **System**, med en räknare för olästa rader, och inte i **Global** eller **Lokal**. Nedskjutningen av en boss får också en rad i dödsloggen som nämner piloten den tillskrivs. Listan *I korthet* i varje artikel säger vem som meddelas.

## Att strida mot en svärm {#fighting-a-swarm}

- **Ledarna börjar aldrig en strid.** En ledare drar omkring tills en pilot träffar den, svarar sedan, och svärmens skepp nära den ansluter sig till striden mot den första piloten som träffade den (avståndet står i reglerna ovan). Pirate Scouts är undantaget: de attackerar varje pilot som kommer nära. En ledare reparerar aldrig sitt skrov själv, så skadan du gjorde blir kvar på den om inte dess följeslagare läker den; dess sköld laddas om som hos alla utomjordingar.
- **Svärmskepp strider bara mot piloter.** De skjuter inte på utomjordingar och utomjordingar skjuter inte på dem, och [koncernpiloterna](/wiki/03-Mechanics/Company-Pilots.md) ignorerar dem: de jagar inte ett svärmskepp och kommer inte till din hjälp mot ett.
- **Raketer.** Pirate Boss samt Dormant Force och Pulses skjuter **raka** raketer, [Rivet-raketer](/wiki/06-Items/Rockets.md), på piloten som attackerade dem. Ett skepp som håller sig i rörelse undviker dem, ett som står still blir träffat.
- **Stridernas storlek.** Seeker-svärmen är till för två piloter, Pirate-svärmen för en liten grupp, Dormant-svärmen för en stor grupp av de starkaste skeppen; de högre världarna kräver fler piloter, som för varje utomjording.

## Vad du bör ha med dig {#what-to-bring}

- **En grupp.** Flyg i en [grupp](/wiki/03-Mechanics/Groups.md): svärmarna är balanserade för grupper, en ensam pilot på låg nivå förstörs snabbt, och bara de starkaste skeppen kan besegra en Pirate Boss ensamma. Ingen besegrar Dormant-svärmen ensam. En svärm strider mot den första piloten som träffade den ([Vem en utomjording strider mot](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)), så låt gruppens tåligaste skepp börja.
- **Bättre ammunition.** Ta med ammunition x2 eller bättre (se [Lasrar och ammunition](/wiki/06-Items/Lasers.md)). Läkningen från en svärms följeslagare kan vara större än vad en liten grupp gör med ammunition x1.
- **Sköldar och reparationer** för en lång strid: ditt skepps förmågor ([Förmågor](/wiki/03-Mechanics/Abilities.md)) betyder mest i striden mot piraterna, som tar minuter.
- **Plats att röra sig på.** Håll dig utanför räckvidden för ett vapen du överträffar i räckvidd, och fortsätt röra dig mot en raket.

## Hur nedskjutningen av en boss betalar {#how-a-boss-kill-pays}

En vanlig utomjording betalar piloten som träffade den först ([Strid](/wiki/03-Mechanics/Combat.md#kill-rewards-first-hit-claims)). En svärms ledare, och varje Dormant Pulse, betalar i stället **efter den skada som gjorts**:

- **Betalningen delas efter skada.** Varje pilot som gjort minst den andel som anges i reglerna ovan får betalt, i proportion till skadan: nedskjutningens krediter, Thulium, XP och heder delas mellan dem. En pilot under andelen får ingenting.
- **Lastlådan går till piloten som gjorde mest skada.** Den är den pilotens (och dess klans) i 30 sekunder, som för varje utomjording, och sedan kan vem som helst ta den ([Last](/wiki/03-Mechanics/Cargo.md)). Varje Dormant-skepp har sin egen skaderäkning och sin egen låda.
- **Följeslagare betalar som vanligt**: Pirate Scouts och Seeker Slaves betalar piloten som träffade dem först, och deras betalning är liten jämfört med en boss.
- **Betalningen för en boss är gjord för att slå utomjordingarna omkring den.** En minuts strid mot en Pirate Boss betalar mer än en minuts strid mot en Goombah, och Dormant-svärmen betalar ännu mer; Boss Seeker betalar exakt tio Seekers.

Varje nedskjutning räknas under skeppets eget namn i din nedskjutningsstatistik och ger PvE-poäng till din ranking:

<!-- swarms-points:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Svärmskepp | Svärm | PvE-poäng per nedskjutning |
| :--- | :--- | ---: |
| **Pirate Boss** | Pirate-svärm | 15 |
| **Pirate Scout** | Pirate-svärm | 4 |
| **Dormant Force** | Dormant-svärm | 25 |
| **Dormant Pulse** | Dormant-svärm | 11 |
| **Boss Seeker** | Seeker-svärm | 5 |
| **Seeker Slave** | Seeker-svärm | 1 |

<!-- swarms-points:end -->

En svärmnedskjutning räknas inte som nedskjutning av någon annan utomjording: en Boss Seeker eller en Seeker Slave är ingen Seeker för ett uppdrag som kräver Seekers, och milstolparna för wipepoäng ([Wipe-tidslinje](/wiki/03-Mechanics/Wipe-Timeline.md#earning-wipe-points)) gäller bara de fem utomjordingarna. Uppdragen som kräver svärmskepp finns uppräknade under [Svärmuppdrag](/wiki/03-Mechanics/Quests.md#swarm-missions).
