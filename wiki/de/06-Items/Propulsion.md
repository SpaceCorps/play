<!-- wiki-i18n source: 1433a0058afe39fa -->
<!-- wiki-i18n title: Antrieb -->
# Antrieb & Tempo {#propulsion-speed}

Antriebssysteme bestimmen die Fluggeschwindigkeit und Wendigkeit deines Schiffs.

## In einer Minute {#in-one-minute}

- **Triebwerke erzeugen Tempo, Schubdüsen stecken darin und erhöhen es.** Ein Triebwerk fasst eine bis drei Schubdüsen (ein Engine I eine, ein Engine II zwei, ein Engine III drei), ein adaptiver Kern ebenso (seine Stufe sagt, wie viele).
- **Zwei Familien mit je vier Stufen.** Impulse Thrusters bringen das meiste feste Tempo. Momentum Thrusters bringen weniger festes Tempo und multiplizieren das Tempo stärker. In beiden Familien ist jede Stufe besser als die darunter, in beiden Werten.
- **Welche wohin.** Als Faustregel gehören Impulse Thrusters überallhin: Nur in einem vollen Engine III (drei Schubdüsen) liegen die Momentum Thrusters der Stufen I und II vorn. [Die Tabelle unten](#which-thruster-where) hat die Zahlen. Das schnellste Engine III fasst drei Impulse Thruster IV und ergibt 52,5.
- **Woher sie kommen.** Stufe I jeder Familie kostet 20.000 Credits. Die Stufen II bis IV werden in der Montage hergestellt, jede aus der Stufe darunter, und eine Schubdüse wechselt nie die Familie.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Gegenstandsbaum {#item-tree}

Was die Montage herstellt, braucht zuerst seine Technologie; zeige auf einen Gegenstand, um zu sehen, wie lange die Forschung dauert. Der Technologiebaum, der Treibstoff und der Boost: [Forschung](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Engine I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I => Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Triebwerke {#engines}

Triebwerke sind die wichtigste Schubquelle deines Schiffs. Ein Triebwerk in einem **Fähigkeits-Slot** gibt dir stattdessen den **Afterburner** aus der Spalte Spezialeffekt, einen Temposchub für zehn Sekunden (länger mit mehr Triebwerken), und bringt selbst keinen Schub (siehe [Fähigkeiten](/wiki/03-Mechanics/Abilities.md)).

| Name | Seltenheit | Grundtempo | Tempobonus % | Schildbonus % | Slots | Spezialeffekt | Kosten |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Minderwertig | +2 | +2 % | -2 % | 1 | Afterburner I | 20.000 Credits |
| **Engine II** | Gewöhnlich | +4 | +4 % | -8 % | 2 | Afterburner II | Nur herstellbar |
| **Engine III** | Selten | +6 | +5 % | -15 % | 3 | Afterburner III | Nur herstellbar |

Das **Engine II** wird in der [Montage](/wiki/06-Items/Overview.md#upgrading-modules) aus einem Engine I hergestellt, mit 1.000 Thulium, 10 Ship Fragments, 1 Power Core und 2 Velkonite Reinforced Plates. Das **Engine III** wird dort aus einem Engine II hergestellt, mit 2.000 Thulium, 60 Ship Fragments, 3 Power Cores und 3 Dark Matter Plates ([Dark Matter und Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)). Jedes behält die Verzauberungsstufe des Triebwerks, das es verbraucht, und seine Boni werden neu ausgewürfelt ([Modul-Upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Nimm das Triebwerk, das verbraucht wird, zuerst von deinem Schiff (und seine Schubdüsen aus ihm): Ein Triebwerk, das ausgerüstet ist oder Schubdüsen enthält, wird nicht verbraucht.

Der Schildbonus der Triebwerke steht in den Gegenstandsdaten, doch das Spiel hat ihn nie angewendet: Triebwerke schwächen deine Schilde nicht, und die Gegenstandskarten lassen ihn weg.

---

## Schubdüsen {#thrusters}

Schubdüsen werden in Triebwerke oder adaptive Kerne eingesetzt, um deren Tempoleistung zu steigern. Es gibt zwei Familien mit je vier Stufen: Die **Impulse Thrusters** bringen am meisten festes Tempo und multiplizieren das Tempo des Triebwerks, in dem sie stecken, ein wenig, die **Momentum Thrusters** bringen weniger festes Tempo, multiplizieren es dafür stärker. In beiden Familien ist jede Stufe besser als die darunter, beim festen Tempo wie beim Faktor. Ein Triebwerk (oder adaptiver Kern) mit Schubdüsen erzeugt **sein eigenes Grundtempo plus die festen Tempo-Boosts der Schubdüsen, das Ganze mal den miteinander multiplizierten Tempofaktoren der Schubdüsen** ([so wird das Tempo berechnet](/wiki/03-Mechanics/Speed.md)): Ein Engine III mit drei Momentum Thruster IV erzeugt (6 + 3 x 11,135) x 1,0935 x 1,0935 x 1,0935 = 51,5, mit drei Impulse Thruster IV (6 + 3 x 14,025) x 1,02975 x 1,02975 x 1,02975 = 52,5, ein Adaptive Core II mit zwei Impulse Thruster IV (0 + 2 x 14,025) x 1,02975 x 1,02975 = 29,7 (26,6 mit zwei Momentum Thruster IV).

| Name | Seltenheit | Fester Tempo-Boost | Tempofaktor | Kosten |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Minderwertig | +4,25 | 1,017x | 20.000 Credits |
| **Impulse Thruster II** | Gewöhnlich | +8,5 | 1,02125x | Nur herstellbar |
| **Impulse Thruster III** | Selten | +12,75 | 1,0255x | Nur herstellbar |
| **Impulse Thruster IV** | Episch | +14,025 | 1,02975x | Nur herstellbar |
| **Momentum Thruster I** | Minderwertig | +3,825 | 1,051x | 20.000 Credits |
| **Momentum Thruster II** | Gewöhnlich | +7,65 | 1,0595x | Nur herstellbar |
| **Momentum Thruster III** | Selten | +10,625 | 1,0765x | Nur herstellbar |
| **Momentum Thruster IV** | Episch | +11,135 | 1,0935x | Nur herstellbar |

### Welche Schubdüse wohin {#which-thruster-where}

Impulse bringt mehr festes Tempo, Momentum multipliziert stärker; welche Familie schneller ist, hängt also davon ab, was das Triebwerk ohnehin schon erzeugt. Festes Tempo zählt am meisten dort, wo wenig Tempo zu multiplizieren ist: in einem adaptiven Kern (er hat kein eigenes Tempo) und in einem Triebwerk mit einer oder zwei Schubdüsen. Ein Faktor zählt am meisten in einem vollen Engine III, wo viel Tempo zu multiplizieren ist, doch dort siegen nur die Momentum Thrusters der Stufen I und II. Das Tempo, das jedes mit Schubdüsen der Stufe IV in allen Slots erzeugt:

| Wo die Schubdüsen stecken | Mit Impulse Thruster IV | Mit Momentum Thruster IV | Schneller |
| :--- | :---: | :---: | :--- |
| Engine I, 1 Schubdüse | 16,5 | 14,4 | Impulse |
| Engine II, 2 Schubdüsen | 34,0 | 31,4 | Impulse |
| Engine III, 1 Schubdüse | 20,6 | 18,7 | Impulse |
| Engine III, 2 Schubdüsen | 36,1 | 33,8 | Impulse |
| Engine III, 3 Schubdüsen | 52,5 | 51,5 | Impulse |
| Adaptive Core II, 2 Schubdüsen | 29,7 | 26,6 | Impulse |

- **Niedrigere Stufen.** Die niedrigeren Stufen verhalten sich genauso, mit zwei knappen Fällen und einer Ausnahme: Mit zwei Schubdüsen in einem Engine II sind die Familien auf den Stufen I und II gleichauf (Impulse liegt um 0,06 und 0,24 vorn), und mit zwei in einem Engine III auch (innerhalb von 0,1). Ab Stufe III liegt Impulse in beiden vorn, um 1,5 bis 2,6. Die Ausnahme ist das volle Engine III: Dort liegt Momentum auf den Stufen I und II vorn, um 0,6 und 0,9, und Impulse auf den Stufen III und IV, um 0,5 und 1,0.
- **Das schnellste Engine III.** Es fasst drei Impulse Thruster IV: 52,5, etwas mehr als mit einem Impulse und zwei Momentum Thruster IV (52,1) oder drei Momentum (51,5).

Ein Bonus auf den Tempofaktor einer Schubdüse aus der [Schmiede](/wiki/06-Items/Forge.md) verstärkt den Teil über 1 (ein Bonus von +15 % auf 1,0935x ergibt 1,1075x), und auf einen Faktor von 1,05x oder weniger würfelt die Schmiede keinen Bonus: Auf dem 1,017x bis 1,02975x eines Impulse Thruster brächte er weniger als 0,005 (+15 % auf 1,02975x ergibt 1,034x). Ein Impulse Thruster fasst einen Bonus (sein festes Tempo), ein Momentum Thruster zwei.

Stufe I jeder Familie wird für 20.000 Credits verkauft. Die Stufen II bis IV werden in der [Montage](/wiki/06-Items/Overview.md#upgrading-modules) hergestellt, jede aus der Schubdüse derselben Familie eine Stufe darunter (ein Impulse Thruster II aus einem Impulse Thruster I, ein III aus einem II, ein IV aus einem III), mit Thulium, Beute und Platten: 2 oder 4 Velkonite Reinforced Plates aus deinem Skylab für Stufe II oder III und 3 Dark Matter Plates für Stufe IV. Eine Schubdüse wechselt nie die Familie: Impulse oder Momentum wählst du beim Kauf der Stufe I. Jede behält die Verzauberungsstufe der Schubdüse, die er verbraucht, und seine Boni werden neu ausgewürfelt ([Modul-Upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Schubdüsen passen nicht in einen [Fähigkeits-Slot](/wiki/03-Mechanics/Abilities.md); sie gehören in Triebwerke und adaptive Kerne.

### Aliens abhängen {#outrunning-aliens}

Die Aliens fliegen mit 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) und 230 (Crystalys). Eine Ostirion mit einem Engine II und zwei Schubdüsen fliegt mit 221,4 mit Impulse Thruster I: noch unter dem Crystalys, es braucht also eine in der Montage hergestellte Schubdüse, um ihn abzuhängen (230,8 mit Impulse Thruster II, 240,3 mit III, 243,3 mit IV). Die Momentum Thrusters fliegen auf diesem Schiff gleich schnell oder etwas niedriger (221,4 mit einem Momentum Thruster I, dann 230,5, 238,4 und 240,7 mit II bis IV): Stufe I beider Familien liegt unter einem Crystalys, jede in der Montage hergestellte Stufe darüber, Stufe II nur um 0,8 und 0,5.
