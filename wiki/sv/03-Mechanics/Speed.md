<!-- wiki-i18n source: 431a488ba7a0842e -->
<!-- wiki-i18n title: Hastighet -->
# Hastighetsberäkning {#speed-calculation}

Hastigheten avgör hur snabbt ditt skepp rör sig på rymdkartan, så att du kan jaga mål, ta dig ur strid eller färdas mellan zoner.

## Hastighetsformeln {#the-speed-formula}

Skeppets slutliga hastighet beräknas på servern med följande formel:

\[\text{Slutlig hastighet} = (\text{Skeppets grundhastighet} + \text{Motorernas totala hastighet}) \times (1,0 + \text{Total fartbonus i procent})\]

### 1. Motorns effektiva hastighet {#1-effective-engine-speed}

Varje utrustad motor ger hastighet. Om det sitter styrraketer i motorn ändras dess hastighet:

\[\text{Motorhastighet} = (\text{Motorns grundhastighet} \times \text{Styrraketmultiplikator}) + \text{Fast styrraketbonus}\]

- **Styrraketmultiplikator**: Produkten av alla hastighetsmultiplikatorer hos de styrraketer som sitter i den motorn (t.ex. är Thruster III `1.1` eller `+10%`).
- **Fast styrraketbonus**: Summan av alla fasta hastighetstillägg från styrraketer (t.ex. är Thruster III `+15` hastighet).

### 2. Avtagande avkastning (marginaleffektivitet) {#2-diminishing-returns-marginal-efficiency-}

För att ingen ska kunna stapla oändligt många motorer för oändlig hastighet används en kurva för **avtagande avkastning (marginaleffektivitet)**. Alla motorer sorteras efter sitt hastighetsbidrag och behandlas i ordning. Adaptiva kärnor (hybrider) och sköldar rangordnas på samma sätt, varje slag i en egen grupp, så ett skepp med både motorer och adaptiva kärnor har en egen topp fyra av varje slag:

| Motorrang | Effektivitetsmultiplikator |
| :---: | :--- |
| **1:a till 4:e** | **100 %** (1,0) |
| **5:e** | **85 %** (0,85) |
| **6:e** | **70 %** (0,70) |
| **7:e** | **55 %** (0,55) |
| **8:e och därefter** | **25 %** (0,25) |

Dessutom multipliceras motorns hastighet med platsens effektivitet (kärnplats: 100 %, stödplats: 75 %, hjälpplats: 50 %).

### 3. Fartbonus i procent och sköldavdrag {#3-speed-bonus-percent-shield-penalties}

Den totala fartbonusen i procent är summan av alla fartbonusar från utrustade motorer (och hybrider) minus avdragen från utrustade sköldar:

- **Motorernas fartbonus**: Motorer ger positiva fartprocent (t.ex. ger Engine III `+5%`).
- **Sköldarnas fartavdrag**: Tunga sköldar tynger ner ditt skepp och ger negativa fartprocent (t.ex. ger Heavy Shield Core `-5%` fart).
- **Skalning efter plats**: De här procentbonusarna och avdragen skalas också med effektiviteten hos platsen där föremålet sitter. En sköld på en av dina drönare bromsar dig lika mycket som en sköld på en kärnplats.
- **Aldrig under noll**: hur många sköldar du än bär går din hastighet inte under 0.
