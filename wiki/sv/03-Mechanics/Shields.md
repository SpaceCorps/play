<!-- wiki-i18n source: 7af844c9c2785078 -->
<!-- wiki-i18n title: Sköldar -->
# Sköldmekanik {#shield-mechanics}

Sköldar tar emot merparten av den inkommande skadan och skyddar skeppets skrov från direkt skada.

## Sköldberäkningar {#shield-calculations}

Skeppets slutliga sköldvärden beräknas så här:

\[\text{Slutlig sköldkapacitet} = \text{Total grundkapacitet} \times (1,0 + \text{Total sköldbonus i procent})\]
\[\text{Slutlig sköldladdningstakt} = \text{Total grundladdning} \times (1,0 + \text{Total sköldbonus i procent})\]

### 1. Platseffektivitet och avtagande avkastning {#1-slot-efficiency-diminishing-returns}

Liksom motorer sorteras utrustade sköldar (och hybridgeneratorer) med de bästa först och påverkas av platseffektivitet (kärnplats: 100 %, stödplats: 75 %, hjälpplats: 50 %, en drönares plats: 100 %, som en kärnplats) och en kurva för avtagande avkastning utifrån deras rang. En sköld rangordnas efter vad som räknas av den: dess kapacitet gånger platsens andel. Återladdningen har en egen ordning (dess värde gånger platsens andel), och de **fyra bästa** sköldbonusarna räknas. En sköld på en av dina [drönare](/wiki/03-Mechanics/Drones.md) rangordnas med skeppets egna:

- **1:a till 4:e skölden**: **100 %** (1,0) marginaleffektivitet.
- **5:e skölden**: **85 %** (0,85) marginaleffektivitet.
- **6:e skölden**: **70 %** (0,70) marginaleffektivitet.
- **7:e skölden**: **55 %** (0,55) marginaleffektivitet.
- **8:e och därefter**: **50 %** (0,50) marginaleffektivitet. (Till och med version 0.4.7 var det 25 %, som för motorerna; motorerna har kvar 25 %, se [Hastighet](/wiki/03-Mechanics/Speed.md).)

**Mer utrustning sänker aldrig din sköld.** Att lägga till en sköld eller en sköldcell sänker aldrig din sköldkapacitet eller din återladdning: varje tal rangordnas med det bästa först efter vad som räknas, så en ny del tar den plats den förtjänar. Absorptionen är medelvärdet av dina sköldar, så den sänks av en ny sköld som är svagare än ditt medelvärde; en cell sänker den aldrig.

**Hangaren visar det.** En sköld, en motor eller en adaptiv kärna som inte räknas med hela sin styrka har en liten procentsats på sin plats (till exempel `64%`: den 5:e skölden, 85 %, på en stödplats, 75 %), och håller du pekaren över den visas uppdelningen. Håll pekaren över rutorna Sköldar och Hastighet bland stridsvärdena för att se dina föremål efter plats och vad en till skulle räknas för. Skeppsfönstret under flygning visar samma listor när du håller pekaren över sköldmätaren och hastigheten.

### 2. Sköldabsorption (skadefördelning) {#2-shield-absorbance-damage-split-}

Absorption är den andel av varje träff som dina sköldar tar; resten går direkt till träffpoängen (HP).
- **Per sköld**: en skölds absorption plus absorptionen hos de sköldceller som sitter i den. En sköld ensam har **45 till 50 %** (Light 45 %, Basic 48 %, Heavy 50 %); celler ger 2 till 10 punkter var (Capacity Shield Cell I–IV +2 %, +3 %, +4 %, +5 %; Absorption Shield Cell I–IV +4 %, +6 %, +8 %, +10 %).
- **Genomsnittlig absorption**: skeppets absorption är det enkla medelvärdet över sköldarna i kärn-, stöd- och hjälpplatser och på dina drönare. Adaptiva kärnor har ingen egen absorption och räknas inte med i medelvärdet (celler i en adaptiv kärna ger bara kapacitet och laddning). Utan någon sköld utrustad är din absorption 0 %: skrovet tar varje träff, och sköldpoäng från celler i en adaptiv kärna används inte, så sätt dit en sköld också.
- **Mest rakt ur lådan är 80 %**: den bästa skölden med de bästa cellerna, en Heavy Shield Core med tre Absorption Shield Cell IV i varje plats. Blandar du in svagare sköldar sänks medelvärdet. Ingen buff från säsongsbutiken och ingen bonus från Smedjan ingår i det talet.
- **Exempel**: en Basic Shield Core (48 %) med två Absorption Shield Cell I ger 56 %; lägg till en Light Shield Core (45 %) och medelvärdet blir 50,5 %.
- **Värdet har inget tak vid 100 %.** Det är vad sköldarna skulle ta av en träff, innan angriparens *sköldgenomträngning* dras av, så ett skepp kan ha mer än en hel träff: 112 % tar fortfarande en hel träff från en angripare med upp till 12 % genomträngning.

#### Sköldgenomträngning {#shield-penetration}

Vissa attacker har en **sköldgenomträngning**: punkter som dras av från din absorption för den träffen. Den andel dina sköldar tar är

\[\text{Sköldandel} = \text{clamp}(\text{Absorption} - \text{Genomträngning},\ 0,\ 100\%)\]

- Sköldarna tar högst `round(damage x share)` av träffen; skrovet tar resten. En sköld som är för låg för sin andel för över skillnaden till HP, och är sköldarna på 0 går all skada direkt på HP.
- **Varifrån genomträngning kommer**: en enkelmålsrakets *sköldgenomträngning* (Lancet I 10 %, Lancet II 25 %, Lancet III 35 %, Rivet I 5 %, Rivet II 25 %, Rivet III 35 %, N.I.K.E. 35 %; områdesskada har ingen, se [Raketer](/wiki/06-Items/Rockets.md)) och laserammunitionens (Ultra Core 5 %, Experimental Fusion Core 10 %; se [Lasrar och ammunition](/wiki/06-Items/Lasers.md)). Utomjordingar har ingen, och det har inte heller x1- och x2-ammunitionen. En laserträff drar också av Penetration Amps i skyttens lasrar (+2 % till +8 % per plats, medelvärdet över dess lasrar) och en drönarformations genomträngning (Gemini +9 %, Stiletto +16 %): summan stannar vid **50 %** för en laser och vid 40 % för en raket ([så läggs en laserträff ihop](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)).
- **Exempel**: 80 % absorption mot en Lancet III (35 %): sköldarna tar 45 % av träffen, skrovet 55 %. 100 % mot den: 65 % och 35 %. 112 % mot 12 % genomträngning: hela träffen. 45 % (en Light Shield Core ensam) mot 35 %: 10 % på skölden, resten på skrovet. Ingen raket tränger helt igenom en Light Shield Core. Den bästa lasern (50 %) klarar det: mot den tar den bästa skölden (80 %) 30 % av träffen och skrovet 70 %, och en Light Shield Core ensam (45 %) tar ingenting.
- Utomjordingar har inget absorptionsvärde: de delar varje träff 80 % / 20 %, minus träffens genomträngning.
- Skadan från en Siphon Battery tas enbart ur målets sköld: absorption och genomträngning spelar ingen roll.

#### Att nå och passera 100 % {#reaching-and-passing-100-}

- **Rakt ur lådan**: högst 80 % (se ovan).
- **Shield Absorbance Boost**: en permanent buff i säsongsbutiken som köps med wipepoäng, **+0,1 punkter per nivå, högst +10 punkter** (100 nivåer, 25 WP var). Den lägger fasta punkter på ditt skepps absorption, lika på alla skepp med sköld: 80 % blir 80,4 % med 4 nivåer (100 WP), och de 45 % som en Light Shield Core har blir 46,2 % med 12 nivåer (300 WP). Ett skepp utan sköld utrustad stannar på 0 %. De 100 nivåerna kostar 2 500 WP, ett mål för flera wipes: dagens källor till wipepoäng (milstolparna för nedskjutningar och uppdragen) betalar sammanlagt 855 WP vid sina tak, överförda över wipes, och det köper 34 nivåer, +3,4 punkter. Fler källor till wipepoäng är planerade. Se [Säsong och wipepoäng](/wiki/03-Mechanics/Wipe-Timeline.md#cross-season-progression-permanent-buffs-).
- **Smedjan**: sköldar och sköldceller kan få en bonus på **absorption**, som multiplicerar värdet: +5 % på en sköld med 50 % är +2,5 punkter. En fullt smidd bästa uppsättning på nivån Evig (kärna och tre celler, varje bonus slumpad till högsta nivå, +15 %) ger upp till 12 punkter, i snitt omkring 10 (se [Smedjan](/wiki/06-Items/Forge.md)).
- **Tillsammans**: 80 % rakt ur lådan, +3,4 punkters buff (alla dagens 855 wipepoäng) och upp till +12 punkter i bonusar från Smedjan blir som mest **95,4 %** i dag; med alla buffens 100 nivåer (+10 punkter, 2 500 WP) skulle det bli 102 %. Varken buffen eller Smedjan ensam når 100 %; att komma dit är ett mål för flera wipes, och fler källor till wipepoäng är planerade.

### Sköldförstärkningar: kapacitet, absorption, laddning {#shield-boosts-capacity-absorbance-recharge}

Varje sköldförstärkning höjer ett av de tre värdena och listas under sin egen sort i fönstret Boosters:

- **Kapacitet** (maximala sköldpoäng): Shield Wall Booster 1 och 2 och den permanenta förstärkningen Shield Capacity Boost.
- **Absorption** (den andel av en träff som dina sköldar tar): den permanenta förstärkningen Shield Absorbance Boost (+0,1 punkter per nivå, högst +10 punkter).
- **Laddning** (sköldpoäng som återställs per sekund): Shield Regen Booster.

Se [Boosters](/wiki/06-Items/Boosters.md) för siffrorna.

---

## Passiv sköldregenerering {#shield-passive-regeneration}

Sköldar regenereras passivt över tid så att du är redo för strid.

- **Regenereringstick**: Om sköldarna ligger under maximal kapacitet återställer de sköldpoäng motsvarande din laddningstakt per sekund.
- **Avbrott vid strid (15 s fördröjning)**: Regenereringen upphör när du tar skada och återupptas först efter **15 sekunder** utan skada. Drönarformationerna Adamant och Redoubt ([Drönarformationer](/wiki/03-Mechanics/Formations.md)) är undantaget: de ger tillbaka sköld varje sekund, även i strid.
