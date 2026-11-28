<!-- wiki-i18n source: 2eff9c368449da99 -->
<!-- wiki-i18n title: Phantasm-Schwarm -->
# Phantasm-Schwarm {#phantasm-swarm}

Der Phantasm-Schwarm ist ein **Boss Phantasm** mit seinen **Phantasm Guards**: ein riesiger [Phantasm](/wiki/04-Aliens/Phantasm.md), der nie einen Kampf beginnt, und kleinere, die in seiner Nähe bleiben und ihn heilen. Er lebt in den äußeren Sektoren der Konzerne, `x-3` und `x-4`, und ist ein Kampf für eine Gruppe von Piloten mittlerer Stufe.

## Auf einen Blick {#at-a-glance}

<!-- phantasm-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Wo**: Die Sektoren `x-3` und `x-4` jedes Konzerns
- **Wie viele**: Einer in jedem dieser Sektoren, 6 in jeder Welt
- **Erscheint**: Ab Saisontag 4 bis zum Wipe (Beta und Gamma: ab Saisontag 1)
- **Anführer**: Boss Phantasm
- **Begleiter**: Bis zu 4 × Phantasm Guard, alle 10 s ein neuer
- **Begleiter bleiben nahe**: höchstens 500 Einheiten vom Anführer entfernt
- **Heilung**: Jeder Phantasm Guard im Umkreis von 600 Einheiten um den Anführer heilt dessen Hülle, in Alpha 30 HP pro Sekunde
- **Anführer zerstört**: Die Begleiter verschwinden 30 s nach der Zerstörung des Anführers, sofern sie nicht gerade angreifen
- **Kehrt zurück**: {{guide:vitals.respawn@Boss Phantasm#1;Boss Phantasm#2;Boss Phantasm#3}} nach der Zerstörung des Anführers, im selben Sektor
- **Meldungen**: Die Piloten des Sektors erfahren, wann der Anführer auftaucht und wann er zerstört wird. Das sind Systemzeilen: Sie erscheinen im Tab **System** des Chats, mit Zähler für Ungelesenes, und nicht in **Global** oder **Lokal**. Der Kill-Feed nennt den Piloten, dem der Abschuss gutgeschrieben wird.

<!-- phantasm-glance:end -->

## Die Mitglieder {#the-members}

- **Boss Phantasm**: ein größerer Phantasm, in der Färbung des Schwarms und mit seinem Namen darüber, mit eigener Hülle, eigenem Schild und eigener Laser-Salve (die Werte stehen unten). Er ist passiv: Er streift umher, bis ein Pilot ihn trifft, setzt dann diesem Piloten nach und feuert auf ihn, und die Schiffe seines Schwarms in der Nähe greifen mit ein. Reichweite seiner Waffe und seine Geschwindigkeit sind die eines Phantasm, und er repariert seine Hülle nie von selbst. Seine [drei Schritte](#the-leaders-three-steps) und eine [Spezialfähigkeit](/wiki/03-Mechanics/Special-Abilities.md) können das ändern.
- **Phantasm Guard**: ein kleinerer Phantasm in der Färbung des Schwarms. Die Guards bleiben nah beim Boss, greifen ein, wenn ein Schwarmschiff in ihrer Nähe getroffen wird, und jeder, der sich in der Nähe des Bosses befindet, heilt dessen Hülle. Ein Guard repariert seine eigene Hülle nach einer Pause, wie es ein Phantasm tut.

## Wie der Kampf verläuft {#how-the-fight-goes}

- **Nimm eine Gruppe mit.** Drei Piloten von Level 4–5 mit x2-Munition zerstören ihn in Alpha in etwa anderthalb Minuten und verlieren höchstens ein Schiff; ein Pilot dieses Levels allein wird zerstört, und zwei gewinnen nur knapp, und nur solange sich die Treffer verteilen. Bessere Schiffe und x4-Munition machen es viel schneller.
- **Schieß auf den Boss, nicht auf die Guards.** Ein Guard fällt in Sekunden, aber ein neuer kommt so oft, wie die Liste *Auf einen Blick* sagt, und was die Guards heilen, ist ein kleiner Teil dessen, was eine Gruppe austeilt: Sie in Ruhe zu lassen kostet etwas Zeit, sie zu jagen kostet mehr.
- **Beta und Gamma sind härter.** Die Schwärme dieser Welten sind stärker ([Welten](/wiki/05-Swarms/Swarms.md#the-worlds)), sie brauchen also mehr Piloten oder bessere Munition.
- **Behalte den Sektor im Auge.** `x-4` ist in Alpha ein PvP-Sektor, und in Beta und Gamma sind es `x-3` und `x-4` ([Welten](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): Ein Rivale kann in den Kampf eingreifen oder auf die Kiste warten. Lass ein Schiff der Gruppe Wache halten.
- **Der Boss kehrt zurück**, nach der Zeit in der Liste *Auf einen Blick*, mit voller Stärke, im selben Sektor, und seine Guards kommen nacheinander.

## Die drei Schritte des Anführers {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Sein Kampf hat drei Schritte ([so funktionieren sie](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); jeder geschieht einmal.

- **Am Anfang**: Jeder seiner Phantasm Guards baut eine Schildschicht von 10 % der eigenen Hülle auf.
- **Unter zwei Dritteln**: 3 Kopien von ihm erscheinen, und das echte trägt einen Ring.
- **Unter einem Drittel**: Springt etwa 2.500 Einheiten von den Piloten weg, und seine Phantasm Guards kommen heil um es zurück.

<!-- mob-ladder:end -->

## Belohnungen und Beute {#rewards-and-drops}

Der Boss Phantasm zahlt für den Kampf, der er ist: Eine Minute Kampf gegen ihn zahlt mehr als eine Minute Kampf gegen einen Goombah, das bestbezahlte Alien dieser Sektoren. Die Bezahlung wird nach Schaden unter den Piloten aufgeteilt, die ihn bekämpft haben ([so zahlt ein Boss-Abschuss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Seine Kiste gehört dem Piloten mit dem meisten Schaden und enthält die Beute eines Phantasm vielfach (Ship Fragments, Daraxium und Nyxite) sowie Munition und Raketen. Die Guards zahlen wenig und lassen nichts fallen; sie zu töten ist kein Farmen, denn sie kommen mit dem Boss zurück.

## Die Werte {#the-numbers}

Die Werte der Schwarmschiffe in den drei Welten ([Welten](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- phantasm-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Phantasm

Basis: Phantasm mit 2.000 % der Hülle und 300 % des Laserschadens; Tempo und Reichweite bleiben die des Vorbilds.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | {{guide:vitals.hull@Boss Phantasm#1}} | {{guide:vitals.hull@Boss Phantasm#2}} | {{guide:vitals.hull@Boss Phantasm#3}} |
| Schild | {{guide:vitals.shield@Boss Phantasm#1}} | {{guide:vitals.shield@Boss Phantasm#2}} | {{guide:vitals.shield@Boss Phantasm#3}} |
| Laserschaden (eine Salve pro Sekunde) | {{guide:vitals.dps@Boss Phantasm#1}} | {{guide:vitals.dps@Boss Phantasm#2}} | {{guide:vitals.dps@Boss Phantasm#3}} |
| Tempo | {{guide:vitals.speed@Boss Phantasm#1}} | {{guide:vitals.speed@Boss Phantasm#2}} | {{guide:vitals.speed@Boss Phantasm#3}} |
| Laserreichweite | 700 | 700 | 700 |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Credits | {{guide:spoils.pay.credits@Boss Phantasm#1}} | {{guide:spoils.pay.credits@Boss Phantasm#2}} | {{guide:spoils.pay.credits@Boss Phantasm#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Phantasm#1}} | {{guide:spoils.pay.thulium@Boss Phantasm#2}} | {{guide:spoils.pay.thulium@Boss Phantasm#3}} |
| Erfahrung (EP) | {{guide:spoils.pay.experience@Boss Phantasm#1}} | {{guide:spoils.pay.experience@Boss Phantasm#2}} | {{guide:spoils.pay.experience@Boss Phantasm#3}} |
| Ehre | {{guide:spoils.pay.honor@Boss Phantasm#1}} | {{guide:spoils.pay.honor@Boss Phantasm#2}} | {{guide:spoils.pay.honor@Boss Phantasm#3}} |
| PvE-Punkte pro Abschuss | 8 | 8 | 8 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand |
| :--- |
| {{guide:spoils.box@Boss Phantasm#1;Boss Phantasm#2;Boss Phantasm#3}} |

### Phantasm Guard

Basis: Phantasm mit 50 % von Hülle, Schild und Schaden; Tempo und Reichweite bleiben die des Vorbilds.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | {{guide:vitals.hull@Phantasm Guard#1}} | {{guide:vitals.hull@Phantasm Guard#2}} | {{guide:vitals.hull@Phantasm Guard#3}} |
| Schild | {{guide:vitals.shield@Phantasm Guard#1}} | {{guide:vitals.shield@Phantasm Guard#2}} | {{guide:vitals.shield@Phantasm Guard#3}} |
| Laserschaden (eine Salve pro Sekunde) | {{guide:vitals.dps@Phantasm Guard#1}} | {{guide:vitals.dps@Phantasm Guard#2}} | {{guide:vitals.dps@Phantasm Guard#3}} |
| Tempo | {{guide:vitals.speed@Phantasm Guard#1}} | {{guide:vitals.speed@Phantasm Guard#2}} | {{guide:vitals.speed@Phantasm Guard#3}} |
| Laserreichweite | 700 | 700 | 700 |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Heilt den Anführer, je Begleiter, pro Sekunde (nur Hülle) | 30 | 45 | 60 |
| Credits | {{guide:spoils.pay.credits@Phantasm Guard#1}} | {{guide:spoils.pay.credits@Phantasm Guard#2}} | {{guide:spoils.pay.credits@Phantasm Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Phantasm Guard#1}} | {{guide:spoils.pay.thulium@Phantasm Guard#2}} | {{guide:spoils.pay.thulium@Phantasm Guard#3}} |
| Erfahrung (EP) | {{guide:spoils.pay.experience@Phantasm Guard#1}} | {{guide:spoils.pay.experience@Phantasm Guard#2}} | {{guide:spoils.pay.experience@Phantasm Guard#3}} |
| Ehre | {{guide:spoils.pay.honor@Phantasm Guard#1}} | {{guide:spoils.pay.honor@Phantasm Guard#2}} | {{guide:spoils.pay.honor@Phantasm Guard#3}} |
| PvE-Punkte pro Abschuss | 1 | 1 | 1 |

**Beute**: keine. Der Abschuss zahlt nur seine Credits, sein Thulium, seine EP und seine Ehre.

<!-- phantasm-members:end -->
