<!-- wiki-i18n source: 885da8b1fe8a0f3a -->
<!-- wiki-i18n title: Spacemap-resor -->
# Spacemap-resor {#spacemap-travel}

Spacemap är ditt navigeringsgränssnitt för att ta dig fram i SpaceCorps-universum. Varje koncern kontrollerar en del av rymden, ordnad i en bestämd topologi som möjliggör både säker utforskning och farliga PvP-möten.

## Universums uppbyggnad {#the-universe-structure}

Universum består av tre huvudsektorer för koncernerna (Mars, Terra, Galactic) och en central PvP-zon.

- **x-1 (hembas)**: Startkartan för varje koncern (M-1, T-1, G-1). Den säkraste zonen.
- **x-2 -> x-3**: Expansionszoner med successivt tuffare utomjordingar.
- **x-4 (gräns)**: Porten till PvP-sektorn.
- **DS-x (farosektorer)**: Den centrala PvP-zonen som förbinder alla koncerner: DS-1 till DS-4.

Bara hembaserna har en station. Det är där **Mission Control** öppnas, och dess säkra zon sträcker sig 1 600 enheter runt den. Farosektorerna har ingen station, `DS-1` inte heller: de enda säkra zonerna där är ringarna på 660 enheter runt hoppportalerna, och Mission Control kan inte öppnas där; flyg tillbaka till din bas för dina uppdrag.

Varje [värld](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) (Alpha, Beta, Gamma) har sin egen kopia av hela den här kartan, och var piloter får strida mot varandra beror på den: i Alpha bara i `x-4` och `DS-x`, i Beta överallt utom `x-1`, i Gamma överallt. Galaxkartan färglägger sektorerna efter din världs regel.

## Visualisering {#visualization}

Galaxkartan nedan visar det kända universums layout i realtid. I spelet är samma karta fönstret **Stjärnsystem**.

```spacemap

```

Med en [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) monterad väljer kartan också ditt mål: tryck på CPU:ns plats i snabbfältet (**JMP**) så öppnas fönstret Stjärnsystem i valläge. De sektorer som CPU:n kan ta dig till lyses upp; din egen sektor och farosektorerna gör det inte. Peka på en upplyst sektor för att läsa priset, klicka på den och bekräfta hoppet när kartan frågar (500 Thulium).

## Så reser du {#how-to-travel}

Resor på Spacemap sker via **portaler** (hoppportaler). [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) är den andra vägen: den behöver ingen portal (se slutet av den här sidan).

1. **Hitta en portal**: Portaler finns oftast i hörnen eller kanterna av en karta.
2. **Navigering**: Flyg ditt skepp nära portalstrukturen.
3. **Aktivering**: Tryck på **”J”** inom 500 enheter från portalen för att starta hoppet.
4. **Vänta**: Hoppet **tar 3 sekunder**. Ett fält ovanför snabbfältet (”Hoppar…”) fylls under tiden, och portalen lyser starkare när den laddas; andra piloter ser samma laddning på portalen när du hoppar. Ditt skepp fortsätter flyga, men du måste stanna inom 500 enheter från portalen tills tiden är ute: flyger du utom räckhåll avbryts hoppet (”Portalen är för långt bort för att hoppa.”, och fältet blir rött). Att trycka på **”J”** igen medan du hoppar gör ingenting annat än att tala om det för dig.
5. **Destination**: Du kommer fram vid motsvarande portal på målkartan.

### Hopp under eld {#jumping-under-fire}

- **Utanför farosektorerna** avbryter attacker, från utomjordingar eller andra piloter, **inte** ditt hopp: det slutförs.
- **I farosektorerna (`DS-1` till `DS-4`)** kan du inte hoppa ut medan du är under attack. Om en pilot eller en utomjording har träffat ditt skepp (dess sköldar eller skrov) under de senaste **10 sekunderna** startar inte hoppet (”Du är under attack: du kan inte hoppa ut ur en farosektor.”), och en träff medan du hoppar avbryter hoppet (fältet blir rött och spelet talar om varför). Skada du tar av det svarta hålets strålning är ingen attack, och inte heller ett skott som en säker zon stoppade. En träff du fick på kartan du hoppade från följer inte med genom portalen: du kommer fram med rent blad.
- Du gör en sak i taget: du kan inte plocka upp en [lastlåda](/wiki/03-Mechanics/Cargo.md) medan du hoppar, och att starta ett hopp avbryter en upplockning du hade påbörjat.
- Att stänga spelet eller återvända till basen mitt i ett hopp avbryter det: du kommer inte fram.
- **En CPU:s teleportering laddas som ett portalhopp.** En Jump CPU laddar i 5 sekunder och en Base CPU i 10, med ett fält ovanför snabbfältet. Ett skott du skjuter eller en träff du får, i vilken sektor som helst, avbryter den (inget betalas eller förbrukas), och ingen av de två CPU:erna startar inom 10 sekunder efter ett skott eller en träff. Tryck på CPU:ns plats igen för att avbryta den själv.

### Hoppförbindelser {#jump-links}

- **Koncernslingan**: Mars, Terra och Galactic har samma layout. Förbindelserna går som `1 <-> 2 <-> 3` och `2 <-> 4` och `3 <-> 4`. Det bildar en slinga mellan de sekundära kartorna (`x-2` och `x-3`) och gränskartan (`x-4`), där `x-1` fungerar som en säker ingång i änden som bara är ansluten till `x-2`: din startkarta har bara en portal.
- **Åtkomstportar till farosektorerna**: Varje koncerns gränskarta (`x-4`) är direkt förbunden med dess egen farosektor:
  - `M-4` leder till `DS-1`
  - `T-4` leder till `DS-2`
  - `G-4` leder till `DS-3`
- **Invasionsvägar (resor mellan koncerner)**: För att ta dig in på en fientlig koncerns territorium genom portalerna måste du korsa PvP-zonen. En pilot från Mars som vill invadera Terra måste till exempel flyga från `M-4` in i farosektorn `DS-1`, ta portalen till `DS-2` och sedan gå in i Terras rymd genom `T-4`; för att nå Galactic tar du portalen till `DS-3` och går in genom `G-4`.
- **Farosektortriangeln**: `DS-1`, `DS-2` och `DS-3` är alla förbundna med varandra. Var och en av dem har en koncerns portal (Mars i `DS-1`, Terra i `DS-2`, Galactic i `DS-3`); `DS-4` har ingen.
- **Kärnan i mitten**: Alla tre yttre farosektorer (`DS-1`, `DS-2` och `DS-3`) är direkt förbundna med mittkartan **`DS-4`**, den farligaste och mest givande PvP-zonen i universum. Ett **svart hål** hänger mitt i den: portalerna och lederna mellan dem ligger långt från det, men ett skepp som flyger in känner dess strålning, sedan dess dragning, och förstörs vid dess händelsehorisont. Se [Det svarta hålet](/wiki/03-Mechanics/Black-Hole.md).

### Jump CPU {#the-jump-cpu}

[Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) tar ditt skepp till vilken koncernsektor som helst i din värld utan portal, för 500 Thulium per hopp, fientliga hemsektorer inräknade. Den leder aldrig till en farosektor, startar inte i strid, och du forskar fram den först i Skylabs forskningscentrum ([Forskning](/wiki/03-Mechanics/Research.md)). [Base CPU](/wiki/06-Items/Extras.md#base-cpus) tar dig hem på samma sätt.
