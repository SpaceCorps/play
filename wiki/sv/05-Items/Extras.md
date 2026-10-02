<!-- wiki-i18n source: 46436d9c65bc6c7e -->
<!-- wiki-i18n title: Extrautrustning -->
# Extrautrustning {#extras}

Extrautrustning är de prylar som sitter i ett skepps **extraplatser** (tre på varje skepp, per konfiguration). Du slår på en från väljaren Extra i snabbfältet eller från en snabbfältsplats du lagt den på. De fungerar bara från den konfiguration du flyger: monterar du en i den andra konfigurationen väntar den tills du byter.

| Extra | Vad den gör | Användningar | Pris |
| :---- | :---------- | :----------- | :--- |
| **Repair Drone I till IV** | Reparerar ditt skrov, 1,5 %, 2,25 %, 3,5 % och 5 % av maxvärdet per sekund | obegränsat | 5 000 / 15 000 / 35 000 krediter, 2 000 Thulium |
| **Cloaking CPU S** | Döljer ditt skepp | 10 | 5 000 Thulium |
| **Cloaking CPU M** | Döljer ditt skepp | 25 | 11 250 Thulium |
| **Cloaking CPU L** | Döljer ditt skepp | 50 | 20 000 Thulium |
| **EMP Charge** | I 3 sekunder kan ingen välja dig som mål, varje målfixering på dig bryts och allt kamouflage i närheten tar slut | 1 | 500 Thulium |

Cloaking CPU och EMP Charge säljs bara i butiken. De kan inte slås ihop, och ingenting ger dig dem gratis.

## Repair Drones {#repair-drones}

Slå på en Repair Drone (REP) så reparerar den skrovet tills det är fullt. Den startar först efter 10 sekunder utan träff, och varje träff stänger av den. Är flera monterade arbetar den bästa. Takterna finns i [Strid](/wiki/03-Mechanics/Combat.md).

## Cloaking CPU {#cloaking-cpu}

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

## EMP Charge {#emp-charge}

Tryck på platsen EMP under en strid. I **3 sekunder** kan ingen låsa på dig, och **alla som var låsta på dig förlorar låsningen** direkt, var de än är: piloter, utomjordingar och koncernpiloter. En pilot vars målfixering bryts får veta ”Målfixering förlorad: målet använde en EMP”. Den som försöker låsa på under de 3 sekunderna nekas.

- **Det är inte osårbarhet.** Den stoppar det som kräver en målfixering: lasrar, målsökande raketer och beröringen från en rak raket med enkelmål, som flyger rakt igenom dig. En raket med **områdesskada** kräver ingen målfixering, så den skadar dig ändå om du är inom den, och det svarta hålet är inte ett skott alls.
- **Du kan fortfarande agera.** Att skjuta avslutar den inte. Du kan kamouflera dig (om kamouflagets egna regler tillåter det) och använda annan extrautrustning.
- **Den avslutar kamouflage i närheten.** Varje skepp som är kamouflerat inom **1 500 enheter** från dig när pulsen går av syns direkt och dess CPU börjar sina 60 sekunders omladdning, oavsett vilken koncern det tillhör, din egen inräknad; skeppen i din egen [grupp](/wiki/03-Mechanics/Groups.md) är undantaget: de behåller sitt kamouflage. Piloten får veta ”Kamouflage bruten: en EMP utlöstes i närheten.”, ser skeppet dyka upp igen med samma krusning som vid varje annat avslöjande, och platsen börjar sin omladdning. Du kan inte använda en EMP medan du själv är kamouflerad.
- **Den döljer ingenting.** Alla ser dig fortfarande, med ett knitrande elektriskt skal under de 3 sekunderna.
- **Du kan inte använda den** medan en säker zon skyddar dig, medan du är kamouflerad eller inom **30 sekunder** efter den förra. Den fungerar överallt annars, även de första dagarna av en säsong (Fredsprotokollet): utomjordingar jagar fortfarande då.
- En utomjording du träffar under de 3 sekunderna vänder sig inte mot dig förrän de är över. Dina pax och reglerna om första träffen ändras inte.
- **Vad du ser.** En puls av böjt rum rusar ut från piloten så långt som pulsen avslutar kamouflage (1 500 enheter), alla inom räckhåll ser den, och ett knitrande elektriskt skal omger skeppet under de 3 sekunderna, med en ring runt ditt eget skepp och en bricka högst upp på skärmen som räknar tiden. Målringen hos alla som hade valt dig bryts sönder, med ett kort knäpp. Platsen EMP visar de laddningar du äger, lyser blått medan skalet är uppe och mörknar medan den laddas om.
- **En laddning, en användning.** Platsen fylls på från ditt inventarie när du äger fler. De **30 sekunderna** av omladdning sparas inte: att logga ut eller hoppa genom en portal nollställer dem, och nästa puls kostar en laddning.
