<!-- wiki-i18n source: 572c3cf8c7a4f519 -->
<!-- wiki-i18n title: Sköldar -->
# Sköldmekanik {#shield-mechanics}

Sköldar tar emot merparten av den inkommande skadan och skyddar skeppets skrov från direkt skada.

## Sköldberäkningar {#shield-calculations}

Skeppets slutliga sköldvärden beräknas så här:

\[\text{Slutlig sköldkapacitet} = \text{Total grundkapacitet} \times (1,0 + \text{Total sköldbonus i procent})\]
\[\text{Slutlig sköldladdningstakt} = \text{Total grundladdning} \times (1,0 + \text{Total sköldbonus i procent})\]

### 1. Platseffektivitet och avtagande avkastning {#1-slot-efficiency-diminishing-returns}

Liksom motorer sorteras utrustade sköldar (och hybridgeneratorer) efter kapacitet och påverkas av platseffektivitet (kärnplats: 100 %, stödplats: 75 %, hjälpplats: 50 %, en drönares plats: 100 %, som en kärnplats) och en kurva för avtagande avkastning utifrån deras rang. En sköld på en av dina [drönare](/wiki/03-Mechanics/Drones.md) rangordnas med skeppets egna:

- **1:a till 4:e skölden**: **100 %** (1,0) marginaleffektivitet.
- **5:e skölden**: **85 %** (0,85) marginaleffektivitet.
- **6:e skölden**: **70 %** (0,70) marginaleffektivitet.
- **7:e skölden**: **55 %** (0,55) marginaleffektivitet.
- **8:e och därefter**: **25 %** (0,25) marginaleffektivitet.

### 2. Sköldabsorption (skadefördelning) {#2-shield-absorbance-damage-split-}

Absorption är den andel av varje träff som dina sköldar tar; resten går direkt till träffpoängen (HP).
- **Per sköld**: en skölds absorption plus absorptionen hos de sköldceller som sitter i den. En sköld ensam har **45 till 50 %** (Light 45 %, Basic 48 %, Heavy 50 %); celler ger 2 till 10 punkter var (Basic +2 %, Advanced +4 %, Reinforced +6 %, Elite +7 %, Prime +8 %, Sovereign +10 %).
- **Genomsnittlig absorption**: skeppets absorption är det enkla medelvärdet över sköldarna i kärn-, stöd- och hjälpplatser och på dina drönare. Adaptiva kärnor har ingen egen absorption och räknas inte med i medelvärdet (celler i en adaptiv kärna ger bara kapacitet och laddning). Utan någon sköld utrustad är din absorption 0 %: skrovet tar varje träff, och sköldpoäng från celler i en adaptiv kärna används inte, så sätt dit en sköld också.
- **Mest rakt ur lådan är 80 %**: den bästa skölden med de bästa cellerna, en Heavy Shield Core med tre Sovereign-celler i varje plats. Blandar du in svagare sköldar sänks medelvärdet. Ingen buff från säsongsbutiken och ingen bonus från Smedjan ingår i det talet.
- **Exempel**: en Basic Shield Core (48 %) med två Advanced-celler ger 56 %; lägg till en Light Shield Core (45 %) och medelvärdet blir 50,5 %.
- **Värdet har inget tak vid 100 %.** Det är vad sköldarna skulle ta av en träff, innan angriparens *sköldgenomträngning* dras av, så ett skepp kan ha mer än en hel träff: 112 % tar fortfarande en hel träff från en angripare med upp till 12 % genomträngning.

#### Sköldgenomträngning {#shield-penetration}

Vissa attacker har en **sköldgenomträngning**: punkter som dras av från din absorption för den träffen. Den andel dina sköldar tar är

\[\text{Sköldandel} = \text{clamp}(\text{Absorption} - \text{Genomträngning},\ 0,\ 100\%)\]

- Sköldarna tar högst `round(damage x share)` av träffen; skrovet tar resten. En sköld som är för låg för sin andel för över skillnaden till HP, och är sköldarna på 0 går all skada direkt på HP.
- **Varifrån genomträngning kommer**: en enkelmålsrakets *sköldgenomträngning* (Lancet 10 %, Javelin 25 %, Harpoon 35 %, Rivet 5 %, Mallet 25 %, Piledriver 35 %, N.I.K.E. 35 %; områdesskada har ingen, se [Raketer](/wiki/05-Items/Rockets.md)) och laserammunitionens (Ultra Core 5 %, Experimental Fusion Core 10 %; se [Lasrar och ammunition](/wiki/05-Items/Lasers.md)). Utomjordingar har ingen, och det har inte heller x1- och x2-ammunitionen.
- **Exempel**: 80 % absorption mot en Harpoon (35 %): sköldarna tar 45 % av de 6 000, skrovet 55 %. 100 % mot den: 65 % och 35 %. 112 % mot 12 % genomträngning: hela träffen. 45 % (en Light Shield Core ensam) mot 35 %: 10 % på skölden, resten på skrovet. Ingen raket tränger helt igenom en Light Shield Core.
- Utomjordingar har inget absorptionsvärde: de delar varje träff 80 % / 20 %, minus träffens genomträngning.
- Skadan från en Siphon Battery tas enbart ur målets sköld: absorption och genomträngning spelar ingen roll.

#### Att nå och passera 100 % {#reaching-and-passing-100-}

- **Rakt ur lådan**: högst 80 % (se ovan).
- **Shield Absorbance Boost**: en permanent buff i säsongsbutiken som köps med wipepoäng, **+0,1 punkter per nivå, högst +10 punkter** (100 nivåer, 25 WP var). Den lägger fasta punkter på ditt skepps absorption, lika på alla skepp med sköld: 80 % blir 80,4 % med 4 nivåer (100 WP), och de 45 % som en Light Shield Core har blir 46,2 % med 12 nivåer (300 WP). Ett skepp utan sköld utrustad stannar på 0 %. De 100 nivåerna kostar 2 500 WP, ett mål för flera wipes: dagens källor till wipepoäng (milstolparna för nedskjutningar och uppdragen) betalar sammanlagt 855 WP vid sina tak, överförda över wipes, och det köper 34 nivåer, +3,4 punkter. Fler källor till wipepoäng är planerade. Se [Säsong och wipepoäng](/wiki/03-Mechanics/Wipe-Timeline.md#cross-season-progression-permanent-buffs-).
- **Smedjan**: sköldar och sköldceller kan få en bonus på **absorption**, som multiplicerar värdet: +5 % på en sköld med 50 % är +2,5 punkter. En fullt smidd bästa uppsättning på nivån Evig (kärna och tre celler, varje bonus slumpad till högsta nivå, +15 %) ger upp till 12 punkter, i snitt omkring 10 (se [Smedjan](/wiki/05-Items/Forge.md)).
- **Tillsammans**: 80 % rakt ur lådan, +3,4 punkters buff (alla dagens 855 wipepoäng) och upp till +12 punkter i bonusar från Smedjan blir som mest **95,4 %** i dag; med alla buffens 100 nivåer (+10 punkter, 2 500 WP) skulle det bli 102 %. Varken buffen eller Smedjan ensam når 100 %; att komma dit är ett mål för flera wipes, och fler källor till wipepoäng är planerade.

### Sköldförstärkningar: kapacitet, absorption, laddning {#shield-boosts-capacity-absorbance-recharge}

Varje sköldförstärkning höjer ett av de tre värdena och listas under sin egen sort i fönstret Boosters:

- **Kapacitet** (maximala sköldpoäng): Shield Wall-boosters och den permanenta förstärkningen Shield Capacity Boost.
- **Absorption** (den andel av en träff som dina sköldar tar): den permanenta förstärkningen Shield Absorbance Boost (+0,1 punkter per nivå, högst +10 punkter).
- **Laddning** (sköldpoäng som återställs per sekund): boostern Shield Regen.

Se [Boosters](/wiki/05-Items/Boosters.md) för siffrorna.

---

## Passiv sköldregenerering {#shield-passive-regeneration}

Sköldar regenereras passivt över tid så att du är redo för strid.

- **Regenereringstick**: Om sköldarna ligger under maximal kapacitet återställer de sköldpoäng motsvarande din laddningstakt per sekund.
- **Avbrott vid strid (15 s fördröjning)**: Regenereringen upphör när du tar skada och återupptas först efter **15 sekunder** utan skada.
