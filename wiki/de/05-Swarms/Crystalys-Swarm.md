<!-- wiki-i18n source: 2b3edf7bcb1d9673 -->
<!-- wiki-i18n title: Crystalys-Schwarm -->
# Crystalys-Schwarm {#crystalys-swarm}

Der Crystalys-Schwarm ist ein **Boss Crystalys** mit seinen **Crystalys Guards**: das zäheste aller Aliens, der [Crystalys](/wiki/04-Aliens/Crystalys.md), noch größer geworden, mit Wachen, die in seiner Nähe bleiben und ihn heilen. Er lebt in den [Gefahrensektoren](/wiki/01-General/Danger-Sectors.md) `DS-1`, `DS-2` und `DS-3`, in jedem einer, und verlässt seinen Sektor nie. Die Gefahrensektoren sind PvP-Sektoren, der Kampf ist also etwas für eine große Gruppe der stärksten Piloten, und der Boss ist dort nicht die einzige Gefahr.

## Auf einen Blick {#at-a-glance}

<!-- crystalys-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Wo**: Die Gefahrensektoren `DS-1`, `DS-2`, `DS-3`
- **Wie viele**: Einer in jedem dieser Sektoren, 3 in jeder Welt
- **Erscheint**: Ab Saisontag 4 bis zum Wipe (Beta und Gamma: ab Saisontag 1)
- **Anführer**: Boss Crystalys
- **Begleiter**: Bis zu 3 × Crystalys Guard, alle 10 s ein neuer
- **Begleiter bleiben nahe**: höchstens 500 Einheiten vom Anführer entfernt
- **Heilung**: Jeder Crystalys Guard im Umkreis von 600 Einheiten um den Anführer heilt dessen Hülle, in Alpha 250 HP pro Sekunde
- **Anführer zerstört**: Die Begleiter verschwinden 30 s nach der Zerstörung des Anführers, sofern sie nicht gerade angreifen
- **Kehrt zurück**: {{guide:vitals.respawn@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} nach der Zerstörung des Anführers, im selben Sektor
- **Meldungen**: Die Piloten des Sektors erfahren, wann der Anführer auftaucht und wann er zerstört wird. Das sind Systemzeilen: Sie erscheinen im Tab **System** des Chats, mit Zähler für Ungelesenes, und nicht in **Global** oder **Lokal**. Der Kill-Feed nennt den Piloten, dem der Abschuss gutgeschrieben wird.

<!-- crystalys-glance:end -->

## Die Mitglieder {#the-members}

- **Boss Crystalys**: ein größerer Crystalys, in der Färbung des Schwarms und mit seinem Namen darüber, mit eigener Hülle, eigenem Schild und eigener Laser-Salve (die Werte stehen unten). Er ist passiv: Er streift umher, bis ein Pilot ihn trifft, setzt dann diesem Piloten nach und feuert auf ihn, und die Schiffe seines Schwarms in der Nähe greifen mit ein. Reichweite seiner Waffe und seine Geschwindigkeit sind die eines Crystalys, und er repariert seine Hülle nie von selbst. Seine [drei Schritte](#the-leaders-three-steps) und eine [Spezialfähigkeit](/wiki/03-Mechanics/Special-Abilities.md) können das ändern.
- **Crystalys Guard**: ein kleinerer Crystalys in der Färbung des Schwarms. Die Guards bleiben nah beim Boss, greifen ein, wenn ein Schwarmschiff in ihrer Nähe getroffen wird, und jeder, der sich in der Nähe des Bosses befindet, heilt dessen Hülle. Ein Guard repariert seine eigene Hülle nach einer Pause, wie es ein Crystalys tut.

## Wie der Kampf verläuft {#how-the-fight-goes}

- **Nimm eine große Gruppe mit.** In Alpha reichen sechs Piloten von Level 8 in Paragons mit x2-Munition, wenn sein Feuer sich auf sie verteilt, neun, wenn es ganz auf einen Piloten geht; mit x4-Munition sind es fünf und sechs. Mehr Piloten beenden den Kampf früher und verlieren weniger Schiffe, und ein Pilot allein wird zerstört.
- **Schieß auf den Boss, nicht auf die Guards.** Ein Guard fällt in Sekunden, aber ein neuer kommt so oft, wie die Liste *Auf einen Blick* sagt, und was die Guards heilen, ist ein kleiner Teil dessen, was eine Gruppe austeilt: Sie in Ruhe zu lassen kostet etwas Zeit, sie zu jagen kostet mehr.
- **Beta und Gamma sind härter.** Die Schwärme dieser Welten sind stärker ([Welten](/wiki/05-Swarms/Swarms.md#the-worlds)), sie brauchen also mehr Piloten oder bessere Munition.
- **Die Gefahrensektoren sind PvP.** Ein Rivale kann die Gruppe mitten im Kampf angreifen und auf die Kiste warten: Sie gehört 30 Sekunden lang dem Piloten mit dem meisten Schaden (und seinem Clan), danach jedem ([Frachtkisten](/wiki/03-Mechanics/Cargo.md)). Komm nicht allein.
- **Der Boss kehrt zurück**, nach der Zeit in der Liste *Auf einen Blick*, mit voller Stärke, im selben Sektor, und seine Guards kommen nacheinander.

## Die drei Schritte des Anführers {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Sein Kampf hat drei Schritte ([so funktionieren sie](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); jeder geschieht einmal.

- **Am Anfang**: Nimmt für 8 s nur 50 % von jedem Treffer.
- **Unter zwei Dritteln**: Ein Ring von 700 Einheiten trifft jedes Schiff darin mit 4 seiner Salven, und es feuert 4 Raketen.
- **Unter einem Drittel**: Heilt 20 % seiner Hülle und seines Schilds (ein Schadensstoß unterbricht es), und 3 weitere Crystalys Guards kommen, höchstens 6 am Leben.

<!-- mob-ladder:end -->

## Belohnungen und Beute {#rewards-and-drops}

Der Boss Crystalys zahlt für den Kampf, der er ist: Eine Minute Kampf gegen ihn zahlt mehr als eine Minute Kampf gegen einen Crystalys, das bestbezahlte Alien. Die Bezahlung wird nach Schaden unter den Piloten aufgeteilt, die ihn bekämpft haben ([so zahlt ein Boss-Abschuss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Seine Kiste gehört dem Piloten mit dem meisten Schaden und enthält Cataclysite und Quorvium, hin und wieder einen Power Core, eine Ancient Control Unit oder Dark Matter, x3- und x4-Munition und epische Raketen. Die Guards zahlen wenig und lassen nichts fallen; sie zu töten ist kein Farmen, denn sie kommen mit dem Boss zurück.

## Die Werte {#the-numbers}

Die Werte der Schwarmschiffe in den drei Welten ([Welten](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- crystalys-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Crystalys

Basis: Crystalys mit 350 % der Hülle und 100 % des Laserschadens; Tempo und Reichweite bleiben die des Vorbilds.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | {{guide:vitals.hull@Boss Crystalys#1}} | {{guide:vitals.hull@Boss Crystalys#2}} | {{guide:vitals.hull@Boss Crystalys#3}} |
| Schild | {{guide:vitals.shield@Boss Crystalys#1}} | {{guide:vitals.shield@Boss Crystalys#2}} | {{guide:vitals.shield@Boss Crystalys#3}} |
| Laserschaden (eine Salve pro Sekunde) | {{guide:vitals.dps@Boss Crystalys#1}} | {{guide:vitals.dps@Boss Crystalys#2}} | {{guide:vitals.dps@Boss Crystalys#3}} |
| Tempo | {{guide:vitals.speed@Boss Crystalys#1}} | {{guide:vitals.speed@Boss Crystalys#2}} | {{guide:vitals.speed@Boss Crystalys#3}} |
| Laserreichweite | 900 | 900 | 900 |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Credits | {{guide:spoils.pay.credits@Boss Crystalys#1}} | {{guide:spoils.pay.credits@Boss Crystalys#2}} | {{guide:spoils.pay.credits@Boss Crystalys#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Crystalys#1}} | {{guide:spoils.pay.thulium@Boss Crystalys#2}} | {{guide:spoils.pay.thulium@Boss Crystalys#3}} |
| Erfahrung (EP) | {{guide:spoils.pay.experience@Boss Crystalys#1}} | {{guide:spoils.pay.experience@Boss Crystalys#2}} | {{guide:spoils.pay.experience@Boss Crystalys#3}} |
| Ehre | {{guide:spoils.pay.honor@Boss Crystalys#1}} | {{guide:spoils.pay.honor@Boss Crystalys#2}} | {{guide:spoils.pay.honor@Boss Crystalys#3}} |
| PvE-Punkte pro Abschuss | 30 | 30 | 30 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand |
| :--- |
| {{guide:spoils.box@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} |

### Crystalys Guard

Basis: Crystalys mit 15 % von Hülle, Schild und Schaden; Tempo und Reichweite bleiben die des Vorbilds.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | {{guide:vitals.hull@Crystalys Guard#1}} | {{guide:vitals.hull@Crystalys Guard#2}} | {{guide:vitals.hull@Crystalys Guard#3}} |
| Schild | {{guide:vitals.shield@Crystalys Guard#1}} | {{guide:vitals.shield@Crystalys Guard#2}} | {{guide:vitals.shield@Crystalys Guard#3}} |
| Laserschaden (eine Salve pro Sekunde) | {{guide:vitals.dps@Crystalys Guard#1}} | {{guide:vitals.dps@Crystalys Guard#2}} | {{guide:vitals.dps@Crystalys Guard#3}} |
| Tempo | {{guide:vitals.speed@Crystalys Guard#1}} | {{guide:vitals.speed@Crystalys Guard#2}} | {{guide:vitals.speed@Crystalys Guard#3}} |
| Laserreichweite | 900 | 900 | 900 |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Heilt den Anführer, je Begleiter, pro Sekunde (nur Hülle) | 250 | 375 | 500 |
| Credits | {{guide:spoils.pay.credits@Crystalys Guard#1}} | {{guide:spoils.pay.credits@Crystalys Guard#2}} | {{guide:spoils.pay.credits@Crystalys Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Crystalys Guard#1}} | {{guide:spoils.pay.thulium@Crystalys Guard#2}} | {{guide:spoils.pay.thulium@Crystalys Guard#3}} |
| Erfahrung (EP) | {{guide:spoils.pay.experience@Crystalys Guard#1}} | {{guide:spoils.pay.experience@Crystalys Guard#2}} | {{guide:spoils.pay.experience@Crystalys Guard#3}} |
| Ehre | {{guide:spoils.pay.honor@Crystalys Guard#1}} | {{guide:spoils.pay.honor@Crystalys Guard#2}} | {{guide:spoils.pay.honor@Crystalys Guard#3}} |
| PvE-Punkte pro Abschuss | 6 | 6 | 6 |

**Beute**: keine. Der Abschuss zahlt nur seine Credits, sein Thulium, seine EP und seine Ehre.

<!-- crystalys-members:end -->
