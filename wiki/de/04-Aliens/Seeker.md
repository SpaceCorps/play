<!-- wiki-i18n source: d1f973df95aefca8 -->
<!-- wiki-i18n title: Seeker -->
# Seeker {#seeker}

Seeker sind einfache Späh- und Aufklärungseinheiten. Sie sind passiv, beginnen also nie einen Kampf: Ein Seeker wendet sich gegen den Piloten, der auf ihn schießt, und nur gegen diesen. Er lässt ab, wenn ihn 10 Sekunden lang niemand getroffen hat, und seine Hülle repariert sich, sobald man ihn 30 Sekunden in Ruhe gelassen hat. Der Boss Seeker und die Seeker Slaves des [Seeker-Schwarms](/wiki/05-Swarms/Seeker-Swarm.md) sehen aus wie Seeker, sind aber Arten für sich: Ihre Abschüsse werden unter ihrem eigenen Namen gezählt, nicht als Seeker-Abschüsse.

## Werte {#stats}

- **Trefferpunkte (HP)**: 800
- **Schild**: 800
- **Schaden**: 180
- **Tempo**: 120
- **Angriffsreichweite**: 600
- **Verhalten**: Passiv

## Verhalten {#behavior}

- Ein Seeker geht nie auf ein Schiff los, das ihm nahe kommt: Er streift umher, bis jemand auf ihn schießt, und verfolgt und beschießt dann den Piloten, der als Erster auf ihn geschossen hat, solange dieser Pilot ihn weiter trifft und er ihn erreichen kann; die Schüsse anderer Piloten bringen ihn währenddessen nicht von seinem Ziel ab, und wenn der Erste ausscheidet, wendet er sich dem nächsten Piloten zu, der in den Kampf eingestiegen ist (siehe [Gegen wen ein Alien kämpft](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)). Das Feuer eines anderen Aliens und ein Treffer, der keinen Schaden anrichtet, provozieren ihn nie.
- Er gibt **10 Sekunden** nach dem letzten Treffer auf, egal von wem, und streift wieder umher. Solange ein Pilot ihn weiter trifft, fliegt er auf diesen Piloten zu, wann immer dieser jenseits der Waffenreichweite des Seeker (600 Einheiten) steht, und feuert, sobald der Pilot in Reichweite ist.
- Er lässt einen Piloten los, wenn dieser mehr als **2.500 Einheiten** von ihm entfernt ist oder wenn er selbst von dem Ort, an dem die Verfolgung begann, **3.000 Einheiten** weit geflogen ist, und geht 8 Sekunden lang nicht wieder auf diesen Piloten los, es sei denn, der Pilot schießt noch einmal auf ihn (siehe [Kampf](/wiki/03-Mechanics/Combat.md)).
- Lässt man ihn **30 Sekunden** in Ruhe, repariert sich seine Hülle um 2 % ihres Maximums pro Sekunde (eine volle Hülle in etwa 50 Sekunden). Sein Schild lädt sich wie bei jedem Alien ab 15 Sekunden nach dem letzten Treffer wieder auf.
- Er kämpft gegen niemanden, der ihn nicht getroffen hat, und ruft nie ein anderes Alien zu Hilfe.
- [Konzernpiloten](/wiki/03-Mechanics/Company-Pilots.md) jagen Seeker. Ein Pilot, der auf einen schießt, zieht dessen Feuer auf sich, es sei denn, der Seeker kämpft bereits gegen jemand anderen.

## Belohnungen {#rewards}

- **Credits**: 800
- **Thulium**: 4
- **Erfahrung (EP)**: 100
- **Ehre**: 2
- **PvE-Punkte pro Abschuss**: 1
- **Schildaufladung**: 10 pro Sekunde (15 s Verzögerung)

## Beute {#loot-drops}

Die Beute fällt als [Frachtkiste](/wiki/03-Mechanics/Cargo.md) dort, wo er explodiert, und gehört 30 Sekunden lang dem Piloten, der ihn abgeschossen hat.

Wofür jede Beute gebraucht wird und wo es sie sonst noch gibt: [Ressourcen](/wiki/06-Items/Resources.md).

- **Ship Fragment**: 20 % Chance (Min.: 1, Max.: 1)
- **Daraxium**: 50 % Chance (Min.: 1, Max.: 2)

## Hintergrund {#lore}

Seeker sind leichte Spähsonden, die der Schwarm der Aliens aussendet, um die Sprungtore der Sektoren zu kartieren und die elektromagnetischen Signaturen menschlicher Flotten aufzuspüren. Mit minimaler Bewaffnung und zerbrechlicher Bauweise sind sie äußerst passiv: Sie ziehen sich zurück oder ignorieren Schiffe, solange niemand auf sie feuert. Sie stimmen sich jedoch mit größeren Kampfeinheiten ab und übermitteln ihre Positionen, wenn sie angegriffen werden.
