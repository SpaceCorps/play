<!-- wiki-i18n source: cddca2909be3ca44 -->
<!-- wiki-i18n title: Schwärme -->
# Schwärme {#swarms}

Ein **Schwarm** ist eine Gruppe von Aliens, die unter einem **Anführer** durch einen Teil der Galaxie streift: einem Boss, weit stärker als jedes Alien um ihn herum, mit **Begleitern**, die ihn bewachen und ihn in zwei der Schwärme heilen. Es gibt drei, und jeder hat einen eigenen Artikel:

- [Seeker-Schwarm](/wiki/05-Swarms/Seeker-Swarm.md): der Boss Seeker und seine Seeker Slaves, der kleinste Schwarm, in den Sektoren, in denen neue Piloten fliegen.
- [Pirate-Schwarm](/wiki/05-Swarms/Pirate-Swarm.md): der Pirate Boss und seine Pirate Scouts, ein langer Kampf für eine Gruppe.
- [Dormant-Schwarm](/wiki/05-Swarms/Dormant-Swarm.md): die Dormant Force und ihre Dormant Pulses, der stärkste Schwarm, mit der reichsten Beute.

Ihre Schiffe sind **Aliens eigener Arten**: Sie haben eigene Namen und eigene Abschusszähler, und keines von ihnen zählt als Seeker, Phantasm oder irgendein anderes Alien. Ein Schwarmschiff hat die Gestalt des Schiffs, auf dem es aufbaut, in einer eigenen Färbung und mit seinem Namen darüber; der Boss Seeker ist ein viel größerer Seeker.

## Die drei Schwärme {#the-three-swarms}

<!-- swarms-list:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Schwarm | Wo | Wie viele | Anführer | Begleiter | Kehrt zurück |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**Pirate-Schwarm**](/wiki/05-Swarms/Pirate-Swarm.md) | Die Sektoren `x-2` und `x-3` jedes Konzerns | Einer in jedem dieser Sektoren, 6 in jeder Welt | **Pirate Boss** | Bis zu 5 × Pirate Scout, alle 10 s ein neuer | 2 min nach der Zerstörung des Anführers, im selben Sektor |
| [**Dormant-Schwarm**](/wiki/05-Swarms/Dormant-Swarm.md) | Die Gefahrensektoren `DS-1`, `DS-2`, `DS-3`, `DS-4`, von einem zum anderen fliegend | Einer in jeder Welt | **Dormant Force** | 2 × Dormant Pulse, die mit dem Anführer fliegen | 1 h nach der Zerstörung des ganzen Schwarms, in einem zufälligen Gefahrensektor |
| [**Seeker-Schwarm**](/wiki/05-Swarms/Seeker-Swarm.md) | Die Sektoren `x-1` und `x-2` jedes Konzerns | Einer in jedem dieser Sektoren, 6 in jeder Welt | **Boss Seeker** | Bis zu 4 × Seeker Slave, alle 10 s ein neuer | 2 min nach der Zerstörung des Anführers, im selben Sektor |

<!-- swarms-list:end -->

## Wann und wo {#when-and-where}

Die Schwärme tauchen ab dem **Erstkontakt** auf und bleiben bis zum Wipe (siehe die [Wipe-Zeitleiste](/wiki/03-Mechanics/Wipe-Timeline.md); den Tag nennt die erste Zeile der Regeln unten). **Jede Welt hat ihre eigenen Schwärme** an denselben Orten: Der Pirate Boss von Alpha und der von Beta sind zwei verschiedene Schiffe, und ein Schwarm, den du in deiner Welt zerstörst, bleibt in einer anderen bestehen. Ein zerstörter Schwarm kehrt nach der Zeit in der Tabelle oben zurück.

## Die Regeln jedes Schwarms {#the-rules-of-every-swarm}

<!-- swarms-rules:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- Die Schwärme erscheinen ab Saisontag 4 bis zum Wipe.
- Wird ein Schwarmschiff getroffen, greifen die Schiffe seines Schwarms im Umkreis von 1.500 Einheiten gegen den ersten Piloten ein, der es getroffen hat.
- Ein Anführer erscheint mindestens 2.500 Einheiten vom Rand jedes Stations- und Torrings entfernt.
- Ein Pilot, der mindestens 5 % des Schadens an einem Boss angerichtet hat, wird für dessen Abschuss bezahlt.

<!-- swarms-rules:end -->

## Die Welten {#the-worlds}

Die Welt skaliert einen Schwarm wie jedes Alien ([Welten](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): Hülle, Schild, Schildaufladung, Laserschaden, Raketenschaden und Heilung eines Schwarmschiffs sind die Werte von Alpha mal der Stärke unten, und ein Abschuss zahlt die Bezahlung unten. Tempo, Reichweite und Beute sind in jeder Welt gleich. Die Artikel nennen die Werte jedes Schiffs in allen drei Welten.

<!-- swarms-world:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Welt | Stärke | Bezahlung |
| :--- | ---: | ---: |
| **Alpha** | ×1 | ×1 |
| **Beta** | ×1,5 | ×2 |
| **Gamma** | ×2 | ×3 |

<!-- swarms-world:end -->

## Was die Piloten erfahren {#what-the-pilots-are-told}

Der Seeker- und der Pirate-Schwarm melden den Piloten ihres Sektors im Chat, wenn ein Boss auftaucht und wenn er zerstört wird. Der Dormant-Schwarm meldet es seiner ganzen Welt, und er ist auf den Karten der Gefahrensektoren und auf der Galaxiekarte markiert, damit Piloten ihn finden können. Der Abschuss eines Bosses bekommt außerdem eine Zeile im Kill-Feed, die den Piloten nennt, dem er gutgeschrieben wird. Die Liste *Auf einen Blick* jedes Artikels sagt, wer informiert wird.

## Einen Schwarm bekämpfen {#fighting-a-swarm}

- **Die Anführer beginnen nie einen Kampf.** Ein Anführer streift umher, bis ein Pilot ihn trifft, wehrt sich dann, und die Schiffe seines Schwarms in seiner Nähe greifen mit ein, und zwar gegen den ersten Piloten, der ihn getroffen hat (die Entfernung steht in den Regeln oben). Die Pirate Scouts sind die Ausnahme: Sie greifen jeden Piloten an, der ihnen nahe kommt. Ein Anführer repariert seine Hülle nie von selbst, der Schaden, den du angerichtet hast, bleibt also auf ihm, es sei denn, seine Begleiter heilen ihn; sein Schild lädt sich wie bei jedem Alien wieder auf.
- **Schwarmschiffe bekämpfen nur Piloten.** Sie schießen nicht auf Aliens, und Aliens schießen nicht auf sie, und [Konzernpiloten](/wiki/03-Mechanics/Company-Pilots.md) ignorieren sie: Sie jagen kein Schwarmschiff und kommen dir auch nicht gegen eines zu Hilfe.
- **Raketen.** Der Pirate Boss sowie die Dormant Force und die Pulses feuern **gerade** Raketen, [Rivet-Raketen](/wiki/06-Items/Rockets.md), auf den Piloten, der sie angegriffen hat. Ein Schiff, das in Bewegung bleibt, weicht ihnen aus, eines, das stillsteht, wird getroffen.
- **Die Größe der Kämpfe.** Der Seeker-Schwarm ist etwas für zwei Piloten, der Pirate-Schwarm für eine kleine Gruppe, der Dormant-Schwarm für eine große Gruppe der stärksten Schiffe; die größeren Welten brauchen mehr Piloten, wie bei jedem Alien.

## Was du mitbringen solltest {#what-to-bring}

- **Eine Gruppe.** Fliege in einer [Gruppe](/wiki/03-Mechanics/Groups.md): Die Schwärme sind auf Gruppen abgestimmt, ein einzelner Pilot niedriger Stufe wird schnell zerstört, und nur die stärksten Schiffe können einen Pirate Boss allein besiegen. Den Dormant-Schwarm besiegt niemand allein. Ein Schwarm kämpft gegen den ersten Piloten, der ihn getroffen hat ([Gegen wen ein Alien kämpft](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)), also soll das robusteste Schiff der Gruppe anfangen.
- **Bessere Munition.** Nimm x2-Munition oder besser mit (siehe [Laser & Munition](/wiki/06-Items/Lasers.md)). Die Heilung der Begleiter eines Schwarms kann mehr sein, als eine kleine Gruppe mit x1-Munition austeilt.
- **Schilde und Reparaturen** für einen langen Kampf: Die Fähigkeiten deines Schiffs ([Fähigkeiten](/wiki/03-Mechanics/Abilities.md)) zählen am meisten im Kampf gegen die Piraten, der Minuten dauert.
- **Platz zum Ausweichen.** Bleib außerhalb der Reichweite einer Waffe, die weniger weit reicht als deine, und bleib gegen eine Rakete in Bewegung.

## Wie ein Boss-Abschuss bezahlt {#how-a-boss-kill-pays}

Ein gewöhnliches Alien zahlt an den Piloten, der es zuerst getroffen hat ([Kampf](/wiki/03-Mechanics/Combat.md#kill-rewards-first-hit-claims)). Der Anführer eines Schwarms und jede Dormant Pulse zahlen stattdessen **nach dem angerichteten Schaden**:

- **Die Bezahlung wird nach Schaden aufgeteilt.** Jeder Pilot, der mindestens den Anteil aus den Regeln oben angerichtet hat, wird bezahlt, im Verhältnis zu seinem Schaden: Credits, Thulium, EP und Ehre des Abschusses werden unter ihnen aufgeteilt. Ein Pilot unter dem Anteil bekommt nichts.
- **Die Frachtkiste geht an den Piloten mit dem meisten Schaden.** Sie gehört 30 Sekunden lang diesem Piloten (und seinem Clan), wie bei jedem Alien, danach kann sie jeder nehmen ([Frachtkisten](/wiki/03-Mechanics/Cargo.md)). Jedes Dormant-Schiff hat seine eigene Schadenszählung und seine eigene Kiste.
- **Begleiter zahlen wie üblich**: Die Pirate Scouts und die Seeker Slaves zahlen an den Piloten, der sie zuerst getroffen hat, und ihre Bezahlung ist klein gegen die eines Bosses.
- **Die Bezahlung eines Bosses soll die Aliens um ihn herum übertreffen.** Eine Minute Kampf gegen einen Pirate Boss zahlt mehr als eine Minute Kampf gegen einen Goombah, und der Dormant-Schwarm zahlt noch mehr; der Boss Seeker zahlt genau zehn Seeker.

Jeder Abschuss wird unter dem eigenen Namen des Schiffs in deiner Abschussstatistik gezählt und bringt PvE-Punkte für deine Rangliste:

<!-- swarms-points:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Schwarmschiff | Schwarm | PvE-Punkte pro Abschuss |
| :--- | :--- | ---: |
| **Pirate Boss** | Pirate-Schwarm | 10 |
| **Pirate Scout** | Pirate-Schwarm | 1 |
| **Dormant Force** | Dormant-Schwarm | 25 |
| **Dormant Pulse** | Dormant-Schwarm | 10 |
| **Boss Seeker** | Seeker-Schwarm | 5 |
| **Seeker Slave** | Seeker-Schwarm | 1 |

<!-- swarms-points:end -->

Ein Schwarmabschuss zählt nicht als Abschuss eines anderen Aliens: Ein Boss Seeker oder ein Seeker Slave ist für einen Auftrag, der Seeker verlangt, kein Seeker, und die Meilensteine der Wipe-Punkte ([Wipe-Zeitleiste](/wiki/03-Mechanics/Wipe-Timeline.md#earning-wipe-points)) gelten nur für die fünf Aliens.
