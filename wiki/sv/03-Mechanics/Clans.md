<!-- wiki-i18n source: 21f10d185095b346 -->
<!-- wiki-i18n title: Klaner -->
# Klaner {#clans}

Att grunda eller gå med i en klan gör att du kan slå ihop resurser, uppgradera en gemensam bank, ställa in skattesatser, samordna dig med fraktionens medlemmar och hantera diplomati.

## Klanens utveckling {#clan-progression}

Klaner börjar på nivå 1 och kan uppgraderas till nivå 5. För att uppgradera klanen måste krediter betalas från **Klanbanken**. Uppgraderingar ökar medlemskapaciteten och de dagliga utbetalningsgränserna.

| Klannivå | Medlemsgräns | Daglig utbetalningsgräns (per medlem) | Uppgraderingskostnad (krediter) |
| :---: | :---: | :---: | :--- |
| **Nivå 1** | 10 | 1 000 000 KRD | — |
| **Nivå 2** | 25 | 2 000 000 KRD | 10 000 000 KRD |
| **Nivå 3** | 50 | 3 000 000 KRD | 100 000 000 KRD |
| **Nivå 4** | 75 | 4 000 000 KRD | 1 000 000 000 KRD |
| **Nivå 5** | 100 | 5 000 000 KRD | 10 000 000 000 KRD |

---

## Klanekonomi och beskattning {#clan-economy-taxation}

Klaner drivs av ett skattebaserat ekonomiskt system:

### 1. Daglig skatt {#1-daily-taxation}

- **Skattesats**: Ledaren eller vice ledarna kan ställa in en daglig skattesats mellan **0 % och 5 %**.
- **Automatisk indrivning**: En gång per dag (UTC) tar servern automatiskt ut skatt från alla klanmedlemmar.
- **Formel**: Skatten beräknas som `ClanTaxRate` av varje medlems aktuella kreditsaldo.
  - *Exempel*: Om du har 10 000 000 krediter och klanskatten är 2 % dras 200 000 krediter från ditt konto och sätts in i Klanbanken.
  - Frivilliga kreditdonationer kan också göras, upp till gränsen i nästa avsnitt.

### 2. Donationer {#2-donations}

- **Donera**: alla medlemmar kan skicka krediter till Klanbanken från sidan Klan. Dialogrutan visar vad du fortfarande kan skicka.
- **Donationsgräns**: en pilot kan skicka högst **1 000 000 krediter till klaner under valfria 24 timmar**, räknat över alla klaner piloten har varit med i. Att lämna en klan och gå med i en annan ger ingen ny gräns.
- **Ingen daglig nollställning**: de 24 timmarna glider. Varje donation slutar räknas exakt 24 timmar efter att den gjordes, och dialogrutan visar när den äldsta gör det och hur mycket som kommer tillbaka. En donation över det som är kvar avvisas helt.
- Den dagliga skatten är ingen donation och förbrukar inte din gräns.

### 3. Utbetalningar från banken {#3-bank-payouts}

- **Utbetalningsgränser**: Klanens ledare och officerare kan fördela krediter från Klanbanken till enskilda medlemmar.
- **Daglig gräns**: En medlem kan inte ta emot mer än `1,000,000 * ClanLevel` krediter i utbetalningar under en enda kalenderdag (UTC).

---

## Hierarki och roller {#hierarchy-roles}

Klaner använder en rollbaserad gradstruktur för att hantera behörigheter:

- **Ledare (roll 3)**: Har full administrativ åtkomst, inklusive uppgradering, att ställa in skatter, diplomati, befordringar, att avskeda medlemmar och att upplösa klanen.
- **Vice ledare (roll 2)**: Kan ställa in skattesatser, betala ut krediter, hantera diplomati och befordra eller degradera lägre grader.
- **Äldste (roll 1)**: Betrodd medlem som kan godkänna nya ansökningar till klanen.
- **Medlem (roll 0)**: Vanlig spelare utan administrativa behörigheter.

### Behörighetstabell {#permissions-table}

| Åtgärd | Ledare | Vice ledare | Äldste | Medlem |
| :--- | :---: | :---: | :---: | :---: |
| **Upplösa klanen** | ✅ | ❌ | ❌ | ❌ |
| **Uppgradera klanen** | ✅ | ❌ | ❌ | ❌ |
| **Ställa in skattesats** | ✅ | ✅ | ❌ | ❌ |
| **Betala ut krediter** | ✅ | ✅ | ❌ | ❌ |
| **Hantera diplomati** | ✅ | ✅ | ❌ | ❌ |
| **Befordra / avskeda** | ✅ | ✅* | ❌ | ❌ |
| **Godkänna ansökningar** | ✅ | ✅ | ✅ | ❌ |

*\*Vice ledare kan bara befordra, degradera eller avskeda medlemmar med lägre grad än sin egen.*

### När ledaren lämnar {#when-the-leader-leaves}

En ledare kan inte lämna en klan som fortfarande har andra medlemmar: befordra först en vice ledare till ledare (ledaren går då ner till vice ledare), eller lämna sist, vilket upplöser klanen. Om ledaren raderar sitt konto (Inställningar › Konto) går ledarskapet till den medlem som har högst grad, vid lika den som varit med längst; en ledare som är ensam i klanen upplöser den, banken inräknad.

---

## Diplomati {#diplomacy}

Klaner kan upprätta formella diplomatiska förbindelser med andra organisationer genom att ange målklanens tagg:

- **Allians**: Formellt allierade klaner. Vänlig status visas på kartan.
- **Icke-angreppspakt (NAP)**: Man kommer överens om att inte inleda fientligheter.
- **Krig**: Formell krigsförklaring. Krigsmål kan angripas var som helst utan straff.

---

## Ta med en vän {#bringing-a-friend}

En vän som är ny i spelet kan gå med med din personliga inbjudningskod och får ett startpaket; se [Bjud in vänner](/wiki/03-Mechanics/Invite-Friends.md). Väl i spelet kan vännen ansöka till din klan som vilken pilot som helst.
