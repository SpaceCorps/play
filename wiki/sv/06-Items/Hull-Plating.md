<!-- wiki-i18n source: 2bd1925e336e25b6 -->
<!-- wiki-i18n title: Skrovpansar -->
# Skrovpansar {#hull-plating}

<!-- wiki-search: hull plate; hull plate slot; hull plate slots; plate slot; plate; armour; armor; hpl; skrovpansar; pansarplats; pansarplatta -->

Studien av Dormant-svärmen visade framsteg i pansarteknik. Med den tekniken kan skepp förbättra sitt skrov: **skrovpansar** är pansar som passar i en plats för skrovplattor på ett tillverkat skepp och ger det skrovpoäng. Det är inte Hull Plating **Booster** på sidan [Boosters](/wiki/06-Items/Boosters.md), som är en tidsbegränsad bonus.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Föremålsträd {#item-tree}

Det som Monteringen tillverkar kräver först sin teknologi; håll pekaren över ett föremål för att se hur lång tid forskningen tar. Teknologiträdet, bränslet och boosten: [Forskning](/wiki/03-Mechanics/Research.md).

```tree
Hull Plating I | hull-plating, uncommon | buy 5000 Thulium | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating II | hull-plating, rare | craft 2500 Thulium, 300 s | research 86400 s, 86400 science, 25 Dark Matter | 1 Hull Plating I, 150 Ship Fragment, 20 Reinforced Hull Plate, 6 Power Core, 5 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating III | hull-plating, epic | craft 4000 Thulium, 600 s | research 172800 s, 172800 science, 40 Dark Matter | 1 Hull Plating II, 300 Ship Fragment, 40 Reinforced Hull Plate, 12 Power Core, 1 Ancient Control Unit, 8 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings

Hull Plating I => Hull Plating II => Hull Plating III
```
<!-- item-tree:end -->

## De tre pansaren {#the-three-platings}

| Föremål | Skrov som läggs till | Varifrån det kommer |
| :--- | ---: | :--- |
| **Hull Plating I** | 5 000 | Butiken, 5 000 Thulium |
| **Hull Plating II** | 10 000 | Monteringen, från en Hull Plating I |
| **Hull Plating III** | 15 000 | Monteringen, från en Hull Plating II |

Hull Plating I köps. **II och III är uppgraderingar**: Monteringen förbrukar ett pansar från nivån under (löst i ditt inventarie) och kräver Thulium, material och **Dark Matter Plates**, 5 för II och 8 för III, medan sista nivån på varje annan utrustningsdel kräver 3. Var och en behöver först sin teknologi, i Hull Plating-trädet på sidan [Forskning](/wiki/03-Mechanics/Research.md#tree-hull-plating): 1 dag och 25 Dark Matter för II, 2 dagar och 40 för III, utöver teknologin för själva Dark Matter Plate. Trädet ovan visar priserna, materialen och tiderna.

[Smedjan](/wiki/06-Items/Forge.md) tar emot alla pansar, och en uppgradering behåller smidesnivån på pansaret den förbrukade och slumpar bonusen på nytt. Ett pansar har bara ett värde, skrovet, och rymmer därför en bonus, +2 % till +15 % efter nivå: en Hull Plating III på Evig nivå ger upp till 17 250. På [Auktionen](/wiki/03-Mechanics/Auction.md) kan Hull Plating II och III läggas ut, aldrig Hull Plating I, som butiken säljer.

## Pansarplatser {#hull-plate-slots}

Skrovpansar passar bara i **pansarplatser**, en egen sorts plats som de fyra skeppen du tillverkar i Monteringen har utöver sina platser för laser, generator, extrautrustning, förmåga och drönare:

| Skepp | Pansarplatser | En full uppsättning Hull Plating III ger |
| :--- | ---: | ---: |
| **Paragon** | 5 | 75 000 |
| **Storm** | 7 | 105 000 |
| **Ironclad** | 15 | 225 000 |
| **Wraith** | 9 | 135 000 |

- **Alla låsta från början.** En plats öppnas när du forskar fram den i Skylab: en teknologi för varje plats, 1 timme och 10 Dark Matter, i ordning från den första. Vyn [Forskning](/wiki/03-Mechanics/Research.md#ship-technologies) visar ett skepps platser som ett enda kort med en prick för varje.
- **En sorts skepp, inte ett enda skepp.** Platserna du har öppnat för Paragon är öppna också på varje Paragon-design ([Skeppsdesigner](/wiki/03-Mechanics/Ship-Designs.md)). En teknologi är din för alltid: wipen behåller den.
- **De två konfigurationerna delar dem.** Pansaren hör till skeppet: att byta konfiguration låter dem sitta kvar, och hangaren visar samma i båda.
- **Valfri blandning.** En plats tar vilket skrovpansar som helst, och två lika är inget problem.
- **Din andel skrov består.** Att montera eller ta av ett pansar behåller den andel skrov du har, så ett pansar läker dig aldrig och skadar dig aldrig.
- **Som all utrustning** monterar och tar du av pansar i hangaren, eller i dess fönster från en säker zon, aldrig ute i fält. En plats du inte har forskat fram nekar pansaret.

I hangaren visar kortet **Skrovpansar** platserna. I en öppen lägger du ett pansar genom att dra och släppa, som i vilken plats som helst; en låst visar ett lås, och ett klick öppnar Skylabs forskning. En ruta bredvid de andra värdena summerar vad de monterade pansaren ger.

## Så läggs skrovet ihop {#how-the-hull-adds-up}

Ett pansar lägger sitt skrov till skeppets eget, och hangaren och skeppsfönstret visar det större talet. Skeppets skrov plus dess pansar går sedan genom samma multiplikatorer som alltid: en [Hull Plating Booster](/wiki/06-Items/Boosters.md) och den [drönarformation](/wiki/03-Mechanics/Formations.md) du bär. En design som ändrar skrovet (BUCKY har 25 % mer) ändrar skeppets eget skrov, och pansaren kommer ovanpå.

## Hull Plating eller Hull Plating Booster? {#hull-plating-or-booster}

Två saker delar namn. **Skrovpansar** (den här sidan) är en rustning: en platta som sitter i en pansarplats på ett tillverkat skepp och lägger till sitt skrov så länge den är monterad. **Hull Plating Booster** är en tidsbegränsad bonus på sidan [Boosters](/wiki/06-Items/Boosters.md), +10 % maximala träffpoäng i 10 timmar på det skepp du flyger, och har inget att montera. De läggs ihop: pansaren kommer först, och boosterns 10 % tas på summan.
