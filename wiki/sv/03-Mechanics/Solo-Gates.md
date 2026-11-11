<!-- wiki-i18n source: 9cfe9cd95c159da6 -->
<!-- wiki-i18n title: Soloportar -->
# Soloportar {#solo-gates}

<!-- wiki-search: solo gates; solo gate; gate; gates; galaxy gates; rift; rifts; alpha rift; beta breach; gamma foundry; delta siege; omega vault; chrono gate; chrono-gate; materializer; energy materializer; scan; spin; gate part; gate parts; guarantee; pity; consolation; wave; waves; nuke wave; skip; boss; lives; resume; abandon; speedrun; no death; challenge; achievement; thulium cap; soloportar; soloport; galaxportar; portdel; portdelar; energimaterialiserare; snurr; garanti; våg; vågor; liv; fortsätt; ge upp; utan död; utmaning; prestation; thulium-tak -->

**Soloportarna** är fem av Galaxportarna som du flyger ensam: **Alpha Rift**, **Beta Breach**, **Gamma Foundry**, **Delta Siege** och **Omega Vault**. Var och en är en egen tom arena där vågor av utomjordingar kommer mot dig en efter en och en boss väntar i slutet. Du öppnar en port med dess **delar**, som du hittar genom att snurra Energimaterialiseraren med Thulium, och en seger betalar krediter, Thulium, erfarenhet, heder, malm, plåtar och ammunition.

En soloport är inte en [klandungeon](/wiki/03-Mechanics/Dungeons.md). En dungeon är en labyrint som en klan öppnar för en grupp, med en krigsherre i slutet; en soloport är en arena som bara du är i, och ingen annan kan gå in med dig. De två har skilda regler, utbetalningar och gränser. Sidan Galaxportar har också **Chrono-Gate**, som inte är en plats att flyga till utan porten som öppnar ditt [Transportförråd](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) inför wipen: dess delar hittas med samma snurr.

## I korthet {#at-a-glance}

<!-- solo-glance:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Portar**: 6: Chrono-Gate och 5 soloportar, Alpha Rift, Beta Breach, Gamma Foundry, Delta Siege och Omega Vault
- **Snurr**: 100 Thulium för varje snurr, och 1, 5, 10 eller 100 snurr åt gången
- **Chans för en del**: 13 % per snurr. Porten som delen tillhör väljs på måfå, och varje port får 2,17 % av snurren. När Chrono-Gate är klar lämnar dess andel hjulet, och soloportarna behåller 2,17 % var
- **Garanti**: Efter 24 snurr i rad utan del stiger chansen med varje snurr, och efter 47 hittar nästa snurr alltid en. En del av vilken port som helst startar räkningen om
- **Liv**: 3 per försök; varje död kostar ett
- **Nedräkning**: 5 s före varje våg, även den första och bossens. En våg har ingen timer, och en omgång har ingen heller
- **Arena**: Öppen rymd på 8 000 × 6 000 enheter utan stenar, och du är ensam i den. En värld har 16 av dem, och när alla är upptagna kan du inte gå in
- **Utomjordingar samtidigt**: Högst 60 av en våg lever samtidigt, och 250 i en valfri våg. Resten väntar på plats
- **Bossar**: En boss kan inte skadas under 3 s när den byter fas
- **Thulium-tak**: En port betalar tillbaka högst 50 % av det Thulium du spenderat på snurr. Resten kapas, och resultatet säger hur mycket

<!-- solo-glance:end -->

## Att hitta portdelar {#finding-gate-parts}

Öppna sidan **Galaxportar** och snurra Energimaterialiseraren. Varje snurr betalas med Thulium och hittar högst en del, och delen tillhör en av de sex portarna, vald på måfå. Du behöver ett antal delar av en port för att öppna den, och delarna är dina tills du använder dem. Ett snurr som inte hittar någon del är inte förlorat: det betalar ett pris ([nedan](#a-spin-without-a-part)). Varje snurr debiteras, även med en klar Chrono-Gate. När Chrono-Gate är klar hittar dess andel av snurren ingenting, och soloportarna behåller sin egen chans, så en del av en soloport kostar detsamma med eller utan den.

Tabellen anger kostnaden för varje port i delar och vad de kostar i snitt **med garantin** (ett snurr är ett lotteri, så en lyckosam pilot betalar mindre och en olycklig mer, upp till den längsta serie snurr som garantin tillåter).

<!-- solo-parts:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Port | Delar för att klara den | Chans för en del per snurr | Snurr i snitt | Thulium i snitt |
| :--- | ---: | ---: | ---: | ---: |
| **Chrono-Gate** | 2 | 2,17 % | 91 | 9 093 |
| **Alpha Rift** | 11 | 2,17 % | 500 | 50 011 |
| **Beta Breach** | 26 | 2,17 % | 1 182 | 118 208 |
| **Gamma Foundry** | 54 | 2,17 % | 2 455 | 245 508 |
| **Delta Siege** | 87 | 2,17 % | 3 955 | 395 541 |
| **Omega Vault** | 108 | 2,17 % | 4 910 | 491 017 |

<!-- solo-parts:end -->

Chrono-Gates delar går tillbaka till noll vid wipen, och du hittar dem igen varje säsong. **Soloportarnas delar finns kvar**, liksom garantins räknare och uppgiften om vad du spenderat på snurr och vad portarna betalat tillbaka; wipen tar ingen av dem ([Portar och wipen](#gates-and-the-wipe)).

### Ett snurr utan del {#a-spin-without-a-part}

De flesta snurr hittar ingen del. Vart och ett betalar ett pris, valt efter chanserna nedan: laserammunition av andra multiplikatorn eller bättre, en raketbunt av andra eller tredje nivån och då och då ett [specialföremål](/wiki/06-Items/Special-Items.md) eller en [container](/wiki/06-Items/Containers.md). Ett pris som inte kan ges (du har till exempel redan det högsta antalet av det specialföremålet) blir en bunt ammunition eller raketer med samma slumpning, så ett snurr betalar aldrig mindre än sin tabell. Priset är tydligt mindre värt än vad snurret kostar: portarna är en Thulium-sänka.

<!-- solo-prizes:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Belöning | Chans per snurr |
| :--- | ---: |
| En container: Chroma Archive | 0,01 % |
| Ett specialföremål: Magic Hammer | 0,2 % |
| Ett specialföremål: Schematics | 0,2 % |
| Ett specialföremål: Philosopher's Stone | 0,2 % |
| Ett specialföremål: Forger's Seal | 0,2 % |
| Ett specialföremål: Workforce Contract | 0,2 % |
| Ett specialföremål: Tinkerer's Badge | 0,1 % |
| Laserammunition: Advanced Plasma ×75 | 12,88 % |
| Laserammunition: Antimatter Battery I ×62 | 8,59 % |
| Laserammunition: Ultra Core ×40 | 8,59 % |
| Laserammunition: Antimatter Battery II ×29 | 4,29 % |
| Laserammunition: Dark Matter Ammo I ×31 | 4,29 % |
| Laserammunition: Experimental Fusion Core ×17 | 2,15 % |
| Laserammunition: Dark Matter Ammo II ×17 | 2,15 % |
| Raketer: Lancet II ×4 | 8,59 % |
| Raketer: Rivet II ×4 | 8,59 % |
| Raketer: Ember II ×4 | 8,59 % |
| Raketer: Scatter II ×4 | 8,59 % |
| Raketer: Lancet III ×1 | 2,15 % |
| Raketer: Rivet III ×1 | 2,15 % |
| Raketer: Ember III ×1 | 2,15 % |
| Raketer: Scatter III ×1 | 2,15 % |

<!-- solo-prizes:end -->

## Att gå in {#going-in}

Du går in från sidan Galaxportar, och bara när:

- du har portens delar: de tas **en gång, första gången du går in**, och en nekad ingång tar ingenting;
- du flyger ett skepp, inte i ett hopp eller en CPU-kanal, inte i strid och inte i en farosektor, och du är på hemservern (de regionala servrarna har inga portar);
- du inte har någon annan solo-omgång öppen: du har en omgång åt gången, och en omgång du lämnat återupptas eller ges upp innan en annan börjar;
- en spricka är ledig i din värld. Varje värld har ett antal av dem, och när alla är upptagna väntar du.

Du landar ensam mitt i en tom arena. Ingen kan attackera dig i den, och Jump CPU och Base CPU fungerar inte.

## Hur en omgång går till {#how-a-run-goes}

1. **En nedräkning kommer före varje våg**, även före den första och före bossens. En våg har ingen timer, och omgången har ingen heller: den tar så lång tid du behöver.
2. **En våg** dyker upp på en ring runt dig och flyger mot dig, i portens takt. Bara så många av den lever samtidigt, och resten väntar på plats. Den tar slut när dess sista utomjording är död.
3. **Dina framsteg sparas efter varje våg.** Om du går börjar en pågående våg om helt när du kommer tillbaka.
4. **En valfri våg** är en enorm våg Seeker, och Delta Siege och Omega Vault har en var. Under dess nedräkning kan du hoppa över den: den räknas då som klar och betalar **ingenting**. Om du bekämpar den betalar dess nedgörningar som i vilken våg som helst.
5. **Den sista vågen är bossen.** Den byter fas när dess skrov faller, och den kan inte skadas ett ögonblick vid varje byte. När bossen dör är omgången klar, och segern betalas direkt.

**Liv.** En död kostar ett liv och skickar dig till din bas som vilken annan död som helst; omgången väntar på dig, utan att någon klocka tickar. **Fortsätt** tar dig tillbaka in vid den sparade vågen med de liv du har kvar, och kräver inga nya delar. När ditt sista liv är borta tar försöket slut men omgången är kvar öppen vid den senast avklarade vågen, och Fortsätt fyller på dina liv. **Lämna**, en utloggning eller ett världsbyte pausar omgången utan att kosta ett liv. En omstart av servern håller också din omgång öppen. **Ge upp** ger upp omgången: dess delar är borta, och utomjordingarna du dödade betalas som de står. **Fortsätt** fungerar bara från ett flygande skepp: efter en död väntar knappen på resultatskärmen, med en rad som säger varför, tills du har återvänt. Ett skepp som återvänder kommer tillbaka med begränsat skrov, så när ditt skrov är under hälften varnar resultatskärmen; **Fortsätt** tar dig ändå tillbaka som du är. Reparationsskeppen vid din bas lagar dig inom sin aura.

Varje värld möter samma port: utomjordingarnas styrka och utbetalning beror inte på vilken värld du flyger i.

### Vågorna {#the-waves}

Utomjordingarna är spelets (Seeker, Phantasm, Bulwark, Goombah och Crystalys), gjorda hårdare eller mjukare av porten. Den planerade tiden är vad porten är byggd för att ta för en pilot på startnivån av Laserteknik ([Pilotfärdigheter](/wiki/03-Mechanics/Pilot-Skills.md)); en pilot som har höjt Laserteknik blir klar tidigare.

<!-- solo-waves:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Port | Vågor, bossens inräknad | Utomjordingar i vågorna | Boss | Planerad tid |
| :--- | ---: | :--- | :--- | :--- |
| **Alpha Rift** | 10 | 60 Seeker, 160 Phantasm | Enhanced Phantasm | 10 till 15 min |
| **Beta Breach** | 14 | 80 Seeker, 180 Phantasm, 80 Bulwark, 20 Goombah | Enhanced Bulwark | 15 till 25 min |
| **Gamma Foundry** | 18 | 100 Phantasm, 120 Bulwark, 100 Goombah, 8 Crystalys | Elite Crystalys | 25 till 35 min |
| **Delta Siege** | 22 | 250 Seeker, 200 Phantasm, 180 Bulwark, 140 Goombah, 15 Crystalys | Siege Construct | 35 till 45 min |
| **Omega Vault** | 26 | 250 Seeker, 250 Phantasm, 200 Bulwark, 200 Goombah, 25 Crystalys | Omega Guardian | 50 till 60 min |

- **Delta Siege**: våg 18 (250 Seeker) är valfri: du kan hoppa över den medan dess nedräkning pågår, och den betalar ingenting
- **Omega Vault**: våg 17 (250 Seeker) är valfri: du kan hoppa över den medan dess nedräkning pågår, och den betalar ingenting; vågorna 22 till 24 är elit, med ×1,5 skrov, sköld och skada

<!-- solo-waves:end -->

### Bossarna {#the-bosses}

En boss är en utomjordings skepp, förstorat, med ett eget skrov, en egen sköld och en egen salva, som ingen inställning av porten eller världen ändrar. En fas börjar när bossens skrov faller till talet i tabellen: dess sköld kan sättas om, dess salva eller all dess skada ändras, och den kan starta ett drag. Varje drag aviseras: en cirkel, en ring eller ett märke på ditt skepp visar det ett ögonblick innan det slår ned. Utomjordingarna en boss kallar på betalar och släpper ingenting.

<!-- solo-bosses:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Boss | Port | Skrov | Sköld | Lasersalva |
| :--- | :--- | ---: | ---: | ---: |
| **Enhanced Phantasm** | Alpha Rift | 330 000 | 530 000 | 5 700–7 000 |
| **Enhanced Bulwark** | Beta Breach | 690 000 | 170 000 | 4 500–5 500 |
| **Elite Crystalys** | Gamma Foundry | 620 000 | 250 000 | 3 800–4 700 |
| **Siege Construct** | Delta Siege | 1 150 000 | 1 730 000 | 3 400–4 200 |
| **Omega Guardian** | Omega Vault | 1 340 000 | 840 000 | 2 600–3 200 |

| Boss | Fas | Kvarvarande skrov | Vad den gör |
| :--- | :--- | :--- | :--- |
| **Enhanced Phantasm** | Enhanced Phantasm | 100 % till 0 % | Den bara skjuter. |
| **Enhanced Bulwark** | Shielded | 100 % till 50 % | Dess sköld sätts till ×4 av bossens egen. |
|  | Second attack | 50 % till 0 % | Dess salva är ×1,3. Den avfyrar 4 Dormant Lance-raketer mot dig, 61 000 var, en var 0,5 s, i en salva var 30 s. |
| **Elite Crystalys** | Elite | 100 % till 50 % | Den bara skjuter. |
|  | Reinforced | 50 % till 0 % | Dess sköld sätts till ×2 av bossens egen. Var 10 min kallar den på 10 Goombah, högst 10 av dem levande; de betalar och släpper ingenting. |
| **Siege Construct** | Siege Construct | 100 % till 0 % | Var 1 min släpper den 3 salvor av 8 meteorer, 5 500 var på allt inom 420 enheter från där de landar, 50 % av dem riktade mot dig; varje cirkel visas 3 s innan den landar. Den avfyrar 6 Dormant Lance-raketer mot dig, 9 000 var, en var 0,5 s, i en salva var 1 min. |
| **Omega Guardian** | Shield Fortress | 100 % till 70 % | Dess sköld sätts till ×1,5 av bossens egen. Var 40 s kallar den på 6 Bulwark, högst 12 av dem levande; de betalar och släpper ingenting. |
|  | Swarm Protocol | 70 % till 35 % | Var 25 s kallar den på 12 Phantasm, högst 24 av dem levande; de betalar och släpper ingenting. Var 30 s träffar en explosion på 140 000 allt inom 700 enheter från bossen; ringen visas 2 s innan den landar. |
|  | Overload | 35 % till 0 % | Dess sköld sätts till ×0,1 av bossens egen. All dess skada är ×2,5. Efter 2 min i fasen är all dess skada ×2 till. Var 25 s träffar en explosion på 28 000 allt inom 700 enheter från bossen; ringen visas 2 s innan den landar. |

<!-- solo-bosses:end -->

## Vad en seger betalar {#what-a-clear-pays}

En seger betalar sin tabell **en gång**, på en gång, i det ögonblick bossen dör: krediterna, Thulium, erfarenheten och heder, malmen, plåtarna och Power Cores, och ammunitionen. Erfarenheten räknas för dina PvE-rankingpoäng, som en dungeons.

<!-- solo-pay:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Port | Krediter | Thulium | XP | Heder |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 450 000 | 5 000 | 70 000 | 1 000 |
| **Beta Breach** | 1 500 000 | 12 000 | 180 000 | 2 500 |
| **Gamma Foundry** | 4 000 000 | 25 000 | 400 000 | 5 500 |
| **Delta Siege** | 8 000 000 | 40 000 | 800 000 | 10 000 |
| **Omega Vault** | 15 000 000 | 60 000 | 1 500 000 | 20 000 |

- **Alpha Rift**: Ship Fragment ×300, Nyxite ×300, Daraxium ×400; ammunition: Advanced Plasma ×20 000, Ultra Core ×5 000
- **Beta Breach**: Ship Fragment ×700, Nyxite ×750, Daraxium ×800, Cataclysite ×400, Quorvium ×100; ammunition: Advanced Plasma ×50 000, Ultra Core ×20 000, Experimental Fusion Core ×3 000
- **Gamma Foundry**: Ship Fragment ×1 150, Nyxite ×1 000, Cataclysite ×900, Quorvium ×400, Power Core ×15; ammunition: Advanced Plasma ×30 000, Ultra Core ×60 000, Experimental Fusion Core ×20 000
- **Delta Siege**: Ship Fragment ×2 000, Nyxite ×1 750, Cataclysite ×1 500, Quorvium ×1 000, Reinforced Hull Plate ×70, Power Core ×40, Ancient Control Unit ×3; ammunition: Advanced Plasma ×40 000, Ultra Core ×90 000, Experimental Fusion Core ×50 000
- **Omega Vault**: Ship Fragment ×3 250, Nyxite ×2 750, Cataclysite ×2 250, Quorvium ×1 600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10; ammunition: Advanced Plasma ×50 000, Ultra Core ×100 000, Experimental Fusion Core ×85 000

<!-- solo-pay:end -->

**Thulium kapas vid ett tak.** Portarna får betala tillbaka högst en andel av det Thulium du spenderat på snurr, räknat över alla dina portar och alla dina snurr (andelen står i listan överst). Det en seger och dess utomjordingar skulle betala över det kapas, och resultatskärmen säger hur mycket. Krediter, erfarenhet, heder, malm, plåtar och ammunition kapas aldrig.

### Utomjordingarna {#the-aliens}

Varje utomjording du dödar i en port betalar med de tal den har i Alpha, vilken värld du än flyger i: ingen världsmultiplikator, ingen booster och ingen Premium-bonus ändrar dem. En våg betalar för sina utomjordingar **en gång** per omgång, hur ofta du än går och kommer tillbaka. Utbetalningen kommer när varje avsnitt av omgången tar slut: när du lämnar, dör, får slut på liv, ger upp eller klarar den. Nedgörningarna i ett avsnitt förblir obetalda bara vid wipen och vid en omstart av servern medan du är inne (din omgång förblir öppen, men nedgörningarna i det avsnittet går förlorade). Nedgörningar i en port räknas för inget annat: inte för uppdragen, nedgörningsstatistiken, prestationernas räknare, dödsloggen eller dina drönares och P.E.T.s erfarenhet. Erfarenheten de betalar räknas däremot för dina PvE-rankingpoäng, som erfarenheten av en seger. Utomjordingarnas byte kommer med utbetalningen, rakt in i ditt inventarium.

<!-- solo-kills:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Utomjording | Krediter | Thulium | XP | Heder |
| :--- | ---: | ---: | ---: | ---: |
| **Seeker** | 1 000 | 4 | 100 | 2 |
| **Phantasm** | 3 000 | 12 | 300 | 6 |
| **Bulwark** | 5 000 | 25 | 800 | 10 |
| **Goombah** | 15 000 | 75 | 3 000 | 24 |
| **Crystalys** | 75 000 | 200 | 12 000 | 52 |

| Port | Krediter | Thulium | XP | Heder |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 540 000 | 2 160 | 54 000 | 1 080 |
| **Beta Breach** | 1 320 000 | 5 980 | 186 000 | 2 520 |
| **Gamma Foundry** | 3 000 000 | 13 300 | 522 000 | 4 616 |
| **Delta Siege** | 4 975 000 | 21 400 | 829 000 | 7 640 |
| **Omega Vault** | 6 875 000 | 29 000 | 1 160 000 | 10 100 |

<!-- solo-kills:end -->

## Utmaningar och prestationer {#challenges-and-achievements}

Två valfria utmaningar kan vinnas vid vilken seger som helst, och de betalar en prestation var och **inget Thulium**. En seger **utan död** är en utan någon död alls under hela omgången, över alla gånger du gick in. En **speedrun** är en seger inom portens kortaste planerade tid, räknad efter den tid du tillbringar inne i arenan. De andra sex prestationerna är för att klara varje port, och alla fem:

<!-- solo-achievements:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Klyftan stängd** (Vanlig): Klara Alpha Rift på egen hand.
- **Bräsch förseglad** (Ovanlig): Klara Beta Breach på egen hand.
- **Gjuteriet nedlagt** (Sällsynt): Klara Gamma Foundry på egen hand.
- **Belägringen bruten** (Sällsynt): Bryt Delta Siege på egen hand.
- **Valvet knäckt** (Episk): Knäck Omega Vault på egen hand.
- **Portvakt** (Legendarisk): Klara alla fem soloportar: Alpha, Beta, Gamma, Delta och Omega.
- **Oberörbar** (Sällsynt): Klara en soloport utan att förlora ett liv.
- **Mot klockan** (Sällsynt): Klara en soloport på dess kortaste tid eller snabbare: 10, 15, 25, 35 eller 50 minuter, från Alpha till Omega.

<!-- solo-achievements:end -->

## Föremål från en port {#items-from-a-gate}

Det en port ger dig är **säljbart**: malmen, plåtarna, Power Cores, ammunitionen och utomjordingarnas byte kan läggas ut på [Auktionen](/wiki/03-Mechanics/Auction.md) som ett drop eller en uppdragsbelöning, med samma undantag som för vilket föremål som helst. Priserna från ett snurr utan del är det inte: de kommer från ett snurr, inte från en port.

## Portar och wipen {#gates-and-the-wipe}

- **Wipen avslutar varje öppen omgång** och ger tillbaka dess delar till dig. En omgång fortsätter inte in i nästa säsong.
- **Behålls genom wipen:** de fem soloportarnas delar, garantins räknare och uppgiften om vad du spenderat på snurr och vad portarna betalat tillbaka, så Thulium-taket fortsätter över säsongerna. Prestationerna är dina för alltid.
- **Förloras vid wipen:** Chrono-Gates delar, som förut. Dina snurr köper dem igen.
- **Att radera ett konto** raderar delarna, räknaren och uppgiften.
