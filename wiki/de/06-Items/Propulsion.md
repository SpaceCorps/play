<!-- wiki-i18n source: 969bfa836749a15e -->
<!-- wiki-i18n title: Antrieb -->
# Antrieb & Tempo {#propulsion-speed}

Antriebssysteme bestimmen die Fluggeschwindigkeit und Wendigkeit deines Schiffs.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Gegenstandsbaum {#item-tree}

Was die Montage herstellt, braucht zuerst seine Technologie; zeige auf einen Gegenstand, um zu sehen, wie lange die Forschung dauert. Der Technologiebaum, der Treibstoff und der Boost: [Forschung](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | buy 2000 Thulium | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I -> Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

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

Schubdüsen werden in Triebwerke oder adaptive Kerne eingesetzt, um deren Tempoleistung zu steigern. Es gibt zwei Familien mit je vier Stufen: Die **Impulse Thrusters** bringen am meisten festes Tempo und multiplizieren das Tempo des Triebwerks, in dem sie stecken, ein wenig, die **Momentum Thrusters** bringen weniger festes Tempo, multiplizieren es dafür stärker. Ein Triebwerk (oder adaptiver Kern) mit Schubdüsen erzeugt **sein eigenes Grundtempo plus die festen Tempo-Boosts der Schubdüsen, das Ganze mal den miteinander multiplizierten Tempofaktoren der Schubdüsen** ([so wird das Tempo berechnet](/wiki/03-Mechanics/Speed.md)): Ein Engine III mit drei Momentum Thruster IV erzeugt (6 + 3 x 12) x 1,11 x 1,11 x 1,11 = 57,4, mit drei Impulse Thruster IV (6 + 3 x 17) x 1,02 x 1,02 x 1,02 = 60,5, ein Adaptive Core II mit zwei Impulse Thruster IV (0 + 2 x 17) x 1,02 x 1,02 = 35,4 (29,6 mit zwei Momentum Thruster IV).

| Name | Seltenheit | Fester Tempo-Boost | Tempofaktor | Kosten |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Minderwertig | +5 | 1,02x | 20.000 Credits |
| **Impulse Thruster II** | Gewöhnlich | +10 | 1,02x | Nur herstellbar |
| **Impulse Thruster III** | Selten | +15 | 1,03x | Nur herstellbar |
| **Impulse Thruster IV** | Episch | +17 | 1,02x | Nur herstellbar |
| **Momentum Thruster I** | Minderwertig | +4 | 1,06x | 20.000 Credits |
| **Momentum Thruster II** | Gewöhnlich | +8 | 1,07x | Nur herstellbar |
| **Momentum Thruster III** | Selten | +11 | 1,09x | Nur herstellbar |
| **Momentum Thruster IV** | Episch | +12 | 1,11x | Nur herstellbar |

Auf jeder Stufe erzeugt ein Impulse Thruster mehr als der Momentum Thruster derselben Stufe, in einem adaptiven Kern ebenso wie in einem Triebwerk mit einer, zwei oder drei Schubdüsen (60,5 gegen 57,4 mit drei Schubdüsen der Stufe IV in einem Engine III, und drei Impulse Thruster IV sind das Beste, was ein Engine III sein kann). Was ein Momentum Thruster ihm voraus hat, ist ein zweiter Bonus (unten).

Ein Bonus auf den Tempofaktor einer Schubdüse aus der [Schmiede](/wiki/06-Items/Forge.md) verstärkt den Teil über 1 (ein Bonus von +15 % auf 1,11x ergibt 1,1265x), und auf einen Faktor von 1,05x oder weniger würfelt die Schmiede keinen Bonus: Auf dem 1,02x oder 1,03x eines Impulse Thruster wäre er ein Tausendstel wert. Ein Impulse Thruster fasst einen Bonus (sein festes Tempo), ein Momentum Thruster zwei.

Stufe I jeder Familie wird für 20.000 Credits verkauft. Die Stufen II bis IV werden in der [Montage](/wiki/06-Items/Overview.md#upgrading-modules) hergestellt, jede aus der Schubdüse derselben Familie eine Stufe darunter (ein Impulse Thruster II aus einem Impulse Thruster I, ein III aus einem II, ein IV aus einem III), mit Thulium, Beute und Velkonite Reinforced Plates aus deinem Skylab (2, 4 und 6 Platten). Eine Schubdüse wechselt nie die Familie: Impulse oder Momentum wählst du beim Kauf der Stufe I. Jede behält die Verzauberungsstufe der Schubdüse, die er verbraucht, und seine Boni werden neu ausgewürfelt ([Modul-Upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Schubdüsen passen nicht in einen [Fähigkeits-Slot](/wiki/03-Mechanics/Abilities.md); sie gehören in Triebwerke und adaptive Kerne.

### Aliens abhängen {#outrunning-aliens}

Die Aliens fliegen mit 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) und 230 (Crystalys). Eine Ostirion mit einem Engine II und zwei Schubdüsen fliegt mit 223,1 mit Impulse Thruster I: noch unter dem Crystalys, es braucht also eine in der Montage hergestellte Schubdüse, um ihn abzuhängen (234,0 mit Impulse Thruster II, 245,5 mit III, 249,1 mit IV). Die Momentum Thrusters fliegen auf diesem Schiff etwas niedriger (222,0 mit einem Momentum Thruster I, 231,8, 240,1 und 243,9 mit II bis IV): Stufe I beider Familien liegt unter einem Crystalys, jede in der Montage hergestellte Stufe darüber.
