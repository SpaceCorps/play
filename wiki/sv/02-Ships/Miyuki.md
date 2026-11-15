<!-- wiki-i18n source: 4734fe19223e935e -->
<!-- wiki-i18n title: Miyuki -->
# Miyuki

Miyuki är ett stödskepp i fem nivåer. Du tillverkar nivå I i Monteringen som vilket skepp som helst och bygger sedan om samma skepp på plats till nivå II, III, IV och V: varje nivå görs av nivån under, och allt som sitter på skeppet blir kvar. Varje nivå ger en laserplats och en pansarplats till, och var och en av de platserna är en teknologi du forskar fram.

## Värden {#stats}

- **Träffpoäng (HP)**: 128 000
- **Grundhastighet**: 270
- **Laserplatser**: 5
- **Extraplatser**: 3
- **Pansarplatser**: 5

### Generator- och stödplatser {#generator-support-slots}

- **Kärnplatser (100 % verkningsgrad)**: 3
- **Stödplatser (75 % verkningsgrad)**: 3
- **Hjälpplatser (50 % verkningsgrad)**: 2

---

## Pris {#price}

- **Krediter**: 0 (Byggs i Monteringen)
- **Thulium**: 0

## Nivåer {#levels}

Värdena ovan gäller nivå I. En nivå över den första tillverkas i Monteringen av Miyuki på nivån under: samma skepp, ombyggt på plats, så dess utrustning och konfigurationer finns kvar. En nivå går inte att hoppa över eller köpa.

| Nivå | Skrov | Grundhastighet | Lasrar | Pansar | Kärna / stöd / hjälp | Sköldkapacitet | Sköldabsorption |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Miyuki** | 128 000 | 270 | 5 | 5 | 3 / 3 / 2 | – | – |
| **Miyuki II** | 134 400 | 270 | 6 | 6 | 3 / 3 / 2 | +5 % | +2 % |
| **Miyuki III** | 141 120 | 270 | 7 | 7 | 3 / 3 / 2 | +10,25 % | +4,04 % |
| **Miyuki IV** | 148 176 | 320 | 8 | 8 | 3 / 3 / 2 | +15,76 % | +6,12 % |
| **Miyuki V** | 155 585 | 320 | 9 | 9 | 4 / 4 / 4 | +21,55 % | +8,24 % |

Sköldkapacitet och sköldabsorption är bonusar över nivå I.

Vad en nivå kräver i Monteringen, förutom Miyuki på nivån under, som byggs om till den nya nivån:

| Nivå | Forskning | Tillverkningstid | Thulium | Material |
| :--- | :--- | ---: | ---: | :--- |
| **Miyuki** | 1 d, 10 Dark Matter | 15 min | 6 000 | 160 Ship Fragment, 25 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit |
| **Miyuki II** | 1 d, 10 Dark Matter | 10 min | 20 000 | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 8 Dark Matter Plate |
| **Miyuki III** | 1 d, 10 Dark Matter | 10 min | 35 000 | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 1 Ancient Control Unit, 8 Dark Matter Plate |
| **Miyuki IV** | 2 d, 10 Dark Matter | 15 min | 50 000 | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 2 Ancient Control Unit, 8 Dark Matter Plate |
| **Miyuki V** | 2 d, 10 Dark Matter | 15 min | 75 000 | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 3 Ancient Control Unit, 8 Dark Matter Plate |

## Förmågor {#abilities}

Miyukis förmågor hör till skeppet, inte till en sak: de tar ingen förmågeplats och kräver inget monterat. [Skeppsförmågor](/wiki/03-Mechanics/Abilities.md#ship-abilities) förklarar hur var och en fungerar; den här tabellen visar vad varje nivå har.

| Nivå | Heal Pod | Channel Heal | Channel Shield |
| :--- | :--- | :--- | :--- |
| **Miyuki** | 7,5 s, 20 000 + 2 % | – | – |
| **Miyuki II** | 7,5 s, 20 000 + 2 % | 50 000 skrov i sekunden (du 10 000), 120 s | – |
| **Miyuki III** | 7,5 s, 30 000 + 3 % | 50 000 skrov i sekunden (du 10 000), 120 s | 75 000 sköld i sekunden (du 15 000), 120 s |
| **Miyuki IV** | 7,5 s, 30 000 + 3 % | 75 000 skrov i sekunden (du 10 000), 100 s | 75 000 sköld i sekunden (du 15 000), 120 s |
| **Miyuki V** | 7,5 s, 30 000 + 3 % | 75 000 skrov i sekunden (du 10 000), 100 s | 75 000 sköld i sekunden (du 15 000), 120 s |

En länk varar i 5 sekunder och når ett skepp i din grupp eller koncern inom 1 200 enheter. Heal Pod når 600.

## Forskning {#research}

- **Nivåer.** Miyuki II till V är egna teknologier i Skylab, var och en bakom nivån under: 1 d för II och III, 2 d för IV och V, och 10 Dark Matter vardera.
- **Platser.** Pansarplatserna, laserplatserna från den sjätte och generatorplatserna från den nionde är egna teknologier i Skylab, på 1 h och 10 Dark Matter vardera: pansarplats 1 till 9 i ordning från den första, laserplats 6 till 9 (var och en bakom sin nivå) och generatorplats 9 till 12 (var och en bakom nivå V). En plats öppnas på skeppet, på vilken nivå det än är, så fort du har forskat fram den; en plats du inte har forskat fram visas låst i Hangaren.
- **Pansarplatser.** Miyuki har 5 [pansarplatser](/wiki/06-Items/Hull-Plating.md#hull-plate-slots) för [skrovpansar](/wiki/06-Items/Hull-Plating.md) på nivå I och 9 på nivå V, alla låsta när du tillverkar det. Alla 9 fyllda med Hull Plating III ger 225 000 skrov.

<!-- research-ship:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **Forska först.** Monteringen tillverkar det här skeppet först när du har forskat fram dess teknologi: 1 d forskning och 10 Dark Matter som ska sättas i forskningscentrumet. Den finns i [trädet Skepp](/wiki/03-Mechanics/Research.md#tree-ships) på sidan [Forskning](/wiki/03-Mechanics/Research.md).
- **Fler extraplatser.** Extra Slots CPU I, II och III, installerade i din Skylab, ger det här skeppet 3, 5 och 7 extraplatser till: 6, 8 och 10 sammanlagt med de 3 det redan har. Du forskar fram och tillverkar dem som vilket annat föremål som helst: se [Extra Slots CPUs](/wiki/06-Items/Extras.md#extra-slots-cpus).

<!-- research-ship:end -->

## Bakgrund {#lore}

Miyuki föddes på Skylabs varv ur en fråga: tänk om skeppet som håller en flotta vid liv kunde växa med piloten som flyger det? Varje ombyggnad behåller utrustningen och konfigurationerna och ger lite mer av allt. En Miyuki V är skeppet som piloten sköt upp första dagen, uppvuxet till ett flaggskepps storlek.
