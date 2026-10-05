<!-- wiki-i18n source: 06696a3c765a00c4 -->
<!-- wiki-i18n title: Schilde -->
# Schilde & Verteidigung {#shields-defense}

Defensive Module liefern Schildkapazität, absorbieren Schaden und laden deine Verteidigung wieder auf.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Gegenstandsbaum {#item-tree}

Was die Montage herstellt, braucht zuerst seine Technologie; zeige auf einen Gegenstand, um zu sehen, wie lange die Forschung dauert. Der Technologiebaum, der Treibstoff und der Boost: [Forschung](/wiki/03-Mechanics/Research.md).

```tree
Light Shield Core | shield, shoddy | buy 20000 Credits | /wiki/06-Items/Shields.md#shield-cores
Basic Shield Core | shield, common | buy 2000 Thulium | /wiki/06-Items/Shields.md#shield-cores
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cores
Adaptive Core I | hybrid-generator, shoddy | buy 100000 Credits | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core II | hybrid-generator, common | buy 4000 Thulium | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core III | hybrid-generator, rare | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Absorption Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells

Light Shield Core -> Basic Shield Core => Heavy Shield Core
Adaptive Core I -> Adaptive Core II -> Adaptive Core III
Absorption Shield Cell I => Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell I => Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```
<!-- item-tree:end -->

## Schilde {#shield-cores}

Rüste Schilde aus, um aktive Schutzbarrieren zu erzeugen, in den Generator-Slots deines Schiffs oder an deinen [Drohnen](/wiki/03-Mechanics/Drones.md) (der Slot einer Drohne zählt als Kern-Slot). Beachte, dass schwere Schilde dein Tempo drücken. Ein Schild in einem **Fähigkeits-Slot** gibt dir stattdessen den **Shield Surge** aus der Spalte Spezialeffekt, eine Schildreparatur über zehn Sekunden, und bringt selbst keinen Schild (siehe [Fähigkeiten](/wiki/03-Mechanics/Abilities.md)).

| Name | Seltenheit | Kapazität | Aufladerate | Absorption | Schild % | Tempo % | Zellen-Slots | Spezialeffekt | Kosten |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Light Shield Core** | Minderwertig | 10.000 | 333/s | 45 % | +5 % | -1 % | 1 | Shield Surge I | 20.000 Credits |
| **Basic Shield Core** | Gewöhnlich | 15.000 | 500/s | 48 % | +10 % | -3 % | 2 | Shield Surge II | 2.000 Thulium |
| **Heavy Shield Core** | Selten | 25.000 | 833/s | 50 % | +20 % | -5 % | 3 | Shield Surge III | Nur herstellbar |

Der **Heavy Shield Core** wird in der [Montage](/wiki/06-Items/Overview.md#upgrading-modules) aus einem Basic Shield Core hergestellt, mit 2.000 Thulium, 20 Cataclysite, 8 Reinforced Hull Plates und 6 Velkonite Reinforced Plates aus deinem Skylab. Er behält die Verzauberungsstufe des Kerns, den er verbraucht, und seine Boni werden neu ausgewürfelt ([Modul-Upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Nimm den Basic Shield Core zuerst von deinem Schiff (und seine Zellen aus ihm): Ein Kern, der ausgerüstet ist oder Zellen enthält, wird nicht verbraucht.

Die **Absorption** ist der Anteil jedes Treffers, den deine Schilde nehmen; den Rest nimmt die Hülle. Ein Schild allein hat **45 bis 50 %**, und seine Zellen steuern den Rest bei: Der beste Schild mit den besten Zellen (ein Heavy Shield Core mit drei Absorption Shield Cell IV) hat **80 %**, das meiste, was ein Schiff ab Werk hat. Zwei dauerhafte Boosts kommen dazu: der Schildabsorptions-Boost des Saison-Shops (+0,1 Punkte pro Level, 100 Level, je 25 Wipe-Punkte) und die Absorptionsboni der Schmiede. Die heutigen Quellen für Wipe-Punkte (insgesamt 855 an ihren Obergrenzen, über Wipes hinweg behalten; weitere Quellen sind geplant) kaufen 34 dieser 100 Level (+3,4 Punkte), womit ein voll geschmiedetes ewiges Set etwa **95 %** erreicht. Der Wert ist jedoch nicht auf 100 % begrenzt: Die *Schilddurchdringung* eines Angreifers wird davon abgezogen, was ein Schiff über 100 % hat, ist also sein Spielraum gegen Durchdringung. Siehe [Schildmechanik](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-).

---

## Hybridgeneratoren (adaptive Kerne) {#hybrid-generators-adaptive-cores-}

Adaptive Kerne arbeiten als Hybridgeneratoren und verbinden Schild- und Tempofähigkeiten. Sie nehmen in ihren Slots sowohl Schubdüsen als auch Schildzellen auf (ein Modul pro Slot, von beiden Arten). Ihr Schild- und Tempobonus zählt wie der eines Schilds oder eines Triebwerks (die vier besten, mal dem Anteil des Slots). Sie haben keine Absorption: Sie ändern die Absorption deines Schiffs nicht, und Zellen in ihnen steuern nur Kapazität und Aufladung bei. Nur Schilde nehmen einen Anteil eines Treffers, Zellen in einem adaptiven Kern brauchen daher auch einen Schild auf dem Schiff.

| Name | Seltenheit | Schildbonus % | Tempobonus % | Slots | Spezialeffekt | Kosten |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **Adaptive Core I** | Minderwertig | +5 % | +3 % | 1 | — | 100.000 Credits |
| **Adaptive Core II** | Gewöhnlich | +8 % | +4 % | 2 | — | 4.000 Thulium |
| **Adaptive Core III** | Selten | +15 % | +5 % | 3 | — | Nur herstellbar |

---

## Schildzellen {#shield-cells}

Schildzellen werden in Schilde oder adaptive Kerne eingesetzt (so viele, wie der Kern Slots hat), um diesen Kern zu verstärken. In einem Schild erhöhen sie auch seine Absorption, in Punkten, und damit den Anteil jedes Treffers, den deine Schilde nehmen. Es gibt zwei Familien mit je vier Stufen: Die **Capacity Shield Cells** bringen am meisten Schild und Aufladung, die **Absorption Shield Cells** am meisten Absorption (auf jeder Stufe doppelt so viel Absorption und halb so viel Schild und Aufladung wie die Capacity-Zelle derselben Stufe). Capacity hilft einem Schiff, bei dem der Schild den Kampf entscheidet, Absorption einem Schiff, bei dem die Hülle ihn entscheidet. Ein Kern, dessen Slots alle mit einer Zellenart gefüllt sind: Ein Light Shield Core (1 Slot) hat 47 bis 55 %, ein Basic Shield Core (2 Slots) 52 bis 68 % und ein Heavy Shield Core (3 Slots) 56 bis 80 %, von den Capacity-Zellen der Stufe I bis zu den Absorption-Zellen der Stufe IV. Legst du den Kern ab oder verbrauchst ihn als Spender eines Zusammenführens in der [Schmiede](/wiki/06-Items/Forge.md), kommen seine Zellen zurück ins Inventar.

| Name | Seltenheit | Kapazitäts-Boost | Auflade-Boost | Absorptions-Boost | Kosten |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Capacity Shield Cell I** | Minderwertig | +3.000 | +250/s | +2 % | 30.000 Credits |
| **Capacity Shield Cell II** | Gewöhnlich | +6.000 | +500/s | +3 % | Nur herstellbar |
| **Capacity Shield Cell III** | Selten | +9.000 | +750/s | +4 % | Nur herstellbar |
| **Capacity Shield Cell IV** | Episch | +12.000 | +1.000/s | +5 % | Nur herstellbar |
| **Absorption Shield Cell I** | Minderwertig | +1.500 | +125/s | +4 % | 30.000 Credits |
| **Absorption Shield Cell II** | Gewöhnlich | +3.000 | +250/s | +6 % | Nur herstellbar |
| **Absorption Shield Cell III** | Selten | +4.500 | +375/s | +8 % | Nur herstellbar |
| **Absorption Shield Cell IV** | Episch | +6.000 | +500/s | +10 % | Nur herstellbar |

Stufe I jeder Familie wird für 30.000 Credits verkauft. Die Stufen II bis IV werden in der [Montage](/wiki/06-Items/Overview.md#upgrading-modules) hergestellt, jede aus der Zelle derselben Familie eine Stufe darunter (eine Capacity Shield Cell II aus einer Capacity Shield Cell I, eine III aus einer II, eine IV aus einer III), mit Thulium, Beute und Velkonite Reinforced Plates aus deinem Skylab (2, 4 und 6 Platten). Eine Zelle wechselt nie die Familie: Capacity oder Absorption wählst du beim Kauf der Stufe I. Die neue Zelle behält die Verzauberungsstufe der Zelle, die sie verbraucht, und ihre Boni werden neu ausgewürfelt ([Modul-Upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Zellen passen nicht in einen [Fähigkeits-Slot](/wiki/03-Mechanics/Abilities.md); sie gehören in Schilde und adaptive Kerne.
