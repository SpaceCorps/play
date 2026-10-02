<!-- wiki-i18n source: 301d58f06f810979 -->
<!-- wiki-i18n title: Schilde -->
# Schilde & Verteidigung {#shields-defense}

Defensive Module liefern Schildkapazität, absorbieren Schaden und laden deine Verteidigung wieder auf.

## Schilde {#shield-cores}

Rüste Schilde aus, um aktive Schutzbarrieren zu erzeugen, in den Generator-Slots deines Schiffs oder an deinen [Drohnen](/wiki/03-Mechanics/Drones.md) (der Slot einer Drohne zählt als Kern-Slot). Beachte, dass schwere Schilde dein Tempo drücken. Ein Schild in einem **Fähigkeits-Slot** gibt dir stattdessen den **Shield Surge** aus der Spalte Spezialeffekt, eine Schildreparatur über zehn Sekunden, und bringt selbst keinen Schild (siehe [Fähigkeiten](/wiki/03-Mechanics/Abilities.md)).

| Name | Seltenheit | Kapazität | Aufladerate | Absorption | Schild % | Tempo % | Zellen-Slots | Spezialeffekt | Kosten |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Light Shield Core** | Minderwertig | 10.000 | 333/s | 45 % | +5 % | -1 % | 1 | Shield Surge I | 20.000 Credits |
| **Basic Shield Core** | Gewöhnlich | 15.000 | 500/s | 48 % | +10 % | -3 % | 2 | Shield Surge II | 2.000 Thulium |
| **Heavy Shield Core** | Selten | 25.000 | 833/s | 50 % | +20 % | -5 % | 3 | Shield Surge III | Nur herstellbar |

Der **Heavy Shield Core** wird in der [Montage](/wiki/05-Items/Overview.md#upgrading-modules) aus einem Basic Shield Core hergestellt, mit 2.000 Thulium, 20 Cataclysite, 8 Reinforced Hull Plates und 6 Velkonite Reinforced Plates aus deinem Skylab. Er behält die Verzauberungsstufe des Kerns, den er verbraucht, und seine Boni werden neu ausgewürfelt ([Modul-Upgrades](/wiki/05-Items/Forge.md#module-upgrades-in-the-assembly)). Nimm den Basic Shield Core zuerst von deinem Schiff (und seine Zellen aus ihm): Ein Kern, der ausgerüstet ist oder Zellen enthält, wird nicht verbraucht.

Die **Absorption** ist der Anteil jedes Treffers, den deine Schilde nehmen; den Rest nimmt die Hülle. Ein Schild allein hat **45 bis 50 %**, und seine Zellen steuern den Rest bei: Der beste Schild mit den besten Zellen (ein Heavy Shield Core mit drei Sovereign Shield Cells) hat **80 %**, das meiste, was ein Schiff ab Werk hat. Zwei dauerhafte Boosts kommen dazu: der Schildabsorptions-Boost des Saison-Shops (+0,1 Punkte pro Level, 100 Level, je 25 Wipe-Punkte) und die Absorptionsboni der Schmiede. Die heutigen Quellen für Wipe-Punkte (insgesamt 855 an ihren Obergrenzen, über Wipes hinweg behalten; weitere Quellen sind geplant) kaufen 34 dieser 100 Level (+3,4 Punkte), womit ein voll geschmiedetes ewiges Set etwa **95 %** erreicht. Der Wert ist jedoch nicht auf 100 % begrenzt: Die *Schilddurchdringung* eines Angreifers wird davon abgezogen, was ein Schiff über 100 % hat, ist also sein Spielraum gegen Durchdringung. Siehe [Schildmechanik](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-).

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

Schildzellen werden in Schilde oder adaptive Kerne eingesetzt (so viele, wie der Kern Slots hat), um diesen Kern zu verstärken. In einem Schild erhöhen sie auch seine Absorption, in Punkten, und damit den Anteil jedes Treffers, den deine Schilde nehmen. Ein Kern, dessen Slots alle mit einer Zellenart gefüllt sind: Ein Light Shield Core (1 Slot) hat 47 bis 55 %, ein Basic Shield Core (2 Slots) 52 bis 68 % und ein Heavy Shield Core (3 Slots) 56 bis 80 %, von Basic Shield Cells bis zu Sovereign Shield Cells. Legst du den Kern ab oder verbrauchst ihn als Spender eines Zusammenführens in der [Schmiede](/wiki/05-Items/Forge.md), kommen seine Zellen zurück ins Inventar.

| Name | Seltenheit | Kapazitäts-Boost | Auflade-Boost | Absorptions-Boost | Kosten |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Basic Shield Cell** | Minderwertig | +1.000 | +100/s | +2 % | 10.000 Credits |
| **Advanced Shield Cell** | Gewöhnlich | +2.500 | +250/s | +4 % | 30.000 Credits |
| **Reinforced Shield Cell** | Ungewöhnlich | +4.200 | +350/s | +6 % | 90.000 Credits |
| **Elite Shield Cell** | Selten | +6.000 | +500/s | +7 % | 5.000 Thulium |
| **Prime Shield Cell** | Selten | +8.500 | +700/s | +8 % | 8.000 Thulium |
| **Sovereign Shield Cell** | Episch | +12.000 | +1.000/s | +10 % | Nur herstellbar |

Die Sovereign Shield Cell wird in der [Montage](/wiki/05-Items/Overview.md#upgrading-modules) aus einer Prime Shield Cell hergestellt, mit Thulium, Beute und 6 Velkonite Reinforced Plates aus deinem Skylab. Sie behält die Verzauberungsstufe der Zelle, die sie verbraucht, und ihre Boni werden neu ausgewürfelt ([Modul-Upgrades](/wiki/05-Items/Forge.md#module-upgrades-in-the-assembly)). Zellen passen nicht in einen [Fähigkeits-Slot](/wiki/03-Mechanics/Abilities.md); sie gehören in Schilde und adaptive Kerne.
