<!-- wiki-i18n source: fe17f46644fd6072 -->
<!-- wiki-i18n title: Antrieb -->
# Antrieb & Tempo {#propulsion-speed}

Antriebssysteme bestimmen die Fluggeschwindigkeit und Wendigkeit deines Schiffs.

## In einer Minute {#in-one-minute}

- **Triebwerke erzeugen Tempo, Schubdüsen stecken darin und erhöhen es.** Ein Triebwerk fasst eine bis drei Schubdüsen (ein Engine I eine, ein Engine II zwei, ein Engine III drei), ein adaptiver Kern ebenso (seine Stufe sagt, wie viele).
- **Zwei Familien mit je vier Stufen.** Impulse Thrusters bringen das meiste feste Tempo. Momentum Thrusters bringen weniger festes Tempo und multiplizieren das Tempo stärker. In beiden Familien ist jede Stufe besser als die darunter, in beiden Werten.
- **Welche wohin.** Als Faustregel gehören Momentum Thrusters in ein volles Engine III (drei Schubdüsen) und Impulse Thrusters in einen adaptiven Kern; in den kleineren Triebwerken liegen beide auf den Stufen I und II nah beieinander, und ab Stufe III liegt Impulse vorn. [Die Tabelle unten](#which-thruster-where) hat die Zahlen. Das schnellste Engine III fasst drei Momentum Thruster IV und ergibt 63,3.
- **Woher sie kommen.** Stufe I jeder Familie kostet 20.000 Credits. Die Stufen II bis IV werden in der Montage hergestellt, jede aus der Stufe darunter, und eine Schubdüse wechselt nie die Familie.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Gegenstandsbaum {#item-tree}

Was die Montage herstellt, braucht zuerst seine Technologie; zeige auf einen Gegenstand, um zu sehen, wie lange die Forschung dauert. Der Technologiebaum, der Treibstoff und der Boost: [Forschung](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Engine I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 4000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 80 Ship Fragment, 4 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 80 Ship Fragment, 4 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 4000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 4000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I => Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Triebwerke {#engines}

Triebwerke sind die wichtigste Schubquelle deines Schiffs. Ein Triebwerk in einem **Fähigkeits-Slot** gibt dir stattdessen den **Afterburner** aus der Spalte Spezialeffekt, einen Temposchub für fünfzehn Sekunden (länger mit mehr Triebwerken), und bringt selbst keinen Schub (siehe [Fähigkeiten](/wiki/03-Mechanics/Abilities.md)).

| Name | Seltenheit | Grundtempo | Tempobonus % | Schildbonus % | Slots | Spezialeffekt | Kosten |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Minderwertig | +5 | +2 % | -2 % | 1 | Afterburner I | 20.000 Credits |
| **Engine II** | Gewöhnlich | +10 | +3 % | -8 % | 2 | Afterburner II | Nur herstellbar |
| **Engine III** | Selten | +15 | +4 % | -15 % | 3 | Afterburner III | Nur herstellbar |

Das **Engine II** wird in der [Montage](/wiki/06-Items/Overview.md#upgrading-modules) aus einem Engine I hergestellt, mit 2.000 Thulium, 60 Ship Fragments, 1 Power Core und 4 Velkonite Reinforced Plates. Das **Engine III** wird dort aus einem Engine II hergestellt, mit 4.000 Thulium, 110 Ship Fragments, 5 Power Cores, 1 Ancient Control Unit und 4 Dark Matter Plates ([Dark Matter und Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)). Jedes behält die Verzauberungsstufe und die Boni des Triebwerks, das es verbraucht ([Modul-Upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Nimm das Triebwerk, das verbraucht wird, zuerst von deinem Schiff (und seine Schubdüsen aus ihm): Ein Triebwerk, das ausgerüstet ist oder Schubdüsen enthält, wird nicht verbraucht.

Der Schildbonus der Triebwerke steht in den Gegenstandsdaten, doch das Spiel hat ihn nie angewendet: Triebwerke schwächen deine Schilde nicht, und die Gegenstandskarten lassen ihn weg.

---

## Schubdüsen {#thrusters}

Schubdüsen werden in Triebwerke oder adaptive Kerne eingesetzt, um deren Tempoleistung zu steigern. Es gibt zwei Familien mit je vier Stufen: Die **Impulse Thrusters** bringen am meisten festes Tempo und multiplizieren das Tempo des Triebwerks, in dem sie stecken, ein wenig, die **Momentum Thrusters** bringen weniger festes Tempo, multiplizieren es dafür stärker. In beiden Familien ist jede Stufe besser als die darunter, beim festen Tempo wie beim Faktor. Ein Triebwerk (oder adaptiver Kern) mit Schubdüsen erzeugt **sein eigenes Grundtempo plus die festen Tempo-Boosts der Schubdüsen, das Ganze mal den miteinander multiplizierten Tempofaktoren der Schubdüsen** ([so wird das Tempo berechnet](/wiki/03-Mechanics/Speed.md)): Ein Engine III mit drei Momentum Thruster IV erzeugt (15 + 3 x 11,135) x 1,0935 x 1,0935 x 1,0935 = 63,3, mit drei Impulse Thruster IV (15 + 3 x 14,025) x 1,02975 x 1,02975 x 1,02975 = 62,3, ein Adaptive Core II mit zwei Impulse Thruster IV (0 + 2 x 14,025) x 1,02975 x 1,02975 = 29,7 (26,6 mit zwei Momentum Thruster IV).

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

Impulse bringt mehr festes Tempo, Momentum multipliziert stärker; welche Familie schneller ist, hängt also davon ab, was das Triebwerk ohnehin schon erzeugt. Festes Tempo zählt am meisten dort, wo wenig Tempo zu multiplizieren ist: in einem adaptiven Kern (er hat kein eigenes Tempo) und in einem Triebwerk mit einer oder zwei Schubdüsen. Ein Faktor zählt am meisten in einem vollen Engine III, wo viel Tempo zu multiplizieren ist, und dort siegen die Momentum Thrusters auf jeder Stufe. Das Tempo, das jedes mit Schubdüsen der Stufe IV in allen Slots erzeugt:

| Wo die Schubdüsen stecken | Mit Impulse Thruster IV | Mit Momentum Thruster IV | Schneller |
| :--- | :---: | :---: | :--- |
| Engine I, 1 Schubdüse | 19,6 | 17,6 | Impulse |
| Engine II, 2 Schubdüsen | 40,3 | 38,6 | Impulse |
| Engine III, 1 Schubdüse | 29,9 | 28,6 | Impulse |
| Engine III, 2 Schubdüsen | 45,6 | 44,6 | Impulse |
| Engine III, 3 Schubdüsen | 62,3 | 63,3 | Momentum |
| Adaptive Core II, 2 Schubdüsen | 29,7 | 26,6 | Impulse |

- **Niedrigere Stufen.** Ab Stufe III liegt Impulse überall vorn, außer im vollen Engine III, um 0,6 bis 3,1. Auf den Stufen I und II liegen die beiden Familien außerhalb des vollen Engine III weniger als einen Punkt auseinander: Impulse liegt in einem Engine I und in einem Adaptive Core I oder II vorn, Momentum liegt in einem Engine III mit einer oder zwei Schubdüsen und in einem Engine II mit zwei vorn oder gleichauf. Die Ausnahme ist das volle Engine III: Dort liegt Momentum auf jeder Stufe vorn, um 1,0 bis 2,0.
- **Das schnellste Engine III.** Es fasst drei Momentum Thruster IV: 63,3, etwas mehr als mit einem Impulse und zwei Momentum Thruster IV (63,2) oder drei Impulse (62,3).

Ein Bonus auf den Tempofaktor einer Schubdüse aus der [Schmiede](/wiki/06-Items/Forge.md) verstärkt den Teil über 1 (ein Bonus von +15 % auf 1,0935x ergibt 1,1075x), und auf einen Faktor von 1,05x oder weniger würfelt die Schmiede keinen Bonus: Auf dem 1,017x bis 1,02975x eines Impulse Thruster brächte er weniger als 0,005 (+15 % auf 1,02975x ergibt 1,034x). Ein Impulse Thruster fasst einen Bonus (sein festes Tempo), ein Momentum Thruster zwei.

Stufe I jeder Familie wird für 20.000 Credits verkauft. Die Stufen II bis IV werden in der [Montage](/wiki/06-Items/Overview.md#upgrading-modules) hergestellt, jede aus der Schubdüse derselben Familie eine Stufe darunter (ein Impulse Thruster II aus einem Impulse Thruster I, ein III aus einem II, ein IV aus einem III), mit Thulium, Beute und Platten: 4 Velkonite Reinforced Plates aus deinem Skylab für Stufe II oder III und 4 Dark Matter Plates und eine Ancient Control Unit für Stufe IV. Eine Schubdüse wechselt nie die Familie: Impulse oder Momentum wählst du beim Kauf der Stufe I. Jede behält die Verzauberungsstufe und die Boni der Schubdüse, die sie verbraucht ([Modul-Upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Schubdüsen passen nicht in einen [Fähigkeits-Slot](/wiki/03-Mechanics/Abilities.md); sie gehören in Triebwerke und adaptive Kerne.

### Aliens abhängen {#outrunning-aliens}

Die Aliens fliegen mit 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) und 230 (Crystalys). Eine Ostirion (Grundtempo 220) mit einem Engine II und zwei Schubdüsen erreicht 246,3 mit Impulse Thruster I, 255,6 mit II, 265,1 mit III und 268,2 mit IV: Jede Stufe hängt den Crystalys ab, sogar der Impulse Thruster I, den du kaufen kannst. Die Momentum Thrusters liegen auf diesem Schiff innerhalb von zwei Punkten davon (246,7 mit einem Momentum Thruster I, dann 255,9, 263,9 und 266,3 mit II bis IV): Jede Stufe beider Familien liegt über einem Crystalys, um mindestens 16,3.
