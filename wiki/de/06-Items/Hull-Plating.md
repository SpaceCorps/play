<!-- wiki-i18n source: 2bd1925e336e25b6 -->
<!-- wiki-i18n title: Hüllenpanzerung -->
# Hüllenpanzerung {#hull-plating}

<!-- wiki-search: hull plate; hull plate slot; hull plate slots; plate slot; plate; armour; armor; hpl; panzerung; panzerungs-slot; panzerungsplatte -->

Die Erforschung des Dormant-Schwarms zeigte Fortschritte in der Panzerungstechnik. Mit dieser Technik können Schiffe ihre Hülle verbessern: **Hüllenpanzerung** ist eine Panzerung, die in einen Hüllenplatten-Slot eines hergestellten Schiffs passt und ihm Hüllenpunkte hinzufügt. Sie ist nicht der Hull Plating **Booster** der Seite [Booster](/wiki/06-Items/Boosters.md), ein Bonus auf Zeit.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Gegenstandsbaum {#item-tree}

Was die Montage herstellt, braucht zuerst seine Technologie; zeige auf einen Gegenstand, um zu sehen, wie lange die Forschung dauert. Der Technologiebaum, der Treibstoff und der Boost: [Forschung](/wiki/03-Mechanics/Research.md).

```tree
Hull Plating I | hull-plating, uncommon | buy 5000 Thulium | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating II | hull-plating, rare | craft 2500 Thulium, 300 s | research 86400 s, 86400 science, 25 Dark Matter | 1 Hull Plating I, 150 Ship Fragment, 20 Reinforced Hull Plate, 6 Power Core, 5 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating III | hull-plating, epic | craft 4000 Thulium, 600 s | research 172800 s, 172800 science, 40 Dark Matter | 1 Hull Plating II, 300 Ship Fragment, 40 Reinforced Hull Plate, 12 Power Core, 1 Ancient Control Unit, 8 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings

Hull Plating I => Hull Plating II => Hull Plating III
```
<!-- item-tree:end -->

## Die drei Panzerungen {#the-three-platings}

| Gegenstand | Hinzugefügte Hülle | Woher er kommt |
| :--- | ---: | :--- |
| **Hull Plating I** | 5.000 | Shop, 5.000 Thulium |
| **Hull Plating II** | 10.000 | Montage, aus einer Hull Plating I |
| **Hull Plating III** | 15.000 | Montage, aus einer Hull Plating II |

Hull Plating I wird gekauft. **II und III sind Aufwertungen**: Die Montage verbraucht eine Panzerung der Stufe darunter (lose in deinem Inventar) und verlangt Thulium, Materialien und **Dark Matter Plates**, 5 für die II und 8 für die III, wo die letzte Stufe jedes anderen Ausrüstungsstücks 3 verlangt. Jede braucht zuerst ihre Technologie, im Hull-Plating-Baum der Seite [Forschung](/wiki/03-Mechanics/Research.md#tree-hull-plating): 1 Tag und 25 Dark Matter für die II, 2 Tage und 40 für die III, zusätzlich zur Technologie der Dark Matter Plate selbst. Der Baum oben zeigt die Preise, die Materialien und die Zeiten.

Die [Schmiede](/wiki/06-Items/Forge.md) nimmt jede Panzerung an, und eine Aufwertung behält die Schmiedestufe der verbrauchten Panzerung und würfelt ihren Bonus neu. Eine Panzerung hat nur einen Wert, ihre Hülle, und fasst deshalb einen Bonus, +2 % bis +15 % je nach Stufe: Eine Hull Plating III auf Ewig fügt bis zu 17.250 hinzu. Die [Auktion](/wiki/03-Mechanics/Auction.md) listet Hull Plating II und III, nie Hull Plating I, die der Shop verkauft.

## Panzerungs-Slots {#hull-plate-slots}

Hüllenpanzerung passt nur in **Panzerungs-Slots**, eine eigene Art von Slot, die die vier Schiffe, die du in der Montage baust, zusätzlich zu ihren Laser-, Generator-, Extra-, Fähigkeits- und Drohnen-Slots haben:

| Schiff | Panzerungs-Slots | Ein voller Satz Hull Plating III fügt hinzu |
| :--- | ---: | ---: |
| **Paragon** | 5 | 75.000 |
| **Storm** | 7 | 105.000 |
| **Ironclad** | 15 | 225.000 |
| **Wraith** | 9 | 135.000 |

- **Anfangs alle gesperrt.** Ein Slot öffnet sich, wenn du ihn im Skylab erforschst: eine Technologie für jeden Slot, 1 Stunde und 10 Dark Matter, der Reihe nach vom ersten an. Die Ansicht [Forschung](/wiki/03-Mechanics/Research.md#ship-technologies) zeigt die Slots eines Schiffs als eine Karte mit einem Punkt für jeden.
- **Eine Schiffsart, nicht ein Schiff.** Die Slots, die du für die Paragon geöffnet hast, sind auch an jedem Paragon-Design offen ([Schiffsdesigns](/wiki/03-Mechanics/Ship-Designs.md)). Eine Technologie gehört dir für immer: Der Wipe lässt sie dir.
- **Beide Konfigurationen teilen sie.** Die Panzerungen gehören zum Schiff: Ein Wechsel der Konfiguration lässt sie dran, und der Hangar zeigt in beiden dieselben.
- **Beliebig gemischt.** Ein Slot nimmt jede Hüllenpanzerung auf, auch zwei gleiche.
- **Dein Hüllenanteil bleibt.** Beim Einbauen oder Ablegen einer Panzerung bleibt der Anteil deiner Hülle gleich, sie heilt dich also nie und schadet dir nie.
- **Wie jede Ausrüstung** baust du Panzerungen im Hangar ein und ab, oder in seinem Fenster aus einer Schutzzone, nie im freien Raum. Ein Slot, den du nicht erforscht hast, lehnt eine Panzerung ab.

Im Hangar zeigt die Karte **Hüllenpanzerung** die Slots. In einen offenen ziehst du eine Panzerung per Drag and Drop, wie in jeden Slot; ein gesperrter zeigt ein Schloss, und ein Klick öffnet die Forschung des Skylabs. Eine Kachel neben den anderen Werten addiert, was die eingebauten Panzerungen geben.

## Wie sich die Hülle summiert {#how-the-hull-adds-up}

Eine Panzerung fügt ihre Hülle der eigenen des Schiffs hinzu, und der Hangar und das Schiffsfenster zeigen die größere Zahl. Die Hülle des Schiffs plus seine Panzerungen geht dann durch dieselben Multiplikatoren wie immer: einen [Hull Plating Booster](/wiki/06-Items/Boosters.md) und die [Drohnenformation](/wiki/03-Mechanics/Formations.md), die du trägst. Ein Design, das die Hülle ändert (BUCKY hat 25 % mehr), ändert die eigene Hülle des Schiffs, und die Panzerungen kommen obendrauf.

## Hull Plating oder Hull Plating Booster? {#hull-plating-or-booster}

Zwei Dinge teilen sich den Namen. **Hüllenpanzerung** (diese Seite) ist eine Panzerung: eine Platte, die in einem Panzerungs-Slot eines gebauten Schiffs sitzt und ihre Hülle hinzufügt, solange sie eingebaut ist. Der **Hull Plating Booster** ist ein Bonus auf Zeit der Seite [Booster](/wiki/06-Items/Boosters.md), +10 % maximale Trefferpunkte für 10 Stunden auf jedem Schiff, das du fliegst, und hat nichts zum Einbauen. Sie addieren sich: Die Panzerungen kommen zuerst, und die 10 % des Boosters werden von der Summe genommen.
