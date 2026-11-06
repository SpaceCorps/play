<!-- wiki-i18n source: 7859e3f6a7efac1e -->
<!-- wiki-i18n title: Goombah-Schwarm -->
# Goombah-Schwarm {#goombah-swarm}

Der Goombah-Schwarm ist ein **Boss Goombah** mit seinen **Goombah Guards**: ein gewaltiger [Goombah](/wiki/04-Aliens/Goombah.md), der nie einen Kampf beginnt, und kleinere, die in seiner Nähe bleiben und ihn heilen. Er lebt in denselben Sektoren wie der [Phantasm-Schwarm](/wiki/05-Swarms/Phantasm-Swarm.md), `x-3` und `x-4`, und ist ein Kampf für eine Gruppe der stärksten Piloten der Konzernsektoren.

## Auf einen Blick {#at-a-glance}

<!-- goombah-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Wo**: Die Sektoren `x-3` und `x-4` jedes Konzerns
- **Wie viele**: Einer in jedem dieser Sektoren, 6 in jeder Welt
- **Erscheint**: Ab Saisontag 4 bis zum Wipe (Beta und Gamma: ab Saisontag 1)
- **Anführer**: Boss Goombah
- **Begleiter**: Bis zu 4 × Goombah Guard, alle 10 s ein neuer
- **Begleiter bleiben nahe**: höchstens 500 Einheiten vom Anführer entfernt
- **Heilung**: Jeder Goombah Guard im Umkreis von 600 Einheiten um den Anführer heilt dessen Hülle, in Alpha 110 HP pro Sekunde
- **Anführer zerstört**: Die Begleiter verschwinden 30 s nach der Zerstörung des Anführers, sofern sie nicht gerade angreifen
- **Kehrt zurück**: 5 min nach der Zerstörung des Anführers, im selben Sektor
- **Meldungen**: Die Piloten des Sektors erfahren, wann der Anführer auftaucht und wann er zerstört wird. Das sind Systemzeilen: Sie erscheinen im Tab **System** des Chats, mit Zähler für Ungelesenes, und nicht in **Global** oder **Lokal**. Der Kill-Feed nennt den Piloten, dem der Abschuss gutgeschrieben wird.

<!-- goombah-glance:end -->

## Die Mitglieder {#the-members}

- **Boss Goombah**: ein größerer Goombah, in der Färbung des Schwarms und mit seinem Namen darüber, mit eigener Hülle, eigenem Schild und eigener Laser-Salve (die Werte stehen unten). Er ist passiv: Er streift umher, bis ein Pilot ihn trifft, setzt dann diesem Piloten nach und feuert auf ihn, und die Schiffe seines Schwarms in der Nähe greifen mit ein. Reichweite seiner Waffe und seine Geschwindigkeit sind die eines Goombah, und er repariert seine Hülle nie von selbst.
- **Goombah Guard**: ein kleinerer Goombah in der Färbung des Schwarms. Die Guards bleiben nah beim Boss, greifen ein, wenn ein Schwarmschiff in ihrer Nähe getroffen wird, und jeder, der sich in der Nähe des Bosses befindet, heilt dessen Hülle. Ein Guard repariert seine eigene Hülle nach einer Pause, wie es ein Goombah tut.

## Wie der Kampf verläuft {#how-the-fight-goes}

- **Nimm eine Gruppe der stärksten Schiffe mit.** Drei Piloten von Level 8 mit x2-Munition zerstören ihn in Alpha in etwa 75 Sekunden und verlieren höchstens ein Schiff; zwei von ihnen brauchen x4-Munition, und Piloten niedrigerer Level richten nicht genug Schaden an, um zu gewinnen.
- **Schieß auf den Boss, nicht auf die Guards.** Ein Guard fällt in Sekunden, aber ein neuer kommt so oft, wie die Liste *Auf einen Blick* sagt, und was die Guards heilen, ist ein kleiner Teil dessen, was eine Gruppe austeilt: Sie in Ruhe zu lassen kostet etwas Zeit, sie zu jagen kostet mehr.
- **Beta und Gamma sind härter.** Die Schwärme dieser Welten sind stärker ([Welten](/wiki/05-Swarms/Swarms.md#the-worlds)), sie brauchen also mehr Piloten oder bessere Munition.
- **Behalte den Sektor im Auge.** `x-4` ist in Alpha ein PvP-Sektor, und in Beta und Gamma sind es `x-3` und `x-4` ([Welten](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): Ein Rivale kann in den Kampf eingreifen oder auf die Kiste warten. Lass ein Schiff der Gruppe Wache halten.
- **Der Boss kehrt zurück**, nach der Zeit in der Liste *Auf einen Blick*, mit voller Stärke, im selben Sektor, und seine Guards kommen nacheinander.

## Belohnungen und Beute {#rewards-and-drops}

Der Boss Goombah zahlt für den Kampf, der er ist: Eine Minute Kampf gegen ihn zahlt mehr als eine Minute Kampf gegen einen Goombah, das bestbezahlte Alien dieser Sektoren. Die Bezahlung wird nach Schaden unter den Piloten aufgeteilt, die ihn bekämpft haben ([so zahlt ein Boss-Abschuss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Seine Kiste gehört dem Piloten mit dem meisten Schaden und enthält die Beute eines Goombah mehrfach (Cataclysite, Quorvium, Power Cores, Reinforced Hull Plates und Ship Fragments) sowie Munition und Raketen. Die Guards zahlen wenig und lassen nichts fallen; sie zu töten ist kein Farmen, denn sie kommen mit dem Boss zurück.

## Die Werte {#the-numbers}

Die Werte der Schwarmschiffe in den drei Welten ([Welten](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- goombah-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Goombah

Basis: Goombah mit 400 % der Hülle und 100 % des Laserschadens; Tempo und Reichweite bleiben die des Vorbilds.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | 128.000 | 192.000 | 256.000 |
| Schild | 192.000 | 288.000 | 384.000 |
| Laserschaden (eine Salve pro Sekunde) | 3.000 | 4.500 | 6.000 |
| Tempo | 180 | 180 | 180 |
| Laserreichweite | 800 | 800 | 800 |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Credits | 120.000 | 240.000 | 360.000 |
| Thulium | 600 | 1.200 | 1.800 |
| Erfahrung (EP) | 24.000 | 48.000 | 72.000 |
| Ehre | 192 | 384 | 576 |
| PvE-Punkte pro Abschuss | 14 | 14 | 14 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand | Chance | Menge |
| :--- | ---: | ---: |
| Ship Fragment | 100 % bei jedem von 8 Würfen | 3 |
| Reinforced Hull Plate | 60 % bei jedem von 8 Würfen | 1 |
| Power Core | 25 % bei jedem von 8 Würfen | 1 |
| Cataclysite | 100 % bei jedem von 8 Würfen | 4 |
| Quorvium | 100 % bei jedem von 8 Würfen | 2–4 |
| Advanced Plasma | 100 % | 100–200 |
| Ultra Core | 100 % | 100–200 |
| Eine der 8 [Raketen](/wiki/06-Items/Rockets.md), die man mit Credits kauft, zufällig gewählt | 100 % | 6–10 |

### Goombah Guard

Basis: Goombah mit 20 % von Hülle, Schild und Schaden; Tempo und Reichweite bleiben die des Vorbilds.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | 6.400 | 9.600 | 12.800 |
| Schild | 9.600 | 14.400 | 19.200 |
| Laserschaden (eine Salve pro Sekunde) | 600 | 900 | 1.200 |
| Tempo | 180 | 180 | 180 |
| Laserreichweite | 800 | 800 | 800 |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Heilt den Anführer, je Begleiter, pro Sekunde (nur Hülle) | 110 | 165 | 220 |
| Credits | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Erfahrung (EP) | 12 | 24 | 36 |
| Ehre | 1 | 2 | 3 |
| PvE-Punkte pro Abschuss | 3 | 3 | 3 |

**Beute**: keine. Der Abschuss zahlt nur seine Credits, sein Thulium, seine EP und seine Ehre.

<!-- goombah-members:end -->
