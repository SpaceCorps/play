<!-- wiki-i18n source: 0a2447734a603004 -->
<!-- wiki-i18n title: Specialförmågor -->
# Specialförmågor {#special-abilities}

<!-- wiki-search: special ability; special abilities; ability; abilities; mob; mobs; regenerate; mending; shield burst; hardened plating; plating; enrage; call reinforcements; reinforcements; clones; decoy; flee and return; flee; life drain; nova pulse; nova; rocket barrage; barrage; veil; sow mines; mines; split; fragments; boss steps; ladder; three steps; warning; tell; surprise; warlord; warden; leader; specialförmågor; regenerering; sköldstöt; härdad plåt; raseri; kalla på förstärkning; kloner; fly och återvänd; livsdränering; novapuls; raketsalva; slöja; minläggning -->

Vissa utomjordingar bär en **specialförmåga**: något de gör en enda gång i sitt liv, när hälften av skrovet är borta. Läkning, en sköldstöt, en flykt, ett rop på hjälp. Inget syns innan den börjar, så varje jakt kan sluta med en överraskning. Den här sidan säger vad varje förmåga gör och hur du möter den. Bossarna fungerar annorlunda: de ändrar sitt sätt att slåss i tre steg när skrovet sjunker, och de små utomjordingarna på den sista nivån kan splittras i fragment om de förstörs för snabbt.

## Så fungerar det {#how-it-works}

<!-- mob-rules:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **En gång.** En utomjording som bär en förmåga använder den en enda gång i sitt liv: när skrovet (inte skölden) i en strid faller under 50 % av maxvärdet. En träff som förstör den uppifrån den gränsen låter den aldrig avfyra, och en utomjording som inte är i strid väntar tills en börjar.
- **Först en varning.** Förmågan börjar med en varning: en ring som sluter sig runt skeppet och ett ord ovanför. En förmåga vars avsnitt nedan säger att den börjar genast har ingen varning. Utomjordingen kan fortfarande förstöras under varningen; då händer ingenting och den betalar som vanligt. De lätta arterna (Seeker och Phantasm) är snabbare: deras varning och effekter varar 50 % så länge.
- **Inget syns i förväg.** En utomjording som bär en förmåga ser ut precis som alla andra, i varje detalj, tills varningen börjar. Ingenting i spelet säger vilken det är, inte ens [Resenärens guide](/wiki/03-Mechanics/Travelers-Guide.md).
- **Vem som bär en.** En liten del av utomjordingarna i koncernsektorerna och Farosektorerna: ju starkare nivå, desto större andel, och svärmarnas ledare (Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah och Boss Crystalys) bär en oftare än de övriga. Utomjordingarna i Deep Void, klanernas dungeons och soloportarna bär aldrig en, och inte heller en svärms följeslagare, en Wardens vågor, Dormant Force eller Tesseract.
- **Den betalar som vilken utomjording som helst.** En utomjording som använder en förmåga betalar, släpper och räknas precis som en som inte gör det: förmågan lägger inget till nedskjutningen och tar tid från den. Nedskjutningen stannar hos piloten som höll den: medan utomjordingen flyr, läker sig eller gömmer sig löper anspråket inte ut.
- **Tillkallade skepp och kopior är inga nedskjutningar.** De skepp en utomjording kallar på och de kopior den gör betalar ingenting, släpper ingenting och räknas inte för något uppdrag, någon statistik eller rankning. Högst 6 lever per tillkallare och 24 på en karta, och kartans egna utomjordingar kommer tillbaka i tid.
- **Alla på kartan ser det.** Kartans piloter får veta när en förmåga börjar: spelet ritar ringen, ordet och effekten och spelar ett ljud.

<!-- mob-rules:end -->

## De tolv förmågorna {#the-twelve-abilities}

En förmåga börjar med en **varning**, om inte dess avsnitt säger att den börjar genast: en ring som sluter sig kring skeppet och ett ord ovanför. Tiderna och talen nedan gäller de tunga arterna. Där ett tal har flera värden gäller de nivåerna i parentes, den grekiska bokstaven framför en utomjordings namn.

<!-- mob-abilities:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

### Regenerering {#regenerate}

Den står stilla och återställer 15 % / 20 % / 25 % / 30 % (α / β / γ / δ) av skrovet och skölden under 6 s, och avfyrar ingenting under tiden. Skada som tillsammans uppgår till 10 % av skrovet och skölden bryter den, och den behåller det den hunnit återställa.

- **Varning**: 1,5 s
- **Ordet ovanför skeppet**: LÄKER
- **Bärs av**: vilken utomjording som helst
- **Svar**: Bränn ner den med raketer eller en hel skara skepp, eller förstör den under varningen.

### Sköldstöt {#shield-burst}

Ett nytt sköldlager på 15 % / 20 % / 30 % / 40 % (α / β / γ / δ) av det största skrovet läggs ovanpå skölden. Så länge det står tar det emot varje poäng av en träff; det är borta när det är förbrukat eller efter 10 s.

- **Varning**: 1 s
- **Ordet ovanför skeppet**: SKÖLD UPP
- **Bärs av**: vilken utomjording som helst
- **Svar**: Ammunition och raketer som tränger igenom sköldar går bättre igenom. Eller skjut på en annan utomjording tills det är borta.

### Härdad plåt {#hardened-plating}

Under 7 s / 8 s / 10 s (β / γ / δ) tar den bara 50 % av varje träff, både skrov och sköld: dubbelt så seg. Den fortsätter slåss, och siffrorna på dina träffar blir grå.

- **Varning**: 1,5 s
- **Ordet ovanför skeppet**: PANSAR
- **Bärs av**: de tunga arterna (Bulwark, Goombah och Crystalys) och de tunga svärmledarna (Pirate Boss och Boss Phantasm), från β och uppåt
- **Svar**: Vänta ut det, träffa en annan utomjording under tiden och spara dina stötar till efteråt.

### Raseri {#enrage}

Under 10 s multipliceras dess skada med ×1,3 / ×1,4 / ×1,5 / ×1,75 (α / β / γ / δ) och dess fart med ×1,25.

- **Varning**: 1 s
- **Ordet ovanför skeppet**: RASERI
- **Bärs av**: vilken utomjording som helst
- **Svar**: Håll skölden uppe, rör dig hela tiden och håll dig utanför dess räckvidd.

### Kalla på förstärkning {#call-reinforcements}

4 / 6 (γ / δ) mindre utomjordingar kommer in från kartans närmaste kant, i 2 vågor med 3 s emellan. Arten som kommer: Phantasm (tillkallade av Bulwark och Goombah); Bulwark (tillkallade av Crystalys). Tillsammans har de 45 % / 60 % (γ / δ) av dess skrov och sköld och avfyrar 50 % av dess salva. De betalar ingenting, släpper ingenting och räknas för ingenting, och de lämnar efter 45 s, eller när tillkallaren förstörs.

- **Varning**: 2 s
- **Ordet ovanför skeppet**: KALLAR
- **Bärs av**: de tunga arterna (Bulwark, Goombah och Crystalys) och de tunga svärmledarna (Boss Phantasm och Boss Goombah), från γ och uppåt
- **Svar**: Förstör tillkallaren: dess skepp följer med. Ett vapen som träffar ett område rensar dem.

### Kloner {#clones}

3 (γ / δ) kopior av den dyker upp runt den, med dess namn och utseende. Tillsammans har de 18 % (γ / δ) av dess skrov och sköld; de avfyrar ingenting och betalar ingenting, och de varar 15 s eller tills den riktiga förstörs. Den riktiga bär en tunn ring medan kopiorna är ute, och målfönstret kallar en kopia "Lockbete".

- **Varning**: 1 s
- **Ordet ovanför skeppet**: KLONAR
- **Bärs av**: vilken utomjording som helst, från γ och uppåt
- **Svar**: Följ ringen och den rörliga skrovmätaren på den riktiga, eller använd ett vapen som träffar ett område.

### Fly och återvänd {#flee-and-return}

Den flyger bort från sina angripare med farten ×2 i 5 s / 6 s / 7 s / 8 s (α / β / γ / δ), och vänder sedan om mot den första piloten som träffade den. Den lämnar aldrig kartan och går aldrig in i en säker zon, den kan träffas hela tiden, och piloten som höll dess nedskjutning behåller den.

- **Varning**: 0,5 s
- **Ordet ovanför skeppet**: FLYR
- **Bärs av**: vilken utomjording som helst
- **Svar**: Jaga den, eller träffa den med raketer medan den flyger.

### Livsdränering {#life-drain}

Under 10 s avfyrar den inget annat: en gång i sekunden dränerar den varje skepp inom räckvidd med en full salva som ingenting undviker, och den läker 75 % / 100 % / 100 % (β / γ / δ) av skadan den gör, högst 20 % av skrovet totalt.

- **Varning**: 1 s
- **Ordet ovanför skeppet**: DRÄNERAR
- **Bärs av**: de tunga arterna (Bulwark, Goombah och Crystalys) och de tunga svärmledarna (Pirate Boss, Boss Phantasm, Boss Goombah och Boss Crystalys), från β och uppåt
- **Svar**: Sätt en sten eller en vägg i linjen, kamouflera dig eller lämna dess räckvidd.

### Novapuls {#nova-pulse}

En ring växer på marken runt den under varningen. När ringen är full träffar den varje skepp inuti en gång, med 4 / 5 (γ / δ) av dess salvor. Dess radie, i enheter, är 700 / 800 (γ / δ).

- **Varning**: 2,5 s
- **Ordet ovanför skeppet**: NOVA
- **Bärs av**: de tunga arterna (Bulwark, Goombah och Crystalys) och de tunga svärmledarna (Pirate Boss, Boss Phantasm och Boss Goombah), från γ och uppåt
- **Svar**: Flyg ut ur ringen innan den fylls: det är den enda stöten du kan undvika.

### Raketsalva {#rocket-barrage}

Under 3 s avfyrar den 4 / 6 / 8 (β / γ / δ) [Rivet-raketer](/wiki/06-Items/Rockets.md#the-twelve-rockets) mot sitt mål: Rivet I / II / II (β / γ / δ). De flyger rakt och är inte målsökande.

- **Varning**: 1,5 s
- **Ordet ovanför skeppet**: SALVA
- **Bärs av**: de tunga arterna (Bulwark, Goombah och Crystalys) och de tunga svärmledarna (Boss Phantasm och Boss Goombah), från β och uppåt
- **Svar**: Rör dig hela tiden: raketerna flyger rakt. En sten i vägen stoppar dem.

### Slöja {#veil}

Under 6 s / 8 s (γ / δ) kan ett skepp längre bort än 700 enheter från den inte låsa på den, och ett lås den hade går förlorat. Närmare än så syns den som vanligt. Den fortsätter slåss, och en explosion skadar den fortfarande.

- **Varning**: ingen, den börjar genast.
- **Ordet ovanför skeppet**: DÖLJER SIG
- **Bärs av**: de tunga arterna (Bulwark, Goombah och Crystalys) och de tunga svärmledarna (Pirate Boss, Boss Phantasm, Boss Goombah och Boss Crystalys), från γ och uppåt
- **Svar**: Gå in till inom 700 enheter.

### Minläggning {#sow-mines}

Den lägger 4 / 6 / 8 (β / γ / δ) minor på en ring på 500 enheter runt platsen där målet stod. En mina aktiveras 3 s efter att den landat, varar 30 s och detonerar en gång, under det första pilotskepp som flyger över den, med 2 / 3 / 3 (β / γ / δ) av utomjordingens salvor. En mina skadar aldrig en utomjording.

- **Varning**: 1,5 s
- **Ordet ovanför skeppet**: LÄGGER MINOR
- **Bärs av**: de tunga arterna (Bulwark, Goombah och Crystalys) och de tunga svärmledarna (Pirate Boss, Boss Phantasm, Boss Goombah och Boss Crystalys), från β och uppåt
- **Svar**: Flyg runt dem: de är ritade på marken och aktiveras sent.


<!-- mob-abilities:end -->

## Splittring {#splitting}

<!-- mob-split:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

De små utomjordingarna på den sista nivån kan också splittras när de förstörs för snabbt. Det gäller bara Seeker, Phantasm, Bulwark, Goombah och Crystalys på nivå δ och ingen annan utomjording, och det är inte en av förmågorna ovan: en utomjording kan ha båda.

- **När**: en pilot förstör den inom 5 s från den första skadan den fick. Inte varje utomjording som dör så snabbt splittras.
- **Vad som kommer ut**: 3 utomjordingar av samma art och nivå, 70 % av dess storlek, var och en med 25 % av skrov och sköld och en full salva, runt platsen där den förstördes. De går på piloten som förstörde den och lämnar efter 180 s.
- **De är vanliga utomjordingar**: var och en betalar vad dess art betalar, släpper vad den släpper och räknas för uppdrag och statistik. De bär ingen förmåga och splittras aldrig.
- **Gränser**: högst 60 fragment lever på en karta, och de håller inte tillbaka kartans egna utomjordingar.
- **Vad det betyder**: en besättning som förstör sina utomjordingar tillräckligt snabbt kan få upp till 4 nedskjutningar från en enda utomjording. En som inte gör det får ingenting av det.

<!-- mob-split:end -->

## Bossarnas tre steg {#the-bosses-three-steps}

Varje boss ändrar sitt sätt att slåss i tre steg: när striden börjar, när skrovet faller under två tredjedelar och när det faller under en tredjedel. Ett steg sker en gång och går aldrig tillbaka, om inte bossen börjar om, som det står nedan.

<!-- mob-ladders:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **En paus vid varje steg.** När ett steg som har något att göra börjar efter det första kan bossen inte skadas under 1,5 s (3 s för Dungeon Warlord och soloportarnas bossar).
- **Också en specialförmåga.** Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah och Boss Crystalys kan bära en specialförmåga också (Dormant Force och Tesseract aldrig): den kommer mellan det andra och det tredje steget; när de två skulle börja samtidigt väntar den senare högst 3 s. Det är aldrig en förmåga som ledarens egna steg använder.
- **Från början igen.** Tesseract börjar om sina steg när den har läkt sig hel.

### Svärmledarna {#the-swarm-leaders}

| Ledare | I början | Under två tredjedelar | Under en tredjedel |
| :--- | :--- | :--- | :--- |
| **Pirate Boss** | Avfyrar en solfjäder av 3 raketer, 12 grader isär, mot den första piloten som träffade den. | Kallar på 5 fler Pirate Scouts på en gång, högst 10 levande. De betalar ingenting och lämnar efter 45 s. | Flyger med farten ×1,8 till närmaste port i 10 s, och vänder sedan om mot piloterna. |
| **Boss Seeker** | Dess Seeker Slaves läker den ×2 så fort i 8 s. | 2 kopior av den dyker upp, och den riktiga bär en ring. | Flyr från piloterna i 4 s och vänder sedan om. |
| **Boss Phantasm** | Var och en av dess Phantasm Guards sätter upp ett sköldlager på 10 % av sitt eget skrov. | 3 kopior av den dyker upp, och den riktiga bär en ring. | Blinkar ungefär 2 500 enheter bort från piloterna, och dess Phantasm Guards kommer tillbaka hela runt den. |
| **Boss Goombah** | Tar 50 % av varje träff i 6 s. | Dess skada multipliceras med ×1,5 och dess fart med ×1,25 i 10 s. | Läker 25 % av skrovet och skölden (en skadestöt bryter det), och dess Goombah Guards läker den ×2 så fort under tiden. |
| **Boss Crystalys** | Tar 50 % av varje träff i 8 s. | En ring på 700 enheter träffar varje skepp inuti med 4 av dess salvor, och den avfyrar 4 raketer. | Läker 20 % av skrovet och skölden (en skadestöt bryter det), och 3 fler Crystalys Guards kommer, högst 6 levande. |
| **Dormant Force** | Tar 70 % av varje träff så länge en av dess Dormant Pulses lever. | Dess Dormant Pulses avfyrar en raket var 2,5 s i 15 s. | Så länge alla dess Dormant Pulses lever läker de den med 5 % av skrovet per sekund i 6 s. |
| **Tesseract** | – | 20 fler Facets anländer på en gång, utöver det vanliga antalet. | – |

### Klanens Warden {#the-clan-wardens}

| Warden | I början | Under två tredjedelar | Under en tredjedel |
| :--- | :--- | :--- | :--- |
| **Brood Warden** (I, II, III) | Alla 4 drönare kommer till dess sida på en gång. | Dess drönare läker den ×1,5 så fort i 15 s. | 2 fler drönare kommer, utöver det vanliga antalet, i 30 s. De betalar ingenting. |
| **Siege Warden** (I, II, III) | – | Avfyrar sin raket ×2 så ofta i 20 s. | Läker 15 % av skrovet och skölden (en skadestöt bryter det). |
| **Wrath Warden** (I, II, III) | – | Dess lasrar slår ×1,25 så hårt. | Dess lasrar slår ×1,5 så hårt sammanlagt, inte ovanpå steget före. |

### Dungeon Warlord {#the-dungeon-warlord}

- **Under två tredjedelar**: Pausen mellan dess förmågor sjunker till 4 s och deras väntetider till ×0,75.
- **Under en tredjedel**: Pausen sjunker till 2 s, väntetiderna till ×0,5 och skadan stiger till ×1,25; den kastar en gratis Meteor-salva, och dess Swarm kommer aldrig tillbaka oftare än var 120 s.
- **En paus vid varje steg.** När ett steg börjar kan Warlord inte skadas under 3 s.

### Soloportarnas bossar {#the-solo-gate-bosses}

De sex bossarna i soloportarna har också tre steg, sina faser: de finns i tabellen över [bossarna](/wiki/03-Mechanics/Solo-Gates.md#the-bosses) i artikeln Soloportar.

<!-- mob-ladders:end -->

## Läs mer {#where-to-read-more}

- [Strid](/wiki/03-Mechanics/Combat.md#who-an-alien-fights): vem en utomjording slåss mot och vem som får dess nedläggning.
- [Svärmar](/wiki/05-Swarms/Swarms.md): ledarna och deras steg, en artikel för varje svärm.
- [Klanens Warden](/wiki/03-Mechanics/Clans.md#fighting-a-warden), [Dungeon Warlord](/wiki/03-Mechanics/Dungeons.md#the-warlord) och [bossarna i soloportarna](/wiki/03-Mechanics/Solo-Gates.md#the-bosses).
- [Resenärens guide](/wiki/03-Mechanics/Travelers-Guide.md): vad du har lärt dig om en utomjording. Den säger aldrig vilken som bär en förmåga.
