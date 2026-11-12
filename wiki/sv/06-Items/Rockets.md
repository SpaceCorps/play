<!-- wiki-i18n source: bd68fa87d7243d6f -->
<!-- wiki-i18n title: Raketer -->
# Raketer {#rockets}

Raketer är ett andra vapen vid sidan av dina lasrar: ett skott var några sekunder som träffar mycket hårdare än en lasersalva. Tolv **vanliga raketer** i fyra typer, tre nivåer vardera, delar **en omladdningstimer på 3 sekunder**, som skeppets raketkastare bestämmer. Tolv **specialraketer**, som gör mer än skada, delar **en egen timer på 5 sekunder**, och var och en väntar dessutom på sin egen. Bara de fyra vanliga raketerna, Flares och Ricochet köps, med **krediter**; varje annan raket tillverkas i Monteringen. En [drönarformation](/wiki/03-Mechanics/Formations.md) kan höja en raketens skada och göra den vanliga timern längre eller kortare: se [Drönarformationer och raketer](#drone-formations-and-rockets).

## På en minut {#in-one-minute}

- **Tolv vanliga raketer.** Fyra typer (Lancet, Rivet, Ember, Scatter), tre nivåer vardera. Bara nivå I säljs, för 500 krediter; nivå II och III tillverkas i Monteringen av 100 raketer av nivån under.
- **Varje raket slumpar sin skada.** När du avfyrar den väljer spelet ett tal mellan raketens lägsta och högsta skada (en Lancet I: 1 700 till 2 100). Ditt skepp, dina lasrar, förstärkare och boosters ändrar inget; en drönarformation och din **Raketteknik** (en pilotförmåga) gör det. De raketer som utomjordingar skjuter slumpar inte: de gör ett fast tal ([Mot utomjordingarna](#against-the-aliens)).
- **Explosioner är starkast i mitten.** Ember- och Scatter-raketer briserar och skadar varje skepp inom ringen: hela talet i mitten, 66 % av det vid kanten (N.U.K.E.:s explosion faller till hälften).
- **Två sorters timer.** De vanliga raketerna delar en: 3 sekunder efter varje avfyrning, eller med en **Raketkastare II till V** en serie på 2 till 5 raketer med 0,15 sekunder emellan och sedan 5 sekunder ([Avfyra](#firing)). Specialraketerna delar en annan på 5 sekunder som ingen raketkastare ändrar, och var och en väntar dessutom på sin egen, från 3 sekunder till 2 minuter ([Specialraketer](#special-rockets)).
- **Tolv specialraketer.** De fryser, stör, förgiftar eller markerar ett skepp, bryter sköldar eller låsningar, läker dina vänner, hoppar till ett andra skepp eller öppnar ett litet svart hål vid markören. N.U.K.E. och N.I.K.E. är två av dem.
- **Målsökande eller rak.** En målsökande raket (Lancet, Ember) behöver ett mål du har valt. En rak (Rivet, Scatter) flyger mot din muspekare.
- **Flera saker bärs som en raket.** **EMP Charge** är en förbrukningsvara: en hög i ditt inventarie, som används från snabbfältet och inte tar någon plats ([EMP Charge](#emp-charge)). Det gäller de två **Energetic Wall** också ([Energetic Wall](/wiki/06-Items/Extras.md#energetic-wall)).

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Föremålsträd {#item-tree}

Det som Monteringen tillverkar kräver först sin teknologi; håll pekaren över ett föremål för att se hur lång tid forskningen tar. Teknologiträdet, bränslet och boosten: [Forskning](/wiki/03-Mechanics/Research.md).

```tree
Lancet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet II | rocket, rare | craft 50000 Credits, 200 Thulium, 120 s, x100 | research 1800 s, 1800 science | 100 Lancet I, 5 Ship Fragment, 10 Nyxite | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet II | rocket, rare | craft 50000 Credits, 200 Thulium, 120 s, x100 | research 1800 s, 1800 science | 100 Rivet I, 5 Ship Fragment, 10 Daraxium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember II | rocket, rare | craft 50000 Credits, 200 Thulium, 120 s, x100 | research 1800 s, 1800 science | 100 Ember I, 5 Ship Fragment, 10 Cataclysite | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter II | rocket, rare | craft 50000 Credits, 200 Thulium, 120 s, x100 | research 1800 s, 1800 science | 100 Scatter I, 5 Ship Fragment, 10 Quorvium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ricochet | rocket, rare | buy 4000 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Flares | rocket, rare | buy 25000 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet III | rocket, epic | craft 150000 Credits, 800 Thulium, 300 s, x100 | research 10800 s, 10800 science | 100 Lancet II, 15 Ship Fragment, 2 Reinforced Hull Plate, 20 Nyxite | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet III | rocket, epic | craft 150000 Credits, 800 Thulium, 300 s, x100 | research 10800 s, 10800 science | 100 Rivet II, 15 Ship Fragment, 2 Reinforced Hull Plate, 20 Daraxium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember III | rocket, epic | craft 150000 Credits, 800 Thulium, 300 s, x100 | research 10800 s, 10800 science | 100 Ember II, 15 Ship Fragment, 2 Reinforced Hull Plate, 20 Cataclysite | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter III | rocket, epic | craft 150000 Credits, 800 Thulium, 300 s, x100 | research 10800 s, 10800 science | 100 Scatter II, 15 Ship Fragment, 2 Reinforced Hull Plate, 20 Quorvium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Freeze Rocket | rocket, epic | craft 50000 Credits, 1000 Thulium, 300 s, x5 | research 14400 s, 14400 science | 10 Ship Fragment, 1 Power Core, 30 Cataclysite | /wiki/06-Items/Rockets.md#the-twelve-rockets
EMP Rocket | rocket, epic | craft 60000 Credits, 1200 Thulium, 300 s, x5 | research 14400 s, 14400 science | 10 Ship Fragment, 2 Power Core, 20 Quorvium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Shield Breaker | rocket, epic | craft 80000 Credits, 1500 Thulium, 300 s, x5 | research 21600 s, 21600 science | 15 Ship Fragment, 3 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-twelve-rockets
Toxic Rocket | rocket, epic | craft 60000 Credits, 1000 Thulium, 300 s, x5 | research 14400 s, 14400 science | 10 Ship Fragment, 30 Nyxite, 10 Quorvium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Marking Rocket | rocket, epic | craft 50000 Credits, 800 Thulium, 300 s, x5 | research 14400 s, 14400 science | 10 Ship Fragment, 30 Daraxium, 10 Nyxite | /wiki/06-Items/Rockets.md#the-twelve-rockets
Support Rocket | rocket, epic | craft 90000 Credits, 2000 Thulium, 600 s, x3 | research 21600 s, 21600 science | 20 Ship Fragment, 2 Power Core, 40 Nyxite, 20 Quorvium | /wiki/06-Items/Rockets.md#the-twelve-rockets
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
Gravitational N.U.K.E. | rocket, mythical | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 1 N.U.K.E., 4 Power Core, 2 Ancient Control Unit, 40 Quorvium | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
Cooldown Rocket | rocket, legendary | craft 100000 Credits, 2500 Thulium, 600 s, x3 | research 28800 s, 28800 science | 20 Ship Fragment, 3 Power Core, 1 Ancient Control Unit, 40 Quorvium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Mine I | consumable, uncommon | buy 100 Thulium | /wiki/06-Items/Extras.md#mine
EMP Charge | consumable, uncommon | buy 500 Thulium | /wiki/06-Items/Rockets.md#emp-charge
Energetic Wall I | consumable, uncommon | buy 10000 Credits | /wiki/06-Items/Extras.md#energetic-wall
Energetic Wall II | consumable, rare | craft 600 Thulium, 120 s | research 21600 s, 21600 science | 5 Ship Fragment, 1 Power Core | /wiki/06-Items/Extras.md#energetic-wall
Mine II | consumable, rare | craft 200 Thulium, 120 s | research 10800 s, 10800 science | 2 Mine I, 3 Ship Fragment, 1 Power Core | /wiki/06-Items/Extras.md#mine
Mine III | consumable, epic | craft 400 Thulium, 300 s | research 21600 s, 21600 science | 2 Mine II, 8 Ship Fragment, 1 Reinforced Hull Plate, 2 Power Core | /wiki/06-Items/Extras.md#mine

Lancet I => Lancet II => Lancet III
Rivet I => Rivet II => Rivet III
Ember I => Ember II => Ember III
Scatter I => Scatter II => Scatter III => N.U.K.E. => Gravitational N.U.K.E.
Mine I => Mine II => Mine III
Energetic Wall I -> Energetic Wall II
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
- En raket med **enkelmål** träffar det första skepp den får träffa (en målsökande bara sitt mål). En raket med **områdesskada** exploderar bredvid det första skepp den möter, vid den punkt du siktade på, eller där dess flykt tar slut, och skadar varje skepp inom sin **explosionsradie**: full skada i mitten, 66 % av den vid kanten (hälften för N.U.K.E.). Ringen som explosionen ritar på kartan är dess exakta räckvidd.
- **Asteroider.** En målsökande raket som avfyras mot en [asteroid](/wiki/03-Mechanics/Asteroid-Mining.md) flyger mot den; en rak raket flyger mot markören, som mot vilket mål som helst, och krossar asteroiden när markören står på den. Den första asteroiden i vägen för vilken raket som helst stoppar den och tar träffen i stället för skeppet bakom ([Skydd](/wiki/03-Mechanics/Asteroid-Mining.md#cover)). En [Energetic Wall](/wiki/06-Items/Extras.md#energetic-wall) stoppar en raket på samma sätt; N.I.K.E. flyger över den. De tolv raketerna i butiken och N.U.K.E. kan spränga en; N.I.K.E. kan inte avfyras mot en och flyger över dem. Dina lasrar skadar också en asteroid, men bara med 5 % av vad de gör mot ett skepp: raketen är verktyget för det jobbet.

## De tolv raketerna {#the-twelve-rockets}

Varje raket har **sin egen skada, som slumpas fram när du avfyrar den**: var som helst mellan dess lägsta och dess högsta tal, och tabellen visar båda och medelvärdet. Den beror inte på ditt skepp, dina lasrar och deras förstärkare, dina boosters, din ammunition eller dina drönare, och en raket ger aldrig kritiska träffar. Bara en **drönarformation** och din **Raketteknik** ändrar den: tabellen här anger skadan utan formation och före Raketteknik (se [Drönarformationer och raketer](#drone-formations-and-rockets) och [Raketteknik](#rocket-tech)). En raket med enkelmål gör den framslumpade skadan på det skepp den träffar; en explosion slumpar en gång och gör den på **varje skepp inom den**, hela talet i mitten och 66 % av det vid kanten (hälften för N.U.K.E.). *Sköldgenomträngning* dras av från målets absorption för den träffen (ett skepps absorption är den andel av en träff som dess sköldar tar, se [Sköldmekanik](/wiki/03-Mechanics/Shields.md#shield-penetration)): en Lancet III:s 35 % lämnar sköldarna på ett skepp med 80 % 45 % av träffen och skickar de övriga 55 % till skrovet. En explosion har ingen.

| Namn | Typ | Sällsynthet | Skada | Medel | Sköldgenomträngning | Explosionsradie | Låsräckvidd | Räckvidd | Fart | Pris | Högst så många kan du bära |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **Lancet I** | Målsökande, enkelmål | Vanlig | 3 500–4 200 | 3 850 | 25 % | – | 1 000 | 1 584 | 660 | 500 krediter | 5 000 |
| **Lancet II** | Målsökande, enkelmål | Sällsynt | 5 200–6 200 | 5 700 | 35 % | – | 1 300 | 2 296 | 820 | Tillverkad av 100 Lancet I | 2 000 |
| **Lancet III** | Målsökande, enkelmål | Episk | 7 300–8 700 | 8 000 | 35 % | – | 1 300 | 2 296 | 820 | Tillverkad av 100 Lancet II | 500 |
| **Rivet I** | Rak, enkelmål | Vanlig | 4 500–5 250 | 4 875 | 25 % | – | – | 1 120 | 700 | 500 krediter | 5 000 |
| **Rivet II** | Rak, enkelmål | Sällsynt | 7 000–8 000 | 7 500 | 35 % | – | – | 1 100 | 500 | Tillverkad av 100 Rivet I | 2 000 |
| **Rivet III** | Rak, enkelmål | Episk | 9 800–11 200 | 10 500 | 35 % | – | – | 1 100 | 500 | Tillverkad av 100 Rivet II | 500 |
| **Ember I** | Målsökande, områdesskada | Vanlig | 2 400–2 900 | 2 650 | – | 345 | 920 | 1 500 | 600 | 500 krediter | 5 000 |
| **Ember II** | Målsökande, områdesskada | Sällsynt | 3 500–4 500 | 4 000 | – | 450 | 1 150 | 2 030 | 700 | Tillverkad av 100 Ember I | 2 000 |
| **Ember III** | Målsökande, områdesskada | Episk | 4 900–6 300 | 5 600 | – | 495 | 1 150 | 2 030 | 700 | Tillverkad av 100 Ember II | 500 |
| **Scatter I** | Rak, områdesskada | Vanlig | 3 000–3 500 | 3 250 | – | 435 | – | 1 080 | 540 | 500 krediter | 5 000 |
| **Scatter II** | Rak, områdesskada | Sällsynt | 4 500–5 500 | 5 000 | – | 600 | – | 1 092 | 420 | Tillverkad av 100 Scatter I | 2 000 |
| **Scatter III** | Rak, områdesskada | Episk | 6 300–7 700 | 7 000 | – | 660 | – | 1 092 | 420 | Tillverkad av 100 Scatter II | 500 |

Ju dyrare nivån är, desto hårdare träffar en raket, desto längre når den, desto mer sköldgenomträngning har den och desto färre kan du bära; de dyra ger också mest skada för pengarna. En rak raket gör i genomsnitt 23 till 32 % mer än den målsökande raketen av samma nivå och samma slag för samma pris (en fjärdedel till en tredjedel mer), eftersom du måste sikta den. En explosion gör ungefär två tredjedelar av vad raketen med enkelmål av samma nivå och slag gör (66 till 70 % i genomsnitt: en Ember mot en Lancet, en Scatter mot en Rivet), på varje skepp den täcker. Skadan i en explosion är full i mitten och faller i en rak linje till **66 % vid kanten** (hälften för N.U.K.E.): ett skepp vars skrov ligger halvvägs ut tar 83 %, och ett vars skrov ligger utanför ringen tar ingenting. Ett skott gör i genomsnitt mitten av sitt intervall, 89 till 94 % av sitt högsta tal, och tabellen längre ner som räknar raketer utgår från det.

## Vad de kostar {#what-they-cost}

En vanlig raket (nivå I) kostar 500 krediter i butiken, i varje typ. De sällsynta (nivå II) och episka (nivå III) raketerna säljs inte: Monteringen tillverkar dem, 100 åt gången, av 100 raketer av nivån under (en sats sällsynta kostar dessutom 50 000 krediter och 200 Thulium, en sats episka 150 000 krediter och 800 Thulium, med några material; butiken och Monteringen säger resten). Avfyrad vid varje timer är en vanlig raket 10 000 krediter i minuten, mot de 900 krediter i minuten som en Ostirions tre lasrar bränner vid x1. Ett fullt lager är 5 000 vanliga raketer (2 500 000 krediter), 2 000 sällsynta eller 500 episka: du köper så många du vill upp till det, och *högst så många kan du bära* för en raket är den enda gränsen för hur många du håller. Vid wipen behåller du utan att göra något upp till 1 000 av var och en av de tolv raketerna; allt över det, och varje N.U.K.E. och N.I.K.E., överlever bara i transportförrådet, där en raket väger 1 kg (en N.U.K.E. eller N.I.K.E. 250 kg): se [wipen](/wiki/03-Mechanics/Wipe-Timeline.md#ammo-and-rockets). En raket var 3:e sekund är bara tjugo i minuten, så en raket är ett extra kraftslag ovanpå dina lasrar: de billiga till de svaga utomjordingarna, de dyra till de stora striderna. Det du har lagt ut i [Auktionen](/wiki/03-Mechanics/Auction.md#limits) och lotterna du leder där räknas in i den gränsen när du köper eller budar på en raket. Det här är grundvärdena: Pilot-forskningen Sealed Backdoor ([Forskning](/wiki/03-Mechanics/Research.md#pilot-technologies)) höjer gränsen för varje raket åt dig, sammanlagt med 25 %, 50 %, 100 %, 150 % eller 200 %, avrundat nedåt, så att 5 000 blir 6 250 på nivå I och 15 000 på nivå V.

Butiken säljer de fyra vanliga raketerna, en typ i taget, och efter dem Flares och Ricochet; hangaren, transportförrådet och raketväljaren listar de tolv vanliga raketerna på samma sätt, varje typ under sitt namn, den vanliga först och den episka sist, och efter dem specialraketerna.

## Mot utomjordingarna {#against-the-aliens}

Så många raketer krävs för att skjuta ner en utomjording, en raketsort i taget, där varje raket slumpar fram medelvärdet av sitt intervall (Alpha; utomjordingar i Beta och Gamma är 1,5 respektive 2 gånger så starka). En explosion räknas som det skepp den briserar bredvid tar emot den, en bit från mitten (95 till 97 % av skadan i mitten). En utomjordings sköld tar 80 % av en träff, minus raketens sköldgenomträngning. Vid det lägsta slumptalet krävs upp till 15 % fler raketer än tabellen anger (en Lancet I behöver 48 för en Goombah, inte 43), vid det bästa upp till 13 % färre (39). En Rivet II, en Lancet III och en Rivet III skjuter ner en Phantasm med en träff vid varje slumptal; en Rivet I behöver två vid ett slumptal på 2 600 eller mer, och tre under det.

| Raketer som krävs | Seeker (1 600) | Phantasm (5 200) | Bulwark (26 000) | Goombah (80 000) | Crystalys (416 000) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Lancet I** | 1 | 2 | 7 | 19 | 109 |
| **Lancet II** | 1 | 1 | 5 | 11 | 73 |
| **Lancet III** | 1 | 1 | 4 | 8 | 52 |
| **Rivet I** | 1 | 1 | 6 | 15 | 86 |
| **Rivet II** | 1 | 1 | 4 | 8 | 56 |
| **Rivet III** | 1 | 1 | 3 | 6 | 40 |
| **Ember I** | 1 | 3 | 11 | 32 | 166 |
| **Ember II** | 1 | 2 | 7 | 21 | 109 |
| **Ember III** | 1 | 1 | 5 | 15 | 78 |
| **Scatter I** | 1 | 2 | 9 | 26 | 134 |
| **Scatter II** | 1 | 2 | 6 | 17 | 87 |
| **Scatter III** | 1 | 1 | 4 | 12 | 62 |

- De **vanliga** raketerna med enkelmål skjuter ner en Seeker med en träff vid varje slumptal och en Phantasm med tre (en Lancet I behöver en fjärde vid sitt lägsta); de är vardagsraketerna i de första sektorerna. De **sällsynta** är till för Bulwark och Goombah: sju Lancet II-raketer tar en Bulwark på ungefär 20 sekunders timer. De **episka** raketerna med enkelmål skjuter ner en Goombah med åtta (Rivet III) till elva (Lancet III). Explosionerna är värda sitt pris när flera utomjordingar står tätt: en Scatter III som briserar över en flock på fem Phantasm (alla inom 250 enheter från målet du siktade på) gör ungefär 33 000 skada över flocken i ett enda skott.
- En nedskjutning enbart med raketer är en rejäl utgift, inget sätt att bli rik: en vanlig raket med enkelmål kostar mellan 9 % (en Rivet I mot en Phantasm) och 47 % (en Lancet I mot en Crystalys) av vad nedskjutningen ger (krediter, och Thulium till 200 krediter styck), och de sällsynta explosionsraketerna mot den starkaste utomjordingen kostar mer än nedskjutningen ger (en Ember II mot en Crystalys: 133 %). Att skjuta ner **Crystalys** med bara en sort kräver 40 till 166 raketer och två till åtta minuters timer; en full hög på 500 episka raketer räcker till sex till tolv av dem. Den starkaste utomjordingen kräver en plan: dina lasrar på x2-ammunition, en raket i mellannivån var 3:e sekund från första sekunden, och de stora raketerna längre ner som extra kraftslag.
- Betalningen för en nedskjutning är densamma hur den än gjordes (se [Crystalys](/wiki/04-Aliens/Crystalys.md) för den största), så en nedskjutning med raket lönar sig när den sparar tid och kostar mindre än den ger.
- **Även utomjordingar skjuter raketer.** Pirate Boss samt Dormant Force och Pulses i [svärmarna](/wiki/05-Swarms/Swarms.md) och Siege Wardens i [klanerna](/wiki/03-Mechanics/Clans.md#clan-wardens) skjuter raka Rivet-raketer på piloten som attackerade dem, med egna timers (5 sekunder hos svärmarna, 8 till 24 hos Siege Wardens) som din formation inte ändrar. **En utomjordings raket slumpar inte och använder inte intervallen ovan**: den gör en fast skada på 2 500 (Rivet I), 5 000 (Rivet II) eller 7 500 (Rivet III), mer i Beta och Gamma, där utomjordingar är 1,5 respektive 2 gånger så starka (en Clan Wardens raket är densamma i alla världar). Ett skepp som håller sig i rörelse undviker dem. Svärmarnas bossar tappar också raketer i sina lådor.

## Raketerna som bara kan tillverkas {#the-craft-only-rockets}

Två raketer finns inte i butiken. **Monteringen** tillverkar dem, och de följer alla regler nedan (den gemensamma timern, säkra zoner, PvP-reglerna). Båda är raka raketer: de flyger mot punkten under din markör, som varje rak raket (spelet skickar markörens riktning oavsett vad du har valt; bara en gammal 0.4.3-klient, som inte skickar någon riktning, låter servern flyga dem mot det valda målet, annars mot punkten under dess markör, annars dit skeppet pekar). De slumpar fram mellan **90 % och 100 %** av sitt högsta tal, ett smalare band än de tolvs, så det de förstör med en träff nedan gäller också vid det lägsta slumptalet.

| Namn | Typ | Sällsynthet | Skada | Sköldgenomträngning | Explosionsradie | Räckvidd | Fart | Högst så många kan du bära | Tillverkas av |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **N.U.K.E.** | Rak, områdesskada | Legendarisk | 45 000–50 000 | – | 1 350 | 1 200 | 300 | 10 | 1 N.U.K.E. per tillverkning: 150 000 krediter, 3 000 Thulium, 6 Scatter III, 4 Power Core, 10 Reinforced Hull Plate, 40 Ship Fragment, 80 Cataclysite |
| **N.I.K.E.** | Rak, enkelmål | Mytisk | 67 500–75 000 | 35 % | – | 4 050 | 900 | 20 | 5 N.I.K.E. per tillverkning: 100 000 krediter, 1 500 Thulium, 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite |

- **N.U.K.E.**: spelets största explosion. En explosion på 1 350 enheter, mer än dubbelt så lång räckvidd som Scatter III:s 600 och fem gånger så stor yta: 45 000 till 50 000 på varje skepp i den i mitten, avtagande till hälften av det, 22 500 till 25 000, vid kanten. Den är långsam (fyra sekunder i flykt). En N.U.K.E. utplånar varje Seeker och Phantasm i hela sin explosion och en Bulwark inom 1 210 enheter från detonationen (1 366 vid det bästa slumptalet), nästan i hela explosionen; den tar mer än hälften av en Goombah och en niondel av en Crystalys. Mot piloter är den det största slaget som finns: se reglerna nedan. Ringen på kartan är dess exakta räckvidd.
- **N.I.K.E.**: en raket med enkelmål som Rivet I, med 67 500 till 75 000 i skada och en sköldgenomträngning på 35 %: **den träffar det första skepp den rör vid och är förbrukad på det.** Det är också raketen som ger [Dark Matter](/wiki/03-Mechanics/Black-Hole.md): avfyrad mot det svarta hålet mitt i Farosektor 4 sväljs den när den korsar händelsehorisonten, och hålet ger tillbaka Dark Matter. Den flyger 4 050 enheter på 4,5 sekunder: avfyra den varifrån som helst mellan strålningens kant och 4 380 enheter från mitten. Från längre ut når den inte fram och går till spillo. Fem N.I.K.E. ger ungefär tio Dark Matter.
- **Haken.** En N.I.K.E. som möter ett skepp på vägen, en rival som väntar på linjen eller något annat den får skada, träffar det med 67 500 till 75 000 och är borta: det svarta hålet får ingenting, och det får inte du heller. Inget annat rör sig inom hålets ring som den kan råka träffa (utomjordingar och koncernpiloter håller sig utanför): bara piloter som gått in för Dark Matter eller väntar på dig vid kanten. Den flyger igenom din egen grupp, skepp i en säker zon och skepp du ännu inte får skada; skepp i din egen koncern träffar den som vilket annat skepp som helst där PvP är på. Lämnar du kartan efter att ha avfyrat den flyger den vidare utan att skada någon och ger ändå din Dark Matter.
- Monteringen startar ingen tillverkning som skulle lämna dig med fler av en raket än dess gräns (*högst så många kan du bära*), inräknat det du har köat. Sealed Backdoor höjer också deras gränser (10 blir 12 och 20 blir 25 på nivå I, 30 och 60 på nivå V).

## Specialraketer {#special-rockets}

Specialraketerna gör saker som en skadesiffra inte säger. De delar **en timer på 5 sekunder** (ingen raketkastare ändrar den), och var och en väntar dessutom på **sin egen timer**, från 3 sekunder till 2 minuter; de vanliga raketernas timer är separat, så en vanlig raket och en specialraket kan avfyras samtidigt. Monteringen tillverkar dem, utom Flares och Ricochet, som butiken säljer (föremålsträdet ovan har varje recept). N.U.K.E. och N.I.K.E. ovan är också specialraketer, och N.U.K.E. har ingen egen timer. Auto-raket-CPU:n och raketkastarna avfyrar bara vanliga raketer.

| Namn | Typ | Effekt | Egen timer | Högst så många kan du bära |
| :--- | :--- | :--- | :---: | :---: |
| **Freeze Rocket** | Målsökande, enkelmål | En målsökande raket utan skada: skeppet den träffar fryser och flyger 60 % långsammare i fyra sekunder. | 30 s | 50 |
| **EMP Rocket** | Målsökande, enkelmål | En målsökande raket utan skada: skeppet den träffar påverkas av en EMP-laddning i tre sekunder. | 30 s | 50 |
| **Shield Breaker** | Rak, enkelmål | En snabb, ostyrd raket gjord för sköldar: 25 000 mot skölden och 5 000 mot skrovet, men så länge det finns sköld kvar träffar den bara skölden. | 15 s | 50 |
| **Toxic Rocket** | Målsökande, enkelmål | En målsökande raket utan egen skada: skeppet den träffar förgiftas i fem sekunder och förlorar en halv procent av sina effektiva livspoäng (skrov och sköld tillsammans) per sekund, taget från skrovet. | 20 s | 50 |
| **Marking Rocket** | Målsökande, enkelmål | En målsökande raket utan skada: skeppet den träffar markeras i fem sekunder och tar 20 % mer skada från allt. | 30 s | 50 |
| **Cooldown Rocket** | Målsökande, enkelmål | En målsökande raket utan skada: i åtta sekunder svalnar det träffade skeppets tidsstyrda föremål med halv hastighet. | 60 s | 20 |
| **Gravitational N.U.K.E.** | Rak, områdesskada | En N.U.K.E. ombyggd kring en kollapsad kärna. Den placeras vid markören och öppnar ett litet svart hål i femton sekunder som drar in skepp och målsökande raketer. Bara en kan finnas på en karta. Endast Monteringen tillverkar den, och den kan aldrig säljas på Auktionen. | 120 s | 5 |
| **Support Rocket** | Målsökande, enkelmål | En målsökande raket utan skada: den reparerar skrovet på det enda vänliga skepp den träffar med exakt 100 000 poäng (aldrig över maxvärdet), oavsett skeppets storlek. Vänliga är din grupp och din koncern, och den kan bara avfyras mot ett vänligt skepp. | 120 s | 20 |
| **Flares** | Rak, enkelmål | Avfyras från ditt eget skepp: den bryter alla målsökande raketer som är låsta på dig. | 60 s | 20 |
| **Ricochet** | Rak, enkelmål | En snabb, ostyrd raket som träffar som en Rivet II och efter första träffen hoppar till ett andra skepp med 75 % av skadan. | 3 s | 500 |

- Ett andra träff av samma slag förnyar en frysning, en störning, en förgiftning, en markering eller en nedsaktad nedkylning och läggs aldrig ovanpå den första. Toxic Rockets skada är skyttens, så ett dödande med gift räknas för hen.
- Gravitations-N.U.K.E. **placeras vid markören**: den flyger till punkten under den, eller så långt den når, och inget skepps zonrör utlöser den. Bara en gravitationsbrunn kan finnas på en karta: en andra avfyrning avvisas och inget förbrukas. I brunnens mitt snurrar ett svart hål, och dess dragning tar även skepp som står stilla, inte bara de som flyger: ett parkerat skepp bärs till mitten tillsammans med sin destination.
- **Support Rocket** reparerar en vän och ingen annan: ett skepp i din grupp eller din koncern, koncernens piloter inräknade. Den återställer exakt 100 000 skrovpoäng (aldrig över maxvärdet) och ingen sköld. Den kan inte användas på dig själv: är inget valt avvisas tryckningen som för vilken målsökande raket som helst, och är en fiende, en alien, en asteroid eller ditt eget skepp valt avvisas den som ”ingen vän”; inget förbrukas. En vän med fullt skrov avvisas och inget förbrukas. En reparation är ingen träff: den avbryter ingen Repair Drone.

## Avfyrning {#firing}

1. Köp de vanliga raketerna i butiken (kategorin **Raketer**), upp till *högst så många du kan bära* av varje, för krediter; tillverka de sällsynta och episka i Monteringen av 100 av nivån under.
2. Öppna **Raketer** ovanför snabbfältet och dra de du vill ha till platser. Väljaren visar en kolumn per typ och en rad per nivå, med det du bär av varje. Under dem finns **specialraketerna**, fyra per rad (en liten hammare markerar en som bara kan tillverkas och som du inte bär någon av).
3. Tryck på platsens tangent. Ett klick på platsen för en **målsökande** raket avfyrar den mot ditt valda mål; ett klick på platsen för en **rak** raket armerar den, och ditt nästa klick i rymden avfyrar den dit. Tangenten **Avfyra raket** (`R` som standard, går att binda om i Inställningar › Styrning) avfyrar den raket du sköt senast, eller den första i snabbfältet.
4. En cirkelsektor sveper över varje raketplats för den timer som den raketen väntar på: 3 sekunder för en vanlig raket (5 med en raketkastare), och för en specialraket den längsta av de 5 sekunderna och dess egen, med de återstående sekunderna i mitten. Ett tryck innan dess säger bara att raketerna laddas om (ett tryck under den sista tiondels sekunden avfyrar ändå). En drönarformation kan göra den vanliga timern mellan 2,19 och 4,05 sekunder (se nedan).

Peka på en raketplats för att se dess siffror (dess lägsta och högsta skada; butiken och hangaren säger detsamma) och, ute i världen, dess låsring (grön när det valda målet är inom räckhåll) eller dess linje och explosionscirkel. En raket som är låst på **dig** får skärmkanten att blinka rött.

**Raketkastare.** En raketkastare II till V förvaras i din hangar som Auto-raket-CPU:n, behöver ingen plats och fungerar på alla skepp (den bästa du äger räknas). Ett tryck på en vanlig raket avfyrar då 2, 3, 4 eller 5 raketer ur lagret med 0,15 sekunder emellan, och sedan väntar de vanliga raketerna 5 sekunder. Monteringen tillverkar dem efter deras forskning (8 till 24 timmar, med 150 000 till 2 000 000 Thulium och material; föremålsträdet för [Extra](/wiki/06-Items/Extras.md) listar dem).

**N.U.K.E.** ritar sin explosion på kartan innan du avfyrar (cirkeln på 1 350 enheter vid den siktade punkten) och, när den detonerar, en vit blixt över vyn, en ring som löper ut till den exakta räckvidden på ungefär en sekund och blir kvar två till, ett moln som reser sig som en svamp, och en kameraskakning som är starkare ju närmare du är. **Minska skärmskakning** tar bort skakningen, och **Minska rörelser** förkortar blixten till en tredjedels sekund med mindre än hälften av dess ljus (båda finns under Inställningar › Grafik); en lägre partikelkvalitet tunnar ut molnet och tar bort gnistorna, aldrig blixten eller ringen. **N.I.K.E.** siktas som en Rivet I, med linjen från ditt skepp till markören, och spelet vägrar den aldrig för att den är långt från det svarta hålet eller på en karta utan något: vart den tar vägen är det upp till dig att bedöma. Dess kort säger **Svart hål: Ger Dark Matter** bredvid dess skada. Den lämnar ett violett spår med gnistor som slingrar sig runt det; ett skepp den möter tar träffen som av vilken raket som helst, och när den i stället korsar horisonten blossar hålet.

## Drönarformationer och raketer {#drone-formations-and-rockets}

En buren [drönarformation](/wiki/03-Mechanics/Formations.md) är det enda på ditt skepp som ändrar en raket; det andra är din egen [Raketteknik](#rocket-tech). Alla skadesiffror på den här sidan gäller ett skepp utan formation och före Raketteknik.

- **Skada.** Raketbonusen hos Ballista (+55 %), Bodkin (+29 %) och Asterism (+24 %) multiplicerar skadan hos alla 14 raketer, även N.U.K.E. och N.I.K.E. Testudos pris på all skada räknas också på raketer, och Cullers skada mot utomjordingar räknas på en raket som träffar en utomjording. Alla faktorer på en raket tillsammans stannar vid ×1,59. Bonusen räknas mot en [asteroid](/wiki/03-Mechanics/Asteroid-Mining.md#breaking-one) precis som mot ett skepp, och asteroidens pansar dras av efter den.
- **Omladdning.** Asterism gör de vanliga raketernas timer 35 % längre (4,05 sekunder), Cordon 11 % längre (3,33) och Redoubt 27 % kortare (2,19), men aldrig kortare än raketens flygning plus ett ögonblick. Under Redoubt väntar de snabba raketerna (Lancet I, Rivet I och II, Ember I, Scatter I och II) 2,19 sekunder, en Rivet III 2,3, en Lancet III 2,9 och en Ember III hela 3. Väntan bestäms när du avfyrar, så att byta formation efteråt förkortar den inte, och cirkelsektorn över raketplatserna följer den. Specialraketernas timers ändras inte av någon formation.
- **De två storas gränser står sig bara för en formation.** Med den bästa formationen träffar en N.I.K.E. med upp till 116 250, vilket en oskadad Paragon (128 000) överlever, och en N.U.K.E. med upp till 77 500, vilket en Goombah (80 000) överlever. [Raketteknik](#rocket-tech) har inget tak och höjer båda: på nivå 100 träffar en N.I.K.E. under en Ballista med upp till 151 125, mer än en oskadad Paragon har (128 000), och en N.U.K.E. med upp till 100 750 i explosionens mitt, nog för att förstöra en Goombah vid varje slumptal.
- **Undanmanöver.** Asterisms 7 % undanmanöver ger en direkt raket som träffar dig 7 % chans att inte göra någon skada alls, och ett flytande ”Miss” visas över ditt skepp; en områdesexplosion har inget sikte och undviks aldrig.
- **Genomträngning.** Gemini lägger sina 15 poäng, och Stiletto sina 35 poäng raketgenomträngning, till sköldgenomträngningen hos en direkt raket (en explosion har ingen), utan tak: en Lancet III med en Stiletto ger 70 %, med Gemini 50 %. En laserträff lägger till Geminis på samma sätt till ammunitionens och förstärkarnas, och får ingenting av Stilettos ([Lasrar och ammunition](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)).

## Raketteknik {#rocket-tech}

**Raketteknik** är en pilotförmåga: den går upp i nivå när du avfyrar raketer och träffar skepp med dem, och nivån är din på varje skepp. Den ändrar varje raket du avfyrar på två sätt.

- **Skada.** En raket gör 1,00 av sin skada på nivå 1, och talet stiger i rak linje till 1,30 på nivå 100: talet som spelet slumpade fram vid avfyringen multipliceras med det, så en träff, en explosion, en asteroid och en Energetic Wall får alla det. Formationernas gräns på ×1,59 gäller bara formationens bonus, så ingenting sätter tak för förmågan: på nivå 100 med en Ballista gör en raket 2,015 gånger sitt tal, och en N.U.K.E. når 100 750 i mitten av sin explosion, mer än en Goombah har (80 000).
- **Blindgångare.** En raket du avfyrar mot en fiende kan bli en blindgångare, med en chans på 10 % på nivå 1 som sjunker i rak linje till 1 % på nivå 100, aldrig helt till noll. En blindgångare kostar raketen, skottet och väntetiden som vilken avfyring som helst, men den flyger ingenstans: alla som ser ditt skepp ser några svaga gnistor och ett grått rökmoln vid mynningen och hör ett dovt pfft och ett klonk i stället för avfyringen, och du får veta: "Din raket blev en blindgångare." Support Rocket och Flares blir aldrig blindgångare.

## Regler {#rules}

- Du behöver **ingen monterad laser** för att avfyra en raket, och dina lasrar ändrar varken vad den gör eller hur långt den når: en målsökande raket låser på ett mål inom sin egen låsräckvidd, en rak flyger sitt eget avstånd. Utan monterad laser visar hangarens ruta Räckvidd ett streck, och bara dina raketer skjuter.
- En raket förbrukas per avfyrning, oavsett om den träffar eller inte.
- Raketer följer lasrarnas regler: inget inom en **säker zon** skadas, ingen pilot skadas innan **Fredsprotokollet** upphör eller där en sektor förbjuder PvP, och **din egen grupp skadas aldrig** av dina raketer, vare sig direktträff eller explosion. **Din egen koncern skonas inte**: där PvP är på skadar en raket en koncernkamrat på samma sätt som en laser (en låsning, en rak raket i sin bana, en explosion), och att förstöra en kostar **100 heder**. Beta och Gamma har inget fredsprotokoll: där gäller PvP från dag 1.
- Att avfyra en raket avslutar ditt eget skydd i säker zon direkt. Det är ett skott: det avslutar också ditt eget **kamouflage**, och Cloaking CPU:n laddas då om i en minut, som efter varje slut på ett kamouflage. Kamouflerad eller inte hindrar en avfyrning dig från att kamouflera dig under de 10 sekunderna efteråt (se [Extrautrustning](/wiki/06-Items/Extras.md)).
- Ett skepp som är **kamouflerat** eller inom **de 3 sekunderna av sin EMP** går inte att låsa på: en målsökande raket nekas, och en som redan flyger mot det tappar sin målfixering och flyger rakt vidare. En rak raket med enkelmål flyger igenom ett sådant skepp. En raket med **områdesskada** kräver ingen målfixering, så den skadar de skepp den täcker, kamouflerade eller inte, och den avslutar ett kamouflage (se [Extrautrustning](/wiki/06-Items/Extras.md)).
- **Ingenting begränsar vad en raket gör mot en pilot.** En annan pilots skepp tar full skada: sköldarna först (deras absorption minus raketens sköldgenomträngning), sedan skrovet. De små skeppen klarar sig inte. På standardsköldkärnorna (Light, 45 % absorption) förstör en N.I.K.E. vid varje slumptal en färsk Protos eller Kitefin med en träff. En färsk Ostirion (64 000 skrov) förlorar ungefär 95 % av sitt skrov vid det lägsta slumptalet och förstörs på den övre hälften av slumptalen; med Heavy-sköldkärnor (55 % absorption) tar en träff 84 till 94 % av skrovet och förstör den aldrig, och när skölden är nere förstörs den vid varje slumptal. En Paragon förlorar 47 till 53 % av sitt skrov, en Wraith 24 till 26 %. En N.U.K.E. förstör en Protos var som helst i sin explosion, en Kitefin inom ungefär 80 enheter från detonationen (340 vid det bästa slumptalet) och inget större i en enda explosion. Två Lancet III-raketer eller två Rivet III-raketer förstör en Protos vid varje slumptal; en Wraith tål mellan 36 och 55 av dem. Fredsprotokollet, de säkra zonerna, sektorerna utan PvP och din grupp är det som står mellan en pilot och en raket. De här siffrorna gäller ett skepp utan formation och före [Raketteknik](#rocket-tech), som multiplicerar dem med 1,00 på nivå 1 och 1,30 på nivå 100; en raketformation höjer dem med upp till 55 % (se [Drönarformationer och raketer](#drone-formations-and-rockets)).
- Bara en rakets **direktträff** paxar en utomjording (se [Strid](/wiki/03-Mechanics/Combat.md)); en explosions kant kan skada en utomjording som någon redan har paxat utan att stjäla den. Varje utomjording en explosion skadar, även en sovande, vänder sig mot dig, som vid en lasersträff (en Seeker eller en Goombah, som bara slår tillbaka, inräknade); en som explosionen missar förblir sovande.
- Timern är din: den överlever ett hopp, en återanslutning, ett skeppsbyte och ett förstört skepp.

Bara de vanliga raketerna i första tabellen, Flares och Ricochet köps (för krediter); varje annan raket tillverkas i Monteringen.

Se även: [Lasrar och ammunition](/wiki/06-Items/Lasers.md), [Strid](/wiki/03-Mechanics/Combat.md), [Det svarta hålet](/wiki/03-Mechanics/Black-Hole.md).

## EMP Charge

**EMP Charge** bär du som en raket, men den är ingen raket: den är en **förbrukningsvara**. Du köper den i butiken för **500 Thulium** per laddning och bär upp till **20** i en hög (det du har lagt ut på [Auktionen](/wiki/03-Mechanics/Auction.md) räknas med), och snabbfältets val **Förbrukningsvaror** visar den med antalet du bär. Den tar **ingen plats** på något skepp; fram till 0.4.21 var den [extrautrustning](/wiki/06-Items/Extras.md) och varje laddning fyllde en extraplats. En laddning väger 250 i transportförrådet.

Tryck på platsen EMP under en strid. I **3 sekunder** kan ingen låsa på dig, och **alla som var låsta på dig förlorar låsningen** direkt, var de än är: piloter, utomjordingar och koncernpiloter. En pilot vars målfixering bryts får veta ”Målfixering förlorad: målet använde en EMP”. Den som försöker låsa på under de 3 sekunderna nekas.

- **Det är inte osårbarhet.** Den stoppar det som kräver en målfixering: lasrar, målsökande raketer och beröringen från en rak raket med enkelmål, som flyger rakt igenom dig. En raket med **områdesskada** kräver ingen målfixering, så den skadar dig ändå om du är inom den, och det svarta hålet är inte ett skott alls.
- **Du kan fortfarande agera.** Att skjuta avslutar den inte. Du kan kamouflera dig (om kamouflagets egna regler tillåter det) och använda annan extrautrustning.
- **Den avslutar kamouflage i närheten.** Varje skepp som är kamouflerat inom **1 500 enheter** från dig när pulsen går av syns direkt och dess CPU börjar sina 60 sekunders omladdning, oavsett vilken koncern det tillhör, din egen inräknad; skeppen i din egen [grupp](/wiki/03-Mechanics/Groups.md) är undantaget: de behåller sitt kamouflage. Piloten får veta ”Kamouflage bruten: en EMP utlöstes i närheten.”, ser skeppet dyka upp igen med samma krusning som vid varje annat avslöjande, och platsen börjar sin omladdning. Du kan inte använda en EMP medan du själv är kamouflerad.
- **Den döljer ingenting.** Alla ser dig fortfarande, med ett knitrande elektriskt skal under de 3 sekunderna.
- **Du kan inte använda den** medan en säker zon skyddar dig, medan du är kamouflerad eller inom **30 sekunder** efter den förra. Den fungerar överallt annars, även de första dagarna av en säsong (Fredsprotokollet): utomjordingar jagar fortfarande då.
- En utomjording du träffar under de 3 sekunderna vänder sig inte mot dig förrän de är över. Dina pax och reglerna om första träffen ändras inte.
- **Vad du ser.** En puls av böjt rum rusar ut från piloten så långt som pulsen avslutar kamouflage (1 500 enheter), alla inom räckhåll ser den, och ett knitrande elektriskt skal omger skeppet under de 3 sekunderna, med en ring runt ditt eget skepp och en bricka högst upp på skärmen som räknar tiden. Målringen hos alla som hade valt dig bryts sönder, med ett kort knäpp. Platsen EMP visar de laddningar du äger, lyser blått medan skalet är uppe och mörknar medan den laddas om.
- **Ett tryck, en laddning.** Ett tryck förbrukar en laddning ur din hög; finns ingen kvar nekas det (”Inga EMP Charge kvar.”). Laddningar i transportförrådet hör till nästa säsong och kan inte användas. Till skillnad från de tolv raketerna, av vilka 1 000 av varje följer med av sig själva, går laddningarna du bär förlorade med säsongen om du inte lägger dem i transportförrådet. De **30 sekunderna** av omladdning sparas inte: att logga ut eller hoppa genom en portal nollställer dem, och nästa puls kostar en laddning.
