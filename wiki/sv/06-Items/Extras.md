<!-- wiki-i18n source: d73343b5c426be4e -->
<!-- wiki-i18n title: Extrautrustning -->
# Extrautrustning {#extras}

Extrautrustning är de prylar som sitter i ett skepps **extraplatser** (två på Protos, Kitefin, Ostirion och Nomad, skeppen du börjar med eller köper, och tre på Paragon, Ironclad, Wraith och Storm, skeppen du tillverkar, per konfiguration, och 3, 5 eller 7 fler med Extra Slots CPU). Du slår på en från väljaren Extra i snabbfältet eller från en snabbfältsplats du lagt den på. De fungerar bara från den konfiguration du flyger: monterar du en i den andra konfigurationen väntar den tills du byter.

| Extra | Vad den gör | Användningar | Pris |
| :---- | :---------- | :----------- | :--- |
| **Repair Drone I till IV** | Reparerar ditt skrov, 1,5 %, 2,25 %, 3,5 % och 5 % av maxvärdet per sekund | obegränsat | 5 000 / 15 000 / 35 000 krediter, 2 000 Thulium |
| **Cloaking CPU S** | Döljer ditt skepp | 10 | 5 000 Thulium |
| **Cloaking CPU M** | Döljer ditt skepp | 25 | 11 250 Thulium |
| **Cloaking CPU L** | Döljer ditt skepp | 50 | 20 000 Thulium |
| **P.E.T. Station I till III** | När den är PÅ ger 2, 3 eller 5 dockade [P.E.T.s](/wiki/03-Mechanics/Pets.md#the-station) boosts åt ditt skepp, samlar erfarenhet och arbetar; när den är AV gör de inget av det | PÅ / AV | Monteringen, efter sin forskning (föremålsträdet nedan) |

Cloaking CPU säljs bara i butiken. De kan inte slås ihop, och ingenting ger dig dem gratis. **EMP Charge** är inte längre extrautrustning: sedan 0.4.21 är den en förbrukningsvara som bärs i en hög, som en raket, och inte sätts i någon plats, så den tar ingen av dina extraplatser (se [Raketer](/wiki/06-Items/Rockets.md#emp-charge)). De två **Energetic Wall** är inte heller extrautrustning längre: sedan 0.4.22 är de förbrukningsvaror också, bärs i en hög och sätts inte i någon plats (se [Energetic Wall](#energetic-wall)).

En ny pilots **startpaket** monterar redan två extrautrustningar på Protos två extraplatser: en **Base CPU I** (10 användningar, en teleport till din koncerns bas) och en **Repair Drone I**. Dra dem från väljaren Extra i snabbfältet till en plats för att använda dem. Bara nya piloter får paketet: den som tog värvning före 0.4.10 har det inte.

Sju CPU:er till säljs inte: Monteringen tillverkar dem när Skylabs forskningscentrum har forskat fram dem (se [Forskning](/wiki/03-Mechanics/Research.md)). De är Extra Slots CPU I, II och III, Jump CPU, Base CPU I och II samt Auto-Repair CPU, och [det sista avsnittet](#research-cpus) säger vad var och en gör. Liksom Cloaking CPU är Jump CPU och Base CPU till för ett lugnt ögonblick: ingen av de tre startar inom 10 sekunder efter ett skott du skjuter eller en träff du får. De två warp-CPU:erna, Jump CPU och Base CPU, nekas också medan du bär på ett uppdragsföremål (”Du kan inte använda en warp-CPU medan du bär på ett uppdragsföremål.”): se [Uppdragsföremål](/wiki/03-Mechanics/Quests.md#quest-items).

Varje extra har en kort etikett på sin plats i snabbfältet: **REP** för en Repair Drone, **CLK** för en Cloaking CPU och **ARP**, **BSE** och **JMP** för Auto-Repair CPU, Base CPU och Jump CPU. Förbrukningsvaror har egna: **EMP** och **WAL** (för en Energetic Wall). Extra Slots CPU har ingen plats: de installeras i din Skylab. De tre **P.E.T. Station**-föremålen är extrautrustning som den andra, med etiketten **PET**: montera ett, så slår dess plats om Stationen **PÅ** eller **AV** (en sekund mellan två tryck) och visar vilket. När den är PÅ räknas de dockade [P.E.T.s](/wiki/03-Mechanics/Pets.md), när den är AV räknas de inte. Peka på en plats för att läsa vad ett tryck gör just nu, eller varför det inte kan.

![The Extras picker of the hotbar: the Repair Drone, the Auto-Repair, Cloaking, Base and Jump CPUs and the P.E.T. Station you have fitted (REP, ARP, CLK, BSE, JMP, PET), to drag onto a slot](../../img/wiki-img/shots/cpu-hotbar.jpg)
![The Consumables picker of the hotbar: the EMP Charge and the Energetic Wall I and II (EMP, WAL) to drag onto a slot, with how many of each you hold](../../img/wiki-img/shots/emp-hotbar.jpg)
![The hotbar with extras on its slots: a Repair Drone, a Cloaking CPU with its uses left, the P.E.T. Station that says ON, the EMP Charge and the Energetic Wall I and II with the number of each you carry](../../img/wiki-img/shots/hotbar-slots.jpg)
![The Repair Drone of an extra slot docked to its ship and its wingmen](../../img/wiki-img/shots/repair-drones-extra.jpg)
![The Shop's Consumables category: the EMP Charge and the Energetic Wall I with their prices in Thulium, and the Energetic Wall II, which only Assembly makes](../../img/wiki-img/shots/shop-consumables.jpg)

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Föremålsträd {#item-tree}

Det som Monteringen tillverkar kräver först sin teknologi; håll pekaren över ett föremål för att se hur lång tid forskningen tar. Teknologiträdet, bränslet och boosten: [Forskning](/wiki/03-Mechanics/Research.md).

```tree
P.E.T. Station I | extra, common | craft 100000 Credits, 2000 Thulium, 300 s | research 10800 s, 10800 science | 25 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md
Cloaking CPU S | extra, common | buy 5000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Repair Drone I | extra, common | buy 5000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone II | extra, common | buy 15000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone III | extra, common | buy 35000 Credits | /wiki/06-Items/Extras.md#repair-drones
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
P.E.T. Station II | extra, uncommon | craft 400000 Credits, 6000 Thulium, 600 s | research 36000 s, 36000 science | 60 Ship Fragment, 6 Reinforced Hull Plate, 4 Power Core, 8 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md
Cloaking CPU M | extra, uncommon | buy 11250 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 2 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Extras.md#base-cpus
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu
P.E.T. Station III | extra, rare | craft 1500000 Credits, 18000 Thulium, 900 s | research 86400 s, 86400 science | 120 Ship Fragment, 12 Reinforced Hull Plate, 8 Power Core, 2 Ancient Control Unit, 12 Velkonite Reinforced Plate, 4 Orvium Reinforced Plate | /wiki/06-Items/Extras.md
Repair Drone IV | extra, rare | buy 2000 Thulium | /wiki/06-Items/Extras.md#repair-drones
Cloaking CPU L | extra, rare | buy 20000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 6 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu

P.E.T. Station I -> P.E.T. Station II -> P.E.T. Station III
Cloaking CPU S -> Cloaking CPU M -> Cloaking CPU L
Repair Drone I -> Repair Drone II -> Repair Drone III -> Repair Drone IV
Extra Slots CPU I -> Extra Slots CPU II -> Extra Slots CPU III
Base CPU I -> Base CPU II
```
<!-- item-tree:end -->

## Repair Drones

Slå på en Repair Drone (REP) så reparerar den skrovet tills det är fullt. Den startar först efter 10 sekunder utan träff, och varje träff stänger av den. Är flera monterade arbetar den bästa. En [Auto-Repair CPU](#auto-repair-cpu) slår på den igen åt dig. Takterna finns i [Strid](/wiki/03-Mechanics/Combat.md). Medan den lagar flyger små reparationsdrönare ut ur skeppet, cirklar runt det och riktar strålar mot skrovet, en för en Repair Drone I, två för en II, tre för en III eller IV, och piloter i närheten ser dem; de dockar igen när reparationen upphör.

## Cloaking CPU

Tryck på platsen CLK för att kamouflera dig. **Ett tryck är en användning**, oavsett paket, och du ser de kvarvarande användningarna på platsen och i hangaren. Ett kamouflage har **ingen tidsgräns**: det ligger kvar tills du stänger av det eller något bryter det.

- **Vem som inte kan se dig.** Andra koncerners piloter och utomjordingar ser inte ditt skepp alls: det finns varken på deras skärm eller i deras mållista, och ingen kan låsa på det. Andra koncerners koncernpiloter ignorerar det också.
- **Radarprickan.** Alla andra piloter på kartan, utom din egen koncern, ser en enkel **röd prick** på minikartan där du befinner dig, så att de vet att någon kamouflerad är i närheten. Pricken har varken namn, skepp, koncern eller id och går inte att klicka på eller välja som mål; när man pekar på den står det bara ”Något är kamouflerat här”. Den är rund, inuti en ring (skepp på minikartan är kvadrater), och ringen andas långsamt, eller står stilla om du har slagit på Minska rörelser. Servern uppdaterar den ungefär två gånger i sekunden och ditt spel flyttar den mjukt däremellan. Den säger att någon finns där och var, inte vem: en pilot som såg dig kamouflera dig kan följa pricken, och en **raketexplosion** riktad mot den hittar dig ändå.
- **Vem som kan se dig.** Du ser ditt eget skepp, svagt, med en kontur. Piloter i din koncern ser dig som ett blekt spöke; klankamrater från andra koncerner gör det inte, eftersom en klan tar emot vem som helst som ansöker. Ingen kan välja spöket som mål, inte ens din koncern.
- **Du kan inte kamouflera dig** i en säker zon, medan CPU:n laddas om eller inom **10 sekunder** efter att du blivit träffad eller avlossat ett skott.
- **Vad som avslutar det.** Att trycka på platsen igen, din första salva eller raket (den träffar, och du syns), att gå in i en säker zon, att CPU:n lämnar den konfiguration du flyger, en **EMP som utlöses inom 1 500 enheter** från dig, vem som än avfyrade den (din egen koncerns också, men inte en gruppmedlems), och områdesskadan från en raket som träffar dig. Tid gör det inte, att plocka upp last gör det inte (en låda du tar är borta för alla, så de får veta att något fanns inom räckhåll för den platsen, inte vem), förmågor gör det inte, och det svarta hålets strålning skadar ett kamouflerat skepp men avslutar inte dess kamouflage. Att logga ut eller dö avslutar det, eftersom ett skepp som inte flygs inte är kamouflerat.
- **Omladdning.** När ett kamouflage tar slut, hur det än tog slut, laddas CPU:n om i **60 sekunder**. Omladdningen tillhör dig, inte skeppet: den fortsätter om du hoppar genom en portal, loggar ut eller dör. Varje tryck kostar fortfarande en användning.
- **Utomjordingar** som var ute efter dig tappar dig. Dina pax släpps när du kamouflerar dig.
- **Raketer.** Ingen kan låsa en målsökande raket på dig, och en rak raket med enkelmål flyger rakt igenom dig. En raket med **områdesskada** skadar ändå ett skepp som ligger inom den och avslutar dess kamouflage, och de piloter som kan se skeppets plats får se den innan skadesiffran visas. Att avfyra en raket är ett skott: det avslutar ditt eget kamouflage på samma sätt som en salva (CPU:n laddas då om i de 60 sekunder som nämns ovan) och hindrar dig, kamouflerad eller inte, från att kamouflera dig under 10 sekunder efteråt.
- **Det svarta hålet** sväljer ett kamouflerat skepp som vilket annat som helst, och kartan får veta det.
- **Vad du ser.** Ditt skepp blir genomskinligt med en streckad violett kontur, dess drönare tonas ned med det, och en bricka högst upp på skärmen säger ”Kamouflerad” med de kvarvarande användningarna (inga sekunder: det finns ingen timer). Platsen CLK visar de kvarvarande användningarna; medan du är kamouflerad lyser den violett och säger PÅ, och när kamouflaget tar slut, hur det än tog slut, mörknar den och räknar de 60 sekundernas omladdning. Ett tryck som servern nekar (omladdning, en säker zon, en träff eller ett skott de senaste 10 sekunderna) får platsen att blinka rött, och ett meddelande berättar varför. En allierad syns som ett blekt spöke med en spökmarkering före sitt namn, och en pilot som kamouflerar sig nära dig försvinner i en krusning. Dra CLK från Extra i snabbfältet till en plats för att använda den, precis som REP.
- **Användningarna** sparas med CPU:n. Att logga ut, dö eller starta om spelet ger inga tillbaka, och en aktivering du avbryter är ändå förbrukad. När ett pakets sista användning är slut är det förbrukat, och dess plats fylls på från en reserv av samma CPU i ditt inventarie, om du äger någon.
- **Flera CPU:er** i en konfiguration läggs inte ihop. Den med minst antal användningar kvar används först.

S, M och L fungerar likadant: de större paketen är bara billigare per användning (500, 450 och 400 Thulium).

## Energetic Wall

Tryck på platsen WAL, så står en **plasmavägg** **vid din markör**, tvärs över linjen från ditt skepp dit: ett band som är 360 enheter långt (ungefär tre och en halv skeppsmodeller) och 10 enheter brett. Dess mitt ligger högst **450 enheter** från skeppets mitt: en markör längre bort sätter den 450 enheter ut längs linjen, en markör närmare än 120 enheter flyttar ut den till 120. Medan platsen är redo visar en svag prickad linje och en spökkontur var den kommer att stå. Vet spelet inte var din markör är, står den 220 enheter framför skeppets mitt, tvärs över dess kurs. En Energetic Wall är en **förbrukningsvara**, som [EMP Charge](/wiki/06-Items/Rockets.md#emp-charge): en hög i ditt inventarie som inte tar **någon plats** på något skepp (fram till 0.4.22 var den extrautrustning). Dra den från snabbfältets Förbrukningsvaror till en plats för att använda den; de två nivåerna är två poster, så en plats rymmer en nivå. Den är till för att gömma sig bakom och för att spärra en fil, inte för att stå i.

- **Vad den stoppar.** Varje skott som korsar den träffar väggen i stället, vem som än sköt det och från vilken sida: en lasersalva, en raket, en utomjordings salva. Det som står bakom tar ingenting och väggens livspoäng tar skadan. Explosionen från en raket som går av vid väggen träffar skeppen på dess nära sida och inte de bakom den. Dina egna skott också: du kan inte skjuta ut genom din egen vägg. N.I.K.E. och Dormant Swamps kanontorn flyger över den, som de flyger över asteroider.
- **Vad den bränner.** Varje skepp vars skrov rör vid bandet tar **2 500 i skada per sekund**, först på skölden, ditt eget också, och utomjordingar och koncernpiloter. Ett skepp i en säker zon eller under skydd av en återkomst brinner inte, och två band på ett skepp läggs inte ihop.
- **Hur länge den håller.** En vägg på nivå 1 har **30 000 livspoäng**, en på nivå 2 **90 000**. En vägg förlorar en sextiondel av dem varje sekund av sig själv, så en som ingen skjuter på är borta efter **60 sekunder**. Skott förkortar det: en Wraith med tolv Helios Beam på x4-ammunition fäller en nivå 1-vägg på ungefär 3,5 sekunder.
- **En i taget, en vägg per tryck.** En ny vägg tar den gamlas plats. Efter ett tryck laddas föremålet i **90 sekunder**; väntan är din, inte skeppets: att dö eller logga ut förkortar den inte. Ett tryck förbrukar **en vägg av den nivå platsen rymmer**, och bara när väggen står: ett tryck som spelet nekar (nedan) förbrukar ingenting och startar ingen väntan. Finns ingen kvar av den nivån säger det ”Inga Energetic Wall kvar.”, och den andra nivån förbrukas aldrig i dess ställe.
- **Var inte.** Inte medan en säker zon eller en återkomst skyddar dig, inte där bandet skulle röra en säker zon eller en port, inte kamouflerad och inte där bandets mitt skulle hamna utanför kartan. Spelet säger vilket fall det är.
- **Nedskjutningar.** Ett skepp som väggen förstör dör av strålning, och nedskjutningen går till den sista fientliga piloten som träffade det inom 15 sekunder, om det fanns någon. Den som satte upp väggen får inget tillgodo för det den inte sköt själv. En utomjording som väggen förstör betalar ingenting: ingen belöning, inget byte.
- **Utomjordingar går inte runt den.** De flyger igenom och brinner, eller blir stående på sin sida och skjuter på väggen.
- **Vad du ser.** Ett band av blåvitt ljus med ljusa streck som löper längs det och en ljuspelare i varje ände; det blixtrar där ett skott slår in och flimrar när det nästan är slut. En vägg på nivå 2 lyser i stället gult, med en tjockare, ljusare kärna och ett starkare sken, men dess band är lika brett som på nivå 1: 10 enheter. En tunn livsmätare bredvid blir kortare och går över i bärnsten och sedan rött; din plats visar väggens återstående liv som en båge och väntan som en skugga. En uppsatt vägg blixtrar till, en nedskjuten rasar i gnistor och en vars tid gått ut bleknar bort. Siffran på platsen räknar också de väggar av dess nivå som du har kvar.
- **Hur du får den och bär den.** Energetic Wall I säljs i butiken för **250 Thulium** per vägg, och du bär upp till **20** i en hög (det du har lagt ut på [Auktionen](/wiki/03-Mechanics/Auction.md) räknas med). Energetic Wall II tillverkas i Monteringen, **en vägg per tillverkning**, för **600 Thulium**, 5 Ship Fragments och en Power Core, när Forskningscentrumet har forskat fram den (6 timmar i normal takt: [Forskning](/wiki/03-Mechanics/Research.md)); av den bär du upp till **10**. Som raketer går väggarna du bär förlorade med säsongen om du inte lägger dem i transportförrådet, och väggar i förrådet kan inte användas. En Energetic Wall II som du har tillverkat kan säljas på Auktionen; en Energetic Wall I, som butiken säljer, aldrig.

## Forskningscentrumets CPU:er {#research-cpus}

Två av CPU:erna kräver Dark Matter Plates, liksom sista nivån i varje uppgraderingskedja: **Extra Slots CPU III** kräver 4 (plus 2 Ancient Control Units och 6 Orvium Reinforced Plates) och **Base CPU II** 4 (plus en Ancient Control Unit och 2 Orvium Reinforced Plates), så forska först fram Dark Matter Plate ([Dark Matter och Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)).

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | Forskningstid | Kräver först | Thulium för tillverkning | Tillverkningstid |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 min | – | 12 000 | 5 min |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10 h | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 000 | 10 min |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1 d | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75 000 | 15 min |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3 h | – | 8 000 | 5 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10 h | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | 20 000 | 10 min |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1 d | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40 000 | 15 min |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6 h | – | 15 000 | 10 min |
| [Energetic Wall II](/wiki/06-Items/Extras.md#energetic-wall) | 6 h | – | 600 | 2 min |

Ingen av dem säljs i butiken: forska fram teknologin och tillverka sedan CPU:n i Monteringen. Håll pekaren över en CPU i trädet för att se vad Monteringen kräver för den.

### Extra Slots CPUs

- **Vad de gör.** Extra Slots CPU I, II och III ger varje skepp 3, 5 och 7 extraplatser till, alltså 6, 8 och 10 sammanlagt på ett skepp som har 3 egna och 5, 7 och 9 på ett som har 2. En högre CPU ersätter den förra: II läggs inte till I.
- **Installeras, bärs inte.** En Extra Slots CPU är inte ett föremål: när du hämtar den i Monteringen installerar den sig i din Skylab, för varje skepp i båda konfigurationerna, och tar ingen plats. Den finns kvar efter wipen.
- **I ordning.** Tillverka dem en efter en: II först när I är installerad, III först när II är installerad; till dess säger Monteringen vilken du ska installera först. De tre kostar 117 000 Thulium sammanlagt: 12 000, 30 000 och 75 000.

### Jump CPU

- **Vad den gör.** Den hoppar ditt skepp till vilken koncernsektor som helst i din värld, både din egen koncerns och de andras, hemsektorerna inräknade (`M`, `T` och `G`, sektor 1 till 4), för **500 Thulium** per hopp. Antalet användningar är obegränsat: du betalar bara Thulium. Den leder aldrig till en farosektor (`DS`) eller en neutral sektor (`N`).
- **Hoppet.** Tryck på platsen JMP, välj sektorn på kartan Stjärnsystem och bekräfta: skeppet laddar i 5 sekunder och kommer sedan fram vid en port i den sektorn, skyddat som efter ett hopp genom en port. CPU:n svalnar i 30 sekunder efter att du har kommit fram.
- **Inte i strid.** Den kan inte starta inom 10 sekunder efter ett skott eller en träff, och ett skott eller en träff under laddningen avbryter hoppet; då betalas inget. Du kan inte hoppa kamouflerad.
- **Inte från en neutral sektor:** en pilot i en neutral sektor, eller utan koncern, kan inte använda den.
- Den får lämna en farosektor när du inte är i strid.

### Base CPUs

- **Vad de gör.** De teleporterar ditt skepp till din koncerns bas, in i den säkra zonen runt dess station (`M-1`, `T-1` eller `G-1`, sektorn med Mission Control), utan Thulium-kostnad. Du startar dem från platsen BSE i snabbfältet.
- **Inte i strid.** En laddning på 10 sekunder, samma för båda. Den kan inte starta inom 10 sekunder efter ett skott eller en träff, inte medan du är kamouflerad och inte när du redan är inne i den säkra zonen vid din bas, och ett skott eller en träff under laddningen avbryter den.

| CPU | Användningar | Nedkylning |
| :--- | ---: | ---: |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 10 | 10 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 25 | 5 min |

- **Förbrukas, laddas inte om.** Varje användning tar en av CPU:ns användningar, och en CPU utan användningar kvar är borta: tillverka en ny. Är båda monterade används den bättre (II) först.

### Auto-Repair CPU

- **Vad den gör.** Den skickar ut den Repair Drone som sitter i dina extraplatser av sig själv, så fort du hade kunnat skicka ut den för hand: ditt skrov är inte fullt, drönaren är inte redan ute och det har gått 10 sekunder sedan den senaste träffen. Det finns ingen skrovnivå att ställa in.
- Den tar en egen extraplats och gör ingenting utan en Repair Drone i en extraplats i samma konfiguration. Den skickar aldrig ut en Repair Drone i en förmågeplats (den är knappen Emergency Repair).
- **Stoppar du drönaren för hand** låter CPU:n den vara tills ditt skrov är fullt igen, eller tills du själv skickar ut drönaren.


<!-- research-cpus:end -->
