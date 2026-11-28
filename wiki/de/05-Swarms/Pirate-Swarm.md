<!-- wiki-i18n source: 33448f95d2520b3a -->
<!-- wiki-i18n title: Pirate-Schwarm -->
# Pirate-Schwarm {#pirate-swarm}

Der Pirate-Schwarm besteht aus einem **Pirate Boss** mit seinen **Pirate Scouts**: einem riesigen, langsamen Schiff, das niemanden angreift und mit Raketen antwortet, und einem Rudel schnellerer Schiffe, die es bewachen und heilen. Er lebt in den Sektoren zwischen der Basis eines Konzerns und seiner Grenze, wo die mittleren Stufen des Spiels gespielt werden, und ist ein langer Kampf für eine Gruppe von Piloten, kein schneller Abschuss.

## Auf einen Blick {#at-a-glance}

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Wo**: Die Sektoren `x-2` und `x-3` jedes Konzerns
- **Wie viele**: Einer in jedem dieser Sektoren, 6 in jeder Welt
- **Erscheint**: Ab Saisontag 4 bis zum Wipe (Beta und Gamma: ab Saisontag 1)
- **Anführer**: Pirate Boss
- **Begleiter**: Bis zu 5 × Pirate Scout, alle 10 s ein neuer
- **Begleiter bleiben nahe**: höchstens 900 Einheiten vom Anführer entfernt
- **Heilung**: Jeder Pirate Scout im Umkreis von 600 Einheiten um den Anführer heilt dessen Hülle, in Alpha 40 HP pro Sekunde
- **Anführer zerstört**: Die Begleiter verschwinden 1 min nach der Zerstörung des Anführers, sofern sie nicht gerade angreifen
- **Kehrt zurück**: {{guide:vitals.respawn@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} nach der Zerstörung des Anführers, im selben Sektor
- **Meldungen**: Die Piloten des Sektors erfahren, wann der Anführer auftaucht und wann er zerstört wird. Das sind Systemzeilen: Sie erscheinen im Tab **System** des Chats, mit Zähler für Ungelesenes, und nicht in **Global** oder **Lokal**. Der Kill-Feed nennt den Piloten, dem der Abschuss gutgeschrieben wird.

<!-- pirate-glance:end -->

## Die Mitglieder {#the-members}

- **Pirate Boss**: ein Schiff auf Basis der Ironclad, mit einem Teil ihrer Stärke (die Werte stehen unten). Er ist passiv und feuert **keine Laser**: Seine einzige Waffe ist eine **gerade Rakete** ([Raketen](/wiki/06-Items/Rockets.md); welche, hängt vom Sektor ab, siehe die Tabelle) auf den Piloten, der ihn angegriffen hat, und er streift weiter umher, während er feuert. Seine Hülle repariert er nie von selbst. Seine [drei Schritte](#the-leaders-three-steps) und eine [Spezialfähigkeit](/wiki/03-Mechanics/Special-Abilities.md) können das ändern.
- **Pirate Scout**: ein Schiff auf Basis der Kitefin, mit einem Teil ihrer Stärke. Scouts greifen jeden Piloten an, der ihnen nahe kommt, bleiben nah beim Boss, und jeder, der in der Nähe des Bosses ist, heilt dessen Hülle.

## Wie der Kampf verläuft {#how-the-fight-goes}

- **Schieß auf den Boss, nicht auf die Scouts.** Die Scouts heilen den Boss, aber die Heilung ist klein gegen seine Hülle, und ein neuer Scout kommt so oft, wie die Liste *Auf einen Blick* sagt: Eine Gruppe, die zuerst die Scouts abschießt, holt sie nie ein, und nur eine sehr große Gruppe kann sie beseitigen und braucht dann trotzdem länger für den Boss als eine, die sie in Ruhe gelassen hat. Die Scouts kosten dich Zeit, sie entscheiden den Kampf nicht.
- **Lenke die Scouts ab.** Ein Scout heilt nur, solange er in Reichweite des Bosses ist; ein Scout, der dir aus der Reichweite folgt, heilt nichts, und eine Ostirion ist schneller als ein Scout.
- **Bleib in Bewegung.** Die Rakete des Bosses ist gerade und ungelenkt: Ein Schiff, das in Bewegung bleibt, weicht ihr aus, eines, das stillsteht, wird getroffen.
- **Bring eine Gruppe mit.** Drei Piloten in Ostirions mit x2-Munition schaffen ihn auf `x-2`, ohne ein Schiff zu verlieren, wenn auch nur knapp, und werden auf `x-3` zerstört, auch solange sich die Treffer verteilen; vier schaffen ihn in Alpha in etwa drei Minuten. Mit x4-Munition schaffen ihn auf `x-3` drei in etwa zwei Minuten. Fünf schaffen ihn in etwa zweieinhalb Minuten, wenn sich die Treffer verteilen, und in etwa drei, wenn ein Pilot das ganze Feuer abbekommt, und verlieren dann zwei Schiffe: Eine Gruppe, bei der ein Pilot das ganze Feuer abbekommt, braucht fünf. In Beta braucht es fünf Piloten und in Gamma sieben, bei verteilten Treffern (der Boss ist dort größer und seine Scouts heilen mehr). In Alpha schafft es eine Ostirion allein auf `x-3` mit x2-Munition nicht, eine Paragon allein schafft es auch nicht, und zwei Paragons schaffen es sicher. In Beta und Gamma wird eine einzelne Paragon auf `x-3` mit x2-Munition und mit x4-Munition zerstört. Der Boss wehrt sich gegen den ersten Piloten, der ihn getroffen hat, also soll das robusteste Schiff anfangen; setze in einem so langen Kampf deine Fähigkeiten ein (Emergency Repair, Shield Surge: [Fähigkeiten](/wiki/03-Mechanics/Abilities.md)). Piloten, die noch Level 2 oder 3 sind, sind ihm zu schwach, auch dort, wo sie fliegen: Halte dich fern, bis du stärker bist.
- **Der Boss kehrt zurück**, nach der Zeit in der Liste *Auf einen Blick*, im selben Sektor.

## Die drei Schritte des Anführers {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Sein Kampf hat drei Schritte ([so funktionieren sie](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); jeder geschieht einmal.

- **Am Anfang**: Feuert einen Fächer aus 3 Raketen im Abstand von 12 Grad auf den ersten Piloten, der es getroffen hat.
- **Unter zwei Dritteln**: Ruft 5 weitere Pirate Scouts auf einmal, höchstens 10 am Leben. Sie zahlen nichts und gehen nach 45 s.
- **Unter einem Drittel**: Fliegt mit ×1,8 Geschwindigkeit für 10 s zum nächsten Tor und wendet sich dann gegen die Piloten.

<!-- mob-ladder:end -->

## Belohnungen und Beute {#rewards-and-drops}

Der Pirate Boss zahlt für den Kampf, der er ist: Eine Minute Kampf gegen ihn zahlt mehr als eine Minute Kampf gegen einen Goombah. Die Bezahlung wird nach Schaden unter den Piloten aufgeteilt, die ihn bekämpft haben ([so zahlt ein Boss-Abschuss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Seine Kiste gehört dem Piloten mit dem meisten Schaden und kann eine **Reinforced Hull Plate**, Raketen und Munition enthalten. Seine Kiste ist etwas weniger als die Hälfte dessen wert, was der Abschuss selbst zahlt. Die Scouts zahlen wenig und lassen nichts fallen.

## Die Werte {#the-numbers}

Die Werte der Schwarmschiffe in den drei Welten ([Welten](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss

Basis: Ironclad mit 50 % von Hülle, Schild und Schaden; Tempo und Reichweite bleiben die des Vorbilds. Feuert alle 5 s eine gerade Rakete ab: [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) in `x-2`, [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) in `x-3`.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | {{guide:vitals.hull@Pirate Boss#1}} | {{guide:vitals.hull@Pirate Boss#2}} | {{guide:vitals.hull@Pirate Boss#3}} |
| Schild | {{guide:vitals.shield@Pirate Boss#1}} | {{guide:vitals.shield@Pirate Boss#2}} | {{guide:vitals.shield@Pirate Boss#3}} |
| Laserschaden (eine Salve pro Sekunde) | keiner | keiner | keiner |
| Tempo | {{guide:vitals.speed@Pirate Boss#1}} | {{guide:vitals.speed@Pirate Boss#2}} | {{guide:vitals.speed@Pirate Boss#3}} |
| Laserreichweite | – | – | – |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Raketenschaden, höchstens | {{guide:behaviour.ability:rocket.damage@Pirate Boss#1}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#2}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#3}} |
| Credits | {{guide:spoils.pay.credits@Pirate Boss#1}} | {{guide:spoils.pay.credits@Pirate Boss#2}} | {{guide:spoils.pay.credits@Pirate Boss#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Boss#1}} | {{guide:spoils.pay.thulium@Pirate Boss#2}} | {{guide:spoils.pay.thulium@Pirate Boss#3}} |
| Erfahrung (EP) | {{guide:spoils.pay.experience@Pirate Boss#1}} | {{guide:spoils.pay.experience@Pirate Boss#2}} | {{guide:spoils.pay.experience@Pirate Boss#3}} |
| Ehre | {{guide:spoils.pay.honor@Pirate Boss#1}} | {{guide:spoils.pay.honor@Pirate Boss#2}} | {{guide:spoils.pay.honor@Pirate Boss#3}} |
| PvE-Punkte pro Abschuss | 15 | 15 | 15 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand |
| :--- |
| {{guide:spoils.box@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} |

### Pirate Scout

Basis: Kitefin mit 50 % der Hülle und 113 % des Laserschadens; Tempo und Reichweite bleiben die des Vorbilds.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | {{guide:vitals.hull@Pirate Scout#1}} | {{guide:vitals.hull@Pirate Scout#2}} | {{guide:vitals.hull@Pirate Scout#3}} |
| Schild | {{guide:vitals.shield@Pirate Scout#1}} | {{guide:vitals.shield@Pirate Scout#2}} | {{guide:vitals.shield@Pirate Scout#3}} |
| Laserschaden (eine Salve pro Sekunde) | {{guide:vitals.dps@Pirate Scout#1}} | {{guide:vitals.dps@Pirate Scout#2}} | {{guide:vitals.dps@Pirate Scout#3}} |
| Tempo | {{guide:vitals.speed@Pirate Scout#1}} | {{guide:vitals.speed@Pirate Scout#2}} | {{guide:vitals.speed@Pirate Scout#3}} |
| Laserreichweite | 700 | 700 | 700 |
| Aggro-Radius | {{guide:vitals.aggro@Pirate Scout#1}} | {{guide:vitals.aggro@Pirate Scout#2}} | {{guide:vitals.aggro@Pirate Scout#3}} |
| Heilt den Anführer, je Begleiter, pro Sekunde (nur Hülle) | 40 | 60 | 80 |
| Credits | {{guide:spoils.pay.credits@Pirate Scout#1}} | {{guide:spoils.pay.credits@Pirate Scout#2}} | {{guide:spoils.pay.credits@Pirate Scout#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Scout#1}} | {{guide:spoils.pay.thulium@Pirate Scout#2}} | {{guide:spoils.pay.thulium@Pirate Scout#3}} |
| Erfahrung (EP) | {{guide:spoils.pay.experience@Pirate Scout#1}} | {{guide:spoils.pay.experience@Pirate Scout#2}} | {{guide:spoils.pay.experience@Pirate Scout#3}} |
| Ehre | {{guide:spoils.pay.honor@Pirate Scout#1}} | {{guide:spoils.pay.honor@Pirate Scout#2}} | {{guide:spoils.pay.honor@Pirate Scout#3}} |
| PvE-Punkte pro Abschuss | 4 | 4 | 4 |

**Beute**: keine. Der Abschuss zahlt nur seine Credits, sein Thulium, seine EP und seine Ehre.

<!-- pirate-members:end -->
