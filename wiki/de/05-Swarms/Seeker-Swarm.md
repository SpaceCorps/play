<!-- wiki-i18n source: babc7a19c6dcab42 -->
<!-- wiki-i18n title: Seeker-Schwarm -->
# Seeker-Schwarm {#seeker-swarm}

Der Seeker-Schwarm ist der kleinste der [Schwärme](/wiki/05-Swarms/Swarms.md): ein **Boss Seeker** und die **Seeker Slaves**, die ihn bewachen und heilen. Er lebt in den Sektoren, in denen neue Piloten zu fliegen beginnen, und ist deshalb der erste Schwarm, dem die meisten Piloten begegnen. Der Boss Seeker beginnt nie einen Kampf, aber sobald du auf ihn schießt, ist er weit gefährlicher als der [Seeker](/wiki/04-Aliens/Seeker.md), auf dem er aufbaut.

## Auf einen Blick {#at-a-glance}

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Wo**: Die Sektoren `x-1` und `x-2` jedes Konzerns
- **Wie viele**: Einer in jedem dieser Sektoren, 6 in jeder Welt
- **Erscheint**: Ab Saisontag 4 bis zum Wipe
- **Anführer**: Boss Seeker
- **Begleiter**: Bis zu 4 × Seeker Slave, alle 10 s ein neuer
- **Begleiter bleiben nahe**: höchstens 500 Einheiten vom Anführer entfernt
- **Heilung**: Jeder Seeker Slave im Umkreis von 600 Einheiten um den Anführer heilt dessen Hülle, in Alpha 50 HP pro Sekunde
- **Anführer zerstört**: Die Begleiter verschwinden 30 s nach der Zerstörung des Anführers, sofern sie nicht gerade angreifen
- **Kehrt zurück**: 2 min nach der Zerstörung des Anführers, im selben Sektor
- **Meldungen**: Die Piloten des Sektors erfahren, wann der Anführer auftaucht und wann er zerstört wird. Das sind Systemzeilen: Sie erscheinen im Tab **System** des Chats, mit Zähler für Ungelesenes, und nicht in **Global** oder **Lokal**. Der Kill-Feed nennt den Piloten, dem der Abschuss gutgeschrieben wird.

<!-- seeker-glance:end -->

## Die Mitglieder {#the-members}

- **Boss Seeker**: ein viel größerer Seeker, in der Färbung des Schwarms und mit seinem Namen darüber, mit dem Vielfachen von Hülle, Schild und Schaden eines Seeker (die Werte stehen unten). Er ist passiv: Er streift umher, bis ein Pilot ihn trifft, bleibt dann stehen und feuert auf diesen Piloten, und die Schiffe seines Schwarms in der Nähe greifen mit ein. Reichweite seiner Waffe und Tempo sind die eines Seeker, und seine Hülle repariert er nie von selbst.
- **Seeker Slave**: ein gewöhnlicher Seeker in der Färbung des Schwarms. Die Slaves bleiben nah beim Boss, greifen ein, wenn ein Schwarmschiff in ihrer Nähe getroffen wird, und jeder, der sich in der Nähe des Bosses befindet, heilt dessen Hülle. Ein Slave repariert seine eigene Hülle nach einer Pause, wie es ein Seeker tut.

## Wie der Kampf verläuft {#how-the-fight-goes}

- **Lass ihn in Ruhe, bis dein Schiff ihm gewachsen ist.** Ein Boss Seeker teilt härter aus, als das erste Schiff eines Piloten aushält: Die Protos eines neuen Piloten, noch ohne Schild, ist in Sekunden zerstört, sobald der Boss und seine Slaves auf ihr sind.
- **Bleib außer Reichweite.** Der Boss und seine Slaves sind langsamer als eine Protos, und ihre Waffen reichen weniger weit als ein Quantum Laser 2 (siehe [Laser & Munition](/wiki/06-Items/Lasers.md)): Ein Pilot mit solchen Lasern, der außerhalb ihrer Reichweite bleibt, erleidet keinen Schaden, während sie feuern. Ein Pilot mit Quantum Laser 1 kann nicht außer Reichweite bleiben.
- **Die Slaves heilen schneller, als ein einzelner neuer Pilot trifft.** Zusammen heilen sie mehr, als die Laser eines Piloten mit x1-Munition austeilen, also nimm einen Partner und x2-Munition mit. Zwei Piloten mit Quantum Laser 2, die Abstand halten, erledigen den Boss in Alpha in etwa einer Minute, mit x2-Munition viel schneller.
- **Der Boss kehrt zurück**, nach der Zeit in der Liste *Auf einen Blick*, mit voller Stärke, im selben Sektor, und seine Slaves kommen nacheinander.

## Belohnungen und Beute {#rewards-and-drops}

Der Boss Seeker zahlt **genau zehn Seeker**: das Zehnfache von Credits, Thulium, EP und Ehre eines Seeker, aufgeteilt nach Schaden unter den Piloten, die ihn bekämpft haben ([so zahlt ein Boss-Abschuss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Seine Kiste enthält die Beute von zehn Seekern und obendrein Munition und Raketen unterhalb von Episch, für den Piloten mit dem meisten Schaden. Die Slaves zahlen wenig und lassen nichts fallen; sie abzuschießen ist kein Farming, denn sie kommen mit dem Boss zurück.

## Die Werte {#the-numbers}

Die Werte der Schwarmschiffe in den drei Welten ([Welten](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker {#boss-seeker}

Basis: Seeker mit 400 % von Hülle, Schild und Schaden; Tempo und Reichweite bleiben die des Vorbilds.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | 3.200 | 4.800 | 6.400 |
| Schild | 3.200 | 4.800 | 6.400 |
| Laserschaden (eine Salve pro Sekunde) | 720 | 1.080 | 1.440 |
| Tempo | 120 | 120 | 120 |
| Laserreichweite | 600 | 600 | 600 |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Credits | 10.000 | 20.000 | 30.000 |
| Thulium | 40 | 80 | 120 |
| Erfahrung (EP) | 1.000 | 2.000 | 3.000 |
| Ehre | 20 | 40 | 60 |
| PvE-Punkte pro Abschuss | 5 | 5 | 5 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand | Chance | Menge |
| :--- | ---: | ---: |
| Ship Fragment | 20 % bei jedem von 10 Würfen | 1 |
| Daraxium | 50 % bei jedem von 10 Würfen | 1–2 |
| Standard Battery | 100 % | 200–400 |
| Advanced Plasma | 100 % | 10–20 |
| Ultra Core | 100 % | 2–4 |
| Eine der 8 [Raketen](/wiki/06-Items/Rockets.md), die man mit Credits kauft, zufällig gewählt | 100 % | 2–3 |

### Seeker Slave {#seeker-slave}

Basis: Seeker mit 100 % von Hülle, Schild und Schaden; Tempo und Reichweite bleiben die des Vorbilds.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | 800 | 1.200 | 1.600 |
| Schild | 800 | 1.200 | 1.600 |
| Laserschaden (eine Salve pro Sekunde) | 180 | 270 | 360 |
| Tempo | 120 | 120 | 120 |
| Laserreichweite | 600 | 600 | 600 |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Heilt den Anführer, je Begleiter, pro Sekunde (nur Hülle) | 50 | 75 | 100 |
| Credits | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Erfahrung (EP) | 12 | 24 | 36 |
| Ehre | 1 | 2 | 3 |
| PvE-Punkte pro Abschuss | 1 | 1 | 1 |

**Beute**: keine. Der Abschuss zahlt nur seine Credits, sein Thulium, seine EP und seine Ehre.

<!-- seeker-members:end -->
