<!-- wiki-i18n source: 38ffa8ba7cbf5000 -->
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
- **Kehrt zurück**: {{guide:vitals.respawn@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} nach der Zerstörung des Anführers, im selben Sektor
- **Meldungen**: Die Piloten des Sektors erfahren, wann der Anführer auftaucht und wann er zerstört wird. Das sind Systemzeilen: Sie erscheinen im Tab **System** des Chats, mit Zähler für Ungelesenes, und nicht in **Global** oder **Lokal**. Der Kill-Feed nennt den Piloten, dem der Abschuss gutgeschrieben wird.

<!-- goombah-glance:end -->

## Die Mitglieder {#the-members}

- **Boss Goombah**: ein größerer Goombah, in der Färbung des Schwarms und mit seinem Namen darüber, mit eigener Hülle, eigenem Schild und eigener Laser-Salve (die Werte stehen unten). Er ist passiv: Er streift umher, bis ein Pilot ihn trifft, setzt dann diesem Piloten nach und feuert auf ihn, und die Schiffe seines Schwarms in der Nähe greifen mit ein. Reichweite seiner Waffe und seine Geschwindigkeit sind die eines Goombah, und er repariert seine Hülle nie von selbst. Seine [drei Schritte](#the-leaders-three-steps) und eine [Spezialfähigkeit](/wiki/03-Mechanics/Special-Abilities.md) können das ändern.
- **Goombah Guard**: ein kleinerer Goombah in der Färbung des Schwarms. Die Guards bleiben nah beim Boss, greifen ein, wenn ein Schwarmschiff in ihrer Nähe getroffen wird, und jeder, der sich in der Nähe des Bosses befindet, heilt dessen Hülle. Ein Guard repariert seine eigene Hülle nach einer Pause, wie es ein Goombah tut.

## Wie der Kampf verläuft {#how-the-fight-goes}

- **Nimm eine Gruppe der stärksten Schiffe mit.** Drei Piloten von Level 8 mit x2-Munition zerstören ihn in Alpha in etwa 75 Sekunden und verlieren höchstens ein Schiff; zwei von ihnen brauchen x4-Munition, und Piloten niedrigerer Level richten nicht genug Schaden an, um zu gewinnen.
- **Schieß auf den Boss, nicht auf die Guards.** Ein Guard fällt in Sekunden, aber ein neuer kommt so oft, wie die Liste *Auf einen Blick* sagt, und was die Guards heilen, ist ein kleiner Teil dessen, was eine Gruppe austeilt: Sie in Ruhe zu lassen kostet etwas Zeit, sie zu jagen kostet mehr.
- **Beta und Gamma sind härter.** Die Schwärme dieser Welten sind stärker ([Welten](/wiki/05-Swarms/Swarms.md#the-worlds)), sie brauchen also mehr Piloten oder bessere Munition.
- **Behalte den Sektor im Auge.** `x-4` ist in Alpha ein PvP-Sektor, und in Beta und Gamma sind es `x-3` und `x-4` ([Welten](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): Ein Rivale kann in den Kampf eingreifen oder auf die Kiste warten. Lass ein Schiff der Gruppe Wache halten.
- **Der Boss kehrt zurück**, nach der Zeit in der Liste *Auf einen Blick*, mit voller Stärke, im selben Sektor, und seine Guards kommen nacheinander.

## Die drei Schritte des Anführers {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Sein Kampf hat drei Schritte ([so funktionieren sie](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); jeder geschieht einmal.

- **Am Anfang**: Nimmt für 6 s nur 50 % von jedem Treffer.
- **Unter zwei Dritteln**: Sein Schaden ist für 10 s mit ×1,5 multipliziert und seine Geschwindigkeit mit ×1,25.
- **Unter einem Drittel**: Heilt 25 % seiner Hülle und seines Schilds (ein Schadensstoß unterbricht es), und seine Goombah Guards heilen es währenddessen ×2 so schnell.

<!-- mob-ladder:end -->

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
| Hülle | {{guide:vitals.hull@Boss Goombah#1}} | {{guide:vitals.hull@Boss Goombah#2}} | {{guide:vitals.hull@Boss Goombah#3}} |
| Schild | {{guide:vitals.shield@Boss Goombah#1}} | {{guide:vitals.shield@Boss Goombah#2}} | {{guide:vitals.shield@Boss Goombah#3}} |
| Laserschaden (eine Salve pro Sekunde) | {{guide:vitals.dps@Boss Goombah#1}} | {{guide:vitals.dps@Boss Goombah#2}} | {{guide:vitals.dps@Boss Goombah#3}} |
| Tempo | {{guide:vitals.speed@Boss Goombah#1}} | {{guide:vitals.speed@Boss Goombah#2}} | {{guide:vitals.speed@Boss Goombah#3}} |
| Laserreichweite | 800 | 800 | 800 |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Credits | {{guide:spoils.pay.credits@Boss Goombah#1}} | {{guide:spoils.pay.credits@Boss Goombah#2}} | {{guide:spoils.pay.credits@Boss Goombah#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Goombah#1}} | {{guide:spoils.pay.thulium@Boss Goombah#2}} | {{guide:spoils.pay.thulium@Boss Goombah#3}} |
| Erfahrung (EP) | {{guide:spoils.pay.experience@Boss Goombah#1}} | {{guide:spoils.pay.experience@Boss Goombah#2}} | {{guide:spoils.pay.experience@Boss Goombah#3}} |
| Ehre | {{guide:spoils.pay.honor@Boss Goombah#1}} | {{guide:spoils.pay.honor@Boss Goombah#2}} | {{guide:spoils.pay.honor@Boss Goombah#3}} |
| PvE-Punkte pro Abschuss | 14 | 14 | 14 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand |
| :--- |
| {{guide:spoils.box@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} |

### Goombah Guard

Basis: Goombah mit 20 % von Hülle, Schild und Schaden; Tempo und Reichweite bleiben die des Vorbilds.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | {{guide:vitals.hull@Goombah Guard#1}} | {{guide:vitals.hull@Goombah Guard#2}} | {{guide:vitals.hull@Goombah Guard#3}} |
| Schild | {{guide:vitals.shield@Goombah Guard#1}} | {{guide:vitals.shield@Goombah Guard#2}} | {{guide:vitals.shield@Goombah Guard#3}} |
| Laserschaden (eine Salve pro Sekunde) | {{guide:vitals.dps@Goombah Guard#1}} | {{guide:vitals.dps@Goombah Guard#2}} | {{guide:vitals.dps@Goombah Guard#3}} |
| Tempo | {{guide:vitals.speed@Goombah Guard#1}} | {{guide:vitals.speed@Goombah Guard#2}} | {{guide:vitals.speed@Goombah Guard#3}} |
| Laserreichweite | 800 | 800 | 800 |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Heilt den Anführer, je Begleiter, pro Sekunde (nur Hülle) | 110 | 165 | 220 |
| Credits | {{guide:spoils.pay.credits@Goombah Guard#1}} | {{guide:spoils.pay.credits@Goombah Guard#2}} | {{guide:spoils.pay.credits@Goombah Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Goombah Guard#1}} | {{guide:spoils.pay.thulium@Goombah Guard#2}} | {{guide:spoils.pay.thulium@Goombah Guard#3}} |
| Erfahrung (EP) | {{guide:spoils.pay.experience@Goombah Guard#1}} | {{guide:spoils.pay.experience@Goombah Guard#2}} | {{guide:spoils.pay.experience@Goombah Guard#3}} |
| Ehre | {{guide:spoils.pay.honor@Goombah Guard#1}} | {{guide:spoils.pay.honor@Goombah Guard#2}} | {{guide:spoils.pay.honor@Goombah Guard#3}} |
| PvE-Punkte pro Abschuss | 3 | 3 | 3 |

**Beute**: keine. Der Abschuss zahlt nur seine Credits, sein Thulium, seine EP und seine Ehre.

<!-- goombah-members:end -->
