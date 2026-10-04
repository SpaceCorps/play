<!-- wiki-i18n source: 539575474f5854de -->
<!-- wiki-i18n title: Boosters -->
# Boosters {#boosters}

Boosters ger tillfälliga värdebonusar som stärker ditt skepps strid, försvar, nivåstigning och resursinsamling.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Föremålsträd {#item-tree}

Det som Monteringen tillverkar kräver först sin teknologi; håll pekaren över ett föremål för att se hur lång tid forskningen tar. Teknologiträdet, bränslet och boosten: [Forskning](/wiki/03-Mechanics/Research.md).

```tree
Experience Kit | booster, common | buy 8000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Honor Beacon | booster, common | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Damage Amp II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Regen | booster, rare | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Resource Magnet | booster, rare | buy 18000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Damage Amp | booster, rare | buy 20000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Loot Luck | booster, legendary | buy 30000 Thulium | /wiki/06-Items/Boosters.md#active-boosters

Shield Wall -> Shield Wall II
Hull Plating -> Hull Plating II
Damage Amp -> Damage Amp II
```
<!-- item-tree:end -->

## Staplingsregler {#stacking-rules}

Boosters använder ett additivt skalningssystem:
1. **Procentbonusar läggs ihop**: Köper du två olika boosters som båda ger +10 % laserskada får du en total bonus på **+20 % laserskada**.
2. **Varaktigheter staplas multiplikativt**: Köper du _samma_ booster flera gånger förlängs dess aktiva tid. Tidtagarna för _olika_ boosters löper parallellt.
3. **Tidsvy**: Aktiva boosters visas i HUD:en i fönstret Boosters, med de sammanlagda aktiva bonusarna grupperade och nästa utgångshändelse.

---

## Aktiva boosters {#active-boosters}

Varje booster varar i grundtiden **10 timmar** och aktiveras direkt när du köper, får eller hämtar den. De tre **II**-boostrarna säljs inte: du forskar fram deras teknologi i Skylab ([Forskning](/wiki/03-Mechanics/Research.md)) och tillverkar dem sedan i Monteringen, och när du hämtar en börjar dess 10 timmar direkt, som när du köper den.

| Namn | Sällsynthet | Grundeffekt (10 timmar) | Pris (Thulium) |
| :--- | :--- | :--- | :--- |
| **Damage Amp** | Sällsynt | +10 % laserskada | 20 000 |
| **Damage Amp II** | Sällsynt | +10 % laserskada | Monteringen: 20 000 |
| **Shield Wall** | Sällsynt | +25 % sköldkapacitet (maximala sköldpoäng) | 15 000 |
| **Shield Wall II** | Sällsynt | +25 % sköldkapacitet (maximala sköldpoäng) | Monteringen: 15 000 |
| **Hull Plating** | Sällsynt | +10 % maximala träffpoäng | 15 000 |
| **Hull Plating II** | Sällsynt | +10 % maximala träffpoäng | Monteringen: 15 000 |
| **Shield Regen** | Sällsynt | +25 % laddningstakt för sköldarna (sköldpoäng som återställs per sekund) | 10 000 |
| **Experience Kit** | Vanlig | +20 % mer erfarenhet | 8 000 |
| **Honor Beacon** | Vanlig | +20 % mer heder | 10 000 |
| **Resource Magnet** | Sällsynt | +25 % utbyte från lastlådor | 18 000 |
| **Loot Luck** | Legendarisk | +5 % chans till sällsynta byten från NPC:er | 30 000 |

---

## Sköldförstärkningar: tre slag {#shield-boosts-three-kinds}

Sköldar har tre separata värden, och varje sköldförstärkning höjer exakt ett av dem. Fönstret Boosters håller isär dem, med en ikon och en summa för vart och ett:

| Slag | Vad det är | Förstärkningar som höjer det |
| :--- | :--- | :--- |
| **Sköldkapacitet** | Dina maximala sköldpoäng | Shield Wall, Shield Wall II, den permanenta buffen **Shield Capacity Boost** (säsongsbutiken) |
| **Sköldabsorption** | Den andel av varje träff som dina sköldar tar (resten träffar skrovet); den kan passera 100 % | Den permanenta buffen **Shield Absorbance Boost** (säsongsbutiken): +0,1 punkter per nivå för 25 WP, högst +10 punkter. Ingen booster höjer den |
| **Sköldladdning** | Sköldpoäng som återställs per sekund | Shield Regen. Ingen permanent buff höjer den |

Förstärkningar av ett slag läggs ihop; de räknas aldrig mot ett annat slag. De permanenta buffarna beskrivs under [Framsteg över säsonger](/wiki/03-Mechanics/Wipe-Timeline.md); värdena själva under [Sköldmekanik](/wiki/03-Mechanics/Shields.md).
