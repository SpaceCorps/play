<!-- wiki-i18n source: 7c6bc3eaf70223f5 -->
<!-- wiki-i18n title: Seeker-Schwarm -->
# Seeker-Schwarm {#seeker-swarm}

Der Seeker-Schwarm ist der kleinste der [Schwärme](/wiki/05-Swarms/Swarms.md): ein **Boss Seeker** und die **Seeker Slaves**, die ihn bewachen und heilen. Er lebt in den Sektoren, in denen neue Piloten zu fliegen beginnen, und ist deshalb der erste Schwarm, dem die meisten Piloten begegnen. Der Boss Seeker beginnt nie einen Kampf, aber sobald du auf ihn schießt, ist er weit gefährlicher als der [Seeker](/wiki/04-Aliens/Seeker.md), auf dem er aufbaut.

## Auf einen Blick {#at-a-glance}

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Wo**: Die Sektoren `x-1` und `x-2` jedes Konzerns
- **Wie viele**: Einer in jedem dieser Sektoren, 6 in jeder Welt
- **Erscheint**: Ab Saisontag 4 bis zum Wipe (Beta und Gamma: ab Saisontag 1)
- **Anführer**: Boss Seeker
- **Begleiter**: Bis zu 4 × Seeker Slave, alle 10 s ein neuer
- **Begleiter bleiben nahe**: höchstens 500 Einheiten vom Anführer entfernt
- **Heilung**: Jeder Seeker Slave im Umkreis von 600 Einheiten um den Anführer heilt dessen Hülle, in Alpha 50 HP pro Sekunde
- **Anführer zerstört**: Die Begleiter verschwinden 30 s nach der Zerstörung des Anführers, sofern sie nicht gerade angreifen
- **Kehrt zurück**: {{guide:vitals.respawn@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} nach der Zerstörung des Anführers, im selben Sektor
- **Meldungen**: Die Piloten des Sektors erfahren, wann der Anführer auftaucht und wann er zerstört wird. Das sind Systemzeilen: Sie erscheinen im Tab **System** des Chats, mit Zähler für Ungelesenes, und nicht in **Global** oder **Lokal**. Der Kill-Feed nennt den Piloten, dem der Abschuss gutgeschrieben wird.

<!-- seeker-glance:end -->

## Die Mitglieder {#the-members}

- **Boss Seeker**: ein viel größerer Seeker, in der Färbung des Schwarms und mit seinem Namen darüber, mit dem Vielfachen von Hülle, Schild und Schaden eines Seeker (die Werte stehen unten). Er ist passiv: Er streift umher, bis ein Pilot ihn trifft, bleibt dann stehen und feuert auf diesen Piloten, und die Schiffe seines Schwarms in der Nähe greifen mit ein. Reichweite seiner Waffe und Tempo sind die eines Seeker, und seine Hülle repariert er nie von selbst. Seine [drei Schritte](#the-leaders-three-steps) und eine [Spezialfähigkeit](/wiki/03-Mechanics/Special-Abilities.md) können das ändern.
- **Seeker Slave**: ein gewöhnlicher Seeker in der Färbung des Schwarms. Die Slaves bleiben nah beim Boss, greifen ein, wenn ein Schwarmschiff in ihrer Nähe getroffen wird, und jeder, der sich in der Nähe des Bosses befindet, heilt dessen Hülle. Ein Slave repariert seine eigene Hülle nach einer Pause, wie es ein Seeker tut.

## Wie der Kampf verläuft {#how-the-fight-goes}

- **Lass ihn in Ruhe, bis dein Schiff ihm gewachsen ist.** Ein Boss Seeker teilt härter aus, als das erste Schiff eines Piloten aushält: Die Protos eines neuen Piloten, noch ohne Schild, ist in Sekunden zerstört, sobald der Boss und seine Slaves auf ihr sind.
- **Bleib außer Reichweite.** Der Boss und seine Slaves sind langsamer als eine Protos, und ihre Waffen reichen weniger weit als ein Quantum Laser II (siehe [Laser & Munition](/wiki/06-Items/Lasers.md)): Ein Pilot mit solchen Lasern, der außerhalb ihrer Reichweite bleibt, erleidet keinen Schaden, während sie feuern. Ein Pilot mit Quantum Laser I kann nicht außer Reichweite bleiben.
- **Die Slaves heilen schneller, als ein einzelner neuer Pilot trifft.** Zusammen heilen sie mehr, als die Laser eines Piloten mit x1-Munition austeilen, also nimm einen Partner und x2-Munition mit. Zwei Piloten mit Quantum Laser II, die Abstand halten, erledigen den Boss in Alpha in etwa einer Minute, mit x2-Munition viel schneller.
- **Der Boss kehrt zurück**, nach der Zeit in der Liste *Auf einen Blick*, mit voller Stärke, im selben Sektor, und seine Slaves kommen nacheinander.

## Die drei Schritte des Anführers {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Sein Kampf hat drei Schritte ([so funktionieren sie](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); jeder geschieht einmal.

- **Am Anfang**: Seine Seeker Slaves heilen es ×2 so schnell für 8 s.
- **Unter zwei Dritteln**: 2 Kopien von ihm erscheinen, und das echte trägt einen Ring.
- **Unter einem Drittel**: Fliegt für 4 s von den Piloten weg und wendet sich dann wieder zu.

<!-- mob-ladder:end -->

## Belohnungen und Beute {#rewards-and-drops}

Der Boss Seeker zahlt **genau zehn Seeker**: das Zehnfache von Credits, Thulium, EP und Ehre eines Seeker, aufgeteilt nach Schaden unter den Piloten, die ihn bekämpft haben ([so zahlt ein Boss-Abschuss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Seine Kiste enthält die Beute von zehn Seekern und obendrein Munition und Raketen unterhalb von Episch, für den Piloten mit dem meisten Schaden. Die Slaves zahlen wenig und lassen nichts fallen; sie abzuschießen ist kein Farming, denn sie kommen mit dem Boss zurück.

## Die Werte {#the-numbers}

Die Werte der Schwarmschiffe in den drei Welten ([Welten](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker

Basis: Seeker mit 400 % von Hülle, Schild und Schaden; Tempo und Reichweite bleiben die des Vorbilds.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | {{guide:vitals.hull@Boss Seeker#1}} | {{guide:vitals.hull@Boss Seeker#2}} | {{guide:vitals.hull@Boss Seeker#3}} |
| Schild | {{guide:vitals.shield@Boss Seeker#1}} | {{guide:vitals.shield@Boss Seeker#2}} | {{guide:vitals.shield@Boss Seeker#3}} |
| Laserschaden (eine Salve pro Sekunde) | {{guide:vitals.dps@Boss Seeker#1}} | {{guide:vitals.dps@Boss Seeker#2}} | {{guide:vitals.dps@Boss Seeker#3}} |
| Tempo | {{guide:vitals.speed@Boss Seeker#1}} | {{guide:vitals.speed@Boss Seeker#2}} | {{guide:vitals.speed@Boss Seeker#3}} |
| Laserreichweite | 600 | 600 | 600 |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Credits | {{guide:spoils.pay.credits@Boss Seeker#1}} | {{guide:spoils.pay.credits@Boss Seeker#2}} | {{guide:spoils.pay.credits@Boss Seeker#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Seeker#1}} | {{guide:spoils.pay.thulium@Boss Seeker#2}} | {{guide:spoils.pay.thulium@Boss Seeker#3}} |
| Erfahrung (EP) | {{guide:spoils.pay.experience@Boss Seeker#1}} | {{guide:spoils.pay.experience@Boss Seeker#2}} | {{guide:spoils.pay.experience@Boss Seeker#3}} |
| Ehre | {{guide:spoils.pay.honor@Boss Seeker#1}} | {{guide:spoils.pay.honor@Boss Seeker#2}} | {{guide:spoils.pay.honor@Boss Seeker#3}} |
| PvE-Punkte pro Abschuss | 5 | 5 | 5 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand |
| :--- |
| {{guide:spoils.box@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} |

### Seeker Slave

Basis: Seeker mit 100 % von Hülle, Schild und Schaden; Tempo und Reichweite bleiben die des Vorbilds.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | {{guide:vitals.hull@Seeker Slave#1}} | {{guide:vitals.hull@Seeker Slave#2}} | {{guide:vitals.hull@Seeker Slave#3}} |
| Schild | {{guide:vitals.shield@Seeker Slave#1}} | {{guide:vitals.shield@Seeker Slave#2}} | {{guide:vitals.shield@Seeker Slave#3}} |
| Laserschaden (eine Salve pro Sekunde) | {{guide:vitals.dps@Seeker Slave#1}} | {{guide:vitals.dps@Seeker Slave#2}} | {{guide:vitals.dps@Seeker Slave#3}} |
| Tempo | {{guide:vitals.speed@Seeker Slave#1}} | {{guide:vitals.speed@Seeker Slave#2}} | {{guide:vitals.speed@Seeker Slave#3}} |
| Laserreichweite | 600 | 600 | 600 |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Heilt den Anführer, je Begleiter, pro Sekunde (nur Hülle) | 50 | 75 | 100 |
| Credits | {{guide:spoils.pay.credits@Seeker Slave#1}} | {{guide:spoils.pay.credits@Seeker Slave#2}} | {{guide:spoils.pay.credits@Seeker Slave#3}} |
| Thulium | {{guide:spoils.pay.thulium@Seeker Slave#1}} | {{guide:spoils.pay.thulium@Seeker Slave#2}} | {{guide:spoils.pay.thulium@Seeker Slave#3}} |
| Erfahrung (EP) | {{guide:spoils.pay.experience@Seeker Slave#1}} | {{guide:spoils.pay.experience@Seeker Slave#2}} | {{guide:spoils.pay.experience@Seeker Slave#3}} |
| Ehre | {{guide:spoils.pay.honor@Seeker Slave#1}} | {{guide:spoils.pay.honor@Seeker Slave#2}} | {{guide:spoils.pay.honor@Seeker Slave#3}} |
| PvE-Punkte pro Abschuss | 1 | 1 | 1 |

**Beute**: keine. Der Abschuss zahlt nur seine Credits, sein Thulium, seine EP und seine Ehre.

<!-- seeker-members:end -->
