<!-- wiki-i18n source: 615b51aa98d6a27d -->
<!-- wiki-i18n title: Raketer -->
# Raketer {#rockets}

Raketer är ett andra vapen vid sidan av dina lasrar: ett skott var några sekunder som träffar mycket hårdare än en lasersalva. Tolv raketer i fyra typer, tre nivåer vardera, ytterligare två som bara Monteringen tillverkar, och **en omladdningstimer på 5 sekunder som alla delar**, vilken du än avfyrar. De vanliga och sällsynta raketerna köps med **krediter**; de fyra episka raketerna köps med **Thulium**. En [drönarformation](/wiki/03-Mechanics/Formations.md) kan höja en raket skada och göra den timern längre eller kortare: se [Drönarformationer och raketer](#drone-formations-and-rockets).

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Föremålsträd {#item-tree}

Det som Monteringen tillverkar kräver först sin teknologi; håll pekaren över ett föremål för att se hur lång tid forskningen tar. Teknologiträdet, bränslet och boosten: [Forskning](/wiki/03-Mechanics/Research.md).

```tree
Lancet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets

Lancet I -> Lancet II -> Lancet III
Rivet I -> Rivet II -> Rivet III
Ember I -> Ember II -> Ember III
Scatter I -> Scatter II -> Scatter III => N.U.K.E.
```
<!-- item-tree:end -->

## De fyra typerna {#the-four-kinds}

| | Enkelmål: träffar ett skepp | Områdesskada: exploderar och skadar allt i närheten |
| :--- | :--- | :--- |
| **Målsökande**: låser på det mål du valt och följer det | Lancet I, Lancet II, Lancet III | Ember I, Ember II, Ember III |
| **Rak**: flyger mot din markör | Rivet I, Rivet II, Rivet III | Scatter I, Scatter II, Scatter III |

Varje typ är en **familj** som har namn efter sin vanliga raket, och nivån är en romersk siffra: **Lancet I**, **Lancet II** och **Lancet III** är den vanliga, den sällsynta och den episka målsökande enkelmålsraketen, och familjerna Rivet, Ember och Scatter följer samma mönster. En raketkod på brickan i raketväljaren och i hangaren är familjens tre bokstäver och siffran (LNC II, RVT III, EMB I, SCT II); de två raketer som bara Monteringen tillverkar behåller namn och kod (N.U.K.E., NUK; N.I.K.E., NIK).

- **Målsökande** raketer kräver ett valt mål inom sin **låsräckvidd** när de avfyras. De styr efter det med begränsad svängtakt, så ett snabbt skepp långt borta kan köra ifrån en billig raket. Om målet förstörs, lämnar området eller når en säker zon fortsätter raketen rakt fram och väljer inget nytt.
- **Raka** raketer behöver inget mål och ignorerar det du har valt: de flyger alltid mot din **markör**, mot punkten under den i flygvyn. **Klicka på platsen för en rak raket för att armera den** (platsen får en vit ram och ett hårkors, och din muspekare blir ett hårkors över rymden), sedan **klicka i rymden**: raketen flyger mot punkten du klickade på och ditt skepp stannar där det är. Esc, ett högerklick eller samma plats igen släpper den. Om raketerna fortfarande laddas om säger klicket bara det, och raketen förblir armerad. Siffertangenterna och **Avfyra raket** skjuter direkt mot den sista punkt markören hade i flygvyn; innan markören har varit där flyger de dit ditt skepp **pekar**. De flyger rakt, så ett skepp som korsar i fart kan väja undan dem.
- En raket med **enkelmål** träffar det första skepp den får träffa (en målsökande bara sitt mål). En raket med **områdesskada** exploderar bredvid det första skepp den möter, vid den punkt du siktade på, eller där dess flykt tar slut, och skadar varje skepp inom sin **explosionsradie**: full skada i mitten, mindre mot kanten. Ringen som explosionen ritar på kartan är dess exakta räckvidd.

## De tolv raketerna {#the-twelve-rockets}

Varje raket har **sin egen skada, som slumpas fram när du avfyrar den**: mellan **80 % och 100 %** av dess högsta tal, och tabellen visar den lägsta och den högsta. Den beror inte på ditt skepp, dina lasrar, dina Damage Amps, dina boosters, din ammunition eller dina drönare, och en raket ger aldrig kritiska träffar. Bara en **drönarformation** ändrar den: tabellen här anger skadan utan formation (se [Drönarformationer och raketer](#drone-formations-and-rockets)). En raket med enkelmål gör den framslumpade skadan på det skepp den träffar; en explosion slumpar en gång och gör den på **varje skepp inom den**, hela talet i mitten och mindre mot kanten. *Sköldgenomträngning* dras av från målets absorption för den träffen (ett skepps absorption är den andel av en träff som dess sköldar tar, se [Sköldmekanik](/wiki/03-Mechanics/Shields.md#shield-penetration)): en Lancet III:s 35 % lämnar sköldarna på ett skepp med 80 % 45 % av träffen och skickar de övriga 55 % till skrovet. En explosion har ingen.

| Namn | Typ | Sällsynthet | Skada | Sköldgenomträngning | Explosionsradie | Låsräckvidd | Räckvidd | Fart | Pris | Högst så många kan du bära |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **Lancet I** | Målsökande, enkelmål | Vanlig | 1 600–2 000 | 10 % | – | 700 | 1 040 | 520 | 500 krediter | 5 000 |
| **Lancet II** | Målsökande, enkelmål | Sällsynt | 3 200–4 000 | 25 % | – | 1 000 | 1 584 | 660 | 800 krediter | 2 000 |
| **Lancet III** | Målsökande, enkelmål | Episk | 4 800–6 000 | 35 % | – | 1 300 | 2 296 | 820 | 5 Thulium | 500 |
| **Rivet I** | Rak, enkelmål | Vanlig | 2 000–2 500 | 5 % | – | – | 1 080 | 900 | 500 krediter | 5 000 |
| **Rivet II** | Rak, enkelmål | Sällsynt | 4 000–5 000 | 25 % | – | – | 1 120 | 700 | 800 krediter | 2 000 |
| **Rivet III** | Rak, enkelmål | Episk | 6 000–7 500 | 35 % | – | – | 1 100 | 500 | 5 Thulium | 500 |
| **Ember I** | Målsökande, områdesskada | Vanlig | 1 120–1 400 | – | 170 | 700 | 1 000 | 500 | 500 krediter | 5 000 |
| **Ember II** | Målsökande, områdesskada | Sällsynt | 2 240–2 800 | – | 230 | 920 | 1 500 | 600 | 800 krediter | 2 000 |
| **Ember III** | Målsökande, områdesskada | Episk | 3 360–4 200 | – | 300 | 1 150 | 2 030 | 700 | 5 Thulium | 500 |
| **Scatter I** | Rak, områdesskada | Vanlig | 1 400–1 750 | – | 210 | – | 1 088 | 640 | 500 krediter | 5 000 |
| **Scatter II** | Rak, områdesskada | Sällsynt | 2 800–3 500 | – | 290 | – | 1 080 | 540 | 800 krediter | 2 000 |
| **Scatter III** | Rak, områdesskada | Episk | 4 200–5 250 | – | 400 | – | 1 092 | 420 | 5 Thulium | 500 |

Ju dyrare nivån är, desto hårdare träffar en raket, desto längre når den, desto mer sköldgenomträngning har den och desto färre kan du bära; de dyra ger också mest skada för pengarna. En rak raket gör **25 % mer** än den målsökande raketen av samma nivå och samma slag för samma pris, eftersom du måste sikta den. En explosion gör 70 % av vad raketen med enkelmål i dess nivå gör, på varje skepp den täcker. Skadan i en explosion är störst i mitten; den faller till 25 till 35 % vid kanten. Ett skott gör i genomsnitt 90 % av sitt högsta tal, och tabellen längre ner som räknar raketer utgår från det.

## Vad de kostar {#what-they-cost}

En vanlig raket kostar 500 krediter, en sällsynt 800 krediter och en episk 5 Thulium, i varje typ. Avfyrad så fort timern tillåter blir det 6 000 krediter i minuten för en vanlig raket, 9 600 för en sällsynt och 60 Thulium för en episk, mot de 1 800 krediter i minuten som en Ostirions tre lasrar förbrukar på x1. En full hög är 5 000 vanliga raketer (2 500 000 krediter), 2 000 sällsynta (1 600 000 krediter) eller 500 episka (2 500 Thulium): du köper så många du vill upp till det, och *högst så många kan du bära* för en raket är den enda gränsen för hur många du håller. Raketer väger ingenting: de tar inget utrymme i transportförrådet. En raket var 5:e sekund är bara tolv i minuten, så en raket är ett extra kraftslag ovanpå dina lasrar: de billiga till de svaga utomjordingarna, de dyra till de stora striderna.

Butiken listar raketerna en typ i taget, var och en under sitt namn, med den vanliga raketen först och den episka sist; hangaren, transportförrådet och väljaren Raketer använder samma ordning.

## Mot utomjordingarna {#against-the-aliens}

Så många raketer krävs för att skjuta ner en utomjording, en raketsort i taget (Alpha; utomjordingar i Beta och Gamma är 1,5 respektive 2 gånger så starka). En explosion räknas som det skepp den briserar bredvid tar emot den, en bit från mitten. En utomjordings sköld tar 80 % av en träff, minus raketens sköldgenomträngning. Här slumpar varje raket fram medelvärdet. Vid det lägsta slumptalet krävs ungefär 10 till 15 % fler raketer än tabellen anger (en Lancet I behöver 50 för en Goombah, inte 45), vid det bästa ungefär 10 % färre (40). En Rivet II skjuter bara ner en Phantasm med en träff vid ett slumptal på 89 % eller mer och behöver två under det.

| Raketer som krävs | Seeker (1 600) | Phantasm (5 200) | Bulwark (26 000) | Goombah (80 000) | Crystalys (416 000) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Lancet I** | 1 | 3 | 15 | 45 | 232 |
| **Lancet II** | 1 | 2 | 8 | 20 | 116 |
| **Lancet III** | 1 | 1 | 5 | 11 | 78 |
| **Rivet I** | 1 | 3 | 12 | 36 | 185 |
| **Rivet II** | 1 | 1 | 6 | 16 | 93 |
| **Rivet III** | 1 | 1 | 4 | 9 | 62 |
| **Ember I** | 2 | 5 | 25 | 77 | 399 |
| **Ember II** | 1 | 3 | 13 | 37 | 193 |
| **Ember III** | 1 | 2 | 8 | 25 | 128 |
| **Scatter I** | 2 | 4 | 20 | 60 | 311 |
| **Scatter II** | 1 | 2 | 10 | 29 | 151 |
| **Scatter III** | 1 | 2 | 7 | 20 | 100 |

- De **vanliga** raketerna med enkelmål skjuter ner en Seeker med en träff vid varje slumptal och en Phantasm med tre (en Lancet I behöver en fjärde vid sitt lägsta); de är vardagsraketerna i de första sektorerna. De **sällsynta** är till för Bulwark och Goombah: åtta Lancet II-raketer tar en Bulwark på ungefär 35 sekunders timer. De **episka** skjuter ner en Phantasm med en träff vid varje slumptal och en Goombah med nio till elva. Explosionerna är värda sitt pris när flera utomjordingar står tätt: en Scatter III som briserar över en flock på fem Phantasm gör ungefär 18 000 skada över flocken i ett enda skott.
- En nedskjutning enbart med raketer är en rejäl utgift, inget sätt att bli rik: för den utomjording den är avsedd för kostar en raket med enkelmål ungefär en sjundedel till tre fjärdedelar av vad nedskjutningen ger (krediter, och Thulium till 200 krediter styck), och de svaga raketerna mot de starka utomjordingarna kostar mer än nedskjutningen ger. Att skjuta ner **Crystalys** med bara en sort kräver 62 till 399 raketer och minst fem minuters timer; en full hög på 500 episka raketer räcker till fyra till åtta av dem. Den starkaste utomjordingen kräver en plan: dina lasrar på x2-ammunition, en raket i mellannivån var 5:e sekund från första sekunden, och de stora raketerna längre ner som extra kraftslag.
- Betalningen för en nedskjutning är densamma hur den än gjordes (se [Crystalys](/wiki/04-Aliens/Crystalys.md) för den största), så en nedskjutning med raket lönar sig när den sparar tid och kostar mindre än den ger.
- **Även utomjordingar skjuter raketer.** Pirate Boss samt Dormant Force och Pulses i [svärmarna](/wiki/05-Swarms/Swarms.md) skjuter raka Rivet-raketer på piloten som attackerade dem, med samma 5-sekunderstimer. Ett skepp som håller sig i rörelse undviker dem. Svärmarnas bossar tappar också raketer i sina lådor.

## Raketerna som bara kan tillverkas {#the-craft-only-rockets}

Två raketer finns inte i butiken. **Monteringen** tillverkar dem, och de följer alla regler nedan (den gemensamma timern, säkra zoner, din koncern). Båda är raka raketer: de flyger mot punkten under din markör, som varje rak raket (spelet skickar markörens riktning oavsett vad du har valt; bara en gammal 0.4.3-klient, som inte skickar någon riktning, låter servern flyga dem mot det valda målet, annars mot punkten under dess markör, annars dit skeppet pekar). De slumpar fram mellan **90 % och 100 %** av sitt högsta tal, ett smalare band än de tolvs, så det de förstör med en träff nedan gäller också vid det lägsta slumptalet.

| Namn | Typ | Sällsynthet | Skada | Sköldgenomträngning | Explosionsradie | Räckvidd | Fart | Högst så många kan du bära | Tillverkas av |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **N.U.K.E.** | Rak, områdesskada | Legendarisk | 45 000–50 000 | – | 900 | 1 200 | 300 | 10 | 1 N.U.K.E. per tillverkning: 150 000 krediter, 3 000 Thulium, 6 Scatter III, 4 Power Core, 10 Reinforced Hull Plate, 40 Ship Fragment, 80 Cataclysite |
| **N.I.K.E.** | Rak, enkelmål | Mytisk | 67 500–75 000 | 35 % | – | 4 050 | 900 | 20 | 5 N.I.K.E. per tillverkning: 100 000 krediter, 1 500 Thulium, 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite |

- **N.U.K.E.**: spelets största explosion. En explosion på 900 enheter, dubbelt så lång räckvidd som Scatter III:s 400 och fem gånger så stor yta: 45 000 till 50 000 på varje skepp i den i mitten, avtagande till hälften av det, 22 500 till 25 000, vid kanten. Den är långsam (fyra sekunder i flykt). En N.U.K.E. utplånar varje Seeker och Phantasm i hela sin explosion och en Bulwark inom 830 enheter från detonationen (934 vid det bästa slumptalet), nästan i hela explosionen; den tar mer än hälften av en Goombah och en niondel av en Crystalys. Mot piloter är den det största slaget som finns: se reglerna nedan. Ringen på kartan är dess exakta räckvidd.
- **N.I.K.E.**: en raket med enkelmål som Rivet I, med 67 500 till 75 000 i skada och en sköldgenomträngning på 35 %: **den träffar det första skepp den rör vid och är förbrukad på det.** Det är också raketen som ger [Dark Matter](/wiki/03-Mechanics/Black-Hole.md): avfyrad mot det svarta hålet mitt i Farosektor 4 sväljs den när den korsar händelsehorisonten, och hålet ger tillbaka Dark Matter. Den flyger 4 050 enheter på 4,5 sekunder: avfyra den varifrån som helst mellan strålningens kant och 4 380 enheter från mitten. Från längre ut når den inte fram och går till spillo. Fem N.I.K.E. ger ungefär tio Dark Matter.
- **Haken.** En N.I.K.E. som möter ett skepp på vägen, en rival som väntar på linjen eller något annat den får skada, träffar det med 67 500 till 75 000 och är borta: det svarta hålet får ingenting, och det får inte du heller. Inget annat rör sig inom hålets ring som den kan råka träffa (utomjordingar och koncernpiloter håller sig utanför): bara piloter som gått in för Dark Matter eller väntar på dig vid kanten. Den flyger igenom din egen koncern, skepp i en säker zon och skepp du ännu inte får skada. Lämnar du kartan efter att ha avfyrat den flyger den vidare utan att skada någon och ger ändå din Dark Matter.
- Monteringen startar ingen tillverkning som skulle lämna dig med fler av en raket än dess gräns (*högst så många kan du bära*), inräknat det du har köat.

## Avfyrning {#firing}

1. Köp raketer i butiken (kategorin **Raketer**), upp till *högst så många kan du bära* för var och en: krediter för de vanliga och sällsynta, Thulium för de episka.
2. Öppna **Raketer** ovanför snabbfältet och dra de du vill ha till platser. Väljaren visar en kolumn per typ och en rad per nivå, med det du bär av varje. Under dem finns en egen rad, **Special · endast Monteringen**, för N.U.K.E. och N.I.K.E. (en liten hammare markerar den du inte bär någon av).
3. Tryck på platsens tangent. Ett klick på platsen för en **målsökande** raket avfyrar den mot ditt valda mål; ett klick på platsen för en **rak** raket armerar den, och ditt nästa klick i rymden avfyrar den dit. Tangenten **Avfyra raket** (`R` som standard, går att binda om i Inställningar › Styrning) avfyrar den raket du sköt senast, eller den första i snabbfältet.
4. En cirkelsektor sveper över **varje** raketplats under de 5 sekunderna till nästa avfyrning, med de återstående sekunderna i mitten. Ett tryck innan dess säger bara att raketerna laddas om (ett tryck under den sista tiondels sekunden avfyrar ändå). En drönarformation kan göra väntan mellan 3,65 och 6,75 sekunder (se nedan).

Peka på en raketplats för att se dess siffror (dess lägsta och högsta skada; butiken och hangaren säger detsamma) och, ute i världen, dess låsring (grön när det valda målet är inom räckhåll) eller dess linje och explosionscirkel. En raket som är låst på **dig** får skärmkanten att blinka rött.

**N.U.K.E.** ritar sin explosion på kartan innan du avfyrar (cirkeln på 900 enheter vid den siktade punkten) och, när den detonerar, en vit blixt över vyn, en ring som löper ut till den exakta räckvidden på ungefär en sekund och blir kvar två till, ett moln som reser sig som en svamp, och en kameraskakning som är starkare ju närmare du är. **Minska skärmskakning** tar bort skakningen, och **Minska rörelser** förkortar blixten till en tredjedels sekund med mindre än hälften av dess ljus (båda finns under Inställningar › Grafik); en lägre partikelkvalitet tunnar ut molnet och tar bort gnistorna, aldrig blixten eller ringen. **N.I.K.E.** siktas som en Rivet I, med linjen från ditt skepp till markören, och spelet vägrar den aldrig för att den är långt från det svarta hålet eller på en karta utan något: vart den tar vägen är det upp till dig att bedöma. Dess kort säger **Svart hål: Ger Dark Matter** bredvid dess skada. Den lämnar ett violett spår med gnistor som slingrar sig runt det; ett skepp den möter tar träffen som av vilken raket som helst, och när den i stället korsar horisonten blossar hålet.

## Drönarformationer och raketer {#drone-formations-and-rockets}

En buren [drönarformation](/wiki/03-Mechanics/Formations.md) är det enda som ändrar en raket. Alla skadesiffror på den här sidan gäller ett skepp utan formation.

- **Skada.** Raketbonusen hos Ballista (+55 %), Bodkin (+29 %) och Asterism (+24 %) multiplicerar skadan hos alla 14 raketer, även N.U.K.E. och N.I.K.E. Testudos pris på all skada räknas också på raketer, och Cullers skada mot utomjordingar räknas på en raket som träffar en utomjording. Alla faktorer på en raket tillsammans stannar vid ×1,59.
- **Omladdning.** Asterism gör den gemensamma timern 35 % längre (6,75 sekunder), Cordon 11 % längre (5,55) och Redoubt 27 % kortare (3,65), men aldrig kortare än raketens flygtid plus ett ögonblick: 4,1 sekunder efter en N.U.K.E. och 4,6 efter en N.I.K.E. Väntan sätts när du avfyrar, så att byta formation efteråt förkortar den inte, och laddcirkeln över raketplatserna följer den.
- **De två storas gränser står sig.** Med den bästa formationen träffar en N.I.K.E. med upp till 116 250, vilket en oskadad Paragon (128 000) överlever, och en N.U.K.E. med upp till 77 500, vilket en Goombah (80 000) överlever.
- **Undanmanöver.** Asterisms 7 % undanmanöver ger en direkt raket som träffar dig 7 % chans att inte göra någon skada alls, och ett flytande ”Miss” visas över ditt skepp; en områdesexplosion har inget sikte och undviks aldrig.
- **Genomträngning.** Gemini och Stiletto lägger sina poäng till sköldgenomträngningen hos en direkt raket (en explosion har ingen), upp till 40 % sammanlagt.

## Regler {#rules}

- Du behöver **ingen monterad laser** för att avfyra en raket, och dina lasrar ändrar varken vad den gör eller hur långt den når: en målsökande raket låser på ett mål inom sin egen låsräckvidd, en rak flyger sitt eget avstånd. Utan monterad laser visar hangarens ruta Räckvidd ett streck, och bara dina raketer skjuter.
- En raket förbrukas per avfyrning, oavsett om den träffar eller inte.
- Raketer följer lasrarnas regler: inget inom en **säker zon** skadas, ingen pilot skadas innan **Fredsprotokollet** upphör eller där en sektor förbjuder PvP, och **din egen koncern och din egen grupp skadas aldrig** av dina raketer, vare sig direktträff eller explosion.
- Att avfyra en raket avslutar ditt eget skydd i säker zon direkt. Det är ett skott: det avslutar också ditt eget **kamouflage**, och Cloaking CPU:n laddas då om i en minut, som efter varje slut på ett kamouflage. Kamouflerad eller inte hindrar en avfyrning dig från att kamouflera dig under de 10 sekunderna efteråt (se [Extrautrustning](/wiki/06-Items/Extras.md)).
- Ett skepp som är **kamouflerat** eller inom **de 3 sekunderna av sin EMP** går inte att låsa på: en målsökande raket nekas, och en som redan flyger mot det tappar sin målfixering och flyger rakt vidare. En rak raket med enkelmål flyger igenom ett sådant skepp. En raket med **områdesskada** kräver ingen målfixering, så den skadar de skepp den täcker, kamouflerade eller inte, och den avslutar ett kamouflage (se [Extrautrustning](/wiki/06-Items/Extras.md)).
- **Ingenting begränsar vad en raket gör mot en pilot.** En annan pilots skepp tar full skada: sköldarna först (deras absorption minus raketens sköldgenomträngning), sedan skrovet. De små skeppen klarar sig inte. På standardsköldkärnorna (Light, 45 % absorption) förstör en N.I.K.E. vid varje slumptal en färsk Protos, Kitefin eller Ostirion med en träff (en Paragon förlorar 47 till 53 % av sitt skrov, en Wraith ungefär en femtedel), och en N.U.K.E. förstör en Protos var som helst i sin explosion, en Kitefin inom ungefär 50 enheter från detonationen (220 vid det bästa slumptalet) och inget större i en enda explosion. Två Lancet III-raketer eller två Rivet III-raketer förstör en Protos vid varje slumptal; en Wraith tål mellan 48 och 75 av dem. Fredsprotokollet, de säkra zonerna och din koncern är det som står mellan en pilot och en raket. De här siffrorna gäller ett skepp utan formation; en raketformation höjer dem med upp till 55 % (se [Drönarformationer och raketer](#drone-formations-and-rockets)).
- Bara en rakets **direktträff** paxar en utomjording (se [Strid](/wiki/03-Mechanics/Combat.md)); en explosions kant kan skada en utomjording som någon redan har paxat utan att stjäla den. Varje utomjording en explosion skadar, även en sovande, vänder sig mot dig, som vid en lasersträff (en Seeker eller en Goombah, som bara slår tillbaka, inräknade); en som explosionen missar förblir sovande.
- Timern är din: den överlever ett hopp, en återanslutning, ett skeppsbyte och ett förstört skepp.

De tolv raketerna i den första tabellen köps (krediter för de vanliga och sällsynta, Thulium för de episka); N.U.K.E. och N.I.K.E. tillverkas.

Se även: [Lasrar och ammunition](/wiki/06-Items/Lasers.md), [Strid](/wiki/03-Mechanics/Combat.md), [Det svarta hålet](/wiki/03-Mechanics/Black-Hole.md).
