<!-- wiki-i18n source: 1855960bc32d6626 -->
<!-- wiki-i18n title: Extrautrustning -->
# Extrautrustning {#extras}

Extrautrustning är de prylar som sitter i ett skepps **extraplatser** (två på Protos, Kitefin, Ostirion och Nomad, skeppen du börjar med eller köper, och tre på Paragon, Ironclad, Wraith och Storm, skeppen du tillverkar, per konfiguration, och 3, 5 eller 7 fler med Extra Slots CPU). Du slår på en från väljaren Extra i snabbfältet eller från en snabbfältsplats du lagt den på. De fungerar bara från den konfiguration du flyger: monterar du en i den andra konfigurationen väntar den tills du byter.

| Extra | Vad den gör | Användningar | Pris |
| :---- | :---------- | :----------- | :--- |
| **Repair Drone I till IV** | Reparerar ditt skrov, 1,5 %, 2,25 %, 3,5 % och 5 % av maxvärdet per sekund | obegränsat | 5 000 / 15 000 / 35 000 krediter, 2 000 Thulium |
| **Cloaking CPU S** | Döljer ditt skepp | 10 | 5 000 Thulium |
| **Cloaking CPU M** | Döljer ditt skepp | 25 | 11 250 Thulium |
| **Cloaking CPU L** | Döljer ditt skepp | 50 | 20 000 Thulium |
| **EMP Charge** | I 3 sekunder kan ingen välja dig som mål, varje målfixering på dig bryts och allt kamouflage i närheten tar slut | 1 | 500 Thulium |

Cloaking CPU och EMP Charge säljs bara i butiken. De kan inte slås ihop, och ingenting ger dig dem gratis.

En ny pilots **startpaket** monterar redan två extrautrustningar på Protos två extraplatser: en **Base CPU I** (10 användningar, en teleport till din koncerns bas) och en **Repair Drone I**. Dra dem från väljaren Extra i snabbfältet till en plats för att använda dem. Bara nya piloter får paketet: den som tog värvning före 0.4.10 har det inte.

Sju CPU:er till säljs inte: Monteringen tillverkar dem när Skylabs forskningscentrum har forskat fram dem (se [Forskning](/wiki/03-Mechanics/Research.md)). De är Extra Slots CPU I, II och III, Jump CPU, Base CPU I och II samt Auto-Repair CPU, och [det sista avsnittet](#research-cpus) säger vad var och en gör. Liksom Cloaking CPU är Jump CPU och Base CPU till för ett lugnt ögonblick: ingen av de tre startar inom 10 sekunder efter ett skott du skjuter eller en träff du får. De två warp-CPU:erna, Jump CPU och Base CPU, nekas också medan du bär på ett uppdragsföremål (”Du kan inte använda en warp-CPU medan du bär på ett uppdragsföremål.”): se [Uppdragsföremål](/wiki/03-Mechanics/Quests.md#quest-items).

Varje extra har en kort etikett på sin plats i snabbfältet: **REP** för en Repair Drone, **CLK** för en Cloaking CPU, **EMP** för EMP Charge och **ARP**, **BSE** och **JMP** för Auto-Repair CPU, Base CPU och Jump CPU. Extra Slots CPU har ingen plats: de installeras i din Skylab. Peka på en plats för att läsa vad ett tryck gör just nu, eller varför det inte kan.

![The Extras picker of the hotbar: Cloaking, Base and Jump CPUs to drag onto a slot](../../img/wiki-img/shots/cpu-hotbar.jpg)
![The Repair Drone of an extra slot docked to its ship and its wingmen](../../img/wiki-img/shots/repair-drones-extra.jpg)

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Föremålsträd {#item-tree}

Det som Monteringen tillverkar kräver först sin teknologi; håll pekaren över ett föremål för att se hur lång tid forskningen tar. Teknologiträdet, bränslet och boosten: [Forskning](/wiki/03-Mechanics/Research.md).

```tree
Cloaking CPU S | extra, common | buy 5000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Repair Drone I | extra, common | buy 5000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone II | extra, common | buy 15000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone III | extra, common | buy 35000 Credits | /wiki/06-Items/Extras.md#repair-drones
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
EMP Charge | extra, uncommon | buy 500 Thulium | /wiki/06-Items/Extras.md#emp-charge
Cloaking CPU M | extra, uncommon | buy 11250 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 8 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu
Repair Drone IV | extra, rare | buy 2000 Thulium | /wiki/06-Items/Extras.md#repair-drones
Cloaking CPU L | extra, rare | buy 20000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 20 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu

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
- **Vad du ser.** Ditt skepp blir genomskinligt med en streckad violett kontur, och en bricka högst upp på skärmen säger ”Kamouflerad” med de kvarvarande användningarna (inga sekunder: det finns ingen timer). Platsen CLK visar de kvarvarande användningarna; medan du är kamouflerad lyser den violett och säger PÅ, och när kamouflaget tar slut, hur det än tog slut, mörknar den och räknar de 60 sekundernas omladdning. Ett tryck som servern nekar (omladdning, en säker zon, en träff eller ett skott de senaste 10 sekunderna) får platsen att blinka rött, och ett meddelande berättar varför. En allierad syns som ett blekt spöke med en spökmarkering före sitt namn, och en pilot som kamouflerar sig nära dig försvinner i en krusning. Dra CLK från Extra i snabbfältet till en plats för att använda den, precis som REP.
- **Användningarna** sparas med CPU:n. Att logga ut, dö eller starta om spelet ger inga tillbaka, och en aktivering du avbryter är ändå förbrukad. När ett pakets sista användning är slut är det förbrukat, och dess plats fylls på från en reserv av samma CPU i ditt inventarie, om du äger någon.
- **Flera CPU:er** i en konfiguration läggs inte ihop. Den med minst antal användningar kvar används först.

S, M och L fungerar likadant: de större paketen är bara billigare per användning (500, 450 och 400 Thulium).

## EMP Charge

Tryck på platsen EMP under en strid. I **3 sekunder** kan ingen låsa på dig, och **alla som var låsta på dig förlorar låsningen** direkt, var de än är: piloter, utomjordingar och koncernpiloter. En pilot vars målfixering bryts får veta ”Målfixering förlorad: målet använde en EMP”. Den som försöker låsa på under de 3 sekunderna nekas.

- **Det är inte osårbarhet.** Den stoppar det som kräver en målfixering: lasrar, målsökande raketer och beröringen från en rak raket med enkelmål, som flyger rakt igenom dig. En raket med **områdesskada** kräver ingen målfixering, så den skadar dig ändå om du är inom den, och det svarta hålet är inte ett skott alls.
- **Du kan fortfarande agera.** Att skjuta avslutar den inte. Du kan kamouflera dig (om kamouflagets egna regler tillåter det) och använda annan extrautrustning.
- **Den avslutar kamouflage i närheten.** Varje skepp som är kamouflerat inom **1 500 enheter** från dig när pulsen går av syns direkt och dess CPU börjar sina 60 sekunders omladdning, oavsett vilken koncern det tillhör, din egen inräknad; skeppen i din egen [grupp](/wiki/03-Mechanics/Groups.md) är undantaget: de behåller sitt kamouflage. Piloten får veta ”Kamouflage bruten: en EMP utlöstes i närheten.”, ser skeppet dyka upp igen med samma krusning som vid varje annat avslöjande, och platsen börjar sin omladdning. Du kan inte använda en EMP medan du själv är kamouflerad.
- **Den döljer ingenting.** Alla ser dig fortfarande, med ett knitrande elektriskt skal under de 3 sekunderna.
- **Du kan inte använda den** medan en säker zon skyddar dig, medan du är kamouflerad eller inom **30 sekunder** efter den förra. Den fungerar överallt annars, även de första dagarna av en säsong (Fredsprotokollet): utomjordingar jagar fortfarande då.
- En utomjording du träffar under de 3 sekunderna vänder sig inte mot dig förrän de är över. Dina pax och reglerna om första träffen ändras inte.
- **Vad du ser.** En puls av böjt rum rusar ut från piloten så långt som pulsen avslutar kamouflage (1 500 enheter), alla inom räckhåll ser den, och ett knitrande elektriskt skal omger skeppet under de 3 sekunderna, med en ring runt ditt eget skepp och en bricka högst upp på skärmen som räknar tiden. Målringen hos alla som hade valt dig bryts sönder, med ett kort knäpp. Platsen EMP visar de laddningar du äger, lyser blått medan skalet är uppe och mörknar medan den laddas om.
- **En laddning, en användning.** Platsen fylls på från ditt inventarie när du äger fler. De **30 sekunderna** av omladdning sparas inte: att logga ut eller hoppa genom en portal nollställer dem, och nästa puls kostar en laddning.

## Forskningscentrumets CPU:er {#research-cpus}

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | Forskningstid | Kräver först | Thulium för tillverkning | Tillverkningstid |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 min | – | 12 000 | 5 min |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10 h | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 000 | 10 min |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1 d | [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75 000 | 15 min |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3 h | – | 8 000 | 5 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10 h | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 20 000 | 10 min |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1 d | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40 000 | 15 min |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6 h | – | 15 000 | 10 min |

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
