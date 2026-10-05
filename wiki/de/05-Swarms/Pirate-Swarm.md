<!-- wiki-i18n source: 17a693ffb6d8a4f2 -->
<!-- wiki-i18n title: Pirate-Schwarm -->
# Pirate-Schwarm {#pirate-swarm}

Der Pirate-Schwarm besteht aus einem **Pirate Boss** mit seinen **Pirate Scouts**: einem riesigen, langsamen Schiff, das niemanden angreift und mit Raketen antwortet, und einem Rudel schnellerer Schiffe, die es bewachen und heilen. Er lebt in den Sektoren zwischen der Basis eines Konzerns und seiner Grenze, wo die mittleren Stufen des Spiels gespielt werden, und ist ein langer Kampf für eine Gruppe von Piloten, kein schneller Abschuss.

## Auf einen Blick {#at-a-glance}

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Wo**: Die Sektoren `x-2` und `x-3` jedes Konzerns
- **Wie viele**: Einer in jedem dieser Sektoren, 6 in jeder Welt
- **Erscheint**: Ab Saisontag 4 bis zum Wipe
- **Anführer**: Pirate Boss
- **Begleiter**: Bis zu 5 × Pirate Scout, alle 10 s ein neuer
- **Begleiter bleiben nahe**: höchstens 900 Einheiten vom Anführer entfernt
- **Heilung**: Jeder Pirate Scout im Umkreis von 600 Einheiten um den Anführer heilt dessen Hülle, in Alpha 40 HP pro Sekunde
- **Anführer zerstört**: Die Begleiter verschwinden 1 min nach der Zerstörung des Anführers, sofern sie nicht gerade angreifen
- **Kehrt zurück**: 2 min nach der Zerstörung des Anführers, im selben Sektor
- **Meldungen**: Die Piloten des Sektors erfahren, wann der Anführer auftaucht und wann er zerstört wird. Das sind Systemzeilen: Sie erscheinen im Tab **System** des Chats, mit Zähler für Ungelesenes, und nicht in **Global** oder **Lokal**. Der Kill-Feed nennt den Piloten, dem der Abschuss gutgeschrieben wird.

<!-- pirate-glance:end -->

## Die Mitglieder {#the-members}

- **Pirate Boss**: ein Schiff auf Basis der Ironclad, mit einem Teil ihrer Stärke (die Werte stehen unten). Er ist passiv und feuert **keine Laser**: Seine einzige Waffe ist eine **gerade Rakete** ([Raketen](/wiki/06-Items/Rockets.md); welche, hängt vom Sektor ab, siehe die Tabelle) auf den Piloten, der ihn angegriffen hat, und er streift weiter umher, während er feuert. Seine Hülle repariert er nie von selbst.
- **Pirate Scout**: ein Schiff auf Basis der Kitefin, mit einem Teil ihrer Stärke. Scouts greifen jeden Piloten an, der ihnen nahe kommt, bleiben nah beim Boss, und jeder, der in der Nähe des Bosses ist, heilt dessen Hülle.

## Wie der Kampf verläuft {#how-the-fight-goes}

- **Schieß auf den Boss, nicht auf die Scouts.** Die Scouts heilen den Boss, aber die Heilung ist klein gegen seine Hülle, und ein neuer Scout kommt so oft, wie die Liste *Auf einen Blick* sagt: Eine Gruppe, die zuerst die Scouts abschießt, holt sie nie ein, und nur eine sehr große Gruppe kann sie beseitigen und braucht dann trotzdem länger für den Boss als eine, die sie in Ruhe gelassen hat. Die Scouts kosten dich Zeit, sie entscheiden den Kampf nicht.
- **Lenke die Scouts ab.** Ein Scout heilt nur, solange er in Reichweite des Bosses ist; ein Scout, der dir aus der Reichweite folgt, heilt nichts, und eine Ostirion ist schneller als ein Scout.
- **Bleib in Bewegung.** Die Rakete des Bosses ist gerade und ungelenkt: Ein Schiff, das in Bewegung bleibt, weicht ihr aus, eines, das stillsteht, wird getroffen.
- **Bring eine Gruppe mit.** Drei Piloten in Ostirions mit x2-Munition schaffen ihn in Alpha in etwa fünf Minuten; eine Ostirion allein schafft es nicht, eine Paragon allein schon. Der Boss wehrt sich gegen den ersten Piloten, der ihn getroffen hat, also soll das robusteste Schiff anfangen; setze in einem so langen Kampf deine Fähigkeiten ein (Emergency Repair, Shield Surge: [Fähigkeiten](/wiki/03-Mechanics/Abilities.md)). Piloten, die noch Level 2 oder 3 sind, sind ihm zu schwach, auch dort, wo sie fliegen: Halte dich fern, bis du stärker bist.
- **Der Boss kehrt zurück**, nach der Zeit in der Liste *Auf einen Blick*, im selben Sektor.

## Belohnungen und Beute {#rewards-and-drops}

Der Pirate Boss zahlt für den Kampf, der er ist: Eine Minute Kampf gegen ihn zahlt mehr als eine Minute Kampf gegen einen Goombah. Die Bezahlung wird nach Schaden unter den Piloten aufgeteilt, die ihn bekämpft haben ([so zahlt ein Boss-Abschuss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Seine Kiste gehört dem Piloten mit dem meisten Schaden und kann eine **Reinforced Hull Plate**, Raketen und Munition enthalten. Die Scouts zahlen wenig und lassen nichts fallen.

## Die Werte {#the-numbers}

Die Werte der Schwarmschiffe in den drei Welten ([Welten](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss

Basis: Ironclad mit 50 % von Hülle, Schild und Schaden; Tempo und Reichweite bleiben die des Vorbilds. Feuert alle 5 s eine gerade Rakete ab: [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) in `x-2`, [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) in `x-3`.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | 300.000 | 450.000 | 600.000 |
| Schild | 50.100 | 75.150 | 100.200 |
| Laserschaden (eine Salve pro Sekunde) | keiner | keiner | keiner |
| Tempo | 92 | 92 | 92 |
| Laserreichweite | – | – | – |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Raketenschaden, höchstens | 2.500 (Rivet I) / 5.000 (Rivet II) | 3.750 (Rivet I) / 7.500 (Rivet II) | 5.000 (Rivet I) / 10.000 (Rivet II) |
| Credits | 145.000 | 290.000 | 435.000 |
| Thulium | 725 | 1.450 | 2.175 |
| Erfahrung (EP) | 29.000 | 58.000 | 87.000 |
| Ehre | 232 | 464 | 696 |
| PvE-Punkte pro Abschuss | 10 | 10 | 10 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand | Chance | Menge |
| :--- | ---: | ---: |
| Reinforced Hull Plate | 50 % | 1 |
| Eine der 8 [Raketen](/wiki/06-Items/Rockets.md), die man mit Credits kauft, zufällig gewählt | 100 % | 5–10 |
| Eines von Advanced Plasma und Siphon Battery, zufällig gewählt | 100 % | 500–1.000 |

### Pirate Scout

Basis: Kitefin mit 50 % von Hülle, Schild und Schaden; Tempo und Reichweite bleiben die des Vorbilds.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | 12.000 | 18.000 | 24.000 |
| Schild | 9.818 | 14.727 | 19.636 |
| Laserschaden (eine Salve pro Sekunde) | 98 | 147 | 196 |
| Tempo | 175 | 175 | 175 |
| Laserreichweite | 700 | 700 | 700 |
| Aggro-Radius | 700 | 700 | 700 |
| Heilt den Anführer, je Begleiter, pro Sekunde (nur Hülle) | 40 | 60 | 80 |
| Credits | 1.000 | 2.000 | 3.000 |
| Thulium | 4 | 8 | 12 |
| Erfahrung (EP) | 100 | 200 | 300 |
| Ehre | 2 | 4 | 6 |
| PvE-Punkte pro Abschuss | 1 | 1 | 1 |

**Beute**: keine. Der Abschuss zahlt nur seine Credits, sein Thulium, seine EP und seine Ehre.

<!-- pirate-members:end -->
