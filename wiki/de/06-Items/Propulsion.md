<!-- wiki-i18n source: b04277deb1c5225f -->
<!-- wiki-i18n title: Antrieb -->
# Antrieb & Tempo {#propulsion-speed}

Antriebssysteme bestimmen die Fluggeschwindigkeit und Wendigkeit deines Schiffs.

## Triebwerke {#engines}

Triebwerke sind die wichtigste Schubquelle deines Schiffs. Ein Triebwerk in einem **Fähigkeits-Slot** gibt dir stattdessen den **Afterburner** aus der Spalte Spezialeffekt, einen Temposchub für zehn Sekunden (länger mit mehr Triebwerken), und bringt selbst keinen Schub (siehe [Fähigkeiten](/wiki/03-Mechanics/Abilities.md)).

| Name | Seltenheit | Grundtempo | Tempobonus % | Schildbonus % | Slots | Spezialeffekt | Kosten |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Minderwertig | +2 | +2 % | -2 % | 1 | Afterburner I | 20.000 Credits |
| **Engine II** | Gewöhnlich | +4 | +4 % | -8 % | 2 | Afterburner II | 2.000 Thulium |
| **Engine III** | Selten | +6 | +5 % | -15 % | 3 | Afterburner III | Nur herstellbar |

Das **Engine III** wird in der [Montage](/wiki/06-Items/Overview.md#upgrading-modules) aus einem Engine II hergestellt, mit 2.000 Thulium, 60 Ship Fragments, 3 Power Cores und 6 Velkonite Reinforced Plates aus deinem Skylab. Es behält die Verzauberungsstufe des Triebwerks, das es verbraucht, und seine Boni werden neu ausgewürfelt ([Modul-Upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Nimm das Engine II zuerst von deinem Schiff (und seine Schubdüsen aus ihm): Ein Triebwerk, das ausgerüstet ist oder Schubdüsen enthält, wird nicht verbraucht.

Der Schildbonus der Triebwerke steht in den Gegenstandsdaten, doch das Spiel hat ihn nie angewendet: Triebwerke schwächen deine Schilde nicht, und die Gegenstandskarten lassen ihn weg.

---

## Schubdüsen {#thrusters}

Schubdüsen werden in Triebwerke oder adaptive Kerne eingesetzt, um deren Tempoleistung zu steigern. Es gibt zwei Familien mit je vier Stufen: Die **Impulse Thrusters** bringen am meisten festes Tempo und multiplizieren das Tempo des Triebwerks, in dem sie stecken, ein wenig, die **Momentum Thrusters** bringen weniger festes Tempo, multiplizieren es dafür stärker. Ein Triebwerk (oder adaptiver Kern) mit Schubdüsen erzeugt **sein eigenes Grundtempo plus die festen Tempo-Boosts der Schubdüsen, das Ganze mal den miteinander multiplizierten Tempofaktoren der Schubdüsen** ([so wird das Tempo berechnet](/wiki/03-Mechanics/Speed.md)): Ein Engine III mit drei Momentum Thruster IV erzeugt (6 + 3 x 12) x 1,14 x 1,14 x 1,14 = 62,2, mit drei Impulse Thruster IV (6 + 3 x 17) x 1,02 x 1,02 x 1,02 = 60,5, ein Adaptive Core II mit zwei Impulse Thruster IV (0 + 2 x 17) x 1,02 x 1,02 = 35,4 (31,2 mit zwei Momentum Thruster IV).

| Name | Seltenheit | Fester Tempo-Boost | Tempofaktor | Kosten |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Minderwertig | +5 | 1,02x | 20.000 Credits |
| **Impulse Thruster II** | Gewöhnlich | +10 | 1,02x | Nur herstellbar |
| **Impulse Thruster III** | Selten | +15 | 1,03x | Nur herstellbar |
| **Impulse Thruster IV** | Episch | +17 | 1,02x | Nur herstellbar |
| **Momentum Thruster I** | Minderwertig | +4 | 1,08x | 20.000 Credits |
| **Momentum Thruster II** | Gewöhnlich | +8 | 1,10x | Nur herstellbar |
| **Momentum Thruster III** | Selten | +11 | 1,13x | Nur herstellbar |
| **Momentum Thruster IV** | Episch | +12 | 1,14x | Nur herstellbar |

Welche Familie schneller ist, hängt vom Einsatzort ab. Die Impulse Thrusters erzeugen mehr in einem adaptiven Kern und in einem Triebwerk mit einer oder zwei Schubdüsen; die Momentum Thrusters derselben Stufe erzeugen mehr in einem Engine III, dessen drei Slots alle belegt sind (62,2 gegen 60,5 auf Stufe IV, und ein Impulse Thruster IV mit zwei Momentum Thruster IV, 62,3, ist das Beste, was ein Engine III sein kann).

Ein Bonus auf den Tempofaktor einer Schubdüse aus der [Schmiede](/wiki/06-Items/Forge.md) verstärkt den Teil über 1 (ein Bonus von +15 % auf 1,14x ergibt 1,161x), und auf einen Faktor von 1,05x oder weniger würfelt die Schmiede keinen Bonus: Auf dem 1,02x oder 1,03x eines Impulse Thruster wäre er ein Tausendstel wert. Ein Impulse Thruster fasst einen Bonus (sein festes Tempo), ein Momentum Thruster zwei.

Stufe I jeder Familie wird für 20.000 Credits verkauft. Die Stufen II bis IV werden in der [Montage](/wiki/06-Items/Overview.md#upgrading-modules) hergestellt, jede aus der Schubdüse derselben Familie eine Stufe darunter (ein Impulse Thruster II aus einem Impulse Thruster I, ein III aus einem II, ein IV aus einem III), mit Thulium, Beute und Velkonite Reinforced Plates aus deinem Skylab (2, 4 und 6 Platten). Eine Schubdüse wechselt nie die Familie: Impulse oder Momentum wählst du beim Kauf der Stufe I. Jede behält die Verzauberungsstufe der Schubdüse, die er verbraucht, und seine Boni werden neu ausgewürfelt ([Modul-Upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Schubdüsen passen nicht in einen [Fähigkeits-Slot](/wiki/03-Mechanics/Abilities.md); sie gehören in Triebwerke und adaptive Kerne.

### Aliens abhängen {#outrunning-aliens}

Die Aliens fliegen mit 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) und 230 (Crystalys). Eine Ostirion mit einem Engine II und zwei Schubdüsen fliegt mit 223,1 mit Impulse Thruster I: noch unter dem Crystalys, es braucht also eine in der Montage hergestellte Schubdüse, um ihn abzuhängen (234,0 mit Impulse Thruster II, 245,5 mit III, 249,1 mit IV). Die Momentum Thrusters fliegen auf diesem Schiff etwas niedriger (222,6 mit einem Momentum Thruster I, 233,2, 242,5 und 245,8 mit II bis IV): Stufe I beider Familien liegt unter einem Crystalys, jede in der Montage hergestellte Stufe darüber.
