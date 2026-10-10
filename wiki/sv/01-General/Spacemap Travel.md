<!-- wiki-i18n source: 129abc8d9ddf80be -->
<!-- wiki-i18n title: Spacemap-resor -->
# Spacemap-resor {#spacemap-travel}

Spacemap är ditt navigeringsgränssnitt för att ta dig fram i SpaceCorps-universum. Varje koncern kontrollerar en del av rymden, ordnad i en bestämd topologi som möjliggör både säker utforskning och farliga PvP-möten.

![Galaxy Gates](../../img/wiki-img/shots/gates.jpg)
![Sector DS-1 as the game draws it](../../img/wiki-img/shots/sector-DS-1.jpg)
![Sector DS-2 as the game draws it](../../img/wiki-img/shots/sector-DS-2.jpg)
![Sector DS-3 as the game draws it](../../img/wiki-img/shots/sector-DS-3.jpg)
![Sector DS-4 as the game draws it](../../img/wiki-img/shots/sector-DS-4.jpg)
![Sector G-1 as the game draws it](../../img/wiki-img/shots/sector-G-1.jpg)
![Sector G-2 as the game draws it](../../img/wiki-img/shots/sector-G-2.jpg)
![Sector G-3 as the game draws it](../../img/wiki-img/shots/sector-G-3.jpg)
![Sector G-4 as the game draws it](../../img/wiki-img/shots/sector-G-4.jpg)
![Sector M-1 as the game draws it](../../img/wiki-img/shots/sector-M-1.jpg)
![Sector M-2 as the game draws it](../../img/wiki-img/shots/sector-M-2.jpg)
![Sector M-3 as the game draws it](../../img/wiki-img/shots/sector-M-3.jpg)
![Sector M-4 as the game draws it](../../img/wiki-img/shots/sector-M-4.jpg)
![Sector T-1 as the game draws it](../../img/wiki-img/shots/sector-T-1.jpg)
![Sector T-2 as the game draws it](../../img/wiki-img/shots/sector-T-2.jpg)
![Sector T-3 as the game draws it](../../img/wiki-img/shots/sector-T-3.jpg)
![Sector T-4 as the game draws it](../../img/wiki-img/shots/sector-T-4.jpg)
![The Star System map: the sectors, the PvP sectors, the gates and the company routes, with the portal ring that joins each company's x-4 sector to the next company's x-3 sector](../../img/wiki-img/shots/star-system.jpg)

## Universums uppbyggnad {#the-universe-structure}

Universum består av tre huvudsektorer för koncernerna (Mars, Terra, Galactic) och en central PvP-zon.

- **x-1 (hembas)**: Startkartan för varje koncern (M-1, T-1, G-1). Den säkraste zonen.
- **x-2 -> x-3**: Expansionszoner med successivt tuffare utomjordingar.
- **x-4 (gräns)**: Porten till PvP-sektorn och till en annan koncerns `x-3` (Ringen, nedan).
- **DS-x (farosektorer)**: Den centrala PvP-zonen som förbinder alla koncerner: DS-1 till DS-4. Den rymmer en pulsar i var och en av DS-1 till DS-3 från säsongens första dag och, från säsongsdag 11, en jättegrävmaskin bredvid varje och Dormant Swamp ([Farosektorer](/wiki/01-General/Danger-Sectors.md)).

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
- **Ringen**: Varje koncerns gränskarta (`x-4`) har ytterligare en portal, till **nästa koncerns** `x-3`, och varje `x-3` har portalen tillbaka. De tre länkarna bildar en ring runt farosektorerna, så att varje koncern har en väg ut och en väg in:
  - `M-4` leder till Terras `T-3`
  - `T-4` leder till Galactics `G-3`
  - `G-4` leder till Mars `M-3`

  Ringen är öppen för alla piloter, oavsett vilken koncern de flyger för: den är ett andra sätt att resa mellan koncernernas kartor som inte korsar PvP-zonen. En ringportal står i ett eget hörn, långt från de andra portalerna på sin karta, med den vanliga säkra zonen på 660 enheter runt sig, och hoppet fungerar som vid vilken portal som helst. Var du kan bli anfallen på andra sidan beror på din värld, som överallt: i Alpha är `T-3` ingen PvP-sektor men `T-4` är det, i Beta är båda det, i Gamma är varje sektor det.
- **Invasionsvägar (resor mellan koncerner)**: Det finns två vägar genom portalerna in på en annan koncerns territorium. Den korta är Ringen: en pilot från Mars flyger från `M-4` genom ringportalen in i Terras `T-3` (tre hopp från Mars bas, `M-1` → `M-2` → `M-4` → `T-3`) och vidare till `T-4` eller `T-2`; Galactics `G-4` leder på samma sätt in i Mars `M-3` och Terras `T-4` in i Galactics `G-3`. Den långa korsar PvP-zonen: från `M-4` in i farosektorn `DS-1`, genom hoppportalen till `DS-2` och sedan in i Terras rymd genom `T-4`; för att nå Galactic tar du hoppportalen till `DS-3` och går in genom `G-4`.
- **Farosektortriangeln**: `DS-1`, `DS-2` och `DS-3` är alla förbundna med varandra. Var och en av dem har en koncerns portal (Mars i `DS-1`, Terra i `DS-2`, Galactic i `DS-3`); `DS-4` har ingen.
- **Kärnan i mitten**: Alla tre yttre farosektorer (`DS-1`, `DS-2` och `DS-3`) är direkt förbundna med mittkartan **`DS-4`**, den farligaste och mest givande PvP-zonen i universum. Ett **svart hål** hänger mitt i den: portalerna och lederna mellan dem ligger långt från det, men ett skepp som flyger in känner dess strålning, sedan dess dragning, och förstörs vid dess händelsehorisont. Se [Det svarta hålet](/wiki/03-Mechanics/Black-Hole.md). Från säsongsdag 11 rymmer det övre vänstra hörnet av `DS-4` [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md), vars kanoner skjuter på varje skepp de ser.

### Jump CPU {#the-jump-cpu}

[Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) tar ditt skepp till vilken koncernsektor som helst i din värld utan portal, för 500 Thulium per hopp, fientliga hemsektorer inräknade. Den leder aldrig till en farosektor, startar inte i strid, och du forskar fram den först i Skylabs forskningscentrum ([Forskning](/wiki/03-Mechanics/Research.md)). [Base CPU](/wiki/06-Items/Extras.md#base-cpus) tar dig hem på samma sätt. En warp-CPU, alltså Jump CPU eller en Base CPU, nekas medan du bär på ett uppdragsföremål (”Du kan inte använda en warp-CPU medan du bär på ett uppdragsföremål.”): flyg hem genom portarna ([Uppdragsföremål](/wiki/03-Mechanics/Quests.md#quest-items)).
