<!-- wiki-i18n source: 630505c843ae163b -->
<!-- wiki-i18n title: Booster -->
# Booster {#boosters}

<!-- wiki-search: damage amp; damage amp ii; shield wall; shield wall ii; hull plating; hull plating ii; shield regen; experience kit; honor beacon; resource magnet; loot luck -->

Booster ändern deine Werte für begrenzte Zeit und stärken dein Schiff im Kampf und in der Verteidigung, beim Leveln und beim Sammeln von Ressourcen.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Gegenstandsbaum {#item-tree}

Was die Montage herstellt, braucht zuerst seine Technologie; zeige auf einen Gegenstand, um zu sehen, wie lange die Forschung dauert. Der Technologiebaum, der Treibstoff und der Boost: [Forschung](/wiki/03-Mechanics/Research.md).

```tree
Experience Booster | booster, common | buy 8000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Honor Booster | booster, common | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Laser Damage Booster 2 | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster 2 | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster 2 | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Regen Booster | booster, rare | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster 1 | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster 1 | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Resource Magnet Booster | booster, rare | buy 18000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Laser Damage Booster 1 | booster, rare | buy 20000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Loot Luck Booster | booster, legendary | buy 30000 Thulium | /wiki/06-Items/Boosters.md#active-boosters

Shield Wall Booster 1 -> Shield Wall Booster 2
Hull Plating Booster 1 -> Hull Plating Booster 2
Laser Damage Booster 1 -> Laser Damage Booster 2
```
<!-- item-tree:end -->

## Stapelregeln {#stacking-rules}

Booster skalieren additiv:
1. **Bonusprozente addieren sich**: Wenn du zwei verschiedene Booster kaufst, die beide +10 % Laserschaden geben, erhältst du insgesamt **+20 % Laserschaden**.
2. **Laufzeiten stapeln sich multiplikativ**: Kaufst du _denselben_ Booster mehrmals, verlängert sich seine aktive Laufzeit. Die Timer _verschiedener_ Booster laufen parallel.
3. **Timer-Ansicht**: Aktive Booster stehen im HUD im Booster-Fenster; es zeigt die zusammengefassten aktiven Boni und das nächste Ablaufereignis.

---

## Aktive Booster {#active-boosters}

Jeder Booster hat eine Grundlaufzeit von **10 Stunden** und wird sofort beim Kauf, Erhalt oder Abholen aktiv. Die drei **Booster der zweiten Stufe** (Laser Damage Booster 2, Shield Wall Booster 2 und Hull Plating Booster 2) werden nicht verkauft: Du erforschst ihre Technologie im Skylab ([Forschung](/wiki/03-Mechanics/Research.md)) und stellst sie dann in der Montage her, und wer einen abholt, startet seine 10 Stunden sofort, wie beim Kauf.

| Name | Seltenheit | Grundeffekt (10 Stunden) | Preis (Thulium) |
| :--- | :--- | :--- | :--- |
| **Laser Damage Booster 1** | Selten | +10 % Laserschaden | 20.000 |
| **Laser Damage Booster 2** | Selten | +10 % Laserschaden | Montage: 20.000 |
| **Shield Wall Booster 1** | Selten | +25 % Schildkapazität (maximale Schildpunkte) | 15.000 |
| **Shield Wall Booster 2** | Selten | +25 % Schildkapazität (maximale Schildpunkte) | Montage: 15.000 |
| **Hull Plating Booster 1** | Selten | +10 % max. Trefferpunkte | 15.000 |
| **Hull Plating Booster 2** | Selten | +10 % max. Trefferpunkte | Montage: 15.000 |
| **Shield Regen Booster** | Selten | +25 % Aufladerate der Schilde (pro Sekunde wiederhergestellte Schildpunkte) | 10.000 |
| **Experience Booster** | Gewöhnlich | +20 % EP-Gewinn | 8.000 |
| **Honor Booster** | Gewöhnlich | +20 % Gewinn an Ehrenpunkten | 10.000 |
| **Resource Magnet Booster** | Selten | +25 % Ertrag der Frachtkisten | 18.000 |
| **Loot Luck Booster** | Legendär | +5 % Chance auf seltene Beute von NPCs | 30.000 |

> [!NOTE]
> **Booster oder Amp?** Das sind zwei verschiedene Dinge. Jeder Booster hat **Booster** im Namen, läuft auf einem Timer und braucht nichts zum Einsetzen: **Laser Damage Booster 1** und **Laser Damage Booster 2** geben +10 % Laserschaden für 10 Stunden, aus dem Shop oder aus der Montage. **Damage Amp**, **Crit Amp** und **Penetration Amp** (Stufen I bis IV) sind Laserverstärker: Module, die du in den Verstärker-Slot eines Lasers einsetzt, ohne Timer ([Laser & Munition](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-)). Vor 0.4.12 hießen die Booster Damage Amp und Damage Amp II, Shield Wall und Shield Wall II, Hull Plating und Hull Plating II, Shield Regen, Experience Kit, Honor Beacon, Resource Magnet und Loot Luck; die Booster, die bei dir liefen, liefen unter den neuen Namen weiter.

---

## Schildboosts: drei Arten {#shield-boosts-three-kinds}

Schilde haben drei getrennte Werte, und jeder Schildboost erhöht genau einen davon. Das Booster-Fenster hält sie auseinander, mit einem Symbol und einer Summe für jeden:

| Art | Was es ist | Boosts, die ihn erhöhen |
| :--- | :--- | :--- |
| **Schildkapazität** | Deine maximalen Schildpunkte | Shield Wall Booster 1, Shield Wall Booster 2, der dauerhafte **Schildkapazitäts-Boost** (Saison-Shop) |
| **Schildabsorption** | Der Anteil jedes Treffers, den deine Schilde nehmen (den Rest bekommt die Hülle); er kann 100 % übersteigen | Der dauerhafte **Schildabsorptions-Boost** (Saison-Shop): +0,1 Punkte pro Level für 25 WP, höchstens +10 Punkte. Kein Booster erhöht ihn |
| **Schildaufladung** | Pro Sekunde wiederhergestellte Schildpunkte | Shield Regen Booster. Kein dauerhafter Buff erhöht sie |

Boosts einer Art addieren sich; sie zählen nie für eine andere Art. Die dauerhaften Buffs sind unter [Saisonübergreifender Fortschritt](/wiki/03-Mechanics/Wipe-Timeline.md) beschrieben, die Werte selbst unter [Schildmechanik](/wiki/03-Mechanics/Shields.md).
