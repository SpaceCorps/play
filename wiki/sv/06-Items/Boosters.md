<!-- wiki-i18n source: bf2f009d73842c4b -->
<!-- wiki-i18n title: Boosters -->
# Boosters

<!-- wiki-search: damage amp; damage amp ii; shield wall; shield wall ii; hull plating; hull plating ii; shield regen; experience kit; honor beacon; resource magnet; loot luck -->

Boosters ger tillfälliga värdebonusar som stärker ditt skepps strid, försvar, nivåstigning och resursinsamling.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Föremålsträd {#item-tree}

Det som Monteringen tillverkar kräver först sin teknologi; håll pekaren över ett föremål för att se hur lång tid forskningen tar. Teknologiträdet, bränslet och boosten: [Forskning](/wiki/03-Mechanics/Research.md).

```tree
Experience Booster | booster, common | buy 8000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Honor Booster | booster, common | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Laser Damage Booster II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Regen Booster | booster, rare | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster I | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster I | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Resource Magnet Booster | booster, rare | buy 18000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Laser Damage Booster I | booster, rare | buy 20000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Loot Luck Booster | booster, legendary | buy 30000 Thulium | /wiki/06-Items/Boosters.md#active-boosters

Shield Wall Booster I -> Shield Wall Booster II
Hull Plating Booster I -> Hull Plating Booster II
Laser Damage Booster I -> Laser Damage Booster II
```
<!-- item-tree:end -->

## Staplingsregler {#stacking-rules}

Boosters använder ett additivt skalningssystem:
1. **Procentbonusar läggs ihop**: Köper du två olika boosters som båda ger +10 % laserskada får du en total bonus på **+20 % laserskada**.
2. **Varaktigheter staplas multiplikativt**: Köper du _samma_ booster flera gånger förlängs dess aktiva tid. Tidtagarna för _olika_ boosters löper parallellt.
3. **Tidsvy**: Aktiva boosters visas i HUD:en i fönstret Boosters, med de sammanlagda aktiva bonusarna grupperade och nästa utgångshändelse.

---

## Aktiva boosters {#active-boosters}

Varje booster varar i grundtiden **10 timmar** och aktiveras direkt när du köper, får eller hämtar den. De tre boostrarna **på andra nivån** (Laser Damage Booster II, Shield Wall Booster II och Hull Plating Booster II) säljs inte: du forskar fram deras teknologi i Skylab ([Forskning](/wiki/03-Mechanics/Research.md)) och tillverkar dem sedan i Monteringen, och när du hämtar en börjar dess 10 timmar direkt, som när du köper den.

| Namn | Sällsynthet | Grundeffekt (10 timmar) | Pris (Thulium) |
| :--- | :--- | :--- | :--- |
| **Laser Damage Booster I** | Sällsynt | +10 % laserskada | 20 000 |
| **Laser Damage Booster II** | Sällsynt | +10 % laserskada | Monteringen: 20 000 |
| **Shield Wall Booster I** | Sällsynt | +25 % sköldkapacitet (maximala sköldpoäng) | 15 000 |
| **Shield Wall Booster II** | Sällsynt | +25 % sköldkapacitet (maximala sköldpoäng) | Monteringen: 15 000 |
| **Hull Plating Booster I** | Sällsynt | +10 % maximala träffpoäng | 15 000 |
| **Hull Plating Booster II** | Sällsynt | +10 % maximala träffpoäng | Monteringen: 15 000 |
| **Shield Regen Booster** | Sällsynt | +25 % laddningstakt för sköldarna (sköldpoäng som återställs per sekund) | 10 000 |
| **Experience Booster** | Vanlig | +20 % mer erfarenhet | 8 000 |
| **Honor Booster** | Vanlig | +20 % mer heder | 10 000 |
| **Resource Magnet Booster** | Sällsynt | +25 % utbyte från lastlådor | 18 000 |
| **Loot Luck Booster** | Legendarisk | +5 % chans till sällsynta byten från NPC:er | 30 000 |

> [!NOTE]
> **Booster eller förstärkare?** De är olika saker. Varje booster har **Booster** i namnet, går på en timer och har inget att montera: **Laser Damage Booster I** och **Laser Damage Booster II** ger +10 % laserskada i 10 timmar, från butiken eller Monteringen. **Damage Amp**, **Crit Amp** och **Penetration Amp** (nivå I till IV) är laserförstärkare: moduler du monterar i en lasers förstärkarplats, utan timer ([Lasrar och ammunition](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-)). Före 0.4.12 hette boostersen Damage Amp och Damage Amp II, Shield Wall och Shield Wall II, Hull Plating och Hull Plating II, Shield Regen, Experience Kit, Honor Beacon, Resource Magnet och Loot Luck; de som gick hos dig fortsatte under de nya namnen.

---

## Sköldförstärkningar: tre slag {#shield-boosts-three-kinds}

Sköldar har tre separata värden, och varje sköldförstärkning höjer exakt ett av dem. Fönstret Boosters håller isär dem, med en ikon och en summa för vart och ett:

| Slag | Vad det är | Förstärkningar som höjer det |
| :--- | :--- | :--- |
| **Sköldkapacitet** | Dina maximala sköldpoäng | Shield Wall Booster I, Shield Wall Booster II, den permanenta buffen **Shield Capacity Boost** (säsongsbutiken) |
| **Sköldabsorption** | Den andel av varje träff som dina sköldar tar (resten träffar skrovet); den kan passera 100 % | Den permanenta buffen **Shield Absorbance Boost** (säsongsbutiken): +0,1 punkter per nivå för 25 WP, högst +10 punkter. Ingen booster höjer den |
| **Sköldladdning** | Sköldpoäng som återställs per sekund | Shield Regen Booster. Ingen permanent buff höjer den |

Förstärkningar av ett slag läggs ihop; de räknas aldrig mot ett annat slag. De permanenta buffarna beskrivs under [Framsteg över säsonger](/wiki/03-Mechanics/Wipe-Timeline.md); värdena själva under [Sköldmekanik](/wiki/03-Mechanics/Shields.md).
