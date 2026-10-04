<!-- wiki-i18n source: 539575474f5854de -->
<!-- wiki-i18n title: Booster -->
# Booster {#boosters}

Booster ändern deine Werte für begrenzte Zeit und stärken dein Schiff im Kampf und in der Verteidigung, beim Leveln und beim Sammeln von Ressourcen.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Gegenstandsbaum {#item-tree}

Was die Montage herstellt, braucht zuerst seine Technologie; zeige auf einen Gegenstand, um zu sehen, wie lange die Forschung dauert. Der Technologiebaum, der Treibstoff und der Boost: [Forschung](/wiki/03-Mechanics/Research.md).

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

## Stapelregeln {#stacking-rules}

Booster skalieren additiv:
1. **Bonusprozente addieren sich**: Wenn du zwei verschiedene Booster kaufst, die beide +10 % Laserschaden geben, erhältst du insgesamt **+20 % Laserschaden**.
2. **Laufzeiten stapeln sich multiplikativ**: Kaufst du _denselben_ Booster mehrmals, verlängert sich seine aktive Laufzeit. Die Timer _verschiedener_ Booster laufen parallel.
3. **Timer-Ansicht**: Aktive Booster stehen im HUD im Booster-Fenster; es zeigt die zusammengefassten aktiven Boni und das nächste Ablaufereignis.

---

## Aktive Booster {#active-boosters}

Jeder Booster hat eine Grundlaufzeit von **10 Stunden** und wird sofort beim Kauf, Erhalt oder Abholen aktiv. Die drei **II**-Booster werden nicht verkauft: Du erforschst ihre Technologie im Skylab ([Forschung](/wiki/03-Mechanics/Research.md)) und stellst sie dann in der Montage her, und wer einen abholt, startet seine 10 Stunden sofort, wie beim Kauf.

| Name | Seltenheit | Grundeffekt (10 Stunden) | Preis (Thulium) |
| :--- | :--- | :--- | :--- |
| **Damage Amp** | Selten | +10 % Laserschaden | 20.000 |
| **Damage Amp II** | Selten | +10 % Laserschaden | Montage: 20.000 |
| **Shield Wall** | Selten | +25 % Schildkapazität (maximale Schildpunkte) | 15.000 |
| **Shield Wall II** | Selten | +25 % Schildkapazität (maximale Schildpunkte) | Montage: 15.000 |
| **Hull Plating** | Selten | +10 % max. Trefferpunkte | 15.000 |
| **Hull Plating II** | Selten | +10 % max. Trefferpunkte | Montage: 15.000 |
| **Shield Regen** | Selten | +25 % Aufladerate der Schilde (pro Sekunde wiederhergestellte Schildpunkte) | 10.000 |
| **Experience Kit** | Gewöhnlich | +20 % EP-Gewinn | 8.000 |
| **Honor Beacon** | Gewöhnlich | +20 % Gewinn an Ehrenpunkten | 10.000 |
| **Resource Magnet** | Selten | +25 % Ertrag der Frachtkisten | 18.000 |
| **Loot Luck** | Legendär | +5 % Chance auf seltene Beute von NPCs | 30.000 |

---

## Schildboosts: drei Arten {#shield-boosts-three-kinds}

Schilde haben drei getrennte Werte, und jeder Schildboost erhöht genau einen davon. Das Booster-Fenster hält sie auseinander, mit einem Symbol und einer Summe für jeden:

| Art | Was es ist | Boosts, die ihn erhöhen |
| :--- | :--- | :--- |
| **Schildkapazität** | Deine maximalen Schildpunkte | Shield Wall, Shield Wall II, der dauerhafte **Schildkapazitäts-Boost** (Saison-Shop) |
| **Schildabsorption** | Der Anteil jedes Treffers, den deine Schilde nehmen (den Rest bekommt die Hülle); er kann 100 % übersteigen | Der dauerhafte **Schildabsorptions-Boost** (Saison-Shop): +0,1 Punkte pro Level für 25 WP, höchstens +10 Punkte. Kein Booster erhöht ihn |
| **Schildaufladung** | Pro Sekunde wiederhergestellte Schildpunkte | Shield Regen. Kein dauerhafter Buff erhöht sie |

Boosts einer Art addieren sich; sie zählen nie für eine andere Art. Die dauerhaften Buffs sind unter [Saisonübergreifender Fortschritt](/wiki/03-Mechanics/Wipe-Timeline.md) beschrieben, die Werte selbst unter [Schildmechanik](/wiki/03-Mechanics/Shields.md).
