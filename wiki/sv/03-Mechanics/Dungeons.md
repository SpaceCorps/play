<!-- wiki-i18n source: a3ead40fe6402d78 -->
<!-- wiki-i18n title: Dungeons -->
# Dungeons

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; port; portar; krigsherre; labyrint; steg; bytezon; kort -->

En **dungeon** kallas **port** i spelet: en sluten labyrint med en **krigsherre** i änden. En vice ledare eller ledaren i en [klan](/wiki/03-Mechanics/Clans.md) öppnar en och betalar för den ur klanbanken, och klanens medlemmar flyger in tillsammans som en [grupp](/wiki/03-Mechanics/Groups.md). De kämpar sig igenom labyrintens utomjordingar, öppnar bytezoner för att välja ett kort i var och en och fäller krigsherren. Varje pilot som deltog i striden får betalt när krigsherren faller, inom gränserna längre ner. Portarna finns på fliken **Portar** på klansidan.

En port är en strid enbart mot utomjordingarna: ingen kan attackera en klankamrat eller någon annan därinne. Utomjordingarna betalar ingenting. Betalningen kommer enbart från krigsherren, så det enda sättet att få betalt är att vara med i striden när den faller.

## I korthet {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Öppnar**: Från säsongsdag 4
- **Vem som öppnar en port**: En vice ledare eller ledaren, som betalar priset ur klanbanken
- **Grupp**: 4 till 10 medlemmar av klanen, i en grupp
- **Portar per dag**: 3 per klan och UTC-dag, en öppen åt gången
- **Portar samtidigt**: 6 i en värld
- **Kartor**: Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Labyrinter**: 8; en väljs när en port öppnas
- **Samling**: 10 min att samlas och starta. En port som ingen startar stängs, och dess pris går tillbaka till klanbanken
- **Tidsgräns**: Steg 1: 80 min, Steg 2: 110 min, Steg 3: 150 min från starten. När tiden tar slut misslyckas porten och betalar ingenting
- **Lämnad tom**: En port där ingen är inne på 3 min misslyckas
- **När krigsherren faller**: Porten förblir öppen i 2 min för piloterna som är inne
- **Komma tillbaka**: En pilot som har lämnat porten eller blivit förstörd kan flyga in igen 3 gånger, med 20 s emellan

<!-- dungeons-glance:end -->

## Hur en omgång går till {#how-a-run-goes}

1. **Kalla fram.** På fliken Portar väljer en [vice ledare eller ledaren](/wiki/03-Mechanics/Clans.md#hierarchy-roles) ett steg och trycker på **Kalla fram**. Priset tas ur [klanbanken](/wiki/03-Mechanics/Clans.md#clan-economy-taxation), och porten får en av kartorna som listas ovan. En port som ingen startar stängs, och priset går tillbaka till banken.
2. **Gå in.** Klanens medlemmar trycker på **Gå in** i klanfönstret medan de flyger. Piloterna därinne är portens grupp.
3. **Starta.** Piloten som öppnade porten, eller en officer, trycker på **Starta** när tillräckligt många piloter är inne. Efter det kan bara piloter som redan var inne komma tillbaka.
4. **Kämpa dig genom labyrinten.** Du kommer in i ena änden av labyrinten och krigsherren väntar i den andra. Utomjordingarna sover i sina rum och vaknar i flockar när gruppen närmar sig.
5. **Öppna bytezonerna.** Ringar i labyrinten markerar zonerna. Håll en och gruppen röstar om ett kort, som betalas ut tillsammans med krigsherrens betalning.
6. **Besegra krigsherren.** Bryt hans sköld och skrov och svara på hans förmågor. När han faller är porten avklarad.
7. **Få betalt.** Betalningen kommer i samma ögonblick som krigsherren faller. Porten står öppen en stund till för piloterna därinne och stängs sedan.

## Gå in {#entering}

För att gå in i en port behöver du ett **skepp i flykt**, så starta först och öppna sedan klanfönstret, och en [grupp](/wiki/03-Mechanics/Groups.md) med tillräckligt många klanmedlemmar. Du behöver också den **nivå** som steget kräver, och du får inte redan vara inne i en annan port. Portens grupp har en storleksgräns: när den är full kan ingen annan gå in.

En vice ledare eller ledaren öppnar en port, en i taget för klanen, och bara upp till antalet portar per dag. Klanbanken måste ha priset. En klan kan öppna ett steg först när den har klarat steget före.

Inne i en port kan du inte byta värld, och Jump CPU och Base CPU fungerar inte. Knappen **Lämna** i portens fält tar ut dig efter att du bekräftat. En pilot som har lämnat, eller blivit förstörd, kan flyga in igen några gånger, med en kort väntan emellan.

## Stegen {#the-stages}

En port har ett steg, och steget är dess svårighetsgrad. Ett högre steg har segare utomjordingar som slår hårdare, och det betalar mer. Multiplikatorerna i tabellen gäller varje utomjording och krigsherren. Skada betyder lasrar, raketer och krigsherrens förmågor. Tabellen visar också hur många utomjordingar ett steg skickar jämfört med det första. **Priset** tas ur klanbanken när porten öppnas.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Steg | Kräver | Utomjordingarnas skrov och sköld | Antal utomjordingar | Utomjordingarnas skada | Portens pris (krediter, ur klanbanken) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Steg 1** | Från nivå 6 | ×1 | ×1 | ×1 | 500 000 |
| **Steg 2** | Från nivå 7 | ×1,5 | ×1 | ×1,25 | 1 000 000 |
| **Steg 3** | Från nivå 8 | ×2,5 | ×1 | ×1,5 | 2 000 000 |

<!-- dungeons-stages:end -->

## Labyrinten {#the-maze}

Varje port är en sluten labyrint på en egen karta, en av kartorna i listan ovan, och labyrinten är en av flera utformningar. En labyrint är ett rutnät av rum och korridorer med massiva väggar. Skepp kan inte ta sig genom en vägg, och en vägg stoppar skott, så den fungerar som skydd. En meteor faller ovanifrån, och en vägg stoppar den inte.

## Utomjordingarna {#the-aliens}

Fyra sorters utomjordingar vaktar labyrinten. De sover i sina rum och vaknar när en pilot kommer nära. Porten håller bara ett visst antal utomjordingar i luften samtidigt, och det antalet växer med gruppens storlek, så en flock du förstör släpper in nästa. En större grupp möter fler utomjordingar i proportion, en mindre färre, och en sorts utomjording blir aldrig färre än en.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Utomjordingar, för en grupp på 5 | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| Gate Goombah | 130 | 130 | 130 |
| Gate Pirate | 28 | 28 | 28 |
| Gate Crystalys | 28 | 28 | 28 |
| Gate Crystalys Twin | 9 | 9 | 9 |
| Tillsammans | 195 | 195 | 195 |
| Vågen i en bytezon | 10 × Gate Goombah och 1 × Gate Crystalys | 10 × Gate Goombah och 1 × Gate Crystalys | 10 × Gate Goombah och 1 × Gate Crystalys |

- **Levande samtidigt**: Högst 10 per pilot i gruppen, och 70 totalt

<!-- dungeons-population:end -->

Varje sort i tur och ordning. Skrov och sköld är de vanliga värdena gånger multiplikatorn för steget i kolumnen.

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Gate Goombah

- **Ser ut som**: Goombah
- **Flyger i flockar om**: 6

|  | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| Skrov | 32 000 | 48 000 | 80 000 |
| Sköld | 48 000 | 72 000 | 120 000 |
| Laserskada (en salva per sekund) | 3 000 | 3 750 | 4 500 |
| Hastighet | 180 | 180 | 180 |
| Laserräckvidd | 800 | 800 | 800 |
| Aggroradie | 1 800 | 1 800 | 1 800 |

### Gate Pirate

- **Ser ut som**: Pirate Boss
- **Flyger i flockar om**: 2
- **Raket**: En rak raket var 5 s, räckvidd 970 enheter

|  | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| Skrov | 300 000 | 450 000 | 750 000 |
| Sköld | 50 100 | 75 150 | 125 250 |
| Laserskada (en salva per sekund) | 200 | 250 | 300 |
| Raketskada | 5 000 | 6 250 | 7 500 |
| Hastighet | 92 | 92 | 92 |
| Laserräckvidd | 700 | 700 | 700 |
| Aggroradie | 1 800 | 1 800 | 1 800 |

### Gate Crystalys

- **Ser ut som**: Crystalys
- **Flyger i flockar om**: 2

|  | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| Skrov | 256 000 | 384 000 | 640 000 |
| Sköld | 160 000 | 240 000 | 400 000 |
| Laserskada (en salva per sekund) | 10 000 | 12 500 | 15 000 |
| Hastighet | 230 | 230 | 230 |
| Laserräckvidd | 900 | 900 | 900 |
| Aggroradie | 2 400 | 2 400 | 2 400 |

### Gate Crystalys Twin

- **Ser ut som**: Crystalys, 1,4 gånger så stor
- **Flyger i flockar om**: 1

|  | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| Skrov | 512 000 | 768 000 | 1 280 000 |
| Sköld | 320 000 | 480 000 | 800 000 |
| Laserskada (en salva per sekund) | 20 000 | 25 000 | 30 000 |
| Hastighet | 230 | 230 | 230 |
| Laserräckvidd | 900 | 900 | 900 |
| Aggroradie | 2 400 | 2 400 | 2 400 |

<!-- dungeons-enemies:end -->

## Krigsherren {#the-warlord}

Krigsherren väntar i rummet längst bort i labyrinten, och han är det enda i en port som betalar. Han är en Crystalys som vuxit enorm. Hans skrov och sköld växer med gruppens storlek: ju fler piloter som går in, desto segare är han, i proportion. Han stannar i sitt rum och använder sina förmågor en i taget, i slumpmässig ordning, var och en med sin egen återhämtningstid.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Ser ut som**: Crystalys, 3 gånger så stor
- **Sköldladdning**: 3 000 per sekund, efter 15 s utan skada

|  | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| Skrov | 10 000 000 | 15 000 000 | 25 000 000 |
| Sköld | 8 000 000 | 12 000 000 | 20 000 000 |
| Laserskada (en salva per sekund) | 8 000 | 10 000 | 12 000 |
| Hastighet | 120 | 120 | 120 |
| Laserräckvidd | 1 100 | 1 100 | 1 100 |

Skrovet och skölden ovan gäller för en grupp på 5. De växer med gruppen: det är krigsherrens skrov och sköld tillsammans, efter antalet piloter i gruppen när porten startar.

| Piloter i gruppen | Steg 1 | Steg 2 | Steg 3 |
| :--- | ---: | ---: | ---: |
| 4 | 14 400 000 | 21 600 000 | 36 000 000 |
| 5 | 18 000 000 | 27 000 000 | 45 000 000 |
| 6 | 21 600 000 | 32 400 000 | 54 000 000 |
| 7 | 25 200 000 | 37 800 000 | 63 000 000 |
| 8 | 28 800 000 | 43 200 000 | 72 000 000 |
| 9 | 32 400 000 | 48 600 000 | 81 000 000 |
| 10 | 36 000 000 | 54 000 000 | 90 000 000 |

<!-- dungeons-boss:end -->

### Hans förmågor {#its-abilities}

- **Den röda ringen** för Livsstjälande aura skadar varje pilot i den och läker krigsherren med skadan. Sköldabsorptionen har också en röd ring: den dränerar sköldarna på piloterna därinne och laddar krigsherrens. I båda fallen ska du lämna ringen eller ställa dig bakom en vägg.
- **De bärnstensfärgade ringarna** för Meteorregn visar var meteorerna slår ner ett ögonblick senare. Fortsätt röra dig och lämna ringen innan den slår ner.
- **Fokus på läkare** vänder krigsherren mot den som läker en annan pilot, och han slår den piloten hårdare. Sprid ut läkningen.
- **Raketsalvan** skickar målsökande raketer mot slumpmässiga piloter. En EMP Charge eller kamouflage skakar av dem.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Förmåga | Förberedelse | Varar | Återhämtning | Ringens radie (enheter) | Krigsherren återfår högst |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Livsstjälande aura** | 2 s | 15 s | 2 min | 900 | 8 % av skrov och sköld |
| **Meteorregn** | 1,5 s | 3 salvor, 4 s emellan | 2 min | 420 | – |
| **Fokus på läkare** | 1 s | 45 s | 2 min | – | – |
| **Raketsalva** | 1,5 s | 45 s | 2 min | – | – |
| **Sköldabsorption** | 2 s | 15 s | 2 min | 900 | 6 % av skölden |

| Förmåga | Steg 1 | Steg 2 | Steg 3 |
| :--- | :--- | :--- | :--- |
| **Livsstjälande aura** | 8 000 per sekund | 10 000 per sekund | 12 000 per sekund |
| **Meteorregn** | 6 meteorer per salva, 40 000 vardera | 8 meteorer per salva, 50 000 vardera | 10 meteorer per salva, 60 000 vardera |
| **Fokus på läkare** | Dess laser träffer ×1,5 så hårt mot piloten den vänder sig mot | Dess laser träffer ×1,5 så hårt mot piloten den vänder sig mot | Dess laser träffer ×1,5 så hårt mot piloten den vänder sig mot |
| **Raketsalva** | 6 500 per raket, en var 15 s | 8 125 per raket, en var 15 s | 9 750 per raket, en var 15 s |
| **Sköldabsorption** | 10 000 sköld per sekund | 12 500 sköld per sekund | 15 000 sköld per sekund |

<!-- dungeons-abilities:end -->

## Bytezoner {#loot-zones}

En ring på labyrintens golv markerar varje bytezon så fort gruppen har hittat den. Stå kvar en stund inne i den så vaknar zonen, och en våg utomjordingar kommer mot den. Sedan måste gruppen **hålla** zonen: ha en pilot kvar inne tills mätaren är full. Utomjordingar i ringen stoppar mätaren, och den går tillbaka medan ingen är därinne, så rensa vågen först. När zonen öppnas ser gruppen tre olika kort och **röstar** om ett. En zon öppnas bara en gång, och dess våg kommer inte tillbaka.

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Bytezoner**: 4 i varje labyrint
- **Radie**: 450 enheter
- **Väckning**: Stå inne i ringen i 2 s
- **Hålla**: Håll en pilot inne i 30 s. Mätaren stannar medan 3 eller fler utomjordingar är i ringen och går tillbaka medan ingen är inne
- **Välja**: Gruppen har 45 s på sig att rösta. Omröstningen slutar tidigare om varje närvarande pilot har röstat eller ett kort har mer än hälften av rösterna

<!-- dungeons-zones:end -->

### Korten {#the-cards}

Korten dras ett i taget ur poolen nedan. Chansen är ett korts chans i en dragning. Ett kort med många exemplar går till varje pilot som får betalt, och ett utrustningskort, med ett exemplar, går till en pilot i gruppen. En pilot som inte får betalt får inte heller något kort, och en zon som öppnats i en port som misslyckas betalar ingenting.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Kort | Steg 1 | Steg 2 | Steg 3 | Chans | Går till |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2 000 | 3 000 | 5 000 | 21 % | Varje betald pilot |
| Velkonite Reinforced Plate | 10 | 15 | 25 | 12 % | Varje betald pilot |
| Orvium Reinforced Plate | 10 | 15 | 25 | 12 % | Varje betald pilot |
| Velkonite | 200 | 300 | 500 | 12 % | Varje betald pilot |
| Orvium | 200 | 300 | 500 | 12 % | Varje betald pilot |
| Ultra Core | 5 000 | 7 500 | 12 500 | 10 % | Varje betald pilot |
| Experimental Fusion Core | 3 000 | 4 500 | 7 500 | 8 % | Varje betald pilot |
| Dark Matter | 5 | 8 | 12 | 8 % | Varje betald pilot |
| Dark Matter Plate | 1 | 1 | 2 | 4 % | Varje betald pilot |
| Engine III | 1 | 1 | 1 | 0,25 % | En pilot i gruppen |
| Heavy Shield Core | 1 | 1 | 1 | 0,25 % | En pilot i gruppen |
| Adaptive Core III | 1 | 1 | 1 | 0,25 % | En pilot i gruppen |
| Starfire-III | 1 | 1 | 1 | 0,25 % | En pilot i gruppen |

- **Utrustning**: Korten med ett enda exemplar är utrustning: tillsammans 1 % av korten

<!-- dungeons-cards:end -->

## Betalning {#pay}

När krigsherren faller får varje pilot som förtjänat det betalt, en gång per genomförd omgång. Korten som gruppen valde kommer ovanpå stegets betalning. Det finns ingen världsmultiplikator: betalningen är densamma i varje värld.

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Steg | Heder | Erfarenhet | Krediter | Thulium | x4-ammunition | PvE-rankingpoäng |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| **Steg 1** | 25 000 | 600 000 | 5 000 000 | 4 000 | 4 000 | 600 |
| **Steg 2** | 50 000 | 1 500 000 | 10 000 000 | 9 000 | 9 000 | 1 500 |
| **Steg 3** | 100 000 | 2 400 000 | 17 500 000 | 15 000 | 15 000 | 2 400 |

<!-- dungeons-pay:end -->

### Vem som får betalt {#who-is-paid}

Utomjordingarna betalar aldrig. En omgång spelas klart även när den inte betalar något, och resultatskärmen säger varför. Inträde nekas aldrig för att du redan fått betalt för ett steg: den omgången betalar bara ingenting.

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **En dag**: Ett steg betalar en pilot en gång per UTC-dag: den dag då krigsherren faller
- **En vecka**: En pilot får betalt för högst 10 avklarade steg per UTC-vecka, måndag till söndag
- **Inne**: Minst 2 min totalt
- **Del i striden**: Minst ett av dessa: orsakat 2 % av krigsherrens skrov och sköld; förstört 10 av portens utomjordingar; läkt andra piloter för 50 000 under striden mot krigsherren

<!-- dungeons-rules:end -->

### Vad en dag och en vecka är värda {#what-a-day-and-a-week-are-worth}

Vad en pilot kan få betalt på en dag, och under den bästa vecka som gränserna tillåter. Sista kolumnen är vad betalningen lägger till dina [PvE-poäng](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points).

<!-- dungeons-totals:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Betalning per pilot | Heder | Erfarenhet | Krediter | Thulium | x4-ammunition | PvE-rankingpoäng |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| En dag, varje steg en gång | 175 000 | 4 500 000 | 32 500 000 | 28 000 | 28 000 | 4 500 |
| Den bästa veckan: 7 × Steg 3 och 3 × Steg 2 | 850 000 | 21 300 000 | 152 500 000 | 132 000 | 132 000 | 21 300 |

Erfarenheten från ett betalt, avklarat steg räknas med i dina PvE-rankingpoäng: en poäng för varje 1 000 erfarenhet.

<!-- dungeons-totals:end -->

## Klanbankens belöning {#clan-bank-reward}

Klanbanken får också betalt, i krediter och inte i Thulium, första gången klanen klarar ett steg under en säsong. Klanen måste vara gammal nog, och tillräckligt många piloter i den omgången måste få betalt. Banken får betalt en gång per steg under en säsong.

<!-- dungeons-clan:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Steg | Krediter till klanbanken |
| :--- | ---: |
| **Steg 1** | 10 000 000 |
| **Steg 2** | 20 000 000 |
| **Steg 3** | 30 000 000 |

- **Klanens ålder**: Minst 3 d
- **Betalda piloter**: Minst 3 i porten

<!-- dungeons-clan:end -->

## Tips

- Rensa en zons våg innan du försöker hålla zonen, och strid inne i ringen om utomjordingar kommer in.
- Använd väggarna: lasrar går inte igenom dem, och krigsherrens ringar slutar vid dem.
- Spara en EMP Charge till Raketsalvan.
- Håll koll på klockan i portens fält. När tiden tar slut misslyckas porten och betalar ingenting.
