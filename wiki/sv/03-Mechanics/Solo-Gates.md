<!-- wiki-i18n source: 0b67d55ade0b37c6 -->
<!-- wiki-i18n title: Soloportar -->
# Soloportar {#solo-gates}

<!-- wiki-search: solo gates; solo gate; gate; gates; galaxy gates; rift; rifts; alpha rift; beta breach; gamma foundry; delta siege; omega vault; chrono gate; chrono-gate; materializer; energy materializer; scan; spin; gate part; gate parts; guarantee; pity; consolation; wave; waves; nuke wave; skip; boss; lives; resume; abandon; speedrun; no death; challenge; achievement; thulium cap; soloportar; soloport; galaxportar; portdel; portdelar; energimaterialiserare; snurr; garanti; våg; vågor; liv; fortsätt; ge upp; utan död; utmaning; prestation; thulium-tak -->

**Soloportarna** är fem av Galaxportarna som du flyger ensam: **Alpha Rift**, **Beta Breach**, **Gamma Foundry**, **Delta Siege** och **Omega Vault**. Var och en är en egen tom arena där vågor av utomjordingar kommer mot dig en efter en och en boss väntar i slutet. Du bygger en port av dess **delar**, som du hittar genom att snurra Energimaterialiseraren med Thulium, och en seger betalar krediter, Thulium, erfarenhet, heder, malm, plåtar och ammunition.

En soloport är inte en [klandungeon](/wiki/03-Mechanics/Dungeons.md). En dungeon är en labyrint som en klan öppnar för en grupp, med en krigsherre i slutet; en soloport är en arena som bara du är i, och ingen annan kan gå in med dig. De två har skilda regler, utbetalningar och gränser. Sidan Galaxportar har också **Chrono-Gate**, som inte är en plats att flyga till utan porten som öppnar ditt [Transportförråd](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) inför wipen: dess delar hittas med samma snurr.

## I korthet {#at-a-glance}

<!-- solo-glance:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Portar**: 7: Chrono-Gate och 6 soloportar, Alpha Rift, Beta Breach, Gamma Foundry, Delta Siege, Omega Vault och Davidski's Nightmare
- **Snurr**: 100 Thulium för varje snurr, och 1, 5, 10 eller 100 snurr åt gången
- **Chans för en del**: 13 % per snurr, i vilken kategori du än snurrar. Delen tillhör en av portarna i den kategorin, alla lika sannolika: Chrono-Gate ensamt får allt, Alpha Rift, Beta Breach och Gamma Foundry får 4,33 % var, och Delta Siege och Omega Vault får 6,5 % var. När Chrono-Gate är klar finns inget mer att snurra i dess kategori
- **Garanti**: Efter 24 snurr i rad utan del stiger chansen med varje snurr, och efter 47 hittar nästa snurr alltid en. En del av vilken port som helst startar räkningen om
- **Liv**: 3 per försök; varje död kostar ett
- **Nedräkning**: 5 s före varje våg, även den första och bossens. En våg har ingen timer, och en omgång har ingen heller
- **Arena**: Öppen rymd på 8 000 × 6 000 enheter utan stenar, och du är ensam i den. En värld har 16 av dem, och när alla är upptagna kan du inte gå in
- **Utomjordingar samtidigt**: Högst 60 av en våg lever samtidigt, och 250 i en valfri våg. Resten väntar på plats
- **Bossar**: En boss kan inte skadas under 3 s när den byter fas
- **Thulium-tak**: En port betalar tillbaka högst 50 % av det Thulium du spenderat på snurr. Resten kapas, och resultatet säger hur mycket

<!-- solo-glance:end -->

## Att hitta portdelar {#finding-gate-parts}

Öppna sidan **Galaxportar** och snurra Energimaterialiseraren. Varje snurr betalas med Thulium och hittar högst en del. Välj först en **kategori**: **Chrono-Gate**, **Alpha–Gamma** (Alpha Rift, Beta Breach och Gamma Foundry) eller **Delta–Omega** (Delta Siege och Omega Vault). Chansen att hitta en del är densamma i varje kategori, och delen tillhör en av portarna i den valda kategorin, alla lika sannolika. Du behöver ett antal delar av en port för att bygga den, och delarna är dina tills du använder dem. Ett snurr som inte hittar någon del är inte förlorat: det betalar ett pris ([nedan](#a-spin-without-a-part)). Varje snurr debiteras. När Chrono-Gate är klar är dess val låst, eftersom det inte finns något mer att hitta i den, och de två andra kategorierna behåller sin chans, så en del av en soloport kostar detsamma med eller utan den.

Tabellen anger kostnaden för varje port i delar och vad de kostar i snitt **med garantin** när du snurrar den kategori som porten tillhör (ett snurr är ett lotteri, så en lyckosam pilot betalar mindre och en olycklig mer, upp till den längsta serie snurr som garantin tillåter).

<!-- solo-parts:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Port | Delar för att klara den | Chans för en del per snurr | Snurr i snitt | Thulium i snitt |
| :--- | ---: | ---: | ---: | ---: |
| **Chrono-Gate** | 13 | 13 % | 99 | 9 851 |
| **Alpha Rift** | 14 | 4,33 % | 318 | 31 825 |
| **Beta Breach** | 33 | 4,33 % | 750 | 75 016 |
| **Gamma Foundry** | 68 | 4,33 % | 1 546 | 154 579 |
| **Delta Siege** | 96 | 6,5 % | 1 455 | 145 486 |
| **Omega Vault** | 119 | 6,5 % | 1 803 | 180 343 |
| **Davidski's Nightmare** | 238 | 13 % | 1 803 | 180 343 |

<!-- solo-parts:end -->

Chrono-Gates delar går tillbaka till noll vid wipen, och du hittar dem igen varje säsong. **Soloportarnas delar finns kvar**, liksom garantins räknare och uppgiften om vad du spenderat på snurr och vad portarna betalat tillbaka; wipen tar ingen av dem ([Portar och wipen](#gates-and-the-wipe)).

### Ett snurr utan del {#a-spin-without-a-part}

De flesta snurr hittar ingen del. Vart och ett betalar ett pris, valt efter chanserna nedan: laserammunition av andra multiplikatorn eller bättre, en raketbunt av andra eller tredje nivån och då och då ett [specialföremål](/wiki/06-Items/Special-Items.md) eller en [container](/wiki/06-Items/Containers.md). Ett pris som inte kan ges (till exempel att specialföremålen eller containrarna är avstängda) blir en bunt ammunition eller raketer med samma slumpning, så ett snurr betalar aldrig mindre än sin tabell. Priset är tydligt mindre värt än vad snurret kostar: portarna är en Thulium-sänka.

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

Du **bygger** en port på sidan Galaxportar och **hoppar in** genom dess portal. Man bygger från stationen, med skeppet dockat, och även under flygning: **Galaxportar-fönstret**, som portknappen i verktygsfältet öppnar, snurrar, bygger och väljer destination som sidan gör. Det krävs:

- portens delar: de tas **en gång, när du bygger den**, och ett nekat bygge tar ingenting;
- porten är inte redan byggd: du kan ha **alla** portar byggda samtidigt, med en portal för varje, och du spelar en i taget; en port du byggt går du in i genom dess portal eller ger upp innan du bygger den igen;
- hemservern (en port byggs bara på hemservern: på en regional server återvänder du först till basen).

Den byggda porten står i din **hemsektor** (`M-1`, `T-1` eller `G-1`, efter din koncern) som en portal med dess namn, och sidan Galaxportar säger var den står. **Flyg ut, flyg till portalen och hoppa** genom den som genom vilken portal som helst. En spricka måste vara ledig i din värld när du går in: varje värld har ett antal av dem, och när alla är upptagna väntar du. Du ser bara **dina egna** portar: portalerna till andra piloters portar i samma sektor visas inte för dig. Du kan ha **alla fem portarna byggda samtidigt**, var och en med sin egen portal, och du spelar en i taget: **medan du är i en arena står ingen av dina portaler**, och de kommer tillbaka när du är ute.

**På de regionala servrarna (Singapore, US East).** En byggd port spelas också där. Portalen till din port står på en regional server i din hemsektor, precis som på hemservern, och du får veta det när du kommer. **Hoppa genom den så går du in i en arena på den servern**, med dess latens i stället för hemserverns. En regional server har bara **två arenor i varje värld**, hemservern har många fler: när båda är upptagna väntar du, som du väntar på en ledig spricka på hemservern. Hemservern är fortfarande den enda plats som håller reda på din omgång, dina delar och din utbetalning: utbetalningen når din plånbok när hemservern har räknat omgången, några sekunder efter att den tagit slut, och **plånboken i ditt flygfönster hinner ikapp när du dockar**. Du går in i nästa omgång först när den senaste har räknats. En omgång du lämnar i arenan tar du upp igen genom portalen; vill du ge upp den gör du det i arenan eller på stationen. Är arenan på en regional server avstängd tar dess portal dig i stället tillbaka till hemservern, där du flyger ut mot din port som ovan. Vad som mer fungerar på en regional server står i [Servrar](/wiki/03-Mechanics/Servers.md).

Du landar ensam mitt i en tom arena. Ingen kan attackera dig i den, och Jump CPU och Base CPU fungerar inte.

## Hur en omgång går till {#how-a-run-goes}

1. **En nedräkning kommer före varje våg**, även före den första och före bossens. En våg har ingen timer, och omgången har ingen heller: den tar så lång tid du behöver.
2. **En våg** dyker upp på en ring runt dig och flyger mot dig, i portens takt. Bara så många av den lever samtidigt, och resten väntar på plats. Den tar slut när dess sista utomjording är död.
3. **Dina framsteg sparas efter varje våg.** Om du går börjar en pågående våg om helt när du kommer tillbaka.
4. **En valfri våg** är en enorm våg Seeker, och Delta Siege och Omega Vault har en var. Under dess nedräkning kan du hoppa över den: den räknas då som klar och betalar **ingenting**. Om du bekämpar den betalar dess nedgörningar som i vilken våg som helst.
5. **Den sista vågen är bossen.** Den byter fas när dess skrov faller, och den kan inte skadas ett ögonblick vid varje byte. När bossen dör är omgången klar, och segern betalas direkt.

**Liv.** En död kostar ett liv och skickar dig till din bas som vilken annan död som helst; omgången väntar på dig, utan att någon klocka tickar. Medan omgången är öppen och du är utanför arenan står **portalen till varje port du har byggt i din hemsektor**, och ett hopp genom en av dem tar dig tillbaka in vid den sparade vågen med de liv du har kvar, som **Fortsätt**; den kräver inga nya delar. När ditt sista liv är borta tar försöket slut men omgången är kvar öppen vid den senast avklarade vågen, och att gå in igen fyller på dina liv. **Lämna**, en utloggning eller ett världsbyte pausar omgången utan att kosta ett liv. En omstart av servern håller också din omgång öppen. **Ge upp** ger upp omgången: dess delar är borta, och utomjordingarna du dödade betalas som de står. **Fortsätt** fungerar bara från ett flygande skepp: efter en död väntar knappen på resultatskärmen, med en rad som säger varför, tills du har återvänt. Ett skepp som återvänder kommer tillbaka med begränsat skrov, så när ditt skrov är under hälften varnar resultatskärmen; **Fortsätt** tar dig ändå tillbaka som du är. Reparationsskeppen vid din bas lagar dig inom sin aura.

Varje värld möter samma port: utomjordingarnas styrka och utbetalning beror inte på vilken värld du flyger i.

### Vågorna {#the-waves}

Utomjordingarna är spelets (Seeker, Phantasm, Bulwark, Goombah och Crystalys), gjorda hårdare eller mjukare av porten. Den planerade tiden är vad porten är byggd för att ta för en pilot på startnivån av Laserteknik ([Pilotfärdigheter](/wiki/03-Mechanics/Pilot-Skills.md)); en pilot som har höjt Laserteknik blir klar tidigare.

Vissa vågor för med sig en **svärm**: en boss-NPC från spelet (en Boss Seeker, Boss Phantasm, Boss Goombah eller Boss Crystalys) med sina vakter, som anfaller som en enda grupp. Varje skepp i en svärm hör till sin våg, och vågen tar slut när det sista av dem är dött. De betalar som vågens övriga skepp, med siffrorna i [tabellen över utomjordingarna](#the-aliens). **En boss-NPC tappar sitt byte som i spelets sektorer**: malm, plåtar, ammunition och raketer (vad var och en tappar står på [svärmarnas sidor](/wiki/05-Swarms/Swarms.md)). I en port finns ingen låda att plocka upp: bytet kommer med utbetalningen, rakt in i ditt inventarium, och bara en gång per omgång, som utbetalningen. Dess vakter tappar ingenting, varken i en port eller i sektorerna, och de varken läker sin boss eller kommer tillbaka. Tabellen nedan säger vilka vågor i varje port som för med sig en svärm.

<!-- solo-waves:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Port | Vågor, bossens inräknad | Utomjordingar i vågorna | Boss-NPC:er och svärmar | Boss | Planerad tid |
| :--- | ---: | :--- | :--- | :--- | :--- |
| **Alpha Rift** | 10 | 44 Seeker, 140 Phantasm | våg 5: 1 Seeker Swarm, 1 Phantasm Swarm | Enhanced Phantasm | 10 till 15 min |
| **Beta Breach** | 14 | 64 Seeker, 158 Phantasm, 80 Bulwark, 20 Goombah | våg 4: 2 Seeker Swarm; våg 9: 1 Phantasm Swarm | Enhanced Bulwark | 15 till 25 min |
| **Gamma Foundry** | 18 | 78 Phantasm, 117 Bulwark, 91 Goombah, 8 Crystalys | våg 4: 1 Phantasm Swarm; våg 9: 1 Goombah Swarm; våg 14: 1 Goombah Swarm | Elite Crystalys | 25 till 35 min |
| **Delta Siege** | 22 | 250 Seeker, 200 Phantasm, 141 Bulwark, 130 Goombah, 12 Crystalys | våg 5: 2 Phantasm Swarm; våg 10: 2 Goombah Swarm; våg 15: 1 Goombah Swarm; våg 20: 1 Crystalys Swarm | Siege Construct | 35 till 45 min |
| **Omega Vault** | 26 | 250 Seeker, 236 Phantasm, 170 Bulwark, 174 Goombah, 25 Crystalys | våg 6: 1 Goombah Swarm; våg 11: 2 Goombah Swarm; våg 16: 1 Crystalys Swarm; våg 22: 1 Phantasm Swarm | Omega Guardian | 50 till 60 min |
| **Davidski's Nightmare** | 13 | 50 Evil Protos, 66 Evil Kitefin, 31 Evil Ostirion, 19 Evil Nomad, 22 Evil Paragon, 7 Evil Storm, 8 Evil Wraith, 2 Evil Ironclad |  | Evil Davidski | 45 till 60 min |

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
| **Evil Davidski** | Davidski's Nightmare | 5 500 000 | 6 600 000 | 7 800–9 600 |

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
| **Evil Davidski** | Evil Davidski | 100 % till 50 % | Den avfyrar 6 Dormant Lance-raketer mot dig, 14 700 var, en var 0,5 s, i en salva var 30 s. Var 1 min släpper den 2 salvor av 8 meteorer, 33 000 var på allt inom 400 enheter från där de landar, 50 % av dem riktade mot dig; varje cirkel visas 3 s innan den landar. Var 40 s kallar den på 5 Evil Protos, högst 10 av dem levande; de betalar och släpper ingenting. |
|  | Angry | 50 % till 0 % | Dess sköld sätts till ×0,5 av bossens egen. All dess skada är ×1,5. Efter 8 min i fasen är all dess skada ×2 till. Den avfyrar 6 Dormant Lance-raketer mot dig, 7 800 var, en var 0,4 s, i en salva var 30 s. Var 1 min släpper den 3 salvor av 8 meteorer, 10 200 var på allt inom 420 enheter från där de landar, 50 % av dem riktade mot dig; varje cirkel visas 3 s innan den landar. Var 45 s träffar en explosion på 105 000 allt inom 700 enheter från bossen; ringen visas 2 s innan den landar. Var 40 s kallar den på 3 Evil Kitefin, högst 6 av dem levande; de betalar och släpper ingenting. |

<!-- solo-bosses:end -->

## Vad en seger betalar {#what-a-clear-pays}

En seger betalar sin tabell **en gång**, på en gång, i det ögonblick bossen dör: krediterna, Thulium, erfarenheten och heder, malmen, plåtarna och Power Cores, och ammunitionen. Erfarenhet och heder räknas för dina PvE-rankingpoäng, som en dungeons.

<!-- solo-pay:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Port | Krediter | Thulium | XP | Heder |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 450 000 | 5 000 | 70 000 | 1 000 |
| **Beta Breach** | 1 500 000 | 12 000 | 180 000 | 2 500 |
| **Gamma Foundry** | 4 000 000 | 25 000 | 400 000 | 5 500 |
| **Delta Siege** | 8 000 000 | 40 000 | 800 000 | 10 000 |
| **Omega Vault** | 15 000 000 | 60 000 | 1 500 000 | 20 000 |
| **Davidski's Nightmare** | 15 000 000 | 60 000 | 1 500 000 | 20 000 |

- **Alpha Rift**: Ship Fragment ×300, Nyxite ×300, Daraxium ×400, Echo Shard ×4, Lattice Shard ×6; ammunition: Advanced Plasma ×15 000, Ultra Core ×3 750, Experimental Fusion Core ×15 000
- **Beta Breach**: Ship Fragment ×700, Nyxite ×750, Daraxium ×800, Cataclysite ×400, Quorvium ×100, Echo Shard ×9, Lattice Shard ×13; ammunition: Advanced Plasma ×37 500, Ultra Core ×15 000, Experimental Fusion Core ×22 500
- **Gamma Foundry**: Ship Fragment ×1 150, Nyxite ×1 000, Cataclysite ×900, Quorvium ×400, Power Core ×15, Echo Shard ×18, Lattice Shard ×27; ammunition: Advanced Plasma ×22 500, Ultra Core ×45 000, Experimental Fusion Core ×37 500
- **Delta Siege**: Ship Fragment ×2 000, Nyxite ×1 750, Cataclysite ×1 500, Quorvium ×1 000, Reinforced Hull Plate ×70, Power Core ×40, Ancient Control Unit ×3, Echo Shard ×29, Lattice Shard ×44; ammunition: Advanced Plasma ×30 000, Ultra Core ×67 500, Experimental Fusion Core ×56 250
- **Omega Vault**: Ship Fragment ×3 250, Nyxite ×2 750, Cataclysite ×2 250, Quorvium ×1 600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10, Echo Shard ×34, Lattice Shard ×54; ammunition: Advanced Plasma ×37 500, Ultra Core ×75 000, Experimental Fusion Core ×75 000
- **Davidski's Nightmare**: Ship Fragment ×3 250, Nyxite ×2 750, Cataclysite ×2 250, Quorvium ×1 600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10, Echo Shard ×34, Lattice Shard ×54; ammunition: Advanced Plasma ×37 500, Ultra Core ×75 000, Experimental Fusion Core ×75 000
- **Heartshards**: 1 vid första avklarningen av varje port under en säsong, och 5 % chans till 1 till vid varje avklarning.

<!-- solo-pay:end -->

**Thulium kapas vid ett tak.** Portarna får betala tillbaka högst en andel av det Thulium du spenderat på snurr, räknat över alla dina portar och alla dina snurr (andelen står i listan överst). Det en seger och dess utomjordingar skulle betala över det kapas, och resultatskärmen säger hur mycket. Krediter, erfarenhet, heder, malm, plåtar och ammunition kapas aldrig.

### Utomjordingarna {#the-aliens}

Varje utomjording du dödar i en port betalar med de tal den har i Alpha, vilken värld du än flyger i: ingen världsmultiplikator, ingen booster och ingen Premium-bonus ändrar dem. En våg betalar för sina utomjordingar **en gång** per omgång, hur ofta du än går och kommer tillbaka. Utbetalningen kommer när varje avsnitt av omgången tar slut: när du lämnar, dör, får slut på liv, ger upp eller klarar den. Nedgörningarna i ett avsnitt förblir obetalda bara vid wipen och vid en omstart av servern medan du är inne (din omgång förblir öppen, men nedgörningarna i det avsnittet går förlorade). Nedgörningar i en port räknas för de [uppdrag](/wiki/03-Mechanics/Quests.md#where-it-counts) som inte anger någon sektor (som de stora jakterna i Utmaningslinjen), i samma stund som de sker (en våg räknas för dem **en gång** per omgång, så som den också betalar en gång), och för inget annat: inte för nedgörningsstatistiken, prestationernas räknare, dödsloggen eller dina drönares och P.E.T.s erfarenhet. Erfarenhet och heder som de betalar räknas däremot för dina PvE-rankingpoäng, som erfarenhet och heder av en seger. Utomjordingarnas byte kommer med utbetalningen, rakt in i ditt inventarium.

<!-- solo-kills:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Utomjording | Krediter | Thulium | XP | Heder |
| :--- | ---: | ---: | ---: | ---: |
| **Seeker** | 1 000 | 4 | 100 | 2 |
| **Phantasm** | 3 000 | 12 | 300 | 6 |
| **Bulwark** | 5 000 | 25 | 800 | 10 |
| **Goombah** | 15 000 | 75 | 3 000 | 24 |
| **Crystalys** | 75 000 | 200 | 12 000 | 52 |
| **Boss Seeker** | 10 000 | 40 | 1 000 | 20 |
| **Seeker Slave** | 125 | 1 | 12 | 1 |
| **Boss Phantasm** | 39 000 | 195 | 7 800 | 62 |
| **Phantasm Guard** | 125 | 1 | 12 | 1 |
| **Boss Goombah** | 120 000 | 600 | 24 000 | 192 |
| **Goombah Guard** | 125 | 1 | 12 | 1 |
| **Boss Crystalys** | 393 750 | 1 050 | 63 000 | 273 |
| **Crystalys Guard** | 125 | 1 | 12 | 1 |
| **Evil Protos** | 4 250 | 17 | 725 | 6 |
| **Evil Kitefin** | 12 850 | 53 | 2 175 | 18 |
| **Evil Ostirion** | 34 350 | 141 | 5 800 | 48 |
| **Evil Nomad** | 59 600 | 245 | 10 060 | 84 |
| **Evil Paragon** | 68 700 | 283 | 11 600 | 97 |
| **Evil Storm** | 96 600 | 398 | 16 315 | 136 |
| **Evil Wraith** | 137 450 | 566 | 23 205 | 194 |
| **Evil Ironclad** | 268 450 | 1 105 | 45 330 | 379 |

| Port | Krediter | Thulium | XP | Heder |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 514 000 | 2 099 | 55 296 | 1 018 |
| **Beta Breach** | 1 298 500 | 5 939 | 187 744 | 2 470 |
| **Gamma Foundry** | 3 064 500 | 13 693 | 541 944 | 4 696 |
| **Delta Siege** | 5 239 625 | 22 338 | 882 676 | 7 850 |
| **Omega Vault** | 7 088 125 | 29 196 | 1 196 828 | 10 022 |
| **Davidski's Nightmare** | 7 081 950 | 29 124 | 1 196 445 | 9 968 |

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
